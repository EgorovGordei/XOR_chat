import sqlite3


DBNAME = 'database.db'


def get_db_connection():
    conn = sqlite3.connect(DBNAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    connection = sqlite3.connect(DBNAME)
    connection.executescript(
                """
                DROP TABLE IF EXISTS messages;

                CREATE TABLE messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    message TEXT NOT NULL,
                    author TEXT NOT NULL
                );

                INSERT INTO messages (message, author) VALUES ('NOTHING', '');
                """)

    connection.commit()
    connection.close()


def pretty_data(data):
    return [([col for col in row]) for row in data]
