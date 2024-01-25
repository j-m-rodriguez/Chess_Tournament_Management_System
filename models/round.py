import random
from .match import Match


class Round:
    def __init__(self, current_round):
        self.current_round = current_round

        self.players = []
        self.matches = []
        self.ranking = []
        self.scores = {}

    def matchmaking(self):
        """
        move to Tournament
        """
        if self.current_round == 1:
            self.ranking = self.players.copy()
            random.shuffle(self.ranking)
        else:
            self.ranking = sorted(self.scores, key=lambda x: x[1], reverse=True)
        for i in range(0, len(self.ranking), 2):
            pair = self.ranking[i:i + 2]
            """
            Make list of these pairings
            checking for identical pairs in Tournament.rounds.matches
            take identical pairs and shuffle
            run matchmaking again
            """
            match = Match(pair)
            self.matches.append(match)

    def __str__(self):
        return f"{self.matches}"

    def round_serialize(self):
        """Use this to format tournament rounds/matches for json"""
        rounds = []
        for match in self.matches:
            rounds.append(match.match_serialize())
        return rounds
