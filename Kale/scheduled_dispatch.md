# 计划调度—制定小时级别时刻表

Alright class, so for this lesson I'm going to run you through one of the coolest features in
JGRPP: Scheduled Dispatch. I will show you how to do my favorite two ways to use it which
consists of what I call "60 minute timetables" and "24 hour timetables". The sixty minute version
of this is what I would call SD easy mode - although you can still use this system in a more
advanced way such as Rico's Archipelago Map in #game-journals on the discord where every
service is scheduled for well timed transfers and service levels. The 24 hour version of this is a
bit more complex and unintuitive but meshes very well with the previously discussed gamescript
Peaks and Troughs, as well as being more realistic if you're into that kind of thing. Let's get into
it.

Here's the "SD Example Railway," as well as our timetabling train and its route. You always want
to start this process with one train (or a few depending on how you set things up) to fill out the
timetable automatically by logging travel and wait times. Travel times are the most important as
wait times for me tend to be customized depending on the station or what's going on around it.
So set your train to "automate" and let it run it's route.

As the train goes through it's timetabling run it will fill out travel times between stations for its
schedule. Now the train knows that it takes a certain amount of time between stations and once
this is set it will expect to be there at the time depicted on the right hand side.

Once the train has done its timetabling run you will have all the travel times logged for you.
That's how you know the train is ready to be setup with scheduled dispatch. You will find the
arrival and departure times for each station timetabled on the right hand side next to "A" and "D"
respectively. All you need to do now is click off automate and fill out wait times if you think that's
necessary. For the sake of our example I've given every stop 1 minute waits. You can do this
simply by double clicking on each order you want to add a wait time to. Then you click on
"Scheduled Dispatch."

This will bring up the scheduled dispatch menu. Hit "enable."
Now you need to assign your scheduled dispatch to an order. We're going to use "Yoshiwa
North" here, our eastern terminus.
Alright we've got our Scheduled Dispatch order set and we're ready to add departure slots.
These slots will be picked up by trains arriving at the station and then they will depart once the
time you have set is reached.

First things first though, we want to change the "Duration" to only 60 minutes.
What this does is change your trains schedule to run through 60 minute rotations on every hour
in game. Keeps things simple, simulates a perpetual hour rotation and thus makes it easy to
create and set your schedules, and then intermingle them with other routes eventually.
So here I've ctrl clicked the "add departure slot" button to bring up this "set time" menu. This will
add multiple departure slots at once so you don't have to fill them in individually. This was not
always a feature so in order to do 24 hour timetables you had to set each on individually. How
times have changed. Here I have it set to add a departure slot every five minutes starting from
0000 and finishing at 0100, the end of the hour.

Here's what you end up with, all the departure slots for the current hour are laid out in front of
you. This hour will repeat infinitely and will fill in current times automatically. It's also given us
some information such as "this schedule requires 3 vehicles" to ensure that a train is back in the
station by the time another dispatch slot is ready to be picked up.

Then I created two more trains (make sure to ctrl click these when you hit "Clone Train" so all
the orders are shared) so that to make sure all these departure slots are picked up by the time
the train has done it's full route and "returned to base."

And here's our system in action. Trains depart Yoshiwa North every five minutes, make their
stops and then return to Yoshiwa North to pick up another return slot. If you do this right there
should only be one train waiting at a time.

Here's an example of what you can do with this in game (this is from an older game on JGR
Server 03). "LHAM 08" is a local train (stops at every station) and thus needs to leave right after
"EHAM 04" which is an express (only stopping at select station stops). Depending on the length
of the route there may need to be an overtake eventually, but doing this simple move ensures
that the local stays out of the way of the express without using tons of infrastructure and allows
you to get a lot more out of less tracks and infrastructure.

Another example from an old JGR server 03 game, this is a regional rail system for the city of
Hamamatsu. On the map light blue means 3 trains per hour (so a train every 20 minutes), red is
6 trains per hour (a train every 10 minutes), and yellow is 12 trains per hour (a train every 5
minutes). Everything is timed out so that without significant delays, a regional train will run
through the yellow section where the central station is located every 5 minutes. This leads to
being able to move a really massive amount of passengers around without just spamming trains
and dealing with frequent jams.
