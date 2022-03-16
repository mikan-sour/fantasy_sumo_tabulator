from .utils import *
from bs4 import BeautifulSoup

def get_soup(html):
    return BeautifulSoup(html,'html.parser')
