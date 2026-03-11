from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
from header_items import *   # Added for Show all Items presentation.
from module_items import *   # Added for Show all Items presentation.
import string

####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

presentations = [
 ]

from util_wrappers import *
from util_scripts import *

presentations_directives = [
#Adds the presentations for the new multiplayer scenes
    [SD_OP_BLOCK_INSERT, "game_multiplayer_admin_panel", D_SEARCH_FROM_TOP | D_SEARCH_SCRIPTLINE | D_INSERT_AFTER,(assign, ":map_image", "mesh_mp_ui_host_maps_randoms"), 0, [
      (else_try),
        (eq, "$g_multiplayer_selected_map", "scn_muiderslot"),
        (assign, ":map_image", "mesh_mp_ui_host_maps_muiderslot"),
    ]],
]

def modmerge_presentations(orig_presentations, check_duplicates = False):
    if( not check_duplicates ):
        orig_presentations.extend(presentations) # Use this only if there are no replacements (i.e. no duplicated item names)
    else:
    # Use the following loop to replace existing entries with same id
        for i in range (0,len(presentations)-1):
          find_index = find_object(orig_presentations, presentations[i][0]); # find_object is from header_common.py
          if( find_index == -1 ):
            orig_presentations.append(presentations[i])
          else:
            orig_presentations[find_index] = presentations[i]

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
        var_name_1 = "presentations"
        orig_presentations = var_set[var_name_1]
        modmerge_presentations(orig_presentations)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)