# config.py

import os

# Ścieżki
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PDF_OUTPUT_PATH = os.path.join(BASE_DIR, 'static', 'pdf')

# Konfiguracja wkhtmltopdf
WKHTMLTOPDF_PATH = r"C:\wkhtmltox\bin\wkhtmltopdf.exe"

# Można także dodać inne zmienne, np. dane do bazy danych, konfiguracje API, itp.