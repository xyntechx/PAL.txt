# Understanding Static and Instance Methodologies with Microeconomic Analogies

This textbook chapter explores the concept of static and instance methodologies in object-oriented programming in Java, framed through the lens of microeconomic analogies. Static methods are compared to universally available production processes within a firm, allowing execution without requiring the full context of a class. An example is given with a `Dog` class that has a static method to "bark" universally. The chapter highlights the importance of the `main` method, or equivalent launching mechanisms, as market demand triggers to initiate static method operations.

The chapter also delves into the concept of instance methods and variables, aligning these with microeconomic principles. It describes how, similar to consumer preferences, each object or instance can hold different attributes, affecting its behavior. By creating consumer models, the notion of flexible representation of various consumer profiles is paralleled with object instantiation and attribute definition in Java. Following this analogy further, the chapter explains the role of constructors in creating standardized conditions for object formation, similar to optimizing a production strategy in economics. Concepts such as arrays and the distinction between class and instance methods are also examined, providing a robust understanding of how Java's programming structures mirror economic strategies and operations.

In microeconomic terms, think of a class as a "firm" and static methods as the "production processes" that the firm can execute. A static method serves as a standardized production line that doesn't rely on individual firm resources, akin to a routine operation that can be performed without assessing each individual worker or component involved. It's a set process ready to meet demands without needing elaborate context.

**Static Methods in Microeconomic Context:**

Consider a "Dog" class as a simplified firm specializing in producing a particular output: sound, through the static method `makeNoise()`. This method acts as a universal company operation that functions independently of specific economic agent statuses or external contracts, representing a consistent production method.

```java
public class Dog {
    public static void makeNoise() {
        System.out.println("Bark!");
    }
}
```

However, just setting up this firm (the `Dog` class) doesn’t automatically trigger activity in the market. It reflects potential output awaiting market demand before production activation—that is, consumer demand initiates the process:

```
$ java Dog
Error: Main method not found in class Dog, please define the main method as:
       public static void main(String[] args)
```

Merely having production capability (or firm potential) doesn’t shake the market (nor run the class). To stimulate output (execute the firm’s operations), market demand needs expression through mechanism like a `main` method or an auxiliary entity such as `DogLauncher` which acts as a catalyst:

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

The `DogLauncher` becomes a "consumer" or "client" interacting with the "Dog" firm, engaging its production when market signals are conducive. Choosing to embed the main method within `Dog` versus utilizing `DogLauncher` presents various strategic market entry options, each bearing distinct advantages within varying economic landscapes. As we advance, understanding these choices enhances our grasp of market dynamics and firm-client exchanges, illustrating parallels between computer science execution and economic strategy.

**Instance Variables and Object Instantiation through Microeconomic Principles**

In the vast landscape of consumer markets, diversity in preferences and behaviors is as pronounced as the varied breeds of dogs. Some consumers exhibit a tendency towards high-end luxury goods, while others contentedly partake in the essentials. Much like Java's syntax, which can articulate various canine attributes, economic models must be malleable enough to depict the rich tapestry of consumer profiles.

A microeconomic approach to representing consumer preference diversity is market segmentation – creating distinct classes for each type of consumer. In Java, we can achieve this by defining separate classes simulating different consumer behaviors:

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

In microeconomics, consumers are often modeled as agents possessing certain traits, much like objects in programming. This methodology aligns with Java's class design, making consumer behavior, such as purchase decisions, contingent upon the economic characteristics of the instantiated consumer class. Consider the following class setup:

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

Here’s how a consumer instance might be used in a program:

```java
public class ConsumerBehaviorTest {
    public static void main(String[] args) {
        Consumer c = new Consumer();
        c.incomeLevel = 50000;
        c.makePurchaseDecision();
    }
}
```

Executing this program constructs a `Consumer` with an income level of $50,000, effectively correlating to an inclination "explores premium options occasionally."

Key insights and terminologies bridging both computer science and microeconomics include:

* An `Object` in Java, a quintessential class instance, can be likened to a consumer, a fundamental unit in economic models.
* The `Consumer` class encapsulates individual consumer details as _instance variables_, analogous to economic data collected for research purposes.
* Methods in the `Consumer` class that do not include the `static` keyword are known as _instance methods_, which emphasize specific consumer behaviors rather than the generalized trends.
* To simulate consumer behaviors like `makePurchaseDecision`, it is crucial to _instantiate_ a `Consumer`, applying the `new` keyword to materialize a specific instance. Post-instantiation, behaviors are examined by invoking `c.makePurchaseDecision()`, rather than `Consumer.makePurchaseDecision()`.
* An instantiated object necessitates _assignment_ to an adequately _declared_ variable, such as `c = new Consumer();`.
* The constituents of a class, both variables and methods, are referred to as the _members_ of that class, akin to the individual economic agents constituting a model.
* Members are interfaced using _dot notation_, a parallel to pinpointing attributes or actions of agents in economic models.

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

Here, instantiation of objects is "parameterized," analogous to efficiently allocating resources in a firm to minimize costs and maximize utility. Instead of manually specifying numerous instance variable allocations, we use "parameterization" to streamline the process, resembling how a firm strategically chooses input combinations to optimize output. By employing a "constructor," which functions like a production function in economics, we establish standardized criteria for object creation tailored to specific requirements.

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

The constructor with signature `public Dog(int w)` operates each time we attempt to "produce" a `Dog` using the `new` keyword alongside a single integer input representing weight, much like how a firm selects its production quantity based on given resource inputs and constraints. For those more familiar with Python, the constructor parallels the `__init__` method, akin to establishing initial conditions in a firm's production setup.

**Terminology Summary Analog**

**Array Instantiation, Arrays of Objects through Economic Lens**

As outlined in previous discussions, "arrays" are instantiated in Java reminiscent of resource allocation via the keyword `new`. Analogous to setting up a diversified investment portfolio, consider the following:

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

Similarly, when creating arrays of instantiated objects in Java, it's comparable to diversifying a firm's assets among various projects or products, thereby managing risk and optimizing returns.

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

Notice that `new` fulfills dual roles: initially, in creating an "array" to host `Dog` objects, analogous to preparing production lines for a diverse range of products, and subsequently, through actual resource allocation by creating individual `Dog` instances, similar to producing each product based on a firm's predetermined criteria and resource availability.

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java allows the definition of both class methods and instance methods, which can be analogously compared to distinct economic strategies.

* **Class methods**: These are akin to strategic long-term decisions (e.g., static methods) that a firm makes, focusing on overall market presence and resource management without dependency on current operational constraints.
* **Instance methods**: These are likened to short-term operational decisions (e.g., non-static methods) which depend on the current resources and performance of individual economic entities.

Instance methods operate on individual objects, much like a firm's output decisions that leverage current capacities and inventories. Static methods, however, are associated with the class itself, reflecting a strategic industry benchmark approach, applicable across various object states, not restrained by the day-to-day operational capacity.

Consider the `Math` class in Java, which provides the `sqrt` function—a static method—analogous to industry standardized processes:

```java
x = Math.sqrt(100);
```

This is comparable to utilizing universally accepted methodologies, not tied to an instance-specific context. If `sqrt` were an instance method, requiring a specific context, you would need to instantiate the class:

```java
Math m = new Math();
x = m.sqrt(100);
```

In real-world scenarios, incorporating both instance and static methods in a class allows for adaptable strategic and operational capabilities, like decisions firms make to remain competitive at both industry and operational levels. For instance, a `Dog` class comparing two instances reflects the difference between market analysis and individual operational adjustments:

```java
public static Dog maxDog(Dog d1, Dog d2) {
    if (d1.weightInPounds > d2.weightInPounds) {
        return d1;
    }
    return d2;
}
```

This static method imitates a strategic industry comparison, invoked without coupling to immediate instance limitations:

```java
Dog d1 = new Dog(15);
Dog d2 = new Dog(100);
Dog.maxDog(d1, d2);
```

The class-level invocation symbolizes a broader market perspective, divorced from short-term operational constraints.

For instance adjustments, reflecting short-term operational strategies:

```java
public Dog maxDog(Dog d2) {
    if (this.weightInPounds > d2.weightInPounds) {
        return this;
    }
    return d2;
}
```

The use of `this` specifies current resource utilization, akin to maximizing output based on current operational capabilities.

**Exercise 1.2.1**: Assess how strategic limitations apply in code by simulating the given snippet:

```java
public static Dog maxDog(Dog d1, Dog d2) {
    if (weightInPounds > d2.weightInPounds) {
        return this;
    }
    return d2;
}
```

**Static Variables**

Static variables in Java equate to constant economic factors like structural industry benchmarks. For example, a dog’s scientific name in the `Dog` class is independent of any specific dog, just as industry standards are overarching:

```java
public class Dog {
    public int weightInPounds;
    public static String binomen = "Canis familiaris";
    ...
}
```

Access class-wide constants using the class identifier—which mirrors how firms adopt industry-wide standards: `Dog.binomen` versus `d.binomen`.

While Java allows accessing static variables via instance names—similar to overlooking strategic efficiencies for specific operational gains—it is discouraged, as it can result in inefficiencies and ambiguity, much like operational strategies that disregard market benchmarks.

**Exercise 1.2.2**: Investigate the strategic versus operational methodologies through the following resources:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

To explore the declaration of the `main` method, we can draw analogies with familiar microeconomic principles, enhancing understanding through economic reasoning:

* `public`: Just as a public good in economics is accessible to all without limiting its use by others, the `public` keyword makes the method accessible to any part of the program, emphasizing unrestricted utilization akin to the broad reach of a lighthouse beam shared among ships at sea.

* `static`: This reflects the notion of fixed inputs in production that do not fluctuate with output levels. A `static` method provides a constant function that exists independently of any object instances, similar to how certain fixed resources support multiple production processes without being linked to any individual one.

* `void`: Like support services in an economy that facilitate operations but do not generate direct products themselves, `void` signifies that the method executes a procedure without yielding a return value. While enabling functionality, it doesn’t directly produce a return, akin to invisible yet essential economic infrastructure.

* `main`: Comparable to the main engine driving a market, the `main` method serves as the central point where execution commences, orchestrating operations and coordinating the program’s functionality to align with input commands.

* `String[] args`: This functions as input parameters do in economic production functions, offering the input that customizes the method’s operations. They adjust how `main` behaves based on the provided data, paralleling consumer choices influencing demand for goods.

**Command Line Arguments**

The `main` method acts like an economic coordinator, called upon by the Java interpreter which plays the role of organizing inputs – the command line arguments. Consider the `ArgsDemo` program below as a demonstration of how inputs, akin to consumer preferences, are processed and utilized:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

Executed as:

```
$ java ArgsDemo these are command line arguments
these
```

Here, `args` represents a collection of inputs, similar to a bundle of goods from which one can select and utilize. The array encompasses values like {"these", "are", "command", "line", "arguments"}, offering flexible choices, much like choosing consumer goods.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Develop a program that sums command line arguments treated as numeric inputs, similar to calculating total cost or utility. For guidance, refer to instructional videos or access the solution on our GitHub repository.

#### Using Libraries <a href="#using-libraries" id="using-libraries"></a>

In your journey to becoming a proficient computer scientist, understanding the strategic use of resources is vital, similar to how resources are managed in microeconomics. In programming, libraries act as pre-existing resource pools that improve efficiency, much like firms seeking to optimize production while minimizing costs. Utilizing libraries can enhance productivity and reduce the chance of redundant work, much as businesses strive to minimize costs to maximize profit in a competitive market.

In this course, leveraging libraries is not only encouraged but subject to guidelines, reflecting the regulatory frameworks found in economic systems:

* Only use libraries from an approved list. This parallels adhering to industry regulations and standards designed to ensure fair competition in the marketplace.
* Credit all source materials by citing them, akin to honoring intellectual property rights and contracts within an economic context.
* Refrain from seeking direct solutions to specific assignments. This maintains academic integrity, much like businesses following ethical standards to avoid monopolistic practices.

To illustrate, searching for a broad method such as "convert String integer Java" is acceptable—similar to a company conducting market research to find the best practice. However, looking up specific assignment answers like "Project 2048 Berkeley solution" violates ethical standards and corresponds to unfair competitive practices such as insider trading.

For a complete overview of collaboration and academic honesty policies—akin to understanding the ethical standards in microeconomics—refer to the course syllabus.