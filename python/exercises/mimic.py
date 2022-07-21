"""Mimic Python exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file. 
Rather than read the file line by line, it's easier to read it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file to a list of all the words that immediately follow that word in the file. 
The list of words can be in any order and should include duplicates. 
So for example the key "and" might have the list ["then", "best", "then", "after", ...] listing all the words which came after "and" in the text. 
We'll say that the empty string is what comes before the first word in the file.

With the mimic dict, it's fairly easy to emit random text that mimics the original. 
Print a word, then look up what words might come next and pick one at random as the next work.
Use the empty string as the first word to prime things. 
If we ever get stuck with a word that is not in the dict, go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a random. choice(list) method which picks a random element from a non-empty list.

For fun, feed your program to itself as input. Could work on getting it to put in linebreaks around 70 columns, so the output looks better.
"""

import random
import sys


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    fi = open(filename, 'r')
    words = fi.read()
    fi.close()
    wordList = list(words.split())
    wordList = ['']+wordList+['']
    mimic_d = dict.fromkeys(wordList,[])
    mimic_d['']=[wordList[1]]
    for i in range(1,len(wordList)):
      try:
          m = wordList[i]
          n = wordList[i+1]
          if(m in mimic_d):
            mimic_d[m]= mimic_d[m]+[n]
          else:
            mimic_d[m] = n
      except IndexError:
        break		
    #print(mimic_d)
    return mimic_d	
    #a=wordList[10]
    #print("OUTPUT:    ",a)
    #print(wordList,"\n")
    #print("NEW INDEX HERE \n \n")
    #print("KEY INTENDED:{0}".format(wordList[i]))
    #print("DICT[KEY]={0}".format(mimic_d[wordList[i]]))
    #print(i,"APPENDED TO KEY={0}:VALUE={1} \n\n".format(mimic_d[wordList[i]],wordList[i]))
    #mimic_d['{0}'.format(a)]=wordList[2]
    #print(wordList[2])
    #mimic_d[a].append(wordList[1])
    #print(mimic_d)
    #mimic
    # for i in range(0,len(wordList)):
    #   mimic_d[wordList[i]] = []
    
    # for i in range(0,len(wordList)):
    #   for j in range(i,len(wordList)):
    #     try:
    #       mimic_d[wordList[i]].append(wordList[j+1])
    #     except IndexError:
    #       break
                
    #temp = list(mimic_d)
    # for i in range(1,len(wordList)):
    #   try:
    #     if(wordList[i] in mimic_d):
    #         mimic_d[wordList[i]].append(wordList[i+1])
    #         #print("KEY INTENDED:{0}".format(wordList[i]))
    #         #print("DICT[KEY]={0}".format(mimic_d[wordList[i]]))
    #         #print(i,"APPENDED TO KEY={0}:VALUE={1} \n\n".format(mimic_d[wordList[i]],wordList[i]))
    #     else:
    #         mimic_d[wordList[i]] = wordList[i+1]
    #         #print("NEW INDEX HERE \n \n")
    #   except IndexError:
    #     break
    #print(mimic_d['those'])
    #print(mimic_d['time'])

    # print(mimic_d)
    # fp = open('output.txt','x')
    # text = str(mimic_d)


#global gi; gi =0
def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  #for gi in range(200):
  rand_word = random.choice(mimic_dict[word])
    #print(mimic_dict[word])
  #print(rand_word,"\n")
    #print_mimic(mimic_dict,rand_word)
    #fp = open("temp_mi")
  # +++your code here+++
  return rand_word


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print ('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  word_new = print_mimic(dict, '')
  print("1 ",word_new)
  
  c=1
  while(c<200):
    word_new= print_mimic(dict,word_new)
    print(c+1,"",word_new)
    c+=1


if __name__ == '__main__':
  main()

