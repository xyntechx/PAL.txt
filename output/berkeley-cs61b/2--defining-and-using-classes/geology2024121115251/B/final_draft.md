# Overview of Geological Classes and Methods

In this chapter, the focus is on defining and utilizing classes within geology-related programming, specifically using Java. The chapter begins by delineating static and non-static methods, illustrating static methods with the `Rock` class example, where a class method `describeFormation` is invoked through a separate `RockLauncher` class. The importance of having a `main` method to execute programs in Java is emphasized, comparing the situational benefits of integrating the `main` method within the class or using a client class to execute methods. The distinction between instance variables and methods is also discussed. Instance variables are non-static variables stored within an object, while instance methods operate on these variables. Through class examples like `Sandstone` and `Granite`, the significance of modeling geological formations with varying attributes, such as hardness, is demonstrated.

Additionally, the chapter covers constructors and their role in efficiently initializing objects with specific properties, such as density, to represent various rock characteristics. The differences between class methods (universal processes) and instance methods (local processes) are outlined, using geology-themed analogies and examples to connect the concepts of method functionality and accessibility. The use of class-wide static variables is explored, emphasizing their role in denoting universal properties inherent to a class type, as illustrated with a `Mineral` class example. Practical exercises reinforce understanding by engaging students with simulations of creating and interacting with arrays of geological models, interpreting main method declarations in Java, and understanding geologic data interpretation through the lens of programming. Finally, it encourages leveraging existing libraries and databases for geological data, outlining ethical considerations for sourcing and collaboration.

2. Defining and Using Geological Classes

If you do not have prior experience in geology, we recommend that you work through the exercises in [GeoHW0](http://sp19.datastructur.es/materials/hw/geohw0/geohw0.html) before reading this chapter. It provides foundational knowledge required to appreciate the geological analogies used in this chapter.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

In geology-related software, akin to geological formations, all code must be organized within a structure, typically a class. Code is primarily implemented through methods, which function like geological processes in defining how aspects work internally. Let's consider an example with a geological context:

```java
public class Rock {
    public static void describeFormation() {
        System.out.println("Igneous!");
    }
}
```

Attempting to run the `Rock` class directly without a main mechanism will result in an error, thus mirroring how a rock would remain unchanged without external intervention:

```
$ java Rock
Error: Main method not found in class Rock, please define the main method as:
       public static void main(String[] args)
```

The `Rock` class we've defined represents the potential of describing formation processes inherent in geological studies. To activate this potential in our programmatic system, you must either modify the `Rock` class by embedding a main method or establish a separate executor class, like `RockLauncher`, which initiates the described method. Here's how:

```java
public class RockLauncher {
    public static void main(String[] args) {
        Rock.describeFormation();
    }
}
```

```
$ java RockLauncher
Igneous!
```

In this arrangement, the `RockLauncher` functions as a "client" or driver of the `Rock` class. This separation can be likened to the relationship between tectonic forces and rock formations — one activates or transforms the other. Deciding whether to incorporate a main method within `Rock` or to create a separate client class like `RockLauncher` depends on the specific requirements of your project environment, similar to choosing a geological approach based on the type of rock formation you're studying. We'll delve deeper into these scenarios as we progress through the course, ensuring clarity in how and when to deploy each method for optimal results. 

Overall, our incorporation of geological concepts serves as an illustrative aid, avoiding complexity while bringing CS concepts into a relatable context, yet always centered around the primary educational goal of mastering CS methodologies.

**Instance Variables and Object Formation**

Just as Earth's rocks exhibit diverse characteristics—from soft and easily eroded forms to resistant against the elements—so too can we create diverse models in the realm of programming to represent these features. Programming languages, like Java, offer us means to mirror such diversity with relative sophistication and precision.

Imagine capturing the essence of various rock formations through distinct classes, each representing a unique geological identity.

```java
public class Sandstone {
    public static void describeFormation() {
        System.out.println("Formed by the compaction and cementation of sand.");
    }
}

public class Granite {
    public static void describeFormation() {
        System.out.println("Crystallized from slowly cooling magma deep below Earth's surface.");
    }
}
```

While it's straightforward to encapsulate rock properties within static classes, programming really shines when we can create instances—individual objects with properties and behaviors. Consider the `Rock` class, where we encapsulate the concept of a rock's hardness and how it informs the rock's classification and resistance.

```java
public class Rock {
    private int hardness;  // hardness is a critical attribute

    public Rock(int hardness) {
        this.hardness = hardness;  // Constructor setting the hardness
    }

    public void describeFormation() {
        if (hardness < 3) {
            System.out.println("Soft sedimentary rock, easily eroded.");
        } else if (hardness < 7) {
            System.out.println("Moderately resistant, often metamorphic.");
        } else {
            System.out.println("Hard igneous rock, very durable.");
        }
    }    
}
```

As an example of utilizing this `Rock` class, consider the program:

```java
public class RockShowcase {
    public static void main(String[] args) {
        Rock quartzite = new Rock(5); // Instantiate with specific hardness
        quartzite.describeFormation();
    }
}
```

Running this program classifies the `quartzite` as "Moderately resistant, often metamorphic," based on its hardness attribute of 5.

Key observations:

* An `Object` in programming is an instance of a class.
* The `Rock` class uses a constructor to initialize its instance variables. Constructors enhance clarity, defining initial values at instance creation.
* The describeFormation method relies on instance-specific data, highlighting the central concept of instance methods.
* Initializing objects via `new` and constructors (`new Rock(5)`) is essential for defining starting states.
* Java's _dot notation_ allows access to methods and variables, e.g., `quartzite.describeFormation()`.

This approach roots abstract programming concepts in tangible analogies, offering clearer entry points into the mechanics of object-oriented programming—akin to studying diverse geological formations to better appreciate Earth's dynamic history.

**Constructors in Geology Simulations**

In geology simulations, we often construct models using a _constructor_, much like how geological formations build over time:

```java
public class RockLauncher {
    public static void main(String[] args) {
        Rock r = new Rock(100);
        r.displayProperties();
    }
}
```

Here, the instantiation process is made more efficient by parameterizing it, akin to sedimentary processes building a rock layer by layer, without manually inputting each property. To achieve this in our code, a "constructor" becomes essential, as demonstrated below:

```java
public class Rock {
    public int densityInKgPerCubicMeter;

    public Rock(int d) {
        densityInKgPerCubicMeter = d;
    }

    public void displayProperties() {
        if (densityInKgPerCubicMeter < 1500) {
            System.out.println("This is a light rock, similar to pumice.");
        } else if (densityInKgPerCubicMeter < 3000) {
            System.out.println("This is a medium density rock, such as limestone.");
        } else {
            System.out.println("This is a dense rock, like basalt.");
        }    
    }
}
```

The constructor `public Rock(int d)` is invoked whenever a `Rock` object is created with the `new` keyword and an integer parameter. For those familiar with Python, think of this as similar to the `__init__` method, which initializes an object's attributes. This allows for a more organized starting point, akin to how tectonic shifts give rise to mountain ranges.

**Terminology Summary**

**Array Instantiation and Arrays of Models**

Arrays in Java, like layers of sedimentary rocks, are created using the `new` keyword. Consider this fundamental process:

```java
public class ArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five integer values representing different densities. */
        int[] someDensities = new int[5];
        someDensities[0] = 2500; // Typical rock density
        someDensities[1] = 2700; // Average density similar to granite
    }
}
```

Similarly, we can establish arrays of instantiated model objects:

```java
public class RockArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two rocks with varying densities. */
        Rock[] rocks = new Rock[2];
        rocks[0] = new Rock(1000);  // Comparable to pumice
        rocks[1] = new Rock(3500);  // Similar to basalt

        /* "Light rock, similar to pumice," will be displayed for rocks[0], given its density. */
        rocks[0].displayProperties();
    }
}
```

Notice how `new` is used: initially to create an array capable of holding two `Rock` objects, followed by its repeated application to instantiate each `Rock`, paralleling geological layering processes. This methodical approach can minimize complexity, like stratigraphy organizing Earth's layers with precision.

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

In geology, we can draw a parallel to computer programming by defining two types of processes:

* **Class methods**, which act like universal geological processes.
* **Instance methods**, which resemble local geological phenomena.

**Instance methods** are akin to geological phenomena that are specific to particular localities or formations, like the unique erosion patterns at a specific coastline. On the other hand, **class methods** represent geological processes observable across various regions and formations, such as the concept of tectonic plate activity.

For illustration, consider a class named `Weathering`. This class might define a universal process called `mechanicalWeathering`, accessible to various rock types:

```java
rate = Weathering.mechanicalWeathering(granite);
```

If `mechanicalWeathering` were a local process, the invocation might look like this:

```java
Weathering w = new Weathering();
rate = w.mechanicalWeathering(granite);
```

In this case, `mechanicalWeathering` is a broad geological process, allowing us to simplify syntax by using the class directly.

Occasionally, it's necessary to compare two minerals using both universal and local processes. For instance, consider adding a universal method to evaluate which of two minerals is harder:

```java
public static Mineral harderMineral(Mineral m1, Mineral m2) {
    if (m1.hardnessScale > m2.hardnessScale) {
        return m1;
    }
    return m2;
}
```

Invoking this would look like:

```java
Mineral quartz = new Mineral(7);
Mineral talc = new Mineral(1);
Mineral.harderMineral(quartz, talc);
```

Here, the method is called using the class, illustrating a universal application.

Alternatively, implementing `harderMineral` as a local process would appear as follows:

```java
public Mineral harderMineral(Mineral m2) {
    if (this.hardnessScale > m2.hardnessScale) {
        return this;
    }
    return m2;
}
```

This local process is initiated on a specific mineral object:

```java
Mineral quartz = new Mineral(7);
Mineral talc = new Mineral(1);
quartz.harderMineral(talc);
```

This differentiation underscores the impact of using specific instances.

**Exercise 1.2.1**: Consider what this method achieves. If unsure, try coding it:

```java
public static Mineral harderMineral(Mineral m1, Mineral m2) {
    if (hardnessScale > m2.hardnessScale) {
        return this;
    }
    return m2;
}
```

**Static Variables**

There are times when a rock type benefits from holding universal properties, inherent to the rock type rather than an individual specimen. For instance, mineral categories shared across all specimens within a class:

```java
public class Mineral {
    public int hardnessScale;
    public static String mineralFamily = "Silicate";
    ...
}
```

Access these universal properties using the class name, as shown:

```java
String family = Mineral.mineralFamily;
```

While possible, accessing via an instance like `quartz.mineralFamily` is considered poor practice due to potential confusion.

**Exercise 1.2.2**: Complete the exercise using these resources:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### Exploring Geologic Events with main Method Concepts <a href="#exploring-geologic-events-with-main-method-concepts" id="exploring-geologic-events-with-main-method-concepts"></a>

Our exploration of the geological phenomenon can be beautifully paralleled with the structure of Java's main method. Each keyword in the method declaration metaphorically connects with geologic principles:

* `public`: Just as tectonic movements impact vast regions and are observable on a global scale, this keyword denotes accessibility to widely dispersed elements.
* `static`: Represents permanence or stability, similar to enduring geological structures like mountains, unyielding to the ebb and flow of external conditions.
* `void`: Symbolizes processes that don't yield direct resources, akin to changes visible only in geological marking rather than matter; no new mineral is extracted, yet the transformation is evident.
* `main`: Envision this as a core geological event, akin to the focal point or epicenter of an earthquake where primary activity unfolds.
* `String[] args`: These are akin to variables or components, much like the multitude of factors in a volcanic eruption, each influencing the process's outcome.

**Geologic Data Interpretation**

Drawing parallels between main methods and geological interpretation involves observing and understanding naturally occurring data, much like geologists decode Earth's narrative. Consider a rudimentary program `RockSampler` designed for field data analysis:

```java
public class RockSampler {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

In this instance, the program outputs initial geological data collected from field studies, for example:

```
$ java RockSampler sedimentary igneous metamorphic types
d
```

Here, `args` stands as an array of String data representing different rock types, namely {"sedimentary", "igneous", "metamorphic", "types"}.

**Summarizing Geological Observations**

**Exercise 1.2.3**: Implement a simulated program to aggregate geological data. Assume this data contains measurable attributes such as mineral composition percentages. Leverage geological simulation libraries or collaborate with equivalent dataset ecosystems to enhance your solution's accuracy and depth.

#### Efficient Use of Resources in Programming <a href="#efficient-use-of-resources-in-programming" id="efficient-use-of-resources-in-programming"></a>

Just as a geologist leverages existing geological databases and resources to minimize redundant fieldwork, a programmer can benefit immensely from utilizing libraries in software development. Libraries contain pre-written code that can perform a wide range of functions, allowing you to focus on building the unique aspects of your project instead of writing everything from scratch.

In this course, you are encouraged to make use of libraries, bearing in mind the following guidelines:

* Stick to pre-approved libraries that we recommend as part of the course materials.
* Properly credit and document any libraries or code snippets you incorporate into your projects.
* Avoid searching explicitly for solutions to specific assignments or coding challenges.

For instance, it's advantageous to find a library for "array manipulation utilities," but not permissible to search for "Solution to problem 4 from Assignment 2." Leveraging libraries responsibly enhances your efficiency without compromising your learning experience.

The course syllabus contains additional guidance on collaboration and academic integrity policies, which are crucial as you progress through your programming journey.