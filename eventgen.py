import random

def spaceeventhook():
	event_list = [
		"A distress beacon on a nearby planet is pulsing.",
		"A battle between two ships is taking place.",
		"A ship crash lands on a nearby planet.",
		"The Hellknights are chasing a ship that claims to be innocent with intent to destroy it.",
		"Space evangelists decide the PC's souls are in dire peril, and will stop at nothing to convert them.",
		"Late-medieval societies have formed and are shooting at each other with early gunpowder weapons in a bloody war.",
		"An underground installation is emitting a unknown radiation, but the ship's priest is unwaveringly certain that they intend to build a weapon that can kill gods.",
		"Passive Sensors detect a weird energy signature. If the ship moves in any direction other than closer, the energy signature follows, maintaining the same distance.",
		"Discover a perfectly fine starship just floating along. There is no distress signal nor any signs of life/undeath. Boarding to look for clues and looting is safe, but attempting to take control of starship causes s&@~ to go sideways.",
		"Space gremlins got on board last time you docked/landed your starship. They are now running around your ship, dealing enough damage to key components to cause various systems to gain the Glitching condition.",
		"The delivery you where asked to make wakes up early from cryo-sleep. Either hostile creature like Alien or innocent forced into slavery.",
		"Someone left a bunch off-world creature on the planet. They're breeding like crazy and decimating the indigenous wildlife and/or plant-life.",
		"Perform an emergency landing due to a critical component allowing space flight is about to break. Play the barter trade game with the locals to get what you need to repair it.",
		"Attacked by pirates!",
		"There's something on the wing!",
		"Party comes out of drift travel in a mirror universe which is much darker, and must find their way home.",
		"A ship identical to the parties ship emergens at the same time in the same system. Both ships believe they are the real party, not the duplicate.",
		"First contact with an alien species",
		"The party makes contact with two warring factions on an industrial age planet, both whom beg the PCs to help them win the war!",
		"Space station casino",
		"The party must journey to a far off volcanic planet to destroy a powerful magic object",
		"An evil force is building a battle station disguised as a moon",
		"Your ship has fallen out of of Drift, there are no visible stars...",
		"Groundhog day style time loop, select one party member who remembers.",
		"A pulse has emanated from your Drift Drive, your ship has fallen out of of Drift, all navigational points are slightly out of alignment.",
		"Something is disrupting drift communication reducing your communications back to light speed. You and your crew are only able to react to what the system looked like X hours ago.",
		"Every time you drop out of drift you are in the same place you entered drift. You were moving while in the drift.",
		"Sensors indicate that somehow the underdeveloped planet you dropped out of Drift near has a society of preflight aliens living in a derelict starship."
		"You find a paradise planet whose weather control system has become damaged",
		"Cultists have set up shop in a nearby space hulk and are attempting to open a portal by drainging energy from the local star.",
		"You've stumbled upon a pirate haven.",
		"A high magic society has evolved on the planet without any technology.",
		"Overuse of resources by the residents of the local planet has lead them to being 4d6 days away from a major catastrophe.",
		"The players come out of the drift and have swapped bodies somehow. Roll randomly.",
		"A message comes in from an old shady contact, telling the players of a job to steal high value cargo from a bad guy.",
		"Its absolutely quiet. Nothing is happening.",
		"The players emerge from the drift in the intended location, but its 2d3 days earlier that it was when they went in",
		"A pact world cruiser demands the party stop and submit to inspection.",
		"A scientist is capturing victims from many different races to use them as pitri dishes to develop vaccines."
	]
	events = random.choice(event_list)
	print events