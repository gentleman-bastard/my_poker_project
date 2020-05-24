import logging

class Logger:
    def __init__(self, name):
        self.name = name
        self.logger = None

    def get_logger(self):
        logging.basicConfig()
        logging.root.setLevel(logging.NOTSET)
        self.logger = logging.getLogger(self.name)

        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_logging = logging.StreamHandler()
        console_logging.setFormatter(formatter)

        return self.logger
