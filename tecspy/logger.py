import logging

class Logger:
    def __init__(self, log_file_path):
        logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(asctime)s: %(message)s')
    
    def log_key(self, key):
        logging.info(key)

    def log_special_event(self, event):
        logging.info(f'Special event: {event}')
