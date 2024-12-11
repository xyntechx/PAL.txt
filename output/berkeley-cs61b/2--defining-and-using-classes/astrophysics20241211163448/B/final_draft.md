# Programming with Classes and Methods

This chapter explores foundational concepts in Java programming, focusing on static versus non-static methods, object instantiation, constructors, and the role of the `main` method. It begins by differentiating between static methods, which are common operations associated with a class itself, and instance methods, which pertain to specific instances of a class, using the example of a `Star` class in Java. Static methods, demonstrated through a class method `emitLight`, are contrasted with the use of instance methods through instance variables that allow objects such as stars to exhibit diverse behaviors based on parameters like mass. This setup highlights the advantage of using object-oriented programming to represent complex entities such as celestial bodies in a more natural, simulation-friendly way.

The discussion extends to managing collections of objects through arrays in Java, emphasizing proper use of dot notation and the `new` keyword for object and array creation. The chapter also covers class versus instance methods further, illustrated by comparing galaxies' methods to calculate luminosity. Additionally, it introduces static variables, which are class-wide properties, and reviews the structure of the `main` method, serving as the entry point for running Java programs. Various exercises are embedded to consolidate understanding of concepts such as method design and practical use of command-line arguments, situating these programming techniques within the cosmic context of astrophysics simulations.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

All computational code related to simulating the motion of celestial bodies needs to belong to a class structure—this mirrors celestial mechanics where celestial bodies adhere to universal laws. In Java, most calculations occur within these methods that can either be static or non-static. Here's a straightforward illustration:

```java
public class Star {
    public static void emitLight() {
        System.out.println("Shine!");
    }
}
```

Observe that running the `Star` class independently would result in an error message:

```
$ java Star
Error: Main method not found in class Star, please define the main method as:
       public static void main(String[] args)
```

This happens because the `Star` class, akin to how stars reach their potential energy balance before shining, defines a capability without enacting it. To execute the class and let it "shine," we must introduce a main method within `Star` or create an auxiliary `StarSimulator` class to deploy methods from `Star`. For instance:

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

The `StarSimulator` acts as a "client" of the `Star` class—just as space telescopes serve as observational clients to monitor stars. Each technique has its merits: incorporating a main method directly within `Star` may enhance cohesive design in straightforward projects, whereas utilizing a client class like `StarSimulator` separates concerns and fosters a modular approach, critical when scaling up projects such as cosmic simulations. The advantages of each tactic will become clearer through further exploration as we proceed through this interdisciplinary course.

**Instance Variables and Object Instantiation in Astrophysics**

The universe is a vast sea of varied celestial wonders. Among these, stars captivate us with their diverse characteristics and behaviors, from the soft twinkle of some to the intense illumination of others. Harnessing programming languages like Java, we can simulate and explore these cosmic entities through code.

A naive approach to capturing the universe's stellar diversity is to define individual classes for each star type:

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

While this works, a more elegant and efficient method involves the use of instance variables to encapsulate the diverse features of stars within a single `Star` class. This enables the creation of distinct instances, each representing a different kind of star with unique properties:

```java
public class Star {
    private double massInSolarMasses; // instance variable to store mass
    
    public Star(double mass) { // constructor
        this.massInSolarMasses = mass;
    }

    public void shine() { // instance method
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

In practice, this class can be instantiated as follows:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star s = new Star(1.2);
        s.shine();
    }
}
```

Executing this program creates a `Star` instance with a mass of 1.2 solar masses, resulting in a "steady shimmer.".

Key observations and terminology include:

* An `Object` in Java is an instance of a class, like a specific star created from the `Star` class.
* Instance variables, such as `massInSolarMasses`, are declared within a class to store particular states of objects.
* Instance methods, unlike static methods, belong to an instance of a class and can operate on its instance variables, exemplified by the `shine` method.
* Objects are instantiated with the `new` keyword and usually involve constructors to set initial states, as seen with `new Star(1.2)`.
* Class members, encompassing both variables and methods, are accessed through dot notation (e.g., `s.shine()`).

This approach efficiently mirrors the way astronomers study a diverse array of stars using a unified framework, employing variables to capture and simulate their unique characteristics.

**Constructors in Java**

Navigating the universe of Java programming, akin to astrophysicists who model the vastness of celestial phenomena, object-oriented languages typically create objects using a construct known as a _constructor_:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star sirius = new Star(1.02);
        sirius.shine();
    }
}
```

This example demonstrates parameterized instantiation, saving us vast amounts of manual labor, similar to crossing interstellar distances efficiently, and bypassing the messiness of numerous instance variable assignments. To enable such graceful instantiation, a "constructor" must be added to our Star class, much like developing a theoretical model of a star system:

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

The constructor with the form `public Star(double mass)` is invoked each time we initiate a `Star` using the `new` keyword accompanied by a floating-point parameter. For those familiar with Python, think of this constructor as resembling the `__init__` method, responsible for the primary setup of cosmic object properties.

**Terminology Summary**

**Array Instantiation, Arrays of Objects**

As introduced in earlier sessions equivalent to preliminary studies, arrays are also initiated in Java through the new keyword. Consider this example, comparable to assembling a small stellar cluster:

```java
public class GalaxyDemo {
    public static void main(String[] args) {
        /* Assemble an array representing a quintet of planetary mass objects. */
        double[] someMasses = new double[5];
        someMasses[0] = 0.3;
        someMasses[1] = 0.4;
    }
}
```

We can extend this concept to create arrays consisting of instantiated celestial objects, such as:

```java
public class StarClusterDemo {
    public static void main(String[] args) {
        /* Formulate an array of stars in a binary system. */
        Star[] binaryStars = new Star[2];
        binaryStars[0] = new Star(0.8);
        binaryStars[1] = new Star(1.02);

        /* Expect a steady glow, as binaryStars[0] exhibits a mass of 0.8. */
        binaryStars[0].shine();
    }
}
```

Notice that `new` functions in two distinct roles: once for constructing an array to "contain" (or figuratively "map") two `Star` entities, and additionally for crafting each singular `Star`, analogous to crafting a constellation with disparate stars.

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java allows us to define two types of methods:

* Class methods, a.k.a. static methods.
* Instance methods, a.k.a. non-static methods.

Instance methods are actions that can be carried out only by a specific instance of a class. They often work with the object's instance variables. Static methods, on the other hand, are actions that are taken by the class itself. They cannot access instance variables but can access static variables of the class. Choosing between static and instance methods depends on the use-case.

Consider the `Universe` class, which includes a static method to calculate the luminosity of a star. We can conveniently invoke this method using the class name as follows:

```java
luminosity = Universe.calculateLuminosity(starMass);
```

If `calculateLuminosity` were designed as an instance method, it would require creating an instance of `Universe`, which is unnecessary in this context:

```java
Universe u = new Universe();
luminosity = u.calculateLuminosity(starMass);
```

In some scenarios, it is beneficial for a class to have both instance and static methods. For example, to compare two galaxies based on their mass, we might include a static method in the `Galaxy` class:

```java
public static Galaxy largerGalaxy(Galaxy g1, Galaxy g2) {
    return (g1.mass > g2.mass) ? g1 : g2;
}
```

This static method is called using the class name, as shown:

```java
Galaxy g1 = new Galaxy(1.5E12);
Galaxy g2 = new Galaxy(1E12);
Galaxy.largerGalaxy(g1, g2);
```

Alternatively, if `largerGalaxy` were an instance method, it would be invoked using a specific instance:

```java
public Galaxy largerGalaxy(Galaxy g2) {
    return (this.mass > g2.mass) ? this : g2;
}
```

Here’s how you would call this non-static method:

```java
Galaxy g1 = new Galaxy(1.5E12);
Galaxy g2 = new Galaxy(1E12);
g1.largerGalaxy(g2);
```

**Exercise 1.2.1**: Determine what would happen with the following erroneous method definition:

```java
public static Galaxy largerGalaxy(Galaxy g1, Galaxy g2) {
    if (mass > g2.mass) {
        return this;
    }
    return g2;
}
```

**Static Variables**

Static variables represent data common to all instances of a class, as opposed to instance variables unique to each object. Consider the following attribute in the `Galaxy` class:

```java
public class Galaxy {
    public double mass;
    public static String modelType = "Milky Way based models";
    ...
}
```

Static variables should be accessed using the class name, emphasizing their global nature, e.g., `Galaxy.modelType`. Accessing a static variable via an instance, like `g1.modelType`, is considered poor coding practice and can cause confusion.

**Exercise 1.2.2**: Address the following exercise to solidify your understanding:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

Venturing beyond Earth, it’s essential to understand how space missions and simulations initiate their operations. Similar to powering up spacecraft systems, let's dissect the main method declaration which commences a Java program:

* `public`: This indicates the method is accessible globally, comparable to a signal broadcast reaching distant galaxies.
* `static`: The method operates independently of any specific instance, akin to physics laws constant throughout the universe.
* `void`: Signifies no data returns after execution, much like a probe sending one-way signals to Earth.
* `main`: The standardized name for this starting procedure, akin to the main thruster activating a spacecraft's journey.
* `String[] args`: Command line inputs to the main method, similar to data relayed from interstellar probes.

**Interstellar Data Inputs**

Engaging the main method resembles mission control issuing commands or researchers providing initial data for a space simulation. These inputs are analogous to command line arguments. Explore the following program `AstroArgsDemo`:

```java
public class AstroArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program outputs the first command line argument, much like processing the first set of telemetry data:

```
$ java AstroArgsDemo Mercury Venus Earth
Mercury
```

Here, `args` can be visualized as an array of stellar names or data points such as {"Mercury", "Venus", "Earth"}.

**Calculating Celestial Distances**

**Exercise 1.2.3**: Write a program that calculates the sum of command line arguments, interpreted as distances between celestial bodies in astronomical units (AU). For solutions, refer to your simulation resources or observatory data archives.

#### Utilizing Research Papers <a href="#utilizing-research-papers" id="utilizing-research-papers"></a>

Astrophysicists must master the skill of efficiently finding and utilizing existing research papers. In this technologically advanced era, these documents can be invaluable for saving time and enhancing your data analyses.

In this field, you are encouraged to rely on research papers, provided you adhere to some critical guidelines:

* **Verify Peer-Review:** Always ensure that the research papers you consult are peer-reviewed. This guarantees that the findings are scrutinized by experts, ensuring their validity.
* **Proper Citation:** Always ensure to reference your sources accurately to uphold academic integrity and enable others to trace back the origins of the information you used.
* **Avoid Over-Specificity:** While it is beneficial to gather information on broad topics like “classifying exoplanet atmospheres using spectroscopy," searching for niche-specific solutions such as "Black Hole Event Horizon simulations from NASA" can limit your exploration and learning process.

For instance, it's advisable to seek out scholarly articles discussing methodologies for analyzing cosmic microwave background radiation, rather than looking for detailed data sets and simulations that effortlessly solve your research question.

For additional details regarding collaborative work and our integrity policies, please consult the course syllabus.