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


# # TEST data for USERS
# cursor.execute(f"INSERT INTO users VALUES (, 'test', 'test_password', '{today_date}', 'ON')")

# TEST data for PDFs
cursor.execute("INSERT INTO pdfs VALUES (, 'test_pdf', 'test_post', '10.02.2025', 1)")

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





