from telethon import TelegramClient, events
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("userbot", api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    print("CHAT ID:", event.chat_id)

client.start()
client.run_until_disconnected()
