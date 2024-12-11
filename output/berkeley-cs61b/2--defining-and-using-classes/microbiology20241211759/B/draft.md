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

The `Bacterium` class we've defined doesn't do anything. We've simply defined something that `Bacterium` **can** do, namely reproduce. To actually run the class, we'd either need to add a main method to the `Bacterium` class, as we saw in chapter 1.1. Or we could create a separate [`CultureLauncher`](https://www.youtube.com/watch?v=Q-LE-jJQLTM) class that runs methods from the `Bacterium` class. For example, consider the program below:

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

**Instance Variables and Object Instantiation in Microbiology**

Not all bacteria are the same. Some bacteria might be responsible for the souring of milk, while others play a crucial role in the decomposition of organic matter. Often, we write programs to reflect the diverse features of the microbial world, and Java's syntax was crafted to seamlessly allow such representation.

One approach to capturing the diversity of bacteria would be to create separate classes for each type of Bacteria.

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

As you should have seen in the past, classes can be instantiated, and instances can hold data. This leads to a more natural approach, where we create instances of the `Bacteria` class and make the behavior of the `Bacteria` methods contingent upon the properties of the specific bacterium. To make this more concrete, consider the class below:

```java
public class Bacteria {
    public int cellDensity;

    public void performFunction() {
        if (cellDensity < 1000) {
            System.out.println("Minimal metabolic activity!");
        } else if (cellDensity < 10000) {
            System.out.println("Moderate metabolic activity.");
        } else {
            System.out.println("High metabolic activity!");
        }
    }    
}
```

As an example of using such a Bacteria, consider:

```java
public class BacteriaLab {
    public static void main(String[] args) {
        Bacteria b;
        b = new Bacteria();
        b.cellDensity = 5000;
        b.performFunction();
    }
}
```

When run, this program will create a `Bacteria` with a cell density of 5000, and that `Bacteria` will soon indicate "Moderate metabolic activity."

Some key observations and terminology:

* An `Object` in Java is an instance of any class.
* The `Bacteria` class has its own variables, also known as _instance variables_ or _non-static variables_. These must be declared inside the class, unlike languages like Python or Matlab, where new variables can be added at runtime.
* The method that we created in the `Bacteria` class did not have the `static` keyword. We call such methods _instance methods_ or _non-static methods_.
* To call the `performFunction` method, we had to first _instantiate_ a `Bacteria` using the `new` keyword, and then determine the activity level. In other words, we called `b.performFunction()` instead of `Bacteria.performFunction()`.
* Once an object has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `b = new Bacteria();`
* Variables and methods of a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_.


**Spore Formation in Microbiology**

As you've hopefully seen before, we usually categorize bacterial spores based on their structure and formation process using _sporulation_:

```java
public class SporeLauncher {
    public static void main(String[] args) {
        Spore s = new Spore(2);
        s.release();
    }
}
```

Here, the sporulation is parameterized, saving us the time and complexity of manually detailing potentially many environmental conditions and genetic expressions. To enable such a process, we need only add a "spore constructor" to our Spore class, as shown below:

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

The constructor with signature `public Spore(int t)` will be invoked anytime that we try to create a `Spore` using the `new` keyword and a single integer parameter. For those of you familiar with protein folding, the constructor is analogous to the initial folding stage in protein structure formation.

**Terminology Summary**

**Colony Formation, Assemblies of Bacteria**

As we saw in Lab0, bacterial colonies are also initiated by individual cells through growth in conducive environments. For example:

```java
public class BacteriaDemo {
    public static void main(String[] args) {
        /* Start a colony with two bacterial cells. */
        int[] initialColony = new int[5];
        initialColony[0] = 1; // single bacterium
        initialColony[1] = 1;
    }
}
```

Similarly, we can create assemblies of bacterial spores in microbiology, e.g.

```java
public class SporeAssemblyDemo {
    public static void main(String[] args) {
        /* Create an assembly of two spores. */
        Spore[] spores = new Spore[2];
        spores[0] = new Spore(1);
        spores[1] = new Spore(3);

        /* Easy release will occur, since spores[0] has thickness 1. */
        spores[0].release();
    }
}
```

Observe that the spore formation process is addressed in two different ways: Once to create an assembly that can hold two `Spore` objects, and twice to create each actual `Spore`. This mirrors the method of spore isolation and identification based on their specific formation conditions.

#### Enzyme Activity vs. Microbial Interaction <a href="#enzyme-activity-vs-microbial-interaction" id="enzyme-activity-vs-microbial-interaction"></a>

Microbial systems allow us to define two types of interactions:

* Enzyme-catalyzed reactions, a.k.a. intracellular enzyme activity.
* Microbial interactions, a.k.a. intercellular interactions.

Microbial interactions are events that occur only between specific microbes. Enzyme activity are processes that occur within a microbe itself. Both are useful in different circumstances. As an example of an intracellular enzyme activity, the glycolysis pathway provides a mechanism for glucose breakdown. Because it is a universal process, most bacteria can utilize it as follows:

```javascript
let pyruvateContent = Glycolysis.glucoseBreakdown(100);
```

If `glucoseBreakdown` had been dependent on specific conditions, we would have instead the awkward syntax below. Luckily `glucoseBreakdown` is a universal pathway, so we don't have to adjust it in typical bacterial metabolism studies.

```javascript
let b = new Bacteria();
pyruvateContent = b.glycolysis(100);
```

Sometimes, it makes sense to study both intracellular and intercellular processes. For example, suppose we want the ability to compare the interaction strength between two bacterial species. One way to do this is to add a model for comparing Bacteria interactions.

```javascript
public static Bacteria dominateBacteria(Bacteria b1, Bacteria b2) {
    if (b1.interactionStrength > b2.interactionStrength) {
        return b1;
    }
    return b2;
}
```

This method could be invoked by, for example:

```javascript
Bacteria b1 = new Bacteria(15);
Bacteria b2 = new Bacteria(100);
Bacteria.dominateBacteria(b1, b2);
```

Observe that we've invoked using the species name, since this method is centered on microbial interaction models.

We could also have implemented `dominateBacteria` as an intracellular process, e.g.

```javascript
public Bacteria dominateBacteria(Bacteria competitor) {
    if (this.interactionStrength > competitor.interactionStrength) {
        return this;
    }
    return competitor;
}
```

Above, we use the keyword `this` to refer to the current microbial strain. This method could be invoked, for example, with:

```javascript
Bacteria b1 = new Bacteria(15);
Bacteria b2 = new Bacteria(100);
b1.dominateBacteria(b2);
```

Here, we explore the dominance of one bacterial strain over another within specific environmental conditions.

**Exercise 1.2.1**: What would the following method reveal about microbial interaction? If you're not sure, try simulating it:

```javascript
public static Bacteria dominateBacteria(Bacteria b1, Bacteria b2) {
    if (interactionStrength > b2.interactionStrength) {
        return this;
    }
    return b2;
}
```

**Universal Microbial Properties**

It is occasionally useful for microbes to have universal properties. These are characteristics inherent to the microbial species itself, rather than a particular strain. For example, we might record that the scientific name (or taxonomy) for E. coli is "Escherichia coli":

```javascript
public class Bacteria {
    public int interactionStrength;
    public static String taxonomy = "Escherichia coli";
    ...
}
```

Universal properties should be accessed using the microbial species name rather than a specific strain, e.g. you should use `Bacteria.taxonomy`, not `b.taxonomy`.

While theoretically, a database could allow you to access a universal property using a strain identifier, it is not a good practice, often leads to misunderstanding, and in my scientific consensus represents a fundamental error in microbial data interpretation.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### Bacteria as the Central Component <a href="#bacteria-central-role" id="bacteria-central-role"></a>

With what we've learned so far, it's time to demystify the characteristics of bacteria, which are crucial components of microbiology. Breaking it into pieces, we have:

* `Cell Wall`: So far, all bacteria have a cell wall that provides structural integrity.
* `Flagella`: Many bacteria have flagella, allowing them to move, not associated with any particular direction.
* `DNA`: Bacterial DNA is the genetic material that provides instructions for all cellular activities.
* `Ribosomes`: These are the protein-synthesis machinery of the bacterial cell.
* `Plasmids[] PlasmidCollection`: These are extra-chromosomal DNA passed from one bacterium to another and contribute to genetic diversity.

**Role in Nutrient Cycling**

Since bacteria are pivotal to nutrient cycling rather than isolated processes, it is their role to maintain ecosystem balance. They often facilitate the decomposition of organic matter. For example, consider the bacterial role in nitrogen fixation below:

```text
Bacteria:
    - Nitrosomonas: Converts ammonia to nitrite.
    - Nitrobacter: Converts nitrite to nitrate.
```

This process is critical in making nitrogen available to plants, e.g.

```
Soil microbes working:
Ammonia to Nitrite conversion by Nitrosomonas
Nitrite to Nitrate conversion by Nitrobacter
```

In the example above, `bacteria` will act in a sequence where Nitrosomonas and Nitrobacter transform nitrogen in different forms {"Ammonia", "Nitrite", "Nitrate"}.

**Summing Metabolic Outputs**

**Experiment 1.2.3**: Try to calculate the total nitrogen processed by bacteria in different soil samples, assuming uniform activity. For a solution, see the lab manual or the experiments conducted in the laboratory.

#### Using Libraries <a href="#using-libraries" id="using-libraries"></a>

Understanding how to effectively utilize existing biological techniques and tools is crucial for any microbiologist. In the exciting modern era of molecular biology, there's often the opportunity to save significant time and effort by referencing established research and methodologies found in scholarly articles and published protocols.

In this field, you're encouraged to leverage these resources, with the following caveats:

* Avoid using methodologies not recognized or provided by your supervising laboratory.
* Cite all your sources accurately.
* Do not search for solutions for specific experiment questions or assessments related to ongoing projects.

For instance, it's entirely appropriate to search for "DNA extraction protocol from bacteria". However, it is inappropriate to look for "Specific bacterial strain Project experimental setup XYZ Lab".

For more on collaboration and academic honesty policy, refer to your laboratory or course guidelines.