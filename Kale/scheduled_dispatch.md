# 计划调度—制定 60 分钟时刻表

在本教程中，我将解释如何使用 JGRPP 当中最棒的功能之一——计划调度。
我会展示两种实现方案，分别是 60 分钟时刻表与 24 小时时刻表。
60 分钟时刻表虽然相对简单但其也可以用来处理复杂调度[^1]。
24 小时时刻表较 60 分钟时刻表而言更复杂，反直觉，
不过这种运营方式更适合于使用 P&T 脚本[^2]的游戏

[^1]: 译注：[Rico's Archipelago Map](https://discord.com/channels/142724111502802944/1134148110654902292)
[^2]: 译注：[Peaks and Troughs](https://www.tt-forums.net/viewtopic.php?t=87840)
（尖峰时刻）游戏脚本可以用来模拟一天不同时段的客流量。游戏脚本由 Erato 开发。

图中所示示例铁路路线的列车完全按计划调度与调度计划[^3]运行。
为整条线路上的列车制定时刻表是一个循序渐进的过程。理想的方法是先制定一列列车的时刻表
（根据需求灵活决定列车列数），
列车在运行的过程中会通过自行记录行车时间与等候时长（停站时长）自动填充时刻表。
我个人习惯单独制定停站时长，所以行车时间相对而言较为重要。
之后开启“自动时刻表”并让列车运行即可。

[^3]: 译注：两者在名称上极为相似，但“计划调度”（Scheduled Dispatch）是 JGRPP 独有的功能，
允许制定更复杂的时刻表，
而“调度计划”（Order List）自《运输大亨》起就在游戏中，
是规定列车行走路线的工具。

列车运行时会自动填充时刻表，同时也设立车站间运行的标准时间。
时刻表窗口的右侧栏中就是确切的到发时间。

你可以在列车的时刻表填充完成之后查看列车的运行时间。
确定所有运行时间之后就可以制定计划调度时刻表了。
运行时间已经确定，因此也不再需要启用“自动时刻表”获取运行时间。
现在你可以关掉“自动”选项然后为你认为必要的站点手动设定停站时间。
双击命令即可修改停站时间。
我在样例中规定每个站点的停站时间为一分钟。
在修改完之后就可以打开计划调度页面了。

在启用计划调度之后，你还需要将时刻表指定到一项命令。
这里我们将时刻表指定到“吉和北站”，也是东侧的终点站。

我们已经设置完毕了计划调度指令，可以添加发车时间[^4]了。
遵循这个时刻表的列车在该站时只会在发车时间发车。

[^4]: 译注：旧版译名为“出发条目”。

不过，既然我们做的是 60 分钟时刻表，在运营前要做的第一件事自然就是将时刻表时长修改为 60 分钟。
时刻表会每小时重复一次。

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
