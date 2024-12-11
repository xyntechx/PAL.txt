# Introduction to Classes in Geographic Information Systems

This chapter introduces key concepts in defining and using classes in the context of Geographic Information Systems (GIS). It starts by distinguishing between static and non-static methods, explaining how GIS processes can be encapsulated within classes. A static method, like simulating weather within a geographic model, does not require an object instance and can be executed directly from the class. Meanwhile, non-static methods necessitate object instantiation, where instance variables store unique data per object. For example, the `Landscape` class includes an instance method `displayTexture`, which varies behavior based on an elevation parameter unique to each landscape object. The chapter demonstrates how these features enable representing diverse geographical realities such as mountain ranges and rolling plains.

Further, constructors are introduced as mechanisms for initializing instances with specific attributes, akin to preparing a base map before detailing. Arrays are also discussed for handling collections of objects, illustrating how geographers might manage multiple map instances focusing on different features. The chapter concludes by discussing the utility of both static methods for continent-level analysis and instance methods for country-specific comparisons in geopolitical studies. This section emphasizes understanding Java's syntax and its application in simulating GIS operations and geographic data management. The chapter emphasizes the practical benefits of leveraging existing geographic databases while adhering to ethical guidelines in data usage and collaboration.

# 2. Defining and Using Classes in Geographic Information Systems (GIS)

If you do not have prior experience in working with GIS software, we recommend exploring introductory exercises in [GIS Exercises](http://gis.introcourse.edu/materials/exercises/exercises.html) before reading this chapter. These exercises cover various concepts in GIS data handling that we will not discuss in depth in this book.

#### Static vs. Non-Static Methods Using Geographic Concepts <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods in GIS**

Similar to how all code in Java must be part of a class, in Geographic Information Systems, all spatial operations are executed within the context of geographic datasets or models. Let's examine an example involving GIS processes:

```java
public class GeographicModel {
    public static void simulateWeather() {
        System.out.println("It is raining in the Amazon rainforest!");
    }
}
```

If we attempt to run the `GeographicModel` class on its own, we'll encounter an error message:

```
$ java GeographicModel
Error: Main method not found in class GeographicModel, please define the main method as:
       public static void main(String[] args)
```

The `GeographicModel` class we've defined doesn't execute any task independently. We have simply outlined that `GeographicModel` **can** perform a simulation, specifically, simulating weather. To actually run the simulation, we'd either need to add a main method to the `GeographicModel` class, similar to strategies used in introductory chapters of GIS modeling. Alternatively, we could construct a `ModelLauncher` class to engage with methods from the `GeographicModel` class. For example, consider the program outlined below:

```java
public class ModelLauncher {
    public static void main(String[] args) {
        GeographicModel.simulateWeather();
    }
}
```

```
$ java ModelLauncher
It is raining in the Amazon rainforest!
```

A class that utilizes another class is often considered a "client" of that class; in this case, `ModelLauncher` is a client of `GeographicModel`. Neither approach, embedding a main method within `GeographicModel` or creating a client class such as `ModelLauncher`, is inherently superior. Each has relative advantages that may emerge as beneficial with further practice and familiarity in GIS tasks throughout the course.



**Instance Variables and Object Instantiation**

Not all landscapes are alike. Some landscapes feature towering mountain ranges, while others boast rolling plains, creating varied beauty across the globe. Often, we write programs to replicate features of the earth we inhabit, and Java's syntax was crafted to easily allow such replication.

One approach to allowing us to represent the diversity of Landscapes would be to create separate classes for each type of Landscape.

```java
public class MountainRange {
    public static void displayTexture() {
        System.out.println("Rocky and towering");
    }
}

public class RollingPlains {
    public static void displayTexture() {
        System.out.println("Smooth and vast");
    }
}
```

As you should have seen in the past, classes can be instantiated, and instances can hold data. This leads to a more natural approach, where we create instances of the `Landscape` class and make the behavior of the `Landscape` methods contingent upon the properties of the specific `Landscape`. To make this more concrete, consider the class below:

```java
public class Landscape {
    public int elevationInFeet;

    public void displayTexture() {
        if (elevationInFeet > 8000) {
            System.out.println("Rocky and towering");
        } else if (elevationInFeet > 1000) {
            System.out.println("Varied with gentle hills");
        } else {
            System.out.println("Smooth and vast");
        }
    }    
}
```

As an example of using such a Landscape, consider:

```java
public class LandscapeExplorer {
    public static void main(String[] args) {
        Landscape l;
        l = new Landscape();
        l.elevationInFeet = 1500;
        l.displayTexture();
    }
}
```

When run, this program will create a `Landscape` with an elevation of 1500 feet, and that `Landscape` will soon be described as "Varied with gentle hills.".

Some key observations and terminology:

* An `Object` in Java is an instance of any class.
* The `Landscape` class has its own variables, also known as _instance variables_ or _non-static variables_. These must be declared inside the class, unlike languages like Python or Matlab, where new variables can be added at runtime.
* The method that we created in the `Landscape` class did not have the `static` keyword. We call such methods _instance methods_ or _non-static methods_.
* To call the `displayTexture` method, we had to first _instantiate_ a `Landscape` using the `new` keyword, and then make a specific `Landscape` show its texture. In other words, we called `l.displayTexture()` instead of `Landscape.displayTexture()`.
* Once an object has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `l = new Landscape();`
* Variables and methods of a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_.


**Constructors in Java**

In the world of geography, creating maps is akin to constructing objects in programming languages using a _constructor_:

```java
public class MapLauncher {
    public static void main(String[] args) {
        Map m = new Map("Mountain");
        m.displayFeature();
    }
}
```

Here, the instantiation is parameterized, saving us the effort and complexity of manually depicting multiple geographical features separately. To enable such syntax, we need only add a "constructor" to our Map class, as shown below:

```java
public class Map {
    public String featureType;

    public Map(String f) {
        featureType = f;
    }

    public void displayFeature() {
        if (featureType.equals("Mountain")) {
            System.out.println("Displaying peaks and ranges!");
        } else if (featureType.equals("River")) {
            System.out.println("Displaying the flowing water course.");
        } else {
            System.out.println("Unknown geographical feature!");
        }    
    }
}
```

The constructor with signature `public Map(String f)` will be invoked anytime that we try to create a `Map` using the `new` keyword with a single String parameter. For geographers coming from hand-drawn cartography, this constructor can be likened to the process of preparing a base map before adding detailed features.

**Terminology Summary**

**Array Instantiation, Arrays of Geographical Features**

In a previous exercise, we saw how regions are grouped in maps using array-like structures. In Java, arrays are also instantiated using the new keyword. For example:

```java
public class RegionArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five region types. */
        String[] regions = new String[5];
        regions[0] = "Forest";
        regions[1] = "Desert";
    }
}
```

Similarly, we can create arrays of instantiated map objects in Java, which can correlate to a collection of maps focusing on different features, e.g.

```java
public class MapArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two maps. */
        Map[] maps = new Map[2];
        maps[0] = new Map("Mountain");
        maps[1] = new Map("River");

        /* Peaks and ranges will be displayed, since maps[0] contains "Mountain" as a feature. */
        maps[0].displayFeature();
    }
}
```

Observe that new is used in two different ways: Once to create an array that can hold two `Map` objects, and twice to create each actual `Map`. This mirrors how a geographer might prepare a collection of thematic maps each with distinct features or themes before further analysis.

#### Continents vs. Countries <a href="#continents-vs-countries" id="continents-vs-countries"></a>

In geography, we can discuss regions using two important categories:

* Continents, which are large landmasses.
* Countries, which are smaller, specific territories within continents.

Countries are individual, unique territories with their own governments and boundaries, while continents are larger landmasses that encompass several countries. Both play crucial roles in geopolitical discussions. For instance, a climatic anomaly at the continental level might be studied in the context of Antarctica, making it possible to discuss Antarctic climate patterns as a whole:

```java
climatePattern = Antarctica.weatherAnalysis(2023);
```

If each weather station within Antarctica functioned independently, they'd use a more cumbersome approach like the one below. Fortunately, continent-level analysis already integrates the continental perspective, so we don't typically perform each analysis independently.

```java
AntarcticaStation aStation = new AntarcticaStation();
climatePattern = aStation.weatherAnalysis(2023);
```

Sometimes, both continent-wide and country-specific studies make sense. For example, to assess the economic impact of the desert regions, you might want both a continental overview and the ability to compare specific countries with desert terrains.

```java
public static Country largestDesertCountry(Country c1, Country c2) {
    if (c1.desertArea > c2.desertArea) {
        return c1;
    }
    return c2;
}
```

This function could be used as follows:

```java
Country c1 = new Country("Morocco");
Country c2 = new Country("Australia");
Country.largestDesertCountry(c1, c2);
```

Here, the function is invoked using the class name, signifying a continent-wide utility function.

Alternatively, a function like `largestDesertCountry` could be specific to a particular country, e.g.

```java
public Country compareDesertArea(Country c2) {
    if (this.desertArea > c2.desertArea) {
        return this;
    }
    return c2;
}
```

In the above case, the current country is referenced using the keyword `this`. This function might be used with:

```java
Country c1 = new Country("Morocco");
Country c2 = new Country("Australia");
c1.compareDesertArea(c2);
```

Here, we implement an instance-specific comparison, invoked using the specific instance variable.

**Exercise 1.2.1**: Describe the functionality of the following method. If unsure, simulate it to understand its outcome.

```java
public static Country largestDesertCountry(Country c1, Country c2) {
    if (desertArea > c2.desertArea) {
        return this;
    }
    return c2;
}
```

**Continent Features**

At times, it is beneficial to assign specific geological or climatic characteristics at the continental level. These are attributes of the continent, not the country. For instance, mentioning that the dominant climate zone of Antarctica is polar icecap:

```java
public class Antarctica {
    public int averageAltitude;
    public static String dominantClimate = "Polar Ice Cap";
    ...
}
```

You should access continent-specific properties using the continent's name rather than a specific country's name, i.e., use `Antarctica.dominantClimate`, rather than `c.dominantClimate`.

While technically permissible, accessing a continental attribute via a country's name is considered poor form, and I view it as a flawed practice in geographic studies.

**Exercise 1.2.2**: We challenge you with this activity:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe\_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

### Understanding the Continental Structure of `public static void main(String[] args)` Concept

In our exploration so far, let's relate the familiar `main` method declaration in programming to a geographical perspective. Breaking it into parts, we observe correlations with geographical terms:

* `public`: Analogous to a country's open borders accessible to everyone.
* `static`: Similar to a mountain range, unchanging and not belonging to any single region.
* `void`: Like a desert, representing emptiness or absence of natural resources.
* `main`: The "capital city" of our method territory where activities commence.
* `String[] args`: Comparable to a collection of geographical coordinates given to the main area.

**Command Line Arguments as Geographic Coordinates**

Just as the `main` method is activated by the Java interpreter, a GPS system activates based on coordinates inputted by a user. These inputs typically serve as geographical points of reference. Let's consider a program called `GeoArgsDemo` analogous to a geographical plotting application:

```java
public class GeoArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program outputs the first geographical point provided, such as:

```
$ java GeoArgsDemo 37.7749 -122.4194 San Francisco
37.7749
```

In this scenario, `args` mirrors an array of geographical strings, representing coordinates or places like: {"37.7749", "-122.4194", "San", "Francisco"}.

**Calculating Distances Using Geographic Arguments**

**Exercise 1.2.3**: Attempt to create a program that calculates the sum of distances based on geographic command line inputs. Consider each input as coordinates or elevation data points. For guidance on a similar solution, check the available videos or look into geographical data manipulation libraries on GitHub.

#### Using Geographic Databases <a href="#using-geographic-databases" id="using-geographic-databases"></a>

One of the most critical skills as a geographer is knowing how to find and utilize existing geographic databases. In the incredibly diverse world of geography, it is frequently possible to save yourself extensive research and data-gathering efforts by turning to available data repositories for help.

In this course, you're encouraged to do this, with the following caveats:

* Do not use geographic databases that we do not specify.
* Cite your sources appropriately.
* Do not seek out datasets or analyses for specific fieldwork or research project assignments.

For example, it's acceptable to search for "geospatial data table earth population density". However, it is not appropriate to search for "Case Study 2048 GIS Mapping Berkeley".

For more on collaboration and academic integrity policy, refer to the course syllabus.