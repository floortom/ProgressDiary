import sqlite3

connection = sqlite3.connect("ProgressDiary.db")


def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries"
                           "(content TEXT,"
                           "date TEXT);"
                           )


def add_entry(entryContent, entryDate):
    with connection:
        connection.execute("INSERT INTO entries (content, date)"
                           "VALUES (?, ?);",
                           (entryContent, entryDate)
                           )


def get_entries():
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor
