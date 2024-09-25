from bs4 import BeautifulSoup
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import re

a = "ln mzk 0"
arg = "train"
card_type = "normal" if arg == "normal" else "after_training"
print(card_type)