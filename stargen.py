import random

def stargen():
	STARGEN = (
	"Mainstream Star",
	"Blue Giant",
	"Red Giant",
	"White Dwarf",
	"Red Dwarf",
	"Binary Star System",
	"Trinary Star System"
	)
	Stars = random.choice(STARGEN)
	print Stars
