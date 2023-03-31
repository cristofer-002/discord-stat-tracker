import requests

'''
This file contains the function for displaying individual user stats.
The message-senders username, <user_info>, and a function mode, <mode>, are passed into the function,
and returns a formatted message for the Discord bot to send. 
The modes are:
    0 -> Lifetime stats
    1 -> Solo stats
    2 -> Duos stats
    3 -> Trios stats
    4 -> Squads stats
'''

def get_stats(user_info, mode):
    custom_header = {"TRN-Api-Key" : "PASTE-THAT-KEY-HERE"}
    url = "https://api.fortnitetracker.com/v1/profile/" + user_info

    # Send request
    response = requests.get(url, headers = custom_header)
    print(response.status_code)

    # Create dictionary with JSON data
    stats = response.json()
    
    # GET LIFETIME STATS
    if mode == 0:

        # Username
        print(stats["epicUserHandle"])
        user = stats["epicUserHandle"]

        # Total matches
        print(stats["lifeTimeStats"][7])
        matchTotal = stats["lifeTimeStats"][7]["value"]

        # Top 10s
        print(stats["lifeTimeStats"][3])
        topTens = stats["lifeTimeStats"][3]["value"]

        #Dubs
        print(stats["lifeTimeStats"][8])
        dubs = stats["lifeTimeStats"][8]["value"]

        # Win rate
        print(stats["lifeTimeStats"][9])
        winRate = stats["lifeTimeStats"][9]["value"]

        # Kills
        print(stats["lifeTimeStats"][10])
        kills = stats["lifeTimeStats"][10]["value"]

        # Kill / death ratio
        print(stats["lifeTimeStats"][11])
        kD = stats["lifeTimeStats"][11]["value"]

       # Formatted Message
        message = "```" + user + "'s " + "Lifetime Fortnite Stats:\nMatches Played: " + matchTotal + "\nTop 10s: " + topTens + "\nDubs: " + dubs + "\nWin rate: " + winRate + "\nKills: " + kills + "\nKill/death ratio: " + kD + "```"
        return message

    # GET SOLO STATS
    elif mode == 1:

        # Username
        print(stats["epicUserHandle"])
        user = stats["epicUserHandle"]

        # Total matches
        print(stats["stats"]["curr_p2"]["matches"]["value"])
        matchTotal = stats["stats"]["curr_p2"]["matches"]["value"]

        #Dubs
        print(stats["stats"]["curr_p2"]["top1"]["value"])
        dubs = stats["stats"]["curr_p2"]["top1"]["value"]

        # Top 10s
        print(stats["stats"]["curr_p2"]["top10"]["value"])
        topTens = stats["stats"]["curr_p2"]["top10"]["value"]

        # Win rate
        print(stats["stats"]["curr_p2"]["winRatio"]["value"] + "%")
        winRate = stats["stats"]["curr_p2"]["winRatio"]["value"] 

        # Kills per game
        print(stats["stats"]["curr_p2"]["kpg"]["value"])
        kills = stats["stats"]["curr_p2"]["kpg"]["value"]

        # Time played
        print(stats["stats"]["curr_p2"]["minutesPlayed"]["displayValue"])
        runtime = stats["stats"]["curr_p2"]["minutesPlayed"]["displayValue"]

        # Formatted Message
        message = "```" + user + "'s " + "Solo Stats This Season:\nMatches Played: " + matchTotal + "\nDubs: " + dubs + "\nWin rate: " + winRate + "%\nTop 10s: " + topTens + "\nAverage kills per match: " + kills + "\nTotal playtime: " + runtime + "```"
        return message


    # GET DUOS STATS
    elif mode == 2:

        # Username
        print(stats["epicUserHandle"])
        user = stats["epicUserHandle"]

        # Total matches
        print(stats["stats"]["curr_p10"]["matches"]["value"])
        matchTotal = stats["stats"]["curr_p10"]["matches"]["value"]

        #Dubs
        print(stats["stats"]["curr_p10"]["top1"]["value"])
        dubs = stats["stats"]["curr_p10"]["top1"]["value"]

        # Win rate
        print(stats["stats"]["curr_p10"]["winRatio"]["value"] + "%")
        winRate = stats["stats"]["curr_p10"]["winRatio"]["value"] 

        # Kills per game
        print(stats["stats"]["curr_p10"]["kpg"]["value"])
        kills = stats["stats"]["curr_p10"]["kpg"]["value"]

        # Time played
        print(stats["stats"]["curr_p10"]["minutesPlayed"]["displayValue"])
        runtime = stats["stats"]["curr_p10"]["minutesPlayed"]["displayValue"]

        # Formatted Message
        message = "```" + user + "'s " + "Duos Stats This Season:\nMatches Played: " + matchTotal + "\nDubs: " + dubs + "\nWin rate: " + winRate + "%\nAverage kills per match: " + kills + "\nTotal playtime: " + runtime + "```"
        return message

    # GET TRIOS STATS
    elif mode == 3:

        # Username
        print(stats["epicUserHandle"])
        user = stats["epicUserHandle"]

        # Total matches
        print(stats["stats"]["curr_trios"]["matches"]["value"])
        matchTotal = stats["stats"]["curr_trios"]["matches"]["value"]

        #Dubs
        print(stats["stats"]["curr_trios"]["top1"]["value"])
        dubs = stats["stats"]["curr_trios"]["top1"]["value"]

        # Win rate
        print(stats["stats"]["curr_trios"]["winRatio"]["value"] + "%")
        winRate = stats["stats"]["curr_trios"]["winRatio"]["value"] 

        # Kills per game
        print(stats["stats"]["curr_trios"]["kpg"]["value"])
        kills = stats["stats"]["curr_trios"]["kpg"]["value"]

        # Time played
        print(stats["stats"]["curr_trios"]["minutesPlayed"]["displayValue"])
        runtime = stats["stats"]["curr_trios"]["minutesPlayed"]["displayValue"]

        # Formatted Message
        message = "```" + user + "'s " + "Trios Stats This Season:\nMatches Played: " + matchTotal + "\nDubs: " + dubs + "\nWin rate: " + winRate + "%\nAverage kills per match: " + kills + "\nTotal playtime: " + runtime + "```"
        return message

    # GET SQUADS STATS
    elif mode == 4:

        # Username
        print(stats["epicUserHandle"])
        user = stats["epicUserHandle"]

        # Total matches
        print(stats["stats"]["curr_p9"]["matches"]["value"])
        matchTotal = stats["stats"]["curr_p9"]["matches"]["value"]

        #Dubs
        print(stats["stats"]["curr_p9"]["top1"]["value"])
        dubs = stats["stats"]["curr_p9"]["top1"]["value"]

        # Win rate
        print(stats["stats"]["curr_p9"]["winRatio"]["value"] + "%")
        winRate = stats["stats"]["curr_p9"]["winRatio"]["value"] 

        # Kills per game
        print(stats["stats"]["curr_p9"]["kpg"]["value"])
        kills = stats["stats"]["curr_p9"]["kpg"]["value"]

        # Time played
        print(stats["stats"]["curr_p9"]["minutesPlayed"]["displayValue"])
        runtime = stats["stats"]["curr_p9"]["minutesPlayed"]["displayValue"]

        # Formatted Message
        message = "```" + user + "'s " + "Squads Stats This Season:\nMatches Played: " + matchTotal + "\nDubs: " + dubs + "\nWin rate: " + winRate + "%\nAverage kills per match: " + kills + "\nTotal playtime: " + runtime + "```"
        return message


# Get full API 
#print(get_stats("pc/butterballo", 0))