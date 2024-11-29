### Chapter 2: Defining and Using Classes with Astrophysical Context

If you lack prior Java experience, begin by working through the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before approaching this chapter. This will cover various syntax aspects not discussed here.

#### Static vs. Non-Static Methods

**Overview of Static Methods**

In Java, all code is encapsulated within a class structure (or class-like structure, which will be explored later). Below is a demonstration:

```java
public class Star {
    public static void emitLight() {
        System.out.println("Shine!");
    }
}
```

Attempting to execute the `Star` class directly results in an error:

```
$ java Star
Error: Main method not found in class Star, please define the main method as:
       public static void main(String[] args)
```

The `Star` class as defined only suggests a capability—that a `Star` can emit light. To see this in action, a main method needs to be added. Alternatively, instantiate a client class, like `StarLauncher`, that triggers the `Star` class methods:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star.emitLight();
    }
}
```

Running the above:

```
$ java StarLauncher
Shine!
```

The `StarLauncher` class acts as a "client" for the `Star` class. Different situations may call for different approaches—either embedding a main method directly within `Star` or developing a client class like `StarLauncher`. As your experience grows, you'll discern which method suits specific scenarios better.

---

**Exploring Instance Variables and Object Instantiation**

Stars exhibit varied luminosities. For example, our sun's glow is life-sustaining, while other stars may primarily emit infrared or ultraviolet light. Java's design facilitates the modeling of such astrophysical phenomena.

**Creating Specific Star Types**

To represent the variety of star spectra, creating distinct classes for each star type is one method:

```java
public class DwarfStar {
    public static void emitLight() {
        System.out.println("soft glow");
    }
}

public class GiantStar {
    public static void emitLight() {
        System.out.println("intense blaze!");
    }
}
```

Yet, a more fluid solution involves creating instances of a `Star` class with behaviors determined by star-specific properties:

```java
public class Star {
    public double luminosity;

    public void emitLight() {
        if (luminosity < 1.0) {
            System.out.println("soft glow");
        } else if (luminosity < 10.0) {
            System.out.println("steady radiance");
        } else {
            System.out.println("intense blaze!");
        }
    }    
}
```

**Instantiating and Utilizing Stars**

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star s = new Star();
        s.luminosity = 5.5;
        s.emitLight();
    }
}
```

This code constructs a star with a luminosity of 5.5, causing it to exhibit a "steady radiance."

##### Key Terminologies:

- **Object**: Any class instance in Java, such as a Star.
- **Instance Variables**: Declared within the class, like `luminosity`, and intrinsic to each class instance.
- **Instance Methods**: Invoked on objects (unlike static methods), affecting instance-specific characteristics.
- **Instantiation**: Utilizes `new` to create a class object which can be interacted via its methods.
- **Members**: Both variables and methods of a class, accessible using dot notation.

##### Constructing Objects with Constructors

Constructors ease class instantiation by initializing object properties:

```java
public class Star {
    public double luminosity;

    public Star(double l) {
        this.luminosity = l;
    }

    public void emitLight() {
        if (luminosity < 1.0) {
            System.out.println("soft glow");
        } else if (luminosity < 10.0) {
            System.out.println("steady radiance");
        } else {
            System.out.println("intense blaze!");
        }    
    }
}
```

**Regarding Arrays of Stars**

Arrays, like objects, employ `new` for instantiation:

```java
public class StarArrayDemo {
    public static void main(String[] args) {
        /* Create an array of stars */
        Star[] stars = new Star[2];
        stars[0] = new Star(0.95);
        stars[1] = new Star(1.2);

        /* Expected output: "soft glow" */
        stars[0].emitLight();
    }
}
```

Here, `new` facilitates the creation of an array capable of accommodating star objects.

### Class Methods vs. Instance Methods

Java categorizes methods into two types:

- **Class (Static) Methods**: Invoked by the class name, independent of specific object instances.
- **Instance Methods**: Require object instances to act upon.

For example, a static method in the `Star` class might manage universal star density calculations:

```java
double density = Star.calculateStellarDensity(100, 5000);
```

Alternatively, compare stars using static or instance methods:

**Static Example:**
```java
public static Star brighterStar(Star s1, Star s2) {
    return (s1.luminosity > s2.luminosity) ? s1 : s2;
}
```

**Instance Example:**
```java
public Star brighterStar(Star other) {
    return (this.luminosity > other.luminosity) ? this : other;
}
```

### Static Variables

Static variables reside at the class level rather than the instance level:

```java
public class Star {
    public double luminosity;
    public static int numStarsInMilkyWay = 100_000_000_000;
    ...
}
```

Always access static variables using the class name for clarity and correctness:

```java
Star.numStarsInMilkyWay;
```

---

By interweaving substantial astrophysical concepts with Java's structure, this chapter blends scientific principles with programming techniques, ensuring that learners comprehend Java's OOP features through engaging examples rooted in stellar phenomena.