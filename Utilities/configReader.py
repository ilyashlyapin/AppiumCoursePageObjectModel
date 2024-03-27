import configparser


def readConfig(section, key):
    config = configparser.ConfigParser()
    config_file_path = '/Users/ilya/Documents/GitHub/appium-course/AppiumCoursePageObjectModel/ConfigurationData/conf.ini'
    config.read(config_file_path)
    return config.get(section, key)
