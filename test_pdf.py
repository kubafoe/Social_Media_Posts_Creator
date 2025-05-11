import pytest
from flask import session,app
from pdf import download_pdf_custom

@pytest.fixture
def client(mocker):
    from pdf import app
    with app.test_client() as client:
        # Mockowanie klucza sesji
        app.secret_key = "test_secret_key"
        with client.session_transaction() as sess:
            sess["custom_respond"] = "Test custom response"
        yield client

def test_download_pdf_custom(client, mocker):
    # Mockowanie jinja2 i pdfkit
    mocker.patch("jinja2.Environment.get_template", return_value=mocker.Mock(render=lambda context: "Rendered HTML"))
    mocker.patch("pdfkit.from_string", return_value=None)

    # Wysyłanie żądania do funkcji
    response = client.get("/download_pdf_custom")

    # Sprawdzanie odpowiedzi
    assert response.status_code == 200
    assert b"PDF is Generated" in response.data