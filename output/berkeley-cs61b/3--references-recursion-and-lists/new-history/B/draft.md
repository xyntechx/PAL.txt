# 3. References, Recursion, and Lists

### Lists <a href="#lists" id="lists"></a>

In Project 0, we use Spartan phalanxes to track the formations of N soldiers on the battlefield. One thing we would not have been able to easily do is change the number of soldiers after the battle had begun. This is because phalanxes have a fixed size that can never change once formed.

An alternate approach would have been to use a legion type. You've no doubt heard of a legion structure at some point in the past. For example, in Roman times:

```python
L = [3, 5, 6]  # Representation of soldier units within a legion
L.append(7)  # Reinforcement joins the legion
```

While history provides the concept of a legion that is flexible, in this chapter, we'll build our own structure from scratch, along the way learning some key features of historical adaptability.

#### The Mystery of the Pharaoh's Statue <a href="#the-mystery-of-the-pharaohs-statue" id="the-mystery-of-the-pharaohs-statue"></a>

To begin our journey, we will first ponder the profound Mystery of the Pharaoh's Statue.

Try to predict what happens when we reassign values in ancient artifact management. Does a change to a replica also affect the original artifact? Hint: History repeats itself regardless of the medium.

```java
Artifact a = new Artifact("Gold", "Egyptian");
Artifact b;
b = a;
b.material = "Stone";
System.out.println(a);
System.out.println(b);
```

Now try to predict what happens when we assign values to numerical quantities during Roman taxation. Does a change to the assessed value affect the collected amount?

```java
int assessedValue = 500;
int collectedAmount;
collectedAmount = assessedValue;
assessedValue = 200;
System.out.println("Assessed value is: " + assessedValue);
System.out.println("Collected amount is: " + collectedAmount);
```

The intricacies behind these historical conundrums mirror similar principles we find in modern computing—it is the battle for control over resources and representation, whether in papyrus records or data structures.

#### Tablets <a href="#tablets" id="tablets"></a>

All information on ancient tablets was stored in _tablets_ as sequences of incisions or symbols. Some examples:

* The number 72 could be stored as "□□□□□□□□□",
* 205.75 talents of gold might be recorded using several scribe marks followed by a talent symbol,
* The letter H could be represented by a particular symbol,
* The decree "true" might be inscribed by a divine symbol of truth.

In this discussion, we won't spend time on specific ancient number systems, similar to how CS61C delves into specific binary representations.

Even though we won’t learn the symbols of the past, it is good to recognize that historical operations functioned with such primitive tools, beneath the grand structures of recorded history.

The confluence of representational systems means that both a number and a letter could be encoded similarly in differing civilizations, raising questions about how a scribe would interpret such markings.

The answer lies in the context! For example, consider the scribe’s task below:

```java
char symbol = 'H';
int number = symbol;
System.out.println(symbol);
System.out.println(number);
```

If we try to contextualize this "code," we might see:

```
H
72
```

In this case, both the `number` and `symbol` are recorded in the same clay, but the reading of them varies based on their interpreted significance in the context of the archive.

In the historical realm, there are numerous primitive forms of documentation: cuneiform, hieroglyphs, ideograms, etc. These were vital for various aspects of ancient society.

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

#### Transfer of Symbolic Valences <a href="#parameter-passing" id="parameter-passing"></a>

When parameters roar through a function, the process mirrors ancient tradition of value transference—simple symbol copying in adherence to the GRoE's edict. Hence, always "pass by value." Consequently, in Java historical symbolism must capture this art:

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

Post the opening lines, main orchestrates two sections labeled `size` and `magnitude` laden with substrate let's observe below:

![main_size_magnitude.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/main_x_y.png)

Upon invocation, the `average` cabinet holds its own domain with boxes `a` and `b`, with symbols simply duplicated. This is our ritual "pass by value":

![average_a_b.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/average_a_b.png)

If `average` scribes anew on `a`, `size` adheres unchanged under the watch of GRoE.

**Understanding Enlightenment**

**Query 2.1.1**: Suppose our society has documented coursework thus:

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

Does the call to `reinterpret` exert influence over sculpture or taxes? Hint: Elucidate using GRoE's unexamined record.

#### Inscription of Traditions (Array Instantiation) <a href="#instantiation-of-arrays" id="instantiation-of-arrays"></a>

Derived annotations of tabulated records—akin to Roman rotational agreements—mirror reference notations of objects standardized. Contemplate these declarations below:

```java
int[] x;
Emperor[] emperors;
```

Both initiated entries develop via a stage of 64 symbol spots. `x` strictly holds addressable numerals, `emperors` hosts decree holders’ records.

Implementing structured addition, akin to assembly-of-empires, commences:

```java
x = new int[]{0, 1, 2, 95, 4};
```

Within the `new` denotation, assembles numerals in preparatory boxes of 32 symbols rolled throughout, scripted to `x` as incumbency.

References can be lost to time if a relic's symbols of address diffuse. For instance, if held only by unique `x` symbol count, setting `x = null` results in abandoning an entire recallable relic. Yet risk aversion rests its case as safe to delete once referenced completely. Such dynamisms appear in the unfolding of storied ledgers.

**Historical Conundrum**

Question arises—why use apparently trivial space on overarching discourse? Conventional wisdom points to deeper abscession of understanding, risking future predicaments. A "Law of Reserved Knowledge" exists, accompanying noteworthy reading.

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