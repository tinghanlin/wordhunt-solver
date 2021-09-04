##################################################
## GamePigeon Word Hunt Solver:
## A player can enter 6 letters in the interactive window, then the program would show the words found
##################################################
## Author: Ting-Han Lin
## Copyright: Copyright 2021, GamePigeon Anagram Solver
## Credits: [Raghav Gurung (https://medium.com/python-anagram-solver/python-anagram-solver-edb2646b65f8)]
## Version: 1.0.0
## Maintainer: Ting-Han Lin
## Email: tinghan@uchicago.edu
## Status: Complete
##################################################

#import modules
import pandas as pd
from collections import Counter
from tkinter import *
import textwrap


#import the all of the words, the longest word is 15 characters
dictionary = pd.read_excel('Collins Scrabble Words (2019).xlsx')

#for GamePigeon Word Hunt, a players has to make words from 16 letters
#and each word has to be longer than 3 letters
#so we get rid of 2 letter words
result_dictionary = dictionary[dictionary['List of Words'].str.len() > 2]

#convert the words from a dataframe to series
word_series=result_dictionary.squeeze()

def searchWords(mystring, word_series):
    #declare an empty list where we put the formable words
    output = []

    #separate the 6 character string, and count the occurrence of each letter
    myletters = list(mystring)
    letters_count = Counter(myletters)

    #check if a word in dictionary can be formed with the given letters
    #reference from https://medium.com/python-anagram-solver/python-anagram-solver-edb2646b65f8
    for word in word_series:
        if not(set(list(word)) - set(myletters)):
            word_count = Counter(word)
            word_set = set()
            for key, value in Counter(word).items():
                if value <= letters_count[key]:
                    word_set.add(key)
                if word_set == set(list(word)):
                    output.append(word)
                    
    output.sort() #sorts by alphabetical order
    output.sort(key=len, reverse=True) #sorts by descending length
    return output

class Cell:
    def __init__(self, rol, col, letter, check):
        self.row = rol
        self.col = col
        self.letter= letter
        self.check = False

c1  = Cell(0, 0, "A", False)
c2  = Cell(0, 1, "B", False)
c3  = Cell(0, 2, "C", False)
c4  = Cell(0, 3, "D", False)
c5  = Cell(1, 0, "E", False)
c6  = Cell(1, 1, "F", False)
c7  = Cell(1, 2, "G", False)
c8  = Cell(1, 3, "H", False)
c9  = Cell(2, 0, "I", False)
c10 = Cell(2, 1, "J", False)
c11 = Cell(2, 2, "K", False)
c12 = Cell(2, 3, "L", False)
c13 = Cell(3, 0, "M", False)
c14 = Cell(3, 1, "N", False)
c15 = Cell(3, 2, "O", False)
c16 = Cell(3, 3, "P", False)

grid = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16]
struct_grid = [[c1,c2,c3,c4],[c5,c6,c7,c8],[c9,c10,c11,c12],[c13,c14,c15,c16]]

#start_cell = [c1]
#word = ['A', 'B', 'C']
def wordhunt(start_cell, word):
    #print("word: ", word)
    
    #base case
    if len(word) == 1:
        return 1 # word is found
    
    word.pop(0)
    
    next_cell=[]
    
    for cell in start_cell:
    
        if cell.row == 0 and cell.col == 0: #upper left
            
            #go right
            if struct_grid[cell.row][cell.col+1].letter == word[0] and struct_grid[cell.row][cell.col+1].check == False:
                struct_grid[cell.row][cell.col+1].check = True
                next_cell.append(struct_grid[cell.row][cell.col+1])
                
            #go bottom right
            if struct_grid[cell.row+1][cell.col+1].letter == word[0] and struct_grid[cell.row+1][cell.col+1].check == False:
                struct_grid[cell.row+1][cell.col+1].check = True
                next_cell.append(struct_grid[cell.row+1][cell.col+1])
                
            #go down
            if struct_grid[cell.row+1][cell.col].letter == word[0] and struct_grid[cell.row+1][cell.col].check == False:
                struct_grid[cell.row+1][cell.col].check = True
                next_cell.append(struct_grid[cell.row+1][cell.col])
        
        elif cell.row == 0 and cell.col == 3: #upper right corner 
            
            #go left
            if struct_grid[cell.row][cell.col-1].letter == word[0] and struct_grid[cell.row][cell.col-1].check == False:
                struct_grid[cell.row][cell.col-1].check = True
                next_cell.append(struct_grid[cell.row][cell.col-1])
            
            #go bottom left
            if struct_grid[cell.row+1][cell.col-1].letter == word[0] and struct_grid[cell.row+1][cell.col-1].check == False:
                struct_grid[cell.row+1][cell.col-1].check = True
                next_cell.append(struct_grid[cell.row+1][cell.col-1])
            
            #go down
            if struct_grid[cell.row+1][cell.col].letter == word[0] and struct_grid[cell.row+1][cell.col].check == False:
                struct_grid[cell.row+1][cell.col].check = True
                next_cell.append(struct_grid[cell.row+1][cell.col])
            
        elif cell.row == 3 and cell.col == 0: #bottom left corner 
            
            #go up
            if struct_grid[cell.row-1][cell.col].letter == word[0] and struct_grid[cell.row-1][cell.col].check == False:
                struct_grid[cell.row-1][cell.col].check = True
                next_cell.append(struct_grid[cell.row-1][cell.col])
            
            #go up right 
            if struct_grid[cell.row-1][cell.col+1].letter == word[0] and struct_grid[cell.row-1][cell.col+1].check == False:
                struct_grid[cell.row-1][cell.col+1].check = True
                next_cell.append(struct_grid[cell.row-1][cell.col+1])
            
            #go right
            if struct_grid[cell.row][cell.col+1].letter == word[0] and struct_grid[cell.row][cell.col+1].check == False:
                struct_grid[cell.row][cell.col+1].check = True
                next_cell.append(struct_grid[cell.row][cell.col+1])
            
        elif cell.row == 3 and cell.col == 3: # bottom right corner
            
            #go up
            if struct_grid[cell.row-1][cell.col].letter == word[0] and struct_grid[cell.row-1][cell.col].check == False:
                struct_grid[cell.row-1][cell.col].check = True
                next_cell.append(struct_grid[cell.row-1][cell.col])
            
            #go up left
            if struct_grid[cell.row-1][cell.col-1].letter == word[0] and struct_grid[cell.row-1][cell.col-1].check == False:
                struct_grid[cell.row-1][cell.col-1].check = True
                next_cell.append(struct_grid[cell.row-1][cell.col-1])
                
            #go left
            if struct_grid[cell.row][cell.col-1].letter == word[0] and struct_grid[cell.row][cell.col-1].check == False:
                struct_grid[cell.row][cell.col-1].check = True
                next_cell.append(struct_grid[cell.row][cell.col-1])
            
        elif cell.row == 0: #upper edge
            #go right
            if struct_grid[cell.row][cell.col+1].letter == word[0] and struct_grid[cell.row][cell.col+1].check == False:
                struct_grid[cell.row][cell.col+1].check = True
                next_cell.append(struct_grid[cell.row][cell.col+1])
            
             #go bottom right
            if struct_grid[cell.row+1][cell.col+1].letter == word[0] and struct_grid[cell.row+1][cell.col+1].check == False:
                struct_grid[cell.row+1][cell.col+1].check = True
                next_cell.append(struct_grid[cell.row+1][cell.col+1])
                
            #go down
            if struct_grid[cell.row+1][cell.col].letter == word[0] and struct_grid[cell.row+1][cell.col].check == False:
                struct_grid[cell.row+1][cell.col].check = True
                next_cell.append(struct_grid[cell.row+1][cell.col])
                
            #go bottom left
            if struct_grid[cell.row+1][cell.col-1].letter == word[0] and struct_grid[cell.row+1][cell.col-1].check == False:
                struct_grid[cell.row+1][cell.col-1].check = True
                next_cell.append(struct_grid[cell.row+1][cell.col-1])
                
            #go up
            if struct_grid[cell.row-1][cell.col].letter == word[0] and struct_grid[cell.row-1][cell.col].check == False:
                struct_grid[cell.row-1][cell.col].check = True
                next_cell.append(struct_grid[cell.row-1][cell.col])
                
        elif cell.row == 3: #lower edge
            #go up left
            if struct_grid[cell.row-1][cell.col-1].letter == word[0] and struct_grid[cell.row-1][cell.col-1].check == False:
                struct_grid[cell.row-1][cell.col-1].check = True
                next_cell.append(struct_grid[cell.row-1][cell.col-1])
                
            #go left
            if struct_grid[cell.row][cell.col-1].letter == word[0] and struct_grid[cell.row][cell.col-1].check == False:
                struct_grid[cell.row][cell.col-1].check = True
                next_cell.append(struct_grid[cell.row][cell.col-1])
                
            #go up
            if struct_grid[cell.row-1][cell.col].letter == word[0] and struct_grid[cell.row-1][cell.col].check == False:
                struct_grid[cell.row-1][cell.col].check = True
                next_cell.append(struct_grid[cell.row-1][cell.col])
            
            #go up right 
            if struct_grid[cell.row-1][cell.col+1].letter == word[0] and struct_grid[cell.row-1][cell.col+1].check == False:
                struct_grid[cell.row-1][cell.col+1].check = True
                next_cell.append(struct_grid[cell.row-1][cell.col+1])
            
            #go right
            if struct_grid[cell.row][cell.col+1].letter == word[0] and struct_grid[cell.row][cell.col+1].check == False:
                struct_grid[cell.row][cell.col+1].check = True
                next_cell.append(struct_grid[cell.row][cell.col+1])
                
        elif cell.col == 3: #right edge
           #go down
            if struct_grid[cell.row+1][cell.col].letter == word[0] and struct_grid[cell.row+1][cell.col].check == False:
                struct_grid[cell.row+1][cell.col].check = True
                next_cell.append(struct_grid[cell.row+1][cell.col])
                
            #go bottom left
            if struct_grid[cell.row+1][cell.col-1].letter == word[0] and struct_grid[cell.row+1][cell.col-1].check == False:
                struct_grid[cell.row+1][cell.col-1].check = True
                next_cell.append(struct_grid[cell.row+1][cell.col-1])
                
            #go up
            if struct_grid[cell.row-1][cell.col].letter == word[0] and struct_grid[cell.row-1][cell.col].check == False:
                struct_grid[cell.row-1][cell.col].check = True
                next_cell.append(struct_grid[cell.row-1][cell.col])
            
            #go up left
            if struct_grid[cell.row-1][cell.col-1].letter == word[0] and struct_grid[cell.row-1][cell.col-1].check == False:
                struct_grid[cell.row-1][cell.col-1].check = True
                next_cell.append(struct_grid[cell.row-1][cell.col-1])
                
            #go left
            if struct_grid[cell.row][cell.col-1].letter == word[0] and struct_grid[cell.row][cell.col-1].check == False:
                struct_grid[cell.row][cell.col-1].check = True
                next_cell.append(struct_grid[cell.row][cell.col-1])
                
        elif cell.col == 0: #left edge
            #go right
            if struct_grid[cell.row][cell.col+1].letter == word[0] and struct_grid[cell.row][cell.col+1].check == False:
                struct_grid[cell.row][cell.col+1].check = True
                next_cell.append(struct_grid[cell.row][cell.col+1])
            
             #go bottom right
            if struct_grid[cell.row+1][cell.col+1].letter == word[0] and struct_grid[cell.row+1][cell.col+1].check == False:
                struct_grid[cell.row+1][cell.col+1].check = True
                next_cell.append(struct_grid[cell.row+1][cell.col+1])
                
            #go down
            if struct_grid[cell.row+1][cell.col].letter == word[0] and struct_grid[cell.row+1][cell.col].check == False:
                struct_grid[cell.row+1][cell.col].check = True
                next_cell.append(struct_grid[cell.row+1][cell.col])
                
            #go up
            if struct_grid[cell.row-1][cell.col].letter == word[0] and struct_grid[cell.row-1][cell.col].check == False:
                struct_grid[cell.row-1][cell.col].check = True
                next_cell.append(struct_grid[cell.row-1][cell.col])
            
            #go up right 
            if struct_grid[cell.row-1][cell.col+1].letter == word[0] and struct_grid[cell.row-1][cell.col+1].check == False:
                struct_grid[cell.row-1][cell.col+1].check = True
                next_cell.append(struct_grid[cell.row-1][cell.col+1])
                
        else: #middle
            #go right
            if struct_grid[cell.row][cell.col+1].letter == word[0] and struct_grid[cell.row][cell.col+1].check == False:
                struct_grid[cell.row][cell.col+1].check = True
                next_cell.append(struct_grid[cell.row][cell.col+1])
            
             #go bottom right
            if struct_grid[cell.row+1][cell.col+1].letter == word[0] and struct_grid[cell.row+1][cell.col+1].check == False:
                struct_grid[cell.row+1][cell.col+1].check = True
                next_cell.append(struct_grid[cell.row+1][cell.col+1])
                
            #go down
            if struct_grid[cell.row+1][cell.col].letter == word[0] and struct_grid[cell.row+1][cell.col].check == False:
                struct_grid[cell.row+1][cell.col].check = True
                next_cell.append(struct_grid[cell.row+1][cell.col])
                
            #go up
            if struct_grid[cell.row-1][cell.col].letter == word[0] and struct_grid[cell.row-1][cell.col].check == False:
                struct_grid[cell.row-1][cell.col].check = True
                next_cell.append(struct_grid[cell.row-1][cell.col])
            
            #go up right 
            if struct_grid[cell.row-1][cell.col+1].letter == word[0] and struct_grid[cell.row-1][cell.col+1].check == False:
                struct_grid[cell.row-1][cell.col+1].check = True
                next_cell.append(struct_grid[cell.row-1][cell.col+1])
            
            #go up left
            if struct_grid[cell.row-1][cell.col-1].letter == word[0] and struct_grid[cell.row-1][cell.col-1].check == False:
                struct_grid[cell.row-1][cell.col-1].check = True
                next_cell.append(struct_grid[cell.row-1][cell.col-1])
                
            #go left
            if struct_grid[cell.row][cell.col-1].letter == word[0] and struct_grid[cell.row][cell.col-1].check == False:
                struct_grid[cell.row][cell.col-1].check = True
                next_cell.append(struct_grid[cell.row][cell.col-1])
                
            #go bottom left
            if struct_grid[cell.row+1][cell.col-1].letter == word[0] and struct_grid[cell.row+1][cell.col-1].check == False:
                struct_grid[cell.row+1][cell.col-1].check = True
                next_cell.append(struct_grid[cell.row+1][cell.col-1])
                
    ###DEBUG###
    """
    if len(next_cell)==0:
        print("no next cell")
    else:
        for cell in next_cell: 
            print("cell name: ", cell , "; letter: ", cell.letter)
    """

    #recursive case
    if len(next_cell)==0:
        return 0 #no word
    else:
        #print("word hunt function runs")
        return wordhunt(next_cell, word) #the first letter of the word here is removed

def findable_word(searchWord):
    findable_word = []
    for vocab in searchWord:
        #print("Vocab: ", vocab)
        vocab_letters = list(vocab)
        start_cell = []

        for cell in grid: 
            #find the starting point for each word
            if cell.letter == vocab_letters[0]: 
                start_cell.append(cell)

        #there will be at least one item in start_cell
        for cell in start_cell:
            #I need the cell to be in a list
            tmp_list = [cell]

            #tmp_list should be in this format: [c1]
            #vocab_letters should be in this format: ['A', 'B', 'C']
            res=wordhunt(tmp_list, vocab_letters)

            #initialize the grid
            for cell in grid:
                cell.check = False

            if res == 1:
                #word is found
                findable_word.append(vocab)
                break

                
    ###DEBUG###
    '''
    for item in findable_word:
        print("find: " ,item)
    '''
    
    return findable_word

#convert list to string
def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))

#click event
def myClick():
    userInput = ent.get()
    
    if (userInput.isalpha() == False) or (len(userInput) > 16 or len(userInput) < 16):
        message['text'] = "Please enter 16 letters!"
    else:
        userInput = userInput.upper()
        userInputList = list(userInput)
        
        #initialize the grid everytime when there is a new userinput
        for i in range(16):
            grid[i].letter = userInputList[i]
        
        #anagram words
        searchWord=searchWords(userInput, word_series)
        
        #cross compare searchable words
        final_answer=findable_word(searchWord)
        
        if len(final_answer) == 0: 
            message['text'] = "No word is found!"
        else:
            final_answer = listToString(final_answer)
            message['text'] = textwrap.fill(final_answer, width=60)

#initialize an interactive window using tkinter
root= Tk()
root.geometry("600x450")  
root.title('Word Hunt Solver')  

instruct = Label(root, text = "Please enter 16 letters in the box below!")
instruct.pack() 
    
ent = Entry(root, width=50, bd=10)
ent.pack()    
    
myButton = Button(root, text="Enter 16 Letters", command = myClick)
myButton.pack()

message = Label(root, text = "")
message.pack() 

root.mainloop()