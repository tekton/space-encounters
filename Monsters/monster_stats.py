import random
from collections import OrderedDict
import pprint
import math
import sys
import copy

monsterstatranges = {
	"orc": {"strength": random.randint(14,18), "dexterity": random.randint(12,16), "constitution": random.randint(12,18), "intelligence": random.randint(8,12), "wisdom": random.randint(10,14), "charisma": random.randint(8,12), "reflex": "GoodMod", "fort": "GoodMod", "will": "BadMod"},
	"goblin": {"strength": random.randint(8,14), "dexterity": random.randint(12,16), "constitution": random.randint(10,14), "intelligence": random.randint(10,14), "wisdom": random.randint(10,14), "charisma": random.randint(8,12), "reflex": "GoodMod", "fort": "BadMod", "will": "BadMod"},
	"human": {"strength": random.randint(10,16), "dexterity": random.randint(10,16), "constitution": random.randint(10,16), "intelligence": random.randint(10,16), "wisdom": random.randint(10,16), "charisma": random.randint(10,16), "reflex": "GoodMod", "fort": "BadMod", "will": "BadMod"}, 
}

savedict = {
	"good": {"1": 2, "2": 3, "3": 3, "4": 4, "5": 4, "6": 5, "7": 5, "8": 6, "9": 6, "10": 7, "11": 7, "12": 8, "13": 8, "14": 9, "15": 9, "16": 10, "17":10, "18": 11, "19": 11, "20": 12},
	"bad": {"1": 0, "2": 0, "3": 1, "4": 1, "5": 1, "6": 2, "7": 2, "8": 2, "9": 3, "10": 3, "11": 3, "12": 4, "13": 4, "14": 4, "15": 5, "16": 5, "17":5, "18": 6, "19": 6, "20": 6}
}

def monsterstatgen(enemy):
	rtn_stats = OrderedDict()
	rtn_stats["STR"] = monsterstatranges[enemy]["strength"]
	rtn_stats["DEX"] = monsterstatranges[enemy]["dexterity"]
	rtn_stats["CON"] = monsterstatranges[enemy]["constitution"]
	rtn_stats["INT"] = monsterstatranges[enemy]["intelligence"]
	rtn_stats["WIS"] = monsterstatranges[enemy]["wisdom"]
	rtn_stats["CHA"] = monsterstatranges[enemy]["charisma"]
	rtn_stats["reflex"] = monsterstatranges[enemy]["reflex"]
	rtn_stats["fort"] = monsterstatranges[enemy]["fort"]
	rtn_stats["will"] = monsterstatranges[enemy]["will"]
	return rtn_stats

def saves(level):
	rtn_saves = OrderedDict()
	rtn_saves["GoodMod"] = savedict["good"][str(level)]
	rtn_saves["BadMod"] = savedict["bad"][str(level)]
	return rtn_saves