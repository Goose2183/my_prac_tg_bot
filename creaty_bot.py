from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage


TOKEN = config("TOKEN")
redis_url = config("REDIS_URL")
ADMINS = config("ADMINS")
WEB_SERVER_HOST = config("WEB_SERVER_HOST")
WEB_SERVER_URL = config("WEB_SERVER_URL")
PORT = int(config("PORT"))
WEBHOOK_PATH = "/webhook"
storage = RedisStorage.from_url(redis_url)


bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=storage)