# Read in date
import sys
import os
import re

def month_converter(month):
	months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	return months.index(month) + 1

def FindFCRecords(inputfile):

	with open(inputfile, "r") as infile:
		data = infile.read()  # Read the contents of the file into memory.

	datalist = data.splitlines()
	# Build foreclose list

	k = 0
	for line in datalist:
		if line.find('foreclosures') > 1:
			print (": ",k, line)
		k = k + 1

	return k


def main(argv):

	month = sys.argv[1]
	inputfile = './data/' + month + '/auction.txt'

	sum  = FindFCRecords(inputfile)

	print ("1: Auction ")
	print ("Total number of records found on the Auction sites: ",sum)

	
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)


