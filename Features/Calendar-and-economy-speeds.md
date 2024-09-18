## Calendar and economy speeds

The economy speed reduction factor setting adjusts the speed of economic processes (e.g. cargo production, town growth, rating calculations) in the game.  
A value of 1 is the same as in vanilla OpenTTD.  
This was previously known as the day length factor setting.

### Calendar timekeeping mode

In calendar timekeeping mode, the calendar speed (day, month, year progression) is the same as the economy speed.  
Values larger than 1 increase the length of a calendar day by this factor.

#### Things which are proportionally slowed in real time, due to slower economy and calendar speeds (in calendar timekeeping mode)

These still happen on a per calendar day, per calendar month or per calendar year basis.  
As the economy speed reduction factor setting is increased, these will occur more slowly in real time.

* Town and industry cargo production  
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

### Wallclock timekeeping mode

The calendar speed is unaffected by the economy speed reduction factor setting.

The economy speed reduction factor only affects the speed of the economy (e.g. cargo production, town growth, rating calculations, etc.).  
A "period" is the economy analogue of a year. Values larger than 1 increase the length of a period by this factor.

#### Things which are proportionally slowed in real time, due to a slower economy speed (in wallclock timekeeping mode)

These still happen on a per period (and subdivisions of a period) basis.  
As the economy speed reduction factor setting is increased, these will occur more slowly in real time.

* Town and industry cargo production  
  (The town and industry cargo scaling settings can be used to compensate for this if needed).
* Town growth
* Grass and tree growth
* Infrastructure maintenance costs
* Ratings calculations (towns and stations)
* Subsidy durations
* Vehicle service intervals (when not using percentage mode)

### Things which stay the same in real time (in both calendar and wallclock timekeeping modes)

These occur at the same real time speed regardless of the value of the economy speed reduction factor setting.

* Vehicle movement
* Vehicle running costs  
  (Note that running costs are per unit real time that the vehicle is running, but as years becomes longer, the headline yearly figure also increases).
* Ageing of cargo in vehicles
* Animations and visual effects
* Infrastructure sharing fees for using infrastructure owned by other companies, such as rail track and stations
