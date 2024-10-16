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

	URL = 'view-source:https://rlselaw.com/property-listing/georgia-property-listings/'
	
	# Read data from URLforeclosure
	r = requests.get(URL)
	  		
	soup = BeautifulSoup(r.text,'lxml')

	i = 1
	fclist = []

	for table_row in soup.select(".property-listing tr"):
		table_cells = table_row.findAll('td')
		strvalue = str(table_cells)
		print(strvalue)
	
	return i

	
def main(argv):

	results = 0
	results = ScrapeForeHtml()


# Initiate main program
if __name__ == "__main__":
    main(sys.argv)
