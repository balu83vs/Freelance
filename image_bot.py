import os
import asyncio
import glob
import random
import time
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


# Укажите токен вашего бота
TOKEN = 'YOUR_BOT_TOKEN'
# Укажите ID канала, в который нужно отправлять картинки
CHANNEL_ID = 'YOUR_CHANNEL_ID'
# Укажите путь к директории с картинками
IMAGES_DIRECTORY = 'PATH_TO_IMAGES_DIRECTORY'
# Укажите период (в секундах) между отправкой картинок
PERIOD = 60  # Например, раз в минуту

# Создаем экземпляры бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Функция для отправки картинок в канал
async def send_images_to_channel():
    # Получаем список файлов в директории с картинками
    images = glob.glob(os.path.join(IMAGES_DIRECTORY, '*.jpg')) + glob.glob(os.path.join(IMAGES_DIRECTORY, '*.png'))
    
    # Отправляем каждую картинку в канал
    for image in images:
        with open(image, 'rb') as photo:
            await bot.send_photo(CHANNEL_ID, photo)
            await asyncio.sleep(PERIOD)


# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    await message.reply('Привет! Я бот, который будет отправлять картинки в канал.')


# Функция, которая будет отправлять картинки в канал с указанным периодом
async def scheduled(wait_for):
    while True:
        await send_images_to_channel()
        await asyncio.sleep(wait_for)


# Функция для запуска бота
def run_bot():
    # Запуск диспетчера с заданным интервалом отправки картинок
    dp.loop.create_task(scheduled(PERIOD))
    executor.start_polling(dp, skip_updates=True)


# Запускаем бота
if __name__ == '__main__':
    run_bot()
