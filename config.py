#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8464714544:AAGNMuJw6wnSsJ1HBchtZBjJednvvY8v9a8")
    API_ID = int(os.environ.get("API_ID", "29978901"))
    API_HASH = os.environ.get("API_HASH", "500fc876c5356cf04ed3698912dc2edf")
    AUTH_USERS = os.environ.get("AUTH_USERS", "5776977809")
