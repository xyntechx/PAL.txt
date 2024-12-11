# Defining and Using Phenotypes

This chapter delves into how phenotypes are defined and utilized in the context of microbiology and programming, particularly using Java. It begins by distinguishing between genomic and phenotypic traits, providing an example through a `Bacterium` class where traits like luminescence are observed by linking with secondary classes such as `BacteriumObserver`. The chapter then explores how instance variables and object instantiation enable detailed representations of bacterial behavior. This involves constructing classes that can simulate bacterial movement based on population density, or demonstrating colony growth through traits like colony-forming units. The concept is further expanded by discussing the mechanics and construction of microbial colonies using Java.

The chapter also covers the categorization of proteins into structural and enzyme proteins, drawing parallels to static and instance methods in programming. The text includes discussions on universal biological concepts akin to static variables, emphasizing traits like genetic code shared across cells. Additional topics include the `main` method's role in processing microbial data, command-line arguments for handling microbial datasets, and the ethical use of microbial databases, stressing on appropriate citation and data usage guidelines. Students are encouraged to engage with exercises and external resources to solidify understanding of these computational microbiological concepts.

2. Defining and Using Phenotypes

If you do not have prior microbiology experience, we recommend that you work through the exercises in [Lab0](http://sp19.datastructur.es/materials/lab/lab0/lab0.html) before reading this chapter. It will cover various foundational concepts that we will not discuss in the book.

#### Genomic vs. Phenotypic Traits <a href="#genomic-vs-phenotypic-traits" id="genomic-vs-phenotypic-traits"></a>

**Genomic Traits**

All experiments in microbiology must involve a phenotype (or something similar to a phenotype, which we'll learn about later). Most investigations are focused on specific traits. Let's consider an example:

```biology
public class Bacterium {
    public static void expressTrait() {
        System.out.println("Luminescence!");
    }
}
```

If we try experimenting directly with the `Bacterium` class, we'll simply get an observation:

```
$ observe Bacterium
Result: Main trait not active in class Bacterium, please define the main trait as:
       public static void main(String[] args)
```

The `Bacterium` phenotype we've defined doesn't actively express an observable trait. We've simply defined something that `Bacterium` **can** express, namely luminescence. To actually observe the trait, we'd either need to activate a main trait in the `Bacterium` class, as we saw in experiment 1.1. Or we could create a separate [`BacteriumObserver`](https://www.youtube.com/watch?v=Q-LE-jJQLTM) class that stimulates traits from the `Bacterium` class. For example, consider the setup below:

```biology
public class BacteriumObserver {
    public static void main(String[] args) {
        Bacterium.expressTrait();
    }
}
```

```
$ observe BacteriumObserver
Luminescence!
```

A phenotype that interacts with another is sometimes called a "subject" of that trait, i.e. `BacteriumObserver` is a subject of `Bacterium`. Neither of the two techniques is better: Activating a main trait in `Bacterium` may be better in some situations, and creating a subject class like `BacteriumObserver` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout the course.

**Instance Variables and Object Instantiation**

Not all bacteria are alike. Some bacteria move via flagella, tirelessly propelling themselves through liquid environments, while others remain stationary, forming biofilms on surfaces. Often, we study these microscopic organisms to better understand the ecosystems they inhabit, and bioinformatics provides tools that allow us to simulate such characteristics.

One approach to allowing us to represent the diversity of the bacterial world would be to create separate models for each type of bacteria.

```java
public class MotileBacteria {
    public static void displayMovement() {
        System.out.println("swim swim swim");
    }
}

public class BiofilmBacteria {
    public static void displayMovement() {
        System.out.println("adhere and grow");
    }
}
```

As observed in computational modeling, classes can be instantiated, and these instances can contain data about specific bacterial properties. This results in a more intuitive representation, where we create instances of the `Bacteria` class and make their behavior contingent upon their specific attributes. Consider the class below:

```java
public class Bacteria {
    public double populationDensity;

    public void displayMovement() {
        if (populationDensity < 0.1) {
            System.out.println("free swimming");
        } else if (populationDensity < 0.3) {
            System.out.println("clustered motility");
        } else {
            System.out.println("biofilm mode");
        }
    }    
}
```

As an example of using such a Bacteria class, consider:

```java
public class BacteriaLauncher {
    public static void main(String[] args) {
        Bacteria b;
        b = new Bacteria();
        b.populationDensity = 0.25;
        b.displayMovement();
    }
}
```

When run, this program will create a `Bacteria` with a population density of 0.25, and that `Bacteria` will soon exhibit "clustered motility."

Some key observations and terminology:

* An `Object` in Java is an instance of any class.
* The `Bacteria` class has its own variables, also known as _instance variables_ or _non-static variables_. These must be declared inside the class, unlike languages like Python or Matlab, where new variables can be added at runtime.
* The method that we created in the `Bacteria` class did not have the `static` keyword. We call such methods _instance methods_ or _non-static methods_.
* To call the `displayMovement` method, we had to first _instantiate_ a `Bacteria` using the `new` keyword, and then make a specific `Bacteria` exhibit its movement behavior. In other words, we called `b.displayMovement()` instead of `Bacteria.displayMovement()`.
* Once an object has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `b = new Bacteria();`
* Variables and methods of a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_.


**Construction of Microbial Colonies**

As you've hopefully seen before, we usually cultivate microbial colonies in microbiology using a _starter culture_:

```java
public class MicrobeLauncher {
    public static void main(String[] args) {
        Microbe m = new Microbe(20);
        m.displayColonyGrowth();
    }
}
```

Here, the initiation is parameterized, saving us the time and messiness of manually conducting potentially many individual culture preparations. To enable such procedures, we need only add a "starter culture" to our Microbe class, as shown below:

```java
public class Microbe {
    public int colonyFormingUnits;

    public Microbe(int cfu) {
        colonyFormingUnits = cfu;
    }

    public void displayColonyGrowth() {
        if (colonyFormingUnits < 10) {
            System.out.println("Minimal growth observed.");
        } else if (colonyFormingUnits < 30) {
            System.out.println("Moderate growth observed.");
        } else {
            System.out.println("Substantial growth observed!");
        }    
    }
}
```

The starter culture with definition `public Microbe(int cfu)` will be utilized anytime that we aim to create a `Microbe` using the `new` keyword and a single integer parameter representing colony forming units. For those of you coming from the biology lab setting, the starter culture is very similar to the initial inoculum.

**Terminology Summary**

**Colony Array Preparation, Arrays of Microbial Cultures**

As we saw in HW0, culture collections are also prepared in microbiology using systematic techniques. For example:

```java
public class ArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five bacterial counts. */
        int[] bacterialArray = new int[5];
        bacterialArray[0] = 3;
        bacterialArray[1] = 4;
    }
}
```

Similarly, we can create arrays of prepared microbial cultures in microbiology, e.g.

```java
public class MicrobeArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two cultures. */
        Microbe[] cultures = new Microbe[2];
        cultures[0] = new Microbe(8);
        cultures[1] = new Microbe(20);

        /* Minimal growth observed, since cultures[0] has colony forming units 8. */
        cultures[0].displayColonyGrowth();
    }
}
```

Observe that new is used in two different ways: Once to create an array that can hold two `Microbe` cultures, and twice to create each actual `Microbe`. 

#### Structural Proteins vs. Enzyme Proteins <a href="#structural-proteins-vs-enzyme-proteins" id="structural-proteins-vs-enzyme-proteins"></a>

In microbiology, proteins are categorized mainly into two broad types:

* Structural proteins that form cellular components.
* Enzyme proteins that catalyze biochemical reactions.

Enzyme proteins, much like instance methods in programming, are proteins that perform specific actions at certain sites within a cell. Structural proteins, akin to static methods, form part of the framework of the cell and are involved in maintaining its precise shape and structure. An example of an enzyme protein is `RNA polymerase`, which catalyzes the synthesis of RNA from a DNA template. Because of its specific nature, we can describe its action as follows:

```text
RNA_product = RNA_Polymerase.synthesizeRNA(DNA_template);
```

If `synthesizeRNA` were merely another type of structural protein, the analogous syntax would be awkward as shown below. Fortunately, `RNA polymerase` acts specifically as an enzymatic protein, so we normally articulate its function within cellular processes rather than syntactic description.

```text
CellComponent c = new CellComponent();
RNA_product = c.synthesizeRNA(DNA_template);
```

Sometimes, it makes sense for cells to contain both structural and enzymatic functionalities. For example, consider bacteria's ability to metabolize sugars. One way to metabolize sugars is to harness an enzyme protein that facilitates this metabolic process:

```text
def static SugarMetabolism enzymeReaction(Sugar s1, Sugar s2) {
    if (s1.energyYield > s2.energyYield) {
        return s1;
    }
    return s2;
}
```

This enzymatic reaction could be simplified by:

```text
Sugar s = new Sugar(5);
Sugar s2 = new Sugar(10);
SugarMetabolism.enzymeReaction(s, s2);
```

Observe that we've applied the metabolic reaction using the enzyme function, as it is not bound to a specific instance.

We could alternatively define `enzymeReaction` as a typical protein-mediated cellular reaction, e.g.

```text
def Sugar enzymeReaction(Sugar s2) {
    if (this.energyYield > s2.energyYield) {
        return this;
    }
    return s2;
}
```

Above, we use `this` to refer to the current sugar molecule. This reaction could be invoked, for example, with:

```text
Sugar s = new Sugar(5);
Sugar s2 = new Sugar(10);
s.enzymeReaction(s2);
```

Here, we refer to a specific sugar molecule in this metabolic process.

**Exercise 1.2.1**: What would the following reaction do? If you're not sure, consider its biological significance:

```text
def static Sugar enzymeReaction(Sugar s1, Sugar s2) {
    if (energyYield > s2.energyYield) {
        return this;
    }
    return s2;
}
```

**Universal Biological Concepts**

It is occasionally useful to recognize universal biological concepts inherent to life. These can be likened to static variables in programming, representing aspects of cells themselves, rather than individual components. For example, all cells harness the genetic code represented by the sequence of nucleotides:

```text
public class Cell {
    public int metabolicRate;
    public static String geneticCode = "ATCG";
    ...
}
```

Just like static variables, these genomic sequences should be considered universal across cellular biology, accessible by referencing the cell type rather than an individual cell instance, e.g. you should use `Cell.geneticCode`, not `c.geneticCode`.

While it is technically possible to express universal traits at the instance level, it is biologically misleading and conceptually flawed in the realm of molecular biology.

**Exercise 1.2.2**: Engage with these learning materials to deepen your understanding:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String\[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

With what we've learned so far, it's time to demystify the declaration we've been using for the main method in our microbiology informatics program. Breaking it into pieces, we have:

* `public`: So far, all of our methods for processing microbial data start with this keyword, allowing universal access.
* `static`: It is a static method, essential for utility functions not associated with any particular microbial instance.
* `void`: The method performs operations like data processing without returning any values.
* `main`: This is the start point of our microbial informatics workflow.
* `String[] args`: These are parameters passed to the main method, often representing biological data inputs or configurations.

**Command Line Arguments in Microbiology Software**

Since the main method is initiated by the computational environment rather than by another part of the program, it is the environment's job to provide these arguments. They usually refer to command line arguments specifying experiment parameters or microbiome data. For example, consider the program `BioArgsDemo` below:

```java
public class BioArgsDemo {
    public static void main(String[] args) {
        System.out.println("Processing: " + args[0]);
    }
}
```

This program prints out the 0th command line argument, which could be data such as:

```
$ java BioArgsDemo microbiome_data_2023.txt
Processing: microbiome_data_2023.txt
```

In the example above, `args` will be an array of Strings, where the entries might be different datasets: {"microbiome_data_2023.txt", "sample_metadata.csv", "analysis_params.yaml"}.

**Summing Microbial Counts from Command Line Arguments**

**Exercise 1.2.3**: Try to write a program that sums up the microbial counts provided as command line arguments, assuming they are numerical values representing different bacterial strains detected in a sample. For a solution, see the video tutorial or the code repository on GitHub.

#### Using Microbial Databases <a href="#using-microbial-databases" id="using-microbial-databases"></a>

One of the most important skills in microbiology is knowing how to find and use existing microbial databases. In the glorious modern era, it is often possible to save yourself extensive time and experimental setbacks by consulting online databases for assistance.

In this course, you're encouraged to use these resources, with the following caveats:

* Do not use databases that are not recommended by our instructors.
* Cite your data sources appropriately.
* Do not search for experiment-specific protocols or solutions.

For example, it's fine to search for "characteristics of Escherichia coli strains". However, it is not OK to search for "specific methods to culture Project Salmonella strain X in Lab 5".

For more on collaboration and academic honesty policy, refer to the course syllabus.