import discord
from discord.ext import commands

import datetime as dt
from datetime import datetime

'''
log collection : channel.history()
'''

TOKEN = "?"

#setting date configurations
delta = dt.timedelta(days=1)
last = datetime.now() - delta

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
      print("Powering up the bot")


@client.command(pass_context=True)
async def collect_logs(ctx, amount=100,):
      channel = ctx.message.channel
      async for message in channel.history(limit=int(amount), after=last):
            
            if message.content == "":
                  list_data = message.embeds
                  for data in list_data:
                        print(data.field)
            else:
                  print(message.content)
            
      await ctx.channel.send('Logs Collected!')
      
      
client.run(TOKEN)
