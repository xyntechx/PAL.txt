# Introduction to Java Classes and Methods

This chapter introduces fundamental concepts related to Java programming, employing an analogy to the universe to clarify the intricacies of object-oriented programming. Key terminologies are explored starting with **classes**, which are likened to blueprints that dictate the behavior of *objects* - the tangible manifestations of these blueprints. The discussion progresses to **static** and **instance methods**: static methods relate to a class as a whole, whereas instance methods operate on specific instances, similar to how gravitational forces act differently depending on the celestial bodies involved. Insights into **instance variables** and **constructors** help elucidate how objects attain unique properties and initialization rites, akin to cosmic formations.

The chapter further explains the instantiation of arrays in Java, specifically arrays of objects, using real-world astrophysical examples. By leveraging code snippets, readers gain familiarity with creating and manipulating arrays intended to simulate celestial systems. The section on **static and instance methods** emphasizes their respective roles and practical use-cases within astronomical calculations. Finally, the chapter explores **static variables** and the `main` method's importance, touching upon command line arguments and the effective use of external libraries within Java programming. This cosmic journey through Java's object-oriented architecture equips readers with foundational skills for understanding and implementing complex simulations.

All of our major terminologies of this section are collected here:

1. **Class**: In a universe governed by the fundamental laws of physics, a class in Java acts similarly as a cosmic blueprint, determining the properties and behaviors of the objects it manifests. Much like the laws dictating celestial mechanics apply uniformly across different systems, the class definitions in Java uniformly shape all instances derived from them.

2. **Static Method**: Imagine a celestial constant, akin to the universal speed of light, consistent across all frames of reference. Static methods are bound to the class itself rather than any single instance, providing uniform behavior akin to an immutable cosmic property.

3. **Instance Variable**: These are analogous to the unique characteristics of each star, such as its luminosity or elemental composition. Instance variables assign specific attributes to individual objects, much like how the characteristics of a star define its individual place in the universe.

4. **Instance Method**: Consider the unique gravitational forces exerted by different celestial bodies, influencing their own systems uniquely. Instance methods operate on an object’s behalf, performing functions relevant to its specific state, akin to how gravitational influences are tailored to the celestial body's own mass and radius.

5. **Constructor**: Analogous to the moments when a star ignites within a nebula, setting its future path and characteristics, a constructor formalizes the initiation of an object's state. It defines the initial conditions crucial to the object's lifecycle, much like the star's formation dictates its stellar journey.

6. **Object**: Within the cosmic expanse of a Java program, objects emerge as tangible entities crafted from their classes. These are the stars and planets born from their cosmic blueprints, embodying the specific attributes and capabilities designated by their defining classes.

7. **Client Class**: Within the interconnected web of a planetary system, planets rely on the star at the center to sustain life and motion. Similarly, a client class depends on the services and behaviors of another class, leveraging these to fulfill its own objectives, akin to a planet's dependency on solar energy.

By aligning Java constructs with universal phenomena, we gain a deeper appreciation for both fields, enriched by the synergy between programming and astrophysics. As we delve further, the diverse structures of our programming universe will reveal themselves to be as infinite and dynamic as the cosmos itself.

**Array Instantiation, Arrays of Objects in Astrophysics**

As we saw in HW0, arrays in Java are instantiated using the `new` keyword. Let's consider modeling a collection of celestial objects for a simulation:

```java
public class ArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five celestial body masses in kilograms. */
        double[] celestialMassesArray = new double[5];
        celestialMassesArray[0] = 5.972e24; // Mass of Earth
        celestialMassesArray[1] = 1.989e30; // Mass of Sun
        // You could add more celestial objects here
    }
}
```

Similarly, we can create arrays of instantiated astronomical objects in Java. These allow us to work with objects representing stars, planets, or even galaxies:

```java
public class StarArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two stars with properties. */
        Star[] stars = new Star[2];
        stars[0] = new Star("Sun", 1.989e30);
        stars[1] = new Star("Sirius", 3.978e30);

        /* Calling lightEmission will show the energy output of stars[0]. */
        stars[0].lightEmission();
    }
}
```

Note the dual use of `new`: once to create the array to hold `Star` objects, and again for each `Star` object itself.

### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

In astrophysics simulation software, Java allows for two types of methods:

* **Class methods**, a.k.a. static methods
* **Instance methods**, a.k.a. non-static methods

Instance methods act on specific instances of an astronomical object, while static methods function at the class level, independent of instances. This distinction is valuable for astronomical computations where some calculations need not depend on object state. For instance, a `Constants` class could hold a static method for retrieving the gravitational constant:

```java
G = Constants.gravitationalConstant();
```

Had `gravitationalConstant` been an instance method, it would require an instantiation first:

```java
Constants c = new Constants();
G = c.gravitationalConstant();
```

Classes can contain both instance and static methods, such as to compare the luminosity of stars through a static method:

```java
public static Star maxLuminosityStar(Star s1, Star s2) {
    return s1.luminosity > s2.luminosity ? s1 : s2;
}
```

Invoke it as:

```java
Star s1 = new Star("Sun", 1.989e30);
Star s2 = new Star("Betelgeuse", 5.972e35);
Star.maxLuminosityStar(s1, s2);
```

This uses the class name due to its static nature.

If implemented as a non-static method:

```java
public Star maxLuminosityStar(Star s2) {
    return this.luminosity > s2.luminosity ? this : s2;
}
```

Invoke it using an instance:

```java
Star s1 = new Star("Sun", 1.989e30);
Star s2 = new Star("Betelgeuse", 5.972e35);
s1.maxLuminosityStar(s2);
```

Here, `this` refers to the current object.

**Exercise 1.2.1**: Evaluate the following method. What errors do you notice? Attempt to implement and test your findings.

```java
public static Star maxLuminosityStar(Star s1, Star s2) {
    if (luminosity > s2.luminosity) {
        return this; // Causes error as 'this' cannot be used in a static context
    }
    return s2;
}
```

### Static Variables

Classes can employ static variables, representing class-wide properties, not instance-specific ones. For example, a star's classification system:

```java
public class Star {
    public double luminosity;
    public static String classificationSystem = "Morgan-Keenan";
    ...
}
```

Access them using the class name: `Star.classificationSystem` instead of through any instance (`s.classificationSystem`), as the latter is considered poor practice.

**Exercise 1.2.2**: Complete and reflect on this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String[] args)

In this section, let's delve deeper into understanding the declaration we use for the main method in Java. The key components are as follows:

* `public`: This keyword signifies that the method is accessible to any part of the program, much like the Sun's influence reaches across the entire solar system.
* `static`: Indicates a static method, meaning it's not tied to any particular instance, akin to the universal laws of physics that apply everywhere in the universe.
* `void`: This method returns no value, similar to how a black hole absorbs all light and matter without giving anything back.
* `main`: The name of this method, representing the core of the program's execution—its gravitational center.
* `String[] args`: This array contains the command line arguments provided to the program, akin to receiving cosmic signals or data from space probes.

**Command Line Arguments**

When the main method is invoked by the Java interpreter, a process comparable to the ignition of a star, it receives input in the form of command line arguments. These inputs influence the program's behavior, much like gravitational forces affecting celestial bodies. Consider the following example program `ArgsDemo`:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);  // Print the first element, similar to capturing the first light from a distant star.
    }
}
```

Running this program with the command `java ArgsDemo galaxy expanding fast` will output:

```
galaxy
```

Here, `args` is an array of Strings, with each element comparable to different astronomical objects in a vast constellation: {"galaxy", "expanding", "fast"}.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Create a program that sums numerical command line arguments, as if calculating the combined mass of a cluster of stars. For a hint, check out the resources available through our online portal or visit the code repository on GitHub.

#### Using Libraries

An essential skill for a computational astronomer—or any programmer—is the ability to find and utilize existing libraries. In the boundless universe of software development, you can save yourself from being pulled into a vortex of endless debugging by seeking out reliable libraries.

In the scope of this course, adhere to the following guidelines:

* Only use libraries that we authorize, staying within the "observable universe" of our course material.
* Always credit your informational sources, resembling how astronomers cite celestial discoveries.
* Shun attempts to search directly for solutions to specific assignments—like peering into forbidden zones of the academic cosmos.

For instance, searching for "Java convert String to integer" is allowed, akin to basic astrometric calculations. However, searching "Project 2048 solution" parallels trying to unveil the Milky Way’s mysteries without proper authorization.

For further details on collaboration and academic integrity across all our scientific and computational domains, please refer to the course syllabus. This ensures we maintain a harmonious balance between our pursuit of knowledge and ethical conduct.