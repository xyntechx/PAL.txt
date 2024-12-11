# Introduction to Object-Oriented Programming in Java

This chapter introduces key object-oriented programming concepts using analogies from microeconomics, focusing primarily on Java. It begins by likening a company's production methods to static methods in Java, explaining how these methods, while defined within a class, require external triggers to execute, much like businesses need a market to sell their products. The chapter then draws parallels between consumer behavior and object instantiation, illustrating how classes in Java can encapsulate diverse characteristics and preferences through instance variables and methods. This provides a foundation for understanding how real-world behaviors and economic models can be translated into software design using Java's object-oriented features.

Further, the text explains the significance of constructors, which are used to create objects with specific states or attributes, akin to consumer choices influenced by budget constraints. Through practical Java code snippets, the material illustrates how objects can be tailored to represent real-world entities, enhancing the software's ability to simulate complex systems. The chapter also discusses the different roles of class methods (static methods) and instance methods, comparing their usage and benefits to public and private goods in microeconomics. It ends with a detailed explanation of the syntax and functionality of the `main` method in Java, drawing comparisons to centralized planning in economics, and emphasizes the importance of using existing libraries to streamline development, cautioning against unethical programming practices to maintain fairness and integrity, akin to market regulations.



In microeconomics, consider a company (class) that produces a specific product (method). This company has defined methods (static methods in CS) that dictate its capacity to make products without requiring specific resources beyond the initial setup. For instance, if a company's operation (method) is to produce widgets, this static method illustrates the potential activity of widget production. However, without a market to sell these products, the method remains unused – analogous to the `Dog` class where the noise-making function exists but doesn't execute by itself.

To bring this static method or company operation to life, similar to how you need a `DogLauncher`, the company may need a sales team or client base to trigger the production process. The `DogLauncher` acts as a marketplace or consumer entity that initiates the process, allowing the static method to perform its function – much like how market demand triggers production in an economic sense. 

In some economic scenarios, aligning sales operations within the company could streamline production, while in others, an external sales force might be advantageous. This decision is akin to choosing between integrating a main method within the `Dog` class for centralized control or utilizing an external `DogLauncher` class to isolate responsibilities and possibly optimize processes. The decision on which approach to take depends on the company's strategic objectives and efficiency analyses, paralleling the programming practice where relative advantages of different approaches become clear with experience and context.



**Instance Variables and Object Instantiation with Microeconomics Analogies**

Not all consumer preferences are alike. Some consumers have a high preference for goods that offer utility through status, while others find joy in goods that provide comfort and reliability. Often, economic models are developed to mimic features of the market we study, and programming languages such as Java provide syntax that allows for such representations easily.

One approach to representing the spectrum of consumer preferences would be to create separate classes for each type of Consumer Utility.

```java
public class LuxuryConsumer {
    public static void expressPreference() {
        System.out.println("I love high-end brands!");
    }
}

public class BudgetConsumer {
    public static void expressPreference() {
        System.out.println("I always hunt for deals!");
    }
}
```

As you should have seen in the past, classes can be instantiated, and instances can hold data closely associated with them. This leads to a more realistic approach, where we create instances of the `Consumer` class and make the behavior of the `Consumer` methods contingent upon the characteristics of the specific `Consumer`. To better illustrate this, consider the class below:

```java
public class Consumer {
    public double budget;

    public void expressPreference() {
        if (budget < 1000) {
            System.out.println("I prefer budget-friendly options!");
        } else if (budget < 5000) {
            System.out.println("I enjoy a good balance of price and quality.");
        } else {
            System.out.println("I value luxury and premium quality!");
        }
    }    
}
```

As an example of using such a Consumer, consider:

```java
public class ConsumerMarket {
    public static void main(String[] args) {
        Consumer c;
        c = new Consumer();
        c.budget = 3000;
        c.expressPreference();
    }
}
```

When run, this program will create a `Consumer` with a budget of 3000, and that `Consumer` will express their preference for goods that offer a good balance of price and quality.

Some key observations and terminology:

* An `Object` in Java is an instance of any market participant.
* The `Consumer` class has its own variables, also known as _instance variables_ or _non-static variables_. These must be declared inside the class, unlike interpretations in some other languages or models, where new variables can be introduced spontaneously.
* The method created in the `Consumer` class did not have the `static` keyword. We call such methods _instance methods_ or _non-static methods_.
* To activate the `expressPreference` method, we had to first _instantiate_ a `Consumer` using the `new` keyword, and then have a specific `Consumer` assess the market. In other words, we called `c.expressPreference()` instead of `Consumer.expressPreference()`.
* Once an object has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `c = new Consumer();`
* Variables and methods of a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_.

Just like in microeconomics, where consumer preferences and budgets determine market choices, instance variables and methods allow objects to represent the diversity of behaviors and characteristics within a program.

## Constructors and Consumer Choices in Java

As you've hopefully seen before, just like consumers make choices under limited resources, we usually construct objects in object-oriented languages using a _constructor_ to optimize our use of resources:

```java
public class DogLauncher {
    public static void main(String[] args) {
        Dog d = new Dog(20);
        d.makeNoise();
    }
}
```

Here, the instantiation is parameterized, much like a consumer choosing goods based on budget constraints and utility functions, saving us the time and messiness of manually typing out potentially many instance variable assignments. To enable such syntax, we need only add a "constructor" to our Dog class, as shown below:

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

Just as consumers will maximize their utility given a price constraint, the constructor with signature `public Dog(int w)` will be invoked anytime that we try to create a `Dog` using the `new` keyword and a single integer parameter, initializing the object efficiently under specified conditions. For those of you coming from Python, the constructor is very similar to the `__init__` method.

## Terminology Summary with Production Analogy

**Array Instantiation, Arrays of Objects, and Production Functions**

As we saw in HW0, arrays are also instantiated in Java using the new keyword, similar to how a firm might allocate inputs to produce outputs. For example:

```java
public class ArrayDemo {
    public static main(String[] args) {
        /* Create an array of five integers. */
        int[] someArray = new int[5];
        someArray[0] = 3;
        someArray[1] = 4;
    }
}
```

Similarly, we can create arrays of instantiated objects in Java, equating to a firm producing a variety of goods:

```java
public class DogArrayDemo {
    public static main(String[] args) {
        /* Create an array of two dogs, representing diverse product offerings. */
        Dog[] dogs = new Dog[2];
        dogs[0] = new Dog(8);
        dogs[1] = new Dog(20);

        /* Yipping will result, simulating consumer feedback, since dogs[0] has weight 8. */
        dogs[0].makeNoise();
    }
}
```

Observe that `new` is used in two different ways: Once to create an array that can hold two `Dog` objects, analogous to setting up a production process for two goods, and twice to create each actual `Dog`, akin to finalizing the output based on optimized input use.

#### Class Methods vs. Instance Methods: An Economic Perspective <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

When considering class methods and instance methods, we can apply microeconomic principles to understand their utility, efficiency, and specialization.

* **Class Methods** (static methods) can be seen as public goods within a class—available to all instances just like roads or electricity. They provide utility across the board without needing to be adjusted for individual instances.
* **Instance Methods** (non-static methods) are akin to personalized goods or services, tailored specifically for each unit (or instance) of the class, such as made-to-measure clothing.

Instance methods, therefore, represent functions subject to diminishing marginal utility to specific objects, whereas static methods serve universal purposes across all instances, optimizing accessibility akin to "club goods".

For instance, consider the static `sqrt` method from the `Math` class. It is a shared resource accessible universally as follows:

```java
x = Math.sqrt(100);
```

If `sqrt` were an instance method, each user (or instance) would need to create their own version—a less efficient allocation of resources reminiscent of individual car ownership versus public transport.

```java
Math m = new Math();
x = m.sqrt(100);
```

In certain scenarios, combining shared resources (static methods) with individualized solutions (instance methods) maximizes overall utility, much as diverse goods and services cater to different market segments. Consider a static method that compares two dogs, evaluating them just like a consumer might evaluate different goods.

```java
public static Dog maxDog(Dog d1, Dog d2) {
    if (d1.weightInPounds > d2.weightInPounds) {
        return d1;
    }
    return d2;
}
```

This method is a utility-maximizing function available to all dogs within the market (i.e., class), invoked simply as:

```java
Dog d = new Dog(15);
Dog d2 = new Dog(100);
Dog.maxDog(d, d2);
```

Conversely, implementing `maxDog` as an instance method reflects a customized service approach, akin to one-on-one consulting services in microeconomics.

```java
public Dog maxDog(Dog d2) {
    if (this.weightInPounds > d2.weightInPounds) {
        return this;
    }
    return d2;
}
```

We can invoke this method in a personalized manner using a specific instance variable, demonstrating individual choice and preferences:

```java
Dog d = new Dog(15);
Dog d2 = new Dog(100);
d.maxDog(d2);
```

**Exercise 1.2.1**: Analyze the following method for potential inefficiencies or logical errors, akin to identifying market failures:

```java
public static Dog maxDog(Dog d1, Dog d2) {
    if (weightInPounds > d2.weightInPounds) {
        return this;
    }
    return d2;
}
```

**Static Variables**: These can be equated to common goods within a class's domain, offering widespread benefits like environmental resources. For instance, we might define the scientific name for Dogs universally as "Canis familiaris":

```java
public class Dog {
    public int weightInPounds;
    public static String binomen = "Canis familiaris";
    ...
}
```

Best practice suggests accessing these goods statically using class names rather than individual references, to avoid inefficiencies akin to tragedy of the commons. Thus, utilize `Dog.binomen` instead of `d.binomen`.

While improper access is permissible, it introduces negative externalities such as confusion and reduces coding efficiency—analogous to awkward resource allocation choices in economic systems.

**Exercise 1.2.2**: Engage with the following resources to further explore the intricacies of method utility:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String\[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

With what we've learned so far, it's time to demystify the declaration we've been using for the main method. Breaking it into pieces, we have:

* `public`: Ensures that this method is accessible from all classes. In microeconomics terms, it's similar to providing a public good that all can access without congestion.
* `static`: Indicates this method belongs to the class, not instances, akin to a fixed cost that doesn't vary with different instances of production.
* `void`: Specifies no output like a service provided without any direct returns, such as freely available software.
* `main`: This is the name of the method, similar to the central hub in a network of interlinked services.
* `String[] args`: This is a parameter that is passed to the main method, akin to consumer inputs in a market transaction.

**Command Line Arguments**

Since main is called by the Java interpreter itself rather than another Java class, it is the interpreter's job to supply these arguments. They refer usually to the command line arguments. Here, the Java interpreter acts as a central planner in a market supplying necessary inputs for execution. For example, consider the program `ArgsDemo` below:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program prints out the 0th command line argument. This is analogous to extracting the first piece of information from a dataset for analysis, e.g.

```
$ java ArgsDemo these are command line arguments
these
```

In the example above, `args` will be an array of Strings, where the entries are {'these', 'are', 'command', 'line', 'arguments'}, similar to parsing consumer preferences from a survey dataset.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Try to write a program that sums up the command line arguments, assuming they are numbers, similar to calculating total utility or sum of economic production outputs. For a solution, see the webcast or the code provided on GitHub.

#### Utilizing Market Mechanisms <a href="#utilizing-market-mechanisms" id="utilizing-market-mechanisms"></a>

One of the most important skills as a programmer is knowing how to effectively navigate and use existing libraries, akin to how an economist leverages market mechanisms for efficient resource allocation. In our interconnected digital economy, it is often possible to save resources (in terms of time and debugging efforts) by engaging with available online resources, similar to utilizing comparative advantage in trade to improve productivity opportunities.

In this course, you're encouraged to do this, with the following caveats:

* Do not use libraries that we do not provide, similar to how monopolistic practices discourage unauthorized methods of trade or resource use.
* Cite your sources, analogous to acknowledging your trading partners or market collaborators, ensuring transparency and trust in economic transactions.
* Do not search for solutions for specific homework or project problems, akin to avoiding insider trading or market manipulation, which creates unfair advantages.

For example, it's fine to search for solutions to general queries like "convert String integer Java"—comparable to seeking general market information or historical data. However, it is not OK to search for specific tailored solutions like "Project 2048 Berkeley", just as it's unethical to exploit specific insider information for personal gain.

For more on collaboration and academic honesty policy, see the course syllabus, which outlines the expected code of conduct much like regulations in economic markets that maintain fairness and competition.