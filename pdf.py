# zmienna form nie dodaje sie do context - sposob na wyciagniecie danych z form.dict
import pdfkit
import jinja2
import os
import datetime as dt

from config import BASE_DIR,WKHTMLTOPDF_PATH
from dotenv import load_dotenv
from flask import app, request, render_template,session

# Load files from .env
load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

CHR_DIR_PATH = os.getenv('CHR_DIR_PATH')
print (CHR_DIR_PATH)
os.chdir(CHR_DIR_PATH)

# Read data_form -> Create PDF 
def download_pdf():
    # Wczytaj dane z formularza
    respond = session.get('respond')
    form = session.get('forms')
    print(form)
    if not form:
        print("Error: Variable 'form' dosent exist.")
        return "Error: Form is empty in session."

    required_keys = ["platform", "topic", "goal", "details", "more_information"]
    for key in required_keys:
        if key not in form:
            print(f"Error: Unexisted '{key}' in 'form'.")
            return f"Error: Unexisted '{key}' in form data."

    print(f"Data PDF: {form}, {form.values()} i  {form.keys()}")
    print("")
    print(form["topic"])
    print("")
    print(f"Variable respond for function download_pdf() ")

    today_date = dt.datetime.today().strftime("%d_%m_%Y_%H_%M")

    context = {
    'form':form,
    'platform': form["platform"],
    "topic": form["topic"],
    "goal": form['goal'],
    'details': form['details'],
    'more_informations': form['more_information'],
    'respond': respond,
    'data': today_date,
    }

    print("Content was generated")

    template_loader = jinja2.FileSystemLoader(F"{CHR_DIR_PATH}\\templates")
    template_env = jinja2.Environment(loader=template_loader)
    
    print("Check if folder exists:", os.path.exists("templates"))
    print(os.path)

    template = template_env.get_template("creator.html")
    
    
    output_text = template.render(context)
    config_pdf = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
    pdf_path = os.path.join(BASE_DIR, 'static', 'pdf', f"post_SocialMedias_{today_date}.pdf")
    css_path = os.path.join(BASE_DIR, "static", "pdf-style.css")
    if not os.path.exists(css_path):
        print(f"Error: File CSS dosent exist in path: {css_path}")
        return "Error: File CSS not found."

    print("Path for file CSS:", css_path)
    print("IF file CSS exist:", os.path.exists(css_path))

    pdfkit.from_string(output_text, pdf_path, configuration=config_pdf, css=css_path)
    pdf_result = "PDF is ready"
    return render_template('index.html', pdf_result=pdf_result)

#  Read custom_data_form -> Create PDF 
def download_pdf_custom():
    cookie_respond_custom = session.get("custom_respond")
    print(f"Function download_pdf_custom() is working: {cookie_respond_custom}")

    today_date = dt.datetime.today().strftime("%d_%m_%Y_%H_%M")

    context = {
    'custom_respond': cookie_respond_custom,
    'date': today_date 
    }

    template_loader = jinja2.FileSystemLoader(F"{CHR_DIR_PATH}\\templates")
    template_env = jinja2.Environment(loader=template_loader)
    
    print("Check if folder exists", os.path.exists("templates"))
    print(os.path)

    template = template_env.get_template("creator_custom.html")

    output_text = template.render(context)
    config_pdf = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
    pdf_path = os.path.join(BASE_DIR, 'static', 'pdf', f"post_CustomSM_{today_date}.pdf")
    css_path = os.path.join(BASE_DIR, "static", "pdf-style.css")
    if not os.path.exists(css_path):
        print(f"Error: File CSS dosent exist in path: {css_path}")
        return "Error: File CSS not found."

    print("Path for CSS:", css_path)
    print("IF file CSS exist:", os.path.exists(css_path))

    pdfkit.from_string(output_text, pdf_path, configuration=config_pdf, css=css_path)
    pdf_result_custom = "PDF is Generated"
    return render_template('custom.html', pdf_result_custom=pdf_result_custom)