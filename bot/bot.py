import asyncio
import random
from PIL import Image, ImageDraw, ImageFont
import requests
import music
import json
import discord
from time import *

ffmpeg_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"

music_queue = []
is_playing = False
client = discord.Client()
pogplay_enabled = True  # Set false if maintenance needed on pogplay

with open("/Users/herring/Development/pogbot/resources/leaderboard.json", 'r') as file:
    data = json.load(file)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!am i pog'):

        if message.author.name == "Shrivyboi":
            await message.channel.send("aryan is always pog")
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

        fnt = ImageFont.truetype('comic sans.ttf', 30)
        d = ImageDraw.Draw(img)
        d.text((250, 250), quote, font=fnt, fill=(255, 106, 0))

        img.save('quote.png')

        with open('/Users/herring/Development/pogbot/resources/quote.png', 'rb') as f:
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
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio("/Users/herring/Development/pogbot/" + mp3), after=lambda e: print('done', e))
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
        count = 0
        for i in data:
            for d in i.keys():
                if d == message.author.name:
                    data[count][message.author.name] = data[count][message.author.name] + 1
                    with open("/Users/herring/Development/pogbot/resources/leaderboard.json", "w") as file:
                        json.dump(data, file)

                    await message.channel.send(message.author.name + " has " + str(data[0][message.author.name]) + " total pogs.")
                    return

            count += 1

        entry = {message.author.name: 1}
        data.append(entry)

        with open("/Users/herring/Development/pogbot/resources/leaderboard.json", "w") as file:
            json.dump(data, file)

        await message.channel.send(message.author.name + " has " + str(data[0][message.author.name]) + " total pogs.")


def get_playing_state():
    return is_playing


client.run('ODgyNzg1NTgxNTk4Mzk2NDg4.YTAcJA.0bUiwgNPN-VgxVrH_n3XndrZjBE')
