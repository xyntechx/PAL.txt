# Understanding Java Classes

In this chapter, we delve into defining and using classes in Java, with a focus on the distinction between static and non-static methods. Java requires all code to be part of a class, and within those classes, we define methods to encapsulate behaviors. Static methods belong to the class itself and can be invoked without an instance, whereas non-static methods require an instance of the class. The text uses the analogy of historical figures to explain these concepts, likening static methods to societal decrees applicable to all, and non-static methods to personal traits of individuals. The chapter also covers instance variables, object instantiation, and constructors, anchoring these concepts in historical narratives to emphasize their use in defining unique object states and behaviors.

Furthermore, the text draws parallels between programming constructs and historical laws, explaining how class members – both variables and methods – are accessed using dot notation. Different types of methods and constructors are used to illustrate event-driven transformations, similar to pivotal historical events. The significance of `public static void main(String[] args)` is explored, connecting it to public declarations in history, and how command line arguments can be likened to directives shaping historical events. The chapter emphasizes the use of credible historical sources to enhance understanding, urging students to engage with external resources responsibly.

# 2. Defining and Using Classes

If you do not have prior Java experience, we recommend that you work through the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before reading this chapter. It will cover various syntax issues that we will not discuss in the book.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

All code in Java must be part of a class (or something similar to a class, which we'll learn about later). Most code is written inside of methods. Let's consider an example:

```java
public class Dog {
    public static void makeNoise() {
        System.out.println("Bark!");
    }
}
```

If we try running the `Dog` class, we'll simply get an error message:

```
$ java Dog
Error: Main method not found in class Dog, please define the main method as:
       public static void main(String[] args)
```

The `Dog` class we've defined doesn't do anything. We've simply defined something that `Dog` **can** do, namely make noise. To actually run the class, we'd either need to add a main method to the `Dog` class, as we saw in chapter 1.1. Or we could create a separate [`DogLauncher`](https://www.youtube.com/watch?v=Q-LE-jJQLTM) class that runs methods from the `Dog` class. For example, consider the program below:

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

A class that uses another class is sometimes called a "client" of that class, i.e. `DogLauncher` is a client of `Dog`. Neither of the two techniques is better: Adding a main method to `Dog` may be better in some situations, and creating a client class like `DogLauncher` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout the course.

Now, consider a historical perspective. Think of the relationship between classes as akin to the relationship between a monarch and their royal court. The monarch, like the `Dog` class, possesses intrinsic capabilities and authority. However, unless called upon or utilized by members of the court or external advisors (similar to a client like the `DogLauncher`), these abilities remain dormant or unexpressed. The court, or client, serves to engage the monarch's capabilities, orchestrating the manifestation of power and decision-making. In one context, the king could take direct action, akin to the `Dog` class having its own main method, while in another, the advisors (or client class) could bring the monarch's decrees to fruition across the realm. As in history, the choice between these mechanisms depends on the need for direct versus mediated execution of commands, much like different historical events sometimes called for monarchs to act independently or through their council.

**Instance Variables and Object Instantiation in Historical Context**

Not all historical figures are alike. Some leaders like to dictate every small detail of governance, while others inspire sonorously, bringing a nation together with their stirring words. Often, we study history to understand the features of the epoch we are analyzing, and historiography was crafted to allow for a deep understanding of such nuances.

One approach to representing the spectrum of historical leadership styles would be to create separate categories for each type of leader.

```
public class AutocraticLeader {
    public static void commandPolicies() {
        System.out.println("implement rigid decrees and control!");
    }
}

public class CharismaticLeader {
    public static void inspireNation() {
        System.out.println("ignite passion with rhetoric and vision!");
    }
}
```

As you should have seen in the past, personas can be instantiated, and individual figures can hold certain traits. This leads to a more natural approach, where we create instances of the `Leader` class and make the behavior of the `Leader` methods contingent upon the traits of the specific `Leader`. To make this more concrete, consider the class below:

```
public class Leader {
    public int influenceLevel;

    public void displayLeadershipStyle() {
        if (influenceLevel < 10) {
            System.out.println("mandate and micromanage!");
        } else if (influenceLevel < 30) {
            System.out.println("debate and negotiate.");
        } else {
            System.out.println("unite and inspire!");
        }
    }    
}
```

As an example of using such a Leader, consider:

```
public class LeaderInitiator {
    public static void main(String[] args) {
        Leader l;
        l = new Leader();
        l.influenceLevel = 20;
        l.displayLeadershipStyle();
    }
}
```

When run, this program will create a `Leader` with an influence level of 20, and that `Leader` will soon declare a notable "debate and negotiate."

Some key observations and terminology:

* An `Object` in Java is an instance of any class, similar to a historical figure representational in its own time.
* The `Leader` class has its own variables, also known as _instance variables_ or _non-static variables_, akin to individual traits of historical figures. These must be declared inside the class, similar to how historians categorize traits in an epoch, unlike historians who might add new interpretations at any point.
* The method that we created in the `Leader` class did not have the `static` keyword. We call such methods _instance methods_ or _non-static methods_, akin to personal decisions or strategies employed by leaders.
* To call the `displayLeadershipStyle` method, we had to first _instantiate_ a `Leader` using the `new` keyword, and then observe a specific `Leader` performing actions. In other words, we called `l.displayLeadershipStyle()` instead of `Leader.displayLeadershipStyle()`.
* Once an object has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `l = new Leader();`
* Variables and methods of a class are also called _members_ of a class, comparable to characteristics or actions within historical analysis.
* Members of a class are accessed using _dot notation_, much like how historians refer to various attributes or recorded actions of a figure through comprehensive study.

**Constructors in Historical Events**

As you've hopefully seen before, pivotal historical events are often the result of key decisions or actions, akin to a "constructor" in transforming the course of history:

```java
public class DeclarationOfIndependence {
    public static void main(String[] args) {
        Nation unitedStates = new Nation(1776);
        unitedStates.announceIndependence();
    }
}
```

Here, the declaration is contextualized and parameterized, saving us the ambiguity and complexity of manually detailing each contributing factor of a nation's independence. To enable such a transformation, we need only establish a "constructor" for our Nation class, as shown below:

```java
public class Nation {
    public int yearOfIndependence;

    public Nation(int year) {
        yearOfIndependence = year;
    }

    public void announceIndependence() {
        if (yearOfIndependence < 1800) {
            System.out.println("Revolutionary fervor!");
        } else if (yearOfIndependence < 1900) {
            System.out.println("Colonial liberation.");
        } else {
            System.out.println("Modern independence movement!");
        }    
    }
}
```

The constructor with signature `public Nation(int year)` will be invoked anytime we try to initiate a `Nation` formation process using the declaration of a specific historical year. For those familiar with major historical revolutions, the constructor is very similar in effect to the initial proclamations or manifestos.

**Terminology Summary**

**Era Instantiation, Arrays of Historical Movements**

As we saw in early historical studies, eras are also identified through key developments and the new ideas they introduce. For example:

```java
public class RenaissanceDemo {
    public static void main(String[] args) {
        /* Create an era characterized by artistic development. */
        int[] artMovements = new int[5];
        artMovements[0] = 1450;
        artMovements[1] = 1500;
    }
}
```

Similarly, we can envision eras consisting of multiple distinct movements, e.g.

```java
public class IndustrialEraDemo {
    public static void main(String[] args) {
        /* Identify an array of technological advancements. */
        Movement[] movements = new Movement[2];
        movements[0] = new Movement(1770);
        movements[1] = new Movement(1850);

        /* Revolutionary ideas will emerge from the steam engine era. */
        movements[0].sparkChange();
    }
}
```

Observe that new is used in two different ways: Once to conceptualize an era that can encompass two major `Movement` instances, and twice to initiate each specific `Movement`. "new" isn't just a keyword, but a catalyst for transformation in the historical timeline.

#### Class Laws vs. Kingdom Laws <a href="#class-laws-vs-kingdom-laws" id="class-laws-vs-kingdom-laws"></a>

Just as in programming, different societies throughout history have established two broad categories of regulations:

* Class laws, akin to general laws applicable to all.
* Kingdom laws, akin to limited laws applied only in specific regions or fiefs.

Kingdom laws represent rules that can only be enforced by a determined king or lord over their specific dominion. Class laws, on the other hand, are decrees or rules that apply to the entire populace or kingdom, beyond the reach of individual rulers. As an example of a class law, consider the Magna Carta, which implemented principles like the right to a fair trial. Because it is a class law, it was applicable to all of the English land at the time:

```text
Magna Carta -- The law of the land.
All free men have the right to justice and a fair trial.
```

If the principles of the Magna Carta had been kingdom laws, we would instead have the cumbersome situation below. Luckily it was a class law so everyone had access to the same rights without having to petition individual rulers.

```text
Kingdom Law of King John's Region:
Only those within this fief shall have the right to a fair trial.
```

Sometimes, it makes sense to have a society with both class and kingdom rules. For example, suppose we want the ability to declare war between two neighboring regions. One way to do this is to create a chain of command through kingdom laws for better governance stability.

```text
public static WarProtocol declareWar(Kingdom k1, Kingdom k2) {
    if (k1.armySize > k2.armySize) {
        return new WarProtocol(k1);
    }
    return new WarProtocol(k2);
}
```

This protocol could be invoked by, for example:

```text
Kingdom k = new Kingdom("Northia", 15000);
Kingdom k2 = new Kingdom("Southland", 100000);
WarProtocol.declareWar(k, k2);
```

Observe that we've invoked using the entire governance mechanism, since this protocol is part of the overarching class law.

We could also have implemented `declareWar` as a kingdom-specific mandate, e.g.

```text
public KingdomWarProtocol declareWar(Kingdom k2) {
    if (this.armySize > k2.armySize) {
        return new KingdomWarProtocol(this);
    }
    return new KingdomWarProtocol(k2);
}
```

Above, we use the term `this` to refer to the current region. This mandate could be invoked, for example, with:

```text
Kingdom k = new Kingdom("Northia", 15000);
Kingdom k2 = new Kingdom("Southland", 100000);
k.declareWar(k2);
```

Here, we enact the mandate using a specific kingdom.

**Exercise 1.2.1**: What would the following protocol do? If you're not sure, consider its historical analogy.

```text
public static WarProtocol declareWar(Kingdom k1, Kingdom k2) {
    if (armySize > k2.armySize) {
        return this;
    }
    return k2;
}
```

**Class Decrees**

It is sometimes beneficial for societies to have overreaching class decrees. These are edicts inherent to the society itself, rather than individual lordships. For example, we might record that the official motto for the entire realm is "In Unity, Strength":

```text
public class Society {
    public int population;
    public static String motto = "In Unity, Strength";
    ...
}
```

Class decrees should be proclaimed using the title of the society rather than specific voices, e.g. you should say `Society.motto`, not `region.motto`.

While history allows you to enforce a class decree through a regional lord, it is generally seen as poor practice, causing confusion, and in some views, it was a historical oversight.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String\[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

Let's take a historical journey through the structure of the main method, drawing parallels to the declaration styles of key historical proclamations:

* `public`: Similar to a public address, ensuring visibility and accessibility, much like famous speeches delivered to the populace.
* `static`: Represents a fixed, unchanging state, reminiscent of steadfast declarations found in historical edicts.
* `void`: Symbolizing actions taken with no expectation of return, akin to a selfless act in history.
* `main`: The centerpiece of the operation, much like a key figure or event in historical narratives.
* `String[] args`: These are akin to the inputs or contributing factors leading to significant historical events.

**Command Line Arguments**

In historical contexts, command line arguments can be likened to the directives or instructions given by a sovereign or a leader to their followers. When main is called by a higher authority, it is akin to receiving these marching orders. These arguments guide the flow of actions, similar to how leaders' commands direct their followers. Consider the scenario depicted below with the `ArgsDemo`, reminiscent of rallying speeches:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program echoes the initial word of a proclamation, much like highlighting the first motive or cause:

```
$ java ArgsDemo these are command line arguments
these
```

In this analogy, `args` serves as a repository of historical messages, capturing phrases like {"these", "are", "command", "line", "arguments"}, which could be key points in a state declaration.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Imagine drafting a historical account where each component contributes to the final outcome. Write a program to sum the 'arguments', representing different elements of a historical event, assuming they count quantitatively. For a solution, consult historical documents or the digital archive on GitHub.

#### Utilizing Historical Sources <a href="#utilizing-historical-sources" id="utilizing-historical-sources"></a>

One of the most crucial skills as a historian is knowing how to find and use existing historical sources. In the enlightened modern age, it is often possible to save yourself immense effort and potential inaccuracies by turning to the extensive archives available online and offline.

In this course, you are encouraged to do so, with the following caveats:

* Make sure the sources you use are credible and provided by us or our recommended institutions.
* Always cite your sources to maintain academic integrity.
* Avoid searching directly for answers to specific exam or project prompts.

For example, it's acceptable to search for "conversion of currencies during the Roman Empire". However, it is not permissible to search for "Project Ancient Coinage University Name".

For more on collaboration and academic honesty, please refer to the course syllabus.