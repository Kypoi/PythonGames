from abc import ABC

from exercicios.tictactoe.result import TicTacToeResult
from exercicios.player import Player


class TicTacToePlayer(Player, ABC):

    def __init__(self, name):
        super().__init__(name)

        """
        stats is a dictionary that will store the number of times each result occurred
        """
        self.__stats = {}
        for tictactoeres in TicTacToeResult:
            self.__stats[tictactoeres] = 0

        """
        here we are storing the number of games
        """
        self.__num_games = 0

    def print_stats(self):
        num_wins = self.__stats[TicTacToeResult.WIN]
        print(
            f"Player {self.get_name()}: {num_wins}/{self.__num_games} wins ({num_wins * 100.0 / self.__num_games} win "
            f"rate)")

    def event_new_game(self):
        self.__num_games += 1

    def event_result(self, pos: int, result: TicTacToeResult):
        if pos == self.get_current_pos():
            self.__stats[result] += 1
