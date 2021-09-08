import discord


class Grid:
    def __init__(self, size: int, default_char: str):
        self.size = size
        self.default_char = default_char

        self.rows = self.new_grid()

    def new_grid(self):
        rows = []

        for x in range(self.size):
            r = " "
            for y in range(self.size):
                r += self.default_char + " "

            rows.append(r)

        return rows

    async def send_grid(self, ctx):
        for x in self.rows:
            await ctx.channel.send(x)


class Tile:
    def __init__(self, value):
        self.num = value

    def replace_num(self, new_value):
        self.num = new_value
