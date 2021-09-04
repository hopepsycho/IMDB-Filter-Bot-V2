#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from pyrogram.errors import PeerIdInvalid, UserNotParticipant

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    try :
        await bot.get_chat_member(update.from_user.id, Translation.FSUB_CHANNEL)
    except PeerIdInvalid :
        print("Add Me As Admin In Your FSub Channel If It Still Didnt Work Check The ID You Provided")
    except UserNotParticipant :
        Fsub_Channel = await bot.get_chat(Translation.FSUB_CHANNEL)
        invite_link = Fsub_Channel.invite_link
        if file_uid :
            my_bot = await bot.get_me().username
            buttons = [
                InlineKeyboardButton("Channel", url=invite_link),
                InlineKeyboardButton("Retry", url=f"https://t.me/{my_bot}?start={file_uid}")
            ]
        else :
            buttons = [
                InlineKeyboardButton("Channel", url=invite_link),
                InlineKeyboardButton("Support", url="https://t.me/CrazyBotsz")
            ]
        reply_markup = InlineKeyboardMarkup(buttons)

        await bot.send_message(
            text=f"<b>Oh No You Havent Joined My <a href='{invite_link}'>Channel</a> Please Join And Come Back To Use Me .</b>",
            reply_markup=reply_markup,
            parse_mode="html",
            disable_webpage_preview=True
        )
        return
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Developers', url="https://t.me/CrazyBotsz"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('Developers', url='https://t.me/CrazyBotsz'),
        InlineKeyboardButton('Source Code 🧾', url ='https://github.com/MrPurple902/IMDB-Filter-Bot-V2')
    ],[
        InlineKeyboardButton('Support 🛠', url='https://t.me/CrazyBotszGrp')
    ],[
        InlineKeyboardButton('Help ⚙', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
