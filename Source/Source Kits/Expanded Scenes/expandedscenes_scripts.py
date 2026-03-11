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
]

from util_wrappers import *
from util_scripts import *

scripts_directives = [
#Adds new multiplayer scenes to deathmatch, battle and capture the flag
    [SD_OP_BLOCK_INSERT, "multiplayer_fill_map_game_types", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,(troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 13, "scn_random_multi_steppe_large"), 0, [
          (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 14, "scn_muiderslot"),
    ]],

    [SD_OP_BLOCK_REPLACE, "multiplayer_fill_map_game_types", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE,(assign, ":num_maps", 14), 0, [
          (assign, ":num_maps", 15),
    ]],

    [SD_OP_BLOCK_INSERT, "multiplayer_fill_map_game_types", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,(troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 13, "scn_random_multi_steppe_large"), 0, [
          (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 14, "scn_muiderslot"),
    ]],

    [SD_OP_BLOCK_REPLACE, "multiplayer_fill_map_game_types", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE,(assign, ":num_maps", 14), 0, [
          (assign, ":num_maps", 15),
    ]],
    [SD_OP_BLOCK_INSERT, "multiplayer_fill_map_game_types", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,(troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 13, "scn_random_multi_steppe_large"), 0, [
          (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 14, "scn_muiderslot"),
    ]],

    [SD_OP_BLOCK_REPLACE, "multiplayer_fill_map_game_types", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE,(assign, ":num_maps", 14), 0, [
          (assign, ":num_maps", 15),
    ]],

#Adds new multiplayer scenes to headquarters
    [SD_OP_BLOCK_INSERT, "multiplayer_fill_map_game_types", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_BEFORE,(assign, ":num_maps", 10), 0, [
          (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 10, "scn_muiderslot"),
    ]],

    [SD_OP_BLOCK_REPLACE, "multiplayer_fill_map_game_types", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE,(assign, ":num_maps", 10), 0, [
          (assign, ":num_maps", 11),
    ]],

#Adds new multiplayer scenes to siege
    [SD_OP_BLOCK_INSERT, "multiplayer_fill_map_game_types", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,(troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 5, "scn_multi_scene_16"), 0, [
          (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 6, "scn_muiderslot"),
    ]],

    [SD_OP_BLOCK_REPLACE, "multiplayer_fill_map_game_types", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE,(assign, ":num_maps", 6), 0, [
          (assign, ":num_maps", 7),
    ]],
]
                
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