import discord
import asyncio

client = discord.Client()

first_roll = 0
second_roll = 0
first_user = ''

def check_for_rollers(reaction, user):
    reaction_string = str(reaction.emoji)
    if reaction_string.startswith('✋'):
        return user

def verify_digits(message):
    return message.content.isdigit()

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

@client.event
async def on_reaction_add(reaction, user):
    reaction_string = str(reaction.emoji)
    if reaction_string.startswith('✋'):
        if reaction.message.content.startswith('Who\'s rolling?'):
            if len(reaction.message.reactions) < 2:
                await client.send_message(user, 'What did you roll?')
                roll_result = await client.wait_for_message(author = user, check = verify_digits)
                first_roll = int(roll_result.content)
                first_user = user.name
            elif len(reaction.message.reactions) == 2:
                await client.send_message(user, 'What did you roll?')
                roll_result = await client.wait_for_message(author = user, check = verify_digits)
                second_roll = int(roll_result.message)
                if first_roll < second_roll:
                    await client.send_message(reaction.message.channel, '{} wins!'.format(user.name))
                else:
                    await client.send_message(reaction.message.channel, '{} wins!'.format(first_user))
            else:
                await client.send_message(reaction.message.channel, 'Only two at a time')
            # await client.send_message(reaction.message.channel, '{} rolled {}!'.format(user.name, roll_result.content))


client.run('')
