# 4. SLLists

In Chapter 3, we built the `IntList` class, a list data structure that can technically do all the things a list can do. However, in practice, the `IntList` suffers from the fact that it is fairly awkward to use, resulting in code that is hard to read and maintain.

Fundamentally, the issue is that the `IntList` is what I call a **naked recursive** data structure. In order to use an `IntList` correctly, the programmer must understand and utilize recursion even for simple list-related tasks. This requires a deeper understanding of recursion, which can limit its accessibility to novice programmers and introduce a whole new class of tricky errors, especially when helper methods provided by the `IntList` class are not effectively utilized.

Inspired by our experience with the `IntList`, we'll now build a new class `SLList`, which more closely resembles the list implementations used in modern languages. SLList aims to simplify access and usability, akin to how Byzantine governance was designed to streamline administration while handling complexity. We'll achieve this by iteratively adding a sequence of improvements. This includes enhancing user experience through better encapsulation—like the private versus public access seen in object-oriented programming and historical governance systems—aiding in maintaining code readability and reducing potential errors.

Moreover, sentinel nodes are compared to Roman boundary markers, serving as boundary markers themselves in lists. They improve list operations by avoiding null checks, enhancing the robustness and efficiency of the list structure. Finally, invariants in coding practices, paralleling the maintenance of boundaries, ensure list integrity and are crucial for effective debugging throughout software development.

#### Improvement #1: Rebranding <a href="#improvement-1-rebranding" id="improvement-1-rebranding"></a>

Our `IntList` class from last time was as follows, with helper methods omitted:

```java
public class IntList {
    public int first;
    public IntList rest;

    public IntList(int f, IntList r) {
        first = f;
        rest = r;
    }
...
```

Our first step will be to simply rename everything and throw away the helper methods. This probably doesn't seem like progress, but trust me, I'm a professional.

```java
public class IntNode {
    public int item;
    public IntNode next;

    public IntNode(int i, IntNode n) {
        item = i;
        next = n;
    }
}
```

Just like the Renaissance, where there was a significant transformation of thought from medieval scholasticism to humanism—where different disciplines sought to refine and expand their ideas—the `IntNode` rebrands its terms, paving the way for conceptual enhancements similar to how historical shifts opened new avenues in society. This simplification enhances our understanding and usability, paralleling the transition from obscured medieval methodologies to the clearer humanistic approaches of the Renaissance. Such rebranding reflects on the refined visibility and accessibility features akin to object-oriented programming's key principles, facilitating a more user-friendly experience while retaining core functional capabilities. Additionally, this renaming is analogous to how historical figures were rebranded, such as the transition from Hermes to Mercury, representing not just a name change but broader cultural and technological implications. Thus, these changes are more than cosmetic; they offer deeper insights into structure and efficiency, aligning with broader shifts seen in history, where new nomenclature and ideas led to expanded horizons in understanding.

#### Improvement #2: Bureaucracy <a href="#improvement-2-bureaucracy" id="improvement-2-bureaucracy"></a>

Knowing that `IntNodes` are hard to work with, we're going to create a separate class called `SLList` that the user will interact with. The basic class is simply:

```java
public class SLList {
    public IntNode first;

    public SLList(int x) {
        first = new IntNode(x, null);
    }
}
```

The `SLList` class serves as a bureaucratic system much like the complexity of civil services that evolved during the Qing Dynasty, but also ensures simplicity in user interaction, akin to the way Roman delegates facilitated interactions between the populace and higher authorities. This setup ensures that the user doesn't have to deal directly with the difficulties posed by handling raw `IntNodes`. 

We can notice why a `SLList` is more approachable. Compare the creation of an `IntList` of one item to the creation of a `SLList` of one item:

```java
IntList L1 = new IntList(5, null);
SLList L2  = new SLList(5);
```

The `SLList` simplifies the user's experience by hiding internal complexities and enabling easier list manipulations, much like how Byzantine scribes organized and clarified messages for broader understanding, rather than merely masking complexity.

To enhance the `SLList` utility, let’s add an `addFirst` and `getFirst` method as a starting point. Try constructing them yourself before reading on.

#### addFirst and getFirst <a href="#addfirst-and-getfirst" id="addfirst-and-getfirst"></a>

`addFirst` is relatively straightforward if you understood chapter 2.1. With `IntLists`, we added to the front with the line of code `L = new IntList(5, L)`. Thus, we end up with:

```java
public class SLList {
    public IntNode first;

    public SLList(int x) {
        first = new IntNode(x, null);
    }

    /** Adds an item to the front of the list. */
    public void addFirst(int x) {
        first = new IntNode(x, first);
    }
}
```

This is analogous to the strategy of enveloping in layers to provide security, akin to fortifications built around medieval castles to ensure strength and defense, where in our code, elements stack in front to build a stronghold.

`getFirst` is even easier. We simply return `first.item`:

```java
/** Retrieves the front item from the list. */
public int getFirst() {
    return first.item;
}
```

The resulting `SLList` class is much easier to use. Compare:

```java
SLList L = new SLList(15);
L.addFirst(10);
L.addFirst(5);
int x = L.getFirst();
```

to the `IntList` equivalent:

```java
IntList L = new IntList(15, null);
L = new IntList(10, L);
L = new IntList(5, L);
int x = L.first;
```

Comparing the two data structures visually, we have: (with the `IntList` version on top and `SLList` version below it)

![IntList_vs_SLList.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig22/IntList_vs_SLList.png)

Essentially, the `SLList` class acts as a mediator between the list user and the raw recursive data structure. As suggested above in the `IntList` version, there is a potentially undesirable possibility for the `IntList` user to have variables that point to the middle of the `IntList`. Just as delegated representatives in the Roman Republic handled the intricate details of governance, much like bureaucratic systems today, without involving common citizens in all the complexities, the `SLList` buffers users from the complexity of recursive lists, making data management accessible and intuitive.

However, an important aspect to consider is that while `IntList` might seem trickier, it can be useful for more direct manipulations when traversal operations are necessary, illustrating a technical trade-off between raw power and user safety.

**Exercise 2.2.1**: The curious reader might object and say that the `IntList` would be just as easy to use if we simply wrote an `addFirst` method. Try to write an `addFirst` method to the `IntList` class. You'll find that the resulting method is tricky as well as inefficient, echoing some of the inefficiencies in historical government systems that didn't adapt intermediary strategies.

#### Improvement #3: Public vs. Private <a href="#improvement-3-public-vs-private" id="improvement-3-public-vs-private"></a>

Unfortunately, our `SLList` can be bypassed, allowing direct and unsafe modification of the list's structure. This is akin to how skilled artisans in historical societies could produce items outside of regulatory oversight. Such unmediated access to the list’s internals risks creating undesirable behaviors, like an infinite loop.

```java
SLList L = new SLList(15);
L.addFirst(10);
L.first.next.next = L.first.next;
```

This code results in a malformed list. To prevent such issues, we can change the `SLList` class so that the `first` variable is `private`.

```java
public class SLList {
    private IntNode first;
...
```

Private variables and methods are only accessible within the same `.java` file, akin to restricted access areas in ancient societies that preserved important knowledge and treasures.

This means that a class like `SLLTroubleMaker` below cannot modify `first`, yielding a `first has private access in SLList` error.

```java
public class SLLTroubleMaker {
    public static void main(String[] args) {
        SLList L = new SLList(15);
        L.addFirst(10);
        L.first.next.next = L.first.next;
    }
}
```

Conversely, any code inside `SLList.java` can still access the `first` variable. At first glance, restricting access may seem unnecessary as it only causes compilation errors. However, in large software projects, using `private` effectively communicates which parts of the code should remain untouched by users, promoting encapsulation. This concept is not unlike maintaining controlled access to complex systems to avoid disruptions, something historically seen in both engineering and societal governance.

An analogy from everyday life involves `public` features like a car’s pedals. The way these operate internally is `private`, much like system internals, allowing different implementations while ensuring consistent, expected behavior. Changes in those implementations could cause significant user disruption, similar to shifts in public policy by ancient empires leading to unrest.

**When you create a `public` member (i.e., a method or variable), be cautious, as you're committing to maintain that member's behavior consistently.**

#### Improvement #4: Nested Classes <a href="#improvement-4-nested-classes" id="improvement-4-nested-classes"></a>

At the moment, we have two `.java` files: `IntNode` and `SLList`. However, the `IntNode` is really just a supporting character in the story of `SLList`, much like a squire to a knight in medieval tournaments, pivotal but not the main participant.

Java provides us with the ability to embed a class declaration inside another for just this situation. The syntax is straightforward and intuitive:

```java
public class SLList {
       public class IntNode {
            public int item;
            public IntNode next;
            public IntNode(int i, IntNode n) {
                item = i;
                next = n;
            }
       }

       private IntNode first; 

       public SLList(int x) {
           first = new IntNode(x, null);
       } 
...
```

Having a nested class has no meaningful effect on code performance, and is simply a tool for keeping code organized, similar to archives in Ancient Alexandria, which had sections distinctly categorized for ease of access and study.

If the nested class has no need to use any of the instance methods or variables of `SLList`, you may declare the nested class `static`, as follows. Declaring a nested class as `static` means that methods inside the static class cannot access any of the members of the enclosing class. In this case, it means that no method in `IntNode` would be able to access `first`, `addFirst`, or `getFirst`.

```java
public class SLList {
       public static class IntNode {
            public int item;
            public IntNode next;
            public IntNode(int i, IntNode n) {
                item = i;
                next = n;
            }
       }

       private IntNode first;
...
```

This saves a bit of memory because each `IntNode` no longer needs to keep track of how to access its enclosing `SLList`. It resembles the efficient use of resources similar to historical inventions like the windcatchers of Ancient Persia, which were simple yet frugal in resource use.

Another way to see it is by examining the code above. Notice that the `IntNode` class never uses the `first` variable of `SLList`, nor any of `SLList`'s methods. As a result, we can use the `static` keyword, which means the `IntNode` class doesn't get a reference to its enclosing `SLList`, saving us a small amount of memory.

If this seems a bit technical and hard to follow, try Exercise 2.2.2. A good rule of thumb is that _if you don't use any instance members of the outer class, make the nested class static_.

**Exercise 2.2.2** Delete the word `static` as few times as possible so that [this program](https://joshhug.gitbooks.io/hug61b/content/chap2/exercises/Government.java) compiles (Refresh the page after clicking the link and making sure the URL changed). Make sure to read the comments at the top before doing the exercise.

#### addLast() and size() <a href="#addlast-and-size" id="addlast-and-size"></a>

To motivate our remaining improvements and also demonstrate some common patterns in data structure implementation, we'll add `addLast(int x)` and `size()` methods. You're encouraged to take the [starter code](https://github.com/Berkeley-CS61B/lectureCode/blob/master/lists2/DIY/addLastAndSize/SLList.java) and try it yourself before reading on. I especially encourage you to try to write a recursive implementation of `size`, which will yield an interesting challenge.

I'll implement the `addLast` method iteratively, though you could also do it recursively. The idea is fairly straightforward: we create a pointer variable `p` and have it iterate through the list to the end. This operation resembles navigating a Roman road network, both providing a straightforward path to a destination, albeit with different complexities for lists of varying lengths.

```java
/** Adds an item to the end of the list. */
public void addLast(int x) {
    IntNode p = first;

    /* Advance p to the end of the list. */
    while (p.next != null) {
        p = p.next;
    }
    p.next = new IntNode(x, null);
}
```

By contrast, I'll implement `size` recursively. This method will be somewhat similar to the `size` method we implemented in section [2.1](https://joshhug.gitbooks.io/hug61b/content/chap2/chap21.html) for `IntList`.

The recursive call for `size` in `IntList` was straightforward: `return 1 + this.rest.size()`. For a `SLList`, this approach does not make sense. A `SLList` has no `rest` variable. Instead, we'll use a common pattern that is used with middleman classes like `SLList` -- we'll create a private helper method that interacts with the underlying naked recursive data structure.

This approach mirrors historical practices, like how Roman delegates facilitated administration by managing complex information for higher authorities, allowing for efficient governance without burdening the top with unnecessary details.

This yields a method like the following:

```java
/** Returns the size of the list starting at IntNode p. */
private static int size(IntNode p) {
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

Here, we have two methods, both named `size`. This is allowed in Java, since they have different parameters. We say that two methods with the same name but different signatures are **overloaded**. Similar to different interpretations of Shakespearean plays, like how "Julius Caesar" has been adapted through various cultural lenses; each method in Java presents a unique perspective by how it embodies its functionality. For more on overloaded methods, see Java's [official documentation](https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html).

An alternate approach is to create a non-static helper method in the `IntNode` class itself. Either approach is fine, though I personally prefer not having any methods in the `IntNode` class, which helps in maintaining cleaner and simpler design by preventing unnecessary complexities in the node itself.

## Improvement #5: Caching <a href="#improvement-5-caching" id="improvement-5-caching"></a>

Consider the `size` method we wrote above. Suppose `size` takes 2 seconds on a list of size 1,000. We expect that on a list of size 1,000,000, the `size` method will take 2,000 seconds, since the computer has to step through 1,000 times as many items in the list to reach the end. Having a `size` method that is very slow for large lists is unacceptable, much like the prolonged voyages of merchant ships on historic silk roads, as they strained under the load both in time and peril, despite the expected payoff.

It is possible to rewrite `size` so that it takes the same amount of time, no matter how large the list.

To do so, we can simply add a `size` variable to the `SLList` class that tracks the current size, yielding the code below. This practice of saving important data to speed up retrieval is sometimes known as **caching**. Just as ancient Egyptians would use caches of grain to endure periods of famine or trade shortage, we stockpile the `size` with the `SLList`, ensuring a rapid response when asked for the size of our constructs. However, be aware that caching can come with risks, such as stale data if not properly managed.

```java
public class SLList {
    ... /* IntNode declaration omitted. */
    private IntNode first;
    private int size;

    public SLList(int x) {
        first = new IntNode(x, null);
        size = 1;
    }

    public void addFirst(int x) {
        first = new IntNode(x, first);
        size += 1;
    }

    public int size() {
        return size;
    }
    ...
}
```

This modification makes our `size` method incredibly fast, no matter how large the list. Of course, it will also slow down our `addFirst` and `addLast` methods, and also increase the memory of usage of our class, though only by a trivial amount. In this case, the tradeoff is clearly in favor of creating a cache for size. Much like how the Byzantine Empire did not only reinforce its boundaries as a defensive necessity, but also as a means to enhance the efficiency of its internal governance, the `SLList` reformation strengthens access capabilities while maintaining a critical balance of complexities.



#### Improvement #6: The Empty List <a href="#improvement-6-the-empty-list" id="improvement-6-the-empty-list"></a>

Our `SLList` has a number of benefits over the simple `IntList` from chapter 2.1:

* Users of an `SLList` never see the `IntList` class.
  * Simpler to use.
  * More efficient `addFirst` method (exercise 2.2.1).
  * Avoids errors or malfeasance by `IntList` users.
* Faster `size` method than possible with `IntList`.

Just as the invention of writing allowed cultures to convey thought efficiently compared to oral tradition, SLLists enhance use by simplifying access and speed, analogous to innovations that streamline operations in complex historical systems, like trade routes.

Another natural advantage is that we will be able to easily implement a constructor that creates an empty list. The most natural way is to set `first` to `null` if the list is empty. This yields the constructor below:

```java
public SLList() {
    first = null;
    size = 0;
}
```

However, this causes complications akin to managing a new territory without established governance. Specifically, it causes our `addLast` method to crash if we insert into an empty list. Since `first` is `null`, the attempt to access `p.next` in `while (p.next != null)` below causes a null pointer exception.

```java
public void addLast(int x) {
    size += 1;
    IntNode p = first;
    if (p == null) {
        first = new IntNode(x, null);
        return;
    }
    while (p.next != null) {
        p = p.next;
    }

    p.next = new IntNode(x, null);
}
```

**Exercise 2.2.3** Fix the `addLast` method. Starter code [here](https://github.com/Berkeley-CS61B/lectureCode/blob/master/lists2/DIY/fixAddLast/SLList.java).

### Historical Analogies and Computation 
Consider explaining sentinel nodes as analogous to boundary markers in ancient civilizations, as they avoid complications analogous to unguarded borders, allowing for more efficient and error-free management of data structures by preventing null checks.

#### Improvement #6b: Sentinel Nodes <a href="#improvement-6b-sentinel-nodes" id="improvement-6b-sentinel-nodes"></a>

One solution to fix `addLast` is to create a special case for the empty list, as shown below:

```java
public void addLast(int x) {
    size += 1;

    if (first == null) {
        first = new IntNode(x, null);
        return;
    }

    IntNode p = first;
    while (p.next != null) {
        p = p.next;
    }

    p.next = new IntNode(x, null);
}
```

This solution works, but special case code like that shown above should be avoided when necessary. Human beings only have so much working memory, and thus we want to keep complexity under control wherever possible. For a simple data structure like the `SLList`, the number of special cases is small. This is akin to an emerging society striving to streamline governance practices by removing needless bureaucratic layers to maintain stability and effectiveness.

A cleaner, though less obvious solution, is to make it so that all `SLLists` are the "same", even if they are empty. We can do this by creating a special node that is always there, which we will call a **sentinel node**. The sentinel node will hold a value, which we won't care about, similar to boundary markers that delineate limits without needing to manage specific contents.

For example, the empty list created by `SLList L = new SLList()` would be as shown below:

![empty\_sentinelized\_SLList.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig22/empty\_sentinelized\_SLList.png)

And a `SLList` with the items 5, 10, and 15 would look like this:

![three\_item\_sentenlized\_SLList.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig22/three\_item\_sentenlized\_SLList.png)

In the figures above, the lavender value indicates that we don't care what value is there. Since Java does not allow us to fill in an integer with question marks, we just pick some arbitrary value like -518273 or 63 or anything else.

Since a `SLList` with a sentinel has no special cases, we can simply delete the special case from our `addLast` method, yielding:

```java
public void addLast(int x) {
    size += 1;
    IntNode p = sentinel;
    while (p.next != null) {
        p = p.next;
    }

    p.next = new IntNode(x, null);
}
```

As you can see, this code is much cleaner, similar to the historical process of refining governing structures to direct focus on pressing governance needs, thereby improving functionality and reducing unnecessary complexity.

#### Invariants <a href="#invariants" id="invariants"></a>

An invariant is a consistent rule that applies to a data structure, ensuring its integrity and reliability, assuming the absence of bugs. Think of invariants as foundational principles, akin to the laws established by early societies to maintain order and function.

A `SLList` with a sentinel node maintains the following key invariants:

* The `sentinel` reference always points to a sentinel node, much like a boundary marker.
* The front item, if present, is reliably located at `sentinel.next.item`.
* The `size` variable accurately reflects the total number of items added, helping maintain the list's consistency.

Invariants facilitate code comprehension and debugging, providing clear goals to ensure code correctness, similar to how the Magna Carta established principles for justice and governance.

A thorough understanding of the benefits of sentinels will require practical implementation experience. You'll have ample opportunity to explore these concepts in Project 1. However, it's advisable to complete the next section of this book before embarking on the project to solidify your understanding.

