import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=r'C:\Users\Daro\PycharmProjects\nopCommerceStore\Logs\log.txt',
                            filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.DEBUG)
        logger = logging
        return logger

