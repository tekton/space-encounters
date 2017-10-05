import sys
from pprint import pprint

basiconehandmeleeweapons = {
	"Unarmed Strike" : {"Level": "-", "price": "-", "damage": "1d3", "damagetype": "B", "Critical": "-", "bulk" "-", "Special": "Archaic, Nonlethal"},
	"Club" : {"Level": "0", "price": "-", "damage": "1d6", "damagetype": "B", "Critical": "-", "bulk" "L", "Special": "Analog, Archaic"},
	"Baton, Tactical" : {"Level": "1", "price": "90", "damage": "1d4", "damagetype": "B", "Critical": "-", "bulk" "L", "Special": "Analog, Operative"},
	"Battleglove, Cestus" : {"Level": "1", "price": "100", "damage": "1d4", "damagetype": "B", "Critical": "-", "bulk" "L", "Special": "Analog"},
	"Knife, Survival" : {"Level": "1", "price": "95", "damage": "1d4", "damagetype": "S", "Critical": "-", "bulk" "L", "Special": "Analog Operative"},
	"Dueling Sword, Tactical" : {"Level": "2", "price": "475", "damage": "1d6", "damagetype": "S", "Critical": "-", "bulk" "L", "Special": "Analog"},
	"Knife, Tactical" : {"Level": "7", "price": "6000", "damage": "2d4", "damagetype": "S", "Critical": "-", "bulk" "L", "Special": "Analog, Operative"},
	"Dueling Sword, Buzzblade" : {"Level": "8", "price": "9500", "damage": "2d6", "damagetype": "S", "Critical": "-", "bulk" "L", "Special": "Powered, Cpacity 20, usage 1"},
	"Incapacitator" : {"Level": "9", "price": "14200", "damage": "3d4", "damagetype": "B", "Critical": "Staggered", "bulk" "L", "Special": "Non-Lethal, Powered, Cpacity 20, Usage 2, Operative"},
	"battleglove, Power" : {"Level": "10", "price": "16100", "damage": "2d8", "damagetype": "B", "Critical": "-", "bulk" "L", "Special": "Powered, Capacity 20, Usage 1"},
	"Dueling Sword, Ultrathin" : {"Level": "11", "price": "26000", "damage": "3d6", "damagetype": "S", "Critical": "-", "bulk" "L", "Special": "Analog"},
	"Dagger, Ultrathin" : {"Level": "12", "price": "32800", "damage": "4d4", "damagetype": "S", "Critical": "-", "bulk" "L", "Special": "Analog, Operative"},
	"battleglove, Nova" : {"Level": "13", "price": "52500", "damage": "3d6", "damagetype": "S", "Critical": "-", "bulk" "L", "Special": "Analog"},
	"Dagger, Zero edge" : {"Level": "14", "price": "64400", "damage": "6d4", "damagetype": "S", "Critical": "-", "bulk" "L", "Special": "Analog, Operative"},
	"Dueling Sword, Ripper" : {"Level": "15", "price": "109250", "damage": "7d6", "damagetype": "S", "Critical": "-", "bulk" "L", "Special": "Powered, Capacity 20, usage 1"},
	"Peacemaker" : {"Level": "16", "price": "185300", "damage": "6d6", "damagetype": "B", "Critical": "Knockdown", "bulk" "L", "Special": "Powered, Capacity 20, usage 2, Operative, Stun"},
	"Battle Glove, Gravity" : {"Level": "17", "price": "214850", "damage": "5d10", "damagetype": "B", "Critical": "-", "bulk" "L", "Special": "Powered, Capacity 20, usage 1"},
	"Dagger, Molecular Rift" : {"Level": "17", "price": "275000", "damage": "10d4", "damagetype": "S", "Critical": "-", "bulk" "L", "Special": "Analog, Operative"},
	"Dueling Sword, Molecular Rift" : {"Level": "18", "price": "331200", "damage": "10d6", "damagetype": "S", "Critical": "-", "bulk" "L", "Special": "Analog"},
	"Baton, Advanced" : {"Level": "19", "price": "540000", "damage": "8d6", "damagetype": "B", "Critical": "-", "bulk" "L", "Special": "Operative, Powered, Capacity 20, usage 1"},
}

