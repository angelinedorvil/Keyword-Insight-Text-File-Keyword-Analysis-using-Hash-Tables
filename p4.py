from timeit import default_timer as timer
import sys

# Angeline Dorvil

#command line arguments
if len(sys.argv) != 3:
 raise ValueError('Please provide two file names.')
firstFile = sys.argv[1]
secondFile = sys.argv[2]
print("\nThe hash table will be built from:", firstFile)
print("\nThe hash table will be compared to:", secondFile)

#Main program
import time
start = time.time()

#Constants
tableSize = 29
a = 31

# Initialize the hash table
hashTable = [""] * tableSize

# Hash Code Calculation Function
def hc(word):
    lgth = len(word)
    hcPlace = 0
    i = 0
    while i < lgth:
        place = ord(word[i]) *(a**(lgth-1-i)) 
        hcPlace += place
        i+=1
    return (hcPlace % tableSize)

# Function to Insert Words into Hash Table with Linear Probing
def insert_word(word):
    hashKey = hc(word)
    
    if word in hashTable[hashKey]:     # Check for duplicates at the specific index
        return
    
    if hashTable[hashKey] == "":  # Check if the index is empty
        hashTable[hashKey] = word
    else:
        nextIndex = (hashKey + 1) % tableSize  # Linear probing to find the next available slot
        
        while hashTable[nextIndex] != "" and nextIndex != hashKey:  # Check for an empty slot
            nextIndex = (nextIndex + 1) % tableSize  # Update index
            
        if hashTable[nextIndex] == "" and nextIndex != hashKey:  # If an empty slot is found
            hashTable[nextIndex] = word
        else:
            return # Handle full hash table scenario

def compare_word(word):
    hashKey = hc(word)
    if word in hashTable[hashKey]:
        return word
    else:
        nextIndex = (hashKey + 1) % tableSize
        while hashTable[nextIndex] != "" and nextIndex != hashKey:
            if word in hashTable[nextIndex]:
                return word
                break
            nextIndex = (nextIndex + 1) % tableSize

    

#read whole text from Ihaveadream file
fileName = "IHaveADream.txt"
with open(fileName, "r") as f:
    lines = f.readlines()
    for line in lines:
        line.rstrip()
        words = line.split()
        for word in words:
            cleanWord = word.strip().lower()
            insert_word(cleanWord)
f.close()

# Initialize variables for statistics
lineCount = 0
wordCount = 0
keywordFreq = {}

#read whole text from MLKSPeech file
speechName = "MLKSpeech.txt"
with open(speechName, "r") as p:
    sLines = p.readlines()
    for sLine in sLines:
        sLine.rstrip()
        if sLine:
            lineCount += 1
            
        sWords = sLine.split()
        for sWord in sWords:
            wordCount +=1
            cleanSword = sWord.strip().lower()            
            token = compare_word(cleanSword)
            
            if token:
                if token in keywordFreq:
                    keywordFreq[token] += 1
                else:
                    keywordFreq[token] = 1
                    
print()
print("Statistics:")
print("Total lines read: ", lineCount)
print("Total words read: ", wordCount)
print()

# Iterate through hashTable to find missing words in text
for word in hashTable:
    if word:
        cleanWord = word.strip().lower()
        if cleanWord not in keywordFreq:
            keywordFreq[cleanWord] = 0

# Print keyword frequencies
print("Break down by keyword:")
for keyword, frequency in keywordFreq.items():
    print(f"{frequency} : {keyword}")

p.close()

# Calculate and print total running time
print()
end = time.time()
print("\nTotal Time of Program: {0} milliseconds\n" .format(end - start))
