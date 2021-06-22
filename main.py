from aiogram import Bot, Dispatcher, types, executor
from asyncio import sleep

bot  = Bot("1861694539:AAGDU8jmX9lwVv8USWKTA9fj5FHjIMlzHXM")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.from_user.id, f"Привет, {message.from_user.username}! Начинаем игру")
    await sleep(1)
    await bot.send_message(message.from_user.id, "Этот мне")
    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data['dice']['value']
    await sleep(5)
    await bot.send_message(message.from_user.id, f"Мне выпало: {bot_data}")
    await sleep(1)
    await bot.send_message(message.from_user.id, "Этот тебе")
    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data['dice']['value']
    await sleep(5)
    await bot.send_message(message.from_user.id, f"Тебе выпало: {user_data}")


    if bot_data < user_data:
        await bot.send_message(message.from_user.id, "Ты победил!")
    elif bot_data > user_data:
        await bot.send_message(message.from_user.id, "Ты проиграл!")
    else:
        await bot.send_message(message.from_user.id, "Ничья!")

# @dp.message_handler()
# async def echo(message: types.Message):
#    await message.answer(message.text)

@dp.message_handler()
async def filter_message(message):
    if "Денис" in message.text:
        await message.delete()
    else:
        await message.answer(message.text)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
