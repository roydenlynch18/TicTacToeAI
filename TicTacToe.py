import random

class Board:

    def __init__(self):
        self.grid = [ [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0] ]

    def checkWin(self):
        b = self.grid

        full=True
        for i in range(0,3):
            for j in range(0,3):
                if b[i][j] == 0:
                    full=False

        if b[0][0]==b[0][1] and b[0][1]==b[0][2] and b[0][0]!=0:
            return b[0][0]
        elif b[1][0]==b[1][1] and b[1][1]==b[1][2] and b[1][0]!=0:
            return b[1][0]
        elif b[2][0]==b[2][1] and b[2][1]==b[2][2] and b[2][0]!=0:
            return b[2][0]

        elif b[0][0]==b[1][0] and b[1][0]==b[2][0] and b[0][0]!=0:
            return b[0][0]
        elif b[0][1]==b[1][1] and b[1][1]==b[2][1] and b[0][1]!=0:
            return b[0][1]
        elif b[0][2]==b[1][2] and b[1][2]==b[2][2] and b[0][2]!=0:
            return b[0][2]

        elif b[0][0]==b[1][1] and b[1][1]==b[2][2] and b[0][0]!=0:
            return b[0][0]
        elif b[0][2]==b[1][1] and b[1][1]==b[2][0] and b[0][2]!=0:
            return b[0][2]
        
        elif full==True:
            return 0
        
        else:
            return -1
    
    def placeMove(self, player, pos):
        self.grid[pos[0]][pos[1]] = player

    def getBoard(self):
        return self.grid

class Player:
    
    def __init__(self, number):
        self.number = number
    
    def doTurn(self, b):
        possibleMoves = []
        for i in range(0,3):
            for j in range(0,3):
                if b.getBoard()[i][j] == 0:
                    possibleMoves.append([i,j])
        random.shuffle(possibleMoves)
        move = possibleMoves[0]
        b.placeMove(self.number, move)

def showBoard(b):
    print(" %d | %d | %d " % (b[0][0], b[0][1], b[0][2]))
    print(" ------------ ")
    print(" %d | %d | %d " % (b[1][0], b[1][1], b[1][2]))
    print(" ------------ ")
    print(" %d | %d | %d " % (b[2][0], b[2][1], b[2][2]))
    print(" ")

def playGame(b, p1, p2):
    whosTurn=1
    done = False
    while not done:
        showBoard(b.getBoard())
        if whosTurn == 1:
            p1.doTurn(b)
            whosTurn=2
        else:
            p2.doTurn(b)
            whosTurn=1
        state = b.checkWin()
        if state==0:
            showBoard(b.getBoard())
            print("Game is over, it is a tie.")
            done=True
        elif state==1:
            showBoard(b.getBoard())
            print("Player 1 has won.")
            done=True
        elif state==2:
            showBoard(b.getBoard())
            print("Player 2 has won.")
            done=True

gameBoard = Board()
player1 = Player(1)
player2 = Player(2)
playGame(gameBoard, player1, player2)

