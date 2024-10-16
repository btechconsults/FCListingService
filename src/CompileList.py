# Read in date 
import sys
import os
import re
import CheckDupList
import shutil

from os import listdir
from os.path import isfile, join

def AddRecords(filename,month):

	buildfile = "../target/" + month + "/" + filename
	with open(buildfile, "r") as datefile:
		data = datefile.read()  # Read the contents of the file into memory.
	datalist = data.splitlines()

	# Remove duplicate records by address
	outputfile = "../target/" + month + "/fc-final-results.csv"
	outfile = open(outputfile,'a+')
		
	k = 0
	for line in datalist:
		strLine = line + "\n"
		outfile.write(strLine)
		k = k + 1 
								
	datefile.close()
	outfile.close()
	
	return k
	
def main(argv):

	month 	  = sys.argv[1]
	day   	  = sys.argv[2]
	nextmonth = sys.argv[3]

	filename = '../target/' + month + '/fc-Mailer-' + month + '.csv'
	# Remove old target file
	if os.path.exists(filename):
		os.remove(filename)

	reportfile = '../data/FCsourcelist.txt'
	# Add  row to final output
	rptfile = open(reportfile,'w')
	
	
	results = 0
	fctotal = 0
	i = 0
	
	mypath="../target/" + month
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

	print ("---------------------------------------------------------- ")
	print (" ")
	print (" The following sites were used to target this month's mailer")
	
	strRecord = month + '|' + day
	rptfile.write(strRecord + '\n')

	for fname in onlyfiles:
		sum = AddRecords(fname,month)
		fctotal = fctotal + sum
		i = i + 1
		if fname.find('01') > -1:
			strRecords = '	1' + '-Auction		' + str(sum)			
			print(strRecords)
			strRecord = 'Action|http://www.auction.com|Foreclosure listing site|/fc-final-' + month + '-01.csv|' + str(sum)		
			rptfile.write(strRecord + '\n')
			
		if fname.find('02') > -1:
			strRecords = '	2' + '-ForeclosureBidslist	' + str(sum)
			print(strRecords)
			strRecord = 'ForeclosureBidslist|https://www.foreclosurebidslist.com/|Foreclosure listing site|/fc-final-' + month + '-02.csv|' + str(sum)
			rptfile.write(strRecord + '\n')
			
		if fname.find('03') > -1:
			strRecords = '	3' + '-McCallaRaymer		' + str(sum)
			print(strRecords)
			strRecord = 'McCalla & Raymer, LLP|http://www.foreclosurehotline.net/' + '|Law Firm|/fc-final-' + month + '-03.csv|' + str(sum) 		
			rptfile.write(strRecord + '\n')

		if fname.find('04') > -1:
			strRecords = '	4' + '-BrockScott		' + str(sum)
			print(strRecords)
			strRecord = 'Brock & Scott,LLP|https://www.brockandscott.com/foreclosure-sales/?_sft_foreclosure_state=ga|Law Firm|/fc-final-' + month + '-05.csv|' + str(sum) 	
			rptfile.write(strRecord + '\n')
			
		if fname.find('05') > -1:
			strRecords = '	5' + '-Adridgepite		' + str(sum)
			print(strRecords)
			strRecord = 'Adridgepite|http://saleday.aldridgepite.com/Listings|Law Firm|/fc-final-' + month + '-06.csv|' + str(sum) 
			rptfile.write(strRecord + '\n')
			
		if fname.find('06') > -1:
			strRecords = '	6' + '-RubinLublin		' + str(sum)
			print(strRecords)
			strRecord = 'Rubin & Lublin,LLP|http://rubinlublin.com/property-listing/georgia-property-listings/|Law Firm|/fc-final-' + month + '-07.csv|' + str(sum) 
			rptfile.write(strRecord + '\n')

	print('---------------------------------------')
	print('Total number of records		',fctotal)

	dupls,names,total = CheckDupList.CheckDup(month,nextmonth)

	strRecord = str(dupls)
	rptfile.write(strRecord)
	
	rptfile.close()
	
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

	
