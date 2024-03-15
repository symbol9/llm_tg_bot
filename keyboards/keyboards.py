from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup)


def filled_form_kb():
    ai_button = KeyboardButton(text='Вент-нейросеть🤖')
    keyboard = ReplyKeyboardMarkup(keyboard=[[ai_button]],
                                   resize_keyboard=True)
    return keyboard
