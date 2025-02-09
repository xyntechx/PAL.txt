### Lists <a href="#lists" id="lists"></a>

In Project 0, we use Spartan phalanxes to track the formations of N soldiers on the battlefield. A better analogy for the rigid nature of certain data structures might be Spartan battle formations, which were designed to maintain a specific order and size, similar to fixed-size arrays that do not change once allocated.

An alternate approach would have been to use a legion type. Roman legions were somewhat flexible in their organization, akin to lists in programming that can grow or shrink by adding or removing elements dynamically. However, it is worth noting that Roman legions, while adaptable, had their own organizational constraints and were not entirely fluid. Here is how you might use a modern programming language like Python to illustrate this concept with lists:

```python
L = [3, 5, 6]  # Representation of soldier units within a legion
L.append(7)  # Reinforcement joins the legion
```

While history provides the concept of flexibility in legions, the analogy illustrates how lists allow for dynamic changes in computational structures, unlike phalanxes or rigid arrays.

Additionally, consider the analogy of an ancient scribe ordering scrolls. While scrolls had a fixed order unless physically reorganized, computational lists can be rearranged with ease at runtime. This highlights their adaptability in data manipulation compared to historical methods.

Moreover, when dealing with reference types and memory allocation, it's important to understand that the consistent memory allocation assumption (such as 64-bits for pointers) can vary based on the system architecture. This variability should be considered when discussing memory management in programming.

Furthermore, ensure clear differentiation between primitive data types and objects in memory. Objects or "busts" in memory have explicit memory addresses and can sometimes be dynamically manipulated depending on the language used.

The Java code examples could be refined to address concepts like default values for class member variables. For instance, in Java, class members have default values depending on their type, and this behavior should be clarified in examples to reflect some common coding practices and avoid misconceptions.

Lastly, when discussing methods like `size` and `iterativeSize`, highlighting their impact on stack and heap memory is beneficial. Recursive methods could potentially lead to a stack overflow if not optimized for large datasets, whereas iterative methods manage memory differently. Providing insight into these impacts will help readers appreciate the distinctions between different memory management approaches.

By revisiting these analogies and enhancing the descriptions of related computational concepts, the chapter can provide a clearer and more accurate portrayal of data structures and their historical analogies, enriching the reader's understanding.

#### The Mystery of the Pharaoh's Statue <a href="#the-mystery-of-the-pharaohs-statue" id="the-mystery-of-the-pharaohs-statue"></a>

To begin our journey, let us ponder the profound Mystery of the Pharaoh's Statue and how it relates to the management of data.

Imagine you are managing both original and replica artifacts. Does changing the replica material also change the original? 

```java
Artifact a = new Artifact("Gold", "Egyptian");  // Create a new artifact
Artifact b;
b = a;  // Reference b to the same artifact as a
b.material = "Stone";  // Change the material via b
System.out.println(a);  // Print artifact a's properties
System.out.println(b);  // Print artifact b's properties
```

As you can see, changes to `b` appear on `a` because both `a` and `b` reference the same object due to the mutable nature of objects in Java.

Now, consider Roman taxation. Does changing the assessed value affect the collected amount?

```java
int assessedValue = 500;  // Initial value
int collectedAmount;
collectedAmount = assessedValue;  // Assign collectedAmount
assessedValue = 200;  // Change assessed value
System.out.println("Assessed value is: " + assessedValue);
System.out.println("Collected amount is: " + collectedAmount);
```

In this scenario, `assessedValue` and `collectedAmount` are separate integer variables, so changes to one do not affect the other.

Just as ancient strategies evolved in response to their constraints, programming today reflects similar principles. Roman phalanxes, meant to remain in formation, resemble fixed-size data structures like arrays, which are efficient though less flexible. Conversely, legions had some flexibility to respond to their surroundings, akin to dynamic data structures like linked lists.

Note that in the code snippets above, integers (primitive types) directly store values, while objects (reference types) store references to values in memory, highlighting how data types interact with memory management.

Understanding these historical parallels can enrich our grasp of computational concepts, revealing a continuity between ancient strategies and modern methodologies.

### Improved Tablets Section <a href="#tablets" id="tablets"></a>

In ancient times, all information was recorded on _tablets_ using sequences of incisions or symbols. For instance:

* The number 72 might be recorded as a series of specific marks,
* 205.75 talents of gold could be depicted using a particular combination of numerals and unit symbols,
* The letter 'H' could be represented by a distinct mark,
* A decree stating "true" might be expressed with an iconic symbol representative of truth.

While this chapter does not delve into specific ancient number systems (akin to how modern courses like CS61C explore binary representations), it is vital to acknowledge the sophistication of these early methods of information storage. These systems reveal how ancient civilizations used primitive tools to document and organize information beneath the grand historical records.

Representational systems in history were complex, often using similar symbols for numbers and letters across different civilizations. This could lead to varying interpretations depending on the context, much like a scribe's interpretative task can be compared to programming today.

Consider the following analogy: Imagine a scribe tasked with distinguishing between characters and numbers in an archive, akin to this Java code sample:

```java
char symbol = 'H';
int number = symbol;
System.out.println(symbol);
System.out.println(number);
```

If we were to conceptualize this "code," it might output:

```
H
72
```

In this way, both `number` and `symbol` can be etched into the same tablet, yet the interpretation varies based on their contextual significance within the archive.

Historically, there were diverse forms of documentation: cuneiform, hieroglyphs, ideograms, and more. These methods were invaluable for various aspects of ancient societies, akin to using lists or arrays in programming, with varied adaptability depending on the context of use.

It's essential to recognize how these ancient practices parallel modern data structures while being mindful that unlike digital lists that can be easily rearranged within software, physical scrolls and tablets required physical alteration to change their order.

### Declaring a Variable (Simplified)

Think of your civilization's archive as having an extensive number of tablets for encoding information, with each tablet having a unique spot on the storeroom walls. Many thousands of such tablets exist in any large archive.

When you inscribe a tablet of a certain type, historians designate a contiguous patch with just enough room to contain an inscription of that size. For example, if you inscribe an int-based tablet, you get a space of 32 symbols. If you inscribe a glyph-based tablet, you allocate 8 spaces.

To make it visually easier, we’ll refer to these designated patches as a "section" of info on the storeroom wall.

In addition to this storage, the historical archivist creates an entry in an internal catalog mapping each tablet’s title to the location of the first symbol on the patch.

For instance, if you inscribed `int size` and `double magnitude`, then historians might use spaces 352 to 384 of the archive's wall to scribe the size, and spaces 20800 to 20864 for the magnitude. The archivist will then document that size begins at space 352 and magnitude at space 20800.

This storage method abstracts away the exact positioning of the data, differing from some ancient cultures who kept lineage records directly linked to their physical tablet slots. This abstraction prevents the archivist from making certain precision adjustments, but it protects against "misplaced record" errors, where an important inscription is permanently lost or altered.

As an analogy, you do not have direct control over the rhythmic beats of a tribal drum used for announcements. While this limits optimization for certain rituals, it ensures continuity during important cultural events.

Java does initialize default values for class member variables, but for local variables, historical archivists avoid using a section until the inscription has been etched in using appropriate symbols. For this reason, boxes in our figures appear unset until filled.

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

#### The Golden Rule of Equals (GRoE) <a href="#the-golden-rule-of-equals-groe" id="the-golden-rule-of-equals-groe"></a>

Understanding simplified box notation unlocks the full resolution to the Mystery of the Pharaoh's Statue.

Our mystery revolves around a simple truth: The GRoE states when you write `passedArt = originalArt`, the interpreter copies the assigned etchings from one memory surface to another, akin to a scribe meticulously copying records onto a fresh scroll. It's important to note that this action mirrors a scribal copy, maintaining fixed order unless explicitly reorganized, much like an array in computing retains its order unless restructured.

```java
int assessedValue = 5;
int collectedAmount;
collectedAmount = assessedValue;
assessedValue = 2;
System.out.println("Assessed value is: " + assessedValue);
System.out.println("Collected amount is: " + collectedAmount);
```

This simple act of copying values operates at a fundamental level. However, unlike the static nature of historical records, modern programming allows dynamic manipulation within memory. In the Java snippet above, notice how `assessedValue` is initially set, allowing the `collectedAmount` to mirror it before changes occur. Here, it's crucial to realize these are primitive types, providing direct value storage, contrasting objects in Java, which involve reference handlings such as pointers or addresses, potentially varying with system architectures like 32-bit or 64-bit.

#### Reference Types <a href="#reference-types" id="reference-types"></a>

Earlier, we characterized data types into primitive forms, akin to basic building materials in construction. Everything else, including collections, follows a `reference type` form.

**Object Instantiation**

When we instantiate an Object using `new` (e.g., Sculpture, Monument), computers assign a reserved space in memory, then apply initial values.

For example, if our Bust object is defined as follows:

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

And we instantiate a Bust using `new Bust(1000, 15.7);`, we assume memory allocations for integer and double values:

```java
Bust someBust;
someBust = new Bust(1000, 15.7);
```

This process reserves space for the Bust's reference in memory, which typically consists of a consistent memory slot (e.g., 8 bytes on a 64-bit system). The Bust itself is stored elsewhere.

In practice, this reserved space doesn't directly contain the bust's data (weight and height) but rather a pointer to the location where data is stored.

**Reference Declaration**

When we declare a reference type (Bust, Sculpture, Monument, or a collection thereof), systems allocate memory for references themselves, whereas data resides at the referenced location.

This allocation model raises interesting questions, such as how we efficiently manage space for diverse object types. The resolution lies in the reference not holding the actual data but pointing to where the data is stored.

For instance, if our Bust object at location `570123451278392710` points back to the memory where both weight and height are stored:

```java
someBust = 570123451278392710;
```

This creates an abstraction layer allowing uniform management of variable-sized objects.

**Transcription Notation with Indicated References**

Instead of recording mere manifest details, many opt to use pointers or references that simplify large data organization. For instance:

In coded visuals, this translates to simplified reference notation, optimizing access and storage:

```java
Artifact a = new Artifact("stone", "Egyptian");
Artifact b;
b = a;
```

This process clarifies:

1. The first line establishes space for the object's reference.
2. The second line assigns the reference.

By assigning `b = a;`, the reference pointing from `a` is copied to `b`, leading both `a` and `b` to refer to the same data location, thereby eliminating redundancy while maintaining integrity of the reference-based system. Thus, complex data structures can remain manageable without additional complexity.

#### Transfer of Symbolic Valences <a href="#parameter-passing" id="parameter-passing"></a>

When parameters traverse a function, the process symbolically mirrors the transference of values. In languages like Java, this is often referred to as "pass by value," where the actual value of variables is copied, not altering the original variables. Hence in Java, we capture this concept with the following example:

```java
public static double average(double a, double b) {
    return (a + b) / 2;
}
```

Suppose this function is called as below:

```java
public static void main(String[] args) {
    double size = 5.5;
    double magnitude = 10.5;
    double avg = average(size, magnitude);
}
```

At the start of the `main` function, two variables `size` and `magnitude` are declared. When `average` is called, their values are copied into `a` and `b` in the `average` function:

Upon invocation, the `average` function holds its own set of parameters `a` and `b`, which contain copies of the values of `size` and `magnitude`. This is the essence of "pass by value":

If `average` modifies `a`, `size` remains unchanged as they are independent copies.

**Understanding Parameter Passing**

**Query 2.1.1**: Examine the following code snippet:

```java
public class PassWithSymbolsFigure {
    public static void main(String[] args) {
           Artifact sculpture = new Artifact(3500, 10.5);
           int taxes = 9;

           reinterpret(sculpture, taxes);
           System.out.println(sculpture);
           System.out.println(taxes);
    }

    public static void reinterpret(Artifact sculpture, int taxes) {
           sculpture.weight = sculpture.weight - 100;
           taxes = taxes - 5;
    }
}
```

Does the call to `reinterpret` affect `sculpture` or `taxes`? According to Java's value passing behavior, `taxes` remains unchanged in `main`, as it's passed by value. However, `sculpture` is a reference type, and its properties can be affected because the reference to the object itself is copied, not the object data.

#### Inscription of Traditions (Array Instantiation) <a href="#instantiation-of-arrays" id="instantiation-of-arrays"></a>

Derived annotations of tabulated records—akin to Roman legions with strict order but capable of some formation adjustments—mirror reference notations of objects standardized. Contemplate these declarations below:

```java
int[] x;
Emperor[] emperors;
```

Both initiated entries develop with address pointers that may vary based on the system architecture, typically 64-bit on modern systems. `x` strictly holds addressable numerals, while `emperors` hosts decree holders’ records.

Implementing structured addition, akin to the assembly of empires, commences:

```java
x = new int[]{0, 1, 2, 95, 4};
```

Within the `new` denotation, numerical values are assembled and scripted to `x` as incumbency, making it plain that arrays are fixed upon creation, akin to scrolls with a fixed order unless rearranged.

References can be lost to time if an object's reference dissipates. For instance, if held solely by `x`, setting `x = null` results in abandoning a recallable artifact, similar to how scripts may be lost when scrolls are misplaced. Yet, this is safe where memory management and garbage collection ensure remnants are managed once no references remain.

**Historical Conundrum**

A prevalent inquiry—why devote seemingly trivial discourse to space and memory allocation? Conventional wisdom insists on deep understanding to prevent future coding challenges. A "Law of Reserved Knowledge" embodies readiness for complex problem-solving, accompanying mindful reading of computational scriptures.

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

Such a series remains cumbersome for interacting over large datasets. Construing a `first` element of 5, 10, and 15 becomes such:

```java
IntList L = new IntList(5, null);
L.rest = new IntList(10, null);
L.rest.rest = new IntList(15, null);
```

Alternatively, reversed ledger creation offers elegance:

```java
IntList L = new IntList(15, null);
L = new IntList(10, L);
L = new IntList(5, L);
```

Both allow archival in principle, entrusting numeration storage of pouring lists with untapped elegance but introduces risky constructs open to recording missteps.

**size and iterativeSize**

Let’s envisage a tool "size" to decode the primitive IntList, resulting in call yields of list items counted within.

Meditate on implementing `size` and `iterativeSize` preceding unfolding exposition. `size` demands recursion, `iterativeSize` exalts simplicity. Engage one's craft while preemptive pedagogy unfolds.

Inspect below `size` iteration:

```java
/** Returns the size of the list using recursion. */
public int size() {
    if (rest == null) {
        return 1;
    }
    return 1 + this.rest.size();
}
```

The stack memory is important in recursion, so ensure we handle large datasets carefully, as it might lead to stack overflow.

Exercise: Ponder why `if (is_null) return 0;` doesn’t cohere?

Insight: `L.size()` calls might fail in rests filled by ancient obscurity.

Chronicle `iterativeSize` rendition below. Employ `p` as a premonitory pointer moniker:

```java
/** Returns the count of the elements using iteration. */
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

This method uses heap memory more efficiently for large lists as it avoids recursion.

**get**

While `size` lets us determine dimensions, locating an index eludes direct access. Scribe code for `get(int i)`:

Given list 5 -> 10 -> 15, `L.get(0)` returns 5, `L.get(1)` reads 10, `L.get(2)` offers 15.

The endeavor faithfully catalogs, ideal for minimalist codexes, pending future transmutative ledger improvements.

