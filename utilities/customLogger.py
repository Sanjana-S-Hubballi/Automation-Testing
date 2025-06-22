# import logging
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=".\\Logs\\automation.log",
#                             format='%(asctime)s: %(levelname)s: %(message)s', datefmt = '%m%d%Y %I:%M:%S %p')
#
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger

import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # Ensure Logs folder exists
        log_folder = os.path.join(os.getcwd(), "Logs")
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        log_path = os.path.join(log_folder, "automation.log")

        logger = logging.getLogger("nopCommerceLogger")

        if not logger.handlers:  # Prevent duplicate handlers
            file_handler = logging.FileHandler(log_path, mode='a')
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%Y %I:%M:%S %p')
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.setLevel(logging.INFO)

        return logger
