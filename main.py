import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session = os.environ["SESSION_STRING"]

ORIGEN_GRUPO = int(os.environ["ORIGEN_GRUPO"])
USUARIO_OBJETIVO = int(os.environ["USUARIO_OBJETIVO"])
DESTINO_PERSONA = int(os.environ["DESTINO_PERSONA"])

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(chats=ORIGEN_GRUPO))
async def handler(event):
    if event.sender_id != USUARIO_OBJETIVO:
        return

    await client.forward_messages(
        entity=DESTINO_PERSONA,
        messages=event.message
    )

async def main():
    await client.start()
    print("✅ Userbot activo 24/7 en Render")
    await client.run_until_disconnected()

client.loop.run_until_complete(main())
