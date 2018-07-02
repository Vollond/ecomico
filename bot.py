import config
import telebot
import os
import psycopg2
print("123")
DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()
 
# Выполняем запрос.
cursor.execute("SELECT * FROM table_name")
row = cursor.fetchone()
 
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, "1213")
    bot.send_message(message.chat.id, row)


if __name__ == '__main__':
     bot.polling(none_stop=True)
	 
# Закрываем подключение.
cursor.close()
conn.close()