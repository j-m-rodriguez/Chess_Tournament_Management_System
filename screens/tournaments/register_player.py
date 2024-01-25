#from commands import RegisterPlayerCmd

from ..base_screen import BaseScreen


class RegisterPlayer(BaseScreen):
    """Screen displayed when registering a player"""

    display = "## Enter the Chess ID  or name of the player you would like to register"

    def get_command(self):
        pass

