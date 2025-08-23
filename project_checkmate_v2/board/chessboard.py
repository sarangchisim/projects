from board.tile import Tile
from pieces.nullpiece import nullpiece
from pieces.queen import queen
from pieces.pawn import pawn
from pieces.rook import rook
from pieces.bishop import bishop
from pieces.king import king
from pieces.knight import knight
import random

class board:

    gameTiles = [[0 for x in range(8)] for y in range(8)]

    def __init__(self):
        pass

    def createboard(self):
        count = 0
        for rows in range(8):
            for column in range(8):
                self.gameTiles[rows][column] = Tile(count, nullpiece())
                count = count + 1

        
        black_major = [
            rook("Black", 0),
            knight("Black", 1),
            bishop("Black", 2),
            queen("Black", 3),
            king("Black", 4),
            bishop("Black", 5),
            knight("Black", 6),
            rook("Black", 7)
        ]
        random.shuffle(black_major)
        for col in range(8):
            self.gameTiles[0][col] = Tile(col, black_major[col])
            black_major[col].position = col 

        black_pawns = [pawn("Black", 8 + col) for col in range(8)]
        random.shuffle(black_pawns)  
        for col in range(8):
            self.gameTiles[1][col] = Tile(8 + col, black_pawns[col])
            black_pawns[col].position = 8 + col

        white_major = [
            rook("White", 56),
            knight("White", 57),
            bishop("White", 58),
            queen("White", 59),
            king("White", 60),
            bishop("White", 61),
            knight("White", 62),
            rook("White", 63)
        ]
        random.shuffle(white_major)
        for col in range(8):
            self.gameTiles[7][col] = Tile(56 + col, white_major[col])
            white_major[col].position = 56 + col  

        white_pawns = [pawn("White", 48 + col) for col in range(8)]
        random.shuffle(white_pawns)  
        for col in range(8):
            self.gameTiles[6][col] = Tile(48 + col, white_pawns[col])
            white_pawns[col].position = 48 + col

    def printboard(self):
        count = 0
        for rows in range(8):
            for column in range(8):
                print('|', end=self.gameTiles[rows][column].pieceonTile.tostring())
            print("|", end='\n')
