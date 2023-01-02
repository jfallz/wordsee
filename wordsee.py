import sys
import os
import collections

F_NAME = "data.txt"
WORD_LIST = []

# function to parse list into however many words/phrases desired
def CreateMultipleLists(word_list, words):
    newlist = []
    for i in range((len(word_list)) - (-1+words)):
        word = ""
        for j in range(words):
            word += word_list[i+j] + " "
        newlist.append(word)
    return newlist

# clear the datafile's text
def clearData():
    with open(F_NAME, 'w'):
        pass
    print("File has been cleared.")
    quit()

# parsing cli arguments
clear = False
for i in range(1, len(sys.argv)):
    if(sys.argv[i] == "-c"):
        clear = True
    if(sys.argv[i] == "-fn"):
        F_NAME = sys.argv[i+1]
if(clear) : clearData()

# now creating list for word storage, and traversing file contents 
try:
    with open(F_NAME, 'r') as f:
        for line in f:
            WORD_LIST.extend(line.split())
        print("List successfully generated.")
except IOError:
    print("File '" + F_NAME + "' not found.")
    quit()

word_list = CreateMultipleLists(WORD_LIST, 1)
if(len(word_list) == 0):
    print("Invalid parameters. Try again.")
    quit()
c = collections.Counter(word_list)
print(c)