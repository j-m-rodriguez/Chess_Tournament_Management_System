from commands import NoopCmd, TournamentListCmd

from ..base_screen import BaseScreen


class TournamentView(BaseScreen):
    """Screen displayed when viewing a Tournament"""

    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):
        print("")
        print("##", self.tournament.name)
        print("Start date:", self.tournament.start_date, "  End date:", self.tournament.end_date)
        #self.tournament.dates
        print("Rounds:", self.tournament.number_of_rounds)
        print("Current Round:", self.tournament.current_round)
        print("Venue:", self.tournament.venue)
        print("Players:", *self.tournament.players)

    def get_command(self):
        """Gets the command for this screen"""
        while True:
            print("Type 'P' to register a player")
            print("Type 'M' to enter results of the matches for the current round")
            print("Type 'A' to advance to the next round")
            print("Type 'R' to generate a tournament report")
            print("Type 'B' to go back to the tournament main menu.")
            action = self.input_string()

            # Need to come back and update all return values after creating commands
            if action.upper() == "B":
                return TournamentListCmd()
            elif action.upper() == "P":
                return NoopCmd("register-player", tournament=self.tournament)
            elif action.upper() == "M":
                return NoopCmd("enter-match-results")
            elif action.upper() == "A":
                return NoopCmd("advance-round")
            elif action.upper() == "R":
                return NoopCmd("player-edit")