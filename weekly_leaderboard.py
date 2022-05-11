import json
import aiohttp
import asyncio
import math
import operator
import datetime 


'''
This file contains the function for displaying a weekly leaderboard. 
A dynamic calendar has not been implemented yet, so currently the date range must be manually entered
into the variables START_DATE and END_DATE.

The <mode> variable here can either be:
    0 -> Debug mode (shows long-form data)
    1 -> Regular mode (shows cleaner, relevant data)
'''

# Set dates for weekly leaderboard
START_DATE = "2022-05-08"
END_DATE = "2022-05-14"

# Varibales for displaying start and stop dates later
s = str(START_DATE.split("-")[1]) + "-" + str(START_DATE.split("-")[2])
e = str(END_DATE.split("-")[1]) + "-" + str(END_DATE.split("-")[2])

# Get current week data
start = datetime.datetime.strptime(START_DATE, "%Y-%m-%d")
end = datetime.datetime.strptime(END_DATE, "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days = x) for x in range(0, (end - start).days)]

this_week = []

for date in date_generated:
    this_week.append(date.strftime("%Y-%m-%d"))


# Get input from file
f = open("users.json")
users = json.load(f)
f.close()

users["cldfire"] = "pc/cldfiɍe"


# API key
# Get your own private API key from: https://fortnitetracker.com/site-api
custom_header = {"TRN-Api-Key" : "PASTE-THAT-KEY-HERE"}
        
# Create dictionaries 
all_users = dict()
user_ids = dict()
matches = dict()


# Date parsing function
def vali_date(date):

    # Parse date
    d = date.split("T")
    new_date = d[0]

    if new_date in this_week:
        return True
    else:
        return False


# Sends and awaits HTTP requests to get Epic ID
async def get_id(session, name, url):
    async with session.get(url, headers = custom_header) as response:
        # Create dictionary with JSON data
            stats = await response.json()

            user_ids[name] = stats["accountId"]


# Sends and awaits HTTP requests for matches
async def get_matches(session, name, url):
    async with session.get(url, headers = custom_header) as response:
        # Create dictionary with JSON data
            stats = await response.json()

            #print("\n" + str(stats))

            all_users[name] = stats


async def weekly(mode):

    # Create dictionary for players:score
    player_leaderboard = dict()
    total_g = dict()
    total_k = dict()
    total_d = dict()

    async with aiohttp.ClientSession() as session:

        # TASKS
        tasks = []
        tasks_m = []

        # Loop through 'name': 'platform/name'
        for name, data in users.items():

            # Data for fetching IDs
            url = "https://api.fortnitetracker.com/v1/profile/" + data
            tasks.append(asyncio.ensure_future(get_id(session, name, url)))


        # Gather function
        await asyncio.gather(*tasks)
        
        
        # Loop through and assign matches 
        for id in user_ids.keys():

            match_url = "https://api.fortnitetracker.com/v1/profile/account/" + user_ids[id] + "/matches"  
            tasks_m.append(asyncio.ensure_future(get_matches(session, id, match_url)))

        # Wait for gather 
        await asyncio.gather(*tasks_m)


        # Loop through users
        for user, games in all_users.items():

            #print("\n" + str(user))
            
            # Declare/clear variables every iteration
            total_matches = 0
            total_kills = 0
            total_dubs = 0

            # Loop through user matches
            for game in games:
                
                # Only calculate games in given time frame
                if vali_date(game["dateCollected"]): 

                    # Do not include limited time modes
                    if game["playlist"] == "ltm" or game["playlist"] == "misc":
                        continue
                        
                    else: 
                            # Try to add game data to totals
                        try:
                            
                            total_matches += game["matches"]
                            #print(game["matches"],"\n")
                            total_kills += game["kills"]
                            #print(game["kills"],"\n")
                            total_dubs += game["top1"]
                            #print(game["top1"],"\n")
                            
                        except:
                            #print(name +" has not played solos this season!")
                            pass
                
            # Calculate total score (dubs + kills) / matches **** F O R M U L A
            try:
                #total_score = int(((total_dubs + total_kills) / total_matches) * 1000)
                total_score = int(((10 * total_dubs + total_kills) * min(math.log(total_matches), 1)) * 10)

            except: 
                    total_score = 0

            player_leaderboard[user] = total_score
            total_g[user] = total_matches
            total_k[user] = total_kills
            total_d[user] = total_dubs

        #print(player_leaderboard)

        # Sort data in descending order
        current_leaderboard = sorted(player_leaderboard.items(), key=operator.itemgetter(1), reverse=True)

        show_leaderboard = "```elm\nWeekly Leaderboard (" + s + " to " + e + "):"

        place = 1

        for i in current_leaderboard:

            # Debug mode
            if mode == 0:
                player = "\n" + str(place) + ". " + str(i[0]) + ": " + str(i[1]) +  " (k:" + str(total_k[i[0]]) + " d:" + str(total_d[i[0]]) + " m: " + str(total_g[i[0]]) + ")" 
            
            # Regular
            else:
                player = "\n" + str(place) + ". " + str(i[0]) + ": " + str(i[1])
            
            # Only include players with scores > 0
            if i[1] != 0 and mode == 1:
                show_leaderboard += player

            # Unless debug mode 
            elif mode == 0:
                show_leaderboard += player

            place += 1

        show_leaderboard += "\n\nBased on ((k + 10w) * min(log(matches), 1)) * 10```"

        # Returned message to be sent by bot
        return show_leaderboard
        #print(show_leaderboard)


# for testing
#asyncio.run(weekly(0))