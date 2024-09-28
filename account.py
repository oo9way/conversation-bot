from telethon import TelegramClient, events

api_id = 8184910
api_hash = "df0a97c7b6d2163610d94c01024e4107"

client = TelegramClient('telethon', api_id, api_hash)


@client.on(events.NewMessage)
async def handle_message(event):
    user_id = event.sender_id
    message_text = event.message.message
    sender = await event.get_sender()
    first_name = sender.first_name if sender.first_name else "Mijoz"

    print(user_id, message_text, sender, first_name)

async def main():
    await client.start()
    await client.run_until_disconnected()


if __name__ == '__main__':
    client.loop.run_until_complete(main())