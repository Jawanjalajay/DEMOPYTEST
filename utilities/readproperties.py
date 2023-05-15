import configparser

config = configparser.RawConfigParser()
config.read("D:\Pytest\pageObjects\config.ini")

class readconfig():
    @staticmethod
    def geturl():
        url=config.get('common info','url')
        return url

    @staticmethod
    def getusername():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password