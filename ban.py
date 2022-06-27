import discord, json, requests

from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, BadArgument
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])

# @bot.command(pass_context=True, aliases=['бан'])
# @commands.has_permissions(ban_members = True)
# async def ban(ctx, member:discord.Member, *, reason = None):
#     await ctx.message.delete()
#     embban = discord.Embed(title = 'Действие успешно ✅', 
#                            description=f"Пользователь {member}, добавлен в бан-лист. \n Причина: {reason}")
#     embban.set_footer(text = 'Администратором - ' + ctx.author.name,
#                              icon_url = ctx.author.avatar_url)
#     await ctx.send(embed = embban)
#     if reason == None:
#              reason = "Причина не указана"
#     for ban_entry in banned_users:
#         user = ban_entry.user
#         # await member.ban(reason = reason)
#         await ctx.guild.ban(user)


@bot.command(pass_context=True, aliases=['бан'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, *,member : discord.Member, member_id: int):
    await ctx.guild.ban(discord.Object(id=member_id))
    await ctx.message.delete()
    embban = discord.Embed(title = 'Действие успешно ✅', 
                           description=f"Пользователь {member}, добавлен в бан-лист. \n Причина: {reason}")
    embban.set_footer(text = 'Администратором - ' + ctx.author.name,
                             icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embban)
    if reason == None:
             reason = "Причина не указана"    