# Impulse-Skill by Caffeine
#
# Version 1.0


# Imports

# ES-Imports
import gamethread

# RPG-Imports
from infinityrpg import playerlist, skillhandler


# Script
skillname = 'Impulse'

def player_hurt(ev):
	if (ev['weapon'] not in ('usp', 'glock', 'p228', 'deagle', 'fiveseven', 'elite') or not skillhandler.IsLoaded('Frostpistol') or (ev['weapon'] in ('usp', 'glock', 'p228', 'deagle', 'fiveseven', 'elite') and playerlist[ev['attacker']].GetSkillLevel('Frostpistol') == 0)) and ev['weapon'] != 'knife' and int(ev['attacker']) != 0:
		# Get userid, level of this skill and playelib instance
		userid = int(ev['userid'])   
		player = playerlist[userid]
		level = player.GetSkillLevel(skillname)
		player = player.player
		# Set ammo
		try:
			player.setPrimaryAmmo(int(player.getAmmo('1')) + level)
		except:
			pass
		try:   
			player.setSecondaryAmmo(int(player.getAmmo('2')) + level)
		except:
			pass 
				