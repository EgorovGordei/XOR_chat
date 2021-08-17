from flask import Flask, render_template, request, make_response, url_for
import sqlite3
from dbutils import init_db, get_db_connection, pretty_data
import random
from datetime import datetime


app = Flask(__name__)


@app.route("/get_last_message")
def get_last_message():
    conn = get_db_connection()
    all_data = conn.execute("""SELECT message FROM messages
                               WHERE id =
                               (SELECT MAX(id) FROM messages);""").fetchall()
    conn.close()
    return str(pretty_data(all_data))

@app.route("/send_message", methods=["POST"])
def send_message():
    if request.method == 'POST':
        message = request.form["message"]
    conn = get_db_connection()
    conn.execute("INSERT INTO messages (message, author) VALUES (?, ?)",
                 (message, ""))
    conn.commit()
    conn.close()
    return ''

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=80)
