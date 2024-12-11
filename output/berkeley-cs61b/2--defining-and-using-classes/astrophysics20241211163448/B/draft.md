# Programming with Classes and Methods

This chapter explores foundational concepts in Java programming, focusing on static versus non-static methods, object instantiation, constructors, and the role of the `main` method. It begins by differentiating between static methods, which are common operations associated with a class itself, and instance methods, which pertain to specific instances of a class, using the example of a `Star` class in Java. Static methods, demonstrated through a class method `emitLight`, are contrasted with the use of instance methods through instance variables that allow objects such as stars to exhibit diverse behaviors based on parameters like mass. This setup highlights the advantage of using object-oriented programming to represent complex entities such as celestial bodies in a more natural, simulation-friendly way.

The discussion extends to managing collections of objects through arrays in Java, emphasizing proper use of dot notation and the `new` keyword for object and array creation. The chapter also covers class versus instance methods further, illustrated by comparing galaxies' methods to calculate luminosity. Additionally, it introduces static variables, which are class-wide properties, and reviews the structure of the `main` method, serving as the entry point for running Java programs. Various exercises are embedded to consolidate understanding of concepts such as method design and practical use of command-line arguments, situating these programming techniques within the cosmic context of astrophysics simulations.



If you do not have prior experience with celestial mechanics, we recommend that you work through the exercises in [HW0](http://astro19.datastructur.es/materials/hw/hw0/hw0.html) before reading this chapter. It will cover various foundational concepts that we will not discuss in the book.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

All code concerning the motion of celestial bodies must be part of a class (or something similar to a class, which we'll explore later). Most calculations are performed within methods. Let's consider an example:

```java
public class Star {
    public static void emitLight() {
        System.out.println("Shine!");
    }
}
```

If we try running the `Star` class, we'll simply get an error message:

```
$ java Star
Error: Main method not found in class Star, please define the main method as:
       public static void main(String[] args)
```

The `Star` class we've defined doesn't do anything. We've simply defined something that `Star` **can** do, namely emit light. To actually execute the class, we'd either need to add a main method to the `Star` class, as we saw in chapter 1.1. Or we could create a separate [`StarSimulator`](https://www.youtube.com/watch?v=Q-LE-jJQLTM) class that runs methods from the `Star` class. For example, consider the program below:

```java
public class StarSimulator {
    public static void main(String[] args) {
        Star.emitLight();
    }
}
```

```
$ java StarSimulator
Shine!
```

A class that utilizes another class is sometimes called a "client" of that class, i.e. `StarSimulator` is a client of `Star`. Neither of the two techniques is inherently better: Adding a main method to `Star` may be preferable in some scenarios, while creating a client class like `StarSimulator` may be more suitable in others. The relative benefits of each approach will become apparent as we gain additional practice throughout the course.



**Instance Variables and Object Instantiation in Astrophysics**

Not all stars are alike. Some stars twinkle gently in the night sky, while others blaze brightly, illuminating the cosmos with their powerful radiance. Often, we explore the mysteries of the universe by creating simulations that capture these celestial phenomena, and programming languages like Java are equipped to help us craft such cosmic simulations.

One approach to representing the stellar diversity of the universe would be to create separate classes for each type of Star.

```java
public class RedDwarfStar {
    public static void shine() {
        System.out.println("dim twinkle twinkle");
    }
}

public class NeutronStar {
    public static void shine() {
        System.out.println("pulsating brilliance!");
    }
}
```

As with stellar classifications, classes can be instantiated, and instances can hold data. This leads to a more natural approach, where we create instances of the `Star` class and define the behavior of the `Star` methods based on the properties of the specific `Star`. To make this more concrete, consider the class below:

```java
public class Star {
    public double massInSolarMasses;

    public void shine() {
        if (massInSolarMasses < 0.5) {
            System.out.println("gentle glow...");
        } else if (massInSolarMasses < 1.5) {
            System.out.println("steady shimmer.");
        } else {
            System.out.println("brilliant blaze!");
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
        s.massInSolarMasses = 1.2;
        s.shine();
    }
}
```

When run, this program will create a `Star` with a mass of 1.2 solar masses, and that `Star` will emit a "steady shimmer.".

Some key observations and terminology:

* An `Object` in Java is an instance of any class.
* The `Star` class has its own variables, also known as _instance variables_ or _non-static variables_. These must be declared inside the class, unlike languages like Python or Matlab, where new variables can be added at runtime.
* The method that we created in the `Star` class did not have the `static` keyword. We call such methods _instance methods_ or _non-static methods_.
* To call the `shine` method, we had to first _instantiate_ a `Star` using the `new` keyword, and then make a specific `Star` shine. In other words, we called `s.shine()` instead of `Star.shine()`.
* Once an object has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `s = new Star();`
* Variables and methods of a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_.


**Constructors in Java**

In the vast cosmos of Java programming, just as astrophysicists construct models of celestial objects, we usually construct objects in object-oriented languages using a _constructor_:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star sirius = new Star(1.02);
        sirius.shine();
    }
}
```

Here, the instantiation is parameterized, saving us the light years of time and avoiding the cosmic messiness of manually typing out potentially many instance variable assignments. To enable such syntax, we need only add a "constructor" to our Star class, kind of like designing a star system model as shown below:

```java
public class Star {
    public double solarMass;

    public Star(double mass) {
        solarMass = mass;
    }

    public void shine() {
        if (solarMass < 0.5) {
            System.out.println("Faint twinkle.");
        } else if (solarMass < 1.5) {
            System.out.println("Steady glow.");
        } else {
            System.out.println("Blazing brilliance!");
        }    
    }
}
```

The constructor with signature `public Star(double mass)` will be invoked anytime that we try to create a `Star` using the `new` keyword and a single floating-point parameter. For those of you coming from Python, consider this constructor akin to the `__init__` method, which initializes the properties of a cosmic object.

**Terminology Summary**

**Array Instantiation, Arrays of Objects**

As we observed in our introductory study (HW0 equivalent), arrays are also instantiated in Java using the new keyword. Consider the following model:

```java
public class GalaxyDemo {
    public static void main(String[] args) {
        /* Create an array representing a cluster of five planetary mass objects. */
        double[] someMasses = new double[5];
        someMasses[0] = 0.3;
        someMasses[1] = 0.4;
    }
}
```

Similarly, we can create arrays of instantiated celestial objects in Java, for example:

```java
public class StarClusterDemo {
    public static void main(String[] args) {
        /* Create an array of two stars in a binary system. */
        Star[] binaryStars = new Star[2];
        binaryStars[0] = new Star(0.8);
        binaryStars[1] = new Star(1.02);

        /* A steady glow will result, since binaryStars[0] has mass 0.8. */
        binaryStars[0].shine();
    }
}
```

Observe that new is used in two different forms: Once to create an array that can "hold" (or rather "model") two `Star` objects, and twice more to create each individual `Star`, similar to modeling a constellation with different stars.

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java allows us to define two types of methods:

* Class methods, a.k.a. static methods.
* Instance methods, a.k.a. non-static methods.

Instance methods are actions that can be taken only by a specific instance of a class. Static methods are actions that are taken by the class itself. Both are useful in different circumstances. As an example of a static method, consider the `Universe` class that provides a `calculateLuminosity` method. Since it is static, we can call it as follows:

```java
luminosity = Universe.calculateLuminosity(starMass);
```

If `calculateLuminosity` had been an instance method, we would have instead the awkward syntax below. Luckily `calculateLuminosity` is a static method so we don't have to do this in real programs.

```java
Universe u = new Universe();
luminosity = u.calculateLuminosity(starMass);
```

Sometimes, it makes sense to have a class with both instance and static methods. For example, suppose we want the ability to compare two galaxies. One way to do this is to add a static method for comparing Galaxies.

```java
public static Galaxy largerGalaxy(Galaxy g1, Galaxy g2) {
    if (g1.mass > g2.mass) {
        return g1;
    }
    return g2;
}
```

This method could be invoked by, for example:

```java
Galaxy g = new Galaxy(1.5E12);
Galaxy g2 = new Galaxy(1E12);
Galaxy.largerGalaxy(g, g2);
```

Observe that we've invoked using the class name, since this method is a static method.

We could also have implemented `largerGalaxy` as a non-static method, e.g.

```java
public Galaxy largerGalaxy(Galaxy g2) {
    if (this.mass > g2.mass) {
        return this;
    }
    return g2;
}
```

Above, we use the keyword `this` to refer to the current object. This method could be invoked, for example, with:

```java
Galaxy g = new Galaxy(1.5E12);
Galaxy g2 = new Galaxy(1E12);
g.largerGalaxy(g2);
```

Here, we invoke the method using a specific instance variable.

**Exercise 1.2.1**: What would the following method do? If you're not sure, try it out.

```java
public static Galaxy largerGalaxy(Galaxy g1, Galaxy g2) {
    if (mass > g2.mass) {
        return this;
    }
    return g2;
}
```

**Static Variables**

It is occasionally useful for classes to have static variables. These are properties inherent to the class itself, rather than the instance. For example, we might record that the scientific name (or binomen) for galaxies in our study is "Milky Way based models":

```java
public class Galaxy {
    public double mass;
    public static String modelType = "Milky Way based models";
    ...
}
```

Static variables should be accessed using the name of the class rather than a specific instance, e.g. you should use `Galaxy.modelType`, not `g.modelType`.

While Java technically allows you to access a static variable using an instance name, it is bad style, confusing, and in my opinion an error by the Java designers.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String\[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

Venturing beyond Earth, it’s essential to understand how the machinery of space probes and simulations start their operations. Much like initiating a spacecraft's systems, let’s unpack the main method declaration, which initiates a Java program:

* `public`: This signals the method is available universally, akin to broadcasting signals to space.
* `static`: The method is universal, resembling principles in physics that are not tied to particular locations in space.
* `void`: Denotes no information will return, similar to a one-way communication channel.
* `main`: The designated name for this initiation process, like the main thruster in a spacecraft.
* `String[] args`: Parameters provided to the main method, analogous to data from space probes.

**Stellar Data Arguments**

Since the main method is engaged by the Java interpreter, it is analogous to mission control relaying commands or data scientists passing initial inputs for a space simulation. These arguments represent command line inputs. Consider the program `AstroArgsDemo` below:

```java
public class AstroArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program prints out the 0th command line argument, analogous to receiving telemetry data:

```
$ java AstroArgsDemo Earth Mars Venus
Earth
```

In the demonstration above, `args` could be likened to an array of celestial names or objects, where inputs are {"Earth", "Mars", "Venus"}.

**Summing Astronomical Distances**

**Exercise 1.2.3**: Try to write a program that sums up command line arguments, assuming they represent distances between celestial bodies in astronomical units (AU). For a solution, consult your simulation platform or the provided resources at the observatory.

#### Utilizing Research Papers <a href="#utilizing-research-papers" id="utilizing-research-papers"></a>

One of the most crucial skills as an astrophysicist is knowing how to find and use existing research papers. In the remarkable modern era, it is frequently possible to save yourself considerable time and data analysis by consulting the Cosmos for insights.

In this field, you're encouraged to do this, with the following conditions:

* Do not rely on research papers that are not peer-reviewed.
* Reference your sources.
* Do not search for specific solutions to detailed star mapping or galactic modeling issues.

For example, it's fine to look for information about "classifying exoplanet atmospheres using spectroscopy". However, it is not acceptable to search for "Black Hole Event Horizon simulations from NASA." 

For more on collaboration and research integrity policy, please refer to the course syllabus. 
