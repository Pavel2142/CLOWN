from telethon import TelegramClient, events
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionEmoji

# Укажите ваш API ID и API Hash
api_id = '22101462'
api_hash = 'cc6369b9c1916ebaaeb7ab76b0a76ce5'

# Устанавливаем имя сессии как 'CLOWN'
client = TelegramClient('CLOWN', api_id, api_hash)

# Функция для добавления реакции "клоун"
async def add_reaction(message):
    try:
        # Создаем объект реакции с эмодзи "клоун"
        reaction = ReactionEmoji(emoticon='🤡')
        # Отправляем реакцию с помощью метода SendReactionRequest
        await client(SendReactionRequest(
            peer=message.peer_id,
            msg_id=message.id,
            reaction=[reaction]
        ))
        print(f"Реакция 'клоун' установлена на сообщение: {message.text}")
    except Exception as e:
        print(f"Ошибка при добавлении реакции к сообщению: {e}")

# Устанавливаем слушатель для новых сообщений
@client.on(events.NewMessage)
async def handler(event):
    # Добавляем реакцию "клоун" на новое сообщение
    await add_reaction(event.message)

# Запускаем клиента
client.start()
print("Бот запущен и ставит реакцию 'клоун' на новые сообщения...")

client.run_until_disconnected()
