import logging
import logging.handlers

# create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# create handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

fh = logging.handlers.RotatingFileHandler("file.log", mode="a", maxBytes=10485760, backupCount=4, encoding='utf-8') 
fh.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s [line:%(lineno)s] - %(funcName)s - %(message)s")

# add formatter
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add handler
logger.addHandler(ch)
logger.addHandler(fh)

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")