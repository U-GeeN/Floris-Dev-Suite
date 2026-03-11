# Kingdom Management Tools (WIP) by Windyplains
# Released --/--/--

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
###########################################################################################################################
#####                                                    KTM 1.0                                                      #####
###########################################################################################################################

# script_kmt_create_mesh
# Creates a mesh image based on mesh ID, (x,y) position, (x,y) size.
# Input: mesh_id, pos_x, pos_y, size_x, size_y
# Output: none
("kmt_create_mesh",
		[
			(store_script_param, ":mesh", 1),
			(store_script_param, ":pos_x", 2),
			(store_script_param, ":pos_y", 3),
			(store_script_param, ":size_x", 4),
			(store_script_param, ":size_y", 5),
			
			(set_fixed_point_multiplier, 1000),
			(create_mesh_overlay, reg0, ":mesh"),
			(position_set_x, pos1, ":pos_x"),
			(position_set_y, pos1, ":pos_y"),
			(overlay_set_position, reg0, pos1),
			(position_set_x, pos2, ":size_x"),
			(position_set_y, pos2, ":size_y"),
			(overlay_set_size, reg0, pos2),
		]
	),

]


from util_wrappers import *
from util_scripts import *

                
def modmerge_scripts(orig_scripts):
	# process script directives first
	# process_script_directives(orig_scripts, scripts_directives)
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