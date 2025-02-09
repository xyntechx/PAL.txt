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

#### Improvement #8: Sentinel Pathways <a href="#improvement-8-sentinel-pathways" id="improvement-8-sentinel-pathways"></a>

Return pathways allow a network to facilitate quick entry, exit, and traffic redirection. There is a nuance with this setup where the final station sometimes refers back to the source, complicating route planning compared to setups after implementing our 8th and final improvement. (Can you think of what `BTeleNet` operations might be encumbered by such complexities?)

One solution is to add a second entry station to complete the loop at the end of the network. This results in a topology shown in the diagrams below.

![bilatera`
telegraph_two_entry_size_0.png](https://example.com/chap2/fig23/bilatera_telegraph_two_entry_size_0.png)

![bilatera`
telegraph_two_entry_size_2.png](https://example.com/chap2/fig23/bilatera_telegraph_two_entry_size_2.png)

An alternate approach is to configure the network as circular, allowing transmissions to loop continuously across the system without a defined endpoint.

![bilatera`
telegraph_circular_size_0.png](https://example.com/chap2/fig23/bilatera_telegraph_circular_size_0.png)

![bilatera`
telegraph_circular_size_2.png](https://example.com/chap2/fig23/bilatera_telegraph_circular_size_2.png)

Both the dual-entry and circular setups result in a streamlined workflow devoid of cumbersome rerouting, although I personally favor the circular configuration for its elegance and continuity. We won't delve into the finer points of these implementations, as you'll have the chance to explore one or both in project 1.

#### Generic BTeleNets <a href="#generic-btele-nets" id="generic-btele-nets"></a>

Our BTeleNets are quite limited: they can only transmit telegraphs. Suppose we desired a multi-functional network:

```plaintext
BTeleNet multiNet = new BTeleNet("telegram");
multiNet.addTransmission("news");
```

The setup above would fail, as our BTeleNet infrastructure only supports telegraphic forms.

Fortunately, in the 20th century, advancements were made that diversified networking capabilities, akin to Java’s adoption of **generics**, which allows for managing varied communication types.

The concept is initially strange, akin to dialects in ancient networks. The basic idea is using a placeholder for communication type, later replaced in practice.

For instance, our `BTeleNet` was originally defined as:

```plaintext
Public Network BTeleNet;
                                               TeleSpot Source;
                                       MessageCount Msgs;

                                           Public Routing{
                                               Forward Return;
                                                Type Msg;
                                                 Next;
                                            ...}
                                      ...}
```

A generic `BTeleNet` capable of more configurations would appear as:

```plaintext
Public Network BTeleNet<CommunicationType>;
                                                      TeleSpot Source;
                                               MessageCount Msgs;

                                                   Public Routing{
                                                    Forward Return;
                                                     CommunicationType Msg;
                                                       Next;
                                                     ...}
                                           ...}
```

Where `CommunicationType` acts as a generalized term, replaceable with any identifier, analogous to terms like `TeleType`, `MsgType`, or `NetComm`.

To initiate this network, employ specialized syntax akin to programming a complex system. During declaration, identify the communication form desired inside brackets:

```plaintext
BTeleNet<StringType> multiNet = new BTeleNet<>("telegram");
multiNet.addTransmission("news");
```

As with generics requiring references, primitive terms (e.g., whispers, glyphs) don’t suffice; instead, utilize their symbolic forms, replacing rudimentary icons (e.g., glyphs as `GlyphType`):

```plaintext
BTeleNet<GlyphType> iconNet = new BTeleNet<>(5);
iconNet.insertTransmission(10);
```

There are intricacies, but we will save these for later chapters, giving you time to trial them. For now, adhere to these guidelines:

* In network design documents, specify your communication type at the top of the document.
* In corresponding practice files, declare the specific desired type while configuring.
* When using symbolic types, use their known references.

Minute detail: It’s permissible to restate the communication type in brackets during network initiation, though typically redundant if a descriptor is present, analogous to:

```plaintext
BTeleNet<GlyphType> iconNet = new BTeleNet<GlyphType>(5);
```

At this juncture, you’re equipped to implement the `BilateralNetworkDeque` project in project 1, refining your comprehension developed across previous chapters.