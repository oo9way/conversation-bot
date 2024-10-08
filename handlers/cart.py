from telegram import Update
from telegram.ext import CallbackContext
from db import get_book_by_id, create_order, create_order_item
from keyboards import inlines, replies
import constants, states


def view_cart(update: Update, context: CallbackContext):
    cart_items = context.user_data.get("cart", [])
    if not cart_items:
        update.message.reply_text("You haven't got any products in your cart")
        return states.END
    
    message = "Kitoblar\n"
    total_amount = 0
    items_for_buttons = []
    for item in cart_items:
        book = get_book_by_id(item['book_id'])
        if book:
            item['title'] = book[1]
            items_for_buttons.append(item)
            total_amount += int(book[3]) * item['amount']
            message += f"Kitob: {book[1]} \n"
            message += f"Narxi: {book[3]} \n"
            message += f"Soni: {item['amount']} \n"
            message += f"Umumiy summa: {int(book[3]) * item['amount']} \n"
            message += "========================\n\n"
    
    message += f"Jami summa: {total_amount}"

    update.message.reply_text(message, reply_markup=inlines.change_order_counts(items_for_buttons))
    return states.CART_ACTIONS


def cart_action(update: Update, context: CallbackContext):
    data = update.callback_query.data

    if data == "complete-order":
        update.callback_query.answer()
        # send order items to admin
        cart_items = context.user_data['cart']
        message = "Buyurtma\n"
        full_name = str(update.callback_query.from_user.first_name) + " " + str(update.callback_query.from_user.last_name)
        message += f"Mijoz: {full_name}\n\n"
        message += "Kitoblar\n"
        total_amount = 0

        for item in cart_items:
            book = get_book_by_id(item['book_id'])
            if book:
                item['title'] = book[1]
                total_amount += int(book[3]) * item['amount']
                message += f"Kitob: {book[1]} \n"
                message += f"Narxi: {int(book[3])} \n"
                message += f"Soni: {item['amount']} \n"
                message += f"Umumiy summa: {int(book[3]) * item['amount']} \n"
                message += "========================\n\n"
        
        message += f"Jami summa: {total_amount}"
        order_id = create_order(update.callback_query.message.from_user.id, total_amount)

        for item in cart_items:
            book = get_book_by_id(item['book_id'])
            create_order_item(item['book_id'], book[3], item['amount'], order_id)

        for admin in constants.ADMINS:
            context.bot.send_message(admin, message)
        update.callback_query.message.delete()
        context.user_data['cart'] = []
        update.callback_query.message.reply_text("Sizning buyurtmangiz adminlarga yuborildi.", reply_markup=replies.get_main("uz"))
        return states.END

    elif data == "clear-cart":
        update.callback_query.answer()
        # we should clear cart
        update.callback_query.message.delete()
        context.user_data['cart'] = []
        update.callback_query.message.reply_text("Savatcha bo'shatildi.", reply_markup=replies.get_main("uz"))
        return states.END

    else:
        action, book_id = data.split("-")
        book_id = int(book_id)
        cart_items = context.user_data['cart']

        if action == "default":
            book = get_book_by_id(book_id)
            update.callback_query.answer(book[1])
            return states.CART_ACTIONS
        
        elif action == "increase":
            new_cart_items = []

            for item in cart_items:
                if item['book_id'] == book_id:
                    item['amount'] = item['amount'] + 1

                new_cart_items.append(item)

            context.user_data['cart'] = new_cart_items

        elif action == "decrease":
            new_cart_items = []

            for item in cart_items:
                if item['book_id'] == book_id:
                    item['amount'] = item['amount'] - 1

                if item['amount'] > 0:
                    new_cart_items.append(item)

            context.user_data['cart'] = new_cart_items

        elif action == "clear":
            new_cart_items = []

            for item in cart_items:
                if item['book_id'] != book_id:
                    new_cart_items.append(item)

            context.user_data['cart'] = new_cart_items

        update.callback_query.answer()
        total_amount = 0
        items_for_buttons = []
        message = "Kitoblar\n"
        for item in context.user_data['cart']:
            book = get_book_by_id(item['book_id'])
            if book:
                item['title'] = book[1]
                items_for_buttons.append(item)
                total_amount += int(book[3]) * item['amount']
                message += f"Kitob: {book[1]} \n"
                message += f"Narxi: {book[3]} \n"
                message += f"Soni: {item['amount']} \n"
                message += f"Umumiy summa: {int(book[3]) * item['amount']} \n"
                message += "========================\n\n"
        
        message += f"Jami summa: {total_amount}"
        update.callback_query.message.delete()
        update.callback_query.message.reply_text(message, reply_markup=inlines.change_order_counts(items_for_buttons))
        return states.CART_ACTIONS