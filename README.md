# VK-Schedule-Bot
 
в процессе написания исчерпывающего гайда

## requirements

### python
3.8+

### vkapi
longapi, 5.120+

### db
- Database *name_your_db*: 
- Table *you_can_name_it, build_personal_data.py*: 
- Columns perID [INT], perName [STRING], 30minNotifications [TINYINT 1], 5minNotifications [TINYINT 1], eveningNotifications [TINYINT 1], morningNotifications [TINYINT 1],    localLessons [TINYINT 1], distantLessons [TINYINT 1]

### jsons
1. locations.json (информация о месте проведения): 
   - [ {lesson_id *(similar to build_data/Data/lessons dict)*: [lecture location, seminar location, lab location]} **x4** ]
2. connection.json (само расписание):
   - [ {day_number: {lesson_number: [lesson_id, lesson_type_id *(similar to build_data/Data/lessons_type dict)* **x4** ]

## управление ботом через сообщения

### управление расписанием
- ` * [тип недели] `
- ` ** [номер дня] `: 1-6 (для удаления расписания на день добавить " /")
- ` *** [номер пары] [номер дисциплины] [номер типа пары: 1 - лекция, 2 - семинар, 3 - лаба] [аудитория/ссылка] `
(для удаления пары из расписания на день использовать `*** [номер пары] /`)
- `^` - обновить кэшируемое расписание
- `^u` - обновить расписание в файле
- `^d` (при удалении пары из дневного расписания) - удалить из кэшируемого расписания (для обновления в файле после этого ^u)
- `^z` - откат расписания к расписанию из файла

### управление уведомлениями
- ` /on` - включить уведомления для всех (по умолчанию включено)
- ` /off` - выключить уведомления для всех

### управление обратной связью
- ` // [баг-репорт]` - для пользователя, админу придет сообщение в лс от бота
- ` % [текст]` - уведомление для всех подписанных на уведомления
