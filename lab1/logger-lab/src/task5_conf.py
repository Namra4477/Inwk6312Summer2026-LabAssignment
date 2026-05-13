import logging
import logging.config

logging.config.fileConfig(fname='task5.conf',
                          disable_existing_loggers=False)
logger = logging.getLogger('sampleLogger')
logger.debug('This is a debug message')
