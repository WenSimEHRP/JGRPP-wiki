## Day length

The day length factor setting adjusts the passage of time in the game.  
A value of 1 is the same as in vanilla OpenTTD.  

### Calendar timekeeping mode

Values larger than 1 increase the length of a calendar day by this factor.

In calendar timekeeping mode, the speed of the economy (e.g. cargo production, town growth, rating calculations, etc.) runs at the same speed as the calendar.  
The economy speed is therefore also slowed by the same factor.

#### Things which are proportionally slowed in real time, due to a slower calendar speed (in calendar timekeeping mode)

These still happen on a per calendar day, per calendar month or per calendar year basis.  
As the day length setting is increased, these will occur more slowly in real time.

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

The calendar speed is unaffected by the day length factor setting.

The day length factor only affects the speed of the economy (e.g. cargo production, town growth, rating calculations, etc.).  
A "period" is the economy analogue of a year. Values larger than 1 increase the length of a period by this factor.

#### Things which are proportionally slowed in real time, due to a slower economy speed (in wallclock timekeeping mode)

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

### Things which stay the same in real time (in both calendar and wallclock timekeeping modes)

These occur at the same real time speed regardless of the value of the day length factor setting.

* Vehicle movement
* Vehicle running costs  
  (Note that running costs are per unit real time that the vehicle is running, but as years becomes longer, the headline yearly figure also increases).
* Ageing of cargo in vehicles
* Animations and visual effects
* Infrastructure sharing fees for using infrastructure owned by other companies, such as rail track and stations
