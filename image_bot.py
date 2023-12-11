import os
import time
import telebot

# Укажите токен вашего бота
TOKEN = 'YOUR_BOT_TOKEN'
# Укажите ID канала, в который нужно отправлять картинки
CHANNEL_ID = 'YOUR_CHANNEL_ID'
# Укажите путь к директории с картинками
IMAGES_DIRECTORY = 'PATH_TO_IMAGES_DIRECTORY'
# Укажите период (в секундах) между отправкой картинок
PERIOD = 60  # Например, раз в минуту

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Функция для отправки картинок в канал
def send_images_to_channel():
    # Получаем список файлов в директории с картинками
    images = [image for image in os.listdir(IMAGES_DIRECTORY) if os.path.isfile(os.path.join(IMAGES_DIRECTORY, image))]
    
    # Отправляем каждую картинку в канал
    for image in images:
        # Полный путь к файлу
        image_path = os.path.join(IMAGES_DIRECTORY, image)
        
        # Отправляем картинку в канал
        with open(image_path, 'rb') as f:
            bot.send_photo(CHANNEL_ID, f)
        
        # Задержка между отправкой картинок
        time.sleep(PERIOD)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Привет! Я бот, который будет отправлять картинки в канал.')

# Главная функция
def main():
    while True:
        try:
            send_images_to_channel()
        except Exception as e:
            print(f'Произошла ошибка: {e}')
        
        # Задержка перед повторной отправкой картинок
        time.sleep(PERIOD)

# Запускаем бота
if __name__ == '__main__':
    main()