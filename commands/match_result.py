from commands.context import Context

from .base import BaseCommand


class MatchResultCmd(BaseCommand):
    """Command to get results of a match"""

    def __init__(self, tournament, match, value, winner=None):
        self.tournament = tournament
        self.match = match
        self.value = value
        self.winner = winner

    def execute(self):
        self.match.set_result(winner=self.winner)
        self.tournament.load_tournament_score()
        if self.value.isdigit():
            return Context("match-results", tournament=self.tournament)
        elif self.value.upper() == "C":
            return Context("enter-results", tournament=self.tournament, value=self.value)
