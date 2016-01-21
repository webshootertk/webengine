#!/usr/local/bin/python

import argparse
from bs4 import BeautifulSoup
import os
import os.path
from random import randint
import requests
import shutil
import sys
from sys import argv, exit
import time
import urlparse

def get_filesFromList(urlFile, save):
    print "--------------------------------"
    print "this function is slow on purpose"
    print "--------------------------------"

    files = save
    resp = ""

    if not os.path.exists(files):
        os.makedirs(files)

    file_to_read = open(urlFile)
    infile_contents = file_to_read.readlines()
    file_to_read.close()
    count = 0
    total = len(infile_contents)

    for line in infile_contents:
    
        time.sleep(randint(2,9))
        count += 1
        try:
            line = line[:-1]
            resp = requests.get(line)
            if resp.status_code >= 400:
                print "Sorry, error occurred getting %s" % line
                print "Status Code: %s" % resp.status_code
                continue
    
            title = urlparse.urlparse(line).path
            # "/wiki/" = 6  
            title = title[6 : len(title)]
            title = title.replace("/", "|")
            text = resp.text
            print "Saving file %s (%d of %d)" % (title, count, total)
            file_to_write = open(os.path.join(files, title), "w")
            file_to_write.write(text.encode("ascii", "xmlcharrefreplace"))
            file_to_write.close()
        
        except: 
            print "exception file: %s" % line
            print "Status Code: %s" % resp.status_code
            print sys.exc_info()[0]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="gets all files from a list of urls")
    parser.add_argument("urlFile", help="file containing a list of urls")
    parser.add_argument("save", help="folder name to save htlm (raw) files in")

    args = parser.parse_args()

    if not os.path.exists(args.urlFile):
        stderr.write("Input file %s not found." % args.urlFile)
        exit()

    if get_filesFromList(args.urlFile, args.save):
        print "Error"
    else:
        print "Done"
