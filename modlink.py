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

def parse_query(query): #This is lame currently, but I'll improve it later. 
    return query.replace(" ", ",").replace("-", ",")
    
async def get_modlink(self, query):
    if query.lower() not in se_modlink_exceptions:
        async with self.session.get("https://search.nexusmods.com/mods", params={"terms": parse_query(query), "game_id": 1704}) as resp:
            if resp.status == 200:
                data = await resp.json()
                results = data["results"]
                if results:
                    return results[0]

async def get_le_modlink(self, query):
    if query.lower() not in le_modlink_exceptions:
        async with self.session.get("https://search.nexusmods.com/mods", params={"terms": parse_query(query), "game_id": 110}) as resp:
            if resp.status == 200:
                data = await resp.json()
                results = data["results"]
                if results:
                    return results[0]