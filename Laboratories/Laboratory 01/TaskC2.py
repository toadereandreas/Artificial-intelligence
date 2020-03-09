# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 22:38:58 2020
@author: Andreas
Task C2
Implement an algorithm that solves a crypt-arithmetic problem:
● Each letter represent a hexadecimal cipher;
● The result of the arithmetic operation must be correct when the letters are replaced
by numbers;
● The numbers can not start with 0;
● Every problem can have only one solution;

ex:
    SEND+     EAT+
    MORE=    THAT=
    ----     -----
   MONEY     APPLE
"""

import string
import random

'''
This method generates a dictionary such that every key ( letter in the alphabet )
has as a value a random number from 0 to 15 and returns it.
Input:
Output: alphabet - a dictionary
'''
def generateAlphabet():
    alphabet = dict.fromkeys(string.ascii_lowercase, 0)
    for key, value in alphabet.items():
        alphabet[key] = random.randint(0,15)
    return alphabet

'''
This method gets an array and transforms its content from letters into numbers
according to the given dictionary.
Input: array - an array of letters
       alphabet - a dictionary with letters as key and integers as numbers
Output:array - an array of integers       
'''
def transformLettersIntoNumbers(array,alphabet):
    for i in range(len(array)):
        array[i] = alphabet.get(array[i])
    return array    

'''
This method returns the key from a dictionary for a given value.
Input: dictionary - a dictonary 
       val - the value for the key
Output:key - the first key that has the value equal to val      
'''
def getKey(dictionary,val):
    for key, value in dictionary.items():
        if value == val:
            return key

'''
This method gets an array and transforms its content from numbers into letters
according to the given dictionary.
Input: array - an array of numbers
       alphabet - a dictionary with letters as key and integers as numbers
Output:array - an array of letters
'''
def transformNumbersIntoLetters(array,alphabet):
    for i in range(len(array)):
        array[i] = getKey(alphabet,array[i])
    return array    

'''
This method adds two numbers represented on 2 arrays in hexadecimal base.
Input: a - the first array
       b - the second array
       n - the length of the array a
       m - the length of the array b
Output: sum - an array containing the sum of the given arrays       
'''
def calSumUtil( a , b , n , m ):
    sum = [0] * n 
    i = n - 1
    j = m - 1
    k = n - 1
    carry = 0
    s = 0

    while j >= 0: 
        s = a[i] + b[j] + carry 
        sum[k] = (s % 16) 
        carry = s // 16
        k-=1
        i-=1
        j-=1
      
    while i >= 0:  
        s = a[i] + carry 
        sum[k] = (s % 16) 
        carry = s // 16
          
        i-=1
        k-=1

    if carry: 
        sum.append(1)
         
    return sum    

# Wrapper Function 
def calSum(a, b, n, m ):
    if n >= m: 
        return calSumUtil(a, b, n, m) 
    else: 
        return calSumUtil(b, a, m, n) 

'''
This method checks whether the two given arrays have the same values on same positions.
Input: arr1 - first array
       arr2 - second array
Output: True/False       
'''
def arraysEqual(arr1,arr2):
    if len(arr1) != len(arr2):
        return False
    if isinstance(arr1,list) == False:
        return False
    if isinstance(arr2,list) == False:
        return False
    for x in range(len(arr1)):
        if arr1[x] != arr2[x]:
            return False
    return True

def example1():
    max = input("Input the number of maximum tries >> ")
    max = int(max)
    result = ["m","o","n","e","y"]
    array3 = []
    tries = 0
    while arraysEqual(array3,result) == False:
        if( max == 0 ):
            break
        max -= 1
        tries += 1
        #print("\nAttempts:" + str(tries))
        alphabet = generateAlphabet()
        #print(alphabet)
        string1 = ["s","e","n","d"]
        string2 = ["m","o","r","e"]
        array1 = transformLettersIntoNumbers(string1,alphabet)
        array2 = transformLettersIntoNumbers(string2,alphabet)
        #print("send = " + str(array1))
        #print("more = " + str(array2))
        len1 = len(array1)
        len2 = len(array2)
        array = calSum(array1,array2,len1,len2)
        #print(array)
        array3 = transformNumbersIntoLetters(array,alphabet)
        #print(array3)
        
def example2():
    max = input("Input the number of maximum tries >> ")
    max = int(max)
    result = ["a","p","p","l","e"]
    array3 = []
    tries = 0
    while arraysEqual(array3,result) == False:
        if( max == 0 ):
            break
        max -= 1
        tries += 1
        print("\nAttempts:" + str(tries))
        alphabet = generateAlphabet()
        print(alphabet)
        string1 = ["e","a","t"]
        string2 = ["t","h","a","t"]
        array1 = transformLettersIntoNumbers(string1,alphabet)
        array2 = transformLettersIntoNumbers(string2,alphabet)
        print("eat = " + str(array1))
        print("that = " + str(array2))
        len1 = len(array1)
        len2 = len(array2)
        array = calSum(array1,array2,len1,len2)
        print(array)
        array3 = transformNumbersIntoLetters(array,alphabet)
        print(array3)
    
def main():
    while True:
        print("\n\n\n\n\nMenu:\n0. Exit\n1. Example 1: SEND + MORE = MONEY;\n2. Example 2: EAT + THAT = APPLE;")
        command = input("Enter command >> ")
        if command == "0":
            break
        if command == "1":
            example1()
        if command == "2":
            example2()
    
main()    