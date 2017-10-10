class Settings():
    """Class to store settings for game"""

    def __init__(self):
        """ Initialize game settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (40, 40, 40)
        self.caption = "Rocket"

        # Rocket settings
        self.speed_factor = 2
