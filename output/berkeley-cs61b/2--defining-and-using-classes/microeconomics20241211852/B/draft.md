# Understanding Static and Instance Methodologies with Microeconomic Analogies

This textbook chapter explores the concept of static and instance methodologies in object-oriented programming in Java, framed through the lens of microeconomic analogies. Static methods are compared to universally available production processes within a firm, allowing execution without requiring the full context of a class. An example is given with a `Dog` class that has a static method to "bark" universally. The chapter highlights the importance of the `main` method, or equivalent launching mechanisms, as market demand triggers to initiate static method operations.

The chapter also delves into the concept of instance methods and variables, aligning these with microeconomic principles. It describes how, similar to consumer preferences, each object or instance can hold different attributes, affecting its behavior. By creating consumer models, the notion of flexible representation of various consumer profiles is paralleled with object instantiation and attribute definition in Java. Following this analogy further, the chapter explains the role of constructors in creating standardized conditions for object formation, similar to optimizing a production strategy in economics. Concepts such as arrays and the distinction between class and instance methods are also examined, providing a robust understanding of how Java's programming structures mirror economic strategies and operations.



In microeconomic terms, we can think of a class as a "firm" and static methods as the "production processes" offered by the firm. A static method is like a production line that is part of a firm’s capabilities but doesn’t require exposing the firm's full resources (or the characteristics of individual workers or machines involved in the production process). It’s a predefined action that can be called upon without needing to establish the detailed context of the firm.

**Static Methods in Microeconomic Context:**

Imagine the "Dog" class as a small firm that produces a single good: noise, represented by the static method `makeNoise()`. This method is the equivalent of a company-wide process that does not depend on the specific state of a particular economic agent or an external contract—a universally accessible production line.

```java
public class Dog {
    public static void makeNoise() {
        System.out.println("Bark!");
    }
}
```

However, if we just establish this firm (the `Dog` class) in the market, it results in no action until there’s an actual demand for its output—a market requirement that invokes the production process:

```
$ java Dog
Error: Main method not found in class Dog, please define the main method as:
       public static void main(String[] args)
```

Simply defining potential output (or firm capability) does not influence the market (or run the class). To activate this output (execute the firm's production), there must be a demand articulated through the market mechanism, represented here by a `main` method or a separate `DogLauncher` containing the trigger for production:

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

The `DogLauncher` serves as a "consumer" or "client" of the "Dog" firm, triggering its production process when market conditions are appropriate. Whether embedding the main method inside `Dog` or using `DogLauncher` to call the method can be viewed as different market entry strategies, each having its situational advantages reflecting diverse economic environments or market structures. As we progress in our understanding, the strategic choice between these methodologies will clarify, aligned with learning about market dynamics and firm-client interactions.

**Instance Variables and Object Instantiation through Microeconomic Principles**

Consider the diverse world of consumer preferences and behaviors, akin to the diversity in dogs. Some consumers have a high propensity to consume luxury goods, while others are more satisfied with basic necessities. Just as Java's syntax allows for the representation of diverse canine behaviors, it also parallels the flexibility needed in economic models to represent diverse consumer profiles.

One approach to model the variation in consumer preferences would be to create separate classes for each consumer type, analogous to market segmentation in microeconomics.

```java
public class BudgetConsumer {
    public static void makePurchaseDecision() {
        System.out.println("prefers affordable options");
    }
}

public class LuxuryConsumer {
    public static void makePurchaseDecision() {
        System.out.println("prefers premium products");
    }
}
```

In the realm of microeconomics, consumers can also be treated as entities with specific characteristics, much like objects in a programming language. This approach aligns with using Java classes and makes consumer behavior (in this case, purchase decisions) dependent on the economic attributes of the specific consumer class instance. Consider the class below:

```java
public class Consumer {
    public double incomeLevel;

    public void makePurchaseDecision() {
        if (incomeLevel < 20000) {
            System.out.println("prefers budget items");
        } else if (incomeLevel < 75000) {
            System.out.println("explores premium options occasionally");
        } else {
            System.out.println("frequently buys luxury goods");
        }
    }    
}
```

An example of using such a Consumer entity in a program could be:

```java
public class ConsumerBehaviorTest {
    public static void main(String[] args) {
        Consumer c;
        c = new Consumer();
        c.incomeLevel = 50000;
        c.makePurchaseDecision();
    }
}
```

When run, this program creates a `Consumer` with an income level of $50,000, and that `Consumer` will likely be inclined to "explores premium options occasionally."

Key observations and terminology which also relate to microeconomics:

* An `Object` in Java represents a specific instance of any class, similar to how a consumer is a unit of analysis in economic models.
* The `Consumer` class holds individual consumer data, known as _instance variables_ or _non-static variables_. These need to be pre-declared within the class, paralleling the constraints economists face when collecting data.
* The method developed in the `Consumer` class, lacking the `static` keyword, is termed an _instance method_ or _non-static method_, emphasizing specific consumer behavior rather than general market predictions.
* In order to simulate consumer behavior like `makePurchaseDecision`, we must _instantiate_ a `Consumer` using the `new` keyword, then examine the behavior of this specific `Consumer`. This is represented by using `c.makePurchaseDecision()` instead of `Consumer.makePurchaseDecision()`.
* Once instantiated, an object can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `c = new Consumer();`
* Variables and methods within a class are also known as _members_ of that class, similar to individual economic units in a model.
* Class members are accessed using _dot notation_, akin to specifying attributes or behaviors in economic models.

**Constructors in Java with Microeconomic Analogy**

In the realm of constructing software solutions, consider Java's _constructor_ as akin to choosing the optimal production strategy in an object-oriented programming economy.

```java
public class DogLauncher {
    public static void main(String[] args) {
        Dog d = new Dog(20);
        d.makeNoise();
    }
}
```

Here, instantiation of objects is "parameterized," analogous to efficiently allocating resources in a firm to minimize costs. Instead of manually specifying numerous instance variable allocations, we use "parameterization" to streamline the process, resembling how a firm strategically chooses input combinations. By employing a "constructor," which functions like a production function in economics, we establish standardized criteria for object creation.

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

The constructor with signature `public Dog(int w)` operates each time we attempt to "produce" a `Dog` using the `new` keyword alongside a single integer input representing weight, much like a firm deciding on production output based on given input quantities. For those analogizing from Python, the constructor parallels the `__init__` method, akin to altering initial conditions in a firm's production setup.

**Terminology Summary Analog**

**Array Instantiation, Arrays of Objects through Economic Lens**

As outlined in previous discussions, "arrays" are instantiated in Java reminiscent of resource allocation via the keyword `new`. Analogous to setting up a balanced portfolio, consider the following:

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

Likewise, imagine creating arrays of instantiated objects in Java, comparable to diversifying a firm's assets among projects or products.

```java
public class DogArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two dogs. */
        Dog[] dogs = new Dog[2];
        dogs[0] = new Dog(8);
        dogs[1] = new Dog(20);

        /* Yipping will result, since dogs[0] has weight 8. */
        dogs[0].makeNoise();
    }
}
```

Notice that `new` fulfills dual roles: initially, in creating an "array" to host `Dog` objects, analogous to preparing production shoots for a line of products, followed by actual resource allocation by creating individual `Dog` instances, akin to producing each product based on predetermined criteria.

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java allows us to define two types of methods which can be likened to the dual aspects of a firm's production decisions in microeconomics:

* Class methods, akin to long-run production decisions (e.g., static methods).
* Instance methods, akin to short-run production decisions (e.g., non-static methods).

Instance methods are actions that can be taken only by a specific instance of a class, much like a firm's output decisions that depend on its current capacity (short-run). Static methods are actions engaged by the class itself, aligning with a firm's strategic decisions unaffected by capacity constraints (long-run). 

As an example analogous to a static method in this economic analogy, the `Math` class provides a utility function `sqrt`, which can be leveraged for calculations beyond the current state of a specific instance (not limited by short-run constraints):

```java
x = Math.sqrt(100);
```

If `sqrt` had been an instance method, evoking short-run constraints, we would require individual instantiation:

```java
Math m = new Math();
x = m.sqrt(100);
```

Similar to firms needing to adjust their production processes differently in the short and long runs, sometimes it's beneficial to have both instance and static methods in a single class. For instance, consider the comparison between two competitive goods' weights, comparable to the "conditions for price competition" among firms.

```java
public static Dog maxDog(Dog d1, Dog d2) {
    if (d1.weightInPounds > d2.weightInPounds) {
        return d1;
    }
    return d2;
}
```

This method acts like a market evaluation, independent of a specific producer’s current constraints, and could be invoked using the class strategy (static context), as shown below:

```java
Dog d = new Dog(15);
Dog d2 = new Dog(100);
Dog.maxDog(d, d2);
```

Observe the invocation using the class name, indicating it is beyond immediate operational constraints.

However, as strategic decisions are revised, operational decisions (instance methods) are still essential for adjusting to short-term changes:

```java
public Dog maxDog(Dog d2) {
    if (this.weightInPounds > d2.weightInPounds) {
        return this;
    }
    return d2;
}
```

Here, the `this` keyword is employed to denote current resource allocation, analogous to current output levels determined by a firm's productive capacity.

**Exercise 1.2.1**: What would the following method do considering the constraints of productive capacity? If you're not sure, simulate the code.

```java
public static Dog maxDog(Dog d1, Dog d2) {
    if (weightInPounds > d2.weightInPounds) {
        return this;
    }
    return d2;
}
```

**Static Variables**

Similar to constant factors in production like technology or environment, static variables characterize class-level properties independent of individual instances. For example, the scientific name (or binomen) for Dogs remains constant like the "industry standard" for species:

```java
public class Dog {
    public int weightInPounds;
    public static String binomen = "Canis familiaris";
    ...
}
```

Access such constants using the class name, akin to how firms utilize industry benchmarks or standards: `Dog.binomen`, rather than `d.binomen`.

While Java technically permits accessing static variables via an instance, akin to operationally ignoring economies of scale efficiencies, it is discouraged, creating inefficiency and confusion akin to misaligned strategic and operational goals.

**Exercise 1.2.2**: Engage with this exercise in the context of exploring strategic vs. operational methodologies:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

Let's evaluate the main method declaration using some microeconomic principles, akin to analyzing the components of a production process:

* `public`: Like a public good in economics, this ensures widespread accessibility, indicating that any external entity can "consume" or utilize this method, just as anyone can enjoy a lighthouse's beam.
* `static`: Similar to a fixed cost in production that does not change with the level of goods produced, a static method is not linked to specific instances but rather provides a constant service regardless of instance creation.
* `void`: Like a utility function that doesn't give direct returns but supports underlying economic activities, this keyword denotes that the method provides a procedural function without direct output.
* `main`: Much like a key player in a market, this is a pivotal method where the primary operations begin.
* `String[] args`: This is akin to varying input parameters in a production function, affecting how the main method operates based on the supplied arguments.

**Command Line Arguments**

The main method is similar to a central planner in an economy: it is called upon by another entity—the Java interpreter—which takes on the role of organizing the inputs, in this case, the command line arguments. For example, in the program `ArgsDemo` below, we can see how the input, typical of consumer preferences, is processed:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program prints out the first "good" or command line argument (similar to the first unit of a consumed good in a demand analysis), represented as:

```
$ java ArgsDemo these are command line arguments
these
```

In this context, `args` represents a collection of consumable goods (command line inputs), akin to a bundle of goods in consumer theory, where the array contains values like {"these", "are", "command", "line", "arguments"}.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Attempt to create a program that totals the command line arguments, treating them as numerical inputs much like calculating the total cost or utility. For a solution, refer to the webcast or the provided code on GitHub.

#### Using Libraries <a href="#using-libraries" id="using-libraries"></a>

As an aspiring computer scientist, it is crucial to understand the parallel with microeconomics wherein resources need to be efficiently allocated. Libraries in programming serve as an existing pool of resources that maximize productivity and minimize opportunity costs. In the dynamic economy of technical development, much like in markets, leveraging existing solutions can lead to greater utility and reduction in the labor cost associated with coding from scratch.

In this course, leveraging these resources is encouraged but with certain regulations representing market rules and constraints:

* Do not utilize libraries outside of approved resources. Think of this as adhering to legal and compliance standards in an economic market.
* Provide citations for all source materials, akin to respecting intellectual property laws.
* Avoid direct methods to source solutions for specific problems to maintain integrity, mirroring fair trade practices.

For example, it's acceptable to search for a general method such as "convert String integer Java", which parallels a general market search for a resource. However, searching for specific solutions like "Project 2048 Berkeley" misaligns with ethical guidelines similar to market manipulation.

For more details on collaboration and academic honesty policy, much like understanding microeconomic ethical standards, see the course syllabus.