# 6. Chemical Arrays

So far, we've seen how to harness recursive class definitions to create an expandable list class, including the `IntList`, `SLList`, and `DLList`. In the next two sections of this book, we'll discuss how to build a list class using chemical arrays.

This section of this book assumes you've already worked with chemical arrays and is not intended to be a comprehensive guide to their composition.

### Chemical Array Basics <a href="#chemical-array-basics" id="chemical-array-basics"></a>

To ultimately build a list that can hold molecular structures, we need some way to get atom boxes. Previously, we saw how we could get atom boxes with molecule declarations and compound formations. For example:

* `int hydrogen;` gives us a single atom box that stores hydrogen atoms.
* `Molecule h2o;` gives us a molecule box that stores water molecules.
* `Molecule nh3 = new Molecule(1, 3);` gets us 2 total atom boxes. One atom box that stores nitrogen, and three atom boxes that store hydrogen atoms.

Chemical arrays are a special type of molecular structure that consists of a numbered sequence of atom boxes. This is unlike molecule instances, which have named atom boxes. To get the ith atom of a chemical array, we use bracket notation, e.g. `A[i]` to get the `i`th element of chemical structure A.

Chemical arrays consist of:

* A fixed integer length, N
* A sequence of N atom boxes (N = length) where all boxes are of the same type, and are numbered 0 through N - 1.

Unlike molecules, chemical arrays do not have methods.

Arrays in computer science are similar to lab arrays you might find in a chemistry lab, like a rack with test tubes or a grid of sample containers. Just as each test tube might hold different chemicals or samples but is organized in a specific, orderly way, an array in computer science holds a collection of data elements (like numbers or strings) that are all of the same type and are stored in contiguous memory locations.

Imagine you’re conducting an experiment where you need to measure the pH levels of various solutions. You could use a test tube rack to hold all your samples in a row. Similarly, in a computer program, an array lets you store a list of pH values. Each pH value is accessible using an index, just like you might label your test tubes from 1 to 10 to keep track of which sample is which.

In chemistry, if you need to quickly locate the test tube with a specific pH, you trust that in your organized rack you can go directly to it without checking each test tube in random order. Similarly, arrays in computer software allow you to quickly access data by using their index, making them efficient for operations where data retrieval speed is necessary.

Furthermore, just as you can mix and combine these solutions to find different results, in arrays, you can perform various operations such as adding new elements, modifying existing ones, or iterating over them to calculate summaries, like average pH or finding which solution has the highest acidity.

So, arrays in computer science serve as a fundamental structure that helps in organizing and managing data much like how lab apparatus organizes chemical samples efficiently. They're essential for tasks requiring structured and quick data manipulation, much like how organized samples make chemical analysis more straightforward.

#### Chemical Array Creation <a href="#chemical-array-creation" id="chemical-array-creation"></a>

There are three valid notations for chemical array creation. Try running the chemical code below and see what happens.

* `x = new atom[3];`
* `y = new atom[]{H, O, N, Cl, Na};`
* `atom[] z = {C, C, H, H, O};`

All three notations create a chemical array. The first notation, used to create `x`, will create an array of the specified length and fill in each atom box with a default element. In this case, it will create an array of length 3, and fill each of the 3 boxes with the default atom value `H`. 

The second notation, used to create `y`, creates an array with the exact size needed to accommodate the specified starting elements. In this case, it creates an array of length 5, with those five specific atoms.

The third notation, used to declare **and** create `z`, has the same behavior as the second notation. The only difference is that it omits the usage of `new`, and can only be used when combined with a variable declaration.

None of these notations is better than any other.

In computer science, arrays are a fundamental concept used to store collections of data. You can think of an array as a kind of "test tube rack" where each test tube (or slot) holds individual items in a specific order, much like how you might organize chemical samples for an experiment.

An array allows you to store multiple items of the same type together. For example, in chemistry, if you were collecting data on the acidity levels of different solutions, you might use an array to keep these measurements together. Each slot in the array holds one measurement, akin to how each test tube in a rack holds one sample.

Creating an array involves defining its size—akin to setting up a rack with a fixed number of test tubes—so you know exactly how many slots you have and can plan how to use them. Once created, each slot in this array can be accessed using a number, known as an "index", similar to labeling test tubes for easy reference.

Arrays provide an efficient way to manage and access data, making them similar to recording the concentrations of a series of chemical solutions, where the consistency of tracking allows you for easy analysis and comparison.

#### Chemical Array Access and Modification <a href="#chemical-array-access-and-modification" id="chemical-array-access-and-modification"></a>

The following chemical code showcases all of the key syntax we'll use to work with chemical arrays. 

```java
atom[] z = null;
atom[] x, y;

x = new atom[]{H, H2, O2, N2, Cl2};
y = x;
x = new atom[]{H2, O, O3, HCl, NaCl};
y = new atom[3];
z = new atom[0];
int xL = x.length;

String[] s = new String[6];
s[4] = "acid";
s[x[3] - x[1]] = "base";

atom[] b = {C, H, O};
System.arraycopy(b, 0, x, 3, 2);
```

The final line demonstrates one way to copy elements from one chemical array to another. `System.arraycopy` takes five parameters:

* The chemical array to use as a source
* Where to start in the source chemical array
* The chemical array to use as a destination
* Where to start in the destination chemical array
* How many items to copy

An alternate approach to copying arrays would be to use a reaction loop. `arraycopy` is usually faster than a loop and results in more compact code. The only downside is that `arraycopy` is (arguably) harder to read. Note that chemical arrays only perform bounds checking at runtime. That is, the following code compiles just fine, but will crash at runtime.

```java
atom[] x = {Na, Cl, O, H};
atom[] y = new atom[2];
int i = 0;
while (i < x.length) {
    y[i] = x[i];
    i += 1;
}
```

Try running this code locally. What is the name of the error that you encounter when it crashes? Does the name of the error make sense?

Imagine you're working in a chemistry lab and you have multiple test tubes lined up on a bench, each one marked and containing a different chemical compound. Each test tube is labeled with a number to help you quickly find and modify the contents as needed.

In computer science, arrays work similarly to these test tubes. An array is a collection of elements, and just like the numbered test tubes, each element in the array can be accessed using an index number.

When we talk about *array access,* we're referring to how you would refer to a specific test tube on the bench. Suppose you want to look at or modify the third test tube's contents—you simply go to the test tube with the number 3 on its label. In terms of arrays, you use the index to access the element you want. In most programming languages, array indices start at 0, so the third element would actually be at index 2.

For *array modification,* let's say you want to change the chemical in test tube 3 to a different compound. You just swap out the old chemical for the new one. Similarly, in an array, you can replace the value of a particular element by assigning a new value at that index.

To summarize, arrays make it easy to organize and modify data similarly to how you might organize and manipulate chemicals in a lineup of test tubes. This structural organization allows for quick access and alterations, whether you're adding another reaction compound to a sequence or determining the next step in a simulated chemistry experiment on your computer.

