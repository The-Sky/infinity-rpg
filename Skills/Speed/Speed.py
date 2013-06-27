# Speed-Skill by Caffeine
#
# Version 1.0


# Imports

# ES-Imports
import es

# RPG-Imports
from infinityrpg import playerlist, config



# Script
skillname = 'Speed'


# Events
def unload():
    for i in playerlist.GetPlayerlist():
        i.player.setSpeed(1.0)
        try:
            del i.properties['speed']
        except:
            pass
         
        
def rpg_player_spawn(ev):
    player = playerlist[ev['userid']]
    speed = 1 + player.GetSkillLevel(skillname) * 0.015
    player.player.setSpeed(speed) 
    player.properties['speed'] = speed 
    
    
def rpg_skill_level_changed(ev):
    if ev['skill'] == skillname:   
        player = playerlist[ev['userid']]
        speed = 1 + player.GetSkillLevel(skillname) * 0.015
        player.player.setSpeed(speed) 
        player.properties['speed'] = speed