import discord
import keyboard



client = discord.Client()

@client.event
async def on_ready():
        print("---------------------")
        print("Network XRYT is on")
        print("Commands are now active")
        print(client.user.name)
        print(client.user.id)
        print("---------------------")


@client.event
async def on_message(message):
        print(message.content)
        keyboard.press_and_release(message.content)

client.run('insert your token here')