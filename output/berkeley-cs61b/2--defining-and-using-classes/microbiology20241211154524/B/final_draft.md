# Object-Oriented Programming in Microbiology with Java

This chapter introduces fundamental concepts of object-oriented programming in Java through the lens of microbiological organisms and operations. The chapter begins by explaining the difference between static methods and instance methods, using a `Dog` class as an illustrative example. Instance variables and methods are explained, providing the foundation for understanding how objects represent individual entities with specific characteristics or behaviors within a Java program. The section progresses by drawing parallels between Java constructs and microbiological concepts, demonstrating how to model microorganisms such as bacteria with different survival conditions.

Throughout the chapter, readers learn to structure classes and methods in Java by implementing biological examples such as bacteria and viruses. The chapter covers creating classes to represent varied bacterial types that thrive in distinct environments (e.g., acidophiles and alkaliphiles). It also illustrates utilizing arrays to simulate collections of microbial strains, akin to laboratory setups. Furthermore, the chapter delves into the distinction between class methods and instance methods and how static elements can serve to represent universal properties or behaviors of microorganisms. By embedding microbiology into programming exercises, the chapter offers a practical approach to understanding Java class structures, constructors, and array usage, culminating in a simplified bioinformatics application example to consolidate learning.

#### Defining and Using Biological Simulations

In this section, we will explore how concepts from microbiology can be modeled using object-oriented programming in Java. Fundamental knowledge of cell biology, particularly the difference between prokaryotic and eukaryotic organisms, will enhance your understanding, though we will simplify these concepts for the sake of clarity.

### Prokaryotic Organisms in Object-Oriented Programming

Prokaryotic organisms, such as bacteria, are characterized by their simple cellular structures. We can draw parallels between these organisms and simple Java classes. Consider a class representing a bacterium:

```java
public class Bacterium {
    public static void replicateDNA() {
        System.out.println("Replicating DNA!");
    }
}
```

This `Bacterium` class defines a method `replicateDNA()`. However, to execute this functionality, we need a `main` method, which is the entry point of any Java application. Let’s use a `MicrobialSimulator` class to run our bacterium's behavior:

```java
public class MicrobialSimulator {
    public static void main(String[] args) {
        Bacterium.replicateDNA();
    }
}
```

When executed, this program will output:
```
Replicating DNA!
```

### Simulating Life Functions and Adaptability

Bacteria can survive in diverse environments, and we can simulate this diversity by utilizing instance variables and methods in Java. Let's improve our representation of bacteria's adaptability to pH environments with instance-based modeling:

```java
public class Bacterium {
    private int idealPH;

    public Bacterium(int idealPH) {
        this.idealPH = idealPH;
    }

    public void survive() {
        if (idealPH < 4) {
            System.out.println("Thriving in acidic conditions!");
        } else if (idealPH <= 7) {
            System.out.println("Thriving in neutral conditions!");
        } else {
            System.out.println("Thriving in alkaline conditions!");
        }
    }
}
```

In `MicrobialSimulator`:

```java
public class MicrobialSimulator {
    public static void main(String[] args) {
        Bacterium acidophile = new Bacterium(3);
        Bacterium neutralophile = new Bacterium(7);

        acidophile.survive();
        neutralophile.survive();
    }
}
```

The output:
```
Thriving in acidic conditions!
Thriving in neutral conditions!
```

### Key Java Concepts Recap

- **Instance Variables**: Variables like `idealPH`, specific to an instance of a class.
- **Constructors**: Special methods like `Bacterium(int idealPH)` that initialize object settings.
- **Instance Methods**: Non-static methods such as `survive()`, which operate on object instances.
- **Class Instantiation**: Creating an object of a class using the `new` keyword.
- **Client Classes**: Classes such as `MicrobialSimulator` that utilize other classes.

Understanding these Java fundamentals and how they relate to biological systems can facilitate a better grasp of both programming and biological processes. By constructing models that emulate real-world biological behaviors, one can appreciate the power of programming as a simulation tool and maintain a balance in learning key CS concepts.


# Introduction to Arrays in Microbiology

In microbiology laboratories, the organization of microbial cultures mirrors how arrays function in computer science. Arrays allow the efficient manipulation of ordered collections of items, similar to the systematic arrangement of cultures or samples. Consider a scenario where we create a collection of bacterial strains.

```java
public class BacteriaArrayDemo {
    public static void main(String[] args) {
        // Initialize an array to hold five bacterial strains.
        Strain[] strains = new Strain[5];
        strains[0] = new Strain("E. coli");
        strains[1] = new Strain("S. aureus");
    }
}
```

In this example, we organize various bacterial strains into an array, akin to labelling petri dishes with different strains. Arrays provide an indexable collection, facilitating the management of microbial data.

# Arrays of Microbial Objects

Arrays can also organize more complex microbial data, such as microbial DNA sequences or other properties of microorganisms. For instance, consider the task of managing an array of `Virus` objects:

```java
public class VirusArrayDemo {
    public static void main(String[] args) {
        // Create an array of two virus instances.
        Virus[] viruses = new Virus[2];
        viruses[0] = new Virus("Influenza", 100);
        viruses[1] = new Virus("Coronavirus", 80);

        // Invoke a method of a particular virus object.
        viruses[0].transmit();
    }
}
```

This setup represents a collection of virus examples, similar to handling viral cultures with distinct properties.

### Differentiating Class Methods and Instance Methods

In microbiology, the difference between class methods and instance methods is reflected in universal operations versus specific sample manipulations.

- **Class methods**: Resemble universal laboratory procedures applying to all microorganisms.
- **Instance methods**: Correspond to specific actions on individual samples or strains.

Instance methods handle specific instances, such as activating an enzyme in one strain. In contrast, static methods might calculate broader concepts, like the growth rate for a microorganism class.

```java
rate = Microbiology.calculateGrowthRate(temp, humidity);
```

If `calculateGrowthRate` were an instance method, it would unnecessarily complicate its universal application.

In certain cases, combining both methods helps analyze bacterial strains' resistance:

```java
public static Strain compareStrains(Strain s1, Strain s2) {
    if (s1.resistance > s2.resistance) {
        return s1;
    }
    return s2;
}
```

The method is invoked as follows:

```java
Strain s1 = new Strain("B. subtilis", 50);
Strain s2 = new Strain("E. coli", 30);
Strain.compareStrains(s1, s2);
```

Using static methods at the class level differentiates them from instance-specific functionalities. Conversely, an instance method can instigate strain comparisons:

```java
public Strain compareResistance(Strain anotherStrain) {
    if (this.resistance > anotherStrain.resistance) {
        return this;
    }
    return anotherStrain;
}
```

Exploiting it as:

```java
Strain s1 = new Strain("B. subtilis", 50);
Strain s2 = new Strain("E. coli", 30);
s1.compareResistance(s2);
```

A particular strain can thus leverage its customized method for individual evaluation.

### Exercise 1.2.1: Identify Code Flaws

Predict the behavior of the flawed code:

```java
public static Strain compareResistance(Strain s1, Strain s2) {
    if (this.resistance > s2.resistance) {
        return this;
    }
    return s2;
}
```

## Static Variables in Microbiology

In microbiology, universally accepted facts and constants resemble static variables, providing stable metadata concerning bacterial classification and taxonomy. For instance, a bacterium's official taxonomy:

```java
public class Bacterium {
    public int effectiveness;
    public static String taxonomy = "Bacillus subtilis";
    //...
}
```

Accessing `Bacterium.taxonomy` separates class-level properties from dynamic instance data, akin to maintaining consistent media across experiments.

### Exercise 1.2.2: Classification Exploration

Engage with the exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### Bacterial Genome Sequence Analysis <a href="#bacterial-genome-sequence" id="bacterial-genome-sequence"></a>

In our exploration of bacterial DNA, understanding the annotation of genome sequences is crucial. Let’s break down what each part signifies:

* `public`: Indicates major regions of the genome accessible for transcriptional activity.
* `static`: Designates conserved regions within the genome, which remain unchanged despite environmental changes.
* `void`: Describes non-coding regions with no currently identified function.
* `main`: Represents the core sequence of interest, often linked to essential cellular functions such as replication origin.
* `String[] args`: Symbolizes an array of nucleotide sequences handed to computational analysis tools for further examination.

**Command Line Parameters in Genomic Analysis**

In computational genomics, bioinformatics software handles the interpretation. It’s tasked with managing the sequence data, often taking command line inputs to dictate its operation. Consider the simple Java program `SeqDemo` as an illustration:

```java
public class SeqDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

Executing this program with command line inputs will display the first entered genome sequence identifier:

```
$ java SeqDemo genome1 genome2 genome3 genome4

genome1
```

Here, `args` captures the sequence identifiers, displaying "genome1" as the first in the list: {"genome1", "genome2", "genome3", "genome4"}.

**Calculating Total Nucleotide Counts**

**Exercise 1.2.3**: Develop a program that accumulates nucleotide counts from multiple genome sequence identifiers, assuming they are entered as numerical representations. To find the solution, consult the resources available in the coursework materials.

#### Leveraging Bioinformatics Resources <a href="#using-bioinformatics-tools" id="using-bioinformatics-tools"></a>

A key skill in microbiology is efficiently utilizing bioinformatics resources. Modern technologies allow for significant data manipulation and analysis, reducing the need for extensive lab work.

In this course, feel free to use various bioinformatic tools, keeping these guidelines in mind:

* Restrict usage to databases and software libraries outlined in course resources.
* Always reference your sources appropriately.
* Avoid seeking solutions for specific assignments or project queries online.

For instance, it’s appropriate to search for how to "translate nucleotide sequences to proteins," but searching for "Project Solutions for GenomeLab Berkeley" is against academic policies.

Consult the course syllabus for more details on collaboration and academic integrity policies.