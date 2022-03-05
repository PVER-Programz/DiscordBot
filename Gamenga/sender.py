# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

DESTid = 805687858907447306
TYPE = "dm"

client = discord.Client()


@client.event
async def on_ready():
	global DESTid
	global TYPE

	while 1:
		send = input("\n::> ")
		if send != "":
			if TYPE == "dm":
				reciever = await client.fetch_user(DESTid)
				await reciever.create_dm()

				if send.startswith("/r"):
					ref = input("ref-> ")
					if ref != "":
						await reciever.dm_channel.send(send[2:], reference = await reciever.dm_channel.fetch_message(ref[19:]))
				else:
					await reciever.dm_channel.send(send)

			elif TYPE == "cha":
				if send.startswith("/r"):
					ref = input("ref-> ")
					if ref != "":
						outputChannel = client.get_channel(int(DESTid))
						await outputChannel.send(send[2:], reference = await outputChannel.fetch_message(ref[19:]))
				else:
					await client.get_channel(int(DESTid)).send(send)
			else:
				print("ERROR in TYPE")
		else:
			cmdchoice = input("[=CMD=] ")
			if cmdchoice == "dm":
				askid = input("DMid >> ")
				DESTid = askid
				TYPE = "dm"
				print(f"[ {DESTid} ] == [ {await client.fetch_user(askid)} ]")
			elif cmdchoice == "cha":
				askid = input("CHAid >> ")
				DESTid = askid
				TYPE = "cha"
				print(f"[ {DESTid} ] == [ {await client.fetch_channel(askid)} ]")

@client.event
async def on_message(message):
	# reciever = await client.fetch_user('805687858907447306')

	# if (message.channel != reciever.dm_channel) or (message.author != reciever):
	# 	return
	# else:
	# 	print(message.content)
	# 	send = input("\n::> ")
	# 	if send != "":
	# 		await reciever.create_dm()
	# 		await reciever.dm_channel.send(send)
	# 	else:
	# 		return
	pass

client.run(TOKEN)
