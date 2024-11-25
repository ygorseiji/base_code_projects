from datetime import datetime
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

class LogFile:
    _instance = None
    _file_name = os.path.join(base_dir, f"../log/log_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.txt")

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def write_log(self, message):
        with open(self._file_name, "a") as file:
            file.write(f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')} - {message}\n")
            print(f'Debug: {message}')