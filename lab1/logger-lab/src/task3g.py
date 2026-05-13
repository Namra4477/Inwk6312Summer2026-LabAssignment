import logging

# 1. Setup: Create logger and add a console handler in one go
logger = logging.getLogger('example_logger2')
logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s')

# 2. Action: Send your message
logger.warning('This is a warning')
