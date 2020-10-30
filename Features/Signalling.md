## Signalling features

* **Routefinding restrictions**  
  Routefinding restriction programs can be attached to any kind of signal.  
  These programs are run by trains, and can check various train properties, and slot and counter values.  
  These programs can be used to control pathfinding, PBS, slots, counters, reversing, speed restrictions and other miscellaneous operations.  
* **Programmable pre-signals**  
  Programmable pre-signals are combo pre-signals, with programmable conditions for whether the signal is red or green.  
  Programmable pre-signals are block signals, with no support for PBS.
* **Slots**  
  Slots are analogous to token systems used in real-life railways, in particular single-line sections.  
  A slot has a capacity, the number of trains which can be in the slot/have a token.  
  A train can be a member of any number of different slots at once (have any number of different tokens at once).  
  Trains can acquire or release membership of slots (acquire or release tokens) at signals, or using conditional orders.  
  Slots can be used in conditionals in routefinding restrictions and programmable pre-signal programs, and in conditional orders.
* **Counters**  
  Counters are named variables which can be modified when a train passes a signal.  
  Counters can be used in conditionals in routefinding restrictions and programmable pre-signal programs, and in conditional orders.  
  In most cases, slots should be used instead.

**Routefinding restrictions**

**Programmable pre-signals**

Programmable pre-signals are combo pre-signals, with programmable conditions for whether the signal is red or green.  
Programmable pre-signals are block signals, with no support for PBS.  
Programmable pre-signal programs cannot test any properties of trains, and are run even if there is no train approaching the signal.  
In most cases, routefinding restrictions are more useful.

Unlike routefinding restrictions, programmable pre-signal programs end when the first "Set signal state" line is reached.

![Programmable pre-signals example](Features/images/prog-presignals-0.png)

**Slots**

**Counters**

Counters are named variables which can be modified by a routefinding restriction program when a train passes a signal.  
Counters can be used in conditionals in routefinding restrictions and programmable pre-signal programs, and in conditional orders.  
The main use case for counters is counting trains and round-robin behaviour.  
For counting the number of trains on a particular section of track, slots should be used instead.

Using counters to store state makes "logic trains" and similar workarounds unnecessary.

![Aesthetically suboptimal](Features/images/counter-before.png) ![A bit tidier, using counters](Features/images/counter-after.png) ![Details](Features/images/counter-detail.png)
