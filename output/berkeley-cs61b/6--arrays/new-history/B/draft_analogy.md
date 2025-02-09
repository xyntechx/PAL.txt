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

Imagine a time when early civilizations were developing systems to keep track of their resources. They used various methods, such as counting sticks or tally marks on stone tablets, to record inventories and transactions. As societies grew in complexity, so did the sophistication of their record-keeping. Fast forward to the invention of writing, and you'll find records on clay tablets or papyrus that often stored data in rows and columns, much like tables today.

In modern computer science, we have a concept called "arrays" that serves a somewhat analogous purpose. An array is a data structure that allows us to store a collection of elements, like numbers or words, in an organized manner so that we can easily access and manipulate them. Think of an array like a row of cubbies, where each cubby holds one item, and each is numbered starting from zero. This numbering, or indexing, allows us to quickly find the item we're looking for without having to search through every cubby one by one.

In the way that ancient records might list series of symbols in specific order to provide valuable information, an array provides a structured way of organizing data for a computer program. Whether you're managing inventory in a large database or simply storing a sequence of historical dates for analysis, arrays are a fundamental tool for efficiently handling these sequences of data.

Just as historians rely on well-preserved and organized records to study past societies, computer scientists use arrays to keep their data tidy and accessible, making them indispensable in both fields for creating a coherent and accessible picture of the information at hand.

#### Array Creation <a href="#array-creation" id="array-creation"></a>

There are three styles for creating arrays much like there are different methods for establishing archives. Conduct a practical exploration akin to examining old library system archives. 

- `x = new int[3];`
- `y = new int[]{1, 2, 3, 4, 5};`
- `int[] z = {9, 10, 11, 12, 13};`

The first notation, `x`, creates an array that defaults to a basic form, similar to a medieval registry with missing details by default. It functions like an open-ended ledger waiting to be filled.

The second, for `y`, specifies a concise list akin to the initial pages of a set register with exact entries inscribed at once.

The third format for `z` combines announcement and storage, reminiscent of a decree etched upon sealing a treaty, marked by default.

No single method is superior; each corresponds to different organizational needs much like historical documentation styles.

Imagine you are a historian trying to organize a vast collection of documents from different periods and regions. You have stacks of scrolls, books, and papers spread around a large hall. To make sense of them and to access them easily, you decide to place these documents into a meticulously organized system.

In computer science, an array is much like our systematic organization of historical documents. It is a way to store a collection of items in a structured manner. Arrays hold items in a specific order, allowing you to efficiently access, manage, and manipulate data. 

Picture a long bookshelf in your archive - each slot in this shelf can hold one book. This bookshelf is similar to an array. It has a fixed number of slots, and each slot, resembling an array element, can store one piece of data - like a historical document. The position of each document on the shelf, or index in an array, makes it easy to locate any particular document quickly, just as you can use the index to locate array elements.

Creating an array in a programming sense is like building this bookshelf with a set number of slots. Once created, you can place the documents (or data elements) inside. Each slot, or element of the array, can be labeled with a number (starting with zero, interestingly, indicating how counting often begins in CS similar to how certain historical figures or events might set a starting point for a new era).

Thus, understanding arrays can be akin to understanding how archivists categorize and store collections of historical evidence. A well-maintained array, like a well-organized archive, can be essential for fast retrieval and analysis of information stored within it.

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

Imagine you’re a historian who has been granted access to a medieval library. The books are stored in a structured manner on shelves, with each shelf representing a specific century and each book representing individual events, chronicles, or knowledge recorded in that time period.

This organizational method parallels how arrays work in computer science. An array is a data structure that contains a collection of elements, each identified by an index or key. Just like how you can easily access a specific book on a specific shelf in the library rather than searching randomly through piles of documents, arrays allow you to access any element within it directly if you know its position.

Arrays have been pivotal to programming since the early days of computing, similar to how the development of organized libraries improved the preservation and dissemination of knowledge. In a computing array, each element can be accessed via its index, usually starting from 0. This is akin to knowing that the third book on the second shelf would be easy to locate because you’ve already marked out exactly where to find each piece of information.

Modifying elements in an array is a straightforward task, akin to replacing an old manuscript with a revised edition without needing to rearrange the entire library. You simply substitute the content of a book with an updated version while leaving its position intact.

Just like how certain libraries in history were the cornerstone of knowledge, arrays in computing are foundational structures used to sort, store, and retrieve data efficiently. Understanding their organization helps keep data management efficient, enabling quicker access and modification, which has been essential since the earliest computers just as catalog systems revolutionized access to information in libraries.

