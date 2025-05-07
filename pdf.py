# zmienna form nie dodaje sie do context - sposob na wyciagniecie danych z form.dict
import pdfkit
import jinja2
import os
import datetime as dt

from config import BASE_DIR,WKHTMLTOPDF_PATH
from dotenv import load_dotenv
from flask import Flask, app, request, render_template,session,make_response

os.chdir("D:\\Programowanie\\Projekt-Formularz-do-Tworzenia postów-w-Social-Mediach")

# Wczytaj sekretny klucz
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

# Wczytaj dane z formularza -> stwórz PDF 
def pobierz_pdf():
    # Wczytaj dane z formularza
    odpowiedz = session.get('odpowiedz')
    form = session.get('form')
    if not form:
        print("Błąd: Zmienna 'form' nie istnieje w sesji.")
        return "Błąd: Brak danych formularza w sesji."

    required_keys = ["platforma", "temat", "cel", "kontekst", "dodatkowe"]
    for key in required_keys:
        if key not in form:
            print(f"Błąd: Brakuje klucza '{key}' w 'form'.")
            return f"Błąd: Brakuje klucza '{key}' w danych formularza."

    print(f"Dane PDF: {form}, {form.values()} i  {form.keys()}")
    print("")
    print(form["temat"])
    print("")
    print(f"Zmienna odpowiedz dla funkcji pobierz_pdf() ")

    
    today_date = dt.datetime.today().strftime("%d_%m_%Y_%H_%M")
    context = {
    'form':form,
    'platformy': form["platforma"],
    "temat": form["temat"],
    "cel": form['cel'],
    'kontekst': form['kontekst'],
    'dodatkowe': form['dodatkowe'],
    'odpowiedz': odpowiedz,
    'data': today_date,
    }

    print("Content został wygenerowany")

    template_loader = jinja2.FileSystemLoader("D:\\Programowanie\\Projekt-Formularz-do-Tworzenia postów-w-Social-Mediach\\templates")
    template_env = jinja2.Environment(loader=template_loader)
    
    print("Czy folder istnieje:", os.path.exists("templates"))
    print(os.path)

    template = template_env.get_template("creator.html")
    
    
    output_text = template.render(context)
    config_pdf = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
    pdf_path = os.path.join(BASE_DIR, 'static', 'pdf', f"post_SocialMedias_{today_date}.pdf")
    css_path = os.path.join(BASE_DIR, "static", "pdf-style.css")
    if not os.path.exists(css_path):
        print(f"Błąd: Plik CSS nie istnieje w ścieżce {css_path}")
        return "Błąd: Plik CSS nie został znaleziony."

    print("Ścieżka do pliku CSS:", css_path)
    print("Czy plik CSS istnieje:", os.path.exists(css_path))

    pdfkit.from_string(output_text, pdf_path, configuration=config_pdf, css=css_path)
    pdf_rezultat = "PDF został wygenerowany"
    return render_template('index.html', pdf_rezultat=pdf_rezultat)

def pobierz_pdf_niestandarodwe(cookie_odpowiedz_niestandardowa):
    cookie_odpowiedz_niestandardowa = session.get("odpowiedz_niestandardowa")
    print(cookie_odpowiedz_niestandardowa)

    today_date = dt.datetime.today().strftime("%d_%m_%Y_%H_%M")

    context = {
    'odpowiedz_niestandardowa': cookie_odpowiedz_niestandardowa,
    'data': today_date 
    }

    template_loader = jinja2.FileSystemLoader("D:\\Programowanie\\Projekt-Formularz-do-Tworzenia postów-w-Social-Mediach\\templates")
    template_env = jinja2.Environment(loader=template_loader)
    
    print("Czy folder istnieje:", os.path.exists("templates"))
    print(os.path)

    template = template_env.get_template("creator_niestandardowy.html")

    output_text = template.render(context)
    config_pdf = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
    pdf_path = os.path.join(BASE_DIR, 'static', 'pdf', f"post_NiestandardoweSM_{today_date}.pdf")
    css_path = os.path.join(BASE_DIR, "static", "pdf-style.css")
    if not os.path.exists(css_path):
        print(f"Błąd: Plik CSS nie istnieje w ścieżce {css_path}")
        return "Błąd: Plik CSS nie został znaleziony."

    print("Ścieżka do pliku CSS:", css_path)
    print("Czy plik CSS istnieje:", os.path.exists(css_path))

    pdfkit.from_string(output_text, pdf_path, configuration=config_pdf, css=css_path)
    pdf_rezultat_niestandardowy = "PDF został wygenerowany"
    return render_template('niestandardowe.html', pdf_rezultat_niestandardowy=pdf_rezultat_niestandardowy)