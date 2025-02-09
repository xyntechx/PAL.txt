# 2. Designing Classes with Cosmic Structures

If you are new to Java or the fascinating world of cosmic classes, consider reviewing the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) first. These exercises will unveil quirky syntax issues that will not be covered in this cosmic-themed chapter.

#### Static vs. Non-Static Methods in Cosmic Classes <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods in Cosmic Realms**

All code in Java, akin to the cosmic code lying in mysterious cosmic structures, must be part of a class or a cosmic object. Consider the celestial example below:

```java
public class Star {
    public static void shine() {
        System.out.println("Shining brightly!");
    }
}
```

If we attempt to run the `Star` class directly, we find nothing occurring except an error message from the universe:

```
$ java Star
Error: Main method not found in class Star, please define the main method as:
       public static void main(String[] args)
```

The `Star` class defined here predicates what `Star` **might** do—sparkle in the cosmic void. To execute this stellar class meaningfully, a main method must be equipped inside `Star`, or a celestial `StarLauncher` could be created to illuminate the method from `Star`. Consider this:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star.shine();
    }
}
```

```
$ java StarLauncher
Shining brightly!
```

Like cosmic bodies attracting each other, a class that uses another cosmic class is described as a "client" of that class, such as `StarLauncher` is for `Star`. Each approach of incorporating main methods is neither superior; the galactic advantages become apparent with practice.

Static and non-static methods are fundamental concepts in computer science, particularly within object-oriented programming, and they can be a useful analogy to understand certain astrophysical phenomena.

In programming, a **static method** belongs to the class itself rather than any specific instance of the class. This means that you can call a static method without creating an object of that class. Essentially, static methods are used for operations that are independent of the state (or specific attributes) of the object instance.

In astrophysics, you can relate this to universal laws or constants, like the gravitational constant (G), which applies consistently throughout the universe regardless of the state or location of a particular celestial body. Similarly, static methods operate universally for the class, independent of individual objects.

On the other hand, **non-static (or instance) methods** require the initiation of an object instance before they can be utilized. These methods can access and modify the instance variables of the object, meaning they are dependent on the object's specific state.

Imagine a non-static method as the unique set of characteristics or conditions affecting a particular star or planet, such as its mass, temperature, or luminosity. Just as each celestial body has its unique properties that determine its behavior and interactions, non-static methods depend on the instantiated object's specific attributes.

By understanding the difference between static and non-static methods, you can grasp how certain properties or actions are universally applicable versus those that are individualized, much like how astrophysicists separate universal laws from object-specific phenomena in their studies of the cosmos. This concept helps in building simulations or models both in software and when theorizing about the behaviors of celestial phenomena.

**Cosmic Constructors in Java**

Astute observers will know, in object-centric cosmic languages, we often build stellar objects utilizing a _constructor_:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star stellarObject = new Star(3);
        stellarObject.emitLight();
    }
}
```

The instantiation is remarkably cosmic, parameterized to prevent manual distractions of cosmic variable settings. Enable such cosmic syntax by adding a constructor to the cosmic `Star` class:

```java
public class Star {
    public double massInSolarMasses;

    public Star(double mass) {
        massInSolarMasses = mass;
    }

    public void emitLight() {
        if (massInSolarMasses < 0.5) {
            System.out.println("gentle glow");
        } else if (massInSolarMasses < 5) {
            System.out.println("standard light");
        } else {
            System.out.println("celestial blaze!");
        }    
    }
}
```

The cosmic constructor `public Star(double mass)` becomes a key to crafting a cosmic `Star` with the `new` keyword and a guiding mass parameter. For language travelers venturing from Python, this is akin to the `__init__` method.

**Cosmic Terminology Recap**

Imagine you're observing the lifecycle of a star. In astrophysics, we understand that stars form in nebulae and go through various stages such as a main-sequence star, red giant, etc. Each stage or type of star has its own properties, like mass, temperature, and luminosity, which help define the star at that particular phase of its life.

Similarly, in computer science, particularly when we talk about object-oriented programming in Java, a constructor is like the starting point or "birth" of an object, in this case, similar to the birth of a star. When you create a new object in Java, you're using a constructor to define the initial state of that object, setting its properties or attributes much like initial conditions in a nebula determine the future of a star.

For example, if you're simulating different types of celestial bodies in a Java program, you might have a class that represents a "Star." The constructor of this class would be what you use to set different properties such as mass, brightness, or temperature when you create a new instance of a Star. This ensures that every time you "form" a new Star object, it initializes with these specific attributes, much like how stars emerge with certain properties determined by their initial conditions.

Just as understanding the initial conditions of a star helps predict its lifecycle and characteristics, using constructors in Java helps define and predict how an object will behave throughout its lifecycle in your program. Constructors ensure that every object you create begins its life with a specific, known state, setting the stage for its subsequent behavior and interactions, much like the physical laws and initial conditions set the path for a star's evolution in the cosmos.

**Exercise 1.2.1 Cosmic Edition**: Predict the method output and verify if needed.

```java
public static Star largestStar(Star s1, Star s2) {
    if (massInSolarMasses > s2.massInSolarMasses) {
        return this;
    }
    return s2;
}
```

**Cosmic Static Variables**

In some cosmic scenarios, classes treasure static variables—their properties defining cosmic essence rather than a singular instance. For instance, remarking a star's galactic classification:

```java
public class Star {
    public double massInSolarMasses;
    public static String classification = "Main Sequence";
    ...
}
```

Static variables are accessed with cosmic class identifiers, for instance `Star.classification`, never `stellarObject.classification`.

Despite Java’s prowess allowing instance-time static access, it transgresses cosmic style and could betray cosmic clarity.

**Exercise 1.2.2 Cosmic Edition**: Engage in cosmic completion:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe\_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

Static variables in computer science can serve as an intriguing parallel to certain concepts in astrophysics, where understanding consistency and the state of a system over time is crucial.

In programming, static variables are attributes of a class or method that maintain their state even as the class or method executes multiple times. Unlike dynamic variables, which are reinitialized upon each activation of a method or each creation of an object, static variables persist throughout the execution of a program. This is akin to certain constants in astrophysics, like the gravitational constant, which remain unchanged regardless of the dynamic processes taking place in the universe.

Imagine you have a function in a computer program that simulates the orbital paths of planets around a star. Let's say this function also needs to track the total number of planets that have been initialized during the simulation. A static variable could be used here to maintain this count because, even as the function processes one planet at a time, we do not want this count to reset with each call.

Astrophysically, consider this similar to the concept of star systems in the Milky Way. While each star system varies in terms of planets and properties (similar to different function calls producing varied outputs), the number of stars or some universal properties like cosmic background radiation remain consistent and measurable on a larger, more static scale.

Thus, static variables are crucial for preserving the state in dynamically changing systems—a concept that has fascinating parallels in studying the relatively constant yet dynamic fabric of our universe.

# 2. Designing Classes with Cosmic Structures

If you are new to Java or the fascinating world of cosmic classes, consider reviewing the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) first. These exercises will unveil quirky syntax issues that will not be covered in this cosmic-themed chapter.

#### Static vs. Non-Static Methods in Cosmic Classes <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods in Cosmic Realms**

All code in Java, akin to the cosmic code lying in mysterious cosmic structures, must be part of a class or a cosmic object. Consider the celestial example below:

```java
public class Star {
    public static void shine() {
        System.out.println("Shining brightly!");
    }
}
```

If we attempt to run the `Star` class directly, we find nothing occurring except an error message from the universe:

```
$ java Star
Error: Main method not found in class Star, please define the main method as:
       public static void main(String[] args)
```

The `Star` class defined here predicates what `Star` **might** do—sparkle in the cosmic void. To execute this stellar class meaningfully, a main method must be equipped inside `Star`, or a celestial `StarLauncher` could be created to illuminate the method from `Star`. Consider this:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star.shine();
    }
}
```

```
$ java StarLauncher
Shining brightly!
```

Like cosmic bodies attracting each other, a class that uses another cosmic class is described as a "client" of that class, such as `StarLauncher` is for `Star`. Each approach of incorporating main methods is neither superior; the galactic advantages become apparent with practice.

Imagine we're trying to send data from a spacecraft back to Earth. The process requires a control center and a team to interpret the data. Similarly, in computer programming, especially in Java, we have a central point called `public static void main(String[] args)` which acts as the entry point for any Java application. This is where your program begins its operation, just like mission control begins organizing the data sent from space.

In astrophysics, data needs to be processed and analyzed in a systematic way. Likewise, when you run a Java application, `main` is required to start the execution. Let's break down what each part means:

- **public**: Just like astrophysics research, which often seeks to share findings with the scientific community, `public` means this method can be accessed anywhere the application is run. It's like making your findings available to the global scientific network.

- **static**: In astrophysics, some principles apply universally, regardless of the specific situation. Similarly, `static` means this method belongs to the class itself, not to any particular object. It's a universal entry point that doesn't require individual instances to utilize it.

- **void**: Just as some missions might not immediately return data or results, `void` indicates that this method doesn't return any data back to wherever it was called from.

- **main(String[] args)**: Think of this as receiving signals from multiple instruments on a spacecraft. `String[] args` is an array of strings, which allows the method to receive data - often configurations or parameters you might want to set before launching an analysis task, akin to receiving various setup instructions for the instruments.

In essence, the `public static void main(String[] args)` is where the program connects with the 'mission parameters' before embarking on its quest, much like data acquisition in a satellite mission, laying the groundwork for the full exploration and study into the cosmos or, in this case, a computer's reasoning task.

#### public static void main(String\[] args) in the Cosmic Domain <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

The cosmic method declaration `public static void main(String[] args)` now unravels its mystery:

* `public`: Universal access as understood across our cosmic classes.
* `static`: A cosmic class-method grander than individual instance.
* `void`: Lacking a cosmic result.
* `main`: The method's cosmic identifier.
* `String[] args`: A cosmic array bearing parameters sent to the cosmic method.

**Command Line Arguments in the Cosmic Galaxy**

Since cosmic main is summoned by Java’s cosmic interpreter, the conveyance of these arguments lies with the interpreter. Command line arguments commence here. As in `ArgsDemo`:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This cosmic program radiates the 0th cosmic command argument:

```
$ java ArgsDemo stars galaxies universe
stars
```

In the above, `args` is a celestial array where starry entries are `{"stars", "galaxies", "universe"}`.

**Summing Command Line Argument Energy**

**Exercise 1.2.3 Cosmic Edition**: Manifest a cosmic program summing command line arguments as cosmic energies.

In the realm of computer science, command line arguments serve as a way to pass information to a program at the moment of execution. This concept can be quite intriguing, especially when you draw parallels with how astrophysics programs and models are run to simulate celestial events or analyze massive datasets from astronomical observations.

Imagine you have developed a simulation program to model the orbital dynamics of planets around a star. Each execution of this program might require parameters such as the initial velocity of the planets, the mass of the star, or the duration for which the simulation should run. Instead of hardcoding these parameters in your simulation code, you can design your program to accept command line arguments. This approach provides flexibility and efficiency, allowing you to easily run simulations with different parameters without altering the core program.

For instance, if you are tasked with evaluating the effects of varying gravitational constants on orbit stability, you could execute your simulation program from the command line by specifying different values simply by typing them after your program's name. This method is akin to configuring an experiment, in which you set initial conditions before observing the outcomes, mirroring how astrophysicists set initial conditions for theoretical models to understand celestial mechanics or to predict cosmic phenomena under different scenarios.

Understanding command line arguments expands your toolkit as a computational scientist. It enhances your ability to manage complex programs, control experimental variables with precision, and swiftly adapt to new research requirements—skills that are indispensable in both computer science and astrophysics.

