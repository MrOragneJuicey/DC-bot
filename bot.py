import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True  # Allow message events to be received

TOKEN = 'MTI2MjEwMjY0MTY3MzI0MDY2Ng.Gi30ba.BvU3qAL3_W7xgOUd17Pcm9exJFqsTI-zlsO3k8'  # Replace with your bot token
CHANNEL_ID = 1262101994227896331  # Replace with your channel ID

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await send_message_loop()

async def send_message_loop():
    channel = bot.get_channel(CHANNEL_ID)
    while True:
        await channel.send("You're gay")
        await asyncio.sleep(3)  # Sends message every 3 seconds

# Ensure bot is properly closed when interrupted
async def close_bot():
    await bot.close()

# Run the bot using an asynchronous main function
async def main():
    try:
        await bot.start(TOKEN)
    finally:
        await close_bot()

# Asynchronously run the main function
if __name__ == '__main__':
    asyncio.run(main())
