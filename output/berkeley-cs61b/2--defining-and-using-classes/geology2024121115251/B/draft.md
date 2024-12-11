# Overview of Geological Classes and Methods

In this chapter, the focus is on defining and utilizing classes within geology-related programming, specifically using Java. The chapter begins by delineating static and non-static methods, illustrating static methods with the `Rock` class example, where a class method `describeFormation` is invoked through a separate `RockLauncher` class. The importance of having a `main` method to execute programs in Java is emphasized, comparing the situational benefits of integrating the `main` method within the class or using a client class to execute methods. The distinction between instance variables and methods is also discussed. Instance variables are non-static variables stored within an object, while instance methods operate on these variables. Through class examples like `Sandstone` and `Granite`, the significance of modeling geological formations with varying attributes, such as hardness, is demonstrated.

Additionally, the chapter covers constructors and their role in efficiently initializing objects with specific properties, such as density, to represent various rock characteristics. The differences between class methods (universal processes) and instance methods (local processes) are outlined, using geology-themed analogies and examples to connect the concepts of method functionality and accessibility. The use of class-wide static variables is explored, emphasizing their role in denoting universal properties inherent to a class type, as illustrated with a `Mineral` class example. Practical exercises reinforce understanding by engaging students with simulations of creating and interacting with arrays of geological models, interpreting main method declarations in Java, and understanding geologic data interpretation through the lens of programming. Finally, it encourages leveraging existing libraries and databases for geological data, outlining ethical considerations for sourcing and collaboration.

2. Defining and Using Geological Classes

If you do not have prior experience in geology, we recommend that you work through the exercises in [GeoHW0](http://sp19.datastructur.es/materials/hw/geohw0/geohw0.html) before reading this chapter. It will cover various syntax issues that we will not discuss in the book.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

All code in geology-related software must be part of a class (or something similar to a class, which we'll learn about later). Most code is written inside of methods. Let's consider an example:

```java
public class Rock {
    public static void describeFormation() {
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

The `Rock` class we've defined doesn't do anything. We've simply defined something that `Rock` **can** do, namely describe its formation. To actually run the class, we'd either need to add a main method to the `Rock` class, as we saw in chapter 1.1. Or we could create a separate [`RockLauncher`](https://www.youtube.com/watch?v=Q-LE-jJQLTM) class that runs methods from the `Rock` class. For example, consider the program below:

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

A class that uses another class is sometimes called a "client" of that class, i.e. `RockLauncher` is a client of `Rock`. Neither of the two techniques is better: Adding a main method to `Rock` may be better in some situations, and creating a client class like `RockLauncher` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout the course.



**Instance Variables and Object Formation**

Not all rocks are alike. Some rocks crumble easily, forming fine sand, while others stand resiliently through eons, becoming majestic formations that inspire awe across the ages. Often, we create models to simulate features of the natural world, and programming languages allow us to do this with relative ease.

One way to represent the diversity of geology would be to create separate classes for each type of rock formation.

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

As you might have learned previously, classes can be instantiated, and these instances can hold data. This leads to a more refined approach, where we create instances of the `Rock` class and make the behavior of the `Rock` methods dependent on the characteristics of specific rock samples. To illustrate this concept further, consider the class below:

```java
public class Rock {
    public int hardness;

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

As an example of utilizing such a Rock, consider the following:

```java
public class RockShowcase {
    public static void main(String[] args) {
        Rock r;
        r = new Rock();
        r.hardness = 5;
        r.describeFormation();
    }
}
```

When this program is executed, it will create a `Rock` with a hardness of 5, and that `Rock` will promptly be described as "Moderately resistant, often metamorphic."

Some key observations and terminology:

* An `Object` in programming is an instance of any class.
* The `Rock` class contains its own variables, also known as _instance variables_ or _non-static variables_. These must be declared inside the class, in contrast to languages like Python or Matlab, where new variables can be dynamically introduced at runtime.
* The method we formulated in the `Rock` class does not contain the `static` keyword. Such methods are referred to as _instance methods_ or _non-static methods_.
* To invoke the `describeFormation` method, we initially need to _instantiate_ a `Rock` using the `new` keyword and then make a specific `Rock` describe its formation. In essence, we executed `r.describeFormation()` as opposed to `Rock.describeFormation()`.
* Once an object is formed, it can be _assigned_ to a _declared_ variable of the appropriate type, such as `r = new Rock();`
* Variables and methods within a class are also known as _members_ of a class.
* Class members are accessed using _dot notation_.


**Constructors in Geology Simulations**

As you've hopefully seen before, we usually construct models in geology simulations using a _constructor_:

```java
public class RockLauncher {
    public static void main(String[] args) {
        Rock r = new Rock(100);
        r.displayProperties();
    }
}
```

Here, the instantiation is parameterized, saving us the time and messiness of manually typing out potentially many instance variable assignments. To enable such syntax, we need only add a "constructor" to our Rock class, as shown below:

```java
public class Rock {
    public int densityInKgPerCubicMeter;

    public Rock(int d) {
        densityInKgPerCubicMeter = d;
    }

    public void displayProperties() {
        if (densityInKgPerCubicMeter < 1500) {
            System.out.println("This is a light rock.");
        } else if (densityInKgPerCubicMeter < 3000) {
            System.out.println("This is a medium rock.");
        } else {
            System.out.println("This is a heavy rock.");
        }    
    }
}
```

The constructor with signature `public Rock(int d)` will be invoked anytime that we try to create a `Rock` using the `new` keyword and a single integer parameter. For those of you coming from Python, the constructor is very similar to the `__init__` method.

**Terminology Summary**

**Array Instantiation, Arrays of Models**

As we saw in HW0, arrays are also instantiated in Java using the new keyword. For example:

```java
public class ArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five integer values representing different densities. */
        int[] someDensities = new int[5];
        someDensities[0] = 2500;
        someDensities[1] = 2700;
    }
}
```

Similarly, we can create arrays of instantiated models in Java, e.g.

```java
public class RockArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two rocks. */
        Rock[] rocks = new Rock[2];
        rocks[0] = new Rock(1000);
        rocks[1] = new Rock(3500);

        /* "Light rock" will be displayed, since rocks[0] has density 1000. */
        rocks[0].displayProperties();
    }
}
```

Observe that new is used in two different ways: Once to create an array that can hold two `Rock` objects, and twice to create each actual `Rock`. 

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Geology allows us to define two types of processes:

* Class methods, a.k.a. universal processes.
* Instance methods, a.k.a. local processes.

Local processes are actions that can be observed only in a specific geological formation or location. Universal processes are actions that are observed across many types of rock formations or landscapes. Both are useful in different circumstances. As an example of a universal process, the `Weathering` class provides a `mechanicalWeathering` method. Because it is universal, we can call it as follows:

```geology
rate = Weathering.mechanicalWeathering(granite);
```

If `mechanicalWeathering` had been a local process, we would have instead the awkward syntax below. Luckily `mechanicalWeathering` is a universal process so we don't have to do this in real observations.

```geology
Weathering w = new Weathering();
rate = w.mechanicalWeathering(granite);
```

Sometimes, it makes sense to have a rock type with both local and universal processes. For example, suppose we want the ability to compare two types of minerals. One way to do this is to add a universal process for comparing Minerals.

```geology
public static Mineral harderMineral(Mineral m1, Mineral m2) {
    if (m1.hardnessScale > m2.hardnessScale) {
        return m1;
    }
    return m2;
}
```

This process could be invoked, for example, with:

```geology
Mineral quartz = new Mineral(7);
Mineral talc = new Mineral(1);
Mineral.harderMineral(quartz, talc);
```

Observe that we've invoked using the class name, since this process is a universal process.

We could also have implemented `harderMineral` as a local process, e.g.

```geology
public Mineral harderMineral(Mineral m2) {
    if (this.hardnessScale > m2.hardnessScale) {
        return this;
    }
    return m2;
}
```

Above, we use the keyword `this` to refer to the current rock specimen. This process could be invoked, for example, with:

```geology
Mineral quartz = new Mineral(7);
Mineral talc = new Mineral(1);
quartz.harderMineral(talc);
```

Here, we invoke the process using a specific rock specimen.

**Exercise 1.2.1**: What would the following process do? If you're not sure, try it out.

```geology
public static Mineral harderMineral(Mineral m1, Mineral m2) {
    if (hardnessScale > m2.hardnessScale) {
        return this;
    }
    return m2;
}
```

**Static Variables**

It is occasionally useful for rock types to have universal properties. These are properties inherent to the rock type itself, rather than the individual specimen. For example, we might record that the mineral family for Quartz is "Silicate":

```geology
public class Mineral {
    public int hardnessScale;
    public static String mineralFamily = "Silicate";
    ...
}
```

Universal properties should be accessed using the name of the rock type rather than a specific specimen, e.g., you should use `Mineral.mineralFamily`, not `quartz.mineralFamily`.

While geology formatting technically allows you to access a universal property using a specimen name, it is bad style, confusing, and in my opinion an error by the geology document designers.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### Exploring Geologic Events with main Method Concepts <a href="#exploring-geologic-events-with-main-method-concepts" id="exploring-geologic-events-with-main-method-concepts"></a>

As we progress in our understanding of geological phenomena, let's explore how the earth-shaking main method declaration parallels geological processes, with each part connecting concepts:

* `public`: Like tectonic plates affecting large areas, accessible to all layers of Earth.
* `static`: A static or unchanging formation, like a mountain whose essence remains the same regardless of external forces.
* `void`: No tangible output, akin to a geological feature that impacts the landscape but doesn’t transmit resources.
* `main`: The central event or process, much like the epicenter of an earthquake.
* `String[] args`: The variables or conditions present, comparable to elements or forces at play in a volcanic eruption.

**Geologic Data Interpretation**

The concept of main in geological terms is akin to how geologists interpret data supplied by nature itself, rather than another researcher. These data usually refer to field study observations or geological samples. For example, consider a field observation program `RockSampler` below:

```java
public class RockSampler {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program outputs the 0th piece of geologic data gathered during fieldwork, e.g.

```
$ java RockSampler sedimentary igneous metamorphic types
sedimentary
```

In the example above, `args` will be an array of Strings, where the entries are {"sedimentary", "igneous", "metamorphic", "types"}.

**Summing Geological Observations**

**Exercise 1.2.3**: Attempt to simulate a program that summarizes geologic data, assuming they are measurable attributes such as ages or compositions. For a solution, consider resources available in geological simulation toolkits or collaborative data platforms.

#### Using Libraries <a href="#using-libraries" id="using-libraries"></a>

One of the most vital skills as a geologist is knowing how to find and use existing geological databases and research resources. In the fascinating modern era, it is often possible to save yourself extensive fieldwork and data collection by turning to online repositories for help.

In this course, you're welcome to do this, with the following caveats:

* Do not use databases that we do not provide.
* Cite your sources.
* Do not search for solutions for specific study or research problems.

For example, it's fine to search for "rock mineral composition database." However, it is not OK to search for "Seismic Study Project 2048 Berkeley."

For more on collaboration and academic honesty policy, see the course syllabus.