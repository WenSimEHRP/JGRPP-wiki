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

Routefinding restriction programs can be attached to any kind of signal.  
These programs are run by trains, and can check various train properties, and slot and counter values.  
These programs can be used to control pathfinding, PBS, slots, counters, reversing, speed restrictions and other miscellaneous operations.  
Routefinding restrictions require using the **YAPF pathfinder** for trains.

By default, electric signals with a routefinding restriction program attached have a blue signal post.  
This does not apply when using custom signal graphics, unless the "Show restricted electric signals using default graphics" setting is enabled.

Programs are executed in order from top to bottom.  
In case where one action cancels another, the last executed action takes effect.

Actions:
* Deny  
  The YAPF pathfinder will see this signal as a dead end, and will not look beyond the signal to find the destination.  
  This can be used to prevent trains from taking a particular route.
* Penalty  
  The YAPF pathfinder will add a penalty value to the cost of pathfinding past this signal.  
  This can be used to fine-tune train pathfinding.  
  The current suggested values in the dropdown are: small = 500, medium = 2000, and large = 8000.
* Reserve through  
  PBS will not end a reservation at this PBS signal, it is as if the signal is not there at all in the forward direction.
* Long reserve  
  If a train makes a PBS reservation that ends at this PBS signal, a second separate reservation will be attempted starting from this signal.  
  The first reservation is not cancelled if the second reservation is not possible.
* News control  
  This allows turning off the train is stuck/lost news messages for trains waiting at this particular signal.

Conditional blocks:
* If  
  This starts a new conditional block. The contents of which are only executed if the condition is true.
* Else if  
  The contents of this block are only executed if the condition is true AND none of the previous conditions in this conditional block were true.
* Or if  
  The contents of this block are only executed if the condition is true AND none of the previous conditions in this conditional block were true, OR if the previous condition in this conditional block was true.
* Else  
  The contents of this block are only executed if none of the previous conditions in this conditional block were true.
* End if  
  This ends the conditional block.

Conditional blocks may be nested inside other conditional blocks.

Conditions:
* Train length  
  This checks the train length in tiles (rounded up).
* Max speed  
  This checks the train's maximum speed.
* Current order  
  This checks the destination of the train's current order.
* Next order  
  This checks the destination of the train's next order after the current order.
* Last visited station  
  This checks which station the train last visited.
* Cargo  
  This checks whether the train can or can't carry a particular cargo.
* Load percentage  
  This checks the current load percentage of the train.  
  (Trains with no cargo capacity at all are considered full: 100%).
* Entry direction  
  This checks which side the train is entering the signal from: front, back or compass direction.
* PBS entry signal  
  This checks the tile of the PBS signal where the PBS reservation is starting from.  
  Note: When a PBS reservation passes through a signal using the "Reserve through" action, the passed signal does not become the PBS entry signal.  
  Note: When a second PBS reservation is started at a signal using the "Long reserve" action, the long reserve signal does become the PBS entry signal.
* Train group  
  This checks whether the train is in a particular group.  
  This works with nested groups.
* Train owner  
  This checks which company owns the train.
* Train status  
  This checks the current status of the train, the statuses which can be checked are:  
  * Empty
  * Full
  * Broken down
  * Needs repair
  * Reversing
  * Heading to station or waypoint
  * Heading to depot
  * Loading
  * Waiting
  * Lost
  * Requires servicing
* Weight  
  This checks the train's current weight.
* Power  
  This checks the train's power.
* Max T.E.  
  This checks the train's maximum tractive effort.
* Power / weight  
  This checks the train's current power to weight ratio.
* Max T.E. / weight  
  This checks the train's current maximum tractive effort to weight ratio.

The more advanced features below are only shown if the "Show advanced routing restriction features" setting is enabled.

Advanced actions  
* Wait at PBS signal  
  The train waits at this PBS signal.
* Slot operation  
  See **Slots** section below for details of what slots are.  
  The sub-actions which this can take are:  
  * Acquire or wait  
    Try to acquire membership in the slot, if the slot is full and the train cannot become a member, wait at this PBS signal.
  * Try to acquire  
    Try to acquire membership in the slot, if the slot is full and the train cannot become a member, carry on anyway.
  * Release (front)  
    Release membership of this slot when the front of the train passes the signal.
  * Release (back)  
    Release membership of this slot when the back of the train passes the signal.
  * PBS end: Acquire or wait  
    When attempting to make a PBS reservation which ends at this signal, try to acquire membership in the slot, if the slot is full and the train cannot become a member, wait at the start PBS signal.
  * PBS end: Try to acquire  
    When attempting to make a PBS reservation which ends at this signal, try to acquire membership in the slot, if the slot is full and the train cannot become a member, make the reservation anyway.
  * PBS end: Release  
    When a PBS reservation is made which ends at this signal, release membership of this slot.
* Reverse behind signal  
  The train reverses behind this signal. The signal must be a PBS signal (not one-way), and the train must be entering from the back direction.
* Speed restriction  
  Set a speed restriction on the train when the train passes the signal.  
  A value of 0 removes the restriction.
* Counter operation  
  See **Counters** section below for details of what counters are.  
  The sub-actions which this can take are:  
  * Increase  
    Increase the value of the counter when the front of the train passes this signal.
  * Decrease  
    Decrease the value of the counter when the front of the train passes this signal. The value will not decrease below 0.
  * Set  
    Set the value of the counter to a particular value when the front of the train passes this signal.

Advanced conditions:
* Train in slot  
  This checks whether the train is currently a member of the slot.
* Slot occupancy  
  This checks how many trains are members of the slot.
* Slot occupancy remaining  
  This checks how much unused capacity there is in the slot, this is the slot capacity minus how many trains are members of the slot.
* Counter value  
  This checks the value of a counter.

**Programmable pre-signals**

Programmable pre-signals are combo pre-signals, with programmable conditions for whether the signal is red or green.  
Programmable pre-signals are block signals, with no support for PBS.  
Programmable pre-signal programs cannot test any properties of trains, and are run even if there is no train approaching the signal.  
In most cases, routefinding restrictions are more useful.

Unlike routefinding restrictions, programmable pre-signal programs end when the first "Set signal state" line is reached.

Programmable signals are not shown in the signal window by default, **"Show programmable pre-signal feature"** must be enabled.

![Programmable pre-signals example](Features/images/prog-presignals-0.png)

**Slots**

**Counters**

Counters are named variables which can be modified by a routefinding restriction program when a train passes a signal.  
Counters can be used in conditionals in routefinding restrictions and programmable pre-signal programs, and in conditional orders.  
The main use case for counters is counting trains and round-robin behaviour.  
For counting the number of trains on a particular section of track, slots should be used instead.

Using counters to store state makes "logic trains" and similar workarounds unnecessary.

Counters are not shown in the user interace by default, **"Show advanced routing restriction features"** must be enabled.

Counters can be created, deleted, renamed and have their value manually changed by selecting "Manage counters" in the train list window "Manage list" dropdown.

![Aesthetically suboptimal](Features/images/counter-before.png) ![A bit tidier, using counters](Features/images/counter-after.png) ![Details](Features/images/counter-detail.png)
