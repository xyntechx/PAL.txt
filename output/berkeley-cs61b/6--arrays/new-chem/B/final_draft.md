# 6. Arrays and Molecular Structures

In the previous sections, we've explored recursive class definitions to create various list classes, such as `IntList`, `SLList`, and `DLList`. In this chapter, we will discuss how to build list classes using arrays in contexts where they can metaphorically represent molecular structures. Note that this analogy serves to illustrate computational concepts and should not be confused with real-world chemical operations.

### Array Basics

To construct a list capable of holding molecular-like structures, we employ an array in a manner somewhat analogous to storing atoms or molecules. It's essential to understand that the following references are metaphorical and do not adhere to formal chemical processes.

* `int hydrogen;` can be thought of metaphorically as a simple storage node that holds an integer value instead of a "hydrogen atom."
* `Molecule h2o;` demonstrates a conceptual "container" for a compound, akin to a simple object in programming with attributes.
* `Molecule nh3 = new Molecule(1, 3);` in pseudo-code gives us a container with predefined values that don't directly map to chemical realism.

Arrays, in this context, offer:

* A fixed integer length, N.
* A sequence of N storage slots (or elements) that are homogeneous in type, indexed from 0 through N - 1.

It's important to clarify that arrays in computer science do not perform any chemical operations like reactions or synthesis. Methods or operations on arrays should not be equated to chemical processes.

### Illustrative Example in Pseudo-Code

When handling array operations, it’s helpful to illustrate using pseudo-code:

- Consider `int[] atomArray = new int[3];` as a metaphor for a simple storage initialization, not as a chemical component.
- `System.arraycopy(source, 0, destination, index, length);` is an example of copying elements within an array; this operation emphasizes data handling rather than any chemical transformation.

### Error Handling and Clarification

For students applying programming rather than chemistry, runtime errors like Java's `ArrayIndexOutOfBoundsException` signify the bounded nature of arrays in computational terms. These programming concepts should not be equated with chemical properties or behaviors.

By maintaining distinct boundaries between computer science concepts and chemistry, this chapter aims to provide clearer context and understanding for students, ensuring they separate metaphorical teachings from real-world principles.

#### Array Creation in Pseudo-code <a href="#array-creation-in-pseudo-code" id="array-creation-in-pseudo-code"></a>

There are three valid notations for illustrating array creation conceptually. The code snippets below are pseudo-code meant to demonstrate these concepts and are not executable in real programming languages.

* `int[] x = new int[3];`
* `int[] y = new int[]{1, 2, 3, 4, 5};`
* `int[] z = {10, 20, 30};`

All three notations create arrays. The first notation, used to create `x`, will create an array of the specified length and fill in each element with a default value (usually zero for integers). In this case, it will create an array of length 3, with each element initialized to 0.

The second notation, used to create `y`, creates an array with the exact size needed to accommodate the specified initial elements. In this case, it is an array of length 5, initialized with those specific values.

The third notation, used to declare **and** create `z`, behaves similarly to the second notation, but omits the usage of `new`. This notation is handy when declaring and initializing a variable at the same time.

It is important to clarify that these notations are purely illustrative and serve as a metaphorical explanation for array operations in programming contexts. There are no direct analogs between these operations and chemical processes.

#### Array Access and Modification <a href="#array-access-and-modification" id="array-access-and-modification"></a>

The following code showcases key syntax used to work with Java arrays. 

```java
int[] z = null;
int[] x, y;

x = new int[]{1, 2, 3, 4, 5};
y = x;
x = new int[]{6, 7, 8, 9, 10};
y = new int[3];
z = new int[0];
int xL = x.length;

String[] s = new String[6];
s[4] = "acid";
s[x[3] - x[1]] = "base";

int[] b = {100, 200, 300};
System.arraycopy(b, 0, x, 3, 2);
```

The final line demonstrates one way to copy elements from one array to another. `System.arraycopy` takes five parameters:

* The array to use as a source
* Where to start in the source array
* The array to use as a destination
* Where to start in the destination array
* How many items to copy

An alternate approach to copying arrays would be to use a loop. `arraycopy` is usually faster than a loop and results in more compact code. The only downside is that `arraycopy` is (arguably) harder to read. Note that arrays in Java perform bounds checking at runtime. That is, the following code compiles but will cause a runtime error.

```java
int[] x = {1, 2, 3, 4};
int[] y = new int[2];
int i = 0;
while (i < x.length) {
    y[i] = x[i];
    i += 1;
}
```

Try running this code locally. You should encounter an `ArrayIndexOutOfBoundsException`. This indicates that the code is trying to access an index outside the bounds of the array, which doesn't reflect any chemical processes but is vital in understanding programming array safety.

#### 2D Arrays in Chemistry and Programming <a href="#id-2d-chemical-arrays" id="id-2d-chemical-arrays"></a>

The concept of a 2D array in computer science refers to a collection of arrays, where each array is an element that can contain further elements. This structure is often used to manage complex data sets. While we can draw loose analogies to how complex chemical compounds might be structured, it's important to remember that this is a programming concept and not directly applicable to chemical structures.

The syntax for arrays of arrays can be a bit tricky. For example, consider the code `Element[][] chemicalMatrix = new Element[4][];`. This line creates a 2D array called `chemicalMatrix` where each of the four top-level elements can point to an array of elements (of unspecified length).

Run the code below in a supportive programming environment to observe the behavior:

```java
Element[][] reactionNetwork;
reactionNetwork = new Element[4][];
Element[] compoundsZero = reactionNetwork[0];

reactionNetwork[0] = new Element[]{new Element("H")};
reactionNetwork[1] = new Element[]{new Element("H2"), new Element("O")};
reactionNetwork[2] = new Element[]{new Element("H2O")};
reactionNetwork[3] = new Element[]{new Element("Na"), new Element("Cl")};
Element[] alkali = reactionNetwork[2];
alkali[0] = new Element("He"); // Hypothetical change, for illustration purposes

Element[][] matrix;
matrix = new Element[4][];
matrix = new Element[4][4];

Element[][] formulaMatrix = new Element[][]{{new Element("C")}, {new Element("C"), new Element("C")},
                                {new Element("C"), new Element("H"), new Element("H"), new Element("C")}, {new Element("H"), new Element("C"), new Element("O")}};
```

**Exercise 2.4.1:** Predict the outcome of the code snippet and observe the values of `x[0][0]` and `w[0][0]`:

```java
Element[][] x = {{new Element("H"), new Element("O"), new Element("N")}, {new Element("Na"), new Element("K"), new Element("Cl")}, {new Element("C"), new Element("C"), new Element("O")}};

Element[][] z = new Element[3][];
z[0] = x[0];
z[1] = x[1];
z[2] = x[2];
z[0][0] = new Element("He"); // Hypothetical change, for illustration purposes

Element[][] w = new Element[3][3];
System.arraycopy(x[0], 0, w[0], 0, 3);
System.arraycopy(x[1], 0, w[1], 0, 3);
System.arraycopy(x[2], 0, w[2], 0, 3);
w[0][0] = new Element("He"); // Hypothetical change, for illustration purposes
```

To further understand how programming concepts like arrays can be used in simulating complex data structures, recognize that programming manipulations, such as copying arrays, are computational processes distinct from actual chemical interactions, which involve a series of reactions and precise molecular bonding mechanisms. Understanding the differences between computational modeling and real-world chemistry is crucial for proper interdisciplinary education.

#### Arrays vs. Molecules <a href="#arrays-vs-molecules" id="arrays-vs-molecules"></a>

In both computer science and chemistry, structures are used to organize components efficiently. In programming, an 'array' can hold a fixed number of elements, similar to how molecular structures in chemistry have a defined set of atoms.

The key differences in accessing elements or atoms in these structures are:

* Array elements are accessed via an index using `[]` notation, while properties of molecules (like function groups or atom types) are accessed more abstractly, often using naming or dot notation.
* All elements in an array must be of the same type (e.g., all integers), while in a molecule, different atoms may come together to form various types of chemical bonds.

A notable difference is the runtime access flexibility with arrays, which allows for dynamic element selection, demonstrated below in pseudo-code:

```java
int indexOfInterest = askUserForInteger();
element[] x = {H, O, N, Cl};
element k = x[indexOfInterest];
System.out.println(k);
```

If we run this code and reflect on the following theoretical outcome:

```
What index do you want? 2
N
```

By contrast, while programming structures allow dynamic interaction, molecule structures are defined distinctly during synthesis, and their properties are accessed differently. Consider this Java-inspired pseudo-code for a molecule:

```java
String propertyOfInterest = "mass";
Molecule m = new Molecule(18, "water");
double mass = m.getMass();
```

Attempting to access properties like an array may result in a syntax error:

```
$ javac chemicalDemo
FieldDemo.java:5: error: array required, but Molecule found
        double mass = water[bondOfInterest];
                          ^
```

Even using dot notation incorrectly can trigger errors:

```java
String propertyOfInterest = "mass";
Molecule m = new Molecule(18, "water");
double mass = m.propertyOfInterest;
```

This would yield:

```
$ javac chemicalDemo
FieldDemo.java:5: error: cannot find symbol
        double mass = water.propertyOfInterest;
                        ^
  symbol:   variable propertyOfInterest
  location: variable water of type Molecule
```

Such limitations, while they might seem restrictive, are intentional. They aim to help developers and chemists avoid mistakes by adhering to well-defined syntaxes and operations in programming and valid chemical principles. Techniques like reflection can bypass these constraints, but they are considered poor practice in programming and not applicable in fundamental chemistry operations. More information about reflection can be found [here](https://en.wikipedia.org/wiki/Reflection_\(computer_programming\)).

In summary, programming languages and chemical software are designed to maintain clarity and safety, avoiding misleading comparisons between data structures in programming and molecular operations, which involve intricate and diverse chemical processes.

#### Appendix: Arrays in Java vs. Other Programming Languages <a href="#appendix-arrays-in-java-vs-other-programming-languages" id="appendix-arrays-in-java-vs-other-programming-languages"></a>

Compared to arrays in other programming languages, Java arrays:

* Have no special syntax for "slicing" (such as in Python).
* Cannot be shrunk or expanded (as allowed in Ruby).
* Do not have member methods (unlike arrays in JavaScript).
* Must contain values only of the same type (unlike Python's list, which can hold mixed types).

**Code Examples Clarification:**

- It is important to note that any notations or code examples provided, such as `x = new int[3]`, are purely illustrative and meant to help understand a concept, not actual Java syntax for chemical operations.
- For example, in `System.arraycopy(b, 0, x, 3, 2);`, this operation is demonstrated to illustrate copying elements in arrays and should not be conflated with actual chemical processes or operations.

**Error Handling Explanation:**

- When discussing errors such as `ArrayIndexOutOfBoundsException`, it's essential to clarify that this is a programming error in Java, unrelated to any chemistry concepts, ensuring clear understanding that these processes do not have a chemical counterpart.

By incorporating these clarifications and ensuring accuracy in both the computer science context, readers will have clearer learning outcomes without conflating distinct concepts from programming and chemistry.

