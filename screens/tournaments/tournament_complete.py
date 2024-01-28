from commands import ExitCmd, TournamentListCmd

from ..base_screen import BaseScreen


class TournamentComplete(BaseScreen):
    def __init__(self):
        pass

    def get_command(self):
        print("The tournament is now complete.\n"
              "Type 'X' to exit the application or type any key to see the list of available tournaments")

        value = self.input_string()

        if value.upper() == "X":
            return ExitCmd()
        else:
            return TournamentListCmd()
