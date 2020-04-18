import sys
import telebot
from telebot import apihelper
import config
import socks5
from get_film import get_film_info
from specifications import create_specification


bot = telebot.TeleBot(config.TOKEN)
apihelper.proxy = {'https': 'socks5://217.182.230.15:4485'}

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Халлоу!)), {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы создавать посты!".format(message.from_user, bot.get_me()),
        parse_mode='html')

@bot.message_handler(commands=['film'])
def get_name_film(message):
    message_film = bot.send_message(message.chat.id, 'Введи название фильма о котором хочешь получить инфу:')
    bot.register_next_step_handler(message_film, create_post, message)
    return message_film

def create_post(message_film, message):
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
    bot.send_message(message.chat.id, f"""Название:📍 {name}
    Год:📆 {year}
    Жанр: {genre_one}, {genre_two}
    Продолжительность:⏱ {time}
    Режиссер:🎥 {producer}
    В главной роли:
    ◼{actor_one}
    ◼{actor_two}
    ◼{actor_three}
    ◼{actor_four}
    ◼{actor_five}
    Описание: 📝
    {description}""")


bot.polling(none_stop = True, interval = 0)
