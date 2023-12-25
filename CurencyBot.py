import telebot
import config

bot = telebot.TeleBot('5875528627:AAGUyFJl3IyGPHn5V9RcOz_OcquJRl2OFA0')
#bot = telebot.TeleBot()

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Hello!')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Help information')

@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.chat.id, 'This is my first bot. It sends information about currency and weather..')

#Bot always running
bot.polling(none_stop=True)
