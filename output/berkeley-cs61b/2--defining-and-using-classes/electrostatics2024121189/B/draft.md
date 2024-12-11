# Defining and Using Classes

In this chapter, we explore the concept of defining and using classes in Java, focusing on both static and non-static methods. The chapter starts with an explanation of static methods, illustrated through the creation of a simple Java class, `Charge`. This highlights that Java code must be part of a class, and emphasizes the role of a `main` method for executing the class. We then delve into instance variables and object instantiation with the `Particle` class, demonstrating how instances of classes can hold data and how to leverage instance methods. The analogy of electrostatics helps in understanding these concepts, with examples that mimic real-world interactions, such as charged particles attracting or repelling each other.

Furthermore, the chapter elaborates on the use of constructors, arrays, and static members in Java, paralleling them with abstract concepts in electrostatics like electric fields and potentials. It illustrates the use of constructors to initialize objects and provides examples of creating arrays of objects, which is crucial for handling collections of similar entities like charged particles in electromagnetics simulations. This chapter aids in building a strong foundational understanding of essential object-oriented programming concepts in Java that are crucial for managing complex systems, akin to simulating physical phenomena in electrostatics.

2. Defining and Using Classes

If you do not have prior Java experience, we recommend that you work through the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before reading this chapter. It will cover various syntax issues that we will not discuss in the book.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

All code in Java must be part of a class (or something similar to a class, which we'll learn about later). Most code is written inside of methods. Let's consider an example:

```java
public class Charge {
    public static void exertForce() {
        System.out.println("Attract or Repel!");
    }
}
```

If we try running the `Charge` class, we'll simply get an error message:

```
$ java Charge
Error: Main method not found in class Charge, please define the main method as:
       public static void main(String[] args)
```

The `Charge` class we've defined doesn't do anything. We've simply defined something that `Charge` **can** do, namely exert a force. To actually run the class, we'd either need to add a main method to the `Charge` class, as we saw in chapter 1.1. Or we could create a separate [`ChargeLauncher`](https://www.youtube.com/watch?v=Q-LE-jJQLTM) class that runs methods from the `Charge` class. For example, consider the program below:

```java
public class ChargeLauncher {
    public static void main(String[] args) {
        Charge.exertForce();
    }
}
```

```
$ java ChargeLauncher
Attract or Repel!
```

A class that uses another class is sometimes called a "client" of that class, i.e. `ChargeLauncher` is a client of `Charge`. Neither of the two techniques is better: Adding a main method to `Charge` may be better in some situations, and creating a client class like `ChargeLauncher` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout the course.

**Instance Variables and Object Instantiation through Electrostatic Analogy**

Not all particles are alike. Some particles carry a charge that attracts, while others repel with a force inversely proportional to the square of the distance between them. Often, we write programs to mimic features of the universe we inhabit, and Java's syntax was crafted to easily allow such mimicry, just as electrostatic forces can mimicationally illustrate the interactions between particles.

One approach to allowing us to represent the spectrum of charged particles would be to create separate classes for each type of Particle.

```java
public class Proton {
    public static void interact() {
        System.out.println("repel protons, attract electrons");
    }
}

public class Electron {
    public static void interact() {
        System.out.println("attract protons, repel electrons");
    }
}
```

As you should have seen in the past, classes can be instantiated, and instances can hold data analogous to charges. This leads to a more natural approach, where we create instances of the `Particle` class and make the behavior of the `Particle` methods contingent upon the properties of the specific `Particle`. To make this more concrete, consider the class below:

```java
public class Particle {
    public int chargeInCoulombs;

    public void interact() {
        if (chargeInCoulombs > 0) {
            System.out.println("repel similar charges, attract opposite");
        } else if (chargeInCoulombs < 0) {
            System.out.println("attract positive charges, repel similar");
        } else {
            System.out.println("no interaction");
        }
    }    
}
```

As an example of using such a Particle, consider:

```java
public class ParticleLauncher {
    public static void main(String[] args) {
        Particle p;
        p = new Particle();
        p.chargeInCoulombs = 1;
        p.interact();
    }
}
```

When run, this program will create a `Particle` with a unit positive charge, and that `Particle` will soon describe its interactions: "repel similar charges, attract opposite."

Some key observations and terminology:

* An `Object` in Java is an instance of any class, analogous to a fundamental particle in electrostatics.
* The `Particle` class has its own variables, also known as _instance variables_ or _charge properties_. These must be declared inside the class, similar to how charge properties must be known to determine electrostatic interactions in physics.
* The method that we created in the `Particle` class did not have the `static` keyword. We call such methods _instance methods_ or _variable charge methods_.
* To call the `interact` method, we had to first _instantiate_ a `Particle` using the `new` keyword, and then make a specific `Particle` interact. In other words, we called `p.interact()` instead of `Particle.interact()`.
* Once an object has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `p = new Particle();`
* Variables and methods of a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_, just as charges influence fields in physics through specific properties and interactions.

**Constructors in Electrostatic Simulations**

In computational electromagnetics, similar to object oriented languages, we often construct objects using initialization processes that resemble a _constructor_. Consider how we might set up a simulation involving charged particles:

```java
public class ElectrostaticsSimulationLauncher {
    public static void main(String[] args) {
        ChargedParticle p = new ChargedParticle(1.6e-19);
        p.displayCharge();
    }
}
```

In this scenario, the initialization is parameterized, allowing us to conveniently assign values to various charge-related properties without manually setting each one. To enable such efficient syntax, we add an "initialization method" to our ChargedParticle class as shown:

```java
public class ChargedParticle {
    public double chargeInCoulombs;

    public ChargedParticle(double q) {
        chargeInCoulombs = q;
    }

    public void displayCharge() {
        System.out.println("Charge: " + chargeInCoulombs + " C");
    }
}
```

The constructor with signature `public ChargedParticle(double q)` will be invoked whenever we want to initialize a `ChargedParticle` with a specific charge value using the `new` keyword. For those of you coming from Python, this process is akin to the initialization done in `__init__` methods.

**Terminology Summary**

**Array Instantiation, Arrays of Charges**

As demonstrated in electrostatics simulations, particle arrays are often initialized using processes similar to Java's new keyword instantiation techniques. Consider:

```java
public class ChargeArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five charges. */
        double[] chargeArray = new double[5];
        chargeArray[0] = 1.6e-19;
        chargeArray[1] = 3.2e-19;
    }
}
```

Similarly, we can create arrays of instantiated charged particles:

```java
public class ChargedParticleArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two charged particles. */
        ChargedParticle[] particles = new ChargedParticle[2];
        particles[0] = new ChargedParticle(1.6e-19);
        particles[1] = new ChargedParticle(3.2e-19);

        /* Charge display will result, showcasing the charge of particles[0]. */
        particles[0].displayCharge();
    }
}
```

Observe that new is employed in two distinct contexts: initially to craft an array capable of holding two `ChargedParticle` objects, followed by its use to create each individual `ChargedParticle`. This mirrors how electric field calculations might manage arrays of charges each initialized with different magnitudes and placed in a simulated field.

#### Electric Fields vs. Electric Potentials <a href="#electric-fields-vs-electric-potentials" id="electric-fields-vs-electric-potentials"></a>

Electrostatics allows us to define two types of concepts:

* Electric fields, a.k.a. vector fields.
* Electric potentials, a.k.a. scalar fields.

Electric potentials represent the potential energy per unit charge at a location in space. Electric fields represent the force per unit charge exerted on a charge at a point in space.  Both are useful in different circumstances. As an example of using a potential, a parallel plate capacitor provides a potential difference. Because it is a static field, we can calculate the force on a charge between the plates as follows:

```plaintext
F = q * (V / d);
```

Where `F` is the force, `q` is the charge, `V` is the potential difference, and `d` is the distance between the plates. If we had used electric fields directly, we would directly calculate the force using this theoretical definition.

```plaintext
electric_field E = charge / permittivity;
F = q * E;
```

Sometimes, it makes sense to use both electric fields and potentials. For example, suppose we want the ability to calculate the force on a charge from both a known field and potential difference. One way to do this is to add a method to compute the force from the potential.

```plaintext
public static double computeForceFromPotential(double q, double V, double d) {
    return q * (V / d);
}
```

This calculation can be invoked by, for example:

```plaintext
double q = 1.5;
double V = 10.0;
double d = 0.5;
double F = computeForceFromPotential(q, V, d);
```

Observe that we've invoked using the method name, since this calculation uses electric potentials.

We could also implement a method to calculate force using electric fields, e.g.

```plaintext
public double computeForceFromField(double q, double E) {
    return q * E;
}
```

Above, we quantify the force directly from the electric field. This calculation could be invoked, for example, with:

```plaintext
double q = 1.5;
double E = 20.0;
double F = computeForceFromField(q, E);
```

Here, we utilize a specific electric field to compute the force on a charge.

**Exercise 1.2.1**: What would the following calculation do? If you're not sure, try it out.

```plaintext
public static double computeForceFromPotentialDifference(double q, double V, double d) {
    return this.q * (V / d);
}
```

**Static Charge Configurations**

It is occasionally useful to define static configurations of charges. These configurations represent the inherent properties of a system, rather than individual charges. For example, we might record that the characteristic field strength of a certain charged plane is `E0`:

```plaintext
public class ChargedPlane {
    public double surfaceChargeDensity;
    public static double characteristicFieldStrength = E0;
    ...
}
```

Static charge properties should be accessed using the name of the structure rather than a specific instance, e.g. you should use `ChargedPlane.characteristicFieldStrength`, not `plane.characteristicFieldStrength`.

While technically one could access a static property using an instance identifier, it is poor practice, confusing, and an oversight by textbook authors if not avoided.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/6JdBLpnVj0c)
* Slide: [link](https://docs.google.com/presentation/d/dQW8oYfAGzQwTdfg7vhlHXmlYwzvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe\_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

With what we've learned so far, it's time to demystify the declaration we've been using for the main method. Breaking it into pieces, we have:

* `public`: So far, all of our methods start with this keyword.
* `static`: It is a static method, not associated with any particular instance, similar to how an electric field permeates space and does not belong to any single charge.
* `void`: It has no return type, just like how electric field lines can extend infinitely without returning.
* `main`: This is the name of the method, analogous to a source charge that generates an electrostatic field.
* `String[] args`: This is a parameter that is passed to the main method, akin to the forces that act on test charges placed within an electric field.

**Command Line Arguments**

Since main is called by the Java interpreter itself rather than another Java class, it is the interpreter's job to supply these arguments. They refer usually to the command line arguments. For instance, consider the program `ArgsDemo` below, which is like releasing a test charge at a point within a field to see the effects or forces exerted by the field:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program prints out the 0th command line argument, e.g.

```
$ java ArgsDemo these are command line arguments
these
```

In the example above, `args` will be an array of Strings, where the entries are {"these", "are", "command", "line", "arguments"}, just as an array of forces or potential differences acting on different test charges placed throughout the electric field.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Try to write a program that sums up the command line arguments, assuming they are numbers. For a solution, see the webcast or the code provided on GitHub, much like summing the forces acting on a collection of test charges to find total influence or effect at a particular point in an electric field.

#### Utilizing Electrostatic Principles <a href="#utilizing-electrostatic-principles" id="utilizing-electrostatic-principles"></a>

Understanding how to apply existing electrostatic principles is crucial for any physicist or electronics engineer working with charged systems and fields. In the dynamic world of electrostatics, leveraging established theories and equations can significantly reduce the complexity of calculations and potential errors.

In this field, it is encouraged to harness these principles, keeping in mind the following guidelines:

* Only employ concepts and theories that are well-documented and peer-reviewed.
* Acknowledge your references.
* Avoid looking for exact solutions to specific research or laboratory problems.

For example, it's valid to refer to "Coulomb's law for point charge interactions". However, it would be inappropriate to search for "Detailed solution to Lab Experiment 101 on Electric Field Mapping at MIT".

For further information on collaboration and integrity in research, refer to the research ethics section of our guidelines.