# 3. References, Recursion, and Lists with Astrophysics Concepts

### Collections of Celestial Objects <a href="#lists" id="lists"></a>

In Project 0, we use arrays to track the spatial coordinates of N celestial bodies in the universe, such as stars, planets, and black holes. One thing that galaxies of this cosmic simulation would quickly face is the static nature of arrays in interstellar distances once the simulation commenced. This rigidity is inherent in the fixed-size nature of arrays in Java which cannot adapt to the birth and death of stars over cosmic time spans.

An alternative is to utilize a list data structure. In the language of cosmic simulations, a list can adaptively manage the ever-changing inventory of celestial entities. For instance, in Python, you could add new stars as they form in the cosmic sea:

```python
L = ['Star', 'Planet', 'Comet']
L.append('Moon')
```

Java offers a native List type, but for now, we’ll plot our own course through the universe of creating our own list from nothingness, learning along the way the elemental coding forces within Java.

#### The Cosmic Mystery of the Celestial Walrus <a href="#the-mystery-of-the-walrus" id="the-mystery-of-the-walrus"></a>

To start our exploratory journey, we must first unravel the enigmatic Cosmic Mystery of the Celestial Walrus.

Predict what manifests when we execute the cosmic code below. Does altering body b affect the astrophysical state of body a? Clue: Astronomical anomalies in Python behave similarly in this parallel realm of Java.

```java
CelestialWalrus a = new CelestialWalrus(1000, 8.3);
CelestialWalrus b;
b = a;
b.mass = 5;
System.out.println(a);
System.out.println(b);
```

Now forecast the behavior of these orbital integers when launched through space-time. Does modifying mass x influence mass y?

```java
int x = 5;
int y;
y = x;
x = 2;
System.out.println("x is: " + x);
System.out.println("y is: " + y);
```

Solutions reside [here](http://cscircles.cemc.uwaterloo.ca/java_visualize/#code=public+class+PollQuestions+%7B%0A+++public+static+void+main%28String%5B%5D+args%29+%7B%0A++++++CelestialWalrus+a+%3D+new+CelestialWalrus%281000,+8.3%29%3B%0A++++++CelestialWalrus+b%3B%0A++++++b+%3D+a%3B%0A++++++b.mass+%3D+5%3B%0A++++++System.out.println%28a%29%3B%0A++++++System.out.println%28b%29%3B++++++%0A%0A++++++int+x+%3D+5%3B%0A++++++int+y%3B%0A++++++y+%3D+x%3B%0A++++++x+%3D+2%3B%0A++++++System.out.println%28%22x+is%3A+%22+%2B+x%29%3B%0A++++++System.out.println%28%22y+is%3A+%22+%2B+y%29%3B++++++%0A+++%7D%0A+++%0A+++public+static+class+CelestialWalrus+%7B%0A++++++public+int+mass%3B%0A++++++public+double+magnitude%3B%0A++++++%0A++++++public+CelestialWalrus%28int+w,+double+ts%29+%7B%0A+++++++++mass+%3D+w%3B%0A+++++++++magnitude+%3D+ts%3B%0A++++++%7D%0A%0A++++++public+String+toString%28%29+%7B%0A+++++++++return+String.format%28%22mass%3A+%25d,+brightness+size%3A+%25.2f%22,+mass,+magnitude%29%3B%0A++++++%7D%0A+++%7D%0A%7D&mode=edit).

While subtle like dark matter, the fundamental truths behind the Mystery of the Celestial Walrus ignite cosmic wisdom vital to the efficiency of data structures we will shape in this course, and mastering this stellar problem fosters safer, more reliable code that withstands the vacillations of the universe.

#### Quantum Bits <a href="#bits" id="bits"></a>

In quantum computing and cosmic simulations, all celestial data resides in a vast memory matrix of ones and zeros. Some cosmic manifestations:

* 72 transpires often as 01001000
* The star brightness 205.75 transpires often as 01000011 01001101 11000000 00000000
* The elemental mark H is stored as 01001000 (equivalent to 72)
* The truth of cosmic events is stored as 00000001

In our astral journey through CS, we shall not delve deep into binary constellations and their ethereal formations, such as why a nebula of value 205.75 maps to this cryptic 32-bit stellar chant. These cosmic significances are unfurled in the celestial course of [CS61C](http://www-inst.eecs.berkeley.edu/~cs61c/), a sequel to our current cosmic exploration.

Even though we won't decode the stars' binary tongue, it is prudent to recall their existence behind the facade of data.

An intriguing notion is that both 72 and the spectral symbol H share the encoding 01001000. How does Java discern the dual nature of this binary photon?

The secret reclines in types! For example, consider the code embedded below in the quantum field theory of Java:

```java
char c = 'H';
int x = c;
System.out.println(c);
System.out.println(x);
```

Upon executing this code, the cosmic print reveals:

```
H
72
```

In this astral code, x and c both channel the same stellar bit sequence (approximately...), yet Java interprets them distinctly in the moment of revelation.

In the Java cosmos, there are eight primary particles: byte, short, int, long, float, double, boolean, and char. Each particle possesses its intrinsic properties, cosmically discussed throughout our journey, with peripheral references to short and float—seldom utilized in scriptural astral navigations.

#### Declaring a Variable (Simplified Astrophysical View) <a href="#declaring-a-variable-simplified" id="declaring-a-variable-simplified"></a>

Envision your computing apparatus as a cosmic expanse housing countless quantum bits as sparks of celestial data, each with a singular identifier. These cosmic flickers number in the billions within contemporary systems aligning with technological constellations.

Declaring a variable of specific cosmic type prompts Java to requisition an aligned nebula of bits to embody an entity of such type. Declaring an int manifests a nebula of 32 bits, whereas declaring a byte produces a nebula of 8 bits. Varying data types radiate with distinctive bit compositions. In our cosmic exploration, the exact magnitude is but a celestial whisper.

For the poetry of understanding, we dub these boundless blocks as "quantum boxes" of bits.

Beyond laying claim to memory, the Java interpreter weaves an astral ledger correlating each variable's cosmic label to its inaugural quantum bit position.

Instance: Upon the declaration of `int x` and `double y`, Java might divine bits 352 through 384 across cosmic memory for x, while for y it may chart bits 20800 through 20864. The interpreter would encode x's inception at bit 352 and y's initiation at bit 20800, as illustrated below in cosmic tableau:

![x\_and\_y\_empty\_bitwise](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/x\_and\_y\_empty\_bitwise.png)

The Java cosmic lingua does not permit one to decipher box locales directly, obscuring them as below a threshold of abstraction accessible contemporaneously. Unlike languages such as C, which allow one to inquire of a datum’s astral address, this luminosity is withheld within Java—a protective veil averting various [astral hazards](http://www.informit.com/articles/article.aspx?p=2246428&seqNum=1). In accord with the cosmic era's grand abundance, forsaking minor efficiencies is oft considered wise, as Donald Knuth astutely observed: "Premature optimization is the root of all evil across galaxies."

In an analogy veiled in cosmic metaphysics, you do not control your heart's rhythm directly. This constraint shields against abrupt optimizations, warding cosmic error akin to accidently synchronizing your pulse to a black hole.

Java imparts no default cosmic state to a declared quantum box. The compiler restricts variable utilization pre-halo, until bits illuminate the geometric void through the `=` bridge. Reasons transcend understanding this very absence shown as the blank face of the celestial boxes above.

Upon celestial assignment using bits, the quantum boxes brim with encoded starlight:

```java
x = -1431195969;
y = 567213.112;
```

Thus, the memory boxes transmute as depicted in cosmic notation:

![x\_and\_y\_empty\_filled.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/x\_and\_y\_empty\_filled.png)

The stellar top bits embody -1431195969, and the cosmic lower bits forge 567213.112. The arcane alchemy governing these represented stellar maps is dispelled in CS61C. Should curiosity lead you, explore [integer mappings](https://en.wikipedia.org/wiki/Two%27s_complement) and [floating point celestial bodies](https://en.wikipedia.org/wiki/IEEE_floating_point) within Wikipedia’s digital cosmos.

Astrophysical allocation weaves its own complexity beyond our narrative scope, yet our celestial model remains firm enough as a guide through CS 61B’s cosmic tapestry.

**Simplified Quantum Box Notation**

Though pristine in depicting memory’s quantum dance, cosmic binary narration eludes terrestrial interpretation. Henceforth, we transmute these stellar markings into human palatable cosmic symbols. This symbolic transformation enriches visualizations throughout the pilgrimage onward:

Following the execution of:

```java
int x;
double y;
x = -1431195969;
y = 567213.112;
```

We construct the celestial box environment via **simplified cosmic notation** below:

![x\_and\_y\_simplified\_box\_notation.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/x\_and\_y\_simplified\_box\_notation.png)

#### The Cosmic Law of Equality (CLE) <a href="#the-cosmic-law-of-equals-groe" id="the-golden-rule-of-equals-groe"></a>

Anchored in box notation derived elegance, we advance to disentangle the Celestial Walrus mystery.

As cosmic serendipity suggests: Executing `y = x`, commands the Java interpreter to transpose x’s cosmic bits into y’s cosmic box. This Cosmic Law of Equality (CLE) crystallizes truth within the Walrus saga.

```java
int x = 5;
int y;
y = x;
x = 2;
System.out.println("x is: " + x);
System.out.println("y is: " + y);
```

The cosmic essence of bit transfiguration holds for EVERY assignment availing `=` within Java’s astral plane. Witness the execution of galaxies via [this astral visualization](http://cscircles.cemc.uwaterloo.ca/java_visualize/#code=public+class+PollQuestions+%7B%0A+++public+static+void+main\(String%5B%5D+args%29+%7B%0A++++++int+x+%3D+5%3B%0A++++++int+y%3B%0A++++++y+%3D+x%3B%0A++++++x+%3D+2%3B%0A++++++System.out.println\(%22x+is%3A+%22+%2B+x%29%3B%0A++++++System.out.println\(%22y+is%3A+%22+%2B+y%29%3B++++++%0A+++%7D%0A%7D&mode=display&curInstr=0).

#### Reference Types in the Astrophysical Spectrum <a href="#reference-types" id="reference-types"></a>

From the vast void stated herein, 8 fundamental types exist: byte, short, int, long, float, double, boolean, char. Beyond these manifests every other type of cosmic object or reference type, including constellations of arrays.

**Celestial Object Instantiation**

When we commence an Object of galactic proportions using `new` (like Nebula, CelestialWalrus, Galaxy), Java’s quantum precepts allocate space for variables and verifies default initialization. Typically, the constructor fulfills these cosmic bounds with illuminative values.

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

Cosmically birth a CelestialWalrus using `new CelestialWalrus(1000, 8.3);`, manifesting a cosmic entity harboring two elementals, each 32 and 64 bits respectively:

![anonymous\_celestial\_walrus.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/anonymous_walrus.png)

Realize that in native implementations of Java, each manifestation has latent overhead like an orbit to a planet, adding an unspoken mass above the explicit 96 bits. For cosmic simplicity, we abstain from engaging this unseen mass since our interactions bypass it.

The CelestialWalrus, although manifested, lacks a cosmic label, its essence remains nameless until it finds a repository in a cosmic variable.

**Reference Variable Declaration**

Upon proclaiming a variable for any reference type (CelestialWalrus, Galaxy, Satellite, array, etc.), the Java cosmos dictates a quantum box of 64 bits, indistinct to the object’s stature.

At first, this may birth a Celestial Paradox. Our massive CelestialWalrus demands more than 64 bits of astral encoding—how then does it fit into 64?

The evanescent answer is: the 64 bit box, imbued with cosmic consciousness, transcribes not cosmic data of the walrus, but the quantum address akin to interstellar coordinates.

For instance:

```java
CelestialWalrus someWalrus;
someWalrus = new CelestialWalrus(1000, 8.3);
```

The nascent line births a cosmic box of 64 bits. The subsequent line spawns a CelestialWalrus, and the nature of creation returns location as its cosmological constant. These spectral bits migrate into `someWalrus` in celestial alignment to CLE.

Imagining our Walrus data originating from bit `5051956592385990207` of astral memory, and magnitude from bit `5051956592385990239`, the quantum signature `5051956592385990207` symbolizes the CelestialWalrus variable. In binary, it is portrayed as `0100011000011100001001111100000100011101110111000001111000111111`, pictorially:

![someWalrus\_bit\_notation.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/someWalrus_bit_notation.png)

Nullification too is cosmic, where the astral address zero aligns with `null` portraying a stellar void.

![someWalrus\_bit\_notation\_null.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/someWalrus_bit_notation_null.png)

**Quantum Box and Pointer Notation**

To counter the ineffable quantum notations within a reference, we'll employ a simplified cosmic box notation. Here:

- All zero addresses morph into `null`.
- A lively non-zero cosmic signature manifests through an **allegorical arrow** pointing towards its divine object manifestation.

In known parlance, this evolves into "box and pointer" astronomy.

For the cases prior, observe:

![someWalrus\_simplified\_bit\_notation.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/someWalrus_simplified_bit_notation.png)

![someWalrus\_simplified\_bit\_notation\_null.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/someWalrus_simplified_bit_notation_null.png)

**Decoding the Cosmic Mystery of the Celestial Walrus**

With our exposure to cosmic truths, the final unveiling of the Celestial Walrus mystery is at hand.

```java
CelestialWalrus a = new CelestialWalrus(1000, 8.3);
CelestialWalrus b;
b = a;
```

Executing the initial cosmic line yields:

![mystery\_of\_the\_walrus\_resolved\_step1.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/mystery_of_the_walrus_resolved_step1.png)

Through line two, arrives:

![mystery\_of\_the\_walrus\_resolved\_step2.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/mystery_of_the_walrus_resolved_step2.png)

Note that above, b whispers undefined, not void `null`.

Adhering to the CLE, the final cosmic passage shares `a`'s quantum path into `b`. Visually translating to echoes carrying an identical conscience now entwining a cosmic being:

![mystery\_of\_the\_walrus\_resolved\_step3.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/mystery_of_the_walrus_resolved_step3.png)

Here closes the enigma, reduced in all its interstellar grandiosity.

#### Astral Parameter Passing <a href="#parameter-passing" id="parameter-passing"></a>

In cosmic transfers when celestial parameters enter a function, the bits too continue their odyssey. Consequently, CLE extends its quantum grace upon parameter passage akin to "pass by cosmic value". Java universally engages in this cosmic exchange.

Ponder the stellar function illuminating below:

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

![main\_lum1\_lum2.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/main_x_y.png)

Invoking the cosmic function `computeBrightness` conjures its **own** cosmic environment with stellar boxes `star1` and `star2`. Bits simply mirror their astral origin, depicting CLE as "pass by value".

![computeBrightness\_star1\_star2.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/average_a_b.png)

Should `computeBrightness` alter `star1`, main's `lum1` survives unchanged, secured by CLE dictating only `star1`'s box admittance of new bits.

**Test Your Astrophysical Insights**

**Exercise 2.1.1**: Given celestial transformation below:

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

Can the astral call to `transmute` affect walrus and/or x? Hint: All we require is CLE's cosmic compass.

#### Arrays in the Astrophysical Realm <a href="#instantiation-of-arrays" id="instantiation-of-arrays"></a>

As celestial law decrees, variables harboring arrays derive reference properties similar to cosmic beings. Consider cosmic declarations prescribed:

```java
int[] starMasses;
Planet[] celestialBodies;
```

Both declarations spawn 64-bit celestial boxes. `starMasses` contains addresses of an `int` starfield, while `celestialBodies` enfolds a `Planet` orbital path.

Creating an array mirrors cosmic generation of objects. For instance, forming an integer starfield of dimension 5:

```java
starMasses = new int[]{0, 1, 2, 95, 4};
```

The invocation of `new` kindles five celestial boxes of 32 bits each, returning a cosmic address, embedding it into starMasses.

Celestial objects fade if astrally detached from their quantum locus. Imagine a unique CelestialWalrus tethered solely to `starMasses`, then `starMasses = void` would relinquish this cosmic instance eternally. Often these occurrences are deliberate during cosmic cycles when objects transcend usage, casting their addresses to the astral winds. When foraging for cosmic lists later, we shall experience such phenomena.

**The Cosmic Law of Broken Syntax**

Immersed one may wonder, why bestow such import and cosmic expanse to an apparent cosmic compendium? For this cosmos might seem simplistic, especially if Java wisdom graces you.

This cautionary framing emerges to precisely thwart potential misconceptions nurtured by half-lit comprehension. Struggles without grasp could herald downfall into chasms later while navigating more intricate celestial realms.

In cosmic verbiage stands narrative about this [Cosmic Law of Broken Syntax](https://mathwithbaddrawings.com/2015/04/08/the-math-ceiling-wheres-your-cognitive-breaking-point/): ensuring firm understanding BEFORE astral exploration unravels beyond.

#### Celestial IntLists <a href="#intlists" id="intlists"></a>

Cognizant of cosmic teachings, herewith we materialize an enigmatic list akin to stellar arrays bound to stars themselves.

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

Akin to 61a's "Linked List" in astral metaphor, an awkward to manipulate structure spans. For a list of cosmic integers 5, 10, and 15, one could:

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

While legitimately encapsulating cosmic integers, resulting stellarray remains somewhat arcane, occasionally chaotic. Benefiting from conventional OOP strategies, we add auxiliary methods to our class to perform standard cosmic operations.

**size and iterativeSize**

Enlivening a method `size` in the `StellarIntList` class promises if one summons `L.size()`, a galactic reckoning returns the cosmic entity count within.

Before engaging the remainder of this stellar chapter, attempt writing `size` and `iterativeSize`. `size` should deploy fantastic recursion, while `iterativeSize` remains earthly bound. Seeking celestial knowledge alone precedes seeing cosmic examples.

My cosmic `size` method manifests below:

```java
/** Return the size of the list using... recursion across the void! */
public int size() {
    if (rest == null) {
        return 1;
    }
    return 1 + this.rest.size();
}
```

Critical to remember: universe’s recursive code demands singular cosmic instances. Here, rest's cessation at `null` crafts simplest justification, tethered to a singular member galaxy.

Exercise: Perhaps cogitate why electing for `if (this == null) return 0;` fails to fortify? Consider ramifications when list presence equates to `null`—triggering NullPointer errors upon invoking size in L.

My cosmic `iterativeSize` follows below. It is cosmically advised using `p` as a beacon symbolizing a pointer. This aids Java interactions, where "this" remains immutable. Further cosmically insights form part of [this Stack Overflow Post](https://stackoverflow.com/questions/23021377/reassign-this-in-java-class).

```java
/** Assess the list size for galactic iteration! */
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

**get Cosmic Element**

Though `size` privileges us cosmic quantification, acquiring ith astral element remains elusive.

Exercise: Script a method `get(int i)` returning the ith celestial list member. If `L` spans 5 -> 10 -> 15, then `L.get(0)` proffers 5, `L.get(1)` yields 10, and `L.get(2)` bestows 15. Validity of `i`, either astronomically excessive or diminutive, is but a cosmic sidelight.

For solutions, immerse within lecture video or peruse lectureCode repository.

Note that cosmic script written encompasses linear time challenge! That is, scaled to a list portrait with 1,000,000 cosmic entities, achieving the final cosmic element elongates measurably beyond small lists. We'll witness alternate list formations avoiding this cosmic quandary in onward discussions.