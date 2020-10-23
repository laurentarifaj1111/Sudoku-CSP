from itertools import chain 
import math
import sys

class Representation:

    def __init__(self):
        print()
        self.rows = []
        self.columns = [] 
        self.subMatrixes = []

        
    def createMatrixes(self):
        self.rows = [ [] for i in range(9) ]
        self.columns = [ [] for i in range(9) ]
        self.subMatrixes = [ [] for i in range(9) ]


    def splitMatrix(self, matrix, i, j):
        n = math.sqrt(len(matrix[0]))
        return int(int(j/n) + n* int(i/n))


    def addToListsNonZeroValues(self, matrix):
        self.createMatrixes()
        for j in range(0 , len(matrix[0])):            
            for i in range (0 , len(matrix[0])):
                if(matrix[i][j] != 0):
                    self.columns[j].append(matrix[i][j])
                    self.rows[i].append(matrix[i][j])
                    self.subMatrixes[self.splitMatrix(matrix, i ,j)].append(matrix[i][j])


    def possibleValues(self , matrix , i ,j, chekDO=''):
        possibleValues = []
        for k in range(1 , len(matrix[0]) + 1):
            if ( k not in self.rows[i] and k not in self.columns[j] 
            and k not in self.subMatrixes[self.splitMatrix(matrix , i ,j)]):
                possibleValues.append(k)

        if(chekDO == 'DO_MCV'):        
            least = self.mostConstraitValue(matrix)        
            if(least in possibleValues):
                possibleValues.remove(least)
                possibleValues.insert(least, 1)
        return possibleValues


    def isCompleted(self,matrix,option):
        # for BT,FC
        if option=='sequential':
            for i in range (0 ,len(matrix[0])):
                for j in range (0 , len(matrix[1])):
                    if (matrix[i][j] == 0):
                        return i , j
            return "finished"
        # for FC-DO
        if option=='MCV':
            temp = int()
            row = None
            column = None
            temp1= 10
            for i in range (0 ,len(matrix[0])):
                for j in range (0 , len(matrix[1])):
                    if (matrix[i][j] == 0):
                        temp = len(self.possibleValues(matrix, i, j))
                        if(temp < temp1):
                            temp1 = temp
                            row =i
                            column = j

            if (row != None and column != None ):
                return row , column 
            else:
                return "finished"

    def printMatrix(self, matrix):
        for i in range(0, 9):
            for j in range(0, 9):
                print(matrix[i][j], end=" ")
            print()
    
    def validValue(self,matrix, i, j, value):
        for k in range(len(matrix[0])):
            if(matrix[i][k]==value or matrix[k][j]==value):
                return False
        subrstart=int(j/3)
        subkstart=int(i/3)
        for subr in  range(subkstart*3, subkstart*3+3):
            for subk in range(subrstart*3, subrstart*3+3):
                if matrix[subr][subk]==value:
                 return False
        return True

    def split(self, word): 
        return [int(char) for char in word]

    def matrix(self, file):
        contents = open(file).read()
        return [self.split(item) for item in contents.split('\n')[:-1]][:-1]

    def mostConstraitValue(self, matrix): 
        flatten_list = list(chain.from_iterable(matrix))
        flatten_list = list(filter(lambda x: x!= 0, flatten_list))
        return (max(set(flatten_list), key = flatten_list.count)) 

