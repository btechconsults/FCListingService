# Read in date
import sys
import os
import re
import FCfunctions

def FindFCRecords(saledate,Month):

	oldfile = './auction.txt'
	newfile = './input.txt'

	my_list = []
	my_list = FCfunctions.CreateNewFile(oldfile,newfile,Month)

	# Build foreclose list

	maxnum = round(len(my_list)/14)
	print ("keys: ", )
	k = 0
	for i in range(1, maxnum - 1):
		m = i * 14
		# Address
		address 	 = my_list[m + 1]
		citystatezip = my_list[m + 2]
		strrecords = saledate + ',' +address + ',' + citystatezip
		print (": ",k,' ', strrecords)
		k = k + 1

	return k


def main(argv):

	month 	 = sys.argv[1]
	saledate = sys.argv[2]
	total = 0
	total = FindFCRecords(saledate,month)

	print ("1: Auction ")
	print ("Total number of records found on the Auction sites: ",total)

	
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)


