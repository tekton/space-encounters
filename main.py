import objectgen
from stargen import stargen
import random
from eventgen import spaceeventhook


entitycount = random.randint(1, 5)
stargen()

while entitycount < 6:
	objectgen.encountergen()
	entitycount = entitycount +1

spaceeventhook()
