import random

def statgen(level):
	strength = random.randint(14,18)
	dex = random.randint(12,16)
	con = random.randint(12,18)
	intelligence = random.randint(8,12)
	wisdom = random.randint(10,14)
	charisma = random.randint(8,12)
	stats = {"STR": strength, "DEX": dex, "CON": con, "INT": intelligence, "WIS": wisdom, "CHA": charisma}

	con_hit_points_bonus = ((con-10)/2) * level
	base_hit_points = level * random.randint(5,8)
	hit_points = int(con_hit_points_bonus + base_hit_points)

	print stats
	print "{} Hit points".format(int(hit_points))

statgen(3)