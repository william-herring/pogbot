import discord


class Grid:
    def __init__(self, size: int, default_char: str):
        self.size = size
        self.default_char = default_char

        self.rows = self.new_grid()

    def new_grid(self):
        rows = []

        for x in range(self.size):
            r = []
            for y in range(self.size):
                r.append(self.default_char + " ")

            rows.append(r)

        return rows

    async def send_grid(self, ctx):
        for x in self.rows:
            await ctx.channel.send(list_to_str(x))

    def plot_char(self, char, x, y):
        self.rows[y - 1][x - 1] = char + " "


class Tile:
    def __init__(self, value):
        self.num = value

    def replace_num(self, new_value):
        self.num = new_value


def list_to_str(s):
    str1 = ""

    for ele in s:
        str1 += ele

    return str1
