import os
from flask import Flask, app, request, render_template
from pdf import download_pdf,download_pdf_custom
from lokal_ollama import send_bot, send_data_custom
from dotenv import load_dotenv

app = Flask(__name__)

# HTML files have to be in "templates" folder.
# CSS files have to be in "static" folder.
# PDF will be created in "static/pdf"

load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html') 

@app.route('/login_page', methods=["GET"])
def login_page():
    return render_template('login.html') 

@app.route('/download_pdf', methods=['POST'])
def download_pdf_route():
    return download_pdf()


@app.route('/send_bot', methods=['POST'])
def send_bot_route():
    return send_bot()

@app.route('/custom', methods=["POST", "GET"])
def custom():
    print("Custom page loaded")
    return render_template("custom.html")

@app.route('/send_data_custom', methods=["POST","GET"])
def send_custom():
    return send_data_custom()

@app.route('/download_pdf_custom', methods=["GET", "POST"] )
def download_pdf_custom_route():
    return download_pdf_custom()

if __name__ == "__main__":
    app.run(debug=True)  