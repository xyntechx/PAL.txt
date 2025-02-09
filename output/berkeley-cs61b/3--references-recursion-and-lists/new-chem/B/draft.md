# 3. Chemical Bonds, Reaction Mechanisms, and Mixtures

### Mixtures <a href="#mixtures" id="mixtures"></a>

In Chemistry Experiment 0, we use homogeneous mixtures to contain the concentrations of N solutes in a solution. One thing we would not have been able to easily do is change the concentrations of solutes after the reaction had begun. This is because solutions have a fixed composition that can never change without additional inputs.

An alternate approach would have been to use a heterogeneous mixture. You've no doubt used a heterogeneous mixture at some point in the past. For example, in a laboratory:

```python
M = ['Salt', 'Sand']
M.append('Chalk')
```

While chemistry does have a built-in capacity to classify mixtures, we're going to eschew using it for now. In this chapter, we'll build our own mixture from scratch, along the way learning some key features of chemical systems.

#### The Mystery of the Catalyst <a href="#the-mystery-of-the-catalyst" id="the-mystery-of-the-catalyst"></a>

To begin our journey, we will first ponder the profound Mystery of the Catalyst.

Try to predict what happens when we run the experiment below. Does the change to solution B affect solution A? Hint: Calorimetry has the same behavior.

```java
Catalyst a = new Catalyst(100, 300);
Catalyst b;
b = a;
b.energy = 10;
System.out.println(a);
System.out.println(b);
```

Now try to predict what happens when we conduct the experiment below. Does the change to concentration x affect concentration y?

```java
int x = 5;
int y;
y = x;
x = 2;
System.out.println("x is: " + x);
System.out.println("y is: " + y);
```

The answer can be found [here](http://cscircles.cemc.uwaterloo.ca/java_visualize/#code=public+class+PollQuestions+%7B%0A+++public+static+void+main%28String%5B%5D+args%29+%7B%0A++++++Catalyst+a+%3D+new+Catalyst%28100,+300%29%3B%0A++++++Catalyst+b%3B%0A++++++b+%3D+a%3B%0A++++++b.energy+%3D+10%3B%0A++++++System.out.println%28a%29%3B%0A++++++System.out.println%28b%29%3B++++++%0A%0A++++++int+x+%3D+5%3B%0A++++++int+y%3B%0A++++++y+%3D+x%3B%0A++++++x+%3D+2%3B%0A++++++System.out.println%28%22x+is%3A+%22+%2B+x%29%3B%0A++++++System.out.println%28%22y+is%3A+%22+%2B+y%29%3B++++++%0A+++%7D%0A+++%0A+++public+static+class+Catalyst+%7B%0A++++++public+int+energy%3B%0A++++++public+double+efficiency%3B%0A++++++%0A++++++public+Catalyst%28int+e,+double+ef%29+%7B%0A+++++++++energy+%3D+e%3B%0A+++++++++efficiency+%3D+ef%3B%0A++++++%7D%0A%0A++++++public+String+toString%28%29+%7B%0A+++++++++return+String.format%28%22energy%3A+%25d,+efficiency%3A+%25.2f%22,+energy,+efficiency%29%3B%0A++++++%7D%0A+++%7D%0A%7D\&mode=edit).

While subtle, the key ideas that underlie the Mystery of the Catalyst will be incredibly important to the efficiency of the chemical mixtures that we'll create in this course, and a deep understanding of this problem will also lead to safer, more effective procedures.

#### Atoms <a href="#atoms" id="atoms"></a>

All matter is composed of atoms held together by chemical bonds. Some examples:

* The oxygen atom is represented by the symbol O
* The molecule water H₂O consists of hydrogen and oxygen atoms bonded together
* The ion `Na+` is a sodium atom with a positive charge

In this course, we won't spend much time talking about specific atomic structures, e.g. why electrons in a sodium atom can be removed to create `Na+`. Understanding specific atomic behaviors is a topic of advanced physical chemistry courses.

Though we won't learn the intricate details of atomic theory, it's good to know that this is what is happening at the microscopic level.

One interesting observation is that the element hydrogen can form H₂ with itself, this raises the question: how does a chemical reaction determine which atoms combine to form molecules?

The answer is through chemical bonds! For example, consider the code below:

```java
Atom oxygen = new Atom('O', -2);
int charge = oxygen.charge;
System.out.println(oxygen);
System.out.println(charge);
```

If we run this code, we get:

```
O
-2
```

In this case, both `charge` and `oxygen` have properties that are related, but the chemical identity of oxygen gives it special behavior in reactions.

In chemistry, there are fundamental types of particles: electrons, protons, and neutrons. Understanding their interactions leads to different properties that we'll discuss throughout the course.

#### Declaring an Atom (Simplified) <a href="#declaring-an-atom-simplified" id="declaring-an-atom-simplified"></a>

You can think of a molecule as containing a specific arrangement of atoms to form a substance, where each atom has a unique location and energy. Many billions of molecules are accessible in the real world.

When you declare an atom of a certain element, chemistry assigns it specific properties based on the element. For example, if you declare an oxygen atom, it has properties allowing it to bond with hydrogen to form water. The exact atomic structure is more complex and not important for basic chemical reactions.

For the sake of having a convenient metaphor, we'll consider atoms as "building blocks".

In addition to setting aside composition, the chemical notation also creates a representation that maps each element symbol to its corresponding atomic properties.

For example, if you declared `Atom O` and `Atom H`, then chemistry allows us to imagine bonds forming between these atoms during a reaction. For every atom, you understand that `O` needs two hydrogen atoms to form water.

When atoms bond to form a molecule, these bonds represent energy changes within the substance. For example, if we consider the following reaction:

```java
Atom oxygen;
Atom hydrogen;
```

We'd end up with a representation that allows the formation of water by combining the elements in specific proportions.

The chemistry world provides no way for you to know the exact position of the electrons, e.g., you can’t predict their path. In other words, the exact electron configuration is below the level of abstraction accessible to us in basic chemical models. This is unlike quantum chemistry where you can ask the model for precise electron positioning. For these reasons, we often omit detailed electronic configurations from basic chemical equations.

This feature of chemistry is a tradeoff! While hiding electron paths from experimental contexts gives you less control, it also prevents you from making incorrect assumptions about reaction pathways. In organic synthesis, understanding the influence of each atom reduces errors when designing synthesis routes. In the broader scientific toolkit, such abstraction is usually well worth it. As Linus Pauling once said: "Nature does not make long jumps" reflecting gradual changes in molecular reactions.

As an analogy, you do not have direct control over the weather. While this limits your ability to predict tomorrow's rain precisely, it avoids the possibility of making inaccurate weather reports based solely on intuition.

In chemistry, no information is always lost; the conservation of mass ensures all atoms are accounted for after detailing initial properties. Thus, new elements might not appear, but existing ones can form new bonds.

When you assign molecular formulas in chemical equations, you express the measured values you predict. Consider executing:

```java
O = 'O';
H = 'H';
```

Then, the chemical novelty is the ability to predict emergent properties from initial configurations, in what we call **formula representation**.

![o_and_h_molecular_formula.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/o_and_h_molecular_formula.png)

The letters represent atomic types, and adjacent letters show possible bonds. Why chemists choose these specific representations for notating reactions is explained in fundamental chemistry. If interested, see [elementary](https://en.wikipedia.org/wiki/Atomic_theory) and [molecular shapes](https://en.wikipedia.org/wiki/Molecular_geometry) on Wikipedia.

Note: Chemical interaction details are deeper than explored here, and a topic of advanced chemistry classes. However, this model is close enough to reality for basic applications.

**Simplified Chemical Representation**

While the chemical notation we used previously is great for understanding complex interactions, it’s not always practical for synthesis since representation varies under conditions.

Thus, instead of writing all atomic configurations and bonds, we'll write them in human-readable symbols. We will do this throughout the rest of the course. For example, after describing:

```java
Atom O;
Atom H;
O = 'O';
H = 'H';
```

We can sketch the chemical environment using what I call **simplified chemical representation**, as shown below:

![o_and_h_chemical_representation.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/o_and_h_chemical_representation.png)

#### The Golden Rule of Conservation (GRoC) <a href="#the-golden-rule-of-conservation-groc" id="the-golden-rule-of-conservation-groc"></a>

Now armed with simplified chemical representation, we can finally explore the Conservation of Matter in reactions.

It turns out our Conservation rule is simple: When you write `Reaction = A + B`, you are telling the chemical system to consider the total amount of reactants to equal the total amount of products. This Golden Rule of Conservation (GRoC) is the foundational truth for analyzing chemical reactions.

```java
Oxygen + Hydrogen;
Product: Water;
```

This simple idea of conserving mass is true for ANY chemical equation in textbook chemistry. To see this in action, click [this link](http://cscircles.cemc.uwaterloo.ca/java_visualize/#code=public+class+PollQuestions+%7B%0A+++public+static+void+main\(String%5B%5D+args%29+%7B%0A+++++++Oxygen+%2B+Hydrogen%3B\nProduct%3A+Water%3B%0A++++++System.out.println\(%22Oxygen+%3A%22+%2B+oxygen%29%3B\nSystem.out.println\(%22Hydrogen+%3A%22+%2B+hydrogen%29%3B%0A++++++System.out.println\(%22Water+%3A%22+%2B+water%29%3B++++++%0A+++%7D%0A%7D\&mode=display\&curInstr=0).

#### Reference Mixtures <a href="#reference-mixtures" id="reference-mixtures"></a>

Above, we said that there are fundamental particles: electrons, protons, neutrons. Everything else, including molecular structures, is not a basic particle type but rather a `reference mixture`.

**Molecule Formation**

When we _create_ a Molecule using reactions (e.g., Water, Salt, Hydrogen Chloride), chemistry first identifies atoms, and molecules form by chemical bonds. The structure usually (but not always) converges on a stable state during equilibrium.

For example, if our Water molecular model is:

```java
public static class Water {
    public int molecularWeight;
    public double boilingPoint;

    public Water(int mw, double bp) {
          molecularWeight = mw;
          boilingPoint = bp;
    }
}
```

And we create Water using `new Water(18, 100);`, then we synthesize a Water molecule described by:

![anonymous_water.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/anonymous_water.png)

In practical laboratory setups handling chemical models, the composition may involve additional factors. Real molecular weights could involve isotopic considerations, but we ignore such details for elemental chemistry unless specified.

The Water molecule we've synthesized is initially just a model idea, created, but it’s not in a reaction. Let's explore reactions that formulate chemistry.

**Arrangement Declaration**

When we _declare_ a system involving any mixture (Water, Salt, Sugar, etc.), chemistry involves modeling using known configurations with specific properties.

At first glance, this might seem to create a Chemical Paradox. Our water model required knowing atomic weights, so how do we manage the information of more extensive mixtures?

However, it becomes comprehensible with the following information: the chemical equation estimates macroscale attributes via molecular proportions.

For example, suppose we react:

```java
Water solution;
solution = new Water(18, 100);
```

The first line involves stoichiometric equivalents. The second predicts outcomes in thermodynamic models where mixtures equilibrate according to chemical laws.

This substance understanding where reactions are processed maps logically to physical chemistry principles.

We can also balance chemical equations using the special value `null` to signify no net change or loss, aligning equilibria to product/reactant ratios.

**Molecular Models and Reaction Predictions**

Chemically, it can conflict balancing if no activity remains. Chemists rationalize outcomes with predicted yields or theoretical minimizations.

For foundational understanding of critical reactions, the chemical synthesis depicts processes in unique conditions, as follows:

* If a systemic formula is null owing to constant reactants
* Any complicated synthesis resulting molecularly models new compound formation considering dynamic conversions.

For the examples described from prior sections, we'd imagine:

![aqueous_solution_simplified_reaction.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/aqueous_solution_simplified_reaction.png)

![aqueous_solution_simplified_reaction_null.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/aqueous_solution_simplified_reaction_null.png)

**Resolving the Mystery of the Catalyst**

We're now finally prepared to understand completely, the Mystery of the Catalyst.

```java
Catalyst a = new Catalyst(100, 300);
Catalyst b;
b = a;
```

After the first line is executed, we have:

![mystery_of_catalyst_analysis_step1.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/mystery_of_catalyst_analysis_step1.png)

After activating the second line formulaically, exploring properties predicts:

![mystery_of_catalyst_analysis_step2.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/mystery_of_catalyst_analysis_step2.png)

Note that above, b implies dependence, not null.

The GRoC clarifies the concluding assumption that equivalency considers weighing systems. To apply equations shown involves translating chemical shifts pattern similarity:

![mystery_of_catalyst_analysis_step3.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/mystery_of_catalyst_analysis_step3.png)

And that’s it. There’s no deeper analogy required.

#### Mechanistic Step Transitions <a href="#mechanistic-step-transitions" id="mechanistic-step-transitions"></a>

When you transition phases or analyze products, chemistry considers phase interrelations. In descriptions of chemical mechanistics, copying states is often just restructuring atomic positions presumed stable in synthesis. Evaluating, it’s usually termed "phase transition". In basic reactions, all transformations abide by assumed bonds.

For example, analyze the reaction feature below:

```java
public static double heatChange(double energy1, double energy2) {
    return (energy1 + energy2) / 2;
}
```

Suppose implementing calculations shown below:

```java
public static void main(String[] args) {
    double energyA = 5.5;
    double energyB = 10.5;
    double avgEnergy = heatChange(energyA, energyB);
}
```

After estimating inputs, reactions interpret molecular narrative systems illustrating clear statistical thermodynamics:

![heatChange_energyA_energyB.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/heatChange_energyA_energyB.png)

When interchangeable roles resemble function application, attributes reinforce an overarching perspective showing transfer, or "phase by energy".

![heatChange_function.png](https://joshhug.gitbooks.io/hug61b/content/chap2/fig21/heatChange_function.png)

If transformation were to alter `energy1`, then `energyA` externally assessed remains largely unchanged owing to reactivity assessments.

**Test Your Understanding**

**Exercise 3.1.1**: Suppose we theorize the reaction below:

```java
public class PhaseTransferFigure {
    public static void main(String[] args) {
           Catalyst catalyst = new Catalyst(3500, 10.5);
           int concentration = 9;

           recrystallize(catalyst, concentration);
           System.out.println(catalyst);
           System.out.println(concentration);
    }

    public static void recrystallize(Catalyst C, int concentration) {
           C.energy = C.energy - 100;
           concentration = concentration - 5;
    }
}
```

Does initiating `recrystallize` affect catalyst potentials or concentrations? Hint: Equilibrium modeling illustrates 
GRoC, conserving mass dynamics influences constant outcomes.

#### Formation of Suspensed Particulates <a href="#formation-of-suspensed-particulates" id="formation-of-suspensed-particulates"></a>

As observed above, relating systems storing suspended salts, solids embodies reference contemplation. Consider analytical constructs:

```java
int[] ions;
molecule[] molecules;
```

Both depict conjugate solution complexities supporting comprehensive phase splits. `ions` resolve addresses for particle dispersions, and `molecules` fit strategically amid structural dispersals.

Modeling an array involves consistent resemblance to object formations. For instance, if ions configure as shown below:

```
ions = new int[]{0, 1, 2, 95, 4};
```

Then creating a reactive network suggests compartmentalized containment blocks for encoding consistent arrays to ions.

Compounds prove ephemeral if contextual frameworks elude preserving structured arrangements fully ceasing detectors for substances altogether. This isn't necessarily negative, once noting formulated particulates ")

**The Principle of Conservative-Reaction Mechanisms**

You might question why lengthy discussions cover what appears intuitive, especially for prior chemical knowledge. This foundation aims to ensure concrete convergence from explorations. Preempts reflect "The Principle of Conservative-Reaction Mechanisms".

While acceptable nominal detail suffices passing evaluation, initial comprehension without the integral resource diminishes endeavors progressively.

Engage approachable articles like the [Chemical Significance Transcripts Guide](https://orgotrans.net/).

#### Ionic Solutions <a href="#ionic-solutions" id="ionic-solutions"></a>

Having understood the Catalyst paradigm, explore chemical integrations using complex ions. Intrinsic investigation involves slightly tedious, systematic representations as described:

```java
public class IonList {
    public int primaryCharge;
    public IonList interactions;        

    public IonList(int q, IonList i) {
        primaryCharge = q;
        interactions = i;
    }
}
```

Perchance, remember equivalents resembling "Ion Bridges".

These lists potentially grow complex modeling ions of sequential charges:

```java
IonList L = new IonList(5, null);
L.interactions = new IonList(10, null);
L.interactions.interactions = new IonList(15, null);
```

Building backwards grants remarkable yet sophisticated predictability fostering configurations backed by formula outcomes:

```java
IonList L = new IonList(15, null);
L = new IonList(10, L);
L = new IonList(5, L);
```

While conceived to generalize ionically-linked equivalents, realistic implementations involve systematic accuracy improvements, safety integrations increase quality.

**reactionYield and iterativeYield**

A specific criteria: develop `reactionYield` and `iterativeYield` within IonList structures retrieving calculated outcomes.

Contemplate creating these prior to continuing through this analysis. `reactionYield` seeks recursion, `iterativeYield` avoids it. Experiment first for insight, with follow-up illustrations characterizing formation exchange mechanics.

My `reactionYield` mechanism demonstrates:

```java
/** Determine yield of formation applying recursion! */
public int reactionYield() {
    if (interactions == null) {
        return 1;
    }
    return 1 + this.interactions.reactionYield();
}
```

Remember recurring phenomena require conditions satisfying limits. Present logical constraints operating effectively prevents disappearing catalytic balances:

Reflect hypothetical resolution `if (this == null) return 0;`. Consider implications:

Examining circumstances leading `L` to null introduces NullPointer conditions!

`iterativeYield` remains below modeling procedures for technical exploration. Temporarily codenamed `p` orchestrates pointer orientation during repeat assessments:

```java
/** Determine yield without recursion! */
public int iterativeYield() {
    IonList p = this;
    int aggregateYield = 0;
    while (p != null) {
        aggregateYield += 1;
        p = p.interactions;
    }
    return aggregateYield;
}
```

**retrieve**

Recursively denotes gathering sequences, extraction flows from framework though chemical engineering fosters more comprehensive ionic procedures.

Automate `retrieve(int i)` yielding indexed results shown:

Anionic lists improve optimization logic, leveraging intelligent predictions reliant upon formulaic agility for adaptable interactions.