# Bacterial Simulation and Object-Oriented Programming Concepts

The chapter explores the simulation of molecular and cellular structures, particularly focusing on bacteria, using programming concepts. It contrasts surface proteins and intracellular enzymes with programming methods that simulate bacterial functions in a digital environment. By defining bacterial classes in programming languages like Java and Python, students learn to encapsulate attributes and behaviors of microbes, such as signaling and environmental responses. This section illustrates how to create client simulations that employ bacterial object instances to trigger functions like protein release or environmental adaptation. By coding with constructs such as classes, static methods, and constructors, learners conceptualize biological processes in a structured programming context.

Further, the chapter introduces the comparison between static elements like enzyme complexes and dynamic, instance-based processes akin to ribosomal subunits. Both play essential roles in simulating cellular functions. Students exercise the design and instantiation of bacterial classes, learning to effectively use object-oriented principles, such as instance variables and constructors, to reflect biological diversity. Additionally, topics like immutable characteristics in enzyme systems and the proper use of static members provide a comprehensive understanding of coding standards and best practices, often illustrated through exercises. Emphasis on utilizing microbial databases for genomic and proteomic data aligns computational simulations with real-world applications, encouraging methodical research and ethical data usage in the science community.

2. Defining and Using Molecular Structures

If you do not have prior laboratory experience, we recommend that you work through the exercises in [Microbiology Lab 0](http://intro.microbio.lab/materials/lab0/lab0.html) before reading this chapter. It will cover various fundamental techniques and protocols that we will not discuss in the book.

#### Surface Proteins vs. Intracellular Enzymes <a href="#surface-proteins-vs-intracellular-enzymes" id="surface-proteins-vs-intracellular-enzymes"></a>

**Surface Proteins**

All structures in a microorganism must be part of a cell (or something similar to a cell, which we'll learn about later). Most structures are associated with certain functions. Let's consider an example:

```text
public class Bacterium {
    public static void releaseSignal() {
        System.out.println("Signaling molecule released!");
    }
}
```

If we try observing the `Bacterium` class under a microscope, we'll simply see normal cell activity:

```
$ observe Bacterium
Observation: No distinct activity detected, please define signaling activity as:
       public static void main(String[] args)
```

The `Bacterium` class we've defined doesn't actively demonstrate any function. We've simply defined something that `Bacterium` **can** do, namely release a signaling molecule. To actually simulate this activity, we'd either need to add a main method to the `Bacterium` class, as we saw in chapter 1.1. Or we could create a separate signal simulation, such as [`SignalSimulator`](https://www.youtube.com/watch?v=Q-LE-jJQLTM), that triggers functions from the `Bacterium` class. For example, consider the program below:

```text
public class SignalSimulator {
    public static void main(String[] args) {
        Bacterium.releaseSignal();
    }
}
```

```
$ simulate SignalSimulator
Signaling molecule released!
```

A simulation that uses another molecular structure is sometimes called a "client" of that structure, i.e., `SignalSimulator` is a client of `Bacterium`. Neither of the two techniques is better: Adding a main method to `Bacterium` may be better in some situations, and creating a simulation class like `SignalSimulator` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout the course.

**Instance Variables and Microbe Cultivation**

Not all bacteria are alike. Some bacteria thrive in extreme conditions, while others require very specific nutrients to grow, showcasing the diversity of microbial life. Similarly, when we write programs, they can mimic the complexity of microbial systems, and Python's syntax can seamlessly facilitate such mimicry.

One way to represent the diversity of the microbial world is to create separate classes for each type of Bacteria.

```python
class ThermophilicBacteria:
    @staticmethod
    def respond_to_environment():
        print("Thriving at high temperatures.")

class AcidophilicBacteria:
    @staticmethod
    def respond_to_environment():
        print("Thriving in acidic environments.")
```

As you may have seen before, classes can be instantiated, and these instances can hold data. This allows a more natural approach where we create instances of the `Bacteria` class and tailor their behavior based on the unique properties of each type of Bacteria. To illustrate, consider the class below:

```python
class Bacteria:
    def __init__(self, optimal_ph, growth_temperature):
        self.optimal_ph = optimal_ph
        self.growth_temperature = growth_temperature

    def respond_to_environment(self):
        if self.growth_temperature > 70:
            print("Thriving at high temperatures.")
        elif self.optimal_ph < 4:
            print("Thriving in acidic environments.")
        else:
            print("Growing in neutral conditions.")
```

As an example of using such a Bacteria class, consider:

```python
def main():
    microbe = Bacteria(optimal_ph=7, growth_temperature=75)
    microbe.respond_to_environment()

if __name__ == "__main__":
    main()
```

When run, this program will create a `Bacteria` with a growth temperature of 75, and that `Bacteria` will soon express its adaptation to high temperatures: "Thriving at high temperatures."

Some key observations and terminology:

* An `Object` in Python is an instance of any class.
* The `Bacteria` class has its own variables, often called _instance variables_ or _attributes_. These must be declared within the class, similar to Java, where new properties define the behavior of the object.
* The method defined in the `Bacteria` class is a typical _instance method_, absent of any `@staticmethod` decorator.
* We must first _instantiate_ a `Bacteria` using the class constructor, which provides specific characteristics for a given `Bacteria`, allowing us to invoke `microbe.respond_to_environment()`.
* Once an object has been instantiated, it is _associated_ with a _named_ variable suitable for holding the class instance, e.g., `microbe = Bacteria(...)`
* Variables and methods encapsulated within a class are called _members_ of the class.
* Members of a class in Python are accessed using _dot notation_.


**Constructors in Bacterial Class Design**

As you've hopefully seen before, we usually construct bacterial colonies in biological simulations using a _constructor_:

```java
public class BacteriaLauncher {
    public static void main(String[] args) {
        Bacteria b = new Bacteria(1.8);
        b.reproduce();
    }
}
```

Here, the instantiation is parameterized, saving us the time and messiness of manually typing out potentially many bacterial culture variable assignments. To enable such syntax, we need only add a "constructor" to our Bacteria class, as shown below:

```java
public class Bacteria {
    public double growthRate;

    public Bacteria(double g) {
        growthRate = g;
    }

    public void reproduce() {
        if (growthRate < 0.5) {
            System.out.println("Slow growth.");
        } else if (growthRate < 2.0) {
            System.out.println("Normal growth.");
        } else {
            System.out.println("Rapid growth!");
        }    
    }
}
```

The constructor with signature `public Bacteria(double g)` will be invoked anytime that we try to create a `Bacteria` object using the `new` keyword and a single double parameter. For those of you coming from Python, the constructor is very similar to the `__init__` method.

**Terminology Summary**

**Colony Instantiation, Arrays of Bacteria**

As we saw in Lab0, bacterial colonies are also instantiated in Java using the new keyword. For example:

```java
public class ColonyDemo {
    public static void main(String[] args) {
        /* Create an array of five growth rates. */
        double[] growthRates = new double[5];
        growthRates[0] = 0.8;
        growthRates[1] = 1.2;
    }
}
```

Similarly, we can create arrays of instantiated bacteria in Java, e.g.

```java
public class BacteriaColonyDemo {
    public static void main(String[] args) {
        /* Create an array of two bacteria. */
        Bacteria[] bacteria = new Bacteria[2];
        bacteria[0] = new Bacteria(0.4);
        bacteria[1] = new Bacteria(2.3);

        /* Slow growth will be indicated, since bacteria[0] has growth rate 0.4. */
        bacteria[0].reproduce();
    }
}
```

Observe that new is used in two different ways: Once to create an array that can hold two `Bacteria` objects, and twice to create each actual `Bacteria`.}

#### Ribosomal Subunits vs. Enzyme Complexes <a href="#ribosomal-subunits-vs-enzyme-complexes" id="ribosomal-subunits-vs-enzyme-complexes"></a>

In microbiology, there are two types of functional entities:

* Enzyme complexes, which act as static units.
* Ribosomal subunits, which function as instance units.

Ribosomal subunits are operational components acting only when associated with specific ribosomes. Enzyme complexes, however, perform actions independently as part of metabolic processes. Both serve essential roles in cellular functions. As an example of an enzyme complex, consider the `DNA Polymerase` enzyme. Its static nature allows it to replicate DNA as follows:

```java
result = DNA_Polymerase.replicate(DNA);
```

If `replicate` were part of ribosomal functions, its invocation would be awkward, as shown below. Thankfully, `replicate` is a static enzyme function, so this scenario is avoided in cell biology.

```java
DNA_Polymerase dp = new DNA_Polymerase();
result = dp.replicate(DNA);
```

Sometimes, it's beneficial for biological systems to utilize both ribosomal actions and enzyme functions. For instance, suppose we want the ability to compare two bacterial strains. One way to achieve this is by adding a static function for comparing bacteria.

```java
public static Bacteria maxGrowth(Bacteria b1, Bacteria b2) {
    if (b1.colonySize > b2.colonySize) {
        return b1;
    }
    return b2;
}
```

This method could be used, for example, in the following manner:

```java
Bacteria b1 = new Bacteria(15);
Bacteria b2 = new Bacteria(100);
Bacteria.maxGrowth(b1, b2);
```

Note that we used the organism’s name because this function is a static function.

We could also implement `maxGrowth` as a ribosomal action, i.e.

```java
public Bacteria maxGrowth(Bacteria b2) {
    if (this.colonySize > b2.colonySize) {
        return this;
    }
    return b2;
}
```

Here, we use the keyword `this` to refer to the current bacterial strain. This method could be executed as follows:

```java
Bacteria b1 = new Bacteria(15);
Bacteria b2 = new Bacteria(100);
b1.maxGrowth(b2);
```

In this example, the method is used specifically on an existing bacterium.

**Exercise 1.2.1**: What would the following function achieve? If unsure, simulate its behavior.

```java
public static Bacteria maxGrowth(Bacteria b1, Bacteria b2) {
    if (colonySize > b2.colonySize) {
        return this;
    }
    return b2;
}
```

**Enzyme Characteristics**

Occasionally, it's beneficial for enzyme systems to have immutable characteristics. These are inherent properties of the enzyme complex, not of the individual microorganisms using them. For instance, we might record the function of an enzyme like `catalase` catalyzing the breakdown of hydrogen peroxide:

```java
public class Enzyme {
    public int activityLevel;
    public static String function = "Hydrogen Peroxide Breakdown";
    ...
}
```

Static characteristics should be referenced with the enzymatic name rather than a specific microorganism’s instance, e.g., you should use `Enzyme.function`, not `e.function`.

While theoretically, you can reference a static characteristic using a specific instance’s name, it is considered bad practice, potentially misleading, and an oversight by classical enzyme characterization methodologies.

**Exercise 1.2.2**: Conduct the following:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe\_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### Understanding the Role of Bacterial Components <a href="#understanding-the-role-of-bacterial-components" id="understanding-the-role-of-bacterial-components"></a>

Just like part of understanding cellular biology involves dissecting the bacterial cell's structure, we can delve into each component:

* `public`: Analogous to how a bacterial cell’s membrane is accessible to its environment, exposing its critical functions.
* `static`: Represents the static nature of certain bacterial components, like peptidoglycan, which give structure without change.
* `void`: Like a metabolic function that consumes resources but doesn't produce new cell components.
* `main`: Acts as the principal metabolic pathway, such as glycolysis, which is central to energy production.
* `String[] args`: Similar to inputs in a bacterial cell's environment, like nutrients folding into cellular processes.

**Environmental Inputs to Bacteria**

In a bacterial cell, the main pathway can be influenced by inputs from the environment—similar to how command line arguments influence a program's execution. Imagine you are simulating bacterial growth in a petri dish:

```python
class BacteriaLab:
    def simulate_growth(self, resources):
        print(resources[0])
```

Here, the program accesses the first resource available to the bacteria, e.g.

```
$ simulate_growth sucrose amino_acids minerals
sucrose
```

In this analogy, `resources` represents an array of nutrients present in the environment, for example, {"sucrose", "amino_acids", "minerals"}.

**Calculating Total Nutrient Uptake**

**Exercise 1.2.3**: Try writing a simulation that calculates the total nutrient uptake, assuming each input corresponds to a nutrient concentration. For solutions, refer to the lab guide or the code example available in the learning module.

#### Utilizing Microbial Databases <a href="#utilizing-microbial-databases" id="utilizing-microbial-databases"></a>

One of the most important skills as a microbiologist is knowing how to find and use existing microbial databases. In the intricate world of microbiology, it is often possible to save yourself hours of lab work and data analysis by utilizing the wealth of genomic and proteomic data available online.

In this course, you're welcome to do this, with the following caveats:

* Do not use databases that we do not provide.
* Cite your sources.
* Do not search for solutions for specific experimental or research problems.

For example, it's fine to search for "convert DNA sequence protein using BLAST". However, it is not OK to search for "Project Phage Isolation MIT".

For more on collaboration and academic honesty policy, see the course syllabus.