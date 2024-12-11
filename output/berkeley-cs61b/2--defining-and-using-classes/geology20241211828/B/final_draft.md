# Defining and Using Classes

In this chapter, we explore the foundational concepts of object-oriented programming in Java by defining and using classes. The discussion begins with the geological analogy of defining processes, such as the `Volcano` class, to illustrate how Java classes encapsulate behavior and can be observed or "monitored" using other classes like `VolcanoWatcher`. This introduction serves as a stepping stone to understanding key object-oriented concepts such as class and instance methods, object instantiation, and constructors. We learn how objects are instances of classes, with instance variables and methods defined to interact with those objects, as shown through the `Mineral` and `RockSample` classes.

Additionally, the chapter delves into the differences between static and instance methods. Static methods, like the `denserRock` example, operate at the class level without needing an instance, whereas instance methods are tied to an object's instance. Static variables are also addressed, highlighting their role in representing class-level properties, such as `commonestMineral` in the example of rocks. We conclude by analyzing the structure of the `public static void main(String[] args)` method, a fundamental entry point for Java applications, and learn about command line arguments and their utility. Overall, the chapter lays a solid groundwork for understanding how Java facilitates object-oriented programming to simulate real-world entities and processes effectively.

## 2. Defining and Using Classes

If you do not have prior experience with geological classification systems, we recommend that you work through the exercises in [GEO0](http://geologystudy.com/materials/hw/geo0/geo0.html) before reading this chapter. It will cover various classification issues that we will not discuss in the book.

#### Igneous vs. Sedimentary Processes <a href="#igneous-vs-sedimentary-processes" id="igneous-vs-sedimentary-processes"></a>

**Igneous Processes**

All formations in geology must be classified as part of a process (or something similar to a process, which we'll learn about later). Most formations can be described through certain processes. Let's consider an example:

```java
public class Volcano {
    public static void erupt() {
        System.out.println("Lava flows and forms igneous rocks!");
    }
}
```

When discussing the `Volcano` process, context is essential to grasp the complete geological picture:

```shell
$ explanation Volcano
Error: Main process not identified in class Volcano, please define the comprehensive process as:
       public static void main(String[] args)
```

The `Volcano` class can initiate an eruption, a critical process in igneous rock formation. However, to fully comprehend this formation process, it is important to track and analyze volcanic activities. By adding a primary execution path to the `Volcano` class or creating a `VolcanoWatcher` class, we can achieve this. For instance, consider the program below:

```java
public class VolcanoWatcher {
    public static void main(String[] args) {
        Volcano.erupt();
    }
}
```

```shell
$ explanation VolcanoWatcher
Lava flows and forms igneous rocks!
```

An observing class such as `VolcanoWatcher` is commonly referred to as a "monitor" class, acting in this case as an observer of `Volcano` activities. Neither functionality integration within the `Volcano` class nor the creation of a standalone observer class holds absolute superiority, as each has its situational advantages. Insight into the effectiveness of these approaches will be enhanced through practice as the course progresses.

**Instance Variables and Object Instantiation**

Just as minerals in the Earth's crust display an impressive variety of colors, lusters, and forms, Java allows us to create diverse objects through its class system. By drawing parallels between mineral characteristics and object-oriented programming, we can see the beauty in both disciplines.

An efficient way to represent different types of minerals in Java is through object instantiation and the use of instance variables. Rather than creating a separate class for each mineral, such as Diamond or Granite, we can define a single `Mineral` class that can capture various properties and behaviors.

```java
public class Mineral {
    private int hardnessValue;
    private String name;

    public Mineral(String name, int hardnessValue) {
        this.name = name;
        this.hardnessValue = hardnessValue;
    }

    public void shine() {
        if (hardnessValue > 7) {
            System.out.println(name + ": Glitter, glitter, sparkle, shine!");
        } else if (hardnessValue > 4) {
            System.out.println(name + ": Subtle glow, enduring strength.");
        } else {
            System.out.println(name + ": Soft luminescence.");
        }
    }    
}
```

The `Mineral` class above has instance variables `name` and `hardnessValue`. Adding a constructor allows us to easily create and initialize minerals with their desired properties.

Here's how we can instantiate and utilize the `Mineral` class:

```java
public class MineralLauncher {
    public static void main(String[] args) {
        Mineral diamond = new Mineral("Diamond", 10);
        diamond.shine();
        
        Mineral quartz = new Mineral("Quartz", 7);
        quartz.shine();
    }
}
```

When executed, this program will create `Mineral` instances for Diamond and Quartz, each displaying its distinct shine based on its hardness value.

Some key observations and terminology:

* An `Object` in Java is an instance of any class, representing specific items with defined properties and behaviors, much like individual minerals on Earth.
* Instance variables such as `hardnessValue` and `name` are unique to each `Mineral` object, representing characteristics analogous to real-world mineral properties.
* The `Mineral` class includes an instance method `shine()`, which demonstrates polymorphism by varying its output based on the mineral's hardness value.
* Instantiation, using the `new` keyword, is essential to spark life into our `Mineral` objects, allowing them to exhibit their unique traits and interactions.
* Accessing an object's members with dot notation (e.g., `diamond.shine()`) simplifies calling methods and retrieving properties of specific instances, paralleling how scientists study individual mineral samples.

By grasping these connections between object-oriented programming principles and the dynamic world of minerals, we gain a deeper appreciation for Java's capabilities and Earth's geological wonders.

**Constructors in Java**

In computer science, particularly in Java programming, a _constructor_ provides a basic foundation similar to how geological models often start with defining specific features of interest.

```java
public class RockSampleLauncher {
    public static void main(String[] args) {
        RockSample rs = new RockSample(12);
        rs.describeSample();
    }
}
```
Here, we use a parameterized constructor to efficiently instantiate rock sample objects, mitigating the need to manually input multiple properties for each instance—akin to organizing mineral data sets in geology.

To harness this functionality in Java, we incorporate a constructor into our `RockSample` class:

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
The constructor, `public RockSample(int m)`, is automatically invoked when creating a `RockSample` through the `new` keyword and an integer parameter, in this case representing mineral composition—similar to how geological properties are initialized in modeling applications.

**Terminology Summary**

**Array Instantiation, Arrays of Objects**

In programming, like managing samples in a geological study, arrays enable bulk handling of related items. For instance:

```java
public class SampleArrayDemo {
    public static void main(String[] args) {
        /* Create an array to hold five mineral composition percentages. */
        int[] compositionPercentages = new int[5];
        compositionPercentages[0] = 45;
        compositionPercentages[1] = 60;
    }
}
```
Similarly, arrays in Java can manage multiple instances of custom objects, such as rock samples:

```java
public class RockSampleArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two rock samples. */
        RockSample[] samples = new RockSample[2];
        samples[0] = new RockSample(25);
        samples[1] = new RockSample(80);

        /* Identify first sample characteristics: 25% mineral composition as sedimentary. */
        samples[0].describeSample();
    }
}
```
The `new` keyword serves dual purposes here: initially to reserve space for two `RockSample` objects in an array, and subsequently to instantiate each individual `RockSample`, illustrating the flexible capabilities of arrays in programming—not unlike cataloging various rock specimens in geology.

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java allows us to define two types of methods:

* Class methods, a.k.a. static methods.
* Instance methods, a.k.a. non-static methods.

Instance methods are actions that can be performed only by a specific instance of a class. In contrast, static methods are actions performed by the class itself, regardless of any instance. Both types are useful in different scenarios. For instance, consider the concept of mineral hardness, which geologists use to classify minerals. A `Hardness` class could define a static method `measure` to evaluate the hardness of minerals such as quartz. By being static, we call it as follows:

```java
hardness = Hardness.measure("Quartz");
```

Had `measure` been an instance method, we would use a somewhat cumbersome syntax. However, since `measure` is static, we avoid the following awkward invocation:

```java
Hardness h = new Hardness();
hardness = h.measure("Quartz");
```

Sometimes, it is practical for a class to include both instance and static methods. Consider a situation where we need to compare the density of two rocks. We could introduce a static method in a `Rock` class that helps us compare such properties.

```java
public static Rock denserRock(Rock r1, Rock r2) {
    return r1.density > r2.density ? r1 : r2;
}
```

This static method could be invoked through the class name, as illustrated below:

```java
Rock r1 = new Rock(2.65);
Rock r2 = new Rock(3.00);
Rock.denserRock(r1, r2);
```

Notice that we've used the class name to invoke this method, since it is static and does not depend on any instance.

Alternatively, `denserRock` could be implemented as an instance method:

```java
public Rock denserRock(Rock r2) {
    return this.density > r2.density ? this : r2;
}
```

Here, the keyword `this` refers to the current rock object. We invoke it on an instance variable, as shown:

```java
Rock r1 = new Rock(2.65);
Rock r2 = new Rock(3.00);
r1.denserRock(r2);
```

**Exercise 1.2.1**: What is incorrect about the following method implementation? Try to reason it out before testing in your IDE:

```java
public static Rock denserRock(Rock r1, Rock r2) {
    if (density > r2.density) {
        return this;
    }
    return r2;
}
```

**Static Variables**

Classes can also have static variables, representing properties belonging to the class as a whole, rather than any specific instance. A geological example could be defining the most prevalent mineral in the Earth's crust:

```java
public class Rock {
    public double density;
    public static String commonestMineral = "Feldspar";
    ...
}
```

Static variables should be referenced via the class name and not an instance, such as `Rock.commonestMineral` instead of `r.commonestMineral`.

Although it is technically permissible to access static variables via an instance, doing so is considered poor style, can lead to confusion, and detracts from clarity.

**Exercise 1.2.2**: Engage with this practical exercise to deepen your understanding:

- Video: [link](https://youtu.be/8Gq-8mVbyFU)
- Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
- Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

Building on our knowledge so far, let's delve into the geological layers of this essential Java method declaration. By breaking it down, we can understand its components in context:

* `public`: This keyword acts as the crust, the outermost layer of our method, making it accessible to the outside world, akin to how landforms are visible on Earth's surface.
* `static`: Similar to stable, enduring geological stratifications, this term indicates the method's stability and independence from any specific instance, like sediment layers that remain constant over time.
* `void`: Representing a barren landscape without yield, it signifies that the method produces no return value, much like a plain devoid of mineral resources.
* `main`: Serving as the core, this is the method's central name where the program begins its execution, similar to a central volcanic vent where eruptions originate.
* `String[] args`: These represent granular components, akin to different mineral deposits dispersed within the substrata of our main method, ready to be analyzed.

**Command Line Arguments**

The main method is called by the Java interpreter itself rather than another class. This is comparable to geological transformations initiated by external forces such as earthquakes or volcanic eruptions. The interpreter supplies these arguments in the form of command line inputs. Consider the following rock formation program `ArgsDemo`:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program displays the primary component or top layer of the command line input, like uncovering the first stratum of rock layers. For instance, executing:

```
$ java ArgsDemo geology is fascinating
geology
```

In this case, `args` forms an array of Strings, akin to a sequence of layered rock samples such as {"geology", "is", "fascinating"}.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Develop a program that aggregates the command line arguments as though they are distinct geological specimens. This task is akin to measuring multiple mineral levels within a formation. Refer to the webcast or consult the main code samples available on GitHub for a comprehensive analysis of the solution.

#### Utilization of Geological Resources in Computer Science <a href="#utilization-of-geological-resources" id="utilization-of-geological-resources"></a>

In the realm of computer science, much like geology, the ability to locate and leverage pre-existing resources is a vital skill. Imagine embarking on a computational project with a vast database of mineral compositions at your disposal—this wealth of data can save time and prevent missteps by offering tested knowledge, mirrored in the extensive archives of both geological and computer science communities.

For this course, you're encouraged to adopt a similar approach, with the following conditions:

* Use the designated resources we provide for your studies.
* Always adhere to proper citation practices for the sources you consult.
* Avoid seeking direct answers for specific project assignments or coding problem sets.

This structure parallels geological fieldwork, where it is perfectly acceptable to research "rock layer analysis techniques," but not to look for "Specific Oregon Rock Formation Analysis Answers." This disciplined approach ensures the integrity of both academic fields.

For more details regarding collaboration and adherence to academic integrity, please refer to the course syllabus.