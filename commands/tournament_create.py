#from commands.context import Context
#from models import Tournament

from .base import BaseCommand


class TournamentCreateCmd(BaseCommand):
    """Command to create a tournament"""

    def __init__(self, name):
        self.name = name

    def execute(self):
        pass
