import discord
import discord.utils
import requests
import random
import os
from dotenv import load_dotenv

import db
load_dotenv('.env')


class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("pog "):
            command = message.content.split("pog ", 2)[1]

            if command == "quote":
                # By using the InspiroBot API, we can retrieve a random quote.
                response = requests.get("https://inspirobot.me/api?generate=true")
                await message.channel.send(str(response.content).split("'")[1])

            if command.startswith("eat "):
                choices = [
                    "was devoured with a light coating of viscous petroleum.",
                    "was far too salty, you can have it back.",
                    "didn't have enough lamb sauce. https://www.youtube.com/watch?v=zOXDcGq7Ohg",
                    "was drizzled with lemon juice before eating.",
                    "is not succulent enough for pogbot.",
                    "tasted like bok choy.",
                    "was lightly seasoned and burnt to perfection.",
                    "got carbon'd.",
                    "was sizzled in a pool of their own blood.",
                    "was fed to the goldfish.",
                    "went down great with a glass of screams of agony.",
                    "was sacrificed to the kiddies.",
                    "got turned into reconstituted juice."
                ]

                user = command.split("eat ", 2)[1]

                await message.channel.send(f"{user} " + choices[random.randrange(0, len(choices))])

            if command == "pogness":
                pogness = random.randrange(0, 100)
                if pogness < 50:
                    comment = "Ur trash lmao. Get pog smh."
                elif pogness == 69:
                    comment = ":smirk:"
                else:
                    comment = "Much pogness. Congrats."

                embed = discord.Embed(
                    title=comment,
                    description=f"{message.author.display_name} is {pogness}% pog.",
                    color=0xFF5733
                )
                embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)

                await message.channel.send(embed=embed)

            if command == "rickroll":
                choices = [
                    'Random article sourced from Google News: '
                    'https://www.theraleighregister.com/after-the-peak-whats-in-store-for-australia-now.html',
                    "Don't forget to take a break! Take some time to relax: "
                    "'https://www.youtube.com/watch?v=V-_O7nl0Ii0",
                    'Random meme sourced from r/memes: https://www.youtube.com/watch?v=RvBwypGUkPo',
                    'Random article sourced from Google News: https://www.youtube.com/watch?v=xfr64zoBTAQ',
                    'Funni doggo: https://www.youtube.com/watch?v=j5a0jTc9S10'
                ]
                c = choices[random.randrange(0, len(choices))]
                await message.delete()
                await message.channel.send(c)

            if command.startswith("sus"):
                await message.author.send("Did someone say sus 😱😱😱 ‼️‼️‼️‼️ IS THAT AN AMONG US REFERENCE????????"
                                          "I PLAY AMONG US IT IS THE BEST GAME 🔥🔥🔥🔥💯💯💯💯 !!! "
                                          "AMONG US? IMPOSTER IS RED!! I AM SUS! ANY SUS ? ANY SUS"
                                          "NOT SUS I WAS VENTING 😂🤣😂🤣😂🤣😂😂😂🤣🤣🤣😂😂😂 ")


client = Client()
client.run(os.getenv('TOKEN'))
