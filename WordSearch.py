#  File: WordSearch.py

#  Description: A program that completes a word search puzzle.

#  Student Name: Rudy Becerra

#  Student UT EID:Rb38259

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E 

#  Unique Number: 52038

#  Date Created: 16-Jan-2023

#  Date Last Modified:

import sys

    

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input ( ):
    # reads first line of n
    num_lines = sys.stdin.readline()
    line = num_lines.strip()

    # creates a blank lst for the grid and words bank
    lst_grid = []
    lst_word = []

    # reads blank line
    blank = sys.stdin.readline()
    
    
    word_row = sys.stdin.readlines()
    count = 0
    
    for item in word_row:
        count+=1
        # creates a 2d list of of the grid
        if count <= int(line):
            
            item.split()

            lst_grid.append(item.split())
            
        # creates a 2d list of the words bank 
        if count >= int(line)+ 3:
            item.split()
            lst_word.append(item.split())

    # turns a 2d list of the word bank to 1d
    word_bank = []  
    for lst in lst_word:
        for word in lst:
            word_bank.append(word)

    
    return lst_grid, word_bank


# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid

                
def find_word (word_grid, word):

    # Finds word in Horizontal search
    for i, row in enumerate(word_grid):
        row_joined = "".join(row)
        j = row_joined.find(word)
        if (j >= 0):
            return (i+1, j+1)
            
    # Finds word in vertical search
    vertical = []
    for row in range(len(word_grid)):
        for colum in range(len(word_grid)):
                vertical.append(word_grid[colum][row])
               

    # compress a 1d lst into a str
    str = ""
    for letter in vertical:
        str += letter

    # creates a new grid verital out of str

    # final 2d array for vertical
    vertical_grid =[]
    for num in range(len(str)):
        if num % len(word_grid) == 0:
            row = str[num:num+len(word_grid)]
            new_grid = []
            for char in row:
                new_grid.append(char)
                
            # appends to final 2d array
            vertical_grid.append(new_grid)
            
    # finds the char index for vertical words
    for i, row in enumerate(vertical_grid):
        row_joined2 = "".join(row)
        j = row_joined2.find(word)
        if (j >= 0):
            return (j+1, i+1)  
    

    
    # finds diaganol words
    diagnol_grid= []
    for i in range(len(word_grid)+1,-1,-1):
        for j in range(len(word_grid)):
            i+= 1
            if j >= len(word_grid) or i>= len(word_grid):
                break
            
            diagnol_grid.append(word_grid[i][j])
        diagnol_grid.append(" ")
    

    str2 = ""
    d_list = []
    for letter in diagnol_grid:
        str2 += letter
         
        if letter != " ":
            d_list = str2.split(" ")
            
   

    for row in d_list:
        if row == "":
            d_list.remove(row)
            
    d_list.remove("")

    for i, row in enumerate(d_list):
        j = row.find(word)
        if (j >= 0):
            return (i-7,j+1)
    
    
        
    
        
    
    return (0,0)

def main():
  # read the input file from stdin
  word_grid, word_list = read_input()

  # find each word and print its location
  for word in word_list:
      location = find_word(word_grid, word)
      print(word + ": " + str(location))

if __name__ == "__main__":
  main()


    







    
