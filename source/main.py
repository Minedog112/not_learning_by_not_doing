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
    id = functions.create_or_read_id_file()
    username = os.getlogin()
    category_name = f"{id}-{username}"

    guild = bot.get_guild(settings.guild_id())  
    channels = await guild.fetch_channels()
    existing_categories = [channel for channel in channels if channel.type == ChannelType.GUILD_CATEGORY]

    if category_name not in [category.name for category in existing_categories]:
        await guild.create_category(category_name)
        print(f"Kategorie {category_name} erstellt.")
    else:
        print(f"Kategorie {category_name} existiert bereits.")


#example command
@slash_command(name="my_command", description="My first command :)")
@slash_option(
    name="integer_option",
    description="Integer Option",
    required=True,
    opt_type=OptionType.INTEGER
)
async def my_command_function( integer_option: int):
    await ctx.send(f"You input {integer_option}")


#start bot
bot.start(settings.token())