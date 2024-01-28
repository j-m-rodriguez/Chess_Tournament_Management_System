from commands.context import Context

from .base import BaseCommand


class AdvanceRoundCmd(BaseCommand):
    def __init__(self, tournament):
        self.tournament = tournament

    def execute(self):
        self.tournament.advance_to_next_round()
        if self.tournament.completed is False:
            return Context("tournament-view", tournament=self.tournament)
        elif self.tournament.completed is True:
            return Context("tournament-complete")
