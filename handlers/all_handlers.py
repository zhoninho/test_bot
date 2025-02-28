from aiogram import Dispatcher, types
from db import main_db

async def start_handler(message: types.Message):
    user = message.from_user
    await message.answer(f"Привет, {user.first_name}! id: {user.id}")

async def info_handler(message: types.Message):
    await message.answer(
        f"Этот бот нужен для заказа товаров из магазина\n"
    )

async def send_products(message: types.Message):
    products = main_db.fetch_all_products()
    if products:
        for product in products:

            caption = (f'Название товара - {product["name_product"]}\n'
                       f'Категория - {product["category"]}\n'
                       f'Размер - {product["size"]}\n'
                       f'Цена - {product["price"]}\n'
                       f'Артикул - {product["product_id"]}')

            await message.answer_photo(photo=product["photo"],
                                            caption=caption)

    else:
        await message.answer('База пуста! Товаров нет.')

async def other_handler(message: types.Message):
    await message.answer("Я вас не понимаю.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(send_products, commands=['send_products'])
    dp.register_message_handler(other_handler)