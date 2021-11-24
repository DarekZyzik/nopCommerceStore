import logging
from pathlib import Path

p = Path(r'C:\Users\Daro\PycharmProjects\nopCommerceStore\Configurations\log.txt')

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=r'C:\Users\Daro\PycharmProjects\nopCommerceStore\Configurations\log.txt',
                            level=logging.INFO,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        # logger.setLevel(logging.INFO)
        return logger
