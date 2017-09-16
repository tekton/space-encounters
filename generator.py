import random

ENCOUNTERTYPES = {
	"Dead": {"Population": "DeadWorldPop", "Atmosphere": "DeadWorldAtmo", "DayLen": "DeadworldDayLen", "Year": "DeadworldYear"}, 
	"Volcanic": {"Population": "VolcanicWorldPop", "Atmosphere": "VolcanicWorldAtmo", "DayLen": "VolcanicworldDayLen", "Year": "VolcanicWorldYear"}, 
	"Oceanic": {"Population": "DeadWorldPop", "Atmosphere": "DeadWorldAtmo", "DayLen": "DeadworldDayLen", "Year": "DeadworldYear"},
	"Jungle": {"Population": "DeadWorldPop", "Atmosphere": "DeadWorldAtmo", "DayLen": "DeadworldDayLen", "Year": "DeadworldYear"},
	"Asteroid Field": {"Population": "DeadWorldPop", "Atmosphere": "DeadWorldAtmo", "DayLen": "DeadworldDayLen", "Year": "DeadworldYear"},
	"wormhole": {"Population": "DeadWorldPop", "Atmosphere": "DeadWorldAtmo", "DayLen": "DeadworldDayLen", "Year": "DeadworldYear"}, 
	"Space Station": {"Population": "DeadWorldPop", "Atmosphere": "DeadWorldAtmo", "DayLen": "DeadworldDayLen", "Year": "DeadworldYear"},
	"Ship": {"Population": "DeadWorldPop", "Atmosphere": "DeadWorldAtmo", "DayLen": "DeadworldDayLen", "Year": "DeadworldYear"},
	"Gas Giant": {"Population": "DeadWorldPop", "Atmosphere": "DeadWorldAtmo", "DayLen": "DeadworldDayLen", "Year": "DeadworldYear"},
	"Temperate World": {"Population": "DeadWorldPop", "Atmosphere": "DeadWorldAtmo", "DayLen": "DeadworldDayLen", "Year": "DeadworldYear"},
	"Ice Planet": {"Population": "DeadWorldPop", "Atmosphere": "DeadWorldAtmo", "DayLen": "DeadworldDayLen", "Year": "DeadworldYear"},
	 "Space Hulk": {"Population": "DeadWorldPop", "Atmosphere": "DeadWorldAtmo", "DayLen": "DeadworldDayLen", "Year": "DeadworldYear"}
}
encountertype = random.choice(ENCOUNTERTYPES)

print encountertype