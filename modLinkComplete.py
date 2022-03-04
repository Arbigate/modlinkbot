"""
Copyright notice:

Parts of this code are based on https://github.com/JonathanFeenstra/discord-modlinkbot:

Copyright (C) 2019-2021 Jonathan Feenstra

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import discord
import re
import aiohttp
import os
from dotenv import load_dotenv
from discord.ext import commands
from modLink import get_modlink
from modLink import parse_query

load_dotenv()

class ModlinkBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='^')
        self.loop.create_task(self.startup())

    async def startup(self):
        self.session = aiohttp.ClientSession()

    async def close(self):
        await self.session.close()
        await super().close()

    async def get_modlink(self, query):
        async with self.session.get("https://search.nexusmods.com/mods", params={"terms": parse_query(query), "game_id": 1704}) as resp:
            if resp.status == 200:
                data = await resp.json()
                results = data["results"]
                if results:
                    return results[0]
            
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self))

    async def on_message(self, message):
        if message.author == self.user:
            return

        queries = re.findall('{(.*?)}', message.content)
        if len(queries) > 5:
            return await message.channel.send('You cannot link more than 5 mods in a message.')
        for query in queries:
            if query.lower() == "lux": #NOTE: This is a temporary measure, and I plan to do this differently in the future. I just needed a quick fix, since I'll implement the "full" version along with many other functions in the next version. 
                lux_embed = discord.Embed(title= "Lux")
                lux_embed.add_field(name="Special Edition", value = 'https://www.nexusmods.com/skyrimspecialedition/mods/43158')
                lux_embed.add_field(name="Information", value = 'If you have any issues with this bot or want the source code, please message Arbigate#6162', inline=False)
                await message.channel.send(embed=lux_embed)
                continue
            modlink = await self.get_modlink(query)
            if modlink is not None:
                embed = discord.Embed(title= modlink["name"])
                embed.add_field(name="Special Edition", value = 'https://www.nexusmods.com' + modlink["url"])
                embed.add_field(name="Information", value = 'If you have any issues with this bot or want the source code, please message Arbigate#6162', inline=False)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send("There were no results for that search term.")

bot = ModlinkBot()
bot.run(os.getenv("DISCORD_TOKEN"))
