#from commands.context import Context
#from models import Tournament

from .base import BaseCommand


class MatchResultCmd(BaseCommand):
    """Command to get results of a match"""

    def __init__(self, name):
        self.name = name

    def execute(self):
        pass
