# 2. Defining and Using Classes

If you do not have prior experience with the basics of Java programming, we recommend that you work through the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before reading this chapter. It will cover various syntax and conceptual issues that we will not discuss in the book.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

All programming processes must be part of a specific set of methods (or something similar, which we'll learn about later). Most processes are conducted through method calls. Let's consider an example:

```java
public class MethodShell {
    public static void executeStaticMethod() {
        System.out.println("Static method executed!");
    }
}
```

If we try executing the `MethodShell` class without a main method, we'll receive an error message:

```
$ java MethodShell
Error: Main method not found in class MethodShell, please define the main method as:
       public static void main(String[] args)
```

The `MethodShell` class we've defined doesn’t do anything on its own. We’ve simply defined a potential method, namely, the execution of a static method. To actually run this method, we'd need to add a main method to the `MethodShell` class, as we saw in chapter 1.1, or we could create a separate `MethodLauncher` class that makes use of the `MethodShell`. For example, consider the program below:

```java
public class MethodLauncher {
    public static void main(String[] args) {
        MethodShell.executeStaticMethod();
    }
}
```

```
$ java MethodLauncher
Static method executed!
```

A class that uses another class is sometimes called a "client" of that class, i.e. `MethodLauncher` is a client of `MethodShell`. Neither of the two techniques is better: Adding a main method to `MethodShell` may be better in some scenarios, and creating a client class like `MethodLauncher` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout this course.

It's important to emphasize that in Java, each "static" method tied to a class is not inherently reactive like chemical reactions. Class instances and method calls must align with computational logic rather than non-programming-related analogies. This clear understanding will help the transition from conceptual "action" to method execution in programming.

**Molecule Attributes and Compound Instantiation**

Not all molecules react similarly. Some molecules react explosively, while others react quietly, releasing a gentle aroma. Often, we write chemical equations to model properties of the substances we study, and chemical notation was conceived to allow such modeling easily. However, this chapter focuses on using programming languages like Java to model chemical species behavior.

One approach to representing these chemical species would be to create separate classes for each type of molecule.

```java
public class TinyMolecule {
    public static void activateReaction() {
        System.out.println("Tiny bubbling!");
    }
}

public class LargeMolecule {
    public static void activateReaction() {
        System.out.println("Slow effervescence!");
    }
}
```

The above classes define simple behavior using static methods in Java. The term "static" means the method belongs to the class rather than instances of the class. It does not imply any specific chemical concept.

As you should have seen in previous studies, chemical classes can be instantiated, and instances can exhibit unique properties. This leads to a more intuitive approach, where we create instances of a `Molecule` class and tailor the behavior of the `activateReaction` method based on the properties of a specific `Molecule`. To make this parallelism clearer, consider the class below:

```java
public class Molecule {
    public int reactivityIndex;

    public void activateReaction() {
        if (reactivityIndex < 10) {
            System.out.println("Gentle fizz!");
        } else if (reactivityIndex < 30) {
            System.out.println("Moderate froth!");
        } else {
            System.out.println("Vigorous bubble!");
        }
    }    
}
```

To illustrate, consider the following example of using such a Molecule:

```java
public class ReactionLauncher {
    public static void main(String[] args) {
        Molecule m;
        m = new Molecule();
        m.reactivityIndex = 20;
        m.activateReaction();
    }
}
```

When executed, this program will instantiate a `Molecule` with a reactivity index of 20, and that `Molecule` will soon initiate a "Moderate froth!" reaction. Note that this "reaction" refers to the output behavior of the program rather than a chemical reaction.

Some key observations and terminology:

* An `Object` in this context is an instance of any class representing a molecule or compound.
* The `Molecule` class has its own variables, also known as _molecular attributes_ or _non-static variables_. These must be declared inside the class, unlike in less structured notations where new variables can be assigned on the fly.
* The method that we created in the `Molecule` class did not have the `static` keyword. We call such methods _instance methods_ (replacing the earlier misleading term _non-static reactions_).
* To initiate the `activateReaction` method, we had to first _instantiate_ a `Molecule` using the `new` keyword, and then trigger a specific `Molecule`'s behavior. This is achieved with a call like `m.activateReaction()` instead of `Molecule.activateReaction()`.
* Once a compound has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `m = new Molecule();`
* Variables and procedures within a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_.

By ensuring clarity and alignment with programming terms, this section aims to accurately reflect the intended parallels between chemical and computational systems without implying unintended correlaries.

**Constructors in Chemistry and Computer Science**

In chemistry, molecules can be configured using defined processes, akin to the use of constructors in programming. The analogy here is meant to illustrate how in both domains, initial setup is crucial for functionality.

```java
public class ReactionLauncher {
    public static void main(String[] args) {
        Molecule m = new Molecule(20);
        m.activateReaction();
    }
}
```

Here, the instantiation is parameterized, sparing us the trouble and untidiness of manually setting potentially numerous molecular attributes. To allow such syntax, we need only add a "constructor" to our Molecule class, as shown below:

```java
public class Molecule {
    public int reactivityIndex;

    public Molecule(int r) {
        reactivityIndex = r;
    }

    public void activateReaction() {
        if (reactivityIndex < 10) {
            System.out.println("Gentle fizz!");
        } else if (reactivityIndex < 30) {
            System.out.println("Moderate froth!");
        } else {
            System.out.println("Vigorous bubble!");
        }    
    }
}
```

The constructor with signature `public Molecule(int r)` is invoked whenever we create a `Molecule` using the `new` keyword and a single integer parameter. Similar to initial configuration processes in scientific experiments, constructors set up necessary conditions for an object's usage in Java.

**Terminology Clarification**
1. **Chemical Languages:** "Chemical languages" could refer to cheminformatics or chemical programming languages/interfaces. However, in this context, it illustrates structuring molecular models using object-oriented principles.
2. **Static Method Context:** The usage of `public static void main(String[] args)` in Java doesn't directly correlate with static reactions in chemistry. The term "static" here refers to Java's class-level methods, not to chemical states.
3. **Programming and Chemistry Analogy:** While chemistry terms like "effervescent release" are metaphorical, focus on the aspect that constructors and methods in programming initiate and manage processes akin to experimental control procedures in chemistry.

By emphasizing the similarities in setup logic between chemistry and programming, we aim for a clearer, interdisciplinary understanding without conflating scientific concepts with programming methodologies. Each domain uses initialization and configuration as foundational steps, albeit for different purposes and outcomes.

**Array Instantiation, Arrays of Molecules**

In programming, arrays are commonly used to organize data, similar to how structured notation is utilized in chemistry. For example:

```java
public class ArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five integers representing atomic counts. */
        int[] atomicCounts = new int[5];
        atomicCounts[0] = 3;
        atomicCounts[1] = 4;
    }
}
```

Similarly, we can create arrays of instantiated molecules in chemical simulations, reflecting how complex chemical considerations might be represented in code:

```java
public class MoleculeArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two molecules. */
        Molecule[] molecules = new Molecule[2];
        molecules[0] = new Molecule(8);
        molecules[1] = new Molecule(20);

        /* Initiate a reaction logic for molecules[0], given its properties. */
        molecules[0].activateReaction();
    }
}
```

Note that `new` is used here to create an array that can store two `Molecule` objects and again each time a `Molecule` is instantiated.

This demonstration uses the concepts from object-oriented programming without confusing them with exact chemical analogs. Keep in mind that terminology such as 'reaction' here serves to illustrate object behavior in the program rather than simulate a chemical process.

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

In programming, particularly in Java, we define two types of methods:

* Class methods, also known as static methods.
* Instance methods, which are non-static.

Instance methods are actions that can only be performed by a specific instance of a class. Static methods are actions that are facilitated by the class itself. Both have usefulness under different circumstances. As an example of a static method, consider a hypothetical `Math` class that offers a `sqrt` function. As it is static, we can call it as follows:

```java
x = Math.sqrt(100);
```

If `sqrt` were an instance method, we would have to use the syntax below. Fortunately, `sqrt` is a static method, allowing us to avoid this in practical programming.

```java
Math m = new Math();
x = m.sqrt(100);
```

Sometimes, it would be logical to have a class incorporating both instance and static methods. Suppose we desire the ability to compare two molecular objects or their properties. One way to accomplish this is by adding a static method for comparing objects of a class:

```java
public static Molecule compareMolecules(Molecule m1, Molecule m2) {
    if (m1.reactivityIndex > m2.reactivityIndex) {
        return m1;
    }
    return m2;
}
```

This method could be invoked by, for example:

```java
Molecule m = new Molecule(15);
Molecule m2 = new Molecule(100);
Molecule.compareMolecules(m, m2);
```

Observe that we've implemented this using the class name, since this method is static.

We could also have structured `compareMolecules` as a non-static method, e.g.

```java
public Molecule compareMolecules(Molecule m2) {
    if (this.reactivityIndex > m2.reactivityIndex) {
        return this;
    }
    return m2;
}
```

In the above example, we utilize the keyword `this` to refer to the current instance. This method could be called, for example, with:

```java
Molecule m = new Molecule(15);
Molecule m2 = new Molecule(100);
m.compareMolecules(m2);
```

Here, we invoke the method using a specific object instance.

[The Start of Improved Section]
**Exercise 1.2.1**: What effect would the following code have? Try it out:

```java
public static Molecule compareMolecules(Molecule m1, Molecule m2) {
    if (m1.reactivityIndex > m2.reactivityIndex) {
        return m1;
    }
    return m2;
}
```

**Static Attributes**

In certain instances, it is beneficial for molecular classes to possess static attributes. These are characteristics inherent to the class as a whole, rather than to an individual molecule. For instance, we might log a universal identifier for Molecules as "H2O-Dipolar Entity":

```java
public class Molecule {
    public int reactivityIndex;
    public static String chemicalIdentifier = "H2O-Dipolar Entity";
    ...
}
```

Static attributes should be referenced using the class name rather than a specific molecule, e.g., it is preferable to use `Molecule.chemicalIdentifier`, not `m.chemicalIdentifier`.

While it is technically permissible to access a static attribute via an instance name in Java, it is stylistically poor and may lead to confusion.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)
[The End of Improved Section]

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

With the knowledge we've acquired thus far, it's time to elucidate the declaration we've been employing for the main function. Dissecting it, we have:

* `public`: This keyword ensures that the method is accessible to any other class.
* `static`: It indicates a method that belongs to the class, not to a specific instance.
* `void`: This method does not return any value.
* `main`: This is the name of the method that's the entry point for Java applications.
* `String[] args`: This is an array of strings that allows command-line arguments to be passed to the main method.

**Command Line Arguments**

Since main is invoked by the Java interpreter itself rather than by another object in your code, it is the interpreter's responsibility to provide these arguments. They usually denote command line arguments. For example, consider the following program named `ArgsDemo`:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program prints out the first command line argument, e.g.

```
$ java ArgsDemo here are command line parameters
here
```

In the example above, `args` will be an array of Strings, holding entries such as {"here", "are", "command", "line", "parameters"}.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Attempt to craft a program that sums up the command line arguments, provided they are numbers. For a solution, consult the webcast or the code available on GitHub.

In this section, careful use of terminology ensures clarity. While these parallels help illustrate concepts of access levels, method applicability, and utility, they don't imply a direct relation to chemical behavior.

#### Utilizing Chemical Libraries <a href="#using-libraries" id="using-libraries"></a>

One of the foremost skills as a chemist is knowing how to discover and utilize existing chemical libraries. In these modern times, one can often save a substantial amount of work and time by turning to web sources for help.

In this course, you're welcome to do this, under the following conditions:

* Do not apply libraries that we do not furnish.
* Provide citations for your sources.
* Refrain from seeking solutions for specific homework or project tasks.

For instance, it's acceptable to search for "convert molecular weight to moles." However, seeking "Project 2048 chemistry solution" is prohibited.

When referring to concepts in programming, it is important to draw clear parallels without assuming direct correlations. For example, the concept of "static" in programming, as used in methods like `public static void main(String[] args)`, does not equate to any particular "reaction" type in chemistry. Instead, understanding static methods emphasizes particular programming logic, such as access levels and method utility, rather than implying any chemical behavior.

Furthermore, terms like "chemistry languages" should clearly highlight their context, focusing on cheminformatics or chemical programming interfaces, which are primarily tools for managing chemical information rather than having direct ties to Java programming structures.

For more on the collaboration and academic honesty policy, refer to the syllabus of this course.

