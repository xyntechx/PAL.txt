# Static vs. Non-Static Methods

In this chapter, we explore the fundamental distinction between static and non-static methods in Java programming, emphasizing their role and implementation. Static methods, marked by the `static` keyword, are associated directly with the class they belong to, meaning they can be invoked using the class name without needing an object instance. This is illustrated through examples, including the `emitLight` method in the `Star` class and the usage of utility methods like `Math.sqrt`. On the other hand, non-static methods, or instance methods, are tied to specific instances of a class, thus requiring object instantiation to be called. The chapter delves into these concepts, demonstrating how instance variables can alter the behavior of an instance method, as seen in variations of the `Star` class where the `emitLight` method's output depends on the mass assigned to a particular instance.

The chapter further expands on constructors and how they facilitate object initialization, saving time and improving clarity by allowing parameters to govern instance variable assignment at the object's creation. Additionally, it introduces static and instance variables, explaining their access and usage within different methods types, emphasizing good coding practices. The text also covers the instantiation of arrays and their ability to contain objects, illustrating how to manage collections of class instances. Finally, the chapter touches upon the significance of the `main` method in Java as a static entry point, the utility of handling command-line arguments, and the importance of understanding and using existing libraries responsibly in programming. Together, these concepts form a solid foundation in understanding Java's object-oriented functionalities and preparing for more advanced topics.

Static vs. Non-Static Methods

**Static Methods**

All classes in Java serve as blueprints for objects. However, not all methods within a class are tied to individual objects. **Static methods** belong to the class itself, not to any particular object instantiated from the class. Let's explore this with a cosmic example:

```java
public class Star {
    public static void stellarAnnouncement() {
        System.out.println("Behold the universal heartbeat!");
    }
}
```

If we attempt to execute the `Star` class without a `main` method, an error will occur:

```
$ java Star
Error: Main method not found in class Star, please define the main method as:
       public static void main(String[] args)
```

Thus, the `Star` class merely outlines the potential for sound without initiating it. To experience the "universal heartbeat," we can instantiate a driver class:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star.stellarAnnouncement();
    }
}
```

```
$ java StarLauncher
Behold the universal heartbeat!
```

The `StarLauncher` acts as a client, invoking methods within the `Star` class. Each approach—embedding a `main` method within the `Star` class versus creating a separate driver class—has unique applications, which will become more evident with continued practice throughout this course.

**Instance Variables and Object Instantiation**

In our vast universe, no two stars are identical. Some stars emit gentle flickers, while others radiate formidable brilliance, embodying distinct characteristics like mass and temperature. In Java, these distinctions can be captured by creating a single `Star` class where each star—each instance—has unique properties.

```java
public class Star {
    public double mass;

    public void emitLight() {
        if (mass < 1.0) {
            System.out.println("twinkle, twinkle, little star.");
        } else if (mass < 10.0) {
            System.out.println("shine. shine.");
        } else {
            System.out.println("supernova in progress!");
        }
    }    
}
```

Here's how you might bring such a star to life:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star s = new Star();
        s.mass = 5.0;
        s.emitLight();
    }
}
```

Running this code creates a `Star` with a mass of 5.0, resulting in a "shine. shine." display due to its mass characteristics.

Key insights and terminology:

* An `Object` in Java is an instance of a class.
* Classes like `Star` have their own variables, termed _instance variables_ or _non-static variables_.
* The method within the `Star` that lacks the `static` keyword is known as an _instance method_ or _non-static method_.
* `s.emitLight()` implies `s` was instantiated—`new Star()`—to glow distinctively based on its assigned mass.
* Objects are linked to declared variables relating to their type, e.g., `s = new Star();`
* Items within a class—variables and methods—are referred to as _members_.
* Interaction with class members utilizes _dot notation_.

**Constructors in Java**

Typically, frameworks demonstrate object creation via constructors in object-oriented languages.

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star s = new Star(5.0);
        s.emitLight();
    }
}
```

This example shows a `Star` being created with a specific mass, thanks to a constructor in the `Star` class:

```java
public class Star {
    public double mass;

    public Star(double m) {
        mass = m;
    }

    public void emitLight() {
        if (mass < 1.0) {
            System.out.println("twinkle, twinkle, little star.");
        } else if (mass < 10.0) {
            System.out.println("shine. shine.");
        } else {
            System.out.println("supernova in progress!");
        }    
    }
}
```

Here, `public Star(double m)` acts akin to Python's `__init__` method, directing initializations during object creations with specific parameters.

### Array Instantiation, Arrays of Astrophysical Objects

Arrays in Java are created using the `new` keyword, which we explored in an earlier study. Below is an example:

```java
public class ArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five star magnitudes. */
        int[] starMagnitudes = new int[5];
        starMagnitudes[0] = 3;
        starMagnitudes[1] = 4;
    }
}
```

Similarly, Java allows us to create arrays of more complex objects, such as planets:

```java
public class PlanetArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two planets with respective masses. */
        Planet[] planets = new Planet[2];
        planets[0] = new Planet(8.0);
        planets[1] = new Planet(20.0);

        /* Simulate gravitational interaction from the first planet */
        planets[0].exertGravity();
    }
}
```

Note the usage of `new` to both instantiate the array and the individual `Planet` objects within it.

#### Class Methods vs. Instance Methods

Java supports two types of methods:

* **Class methods**: Also known as static methods, are invoked through the class itself.
* **Instance methods**: Are specific to an object instance of a class.

Instance methods operate on an instance of a class. Static methods, by contrast, are called on the class itself. Examine the `Math` class's static `sqrt` method:

```java
x = Math.sqrt(100);
```

If `sqrt` were an instance method, we'd have a less elegant syntax. Fortunately, as a static method, it simplifies usage.

```java
Math m = new Math();
x = m.sqrt(100);
```

Classes may contain both kinds of methods. Consider a static method for comparing two planets:

```java
public static Planet maxPlanet(Planet p1, Planet p2) {
    if (p1.mass > p2.mass) {
        return p1;
    }
    return p2;
}
```

This function could be executed as:

```java
Planet p1 = new Planet(15.0);
Planet p2 = new Planet(100.0);
Planet.maxPlanet(p1, p2);
```

The static method is accessed via the class name.

Alternatively, `maxPlanet` could be non-static:

```java
public Planet maxPlanet(Planet p2) {
    if (this.mass > p2.mass) {
        return this;
    }
    return p2;
}
```

When invoked, you use a specific instance:

```java
Planet p1 = new Planet(15.0);
Planet p2 = new Planet(100.0);
p1.maxPlanet(p2);
```

The method is called through an instance reference, using `this` to reference the caller object.

**Exercise 1.2.1**: What is wrong with the following static method implementation? Analyze and test it.

```java
public static Planet maxPlanet(Planet p1, Planet p2) {
    if (mass > p2.mass) {
        return this;
    }
    return p2;
}
```

**Static Variables**

Static variables are commonly used for values shared by all instances of a class. For example, consider a class attribute that categorizes planets:

```java
public class Planet {
    public double mass;
    public static String classification = "Celestial Bodies";
    ...
}
```

Access static variables via the class name for clarity, as in `Planet.classification`. Accessing via an instance like `p.classification` leads to less clear and properly discouraged code.

**Exercise 1.2.2**: Complete this task:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe\_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

## Main Sequence and Method Implementation

At this stage, we’ll delve into the structure of method declarations in Java, which play a vital role in cosmic simulations. Here's the breakdown of the components:

* `public`: Used for all our methods simulating cosmic phenomena, ensuring universal access.
* `static`: Represents the unchanging nature of a method, akin to a universal constant.
* `void`: Indicates the method returns no output, similar to energy dissipating into the cosmos without direct retrieval.
* `main`: Recognized as the core method, initiating our cosmic simulations.
* `String[] args`: An array representing the initial conditions for our simulated universe.

**Command Line Arguments in Astrophysical Context**

The `main` method, much like a telescope, begins with parameters provided by the universe framework, mirroring command line inputs used to set up astrophysical surveys. Observe the program `GalaxySimulator` below:

```java
public class GalaxySimulator {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

Executing this program simulates cosmic initialization with output based on these commands:

```
$ java GalaxySimulator MilkyWay Andromeda Triangulum
MilkyWay
```

Here, `args` becomes an array of Strings, like the array elements {"MilkyWay", "Andromeda", "Triangulum"}.

**Calculating Cosmic Time**

**Exercise 1.2.3**: Write a program that calculates time elapsed since the Big Bang using input eras measured in billions of years. For detailed methods, reference the cosmic lecture notes or algorithms preserved in our simulation archives.

#### Utilizing Cosmic Libraries <a href="#using-cosmic-libraries" id="using-cosmic-libraries"></a>

Mastering the use of pre-existing cosmic data libraries is crucial for computational astrophysics. Within the vast cosmos of data, your efficiency and insight improve by relying on verified theories and models.

We encourage exploration of libraries under the following guidelines:

* Use only the cosmic libraries provided.
* Cite and attribute astronomical inspirations.
* Avoid directly seeking ready-made solutions for specific research assignments or space missions.

Appropriate searches include "Java parsecs to light years conversion," whereas it’s inappropriate to search for "algorithm for detecting exoplanets in our survey project."

For information regarding collaborative efforts, universal ethics, and our academic standards, consult the university's interstellar guidebook.