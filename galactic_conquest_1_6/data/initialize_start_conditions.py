from random import *
from galactic_conquest_1_6.game.defaults.unit_default import UnitTemplate
from galactic_conquest_1_6.game.general_functions import spawn_garrison
from galactic_conquest_1_6.game.defaults.faction_default import FactionTemplate

def create_starting_garrisons(file):
    for _planet in file.planets:
        _num_starting_units = randint(0, 3)
        _faction = _planet.faction
        for _num in range(_num_starting_units):
            _unit = spawn_garrison(file, _planet, _planet.faction, randint(500, 600))
            # print(_unit.name + " made on " + _planet.name + " of faction " + _planet.faction.name + " P:U " + _unit.faction.name)

def create_starting_factions(file):
    file.factions.append(FactionTemplate())
    file.factions[0].name = "Galactic Alliance"
    file.factions[0].owning_player = None
    file.factions[0].color = 'DarkGreen'

    file.factions.append(FactionTemplate())
    file.factions[1].name = "Rebellion"
    file.factions[1].owning_player = None
    file.factions[1].color = 'DarkRed'

    file.factions.append(FactionTemplate())
    file.factions[2].name = "test3"
    file.factions[2].owning_player = None
    file.factions[2].color = 'Orange'

    file.factions.append(FactionTemplate())
    file.factions[3].name = "test4"
    file.factions[3].owning_player = None
    file.factions[3].color = 'Pink'

    file.factions.append(FactionTemplate())
    file.factions[4].name = "test5"
    file.factions[4].owning_player = None
    file.factions[4].color = 'Blue'

    file.factions.append(FactionTemplate())
    file.factions[5].name = "test6"
    file.factions[5].owning_player = None
    file.factions[5].color = 'Purple'

    return file.factions
