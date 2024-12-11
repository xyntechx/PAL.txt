# Static vs. Non-Static Methods

In this chapter, we explore the fundamental distinction between static and non-static methods in Java programming, emphasizing their role and implementation. Static methods, marked by the `static` keyword, are associated directly with the class they belong to, meaning they can be invoked using the class name without needing an object instance. This is illustrated through examples, including the `emitLight` method in the `Star` class and the usage of utility methods like `Math.sqrt`. On the other hand, non-static methods, or instance methods, are tied to specific instances of a class, thus requiring object instantiation to be called. The chapter delves into these concepts, demonstrating how instance variables can alter the behavior of an instance method, as seen in variations of the `Star` class where the `emitLight` method's output depends on the mass assigned to a particular instance.

The chapter further expands on constructors and how they facilitate object initialization, saving time and improving clarity by allowing parameters to govern instance variable assignment at the object's creation. Additionally, it introduces static and instance variables, explaining their access and usage within different methods types, emphasizing good coding practices. The text also covers the instantiation of arrays and their ability to contain objects, illustrating how to manage collections of class instances. Finally, the chapter touches upon the significance of the `main` method in Java as a static entry point, the utility of handling command-line arguments, and the importance of understanding and using existing libraries responsibly in programming. Together, these concepts form a solid foundation in understanding Java's object-oriented functionalities and preparing for more advanced topics.

Static vs. Non-Static Methods

**Static Methods**

All code in Java must be part of a class (or something similar to a class, which we'll learn about later). Most code is written inside of methods. Let's consider an example:

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

The `Star` class we've defined doesn't do anything. We've simply defined something that `Star` **can** do, namely emit light. To actually run the class, we'd either need to add a main method to the `Star` class, as we saw in chapter 1.1. Or we could create a separate [`StarLauncher`](https://www.youtube.com/watch?v=Q-LE-jJQLTM) class that runs methods from the `Star` class. For example, consider the program below:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star.emitLight();
    }
}
```

```
$ java StarLauncher
Shine!
```

A class that uses another class is sometimes called a "client" of that class, i.e. `StarLauncher` is a client of `Star`. Neither of the two techniques is better: Adding a main method to `Star` may be better in some situations, and creating a client class like `StarLauncher` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout the course.

**Instance Variables and Object Instantiation**

Not all stars are alike. Some stars twinkle faintly in the vast cosmos, while others blaze fiercely, illuminating entire galaxies with their radiant glow. Often, we write programs to mimic features of the universe we inhabit, and Java's syntax was crafted to easily allow such mimicry.

One approach to allowing us to represent the spectrum of Stardom would be to create separate classes for each type of Star.

```java
public class DwarfStar {
    public static void emitLight() {
        System.out.println("flicker flicker flicker");
    }
}

public class SupernovaStar {
    public static void emitLight() {
        System.out.println("kaboom!");
    }
}
```

As you should have seen in the past, classes can be instantiated, and instances can hold data. This leads to a more natural approach, where we create instances of the `Star` class and make the behavior of the `Star` methods contingent upon the properties of the specific `Star`. To make this more concrete, consider the class below:

```java
public class Star {
    public double mass;

    public void emitLight() {
        if (mass < 1.0) {
            System.out.println("twinkle, twinkle, little star.");
        } else if (mass < 10.0) {
            System.out.println("shine. shine.");
        } else {
            System.out.println("blinding brightness!");
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
        s.mass = 5.0;
        s.emitLight();
    }
}
```

When run, this program will create a `Star` with mass 5.0, and that `Star` will soon let out a nice "shine. shine.".

Some key observations and terminology:

* An `Object` in Java is an instance of any class.
* The `Star` class has its own variables, also known as _instance variables_ or _non-static variables_. These must be declared inside the class, unlike languages like Python or Matlab, where new variables can be added at runtime.
* The method that we created in the `Star` class did not have the `static` keyword. We call such methods _instance methods_ or _non-static methods_.
* To call the `emitLight` method, we had to first _instantiate_ a `Star` using the `new` keyword, and then make a specific `Star` shine. In other words, we called `s.emitLight()` instead of `Star.emitLight()`.
* Once an object has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `s = new Star();`
* Variables and methods of a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_.

**Constructors in Java**

As you've hopefully seen before, we usually construct objects in object oriented languages using a _constructor_:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star s = new Star(5.0);
        s.emitLight();
    }
}
```

Here, the instantiation is parameterized, saving us the time and messiness of manually typing out potentially many instance variable assignments. To enable such syntax, we need only add a "constructor" to our Star class, as shown below:

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
            System.out.println("blinding brightness!");
        }    
    }
}
```

The constructor with signature `public Star(double m)` will be invoked anytime that we try to create a `Star` using the `new` keyword and a single double parameter. For those of you coming from Python, the constructor is very similar to the `__init__` method.

Array Instantiation, Arrays of Astrophysical Objects

As we saw in HW0, arrays are also instantiated in Java using the new keyword. For example:

```java
public class ArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five stars. */
        int[] starArray = new int[5];
        starArray[0] = 3;
        starArray[1] = 4;
    }
}
```

Similarly, we can create arrays of instantiated astrophysical objects in Java, e.g.

```java
public class PlanetArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two planets. */
        Planet[] planets = new Planet[2];
        planets[0] = new Planet(8.0);
        planets[1] = new Planet(20.0);

        /* Observe the gravitational impact, since planets[0] has a mass of 8.0. */
        planets[0].exertGravity();
    }
}
```

Observe that new is used in two different ways: Once to create an array that can hold two `Planet` objects, and twice to create each actual `Planet`.

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java allows us to define two types of methods:

* Class methods, a.k.a. static methods.
* Instance methods, a.k.a. non-static methods.

Instance methods are actions that can be taken only by a specific instance of a class. Static methods are actions that are taken by the class itself. Both are useful in different circumstances. As an example of a static method, the `Math` class provides a `sqrt` method. Because it is static, we can call it as follows:

```java
x = Math.sqrt(100);
```

If `sqrt` had been an instance method, we would have instead the awkward syntax below. Luckily `sqrt` is a static method so we don't have to do this in real programs.

```java
Math m = new Math();
x = m.sqrt(100);
```

Sometimes, it makes sense to have a class with both instance and static methods. For example, suppose we want the ability to compare two planets. One way to do this is to add a static method for comparing Planets.

```java
public static Planet maxPlanet(Planet p1, Planet p2) {
    if (p1.mass > p2.mass) {
        return p1;
    }
    return p2;
}
```

This method could be invoked by, for example:

```java
Planet p = new Planet(15.0);
Planet p2 = new Planet(100.0);
Planet.maxPlanet(p, p2);
```

Observe that we've invoked using the class name, since this is a static method.

We could also have implemented `maxPlanet` as a non-static method, e.g.

```java
public Planet maxPlanet(Planet p2) {
    if (this.mass > p2.mass) {
        return this;
    }
    return p2;
}
```

Above, we use the keyword `this` to refer to the current object. This method could be invoked, for example, with:

```java
Planet p = new Planet(15.0);
Planet p2 = new Planet(100.0);
p.maxPlanet(p2);
```

Here, we invoke the method using a specific instance variable.

**Exercise 1.2.1**: What would the following method do? If you're not sure, try it out.

```java
public static Planet maxPlanet(Planet p1, Planet p2) {
    if (mass > p2.mass) {
        return this;
    }
    return p2;
}
```

**Static Variables**

It is occasionally useful for classes to have static variables. These are properties inherent to the class itself, rather than the instance. For example, we might record that the astronomical classification for planets is "Celestial Bodies":

```java
public class Planet {
    public double mass;
    public static String classification = "Celestial Bodies";
    ...
}
```

Static variables should be accessed using the name of the class rather than a specific instance, e.g. you should use `Planet.classification`, not `p.classification`.

While Java technically allows you to access a static variable using an instance name, it is bad style, confusing, and in my opinion an error by the Java designers.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe\_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

## main Sequence and method Implementation

Now that we've reached this stage, it's time to break down the composition of the method declaration we've used frequently. Analyzing it, we have:

* `public`: All of our methods that define cosmic phenomena begin with this keyword.
* `static`: This signifies the method's static nature, much like a cosmic constant.
* `void`: It does not return light or data.
* `main`: Formally recognized as the principal method in our cosmic simulations.
* `String[] args`: This parameter acts as the initial conditions for the universe we are going to simulate.

**Galactic Command Line Arguments**

Since the `main` method is invoked by the Java interpreter analogous to how astronomers might initiate observations with telescopes, it is the universe's framework that provides these conditions. These typically correspond to the command line parameters similar to how parameters define the observational setup in an astrophysical survey. Consider the program `GalaxySimulator` below:

```java
public class GalaxySimulator {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This cosmic program prints out the initial parameter, e.g.

```
$ java GalaxySimulator MilkyWay Andromeda Triangulum
MilkyWay
```

In this astrophysical example, `args` will be an array of Strings, where the elements are {"MilkyWay", "Andromeda", "Triangulum"}.

**Calculating Cosmic Elapsed Time**

**Exercise 1.2.3**: Attempt to write a program that calculates the elapsed time since the big bang using the input as cosmic eras in billions of years. For a detailed method, see the cosmic lecture or the algorithm provided on our simulation archives.

#### Utilizing Cosmic Libraries <a href="#using-cosmic-libraries" id="using-cosmic-libraries"></a>

Understanding how to access and implement pre-existing cosmic data libraries is an invaluable skill for an astrophysicist. In the expansive cosmos of data, efficiency and accuracy can be significantly enhanced by relying on established theories and models.

In this course, you’re encouraged to explore libraries, keeping these guidelines in mind:

* Avoid using any cosmic libraries that have not been provided.
* Acknowledge and reference your sources of astronomical inspiration.
* Refrain from directly searching solutions for specific space mission challenges or research assignments.

For instance, it's appropriate to search for "convert parsecs to light years in Java," but inappropriate to search for "exact algorithm for detecting exoplanets specific to our galactic survey project".

For more on collaboration, universal ethics, and our research integrity policy, refer to the university interstellar guidebook.