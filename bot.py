from aiogram import Bot, types, Dispatcher, executor
import db_map as jojo



from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands="special1")
async def cmd_special_buttons(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Запросить геолокацию", request_location=True))
    keyboard.add(types.KeyboardButton(text="Запросить контакт", request_contact=True))
    keyboard.add(types.KeyboardButton(text="Создать викторину",
    request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
    await message.answer("Выберите действие:", reply_markup=keyboard)


@dp.message_handler(commands="jojo")
async def cmd_start(message: types.Message):
    await message.answer('1231414244')
    await message.answer("Начинаем", reply_markup=jojo.hto_i)


@dp.message_handler(lambda message:message.text in jojo.button_main1)
async def cmd_start_1(message: types.Message):
    await message.answer('aaa',reply_markup=jojo.key)


@dp.message_handler(lambda message:message.text in jojo.button)
async def cmd_start1(message: types.Message):
    await message.answer('11111')
    await message.answer('1234', reply_markup = jojo.butt)






































@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)