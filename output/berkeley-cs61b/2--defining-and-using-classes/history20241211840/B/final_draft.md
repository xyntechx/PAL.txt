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

A class that uses another class is sometimes called a "client" of that class, i.e., `DogLauncher` is a client of `Dog`. Neither of the two techniques is better: Adding a main method to `Dog` may be better in some situations, and creating a client class like `DogLauncher` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout the course.

To understand these interactions without over-complicating the view, consider the historical analogy of governance in a kingdom. The `Dog` class is like an office or position of power within a government that has specific abilities or duties, similar to a minister. However, the king or ruling body (akin to a client class like `DogLauncher`) is needed to call upon and direct the minister to act in a way that affects the kingdom (our program). This client class therefore delegates and uses the methods of another class, implementing a clear action within the system. Similarly, when kings commanded ministers in history, it was understanding who holds power and how functions are executed that maintained the balance and ensured that the state operated effectively. Remember, like a minister, the `Dog` class on its own has potential, but it requires the organizational structure of a kingdom (the client) to cause that potential to manifest impacts (or outputs) in the realm of its program (the execution environment). This analogy should clarify rather than amplify complexity, emphasizing straightforward functionality relationships between classes.

**Instance Variables and Object Instantiation in Historical Context**

In history, leaders have often differed in their styles and approaches. Similarly, in Java programming, we can create different types of classes to represent varying attributes. For example, some leaders may govern with strict control, like an autocrat, whereas others inspire through vision and words, like a charismatic leader.

To illustrate this using Java, one could design representations for these distinct leadership types:

```java
public class AutocraticLeader {
    public static void executePolicies() {
        System.out.println("Enforce strict directives!");
    }
}

public class CharismaticLeader {
    public static void motivateNation() {
        System.out.println("Rally people with inspiration and vision!");
    }
}
```

However, this simplicity belies the complexity of leadership, much like the nuanced profiles of historical figures. By employing instance variables, we can create more realistic representations that embody unique characteristics of leaders.

Consider this Java class representing a generalized leader:

```java
public class Leader {
    public int influenceLevel;

    public void showLeadershipStyle() {
        if (influenceLevel < 10) {
            System.out.println("Control through authority!");
        } else if (influenceLevel < 30) {
            System.out.println("Discuss and persuade.");
        } else {
            System.out.println("Inspire and unite the people!");
        }
    }    
}
```

Instantiating a `Leader` class can provide insight into the approach of a particular leader, as seen in this example:

```java
public class LeaderDemo {
    public static void main(String[] args) {
        Leader leaderInstance = new Leader();
        leaderInstance.influenceLevel = 20;
        leaderInstance.showLeadershipStyle();
    }
}
```

Upon execution, this program represents a leader with an influence level of 20, who will rely on discussion and persuasion as his primary leadership style.

Some fundamental observations in these Java examples:

* An `Object` in Java refers to an instance of a class, much like a leader's representation in historical narratives.
* Instance variables, such as `influenceLevel`, define attributes specific to each instance, similar to unique characteristics attributed to historical figures.
* The `showLeadershipStyle` method is termed an instance method, which reflects decisions analogous to a leader's strategies.
* Object creation involves instantiation, achieved here with `new Leader()`, echoing the emergence and actions of individual leaders in particular contexts.
* Dot notation is crucial for accessing members (variables and methods) of a class, akin to accessing information about historical figures through detailed study.

These Java concepts mirror the intricate tapestry of history, offering a rich perspective on the design and function of classes and objects within the language.

**Constructors in Historical Events**

History, much like programming, is shaped by pivotal moments often dictated by crucial decisions, akin to how a "constructor" operates within object-oriented programming to set foundational parameters:

```java
public class DeclarationOfIndependence {
    public static void main(String[] args) {
        Nation unitedStates = new Nation(1776);
        unitedStates.announceIndependence();
    }
}
```

In this analogy, the act of declaring independence is organized within a structured context, eliminating the need for dissecting every underlying cause of the revolution independently. The establishment of a "constructor" for our Nation class sets the foundation for a new historical entity, as shown below:

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

The constructor `public Nation(int year)` automatically initializes a `Nation` using the particular historical year provided. This mirrors how significant declarations or manifestos historically set the stage for revolutionary transformations.

**Terminology Summary**

**Era Instantiation, Arrays of Historical Movements**

Just as programmers instantiate objects and arrays, historians identify eras by key developments and the innovations they bring forth. Consider the following:

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

Here, eras can be imagined as compilations of significant movements:

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

Notice how `new` is used to create both a conceptual framework for an era consisting of multiple `Movement` objects and individually instantiate each `Movement.` In programming, "new" is essential for creating instances; historically, it serves to illustrate transformation across time periods. Ensuring clarity in these parallels supports understanding of both disciplines.

#### Class Laws vs. Kingdom Laws <a href="#class-laws-vs-kingdom-laws" id="class-laws-vs-kingdom-laws"></a>

Throughout history, societies have operated under two core types of laws:

* Class laws, akin to universal statutes applicable throughout an empire.
* Kingdom laws, similar to local ordinances enforced within specific territories.

Kingdom laws were rules that a king or lord could enforce uniquely within their domain. Class laws transcended these local rulings, applying uniformly across the entire realm. For example, the Magna Carta established essential principles like the right to a fair trial. As a class law, it applied to every English subject universally:

```text
Magna Carta -- The law of the land.
All free men have the right to justice and a fair trial.
```

In contrast, if the Magna Carta were considered a kingdom law, various regions might have inconsistencies in rights and justice:

```text
Kingdom Law of King John's Region:
Only those within this fief shall have the right to a fair trial.
```

Often, blending class and kingdom laws makes governance adaptive yet cohesive. For example, handling warfare might require a hierarchy through kingdom laws to maintain regional stability. Consider the following simplified Java function:

```java
public static WarProtocol declareWar(Kingdom k1, Kingdom k2) {
    if (k1.armySize > k2.armySize) {
        return new WarProtocol(k1);
    }
    return new WarProtocol(k2);
}
```

This protocol allows decision-making based on collective military strength rather than isolated commands.

We might also have a kingdom-specific implementation:

```java
public KingdomWarProtocol declareWar(Kingdom k2) {
    if (this.armySize > k2.armySize) {
        return new KingdomWarProtocol(this);
    }
    return new KingdomWarProtocol(k2);
}
```

Here, `this` signifies the current kingdom engaging in the war declaration, highlighting localized operations.

**Exercise 1.2.1**: What implications does this protocol have?

```java
public static WarProtocol declareWar(Kingdom k1, Kingdom k2) {
    if (armySize > k2.armySize) {
        return this;
    }
    return k2;
}
```

**Class Decrees**

Class decrees serve to standardize policies across society. These enduring edicts are rooted in the society's fabric rather than individual rulers' whims. For instance, declaring a society-wide motto, like "In Unity, Strength," can set a consistent cultural tone:

```java
public class Society {
    public int population;
    public static String motto = "In Unity, Strength";
    // other members
}
```

It is best practice to refer to such decrees by the larger society rather than a singular locality, ensuring consistency and clarity.

**Exercise 1.2.2**: Reflect on how consistent class decrees strengthen societal unity.

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

In modern coding, akin to significant declarations throughout history, the `main` method serves a pivotal role. Let's explore its structure through both programming and historical lenses:

* `public`: Ensures visibility and accessibility, much like public decrees that were meant for all citizens, ensuring transparency and widespread knowledge.
* `static`: Signifies a fixed, consistent state, akin to the unwavering commitments made in historical charters or treaties, establishing rules that remain constant over time.
* `void`: Indicates an action that completes without returning a result, comparable to altruistic deeds in history where the focus was solely on the benefit to others, not personal gain.
* `main`: As the central entry point, it can be compared to a pivotal event or leader in history that initiates a significant change or movement.
* `String[] args`: Similar to the advice or information given to leaders by their councils, these arguments serve as input that can alter the program's behavior, reflecting the diverse influences shaping historical decisions.

**Command Line Arguments**

In historical contexts, command line arguments are like the directives issued by leaders, guiding their followers' actions. When `main` is invoked, it's akin to receiving specific guidance to proceed. These arguments dictate the program's flow, paralleling how strategic commands shape historical outcomes. Consider the `ArgsDemo` below, representing this clarity of instruction:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program showcases the initial input, much like the opening remarks of a historic doctrine or address:

```
$ java ArgsDemo these are command line arguments
these
```

Here, `args` operates as a collection of inputs, akin to capturing the essential elements of a historical document, such as "these", "are", "command", "line", "arguments".

**Summing Command Line Arguments**

**Exercise 1.2.3**: Imagine constructing a historical analysis, where each input element contributes to a comprehensive outcome. Develop a program to sum the 'arguments', representing various aspects of a historical event, assuming numeric values for simplicity. For assistance, consult historical records or explore additional resources such as online archives.

#### Utilizing Historical Sources in Computer Science <a href="#utilizing-historical-sources" id="utilizing-historical-sources"></a>

Navigating historical resources is similar to querying a database efficiently in computer science. Just as a historian seeks credible records to construct an accurate representation of the past, a computer scientist must adeptly utilize existing digital archives and documentation to problem-solve and innovate. The parallels between these disciplines can enrich our approach to both.

In this course, it is encouraged to draw from a wide array of historical and computational resources, with the following considerations:

* **Source Credibility:** Ensure that the data, whether historical texts or coding libraries, is reliable. Use resources recommended by the course or verified institutions.
* **Citation and Documentation:** Maintain transparency and academic integrity by appropriately citing sources, whether they are historical records or software documentation.
* **Focused Research:** Aim to conduct research to understand the broader concepts rather than seeking verbatim solutions for specific tasks, just like building algorithms and not merely copying code.

For instance, researching "historical data structures like the Incan quipus" could provide insights into how civilizations stored data, similar to understanding "data structures used in computing". However, searching for "Exam Programming Structure University Name" to find answers is not advisable.

Refer to the course syllabus for more on collaboration, proper referencing, and academic honesty within the context of both historical studies and computer science principles.