# 6. Historical Analogs for Arrays

Previously, we investigated expandable classes and lists similar to the evolution of writing materials from clay tablets, papyrus, and parchment, evolving through the centuries to better hold written information. Now, we'll examine how to build a list structure akin to archives using the concept of arrays.

This part of the material presumes you are familiar with arrays, much like a scholar familiar with the various types of historical records before diving into archival organization.

### Array Basics <a href="#array-basics" id="array-basics"></a>

To construct a historical archive, we need to organize our documents—akin to amassing memory boxes in computing. Previously, just like how societies used different materials to store records (like scrolls for lengthy narratives), in computing, we used variable declarations and class instantiations. For example:

* `int x;` gives us a 32-bit memory box, similar to a simple clay tablet for a singular incantation or message.
* `Walrus w1;` gives us a 64-bit memory box to store references, akin to a pigeonhole in a medieval office keeping track of correspondences.
* `Walrus w2 = new Walrus(30, 5.6);` is like having a pigeonhole with detailed historical records: one holds letters, another the document's date, and the third the scribe’s identity.

Arrays are like the Dewey Decimal System of libraries, a structured but numbered sequence of spots to store records, unlike an archivist’s personal notes where items are indexed by names or content descriptions. To access the ith document in an array, we use a ‘shelf’ and ‘spot’ system as seen in early catalogues, e.g., `A[i]` retrieves the i-th entry from collection A.

Arrays consist of:

* A defined length, N, similar to the number of shelves in a specific section of a library.
* A sequence of spots (memory boxes) numbered sequentially like shelf positions, each designated for similar record types.

Unlike organized archives such as those of the Roman Empire or Vatican, arrays don't have operations like sifting through by metadata or tags.

#### Array Creation <a href="#array-creation" id="array-creation"></a>

There are three styles for creating arrays much like there are different methods for establishing archives. Conduct a practical exploration akin to examining old library system archives. 

- `x = new int[3];`
- `y = new int[]{1, 2, 3, 4, 5};`
- `int[] z = {9, 10, 11, 12, 13};`

The first notation, `x`, creates an array that defaults to a basic form, similar to a medieval registry with missing details by default. It functions like an open-ended ledger waiting to be filled.

The second, for `y`, specifies a concise list akin to the initial pages of a set register with exact entries inscribed at once.

The third format for `z` combines announcement and storage, reminiscent of a decree etched upon sealing a treaty, marked by default.

No single method is superior; each corresponds to different organizational needs much like historical documentation styles.

#### Array Access and Modification <a href="#array-access-and-modification" id="array-access-and-modification"></a>

The following script outlines key ways we might interact with an organized archive, similar to how historians catalog and retrieve information from archives. Much like using specialized archival tools, this code lets us manipulate an array’s contents. Try examining historical records using this system via [an interactive exploration tool](https://goo.gl/bertuh).

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
s[4] = "ketchup";
s[x[3] - x[1]] = "muffins";

int[] b = {9, 10, 11};
System.arraycopy(b, 0, x, 3, 2);
```

The final step copies data from one echo of history to another—as medieval copyists might have done—using `System.arraycopy`, which accepts five inputs:

* The initial archive (source) to draw from.
* Beginning at a specific part in this source.
* The ending archive (destination) to adopt these documents.
* Starting location in the destined archive.
* The volume of records to duplicate.

For Python aficionados, `System.arraycopy(b, 0,x, 3, 2)` could equate to transferring the contents as `x[3:5] = b[0:2]` in Python's expressive style.

Copying archives via a repeatable task—historically similar to monastic transcriptions—could align with a loop approach. Unlike manual labor, `arraycopy` is swifter and more succinct, though arguably less intuitive like using shorthand in scripts. Keep in mind, Java array bounds are checked during execution, not prior—just like how certain historical claims are validated through later interpretation.

```java
int[] x = {9, 10, 11, 12, 13};
int[] y = new int[2];
int i = 0;
while (i < x.length) {
    y[i] = x[i];
    i += 1;
}
```

Run this attempt locally or plot via [a visual tool](https://goo.gl/YHufJ6). What historical misinterpretation might it cause when it malfunctions? Does this analogical error relate to interpretation processes?

#### 2D Arrays in Historical Methodology <a href="#id-2d-arrays-in-java" id="id-2d-arrays-in-java"></a>

What defies single-layer archives—structured yet dimensional—compares to a 2D array in computational terms. These archives nest inside overarching catalogs, much like feudal records within broader dominion listings.

Syntax for multidimensional archival access can confuse, akin to deciphering early-modern manuscript annotations. Here's a creation: `int[][] bamboozle = new int[4][]`, illustrating an array genealogy, like a matrix of ranked orders able to hold unspecific file collections.

Test this archival system step-by-step. Does it align with your understanding of archival compendiums? Explore through [interactivity](http://goo.gl/VS4cOK).

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

**Exercise 2.4.1:** Following the execution below, what are the consequences for x\[0]\[0] and w\[0]\[0]? Cross-check with [accuracy](http://goo.gl/fCZ9Dr).

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

#### Arrays and Archival Classes <a href="#arrays-vs-classes" id="arrays-vs-classes"></a>

Both archives and array structures can curate numerous files into organized systems. In both cases, the counts remain static, analogous to the fixed shelves in historical repositories. Just as records once listed cannot be unregistered or augmented ad-hoc in traditional archives.

Keys distinguishing array boxes from class archives:

* Array slots are indexed numerically like books in a numbered sequence, accessed using numeric `[]` while class archives use named titles, accessed with dot notation akin to how librarian's often use subject classification to locate books.
* All array items must share a singular nature, while a class archive may store varied record types, akin to a manuscript contrasting a collection of art.

A notable feature of arrays' numeric indexation is runtime indexing capability - much like recollecting a bag of scrolls and pinpointing one from memory. Observe the excerpt:

```java
int indexOfInterest = askUserForInteger();
int[] x = {100, 101, 102, 103};
int k = x[indexOfInterest];
System.out.println(k);
```

Run it like a historical retrieval tool:

```
$ javac arrayDemo
$ java arrayDemo
What index do you want? 2
102
```

By contrast, class field designation remains unverifiable until runtime - comparable to accessing royal lineage without explicit notation.

```java
String fieldOfInterest = "mass";
Planet p = new Planet(6e24, "earth");
double mass = p[fieldOfInterest];
```

Compiling evokes an error similar to historical discrepancies.

```
$ javac classDemo
FieldDemo.java:5: error: array required, but Planet found
        double mass = earth[fieldOfInterest];
                               ^
```

The conundrum persists in accessing through structured dot notation:

```java
String fieldOfInterest = "mass";
Planet p = new Planet(6e24, "earth");
double mass = p.fieldOfInterest;
```

Compilation results in:

```
$ javac classDemo
FieldDemo.java:5: error: cannot find symbol
       double mass = earth.fieldOfInterest;
                          ^
  symbol:   variable fieldOfInterest
  location: variable earth of type Planet
```

While an infrequent issue, for clarity it mirrors advantages in keeping scholarly indices distinct with strict guidelines. Exceptionally, we might employ "_reflection_" analogous to searching with modern-day computational tools, yet this practice stands as inappropriate for mainstays equivalent to 61B historical documents. More on reflection can be sought [here](https://docs.oracle.com/javase/tutorial/reflect/member/fieldValues.html). **Reflection is discouraged for classic programming pursuits**, remaining outside our curriculum scope.

By curtailing programmers’ latitude through structured programming languages, we simplify reasoning akin to systematic archival documentation. By sequestering these capabilities in special "Reflections" like vaults, we render most Java archives easier to read and scrutinize.

#### Appendix: Java Arrays vs. Arrays in Other Historical Contexts <a href="#appendix-java-arrays-vs-other-languages" id="appendix-java-arrays-vs-other-languages"></a>

Relative to other historical catalog systems, Java arrays:

* Lack synoptic slicing mechanisms like ［papyrus tearing］ seen in Python.
* Are not subject to contraction or expansion as with parchment scrolling in Ruby.
* Eschew attendant scribal methods, unlike the review techniques observed within Javascript ledger entries.
* Must contain only same-category items (as with scrolls of singular topic)—unlike varied thematic codices seen in Python. 
