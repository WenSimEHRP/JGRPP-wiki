# 真实制动

![Trains reserving ahead](images/realistic-braking-header.png)

真实制动于 0.40 被加入游戏中。

真实制动由“列车制动模型”选项控制。
“原版”模型允许列车立刻停止。
在本页面中描述的“现实”模型中，火车会有一段制动距离，并会相应地提前预留轨道，无法立刻停止。

真实列车制动是一项高级功能，对信号系统和轨道设计有很大影响，因此可能不适合新手。启用真实制动时将无法原版中的逻辑信号（出入口信号、复合信号、块信号），
且只能使用路径信号（块信号使用路径信号的逻辑，并被作为路径信号处理）。

模型可以在游戏进行时被更改，但如果地图上尚存有不兼容的信号则无法更改。
可以使用 `find_non_realistic_braking_signal` 控制台命令找到这些信号。

## 列车行为

火车会提前制动，以便在其路径预留范围内停车，并满足预留范围内的任何速度限制。
火车会尝试提前预留，直到制动距离足够长，以便以该信号的目标速度通过**下一个**信号。目标速度受以下因素影响：

- 火车的最高速度
- 桥梁速度限制
- 铁轨类型速度限制
- 寻路限制速度限制

此外，火车还会在以下设施/命令前提前制动：

- 停靠的车站/路标
- 曲线（在现实加速模式下）
- 反向信号或路点
- 预留范围的终点（包括线路终点、车库等）
- 当前指令速度限制

Trains reserving ahead multiple signal blocks is implemented by the "Long Reserve" mechanism, see the [Signalling](./Signalling.md#寻路限制) page.

Trains only extend their reservation when approaching/passing a signal. (This is the only time that the hypothetical train driver gets an update on how much track there is available ahead).

The decision on whether to extend the reservation can be overriden on a per-signal basis by using the "Long reserve" and "Cancel long reserve" routing restriction actions.
Occupied blocks and other routing restriction actions which block reservations continue to work in the same way as usual.

Unlike the "original" train braking model, trains can reserve into, out of and through signalled bridges/tunnels.

Changing the track layout in a way that would obstruct or affect the reservation of a moving train is not permitted. Here "moving" means either that the train has a non-zero speed or that it is not in the stopped state.

## Signal behaviour changes

Normal block signals on plain line track behave as automatic signals, and may show a green aspect even when there is no train reservation.
In all other cases normal block signals default to a red aspect, the same as PBS signals.
"Plain line" means that the track beyond the signal has no junctions, and leads to either another one-way signal in the same direction, or an end-of-line.

![Plain link block signals](images/realistic-braking-auto-signals.png)

## Speed/distance calculations

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

## Track layout/signalling changes

Standard single-direction track with regularly spaced signals, and typical junction and station layouts, can be used in largely the same way as in the "original" braking model.

Single track line with passing loops and single line branches may need modifications.
This is because trains may reserve more one than passing loop ahead or beyond the end of the single line to avoid needing to brake in advance of the signal at the end of the line or passing loop.
To avoid this, additional signal(s) should be added which give the hypothetical driver advance notice of the state of the signal at the end of the line or passing loop.
These extra signals should use the "reserve through" routing restriction action so that they are not considered a place to end a reservation, which would otherwise cause deadlocks or other problems.

![Passing loop extra signals](images/realistic-braking-passing-loops.png)

![Single line exit extra signal](images/realistic-braking-branch.png)

## Things to avoid

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

![Bad use of conditional orders](images/realistic-braking-bad-cond-orders.png)

## Multi-aspect signals

NewGRFs may provide alternative signal graphics and signal styles, and when realistic train braking is enabled, these can also include graphics for additional signal aspects, instead of just red and green.

![Multi-aspect signals](images/multi-aspect-signals.png)

An example of such a GRF is: [Multi-Aspect Signals NewGRF](https://github.com/JGRennison/multi-aspect-signals-grf), this is available in the online content downloader, in-game.

When the "Realistic train braking is aspect limited" setting is enabled, the distance that the train "driver" can tell is clear beyond the signal is limited to the maximum aspect that the signal
could display, as defined by the multi-aspect signal GRF in use.
In effect, the train "driver" can no longer see an unlimited number of signals ahead.

It is still possible for a train reservation to be longer than that, for example when using the long reserve or reserve through routing restriction actions, but the train "driver" will
not then be able to "see" the full length of the reservation.

When enabled, additional thought is required when designing track layouts and choosing where and at what spacing to place signals, especially at higher speeds.
This is an advanced feature which is not suitable for beginner players.

Additional signal styles which are are added by signal GRFs may propagate aspects between signals differently, or only be able to show a more restrictive set of signal aspects to the "driver".
