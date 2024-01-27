from commands import PlayerListCmd, NoopCmd

from ..base_screen import BaseScreen


class FindPlayer(BaseScreen):
    """Screen displayed when registering a player"""

    def __init__(self, tournament, player=None):
        self.tournament = tournament
        self.player = player

    display = "## Registering for the tournament"

    def get_command(self):
        while True:
            print("Type 'A' to view a list of all available players")
            print("Type 'S' to search for a specific player.")
            print("Type 'B' to go back.")

            action = self.input_string()

            if action.upper() == "A":
                return PlayerListCmd(self.tournament)
            elif action.upper() == "S":
                print("Type a portion of the player's name or their full Chess ID")
                action = self.input_string()
                return PlayerListCmd(self.tournament, player=action)
            elif action.upper() == "B":
                return NoopCmd("tournament-view", tournament=self.tournament)
