from exercicios.tictactoe.player import TicTacToePlayer
from exercicios.tictactoe.state import TicTacToeState
from exercicios.game_simulator import GameSimulator


class TicTacToeSimulator(GameSimulator):

    def __init__(self, player1: TicTacToePlayer, player2: TicTacToePlayer, num_rows: int = 6, num_cols: int = 7):
        super(TicTacToeSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the TicTacToe grid
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

    def init_game(self):
        return TicTacToeState(self.__num_rows, self.__num_cols)

    def before_end_game(self, state: TicTacToeState):
        # ignored for this simulator
        pass

    def end_game(self, state: TicTacToeState):
        # ignored for this simulator
        pass
