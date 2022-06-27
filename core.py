import discord, json, requests

from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, BadArgument
from discord.utils import get
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event
async def on_ready():
    print("#"*30 + "\n#" + " "*8 + "Bot is ready!" + " "*7 + "#" + "\n" + "#"*30)

#################################
#                               #
#           БАН ЮЗЕРА           #
#                               #
#################################

@bot.command(name="ban")
@commands.has_permissions(ban_members = True)
async def ban(ctx, member:discord.Member, *, reason=None):
    await ctx.message.delete()
    if member == None:
        return
    # user = await (member.id)
    if reason == None:
             reason = "Причина не указана"
    emb_ban = discord.Embed(title = 'Действие успешно ✅', 
                           description=f"Пользователь <@{member.id}>, добавлен в бан-лист. \n Причина: {reason}")
    emb_ban.set_footer(text = 'Администратором - ' + ctx.author.name,
                             icon_url = ctx.author.avatar_url)
    await member.ban(reason=reason)
    await ctx.send(embed = emb_ban)

#################################
#                               #
#          РАЗБАН ЮЗЕРА         #
#                               #
#################################

@bot.command(name="unban", pass_context=True)
@commands.has_permissions(administrator=True, ban_members = True)
async def unban(ctx, *, id:int):
    await ctx.message.delete()
    user = await bot.fetch_user(id)
    emb_unban = discord.Embed(title = 'Действие успешно ✅', 
                        description=f"Пользователь <@{id}>, убран из бан-листа.")
    emb_unban.set_footer(text = 'Администратором - ' + ctx.author.name,
                         description=f"Примечание: На испытательном сроке.",
                         icon_url = ctx.author.avatar_url)
    await ctx.send(embed = emb_unban)
    await ctx.guild.unban(user)

bot.run(settings['token'])