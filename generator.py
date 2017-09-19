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
	"21MM-100MM",
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
	"Small",
	"Medium",
	"Large",
	"Huge",
	"Gargantuan",
	"Collosal"
	)
WormholeSize = random.choice(WORMHOLESIZEGEN)

WORMHOLESTABGEN = (
	"40%",
	"30%",
	"15%",
	"05%"
	)
WormHoleStab = random.choice(WORMHOLESTABGEN)

DAYLENGEN = (
	"8 Hours",
	"12 Hours",
	"18 Hours",
	"24 Hours",
	"30 Hours",
	"36 Hours",
	"42 Hours",
	"48 Hours"
	)
DayLen = random.choice(DAYLENGEN)

YEARLENGEN = (
	"30 Days",
	"60 Days",
	"90 Days",
	"120 Days",
	"180 Days",
	"270 Days",
	"360 Days",
	"520 Days",
	"760 Days"
	)
YearLen = random.choice(YEARLENGEN)

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
	"Pact World Wardens",
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

print encounter