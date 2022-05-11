from calendar import week
from genericpath import exists
import requests
import json
import operator

'''
This file contains the function for displaying leaderboards for the different game modes. 
The <mode> variable specifies the game mode leaderboard to return:
    0 -> Leaderboard accross all game modes 
    1 -> Leaderboard for solo matches 
    2 -> Leaderboard for duos matches 
    3 -> Leaderboard for trios matches 
    4 -> Leaderboard for squads matches  
'''


def leaderboard(mode):

    # Get input from file
    f = open("users.json")
    users = json.load(f)
    f.close()

    # API key
    # Get your own private API key from: https://fortnitetracker.com/site-api
    custom_header = {"TRN-Api-Key" : "PASTE-THAT-KEY-HERE"}
    
    # Create dictionaries 
    all_users = dict()
    user_ids = dict()

            
    # Loop through 'name': 'platform/name'
    for name, data in users.items():

        url = "https://api.fortnitetracker.com/v1/profile/" + data

        # Send request
        response = requests.get(url, headers = custom_header)

        # Create dictionary with JSON data
        stats = response.json()

        all_users[name] = stats["stats"]
        user_ids[name] = stats["accountId"]
                        

    # OVERALL LEADERBOARD 
    if mode == 0:

        # Create dictionary for players:score
        player_leaderboard = dict()
        
        for name in all_users.keys():

            # Declare/clear variables every iteration
            total_matches = 0
            total_kills = 0
            total_dubs = 0

            # Try to add solos data
            try:
                total_matches += all_users[name]["curr_p2"]["matches"]["valueInt"]
                total_kills += all_users[name]["curr_p2"]["kills"]["valueInt"]
                total_dubs += all_users[name]["curr_p2"]["top1"]["valueInt"]
            
            except:
                #print(name +" has not played solos this season!")
                pass


            # Try to add duos data
            try:
                total_matches += all_users[name]["curr_p10"]["matches"]["valueInt"]
                total_kills += all_users[name]["curr_p10"]["kills"]["valueInt"]
                total_dubs += all_users[name]["curr_p10"]["top1"]["valueInt"]
            
            except:
                #print(name +" has not played duos this season!")
                pass


            # Try to add trios data
            try:
                total_matches += all_users[name]["curr_trios"]["matches"]["valueInt"]
                total_kills += all_users[name]["curr_trios"]["kills"]["valueInt"]
                total_dubs += all_users[name]["curr_trios"]["top1"]["valueInt"]
            
            except:
                #print(name +" has not played trios this season!")
                pass


            # Try to add squads data
            try:
                total_matches += all_users[name]["curr_p9"]["matches"]["valueInt"]
                total_kills += all_users[name]["curr_p9"]["kills"]["valueInt"]
                total_dubs += all_users[name]["curr_p9"]["top1"]["valueInt"]
            
            except:
                #print(name +" has not played squads this season!")
                pass

            '''
            print(name)
            print("Total matches:", total_matches)
            print("Total kills:", total_kills)
            print("Total dubs:", total_dubs)
            '''
            # Calculate total score (dubs + kills) / matches
            try:
                total_score = int(((total_dubs + total_kills) / total_matches) * 1000)

            except: 
                total_score = 0

            player_leaderboard[name] = total_score

            #print("Score:", total_score, "\n")

        print(player_leaderboard)

        # Sort data in descending order
        current_leaderboard = sorted(player_leaderboard.items(), key=operator.itemgetter(1), reverse=True)

        show_leaderboard = "```elm\nThis Season's Leaderboard:"

        place = 1

        for i in current_leaderboard:
            player = "\n" + str(place) + ". " + str(i[0]) + ": " + str(i[1])
            #print(player)
            show_leaderboard += player

            place += 1

        show_leaderboard += "\n\nBased on ((kills + wins) / matches) * 1000```"

        return show_leaderboard
        
        #print(show_leaderboard)

    # SOLOS LEADERBOARD
    if mode == 1:

        # Create dictionary for players:score
        player_leaderboard = dict()
        
        for name in all_users.keys():

            # Declare/clear variables every iteration
            total_matches = 0
            total_kills = 0
            total_dubs = 0

            # Try to add solos data
            try:
                total_matches = all_users[name]["curr_p2"]["matches"]["valueInt"]
                total_kills = all_users[name]["curr_p2"]["kills"]["valueInt"]
                total_dubs = all_users[name]["curr_p2"]["top1"]["valueInt"]
            
            except:
                #print(name +" has not played solos this season!")
                pass

            # Calculate total score (dubs + kills) / matches

            try:
                total_score = int(((total_dubs + total_kills) / total_matches) * 1000)

            except: 
                total_score = 0

            player_leaderboard[name] = total_score

            #print("Score:", total_score, "\n")

        print(player_leaderboard)

        # Sort data in descending order
        current_leaderboard = sorted(player_leaderboard.items(), key=operator.itemgetter(1), reverse=True)

        show_leaderboard = "```elm\nThis Season's Solos Leaderboard:"

        place = 1

        for i in current_leaderboard:
            player = "\n" + str(place) + ". " + str(i[0]) + ": " + str(i[1])
            #print(player)
            show_leaderboard += player

            place += 1

        show_leaderboard += "\n\nBased on ((kills + wins) / matches) * 1000```"

        return show_leaderboard

    # DUOS LEADERBOARD
    if mode == 2:

        # Create dictionary for players:score
        player_leaderboard = dict()
        
        for name in all_users.keys():

            # Declare/clear variables every iteration
            total_matches = 0
            total_kills = 0
            total_dubs = 0

            # Try to add solos data
            try:
                total_matches = all_users[name]["curr_p10"]["matches"]["valueInt"]
                total_kills = all_users[name]["curr_p10"]["kills"]["valueInt"]
                total_dubs = all_users[name]["curr_p10"]["top1"]["valueInt"]
            
            except:
                #print(name +" has not played solos this season!")
                pass

            # Calculate total score (dubs + kills) / matches

            try:
                total_score = int(((total_dubs + total_kills) / total_matches) * 1000)

            except: 
                total_score = 0

            player_leaderboard[name] = total_score

            #print("Score:", total_score, "\n")

        print(player_leaderboard)

        # Sort data in descending order
        current_leaderboard = sorted(player_leaderboard.items(), key=operator.itemgetter(1), reverse=True)

        show_leaderboard = "```elm\nThis Season's Duos Leaderboard:"

        place = 1

        for i in current_leaderboard:
            player = "\n" + str(place) + ". " + str(i[0]) + ": " + str(i[1])
            #print(player)
            show_leaderboard += player

            place += 1

        show_leaderboard += "\n\nBased on ((kills + wins) / matches) * 1000```"

        #print(show_leaderboard)

        return show_leaderboard
        
    
    # TRIOS LEADERBOARD
    if mode == 3:

        # Create dictionary for players:score
        player_leaderboard = dict()
        
        for name in all_users.keys():

            # Declare/clear variables every iteration
            total_matches = 0
            total_kills = 0
            total_dubs = 0

            # Try to add solos data
            try:
                total_matches = all_users[name]["curr_trios"]["matches"]["valueInt"]
                total_kills = all_users[name]["curr_trios"]["kills"]["valueInt"]
                total_dubs = all_users[name]["curr_trios"]["top1"]["valueInt"]
            
            except:
                #print(name +" has not played solos this season!")
                pass

            # Calculate total score (dubs + kills) / matches

            try:
                total_score = int(((total_dubs + total_kills) / total_matches) * 1000)

            except: 
                total_score = 0

            player_leaderboard[name] = total_score

            #print("Score:", total_score, "\n")

        print(player_leaderboard)

        # Sort data in descending order
        current_leaderboard = sorted(player_leaderboard.items(), key=operator.itemgetter(1), reverse=True)

        show_leaderboard = "```elm\nThis Season's Trios Leaderboard:"

        place = 1

        for i in current_leaderboard:
            player = "\n" + str(place) + ". " + str(i[0]) + ": " + str(i[1])
            #print(player)
            show_leaderboard += player

            place += 1

        show_leaderboard += "\n\nBased on ((kills + wins) / matches) * 1000```"

        return show_leaderboard
    
    # SQUADS LEADERBOARD
    if mode == 4:

        # Create dictionary for players:score
        player_leaderboard = dict()
        
        for name in all_users.keys():

            # Declare/clear variables every iteration
            total_matches = 0
            total_kills = 0
            total_dubs = 0

            # Try to add solos data
            try:
                total_matches = all_users[name]["curr_p9"]["matches"]["valueInt"]
                total_kills = all_users[name]["curr_p9"]["kills"]["valueInt"]
                total_dubs = all_users[name]["curr_p9"]["top1"]["valueInt"]
            
            except:
                #print(name +" has not played solos this season!")
                pass

            # Calculate total score (dubs + kills) / matches

            try:
                total_score = int(((total_dubs + total_kills) / total_matches) * 1000)

                # MAYBE FORMULA
                #total_score = int((total_dubs + total_kills) * math.log(total_matches, 10) * 1.5) 

            except: 
                total_score = 0

            player_leaderboard[name] = total_score

            #print("Score:", total_score, "\n")

        print(player_leaderboard)

        # Sort data in descending order
        current_leaderboard = sorted(player_leaderboard.items(), key=operator.itemgetter(1), reverse=True)

        show_leaderboard = "```elm\nThis Season's Squads Leaderboard:"

        place = 1

        for i in current_leaderboard:
            player = "\n" + str(place) + ". " + str(i[0]) + ": " + str(i[1])
            #print(player)
            show_leaderboard += player

            place += 1

        show_leaderboard += "\n\nBased on ((kills + wins) / matches) * 1000```"

        # Returns formatted message to be sent by bot
        return show_leaderboard
        #print(show_leaderboard)

# TESTING
#leaderboard(1)