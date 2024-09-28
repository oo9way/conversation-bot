from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext, PollAnswerHandler
from translation import get_translation as _
from keyboards import replies, inlines
import states
from db import get_books_by_type, get_book_by_id

def set_language(update: Update, context: CallbackContext):
    context.user_data["language"] = update.callback_query.data
    update.callback_query.answer()
    update.callback_query.message.delete()
    update.callback_query.message.reply_text(_("change_language", update.callback_query.data))


def get_books(update: Update, context: CallbackContext):
    language = context.user_data["language"]
    books = ""
    book_list = []

    BOOKS = get_books_by_type()

    for book in BOOKS:
        book_list.append(book)
        books += "======================\n"
        books += f"Nomi: {book[1]}\n"
        books += f"Narxi: {book[3]}\n"
        books += "======================\n\n"


    if not books:
        update.message.reply_text(_("books_bot_found", language), reply_markup=replies.get_main(language))
        return
    message = "<b>Kitoblar</b>\n" + books
    if update and update.message:
        update.message.reply_text(message, reply_markup=inlines.get_list_button(book_list), parse_mode="html")
    if update and update.callback_query:
        update.callback_query.message.reply_text(message, reply_markup=inlines.get_list_button(book_list), parse_mode="html")
    return states.BOOK_SINGLE



def get_book(update:Update, context:CallbackContext):
    book_id = int(update.callback_query.data.split("-")[-1])
    update.callback_query.answer()
    update.callback_query.message.delete()

    # for item in get_books_by_type():
    #     if item['id'] == book_id:
    #         book = item
    #         break

    book = get_book_by_id(book_id)

    if not book:
        update.message.reply_text("Siz izlagan kitob topilmadi", )
        return get_books(update, context)
    
    context.user_data["selected_book"] = book_id

    caption = f"<b>{book[1]}</b>\n"
    caption += f"<b>Narxi:</b> {book[3]}\n"
    caption += f"<b>Tavsif:</b> {book[5]}"

    update.callback_query.message.reply_photo(photo=book[6], caption=caption, parse_mode="html", reply_markup=inlines.get_book_actions())
    return states.BOOK_ACTION


def get_book_action(update: Update, context: CallbackContext):
    data = update.callback_query.data
    update.callback_query.answer()
    update.callback_query.message.delete()

    if data == "cancel":
        return get_books(update, context)
    
    else:
        update.callback_query.message.reply_text("Buyurtma sonini kiriting")
        return states.GET_ORDER


def get_book_order(update: Update, context: CallbackContext):
    amount = update.message.text

    try:
        amount = int(amount)
    except:
        update.message.reply_text("Iltimos, buyurtma sonini raqamlarda kiriting")
        return states.GET_ORDER
    
    order_item = {
        "book_id": context.user_data["selected_book"],
        "amount": amount
    }

    cart = context.user_data.get("cart", None)

    if cart:
        cart.append(order_item)
        context.user_data['cart'] = cart
    else:
        context.user_data['cart'] = [order_item]

    update.message.reply_text("Mahsulot savatga qo'shildi", reply_markup=replies.get_main("uz"))
    return states.END
