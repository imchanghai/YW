from urllib.request import urlopen
from bs4 import BeautifulSoup
from xml.dom import minidom
import os 
import datetime
import subprocess



#write XML code to file system
xml_str = "this is test1".encode()

save_path_file = "suzhoutest.xml"

with open(save_path_file, "wb") as f:
    f.write(xml_str) 
    
