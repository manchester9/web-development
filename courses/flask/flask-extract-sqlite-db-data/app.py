from flask import Flask, g, render_template
import sqlite3
import os

DATABASE = "./database.db"

# Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'

# check if the database exist
# if not, create the database, the table and insert records
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (firstname TEXT, lastname TEXT, age INTEGER);")
    conn.commit()
    cur.execute("INSERT INTO users VALUES('Marina', 'Tyson', '40');")
    cur.execute("INSERT INTO users VALUES('Susan', 'Jasper', '40');")
    cur.execute("INSERT INTO users VALUES('Jerry', 'Mouse', '40');")
    cur.execute("INSERT INTO users VALUES('Peter', 'Pan', '40');")
    conn.commit()
    conn.close()


# helper method to get the database since calls are per thread,
# and everything function is a new thread when called
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# helper to close
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    cur = get_db().cursor()
    res = cur.execute("SELECT * FROM users")
    return render_template("index.html", users=res)


if __name__ == "__main__":
    app.run()
