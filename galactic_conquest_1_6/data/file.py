from galactic_conquest_1_6.game.defaults.planet_default import PlanetTemplate
from galactic_conquest_1_6.game.defaults.faction_default import FactionTemplate
from galactic_conquest_1_6.game.defaults.player_default import PlayerTemplate
from galactic_conquest_1_6.game.turn_manager import TurnManager
from galactic_conquest_1_6.data.initialize_start_conditions import create_starting_factions
from random import choice

# available colors here:
# https://www.quackit.com/css/css_color_codes.cfm#:~:text=Basic%20CSS%20Colors%20%20%20%20Color%20Name,%20%200%2C128%2C128%20%202%20more%20rows%20

class File:
    def __init__(self):
        # Instantiate the players
        self.players = []
        self.application = None  # UI loaded here

        # Faction pool
        self.factions = []
        self.factions = create_starting_factions(self)

        # A player is defined as a human or AI that controls a united group
        self.total_players_generated = 3
        self.human_players = 1

        _used_factions = []
        if self.human_players >= 1:
            self.players.append(PlayerTemplate(False))
            # Assign player 0 (you) as the galactic alliance for testing purposes
            self.players[0].faction = self.factions[0]
            _used_factions.append(self.players[0].faction.name)
            #self.players[0].faction.name = "Galactic Alliance"

        # Generate AI players
        for _index in range(0, self.total_players_generated-self.human_players):
            self.players.append(PlayerTemplate())
            _check = True
            while _check:
                self.players[_index+self.human_players].faction = choice(self.factions)
                if self.players[_index+self.human_players].faction.name not in _used_factions:
                    _check = False
                    _used_factions.append(self.players[_index+self.human_players].faction.name)



        # Instantiate the planets
        self.planets = []
        self.active_planet = None

        # generate planets into an array
        self.total_planets_generated = 100  # Max reasonable amount for reasonable distance is 135 planets w/ 200d
        self.planet_distance = 200
        self.planet_distance_neighbor = 5000
        for index in range(0, self.total_planets_generated):
            self.planets.append(PlanetTemplate(self.application))
            pass

        self.active_planet = None

        self.turn_manager = TurnManager(self)
        #
        # # Starting condictions data
        for _planet in self.planets:
            _planet.faction = choice(self.factions)



        # Define what each screen is here as it will not change
        # Dictionary helps to easily identify to programmer what screen is being displayed with a numerical identifier assigned to it
        # Must update everytime you add a new screen so it can track its ID number. Should match in QT Designer
        self.screen_Dictionary = {
            "Menu": 0,
            "Map": 1,
            "Planet": 2,
            "PlanetGround": 3
        }

        # Movement
        self.movement_start = None
        self.movement_end = None