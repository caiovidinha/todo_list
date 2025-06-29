import logging

LOG_FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logger(name: str = "todo") -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(LOG_FORMAT, datefmt=LOG_DATE_FORMAT)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(logging.INFO) 
    logger.propagate = False      

    return logger
