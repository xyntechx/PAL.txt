# 3. Applications of Computer Science in Biology

### Data Structures and Algorithms in Biological Research <a href="#data-structures-and-algorithms-in-biological-research" id="data-structures-and-algorithms-in-biological-research"></a>

In Project 0, we use arrays to track genetic sequences consisting of nucleotides. As our biological data grows, we encounter new challenges that aren’t efficiently solved with fixed-size arrays. For instance, representing dynamic biological models, such as cellular structures or protein interactions, often requires data structures that can grow or shrink as needed.

An alternate approach would have been to use a list type. In Python, list data structures provide flexibility:

```python
nucleotide_sequence = ['A', 'T', 'G']
nucleotide_sequence.append('C')
```

While Java and other programming languages offer built-in List types, in this chapter, we'll explore how building our own list from the ground up can deepen our understanding of data structures and their applications in biology.

#### The Case of Genetic Data Reuse <a href="#the-case-of-genetic-data-reuse" id="the-case-of-genetic-data-reuse"></a>

Consider the following Java code where genetic data is reused across various variables. Predict what happens to `a` if changes are made through `b`. This reflects scenarios in bioinformatics where reference handling of genetic data impacts memory and performance:

```java
GeneSequence a = new GeneSequence("ATGC");
GeneSequence b;
b = a;
b.geneticCode = "GCAT";
System.out.println(a);
System.out.println(b);
```

Now observe how primitive types behave differently in this scenario, similar to simple numerical data manipulations in phenotypic assays:

```java
int x = 5;
int y;
y = x;
x = 2;
System.out.println("x is: " + x);
System.out.println("y is: " + y);
```

#### Binary Representation of Biological Data <a href="#binary-representation-of-biological-data" id="binary-representation-of-biological-data"></a>

All biological information processed computationally is ultimately represented in a binary format. For example:

* Nucleotide 'A' might be encoded as 01000001
* A floating-point representation of temperature in a biological process might be encoded similarly to decimal numbers.

While we won’t delve into the specifics of why certain biological measurements are stored as particular sequences of bits, these concepts stem from fundamental computing courses and are vital for bioinformatics.

It is crucial for bioinformatics programs to correctly interpret these binary encodings to accurately process biological data types such as genetic sequences or protein structures.

#### Variables and Biological Data Types <a href="#variables-and-biological-data-types" id="variables-and-biological-data-types"></a>

In computational biology, defining variables for different biological data types (e.g., nucleotide sequences, protein structures) requires understanding how these variables are allocated in memory.

For instance, a variable to store the length of a gene sequence could be declared and utilized as follows:

```java
int geneLength;
double mutationRate;
```

Java allocates blocks suitable for the data type specified, which is critical when dealing with large datasets typical in bioinformatics.

#### GenePacking Application – Arrays and Lists <a href="#genepacking-application-arrays-and-lists" id="genepacking-application-arrays-and-lists"></a>

Understanding memory allocation helps when developing applications like GenePacking, where large quantities of genetic data are managed dynamically.

Depending on needs, lists allow dynamic alterations, such as adding or removing mutations, unlike arrays that require predefined sizes. This flexibility is crucial for tasks such as simulating evolutionary processes or structural bioinformatics where the size of the data set can change dynamically.

To illustrate:

```java
List<String> mutations = new LinkedList<>();
mutations.add("Insertion");
mutations.add("Deletion");
```

Such a mechanism allows managing significant genetic changes efficiently.

#### Biological Data Handling – Reference Types <a href="#biological-data-handling-reference-types" id="biological-data-handling-reference-types"></a>

Managing biological data using reference types ensures that changes made in one dataset can be reflected across copies, facilitating collaborative research environments and databases. For instance, handling datasets of SNPs (Single Nucleotide Polymorphisms) efficiently using such reference models speeds up bioinformatics analyses.

#### Building Biological Data Structures: BioLinkedList <a href="#building-biological-data-structures-biolinkedlist" id="building-biological-data-structures-biolinkedlist"></a>

In building BioLinkedList data structures, useful for storing sequences or genetic markers, we mirror nature's adaptability. We incrementally construct this, learning from standard linked lists whilst tailoring to biological contexts:

```java
public class BioLinkedList {
    public String geneticMarker;
    public BioLinkedList nextMarker;

    public BioLinkedList(String marker, BioLinkedList next) {
        geneticMarker = marker;
        nextMarker = next;
    }
}
```

This allows for efficient insertion and traversal of genetic markers in bioinformatics applications.

In summary, adopting and adapting traditional CS concepts such as lists and references in the context of biology can offer powerful tools for handling the complexities of genetic and bioinformatics data efficiently.