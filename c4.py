import random

class Connect4:
    def __init__(self, width, height, window=None):
        self.width = width
        self.height = height
        self.data = []
        for row in range(self.height):
            boardRow = []
            for col in range(self.width):
                boardRow += [' ']
            self.data += [boardRow]

    # Displays the game board based on height and width inputs
    def __repr__(self):
        s = ''
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.data[row][col] + '|'
            s += '\n'
        s += '--'*self.width + '-\n'
        for col in range(self.width):
            s += ' ' + str(col+1 % 10)
        s += '\n'
        return s

    # Clears Board
    def clear(self):
        self.data = []
        for row in range(self.height):
            boardRow = []
            for col in range(self.width):
                boardRow += [' ']
            self.data += [boardRow]

    # Checks if the column is full
    def allowsMove(self, col):
        if 0 <= col < self.width:
            return self.data[0][col] == ' '
        return False

    # Makes a move correlating to the game piece
    def addMove(self, col, ox):
        if self.allowsMove(col):
            for row in range(self.height):
                if self.data[row][col] != ' ':
                    self.data[row-1][col] = ox
                    return True
            self.data[self.height-1][col] = ox
            return True
        return False

    # Removes top checker piece from board if column if full
    def delMove(self, col):
        for row in range(self.height):
            if self.data[row][col] != ' ':
                self.data[row-self.height][col] = ' '
                return True
        return False

    # Checks if the column in the top rows are full
    def isFull(self):
        for col in range(0, self.width):
            if self.allowsMove(col):
                return False
        return True

    def winsFor(self, ox):
        # Checks for horizontal wins
        for row in range(0, self.height):
            for col in range(0, self.width-3):
                if self.data[row][col] == ox and \
                self.data[row][col+1] == ox and \
                self.data[row][col+2] == ox and \
                self.data[row][col+3] == ox:
                    return True
        # Checks for vertical wins
        for col in range(0, self.width):
            for row in range(0, self.height-3):
                if self.data[row][col] == ox and \
                self.data[row+1][col] == ox and \
                self.data[row+2][col] == ox and \
                self.data[row+3][col] == ox:
                    return True
        # Checks for diagonal win NW -> SE
        for row in range(0, self.height-3):
            for col in range(0, self.width-3):
                if self.data[row][col] == ox and \
                self.data[row+1][col+1] == ox and \
                self.data[row+2][col+2] == ox and \
                self.data[row+3][col+3] == ox:
                    return True
        # Checks for diagonal win NE -> SW
        for row in range(0, self.height-3):
            for col in range(3, self.width):
                if self.data[row][col] == ox and \
                self.data[row+1][col-1] == ox and \
                self.data[row+2][col-2] == ox and \
                self.data[row+3][col-3] == ox:
                    return True
        return False

    # Controls player turns
    def hostGame(self):
        currentTurn = 'x'
        while True:
            if self.winsFor('x'):
                print('Congrats player 1 has won!')
                print(self)
                break
            elif self.winsFor('o'):
                print('Congrats player 2 has won!')
                print(self)
                break
            if self.isFull():
                print('It is a tie')
                print(self)
                break
            if currentTurn == 'x':
                p1 = int(input('Enter a column value P1: '))
                if self.addMove(p1, currentTurn):
                    print(self)
                    currentTurn = 'o'
                else:
                    p1 = int(input('Please select a different column: '))
                    currentTurn = 'x'
            else:
                p2 = int(input('Enter a colum value P2: '))
                if self.addMove(p2, currentTurn):
                    print(self)
                    currentTurn = 'x'
                else:
                    p2 = int(input('Please select a different column: '))
                    currentTurn = 'o'

    # AI player
    def playGameWith(self, Player):
        currentTurn = 'x'
        while True:
            if self.winsFor('x'):
                print('Congrats player 1 has won!')
                print(self)
                break
            elif self.winsFor('o'):
                print('Congrats player 2 has won!')
                print(self)
                break
            if self.isFull():
                print('It is a tie')
                print(self)
                break
            if currentTurn == 'x':
                p1 = int(input('Enter a column value P1: '))
                if self.addMove(p1-1, currentTurn):
                    print(self)
                    currentTurn = 'o'
                else:
                    p1 = int(input('Please select a different column: '))
                    currentTurn = 'x'
            else:
                p2 = Player.nextMove(self)
                if self.addMove(p2, currentTurn):
                    print(self)
                    currentTurn = 'x'
                else:
                    p2 = Player.nextMove(self)
                    currentTurn = 'o'

class Player:
    def __init__(self, ox, tbt, ply):
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    # Probability of winning at ply 0
    def scoresBoard(self, board):
        scores = []
        for col in board.width:
            if board.allowsMove() == False:
                scores += [-1]
            else:
                if board.winsFor(self.ox):
                    scores += [100]
                elif board.winsFor(self.ox) == False:
                    scores += [0]
                else:
                    scores += [50]

    # Switches player pieces
    def switchPlayers(self, ox):
        if ox == 'o':
            return 'x'
        else:
            return 'o'

    # Returns a list of scores for each column
    def scoresFor(self, board, ox, ply):
        scores = []
        for col in range(board.width):
            if board.allowsMove(col) == False:
                scores += [-1]
            else:
                board.addMove(col, ox)
                if ply == 0:
                    if board.winsFor(ox):
                        scores += [100]
                    else:
                        scores += [50]
                elif ply > 0:
                    if board.winsFor(ox):
                        scores += [100]
                    else:
                        ox = self.switchPlayers(ox)
                        scores += [100 - max(self.scoresFor(board, ox, ply-1))]
                        ox = self.switchPlayers(ox)
                board.delMove(col)
        return scores

    # Gets the column number of the highest score position depending on tbt
    def tieBreakMove(self, scores):
        maxScoreList = []
        # Iterates through each column in the given list
        for colNum in range(len(scores)):
            # Assigns highest scores to the index of the original list of scores
            if scores[colNum] == max(scores):
                # Grabs the column number for the highest scores
                maxScoreList.append(colNum)
        # If left was selected then return the left most column number
        if self.tbt == 'Left':
            return maxScoreList[0]
        # If right was selected then return the right most column number
        elif self.tbt == 'Right':
            return maxScoreList[-1]
        # If random was selected then return a random column number
        else:
            return random.choice(maxScoreList)

    # Returns the best column number based on the best score
    def nextMove(self, board):
        L = self.scoresFor(board, 'o', self.ply)
        return self.tieBreakMove(L)

# Initialize game with board size and level of difficulty
def main():
    board = Connect4(7,6)
    p = Player('x', 'Left', 2)
    board.playGameWith(p)

if __name__ == '__main__':
    main()
