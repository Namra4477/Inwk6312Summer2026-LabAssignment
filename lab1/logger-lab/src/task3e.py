import logging


logger = logging.getLogger('example_logger')
logger.warning('This is a warning')

logger2 = logging.getLogger('example_logger2')
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
handler.setFormatter(formatter)
logger2.addHandler(handler)
logger2.warning('This is a warning')


logger3 = logging.getLogger(__name__)
logger3.addHandler(handler)
logger3.warning('This is a warning using __name__')
