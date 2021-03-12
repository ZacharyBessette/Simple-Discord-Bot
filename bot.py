import discord
import random
import time

client = discord.Client()

bot_token = "Enter bot token here"
audio_file_path = 'Enter Audio Path Here'

@client.event
async def on_ready():
    print('We have successfully connected as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'league' in message.content:
        reply_choice = ['You will be forever Bronze', 'Need to get carried again?',
                        'Hes not responding because he doesnt like you', 'Eager to be farmed again?']
        reply_num1 = random.randint(0, len(reply_choice)-1)
        await message.channel.send(reply_choice[reply_num1])

    if client.user.mentioned_in(message) or 'roboted' in message.content.lower().replace(" ", ""):
        await message.channel.send('Hey, ( ͡° ͜ʖ ͡°)')

    if any([keyword in message.content.lower().replace(" ", "")[message.content.lower().find('>'):] for
            keyword in ('four', '4', 'for')]):
        print("<four detected>")
        # Only triggers if any of the message keys are present in the text with no characters besides " " between them

        message_raw = message.content.lower()

        if '<@' in message_raw:
            message_raw = message_raw[message_raw.find('>'):]

        for i in range(len(message.content.lower())):
            if i < len(message_raw):
                while i < len(message_raw) and message_raw[i] == 'f' and not message_raw[i+1].isalpha():
                    message_raw = message_raw[:i+1] + message_raw[i+2:]
            if i+2 < len(message_raw):
                while i+1 < len(message_raw) and message_raw[i+1] == 'o' and not message_raw[i+2].isalpha():
                    message_raw = message_raw[:i+2] + message_raw[i+3:]
            if i+3 < len(message_raw):
                while i+2 < len(message_raw) and message_raw[i+2] == 'u' and not message_raw[i+3].isalpha():
                    message_raw = message_raw[:i+3] + message_raw[i+4:]
            if i+4 < len(message_raw):
                while i+3 < len(message_raw) and message_raw[i+3] == 'r' and \
                        (not message_raw[i+4].isalpha() and (message_raw[i+4] != "!")):
                    message_raw = message_raw[:i+4] + message_raw[i+5:]

        # TODO: Can probably fix up the above code some
        # TODO (maybe): consonants that don't result in crisp FOUR sound; d, g, j, o, u, y

        message_list = message_raw.split()

        msg = ""

        for i in range(len(message_list)):
            if 'four!' in message_list[i]:
                message_list[i] = message_list[i].replace('four!', 'FOUR!')
            elif any(word in message_list[i] for word in ('four', 'for', '4')):
                message_list[i] = message_list[i].replace('four', 'FOUR!')
                message_list[i] = message_list[i].replace('for', 'FOUR!')
                message_list[i] = message_list[i].replace('4', 'FOUR!')
                enunciated_fours = False

            msg += message_list[i] + " "
        if enunciated_fours:
            await message.channel.send('Thank you for enunciating your fours!')
        else:
            await message.channel.send('Please enunciate your fours:')
        await message.channel.send(msg)

        if message.author.voice:
            vc = await message.author.voice.channel.connect()
            vc.play(discord.FFmpegPCMAudio(audio_file_path))
            time.sleep(1)
            vc.stop()
            await vc.disconnect()

client.run(bot_token)
#Holla Holla Get Dolla bot
#client.run('NTQ2NDYwOTMyOTIyOTMzMjQ4.XGiRZw.IzglQ3WmNVWsS8Djvj9DJcyO180')
