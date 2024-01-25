import json
from datetime import datetime
from .player import Player
from .round import Round
from .match import Match
from .search_player import SearchPlayer


class Tournament:
    """
    Data is loaded from a JSON file (provided as argument).
    The class creates Player instances based on JSON data.
    """

    DATE_FORMAT = "%d-%m-%Y"

    def __init__(self, filepath="", name="", start_date=None, end_date=None, venue="", number_of_rounds=0):
        """The constructor works in two ways:
        - if the filepath is provided, it loads data from JSON
        - if it is not but a name is provided, it creates a new tournament (and a new JSON file)
        """

        self.name = name
        self.filepath = filepath

        self.start_date = start_date
        self.end_date = end_date
        self.dates = {"from": self.start_date, "to": self.end_date}
        self.venue = venue
        self.number_of_rounds = number_of_rounds
        self.current_round = None
        self.completed = False
        self.players = []
        self.scores = {}
        self.finished = False
        self.rounds = []

        if filepath and not name:
            # Load data from the JSON file
            with open(filepath) as fp:
                data = json.load(fp)
                self.name = data["name"]
                self.dates = data["dates"]
                self.start_date = data["dates"]["from"]
                self.end_date = data["dates"]["to"]
                self.venue = data["venue"]
                self.number_of_rounds = data["number_of_rounds"]
                self.current_round = data["current_round"]
                self.completed = data["completed"]
                for player in data["players"]:
                    self.players.extend(SearchPlayer(player).players)
                self.finished = data["finished"]

                round_number = 1
                for json_round in data["rounds"]:
                    tourney_round = Round(1)
                    round_number += 1
                    self.rounds.append(tourney_round)
                    for json_match in json_round:
                        match = Match(json_match["players"], completed=json_match["completed"],
                                      winner=json_match["winner"])
                        tourney_round.matches.append(match)
                self.load_tournament_score(data)

        elif not filepath:
            # We did not have a file, so we are going to create it by running the save method
            self.save()

    def save(self):
        """Saves the tournament info to the JSON file"""

        if self.filepath is None:
            self.filepath = "../data/tournaments/" + self.name + ".json"

        with open(self.filepath, "w") as fp:
            json.dump(
                {
                    "name": self.name,
                    "dates": self.dates,
                    "venue": self.venue,
                    "number_of_rounds": self.number_of_rounds,
                    "current_round": self.current_round,
                    "completed": self.completed,
                    "players": [player.chess_id for player in self.players],
                    "finished": self.finished,
                    "rounds": [tourney_round.round_serialize() for tourney_round in self.rounds]
                },
                fp, indent=4
            )

    @property
    def start(self):
        """Property to get the start date (string) from the start date (datetime)"""
        return self.start_date.strftime(self.DATE_FORMAT)

    @start.setter
    def start(self, value):
        """Sets the start date (datetime) from a string"""
        self.start_date = datetime.strptime(value, self.DATE_FORMAT)

    @property
    def end(self):
        """Property to get the end date (string) from the end date (datetime)"""
        return self.end_date.strftime(self.DATE_FORMAT)

    @end.setter
    def end(self, value):
        """Sets the end date (datetime) from a string"""
        self.end_date = datetime.strptime(value, self.DATE_FORMAT)

    # need to redo after changing self.players to Player instances
    def register_player(self, player):
        if type(player) is Player:
            self.players[player.chess_id] = 0.0
        else:
            self.players[player] = 0.0
        self.save()
        return player

    # redo after changing self.players to Player instances
    def load_tournament_score(self, data):
        """For setting player scores based on json data"""
        for each_round in data["rounds"]:
            for match in each_round:
                if match["completed"] is True:
                    load_match = Match(match["players"],
                                       completed=match["completed"],
                                       winner=match["winner"]
                                       )
                    load_match.set_match_score()
                    self.update_tournament_score(load_match.match_score)

    # not sure if I need to redo
    def update_tournament_score(self, match_score):
        """Updates player scores after match completion"""
        for k, v in match_score.items():
            self.players[k] += v

    def advance_to_next_round(self):
        pass
        """
        come back and do this later
        """
