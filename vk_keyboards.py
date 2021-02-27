from build_data import Data
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from notifications import build_personal_data as person

from vk_connection import vk as vk

def mainKeyboard():
    main_keyboard = VkKeyboard(one_time=True)

    main_keyboard.add_button('Сегодня')
    main_keyboard.add_button('Следующая пара')
    main_keyboard.add_line()

    main_keyboard.add_button('Завтра')
    main_keyboard.add_openlink_button('Новости', 'https://vk.com/pressyourgrouphere')
    main_keyboard.add_line()

    main_keyboard.add_button('Расписание')
    main_keyboard.add_line()

    main_keyboard.add_button('Настройки', color=VkKeyboardColor.PRIMARY)

    return main_keyboard

def scheduleKeyboard(short_selected_week):
    schedule_keyboard = VkKeyboard(one_time=True)

    for element in Data.short_weeks.values():
        if element != short_selected_week:
            schedule_keyboard.add_button(element)
        else:
            schedule_keyboard.add_button(element, color=VkKeyboardColor.POSITIVE)

    schedule_keyboard.add_line()

    schedule_keyboard.add_button('Понедельник')
    schedule_keyboard.add_button('Четверг')
    schedule_keyboard.add_line()

    schedule_keyboard.add_button('Вторник')
    schedule_keyboard.add_button('Пятница')
    schedule_keyboard.add_line()

    schedule_keyboard.add_button('Среда')
    schedule_keyboard.add_button('Суббота')
    schedule_keyboard.add_line()

    schedule_keyboard.add_button('Вся выбранная неделя')
    schedule_keyboard.add_line()


    schedule_keyboard.add_button('Главная', color=VkKeyboardColor.PRIMARY)

    return schedule_keyboard

def settingsKeyboard():
    settings_keyboard = VkKeyboard(one_time=True)

    settings_keyboard.add_button('Уведомления')
    settings_keyboard.add_line()

    settings_keyboard.add_openlink_button('GitHub', 'https://github.com/evenmare/VK-Schedule-Bot')
    settings_keyboard.add_button('Сообщить об ошибке', color=VkKeyboardColor.NEGATIVE)
    settings_keyboard.add_line()

    settings_keyboard.add_button('Главная', color=VkKeyboardColor.PRIMARY)

    return settings_keyboard

def notificationKeyboard(event, personID):
    notification_keyboard = VkKeyboard(one_time=True)
    dbRequestCallback = person.selectUserInfo(personID)

    if dbRequestCallback == None:
        notification_keyboard.add_button('Подключить')
        notification_keyboard.add_line()
        notification_keyboard.add_button('Настройки', color=VkKeyboardColor.PRIMARY)
        vk.method('messages.send',
                  {'peer_id': event.user_id, 'keyboard': notification_keyboard.get_keyboard(),
                   'random_id': get_random_id(),
                   'message': 'Для первичной настройки уведомлений необходимо провести подключение функции.'})

    else:

        if dbRequestCallback[2] == 0:
            notification_keyboard.add_button("Вечерние")
        else:
            notification_keyboard.add_button("Вечерние", color=VkKeyboardColor.POSITIVE)

        if dbRequestCallback[3] == 0:
            notification_keyboard.add_button("Утренние")
        else:
            notification_keyboard.add_button("Утренние", color=VkKeyboardColor.POSITIVE)

        notification_keyboard.add_line()

        if dbRequestCallback[4] == 0:
            notification_keyboard.add_button("За 30 минут")
        else:
            notification_keyboard.add_button("За 30 минут", color=VkKeyboardColor.POSITIVE)

        if dbRequestCallback[5] == 0:
            notification_keyboard.add_button("За 5 минут")
        else:
            notification_keyboard.add_button("За 5 минут", color=VkKeyboardColor.POSITIVE)

        notification_keyboard.add_line()

        if dbRequestCallback[6] == 0:
            notification_keyboard.add_button("Очные")
        else:
            notification_keyboard.add_button("Очные", color=VkKeyboardColor.POSITIVE)

        if dbRequestCallback[7] == 0:
            notification_keyboard.add_button("Дистанционные")
        else:
            notification_keyboard.add_button("Дистанционные", color=VkKeyboardColor.POSITIVE)

        notification_keyboard.add_line()

        notification_keyboard.add_button("Отключить", color=VkKeyboardColor.NEGATIVE)
        notification_keyboard.add_line()

        notification_keyboard.add_button('Настройки', color=VkKeyboardColor.PRIMARY)

        vk.method('messages.send',
                  {'peer_id': event.user_id, 'keyboard': notification_keyboard.get_keyboard(),
                   'random_id': get_random_id(),
                   'message': 'Настройки загружены. Для изменения нажмите на соответствующую кнопку.'})