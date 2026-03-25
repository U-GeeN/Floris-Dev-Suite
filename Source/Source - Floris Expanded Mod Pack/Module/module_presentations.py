from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
import string

## CC
from header_skills import *
from header_items import *
##diplomacy start+ Import for use with terrain advantage
from header_terrain_types import *
##diplomacy end+
from module_items import *
from module_my_mod_set import *
## CC

####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

from module_presentations_part1 import *
from module_presentations_part2 import *
from module_presentations_part3 import *
from module_presentations_part4 import *

presentations = presentations_part1 + presentations_part2 + presentations_part3 + presentations_part4

 
# modmerger_start version=201 type=2
try:
    component_name = "presentations"
    var_set = { "presentations" : presentations }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
