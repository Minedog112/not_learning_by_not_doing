# Author: Deltatoolbox aka TornLotus
# Github: https://github.com/Deltatoolbox/not_learning_by_not_doing
#normal imports
from interactions import slash_command, SlashContext
from interactions import OptionType, slash_option
from interactions import Client, Intents, listen
from interactions import ChannelType
import json
import os
#my imports
from modules import basic_functions as functions
#local settings
ctx = SlashContext
#check if the file is in the final folder   
functions.check_location(functions.read_config["location"])
#create a ID on start 
functions.create_or_read_id_file()
print(functions.create_or_read_id_file())
#discord set intents
bot = Client(intents=Intents.DEFAULT)

@listen()
async def on_ready():
    category_name = functions.category_name()

    guild = bot.get_guild(functions.read_config["guild_id"])  
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
        info_channel = await category.create_text_channel("info")
        main_channel = await category.create_text_channel("main")
        spam_channel = await category.create_text_channel("spam")

        # save all channel ids
        functions.save_ids(category.id, info_channel.id, main_channel.id, spam_channel.id)





#start bot
bot.start(functions.read_config["token"])