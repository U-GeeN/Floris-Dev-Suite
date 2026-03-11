#=#######################################
# Lumos: You have to add the given troops to you module_troops file.
#-#######################################

# You can place them anywhere, but make sure they're not breaking
# any constant regions. Your safest bet would be to put them near the end.

from module_troops import *

troops = [
#-## Outposts begin
 ["fort_walker","Patrol","Guards",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_player_faction,
   [],
   def_attrib|level(11),wp(75),knows_common,swadian_man_face_young_1, swadian_man_face_old_2],
 ["fort_rider","Patrol","Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_gloves|tf_guarantee_shield,0,0,fac_player_faction,
   [],
   def_attrib|level(11),wp(75),knows_common|knows_riding_2,swadian_man_face_young_1, swadian_man_face_old_2],
 #["fort_slave","Slave","Slaves",0,0,0,fac_commoners,
 #  [itm_shirt],
 #  def_attrib|level(4),wp(20),knows_common,man_face_young_1, man_face_old_2],

 # ["fort_captain","Fort Captain","Fort Captains",tf_hero|tf_female|tf_allways_fall_dead|tf_no_capture_alive, scn_fort|entry(11),reserved,  fac_commoners,[itm_coat_of_plates,itm_splinted_greaves,itm_gauntlets],knight_attrib_5|level(40),wp(150),knows_common,0x0000000a1a00200336db6db6db6db6db00000000001db6db0000000000000000, 0x0000000a1a00200336db6db6db6db6db00000000001db6db0000000000000000],
#-## Outposts end
]

from util_common import *
from util_wrappers import *

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
		var_name_1 = "troops"
		orig_troops = var_set[var_name_1]
		pos = OpBlockWrapper(orig_troops).FindLastLine()
		OpBlockWrapper(orig_troops).InsertBefore(pos, troops)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)