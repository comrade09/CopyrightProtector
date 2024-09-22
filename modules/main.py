import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import api_id, api_hash, bot_token
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token)


@bot.on_message(filters.command(["start"]))
async def start(bot: Client, m: Message):
    editable = await m.reply_text(f"Hi I am NW Joiner bot just send `/join` Command to access our groups ")


@bot.on_message(filters.command("join") & filters.private)
async def joiner(_, m):
    buttons = [
        [
            InlineKeyboardButton("GROUP A", callback_data= "gc_1"),
            InlineKeyboardButton("GROUP B ", callback_data= "pc_nots"),
        ],
        [
            
            InlineKeyboardButton("BLANK 3 ", callback_data= "org_nots"),
            InlineKeyboardButton("BLANK 4 ", callback_data= "zoo_nots"),
        ],
    ]
 
 
await message.reply_text( text = f'''Notes of Unacademy Plus classes merged  ''',
   reply_markup = InlineKeyboardMarkup(buttons),                       
   disable_web_page_preview = False
   )
 

bot.run()
