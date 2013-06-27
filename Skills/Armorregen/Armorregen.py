# Armorregen-Skill by Caffeine
#
# Version 1.0


# Imports

# ES-Imports
import es
import playerlib
import gamethread

# RPG-Imports
from infinityrpg import playerlist, skillhandler


# Script
skillname = 'Armorregen'
        
def unload():
    gamethread.cancelDelayed('rpg_%s' %(skillname))    

def round_start(ev):
    gamethread.delayedname(5.0, 'rpg_%s' %(skillname), rpg_Armorregen, ())
    
def round_end(ev):
    gamethread.cancelDelayed('rpg_%s' %(skillname)) 
        
def rpg_Armorregen():
    gamethread.delayedname(5.0, 'rpg_%s' %(skillname), rpg_Armorregen, ())
    for i in playerlib.getPlayerList('#alive'):
        if level:
            # Get the player's maxhealth, level of this skill and it's playerlib instance
            player = playerlist[i]
            level = player.GetSkillLevel('Armor')
            MaxArmor = 10 * level
            player = player.player
            
            level = player.GetSkillLevel(skillname)
            # Calculate new Armor and set it 
            Armor = player.getArmor() + level
            if Armor < MaxArmor:
                player.setArmor(Armor)  
            else:
                player.setArmor(MaxArmor)