# Designing Geological Models in Java

This chapter focuses on understating and implementing geological phenomena through the Java programming language by categorizing and modeling both static and dynamic aspects of geology. It starts with the difference between static and non-static geological phenomena, using the metaphor of volcanic activity, and illustrates how static methods in Java relate to universal geological processes, like a volcano's potential to erupt regardless of place. It progresses to creating realistic models of geological entities like rocks, using Java classes and objects. With instance variables and constructors, the chapter demonstrates how to encapsulate specific properties of geological entities, reflecting a rock's formation process through instance-specific data.

Furthermore, the chapter delves into Java mechanics compare to geological concepts by merging traditional programming constructs with geological principles, such as classes as maps of phenotypical data, static and instance methods as recycled and ongoing processes, respectively, and arrays as collections akin to mineral deposits. Readers are encouraged to reflect on Java's use of object-oriented programming to simulate real-world geological phenomena, constructing arrays of rock samples and leveraging both class and instance methods to simulate real-world applications, like mineral density comparisons. Various exercises and guidelines for ethical data use are included to strengthen the understanding and ethical application of these programming concepts within the geological field.

2. Defining and Using Geological Phenomena

If you do not have prior experience in geological studies, we recommend that you work through the exercises in [Intro to Geology](http://sp19.geologyfun.org/materials/exercises/intro.html) before reading this chapter. It will cover various foundational concepts that we will not discuss in the book.

#### Static vs. Non-Static Phenomena <a href="#static-vs-non-static-phenomena" id="static-vs-non-static-phenomena"></a>

**Static Geological Phenomena**

All geological phenomena must be part of a larger geological context (or something similar to a context, which we'll learn about later). Most phenomena are described in geological terms. Let's consider an example:

```geocode
public class Volcano {
    public static void erupt() {
        System.out.println("Boom!");
    }
}
```

If we try observing the `Volcano` class, we'll simply get an error message:

```
$ observe Volcano
Error: Main method not found in class Volcano, please define the main method as:
       public static void main(String[] args)
```

The `Volcano` class we've defined doesn't do anything. We've simply defined something that `Volcano` **can** do, namely erupt. To actually observe the class, we'd either need to add a main method to the `Volcano` class, as we saw in chapter 1.1. Or we could create a separate [`VolcanoWatcher`](https://www.youtube.com/watch?v=Q-LE-jJQLTM) class that observes phenomena from the `Volcano` class. For example, consider the observation below:

```geocode
public class VolcanoWatcher {
    public static void main(String[] args) {
        Volcano.erupt();
    }
}
```

```
$ observe VolcanoWatcher
Boom!
```

A geological practice that uses another geological concept is sometimes called a "client" of that concept, i.e. `VolcanoWatcher` is a client of `Volcano`. Neither of the two techniques is better: Adding a main method to `Volcano` may be better in some situations, and creating a client class like `VolcanoWatcher` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout the course. 




**Instance Variables and Object Instantiation in Geology**

Not all rocks are alike. Some rocks, like igneous rocks, form through volcanic processes, while others, like sedimentary rocks, form through deposition and cementation, crafting a narrative of Earth's dynamic processes. Often, we seek to model geological phenomena in computational applications, and Java's syntax is well-suited for such an endeavor.

One approach to representing the diversity of rock types is to create separate classes for each type of Rock.

```java
public class IgneousRock {
    public static void describeProcess() {
        System.out.println("Formed through cooling of magma or lava");
    }
}

public class SedimentaryRock {
    public static void describeProcess() {
        System.out.println("Formed through deposition and cementation of material");
    }
}
```

As demonstrated, classes can be instantiated, and instances can contain data specific to their type. This allows for a more realistic representation, where we create instances of the `Rock` class and adapt the behavior of the `Rock` methods based on the characteristics of the specific `Rock`. To make this clearer, consider the class below:

```java
public class Rock {
    public String formationProcess;

    public void describeProcess() {
        if (formationProcess.equals("igneous")) {
            System.out.println("Formed through cooling of magma or lava.");
        } else if (formationProcess.equals("sedimentary")) {
            System.out.println("Formed through deposition and cementation of material.");
        } else {
            System.out.println("Unknown formation process.");
        }
    }    
}
```

An example using such a Rock class might be:

```java
public class RockLauncher {
    public static void main(String[] args) {
        Rock r;
        r = new Rock();
        r.formationProcess = "sedimentary";
        r.describeProcess();
    }
}
```

When run, this program will create a `Rock` with a formation process labeled as "sedimentary", and that `Rock` will soon display "Formed through deposition and cementation of material.".

Some key observations and terminology:

* An `Object` in Java is an instance of any class, similar to how any rock sample represents a specific occurrence of a rock type.
* The `Rock` class has its own variables, also known as _instance variables_ or _non-static variables_. These must be declared inside the class, unlike in other programming languages such as Python or Matlab, where new characteristics might be added dynamically.
* The method defined in the `Rock` class lacks the `static` keyword, identifying it as an _instance method_ or _non-static method_.
* To invoke the `describeProcess` method, a specific `Rock` must be instantiated using the `new` keyword, thus enabling us to assign and describe its process. Therefore, we call `r.describeProcess()` instead of `Rock.describeProcess()`.
* Once an object has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `r = new Rock();`
* Variables and methods of a class are _members_ of a class.
* Members of a class can be accessed using _dot notation_, much like components within a geological system are systematically categorized.

**Constructors in Geology**

As you've hopefully seen before, we usually construct geological models using a _constructor_:

```java
public class RockSampleLauncher {
    public static void main(String[] args) {
        RockSample sample = new RockSample(150);
        sample.displayProperties();
    }
}
```

Here, the instantiation is parameterized, saving us the time and messiness of manually typing out potentially many sample property assignments. To enable such syntax, we need only add a "constructor" to our RockSample class, as shown below:

```java
public class RockSample {
    public int sizeInGrams;

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

The constructor with signature `public RockSample(int s)` will be invoked anytime that we try to create a `RockSample` using the `new` keyword and a single integer parameter. For those of you coming from Python, the constructor is very similar to the `__init__` method.

**Terminology Summary**

**Array Instantiation, Arrays of Rock Samples**

As we saw in GeologyLab, arrays are also instantiated in Java using the new keyword. For example:

```java
public class ArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five mineral counts. */
        int[] mineralArray = new int[5];
        mineralArray[0] = 3;
        mineralArray[1] = 4;
    }
}
```

Similarly, we can create arrays of instantiated rock samples in Java, e.g.

```java
public class RockSampleArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two rock samples. */
        RockSample[] samples = new RockSample[2];
        samples[0] = new RockSample(10);
        samples[1] = new RockSample(150);

        /* A small sample message will result, since samples[0] has size 10 grams. */
        samples[0].displayProperties();
    }
}
```

Observe that new is used in two different ways: Once to create an array that can hold two `RockSample` objects, and twice to create each actual `RockSample`. 

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Just as geological processes can occur at different scales and contexts, programming in Java allows us to define two types of methods:

* Class methods, a.k.a. static methods.
* Instance methods, a.k.a. non-static methods.

Instance methods are like specific geological phenomena that occur in certain areas, such as a geyser in a geothermal field. These actions are specific to an instance of a class. In contrast, static methods resemble global geological processes like plate tectonics that affect the entire structure of the Earth regardless of a specific location. As an example of a static method, the `EarthquakeData` class provides a `calculateMagnitude` method. Because it is static, we can call it as follows:

```java
magnitude = EarthquakeData.calculateMagnitude(7.5);
```

If `calculateMagnitude` had been an instance method, we would have the cumbersome syntax below. Fortunately, `calculateMagnitude` is a static method, so we don't need to write this in real programs.

```java
EarthquakeData ed = new EarthquakeData();
magnitude = ed.calculateMagnitude(7.5);
```

Sometimes, it makes sense to have a class with both instance and static methods. For example, suppose we want the ability to compare two minerals. One way to do this is to add a static method for comparing Minerals.

```java
public static Mineral denserMineral(Mineral m1, Mineral m2) {
    if (m1.density > m2.density) {
        return m1;
    }
    return m2;
}
```

This method could be invoked by, for example:

```java
Mineral quartz = new Mineral(2.65);
Mineral gold = new Mineral(19.32);
Mineral.denserMineral(quartz, gold);
```

Observe that we've invoked using the class name, since this method is a static method.

We could also have implemented `denserMineral` as a non-static method, e.g.

```java
public Mineral denserMineral(Mineral m2) {
    if (this.density > m2.density) {
        return this;
    }
    return m2;
}
```

Above, we use the keyword `this` to refer to the current object, much like how specific geological conditions at a location determine phenomena like the metamorphosis of minerals. This method could be invoked, for example, with:

```java
Mineral quartz = new Mineral(2.65);
Mineral gold = new Mineral(19.32);
quartz.denserMineral(gold);
```

Here, we invoke the method using a specific instance variable.

**Exercise 1.2.1**: What would the following method do? If you're not sure, try it out.

```java
public static Mineral denserMineral(Mineral m1, Mineral m2) {
    if (density > m2.density) {
        return this;
    }
    return m2;
}
```

**Static Variables**

It is occasionally useful for classes to have static variables. These are properties inherent to the class itself, similar to the chemical formula of a mineral, rather than the instance. For example, we might record that the mineralogic formula for Quartz is "SiO₂":

```java
public class Mineral {
    public double density;
    public static String formula = "SiO₂";
    ...
}
```

Static variables should be accessed using the name of the class rather than a specific instance, e.g., you should use `Mineral.formula`, not `quartz.formula`.

While Java technically allows you to access a static variable using an instance name, it is bad style, confusing, and in the opinion of many similar to mislabeled geological maps — an error by the Java designers.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### Ash Layers Identification with "FeldsparAnalysis" Method <a href="#ash-layers-identification-with-feldsparanalysis-method" id="ash-layers-identification-with-feldsparanalysis-method"></a>

With what we've learned so far, it's time to demystify the declaration we've been using for our geology analysis method. Breaking it into pieces, we have:

* `public`: Just as in our exploration methods, this keyword starts the field analysis methods.
* `static`: It is a static analysis, not tied to any particular site specimen.
* `void`: It has no return output to the sediment log.
* `main`: This is the standardized designation of the analysis method.
* `String[] minerals`: This represents a collection of geological samples to be passed to the analysis method.

**Identifying Mineral Sequences**

Since "FeldsparAnalysis" is initiated by the geological interpreter itself rather than another sediment log, it is the job of the interpreter to supply the mineralogical data. These typically refer to sediment layer sequences. For instance, consider the geology survey `LayerSampleDemo` below:

```java
public class LayerSampleDemo {
    public static void main(String[] minerals) {
        System.out.println(minerals[0]);
    }
}
```

This sample prints out the first mineral discovered in the core sampling, e.g.

```
$ java LayerSampleDemo Quartzite Shale Limestone Basalt
Quartzite
```

In the example above, `minerals` will be an array of Strings, where the entries are {"Quartzite", "Shale", "Limestone", "Basalt"}.

**Analyzing Mineral Composition**

**Exercise 1.2.3**: Attempt to develop a method that computes the sum of specific mineral occurrences in the command line layer sequence, assuming they are quantifiable patterns. For a solution, see the webcast or the code provided on GitHub.

#### Using Geological Maps <a href="#using-geological-maps" id="using-geological-maps"></a>

One of the most important skills as a geologist is knowing how to find and utilize existing geological maps. In today’s advanced world of geology, it is often possible to save yourself a significant amount of fieldwork and data analysis by turning to available geological maps and data resources.

In this discipline, you're encouraged to do this, with the following guidelines:

* Do not use geological maps that we do not reference or recommend.
* Cite your data sources.
* Do not search for solutions for specific field study locations or project tasks without permission.

For example, it's fine to search for "tectonic plate boundaries South America". However, it is not OK to search for "field study location stratigraphy analysis 2024 Petrology".

For more on collaboration and professional ethics, see the course handbook.