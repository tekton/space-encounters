import random
from random import randint

LowWorldPopGen = randint(0, 5000)

LowWorldPop = "{} life signs".format(LowWorldPopGen)

MedWorldPopGen = randint(5001, 500000)

MedWorldPop = "{} life signs".format(MedWorldPopGen)

HighWorldPopGen = randint(500000, 8000000000)

HighWorldPop = "{} life signs".format(HighWorldPopGen)

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
	"Small",
	"Medium",
	"Large",
	"Huge",
	"Gargantuan",
	"Collosal"
	)
WormholeSize = random.choice(WORMHOLESIZEGEN)

WormHoleStabGen = randint(01, 100)

WormHoleStab = "{} Hours".format(WormHoleStabGen)

DayHours = randint(8, 96) 

DayLen = "{} Hours".format(DayHours)

YearDays = randint(90, 1200)

YearLen = "{} Hours".format(YearDays)

CONGEN = (
	"Perfect",
	"Average",
	"Disrepair",
	"Derelict"
	)
Con = random.choice(CONGEN)

DISPOSITIONGEN = (
	"Helpful",
	"Friendly",
	"Neutral",
	"Unfriendly",
	"Hostile"
	)
Disposition = random.choice(DISPOSITIONGEN)

HOSTILEGEN = (
	"Orcs",
	"Goblins",
	"Pirates",
	"Demons",
	"Hive",
	"Cultists",
	"Soldiers",
	"Kobolds",
	"Gnolls",
	"Aliens",
	"none"
	)
Hostiles = random.choice(HOSTILEGEN)

ENCOUNTERTYPES = {
	"Dead": {"Type": "Dead World", "Population": LowWorldPop, "Atmosphere": WorldAtmo, "Day Length": DayLen, "Year": YearLen, "Hostiles": Hostiles}, 
	"Volcanic": {"Type": "Volcanic World", "Population": LowWorldPop, "Atmosphere": WorldAtmo, "Day Length": DayLen, "Year": YearLen, "Hostiles": Hostiles}, 
	"Oceanic": {"Type": "Oceanic World", "Population": MedWorldPop, "Atmosphere": WorldAtmo, "Day Length": DayLen, "Year": YearLen, "Hostiles": Hostiles},
	"Jungle": {"Type": "Jungle World", "Population": MedWorldPop, "Atmosphere": LivingWorldAtmo, "Day Length": DayLen, "Year": YearLen, "Hostiles": Hostiles},
	"Asteroid Field": {"Type": "Asteroid Field", "Population": LowWorldPop, "Atmosphere": WorldAtmo, "Hostiles": Hostiles},
	"Wormhole": {"Type": "WormHole", "Size": WormholeSize, "Stability": WormHoleStab, "Hostiles": Hostiles}, 
	"Space Station": {"Type": "Space Station", "Population": LowWorldPop, "Atmosphere": ShipAtmo, "Station Condition": Con, "Disposition": Disposition, "Hostiles": Hostiles},
	"Ship": {"Type": "Ship", "Population": LowWorldPop, "Atmosphere": WorldAtmo, "Condition": Con, "Disposition": Disposition, "Hostiles": Hostiles},
	"Gas Giant": {"Type": "Gas Giant", "Population": LowWorldPop, "Atmosphere": WorldAtmo, "Day Length": DayLen, "Year": YearLen, "Hostiles": Hostiles},
	"Temperate World": {"Type": "Temperate World", "Population": MedWorldPop, "Atmosphere": LivingWorldAtmo, "Day Length": DayLen, "Year": YearLen, "Hostiles": Hostiles},
	"Ice Planet": {"Type": "Ice World", "Population": LowWorldPop, "Atmosphere": WorldAtmo, "Day Length": DayLen, "Year": YearLen, "Hostiles": Hostiles},
	"Space Hulk": {"Type": "Space Hulk", "Population": LowWorldPop, "Atmosphere": WorldAtmo, "Hostiles": "SpaceHulkHostiles", "Hostiles": Hostiles}
}

encounter = ENCOUNTERTYPES[random.choice(ENCOUNTERTYPES.keys())]

def encountergen():
	print encounter

encountergen()