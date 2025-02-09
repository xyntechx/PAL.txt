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

Imagine the programming world as a vast, meticulously detailed kingdom, much like the vast empires studied in history. Within the vast lands of this programming kingdom, there is a ceremonial court—the court of Java.

Java, much like the structured societies of ancient Rome or Greece, is built upon a set of strict rules and customs. To run any program in the Java kingdom, you must first partake in its fundamental ceremony—the grand invocation of "public static void main(String[] args)." This phrase is central to every Java program, akin to reciting an oath before a council.

1. **Public** - This term signifies openness. In the realm of Java, by declaring something as public, it is like announcing your intentions aloud in a public forum—available for all parts of the kingdom (or program) to access and interact with. It echoes ideas from history where open declarations or decrees were made in public squares.

2. **Static** - Imagine static as a solid cornerstone in a castle. It is fixed and unwavering. In computer programs, this word means that the method belongs to the class itself rather than an instance (or object) of the class, akin to how a law might apply to a nation-state rather than to its individual citizens.

3. **Void** - An echo of simplicity, void harkens back to the simple decree of "there shall be no return". In function, it means this method does not return any value, akin to a one-way communiqué.

4. **Main** - Serving as the herald of the program, the main method is the grand entrance to any execution in Java. It is the designated starting point, much like the crowning ceremony that officially begins a ruler’s reign or the opening of a city's gates to start a grand procession.

5. **String[] args** - These are your heralds' messengers—the words or proclamations that might be passed to the main method. Arguments can be seen as instructions from the emperor’s scrolls, detailing what this particular invocation of the Java court should accomplish.

Much like historians interpret speeches and declarations to understand the movements of empires, a programmer uses this string of words to understand and control the flow of their programs.

