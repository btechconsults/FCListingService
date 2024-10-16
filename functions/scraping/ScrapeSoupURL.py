# Read in date 
import sys
import os
import requests
import string
import re
import shutil
import io

from bs4 import BeautifulSoup
from lxml import html


def ScrapeForeHtml():

	URL = 'https://www.realtytrac.com/mapsearch/la/saint-tammany-county-foreclosures.html'
	r = requests.get(URL)

	soup = BeautifulSoup('html.parser').encode("utf-8")
	print(soup)

	return 1
	
	
def main(argv):

	sum = 0
	results = ScrapeForeHtml()

# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)
