import random
from .match import Match


class Round:
    def __init__(self, current_round=1):
        self.current_round = current_round

        self.players = []
        self.matches = []
        self.ranking = []
        self.scores = {}

    def matchmaking(self, players, ranking):
        """
        move to Tournament
        """
        if self.current_round == 1:
            self.randomize(players)

        else:
            for i in range(0, len(ranking), 2):
                players = []
                for player in ranking.keys():
                    players.append(player)
                pair = players[i:i + 2]
                """
                Make list of these pairings
                checking for identical pairs in Tournament.rounds.matches
                take identical pairs and shuffle
                run matchmaking again
                """
                match = Match(pair)
                self.matches.append(match)

    def randomize(self, players):
        random.shuffle(players)
        for i in range(0, len(players), 2):
            pair = players[i:i + 2]
            match = Match(pair)
            self.matches.append(match)

    def __str__(self):
        for match in self.matches:
            return f"{match.players[0]} vs {match.players[1]}"

    def round_serialize(self):
        """Use this to format tournament rounds/matches for json"""
        rounds = []
        for match in self.matches:
            rounds.append(match.match_serialize())
        return rounds
