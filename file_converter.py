#!/usr/local/bin/python

import argparse
from bs4 import BeautifulSoup   
import html2text
from html_cleaner import filtered_text
import os
import os.path
import shutil
from sys import argv, exit

def get_convertedFiles(path, save, ext):

    if not os.path.exists(save):
        os.makedirs(save)
    
    file_ext = ".md"
    if ext is "html":
        file_ext = ".html"

    for f in os.listdir(path):
        extension = os.path.splitext(f)[1]
        if extension not in (".md", ".py", ".pyc", ".pdf"):
            print "converting file %s" % f
            infile = open(os.path.join(path, f)).read()
            h2t = html2text.HTML2Text()
            content = h2t.handle(infile)
            if extension == ".html":
                fileName = f[0:len(f) -5] + file_ext
            else:
                fileName = f + ".md"
            outfile = open(os.path.join(save, fileName), "w")
            outfile.write(content.encode("ascii", "xmlcharrefreplace"))
            outfile.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="converts html (raw) files to markdown")
    parser.add_argument("path", help="folder containing a html (raw) files")
    parser.add_argument("save", help="folder to put markdown files")
    parser.add_argument("ext", help="html of md")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        stderr.write("folder %s not found." % args.path)
        exit()

    if get_convertedFiles(args.path, args.save, args.ext):
        print "Error"
    else:
        print "Done"
