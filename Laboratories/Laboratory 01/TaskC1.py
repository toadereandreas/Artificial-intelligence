# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 20:15:31 2020
@author: Andreas
Task C1
Consider a Sudoku game - a logic puzzle represented on a n x n board; some squares
contain already a number, others must be completed with other numbers from {1,2,…,n} in such a
way that each line, column and square with the edge equal with √n must contain only different
numbers. Determine one correct solution for the puzzle.
"""

import random
import math
import collections 

'''
This method generates a matrix of n x n with all the cells containing zero.
Input: n - integer
Output: matrix - n x n matrix
'''
def createBoard(n):
    matrix=[] # define empty matrix
    for i in range(n): # total row is 3
        row=[]
        for j in range(n): # total column is 3
            row.append(0) # adding 0 value for each column for this row
        matrix.append(row) # add fully defined column into the row
    return matrix
   
'''
This method populates the given matrix with numbers between 1 and n.
Input: matrix - n x n matrix
       n      - integer
Output:       
'''    
def populateRandom(matrix,n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][j] = random.randint(1,n)  
    
'''
This method prints a given matrix as a Sudoku board.
Input: matrix - n x n matrix
       n      - integer
Output:       
'''    
def printMatrixAsBoard(matrix,n):
    sqrn = int(math.sqrt(n))
    result = "\n"
    for i in range(n):
        partialResult = "|| "
        for j in range(n):
            partialResult += str(matrix[i][j])
            if( j % sqrn == sqrn - 1 ):
                partialResult += " || "
            else:
                partialResult += " | "
        partialResult += '\n'  
        length = len(partialResult)    
        beginning = ""
        if( i % sqrn == sqrn - 1 ):
            for x in range(length-2):
                partialResult += "="
                beginning += "="
            partialResult += '\n'    
        result += partialResult      
    print(str(beginning)+str(result))   
    
'''
This method checks whether the given number n is a perfect square.
Input: n - integer
Outut: True/False
'''    
def validateN(n):
    if( int(math.sqrt(n)) == math.sqrt(n) ):
        return True
    return False    

'''
This method returns a dictionary containing the frequency of the elements in the given array.
Input: array - array of integer
Output: dictionary
'''
def countFrequency(arr): 
    return collections.Counter(arr)   

'''
This method checks wheter there are duplicates on any row in the given matrix.
Input: matrix - n x n matrix
       n      - integer
Output: True/False       
'''
def checkLine(matrix,n):
    for i in range(n):
        freq = countFrequency(matrix[i])
        for key, value in freq.items():
            if(value > 1):
                return False
    return True       

'''
This method returns all the elements from a given column in a given matrix.
Input : matrix - n x n matrix
        n      - integer
        j      - integer
Output: array - array        
'''
def getArrayFromColumnJ(matrix,j,n):
    array = []
    for i in range(n):
        for jj in range(n):
            if jj == j:
                array.append(matrix[i][j])
    return array            

'''
This method checks wheter there are duplicates on any column in the given matrix.
Input: matrix - n x n matrix
       n      - integer
Output: True/False       
'''
def checkColumn(matrix,n):
    for j in range(n):
        arrayJ = getArrayFromColumnJ(matrix,j,n)
        freq = countFrequency(arrayJ)
        for key, value in freq.items():
            if(value > 1):
                return False
    return True       

'''
This method checks whether there are duplicates in a given Sudoku square.
Input: matrix - n x n matrix
       n      - integer
       i      - the line of the top left corner of the square
       j      - the column of the top left corner of the square
Output: True/False       
'''
def checkSquare(matrix,n,i,j):
    sqrn = int(math.sqrt(n))
    array = []
    ii = i
    jj = j
    while(i<ii+sqrn):
        while(j<jj+sqrn):
            array.append(matrix[i][j])
            j += 1
        j = jj    
        i += 1
    freq = countFrequency(array)
    for key, value in freq.items():
        if(value > 1):
            return False
    return True  
            
'''
This method checks whether there are duplicates in any Sudoku square.
Input: matrix - n x n matrix
       n - integer
Output: True/False       
'''
def check(matrix,n):
    sqrn = int(math.sqrt(n))
    i = 0
    j = 0
    while(i<n):
        while(j<n):
            if checkSquare(matrix,n,i,j) == False:
                return False
            j = j + sqrn
        j = 0    
        i = i + sqrn    
    return True    
    
def populateExample1(matrix):
    matrix[0][0] = 3
    matrix[0][3] = 2
    matrix[1][1] = 1
    matrix[1][2] = 4
    matrix[2][0] = 1
    matrix[2][1] = 2
    matrix[2][3] = 4
    matrix[3][1] = 3
    matrix[3][2] = 2
    matrix[3][3] = 1
    
def populateExample2(matrix):
    matrix[0][2] = 8
    matrix[0][4] = 6
    matrix[0][5] = 2
    matrix[1][1] = 3
    matrix[1][3] = 8
    matrix[1][4] = 4
    matrix[1][6] = 9
    matrix[1][8] = 2
    matrix[2][0] = 9
    matrix[2][2] = 6
    matrix[2][7] = 1
    matrix[2][8] = 4  
    matrix[3][1] = 1
    matrix[3][2] = 2
    matrix[3][5] = 8
    matrix[3][6] = 6
    matrix[4][0] = 3
    matrix[4][4] = 7
    matrix[4][5] = 9
    matrix[4][7] = 2
    matrix[5][1] = 6
    matrix[5][3] = 1
    matrix[5][7] = 3
    matrix[5][8] = 7
    matrix[6][2] = 1
    matrix[6][3] = 7
    matrix[6][4] = 8
    matrix[6][6] = 3
    matrix[7][0] = 6
    matrix[7][1] = 8
    matrix[7][2] = 5
    matrix[7][3] = 2
    matrix[7][6] = 7
    matrix[7][7] = 4
    matrix[8][0] = 4
    matrix[8][4] = 9
    matrix[8][5] = 6
    matrix[8][8] = 1
    
def checkForZero(matrix,n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                return True
    return False        

def main():
    n = 0
    while(True):
        n = input("Enter the size of the board: n >> ")
        if( validateN(int(n)) == True ):
            break
        print("Invalid n. N must be a perfect square!")
    
    matrix = createBoard(int(n))
    copy_matrix = createBoard(int(n))
    example = "0"
    
    choice = input("Choose whether to \n1. Start from an example \n2. Give the initial values yourself \n>> ")
    if choice == "1":
        example = input("If you want to start from an example, choose 1 or 2 >> ")

    if choice == "2":
        print("Now input the initial values that you want: ( to stop enter 0 for value )")
        value = 1
        while( value > 0 ):
            value = input("Value >> ")
            value = int(value)
            if value == 0:
                break
            i = input("Line >> ")
            i = int(i)
            j = input("Column >> ")
            j = int(j)
            matrix[i-1][j-1] = value
            copy_matrix[i-1][j-1] = value
        printMatrixAsBoard(copy_matrix,int(n))
        
    max = input("Input the number of maximum attempts >> ") 
    max = int(max)     
    attempts = 0
    while( checkLine(matrix,int(n)) == False or checkColumn(matrix,int(n)) == False or check(matrix,int(n)) == False or checkForZero(matrix,int(n)) == True):
        attempts = attempts + 1
        if( max == 0 ):
            print("Maximum number of attempts has been reached => FAILURE.")
            break
        max -= 1
        matrix = createBoard(int(n))
        if example == "0":
            for i in range(int(n)):
                for j in range(int(n)):
                    matrix[i][j] = copy_matrix[i][j]
        if example == "1":
            populateExample1(matrix)
        if example == "2":
            populateExample2(matrix)
        populateRandom(matrix,int(n))
        printMatrixAsBoard(matrix,int(n))
        #if attempts % 10000 == 0:
        #    printMatrixAsBoard(matrix,int(n))
        
    if checkLine(matrix,int(n)) == True or checkColumn(matrix,int(n)) == True or check(matrix,int(n)) == True:
        print("Solution:")
        printMatrixAsBoard(matrix,int(n))
    
main()    