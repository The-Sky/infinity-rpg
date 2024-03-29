# Vampire-Skill by Caffeine
#
# Version 1.0


# Imports

# RPG-Imports
from infinityrpg import playerlist, config



# Script
skillname = 'Vampire'


# Events            
def player_hurt(ev):
    # Get userid, level, maxHealth and plyerlib instance
    userid = int(ev['attacker']) 
    player = playerlist[userid] 
    maxHealth = player.properties['maxHealth']     
    level = player.GetSkillLevel(skillname)
    player = player.player
    # Calculate and set hp
    hp = player.getHealth() + int(int(ev['dmg_health']) * 0.075 * level)
    if hp < maxHealth:
        player.setHealth(hp) 
    else:
        player.setHealth(maxHealth)
