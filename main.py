import logging
import time

from aiogram import Bot, Dispatcher, executor, types
from decouple import config


API_TOKEN = config('API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# g_keyboard = types.ReplyKeyboardMarkup()
# button1 =  types.KeyboardButton('HELLO')
# button2 =  types.KeyboardButton('BUY MY GOLD')
# # g_keyboard.add(button1)
# g_keyboard.add(button1, button2)

# g_keyboard = types.ReplyKeyboardMarkup(
#     [[types.KeyboardButton('1️⃣'),types.KeyboardButton('2️⃣'),types.KeyboardButton('3️⃣')],
#      [types.KeyboardButton('MIDDLE🤔')],
#      [types.KeyboardButton('BUY MY GOLD'),types.KeyboardButton('BUY MY GOLD'),types.KeyboardButton('BUY MY GOLD')]],
#     resize_keyboard= True, row_width=1
# )

# g_keyboard = types.ReplyKeyboardMarkup(
#     resize_keyboard= False, row_width=2
# )

# for el in range(10):
#     g_keyboard.add(types.KeyboardButton('key_'+ str(el)))


g_inline_keyboard = types.InlineKeyboardMarkup()
g_inline_keyboard.add(types.InlineKeyboardButton('button1',callback_data='LOL'))

scratch_url = 'https://scratch.mit.edu/projects/142394929'
back_inline = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('HMM GO BACK', callback_data='mainMenu'))
back_inline.add(types.InlineKeyboardButton('LINK to Scratch', url=scratch_url))




@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.",reply_markup=g_inline_keyboard)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text in '1️⃣2️⃣3️⃣':
        await message.reply("ONE TWO THREE!❌😄", reply_markup=types.ReplyKeyboardRemove())
    await message.answer(message.text)

@dp.callback_query_handler()
async def inline_butttonsss(query: types.CallbackQuery):
    print(query)
    # time.sleep(2)
    if query.data == 'LOL':
        await query.message.edit_text("ITS so works",reply_markup=back_inline)
    elif query.data == 'mainMenu':
        await query.message.edit_text("ITS A MAIN MENU MAN!", reply_markup=g_inline_keyboard) 
    



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


