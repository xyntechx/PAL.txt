# Object-Oriented Programming in Microbiology with Java

This chapter introduces fundamental concepts of object-oriented programming in Java through the lens of microbiological organisms and operations. The chapter begins by explaining the difference between static methods and instance methods, using a `Dog` class as an illustrative example. Instance variables and methods are explained, providing the foundation for understanding how objects represent individual entities with specific characteristics or behaviors within a Java program. The section progresses by drawing parallels between Java constructs and microbiological concepts, demonstrating how to model microorganisms such as bacteria with different survival conditions.

Throughout the chapter, readers learn to structure classes and methods in Java by implementing biological examples such as bacteria and viruses. The chapter covers creating classes to represent varied bacterial types that thrive in distinct environments (e.g., acidophiles and alkaliphiles). It also illustrates utilizing arrays to simulate collections of microbial strains, akin to laboratory setups. Furthermore, the chapter delves into the distinction between class methods and instance methods and how static elements can serve to represent universal properties or behaviors of microorganisms. By embedding microbiology into programming exercises, the chapter offers a practical approach to understanding Java class structures, constructors, and array usage, culminating in a simplified bioinformatics application example to consolidate learning.

In summary, we've introduced some basic terminology and syntax for using classes in Java. The `Dog` class had two methods: a static method and an instance method. We also introduced _instance variables_, which are variables that are specific to a particular object created from the class. Methods without the `static` keyword are known as instance methods or non-static methods.

3. Defining and Using Organisms

If you do not have prior experience with microbiology concepts, we recommend reviewing basic cell biology concepts to familiarize yourself with fundamental ideas such as organelles and microbial structure, which will not be extensively discussed here.

#### Prokaryotic vs. Eukaryotic Organisms <a href="#prokaryotic-vs-eukaryotic-organisms" id="prokaryotic-vs-eukaryotic-organisms"></a>

**Prokaryotic Organisms**

All living organisms are composed of cells, which can be broadly classified into two categories: prokaryotic or eukaryotic. Let's consider an example of a prokaryotic organism:

```java
public class Bacterium {
    public static void replicateDNA() {
        System.out.println("Replicating circular DNA!");
    }
}
```

If we try running the `Bacterium` process, we'll simply get an error message, because it's not a complete organism representation:

```
$ java Bacterium
Error: Main method not found in class Bacterium, please define the main method as:
       public static void main(String[] args)
```

The `Bacterium` class we've defined doesn't do anything functional yet. We've simply defined something the `Bacterium` **can** do, namely replicate DNA. To actually execute a process, we'd either need to add a main method to the `Bacterium` class or create a separate `MicrobialSimulator` class that runs methods from the `Bacterium` class. Consider the program below:

```java
public class MicrobialSimulator {
    public static void main(String[] args) {
        Bacterium.replicateDNA();
    }
}
```

```
$ java MicrobialSimulator
Replicating circular DNA!
```

A class that uses another class is sometimes called a "client" of that class, i.e., `MicrobialSimulator` is a client of `Bacterium`. Neither of these techniques is superior by default: including a main method within `Bacterium` may be more appropriate in some cases, while creating a client-like `MicrobialSimulator` might be more appropriate in others. The advantages of each approach will become more obvious as we develop more complex organism simulations.

**Life Functions and Cell Structure**

Not all bacteria are identical. Some bacteria thrive in acidic environments, while others prefer alkaline conditions, reflecting the incredible diversity of microbial life. We frequently create models to simulate characteristics of the microbial world, and Java's syntax can be adopted to allow such simulation.

One strategy to represent this bacterial diversity is to create separate classes for each type of bacterium.

```java
public class Acidophile {
    public static void survive() {
        System.out.println("Thriving in acidic environments!");
    }
}

public class Alkaliphile {
    public static void survive() {
        System.out.println("Thriving in alkaline environments!");
    }
}
```

As you've learned, classes can be instantiated, and instances can hold data. This results in a more natural design where we instantiate the `Bacterium` class and enable the behavior of bacterium methods to depend on specific properties of the Bacterium. To illustrate this more clearly, observe the class below:

```java
public class Bacterium {
    public int idealPH;

    public void survive() {
        if (idealPH < 5) {
            System.out.println("Surviving in acidic condition!");
        } else if (idealPH < 8) {
            System.out.println("Surviving in neutral condition!");
        } else {
            System.out.println("Surviving in basic condition!");
        }
    }    
}
```

As an example of utilizing such a Bacterium, consider:

```java
public class MicrobialSimulator {
    public static void main(String[] args) {
        Bacterium b;
        b = new Bacterium();
        b.idealPH = 7;
        b.survive();
    }
}
```

When executed, this program will create a `Bacterium` with an ideal pH of 7, and that `Bacterium` will announce "Surviving in neutral condition!"

Some key observations and terminology:

* An `Object` in Java represents an instance of any class.
* The `Bacterium` class has its own variables, also referred to as _instance variables_ or _non-static variables_, which need to be declared within the class, unlike languages such as Python or Matlab, where new variables can be dynamically created.
* The method created in the `Bacterium` class lacked the `static` keyword. Such methods are known as _instance methods_ or _non-static methods_.
* To invoke the `survive` method, it is necessary to first _instantiate_ a `Bacterium` using the `new` keyword, and then have that specific `Bacterium` demonstrate survival.
* Once an object has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, like `b = new Bacterium();`
* Variables and methods of a class are considered _members_ of a class.
* Members of a class are accessed using _dot notation_.

**Constructors in Biology-Inspired Programming**

In object-oriented programming, constructing objects often involves using a _constructor_ method:

```java
public class MicrobialSimulator {
    public static void main(String[] args) {
        Bacterium b = new Bacterium(7);
        b.survive();
    }
}
```

Here, the instantiation is parameterized, saving us the time and complexity of manually typing out numerous instance variable assignments. To enable this syntax, we add a "constructor" to our Bacterium class, as shown below:

```java
public class Bacterium {
    public int idealPH;

    public Bacterium(int pH) {
        idealPH = pH;
    }

    public void survive() {
        if (idealPH < 5) {
            System.out.println("Surviving in acidic condition!");
        } else if (idealPH < 8) {
            System.out.println("Surviving in neutral condition!");
        } else {
            System.out.println("Surviving in basic condition!");
        }    
    }
}
```

The constructor with the signature `public Bacterium(int pH)` is executed whenever we attempt to create a `Bacterium` using the `new` keyword and an integer parameter. For those familiar with Python, the concept of a constructor parallels the `__init__` method.

**Terminology Summary**



# Introduction to Arrays in Microbiology

Arrays in microbiology can be likened to how microbial cultures are organized in laboratories. We often arrange cultures or samples in systematic forms to perform experiments or for storage. In computational terms, arrays allow these ordered collections of similar items to be manipulated efficiently. Let's look at a simple scenario of creating a collection of bacterial strains.

```java
public class BacteriaArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five bacterial samples. */
        Strain[] strains = new Strain[5];
        strains[0] = new Strain("E. coli");
        strains[1] = new Strain("S. aureus");
    }
}
```

In the above example, we are organizing various bacterial strains into an array. Just like using petri dishes labeled with different strains, arrays provide an indexable collection of microbial data.

# Arrays of Microbial Objects

Arrays can equally be employed to organize more complex microbial data, such as sequences of microbial DNA or various properties of each microorganism. Consider this more advanced example where we want to manage an array of `Virus` objects:

```java
public class VirusArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two viruses. */
        Virus[] viruses = new Virus[2];
        viruses[0] = new Virus("Influenza", 100);
        viruses[1] = new Virus("Coronavirus", 80);

        /* Call a method associated with a specific virus. */
        viruses[0].transmit();
    }
}
```

Here, `Virus` objects are stored in an array, akin to maintaining a collection of viral cultures in a series of vials, each with unique properties.

### Class Methods vs. Instance Methods

In the realm of microbiology, class methods and instance methods can be paralleled to universal microbial operations and specific sample manipulations respectively.

- **Class methods**, similar to universal lab procedures.
- **Instance methods**, like handling a particular sample or strain.

Instance methods work with specific microbial instances. For example, activating a particular enzyme in one strain. Static methods, on the other hand, operate at a broader scale, such as determining the optimum temperature for a class of microorganisms. For instance, the `Microbiology` class might offer a method determining the growth rate under certain conditions.

```java
rate = Microbiology.calculateGrowthRate(temp, humidity);
```

If `calculateGrowthRate` were an instance method, erroneous complexity would ensue for static descriptive utilities.

Sometimes, combining both methods in microbiological classes can be beneficial. Consider comparing two bacterial strains regarding their resistance:

```java
public static Strain compareStrains(Strain s1, Strain s2) {
    if (s1.resistance > s2.resistance) {
        return s1;
    }
    return s2;
}
```

This class method could be invoked like so:

```java
Strain s1 = new Strain("B. subtilis", 50);
Strain s2 = new Strain("E. coli", 30);
Strain.compareStrains(s1, s2);
```

Using the static method by class reference is crucial here, differentiating from instance-only functionalities.

Alternatively, a non-static method could achieve strain comparison by operating on instances:

```java
public Strain compareResistance(Strain anotherStrain) {
    if (this.resistance > anotherStrain.resistance) {
        return this;
    }
    return anotherStrain;
}
```

Through:

```java
Strain s1 = new Strain("B. subtilis", 50);
Strain s2 = new Strain("E. coli", 30);
s1.compareResistance(s2);
```

Here, a specific strain adapts the method tailored to its unique properties.

### Exercise 1.2.1: Anomalous Code

Predict the behavior of this code snippet, though the design shows improper use:

```java
public static Strain compareResistance(Strain s1, Strain s2) {
    if (resistance > s2.resistance) {
        return this;
    }
    return s2;
}
```

## Static Variables in Microbiology

On the conversational plane of microbiology metadata, static variables manifest universally accepted facts or constants around bacterial classification and taxonomy. For instance, recognizing a bacterium's official nomenclature:

```java
public class Bacterium {
    public int effectiveness;
    public static String taxonomy = "Bacillus subtilis";
    ...
}
```

Accessing these inherent class properties, like `Bacterium.taxonomy`, enforces the distinction from dynamic instance data, akin to setting consistent media formulations in experiments.

Though technically permissible, referring to static variables through instances (e.g., `b.taxonomy`) can obscure clarity, paralleling misleading microbial attribute assignments in research.

### Exercise 1.2.2: Class and Taxonomy Discussion

Engage with this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### bacterial genome sequence <a href="#bacterial-genome-sequence" id="bacterial-genome-sequence"></a>

With what we've learned so far, it's time to demystify the genome sequence annotation we've been using for analyzing bacterial DNA. Breaking it into pieces, we have:

* `public`: Refers to publicly accessible regions of the genome.
* `static`: Indicates a static region of DNA, not associated with any dynamic mutations.
* `void`: Denotes a region with no coding function.
* `main`: This is the primary sequence of interest, often the origin of replication.
* `String[] args`: Represents an array of nucleotide sequences that are passed to genetic analysis protocols.

**Command Line Arguments in Sequencing**

Since the genome sequence is processed by the genetic interpreter (bioinformatics software) itself rather than another sequence, it is the software's job to supply these sequences. They usually refer to input data identifiers or parameters for analysis. For example, consider the program `SeqDemo` below:

```java
public class SeqDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program prints out the 0th nucleotide sequence identifier, e.g.

```
$ java SeqDemo genome1 genome2 genome3 genome4

genome1
```

In the example above, `args` will be an array of String identifiers, where the entries are {"genome1", "genome2", "genome3", "genome4"}.

**Summing Nucleotide Counts**

**Exercise 1.2.3**: Try to write a program that sums up the nucleotide counts from different genome sequence identifiers, assuming they are provided in numerical format. For a solution, see the webcast or the code provided on GitHub.

#### Using Bioinformatics Tools <a href="#using-bioinformatics-tools" id="using-bioinformatics-tools"></a>

One of the most important skills as a microbiologist is knowing how to find and use existing bioinformatics tools and databases. In the glorious modern era, it is often possible to save yourself tons of lab work and verification by turning to online resources for help.

In this course, you're welcome to do this, with the following caveats:

* Do not use databases or software libraries that we do not provide.
* Cite your sources.
* Do not search for solutions for specific lab exercises or project problems.

For example, it's fine to search for "convert nucleotide sequence to protein". However, it is not OK to search for "Project GenomeLab Berkeley".

For more on collaboration and academic honesty policy, see the course syllabus.