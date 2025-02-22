from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from misc import text
import pytz
from datetime import datetime
from db import add_user
from keyboards.inline_kb import main_kb
from misc.fms import UserStates
from aiogram.fsm.context import FSMContext

start_router = Router()


@start_router.message(Command('start'))
async def cmd_start(msg: Message, state: FSMContext):
    moscow_tz = pytz.timezone("Europe/Moscow")
    user_id = msg.from_user.id
    user_fullname = msg.from_user.full_name
    user_shortname = msg.from_user.username
    user_status = 'subscribed'
    user_sub_date = datetime.now(moscow_tz).strftime("%Y:%m:%d:%H:%M")
    await msg.answer(text.start_msg.format(user_fullname, user_id),
                     reply_markup=main_kb(msg.from_user.id))
    await add_user(user_id, user_fullname, user_shortname, user_status, user_sub_date)
    await state.set_state(UserStates.main_menu_state)


async def cmd_start_edit(msg:Message, state: FSMContext):
    await msg.edit_text(text.start_msg.format(msg.from_user.full_name, msg.from_user.id),
                                    reply_markup=main_kb(msg.from_user.id))
    await state.set_state(UserStates.main_menu_state)
