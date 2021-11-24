from configparser import ConfigParser

parser = ConfigParser()
parser.read(r'C:\Users\Daro\PycharmProjects\nopCommerceStore\Configurations\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = parser['common info']['baseURL']
        return url

    @staticmethod
    def getUseremail():
        username = parser['common info']['useremail']
        return username

    @staticmethod
    def getPassword():
        password = parser['common info']['password']
        return password







