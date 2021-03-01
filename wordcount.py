# define a function which takes in a textfile and returns the words in it and their count
# open the textfile
# for each word make a list using the dictionaries
# return that

# put your code here.
import sys 

def wordcount(textfile):
    """counting words"""
    datafile = open(textfile)
    
    word_count = {}
    for line in datafile:
        line = line.strip()
        words = line.split(" ")
        for word in words:
            word = word.strip("\\,.!?-#$%^&();:_/")
            word = word.lower()
            word_count[word] = word_count.get(word, 0) + 1

    print(word_count)

    return word_count

# wordcount('test.txt')
wordcount('test.txt')
# print("This is the name of the program:", 
#        sys.argv[0])

add = 0.0
  
# Getting the length of command 
# line arguments 
n = len(sys.argv) 
  
for i in range(1, n): 
    add += float(sys.argv[i]) 
  
print ("the sum is :", add)
