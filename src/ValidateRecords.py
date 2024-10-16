# Read in date 
import sys
import os
import re
from os import listdir
from os.path import isfile, join

def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   
   return " ".join(final)

def AddRecords(filename):

    buildfile = "./validate-records/" + filename
    with open(buildfile, "r") as datefile:
        data = datefile.read()  # Read the contents of the file into memory.
    datalist = data.splitlines()

    # Remove duplicate records by address
    outputfile = "./validate-records/fc-results.csv"
    outfile = open(outputfile,'a+')

    k = 0
    for line in datalist:
        strLine = line + "\n"
        outfile.write(strLine)
        k = k + 1

    datefile.close()
    outfile.close()

    return k

def CheckDup():

    fclistpath = './validate-records/fc-results.csv'

    # Build check for duplicate record in list
    k=1
    i=0
    t=0
    duplicate = []

    with open(fclistpath) as infile:
        seen = set()
        for line in infile:
            k=k+1
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
                else:
                    seen.add(address)
                    t = t + 1
                    #print(t,': ', address)
                # Build new list

    infile.close()
    os.remove(fclistpath)

    return k-1,t

def main(argv):

    fctotal = 0
    i = 0

    mypath="./validate-records/"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    for fname in onlyfiles:
        sum = AddRecords(fname)
        fctotal = fctotal + sum
        i = i + 1

    print("The number of files processed: ",i)
    k,t = CheckDup()
    print ("Total number of records found: : ",t)
    print ("Total number of duplicate records found: : ",k-t
           )


# Initiate main program
if __name__ == "__main__":
    main(sys.argv)


