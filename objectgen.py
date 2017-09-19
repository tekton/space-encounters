import random
import stargen


LowWorldPopGen = random.randint(0, 5000)

LowWorldPop = "{} life signs".format(LowWorldPopGen)

MedWorldPopGen = random.randint(5001, 500000)

MedWorldPop = "{} life signs".format(MedWorldPopGen)

HighWorldPopGen = random.randint(500000, 8000000000)

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

WormHoleStabGen = random.randint(01, 100)

WormHoleStab = "{} Hours".format(WormHoleStabGen)

DayHours = random.randint(8, 96) 

DayLen = "{} Hours".format(DayHours)

YearDays = random.randint(90, 1200)

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

ENCOUNTERTYPES = {
	"Dead": {"Type": "Dead World", "Population": LowWorldPop, "Atmosphere": WorldAtmo, "Day Length": DayLen, "Year": YearLen}, 
	"Volcanic": {"Type": "Volcanic World", "Population": LowWorldPop, "Atmosphere": WorldAtmo, "Day Length": DayLen, "Year": YearLen}, 
	"Oceanic": {"Type": "Oceanic World", "Population": MedWorldPop, "Atmosphere": WorldAtmo, "Day Length": DayLen, "Year": YearLen},
	"Jungle": {"Type": "Jungle World", "Population": MedWorldPop, "Atmosphere": LivingWorldAtmo, "Day Length": DayLen, "Year": YearLen},
	"Asteroid Field": {"Type": "Asteroid Field", "Population": LowWorldPop, "Atmosphere": WorldAtmo},
	"Wormhole": {"Type": "WormHole", "Size": WormholeSize, "Stability": WormHoleStab}, 
	"Space Station": {"Type": "Space Station", "Population": LowWorldPop, "Atmosphere": ShipAtmo, "Station Condition": Con, "Disposition": Disposition},
	"Ship": {"Type": "Ship", "Population": LowWorldPop, "Atmosphere": WorldAtmo, "Condition": Con, "Disposition": Disposition},
	"Gas Giant": {"Type": "Gas Giant", "Population": LowWorldPop, "Atmosphere": WorldAtmo, "Day Length": DayLen, "Year": YearLen},
	"Temperate World": {"Type": "Temperate World", "Population": MedWorldPop, "Atmosphere": LivingWorldAtmo, "Day Length": DayLen, "Year": YearLen},
	"Ice Planet": {"Type": "Ice World", "Population": LowWorldPop, "Atmosphere": WorldAtmo, "Day Length": DayLen, "Year": YearLen},
	"Space Hulk": {"Type": "Space Hulk", "Population": LowWorldPop, "Atmosphere": WorldAtmo}
}

encounter = ENCOUNTERTYPES[random.choice(ENCOUNTERTYPES.keys())]

def encountergen():
	print encounter

encountergen()