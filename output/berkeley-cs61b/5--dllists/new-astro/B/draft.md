# 5. DLLists in Astrophysics

In Chapter 2.2, we crafted the `SLList` class, which was more efficient than our earlier rudimentary recursive `AstronomicalBodyList` data structure. In this section, we'll conclude our discussion of linked lists, and begin learning the fundamentals of arrays that we'll need for an array-based list we'll call an `AList`. As we progress, we'll also reveal the secret behind why we used the peculiar name `SLList` in the previous chapter.

#### addLast <a href="#addlast" id="addlast"></a>

Consider the `addLast(AstronomicalBody x)` method from the previous chapter.

```java
public void addLast(AstronomicalBody x) {
    size += 1;
    AstNode p = sentinel;
    while (p.next != null) {
        p = p.next;
    }

    p.next = new AstNode(x, null);
}
```

The issue with this method is that it is slow. For a long list of celestial bodies, the `addLast` method has to traverse the entire list, much like we observed with the `size` method in chapter 2.2. Similarly, we can expedite the process by introducing a `last` variable to quicken our code, as demonstrated below:

```java
public class SLList {
    private AstNode sentinel;
    private AstNode last;
    private int size;    

    public void addLast(AstronomicalBody x) {
        last.next = new AstNode(x, null);
        last = last.next;
        size += 1;
    }
    ...
}
```

**Exercise 2.3.1:** Consider the illustration representing the `SLList` implementation above, which includes the last pointer for astronomical bodies. Suppose that we'd like to support `addLast`, `getLast`, and `removeLast` operations. Will the structure shown support rapid `addLast`, `getLast`, and `removeLast` operations? If not, which operations are slow?

![sllist_last_pointer.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig23/sllist_last_pointer.png)

**Answer 2.3.1:** `addLast` and `getLast` will be fast, but `removeLast` will be slow. That's because we have no straightforward method to get the second-to-last astronomical body, to update the `last` pointer, after removing the last one.

#### SecondToLast <a href="#secondtolast" id="secondtolast"></a>

The issue with the structure from exercise 2.3.1 is that a method that removes the last astronomical body in the list will be inherently slow. This is because we need to first find the second-to-last item, and then set its next pointer to null. Introducing a `secondToLast` pointer will not help either, as we'd need to locate the third-to-last item in the list to ensure that `secondToLast` and `last` are properly updated after removing the last item.

**Exercise 2.3.2:** Attempt to devise a scheme for speeding up the `removeLast` operation so that it consistently runs in constant time, regardless of the length of the list of astronomical bodies. Don't worry about actually coding up a solution, we'll leave that to project 1. Just come up with an idea on how you'd modify the structure of the list (i.e. the instance variables).

We'll describe the solution in Improvement #7.

#### Improvement #7: Looking Back <a href="#improvement-7-looking-back" id="improvement-7-looking-back"></a>

The most natural way to tackle this issue is to add a previous pointer to each `AstNode`, i.e.

```java
public class AstNode {
    public AstNode prev;
    public AstronomicalBody item;
    public AstNode next;
}
```

In other words, our list now has two links for every astronomical node. One common term for such lists is the "Doubly Linked List", which we'll refer to as a `DLList` for simplicity. This contrasts with the single linked list from chapter 2.2, a.k.a. an `SLList`.

The addition of these extra pointers will lead to increased code complexity. Rather than walk you through it, you'll construct a doubly linked list of celestial bodies on your own in project 1. The illustration below shows more precisely what a doubly linked list looks like for lists of size 0 and size 2, respectively.

![dllist_basic_size_0.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig23/dllist_basic_size_0.png)

![dllist_basic_size_2.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig23/dllist_basic_size_2.png)

#### Improvement #8: Sentinel Upgrade <a href="#improvement-8-sentinel-upgrade" id="improvement-8-sentinel-upgrade"></a>

Back pointers enable a list to support adding, fetching, and removing the front and back of a list in constant time. There is a subtle issue with this design where the `last` pointer occasionally points at the sentinel node, and other times at an actual celestial node. Just like the non-sentinel version of the `SLList`, this results in code with special cases that is far less elegant than what we'll achieve after our 8th and ultimate improvement. (Can you conceive of which `DLList` methods would encounter these special cases?)

One fix is to add a second sentinel node to the back of the list. This results in the topology shown below as an illustration.

![dllist_double_sentinel_size_0.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig23/dllist_double_sentinel_size_0.png)

![dllist_double_sentinel_size_2.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig23/dllist_double_sentinel_size_2.png)

An alternate approach is to configure the list to be circular, with the front and back pointers sharing the same sentinel node.

![dllist_circular_sentinel_size_0.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig23/dllist_circular_sentinel_size_0.png)

![dllist_circular_sentinel_size_2.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig23/dllist_circular_sentinel_size_2.png)

Both the two-sentinel and circular sentinel approaches work and result in code that is free of cumbersome special cases, though I personally find the circular approach to be cleaner and aesthetically more pleasing. We will not delve into the details of these implementations, as you'll have a chance to explore one or both in project 1.

#### Generic DLLists <a href="#generic-dllists" id="generic-dllists"></a>

Our DLLists have a major limitation: they can only hold celestial integer identifiers, not descriptive objects. For instance, suppose we wanted to create a list of Spacecraft Names:

```java
DLList d2 = new DLList("Voyager");
d2.addLast("Pioneer");
```

The code above would fail, as our `DLList` constructor and `addLast` methods only accept an integer.

Fortunately, in 2004, the creators of Java introduced **generics** to the language, allowing you to, among other things, create data structures capable of holding any reference type.

The syntax might initially seem strange. The main idea is that right after the name of the class in your class declaration, you use an arbitrary placeholder inside angle brackets: `<>`. Then, anytime you want to utilize the arbitrary type, you use that placeholder instead.

For example, our earlier `DLList` declaration was:

```java
public class DLList {
    private AstNode sentinel;
    private int size;

    public class AstNode {
        public AstNode prev;
        public AstronomicalBody item;
        public AstNode next;
        ...
    }
    ...
}
```

A generic `DLList` capable of holding any type would resemble:

```java
public class DLList<QuasarType> {
    private AstNode sentinel;
    private int size;

    public class AstNode {
        public AstNode prev;
        public QuasarType item;
        public AstNode next;
        ...
    }
    ...
}
```

In this case, `QuasarType` is simply a name I conjured, and you could use any other name you prefer, like `GalaxyCluster`, `AstroParticle`, or `CosmicRay`.

Now that we've defined a generic version of the `DLList` class, we must also use a unique syntax to instantiate this class. To do this, we put the desired type inside of angle brackets during declaration and use empty angle brackets during instantiation. For example:

```java
DLList<String> d2 = new DLList<>("Voyager");
d2.addLast("Pioneer");
```

Since generics only work with reference types, we cannot put primitives like `int` or `double` inside of angle brackets, e.g. `<int>`. Instead, we use the reference version of the primitive type, which in the case of `int` is `Integer`, e.g.

```java
DLList<Integer> d1 = new DLList<>(42);
d1.insertFront(99);
```

There are additional nuances about working with generic types, but we will postpone them to a later chapter of this book when you've had more opportunity to experiment with them on your own. For now, adhere to the following rules of thumb:

* In the .java file **implementing** a data structure, specify your generic type name only once at the very top of the file, following the class name.
* In other .java files that use your data structure, specify the specific desired type during declaration and use the empty diamond operator during instantiation.
* If you need to instantiate a generic over a primitive type, use `Integer`, `Double`, `Character`, `Boolean`, `Long`, `Short`, `Byte`, or `Float` instead of their primitive counterparts.

Minor detail: You may also declare the type inside of angle brackets when instantiating, though this is not necessary, as long as you're also declaring a variable on the same line. In other words, the following line of code is valid, even though the `Integer` on the right-hand side is repetitive.

```java
DLList<Integer> d1 = new DLList<Integer>(42);
```

At this point, you comprehend everything necessary to implement the `LinkedListDeque` project on project 1, where you'll refine all the knowledge you've acquired in chapters 2.1, 2.2, and 2.3.