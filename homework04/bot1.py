import requests
import config
import telebot
from bs4 import BeautifulSoup
import datetime
import io
import sys


bot = telebot.TeleBot(config.access_token)


days = {
    'monday': 1,
    'tuesday': 2,
    'wednesday': 3,
    'thursday': 4,
    'friday': 5,
    'saturday': 6,
    'sunday': 7
}

def get_page(group, week=''):
    with io.open('shedule.html', encoding='utf-8') as f:
        f_contents = f.read()
        return(f_contents)
    if week:
        week = str(week) + '/'
    url = '{domain}/{group}/{week}raspisanie_zanyatiy_{group}.htm'.format(
        domain=config.domain,
        week=week,
        group=group)
    response = requests.get(url)
    web_page = response.text
    return web_page


def parse_schedule_for_a_day(web_page, day):
    soup = BeautifulSoup(web_page, "html5lib")

    # Получаем таблицу с расписанием
    schedule_table = soup.find("table", attrs={"id": str(day)+"day"})
    if not schedule_table:
        return ['Никогда'], ['Нигде'], ['Ничего']
    # Время проведения занятий
    times_list = schedule_table.find_all("td", attrs={"class": "time"})
    times_list = [time.span.text for time in times_list]

    # Место проведения занятий
    locations_list = schedule_table.find_all("td", attrs={"class": "room"})
    locations_list = [room.span.text for room in locations_list]

    # Название дисциплин и имена преподавателей
    lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
    lessons_list = [lesson.text.split('\n\n') for lesson in lessons_list]
    lessons_list = [', '.join([info for info in lesson_info if info]) for lesson_info in lessons_list]

    return times_list, locations_list, lessons_list

def get_schedule_data_for_a_day(day,group):
    web_page = get_page(group)
    times_lst, locations_lst, lessons_lst = \
        parse_schedule_for_a_day(web_page, day)
    return  zip(times_lst, locations_lst, lessons_lst) 

def base_get_schedule(day, group):
    
    data = get_schedule_data_for_a_day(day, group)
    resp = ''
    for time, location, lession in data:
        resp += '<b>{}</b>, {}, {}\n'.format(time, location, lession)
    return resp






@bot.message_handler(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
def get_schedule(message):
    """ Получить расписание на указанный день """
    command, group = message.text.split()
    resp = base_get_schedule(days[command[1:]], group)   
    bot.send_message(message.chat.id, resp, parse_mode='HTML')
    


@bot.message_handler(commands=['near'])
def get_near_lesson(message):
    """ Получить ближайшее занятие """
    # PUT YOUR CODE HERE
    command, group = message.text.split()
    today = datetime.datetime.now().isoweekday()
    time_now = datetime.datetime.now()
    resp = ''
    x = 0
    while resp == '':  
        data = get_schedule_data_for_a_day(today + x, group)
        x = x + 1
        for time, location, lession in data:
            if time=='Никогда':
                continue
            hour, minutes = time.split('-')[0].split(':')
            if x > 1 or (int(hour) >= time_now.hour or (int(hour) == time_now.hour and int(minutes) >= time_now.minute)):
                resp = '<b>{}</b>, {}, {}\n'.format(time, location, lession)
                break
    
    bot.send_message(message.chat.id, resp, parse_mode='HTML')
        



@bot.message_handler(commands=['tommorow'])
def get_tommorow(message):
    """ Получить расписание на следующий день """
    # PUT YOUR CODE HERE
    today = datetime.datetime.now().isoweekday()
    next_day = (today+1) % 7
    command, group = message.text.split()
    resp = base_get_schedule(next_day, group)   
    bot.send_message(message.chat.id, resp, parse_mode='HTML')




@bot.message_handler(commands=['all'])
def get_all_schedule(message):
    """ Получить расписание на всю неделю для указанной группы """
    command, group = message.text.split()
    for i in range(1,7):
        resp = base_get_schedule(i, group)   
        bot.send_message(message.chat.id, resp, parse_mode='HTML')


if __name__ == '__main__':
    bot.polling(none_stop=True)
