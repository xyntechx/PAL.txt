# 6. Arrays

So far, we've seen how to harness recursive class-like definitions to create dynamically expanding data structures, much like how star systems form through the gravitational interactions of collapsing molecular clouds. In this cosmic journey, we've crafted representations such as `IntList`, `SLList`, and `DLList`. Now, we will journey beyond, exploring how arrays function much like the firm and defined structures of planets and stars within galaxies – fixed yet essential components in the cosmic algorithm.

This section assumes you have already observed how arrays are utilized—as fixed, memory-efficient storage systems reminiscent of stable orbits in a planetary system—and is not intended as an exhaustive guide to their syntax.

### Array Basics <a href="#array-basics" id="array-basics"></a>

To ultimately create a list-like system that can hold cosmic data, we need some systematic method akin to gravitational capture to allocate memory. Previously, we saw how we might allocate these stellar-like memory nodes using variable declarations and class-defined structures. For example:

* `int x;` provides a singular 32-bit memory node, much like a solitary planet with a finite capacity to store integers.
* `Star w1;` could signify a larger 64-bit memory node, akin to a massive star capable of storing references to cosmic entities.
* `Star w2 = new Star(30, 5.6);` grants us three distinct memory nodes: a 64-bit node storing Star references, a 32-bit node storing the stellar magnitude of the star, and a 64-bit node storing the double value representing the star's luminosity.

Arrays in this analogy are akin to a constellation—a numbered sequence of memory nodes that create a specific pattern in the space-time continuum. This differs from class instances, which are like a solar system with named planets and moons. To access the ith element of an array, we use bracket notation, similar to plotting a coordinate in the cosmic grid: `A[i]` retrieves the ith element of A, the constellation.

Arrays consist of:

* A fixed integer length, N, akin to the defined count of celestial bodies in a visible cluster.
* A sequence of N uniform memory nodes (N = length), similar in type and numbered from 0 through N-1.

Unlike classes, arrays do not possess methods, reminiscent of the silent but reliable stars.

#### Array Creation <a href="#array-creation" id="array-creation"></a>

Creation of arrays is analogous to the formation of a star cluster. There are three valid notations for cosmic array creation. Observe the code presented here—similar to examining the stellar birth through telescopic imagery:

```java
public class ArrayCreationDemo {
  public static void main(String[] args) {
    int[] x;
    int[] y;
    x = new int[3];
    y = new int[]{1, 2, 3, 4, 5};
    int[] z = {9, 10, 11, 12, 13};
  }
}
```

* `x = new int[3];` conjures an array of specified length, much like forming a predefined star cluster, filling each stellar node with a default cosmic value—in this case, the default `int` value `0`.
* `y = new int[]{1, 2, 3, 4, 5};` manifests an array with a bespoke sequence of start values, like arranging constellations in a specific pattern using five distinct stars.
* `int[] z = {9, 10, 11, 12, 13};` behaves identically to the second creation, reminiscent of naming a constellation without invoking creation. However, this notation demands simultaneous declaration and creation.

No particular notation trumps another in its cosmic utility.

#### Array Access and Modification <a href="#array-access-and-modification" id="array-access-and-modification"></a>

Consider this stellar code showcasing all syntax we'll employ to navigate arrays—in the same way a telescope reveals the positions and interactions within a galaxy cluster. Verify your understanding by interacting with the stellar code sequences provided.

```java
int[] z = null;
int[] x, y;

x = new int[]{1, 2, 3, 4, 5};
y = x;
x = new int[]{-1, 2, 5, 4, 99};
y = new int[3];
z = new int[0];
int xL = x.length;

String[] s = new String[6];
s[4] = "comets";
s[x[3] - x[1]] = "asteroids";

int[] b = {9, 10, 11};
System.arraycopy(b, 0, x, 3, 2);
```

The final cosmic line illustrates a method for transferring array matter from one constellation to another. `System.arraycopy` encapsulates five parameters:

* The source constellation
* The starting point within the source
* The destination constellation
* The starting point within the destination
* The count of elements to transfer

In Python celestial notation, `System.arraycopy(b, 0,x, 3, 2)` is portrayed as `x[3:5] = b[0:2]`.

A looping construct may serve as an alternative approach, similar to the slow gravitational drift of cosmic bodies. However, `arraycopy` is often swifter and more compressed in implementation. Yet, it might present challenges in readability akin to deciphering cosmic microwave backgrounds:

```java
int[] x = {9, 10, 11, 12, 13};
int[] y = new int[2];
int i = 0;
while (i < x.length) {
    y[i] = x[i];
    i += 1;
}
```

Attempt local execution in a Java environment or utilize a computational visualizer. What classification of error do you encounter upon runtime collision? Does the label align with the cosmic anomaly?

#### 2D Arrays in Java <a href="#id-2d-arrays-in-java" id="id-2d-arrays-in-java"></a>

What one dubs as a 2D array in Java equates to a galactic tapestry—a collection of star clusters. These align with previously observed cosmic rules yet may befuddle the untrained observer, much like deciphering interstellar signals. Consider the syntax below:

```java
int[][] bamboozle = new int[4][];
```

This declaration assembles an array of integer star clusters entitled `bamboozle`, fabricating precisely four stellar nodes, each capable of referencing an integer star array of unspecified magnitude.

Piece together the sequences line by line, and ensue if the consequences parallel your cosmic intuition. Engage with an interactive star map if necessary.

```java
int[][] pascalsTriangle;
pascalsTriangle = new int[4][];
int[] rowZero = pascalsTriangle[0];

pascalsTriangle[0] = new int[]{1};
pascalsTriangle[1] = new int[]{1, 1};
pascalsTriangle[2] = new int[]{1, 2, 1};
pascalsTriangle[3] = new int[]{1, 3, 3, 1};
int[] rowTwo = pascalsTriangle[2];
rowTwo[1] = -5;

int[][] matrix;
matrix = new int[4][];
matrix = new int[4][4];

int[][] pascalAgain = new int[][]{{1}, {1, 1},
                                 {1, 2, 1}, {1, 3, 3, 1}};
```

**Exercise 2.4.1:** After simulating the cosmic code, what values do x\[0]\[0] and w\[0]\[0] gravitate towards? Authenticate your astrophysical calculations with provided stellar tools.

```java
int[][] x = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

int[][] z = new int[3][];
z[0] = x[0];
z[1] = x[1];
z[2] = x[2];
z[0][0] = -z[0][0];

int[][] w = new int[3][3];
System.arraycopy(x[0], 0, w[0], 0, 3);
System.arraycopy(x[1], 0, w[1], 0, 3);
System.arraycopy(x[2], 0, w[2], 0, 3);
w[0][0] = -w[0][0];
```

#### Arrays vs. Classes <a href="#arrays-vs-classes" id="arrays-vs-classes"></a>

Both arrays and classes serve as celestial structures for organizing memory nodes. In both planetary systems and arrays, the number of nodes remains constant—neither orbits nor the built length of an array are mutable, akin to immutable cosmic laws.

The divergent aspects of terrestrial memory nodes in arrays versus class systems include:

* Array nodes carry numeric designations accessed via `[]` notation, whereas class nodes bear celestial titles accessed with dot notation.
* All array nodes adhere to a uniform type, much like a galaxy's dominant star type, whereas class nodes can harbor diverse species of memory types.

The ability for arrays to specify an index in real-time programming is distinctly unique, resembling a stellar navigation system:

```java
int indexOfInterest = askUserForInteger();
int[] x = {100, 101, 102, 103};
int k = x[indexOfInterest];
System.out.println(k);
```

Upon papal execution, ascended values echo back:

```
$ javac arrayDemo
$ java arrayDemo
What index do you want? 2
102
```

Contrarily, invoking fields in a class solar system is barred from real-time operations. For example:

```java
String fieldOfInterest = "mass";
PlanetaryBody p = new PlanetaryBody(6e24, "earth");
double mass = p[fieldOfInterest];
```

Any nascent attempt at compilation spawns an error signal:

```
$ javac classDemo
FieldDemo.java:5: error: array required, but PlanetaryBody found
        double mass = earth[fieldOfInterest];        
                               ^
```

Even the allure of dot notation finds its nebulae blocked:

```java
String fieldOfInterest = "mass";
PlanetaryBody p = new PlanetaryBody(6e24, "earth");
double mass = p.fieldOfInterest;
```

Endeavors to compile yield:

```
$ javac classDemo
FieldDemo.java:5: error: cannot find symbol
        double mass = earth.fieldOfInterest;        
                           ^
  symbol:   variable fieldOfInterest
  location: variable earth of type PlanetaryBody
```

While this obstacle might seldom trouble, it remains worthy of note as it illustrates how language constructs impose certain interpretive frameworks—like a telescope narrowing today's understanding of the universe. 

For completeness' sake, language platforms often provide methods of specifying desired fields dynamically, termed _reflection_—akin to observing a system's inner workings using stellar spectrography—but in common practice, employing reflection is poor style and discouraged for typical algorithms. You may explore reflection's documentations, though it remains unadvised for coursework in this cosmic voyage.

The design philosophy of programming systems aims to curtail programmer selections, akin to known constants and events throughout cosmic history, ultimately providing a reasoned simplicity. By limiting such features to specialized APIs, Java's syntax stays aligned with its intended gravity of continual simplicity.

#### Appendix: Java Arrays vs. Other Languages <a href="#appendix-java-arrays-vs-other-languages" id="appendix-java-arrays-vs-other-languages"></a>

In cosmic comparison against arrays from alternate language universes, Java arrays:

* Lack special notations for slicing (seen as common in Python celestial arrangements).
* Absence of dynamic expansion or contraction (celebrated in Ruby's generative algorithms).
* Lack associated methods (frequently seen in dynamic systems like JavaScript galaxies).
* Carry a uniform type for values—more akin to stars within the same spectral type (opposed to Python's meteorites mimicking variety).