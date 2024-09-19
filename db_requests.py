telegram_id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name

    print(telegram_id, first_name, last_name)

    try:
        conn = sqlite3.connect("my_bot.db")
        cursor = conn.cursor()

        cursor.execute(
            f"""
                INSERT INTO telegram_users (telegram_id, first_name, last_name) VALUES('{telegram_id}', '{first_name}', '{last_name}')
            """
        )

        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        pass





def get_users(update: Update, context: CallbackContext):
    conn = sqlite3.connect("my_bot.db")
    cursor = conn.cursor()

    rows = cursor.execute("select * from telegram_users")
    rows = rows.fetchall()

    message = "Your current users list \n"
    for row in rows:
        message += f"User: {row[1]} {row[2]}\n"    

    update.message.reply_text(message)