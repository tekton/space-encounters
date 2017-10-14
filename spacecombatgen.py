import argparse
import math
import sys
import random
from collections import OrderedDict
from pprint import pprint
from ship_data.shiptiers import shiptiers, point_hp_mod_list, hp_mod
from ship_data.difficultymod import difficultymod
from ship_data.shipsizes import shipsizes
from ship_data.shipmaneuver import shipmaneuverability, manuver_table
from ship_data.shipframes import shipframes
from ship_data.shippower import shippower


shipthrusters = {
	"T6 Thrusters": {
		"size": "tiny",
		"Speed": "6",
		"Pilot_Mod": 1,
		"PCU": 20,
		"cost": 3
	},
	"T8 Thrusters": {
		"size": "tiny",
		"Speed": "8",
		"Pilot_Mod": 0,
		"PCU": 25,
		"cost": 4
	},
	"T10 Thrusters": {
		"size": "tiny",
		"Speed": "10",
		"Pilot_Mod": 0,
		"PCU": 30,
		"cost": 5
	},
	"T12 Thrusters": {
		"size": "tiny",
		"Speed": "12",
		"Pilot_Mod": -1,
		"PCU": 35,
		"cost": 6
	},
	"T14 Thrusters": {
		"size": "tiny",
		"Speed": "14",
		"Pilot_Mod": -2,
		"PCU": 40,
		"cost": 7
	},
	"S6 Thrusters": {
		"size": "small",
		"Speed": "6",
		"Pilot_Mod": 1,
		"PCU": 30,
		"cost": 3
	},
	"S8 Thrusters": {
		"size": "small",
		"Speed": "8",
		"Pilot_Mod": 0,
		"PCU": 40,
		"cost": 4
	},
	"S10 Thrusters": {
		"size": "small",
		"Speed": "10",
		"Pilot_Mod": 0,
		"PCU": 50,
		"cost": 5
	},
	"S12 Thrusters": {
		"size": "small",
		"Speed": "12",
		"Pilot_Mod": -1,
		"PCU": 60,
		"cost": 6
	},
	"M4 Thrusters": {
		"size": "medium",
		"Speed": "4",
		"Pilot_Mod": 2,
		"PCU": 40,
		"cost": 2
	},
	"M6 Thrusters": {
		"size": "medium",
		"Speed": "6",
		"Pilot_Mod": 1,
		"PCU": 50,
		"cost": 3
	},
	"M8 Thrusters": {
		"size": "medium",
		"Speed": "8",
		"Pilot_Mod": 0,
		"PCU": 60,
		"cost": 4
	},
	"M10 Thrusters": {
		"size": "medium",
		"Speed": "10",
		"Pilot_Mod": 0,
		"PCU": 70,
		"cost": 5
	},
	"M12 Thrusters": {
		"size": "medium",
		"Speed": "12",
		"Pilot_Mod": -1,
		"PCU": 80,
		"cost": 6
	},
	"L4 Thrusters": {
		"size": "large",
		"Speed": "4",
		"Pilot_Mod": 2,
		"PCU": 60,
		"cost": 4
	},
	"L6 Thrusters": {
		"size": "large",
		"Speed": "6",
		"Pilot_Mod": 1,
		"PCU": 80,
		"cost": 6
	},
	"L8 Thrusters": {
		"size": "large",
		"Speed": "8",
		"Pilot_Mod": 0,
		"PCU": 100,
		"cost": 8
	},
	"L10 Thrusters": {
		"size": "large",
		"Speed": "10",
		"Pilot_Mod": 0,
		"PCU": 120,
		"cost": 10
	},
	"H4 Thrusters": {
		"size": "huge",
		"Speed": "4",
		"Pilot_Mod": 2,
		"PCU": 80,
		"cost": 4
	},
	"H6 Thrusters": {
		"size": "huge",
		"Speed": "6",
		"Pilot_Mod": 1,
		"PCU": 120,
		"cost": 6
	},
	"H8 Thrusters": {
		"size": "huge",
		"Speed": "8",
		"Pilot_Mod": 0,
		"PCU": 140,
		"cost": 8
	},
	"H10 Thrusters": {
		"size": "huge",
		"Speed": "10",
		"Pilot_Mod": 0,
		"PCU": 160,
		"cost": 10
	},
	"G4 Thrusters": {
		"size": "gargantuan",
		"Speed": "4",
		"Pilot_Mod": 2,
		"PCU": 120,
		"cost": 8
	},
	"G6 Thrusters": {
		"size": "gargantuan",
		"Speed": "6",
		"Pilot_Mod": 1,
		"PCU": 180,
		"cost": 12
	},
	"G8 Thrusters": {
		"size": "gargantuan",
		"Speed": "8",
		"Pilot_Mod": 0,
		"PCU": 240,
		"cost": 16
	},
	"C4 Thrusters": {
		"size": "colossal",
		"Speed": "4",
		"Pilot_Mod": 2,
		"PCU": 200,
		"cost": 8
	},
	"C6 Thrusters": {
		"size": "colossal",
		"Speed": "6",
		"Pilot_Mod": 1,
		"PCU": 300,
		"cost": 12
	},
	"C8 Thrusters": {
		"size": "colossal",
		"Speed": "8",
		"Pilot_Mod": 0,
		"PCU": 400,
		"cost": 16
	}
}

shiparmor = {
	"Mk 1 armor": {
		"AC": 1,
		"TL": 0,
		"turn": 0,
		"costmultiplier": 1
	},
	"Mk 2 armor": {
		"AC": 2,
		"TL": 0,
		"turn": 0,
		"costmultiplier": 2
	},
	"Mk 3 armor": {
		"AC": 3,
		"TL": 0,
		"turn": 0,
		"costmultiplier": 3
	},
	"Mk 4 armor": {
		"AC": 4,
		"TL": 0,
		"turn": 0,
		"costmultiplier": 5
	},
	"Mk 5 armor": {
		"AC": 5,
		"TL": 0,
		"turn": 0,
		"costmultiplier": 7
	},
	"Mk 6 armor": {
		"AC": 6,
		"TL": 1,
		"turn": 0,
		"costmultiplier": 9
	},
	"Mk 7 armor": {
		"AC": 7,
		"TL": 1,
		"turn": 0,
		"costmultiplier": 12
	},
	"Mk 8 armor": {
		"AC": 8,
		"TL": 1,
		"turn": 0,
		"costmultiplier": 15
	},
	"Mk 9 armor": {
		"AC": 9,
		"TL": 2,
		"turn": 1,
		"costmultiplier": 18
	},
	"Mk 10 armor": {
		"AC": 10,
		"TL": 2,
		"turn": 1,
		"costmultiplier": 21
	},
	"Mk 11 armor": {
		"AC": 11,
		"TL": 2,
		"turn": 1,
		"costmultiplier": 25
	},
	"Mk 12 armor": {
		"AC": 12,
		"TL": 3,
		"turn": 2,
		"costmultiplier": 30
	},
	"Mk 13 armor": {
		"AC": 13,
		"TL": 3,
		"turn": 2,
		"costmultiplier": 35
	},
	"Mk 14 armor": {
		"AC": 14,
		"TL": 3,
		"turn": 2,
		"costmultiplier": 40
	},
	"Mk 15 armor": {
		"AC": 15,
		"TL": 4,
		"turn": 3,
		"costmultiplier": 45
	},
}

shipcomputer = {
	"Basic Computer": {
		"Bonus": "0",
		"Nodes": "0",
		"PCU": 0,
		"cost": 0
	},
	"Mk 1 mononode": {
		"Bonus": "+1",
		"Nodes": "1",
		"PCU": 10,
		"cost": 1
	},
	"Mk 1 duonode": {
		"Bonus": "+1",
		"Nodes": "2",
		"PCU": 10,
		"cost": 2
	},
	"Mk 1 trionode": {
		"Bonus": "+1",
		"Nodes": "3",
		"PCU": 10,
		"cost": 3
	},
	"Mk 1 tetranode": {
		"Bonus": "+1",
		"Nodes": "4",
		"PCU": 10,
		"cost": 4
	},
	"Mk 2 mononode": {
		"Bonus": "+2",
		"Nodes": "1",
		"PCU": 15,
		"cost": 4
	},
	"Mk 2 duonode": {
		"Bonus": "+2",
		"Nodes": "2",
		"PCU": 15,
		"cost": 8
	},
	"Mk 2 trinode": {
		"Bonus": "+2",
		"Nodes": "3",
		"PCU": 15,
		"cost": 12
	},
	"Mk 2 tetranode": {
		"Bonus": "+2",
		"Nodes": "4",
		"PCU": 15,
		"cost": 16
	},
	"Mk 3 mononode": {
		"Bonus": "+3",
		"Nodes": "1",
		"PCU": 20,
		"cost": 9
	},
	"Mk 3 duonode": {
		"Bonus": "+3",
		"Nodes": "2",
		"PCU": 20,
		"cost": 18
	},
	"Mk 3 trinode": {
		"Bonus": "+3",
		"Nodes": "3",
		"PCU": 20,
		"cost": 27
	},
	"Mk 3 tetranode": {
		"Bonus": "+3",
		"Nodes": "4",
		"PCU": 20,
		"cost": 36
	},
	"Mk 4 mononode": {
		"Bonus": "+4",
		"Nodes": "1",
		"PCU": 25,
		"cost": 16
	},
	"Mk 4 duonode": {
		"Bonus": "+4",
		"Nodes": "2",
		"PCU": 25,
		"cost": 32
	},
	"Mk 4 trinode": {
		"Bonus": "+4",
		"Nodes": "3",
		"PCU": 25,
		"cost": 48
	},
	"Mk 5 mononode": {
		"Bonus": "+5",
		"Nodes": "1",
		"PCU": 30,
		"cost": 25
	},
	"Mk 5 duonode": {
		"Bonus": "+5",
		"Nodes": "2",
		"PCU": 30,
		"cost": 50
	},
	"Mk 5 trinode": {
		"Bonus": "+5",
		"Nodes": "3",
		"PCU": 30,
		"cost": 75
	},
	"Mk 6 mononode": {
		"Bonus": "+6",
		"Nodes": "1",
		"PCU": 35,
		"cost": 36
	},
	"Mk 6 duonode": {
		"Bonus": "+6",
		"Nodes": "2",
		"PCU": 35,
		"cost": 72
	},
	"Mk 7 mononode": {
		"Bonus": "+7",
		"Nodes": "1",
		"PCU": 40,
		"cost": 49
	},
	"Mk 7 mononode": {
		"Bonus": "+7",
		"Nodes": "2",
		"PCU": 40,
		"cost": 98
	},
	"Mk 8 mononode": {
		"Bonus": "+8",
		"Nodes": "1",
		"PCU": 45,
		"cost": 64
	},
	"Mk 8 mononode": {
		"Bonus": "+8",
		"Nodes": "2",
		"PCU": 45,
		"cost": 128
	},
	"Mk 9 mononode": {
		"Bonus": "+9",
		"Nodes": "1",
		"PCU": 50,
		"cost": 81
	},
	"Mk 9 mononode": {
		"Bonus": "+9",
		"Nodes": "2",
		"PCU": 50,
		"cost": 162
	},
	"Mk 10 mononode": {
		"Bonus": "+10",
		"Nodes": "1",
		"PCU": 55,
		"cost": 100
	},
	"Mk 10 mononode": {
		"Bonus": "+10",
		"Nodes": "2",
		"PCU": 55,
		"cost": 200}
}

shipcrewquarters = {
	"Common": {
		"cost": 0
	},
	"Good": {
		"cost": 2
	},
	"Luxurious": {
		"cost": 4}
}

shipdefensivecounter = {
	"Mk 1 Defenses": {
		"TL Bonus": 1,
		"PCU": 1,
		"cost": 2
	},
	"Mk 2 Defenses": {
		"TL Bonus": 2,
		"PCU": 1,
		"cost": 3
	},
	"Mk 3 Defenses": {
		"TL Bonus": 3,
		"PCU": 2,
		"cost": 4
	},
	"Mk 4 Defenses": {
		"TL Bonus": 4,
		"PCU": 3,
		"cost": 6
	},
	"Mk 5 Defenses": {
		"TL Bonus": 5,
		"PCU": 4,
		"cost": 8
	},
	"Mk 6 Defenses": {
		"TL Bonus": 6,
		"PCU": 5,
		"cost": 11
	},
	"Mk 7 Defenses": {
		"TL Bonus": 7,
		"PCU": 7,
		"cost": 14
	},
	"Mk 8 Defenses": {
		"TL Bonus": 8,
		"PCU": 9,
		"cost": 18
	},
	"Mk 9 Defenses": {
		"TL Bonus": 9,
		"PCU": 11,
		"cost": 22
	},
	"Mk 10 Defenses": {
		"TL Bonus": 10,
		"PCU": 13,
		"cost": 27
	},
	"Mk 11 Defenses": {
		"TL Bonus": 11,
		"PCU": 16,
		"cost": 33
	},
	"Mk 12 Defenses": {
		"TL Bonus": 12,
		"PCU": 20,
		"cost": 40
	},
	"Mk 13 Defenses": {
		"TL Bonus": 13,
		"PCU": 25,
		"cost": 50
	},
	"Mk 14 Defenses": {
		"TL Bonus": 14,
		"PCU": 32,
		"cost": 65
	},
	"Mk 15 Defenses": {
		"TL Bonus": 15,
		"PCU": 45,
		"cost": 90
	},
}

shipdriftengines = {
	"Signal Basic": {
		"Engine Rating": "1",
		"Min Engine PCU": 75,
		"Max Ship size": "-",
		"cost Multiplier": 2
	},
	"Signal Booster": {
		"Engine Rating": "2",
		"Min Engine PCU": 100,
		"Max Ship size": "Huge",
		"cost Multiplier": 5
	},
	"Signal Major": {
		"Engine Rating": "3",
		"Min Engine PCU": 150,
		"Max Ship size": "Large",
		"cost Multiplier": 10
	},
	"Signal Superior": {
		"Engine Rating": "4",
		"Min Engine PCU": 175,
		"Max Ship size": "Large",
		"cost Multiplier": 15
	},
	"Signal Ultra": {
		"Engine Rating": "5",
		"Min Engine PCU": 200,
		"Max Ship size": "Medium",
		"cost Multiplier": 20
	},
}

shipexpansionbays = {
	"Arcane laboratory": {
		"PCU": 1,
		"cost": 1,
		"bays": 1
	},
	"Cargo Hold": {
		"PCU": 0,
		"cost": 0,
		"bays": 1
	},
	"Escape pods": {
		"PCU": 2,
		"cost": 1,
		"bays": 1
	},
	"Guest Quarters": {
		"PCU": 1,
		"cost": 1,
		"bays": 1
	},
	"Hanger Bay": {
		"PCU": 30,
		"cost": 10,
		"bays": 4
	},
	"Life Boats": {
		"PCU": 5,
		"cost": 3
	},
	"Medical Bay": {
		"PCU": 4,
		"cost": 8,
		"bays": 1
	},
	"Passenger Seating": {
		"PCU": 0,
		"cost": 0,
		"bays": 1
	},
	"Power Core Housing": {
		"PCU": 0,
		"cost": 10,
		"bays": 1
	},
	"Gym": {
		"PCU": 0,
		"cost": 1,
		"bays": 1
	},
	"Trivid Den": {
		"PCU": 1,
		"cost": 1,
		"bays": 1
	},
	"Holosuite": {
		"PCU": 3,
		"cost": 1,
		"bays": 1
	},
	"Science Lab": {
		"PCU": 2,
		"cost": 1,
		"bays": 1
	},
	"Sealed Environment Chamber": {
		"PCU": 2,
		"cost": 1,
		"bays": 1
	},
	"Shuttle Bay": {
		"PCU": 10,
		"cost": 4,
		"bays": 2
	},
	"Smuggler Compartment": {
		"PCU": 4,
		"cost": 2,
		"bays": 1
	},
	"Synthesis bay": {
		"PCU": 2,
		"cost": 1,
		"bays": 1
	},
	"Tech Workshop": {
		"PCU": 3,
		"cost": 1,
		"bays": 1
	}
}

shipsecurity = {
	"Anti-hacking system": {
		"cost": 3
	},
	"Antipersonnel weapon - heavy": {
		"costmod": 5
	},
	"Antipersonnel weapon - longarm": {
		"costmod": 0
	},
	"Biometric Locks": {
		"cost": 5
	},
	"computer countermeasures": {
		"costmod": 0
	},
	"Self Destruct Sytem": {
		"costmultiplier": 5
	}
}

shipsensors = {
	"Cut Rate": {
		"range": "short",
		"mod": -2,
		"cost": 1
	},
	"Budget short-range": {
		"range": "short",
		"mod": 0,
		"cost": 2
	},
	"Basic short-range": {
		"range": "short",
		"mod": 2,
		"cost": 3
	},
	"Advanced short-range": {
		"range": "short",
		"mod": 4,
		"cost": 4
	},
	"Budget medium-range": {
		"range": "medium",
		"mod": 0,
		"cost": 3
	},
	"Basic medium-range": {
		"range": "medium",
		"mod": 2,
		"cost": 5
	},
	"Advanced medium-range": {
		"range": "medium",
		"mod": 4,
		"cost": 8
	},
	"Budget long-range": {
		"range": "long",
		"mod": 0,
		"cost": 6
	},
	"Basic long-range": {
		"range": "long",
		"mod": 2,
		"cost": 10
	},
	"Advanced long-range": {
		"range": "long",
		"mod": 4,
		"cost": 14
	},
}

shipshields = {
	"Basic Shields 1": {
		"Total SP": "10",
		"Regen rate": "1 per min",
		"PCU": 5,
		"cost": 2
	},
	"Basic Shields 2": {
		"Total SP": "20",
		"Regen rate": "1 per min",
		"PCU": 10,
		"cost": 3
	},
	"Basic Shields 3": {
		"Total SP": "30",
		"Regen rate": "1 per min",
		"PCU": 15,
		"cost": 4
	},
	"Basic Shields 4": {
		"Total SP": "40",
		"Regen rate": "1 per min",
		"PCU": 15,
		"cost": 5
	},
	"Light Shields 1": {
		"Total SP": "50",
		"Regen rate": "2 per min",
		"PCU": 20,
		"cost": 6
	},
	"Light Shields 2": {
		"Total SP": "60",
		"Regen rate": "2 per min",
		"PCU": 20,
		"cost": 8
	},
	"Light Shields 3": {
		"Total SP": "70",
		"Regen rate": "2 per min",
		"PCU": 25,
		"cost": 10
	},
	"Light Shields 4": {
		"Total SP": "80",
		"Regen rate": "2 per min",
		"PCU": 30,
		"cost": 12
	},
	"Medium Shields 1": {
		"Total SP": "90",
		"Regen rate": "4 per min",
		"PCU": 30,
		"cost": 13
	},
	"Medium Shields 2": {
		"Total SP": "100",
		"Regen rate": "4 per min",
		"PCU": 30,
		"cost": 15
	},
	"Medium Shields 3": {
		"Total SP": "120",
		"Regen rate": "4 per min",
		"PCU": 35,
		"cost": 17
	},
	"Medium Shields 4": {
		"Total SP": "140",
		"Regen rate": "8 per min",
		"PCU": 40,
		"cost": 18
	},
	"Medium Shields 5": {
		"Total SP": "160",
		"Regen rate": "8 per min",
		"PCU": 45,
		"cost": 20
	},
	"Medium Shields 6": {
		"Total SP": "200",
		"Regen rate": "8 per min",
		"PCU": 50,
		"cost": 22
	},
	"Heavy Shields 1": {
		"Total SP": "240",
		"Regen rate": "16 per min",
		"PCU": 55,
		"cost": 23
	},
	"Heavy Shields 2": {
		"Total SP": "280",
		"Regen rate": "16 per min",
		"PCU": 60,
		"cost": 25
	},
	"Heavy Shields 3": {
		"Total SP": "320",
		"Regen rate": "16 per min",
		"PCU": 70,
		"cost": 27
	},
	"Heavy Shields 4": {
		"Total SP": "360",
		"Regen rate": "32 per min",
		"PCU": 80,
		"cost": 28
	},
	"Heavy Shields 5": {
		"Total SP": "420",
		"Regen rate": "32 per min",
		"PCU": 90,
		"cost": 30
	},
	"Heavy Shields 6": {
		"Total SP": "480",
		"Regen rate": "32 per min",
		"PCU": 110,
		"cost": 32
	},
	"Superior Shields 1": {
		"Total SP": "540",
		"Regen rate": "64 per min",
		"PCU": 130,
		"cost": 35
	},
	"Superior Shields 2": {
		"Total SP": "600",
		"Regen rate": "64 per min",
		"PCU": 160,
		"cost": 40
	}
}

direct_ship_weapons = {
	"Chain cannon": {
		"type": "Light",
		"range": "Short",
		"damage": "6d4",
		"PCU": 15,
		"cost": 15,
		"special": "Ripper"
	},
	"Coilgun": {
		"type": "Light",
		"range": "Long",
		"damage": "4d4",
		"PCU": 10,
		"cost": 6,
		"special": "-"
	},
	"Flak Thrower": {
		"type": "Light",
		"range": "Short",
		"damage": "3d4",
		"PCU": 10,
		"cost": 5,
		"special": "Point +8"
	},
	"Gyrolaser": {
		"type": "Light",
		"range": "Short",
		"damage": "1d8",
		"PCU": 10,
		"cost": 5,
		"special": "Broad Arc"
	},
	"Laser Net": {
		"type": "Light",
		"range": "Short",
		"damage": "2d6",
		"PCU": 10,
		"cost": 9,
		"special": "Point +10"
	},
	"Light EMP Cannon": {
		"type": "Light",
		"range": "Short",
		"damage": "special",
		"PCU": 10,
		"cost": 8,
		"special": "EMP"
	},
	"Light Laser Cannon": {
		"type": "Light",
		"range": "Short",
		"damage": "2d4",
		"PCU": 5,
		"cost": 2,
		"special": "-"
	},
	"Light Particle Beam": {
		"type": "Light",
		"range": "Medium",
		"damage": "3d6",
		"PCU": 10,
		"cost": 10,
		"special": "-"
	},
	"Light Plasma Cannon": {
		"type": "Light",
		"range": "Short",
		"damage": "2d12",
		"PCU": 10,
		"cost": 12,
		"special": "-"
	},
	"Graser": {
		"type": "Heavy",
		"range": "Short",
		"damage": "7d10",
		"PCU": 40,
		"cost": 35,
		"special": "Irradiate(Medium)"
	},
	"Gravity Gun": {
		"type": "Heavy",
		"range": "Medium",
		"damage": "6d6",
		"PCU": 40,
		"cost": 30,
		"special": "Tractor Beam"
	},
	"Heavy EMP Cannon": {
		"type": "Heavy",
		"range": "Medium",
		"damage": "special",
		"PCU": 30,
		"cost": 24,
		"special": "EMP"
	},
	"Heavy Laser Array": {
		"type": "Heavy",
		"range": "Short",
		"damage": "6d4",
		"PCU": 15,
		"cost": 10,
		"special": "Array"
	},
	"Heavy Laser Cannon": {
		"type": "Heavy",
		"range": "Medium",
		"damage": "4d8",
		"PCU": 10,
		"cost": 8,
		"special": "-"
	},
	"Heavy Laser Net": {
		"type": "Heavy",
		"range": "Short",
		"damage": "5d6",
		"PCU": 15,
		"cost": 12,
		"special": "Point +12"
	},
	"Maser": {
		"type": "Heavy",
		"range": "Long",
		"damage": "6d10",
		"PCU": 35,
		"cost": 22,
		"special": "-"
	},
	"Particle Beam": {
		"type": "Heavy",
		"range": "Long",
		"damage": "8d6",
		"PCU": 25,
		"cost": 15,
		"special": "-"
	},
	"Persistent Particle Beam": {
		"type": "Heavy",
		"range": "Long",
		"damage": "10d6",
		"PCU": 40,
		"cost": 25,
		"special": "-"
	},
	"Plasma cannon": {
		"type": "Heavy",
		"range": "Medium",
		"damage": "5d12",
		"PCU": 30,
		"cost": 20,
		"special": "-"
	},
	"Railgun": {
		"type": "Heavy",
		"range": "Long",
		"damage": "8d4",
		"PCU": 20,
		"cost": 15,
		"special": "-"
	},
	"Twin Laser": {
		"type": "Heavy",
		"range": "Long",
		"damage": "5d8",
		"PCU": 15,
		"cost": 12,
		"special": "-"
	},
	"X-Laser cannon": {
		"type": "Heavy",
		"range": "Long",
		"damage": "8d6",
		"PCU": 40,
		"cost": 35,
		"special": "Line"
	},
	"Capital Gravity Cannon": {
		"type": "Capital",
		"range": "Long",
		"damage": "2d6 x 10",
		"PCU": 40,
		"cost": 50,
		"special": "Tractor Beam"
	},
	"Mass Driver": {
		"type": "Capital",
		"range": "Long",
		"damage": "2d6 x 10",
		"PCU": 25,
		"cost": 25,
		"special": "-"
	},
	"Particle Beam Cannon": {
		"type": "Capital",
		"range": "Long",
		"damage": "3d4 x 10",
		"PCU": 30,
		"cost": 30,
		"special": "-"
	},
	"Persistent Particle Beam Cannon": {
		"type": "Capital",
		"range": "Long",
		"damage": "2d10 x 10",
		"PCU": 50,
		"cost": 40,
		"special": "-"
	},
	"Super EMP cannon": {
		"type": "Capital",
		"range": "Long",
		"damage": "special",
		"PCU": 45,
		"cost": 45,
		"special": "EMP"
	},
	"Super Plasma Cannon": {
		"type": "Capital",
		"range": "Medium",
		"damage": "3d6 x 10",
		"PCU": 45,
		"cost": 35,
		"special": "-"
	},
	"Super X-laser Cannon": {
		"type": "Capital",
		"range": "Long",
		"damage": "3d4 x 10",
		"PCU": 50,
		"cost": 60,
		"special": "Line"
	},
	"Supergraser": {
		"type": "Capital",
		"range": "Medium",
		"damage": "2d8 x 10",
		"PCU": 50,
		"cost": 60,
		"special": "Irradiate(High)"
	},
	"Superlaser": {
		"type": "Capital",
		"range": "Long",
		"damage": "2d4 x 10",
		"PCU": 20,
		"cost": 20,
		"special": "-"
	},
	"Supermaser": {
		"type": "Capital",
		"range": "Long",
		"damage": "2d8 x 10",
		"PCU": 40,
		"cost": 35,
		"special": "-"
	},
	"Vortex Cannon": {
		"type": "Capital",
		"range": "Long",
		"damage": "2d12 x 10",
		"PCU": 55,
		"cost": 75,
		"special": "Vortex"
	},
}

tracking_ship_weapons = {
	"High explosive missile launcher": {
		"type": "Light",
		"range": "Long",
		"Speed": "12",
		"damage": "4d8",
		"PCU": 10,
		"cost": 4,
		"special": "Limited Fire 5"
	
	},
	"Light plasma torpedo launcher": {
		"type": "Light",
		"range": "Long",
		"Speed": "14",
		"damage": "3d8",
		"PCU": 5,
		"cost": 5,
		"special": "Limited Fire 5"
	},
	"Light torpedo launcher": {
		"type": "Light",
		"range": "Long",
		"Speed": "16",
		"damage": "2d8",
		"PCU": 5,
		"cost": 4,
		"special": "Limited Fire 5"
	},
	"Micromissile battery": {
		"type": "Light",
		"range": "Long",
		"Speed": "10",
		"damage": "2d6",
		"PCU": 10,
		"cost": 3,
		"special": "Array, Limited Fire 5"
	},
	"Tactical Nuclear Missile Launcher": {
		"type": "Light",
		"range": "Long",
		"Speed": "10",
		"damage": "5d8",
		"PCU": 10,
		"cost": 5,
		"special": "Irradiate(low), Limited Fire 5"
	},
	"Heavy Antimatter missile launcher": {
		"type": "Heavy",
		"range": "Long",
		"Speed": "8",
		"damage": "10d10",
		"PCU": 15,
		"cost": 12,
		"special": "Limited Fire 5"
	},
	"Heavy Nuclear missile launcher": {
		"type": "Heavy",
		"range": "Long",
		"Speed": "10",
		"damage": "10d8",
		"PCU": 15,
		"cost": 10,
		"special": "Irradiate(medium), Limited Fire 5"
	},
	"Heavy Plasma Torpedo launcher": {
		"type": "Heavy",
		"range": "Long",
		"Speed": "12",
		"damage": "5d10",
		"PCU": 10,
		"cost": 10,
		"special": "Limited Fire 5"
	},
	"Heavy Torpedo launcher": {
		"type": "Heavy",
		"range": "Long",
		"Speed": "14",
		"damage": "5d8",
		"PCU": 10,
		"cost": 8,
		"special": "Limited Fire 5"
	},
	"Antimatter Mega Missile Launcher": {
		"type": "Capital",
		"range": "Long",
		"Speed": "6",
		"damage": "4d10 X 10",
		"PCU": 15,
		"cost": 25,
		"special": "Limited Fire 5"
	},
	"Hellfire Torpedo Launcher": {
		"type": "Capital",
		"range": "Long",
		"Speed": "8",
		"damage": "2d10 X 10",
		"PCU": 10,
		"cost": 25,
		"special": "Limited Fire 5"
	},
	"Nuclear Mega Missile Launcher": {
		"type": "Capital",
		"range": "Long",
		"Speed": "8",
		"damage": "4d8 X 10",
		"PCU": 15,
		"cost": 20,
		"special": "Limited Fire 5"
	},
	"Quantum Missile Launcher": {
		"type": "Capital",
		"range": "Long",
		"Speed": "12",
		"damage": "2d8 X 10",
		"PCU": 15,
		"cost": 20,
		"special": "Limited Fire 5, Quantum"
	},
	"Solar Torpedo Launcher": {
		"type": "Capital",
		"range": "Long",
		"Speed": "10",
		"damage": "2d6 X 10",
		"PCU": 10,
		"cost": 20,
		"special": "Limited Fire 5"
	}
}


def get_ship_tier_list(_max=0):
	rtn_list = []
	for tier in shiptiers:
		if shiptiers[tier]["points"] <= _max:
			rtn_list.append(shiptiers[tier])
	return rtn_list


def get_ship_tier(bp):
	# get the actual "tier" of ship since points are semi static
	last_cost = 0
	for tier in point_hp_mod_list:
		if bp > last_cost and bp <= tier["points"]:
			return tier
		last_cost = tier["points"]


def get_ship_frame_list(max_bp=1000,
		min_bp=0,
				        min_crew=None,
		max_crew=None,
				        min_cargo=None,
		max_cargo=None):
	print(min_bp,
		max_bp)
	rtn_list = []
	for frame in shipframes:
		print(frame,
		shipframes[frame]["cost"])
		append = 0
		append_max = 1
		if shipframes[frame]["cost"] <= max_bp and shipframes[frame]["cost"] >= min_bp:
			append += 1
		if min_crew:
			print("min_crew",
		min_crew,
		shipframes[frame]["crew"]["min"])
			append_max += 1
			if int(min_crew) >= shipframes[frame]["crew"]["min"]:
				append += 1
		if max_crew:
			print("max_crew",
		max_crew,
		shipframes[frame]["crew"]["max"])
			append_max += 1
			if int(max_crew) <= shipframes[frame]["crew"]["max"]:
				append += 1
		# cargo checks...
		if min_cargo:
			if int(min_cargo) > 0:
				append_max += 1
				if "Expansion Bays" in shipframes[frame]:
					print(frame,
		"min_cargo",
		int(min_cargo),
		shipframes[frame]["Expansion Bays"])
					if shipframes[frame]["Expansion Bays"] > 0 and int(min_cargo) <= shipframes[frame]["Expansion Bays"]:
						append += 1
		if max_cargo:
			if int(max_cargo) > 0:
				append_max += 1
				if "Expansion Bays" in shipframes[frame]:
					print(frame,
		"max_cargo",
		int(max_cargo),
		shipframes[frame]["Expansion Bays"])
					if shipframes[frame]["Expansion Bays"] > 0 and int(max_cargo) <= shipframes[frame]["Expansion Bays"]:
						append += 1
		# /cargo_checks
		if append == append_max:
			rtn_list.append(frame)
	return rtn_list


def gen_npc_ships(**kwargs):
	dif_mod = float(kwargs.pop("difficulty",
		".75"))
	if "pc_bp" not in kwargs or kwargs["pc_bp"] is None:
		_bp = random.randint(25,
		1000)
	else:
		_bp = int(kwargs.pop("pc_bp"))
	_handicap = int(kwargs.pop("pc_handicap",
		"0"))
	print(_bp,
		dif_mod,
		_handicap)
	bp = int(_bp * dif_mod) - _handicap
	print(bp)
	if bp < 25:
		bp = 25
	bp = get_ship_tier(bp)
	hp_mod = bp["hp_multiplier"]
	bp = bp["points"]
	print(bp)
	get_frames_dict = {
		"min_bp": int(bp * .1),
		"max_bp": int(bp * .3)
	}
	# check other limiters...
	if "min_crew" in kwargs:
		get_frames_dict["min_crew"] = kwargs["min_crew"]
	if "max_crew" in kwargs:
		get_frames_dict["max_crew"] = kwargs["max_crew"]
	if "min_cargo" in kwargs:
		get_frames_dict["min_cargo"] = kwargs["min_cargo"]
	if "max_cargo" in kwargs:
		get_frames_dict["max_cargo"] = kwargs["max_cargo"]
	#
	frames = get_ship_frame_list(**get_frames_dict)
	if len(frames) == 0:
		print("Unable to find any frames with the limits imposed!")
		return
	print(frames)
	frame = random.choice(frames)
	print(frame)
	bp = bp - shipframes[frame]["cost"]
	print(bp)


if __name__ == "__main__":
	# argument parsing and you
	parser = argparse.ArgumentParser()
	# What are we trying to run?
	parser.add_argument('--pc',
		help="Create a ship for the players",
		action="store_true")
	parser.add_argument('--npc',
		help="Create an NPC ship for people to interact with",
		action="store_true")
	# What are the options?
	parser.add_argument('--pc-bp', help="Player character(s) build points")
	parser.add_argument('--pc-handicap', help="Player character(s) handicap for calculations")
	parser.add_argument('--difficulty', help="The difficulty modifier of the encounter")
	parser.add_argument('--max-ships', help="The maximum number of ships to create")
	# Limiters for ship type
	parser.add_argument('--min-cargo', help="The minimum number of cargo holds")
	parser.add_argument('--max-cargo', help="The maximum number of cargo holds")
	parser.add_argument('--min-crew', help="The minimum number of crew members")
	parser.add_argument('--max-crew', help="The maximum number of crew members")
	#
	parser.add_argument('--debug',
		help="Change logging level to debug",
		action="store_true")
	#
	args = parser.parse_args()
	#
	print(args)
	# print(dir(args))
	print(args.__dict__)
	if args.npc:
		_d = args.__dict__
		for j in _d.keys():
			if _d[j] is None:
				del(_d[j])
		print(args)
		if "max_ships" in _d:
			for x in range(_d["max_ships"]):
				gen_npc_ships(**_d)
		else:
			gen_npc_ships(**_d)
	