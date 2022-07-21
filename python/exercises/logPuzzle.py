# Log Puzzle
# Exercise
# For the Log Puzzle exercise, you'll use Python code to solve two puzzles. This exercise uses the urllib module, as shown in the Python utility section. 
# The files for this exercise are in the "log puzzle" directory inside google-python-exercises (download the google-python-exercises.zip 
# if you have not already, see Set Up for details). Add your code to the "logpuzzle.py" file.

# An image of an animal has been broken into many narrow vertical stripe images. The stripe images are on the internet somewhere, each with its own URL. 
# The URLs are hidden in a web server log file. Your mission is to find the URLs and download all image stripes to re-create the original image.

# The slice URLs are hidden inside apache log files (the open-source Apache web server is the most widely used server on the internet). 
# Each log file is from some server, and the desired slice URLs are hidden within the logs. The log file encodes what server it comes from like this: 
# the log file animal_code.google.com is from the code.google.com server (formally, we'll say that the server name is whatever follows the first underbar). 
# The animal_code.google.com log file contains the data for the "animal" puzzle image. Although the data in the log files has the syntax of a real apache web server, 
# the data beyond what's needed for the puzzle is randomized data from a real log file.

# Here is what a single line from the log file looks like (this really is what apache log files look like):



# The first few numbers are the address of the requesting browser. The most interesting part is the "GET path HTTP" showing the path of a web request 
# received by the server. The path itself never contains spaces and is separated from the GET and HTTP by spaces (regex suggestion: \S (upper case S) 
# matches any non-space char). Find the lines in the log where the string "puzzle" appears inside the path, ignoring the many other lines in the log.

# Part A - Log File To Urls
# Complete the read_urls(filename) function that extracts the puzzle URLs from inside a logfile. Find all the "puzzle" path URLs in the log file. 
# Combine the path from each URL with the server name from the filename to form a full URL, e.g. "http://www.example.com/path/puzzle/from/inside/file". 
# Screen out URLs that appear more than once. The read_urls() function should return the list of full URLs, sorted in alphabetical order and without duplicates. 
# Taking the URLs in alphabetical order will yield the image slices in the correct left-to-right order to re-create the original animal image. 
# In the simplest case, main() should just print the URLs, one per line.

# $ ./logpuzzle.py animal_code.google.com


# ...


# Part B - Download Images Puzzle
# Complete the download_images() function which takes a sorted list of URLs and a directory. Download the image from each URL into the given directory, 
# creating the directory first if necessary (see the "os" module to create a directory, and "urllib.urlretrieve()" for downloading a URL). 
# Name the local image files with a simple scheme like "img0", "img1", "img2", and so on. You may wish to print a little "Retrieving..." 
# status output line while downloading each image since it can be slow and it's nice to have some indication that the program is working. 
# Each image is a little vertical slice from the original. How to put the slices together to re-create the original? 
# It can be solved nicely with a little HTML (knowledge of HTML is not required).

# The download_images() function should also create an index.html file in the directory with an *img* tag to show each local image file. 
# The IMG tags should all be on one line together without separation. In this way, the browser displays all the slices together seamlessly. 
# You do not need knowledge of HTML to do this; just create an index.html file that looks like this:



# Here's what it should look like when you can download the animal puzzle:



# When it's all working, opening the index.html in a browser should reveal the original animal image. What is the animal in the image?

# Part C - Image Slice Descrambling
# The second puzzle involves an image of a very famous place but depends on some custom sorting. For the first puzzle, 
# the URLs can be sorted alphabetically to order the images correctly. In the sort, the whole URL is used. However, 
# we'll say that if the URL ends in the pattern "-wordchars-wordchars.jpg", e.g. "", then the URL should be represented by the second word in the sort (e.g. "baaa").
# So sorting a list of URLs each ending with the word-word.jpg pattern should order the URLs by the second word.

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  fp = open(filename,'r')
  text = fp.read()
  fp.close()
  hostname = "http://"+filename.split('_')[1]
  links = []
  imgs = re.findall('([-\w]+\.(?:jpg|gif|png))', text)
  for x in imgs:
    links.append(hostname+imgs)
  return sorted(links)    
  # +++your code here+++
 

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
  os.chdir(dest_dir)

  image_tags = []

  for url in img_urls:
      image_name = url.split("/")[-1]
      response = urllib.request.urlopen(url)
      image = open(image_name, "wb")
      image.write(response.read())
      image_tags.append('<img src="{0}">'.format(image_name))

  html_file = open("index.html", "w")
  html_file.write("<html><body>{0}</body></html>".format(''.join(image_tags)))

  return 0
  # +++your code here+++
 

def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()