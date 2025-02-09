### Collections of Celestial Objects <a href="#lists" id="lists"></a>

In Project 0, we use arrays to track the spatial coordinates of N celestial bodies in the universe, such as stars, planets, and black holes. One thing that galaxies of this cosmic simulation would quickly face is the static nature of arrays in interstellar distances once the simulation commenced. This rigidity is inherent in the fixed-size nature of arrays in Java which cannot adapt to the birth and death of stars over cosmic time spans.

An alternative is to utilize a list data structure. Like how constellations are conceptually linked by our observations in the night sky, a list can dynamically manage the ever-changing inventory of celestial entities. For instance, in Python, as new stars form in the cosmic sea, they can be added to your collection:

```python
L = ['Star', 'Planet', 'Comet']
L.append('Moon')
```

Java offers a native List type, but for now, we’ll explore the fundamentals by creating our own list from nothingness, thus delving into the elemental coding forces within Java.

Additionally, when implementing a `StellarIntList`, consider the impact of using a recursive approach for functions like `size()`. While recursive solutions elegantly emulate list traversal, they may lead to stack overflow with larger lists. Techniques such as tail recursion optimization could mitigate this, but are not inherently supported by Java.

Moreover, when discussing binary representation, it's important to connect these concepts to their applications in astronomy, such as how CCD image encoding or radio telescope data rely on binary data handling. This will provide a clearer connection to real-world astronomical data collection and processing.

Understanding reference types in Java is crucial, especially in terms of performance in simulations. Handling reference types influences memory usage significantly, impacting computational efficiency during astrophysical simulations.

Finally, when considering parameter passing, it’s essential to emphasize that Java employs pass-by-value for all variable types. In the context of objects, this "value" is the reference itself, which can lead to misunderstandings about object manipulations, particularly in intricate simulations or data processing tasks where accurate model interactions are vital.

By grounding our exploration in authentic astrophysical requirements and challenges, we bridge the conceptual framework between computer science applications and astrophysical inquiry, enriching our understanding and honing our skills across both domains.

#### The Cosmic Mystery of the Celestial Walrus <a href="#the-mystery-of-the-walrus" id="the-mystery-of-the-walrus"></a>

To start our exploratory journey, let's unravel the Cosmic Mystery of the Celestial Walrus.

Predict what happens when we execute the cosmic code below. Consider: If `body b` is altered, does it affect the state of `body a`? Note: References in Java can have cosmic parallelism to handling shared resources.

```java
CelestialWalrus a = new CelestialWalrus(1000, 8.3);
CelestialWalrus b;
b = a;
b.mass = 5;
System.out.println(a);
System.out.println(b);
```

Now forecast the behavior of these integers in a void. Does changing `mass x` change `mass y`?

```java
int x = 5;
int y;
y = x;
x = 2;
System.out.println("x is: " + x);
System.out.println("y is: " + y);
```

Solutions reside [here](http://cscircles.cemc.uwaterloo.ca/java_visualize/#code=public+class+PollQuestions+%7B%0A+++public+static+void+main%28String%5B%5D+args%29+%7B%0A++++++CelestialWalrus+a+%3D+new+CelestialWalrus%281000,+8.3%29%3B%0A++++++CelestialWalrus+b%3B%0A++++++b+%3D+a%3B%0A++++++b.mass+%3D+5%3B%0A++++++System.out.println%28a%29%3B%0A++++++System.out.println%28b%29%3B++++++%0A%0A++++++int+x+%3D+5%3B%0A++++++int+y%3B%0A++++++y+%3D+x%3B%0A++++++x+%3D+2%3B%0A++++++System.out.println%28%22x+is%3A+%22+%2B+x%29%3B%0A++++++System.out.println%28%22y+is%3A+%22+%2B+y%29%3B++++++%0A+++%7D%0A+++%0A+++public+static+class+CelestialWalrus+%7B%0A++++++public+int+mass%3B%0A++++++public+double+magnitude%3B%0A++++++%0A++++++public+CelestialWalrus%28int+w,+double+ts%29+%7B%0A+++++++++mass+%3D+w%3B%0A+++++++++magnitude+%3D+ts%3B%0A++++++%7D%0A%0A++++++public+String+toString%28%29+%7B%0A+++++++++return+String.format%28%22mass%3A+%25d,+brightness+size%3A+%25.2f%22,+mass,+magnitude%29%3B%0A++++++%7D%0A+++%7D%0A%7D&mode=edit).

This cosmic analogy highlights how reference types work in Java. In Java, a variable holds only the reference (or address) of an object, not the object itself. This is akin to how data references work in simulations where memory efficiency is key, especially in large-scale astrophysical simulations involving data such as CCD images or radio telescope signals. Understanding these interactions is crucial for crafting efficient and reliable code that can navigate the vast complexities of both computer science and astrophysics.

#### Quantum Bits <a href="#bits" id="bits"></a>

In quantum computing and simulations of the universe, binary data play a crucial role in encoding astronomical observations. These are stored in a vast memory grid of ones and zeros. Let’s explore some examples:

* The integer 72 is often represented as 01001000.
* The floating-point number 205.75, commonly seen in astrophysical calculations, is represented as 01000011 01001101 11000000 00000000 in IEEE 754 binary format.
* The elemental symbol 'H' for Hydrogen shares the binary sequence 01001000, akin to the value 72.
* Boolean values representing the truth of cosmic events are stored simply as 00000001 for true.

While we won't delve into the detailed process of binary encoding, it's important to acknowledge these binary sequences are essential in processing data from cosmic observations, such as CCD image encoding and radio telescope data translation. These types of data help us understand the universe’s structure and evolution.

An interesting observation is that both 72 and the character 'H' use the same binary encoding: 01001000. How does Java interpret this duality?

The answer lies in data types! Consider the following Java code snippet:

```java
char c = 'H';
int x = c;
System.out.println(c);
System.out.println(x);
```

When executed, this code outputs:

```
H
72
```

In this example, `x` and `c` originate from the same underlying binary sequence, but Java distinguishes them by using the type specified in the program.

Java features eight primary data types: byte, short, int, long, float, double, boolean, and char. Each has unique characteristics important for simulation tasks and data management in astrophysical contexts. Understanding these types becomes crucial in handling data efficiently in large-scale simulations or high-precision computations related to astronomical phenomena.

#### Declaring a Variable with an Astrophysical Perspective <a href="#declaring-a-variable-simplified" id="declaring-a-variable-simplified"></a>

Consider your computer as a cosmic expanse that holds countless data bits like celestial objects, each with a unique identifier. These bits operate like digital stars within contemporary computational systems.

Declaring a variable of a specific type prompts Java to allocate space equivalent to a segment of this cosmic landscape to hold a particular entity. For instance, declaring an `int` leads to reserving a nebula of 32 bits, while a `byte` reserves 8 bits. Different data types occupy different-sized regions in this cosmic terrain. The exact size, however, is often abstracted away from the user.

For simplicity, let's use the analogy of placing these bits into "quantum boxes."

When you declare a variable in Java, the Java interpreter maintains a metaphorical map that links each variable's name to its starting position within this cosmic space.

Example: Declaring `int x;` may result in assigning bits 352 to 384 for `x`, and `double y;` may use bits 20800 to 20864. Thus, the interpreter notes that these positions are linked to `x` and `y` as follows:

![x\_and\_y\_empty\_bitwise](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/x\_and\_y\_empty\_bitwise.png)

In Java, unlike languages such as C, you cannot directly access the memory addresses of these variables. This restriction prevents certain bugs and errors, providing a layer of abstraction.

Java does not supply a default initial state for a declared variable. The compiler restricts usage of a variable until it is initialized via the `=` operator.

Upon assigning values to these variables:

```java
x = -1431195969;
y = 567213.112;
```

The memory boxes fill with specified values as depicted:

![x\_and\_y\_empty\_filled.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/x\_and\_y\_empty\_filled.png)

The underlying bit encoding for integers and floating-point numbers is a deeper topic explored in advanced courses like CS61C. Interested readers can explore resources on [integer representations](https://en.wikipedia.org/wiki/Two%27s_complement) and [floating-point numbers](https://en.wikipedia.org/wiki/IEEE_floating_point) for in-depth explanation.

**Simplified Memory Visualization**

Though it's informative to depict memory using binary structure, this notation is often transformed into a more digestible form for human understanding. This transformation assists in creating clear visualizations for studying computations:

Following the initialization of:

```java
int x;
double y;
x = -1431195969;
y = 567213.112;
```

We depict the variable environment as follows in a human-readable format:

![x\_and\_y\_simplified\_box\_notation.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/x\_and\_y\_simplified\_box\_notation.png)

#### The Cosmic Law of Equality (CLE) <a href="#the-cosmic-law-of-equals-groe" id="the-golden-rule-of-equals-groe"></a>

Anchored in box notation derived elegance, we advance to disentangle the Celestial Constellation mystery.

As cosmic serendipity suggests: Executing `y = x`, commands the Java interpreter to transpose x’s cosmic bits into y’s cosmic box. This Cosmic Law of Equality (CLE) crystallizes truth within our observations of constellations.

```java
int x = 5;
int y;
y = x;
x = 2;
System.out.println("x is: " + x);
System.out.println("y is: " + y);
```

The cosmic essence of bit transfiguration holds for EVERY assignment availing `=` within Java’s astral plane. Witness this execution via [this astral visualization](http://cscircles.cemc.uwaterloo.ca/java_visualize/#code=public+class+PollQuestions+%7B%0A+++public+static+void+main\(String%5B%5D+args%29+%7B%0A++++++int+x+%3D+5%3B%0A++++++int+y%3B%0A++++++y+%3D+x%3B%0A++++++x+%3D+2%3B%0A++++++System.out.println\(%22x+is%3A+%22+%2B+x%29%3B%0A++++++System.out.println\(%22y+is%3A+%22+%2B+y%29%3B++++++%0A+++%7D%0A%7D&mode=display&curInstr=0).

Additionally, handling of reference types in Java affects performance, which is crucial in simulations, much like data handling in astrophysical contexts. Java's parameter passing is by value, even for objects, where the “value” is actually a reference, emphasizing careful consideration in object manipulation, similar to optimizing data flows in astronomical simulations.

#### Reference Types in the Astrophysical Spectrum <a href="#reference-types" id="reference-types"></a>

In the vast expanse of the cosmos, Java’s fundamental data types exist as eight basic types: byte, short, int, long, float, double, boolean, char. Beyond these, we encounter reference types, including arrays, which serve as conceptual constellations rather than physical representations.

**Celestial Object Instantiation**

When we instantiate an Object using `new` (such as Nebula, CelestialWalrus, or Galaxy), Java's memory model allocates space for variables and ensures default initialization. The constructor typically sets initial values to these fields.

Consider the CelestialWalrus class:

```java
public static class CelestialWalrus {
    public int mass;
    public double magnitude;

    public CelestialWalrus(int m, double size) {
          mass = m;
          magnitude = size;
    }
}
```

We can create a CelestialWalrus object with `new CelestialWalrus(1000, 8.3);` representing an object with two properties, each occupying 32 and 64 bits respectively. In Java implementations, each object instance includes additional overhead. However, for simplicity, we generally ignore this additional overhead in educational illustrations.

The new CelestialWalrus is merely instantiated and doesn't engage until it is assigned to a variable.

**Reference Variable Declaration**

When you declare a variable for a reference type (such as CelestialWalrus, Galaxy, Satellite, arrays, etc.), Java assigns a memory address of 64 bits, independent of the object's size.

Initially, this might seem paradoxical. The CelestialWalrus requires more than 64 bits for its data, so how is it contained within the 64-bit reference?

The answer is that the 64-bit reference stores not the data itself but the memory address where the object resides, akin to coordinates.

For example:

```java
CelestialWalrus someWalrus;
someWalrus = new CelestialWalrus(1000, 8.3);
```

The first line allocates a box of 64 bits; the second line creates an object. The memory location of this object is what gets stored in `someWalrus`.

Binary representation examples align closely with data storage in astronomical observation technologies, like how CCD images or data from radio telescopes are encoded.

The null reference, represented by zero, signifies a non-existent object.

**Box and Pointer Notation**

To simplify understanding of references, "box and pointer" notation is often used:

- A null reference is shown as an empty box.
- A reference with an address points to its object with an arrow.

This approach clarifies visualization of object references.

In astrophysics, managing large datasets requires attention to memory management, analogous to efficiently handling Java references.

**Resolving References for Celestial Entities**

Let's clarify these concepts with a brief exercise.

```java
CelestialWalrus a = new CelestialWalrus(1000, 8.3);
CelestialWalrus b;
b = a;
```

After the first line, `a` holds a reference to our astronomical data, while the assignment of `b = a;` means both variables point to the same object—similar to how different observations can map to the same star grouping based on context.

This section closes with a reminder that handling references efficiently impacts performance, especially in simulations that mirror astrophysical phenomena, illustrating the practical importance of these concepts.

#### Astral Parameter Passing <a href="#parameter-passing" id="parameter-passing"></a>

In cosmic transfers, when celestial parameters enter a function, the bits continue their odyssey. Consequently, CLE extends its precise control upon parameter passage akin to "pass by cosmic value" in Java, which universally engages in this exchange.

Consider the stellar function illuminating below:

```java
public static double computeBrightness(double star1, double star2) {
    return (star1 + star2) / 2;
}
```

Suppose one invokes this cosmic calculation as scripted:

```java
public static void main(String[] args) {
    double lum1 = 5.5;
    double lum2 = 10.5;
    double lumAvg = computeBrightness(lum1, lum2);
}
```

Upon executing introductory statements, the main cosmic field visualizes `lum1` and `lum2` enshrined in cosmic capsules bearing:

![main_lum1_lum2.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/main_x_y.png)

Invoking the cosmic function `computeBrightness` conjures its **own** cosmic environment with stellar boxes `star1` and `star2`. Bits simply mirror their origin, depicting CLE as "pass by value". Note that while Java passes objects by sharing the reference value, it still adheres to its sole pass-by-value paradigm.

![computeBrightness_star1_star2.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/average_a_b.png)

Should `computeBrightness` alter `star1`, main's `lum1` remains unchanged, as CLE dictates only `star1`'s box admittance of new bits.

**Test Your Astrophysical Insights**

**Exercise 2.1.1**: Given the celestial transformation below:

```java
public class GalaxyPassByValue {
    public static void main(String[] args) {
           CelestialWalrus walrus = new CelestialWalrus(3500, 10.5);
           int x = 9;

           transmute(walrus, x);
           System.out.println(walrus);
           System.out.println(x);
    }

    public static void transmute(CelestialWalrus W, int x) {
           W.mass = W.mass - 100;
           x = x - 5;
    }
}
```

Can the astral call to `transmute` affect walrus and/or x? Hint: Java's methodology ensures object fields can change via reference, but primitives such as `x` convey only their value.

#### Arrays in the Astrophysical Realm <a href="#instantiation-of-arrays" id="instantiation-of-arrays"></a>

As celestial law decrees, variables harboring arrays derive reference properties similar to conceptual constellations mapped out in our night sky. Consider cosmic declarations prescribed:

```java
int[] starMasses;
Planet[] celestialBodies;
```

Both declarations spawn 64-bit celestial boxes. `starMasses` contains addresses of an `int` starfield, while `celestialBodies` enfolds a `Planet` orbital path.

Creating an array mirrors cosmic generation of objects. For instance, forming an integer starfield of dimension 5:

```java
starMasses = new int[]{0, 1, 2, 95, 4};
```

The invocation of `new` kindles five celestial boxes of 32 bits each, returning a cosmic address that is embedded into `starMasses`.

To make this discussion more relevant to astrophysics, consider how binary data translate to processes in astronomical data collection, like how CCD images are encoded into binary formats or how radio telescopes convert their received signals into binary data.

Celestial objects fade if astrally detached from their quantum locus. Imagine a unique CelestialWalrus tethered solely to `starMasses`, then `starMasses = null` would relinquish this cosmic instance eternally. Often these occurrences are deliberate during cosmic cycles when objects transcend usage, casting their addresses to the astral winds. When foraging for cosmic lists later, we shall experience such phenomena.

**The Cosmic Law of Broken Syntax**

Immersed one may wonder, why bestow such import and cosmic expanse to an apparent cosmic compendium? For this cosmos might seem simplistic, especially if Java wisdom graces you.

This cautionary framing emerges to precisely thwart potential misconceptions nurtured by half-lit comprehension. Struggles without grasp could herald downfall into chasms later while navigating more intricate celestial realms.

In cosmic verbiage stands narrative about this [Cosmic Law of Broken Syntax](https://mathwithbaddrawings.com/2015/04/08/the-math-ceiling-wheres-your-cognitive-breaking-point/): ensuring firm understanding BEFORE astral exploration unravels beyond.

Handling such cosmic references can impact performance, such as memory use in simulations. In Java, all parameter passing is by value, even for objects where the "value" being passed is a reference. Keeping this in mind prevents misconceptions about object manipulation, especially in large-scale astrophysical simulations.

#### Celestial IntLists <a href="#intlists" id="intlists"></a>

Cognizant of cosmic teachings, herewith we materialize an enigmatic list akin to constellations mapped out in the sky, conceptually linking elements like stars connected by our observations.

This basic celestial list emerges almost trivially, as follows:

```java
public class StellarIntList {
    public int first;
    public StellarIntList rest;        

    public StellarIntList(int f, StellarIntList r) {
        first = f;
        rest = r;
    }
}
```

Akin to 61a's "Linked List" with an astral metaphor, an awkward-to-manipulate structure spans. For a list of cosmic integers 5, 10, and 15, one could:

```java
StellarIntList L = new StellarIntList(5, null);
L.rest = new StellarIntList(10, null);
L.rest.rest = new StellarIntList(15, null);
```

Alternatively, one could architect their celestial list in reverse, producing a slightly more efficient but opaque script:

```java
StellarIntList L = new StellarIntList(15, null);
L = new StellarIntList(10, L);
L = new StellarIntList(5, L);
```

While legitimately encapsulating cosmic integers, the resulting structure remains somewhat arcane, occasionally chaotic. Benefiting from conventional OOP strategies, we add auxiliary methods to our class to perform standard operations.

**size and iterativeSize**

Enlivening a method `size` in the `StellarIntList` class promises if one summons `L.size()`, a reckoning returns the entity count within. Although effective for small lists, be cautious of large list sizes as recursive depth could risk stack overflow. Consider mitigating techniques such as tail recursion optimization if applicable.

Before engaging the remainder of this chapter, attempt writing `size` and `iterativeSize`. `size` should deploy recursion, while `iterativeSize` remains iterative. Seeking knowledge alone precedes seeing examples.

My `size` method manifests below:

```java
/** Return the size of the list using recursion. */
public int size() {
    if (rest == null) {
        return 1;
    }
    return 1 + this.rest.size();
}
```

Critical to remember: Recursive code requires careful consideration to avoid deep recursive calls. Here, rest's cessation at `null` creates the simplest base case.

Exercise: Cogitate why opting for `if (this == null) return 0;` fails to fortify? Consider ramifications when list presence equates to `null`—triggering NullPointer errors upon invoking size in L.

My `iterativeSize` follows below. Use `p` as a pointer. This eases Java interactions, where "this" remains immutable.

```java
/** Assess the list size iteratively. */
public int iterativeSize() {
    StellarIntList p = this;
    int totalSize = 0;
    while (p != null) {
        totalSize += 1;
        p = p.rest;
    }
    return totalSize;
}
```

**get Element**

Though `size` privileges us quantification, acquiring ith element remains elusive.

Exercise: Script a method `get(int i)` returning the ith list member. If `L` spans 5 -> 10 -> 15, then `L.get(0)` proffers 5, `L.get(1)` yields 10, and `L.get(2)` bestows 15. Validity of `i`, either too large or small, should be considered.

For solutions, immerse within lecture video or peruse the lectureCode repository.

Note that the script runs with linear time complexity! Hence, with 1,000,000 entities, accessing the final element is lengthy. We'll witness alternate formations avoiding this challenge moving forward.


