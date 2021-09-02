import asyncio
import random
from PIL import Image, ImageDraw, ImageFont
import requests
import music

import discord

music_queue = []
is_playing = False
client = discord.Client()


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

        with open('quote.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)

    if message.content.startswith('!pogplay'):

        link = message.content.split('!pogplay ', 1)[1]
        mp3 = music.get_mp3(link)

        music_queue.append(mp3)

        # adding to queue

        voice_channel = message.author.voice.channel

        if not get_playing_state():
            while len(music_queue) > 0:
                if voice_channel is not None:
                    is_playing = True
                    vc = await voice_channel.connect()

                    vc.play(discord.FFmpegPCMAudio(music_queue[len(music_queue) - 1]), after=lambda e: print("done", e))
                    message.channel.send("Now playing: " + str(music_queue[len(music_queue) - 1]))

                    while not vc.is_done():
                        await asyncio.sleep(1)

                    vc.stop()
                    music_queue.remove(0)

                    if len(music_queue) == 0:
                        is_playing = False
                        await vc.disconnect()
                        break
        else:
            message.channel.send("Added to queue")
            return


def get_playing_state():
    return is_playing



client.run('ODgyNzg1NTgxNTk4Mzk2NDg4.YTAcJA.nYaVqzfdbth5arqKOKmTV12we18')
