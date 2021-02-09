class Data:

    class Notification:

        notifications_time = {
            1: ["08:30", "08:55"],
            2: ["10:10", "10:35"],
            3: [["11:50", "12:15"], ["12:20", "12:45"]],
            4: ["14:00", "14:25"],
            5: ["15:40", "16:05"],
            6: ["17:50", "18:15"],
            7: ["19:30", "19:55"],
            "morning": "08:01",
            "evening": "20:01"
        }

        notifications_time_list = ["08:01", "08:30", "08:55", "10:10", "10:35", "11:50", "12:15", "12:20", "12:45", "14:00",
                                   "14:25", "15:40", "16:05", "17:50", "18:15", "19:30", "19:55", "20:01"]

        time_types_of_notification = {
            "5min": "ЧЕРЕЗ 5 МИНУТ ПАРА!",
            "30min": "ЧЕРЕЗ 30 МИНУТ ПАРА!",
            "evening": "ЗАВТРА: ",
            "morning": "СЕГОДНЯ: "
        }

        location_types_of_notifications = {
            1: "local",
            2: "distant"
        }

    class Educate:
        phrases = [
            "Каждый из нас гений. Но если судить рыбу по ее умению лазить по деревьям, она проживет всю жизнь, считая себя глупой.\n(c) Альберт Эйнштейн",
            "Перед тем, как диагностировать у себя депрессию или заниженную самооценку, убедитесь, что не находитесь в окружении дураков.\n(c) Зигмунд Фрейд",
            "Занимаясь поисками счастья для других, вы найдете его в себе.\n(c) Неизвестный автор",
            "Любовь — это глагол. Любовь — это чувство, которое является плодом любви.\n(c) Стивен Кови",
            "У человека можно забрать все, кроме одного: человеческой свободы — способности выбирать свое отношение к сложившейся ситуации и выбора собственного пути.\n(c) Виктор Франкл",
            "Успех — это способность терпеть неудачу снова и снова без потери энтузиазма.\n(c) Уинстон Черчиль",
            "Вы должны изменить себя, если хотите увидеть изменение в мире.\n(c) Ганди",
            "Трудности — это то, что делает жизнь интересной и осмысленной, придавая ей значимость.\n(c) Джошуа Дж Марин",
            "Если вы хотите часик побыть счастливым — вздремните. Если хотите счастья на день — сходите на рыбалку. Если вы хотите быть счастливым в течении года — унаследуйте состояние. Если хотите сделать всю жизнь счастливой — помогите кому-нибудь еще.\n(c) Китайская пословица",
            "Обстоятельства никогда не сделают жизнь невыносимой, но это могут сделать отсутствие цели и смысла.\n(c) Виктор Франкл",
            "Ум, который расширяется новым опытом, никогда не сможет вернуться к своим старым размерам.\n(c) Оливер Уэнделл Холмс",
            "Жизнь очень проста, но мы настаиваем на том, что она сложная.\n(c) Конфуций",
            "Люди очень увлеченные существа, но из-за их ограниченных убеждений, о том,кто они и что могут сделать, они не предпринимают действий, которые могут воплотить их мечты в реальность.\n(c) Энтони Робинс",
            "Истинный успех — это преодоление страха неудачи.\n(c) Пол Суини",
            "Единственный способ, позволяющий нам жить — это рост. Единственный способ расти — когда мы меняемся. Единственный способ измениться — узнавать. Единственный способ узнавать — быть открытым. И единственный способ быть открытым — это пройти сквозь себя и открыться.\n(c) Джойбел",
            "Если вам что-то не нравится — измените это. Если не можете изменить, измените свои мысли об этом.\n(c) Мэри Энгельбрайт",
            "Жизнь, потраченная на совершение ошибок, не только достойна чести, но и намного полезнее той жизни, когда ничего не делаешь.\n(c) Джордж Бернард Шоу",
            "Я предпочту умереть смертью, наполненной смысла, чем прожить жизнь, лишенную всякого смысла.\n(c) Корасон Акино",
            "Время идет слишком медленно для тех, кто чего-то ждет, слишком быстро для тех, кто боится, слишком долго для тех, кто скорбит, оно слишком короткое для тех, кто радуется и вечное для тех, кто любит.\n(c) Генри Ван Дайк",
            "Господи, дай мне сил принять то, что я не могу изменить, мужества изменить то, что могу и мудрости, чтобы отличить одно от другого.\n(c) Рейнхольд Нибур",
            "Большинство людей не слушает, чтобы понять, они слушают, чтобы ответить.\n(c) Стивен Кови",
            "Мы считаем, что бедность это отсутствие одежды, дома и еды. Однако, когда тебя не любят, ты заброшен и никому ненужен — это величайшая бедность. Мы должны начать с собственного дома, чтобы исправить последний вид бедности.\n(c) Мать Тереза",
            "Вчера — это история, завтра — это загадка, сегодня — это подарок.\n(c) Бил Кин",
            "Влюбленность — это не выбор. Сохранить любовь — да.\n(c) Неизвестный автор",
            "Самые красивые люди, которых мы знаем это те, кто потерпели поражение, прошли через страдания, боролись, потеряли и в итоге нашли свой путь. Они этого не скрывают, об этом известно всем. Эти люди высоко ценятся, чувствительны и понимают жизнь, которая наполняет их состраданием, мягкостью и глубоко любящим беспокойством. Красивыми людьми не рождаются.\n(c) Элизабет Кюблер-Росс",
            "Мир, каким мы его создали — это процесс нашего мышления. Его нельзя изменить без изменения нашего мышления.\n(c) Альберт Эйнштейн",
            "Счастье подобно бабочке. Чем дольше мы его преследуем, тем больше оно ускользает от нас. Но, если переключить взгляд на другие вещи, то оно придет и сядет к вам на плечо.\n(c) Генри Дэвид Торо",
            "Когда одна дверь счастья закрывается, открывается другая, но мы часто смотрим так долго на закрытую дверь, что не замечаем ту, которая открылась.\n(c) Хелен Келлер",
            "Тот, кто боится, что он будет страдать, уже страдает, потому что он боится.\n(c) Мишель де Мюнтень"
        ]

    start_day = 39

    short_weeks = {
        0: "Ч1",
        1: "З1",
        2: "Ч2",
        3: "З2"
    }

    weeks = {
        0: "Числитель 1",
        1: "Знаменатель 1",
        2: "Числитель 2",
        3: "Знаменатель 2"
    }

    days_of_week = {
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота"
    }

    lessons_type = {
        1: "Лекция",
        2: "Семинар",
        3: "Лабораторная"
    }

    lessons_time = {
        1: ["09:00", "10:30"],
        2: ["10:40", "12:10"],
        3: [["12:20", "13:50"], ["12:50", "14:20"]],
        4: ["14:30", "16:00"],
        5: ["16:10", "17:40"],
        6: ["18:20", "19:50"],
        7: ["20:00", "21:30"]
    }

    lessons = {
        1: "lessonName",
        2: "lessonName",
        3: "lessonName",
        4: "lessonName",
        5: "lessonName",
        6: "lessonName",
        7: "lessonName",
        8: "lessonName",
        9: "lessonName",
        10: "lessonName",
        11: "lessonName",
        12: "lessonName",
        13: "lessonName"
    }

    teachers = {
        1: [["Name", "e@mail.com"],
            ["Name", "e@mail.com"],
            ["Name", "e@mail.com"]],
        2: [["Name", "e@mail.com"]],
        3: [["Name", "e@mail.com"]],
        4: [["Name", "e@mail.com"]],
        5: [["Name", "e@mail.com"]],
        6: [["Name", "e@mail.com"],
            ["Name", "e@mail.com"],
            ["Name", "e@mail.com"]],
        7: [["Name", "e@mail.com"]],
        8: [["Name", "e@mail.com"]],
        9: [["Name", "e@mail.com"]],
        10: [["Name", "e@mail.com"]],
        11: [["Name", "e@mail.com"]],
        12: [["Name", "e@mail.com"]],
        13: [["Name", "e@mail.com"]]
    }

    notification_kinds = {
        "Вечерние": 2,
        "Утренние": 3,
        "За 30 минут": 4,
        "За 5 минут": 5,
        "Очные": 6,
        "Дистанционные": 7
    }

class Schedule:

    # lessons: [lecture, seminar, lab] OR lessons: [link]
    lessons_location = {}
    # day_of_week: lesson_time: [lesson, lesson_type, #3rd toggle]
    connection = {}

    def get_day(self, day_of_week):
        return Data.days_of_week[day_of_week]

    def get_day_number(self, day_of_week):
        return list(Data.days_of_week.values()).index(day_of_week) + 1

    def get_time(self, lesson_time, number=0):
        if lesson_time == 3:
            if number == 0:
                return "(" + list(Data.lessons_time.values())[lesson_time - 1][0][0] + " - " + list(Data.lessons_time.values())[lesson_time - 1][0][1] + ")"
            else:
                return "(" + list(Data.lessons_time.values())[lesson_time - 1][number - 1][0] + " - " + list(Data.lessons_time.values())[lesson_time - 1][number - 1][1] + ")"
        else:
            return "(" + list(Data.lessons_time.values())[lesson_time - 1][0] + " - " + list(Data.lessons_time.values())[lesson_time - 1][1] + ")"

    def get_teacher(self, lesson, lesson_type):
        if len(Data.teachers[lesson]) == 1:
            lesson_type = 0
        return Data.teachers[lesson][lesson_type][0] + " (" + Data.teachers[lesson][lesson_type][1] + ")"

    def get_lesson(self, lesson, lesson_type, time=""):
        if len(self.lessons_location[lesson]) == 1:
            return Data.lessons[lesson] + "\n" + Data.lessons_type[lesson_type] + " " + time + "\n" + self.lessons_location[lesson][0] + "\n" + self.get_teacher(lesson, lesson_type - 1) + "\n"
        else:
            return Data.lessons[lesson] + "\n" + Data.lessons_type[lesson_type] + " " + time + "\n" + self.lessons_location[lesson][lesson_type - 1] + self.get_teacher(lesson, lesson_type - 1) + "\n"

    def get_full_on_a_day(self, day):
        text = day + "\n\n"
        data = self.connection[self.get_day_number(day)]
        for key in data:
            if key != 3:
                text += str(key) + ". " + self.get_lesson(data[key][0], data[key][1], self.get_time(key)) + "\n"
            else:
                try:
                    kind = data[key][2]
                except Exception:
                    kind = 0
                text += str(key) + ". " + self.get_lesson(data[key][0], data[key][1], self.get_time(key, kind)) + "\n"
        return text

scheduleList = [Schedule(), Schedule(), Schedule(), Schedule()]

def load():

    with open('/usr/local/bin/vkBot/locations.json', 'r', encoding='UTF8') as file:
        locations = json.load(file)
        for i in range(4):
            scheduleList[i].lessons_location = locations[i]
            scheduleList[i].lessons_location = {int(k): v for k, v in scheduleList[i].lessons_location.items()}

    with open('/usr/local/bin/vkBot/schedules.json', 'r', encoding='UTF8') as file:
        connections = json.load(file)
        for i in range(4):
            scheduleList[i].connection = connections[i]
            for key in scheduleList[i].connection.keys():
                scheduleList[i].connection[key] = {int(k): v for k, v in scheduleList[i].connection[key].items()}
            scheduleList[i].connection = {int(k): v for k, v in scheduleList[i].connection.items()}

def update_jsons():

    locations_list = []
    connections_list = []

    for i in range(4):
        locations_list.append(scheduleList[i].lessons_location)
        connections_list.append(scheduleList[i].connection)

    with open('/usr/local/bin/vkBot/locations.json', 'w', encoding='UTF8') as file:
        json.dump(locations_list, file, ensure_ascii=False)

    with open('/usr/local/bin/vkBot/schedules.json', 'w', encoding='UTF8') as file:
        json.dump(connections_list, file, ensure_ascii=False)