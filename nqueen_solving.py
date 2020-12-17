import time

class Board:
    #Initialize a board
    def __init__(self, tabBoard):
        self.tabBoard = tabBoard

    #First algorithm, supposed to be very slow
    def worst_QueenFinder(self, board_size, col = 0) :
        for line in range(board_size) :
            if self.tabBoard[line][col] == 0 :
                self.placeQueen(board_size, line, col, 1)
                if col != len(self.tabBoard) - 1 :
                    if self.queensSafes() :
                        if self.worst_QueenFinder(board_size, col + 1)[1] :
                            if col == 0 :
                                self.unHeat()
                            return self.tabBoard, True
                    self.placeQueen(board_size, line, col, -1)
                elif self.isSoluce()[0] :
                    if col == 0 :
                        self.unHeat()
                    return self.tabBoard, True
                else :
                    self.placeQueen(board_size, line, col, -1)
        self.unHeat()
        return self.tabBoard, False

    #Second algorithm, supposed to be the fastest
    def best_QueenFinder(self, board_size) :
        return self.tabBoard, False

    #Third algorithm who return every possible configuration for the given board size
    def all_QueenFinder(self, board_size, col = 0, boardConfigurations = []) :
        for line in range(board_size) :
            if self.tabBoard[line][col] == 0 :
                self.placeQueen(board_size, line, col, 1)

                if col != len(self.tabBoard) - 1 :
                    self.all_QueenFinder(board_size, col + 1, boardConfigurations)
                elif self.isSoluce()[0] :
                    print(self)
                    boardConfigurations.append(self.tabBoard)
                    self.placeQueen(board_size, line, col, -1)
                else :
                    self.placeQueen(board_size, line, col, -1)
        if col != 0 :
            pass
        for board in boardConfigurations :
            unHeat(board)
        return boardConfigurations

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
    def __repr__(self, showHeatMap = 0) :
        printBoard = ""
        for line in self.tabBoard :
            for case in line :
                if showHeatMap == 2:
                    printBoard += ("X" if case == 1 else ".") + " "
                elif showHeatMap == 1:
                    printBoard += ("." if case == 0 else str(case)) + " "
                else :
                    printBoard += " " + str(1 if case == 1 else 0)
            printBoard += "\n"
        return printBoard.rstrip("\n")

    def unHeat(self) :
        for line in range(len(self.tabBoard)) :
            for col in range(len(self.tabBoard)) :
                if self.tabBoard[line][col] != 1 :
                    self.tabBoard[line][col] = 0

    def manageHeat(self, line, col, heat) :
        if self.tabBoard[line][col] == 1-heat :
            self.tabBoard[line][col] = 1+heat
        elif self.tabBoard[line][col] > 1 :
            self.tabBoard[line][col] += heat

    def placeQueen(self, board_size, line, col, heat) :
        self.tabBoard[line][col] += heat
        for oneLine in range (board_size) :
            self.manageHeat(line, oneLine, heat)
        for oneCol in range (board_size) :
            self.manageHeat(oneCol, col, heat)
        for diag in range(-board_size, 0) :
            if line+diag < board_size and line + diag > -1 :
                if col+diag < board_size and col + diag > -1 :
                    self.manageHeat(line + diag, col + diag, heat)
                if col-diag < board_size and col - diag > -1 :
                    self.manageHeat(line + diag, col - diag, heat)
            if line-diag < board_size and line - diag > -1 :
                if col+diag < board_size and col + diag > -1 :
                    self.manageHeat(line - diag, col + diag, heat)
                if col-diag < board_size and col - diag > -1 :
                    self.manageHeat(line - diag, col - diag, heat)
        return

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

board = Board(generate_board(10))

print(Board(board.worst_QueenFinder(10)[0]))