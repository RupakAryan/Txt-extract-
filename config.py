#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "27765349"))
    API_HASH = os.environ.get("API_HASH", "9df1f705c8047ac0d723b29069a1332b")
    AUTH_USERS = os.environ.get("AUTH_USERS", "1116405290")
