# Read in date 
import sys
import os
import re
import shutil

from os import listdir
from os.path import isfile, join 

def FindMRRecords(Month,filename):

	# Add records records by address
	outputfile = './target/' + Month + '/fc-final-' + Month + '.csv'
	outfile = open(outputfile,'w+')

	with open(filename, "r") as inputfile:
		data = inputfile.read()  # Read the contents of the file into memory.
	datalist = data.splitlines()

	i = 0
	count = 1


	maxnum = round(len(datalist)/3)

	for i in range(1, maxnum):
		m = i * 3

	   # saledate, Address, and State
		rec1 = datalist[m + 0]
		rec1 = rec1.split(',')

		saledate = rec1[1]
		address  = rec1[2]
		county   = rec1[3]

		list = datalist[m + 1]
		list = list.split(',')
		cityzip = list[2].split(' ')
		if len(cityzip) > 3:
			city = cityzip[0] + ' ' + cityzip[1]
			zip  = cityzip[3]
		else:
			city = cityzip[0]
			zip  = cityzip[2]

		strRecord = saledate + ',' + address + ',' + city + ',GA,' + zip + ',Homeowner,' + county + '\n'

		#print(count,': ',strRecord)
		outfile.write(strRecord)
		count = count + 1

	outfile.close()

	return count
	
def main(argv):

	sum = 0	
	total = 0
	
	Month    = sys.argv[1]

	directory = './target/' + Month 
	if not os.path.exists(directory):
		os.makedirs(directory)		

	datadir = './data/' + Month
	if not os.path.exists(datadir):
		os.makedirs(datadir)

	filename = './data/' + Month + '/input.csv'

	total = FindMRRecords(Month,filename)

	print ("------------------------------------------------ ")
	print ('3 MaCalla & Raymer ')
	print (" ")
	print ('The total number of records found: ',total-1)
	print (" ")

	src  = './target/' + Month + '/fc-final-' + Month + '.csv'
	dest = '../../target/' + Month + '/fc-final-' + Month + '-03.csv'
		
	shutil.copy2(src,dest)

	reportfile = '../../target/' + Month + '/FCreport.csv'
	# Add  row to final output
	rptfile = open(reportfile,'a+')

	strRecord ='MaCalla & Raymer|' + str(total) + '|' + 'http://www.foreclosurehotline.net/Foreclosure.aspx|' + './3-McCallaRaymer/target/' + Month +  '/fc-final-' + Month  + '-.csv'
	rptfile.write(strRecord + '\n')

# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

	
