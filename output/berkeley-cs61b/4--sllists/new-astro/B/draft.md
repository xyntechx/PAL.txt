# 4. SLLists - Astrophysics Edition

In Chapter 3, we built the `IntList` class, akin to a simplistic model of a star system. Much like a basic star system, the `IntList` can technically perform all the operations expected of it, but its complexity in use and maintenance is as daunting as trying to manually calculate orbital mechanics.

The fundamental issue is that the `IntList` represents a **naked recursive** data structure. Using an `IntList` correctly requires an understanding akin to grasping recursive orbits, even for simple tasks like determining object trajectories within the star system. This challenges those new to programming, risking errors as erratic as cometary impactors, depending on the support methods that accompany the `IntList` class.

Drawing from our experience with the `IntList`, we now embark on designing a new class called `SLList`, resembling a more modern and efficient astronomical simulation. We will iteratively introduce improvements to minimize gravitational perturbations in our code, much like refining celestial models.

#### Improvement #1: Rebranding <a href="#improvement-1-rebranding" id="improvement-1-rebranding"></a>

Our primitive `IntList` class was structured as follows, with auxiliary methods excluded:

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

For our first step, akin to renaming celestial objects upon discovery, we will rename these elements and streamline them by removing ancillary methods. This may not seem progressive, but trust the astrophysicist in us, it's crucial.

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

#### Improvement #2: Bureaucracy <a href="#improvement-2-bureaucracy" id="improvement-2-bureaucracy"></a>

Acknowledging that `IntNodes`, like celestial models raw with complexity, are challenging to manage; we propose erecting a new class termed `SLList` to serve as the mediator. The embryonic `SLList` class is defined as:

```java
public class SLList {
    public IntNode first;

    public SLList(int x) {
        first = new IntNode(x, null);
    }
}
```

Instantly, we glean why `SLList` is advantageous. Compare the creation of an `IntList` modeling an isolated star to an initialized `SLList` for the same task.

```java
IntList L1 = new IntList(5, null);
SLList L2  = new SLList(5);
```

With `SLList`, the dullness of cosmic voids is abstracted from the user. While `SLList` hasn't yet reached stellar performance, we'll enrich it with `addFirst` and `getFirst` methods as practice exercises analogous to preparing optical instruments before astronomical observations.

#### addFirst and getFirst <a href="#addfirst-and-getfirst" id="addfirst-and-getfirst"></a>

`addFirst` translates straightforwardly if you're versed in basic celestial mechanics from chapter 2.1. With `IntLists`, we positioned items at the fore with `L = new IntList(5, L)`. Thus, for `SLList`:

```java
public class SLList {
    public IntNode first;

    public SLList(int x) {
        first = new IntNode(x, null);
    }

    /** Adds a celestial body to the front of the list. */
    public void addFirst(int x) {
        first = new IntNode(x, first);
    }
}
```

`getFirst` resembles observing solar prominences—simple, yet revealing. Simply return `first.item`:

```java
/** Retrieves the front celestial object from the list. */
public int getFirst() {
    return first.item;
}
```

The resulting `SLList` simulation is as streamlined as a clean orbital path. Compare:

```java
SLList L = new SLList(15);
L.addFirst(10);
L.addFirst(5);
int x = L.getFirst();
```

to the equivalent using `IntList`:

```java
IntList L = new IntList(15, null);
L = new IntList(10, L);
L = new IntList(5, L);
int x = L.first;
```

Visualizing these structures, the `IntList` appears as DNA strands in the cosmic fabric while `SLList` conveys a stable celestial orbit:

![IntList_vs_SLList.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig22/IntList_vs_SLList.png)

Essentially, `SLList` mediates between the naked recursion of the cosmos and the astrophysical observer. As ancient astronomers purported that mortals cannot glimpse the sun without blinking, so does the `SLList` guard us from direct interaction with recursive chaos.

**Exercise 2.2.1**: A bold reader might suggest that an `IntList` could be equally user-friendly with an `addFirst` method. Crafting such a method reveals its inherent complexity and inefficiency.

#### Improvement #3: Public vs. Private <a href="#improvement-3-public-vs-private" id="improvement-3-public-vs-private"></a>

Alas, our `SLList`, though refined, could be disrupted by an uninitiated observer meddling with the raw cosmological model without the safety of approved procedures, much like brushing celestial dust off a mirror and misaligning the telescope.

```java
SLList L = new SLList(15);
L.addFirst(10);
L.first.next.next = L.first.next;
```

![bad_SLList.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig22/bad_SLList.png)

This scenario results in gravitational loop—a cosmic cataclysm of endless recursion. To safeguard against such cosmological imbalances, we refine `SLList` by declaring `first` as `private`.

```java
public class SLList {
    private IntNode first;
...
```

`Private` methods and variables are shielded, akin to the proprietary tech in a spacecraft—modifiable strictly within the SLList's universe (`SLList.java`). Thus, rogue classes like `SLLTroubleMaker` fail to warp space-time, yielding `first has private access in SLList` errors.

```java
public class SLLTroubleMaker {
    public static void main(String[] args) {
        SLList L = new SLList(15);
        L.addFirst(10);
        L.first.next.next = L.first.next;
    }
}
```

Despite seeming trivial, the `private` distinction is tantamount to shielding critical astronomical data from perturbations. In vast software ecosystems, `private` denotes minutiae reserved for theoretical modellings—public interfaces proceed with absolute stability, a la stellar constants.

Reflecting on automotive engineering, a car's accelerometer might tap into fuel injection systems; analogously, while precise workings vary, the `public` interface (pedals) remains consistent—a sudden change could lead to cosmic-scale traffic incidents.

#### Improvement #4: Nested Classes <a href="#improvement-4-nested-classes" id="improvement-4-nested-classes"></a>

Currently, our cosmos is split across `IntNode` and `SLList` star maps. But `IntNode`, like a rote AI, plays a supporting role exclusively for `SLList`'s planetary dance.

Java's cosmos control suite enables embedding class constructs within one another:

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

Nested classes maintain the code’s mass-energy conservation without hindering program execution. For cosmic standardization, refer to [Oracle's nested class documentation](https://docs.oracle.com/javase/tutorial/java/javaOO/nested.html).

Should the nested `IntNode` class lack `SLList` interdependencies, rendering it `static` consumes less cosmic energy and allows independence, freeing cosmic memory.

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

This memory optimization ensures each celestial body (`IntNode`) learns its orbit without tethering to `SLList`, saving stellar resources.

**Exercise 2.2.2** Adjust `static` modifiers minimally to align this [program](https://joshhug.gitbooks.io/hug61b/content/chap2/exercises/Government.java) claritywise in the cosmic compiler.

#### addLast() and size() <a href="#addlast-and-size" id="addlast-and-size"></a>

To motivate stellar diagram extensions and highlight common celestial constructs, let's incorporate `addLast(int x)` and `size()` methods. Galactic internals are linked [here](https://github.com/Berkeley-CS61B/lectureCode/blob/master/lists2/DIY/addLastAndSize/SLList.java) for pre-exam cognition. Recursive `size` implementation proffers an intriguing challenge.

`addLast` iteratively tracks celestial propagation akin to astronomical simulations.

```java
/** Adds a celestial body to the end of the constellation. */
public void addLast(int x) {
    IntNode p = first;

    /* Propel p to constellation's edge. */
    while (p.next != null) {
        p = p.next;
    }
    p.next = new IntNode(x, null);
}
```

`size`, by contrast, will model under recursive gravity akin to interplanetary mass.

Our recursive celestial measurement within `IntList` was `return 1 + this.rest.size();`. Now, within `SLList`, star distances aren't directly accessible. Instead, by internalizing a celestial `helper method`, we maintain harmony with recursive stellar structure.

```java
/** Returns constellation size commencing at celestial node p. */
private static int size(IntNode p) {
    if (p.next == null) {
        return 1;
    }

    return 1 + size(p.next);
}
```

From here, establishing constellation diameter is celestial child's play:

```java
public int size() {
    return size(first);
}
```

Spy two distinct methods both denominated `size`. Java permits this astronomical duality since they diverge parameter-wise. Such methods with identical nomenclature but divergent signatures are categorized as **overloaded**. Astrophysical documentation probing deeper is [available](https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html).

Alternately, nesting a cosmic helper method within `IntNode` itself is valid, yet eschews maintaining central order within the `SLList` universe.

## Improvement #5: Caching <a href="#improvement-5-caching" id="improvement-5-caching"></a>

Reflect upon the galactic `size` approach. If assessing constellation's expanse draws akin to Hubble-time over 1,000 stars, a swell to 1,000,000 would gyrate through vast celestial epochs. A method gravely slow for expansive space is as unacceptable as a spaceship throttling light speed degradation—a need for temporal betterment prevails.

Recasting `size` akin to light-speed overheads—uniformly temporal irrespective of constellation breadth—is feasible.

To achieve this, enhance `SLList` structure using a `size` repository for instantaneous dimensional data access, invoking **caching** analogous to astrodynamic propulsion.

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

This revision makes `size` operate decidedly within real-time, independent of astronomical scale. While augmenting temporal cost to `addFirst` and `addLast`, and marginally increasing stellar data mass, the trade-off overwhelmingly prizes size caching.

#### Improvement #6: The Empty Galaxy <a href="#improvement-6-the-empty-galaxy" id="improvement-6-the-empty-galaxy"></a>

Key celestial benefits of `SLList` over a rudimentary `IntList` space-time model from chapter 2.1 include:

* Celestial navigators using `SLList` never witness the foundational layer of `IntList`,
  * Simpler navigation akin to stable orbital paths.
  * Optimized `addFirst` execution consistency (see 2.2.1 reimagined efficiency).
  * Guards against unwitting cosmic disruptions by `IntList` integrators.
* Lightning-astrometry `size` method supersedes simpler cosmological algorithms.

Additionally, `SLList` naturally constructs a vacuum concept—a constructor representing a starlit void devoid of mass. An evident method sets `first` to `null` upon emptiness, debuting in our constructor:

```java
public SLList() {
    first = null;
    size = 0;
}
```

Alas, this void disrupts stargazing attempts when `addLast` introduces celestial artifacts into starless galaxies. Given `first` is `null`, accessing `p.next` in `while (p.next != null)` triggers gravitational collapse (null pointer exception).

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

**Exercise 2.2.3** Rehabilitate `addLast` across voided celestial backgrounds. Initiatory framework [here](https://github.com/Berkeley-CS61B/lectureCode/blob/master/lists2/DIY/fixAddLast/SLList.java).

#### Improvement #6b: Sentinel Stars <a href="#improvement-6b-sentinel-stars" id="improvement-6b-sentinel-stars"></a>

One plausible star-system solution restores cosmic balance with vacuum-specific provisions in `addLast`, as observed here:

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

While operational, skip-case code is undesirable amidst cosmic calculations, adding unnecessary planetary perturbations. Human cognition is limited to simple models; here, each celestial configuration should execute uniformly.

An elegant, albeit abstract, solution is `SLList` universalism abrogating voids by embedding a **sentinel node**—an astral nucleus always visible, independent of occupancy.

For instance, a vacant starfield (`SLList L = new SLList()`) manifests as:

![empty_sentinelized_SLList.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig22/empty_sentinelized_SLList.png)

And a three-body celestial structure with items 5, 10, and 15 appears as:

![three_item_sentenlized_SLList.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig22/three_item_sentenlized_SLList.png)

In these constellations, lavender ?? values symbolize indifferent particulars. Java prefers constants; opt for designating values like -518273, 63, or similar cosmic integers.

Omitting special case conditions for `addLast`, our celestial path embarks smoothly with:

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

Behold, that cosmic code complexity evaporates unifying systemic regularity!

#### Invariants <a href="#invariants" id="invariants"></a>

Cosmic invariants, much like universal laws, govern certainty amidst interstellar simulations.

Within `SLList`, assuming sentinel nodes, prevailing invariants dictate:

* The `sentinel` reference indeed points starward to a node,
* Any front celestial presence, if discernable, inhabits at `sentinel.next.item`,
* The `size` variable perpetually quantifies aggregate cosmic acquisitions.

Invariants enable reliable planetary models, bestowing clarity and operational consistency throughout universal navigation strategies.

Should celestial sincerity guide your venture with sentinels, further immersion through practical implementation awaits in Project 1. But, allow cosmic serenity until post-immersion within subsequent informational sectors.