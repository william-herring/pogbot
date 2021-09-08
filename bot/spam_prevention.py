import asyncio

pog_leaderboard_timeout = []


async def timeout_user(user, command, time):
    print("timeout invoked on user: " + user)
    print(pog_leaderboard_timeout)

    if command == "pog":
        pog_leaderboard_timeout.append(user)
        await asyncio.sleep(time)
        pog_leaderboard_timeout.remove(user)
        return
