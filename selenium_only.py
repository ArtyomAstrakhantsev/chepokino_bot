from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



chrome_options = Options()
#chrome_options.add_argument("headless")
chrome_options.add_argument("--window-size=1920,1080")
#chrome_options.add_argument("proxy-server=31.14.131.70:8080")
browser = webdriver.Chrome(executable_path = "chromedriver.exe", options = chrome_options)
browser.implicitly_wait(5)
browser.get('https://www.film.ru/')
search = browser.find_element_by_id('quick_search_input')
search.click()
search.send_keys('50 первых поцелуев' + '\n')
film = browser.find_element_by_xpath('//*[@id="movies_list"]/a[1]')
film.click()
film_name = browser.find_element_by_xpath('//*[@id="block-system-main"]/div/div[1]/div[1]/div[3]/h1')
year_film = browser.find_element_by_xpath('//*[@id="block-system-main"]/div/div[1]/div[1]/div[3]/h3')
filmYear = year_film.text
time_film = browser.find_element_by_xpath('//*[@id="block-system-main"]/div/div[1]/div[1]/div[3]/div[1]/div[1]/strong')
producer_film = browser.find_element_by_xpath('//*[@id="block-system-main"]/div/div[1]/div[1]/div[3]/div[1]/div[2]/strong/a/span')
actor_one = browser.find_element_by_xpath('//*[@id="switch-1"]/a[1]/span[1]')
actor_two = browser.find_element_by_xpath('//*[@id="switch-1"]/a[2]/span[1]')
actor_three = browser.find_element_by_xpath('//*[@id="switch-1"]/a[3]/span[1]')
actor_four = browser.find_element_by_xpath('//*[@id="switch-1"]/a[4]/span[1]')
actor_five = browser.find_element_by_xpath('//*[@id="switch-1"]/a[5]/span[1]')
description_film = browser.find_element_by_xpath('//*[@id="movies-1"]/div/p')

punctuation = ['.',',',':',';','!','?','(',')']
wordList = filmYear.split()
i = 0
for word in wordList:
    if word[-1] in punctuation:
        wordList[i] = word[:-1]
        word = wordList[i]
    if word[0] in punctuation:
        wordList[i] = word[1:]
    i += 1

year = wordList[0]
genre_one = wordList[1]
genre_two = wordList[2]
film_list = [film_name.text, year, genre_one, genre_two, time_film.text, producer_film.text,
actor_one.text, actor_two.text, actor_three.text, actor_four.text, actor_five.text, description_film.text]

film_text = open('page_film.html', 'w', encoding='UTF-8')
for element in film_list:
    print(element, file=film_text)
film_text.close()

browser.close()

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
print(
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