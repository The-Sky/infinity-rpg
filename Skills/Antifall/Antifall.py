# Antifall-Skill by Caffeine
#
# Version 1.0


# Imports

# Python-Imports
import random

# ES-Imports
import es

# RPG-Imports
from infinityrpg import playerlist


# Script
skillname = 'Antifall'


def player_falldamage(ev):  
    player = playerlist[ev['userid']]
    level = player.GetSkillLevel(skillname)
    if level > 0:
        if random.randint(1,10) <= level * 2:
            player = player.player
            player.setHealth(player.getHealth() + int(float(ev['damage'])))     