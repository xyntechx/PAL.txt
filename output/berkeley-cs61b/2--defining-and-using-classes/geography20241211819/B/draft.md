# Defining and Using Classes

In this chapter, the focus is on understanding how to define and utilize classes in Java, a fundamental aspect of object-oriented programming. The chapter explains various concepts through geographic analogies, such as views from a mountain or different terrain types, to make the learning experience relatable and engaging. Key topics discussed include creating classes and objects, implementing instance variables, and instance methods. Through examples, it is shown how classes can model real-world entities, like landscapes, with instance variables representing attributes (e.g., elevation) and methods for behaviors (e.g., describing terrain). A distinction is also made between static and instance methods, illustrating how the former relates to the class itself while the latter pertains to individual objects.

Moreover, the chapter introduces the concept of constructors, which are special methods used to instantiate objects with specific attributes right from their creation. By using examples like mountain ranges, the text demonstrates how constructors facilitate a structured way of initializing objects. The chapter also covers more advanced topics such as static variables and methods, arrays of objects, and the "main" method structure (`public static void main(String[] args)`). This last section provides insights into the use of command-line arguments, revealing how a Java application can be made more dynamic by accepting input at the start of execution. Through these geographic-themed scenarios and exercises, the chapter solidifies one's understanding of key class-based programming principles in Java.



2. Defining and Using Classes

If you do not have prior navigation experience, we recommend that you work through the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before reading this chapter. It will cover various geographic concepts that we will not discuss in the book.

#### Elevation vs. Sea-Level Views <a href="#elevation-vs-sea-level-views" id="elevation-vs-sea-level-views"></a>

**Elevation Views**

All geographies must be part of a region (or something similar to a region, which we'll learn about later). Most landscapes are depicted with specific viewpoints. Let's consider an example:

```java
public class Mountain {
    public static void viewFromPeak() {
        System.out.println("Majestic panorama!");
    }
}
```

If we try exploring the `Mountain` region like this, we'll simply get an error message:

```
$ java Mountain
Error: Main viewpoint not found in region Mountain, please define the main viewpoint as:
       public static void main(String[] args)
```

The `Mountain` region we've defined doesn't manifest any activity. We've simply defined something that `Mountain` **can** offer, namely a view from its peak. To actually explore the region, we'd either need to add a main viewpoint to the `Mountain` class, as we saw in chapter 1.1. Or we could create a separate [`MountainExplorer`](https://www.youtube.com/watch?v=Q-LE-jJQLTM) class that extracts views from the `Mountain` region. For example, consider the program below:

```java
public class MountainExplorer {
    public static void main(String[] args) {
        Mountain.viewFromPeak();
    }
}
```

```
$ java MountainExplorer
Majestic panorama!
```

A region that facilitates another region's exploration is sometimes called a "viewer" of that region, i.e. `MountainExplorer` is a viewer of `Mountain`. Neither of the two techniques is better: Adding a main viewpoint to `Mountain` may be better in some situations, and creating a viewer class like `MountainExplorer` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout the journey.

## Instance Variables and Object Instantiation Reimagined Through Geography

Not all landscapes are alike. Some landscapes are characterized by rolling hills and lush valleys, while others feature towering mountains and expansive deserts, offering a diverse array of vistas that each have their unique charm and characteristics. Often, we write programs to mimic features of the universe we inhabit, and Java's syntax was crafted to easily allow such mimicry.

One approach to allowing us to represent the spectrum of Earth's landscapes would be to create separate classes for each type of landscape.

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

As you should have seen in the past, classes can be instantiated, and instances can hold data. This leads to a more natural approach, where we create instances of the `Landscape` class and make the behavior of the `Landscape` methods contingent upon the properties of the specific `Landscape`. To make this more concrete, consider the class below:

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

As an example of using such a Landscape, consider:

```java
public class LandscapeExploration {
    public static void main(String[] args) {
        Landscape l;
        l = new Landscape();
        l.elevationInMeters = 500;
        l.describeTerrain();
    }
}
```

When run, this program will create a `Landscape` with an elevation of 500 meters, and that `Landscape` will soon be described as having "Rolling hills and pastoral vistas."

Some key observations and terminology:

* An `Object` in Java is an instance of any class.
* The `Landscape` class has its own variables, also known as _instance variables_ or _non-static variables_. These must be declared inside the class, unlike languages like Python or Matlab, where new variables can be added at runtime.
* The method that we created in the `Landscape` class did not have the `static` keyword. We call such methods _instance methods_ or _non-static methods_.
* To call the `describeTerrain` method, we had to first _instantiate_ a `Landscape` using the `new` keyword, and then make a specific `Landscape` described. In other words, we called `l.describeTerrain()` instead of `Landscape.describeTerrain()`.
* Once an object has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `l = new Landscape();`
* Variables and methods of a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_.


**Constructors in Java through Geographical Concepts**

Much like how geographers classify regions using specific defining characteristics, in object-oriented programming, we construct objects using a specialized tool called a _constructor_.

```java
public class MountainRangeLauncher {
    public static void main(String[] args) {
        MountainRange himalayas = new MountainRange(8848);
        himalayas.displayCharacteristics();
    }
}
```

Here, the instantiation of a MountainRange is "parameterized" by its defining characteristic, saving us the time of manually assigning values to potentially many variables for each new region we study. To allow this seamless setup, we introduce a "constructor" for our MountainRange class as outlined below:

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

The constructor with the signature `public MountainRange(int elevation)` acts as the initial defining tool whenever we define a MountainRange using a characteristic like elevation. For those familiar with geographic modeling, this is akin to using a specialized algorithm to delineate a region based on climatic data.

**Terminology Summary**

**Geographical Region Instantiation, Arrays of Regions**

As explained in HW0, much like organizing regions by climate in geography, arrays can also be established in Java using the 'new' keyword to represent different datasets. For example:

```java
public class ClimateZoneDemo {
    public static void main(String[] args) {
        /* Create an array representing five climatic zones. */
        int[] climateZones = new int[5];
        climateZones[0] = 1; // tundra
        climateZones[1] = 2; // arid
    }
}
```

Similarly, we can create arrays of instantiated objects, akin to studying multiple geographical settings. For example:

```java
public class RangeArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two mountain ranges. */
        MountainRange[] ranges = new MountainRange[2];
        ranges[0] = new MountainRange(1500);
        ranges[1] = new MountainRange(6000);

        /* "Low mountains" will display, as ranges[0] has elevation 1500. */
        ranges[0].displayCharacteristics();
    }
}
```

Observe that 'new' is utilized in different contexts: once to sketch out an array capable of holding two MountainRange objects, and twice to create each actual MountainRange representation.

#### Continental Methods vs. Regional Methods <a href="#continental-methods-vs-regional-methods" id="continental-methods-vs-regional-methods"></a>

Geographical modeling allows us to define two types of processes:

* Continental methods, a.k.a. static methods.
* Regional methods, a.k.a. non-static methods.

Regional processes are actions or changes that can be observed only in a specific region of a continent. Static methods represent processes that are relevant to the continent as a whole. Both are significant under different geographical circumstances. As an example of a static method, the `Earth` class provides a `calculateGravity` method. Because it is static, we can call it as follows:

```java
x = Earth.calculateGravity(9.8);
```

If `calculateGravity` had been a regional method, the invocation would require this cumbersome syntax. Thankfully `calculateGravity` is a static method, so we don't have to do this in practical geographic models.

```java
Earth e = new Earth();
x = e.calculateGravity(9.8);
```

Sometimes, it makes sense for a geographical system to incorporate both regional and static methods. For example, suppose we want to compare two mountain ranges. One approach is to add a static method for comparing Mountains.

```java
public static Mountain maxHeightMountain(Mountain m1, Mountain m2) {
    if (m1.height > m2.height) {
        return m1;
    }
    return m2;
}
```

This method could be invoked by, for example:

```java
Mountain m = new Mountain(4500);
Mountain m2 = new Mountain(8848);
Mountain.maxHeightMountain(m, m2);
```

Notice that we've called this method using the class name, as it is a static method.

We could also have implemented `maxHeightMountain` as a non-static method, e.g.

```java
public Mountain maxHeightMountain(Mountain m2) {
    if (this.height > m2.height) {
        return this;
    }
    return m2;
}
```

Above, we use the keyword `this` to refer specifically to the mountain instance in question. This method could be invoked, for example, with:

```java
Mountain m = new Mountain(4500);
Mountain m2 = new Mountain(8848);
m.maxHeightMountain(m2);
```

Here, we engage the method using a specific instance of a mountain.

**Exercise 1.2.1**: What would the following method do? If you're not sure, try it out.

```java
public static Mountain maxHeightMountain(Mountain m1, Mountain m2) {
    if (height > m2.height) {
        return this;
    }
    return m2;
}
```

**Static Variables**

It can be strategically beneficial for geographical classes to have static variables. These are properties characteristic of the continent itself, rather than individual regions. For example, we might note that the latitudinal range of the Sahara is between 15° and 30° N:

```java
public class Sahara {
    public int areaSize;
    public static String latitudinalRange = "15° to 30° N";
    ...
}
```

Static variables should be accessed using the name of the geography class rather than a specific instance, e.g. you should use `Sahara.latitudinalRange`, not `s.latitudinalRange`.

While Java allows you to technically access a static variable using an instance name, it is considered poor practice, confusing, and, in my opinion, a mistake by the Java developers.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe\_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)



#### public static void main(String\[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

Let's navigate the landscape of the declaration we've been using for the main method. It's time to map out its elements:

* `public`: This visibility scope acts like an open border, allowing any external part of the program to access this method.
* `static`: Much like a geographic landmark that stands independently, this method is not tied to any specific instance.
* `void`: This denotes an absence, similar to a desert with no water bodies—it provides no return value.
* `main`: This is the method's name, akin to naming a central city or capital.
* `String[] args`: These are like rivers, flowing parameters that carry data into the main method.

**Command Line Arguments**

Since main is called by the Java interpreter itself rather than another Java class, it's similar to a central hub receiving traveler inputs from various regions through command line arguments. Consider the `ArgsDemo` terrain below, where each argument travels into the program:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program acts as a scout, reporting back the first traveler it encounters in the argument list:

```
$ java ArgsDemo these are command line arguments
these
```

In the landscape above, `args` will be an array of Strings, with entries {"these", "are", "command", "line", "arguments"}—much like a group of explorers setting out on a journey together.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Chart out a program that sums up these command line travelers, assuming they represent numerical values. Find a pathway to the solution in the webcast or buried in the GitHub repository.

#### Utilizing Geographic Databases <a href="#utilizing-geographic-databases" id="utilizing-geographic-databases"></a>

One of the most vital skills as a geographer is knowing how to find and utilize existing geographic databases. In the glorious modern age, it is often possible to save yourself tons of field work and data collection by turning to digital resources for help.

In this field, you're welcome to do this, with the following caveats:

* Do not use geographic data sets that are not provided by verified sources.
* Cite your data sources.
* Do not search for specific analysis or interpretations for specific geographic case studies or research problems.

For example, it's fine to search for "convert map coordinate system GIS". However, it is not OK to search for "Amazon Deforestation Study GeoAnalytics".

For more on collaboration and academic honesty policy, see the department guidelines.