# Read in date
import sys
import os
import re

def remove_line(auctionfile,nfile,month):

	the_list = ['Newly', 'Listed',month]
	with open(auctionfile) as oldfile, open(nfile, 'w') as newfile:
		for line in oldfile:
			if not any(bad_word in line for bad_word in the_list):
				newfile.write(line)

def CreateNewFile(oldfile,newfile,month):

	remove_line(oldfile,newfile,month)

	with open(newfile, "r") as infile:
		data = infile.read()  # Read the contents of the file into memory.

	my_list = data.splitlines()
	# Remove the new listing line

	print (len(my_list))
	# using remove() to
	# perform removal
	while("" in my_list) :
		my_list.remove("")

	return my_list
