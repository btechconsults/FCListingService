# Read in date
import FCfunctions
import sys
import os
import re

def main(argv):

    oldfile	 = sys.argv[1]
    newfile  = sys.argv[2]

    my_list = []
    my_list = FCfunctions.CreateNewFile(oldfile,newfile)
    print (len(my_list))

# Initiate main program
if __name__ == "__main__":
    main(sys.argv)


