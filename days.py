import telebot
import config 

from telebot import types

bot = telebot.TeleBot("991306073:AAGrj0lh9lCHt_zU95yMZ60KVK9eN7CcquY")

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('D:/Telegram/static/welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

#keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("1 Курс 🐣")
	item2 = types.KeyboardButton("2 Курс 🐥")
	item3 = types.KeyboardButton("3 Курс 🦆")
	item4 = types.KeyboardButton("4 Курс 🦅")
	
	markup.add(item1, item2, item3, item4 )
	

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный, чтобы показывать тебе расписание на неделю.".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup )

@bot.message_handler(content_types=["text"])
def lalala(message):
	if message.chat.type == "private":
		if message.text == "3 Курс 🦆":

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton(" Я арабист", callback_data="first")
			item2 = types.InlineKeyboardButton(" Я китаист ", callback_data="second")
			item3 = types.InlineKeyboardButton(" Я японист ", callback_data="third")
			item4 = types.InlineKeyboardButton(" Я кореевед ", callback_data="fourth")
			item5 = types.InlineKeyboardButton(" Я безвосточник 🌈 ", callback_data="fifth")
			item6 = types.InlineKeyboardButton(" Я индонезиец", callback_data="sixth")

			markup.add(item1, item2, item3, item4, item5, item6)

			bot.send_message(message.chat.id, "На каком ты направлении?", reply_markup=markup)
		else:
			bot.send_message(message.chat.id, "Я не знаю, что ответить 😥 ")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:		
		if call.message:
			if call.data == "first":
				markup = types.InlineKeyboardMarkup(row_width=2)
				item1 = types.InlineKeyboardButton(" Понедельник ", callback_data="Monday")
				item2 = types.InlineKeyboardButton(" Вторник ", callback_data="Tuesday")
				item3 = types.InlineKeyboardButton(" Среда ", callback_data="Wednesday")
				item4 = types.InlineKeyboardButton(" Четверг ", callback_data="Thursday")
				item5 = types.InlineKeyboardButton(" Пятница ", callback_data="Friday")

				markup.add(item1, item2, item3, item4, item5)

				bot.send_message(call.message.chat.id, " Выбери день недели ", reply_markup=markup)


			if call.message:
				if call.data == "Monday":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Даосизм \n 11:10-12:40 Теория международных отношений \n 13:10-14:40 Арабский язык \n 14:50-16:20 Арабский язык")
				if call.data == "Tuesday":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Английский язык 🥇Группа🥇 \n 11:10-12:40 Экономика и политика Арабских стран \n 13:10-14:40 Межкультурные коммуникации \n 14:50-16:20 Английский язык")
				if call.data == "Wednesday":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Арабский язык \n 11:10-12:40 Курльтура Арабских стран \n 13:10-14:40 Арабский язык \n 14:50-16:20 Гос. право региона специализации \n 16:30-18:00 Гос. право региона специализации")
				if call.data == "Thursday":
					bot.send_message(call.message.chat.id, " 11:10-12:40 Английский язык")
				if call.data == "Friday":
					bot.send_message(call.message.chat.id, " 11:10-12:40 Арабский язык \n 13:10-14:40 Арабский язык")


			if call.data == "second":
				markup = types.InlineKeyboardMarkup(row_width=2)
				item1 = types.InlineKeyboardButton(" Понедельник ", callback_data="Monday1")
				item2 = types.InlineKeyboardButton(" Вторник ", callback_data="Tuesday1")
				item3 = types.InlineKeyboardButton(" Среда ", callback_data="Wednesday1")
				item4 = types.InlineKeyboardButton(" Четверг ", callback_data="Thursday1")
				item5 = types.InlineKeyboardButton(" Пятница ", callback_data="Friday1")

				markup.add(item1, item2, item3, item4, item5)

				bot.send_message(call.message.chat.id, " Выбери день недели ", reply_markup=markup)

			if call.message:	
				if call.data == "Monday1":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Даосизм \n 11:10-12:40 Теория международных отношений \n 13:10-14:40 Китайский язык")
				if call.data == "Tuesday1":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Английский язык 🥇1 Группа🥇 \n 11:00-12:40 Экономика и политика Арабских стран \n 13:10-14:40 Межкультурные коммуникации \n 14:50-16:20 Английский язык")
				if call.data == "Wednesday1":
					bot.send_message(call.message.chat.id, " 11:10-12:40 Китайский язык \n 13:10-14:40 Китайский язык \n 14:50-16:20 Гос. право региона специализации \n 16:30-18:00 Гос. право региона специализации")
				if call.data == "Thursaday1":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Основы международной безопасности (МО) \n 11:00-12:40 Английский язык")
				if call.data == "Friday1":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Культура Китая \n 11:10-12:40 Китайский язык \n 13:10-14:40 Китайский язык \n 14:50-16:20 Китайский язык")

			if call.data == "third":
				markup = types.InlineKeyboardMarkup(row_width=2)
				item1 = types.InlineKeyboardButton(" Понедельник ", callback_data="Monday2")
				item2 = types.InlineKeyboardButton(" Вторник ", callback_data="Tuesday2")
				item3 = types.InlineKeyboardButton(" Среда ", callback_data="Wednesday2")
				item4 = types.InlineKeyboardButton(" Четверг ", callback_data="Thursday2")
				item5 = types.InlineKeyboardButton(" Пятница ", callback_data="Friday2")

				markup.add(item1, item2, item3, item4, item5)

				bot.send_message(call.message.chat.id, " Выбери день недели ", reply_markup=markup)

			if call.message:
				if call.data == "Monday2":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Даосизм \n 11:10-12:40 Теория международных отношений \n 13:10-14:40 Японский язык \n 14:50-16:20 Японский язык 🥇1 Группа🥇")
				if call.data == "Tuesday2":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Английский язык 🥇Группа🥇 \n 11:10-12:40 Экономика и политика Арабских стран \n 13:10-14:40 Межкультурные коммуникации \n 14:50-16:20 Английский язык")
				if call.data == "Wednesday2":
					bot.send_message(call.message.chat.id, " 11:10-12:40 Японский язык \n 13:10-14:40 Японский язык \n 14:50-16:20 Гос. право региона специализации \n 16:30-18:00 Гос. право региона специализации")
				if call.data == "Thursday2":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Основы международной безопасности (МО) \n 11:00-12:40 Английский язык \n 13:10-14:40 Японский язык \n 14:50-16:20 Японский язык")
				if call.data == "Friday2":
					bot.send_message(call.message.chat.id, " 11:10-12:40 Японский язык (2 группа) \n 13:10-14:40 Японский язык (2 группа) \n 14:50-16:20 Японский язык (1 группа) \n 16:30-18:00 Японский язык (1 группа)")




			if call.data == "fourth":
				markup = types.InlineKeyboardMarkup(row_width=2)
				item1 = types.InlineKeyboardButton(" Понедельник ", callback_data="Monday3")
				item2 = types.InlineKeyboardButton(" Вторник ", callback_data="Tuesday3")
				item3 = types.InlineKeyboardButton(" Среда ", callback_data="Wednesday3")
				item4 = types.InlineKeyboardButton(" Четверг ", callback_data="Thursday3")
				item5 = types.InlineKeyboardButton(" Пятница ", callback_data="Friday3")

				markup.add(item1, item2, item3, item4, item5)

				bot.send_message(call.message.chat.id, " Выбери день недели ", reply_markup=markup)

			if call.message:
				if call.data == "Monday3":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Даосизм \n 11:10-12:40 Теория международных отношений \n 13:10-14:40 Культура Кореи")
				if call.data == "Tuesday3":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Английский язык 🥇Группа🥇 \n 11:10-12:40 Экономика и политика Арабских стран \n 13:10-14:40 Межкультурные коммуникации \n 14:50-16:20 Английский язык \n 16:30-18:00 Корейский язык")
				if call.data == "Wednesday3":
					bot.send_message(call.message.chat.id, " 14:50-16:20 Гос. право региона специализации \n 16:30-18:00 Гос. право региона специализации")
				if call.data == "Thursday3":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Основы международной безопасности (МО) \n 11:00-12:40 Английский язык \n 13:10-14:40 Корейский язык \n 14:50-16:20 Корейский язык")
				if call.data == "Friday3":
					bot.send_message(call.message.chat.id, " 11:00-12:40 Корейский язык \n 13:10-14:40 Корейский язык")


			if call.data == "fifth":
				markup = types.InlineKeyboardMarkup(row_width=2)
				item1 = types.InlineKeyboardButton(" Понедельник ", callback_data="Monday4")
				item2 = types.InlineKeyboardButton(" Вторник ", callback_data="Tuesday4")
				item3 = types.InlineKeyboardButton(" Среда ", callback_data="Wednesday4")
				item4 = types.InlineKeyboardButton(" Четверг ", callback_data="Thursday4")
				item5 = types.InlineKeyboardButton(" Пятница ", callback_data="Friday4")

				markup.add(item1, item2, item3, item4, item5)

				bot.send_message(call.message.chat.id, " Выбери день недели ", reply_markup=markup)

			if call.message:
				if call.data == "Monday4":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Даосизм \n 11:10-12:40 Теория международных отношений \n 13:10-14:40 Английский язык \n 14:50-16:20 Английский язык")
				if call.data == "Tuesday4":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Английский язык 🥇Группа🥇 \n 11:10-12:40 Экономика и политика Арабских стран \n 13:10-14:40 Межкультурные коммуникации \n 14:50-16:20 Английский язык")
				if call.data == "Wednesday4":
					bot.send_message(call.message.chat.id, " 11:10-12:40 Экономика Австралии и Океании \n 13:10-14:40 Экономика Австралии и Океании \n 14:50-16:20 Гос. право региона специализации \n 16:30-18:00 Гос. право региона специализации")
				if call.data == "Thursday4":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Основы международной безопасности (МО) \n 11:00-12:40 Английский язык")
				if call.data == "Friday4":
					bot.send_message(call.message.chat.id, " 11:00-12:40 Испанский язык \n 13:10-14:40 Испанский язык")


			if call.data == "sixth":
				markup = types.InlineKeyboardMarkup(row_width=2)
				item1 = types.InlineKeyboardButton(" Понедельник ", callback_data="Monday5")
				item2 = types.InlineKeyboardButton(" Вторник ", callback_data="Tuesday5")
				item3 = types.InlineKeyboardButton(" Среда ", callback_data="Wednesday5")
				item4 = types.InlineKeyboardButton(" Четверг ", callback_data="Thursday5")
				item5 = types.InlineKeyboardButton(" Пятница ", callback_data="Friday5")

				markup.add(item1, item2, item3, item4, item5)

				bot.send_message(call.message.chat.id, " Выбери день недели ", reply_markup=markup)

			if call.message:
				if call.data == "Monday5":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Даосизм \n 11:10-12:40 Теория международных отношений \n 13:10-14:40 Индонезийский язык \n 14:50-16:20 Индонезийский язык")
				if call.data == "Tuesday5":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Английский язык 🥇Группа🥇 \n 11:10-12:40 Экономика и политика Арабских стран \n 13:10-14:40 Межкультурные коммуникации \n 14:50-16:20 Английский язык")
				if call.data == "Wednesday5":
					bot.send_message(call.message.chat.id, "  11:10-12:40 Индонезийский язык \n 13:10-14:40 Индонезийский язык \n 14:50-16:20 Гос. право региона специализации \n 16:30-18:00 Гос. право региона специализации")
				if call.data == "Thursday5":
					bot.send_message(call.message.chat.id, " 9:30-11:00 Основы международной безопасности (МО) \n 11:00-12:40 Английский язык")
				if call.data == "Friday5":
					bot.send_message(call.message.chat.id, " 11:00-12:40 Индонезийский язык \n 13:10-14:40 Индонезийский язык")










			
			#Remove inline buttons 
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" 3 Курс 🦆 ",
				reply_markup=None)
			#show alert 
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
				text =" Вот твоё расписание!")

	except Exception as e:
		print(repr(e))



#RUN
bot.polling(none_stop=True)