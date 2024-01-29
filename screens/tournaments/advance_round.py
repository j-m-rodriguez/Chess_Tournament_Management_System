from commands import NoopCmd, AdvanceRoundCmd

from ..base_screen import BaseScreen


class AdvanceRound(BaseScreen):
    """Screen displayed when advancing to the next round in a tournament"""

    def __init__(self, tournament):
        self.tournament = tournament

    display = "\nAdvancing to the next round"

    def get_command(self):
        print("Type 'C' to continue or 'B' to go back.")
        value = self.input_string()
        if value.upper() == "C":
            return AdvanceRoundCmd(tournament=self.tournament)
        if value.upper() == "B":
            return NoopCmd("tournament-view", tournament=self.tournament)
