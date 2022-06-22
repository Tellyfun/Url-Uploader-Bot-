import shutil
import psutil
from pyrogram import filters
from pyrogram.types import (
    Message
)
from plugins.config import Config
from pyrogram import Client
from plugins.database.database import db
from functions.display_progress import humanbytes
from plugins.database.bcast import broadcast_handler
f = filters.command("status") & filters.user(Config.OWNER_ID)
s = filters.command("broadcast") & filters.user(Config.OWNER_ID) & filters.reply

@app.on_message(f)
async def edited(_, m: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await m.reply_text(
        text=f"**Total Disk Space:** {total} \n"
             f"**Used Space:** {used}({disk_usage}%) \n"
             f"**Free Space:** {free} \n"
             f"**CPU Usage:** {cpu_usage}% \n"
             f"**RAM Usage:** {ram_usage}%\n\n"
             f"**Total Users in DB:** `{total_users}`",
        parse_mode="Markdown",
        quote=True
    )
    print("edited")

@app.on_message(s)
async def edited(_, m: Message):
    await broadcast_handler(m)
    print("edited")





