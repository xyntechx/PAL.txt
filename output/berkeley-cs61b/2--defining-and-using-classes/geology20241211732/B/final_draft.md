# Designing Geological Models in Java

This chapter focuses on understating and implementing geological phenomena through the Java programming language by categorizing and modeling both static and dynamic aspects of geology. It starts with the difference between static and non-static geological phenomena, using the metaphor of volcanic activity, and illustrates how static methods in Java relate to universal geological processes, like a volcano's potential to erupt regardless of place. It progresses to creating realistic models of geological entities like rocks, using Java classes and objects. With instance variables and constructors, the chapter demonstrates how to encapsulate specific properties of geological entities, reflecting a rock's formation process through instance-specific data.

Furthermore, the chapter delves into Java mechanics compare to geological concepts by merging traditional programming constructs with geological principles, such as classes as maps of phenotypical data, static and instance methods as recycled and ongoing processes, respectively, and arrays as collections akin to mineral deposits. Readers are encouraged to reflect on Java's use of object-oriented programming to simulate real-world geological phenomena, constructing arrays of rock samples and leveraging both class and instance methods to simulate real-world applications, like mineral density comparisons. Various exercises and guidelines for ethical data use are included to strengthen the understanding and ethical application of these programming concepts within the geological field.

### 2. Defining Geological Phenomena with Computer Science Concepts

If you do not have prior experience in geological studies, we recommend that you work through the exercises in [Intro to Geology](http://sp19.geologyfun.org/materials/exercises/intro.html) before reading this chapter. It will help you grasp the foundational geological concepts which we use here as analogies for computer science principles.

#### Understanding Static and Non-Static Concepts: A Geological Perspective <a href="#static-vs-non-static-phenomena" id="static-vs-non-static-phenomena"></a>

**Static Geological Phenomena Reflected in Static Methods**

In computer science, 'static' refers to methods that belong to the class itself rather than any particular object created from that class, akin to widespread geological phenomena that occur irrespective of individual conditions. Let's explore this using a geological analogy:

```java
public class Volcano {
    public static void erupt() {
        System.out.println("Boom!");
    }
}
```

This `Volcano` class illustrates a geological feature with a static method `erupt()`, which simulates a volcanic eruption. However, just referencing this class will not trigger this action unless properly executed.:

```
$ observe Volcano
Error: Main method not found in class Volcano, please define the main method as:
       public static void main(String[] args)
```

Our class currently lacks a main method, which is necessary to observe the eruption in action. To visualize this process, we either need to include a main method or utilize another class to trigger the volcanic activity:

```java
public class VolcanoWatcher {
    public static void main(String[] args) {
        Volcano.erupt();
    }
}
```

Running this `VolcanoWatcher` class:

```
$ observe VolcanoWatcher
Boom!
```

A geological operation like observing volcanic activity is analogous to utilizing a "client" class in programming where `VolcanoWatcher` acts as a client to `Volcano`. This parallel between geology and programming helps elucidate how static methods, which do not require creating an instance of the class, can be utilized effectively. As we delve deeper into these topics, you will better understand when to apply such methods within your code. Integrating static methods directly into the `Volcano` class or through a client like `VolcanoWatcher` each have their merits depending on the situation at hand.

**Instance Variables and Object Instantiation in Geology**

In the diverse world of geology, rocks tell many tales. Igneous rocks, born of volcanic activity, contrast sharply with sedimentary rocks that arise from the slow deposition and cementation of particles. To encapsallate this variety programmatically, Java provides tools that are surprisingly apropos.

To encapsulate the variety among rock types, we can represent them through distinct classes in Java.

```java
public class IgneousRock {
    public void describeFormation() {
        System.out.println("Formed through cooling and solidification of magma or lava.");
    }
}

public class SedimentaryRock {
    public void describeFormation() {
        System.out.println("Formed through accumulation and cementation of sediment.");
    }
}
```

These classes offer a foundation by which specific information and methods can be tied to individual rock types. For a more dynamic model, we can incorporate instance variables to further distinguish each rock instance, harnessing the power of Java's object-oriented approach.

```java
public class Rock {
    private String formationProcess;

    public Rock(String process) {
        this.formationProcess = process;
    }

    public void describeProcess() {
        switch(formationProcess) {
            case "igneous":
                System.out.println("Formed through cooling of magma or lava.");
                break;
            case "sedimentary":
                System.out.println("Formed through deposition and cementation of material.");
                break;
            default:
                System.out.println("Unknown formation process.");
        }
    }

    public String getFormationProcess() {
        return formationProcess;
    }
}
```

With this setup, we utilize instance variables and methods to craft varied rock samples each with unique characteristics:

```java
public class RockSimulator {
    public static void main(String[] args) {
        Rock rockSample = new Rock("sedimentary");
        rockSample.describeProcess();
    }
}
```

Running this simulation provides insight into the world of sedimentary processes by outputting "Formed through deposition and cementation of material." when describing the rock.

Key Observations:

* An **Object** in Java is akin to a specific rock sample in geology—it's an instance of a class, embodying specific attributes of that rock type.
* The `Rock` class defines variables specific to its nature, known as **instance variables**. These are unique to each object created from the class, similar to how each rock's characteristics might differ in nature.
* The methods within our `Rock` class, specifically lacking `static`, are termed **instance methods**, enabling operations tied to each rock instance.
* For usage, `describeProcess()` is invoked on an object instance—`rockSample.describeProcess()`—requiring that object to identify the correct formation process.
* Creating a new rock simulation involves the instantiation of an object using `new Rock("type")`, associating the attributes defined by that instance.
* Class members, both data and functions, are accessed via **dot notation**, similar to how minerals and layers in geology identify attributes systematically within a formation.

**Constructors in Geology and Java**

In computer science, and especially in Java programming, constructors play an essential role in creating and initializing objects. By using geology as our theme, let's build a clear understanding of constructors and their use in object instantiation.

Consider this example where we simulate the creation of a geological sample:

```java
public class RockSampleLauncher {
    public static void main(String[] args) {
        RockSample sample = new RockSample(150);
        sample.displayProperties();
    }
}
```

Here, we're using a parameterized constructor to avoid the tedium of individually setting each property of the `RockSample`. By doing so, we enhance code efficiency and maintain neatness. The `RockSample` class example shows how a constructor initializes the rock's mass:

```java
public class RockSample {
    private int sizeInGrams;

    // Constructor
    public RockSample(int s) {
        sizeInGrams = s;
    }

    public void displayProperties() {
        if (sizeInGrams < 50) {
            System.out.println("This is a small sample!");
        } else if (sizeInGrams < 200) {
            System.out.println("This is a medium sample.");
        } else {
            System.out.println("This is a large sample!");
        }    
    }
}
```

The constructor, `public RockSample(int s)`, gets invoked with the `new` keyword, establishing the `RockSample's` characteristic right at the point of creation. For Python enthusiasts, this mirrors the `__init__` method.

**Exploring Array Instantiation with Rock Samples**

Arrays, both in geology and programming, allow the collection of elements—in this context, mineral data or rock samples. In Java, arrays are dynamically created using the `new` keyword:

```java
public class ArrayDemo {
    public static void main(String[] args) {
        /* Create an array of mineral counts. */
        int[] mineralArray = new int[5];
        mineralArray[0] = 3; // Sample mineral counts
        mineralArray[1] = 4;
    }
}
```

Similarly, arrays can store multiple instances of our `RockSample` class:

```java
public class RockSampleArrayDemo {
    public static void main(String[] args) {
        /* Create an array of rock samples. */
        RockSample[] samples = new RockSample[2];
        samples[0] = new RockSample(10);  // Instantiate new rock samples
        samples[1] = new RockSample(150);

        /* Invoke method to display properties. */
        samples[0].displayProperties();
    }
}
```

Notice how `new` is pivotal here—first to frame an array structure capable of holding `RockSample` objects, and then to instantiate each specific sample itself. Mastering this use of constructors and arrays reinforces your Java capabilities, much like understanding various rock formations bolsters geological knowledge.

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

In Java, much like in geology where processes affect materials in different ways and at different scales, programming provides us with two types of methods:

* Class methods, also known as static methods.
* Instance methods, also known as non-static methods.

**Instance Methods:** Similar to localized geological events like the eruption of a particular volcano, instance methods operate specifically on instances of a class. For example, a method that calculates a mineral’s weight based on its volume and density applies to that specific mineral object.

**Class Methods:** In contrast, static methods can be likened to pervasive geological processes such as atmospheric weathering that impacts all exposed rocks globally. A class method operates at the class level, which means it can be called without an instance of the class. For example, consider a static method `calculateMagnitude` in a class `EarthquakeData` that we call as follows:

```java
magnitude = EarthquakeData.calculateMagnitude(7.5);
```

If `calculateMagnitude` were an instance method, we would have to first create an object of `EarthquakeData`, resulting in a syntax more cumbersome than necessary:

```java
EarthquakeData ed = new EarthquakeData();
magnitude = ed.calculateMagnitude(7.5);
```

Though sometimes it's essential to use both static and non-static methods within a class, there's a place for each. Imagine we need to compare two mineral samples. A static method such as `denserMineral` could help in this context, returning the denser mineral between the two given samples:

```java
public static Mineral denserMineral(Mineral m1, Mineral m2) {
    return (m1.density > m2.density) ? m1 : m2;
}
```

Such a method can be invoked as follows:

```java
Mineral quartz = new Mineral(2.65);
Mineral gold = new Mineral(19.32);
Mineral.denserMineral(quartz, gold);
```

Here, the method is called with the class name, showcasing how global geological principles apply universally as static methods do among classes.

Alternatively, an instance method may use the `this` keyword to account for its specific locality, similar to mineral composition varying by site. This version can be invoked as:

```java
public Mineral denserMineral(Mineral m2) {
    return (this.density > m2.density) ? this : m2;
}
```

In practice:

```java
Mineral quartz = new Mineral(2.65);
Mineral gold = new Mineral(19.32);
quartz.denserMineral(gold);
```

Here, `quartz.denserMineral(gold)` provides a specific interaction between these two instances.

**Exercise 1.2.1**: Evaluate the following code snippet. Try running it to observe any errors regarding static and instance method contexts.

```java
public static Mineral denserMineral(Mineral m1, Mineral m2) {
    if (density > m2.density) {
        return this;
    }
    return m2;
}
```

**Static Variables**

Static variables, akin to the general chemical composition of all samples of quartz being SiO₂, are a property of the class itself, not any individual instance. Consider this exemplary class:

```java
public class Mineral {
    public double density;
    public static String formula = "SiO₂";
    ...
}
```

Static variables should be accessed using the class name, such as `Mineral.formula`. Accessing them via an instance, like `quartz.formula`, may work technically but is considered poor form, resembling how inaccurate labels on a geological map could lead to confusion.

**Exercise 1.2.2**: Try completing this task to reinforce your understanding:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### Ash Layers Identification with "FeldsparAnalysis" Method <a href="#ash-layers-identification-with-feldsparanalysis-method" id="ash-layers-identification-with-feldsparanalysis-method"></a>

With what we've learned so far, it's time to unravel the declaration we've been using for our geology analysis method. Breaking it into parts, we have:

* `public`: Just as in our exploration methods, this keyword initiates the field analysis methods, allowing them to be accessed broadly, like a geologist open to sharing findings with the community.
* `static`: It pertains to a static analysis technique, not bound to any specific field sample, akin to a universal principle in geology that applies regardless of location.
* `void`: This signifies that the method does not return any output to the sediment log, like a preliminary survey that gathers information without drawing conclusions yet.
* `main`: This is the conventional entry-point of the analysis method, akin to the chief interpreter guiding the examination process.
* `String[] minerals`: This denotes an array of geological samples supplied to the analysis method, serving as the diverse rock stratum to be evaluated.

**Identifying Mineral Sequences**

Since "FeldsparAnalysis" is initiated by the geological interpreter rather than another sediment log, it's the interpreter's role to present the mineralogical data. These data typically correspond to sediment layer sequences. For instance, consider the geological survey `LayerSampleDemo` below:

```java
public class LayerSampleDemo {
    public static void main(String[] minerals) {
        System.out.println(minerals[0]);
    }
}
```

This sample outputs the first mineral found in the core sampling, e.g.

```
$ java LayerSampleDemo Quartzite Shale Limestone Basalt
Quartzite
```

In this example, `minerals` acts as an array of Strings wherein the entries are {"Quartzite", "Shale", "Limestone", "Basalt"}, representing a core sample's sequence.

**Analyzing Mineral Composition**

Understanding the sequence and composition of minerals assists in predicting geological history and structure. Similarly, grasping how arrays function in Java reveals the organization and manipulation of data.

**Exercise 1.2.3**: Develop a method that calculates the occurrence of a specific mineral within the command line-layer sequence, treated as discernible patterns. For guidance, watch the webcast or examine the solution on GitHub.

#### Utilizing Geological Maps <a href="#utilizing-geological-maps" id="utilizing-geological-maps"></a>

For geologists, effective use of existing geological maps is an invaluable skill, akin to how computer scientists leverage libraries and frameworks. In today's technologically enhanced geoscience landscape, geological maps and data repositories are often as crucial as first-hand fieldwork and analysis.

When incorporating geological maps in your research, adhere to these best practices:

* Utilize only those geological maps that have been vetted or referenced by credible sources, much like relying on well-documented APIs in programming.
* Always cite your data sources meticulously to maintain academic integrity, similar to documenting code sources in software development.
* Seek permission before delving into specialized databases or resources, analogous to requiring authorization for accessing private repositories in the tech world.

For instance, while it's perfectly acceptable to search for generalized information such as “tectonic plate boundaries South America,” searching for specific project-related data like “2024 Stratigraphy Analysis at Petrology Site” without approval is discouraged to maintain ethical research practices.

Refer to the course handbook for in-depth guidance on collaboration ethics and proper use of scientific resources, drawing parallels to corporate guidelines in sharing and using code in CS.