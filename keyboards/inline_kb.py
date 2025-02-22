from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from creaty_bot import ADMINS


def my_ps_link():
    kb_link = [
        [InlineKeyboardButton(text='Моя личка', url='t.me/Tond1x')],
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb_link)


def admin_kb():
    admin_kb_list = [
        [InlineKeyboardButton(text='Рассылка', callback_data='mailing'),
         InlineKeyboardButton(text='Статистика', callback_data='users_statistic')],
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=admin_kb_list)

def main_kb(user_id):
    main_kb_list = [
        [InlineKeyboardButton(text='Оформить заказ✅', callback_data='order')],
        [InlineKeyboardButton(text='О боте❓',callback_data='bot_info'),
         InlineKeyboardButton(text='Прайс лист', callback_data='price_list')]
    ]
    if user_id == int(ADMINS):
        main_kb_list.append([InlineKeyboardButton(text="Админ панель", callback_data='admin_panel')])
    return InlineKeyboardMarkup(inline_keyboard=main_kb_list)


def back_btn():
    back_btn_list = [
        [InlineKeyboardButton(text="Назад⬅️", callback_data='back')]
    ]

    return InlineKeyboardMarkup(inline_keyboard=back_btn_list)
def mailing_btn():
    mailing_cancel_btn = [
        [InlineKeyboardButton(text="Нет", callback_data="cancel"),
         InlineKeyboardButton(text="Да", callback_data="accept")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=mailing_cancel_btn)
