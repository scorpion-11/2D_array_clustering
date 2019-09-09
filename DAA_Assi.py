# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:53:06 2019

@author: ISHA
"""

arr = [    
        [ 'XYZ', 1, 88, 56, 45],
        [ 'ABC', 2, 45, 86, 52],  
        [ 'LMN', 3, 87, 39, 40],
        [ 'QWS', 4, 96, 86, 85],
        [ 'TRE', 5, 76, 56, 53],
        [ 'UTH', 6, 35, 79, 48],
        [ 'GHJ', 7, 88, 98, 88],
        [ 'DFS', 8, 72, 80, 68],
        [ 'CVB', 9, 45, 56, 50],
        [ 'PQR', 10, 78, 36, 25]]
sumCol=[]
for i in range(len(arr)):
    sumCol.append(0)
#sumCol[len(arr)]

#j = len(arr[0]);
for row in range (0,len(arr)):
   # sumCol[row] = 0;
    for col in range(2,len(arr[row])):
        sumCol[row] = sumCol[row] + arr[row][col]
print("Average marks of all Students of T1, T2, T3 : ",sumCol)
print("Data of Students with greatest cluster are :")
print("- - - - - - - - - - - - - - - - - - - - - -")
print("\ Name  \ Roll No  \ T1     \ T2     \ T3 ")
print("- - - - - - - - - - - - - - - - - - - - - -")
for i in range(len(arr)):
    if sumCol[i]>240:
         for j in range(len(arr[i])):
          print("\ ",arr[i][j], end='\t')
    
    print()
print("- - - - - - - - - - - - - - - - - - - - - -")

   
        