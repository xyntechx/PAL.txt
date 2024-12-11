# Defining and Using Phenotypes

This chapter delves into how phenotypes are defined and utilized in the context of microbiology and programming, particularly using Java. It begins by distinguishing between genomic and phenotypic traits, providing an example through a `Bacterium` class where traits like luminescence are observed by linking with secondary classes such as `BacteriumObserver`. The chapter then explores how instance variables and object instantiation enable detailed representations of bacterial behavior. This involves constructing classes that can simulate bacterial movement based on population density, or demonstrating colony growth through traits like colony-forming units. The concept is further expanded by discussing the mechanics and construction of microbial colonies using Java.

The chapter also covers the categorization of proteins into structural and enzyme proteins, drawing parallels to static and instance methods in programming. The text includes discussions on universal biological concepts akin to static variables, emphasizing traits like genetic code shared across cells. Additional topics include the `main` method's role in processing microbial data, command-line arguments for handling microbial datasets, and the ethical use of microbial databases, stressing on appropriate citation and data usage guidelines. Students are encouraged to engage with exercises and external resources to solidify understanding of these computational microbiological concepts.

2. Defining and Using Phenotypes

If you do not have prior microbiology experience, we recommend that you work through the exercises in [Lab0](http://sp19.datastructur.es/materials/lab/lab0/lab0.html) before reading this chapter. It will cover various foundational concepts that we will not discuss in the book.

#### Genomic vs. Phenotypic Traits <a href="#genomic-vs-phenotypic-traits" id="genomic-vs-phenotypic-traits"></a>

**Genomic Traits**

All experiments in microbiology must involve a phenotype—a trait that we can observe. In programming, this can be likened to methods or functionality that a class can exhibit. Let's consider an example:

```java
public class Bacterium {
    public static void expressTrait() {
        System.out.println("Luminescence!");
    }
}
```

If we attempt to make an observation about the `Bacterium` class directly, we'll merely describe the potential but not an active trait:

```
$ java Bacterium
Error: Main trait not executed in class Bacterium. Define the main trait as:
       public static void main(String[] args)
```

The `Bacterium` class represents a genomic trait which outlines what the organism can potentially express but isn't active by default. To actually express or "observe" a trait, we need to invoke it correctly. We can do this by implementing a `main` method within the `Bacterium` class, or by creating an auxiliary class to stimulate this trait. Below is a demonstration of the latter approach:

```java
public class BacteriumObserver {
    public static void main(String[] args) {
        Bacterium.expressTrait();
    }
}
```

When we run the `BacteriumObserver` class:

```
$ java BacteriumObserver
Luminescence!
```

Here, `BacteriumObserver` serves as an activating agent, a common analogy to a catalyst in biology. This highlights how one system (a biological observer or programming class) can invoke changes or activate traits in another. Neither the direct invocation in `Bacterium` nor using an external `BacteriumObserver` is superior. The choice depends on the complexity and requirement of the trait observation or expression experiments.

Balancing the expression of these traits or functions acknowledges not only the potential within our code but the pathways through which these potentials are realized, providing insightful parallels between computational and biological systems.

**Instance Variables and Object Instantiation**

In the natural world, bacteria exhibit a multitude of behaviors. Some bacteria propel themselves with the help of flagella, moving seamlessly through their liquid surroundings, while others form dense communities known as biofilms, adhering steadfastly to surfaces. Understanding these behaviors can provide insight into broader ecosystems, and computational tools such as bioinformatics can simulate and analyze such microbial characteristics.

To simulate the diversity of bacterial behaviors, we can represent different types of bacteria using distinct models. Consider a simple Java implementation:

```java
public class MotileBacteria {
    public void displayMovement() {
        System.out.println("swim swim swim");
    }
}

public class BiofilmBacteria {
    public void displayMovement() {
        System.out.println("adhere and grow");
    }
}
```

In computational modeling, we create objects—specific instances of a class—that can hold data reflecting the properties of individual bacteria. This allows for a more intuitive representation of bacterial behaviors by creating instances of a `Bacteria` class, with behaviors adapting based on certain attributes. Observe the following class:

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

Here, the method `displayMovement()` changes the behavior of the bacteria based on the population density, akin to how bacterial colonies shift behaviors in response to environmental conditions.

An application of the `Bacteria` class might look like this:

```java
public class BacteriaLauncher {
    public static void main(String[] args) {
        Bacteria b1 = new Bacteria();
        b1.populationDensity = 0.25;
        b1.displayMovement();
    }
}
```

This program instantiates a `Bacteria` object with a density of 0.25, resulting in its displaying "clustered motility" when the `displayMovement()` method is called.

Key observations and terminology include:

- An `Object` in Java is a specific instance of any class.
- The `Bacteria` class defines its own variables known as _instance variables_ or _non-static variables_, distinct from other programming languages where variable addition can occur at runtime.
- Methods, like `displayMovement` in the `Bacteria` class, without the `static` keyword are referred to as _instance methods_ or _non-static methods_.
- An object needs to be _instantiated_ using the `new` keyword before method calls can be made on it, as shown in `b1.displayMovement()` rather than `Bacteria.displayMovement()`.
- Instantiated objects are assigned to declared variables of the appropriate type, e.g., `Bacteria b1 = new Bacteria();`.
- The elements of a class—variables and methods—are also referred to as _members_ of the class.
- Members are accessed using _dot notation_, which involves appending the member name to the object name, separated by a dot.

**Construction of Microbial Colonies Using Java**

In microbiology, a _starter culture_ is often the beginning point for cultivating microbial colonies. We can draw an interesting parallel in computer science with object-oriented programming where object instantiation resembles cultivating colonies. Here's a simple Java code example:

```java
public class MicrobeLauncher {
    public static void main(String[] args) {
        Microbe m = new Microbe(20);
        m.displayColonyGrowth();
    }
}
```

In this example, we create a new instance of `Microbe` using a "starter culture" concept, represented by an integer parameter that stands for colony-forming units (CFU). The constructor of `Microbe` initializes the object's state based on this parameter. This is akin to inoculating a culture in a lab setup to observe its growth.

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

The constructor `public Microbe(int cfu)` initializes each `Microbe` object with a specified number of CFUs, much like how a biologist prepares a culture with certain growth conditions. Using the `new` keyword and providing relevant traits like the initial CFU count allows for systematic and reproducible culture creation, echoing efficiency in lab work.

**Arrays and Their Biological Counterparts**

Arrays in Java, such as collections of numbers or objects, can be likened to systematic arrangements of microbial cultures in microbiology:

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

Similarly, we orchestrate arrays of microbial cultures, where each element holds a specific microbial sample:

```java
public class MicrobeArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two cultures. */
        Microbe[] cultures = new Microbe[2];
        cultures[0] = new Microbe(8);
        cultures[1] = new Microbe(20);

        /* Display growth of each culture based on CFUs. */
        cultures[0].displayColonyGrowth();  // Minimal growth observed for CFUs=8
        cultures[1].displayColonyGrowth();  // Substantial growth observed for CFUs=20
    }
}
```

Here, the `new` keyword serves dual purposes: it first allocates memory for the array, and subsequently for each `Microbe` object. This organization mirrors the preparation of multiple experimental setups in the lab, emphasizing the importance of replication and data consistency both in programming and scientific experiments. Through this analogy, the breadth of programming concepts is clearer, reinforcing learning via a familiar biological context.

#### Structural Proteins vs. Enzyme Proteins <a href="#structural-proteins-vs-enzyme-proteins" id="structural-proteins-vs-enzyme-proteins"></a>

In microbiology, proteins are categorized mainly into two significant types:

* **Structural proteins** that form cellular components and maintain cell integrity.
* **Enzyme proteins** that catalyze biochemical reactions and facilitate cellular processes.

Enzyme proteins are akin to instance methods in programming because they perform specific actions using particular substrates at certain sites within a cell. For example, `RNA polymerase` catalyzes the synthesis of RNA from a DNA template, demonstrating a specific action within the cellular environment. This can be likened to the following programming analogy:

```java
RNA_product = RNA_Polymerase.synthesizeRNA(DNA_template);
```

If we incorrectly liken `RNA polymerase` to a structural role, the metaphor becomes misaligned with the true nature of enzymatic action:

```java
CellComponent c = new CellComponent();
RNA_product = c.synthesizeRNA(DNA_template);
```

Here, `synthesizeRNA` is improperly presented as a generic component action rather than an enzymatic function.

Cells often synergize structural and enzymatic roles to optimize functions. An example from bacterial metabolic pathways is their mechanism to metabolize sugars. In programming terms, a function might observe the following form:

```java
def static Sugar bestSugarMetabolism(Sugar s1, Sugar s2) {
    if (s1.energyYield > s2.energyYield) {
        return s1;
    }
    return s2;
}
```

This method can be utilized to determine the more energy-efficient sugar:

```java
Sugar s = new Sugar(5);
Sugar s2 = new Sugar(10);
Sugar result = SugarMetabolism.bestSugarMetabolism(s, s2);
```

Viewing this through a protein-mediated viewpoint with enzyme specificity:

```java
def Sugar enzymeReaction(Sugar s2) {
    if (this.energyYield > s2.energyYield) {
        return this;
    }
    return s2;
}
```

Here, `this` references the active sugar participant in the reaction, highlighting the enzyme-like nature in selecting substrates:

```java
Sugar s = new Sugar(5);
Sugar s2 = new Sugar(10);
Sugar result = s.enzymeReaction(s2);
```

**Exercise 1.2.1**: Analyze the following protein action. Discuss its implications and potential errors in mimicking enzymatic behaviors:

```java
def static Sugar enzymeReaction(Sugar s1, Sugar s2) {
    if (energyYield > s2.energyYield) {
        return this;
    }
    return s2;
}
```

**Universal Biological Concepts**

Just as in programming where certain global methods or variables exist, biology too exhibits universal principles. The genetic code, serving as a core template across all living entities, acts much like a static variable accessible to any cell type:

```java
public class Cell {
    public int metabolicRate;
    public static final String GENETIC_CODE = "ATCG";
    ...
}
```

These genomic sequences model a shared framework in biology, similar to static variables globally accessible by a reference to the class itself rather than any specific cell instance, succinctly exemplified by `Cell.GENETIC_CODE`.

While conceptualizing universal traits at the instance level is conceivable, it defies biological principles and misrepresents the global nature of genomic information.

**Exercise 1.2.2**: Engage further with these resources to deepen understanding:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slides: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

In our exploration of Java programming, particularly for applications in microbiology, let's delve into the structure of the main method that forms the cornerstone of our microbiological informatics applications. Breaking it down, we find:

* `public`: This keyword ensures the method can be accessed from anywhere, reflecting how microbial processes can often be observed and studied universally in different contexts.
* `static`: Used here to indicate this method belongs to the class itself rather than any object instance, similar to how certain microbial traits are consistent across an entire species rather than individual strains.
* `void`: The method carries out essential tasks—like data processing or simulation—without needing to return a result, akin to automated processes in microbial workflows that might proceed without direct human input.
* `main`: This method acts as the entry point to our application, similar to how specific reactions start metabolic pathways in cells.
* `String[] args`: These are inputs to the program, much like experimental conditions and variables provided to a biological experiment.

**Understanding Command Line Arguments Through Microbiology Applications**

The Java main method is invoked by the system when a program starts, with command line arguments often carrying critical parameters for microbiological simulations or data analyses. Consider the following `BioArgsDemo` program:

```java
public class BioArgsDemo {
    public static void main(String[] args) {
        System.out.println("Initiating Analysis on: " + args[0]);
    }
}
```

Executed with a command such as:

```
$ java BioArgsDemo sample_data_2023.txt
Initiating Analysis on: sample_data_2023.txt
```

In this scenario, `args` is an array of Strings, capable of holding multiple elements—akin to an array of different microbial species in a sample: {"sample_data_2023.txt", "experiment1_conditions.csv", "output_results.yaml"}.

**Practical Exercise: Summing Data Input from Command Line Arguments**

**Exercise 1.2.3**: Develop a Java program that can compute the total of microbial counts provided as command line arguments. Imagine each count represents a quantity of bacterial genes identified in sequenced sample data. Refer to the instructional video or GitHub repository for code implementation guidance. Be sure to handle potential errors such as non-numeric inputs as part of the exercise, reflecting the care required in biological data analysis.

#### Using Microbial Databases Effectively <a href="#using-microbial-databases-effectively" id="using-microbial-databases-effectively"></a>

In both computer science and microbiology, the ability to efficiently access and utilize databases is crucial. For microbiologists, online microbial databases are invaluable resources that can prevent redundant experimentation and guide research.

While you are encouraged to explore these rich databases, please observe these guidelines to ensure their correct use:

* Consult only those databases recommended by our instructors to guarantee data reliability and integrity.
* Follow strict citation practices to acknowledge the sources of your information.
* Avoid using databases to search for solutions specific to your ongoing experiments or assessments.

For instance, searching for general information such as "common antibiotic resistance in Escherichia coli" is encouraged. Conversely, querying databases for "techniques to culture specific Salmonella strain in Experiment 5" would breach academic guidelines.

To better understand collaboration standards and uphold academic honesty, please review our detailed course syllabus.