# Read in date
import sys
import os
import re
import shutil
import FCfunctions

def remove_line(infile,outfile):

    the_list = ['Newly', 'Listed']
    with open(infile) as oldfile, open(outfile, 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in the_list):
                newfile.write(line)
    return 1

def title_except(s, exceptions):
   word_list = re.split(' ', s)       #re.split behaves as expected
   final = [word_list[0].capitalize()]
   for word in word_list[1:]:
      final.append(word in exceptions and word or word.capitalize())
   return " ".join(final)


# Build forecloser list
def FindFCRecords(State,saledate,Month):

    builddir = './target/' + Month
    if not os.path.exists(builddir):
        os.makedirs(builddir)

    datadir = './data/' + Month
    if not os.path.exists(datadir):
        os.makedirs(datadir)

    filename = './target/' + Month + '/fc-final-' + Month + '.csv'
    outfile = open(filename,'a+')


    oldfile = './data/' + Month + '/auction.txt'
    newfile = './data/' + Month + '/input.txt'

    my_list = []
    my_list = FCfunctions.CreateNewFile(oldfile,newfile,Month)

   # Build foreclose list

    maxnum = round(len(my_list)/14)
    k = 0
	
    for i in range(1, maxnum):
        m = i * 14
        # Address
        # Address
        address = my_list[m + 1]
        address = title_except(address,"")

        citystatezip = my_list[m + 2]
        citystatezip = citystatezip.split(",")
        # Missing city and zip
        #print (citystatezip)
        if len(citystatezip) > 2:
            #print (citystatezip)
            city = citystatezip[0]
            city = title_except(city,"")
            zip = citystatezip[1].split(" ")
            county = citystatezip[2].split(' ')
            # Add record to mailer file
            k = k + 1
            strRecord = saledate + ',' + address + ',' +  city + ',' + State + ',' + str(zip[2]) + ',Homeowner,' + county[1] +  '\n'
            #print (": ",k, strRecord)
            outfile.write(strRecord)

    outfile.close()

 

    return k


def main(argv):

    State    = sys.argv[1]
    month 	 = sys.argv[2]
    saledate = sys.argv[3]
    total = 0

    filename = './target/' + month + '/fc-final-' + month + '.csv'
    # Remove old target file
    if os.path.exists(filename):
        os.remove(filename)

    toatl = 0
    total = FindFCRecords(State,saledate,month)

    print ("------------------------------------------------ ")
    print ("1: Auction ")
    print ("Total number of records found on the Auction site: ", total)
    print ("")

    reportfile = '../../target/' + month  + '/FCreportGA.txt'
        # Add  row to final output
    rptfile = open(reportfile,'a+')

    strRecord = 'Auction|' + str(sum) + '|' + 'https://www.Auction.com|'  + './1-Auction/target/' + month +  '/fc-final-Aug.csv'
    rptfile.write(strRecord + '\n')

    src  = './target/' + month + '/fc-final-' + month + '.csv'
    dest = '../../target/' + month + '/fc-final-' + month + '-01.csv'

    shutil.copy2(src,dest)

    reportfile = '../../target/' + month + '/FCreport.csv'
    # Add  row to final output
    rptfile = open(reportfile,'a+')

    strRecord ='Auction|' + str(total) + '|' + 'https://www.auction.com|' + './2-Auction/target/' + month +  '/fc-final-' + month  + '-.csv'
    rptfile.write(strRecord + '\n')

# Initiate main program	
if __name__ == "__main__":
    main(sys.argv)

	
