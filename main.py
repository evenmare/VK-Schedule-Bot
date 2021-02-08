import vk_api
import time
import random
import requests

from threading import Thread
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType

import vk_keyboards
from private import token as token
from private import admin_id as admin_id
from build_data import scheduleList as scheduleList
from build_data import Data as data
from notifications import startNotificationService

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Клавиатуры
main_keyboard = vk_keyboards.mainKeyboard()
settings_keyboard = vk_keyboards.settingsKeyboard()
schedule_keyboard = vk_keyboards.scheduleKeyboard # это - функция

# Создание сообщения с расписанием на конкретный день (см. кнопки "Сегодня", "Завтра")
def dayFunc(day_of_week_now, type_of_week_now, week_message, event, request, keyboard=main_keyboard):
    day_message = week_message

    if day_of_week_now != 7:

        day_message += scheduleList[type_of_week_now].get_full_on_a_day(data.days_of_week[day_of_week_now])
        vk.method('messages.send', {'peer_id': event.user_id, 'keyboard': keyboard.get_keyboard(),
                                    'random_id': get_random_id(), 'message': request + ":\n" + day_message})

    else:
        day_message += "Воскресение - пар нет"
        vk.method('messages.send',
                  {'peer_id': event.user_id, 'keyboard': keyboard.get_keyboard(),
                   'random_id': get_random_id(),
                   'message': request + ":\n" + day_message})

# Основной цикл
def event_listening():

    # Словарь вида id - short_type_of_week для сохранения данных о выбранной неделе в "Расписание"
    user_selected_week = {}

    try:

        for event in longpoll.listen():

            from notifications import build_personal_data as person

            # Если пришло новое сообщение
            if event.type == VkEventType.MESSAGE_NEW:

                if event.to_me:

                    personID = event.user_id                                                                            # ID пользователя
                    personName = vk.method("users.get", {"user_ids": personID})[0]['first_name']                        # Имя пользователя
                    day_now = time.localtime(time.time()).tm_yday                                                       ## День в году сейчас (используется для определения типа недели)
                    day_of_week_now = time.localtime(time.time()).tm_wday + 1                                           # День недели сейчас
                    type_of_week_now_number = (day_now - data.start_day) % 28 // 7                                      ## Номер типа недели в семестре сейчас (для доступа к словарю)
                    type_of_week_now = data.weeks[type_of_week_now_number]                                              # Название типа недели в семестре
                    short_type_of_week_now = data.short_weeks[type_of_week_now_number]                                  # Короткое название типа недели в семестре
                    number_of_week_now = (day_now - data.start_day) // 7 + 1                                            # Номер недели сейчас
                    week_message = "Неделя " + str(number_of_week_now) + ", " + type_of_week_now + "\n"                 # Стандартный текст для сообщения: Неделя, тип недели

                    if event.user_id in user_selected_week.keys():                                                      # Случай, когда в "Расписание" пользователь выбрал неделю, отличную от настоящей
                        short_type_of_week_now = user_selected_week[event.user_id]
                        type_of_week_now_number = list(data.short_weeks.values()).index(short_type_of_week_now)
                        week_message = data.weeks[type_of_week_now_number] + "\n"

                    request = event.text

                    if request == "Сегодня":
                        dayFunc(day_of_week_now, type_of_week_now_number, week_message, event, request)

                    elif request == "Следующая пара":

                        hrs_now = str(time.strftime("%X", time.localtime())[:2])
                        mins_now = str(time.strftime("%X", time.localtime())[3:5])
                        lessonNumber = 0
                        lessonTime = ""
                        message = ""

                        if day_of_week_now == 7:
                            message += "Воскресение - пар нет"
                            vk.method('messages.send',
                                      {'peer_id': event.user_id, 'keyboard': main_keyboard.get_keyboard(),
                                       'random_id': get_random_id(),
                                       'message': request + ":\n" + message})

                        else:

                            day_schedule = scheduleList[type_of_week_now_number].connection[day_of_week_now]
                            day_lesson_numbers = list(day_schedule.keys())

                            for i in range(len(day_lesson_numbers)):
                                checkingTime = data.lessons_time[day_lesson_numbers[i]]
                                if day_lesson_numbers[i] == 3:
                                    if len(day_schedule[3]) == 3:
                                        checkingTime = checkingTime[day_schedule[3][2] - 1]
                                    else:
                                        checkingTime = checkingTime[0]
                                checkingTime = checkingTime[0]
                                if hrs_now < checkingTime[:2] or (hrs_now == checkingTime[:2] and mins_now < checkingTime[3:5]):
                                    lessonNumber = day_lesson_numbers[i]
                                    lessonTime = checkingTime

                            if lessonNumber == 0:
                                message += "На сегодня пар больше не осталось!"
                                vk.method('messages.send',
                                          {'peer_id': event.user_id, 'keyboard': main_keyboard.get_keyboard(),
                                           'random_id': get_random_id(),
                                           'message': request + ":\n" + message})

                            else:
                                message += scheduleList[type_of_week_now_number].get_lesson(day_schedule[lessonNumber][0], day_schedule[lessonNumber][1], lessonTime)
                                vk.method('messages.send',
                                          {'peer_id': event.user_id, 'keyboard': main_keyboard.get_keyboard(),
                                           'random_id': get_random_id(),
                                           'message': request + ":\n" + message})

                    elif request == "Завтра":
                        if day_of_week_now != 7:
                            dayFunc(day_of_week_now + 1, type_of_week_now_number, week_message, event, request)
                        else:
                            dayFunc(1, type_of_week_now_number + 1, "Неделя " + str(number_of_week_now + 1) + ", " + data.weeks[type_of_week_now_number + 1] + "\n",
                                    event, request)

                    elif request == "Настройки":
                        vk.method('messages.send', {'peer_id': event.user_id, 'keyboard': settings_keyboard.get_keyboard(),
                                                    'random_id': get_random_id(), 'message': 'Что изменим на этот раз?'})

                    elif request == "Уведомления":
                        vk_keyboards.notificationKeyboard(event, personID)

                    elif request == "Подключить":
                        person.insertNewUserInfo(personID, personName)
                        vk.method('messages.send', {'peer_id': event.user_id, 'keyboard': settings_keyboard.get_keyboard(),
                                                    'random_id': get_random_id(), 'message': 'Подключение прошло успешно!'})

                    elif request == "Отключить":
                        person.deleteUserInfo(personID)
                        vk.method('messages.send', {'peer_id': event.user_id, 'keyboard': settings_keyboard.get_keyboard(),
                                                    'random_id': get_random_id(), 'message': 'Отключение прошло успешно!'})

                    elif request in data.notification_kinds:
                        person_info = person.selectUserInfo(personID)
                        if person_info != None  :
                            person_info = list(person_info)
                            person_info[data.notification_kinds[request]] = 1 - person_info[data.notification_kinds[request]]
                            person.updateUserInfo(person_info[0], person_info[2], person_info[3], person_info[4], person_info[5], person_info[6], person_info[7])
                            vk_keyboards.notificationKeyboard(event, personID)
                        else:
                            vk.method('messages.send',
                                      {'peer_id': event.user_id, 'keyboard': settings_keyboard.get_keyboard(),
                                       'random_id': get_random_id(), 'message': 'Для активации команды необходимо подключить уведомления.'})

                    elif request == "Расписание":
                        vk.method('messages.send',
                                  {'peer_id': event.user_id, 'keyboard': schedule_keyboard(short_type_of_week_now).get_keyboard(),
                                   'random_id': get_random_id(),
                                   'message': data.Educate.phrases[random.randint(0, len(data.Educate.phrases) - 1)]})

                    elif request in data.short_weeks.values():
                        user_selected_week[event.user_id] = request
                        vk.method('messages.send',
                                  {'peer_id': event.user_id, 'keyboard': schedule_keyboard(request).get_keyboard(),
                                   'random_id': get_random_id(),
                                   'message': 'Сменим неделю'})

                    elif request in list(data.days_of_week.values()):
                        vk.method('messages.send',
                                  {'peer_id': event.user_id, 'keyboard': schedule_keyboard(short_type_of_week_now).get_keyboard(), 'random_id': get_random_id(),
                                   'message': week_message + scheduleList[type_of_week_now_number].get_full_on_a_day(request)})

                    elif request == "Вся выбранная неделя":
                        week_sch_message = ""
                        for day in data.days_of_week.values():
                            week_sch_message += scheduleList[type_of_week_now_number].get_full_on_a_day(day)
                            if day != data.days_of_week[6]:
                                week_sch_message += "-" * 40 + "\n"
                        vk.method('messages.send',
                                  {'peer_id': event.user_id,
                                   'keyboard': schedule_keyboard(short_type_of_week_now).get_keyboard(),
                                   'random_id': get_random_id(),
                                   'message': week_message + "\n" + week_sch_message})

                    elif request == "Сообщить об ошибке":
                        vk.method('messages.send', {'peer_id': event.user_id, 'keyboard': settings_keyboard.get_keyboard(),
                                                    'random_id': get_random_id(), 'message': 'Для описания ошибки в начале сообщения укажите символы "//" или напишите в ЛС @evenmare.'})

                    elif request == "Главная":
                        vk.method('messages.send',
                                  {'peer_id': event.user_id, 'keyboard': main_keyboard.get_keyboard(),
                                   'random_id': get_random_id(),
                                   'message': data.Educate.phrases[random.randint(0, len(data.Educate.phrases) - 1)]})

                    elif "//" in request:
                        vk.method('messages.send', {'peer_id': admin_id, 'keyboard': settings_keyboard.get_keyboard(),
                                                    'random_id': get_random_id(),
                                                    'message': "СООБЩЕНИЕ ОБ ОШИБКЕ \n @id" + str(event.user_id) + "\n" + request})
                        vk.method('messages.send',
                                  {'peer_id': event.user_id, 'keyboard': settings_keyboard.get_keyboard(),
                                   'random_id': get_random_id(),
                                   'message': "Сообщение отправлено. Спасибо!"})

                    elif "%" in request and event.user_id == admin_id:
                        users = person.selectAllUsers()
                        for user_id in users:
                            vk.method('messages.send',
                                      {'peer_id': user_id, 'keyboard': main_keyboard.get_keyboard(),
                                       'random_id': get_random_id(),
                                       'message': "Сообщение от @evenmare:\n" + request[1:]})

                    else:
                        vk.method('messages.send',
                                  {'peer_id': event.user_id, 'keyboard': main_keyboard.get_keyboard(),
                                   'random_id': get_random_id(),
                                   'message': 'Я бы с радостью ответил Вам на человеческом, ' + personName + ', но, к сожалению, я не понимаю ничего, кроме команд.'})

                    if request not in list(data.days_of_week.values()) and request not in data.short_weeks.values() and event.user_id in user_selected_week.keys():
                        user_selected_week.pop(event.user_id)

    except requests.exceptions.RequestException:
        event_listening()

thread1 = Thread(target=event_listening)
thread2 = Thread(target=startNotificationService)

thread1.start()
thread2.start()

thread1.join()
thread2.join()