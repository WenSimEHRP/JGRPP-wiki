## Day length

The day length factor setting adjusts the passage of time in the game.  
A value of 1 is the same as in vanilla OpenTTD.  
Values larger than 1 increase the length of a calendar day by this factor.

### Things which stay the same in calendar time

These still happen on a per calendar day, per calendar month or per calendar year basis.  
As the day length setting is increased, these will occur more slowly in real time.

* Town and industry cargo production  
  (The town and industry cargo scaling settings can be used to compensate for this if needed).
* Town growth
* Grass and tree growth
* Seasonal changes such as snow line movements
* Infrastructure maintenance costs
* Ratings calculations (towns and stations)
* Inflation
* Introduction and expiry of vehicle, object, station, house, etc. models

### Things which stay the same in real time

These occur at the same real time speed regardless of the value of the day length factor setting.

* Vehicle movement
* Vehicle running costs  
  (Note that running costs are per unit real time that the vehicle is running, but as years becomes longer, the headline yearly figure also increases).
* Vehicle ageing
* Animations and visual effects
