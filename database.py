import sqlite3
import os
import datetime as dt
from flask import Flask,render_template,request, jsonify,make_response

from flask import app 
from dotenv import load_dotenv




load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

today_date = dt.datetime.today().strftime("%d_%m_%Y_%H_%M")

con = sqlite3.connect("users.db")
cursor = con.cursor()

command1 = """
    CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY  AUTOINCREMENT, 
    email TEXT, 
    password TEXT, 
    created TEXT, 
    session TEXT
)
"""

cursor = cursor.execute(command1)

command2 = """
CREATE TABLE IF NOT EXISTS pdfs(
    pdf_id INTEGER PRIMARY KEY  AUTOINCREMENT, 
    Name TEXT, 
    nickname TEXT, 
    date_of_created TEXT, 
    user_id INTEGER, 
    FOREIGN KEY(user_id) REFERENCES users(user_id)
)
"""

cursor.execute(command2)

# TEST data for USERS
cursor.execute(f"INSERT INTO users VALUES (, 'test', 'test_password', '{today_date}', 'ON')")

# TEST data for PDFs
cursor.execute(f"INSERT INTO pdfs VALUES (, 'test_pdf', 'test_post', '{today_date}', 1)")

# Results
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()

cursor.execute("SELECT * FROM users")

result = cursor.fetchall()
print(result)

cursor.execute("SELECT * FROM pdfs")


result = cursor.fetchall()
print(result)
con.commit()
con.close()





