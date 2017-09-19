import random
import stargen

def encountergen():

	atmogen = (
	"Thin",
	"none",
	"Special"
	)
	living_world_atmogen = (
	"Thin",
	"Normal",
	"Special"
	)
	ship_atmo_gen = (
	"Thin",
	"Normal",
	"Special",
	"None"
	)
	wormhole_size_gen = (
	"Tiny",
	"Small",
	"Medium",
	"Large",
	"Huge",
	"Gargantuan",
	"Collosal"
	)
	low_world_pop_gen = random.randint(0, 5000)
	low_world_pop = "{} life signs".format(low_world_pop_gen)
	med_world_pop_gen = random.randint(5001, 500000)
	med_world_pop = "{} life signs".format(med_world_pop_gen)
	high_world_pop_gen = random.randint(500000, 8000000000)
	high_world_pop = "{} life signs".format(high_world_pop_gen)
	world_atmo = random.choice(ATMOGEN)
	living_world_atmo = random.choice(living_world_atmogen)
	ship_atmo = random.choice(ship_atmo_gen)
	worm_hole_size = random.choice(wormhole_size_gen)
	worm_hole_stab_gen = random.randint(01, 100)
	worm_hole_stab = "{} Hours".format(worm_hole_stab_gen)
	day_hours = random.randint(8, 96)
	day_len = "{} Hours".format(day_hours)
	year_days = random.randint(90, 1200)
	year_len = "{} Hours".format(year_days)

	disposition_gen = (
	"Helpful",
	"Friendly",
	"Neutral",
	"Unfriendly",
	"Hostile"
	)
	disposition = random.choice(disposition_gen)
	con_gen = (
	"Perfect",
	"Average",
	"Disrepair",
	"Derelict"
	)
	con = random.choice(con_gen)
	encounter_types = {
	"Dead": {"Type": "Dead World", "Population": low_world_pop, "Atmosphere": world_atmo, "Day Length": day_len, "Year": year_len}, 
	"Volcanic": {"Type": "Volcanic World", "Population": low_world_pop, "Atmosphere": world_atmo, "Day Length": day_len, "Year": year_len}, 
	"Oceanic": {"Type": "Oceanic World", "Population": med_world_pop, "Atmosphere": world_atmo, "Day Length": day_len, "Year": year_len},
	"Jungle": {"Type": "Jungle World", "Population": med_world_pop, "Atmosphere": Livingworld_atmo, "Day Length": day_len, "Year": year_len},
	"Asteroid Field": {"Type": "Asteroid Field", "Population": low_world_pop, "Atmosphere": world_atmo},
	"Wormhole": {"Type": "WormHole", "Size": WormholeSize, "Stability": WormHoleStab}, 
	"Space Station": {"Type": "Space Station", "Population": low_world_pop, "Atmosphere": ShipAtmo, "Station Condition": Con, "Disposition": Disposition},
	"Ship": {"Type": "Ship", "Population": low_world_pop, "Atmosphere": world_atmo, "Condition": Con, "Disposition": Disposition},
	"Gas Giant": {"Type": "Gas Giant", "Population": low_world_pop, "Atmosphere": world_atmo, "Day Length": day_len, "Year": year_len},
	"Temperate World": {"Type": "Temperate World", "Population": med_world_pop, "Atmosphere": Livingworld_atmo, "Day Length": day_len, "Year": year_len},
	"Ice Planet": {"Type": "Ice World", "Population": low_world_pop, "Atmosphere": world_atmo, "Day Length": day_len, "Year": year_len},
	"Space Hulk": {"Type": "Space Hulk", "Population": low_world_pop, "Atmosphere": world_atmo}
	}
	encounter = encounter_types[random.choice(encounter_types.keys())]
	print encounter