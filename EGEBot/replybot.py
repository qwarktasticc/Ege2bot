import telebot
from telebot import types

bot = telebot.TeleBot('6213169353:AAEzp-fJCys0_I4lLvri_LZ-Y5pWZ6HWgHQ')


@bot.message_handler(commands=['start'])
def start(message):
    first_name = message.from_user.first_name
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Геометрия📕')
    btn2 = types.KeyboardButton('Алгебра📒')
    btn3 = types.KeyboardButton('Тригонометрия📗')
    markup.row(btn1, btn2, btn3)
    btn4 = types.KeyboardButton('Шкала перевода баллов ЕГЭ📝')
    btn5 = types.KeyboardButton('Полезные каналы📌')
    btn6 = types.KeyboardButton('Структура ЕГЭ🧐')
    btn7 = types.KeyboardButton('Проверь свои знания🤓')
    markup.row(btn4, btn5, btn6, btn7)
    bot.send_message(message.chat.id, text=f'Привет, {first_name}!'
                                           f' Этот бот поможет тебе с подготовкой к ЕГЭ по профильной математике.',
                     reply_markup=markup)


@bot.message_handler(regexp='Нет')
@bot.message_handler(regexp='Вернуться в главное меню')
def main_menu(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Геометрия📕')
    btn2 = types.KeyboardButton('Алгебра📒')
    btn3 = types.KeyboardButton('Тригонометрия📗')
    markup.row(btn1, btn2, btn3)
    btn4 = types.KeyboardButton('Шкала перевода баллов ЕГЭ📝')
    btn5 = types.KeyboardButton('Полезные каналы📌')
    btn6 = types.KeyboardButton('Структура ЕГЭ🧐')
    btn7 = types.KeyboardButton('Проверь свои знания🤓')
    markup.row(btn4, btn5, btn6, btn7)
    bot.send_message(message.chat.id, 'Вы вернулись в главное меню',
                     reply_markup=markup)


@bot.message_handler(regexp='Геометрия📕')
def geometry(message):
    if message.text == 'Геометрия📕':
        markup = types.ReplyKeyboardMarkup()
        butn1 = types.KeyboardButton('Планиметрия')
        butn2 = types.KeyboardButton('Стереометрия')
        butn3 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(butn1, butn2, butn3)
        bot.send_message(message.chat.id, 'Тут содержится теория к блокам планиметрия и стереометрия. Пользуйся😉',
                         reply_markup=markup)


@bot.message_handler(regexp='Планиметрия')
def planimetry(message):
    bot.send_document(message.chat.id, document=open('2023-08-01_19-40-36.pdf', 'rb'))


@bot.message_handler(regexp='Стереометрия')
def stereometry(message):
    bot.send_document(message.chat.id, document=open('Teoria_k_zadaniyu_2.pdf', 'rb'))


@bot.message_handler(regexp='Тригонометрия📗')
def trigonometry(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Большой файл с общей теорией о тригонометрии')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Тригонометрическая окружность')
    btn3 = types.KeyboardButton('Формулы приведения')
    markup.row(btn2, btn3)
    btn4 = types.KeyboardButton('Вернуться в главное меню')
    markup.row(btn4)
    bot.send_message(message.chat.id, 'Это поможет тебе разобраться с тригонометрией😎', reply_markup=markup)


@bot.message_handler(regexp='Большой файл с общей теорией о тригонометрии')
def big_f(message):
    bot.send_document(message.chat.id, document=open('Trigonometria_Alles_v2.pdf', 'rb'))


@bot.message_handler(regexp='Тригонометрическая окружность')
def tryg_circle(message):
    bot.send_photo(message.chat.id, photo=open('2023-08-05_18-12-10.png', 'rb'))


@bot.message_handler(regexp='Формулы приведения')
def formulae(message):
    bot.send_photo(message.chat.id, photo=open('2023-08-05_18-30-13.png', 'rb'))


@bot.message_handler(regexp='Алгебра📒')
def algebra(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Логарифмы')
    btn2 = types.KeyboardButton('Производные')
    btn3 = types.KeyboardButton('Степени и корни')
    btn4 = types.KeyboardButton('Функции')
    markup.row(btn1, btn2, btn3, btn4)
    btn5 = types.KeyboardButton('Формулы сокращенного умножения и уравнения')
    btn6 = types.KeyboardButton('Модули и арифметические прогрессии')
    btn7 = types.KeyboardButton('Метод рационализации и теория к 9 заданию')
    btn8 = types.KeyboardButton('Графики')
    markup.add(btn5, btn6, btn7, btn8)
    btn9 = types.KeyboardButton('Вернуться в главное меню')
    markup.add(btn9)
    bot.send_message(message.chat.id, 'Что бы ты хотел узнать о алгебре?', reply_markup=markup)


@bot.message_handler(regexp='Логарифмы')
def logarifmi(message):
    bot.send_photo(message.chat.id, photo=open('2023-08-07_21-02-23.png', 'rb'))


@bot.message_handler(regexp='Производные')
def proizvodnie(message):
    bot.send_photo(message.chat.id, photo=open('2023-08-07_21-02-58.png', 'rb'))


@bot.message_handler(regexp='Степени и корни')
def step_korni(message):
    bot.send_photo(message.chat.id, photo=open('2023-08-07_21-03-30.png', 'rb'))


@bot.message_handler(regexp='Функции')
def funcii(message):
    bot.send_document(message.chat.id, document=open('Teoria_k_zadaniyu_10.pdf', 'rb'))


@bot.message_handler(regexp='Формулы сокращенного умножения и уравнения')
def f_s_m(message):
    bot.send_photo(message.chat.id, photo=open('2023-08-07_21-04-17.png', 'rb'))


@bot.message_handler(regexp='Модули и арифметические прогрессии')
def moduls(message):
    bot.send_photo(message.chat.id, photo=open('2023-08-07_21-04-46.png', 'rb'))


@bot.message_handler(regexp='Метод рационализации и теория к 9 заданию')
def m_z_m(message):
    bot.send_photo(message.chat.id, photo=open('2023-08-07_21-05-21.png', 'rb'))


@bot.message_handler(regexp='Графики')
def grafics(message):
    bot.send_document(message.chat.id, document=open('Teoria_k_zadaniyu_7.pdf', 'rb'))


@bot.message_handler(regexp='Шкала перевода баллов ЕГЭ📝')
def shkala(message):
    bot.send_photo(message.chat.id, photo=open('2023-08-10_17-31-27.png', 'rb'))
    bot.send_message(message.chat.id, 'Красным обозначен минимальный балл для поступления в вуз.'
                                      '\nЗеленая область означает высокий уровень подготовки участника к экзамену.')


@bot.message_handler(regexp='Полезные каналы📌')
def useful_channels(message):
    bot.send_message(message.chat.id, 'Могу порекомендовать эти каналы:'
                                      '\nШкола Пифагора ЕГЭ по математике'
                                      '\n(https://www.youtube.com/@pifagor1)'
                                      '\nМатематик МГУ(https://www.youtube.com/@hitman_math)')


@bot.message_handler(regexp='Структура ЕГЭ🧐')
def structure(message):
    bot.send_message(message.chat.id, '1 часть:'
                                      '\nВ ней содержится 11 заданий с кратким ответом.'
                                      'Приносит 11 первичных баллов или 64 вторичных.'
                                      '\n2 часть:'
                                      '\nВ ней содержится 7 заданий с развернутым ответом.'
                                      ' Приносит 20 баллов за полное решение.')


@bot.message_handler(regexp='Перейти к заданиям')
@bot.message_handler(regexp='Проверь свои знания🤓')
def test(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Задание 1')
    btn2 = types.KeyboardButton('Задание 2')
    btn3 = types.KeyboardButton('Задание 3')
    btn4 = types.KeyboardButton('Задание 4')
    btn5 = types.KeyboardButton('Задание 5')
    btn6 = types.KeyboardButton('Задание 6')
    btn7 = types.KeyboardButton('Задание 7')
    btn8 = types.KeyboardButton('Задание 8')
    btn9 = types.KeyboardButton('Задание 9')
    btn10 = types.KeyboardButton('10 задание')
    btn11 = types.KeyboardButton('11 задание')
    btn12 = types.KeyboardButton('Вернуться в главное меню')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
    bot.send_message(message.chat.id, 'Тут ты можешь выбрать задания из первой части и ответить на них.'
                                      '\nТебе будет предложено 4 варианта и один из них правильный.', reply_markup=markup)


user_task = {}


@bot.message_handler(regexp='Задание 1')
def zadanie_1(message):
    if message.text == 'Задание 1':
        # Сохраняем текущее задание для данного пользователя
        user_task[message.chat.id] = 'Задание 1'

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('45')
        btn2 = types.KeyboardButton('55')
        btn3 = types.KeyboardButton('90')
        btn4 = types.KeyboardButton('125')
        btn5 = types.KeyboardButton('Перейти к заданиям')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_photo(message.chat.id, photo=open('2023-08-14_20-34-43.png', 'rb'), reply_markup=markup)


@bot.message_handler(
    func=lambda message: message.text in ['45', '55', '90', '125'] and user_task.get(message.chat.id) == 'Задание 1')
def check_answer(message):
    if message.text == '55':
        bot.send_message(message.chat.id, 'Правильный ответ')
    else:
        bot.send_message(message.chat.id, 'Неправильный ответ')
    # Очищаем активное задание для данного пользователя
    user_task.pop(message.chat.id, None)


@bot.message_handler(regexp='Задание 2')
def zadanie_2(message):
    if message.text == 'Задание 2':
        user_task[message.chat.id] = 'Задание 2'

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('90')
        btn2 = types.KeyboardButton('60')
        btn3 = types.KeyboardButton('30')
        btn4 = types.KeyboardButton('45')
        btn5 = types.KeyboardButton('Перейти к заданиям')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_photo(message.chat.id, photo=open('2023-08-14_20-36-33.png', 'rb'), reply_markup=markup)


@bot.message_handler(
    func=lambda message: message.text in ['90', '60', '30', '45'] and user_task.get(message.chat.id) == 'Задание 2')
def check_answer_2(message):
    if message.text == '60':
        bot.send_message(message.chat.id, 'Правильный ответ')
    else:
        bot.send_message(message.chat.id, 'Неправильный ответ')
    user_task.pop(message.chat.id, None)


@bot.message_handler(regexp='Задание 3')
def zadanie_3(message):
    if message.text == 'Задание 3':
        user_task[message.chat.id] = 'Задание 3'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('0,4')
        btn2 = types.KeyboardButton('0,35')
        btn3 = types.KeyboardButton('0,2')
        btn4 = types.KeyboardButton('0,6')
        btn5 = types.KeyboardButton('Перейти к заданиям')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_photo(message.chat.id, photo=open('2023-08-14_20-37-22.png', 'rb'), reply_markup=markup)


@bot.message_handler(
    func=lambda message: message.text in ['0,4', '0,35', '0,2', '0,6'] and user_task.get(message.chat.id) == 'Задание 3')
def check_answer_2(message):
    if message.text == '0,4':
        bot.send_message(message.chat.id, 'Правильный ответ')
    else:
        bot.send_message(message.chat.id, 'Неправильный ответ')
    user_task.pop(message.chat.id, None)


@bot.message_handler(regexp='Задание 4')
def zadanie_4(message):
    if message.text == 'Задание 4':
        user_task[message.chat.id] = 'Задание 4'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('0,45')
        btn2 = types.KeyboardButton('0,65')
        btn3 = types.KeyboardButton('0,8')
        btn4 = types.KeyboardButton('0,55')
        btn5 = types.KeyboardButton('Перейти к заданиям')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_photo(message.chat.id, photo=open('2023-08-14_20-40-18.png', 'rb'), reply_markup=markup)


@bot.message_handler(
    func=lambda message: message.text in ['0,45', '0,65', '0,8', '0,55'] and user_task.get(message.chat.id) == 'Задание 4')
def check_answer_2(message):
    if message.text == '0,55':
        bot.send_message(message.chat.id, 'Правильный ответ')
    else:
        bot.send_message(message.chat.id, 'Неправильный ответ')
    user_task.pop(message.chat.id, None)


@bot.message_handler(regexp='Задание 5')
def zadanie_5(message):
    if message.text == 'Задание 5':
        user_task[message.chat.id] = 'Задание 5'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('3')
        btn2 = types.KeyboardButton('5')
        btn3 = types.KeyboardButton('11')
        btn4 = types.KeyboardButton('2')
        btn5 = types.KeyboardButton('Перейти к заданиям')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_photo(message.chat.id, photo=open('2023-08-14_20-41-33.png', 'rb'), reply_markup=markup)


@bot.message_handler(
    func=lambda message: message.text in ['3', '5', '11', '2'] and user_task.get(message.chat.id) == 'Задание 5')
def check_answer_2(message):
    if message.text == '2':
        bot.send_message(message.chat.id, 'Правильный ответ')
    else:
        bot.send_message(message.chat.id, 'Неправильный ответ')
    user_task.pop(message.chat.id, None)


@bot.message_handler(regexp='Задание 6')
def zadanie_6(message):
    if message.text == 'Задание 6':
        user_task[message.chat.id] = 'Задание 6'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('0,2')
        btn2 = types.KeyboardButton('25')
        btn3 = types.KeyboardButton('5')
        btn4 = types.KeyboardButton('125')
        btn5 = types.KeyboardButton('Перейти к заданиям')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_photo(message.chat.id, photo=open('2023-08-14_20-45-48.png', 'rb'), reply_markup=markup)


@bot.message_handler(
    func=lambda message: message.text in ['0,2', '5', '25', '125'] and user_task.get(message.chat.id) == 'Задание 6')
def check_answer_2(message):
    if message.text == '5':
        bot.send_message(message.chat.id, 'Правильный ответ')
    else:
        bot.send_message(message.chat.id, 'Неправильный ответ')
    user_task.pop(message.chat.id, None)


@bot.message_handler(regexp='Задание 7')
def zadanie_7(message):
    if message.text == 'Задание 7':
        user_task[message.chat.id] = 'Задание 7'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('4')
        btn2 = types.KeyboardButton('3')
        btn3 = types.KeyboardButton('5')
        btn4 = types.KeyboardButton('1')
        btn5 = types.KeyboardButton('Перейти к заданиям')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_photo(message.chat.id, photo=open('2023-08-14_20-49-25.png', 'rb'), reply_markup=markup)


@bot.message_handler(
    func=lambda message: message.text in ['4', '3', '5', '1'] and user_task.get(message.chat.id) == 'Задание 7')
def check_answer_2(message):
    if message.text == '3':
        bot.send_message(message.chat.id, 'Правильный ответ')
    else:
        bot.send_message(message.chat.id, 'Неправильный ответ')
    user_task.pop(message.chat.id, None)


@bot.message_handler(regexp='Задание 8')
def zadanie_8(message):
    if message.text == 'Задание 8':
        user_task[message.chat.id] = 'Задание 8'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('0,445')
        btn2 = types.KeyboardButton('0,5')
        btn3 = types.KeyboardButton('0,45')
        btn4 = types.KeyboardButton('0,625')
        btn5 = types.KeyboardButton('Перейти к заданиям')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_photo(message.chat.id, photo=open('2023-08-14_20-51-48.png', 'rb'), reply_markup=markup)


@bot.message_handler(
    func=lambda message: message.text in ['0,445', '0,5', '0,45', '0,625'] and user_task.get(message.chat.id) == 'Задание 8')
def check_answer_2(message):
    if message.text == '0,445':
        bot.send_message(message.chat.id, 'Правильный ответ')
    else:
        bot.send_message(message.chat.id, 'Неправильный ответ')
    user_task.pop(message.chat.id, None)


@bot.message_handler(regexp='Задание 9')
def zadanie_9(message):
    if message.text == 'Задание 9':
        user_task[message.chat.id] = 'Задание 9'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('6')
        btn2 = types.KeyboardButton('18')
        btn3 = types.KeyboardButton('20')
        btn4 = types.KeyboardButton('30')
        btn5 = types.KeyboardButton('Перейти к заданиям')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_photo(message.chat.id, photo=open('2023-08-14_21-07-14.png', 'rb'), reply_markup=markup)


@bot.message_handler(
    func=lambda message: message.text in ['6', '18', '20', '30'] and user_task.get(message.chat.id) == 'Задание 9')
def check_answer_2(message):
    if message.text == '18':
        bot.send_message(message.chat.id, 'Правильный ответ')
    else:
        bot.send_message(message.chat.id, 'Неправильный ответ')
    user_task.pop(message.chat.id, None)


@bot.message_handler(regexp='10 задание')
def zadanie_10(message):
    if message.text == '10 задание':
        user_task[message.chat.id] = '10 задание'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('8')
        btn2 = types.KeyboardButton('-4')
        btn3 = types.KeyboardButton('-5')
        btn4 = types.KeyboardButton('10')
        btn5 = types.KeyboardButton('Перейти к заданиям')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_photo(message.chat.id, photo=open('2023-08-14_21-06-40.png', 'rb'), reply_markup=markup)


@bot.message_handler(
    func=lambda message: message.text in ['8', '-4', '-5', '10'] and user_task.get(message.chat.id) == '10 задание')
def check_answer_2(message):
    if message.text == '8':
        bot.send_message(message.chat.id, 'Правильный ответ')
    else:
        bot.send_message(message.chat.id, 'Неправильный ответ')
    user_task.pop(message.chat.id, None)


@bot.message_handler(regexp='11 задание')
def zadanie_11(message):
    if message.text == '11 задание':
        user_task[message.chat.id] = '11 задание'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('2')
        btn2 = types.KeyboardButton('4')
        btn3 = types.KeyboardButton('14')
        btn4 = types.KeyboardButton('0')
        btn5 = types.KeyboardButton('Перейти к заданиям')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_photo(message.chat.id, photo=open('2023-08-14_21-15-16.png', 'rb'), reply_markup=markup)


@bot.message_handler(
    func=lambda message: message.text in ['2', '4', '14', '0'] and user_task.get(message.chat.id) == '11 задание')
def check_answer_2(message):
    if message.text == '8':
        bot.send_message(message.chat.id, 'Правильный ответ')
    else:
        bot.send_message(message.chat.id, 'Неправильный ответ')
    user_task.pop(message.chat.id, None)


bot.polling(none_stop=True)