import discord

char_map = {
    2: "<:2048_2:885345927492161557>",
    4: "<:2048_4:885345927303409674>",
    8: "<:2048_8:885345927836082186>",
    16: "<:2048_16:885345927315992677>"
}


class Grid:
    def __init__(self, size: int, default_char: str):
        self.size = size
        self.default_char = default_char

        self.rows, self.tiles = self.new_grid()

    def new_grid(self):
        rows = []
        tiles = []

        for x in range(self.size):
            r = []
            t = []
            for y in range(self.size):
                r.append(self.default_char + " ")
                t.append(Tile(0))

            rows.append(r)
            tiles.append(t)

        return rows, tiles

    async def send_grid(self, ctx):
        print(self.tiles)

        for x in self.rows:
            await ctx.channel.send(list_to_str(x))

    def plot_char(self, val, x, y):

        self.tiles[y - 1][x - 1] = Tile(val)
        self.rows[y - 1][x - 1] = char_map[val] + " "

    def move_tile(self):
        return


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
