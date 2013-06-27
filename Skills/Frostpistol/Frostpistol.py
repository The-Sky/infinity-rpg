# Frostpistol-Skill by Caffeine
#
# Version 1.0


# Imports

# ES-Imports
import es
import gamethread
import playerlib

# RPG-Imports
from infinityrpg import playerlist


# Script
skillname = 'Frostpistol'
 
        
def unload():
    for i in playerlist.GetPlayerlist():
        gamethread.cancelDelayed('rpg_%s_%s' %(skillname, i.userid))
        rpg_unfrost(i.userid)
    
    
def player_hurt(ev):    
    if ev['weapon'] in ('usp', 'glock', 'p228', 'deagle', 'fiveseven', 'elite'):
        # Get level of that skill and playerlib instance of the victim
        level = playerlist[ev['attacker']].GetSkillLevel(skillname)
        userid = int(ev['userid'])
        player = playerlist[userid].player        
        if level > 0:
            # Set delayname         
            delayname = 'rpg_%s_%s' %(skillname,userid)      
            # Set speed
            if ev['weapon'] in ('usp', 'glock', 'p228'):
                player.setSpeed(0.2)  
            else:
                player.setSpeed(0.4)  
            # Set delay 
            player.setColor(0, 0, 255)
            delaytime = level * 0.03                  
            gamethread.cancelDelayed(delayname)
            gamethread.delayedname(delaytime, delayname, rpg_unfrost, userid)                                                              
                    
                    
def player_death(ev):
    gamethread.cancelDelayed('rpg_%s_%s' %(skillname, ev['userid']))
            
            
def player_disconnect(ev):
    gamethread.cancelDelayed('rpg_%s_%s' %(skillname, ev['userid']))
            
            
def rpg_unfrost(userid):
    playerlist[userid].player.setSpeed(1) 
    playerlist[userid].player.setColor(255, 255, 255)

def player_spawn(ev):
    userid = ev['userid']
    player = playerlib.getPlayer(userid)
    player.setColor(255, 255, 255)
