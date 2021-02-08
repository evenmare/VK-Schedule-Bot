import schedule
import requests
import time
import vk_api
import build_data as Info

from build_personal_data import buildClass as build_personal_data
from vk_api.utils import get_random_id
from build_data import scheduleList as scheduleList
from private import token
from private import connectDB as connectDB

vk = vk_api.VkApi(token=token)

def updateConnection(): # обновление подключения к БД
    build_personal_data.dbConnection = connectDB()

def notificationFunc(): # главная функция для оповещений
    timeNow = time.strftime("%X", time.localtime())[:-3]
    if timeNow in Info.Data.Notification.notifications_time_list:
        timeNotificationType, lessonNumber, kind3 = searchingTime(timeNow)                                              # вид оповещений, номер пары, тип третьей пары

        if timeNotificationType != False:

            day_now = time.localtime(time.time()).tm_yday
            type_of_week_now = (day_now - Info.Data.start_day) % 28 // 7
            day_of_week_now = time.localtime(time.time()).tm_wday + 1

            if timeNotificationType != "morning" and timeNotificationType != "evening":
                lessonLocation, lessonID, lessontypeID = searchingLesson(type_of_week_now, day_of_week_now, lessonNumber) # локация проведения занятий, номер названия пары для доступа к словарю, 
                if lessonLocation != None:
                    message = creatingShortMessage(timeNotificationType, type_of_week_now, lessonID, lessontypeID)
                    sendingMessage(timeNotificationType, message, lessonLocation)
            else:
                if timeNotificationType == "evening":
                    day_of_week_now += 1
                message = creatingFullMessage(timeNotificationType, type_of_week_now, day_of_week_now)
                sendingMessage(timeNotificationType, message)

def searchingTime(time_now):
    kind3 = 0
    lesson_number = -1
    if time_now[-1] == "0":
        time_notification_type = "30min"
        for i in range(1, 8):
            if i != 3:
                if Info.Data.Notification.notifications_time[i][0] == time_now:
                   lesson_number = i
            else:
                if Info.Data.Notification.notifications_time[i][0][0] == time_now:
                    lesson_number = 3; kind3 = 0
                elif Info.Data.Notification.notifications_time[i][1][0] == time_now:
                    lesson_number = 3; kind3 = 1
    elif time_now[-1] == "5":
        time_notification_type = "5min"
        for i in range(1, 8):
            if i != 3:
                if Info.Data.Notification.notifications_time[i][1] == time_now:
                   lesson_number = i
            else:
                if Info.Data.Notification.notifications_time[i][0][1] == time_now:
                    lesson_number = 3; kind3 = 1
                elif Info.Data.Notification.notifications_time[i][1][1] == time_now:
                    lesson_number = 3; kind3 = 2
    elif time_now == Info.Data.Notification.notifications_time["evening"]:
        time_notification_type = "evening"
    elif time_now == Info.Data.Notification.notifications_time["morning"]:
        time_notification_type = "morning"
    else:
        time_notification_type = False

    return time_notification_type, lesson_number, kind3

def searchingLesson(type_of_week_now, day_of_week_now, lesson_number):
    if lesson_number in scheduleList[type_of_week_now].connection[day_of_week_now]:
        lessonID = scheduleList[type_of_week_now].connection[day_of_week_now][lesson_number][0]
        lessontypeID = scheduleList[type_of_week_now].connection[day_of_week_now][lesson_number][1]
        if len(scheduleList[type_of_week_now].lessons_location[lessonID]) != 1:
            lessonLocation = scheduleList[type_of_week_now].lessons_location[lessonID][lessontypeID]
        else:
            lessonLocation = scheduleList[type_of_week_now].lessons_location[lessonID][0]

        if lessonLocation.find('.') == -1:
            lessonLocationGen = "local"
        else:
            lessonLocationGen = "distant"
    else:
        lessonLocationGen, lessonID, lessontypeID = None, None, None

    return lessonLocationGen, lessonID, lessontypeID

def creatingShortMessage(time_notification_type, type_of_week, lessonID, lessontypeID):
    message = Info.Data.Notification.time_types_of_notification[time_notification_type] + "\n\n" + scheduleList[type_of_week].get_lesson(lessonID, lessontypeID)
    return message

def creatingFullMessage(time, type_of_week, day_of_week_now):
    message = Info.Data.Notification.time_types_of_notification[time] + scheduleList[type_of_week].get_full_on_a_day(Info.Data.days_of_week[day_of_week_now])
    return message

def sendingMessage(timeTypeNotification, message, locationTypeNotification=None):
    clientByTimeIDs = build_personal_data.selectTimeNotifications(timeTypeNotification)
    if locationTypeNotification != None:
        clientByLocationIDs = build_personal_data.selectLocationNotifications(locationTypeNotification)
    else:
        clientByLocationIDs = clientByTimeIDs

    for ID in clientByTimeIDs:
        if ID in clientByLocationIDs:
            try:
                vk.method('messages.send',
                          {'peer_id': ID,
                           'random_id': get_random_id(),
                           'message': message})
            except Exception:
                True

def startNotificationService():
    for element in Info.Data.Notification.notifications_time_list:
        schedule.every().day.at(element).do(notificationFunc)
    schedule.every().hour.do(updateConnection)

    while True:
        schedule.run_pending()
        time.sleep(5)