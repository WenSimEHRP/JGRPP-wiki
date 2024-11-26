## Signalling features

* [**Routefinding restrictions**](#routefinding-restrictions)  
  Routefinding restriction programs can be attached to any kind of signal.  
  These programs are run by trains, and can check various train properties, and slot and counter values.  
  These programs can be used to control pathfinding, path reservation, slots, counters, reversing, speed restrictions and other miscellaneous operations.  
* [**Slots**](#slots)  
  Slots are analogous to token systems used in real-life railways, in particular single-line sections.  
  A slot has a capacity, the number of trains which can be in the slot/have a token.  
  A train can be a member of any number of different slots at once (have any number of different tokens at once).  
  Trains can acquire or release membership of slots (acquire or release tokens) at signals, or using conditional orders.  
  Slots can be used in conditionals in routefinding restrictions and programmable pre-signal programs, and in conditional orders.
* [**Counters**](#counters)  
  Counters are named variables which can be modified when a train passes a signal.  
  Counters can be used in conditionals in routefinding restrictions and programmable pre-signal programs, and in conditional orders.  
  In most cases, slots should be used instead.
* [**Programmable pre-signals**](#programmable-pre-signals)  
  Programmable pre-signals are combo pre-signals, with programmable conditions for whether the signal is red or green.  
  Programmable pre-signals are block signals, with no support for path signalling.

### Routefinding restrictions

Routefinding restriction programs can be attached to any kind of signal.  
These programs are run by trains, and can check various train properties, and slot and counter values.  
These programs can be used to control pathfinding, path reservation, slots, counters, reversing, speed restrictions and other miscellaneous operations.  
Routefinding restrictions require using the **YAPF pathfinder** for trains.

By default, electric signals with a routefinding restriction program attached have a blue signal post.  
This does not apply when using custom signal graphics, unless the "Show restricted electric signals using default graphics" setting is enabled.

Programs are executed in order from top to bottom.  
In the case where one action cancels another, the last executed action takes effect.

#### Example 1: Combined bay and through station

![Routing restrictions example 1](Features/images/routing-restrictions-example-0.png)

This is a possible way to implement a combined bay and through station.  
The example assumes that only bay-platform traffic calls next at "Southerly Station", which is to the south-east.  
The two signals in front of the bay platforms share the program in the upper window.  
The signal in front of the north/west bound through platform has the program in the lower window.

The bay platform signals deny access if the train is entering from the back of the signal and the next order (the order after the call at New Bedtown) *is not* Southerly Station.  
This has the effect of stopping trains which need to continue north/west from using the bay platforms.  
The "train is entering from the back of the signal" test is to avoid restricting trains trying to leave the platforms.

The through platform signal adds a pathfinder penalty if the train is entering from the back of the signal and the next order (the order after the call at New Bedtown) *is* Southerly Station.  
This has the effect of adding a penalty for trains which could use the bay platforms, such that those trains will always use a bay platforms if one is available. However if all the bay platforms are full or otherwise unreachable, it can still use the through platform, and reverse out again afterwards.

#### Example 2: Station with single passing track

![Routing restrictions example 2](Features/images/routing-restrictions-example-1.png)

This is a possible way to implement a station with a single bi-directional passing track.

Trains will use the platform tracks if unoccupied, otherwise if the platform is occupied and the train does not call at this station,
trains will use the central track to bypass the occupied platform.

The pathfinder penalty for a station tile defaults to 800, therefore the total penalty for a 4 tile platform is 3200.  
Here the same station platform penalty is added to the central track (1600 on each of the two signals).  
The backwards facing signal on entrance to the central track is large enough that the platform track has a lower pathfinder cost than the central track when unoccupied.  
However when the platform track is occupied but the central track is not, the central track has a lower pathfinder cost.

The long reserve action on the central track signals is to better allow non-stop trains using the central track to overtake trains currently occupying the platform.

#### Actions

<ul>

##### Deny

The pathfinder will see this signal as a dead end, and will not look beyond the signal to find the destination.  
This can be used to prevent trains from taking a particular route.

##### Penalty

The pathfinder will add a penalty value to the cost of pathfinding past this signal.  
This can be used to fine-tune train pathfinding.  
The current suggested values in the dropdown are: small = 500, medium = 2000, and large = 8000.

##### Reserve through

Path reservations will not end a reservation at this path signal, it is as if the signal is not there at all in the forward direction.  
This action has no effect when applied to a signalled tunnel/bridge entrance or exit.

##### Long reserve

If a train makes a path reservation that ends at this path signal, a second separate reservation will be attempted starting from this signal.  
The first reservation is not cancelled if the second reservation is not possible.  
This action has no effect when applied to a signalled tunnel/bridge entrance.

The "Long reserve (unless stopping)" sub-action can be used to only enable long reserve when the train is not stopping at a station or waypoint,
earlier in the train's reservation. This is useful for signals at platform ends where it would not be useful to enable long reserve for trains which will be stopping.

##### Slot operation

See [**Slots**](#slots) section below for details of what slots are.  
The sub-actions which this can take are:  
* Acquire or wait  
  Try to acquire membership in the slot, if the slot is full and the train cannot become a member, wait at this path signal.
* Try to acquire  
  Try to acquire membership in the slot, if the slot is full and the train cannot become a member, carry on anyway.  
  When reserving ahead it is attempted when making the reservation, no second attempt is made when later passing the already reserved signal.
* Release (front)  
  Release membership of this slot when the front of the train passes the signal.
* Release (back)  
  Release membership of this slot when the back of the train passes the signal.
* Release (on reserve)  
  Release membership of this slot when making a reservation from this signal (this is the executed in the same conditions as the "acquire or wait" and "try to acquire" sub-actions).
* Path end: Acquire or wait  
  When attempting to make a path reservation which ends at this signal, try to acquire membership in the slot, if the slot is full and the train cannot become a member, wait at the start path signal.
* Path end: Try to acquire  
  When attempting to make a path reservation which ends at this signal, try to acquire membership in the slot, if the slot is full and the train cannot become a member, make the reservation anyway.
* Path end: Release  
  When a path reservation is made which ends at this signal, release membership of this slot.

##### News control

This allows turning off the train is stuck/lost news messages for trains waiting at this particular signal.

</ul>

#### Conditional blocks

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

When a conditional block is selected, clicking the "Remove" button removes the entire block and its contents.  
Ctrl-clicking the "Remove" button removes the condition but does not remove the contents of the block.

#### Conditions

<ul>

##### Train length

This checks the train length in tiles (rounded up).

##### Max speed

This checks the train's maximum speed.

##### Current order

This checks the destination of the train's current order.

##### Next order

This checks the destination of the train's next order after the current order.

##### Last visited station

This checks which station the train last visited.

##### Cargo

This checks whether the train can or can't carry a particular cargo.

##### Load percentage

This checks the current load percentage of the train.  
(Trains with no cargo capacity at all are considered full: 100%).

##### Entry direction

This checks which side the train is entering the signal from: front, back, compass direction, or entering/exiting tunnel/bridge.

##### Train group

This checks whether the train is in a particular group.  
This works with nested groups.

##### Train owner

This checks which company owns the train.

##### Train status

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
* Stopping at station/waypoint

##### Weight

This checks the train's current weight.

##### Power

This checks the train's power.

##### Max T.E.

This checks the train's maximum tractive effort.

##### Power / weight

This checks the train's current power to weight ratio.

##### Max T.E. / weight

This checks the train's current maximum tractive effort to weight ratio.

##### Engine class

This checks whether the train has at least one engine of a particular class. The engine classes are:
* Steam
* Diesel
* Electric
* Monorail
* Maglev

##### Direction of order target

This checks which direction the tile of the train's current or next order is in, relative to the signal tile.

</ul>

#### Advanced actions

The more advanced features below are only shown if the "Show advanced routing restriction features" setting is enabled.

<ul>

##### Wait at path signal

The sub-actions which this can take are:  
* Wait at path signal  
  The train waits at this path signal.
* Cancel wait at path signal  
  Cancels a previous wait at path signal action.
* Wait at start path signal for reservation ending here  
  If a train would make a path reservation which ends at this signal, the train will instead wait at the start signal and not make the reservation.
* Cancel wait at start path signal for reservation ending here  
  Cancel a previous wait at start path signal for reservation ending here.

##### Reverse

The sub-actions which this can take are:  
* Reverse behind signal  
  The train reverses behind this signal.  
  The signal must be a path signal (not one-way), and the train must be entering from the back direction.  
  The pathfinder can follow reverse being signal actions, (within the number of signals where routing restriction programs are evaluated).
* Cancel reverse behind signal  
  Cancel a previous reverse behind signal.
* Reverse at path signal  
  The trains reverses at this path signal, the train must be approaching from the front direction.  
  The pathfinder cannot follow reverse at path signal actions.  
  In most cases, reverse behind signal should be used instead.
* Cancel reverse at path signal  
  Cancel a previous reverse at path signal.

##### Speed restriction

Set a speed restriction on the train when the train passes the signal.  
A value of 0 removes the restriction.

##### Counter operation

See [**Counters**](#counters) section below for details of what counters are.  
The sub-actions which this can take are:  
* Increase  
  Increase the value of the counter when the front of the train passes this signal.
* Decrease  
  Decrease the value of the counter when the front of the train passes this signal. The value will not decrease below 0.
* Set  
  Set the value of the counter to a particular value when the front of the train passes this signal.

##### Penalty config

The sub-actions which this can take are:  
* No path signal back penalty  
  Do not apply the pathfinder penalty for passing this signal from the back side.
* Cancel no path signal back penalty  
  Cancel a previous do not apply the pathfinder penalty for passing this signal from the back side.

##### Speed adaptation control

The sub-actions which this can take are:  
* Make exempt  
  The train is made exempt from automatic speed adaptation when the train passes this signal.
* Remove exemption  
  A previous exemption from automatic speed adaptation is removed when the train passes this signal.

##### Signal mode control

This action may be used to override whether a reservation made from a combined normal/shunt style signal  
uses normal or shunt mode. The normal/shunt mode affects the displayed signal aspect, and the train driving  
model if the train braking is aspect limited setting is enabled.  
This action is executed after the reservation has been made.  
This requires the realistic train braking model.

</ul>

#### Advanced conditions

The more advanced features below are only shown if the "Show advanced routing restriction features" setting is enabled.

<ul>

##### Train in slot

This checks whether the train is currently a member of the slot.

##### Slot occupancy

This checks how many trains are members of the slot.

##### Slot occupancy remaining

This checks how much unused capacity there is in the slot, this is the slot capacity minus how many trains are members of the slot.

##### Counter value

This checks the value of a counter.

##### Current time/date

This checks the current time/date. The hour and minute values require that the savegame setting "Show time in minutes instead of days" is enabled.  
This is not affected by any use of the setting "Use client time settings instead of savegame time settings".  
The time values which can be tested are:  
* Minute (0 - 59)  
* Hour (0 - 23)  
* Hour and minute (0 - 2359)
* Day (1 - 31)
* Month (1 - 12)

##### Reserved tiles ahead

This checks the number of tiles of reservation ahead of the train (rounded down). This requires the realistic train braking model.  
This is mainly useful to control the long reserve action.

##### Path reservation passes tile

This checks whether the train's reservation passes through the tile, at any point along its length.  

##### Path entry signal

This checks the tile of the path signal where the path reservation is starting from.  
Note: When a path reservation passes through a signal using the "Reserve through" or "Long reserve" actions, the passed signal does not become the path entry signal.  
This is mainly useful to control the long reserve, reserve through and possibly wait at start path signal for reservation ending here actions.  
This condition may not be used with the signal mode control action.

##### Path end signal

This checks the tile of the path signal at the current end of the path reservation. This requires the realistic train braking model.  
Note: When a path reservation passes through a signal using the "Reserve through" action, the passed signal does not become the path end signal.  
Note: When a second path reservation is started at a signal using the "Long reserve" action or due to the train reserving ahead, the signal does become the new reservation end signal.  
This test should be used when checking which signal is used to enter a block when using realistic braking, instead of the path entry signal condition, which could return a signal closer to the train.  
This is mainly useful to control the reserve through and possibly wait at start path signal for reservation ending here actions. This is not useful for controlling the long reserve action.  
This condition may not be used with the signal mode control action.

##### Path reservation end tile

This condition may ONLY be used with the signal mode control action.  
This condition checks the tile at the end of the reservation (the last reserved tile), after the reservation has been made from this signal.  
This requires the realistic train braking model.

</ul>

Note that the path entry/end signal conditionals are somewhat tricky to use and can have non-intuitive behaviour when used with pathfinding/penalty actions,
because pathfinding also takes place beyond the current signal block where any reservation is being made. In this case a prediction of what the path signal would be
is made.


### Slots

Slots are analogous to token systems used in real-life railways, in particular single-line sections.  
A slot has a capacity, the number of trains which can be in the slot/have a token.  
A train can be a member of any number of different slots at once (have any number of different tokens at once).  
Trains can acquire or release membership of slots (acquire or release tokens) at signals, or using conditional orders.  
Slots can be used in conditionals in routefinding restrictions and programmable pre-signal programs, and in conditional orders.

Slots can be created, deleted, renamed, have their capacity changed, and have trains manually added/removed from the slot by selecting "Manage slots" in the train list window "Manage list" dropdown.

Road vehicles, aircraft and ships can also use slots. These can only use conditional orders to check and control slot membership (not signals), but otherwise function the same as train slots. Each vehicle type has a separate set of slots. 

#### Example 1: Using slots and pathfinder deny to hold trains in queuing sidings

![Slots example](Features/images/slots-example-0.png)

In this example, only one recycling train should be full-loading at the station at a time.  
Other recycling trains may be held somewhere more convenient some distance away from the station until it is free.

At the first, right-most signal, recycling trains headed for the station try to reserve the slot.

At the second signal, recycling trains which are not in the slot (they did not manage to acquire the slot) may not pathfind past the signal.  
This forces them to pathfind via the adjacent queuing sidings.

At the siding exit signals, recycling trains wait indefinitely until they can acquire the slot.

![Slots example](Features/images/slots-example-1.png)

At the platform exit signal, if the train is leaving the platform (entering the signal from the front), the slot is released, allowing another train to acquire it.

The slot is shown in the slots management window as 1/1, this means that it is occupied by 1 train and has a capacity of 1, it is currently full.  
The train occupying the slot is shown on the right, this is the train currently in the platform.

#### Example 2: Using slots and conditional orders to divert and hold trains in queuing sidings

![Slots example](Features/images/slots-example-2.png)

This example is similar to example 1, except that conditional orders are used to divert trains which cannot acquire the slot into the queuing sidings.  
This is useful when the train would not otherwise go past the sidings, such that it would be impractical to divert the train into the sidings using
pathfinder deny or penalty routing restrictions on signals.

After passing the waypoint at order 16, the conditional order at order 17 is evaluated.  
If the train is already in or can acquire the slot, the train immediately jumps to order 21.  
This bypasses the orders for the queuing siding, such that it need not go near the sidings at all.  
If the slot is already full and the train cannot acquire the slot, the train immediately proceeds to order 18.  
This diverts the train into the siding via another reversing siding.  
The train is held in the siding by a routing restriction on all the siding exit signals which waits until the train can acquire the slot.

![Slots example](Features/images/slots-example-3.png)

See above for a diagram of the positions of orders 16 to 21.  
Using conditional orders in this ways allows more flexible placement or selection of queuing sidings.

#### Example 3: Using conditional orders and slots for dynamic dispatch of trains

![Slots example](Features/images/slots-example-4.png)

In this example a single set of trains with shared orders services multiple producing stations.  
When one of the producing stations has more than a threshold quantity of cargo waiting, a single train is dispatched from
the sidings to that station.  
(Alternatively a depot or station could be used instead of sidings).  
Each producing station has an associated slot of capacity 1. This is to ensure that only one train at a time is dispatched to each station.  

This allows using fewer trains than there are loading stations to be serviced.

For each of the producing stations:

1. Use a conditional order to check whether there is enough cargo waiting at the station, if not skip this station.
2. Try to acquire the slot for this station, if not (meaning that another train has already been dispatched there) skip this station.
3. Go to the producing station and load cargo.
4. Release the slot for the station.
5. Go to the accepting station and unload cargo.
6. Return to the sidings.

The train will not move from the waiting sidings waypoint/depot/station if there are no stations available to load from such that the conditional
order jumps lead to the order for the waypoint/depot/station where the train is already waiting.

![Slots example](Features/images/slots-example-5.png)

A timetabled wait time should be added to the sidings waypoint, depot or station order where the train waits.

#### Example 4: Bidirectionally signalled lines

In this example a single track line is signalled in both directions.  
Multiple trains can travel in the same direction on the line at once.  
Slots are used to avoid a deadlock where trains travel in opposite directions on the single line at the same time and block each other.

One slot is required for each direction. Each slot should have a capacity at least as large as the number of trains which could
be travelling in the same direction at the same time.

![Slots example](Features/images/slots-example-6.png)

Here two trains have entered the single line heading north. Both trains acquired the northbound slot, such that the occupancy of the northbound slot is two,
and the southbound slot is empty.

If the southbound slot was not empty, the trains would wait at the signal before the single track and not acquire the northbound slot.

The slot is released after the train has left the single track section.

![Slots example](Features/images/slots-example-7.png)

At the other end, a train is waiting because the northbound slot is not empty. It does not acquire the southbound slot and proceed past the signal
until the northbound slot is empty, indicating that there are no trains using the single line heading north.

This type of layout is useful when terrain, expense or other constraints make double-tracked lines impractical, but more capacity is required than can be achieved
by not signalling the single track at all such that only one train could occupy the single track at once.


**Variation:** The slot acquire and wait at the entrance to the single track section can be moved to the first signal within the single track section.  
This is mainly useful when the transition between double track and single track is also a junction, and not all approaching trains are headed for the single track.

Similarly, the slot release can be moved to the last signal within the single track section.

The signal direction tests are needed so that the slot actions are not applied when passing the signals in the opposite direction.

![Slots example](Features/images/slots-example-9.png)

#### Example 5: Diverting slow trains into a siding to allow fast trains behind to overtake

![Slots example](Features/images/slots-example-8.png)

In this example, slow trains are automatically diverted into a siding if they're followed by one or more fast trains, to allow them to overtake.  
This example uses the train's cargo (passengers) to differentiate between fast and slow trains, but this could instead be done using other conditions
such as maximum speed, current destination, train group, train weight, etc.

Well ahead of the siding (shown in the inset viewport), trains considered "fast" try to acquire the slot.  
The slot capacity should be large enough to that a fast train will always be able to acquire the slot, even if there
are other fast trains in the section.  

The signal at the end of the siding is set to deny trains which are in the slot. Fast trains which have acquired the slot should never use the siding.  
Trains which are in the siding should wait there until there are no trains in the slot.

The signal on the mainline track adds a pathfinder penalty for trains which are not in the slot, if the slot is not empty.  
This diverts slow trains into the siding if there is one or more fast trains behind and the siding is empty.  
Deny or a very large penalty should not be used, as this can cause a deadlock if two slow trains
are followed by a fast train, and the second slow train stops on the mainline waiting for the siding to become available.  
This signal also releases the slot from fast trains as they go past.

The distance between the slot acquire signal and the siding should be far enough that a slow train in front won't have reached the siding yet, but not so long
that a slow train in the siding doesn't get a chance to exit before another fast train comes past.

#### Other potential uses for slots:

* Complex one train working lines
* Congestion/queueing control
* Deadlock prevention on tricky flat junctions
* Conditional order dispatch across multiple trains
* Conflict prevention in general
* Prioritisation at junctions


### Counters

Counters are named variables which can be modified by a routefinding restriction program when a train passes a signal.  
Counters can be used in conditionals in routefinding restrictions and programmable pre-signal programs, and in conditional orders.  
The main use case for counters is counting trains and round-robin behaviour.  
For counting the number of trains on a particular section of track, slots should be used instead.

Using counters to store state makes "logic trains" and similar workarounds unnecessary.

Counters are not shown in the user interace by default, **"Show advanced routing restriction features"** must be enabled.

Counters can be created, deleted, renamed and have their value manually changed by selecting "Manage counters" in the train list window "Manage list" dropdown.

![Aesthetically suboptimal](Features/images/counter-before.png) ![A bit tidier, using counters](Features/images/counter-after.png) ![Details](Features/images/counter-detail.png)


### Programmable pre-signals

Programmable pre-signals are combo pre-signals, with programmable conditions for whether the signal is red or green.  
Programmable pre-signals are block signals, with no support for path signalling.  
Programmable pre-signal programs cannot test any properties of trains, and are run even if there is no train approaching the signal.  
In most cases, routefinding restrictions are more useful.

Unlike routefinding restrictions, programmable pre-signal programs end when the first "Set signal state" line is reached.

Programmable signals are not shown in the signal window by default, **"Show programmable pre-signal feature"** must be enabled.

![Programmable pre-signals example](Features/images/prog-presignals-0.png)
