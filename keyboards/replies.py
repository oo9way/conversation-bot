from telegram import ReplyKeyboardMarkup, KeyboardButton
from translation import get_translation as _

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


def get_main(lang):
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(_("books", lang)), KeyboardButton(_("audio_books", lang),) ],
            [KeyboardButton(_("cart", lang)), KeyboardButton(_("language", lang),) ],
        ], resize_keyboard=True
    )


def get_finish_order():
    return ReplyKeyboardMarkup(
        [
            [
                KeyboardButton("Buyurtmani yakunlash"), KeyboardButton("Savatni tozalash")
            ]
        ]
    )