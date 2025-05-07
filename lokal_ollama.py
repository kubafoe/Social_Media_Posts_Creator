from flask import session, request, render_template, app, make_response
from ollama import chat
from dotenv import load_dotenv
from sqlite3 import connect
import os


# Wczytaj sekretny klucz
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

class formularz:
    def __init__(self, temat, cel, platforma, kontekst, dodatkowe, tagi_html,model):
        self.temat = temat
        self.cel = cel
        self.platforma = platforma
        self.kontekst = kontekst
        self.dodatkowe = dodatkowe
        self.tagi_html = tagi_html
        self.model = tagi_html
        self.dane = [temat, cel, platforma, kontekst, dodatkowe, tagi_html, model]

    def to_dict(self):
        return {
        "temat": self.temat,
        "cel": self.cel,
        "platforma": self.platforma,
        "kontekst": self.kontekst,
        "dodatkowe": self.dodatkowe,
        "tagi_html": self.tagi_html,
        "model": self.model
        }

# Wczytaj dane z formularza -> wyślij dane do AI -> wprowadź na stronie index.html
def send_bot(): 
    # Wczytaj dane z formularza
    form = formularz(
    request.form.get('temat'),
    request.form.get('cel'),
    request.form.get('platformy'),
    request.form.get('kontekst'),
    request.form.get('dodatkowe'),
    request.form.get('tagi_html')
    )
    print(form.to_dict())
    print(form)
    

    if not form.temat.strip() or not form.kontekst.strip():
        error = "Uzupełnij wymagane pola!"
        print(error)
        return render_template('index.html',error=error)
    else:
        odpowiedz = wyslij_dane(form.temat,form.cel,form.platforma,form.kontekst,form.dodatkowe,form.tagi_html)
        session['odpowiedz'] = odpowiedz
        session['form'] = form.to_dict()
        print("send_BOT + wyslij_dane Sukces")
        return render_template("index.html", odpowiedz=odpowiedz)
   
# Wyślij dane do AI ze wczytanimi informacje z funkcji send_ bot()
def wyslij_dane(temat,cel,platforma,kontekst,dodatkowe,tagi_html):
    print("Wyslij dane uruchomione" )

    prompt = f"Stwórz post w języku polskim na {platforma}, na temat {temat} w celu {cel} w kontekście {kontekst} oraz opcjonalnie zawierający: {dodatkowe}."
    if tagi_html == '1':
        prompt += " Ważne: użyj składni HTML."

    response = chat(model="gemma3", messages=[{"role": "user", "content": prompt}])

    print(prompt)
    odpowiedz = response.message.content
    return odpowiedz

def wyslij_dane_niestandardowe():
    prompt = request.form.get('niestandardowe_prompt')
    print(f"prompt = {prompt}")
    if prompt == None or prompt == "":
        error = "Wprowadź dane do formularza!"
        print(error)
        return  render_template("niestandardowe.html", error=error)
    else:
        response = chat(model="gemma3", messages=[{"role": "user", "content": prompt}])
        odpowiedz_niestandardowa = response.message.content
        print(f"response: {response}")
        session['odpowiedz_niestandardowa'] = odpowiedz_niestandardowa
        print(odpowiedz_niestandardowa)
        return render_template("niestandardowe.html", odpowiedz_niestandardowa=odpowiedz_niestandardowa)
    




 