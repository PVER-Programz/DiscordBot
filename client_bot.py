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
	print(f'{client.user} has connected to Discord!')
	helomsg = []
	await client.get_channel(866540307847708694).send("Hello There")

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	sent = message.content.lower()

	if 'phec' in message.content.lower():
		await message.channel.send('Va Va !! Vandhu Phec pannu')
	
	if 'cmd' in message.content.lower():################################## TEST CMD
		await message.channel.send('Ajax', reference=await message.channel.fetch_message('938432359693422632'))
	
	if 'gay' in sent or 'chubkov' in sent:
		await message.channel.send('*touches in chubkov mood*')
	
	if 'dhar uyiroda irukia ?' in sent or 'dhar ping' in sent:
		await message.channel.send("illa sethuten. poda !!", reference = message)
		print(message.author.id)
	
	if 'hello' in sent or 'helo' in sent or '948182088568422422' in sent or 'fehk' in sent or 'fuck' in sent:
		await message.channel.send(file=discord.File("Dhar_signatureDialog.mp3"))
			
	if 'chollu ' in sent:
		await message.channel.send(sent[6:])

	# if 'chollu ' in sent:###:###:###
	# 	await message.channel.send(sent[6:])

	if 'dhar help' in sent:
		# await client.user.edit(nickname="asdf")
		await message.channel.send("""IMPORTANT POINS FOR EXAM:
			- helo
			- tell me to phec i phec u
			- i'm not gay
			- naan enna **chollanum** ??
			- stop dm-ing me 'dhar uyiroda irukia ?'
			- i can dm you if you want
			- naan saava maaten""")
	
	if 'dm me' in sent:
		await message.author.create_dm()
		await message.author.dm_channel.send(f'Send Nudes 😜')
		await message.add_reaction("<:ms:948548311206461510>")
	
	if 'stat  ' in sent:
		await client.change_presence(activity=sent[4:])
	
	if 'savuda' in sent or 'saavuda' in sent or 'sethupo' in sent or 'savu da' in sent or 'saavu da' in sent or'sethu po' in sent:
		await message.channel.send("https://tenor.com/view/gifsblog-goundamani-tamil-funny-comedy-gif-13257096")
		raise Exception("WE'RE DONE !!")
		exit()

client.run(TOKEN)
