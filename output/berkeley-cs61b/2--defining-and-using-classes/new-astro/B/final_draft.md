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

**Clarifying Static vs. Non-Static Methods**

In the universe of Java, non-static methods belong to the individual instance of the class, akin to dynamic astrophysical processes like star formation or evolution. They can alter an object's internal state just as these processes transform a celestial body over time.

Static methods, on the other hand, are associated with the class itself, much like universal constants that govern behaviors but do not adapt based on individual circumstances.

**Best Practices for Static Access**

When accessing static variables and methods, it is considered best practice to use the class name, as in `Star.classification`. This reinforces proper style and avoids potential pitfalls when static variables are accessed through instances, which might misleadingly imply a connection to the specific instance.

**Command Line Arguments in the Main Method**

For the `public static void main(String[] args)` method, command line arguments prove particularly useful for batch processing of data or automated testing, where predefined inputs lead to predictable outcomes. For instance, they can serve as inputs for calculations or configurations essential to the operation of a program during these tasks.

In scenarios such as "Summing Command Line Argument Energy," be sure to convert string arguments to numeric data types before summation to avoid errors associated with string handling and numeric operations.

**Astrophysical Precision in Method Examples**

In context, some method outputs may relate to astrophysical phenomena, such as different types of star emissions which emit various electromagnetic radiations. These examples strengthen the cosmic theme by grounding it in specific astrophysical principles, providing both imaginative and scientifically accurate narratives for the learner.

**Instance Variables and Cosmic Object Creation**

Not all stars twinkle the same. Some stars faintly flicker while others blaze, captivating cosmic observers with their dazzling streaks. When mimicking the cosmic tapestry in Java, the syntax can replicate such stellar diversity.

One avenue to illustrate cosmic stellar types would be to compose distinct classes for each star type:

```java
public class WhiteDwarf {
    public static void emitLight() {
        System.out.println("faint twinkle.");
    }
}

public class Supernova {
    public static void emitLight() {
        System.out.println("BLINDING LIGHT!");
    }
}
```

As seen in cosmic endeavors, classes are instantiated, and these instances harbor data. Adopting a more celestial method, we cultivate instances of the `Star` class, with stellar behaviors contingent on individual `Star` properties. This approach parallels the dynamic processes in astrophysics, such as a star's formation or evolution, influenced by its changing mass and state.

Observe the cosmic class below:

```java
public class Star {
    public double massInSolarMasses;

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

Experiencing such a Star in action:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star stellarObject;
        stellarObject = new Star();
        stellarObject.massInSolarMasses = 3;
        stellarObject.emitLight();
    }
}
```

Running this program conjures a `Star` with a mass of 3 Solar masses, animating a "standard light".

Cosmic Observations and Terminologies:

* An `Object` in Java emulates an instance of any cosmic class.
* The `Star` class's cosmic variables are labeled _instance variables_ or _non-static variables_, embedded within the cosmic class structure.
* The method within the `Star` class lacks the `static` keyword, marking it as an _instance method_ or _non-static method_ capable of interacting with and dynamically affecting an object’s state.
* Initiating cosmic events, a `Star` is summoned using `new`, triggering specific radiance through `stellarObject.emitLight()` over `Star.emitLight()`.
* Cosmic objects, after instantiation, assign to a _declared_ variable, e.g., `stellarObject = new Star();`
* Cosmic variables and stellar methods are cosmic _members_ of a class.
* Cosmic members connect via _dot notation_.

For static concepts, it is recommended to access static variables or constants using the class name directly (e.g., `Star.classification`) to reinforce proper programming style and clarify usage.

Regarding the command line and `public static void main(String[] args)`, such arguments can be exceptionally useful in automated testing or batch data processing scenarios, where variations in input shimmer like cosmic variables in different simulations.

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

    // Example for improved clarity on method context
    public boolean isLargerThan(Star otherStar) {
        return this.massInSolarMasses > otherStar.massInSolarMasses;
    }
}
```

The cosmic constructor `public Star(double mass)` becomes a key to crafting a cosmic `Star` with the `new` keyword and a guiding mass parameter, akin to star formation processes where mass dictates their lifecycle. For language travelers venturing from Python, this is akin to the `__init__` method.

**Expanded Cosmic Terminology Recap**

- **Static Method**: Represents universal constants akin to immutable physical laws, accessible without an instance.
- **Instance Method**: Showcases unique celestial characteristics akin to an evolving star's state, requiring interaction with specific object instances.
- **Static Variable**: Best accessed using the class name like `Star.constant` to denote universal characteristics across all objects. Caution when accessed via instances due to potential mutability misconceptions.

These concepts reflect astrophysical dynamics profoundly, ensuring an engaging narrative while upholding accurate technical comprehension for learners from both domains. The method design subtly draws parallels with astrophysical processes such as evolving stellar features over time.

**Celestial Array Instantiation, Arrays of Cosmic Objects**

In our journey through HW0, arrays manifest in Java with the `new` keyword:

```java
public class CelestialArrayDemo {
    public static void main(String[] args) {
        /* Manifest an array of cosmic energies. */
        double[] energyArray = new double[5];
        energyArray[0] = 1.5;
        energyArray[1] = 2.3;
    }
}
```

Unveiling arrays of cosmic objects in Java provides:

```java
public class StarArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two cosmic stars. */
        Star[] stars = new Star[2];
        stars[0] = new Star(0.4);
        stars[1] = new Star(10);

        /* A gentle glow will grace us, from stars[0] with mass 0.4 solar masses. */
        stars[0].emitLight();
    }
}
```

Here, the cosmic keyword `new` adopts two forms: once to conjure an array harboring two `Star` objects, and then to birth each `Star`. Dynamic behaviors like `emitLight()` can be thought of as representing the star characteristics, akin to processes like star evolution or supernova events, which modify their intrinsic state over time.

### Static and Instance Concepts Clarification

In our previous examples, individual stars have dynamic, non-static characteristics, while static concepts in Java, such as constants, remain unchanging and universal, like laws of physics.

When dealing with static elements, it's a best practice to access them via the class name (e.g., `Star.classification`) to maintain clarity and prevent errors.

### Command Line Arguments

The `public static void main(String[] args)` method allows for command line arguments, enhancing flexibility in processes like batch data analysis and automated testing.

In exercises like "Summing Command Line Argument Energy," remember to convert the string arguments into numeric types to accurately perform operations like summation.

### Accurate Astrophysical References

Astrophysical analogies enrich our understanding; for instance, distinguishing `emitLight()` among different star types can elucidate electromagnetic emission spectra variations across the cosmos, adding scientific precision to your coding exploration.

#### Methods of Cosmic Objects and the Cosmos <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java provides us the privilege to transpose two cosmic method forms:

* Cosmic class methods, resembling static methods and universal constants.
* Interstellar instance methods, akin to dynamic astrophysical processes like star formation or evolution.

Instance methods echo cosmic actions reserved for a unique celestial body, allowing them to dynamically interact with an object’s state. Static methods resonate with the cosmic class itself, much like universal constants. Both possess cosmic wisdom aplenty. Observe the `Math` class offers a cosmic `sqrt` method. Its static nature allows for:

```java
x = Math.sqrt(100);
```

Had `sqrt` been an earthly instance method:

```java
Math m = new Math();
x = m.sqrt(100);
```

Sometimes, cosmic logic dictates classes housing both stellar methods. Suppose our cosmic beings need to compare two stars. A non-static comparison method might unfold as thus:

```java
public Star largestStar(Star s2) {
    if (this.massInSolarMasses > s2.massInSolarMasses) {
        return this;
    }
    return s2;
}
```

The `this` keyword identifies the cosmic object in focus. Use cosmic syntax with:

```java
Star s1 = new Star(3);
Star s2 = new Star(8);
s1.largestStar(s2);
```

Alternatively, if a static method is needed, such as operating like a universal constant:

```java
public static Star largestStar(Star s1, Star s2) {
    if (s1.massInSolarMasses > s2.massInSolarMasses) {
        return s1;
    }
    return s2;
}
```

This cosmic method lifts as:

```java
Star s1 = new Star(3);
Star s2 = new Star(8);
Star.largestStar(s1, s2);
```

Observe the use of the cosmic class name—this is best practice when accessing a static method.

The "largestStar" method example confirms using static context correctly, ensuring the potential pitfalls of accessing static variables through instances are avoided. 

In addition, when implementing a `public static void main(String[] args)` method, scenarios where command line arguments are beneficial might include batch processing of data or automated testing, proving invaluable for pragmatic software engineering practices.

Exercise suggestion: "Summing Command Line Argument Energy" should explicitly state to convert string arguments to numeric data types before summation, providing clarity for learners new to string handling and numeric operations.

Overall, these cosmic analogies not only enhance engagement but strengthen technical precision, offering learners a deeper understanding of intertwining computer science and astrophysics.

**Improved Exercise 1.2.1 Cosmic Edition**: Predict the method output and verify if needed.

```java
public class Star {
    public double massInSolarMasses;
    
    public Star(double mass) {
        this.massInSolarMasses = mass;
    }

    public static Star largestStar(Star s1, Star s2) {
        if (s1.massInSolarMasses > s2.massInSolarMasses) {
            return s1;
        }
        return s2;
    }
}
```

**Cosmic Static Variables**

In some cosmic scenarios, classes treasure static variables—their properties defining cosmic essence rather than a singular instance. For instance, remarking a star's galactic classification:

```java
public class Star {
    public double massInSolarMasses;
    public static String classification = "Main Sequence";
    // Methods and additional properties
}
```

Static variables are best accessed with cosmic class identifiers, such as `Star.classification`, never through instance names like `stellarObject.classification`. Despite Java's allowance for instance-time static access, it contradicts cosmic style and can compromise cosmic clarity.

**Improved Explanation for "public static void main(String[] args)" Method**:
- Command line arguments allow for scenarios such as batch processing of data or automated testing. These enable programs to dynamically respond to varying input without altering the code base.

**Exercise 1.2.2 Cosmic Edition**: Engage in cosmic completion:

- Video: [link](https://youtu.be/8Gq-8mVbyFU)
- Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
- Solution Video: [link](https://youtu.be/Osuy8UEH03M)

In programs utilizing command line arguments to sum energy values, remember to convert string arguments to numeric data types before summation to avoid confusion for learners. This relates to string handling and numeric operations, critical for transitioning from theoretical code to functional software.

#### public static void main(String[] args) in the Cosmic Domain <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

The cosmic method declaration `public static void main(String[] args)` now unravels its mystery:

* `public`: Universal access as understood across our cosmic classes.
* `static`: A cosmic class-method grander than individual instance methods, analogous to universal constants, whereas non-static methods can represent dynamic astrophysical processes like star formation or evolution.
* `void`: Lacking a cosmic result.
* `main`: The method's cosmic identifier.
* `String[] args`: A cosmic array bearing parameters sent to the cosmic method.

**Command Line Arguments in the Cosmic Galaxy**

Since cosmic main is summoned by Java’s cosmic interpreter, the conveyance of these arguments lies with the interpreter. Command line arguments can be particularly useful in scenarios such as batch processing of data or automated testing. As illustrated in `ArgsDemo`:

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

**Exercise 1.2.3 Cosmic Edition**: Manifest a cosmic program summing command line arguments as cosmic energies. Remember to convert string arguments to numeric data types before performing summation to avoid confusion for those new to string handling and numeric operations.

#### Exploring Cosmic Libraries <a href="#using-libraries" id="using-libraries"></a>

The starry navigation of programming necessitates discovering and harnessing cosmic libraries. In our epoch of cosmic bounty, wisdom exists online, averting creative toil and debugging.

During our cosmic expedition:

* Use no cosmic libraries beyond those shared.
* Cite cosmic sources extensively.
* Explore not cosmic solutions for specific coursework like "Cosmic Expansion Berkeley".

Feel encouraged to search glorious queries like "convert CosmicString to Integer Cosmic". However, specifics akin to "Cosmic Odyssey HW - Nebula" remain off-limits.

Our course essentials, collaborative ideology, and honesty maps lie succinctly in the cosmic syllabus.

#### Astrophysical Analogies with Programming Concepts

While the chapter effectively draws parallels between static methods and universal constants, it is important to note that non-static methods dynamically interact with an object’s state, much like dynamic astrophysical processes such as star formation or stellar evolution. This distinction helps clarify the adaptability and state-specific characteristics of non-static methods.

#### Correct Usage of Static Contexts in Code

In programming, when dealing with static methods such as the "largestStar" method example, remember that static methods cannot directly reference instance variables. Instead, it is crucial to either modify the method to be non-static or pass instance data like `s1.massInSolarMasses` during the method call. For best practice, access static variables using the class name, e.g., `Star.classification`, to ensure clarity and correctness in style.

#### Explanation for "public static void main(String[] args)"

The `main` method, declared as `public static void main(String[] args)`, is central for program execution. Command line arguments, like those passed through the `args` array, are particularly useful in scenarios such as batch processing of data or automated test execution. By understanding these contexts, programmers can leverage command line arguments for streamlined workflows and testing.

#### Command Line Argument Energy Summation

In exercises such as "Summing Command Line Argument Energy," it is vital to convert string arguments to numerical types before performing a summation. This conversion prevents confusion and errors, ensuring accurate mathematical operations for learners new to data type handling in programming.

#### Enhanced Astrophysical Content

To enrich the educational fabric with astrophysical data, using detailed astrophysical examples can clarify concepts. For instance, the `emitLight` method could explore outputs related to different star types by using electromagnetic radiation distinctions, aligning technical programming discussions with precise, scientific astrophysical references.

