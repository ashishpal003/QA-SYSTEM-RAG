## Here I am testing for logger setup
from src.logger import logging

print("Starting a test logging session....")
print("Please check for a log folder.")
logging.info('This is a test log.')

## Here I am testing for exception setup
from src.exceptions import MyCustomeException
import os
import sys

try:
    a = 0
    b = 10

    c = b/a
except Exception as e:
    logging.exception(MyCustomeException(e, sys), exc_info=False)
    raise MyCustomeException(e, sys)