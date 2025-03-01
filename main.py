from aiogram import executor
from config import dp, bot, staff
from handlers import all_handlers, store_fsm, order_fsm
from database import create_tables

async def on_startup(_):
    for admin in staff:
        await bot.send_message(chat_id=admin, text="Bot activated!")

    await create_tables()

store_fsm.register_handlers(dp)
order_fsm.register_handlers(dp)
all_handlers.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)