# Defining and Using Microbial Classes

In this chapter, we delve into the principles of object-oriented programming by defining and using classes to model microbial entities. Starting with static methods, we explore how all microbial simulations must be encapsulated within a class. By demonstrating the use of static methods through Java examples, such as in the `Bacterium` and `CultureLauncher` classes, we illustrate how these methods are invoked. Static methods, being associated with classes rather than instances, contrast with non-static instance methods that cater to individual objects and their properties.

Further, the chapter examines object instantiation and emphasizes the rich diversity of microbial life by using instance variables to differentiate between bacterial species. We learn how instance methods use the specific attributes of an instantiated object to determine behavior, exemplified by cell density impacting metabolic activity in the `Bacteria` class. Additionally, the chapter covers microbial concepts like spore formation and colony assembly, highlighting the importance of constructors in crafting parameterized instances. Finally, we discuss universal microbial properties and explore the distinctions between enzyme activities within cells and interactions among different microbes, enriching our understanding of microbial systems and the dynamic intercellular processes that dominate their environments.

2. Defining and Using Microbial Classes

If you do not have prior microbial modeling experience, we recommend that you work through the exercises in [MW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before reading this chapter. It will cover various syntax issues that we will not discuss in the book.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

All code in microbial simulations must be part of a class (or something similar to a class, which we'll learn about later). Most processes are written inside of methods. Let's consider an example:

```java
public class Bacterium {
    public static void reproduce() {
        System.out.println("Splitting into two!");
    }
}
```

If we try running the `Bacterium` class, we'll simply get an error message:

```
$ java Bacterium
Error: Main method not found in class Bacterium, please define the main method as:
       public static void main(String[] args)
```

The `Bacterium` class we've defined doesn't do anything. We've simply defined something that `Bacterium` **can** do, namely reproduce. To actually run the class, we'd either need to add a main method to the `Bacterium` class, as we saw in Chapter 1.1. Or we could create a separate [`CultureLauncher`](https://www.youtube.com/watch?v=Q-LE-jJQLTM) class that runs methods from the `Bacterium` class. For example, consider the program below:

```java
public class CultureLauncher {
    public static void main(String[] args) {
        Bacterium.reproduce();
    }
}
```

```
$ java CultureLauncher
Splitting into two!
```

A class that uses another class is sometimes called a "client" of that class, i.e. `CultureLauncher` is a client of `Bacterium`. Neither of the two techniques is better: Adding a main method to `Bacterium` may be better in some situations, and creating a client class like `CultureLauncher` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout the course.

**Microbial Context**

In the microbial world, static methods can be likened to universal functions applicable to all bacteria within a certain class or criteria, such as reproduction through binary fission. This method does not rely on the specific attributes of an individual bacterium, akin to a static method in programming which isn't dependent on instance variables. However, understanding microbial interactions is crucial. While static methods cover broad, shared actions, non-static methods would allow us to specify interactions and dependencies, giving deeper insights into microbial ecosystems. For example, methods to simulate nutrient consumption, spore formation, or response to environmental changes, require detailed microbe-specific data to provide informative simulations, just as non-static methods require instance-specific data to perform unique functions.

**Instance Variables and Object Instantiation in Microbiology**

Not all bacteria share the same characteristics. While some bacteria, such as Lactobacillus, are involved in the souring of milk, others contribute to the breakdown of dead plants and animals, promoting nutrient cycling. Java's syntax allows us to model the complexity of microbial life forms in our programming.

To encapsulate the distinctive features of bacterial species, separate classes could be created for each bacterium type.

```java
public class Lactobacillus {
    public static void generateAcid() {
        System.out.println("Lactic acid production...");
    }
}

public class DecomposerBacteria {
    public static void breakDownMatter() {
        System.out.println("Decomposing organic matter...");
    }
}
```

However, a more refined strategy involves creating instances of a more generalized `Bacteria` class. Here, object behavior can be influenced by the properties of individual bacteria, such as cell density or enzyme activity. Let us examine the refined version:

```java
public class Bacteria {
    public int cellDensity;
    public boolean enzymeActivity;

    public void performFunction() {
        if (cellDensity < 1000) {
            System.out.println("Minimal metabolic activity!");
        } else if (cellDensity < 10000) {
            System.out.println("Moderate metabolic activity.");
        } else {
            System.out.println("High metabolic activity!");
        }
        if (enzymeActivity) {
            System.out.println("Enzymes actively breaking down substrates.");
        }
    }    
}
```

Usage of this `Bacteria` class in a practical scenario is seen below:

```java
public class BacteriaLab {
    public static void main(String[] args) {
        Bacteria b = new Bacteria();
        b.cellDensity = 5000;
        b.enzymeActivity = true;
        b.performFunction();
    }
}
```

Running this program will produce a `Bacteria` with a cell density of 5000 and active enzymes, indicating both "Moderate metabolic activity" and "Enzymes actively breaking down substrates."

Key observations and terminology include:

* An `Object` in Java is an instance of any class.
* The `Bacteria` class contains _instance variables_ which uniquely characterize each instance, like `cellDensity` and `enzymeActivity`. These variables help differentiate one bacterial object from another.
* Methods without the `static` keyword, such as `performFunction`, are _instance methods_ accessed through an instance of the class.
* To invoke the `performFunction` method, we had to _instantiate_ a `Bacteria` object using the `new` keyword, creating a unique instance with its own state.
* After instantiation, the object can be _assigned_ to a variable of the type `Bacteria`, e.g., `b = new Bacteria();`
* Class members, including variables and methods, are accessed using _dot notation_.

This approach gives us a flexible framework to model various biological processes, while adhering to essential object-oriented programming principles laid out by Java.

**Spore Formation in Microbiology and Object-Oriented Programming**

Microbiology offers rich insights into the world of bacterial spore formation, an extreme survival strategy employed by certain bacteria. This process can be likened to certain programming tasks using object-oriented principles in Java.

Let's consider how we model sporulation using Java. Bacterial spores are categorized based on their structural robustness, akin to instantiating objects with varied properties:

```java
public class SporeLauncher {
    public static void main(String[] args) {
        Spore s = new Spore(2);
        s.release();
    }
}
```

The class `Spore` is designed to encapsulate the concept of sporulation, defining its properties through constructors. The constructor allows us to adjust the conditions, like spore coat thickness, impacting the spore's resistance. Here is a deeper dive into how this class is constructed:

```java
public class Spore {
    public int thickness; // spore coat thickness

    public Spore(int t) {
        thickness = t;
    }

    public void release() {
        if (thickness < 1) {
            System.out.println("Spores released easily!");
        } else if (thickness < 2) {
            System.out.println("Moderately resistant spore!");
        } else {
            System.out.println("Highly resistant spore structure!");
        }    
    }
}
```

In this class, the constructor `Spore(int t)` corresponds to setting the initial conditions for spore formation, akin to proteins folding during cellular processes. The conditional logic within the `release()` method maps back to biological scenarios where different spore coats confer varying levels of environmental resistance.

**Terminology Summary**

**Colony Formation and Programming Parallels**

Much like bacterial colonies, which arise from the growth of bacterial cells in optimal conditions, Java arrays can be similarly used to represent collections of objects. Let's see how a bacterial colony might be represented:

```java
public class BacteriaDemo {
    public static void main(String[] args) {
        // Initialize a bacterial colony with five slots, initially two are active.
        int[] initialColony = new int[5];
        initialColony[0] = 1; // represents a single bacterium
        initialColony[1] = 1;
    }
}
```

Java permits us to also mimic the formation of spore assemblies, which biologists often encounter when studying sporulation patterns:

```java
public class SporeAssemblyDemo {
    public static void main(String[] args) {
        // Create an array for a spore assembly with varying resistance.
        Spore[] spores = new Spore[2];
        spores[0] = new Spore(1);
        spores[1] = new Spore(3);

        // Demonstrate the release process, which depends on spore's thickness.
        spores[0].release();
    }
}
```

The array here mirrors an assembly of spores, each spore potentially showing different reactions based on its formation criteria—thickness in this case. Such coding analogies not only help to understand Java programming but also elucidate biological formation mechanisms, making the learning interface both rich and diverse. The parallels in setting initialization conditions stress important conceptual overlaps between coding patterns and biological development, ensuring a balanced and insightful educational experience.

#### Enzyme Activity vs. Microbial Interaction <a href="#enzyme-activity-vs-microbial-interaction" id="enzyme-activity-vs-microbial-interaction"></a>

Microbial systems provide a fascinating context to explore interactions on both intracellular and intercellular levels, relevant to computer science through simulation of interactions and modeling pathways.

* **Intracellular Enzyme Activity:** These are enzyme-catalyzed reactions within a single microbe that drive metabolic functions. A classic example is the glycolysis pathway, a series of reactions breaking down glucose to produce energy, ubiquitous in bacteria.

```javascript
let pyruvateContent = Glycolysis.glucoseBreakdown(100);
```

In this example, `glucoseBreakdown` is consistent across different bacterial species, demonstrating a universal intracellular process that independent bacterial strains can leverage.

When bacteria need to adapt to specific environments, understanding variations in enzymatic pathways via modular coding supports simulations of these adaptive mechanisms.

```javascript
let b = new Bacteria();
pyruvateContent = b.glycolysis(100);
```

* **Intercellular Microbial Interactions:** These occur between separate microbial entities, where characteristics or actions of one influence another. This is significant in microbial ecology and competition studies.

For instance, modeling interaction strength can be vital to predict outcomes in shared microbial environments:

```javascript
public static Bacteria dominateBacteria(Bacteria b1, Bacteria b2) {
    if (b1.interactionStrength > b2.interactionStrength) {
        return b1;
    }
    return b2;
}
```

This model demonstrates how interaction properties can be quantified and assessed in a comparative analysis:

```javascript
Bacteria b1 = new Bacteria(20);
Bacteria b2 = new Bacteria(10);
Bacteria.dominateBacteria(b1, b2);
```

To explore interaction dynamics further, integrating environmental variables can enrich these simulations. Consider modeling how nutrient availability modifies `interactionStrength` to simulate more complex ecosystems.

Similarly, an instance-based approach refines these models by accounting for particular strain attributes:

```javascript
public Bacteria dominateBacteria(Bacteria competitor) {
    if (this.interactionStrength > competitor.interactionStrength) {
        return this;
    }
    return competitor;
}
```

Understanding these principles allows scientists to study microbial dominance within controlled and variable ecosystems using tailored computational models.

**Exercise 1.2.1**: Analyze the effect of different interaction strengths:

```javascript
public static Bacteria dominateBacteria(Bacteria b1, Bacteria b2) {
    if (b1.getInteractionStrength() > b2.getInteractionStrength()) {
        return b1;
    }
    return b2;
}
```

Investigate how altering interaction conditions affects microbial outcomes and dominance patterns in simulations.

**Universal Microbial Properties**

Microbes can possess universal properties that are invariant across specific strains within a species, aiding in classification and identification:

```javascript
public class Bacteria {
    public int interactionStrength;
    public static String taxonomy = "Escherichia coli";
    ...
}
```

Utilizing these properties appropriately facilitates standardized communication in both scientific discourse and computational models, emphasizing their role in data fidelity.

**Exercise 1.2.2**: Reflect on these microbial concepts while observing potential outcomes:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

Engage with the exercise materials to understand how universal microbial properties enhance model consistency and how this relates to broader programming principles.

#### Bacteria as the Central Component <a href="#bacteria-central-role" id="bacteria-central-role"></a>

Bacteria are foundational organisms in microbiology due to their essential roles in various ecological processes. Let's explore some core characteristics of bacteria:

* **Cell Wall**: Nearly all bacteria possess a cell wall that provides structural support and shape, critical for their survival in diverse environments.
* **Flagella**: Many bacteria have one or more flagella, which are whip-like structures that enable them to move toward favorable conditions or away from hostile ones. This movement is often directional, such as chemotaxis, a response to chemical stimuli.
* **DNA**: Bacteria typically contain a single circular chromosome housed in the nucleoid. This genetic material commands all cellular functions and replication processes.
* **Ribosomes**: Comprising rRNA and proteins, these are the sites of protein synthesis within the bacterial cell, translating the genetic code into functional proteins.
* **Plasmids**: Small, circular, double-stranded DNA molecules that stand apart from chromosomal DNA, plasmids often carry genes that confer advantageous traits such as antibiotic resistance, enhancing bacterial adaptability.

**Role in Nutrient Cycling**

Bacteria play a crucial role in nutrient cycling, maintaining ecosystem balance through processes like decomposition, mineralization, and nitrogen fixation. Specific bacteria facilitate these cycles, making nutrients accessible to other organisms:

```text
Nitrogen Cycle Bacteria:
    - Nitrosomonas: Oxidizes ammonia to nitrite.
    - Nitrobacter: Converts nitrite to nitrate.
```

Such transformations are vital for nitrogen assimilation by plants, contributing to their growth and productivity:

```
Soil Microbes in Action:
Ammonia to Nitrite conversion by Nitrosomonas
Nitrite to Nitrate conversion by Nitrobacter
```

In nutrient cycling, bacteria sequentially transform nitrogen-containing compounds, moving from ammonia to nitrite and then to nitrate forms {"Ammonia", "Nitrite", "Nitrate"}.

**Summing Metabolic Outputs**

**Experiment 1.2.3**: Evaluate the total nitrogen processed by bacteria in various soil samples, assuming consistent microbial activity. Solutions and detailed procedures can be found in the lab manual or experiment guidelines provided in the relevant workbook.

#### Utilizing Computational Libraries in Bioinformatics <a href="#utilizing-computational-libraries" id="utilizing-computational-libraries"></a>

In the realm of computational biology, leveraging pre-existing libraries and frameworks is analogous to a microbiologist utilizing established biological techniques. These tools allow for efficient analysis and visualization of biological data, akin to accessing a detailed protocol for molecular procedures. Such resources are invaluable in this fast-evolving field, and effectively harnessing them can significantly enhance the progress and outcomes of biological studies.

When integrating these computational tools, consider the following principles:

* Ensure the libraries you choose are compatible with your project requirements and are supported by robust community or institutional backing.
* Clearly document and cite all libraries and tools employed in your analysis, following the academic standards applicable to both computer science and microbiology.
* Avoid over-reliance on automated solutions for research questions without a thorough understanding of the underlying algorithms and principles.

For instance, using a library for "sequence alignment algorithms" is beneficial for handling large datasets efficiently. However, relying solely on "pre-packaged pipeline unexplored for specific genome assembly" may lead to unsound interpretations, especially in novel research settings.

For guidance on ethical use and collaboration standards, refer to your institution's comprehensive policy on academic conduct and data sharing.