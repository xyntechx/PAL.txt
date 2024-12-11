# Defining and Using Classes

This chapter delves into Java's object-oriented programming features, particularly focusing on defining and using classes. It begins with an exploration of static versus non-static methods, illustrating through examples how methods can be part of the class itself or act upon an instance of the class. For instance, the `Star` class can have static methods like `emitLight()`, which is called using the class name, and non-static methods like `shine()` that require an object instance. The concept of instance variables is introduced, demonstrating how they provide the unique properties of each object instance. The chapter also discusses the importance of constructors in object instantiation, allowing developers to initialize objects with specific attributes.

Further, it covers arrays of objects and how they can be instantiated using Java's `new` keyword, providing examples of how multiple objects are managed. Class methods and static methods are distinguished by their application: class methods operate at the class level, while instance methods work on specific object instances. The chapter also introduces static variables and highlights their universal applicability and access through class names rather than object instances. The main method (`public static void main(String[] args)`) is explained as the entry point for executing Java programs, including how to handle command-line arguments. Finally, the chapter advises leveraging existing libraries and tools, underscoring the importance of peer-reviewed and credible sources to avoid errors in programming practices.

2. Defining and Using Classes

If you do not have prior Java experience, we recommend that you work through the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before reading this chapter. It will cover various syntax issues that we will not discuss in the book.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

All code in Java must be part of a class (or something similar to a class, which we'll learn about later). Most code is written inside of methods. Let's consider an example utilizing astrophysical concepts:

```java
public class Star {
    public static void emitLight() {
        System.out.println("Glimmer!");
    }
}
```

If we try running the `Star` class, we'll simply get an error message:

```
$ java Star
Error: Main method not found in class Star, please define the main method as:
       public static void main(String[] args)
```

The `Star` class we've defined doesn't do anything. We've simply defined something that `Star` **can** do, namely emit light. To actually run the class, we'd either need to add a main method to the `Star` class, as we saw in chapter 1.1. Or we could create a separate [`GalaxyLauncher`](https://www.youtube.com/watch?v=Q-LE-jJQLTM) class that runs methods from the `Star` class. For example, consider the program below:

```java
public class GalaxyLauncher {
    public static void main(String[] args) {
        Star.emitLight();
    }
}
```

```
$ java GalaxyLauncher
Glimmer!
```

A class that uses another class is sometimes called a "client" of that class, i.e. `GalaxyLauncher` is a client of `Star`. Neither of the two techniques is better: Adding a main method to `Star` may be better in some situations, and creating a client class like `GalaxyLauncher` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout the course. 


**Instance Variables and Celestial Object Instantiation**

Not all stars are alike. Some stars emit gentle twinkles, while others unleash powerful supernovae, captivating the cosmos with their spectacular displays. Often, we create simulations to imitate aspects of the universe, and Java's syntax allows us to effortlessly achieve such cosmic mimicry.

One strategy to represent the diversity of celestial bodies would be to create individual classes for each type of star.

```java
public class RedDwarf {
    public static void shine() {
        System.out.println("twinkle twinkle twinkle");
    }
}

public class Supernova {
    public static void shine() {
        System.out.println("BOOM!");
    }
}
```

As you should have seen in the past, classes can be instantiated, and instances can hold data. This leads to a more natural approach, where we create instances of the `Star` class and make the behavior of the `Star` methods contingent upon the properties of the specific `Star`. To make this more concrete, consider the class below:

```java
public class Star {
    public double massInSolarMasses;

    public void shine() {
        if (massInSolarMasses < 0.5) {
            System.out.println("twinkle twinkle twinkle");
        } else if (massInSolarMasses < 10) {
            System.out.println("shine steady.");
        } else {
            System.out.println("BOOM!");
        }
    }    
}
```

As an example of using such a Star, consider:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star s;
        s = new Star();
        s.massInSolarMasses = 8.5;
        s.shine();
    }
}
```

When run, this program will create a `Star` with mass 8.5 solar masses, and that `Star` will soon emit a steady shine.

Some key observations and terminology:

* An `Object` in Java is an instance of any class.
* The `Star` class has its own variables, also known as _instance variables_ or _non-static variables_. These must be declared inside the class, unlike languages like Python or Matlab, where new variables can be added at runtime.
* The method that we created in the `Star` class did not have the `static` keyword. We call such methods _instance methods_ or _non-static methods_.
* To call the `shine` method, we had to first _instantiate_ a `Star` using the `new` keyword, and then make a specific `Star` emit light. In other words, we called `s.shine()` instead of `Star.shine()`.
* Once an object has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `s = new Star();`
* Variables and methods of a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_.


**Constructors in Java: Astrophysics Analogy**

As you've hopefully seen before, we usually construct objects in object-oriented languages using a _constructor_. Let's illustrate this with an example that considers an analogy in astrophysics:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star s = new Star(5.0);
        s.emitLight();
    }
}
```

In this analogy, the instantiation is parameterized, saving us the complexity of manually characterizing potentially many properties of celestial bodies. To enable such a syntax, we only need to add a "constructor" to our `Star` class, as demonstrated below:

```java
public class Star {
    public double massInSolarMasses;

    public Star(double m) {
        massInSolarMasses = m;
    }

    public void emitLight() {
        if (massInSolarMasses < 0.5) {
            System.out.println("faint glow");
        } else if (massInSolarMasses < 3.0) {
            System.out.println("bright shine");
        } else {
            System.out.println("blazing blaze");
        }    
    }
}
```

The constructor with the signature `public Star(double m)` will be activated each time we try to create a `Star` object using the `new` keyword along with a single real number parameter. If you're transitioning from Python, the constructor is quite similar to the `__init__` method in that language.

**Terminology Summary**

**Array Instantiation, Arrays of Objects**

As we observed in HW0, arrays are instantiated in Java using the new keyword. For instance:

```java
public class ArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five solar systems. */
        double[] solarSystemMasses = new double[5];
        solarSystemMasses[0] = 1.0;
        solarSystemMasses[1] = 1.5;
    }
}
```

Similarly, we can create arrays of instantiated objects in Java, for example:

```java
public class StarArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two stars. */
        Star[] stars = new Star[2];
        stars[0] = new Star(0.3);
        stars[1] = new Star(5.0);

        /* A faint glow will result, since stars[0] has mass 0.3 solar masses. */
        stars[0].emitLight();
    }
}
```

Observe that `new` is used in two different ways: Once to create an array capable of holding two `Star` objects, and twice to create each actual `Star`. This parallels the cosmic assembly of diverse celestial entities within the universe.

#### Class Methods vs. Instance Methods in Astrophysics <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java allows us to define two types of methods:

* Class methods, a.k.a. static methods.
* Instance methods, a.k.a. non-static methods.

Instance methods are actions that can be taken only by a specific instance of a class, akin to how individual stars have unique formation and lifecycle processes within the galaxy. Static methods are actions that are taken by the class itself, much like universal laws of physics that apply generally to celestial phenomena. Both are useful in different circumstances. As an example of a static method, consider a `Galaxy` class providing a `calculateEscapeVelocity` method. Because it is static, we can call it as follows:

```java
v = Galaxy.calculateEscapeVelocity(300000); // speed in meters per second
```

If `calculateEscapeVelocity` had been an instance method, we would have instead the awkward syntax below. Luckily `calculateEscapeVelocity` is a static method so we don't have to do this in real programs.

```java
Galaxy g = new Galaxy();
v = g.calculateEscapeVelocity(300000);
```

Sometimes, it makes sense to have a class with both instance and static methods. For example, suppose we want the ability to compare two astronomical bodies' brightness. One way to do this is to add a static method for comparing Stars.

```java
public static Star brighterStar(Star s1, Star s2) {
    if (s1.luminosity > s2.luminosity) {
        return s1;
    }
    return s2;
}
```

This method could be invoked by, for example:

```java
Star s1 = new Star(1.0); // normalized luminosity, for example
Star s2 = new Star(10.0);
Star.brighterStar(s1, s2);
```

Observe that we've invoked using the class name, since this method is a static method.

We could also have implemented `brighterStar` as a non-static method, e.g.

```java
public Star brighterStar(Star s2) {
    if (this.luminosity > s2.luminosity) {
        return this;
    }
    return s2;
}
```

Above, we use the keyword `this` to refer to the current star object. This method could be invoked, for example, with:

```java
Star s1 = new Star(1.0);
Star s2 = new Star(10.0);
s1.brighterStar(s2);
```

Here, we invoke the method using a specific instance variable, just like individual stars comparing their brightness against each other.

**Exercise 1.2.1**: What would the following method do? If you're not sure, try it out.

```java
public static Star brighterStar(Star s1, Star s2) {
    if (luminosity > s2.luminosity) {
        return this;
    }
    return s2;
}
```

**Static Variables in Astrophysics**

It is occasionally useful for classes to have static variables. These are properties inherent to the class itself, rather than an instance, similar to Newton's gravitational constant which applies universally. For example, we might record that the speed of light constant in the `PhysicsConstants` class:

```java
public class PhysicsConstants {
    public static final double speedOfLight = 299792458; // meters per second
    ...
}
```

Static variables should be accessed using the name of the class rather than a specific instance, e.g., you should use `PhysicsConstants.speedOfLight`, not `c.speedOfLight`.

While Java technically allows you to access a static variable using an instance name, it is bad style, confusing, and in my opinion an error by the Java designers.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe\_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String\[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

Incorporating concepts from astrophysics, let's explore the main method declaration that can be likened to coordinating a celestial event, such as a solar eclipse. Here's the breakdown:

* `public`: This is akin to a universal phenomenon, observed by all in the cosmos to maximize visibility.
* `static`: Like the fundamental constants of the universe, it remains unchanged across all instances.
* `void`: Similar to vacuum energy, which leaves no tangible residue.
* `main`: This serves as the central focal point, much like the sun in a solar system.
* `String[] args`: Analogous to cosmic rays, these parameters enter from separate regions of the universe.

**Command Line Arguments**

When a main method is invoked by the cosmic equivalent of a Java interpreter—imagine it as gravity acting to organize orbital patterns—it's tasked with acquiring these parameters akin to gathering cosmic data. These are often sourced from command line inputs to the Java program. Consider examining the cosmic analog for `ArgsDemo`, which is illustrated below:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

In this instance, the program simply echoes the 0th cosmic "ray" or argument entering its event horizon, such as:

```
$ java ArgsDemo quasar astronomy blackhole warp
quasar
```

In this scenario, `args` is an array of cosmic strings, where cosmic threads are {"quasar", "astronomy", "blackhole", "warp"}.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Imagine creating a program that calculates the sum of these command line arguments, hypothesizing they represent astronomical distances or values significant in astrophysical calculations. Refer to astrophysical simulation software or consult the repository on GitHub for solutions.

#### Utilizing Cosmic Tools <a href="#using-libraries" id="using-libraries"></a>

One of the most crucial skills as an astrophysicist is knowing how to locate and utilize existing cosmic tools or models. In the expansive universe of astrophysics, it is often possible to save yourself years of observations and analysis by consulting astronomical databases and simulation tools available online.

In this field, you're encouraged to do this, with the following caveats:

* Do not use astronomical models that are not peer-reviewed or verified by the scientific community.
* Cite your cosmic data sources and models utilized.
* Do not seek exact astronomical data or simulations for specific research experiments or hypotheses without due diligence.

For example, it's fine to search for "redshift calculation methods". However, it is not permissible to search for "Black Hole Project Milky Way parameters".

For more on collaboration and academic honesty policy, refer to the astrophysical research conduct guidelines.