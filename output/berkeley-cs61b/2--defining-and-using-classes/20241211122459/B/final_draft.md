# Defining and Using Classes

In this chapter, we explore foundational Java concepts related to defining and using classes, focusing on the distinction between static and non-static methods, instance variables, object instantiation, and constructors. Static methods belong to the class level and can be called on the class itself, without needing an object instance. In contrast, instance methods require an instance of their class, allowing distinct objects to maintain unique states and behaviors. The chapter emphasizes how Java organizes code into classes and methods, crucially tying actions to objects, and describes how instance variables allow each object to maintain its unique data state.

We also delve into constructors, special methods used to create and initialize objects. Through practical examples, such as creating and manipulating "Saiyan" objects, we illustrate how constructors and arrays can effectively manage collections of objects. The chapter discusses defining class-level (static) attributes and their usage, reinforcing the significance of understanding the role of static methods and attributes in designing reusable, efficient classes. Additionally, the chapter provides insight into Java's command line argument handling and highlights best practices for incorporating libraries, analogous to leveraging known techniques in battle, to enhance programming proficiency and solution development.

2. Defining and Using Classes

Before diving into the realm of Java programming, it's crucial to build a strong foundation. If this is your initial encounter with channeling your inner Saiyan or Namekian, consider sharpening your syntax skills in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html). Think of it as training in the Hyperbolic Time Chamber—an intense preparation that primes your mind for the coding battles ahead.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

In Java, as in any great battle, every technique (code) must belong to a class—consider them your warriors. Most combat strategies are encoded in methods. Let’s start with a straightforward example:

```java
public class Saiyan {
    public static void powerUp() {
        System.out.println("Kamehameha!");
    }
}
```

Attempting to invoke the raw power of the `Saiyan` class without a strategy would lead to error energy accumulation:

```
$ java Saiyan
Error: Main method not found in class Saiyan, please define the main method as:
       public static void main(String[] args)
```

In this setup, the `Saiyan` class is poised with the potential to unleash the legendary Kamehameha, but it needs explicit commands to do so. The solution lies in adding a `main` battle method within the `Saiyan` class or deploying an external `SaiyanLauncher` class to execute the `Saiyan` techniques. Here's how this approach unfolds in practice:

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

The `SaiyanLauncher` thus becomes an ally, orchestrating the `Saiyan` class to perform its feats. There is no definitive superiority of one technique over the other; embedding a main battle method within `Saiyan` may be optimal for solo challenges, whereas a partner class like `SaiyanLauncher` could excel in collaborative battles. As your expertise expands, discerning the right choice for various scenarios becomes clearer with experience and practice.

**Instance Variables and Object Instantiation**

In the Dragon Ball universe, not all Saiyans exhibit the same prowess or transformations. Just as different Saiyans channel their energy uniquely—some through thunderous yells, others through concentrated silence—Java allows for the creation of diverse behaviors among objects with its class structure.

To mimic the variety of Saiyan transformations through code, a straightforward approach would be defining separate classes for each type of Saiyan. Consider the following examples:

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

While this method works, a more elegant solution involves leveraging Java's capability to instantiate classes and utilize instances that hold different data, providing a more flexible design. Let's introduce a `Saiyan` class, which can encapsulate various transformations based on its instance variables.

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

In a program using this structure, a `Saiyan` object can be instantiated to demonstrate its unique power level and corresponding behavior:

```java
public class SaiyanLauncher {
    public static void main(String[] args) {
        Saiyan s = new Saiyan();
        s.powerLevel = 7500;
        s.powerUp();
    }
}
```

Running this code snippet will produce a `Saiyan` with a power level of 7500, showcasing a spirited "Ha! You've got grit!". 

Key concepts and terminology to note:

* **Object**: In Java, any created instance of a class.
* **Instance Variables**: The `Saiyan` class uses a non-static variable, `powerLevel`, which is unique to each instance. Unlike some languages, Java requires variables to be declared within the class.
* **Instance Methods**: Methods like `powerUp` do not use the `static` keyword, hence they operate on the specific instance.
* **Instantiation**: To use an instance method, a `Saiyan` object must first be instantiated with the `new` keyword, followed by a method call, e.g., `s.powerUp()`.
* **Assignment and Declaration**: Once an object is instantiated, it's assigned to a variable declared with the appropriate class type, as in `s = new Saiyan();`.
* **Members**: Variables and methods within a class are termed its members and are accessed through dot notation, like `s.powerLevel` or `s.powerUp()`.

The use of these constructs allows Java programs not only to represent the breadth of Saiyan transformations but also to effectively manage and manipulate various object properties and behaviors, striking a balance between representation and functionality.

**Constructors in Dragon-Powered Java**

In object-oriented languages like Java, we use _constructors_ to bring Dragon Ball characters to life:

```java
public class SaiyanSummoner {
    public static void main(String[] args) {
        Saiyan goku = new Saiyan("Kakarot", 9000);
        goku.shoutPowerLevel();
    }
}
```

Here, the summoning relies on specific parameters to infuse our Saiyan with energy, streamlining the creation process by eliminating the need to manually set each attribute. The magic lies in the class's constructor:

```java
public class Saiyan {
    public String name;
    public int powerLevel;

    public Saiyan(String n, int p) {
        name = n;
        powerLevel = p;
    }

    public void shoutPowerLevel() {
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

The constructor `public Saiyan(String n, int p)` is invoked during each `Saiyan` summoning using the `new` keyword, along with a name and power level. This process is similar to the `__init__` method in Python, initializing your character effectively.

**Terminology Summary**

**Array Summoning: Arrays of Characters**

In Java, arrays are instantiated using the new keyword. Consider this code:

```java
public class EnergyOrbArrayDemo {
    public static void main(String[] args) {
        /* Create an array orb of five energy levels. */
        int[] energyOrbs = new int[5];
        energyOrbs[0] = 1500;
        energyOrbs[1] = 3000;
    }
}
```

Similarly, we can summon arrays of Dragon Ball characters:

```java
public class SaiyanArrayDemo {
    public static void main(String[] args) {
        /* Forge an array containing two Saiyans. */
        Saiyan[] warriors = new Saiyan[2];
        warriors[0] = new Saiyan("Vegeta", 7500);
        warriors[1] = new Saiyan("Goku", 12000);

        /* A declaration will echo, as warriors[0] has a power level of 7500. */
        warriors[0].shoutPowerLevel();
    }
}
```

The `new` keyword is used twice: first, to craft an array capable of holding `Saiyan` entities, and again when individually creating each `Saiyan`. The world of Dragon Ball seamlessly meets Java here.

#### Ki Techniques vs. Power Level Techniques <a href="#ki-techniques-vs-power-level-techniques" id="ki-techniques-vs-power-level-techniques"></a>

In the Dragon Ball universe, akin to Java, there are two essential types of techniques to master:

* **Ki Techniques**, also known as static techniques.
* **Power Level Techniques**, referred to as non-static (or instance) techniques.

Power Level Techniques are unique maneuvers executable solely by a specific warrior instance. Static techniques, however, belong to the Z Fighter class as a whole, usable independently of an object instance. Both types hold strategic value depending on battle scenarios. Consider the `Fusion Dance` as an example of a static technique; it’s a collective skill executed by calling the Z Fighter class itself:

```java
fusion = ZFighter.fuse(Goku, Vegeta);
```

If `fuse` were a power level technique, we would need the following syntax, which proves cumbersome, especially in high-stakes galactic battles:

```java
ZFighter goku = new ZFighter();
goku.fuse(Goku, Vegeta);
```

It's sometimes beneficial for a class to exhibit both power level and static techniques. For instance, we may wish to compare the strength of two Saiyans by creating a static technique:

```java
public static Saiyan strongerSaiyan(Saiyan s1, Saiyan s2) {
    if (s1.powerLevel > s2.powerLevel) {
        return s1;
    }
    return s2;
}
```

This technique is invoked using the class name, showcasing its static nature:

```java
Saiyan goku = new Saiyan(150000);
Saiyan vegeta = new Saiyan(120000);
Saiyan.strongerSaiyan(goku, vegeta);
```

Alternatively, `strongerSaiyan` could function as a power level technique:

```java
public Saiyan strongerSaiyan(Saiyan other) {
    if (this.powerLevel > other.powerLevel) {
        return this;
    }
    return other;
}
```

Here, `this` references the current instance of the Saiyan, and the method is invoked via a specific object:

```java
Saiyan goku = new Saiyan(150000);
Saiyan vegeta = new Saiyan(120000);
goku.strongerSaiyan(vegeta);
```

**Training 1.2.1**: What would the following technique achieve? Test your ideas if unsure.

```java
public static Saiyan strongerSaiyan(Saiyan s1, Saiyan s2) {
    if (powerLevel > s2.powerLevel) {
        return this;
    }
    return s2;
}
```

**Static Attributes**

There are times when it's beneficial for the Z Fighter class to house static attributes. Such attributes are integral to the class itself, rather than its warriors. A static attribute example is the legendary title of the Saiyans, such as "Super Saiyan":

```java
public class Saiyan {
    public int powerLevel;
    public static String legendaryTitle = "Super Saiyan";
    ...
}
```

Access static attributes using the class name, not an instance, to avoid bad practices and potential misinterpretations, e.g., `Saiyan.legendaryTitle` rather than `goku.legendaryTitle`.

While you can technically access a static variable using an instance, best practices frown upon this as it may cause confusion, which the eternal guardian surely wishes to avoid.

**Training 1.2.2**: Kick off this training by checking out the following resources:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slides: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)



#### public static void main(String\[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

In our journey through Java programming, let's unravel the components of the main method declaration we've consistently used. Each part has a purpose, much like the techniques and tactics used by warriors in the Dragon Ball universe:

* `public`: This is akin to making a powerful move like the Kamehameha available to anyone across the universe. It ensures the method can be accessed from anywhere.
* `static`: Just as the Spirit Bomb can be gathered and used by Goku alone without needing his allies to generate it for him, this method belongs to the class rather than any object of the class.
* `void`: This indicates that the method doesn't return a result, similar to a wish made to Shenron that has no tangible effect on the universe.
* `main`: Consider this as the signature move or technique.
* `String[] args`: These parameters can be likened to receiving crucial intel from King Kai before a major battle—essential information that can alter the course of a fight.

**Command Line Arguments**

The `main` method is invoked by the Java interpreter itself, rather than by another Java class. It's the interpreter's role to supply any arguments. Think of these as vital strategy updates from King Kai, sent just before the Z Fighters engage their enemies. For instance, consider the following `ArgsDemo` program:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

In this example, the program prints the first command line argument passed to it. It is in the same way Vegeta might demand to immediately review the highest power level reading:

```
$ java ArgsDemo these are command line arguments
these
```

Here, `args` is an array of String elements, where the entries are {"these", "are", "command", "line", "arguments"}, comparable to a list of warriors in a Saiyan space pod log, ready for dispatch.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Write a program that sums up command line arguments, assuming they are numbers, much like determining the combined power level of all Z Fighters participating in a battle. Solutions for exercises can be compared to intense training sessions in the Hyperbolic Time Chamber or by checking related resources on Bulma's computer via GitHub.

#### Using Libraries Like Z-Warriors <a href="#using-libraries-like-z-warriors" id="using-libraries-like-z-warriors"></a>

One of the most crucial skills as a developer (akin to being a Z-fighter) is the ability to identify and utilize existing libraries (similar to mastering Kamehameha or Fusion techniques from fellow Z-fighters). In the dynamic world of Dragon Ball, saving time and effort (or conserving ki energy) and minimizing debugging (or intense combat training) are often achieved by drawing on the hyperbolic time chamber (or the wisdom of Master Roshi) for guidance and expertise.

In this (course) adventure, utilizing libraries is encouraged, but consider these guidelines:

* Utilize only those libraries (martial arts techniques) that we introduce (which are part of the Z-fighter’s approved arsenal).
* Properly attribute your sources (recognize and credit the warrior's strength and contributions).
* Refrain from seeking solutions for particular problems (combat scenarios) that involve techniques you have yet to master or are prohibited.

For instance, searching for "convert Super Saiyan Kamehameha" is acceptable. However, searching for "Final Blow Cell Saga Uncut Version" is not permissible due to potential unapproved techniques or spoilers.

For detailed insight into collaboration and the academic integrity policy (or the Z-warrior code of conduct), please refer to the course syllabus. Remain steadfast in your training and development, just as a Z-warrior adheres to their principles while advancing their skills.