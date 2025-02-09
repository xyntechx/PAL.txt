# 4. MoleculeLists

In Chapter 3, we built the `AtomChain` class, a structure representation that can technically do all the things a chain of atoms can do. However, in practice, the `AtomChain` suffers from the fact that it is fairly awkward to use, resulting in code that is hard to read and maintain.

Fundamentally, the issue is that the `AtomChain` is what I call a **naked recursive** data structure. In order to use an `AtomChain` correctly, the chemist must understand and utilize recursion even for simple chain-related tasks. This limits its usefulness to novice chemists and potentially introduces a whole new class of challenging arrangements that chemists might encounter, depending on what sort of helper methods are provided by the `AtomChain` class.

Inspired by our experience with the `AtomChain`, we'll now build a new class `MoleculeList`, which much more closely resembles the molecule representations that chemists use in modern languages. We'll do so by iteratively adding a sequence of improvements.

## Enhancing Immutability and Encapsulation

When discussing the `AtomNode` and `MoleculeList` classes, it is crucial to highlight the significance of immutability and encapsulation. Immutability helps in maintaining consistency and simplicity, while encapsulation restricts access to an object's components, shielding the logic from unwanted external interference. Making the `AtomNode` an inner static class is advisable unless there's a necessity for it to have a specific association with the outer `MoleculeList` class.

## Addressing Recursive Implementation Pitfalls

The recursive implementation for calculating size can be suboptimal in terms of performance due to its linear time complexity for each traversal. By introducing a cached size variable, we can improve performance significantly, reducing time complexity to constant time where possible. This is a standard approach for optimizing such linked list operations.

## Improving Algorithmic Context

When adding new methods such as `addLast`, it is essential to discuss algorithmic complexity. Best practices in linked list manipulation suggest maintaining tail references and using sentinel nodes to manage edge cases efficiently. A seasoned analogy to help visualize this might compare a sentinel node to a guard molecule that maintains order at the chain's boundary.

By implementing these considerations, our `MoleculeList` will be more robust and accessible, mirroring the iterative, precise modifications that chemists apply to alter molecular properties methodically. Additionally, when discussing access control, we can liken public versus private access to the selective activity at a catalyst's bonding sites, where only the active sites (public) participate in reactions, leaving others inactive (private). Without a doubt, these enhancements will make the `MoleculeList` more intuitive and aligned with chemical principles, solidifying the connection between chemistry and computer science for students.

### Improved Section

#### Improvement #1: Object Redesign <a href="#improvement-1-object-redesign" id="improvement-1-object-redesign"></a>

Our `AtomChain` class was previously defined as follows, with helper methods omitted:

```java
public class AtomChain {
    public String element;
    public AtomChain next;

    public AtomChain(String e, AtomChain n) {
        element = e;
        next = n;
    }
```

For improved design, we'll rename the class to `AtomNode` and re-evaluate our approach to its construction. In chemical terms, think of this as a molecular restructuring where we reinterpret how molecular components interact, like modifying a molecular structure to impact its properties.

```java
public class AtomNode {
    private final String element;
    private AtomNode next;

    public AtomNode(String e, AtomNode n) {
        element = e;
        next = n;
    }
}
```

#### Improvement #2: Modular Fabrication <a href="#improvement-2-modular-fabrication" id="improvement-2-modular-fabrication"></a>

Recognizing that direct interaction with `AtomNode` objects can be cumbersome, we introduce a `MoleculeList` class. This is akin to designing a molecular scaffold for easier manipulation of chemical groups.

```java
public class MoleculeList {
    private AtomNode first;

    public MoleculeList(String e) {
        first = new AtomNode(e, null);
    }

    // Future methods will ensure encapsulation and robust design.
    public void addFirst(String e) {
        first = new AtomNode(e, first);
    }

    public String getFirst() {
        return first != null ? first.element : null;
    }
}
```

Using `MoleculeList`, compare the initialization for a single-element structure:

```java
AtomChain C1 = new AtomChain("H", null);
MoleculeList M2 = new MoleculeList("H");
```

`MoleculeList` abstracts the user's need to handle underlying data factors directly, improving maintainability and safety. This mirrors isolating selective sites in catalysts, where certain chemical actions occur while others remain inaccessible, emphasizing encapsulation.

#### Improving Algorithm Efficiency

When developing methods such as `addLast`, consider the time complexity associated with linked list operations. Discussing algorithmic trade-offs here enhances understanding, much like comparing reaction rates based on molecular pathway selections in chemistry.

By rethinking our class design and implementation details, from public versus private access (like active/unaccessible catalyst sites), we mimic the real-world logic of chemistry and improve the programming integrity of our code.

#### addFirst and getFirst <a href="#addfirst-and-getfirst" id="addfirst-and-getfirst"></a>

`addFirst` is relatively straightforward if you understood chapter 2.1. With `AtomChains`, we added to the front with the line of code `C = new AtomChain("H", C)`. Thus, we end up with:

```java
public class MoleculeList {
    private AtomNode first;

    public MoleculeList(String e) {
        first = new AtomNode(e, null);
    }

    /** Adds an atom to the front of the list. */
    public void addFirst(String e) {
        first = new AtomNode(e, first);
    }
}
```

Note the importance of immutability and encapsulation here: making `first` private enforces a clear structure by preventing external modification, just as chemical bonds structure a stable molecule.

`getFirst` is even easier. We simply return `first.element`:

```java
/** Retrieves the front atom from the list. */
public String getFirst() {
    return first.element;
}
```

The resulting `MoleculeList` class is more user-friendly. Compare:

```java
MoleculeList M = new MoleculeList("O");
M.addFirst("H");
M.addFirst("H");
String e = M.getFirst();
```

to the `AtomChain` equivalent:

```java
AtomChain C = new AtomChain("O", null);
C = new AtomChain("H", C);
C = new AtomChain("H", C);
String e = C.element;
```

Comparing the two data structures visually, we have:

![AtomChain_vs_MoleculeList.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig22/IntList_vs_SLList.png)

Essentially, the `MoleculeList` class acts as an intermediary between the programmer and the `AtomChain`. This mirrors how a catalyst in chemistry provides controlled access to active sites, ensuring proper interaction. In CS, avoiding direct access ensures better encapsulation and reduces error susceptibility.

To recap, refactoring the `AtomNode` into a static inner class may offer advantages by separating its lifecycle from the enclosing class unless specific outer class associations are required.

**Exercise 2.2.1**: The curious reader might suggest that `AtomChain` could be just as user-friendly by implementing an `addFirst` method. Attempting this, you'll discover the method is complex and inefficient, highlighting the trade-offs similar to those in optimizing chemical reactions for desired outcomes.

#### Improvement #3: Public vs. Private <a href="#improvement-3-public-vs-private" id="improvement-3-public-vs-private"></a>

Unfortunately, our `MoleculeList` can be bypassed and the raw power of our naked data structure (with all its dangers) can be accessed. A chemist can easily modify the list directly, without going through the kid-tested, mother-approved `addFirst` method, for example:

```java
MoleculeList M = new MoleculeList("O");
M.addFirst("H");
M.first.next.next = M.first.next;
```

![bad_MoleculeList.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig22/bad_SLList.png)

This results in a malformed list with an infinite loop. To deal with this problem, we can modify the `MoleculeList` class so that the `first` variable is declared with the `private` keyword.

```java
public class MoleculeList {
    private AtomNode first;
    // Add a static keyword to AtomNode for better encapsulation
    private static class AtomNode {
        // AtomNode code here
    }
...
```

Private variables and methods can only be accessed by code inside the same `.java` file, e.g., in this case `MoleculeList.java`. This enhances encapsulation, ensuring internal representations are insulated from external modification. Consequently, a class like `MoleculeTroubleMaker` below will fail to compile, yielding a `first has private access in MoleculeList` error.

```java
public class MoleculeTroubleMaker {
    public static void main(String[] args) {
        MoleculeList M = new MoleculeList("O");
        M.addFirst("H");
        M.first.next.next = M.first.next;
    }
}
```

By contrast, any code inside the `MoleculeList.java` file will be able to access the `first` variable.

It may seem a little silly to restrict access. After all, the only thing that the `private` keyword does is break programs that would otherwise compile. However, in large scientific modeling projects, the `private` keyword serves as a critical mechanism for defining clear interfaces and hiding implementation details. This is similar to how certain bonding sites on a catalyst (active sites) are accessible (public) and others are not (private) in a chemical reaction. Like changing these bonding sites can affect a reaction, modifying public methods can drastically alter how software interacts with these methods.

**When you create a `public` member (i.e., method or variable), be careful, because you're effectively committing to supporting that member's behavior exactly as it is now, forever.** This commitment is crucial for maintaining consistency and reliability in long-term scientific software projects.

#### Improvement #4: Nested Classes <a href="#improvement-4-nested-classes" id="improvement-4-nested-classes"></a>

At the moment, we have two `.java` files: `AtomNode` and `MoleculeList`. However, the `AtomNode` is really just a supporting character in the story of `MoleculeList`.

Java provides us with the ability to embed a class declaration inside of another for just this situation. The syntax is straightforward and intuitive:

```java
public class MoleculeList {
       public class AtomNode {
            public String element;
            public AtomNode next;
            public AtomNode(String e, AtomNode n) {
                element = e;
                next = n;
            }
       }

       private AtomNode first; 

       public MoleculeList(String e) {
           first = new AtomNode(e, null);
       } 
...
```

Having a nested class has no meaningful effect on code performance, and is simply a tool for keeping code organized. For more on nested classes, see [Oracle's official documentation](https://docs.oracle.com/javase/tutorial/java/javaOO/nested.html).

If the nested class has no need to use any of the instance methods or variables of `MoleculeList`, you may declare the nested class `static`, as follows. Declaring a nested class as `static` means that methods inside the static class cannot access any of the members of the enclosing class. In this case, it means that no method in `AtomNode` would be able to access `first`, `addFirst`, or `getFirst`.

```java
public class MoleculeList {
       public static class AtomNode {
            public String element;
            public AtomNode next;
            public AtomNode(String e, AtomNode n) {
                element = e;
                next = n;
            }
       }

       private AtomNode first;
...
```

Using a static nested class in this instance also aligns with best practices for immutability and encapsulation, as `AtomNode` doesn’t need an association with its outer `MoleculeList` class.

This saves a bit of memory, because each `AtomNode` no longer needs to keep track of how to access its enclosing `MoleculeList`.

Put another way, if you examine the code above, you'll see that the `AtomNode` class never uses the `first` variable of `MoleculeList`, nor any of `MoleculeList`'s methods. As a result, we can use the static keyword, which means the `AtomNode` class doesn't get a reference to its boss, saving us a small amount of memory.

If this seems a bit technical and hard to follow, try Exercise 2.2.2. A simple rule of thumb is that _if you don't use any instance members of the outer class, make the nested class static_.

**Exercise 2.2.2** Delete the word `static` as few times as possible so that [this program](https://joshhug.gitbooks.io/hug61b/content/chap2/exercises/Government.java) compiles (Refresh the page after clicking the link and making sure the URL changed). Make sure to read the comments at the top before doing the exercise.

Additionally, the concept of instance members being public or private can be linked to how chemical bonding sites are active or inactive in catalysts, underlining how some elements in programming or chemistry can be more accessible compared to others.

#### addLast() and size() <a href="#addlast-and-size" id="addlast-and-size"></a>

To motivate our remaining improvements and also demonstrate some common patterns in data structure implementation, we'll add `addLast(String e)` and `size()` methods. You're encouraged to take the [starter code](https://github.com/Berkeley-CS61B/lectureCode/blob/master/lists2/DIY/addLastAndSize/SLList.java) and try it yourself before reading on. I especially encourage you to try to write a recursive implementation of `size`, which will yield an interesting challenge.

I'll implement the `addLast` method iteratively, though you could also do it recursively. The idea is fairly straightforward, we create a pointer variable `p` and have it iterate through the list to the end.

```java
/** Adds an atom to the end of the list. */
public void addLast(String e) {
    AtomNode p = first;

    /* Advance p to the end of the list. */
    while (p.next != null) {
        p = p.next;
    }
    p.next = new AtomNode(e, null);
}
```

This operation has a time complexity of O(n) which can be contrasted with structures that maintain a reference to the tail of the list, enabling O(1) complexity for tail insertions.

By contrast, I'll implement `size` recursively. This method will be somewhat similar to the `size` method we implemented in section [2.1](https://joshhug.gitbooks.io/hug61b/content/chap2/chap21.html) for `AtomChain`.

The recursive call for `size` in `AtomChain` was straightforward: `return 1 + this.next.size()`. For a `MoleculeList`, this approach does not make sense. A `MoleculeList` has no `next` variable. Instead, we'll use a common pattern that is used with middleman classes like `MoleculeList` -- we'll create a private helper method that interacts with the underlying data structure.

This yields a method like the following:

```java
/** Returns the size of the list starting at AtomNode p. */
private static int size(AtomNode p) {
    if (p.next == null) {
        return 1;
    }
    return 1 + size(p.next);
}
```

Using this method, we can easily compute the size of the entire list:

```java
public int size() {
    return size(first);
}
```

However, be aware that a recursive implementation can have a higher overhead compared to an iterative solution, and it might be more efficient to maintain a cached size variable for operations involving frequent size retrievals.

Here, we have two methods, both named `size`. This is allowed in Java, since they have different parameters. We say that two methods with the same name but different signatures are **overloaded**. For more on overloaded methods, see Java's [official documentation](https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html).

An alternate approach is to create a non-static helper method in the `AtomNode` class itself, but this might violate encapsulation principles if `AtomNode` does not necessitate an association with `MoleculeList`. Using a static nested class for `AtomNode` can improve modularity, ensuring no unintended side effects or dependencies between the nodes and list.

Finally, consider public vs. private access control in methods. Just as certain chemical reaction sites on a catalyst might be accessible (public) while others are not (private), method access control dictates interaction interfaces, ensuring appropriate encapsulation and modularity within your code.

## Improvement #5: Caching <a href="#improvement-5-caching" id="improvement-5-caching"></a>

Consider the `size` method we wrote above. Suppose `size` takes 2 seconds on a list of size 1,000. We expect that on a list of size 1,000,000, the `size` method will take 2,000 seconds, since the algorithm has to iterate through 1,000 times as many nodes in the list to reach the end. Having a `size` method that is very slow for large lists is unacceptable, since we can do better.

It is possible to rewrite `size` so that it takes constant time, irrespective of how large the list is.

To achieve this, we can maintain a `size` variable within the `MoleculeList` class that tracks the current number of nodes. This optimization technique is an example of **caching**, which involves storing important data to expedite future access.

```java
public class MoleculeList {
    ... /* Inner static AtomNode declaration omitted. */
    private AtomNode first;
    private int size;

    public MoleculeList(String e) {
        first = new AtomNode(e, null);
        size = 1;
    }

    public void addFirst(String e) {
        first = new AtomNode(e, first);
        size += 1;
    }

    public int size() {
        return size;
    }
    ...
}
```

This modification renders our `size` method exceptionally fast irrespective of list length. While it slightly increases the complexity of methods such as `addFirst` and `addLast`, and marginally raises the memory footprint of our class due to the additional `size` variable, the benefits make this trade-off worthwhile. This caching mechanism highlights the importance of balancing time complexity with space complexity in algorithm design.

#### Improvement #6: The Empty List <a href="#improvement-6-the-empty-list" id="improvement-6-the-empty-list"></a>

Our `MoleculeList` has a number of benefits over the simple `AtomChain` from chapter 2.1:

* Users of a `MoleculeList` never see the `AtomChain` class.
  * Simpler to use.
  * More efficient `addFirst` method (exercise 2.2.1).
  * Avoids errors or malfeasance by `AtomChain` users.
* Faster `size` method than possible with `AtomChain`, due to caching the size within the `MoleculeList` structure, preventing the need for recursive size calculations that would lead to increased time complexity.

Another natural advantage is that we will be able to easily implement a constructor that creates an empty list. The most natural way is to set `first` to `null` if the list is empty. This yields the constructor below:

```java
public MoleculeList() {
    first = null;
    size = 0;
}
```

Unfortunately, this causes our `addLast` method to crash if we insert into an empty list. Since `first` is `null`, trying to access `p.next` in `while (p.next != null)` below leads to a null pointer exception.

```java
public void addLast(String e) {
    size += 1;
    if (first == null) {
        first = new AtomNode(e, null);
    } else {
        AtomNode p = first;
        while (p.next != null) {
            p = p.next;
        }
        p.next = new AtomNode(e, null);
    }
}
```

This improved `addLast` method checks if `first` is `null` to appropriately handle the case of inserting into an empty list, thereby preventing a null pointer exception.

**Exercise 2.2.3** Fix the original implementation of the `addLast` method using the improved logic above, ensuring that it correctly handles empty lists without causing errors. Starter code [here](https://github.com/Berkeley-CS61B/lectureCode/blob/master/lists2/DIY/fixAddLast/SLList.java).

Additionally, consider the broader relevance: much like the selective accessibility of bonding sites in a catalyst with active (public) and inactive (private) sites, managing access to data members in a class controls interaction and protects data integrity.

#### Improvement #6b: Sentinel Nodes <a href="#improvement-6b-sentinel-nodes" id="improvement-6b-sentinel-nodes"></a>

One solution to fix `addLast` is to create a special case for the empty list, as shown below:

```java
public void addLast(String e) {
    size += 1;

    if (first == null) {
        first = new AtomNode(e, null);
        return;
    }

    AtomNode p = first;
    while (p.next != null) {
        p = p.next;
    }

    p.next = new AtomNode(e, null);
}
```

This solution works, but special case code like that shown above should be avoided when necessary. Human beings only have so much working memory, and thus we want to keep complexity under control wherever possible. For a simple structure like the `MoleculeList`, the number of special cases is small. More complicated structures like molecular trees can get much, much uglier.

A cleaner, though less obvious solution, is to make it so that all `MoleculeLists` are the "same", even if they are empty. We can do this by creating a special node that is always there, which we will call a **sentinel node**. The sentinel node will hold an element, which we won't care about.

For example, the empty list created by `MoleculeList M = new MoleculeList()` would be as shown below:

![empty_sentinelized_MoleculeList.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig22/empty_sentinelized_SLList.png)

And a `MoleculeList` with the atoms "H", "O", and "H" would look like:

![three_item_sentenlized_MoleculeList.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig22/three_item_sentenlized_SLList.png)

In the figures above, the lavender ?? value indicates that we don't care what value is there. Since Java does not allow us to fill in a string with question marks, we just pick some arbitrary string like "?" or anything else.

Since a `MoleculeList` with a sentinel has no special cases, we can simply delete the special case from our `addLast` method, yielding:

```java
public void addLast(String e) {
    size += 1;
    AtomNode p = sentinel;
    while (p.next != null) {
        p = p.next;
    }

    p.next = new AtomNode(e, null);
}
```

As you can see, this code is much cleaner!

#### Invariants <a href="#invariants" id="invariants"></a>

An invariant is a fact about a data structure that is guaranteed to be true (assuming there are no bugs in your code).

A `MoleculeList` with a sentinel node has at least the following invariants:

* The `sentinel` reference always points to a sentinel node.
* The front atom (if it exists), is always at `sentinel.next.element`.
* The `size` variable is always the total number of atoms that have been added.

Invariants make it easier to reason about code, and also give you specific goals to strive for in making sure your code works.

The concept of a sentinel node is similar to having constant structure in a data system—akin to how certain stable background settings operate in experimental conditions in chemistry.

A true understanding of how convenient sentinels are will require you to really dig in and do some implementation of your own. You'll get plenty of practice in Lab Project 1. However, we recommend that you wait until after you've finished the next section of this book before beginning Lab Project 1.

