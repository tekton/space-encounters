import random

LOW_WORLD_POP_GEN = random.randint(0, 5000)
LOW_WORLD_POP = "{} life signs".format(LOW_WORLD_POP_GEN)
MED_WORLD_POP_GEN = random.randint(5001, 500000)
MED_WORLD_POP = "{} life signs".format(MED_WORLD_POP_GEN)
HIGH_WORLD_POP_GEN = random.randint(500000, 8000000000)
HIGH_WORLD_POP = "{} life signs".format(HIGH_WORLD_POP_GEN)
WORLD_ATMO = random.choice(ATMOGEN)
LIVING_WORLD_ATMO = random.choice(LIVING_WORLD_ATMOGEN)
SHIP_ATMO = random.choice(SHIP_ATMO_GEN)
WORM_HOLE_SIZE = random.choice(WORMHOLE_SIZE_GEN)
WORM_HOLE_STAB_GEN = random.randint(1, 100)
WORM_HOLE_STAB = "{} Percent".format(WORM_HOLE_STAB_GEN)
DAY_HOURS = random.randint(8, 96)
DAY_LEN = "{} Hours".format(day_hours)
YEAR_DAYS = random.randint(90, 1200)
YEAR_LEN = "{} Days".format(YEAR_DAYS)
PLANET_SIZE = random.randint(100000000, 100000000000)
PLANET_DIAMETER = "{} Kilometers".format(PLANET_SIZE)

ATMOGEN = [
"Thin",
"none",
"Special"
]

LIVING_WORLD_ATMOGEN = [
"Thin",
"Normal",
"Special"
]

SHIP_ATMO_GEN = [
"Thin",
"Normal",
"Special",
"None"
]
WORMHOLE_SIZE_GEN = [
"Tiny",
"Small",
"Medium",
"Large",
"Huge",
"Gargantuan",
"Collosal"
]

DISPOSITION_GEN = [
"Helpful",
"Friendly",
"Neutral",
"Unfriendly",
"Hostile"
]
DISPOSITION = random.choice(DISPOSITION_GEN)

CON_GEN = [
"Perfect",
"Average",
"Disrepair",
"Derelict"
]
CON = random.choice(CON_GEN)

def encountergen():

	world_pop = [
	LOW_WORLD_POP,
	MED_WORLD_POP,
	HIGH_WORLD_POP
	]

	encounter_types = {
	"Dead": {"Type": "Dead World", "Population": world_pop, "Atmosphere": WORLD_ATMO, "Day Length": DAY_LEN, "Year": YEAR_LEN, "Planet Diameter": PLANET_DIAMETER}, 
	"Volcanic": {"Type": "Volcanic World", "Population": world_pop, "Atmosphere": WORLD_ATMO, "Day Length": DAY_LEN, "Year": YEAR_LEN, "Planet Diameter": PLANET_DIAMETER}, 
	"Oceanic": {"Type": "Oceanic World", "Population": world_pop, "Atmosphere": WORLD_ATMO, "Day Length": DAY_LEN, "Year": YEAR_LEN, "Planet Diameter": PLANET_DIAMETER},
	"Jungle": {"Type": "Jungle World", "Population": world_pop, "Atmosphere": LIVING_WORLD_ATMO, "Day Length": DAY_LEN, "Year": YEAR_LEN, "Planet Diameter": PLANET_DIAMETER},
	"Asteroid Field": {"Type": "Asteroid Field", "Population": world_pop, "Atmosphere": WORLD_ATMO},
	"Wormhole": {"Type": "WormHole", "Size": WORM_HOLE_SIZE, "Stability": WORM_HOLE_STAB}, 
	"Space Station": {"Type": "Space Station", "Population": world_pop, "Atmosphere": SHIP_ATMO, "Station Condition": CON, "Disposition": DISPOSITION},
	"Ship": {"Type": "Ship", "Population": world_pop, "Atmosphere": WORLD_ATMO, "Condition": CON, "Disposition": DISPOSITION},
	"Gas Giant": {"Type": "Gas Giant", "Population": world_pop, "Atmosphere": WORLD_ATMO, "Day Length": DAY_LEN, "Year": YEAR_LEN, "Planet Diameter": PLANET_DIAMETER},
	"Temperate World": {"Type": "Temperate World", "Population": world_pop, "Atmosphere": LIVING_WORLD_ATMO, "Day Length": DAY_LEN, "Year": YEAR_LEN, "Planet Diameter": PLANET_DIAMETER},
	"Ice Planet": {"Type": "Ice World", "Population": world_pop, "Atmosphere": WORLD_ATMO, "Day Length": DAY_LEN, "Year": YEAR_LEN, "Planet Diameter": PLANET_DIAMETER},
	"Space Hulk": {"Type": "Space Hulk", "Population": world_pop, "Atmosphere": WORLD_ATMO}
	}
	encounter = encounter_types[random.choice(encounter_types.keys())]
	print encounter