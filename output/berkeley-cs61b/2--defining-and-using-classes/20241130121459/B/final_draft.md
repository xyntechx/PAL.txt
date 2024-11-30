# 2. Defining and Using Classes in Astrophysics Simulations

If you do not have prior Java experience, we recommend that you work through the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before reading this chapter. It will cover various syntax issues that we will not discuss in the book.

#### Static vs. Non-Static Methods in Astrophysics <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

In Java, all code must be part of a class. Java classes can be utilized to model various astronomical phenomena, akin to how stars and planets are fundamental entities in astrophysics. Most code resides inside methods. Let's consider an example where we simulate a simple astronomical phenomenon:

```java
public class Star {
    public static void emitLight() {
        System.out.println("Twinkle, twinkle!");
    }
}
```

If you try to run the `Star` class directly, you'll get an error message:

```
$ java Star
Error: Main method not found in class Star, please define the main method as:
       public static void main(String[] args)
```

The `Star` class solely describes what a Star **can** do—emit light, much like theoretical models that illustrate potential star behaviors. To simulate this, a client class calls the method:

```java
public class StarSimulator {
    public static void main(String[] args) {
        Star.emitLight();
    }
}
```

```
$ java StarSimulator
Twinkle, twinkle!
```

The `StarSimulator` class functions as a client to the `Star` class. This mirrors how astrophysical research employs simulations to test and predict cosmic phenomena. Choosing whether to include a main method directly in `Star` or utilizing a separate client class depends on clarity and the complexity of the simulation.

**Instance Variables and Object Instantiation in Astrophysical Models**

Stars are not uniform; they vary in brightness, size, and temperature. Our simulations aim to reflect this diversity by creating dynamic instances that model these variations.

Consider a `Star` class designed with properties for luminosity, size, and temperature:

```java
public class Star {
    public double luminosity;
    public double size;

    public void categorizeStar() {
        if (size < 1) {
            System.out.println("Dwarf Star");
        } else if (size < 10) {
            System.out.println("Main Sequence Star");
        } else {
            System.out.println("Giant Star");
        }
    }    
}
```

Instantiate this class to simulate a specific star's characteristics:

```java
public class StarSimulator {
    public static void main(String[] args) {
        Star sun = new Star();
        sun.size = 1.0;
        sun.categorizeStar();
    }
}
```

Running this program, the `Star` object `sun` is categorized as a "Main Sequence Star". This capability parallels constructing models of celestial objects with distinct characteristics in astrophysical studies.

Key points and terminology:

* An `Object` in Java symbolizes an instance of any class.
* The `Star` class utilizes instance variables or non-static variables, representing physical properties of each star like luminosity.
* You invoke the `categorizeStar` method on instantiated objects, as in `sun.categorizeStar()`.
* Using `new`, you instantiate each star with specific features, emulating real celestial bodies.

**Using Constructors for Celestial Simulation Initiatives**

Constructors in astrophysics simulations effectively define initial conditions for stars:

```java
public class Star {
    public double luminosity;
    public double size;

    public Star(double sz) {
        size = sz;
    }

    public void categorizeStar() {
        if (size < 1) {
            System.out.println("Dwarf Star");
        } else if (size < 10) {
            System.out.println("Main Sequence Star");
        } else {
            System.out.println("Giant Star");
        }    
    }
}
```

Using constructors, you set up new stars with properties tailored to specific simulation objectives, allowing for variance in star behavior based on size and other attributes.

**Managing Arrays of Celestial Bodies**

Simulations might involve vast arrays of objects, akin to stars or planets across a galaxy.

```java
public class GalaxyDemo {
    public static void main(String[] args) {
        /* Create an array of stars in a galaxy. */
        Star[] galaxy = new Star[3];
        galaxy[0] = new Star(0.5);
        galaxy[1] = new Star(7);
        galaxy[2] = new Star(50);

        /* Categorize each star based on its size. */
        for (Star star : galaxy) {
            star.categorizeStar();
        }
    }
}
```

This method reflects real astrophysical studies, capturing scenarios ranging from star clusters to entire galaxies and star systems.

#### Class Methods vs. Instance Methods in a Cosmic Framework <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java's class and instance methods enable modeling both universal cosmic phenomena and specific celestial events. Instance methods act on individual celestial objects, while static methods encompass universal constants or operations affecting multiple bodies within a simulation.

For instance, calculating light absorption across vast interstellar spaces might involve static methods applicable universe-wide rather than individual star instances.

Balancing simulations and data analysis with an understanding of object-oriented programming in Java advances our grasp of the cosmos and its vast complexities.