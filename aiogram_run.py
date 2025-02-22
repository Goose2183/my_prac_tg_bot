import logging
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from creaty_bot import bot, dp, WEBHOOK_PATH, WEB_SERVER_URL, PORT, ADMINS, WEB_SERVER_HOST
from handlers.message import message_router
from handlers.start import start_router
from handlers.callback import callback_router
from db.create_database import create_db

async def on_startup() -> None:
    await bot.set_webhook(f"{WEB_SERVER_URL}{WEBHOOK_PATH}")
    await bot.send_message(chat_id=ADMINS, text="Бот запущен!")

async def on_shutdown() -> None:
    await bot.send_message(chat_id=ADMINS, text='Бот остановлен!')
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.session.close()

async def main():
    dp.include_routers(start_router, callback_router, message_router)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot
    )
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    web.run_app(app, host=WEB_SERVER_HOST, port=PORT)

if __name__ == "__main__":
    create_db()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    main()