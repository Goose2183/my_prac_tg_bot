from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from misc.fms import AdminStates
from aiogram.types import Message
from keyboards.inline_kb import mailing_btn
from misc import text


message_router = Router()

@message_router.message(F.from_user.id == 7552379546, AdminStates.admin_mailing_msg)
async def mailing_copy_msg(msg: Message, state: FSMContext):
    await msg.copy_to(msg.from_user.id, reply_markup=msg.reply_markup)
    if msg.photo:
        await state.update_data(admin_mailing_msg =
                                {"msg_text":msg.text,
                                 "msg_caption":msg.caption,
                                 "msg_reply_markup":msg.reply_markup,
                                 "msg_photo":msg.photo[-1].file_id})
    else:
        await state.update_data(admin_mailing_msg=
                          {"msg_text": msg.text,
                           "msg_reply_markup":msg.reply_markup,})
    await msg.answer(text=text.mailing_accept, reply_markup=mailing_btn())
    await state.set_state(AdminStates.admin_mailing_accept)
