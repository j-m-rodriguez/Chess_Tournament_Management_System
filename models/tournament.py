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

    def __init__(self, filepath=None, name=None, start_date="", end_date="", venue="", number_of_rounds=1):
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
        self.number_of_rounds = int(number_of_rounds)
        self.current_round = 0
        self.completed = False
        self.players = []
        self.scores = {}
        self.ranking = {}
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
                found_players = []
                for player in data["players"]:
                    found_players.append(SearchPlayer(player).player)
                self.players.extend(found_players)
                for player in self.players:
                    self.scores[player] = 0
                round_number = 1
                for json_round in data["rounds"]:
                    tourney_round = Round(current_round=round_number)
                    round_number += 1
                    self.rounds.append(tourney_round)
                    for json_match in json_round:
                        match_players = []
                        for player in json_match["players"]:
                            match_players.append(SearchPlayer(player).player)
                        match = Match(match_players, completed=json_match["completed"],
                                      winner=SearchPlayer(json_match["winner"]).player)
                        tourney_round.matches.append(match)
                self.load_tournament_score()

        elif not filepath:
            # We did not have a file, so we are going to create it by running the save method
            self.save()

    def save(self):
        """Saves the tournament info to the JSON file"""

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
                    "rounds": [tourney_round.round_serialize() for tourney_round in self.rounds]
                },
                fp, indent=4
            )

    # need to redo after changing self.players to Player instances
    def register_player(self, player):
        if type(player) is Player:
            self.players.append(player)
        else:
            player = SearchPlayer(player)
            self.players.append(player)
        self.scores[player] = 0
        self.save()
        return player

    # redo after changing self.players to Player instances
    def load_tournament_score(self):
        """For setting player scores based on json data"""
        for score in self.scores:
            self.scores[score] = 0
        for each_round in self.rounds:
            for match in each_round.matches:
                match.set_match_score()
                for player, score in match.match_score.items():
                    self.scores[player] += score
        self.ranking = dict(sorted(self.scores.items(), key=lambda x: x[1], reverse=True))
        self.save()

    def advance_to_next_round(self):
        if self.current_round == self.number_of_rounds:
            self.end_tournament()
        else:
            for match in self.rounds[self.current_round - 1].matches:
                if match.completed is True:
                    done = True
                else:
                    print("Please complete all matches before advancing to the next round.")
                    break
            if done:
                self.current_round += 1
                next_round = Round(current_round=self.current_round)
                next_round.players = self.players
                next_round.matchmaking(self.players, self.ranking)
                self.rounds.append(next_round)
        self.save()

    def end_tournament(self):
        self.completed = True
        self.current_round = None

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
