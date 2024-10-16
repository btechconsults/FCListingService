# Read in date
import sys
import os
import re

def remove_line(auctionfile):

	the_list = ['Newly', 'Listed']
	with open(auctionfile) as oldfile, open('auction2.txt', 'w') as newfile:
		for line in oldfile:
			if not any(bad_word in line for bad_word in the_list):
				newfile.write(line)

def CreateNewFile():

	remove_line('auction.txt')

	inputfile = './auction2.txt'
	with open(inputfile, "r") as infile:
		data = infile.read()  # Read the contents of the file into memory.

	my_list = data.splitlines()
	# Remove the new listing line

	print (len(my_list))

	return my_list


my_list = CreateNewFile()
