import collections

# function to parse list into however many words/phrases desired
def CreateMultipleLists(word_list, words):
    newlist = []
    for i in range((len(word_list)) - (-1+words)):
        word = ""
        for j in range(words):
            word += word_list[i+j] + " "
        newlist.append(word)
    if(len(word_list) == 0):
        print("Invalid parameters. Try again.")
        quit()
    return newlist

# clear the datafile's text
def clearData(f_name):
    with open(f_name, 'w'):
        pass
    print("File has been cleared.")
    quit()

# sort the dictionary into a list, then reconvert to dict
def Organize(unsorted_dict):
    sorted_dict = sorted(unsorted_dict.items(), key=lambda x:x[1], reverse=True)
    return dict(sorted_dict)

