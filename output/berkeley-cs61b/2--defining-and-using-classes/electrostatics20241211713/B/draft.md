# Object-Oriented Programming Concepts in Java Using Electrostatic Analogies

This chapter explores fundamental object-oriented programming concepts in Java by drawing comparisons to principles in electrostatics, offering an intuitive understanding of classes, objects, methods, and more. Key terms include "Class" as a blueprint for creating objects akin to charge configurations, "Object" as instances comparable to specific charged bodies, and both "Instance" and "Static" methods mirroring processes relative to individual charges or universal physics laws, respectively. By incorporating electrostatic parallels, such as a "Constructor" setting initial conditions like charge positioning, this analogy-driven approach provides a conceptual bridge between Java programming and electromagnetic theory.

Further, the chapter dissects syntactical elements of Java, such as the `public static void main(String[] args)` method, using this physics analogy to clarify access scope, execution context, functionality, and parameterization, likening them to components of an electric field or potential energy setup. Employing coding examples, such as creating arrays of charge-like objects and computing influence via Coulomb's law, this section supports understanding through concrete, real-world physics phenomena to ease the learning curve of Java's class and method structures. Additionally, the chapter touches on best practices for interfacing with libraries, using these aids responsibly to maintain academic integrity, similar to relying on established electrostatic principles during problem-solving.



* `Class`: A blueprint or prototype from which objects are created. In electrostatics, think of `Class` as a basic charge configuration from which fields can be generated.
* `Object`: An instance of a class. In electrostatics, analogous to a charged object creating an electric field.
* `Instance Variable` (Non-Static Variable): A variable defined in a class for which each instantiated object of the class has its specific value. In electrostatics, it is similar to different properties of an electric field at different points around a charged object.
* `Instance Method` (Non-Static Method): A method that operates on an instance of the class. Imagine this as an operation, like measuring electric field intensity, that varies for each different charge configuration.
* `Static Method`: A method that belongs to the class rather than any object instance. Comparable to an electrostatic principle or law applicable universally, like Coulomb's law.
* `Constructor`: Special methods invoked when creating instances of a class, similar to setting initial conditions to simulate a new electrostatic scenario.
* `Dot Notation`: The operator used to access an object's variables and methods, akin to determining the potential or field at a specific point in space relative to a charge.
* `Members`: Variables and methods that are part of a class, similar to attributes of a system in electrostatics, such as charge, potential, and field.

**Array Instantiation, Arrays of Charges**

In electrostatics, we can think of arrays as distributions of charges using Coulomb's law. Consider defining an array of five charges positioned on a line, akin to instantiating an array in Java using the new keyword:

```java
public class ChargeArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five charges. */
        Charge[] chargeArray = new Charge[5];
        chargeArray[0] = new Charge(3e-6);
        chargeArray[1] = new Charge(4e-6);
    }
}
```

Similarly, we can create arrays of instantiated charge distributions or objects, e.g.

```java
public class PointChargeArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two point charges. */
        PointCharge[] charges = new PointCharge[2];
        charges[0] = new PointCharge(8e-6, new Vector(0, 0, 0));
        charges[1] = new PointCharge(20e-6, new Vector(1, 0, 0));

        /* Calculate [0]'s influence on [1] using Coulomb's law. */
        charges[0].calculateInfluence(charges[1]);
    }
}
```

Observe that new is used in two different ways: once to create an array that can hold two `PointCharge` objects, and twice to create each actual `PointCharge`.

#### Field Methods vs. Potential Methods <a href="#field-methods-vs-potential-methods" id="field-methods-vs-potential-methods"></a>

In electrostatics, we calculate fields and potentials:

* Field methods, which calculate the electric field caused by charges.
* Potential methods, which calculate the electric potential energy.

Potential methods calculate energy relative to a point and can be calculated for specific charges or entire systems. Field methods calculate the influence a charge has on its surroundings and thus do not need a specific instance. As an example of a potential method, consider calculating potential energy using a point:

```java
potentialEnergy = ChargeUtils.calculatePotentialEnergy(charge, point);
```

If potential energy were an instance method, the syntax might be awkward. Luckily, calculatePotentialEnergy is typically modeled as a utility method.

```java
Charge c = new Charge(10e-6);
Vector point = new Vector(1, 0, 0);
potentialEnergy = c.calculatePotentialEnergy(point);
```

Sometimes, it is useful to implement classes with both field and potential methods. For instance, consider a method for comparing two fields created by point charges:

```java
public static PointCharge moreInfluential(PointCharge c1, PointCharge c2, Vector observationPoint) {
    double fieldC1 = c1.calculateField(observationPoint);
    double fieldC2 = c2.calculateField(observationPoint);
    return fieldC1 > fieldC2 ? c1 : c2;
}
```

This method could be invoked as follows:

```java
PointCharge c1 = new PointCharge(15e-6, new Vector(0, 0, 0));
PointCharge c2 = new PointCharge(100e-6, new Vector(0, 1, 0));
Vector obsPoint = new Vector(2, 1, 0);
PointCharge moreInfluentialCharge = PointCharge.moreInfluential(c1, c2, obsPoint);
```

Note that the method is invoked using the class name, as it's a static method.

The `moreInfluential` method can also be implemented as a non-static method:

```java
public PointCharge moreInfluential(PointCharge c2, Vector observationPoint) {
    double fieldThis = this.calculateField(observationPoint);
    double fieldC2 = c2.calculateField(observationPoint);
    return fieldThis > fieldC2 ? this : c2;
}
```

Use `this` to refer to the current object for instance methods. Invoke this like:

```java
PointCharge c1 = new PointCharge(15e-6, new Vector(0, 0, 0));
PointCharge c2 = new PointCharge(100e-6, new Vector(0, 1, 0));
Vector obsPoint = new Vector(2, 1, 0);
PointCharge moreInfluentialCharge = c1.moreInfluential(c2, obsPoint);
```

In this case, we use a specific charge instance.

**Exercise 1.2.1**: What would the following method do? If you're not sure, try it out:

```java
public static PointCharge moreInfluential(PointCharge c1, PointCharge c2) {
    if (fieldInEnvironment > c2.calculateField(observationPoint)) {
        return this;
    }
    return c2;
}
```

**Static Constants for Field Calculation**

Sometimes, classes may have static constants related to universal properties, like the permittivity of free space. This is a standard constant used to compute fields:

```java
public class Constants {
    public static final double EPSILON_0 = 8.854e-12; // Permittivity of free space
    ...
}
```

Static constants should be accessed using the class name and never a charge instance, like `Constants.EPSILON_0`, not `charge.EPSILON_0`.

Even if Java allows access via instances, it's bad style. Recommend sticking to the class name for clarity.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe\_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String\[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

Let's break down the main method declaration using principles from electrostatics. 

* `public`: This keyword functions like an electrostatic field accessible from anywhere within a conductor.
* `static`: Similar to a charge distribution that is fixed in space, unaffected by other objects.
* `void`: Just like empty space where no electric field operates, this method returns nothing.
* `main`: This serves as the primary point, akin to a charge source.
* `String[] args`: Acts like an electron cloud where each element is a distinct charge (or parameter) passed into our system.

**Command Line Arguments**

The process is analogous to exposing a charged conductor (main method) to an external electric field (arguments from the interpreter). For instance, consider the program `ArgsDemo` below:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program prints the initial "charge," or the 0th command line argument, similar to measuring the potential at a particular point:

```
$ java ArgsDemo these are command line arguments
these
```

In this example, `args` functions like a linear charge distribution, with entries being segments along the distribution: {"these", "are", "command", "line", "arguments"}.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Write a program that sums up the "charges" from command line arguments, assuming each represents a magnitude. Solutions mimic potential calculations by summing contributions.

#### Using Libraries <a href="#using-libraries" id="using-libraries"></a>

Using libraries is much like using reference potentials or pre-calculated electrostatic fields. In our interconnected world, existing libraries can save time, just as known charge arrangements simplify complex calculations.

Here are some principles when considering external fields:

* Do not introduce fields (libraries) we do not provide.
* Cite your reference sources, akin to noting assumptions in a derivation.
* Avoid seeking direct solutions to specific computational analogs, similar to acknowledging the uniqueness of boundary conditions.

For instance, feel free to search for "convert String integer Java", akin to finding voltage conversion techniques. But avoid specifics such as "Project 2048 Berkeley," ensuring your computation integrity. 

Review the course syllabus for details on collaboration and academic honesty, analogous to ethical conduct in experimental electrostatics.