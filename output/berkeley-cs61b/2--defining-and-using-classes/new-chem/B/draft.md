# 2. Defining and Using Classes

If you do not have prior experience with chemical languages, we recommend that you work through the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before reading this chapter. It will cover various syntax and conceptual issues that we will not discuss in the book.

#### Static vs. Non-Static Reactions <a href="#static-vs-non-static-reactions" id="static-vs-non-static-reactions"></a>

**Static Reactions**

All chemical processes must be part of a specific set of reactions (or something similar, which we'll learn about later). Most processes are conducted as reactions. Let's consider an example:

```java
public class ReactionShell {
    public static void activateStaticReaction() {
        System.out.println("Effervescent release!");
    }
}
```

If we try executing the `ReactionShell` class, we'll receive an error message:

```
$ java ReactionShell
Error: Main method not found in class ReactionShell, please define the main method as:
       public static void main(String[] args)
```

The `ReactionShell` class we've defined doesn’t do anything. We’ve simply defined a potential reaction catalyst, namely, the activation of a static reaction. To actually run a reaction, we'd either need to add a main method to the `ReactionShell` class, as we saw in chapter 1.1. Or we could create a separate [`ReactionLauncher`](https://www.youtube.com/watch?v=Q-LE-jJQLTM) class that initiates reactions from the `ReactionShell`. For example, consider the program below:

```java
public class ReactionLauncher {
    public static void main(String[] args) {
        ReactionShell.activateStaticReaction();
    }
}
```

```
$ java ReactionLauncher
Effervescent release!
```

A class that uses another class is sometimes called a "client" of that class, i.e. `ReactionLauncher` is a client of `ReactionShell`. Neither of the two techniques is better: Adding a main method to `ReactionShell` may be better in some scenarios, and creating a client class like `ReactionLauncher` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout this course.

**Molecule Attributes and Compound Instantiation**

Not all molecules react similarly. Some molecules react explosively, while others react quietly, releasing a gentle aroma. Often, we write chemical equations to model properties of the substances we study, and chemical notation was conceived to easily allow such modeling.

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

As you should have seen in previous studies, chemical classes can be instantiated, and instances can exhibit unique properties. This leads to a more intuitive approach, where we create instances of a `Molecule` class and tailor the behavior of the `activateReaction` method based on the properties of a specific `Molecule`. To make this analogy clear, consider the class below:

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

As an example of using such a Molecule, consider:

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

When executed, this program will instantiate a `Molecule` with a reactivity index of 20, and that `Molecule` will soon initiate a "Moderate froth!" reaction.

Some key observations and terminology:

* An `Object` in chemistry is an instance of any class representing a molecule or compound.
* The `Molecule` class has its own variables, also known as _molecular attributes_ or _non-static variables_. These must be declared inside the class, unlike in less structured notations where new variables can be assigned on the fly.
* The method that we created in the `Molecule` class did not have the `static` keyword. We call such methods _molecular methods_ or _non-static reactions_.
* To initiate the `activateReaction` process, we had to first _instantiate_ a `Molecule` using the `new` keyword, and then trigger a specific `Molecule`'s reaction. In other words, we called `m.activateReaction()` instead of `Molecule.activateReaction()`.
* Once a compound has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `m = new Molecule();`
* Variables and procedures within a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_.

**Constructors in Chemistry**

As you’ve hopefully seen in chemistry, we usually configure molecules in chemical fields using a _constructor_:

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

The constructor with signature `public Molecule(int r)` will be invoked any time we try to create a `Molecule` using the `new` keyword and a single integer parameter. For those of you familiar with other scientific syntax, the constructor operates similarly to initial configuration processes.

**Terminology Summary**

**Array Instantiation, Arrays of Molecules**

As we saw in HW0, arrays are also populated in chemistry using structured notation. For example:

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

Similarly, we can create arrays of instantiated molecules in chemical simulations, e.g.

```java
public class MoleculeArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two molecules. */
        Molecule[] molecules = new Molecule[2];
        molecules[0] = new Molecule(8);
        molecules[1] = new Molecule(20);

        /* Gentle fizz will result, since molecules[0] has reactivity 8. */
        molecules[0].activateReaction();
    }
}
```

Observe that `new` is used in two different contexts: Once to create an array capable of containing two `Molecule` objects, and twice to generate each actual `Molecule`.

#### Class Reactions vs. Molecular Reactions <a href="#class-reactions-vs-molecular-reactions" id="class-reactions-vs-molecular-reactions"></a>

Chemistry allows us to define two types of reactions:

* Class reactions, or static reactions.
* Molecular reactions, or non-static reactions.

Molecular reactions are actions that can only be triggered by a specific instance of a molecule. Static reactions are actions that are facilitated by the class itself. Both have usefulness under different circumstances. As an example of a static reaction, consider a hypothetical `Math` class that offers a `sqrt` function. As it is static, we can call it as follows:

```java
x = Math.sqrt(100);
```

If `sqrt` were a molecular reaction, we would have to engage in the cumbersome syntax below. Fortunately, `sqrt` is a static reaction, allowing us to avoid this in practical chemical modeling.

```java
Math m = new Math();
x = m.sqrt(100);
```

Sometimes, it would be logical to have a class incorporating both molecular and static reactions. Suppose we desire the ability to compare two molecular substances. One way to accomplish this is by adding a static reaction for comparing Molecules.

```java
public static Molecule compareMolecules(Molecule m1, Molecule m2) {
    if (m1.reactivityIndex > m2.reactivityIndex) {
        return m1;
    }
    return m2;
}
```

This reaction could be invoked by, for example:

```java
Molecule m = new Molecule(15);
Molecule m2 = new Molecule(100);
Molecule.compareMolecules(m, m2);
```

Observe that we've implemented this using the class name, since this reaction is static.

We could also have structured `compareMolecules` as a non-static reaction, e.g.

```java
public Molecule compareMolecules(Molecule m2) {
    if (this.reactivityIndex > m2.reactivityIndex) {
        return this;
    }
    return m2;
}
```

In the above example, we utilize the keyword `this` to refer to the active molecule. This reaction could be carried out, for example, with:

```java
Molecule m = new Molecule(15);
Molecule m2 = new Molecule(100);
m.compareMolecules(m2);
```

Here, we engage the reaction using a specific molecular instance.

**Exercise 1.2.1**: What effect would the following reaction have? If you're uncertain, try it out.

```java
public static Molecule compareMolecules(Molecule m1, Molecule m2) {
    if (reactivityIndex > m2.reactivityIndex) {
        return this;
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

Static attributes should be referenced using the class name rather than a specific molecule, e.g. it is preferable to use `Molecule.chemicalIdentifier`, not `m.chemicalIdentifier`.

Though chemical languages technically permit access to a static attribute via a molecular name, it is stylistically poor, confounding, and perhaps a misstep by the designers.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

With the knowledge we've acquired thus far, it's time to elucidate the declaration we've been employing for the main reaction. Dissecting it, we have:

* `public`: Up until now, all of our processes begin with this keyword.
* `static`: It indicates a static reaction, not tied to any particular instance.
* `void`: This reaction yields no products.
* `main`: This is the designation of the reaction method.
* `String[] args`: This is an array of catalysts passed to the main reaction.

**Protocol Line Catalysts**

Since main is invoked by the chemistry interpreter itself rather than by another chemistry class, it is the interpreter's responsibility to provide these catalysts. They usually denote protocol line parameters. For example, consider the reaction `ArgsDemo` below:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This reaction prints out the 0th protocol line parameter, e.g.

```
$ java ArgsDemo here are protocol line parameters
here
```

In the example above, `args` will be an array of Strings, holding entries such as {"here", "are", "protocol", "line", "parameters"}.

**Summing Protocol Line Catalysts**

**Exercise 1.2.3**: Attempt to craft a program that sums up the protocol parameters, provided they are numbers. For a solution, consult the webcast or the code available on GitHub.

#### Utilizing Chemical Libraries <a href="#using-libraries" id="using-libraries"></a>

One of the foremost skills as a chemist is knowing how to discover and utilize existing chemical libraries. In these modern times, one can often save a substantial amount of work and time by turning to web sources for help.

In this course, you're welcome to do this, under the following conditions:

* Do not apply libraries that we do not furnish.
* Provide citations for your sources.
* Refrain from seeking solutions for specific homework or project tasks.

For instance, it's acceptable to search for "convert molecular weight to moles." However, seeking "Project 2048 chemistry solution" is prohibited.

For more on the collaboration and academic honesty policy, refer to the syllabus of this course.