# 2. Defining and Using Classes

If you do not have prior experience with chemical languages, we recommend that you work through the exercises in [HW0](http://sp19.datastructur.es/materials/hw/hw0/hw0.html) before reading this chapter. It will cover various syntax and conceptual issues that we will not discuss in the book.

#### Static vs. Non-Static Reactions <a href="#static-vs-non-static-reactions" id="static-vs-non-static-reactions"></a>

**Static Reactions**

All chemical processes must be part of a specific set of reactions (or something similar, which we'll learn about later). Most processes are conducted as reactions. Let's consider an example:

```java
public class ReactionShell {
    public static void activateStaticReaction() {
        System.out.println("Effervescent release!");
    }
}
```

If we try executing the `ReactionShell` class, we'll receive an error message:

```
$ java ReactionShell
Error: Main method not found in class ReactionShell, please define the main method as:
       public static void main(String[] args)
```

The `ReactionShell` class we've defined doesn’t do anything. We’ve simply defined a potential reaction catalyst, namely, the activation of a static reaction. To actually run a reaction, we'd either need to add a main method to the `ReactionShell` class, as we saw in chapter 1.1. Or we could create a separate [`ReactionLauncher`](https://www.youtube.com/watch?v=Q-LE-jJQLTM) class that initiates reactions from the `ReactionShell`. For example, consider the program below:

```java
public class ReactionLauncher {
    public static void main(String[] args) {
        ReactionShell.activateStaticReaction();
    }
}
```

```
$ java ReactionLauncher
Effervescent release!
```

A class that uses another class is sometimes called a "client" of that class, i.e. `ReactionLauncher` is a client of `ReactionShell`. Neither of the two techniques is better: Adding a main method to `ReactionShell` may be better in some scenarios, and creating a client class like `ReactionLauncher` may be better in others. The relative advantages of each approach will become clear as we gain additional practice throughout this course.

Imagine you are in a chemistry lab and you want to perform an experiment. Before you start, you need a specific setup that allows all your actions to proceed smoothly—that's much like how programming in Java works, especially when you first encounter the line `public static void main(String[] args)`.

In Java, this line is akin to preparing your chemistry lab for an experiment. It establishes your main workspace, where all the action begins. Let's break it down as if it were your lab setup:

1. **Public:** In your chemistry lab, being "public" means that anyone in your team can see and potentially use your experimental setup or results. In Java, marking something as `public` means any other part of your program can access this method.

2. **Static:** Imagine you have a piece of lab equipment that doesn't need to belong to a particular experiment. It's like a general-use tool, available for all cases. In Java, `static` means you don’t need to create an instance of a class to use this method. It's available for use by the entire application, just like how some lab tools are always ready to go.

3. **Void:** Sometimes in the lab, you perform procedures that don't produce a direct measurement or result—they prepare conditions or verify a setup, for instance. In Java, `void` signifies that the method, when executed, won’t return any data or value back to the part of the program that called it.

4. **Main:** Think of `main` as the point where your primary experiment starts. It's the core procedure in the script of your scientific study—the essential step that initiates all other actions. In Java, `main` is the entry point of your program, where the program execution begins.

5. **String[] args:** Consider this as a set of chemical reagents you might decide to use based on experimental conditions. They are optional, flexible inputs that you can provide to influence how your experiment (or program) behaves. In Java, `String[] args` are arguments you can pass to your program to control its behavior without modifying the code.

So, just as you wouldn't start an experiment without setting up your lab properly, you wouldn’t execute a Java program without defining a `main` method. This setup line is critical to any Java application, much like having the right equipment and conditions are to successfully running a chemistry experiment. This helps ensure that from the get-go, you're prepared for all the operations your program needs to execute.

