import os

class Config(object):
    SECRET_KEY = (os.environ.get("SECRET_KEY") or 
        "blooskyntattoo_by_clement_bonnet_for_clara_tonnele")