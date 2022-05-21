"""
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
from discord.ext import commands

class HelpCommand(commands.HelpCommand):

    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title='Modding Support Commands', description="-guide (beginner's modding guide) \n -skse (SKSE tutorial) \n -ae / -downgrade (information about AE) \n -version (breaks down the versions of the game) \n -porting / -converting (tutorial for porting mods) \n -crash (what to do in the event of a crash) \n -modmanager (mod manager comparison) \n -reinstall (how to correctly reinstall the game) \n -laws (10 Commandments of Modding™️)")
        embed.set_footer(text="Bot created by Arbigate and Geborgen. Type -ping to return latency.\n \nPage 1/4 | Type -help2 for next page")
        await self.get_destination().send(embed=embed)
