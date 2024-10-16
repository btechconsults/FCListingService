# Build Georgia listing

import sys
import os
import shutil

from os import listdir
from os.path import isfile, join

from configparser import ConfigParser

def main(argv):
	# instantiate add the month
	config = ConfigParser()

	# parse existing file
	config.read('Config.ini')	
	
	# Read paths from a section

	V_Month = config.get('FC_LISTING', 'Month') 		
	# Remove files

	mypath = '../target/' + V_Month
	if not os.path.exists(mypath):
		os.makedirs(mypath)	
			
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

	print ('Removing previous build files')
	
	for fname in onlyfiles:
		filename = '../target/' + V_Month + '/' + fname
		print (filename)
		os.remove(filename)

	reportfile = '../target/' + V_Month + '/FCreport.csv'
	if os.path.exists(reportfile):
		os.remove(reportfile)
	weblistfile = '../target/' + V_Month + '/FCreportGA.txt'
	if os.path.exists(weblistfile):
		os.remove(weblistfile)

# Initiate main program	
if __name__ == "__main__":
	main(sys.argv)
