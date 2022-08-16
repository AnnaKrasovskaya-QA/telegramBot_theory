# В google colab добавить: !pip install pyTelegramBotAPI


from telebot import TeleBot, types

bot = TeleBot(token='5414002769:AAFBbdkZaFWbrql2ssLk-WzS8-Nf3RfZf2U', parse_mode='html') # создание бота


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать тест❓")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот в котором ты можешь проверить свои знания по теории тестирования".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Начать тест❓"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Quality assurance")
        btn2 = types.KeyboardButton("Quick answer")
        btn3 = types.KeyboardButton("Вопрос№2")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Что такое QA?", reply_markup=markup)
    
    elif(message.text == "Quality assurance"):
        bot.send_message(message.chat.id, text="Верно! Молодец!✅")
        bot.send_message(message.chat.id, text="<b>Quality assurance</b> - обеспечение качества")
    
    elif message.text == "Quick answer":
        bot.send_message(message.chat.id, text="Неправильно!❌ <b>Верный ответ: Quality assurance - обеспечение качества</b>")
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Начать тест❓")
        markup.add(button1)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif (message.text == "Вопрос№2"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton("S5 – Trivial")
        btn5 = types.KeyboardButton("S4 – Minor")
        btn6 = types.KeyboardButton("Вопрос№3")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text="Опечатки в тексте, несоответствие шрифта и оттенка", reply_markup=markup)

    elif(message.text == "S5 – Trivial"):
        bot.send_message(message.chat.id, "Верно! Молодец!✅")
        bot.send_message(message.chat.id, "<b>Тривиальный (S5 – Trivial)</b> Почти всегда дефекты на GUI — опечатки в тексте, несоответствие шрифта и оттенка и т.п., либо плохо воспроизводимая ошибка, не касающаяся бизнес-логики, проблема сторонних библиотек или сервисов, проблема, не оказывающая никакого влияния на общее качество продукта.")
    elif message.text == "S4 – Minor":
        bot.send_message(message.chat.id, text="Неправильно!❌ <b>Верный ответ: Тривиальный (S5 – Trivial)</b>")
        bot.send_message(message.chat.id, text="<b>Незначительный (S4 – Minor)</b> Часто ошибки GUI, которые не влияют на функциональность, но портят юзабилити или внешний вид. Также незначительные функциональные дефекты, либо которые воспроизводятся на определенном устройстве.")
    
    elif (message.text == "Вопрос№3"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton("Верификация")
        btn5 = types.KeyboardButton("Валидация")
        btn6 = types.KeyboardButton("Вопрос№4")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text="Как называется процесс оценки системы, чтобы понять, удовлетворяют ли результаты текущего этапа разработки условиям, которые были сформулированы в его начале?", reply_markup=markup)

    elif(message.text == "Верификация"):
        bot.send_message(message.chat.id, "Верно! Молодец!✅")
    
    elif message.text == "Валидация":
        bot.send_message(message.chat.id, text="Неправильно!❌ <b>Верный ответ: Верификация</b>")
        bot.send_message(message.chat.id, text="<b>Валидация (validation)</b> — это определение соответствия разрабатываемого ПО ожиданиям и потребностям пользователя, его требованиям к системе. ")
    
    elif (message.text == "Вопрос№4"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton("Статическое тестирование")
        btn5 = types.KeyboardButton("Динамическое тестирование")
        btn6 = types.KeyboardButton("Вопрос№5")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text="Какой вид тестирования проводится на работающей системе, с запуском программного кода приложения?", reply_markup=markup)

    elif(message.text == "Динамическое тестирование"):
        bot.send_message(message.chat.id, "Верно! Молодец!✅")
    
    elif message.text == "Статическое тестирование":
        bot.send_message(message.chat.id, text="Неправильно!❌ <b>Верный ответ: Динамическое тестирование</b>")
        bot.send_message(message.chat.id, text="<b>Статическое тестирование</b> — это метод тестирования программного обеспечения, с помощью которого мы можем проверять дефекты ПО, фактически не выполняя его.")

    elif (message.text == "Вопрос№5"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton("Модульное тестирование")
        btn5 = types.KeyboardButton("Интеграционное тестирование")
        btn6 = types.KeyboardButton("Вопрос№6")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text="Какой вид тестирования проверяет корректность взаимодействия нескольких модулей, объединенных в единое целое?", reply_markup=markup)

    elif(message.text == "Интеграционное тестирование"):
        bot.send_message(message.chat.id, "Верно! Молодец!✅")
    
    elif message.text == "Модульное тестирование":
        bot.send_message(message.chat.id, text="Неправильно!❌ <b>Верный ответ: Интеграционное тестирование</b>")
        bot.send_message(message.chat.id, text="<b>Модульное тестирование</b> — проводится для тестирования какого-либо одного логически выделенного и изолированного элемента (модуля) системы в коде. Проводится самими разработчиками, так как предполагает полный доступ к коду.")

    elif (message.text == "Вопрос№6"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton("S1 – Blocker")
        btn5 = types.KeyboardButton("S2 – Critical")
        btn6 = types.KeyboardButton("Вопрос№7")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text="Ошибка, приводящая приложение в нерабочее состояние", reply_markup=markup)

    elif(message.text == "S1 – Blocker"):
        bot.send_message(message.chat.id, "Верно! Молодец!✅")
        bot.send_message(message.chat.id, "<b>Блокирующий (S1 – Blocker)</b> тестирование значительной части функциональности вообще недоступно. Блокирующая ошибка, приводящая приложение в нерабочее состояние, в результате которого дальнейшая работа с тестируемой системой или ее ключевыми функциями становится невозможна.")
    
    elif message.text == "S2 – Critical":
        bot.send_message(message.chat.id, text="Неправильно!❌ <b>Верный ответ: S1 – Blocker</b>")
        bot.send_message(message.chat.id, text="<b>Критический (S2 – Critical)</b> критическая ошибка, неправильно работающая ключевая бизнес-логика, дыра в системе безопасности, проблема, приведшая к временному падению сервера или приводящая в нерабочее состояние некоторую часть системы, то есть не работает важная часть одной какой-либо функции либо не работает значительная часть, но имеется workaround (обходной путь/другие входные точки), позволяющий продолжить тестирование.")



    elif (message.text == "Вопрос№7"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton("Нагрузочное тестирование")
        btn5 = types.KeyboardButton("Стрессовое тестирование")
        btn6 = types.KeyboardButton("Вопрос№8")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text="Какой вид тестирования применяется для исследования граничных нагрузок для программного обеспечения?", reply_markup=markup)

    elif(message.text == "Стрессовое тестирование"):
        bot.send_message(message.chat.id, "Верно! Молодец!✅")
        bot.send_message(message.chat.id, "<b>Стрессовое тестирование</b> тип тестирования, направленный для проверки, как система обращается с нарастающей нагрузкой (количеством одновременных пользователей).")
    
    elif message.text == "Нагрузочное тестирование":
        bot.send_message(message.chat.id, text="Неправильно!❌ Верный ответ: <b>Стрессовое тестирование.</b>")
        bot.send_message(message.chat.id, text="<b>Нагрузочное тестирование</b> — определение или сбор показателей производительности и времени отклика программно-технической системы или устройства в ответ на внешний запрос с целью установления соответствия требованиям, предъявляемым к данной системе (устройству).")

    elif (message.text == "Вопрос№8"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton("White box")
        btn5 = types.KeyboardButton("Black box")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn4, btn5, back)
        bot.send_message(message.chat.id, text="Последний вопрос! Как называется метод тестирование без доступа к исходному коду?", reply_markup=markup)

    elif (message.text == "Black box"):
        bot.send_message(message.chat.id, "Верно! Молодец!✅")
        bot.send_message(message.chat.id, "<b>Black box Тестирование чёрного ящика</b> — также известное как тестирование, основанное на спецификации или тестирование поведения — техника тестирования, основанная на работе исключительно с внешними интерфейсами тестируемой системы.")
        bot.send_message(message.chat.id, "🏁 Круто! {0.first_name}, поздравляю! Ты прошел тест до конца! Надеюсь бот помог повторить теорию. Ты можете заново пройти этот тест перейдя в главное меню!")

    elif message.text == "White box":
        bot.send_message(message.chat.id, text="Неправильно!❌ Верный ответ: <b>Black box.</b>")
        bot.send_message(message.chat.id, "<b>White box Тестирование белого ящика</b> — метод тестирования ПО, который предполагает, что внутренняя структура/устройство/реализация системы известны тестировщику.")
        bot.send_message(message.chat.id, "🏁 Круто! Поздравляю! Ты прошел тест до конца! Надеюсь бот помог повторить теорию. Ты можете заново пройти этот тест перейдя в главное меню!")
    
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")
    

bot.polling(none_stop=True)
