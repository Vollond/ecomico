import config
import telebot
import os
import psycopg2
from flask import Flask, request
import logging

bot = telebot.TeleBot(config.token)

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()
 
# Выполняем запрос.
cursor.execute("SELECT * FROM users")
row = cursor.fetchone()

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
server = Flask(__name__)
@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://ecomico.herokuapp.com/bot") # этот url нужно заменить на url вашего Хероку приложения
    return "?", 200
server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
 
 
 


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, "1213")
    bot.send_message(message.chat.id, row)
print(row)


# Закрываем подключение.
cursor.close()
conn.close()