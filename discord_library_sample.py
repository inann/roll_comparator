import discord
import asyncio

client = discord.Client()

def check_for_rollers(reaction, user):
    reaction_string = str(reaction.emoji)
    if reaction_string.startswith('✋'):
        return user

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!rolloff'):
        message = await client.send_message(message.channel, 'Who\'s rolling?')
        res = await client.wait_for_reaction(
            message=message, check=check_for_rollers)
        print('LENGTH: ' + str(len(res)))
        await client.send_message(message.channel, 'User {0.user} is rolling!'.format(res))

client.run('')
