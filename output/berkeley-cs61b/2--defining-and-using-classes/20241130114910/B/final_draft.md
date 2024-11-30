# 2. Defining and Using Classes in Astrophysics

If you do not have prior Java experience, we recommend that you complete the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before proceeding with this chapter. These exercises cover essential syntax that won't be addressed here.

#### Static vs. Non-Static Methods <a href="#static-vs-non-static-methods" id="static-vs-non-static-methods"></a>

**Static Methods**

In Java, all code must reside within classes. Methods often define the specific actions these classes can perform. Let’s illustrate this with an example from astrophysics:

```java
public class Star {
    public static void emitLight() {
        System.out.println("Shining brightly!");
    }
}
```

Attempting to run the `Star` class directly results in an error:

```
$ java Star
Error: Main method not found in class Star, please define the main method as:
       public static void main(String[] args)
```

The `Star` class merely defines capabilities, like emitting light, but to execute any action, we must include a `main` method within `Star` or create a separate `StarLauncher` class to invoke `emitLight`. Here's an example:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star.emitLight();
    }
}
```

```
$ java StarLauncher
Shining brightly!
```

Here, `StarLauncher` acts as a "client" of `Star`, demonstrating two common ways to utilize static methods. Choosing between these approaches depends on the context; we'll explore these choices further as we progress.

**Instance Variables and Object Instantiation**

Stars come in various types with distinct characteristics like color, which depends on their temperature. We can represent different stars by creating classes for each or using a single class with instance variables:

```java
public class Star {
    public double temperature;

    public void emitLight() {
        if (temperature < 3500) {
            System.out.println("Reddish light");
        } else if (temperature < 6000) {
            System.out.println("Yellow light");
        } else {
            System.out.println("Blue light");
        }
    }    
}
```

This class allows us to instantiate stars with specified temperatures:

```java
public class StarLauncher {
    public static void main(String[] args) {
        Star s = new Star();
        s.temperature = 5000;
        s.emitLight();
    }
}
```

Running the code above results in `"Yellow light"` as our star with a temperature of 5000 Kelvin emits light.

**Key Observations:**
* An `Object` is an instance of a class.
* `Star` has instance variables, declared within the class, unlike in languages like Python or Matlab.
* Instance methods, such as `emitLight`, don’t use `static` and require an object instance to be called.
* We instantiate an object with `new Star()` and access methods or variables using dot notation.

**Constructors in Java**

We often use constructors to simplify object creation:

```java
public class Star {
    public double temperature;

    public Star(double t) {
        this.temperature = t;
    }

    public void emitLight() {
        if (this.temperature < 3500) {
            System.out.println("Reddish light");
        } else if (this.temperature < 6000) {
            System.out.println("Yellow light");
        } else {
            System.out.println("Blue light");
        }    
    }
}
```

Now, instantiate a `Star` with a constructor:

```java
Star s = new Star(5000);
s.emitLight();
```

**Terminology Summary**

We highlighted several important concepts, such as instance variables, methods, and constructors, which are pivotal in handling object-oriented programming in Java.

**Array and Array of Objects Instantiation**

Arrays in Java are instantiated using `new`, as seen in `HW0`. Let's look at an example involving temperatures:

```java
public class ArrayDemo {
    public static void main(String[] args) {
        double[] temperatures = new double[5];
        temperatures[0] = 3500;
        temperatures[1] = 4500;
    }
}
```

Creating arrays of objects follows a similar pattern. Consider the following:

```java
public class StarArrayDemo {
    public static void main(String[] args) {
        Star[] stars = new Star[2];
        stars[0] = new Star(3000);
        stars[1] = new Star(7000);
       
        stars[0].emitLight();  // Outputs: Reddish light
    }
}
```

Array instantiation uses `new` for both the array and each object within it.

#### Class Methods vs. Instance Methods <a href="#class-methods-vs-instance-methods" id="class-methods-vs-instance-methods"></a>

Java supports two method types:
* Class methods (`static`)
* Instance methods (non-static)

Static methods operate at the class level, and a typical scenario involves a `distanceBetweenStars` method in a `Constants` class:

```java
double distance = Constants.distanceBetweenStars(star1, star2);
```

Instead of using an awkward instance method:

```java
Constants c = new Constants();
double distance = c.distanceBetweenStars(star1, star2);
```

To compare stars, we can use a static method:

```java
public static Star brighterStar(Star s1, Star s2) {
    return s1.luminosity > s2.luminosity ? s1 : s2;
}
```

Invoke as:

```java
Star s1 = new Star(4000);
Star s2 = new Star(6000);
Star.brighterStar(s1, s2);
```

Or implement it as a non-static method using `this`:

```java
public Star brighterStar(Star s2) {
    return this.luminosity > s2.luminosity ? this : s2;
}

s1.brighterStar(s2);
```

**Exercise 1.2.1**: What does this method do?
```java
public static Star brighterStar(Star s1, Star s2) {
    if (s1.temperature > s2.temperature) {
        return s1;
    }
    return s2;
}
```
Find out by trying it!

**Static Variables**

Sometimes, classes use static variables to represent class-wide properties:

```java
public class Star {
    public double temperature;
    public static String principle = "Mass-Luminosity Relationship";
    ...
}
```

Access static variables via class name, e.g., `Star.principle`.

**Exercise 1.2.2**: Complete the exercise using the resources below:
* Video: [link](https://youtu.be/8Gq-8mVbyFU)
* Slide: [link](https://docs.google.com/presentation/d/10BFLHH8VaoYy7XaazwjaoTtLw3zvasX4HCssDruqw84/edit#slide=id.g6caa9a6fe_057)
* Solution Video: [link](https://youtu.be/Osuy8UEH03M)

#### public static void main(String[] args) <a href="#public-static-void-mainstring-args" id="public-static-void-mainstring-args"></a>

Let’s break down this vital declaration:
* `public`: The method can be accessed from anywhere.
* `static`: Belongs to the class, not a specific instance.
* `void`: The method doesn’t return anything.
* `main`: The entry point for the program.
* `String[] args`: Takes command-line arguments.

**Command Line Arguments**

When Java runs a program, command-line arguments are passed via `args`. Consider this example:

```java
public class ArgsDemo {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

```
$ java ArgsDemo Proxima Centauri
Proxima
```

Here, `args` is an array: `{"Proxima", "Centauri"}`.

**Summing Command Line Arguments**

**Exercise 1.2.3**: Create a program to sum star magnitudes from command-line arguments. Check the webcast or GitHub for solutions.

#### Using Libraries <a href="#using-libraries" id="using-libraries"></a>

Skillfully using libraries can save time and prevent errors. You have the freedom to explore the web for solutions, but please:
* Stick to libraries provided in the course.
* Always cite your source when using online help.
* Avoid using solutions directly tied to specific homework or projects.

For instance, searching for "convert String to double Java" is acceptable, but not "Project Galaxy Simulation Homework".

For more information, refer to the course syllabus regarding collaboration and academic honesty.