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

def CountField(filename,nextdate):
	with open(filename, "r") as datefile:
		data = datefile.read()  # Read the contents of the file into memory.
	datalist = data.splitlines()

	k = 0

	for line in datalist:
		value = line.split(',')
		if value[0] == nextdate:
			k = k + 1

	return k

def CheckDup(salemonth,nextdate):

	fclistpath = '../target/' + salemonth + '/fc-final-results.csv'

	# Build check for duplicate record in list 
	k=1
	i=0
	t=0
	duplicate = []
	
	# Remove dupliacte records by address
	filename = '../target/' + salemonth + '/fc-Mailer-' + salemonth + '.csv'
	outfile = open(filename,'w')

	with open(fclistpath) as infile:
		seen = set()
		for line in infile:
			line_lower = line.lower()
			list = line_lower.split(",")
			if len(list) > 1:
				address=list[1]
				temp = address.split(" ")
				if len(temp) > 1:
					street = title_except(temp[1], "")
					address = temp[0] + street							
				else:
					address = temp[0]
					
				if address in seen:
					duplicate.append(address)
					k=k+1
				else:		
					seen.add(address)
					array_fc = line.split(",")					
					array_fc[2] = title_except(array_fc[2], "")					
					build_list =  ','.join(array_fc)
					outfile.write(line)
					t=t+1
					if "Homeowner" not in line:
						i=i+1
				# Build new list 		

	numvalue = CountField(filename,nextdate)

	print ("Total duplicate: ", k-1)
	h=t-i
	print('The of records found for month ', nextdate,' is',numvalue)
	print ("Total records without names: ", h)
	print ("Total records with names: ", i)
	print ("Total records: ", t)

	infile.close()
	outfile.close()
	os.remove(fclistpath)
	
	return k,h,t
	
	
	
