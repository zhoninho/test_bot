from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from config import staff, bot

class OrderFSM(StatesGroup):
    product_id = State()
    size = State()
    quantity = State()
    contact = State()
    submit = State()


async def start_fsm_order(message: types.Message):
    await OrderFSM.product_id.set()
    await message.answer("Введите артикул товара: ")


async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await OrderFSM.next()
    await message.answer("Введите размер товара: ")


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await OrderFSM.next()
    await message.answer("Введите кол-во товара: ")


async def load_quantity(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text

    await OrderFSM.next()
    await message.answer("Введите свои контактные данные (номер телефона): ")


async def load_contact(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact'] = message.text

    await OrderFSM.next()
    await message.answer("Верны ли данные ?: ")
    await message.answer(f'Артикул - {data["product_id"]}\n'          
                         f'Размер - {data["size"]}\n'
                         f'Кол-во - {data["quantity"]}\n'
                         f'Кон-е данные (тел.) - {data["contact"]}')

async def submit_load(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        async with state.proxy() as data:
            for admin in staff:
                await bot.send_message(chat_id=admin, text=f'Артикул - {data["product_id"]}\n'          
                                                           f'Размер - {data["size"]}\n'
                                                           f'Кол-во - {data["quantity"]}\n'
                                                           f'Кон-е данные (тел.) - {data["contact"]}')

            await state.finish()

    elif message.text.lower() == 'нет':
        await message.answer('Хорошо, отменено!')

    else:
        await message.answer('Выберите да или нет')

async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm,
                                Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(start_fsm_order, commands=['order'])
    dp.register_message_handler(load_product_id, state=OrderFSM.product_id)
    dp.register_message_handler(load_size, state=OrderFSM.size)
    dp.register_message_handler(load_quantity, state=OrderFSM.quantity)
    dp.register_message_handler(load_contact, state=OrderFSM.contact)
    dp.register_message_handler(submit_load, state=OrderFSM.submit)