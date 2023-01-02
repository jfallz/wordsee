import sys
import os

F_NAME = "data.txt"
WORD_LIST = []

# clear the datafile's text
def clearData():
    with open(F_NAME, 'w'):
        pass
    print("File has been cleared.")

# parsing cli arguments
for i in range(1, len(sys.argv)):
    if(sys.argv[i] == "-c"):
        clearData()
    if(sys.argv[i] == "-fn"):
        F_NAME = sys.argv[i+1]

# now creating vector for word storage, and traversing file contents 
try:
    with open(F_NAME, 'r') as f:
        for line in f:
            WORD_LIST.extend(line.split())
        print("List successfully generated.")
except IOError:
    print("File '" + F_NAME + "' not found.")
