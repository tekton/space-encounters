import random
from objectgen import *

class Planet(object):
    def __init__(*args, **kwargs):
        pass

    def select_type(self):
        if not self.kind:
            pass

    def select_size(self):
            if not self.size:
              self.size =  random.choice(self.valid_sizes)

class IceWorld(Planet):
	def __init__(*args, **kwargs):
		self.kind = "Ice"
		self.valid_atmos = [
			"thin",
			"normal",
			"special"
		]
		self.population = low_world_pop

planet = IceWorld()