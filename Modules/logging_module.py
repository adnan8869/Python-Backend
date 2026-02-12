# import logging

# logging.basicConfig(filename='app.log', level=logging.DEBUG)
# def sum(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def mul(a, b):
#     return a * b


# add_result = sum(8, 3)
# logging.debug(f"Sum: {add_result}")

# sub_result = sub(5, 3)
# logging.debug(f"Subtraction: {sub_result}")

# mul_result = mul(5, 4)
# logging.debug(f"Multiplication: {mul_result}")




# import logging

# logging.basicConfig(filename='history.log', level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')


# def fun(val):
#     if val < 0:
#         raise ValueError("Invalid value: Value cannot be negative.")
#     else:
#         logging.info("Operation performed successfully.")


# try:
#     v1 = int(input("Enter a value: "))
#     fun(v1)
# except ValueError as ve:
#     logging.exception("Exception occurred: %s", str(ve))


import logging
from logging.handlers import RotatingFileHandler

# Create logger
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)  # Capture all levels

# -------------------------
# Formatter
# -------------------------
formatter = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)

# -------------------------
# File Handler: INFO logs
# -------------------------
info_handler = RotatingFileHandler(
    "app.log", maxBytes=5*1024*1024, backupCount=3
)
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)

# -------------------------
# File Handler: ERROR logs
# -------------------------
error_handler = RotatingFileHandler(
    "error.log", maxBytes=5*1024*1024, backupCount=3
)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

# -------------------------
# File Handler: DEBUG logs
# -------------------------
debug_handler = RotatingFileHandler(
    "debug.log", maxBytes=5*1024*1024, backupCount=3
)
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(formatter)

# -------------------------
# Add handlers to logger
# -------------------------
logger.addHandler(info_handler)
logger.addHandler(error_handler)
logger.addHandler(debug_handler)


# -------------------------
# Test Logs
# -------------------------

logger.debug("This is a debug message")
logger.info("Application started")
logger.warning("Low memory warning")
logger.error("Database connection failed")
logger.critical("System crash")



