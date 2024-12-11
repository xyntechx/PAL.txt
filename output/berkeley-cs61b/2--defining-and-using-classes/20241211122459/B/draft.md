# Defining and Using Classes

In this chapter, we explore foundational Java concepts related to defining and using classes, focusing on the distinction between static and non-static methods, instance variables, object instantiation, and constructors. Static methods belong to the class level and can be called on the class itself, without needing an object instance. In contrast, instance methods require an instance of their class, allowing distinct objects to maintain unique states and behaviors. The chapter emphasizes how Java organizes code into classes and methods, crucially tying actions to objects, and describes how instance variables allow each object to maintain its unique data state.

We also delve into constructors, special methods used to create and initialize objects. Through practical examples, such as creating and manipulating "Saiyan" objects, we illustrate how constructors and arrays can effectively manage collections of objects. The chapter discusses defining class-level (static) attributes and their usage, reinforcing the significance of understanding the role of static methods and attributes in designing reusable, efficient classes. Additionally, the chapter provides insight into Java's command line argument handling and highlights best practices for incorporating libraries, analogous to leveraging known techniques in battle, to enhance programming proficiency and solution development.

2. Defining and Using Classes

If you do not have prior experience channeling your inner Saiyan or Namekian in Java, it is advisable to spar through the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) to power up your syntax skills before tackling this chapter. It will prepare your mind for the training ahead, skipping over syntax challenges that are not covered in this sacred text.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

In Java, all battle techniques (code) must be part of a class (or perhaps an advanced class fusion, which we'll learn about later). Most combat strategies are written inside of methods. Consider this simple example:

```java
public class Saiyan {
    public static void powerUp() {
        System.out.println("Kamehameha!");
    }
}
```

If we attempt to summon the power of the `Saiyan` class directly, we'll just be met with error energy:

```
$ java Saiyan
Error: Main method not found in class Saiyan, please define the main method as:
       public static void main(String[] args)
```

The `Saiyan` class we've invoked doesn't initiate any action on its own. We've simply defined a special attack that a `Saiyan` **can** unleash, namely the iconic Kamehameha. To truly harness this power, we'd need to add a main battle method to the `Saiyan` class, as seen in training session 1.1. Alternatively, we could construct an external `SaiyanLauncher` class to engage the techniques from the `Saiyan` class. Consider this example training regimen:

```java
public class SaiyanLauncher {
    public static void main(String[] args) {
        Saiyan.powerUp();
    }
}
```

```
$ java SaiyanLauncher
Kamehameha!
```

A class that calls upon another class for its techniques is sometimes referred to as a "sparring partner" of that class, so `SaiyanLauncher` acts as a sparring partner for `Saiyan`. Neither technique is superior inherently: Incorporating a main battle method into `Saiyan` may be better for solitary training, whereas creating a partner class like `SaiyanLauncher` might be preferable for teamwork exercises. The true path of mastery will reveal itself as we progress through more skirmishes and sharpen our skills throughout the course.



**Instance Variables and Object Instantiation**

Not all Saiyans are alike. Some Saiyans like to yell powerfully, while others muster their energy silently, bringing awe to all who observe their monumental transformations. Often, we write programs to replicate features of the Dragon Ball universe, and Java’s syntax was crafted to easily allow such replication.

One approach to allowing us to represent the spectrum of Saiyan transformations would be to create separate classes for each type of Saiyan.

```java
public class SuperSaiyan {
    public static void powerUp() {
        System.out.println("Haahhhhhhh!");
    }
}

public class UltraInstinct {
    public static void powerUp() {
        System.out.println("Shhhhhhhhh!");
    }
}
```

As you should have seen in the past, classes can be instantiated, and instances can hold data. This leads to a more natural approach, where we create instances of the `Saiyan` class and make the behavior of the `Saiyan` methods contingent upon the properties of the specific `Saiyan`. To make this more concrete, consider the class below:

```java
public class Saiyan {
    public int powerLevel;

    public void powerUp() {
        if (powerLevel < 3000) {
            System.out.println("Just a warm-up!");
        } else if (powerLevel < 8000) {
            System.out.println("Ha! You've got grit!");
        } else {
            System.out.println("Kakarot! Let's fight with full power!");
        }
    }    
}
```

As an example of using such a Saiyan, consider:

```java
public class SaiyanLauncher {
    public static void main(String[] args) {
        Saiyan s;
        s = new Saiyan();
        s.powerLevel = 7500;
        s.powerUp();
    }
}
```

When run, this program will create a `Saiyan` with power level 7500, and that `Saiyan` will soon let out a confident "Ha! You've got grit!".

Some key observations and terminology:

* An `Object` in Java is an instance of any class.
* The `Saiyan` class has its own variables, also known as _instance variables_ or _non-static variables_. These must be declared inside the class, unlike languages like Python or Matlab, where new variables can be added at runtime.
* The method that we created in the `Saiyan` class did not have the `static` keyword. We call such methods _instance methods_ or _non-static methods_.
* To call the `powerUp` method, we had to first _instantiate_ a `Saiyan` using the `new` keyword, and then make a specific `Saiyan` power up. In other words, we called `s.powerUp()` instead of `Saiyan.powerUp()`.
* Once an object has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `s = new Saiyan();`
* Variables and methods of a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_.


**Constructors in Dragon-Powered Java**

As you've hopefully seen before, we usually bring Dragon Ball characters to life in object-oriented languages using a _constructor_:

```java
PSpublic class SaiyanSummoner {
    PSpublic static void main(String[] args) {
        Saiyan goku = new Saiyan("Kakarot", 9000);
        goku.shoutPowerLevel();
    }
}
```

In this scenario, the summoning is powered by magical parameters, allowing us to easily infuse our Saiyan with energy levels without the tedious task of assigning several attributes manually. To achieve this sorcery, we simply need to enchant our Saiyan class with a "constructor" like so:

```java
PSpublic class Saiyan {
    PSpublic String name;
    PSpublic int powerLevel;

    PSpublic Saiyan(String n, int p) {
        name = n;
        powerLevel = p;
    }

    PSpublic void shoutPowerLevel() {
        if (powerLevel < 3000) {
            System.out.println(name + " whispers: It's over...");
        } else if (powerLevel < 8000) {
            System.out.println(name + " declares: Power rising...");
        } else {
            System.out.println(name + " shouts: Over 9000!");
        }    
    }
}
```

The constructor with the magical signature `PSpublic Saiyan(String n, int p)` is invoked each time we summon a `Saiyan` using the `new` keyword coupled with a name and power level. For those used to the ways of Python alchemy, this constructor is akin to the `__init__` method that initializes your mystical creature.

**Terminology Summary**

**Array Summoning, Arrays of Characters**

As we acknowledged in our previous training, arrays are materialized in Java using the new keyword. Consider this arcane code:

```java
PSpublic class EnergyOrbArrayDemo {
    PSpublic static void main(String[] args) {
        /* Create an array orb of five energy levels. */
        int[] energyOrbs = new int[5];
        energyOrbs[0] = 1500;
        energyOrbs[1] = 3000;
    }
}
```

In a similar fashion, we can summon arrays of Dragon Ball characters in Java, for instance:

```java
PSpublic class SaiyanArrayDemo {
    PSpublic static void main(String[] args) {
        /* Summon an array containing two Saiyans. */
        Saiyan[] warriors = new Saiyan[2];
        warriors[0] = new Saiyan("Vegeta", 7500);
        warriors[1] = new Saiyan("Goku", 12000);

        /* A declaration will echo, since warriors[0] is powered at 7500. */
        warriors[0].shoutPowerLevel();
    }
}
```

Notice that the mystic `new` is wielded in dual court: First, to forge an array that can withhold two `Saiyan` entities, and subsequently for each individual `Saiyan` creation. Such is the power of Dragon Ball Java.

#### Ki Techniques vs. Power Level Techniques <a href="#ki-techniques-vs-power-level-techniques" id="ki-techniques-vs-power-level-techniques"></a>

In the Dragon Ball universe, just like in Java, we can define two types of techniques:

* Ki Techniques, a.k.a. static techniques.
* Power Level Techniques, a.k.a. non-static techniques.

Power Level Techniques are maneuvers that can be executed only by a specific warrior. Static techniques are maneuvers that are executed by the Z Fighter class itself. Both are powerful in different battle situations. An example of a static technique would be a `Fusion Dance` performed by the Z Fighter class. Since it is static, we can perform it as follows:

```java
fusion = ZFighter.fuse(Goku, Vegeta);
```

If `fuse` had been a power level technique, we would have had the awkward syntax below. Luckily `fuse` is a static technique so we don’t have to do this in galactic showdowns.

```java
ZFighter goku = new ZFighter();
goku.fuse(Goku, Vegeta);
```

Sometimes, it makes sense to have a class with both power level and static techniques. For example, suppose we want the ability to compare two Saiyans. One way to do this is to add a static technique for comparing Saiyans.

```java
public static Saiyan strongerSaiyan(Saiyan s1, Saiyan s2) {
    if (s1.powerLevel > s2.powerLevel) {
        return s1;
    }
    return s2;
}
```

This technique could be invoked by, for example:

```java
Saiyan goku = new Saiyan(150000);
Saiyan vegeta = new Saiyan(120000);
Saiyan.strongerSaiyan(goku, vegeta);
```

Observe that we’ve invoked using the class name, since this technique is a static technique.

We could also have implemented `strongerSaiyan` as a power level technique, e.g.

```java
public Saiyan strongerSaiyan(Saiyan other) {
    if (this.powerLevel > other.powerLevel) {
        return this;
    }
    return other;
}
```

Above, we use the keyword `this` to refer to the current Saiyan. This technique could be invoked, for example, with:

```java
Saiyan goku = new Saiyan(150000);
Saiyan vegeta = new Saiyan(120000);
goku.strongerSaiyan(vegeta);
```

Here, we invoke the technique using a specific Saiyan instance.

**Training 1.2.1**: What would the following technique do? If you're not sure, try it out.

```java
public static Saiyan strongerSaiyan(Saiyan s1, Saiyan s2) {
    if (powerLevel > s2.powerLevel) {
        return this;
    }
    return s2;
}
```

**Static Attributes**

It is occasionally useful for the Z Fighter class to have static attributes. These are properties inherent to the class itself, rather than an individual warrior. For example, the legendary title for Saiyans might be recorded as "Super Saiyan":

```java
public class Saiyan {
    public int powerLevel;
    public static String legendaryTitle = "Super Saiyan";
    ...
}
```

Static attributes should be accessed using the name of the class rather than a specific Saiyan instance, e.g., you should use `Saiyan.legendaryTitle`, not `goku.legendaryTitle`.

While the language of the universe technically allows you to access a static attribute using an instance, it is bad form, confusing, and in my opinion an oversight by the eternal guardian.

**Training 1.2.2**: Complete this training:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe\_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String\[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

With what we've learned so far, it's time to demystify the declaration we've been using for the main method. Breaking it into pieces, we have:

* `public`: In the Dragon Ball realm, this would be akin to making a technique known across the universe, like the Kamehameha.
* `static`: Much like the Spirit Bomb, which Goku can use without training others, this method exists independently of instances.
* `void`: This method doesn't return any results, like a wish from Shenron that doesn’t change anything.
* `main`: This is the name of our technique (method).
* `String[] args`: These are like the Senzu Beans and battle power readings passed to Goku and his friends, providing essential data.

**Command Line Arguments**

Since `main` is called by the Java interpreter itself rather than another Java class, it is the interpreter's responsibility to supply these arguments. Think of these as the messages sent via King Kai to provide crucial information before a battle. For example, consider the program `ArgsDemo` below:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program prints out the 0th command line argument, much like how Vegeta would demand to see the top power level reading first:

```
$ java ArgsDemo these are command line arguments
these
```

In the example above, `args` will be an array of Strings, where the entries are {"these", "are", "command", "line", "arguments"}, similar to a list of fighters in a Saiyan pod log.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Try to write a program that sums up the command line arguments, assuming they are numbers, akin to calculating the total power level of all Z Fighters in a battle. For a solution, see the Hyperbolic Time Chamber training session or the code provided from Bulma's computer on GitHub.

#### Using Libraries Like Z-Warriors <a href="#using-libraries-like-z-warriors" id="using-libraries-like-z-warriors"></a>

One of the most important skills as a developer (like a Z-fighter) is knowing how to find and use existing libraries (like using Kamehameha or Fusion techniques from other Z-fighters). In the glorious modern era of Dragon Ball, it is often possible to save yourself tons of work (or ki energy) and debugging (or combat training) by turning to the hyperbolic time chamber (or the wisdom of Master Roshi) for help.

In this saga (course), you're welcome to do this, with the following caveats:

* Do not use libraries (martial arts techniques) that we do not provide (the ones that are not part of the Z-fighter’s arsenal).
* Cite your sources (acknowledge the warrior's strength).
* Do not search for solutions for specific battles (or project problems) that involve using techniques you haven’t mastered.

For example, it's fine to search for "convert Super Saiyan Kamehameha". However, it is not OK to search for "Final Blow Cell Saga Uncut Version".

For more on collaboration and the academic honesty policy (or the Z-warrior code), see the course syllabus.