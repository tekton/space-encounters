import objectgen
from stargen import stargen
import random
from eventgen import spaceeventhook


entitycount = random.randint(1, 9)
eventcount = random.randint(5,9)
stargen()

while entitycount < 10:
	objectgen.encountergen()
	entitycount = entitycount +1

while eventcount < 10:
	spaceeventhook()
	eventcount = eventcount +1