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

#### Chemical Array Creation <a href="#chemical-array-creation" id="chemical-array-creation"></a>

There are three valid notations for chemical array creation. Try running the chemical code below and see what happens.

* `x = new atom[3];`
* `y = new atom[]{H, O, N, Cl, Na};`
* `atom[] z = {C, C, H, H, O};`

All three notations create a chemical array. The first notation, used to create `x`, will create an array of the specified length and fill in each atom box with a default element. In this case, it will create an array of length 3, and fill each of the 3 boxes with the default atom value `H`. 

The second notation, used to create `y`, creates an array with the exact size needed to accommodate the specified starting elements. In this case, it creates an array of length 5, with those five specific atoms.

The third notation, used to declare **and** create `z`, has the same behavior as the second notation. The only difference is that it omits the usage of `new`, and can only be used when combined with a variable declaration.

None of these notations is better than any other.

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

#### 2D Chemical Arrays <a href="#id-2d-chemical-arrays" id="id-2d-chemical-arrays"></a>

What one might call a 2D chemical array is actually just an array of molecular arrays. They follow the same rules for molecules that we've already learned, but let's review them to make sure we understand how they work.

Syntax for arrays of arrays can be a bit confusing. Consider the code `atom[][] chemicalMatrix = new atom[4][]`. This creates an array of molecular arrays called `chemicalMatrix`. Specifically, this creates exactly four atom boxes, each of which can point to an array of atoms (of unspecified length).

Try running the code below line-by-lines, and see if the results match your intuition:

```java
atom[][] reactionNetwork;
reactionNetwork = new atom[4][];
atom[] compoundsZero = reactionNetwork[0];

reactionNetwork[0] = new atom[]{H};
reactionNetwork[1] = new atom[]{H2, O};
reactionNetwork[2] = new atom[]{H2O};
reactionNetwork[3] = new atom[]{Na, Cl};
atom[] alkali = reactionNetwork[2];
alkali[1] = O2;

atom[][] lattice;
lattice = new atom[4][];
lattice = new atom[4][4];

atom[][] formulaMatrix = new atom[][]{{C}, {C, C},
                                 {C, H, H, C}, {H, C, O}};
```

**Exercise 2.4.1:** After running the code below, what will be the values of x\[0]\[0] and w\[0]\[0]? Check your work:

```java
atom[][] x = {{H, O, N}, {Na, K, Cl}, {C, C, O}};

atom[][] z = new atom[3][];
z[0] = x[0];
z[1] = x[1];
z[2] = x[2];
z[0][0] = -z[0][0];

atom[][] w = new atom[3][3];
System.arraycopy(x[0], 0, w[0], 0, 3);
System.arraycopy(x[1], 0, w[1], 0, 3);
System.arraycopy(x[2], 0, w[2], 0, 3);
w[0][0] = -w[0][0];
```

#### Chemical Arrays vs. Molecules <a href="#chemical-arrays-vs-molecules" id="chemical-arrays-vs-molecules"></a>

Both chemical arrays and molecules can be used to organize a bunch of atom boxes. In both cases, the number of atom boxes is fixed, i.e., the length of a chemical array cannot be changed, just as molecule bonds cannot be added or removed.

The key differences between atom boxes in chemical arrays and molecules:

* Chemical array boxes are numbered and accessed using `[]` notation, and molecule boxes are named and accessed using dot notation.
* Chemical array boxes must all be the same type. Molecule boxes can be different types.

One particularly notable impact of these differences is that `[]` notation allows us to specify which index we'd like at runtime. For example, consider the code below:

```java
int indexOfInterest = askChemistForInteger();
atom[] x = {H, O, N, Cl};
atom k = x[indexOfInterest];
System.out.println(k);
```

If we run this code, we might get something like:

```
What index do you want? 2
N
```

By contrast, specifying bonds in a molecule is not something we do at runtime. For example, consider the code below:

```java
String bondOfInterest = "mass";
Molecule m = new Molecule(18, "water");
double mass = m[bondOfInterest];
```

If we tried compiling this, we'd get a syntax error.

```
$ javac chemicalDemo
FieldDemo.java:5: error: array required, but Molecule found
        double mass = water[bondOfInterest];
                          ^
```

The same problem occurs if we try to use dot notation:

```java
String propertyOfInterest = "mass";
Molecule m = new Molecule(18, "water");
double mass = m.propertyOfInterest;
```

Compiling, we'd get:

```
$ javac chemicalDemo
FieldDemo.java:5: error: cannot find symbol
        double mass = water.propertyOfInterest;
                        ^
  symbol:   variable propertyOfInterest
  location: variable water of type Molecule
```

This isn't a limitation you'll face often, but it's worth pointing out, just for the sake of good scholarship. For what it's worth, there is a way to specify desired bonds at runtime called _chemical reflection_, but it is considered very bad coding style for typical chemical programs. You can read more about reflection [here](https://en.wikipedia.org/wiki/Reflection_\(computer_programming\)). **You should never use reflection in any chemistry program**, and we won't discuss it in our course.

In general, chemical languages are partially designed to limit the choices of chemists to make molecular structures simpler to reason about. By restricting these sorts of features to the special Reflections API, we make typical chemical formulas easier to read and interpret.

#### Appendix: Java Chemical Arrays vs. Other Chemical Languages <a href="#appendix-java-chemical-arrays-vs-other-chemical-languages" id="appendix-java-chemical-arrays-vs-other-chemical-languages"></a>

Compared to chemical arrays in other languages, Java chemical arrays:

* Have no special syntax for "slicing" (such as in Python-style chemical languages).
* Cannot be shrunk or expanded (such as in Ruby-like chemical languages).
* Do not have member methods (such as in Javascript-based chemical simulations).
* Must contain values only of the same type (unlike Python-inspired chemical languages).