import discord
from discord.ext import commands
import random
import os 
from func import *

TOKEN = os.environ["TOKEN"]
bot = commands.Bot(command_prefix='/')

@bot.command()
async def atcoder(ctx, message):

    lower, upper = parse(message)
    if lower == INF and upper == INF:
        lower, upper = color_req(message)

    problems = get_problems(lower, upper)

    if(len(problems) == 0) :
        await ctx.send("問題がありません")
        return  

    rnd = random.randrange(len(problems) - 1)
    problem = str(problems[rnd])

    contest = str(problem[0:len(problem) - 2]).replace('_', '-')
    if contest[len(contest) - 1] == "-" : contest = contest[0 : len(contest) - 1]
    if contest[0:4] == "code" : contest = fix_code_fes_link(contest)

    link = "https://atcoder.jp/contests/" + contest + "/tasks/" + problem
    await ctx.send(link)

bot.run(TOKEN)
