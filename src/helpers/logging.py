# ----------------------------------------------------------------------
# File: src/helpers/logging.py
# Author: Gabriel Zacchi Braga (Owner)
# Date: 26 jun 2021
# Brief: Config module for logging system.
# ----------------------------------------------------------------------
import logging

# -----------------------------
# Set up wrapper logging
logging.getLogger().setLevel(logging.DEBUG)
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] [%(levelname)s] [%(funcName)s] [line %(lineno)d] - %(message)s ',
)
