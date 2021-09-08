import discord


class Grid:
    def __init__(self, size: int, default_char: str):
        self.size = size
        self.default_char = default_char

        self.rows = self.new_grid()

    def new_grid(self):
        rows = []

        count = 0
        for x in range(self.size):
            rows.append([])
            for y in range(self.size):
                rows[count].append(self.default_char + " ")

            count += 1

        return rows

    def send_grid(self, ctx):
        for x in self.rows:
            for y in x:
                await ctx.channel.send(y)


class Tile:
    def __init__(self, value):
        self.num = value

    def replace_num(self, new_value):
        self.num = new_value
