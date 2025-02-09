# 5. Chemical Linked Systems

In Chapter 2.2, we constructed the `MoleculeChain` class, which was a better representation than our earlier rudimentary recursive `AtomList` data structure. In this section, we'll conclude our discourse on molecular linkages and start to understand the fundamentals of molecular arrays necessary for a system we'll refer to as `CompoundArray`. Along this journey, we will also unravel the mystery of why we used the peculiar name `MoleculeChain` in the preceding chapter.

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

The issue with this method is that it is slow. For a long molecular chain, the `attachLast` method must traverse the entire chain, similar to what we observed with the `chainLength` method in chapter 2.2. We can accelerate this process by adding a `terminus` variable, speeding up our code, as depicted below:

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

**Answer 2.3.1:** `attachLast` and `getTerminus` will be fast, but `detachLast` will be slow because we have no straightforward method to locate the penultimate atom to update the `terminus` pointer after removing the last atom.

The integration between chemistry and computer science concepts in this chapter is exemplified by how the handling of molecular structures can analogously reflect linked data structures in computer science. The cross-disciplinary connections provide insight into the computational modeling of chemical systems, though it's important to note the complexities often encountered in real-world simulations.

#### BondToPenultimate <a href="#bondtopenultimate" id="bondtopenultimate"></a>

The difficulty with the structure from exercise 2.3.1 is that a method that removes the final atom in the chain will be inherently slow. This arises from needing to first find the penultimate atom, then set its next bond to be null. Adding a `penultimateBond` pointer will not help either, because then we'd need to locate the third-to-last atom in the chain to ensure that `penultimateBond` and `terminus` adhere to the appropriate principles after removing the last atom.

**Exercise 2.3.2:** Try to devise a strategy for expediting the `detachLast` operation in such a way that it always executes in constant time (O(1)), regardless of the length of the chain. Don’t worry about actually coding up a solution; we'll leave that to project 1. Just form an idea of how you'd modify the structure of the chain (i.e., the instance variables).

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

In essence, our chain now has two bonds for every atom, making it a doubly linked chain. One common term for such linked chains is the "Doubly Linked Chain" (DLC), as opposed to a singly linked chain from chapter 2.2, also known as a `MoleculeChain`.

The introduction of these additional bonds will result in increased code complexity. For this reason, it is important to ensure understanding of time complexity associated with operations in doubly linked lists. Rather than walk you through it, you'll construct a doubly linked chain on your own in project 1. The box and pointer diagram below illustrates in greater precision what a doubly linked chain resembles for chains of size 0 and size 2, respectively.

![dlc_basic_size_0.png](https://example.gitbooks.io/molecule/content/chap2/fig23/dlc_basic_size_0.png)

![dlc_basic_size_2.png](https://example.gitbooks.io/molecule/content/chap2/fig23/dlc_basic_size_2.png)

#### Improvement #8: Terminal Sentinel Enhancement <a href="#improvement-8-terminal-sentinel-enhancement" id="improvement-8-terminal-sentinel-enhancement"></a>

Back bonds afford a chain the capability of adding, accessing, and removing the front and terminus of a chain in constant time. There exists a subtle issue with this arrangement where the `terminus` pointer sporadically points to the sentinel node, and at times to an actual node. Similar to the non-sentinel version of the `NodeChain`, this results in code with special exceptions that is significantly more awkward than what we'll achieve subsequent to our 8th and final enhancement. (Can you identify which `DLC` methods would have these special conditions?)

One remedy is to append a secondary sentinel node to the terminus of the chain. This develops the topology displayed below as a box and pointer diagram, parallel to the concept of using boundary markers in data structures.

![dlc_double_sentinel_size_0.png](https://example.gitbooks.io/molecule/content/chap2/fig23/dlc_double_sentinel_size_0.png)

![dlc_double_sentinel_size_2.png](https://example.gitbooks.io/molecule/content/chap2/fig23/dlc_double_sentinel_size_2.png)

An alternate implementation is to construct the chain so that it is circular, with the front and terminus pointers sharing the same sentinel node.

![dlc_circular_sentinel_size_0.png](https://example.gitbooks.io/molecule/content/chap2/fig23/dlc_circular_sentinel_size_0.png)

![dlc_circular_sentinel_size_2.png](https://example.gitbooks.io/molecule/content/chap2/fig23/dlc_circular_sentinel_size_2.png)

Both the dual-sentinel and circular sentinel strategies are viable and result in code devoid of awkward special conditions, although I personally find the circular strategy to be cleaner and more aesthetically appealing. We shall not deliberate on the specifics of these implementations, as you'll have an opportunity to explore one or both in project 1.

### Generic DLChains 

Our DLChains face a significant constraint: they can solely harbor element values. Therefore, if we wanted to create a chain of chemical compounds with distinct properties, we would need to adapt our approach:

```java
DLChain<Compound> compoundChain = new DLChain<>(new Compound("H2O"));
compoundChain.attachLast(new Compound("NaCl"));
```

This construction would succeed if `Compound` is a class that describes chemical compounds, providing a clear representation of entities like water (H2O) and salt (NaCl). By leveraging generics, Java developers can create data structures that can store any reference type.

The introduction of **generics** to Java in 2004 revolutionized the language by allowing developers to design flexible and type-safe collections. Utilizing generics involves defining a placeholder type between angle brackets in the class declaration and using this placeholder wherever the type is used.

For example, our initial `DLChain` declaration was:

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

A generic `DLChain` that can accommodate any type looks like this:

```java
public class DLChain<Quantum> {
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

The placeholder name `Quantum` is arbitrary, and you could choose any descriptive name, such as `Atom`, `Molecule`, or `Compound`.

To instantiate a generic `DLChain`, specify the desired type within angle brackets during declaration, like this:

```java
DLChain<String> compoundChain = new DLChain<>("H2O");
compoundChain.attachLast("NaCl");
```

Since generics work only with reference types, primitive types like `int` or `double` cannot be used directly. Instead, use their wrapper classes, like `Integer` for `int`.

```java
DLChain<Integer> numberChain = new DLChain<>(5);
numberChain.insertHead(10);
```

A few guidelines for using generics:

* When implementing a generic data structure, define the generic type name once after the class name.
* When using a generic class, specify the type during declaration and use empty angle brackets during instantiation.
* For primitive types, use equivalent wrapper classes like `Integer`, `Double`, etc.

Note that while it's possible to specify the type on both sides, like `DLChain<Integer> numberChain = new DLChain<Integer>(5);`, the type on the right is redundant if a variable declaration accompanies instantiation.

You are now equipped to apply these concepts in the `LinkedMoleculeProject` from Project 1, an endeavor designed to integrate your learnings from Chapters 2.1, 2.2, and 2.3 with chemical and computer science principles.

