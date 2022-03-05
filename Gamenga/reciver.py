# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()


@client.event
async def on_ready():
	global shitout
	shitout = client.get_channel(937610897302622248)
	print(f'{client.user} has connected to Discord!\n')
	await client.get_channel(866540307847708694).send("✉️ Messenger mode ACTIVATED")

@client.event
async def on_message(message):
	# reciever = await client.fetch_user('805687858907447306')
	# reciever = await client.fetch_user('747757993893953607')

	# if (message.channel != reciever.dm_channel) or (message.author != reciever):
	# 	return
	# else:
	# 	print(message.content)
		# send = input("\n::> ")
		# if send != "":
		# 	await reciever.create_dm()
		# 	await reciever.dm_channel.send(send)
		# else:
		# 	return
	print(f'[{message.author}] on [{message.channel}]\n{message.content}\n')
	

client.run(TOKEN)
