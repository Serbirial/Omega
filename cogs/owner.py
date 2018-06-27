from discord.ext import commands
import discord


class owner:

    def __init__(self, bot):
        self.bot = bot

    # Hidden means it won't show up on the default help.
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def cog_load(self, ctx, *, cog: str):
        """gotta do cogs.(cog)
        Exampls: (prefix) load cog.fun"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def cog_unload(self, ctx, *, cog: str):
        """gotta do cogs.(cog)
        Exampls: (prefix) load cog.fun"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def cog_reload(self, ctx, *, cog: str):
        """gotta do cogs.(cog)
        Exampls: (prefix) load cog.fun"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


    @commands.command()
    @commands.is_owner()
    async def kick(self, ctx, member: discord.Member):
        'kick someboy'
        await ctx.send(':boot: Cya, {}. Ya loser!'.format(user.name))
        await user.kick()
        print('user has kicked someone')


    @commands.command()
    @commands.is_owner()
    async def ban(self, ctx, member: discord.Member):
        'ban somebody'
        await ctx.send('okay! ill ban {}, for you!'.format(user.name))
        await user.ban()
        print('user has banned someone')

def setup(bot):
    bot.add_cog(owner(bot))
