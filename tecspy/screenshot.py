import pyautogui
import os
from datetime import datetime

class ScreenshotCapturer:
    def __init__(self, screenshot_dir):
        self.screenshot_dir = screenshot_dir
        self.ensure_directory_exists()

    def ensure_directory_exists(self):
        """Certifica-se de que o diretório para capturas de tela exista."""
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def capture(self):
        """Captura a tela e salva a imagem no diretório especificado."""
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_path = os.path.join(self.screenshot_dir, f'screenshot_{timestamp}.png')
        image = pyautogui.screenshot()
        image.save(screenshot_path)
        print(f"Screenshot salva em: {screenshot_path}")

