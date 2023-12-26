import telebot
from config import tbot

bot = telebot.TeleBot(tbot)
#bot = telebot.TeleBot()

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Hello! {message.from_user.first_name}')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, message)

@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.chat.id, 'This is my first bot. It sends information about currency and weather..')

#Bot always running
bot.polling(none_stop=True)
