# Read in date
import sys
import os
import re
import shutil

def title_except(s, exceptions):
    word_list = re.split(' ', s)       #re.split behaves as expected
    final = [word_list[0].capitalize()]
    for word in word_list[1:]:
        final.append(word in exceptions and word or word.capitalize())

    return " ".join(final)

def FindFCRecords(month):

    fclistpath = './data/' + month + '/input.csv'


    # Build check for duplicate record in list
    k=1
    i=1
    fclisst = []
    # Remove dupliacte records by address
    filename = './target/' + month + '/fc-final-' + month + '.csv'
    outfile = open(filename,'w')

    with open(fclistpath) as infile:
        for line in infile:
            strvalue = str(line)
            fclist   = strvalue.split('\t')
            saledate = fclist[0]
            address = fclist[2]
            city    = fclist[3]
            zip		= fclist[4]
            county  = fclist[5]
            strRecord = saledate + ',' + address + ',' + city + ',GA,' + zip + ',Homeowner,' + county + '\n'
            #print(i,': ',strRecord)
            i = i  + 1
            outfile.write(strRecord)

    infile.close()
    outfile.close()

    return i
# os.remove(fclistpath)

def main(argv):

    # Read data from Aldp
    try:

        month  	 = sys.argv[1]

        total = 0

        directory = './target/' + month
        if not os.path.exists(directory):
            os.makedirs(directory)

        directory = './data/' + month
        if not os.path.exists(directory):
            os.makedirs(directory)

        total = FindFCRecords(month)

        print ("------------------------------------------------ ")
        print ("6: RubinLublin")
        print (" ")
        print ("Total numbers records found on this site: ",total)
        print (" ")

        reportfile = '../../target/' + month  + '/FCreportGA.txt'
        # Add  row to final output
        rptfile = open(reportfile,'a+')

        strRecord = 'RubinLublin|' + str(sum) + '|' + 'https://www.Auction.com|'  + './6-RubinLublin/target/' + month +  '/fc-final-Aug.csv'
        rptfile.write(strRecord + '\n')

        src  = './target/' + month + '/fc-final-' + month + '.csv'
        dest = '../../target/' + month + '/fc-final-' + month + '-06.csv'

        shutil.copy2(src,dest)

        reportfile = '../../target/' + month + '/FCreport.csv'
        # Add  row to final output
        rptfile = open(reportfile,'a+')

        strRecord ='RubinLublin|' + str(total) + '|' + 'https://rlselaw.com/property-listing/georgia-property-listings/|' + './6-RubinLublin/target/' + month +  '/fc-final-' + month  + '-.csv'
        rptfile.write(strRecord + '\n')

    except ValueError:
        print ("Oops!  That was not a valid URL.  Try again...")
        raise


    # Initiate main program
if __name__ == "__main__":
    main(sys.argv)
