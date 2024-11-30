# 2. Defining and Using Classes with Astrophysics Applications

If you're new to Java, it's recommended that you complete the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before diving into this chapter. These exercises will help you grasp some syntax rules that we won't cover here, but are essential for applying astrophysical concepts in Java programming.

#### Static vs. Non-Static Methods in Astrophysics Context <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

In astrophysics, equations and simulations often model cosmic phenomena and can be encoded into Java programs. All Java code must reside inside a class, and typically, code functionality is encapsulated within methods. Let's consider an astrophysics-inspired example:

```java
public class Star {
    public static void emitLight() {
        System.out.println("The star shines brightly!");
    }
}
```

If you attempt to execute the `Star` class directly without a `main` method, you'll encounter an error:

```
$ java Star
Error: Main method not found in class Star, please define the main method as:
       public static void main(String[] args)
```

Our `Star` class has a static method `emitLight` that outputs a message representing the star's capability to emit light. However, to execute this method, you need a `main` method within the `Star` class or a "client" class, such as `StarSimulator`:

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

In this example, `StarSimulator` serves as a client class that utilizes the `Star` class. Both approaches—embedding the `main` method within `Star` or using an external client class—are useful, depending on the context.

**Instance Variables and Object Instantiation**

Stars in the universe exhibit diverse sizes and luminosities. We can use instance variables in Java to model these variations rather than creating separate classes for each star type.

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

This class allows for the creation of different `Star` instances with varying luminosities:

```java
public class StarSimulator {
    public static void main(String[] args) {
        Star s = new Star();
        s.brightnessInLumens = 500;
        s.emitLight();
    }
}
```

Running the above code creates a `Star` instance with a brightness of 500 lumens, outputting "The star is moderately bright."

Key concepts and terminology:

* An `Object` in Java is an instance of a class.
* The `emitLight` method is an instance method as it operates on an instance of `Star` and accesses the instance variable `brightnessInLumens`.
* To use non-static methods, a class instance must be created first.
* Instantiate objects with `new`, e.g., `Star s = new Star();`.
* Access object methods and variables using dot notation, e.g., `s.emitLight()`.

**Constructors in Java for Astronomical Objects**

Constructors streamline object instantiation by initializing class fields at the time of object creation:

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

Instead of setting `brightnessInLumens` separately, it is initialized during object creation:

```java
public class StarSimulator {
    public static void main(String[] args) {
        Star s = new Star(700);
        s.emitLight();
    }
}
```

**Terminology Summary**

* Static methods belong to the class and can be called without an instance.
* Instance methods are invoked on objects, requiring object instantiation.
* Constructors initialize object state upon creation.

**Array Instantiation, Arrays of Astronomical Objects**

Familiarize yourself with arrays as seen in HW0, where arrays are created using `new`:

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

Similarly, instantiate arrays of celestial objects:

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

Note that `new` is used to create the array itself and each `Star` object within the array.

#### Class Methods vs. Instance Methods in Astrophysical Applications <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java allows for two types of methods:

* Class (Static) Methods
* Instance (Non-Static) Methods

Instance methods relate to specific object instances, while static methods can be called on the class itself. An example is computing distances in celestial navigation:

```java
x = Math.sqrt(distanceToCentauri);
```

Here, `Math.sqrt` is a static method called directly using the class name.

For cases like comparing luminosities of stars, either method type could work:

```java
public static Star brightestStar(Star s1, Star s2) {
    if (s1.brightnessInLumens > s2.brightnessInLumens) {
        return s1;
    }
    return s2;
}
```

Invoke the static method with:

```java
Star s1 = new Star(300);
Star s2 = new Star(5000);
Star.brightestStar(s1, s2);
```

Alternatively, an instance method approach might be:

```java
public Star brightestStar(Star s2) {
    if (this.brightnessInLumens > s2.brightnessInLumens) {
        return this;
    }
    return s2;
}
```

Call it with an instance:

```java
Star s1 = new Star(300);
Star s2 = new Star(5000);
s1.brightestStar(s2);
```

**Exercise 1.2.1**: Predict the behavior of the following method. Test if uncertain.

```java
public static Star brightestStar(Star s1, Star s2) {
    if (s1.brightnessInLumens > s2.brightnessInLumens) {
        return s1;
    }
    return s2;
}  // Removed incorrect 'this' usage in static context
```

**Static Variables**

Static variables describe universal attributes of a class, not linked to specific objects. For instance, a constant for a celestial object's galaxy:

```java
public class Star {
    public int brightnessInLumens;
    public static String galaxy = "Milky Way";
    // Other members...
}
```

Access static variables via the class name, e.g., `Star.galaxy`, not via instances.

**Exercise 1.2.2**: Complete this astronomy-themed exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### Understanding `public static void main(String[] args)` in Astrophysics Context <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

The `main` method is central in Java programming, typically designed as:

* `public`: Accessible by Java runtime.
* `static`: Callable without instance.
* `void`: No return value.
* `main`: Method name, beginning program execution.
* `String[] args`: Accepts command-line arguments.

**Command Line Arguments in Astronomy Simulations**

The method’s `args` receives input arguments, enabling dynamic handling of execution parameters. Consider `ArgsDemo`:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

Invoke as:

```
$ java ArgsDemo Polaris is a star
Polaris
```

Here, `args` contains the strings entered after the program name.

**Summing Celestial Data from Command Line**

**Exercise 1.2.3**: Develop a program summing numerical command line arguments. Explore solutions on GitHub or available webcast resources.

#### Leveraging Libraries for Astronomy Simulations <a href="#using-libraries" id="using-libraries"></a>

A key skill is identifying existing library solutions for problems. Utilize the wealth of resources online to avoid unnecessary effort—always adhering to course guidelines:

* Use available libraries responsibly.
* Cite all references and sources.
* Avoid searching for answers specific to assignments.

Broad searches like "convert String to integer Java" are generally fine, whereas direct queries related to specific assignments are not.

Familiarize yourself with the course’s collaboration and academic honesty policies detailed in the syllabus for guidance.