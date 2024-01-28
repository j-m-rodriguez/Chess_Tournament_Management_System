from commands import TournamentCreateCmd

from ..base_screen import BaseScreen


class TournamentCreate(BaseScreen):
    """Screen displayed when creating a tournament"""

    display = "## Create tournament"

    def get_command(self):
        """Goes through the attributes and gets them from the user"""
        attrs = [
            ("start_date", "Start Date", self.input_string),
            ("end_date", "End Date", self.input_string),
            ("venue", "Venue", self.input_string),
            ("number_of_rounds", "Number of Rounds", self.input_string)
        ]

        data = {}
        name = self.input_string("Tournament Name")
        for key, prompt, func in attrs:
            kwargs = {"prompt": prompt}
            data[key] = func(**kwargs)

        return TournamentCreateCmd(name, **data)

    """
    def get_command(self):
        print("Type in the name of the tournament")
        name = self.input_string()

        return TournamentCreateCmd(name)
    """
