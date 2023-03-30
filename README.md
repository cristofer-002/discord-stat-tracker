# discord-stat-tracker
## Framework for a Discord bot to fetch Fortnite stats for customized users and display them in a given Discord channel.
### Utilizes the Fortnite Tracker API https://fortnitetracker.com/site-api

The file **blizabelle.py** is the executable file to run the bot (with a version of Python installed).

You will need to set up a bot on the **[Discord Developer Portal](https://discord.com/developers/docs/intro)**
and place the bot token in **blizabelle.py** on line 28.
```
27    ...
28  TOKEN = "PASTE-TOKEN-HERE"
29    ...
```

You will also need to follow the instructions to get your own private API key from the **[Fortnite Tracker](https://fortnitetracker.com/site-api)** site. 
After that, you will need to paste that key in both the **leaderboards.py** file at line 27, and in **weekly_leaderboards.py** at line 48. 
```
# In leaderboards.py
...
27  custom_header = {"TRN-Api-Key" : "PASTE-THAT-KEY-HERE"}
...

# In weekly_leaderboard.py
...
48  custom_header = {"TRN-Api-Key" : "PASTE-THAT-KEY-HERE"}
...
```

Finally, you will need to populate **users.json** with your player data. The format is:
```
"discord-name": "platform/fortnite-name"
```
where "platform" can be:
 ```
    kbm (for PC players)
    gamepad (for console players)
    touch (for mobile players, which I'm not sure even exists anymore?)
 ```

For example, my Discord name is christopher_m, I play on PC, and my Fortnite name is c_dawg_m.
So, in the **users.json** file I would enter: 
```
{
    "christopher_m": "pc/c_dawg_m"
}
```
and a comma afterwards if there are more entries. 

After that you're good to go! The bot just needs run from the console.

## Current commands
There are currently commands for displaying individual user stats:
```
    Lifetime stats: -stats 
    Solo stats: -stats1 
    Duos stats: -stats2 
    Trios stats: -stats3 
    Squads stats: -stats4
```
And commands for displaying current season leaderboards:
```
    Leaderboard (Overall): -leaderboard 
    Leaderboard (Solos): -leaderboard1 
    Leaderboard (Duos): -leaderboard2 
    Leaderboard (Trios): -leaderboard3 
    Leaderboard (Squads): -leaderboard4 
    Leaderboard (Weekly): -weekly 
    Leaderboard (Weekly Debug Mode): -weekly-debug
```
The specific commands can be changed in the **blizabelle.py** file.
