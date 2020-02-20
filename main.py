import discord
import random
import os 
from func import *

TOKEN = os.environ["TOKEN"]
client = discord.Client()

@client.event
async def on_message(message):
    if client.user == message.author : return 
    if len(message.content) < 2 : return 
    if message.content[0] != '\\' : return 

    lower, upper = parse(message.content)
    if lower == INF and upper == INF:
        lower, upper = color_req(message.content)

    problems = get_problems(lower, upper)

    if(len(problems) == 0) :
        await message.channel.send(f"{message.author.mention} 問題がありません")
        return  

    rnd = random.randrange(len(problems) - 1)
    problem = str(problems[rnd])

    contest = str(problem[0:len(problem) - 2]).replace('_', '-')
    if contest[len(contest) - 1] == "-" : contest = contest[0 : len(contest) - 1]
    if contest[0:4] == "code" : contest = fix_code_fes_link(contest)

    link = f"{message.author.mention} \n" + "https://atcoder.jp/contests/" + contest + "/tasks/" + problem
    await message.channel.send(link)

client.run(TOKEN)
