# Defining and Using Classes

This chapter delves into Java's object-oriented programming features, particularly focusing on defining and using classes. It begins with an exploration of static versus non-static methods, illustrating through examples how methods can be part of the class itself or act upon an instance of the class. For instance, the `Star` class can have static methods like `emitLight()`, which is called using the class name, and non-static methods like `shine()` that require an object instance. The concept of instance variables is introduced, demonstrating how they provide the unique properties of each object instance. The chapter also discusses the importance of constructors in object instantiation, allowing developers to initialize objects with specific attributes.

Further, it covers arrays of objects and how they can be instantiated using Java's `new` keyword, providing examples of how multiple objects are managed. Class methods and static methods are distinguished by their application: class methods operate at the class level, while instance methods work on specific object instances. The chapter also introduces static variables and highlights their universal applicability and access through class names rather than object instances. The main method (`public static void main(String[] args)`) is explained as the entry point for executing Java programs, including how to handle command-line arguments. Finally, the chapter advises leveraging existing libraries and tools, underscoring the importance of peer-reviewed and credible sources to avoid errors in programming practices.

### Suggested Improvements:

Taking into account the feedback, especially the point that some astrophysical concepts used may not hold scientifically rigorous meanings, we'll refine the explanations and metaphors to better match astrophysical realities while maintaining clarity for CS learners.

### Revised Subsection:

2. Defining and Using Classes

If you do not have prior Java experience, we recommend that you work through the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before reading this chapter. It will cover various syntax issues that we will not discuss in the book.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

All code in Java must be part of a class (or something similar to a class, which we'll learn about later). Most code is written inside of methods. Let's consider an example utilizing a basic astrophysical concept: the emission of light by stars.

```java
public class Star {
    public static void emitLight() {
        System.out.println("The star is emitting light!");
    }
}
```

If we attempt to execute the `Star` class directly, we will receive an error message:

```
$ java Star
Error: Main method not found in class Star, please define the main method as:
       public static void main(String[] args)
```

The `Star` class we've created doesn't perform any operations by itself. We have only specified an action that a `Star` can perform, namely emitting light. To execute this action, we need to define a main method within the `Star` class or utilize a separate class to manage our execution, such as a `UniverseSimulator`. Here's how this could look:

```java
public class UniverseSimulator {
    public static void main(String[] args) {
        Star.emitLight();
    }
}
```

```
$ java UniverseSimulator
The star is emitting light!
```

A class that utilizes another class is often referred to as a "client" of that class, meaning that `UniverseSimulator` is a client of `Star`. Neither technique of adding a main method to `Star` or creating a separate client class is universally superior; each has its advantages. As you work through more examples in the course, you'll gain insights into the circumstances where each method is most beneficial.

**Instance Variables and Celestial Object Instantiation**

Just as the universe hosts a diverse array of stars, each with unique characteristics and behaviors, Java provides us with the tools to simulate these celestial wonders through object-oriented programming. In our cosmic simulation, we can model different types of stars using classes and instance variables.

One approach to representing the variety of stars would be to define separate classes for each type:

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

This technique works, but it can be inflexible. Instead, we can create a single `Star` class and utilize instance variables to define specific star properties. This approach allows us to instantiate unique stars with diverse behaviors:

```java
public class Star {
    private double massInSolarMasses;

    // Constructor to initialize star mass
    public Star(double mass) {
        this.setMass(mass);
    }

    // Setter method
    public void setMass(double mass) {
        this.massInSolarMasses = mass;
    }

    // Provides adaptable behavior
    public String getStarType() {
        if (massInSolarMasses < 0.5) {
            return "Red Dwarf";
        } else if (massInSolarMasses < 10) {
            return "Regular Star";
        } else {
            return "Supernova";
        }
    }

    public void shine() {
        switch (this.getStarType()) {
            case "Red Dwarf":
                System.out.println("twinkle twinkle twinkle");
                break;
            case "Regular Star":
                System.out.println("shine steady.");
                break;
            case "Supernova":
                System.out.println("BOOM!");
                break;
        }
    }
}
```

Now let's see this in action:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star s = new Star(8.5);
        System.out.println("The star type is: " + s.getStarType());
        s.shine();
    }
}
```

The `StarLauncher` program creates a `Star` with a mass of 8.5 solar masses. It classifies it as a "Regular Star," thus producing a steady shine upon execution.

Key observations and terminology:

* An **Object** in Java is an instance of any class, such as `Star`.
* The `Star` class utilizes **instance variables**, which are non-static and tied to specific objects, providing diverse behavior based on instance-specific data.
* The conversion of a star's mass into a type (e.g., Red Dwarf) utilizes an **instance method** that is invoked on an instance of the class using dot notation (e.g., `s.shine()`).
* To create a new instance, we use a **constructor**, facilitating the initialization of an object with particular properties, e.g., `new Star(mass)`, whereas direct field access (as seen in the original example) isn't encouraged due to encapsulation principles.
* **Dot notation** is employed to access the methods and instance variables of a class, improving readability and understanding in the code's interaction with objects.

This model enhances our simulation's adaptability to new celestial phenomena as additional star types can be characterized within this flexible framework, enriched by both astrophysical precision and programming versatility.

**Constructors in Java: Astrophysics Analogy**

In object-oriented programming, we typically use a _constructor_ to create instances, or objects, of a class. Let's explore this concept with an analogy that brings in ideas from astrophysics:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star s = new Star(5.0);
        s.emitLight();
    }
}
```

In this analogy, parameterized instantiation simplifies the process of defining numerous properties of celestial bodies, much like how individual stars can differ in mass. By incorporating a constructor into our `Star` class, we can achieve the desired functionality:

```java
public class Star {
    public double massInSolarMasses;

    public Star(double mass) {
        massInSolarMasses = mass;
    }

    public void emitLight() {
        if (massInSolarMasses < 0.5) {
            System.out.println("faint glow");
        } else if (massInSolarMasses < 3.0) {
            System.out.println("bright shine");
        } else {
            System.out.println("blazing intense light");
        }    
    }
}
```

The constructor `public Star(double mass)` is triggered whenever a `Star` object is instantiated with the `new` keyword. This setup is quite similar to the `__init__` method in Python, for those familiar with the language.

**Terminology Summary**

**Array Instantiation, Arrays of Objects**

As introduced early in HW0, Java arrays are instantiated using the `new` keyword. For instance:

```java
public class ArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five solar system masses. */
        double[] solarSystemMasses = new double[5];
        solarSystemMasses[0] = 1.0;
        solarSystemMasses[1] = 1.5;
    }
}
```

We can also declare arrays of objects, as demonstrated here:

```java
public class StarArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two stars. */
        Star[] stars = new Star[2];
        stars[0] = new Star(0.3);
        stars[1] = new Star(5.0);

        /* Expect a faint glow from stars[0], since it has a mass of 0.3 solar masses. */
        stars[0].emitLight();
    }
}
```

Notice the dual application of `new`: first, to set up an array to hold two `Star` objects, and then to instantiate each individual `Star`. This process resembles the collection of distinct celestial entities in the universe, while keeping our focus on learning Java concepts effectively.

The section on class methods and instance methods in Java provides a clear and engaging way to understand these core concepts by drawing parallels to astrophysical phenomena. To address the feedback, it is essential to refine certain metaphors and terminologies to ensure alignment with astrophysical accuracy while maintaining effective illustration.

#### Class Methods vs. Instance Methods in Astrophysics <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java allows us to define two types of methods:

* Class methods, a.k.a. static methods.
* Instance methods, a.k.a. non-static methods.

Instance methods are actions that can be taken only by a specific instance of a class, similar to how individual stars have unique origins and intrinsic properties within a galaxy. Static methods are actions applied at the class level, analogous to fundamental principles of physics that universally dictate celestial dynamics. Both are useful in different contexts. To illustrate a static method, consider a `Galaxy` class with a `calculateEscapeVelocity` method. Since it is static, it can be called as follows:

```java
v = Galaxy.calculateEscapeVelocity(300000); // assume mass in solar masses
```

If `calculateEscapeVelocity` had been an instance method, the call would instead resemble the following. Fortunately, `calculateEscapeVelocity` is designed as a static method, avoiding this syntax in practical scenarios.

```java
Galaxy g = new Galaxy();
v = g.calculateEscapeVelocity(300000);
```

It often makes sense to create classes incorporating both instance and static methods. For example, suppose we want to compare the brightness of two stars. A static method for this task can be defined in a `Star` class as follows:

```java
public static Star brighterStar(Star s1, Star s2) {
    if (s1.luminosity > s2.luminosity) {
        return s1;
    }
    return s2;
}
```

This method can be invoked using the class name, like so:

```java
Star s1 = new Star(1.0); // relative luminosity
Star s2 = new Star(10.0);
Star.brighterStar(s1, s2);
```

Notice that the method is accessed with the class name because it is a static function.

Alternatively, the `brighterStar` method could be implemented as a non-static method:

```java
public Star brighterStar(Star s2) {
    if (this.luminosity > s2.luminosity) {
        return this;
    }
    return s2;
}
```

Here, we use `this` to refer to the current star instance. Invocation resembles this syntax:

```java
Star s1 = new Star(1.0);
Star s2 = new Star(10.0);
s1.brighterStar(s2);
```

This approach parallels individual stars comparing their brightness directly, echoing how stars are studied in proximity.

**Exercise 1.2.1**: Analyze and determine what the following method does. If uncertain, execute or double-check your understanding.

```java
public static Star brighterStar(Star s1, Star s2) {
    if (luminosity > s2.luminosity) {
        return this;
    }
    return s2;
}
```

**Static Variables in Astrophysics**

Classes sometimes benefit from static variables, which hold values inherent to the class itself, akin to constants like the speed of light in a vacuum. Consider how this can be coded in a `PhysicsConstants` class:

```java
public class PhysicsConstants {
    public static final double speedOfLight = 299792458; // meters per second
    ...
}
```

Access static variables using the class name rather than an instance, i.e., `PhysicsConstants.speedOfLight`, not through instances such as `c.speedOfLight`—although possible, it is considered poor style and can lead to confusion.

**Exercise 1.2.2**: Explore the following exercise for deeper understanding:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

The above revisions aim to enhance the scientific integrity of the metaphors used, ensuring accurate analogies while maintaining clarity in explaining Java's programming concepts.

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

Incorporating concepts from astrophysics, let's explore the main method declaration that can be likened to coordinating an astronomical event, such as a solar eclipse. Here's the breakdown:

* `public`: This is akin to a universal phenomenon, observable by all in the cosmos to maximize visibility, similar to the almost universally visible solar eclipse.
* `static`: Like the fundamental constants of the universe, it remains unchanged across all instances, providing a solid, unchanging framework similar to the force of gravity.
* `void`: Similar to the concept of vacuum energy in space, which does not produce tangible matter but has an underlying presence.
* `main`: This serves as the central focal point, much like the sun in our solar system, crucial as the primary source of energy and light.
* `String[] args`: Analogous to cosmic rays, these parameters travel vast distances across the universe, bringing information from different cosmic regions.

**Command Line Arguments**

When a main method is invoked by the cosmic equivalent of a Java interpreter—imagine it as gravity pulling celestial bodies into a structured orbit—it's tasked with acquiring these parameters akin to gathering cosmic data. These are often sourced from command line inputs to the Java program. Consider examining the cosmic analogy for `ArgsDemo`, which is illustrated below:

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

**Exercise 1.2.3**: Imagine creating a program that calculates the sum of these command line arguments, hypothesizing they represent interstellar distances or values significant in space-time calculations. For an astronomical context, refer to astrophysical simulation resources or consult a repository, such as those found on GitHub, for solutions.

Feedback Integration: Although the astrophysical metaphors such as `static` being like universal laws and `void` as vacuum energy are creatively illustrative, we should balance artistic expression with technical accuracy. Keeping this in mind, I have aimed to enhance our analogies to be more consistent with current scientific understanding without compromising the intended illustrative purpose.

### Utilizing Cosmic Tools<a href="#using-libraries" id="using-libraries"></a>

In the realm of astrophysics, one of the paramount skills is the ability to discern and deploy existing cosmic tools and models effectively. The vast universe of astrophysics often allows researchers to circumvent years of observations and analyses by leveraging astronomical databases and simulation tools readily accessible online.

In this field, the following guidelines are imperative to follow:

* **Verify the Reliability**: Use only astronomical models that have been peer-reviewed or verified by the scientific community. This ensures that the data and models are credible and scientifically sound.
* **Cite Appropriately**: Always cite the sources of your cosmic data and any models you utilize. Proper citation is crucial for maintaining academic integrity and ensuring traceability of the scientific process.
* **Exercise Due Diligence**: Before using exact astronomical data or simulations for specific research experiments or hypotheses, conduct thorough investigations to confirm their relevance and accuracy.

For instance, it's appropriate to look for generalized "redshift calculation methods". However, directly searching for specific experiment data like "Black Hole Project Milky Way parameters" without proper methodology and validation is discouraged.

For more detailed guidelines on collaboration and maintaining academic honesty, refer to the astrophysical research conduct instructions.