# Introduction to Object-Oriented Programming in Java

This chapter introduces key object-oriented programming concepts using analogies from microeconomics, focusing primarily on Java. It begins by likening a company's production methods to static methods in Java, explaining how these methods, while defined within a class, require external triggers to execute, much like businesses need a market to sell their products. The chapter then draws parallels between consumer behavior and object instantiation, illustrating how classes in Java can encapsulate diverse characteristics and preferences through instance variables and methods. This provides a foundation for understanding how real-world behaviors and economic models can be translated into software design using Java's object-oriented features.

Further, the text explains the significance of constructors, which are used to create objects with specific states or attributes, akin to consumer choices influenced by budget constraints. Through practical Java code snippets, the material illustrates how objects can be tailored to represent real-world entities, enhancing the software's ability to simulate complex systems. The chapter also discusses the different roles of class methods (static methods) and instance methods, comparing their usage and benefits to public and private goods in microeconomics. It ends with a detailed explanation of the syntax and functionality of the `main` method in Java, drawing comparisons to centralized planning in economics, and emphasizes the importance of using existing libraries to streamline development, cautioning against unethical programming practices to maintain fairness and integrity, akin to market regulations.

In microeconomics, consider a company (class) that produces a specific product (method). This company defines operation protocols (static methods in CS) that guide its production capacity without necessitating additional resources beyond the initial setup. For instance, if a company’s operation (method) is to manufacture widgets, this static method defines the theoretical capacity for widget production. However, similar to how a method in a class remains dormant until called, production does not commence without market demand.

To initiate this static company operation, akin to calling a method, an external trigger such as market demand is required. In programming, a `main` method or another class (like a `DogLauncher`) kicks off the process, just as a sales team might initiate production based on market signals. Here, the `DogLauncher` is analogous to market forces or customer demand that activates the production capability, allowing the static method to execute and produce goods. 

In economic terms, internalizing sales functions within the company may streamline production. Alternatively, relying on an external sales team could provide flexibility and specialization advantages. This choice echoes programming design decisions: integrating a main method within the `Dog` class for centralized control, or utilizing an external `DogLauncher` to segregate functions and potentially enhance efficiency. The decision hinges on strategic goals and efficiency assessments, paralleling how experienced programmers assess the trade-offs between centralized and modular coding approaches.

**Instance Variables and Object Instantiation with Microeconomics Analogies**

In the study of microeconomics, understanding different consumer behaviors is paramount. Just as in economics where some consumers prioritize luxury over cost-effectiveness, Java programming allows us to capture diverse behaviors through the use of instance variables and methods.

To represent different consumer preferences in Java, we can create a generic `Consumer` class that can be tailored with specific characteristics, much like how real-world consumers have unique preferences.

```java
public class Consumer {
    private double budget;

    public Consumer(double budget) {
        this.budget = budget;
    }

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

In this example, we utilize a constructor method in the `Consumer` class, which initializes an instance variable, `budget`. This mirrors economic models where initial conditions influence outcomes.

```java
public class ConsumerMarket {
    public static void main(String[] args) {
        Consumer c = new Consumer(3000); // Instantiate a Consumer with a budget of 3000
        c.expressPreference();
    }
}
```

When executing the `ConsumerMarket` class, we create a `Consumer` object with a defined budget. The `expressPreference` method outputs consumer choices based on this budget, akin to market decisions influenced by purchasing power.

**Key Observations:**

- **Objects and Instantiation:** In Java, an object is an instance of a class, representing unique market participants with specific attributes like budget.
- **Instance Variables vs. Static Variables:** Instance variables (here, `budget`) differ from static variables as they hold data unique to each object, unlike static variables which are shared across all instances.
- **Instance Methods:** Methods without the `static` keyword, such as `expressPreference`, operate on instance variables and reflect behavior unique to each object.
- **Constructors:** Special methods that initialize new objects. Our `Consumer(double budget)` constructor sets the initial budget, akin to assigning an initial endowment in an economic model.
- **Dot Notation:** Objects access their methods and variables using dot notation, e.g., `c.expressPreference()`.

This approach of structuring classes and using instance variables provides rich flexibility to simulate varied behaviors, just as economic models incorporate diverse consumer preferences into analyses.

## Constructors and Consumer Choices in Java

In programming, constructing objects is akin to how consumers make decisions based on constraints. In Java, we use a _constructor_ to create objects, similar to consumers optimizing utility with limited resources:

```java
public class DogLauncher {
    public static void main(String[] args) {
        Dog d = new Dog(20);
        d.makeNoise();
    }
}
```

In this snippet, `Dog d = new Dog(20);` initializes a `Dog`, similar to a consumer selecting a product within their budget. To support such initialization, the `Dog` class needs a constructor:

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

The `Dog` constructor allows efficient object creation, much like consumers maximizing utility under constraints. Here, the constructor `public Dog(int w)` gets invoked during object creation via `new`, similar to economic decision-making.

## Static and Instance Contexts

In Java, methods can be either static or instance-based. The `public static void main` method above is static, and can be seen as a public amenity available without needing a specific instance, akin to a public good. Static methods belong to the class rather than any object, thus not requiring instantiation, which can be compared to resources or functions that do not deplete with usage in economics.

Instance methods, however, operate on individual objects like `makeNoise` above and require an instance, paralleling private goods determined by personal use.

## Array Instantiation and Firm Production Practices

Array creation in Java, like economic production, involves organizing resources for output:

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

By initializing arrays like `int[] someArray = new int[5];`, Java provides the framework to manage resources, similar to how firms allocate inputs for production.

Similarly, arrays can hold objects, representing diverse production outputs:

```java
public class DogArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two dogs, each as a unique product offering. */
        Dog[] dogs = new Dog[2];
        dogs[0] = new Dog(8);
        dogs[1] = new Dog(20);

        /* Simulate output based on consumer preferences. */
        dogs[0].makeNoise();
    }
}
```

The `new` keyword supports both array creation and object instantiation, akin to setting up the infrastructure and completing production. This dual use reflects optimizing available resources to meet demands, efficiently producing various outputs.

#### Class Methods vs. Instance Methods: An Economic Perspective <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

In programming, understanding class methods and instance methods can be enhanced through microeconomic principles by considering their efficiency and utility.

* **Class Methods** (static methods) can be thought of as shared resources, like public infrastructure that benefits all vehicles without needing customization for individual drivers. Similarly, class methods offer functionality accessible to all instances of a class, without modification.
* **Instance Methods** (non-static methods) resemble personalized services, such as tailored clothing or custom consultations, providing specific utility to each object instance.

Instance methods can be likened to goods with diminishing returns for specific objects: as one object uses an instance method more, the additional utility it gains decreases. Conversely, static methods serve as a utility-maximizing universal resource, much like public utilities.

Consider the static `sqrt` method from the `Math` class, which can be used by all without alteration, akin to accessing a public broadcast:

```java
x = Math.sqrt(100);
```

If `sqrt` were an instance method, it would require each user to instantiate their own version, similar to each person owning a television set to access the same content:

```java
Math m = new Math();
x = m.sqrt(100);
```

In some scenarios, blending class methods and instance methods optimizes utility, just as a mix of public amenities and private goods caters to diverse consumer needs. For example, a static method that determines the larger of two dogs, akin to a market comparison tool:

```java
public static Dog maxDog(Dog d1, Dog d2) {
    if (d1.weightInPounds > d2.weightInPounds) {
        return d1;
    }
    return d2;
}
```

This method is accessible to all instances within the class "market," invoked simply as:

```java
Dog d = new Dog(15);
Dog d2 = new Dog(100);
Dog.maxDog(d, d2);
```

Conversely, an instance method version provides a direct comparison, emphasizing individual preference, much like tailored financial advice:

```java
public Dog maxDog(Dog d2) {
    if (this.weightInPounds > d2.weightInPounds) {
        return this;
    }
    return d2;
}
```

Invoke this method using a specific instance, demonstrating customized service:

```java
Dog d = new Dog(15);
Dog d2 = new Dog(100);
d.maxDog(d2);
```

**Exercise 1.2.1**: Examine the following method for inefficiencies or logical errors, similar to identifying economic inefficiencies:

```java
public static Dog maxDog(Dog d1, Dog d2) {
    if (weightInPounds > d2.weightInPounds) {
        return this;
    }
    return d2;
}
```

**Static Variables**: These are like common goods within a class's domain, offering universal benefits akin to environmental resources. For example, the scientific name for dogs is defined once and shared across all instances:

```java
public class Dog {
    public int weightInPounds;
    public static String binomen = "Canis familiaris";
    ...
}
```

Accessing these static resources effectively requires using the class name, akin to shared resource management to prevent overuse:

```java
String name = Dog.binomen;
```

Mismanagement can lead to confusion and inefficiency, similar to resource misallocation in economic terms.

**Exercise 1.2.2**: Explore additional material to deepen your understanding of method utility in programming:

* [Video Explanation](https://youtu.be/8Gq-8mVbyFU)
* [Related Slide](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* [Solution Video](https://youtu.be/Osuy8UEH03M)

#### public static void main(String[] args)

In this section, we will break down the declaration we've been frequently using for the `main` method in Java and understand its components in detail:

* `public`: This keyword means that the method is accessible from any other class. This is similar to a public good in microeconomics, which is accessible to all without restriction. However, unlike public goods which can suffer from congestion, a `public` method in a class is designed to handle multiple accesses efficiently.

* `static`: This keyword signifies that the method belongs to the class itself rather than any instance of the class. Imagine this as the fixed cost in production where the cost remains constant irrespective of the number of goods produced. A `static` method similarly provides its functionality without requiring any instantiated objects.

* `void`: This indicates that the method does not return any value. In economic terms, this might be like a service that provides intangible benefits rather than direct returns, such as open-source software contributing to societal knowledge.

* `main`: This signifies the central method. It's similar to a central hub in an interconnected service network, where various data inputs (like consumer demands in a market model) converge for processing.

* `String[] args`: These are parameters passed to the `main` method, functioning similarly to inputs in a market transaction. The `args` array holds command line arguments, just as consumers' choices are inputs that drive market functions.

**Command Line Arguments**

The `main` method is invoked by the Java interpreter, which feeds it command line arguments. Essentially, the interpreter acts like a central planner providing essential inputs for program execution. Consider the following example, `ArgsDemo`:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

In this program, the first command line argument is printed out. This mirrors selecting a particular data point from a comprehensive dataset for evaluation, akin to isolating a specific consumer preference in economic analysis:

```
$ java ArgsDemo these are command line arguments
these
```

Here, `args` is an array of `String` values containing the command line arguments. Each element, like pieces of consumer data collected from a survey, can be separately analyzed or utilized.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Try crafting a program that adds up command line arguments, assuming they're numbers. This parallels calculating a total utility or summing up economic outputs in a production function. For the solution, refer to the webcast or provided GitHub repository.

#### Utilizing Market Mechanisms <a href="#utilizing-market-mechanisms" id="utilizing-market-mechanisms"></a>

One of the most crucial skills for a programmer is effectively navigating and utilizing existing libraries, much like an economist leverages market mechanisms for efficient resource allocation. In our interconnected digital economy, programmers can save resources—such as time and debugging efforts—by engaging with available online resources, similar to utilizing comparative advantage in trade to enhance productivity.

Throughout this course, students are encouraged to practice this efficiency, with these important caveats:

* Limit your use of libraries to those provided within the course, akin to respecting legal trade boundaries established to maintain fair markets.
* Always cite your sources, similar to how economists acknowledge data sources or collaborators to build trust and transparency in any market transaction.
* Avoid searching for specific homework or project solutions, akin to steering clear of insider trading in market activities to maintain fairness and integrity.

For instance, it is permissible to search for general solutions, like how to convert a String to an Integer in Java, which is similar to seeking general market information or historical economic data. However, it is not permissible to search for direct solutions to specific course projects like "Project 2048 Berkeley", as this would mirror the unethical use of insider information for personal advantage.

Further details on collaboration and our academic honesty policy can be found in the course syllabus, which establishes expected behaviors much like regulations in economic markets that uphold fairness and competition. This ensures a balanced educational environment, just as rules and norms maintain order and fairness in economic systems.