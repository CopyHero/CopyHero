# coding:utf-8

import logging
import os
from logging.handlers import TimedRotatingFileHandler

# Define log levels
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

# Define paths for log files
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.join(CURRENT_PATH, os.pardir)
LOG_PATH = os.path.join(ROOT_PATH, "..", "copy-hero-logs")

# Create log directory if it doesn't exist
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


# Define a custom log handler class
class LogHandler(logging.Logger):
    """
    LogHandler
    """

    def __init__(self, name, level=DEBUG, stream=True, file=True):
        """
        Initialize the LogHandler with specified name and log level.
        Optionally enable stream and file handlers.
        """
        self.name = name
        self.level = level
        logging.Logger.__init__(self, self.name, level=level)
        if stream:
            self.__setStreamHandler__()
        if file:
            self.__setFileHandler__()

    def __setFileHandler__(self, level=None):
        """
        Set up the file handler for logging to a file.
        Log files are rolled over daily and kept for 15 days.
        """
        file_name = os.path.join(LOG_PATH, "{name}.log".format(name=self.name))
        # Set log rotation: daily files, keep 15 days of logs
        file_handler = TimedRotatingFileHandler(
            filename=file_name, when="D", interval=1, backupCount=15
        )
        file_handler.suffix = "%Y%m%d.log"
        if not level:
            file_handler.setLevel(self.level)
        else:
            file_handler.setLevel(level)
        formatter = logging.Formatter(
            "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s"
        )

        file_handler.setFormatter(formatter)
        self.file_handler = file_handler
        self.addHandler(file_handler)

    def __setStreamHandler__(self, level=None):
        """
        Set up the stream handler for logging to the console.
        """
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s"
        )
        stream_handler.setFormatter(formatter)
        if not level:
            stream_handler.setLevel(self.level)
        else:
            stream_handler.setLevel(level)
        self.addHandler(stream_handler)

    def __setErrorFileHandler__(self, level=None):
        """
        Set up a separate file handler for logging error messages.
        """
        error_file_name = os.path.join(LOG_PATH, "error.log")
        error_file_handler = logging.FileHandler(error_file_name)
        if not level:
            error_file_handler.setLevel(self.level)
        else:
            error_file_handler.setLevel(level)
        formatter = logging.Formatter(
            "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s"
        )
        error_file_handler.setFormatter(formatter)
        self.addHandler(error_file_handler)

    def resetName(self, name):
        """
        Reset the logger's name and update the file handler.
        """
        self.name = name
        self.removeHandler(self.file_handler)
        self.__setFileHandler__()


def main():
    # Create a logger instance
    log = LogHandler("test", "INFO")
    log.info("this is test info msg")
    log.warning("this is test warning msg")
    log.error("this is test error msg")


if __name__ == "__main__":
    main()
