import logging

class Logger:
    def __init__(self, name, level = "DEBUG"):
        self.name = name
        self.level = level
        self.logger = None

    def set_level(self):
        if self.level == '' or self.level is None:
            return logging.INFO
        else:
            return self.level

    def get_logger(self):
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(self.set_level())
        formatter = logging.Formatter('%asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_logging = logging.StreamHandler()
        console_logging.setFormatter(formatter)

        return self.logger
