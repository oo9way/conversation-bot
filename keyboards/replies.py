from telegram import ReplyKeyboardMarkup, KeyboardButton


def get_contact():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(text="Telefon raqamni yuborish", request_contact=True)]
        ], resize_keyboard=True
    )


def get_location():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(text="Manzilni yuborish", request_location=True)]
        ], resize_keyboard=True
    )