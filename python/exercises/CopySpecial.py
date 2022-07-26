"""CopySpecial
Exercise
The copyspecial.py program takes one or more directories as its arguments. We'll say that a "special" file is one 
where the name contains the pattern __w__ somewhere, where the w is one or more word chars. 
The provided main() includes code to parse the command line arguments, but the rest is up to you. 
Write functions to implement the features below and modify main() to call your functions.

Suggested functions for your solution(details below):

    get_special_paths(dir) -- returns a list of the absolute paths of the special files in the given directory
    copy_to(paths, dir) given a list of paths, copies those files into the given directory
    zip_to(paths, zippath) given a list of paths, zip those files up into the given zipfile

Part A (manipulating file paths)

Gather a list of the absolute paths of the special files in all the directories. 
In the simplest case, just print that list (here the "." after the command is a single argument indicating the current directory). 
Print one absolute path per line.



We'll assume that names are not repeated across the directories (optional: check that assumption and error out if it's violated).

Part B (file copying)
If the "--todir dir" option is present at the start of the command line, do not print anything and instead copy the files to the given directory, 
creating it if necessary. Use the python module "shutil" for file copying.


Part C (calling an external program)

If the "--tozip zipfile" option is present at the start of the command line, run this command: "zip -j zipfile <list all the files>". 
This will create a zip file containing the files. Just for fun/reassurance, also print the command line you are going to do first (as shown in the lecture). 
(Windows note: windows do not come with a program to produce standard .zip archives by default, but you can get download the free and 
open zip program from www.info-zip.org.)

If the child process exits with an error code, exit with an error code and print the command's output. 
Test this by trying to write a zip file to a directory that does not exist.
"""

 
import sys
import re
import os
import shutil
import subprocess

#Copy Special exercise

# +++your code here+++
# Write functions and modify main() to call them

def list_dir_files(dir):
  res = []
  try:
    files = os.listdir(dir)
  except NotADirectoryError:
    files = os.listdir('.') 
  for x in files:
    match = re.search(r'__(\w+)__', x)
    if(match):
      res.append(os.path.abspath(os.path.join(dir, x)))
  return res

def copy(c_dirs, todir):
  if(os.path.isdir(todir)):
    for path in c_dirs:
      fname = os.path.basename(path)
      shutil.copy(path, os.path.join(todir, fname))
  else:
    os.mkdir(todir)
    for path in c_dirs:
      fname = os.path.basename(path)
      shutil.copy(path, os.path.join(todir, fname))
  return 0

def zip(c_dirs, tozip):
  cmd = 'zip -j '+tozip+' '+''.join(c_dirs)
  print('c_dirs: ',c_dirs)
  print('To zip:',tozip)
  print('Command: ',cmd)
  stat = subprocess.run(cmd)
  try:
    subprocess.check_output(stat)
  except subprocess.CalledProcessError as e:
    print(e.stderr)
  return 0

def main():
  # This basic command-line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)

  c_dirs = []
  #dirs = list_dir_files(c_dirs)
  temp = [args[2:]]
  for x in temp:
    c_dirs.extend(x)
    print(x,"\n")
  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  tozip = ''

  if args[0] == '--todir':
    todir = args[1]
    #del args[0:2]
  elif args[0] == '--tozip':
    tozip = args[1]
    #del args[0:2]
  else:
    print("error: must specify one or more dirs")
    sys.exit(1)

  
  if(todir != ''):
    copy(c_dirs, todir)
  elif(tozip != ''):
    zip(c_dirs, tozip)
  else:
    for x in c_dirs:
      print(x+"\n")
  # +++your code here+++
  # Call your functions
 
if __name__ == "__main__":
  main()