class Match:
    def __init__(self, players, completed=False, winner=None):
        self.players = players
        self.completed = completed
        self.winner = winner
        self.match_score = {players[0]: 0.0, players[1]: 0.0}

    def set_result(self, winner=None):
        if winner is not None:
            self.match_winner(winner)
        elif winner is None:
            self.match_draw()

    def match_winner(self, winner):
        self.winner = winner
        self.completed = True

        self.set_match_score()

    def match_draw(self):
        self.completed = True
        self.winner = None

        self.set_match_score()

    def set_match_score(self):
        """
        This is automatically called after setting the winner (or tie)
        """
        for player in self.players:
            self.match_score[player] = 0
        if self.completed is True and self.winner is None:
            self.match_score[self.players[0]] = 0.5
            self.match_score[self.players[1]] = 0.5
        elif self.completed is True:
            self.match_score[self.winner] = 1.0

        """
        Add function to automatically update tournament scores
        """

    def match_results(self):
        if self.completed is True and self.winner is not None:
            print(f"The winner of the match between {self.players[0]} and {self.players[1]} is {self.winner}!")
        elif self.completed is True and self.winner is None:
            print(f"The match between {self.players[0]} and {self.players[1]} resulted in a tie.")
        else:
            print("This match is not over yet.")

    def match_serialize(self):
        if self.winner is not None:
            return {"players": [player.chess_id for player in self.players],
                    "completed": self.completed,
                    "winner": self.winner.chess_id}
        else:
            return {"players": [player.chess_id for player in self.players],
                    "completed": self.completed,
                    "winner": self.winner}
