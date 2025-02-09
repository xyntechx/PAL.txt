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

#### Improvement #2: Bureaucracy <a href="#improvement-2-bureaucracy" id="improvement-2-bureaucracy"></a>

Knowing that `AtomNodes` are hard to work with, we're going to create a separate class called `MoleculeList` that the user will interact with. The basic class is simply:

```java
public class MoleculeList {
    public AtomNode first;

    public MoleculeList(String e) {
        first = new AtomNode(e, null);
    }
}

Already, we can get a vague sense of why a `MoleculeList` is better. Compare the creation of an `AtomChain` of one atom to the creation of a `MoleculeList` of one atom.

```java
AtomChain C1 = new AtomChain("H", null);
MoleculeList M2  = new MoleculeList("H");
```

The `MoleculeList` hides the detail that there exists a null bond from the user. The `MoleculeList` class isn't very useful yet, so let's add an `addFirst` and `getFirst` method as simple warmup methods. Consider trying to write them yourself before reading on.

Rebranding in the context of computer science might initially seem unrelated to chemistry, but there's an intriguing connection in how one can think about the revitalization of both a software product and a chemical compound. Just as a rebranding effort involves changing the perception and presentation of a product to attract new users or rekindle interest among existing ones, chemists often explore different forms or derivatives of a compound to enhance its effectiveness or broaden its use.

For instance, consider how chemists might rebrand a compound by altering its formulation or delivery method. This can be similar to how software developers update the interface, features, or even the very mission of a software product to better meet the needs of its users or to penetrate new markets. Both processes require a deep understanding of the initial product or compound, its strengths and limitations, and the needs and desires of the target audience.

Effective rebranding in computer science involves market research, creative design, and strategic communication, while in chemistry, it may involve research, synthesis, and tests to reach new applications. The goal in both fields is not only to improve upon what already exists but also to give it a new identity that resonates more effectively with the intended audience, whether that be consumers of a digital service or users of a chemical product.

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

#### Improvement #2: Bureaucracy <a href="#improvement-2-bureaucracy" id="improvement-2-bureaucracy"></a>

Knowing that `AtomNodes` are hard to work with, we're going to create a separate class called `MoleculeList` that the user will interact with. The basic class is simply:

```java
public class MoleculeList {
    public AtomNode first;

    public MoleculeList(String e) {
        first = new AtomNode(e, null);
    }
}

Already, we can get a vague sense of why a `MoleculeList` is better. Compare the creation of an `AtomChain` of one atom to the creation of a `MoleculeList` of one atom.

```java
AtomChain C1 = new AtomChain("H", null);
MoleculeList M2  = new MoleculeList("H");
```

The `MoleculeList` hides the detail that there exists a null bond from the user. The `MoleculeList` class isn't very useful yet, so let's add an `addFirst` and `getFirst` method as simple warmup methods. Consider trying to write them yourself before reading on.

In computer science, the term "bureaucracy" within the context of algorithm design can draw an interesting parallel to processes often seen in chemical reactions or industrial chemistry.

Consider the bureaucratic process in a governmental or corporate setting where there are procedures and checks that must be followed methodically to achieve a specific result. This mirrors how, in chemistry, specific steps or protocols need to be followed in a reaction or process to yield a successful outcome. Likewise, in computer science, particularly in algorithm design, "bureaucracy" refers to the systematic, structured steps an algorithm may follow to ensure the successful completion of computational tasks.

One could understand this as the series of "papers" or data points that need to be "stamped" or processed as they pass through each stage of an algorithm. Just as in a chemical process where intermediates are formed and must transform step by step under certain conditions, algorithms proceed in layers of abstraction and rules to effectively solve a problem.

Thus, the term "bureaucracy" in algorithms refers to the necessary structural overhead needed to maintain order and efficiency as a program grows more complex. When designing an algorithm, especially a large-scale one, it's crucial to have these layers organized, much as you would in a complex chemical synthesis, where each reaction stage needs to be meticulously planned and controlled for optimal results.

Recognizing and optimizing these "bureaucratic" structures in algorithms can lead to more efficient computational processes, similarly to how refining pathways in chemical syntheses can lead to improved yields and purity in products.

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

Imagine you are working with a chemical inventory list, where you have various chemicals lined up in a sequence. Let's say you are maintaining a list of chemical containers for an experiment. In computing, particularly in the context of a data structure called a 'linked list,' there are methods such as `addFirst` and `getFirst` that help organize and access data efficiently.

- **addFirst**: This is akin to adding a new container at the very front of your sequence of chemicals. Similar to when a new batch of a crucial reagent arrives in the lab, and you want it immediately accessible, you place it right at the start of your list. This operation ensures that the container you just placed is the first one you'll encounter, which means it's the first one you'd pick when starting an experiment.

- **getFirst**: Imagine needing to quickly grab the first chemical on your list—perhaps for a time-sensitive experiment. The `getFirst` operation gives you access to this leading container without altering its position in the lineup. It’s like reaching into the front of your shelf to retrieve the first container, ensuring you efficiently grab what's critical without rearranging your whole inventory.

In the context of computing, these operations help manage data efficiently within dynamic lists. In chemistry, where time and precision are of the essence, understanding such structured data management can aid in devising algorithms that simulate chemical processes, catalog data, or even control experimental workflows.

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

In computer science, especially in programming and software development, the concepts of public and private are central to object-oriented programming (OOP). These terms refer to the accessibility levels of components within a class, which is a blueprint for creating objects (a key concept not unlike how you use the periodic table to understand the behavior of elements).

Imagine you have a chemistry lab with various sections. Some areas are accessible to everyone, like the general workspace, while others, like the storage for hazardous materials, are restricted and only accessible to certain people for safety reasons. This is similar to how public and private access works in programming.

**Public** components are accessible to everyone and everywhere in your program. They are akin to the general workspace in your lab, where you can perform synthesis or analyze compounds without any restrictions. In a chemistry program, if an object’s method or variable is public, it can be used across different parts of the application.

**Private** components, on the other hand, are like those hazardous materials stored away from public access. They can only be accessed within the confines of their specific class. This ensures that critical parts of the program are protected from unintended interference or misuse, which could disrupt the stability or reliability of your program, much like mishandling hazardous materials could disrupt a lab setup.

Public and private access help in encapsulating data, maintaining clean interfaces, and protecting the integrity of classes in programming. Similarly, in a chemistry lab, clear boundaries help maintain safety and ensure efficient, responsible handling of substances and equipment. Understanding these concepts can enhance both your programming skills and your appreciation of chemistry laboratory management.

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

As a chemistry enthusiast, you're likely familiar with the concept of nested structures at the molecular level. Think of how complex molecules like proteins have a hierarchy where smaller building blocks, such as amino acids, fold into secondary, tertiary, and quaternary structures. In computer science, there's a similar idea using nested classes, which are like having smaller, related components within a larger complex structure.

In programming, a nested class is a class defined within another class. This is akin to having a specific molecular group within a larger molecule. The idea is to create a logical grouping for a class that is only useful in the context of the outer class—much like how a functional group is crucial to the properties of a molecule but doesn’t necessarily make sense outside of it.

For instance, in a chemistry simulation program, you might have a class called `Molecule` that represents a complete molecule. Within it, you might define a nested class called `Atom`, as each `Atom` is a fundamental, indivisible part of every `Molecule`. This allows the program to keep the structure neat and demonstrates the direct relationship between `Atom` and `Molecule`.

So, just as nested structures in chemistry help in understanding properties and reactions by logically grouping certain parts, nested classes in programming help maintain organization and encapsulation, aiding in the development of complex systems where components have clear, hierarchical relationships.

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

Imagine you're conducting an experiment in chemistry where you're observing the properties of different liquids. Each time you get a new liquid sample, you add it to your list of experiments. This is similar to how computer scientists use a method called `addLast()` when working with data structures, like lists.

In computing, a list is like a beaker where you collect samples—in this case, these samples are data items. **`addLast()`** is a function used to add an item to the end of this list. It's akin to taking your latest sample of liquid and pouring it into the last spot in a row of test tubes you've lined up in your lab. Each time you get new information, you store it at the "end" of your current "list" of data.

Now, every chemist wants to know how many samples they have at any moment to keep their records straight and for further analysis. In computer science, we use a method called **`size()`** to count how many items are in our list or our "collection of samples". Just like you might count how many test tubes you filled, `size()` will tell you the number of data items that have been stored in your list.

Understanding these concepts in CS is as crucial as keeping track of your samples and experiments in chemistry. You want to be able to add new data in a systematic way and know your total data count, similar to how you'd manage handling and documentation of samples in chemistry research.

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

In computer science, the concept of caching is incredibly similar to certain processes in chemistry where temporary storage of reactive intermediates is crucial for efficient reactions. To introduce caching to someone with a chemistry background, think about catalysts or intermediates in a reaction pathway.

In chemical reactions, especially in multi-step syntheses, intermediates are often formed that temporarily hold energy or structural information needed for the subsequent step. Similarly, caching in computing is about storing data temporarily so it can be accessed more quickly when needed rather than recalculating or retrieving it from a slower storage mechanism.

Imagine you're running a complex computation (or chemical reaction), and one portion of the process needs to repeatedly access certain data values (akin to reusing an intermediate). Rather than recalculating these values every time (analogous to synthesizing more intermediates), a cache stores these values close to the processing unit so they can be quickly accessed, mimicking the way enzymes stabilize transition states or as storage of intermediates speeds up metabolic pathways.

This optimization is vital because fetching data from a cache significantly reduces time, much like a catalyst reduces the energy barrier and speeds up a chemical reaction. Caching improves performance in computing the way nature uses efficiencies in chemical processes to sustain life efficiently.

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

In computer science, an *empty list* can be compared to a barren flask in chemistry. Just as a flask initially might be empty before you add any chemicals to conduct an experiment, an empty list is a data structure in programming that has no elements in it at the start.

From a programming standpoint, an empty list acts as a placeholder, ready to store elements later, similar to how an empty flask is ready to hold reactants for a chemical reaction. The concept becomes powerful when you consider operations on lists, particularly in processing data where you need a clean slate to start gathering information — much like starting with a clean flask before mixing substances to avoid contamination.

When dealing with complex chemical equations, you wouldn’t want unintended materials left in your flask, just like in programming you wouldn’t want unintended data in your lists. By initializing lists as empty, we ensure that only the elements which you explicitly choose are there.

Moreover, empty lists in algorithms can serve as buffer spaces or temporary holding pens, essential for storing intermediate results. This is much like using empty beakers or flasks to temporarily hold substances when separating or purifying chemicals.

Thus, understanding and using an empty list in programming is like preparing tools in a lab to ensure precision and accuracy in conducting experiments.

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

A sentinel node in computer science serves as a convenient marker or placeholder, especially in data structures like linked lists. Let's draw a similarity to a concept familiar in chemistry to make it more relatable.

Imagine a sentinel node as an unreactive element or a noble gas, such as neon or argon, sitting at the edge of a series of chemical reactions. Like noble gases, which are often used to avoid reactions because of their stability and non-reactivity, a sentinel node serves as a boundary or end marker in a list, indicating limits without being involved in the primary process of data manipulation or storage.

In a linked list, sentinel nodes could easily be compared to end caps in a series of reactions where you might need to define either the start or end point of your process without those points actively engaging in chemical changes – much like how neon signs glow but don’t react with their surrounding environment.

The purpose of these sentinel nodes is to simplify algorithms; they help avoid edge cases, which are exceptional conditions that can sometimes complicate programming logic. By functioning as a boundary, they make traversal through a data structure cleaner and more efficient, much like how a noble gas might act as an unchanging barrier in a controlled chemical environment to maintain stability and ensure smooth operation.

So, by thinking of sentinel nodes as the noble gases of linked lists, we can appreciate their role in maintaining order and facilitating smooth operations without directly 'reacting' with the data they contain or organize.

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

In the realm of computer science, the concept of **invariants** is fundamental to understanding how systems maintain consistent behavior under changing conditions. This can be fascinatingly relatable to principles you often encounter in chemistry.

Invariants in CS refer to properties or conditions that remain unchanged even as other aspects of a system evolve during the process of computation or execution of an algorithm. They act as fixed points of truth that hold throughout different states of the system or algorithm operations.

Think of invariants as akin to the **conservation laws** in chemistry, such as the conservation of mass or energy in a chemical reaction. Just as mass is conserved in a closed system—regardless of how the substances within are transformed—an invariant is a property of a program that remains steady no matter the changes or iterations happening during its runtime.

For instance, consider sorting algorithms like bubble sort. An important invariant in bubble sort is that at the end of each full pass through the list, the largest unsorted element is correctly placed in its final position. Regardless of how the list changes from one pass to the next, this condition remains true, guiding the algorithm to completion.

Understanding invariants ensures reliability and predictability in software, similar to how knowing conservation laws allows chemists to predict product amounts in reactions. Both concepts bring a layer of structure and insight into complex systems, whether in coding a program to perform specific tasks or in predicting the outcomes of synthesizing new compounds.

