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

	URL = 'https://www.brockandscott.com/foreclosure-sales/?_sft_foreclosure_state=ga&sf_paged=2'
	
	# Read data from URLforeclosure
	r = requests.get(URL)
	  		
	soup = BeautifulSoup(r.text,'lxml')

	i = 1
	fclist = []
	for div_row in soup.select(".content"):
		div_cells   = div_row.findAll('p')	
		strvalue    = str(div_cells[11])
		strvalue = strvalue.split(',')
		addresscity  = strvalue[0].replace('<p>','')
		zipval  = strvalue[1].split('<')
		zipval  = zipval[0].split(' ')
		zip = zipval[2]
		print(addresscity,',', zip)

		i = i + 1

	return i

	
def main(argv):

	results = 0
	results = ScrapeForeHtml()


# Initiate main program
if __name__ == "__main__":
    main(sys.argv)
