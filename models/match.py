class Match:
    def __init__(self, players, completed=False, winner=None):
        self.players = players
        self.completed = completed
        self.winner = winner
        self.match_score = {players[0]: 0.0, players[1]: 0.0}

    def match_winner(self, winner):
        self.winner = self.players[winner]
        self.completed = True

        self.set_match_score()
        """
        assign scores based on match outcome
        dictionary playerID : score
        """

    def match_draw(self):
        self.completed = True
        self.winner = None

        self.set_match_score()

    def set_match_score(self):
        """
        This is automatically called after setting the winner (or tie)
        """
        if self.completed is True and self.winner is None:
            self.match_score[self.players[0]] = 0.5
            self.match_score[self.players[1]] = 0.5
        elif self.completed is True and self.winner is not None:
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
        return {"players": self.players, "completed": self.completed, "winner": self.winner}
