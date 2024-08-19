# 经济速度（日长因子）

“经济速度因子”[^1]设置可以用来调整游戏经济周期的时长。
当设置为 1 时，经济速度与原版相同。

[^1]: 自 0.61.0 起由“日长因子”修改为“经济速度因子”。

## 日历计时模式

在此模式中，经济周期与日期绑定。即货物生产、城镇发展、车站评价等都与日期绑定。
自然，经济速度因子越大，一天时间越长。


由于日历速度较慢 (在日历计时模式下)，在实时中按比例减慢的事物

### 这里哪里 todo

### Things which are proportionally slowed in real time, due to a slower calendar speed (in calendar timekeeping mode)

These still happen on a per calendar day, per calendar month or per calendar year basis.
As the day length setting is increased, these will occur more slowly in real time.

* 城镇与货物产出
  (The town and industry cargo scaling settings can be used to compensate for this if needed).
* Town growth
* Grass and tree growth
* Seasonal changes such as snow line movements
* Infrastructure maintenance costs
* Ratings calculations (towns and stations)
* Subsidy durations
* Vehicle service intervals (when not using percentage mode)
* Inflation
* Introduction and expiry of vehicle, object, station, house, etc. models
* Vehicle ageing

## 挂钟计时时间

The calendar speed is unaffected by the day length factor setting.

The day length factor only affects the speed of the economy (e.g. cargo production, town growth, rating calculations, etc.).
A "period" is the economy analogue of a year. Values larger than 1 increase the length of a period by this factor.

### Things which are proportionally slowed in real time, due to a slower economy speed (in wallclock timekeeping mode)

These still happen on a per period (and subdivisions of a period) basis.
As the day length setting is increased, these will occur more slowly in real time.

* Town and industry cargo production
  (The town and industry cargo scaling settings can be used to compensate for this if needed).
* Town growth
* Grass and tree growth
* Infrastructure maintenance costs
* Ratings calculations (towns and stations)
* Subsidy durations
* Vehicle service intervals (when not using percentage mode)

## Things which stay the same in real time (in both calendar and wallclock timekeeping modes)

These occur at the same real time speed regardless of the value of the day length factor setting.

* Vehicle movement
* Vehicle running costs
  (Note that running costs are per unit real time that the vehicle is running, but as years becomes longer, the headline yearly figure also increases).
* Ageing of cargo in vehicles
* Animations and visual effects
* Infrastructure sharing fees for using infrastructure owned by other companies, such as rail track and stations
