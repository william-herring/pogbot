import asyncio
import random
from PIL import Image, ImageDraw, ImageFont
import requests
import music
import json
import discord
import spam_prevention
from time import *

ffmpeg_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"

music_queue = []
is_playing = False
client = discord.Client()
root = open("../root_path_config.txt", 'r').read()
pogplay_enabled = True  # Set false if maintenance needed on pogplay

with open(root + "/resources/leaderboard.json", 'r') as file:
    data = json.load(file)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!am i pog'):

        if message.author.name == "coles car insurance":
            await message.channel.send("william is always pog and you know it")
            return

        pog = random.choice(["not pog", "very pog"])
        await message.channel.send(pog)

    if message.content.startswith('!cookie'):
        await message.channel.send("🍪")

    if message.content.startswith('!quote'):
        quote = ('\"' + str(message.content.split("!quote", 1)[1]) + '\"' + " -" + str(message.author.name))

        img = Image.open(requests.get(
            "https://images.unsplash.com/photo-1543157145-f78c636d023d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8Nnx8fGVufDB8fHx8&w=1000&q=80",
            stream=True).raw)

        fnt = ImageFont.truetype('../comic sans.TTF', 30)
        d = ImageDraw.Draw(img)
        d.text((250, 250), quote, font=fnt, fill=(255, 106, 0))

        img.save(root + '/resources/quote.png')

        with open(root + '/resources/quote.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)

    if message.content.startswith('!pogplay') and pogplay_enabled:

        link = message.content.split('!pogplay ', 1)[1]
        mp3 = music.get_mp3(link)

        music_queue.append(mp3)
        print(music_queue)
        queue_id = music_queue.index(mp3)

        # adding to queue

        voice_channel = message.author.voice.channel

        await message.channel.send("Added to queue")

        while queue_id != 0:
            sleep(5)
            queue_id = music_queue.index(mp3)
            print("waiting in queue with " + mp3)

        if voice_channel is not None:
            print("connected")
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio(root + "/bot/" + mp3), after=lambda e: print('done', e))
            await message.channel.send("Now playing: " + mp3)

            while vc.is_playing():
                print("in loop")
                await asyncio.sleep(1)

            print("out of loop")
            vc.stop()
            await vc.disconnect()
            music_queue.remove(mp3)
            print(music_queue)
        else:
            await client.say('User is not in a voice channel.')

    elif message.content.startswith('!pogplay') and not pogplay_enabled:
        await message.channel.send("Pogplay is down right now. Come back later.")

    if message.content.startswith("!queue"):
        if len(music_queue) == 0:
            message.channel.send("The queue is empty. Add a song by using the command !pogplay <YouTube link>")
            return

        message.channel.send("Current queue:")
        for i in music_queue:
            message.channel.send(i)

    if message.content.startswith("!scold "):
        target = message.content.split("!scold ", 1)[1]

        await message.channel.send("Very unpog of you, " + target + ". Think about your actions and apologise.")

    if "pog" in message.content and not message.content.startswith("!"):
        if message.author.name in spam_prevention.pog_leaderboard_timeout:
            await message.channel.send("You are currently in timeout for use of this command.")
            return

        count = 0
        for i in data:
            for d in i.keys():
                if d == message.author.name:
                    data[count][message.author.name] = data[count][message.author.name] + 1
                    with open(root + "/resources/leaderboard.json", "w") as file:
                        json.dump(data, file)

                    await message.channel.send(message.author.name + " has " + str(data[count][message.author.name]) + " total pogs.")

                    await spam_prevention.timeout_user(message.author.name, "pog", 300)
                    return

            count += 1

        entry = {message.author.name: 1}
        data.append(entry)

        with open(root + "/resources/leaderboard.json", "w") as file:
            json.dump(data, file)

        await message.channel.send(message.author.name + " has " + str(data[len(data) - 1][message.author.name]) + " total pogs.")
        await spam_prevention.timeout_user(message.author.name, "pog", 300)

    if message.content.startswith("!leaderboard"):
        await message.channel.send("-LEADERBOARD-")

        for i in data:
            key = ""
            for d in i.keys():
                key = d

            await message.channel.send(key + ":" + str(i[key]))


def get_playing_state():
    return is_playing


def sort_by(x):
    try:
        return int(x[1].split(' ')[0])
    except ValueError:
        return float('inf')


client.run('ODgyNzg1NTgxNTk4Mzk2NDg4.YTAcJA.0bUiwgNPN-VgxVrH_n3XndrZjBE')
