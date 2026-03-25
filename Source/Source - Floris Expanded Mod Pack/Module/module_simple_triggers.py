from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *
##diplomacy start+
from header_terrain_types import *
from module_factions import dplmc_factions_end
##diplomacy end+

from module_constants import *

####################################################################################################################
# Simple triggers are the alternative to old style triggers. They do not preserve state, and thus simpler to maintain.
#
#  Each simple trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################



from module_simple_triggers_part1 import *
from module_simple_triggers_part2 import *
from module_simple_triggers_part3 import *
from module_simple_triggers_part4 import *
from module_simple_triggers_part5 import *

simple_triggers = simple_triggers_part1 + simple_triggers_part2 + simple_triggers_part3 + simple_triggers_part4 + simple_triggers_part5



# modmerger_start version=201 type=2
try:
    component_name = "simple_triggers"
    var_set = { "simple_triggers" : simple_triggers }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end