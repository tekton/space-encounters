shipframes = {
	"Racer": {
		"cost": 4,
		"size": "tiny",
		"maneuverability": manuver_table["0"],
		 # "Perfect",
		"hp": 20,
		"HP increment": 5,
		"CT": "4",
		"weapons": {
			"forward": {
				"light": 1},
			"aft": {
				"light": 1}
		},
		"crew": {
			"min": 1,
			"max": 1
		}
	},
	"Interceptor": {
		"cost": 6,
		"size": "tiny",
		"Maneuverability": manuver_table["0"],
		"hp": 30,
		"HP increment": 5,
		"CT": "6",
		"Weapons": {
			"Forward": {
				"light": 2}
		},
		"Expansion Bays": 0,
		
		"crew": {
			"min": 1,
			"max": 1
		}
	},
	"Fighter": {
		"cost": 8,
		"size": "tiny",
		"Maneuverability": manuver_table["1"],
		"hp": 35,
		"HP increment": 5,
		"CT": "7",
		"Weapons": {
			"Forward": {
				"light": 2,
			},
			"Aft": {
				"light": 1,
			}
		},
		"Expansion Bays": 0,
		"crew": {
			"min": 1,
			"max": 2
		}
	},
	"Shuttle": {
		"cost": 6,
		"size": "small",
		"Maneuverability": manuver_table["0"],
		"hp": 35,
		"HP increment": 5,
		"CT": "7",
		"Weapons": {
			"Forward": {
				"light": 1,
			}
		},
		"Expansion Bays": 3,
		
		"crew": {
			"min": 1,
			"max": 4
		}
	},
	"Light Freighter": {
		"cost": 10,
		"size": "small",
		"Maneuverability": manuver_table["1"],
		"hp": 40,
		"HP increment": 10,
		"CT": "8",
		"Weapons": {
			"Forward": {
				"light": 2,
			},
			"Port": {
				"light": 1,
			},
			"Starboard": {
				"light": 1,
			}
		},
		"Expansion Bays": 3,
		
		"crew": {
			"min": 1,
			"max": 6
		}
	},
	"Explorer": {
		"cost": 12,
		"size": "medium",
		"Maneuverability": manuver_table["1"],
		"hp": 55,
		"HP increment": 10,
		"CT": "11",
		"Weapons": {
			"Forward": {
				"light": 1,
			},
			"Port": {
				"light": 1,
			},
			"Starboard": {
				"light": 1,
			},
			"turret": {
				"light": 1,
			}
		},
		"Expansion Bays": 4,
		
		"crew": {
			"min": 1,
			"max": 6
		}
	},
	"Transport": {
		"cost": 15,
		"size": "medium",
		"Maneuverability": manuver_table["2"],
		"hp": 70,
		"HP increment": 15,
		"CT": "14",
		"Weapons": {
			"Forward": {
				"light": 1,
				"heavy": 1,
			},
			"Aft": {
			"light": 1,
			},
			"turret": {
				"light": 2,
			}
		},
		"Expansion Bays": 5,
		
		"crew": {
			"min": 1,
			"max": 6
		}
	},
	"Destroyer": {
		"cost": 30,
		"size": "large",
		"Maneuverability": manuver_table["2"],
		"hp": 150,
		"HP increment": 20,
		"CT": "30",
		"Weapons": {
			"Forward": {
				"heavy": 2,
			},
			"Port": {
				"light": 1,
			},
			"Starboard": {
				"light": 1,
			},
			"Aft": {
				"light": 1,
			},
			"turret": {
				"light": 1,
			}
		},
		"Expansion Bays": 4,
		
		"crew": {
			"min": 6,
			"max": 20
		}
	},
	"Heavy Freighter": {
		"cost": 40,
		"size": "large",
		"Maneuverability": manuver_table["2"],
		"hp": 120,
		"HP increment": 20,
		"CT": "24",
		"Weapons": {
			"Forward": {
				"light": 2,
				"heavy": 1,
			},
			"Port": {
				"heavy": 1,
			},
			"Starboard": {
				"heavy": 1,
			}
		},
		"Expansion Bays": 8,
		
		"crew": {
			"min": 6,
			"max": 20
		}
	},
	"Bulk Freighter": {
		"cost": 55,
		"size": "huge",
		"Maneuverability": manuver_table["3"],
		"hp": 160,
		"HP increment": 20,
		"DT": "5",
		"CT": "32",
		"Weapons": {
			"Forward": {
				"heavy": 1,
			},
			"Aft": {
				"heavy": 1,
			},
			"turret": {
				"light": 2,
			}
		},
		"Expansion Bays": 10,
		
		"crew": {
			"min": 20,
			"max": 50
		}
	},
	"Cruiser": {
		"cost": 60,
		"size": "huge",
		"Maneuverability": manuver_table["2"],
		"hp": 180,
		"HP increment": 25,
		"DT": "5",
		"CT": "36",
		"Weapons": {
			"Forward": {
				"capital": 1},
			"Port": {
				"light": 1,
			},
			"Starboard": {
				"light": 1,
			},
			"turret": {
				"heavy": 1,
			}
		},
		"Expansion Bays": 6,
		
		"crew": {
			"min": 20,
			"max": 100
		}
	},
	"Carrier": {
		"cost": 120,
		"size": "gargantuan",
		"Maneuverability": manuver_table["3"],
		"hp": 240,
		"HP increment": 30,
		"DT": "10",
		"CT": "48",
		"Weapons": {
			"Forward": {
				"capital": 1},
			"Port": {
				"heavy": 3,
				},
			"Starboard": {
				"heavy": 3,
			},
			"Aft": {
				"light": 1,
			},
			"turret": {
				"light": 2,
			}
		},
		"Expansion Bays": 10,
		
		"crew": {
			"min": 75,
			"max": 200
		}
	},
	"Battleship": {
		"cost": 150,
		"size": "gargantuan",
		"Maneuverability": manuver_table["2"],
		"hp": 280,
		"HP increment": 40,
		"DT": "10",
		"CT": "56",
		"Weapons": {
			"Forward": {
				"heavy": 2,
				"capital": 1
				},
			"Port": {
				"light": 1,
				"heavy": 2,
			},
			"Starboard": {
				"light": 1,
				"heavy": 2,
			},
			"Aft": {
				"light": 1,
			},
			"turret": {
				"heavy": 2,
			}
		},
		"Expansion Bays": 8,
		
		"crew": {
			"min": 100,
			"max": 300
		}
	},
	"Dreadnought": {
		"cost": 200,
		"size": "gargantuan",
		"Maneuverability": manuver_table["4"],
		"hp": 400,
		"HP increment": 50,
		"DT": "15",
		"CT": "80",
		"Weapons": {
			"Forward": {
				"heavy": 2,
				"capital": 2
				},
			"Port": {
				"heavy": 3,
				"capital": 1
				},
			"Starboard": {
				"heavy": 3,
				"capital": 1
				},
			"turret": {
				"light": 4,
			}
		},
		"Expansion Bays": 20,
		
		"crew": {
			"min": 125,
			"max": 500
		}
	}
}