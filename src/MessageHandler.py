from Utilities import *

class MessageHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_message(self, message:discord.message):
        if message.author != self.bot.user:
            if "hello" in message.content.lower():
                msg = await message.channel.send("Henlo")
                await asyncio.sleep(10)
                await msg.add_reaction("🗑️")

            if "wait" in message.content.lower():
                await delSend("https://www.youtube.com/watch?v=sBl9qcaQos4", message.channel)