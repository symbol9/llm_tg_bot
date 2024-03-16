from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup)


def filled_form_kb():
    ai_button = KeyboardButton(text='QA_BTN🤖')
    keyboard = ReplyKeyboardMarkup(keyboard=[[ai_button]],
                                   resize_keyboard=True)
    return keyboard
