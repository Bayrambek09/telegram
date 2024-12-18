import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery,callback_query
from config import BOT_TOKEN as token
from button import *

bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(Command('start'))
async def StartCommand(message: Message):
    await message.answer_photo(
        photo='https://olcha.uz/image/668x380/category_slider/cdn_1/2024-07-02/n2HGhNFwVw9SAIPkUaGCR9FfTeHICgCrzbhZoqa0zXWjMJfWUjXhH3xFdGUy.jpg',
        caption='MaishiyTexnika', reply_markup=menu)


@dp.callback_query(F.data == 'maishiy')
async def shop2(call: CallbackQuery):
    await call.message.answer_photo(photo='https://frankfurt.apollo.olxcdn.com/v1/files/n67dozhmk8sb1-UZ/image;s=1200x1200',caption='lkjhgfd',reply_markup=maishiy1)
    await call.message.delete()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

