import random
from collections import OrderedDict
import pprint
import math
import sys

professions = {
	"Envoy": {"HP_per_Level": 6, "BaseAttack": "third", "fort": "Bad", "reflex": "Good", "will" "Good"},
	"Soldier": {"HP_per_Level": 7, "BaseAttack": "Full", "fort": "Good", "reflex": "Bad", "will" "Good"},
	"Mystic": {"HP_per_Level": 6, "BaseAttack": "third", "fort": "Bad", "reflex": "Bad", "will" "Good"},
	"Operative": {"HP_per_Level": 5, "BaseAttack": "third", "fort": "Bad", "reflex": "Bad", "will" "Good"},
	"Mechanic": {"HP_per_Level": 6, "BaseAttack": "third", "fort": "Good", "reflex": "Good", "will" "Bad"},
	"Solarian": {"HP_per_Level": 7, "BaseAttack": "Full", "fort": "Good", "reflex": "Bad", "will" "Good"},
	"Soldier": {"HP_per_Level": 5, "BaseAttack": "Third", "fort": "Bad", "reflex": "Bad", "will" "Good"},
}

spellsperday = {
	"1st Level": {"1": 2, "2": 2, "3": 3, "4": 3, "5": 4, "6": 4, "7": 4, "8": 4, "9": 5, "10": 5, "11": 5, "12": 5, "13": 5, "14": 5, "15": 5, "16": 5, "17": 5, "18": 5, "19": 5, "20": 5},
	"2nd Level": {"1": 0, "2": 0, "3": 0, "4": 2, "5": 2, "6": 3, "7": 3, "8": 4, "9": 4, "10": 4, "11": 4, "12": 5, "13": 5, "14": 5, "15": 5, "16": 5, "17": 5, "18": 5, "19": 5, "20": 5},
	"3rd Level": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 2, "8": 2, "9": 3, "10": 3, "11": 4, "12": 4, "13": 4, "14": 4, "15": 5, "16": 5, "17": 5, "18": 5, "19": 5, "20": 5},
	"4th Level": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 2, "11": 2, "12": 3, "13": 3, "14": 4, "15": 4, "16": 4, "17": 4, "18": 5, "19": 5, "20": 5},
	"5th Level": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 2, "14": 2, "15": 3, "16": 3, "17": 4, "18": 4, "19": 5, "20": 5},
	"6th Level": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 2, "17": 2, "18": 3, "19": 4, "20": 5}
}
