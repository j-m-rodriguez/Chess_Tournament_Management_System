from commands import NoopCmd

from ..base_screen import BaseScreen


class Report(BaseScreen):
    def __init__(self, tournament):
        self.tournament = tournament

    def display(self):
        print(f"\nTournament: {self.tournament.name}")
        print(f"Dates: {self.tournament.start_date} to {self.tournament.end_date}")
        print("\nRanking: ")
        for idx, player in enumerate(self.tournament.ranking, 1):
            print(idx, player, ":", self.tournament.scores[player], "point(s)")
        for round in self.tournament.rounds:
            print(f"\nRound #{round.current_round}")
            for match in round.matches:
                print(f"{match.players[0]} vs {match.players[1]}")

    def get_command(self):
        print("Type 'B' to go back.\n[Back]")
        value = self.input_string()
        if value.upper() == "B":
            return NoopCmd("tournament-view", tournament=self.tournament)
