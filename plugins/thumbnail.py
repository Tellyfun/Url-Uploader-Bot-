# Copyright @Tellybots | @ShriMadhavUk

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import random
import numpy
import os
from PIL import Image
import time

# the Strings used for this "thing"
from plugins.script import Translation
from pyrogram import Client

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyrogram import filters
from functions.help_Nekmo_ffmpeg import take_screen_shot
import psutil
import shutil
import string
import asyncio
from asyncio import TimeoutError
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from functions.forcesub import handle_force_subscribe
from plugins.database.database import db
from plugins.config import Config
from plugins.database.add import add_user_to_database
from plugins.settings.settings import *




