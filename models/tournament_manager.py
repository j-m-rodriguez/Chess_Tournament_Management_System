import json
from pathlib import Path
import operator

from .tournament import Tournament


class TournamentManager:
    def __init__(self, data_folder="data/tournaments"):
        datadir = Path(data_folder)
        self.data_folder = datadir
        self.tournaments = []
        self.tournament_dates = []
        for filepath in datadir.iterdir():
            if filepath.is_file() and filepath.suffix == ".json":
                try:
                    self.tournaments.append(Tournament(filepath))
                except json.JSONDecodeError:
                    print(filepath, "is invalid JSON file.")
        self.tournaments.sort(key=lambda x: x.start_date, reverse=True)
        #for tournament in self.tournaments:
        #    self.tournament_dates.append([tournament.name, tournament.start_date])
        #self.tournament_dates = sorted(self.tournament_dates, key=operator.itemgetter(1, 0), reverse=True)

    def create(self, name):
        filepath = self.data_folder / (name.replace(" ", "") + ".json")
        tournament = Tournament(name=name, filepath=filepath)
        tournament.save()

        self.tournaments.append(tournament)
        return tournament