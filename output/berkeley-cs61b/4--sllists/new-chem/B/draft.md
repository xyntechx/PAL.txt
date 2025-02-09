# 4. MoleculeLists

In Chapter 3, we built the `AtomChain` class, a structure representation that can technically do all the things a chain of atoms can do. However, in practice, the `AtomChain` suffers from the fact that it is fairly awkward to use, resulting in code that is hard to read and maintain.

Fundamentally, the issue is that the `AtomChain` is what I call a **naked recursive** data structure. In order to use an `AtomChain` correctly, the chemist must understand and utilize recursion even for simple chain-related tasks. This limits its usefulness to novice chemists, and potentially introduces a whole new class of tricky arrangements that chemists might run into, depending on what sort of helper methods are provided by the `AtomChain` class.

Inspired by our experience with the `AtomChain`, we'll now build a new class `MoleculeList`, which much more closely resembles the molecule representations that chemists use in modern languages. We'll do so by iteratively adding a sequence of improvements.

#### Improvement #1: Rebranding <a href="#improvement-1-rebranding" id="improvement-1-rebranding"></a>

Our `AtomChain` class from last time was as follows, with helper methods omitted:

```java
public class AtomChain {
    public String element;
    public AtomChain next;

    public AtomChain(String e, AtomChain n) {
        element = e;
        next = n;
    }
...
```

Our first step will be to simply rename everything and throw away the helper methods. This probably doesn't seem like progress, but trust me, I'm a professional.

```java
public class AtomNode {
    public String element;
    public AtomNode next;

    public AtomNode(String e, AtomNode n) {
        element = e;
        next = n;
    }
}
```

#### Improvement #2: Bureaucracy <a href="#improvement-2-bureaucracy" id="improvement-2-bureaucracy"></a>

Knowing that `AtomNodes` are hard to work with, we're going to create a separate class called `MoleculeList` that the user will interact with. The basic class is simply:

```java
public class MoleculeList {
    public AtomNode first;

    public MoleculeList(String e) {
        first = new AtomNode(e, null);
    }
}
```

Already, we can get a vague sense of why a `MoleculeList` is better. Compare the creation of an `AtomChain` of one atom to the creation of a `MoleculeList` of one atom.

```java
AtomChain C1 = new AtomChain("H", null);
MoleculeList M2  = new MoleculeList("H");
```

The `MoleculeList` hides the detail that there exists a null bond from the user. The `MoleculeList` class isn't very useful yet, so let's add an `addFirst` and `getFirst` method as simple warmup methods. Consider trying to write them yourself before reading on.

#### addFirst and getFirst <a href="#addfirst-and-getfirst" id="addfirst-and-getfirst"></a>

`addFirst` is relatively straightforward if you understood chapter 2.1. With `AtomChains`, we added to the front with the line of code `C = new AtomChain("H", C)`. Thus, we end up with:

```java
public class MoleculeList {
    public AtomNode first;

    public MoleculeList(String e) {
        first = new AtomNode(e, null);
    }

    /** Adds an atom to the front of the list. */
    public void addFirst(String e) {
        first = new AtomNode(e, first);
    }
}
```

`getFirst` is even easier. We simply return `first.element`:

```java
/** Retrieves the front atom from the list. */
public String getFirst() {
    return first.element;
}
```

The resulting `MoleculeList` class is much easier to use. Compare:

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

Comparing the two data structures visually, we have: (with the `AtomChain` version on top and `MoleculeList` version below it)

![AtomChain_vs_MoleculeList.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig22/IntList_vs_SLList.png)

Essentially, the `MoleculeList` class acts as a middleman between the molecule user and the naked recursive data structure. As suggested above in the `AtomChain` version, there is a potentially undesirable possibility for the `AtomChain` user to have variables that point to the middle of the `AtomChain`. As Ovid said: [Mortals cannot look upon a god without dying](https://en.wikipedia.org/wiki/Semele), so perhaps it is best that the `MoleculeList` is there to act as our intermediary.

**Exercise 2.2.1**: The curious reader might object and say that the `AtomChain` would be just as easy to use if we simply wrote an `addFirst` method. Try to write an `addFirst` method to the `AtomChain` class. You'll find that the resulting method is tricky as well as inefficient.

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
...
```

Private variables and methods can only be accessed by code inside the same `.java` file, e.g., in this case `MoleculeList.java`. That means that a class like `MoleculeTroubleMaker` below will fail to compile, yielding a `first has private access in MoleculeList` error.

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

It may seem a little silly to restrict access. After all, the only thing that the `private` keyword does is break programs that otherwise compile. However, in large scientific modeling projects, the `private` keyword is an invaluable signal that certain pieces of code should be ignored (and thus need not be understood) by the end user. Likewise, the `public` keyword should be thought of as a declaration that a method is available and will work **forever** exactly as it does now.

As an analogy, a lab setup has certain `public` features, e.g., the stopwatch and measurement markings. Under the hood, there are `private` details about how these operate. While the private details may vary from setup to setup, we expect the same behavior from all `public` features. Changing these would cause great confusion for users, and quite possibly erroneous experiments.

**When you create a `public` member (i.e., method or variable), be careful, because you're effectively committing to supporting that member's behavior exactly as it is now, forever.**

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

This saves a bit of memory, because each `AtomNode` no longer needs to keep track of how to access its enclosing `MoleculeList`.

Put another way, if you examine the code above, you'll see that the `AtomNode` class never uses the `first` variable of `MoleculeList`, nor any of `MoleculeList`'s methods. As a result, we can use the static keyword, which means the `AtomNode` class doesn't get a reference to its boss, saving us a small amount of memory.

If this seems a bit technical and hard to follow, try Exercise 2.2.2. A simple rule of thumb is that _if you don't use any instance members of the outer class, make the nested class static_.

**Exercise 2.2.2** Delete the word `static` as few times as possible so that [this program](https://joshhug.gitbooks.io/hug61b/content/chap2/exercises/Government.java) compiles (Refresh the page after clicking the link and making sure the URL changed). Make sure to read the comments at the top before doing the exercise.

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

By contrast, I'll implement `size` recursively. This method will be somewhat similar to the `size` method we implemented in section [2.1](https://joshhug.gitbooks.io/hug61b/content/chap2/chap21.html) for `AtomChain`.

The recursive call for `size` in `AtomChain` was straightforward: `return 1 + this.next.size()`. For a `MoleculeList`, this approach does not make sense. A `MoleculeList` has no `next` variable. Instead, we'll use a common pattern that is used with middleman classes like `MoleculeList` -- we'll create a private helper method that interacts with the underlying naked recursive data structure.

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

Here, we have two methods, both named `size`. This is allowed in Java, since they have different parameters. We say that two methods with the same name but different signatures are **overloaded**. For more on overloaded methods, see Java's [official documentation](https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html).

An alternate approach is to create a non-static helper method in the `AtomNode` class itself. Either approach is fine, though I personally prefer not having any methods in the `AtomNode` class.

## Improvement #5: Caching <a href="#improvement-5-caching" id="improvement-5-caching"></a>

Consider the `size` method we wrote above. Suppose `size` takes 2 seconds on a list of size 1,000. We expect that on a list of size 1,000,000, the `size` method will take 2,000 seconds, since the algorithm has to step through 1,000 times as many atoms in the list to reach the end. Having a `size` method that is very slow for large lists is unacceptable, since we can do better.

It is possible to rewrite `size` so that it takes the same amount of time, no matter how large the list.

To do so, we can simply add a `size` variable to the `MoleculeList` class that tracks the current size, yielding the code below. This practice of saving important data to speed up retrieval is sometimes known as **caching**.

```java
public class MoleculeList {
    ... /* AtomNode declaration omitted. */
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

This modification makes our `size` method incredibly fast, no matter how large the list. Of course, it will also slow down our `addFirst` and `addLast` methods, and also increase the memory usage of our class, but only by a trivial amount. In this case, the tradeoff is clearly in favor of creating a cache for size.

#### Improvement #6: The Empty List <a href="#improvement-6-the-empty-list" id="improvement-6-the-empty-list"></a>

Our `MoleculeList` has a number of benefits over the simple `AtomChain` from chapter 2.1:

* Users of a `MoleculeList` never see the `AtomChain` class.
  * Simpler to use.
  * More efficient `addFirst` method (exercise 2.2.1).
  * Avoids errors or malfeasance by `AtomChain` users.
* Faster `size` method than possible with `AtomChain`.

Another natural advantage is that we will be able to easily implement a constructor that creates an empty list. The most natural way is to set `first` to `null` if the list is empty. This yields the constructor below:

```java
public MoleculeList() {
    first = null;
    size = 0;
}
```

Unfortunately, this causes our `addLast` method to crash if we insert into an empty list. Since `first` is `null`, the attempt to access `p.next` in `while (p.next != null)` below causes a null pointer exception.

```java
public void addLast(String e) {
    size += 1;
    AtomNode p = first;
    while (p.next != null) {
        p = p.next;
    }

    p.next = new AtomNode(e, null);
}
```

**Exercise 2.2.3** Fix the `addLast` method. Starter code [here](https://github.com/Berkeley-CS61B/lectureCode/blob/master/lists2/DIY/fixAddLast/SLList.java).

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

In the figures above, the lavender ?? value indicates that we don't care what value is there. Since Java does not allow us to fill in a string with question marks, we just pick some abitrary string like "?" or anything else.

Since a `MoleculeList` without a sentinel has no special cases, we can simply delete the special case from our `addLast` method, yielding:

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

As you can see, this code is much much cleaner!

#### Invariants <a href="#invariants" id="invariants"></a>

An invariant is a fact about a data structure that is guaranteed to be true (assuming there are no bugs in your code).

A `MoleculeList` with a sentinel node has at least the following invariants:

* The `sentinel` reference always points to a sentinel node.
* The front atom (if it exists), is always at `sentinel.next.element`.
* The `size` variable is always the total number of atoms that have been added.

Invariants make it easier to reason about code, and also give you specific goals to strive for in making sure your code works.

A true understanding of how convenient sentinels are will require you to really dig in and do some implementation of your own. You'll get plenty of practice in Lab Project 1. However, we recommend that you wait until after you've finished the next section of this book before beginning Lab Project 1.