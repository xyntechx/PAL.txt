# Introduction to Java Classes and Methods

This chapter introduces fundamental concepts related to Java programming, employing an analogy to the universe to clarify the intricacies of object-oriented programming. Key terminologies are explored starting with **classes**, which are likened to blueprints that dictate the behavior of *objects* - the tangible manifestations of these blueprints. The discussion progresses to **static** and **instance methods**: static methods relate to a class as a whole, whereas instance methods operate on specific instances, similar to how gravitational forces act differently depending on the celestial bodies involved. Insights into **instance variables** and **constructors** help elucidate how objects attain unique properties and initialization rites, akin to cosmic formations.

The chapter further explains the instantiation of arrays in Java, specifically arrays of objects, using real-world astrophysical examples. By leveraging code snippets, readers gain familiarity with creating and manipulating arrays intended to simulate celestial systems. The section on **static and instance methods** emphasizes their respective roles and practical use-cases within astronomical calculations. Finally, the chapter explores **static variables** and the `main` method's importance, touching upon command line arguments and the effective use of external libraries within Java programming. This cosmic journey through Java's object-oriented architecture equips readers with foundational skills for understanding and implementing complex simulations.

All of our major terminologies of this section are collected here:

1. **Class**: To continue with our universe analogy, a class in Java can be thought of as a cosmic blueprint. Just as the laws of physics govern the behavior of celestial bodies, Java's class definitions dictate the behavior of objects.

2. **Static Method**: A phenomenon inherent to stellar constellations that does not change or vary across different instances, like a star that maintains a constant luminosity regardless of its surrounding celestial sphere. Static methods belong to a class rather than to individual objects.

3. **Instance Variable**: Much like the unique properties of individual stars, such as brightness or spectral class, instance variables are unique properties that belong to each object. These could be the mass, radius, or metallicity in the realm of stars, analogous to weight in our `Dog` class.

4. **Instance Method**: Comparable to gravitational influences unique to each celestial body. These methods perform actions dependent on the instance they're associated with, like how a star's gravitational pull affects its nearby planets individually.

5. **Constructor**: This is akin to the formation of a new star in a nebula, where initial conditions dictate its trajectory and evolution. A constructor initializes an object's properties at the cosmic moment of its creation.

6. **Object**: An instance of a class represents a tangible manifestation of matter within the cosmic system you create in your program. In our universe metaphor, objects are analogous to individual celestial bodies, like stars or planets, birthed from their defining classes.

7. **Client Class**: Just as a planetary system relies on a star’s energy, a client class relies on another class. It uses the functionality and behaviors defined by another class to serve its own purpose or drive its methods, much like how life thrives under the energizing rays of a star system.

By channeling our understanding of universe phenomena into Java constructs, we foster a greater appreciation of both fields and enrich our tapestry of knowledge across the sciences. As we advance, the vast methods and instances of our programming cosmos will become as wondrous and expansive as the stars that blanket our night sky.

**Array Instantiation, Arrays of Objects in Astrophysics**

As we saw in HW0, arrays are also instantiated in Java using the new keyword. Consider a scenario where we want to model a set of celestial objects in a simulation:

```java
public class ArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five celestial body masses, in kilograms. */
        double[] celestialMassesArray = new double[5];
        celestialMassesArray[0] = 5.972e24; // Mass of Earth
        celestialMassesArray[1] = 1.989e30; // Mass of Sun
    }
}
```

Similarly, we can create arrays of instantiated astronomical objects in Java, for instance:

```java
public class StarArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two stars. */
        Star[] stars = new Star[2];
        stars[0] = new Star("Sun", 1.989e30);
        stars[1] = new Star("Sirius", 3.978e30);

        /* Calling lightEmission will show the energy output of stars[0]. */
        stars[0].lightEmission();
    }
}
```

Observe that `new` is used in two different ways: Once to create an array that can hold two `Star` objects, and twice to create each actual `Star`.

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

In the context of astrophysics simulation software, Java allows us to define two types of methods:

* Class methods, a.k.a. static methods.
* Instance methods, a.k.a. non-static methods.

Instance methods perform actions on specific instances of an astronomical object class, while static methods perform actions at the class level, disregarding specific instances. Both are useful in different astronomical calculations. As an example of a static method, consider a `Constants` class which might offer a method to retrieve the gravitational constant. Because it is static, it can be called as follows:

```java
G = Constants.gravitationalConstant();
```

If `gravitationalConstant` had been an instance method, the syntax would be more cumbersome, for instance:

```java
Constants c = new Constants();
G = c.gravitationalConstant();
```

Sometimes, it makes sense to have a class with both instance and static methods. For example, suppose you want the capability to compare the luminosity of two stars. One way to implement this is through a static method for comparing stars.

```java
public static Star maxLuminosityStar(Star s1, Star s2) {
    if (s1.luminosity > s2.luminosity) {
        return s1;
    }
    return s2;
}
```

This method could be invoked as follows:

```java
Star s1 = new Star("Sun", 1.989e30);
Star s2 = new Star("Betelgeuse", 5.972e35);
Star.maxLuminosityStar(s1, s2);
```

Observe that we've called it using the class name, since it's a static method.

We could also implement `maxLuminosityStar` as a non-static method, such as:

```java
public Star maxLuminosityStar(Star s2) {
    if (this.luminosity > s2.luminosity) {
        return this;
    }
    return s2;
}
```

Here, we use the keyword `this` to refer to the current object. This method could be invoked, for example, with:

```java
Star s1 = new Star("Sun", 1.989e30);
Star s2 = new Star("Betelgeuse", 5.972e35);
s1.maxLuminosityStar(s2);
```

Here, we invoke the method using a specific instance variable.

**Exercise 1.2.1**: What would the following method do? If you're not sure, try it out.

```java
public static Star maxLuminosityStar(Star s1, Star s2) {
    if (luminosity > s2.luminosity) {
        return this;
    }
    return s2;
}
```


**Static Variables**

It is occasionally useful for classes to have static variables. These are properties inherent to the class itself, not an instance. For example, we might record that the default star classification system is "Morgan-Keenan" with the classification enum or variable.

```java
public class Star {
    public double luminosity;
    public static String classificationSystem = "Morgan-Keenan";
    ...
}
```

Static variables should be accessed using the class name rather than a specific instance, e.g., you should use `Star.classificationSystem`, not `s.classificationSystem`.

While Java technically allows you to access a static variable using an instance name, it is bad style, confusing, and in my opinion, an oversight by the Java designers.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe\_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String\[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

With what we've learned so far, it's time to demystify the declaration we've been using for the main method. Breaking it into pieces, we have:

* `public`: So far, all of our methods start with this keyword.
* `static`: It is a static method, not associated with any particular cosmic body.
* `void`: It outputs no material results, just like a black hole consuming information.
* `main`: This is the name of the focal point of the program.
* `String[] args`: This is a constellation of parameters, passed into the main method, representing external influences.

**Command Line Arguments**

Since main is initiated by the Java interpreter, akin to the cosmic event causing a supernova, rather than another Java class, it is the interpreter's job to supply these inputs. They refer typically to the command line influences, analogous to external forces acting on a star. For example, consider the program `ArgsDemo` below:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);  // Output the first element, much like observing the first star of a constellation.
    }
}
```

This program reveals the 0th cosmic argument, e.g.

```
$ java ArgsDemo universe expanding rapidly
universe
```

In the example above, `args` will be an array of Strings, where the entries are analogous to planets orbiting a central star: {"universe", "expanding", "rapidly"}.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Attempt to write a program that sums up the command line arguments, assuming they are numerical as if calculating the combined mass of celestial bodies. For an astronomical solution, refer to the webcast or the code available on GitHub.

#### Using Libraries <a href="#using-libraries" id="using-libraries"></a>

One of the primary skills for a computational astronomer is knowing how to locate and utilize existing libraries. In the vast universe of modern programming, it is often worthwhile to save yourself from computational black holes and debugging supernovae by reaching out to the web for assistance.

In this course, you're welcome to do this, with the following observatory guidelines:

* Do not use libraries that we do not provide—stay within our galaxy of allowed tools.
* Cite your interstellar sources.
* Do not search for specific solutions to constellation homework or project challenges.

For example, it's fine to search for "convert String integer Java"—a task as routine as measuring a star's luminosity. However, it is not OK to search for "Project 2048 Berkeley" as if uncovering the secrets of the universe.

For more information on collaboration and academic honesty policies across our scientific domains, see the course syllabus.