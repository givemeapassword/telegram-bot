from aiogram.types import ReplyKeyboardMarkup


btnInfo = ['аниме']
main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add(*btnInfo)



butt = ReplyKeyboardMarkup(resize_keyboard=True)
button_main = ['Тест на профорентацию','Направления подготовки',
'Вступительные испытания','Поступление','Об институте','Задать вопрос']
butt.add(*button_main)

hto_i = ReplyKeyboardMarkup(resize_keyboard=True)
button_main1 = ['абитуриент','студент','преподаватель']
hto_i.add(*button_main1)


key = ReplyKeyboardMarkup(resize_keyboard=True)
button=['Русский','English','Espanol']
key.add(*button)