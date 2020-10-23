# import necessary libraries and Representation Class
from Representation import Representation
import timeit
from Algorithms import algorithms
import sys
import json

class SudokuCSP:
    def __init__(self, algorithm):
        self.representation = Representation()
        self.algorithms = algorithms()
        self.algorithm = algorithm
        self.solution(algorithm)

    def getMatrixes(self, i):
        easy = self.representation.matrix('./instances/instance' + str(i+1) + '.txt')
        intermediate =self.representation.matrix('./instances/instance' + str(i+2) + '.txt')
        expert = self.representation.matrix('./instances/instance' + str(i+3) + '.txt')
        instances = [easy, intermediate, expert]
        return instances  


    # main function
    def solution(self, choice):

        labels=['easy','intermediate','expert']
        instances = []
        # calculate time
        if int(choice) == 1:
            algorithm = "solveSudokuBT"
            instances = self.getMatrixes(0)
        elif int(choice) == 2:
            algorithm = "solveSudokuFC"
            instances = self.getMatrixes(3)

        elif int(choice) == 3:
            algorithm = "solveSudokuFC_DO"
            instances = self.getMatrixes(6)

        elif int(choice) == 4:
            algorithm = "solveSudokuFC_DO"
            instances = self.getMatrixes(1)


        dispatcher = { 'solveSudokuBT' : self.algorithms.solveSudokuBT, 
        'solveSudokuFC' : self.algorithms.solveSudokuFC,
        'solveSudokuFC_DO': self.algorithms.solveSudokuFC_DO,
        'solveSudokuFC_DO_MCV': self.algorithms.solveSudokuFC_DO_MCV }

        for i in range(0,3):
            start = timeit.default_timer() 
            self.algorithms.matrix(instances[i])
            if  dispatcher[algorithm](instances[i]):
                print(labels[i])
                self.representation.printMatrix(instances[i])
                stop = timeit.default_timer()
                print('Time: ', stop - start) 
                print('------------------')
               

            else: print('No solution')

            



def main():
    while True:
        print("Choose Algorithm")
        print("---------------------------------------------")
        print("1 - Backtracking ")
        print("2 - Forward checking ")
        print("3 - Forward Checking with Dynamic Ordering LCV")
        print("4 - Forward Checking with Dynamic Ordering MVC")
        print("---------------------------------------------")
        choice = input()
        if(choice == '1' or choice == '2' or choice == '3' or choice == '4' ):    
            sudokuCSP = SudokuCSP(choice)
        else:
            print("Undefined value")
        print("---------------------------------------------")
        print("E - End ")
        print("C - Continue ")
        print("---------------------------------------------")
        if(input().upper() != "C"):
            return False
        


if __name__=="__main__": 
    main()
