# Read in date
import io
import sys
import os
import requests
from bs4 import BeautifulSoup
from lxml import html


def ScrapeForeHtml():


	resp = requests.get('https://www.realtytrac.com/mapsearch/la/saint-tammany-county-foreclosures.html')

	with io.open('data.xml', "w", encoding="utf-8") as f:
		f.write(resp.text)

	return 1
	
	
def main(argv):

	sum = 0
	results = ScrapeForeHtml()

# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)
