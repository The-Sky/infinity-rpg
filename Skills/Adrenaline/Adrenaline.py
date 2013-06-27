# Adrenaline-Skill by Caffeine
#
# Version 1.0


# Imports

# ES-Imports
import gamethread
import es
import playerlib
# RPG-Imports
from infinityrpg import playerlist, skillhandler


# Script
skillname = 'Adrenaline'

def unload():
    for i in playerlist.GetPlayerlist():
        gamethread.cancelDelayed('rpg_%s_%s' %(skillname, i.userid))
        rpg_repulse(i.userid)


def player_hurt(ev):
    # Get userid, level of this skill and playelib instance
    userid = int(ev['userid'])   
    player = playerlist[userid]
    level = player.GetSkillLevel(skillname)
    player = player.player
    if int(ev['attacker']) != 0:
        if level:
            #Set speed
            player.setSpeed(1 + 0.15 * level)
            delayname = 'rpg_%s_%s' %(skillname, userid)
            gamethread.cancelDelayed(delayname)
            gamethread.delayedname(1.5,delayname, rpg_repulse, (userid))

def player_death(ev):
    gamethread.cancelDelayed('rpg_%s_%s' %(skillname, ev['userid']))
            
            
def player_disconnect(ev):
    gamethread.cancelDelayed('rpg_%s_%s' %(skillname, ev['userid']))

def rpg_repulse(userid):
    skillname = 'Speed'
    player = playerlist[userid]
    level = player.GetSkillLevel(skillname)
    if level:
        es.setplayerprop(userid, 'CBasePlayer.localdata.m_flLaggedMovementValue', (1 + 0.015 * level))
    else:
        playerlist[userid].player.setSpeed(1)