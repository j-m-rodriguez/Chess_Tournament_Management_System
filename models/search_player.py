import re

from .club_manager import ClubManager


class SearchPlayer:
    def __init__(self, identifier=""):
        self.identifier = identifier
        self.players = []
        self.player = None

        if self.identifier is None:
            pass
        elif re.fullmatch("[a-zA-Z]{2}[0-9]{5}", self.identifier):
            self.search_by_id()
        elif re.fullmatch(r"[a-zA-Z]+\s*[a-zA-Z]*", self.identifier):
            self.search_by_name()
        else:
            print("Invalid input")

    def search_by_id(self):
        """Searches the club database by player's Chess ID"""
        cm = ClubManager()
        for club in cm.clubs:
            for player in club.players:
                if self.identifier.upper() == player.chess_id:
                    self.players.append(player)
                    self.player = player
                    break
            if len(self.players) == 1:
                break
        if len(self.players) == 0:
            print(f"\nPlayer {self.identifier} was not found")

    def search_by_name(self):
        """Searches the club database by any portion of a player's name"""
        cm = ClubManager()
        for club in cm.clubs:
            for player in club.players:
                if re.search(self.identifier, player.name, re.IGNORECASE):
                    self.players.append(player)
                    self.player = player
        if len(self.players) == 0:
            print(f"\nPlayer {self.identifier} was not found")
