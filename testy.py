from flask import session, request, render_template, app
from ollama import chat
from dotenv import load_dotenv
import os

# Przetetuje zabawe z to_dict(values i kesy)
app.secret_key = os.getenv('SECRET_KEY')
load_dotenv()



odpowiedz = session.get('odpowiedz')
form = session.get('form')

print(f"Dane PDF: {form}, {form.values()} i  {form.keys()}")
print("")
print(f"Zmienna odpowiedz dla funkcji pobierz_pdf() {odpowiedz}")




print(app.secret_key)
