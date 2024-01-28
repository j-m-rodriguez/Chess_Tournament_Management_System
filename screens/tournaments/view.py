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
        print("Rounds:", self.tournament.number_of_rounds)
        print("Current Round:", self.tournament.current_round)
        print("Venue:", self.tournament.venue)
        print("Players:", *self.tournament.players)

    def get_command(self):
        """Gets the command for this screen"""
        while True:
            print("Enter a number to select an option, or type 'B' to go back.")

            print("1. View a tournament report")
            if self.tournament.completed is False:
                print("2. Register a player for the tournament")
                print("3. Enter results of the matches for the current round")
                print("4. Advance to the next round")
            print("[Back]\n")
            action = self.input_string("What would you like to do")

            # Need to come back and update all return values after creating commands
            if action.upper() == "1":
                return NoopCmd("tournament-report", tournament=self.tournament)
            elif action.upper() == "B":
                return TournamentListCmd()
            elif self.tournament.completed is True:
                return NoopCmd("tournament-view", tournament=self.tournament)
            elif action.upper() == "2":
                return NoopCmd("find-player", tournament=self.tournament)
            elif action.upper() == "3":
                return NoopCmd("match-results", tournament=self.tournament)
            elif action.upper() == "4":
                return NoopCmd("advance-round", tournament=self.tournament)
