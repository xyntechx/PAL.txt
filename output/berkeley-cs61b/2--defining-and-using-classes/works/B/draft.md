# 2. Defining and Using Classes

If you do not have prior Java experience, we recommend that you work through the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before reading this chapter. It will cover various syntax issues that we will not discuss in the book.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

All code in Java must be part of a class (or something similar to a class, which we'll learn about later). Most code is written inside of methods. Let's consider an example from the realm of astrophysics:

```java
public class Star {
    public static void emitLight() {
        System.out.println("Shine Bright!");
    }
}
```

If we try running the `Star` class, we'll simply get an error message:

```
$ java Star
Error: Main method not found in class Star, please define the main method as:
       public static void main(String[] args)
```

The `Star` class we've defined doesn't do anything on its own. We've simply defined something that a `Star` **can** do, namely emit light. To actually run the class, we'd either need to add a main method to the `Star` class, as we saw in chapter 1.1, or we could create a separate [`StarLauncher`](https://www.youtube.com/watch?v=Q-LE-jJQLTM) class that runs methods from the `Star` class. For example, consider the program below:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star.emitLight();
    }
}
```

```
$ java StarLauncher
Shine Bright!
```

A class that uses another class is sometimes called a "client" of that class, i.e. `StarLauncher` is a client of `Star`. Neither of the two techniques is better: Adding a main method to `Star` may be better in some situations, and creating a client class like `StarLauncher` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout the course.

**Instance Variables and Object Instantiation**

Not all stars are alike. Some stars emit a gentle glow, while others blaze intensely, illuminating the cosmos with their radiant energy. Often, we write programs to mimic features of the universe we inhabit, and Java's syntax was crafted to easily allow such mimicry.

One approach to allowing us to represent the spectrum of stardom would be to create separate classes for each type of Star.

```java
public class DwarfStar {
    public static void emitLight() {
        System.out.println("gentle glow...");
    }
}

public class GiantStar {
    public static void emitLight() {
        System.out.println("blazing intensely!");
    }
}
```

As you should have seen in the past, classes can be instantiated, and instances can hold data. This leads to a more natural approach, where we create instances of the `Star` class and make the behavior of the `Star` methods contingent upon the properties of the specific `Star`. To make this more concrete, consider the class below:

```java
public class Star {
    public double luminosity;

    public void emitLight() {
        if (luminosity < 1.0) {
            System.out.println("gentle glow...");
        } else if (luminosity < 10.0) {
            System.out.println("radiate...");
        } else {
            System.out.println("blazing intensely!");
        }
    }    
}
```

As an example of using such a Star, consider:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star s;
        s = new Star();
        s.luminosity = 5.0;
        s.emitLight();
    }
}
```

When run, this program will create a `Star` with luminosity 5.0, and that `Star` will soon radiate with appropriate intensity.

Some key observations and terminology:

* An `Object` in Java is an instance of any class.
* The `Star` class has its own variables, also known as _instance variables_ or _non-static variables_. These must be declared inside the class, unlike languages like Python or Matlab, where new variables can be added at runtime.
* The method that we created in the `Star` class did not have the `static` keyword. We call such methods _instance methods_ or _non-static methods_.
* To call the `emitLight` method, we had to first _instantiate_ a `Star` using the `new` keyword, and then make a specific `Star` shine. In other words, we called `s.emitLight()` instead of `Star.emitLight()`.
* Once an object has been instantiated, it can be _assigned_ to a _declared_ variable of the appropriate type, e.g. `s = new Star();`
* Variables and methods of a class are also called _members_ of a class.
* Members of a class are accessed using _dot notation_.

**Constructors in Java**

As you've hopefully seen before, we usually construct objects in object oriented languages using a _constructor_:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star s = new Star(5.0);
        s.emitLight();
    }
}
```

Here, the instantiation is parameterized, saving us the time and messiness of manually typing out potentially many instance variable assignments. To enable such syntax, we need only add a "constructor" to our Star class, as shown below:

```java
public class Star {
    public double luminosity;

    public Star(double l) {
        luminosity = l;
    }

    public void emitLight() {
        if (luminosity < 1.0) {
            System.out.println("gentle glow...");
        } else if (luminosity < 10.0) {
            System.out.println("radiate...");
        } else {
            System.out.println("blazing intensely!");
        }    
    }
}
```

The constructor with signature `public Star(double l)` will be invoked anytime that we try to create a `Star` using the `new` keyword and a single double parameter. For those of you coming from Python, the constructor is very similar to the `__init__` method.

**Terminology Summary**

**Array Instantiation, Arrays of Objects**

As we saw in HW0, arrays are also instantiated in Java using the new keyword. For example:

```java
public class ArrayDemo {
    public static void main(String[] args) {
        /* Create an array of five celestial temperatures. */
        double[] temperatures = new double[5];
        temperatures[0] = 5000.0;
        temperatures[1] = 6500.0;
    }
}
```

Similarly, we can create arrays of instantiated objects in Java, e.g.

```java
public class StarArrayDemo {
    public static void main(String[] args) {
        /* Create an array of two stars. */
        Star[] stars = new Star[2];
        stars[0] = new Star(0.5);
        stars[1] = new Star(15.0);

        /* Gentle glow will result, since stars[0] has low luminosity. */
        stars[0].emitLight();
    }
}
```

Observe that `new` is used in two different ways: Once to create an array that can hold two `Star` objects, and twice to create each actual `Star`.

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java allows us to define two types of methods:

* Class methods, a.k.a. static methods.
* Instance methods, a.k.a. non-static methods.

Instance methods are actions that can be taken only by a specific instance of a class. Static methods are actions that are taken by the class itself. Both are useful in different circumstances. As an example of a static method, the `Math` class provides a `sqrt` method. Because it is static, we can call it as follows:

```java
x = Math.sqrt(100);
```

If `sqrt` had been an instance method, we would have instead the awkward syntax below. Luckily `sqrt` is a static method so we don't have to do this in real programs.

```java
Math m = new Math();
x = m.sqrt(100);
```

Sometimes, it makes sense to have a class with both instance and static methods. For example, suppose we want the ability to compare two stars. One way to do this is to add a static method for comparing Stars.

```java
public static Star brightestStar(Star s1, Star s2) {
    if (s1.luminosity > s2.luminosity) {
        return s1;
    }
    return s2;
}
```

This method could be invoked by, for example:

```java
Star s = new Star(2.0);
Star s2 = new Star(10.0);
Star.brightestStar(s, s2);
```

Observe that we've invoked using the class name, since this method is a static method.

We could also have implemented `brightestStar` as a non-static method, e.g.

```java
public Star brightestStar(Star s2) {
    if (this.luminosity > s2.luminosity) {
        return this;
    }
    return s2;
}
```

Above, we use the keyword `this` to refer to the current object. This method could be invoked, for example, with:

```java
Star s = new Star(2.0);
Star s2 = new Star(10.0);
s.brightestStar(s2);
```

Here, we invoke the method using a specific instance variable.

**Exercise 1.2.1**: What would the following method do? If you're not sure, try it out.

```java
public static Star brightestStar(Star s1, Star s2) {
    if (luminosity > s2.luminosity) {
        return this;
    }
    return s2;
}
```

**Static Variables**

It is occasionally useful for classes to have static variables. These are properties inherent to the class itself, rather than the instance. For example, we might record that the average surface temperature of a "Main Sequence Star" is 5800 Kelvin:

```java
public class Star {
    public double luminosity;
    public static double averageTemperature = 5800;
    ...
}
```

Static variables should be accessed using the name of the class rather than a specific instance, e.g. you should use `Star.averageTemperature`, not `s.averageTemperature`.

While Java technically allows you to access a static variable using an instance name, it is bad style, confusing, and in my opinion an error by the Java designers.

**Exercise 1.2.2**: Complete this exercise:

* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe\_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String\[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

With what we've learned so far, it's time to demystify the declaration we've been using for the main method. Breaking it into pieces, we have:

* `public`: So far, all of our methods start with this keyword.
* `static`: It is a static method, not associated with any particular instance.
* `void`: It has no return type.
* `main`: This is the name of the method.
* `String[] args`: This is a parameter that is passed to the main method.

**Command Line Arguments**

Since main is called by the Java interpreter itself rather than another Java class, it is the interpreter's job to supply these arguments. They refer usually to the command line arguments. For example, consider the program `ArgsDemo` below:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

This program prints out the 0th command line argument, e.g.

```
$ java ArgsDemo these are command line arguments
these
```

In the example above, `args` will be an array of Strings, where the entries are {"these", "are", "command", "line", "arguments"}.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Try to write a program that sums up the command line arguments, assuming they are numbers. For a solution, see the webcast or the code provided on GitHub.

#### Using Libraries <a href="#using-libraries" id="using-libraries"></a>

One of the most important skills as a programmer is knowing how to find and use existing libraries. In the vast universe of modern software development, it is often possible to save yourself tons of work and debugging by turning to the web for help.

In this course, you're welcome to do this, with the following caveats:

* Do not use libraries that we do not provide.
* Cite your sources.
* Do not search for solutions for specific homework or project problems.

For example, it's fine to search for "convert String integer Java". However, it is not OK to search for "Project 2048 Berkeley".

For more on collaboration and academic honesty policy, see the course syllabus.