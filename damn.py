from time import sleep

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.amazon.co.jp/s?k=python&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=35TODDLQ4TZI4&sprefix=python%2Caps%2C244&ref=nb_sb_noss_1"
r = requests.get(url, timeout=3)
r.raise_for_status

soup = BeautifulSoup(r.content, "lxml")

a_tags = soup.select_oen("span:-soup-contains('python')")
print(a_tags)
