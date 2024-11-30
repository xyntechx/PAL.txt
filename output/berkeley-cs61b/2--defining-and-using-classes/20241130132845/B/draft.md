# 2. Defining and Using Classes with Astrophysics Applications

If you're new to Java, it's recommended that you complete the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before diving into this chapter. This will help you grasp some syntax rules that we won't cover here, but are essential for weaving astrophysical concepts into Java programming.

#### Static vs. Non-Static Methods in Astrophysics Context <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

In astrophysics, concepts are often modeled using equations and simulations that we can encode into Java. All Java code must reside inside a class (or a variation thereof). Most Java code is encapsulated within methods. Let's consider an astrophysics-inspired example:

```java
public class Star {
    public static void emitLight() {
        System.out.println("The star shines brightly!");
    }
}
```

If you attempt to execute the `Star` class directly, you'll encounter an error:

```
$ java Star
Error: Main method not found in class Star, please define the main method as:
       public static void main(String[] args)
```

Our `Star` class defines what a star **can** do—emit light—but it doesn't actually perform any action on its own. To execute this class, you need a `main` method within the `Star` class or a separate `StarSimulator` class to run the `Star`'s method. For instance:

```java
public class StarSimulator {
    public static void main(String[] args) {
        Star.emitLight();
    }
}
```

```
$ java StarSimulator
The star shines brightly!
```

A class utilizing another is termed a "client" of that class, so `StarSimulator` is a client of `Star`. Either technique can be useful: Adding a `main` method to `Star` might suit certain situations, just as creating a client class like `StarSimulator` might better serve others. The benefits of each approach will become clearer as you gain more experience throughout this course.

**Instance Variables and Object Instantiation**

Not all stars are alike—they come in different sizes and luminosities. To represent these variations, you might consider defining specific classes for each type of star.

```java
public class RedDwarfStar {
    public static void emitLight() {
        System.out.println("The red dwarf star glows faintly.");
    }
}

public class SupergiantStar {
    public static void emitLight() {
        System.out.println("The supergiant star blazes intensely!");
    }
}
```

Frequently, classes in Java are instantiated, with instances containing data, providing a more natural representation of diverse astronomical bodies. To illustrate:

```java
public class Star {
    public int brightnessInLumens;

    public void emitLight() {
        if (brightnessInLumens < 100) {
            System.out.println("The star has a gentle glow.");
        } else if (brightnessInLumens < 1000) {
            System.out.println("The star is moderately bright.");
        } else {
            System.out.println("The star shines with exceptional intensity!");
        }
    }    
}
```

Consider this in practical use:

```java
public class StarSimulator {
    public static void main(String[] args) {
        Star s;
        s = new Star();
        s.brightnessInLumens = 500;
        s.emitLight();
    }
}
```

Running the program above creates a `Star` with brightness 500 lumens, emitting a message saying "The star is moderately bright."

Key observations and terminology:

* An `Object` in Java is an instance of any class.
* The `Star` class houses instance or non-static variables. Unlike dynamic languages like Python or Matlab, Java requires variable declaration inside the class.
* The `emitLight` method is an instance method since it lacks the `static` keyword.
* To invoke `emitLight`, instantiate a `Star` first: `s.emitLight()` not `Star.emitLight()`.
* Instantiated objects can be assigned to declared variables via `s = new Star();`
* Access class members using dot notation.

**Constructors in Java for Astronomical Objects**

To unleash the power of object-oriented programming with cosmic entities, constructors facilitate object creation:

```java
public class StarSimulator {
    public static void main(String[] args) {
        Star s = new Star(700);
        s.emitLight();
    }
}
```

An instance gets parameterized upon instantiation, minimizing laborious data assignments. The `Star` class is adjusted accordingly:

```java
public class Star {
    public int brightnessInLumens;

    public Star(int b) {
        brightnessInLumens = b;
    }

    public void emitLight() {
        if (brightnessInLumens < 100) {
            System.out.println("The star has a gentle glow.");
        } else if (brightnessInLumens < 1000) {
            System.out.println("The star is moderately bright.");
        } else {
            System.out.println("The star shines with exceptional intensity!");
        }    
    }
}
```

The constructor `public Star(int b)` initialises a `Star` when an integer parameter is passed. This is akin to Python's `__init__` method.

**Terminology Summary**

**Array Instantiation, Arrays of Astronomical Objects**

Per HW0, arrays are instantiated in Java with `new`.

```java
public class ArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five integers. */
        int[] magnitudeArray = new int[5];
        magnitudeArray[0] = 10;
        magnitudeArray[1] = 20;
    }
}
```

Similarly, create arrays of instantiated celestial bodies:

```java
public class StarArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two stars. */
        Star[] stars = new Star[2];
        stars[0] = new Star(90);
        stars[1] = new Star(980);

        /* A gentle glow as stars[0] has brightness 90 lumens. */
        stars[0].emitLight();
    }
}
```

Note that `new` is used twice: Once for allocating two `Star` object slots, and individually creating each `Star`.

#### Class Methods vs. Instance Methods in Astrophysical Applications <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java allows defining two method types:

* Class (Static) Methods.
* Instance (Non-Static) Methods.

Instance methods are specific to class instances, while static methods pertain to the class itself, each useful in different scenarios. For instance, consider celestial navigation:

```java
x = Math.sqrt(distanceToCentauri);
```

Here, static `sqrt` is utilized, foregoing awkward instantiation syntax.

```java
Math m = new Math();
x = m.sqrt(distanceToCentauri);
```

Class methods alongside instance methods provide flexibility. For example, if comparing star luminosities, a static method might suffice:

```java
public static Star brightestStar(Star s1, Star s2) {
    if (s1.brightnessInLumens > s2.brightnessInLumens) {
        return s1;
    }
    return s2;
}
```

Invoke it thus:

```java
Star s1 = new Star(300);
Star s2 = new Star(5000);
Star.brightestStar(s1, s2);
```

Here, the method called via the class name suggests its static nature.

Alternatively, an instance-based approach might be:

```java
public Star brightestStar(Star s2) {
    if (this.brightnessInLumens > s2.brightnessInLumens) {
        return this;
    }
    return s2;
}
```

Invoke it using an instance variable:

```java
Star s1 = new Star(300);
Star s2 = new Star(5000);
s1.brightestStar(s2);
```

**Exercise 1.2.1**: Predict the behavior of the following method. Test if uncertain.

```java
public static Star brightestStar(Star s1, Star s2) {
    if (brightnessInLumens > s2.brightnessInLumens) {
        return this;
    }
    return s2;
}
```

**Static Variables**

Static variables sometimes describe universal class properties, not linked to an instance. For instance, defining constants for a celestial object:

```java
public class Star {
    public int brightnessInLumens;
    public static String galaxy = "Milky Way";
    ...
}
```

Access static variables via the class name, e.g., `Star.galaxy`, rather than instance names.

Using instances for static variables, while possible, is stylistically discouraged, considered a design flaw in Java.

**Exercise 1.2.2**: Complete this astronomically themed exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String[] args) in Astrophysics Context <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

Let's dissect the familiar `main` method in our explorations so far:

* `public`: Initiator of our methods.
* `static`: Without a specific instance tie.
* `void`: Lacks return type.
* `main`: Method's name.
* `String[] args`: Command-line parameter for the main method.

**Command Line Arguments in Astronomy Simulations**

The Java interpreter calls `main`, expected to provide these arguments, typically as command line inputs. Consider the `ArgsDemo` program:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

Executing such a program with arguments:

```
$ java ArgsDemo Polaris is a star
Polaris
```

In the example above, `args` would hold {"Polaris", "is", "a", "star"}.

**Summing Celestial Data from Command Line**

**Exercise 1.2.3**: Develop a program summing numerical command line arguments. Explore solutions on GitHub or available webcast resources.

#### Leveraging Libraries for Astronomy Simulations <a href="#using-libraries" id="using-libraries"></a>

A key programmer's skill is efficiently sourcing and utilizing libraries. With online resources, avoid reinventing and debugging; seek existing solutions—but adhere to course guidelines:

* Use provided libraries only.
* Cite all references.
* Avoid specific homework/project problem searches.

For instance, "convert String integer Java" is permissible, yet "Project 2048 Berkeley" isn't.

Ascertain course policies on collaboration and academic sincerity as detailed within the syllabus.