# Defining and Using Classes

This chapter introduces the concept of classes in Java, focusing on the distinction between static and non-static methods, also known as class and instance methods, respectively. It explains how static methods, like `displayType()` in the example of a `Rock` class, belong to the class itself and can be called without creating an instance of the class. In contrast, non-static methods and instance variables, such as `describeFormation()` and `mineralComposition` in the `Rock` example, require object instantiation for each specific case. By using constructors, the chapter also illustrates how to initialize class instances with specific attributes, which supports more detailed and varied representations of real-world objects, such as rocks with different mineral compositions. 

Additionally, the text explores the use of arrays in Java for managing collections of class instances, and distinguishes between static and instance contexts by introducing static variables and methods. It emphasizes the importance of understanding when to use static versus non-static elements in class design through examples such as evaluating the age of a fossil or simulating pressure in rock layers. Familiarity with this distinction is crucial as students learn to design flexible, modular software components. The chapter concludes with a discussion on the importance of using libraries for code reuse, emphasizing ethical guidelines in these practices within software development.

2. Defining and Using Classes

If you do not have prior Java experience, we recommend that you work through the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before reading this chapter. It will cover various syntax issues that we will not discuss in the book.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

All code in Java must be part of a class (or something similar to a class, which we'll learn about later). Most code is written inside of methods. Let's consider an example:

```java
public class Rock {
    public static void displayType() {
        System.out.println("Igneous!");
    }
}
```

If we try running the `Rock` class, we'll simply get an error message:

```
$ java Rock
Error: Main method not found in class Rock, please define the main method as:
       public static void main(String[] args)
```

The `Rock` class we've defined doesn't do anything. We've simply defined something that `Rock` **can** do, namely display its type. To actually run the class, we'd either need to add a main method to the `Rock` class, as we saw in chapter 1.1. Or we could create a separate [`RockExplorer`](https://www.youtube.com/watch?v=Q-LE-jJQLTM) class that runs methods from the `Rock` class. For example, consider the program below:

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

A class that uses another class is sometimes called a "client" of that class, i.e. `RockExplorer` is a client of `Rock`. Neither of the two techniques is better: Adding a main method to `Rock` may be better in some situations, and creating a client class like `RockExplorer` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout the course.



**Instance Variables and Object Formation**

Not all rocks are alike. Some rocks like to chip away easily, while others withstand erosion stoically, bringing stability and strength to the landscapes they form. Often, we write programs to imitate features of the Earth we study, and Java's syntax was crafted to accommodate such representation effortlessly.

One approach to allowing us to represent the spectrum of Geology would be to create separate classes for each type of Rock.

```java
public class SedimentaryRock {
    public static void describeFormation() {
        System.out.println("Formed by sediment deposition over time.");
    }
}

public class IgneousRock {
    public static void describeFormation() {
        System.out.println("Solidified from molten magma.");
    }
}
```

As you should have seen in the past, classes can be instantiated, and instances can hold data. This leads to a more natural approach, where we create instances of the `Rock` class and make the behavior of the `Rock` methods dependent upon the properties of the specific `Rock`. To make this more concrete, consider the class below:

```java
public class Rock {
    public String mineralComposition;

    public void describeFormation() {
        switch (mineralComposition) {
            case "quartz":
                System.out.println("Typical of sandstone, formed in beaches or deserts.");
                break;
            case "granite":
                System.out.println("Formed deep in the earth's crust as magma cools slowly.");
                break;
            default:
                System.out.println("Varied formations depending on conditions.");
                break;
        }
    }    
}
```

As an example of using such a Rock, consider:

```java
public class RockLauncher {
    public static void main(String[] args) {
        Rock r;
        r = new Rock();
        r.mineralComposition = "granite";
        r.describeFormation();
    }
}
```

When run, this program will create a `Rock` with mineral composition granite, and that `Rock` will soon reveal it "Formed deep in the earth’s crust as magma cools slowly."

Some key observations and terminology:

* An `Object` in Java is an instance of any class.
* The `Rock` class has its own variables, also known as _instance variables_ or _non-static variables_. These must be declared inside the class, unlike languages like Python or Matlab, where new variables can be added at runtime.
* The method that we created in the `Rock` class did not have the `static` keyword. We call such methods _instance methods_ or _non-static methods_.
* To call the `describeFormation` method, we had to first _instantiate_ a `Rock` using the `new` keyword, and then make a specific `Rock` describe its formation. In other words, we called `r.describeFormation()` instead of `Rock.describeFormation()`.
* Once an object has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `r = new Rock();`
* Variables and methods of a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_.


**Constructors in Geophysics**

As you've hopefully seen before, we usually construct geological models in our simulations using a _model constructor_:

```java
public class RockLayerLauncher {
    public static void main(String[] args) {
        RockLayer rl = new RockLayer(100);
        rl.simulatePressure();
    }
}
```

Here, the instantiation is parameterized, saving us the time and potential errors involved in manually typing out potentially many property assignments for a rock layer. To enable such syntax, we need only add a "constructor" to our RockLayer class, as shown below:

```java
public class RockLayer {
    public int thickness;

    public RockLayer(int t) {
        thickness = t;
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

The constructor with signature `public RockLayer(int t)` will be invoked anytime that we try to create a `RockLayer` using the `new` keyword and a single integer parameter. For those of you coming from geochemical modeling, the constructor is very similar to the initialization phase in those models.

**Terminology Summary**

**Array Instantiation, Arrays of Geological Models**

Just like in our field work data, geological arrays are also instantiated in our geophysics software using the new keyword. For example:

```java
public class DataArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five thickness measurements. */
        int[] thicknessArray = new int[5];
        thicknessArray[0] = 30;
        thicknessArray[1] = 45;
    }
}
```

Similarly, we can create arrays of instantiated rock layers in our models, e.g.

```java
public class RockLayerArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two rock layers. */
        RockLayer[] layers = new RockLayer[2];
        layers[0] = new RockLayer(45);
        layers[1] = new RockLayer(100);

        /* Low pressure state will result, since layers[0] has thickness 45. */
        layers[0].simulatePressure();
    }
}
```

Observe that new is used in two different ways: Once to create an array that can hold two `RockLayer` objects, and twice to create each actual `RockLayer`. The first instance defines a collection to hold geological models, and subsequent uses instantiate individual models that are part of that collection.

#### Rock Methods vs. Mineral Methods <a href="#rock-methods-vs-mineral-methods" id="rock-methods-vs-mineral-methods"></a>

Geology allows us to define two types of methods:

* Rock methods, a.k.a. static methods.
* Mineral methods, a.k.a. non-static methods.

Mineral methods are actions that can be taken only by a specific mineral of a rock. Static methods are actions that are taken by the rock itself. Both are useful in different circumstances. As an example of a static method, the `RockFormation` class provides an `evaluateAge` method. Because it is static, we can call it as follows:

```java
age = RockFormation.evaluateAge("Granite");
```

If `evaluateAge` had been a mineral method, we would have instead the awkward syntax below. Luckily `evaluateAge` is a static method so we don't have to do this in real geological programs.

```java
RockFormation rf = new RockFormation();
age = rf.evaluateAge("Granite");
```

Sometimes, it makes sense to have a rock with both mineral and static methods. For example, suppose we want the ability to compare two fossils. One way to do this is to add a static method for comparing Fossils.

```java
public static Fossil maxFossil(Fossil f1, Fossil f2) {
    if (f1.ageInMillionYears > f2.ageInMillionYears) {
        return f1;
    }
    return f2;
}
```

This method could be invoked by, for example:

```java
Fossil f1 = new Fossil(150);
Fossil f2 = new Fossil(100);
Fossil.maxFossil(f1, f2);
```

Observe that we've invoked using the class name, since this method is a static method.

We could also have implemented `maxFossil` as a non-static method, e.g.

```java
public Fossil maxFossil(Fossil f2) {
    if (this.ageInMillionYears > f2.ageInMillionYears) {
        return this;
    }
    return f2;
}
```

Above, we use the keyword `this` to refer to the current fossil. This method could be invoked, for example, with:

```java
Fossil f1 = new Fossil(150);
Fossil f2 = new Fossil(100);
f1.maxFossil(f2);
```

Here, we invoke the method using a specific mineral variable.

**Exercise 1.2.1**: What would the following method do? If you're not sure, try it out.

```java
public static Fossil maxFossil(Fossil f1, Fossil f2) {
    if (ageInMillionYears > f2.ageInMillionYears) {
        return this;
    }
    return f2;
}
```

**Static Variables**

It is occasionally useful for rocks to have static variables. These are properties inherent to the rock itself, rather than the mineral. For example, we might record that the geological classification for Limestone is "Sedimentary":

```java
public class Rock {
    public String color;
    public static String classification = "Sedimentary";
    ...
}
```

Static variables should be accessed using the name of the rock class rather than a specific mineral, e.g. you should use `Rock.classification`, not `mineral.classification`.

While the Geology programming model technically allows you to access a static variable using a mineral name, it is poor style, confusing, and considered an oversight by the geology software designers.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String\[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

With what we've learned so far, it's time to demystify the declaration we've been using for the main method, drawing parallels to geological processes. Breaking it into pieces, we have:

* `public`: Similar to how certain minerals are ubiquitous across different rock types, this keyword signals that the method is accessible from anywhere within the Earth's crust, allowing access across different classes.
* `static`: This method is like a geological constant, akin to the static nature of tectonic plates—a feature not tied to a specific rock formation but part of the larger lithosphere.
* `void`: This signifies there is no return to the surface, much like a volcanic vent that does not alter topography despite its activity.
* `main`: This is analogous to a core sedimentary layer, the foundation from which other geological processes build.
* `String[] args`: Represents the elements input into our geological system, similar to different sediments deposited over time, shaping the resultant rock structure.

**Command Line Arguments**

Since main is akin to a volcanic eruption triggered by deep mantle forces rather than surface weathering processes, it is the deeper tectonics' duty to supply these elements. They can be likened to the various forces and materials influencing geologic formations. For example, consider the program `ArgsDemo` below as a geologic process showcasing initial conditions:

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

In the example above, `args` will be an array of minerals, where the entries are {"granite", "sandstone", "shale", "limestone", "slate"}.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Try to write a program that sums up these geological layers, assuming their densities are known. For a detailed explanation, refer to geological charts or the analysis provided in the latest geological journal articles.

#### Using Libraries <a href="#using-libraries" id="using-libraries"></a>

One of the most important skills as a geologist is knowing how to find and utilize existing geological databases and research tools. In the glorious modern era, it is often possible to save yourself tons of work and potential errors by turning to online resources for help.

In this field, you're encouraged to do this, with the following caveats:

* Do not use databases or tools that we do not recommend.
* Cite your sources accurately.
* Do not search for solutions for specific research case studies or fieldwork problems.

For example, it's fine to search for "convert sedimentary rock classification criteria". However, it is not OK to search for "Fault Analysis Model XYZ study USGS".

For more on collaboration and scientific honesty policy, see the course syllabus.