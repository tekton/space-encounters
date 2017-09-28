import random
from collections import OrderedDict
import pprint
import math
import sys
from monster_stats import *



def statgen(enemystats, level):
	rtn_stats = OrderedDict()
	rtn_stats = 
	strmod = int(math.floor((rtn_stats["STR"] -10)/2))
	dexmod = int(math.floor((rtn_stats["DEX"] -10)/2))
	conmod = int(math.floor((rtn_stats["CON"] -10)/2))
	intmod = int(math.floor((rtn_stats["INT"] -10)/2))
	wismod = int(math.floor((rtn_stats["WIS"] -10)/2))
	chamod = int(math.floor((rtn_stats["CHA"] -10)/2))
	monlevel = int(level)
	conmodtotal = monlevel*conmod
	hitdie = int(random.randint(1,12))
	hitpoints = (hitdie*monlevel) + conmodtotal
	rtn_stats["HP"] = hitpoints
	rtn_stats["MAT"] = strmod+monlevel
	rtn_stats["RAT"] = dexmod+monlevel
	rtn_stats["REFSAVE"] = dexmod + int(math.floor(monlevel/2))
	rtn_stats["FORTSAVE"] = conmod + int(math.floor(monlevel/2)+1)
	rtn_stats["WILLSAVE"] = wismod 
	return rtn_stats

if __name__ == "__main__":
	enemytype = str(sys.argv[1])
	level = str(sys.argv[2])
	stats = statgen(level)

	pprint.pprint(stats)