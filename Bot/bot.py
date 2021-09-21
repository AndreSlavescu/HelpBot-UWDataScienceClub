import discord
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant
import h5py

chatbot = GenericAssistant('Bot/intents.json')
chatbot.train_model()
chatbot.save_model()

print("Bot is running")

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith("$funbot"):
        response = chatbot.request(message.content[7:])
        await message.channel.send(response)

client.run("Your Token Here")
