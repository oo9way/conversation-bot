from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def get_language():
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text="O'zbek tili", callback_data="uz")],
            [InlineKeyboardButton(text="Rus tili", callback_data="ru")],
            [InlineKeyboardButton(text="Ingliz", callback_data="en")],
            [InlineKeyboardButton(text="Tojik tili", callback_data="tj")],
            [InlineKeyboardButton(text="Kun.uz", url="https://kun.uz")],
        ]
    )


def get_list_button(items):
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=item['title'], callback_data=f"book-{item['id']}")] for item in items
        ]
    )

def get_book_actions():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Buyurtma berish", callback_data="order"),InlineKeyboardButton("Bekor qilish", callback_data="cancel")
            ]
        ]
    )


def change_order_counts(items):
    keyboards = []

    for item in items:
        keyboards.append(
            [
                InlineKeyboardButton("+", callback_data=f"increase-{item['book_id']}"),
                InlineKeyboardButton(item['title'], callback_data=f"default-{item['book_id']}"),
                InlineKeyboardButton("-", callback_data=f"decrease-{item['book_id']}"),
                InlineKeyboardButton("x", callback_data=f"clear-{item['book_id']}")
            ],
        )

    keyboards.append(
        [
            InlineKeyboardButton("Buyurtmani yakunlash", callback_data="complete-order"),
            InlineKeyboardButton("Savatni tozalash", callback_data="clear-cart")
        ]
    )


    return InlineKeyboardMarkup(keyboards)