# 4. SLLists

In Chapter 3, we built the `IntList` class, a list data structure that can technically do all the things a list can do. However, in practice, the `IntList` suffers from the fact that it is fairly awkward to use, resulting in code that is hard to read and maintain.

Fundamentally, the issue is that the `IntList` is what I call a **naked recursive** data structure. In order to use an `IntList` correctly, the programmer must understand and utilize recursion even for simple list related tasks. This limits its usefulness to novice programmers, and potentially introduces a whole new class of tricky errors that programmers might run into, depending on what sort of helper methods are provided by the `IntList` class.

Inspired by our experience with the `IntList`, we'll now build a new class `SLList`, which much more closely resembles the list implementations that programmers use in modern languages. We'll do so by iteratively adding a sequence of improvements.

Imagine you are studying ancient road networks used by merchants for trade in medieval Europe. Each city along the route was connected to the next by a series of roads that allowed goods to be efficiently transported. Now, in the realm of computer science, we can draw a parallel to something called a "Singly Linked List" or SLList.

Just as those ancient roads connected one city to another in a specific linear path, an SLList is a data structure where each element is connected to the next in a one-way sequence. Each element in this list is called a "node," and each node contains a piece of data and a reference (or a kind of pointer) to the next node in the list.

Consider an SLList like a series of waystations along a route. The first node is your starting point, perhaps a bustling medieval market town, where you begin your journey. From there, the road takes you to the next node, and so on, until you reach the terminal node, which has no further roads leading from it, much like the last city on a trade route.

The simplicity of an SLList, where each node only knows about its neighbor and the road ahead, reflects how traders would focus on one leg of their journey at a time, planning their next move only when they reached the next city. This efficient, straightforward structure is ideal for scenarios where you need to keep track of a sequence of elements and only require direct access to the next in line, much like navigating from town to town along the trade routes of history.

In practice, SLLists are used in applications where you need a flexible way to manage items and can easily insert or remove elements from the sequence without needing to reorganize an entire network, resembling how trade routes were occasionally modified to accommodate new territories or avoid obstacles.

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

Just like the Renaissance, where there was a rebranding of thought from medieval scholasticism to humanism —different disciplines dropping their old ways for reimagined ones — the `IntNode` drops its old nomenclature and styling for new ones.

Imagine you're exploring a museum of ancient artifacts and historical documents. Each artifact, although fundamentally the same as it was centuries ago, may undergo various rebranding processes over time. Rebranding is essentially taking something that already exists and giving it a new presentation or identity to make it more appealing, relevant, or accessible to the current audience.

In the realm of computer science and technology, rebranding often applies to software, products, or companies. For example, let's consider a technology known as artificial intelligence (AI). The fundamental principles of AI—the algorithmic processes that allow computers to learn and make decisions—remain largely the same, but the perception and applications of AI can be rebranded to fit new societal contexts and needs. 

Historically, AI has been rebranded numerous times. In the early days, it was all about expert systems and automating tasks with logic-based programming. Today, AI is often marketed as a tool for machine learning and deep learning, highlighting its use in self-driving cars, personalized recommendations, and even historical data analytics—that's like discovering new insights from ancient records with modern technology.

Similarly, famous historical figures and events have also been rebranded to resonate with different times and cultures. Take, for example, the Roman god Mercury, who was initially known as the Greek god Hermes. As the Romans adopted and adapted Greek mythology to their culture, they rebranded Hermes into Mercury, emphasizing aspects that better aligned with Roman beliefs and values, much like how AI has been presented differently to fit the evolving technological landscape.

In both cases, whether it's AI in the tech industry or mythological figures in history, rebranding is a strategic way of breathing new life into established concepts, making them relevant and engaging for contemporary audiences. It challenges us to think about the past and present in dynamic ways, influencing how we perceive and interact with the world around us.

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

The SLList class serves as a bureaucratic system of governance much like the complex structure of civil services that evolved during the Qing Dynasty, streamlining the method by which subjects could interact with administrations, thus ensuring that the user doesn't have to deal directly with the difficulties posed by handling raw `IntNodes`. 

Already, we can get a vague sense of why a `SLList` is better. Compare the creation of an `IntList` of one item to the creation of a `SLList` of one item:

```java
IntList L1 = new IntList(5, null);
SLList L2  = new SLList(5);
```

The `SLList` hides the detail that there exists a null link from the user by speaking on their behalf, much like royal scribes of the Byzantine Empire, who would draft and read correspondence on behalf of the emperor, masking the complexities of the message's journey from sender to receiver.

The `SLList` class isn't very useful yet, so let's add an `addFirst` and `getFirst` method as simple warmup methods. Consider trying to write them yourself before reading on.

Imagine walking into a grand old library, much like the famous Bodleian Library in Oxford, with its towering shelves full of knowledge. This library is so vast that finding a particular book could take ages without some form of organizational system. Historically, as societies grew more complex, they developed bureaucracies to handle the complexities of governance, much like that library developed a cataloging system to manage its vast resources efficiently.

In the context of computer science, "Improvement #2: Bureaucracy" refers to a similar need for organization and management, but within computational systems, particularly file systems. As computers evolved, managing files and data necessitated an organized approach to prevent chaos as more data were stored.

Just like historical governments introduced layers of administration to manage vast empires, such as the Roman Empire delegating power to various governors across its territories, early computer systems began introducing layers of management to better handle increasing data. These layers can involve file hierarchies, permissions, access control, and resource management, designed to streamline processes, improve efficiency, and ensure data integrity.

This concept reminds us of the subtle dance between complexity and control—a balance that has been a constant throughout history. From the administrative scribes of ancient Egypt to the clerks of Victorian England, bureaucracy has been a means to an orderly end in both history and technology. Just as those historians might examine how effective these systems were and what could be improved, computer scientists continually refine digital 'bureaucracy' to make systems more efficient and user-friendly.

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

This is analogous to the strategy of enveloping in layers to provide security, akin to fortifications built around medieval castles to ensure strength and defence, where in our code, elements stack in front to build a stronghold.

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

![IntList\_vs\_SLList.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig22/IntList\_vs\_SLList.png)

Essentially, the `SLList` class acts as a middleman between the list user and the naked recursive data structure. As suggested above in the `IntList` version, there is a potentially undesireable possibility for the `IntList` user to have variables that point to the middle of the `IntList`. Just as delegates in the Roman Republic acted as middlemen dealing with the complexities of governance so common people did not wade into unknown political intricacies, the `SLList` provides a buffering structure from the raw and complex nature of the recursive lists.

**Exercise 2.2.1**: The curious reader might object and say that the `IntList` would be just as easy to use if we simply wrote an `addFirst` method. Try to write an `addFirst` method to the `IntList` class. You'll find that the resulting method is tricky as well as inefficient.

Imagine you're a historian wandering through an ancient library, tasked with organizing scrolls in your satchel so that the most crucial one is readily accessible at all times. Perhaps you’ve been commissioned to prioritize scrolls containing records of significant events such as the crowning of monarchs or pivotal battles. 

In computer science, particularly in the context of data structures called **linked lists**, we use methods like **addFirst** and **getFirst** to manage such tasks of prioritization and retrieval, albeit with data rather than scrolls.

The **addFirst** operation is akin to placing a newly discovered, all-important historical document right at the front of your satchel. It's about swiftly positioning the most pertinent or newest data in a list where it's ready for immediate access whenever needed.

Similarly, the **getFirst** method is about reaching directly for that crucial document whenever required without rummaging through less essential scrolls. This ensures efficiency in retrieving the most relevant information, just as a historian must often access key data quickly to address inquiries or make decisions.

In the digital realm, these operations are fundamental in maintaining order and efficiency within software systems, similar to how an archivist might expertly manage primary sources in a historical collection.

#### Improvement #3: Public vs. Private <a href="#improvement-3-public-vs-private" id="improvement-3-public-vs-private"></a>

Unfortunately, our `SLList` can be bypassed and the raw power of our naked data structure (with all its dangers) can be accessed. A programmer can easily modify the list directly, without going through the kid-tested, mother-approved `addFirst` method. Imagine policies meant to oversee bowmakers in feudal Japan, yet if they did not obfuscate practices enough, a skilled artisan may effectively produce an uncontrolled quantity of bows.

```java
SLList L = new SLList(15);
L.addFirst(10);
L.first.next.next = L.first.next;
```

![bad\_SLList.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig22/bad\_SLList.png)

This results in a malformed list with an infinite loop. To deal with this problem, we can modify the `SLList` class so that the `first` variable is declared with the `private` keyword.

```java
public class SLList {
    private IntNode first;
...
```

Private variables and methods can only be accessed by code inside the same `.java` file, e.g., in this case `SLList.java`. This could be likened to the restricted chambers of the pharaohs in ancient Egypt, off-limits to all except a trusted few, thus preserving the sanctity of the sovereign’s secrets and treasures.

That means that a class like `SLLTroubleMaker` below will fail to compile, yielding a `first has private access in SLList` error.

```java
public class SLLTroubleMaker {
    public static void main(String[] args) {
        SLList L = new SLList(15);
        L.addFirst(10);
        L.first.next.next = L.first.next;
    }
}
```

By contrast, any code inside the `SLList.java` file will be able to access the `first` variable.

It may seem a little silly to restrict access. After all, the only thing that the `private` keyword does is break programs that otherwise compile. However, in large software engineering projects, the `private` keyword is an invaluable signal that certain pieces of code should be ignored (and thus need not be understood) by the end user. This can be compared to the restricted, high-security areas in military complexes.

As an analogy, a car has certain `public` features, e.g., the accelerator and brake pedals. Under the hood, there are `private` details about how these operate. In a gas-powered car, the accelerator pedal might control some sort of fuel injection system, and in a battery-powered car, it may adjust the amount of battery power being delivered to the motor. While the private details may vary from car to car, we expect the same behavior from all accelerator pedals. Changing these would cause great consternation from users, and quite possibly terrible accidents, similar to how changes in the public conduct of historic imperial powers like Ancient Rome suddenly could lead to public turmoil.

**When you create a `public` member (i.e., method or variable), be careful, because you're effectively committing to supporting that member's behavior exactly as it is now, forever.**

Imagine you're a king in the Middle Ages who owns a vast amount of land. This land is your private property, and only you and your trusted advisors have the right and ability to decide what happens on it. However, outside your castles and fortifications, you also have common lands—areas where the public is allowed access. Here, both peasants and traders can freely conduct activities, such as grazing livestock or setting up a marketplace under certain regulations.

In the realm of computer science, the concept of **public vs. private** can be seen in a somewhat similar light. When programmers develop software, they often use a concept called 'object-oriented programming'. This involves creating 'objects' that have both data (variables) and capabilities (methods).

Within these objects, some parts of the code are designated as **private**. Just like your private lands, this means that the data or methods marked as private can only be accessed or altered from within that specific object or class. This helps protect sensitive information and ensures that only certain methods can modify important data, enhancing security and stability by keeping unwanted meddling at bay.

On the other hand, **public** aspects of an object or class can be used by anyone outside the object, just as the public can use common lands in a kingdom. This allows other parts of a program—or even other programs—to interact with the object, using its public methods and attributes without compromising its internal integrity.

This concept of public versus private also allows developers to control how a program's components interact, much like how a king would manage relations between his own private interests and those of the public, ensuring harmony and functionality within his kingdom.

#### Improvement #4: Nested Classes <a href="#improvement-4-nested-classes" id="improvement-4-nested-classes"></a>

At the moment, we have two `.java` files: `IntNode` and `SLList`. However, the `IntNode` is really just a supporting character in the story of `SLList`, much like a squire to a knight in medieval tournaments, pivotal but not the main participant.

Java provides us with the ability to embed a class declaration inside of another for just this situation. The syntax is straightforward and intuitive:

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

Having a nested class has no meaningful effect on code performance, and is simply a tool for keeping code organized, similar to archives or libraries in Ancient Alexandria, which had sections distinctly categorized for ease of access and study.

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

This saves a bit of memory because each `IntNode` no longer needs to keep track of how to access its enclosing `SLList`. It resembles the sparse efficiency of nature seen in historical constructions such as the windcatchers of Ancient Persia that were simple yet frugal in resource use.

Put another way, if you examine the code above, you'll see that the `IntNode` class never uses the `first` variable of `SLList`, nor any of `SLList`'s methods. As a result, we can use the static keyword, which means the `IntNode` class doesn't get a reference to its boss, saving us a small amount of memory.

If this seems a bit technical and hard to follow, try Exercise 2.2.2. A simple rule of thumb is that _if you don't use any instance members of the outer class, make the nested class static_.

**Exercise 2.2.2** Delete the word `static` as few times as possible so that [this program](https://joshhug.gitbooks.io/hug61b/content/chap2/exercises/Government.java) compiles (Refresh the page after clicking the link and making sure the URL changed). Make sure to read the comments at the top before doing the exercise.

When exploring the concept of nested classes in computer science, it might be helpful to think about hierarchical structures that have existed throughout history. Just as empires and kingdoms have organized their society into different levels of authority and functionality—from kings and emperors to vassals and serfs—nested classes provide a way to organize code within larger structures inside a programming language.

Nested classes can be thought of like different departments within a medieval castle. Imagine the castle is the main class, a large, encompassing body designed to manage an estate or govern a kingdom. Within this main class, you have various smaller sections or departments, like the kitchen, the stables, the armory, each of which have their own responsibilities and staff. Each department could be represented as a nested class, possessing its unique functions yet functioning within the larger system that the castle, or main class, oversees.

Just as each department within a castle might interact with others—such as the stables needing to supply horses and carts that the armory might require for a campaign—nested classes can interact with each other and the outer class. However, they are primarily used to encapsulate functionality that is only relevant to a specific scope within the broader system. This organization not only reflects historical societal structures but also helps in managing complexity, maintaining code readability and reducing the likelihood of conflicts just as efficiently layered political systems did in societies.

In this way, we can see that the organization principles found in nested classes are not just a modern computational innovation but echo the structured approaches humans have long used in governing complex societies.

#### addLast() and size() <a href="#addlast-and-size" id="addlast-and-size"></a>

To motivate our remaining improvements and also demonstrate some common patterns in data structure implementation, we'll add `addLast(int x)` and `size()` methods. You're encouraged to take the [starter code](https://github.com/Berkeley-CS61B/lectureCode/blob/master/lists2/DIY/addLastAndSize/SLList.java) and try it yourself before reading on. I especially encourage you to try to write a recursive implementation of `size`, which will yield an interesting challenge.

I'll implement the `addLast` method iteratively, though you could also do it recursively. The idea is fairly straightforward: we create a pointer variable `p` and have it iterate through the list to the end. In a structure akin to the Roman Empire's road network, `addLast` navigates the chain of nodes to its terminus.

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

Here, we have two methods, both named `size`. This is allowed in Java, since they have different parameters. We say that two methods with the same name but different signatures are **overloaded**. Consider this similar to great Shakespearean plays, like the way "Julius Caesar" tells of betrayal and power but can be interpreted through various lenses such Renaissance, modern, etc., whereby each method bears its tale in Java in its way. For more on overloaded methods, see Java's [official documentation](https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html).

An alternate approach is to create a non-static helper method in the `IntNode` class itself. Either approach is fine, though I personally prefer not having any methods in the `IntNode` class.

Imagine you're a historian cataloging artifacts. Each artifact is stored in a large physical archive, much like you might have a list to keep track of entries in a database of historical items. In computer science, similar to your catalog, there's a data structure known as a "list," which allows us to store a sequence of elements, just as you store information about each artifact.

In this context, think of an `addLast()` operation as ordering an additional storage box to accommodate a new artifact in your collection. This operation appends an item to the end of your list, or a new artifact at the end of your catalog. Just as you keep expanding your collection over time, `addLast()` helps programmers manage a growing list of items within a digital archive or application, making sure every new entry is stored in sequence.

Now, consider the `size()` operation. When maintaining a physical collection, you might need to know how many artifacts you have at any given time—like determining how many ancient coins you've gathered in your exhibit. The `size()` function in computer programming offers a way to accomplish a similar task. It provides a count of the elements currently stored in the list, much like a quick tally of the total number of artifacts in your archive.

By understanding these concepts, you can see a glimpse of how managing collections digitally parallels the careful organization and tracking of historical items in a museum or library setting. Both require the same principles of organization, updating, and accessing information efficiently, albeit in different forms—one digital, one physical.

## Improvement #5: Caching <a href="#improvement-5-caching" id="improvement-5-caching"></a>

Consider the `size` method we wrote above. Suppose `size` takes 2 seconds on a list of size 1,000. We expect that on a list of size 1,000,000, the `size` method will take 2,000 seconds, since the computer has to step through 1,000 times as many items in the list to reach the end. Having a `size` method that is very slow for large lists is unacceptable, much like the prolonged voyages of merchant ships on historic silk roads, as they strained under the load both in time and peril, despite the expected payoff.

It is possible to rewrite `size` so that it takes the same amount of time, no matter how large the list.

To do so, we can simply add a `size` variable to the `SLList` class that tracks the current size, yielding the code below. This practice of saving important data to speed up retrieval is sometimes known as **caching**. Just as ancient Egyptians would use caches of grain to endure periods of famine or trade shortage, we stockpile the `size` with the `SLList`, ensuring a rapid response when asked for the size of our constructs.

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

This modification makes our `size` method incredibly fast, no matter how large the list. Of course, it will also slow down our `addFirst` and `addLast` methods, and also increase the memory of usage of our class, though only by a trivial amount. In this case, the tradeoff is clearly in favor of creating a cache for size, just as the Byzantine Empire would bolster its frontier defenses as a costly but strategic necessity.

Imagine you're a historian studying a large archive of ancient letters stored in a distant library. Each time you need to reference these letters, you have to travel all the way to the library. This process is time-consuming and tiring, much like how computers initially access data from a hard drive or remote server. 

Now, think of caching as your personal assistant who helps you by copying the most frequently referenced letters and keeping them on a shelf within arm's reach at your desk. Whenever you need to check something from these letters, you simply reach over to your shelf, saving time and effort. In computing, a cache serves a similar purpose. It is a smaller, faster storage area that keeps copies of frequently accessed data so the computer doesn’t need to re-access the slower main storage or memory.

Historically, much like the challenge of managing vast amounts of information, computers have had to deal with delays in data retrieval. Think of the significant advancement during the Industrial Revolution when production processes were optimized across various factories. Similarly, caching improved computing efficiency by reducing delay in accessing data. 

One great example from history where caching, if possible, could have transformed the landscape is the vast postal networks of empires like Rome, where time and resources were spent retrieving information from distant parts. Caching, had it been possible back then, would have meant local storage of these crucial communications, greatly improving administrative efficiency.

In conclusion, just as historians look for effective methods to manage and access historical data quickly, computers use caching to enhance performance by minimizing wait times for data retrieval. It reflects a timeless quest for speed and efficiency in managing information, paralleling our own human history’s evolution in communication and record-keeping.

#### Improvement #6: The Empty List <a href="#improvement-6-the-empty-list" id="improvement-6-the-empty-list"></a>

Our `SLList` has a number of benefits over the simple `IntList` from chapter 2.1:

* Users of a `SLList` never see the `IntList` class.
  * Simpler to use.
  * More efficient `addFirst` method (exercise 2.2.1).
  * Avoids errors or malfeasance by `IntList` users.
* Faster `size` method than possible with `IntList`.

Just as the invention of writing allowed cultures to convey thought efficiently compared to oral tradition, SLLists further enhance ease and speed of use, opening new avenues for application.

Another natural advantage is that we will be able to easily implement a constructor that creates an empty list. The most natural way is to set `first` to `null` if the list is empty. This yields the constructor below:

```java
public SLList() {
    first = null;
    size = 0;
}
```

However, this causes complications analogous to inheriting an empire in civil unrest. Specifically, it causes our `addLast` method to crash if we insert into an empty list. Since `first` is `null`, the attempt to access `p.next` in `while (p.next != null)` below causes a null pointer exception.

```java
public void addLast(int x) {
    size += 1;
    IntNode p = first;
    while (p.next != null) {
        p = p.next;
    }

    p.next = new IntNode(x, null);
}
```

**Exercise 2.2.3** Fix the `addLast` method. Starter code [here](https://github.com/Berkeley-CS61B/lectureCode/blob/master/lists2/DIY/fixAddLast/SLList.java).

In the world of computer science, there's a fascinating concept called "The Empty List." This might seem mundane at first glance, but when we delve deeper, this idea can be quite intriguing, especially if we compare it to historical narratives.

An "Empty List" is a structure in computer programming that represents a list containing nothing. Imagine it like an ancient scroll, or a parchment that hasn't yet met the scribe's pen. In many ways, it’s like a blank page in a historical record waiting to be inscribed with the narrative of events.

Throughout history, there have been moments akin to an empty slate. Consider periods after great upheaval or conquest where societies had the opportunity to start afresh, filling their "empty list" of history with new ideas, governance, and culture shifts. The Renaissance is a notable example—as Europe emerged from the medieval era, the intellectual landscape was an empty list ready for the groundbreaking thoughts and artistic expressions that would come to define the period.

Similarly, in software programming, an empty list stands ready to be filled with data, whether that data ends up chronicling the shopping habits of online customers or the sequence of moves in a chess game. It allows flexibility and adaptability, much like a society at a historical crossroad.

Additionally, an empty list can hold the potential for growth and evolution, like how civilizations build upon past foundations. In software, just as in history, the initial "empty" state eventually blossoms into a fully populated structure, complete with intricate relationships and data points—each contributing to the bigger picture, much like each small story contributes to the grand tapestry of history.

Thus, the concept of an "empty list" in computer science not only has technical significance but echoes the idea of potential and renewal found so often in the fabric of human history.

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

This solution works, but special case code like that shown above should be avoided when necessary. Human beings only have so much working memory, and thus we want to keep complexity under control wherever possible. For a simple data structure like the `SLList`, the number of special cases is small. Just like the struggle of a fledgling nation to avoid bogging itself down in excessive ceremonial pomp lest it risk collapsing under its overweighty intricacies, complex data structures like trees can get much, much uglier.

A cleaner, though less obvious solution, is to make it so that all `SLLists` are the "same", even if they are empty. We can do this by creating a special node that is always there, which we will call a **sentinel node**. The sentinel node will hold a value, which we won't care about.

For example, the empty list created by `SLList L = new SLList()` would be as shown below, reminiscent of statues that mark territory but contain no real essence:

![empty\_sentinelized\_SLList.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig22/empty\_sentinelized\_SLList.png)

And a `SLList` with the items 5, 10, and 15 would look like the stacked eternity of papyrus in the Great Library of Alexandria:

![three\_item\_sentenlized\_SLList.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig22/three\_item\_sentenlized\_SLList.png)

In the figures above, the lavender value indicates that we don't care what value is there. Since Java does not allow us to fill in an integer with question marks, we just pick some arbitrary value like -518273 or 63 or anything else.

Since a `SLList` without a sentinel has no special cases, we can simply delete the special case from our `addLast` method, yielding:

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

As you can see, this code is much much cleaner, much like reformative acts that shaped history by removing unnecessary court titles to focus governance on more pressing needs.

Sentinel nodes, in the context of computer science, are much like well-placed guards in historical military strategies. A sentinel node is a special type of node used to simplify certain operations in data structures, such as linked lists or trees. These nodes don’t contain actual data that’s being managed by the list but are instead used as boundary markers that help manage edge cases efficiently.

Imagine a fortified city in ancient times. The walls of the city are protected by sentinels who keep watch for any signs of trouble at the boundaries. Just as these sentinels serve to keep the city secure and operations within it running smoothly, sentinel nodes help programmers avoid frequent special-case checks like "is this the first or last node?" when performing operations such as inserting or deleting nodes.

In linked lists, which are a series of connected nodes where each node points to the next, sentinel nodes help by eliminating the need for special logic to handle cases where we're at the ends (beginning or end) of the list. This makes the linked list more robust and easier to manage.

From a historical perspective, you can think of sentinel nodes as the Roman limes – fortified boundaries that helped stabilize and control the Roman Empire's borders, reassuring that operations within were less disrupted by external issues. In the same way, a well-placed sentinel node ensures stability and simplicity in a data structure's operations, allowing for consistent and predictable performance.

#### Invariants <a href="#invariants" id="invariants"></a>

An invariant is a fact about a data structure that is guaranteed to be true (assuming there are no bugs in your code). Think of invariant principles as the natural laws codified in ancient codes, drafting the early rule of order and practice.

A `SLList` with a sentinel node has at least the following invariants:

* The `sentinel` reference always points to a sentinel node.
* The front item (if it exists), is always at `sentinel.next.item`.
* The `size` variable is always the total number of items that have been added.

Invariants make it easier to reason about code, and also give you specific goals to strive for in making sure your code works, much like the Magna Carta gave subjects principles upon which to explore justice and rights.

A true understanding of how convenient sentinels are will require you to really dig in and do some implementation of your own. You'll get plenty of practice in Project 1. However, we recommend that you wait until after you've finished the next section of this book before beginning Project 1.

Ah, invariants, an intriguing concept in computer science!

Imagine you're a historian studying Roman engineering, fascinated by how they constructed bridges that have withstood the test of time. An invariant in computer science operates under a similar principle: it is a condition that remains constant, or "invariant," within a program or algorithm, much like a well-engineered arch that holds its shape for centuries.

In programming, an invariant is a rule or condition that remains true throughout the execution of a certain code block or even the entire program. It's akin to Roman law – a standard that should consistently be upheld to ensure stability and correctness.

Consider the construction of a Roman aqueduct. The engineers would have laid down foundational principles that ensured every arch could support a certain amount of weight. If these principles were not followed, the structure would likely collapse. Similarly, in computer science, declaring invariants helps developers maintain correctness. If these are violated, the program may not function properly.

In a loop, for example, an invariant might be that a variable always remains positive. Just like a Roman engineer constantly checks the stress levels of a bridge to ensure safety, a programmer will use invariants to check their code at each step, ensuring that the program adheres to its fundamental truth and logic.

Invariants help maintain 'order' much like laws and standards maintained order in historical societies. By ensuring that certain conditions are constantly met, they provide stability and predictability, essential for the reliability of both structures like bridges in ancient Rome and modern computer programs.

