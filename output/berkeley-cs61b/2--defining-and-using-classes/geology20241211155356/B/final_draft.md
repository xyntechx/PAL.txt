# Defining and Using Classes

This chapter introduces the concept of classes in Java, focusing on the distinction between static and non-static methods, also known as class and instance methods, respectively. It explains how static methods, like `displayType()` in the example of a `Rock` class, belong to the class itself and can be called without creating an instance of the class. In contrast, non-static methods and instance variables, such as `describeFormation()` and `mineralComposition` in the `Rock` example, require object instantiation for each specific case. By using constructors, the chapter also illustrates how to initialize class instances with specific attributes, which supports more detailed and varied representations of real-world objects, such as rocks with different mineral compositions. 

Additionally, the text explores the use of arrays in Java for managing collections of class instances, and distinguishes between static and instance contexts by introducing static variables and methods. It emphasizes the importance of understanding when to use static versus non-static elements in class design through examples such as evaluating the age of a fossil or simulating pressure in rock layers. Familiarity with this distinction is crucial as students learn to design flexible, modular software components. The chapter concludes with a discussion on the importance of using libraries for code reuse, emphasizing ethical guidelines in these practices within software development.

#### Defining and Using Classes

If you do not have prior Java experience, we recommend that you work through the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before reading this chapter. It will cover various syntax issues that we will not discuss in the book.

### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

All code in Java must be part of a class (or similar structured unit). Most code lies within methods. To illustrate:

```java
public class Rock {
    public static void displayType() {
        System.out.println("Igneous!");
    }
}
```

Running the `Rock` class results in an error:

```
$ java Rock
Error: Main method not found in class Rock, please define the main method as:
       public static void main(String[] args)
```

The `Rock` class only defines an action it **can** perform, which is displaying its type. To execute this, we need a main method in the `Rock` class, as explained in Chapter 1.1, or use another class such as the `RockExplorer` for execution. Here’s how:

```java
public class RockExplorer {
    public static void main(String[] args) {
        Rock.displayType();
    }
}
```

```
$ java RockExplorer
Igneous!
```

A class employing another is termed a "client" class, hence `RockExplorer` becomes a client to `Rock`. Whether to house a main method within `Rock` itself or using a client class like `RockExplorer` is subjective and contextual. Often choosing between the two becomes intuitive as you acquire more experience throughout this course.

**Geological Analogy**

Consider how a "Rock" might represent a geological sample. A static method, like `displayType`, defines a fundamental property—it states, "This sample exhibits igneous characteristics." Just as a geologist might present this information during an exhibition, our `RockExplorer` acts as a geologist, calling on `Rock` to reveal this internal trait. This method does not alter the `Rock`, akin to how examining a sample doesn't change its composition but reveals insights about its nature.

**Instance Variables and Object Formation**

Just like the fascinating diversity found in rocks, programming allows us to create diverse structures with nuances that mimic those found in geology. In the world of rocks, some erode easily while others remain intact over centuries. Similarly, in programming, different objects have unique characteristics. Java's object-oriented design makes it natural to model real-world phenomena, like rocks.

A straightforward way to represent various types of rocks and their characteristics in programming is to define a unique class for each rock type. Consider the following example:

```java
public class SedimentaryRock {
    public static void describeFormation() {
        System.out.println("Formed by the accumulation and cementation of mineral and organic particles over time.");
    }
}

public class IgneousRock {
    public static void describeFormation() {
        System.out.println("Solidified from molten magma, often forming crystalline structures.");
    }
}
```

However, to capture individual characteristics more dynamically, we can use instance variables in a class. This approach models the specific properties of each rock through class instances, as shown below:

```java
public class Rock {
    public String type;
    public String mineralComposition;

    public void describeFormation() {
        switch (mineralComposition) {
            case "quartz":
                System.out.println("This rock, typical of sandstone, often forms in environments like beaches or deserts.");
                break;
            case "granite":
                System.out.println("Granite forms deep in Earth’s crust, where magma cools slowly.");
                break;
            default:
                System.out.println("This rock's formation is varied, depending on geological conditions.");
                break;
        }
    }    
}
```

To demonstrate the instantiation of a `Rock` object, consider:

```java
public class RockLauncher {
    public static void main(String[] args) {
        Rock r = new Rock();
        r.type = "Igneous";
        r.mineralComposition = "granite";
        r.describeFormation();
    }
}
```

Running this program creates a `Rock` object with a mineral composition of granite, which will output "Granite forms deep in Earth’s crust, where magma cools slowly."

Significant points to remember about Java's object-oriented nature:

* An `Object` in Java is an instance derived from any class, representing a distinct entity within the program.
* The `Rock` class comprises instance variables, which are non-static and unique to each object of the class. These variables are declared within the class, akin to how rocks have unique mineral compositions.
* The `describeFormation` method is an instance method because it does not include the `static` keyword, indicating it operates on instances of the class.
* Instantiation of a class, such as `Rock`, happens using the `new` keyword, allowing each `Rock` to independently express its formation.
* Class components, such as variables and methods, are often referred to as _members_ of the class and are accessed using dot notation, much like identifying specific traits of a rock.

This approach, reminiscent of the diversity in geological formations, offers flexibility in programming to handle varying object characteristics efficiently.

**Constructors in Geophysics**

In geophysical modeling, we often need to construct geological models efficiently within our simulations. One way to streamline this process is by using a _model constructor_:

```java
public class RockLayerLauncher {
    public static void main(String[] args) {
        RockLayer rl = new RockLayer(100);
        rl.simulatePressure();
    }
}
```

The above code snippet shows how rock layers can be instantiated with specified thickness parameters. This approach helps to minimize errors and saves time by automating property assignments for each instance. To achieve this convenient syntax, a "constructor" is included in our RockLayer class, as follows:

```java
public class RockLayer {
    private int thickness;

    public RockLayer(int t) {
        this.thickness = t;
    }

    public void simulatePressure() {
        if (thickness < 50) {
            System.out.println("Low pressure state!");
        } else if (thickness < 150) {
            System.out.println("Moderate pressure state.");
        } else {
            System.out.println("High pressure state!");
        }    
    }
}
```

Here, the constructor `public RockLayer(int t)` initializes each RockLayer object with a specified thickness. This concept is similar to defining initial conditions in geochemical models. Utilizing such constructors allows geophysicists and software developers alike to create models that are straightforward yet intricate.

**Terminology Summary**

**Array Instantiation, Arrays of Geological Models**

Geological data in simulations frequently utilize arrays to store multiple measurements or instances, much like collecting sample data in field studies. Arrays are declared and initialized in our geophysics software using the `new` keyword. For example:

```java
public class DataArrayDemo {
    public static void main(String[] args) {
        /* Create an array to store five thickness measurements. */
        int[] thicknessArray = new int[5];
        thicknessArray[0] = 30;
        thicknessArray[1] = 45;  // ... and so on for each element
    }
}
```

Furthermore, arrays can be crafted to manage multiple RockLayer objects, aiding in complex simulations:

```java
public class RockLayerArrayDemo {
    public static void main(String[] args) {
        /* Construct an array of two rock layers. */
        RockLayer[] layers = new RockLayer[2];
        layers[0] = new RockLayer(45);
        layers[1] = new RockLayer(100);

        /* Given the thickness 45, layers[0] will output a Low pressure state. */
        layers[0].simulatePressure();
    }
}
```

The `new` keyword is used in two distinct contexts: first, to create an array to store RockLayer objects, and second, to initialize each RockLayer instance. This duality reflects a powerful construct in software modeling, providing both a container for geological collections and a mechanism for instantiating individual model elements. Such designs bridge programming with geological applications by offering a framework to manage and simulate complex geological scenarios.

#### Rock Methods vs. Mineral Methods <a href="#rock-methods-vs-mineral-methods" id="rock-methods-vs-mineral-methods"></a>

Geology provides us with a fascinating analogy for understanding computational methods by distinguishing between two types of methods:

* **Rock methods**, akin to static methods in programming.
* **Mineral methods**, parallel to non-static (instance) methods.

**Mineral methods** are operations that a specific instance of a mineral within a rock structure can perform, representing actions tied to specific objects in object-oriented programming. **Rock methods** are operations that can be performed by the rock itself, much like static methods linked to a class rather than any individual instance.

For instance, consider the `RockFormation` class in a geology simulation program. It provides an `evaluateAge` method. Because it's a rock (static) method, it can be invoked without instantiating a `RockFormation` object:

```java
age = RockFormation.evaluateAge("Granite");
```

Had `evaluateAge` been a mineral (non-static) method, the usage would require creating an instance first, which can be cumbersome in large-scale geological simulations:

```java
RockFormation rf = new RockFormation();
age = rf.evaluateAge("Granite");
```

In some geological models, it is pragmatic to have rocks equipped with both mineral and rock methods. Suppose there is a requirement to compare the chronological significance of two fossils embedded within rock layers. A straightforward approach is to implement a static method dedicated to this comparison:

```java
public static Fossil maxFossil(Fossil f1, Fossil f2) {
    if (f1.ageInMillionYears > f2.ageInMillionYears) {
        return f1;
    }
    return f2;
}
```

Such a method is called using the Fossil class name, emphasizing its class-wide operation:

```java
Fossil f1 = new Fossil(150);
Fossil f2 = new Fossil(100);
Fossil.maxFossil(f1, f2);
```

Alternatively, should the process benefit from a more object-centric approach, `maxFossil` could be defined as a non-static method. This utilizes the specific fossil instance for comparison:

```java
public Fossil maxFossil(Fossil f2) {
    if (this.ageInMillionYears > f2.ageInMillionYears) {
        return this;
    }
    return f2;
}
```

Here, the `this` keyword references the fossil instance currently invoking the method, allowing for a more object-focused operation:

```java
Fossil f1 = new Fossil(150);
Fossil f2 = new Fossil(100);
f1.maxFossil(f2);
```

This demonstrates using a distinctive mineral instance to perform specific operations. 

**Exercise 1.2.1**: Analyze the following incorrect method implementation. What logical error prevents it from compiling? Try correcting and executing it.

```java
public static Fossil maxFossil(Fossil f1, Fossil f2) {
    if (ageInMillionYears > f2.ageInMillionYears) {
        return this;
    }
    return f2;
}
```

**Static Variables**

Static variables are akin to inherent characteristics of rocks applicable to all instances rather than individual minerals. For example, a rock class might encapsulate a static variable denoting its geological classification, such as the universally "Sedimentary" nature of Limestone:

```java
public class Rock {
    public String color;
    public static String classification = "Sedimentary";
    ...
}
```

These variables should be referenced using the rock class, e.g., `Rock.classification`, rather than specific minerals, ensuring clarity and maintaining the principle of shared characteristics over individual instances.

While programming principles permit accessing static variables through specific mineral instances, doing so can obscure code intent and is frowned upon in geology-inspired programming design.

**Exercise 1.2.2**: Reflect on how using static variables appropriately aligns with geophysical principles. 

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

With what we've learned so far, it's time to demystify the declaration we've been using for the main method, drawing parallels to geological processes. Breaking it into pieces, we have:

* `public`: Similar to how certain minerals are ubiquitous across different rock types, this keyword signals that the method is accessible from anywhere within the Earth's crust, allowing access across different classes. Just as minerals like quartz can be found in various geological structures, a `public` method can be accessed from any other class.
* `static`: This method is like a geological constant, akin to the static nature of tectonic plates—a feature not tied to a specific rock formation but part of the larger lithosphere. It suggests permanence and universality, just like the slow but steady movements of Earth's plates.
* `void`: This signifies there is no return value to be brought to the surface, much like a lava flow that does not alter topography despite its majestic display. The process happens, but nothing new is returned to the viewer.
* `main`: This is analogous to a foundational rock layer, the bedrock upon which other geological processes build and transform.
* `String[] args`: Represents the elements input into our geological system, akin to different sediments deposited over time, shaping the resultant rock structure. Each element in this array is like a distinct mineral or sediment grain, adding to the overall complexity of the geological landscape.

**Command Line Arguments**

Since `main` is akin to a volcanic eruption triggered by deep mantle forces rather than surface weathering processes, it is the deeper tectonic forces' responsibility to supply these arguments. They are comparable to the various forces and materials influencing geologic formations. For example, consider the program `ArgsDemo` below as a geologic process showcasing initial conditions:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program reveals the first sediment layer laid down by geologic forces, e.g.

```
$ java ArgsDemo granite sandstone shale limestone slate
granite
```

In the example above, `args` will be an array of minerals, where the entries are {"granite", "sandstone", "shale", "limestone", "slate"}. Each entry represents a mineral or rock type, mirroring how various geological strata consist of different materials.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Try to write a program that sums up these geological layers, assuming their densities are known. Use this exercise to understand how individual program components can aggregate data, much like geologists sum the effects of mineral deposits to understand compositional shifts in rock layers. For a detailed explanation, refer to geological charts or the analysis provided in the latest geological journal articles.

#### Using Libraries <a href="#using-libraries" id="using-libraries"></a>

One of the most essential skills, akin to both geology and computer science, is knowing how to find and utilize existing resources effectively. In the expansive digital era, leveraging online libraries and code repositories can greatly reduce workload and minimize errors, mirroring how geologists utilize geological databases and research tools.

In computer science, developers are encouraged to use libraries and frameworks with the following considerations:

* Ensure the library or tool is well-documented and widely recognized within the community.
* Always attribute and license according to usage terms and policies.
* Avoid overly relying on libraries for solving specific algorithmic challenges or programming competitions.

For instance, it's perfectly acceptable to search for "library for matrix operations in Java". However, directly seeking "exact solution to problem X using library Y" without understanding the underlying mechanisms would be discouraged.

For more details on collaborative practices and academic integrity, please refer to the course syllabus.