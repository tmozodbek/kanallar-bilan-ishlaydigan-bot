import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create a bot instance
bot = Bot(token='6299626633:AAEKYLHAIutcOfdDTrsIumET6RmKSpUubTg')

# Create a dispatcher
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)

# Define a command handler
@dispatcher.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    await message.reply("Hello! I'm your Telegram bot.")

# Define a message handler
@dispatcher.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_message(message: types.Message):
    # Do something with the received message
    await message.reply("I received your message!")

@dispatcher.channel_post_handler(content_types=types.ContentTypes.ANY)
async def handle_channel_post(message: types.Message):
    if message.content_type == types.ContentType.TEXT:
        # Handle text message
        await handle_text_message(message)
    elif message.content_type == types.ContentType.PHOTO:
        # Handle photo
        await handle_photo(message)
    elif message.content_type == types.ContentType.AUDIO:
        # Handle audio
        await handle_audio(message)
    elif message.content_type == types.ContentType.DOCUMENT:
        # Handle document
        await handle_document(message)
    elif message.content_type == types.ContentType.VIDEO:
        # Handle video
        await handle_video(message)
    elif message.content_type == types.ContentType.ANIMATION:
        # Handle animation
        await handle_animation(message)
    elif message.content_type == types.ContentType.VOICE:
        # Handle voice
        await handle_voice(message)
    elif message.content_type == types.ContentType.STICKER:
        # Handle sticker
        await handle_sticker(message)
    elif message.content_type == types.ContentType.VIDEO_NOTE:
        await handle_videonote(message)
    else:
        # Handle unsupported content type
        await handle_unsupported_content(message)



# Define a function to handle text messages
async def handle_text_message(message: types.Message):
    # Forward the text message to the bot
    user_ids = ['6030120317']
    for user_id in user_ids:
        await bot.send_message(chat_id=user_id, text=message.text)

# Define a function to handle photos
async def handle_photo(message: types.Message):
    # Forward the photo to the bot
    user_ids = ['6030120317']
    for user_id in user_ids:
        await bot.send_photo(chat_id=user_id, photo=message.photo[-1].file_id, caption=message.caption)

# Define a function to handle audio
async def handle_audio(message: types.Message):
    # Forward the audio to the bot
    user_ids = ['6030120317']
    for user_id in user_ids:
        await bot.send_audio(chat_id=user_id, audio=message.audio.file_id, caption=message.caption)

# Define a function to handle documents
async def handle_document(message: types.Message):
    # Forward the document to the bot
    user_ids = ['6030120317']
    for user_id in user_ids:
        await bot.send_document(chat_id=user_id, document=message.document.file_id, caption=message.caption)

# Define a function to handle videos
async def handle_video(message: types.Message):
    # Forward the video to the bot
    user_ids = ['6030120317']
    for user_id in user_ids:
        await bot.send_video(chat_id=user_id, video=message.video.file_id, caption=message.caption)

# Define a function to handle animations
async def handle_animation(message: types.Message):
    # Forward the animation to the bot
    user_ids = ['6030120317']
    for user_id in user_ids:
        await bot.send_animation(chat_id=user_id, animation=message.animation.file_id, caption=message.caption)

# Define a function to handle voice
async def handle_voice(message: types.Message):
    # Forward the voice to the bot
    user_ids = ['6030120317']
    for user_id in user_ids:
        await bot.send_voice(chat_id=user_id, voice=message.voice.file_id, caption=message.caption)

# Define a function to handle stickers
async def handle_sticker(message: types.Message):
    # Forward the sticker to the bot
    user_ids = ['6030120317']
    for user_id in user_ids:
        await bot.send_sticker(chat_id=user_id, sticker=message.sticker.file_id)

# Define a function to handle videonote
async def handle_videonote(message: types.Message):
    # Forward the videonote to the bot
    user_ids = ['6030120317']
    for user_id in user_ids:
        await bot.send_video_note(chat_id=user_id, video_note=message.video_note.file_id)

#Define a function to handle unsupported content
async def handle_unsupported_content(message: types.Message):
    # Forward the error to the bot
    user_ids = ['6030120317']
    for user_id in user_ids:
        await bot.send_message(chat_id=user_id, text="Unsupported content type")


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
