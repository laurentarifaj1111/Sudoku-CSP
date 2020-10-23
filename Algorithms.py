from Representation import Representation



class algorithms:
    def __init__ (self):
        self.representation = Representation()

    def matrix(self, matrix):
        self.representation.addToListsNonZeroValues(matrix)


    def solveSudokuBT(self, matrix):
       
        if (self.representation.isCompleted(matrix,'sequential') == "finished") :
            return True
        # choose next non-zero variable in sequential order
        i , j = self.representation.isCompleted(matrix,'sequential')
        for value in self.representation.possibleValues(matrix, i, j):

            if self.representation.validValue(matrix,i,j,value):
                matrix[i][j] = value

                if self.solveSudokuBT(matrix):
                    return True

                matrix[i][j] = 0
                
        return False


    def solveSudokuFC(self, matrix):

        if (self.representation.isCompleted(matrix,'MCV') == "finished") :
            return True

        # find most constrained variable
        i , j = self.representation.isCompleted(matrix,'MCV')

        for t in self.representation.possibleValues(matrix, i, j):
            matrix[i][j] = t

            self.representation.rows[i].append(t)
            self.representation.columns[j].append(t)
            self.representation.subMatrixes[self.representation.splitMatrix(matrix, i, j)].append(t)

            if self.solveSudokuFC(matrix):
                return True

            matrix[i][j] = 0

            self.representation.rows[i].pop()
            self.representation.columns[j].pop()
            self.representation.subMatrixes[self.representation.splitMatrix(matrix, i, j)].pop()

        return False


    def solveSudokuFC_DO(self, matrix):

        if (self.representation.isCompleted(matrix,'MCV') == "finished") :
            return True
        # find most constrained variable
        i , j = self.representation.isCompleted(matrix,'MCV')

        for t in self.representation.possibleValues(matrix, i, j):
            matrix[i][j] = t

            self.representation.rows[i].append(t)
            self.representation.columns[j].append(t)
            self.representation.subMatrixes[self.representation.splitMatrix(matrix, i, j)].append(t)

            if self.solveSudokuFC_DO(matrix):
                return True

            matrix[i][j] = 0

            self.representation.rows[i].pop()
            self.representation.columns[j].pop()
            self.representation.subMatrixes[self.representation.splitMatrix(matrix, i, j)].pop()

        return False


    def solveSudokuFC_DO_MCV(self, matrix, MVC):

        if (self.representation.isCompleted(matrix,'MCV') == "finished") :
            return True

        # find most constrained variable
        i , j = self.representation.isCompleted(matrix,'MCV')

        for t in self.representation.possibleValues(matrix, i, j):
            matrix[i][j] = t

            self.representation.rows[i].append(t)
            self.representation.columns[j].append(t)
            self.representation.subMatrixes[self.representation.splitMatrix(matrix, i, j)].append(t)

            if self.solveSudokuFC(matrix):
                return True

            matrix[i][j] = 0

            self.representation.rows[i].pop()
            self.representation.columns[j].pop()
            self.representation.subMatrixes[self.representation.splitMatrix(matrix, i, j)].pop()

        return False
