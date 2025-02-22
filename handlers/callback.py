import aiogram.exceptions
from aiogram import Router, F
from aiogram.types import CallbackQuery
from misc import text
from keyboards.inline_kb import my_ps_link, back_btn, admin_kb, main_kb
from misc.fms import UserStates, AdminStates
from aiogram.fsm.context import FSMContext
from db import get_statistic, get_id_from_db, edit_user

callback_router = Router()


@callback_router.callback_query(F.data == 'order')
async def place_order(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(
        text.bot_info_text,
        reply_markup=my_ps_link())
    await state.set_state(UserStates.order_state)


@callback_router.callback_query(F.data == 'bot_info')
async def bot_information(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(
        text.bot_info_text,
        reply_markup=back_btn())
    await state.set_state(UserStates.bot_info_state)


@callback_router.callback_query(F.data == 'back')
async def back(call: CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if (current_state == UserStates.order_state or
        current_state == UserStates.bot_info_state or
        current_state == UserStates.price_list_state or
        current_state == AdminStates.admin_menu_state):
        await call.message.edit_text(text.start_msg.format(call.from_user.full_name, call.from_user.id),
                            reply_markup=main_kb(call.from_user.id))
        await state.set_state(UserStates.main_menu_state)
    elif(current_state == AdminStates.mailing_state or
        current_state == AdminStates.statistic_state):
        await admin_panel(call, state)


@callback_router.callback_query(F.data == 'mailing')
async def mailing(call: CallbackQuery, state: FSMContext):
    await call.message.answer(text.mailing_text,
                                 reply_markup=back_btn())
    await state.set_state(AdminStates.admin_mailing_msg)


@callback_router.callback_query(F.data == 'users_statistic')
async def statistic(call: CallbackQuery, state: FSMContext):
    users_statistic = await get_statistic()
    await call.message.edit_text(text.statistic_text.format(users_statistic[0],
                                                            users_statistic[1],
                                                            users_statistic[2]),
                                 reply_markup=back_btn())
    await state.set_state(AdminStates.statistic_state)


@callback_router.callback_query((F.data == "admin_panel") | (F.data == "cancel"))
async def admin_panel(call: CallbackQuery, state: FSMContext):
    from creaty_bot import ADMINS
    if call.from_user.id == int(ADMINS):
        await call.message.edit_text(text.admin_text.format(call.from_user.full_name),
                                     reply_markup=admin_kb())
        await state.set_state(AdminStates.admin_menu_state)


@callback_router.callback_query(F.data == "price_list")
async def price_lst(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(text.price_text,
                                 reply_markup=back_btn())
    await state.set_state(UserStates.price_list_state)


@callback_router.callback_query(F.data == "accept")
async def mailing_accept(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg_info = data.get("admin_mailing_msg")
    users_id = await get_id_from_db.get_users_id()
    banned_users = 0
    unbanned_users = 0
    for user_id in users_id:
        try:
            if msg_info["msg_text"] == None:
                await call.bot.send_photo(caption=msg_info["msg_caption"],
                                            photo=msg_info["msg_photo"],
                                            reply_markup=msg_info["msg_reply_markup"],
                                            chat_id=user_id)
            else:
                await call.bot.send_message(text=msg_info["msg_text"],
                                            reply_markup=msg_info["msg_reply_markup"],
                                            chat_id=user_id)
            await edit_user.unbanned_user(user_id)
            unbanned_users += 1
        except aiogram.exceptions.TelegramForbiddenError:
            await edit_user.banned_user(user_id)
            banned_users += 1
    await call.message.answer(text=text.mailing_send_accept_text.format(unbanned_users, banned_users))







