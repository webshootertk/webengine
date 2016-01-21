#!/usr/local/bin/python

import argparse
from bs4 import BeautifulSoup   
from html_cleaner import filtered_text
import os
import os.path
import requests
import shutil
from sys import argv, exit
import urllib
import urllib2

def download_images(collection, save):
    if not os.path.exists(save):
        os.makedirs(save)

    for image in collection:
         print "gathering %s" % image
         urllib.urlretrieve(image, os.path.join(save, os.path.basename(image)))

def get_imageFiles(path, save, domain):
    collection = []
    print "checking all files for images"
    print "this can take a bit..."

    for f in os.listdir(path):
        infile = open(os.path.join(path, f)).read()
        soup = BeautifulSoup(infile)
        imgs = soup.findAll("img")
        for img in imgs:
            if "http://" in img['src'] or "https://" in img['src']:
                imgURL = img['src']
            else:
                if img['src'][0] == "/":
                    imgURL = domain + img['src']
                else:
                    imgURL = domain + "/" + img['src']

            if imgURL not in collection:
                collection.append(imgURL)

    download_images(collection, save)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="saves all images from a collection of html (raw) pages")
    parser.add_argument("path", help="folder containing html (raw) files")
    parser.add_argument("save", help="folder to put image files")
    parser.add_argument("domain", help="site domain")

    args = parser.parse_args()

    if not os.path.exists(args.path):
        stderr.write("folder %s not found." % args.path)
        exit()

    resp = requests.get(args.domain)
    if resp.status_code >= 400:
        stderr.write("Sorry, domain unavailable")
        exit()

    if get_imageFiles(args.path, args.save, args.domain):
        print "Error"
    else:
        print "Done"
