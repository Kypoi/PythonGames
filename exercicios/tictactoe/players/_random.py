from random import randint

from exercicios.tictactoe.action import TicTacToeAction
from exercicios.tictactoe.player import TicTacToePlayer
from exercicios.tictactoe.state import TicTacToeState
from exercicios.tictactoe.state import State


class RandomTicTacToePlayer(TicTacToePlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TicTacToeState):
        return TicTacToeAction(randint(0, state.get_num_cols()),state.get_num_cols())

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
