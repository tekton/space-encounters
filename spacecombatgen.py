import argparse
import math
import sys
import random
from collections import OrderedDict
from pprint import pprint
from ship_data.shiptiers import shiptiers, point_hp_mod_list, hp_mod
from ship_data.difficultymod import difficultymod
from ship_data.shipsizes import shipsizes
from ship_data.shipmaneuver import shipmaneuverability, manuver_table
from ship_data.shipframes import shipframes
from ship_data.shippower import shippower
from ship_data.shipthrusters import shipthrusters
from ship_data.shiparmor import shiparmor
from ship_data.shipcomputer import shipcomputer
from ship_data.shipcrewquarters import shipcrewquarters
from ship_data.shipdefensivecounter import shipdefensivecounter
from ship_data.shipdriftengines import shipdriftengines
from ship_data.shipexpansionbays import shipexpansionbays
from ship_data.shipsecurity import shipsecurity
from ship_data.shipsensors import shipsensors
from ship_data.shipshields import shipshields
from ship_data.directshipweapons import directshipweapons
from ship_data.trackingweapons import trackingshipweapons

def get_ship_tier_list(_max=0):
	rtn_list = []
	for tier in shiptiers:
		if shiptiers[tier]["points"] <= _max:
			rtn_list.append(shiptiers[tier])
	return rtn_list


def get_ship_tier(bp):
	# get the actual "tier" of ship since points are semi static
	last_cost = 0
	for tier in point_hp_mod_list:
		if bp > last_cost and bp <= tier["points"]:
			return tier
		last_cost = tier["points"]


def get_ship_frame_list(max_bp=1000,
		min_bp=0,
				        min_crew=None,
		max_crew=None,
				        min_cargo=None,
		max_cargo=None):
	print(min_bp,
		max_bp)
	rtn_list = []
	for frame in shipframes:
		print(frame,
		shipframes[frame]["cost"])
		append = 0
		append_max = 1
		if shipframes[frame]["cost"] <= max_bp and shipframes[frame]["cost"] >= min_bp:
			append += 1
		if min_crew:
			print("min_crew",
		min_crew,
		shipframes[frame]["crew"]["min"])
			append_max += 1
			if int(min_crew) >= shipframes[frame]["crew"]["min"]:
				append += 1
		if max_crew:
			print("max_crew",
		max_crew,
		shipframes[frame]["crew"]["max"])
			append_max += 1
			if int(max_crew) <= shipframes[frame]["crew"]["max"]:
				append += 1
		# cargo checks...
		if min_cargo:
			if int(min_cargo) > 0:
				append_max += 1
				if "Expansion Bays" in shipframes[frame]:
					print(frame,
		"min_cargo",
		int(min_cargo),
		shipframes[frame]["Expansion Bays"])
					if shipframes[frame]["Expansion Bays"] > 0 and int(min_cargo) <= shipframes[frame]["Expansion Bays"]:
						append += 1
		if max_cargo:
			if int(max_cargo) > 0:
				append_max += 1
				if "Expansion Bays" in shipframes[frame]:
					print(frame,
		"max_cargo",
		int(max_cargo),
		shipframes[frame]["Expansion Bays"])
					if shipframes[frame]["Expansion Bays"] > 0 and int(max_cargo) <= shipframes[frame]["Expansion Bays"]:
						append += 1
		# /cargo_checks
		if append == append_max:
			rtn_list.append(frame)
	return rtn_list


def gen_npc_ships(**kwargs):
	dif_mod = float(kwargs.pop("difficulty",
		".75"))
	if "pc_bp" not in kwargs or kwargs["pc_bp"] is None:
		_bp = random.randint(25,
		1000)
	else:
		_bp = int(kwargs.pop("pc_bp"))
	_handicap = int(kwargs.pop("pc_handicap",
		"0"))
	print(_bp,
		dif_mod,
		_handicap)
	bp = int(_bp * dif_mod) - _handicap
	print(bp)
	if bp < 25:
		bp = 25
	bp = get_ship_tier(bp)
	hp_mod = bp["hp_multiplier"]
	bp = bp["points"]
	print(bp)
	get_frames_dict = {
		"min_bp": int(bp * .1),
		"max_bp": int(bp * .3)
	}
	# check other limiters...
	if "min_crew" in kwargs:
		get_frames_dict["min_crew"] = kwargs["min_crew"]
	if "max_crew" in kwargs:
		get_frames_dict["max_crew"] = kwargs["max_crew"]
	if "min_cargo" in kwargs:
		get_frames_dict["min_cargo"] = kwargs["min_cargo"]
	if "max_cargo" in kwargs:
		get_frames_dict["max_cargo"] = kwargs["max_cargo"]
	#
	frames = get_ship_frame_list(**get_frames_dict)
	if len(frames) == 0:
		print("Unable to find any frames with the limits imposed!")
		return
	print(frames)
	frame = random.choice(frames)
	print(frame)
	bp = bp - shipframes[frame]["cost"]
	print(bp)


if __name__ == "__main__":
	# argument parsing and you
	parser = argparse.ArgumentParser()
	# What are we trying to run?
	parser.add_argument('--pc',
		help="Create a ship for the players",
		action="store_true")
	parser.add_argument('--npc',
		help="Create an NPC ship for people to interact with",
		action="store_true")
	# What are the options?
	parser.add_argument('--pc-bp', help="Player character(s) build points")
	parser.add_argument('--pc-handicap', help="Player character(s) handicap for calculations")
	parser.add_argument('--difficulty', help="The difficulty modifier of the encounter")
	parser.add_argument('--max-ships', help="The maximum number of ships to create")
	# Limiters for ship type
	parser.add_argument('--min-cargo', help="The minimum number of cargo holds")
	parser.add_argument('--max-cargo', help="The maximum number of cargo holds")
	parser.add_argument('--min-crew', help="The minimum number of crew members")
	parser.add_argument('--max-crew', help="The maximum number of crew members")
	#
	parser.add_argument('--debug',
		help="Change logging level to debug",
		action="store_true")
	#
	args = parser.parse_args()
	#
	print(args)
	# print(dir(args))
	print(args.__dict__)
	if args.npc:
		_d = args.__dict__
		for j in _d.keys():
			if _d[j] is None:
				del(_d[j])
		print(args)
		if "max_ships" in _d:
			for x in range(_d["max_ships"]):
				gen_npc_ships(**_d)
		else:
			gen_npc_ships(**_d)
	