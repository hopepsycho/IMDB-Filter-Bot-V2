#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @hopepsycho
import os

class Translation(object):
    
    START_TEXT = """<b>Hey {}!!</b>
<i>Am Just A Advance Auto Filter Bot....😉

Join My Group And REquest A Movie To See My Pevers 🔥🔥😝

For More Details Click Help Button Below..
@kunjppansupportez
</i>"""    
    
    HELP_TEXT = """
<b><i><u>How To Use Me!?</u></i></b>

<i>
-> Join My Group 
-> Ask for Your Movie
</i>

<b>Bot Commands (Strictly Admins Only And Designed To work In a Specific Group) :</b>

    -> <code>/add chat_id</code>
                OR                  - To Connect A Group With A Channel (Bot Should Be Admin With Full Previlages In Both Group And Channel)
     <code>/add @Username</code>
     
    -> <code>/del chat_id</code>
                OR                  - To disconnect A Group With A Channel
     <code>/del @Username</code>
     
    -> <code>/delall</code>  - This Command Will Disconnect All Connected Channel With The Group And Deletes All Its File From DB
    
    -> <code>/settings</code> -  This Command Will Display You A Settings Pannel Instance Which Can Be Used To Tweek Bot's Settings Accordingly

            -> <code>Channel</code> - Button Will Show You All The Connected Chats With The Group And Will Show Buttons Correspnding To There Order For Furthur Controls
            
            -> <code>Filter Types</code> - Button Will Show You The 3 Filter Option Available In Bot... Pressing Each Buttons Will Either Enable or Disable Them And This Will Take Into Action As Soon As You Use Them Without The Need Of A Restart

            -> <code>Configure</code> - Button Will Helps You To Change No. of Pages/ Buttons Per Page/ Total Result Without Acutally Editing The Repo... Also It Provide Option To Enable/Disable For Showing Invite Link In Each Results
            
            -> <code>Status</code> - Button Will Shows The Stats Of Your Channel
            
@kunjappansupportez
"""
    
    ABOUT_TEXT = """<b>➥ Name</b> : <code> Auto Filter Bot</code>
    
<b>➥ Creator</b> : <b><i><a href="https://t.me/king_of_psycho">PSYCHO</a></i></b>

<b>➥ ReCreator</b> : <b><i><a href="tg://user?id=1316481146">hopepsycho</a></i></b>

<b>➥ Language</b> : <code>Python3</code>

<b>➥ Library</b> : <i><a href="https://docs.pyrogram.org">Pyrogram Asyncio 1.13.0 </a></i>

<b>➥ Source Code</b> : <i><a href="https://github.com/hopepsycho/professor_v2">Click Me</a></i>
"""

    SIZE_BUTTON = bool(os.environ.get("SIZE_BUTTON"))
    BACKUP_IMAGE = os.environ.get("DEFAULT_IMAGE")
    FSUB_CHANNEL = os.environ.get("FSUB_CHANNEL")
    FSUB_LINK = os.environ.get("FSUB_CHANNEL_LINK")
