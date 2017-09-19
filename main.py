import objectgen
import stargen
import random

entitycount = random.randint(1, 9)

stargen.stargen()

while entitycount < 10:
	objectgen.encountergen()
	entitycount = entitycount +1