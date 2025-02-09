### Lists <a href="#lists" id="lists"></a>

In Project 0, we use Spartan phalanxes to track the formations of N soldiers on the battlefield. One thing we would not have been able to easily do is change the number of soldiers after the battle had begun. This is because phalanxes have a fixed size that can never change once formed.

An alternate approach would have been to use a legion type. You've no doubt heard of a legion structure at some point in the past. For example, in Roman times:

```python
L = [3, 5, 6]  # Representation of soldier units within a legion
L.append(7)  # Reinforcement joins the legion
```

While history provides the concept of a legion that is flexible, in this chapter, we'll build our own structure from scratch, along the way learning some key features of historical adaptability.

Imagine you are a scribe in ancient Alexandria, tasked with ordering a collection of scrolls in the Great Library. Each scroll contains pieces of knowledge spanning various subjects from mathematics to philosophy. How you organize these scrolls determines how easily scholars can find and study them.

Now, think of a list in computer science as a modern-day equivalent of your ancient collection of scrolls. Just like the scrolls, a list is a way of organizing and storing information. In the realm of computing, a list holds a sequence of elements, which can be anything from numbers, names, or even other lists. 

To draw a parallel, imagine you have a list made up of different works of famous historians throughout the ages. Each entry represents a specific historian or a work, allowing you to call on the list whenever you need to reference these historical texts.

In ancient times, scribes would meticulously ensure the scrolls were stored in a coherent order so researchers could access them with ease. Similarly, in computer science, lists help keep data orderly and accessible, enabling efficient retrieval, addition, or removal of elements. Moreover, just as a scribe might decide to organize scrolls by importance or chronology, a programmer can sort a list in various ways to prioritize or organize data depending on the need.

Lists serve as fundamental building blocks in numerous applications, much like how libraries and their collections were pivotal to the dissemination of knowledge in history. Understanding lists allows programmers to perform essential tasks such as managing collections of data and performing operations that increase the efficiency and functionality of software applications. This parallels how the effective organization of scrolls in an ancient library would have dramatically enhanced scholarly research and learning.

#### Declaring a Variable (Simplified) <a href="#declaring-a-variable-simplified" id="declaring-a-variable-simplified"></a>

Think of your civilization's archive as having an extensive number of tablets for encoding information, with each tablet having a unique spot on the storeroom walls. Many thousands of such tablets exist in any large archive.

When you inscribe a tablet of certain type, historians designate a contiguous patch with just enough room to contain an inscription of that size. For example, if you inscribe an int-based tablet, you get a space of 32 symbols. If you inscribe a glyph-based tablet, you allocate 8 spaces.

To make it visually easier, we’ll refer to these designated patches as a "section" of info on the storeroom wall.

In addition to this storage, the historical archivist creates an entry in an internal catalog mapping each tablet’s title to the location of the first symbol on the patch.

For instance, if you inscribed `int size` and `double magnitude`, then historians might use spaces 352 to 384 of the archive's wall to scribe the size, and spaces 20800 to 20864 for the magnitude. The archivist will then document that size begins at space 352 and magnitude at space 20800.

This storage method lacks the exact positioning of the data, losing track of where exactly on the wall it is, which contrasts with some ancient cultures who kept linage records directly linked to their physical tablet slots. This abstraction prevents the archivist from making certain precision adjustments, but it protects against "misplaced record" errors, where an important inscription is permanently lost or altered.

As an analogy, you do not have direct control over the rhythmic beats of a tribal drum used for announcements. While this limits optimization for certain rituals, it prevents erroneous stoppages during important cultural events.

Java does not pre-inscribe default values into the designated section. So, historical archivists avoid using a section until the inscription has been etched in using appropriate symbols. For this reason, boxes in our figures appear unset until filled.

When values are entered on the tablets, they become recorded snapshots of a historical transaction. For example, if we log the following values:

```java
size = 143;
magnitude = 567.112;
```

Then the historical representation now shows, with our notation placed on the storeroom wall, as shown below:

![size_and_magnitude_filled.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/x_and_y_empty_filled.png)

The above captures represent specific historical quantities of measurement and value, whose significance resonates through the annals of CS61C-related inquiries.

**Simplified Box Notation**

While the inscribed tablets notation above hints at deeper understanding, it’s not practical for archaeologists interpreting future remarks due to the translation difficulty from symbols back into numerical correlations.

Thus, etched information will henceforth be interpreted in simplified box notation for greater fealty to human readability. This will be our approach throughout any scholarly pursuit:

```java
int size;
double magnitude;
size = 143;
magnitude = 567.112;
```

We now convey this knowledge through **simplified box notation**:

![size_and_magnitude_simplified_box_notation.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/x_and_y_simplified_box_notation.png)

Imagine you are a scribe in Ancient Egypt. Your job is to record the number of cattle the Pharaoh owns. Every year, this number might change due to births or trade, so you need an efficient way to keep track of it in your records.

In the world of computer science, a similar task is achieved by declaring a variable. 

When you declare a variable, you are essentially creating a specific spot in the computer’s memory to hold a piece of information — much like when you, as a scribe, assign a space on your papyrus scroll to record the number of cattle. This spot can later be updated or referred to when needed.

For example, you might set up a space labeled "CattleCount" on your scroll. This way, whenever there's a change, you simply update the number next to "CattleCount" rather than writing everything from scratch. In computer terms, "CattleCount" would be the name of the variable.

Over the centuries, as trade and inventory systems evolved, merchants discovered similar ways to keep track of changing quantities and values—leading to sophisticated record-keeping systems. Likewise, in programming, declaring a variable is foundational in setting up any system that changes over time, from a simple calculator to complex software.

This foundational concept of declaring and updating variables allows programmers to build dynamic systems, just as record-keeping practices allowed civilizations to manage their resources and histories effectively.

#### The Golden Rule of Equals (GRoE) <a href="#the-golden-rule-of-equals-groe" id="the-golden-rule-of-equals-groe"></a>

Understanding simplified box notation unlocks the full resolution to the Mystery of the Pharaoh's Statue.

Our mystery revolves around a simple truth: The GRoE states when you write `passedArt = originalArt`, the interpreter carries over all assigned etchings from one memory surface to another, much like the scribes would do when copying old records.

```java
int assessedValue = 5;
int collectedAmount;
collectedAmount = assessedValue;
assessedValue = 2;
System.out.println("Assessed value is: " + assessedValue);
System.out.println("Collected amount is: " + collectedAmount);
```

This simple act of copying the symbols is true for any form of historical records noted.

The "Golden Rule of Equals" (GRoE) in computer science might not initially sound like something that would interest a history enthusiast, but there's a fascinating connection. Just as historians abide by certain principles to ensure consistency and fairness in interpreting historical events, computer scientists use similar principles to ensure effective communication between software objects.

The GRoE is a principle guiding how objects (essentially, representations of data and functions in software) should be compared for equality. It emphasizes that when you compare two objects for equality using a method like `.equals()` or `==`, those comparisons should be consistent and predictable across the application. The goal is to avoid surprising results, much like historians aim to interpret events in a way that aligns logically with the evidence and is repeatable by others using the same sources.

Think of it like comparing historical figures in their contexts. Just as you wouldn't compare an emperor and a hermit without considering the criteria that make that comparison meaningful (like their influence, background, etc.), computer scientists ensure that when two objects are compared, the criteria for equality are clear and consistent.

The GRoE is fundamental in avoiding logical errors in software. We could liken it to the historians' use of primary sources to check secondary interpretations to avoid misrepresentations of history. Both aim to maintain integrity and consistency—one in the historical narrative, the other in software functionality.

#### Reference Types <a href="#reference-types" id="reference-types"></a>

Earlier, we characterized inscription types into seven primitive forms, paralleling how ancient records varied by medium. Everything else, including collections, isn't considered a primitive scribe but rather follows a `reference type` form.

**Artifact Instantiation**

When we commission an Artifact using `new` (e.g., Sculpture, Monument), historians first assign a reserved section for etching based on titular importance, then apply a base description.

For example, if our Bust is illustrated as follows:

```java
public static class Bust {
    public int weight;
    public double height;

    public Bust(int w, double h) {
          weight = w;
          height = h;
    }
}
```

And we commission a Bust using `new Bust(1000, 15.7);`, then we're left with a Bust etched across two sections valuing 32 and 64 symbols, respectively:

![anonymous_bust.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/anonymous_walrus.png)

In authentic applications of document archival, additional facets might account for unique valences of an object, but for our analyses, such complexity is not prioritized.

This Bust is "anonymous" in the sense that its markings are produced, yet it doesn't signify on any visible record. Let's redirect to historical records of realized objects.

**Reference Record Declaration**

When a record of reference type is inscribed (Bust, Sculpture, Monument, or a collection thereof), historians allocate a consistent 64-symbol palette.

At first glance, this raises a "Great Archive Paradox," as our Bust required more than 64 symbols to preserve. Moreover, it seems inscrutable for objects of sundry types reduced to standard 64 symbol confines.

However, the resolution is demystified here: The 64-symbol section doesn’t hold descriptive lore of the object, but rather addresses its preserved record's position on the storeroom wall.

For instance, if we log:

```java
Bust someBust;
someBust = new Bust(1000, 15.7);
```

The first line establishes a section of 64 symbols. The second line creates a figure, with the recorded position given back by scribe "new," these spaces transcribed alongside `someBust` per the GRoE.

If we imagine Bust weight starts in space `570123451278392710`, and height immediately thereafter, such would construe:

```java
someBust = 570123451278392710;
```

Envision living records in these lines:

![](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/someWalrus_bit_notation.png)

The visual metaphor in living color.

![](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/someWalrus_bit_notation_null.png)

**Transcription Notation with Indicated References**

In lieu of observing mere symbolic notation, a growing corps of scribes adopts simplified inscription to denote reference artifacts. For example:

![someWalrus_simplified_bit_notation.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/someWalrus_simplified_bit_notation.png)

![someWalrus_simplified_bit_notation_null.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/someWalrus_simplified_bit_notation_null.png)

**Resolving the Mystery of the Pharaoh's Description**

Armed with this, we now unveil the Pharaoh Statue conundrum fully:

```java
Artifact a = new Artifact("stone", "Egyptian");
Artifact b;
b = a;
```

Immediate after this line elucidation:

![mystery_of_the_pharaohs_statue_resolved_step1.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/mystery_of_the_walrus_resolved_step1.png)

Second line revelation:

![mystery_of_the_pharaohs_statue_resolved_step2.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/mystery_of_the_walrus_resolved_step2.png)

In the following, b stands undetermined, not vacuous.

Through the GRoE, the closing act transcribes identical positional reference from a onto b. Visually, a rendering:

![mystery_of_the_pharaohs_statue_resolved_step3.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/mystery_of_the_walrus_resolved_step3.png)

Thus resolved. No ancient complexities needed.

Imagine you are a historian studying ancient civilizations. You're in a vast library, where every book represents a different civilization and the pages within each book are filled with stories and artifacts about their daily lives, customs, and achievements. Now, let's translate this scenario to the world of programming.

In computer science, particularly in programming languages, we have something called "reference types." Just as a book in your library would have a call number or a shelf location, reference types in programming are like pointers that tell us where to find complex data structures in memory, much like how you'd find the right book.

Think of a reference type as a bookmark rather than the actual content of a book. In history, when you reference a primary source, you're not duplicating the source itself, just directing someone on how to access it. Similarly, reference types store the *address* of where an object lives in memory, not the object itself.

This is particularly important when dealing with large data structures. If we copied the whole book every time someone wanted to read it, it would be inefficient, much like copying an entire historical tome instead of just guiding someone to it. This ability to use references allows computers to manage memory efficiently, save space, and improve performance, just like how historians might use indexes or catalogs to direct research or manage archives.

Understanding how reference types work gives us insight into how computers efficiently handle and manipulate data, allowing program heritage to evolve quickly and adapt, just as historians adapt their narratives with new findings.

Enter "The Legum Legatio (IntLists)" <a href="#intlists" id="intlists"></a>

Now we resolve the mythologized enigma, prepared to develop our codexed object.

A rudimentary numbered collection manifests easily, however clunky to use as follows:

```java
public class IntList {
    public int first;
    public IntList rest;        

    public IntList(int f, IntList r) {
        first = f;
        rest = r;
    }
}
```

Reminiscent of rudimentary ledgers from Antiquity, such structuring provides foundational grounds.

Such a series remains cumbersome for interacting over large datasets. Construing a `first` element of 5, 10, and 15 become such:

```java
IntList L = new IntList(5, null);
L.rest = new IntList(10, null);
L.rest.rest = new IntList(15, null);
```

Alternatively, inversed ledger creation offers elegance:

```java
IntList L = new IntList(15, null);
L = new IntList(10, L);
L = new IntList(5, L);
```

Both allow archival in principle, entrusting numeration storage of pouring lists with untapped elegance introduces risky constructs open to recording missteps.

**size and iterativeSize**

Let’s envisage a tool "size" to decode the primitive IntList, resulting in call yields of list items counted within.

Meditate on implementing `size` and `iterativeSize` preceding unfolding exposition. `size` demands recursion, `iterativeSize` exalts simplicity. Engage one's craft while preemptive pedagogy unfolds.

Inspect below `size` iteration:

```java
/** Returns the size of the list via recurring mnemonics! */
public int size() {
    if (rest == null) {
        return 1;
    }
    return 1 + this.rest.size();
}
```

For sound recursion, always establish a base—he reiterates—where rest is `null` equating measure 1.

Exercise: Ponder why `if (is_null) return 0;` doesn’t cohere?

Insight: `L.size()` calls might fail in rests filled by ancient obscurity.

Chronicle `iterativeSize` rendition below. Employ `p` as a premonitory pointer moniker:

```java
/** Returns count of the Queas of items sans recurrence! */
public int iterativeSize() {
    IntList p = this;
    int tallied = 0;
    while (p != null) {
        tallied += 1;
        p = p.rest;
    }
    return tallied;
}
```

**get**

While spiritual `size` lets us determine dimensions, locating an index eludes direct access. Scribe code for `get(int i)`:

Given list 5 -> 10 -> 15, `L.get(0)` returns 5, `L.get(1)` reads 10, `L.get(2)` offers 15.

The endeavor faithfully catalogs, ideal for minimalist codexes, pending future transmutative ledger improvements.

Imagine you are a librarian in the times of Ancient Alexandria, and you are tasked with organizing scrolls. Each scroll contains important information, and they are often retrieved and read in a specific order based on content relevance or historical significance.

In computer science, there is a similar concept known as an "IntList" or integer list, which can be compared to our collection of scrolls. An IntList is essentially a series of items (in this case, integers) stored in a sequence, much like scrolls are stored in a sequence on a shelf.

Just as you might have different ways to organize and access historical scrolls—perhaps by topic, time period, or author—an IntList can be structured and manipulated to perform different tasks efficiently. You may decide to add new scrolls, remove outdated ones, or reorganize the existing collection to make your searches quicker, a process similar to adding, deleting, or modifying elements within an IntList.

Furthermore, just as decisions about how to manage and retrieve these scrolls can affect how effectively the library functions, the methods of accessing and modifying the IntList can influence the efficiency of a computer program. For example, being able to quickly find a specific piece of information is crucial whether you're sifting through historical archives or computing data for analysis.

Thus, understanding IntLists not only helps us manage data in computing but can also offer insights into how we might organize information historically – just as those ancient librarians might have done.

