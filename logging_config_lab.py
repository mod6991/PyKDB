import logging
import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger()

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")