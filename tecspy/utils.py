import os

def create_log_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
