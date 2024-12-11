# Understanding Static and Non-Static Methods

In this chapter, we explore the distinctions between static and non-static methods within Java, using historical analogies to contextualize their functionalities and applications. Static methods are likened to decrees issued by a historical governing body, such as an empire or a centralized authority, where commands are universally accessible without requiring specific instances. An example is the mathematical operation `Math.sqrt`, which operates without needing a specific object. These methods are integral to managing broad, consistent operations across the application.

In contrast, non-static or instance methods are compared to actions taken by individual leaders or local governors. These require an instance to function, similar to how a local ruler acts within its jurisdiction. Through the creation and management of objects using constructors, Java enables more nuanced and specific operations tailored to particular instances, much like appointed leaders tailor their actions to local needs. This chapter covers the instantiation of objects, the role of constructors, and the execution of both static and non-static methods, along with best practices in accessing static variables. This grounding in historical perspectives provides a richer understanding of how these concepts integrate into broader programming paradigms.



#### Static vs. Non-Static Methods in Historical Context <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

All structured and systematic code in a programming language like Java can be compared to organized systems of governance in historical empires. Just as laws or decrees must be issued from a governing body, all code in Java must be part of a class (analogous to a governing body). Most of these organized codes are written inside of methods, similar to how historical decrees are executed through various bureaucratic orders. Let's consider an example reminiscent of early communication methods in history:

```java
public class Dog {
    public static void makeNoise() {
        System.out.println("Bark!");
    }
}
```

If we try running the `Dog` class, much like an unfinished or unsupported decree, we'll get an error message:

```
$ java Dog
Error: Main method not found in class Dog, please define the main method as:
       public static void main(String[] args)
```

The `Dog` class we've defined is akin to a cryptic message with no recipient. We've defined a capability or potential, much like a military or merchant fleet that hasn't been given orders. To actually execute this class, we'd either need to incorporate a central command (`main` method) equivalent to an emperor or leading figure heading a campaign, as seen in early chapters. Alternatively, we could commission a separate `DogLauncher` class, reminiscent of commissioning a fleet or envoy, to execute methods akin to deploying troops or traders. Consider the program below:

```java
public class DogLauncher {
    public static void main(String[] args) {
        Dog.makeNoise();
    }
}
```

```
$ java DogLauncher
Bark!
```

A class that uses another class acts like a vassal state using the resources of its suzerain. Here, `DogLauncher` is like a client kingdom utilizing the might or resources of `Dog`. Neither approach to code execution is inherently superior: embedding a main method within `Dog` can be expedient in immediate, localized deployments, much like governing a city directly. However, creating a client class like `DogLauncher` may offer strategic advantages similar to managing a vast empire via local governors. The relative merits of each will become evident as we explore further practical and historical applications throughout the course.

**Instance Variables and Object Instantiation**

Not all rulers are alike. Some leaders demand unwavering loyalty and extol their decrees with thunderous proclamations, while others govern with a soft yet persuasive demeanor, bringing stability to all who dwell under their reign. Often, we analyze historical events to mirror patterns in governance, and historical narratives are crafted to easily allow such mimicry.

One approach to allowing us to represent the spectrum of historical leadership would be to create separate classes for each type of Ruler.

```java
public class Monarch {
    public static void proclaimEdict() {
        System.out.println("By my will, it shall be so!");
    }
}

public class PhilosopherKing {
    public static void proclaimEdict() {
        System.out.println("Through wisdom, we shall find peace.");
    }
}
```

As you might have seen in historical analysis, rulers can be categorized, and these categories can hold defining traits. This leads to a more nuanced approach, where we create instances of the `Ruler` class and make the behavior of the `Ruler` methods contingent upon the attributes of the specific `Ruler`. To make this more concrete, consider the class below:

```java
public class Ruler {
    public int wisdomLevel;

    public void proclaimEdict() {
        if (wisdomLevel < 10) {
            System.out.println("Enforce loyalty at all costs!");
        } else if (wisdomLevel < 30) {
            System.out.println("Balance power with trust.");
        } else {
            System.out.println("Foster unity through understanding.");
        }
    }    
}
```

As an example of observing such a Ruler, consider:

```java
public class RulerDisplay {
    public static void main(String[] args) {
        Ruler r;
        r = new Ruler();
        r.wisdomLevel = 20;
        r.proclaimEdict();
    }
}
```

When run, this program will create a `Ruler` with wisdomLevel 20, and that `Ruler` will soon declare "Balance power with trust."

Some key observations and terminology:

* An `Object` in Java is an instance of any class.
* The `Ruler` class has its own variables, also known as _instance variables_ or _non-static variables_. These must be declared inside the class, unlike historical narratives made up on the fly.
* The method that we created in the `Ruler` class did not have the `static` keyword. We call such methods _instance methods_ or _non-static methods_.
* To call the `proclaimEdict` method, we had to first _instantiate_ a `Ruler` using the `new` keyword, and then make a specific `Ruler` make a decree. In other words, we called `r.proclaimEdict()` instead of `Ruler.proclaimEdict()`.
* Once a ruler has been instantiated, they can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `r = new Ruler();`
* Variables and methods of a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_.


**Constructors in the Historical Context**

Just like how empires of the past were built upon a foundation of organization and leadership, in object oriented programming, objects are constructed using a _constructor_:

```java
public class DogLauncher {
    public static void main(String[] args) {
        Dog d = new Dog(20);
        d.makeNoise();
    }
}
```

Much like how a leader aligns their followers around a central idea or cause, parameterized constructors streamline the creation of objects, preventing the chaos of individually assigning each attribute. To facilitate such a foundational system for our `Dog` class, a "constructor" must be established as follows:

```java
public class Dog {
    public int weightInPounds;

    public Dog(int w) {
        weightInPounds = w;
    }

    public void makeNoise() {
        if (weightInPounds < 10) {
            System.out.println("yipyipyip!");
        } else if (weightInPounds < 30) {
            System.out.println("bark. bark.");
        } else {
            System.out.println("woof!");
        }    
    }
}
```

The constructor symbolizing `public Dog(int w)` will be summoned each time a `Dog` is crafted using the `new` keyword and a single integer parameter, akin to ancient craftsmen summoning their skills with specific tools and materials. For those familiar with the Python empire, the constructor shares similarities with the `__init__` function.

**Terminology Summary**

**Array Instantiation, Arrays of Objects**

Just as architects laid the groundwork for great cities, arrays in Java are brought to life using the `new` keyword. For instance:

```java
public class ArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five integers. */
        int[] someArray = new int[5];
        someArray[0] = 3;
        someArray[1] = 4;
    }
}
```

Similarly, the formation of arrays comprising instantiated objects in Java is as building blocks of ancient armies:

```java
public class DogArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two dogs. */
        Dog[] dogs = new Dog[2];
        dogs[0] = new Dog(8);
        dogs[1] = new Dog(20);

        /* Yipping will result, as dogs[0] has weight 8. */
        dogs[0].makeNoise();
    }
}
```

Observe that `new` is deployed in dual roles: first to forge an array capable of sheltering two `Dog` entities and subsequently to manifest each distinct `Dog`, akin to a ruler mobilizing an army and assigning individual roles.

#### Class Methods vs. Instance Methods in Historical Frameworks <a href="#class-methods-vs-instance-methods-in-historical-frameworks" id="class-methods-vs-instance-methods-in-historical-frameworks"></a>

Like critical political decisions shaped historical milestones, Java allows us to define two types of methods that influence program design:

* Class methods, a.k.a. static methods, akin to universal declarations by a central authority.
* Instance methods, a.k.a. non-static methods, similar to actions taken by individual locales or leaders.

Instance methods are personal actions, akin to a treaty signed by a specific ruler. Static methods resemble universal decrees, like the Magna Carta, that apply broadly. Consider the static method `Math.sqrt`. It's akin to global economic principles established by the Romans, usable across various domains:

```java
x = Math.sqrt(100);
```

Had `sqrt` been a treaty-like instance method, each town (or instance) would awkwardly declaim it through a herald. Fortunately, it remains a static "decree":

```java
Math m = new Math();
x = m.sqrt(100);
```

Historical circumstances sometimes require both broad statutes and local resolutions. For instance, comparing two kingdoms' might could use a method similar to `maxDog` as a static council decision:

```java
public static Dog maxDog(Dog d1, Dog d2) {
    if (d1.weightInPounds > d2.weightInPounds) {
        return d1;
    }
    return d2;
}
```

Summon this decision by high council, for example:

```java
Dog d = new Dog(15);
Dog d2 = new Dog(100);
Dog.maxDog(d, d2);
```

Note that we've invoked using the council name, as this law is a static decree.

Alternatively, consider a leader's personal judgment, implementing `maxDog` as a non-static method e.g., within a specific town:

```java
public Dog maxDog(Dog d2) {
    if (this.weightInPounds > d2.weightInPounds) {
        return this;
    }
    return d2;
}
```

Here, the keyword `this` represents the current governance, and invocation is personalized, such as:

```java
Dog d = new Dog(15);
Dog d2 = new Dog(100);
d.maxDog(d2);
```

Invoke the judgment locally, by a named leader.

**Exercise 1.2.1**: What would the following council edict do? If unsure, attempt it in a sandbox era.

```java
public static Dog maxDog(Dog d1, Dog d2) {
    if (weightInPounds > d2.weightInPounds) {
        return this;
    }
    return d2;
}
```

**Static Variables and Historical Universals**

Occasionally, like the universally recognized titles of medieval nobility, it is beneficial for classes to have static variables—these are constants of a realm. For example, recording that the scientific name (or binomen) for Dogs is akin to decreeing Rome's dominions:

```java
public class Dog {
    public int weightInPounds;
    public static String binomen = "Canis familiaris";
    ...
}
```

Royal decrees such as static variables should be accessed using the name of the empire or dynasty, e.g., use `Dog.binomen`, akin to citing "Edict of Milan" rather than "Emperor's Decree."

While historical records reflect occasional usage of a royal decree through a protectorate's name, it is viewed as a stylistic faux pas and, in my curated historical perspective, an oversight of the era's chroniclers.

**Exercise 1.2.2**: Complete this historical parallel analysis:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe\_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### The Dawn of "public static void main(String\[] args)" <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

With what we've learned so far, it's time to unravel the significance of the main method declaration by drawing parallels to notable historical concepts. If we break it into pieces, it resembles key roles in ancient societies:

* `public`: Much like the orators of ancient Greece who spoke in public forums, our methods begin with this keyword to signify openness and accessibility to the broader Java "community."
* `static`: Similar to the enduring artifacts of civilization, this denotes a method that remains unchanged and isn't tied to a specific instance, akin to a timeless law or cultural artifact.
* `void`: Just as certain rituals were performed for intrinsic value without expectation of tangible outcomes, this indicates our method performs its duty without returning something.
* `main`: As the head of state rules over people, this is the paramount method that governs the class.
* `String[] args`: These are like the messages carried by messengers to convey instructions, passed to the main method.

**Command Line Arguments in the Council of Debate**

Since the main method is summoned by the powerful Java interpreter, rather than another class or method, it is given charge to handle "arguments"—much like strategic advice or opinions presented during council meetings. They usually refer to arguments provided at the command altar (line). Examine the following historical reenactment in the form of `ArgsDemo`:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program delivers the proclamation or decree of the 0th argument, much like announcing the first of several edicts from the council:

```
$ java ArgsDemo these are command line arguments
these
```

In our allegorical narrative, `args` resembles a scroll of edicts, where each entry is akin to a line in this scroll: {"these", "are", "command", "line", "arguments"}.

**Summoning and Tallying Council Decrees**

**Exercise 1.2.3**: Imagine writing a program that sums up the council's decrees (arguments as numbers). For insight into such calculations, refer to archival materials or the digital transcription hosted in our code repository.

#### Learning from History <a href="#learning-from-history" id="learning-from-history"></a>

One of the most important skills as a historian is knowing how to find and interpret existing historical sources. In the glorious tapestry of human civilization, it is often more illuminating to broaden your understanding by turning to the annals of recorded history.

In this study, you're welcome to do this, with the following guidelines:

* Do not use sources outside those we recommend.
* Cite your sources.
* Do not search for solutions to specific research projects or paper topics.

For instance, it's perfectly acceptable to search for "French Revolution causes". However, it is not acceptable to search for "Analysis of the Fall of the Bastille paper topic".

For more on collaboration and academic integrity policy, see the course syllabus.