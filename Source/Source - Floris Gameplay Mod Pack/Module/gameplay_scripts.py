# Tournament Play Enhancements (1.3.8) by Windyplains
# Released 11/7/2011

from header_common import *
from header_operations import *
from module_constants import *
from header_mission_templates import *
from header_items import *
from header_presentations import *  # (COMPANIONS OVERSEER MOD)
from companions_constants import *  # (COMPANIONS OVERSEER MOD)

####################################################################################################################
# scripts is a list of script records.
# Each script record contains the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

scripts = [
# script_tpe_setup_loot_table
# Populates the loot table.
# Input: none
# Output: none
  ("tpe_setup_loot_table",
    [
		# Higher the slot value the more valuable the item.  Final value should be based on 200 + average(difficulty) + (level/3) or + (level/2 with level scaling on)
		(troop_set_slot, tpe_xp_table, 201, "itm_trade_wine"),
		(troop_set_slot, tpe_xp_table, 202, "itm_trade_furs"),
		(troop_set_slot, tpe_xp_table, 203, "itm_ho_swa_saddle_black"),
		(troop_set_slot, tpe_xp_table, 204, "itm_ho_swa_saddle_black"),
		(troop_set_slot, tpe_xp_table, 205, "itm_ho_swa_saddle_black"),
		(troop_set_slot, tpe_xp_table, 206, "itm_we_khe_sword_khergit"),
		(troop_set_slot, tpe_xp_table, 207, "itm_we_rho_crossbow_hunting"),
		(troop_set_slot, tpe_xp_table, 208, "itm_we_khe_spear_viper"),
		(troop_set_slot, tpe_xp_table, 209, "itm_trade_velvet"),
		(troop_set_slot, tpe_xp_table, 210, "itm_we_vae_bow_hunting"),
		# Medium Range Items
		(troop_set_slot, tpe_xp_table, 211, "itm_ar_swa_t3_hauberk_a"),
		(troop_set_slot, tpe_xp_table, 212, "itm_ar_vae_t4_jerkin_a"),
		(troop_set_slot, tpe_xp_table, 213, "itm_ho_swa_destrier_black"),
		(troop_set_slot, tpe_xp_table, 214, "itm_ho_swa_destrier_black"),
		(troop_set_slot, tpe_xp_table, 215, "itm_ho_swa_destrier_black"),
		(troop_set_slot, tpe_xp_table, 216, "itm_sh_swa_hea_horseman"),
		(troop_set_slot, tpe_xp_table, 217, "itm_ar_swa_t4_tabardmail_a"),
		(troop_set_slot, tpe_xp_table, 218, "itm_we_swa_blunt_morningstar"),
		(troop_set_slot, tpe_xp_table, 219, "itm_we_vae_bow_hunting"),
		(troop_set_slot, tpe_xp_table, 220, "itm_we_khe_spear_nagitakhergit"),
		(troop_set_slot, tpe_xp_table, 221, "itm_we_sar_axe_wariron"),
		(troop_set_slot, tpe_xp_table, 222, "itm_we_nor_sword_danish_great"),
		(troop_set_slot, tpe_xp_table, 223, "itm_we_swa_spear_lance_great"),
		(troop_set_slot, tpe_xp_table, 224, "itm_we_vae_sword_throw_daggers"),
		(troop_set_slot, tpe_xp_table, 225, "itm_sh_pla_rou_dragon"),
		(troop_set_slot, tpe_xp_table, 226, "itm_sh_rho_hea_golden"),
		(troop_set_slot, tpe_xp_table, 227, "itm_sh_rho_hea_golden"),
		(troop_set_slot, tpe_xp_table, 228, "itm_he_khe_t5_neck_a"),
		# Higher Range Items
		(troop_set_slot, tpe_xp_table, 229, "itm_we_pla_sword_hospitaller"),
		(troop_set_slot, tpe_xp_table, 230, "itm_we_vae_blunt_maul"),
		(troop_set_slot, tpe_xp_table, 231, "itm_we_pla_sword_strange_great"),
		(troop_set_slot, tpe_xp_table, 232, "itm_we_nor_axe_throw_vendelox"),
		(troop_set_slot, tpe_xp_table, 233, "itm_bo_pla_t6_shynbaulds"),
		(troop_set_slot, tpe_xp_table, 234, "itm_bo_pla_t7_greaves"),
		(troop_set_slot, tpe_xp_table, 235, "itm_ho_nor_war_blue"),
		(troop_set_slot, tpe_xp_table, 236, "itm_bo_pla_t7_greaves"),
		(troop_set_slot, tpe_xp_table, 237, "itm_bo_pla_t7_greaves"),
		(troop_set_slot, tpe_xp_table, 238, "itm_ar_vae_t6_cuirbouilli_a"),
		(troop_set_slot, tpe_xp_table, 239, "itm_we_vae_bow_imperial"),
		(troop_set_slot, tpe_xp_table, 240, "itm_we_vae_bow_imperial"),
		(troop_set_slot, tpe_xp_table, 241, "itm_ar_pla_t6_heraldic_a"),
	]),
]


from util_wrappers import *
from util_scripts import *

scripts_directives = [
	#rename scripts to "insert" switch scripts (see end of scripts[])
	#[SD_RENAME, "end_tournament_fight" , "orig_end_tournament_fight"], 
	#[SD_RENAME, "fill_tournament_participants_troop" , "orig_fill_tournament_participants_troop"],
	#[SD_RENAME, "get_random_tournament_participant" , "orig_get_random_tournament_participant"],
	#[SD_RENAME, "set_items_for_tournament" , "orig_set_items_for_tournament"], 
	#Add in global variable $g_wp_town_walkers into the visitor code for script_init_town_walkers.
	# [SD_OP_BLOCK_INSERT, "init_town_walkers", D_SEARCH_FROM_BOTTOM | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE, (set_visitor, ":entry_no", ":walker_troop_id"), 0, 
		# [(set_visitors,":entry_no", ":walker_troop_id", "$g_wp_town_walkers"),], 1],
	# [SD_OP_BLOCK_INSERT, "init_town_walkers", D_SEARCH_FROM_BOTTOM | D_SEARCH_LINENUMBER | D_INSERT_BEFORE, 0, 0, [
		# (call_script, "script_player_order_formations", ":order"),	#for formations
	# ]],
] # scripts_rename
                
def modmerge_scripts(orig_scripts):
	# process script directives first
	process_script_directives(orig_scripts, scripts_directives)
	# add remaining scripts
	add_scripts(orig_scripts, scripts, True)
	
# Used by modmerger framework version >= 200 to merge stuff
# This function will be looked for and called by modmerger if this mod is active
# Do not rename the function, though you can insert your own merging calls where indicated
def modmerge(var_set):
    try:
        var_name_1 = "scripts"
        orig_scripts = var_set[var_name_1]
    
        
		# START do your own stuff to do merging
		
        modmerge_scripts(orig_scripts)

		# END do your own stuff
        
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)