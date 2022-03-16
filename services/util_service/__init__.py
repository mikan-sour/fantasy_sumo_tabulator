import os
from dotenv import dotenv_values

dir_path = os.path.dirname(os.path.realpath(__file__))
dotenv_path = os.path.join(dir_path,'..','..','.env')
config = dotenv_values(dotenv_path)

def getConfig():
    return config