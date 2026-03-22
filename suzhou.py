from urllib.request import urlopen
from bs4 import BeautifulSoup
from xml.dom import minidom
import os 
import datetime
import gzip



#write XML code to file system
xml_str = datetime.datetime.now() + datetime.timedelta(hours=8)
xml_str = xml_str.isoformat().encode()
save_path_file = "suzhoutest.xml"

with open(save_path_file, "wb") as f:
    f.write(xml_str) 
    
f = gzip.open('suzhoutest.xml.gz', 'wb')
f.write(xml_str)
f.close()
