from commands import NoopCmd

from ..base_screen import BaseScreen


class MatchResult(BaseScreen):
    """Screen displayed when entering the outcome of a match"""
    def __init__(self, tournament):
        self.tournament = tournament
        self.matches = tournament.rounds[tournament.current_round - 1].matches

    def display(self):
        print(f"\nRound #{self.tournament.current_round} matches:")
        for idx, match in enumerate(self.matches, 1):
            print(str(idx)+".", match.players[0].name, "vs", match.players[1].name+",",
                  f"Winner: {match.winner}" if match.winner else "Draw")

    def get_command(self):
        while True:
            for match in self.matches:
                if match.completed is False:
                    prompt = ("Enter the number of the match you would like to edit, "
                              "type 'A' to enter all remaining match results, or type 'B' to go back.")
                    break
                else:
                    prompt = ("All of the matches for this round have been completed\n"
                              "Enter the number of the match you would like to change, or type 'B' to go back.")
            print(prompt)
            print("[Back]")
            value = self.input_string()

            if value.upper() == "B":
                return NoopCmd("tournament-view", tournament=self.tournament)
            elif value.isdigit() or value.upper() == "A":
                return NoopCmd("enter-results", tournament=self.tournament, value=value)
