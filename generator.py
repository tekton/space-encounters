import random

LOWWORLDPOPGEN = (
	"0", 
	"1-1000", 
	"1001-5000"
	)
LowWorldPop = random.choice(LOWWORLDPOPGEN)

MEDWORLDPOPGEN = (  
	"5001-25000",
	"25001-100,000",
	"100,001-250,000",
	"250,001-500,000"
	)
MedWorldPop = random.choice(MEDWORLDPOPGEN)

HIGHWORLDPOPGEN = (  
	"500,001-1,000,000",
	"1MM-20MM",
	"21MM-100MM"
	"100MM-1B",
	"1B-8B"
	)
HighWorldPop = random.choice(HIGHWORLDPOPGEN)

ATMOGEN = (
	"Thin",
	"none",
	"Special"
	)
WorldAtmo = random.choice(ATMOGEN)

LIVINGWORLDATMOGEN = (
	"Thin",
	"Normal",
	"Special"
	)
LivingWorldAtmo = random.choice(LIVINGWORLDATMOGEN)

SHIPATMOGEN = (
	"Thin",
	"Normal",
	"Special",
	"None"
	)
ShipAtmo = random.choice(SHIPATMOGEN)

WORMHOLESIZEGEN = (
	"Tiny",
	"Small"
	"Medium",
	"Large",
	"Huge",
	"Gargantuan",
	"Collosal"
	)
WormholeSize = random.choice(WORMHOLESIZEGEN)

ENCOUNTERTYPES = {
	"Dead": {"Type": "Dead World", "Population": LowWorldPop, "Atmosphere": WorldAtmo, "DayLen": "DeadworldDayLen", "Year": "DeadworldYear", "Resources": "DeadWorldResources"}, 
	"Volcanic": {"Type": "Volcanic World", "Population": LowWorldPop, "Atmosphere": WorldAtmo, "DayLen": "VolcanicworldDayLen", "Year": "VolcanicWorldYear", "Resources": "VolcanicResources"}, 
	"Oceanic": {"Type": "Oceanic World", "Population": MedWorldPop, "Atmosphere": WorldAtmo, "DayLen": "OceanicDayLen", "Year": "OceanicworldYear"},
	"Jungle": {"Type": "Jungle World", "Population": MedWorldPop, "Atmosphere": LivingWorldAtmo, "DayLen": "JungleworldDayLen", "Year": "JungleworldYear", "Resources": "JungleResources"},
	"Asteroid Field": {"Type": "Asteroid Field", "Population": LowWorldPop, "Atmosphere": "AsteroidAtmo", "Resources": "AsteroidResources"},
	"Wormhole": {"Type": "WormHole", "Size": "WormholeSize", "Stability": "WormHoleStab"}, 
	"Space Station": {"Type": "Space Station", "Population": LowWorldPop, "Atmosphere": "StationAtmo", "DayLen": "StationDayLen", "Year": "StationYear"},
	"Ship": {"Type": "Ship", "Population": LowWorldPop, "Atmosphere": WorldAtmo, "Condition": "ShipCondition", "Disposition": "ShipDisposition"},
	"Gas Giant": {"Type": "Gas Giant", "Population": LowWorldPop, "Atmosphere": "GasAtmo", "DayLen": "GasDayLen", "Year": "GasYear", "Resources": "GasResources"},
	"Temperate World": {"Type": "Temperate World", "Population": MedWorldPop, "Atmosphere": LivingWorldAtmo, "DayLen": "TemperateDayLen", "Year": "TemperateYear", "Resources": "TemperateResources"},
	"Ice Planet": {"Type": "Ice World", "Population": LowWorldPop, "Atmosphere": WorldAtmo, "DayLen": "IceworldDayLen", "Year": "IceworldYear"},
	"Space Hulk": {"Type": "Space Hulk", "Population": LowWorldPop, "Atmosphere": WorldAtmo, "Hostiles": "SpaceHulkHostiles"}
},

encounter = ENCOUNTERTYPES[random.choice(ENCOUNTERTYPES.keys())]

print encounter