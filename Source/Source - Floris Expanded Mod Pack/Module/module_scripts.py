# -*- coding: cp1254 -*-
from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from header_map_icons import *
from ID_animations import *
##diplomacy start+
from module_factions import dplmc_factions_begin, dplmc_factions_end, dplmc_non_generic_factions_begin
##diplomacy end+

## CC
from module_my_mod_set import *
from header_presentations import *
## CC

##diplomacy begin
##jrider reports
from header_presentations import tf_left_align
##diplomacy end

####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

from module_scripts_part1 import *
from module_scripts_part2 import *
from module_scripts_part3 import *
from module_scripts_part4 import *
from module_scripts_part5 import *

scripts = scripts_part1 + scripts_part2 + scripts_part3 + scripts_part4 + scripts_part5

  
# modmerger_start version=201 type=2
try:
    component_name = "scripts"
    var_set = { "scripts" : scripts }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end					  
	
