import sys
import os
import re

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


filename = './fc-Mailer-Jan.csv'
nextdate = '02/04/2020'

numvalue = CountField(filename,nextdate)
print('The of records found for month ', nextdate,' is',numvalue)


