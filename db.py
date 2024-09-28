import sqlite3
from python_db import BOOKS


def create_db():
    conn = sqlite3.connect("my_bot.db")
    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS client (
        telegram_id PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        phone TEXT,
        address TEXT,
        is_admin TEXT
        );"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS book (
        id PRIMARY KEY,
        title TEXT,
        isbn TEXT,
        price TEXT,
        type TEXT,
        description TEXT,
        cover TEXT
        );"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS ClientOrder (
            id PRIMARY KEY,
            client_id TEXT,
            address TEXT,
            payment_type TEXT,
            total TEXT
        );"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS orderItem (
        id PRIMARY KEY,
        book_id TEXT,
        price TEXT,
        qty TEXT,
        order_id TEXT
        );"""
    )

    conn.commit()
    conn.close()


def create_user(telegram_id, first_name, last_name=None, address=None, phone=None, is_admin=0):
    conn = sqlite3.connect("my_bot.db")
    cursor = conn.cursor()

    user = cursor.execute(
        f"""SELECT * FROM client WHERE telegram_id='{telegram_id}'"""
    )

    user = user.fetchall()

    if not user:
        cursor.execute(
            f"""INSERT INTO client (
                telegram_id,
                first_name,
                last_name,
                phone,
                address,
                is_admin
            ) VALUES (
                '{telegram_id}',
                '{first_name}',
                '{last_name}',
                '{phone}',
                '{address}',
                '{is_admin}'
            )
            ;"""
        )

    conn.commit()
    conn.close()

    return {
        "telegram_id": telegram_id,
        "first_name": first_name,
        "last_name": last_name,
        "address":address,
        "phone": phone,
        "is_admin": is_admin
    }


def get_users():
    conn = sqlite3.connect("my_bot.db")
    cursor = conn.cursor()

    rows = cursor.execute(
        """SELECT * FROM client;"""
    )

    conn.commit()
    rows = rows.fetchall()
    conn.close()

    return rows


def create_book(title, isbn, price, type, description, cover):
    conn = sqlite3.connect("my_bot.db")
    cursor = conn.cursor()

    book = cursor.execute(
        "SELECT id FROM book ORDER BY id DESC LIMIT 1"
    )

    book = book.fetchone()
    book_id = int(book[0] if book else 0) + 1
    print("BOOK", book_id)

    query = f"""INSERT INTO book (id, title, isbn, price, type, description, cover)
            VALUES("{book_id}", "{title}", "{isbn}", 
            "{price}", "{type}", "{description}", "{cover}");"""
    
    book = cursor.execute(query)

    conn.commit()
    conn.close()


def import_books():
    for book in BOOKS:
        create_book(book['title'], book['isbn'], book['price'], book['_type'], book['description'], book['cover'])


def get_books():
    conn = sqlite3.connect("my_bot.db")
    cursor = conn.cursor()

    rows = cursor.execute(
        """SELECT * FROM book;"""
    )

    conn.commit()
    rows = rows.fetchall()
    conn.close()

    return rows


def get_books_by_type(_type="paper"):
    conn = sqlite3.connect("my_bot.db")
    cursor = conn.cursor()

    rows = cursor.execute(
        f"""SELECT * FROM book WHERE type='{_type}'"""
    )
    rows = rows.fetchall()
    conn.close()

    return rows

def get_book_by_id(id=None):
    if not id:
        return []
    conn = sqlite3.connect("my_bot.db")
    cursor = conn.cursor()

    rows = cursor.execute(
        f"""SELECT * FROM book WHERE id='{id}'"""
    )
    rows = rows.fetchone()
    conn.close()

    return rows


def create_order(client_id, total):
    conn = sqlite3.connect("my_bot.db")
    cursor = conn.cursor()

    last_order = cursor.execute(
        "SELECT id FROM ClientOrder ORDER BY id DESC LIMIT 1"
    )

    last_order = last_order.fetchone()
    order_id = int(last_order[0] if last_order else 0) + 1

    cursor.execute(
        f"""INSERT INTO ClientOrder (id, client_id, address, payment_type, total)
            VALUES("{order_id}", "{client_id}", "{None}", "{None}", {total});"""
    )
    conn.commit()
    conn.close()

    return order_id


def create_order_item(book_id, price, qty, order_id):
    conn = sqlite3.connect("my_bot.db")
    cursor = conn.cursor()

    last_order_item = cursor.execute(
        "SELECT id FROM orderItem ORDER BY id DESC LIMIT 1"
    )

    last_order_item = last_order_item.fetchone()
    order_id = int(last_order_item[0] if last_order_item else 0) + 1

    cursor.execute(
        f"""INSERT INTO orderItem (id, book_id, price, qty, order_id)
            VALUES("{order_id}", "{book_id}", "{price}", "{qty}", {order_id});"""
    )
    conn.commit()
    conn.close()




def finish_order(client_id, order_items):
    total = 0
    for item in order_items:
        book = get_book_by_id(item['book_id'])
        if book:
            total += int(book[3]) * int(item['amount'])

    order_id = create_order(client_id, total)
    
    for item in order_items:
        book = get_book_by_id(item['book_id'])
        if book:
            create_order_item(item['book_id'], int(book[3]), item['amount'], order_id)




if __name__ == "__main__":
    create_db()
    print("DB Created successfully")