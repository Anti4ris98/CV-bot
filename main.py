import telebot
import webbrowser

bot = telebot.TeleBot('6896862671:AAE9GWFSnReoGNHF5Q0cvi03iPDRjqNWvM4')

@bot.message_handler(commands=['start'])
def main(message):
    if message.from_user.language_code == 'uk':
        bot.send_message(message.chat.id, f"Доброго дня {message.from_user.first_name}{message.from_user.last_name}, Мене звати Ілля. То з чого почнемо знайомство? Напишіть слово <b>Допомога</b> і я розкажу що я могу вам розказати", parse_mode='html')
    elif message.from_user.language_code == 'en':
        bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}{message.from_user.last_name}, my name is Illia Lobachov, let`s start our acquaintance. Just write <b>Assistance</b> and I will describe you what I can what can I tell about myself", parse_mode='html')


@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id, message)
    
@bot.message_handler(commands=['git'])
def site(message):
    webbrowser.open('https://github.com/Anti4ris98')

@bot.message_handler(commands=['linkedin'])
def site(message):
    webbrowser.open('https://www.linkedin.com/in/ilya-lobachov-927873188/')

@bot.message_handler(commands=['storage'])
def site(message):
    webbrowser.open('https://drive.google.com/drive/u/0/folders/1e7p3FlCashIPPDcno7_iMhC-huw7ogFL?q=sharedwith:public%20parent:1e7p3FlCashIPPDcno7_iMhC-huw7ogFL')

@bot.message_handler()
def help(message):
    if message.text.lower() == 'допомога':
        bot.send_message(message.chat.id, '<b>За допомогою цих фраз я...</b>', parse_mode='html')
        bot.send_message(message.chat.id, '<em>/summary</em> - розповім що вмію', parse_mode='html')
        bot.send_message(message.chat.id, '<em>/academic</em> - розповім де вчився', parse_mode='html')
        bot.send_message(message.chat.id, '<em>/expirience</em> - розповім свою професійну історію', parse_mode='html')
        bot.send_message(message.chat.id, '<em>/contact</em> - як зі мною звязатись', parse_mode='html')
        bot.send_message(message.chat.id, '<em>/export</em> - вишлю ці данні вам на пошту', parse_mode='html')
    elif message.text.lower() == 'assistance':
        bot.send_message(message.chat.id, '<b>By using this comands I will ...</b>', parse_mode='html')
        bot.send_message(message.chat.id, '<em>/summary</em> - describe my abbilities', parse_mode='html')
        bot.send_message(message.chat.id, '<em>/academic</em> - tell about my academic history', parse_mode='html')
        bot.send_message(message.chat.id, '<em>/expirience</em> - tell you my сareer пrowth', parse_mode='html')
        bot.send_message(message.chat.id, '<em>/contact</em> - how to contack with me', parse_mode='html')
        bot.send_message(message.chat.id, '<em>/export</em> - send CV by email', parse_mode='html')
                 





bot.polling(non_stop=True)