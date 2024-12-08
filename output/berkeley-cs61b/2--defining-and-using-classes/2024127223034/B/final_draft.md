# 2. Defining and Using Classes in Astrophysics

If you're not familiar with Java, it might be beneficial to complete exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) to ground yourself in Java syntax. This chapter will blend basic Java class usage with astrophysics applications, using detailed examples to enhance understanding.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

In Java, all code resides within the structure of a class. Functionality is encapsulated in methods, illustrated here using an astrophysical example:

```java
public class Star {
    public static void illuminate() {
        System.out.println("A dazzling star in the cosmos");
    }
}
```

Directly running the `Star` class will produce an error:

```
$ java Star
Error: Main method not found in class Star, please define the main method as:
       public static void main(String[] args)
```

Although the `Star` class defines potential capabilities (like illuminating), it doesn't perform actions by itself. To execute this functionality, you can encapsulate it in a `main` method or utilize another class like `StarObserver` to trigger the `Star` methods:

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

In this example, `StarObserver` acts as a client invoking the `Star` class. Choosing between embedding a `main` method or using external classes depends on the context and will become more intuitive with practice.

**Instance Variables and Object Instantiation**

Stars vary significantly in their luminosity, analogous to how instance variables represent object differences in Java. To model these variations without multiple sub-classes, you can create instances:

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

Here’s how you use the `Star` class:

```java
public class StarObserver {
    public static void main(String[] args) {
        Star s = new Star();
        s.luminosity = 5.0;
        s.shine();
    }
}
```

Running this results in a `Star` with a luminosity of 5, emitting "A steady glow, surveying the universe."

Key points:

* A Java Object is an instance of any class.
* The `Star` class uses instance variables, like `luminosity`, defined within the class. 
* The `shine` method exemplifies an instance method due to the absence of `static`. 
* Creation and utilization of a `Star` instance use `new Star()` and `s.shine()`.
* Objects are manipulated using dot notation for properties and behaviors.

**Constructors in Java**

Constructors simplify object initialization, essential in object-oriented design:

```java
public class StarObserver {
    public static void main(String[] args) {
        Star s = new Star(5.0);
        s.shine();
    }
}
```

Here's a constructor in the `Star` class:

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

Constructors, similar to `__init__` in Python, establish an object's initial state, allowing for specified parameters. When `new` is used, this constructor initializes the `Star` with a set luminosity.

**Terminology Summary**

**Array Instantiation, Arrays of Objects**

Arrays, dynamically created with `new`, handle multiple objects efficiently, e.g., an array of stars:

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

Firstly, `new` defines an array capacity, and then it instantiates each `Star` within the array.

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java supports both static and instance methods. Static methods, like `Math.sqrt`, are executed at the class level:

```java
double result = Math.sqrt(144);
```

If `sqrt` were an instance method, instantiation would be necessary:

```java
Math m = new Math();
double result = m.sqrt(144);
```

A class may utilize both methods, such as comparing stars by luminosity:

```java
public static Star brighterStar(Star s1, Star s2) {
    if (s1.luminosity > s2.luminosity) {
        return s1;
    }
    return s2;
}
```

This is employed as:

```java
Star s1 = new Star(5.0);
Star s2 = new Star(8.5);
Star brightest = Star.brighterStar(s1, s2);
```

Static methods operate at the class level, streamlining syntax where suitable.

Non-static alternatives access instance variables directly:

```java
public Star brighterStar(Star s2) {
    if (this.luminosity > s2.luminosity) {
        return this;
    }
    return s2;
}
```

Invoked as:

```java
Star s1 = new Star(5.0);
Star s2 = new Star(8.5);
Star brightest = s1.brighterStar(s2);
```

**Exercise 1.2.1**: Determine the intention behind this faulty method:

```java
public static Star brighterStar(Star s1, Star s2) {
    if (luminosity > s2.luminosity) {
        return this;
    }
    return s2;
}
```

**Static Variables**

Static variables apply class-level attributes, like uniform properties across stars:

```java
public class Star {
    public double luminosity;
    public static String spectralType = "Main Sequence";
    ...
}
```

Acquired as `Star.spectralType`, these avoid redundancy in denoting universal class traits. Good practice dictates accessing static variables via class names.

**Exercise 1.2.2**: Complete the following exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

Explore the main method structure:

* `public`: Accessible from other classes.
* `static`: Disassociated from specific instances.
* `void`: Returns no output.
* `main`: Conventionally named entry point.
* `String[] args`: Accepts command line arguments.

**Command Line Arguments**

These parameters enable dynamic data input in `main`:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0] + " is an intriguing celestial body.");
    }
}
```

Executing `java ArgsDemo Venus` outputs "Venus is an intriguing celestial body."

**Summing Command Line Arguments**

**Exercise 1.2.3**: Develop a program that sums command line numeric inputs. Refer to provided resources for the solution.

#### Using Libraries <a href="#using-libraries" id="using-libraries"></a>

Proficiency with libraries is essential in astrophysics programming, encouraging external resources for efficient development:

* Employ only sanctioned libraries.
* Properly cite sources.
* Avoid directly searching specific course work solutions.

While general queries, like "convert String to integer Java," are permissible, searching for explicit homework or project solutions contravenes syllabus integrity policies.