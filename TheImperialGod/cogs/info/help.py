import discord
from discord.ext import commands
import asyncio
import random

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.utils_commands = [
            'Coinflip',
            'Random_Number',
            'Code',
            'Guess',
            'respect',
            'Poll',
            'Thank',
            'Reverse',
            'eightball',
            'fight',
            'whois',
            'wanted',
            "quote",
            "osay",
            "embed"
        ]
        self.gaws_commands = [
            'gstart',
            'reroll'
        ]
        self.misc_commands = [
            'invite',
            'show_toprole',
            'avatar',
            'candy',
            "hypesquad",
            "support"
            ]
        self.owner_commands = [
                'enableautomod',
                "disableautomod",
                "checkautomod",
        ]
        self.economy_commands = [
            "Withdraw",
            "Balance",
            "Deposit",
            "Slots"
            'Rob',
            'Dice',
            'Leaderboard',
            'Daily',
            'Weekly'
            ]
        self.info_commands = [
            "channelinfo",
            "botinfo",
            "serverinfo",
            "userinfo"
        ]
        self.tips = [
            "Did you know that TheImperialGod has an economy system!",
            "Did you know that TheImperialGod was made by NightZan999?",
            "Did you know that TheImperialGod was coded in a language called Python!",
            f"Did you know that TheImperialGod is in {len(self.client.guilds)} servers!",
            "Did you know that TheImperialGod has over 8,000 lines of code if put in one file!"
        ]

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help command ready!")

    @commands.group(invoke_without_command = True)
    async def help(self, ctx, category = None):
        page1 = discord.Embed(title = "Help", color = ctx.author.color, description = f"""
        **Type `imp help` and then a __category__ for more information for even more information!**\n
        """)
        page1.add_field(name = f":dollar: Economy Commands: [11]", value = "`Balance`, `Beg`, `Serve`, `Withdraw`, `Deposit`, `Slots`, `Rob`, `Dice`, `Leaderboard`, `Daily`, `Weekly` ")
        page1.add_field(name = f"<:moderation:761292265049686057> Moderation Commands: [15]", value = "`Kick`, `Ban`, `Softban`, `Purge`, `Lock`, `Unlock`, `Mute`, `Unmute`, `Unban`, `createrole`, `Announce`, `nick`, `setmuterole`")
        page1.add_field(name = f"<:info:761298826907746386> Information Commands: [{len(self.info_commands)}]", value = f"`userinfo`, `avatar`, `serverinfo`, `whois`, `channelinfo`, `botinfo`,`show_toprole`")
        page1.add_field(name = f":tools: Utilities: [{len(self.utils_commands)}]", value = "`Coinflip`, `Random_Number`, `code`, `guess`, `respect`, `poll`, `thank`, `reverse`, `eightball`, `fight`, `quote`, `osay`, `nick`, `treat`, `embed`")
        page1.add_field(name = f"<:pepethink:791969112771395625> Math Commands [7]:", value = f"`add`, `subtract`, `multiply`, `divide`, `square`, `sqrt`, `pow`")
        page1.add_field(name = f':video_game: Fun: [12]', value = f"`dog`, `cat`, `duck`, `fox`, `panda`, `koala`, `tiger`, `lion`, `snake`, `redpanda`, `owl`, `meme`, `joke`")
        page1.add_field(name = f":gift: Giveaways: [{len(self.gaws_commands)}]", value = "`gstart`, `reroll`")
        page1.add_field(name = f":ticket: Imperial Tickets [3]", value = f"`new`, `close`, `addticketrole`")
        page1.add_field(name = f":question: Misc: [{len(self.misc_commands) - 1}]", value = "`invite`,  `avatar`, `candy`, `suggest`, `support`")
        page1.add_field(name =f"<:settings:761301883792654386> Admin Commands: [{len(self.owner_commands)}]", value = f"`enableautomod`, `disableautomod`, `checkautomod`")
        page1.set_footer(text = f"My prefix is `imp`")
        msg = await ctx.send(embed = page1)

        links = discord.Embed(title = "Help Center", color = ctx.author.color,
        description = """:bell: [Invite](https://discord.com/oauth2/authorize?client_id=768695035092271124&scope=bot&permissions=21474836398)\n
        :radioactive: [Top.gg](https://top.gg/bot/768695035092271124)\n
        :scorpius: [Vote](https://top.gg/bot/768695035092271124/vote)\n
        <:info:761298826907746386> [Support Server](https://discord.gg/KuPzxqHe)\n
        <:VERIFIED_DEVELOPER:761297621502656512> [Web Dashboard](https://theimperialgodwebsite.herokuapp.com)
        """
        )
        links.add_field(name = 'Required Arguments', value = "<> = means a required argument!\n[] = means an optional argument!")
        links.add_field(name = 'Embed Info', value = "This message deletes after 30 seconds due to congestion! So does the other one!")
        links.add_field(name = "Tip :coin::", value =f"**{random.choice(self.tips)}**")
        links.set_footer(text='Bot Made by NightZan999#0194')
        try:
            mesg = await ctx.author.send(embed = links)
        except:
            await ctx.send(f"{ctx.author.mention}, please open direct messages. Since I need to send you a DM!")
            return
        else:
            await asyncio.sleep(30)
            await mesg.delete()

    @help.command(aliases= ["eco"])
    async def economy(self, ctx):
        em = discord.Embed(title = 'Help Economy', color =ctx.author.color)
        em.add_field(name = "Balance", value = "Check the balance of a user!")
        em.add_field(name = "Beg", value = "Beg and make money!")
        em.add_field(name = "Serve", value = "Serve your server and make some coins")
        em.add_field(name = "Withdraw", value = "Withdraw some coins from your bank!")
        em.add_field(name=  "Deposit", value = "Deposit some coins into your bank!")
        em.add_field(name= "Slots", value = "Bet some money and lose or win!")
        em.add_field(name = "Rob", value = "Robs a user!")
        em.set_footer(text='Bot Made by NightZan999#0194')
        msg = await ctx.send(embed = em)
        await msg.add_reaction('💰')

    @help.command(aliases=["mod"])
    async def moderation(self, ctx):
        em = discord.Embed(title = 'Help Moderation', color =ctx.author.color)
        em.add_field(name = "Kick", value = "Kick a user")
        em.add_field(name = "Ban", value = "Ban a user")
        em.add_field(name = "Purge", value = "Delete tons of messages quickly")
        em.add_field(name = "Lock", value = "Lock a channel")
        em.add_field(name=  "Unlock", value = "Unlock a channel")
        em.add_field(name= "Unban", value = "Unban a user")
        em.add_field(name = "Warn", value = "Warn a user")
        em.add_field(name = "Addrole", value = "Give a role")
        em.add_field(name = "Removerole", value = "Remove a role from a user")
        em.add_field(name = "Setdelay", value = "Sets a **custom slowmode in the channel**")
        em.set_footer(text='Bot Made by NightZan999#0194')
        msg  = await ctx.send(embed = em)
        await msg.add_reaction("🗡")

    @help.command(aliases = ["utilties"])
    async def utils(self,ctx):
        em = discord.Embed(title = "Help Utils:", color = ctx.author.color)
        em.add_field(name = "Coinflip", value = "Flips a coin")
        em.add_field(name = "Random Number", value = "Gives a random number in a range")
        em.add_field(name = "Code", value = "Turns a message into code")
        em.add_field(name = "Guess", value = "Selects a random number in a range and plays a guess game!")
        em.add_field(name = "Respect", value = "Shows your respect for anything")
        em.add_field(name = "Poll", value = "Creates a poll")
        em.add_field(name = "Thank", value = "Thanks someone for something")
        em.add_field(name = "Reverse", value = "Reverses a message")
        em.add_field(name = "Eightball", value = "Classic Eightball")
        em.add_field(name = "Fight", value = "Fight someone with lightsabers!")
        em.add_field(name = "Wanted", value = "Can't spoil the fun try it yourself!")
        em.add_field(name=  "Whois", value = "Show information about people")
        em.add_field(name=  "Osay:", value = "Make the bot say something in a channel")
        em.add_field(name = "Treat", value = "Treat someone to a treat!")
        em.set_footer(text='Bot Made by NightZan999#0194')
        msg = await ctx.send(embed = em)
        await msg.add_reaction("🍩")

    @help.command(aliases= ["gstart", "gaws", "gaw", "giveaway"])
    async def giveaways(self, ctx):
        em = discord.Embed(title = "Help Giveaways:", color = ctx.author.color)
        em.add_field(name = "gstart", value = "Starts a giveaway")
        em.add_field(name = "reroll", value = "Rerolls a giveaway")
        em.set_footer(text='Bot Made by NightZan999#0194')
        msg = await ctx.send(embed = em)
        await msg.add_reaction("🎉")

    @help.command(aliases=['miscellaneous'])
    async def misc(self, ctx):
        em = discord.Embed(title = "Help Misc:", color = ctx.author.color)
        em.add_field(name = "invite", value = "Get a link to invite the bot to your s")
        em.add_field(name = "show_toprole", value = "Shows the top role of a person")
        em.add_field(name = "passwordgenerator", value = "DMs you a random password, you can also specify how many letters!")
        em.add_field(name = "botinfo", value = "Shows general information about the Bot!")
        em.add_field(name = "serverinfo", value = "Shows you information about your server!")
        em.add_field(name = "userinfo", value = "Shows you information about a user")
        em.add_field(name = "channelinfo", value = "Shows you information about a channel!")
        em.add_field(name = "avatar", value = "Shows you an avatar of a person")
        em.set_footer(text='Bot Made by NightZan999#0194')
        msg = await ctx.send(embed = em)
        await msg.add_reaction("🐬")

    @help.command()
    async def admin(self, ctx):
        embed = discord.Embed(title = "Help Admin:", color = ctx.author.color)
        embed.add_field(name = "enableautomod", value = "Enables automod for the server, if anyone types a bad word. It deletes")
        embed.add_field(name = "disableautomod", value = "Disable automoderation for the entire server!")
        embed.add_field(name = "checkautomod", value = "Tells you automod status")
        embed.set_footer(text='Bot Made by NightZan999#0194')
        msg = await ctx.send(embed = embed)
        await msg.add_reaction("🐯")

    @help.command(aliases=["ticket"])
    async def tickets(self, ctx):
        em = discord.Embed(title = "Help Tickets", color = ctx.author.color,
        description = """Tickets are the easiest way for members getting their answers via the staff!\n
        A user types `imp new [reason]` and gets a private channel only, the user, the owner and a role can get access to.\n
        Conversations are completely safe and we respect your privacy. To fully setup tickets see the commands!
        """)
        em.add_field(name = "New", value = "Creates a new ticket")
        em.add_field(name = "Close", value = 'Deletes a ticket')
        em.add_field(name = "Addticketrole", value = "Add a role which can access tickets")
        em.set_footer(text='Bot Made by NightZan999#0194')
        await ctx.send(embed  = em)


def setup(client):
    client.remove_command("help")
    client.add_cog(Help(client))
