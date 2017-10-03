import random
from collections import OrderedDict
import pprint
import math
import sys
from monster_stats import saves, monsterstatgen


def statgen(enemy, level):
	rtn_stats = OrderedDict()
	rtn_stats = monsterstatgen(enemy)
	rtn_saves = OrderedDict()
	rtn_saves = saves(level)
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
	reflex = rtn_saves[rtn_stats["reflex"]]
	fort = rtn_saves[rtn_stats["fort"]]
	will = rtn_saves[rtn_stats["will"]]
	rtn_stats["HP"] = hitpoints
	rtn_stats["MAT"] = strmod+monlevel
	rtn_stats["RAT"] = dexmod+monlevel
	rtn_stats["REFSAVE"] = dexmod + reflex
	rtn_stats["FORTSAVE"] = conmod + fort
	rtn_stats["WILLSAVE"] = wismod + will
	return rtn_stats


if __name__ == "__main__":
	enemy = str(sys.argv[1])
	level = str(sys.argv[2])
	stats = statgen(enemy, level)

	pprint.pprint(stats)

