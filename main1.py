#pip install pyTelegramBotAPI==3.6.7
import telebot
from telebot import types
from openpyxl import load_workbook

wb = load_workbook('./Проект.xlsx')

moder_chat = 0

list = wb.active
bot = telebot.TeleBot("1165779184:AAELE6Gs19G6Yi-ARpCn3F883gz9816onNs")

@bot.message_handler(commands=['start'])
def privetstvie(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton("Начать тестирование", callback_data="question1.1")
    markup.add(button1)
    bot.send_message(message.chat.id, "Здравствуйте! Этот бот поможет подобрать вам ВУЗ с помощью небольшого теста.", reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == "question1.1":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("Да", callback_data="question2")
            button2 = types.InlineKeyboardButton("Нет", callback_data="question5")
            button3 = types.InlineKeyboardButton("Назад", callback_data="privetstvie1")
            markup.add(button1, button2, button3)
            bot.send_message(call.message.chat.id, "Хотел(а) бы ты связать свою жизнь с математикой?", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Здравствуйте! Этот бот поможет подобрать вам ВУЗ с помощью небольшого теста.", reply_markup=None)
        elif call.data == "question2":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("Да", callback_data="question3")
            button2 = types.InlineKeyboardButton("Нет", callback_data="question4")
            button3 = types.InlineKeyboardButton("Назад", callback_data="question1.1")
            markup.add(button1, button2, button3)
            bot.send_message(call.message.chat.id, "Хотел(а) бы ты видеть творческую сторону своей профессии?", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Хотел(а) бы ты связать свою жизнь с математикой?", reply_markup=None)
        elif call.data == "question3":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("Схемы и графики", callback_data="vibor1")
            button2 = types.InlineKeyboardButton("Рисунки", callback_data="spisok3")
            button3 = types.InlineKeyboardButton("Назад", callback_data="question2")
            markup.add(button1, button2, button3)
            bot.send_message(call.message.chat.id, "Выбери:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Хотел(а) бы ты видеть творческую сторону своей профессии?", reply_markup=None)
        elif call.data == "question4":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("Да", callback_data="spisok4")
            button2 = types.InlineKeyboardButton("Нет", callback_data="vibor2")
            button3 = types.InlineKeyboardButton("Назад", callback_data="question3")
            markup.add(button1, button2, button3)
            bot.send_message(call.message.chat.id, "Хотел(а) бы ты связать свою работу с медициной?", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Хотел(а) бы ты видеть творческую сторону своей профессии?", reply_markup=None)
        elif call.data == "question5":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("Да", callback_data="question6")
            button2 = types.InlineKeyboardButton("Нет", callback_data="question8")
            button3 = types.InlineKeyboardButton("Назад", callback_data="question1.1")
            markup.add(button1, button2, button3)
            bot.send_message(call.message.chat.id, "Хотел(а) бы ты выступать перед людьми?", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Хотел(а) бы ты связать свою жизнь с математикой?", reply_markup=None)
        elif call.data == "question6":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("Да", callback_data="vibor3")
            button2 = types.InlineKeyboardButton("Нет", callback_data="question7")
            button3 = types.InlineKeyboardButton("Назад", callback_data="question5")
            markup.add(button1, button2, button3)
            bot.send_message(call.message.chat.id, "Хотел(а) бы ты работать с детьми?", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Хотел(а) бы ты выступать перед людьми?", reply_markup=None)
        elif call.data == "question7":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("Да", callback_data="vibor4")
            button2 = types.InlineKeyboardButton("Нет", callback_data="spisok11")
            button3 = types.InlineKeyboardButton("Назад", callback_data="question6")
            markup.add(button1, button2, button3)
            bot.send_message(call.message.chat.id, "Хотел(а) бы ты работать в медиа?", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Хотел(а) бы ты работать с детьми?", reply_markup=None)
        elif call.data == "question8":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("Работать с людьми", callback_data="question9")
            button2 = types.InlineKeyboardButton("Работать с языками", callback_data="vibor5")
            button3 = types.InlineKeyboardButton("Назад", callback_data="question5")
            markup.add(button1, button2, button3)
            bot.send_message(call.message.chat.id, "Выбери:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Хотел(а) бы ты выступать перед людьми?", reply_markup=None)
        elif call.data == "question9":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("Да", callback_data="vibor6")
            button2 = types.InlineKeyboardButton("Нет", callback_data="spisok14")
            button3 = types.InlineKeyboardButton("Назад", callback_data="question8")
            markup.add(button1, button2, button3)
            bot.send_message(call.message.chat.id, "Готов(а) ли ты учить биологию?", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выбери:", reply_markup=None)
        elif call.data == "privetstvie1":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("Начать тестирование", callback_data="question1.1")
            markup.add(button1)
            bot.send_message(call.message.chat.id,
                             "Здравствуйте! Этот бот поможет подобрать вам ВУЗ с помощью небольшого теста.",
                             reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Хотел(а) бы ты связать свою жизнь с математикой?", reply_markup=None)
        elif call.data == "vibor1":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("Маркетинг", callback_data="spisok1")
            button2 = types.InlineKeyboardButton("Менеджмент", callback_data="spisok2")
            button3 = types.InlineKeyboardButton("Бизнес информатика", callback_data="spisok17")
            button4 = types.InlineKeyboardButton("Назад", callback_data="question3")
            markup.add(button1, button2, button3, button4)
            bot.send_message(call.message.chat.id, "Выберите направление:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выбери:", reply_markup=None)
        elif call.data == "vibor2":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("Экономическое", callback_data="spisok5")
            button2 = types.InlineKeyboardButton("Математическое", callback_data="spisok6")
            button3 = types.InlineKeyboardButton("Назад", callback_data="question4")
            markup.add(button1, button2, button3)
            bot.send_message(call.message.chat.id, "Выберите направление:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Хотел(а) бы ты связать свою работу с медициной?", reply_markup=None)
        elif call.data == "vibor3":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("Педагогика", callback_data="spisok7")
            button2 = types.InlineKeyboardButton("Актёрский", callback_data="spisok8")
            button3 = types.InlineKeyboardButton("Назад", callback_data="question6")
            markup.add(button1, button2, button3)
            bot.send_message(call.message.chat.id, "Выберите направление:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Хотел(а) бы ты работать с детьми?", reply_markup=None)
        elif call.data == "vibor4":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("Связь с общественностью", callback_data="spisok9")
            button2 = types.InlineKeyboardButton("Журналистика", callback_data="spisok10")
            button3 = types.InlineKeyboardButton("Назад", callback_data="question7")
            markup.add(button1, button2, button3)
            bot.send_message(call.message.chat.id, "Выберите направление:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Хотел(а) бы ты работать в медиа?", reply_markup=None)
        elif call.data == "vibor5":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("Филология", callback_data="spisok12")
            button2 = types.InlineKeyboardButton("Лингвистика", callback_data="spisok13")
            button3 = types.InlineKeyboardButton("Назад", callback_data="question8")
            markup.add(button1, button2, button3)
            bot.send_message(call.message.chat.id, "Выберите направление:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выбери:", reply_markup=None)
        elif call.data == "vibor6":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("Психология", callback_data="spisok15")
            button2 = types.InlineKeyboardButton("Лечебное дело", callback_data="spisok16")
            button3 = types.InlineKeyboardButton("Назад", callback_data="question9")
            markup.add(button1, button2, button3)
            bot.send_message(call.message.chat.id, "Выберите направление:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Готов(а) ли ты учить биологию?", reply_markup=None)
        elif call.data == "spisok1":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("ВШЭ", callback_data="Vshe1")
            button2 = types.InlineKeyboardButton("Плеханова", callback_data="Plehanova1")
            button3 = types.InlineKeyboardButton("РГГУ", callback_data="RGGU1")
            button4 = types.InlineKeyboardButton("МГПУ", callback_data="MGPU1")
            button5 = types.InlineKeyboardButton("РУДН", callback_data="RUDN1")
            button6 = types.InlineKeyboardButton("РАНХиГС", callback_data="RANHiGS1")
            button7 = types.InlineKeyboardButton("РГСУ", callback_data="RGSU1")
            button8 = types.InlineKeyboardButton("Назад", callback_data="vibor1")
            markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
            bot.send_message(call.message.chat.id, "ВУЗы, которые вам подойдут:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите направление:", reply_markup=None)
        elif call.data == "spisok2":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("МГУ", callback_data="MGU1")
            button2 = types.InlineKeyboardButton("ВШЭ", callback_data="Vshe2")
            button3 = types.InlineKeyboardButton("Бауманка", callback_data="Bauma1")
            button4 = types.InlineKeyboardButton("РУДН", callback_data="RUDN2")
            button5 = types.InlineKeyboardButton("РАНХиГС", callback_data="RANHiGS2")
            button6 = types.InlineKeyboardButton("Плехановка", callback_data="Plehanova2")
            button7 = types.InlineKeyboardButton("РГГУ", callback_data="RGGU2")
            button8 = types.InlineKeyboardButton("Назад", callback_data="vibor1")
            markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
            bot.send_message(call.message.chat.id, "ВУЗы, которые вам подойдут:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите направление:", reply_markup=None)
        elif call.data == "spisok3":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("МАРХИ", callback_data="MARHI1")
            button2 = types.InlineKeyboardButton("РУДН", callback_data="RUDN3")
            button3 = types.InlineKeyboardButton("Назад", callback_data="question3")
            markup.add(button1, button2, button3)
            bot.send_message(call.message.chat.id, "ВУЗы, которые вам подойдут:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выбери:", reply_markup=None)
        elif call.data == "spisok4":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("МГУ", callback_data="MGU2")
            button2 = types.InlineKeyboardButton("Пирогова", callback_data="Pirogova1")
            button3 = types.InlineKeyboardButton("РГСУ", callback_data="RGSU2")
            button4 = types.InlineKeyboardButton("Сеченова", callback_data="Sechenov1")
            button5 = types.InlineKeyboardButton("Назад", callback_data="question4")
            markup.add(button1, button2, button3, button4, button5)
            bot.send_message(call.message.chat.id, "ВУЗы, которые вам подойдут:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Хотел(а) бы ты связать свою работу с медициной?", reply_markup=None)
        elif call.data == "spisok5":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("МГУ", callback_data="MGU3")
            button2 = types.InlineKeyboardButton("ВШЭ", callback_data="Vshe3")
            button3 = types.InlineKeyboardButton("РГГУ", callback_data="RGGU3")
            button4 = types.InlineKeyboardButton("РУДН", callback_data="RUDN4")
            button5 = types.InlineKeyboardButton("Плеханова", callback_data="Plehanova3")
            button6 = types.InlineKeyboardButton("Назад", callback_data="vibor2")
            markup.add(button1, button2, button3, button4, button5, button6)
            bot.send_message(call.message.chat.id, "ВУЗы, которые вам подойдут:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите направление:", reply_markup=None)
        elif call.data == "spisok6":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("ВШЭ", callback_data="Vshe4")
            button2 = types.InlineKeyboardButton("Бауманка", callback_data="Bauma2")
            button3 = types.InlineKeyboardButton("РГГУ", callback_data="RGGU4")
            button4 = types.InlineKeyboardButton("МГУ", callback_data="MGU4")
            button5 = types.InlineKeyboardButton("МИСИС", callback_data="MISIS1")
            button6 = types.InlineKeyboardButton("Назад", callback_data="vibor2")
            markup.add(button1, button2, button3, button4, button5, button6)
            bot.send_message(call.message.chat.id, "ВУЗы, которые вам подойдут:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите направление:", reply_markup=None)
        elif call.data == "spisok7":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("МГПУ (начал. образование)", callback_data="MGPU2")
            button2 = types.InlineKeyboardButton("РГСУ (учит. физры)", callback_data="RGSU3")
            button3 = types.InlineKeyboardButton("Назад", callback_data="vibor3")
            markup.add(button1, button2, button3)
            bot.send_message(call.message.chat.id, "ВУЗы, которые вам подойдут:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите направление:", reply_markup=None)
        elif call.data == "spisok8":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("МГПУ", callback_data="MGPU3")
            button2 = types.InlineKeyboardButton("РГСУ", callback_data="RGSU4")
            button3 = types.InlineKeyboardButton("Щукина", callback_data="Shukina1")
            button4 = types.InlineKeyboardButton("ВГИК", callback_data="VGIK1")
            button5 = types.InlineKeyboardButton("Назад", callback_data="vibor3")
            markup.add(button1, button2, button3, button4, button5)
            bot.send_message(call.message.chat.id, "ВУЗы, которые вам подойдут:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите направление:", reply_markup=None)
        elif call.data == "spisok9":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("МГУ", callback_data="MGU5")
            button2 = types.InlineKeyboardButton("ВШЭ", callback_data="Vshe5")
            button3 = types.InlineKeyboardButton("РУДН", callback_data="RUDN5")
            button4 = types.InlineKeyboardButton("РАНХиГС", callback_data="RANHiGS3")
            button5 = types.InlineKeyboardButton("Плехановка", callback_data="Plehanova4")
            button6 = types.InlineKeyboardButton("Назад", callback_data="vibor4")
            markup.add(button1, button2, button3, button4, button5, button6)
            bot.send_message(call.message.chat.id, "ВУЗы, которые вам подойдут:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите направление:", reply_markup=None)
        elif call.data == "spisok10":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("ВШЭ", callback_data="Vshe6")
            button2 = types.InlineKeyboardButton("МГУ", callback_data="MGU6")
            button3 = types.InlineKeyboardButton("РУДН", callback_data="RUDN6")
            button4 = types.InlineKeyboardButton("Плехановка", callback_data="Plehanova5")
            button5 = types.InlineKeyboardButton("РГГУ", callback_data="RGGU5")
            button6 = types.InlineKeyboardButton("Косыгина", callback_data="Kosigina1")
            button7 = types.InlineKeyboardButton("Назад", callback_data="vibor4")
            markup.add(button1, button2, button3, button4, button5, button6, button7)
            bot.send_message(call.message.chat.id, "ВУЗы, которые вам подойдут:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите направление:", reply_markup=None)
        elif call.data == "spisok11":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("МГУ", callback_data="MGU7")
            button2 = types.InlineKeyboardButton("ВШЭ", callback_data="Vshe7")
            button3 = types.InlineKeyboardButton("РУДН", callback_data="RUDN7")
            button4 = types.InlineKeyboardButton("РАНХиГС", callback_data="RANHiGS4")
            button5 = types.InlineKeyboardButton("МГПУ", callback_data="MGPU4")
            button6 = types.InlineKeyboardButton("Плехановка", callback_data="Plehanova6")
            button7 = types.InlineKeyboardButton("Назад", callback_data="question7")
            markup.add(button1, button2, button3, button4, button5, button6, button7)
            bot.send_message(call.message.chat.id, "ВУЗы, которые вам подойдут:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Хотел(а) бы ты работать в медиа?", reply_markup=None)
        elif call.data == "spisok12":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("МГУ", callback_data="MGU8")
            button2 = types.InlineKeyboardButton("ВШЭ", callback_data="Vshe8")
            button3 = types.InlineKeyboardButton("РУДН", callback_data="RUDN8")
            button4 = types.InlineKeyboardButton("Назад", callback_data="vibor5")
            markup.add(button1, button2, button3, button4)
            bot.send_message(call.message.chat.id, "ВУЗы, которые вам подойдут:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите направление:", reply_markup=None)
        elif call.data == "spisok13":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("МГУ", callback_data="MGU9")
            button2 = types.InlineKeyboardButton("ВШЭ", callback_data="Vshe9")
            button3 = types.InlineKeyboardButton("Плеханова", callback_data="Plehanova7")
            button4 = types.InlineKeyboardButton("РУДН", callback_data="RUDN9")
            button5 = types.InlineKeyboardButton("Назад", callback_data="vibor5")
            markup.add(button1, button2, button3, button4, button5)
            bot.send_message(call.message.chat.id, "ВУЗы, которые вам подойдут:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите направление:", reply_markup=None)
        elif call.data == "spisok14":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("МГУ", callback_data="MGU10")
            button2 = types.InlineKeyboardButton("РУДН", callback_data="RUDN10")
            button3 = types.InlineKeyboardButton("РАНХиГС", callback_data="RANHiGS5")
            button4 = types.InlineKeyboardButton("Плеханова", callback_data="Plehanova8")
            button5 = types.InlineKeyboardButton("РГГУ", callback_data="RGGU6")
            button6 = types.InlineKeyboardButton("РГСУ", callback_data="RGSU5")
            button7 = types.InlineKeyboardButton("Назад", callback_data="question9")
            markup.add(button1, button2, button3, button4, button5, button6, button7)
            bot.send_message(call.message.chat.id, "ВУЗы, которые вам подойдут:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Готов(а) ли ты учить биологию?", reply_markup=None)
        elif call.data == "spisok15":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("ВШЭ", callback_data="Vshe10")
            button2 = types.InlineKeyboardButton("РУДН", callback_data="RUDN11")
            button3 = types.InlineKeyboardButton("МГПУ", callback_data="MGPU5")
            button4 = types.InlineKeyboardButton("РГГУ", callback_data="RGGU7")
            button5 = types.InlineKeyboardButton("Косыгина", callback_data="Kosigina2")
            button6 = types.InlineKeyboardButton("Назад", callback_data="vibor6")
            markup.add(button1, button2, button3, button4, button5, button6)
            bot.send_message(call.message.chat.id, "ВУЗы, которые вам подойдут:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите направление:", reply_markup=None)
        elif call.data == "spisok16":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("МГУ", callback_data="MGU11")
            button2 = types.InlineKeyboardButton("Пирогова", callback_data="Pirogova2")
            button3 = types.InlineKeyboardButton("РУДН", callback_data="RUDN12")
            button4 = types.InlineKeyboardButton("Евдокимова", callback_data="Evdokimova1")
            button5 = types.InlineKeyboardButton("Назад", callback_data="vibor6")
            markup.add(button1, button2, button3, button4, button5)
            bot.send_message(call.message.chat.id, "ВУЗы, которые вам подойдут:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите направление:", reply_markup=None)
        elif call.data == "spisok17":
            markup = types.InlineKeyboardMarkup(row_width=1)
            button1 = types.InlineKeyboardButton("ВШЭ", callback_data="Vshe11")
            button2 = types.InlineKeyboardButton("Бауманка", callback_data="Bauma3")
            button3 = types.InlineKeyboardButton("РУДН", callback_data="RUDN13")
            button4 = types.InlineKeyboardButton("МИСИС", callback_data="MISIS2")
            button5 = types.InlineKeyboardButton("РАНХиГС", callback_data="RANHiGS6")
            button6 = types.InlineKeyboardButton("МГПУ", callback_data="MGPU6")
            button7 = types.InlineKeyboardButton("МИРЭА", callback_data="MIREA1")
            button8 = types.InlineKeyboardButton("Назад", callback_data="vibor1")
            markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
            bot.send_message(call.message.chat.id, "ВУЗы, которые вам подойдут:", reply_markup=markup)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Выберите направление:", reply_markup=None)
        elif call.data == "Vshe1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Vshe2":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BI3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BI4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BI5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BI6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BI7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BI8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BI9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BI10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BI11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BI12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BI13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BI14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BI15"].value + "\n" + "\n")
        elif call.data == "Vshe3":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["AJ3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["AJ4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["AJ5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["AJ6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["AJ7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["AJ8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["AJ9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["AJ10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["AJ11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["AJ12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["AJ13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["AJ14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["AJ15"].value + "\n" + "\n")
        elif call.data == "Vshe4":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["CA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["CA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["CA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["CA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["CA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["CA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["CA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["CA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["CA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["CA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["CA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["CA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["CA15"].value + "\n" + "\n")
        elif call.data == "Vshe5":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Vshe6":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Vshe7":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Vshe8":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["AO4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["AO5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["AO6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["AO7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["AO8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["AO9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["AO10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["AO11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["AO12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["AO13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["AO14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["AO15"].value + "\n" + "\n")
        elif call.data == "Vshe9":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Vshe10":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Vshe11":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Plehanova1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BB3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BB4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BB5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BB6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BB7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BB8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BB9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BB10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BB11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BB12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BB13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BB14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BB15"].value + "\n" + "\n")
        elif call.data == "Plehanova2":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BM3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BM4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BM5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BM6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BM7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BM8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BM9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BM10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BM11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BM12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BM13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BM14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BM15"].value + "\n" + "\n")
        elif call.data == "Plehanova3":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["AM3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["AM4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["AM5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["AM6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["AM7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["AM8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["AM9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["AM10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["AM11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["AM12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["AM13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["AM14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["AM15"].value + "\n" + "\n")
        elif call.data == "Plehanova4":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Plehanova5":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Plehanova6":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Plehanova7":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Plehanova8":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RGGU1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BC3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BC4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BC5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BC6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BC7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BC8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BC9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BC10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BC11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BC12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BC13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BC14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BC15"].value + "\n" + "\n")
        elif call.data == "RGGU2":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BN3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BN4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BN5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BN6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BN7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BN8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BN9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BN10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BN11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BN12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BN13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BN14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BN15"].value + "\n" + "\n")
        elif call.data == "RGGU3":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["AK3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["AK4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["AK5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["AK6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["AK7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["AK8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["AK9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["AK10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["AK11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["AK12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["AK13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["AK14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["AK15"].value + "\n" + "\n")
        elif call.data == "RGGU4":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["CC3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["CC4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["CC5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["CC6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["CC7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["CC8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["CC9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["CC10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["CC11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["CC12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["CC13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["CC14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["CC15"].value + "\n" + "\n")
        elif call.data == "RGGU5":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RGGU6":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RGGU7":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "MGPU1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BD3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BD4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BD5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BD6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BD7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BD8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BD9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BD10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BD11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BD12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BD13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BD14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BD15"].value + "\n" + "\n")
        elif call.data == "MGPU2":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "MGPU3":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "MGPU4":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "MGPU5":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "MGPU6":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RUDN1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BE3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BE4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BE5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BE6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BE7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BE8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BE9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BE10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BE11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BE12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BE13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BE14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BE15"].value + "\n" + "\n")
        elif call.data == "RUDN2":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BK3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BK4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BK5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BK6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BK7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BK8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BK9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BK10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BK11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BK12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BK13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BK14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BK15"].value + "\n" + "\n")
        elif call.data == "RUDN3":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RUDN4":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["AL3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["AL4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["AL5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["AL6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["AL7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["AL8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["AL9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["AL10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["AL11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["AL12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["AL13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["AL14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["AL15"].value + "\n" + "\n")
        elif call.data == "RUDN5":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RUDN6":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RUDN7":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RUDN8":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RUDN9":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RUDN10":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RUDN11":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RUDN12":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RUDN13":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RANHiGS1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BF3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BF4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BF5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BF6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BF7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BF8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BF9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BF10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BF11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BF12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BF13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BF14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BF15"].value + "\n" + "\n")
        elif call.data == "RANHiGS2":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BL3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BL4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BL5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BL6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BL7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BL8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BL9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BL10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BL11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BL12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BL13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BL14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BL15"].value + "\n" + "\n")
        elif call.data == "RANHiGS3":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RANHiGS4":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RANHiGS5":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RANHiGS6":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RGSU1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BG3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BG4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BG5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BG6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BG7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BG8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BG9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BG10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BG11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BG12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BG13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BG14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BG15"].value + "\n" + "\n")
        elif call.data == "RGSU2":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["AG3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["AG4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["AG5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["AG6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["AG7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["AG8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["AG9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["AG10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["AG11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["AG12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["AG13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["AG14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["AG15"].value + "\n" + "\n")
        elif call.data == "RGSU3":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RGSU4":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "RGSU5":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "MGU1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BH3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BH4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BH5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BH6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BH7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BH8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BH9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BH10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BH11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BH12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BH13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BH14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BH15"].value + "\n" + "\n")
        elif call.data == "MGU2":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["AE3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["AE4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["AE5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["AE6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["AE7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["AE8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["AE9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["AE10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["AE11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["AE12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["AE13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["AE14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["AE15"].value + "\n" + "\n")
        elif call.data == "MGU3":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["AI3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["AI4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["AI5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["AI6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["AI7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["AI8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["AI9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["AI10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["AI11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["AI12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["AI13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["AI14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["AI15"].value + "\n" + "\n")
        elif call.data == "MGU4":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["CD3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["CD4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["CD5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["CD6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["CD7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["CD8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["CD9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["CD10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["CD11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["CD12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["CD13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["CD14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["CD15"].value + "\n" + "\n")
        elif call.data == "MGU5":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "MGU6":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "MGU7":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "MGU8":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "MGU9":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "MGU10":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "MGU11":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Bauma1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BJ3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BJ4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BJ5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BJ6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BJ7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BJ8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BJ9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BJ10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BJ11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BJ12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BJ13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BJ14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BJ15"].value + "\n" + "\n")
        elif call.data == "Bauma2":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["CB3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["CB4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["CB5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["CB6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["CB7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["CB8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["CB9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["CB10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["CB11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["CB12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["CB13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["CB14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["CB15"].value + "\n" + "\n")
        elif call.data == "Bauma3":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "MARHI1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BU3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BU4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BU5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BU6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BU7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BU8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BU9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BU10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BU11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BU12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BU13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BU14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BU15"].value + "\n" + "\n")
        elif call.data == "Pirogova1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["AF3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["AF4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["AF5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["AF6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["AF7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["AF8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["AF9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["AF10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["AF11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["AF12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["AF13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["AF14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["AF15"].value + "\n" + "\n")
        elif call.data == "Pirogova2":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Sechenov1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["AH3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["AH4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["AH5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["AH6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["AH7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["AH8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["AH9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["AH10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["AH11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["AH12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["AH13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["AH14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["AH15"].value + "\n" + "\n")
        elif call.data == "MISIS1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["CE3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["CE4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["CE5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["CE6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["CE7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["CE8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["CE9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["CE10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["CE11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["CE12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["CE13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["CE14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["CE15"].value + "\n" + "\n")
        elif call.data == "MISIS2":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Shukina1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "VGIK1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Kosigina1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Kosigina2":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Evdokimova1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "MIREA1":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BA3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BA4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BA5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BA6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BA7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BA8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BA9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BA10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BA11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BA12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BA13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BA14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BA15"].value + "\n" + "\n")
        elif call.data == "Vshe8":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["AO3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["AO4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["AO5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["AO6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["AO7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["AO8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["AO9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["AO10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["AO11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["AO12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["AO13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["AO14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["AO15"].value + "\n" + "\n")
            bot.send_message(moder_chat, call.message.chat.id + " выбрал ВШЭ, филологический факультет.")
        elif call.data == "MGU8":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["AN3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["AN4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["AN5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["AN6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["AN7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["AN8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["AN9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["AN10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["AN11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["AN12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["AN13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["AN14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["AN15"].value + "\n" + "\n"
                             + "https://docs.google.com/forms/d/e/1FAIpQLSfrJc_PcSrrthXBVYOKNF-6c7wba5eJsdeN06WbdI0we56XlA/viewform")
            bot.send_message(moder_chat, call.message.chat.id + " выбрал МГУ, филологический факультет.")

        elif call.data == "RUDN8":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["AP3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["AP4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["AP5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["AP6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["AP7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["AP8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["AP9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["AP10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["AP11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["AP12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["AP13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["AP14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["AP15"].value + "\n" + "\n"
                             + "https://docs.google.com/forms/d/e/1FAIpQLSfrJc_PcSrrthXBVYOKNF-6c7wba5eJsdeN06WbdI0we56XlA/viewform")
            bot.send_message(moder_chat, call.message.chat.id + " выбрал РУДН, филологический факультет.")

        elif call.data == "MGU9":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["AQ3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["AQ4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["AQ5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["AQ6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["AQ7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["AQ8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["AQ9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["AQ10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["AQ11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["AQ12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["AQ13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["AQ14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["AQ15"].value + "\n" + "\n"
                             + "https://docs.google.com/forms/d/e/1FAIpQLSfrJc_PcSrrthXBVYOKNF-6c7wba5eJsdeN06WbdI0we56XlA/viewform")
            bot.send_message(moder_chat, call.message.chat.id + " выбрал МГУ, лингвистический факультет.")

        elif call.data == "Vshe9":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["AR3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["AR4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["AR5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["AR6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["AR7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["AR8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["AR9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["AR10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["AR11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["AR12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["AR13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["AR14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["AR15"].value + "\n" + "\n"
                             + "https://docs.google.com/forms/d/e/1FAIpQLSfrJc_PcSrrthXBVYOKNF-6c7wba5eJsdeN06WbdI0we56XlA/viewform")
            bot.send_message(moder_chat, call.message.chat.id + " выбрал ВШЭ, лингвистический факультет.")

        elif call.data == "Plehanova7":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["AS3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["AS4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["AS5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["AS6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["AS7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["AS8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["AS9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["AS10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["AS11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["AS12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["AS13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["AS14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["AS15"].value + "\n" + "\n"
                             + "https://docs.google.com/forms/d/e/1FAIpQLSfrJc_PcSrrthXBVYOKNF-6c7wba5eJsdeN06WbdI0we56XlA/viewform")
            bot.send_message(moder_chat, call.message.chat.id + " выбрал Плеханова, лингвистический факультет.")

        elif call.data == "RUDN9":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["AT3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["AT4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["AT5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["AT6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["AT7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["AT8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["AT9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["AT10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["AT11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["AT12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["AT13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["AT14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["AT15"].value + "\n" + "\n"
                             + "https://docs.google.com/forms/d/e/1FAIpQLSfrJc_PcSrrthXBVYOKNF-6c7wba5eJsdeN06WbdI0we56XlA/viewform")
            bot.send_message(moder_chat, call.message.chat.id + " выбрал РУДН, лингвистический факультет.")

        elif call.data == "MGU10":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BO3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BO4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BO5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BO6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BO7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BO8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BO9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BO10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BO11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BO12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BO13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BO14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BO15"].value + "\n" + "\n"
                             + "https://docs.google.com/forms/d/e/1FAIpQLSfrJc_PcSrrthXBVYOKNF-6c7wba5eJsdeN06WbdI0we56XlA/viewform")
            bot.send_message(moder_chat, call.message.chat.id + " выбрал МГУ, туристический факультет.")

        elif call.data == "RUDN10":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BP3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BP4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BP5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BP6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BP7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BP8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BP9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BP10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BP11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BP12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BP13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BP14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BP15"].value + "\n" + "\n"
                             + "https://docs.google.com/forms/d/e/1FAIpQLSfrJc_PcSrrthXBVYOKNF-6c7wba5eJsdeN06WbdI0we56XlA/viewform")
            bot.send_message(moder_chat, call.message.chat.id + " выбрал РУДН, туристический факультет.")

        elif call.data == "RANHiGS5":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BQ3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BQ4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BQ5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BQ6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BQ7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BQ8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BQ9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BQ10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BQ11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BQ12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BQ13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BQ14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BQ15"].value + "\n" + "\n"
                             + "https://docs.google.com/forms/d/e/1FAIpQLSfrJc_PcSrrthXBVYOKNF-6c7wba5eJsdeN06WbdI0we56XlA/viewform")
            bot.send_message(moder_chat, call.message.chat.id + " выбрал Ранхигс, туристический факультет.")

        elif call.data == "Plehanova8":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BR3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BR4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BR5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BR6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BR7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BR8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BR9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BR10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BR11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BR12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BR13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BR14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BR15"].value + "\n" + "\n"
                             + "https://docs.google.com/forms/d/e/1FAIpQLSfrJc_PcSrrthXBVYOKNF-6c7wba5eJsdeN06WbdI0we56XlA/viewform")
            bot.send_message(moder_chat, call.message.chat.id + " выбрал Плеханова, туристический факультет.")

        elif call.data == "RGGU6":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BS3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BS4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BS5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BS6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BS7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BS8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BS9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BS10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BS11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BS12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BS13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BS14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BS15"].value + "\n" + "\n"
                             + "https://docs.google.com/forms/d/e/1FAIpQLSfrJc_PcSrrthXBVYOKNF-6c7wba5eJsdeN06WbdI0we56XlA/viewform")
            bot.send_message(moder_chat, call.message.chat.id + " выбрал РГГУ, туристический факультет.")

        elif call.data == "RGSU5":
            bot.send_message(call.message.chat.id, "1)" + list["A3"].value + ": " + list["BT3"].value + "\n" + "\n"
                             + "2)" + list["A4"].value + ": " + list["BT4"].value + "\n" + "\n"
                             + "3)" + list["A5"].value + ": " + list["BT5"].value + "\n" + "\n"
                             + "4)" + list["A6"].value + ": " + list["BT6"].value + "\n" + "\n"
                             + "5)" + list["A7"].value + ": " + list["BT7"].value + "\n" + "\n"
                             + "6)" + list["A8"].value + ": " + list["BT8"].value + "\n" + "\n"
                             + "7)" + list["A9"].value + ": " + list["BT9"].value + "\n" + "\n"
                             + "8)" + list["A10"].value + ": " + list["BT10"].value + "\n" + "\n"
                             + "9)" + list["A11"].value + ": " + list["BT11"].value + "\n" + "\n"
                             + "10)" + list["A12"].value + ": " + list["BT12"].value + "\n" + "\n"
                             + "11)" + list["A13"].value + ": " + list["BT13"].value + "\n" + "\n"
                             + "12)" + list["A14"].value + ": " + list["BT14"].value + "\n" + "\n"
                             + "13)" + list["A15"].value + ": " + list["BT15"].value + "\n" + "\n"
                             + "https://docs.google.com/forms/d/e/1FAIpQLSfrJc_PcSrrthXBVYOKNF-6c7wba5eJsdeN06WbdI0we56XlA/viewform")
            bot.send_message(moder_chat, call.message.chat.id + " выбрал РГСУ, туристический факультет.")



bot.polling(none_stop = True, interval=0)
