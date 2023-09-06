import telebot

TOKEN = "6022335594:AAHWg1RS36yJuLOJa4oiLcEd7vM4aWio3xg"
bot = telebot.TeleBot(TOKEN)

#Приветственное сообщение
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    bot.reply_to(message, f"Привет, {message.chat.username}")


#Ответ на сообщение с фотографией с привязкой к картинке
@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

#Ответ на голосовое сообщение
@bot.message_handler(content_types=['voice', ])
def say_voice_beauty(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'У тебя красивый голос')

bot.polling(none_stop=True)