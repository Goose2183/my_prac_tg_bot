from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    order_state = State()
    bot_info_state = State()
    main_menu_state = State()
    price_list_state = State()


class AdminStates(StatesGroup):
    mailing_state = State()
    statistic_state = State()
    admin_menu_state = State()
    admin_mailing_msg = State()
    admin_mailing_accept = State()

