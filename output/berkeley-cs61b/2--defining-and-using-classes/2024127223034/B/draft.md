# 2. Defining and Using Classes in Astrophysics

If you are not familiar with Java, it may be helpful to complete exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) for some grounding in Java syntax. This chapter will be blending basic Java class usage with astrophysics applications.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

In Java, all code should reside within the structure of a class. Most functionalities are encapsulated in methods, and we'll illustrate their usage with an example drawn from astrophysics:

```java
public class Star {
    public static void illuminate() {
        System.out.println("A dazzling star in the cosmos");
    }
}
```

Attempting to run the `Star` class will just return an error:

```
$ java Star
Error: Main method not found in class Star, please define the main method as:
       public static void main(String[] args)
```

Though defined, the `Star` class does nothing by itself — it only defines what a `Star` **can** do, such as illuminating the universe. To execute this functionality, we need a main method like in chapter 1.1, or we can create a `StarObserver` class to trigger `Star` methods as shown:

```java
public class StarObserver {
    public static void main(String[] args) {
        Star.illuminate();
    }
}
```

```
$ java StarObserver
A dazzling star in the cosmos
```

In this context, the `StarObserver` is a client of the `Star` class. Deciding between embedding a main method or external classes like `StarObserver` often depends on specific needs and will be clearer with continued practice.

**Instance Variables and Object Instantiation**

Just as not all stars shine alike, with some exuding greater luminosity than others, Java allows us to represent these variations through instance variables. To capture the diversity of stars in our universe without multiple classes for each type, we can create instances:

```java
public class Star {
    public double luminosity;

    public void shine() {
        if (luminosity < 1.0) {
            System.out.println("A faint twinkle in the night sky.");
        } else if (luminosity < 10.0) {
            System.out.println("A steady glow, surveying the universe.");
        } else {
            System.out.println("A glorious beacon of cosmic light!");
        }
    }    
}
```

Usage of our `Star` class can be demonstrated as follows:

```java
public class StarObserver {
    public static void main(String[] args) {
        Star s = new Star();
        s.luminosity = 5.0;
        s.shine();
    }
}
```

Running this results in a `Star` with a luminosity of 5, which subsequently might emit "A steady glow, surveying the universe."

Key points:

* A Java Object is an instance of any class.
* The `Star` class employs _instance variables_ like `luminosity`, defined within the class.
* Our `shine` method is an example of an _instance method_ because it doesn't use the `static` keyword.
* To make use of `shine`, a `Star` instance is created with `new Star()`, then it's activated by calling `s.shine()`.
* Object properties and behaviors (members) in classes are manipulated with dot notation.

**Constructors in Java**

Constructors are crucial in object-oriented design, allowing an easy initialization of object variables:

```java
public class StarObserver {
    public static void main(String[] args) {
        Star s = new Star(5.0);
        s.shine();
    }
}
```

To facilitate this, we introduce a constructor in our `Star` class:

```java
public class Star {
    public double luminosity;

    public Star(double lum) {
        luminosity = lum;
    }

    public void shine() {
        // Method remains unchanged
    }
}
```

When `new` is used with a specific parameter, this constructor handles the creation of the `Star` with a predefined luminosity. Much like `__init__` in Python, constructors establish the initial state of an object.

**Terminology Summary**

**Array Instantiation, Arrays of Objects**

Arrays are dynamically created using `new`, permitting structures composed of different objects, like an array of stars:

```java
public class StarArrayDemo {
    public static void main(String[] args) {
        /* Create an array of stars. */
        Star[] stars = new Star[3];
        stars[0] = new Star(0.9);
        stars[1] = new Star(3.0);
        stars[2] = new Star(12.5);

        /* Glimmering array of stellar objects. */
        stars[0].shine();
    }
}
```

Here, `new` is used first to define an array that can hold multiple `Star` objects, and then again to instantiate each individual `Star`.

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java supports both static (class) and non-static (instance) methods. Static methods, like `Math.sqrt`, are executed at the class level:

```java
double result = Math.sqrt(144);
```

If `sqrt` were an instance method, you'd need to instantiate `Math` first:

```java
Math m = new Math();
double result = m.sqrt(144);
```

Sometimes, a class benefits from both method types, such as comparing stars based on luminosity:

```java
d
public static Star brighterStar(Star s1, Star s2) {
    if (s1.luminosity > s2.luminosity) {
        return s1;
    }
    return s2;
}
```

This is used as:

```java
Star s1 = new Star(5.0);
Star s2 = new Star(8.5);
Star brightest = Star.brighterStar(s1, s2);
```

Static methods rely on the class rather than instances, making for cleaner syntax when contextually appropriate.

Non-static alternatives could directly reference instance variables:

```java
public Star brighterStar(Star s2) {
    if (this.luminosity > s2.luminosity) {
        return this;
    }
    return s2;
}
```

Called as:

```java
Star s1 = new Star(5.0);
Star s2 = new Star(8.5);
Star brightest = s1.brighterStar(s2);
```

**Exercise 1.2.1**: Evaluate what the following erroneous method might intend to do:

```java
public static Star brighterStar(Star s1, Star s2) {
    if (luminosity > s2.luminosity) {
        return this;
    }
    return s2;
}
```

**Static Variables**

Static variables generalize attributes across all instances of a class, like the spectral classification of stars:

```java
public class Star {
    public double luminosity;
    public static String spectralType = "Main Sequence";
    ...
}
```

Accessed serially as `Star.spectralType`, these describe characteristics common to all stars represented by the class, avoiding redundancy.

In good Java practice, static variables should invariably be accessed via class names rather than instances.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

Let's explore the anatomy of the main method:

* `public`: Visibility from other classes.
* `static`: Not linked to an instance.
* `void`: Returns no value.
* `main`: Method name by convention.
* `String[] args`: Input parameters from the command line.

**Command Line Arguments**

The interpreter passes these parameters to `main`, allowing for dynamic input manipulation:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0] + " is an intriguing celestial body.");
    }
}
```

Running `java ArgsDemo Venus` outputs "Venus is an intriguing celestial body."

**Summing Command Line Arguments**

**Exercise 1.2.3**: Write a program that aggregates numerical command line inputs. Consult the provided resources for the answer.

#### Using Libraries <a href="#using-libraries" id="using-libraries"></a>

Mastering library use is crucial in astrophysics programming. Often reliance on external resources is encouraged to expedite development:

* Use only approved libraries.
* Attribute sources adequately.
* Avoid searching direct answers for course-specific problems.

It's permissible to query general functionality, like "convert String integer Java", while searching for specific homework or project solutions is forbidden as per the syllabus's integrity policies.