import random
from collections import OrderedDict
import pprint

def statgen():
	rtn_stats = OrderedDict()
	rtn_stats["STR"] = random.randint(14,18)
	rtn_stats["DEX"] = random.randint(12,16)
	rtn_stats["CON"] = random.randint(12,18)
	rtn_stats["INT"] = random.randint(8,12)
	rtn_stats["WIS"] = random.randint(10,14)
	rtn_stats["CHA"] = random.randint(8,12)
	return rtn_stats

statgen()