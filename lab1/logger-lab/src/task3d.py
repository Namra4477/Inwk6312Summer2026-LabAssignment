import logging

# Creating a custom logger using __name__
logger = logging.getLogger(__name__)

# This creates a logger named __main__ when run directly
logger.warning('This is a warning')
