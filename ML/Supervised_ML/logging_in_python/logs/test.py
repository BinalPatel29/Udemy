from logger import logger

def add(a, b):
    logger.debug("The addition operation is taking place")
    return a + b

logger.debug("The addition function is called")
result = add(10, 15)
print("Result:", result)