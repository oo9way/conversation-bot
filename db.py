import sqlite3

def create_db():
    conn = sqlite3.connect("my_bot.db")
    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS telegram_users (
        telegram_id PRIMARY KEY,
        first_name TEXT,
        last_name TEXT
        )"""
    )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
    print("DB Created successfully")