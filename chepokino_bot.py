import sys
import telebot
from telebot import apihelper
import config
import socks5
from telebot import types
from get_film import get_film_info


bot = telebot.TeleBot(config.TOKEN)
apihelper.proxy = {'https': 'socks5://148.251.234.93:1080'}

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Узнать интересное про фильм') #Имя кнопки
    msg = bot.reply_to(message, "Халлоу!)), {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы создавать посты!".format(message.from_user, bot.get_me()),parse_mode='html')
    bot.register_next_step_handler(msg, get_name_film)
    

@bot.message_handler(commands=['film'])
def get_name_film(message):
    message_film = bot.send_message(message.chat.id, 'Введи название фильма о котором хочешь получить инфу:')
    bot.register_next_step_handler(message_film, create_post, message)
    return message_film

def create_post(message_film, message):
    bot.send_message(message.chat.id, 'Теперь нужно подождать:) Обычно я думаю не больше 2-х минут:)')
    bot.send_message(message.chat.id, 'Загрузка...')
    get_film_info(message_film)
    text_film = open('page_film.html', 'r', encoding='UTF-8')
    line = text_film.readlines()
    name = line[0]
    year = line[1]
    genre_one = line[2]
    genre_two = line[3]
    time = line[4]
    producer = line[5]
    actor_one = line[6]
    actor_two = line[7]
    actor_three = line[8]
    actor_four = line[9]
    actor_five = line[10]
    description = line[11]
    text_film.close()
    bot.send_message(message.chat.id,
    f"""Название:📍 {name}
Жанр: {genre_one},{genre_two}
Год выпуска:📆 {year}
Продолжительность:⏱ {time}
Режиссер:🎥 {producer}
Оценка кинопоиск:🟢 

Оценка IMDb:🟢

В главной роли:
◾{actor_one}
◾{actor_two}
◾{actor_three}
◾{actor_four}
◾{actor_five}
Смотрите Трейлер здесь :)

Описание:📝
{description}
Мнение автора:📝
    
#ЧеПоКино
#Кино
#{name}""")
    bot.send_message(message.chat.id, 'Не благодарите😉')


bot.polling(none_stop = True, interval = 0)
