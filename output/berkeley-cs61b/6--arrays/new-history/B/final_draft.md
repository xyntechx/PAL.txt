# 6. Historical Analogs for Arrays

Previously, we investigated dynamic data structures and lists similar to the evolution of writing materials from clay tablets, papyrus, and parchment, evolving through the centuries to better hold written information. Now, we'll examine how to build a list structure akin to archives using the concept of arrays.

This part of the material presumes you are familiar with arrays, much like a scholar familiar with the various types of historical records before diving into archival organization.

### Array Basics <a href="#array-basics" id="array-basics"></a>

To construct a historical archive, we need to organize our documents—akin to amassing memory boxes in computing. Previously, just like how societies used different materials to store records (like scrolls for lengthy narratives), in computing, we used variable declarations and class instantiations. For example:

* `int x;` gives us a 32-bit memory box, similar to a basic arithmetic log on a clay tablet recording singular calculations.
* `Walrus w1;` gives us a reference to a memory location, akin to having an index in a ledger specifying where more detailed information can be found, much like a compartment in a library catalogue.
* `Walrus w2 = new Walrus(30, 5.6);` creates an object with attributes, similar to creating an organized file that holds multiple details—like a document detailing an event with specifics about dates and participants.

Arrays are like the Dewey Decimal System of libraries, providing a structured, numbered sequence of spots to store records, unlike an archivist’s personal notes where items are indexed by names or content descriptions. This system resembles structured catalogs, where call numbers represent locations on physical or metaphorical shelves. To access the ith document in an array, we use the idea of a ‘shelf’ and ‘spot’ system as seen in early catalog countries, e.g., `A[i]` retrieves the i-th entry from collection A.

Arrays consist of:

* A defined length, N, similar to the number of shelves in a specific section of a library.
* A sequence of spots (memory boxes) numbered sequentially—each designated for similar record types, just like how tally stones might have been used for counting identical items.

Unlike organized archives such as those of the Roman Empire or Vatican, arrays store elements of the same data type, meaning each scroll or document would contain the same kinds of records.

Historically, zero-based counting systems exist, much like how arrays are zero-indexed. This approach can be traced to early counting methods, where initial positions corresponded to 'zero' rather than 'one.'

Exploring operations such as `System.arraycopy`, an analogy might be direct transcription methods where information was verified and then copied for precision, akin to ensuring accurate record duplication. 

The constraints like array bounds mirror historical limitations encountered when interpreting records without pre-checks—resulting in errors if not carefully managed, much like surpassing the edges of a filled counting board.

When using `arraycopy`, the verification ensures that data can be accurately duplicated, much like how historical records were copied after authentication, ensuring fidelity to the original document.

Through these structured analogies, we maintain accuracy without oversimplification, paralleling the evolution of record-keeping with modern computing techniques to highlight how these principles transcend their origins to guide present-day practices.

#### Array Creation <a href="#array-creation" id="array-creation"></a>

There are three styles for creating arrays much like there are different methods for establishing archives in history, each with its own peculiarities and uses.

- `x = new int[3];`
- `y = new int[]{1, 2, 3, 4, 5};`
- `int[] z = {9, 10, 11, 12, 13};`

The first notation, `x`, creates an array that defaults to a specific size, initialized with default values, similar to a medieval registry where entries are predetermined but yet to be filled—akin to the initial setup of a system like the Dewey Decimal System, which organizes but leaves room for data entry.

The second, for `y`, specifies elements directly, akin to the completion of a concise record from the start, much like an exact transcription into a structured archive where each entry is inscribed upon creation.

The third format for `z` declares and initializes simultaneously, reminiscent of a written decree that immediately effects changes in a record system, akin to a finalized treaty etched and sealed.

These methods align with different organizational needs, reflecting how historical documentation evolved. Arrays necessitate elements of the same data type, paralleling how certain archives categorize data homogeneously. Arrays start at zero-index based, tracing back to historical zero-based systems such as early numeric recordings found in Sumerian accounting.

In discussing the manipulation of arrays, "System.arraycopy" functions akin to historical methods for data transcription, ensuring precise transfer as verified records were handled, stressing the crucial maintenance of order and accuracy—core both to early archival systems and modern programming.

Array bounds, like historical bureaucratic protocols, must be observed to prevent errors. Just as records needed verification, arrays require careful boundary checks to avoid overstepping and causing computational errors, underscoring the balance between structure and flexibility in both fields.

#### Dynamic Data Structures: Array Access and Modification <a href="#array-access-and-modification" id="array-access-and-modification"></a>

In this section, we explore fundamental ways we may interact with organized digital libraries, akin to how historians catalog and retrieve information using structured databases. This code allows us to manipulate an array’s contents, much like historians would handle historical logs or indices. Engage with these concepts via [an interactive exploration tool](https://goo.gl/bertuh).

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

Just as medieval scribes copied texts from one script to another, `System.arraycopy` accomplishes this transfer digitally, accepting five parameters:

* The original archive (source) to use.
* Starting index in this source.
* The destination archive (target).
* Initial index in this target.
* The quantity of records to copy.

For those who prefer Python, `System.arraycopy(b, 0, x, 3, 2)` resembles directly assigning elements as `x[3:5] = b[0:2]` in Python’s syntax.

This transference, much like historical copyists, can also be performed repetitively using loops. While historically slower and more manual, automated methods like `arraycopy` enhance speed and clarity, though requiring understanding of Java’s runtime checks akin to historical scrutiny of record interpretation.

```java
int[] x = {9, 10, 11, 12, 13};
int[] y = new int[2];
int i = 0;
while (i < x.length) {
    y[i] = x[i];
    i += 1;
}
```

Try running this example locally or through [a visual tool](https://goo.gl/YHufJ6). Consider the potential for historical misinterpretation if it malfunctions. Does this analogical error parallel the process of historical errors being uncovered through analysis?

#### 2D Arrays in Historical Methodology <a href="#id-2d-arrays-in-java" id="id-2d-arrays-in-java"></a>

What defies single-layer archives—structured yet dimensional—compares to a 2D array in computational terms. These archives nest inside overarching catalogs, much like feudal records organized through a system such as the Dewey Decimal System within broader dominion listings.

Syntax for multidimensional archival access can confuse, akin to deciphering early-modern manuscript annotations. Here's a creation: `int[][] bamboozle = new int[4][]`, illustrating an array genealogy, like a matrix of ranked orders able to hold unspecific file collections. This array can be likened to an organized file with multiple details, where the object constructs a structured approach to storage.

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

Arrays are zero-indexed, a concept reminiscent of early historical zero-based counting systems. To better understand how arrays function, such as in the way they store elements of the same data type much like registries that maintain uniform records, understanding these foundational principles is key.

The `System.arraycopy` method can be directly compared to historical methods of replicating records only after validation, ensuring that the data copied is accurate, similar to the verification required before copying historical records.

The error constraints, akin to limitations on interpreting historical records without predefined checks, illustrate how going beyond array bounds without pre-checks can cause issues, similar to breaking the understood systems of documentation in record-keeping history.

#### Arrays and Archival Classes <a href="#arrays-vs-classes" id="arrays-vs-classes"></a>

Both dynamic data structures and array structures can curate numerous files into organized systems. In both cases, the counts remain static, analogous to the fixed shelves in historical repositories. Just as records once listed cannot be unregistered or augmented ad-hoc in traditional archives.

Keys distinguishing array boxes from class archives:

* Array slots are indexed numerically like books in a numbered sequence, accessed using numeric `[]`, while class archives use named titles, accessed with dot notation akin to how librarians often use the Dewey Decimal System to locate books.
* All array items must share a singular data type, unlike scrolls that might contain different records, while a class archive may store varied record types, akin to a manuscript contrasting a collection of art.

A notable feature of arrays' numeric indexation is runtime indexing capability - much like recalling a bag of scrolls and pinpointing one from memory, or using a compartment index in a historical system. Observe the excerpt:

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

While it is an infrequent issue, for clarity, it mirrors advantages in keeping scholarly indices distinct with strict guidelines. Exceptionally, we might employ "_reflection_" analogous to searching with modern-day computational tools, yet this practice stands as inappropriate for mainstays equivalent to 61B historical documents. More on reflection can be sought [here](https://docs.oracle.com/javase/tutorial/reflect/member/fieldValues.html). **Reflection is discouraged for classic programming pursuits**, remaining outside our curriculum scope.

By curtailing programmers’ latitude through structured programming languages, we simplify reasoning akin to systematic archival documentation. By sequestering these capabilities in special "Reflections" like vaults, we render most Java archives easier to read and scrutinize.

### Appendix: Java Arrays vs. Arrays in Historical Contexts

Relative to other historical catalog systems, Java arrays:

* Lack dynamic data structures like the "slicing mechanisms" seen in Python akin to papyrus tearing.
* Are not subject to expansion or contraction as seen in dynamic structures such as Ruby lists resembling parchment scrolling.
* Eschew attendant scribal methods, unlike the review techniques observed within JavaScript ledger entries, which involve handwritten annotations.
* Must contain only same-category items, akin to scrolls with singular topics—unlike varied thematic codices seen in Python that hold diverse records.

The analogy of Java's array to historical systems can be further explored through comparison with the Dewey Decimal System—a structured, orderly system ensuring items categorized similarly are stored together, much like an array's requirement for uniform data types.

Moreover, early compute systems relied on elements like stone tablets, with tally marks representing basic logs or records, akin to primitive arrays storing numbers. This structured record-keeping evolved into more complex structures, mirroring the evolution of arrays over time.

Arrays are inherently constrained by their boundaries, paralleling historical record interpretations that could not exceed physical document limitations. Unlike scrolls that contained both varied information, which allows for more flexibility, arrays strictly constrain such flexibility until pre-checks are completed, avoiding array bounds errors.

Furthermore, Java arrays start at a zero index, a practice which can be traced back to historical zero-based counting systems. This allows more efficient memory access and calculation processes.

Effective data transfer using `System.arraycopy` in Java serves as a more organized replica of historical shorthand methods where data transfer was directly handled only after thorough verification, much like reviewing records before making a copy.

In summary, arrays in Java maintain a level of rigidity and simplicity, akin to historical record-keeping methods, ensuring precision and consistency in data handling.

