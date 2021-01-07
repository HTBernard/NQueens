import copy


class Board:
    # Initialize a board
    def __init__(self, tabBoard):
        self.board_size = len(tabBoard)
        self.tabBoard = tabBoard
        self.riskBoard = tabBoard

    # Backtracking algorithm
    def worst_QueenFinder(self, col=0):
        for line in range(self.board_size):
            if self.riskBoard[line][col] == 0:
                self.tabBoard[line][col] = 1
                self.riskMap()
                if col != self.board_size - 1:
                    if self.worst_QueenFinder(col + 1)[1]:
                        return self.tabBoard, True
                    self.tabBoard[line][col] = 0
                elif self.isSoluce()[0]:
                    return self.tabBoard, True
                else:
                    self.tabBoard[line][col] = 0
                self.riskMap()
        return self.tabBoard, False

    # Return every possible configuration for the given board size
    def all_QueenFinder(self, col=0, boardConfigs=[]):
        if col == 0:
            boardConfigs = []
        for line in range(self.board_size):
            if self.riskBoard[line][col] == 0:
                self.tabBoard[line][col] = 1
                self.riskMap()
                if col != self.board_size - 1:
                    boardConfigs = self.all_QueenFinder(col + 1, boardConfigs)
                elif self.isSoluce()[0]:
                    boardConfigs.append(copy.deepcopy(self.tabBoard))
                self.tabBoard[line][col] = 0
                self.riskMap()
        return boardConfigs

    # Ensure 2 queens given are safe from eachother
    def queensSafes(queen, queenComp):
        if not (queen[0] == queenComp[0] and queen[1] == queenComp[1]):
            queenOnLine = queen[0] == queenComp[0]
            queenOnCol = queen[1] == queenComp[1]
            queenOnDiag1 = queen[0] + queen[1] == queenComp[0] + queenComp[1]
            queenOnDiag2 = queen[0] - queen[1] == queenComp[0] - queenComp[1]
            if queenOnLine or queenOnCol or queenOnDiag1 or queenOnDiag2:
                return False
        return True

    # Find all queens on the board
    def findQueens(self):
        queensTab = []
        for lineCmpt in range(self.board_size):
            for colCmpt in range(self.board_size):
                if self.tabBoard[lineCmpt][colCmpt] == 1:
                    queensTab.append([lineCmpt, colCmpt])
        return queensTab

    # Return true if any queen can't attack any other queen
    def allQueensSafes(self):
        queensTab = self.findQueens()
        for queenIndex in range(len(queensTab)):
            for queenCompIndex in range(queenIndex+1, len(queensTab)):
                queen = queensTab[queenIndex]
                queenComp = queensTab[queenCompIndex]
                if not Board.queensSafes(queen, queenComp):
                    return False
        return True

    # Return if board is a solition and the number of queens placed
    def isSoluce(self):
        nbQueen = 0
        for lineCmpt in range(len(self.tabBoard)):
            for colCmpt in range(len(self.tabBoard[lineCmpt])):
                nbQueen += self.tabBoard[lineCmpt][colCmpt]
        if nbQueen < len(self.tabBoard):
            return False, nbQueen
        return self.allQueensSafes(), nbQueen

    # Print the board
    def __repr__(self, showHeatMap=0):
        printLine = ""
        for line in self.tabBoard:
            for place in line:
                printLine += " " + str(1 if place == 1 else 0)
            printLine += "\n"
        return printLine.rstrip("\n")

    # Update the risk board
    def riskMap(self):
        self.riskBoard = Board.blankBoard(self.board_size)
        queensTab = self.findQueens()
        for queenPos in queensTab:
            self.heatUp(queenPos[0], queenPos[1])

    # Return a blank board
    def blankBoard(size):
        return [[0 for x in range(size)] for y in range(size)]

    # Update the risk board for a given position
    def heatUp(self, line, col):
        for distance in range(1, self.board_size):
            if line-distance >= 0:
                if col-distance >= 0:
                    self.riskBoard[line-distance][col-distance] += 1
                if col+distance < self.board_size:
                    self.riskBoard[line-distance][col+distance] += 1
            if line+distance < self.board_size:
                if col-distance >= 0:
                    self.riskBoard[line+distance][col-distance] += 1
                if col+distance < self.board_size:
                    self.riskBoard[line+distance][col+distance] += 1
            if col-distance >= 0:
                self.riskBoard[line][col-distance] += 1
            if col+distance < self.board_size:
                self.riskBoard[line][col+distance] += 1


def solve_n_queen_small(board_size, board):
    theBoard = Board(board)
    return theBoard.worst_QueenFinder()


def solve_n_queen_big(board_size, board):
    return None, False


def solve_n_queen_all_soluce(board_size, board):
    theBoard = Board(board)
    return theBoard.all_QueenFinder()


def can_t_attack(board_size, board):
    theBoard = Board(board)
    return theBoard.allQueensSafes()


def is_soluce(board_size, board):
    theBoard = Board(board)
    return theBoard.isSoluce()


def print_board(board_size, board):
    theBoard = Board(board)
    print(theBoard)
