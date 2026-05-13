import logging

# 1. Setup the format and level
logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s', level=logging.WARNING)

# 2. Fire the message
logging.warning('This is a warning')
