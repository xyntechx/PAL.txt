

# 2. Defining and Using Classes in Astrophysics Simulations

If you do not have prior Java experience, we recommend that you work through the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before reading this chapter. It will cover various syntax issues that we will not discuss in the book.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

All code in Java must be part of a class. Java classes can be utilized to model various astronomical phenomena. Most code is written inside of methods. Let's consider an example to simulate a simple phenomenon:

```java
public class Star {
    public static void emitLight() {
        System.out.println("Twinkle, twinkle!");
    }
}
```

If we try running the `Star` class directly, we'll simply get an error message:

```
$ java Star
Error: Main method not found in class Star, please define the main method as:
       public static void main(String[] args)
```

The `Star` class we've defined only describes what a Star **can** do — namely emit light. To actually simulate this, we'll use a client class to call the method:

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

The `StarSimulator` class acts as a client to the `Star` class. This concept parallels real astrophysical research, where simulations are run on models to predict behaviors. Adding a main method in `Star` or using a separate class as a client depends on the clarity and requirements of the simulation at hand.

**Instance Variables and Object Instantiation**

Not all stars are alike; their brightness, size, and temperature vary greatly. Our goal in simulation is to reflect such variation, allowing us to represent these differences dynamically through instances.

For example, we might define a `Star` class with properties to store its luminosity, size, and temperature:

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

We instantiate and use this class to create a specific `Star` object representing an actual star's features:

```java
public class StarSimulator {
    public static void main(String[] args) {
        Star sun = new Star();
        sun.size = 1;
        sun.categorizeStar();
    }
}
```

When this program is run, the `Star` object `sun` will be categorized as a "Main Sequence Star". This ability to instantiate specific stars with distinct characteristics is akin to the modeling done in investigations of celestial objects.

Some key observations and terminology:

* An `Object` in Java represents an instance of any class.
* The `Star` class has its own variables, known as _instance variables_ or _non-static variables_. These reflect the physical properties stored for each star.
* We can call the `categorizeStar` method only for instantiated stars, i.e., individual star objects created in the simulation, using `sun.categorizeStar()`.
* Using the `new` keyword, each star can be instantiated and defined with specific attributes mimicking real-world stars.

**Constructors in Java for Astrophysics Simulation**

In astrophysical simulations, constructors can efficiently set initial conditions for stars and other entities:

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

By utilizing constructors, we can initialize new stars with properties specific to the simulation's requirements, allowing each star to exhibit behaviors based on its defined properties.

**Array Instantiation of Celestial Bodies**

Simulations often require managing multiple objects, such as arrays of stars or planets.

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

This effectively maps the stars' array to multiple scientific scenarios, reflective of real astrophysical study collections, even portraying entire galaxies or star systems.

#### Class Methods vs. Instance Methods in Cosmic Contexts <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java enables us to model both global cosmic phenomena and specific celestial occurrences through class and instance methods. Instance methods act on specific celestial objects, while static methods can define cosmic constants or operations impacting multiple bodies in a simulation.

For example, calculating cosmic darkness across a distance between stars may involve such static methods for universal applicability rather than per-instance invocation.

Whether crafting simulations or analyzing astronomical data, understanding and effectively using object-oriented paradigms in Java supports advancing our comprehension of the universe.