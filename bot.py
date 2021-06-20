
import telebot
import parser
from telebot import types
import os, re


TOKEN = "1739015805:AAHOsXUcs28aK8VHJ10SSH-CWDPw6RHeneQ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def inline(message):
    bot.send_message(message.chat.id, "Ваши инвестиции💰 – это не рынки и доходность. Речь идет о Вас и Вашей семье. "
                                      "Инвестиции – это достижение Ваших целей, забота о Ваших близких и обеспечение "
                                      "комфортного для Вас уровня жизни. Выбирайте нужную ВАМ инвестиционную платформу "
                                      "или пишите @FilimonovIE для консультации и начинайте делать первые шаги уже сегодня!!!💸")
    bot.send_message(message.chat.id, "РОЙ Клуб😎- Современная площадка для инвестиций до 40%!!!\n" 
                                        "Приумножайте криптовалюту для "
                                        "вас и вашей семьи 24/7\n"
                                        "Пассивный рост криптовалют до 40% в месяц!!!💰💰💰"
                                        "\n @testcomp21bot")
    bot.send_message(message.chat.id, "TO THE MARS🚀🚀🚀 — это платформа, позволяющая зарабатывать на инвестировании"
                                        " от 96% годовых с возможностью реинвестирования 😱👍"
                                        "\n @testcomp22bot")

@bot.message_handler(commands=["start1"])
def inline(message):
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="NumberOne", callback_data="NumberOne")
    but_2 = types.InlineKeyboardButton(text="NumberTwo", callback_data="NumberTwo")
    but_3 = types.InlineKeyboardButton(text="NumberTree", callback_data="NumberTree")
    but_4 = types.InlineKeyboardButton(text="Number4", callback_data="Number4")
    key.add(but_1, but_2, but_3, but_4)
    bot.send_message(message.chat.id, "ВЫБЕРИТЕ КНОПКУ", reply_markup=key)

@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    if c.data == 'NumberOne':
        bot.send_message(c.message.chat.id, '')
    if c.data == 'NumberTwo':
        bot.send_message(c.message.chat.id, 'Это кнопка 2')
    if c.data == 'NumberTree':
        bot.send_message(c.message.chat.id, 'Это кнопка 3')
    if c.data == 'Number4':
        bot.send_message(c.message.chat.id, 'Это кнопка 4')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'список команд')
    elif text == "как дела?":
        bot.send_message(chat_id, 'Хорошо, а у тебя?')
    elif text == "как дела?":
        bot.send_message(chat_id, 'Хорошо, а у тебя?')
    elif text == "как дела?":
        bot.send_message(chat_id, 'Хорошо, а у тебя?')
    elif text == "как дела?":
        bot.send_message(chat_id, 'Хорошо, а у тебя?')
    else:
        bot.send_message(chat_id, 'Простите, я вам не понял, пропробуйте нажать /start')

bot.polling()