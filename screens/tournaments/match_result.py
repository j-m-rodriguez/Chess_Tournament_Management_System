from commands import MatchResultCmd

from ..base_screen import BaseScreen


class MatchResult(BaseScreen):
    """Screen displayed when entering the outcome of a match"""

    display = "## Enter the Chess ID of the winner or D if it was a draw"

    def get_command(self):
        print("Type in the result")
        name = self.input_string()

        return MatchResultCmd(name)
