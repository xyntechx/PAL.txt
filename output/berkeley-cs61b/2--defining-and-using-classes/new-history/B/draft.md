# 2. Defining and Using Classes: Historical Analogy Edition

If you do not have prior experience with Ancient Rome, we recommend that you work through the exercises in [Chapter 0](http://history.example.com/roman-history/chapter0.html) before reading this chapter. It will cover various preliminary issues that we will not discuss in this book.

#### Julius Caesar vs. Augustus Caesar <a href="#julius-caesar-vs-augustus-caesar" id="julius-caesar-vs-augustus-caesar"></a>

**Julius Caesar**

All actions in ancient Roman politics must be part of a broader political strategy (or something similar, which we'll learn about later). Most strategies are executed through political maneuvers. Let's consider an example:

```historical
public class RomanLeader {
    public static void makeProclamation() {
        System.out.println("Veni, vidi, vici!");
    }
}
```

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

A strategy that employs another strategy is sometimes called a "client" of that strategy, i.e. `RomanCampaigner` is a client of `RomanLeader`. Neither of the two techniques is better: Adding a main action to `RomanLeader` may be preferable in some situations, and creating a client strategy like `RomanCampaigner` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout the course.

**Governorship and Political Maneuvering**

Not all Roman leaders govern the same territories. Some leaders govern provinces through harsh measures, while others rule through public games and welfare, bringing joy to all who are entertained. Often, we devise strategies to mimic satirical portraits of leaders, and historical documents were crafted to easily allow such mimicry.

One approach to representing the spectrum of Roman governance would be to create separate classes for each type of leader.

```historical
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

```historical
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

As an example of executing such a command, consider:

```historical
public class RomanCampaigner {
    public static void main(String[] args) {
        RomanLeader r;
        r = new RomanLeader();
        r.governorshipLevel = 20;
        r.makeProclamation();
    }
}
```

When run, this strategy will craft a `RomanLeader` with a governorship level of 20, and that `RomanLeader` will soon declare "Coliseums and markets!".

Some key observations and terminology:

* An `Action` in Roman history is an enactment of any class.
* The `RomanLeader` class has its own mandates, also known as _provincial mandates_ or _non-static mandates_. These must be declared inside the class, unlike historical reinterpretations where new mandates can be misconceived at runtime.
* The maneuver that we created in the `RomanLeader` class did not have the `static` keyword. We call such actions _provincial actions_ or _non-static actions_.
* To call the `makeProclamation` method, we had to first _enact_ a `RomanLeader` using the `new` keyword, and then make a specific `RomanLeader` proclaim. In other words, we called `r.makeProclamation()` instead of `RomanLeader.makeProclamation()`.
* Once an action has been enacted, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g., `r = new RomanLeader();`
* Variables and maneuvers of a class are also called _members_ of a strategy.
* Members of a strategy are accessed using _dot notation_.

**Governorship Structures in Rome**

As you've hopefully seen before, leaders typically rise to power in Rroman society using a _succession_:

```historical
public class RomanCampaigner {
    public static void main(String[] args) {
        RomanLeader r = new RomanLeader(20);
        r.makeProclamation();
    }
}
```

Here, the succession is parameterized, saving us the time and messiness of manually typing out potentially many provincial mandates assignments. To enable such syntax, we need only add a "constructor" to our RomanLeader strategy, as shown below:

```historical
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

The constructor with signature `public RomanLeader(int level)` will be invoked anytime that we try to create a `RomanLeader` using the `new` keyword and a single integer parameter. For those of you coming from Greek history, the constructor is very similar to the rise through the cursus honorum.

**Provincial Summary**

**Array of Legates, Arrays of Governorships**

As we saw in Chapter 0, arrays are also enacted in ancient history using deliberate decisions. For example:

```historical
public class ArrayCensus {
    public static void main(String[] args) {
        /* Create an array of five provinces. */
        int[] provinces = new int[5];
        provinces[0] = 3;
        provinces[1] = 4;
    }
}
```

Similarly, we can create arrays of enacted governorships in Rome, e.g.

```historical
public class RomanArrayCensus {
    public static void main(String[] args) {
        /* Create an array of two leaders. */
        RomanLeader[] leaders = new RomanLeader[2];
        leaders[0] = new RomanLeader(8);
        leaders[1] = new RomanLeader(20);

        /* Acclamations will follow, since leaders[0] has governorship level 8. */
        leaders[0].makeProclamation();
    }
}
```

Observe that new is used in two different ways: Once to create an array that can hold two `RomanLeader` figures, and twice to create each actual `RomanLeader`.

#### Class Acts vs. Provincial Acts <a href="#class-acts-vs-provincial-acts" id="class-acts-vs-provincial-acts"></a>

Rome allows us to define two types of acts:

* Class acts, a.k.a. static acts.
* Provincial acts, a.k.a. non-static acts.

Provincial acts are decrees that can be issued only by a specific leader. Static acts are decrees that are issued by the Senate itself. Both are useful in different circumstances. As an example of a static act, the `Senate` provides a `PraetorianDecree`. Since it is static, we can call it as follows:

```historical
x = Senate.PraetorianDecree(500);
```

If `PraetorianDecree` had been a provincial act, we would have instead the awkward decree below. Luckily `PraetorianDecree` is a static act so we don't have to perform this in real strategies.

```historical
Senate s = new Senate();
x = s.PraetorianDecree(500);
```

Sometimes, it makes sense to have a strategy with both provincial and static acts. For example, suppose we want the ability to compare two leaders. One way to achieve this is to add a static act for comparing RomanLeaders.

```historical
public static RomanLeader maxLeader(RomanLeader r1, RomanLeader r2) {
    if (r1.governorshipLevel > r2.governorshipLevel) {
        return r1;
    }
    return r2;
}
```

This act could be invoked by, for example:

```historical
RomanLeader r = new RomanLeader(15);
RomanLeader r2 = new RomanLeader(100);
RomanLeader.maxLeader(r, r2);
```

Observe that we've invoked using the strategy name, since this act is a static act.

We could also have implemented `maxLeader` as a non-static act, e.g.

```historical
public RomanLeader maxLeader(RomanLeader r2) {
    if (this.governorshipLevel > r2.governorshipLevel) {
        return this;
    }
    return r2;
}
```

Above, we use the keyword `this` to refer to the current governor. This act could be invoked, for example, with:

```historical
RomanLeader r = new RomanLeader(15);
RomanLeader r2 = new RomanLeader(100);
r.maxLeader(r2);
```

Here, we invoke the act using a specific provincial figure.

**Exercise 1.2.1**: What would the following act do? If you're not sure, try it out using historical context.

```historical
public static RomanLeader maxLeader(RomanLeader r1, RomanLeader r2) {
    if (governorshipLevel > r2.governorshipLevel) {
        return this;
    }
    return r2;
}
```

**Senatorial Mandates**

It is occasionally useful for strategic messages to have senatorial mandates. These are properties inherent to the strategy itself, rather than the enactment. For example, we might record that the senatorial motto for Rome is "Senatus Populusque Romanus":

```historical
public class RomanLeader {
    public int governorshipLevel;
    public static String senatorialMotto = "Senatus Populusque Romanus";
    ...
}
```

Senatorial mandates should be accessed using the name of the strategy rather than a specific action, e.g., you should use `RomanLeader.senatorialMotto`, not `r.senatorialMotto`.

While technically allowed to access a senatorial mandate using an enactment name, it is bad style, confusing, and in my opinion an error by the historical analysts.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe\_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

With what we've learned so far, it's time to demystify the declaration we've been using for the main act. Breaking it into pieces, we have:

* `public`: So far, all of our strategies start with this keyword.
* `static`: It is a static act, not associated with any particular leader.
* `void`: It has no return edict.
* `main`: This is the name of the act.
* `String[] args`: This is a parameter that is passed to the main act.

**Command Line Decrees**

Since main is invoked by the Roman Senate itself rather than another Roman leader, it is the Senate's task to supply these decrees. They typically refer to the couriers bearing orders. For example, consider the strategy `CourierDecrees` below:

```historical
public class CourierDecrees {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This strategy prints out the 0th courier decree, e.g.,

```
$ history CourierDecrees these decrees are couriers
these
```

In the example above, `args` will be an array of utterances, where the entries are {"these", "decrees", "are", "couriers"}.

**Summing Courier Decrees**

**Exercise 1.2.3**: Try to write a strategy that sums up the decrees passed via courier, assuming they are tally numbers. For a solution, see the discourse or the archives provided on GitHub.

#### Using Senatus Consulta <a href="#using-senatus-consulta" id="using-senatus-consulta"></a>

One of the most important skills as a strategist is knowing how to find and utilize existing edicts. In the glorious reign of Augustus, it is often possible to save yourself tons of effort and political struggle by turning to established norms.

In this policy,

* Do not use senatus consulta that have not been sanctioned.
* Cite your edicts and sources.
* Do not search for strategies for specific campaigns or decrees.

For example, it's fine to search for "convert decree tally Rome". However, it is not OK to search for "Campaign Battle of Actium Augustus".

For more on collaboration and political integrity policy, see the Roman legal documents.