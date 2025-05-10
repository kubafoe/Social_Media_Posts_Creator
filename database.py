import os
import datetime as dt
from flask import Flask,render_template,request, jsonify,make_response
from flask_sqlalchemy import SQLAlchemy

from flask import app 
from dotenv import load_dotenv




load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

# con = sqlite3.connect("users.db")
# cursor = con.cursor()

# command1 = """CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY  AUTOINCREMENT, email TEXT, password TEXT, created TEXT, session TEXT)"""

# # cursor = cursor.execute(command1)

# command2 = """
# CREATE TABLE IF NOT EXISTS pdfs(
#     pdf_id INTEGER PRIMARY KEY  AUTOINCREMENT, 
#     Name TEXT, 
#     nickname TEXT, 
#     date_of_created TEXT, 
#     user_id INTEGER, 
#     FOREIGN KEY(user_id) REFERENCES users(user_id)
# )
# """

# # cursor.execute(command2)

# # # TEST data for USERS
# # cursor.execute(f"INSERT INTO users VALUES (1, 'test', 'test_password', '{today_date}', 'ON')")

# # # TEST data for PDFs
# # cursor.execute(f"INSERT INTO pdfs VALUES (1, 'test_pdf', 'test_post', '{today_date}', 1)")

# # # Results
# # cursor.execute("SELECT * FROM users")
# # results = cursor.fetchall()

# cursor.execute("SELECT * FROM users")

# result = cursor.fetchall()
# print(result)

# cursor.execute("SELECT * FROM pdfs")


# result = cursor.fetchall()
# print(result)
# con.commit()
# con.close()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)
today_date = dt.datetime.today().strftime("%d_%m_%Y_%H_%M")

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    created = db.Column(db.String, nullable=False)
    session = db.Column(db.String, nullable=False)
    
    def to_dict(self):
        return {"id": self.id, "email": self.email, "password": self.password, "session": self.session}
    
# File location: 'D:\Programowanie\"Projekt-Formularz-do-Tworzenia postów-w-Social-Mediach"\database.py'
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Task': Task}

klasa = Task(
    email="test@example.com",
    password="securepassword",
    created=today_date,
    session="ON"
)

print (klasa)
db.session.add(klasa)
db.session.commit()
