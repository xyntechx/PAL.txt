# Understanding Static and Non-Static Methods

In this chapter, we explore the distinctions between static and non-static methods within Java, using historical analogies to contextualize their functionalities and applications. Static methods are likened to decrees issued by a historical governing body, such as an empire or a centralized authority, where commands are universally accessible without requiring specific instances. An example is the mathematical operation `Math.sqrt`, which operates without needing a specific object. These methods are integral to managing broad, consistent operations across the application.

In contrast, non-static or instance methods are compared to actions taken by individual leaders or local governors. These require an instance to function, similar to how a local ruler acts within its jurisdiction. Through the creation and management of objects using constructors, Java enables more nuanced and specific operations tailored to particular instances, much like appointed leaders tailor their actions to local needs. This chapter covers the instantiation of objects, the role of constructors, and the execution of both static and non-static methods, along with best practices in accessing static variables. This grounding in historical perspectives provides a richer understanding of how these concepts integrate into broader programming paradigms.

#### Static vs. Non-Static Methods in Historical Context <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

In programming languages like Java, the structure of code can be likened to the organization of historical empires, with static methods akin to centralized decrees that apply universally, regardless of individual entities. Imagine the Roman Empire, where laws were applied throughout, irrespective of local custom. Similarly, static methods in Java belong to the class level and can be invoked without the need for creating an instance of that class. Consider an example of such a method:

```java
public class Dog {
    public static void makeNoise() {
        System.out.println("Bark!");
    }
}
```

Attempting to run the `Dog` class without a central point of command would result in confusion, much like issuing a decree without an emperor's signature:

```
$ java Dog
Error: Main method not found in class Dog, please define the main method as:
       public static void main(String[] args)
```

This error highlights the requirement of a `main` method, which acts as the emperor executing the decree. To make the static method functional, we might introduce a `DogLauncher` class, akin to a general carrying out the emperor's orders, ensuring instructions reach their destination:

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

Creating a `DogLauncher` class to utilize the `Dog` class reflects how lesser states or regions implemented overarching laws. This decentralized execution can have strategic advantages similar to regional governors providing efficient local governance. Embedding a main method within `Dog` might be more efficient for small, direct applications, comparable to a chief executing orders without additional intermediaries. Both methods showcase different strategies in historical and technical contexts, each suitable for specific scenarios that will be explored later in this course.

**Instance Variables and Object Instantiation**

Throughout history, leaders have varied as distinctly as the kingdoms they rule. Some impose their will with iron-fisted decrees, while others inspire unity through wisdom and understanding. This array of leadership styles suggests a parallel to how we might structure objects in programming to reflect such diversity.

To begin representing various historical leaders, one might create separate classes for specific types of rulers, similar to distinguishing between monarchs and philosopher kings in the chronicles of ancient times:

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

Just as historians categorize rulers by their defining traits, programmers can define characteristics within a class to encapsulate a ruler's attributes and behaviors using instance variables. This allows us to create instances of the `Ruler` class where methods like `proclaimEdict` vary according to the specific ruler's traits:

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

In practice, such a ruler might be observed in the following manner:

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

With a wisdom level of 20, this `Ruler` advises "Balance power with trust." Thus encapsulating the philosophy of a moderate leader.

Key observations and terminology relevant to this programming analogy include:

* An `Object` in Java is an instance of any class, akin to a realized historical figure in a narrative.
* Instance variables, such as `wisdomLevel`, define the unique traits of an object, paralleling the aspects defining individual rulers.
* Methods without the `static` keyword are instance methods, representing behaviors reliant on an object's state, much like leadership decisions contingent on a ruler’s wisdom.
* Instantiation is crucial before an object like `Ruler` can act, akin to how a leader must first rise to power.
* Once instantiated, an object is associated with a declared variable, much like appointing a leader to their office.
* Members of a class, both variables and methods, are accessed using dot notation, allowing interaction with an object’s capabilities and attributes.

**Constructors in the Historical Context**

Just as empires of the past were built on a solid foundation of organization and leadership, in object-oriented programming, objects are created using a _constructor_, which serves as the blueprint:

```java
public class DogLauncher {
    public static void main(String[] args) {
        Dog d = new Dog(20);
        d.makeNoise();
    }
}
```

Much like how an effective leader organizes their followers around a central cause, parameterized constructors streamline the creation of objects by unifying the initialization process. To build this foundational system for our `Dog` class, a constructor must be established:

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

The constructor `public Dog(int w)` is invoked each time a `Dog` object is created using the `new` keyword and a single integer parameter, similar to how an artisan uses specific tools and resources to create unique works. For those familiar with Python, the constructor is akin to the `__init__` function, serving a similar purpose in object initialization.

**Terminology Summary**

**Array Instantiation, Arrays of Objects**

Just as architects laid the groundwork for great cities, arrays in Java are initialized using the `new` keyword, forming building blocks for more complex structures:

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

Similarly, creating arrays of objects in Java is like organizing units of an ancient army, each with distinct roles yet part of a cohesive whole:

```java
public class DogArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two dogs. */
        Dog[] dogs = new Dog[2];
        dogs[0] = new Dog(8);
        dogs[1] = new Dog(20);

        /* Ensures each dog performs its role, as dogs[0] has weight 8. */
        dogs[0].makeNoise();
    }
}
```

Notice how `new` serves a dual purpose: it constructs an array to hold two `Dog` objects and then individually creates each `Dog`, reminiscent of a leader mustering forces and assigning specific tasks to each member. This dual action echoes the precision and organization crucial to both programming and historical endeavors.

#### Class Methods vs. Instance Methods in Historical Contexts <a href="#class-methods-vs-instance-methods-in-historical-contexts" id="class-methods-vs-instance-methods-in-historical-contexts"></a>

Java, much like key political frameworks that shaped eras, employs two types of methods that impact programming architecture:

* **Class methods**, also known as static methods, resemble proclamations issued by a central government, applying uniformly.
* **Instance methods**, known as non-static methods, parallel localized decrees made by individual leaders.

Instance methods are akin to actions a specific king might take, much like a treaty tailored to local needs. Static methods act as broad mandates—consider the Magna Carta’s universal principles. Take the static method `Math.sqrt`, which functions like Roman legal tenets that transcend local application:

```java
x = Math.sqrt(100);
```

If `sqrt` were an instance method—a localized treaty—each province would uniquely proclaim it. Thankfully, it stands as a static decree:

```java
Math m = new Math();
x = m.sqrt(100);
```

In history, broad policies coexist with local initiatives. Comparing the might of two city-states might utilize a method like `maxDog` in a unified decision:

```java
public static Dog maxDog(Dog d1, Dog d2) {
    if (d1.weightInPounds > d2.weightInPounds) {
        return d1;
    }
    return d2;
}
```

This choice is akin to a universal agreement, calling upon a council's judgment:

```java
Dog d = new Dog(15);
Dog d2 = new Dog(100);
Dog.maxDog(d, d2);
```

Here, we invoke a decision through the council's name, underlining its status as a global judgment.

Alternatively, consider personalized governance—a leader’s subjective decision through an instance method like `maxDog` within one jurisdiction:

```java
public Dog maxDog(Dog d2) {
    if (this.weightInPounds > d2.weightInPounds) {
        return this;
    }
    return d2;
}
```

Here, `this` embodies the current ruler, executed locally by:

```java
Dog d = new Dog(15);
Dog d2 = new Dog(100);
d.maxDog(d2);
```

The judgment reflects a leader’s personalized decision.

**Exercise 1.2.1**: Analyze what this council decree would execute. If unsure, test it in a historical emulation.

```java
public static Dog maxDog(Dog d1, Dog d2) {
    if (weightInPounds > d2.weightInPounds) {
        return this;
    }
    return d2;
}
```

**Static Variables and Universal Principles**

Like the timeless accolades of medieval monarchy, certain class attributes should be static—these are constants within a realm. The scientific name of Dogs, `Canis familiaris`, is akin to a realm’s decree:

```java
public class Dog {
    public int weightInPounds;
    public static String binomen = "Canis familiaris";
    ...
}
```

Access static variables using the dynasty or species name, `Dog.binomen`, evocative of referencing "The Edict of Milan" by title rather than its promulgator.

Though some documents note royal proclamations by subordinate provinces, it is considered anachronistic and, in historical scrutiny, a lapse in the chronicler’s diligence.

**Exercise 1.2.2**: Extend this historical-technical analysis:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### The Dawn of "public static void main(String[] args)" <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

With the foundational concepts in place, let's delve into the main method declaration by drawing parallels to historical ideas. Each component can be seen as fulfilling key roles reminiscent of ancient societal structures:

* `public`: Much like public forums in ancient Rome where decisions were shared with the populace, this keyword signifies that our methods are open for communal interaction within the Java "empire."
* `static`: Analogous to enduring monuments that symbolize enduring principles, this term denotes a method that remains constant, untethered to individual instances, akin to a timeless maxim.
* `void`: Just as many ceremonies were conducted for their inherent value, this term indicates that our method completes its role without the need for compensation.
* `main`: As the sovereign presides over a domain, this method oversees and orchestrates the class's operations.
* `String[] args`: These are akin to heralds conveying vital messages to the method, much like envoys bringing counsel or directives to a ruler.

**Command Line Arguments as Council Advisories**

The main method is invoked by the powerful Java interpreter, charged with handling "arguments"—akin to counsel or propositions presented during a council assembly. These often refer to advisories delivered at the command threshold (line). Explore the historical reenactment in `ArgsDemo`:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program announces the 0th argument, much like declaring the first of several ordinances from the council chamber:

```
$ java ArgsDemo these are command line arguments
these
```

In our illustrative narrative, `args` acts as a scroll of decrees, each entry representing an individual line in this scroll: {"these", "are", "command", "line", "arguments"}.

**Counting Council Advisories**

**Exercise 1.2.3**: Envision crafting a program that calculates the total of the council's advisories (arguments as numbers). For guidance on such calculations, refer to archived documentation or explore the digital repository within our code library.

#### Learning from History <a href="#learning-from-history" id="learning-from-history"></a>

One of the most important skills for computer scientists is learning from past technological developments and methodologies, akin to how historians delve into historical sources to gain insights into human civilization. Just as historians explore the annals of recorded history for clarity and understanding, computer scientists scrutinize past projects and read the documentation to draw lessons that could shape future innovations.

In your exploration, consider the following guidelines:

* Utilize the recommended documentation and resources to understand foundational technology concepts.
* Cite any resources you reference in your work.
* Focus on the principles and patterns demonstrated in these sources instead of searching for cookie-cutter solutions to problems.

For example, researching general concepts such as "object-oriented programming principles" is encouraged, much like a historian studying "Victorian Era innovations". However, seeking out a specific coded solution online undermines the learning process, similar to a historian simply copying an analysis of a historical event without original thought.

For more guidelines on academic integrity and collaboration expectations, please refer to the course syllabus.