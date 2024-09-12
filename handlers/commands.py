from telegram import Update
from telegram.ext import CallbackContext
import states


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Assalamu alaykum\nBotimizga xush kelibsiz!")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("Siz yordam sahifasidasiz.\nBotdan ro'yxatdan o'tish uchun /register buyrug'ini yuboring")


def contact(update: Update, context: CallbackContext):
    update.message.reply_text("Murojaat uchun:\n\n+156648488848")


def register(update: Update, context: CallbackContext):
    update.message.reply_text("Ro'yxatdan o'tish uchun to'liq ismingizni kiriting")
    return states.FULLNAME