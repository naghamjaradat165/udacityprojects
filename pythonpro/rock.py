import random
import time

# Constants for game moves
MOVES = ["rock", "paper", "scissors"]
VALID_INPUTS = {
    "r": "rock",
    "p": "paper",
    "s": "scissors",
    "rock": "rock",
    "paper": "paper",
    "scissors": "scissors"
}


class Player:
    """Base class for all players."""

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.previous_move = None
        self.move_history = []

    def get_move(self):
        """Get the player's move."""
        raise NotImplementedError

    def remember(self, opponent_move):
        """Remember opponent's move."""
        raise NotImplementedError


class HumanPlayer(Player):

    def get_move(self):
        while True:
            move = input("\nEnter your move (rock/paper/scissors "
                         "or r/p/s): ").lower()
            if move in VALID_INPUTS:
                return VALID_INPUTS[move]
            print("Invalid move! Please try again.")

    def remember(self, opponent_move):
        """Human players don't need to remember moves."""
        pass


class ReflectPlayer(Player):
    """Counters the opponent's last move by playing what beats it."""

    def get_move(self):
        if self.previous_move:
            return self.previous_move  # Return the opponent's previous move
        return random.choice(MOVES)

    def remember(self, opponent_move):
        self.previous_move = opponent_move


class RockPlayer(Player):
    """Computer player that always plays rock."""

    def get_move(self):
        return "rock"

    def remember(self, opponent_move):
        pass


class RandomPlayer(Player):
    """Computer player that chooses moves randomly."""

    def get_move(self):
        return random.choice(MOVES)

    def remember(self, opponent_move):
        pass


class CyclePlayer(Player):
    """Computer player that cycles through moves in order."""

    def __init__(self, name):
        super().__init__(name)
        self.move_cycle = ["rock", "paper", "scissors"]
        self.current_move_index = 0

    def get_move(self):
        move = self.move_cycle[self.current_move_index]
        self.current_move_index = (self.current_move_index + 1) % 3
        return move

    def remember(self, opponent_move):
        pass  # CyclePlayer doesn't need to remember opponent moves


class Game:
    """Main game class for Rock, Paper, Scissors."""

    def __init__(self, human_player, computer_player):
        self.human_player = human_player
        self.computer_player = computer_player
        self.round_number = 0

    def determine_winner(self, move1, move2):
        """Convert moves to numbers and determine winner."""
        move_values = {"rock": 0, "paper": 1, "scissors": 2}
        m1 = move_values[move1]
        m2 = move_values[move2]

        if m1 == m2:
            return 0
        if (m1 - m2) % 3 == 1:  # First player wins if difference is 1
            return 1
        return 2

    def play_round(self):
        self.round_number += 1
        print(f"\nRound {self.round_number}")

        human_move = self.human_player.get_move()
        print("\nRock...")
        time.sleep(0.5)
        print("Paper...")
        time.sleep(0.5)
        print("Scissors...")
        time.sleep(0.5)
        print("Shoot!\n")

        computer_move = self.computer_player.get_move()

        print(f"{self.human_player.name} chose: {human_move}")
        print(f"{self.computer_player.name} chose: {computer_move}")

        result = self.determine_winner(human_move, computer_move)

        if result == 0:
            print("\nIt's a tie!")
        elif result == 1:
            print(f"\n{self.human_player.name} wins this round!")
            self.human_player.score += 1
        else:
            print(f"\n{self.computer_player.name} wins this round!")
            self.computer_player.score += 1

        self.computer_player.remember(human_move)
        self.human_player.remember(computer_move)

        print("\nCurrent Score:")
        print(f"{self.human_player.name}: {self.human_player.score}")
        print(f"{self.computer_player.name}: {self.computer_player.score}")

    def play_match(self, num_rounds):
        print("\nWelcome to Rock, Paper, Scissors!")
        print(f"You'll be playing against {self.computer_player.name}")
        print(f"This match will be {num_rounds} rounds")

        for x in range(num_rounds):
            self.play_round()
            if x < num_rounds - 1:  # Don't ask after the last round
                if not self.continue_playing():
                    break

        self.display_final_results()

    def continue_playing(self):
        """Ask if player wants to continue."""
        while True:
            response = input("\nPress Enter to continue or "
                             "q to quit: ").lower()
            if response == 'q':
                return False
            if response == '':
                return True
            print("Invalid input. Please try again.")

    def display_final_results(self):
        """Display the final game results."""
        print("Game Over!")
        print(f"Final Score after {self.round_number} rounds:")
        print(f"{self.human_player.name}: {self.human_player.score}")
        print(f"{self.computer_player.name}: {self.computer_player.score}")

        if self.human_player.score > self.computer_player.score:
            print(f"\nCongrats! {self.human_player.name} wins")
        elif self.human_player.score < self.computer_player.score:
            print(f"\n{self.computer_player.name} wins the match!")
        else:
            print("\nThe match ends in a tie!")


def main():
    """Main function to run the game."""
    human_player = HumanPlayer("Human")

    computer_players = {
        1: ("Rock Player", RockPlayer),
        2: ("Random Player", RandomPlayer),
        3:  ("Reflect Player", ReflectPlayer),
        4: ("Cycle Player", CyclePlayer)
    }

    print("\nChoose your opponent:")
    for num, (name, _) in computer_players.items():
        print(f"{num}. {name}")

    while True:
        choice = int(input("Enter the number of your opponent (1-4): "))
        if choice in computer_players:
            break
        print("Please enter a number between 1 and 4.")

    player_name, player_class = computer_players[choice]
    computer_player = player_class(player_name)

    while True:
        rounds = int(input("\nchoose number of rounds (1-10): "))
        if 1 <= rounds <= 10:
            break
        print("Please enter a number between 1 and 10.")

    game = Game(human_player, computer_player)
    game.play_match(rounds)


if __name__ == "__main__":
    main()
