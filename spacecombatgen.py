import math
import sys
import random


shiptiers = {
	"1/4": {"Build_points": 25, "HP_Increase": 0},
	"1/3": {"Build_points": 30, "HP_Increase": 0},
	"1/2": {"Build_points": 40, "HP_Increase": 0},
	"1": {"Build_points": 55, "HP_Increase": 0},
	"2": {"Build_points": 75 "HP_Increase": 0},
	"3": {"Build_points": 95, "HP_Increase": 0},
	"4": {"Build_points": 115, "HP_Increase": 1},
	"5": {"Build_points": 135, "HP_Increase": 1},
	"6": {"Build_points": 155, "HP_Increase": 1},
	"7": {"Build_points": 180, "HP_Increase": 1},
	"8": {"Build_points": 205, "HP_Increase": 2},
	"9": {"Build_points": 230, "HP_Increase": 2},
	"10": {"Build_points": 270, "HP_Increase": 2},
	"11": {"Build_points": 310, "HP_Increase": 2},
	"12": {"Build_points": 350, "HP_Increase": 3},
	"13": {"Build_points": 400, "HP_Increase": 3},
	"14": {"Build_points": 450, "HP_Increase": 3},
	"15": {"Build_points": 500, "HP_Increase": 3},
	"16": {"Build_points": 600, "HP_Increase": 4},
	"17": {"Build_points": 700, "HP_Increase": 4},
	"18": {"Build_points": 800, "HP_Increase": 4},
	"19": {"Build_points": 900, "HP_Increase": 4},
	"20": {"Build_points": 1000, "HP_Increase": 5}
}

shipsizes = {
	"tiny": {"category": 1, "Length": random.ranint(20, 60), "Weight": random.randint(3, 20), "AC and TL mod": 2},
	"small": {"category": 2, "Length": random.ranint(60, 120), "Weight": random.randint(20, 40), "AC and TL mod": 1},
	"medium": {"category": 3, "Length": random.ranint(120, 300), "Weight": random.randint(40, 150), "AC and TL mod": 0},
	"large": {"category": 4, "Length": random.ranint(300, 800), "Weight": random.randint(150, 420), "AC and TL mod": -1},
	"huge": {"category": 5, "Length": random.ranint(800, 2000), "Weight": random.randint(420, 1200), "AC and TL mod": -2},
	"gargantuan": {"category": 6, "Length": random.ranint(2000, 15000), "Weight": random.randint(1200, 8000), "AC and TL mod": -4},
	"colossal": {"category": 7, "Length": random.ranint(15000, 45000), "Weight": random.randint(8000, 20000), "AC and TL mod": -8}
}

shipmaneuverability = {
	"Perfect": {"pilotingmod": 2, "turn": 0},
	"Good": {"pilotingmod": 1, "turn": 1},
	"Average": {"pilotingmod": 0, "turn": 2},
	"Poor": {"pilotingmod": -1, "turn": 3},
	"Clumsy": {"pilotingmod": -2, "turn": 4}
}

shipframes = {
	"Racer": {"Cost": 4, "Size": "tiny", "Maneuverability": "Prefect", "HP": 20, "HP increment": 5, "DT": "-", "CT": "4", "Forward": {"light": 1}, "Port": 0, "Starboard": 0, "Aft": {"light": 1}, "turret": 0, "Expansion Bays": 0, "Minimum Crew": "1", "Max Crew": "1"},
	"Interceptor": {"Cost": 6, "Size": "tiny", "Maneuverability": "Prefect", "HP": 30, "HP increment": 5, "DT": "-", "CT": "6", "Forward": {"light": 2}, "Port": 0, "Starboard": 0, "Aft": 0, "turret": 0, "Expansion Bays": 0, "Minimum Crew": "1", "Max Crew": "1"},
	"Fighter": {"Cost": 8, "Size": "tiny", "Maneuverability": "Good", "HP": 35, "HP increment": 5, "DT": "-", "CT": "7", "Forward": {"light": 2}, "Port": 0, "Starboard": 0, "Aft": {"light": 1}, "turret": 0, "Expansion Bays": 0, "Minimum Crew": "1", "Max Crew": "2"},
	"Shuttle": {"Cost": 6, "Size": "small", "Maneuverability": "Perfect", "HP": 35, "HP increment": 5, "DT": "-", "CT": "7", "Forward": {"light": 1}, "Port": 0, "Starboard": 0, "Aft": 0, "turret": 0, "Expansion Bays": 3, "Minimum Crew": "1", "Max Crew": "4"},
	"Light Freighter": {"Cost": 10, "Size": "small", "Maneuverability": "Good", "HP": 40, "HP increment": 10, "DT": "-", "CT": "8", "Forward": {"light": 2}, "Port": {"light": 1}, "Starboard": {"light": 1}, "Aft": 0, "turret": 0, "Expansion Bays": 3, "Minimum Crew": "1", "Max Crew": "6"},
	"Explorer": {"Cost": 12, "Size": "medium", "Maneuverability": "Good", "HP": 55, "HP increment": 10, "DT": "-", "CT": "11", "Forward": {"light": 1}, "Port": {"light": 1}, "Starboard": {"light": 1}, "Aft": 0, "turret": {"light": 1}, "Expansion Bays": 4, "Minimum Crew": "1", "Max Crew": "6"},
	"Transport": {"Cost": 15, "Size": "medium", "Maneuverability": "Average", "HP": 70, "HP increment": 15, "DT": "-", "CT": "14", "Forward": {"light": 1, "heavy": 1}, "Port": 0, "Starboard": 0, "Aft": {"light": 1}, "turret": {"light": 2}, "Expansion Bays": 5, "Minimum Crew": "1", "Max Crew": "6"},
	"Destroyer": {"Cost": 30, "Size": "large", "Maneuverability": "Average", "HP": 150, "HP increment": 20, "DT": "-", "CT": "30", "Forward": {"heavy": 2}, "Port": {"light": 1}, "Starboard": {"light": 1}, "Aft": {"light": 1}, "turret": {"light": 1}, "Expansion Bays": 4, "Minimum Crew": "6", "Max Crew": "20"},
	"Heavy Freighter": {"Cost": 40, "Size": "large", "Maneuverability": "Average", "HP": 120, "HP increment": 20, "DT": "-", "CT": "24", "Forward": {"light": 1, "heavy": 1}, "Port": {"heavy": 1}, "Starboard": {"heavy": 1}, "Aft": 0, "turret": 0, "Expansion Bays": 8, "Minimum Crew": "6", "Max Crew": "20"},
	"Bulk Freighter": {"Cost": 55, "Size": "huge", "Maneuverability": "Poor", "HP": 160, "HP increment": 20, "DT": "5", "CT": "32", "Forward": {"heavy": 1}, "Port": 0, "Starboard": 0, "Aft": {"heavy": 1}, "turret": {"light": 2}, "Expansion Bays": 10, "Minimum Crew": "20", "Max Crew": "50"},
	"Cruiser": {"Cost": 60, "Size": "huge", "Maneuverability": "Average", "HP": 180, "HP increment": 25, "DT": "5", "CT": "36", "Forward": {"capital": 1}, "Port": {"light": 1}, "Starboard": {"light": 1}, "Aft": 0, "turret": {"heavy": 1}, "Expansion Bays": 6, "Minimum Crew": "20", "Max Crew": "100"},
	"Carrier": {"Cost": 120, "Size": "gargantuan", "Maneuverability": "Poor", "HP": 240, "HP increment": 30, "DT": "10", "CT": "48", "Forward": {"capital": 1}, "Port": {"heavy": 3}, "Starboard": {"heavy": 3}, "Aft": 0, "turret": {"light": 2}, "Expansion Bays": 10, "Minimum Crew": "75", "Max Crew": "200"},
	"Battleship": {"Cost": 150, "Size": "gargantuan", "Maneuverability": "Average", "HP": 280, "HP increment": 40, "DT": "10", "CT": "56", "Forward": {"capital": 1, "heavy": 2}, "Port": {"light": 1, "heavy": 2}, "Starboard": {"light": 1, "heavy": 2}, "Aft": {"light": 1}, "turret": {"heavy": 2}, "Expansion Bays": 8, "Minimum Crew": "100", "Max Crew": "300"},
	"Dreadnought": {"Cost": 200, "Size": "gargantuan", "Maneuverability": "Clumsy", "HP": 400, "HP increment": 50, "DT": "15", "CT": "80", "Forward": {"capital": 2, "heavy": 2}, "Port": {"heavy": 3, "capital": 1}, "Starboard": {"heavy": 3, "capital": 1}, "Aft": 0, "turret": {"light": 4}, "Expansion Bays": 20, "Minimum Crew": "125", "Max Crew": "500"}
}

shippower = {
	"Micron Light": {"size": "tiny", "PCU": 50, "cost": 4},
	"Micron Heavy": {"size": "tiny", "PCU": 70, "cost": 6},
	"Micron Ultra": {"size": "tiny", "PCU": 80, "cost": 8},
	"Arcus Light": {"size": ["tiny", "small"], "PCU": 70, "cost": 7},
	"Pulse Brown": {"size": ["tiny", "small"], "PCU": 90, "cost": 9},
	"Pulse Black": {"size": ["tiny", "small"], "PCU": 120, "cost": 12},
	"Pulse White": {"size": ["tiny", "small"], "PCU": 140, "cost": 14},
	"Pulse Gray": {"size": ["tiny", "small", "medium"], "PCU": 100, "cost": 10},
	"Arcus Heavy": {"size": ["tiny", "small", "medium"], "PCU": 130, "cost": 13},
	"Pulse Green": {"size": ["tiny", "small", "medium"], "PCU": 150, "cost": 15},
	"Pulse Red": {"size": ["tiny", "small", "medium"], "PCU": 175, "cost": 17},
	"Pulse Blue": {"size": ["tiny", "small", "medium"], "PCU": 200, "cost": 20},
	"Arcus Ultra": {"size": ["small", "medium", "large"], "PCU": 150, "cost": 15},
	"Arcus Maximum": {"size": ["small", "medium", "large"], "PCU": 200, "cost": 20},
	"Pulse Orange": {"size": ["small", "medium", "large"], "PCU": 250, "cost": 25},
	"Pulse Prismatic": {"size": ["small", "medium", "large"], "PCU": 300, "cost": 30},
	"Nova Light": {"size": ["medium", "large", "huge"], "PCU": 150, "cost": 15},
	"Nova Heavy": {"size": ["medium", "large", "huge"], "PCU": 200, "cost": 20},
	"Nova Ultra": {"size": ["medium", "large", "huge"], "PCU": 300, "cost": 30},
	"Gateway Light": {"size": ["large", "huge", "gargantuan"], "PCU": 300, "cost": 30},
	"Gateway Heavy": {"size": ["large", "huge", "gargantuan"], "PCU": 400, "cost": 40},
	"Gateway Ultra": {"size": ["huge", "gargantuan", "colossal"], "PCU": 500, "cost": 50}
}

shipthrusters = {
	"T6 Thrusters": {"Size": "tiny", "Speed": "6", "Pilot_Mod": 1, "PCU": 20, "Cost": 3},
	"T8 Thrusters": {"Size": "tiny", "Speed": "8", "Pilot_Mod": 0, "PCU": 25, "Cost": 4},
	"T10 Thrusters": {"Size": "tiny", "Speed": "10", "Pilot_Mod": 0, "PCU": 30, "Cost": 5},
	"T12 Thrusters": {"Size": "tiny", "Speed": "12", "Pilot_Mod": -1, "PCU": 35, "Cost": 6},
	"T14 Thrusters": {"Size": "tiny", "Speed": "14", "Pilot_Mod": -2, "PCU": 40, "Cost": 7},
	"S6 Thrusters": {"Size": "small", "Speed": "6", "Pilot_Mod": 1, "PCU": 30, "Cost": 3},
	"S8 Thrusters": {"Size": "small", "Speed": "8", "Pilot_Mod": 0, "PCU": 40, "Cost": 4},
	"S10 Thrusters": {"Size": "small", "Speed": "10", "Pilot_Mod": 0, "PCU": 50, "Cost": 5},
	"S12 Thrusters": {"Size": "small", "Speed": "12", "Pilot_Mod": -1, "PCU": 60, "Cost": 6},
	"M4 Thrusters": {"Size": "medium", "Speed": "4", "Pilot_Mod": 2, "PCU": 40, "Cost": 2},
	"M6 Thrusters": {"Size": "medium", "Speed": "6", "Pilot_Mod": 1, "PCU": 50, "Cost": 3},
	"M8 Thrusters": {"Size": "medium", "Speed": "8", "Pilot_Mod": 0, "PCU": 60, "Cost": 4},
	"M10 Thrusters": {"Size": "medium", "Speed": "10", "Pilot_Mod": 0, "PCU": 70, "Cost": 5},
	"M12 Thrusters": {"Size": "medium", "Speed": "12", "Pilot_Mod": -1, "PCU": 80, "Cost": 6},
	"L4 Thrusters": {"Size": "large", "Speed": "4", "Pilot_Mod": 2, "PCU": 60, "Cost": 4},
	"L6 Thrusters": {"Size": "large", "Speed": "6", "Pilot_Mod": 1, "PCU": 80, "Cost": 6},
	"L8 Thrusters": {"Size": "large", "Speed": "8", "Pilot_Mod": 0, "PCU": 100, "Cost": 8},
	"L10 Thrusters": {"Size": "large", "Speed": "10", "Pilot_Mod": 0, "PCU": 120, "Cost": 10},
	"H4 Thrusters": {"Size": "huge", "Speed": "4", "Pilot_Mod": 2, "PCU": 80, "Cost": 4},
	"H6 Thrusters": {"Size": "huge", "Speed": "6", "Pilot_Mod": 1, "PCU": 120, "Cost": 6},
	"H8 Thrusters": {"Size": "huge", "Speed": "8", "Pilot_Mod": 0, "PCU": 140, "Cost": 8},
	"H10 Thrusters": {"Size": "huge", "Speed": "10", "Pilot_Mod": 0, "PCU": 160, "Cost": 10},
	"G4 Thrusters": {"Size": "gargantuan", "Speed": "4", "Pilot_Mod": 2, "PCU": 120, "Cost": 8},
	"G6 Thrusters": {"Size": "gargantuan", "Speed": "6", "Pilot_Mod": 1, "PCU": 180, "Cost": 12},
	"G8 Thrusters": {"Size": "gargantuan", "Speed": "8", "Pilot_Mod": 0, "PCU": 240, "Cost": 16},
	"C4 Thrusters": {"Size": "colossal", "Speed": "4", "Pilot_Mod": 2, "PCU": 200, "Cost": 8},
	"C6 Thrusters": {"Size": "colossal", "Speed": "6", "Pilot_Mod": 1, "PCU": 300, "Cost": 12},
	"C8 Thrusters": {"Size": "colossal", "Speed": "8", "Pilot_Mod": 0, "PCU": 400, "Cost": 16}
}

shiparmor = {
	"Mk 1 armor": {"AC bonus": 1, "TL Mod": 0, "Turn Mod": 0, "costmultiplier": 1},
	"Mk 2 armor": {"AC bonus": 2, "TL Mod": 0, "Turn Mod": 0, "costmultiplier": 2},
	"Mk 3 armor": {"AC bonus": 3, "TL Mod": 0, "Turn Mod": 0, "costmultiplier": 3},
	"Mk 4 armor": {"AC bonus": 4, "TL Mod": 0, "Turn Mod": 0, "costmultiplier": 5},
	"Mk 5 armor": {"AC bonus": 5, "TL Mod": 0, "Turn Mod": 0, "costmultiplier": 7},
	"Mk 6 armor": {"AC bonus": 6, "TL Mod": 1, "Turn Mod": 0, "costmultiplier": 9},
	"Mk 7 armor": {"AC bonus": 7, "TL Mod": 1, "Turn Mod": 0, "costmultiplier": 12},
	"Mk 8 armor": {"AC bonus": 8, "TL Mod": 1, "Turn Mod": 0, "costmultiplier": 15},
	"Mk 9 armor": {"AC bonus": 9, "TL Mod": 2, "Turn Mod": 1, "costmultiplier": 18},
	"Mk 10 armor": {"AC bonus": 10, "TL Mod": 2, "Turn Mod": 1, "costmultiplier": 21},
	"Mk 11 armor": {"AC bonus": 11, "TL Mod": 2, "Turn Mod": 1, "costmultiplier": 25},
	"Mk 12 armor": {"AC bonus": 12, "TL Mod": 3, "Turn Mod": 2, "costmultiplier": 30},
	"Mk 13 armor": {"AC bonus": 13, "TL Mod": 3, "Turn Mod": 2, "costmultiplier": 35},
	"Mk 14 armor": {"AC bonus": 14, "TL Mod": 3, "Turn Mod": 2, "costmultiplier": 40},
	"Mk 15 armor": {"AC bonus": 15, "TL Mod": 4, "Turn Mod": 3, "costmultiplier": 45},
}

shipcomputer = {
	"Basic Computer": {"Bonus": "0", "Nodes": "0", "PCU": 0, "Cost": 0},
	"Mk 1 mononode": {"Bonus": "+1", "Nodes": "1", "PCU": 10, "Cost": 1},
	"Mk 1 duonode": {"Bonus": "+1", "Nodes": "2", "PCU": 10, "Cost": 2},
	"Mk 1 trionode": {"Bonus": "+1", "Nodes": "3", "PCU": 10, "Cost": 3},
	"Mk 1 tetranode": {"Bonus": "+1", "Nodes": "4", "PCU": 10, "Cost": 4},
	"Mk 2 mononode": {"Bonus": "+2", "Nodes": "1", "PCU": 15, "Cost": 4},
	"Mk 2 duonode": {"Bonus": "+2", "Nodes": "2", "PCU": 15, "Cost": 8},
	"Mk 2 trinode": {"Bonus": "+2", "Nodes": "3", "PCU": 15, "Cost": 12},
	"Mk 2 tetranode": {"Bonus": "+2", "Nodes": "4", "PCU": 15, "Cost": 16},
	"Mk 3 mononode": {"Bonus": "+3", "Nodes": "1", "PCU": 20, "Cost": 9},
	"Mk 3 duonode": {"Bonus": "+3", "Nodes": "2", "PCU": 20, "Cost": 18},
	"Mk 3 trinode": {"Bonus": "+3", "Nodes": "3", "PCU": 20, "Cost": 27},
	"Mk 3 tetranode": {"Bonus": "+3", "Nodes": "4", "PCU": 20, "Cost": 36},
	"Mk 4 mononode": {"Bonus": "+4", "Nodes": "1", "PCU": 25, "Cost": 16},
	"Mk 4 duonode": {"Bonus": "+4", "Nodes": "2", "PCU": 25, "Cost": 32},
	"Mk 4 trinode": {"Bonus": "+4", "Nodes": "3", "PCU": 25, "Cost": 48},
	"Mk 5 mononode": {"Bonus": "+5", "Nodes": "1", "PCU": 30, "Cost": 25},
	"Mk 5 duonode": {"Bonus": "+5", "Nodes": "2", "PCU": 30, "Cost": 50},
	"Mk 5 trinode": {"Bonus": "+5", "Nodes": "3", "PCU": 30, "Cost": 75},
	"Mk 6 mononode": {"Bonus": "+6", "Nodes": "1", "PCU": 35, "Cost": 36},
	"Mk 6 duonode": {"Bonus": "+6", "Nodes": "2", "PCU": 35, "Cost": 72},
	"Mk 7 mononode": {"Bonus": "+7", "Nodes": "1", "PCU": 40, "Cost": 49},
	"Mk 7 mononode": {"Bonus": "+7", "Nodes": "2", "PCU": 40, "Cost": 98},
	"Mk 8 mononode": {"Bonus": "+8", "Nodes": "1", "PCU": 45, "Cost": 64},
	"Mk 8 mononode": {"Bonus": "+8", "Nodes": "2", "PCU": 45, "Cost": 128},
	"Mk 9 mononode": {"Bonus": "+9", "Nodes": "1", "PCU": 50, "Cost": 81},
	"Mk 9 mononode": {"Bonus": "+9", "Nodes": "2", "PCU": 50, "Cost": 162},
	"Mk 10 mononode": {"Bonus": "+10", "Nodes": "1", "PCU": 55, "Cost": 100},
	"Mk 10 mononode": {"Bonus": "+10", "Nodes": "2", "PCU": 55, "Cost": 200}
}

shipcrewquarters = {
	"Common": {"Cost": 0},
	"Good": {"Cost": 2},
	"Luxurious": {"Cost": 4}
}

shipdefensivecounter = {
	"Mk 1 Defenses" {"TL Bonus": 1, "PCU": 1, "Cost": 2},
	"Mk 2 Defenses" {"TL Bonus": 2, "PCU": 1, "Cost": 3},
	"Mk 3 Defenses" {"TL Bonus": 3, "PCU": 2, "Cost": 4},
	"Mk 4 Defenses" {"TL Bonus": 4, "PCU": 3, "Cost": 6},
	"Mk 5 Defenses" {"TL Bonus": 5, "PCU": 4, "Cost": 8},
	"Mk 6 Defenses" {"TL Bonus": 6, "PCU": 5, "Cost": 11},
	"Mk 7 Defenses" {"TL Bonus": 7, "PCU": 7, "Cost": 14},
	"Mk 8 Defenses" {"TL Bonus": 8, "PCU": 9, "Cost": 18},
	"Mk 9 Defenses" {"TL Bonus": 9, "PCU": 11, "Cost": 22},
	"Mk 10 Defenses" {"TL Bonus": 10, "PCU": 13, "Cost": 27},
	"Mk 11 Defenses" {"TL Bonus": 11, "PCU": 16, "Cost": 33},
	"Mk 12 Defenses" {"TL Bonus": 12, "PCU": 20, "Cost": 40},
	"Mk 13 Defenses" {"TL Bonus": 13, "PCU": 25, "Cost": 50},
	"Mk 14 Defenses" {"TL Bonus": 14, "PCU": 32, "Cost": 65,
	"Mk 15 Defenses" {"TL Bonus": 15, "PCU": 45, "Cost": 90},
}

shipdriftengines = {
	"Signal Basic": {"Engine Rating": "1", "Min Engine PCU": 75, "Max Ship Size": "-", "Cost Multiplier": 2},
	"Signal Booster": {"Engine Rating": "2", "Min Engine PCU": 100, "Max Ship Size": "Huge", "Cost Multiplier": 5},
	"Signal Major": {"Engine Rating": "3", "Min Engine PCU": 150, "Max Ship Size": "Large", "Cost Multiplier": 10},
	"Signal Superior": {"Engine Rating": "4", "Min Engine PCU": 175, "Max Ship Size": "Large", "Cost Multiplier": 15},
	"Signal Ultra": {"Engine Rating": "5", "Min Engine PCU": 200, "Max Ship Size": "Medium", "Cost Multiplier": 20},
}

shipexpansionbays = {
	"Arcane laboratory": {"PCU": 1, "Cost": 1, "bays": 1},
	"Cargo Hold": {"PCU": 0, "Cost": 0, "bays": 1},
	"Escape pods": {"PCU": 2, "Cost": 1, "bays": 1},
	"Guest Quarters": {"PCU": 1, "Cost": 1, "bays": 1},
	"Hanger Bay": {"PCU": 30, "Cost": 10, "bays": 4},
	"Life Boats": {"PCU": 5, "Cost": 3},
	"Medical Bay": {"PCU": 4, "Cost": 8, "bays": 1},
	"Passenger Seating": {"PCU": 0, "Cost": 0, "bays": 1},
	"Power Core Housing": {"PCU": 0, "Cost": 10, "bays": 1},
	"Gym": {"PCU": 0, "Cost": 1, "bays": 1},
	"Trivid Den": {"PCU": 1, "Cost": 1, "bays": 1},
	"Holosuite": {"PCU": 3, "Cost": 1, "bays": 1},
	"Science Lab": {"PCU": 2, "Cost": 1, "bays": 1},
	"Sealed Environment Chamber": {"PCU": 2, "Cost": 1, "bays": 1},
	"Shuttle Bay": {"PCU": 10, "Cost": 4, "bays": 2},
	"Smuggler Compartment": {"PCU": 4, "Cost": 2, "bays": 1},
	"Synthesis bay": {"PCU": 2, "Cost": 1, "bays": 1},
	"Tech Workshop": {"PCU": 3, "Cost": 1, "bays": 1}
	}

shipsecurity = {
	"Anti-hacking system": {"Cost": 3},
	"Antipersonnel weapon - heavy": {"costmod": 5},
	"Antipersonnel weapon - longarm": {"costmod": 0},
	"Biometric Locks": {"Cost": 5},
	"computer countermeasures": {"costmod": 0},
	"Self Destruct Sytem": {"costmultiplier": 5}
}

shipsensors = {
	"Cut Rate": {"range": "short", "mod": -2, "cost": 1},
	"Budget short-range": {"range": "short", "mod": 0, "cost": 2},
	"Basic short-range": {"range": "short", "mod": 2, "cost": 3},
	"Advanced short-range": {"range": "short", "mod": 4, "cost": 4},
	"Budget medium-range": {"range": "medium", "mod": 0, "cost": 3},
	"Basic medium-range": {"range": "medium", "mod": 2, "cost": 5},
	"Advanced medium-range": {"range": "medium", "mod": 4, "cost": 8},
	"Budget long-range": {"range": "long", "mod": 0, "cost": 6},
	"Basic long-range": {"range": "long", "mod": 2, "cost": 10},
	"Advanced long-range": {"range": "long", "mod": 4, "cost": 14},
}

shipshields = {
	"Basic Shields 1": {"Total SP": "10", "Regen rate": "1 per min", "PCU": 5, "Cost": 2},
	"Basic Shields 2": {"Total SP": "20", "Regen rate": "1 per min", "PCU": 10, "Cost": 3},
	"Basic Shields 3": {"Total SP": "30", "Regen rate": "1 per min", "PCU": 15, "Cost": 4},
	"Basic Shields 4": {"Total SP": "40", "Regen rate": "1 per min", "PCU": 15, "Cost": 5},
	"Light Shields 1": {"Total SP": "50", "Regen rate": "2 per min", "PCU": 20, "Cost": 6},
	"Light Shields 2": {"Total SP": "60", "Regen rate": "2 per min", "PCU": 20, "Cost": 8},
	"Light Shields 3": {"Total SP": "70", "Regen rate": "2 per min", "PCU": 25, "Cost": 10},
	"Light Shields 4": {"Total SP": "80", "Regen rate": "2 per min", "PCU": 30, "Cost": 12},
	"Medium Shields 1": {"Total SP": "90", "Regen rate": "4 per min", "PCU": 30, "Cost": 13},
	"Medium Shields 2": {"Total SP": "100", "Regen rate": "4 per min", "PCU": 30, "Cost": 15},
	"Medium Shields 3": {"Total SP": "120", "Regen rate": "4 per min", "PCU": 35, "Cost": 17},
	"Medium Shields 4": {"Total SP": "140", "Regen rate": "8 per min", "PCU": 40, "Cost": 18},
	"Medium Shields 5": {"Total SP": "160", "Regen rate": "8 per min", "PCU": 45, "Cost": 20},
	"Medium Shields 6": {"Total SP": "200", "Regen rate": "8 per min", "PCU": 50, "Cost": 22},
	"Heavy Shields 1": {"Total SP": "240", "Regen rate": "16 per min", "PCU": 55, "Cost": 23},
	"Heavy Shields 2": {"Total SP": "280", "Regen rate": "16 per min", "PCU": 60, "Cost": 25},
	"Heavy Shields 3": {"Total SP": "320", "Regen rate": "16 per min", "PCU": 70, "Cost": 27},
	"Heavy Shields 4": {"Total SP": "360", "Regen rate": "32 per min", "PCU": 80, "Cost": 28},
	"Heavy Shields 5": {"Total SP": "420", "Regen rate": "32 per min", "PCU": 90, "Cost": 30},
	"Heavy Shields 6": {"Total SP": "480", "Regen rate": "32 per min", "PCU": 110, "Cost": 32},
	"Superior Shields 1": {"Total SP": "540", "Regen rate": "64 per min", "PCU": 130, "Cost": 35},
	"Superior Shields 2": {"Total SP": "600", "Regen rate": "64 per min", "PCU": 160, "Cost": 40}
}

direct_ship_weapons = {
	"Chain cannon": {"type": "Light", "Range": "Short", "Damage": "6d4", "PCU": 15, "Cost" 15, "Special": "Ripper"},
	"Coilgun": {"type": "Light", "Range": "Long", "Damage": "4d4", "PCU": 10, "Cost" 6, "Special": "-"},
	"Flak Thrower": {"type": "Light", "Range": "Short", "Damage": "3d4", "PCU": 10, "Cost" 5, "Special": "Point +8"},
	"Gyrolaser": {"type": "Light", "Range": "Short", "Damage": "1d8", "PCU": 10, "Cost" 5, "Special": "Broad Arc"},
	"Laser Net": {"type": "Light", "Range": "Short", "Damage": "2d6", "PCU": 10, "Cost" 9, "Special": "Point +10"},
	"Light EMP Cannon": {"type": "Light", "Range": "Short", "Damage": "Special", "PCU": 10, "Cost" 8, "Special": "EMP"},
	"Light Laser Cannon": {"type": "Light", "Range": "Short", "Damage": "2d4", "PCU": 5, "Cost" 2, "Special": "-"},
	"Light Particle Beam": {"type": "Light", "Range": "Medium", "Damage": "3d6", "PCU": 10, "Cost" 10, "Special": "-"},
	"Light Plasma Cannon": {"type": "Light", "Range": "Short", "Damage": "2d12", "PCU": 10, "Cost" 12, "Special": "-"},
	"Graser": {"type": "Heavy", "Range": "Short", "Damage": "7d10", "PCU": 40, "Cost" 35, "Special": "Irradiate(Medium)"},
	"Gravity Gun": {"type": "Heavy", "Range": "Medium", "Damage": "6d6", "PCU": 40, "Cost" 30, "Special": "Tractor Beam"},
	"Heavy EMP Cannon": {"type": "Heavy", "Range": "Medium", "Damage": "Special", "PCU": 30, "Cost" 24, "Special": "EMP"},
	"Heavy Laser Array": {"type": "Heavy", "Range": "Short", "Damage": "6d4", "PCU": 15, "Cost" 10, "Special": "Array"},
	"Heavy Laser Cannon": {"type": "Heavy", "Range": "Medium", "Damage": "4d8", "PCU": 10, "Cost" 8, "Special": "-"},
	"Heavy Laser Net": {"type": "Heavy", "Range": "Short", "Damage": "5d6", "PCU": 15, "Cost" 12, "Special": "Point +12"},
	"Maser": {"type": "Heavy", "Range": "Long", "Damage": "6d10", "PCU": 35, "Cost" 22, "Special": "-"},
	"Particle Beam": {"type": "Heavy", "Range": "Long", "Damage": "8d6", "PCU": 25, "Cost" 15, "Special": "-"},
	"Persistent Particle Beam": {"type": "Heavy", "Range": "Long", "Damage": "10d6", "PCU": 40, "Cost" 25, "Special": "-"},
	"Plasma cannon": {"type": "Heavy", "Range": "Medium", "Damage": "5d12", "PCU": 30, "Cost" 20, "Special": "-"},
	"Railgun": {"type": "Heavy", "Range": "Long", "Damage": "8d4", "PCU": 20, "Cost" 15, "Special": "-"},
	"Twin Laser": {"type": "Heavy", "Range": "Long", "Damage": "5d8", "PCU": 15, "Cost" 12, "Special": "-"},
	"X-Laser cannon": {"type": "Heavy", "Range": "Long", "Damage": "8d6", "PCU": 40, "Cost" 35, "Special": "Line"},
	"Capital Gravity Cannon": {"type": "Capital", "Range": "Long", "Damage": "2d6 x 10", "PCU": 40, "Cost" 50, "Special": "Tractor Beam"},
	"Mass Driver": {"type": "Capital", "Range": "Long", "Damage": "2d6 x 10", "PCU": 25, "Cost" 25, "Special": "-"},
	"Particle Beam Cannon": {"type": "Capital", "Range": "Long", "Damage": "3d4 x 10", "PCU": 30, "Cost" 30, "Special": "-"},
	"Persistent Particle Beam Cannon": {"type": "Capital", "Range": "Long", "Damage": "2d10 x 10", "PCU": 50, "Cost" 40, "Special": "-"},
	"Super EMP cannon": {"type": "Capital", "Range": "Long", "Damage": "Special", "PCU": 45, "Cost" 45, "Special": "EMP"},
	"Super Plasma Cannon": {"type": "Capital", "Range": "Medium", "Damage": "3d6 x 10", "PCU": 45, "Cost" 35, "Special": "-"},
	"Super X-laser Cannon": {"type": "Capital", "Range": "Long", "Damage": "3d4 x 10", "PCU": 50, "Cost" 60, "Special": "Line"},
	"Supergraser": {"type": "Capital", "Range": "Medium", "Damage": "2d8 x 10", "PCU": 50, "Cost" 60, "Special": "Irradiate(High)"},
	"Superlaser": {"type": "Capital", "Range": "Long", "Damage": "2d4 x 10", "PCU": 20, "Cost" 20, "Special": "-"},
	"Supermaser": {"type": "Capital", "Range": "Long", "Damage": "2d8 x 10", "PCU": 40, "Cost" 35, "Special": "-"},
	"Vortex Cannon": {"type": "Capital", "Range": "Long", "Damage": "2d12 x 10", "PCU": 55, "Cost" 75, "Special": "Vortex"},
}

