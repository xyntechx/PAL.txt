# Defining and Using Classes

In this chapter, we explore the foundational concepts of object-oriented programming in Java by defining and using classes. The discussion begins with the geological analogy of defining processes, such as the `Volcano` class, to illustrate how Java classes encapsulate behavior and can be observed or "monitored" using other classes like `VolcanoWatcher`. This introduction serves as a stepping stone to understanding key object-oriented concepts such as class and instance methods, object instantiation, and constructors. We learn how objects are instances of classes, with instance variables and methods defined to interact with those objects, as shown through the `Mineral` and `RockSample` classes.

Additionally, the chapter delves into the differences between static and instance methods. Static methods, like the `denserRock` example, operate at the class level without needing an instance, whereas instance methods are tied to an object's instance. Static variables are also addressed, highlighting their role in representing class-level properties, such as `commonestMineral` in the example of rocks. We conclude by analyzing the structure of the `public static void main(String[] args)` method, a fundamental entry point for Java applications, and learn about command line arguments and their utility. Overall, the chapter lays a solid groundwork for understanding how Java facilitates object-oriented programming to simulate real-world entities and processes effectively.

2. Defining and Using Classes

If you do not have prior experience with geological classification systems, we recommend that you work through the exercises in [GEO0](http://geologystudy.com/materials/hw/geo0/geo0.html) before reading this chapter. It will cover various classification issues that we will not discuss in the book.

#### Igneous vs. Sedimentary Processes <a href="#igneous-vs-sedimentary-processes" id="igneous-vs-sedimentary-processes"></a>

**Igneous Processes**

All formations in geology must be classified as part of a process (or something similar to a process, which we'll learn about later). Most formations can be described through certain processes. Let's consider an example:

```java
public class Volcano {
    public static void erupt() {
        System.out.println("Lava flows!");
    }
}
```

If we try to explain the `Volcano` process without context, we'll simply get an incomplete geological picture:

```
$ explanation Volcano
Error: Main process not identified in class Volcano, please define the comprehensive process as:
       public static void main(String[] args)
```

The `Volcano` class we've defined doesn't produce any observable formation. We've simply defined something that `Volcano` **can** do, namely erupt. To actually understand the formation, we'd either need to add a main process to the `Volcano` class, as we saw in chapter 1.1. Or we could create a separate [`VolcanoWatcher`](https://www.youtube.com/watch?v=L-ER6CrNhIs) class that examines processes from the `Volcano` class. For example, consider the program below:

```java
public class VolcanoWatcher {
    public static void main(String[] args) {
        Volcano.erupt();
    }
}
```

```
$ explanation VolcanoWatcher
Lava flows!
```

A class that observes another class is sometimes called a "monitor" of that class, i.e. `VolcanoWatcher` is a monitor of `Volcano`. Neither of the two observation techniques is superior: Adding a main process to `Volcano` may be better in some situations, and creating a monitor class like `VolcanoWatcher` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout the course.

**Instance Variables and Object Instantiation**

Not all minerals are alike. Some glimmer with the brilliance of a thousand suns, while others lie understated and muted, whispering stories of the ancient Earth. Often, we write programs to mimic features of the planet we dwell on, and Java's syntax was crafted to easily allow such mimicry.

One approach to allowing us to represent the spectrum of mineral types would be to create separate classes for each type of Mineral.

```java
public class Diamond {
    public static void shine() {
        System.out.println("Glitter, glitter, sparkle, shine!");
    }
}

public class Granite {
    public static void shine() {
        System.out.println("Subtle glow, enduring strength.");
    }
}
```

As you should have seen in the past, classes can be instantiated, and instances can hold data. This leads to a more natural approach, where we create instances of the `Mineral` class and make the behavior of the `Mineral` methods contingent upon the properties of the specific `Mineral`. To make this more concrete, consider the class below:

```java
public class Mineral {
    public int hardnessValue;

    public void shine() {
        if (hardnessValue > 7) {
            System.out.println("Glitter, glitter, sparkle, shine!");
        } else if (hardnessValue > 4) {
            System.out.println("Subtle glow, enduring strength.");
        } else {
            System.out.println("Soft luminescence.");
        }
    }    
}
```

As an example of using such a Mineral, consider:

```java
public class MineralLauncher {
    public static void main(String[] args) {
        Mineral m;
        m = new Mineral();
        m.hardnessValue = 6;
        m.shine();
    }
}
```

When run, this program will create a `Mineral` with a hardness value of 6, and that `Mineral` will soon exhibit a "subtle glow, enduring strength".

Some key observations and terminology:

* An `Object` in Java is an instance of any class.
* The `Mineral` class has its own variables, also known as _instance variables_ or _non-static variables_. These must be declared inside the class, unlike languages like Python or Matlab, where new variables can be added at runtime.
* The method that we created in the `Mineral` class did not have the `static` keyword. We call such methods _instance methods_ or _non-static methods_.
* To call the `shine` method, we had to first _instantiate_ a `Mineral` using the `new` keyword, and then make a specific `Mineral` shine. In other words, we called `m.shine()` instead of `Mineral.shine()`.
* Once an object has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `m = new Mineral();`
* Variables and methods of a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_.


**Constructors in Java**

As you've hopefully seen before, we usually construct geological sample objects in geological modeling using a _constructor_:

```java
public class RockSampleLauncher {
    public static void main(String[] args) {
        RockSample rs = new RockSample(12);
        rs.describeSample();
    }
}
```

Here, the instantiation is parameterized, saving us the time and messiness of manually typing out potentially many properties of each rock sample. To enable such syntax, we need only add a "constructor" to our RockSample class, as shown below:

```java
public class RockSample {
    public int mineralCompositionPercentage;

    public RockSample(int m) {
        mineralCompositionPercentage = m;
    }

    public void describeSample() {
        if (mineralCompositionPercentage < 30) {
            System.out.println("This is a sedimentary rock.");
        } else if (mineralCompositionPercentage < 70) {
            System.out.println("This is a metamorphic rock.");
        } else {
            System.out.println("This is an igneous rock.");
        }    
    }
}
```

The constructor with signature `public RockSample(int m)` will be invoked anytime that we try to create a `RockSample` using the `new` keyword and a single integer parameter. For those of you coming from other domains, the constructor is very similar to the initialization functions used in creating geological models.

**Terminology Summary**

**Array Instantiation, Arrays of Objects**

As we saw in HW0, arrays are also instantiated in Java using the new keyword. For example:

```java
public class SampleArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five mineral percentages. */
        int[] compositionPercentages = new int[5];
        compositionPercentages[0] = 45;
        compositionPercentages[1] = 60;
    }
}
```

Similarly, we can create arrays of instantiated rock samples in Java, e.g.

```java
public class RockSampleArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two rock samples. */
        RockSample[] samples = new RockSample[2];
        samples[0] = new RockSample(25);
        samples[1] = new RockSample(80);

        /* This will identify the first sample as sedimentary, since samples[0] has 25% mineral composition. */
        samples[0].describeSample();
    }
}
```

Observe that new is used in two different ways: Once to create an array that can hold two `RockSample` objects, and twice to create each actual `RockSample`. 

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java allows us to define two types of methods:

* Class methods, a.k.a. static methods.
* Instance methods, a.k.a. non-static methods.

Instance methods are actions that can be taken only by a specific instance of a class. Static methods are actions that are taken by the class itself. Both are useful in different circumstances. As an example of a static method, consider the concept of mineral hardness. A `Hardness` class could provide a `measure` method. Because it is static, we can call it as follows:

```java
hardness = Hardness.measure("Quartz");
```

If `measure` had been an instance method, we would have instead the awkward syntax below. Luckily `measure` is a static method so we don't have to do this in real programs.

```java
Hardness h = new Hardness();
hardness = h.measure("Quartz");
```

Sometimes, it makes sense to have a class with both instance and static methods. For example, suppose we want the ability to compare two rocks by their density. One way to do this is to add a static method for comparing Rocks.

```java
public static Rock denserRock(Rock r1, Rock r2) {
    if (r1.density > r2.density) {
        return r1;
    }
    return r2;
}
```

This method could be invoked by, for example:

```java
Rock r = new Rock(2.65);
Rock r2 = new Rock(3.00);
Rock.denserRock(r, r2);
```

Observe that we've invoked it using the class name, since this method is a static method.

We could also have implemented `denserRock` as a non-static method, e.g.

```java
public Rock denserRock(Rock r2) {
    if (this.density > r2.density) {
        return this;
    }
    return r2;
}
```

Above, we use the keyword `this` to refer to the current object. This method could be invoked, for example, with:

```java
Rock r = new Rock(2.65);
Rock r2 = new Rock(3.00);
r.denserRock(r2);
```

Here, we invoke the method using a specific instance variable.

**Exercise 1.2.1**: What would the following method do? If you're not sure, try it out.

```java
public static Rock denserRock(Rock r1, Rock r2) {
    if (density > r2.density) {
        return this;
    }
    return r2;
}
```

**Static Variables**

It is occasionally useful for classes to have static variables. These are properties inherent to the class itself, rather than the instance. For example, we might record that the most common mineral in the Earth's crust is "Feldspar":

```java
public class Rock {
    public double density;
    public static String commonestMineral = "Feldspar";
    ...
}
```

Static variables should be accessed using the name of the class rather than a specific instance, e.g., you should use `Rock.commonestMineral`, not `r.commonestMineral`.

While Java technically allows you to access a static variable using an instance name, it is bad style, confusing, and in my opinion an error by the Java designers.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe\_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String\[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

With what we've learned so far, it's time to unravel the layers of the earth to understand the structure of this crucial method declaration. Analyzing it layer by layer, we have:

* `public`: So far, this keyword marks all of our methods like the crust of the Earth, visible and accessible.
* `static`: Like a steady, unchanging geological formation, this denotes that the method is constant, independent of any particular instance.
* `void`: Much like a barren rock devoid of resources, this signifies that the method has no return value.
* `main`: This is the core, the name of the method where everything converges.
* `String[] args`: These are the components, much like different mineral deposits sprinkled through the substrata of our main method.

**Command Line Arguments**

Since the main function is called by the Java interpreter itself rather than another Java class, it is akin to a geological process initiated by a specific external trigger, independent from usual sedimentary processes. The interpreter must provide these arguments, often in the form of command line inputs. Consider the rock specimen program `ArgsDemo` below:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program displays the primary element or the first stratum of the command line argument layer, e.g.

```
$ java ArgsDemo these are sedimentary layers
these
```

In the example above, `args` will be an array of Strings, resembling a stratigraphic sequence where each layer is labeled {"these", "are", "sedimentary", "layers"}.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Attempt to develop a program that aggregates the command line arguments, assuming they are analogous to measurable quantities like mineral concentrations. For a complete geological analysis of the solution, see the webcast or consult the core code samples provided on GitHub.

#### Utilizing Geological Resources <a href="#utilizing-geological-resources" id="utilizing-geological-resources"></a>

One of the most essential skills in geology is knowing how to find and apply existing resources. In the fascinating field of geology, it is often possible to save yourself immense effort and potential errors by consulting the wealth of knowledge already available in geological databases and literature.

In this course, you're encouraged to do this, with the following conditions:

* Do not use resources other than those we provide.
* Properly cite your references.
* Do not seek out solutions for specific fieldwork or research project problems.

For example, it's permissible to search for "mineral identification in granite rock samples". However, it is not acceptable to search for "Seismic Activity Analysis Project Answers Berkeley".

For more on collaboration and academic integrity policy, please refer to the course syllabus.