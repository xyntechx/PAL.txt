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

As seen in cosmic endeavors, classes are instantiated, and these instances harbor data. Adopting a more celestial method, we cultivate instances of the `Star` class, with stellar behaviors contingent on individual `Star` properties. Observe the cosmic class below:

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
* The method within the `Star` class lacks the `static` keyword, marking it as an _instance method_ or _non-static method_.
* Initiating cosmic events, a `Star` is summoned using `new`, triggering specific radiance through `stellarObject.emitLight()` over `Star.emitLight()`.
* Cosmic objects, after instantiation, assign to a _declared_ variable, e.g., `stellarObject = new Star();`
* Cosmic variables and stellar methods are cosmic _members_ of a class.
* Cosmic members connect via _dot notation_.

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

Here, the cosmic keyword `new` adopts two forms: once to conjure an array harboring two `Star` objects, and then to birth each `Star`.

#### Methods of Cosmic Objects and the Cosmos <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java provides us the privilege to transpose two cosmic method forms:

* Cosmic class methods, resembling static methods.
* Interstellar instance methods, non-static in nature.

Instance methods echo cosmic actions reserved for a unique celestial body. Static methods resonate with the cosmic class itself. Both possess cosmic wisdom aplenty. Observe the `Math` class offers a cosmic `sqrt` method. Its static nature allows for:

```java
x = Math.sqrt(100);
```

Had `sqrt` been an earthly instance method:

```java
Math m = new Math();
x = m.sqrt(100);
```

Sometimes, cosmic logic dictates classes housing both stellar methods. Suppose our cosmic beings require comparing two stars. A static comparison method swirls as thus:

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

Observe usage of the cosmic class name—since the function is static.

Alternately, if interstellar nuances beckon non-static methods:

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

Here, invocation occurs through a specific cosmic instance.

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

#### Exploring Cosmic Libraries <a href="#using-libraries" id="using-libraries"></a>

The starry navigation of programming necessitates discovering and harnessing cosmic libraries. In our epoch of cosmic bounty, wisdom exists online, averting creative toil and debugging.

During our cosmic expedition:

* Use no cosmic libraries beyond those shared.
* Cite cosmic sources extensively.
* Explore not cosmic solutions for specific coursework like "Cosmic Expansion Berkeley".

Feel encouraged to search glorious queries like "convert CosmicString to Integer Cosmic". However, specifics akin to "Cosmic Odyssey HW - Nebula" remain off-limits.

Our course essentials, collaborative ideology, and honesty maps lie succinctly in the cosmic syllabus.