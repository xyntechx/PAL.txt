# Defining and Using Classes

In this chapter, we explore the concept of defining and using classes in Java, focusing on both static and non-static methods. The chapter starts with an explanation of static methods, illustrated through the creation of a simple Java class, `Charge`. This highlights that Java code must be part of a class, and emphasizes the role of a `main` method for executing the class. We then delve into instance variables and object instantiation with the `Particle` class, demonstrating how instances of classes can hold data and how to leverage instance methods. The analogy of electrostatics helps in understanding these concepts, with examples that mimic real-world interactions, such as charged particles attracting or repelling each other.

Furthermore, the chapter elaborates on the use of constructors, arrays, and static members in Java, paralleling them with abstract concepts in electrostatics like electric fields and potentials. It illustrates the use of constructors to initialize objects and provides examples of creating arrays of objects, which is crucial for handling collections of similar entities like charged particles in electromagnetics simulations. This chapter aids in building a strong foundational understanding of essential object-oriented programming concepts in Java that are crucial for managing complex systems, akin to simulating physical phenomena in electrostatics.

2. Defining and Using Classes

If you do not have prior Java experience, we recommend that you work through the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before reading this chapter. It will cover various syntax issues that we will not discuss in the book.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

All code in Java must be part of a class (or something similar to a class, which we'll learn about later). Most code is written inside of methods. Let's consider an example using a concept from electrostatics:

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

The `Charge` class we've defined doesn't do anything on its own—it’s like a charged particle defined with potential action, but with no context or other particles to interact with. To actually run the class, we'd either need to add a main method to the `Charge` class, as we saw in chapter 1.1. Or we could create a separate [`ChargeLauncher`](https://www.youtube.com/watch?v=Q-LE-jJQLTM) class that runs methods from the `Charge` class. For example, consider the program below:

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

A class that uses another class is sometimes called a "client" of that class, i.e., `ChargeLauncher` is a client of `Charge`. Neither of the two techniques is better: Adding a main method to `Charge` may be better in some situations—like attaching a charge to a circuit—while creating a client class like `ChargeLauncher` may be better in others—similar to having a separate instrument to measure the effect of a charge. The relative advantages of each approach will become clearer as we gain additional practice throughout the course.

When explaining potential analogies, ensure that they remain simple and connected directly to the programming concepts without introducing complex electrostatics details that might overshadow the CS content itself. In real electrostatics, charges are not integers but floats or doubles, reflecting their precision. Similarly, use realistic and straightforward scenarios to symbolize Java concepts without over-extending these representations.

**Instance Variables and Object Instantiation through Electrostatic Analogy**

In electrostatics, not all particles are alike; some carry charges that either attract or repel depending on their type. This is reminiscent of programming, where objects can have unique properties and behaviors. Understanding this analogy, Java's syntax was crafted to mimic interactions akin to electrostatics, allowing us to model these real-world phenomena.

One way to represent different charged particles would be to create a unique class for each type of particle. Consider the following code:

```java
public class Proton {
    public void interact() {
        System.out.println("repel protons, attract electrons");
    }
}

public class Electron {
    public void interact() {
        System.out.println("attract protons, repel electrons");
    }
}
```

In programming, much like in electrostatics, the creation of instances is central. An instance of a class in programming can hold unique data, similar to how particles have distinct charges. To effectively represent particles, we use instances of a `Particle` class and define their behavior based on their properties. Here's how that might look:

```java
public class Particle {
    private double chargeInCoulombs;

    public Particle(double charge) {
        this.chargeInCoulombs = charge;
    }

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

To see the `Particle` class in action, consider the following usage example:

```java
public class ParticleLauncher {
    public static void main(String[] args) {
        Particle p = new Particle(1.0);
        p.interact();
    }
}
```

When executed, this program creates a `Particle` with a positive charge, which will describe its behavior: "repel similar charges, attract opposite."

Key observations and terminology include:

* An `Object` in Java acts like a physical particle, representing an instance of any class.
* Our `Particle` class contains variables known as _instance variables_, such as `chargeInCoulombs`, analogous to defining charges in electrostatics.
* The method within the `Particle` class is an _instance method_ omitted of the `static` keyword, akin to charge-specific interactions.
* Creation of a specific `Particle` instance requires instantiation, using the `new` keyword. We observe how calling `p.interact()` pertains only to a particular `Particle` object and not to the `Particle` class as a whole.
* Instantiated objects are _assigned_ to variables of a particular type, for example, `p = new Particle(1.0);` which aligns with physics concepts where specific properties are assigned to particles.
* The terms _members_ of a class refer to both variables and methods, accessed through _dot notation_, resonating with how properties of particles influence their range of interactions in physical theory.

Through this analogy, Java programming can mirror complex interactions such as those found in electrostatics, enhancing our understanding of both coding and natural phenomena.

**Constructors in Electrostatic Simulations**

In computational electromagnetics, similar to object-oriented programming, constructors are used to initialize objects with desired attributes. This method is reflective of how we might initiate a simulation with charged particles:

```java
public class ElectrostaticsSimulationLauncher {
    public static void main(String[] args) {
        ChargedParticle p = new ChargedParticle(1.6e-19);
        p.displayCharge();
    }
}
```

Here, the constructor is designed to conveniently assign values to charge-related properties, automating the initialization process. Consider the `ChargedParticle` class, where the initialization method is crafted as follows:

```java
public class ChargedParticle {
    private double chargeInCoulombs;

    public ChargedParticle(double q) {
        chargeInCoulombs = q;
    }

    public void displayCharge() {
        System.out.println("Charge: " + chargeInCoulombs + " C");
    }
}
```

Notice that `chargeInCoulombs` is a double, reflecting realistic charge values. The constructor `public ChargedParticle(double q)` is invoked each time a `ChargedParticle` is instantiated with the `new` keyword, mimicking Python’s `__init__` method behavior.

**Terminology Summary**

**Array Instantiation, Arrays of Charges**

In electrostatics simulations, we often manage multiple particles, necessitating arrays. Java’s array instantiation techniques are used to craft arrays of charges, as demonstrated:

```java
public class ChargeArrayDemo {
    public static void main(String[] args) {
        /* Create an array representing various charges. */
        double[] chargeArray = {1.6e-19, 3.2e-19};
    }
}
```

Similarly, arrays can hold instantiated charged particles:

```java
public class ChargedParticleArrayDemo {
    public static void main(String[] args) {
        /* Create an array of charged particles. */
        ChargedParticle[] particles = new ChargedParticle[2];
        particles[0] = new ChargedParticle(1.6e-19);
        particles[1] = new ChargedParticle(3.2e-19);

        /* Display the charge of the first particle to the console. */
        particles[0].displayCharge();
    }
}
```

Here, `new` is first used to allocate an array for `ChargedParticle` objects and subsequently to instantiate each one. This methodology resembles how one might organize charged entities in an electric field, each with distinct magnitudes, situated within a computational framework. By maintaining this balance, the understanding of Java constructs remains clear, supported by the electrostatics context rather than overshadowed by it.

#### Electric Fields vs. Electric Potentials <a href="#electric-fields-vs-electric-potentials" id="electric-fields-vs-electric-potentials"></a>

In electrostatics, two fundamental concepts are often discussed:

* Electric fields, which are vector fields.
* Electric potentials, which are scalar fields.

The electric potential at a location in space represents the potential energy per unit charge, while an electric field represents the force per unit charge exerted on a charge at that point. Both concepts are pivotal in different analytical circumstances. For instance, a parallel plate capacitor provides a potential difference. Using this static field, we can determine the force on a charge located between the plates using:

```plaintext
F = q * (V / d);
```

Where `F` is the force experienced by the charge, `q` is the charge magnitude, `V` is the potential difference, and `d` is the distance between the plates. Alternatively, if we use the concept of electric fields, the force can be directly calculated as:

```plaintext
electric_field E = charge_density / permittivity;
F = q * E;
```

Utilizing both electric fields and potentials might sometimes be beneficial. For example, if tasked with calculating the force on a charge using both a known field and potential difference, it can be efficient to employ methods that leverage these properties.

```plaintext
public static double computeForceFromPotential(double q, double V, double d) {
    return q * (V / d);
}
```

This method might be used as follows:

```plaintext
double q = 1.5;
double V = 10.0;
double d = 0.5;
double F = computeForceFromPotential(q, V, d);
```

In this example, the potential approach is highlighted using a descriptive method name.

Conversely, to compute force utilizing an electric field directly, one might implement:

```plaintext
public double computeForceFromField(double q, double E) {
    return q * E;
}
```

This method can be invoked in a scenario like:

```plaintext
double q = 1.5;
double E = 20.0;
double F = computeForceFromField(q, E);
```

This illustrates computing force directly from an electric field rather than a potential difference.

**Exercise 1.2.1:** Consider the outcome of the following method. If unclear, test it practically:

```plaintext
public static double computeForceFromPotentialDifference(double q, double V, double d) {
    return q * (V / d);
}
```

**Static Charge Configurations**

In certain analyses, defining static configurations of charges becomes vital. These configurations underscore the inherent attributes of a system above individual charge behaviors. For example, one may document the typical field strength of a charged plane as `E0`:

```plaintext
public class ChargedPlane {
    public double surfaceChargeDensity;
    public static double characteristicFieldStrength = E0;
    // Additional members...
}
```

Static charge properties should be accessed using the class name rather than an instance name, enhancing clarity. For example, prefer `ChargedPlane.characteristicFieldStrength` over `plane.characteristicFieldStrength`.

While technically permissible, accessing static properties via an instance can be misleading and is considered suboptimal coding practice.

**Exercise 1.2.2:** Complete the following exercise:

* Video: [link](https://youtu.be/6JdBLpnVj0c)
* Slide: [link](https://docs.google.com/presentation/d/dQW8oYfAGzQwTdfg7vhlHXmlYwzvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

This completes our exploration of the interplay between electric fields and potentials and their analogous application within object-oriented programming concepts.

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

With what we've learned so far, it's time to demystify the declaration we've been using for the main method. Let's break it down into smaller parts:

* `public`: This keyword signifies that the method can be accessed from outside its class, much like how external forces can influence a charged particle.
* `static`: This designates the method as not tied to any particular instance of a class. Like an electric field that exists throughout space independent of a single charge, the `static` method belongs to the class itself rather than any object.
* `void`: This term indicates the method does not return a value. Similar to how electric field lines may extend without a termination point, this method concludes without returning data.
* `main`: This is the designated name for the method that serves as the entry point of any Java application, comparable to a source charge that initiates an electric field.
* `String[] args`: These are parameters passed to the command line, akin to diverse forces that can influence a test charge within an electric field, offering flexible input to initiate a program's starting conditions.

**Command Line Arguments**

Since `main` is invoked by the Java interpreter instead of any other Java class, the interpreter inputs these arguments as command line parameters. They can be considered inputs like those influencing an electric field. Here's a basic illustration with `ArgsDemo`, representing the introduction of a test charge into a field:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program will print the first command line argument input, for example:

```
$ java ArgsDemo these are command line arguments
these
```

In this case, `args` is an array of Strings, similar to an array representing multiple charges within a field. Elements could be {"these", "are", "command", "line", "arguments"}, representing varied charges or fields impacting a central point.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Write a program that calculates the sum of command line arguments, assuming they represent numeric values. This is like summing vectors of force on various charges to determine the resultant effect. You can find a solution in the webcast or the provided code on GitHub, offering clarity much in the way physical principles provide insight into complex systems.

#### Utilizing Electrostatic Principles <a href="#utilizing-electrostatic-principles" id="utilizing-electrostatic-principles"></a>

Understanding how to apply existing electrostatic principles is crucial for any physicist or electronics engineer working with charged systems and fields. In the realm of computer science, electrostatic analogies can elucidate complex concepts related to object interactions and method functionality.

Electrostatics provides a rich set of metaphors that can aid in conceptualizing interactions in object-oriented programming, particularly in languages such as Java. To effectively leverage these analogies, consider the following guidelines:

* Ensure that the electrostatic principles utilized are easily relatable to the computing concepts being explained. For instance, while Coulomb's Law illustrates point charge interactions, it can serve as a metaphor for object interaction in software.
* Utilize analogies that maintain precision and relevance, avoiding overly complex electrostatic scenarios that may confuse rather than clarify.
* Balance the use of electrostatic metaphors with core explanations of programming concepts to prevent overshadowing the primary subject matter.

For example, using 'Coulomb's law for point charge interactions' as an analogy, we can discuss how objects in a program can exert influence over each other through method calls. However, attempting to find a "detailed solution to a complex electrostatic situation" may not directly translate and could detract from the understanding of the Java concept.

For additional insights into the role of analogies in programming instruction and maintaining academic integrity, refer to the research ethics section of our guidelines.