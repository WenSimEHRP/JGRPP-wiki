## Realistic train braking

![Trains reserving ahead](Features/images/realistic-braking-header.png)

Version 0.40 adds a realistic train braking feature.

This is controlled by the "train braking model" setting.  
The "original" model allows trains to stop instantly.  
In the "realistic" model, described in this document, trains have a stopping distance and will reserve ahead accordingly, trains cannot stop instantly.

The realistic model as described below has many implications for signalling and track layout design, and is therefore an advanced feature which may not be suitable for beginners.  
In particular pre-signals and two-way signals are not permitted, and PBS is used for all signalling, including from normal block signals.
This is a significant change from the layouts suggested by many beginner tutorials.

It is possible to change the braking model during a running game.  
However this may be blocked if there are signals present which are not allowed in the realistic mode.  
These can be found using the `find_non_realistic_braking_signal` console command. (To save some typing, you can do `find<TAB KEY>`).


### Train behaviour changes

Trains will brake in advance such that they can come to a halt within their PBS reservation, and meet any speed restrictions within their reservation.

Trains will attempt to reserve ahead until the braking distance is long enough that they can pass the **next** signal at the target speed at that signal.  
The target speed is affected by:  
* Train maximum speed
* Bridge speed limit
* Rail type speed limit
* Routing restriction speed restrictions

As well as the above, trains will brake in advance of:  
* Stations/waypoints where the train is stopping
* Curves (in realistic acceleration mode)
* Reversing signals or waypoints
* End of reservation (including end of line, depots, etc.)
* Current order speed restrictions

Trains reserving ahead multiple signal blocks is implemented by the "Long Reserve" mechanism, see the [Signalling](Signalling#routefinding-restrictions) page.

Trains only extend their reservation when approaching/passing a signal. (This is the only time that the hypothetical train driver gets an update on how much track there is available ahead).

The decision on whether to extend the reservation can be overriden on a per-signal basis by using the "Long reserve" and "Cancel long reserve" routing restriction actions.  
Occupied blocks and other routing restriction actions which block reservations continue to work in the same way as usual.

Unlike the "original" train braking model, trains can reserve into, out of and through signalled bridges/tunnels.

Changing the track layout in a way that would obstruct or affect the reservation of a moving train is not permitted. Here "moving" means either that the train has a non-zero speed or that it is not in the stopped state.


### Signal behaviour changes

Normal block signals on plain line track behave as automatic signals, and may show a green aspect even when there is no train reservation.  
In all other cases normal block signals default to a red aspect, the same as PBS signals.  
"Plain line" means that the track beyond the signal has no junctions, and leads to either another one-way signal in the same direction, or an end-of-line.

![Plain link block signals](Features/images/realistic-braking-auto-signals.png)

### Speed/distance calculations

Train braking force and deceleration is calculated in a similar way to train acceleration, and so depends on whether the original or realistic acceleration model is used.

The braking deceleration is capped to a maximum value which depends on whether the train is a normal railway train, monorail or maglev. The latter have higher limits.

Most trains which are not heavy freight will meet the braking deceleration cap.

Trains may have a lower effective deceleration and so a longer braking distance when going downhill. This mainly applies to heavy freight.

Braking distance are quadratic in distance with respect to speed, i.e. a train travelling twice as fast has a braking distance 4 times as long.

A table of minimum braking distance for a selection of speeds, on the flat, can be found below.  
Note that these are braking distances used for speed management and reservation distance calculations, and so are slightly conservative with respect to the absolute minimum values for the purposes of defensive driving.

| Speed (km/h)  | Railway distance (tiles) | Monorail distance (tiles) | Maglev distance (tiles) |
| ------------- | ------------------------ | ------------------------- | ----------------------- |
|            50 |                      0.7 |                       0.5 |                     0.4 |
|           100 |                      2.6 |                       1.9 |                     1.4 |
|           150 |                      5.9 |                       4.2 |                     3.3 |
|           200 |                     10.4 |                       7.4 |                     5.8 |
|           300 |                     23.4 |                      16.7 |                    13.0 |
|           400 |                     41.7 |                      29.8 |                    23.1 |


### Track layout/signalling changes

Standard single-direction track with regularly spaced signals, and typical junction and station layouts, can be used in largely the same way as in the "original" braking model.

Single track line with passing loops and single line branches may need modifications.  
This is because trains may reserve more one than passing loop ahead or beyond the end of the single line to avoid needing to brake in advance of the signal at the end of the line or passing loop.  
To avoid this, additional signal(s) should be added which give the hypothetical driver advance notice of the state of the signal at the end of the line or passing loop.  
These extra signals should use the "reserve through" routing restriction action so that they are not considered a place to end a reservation, which would otherwise cause deadlocks or other problems.

![Passing loop extra signals](Features/images/realistic-braking-passing-loops.png)

![Single line exit extra signal](Features/images/realistic-braking-branch.png)


### Things to avoid

Avoid track layouts and order arrangements where the train does not have reasonable advance notice of which way it is going or whether it should be stopping.

In particular: do not use unpredictable conditional orders after a waypoint or other non-stopping order, where the waypoint is directly before a junction where the train could go either way,
or directly before a station it may or may not need to stop at.

The train may need to reserve significantly past the waypoint in order to pass the waypoint at speed.  
If the reservation reaches any following junction it will predict what the conditional order will be and reserve accordingly, however the conditional order would not be actually
reached and definitively evaluated one way or the other until the waypoint is passed.  
Likewise, if train needs to begin braking before reaching the waypoint to stop at the following station it could overshoot the station or brake unnecessarily if the conditional order is mispredicted.

For similar reasons changing the orders of a moving train to call at a station could cause it to fail to stop if it is already going too fast and is too near.

AIs may not be able to build and run a workable railway in this mode, in particular AIs which use traditional block signal patterns are unlikely to do well.  
AIs should be tested with this mode enabled before expecting them to usefully compete.

![Bad use of conditional orders](Features/images/realistic-braking-bad-cond-orders.png)


### Multi-aspect signals

NewGRFs may provide alternative signal graphics and signal styles, and when realistic train braking is enabled, these can also include graphics for additional signal aspects, instead of just red and green.

![Multi-aspect signals](Features/images/multi-aspect-signals.png)

An example of such a GRF is: [Multi-Aspect Signals NewGRF](https://github.com/JGRennison/multi-aspect-signals-grf), this is available in the online content downloader, in-game.

When the "Realistic train braking is aspect limited" setting is enabled, the distance that the train "driver" can tell is clear beyond the signal is limited to the maximum aspect that the signal
could display, as defined by the multi-aspect signal GRF in use.  
In effect, the train "driver" can no longer see an unlimited number of signals ahead.

It is still possible for a train reservation to be longer than that, for example when using the long reserve or reserve through routing restriction actions, but the train "driver" will
not then be able to "see" the full length of the reservation.

When enabled, additional thought is required when designing track layouts and choosing where and at what spacing to place signals, especially at higher speeds.  
This is an advanced feature which is not suitable for beginner players.

Additional signal styles which are are added by signal GRFs may propagate aspects between signals differently, or only be able to show a more restrictive set of signal aspects to the "driver".
