from commands.context import Context
from .base import BaseCommand


class MatchListCmd(BaseCommand):
    def __init__(self, tournament):
        self.tournament = tournament
        self.ongoing_round = self.tournament.rounds[self.tournament.current_round - 1]
        self.ongoing_matches = self.ongoing_round.matches

    def execute(self):
        return Context("match-result", tournament=self.tournament,
                       round=self.ongoing_round, matches=self.ongoing_matches)
