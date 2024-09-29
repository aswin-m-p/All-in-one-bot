#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7619482400:AAFGp5-uBHKUAi8Q3XE6JDl40w9HtLdAKL4")
    API_ID = int(os.environ.get("API_ID", "28174664"))
    API_HASH = os.environ.get("API_HASH", "f504bf34ad7dbc597c8802db2f46453c")
    AUTH_USERS = "219249035"

