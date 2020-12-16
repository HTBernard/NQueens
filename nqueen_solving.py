import time

class Board:
    #Initialize a board
    def __init__(self, tabBoard):
        self.tabBoard = tabBoard

    #First algorithm, supposed to be very slow
    def worst_QueenFinder(self, board_size, colIndex = 0) :
        for lineIndex in range(board_size) :
            if self.tabBoard[lineIndex][colIndex] == 0 :
                self.heatMap(lineIndex, colIndex, 1)
                if colIndex != len(self.tabBoard) - 1 :
                    if self.queensSafes() :
                        if self.worst_QueenFinder(board_size, colIndex + 1)[1] :
                            return self.tabBoard, True
                    self.heatMap(lineIndex, colIndex, -1)
                elif self.isSoluce()[0] :
                    return self.tabBoard, True
                else :
                    self.heatMap(lineIndex, colIndex, -1)
        return self.tabBoard, False

    #Second algorithm, supposed to be the fastest
    def best_QueenFinder(self, board_size) :
        for lineIndex in range(board_size) :
            if self.tabBoard[lineIndex][colIndex] == 0 :
                self.tabBoard[lineIndex][colIndex] = 1
                if colIndex != len(self.tabBoard) - 1 :
                    self.showHeatMap()
                    print(self)
        return self.tabBoard, False

    #Third algorithm who return every possible configuration for the given board size
    def all_QueenFinder(self, board_size) :

        return boardsConfigurations

    #Return true if any queen can't attack any other queen
    def queensSafes(self, heatNumber = False) :
        returnVal = 0 if heatNumber else True
        queenTab = []
        for lineCmpt in range(len(self.tabBoard)) :
            for colCmpt in range(len(self.tabBoard[lineCmpt])) :
                if self.tabBoard[lineCmpt][colCmpt] == 1 :
                    queenTab.append([lineCmpt,colCmpt])
        for queen in queenTab :
            for queenComp in queenTab :
                if not (queen[0] == queenComp[0] and queen[1] == queenComp[1]) :
                    queenOnLine = queen[0] == queenComp[0]
                    queenOnCol = queen[1] == queenComp[1]
                    queenOnDiag1 = queen[0] + queen[1] == queenComp[0] + queenComp[1]
                    queenOnDiag2 = queen[0] - queen[1] == queenComp[0] - queenComp[1]
                    if queenOnLine or queenOnCol or queenOnDiag1 or queenOnDiag2 :
                        if heatNumber :
                            returnVal += 1
                        else :
                            return False
        return returnVal

    #Return true if the board in this configuration is a solution, also return how many queens are placed
    def isSoluce(self) :
        nbQueen = 0
        for lineCmpt in range(len(self.tabBoard)) :
            for colCmpt in range(len(self.tabBoard[lineCmpt])) :
                nbQueen += self.tabBoard[lineCmpt][colCmpt]
        if nbQueen < len(self.tabBoard) :
            return False, nbQueen
        return self.queensSafes(), nbQueen

    #Print the board
    def __repr__(self) :
        printBoard = ""
        for line in self.tabBoard :
            for case in line :
                printBoard += str(1 if case == 1 else 0) + " "
            printBoard += "\n"
        return printBoard

    def heatMap(self, line, col, heatUp) :
        self.tabBoard[line][col] += heatUp
        for oneLine in range (len(self.tabBoard)) :
            if self.tabBoard[line][oneLine] == 1-heatUp :
                self.tabBoard[line][oneLine] = 1+heatUp
            elif self.tabBoard[line][oneLine] > 1 :
                self.tabBoard[line][oneLine] += heatUp
        for oneCol in range (len(self.tabBoard)) :
            if self.tabBoard[oneCol][col] == 1-heatUp :
                self.tabBoard[oneCol][col] = 1+heatUp
            elif self.tabBoard[oneCol][col] > 1 :
                self.tabBoard[oneCol][col] += heatUp
        return

    def permuteLines(self, line1, line2) :
        firstLine = self.tabBoard[line1]
        self.tabBoard[line1] = self.tabBoard[line2]
        self.tabBoard[line2] = firstLine

def solve_n_queen_small(board_size, board) :
    theBoard = Board(board)
    return theBoard.worst_QueenFinder(board_size)

def solve_n_queen_big(board_size, board) :
    theBoard = Board(board)
    return theBoard.best_QueenFinder(board_size)

def solve_n_queen_all_soluce(board_size, board) :
    theBoard = Board(board)
    return theBoard.all_QueenFinder(board_size)

def can_t_attack(board_size, board) :
    theBoard = Board(board)
    return theBoard.queensSafes()

def is_soluce(board_size, board) :
    theBoard = Board(board)
    return theBoard.isSoluce()

def print_board(board_size, board) :
    theBoard = Board(board)
    print(theBoard)


def generate_board(size):
    return [[0 for x in range(size)] for y in range(size)]

size = 16
board = generate_board(size)
millis = int(round(time.time() * 1000))
board = solve_n_queen_small(size, board)[0]
millis = millis = int(round(time.time() * 1000)) - millis
print (Board(board))
print("Took " + str(millis) + " milliseconds.")