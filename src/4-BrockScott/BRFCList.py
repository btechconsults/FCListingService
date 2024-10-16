# Read in date
import sys
import os
import requests
import string
import re
import shutil

from bs4 import BeautifulSoup
from lxml import html


def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())

   return " ".join(final)

def SplitLocation(Location,StreetType):

	street = ''
	city   = ''

	for type in StreetType:
		if Location.find(type) > -1:
			address = Location.split(type)
			if len(address) > 1:
				street = address[0] + ' ' + type
				city   = address[1]
				if city.find('AKA') > -1:
					city = ''
				break;

	return street,


def title_except(s, exceptions):
	word_list = re.split(' ', s)       #re.split behaves as expected
	final = [word_list[0].capitalize()]
	for word in word_list[1:]:
		final.append(word in exceptions and word or word.capitalize())

	return " ".join(final)

def SplitLocation(Location,StreetType):

	street = ''
	city   = ''

	for type in StreetType:
		if Location.find(type) > -1:
			address = Location.split(type)
			if len(address) > 1:
				street = address[0] + ' ' + type
				city   = address[1]
				if city.find('AKA') > -1:
					city = ''
				break;

	return street,city


def ScrapeForeHtml(month,Saledate,page,outfile):

	StreetTypefile = '../lookup/StreetType.txt'

	with open(StreetTypefile, "r") as datefile:
		data = datefile.read()  # Read the contents of the file into memory.
	typelist = data.splitlines()

	URL = 'https://www.brockandscott.com/foreclosure-sales/?_sft_foreclosure_state=ga&sf_paged=' + str(page)


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
		# Spilt street and city
		Street,City = SplitLocation(addresscity,typelist)
		zipval  = strvalue[1].split('<')
		zipval  = zipval[0].split(' ')
		zip = zipval[2]
		strRecord = Saledate + ',' + Street + ',' + City + ',GA,' +  zip  + ',Homeowner,' + '\n'
		#print (i,': ',strRecord)
		outfile.write(strRecord)
		i = i + 1

	return i


def main(argv):

	# Read data from Aldp
	try:
	
		month  	  = sys.argv[1]
		saledate  = sys.argv[2]
		pages	  = sys.argv[3]
		sum = 0

		directory = './target/' + month
		if not os.path.exists(directory):
			os.makedirs(directory)		

		# Build mailer file
		filename = './target/' + month + '/fc-final-' + month + '.csv'
		outfile = open(filename,'w')

		sum = 0
		total = 0
		for page in range(2, int(pages)):
			sum = ScrapeForeHtml(month,saledate,page,outfile)
			total = total + sum

		outfile.close()

		print ("------------------------------------------------ ")
		print ("4: Brock & Scoot")
		print ("")
		print ("The total number of records found on : ",total)
		print ("")

		src  = './target/' + month + '/fc-final-' + month + '.csv'
		dest = '../../target/' + month + '/fc-final-' + month + '-04.csv'
			
		shutil.copy2(src,dest) 
		
		reportfile = '../../target/' + month + '/FCreport.csv'
		# Add  row to final output
		rptfile = open(reportfile,'a')
		
		strRecord = 'Brack & Scott|' + str(sum) + '|https://www.brockandscott.com/foreclosure-sales/?_sft_foreclosure_state=ga'+ './4-BrockScott/target/' + month +  '/fc-final-' + month + '.csv'
		rptfile.write(strRecord + '\n')
		rptfile.close()


	except ValueError:
		print ("Oops!  That was not a valid URL.  Try again...")
		raise 
	
		
# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)
