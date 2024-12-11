# Introduction to Classes in Geographic Information Systems

This chapter introduces key concepts in defining and using classes in the context of Geographic Information Systems (GIS). It starts by distinguishing between static and non-static methods, explaining how GIS processes can be encapsulated within classes. A static method, like simulating weather within a geographic model, does not require an object instance and can be executed directly from the class. Meanwhile, non-static methods necessitate object instantiation, where instance variables store unique data per object. For example, the `Landscape` class includes an instance method `displayTexture`, which varies behavior based on an elevation parameter unique to each landscape object. The chapter demonstrates how these features enable representing diverse geographical realities such as mountain ranges and rolling plains.

Further, constructors are introduced as mechanisms for initializing instances with specific attributes, akin to preparing a base map before detailing. Arrays are also discussed for handling collections of objects, illustrating how geographers might manage multiple map instances focusing on different features. The chapter concludes by discussing the utility of both static methods for continent-level analysis and instance methods for country-specific comparisons in geopolitical studies. This section emphasizes understanding Java's syntax and its application in simulating GIS operations and geographic data management. The chapter emphasizes the practical benefits of leveraging existing geographic databases while adhering to ethical guidelines in data usage and collaboration.

# 2. Defining and Using Classes in Geographic Information Systems (GIS)

If you do not have prior experience with GIS software, it might be beneficial to explore some basic exercises in [GIS Exercises](http://gis.introcourse.edu/materials/exercises/exercises.html) before diving into this chapter. These exercises introduce concepts in GIS data handling that we will not cover extensively here.

#### Using Static and Non-Static Methods in Geographic Models <a href="#using-static-and-non-static-methods" id="using-static-and-non-static-methods"></a>

**Static Methods in GIS**

In both Java programming and Geographic Information Systems (GIS), the concept of classes is essential. In GIS, spatial operations are generally executed within geographic datasets or models. Consider the following Java example that relates to GIS processes:

```java
public class GeographicModel {
    public static void simulateWeather() {
        System.out.println("Simulating weather changes such as rainfall in the Amazon rainforest!");
    }
}
```

Attempting to run the `GeographicModel` class on its own without further context would result in an error:

```
$ java GeographicModel
Error: Main method not found in class GeographicModel, please define the main method as:
       public static void main(String[] args)
```

The `GeographicModel` class is designed to perform tasks like weather simulations. However, it doesn't execute automatically without a main method. To run the simulation, we need to incorporate a main method, or alternatively, create a `ModelLauncher` client class to call methods from `GeographicModel`:

```java
public class ModelLauncher {
    public static void main(String[] args) {
        GeographicModel.simulateWeather();
    }
}
```

When executed, the result illustrates how GIS models work within a coding framework:

```
$ java ModelLauncher
Simulating weather changes such as rainfall in the Amazon rainforest!
```

In this scenario, a client class like `ModelLauncher` enables `GeographicModel` to perform its functions. Whether to use a main method within `GeographicModel` or a separate client class involves various considerations, each with its own advantages. Understanding these approaches expands your ability to work effectively with GIS simulations in Java, a beneficial component of GIS applications you might build throughout this course.

**Instance Variables and Object Instantiation**

Just like the diverse terrains of our planet, from majestic mountain ranges to gentle rolling plains, programming offers diverse ways to represent and manage data. With Java, we can effectively mirror these diverse landscapes through classes and objects.

To capture the varied features of different types of Landscapes, we might initially consider creating a distinct class for each one.

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

However, a more scalable and object-oriented approach is to instantiate objects of a single `Landscape` class, using instance variables to manage data specific to each object. This allows different `Landscape` objects to exhibit unique behaviors based on their properties. Consider the following class:

```java
public class Landscape {
    private int elevationInFeet;

    public Landscape(int elevation) {
        this.elevationInFeet = elevation;
    }

    public void displayTexture() {
        if (elevationInFeet > 8000) {
            System.out.println("Rocky and towering");
        } else if (elevationInFeet > 1000) {
            System.out.println("Varied with gentle hills");
        } else {
            System.out.println("Smooth and vast");
        }
    }    

    public int getElevationInFeet() {
        return elevationInFeet;
    }
}
```

This class uses a constructor to set the elevation when creating a new `Landscape` object, providing flexibility and encapsulation. Let's explore how you might use this class:

```java
public class LandscapeExplorer {
    public static void main(String[] args) {
        Landscape l = new Landscape(1500);
        l.displayTexture();
    }
}
```

By running this program, a `Landscape` object with an elevation of 1500 feet would describe itself as "Varied with gentle hills."

Key points and terminology:

* An `Object` in Java represents an instance of a class, encapsulating its state and behaviors.
* The `Landscape` class defines properties as _instance variables_. Unlike languages such as Python, these variables are declared in the class and cannot be arbitrarily created or extended at runtime.
* The class constructor allows for initialization of instance variables, instantiating a `Landscape` with specific properties.
* Methods without the `static` keyword, such as `displayTexture`, are known as _instance methods_ and require an object of the class to be called.
* A `new` keyword initializes new objects, and these objects are then linked to references like `l` using the dot notation to access their methods and properties.
* Remember, members of a class, whether variables or methods, are integral to defining the data and behaviors afforded by that class architecture in programming.

**Constructors in Java**

In the world of geography, creating maps is akin to constructing objects in programming languages using a _constructor_. Just as a cartographer might specialize a base map with different features, programmers initialize objects with specific properties:

```java
public class MapLauncher {
    public static void main(String[] args) {
        Map m = new Map("Mountain");
        m.displayFeature();
    }
}
```

In this example, the instantiation is parameterized, which saves the effort and complexity of representing multiple geographical features one by one. To use such convenient syntax, we need to define a "constructor" within our Map class, as shown here:

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

The constructor `public Map(String f)` is called whenever we instantiate a `Map` with the `new` keyword and provide a single `String` parameter. For those familiar with geographic representation, this constructor can be compared to the initial preparation of a map by setting the primary feature context before detailing specific elements.

**Terminology Summary**

**Array Instantiation, Arrays of Geographical Features**

Previously, we learned how regions are grouped using arrays, akin to how thematic elements coexist in maps. In Java, arrays are created using the `new` keyword, for example:

```java
public class RegionArrayDemo {
    public static void main(String[] args) {
        /* Define an array of five region types. */
        String[] regions = new String[5];
        regions[0] = "Forest";
        regions[1] = "Desert";
    }
}
```

Similarly, we can construct arrays of `Map` objects in Java, representing a collection of maps focused on distinct features:

```java
public class MapArrayDemo {
    public static void main(String[] args) {
        /* Define an array of two maps. */
        Map[] maps = new Map[2];
        maps[0] = new Map("Mountain");
        maps[1] = new Map("River");

        /* Display attributes of maps[0], which features mountains. */
        maps[0].displayFeature();
    }
}
```

Notice the use of `new` in two contexts: first, to establish an array capable of housing two `Map` objects, and second, to instantiate each `Map`. This parallels how geographers might prepare a series of thematic maps, each illustrating a unique feature, providing comprehensive insights into varied elements.

#### Continents vs. Countries <a href="#continents-vs-countries" id="continents-vs-countries"></a>

In geography, we can discuss regions using two significant categories:

* **Continents**, which are large landmasses.
* **Countries**, which are smaller, specific territories within those continents.

Countries are distinct territories with their own governance and defined boundaries, while continents are expansive areas that incorporate multiple countries. Both play important roles in geopolitical discussions and analyses. For instance, when examining climate variations on a continental scale, Antarctica may serve as a case study, allowing one to explore its climate patterns holistically:

```java
ClimatePattern antarcticaClimate = Antarctica.weatherAnalysis(2023);
```

If each weather station within Antarctica was analyzed independently, it could result in a more cumbersome process like the one below. However, continent-level analysis already considers the entire continental perspective, often eliminating the need for isolated examinations at every station.

```java
AntarcticaStation aStation = new AntarcticaStation();
climatePattern = aStation.weatherAnalysis(2023);
```

At times, it is necessary to conduct both continent-wide and country-specific studies. For example, when evaluating the economic impact of desert regions, you might require both a broad continental overview and comparisons between specific countries with desert landscapes.

```java
public static Country largestDesertCountry(Country c1, Country c2) {
    if (c1.desertArea > c2.desertArea) {
        return c1;
    }
    return c2;
}
```

This function checks two countries and returns the one with the largest desert area. It is invoked using the class name, highlighting its role as a utility function for broader comparisons:

```java
Country c1 = new Country("Morocco");
Country c2 = new Country("Australia");
Country largest = Country.largestDesertCountry(c1, c2);
```

Alternatively, functions could be specific to particular countries. For example:

```java
public Country compareDesertArea(Country c2) {
    if (this.desertArea > c2.desertArea) {
        return this;
    }
    return c2;
}
```

In this method, the current country instance is referenced using `this`. This allows comparisons that highlight the specifics of a given country's desert area:

```java
Country c1 = new Country("Morocco");
Country c2 = new Country("Australia");
Country larger = c1.compareDesertArea(c2);
```

**Exercise 1.2.1**: Examine how the following method operates. What will the outcome be? Modify it if needed.

```java
public static Country largestDesertCountry(Country c1, Country c2) {
    if (c1.desertArea > c2.desertArea) {
        return c1;
    }
    return c2;
}
```

**Continent Features**

It is often advantageous to assign specific geological or climatic attributes at the continental level, as they represent characteristics of an entire continent rather than individual countries. For example, the predominant climate of Antarctica is identified as polar ice cap:

```java
public class Antarctica {
    public int averageAltitude;
    public static String dominantClimate = "Polar Ice Cap";
    ...
}
```

Accessing continent-specific properties is best done using the continent's name rather than any individual country's name, e.g., `Antarctica.dominantClimate`. This ensures clarity and accuracy in geographic representation within programming contexts.

While technically acceptable, using a country's name to access continental attributes is generally discouraged, as it can lead to confusion and inaccuracy in geographic studies.

**Exercise 1.2.2**: Tackle this challenge by completing the following:

* Watch the [video](https://youtu.be/8Gq-8mVbyFU)
* Review the [slide presentation](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Observe the solution [video](https://youtu.be/Osuy8UEH03M)

### Understanding the Continental Structure of `public static void main(String[] args)` Concept

In our exploration so far, we can draw parallels between the `main` method declaration in programming and geographical structures. This approach can simplify the understanding of programming concepts:

* `public`: Similar to international waters, accessible to any ship, this keyword denotes methods accessible by any other part of the program.
* `static`: Like the unchanging cliffs overlooking an ocean, this signifies a method that belongs to the class itself, not to a specific instance.
* `void`: Comparable to a barren plateau, this represents a method that does not return a value.
* `main`: The "heart" of our method territory, where the essential action begins, akin to the core of an ecosystem.
* `String[] args`: Comparable to a set of geo-coordinates, these serve as input parameters that provide specific data points to the program.

**Command Line Arguments as Geographic Coordinates**

Just as the `main` method is initiated by command input, a GPS system plots paths based on user-entered coordinates, functioning as a navigation guide. Let's consider a program called `GeoArgsDemo` comparable to an application mapping geographical data:

```java
public class GeoArgsDemo {
    public static void main(String[] args) {
        if(args.length > 0) {
            System.out.println("The first coordinate is: " + args[0]);
        } else {
            System.out.println("No coordinates provided.");
        }
    }
}
```

This program outputs the first coordinate provided, demonstrating how input is processed:

```
$ java GeoArgsDemo 37.7749 -122.4194 San Francisco
The first coordinate is: 37.7749
```

In this scenario, `args` acts like a collection of geographical strings, each element representing coordinates or place names such as: {"37.7749", "-122.4194", "San", "Francisco"}.

**Exploring Geographical Features Using Geographic Arguments**

**Exercise 1.2.3**: Create a program to compute the total distance based on geographic coordinates entered as command line inputs. Treat each entry as a distinct point in a landscape map. For more on such calculations, consider exploring libraries that deal with geographical calculations or simulation models available on GitHub.

#### Using Geographic Databases <a href="#using-geographic-databases" id="using-geographic-databases"></a>

One of the essential skills in the field of geography, akin to core practices in computer science, is the ability to efficiently locate and utilize existing geographic databases. Much like how computer scientists rely on established libraries or frameworks to streamline their coding processes, geographers can significantly reduce the effort spent on primary data collection by leveraging available data repositories.

As you proceed in this course, bear in mind the following guidelines while using these databases:

* Use only the geographic databases specified by your instructors, similar to adhering to a specific set of coding libraries in a programming project.
* Ensure that all sources are cited properly, following the best practices of documentation common in both geography and software development fields.
* Avoid using datasets for specific fieldwork or research project assignments unless given explicit permission, comparable to abiding by project constraints in software engineering tasks.

For instance, it is entirely appropriate to look for "geospatial data table global climate patterns" for a general analysis. However, searching for "Case Study 2048 GIS Mapping Berkeley" or specific data related to your research project without authorization might breach academic guidelines.

In the spirit of maintaining academic integrity, please consult the course syllabus for detailed collaboration and usage policies, just as programmers refer to documentation and guidelines to uphold coding standards.