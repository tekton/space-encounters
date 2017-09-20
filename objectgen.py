import random

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
	world_atmo = random.choice(atmogen)
	living_world_atmo = random.choice(living_world_atmogen)
	ship_atmo = random.choice(ship_atmo_gen)
	worm_hole_size = random.choice(wormhole_size_gen)
	worm_hole_stab_gen = random.randint(1, 100)
	worm_hole_stab = "{} Percent".format(worm_hole_stab_gen)
	day_hours = random.randint(8, 96)
	day_len = "{} Hours".format(day_hours)
	year_days = random.randint(90, 1200)
	year_len = "{} Days".format(year_days)
	planet_size = random.randint(100000000, 100000000000)
	planet_diameter = "{} Kilometers".format(planet_size)

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
	"Dead": {"Type": "Dead World", "Population": low_world_pop, "Atmosphere": world_atmo, "Day Length": day_len, "Year": year_len, "Planet Diameter": planet_diameter}, 
	"Volcanic": {"Type": "Volcanic World", "Population": low_world_pop, "Atmosphere": world_atmo, "Day Length": day_len, "Year": year_len, "Planet Diameter": planet_diameter}, 
	"Oceanic": {"Type": "Oceanic World", "Population": med_world_pop, "Atmosphere": world_atmo, "Day Length": day_len, "Year": year_len, "Planet Diameter": planet_diameter},
	"Jungle": {"Type": "Jungle World", "Population": med_world_pop, "Atmosphere": living_world_atmo, "Day Length": day_len, "Year": year_len, "Planet Diameter": planet_diameter},
	"Asteroid Field": {"Type": "Asteroid Field", "Population": low_world_pop, "Atmosphere": world_atmo},
	"Wormhole": {"Type": "WormHole", "Size": worm_hole_size, "Stability": worm_hole_stab}, 
	"Space Station": {"Type": "Space Station", "Population": low_world_pop, "Atmosphere": ship_atmo, "Station Condition": con, "Disposition": disposition},
	"Ship": {"Type": "Ship", "Population": low_world_pop, "Atmosphere": world_atmo, "Condition": con, "Disposition": disposition},
	"Gas Giant": {"Type": "Gas Giant", "Population": low_world_pop, "Atmosphere": world_atmo, "Day Length": day_len, "Year": year_len, "Planet Diameter": planet_diameter},
	"Temperate World": {"Type": "Temperate World", "Population": high_world_pop, "Atmosphere": living_world_atmo, "Day Length": day_len, "Year": year_len, "Planet Diameter": planet_diameter},
	"Ice Planet": {"Type": "Ice World", "Population": low_world_pop, "Atmosphere": world_atmo, "Day Length": day_len, "Year": year_len, "Planet Diameter": planet_diameter},
	"Space Hulk": {"Type": "Space Hulk", "Population": low_world_pop, "Atmosphere": world_atmo}
	}
	encounter = encounter_types[random.choice(encounter_types.keys())]
	print encounter