from configparser import ConfigParser

def config_parser():
    cfg = ConfigParser()
    cfg.read('../FilesDirectory1/objectConfig.ini', encoding="utf8")
    return cfg
