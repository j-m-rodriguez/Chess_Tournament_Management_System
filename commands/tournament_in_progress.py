from commands.context import Context
from commands.tournament_list import TournamentListCmd
from models import TournamentManager

from .base import BaseCommand


class TournamentStart(BaseCommand):
    """Command to check if there is only 1 tournament in progress"""

    def execute(self):
        tm = TournamentManager()
        if len(tm.in_progress) == 1:
            return Context("tournament-view", tournament=tm.in_progress[0])
        else:
            return TournamentListCmd()
