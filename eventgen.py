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
	]
	events = random.choice(event_list)
	print events