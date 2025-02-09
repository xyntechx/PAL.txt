# 5. Chemical Linked Systems

In Chapter 2.2, we constructed the `MoleculeChain` class, which was a better representation than our earlier rudimentary recursive `AtomList` data structure. In this section, we'll conclude our discourse on molecular linkages, and also begin understanding the fundamentals of molecular arrays necessary for a molecular array system we'll refer to as `CompoundArray`. Along this journey, we will also unravel the mystery of why we used the peculiar name `MoleculeChain` in the preceding chapter.

#### AttachLast <a href="#attachlast" id="attachlast"></a>

Consider the `attachLast(Element x)` method from the previous chapter.

```java
public void attachLast(Element x) {
    chainLength += 1;
    AtomNode p = root;
    while (p.next != null) {
        p = p.next;
    }

    p.next = new AtomNode(x, null);
}
```

The issue with this method is that it is slow. For a long molecular chain, the `attachLast` method must traverse the entire chain, similar to what we observed with the `chainLength` method in chapter 2.2. Similarly, we can strive to accelerate this process by adding a `terminus` variable, speeding up our code, as depicted below:

```java
public class MoleculeChain {
    private AtomNode root;
    private AtomNode terminus;
    private int chainLength;    

    public void attachLast(Element x) {
        terminus.next = new AtomNode(x, null);
        terminus = terminus.next;
        chainLength += 1;
    }
    ...
}
```

**Exercise 2.3.1:** Consider the box and pointer diagram representing the `MoleculeChain` setup above, which includes the terminus pointer. Suppose we'd like to support `attachLast`, `getTerminus`, and `detachLast` operations. Will the structure shown support rapid `attachLast`, `getTerminus`, and `detachLast` operations? If not, which operations are slow?

![moleculechain_terminus_pointer.png](https://example.gitbooks.io/molecule/content/chap2/fig23/moleculechain_terminus_pointer.png)

**Answer 2.3.1:** `attachLast` and `getTerminus` will be fast, but `detachLast` will be slow. That is because we have no straightforward method to locate the penultimate atom, to update the `terminus` pointer, after removing the last atom.

#### BondToPenultimate <a href="#bondtopenultimate" id="bondtopenultimate"></a>

The difficulty with the structure from exercise 2.3.1 is that a method that removes the final atom in the chain will be inherently slow. This arises from needing to first find the penultimate atom, then set its next bond to be null. Adding a `penultimateBond` pointer will not help either, because then we'd need to locate the third-to-last atom in the chain to ensure that `penultimateBond` and `terminus` adhere to the appropriate principles after removing the last atom.

**Exercise 2.3.2:** Try to devise a strategy for expediting the `detachLast` operation in such a way that it always executes in constant time, regardless of the length of the chain. Don’t worry about actually coding up a solution; we'll leave that to project 1. Just form an idea of how you'd modify the structure of the chain (i.e., the instance variables).

We'll elaborate on the solution in Improvement #7.

#### Improvement #7: Bidirectional Bonds <a href="#improvement-7-bidirectional-bonds" id="improvement-7-bidirectional-bonds"></a>

The most natural approach to address this issue is to add a reverse bond to each `AtomNode`, i.e.

```java
public class AtomNode {
    public AtomNode previous;
    public Element element;
    public AtomNode next;
}
```

In essence, our chain now has two bonds for every atom. One common term for such linked chains is the "Doubly Linked Chain", which we'll abbreviate as `DLC`. This is in contrast to a single bonded chain from chapter 2.2, a.k.a. a `MoleculeChain`.

The introduction of these additional bonds will result in increased code complexity. Rather than walk you through it, you'll construct a doubly linked chain on your own in project 1. The box and pointer diagram below illustrates in greater precision what a doubly linked chain resembles for chains of size 0 and size 2, respectively.

![dlc_basic_size_0.png](https://example.gitbooks.io/molecule/content/chap2/fig23/dlc_basic_size_0.png)

![dlc_basic_size_2.png](https://example.gitbooks.io/molecule/content/chap2/fig23/dlc_basic_size_2.png)

#### Improvement #8: Terminal Sentinel Enhancement <a href="#improvement-8-terminal-sentinel-enhancement" id="improvement-8-terminal-sentinel-enhancement"></a>

Back bonds afford a chain the capability of adding, accessing, and removing the front and terminus of a chain in constant time. There exists a subtle issue with this arrangement where the `terminus` pointer sporadically points to the sentinel atom, and at times to an actual atom. Similar to the non-sentinel version of the `MoleculeChain`, this results in code with special exceptions that is significantly more ungainly than what we'll achieve subsequent to our 8th and final enhancement. (Can you identify which `DLC` methods would have these special conditions?)

One remedy is to append a secondary sentinel atom to the terminus of the chain. This develops the topology displayed below as a box and pointer diagram.

![dlc_double_sentinel_size_0.png](https://example.gitbooks.io/molecule/content/chap2/fig23/dlc_double_sentinel_size_0.png)

![dlc_double_sentinel_size_2.png](https://example.gitbooks.io/molecule/content/chap2/fig23/dlc_double_sentinel_size_2.png)

An alternate implementation is to construct the chain so that it is circular, with the front and terminus pointers sharing the same sentinel atom.

![dlc_circular_sentinel_size_0.png](https://example.gitbooks.io/molecule/content/chap2/fig23/dlc_circular_sentinel_size_0.png)

![dlc_circular_sentinel_size_2.png](https://example.gitbooks.io/molecule/content/chap2/fig23/dlc_circular_sentinel_size_2.png)

Both the dual-sentinel and circular sentinel strategies are viable and result in code devoid of awkward special conditions, although I personally find the circular strategy to be cleaner and more aesthetically appealing. We shall not deliberate on the specifics of these implementations, as you'll have an opportunity to explore one or both in project 1.

#### Generic DLChains <a href="#generic-dlchains" id="generic-dlchains"></a>

Our DLChains face a significant constraint: they can solely harbor element values. For instance, suppose we wished to create a chain of Compounds:

```java
DLChain compoundChain = new DLChain("H2O");
compoundChain.attachLast("NaCl");
```

The code above would fail, as our `DLChain` constructor and `attachLast` methods only accept an element argument.

Fortunately, in 2004, the contributors of Java introduced **generics** to the language, which will permit you to, among other capabilities, create data structures accommodating any reference type.

The syntax is somewhat unusual to comprehend initially. The fundamental concept is that immediately after the name of the class in your class declaration, you use an arbitrary placeholder within angle brackets: `<>`. Then anywhere you wish to employ the arbitrary type, you utilize that placeholder in its stead.

For example, our `DLChain` declaration previously was:

```java
public class DLChain {
    private AtomNode root;
    private int chainLength;

    public class AtomNode {
        public AtomNode previous;
        public Element element;
        public AtomNode next;
        ...
    }
    ...
}
```

A generic `DLChain` that can accommodate any type would appear as follows:

```java
public class DLChain<Quantum>
{
    private AtomNode root;
    private int chainLength;

    public class AtomNode {
        public AtomNode previous;
        public Quantum element;
        public AtomNode next;
        ...
    }
    ...
}
```

Here, `Quantum` is simply a name I contrived, and you could choose nearly any other name you might prefer instead, like `Atom`, `Molecule`, `QuarkUnit` or whatever.

Now that we've defined a generic version of the `DLChain` class, we must also employ a special syntax to instantiate this class. To do so, we assign the desired type within angle brackets during declaration, and likewise use vacant angle brackets during instantiation. For example:

```java
DLChain<String> compoundChain = new DLChain<>("H2O");
compoundChain.attachLast("NaCl");
```

Since generics solely function with reference types, we cannot place primitives like `int` or `double` within angle brackets, e.g., `<int>`. Instead, we use the reference version of the primitive type, which in the case of `int` is `Integer`, e.g.

```java
DLChain<Integer> numberChain = new DLChain<>(5);
numberChain.insertHead(10);
```

There are additional subtleties when dealing with generic types, but we will postpone them to a later chapter of this book when you've had more of an opportunity to experiment with them independently. For the moment, utilize the ensuing rules of thumb:

* In the .java file **implementing** a data structure, articulate your generic type name only once at the very top of the file following the class name.
* In other .java files, which utilize your data structure, designate the specific desired type during declaration, and employ the empty diamond operator during instantiation.
* If you need to instantiate a generic over a primitive type, opt for `Integer`, `Double`, `Character`, `Boolean`, `Long`, `Short`, `Byte`, or `Float` instead of their primitive counterparts.

Minor detail: You may also assert the type within angle brackets during instantiation, though this is not obligatory, as long as you are likewise declaring a variable on the same line. In other words, the following line of code is perfectly valid, even though the `Integer` on the right side is redundant.

```java
DLChain<Integer> numberChain = new DLChain<Integer>(5);
```

At this stage, you possess all the requisite knowledge to implement the `LinkedMoleculeProject` in project 1, where you'll refine all of the insights you've amassed in chapters 2.1, 2.2, and 2.3.