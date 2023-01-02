import sys
import os
F_NAME = "data.txt"

# clear the datafile's text
def clearData():
    with open(F_NAME, 'w'):
        pass

# parsing cli arguments
for i in range(1, len(sys.argv)):
    if(sys.argv[i] == "-c"):
        clearData()
    if(sys.argv[i] == "-fn"):
        F_NAME = sys.argv[i+1]

# now creating vector for word storage, and traversing file contents 

try:
    with open(F_NAME, 'r') as f:
        print("a")
except IOError:
    print("File '" + F_NAME + "' not found.")
