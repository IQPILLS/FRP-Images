import discord
from config import bot_id, guild_id, channel_id, tkn

client = discord.Client(guilds=True)


@client.event
async def on_message(message):
    if not message.guild:
        if message.author.id != bot_id:
            guild = client.get_guild(guild_id)
            huh = await guild.fetch_member(message.author.id)
            display_name = huh.nick or message.author.name
            await message.add_reaction('👍')

            channel = client.get_channel(channel_id)

            embed = discord.Embed(title="Новая фотокарточка", color=0x2F3136)
            if message.content:
                embed.description = message.content
            embed.set_author(name=display_name, icon_url=f'https://rp.plo.su/avatar/{display_name}')
            embed.set_image(url=message.attachments[0].url)
            await channel.send(embed=embed)

    else:
        if message.author.id == bot_id:
            await message.add_reaction("👍")
            await message.add_reaction("🍞")
            await message.add_reaction("👎")


@client.event
async def on_ready():
    print('Запущено')

client.run(tkn)
