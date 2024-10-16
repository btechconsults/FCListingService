import pyodbc
import urllib
xmlpath = "http://www.w3schools.com/xml/cd_catalog.xml"
xmlurl= urllib.urlopen(xmlpath)
xml_as_string = xmlurl.read()


cnxn = pyodbc.connect(
    'Trusted_Connection=yes; 
    DRIVER={SQL Server};
    SERVER=servername; 
    DATABASE=database_name; 
    UID=user; 
    PWD=pass'
) 
cursor = cnxn.cursor()
cursor.execute("insert into table values ('Text', 1, '"+ xml_as_string +"')") 
cnxn.commit()

