"""
Wordle assistance prgram 
General wordle info: 5 character words, 6 attempts to guess word 
guess common letters first, work from data gathered from that 
pull up all words matching specified pattern from list of words in seperate file
"""

def fileToList(wordFile): #this function works
  #parse word file line by line, strip whitespace and append each line to the list
  preEditList = []
  for line in wordFile:
    entry = line.strip()
    preEditList.append(entry)
  return preEditList

def findViableWords(preEditList): #this function works
  #take in main word list and return a list with only words that have 5 letters
  editedList = []
  for element in preEditList:
    if len(element) == 5:
      editedList.append(element)
  return editedList

#return true if a letter not supposed to be in the word is in the word
def checkWord(word, badLetters):
  for letter in badLetters:
    if letter in word:
      return True
#return true if a letter supposed to be in the word is not in the word
def checkWord2(word, goodLetters):
  for letter in goodLetters:
    if letter not in word:
      return True
      
def wordElimination(editedList, badLetters, goodLetters):
#remove words from edited list that contain letters that are not
#in the solution word. These letters are entered by the user 
  editList = editedList
  trashList = []
  for word in editList:
    if checkWord(word, badLetters):
      trashList.append(word)
        
#also remove words that do not contain letters that are supposed to be in the word. these are also
#entered by the user 
  for word in editList:
    if checkWord2(word, goodLetters):
      trashList.append(word)

  for word in trashList:
    if word in editList:
      editList.remove(word)
      
  return editList

def stringToList(Letters):
  # take user input string and separate individual characters into a list and return list
  LettersList = []
  Letters = Letters.strip()
  for i in range(len(Letters)):
    LettersList.append(Letters[i])
  return LettersList
  

def main():
  #open word list file and put each word in a list 
  wordFile = open("WordList.txt", 'r')
  
  #create list of all words in text file
  preEditWordList = fileToList(wordFile)
  
  #remove all words that are not 5 letters
  editedWordList = findViableWords(preEditWordList)
  
  #get list of letters not in the word 
  badLetters = stringToList(input("enter letters that are not in the word without spaces: "))

  #get list of letters that are present in the word 
  goodLetters = stringToList(input("enter letters that are in the word without spaces: "))
  
  #get list of all words that meet specified criteria 
  finalList = wordElimination(editedWordList, badLetters, goodLetters)
  
  print("All viable words:\n")
  print(finalList)

if __name__ == "__main__":
  main()