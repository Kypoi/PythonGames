from exercicios.tictactoe.players.greedy import GreedyTicTacToePlayer
from exercicios.tictactoe.players.minimax import MinimaxTicTacToePlayer
from exercicios.tictactoe.players._random import RandomTicTacToePlayer
from exercicios.tictactoe.simulator import TicTacToeSimulator
from exercicios.game_simulator import GameSimulator


def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA exercicios Simulator")

    num_iterations = 1000

    c4_simulations = [
        # uncomment to play as human
        # {
        #    "name": "tictactoe - Human VS Random",
        #    "player1": HumantictactoePlayer("Human"),
        #    "player2": RandomTicTacToePlayer("Random")
        # },
        {
            "name": "tictactoe - Random VS Random",
            "player1": RandomTicTacToePlayer("Random 1"),
            "player2": RandomTicTacToePlayer("Random 2")
        },
        {
            "name": "tictactoe - Greedy VS Random",
            "player1": GreedyTicTacToePlayer("Greedy"),
            "player2": RandomTicTacToePlayer("Random")
        },
        {
            "name": "Minimax VS Random",
            "player1": MinimaxTicTacToePlayer("Minimax"),
            "player2": RandomTicTacToePlayer("Random")
        },
        {
            "name": "Minimax VS Greedy",
            "player1": MinimaxTicTacToePlayer("Minimax"),
            "player2": GreedyTicTacToePlayer("Greedy")
        }
    ]

    for sim in c4_simulations:
        run_simulation(sim["name"], TicTacToeSimulator(sim["player1"], sim["player2"]), num_iterations)


if __name__ == "__main__":
    main()
