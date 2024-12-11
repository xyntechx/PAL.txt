# Exploring Java Methods and Microeconomic Analogies

This chapter explores the concept of static and non-static methods in Java through the lens of microeconomic market structures. Static methods are likened to universally fixed properties in perfect competition, where firms react uniformly to external market conditions, similar to how static methods operate independently of object-specific data. Meanwhile, non-static methods parallel firm behavior in monopolistic or oligopolistic markets, where decisions are influenced by internal variables and strategic interactions just as non-static methods can adjust their behavior based on instance-specific details.

Throughout the chapter, different market types such as monopolistic competition, oligopoly, and perfect competition are used to illustrate how types of methods in Java can be metaphorically connected to economic models. The text covers Java programming concepts such as instance variables, constructors, class instantiation, and the differentiation between class and instance methods, drawing economic parallels like market strategy formulation and price setting. Additionally, the importance of leveraging external libraries in programming is compared to firms sourcing inputs to optimize efficiency, while adhering to ethical standards and ensuring proper attribution rightly aligns with maintaining integrity in both fields.



From a microeconomic perspective, static methods in our Java example could be compared to universally fixed properties in market structures like perfect competition. In perfect competition, firms regard the market price as given and base their quantities on these externally fixed prices — similar to how static methods are universally accessible without needing any object reference.



**Static Method Analogy in Microeconomics**

In microeconomics, the concept of a "static method" can be paralleled to a perfectly competitive market setting where decisions are not dependent on individual interactions but instead are based on market-wide information. For example, in markets with complete transparency and homogeneous goods, any decision to "make noise" or produce an output is driven entirely by prevailing market trends, much in the way a static method operates independently of instance-specific variables.



**Non-Static Methods**

Unlike static methods, non-static methods in Java can interact with instance-specific variables. This interaction mirrors the way firms operating in monopolistic or oligopolistic markets are influenced by internal factors and strategic interactions.

```java
public class Dog {
    public int barkVolume;

    public void makeLoudNoise() {
        System.out.println("Bark at volume: " + barkVolume);
    }
}
```

In this snippet, `makeLoudNoise` is a non-static method that can vary in output depending on the `barkVolume` setting of `Dog`. This method is akin to firms in a monopolistic competition adjusting their output and prices based on their cost structures and differentiation strategies.

#### Non-Static Method Analogy in Microeconomics

In a market with monopolistic competition or oligopoly, individual firms must consider their own cost structures, brand differentiation, and strategic interactions with competitors. Similarly, non-static methods use instance-specific information which resembles a firm tailoring its strategies, like setting a unique product price, to achieve competitive advantages.

**Practical Examples in Microeconomics**

In real economic scenarios, firms must decide whether their strategies should be based on the market-wide conditions or specific to their internal operations and market niche. For example, a new entrant might adopt entry-level pricing, a static strategy in the market, before moving to dynamic, non-static pricing, adjusting based on brand loyalty and customer feedback.

Just like in Java programming, where both static and non-static methods have their place, economic agents must leverage both static market conditions and custom adaptive strategies to optimize their outcomes.

**Instance Variables and Object Instantiation Through Microeconomic Lens**

In the economic ecosystem, each business entity operates differently. Some firms are ambitious and adopt aggressive marketing strategies to capture market share, symbolized by the yapping of a small dog, while others have an established reputation that naturally attracts customers, similar to the majestic howl of a malamute. Just as economic theories and models allow us to understand and replicate market behavior, Java's syntax enables us to model complex behaviors in software.

One way to portray the diverse landscape of market structures is to create separate classes for each type of firm or industry within an economy.

```java
public class SmallFirm {
    public static void marketStrategy() {
        System.out.println("aggressively advertising through social media!");
    }
}

public class LargeCorporation {
    public static void marketStrategy() {
        System.out.println("maintaining brand loyalty and reputation!");
    }
}
```

In economics, like in programming, instances represent real-world entities. Classes can be instantiated to model specific market players or behaviors, and these instances can hold attributes that affect their economic performance. This leads to a more realistic approach, where we create instances of the `Firm` class and structure the behaviors of the `Firm` methods based on the attributes of the specific `Firm`. Consider the class below that models firm behavior based on size:

```java
public class Firm {
    public int sizeInEmployees;

    public void marketStrategy() {
        if (sizeInEmployees < 50) {
            System.out.println("niche market focus with personalized service!");
        } else if (sizeInEmployees < 500) {
            System.out.println("expanding regional presence!");
        } else {
            System.out.println("dominating global markets!");
        }
    }    
}
```

Here is how such an instance might be used to simulate real-world firm strategy:

```java
public class FirmSimulator {
    public static void main(String[] args) {
        Firm f;
        f = new Firm();
        f.sizeInEmployees = 300;
        f.marketStrategy();
    }
}
```

This simulation will create a `Firm` with 300 employees, and it will execute a strategy described by "expanding regional presence!" reflecting its position in the market.

Key observations and terminology from an economic perspective:

* An `Object` in Java serves as a simulation of any entity or agent operating within an economic model.
* The `Firm` class maintains its own attributes, known as _instance variables_ or _non-static variables_. These attributes must be defined within the class and impact the behavior of the instance in the market.
* The method within the `Firm` class lacks the `static` keyword, categorizing it as an _instance method_ or _non-static method_.
* To execute the `marketStrategy` method, we instantiate a `Firm` using the `new` keyword, thus simulating the introduction of a new market player. Rather than invoking `Firm.marketStrategy()`, we tailored the strategy using `f.marketStrategy()`.
* Once instantiated, an object can be _assigned_ to a _declared_ variable of the suitable type, as shown by `f = new Firm();`
* Variables and methods embodied by a class are referred to as _members_ of a class.
* Access to class members is achieved through _dot notation_, analogous to accessing specific economic metrics or strategies of a firm.



**Constructors in Java and their Economic Analogue**

In computer science, we often construct objects in object-oriented languages using a _constructor_. Similarly, in microeconomics, products are "constructed" based on demand, consumer preferences, or other market forces that act as parameters:

```java
public class EconomySimulator {
    public static void main(String[] args) {
        Product p = new Product(100);
        p.describe();
    }
}
```

Here, the instantiation is parameterized, analogous to how prices might be set in a market. This reflects the law of demand: as variables change (such as price), the quantity demanded changes, thus influencing the "construction" of products. In this simulation, adding a "constructor" to our Product class can be seen as setting initial economic conditions, as shown below:

```java
public class Product {
    public int priceInDollars;

    public Product(int p) {
        priceInDollars = p;
    }

    public void describe() {
        if (priceInDollars < 50) {
            System.out.println("This is a cheap product!");
        } else if (priceInDollars < 150) {
            System.out.println("This product has a moderate price.");
        } else {
            System.out.println("This is a premium product!");
        }    
    }
}
```

The constructor with signature `public Product(int p)` is invoked to simulate market entry with a specific pricing strategy, much like firms set prices based on initial economic evaluations. Those familiar with Python will recognize this concept as akin to the `__init__` method, which sets initial conditions or properties of an instance or market.

**Economic Terminology Summary**

**Market Instantiation, Arrays of Products**

Just like in Economics 101, where we construct models to predict outcomes, in CS, arrays are instantiated using the new keyword, which mirrors setting variables like labor and capital in a production function. For example:

```java
public class MarketModelDemo {
    public static void main(String[] args) {
        /* Create a model of five products. */
        int[] priceArray = new int[5];
        priceArray[0] = 25;
        priceArray[1] = 75;
    }
}
```

This can be likened to setting initial prices or quantities for market simulations. Similarly, we can create arrays of instantiated product models in Java, which is equivalent to simulating products across different market segments:

```java
public class ProductArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two product offerings. */
        Product[] productArray = new Product[2];
        productArray[0] = new Product(40);
        productArray[1] = new Product(120);

        /* Market description will result, reflecting competitive pricing effects. */
        productArray[0].describe();
    }
}
```

Observe that the `new` keyword is used similarly to initiating both an array of potential product forms and each specific product entry. This dual use is reflective of both setting market capacities and firm-level decisions to enter a market with specific choices or strategies.

#### Class Methods vs. Instance Methods with a Microeconomic Twist <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

In microeconomics, we often distinguish between actions of individual agents versus the market as a whole. Similarly, Java allows us to define two types of methods:

* Class methods, a.k.a. static methods.
* Instance methods, a.k.a. non-static methods.

Instance methods can be likened to actions or preferences of individual economic agents that can only be effectively applied by that agent or firm. Static methods, on the other hand, resemble market-level actions or facts that do not vary between different agents except by implementation. As an example of a static method, the `Math` class provides a `sqrt` method. Because it is static, we can call it as follows:

```java
x = Math.sqrt(100);
```

If `sqrt` had been an instance method, we would have instead the awkward syntax below, akin to every firm having to define how to execute basic economic functions themselves. Luckily `sqrt` is a static method so we don't have to do this in real programs.

```java
Math m = new Math();
x = m.sqrt(100);
```

Sometimes, it makes sense to have a class with both instance and static methods. For example, suppose we want the ability to compare two market competitors. One way to do this is to add a static method for comparing MarketCompetitors.

```java
public static MarketCompetitor maxCompetitor(MarketCompetitor c1, MarketCompetitor c2) {
    if (c1.marketShare > c2.marketShare) {
        return c1;
    }
    return c2;
}
```

This method could be invoked by, for example:

```java
MarketCompetitor c = new MarketCompetitor(15);
MarketCompetitor c2 = new MarketCompetitor(100);
MarketCompetitor.maxCompetitor(c, c2);
```

Observe that we've invoked using the class name, just as a policy analyst would use economic indicators to compare firms, since this method is a static method.

We could also have implemented `maxCompetitor` as a non-static method, e.g.

```java
public MarketCompetitor maxCompetitor(MarketCompetitor c2) {
    if (this.marketShare > c2.marketShare) {
        return this;
    }
    return c2;
}
```

Above, we use the keyword `this` to refer to the current competitor, similar to an individual firm making comparisons based on private information. This method could be invoked, for example, with:

```java
MarketCompetitor c = new MarketCompetitor(15);
MarketCompetitor c2 = new MarketCompetitor(100);
c.maxCompetitor(c2);
```

Here, we invoke the method using a specific instance variable, reflecting firm-level decision-making.

**Exercise 1.2.1**: What would the following method do? If you're not sure, try it out.

```java
public static MarketCompetitor maxCompetitor(MarketCompetitor c1, MarketCompetitor c2) {
    if (marketShare > c2.marketShare) {
        return this;
    }
    return c2;
}
```

**Static Variables**

Much like market constants or widely accepted truths in economics, it is occasionally useful for classes to have static variables. These are properties inherent to the class itself, rather than the instance. For example, we might record that the common economic term for competitors is "Oligopoly":

```java
public class MarketCompetitor {
    public int marketShare;
    public static String marketType = "Oligopoly";
    ...
}
```

Static variables should be accessed using the name of the class rather than a specific instance, e.g. you should use `MarketCompetitor.marketType`, not `c.marketType`.

While Java technically allows you to access a static variable using an instance name, it is poor form, potentially confusing economic understanding and, in my opinion, an oversight by the Java designers.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

### public static void main(String\[] args) 

Understanding the role of key concepts in programming can be enlightened by drawing parallels to microeconomic principles. We can analyze this in terms of the main method setup in Java, comparing it to a market operation or bargaining scenario.

* `public`: In economics, think of this in line with "public goods", which are non-excludable and non-rivalrous. Similarly, declaring a method `public` means it is available or "accessible" to everyone (any part of your program).
* `static`: Analogous to fixed supply in the short-run, a `static` method does not change with demand since it does not require an object to be instantiated.
* `void`: As a zero-sum transaction, a `void` method signifies no returns or surplus, illustrating an operation where outputs perfectly balance costs, leaving nothing excess.
* `main`: This is like the central agent facilitating transactions in a market.
* `String[] args`: The input parameters can be compared to the goods or information fed into markets, impacting outcomes.

**Command Line Arguments as Market Inputs**

As a competitive market requires inputs from various actors, the Java interpreter supplies arguments to the main method—similar to consumer preferences or government policies influencing market function. Let's examine the `ArgsDemo` scenario:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

Here, the program prints out the 0th command line argument, signifying primary market data input, e.g.

```
$ java ArgsDemo demand supply equilibrium prices

demand
```

In this example, `args` acts as an array of Strings, comparable to economic variables such as {"demand", "supply", "equilibrium", "prices"}.

**Summing Command Line Arguments**: Analyzing Aggregate Economic Factors

**Exercise 1.2.3**: Calculate the sum of command line arguments, akin to determining total market supply or demand, assuming inputs are numerical. For detailed solutions, see educational resources online or code repositories.

#### Leveraging External Resources in Programming <a href="#using-libraries" id="using-libraries"></a>

One of the most critical skills in programming is the ability to efficiently find and utilize existing libraries, much like how firms in microeconomics source inputs to minimize costs and optimize production efficiency. In today’s digital age, programmers can significantly reduce opportunity costs—time and effort spent developing code from scratch—by sourcing mature and reliable libraries developed by others in the community.

In this course, you're encouraged to adopt this efficient approach, akin to firms maximizing utility under certain constraints, with the following stipulations acting as constraints:

* Exclusively use libraries that have been provided to you—similar to firms adhering to compliance and regulatory standards.
* Ensure you credit your sources, reflecting the importance of transparency and intellectual property rights in economic transactions.
* Avoid searching for specific solutions to assigned problems, akin to maintaining ethical standards and avoiding market manipulation.

For instance, looking up how to "convert String to integer Java" aligns with seeking operational efficiencies and enhancing your coding productivity. However, explicitly searching for "Project 2048 Berkeley" is akin to shadow pricing, attempting to bypass resource allocation constraints unfairly.

For further information on collaboration and the academic honesty policy, please refer to the course syllabus. This is analogous to the guidelines and regulations detailed in a market’s legal framework to ensure fair trade and competition.