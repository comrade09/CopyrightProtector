import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from datetime import datetime, timedelta

import core as helper
from utils import progress_bar
from vars import api_id, api_hash, bot_token
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message


bot = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token)


GROUPS = {
    "Group 1": -1002468416084,  # Replace with your actual group IDs
    "Group 2": -1001234567890,  # Replace with your actual group IDs
    "Group 3": -1009876543210   # Replace with your actual group IDs
}

@bot.on_message(filters.command('start') & filters.private)
async def command(bot, message):
    await bot.send_message(message.chat.id, "hi")

@bot.on_message(filters.command('join') & filters.private)
async def join_command(bot, message):
    # Create inline buttons for each group, ensuring callback_data is a string
    buttons = [
        [InlineKeyboardButton(group_name, callback_data=str(group_id))] for group_name, group_id in GROUPS.items()
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        message.chat.id,
        "Choose a group to join:",
        reply_markup=reply_markup
    )

@bot.on_callback_query()
async def handle_callback_query(bot, callback_query: CallbackQuery):
    group_id = int(callback_query.data)  # Convert group_id back to int
    try:
        expiration_time = datetime.now() + timedelta(minutes=15)

        # Generate the join link for the specified group
        link = await bot.create_chat_invite_link(
            group_id,
            expire_date=expiration_time,
            creates_join_request=True
        )

        # Send the link to the user
        await bot.send_message(callback_query.message.chat.id, f"Join link (valid for 3 minutes): {link.invite_link}")

        # Wait for 15 minutes before revoking the link
        await asyncio.sleep(180)  # 15 minutes
        await bot.revoke_chat_invite_link(group_id, link.invite_link)
        await bot.send_message(callback_query.message.chat.id, "The join link has expired.")

    except Exception as e:
        await bot.send_message(callback_query.message.chat.id, f"Sorry, I was unable to generate the join link. Error: {str(e)}")


bot.run()
