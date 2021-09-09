from objects import *
import random

two = "<:2048_2:885345927492161557>"
four = "<:2048_4:885345927303409674>"
eight = "<:2048_8:885345927836082186>"
sixteen = "<:2048_16:885345927315992677>"

grid = Grid(4, "<:2048_blank:885345926925914163>")


async def start_game(ctx):
    x = random.randint(1, 4)
    y = random.randint(1, 4)

    print(x, y)
    grid.plot_char(random.choice([two, four]), x, y)
    await grid.send_grid(ctx)
    await ctx.channel.send("Send w, a, s, d to specify direction")
