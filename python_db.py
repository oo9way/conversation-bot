BOOKS = [
    {
        "id": 1,
        "title": "Sariq devni minib",
        "price": 25000,
        "description": """I'm using Python/SQLite for accessing database. After running the query, 
        and getting the result, I want to know the number of rows, the number of columns, and the name of
        the column from the queried result and database. """,
        "_type": "paper",
        "cover": "https://static.vecteezy.com/system/resources/thumbnails/020/484/423/small_2x/hand-drawn-open-book-vector.jpg"
    },
    {
        "id": 2,
        "title": "Harry Potter",
        "price": 56800,
        "description": """I'm using Python/SQLite for accessing database. After running the query, 
        and getting the result, I want to know the number of rows, the number of columns, and the name of
        the column from the queried result and database. """,
        "_type": "audio",
        "cover": "https://static.vecteezy.com/system/resources/thumbnails/020/484/423/small_2x/hand-drawn-open-book-vector.jpg"

    },
    {
        "id": 3,
        "title": "Kichkina Shaxzoda",
        "price": 14000,
        "description": """I'm using Python/SQLite for accessing database. After running the query, 
        and getting the result, I want to know the number of rows, the number of columns, and the name of
        the column from the queried result and database. """,
        "_type": 'audio',
        "cover": "https://static.vecteezy.com/system/resources/thumbnails/020/484/423/small_2x/hand-drawn-open-book-vector.jpg"

    },
    {
        "id": 4,
        "title": "O'tgan kunlar",
        "price": 2200,
        "description": """I'm using Python/SQLite for accessing database. After running the query, 
        and getting the result, I want to know the number of rows, the number of columns, and the name of
        the column from the queried result and database. """,
        "_type": "paper",
        "cover": "https://static.vecteezy.com/system/resources/thumbnails/020/484/423/small_2x/hand-drawn-open-book-vector.jpg"
    },
    {
        "id": 5,
        "title": "Otamdan qolgan dalalar",
        "price": 90000,
        "description": """I'm using Python/SQLite for accessing database. After running the query, 
        and getting the result, I want to know the number of rows, the number of columns, and the name of
        the column from the queried result and database. """,
        "_type": "paper",
        "cover": "https://static.vecteezy.com/system/resources/thumbnails/020/484/423/small_2x/hand-drawn-open-book-vector.jpg"
    }
]

def get_book_by_id(book_id: int) -> dict:
    for book in BOOKS:
        if book["id"] == book_id:
            return book
        
    return None