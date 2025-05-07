import datetime as dt
import os

from flask import Flask, app, request, render_template,session
from pdf import pobierz_pdf
from lokal_ollama import send_bot, wyslij_dane_niestandardowe
from dotenv import load_dotenv

app = Flask(__name__)

# Wczytaj sekretny klucz
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

# Wczytanie strony index
@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')  # Plik musi być w folderze "templates"

#Odpal funkcje po wciśnięciu przycisku 
@app.route('/pobierz_pdf', methods=['POST'])
def pobierz_pdf_route():
    return pobierz_pdf()

#Odpal funkcje po wciśnięciu przycisku 
@app.route('/send_bot', methods=['POST'])
def send_bot_route():
    return send_bot()

@app.route('/niestandardowe', methods=["POST"])
def niestandardowe():
    return render_template("niestandardowe.html")

@app.route('/niestandardowe_wyslij', methods=["POST","GET"])
def  niestandardowe_wyslij():
    return wyslij_dane_niestandardowe()

if __name__ == "__main__":
    app.run(debug=True)  # Uruchomienie serwera Flask w try