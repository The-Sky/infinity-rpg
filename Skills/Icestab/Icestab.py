# Icestab-Skill by Caffeine
#
# Version 1.0


# Imports

# ES-Imports
import es
import gamethread
import random
import playerlib
import weaponlib

# RPG-Imports
from infinityrpg import playerlist


# Script
skillname = 'Icestab'

frozen = []

def unload():
    for i in playerlist.GetPlayerlist():
        gamethread.cancelDelayed('rpg_%s_%s' %(skillname, i.userid))
        rpg_unfreeze(i.userid)

# When the player is hurt
def player_hurt(ev):
    attacker = ev['attacker']
    player = playerlist[ev['attacker']]
    # If damage is not NULL
    if ev['damage'].isdigit():
        damage = int(ev['damage'])
    elif ev['dmg_health'].isdigit():
        damage = int(ev['dmg_health'])
    player = playerlist[ev['userid']]
    userid = player.userid  
    # If Attacker and Victim are not frozen: 
    if ev['weapon'] == 'knife':
        if attacker and int(attacker) in frozen:
            quit()
        if damage >= 35:
            player = playerlist[ev['attacker']]
            level = player.GetSkillLevel(skillname)
            if level:
                if userid not in frozen:
                    frozen.append(userid)
                # Freeze the player
                gamethread.cancelDelayed('rpg_%s_%s' % (skillname, userid))
                es.emitsound('player', userid, 'physics/glass/glass_impact_bullet%s.wav' % random.randint(1,4), '1.0', '0.5')
                player = playerlib.getPlayer(userid)
                player.freeze(True)
                player.setColor(0, 0, 255)
                # Delay
                delayname = 'rpg_%s_%s' %(skillname, userid)
                gamethread.cancelDelayed(delayname)
                gamethread.delayedname(0.42 * level, delayname, rpg_unfreeze, (player.userid))   
    if ev['weapon'] != 'knife':
        if userid in frozen:
            player = playerlib.getPlayer(userid)
            player.health += int(damage / 100 * 98)

                
def player_death(ev):
    player = playerlist[ev['userid']]
    gamethread.cancelDelayed('rpg_%s_%s' %(skillname, player.userid))   
                
def rpg_unfreeze(userid):  
    player = playerlib.getPlayer(userid)
    player.freeze(False)
    player.setColor(255, 255, 255)
    if userid in frozen:
        frozen.remove(userid)

def player_spawn(ev):
    userid = ev['userid']
    player = playerlib.getPlayer(userid)
    player.setColor(255, 255, 255)
    if userid in frozen:
        frozen.remove(userid)

def round_start(ev):
    del frozen[:]
