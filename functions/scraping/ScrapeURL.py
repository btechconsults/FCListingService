# Read in date 
import sys
import os
import requests
import string
import re
import shutil

from bs4 import BeautifulSoup
from lxml import html


def ScrapeForeHtml():

	URL = 'https://foreclosurebidslist.com/foreclosures/ga/barrow'

	# Read data from URLforeclosure
	r = requests.get(URL)

	soup= BeautifulSoup(r.text,'lxml')

	print(soup)

	i = 0
	return i
	
	
def main(argv):

	sum = 0
	results = ScrapeForeHtml()

# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)
