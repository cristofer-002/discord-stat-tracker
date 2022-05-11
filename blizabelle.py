import json
import discord
from functions import *
from weekly_leaderboard import weekly
from leaderboards import leaderboard

'''
This is the main file for bot execution. 
Individual user data must be entered into <users.json> in the format of:
    "discord-name": "platform/fortnite-name"
where "platform" can be:
    "kbm" (for PC players)
    "gamepad" (for console platers)
    "touch" (for mobile players, which I'm not sure even exists anymore?)

For example, my Discord name is christopher_m, I play on PC, and my Fortnite name is c_dawg_m.
So, in the <users.json> file I would enter: "christopher_m": "pc/c_dawg_m"
and a comma, if there are more entries. 
'''

# Get input from file
f = open("users.json")
users = json.load(f)
f.close()

# Discord bot token
# Get from https://discord.com/developers/docs/intro
TOKEN = "PASTE-TOKEN-HERE"

client = discord.Client()

# Once bot is ready
@client.event
async def on_ready():
    print("The bot has landed...")

# Event for sent message
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0].lower() # Get username
    user_message = str(message.content)
    channel = str(message.channel.name) # Get current channel
    print(f"{username}: {user_message} ({channel})") # Logs all messages sent to console

    # Validate bot did not send message
    if message.author == client.user:
        return #nothing

    # SPECIFY ALLOWED CHANNELS 
    approved_channel = "enter channel where bot will be active"

    # Uncomment second half for more than one channel
    if message.channel.name == approved_channel: #or message.channel.name == "another approved channel":
        
        # Message to call command
        if user_message == "-stats":

            # Send data to function from JSON dictionary
            if username in users:

                try:
                    await message.channel.send(get_stats((users[username]), 0))

                except:
                    await message.channel.send("```No data found!```")

        # SOLO STATS
        elif user_message == "-stats1":

            # Send data to function from JSON dictionary
            if username in users:

                try:
                    await message.channel.send(get_stats((users[username]), 1))

                except:
                    await message.channel.send("```No data found!```")

        # DUOS STATS
        elif user_message == "-stats2":

            # Send data to function from JSON dictionary
            if username in users:

                try:
                    await message.channel.send(get_stats((users[username]), 2))

                except:
                    await message.channel.send("```No data found!```")

        # TRIOS STATS
        elif user_message == "-stats3":

            # Send data to function from JSON dictionary
            if username in users:
                
                try:
                    await message.channel.send(get_stats((users[username]), 3))

                except:
                    await message.channel.send("```No data found!```")

        # SQUADS STATS
        elif user_message == "-stats4":

            # Send data to function from JSON dictionary
            if username in users:
                
                try:
                    await message.channel.send(get_stats((users[username]), 4))

                except:
                    await message.channel.send("```No data found!```")
            

        # WEEKLY LEADERBOARD
        elif user_message == "-weekly":

            try:
                #task = asyncio.create_task(weekly(1))
                await message.channel.send(await weekly(1))

            except:
                await message.channel.send("Error in getting leaderboard!")

        # WEEKLY DEBUG MODE
        elif user_message == "-weekly-debug":

            try:
                await message.channel.send(await weekly(0))

            except:
                await message.channel.send("Error in getting leaderboard!")

        # LEADERBOARD
        elif user_message == "-leaderboard":
            
            try:
                await message.channel.send(leaderboard(0))

            except:
                await message.channel.send("Error in getting leaderboard!")

        # SOLOS LEADERBOARD
        elif user_message == "-leaderboard1":
            
            try:
                await message.channel.send(leaderboard(1))

            except:
                await message.channel.send("Error in getting leaderboard!")

        # DUOS LEADERBOARD
        elif user_message == "-leaderboard2":
            
            try:
                await message.channel.send(leaderboard(2))

            except:
                await message.channel.send("Error in getting leaderboard!")

        # TRIOS LEADERBOARD
        elif user_message == "-leaderboard3":
            
            try:
                await message.channel.send(leaderboard(3))

            except:
                await message.channel.send("Error in getting leaderboard!")

        #SQUADS LEADERBOARD
        elif user_message == "-leaderboard4":
            
            try:
                await message.channel.send(leaderboard(4))

            except:
                await message.channel.send("Error in getting leaderboard!")


        # HELP COMMAND
        elif user_message == "-help":

            await message.channel.send("```elm\nAvailable commands: \nLifetime stats: -stats \nSolo stats: stats1 \nDuos stats: -stats2 \nTrios stats: -stats3 \nSquads stats: -stats4 \n\nLeaderboard: -leaderboard \nLeaderboard (Solos): -leaderboard1 \nLeaderboard (Duos): -leaderboard2 \nLeaderboard (Trios): -leaderboard3 \nLeaderboard (Squads): -leaderboard4 \nLeaderboard (Weekly): -weekly \nLeaderboard (Weekly Debug Mode): -weekly-debug```")

# Run bot run
client.run(TOKEN)