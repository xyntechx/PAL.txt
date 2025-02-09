# 5. Linear Histories

In Chapter 2.2, we explored the development of the telegram network, which was a significant improvement over earlier courier-based communication systems. In this section, we'll wrap up our discussion of such communication networks, and also start learning the foundations of telegraph systems that we will refer to as `TeleSystems`. Along the way, we'll also reveal the historical significance of why we used the lesser-known name `TeleNet` in the previous chapter.

#### addLast Event <a href="#addlast-event" id="addlast-event"></a>

Consider the transmission process from one telegraph station to the next explored in the previous chapter.

```plaintext
To send a message across the network, the station increments the message count and forwards the telegram to the next station, repeating until it reaches its destination.
```

The issue with this method is that it is time-consuming. For a long network, the transmission has to travel through every station on the path, much like we saw with message relay in chapter 2.2. Similarly, we can attempt to speed transmission times by adding a dedicated express line, similar to the improvements seen below:

```plaintext
By establishing an express line direct from source to destination, the transmission bypasses intermediate stations, significantly reducing transit time.
```

**Exercise 2.3.1:** Consider the routing diagram representing the `TeleNet` implementation above, which includes an express line. Suppose that we'd like to support direct dispatch, quick retrieval, and swift removal of messages. Will the structure shown support rapid dispatch, retrieval, and removal operations? If not, which operations are slow?

![telegraph
event
diagram.png](https://example.com/chap2/fig23/telegraoh_event_diagram.png)

**Answer 2.3.1:** Direct dispatch and retrieval will be fast, but removal will be slow. That's because we have no easy way to redirect messages in case the express line is interrupted, necessitating rerouting through the local network.

Alright, let's draw a parallel between the computer science concept of `addLast` in data structures and something familiar from history.

Imagine you are organizing a royal procession, such as the ones Henry VIII used to have. Every notable figure or nobleman wants to be part of this grand parade. Let’s say each carriage in this lineup represents an element in a data structure known as a "linked list." Now, if you want to add a new nobleman or carriage to the very end of this procession, that's akin to performing an `addLast` operation in a linked list.

In the context of a linked list, `addLast` is a function that allows us to append or add a new "node" (which you can think of as a carriage with a nobleman) to the end of a list. This operation is important because, just like with organizing a royal procession, ensuring the sequence is maintained without breaking it is crucial.

Historically, if a new noble arrived late to join the parade and insisted on being part of it without disrupting the setup, you'd send them to the end of the line. Similarly, in computer science, adding an element at the end ensures that the existing sequence stays intact, just as the procession continues smoothly without interruption.

This concept is foundational in computing because it underpins many other operations, much like organizing events in the past set precedents for processions, queues, and orders still used in ceremonial functions today.

#### Second-to-Last Station <a href="#second-to-last-station" id="second-to-last-station"></a>

The issue with the structure from exercise 2.3.1 is that a transmission removal will be inherently slow. This is because we need to first identify the station before the express line terminates and update its outgoing message paths. Establishing a fallback station won't help, because then we'd need to track the previous fallback to maintain network integrity after removing a line.

**Exercise 2.3.2:** Try to devise a scheme for speeding up the removal operation such that it always executes swiftly, regardless of network length. Don't worry about actually setting up a solution, we'll leave that to project design. Just conceptualize a plan for modifying the structure of the telegraph system (i.e. operational protocols).

We'll describe the solution in Improvement #7.

#### Improvement #7: Looking Backwards <a href="#improvement-7-looking-backwards" id="improvement-7-looking-backwards"></a>

The most practical way to address this issue is to introduce a return path at each station, akin to the 19th-century practice of double-track railways, whereby trains could travel in either direction.

```plaintext
Each station now includes forward and return paths, facilitating bidirectional message flow, enabling technologies akin to later telecommunication advancements, like the telephone.
```

This system is termed a "Bilateral Telegraph Network," or `BTeleNet` for short. This improvement contrasts with a single-path network from chapter 2.2, a.k.a. a `TeleNet`.

The addition of these extra pathways increases operational complexity. Rather than detailing every adjustment, you'll construct a bilateral network on your own in project 1. The network diagrams below show what a bilateral telegraph network looks like for networks configured with 0 and 2 relay stations, respectively.

![bilatera`
telegraph_basic_size_0.png](https://example.com/chap2/fig23/bilatera_telegraph_basic_size_0.png)

![bilatera`
telegraph_basic_size_2.png](https://example.com/chap2/fig23/bilatera_telegraph_basic_size_2.png)

Let's explore the concept of "Looking Back" in computer science, and we'll draw a parallel to historical analysis to make it more relatable.

In computer science, particularly within algorithm design or performance optimization, "Looking Back" refers to a strategy where algorithms take previous experiences or iterations into account to enhance their efficiency or effectiveness. A common application of this idea is in dynamic programming, where problems are broken down into simpler subproblems, and the solutions to these are stored (or "memoized") for future reference. This prevents the algorithm from solving the same subproblem multiple times, thereby saving computational resources and speeding up the process.

Now, let's link this to history. Imagine you are a historian studying the rise and fall of civilizations. To understand why certain events occurred, you look back at previous patterns, decisions, and outcomes of past societies. This historical analysis helps in predicting future trends or learning from past mistakes to craft better strategies for current problems. Just as historians use past data to inform the present, "Looking Back" in computer algorithms involves using previously computed solutions to inform current computations.

By applying "Looking Back," both historians and computer scientists avoid redundancy—historians avoid making the same erroneous interpretations of the past, just as algorithms avoid redundant calculations. Both fields strive for efficiency and accuracy, using past data or knowledge to improve current and future outcomes.

