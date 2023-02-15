import telebot
from datetime import datetime
import pytz

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start_message(msg):
    text = 'Вітаю! Що Ви хочете дізнатися?'
    bot.send_message(msg.chat.id, text)

@bot.message_handler(commands=['time'])
def time_message(msg):
    text = 'Вкажіть, будь ласка, місто'
    bot.send_message(msg.chat.id, text)


@bot.message_handler(content_types=['text'])
def send_text(msg):
    if msg.text.lower() == 'київ':
        now = datetime.now(pytz.timezone('Europe/Kiev'))
        now = now.strftime("%d/%m/%Y %H:%M:%S")
        bot.send_message(msg.chat.id, now)

    elif msg.text.lower() == 'лондон':
        now = datetime.now(pytz.timezone('Europe/London'))
        now = now.strftime("%d/%m/%Y %H:%M:%S")
        bot.send_message(msg.chat.id, now)

    elif msg.text.lower() == 'фінікс':
        now = datetime.now(pytz.timezone('US/Arizona'))
        now = now.strftime("%d/%m/%Y %H:%M:%S")
        bot.send_message(msg.chat.id, now)

    else:
        text = 'Вибачте, невідоме місто. Спробуйте інше...'
        bot.send_message(msg.chat.id, text)


if __name__ == '__main__':
    print ('Listening ...')
    bot.infinity_polling()

