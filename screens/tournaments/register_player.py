from commands import NoopCmd, RegisterPlayerCmd

from ..base_screen import BaseScreen


class RegisterPlayer(BaseScreen):
    """Screen displayed when registering a player"""

    def __init__(self, tournament, players):
        self.tournament = tournament
        self.players = players

    def display(self):
        print("\nAvailable players:")
        for idx, player in enumerate(self.players, 1):
            print(str(idx) + ".", player.name + ":", player.chess_id)

    def get_command(self):
        while True:
            print("Type the player's number to register them for the tournament or type 'B' to go back.")
            value = self.input_string()

            if value.isdigit():
                value = int(value)
                if value in range(1, len(self.players) + 1):
                    return RegisterPlayerCmd(self.tournament, self.players[value - 1])

            elif value.upper() == "B":
                return NoopCmd("find-player", tournament=self.tournament)
