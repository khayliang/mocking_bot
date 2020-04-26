import discord
import random

client = discord.Client()

negative_messages = [
    "Just give up.",
    "Why are you trying so hard",
    "It's just a game.",
    "Stop tryharding",
    "Loser.",
    "Don't you have anything better to do?",
    "I'm so disappointed in you.",
    "You're the epitome of disappointment",
    "I think you should be doing work and not be on here.",
    "This game is the only thing you're good at."
]

#credits https://github.com/nkrim/spongemock
def mock(text, diversity_bias=0.5, random_seed=None):
	# Error handling
	if diversity_bias < 0 or diversity_bias > 1:
		raise ValueError('diversity_bias must be between the inclusive range [0,1]')
	# Seed the random number generator
	random.seed(random_seed)
	# Mock the text
	out = ''
	last_was_upper = True
	swap_chance = 0.5
	for c in text:
		if c.isalpha():
			if random.random() < swap_chance:
				last_was_upper = not last_was_upper
				swap_chance = 0.5
			c = c.upper() if last_was_upper else c.lower()
			swap_chance += (1-swap_chance)*diversity_bias
		out += c
	return out

winston_count = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$waifu'):
        await message.channel.send('weeb.')

    if str(message.author) == "wins#3866":
        if (message.content)[0] == '$':
            number = random.randrange(9)
            await message.channel.send(negative_messages[number])
        else:
            if winston_count == 10:
                winston_count = 0
                new_message = mock(message.content)
                await message.channel.send(new_message)
            else:
                winston_count += 1






client.run('token id here')



