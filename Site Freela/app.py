from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Configurações do seu servidor de e-mail (SMTP)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "joaofelipegaldinodelima75@gmail.com"
EMAIL_PASSWORD = "sjkz ygps xbhu jrbd"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar_mensagem", methods=["POST"])
def enviar_mensagem():
    # Pega os dados do formulário
    nome = request.form.get("name")
    email_cliente = request.form.get("email")
    mensagem = request.form.get("message")

    # Cria a mensagem de e-mail
    msg = EmailMessage()
    msg.set_content(f"Nome: {nome}\nE-mail: {email_cliente}\n\nMensagem:\n{mensagem}")
    msg["Subject"] = "Nova Mensagem de Contato do Site Freelance"
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_USER

    try:
        # Conecta e envia o e-mail
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)
        return redirect(url_for('sucesso'))
    except Exception as e:
        return f"Ocorreu um erro: {e}"

@app.route("/sucesso")
def sucesso():
    return "<h1>Mensagem enviada com sucesso!</h1><p>Em breve entraremos em contato.</p>"

if __name__ == "__main__":
    app.run(debug=True, port=5500)