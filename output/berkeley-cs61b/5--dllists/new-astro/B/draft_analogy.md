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

A Doubly Linked List (DLList) is a data structure that might not seem immediately relevant to astrophysics, but understanding it can provide valuable insight into how data is organized and manipulated, which is crucial for managing the vast amounts of data generated in astrophysics research.

In essence, a DLList is a sequence of elements, each containing a 'node' that holds three parts: the data itself, a reference to the next node, and a reference to the previous node. This structure allows for traversal in both directions, making operations like insertion and deletion of elements more efficient than in a singly linked list, where you can only traverse in one direction.

In astrophysics, imagine you are trying to process or model a series of observations captured by a telescope over time. The ability to efficiently insert new data points, remove outliers, or modify entries as new information becomes available is crucial. A DLList can help manage these tasks with reduced computational overhead compared to other structures.

Furthermore, understanding linkages and pointers within DLLists is akin to understanding the relationships between celestial bodies and their movements. Just as nodes in a DLList are interconnected, cosmic entities like stars and planets are interconnected through gravitational forces and other physical interactions. Grasping how these connections work computationally can provide a more intuitive grasp of how models are built to simulate real astrophysical phenomena.

Learning about computer science concepts like DLLists sharpens problem-solving skills and enhances your ability to work with complex datasets, both of which are vital skills in the field of astrophysics.

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

In computer science, the concept of "addLast" typically applies to data structures known as linked lists, specifically a type called a "doubly linked list." Imagine a linked list as a sequence of nodes, where each node contains some data and a reference (or link) to the next and, in the case of doubly linked lists, the previous node in the sequence. Think of it like a train where each car is linked to the next, and they can also be linked to the one behind.

The "addLast" operation is used to add a new element to the end of this sequence. This is akin to attaching a new car to the end of a train. In the context of astrophysics, you can think of this like adding a new satellite or probe at the edge of a sequence of celestial bodies being monitored or explored. Just as you might add a new part to a space exploration mission, "addLast" places a new node at the end of the list, maintaining the linked sequence.

This can be particularly useful when dealing with large datasets or sequences, such as star observations, planetary data, or simulations of large cosmic structures, where you often need flexible and dynamic ways to manage data that can grow over time as new data comes in. A linked list allows adding new data (nodes) without having to reorganize the entire dataset, providing both efficiency and flexibility.

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

The CS concept of "SecondToLast" refers to an operation often found in programming where you need to identify or retrieve the second to last element from a sequence, like a list or an array. This might seem like a simple idea, but it's a perfect example of how computational thinking and programming skills are applied to create specific solutions in a step-by-step fashion.

Now, considering your interest in astrophysics, think about a sequence of data points that represent the brightness of a star over time (like how you might see in light curves from observational astronomy). If you wanted to analyze a specific time point just before the last observation (for instance, to compare it to the last to understand sudden changes better), you would use a method or algorithm similar to "SecondToLast" to zoom in on that specific data point. 

This concept is not just about finding an element but thinking about data manipulation and the clear, logical steps needed to achieve your goals—similar to how computational algorithms process vast amounts of astronomical data to help us understand cosmic phenomena. So, "SecondToLast" is a handy tool for any astrophysics researcher who frequently deals with sequences of data.

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

Looking Back is a concept primarily used within the field of computer science, particularly in optimization and problem-solving. It involves using information from previous computations or decisions to inform future choices. This method is often applied in algorithms to enhance efficiency and accuracy when tackling complex problems, such as in backtracking algorithms.

Now, how does this relate to your interest in astrophysics? Just as Looking Back helps refine computational techniques by utilizing previous steps to improve current decisions, astrophysics also thrives on the idea of reflecting back on past data to make sense of the universe. Consider how scientists utilize historical astronomical data—like star positions, brightness, and redshifts—to inform models of galaxy evolution or to test theories of the universe’s expansion.

For example, the initial data from cosmic microwave background radiation or observations of distant supernovae provide clues that allow physicists to refine models of the Big Bang or the accelerating universe. In a programmatic context, Looking Back can help streamline the analysis of massive datasets collected by telescopes by identifying patterns, errors, or anomalies that previous runs may have flagged. This iterative process is akin to an astrophysicist revisiting past analyses, learning from them, and applying those insights to refine simulations or improve the interpretation of new cosmic observations.

Thus, whether in algorithm design or studying celestial phenomena, the principle of Looking Back emphasizes an iterative refinement process crucial for making discoveries and improving understanding in both computer science and astrophysics.

#### Improvement #8: Sentinel Upgrade <a href="#improvement-8-sentinel-upgrade" id="improvement-8-sentinel-upgrade"></a>

Back pointers enable a list to support adding, fetching, and removing the front and back of a list in constant time. There is a subtle issue with this design where the `last` pointer occasionally points at the sentinel node, and other times at an actual celestial node. Just like the non-sentinel version of the `SLList`, this results in code with special cases that is far less elegant than what we'll achieve after our 8th and ultimate improvement. (Can you conceive of which `DLList` methods would encounter these special cases?)

One fix is to add a second sentinel node to the back of the list. This results in the topology shown below as an illustration.

![dllist_double_sentinel_size_0.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig23/dllist_double_sentinel_size_0.png)

![dllist_double_sentinel_size_2.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig23/dllist_double_sentinel_size_2.png)

An alternate approach is to configure the list to be circular, with the front and back pointers sharing the same sentinel node.

![dllist_circular_sentinel_size_0.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig23/dllist_circular_sentinel_size_0.png)

![dllist_circular_sentinel_size_2.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig23/dllist_circular_sentinel_size_2.png)

Both the two-sentinel and circular sentinel approaches work and result in code that is free of cumbersome special cases, though I personally find the circular approach to be cleaner and aesthetically more pleasing. We will not delve into the details of these implementations, as you'll have a chance to explore one or both in project 1.

The concept of a "sentinel upgrade" in computer science can be quite intriguing, especially when viewed through the lens of astrophysics. In computer science, a sentinel is a specific value that is used to control the operation of a loop or an algorithm, typically to signal the start or end of a process. Sentinels help ensure that computer programs operate smoothly and efficiently by providing a clear definition for stopping or for transitions, much like how certain celestial events act as markers in the study of the universe.

To relate this to astrophysics, think about the role of specific astronomical phenomena or celestial markers, such as the transit of a planet across a star, or the appearance of a particular constellation at certain times of the year. These events act as "sentinels" in the cosmos, providing astronomers with cues for observations, timing, and even alerting them to changes or completion of a cosmic cycle.

By upgrading a sentinel in a software context, programmers can refine how they detect or transition from one state to another, ensuring more robust and error-free operations. Similarly, in astrophysics, refining our "sentinels"—whether they be instruments, mathematical models, or observational techniques—can lead to more accurate readings, improved predictions, and ultimately a better understanding of the universe.

So, the idea of a "sentinel upgrade" emphasizes the importance of improving the markers and boundaries we use in both programming and astrophysical research to achieve greater precision and efficiency in our work.

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

As an astrophysics enthusiast, you often deal with vast amounts of data. Whether it's processing images from telescopes or simulating the dynamics of galaxies, managing complex data efficiently is crucial. This is where understanding data structures, a fundamental concept of computer science, becomes invaluable.

One particular data structure that can be quite beneficial in handling and organizing large datasets is the "Generic Doubly Linked List" (DLList). Imagine it as a way to store sequences of data where each item is a node containing some value, and importantly, each node is connected to both its predecessor and successor. This bidirectional navigation is akin to looking at a star map where you can move in any direction—forward and backward—making adjustments and recalibrations easier and more efficient.

A generic doubly linked list is versatile because it can handle different types of data without needing to rewrite or redesign the list structure for each new dataset. In astrophysics, this means you can store different measurements such as temperature readings, distance, or luminosity values all in one cohesive system, allowing for interconnected data processing and analysis.

Let’s say you're simulating the motion of celestial objects under gravity. You could use a generic DLList to manage the state of each object—such as its position, velocity, and other attributes—and update these states iteratively. The benefit here is clear: you can efficiently traverse through your list in both directions, facilitate complex time-stepping simulations, and modify or access any celestial object's data at any time without needing to reorder or restructure the data sequentially.

Furthermore, if at any point you need to add more data points or remove some obsolete measurements, the DLList allows for dynamic memory allocation, which means you can easily insert or delete nodes without affecting the integrity of the entire dataset. This flexibility can be especially useful when dealing with unpredictable phenomena, like unexpected observational data or when adjusting parameters in a cosmic simulation.

In essence, understanding and using generic doubly linked lists can dramatically improve how you handle multi-faceted and expansive datasets common in astrophysics, offering both efficiency and versatility in data management and manipulation.

