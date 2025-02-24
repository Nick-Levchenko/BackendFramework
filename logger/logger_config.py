import logging
import os


class LoggerConfig:
    LOGS_DIRECTORY = "logs"
    LOGGER_NAME = "Logger"
    LOGS_FILENAME = LOGS_DIRECTORY + os.sep + "api.log"
    LOGS_LEVEL = logging.INFO
    MAX_BYTES = 100000
    BACKUP_COUNT = 10
    FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
