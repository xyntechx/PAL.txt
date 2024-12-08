# 2. Defining and Using Celestial Objects

If you do not have a prior background in object-oriented programming, we recommend that you explore introductory exercises before diving into this chapter. It will help you understand various syntax issues that we will not discuss here.

#### Static vs. Non-Static Methods in Celestial Simulations <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

In Java, all code must be encapsulated within a class. Most code is written inside methods. To illustrate this, let's consider an example involving a celestial object:

```java
public class Star {
    public static void emitLight() {
        System.out.println("Shining Bright!");
    }
}
```

Attempting to run the `Star` class by itself results in an error message:

```
$ java Star
Error: Main method not found in class Star, please define the main method as:
       public static void main(String[] args)
```

Here, the `Star` class simply defines a method to emit light, but doesn't execute any functionality by itself. To utilize the `Star` class, you need to define a main method within it or introduce a separate launcher class, such as `StarLauncher`, as shown below:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star.emitLight();
    }
}
```

```
$ java StarLauncher
Shining Bright!
```

A class running another class can be considered its "client," for instance, `StarLauncher` acts as a client of `Star`. There are advantages to both approaches which will become clearer with practice.

**Instance Variables and Object Instantiation**

Not all celestial bodies are identical. Stars could vary in brightness, size, or the type of light they emit. As we seek to model the universe, our programs must reflect such variance. Instead of creating a new class for each type of star, a more nuanced approach is to use instance variables.

```java
public class Star {
    public double luminosity;

    public void emitLight() {
        if (luminosity < 1.0) {
            System.out.println("Dim shine.");
        } else if (luminosity < 5.0) {
            System.out.println("Moderate shine.");
        } else {
            System.out.println("Blinding shine!");
        }
    }    
}
```

When executed, the program below creates a `Star` with certain luminosity:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star s;
        s = new Star();
        s.luminosity = 3.5;
        s.emitLight();
    }
}
```

This program will create a `Star` with a luminosity of 3.5 which emits a "Moderate shine.".

**Constructors in Celestial Modeling**

Most celestial objects in simulation scenarios are constructed using a constructor, enabling parameterized instantiation:

```java
public class Star {
    public double luminosity;

    public Star(double lum) {
        luminosity = lum;
    }

    public void emitLight() {
        if (luminosity < 1.0) {
            System.out.println("Dim shine.");
        } else if (luminosity < 5.0) {
            System.out.println("Moderate shine.");
        } else {
            System.out.println("Blinding shine!");
        }    
    }
}
```

Here, creating a `Star` object can be simplified and optimized with its luminosity parameter:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star s = new Star(6.8);
        s.emitLight();
    }
}
```

The constructor `Star(double lum)` is triggered when creating a new `Star` using specific parameters.

**Arrays in Celestial Simulations**

Arrays can be used to store collections of celestial objects, as demonstrated:

```java
public class GalaxySimulation {
    public static void main(String[] args) {
        /* Create an array of stars */
        Star[] stars = new Star[3];
        stars[0] = new Star(0.8);
        stars[1] = new Star(2.3);
        stars[2] = new Star(7.5);

        /* Each star emits its respective light */
        stars[2].emitLight();  // Should say "Blinding shine!"
    }
}
```

#### Class Methods vs. Instance Methods in Astrophysics Context <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Two types of methods exist in Java:

* Class methods (Static methods).
* Instance methods (Non-static methods).

For comparing celestial bodies like stars, we can use a static method:

```java
public static Star brighterStar(Star s1, Star s2) {
    if (s1.luminosity > s2.luminosity) {
        return s1;
    }
    return s2;
}
```

Use this method to compare stars as follows:

```java
Star s1 = new Star(2.7);
Star s2 = new Star(4.4);
Star.brightestStar(s1, s2);
```

In scenarios focusing on instance-specific interactions, like gravitational interactions, instance methods prove beneficial.

**Static Variables in Astrophysics**

Static variables are characteristics common to all instances of a class, for example:

```java
public class Star {
    public double luminosity;
    public static String galaxy = "Milky Way";
    ...
}
```

Static variables like `Star.galaxy` should typically be accessed using the class name, `Star.galaxy` not `s.galaxy`.

In astrophysics-related programming, comprehensively understanding how to manage and manipulate celestial simulations using object-oriented programming enhances simulations and model accuracy, contributing to our understanding of the universe.