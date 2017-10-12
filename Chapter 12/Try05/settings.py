class Settings():
    """Class to store game settings"""

    def __init__(self):
        """Init default settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (40, 40, 40)
        self.caption = "Sidways Shooter"

        # Ship settings
        self.ship_speed_factor = 1.5
