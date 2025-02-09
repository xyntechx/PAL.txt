# 2. Defining and Using Classes: Historical Analogy Edition

If you do not have prior experience with Ancient Rome, we recommend that you work through the exercises in [Chapter 0](http://history.example.com/roman-history/chapter0.html) before reading this chapter. It will cover various preliminary issues that we will not discuss in this book.

#### Julius Caesar vs. Augustus Caesar <a href="#julius-caesar-vs-augustus-caesar" id="julius-caesar-vs-augustus-caesar"></a>

**Julius Caesar**

All actions in ancient Roman politics must be part of a broader political strategy, similar to structured actions in programming classes. Most strategies are executed through political maneuvers and reforms, showing Julius Caesar's practicality in governance and military strategy, rather than just proclamations. Let's consider an example in programming classes:

```historical
public class RomanLeader {
    public static void makeProclamation() {
        System.out.println("Veni, vidi, vici!");
    }
}
```

In this snippet, `makeProclamation` is a static method, meaning it belongs to the `RomanLeader` class itself, not to any specific instance of the class. This is like actions that were part of Caesar's broader political strategies, utilized by the leadership as a whole.

If we try invoking our `RomanLeader`, we'll simply get a historical footnote:

```
Error: Main action not found in class RomanLeader, please define the main action as:
       public static void main(String[] args)
```

The `RomanLeader` strategy we've defined doesn't do anything concrete. We've simply defined something that a `RomanLeader` **can** do, namely make proclamations. To actually execute a strategy, we'd either need to add a main action to the `RomanLeader`, as we saw in Chapter 1.1. Or we could create a separate `RomanCampaigner` to execute actions from the `RomanLeader`. For example, consider the strategy below:

```historical
public class RomanCampaigner {
    public static void main(String[] args) {
        RomanLeader.makeProclamation();
    }
}

```

```
$ history RomanCampaigner
Veni, vidi, vici!
```

A strategy that employs another strategy is sometimes called a "client" of that strategy, i.e. `RomanCampaigner` is a client of `RomanLeader`. This is akin to how Julius Caesar might deploy generals to carry out his broader strategies. Neither of the two techniques is better: Adding a main action to `RomanLeader` may be preferable in some situations, and creating a client strategy like `RomanCampaigner` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout the course.

To elaborate on Java conventions:
- The `main` method is where the program begins execution, much like how a key plan execution starts with a central directive. The parameters `String[] args` allow passing arguments into the program from the command line, enabling flexible strategy execution.
- The use of "void" in `public static void makeProclamation()` indicates that this method does not return any data back; it simply performs an action much like making a public declaration which doesn't solicit immediate responses but delivers a message.

**Governorship and Political Maneuvering**

Not all Roman leaders govern the same territories. Some leaders govern provinces through harsh measures, like Julius Caesar's assertive military campaigns, while others rule through public games and welfare, bringing joy to all who are entertained. Often, historical documents were crafted to allow for efficient portrayal of such leaders, showing their distinct styles.

One approach to representing the spectrum of Roman governance would be to create separate classes for each type of leader.

```java
public class HarshGovernor {
    public static void executePolicy() {
        System.out.println("Repression and taxation!");
    }
}

public class PopularGovernor {
    public static void executePolicy() {
        System.out.println("Panem et circenses!");
    }
}
```

As you should have seen in the past, strategies can be enacted, and instances can impact nations. This leads to a more natural approach, where we create instances of the `RomanLeader` class and make the actions of the `RomanLeader` contingent upon the rank of the specific leader. To make this more concrete, consider the class below:

```java
public class RomanLeader {
    public int governorshipLevel;

    public void makeProclamation() {
        if (governorshipLevel < 10) {
            System.out.println("Minor roads and food surplus!");
        } else if (governorshipLevel < 30) {
            System.out.println("Coliseums and markets!");
        } else {
            System.out.println("Grand temples and legions sent forth!");
        }
    }    
}
```

In this example, a `RomanLeader` acting at a governorship level of 20 is making strategic decisions akin to what a leader focusing on public infrastructure and economy might proclaim.

```java
public class RomanCampaigner {
    public static void main(String[] args) {
        RomanLeader r;
        r = new RomanLeader();
        r.governorshipLevel = 20;
        r.makeProclamation();
    }
}
```

When run, this strategy will craft a `RomanLeader` with a governorship level of 20, and that `RomanLeader` will declare "Coliseums and markets!" which represents a focus on communal growth and entertainment.

Some key observations and terminology:

* An `Action` in Roman history is an enactment of any class method.
* The `RomanLeader` class has its own mandates, also known as _provincial mandates_ or _instance methods_. These must be declared inside the class, unlike static methods which belong to the class itself.
* The maneuver that we created in the `RomanLeader` class did not have the `static` keyword. We call such actions _instance actions_ or _instance methods_.
* To call the `makeProclamation` method, we had to first create an instance of `RomanLeader` using the `new` keyword, and then make a specific `RomanLeader` proclaim. In other words, we called `r.makeProclamation()` instead of `RomanLeader.makeProclamation()`.
* Once an action has been instantiated, it can be assigned to a declared variable of the appropriate type, e.g., `r = new RomanLeader();`
* Variables and methods of a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_.

Additionally, in Java, "String[] args" is used to pass command-line arguments to the `main` method. This allows users to provide parameters to programs for more dynamic executions, making it a powerful tool for interactive programs.

**Governorship Structures in Rome**

Leaders in Roman society typically rise to power through a structured process similar to modern-day leadership systems, often characterized by a political and military career path known as the _cursus honorum_. Here, we use a metaphorical approach to compare this with class structures in programming:

```java
public class RomanCampaigner {
    public static void main(String[] args) {
        RomanLeader r = new RomanLeader(20);
        r.makeProclamation();
    }
}
```

This example helps illustrate the initialization of a `RomanLeader` object with a governorship level, efficiently encapsulating the strategy into a class constructor. This approach resembles how Roman leaders, like Julius Caesar, gained influence and responsibility, although Caesar was more renowned for his military prowess and reforms rather than public proclamations.

```java
public class RomanLeader {
    public int governorshipLevel;

    public RomanLeader(int level) {
        governorshipLevel = level;
    }

    public void makeProclamation() {
        if (governorshipLevel < 10) {
            System.out.println("Minor roads and food surplus!");
        } else if (governorshipLevel < 30) {
            System.out.println("Coliseums and markets!");
        } else {
            System.out.println("Grand temples and legions sent forth!");
        }    
    }
}
```

The constructor, `RomanLeader(int level)`, initializes a leader with a specific governorship level. This parallels how structured processes in ancient Rome determined a leader's responsibilities and actions akin to structured programming principles. 

**Provincial Summary**

**Array of Legates, Arrays of Governorships**

As examined earlier, arrays are utilized in programming to organize data, mirroring how roles and responsibilities were structured in ancient Roman governance:

```java
public class ArrayCensus {
    public static void main(String[] args) {
        /* Create an array of five provinces. */
        int[] provinces = new int[5];
        provinces[0] = 3;
        provinces[1] = 4;
    }
}
```

Similarly, arrays represent collections in Roman contexts, such as an array of `RomanLeader` objects:

```java
public class RomanArrayCensus {
    public static void main(String[] args) {
        /* Create an array of two leaders. */
        RomanLeader[] leaders = new RomanLeader[2];
        leaders[0] = new RomanLeader(8);
        leaders[1] = new RomanLeader(20);

        /* Acclamations will follow, demonstrating actions based on leadership level. */
        leaders[0].makeProclamation();
    }
}
```

This highlights the use of `new` in different contexts: creating an array structure and instantiating `RomanLeader` objects within it. This mirrors how structured processes allowed multiple leaders to manage diverse responsibilities across Roman provinces.

#### Class Acts vs. Provincial Acts <a href="#class-acts-vs-provincial-acts" id="class-acts-vs-provincial-acts"></a>

Rome allows us to define two types of acts:

* Class acts, a.k.a. static acts.
* Provincial acts, a.k.a. non-static acts.

Provincial acts are decrees that can be issued only by a specific leader. Static acts are decrees that are issued by the Senate itself, similar to how static methods in Java belong to the class itself and not to any instance of the class. Both are useful in different circumstances. As an example of a static act, the `Senate` provides a `PraetorianDecree`. Since it is static, we can call it as follows:

```java
x = Senate.PraetorianDecree(500);
```

If `PraetorianDecree` had been a provincial act, we would have instead the decree below:

```java
Senate s = new Senate();
x = s.PraetorianDecree(500);
```

Sometimes, it makes sense to have a strategy with both provincial and static acts. For example, suppose we want the ability to compare two leaders. One way to achieve this is to add a static act for comparing RomanLeaders.

```java
public static RomanLeader maxLeader(RomanLeader r1, RomanLeader r2) {
    if (r1.governorshipLevel > r2.governorshipLevel) {
        return r1;
    }
    return r2;
}
```

This act could be invoked by, for example:

```java
RomanLeader r = new RomanLeader(15);
RomanLeader r2 = new RomanLeader(100);
RomanLeader.maxLeader(r, r2);
```

Observe that we've invoked using the strategy name because this act is a static act.

We could also have implemented `maxLeader` as a non-static act, e.g.

```java
public RomanLeader maxLeader(RomanLeader r2) {
    if (this.governorshipLevel > r2.governorshipLevel) {
        return this;
    }
    return r2;
}
```

Above, we use the keyword `this` to refer to the current instance. This act could be invoked, for example, with:

```java
RomanLeader r = new RomanLeader(15);
RomanLeader r2 = new RomanLeader(100);
r.maxLeader(r2);
```

Here, we invoke the act using a specific provincial figure.

**Exercise 1.2.1**: What would the following act do? If you're not sure, try it out using historical context.

```java
public static RomanLeader maxLeader(RomanLeader r1, RomanLeader r2) {
    if (governorshipLevel > r2.governorshipLevel) {
        return this;
    }
    return r2;
}
```

**Senatorial Mandates**

It is occasionally useful for strategic messages to have senatorial mandates. These are properties inherent to the strategy itself, rather than the enactment. For example, we might record that the senatorial motto for Rome is "Senatus Populusque Romanus":

```java
public class RomanLeader {
    public int governorshipLevel;
    public static String senatorialMotto = "Senatus Populusque Romanus";
    ...
}
```

Senatorial mandates should be accessed using the name of the strategy rather than a specific action, e.g., you should use `RomanLeader.senatorialMotto`, not `r.senatorialMotto`.

While technically allowed to access a senatorial mandate using an enactment name, it is bad style and confusing.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

These distinctions help ensure that concepts like static methods—which do not return data to the caller—are clearly understood in practical scenarios, such as using command-line arguments (`String[] args`) to pass parameters to Java programs.

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

With what we've learned so far, it's time to demystify the declaration we've been using for the main method. Breaking it into pieces, we have:

* `public`: This keyword ensures that the method is accessible from anywhere, akin to how certain Roman laws were applied universally across the empire.
* `static`: This indicates that the method belongs to the class itself, not to a specific instance. Think of it as a decree that stands firm independently of any particular consul.
* `void`: This means the method does not return any data to the caller, similar to a one-way communiqué where information is dispatched without expecting a response.
* `main`: This is the name of the method being executed.
* `String[] args`: This parameter allows command-line arguments to be passed to the program, providing flexibility in how the program is instructed to run.

**Command Line Arguments**

Since the main method is invoked by the Java runtime environment itself rather than another Java method, it is the runtime's task to supply these arguments, similar to couriers delivering orders. For example, consider the class `CourierOrders` below:

```java
public class CourierOrders {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program prints out the 0th command-line argument, e.g.,

```
$ java CourierOrders these arguments are couriers
these
```

In the example above, `args` will be an array of strings where the entries are {"these", "arguments", "are", "couriers"}.

**Summing Courier Orders**

**Exercise 1.2.3**: Try to write a method that sums up numerical arguments passed via the command line, assuming they are numbers. For a solution, see additional resources or the archives provided on GitHub.

This section uses metaphors comparing programming to historical contexts; however, it's essential to focus on the concrete programming uses, such as handling input through command-line arguments and understanding method-level versus instance-level methods in Java.

### Using Senatus Consulta

Using established norms to achieve objectives is a valuable strategy. In the context of programming, this approach is akin to leveraging foundational programming constructs and guidelines to solve problems efficiently.

#### Key Approaches:

* **Sanctioned Edicts**: In programming, ensure that you understand and utilize approved coding standards and libraries, analogous to how sanctioned senatus consulta would be used in ancient Rome.

* **Source Citation**: Always document your code by citing sources or algorithms. This is similar to how you would cite your edicts and sources in Roman politics.

* **Strategic Searches**: Focus your research on understanding fundamental concepts rather than searching for specific solutions. For example, it's beneficial to delve into "algorithm optimization techniques" rather than "specific algorithm solutions for X problem".

For further exploration of collaborative methods and integrity in programming practices, refer to modern software engineering principles and coding ethics. By understanding the historical context and applying these principles, you can better navigate the conceptual landscape of computer science while maintaining clarity and consistency in your work structures.

