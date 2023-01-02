from funcs import *
from datavis import *
import sys
import os

F_NAME = "data.txt"
WORD_LIST = []
TOTAL_WORDS = 1

# parsing cli arguments
clear = False
for i in range(1, len(sys.argv)):
    if(sys.argv[i] == "-fn"):
        F_NAME = sys.argv[i+1]
    if(sys.argv[i] == "-w"):
        TOTAL_WORDS = int(sys.argv[i+1])

# now creating list for word storage, and traversing file contents 
try:
    with open(F_NAME, 'r') as f:
        for line in f:
            WORD_LIST.extend(line.split())
        print("List successfully generated.")
except IOError:
    print("File '" + F_NAME + "' not found.")
    quit()

for i in range(TOTAL_WORDS):
    word_list = CreateMultipleLists(WORD_LIST, i+1)
    c = collections.Counter(word_list)
    c = Organize(c)
    try:
        PlotData(c, str(i+1))
        print("Successfully created plot with " + str(i+1) + " word(s).")
    except IOError: 
        print("Error creating plot.")
        quit()