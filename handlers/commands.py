from telegram import Update, Poll
from telegram.ext import CallbackContext
from keyboards import inlines, replies
from translation import get_translation as _
import db


def start(update: Update, context: CallbackContext):
    language = context.user_data.get("language", None)
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    telegram_id = update.message.from_user.id

    db.create_user(telegram_id, first_name, last_name)

    if not language:
        context.user_data["language"] = "uz"
    update.message.reply_text(_("bot_salom", language), reply_markup=replies.get_main(language))


def help(update: Update, context: CallbackContext):
    update.message.reply_text("Siz yordam sahifasidasiz.\nBotdan ro'yxatdan o'tish uchun /register buyrug'ini yuboring")


def contact(update: Update, context: CallbackContext):
    update.message.reply_text("Murojaat uchun:\n\n+156648488848")


def language(update: Update, context: CallbackContext):
    update.message.reply_text("Tilni tanlang", reply_markup=inlines.get_language())
