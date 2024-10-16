# Read in date
import sys
import os
import re
import FCfunctions

def FindFCRecords(Month, Year):

	oldfile = './data/' + Month + '/auction.txt'
	newfile = './data/' + Month + '/input.txt'

	my_list = []
	my_list = FCfunctions.CreateNewFile(oldfile,newfile)

	# Build foreclose list

	maxnum = round(len(my_list)/15)
	print ("keys: ", )
	k = 0
	for i in range(1, maxnum - 1):
		m = i * 15
		# Address
		address 	 = my_list[m + 1]
		citystatezip = my_list[m + 2]
		saledate     = my_list[m + 3]
		strrecords = address + ',' + citystatezip + ',' + saledate
		print (": ",k,' ', strrecords)
		k = k + 1

	return k


def main(argv):

	month	= sys.argv[1]
	year 	= sys.argv[2]
	sum   = 0


	sum  = FindFCRecords(month,year)

	print ("1: Auction ")
	print ("Total number of records found on the Auction sites: ",sum)

	
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)


