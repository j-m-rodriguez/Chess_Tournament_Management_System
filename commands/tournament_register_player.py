from commands.context import Context

from .base import BaseCommand


class RegisterPlayerCmd(BaseCommand):
    """Command to register player for a tournament"""

    def __init__(self, tournament, player):
        self.tournament = tournament
        self.player = player

    def execute(self):
        self.tournament.register_player(self.player)
        return Context("tournament-view", tournament=self.tournament)
