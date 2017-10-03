import random

def spaceeventhook():
	event_list = [
		"A distress beacon on a nearby planet is pulsing.",
		"A battle between two ships is taking place.",
		"A ship crash lands on a nearby planet."
	]
	events = random.choice(event_list)
	print events