from commands.context import Context
from models import ClubManager, SearchPlayer

from .base import BaseCommand


class PlayerListCmd(BaseCommand):
    """Command to get the list of players"""

    def __init__(self, tournament, player=None):
        self.tournament = tournament
        self.player = player
        self.players = []

    def execute(self):
        if self.player is not None:
            self.players = SearchPlayer(self.player).players
            if len(self.players) == 0:
                return Context("find-player", tournament=self.tournament)
            else:
                return Context("register-player", tournament=self.tournament, players=self.players)

        else:
            cm = ClubManager()
            for club in cm.clubs:
                self.players.extend(club.players)
            self.players.sort(key=lambda x: x.name)
            return Context("register-player", tournament=self.tournament, players=self.players)
