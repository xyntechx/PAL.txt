# Java Programming Concepts in a Microeconomic Context

This chapter explores the parallels between Java programming concepts and microeconomic principles, using classes and methods to illustrate economic behaviors within market structures. It elucidates the difference between static and non-static methods by comparing them to economies of scale and individualized production processes, respectively. The `Dog` class and its methods are utilized as examples to demonstrate static methods as a way to operate without additional setup costs, akin to mass production, whereas non-static methods highlight the costliness of meeting specific consumer demands through instance creation.

Further, the discussion extends to object instantiation and use of instance variables portrayed through the `Firm` class, where varying levels of market power determine firm behavior akin to competitive market dynamics. Constructors are compared to production functions, illustrating the initialization process in object creation as a firm's capital management strategy. The chapter also covers the instantiation of arrays, drawing analogies to resource distribution among firms. Moreover, it contrasts class methods to instance methods in relation to public and private goods, underscoring the differences through practical examples and analogies to market behaviors. Static variables and libraries are deliberated upon with an economic perspective, emphasizing their utility in reducing resource allocation costs and adhering to fair use policies within educational and market environments.



In microeconomic terms, think of the `Dog` class as representing a firm's potential activities. The "makeNoise" method symbolizes the firm's ability to produce a specific output (in this case, a "Bark"). However, without any demand or application (akin to consumers in a market), the class does not actively produce anything; it sits idle like capital not yet in use because it hasn't been demanded in the absence of a main method.

**Non-Static Methods vs. Static Methods**

When we use static methods without creating an instance of a class — analogous to a firm's ability to produce a service without having to set up new operations each time — it allows us to benefit from economies of scale. We can leverage existing capabilities to meet uniform demand quickly without additional setup costs, much like how a company might use an automated process to service a client request immediately.

**Non-Static Methods**

Now, let's consider a method that must be invoked through an instance of a class, similar to a firm that requires specific assembly or set-up each time it meets new consumer needs:

```java
public class Dog {
    public void bark() {
        System.out.println("Woof!");
    }
}
```

Unlike static methods, invoking a non-static method requires the overhead of creating a specific instance, just like setting up individualized service that cannot be standardized. In economic terms, this method of operation might entail higher marginal costs because each output (or "instance") requires additional input each time it's created.

Consider the following launch program:

```java
public class DogLauncher {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.bark();
    }
}
```

```
$ java DogLauncher
Woof!
```

In this scenario, `DogLauncher` acts as a focal point for generating demand for the output "Woof!" using the `bark` method of a `Dog` object. The `DogLauncher` is analogous to a market that triggers the creation of operational instances to meet variable demands, indicating a potentially higher cost to satisfy each client because more resources are needed to achieve the individual instances.

The choice between static and non-static methods resembles the economic decision-making process between utilizing a mass-production approach for lower marginal costs or a customized production run that better meets specific demands, at a possibly higher marginal cost. As with economic choices, understanding which method is most efficient depends on the specific context and objectives, a balance that becomes clearer with further experience and study.




**Instance Variables and Object Instantiation in Microeconomic Contexts**

Not all production firms are alike. Some firms operate in competitive markets with little market power, producing homogeneous goods, while others enjoy monopoly power, allowing them to set prices above marginal cost. Often, we write economic models to mimic features of the real-world markets we study, and Java's syntax can be deftly repurposed to model such economic scenarios.

One approach to allowing us to represent different types of firms would be to create separate classes for each firm market structure.

```java
public class CompetitiveFirm {
    public static void produceOutput() {
        System.out.println("Produces at P = MC");
    }
}

public class Monopolist {
    public static void produceOutput() {
        System.out.println("Produces where MR = MC");
    }
}
```

As you should have seen in the past, classes can be instantiated, and instances can hold data. This leads to a more natural approach, where we create instances of the `Firm` class and make the behavior of the `Firm` methods contingent upon the characteristics of the specific `Firm`. To make this more concrete, consider the class below:

```java
public class Firm {
    public int marketPower;

    public void produceOutput() {
        if (marketPower < 10) {
            System.out.println("Operating as a competitive firm");
        } else if (marketPower < 30) {
            System.out.println("Oligopoly firm behavior");
        } else {
            System.out.println("Monopoly power, setting prices");
        }
    }    
}
```

As an example of using such a Firm, consider:

```java
public class FirmLauncher {
    public static void main(String[] args) {
        Firm f;
        f = new Firm();
        f.marketPower = 20;
        f.produceOutput();
    }
}
```

When run, this program will create a `Firm` with market power 20, and that `Firm` will soon exhibit "Oligopoly firm behavior".

Some key observations and terminology:

* An `Object` in Java is an instance of any class.
* The `Firm` class has its own variables, also known as _instance variables_ or _non-static variables_. These must be declared inside the class, unlike languages like Python or Matlab, where new variables can be added at runtime.
* The method that we created in the `Firm` class did not have the `static` keyword. We call such methods _instance methods_ or _non-static methods_.
* To call the `produceOutput` method, we had to first _instantiate_ a `Firm` using the `new` keyword, and then make a specific `Firm` produce. In other words, we called `f.produceOutput()` instead of `Firm.produceOutput()`.
* Once an object has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `f = new Firm();`
* Variables and methods of a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_.


### Constructors in Java with Microeconomics Concepts

Consider the process of object creation in object-oriented programming akin to a firm's decision to produce goods. In this analogy, a constructor acts as the production function, determining how inputs (parameters) are transformed into an output (an object). Just as firms strive to minimize effort and resources while producing goods, constructors streamline the initialization process, enhancing efficiency and productivity.

```java
public class DogLauncher {
    public static void main(String[] args) {
        Dog d = new Dog(20);
        d.makeNoise();
    }
}
```

In the above code, the instantiation of the `Dog` object functions like a firm's production of a new unit of a good, here parameterized to optimize resource use, much like a firm's decision to choose a cost-minimizing input combination. A constructor in Java acts as the production facility, making sure each object is correctly initialized. For the `Dog` class, the constructor is your facility, setting initial `weightInPounds` when a new `Dog` is created.

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

The constructor `public Dog(int w)` operates like a recipe for production, indicating the necessary initial capital (here represented by `weightInPounds`) when a `Dog` is created with specific parameters. Such efficiency reduces transaction costs, similar to how a firm efficiently manages its capital and labor resources for optimal output.

**Terminology Summary**

### Array Instantiation and Market Models

Array instantiation in Java reflects varying market models within microeconomics. For example, instantiating an array might represent the distribution of capital goods among various firms in a competitive market. Java's use of the `new` keyword for array creation not only marks resource allocation but resembles the initial investment phase in a market.

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

Similarly, constructing arrays of objects mirrors the creation of a multi-product firm, where each object represents a different product line or business unit:

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

Observe that `new` is used, both for creating an array to allocate for expected demand (like a firm's analysis of market size) and for each individual object, representing unique products produced by the firm. The conceptual division helps us understand allocation and utilization of resources, crucial in optimizing production and market success.

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

In Java, we have two primary types of methods that model different economic behaviors within a financial system:

* Class methods, akin to public goods or services.
* Instance methods, akin to private goods or services.

Instance methods, like private goods, are actions taken by a specific instance, i.e., the firm or individual, in an economy. Static methods, similar to public goods, are actions taken by the economy or market system as a whole. Both have unique utilities in varied situations. For instance, in the `Math` class, the `sqrt` method is analogous to a public good, accessible to all without needing individual provision:

```java
x = Math.sqrt(100);
```

If `sqrt` were an instance method, analogous to a private good, we would require individual provision as shown below. Fortunately, it's designed as a public service, allowing universal accessibility:

```java
Math m = new Math();
x = m.sqrt(100);
```

In some cases, it is economically rational for a class to offer both types of methods, similar to mixed goods that have both public and private characteristics. Consider the capability to compare two dogs. We could implement a static method for comparing Dogs, akin to a regulatory standard set by a central authority:

```java
public static Dog maxDog(Dog d1, Dog d2) {
    if (d1.weightInPounds > d2.weightInPounds) {
        return d1;
    }
    return d2;
}
```

This centralized comparison method can be thought of as a regulatory utility invoked with a focus on efficiency:

```java
Dog d = new Dog(15);
Dog d2 = new Dog(100);
Dog.maxDog(d, d2);
```

Notice the invocation through the class name, akin to accessing a universal market service.

Alternatively, we could implement `maxDog` as a non-static method, reflecting a more individualistic approach where the firm or individual manages operations internally:

```java
public Dog maxDog(Dog d2) {
    if (this.weightInPounds > d2.weightInPounds) {
        return this;
    }
    return d2;
}
```

Here, `this` references the resource in question, resembling a private operational strategy. This approach might be employed as follows:

```java
Dog d = new Dog(15);
Dog d2 = new Dog(100);
d.maxDog(d2);
```

Here, the decision-making power lies within the individual economic entity.

**Exercise 1.2.1**: Predict the economic behavior of the following scenario. If uncertain, simulate the operation.

```java
public static Dog maxDog(Dog d1, Dog d2) {
    if (weightInPounds > d2.weightInPounds) {
        return this;
    }
    return d2;
}
```

**Static Variables**

Occasionally in economies, it's practical for sectors to have static characteristics, akin to intrinsic market features or national resources. For example, a distinguishing trait could be the classification "Canis familiaris" for dogs, paralleling essential economic identifiers:

```java
public class Dog {
    public int weightInPounds;
    public static String binomen = "Canis familiaris";
    ...
}
```

These static variables or intrinsic economic traits should be referenced through the sector or class name, ensuring clarity similar to industry-wide identifiers, e.g., using `Dog.binomen` rather than referring through an individual instance, which could lead to market confusion or misallocation.

Java permits referencing static variables via instances, akin to a policy breach in economic systems — bad practice and suboptimal from a design perspective.

**Exercise 1.2.2**: Tackle this economic exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)



#### public static void main(String\[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

The main method in our program can be thought of like the decision-making point in a market economy where various forces of supply and demand interact. To breakdown the components of our main method:

* `public`: Much like a publicly available resource, this keyword means the method can be accessed by any part of the program.
* `static`: Think of this like a static analysis in economics that studies an equilibrium state without transitioning through various points – the "static" keyword defines the method as belonging to the class itself rather than any particular instance, or "state" of an object.
* `void`: Indicates the method does not return utility, akin to a consumer consuming without any expectation of return.
* `main`: Signifies the function as the primary interaction point of the program, much like the equilibrium price point in a market.
* `String[] args`: Represents the inputs, similar to consumer preferences or external market conditions that influence broader market outcomes.

**Command Line Arguments**

These arguments can be analogized to external shocks or parameters in an economic model that affect the equilibrium state. Since main is called by the Java interpreter itself—akin to an external force—it is responsible for supplying these parameters, typically in the form of command line arguments. Consider the `ArgsDemo` program below:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

In this example, the program extracts and prints the first argument, similar to a market model analyzing changes caused by a shift in a single parameter. For instance:

```
$ java ArgsDemo demand-side shift
"demand-side"
```

In this scenario, `args` will be an array of Strings, interpreted as {"demand-side", "shift"} affecting the economic model based on external conditions.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Create a program to sum command line arguments, assuming they represent numerical data such as prices or quantities. This mirrors how economic models aggregate individual data points to derive market outcomes. For a detailed solution, see the webcast or the accompanying code on GitHub.

#### Using Libraries with a Microeconomic Perspective <a href="#using-libraries" id="using-libraries"></a>

One of the most valuable skills in programming is the ability to efficiently allocate resources by leveraging existing libraries. In microeconomic terms, utilizing these resources can significantly reduce your "opportunity cost," as you can allocate your time and labor to tasks that yield a higher "marginal utility" or benefit.

In this course, you're encouraged to harness this economic "efficiency," with the following constraints operating as our "market regulations":

* Do not use libraries that we do not provide, akin to adhering to market standards or regulations in product usage.
* Cite your sources, similar to revealing the "provenance" of resources or intellectual property in economic exchanges.
* Do not search for solutions for specific homework or project problems, much like avoiding "asymmetric information transactions," where undue advantage is gained without fair exchange in knowledge acquisition.

For example, it's economically sound to search for information equivalent to "convert String integer Java," akin to seeking general market knowledge. However, it is not appropriate to search for "Project 2048 Berkeley," which would relate to a "market manipulation" scenario in a competitive academic environment.

For more on collaboration and academic honesty policy, reflecting principles of "fair trade" and "transparency" in educational contexts, see the course syllabus.