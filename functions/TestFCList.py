# Read in date
import sys
import os
import re

def title_except(s, exceptions):
	word_list = re.split(' ', s)       #re.split behaves as expected
	final = [word_list[0].capitalize()]
	for word in word_list[1:]:
		final.append(word in exceptions and word or word.capitalize())
	return " ".join(final)

def month_converter(month):
	months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	return months.index(month) + 1

def FindFCRecords(Month, Year):


	inputfile = 'data/' + Month + '/auction.txt'
	
	with open(inputfile, "r") as infile:
		data = infile.read()  # Read the contents of the file into memory.

	my_list = data.splitlines()

	# Build foreclose list

	maxnum = round(len(my_list)/15)
	print ("keys: ", )
	k = 0
	for i in range(1, maxnum):
		m = i * 15
		# Address
		address = my_list[m + 2]
		address = title_except(address,"")
		# City State Zipcode
		citystatezip = my_list[m + 3]
		citystatezip = citystatezip.split(",")
		city 	 = citystatezip[0]
		city = title_except(city,"")
		#zip = citystatezip[1].split(" ")
		# County
		county	 = citystatezip[2].rsplit(' ', 1)[0]
		# Sale date
		saledate 	 = my_list[m + 4]
		saledate = saledate.split(",")
		# Build string
		#  + str(zip[2])
		strrecords =  '"' + saledate[0] + ',' + Year + '",' + address + ',' +  city + ',GA,' + ',Homeowner,' + county
		print (": ",k, strrecords)
		k = k + 1

	return k


def main(argv):

	year 	= sys.argv[2]
	month	= sys.argv[1]
	sum   = 0

	sum  = FindFCRecords(month,year)

	print ("1: Auction ")
	print ("Total number of records found on the Auction sites: ",sum)

	
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)


