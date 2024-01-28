from commands.context import Context
from models import TournamentManager

from .base import BaseCommand


class TournamentCreateCmd(BaseCommand):
    """Command to create a tournament"""

    def __init__(self, name, **data):
        self.name = name
        self.data = data

    def execute(self):
        tm = TournamentManager()
        tournament = tm.create(name=self.name, **self.data)
        return Context("tournament-view", tournament=tournament)
