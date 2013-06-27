# Armor-Skill by Caffeine
#
# Version 1.0


# Imports

# ES-Imports
import es
import gamethread

# RPG-Imports
from infinityrpg import playerlist, skillhandler


# Script
skillname = 'Armor'

# Events 
def rpg_player_spawn(ev):  
    player = playerlist[ev['userid']]
    level = player.GetSkillLevel(skillname)
    player = player.player
    if level > 0:
        armor = level * 10
        if player.getArmor() < armor:
            player.setArmor(armor)      
				
