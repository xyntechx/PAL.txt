# Defining and Using Classes

In this chapter, the focus is on understanding how to define and utilize classes in Java, a fundamental aspect of object-oriented programming. The chapter explains various concepts through geographic analogies, such as views from a mountain or different terrain types, to make the learning experience relatable and engaging. Key topics discussed include creating classes and objects, implementing instance variables, and instance methods. Through examples, it is shown how classes can model real-world entities, like landscapes, with instance variables representing attributes (e.g., elevation) and methods for behaviors (e.g., describing terrain). A distinction is also made between static and instance methods, illustrating how the former relates to the class itself while the latter pertains to individual objects.

Moreover, the chapter introduces the concept of constructors, which are special methods used to instantiate objects with specific attributes right from their creation. By using examples like mountain ranges, the text demonstrates how constructors facilitate a structured way of initializing objects. The chapter also covers more advanced topics such as static variables and methods, arrays of objects, and the "main" method structure (`public static void main(String[] args)`). This last section provides insights into the use of command-line arguments, revealing how a Java application can be made more dynamic by accepting input at the start of execution. Through these geographic-themed scenarios and exercises, the chapter solidifies one's understanding of key class-based programming principles in Java.

### 2. Defining and Using Classes

If you're new to programming and geographic navigation simultaneously, we highly recommend completing the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) to get acquainted with some fundamental geographic concepts. This chapter will then build upon those concepts without revisiting them in detail.

#### Elevation vs. Sea-Level Views <a href="#elevation-vs-sea-level-views" id="elevation-vs-sea-level-views"></a>

**Elevation Views**

In geography, recognizing how landscapes form part of broader regions assists in understanding how software classes function within a program. Just as landscapes are often depicted from different perspectives, software classes encapsulate varying functionalities. Let's dive deeper into this analogy:

```java
public class Mountain {
    public static void viewFromPeak() {
        System.out.println("Majestic panorama!");
    }
}
```

Attempting to navigate the `Mountain` class without a clear entry point results in an error message:

```
$ java Mountain
Error: Main viewpoint not found in region Mountain, please define the main viewpoint as:
       public static void main(String[] args)
```

The `Mountain` class above doesn't carry out any actions independently. Instead, it offers a distinct vantage point – in this case, a view from its peak. To actually "explore" or utilize the `Mountain` class, we should either incorporate a main entry point within it or craft an external explorer, such as the `MountainExplorer` class, to initiate its features. Here's an example of such a setup:

```java
public class MountainExplorer {
    public static void main(String[] args) {
        Mountain.viewFromPeak();
    }
}
```

Running `MountainExplorer` lets us "explore" the Mountain's viewpoint:

```
$ java MountainExplorer
Majestic panorama!
```

In programming terms, a class that serves to operationalize another class could be described as a "viewer" of the first class. Here, `MountainExplorer` functions as a viewer of `Mountain`. Each approach—embedding a primary function within the class itself or employing a separate viewer class—comes with its advantages. The best choice varies with context and requirements, which we will better understand as we further explore object-oriented programming principles throughout this text.

## Instance Variables and Object Instantiation Reimagined Through Geography

Imagine the diverse terrains found across the globe. Some regions are defined by their rolling hills and lush valleys, while others boast towering mountains and vast deserts. Each has unique characteristics and offers a particular charm. Similarly, programming languages like Java provide mechanisms to represent such diversity through classes and objects.

Consider a program designed to replicate the various landscapes of Earth; one approach would involve creating separate classes for each landscape type:

```java
public class Valley {
    public static void describeTerrain() {
        System.out.println("Gentle slopes with vibrant greenery.");
    }
}

public class Mountain {
    public static void describeTerrain() {
        System.out.println("Soaring peaks and rocky crags!");
    }
}
```

From past experience, we know that classes can be instantiated, and instances can store specific data. This enables a more flexible approach, where instances of a generic `Landscape` class can be tailored to depict different terrains based on their properties. Consider the class below:

```java
public class Landscape {
    public int elevationInMeters;

    public void describeTerrain() {
        if (elevationInMeters < 200) {
            System.out.println("Flat and fertile plains.");
        } else if (elevationInMeters < 1000) {
            System.out.println("Rolling hills and pastoral vistas.");
        } else {
            System.out.println("Majestic mountains and rugged ridges!");
        }
    }    
}
```

Let's explore how this class is used:

```java
public class LandscapeExploration {
    public static void main(String[] args) {
        Landscape landscapeInstance = new Landscape();
        landscapeInstance.elevationInMeters = 500;
        landscapeInstance.describeTerrain();
    }
}
```

When executed, this program creates a `Landscape` object with an elevation of 500 meters, which is then described as having "Rolling hills and pastoral vistas."

Key observations and terminology:

* An `Object` in Java is an instance of a class.
* The `Landscape` class contains its own variables, known as _instance variables_ or _non-static variables_. These must be declared within the class, unlike in some other languages where variables can be dynamically added.
* The method defined within the `Landscape` class lacks the `static` keyword, making it an _instance method_ or _non-static method_.
* To invoke the `describeTerrain` method, we first _instantiate_ a `Landscape` with the `new` keyword and then call the method on a specific instance, i.e., `landscapeInstance.describeTerrain()` rather than `Landscape.describeTerrain()`.
* After an object has been instantiated, it can be _assigned_ to a _declared_ variable of the corresponding type, for example, `landscapeInstance = new Landscape();`
* A class's variables and methods are referred to as its _members_.
* Members of a class are accessed using _dot notation_.

By marrying geography with programming concepts, we can create intuitive and relatable examples, assisting learners in grasping the foundational elements of Java objects and classes more effectively.

**Constructors in Java through Geographical Concepts**

Imagine how geographers define regions by key features like climate and altitude. Similarly, in object-oriented programming, we construct objects using a specialized feature called a _constructor_. This allows us to create objects with specified characteristics, streamlining the process much like defining physical regions with clear boundaries.

```java
public class MountainRangeLauncher {
    public static void main(String[] args) {
        MountainRange himalayas = new MountainRange(8848);
        himalayas.displayCharacteristics();
    }
}
```

Here, we initiate a MountainRange object "parameterized" by its defining characteristic—elevation—saving us the repetitive task of assigning values manually to multiple attributes. This is akin to automatically classifying geographical regions based on altitude ranges. Our "constructor" helps us achieve this efficiency for the MountainRange class, as seen below:

```java
public class MountainRange {
    public int highestPeak;

    public MountainRange(int elevation) {
        highestPeak = elevation;
    }

    public void displayCharacteristics() {
        if (highestPeak < 1000) {
            System.out.println("hills.");
        } else if (highestPeak < 5000) {
            System.out.println("low mountains.");
        } else {
            System.out.println("high mountains!");
        }    
    }
}
```

The constructor with the signature `public MountainRange(int elevation)` is like deploying a standard set of criteria for identifying a MountainRange. For geographers, this is similar to using criteria such as elevation or vegetation to categorize a terrain feature.

**Terminology Summary**

**Geographical Region Instantiation and Arrays of Regions**

Just as geographers organize regions by characteristics like climate, arrays in Java can represent collections of data using the 'new' keyword to signify different sets of information. For example:

```java
public class ClimateZoneDemo {
    public static void main(String[] args) {
        /* Create an array representing various climate zones. */
        int[] climateZones = new int[5];
        climateZones[0] = 1; // tundra
        climateZones[1] = 2; // arid
    }
}
```

Similarly, arrays can be used to store multiple instantiated objects, akin to organizing multiple geographical features for study. For instance:

```java
public class RangeArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two mountain ranges. */
        MountainRange[] ranges = new MountainRange[2];
        ranges[0] = new MountainRange(1500);
        ranges[1] = new MountainRange(6000);

        /* "Low mountains" will display as ranges[0] has elevation 1500. */
        ranges[0].displayCharacteristics();
    }
}
```

Notice how the 'new' keyword is employed here for different tasks: first, to initiate an array that will hold MountainRange objects, and then to actually create each MountainRange entity. This parallel with geographic elements underscores how programming can simplify organization just as maps and charts do in physical geography.

#### Continental Methods vs. Regional Methods <a href="#continental-methods-vs-regional-methods" id="continental-methods-vs-regional-methods"></a>

Geographical modeling allows us to define two types of processes:

* **Continental methods**: Also known as static methods, these are applicable across the entire landmass.
* **Regional methods**: Alternatively referred to as non-static methods, these are specific to particular areas or regions.

**Regional processes** reflect changes observable only in distinct areas within a continent, akin to neighborhood variations in a city. On the other hand, static methods exemplify processes relevant to entire continents, such as gravitational forces.

For instance, consider the `Earth` class with a `calculateGravity` method—a static method indicative of consistent gravitational force across a continent:

```java
x = Earth.calculateGravity(9.8);
```

Were `calculateGravity` a regional method, invoking it would demand a specific instance of the `Earth` class:

```java
Earth e = new Earth();
x = e.calculateGravity(9.8);
```

In geographical modeling, leveraging both regional and static methods judiciously is imperative. Assume we aim to evaluate two mountain ranges' heights. A static method could be employed for this purpose:

```java
public static Mountain maxHeightMountain(Mountain m1, Mountain m2) {
    if (m1.height > m2.height) {
        return m1;
    }
    return m2;
}
```

Invocation follows a direct approach:

```java
Mountain m = new Mountain(4500);
Mountain m2 = new Mountain(8848);
Mountain.maxHeightMountain(m, m2);
```

This methodology, using the class name, reflects a static method.

Conversely, implementing `maxHeightMountain` as a non-static, regional method utilizes instance-based engagement:

```java
public Mountain maxHeightMountain(Mountain m2) {
    if (this.height > m2.height) {
        return this;
    }
    return m2;
}
```

Invocation requires attention to specific mountain instances:

```java
Mountain m = new Mountain(4500);
Mountain m2 = new Mountain(8848);
m.maxHeightMountain(m2);
```

This instance-specific engagement aligns with regional method use.

**Exercise 1.2.1**: Analyze what this method would accomplish. If uncertain, attempt a practical trial.

```java
public static Mountain maxHeightMountain(Mountain m1, Mountain m2) {
    if (height > m2.height) {
        return this;
    }
    return m2;
}
```

**Delving into Static Variables**

Effective geographical classes may incorporate static variables, reserved for attributes concerning entire landmasses rather than secluded areas. For instance, the Sahara's latitudinal breadth (15° - 30° N) may be denoted as a static variable:

```java
public class Sahara {
    public int areaSize;
    public static String latitudinalRange = "15° to 30° N";
    ...
}
```

Static variables merit access via a class identifier, e.g., `Sahara.latitudinalRange`, eschewing instance references like `s.latitudinalRange`.

Even though Java permits static variable access via instance identifiers, this practice is discouraged due to potential confusion, constituting what many practitioners consider an oversight by Java's designers.

**Exercise 1.2.2**: Fulfill this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

Let's explore the territory of the declaration we've been using for Java's main method. We'll chart out each part:

* `public`: This visibility level is like an open border between countries, allowing any external part of the program—no matter where—to access this method whenever needed.
* `static`: This is akin to a prominent geographic landmark that remains constant, not tied to any specific instance or object, standing independently in the landscape.
* `void`: This signifies an absence, much like an arid desert spanning the horizon—this method does not yield any return value.
* `main`: The method's name serves as a capital city within our program, representing a central point of focus where the program begins its journey.
* `String[] args`: These are like tributaries feeding a river, bringing the vital input data into the main method.

**Command Line Arguments**

The main method is invoked by the Java interpreter itself, operating like a central hub welcoming input from various regions in the form of command line arguments. Visualize the program as a map called `ArgsDemo`, with each argument like a caravan traversing into the program:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

In this program, we take the role of a scout, reporting back the first caravan encountered in the list of arguments:

```
$ java ArgsDemo these are command line arguments
these
```

In our mapped journey above, `args` is an array of Strings, resembling a convoy of explorers embarking together: {"these", "are", "command", "line", "arguments"}.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Draft a program that calculates the sum of these command line arguments, assuming they signify numerical values. Seek out a route to the solution in the webcast or delve into the GitHub repository.

#### Utilizing Geographic Databases <a href="#utilizing-geographic-databases" id="utilizing-geographic-databases"></a>

In computer science, much like geography, effectively harnessing existing databases is a fundamental skill. Geographic databases, specifically, hold immense potential to streamline research efforts in the field of geography. This is akin to leveraging pre-existing classes and libraries in programming to enhance productivity and efficiency.

Here are some key considerations for utilizing digital geographic resources responsibly:

* Ensure that geographic datasets are sourced from reputable and verified sources. Just as in programming, where using trusted libraries is critical to avoiding security vulnerabilities, your research should rely on credible databases to maintain accuracy and reliability.
* Always document and cite your data sources accordingly. This practice is similar to citing code libraries in programming, upholding the principles of academic integrity and transparency.
* While it's beneficial to seek information on methods like "convert map coordinate system using GIS tools," refrain from searching for direct analysis on specific geographic research problems or case studies, such as "Amazon Deforestation Study GeoAnalytics." Understanding and implementing foundational concepts without over-relying on pre-processed analyses fosters deeper learning and research skills.

For more information on maintaining integrity in your research approaches, refer to the academic honesty guidelines set by your department.

This approach not only respects scholarly practices but enhances one’s skillset in both geography and computer science. By drawing parallels with CS concepts, geographers can grasp the importance of foundational methodologies akin to algorithms and data structures used in software development.