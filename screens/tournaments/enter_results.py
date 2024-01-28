from commands import MatchResultCmd, NoopCmd

from ..base_screen import BaseScreen


class EnterResults(BaseScreen):
    def __init__(self, tournament, value):
        self.tournament = tournament
        self.value = value
        self.matches = tournament.rounds[tournament.current_round - 1].matches
        self.completed_matches = []
        for match in self.matches:
            if match.completed is True:
                self.completed_matches.append(match)

    def get_command(self):
        value = self.value
        while True:
            if value.isdigit():
                value = int(value)
                if value in range(1, len(self.matches) + 1):
                    match = self.matches[value - 1]
                    print("Type a number to enter the winner, or 'D' if it was a draw.")
                    print("Type 'B' to go back.")
                    for idx, player in enumerate(match.players, 1):
                        print(str(idx) + ".", player.name)
                    value = self.input_string()
                    if value.isdigit():
                        value = int(value)
                        return MatchResultCmd(self.tournament, match, self.value, winner=match.players[value - 1])
                    elif value.upper() == "D":
                        return MatchResultCmd(self.tournament, match, self.value)
                    elif value.upper() == "B":
                        return NoopCmd("match-results", tournament=self.tournament)

            elif value.upper() == "A":
                if len(self.matches) == len(self.completed_matches):
                    return NoopCmd("match-results", tournament=self.tournament)
                print("Type a number to enter the winner, or 'D' if it was a draw.")
                for match in self.matches:
                    if match.completed is True:
                        continue
                    for idx, player in enumerate(match.players, 1):
                        print(str(idx) + ".", player.name)
                    value = self.input_string()
                    if value.isdigit():
                        value = int(value)
                        return MatchResultCmd(self.tournament, match, self.value, winner=match.players[value - 1])
                    elif value.upper() == "D":
                        return MatchResultCmd(self.tournament, match, self.value)
