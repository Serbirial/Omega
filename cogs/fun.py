import discord
from discord.ext import commands



class fun:
    """SimpleCog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='repeat', aliases=['copy', 'mimic'])
    async def do_repeat(self, ctx, *, our_input: str):
        """A simple command which repeats our input.
        In rewrite Context is automatically passed to our commands as the first argument after self."""

        await ctx.send(our_input)

    @commands.command(name='add', aliases=['plus'])
    @commands.guild_only()
    async def do_addition(self, ctx, first: int, second: int):
        """A simple command which does addition on two integer values."""

        total = first + second
        await ctx.send(f'The sum of **{first}** and **{second}**  is  **{total}**')

    @commands.command(name='me')
    @commands.is_owner()
    async def only_me(self, ctx):
        """somthing only owner can do"""

        await ctx.send(f'Hello {ctx.author.mention}.')


    @commands.command()
    async def botsupport(self, ctx):
        'things about the bot'
        await ctx.send('This is the Owner version of Starter bot! if you get any errors with your code, then tell @dathidewolf#4041')
        await ctx.send('if you want your own starter bot go here! https://github.com/dathidewolf/Omega (they wont be better than me >:T)')


    @commands.command()
    async def cool(self, ctx, context):
        'are you cool?'
        author = context.message.author.mention
        choices = ['yes', 'no', 'i wouldint count on it', ' definatly not']
        image = random.choice(choices)
        embed = discord.Embed(description=choices.format(author), colour=discord.Colour.blue())
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(fun(bot))
