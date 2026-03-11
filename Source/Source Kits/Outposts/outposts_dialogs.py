#=#######################################
# Lumos: 
# About the placement: in the example build, I've placed the dialogs
#  at the end of module_dialogs. You can place it anywhere, but know that
#  if you have other patrol talks, like Diplomacy's, they might override these.
#  Be sure to have these dialogs placed BEFORE any conflicting others.

# There's also a possible bug with the beginning merchant's dialogs,
# if you put these too much to the start of the file.

from header_dialogs import *
from header_operations import *
from module_constants import *
from header_common import *
from header_parties import *

start_dialogs = [
  [anyone, "start",
    [
	 (this_or_next|party_slot_eq, "p_outpost_1", slot_outpost_patrol, "$g_encountered_party"),
	 (this_or_next|party_slot_eq, "p_outpost_2", slot_outpost_patrol, "$g_encountered_party"),
	 (party_slot_eq, "p_fort", slot_outpost_patrol, "$g_encountered_party"),
	 #(neq, "$talk_context", tc_merchants_house), # Bugfix ?
	 (neq, "$g_encountered_party", 0), #better bugfix, i would think
	# Report current activity:
	#(party_get_slot, ":patrol_state", "$g_encountered_party", slot_outpost_patrol_behavior),
	(party_get_slot, ":patrol_state", "$g_encountered_party", slot_party_ai_state),
	(try_begin),
		(eq, ":patrol_state", spai_accompanying_army),
		(str_store_string, s1, "@We are currently following you."),
	(else_try),
		(eq, ":patrol_state", spai_holding_center),
		(str_store_string, s1, "@We are currently holding this location."),
	(else_try),
		(eq, ":patrol_state", spai_patrolling_around_center),
		(str_store_string, s1, "@We are currently patrolling around the outpost."),
	(else_try), # Assume that patrolling is the normal activity
		(str_store_string, s1, "@We are currently patrolling around the area."),
	(try_end),
	],
   "Good day, {sir/madam}. Is there anything we can do for you? {s1}", "outpost_patrol",[]],
  
  #[anyone,"start", [(party_slot_eq, "$g_encountered_party", slot_party_type, spt_fort),(party_stack_get_troop_id, ":captain", "$g_encountered_party", 0),(eq, "$g_talk_troop", ":captain")], "How may I help you, Commander?", "fort_captain",[]],
  [anyone,"start", [(party_slot_eq, "$g_encountered_party", slot_party_type, spt_fort),(this_or_next|eq, "$g_talk_troop", "trp_fort_walker"),(eq, "$g_talk_troop", "trp_fort_rider")], "Yes {sir/madam}?", "fort_guard_talk",[]],
]

dialogs = [   

 [anyone,"outpost_patrol_pretalk", [], "Anything else?", "outpost_patrol",[]],   
   
	# Lumos: Stolen from the cattle herding. :D
  [anyone|plyr,"outpost_patrol", [(neg|party_slot_eq, "$g_encountered_party", slot_party_ai_state, spai_accompanying_army)], "Follow me.", "outpost_patrol_pretalk",[ 
        (party_set_slot, "$g_encountered_party", slot_party_ai_state, spai_accompanying_army),
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_escort_party),
        (party_set_ai_object,"$g_encountered_party", "p_main_party"),
	]],
  [anyone|plyr,"outpost_patrol", [(neg|party_slot_eq, "$g_encountered_party", slot_party_ai_state, spai_holding_center)], "Hold this location.", "outpost_patrol_pretalk",[
        (party_set_slot, "$g_encountered_party", slot_party_ai_state, spai_holding_center),
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_hold),
		(party_get_position, pos1, "p_main_party"),
		(party_set_ai_target_position, "$g_encountered_party", pos1),
		(party_set_ai_object, "$g_encountered_party", "$g_encountered_party"),
	]], 
  [anyone|plyr,"outpost_patrol", [], "Patrol around this location.", "outpost_patrol_pretalk",[
        (party_set_slot, "$g_encountered_party", slot_party_ai_state, spai_engaging_army), #just to give it a value
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_patrol_location),
        (party_set_ai_patrol_radius, "$g_encountered_party", 1),
		(party_get_position, pos1, "p_main_party"),
        (party_set_ai_target_position, "$g_encountered_party", pos1),
		(party_set_ai_object, "$g_encountered_party", "$g_encountered_party"),
	]], 

  [anyone|plyr,"outpost_patrol", [(neg|party_slot_eq, "$g_encountered_party", slot_party_ai_state, spai_patrolling_around_center)], "Patrol around your outpost.", "outpost_patrol_pretalk",[
        (party_set_slot, "$g_encountered_party", slot_party_ai_state, spai_patrolling_around_center),
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_patrol_party),
        (party_set_ai_patrol_radius, "$g_encountered_party", 1),
		(party_get_slot, ":home", "$g_encountered_party", slot_party_home_center),
		(party_set_ai_object, "$g_encountered_party", ":home"),
	]], 
  [anyone|plyr,"outpost_patrol", [], "I want to give some troops to you.", "outpost_patrol_pretalk",[
        (change_screen_exchange_members, 0),
	]], 
  [anyone|plyr,"outpost_patrol", [], "Continue your activities.", "outpost_patrol_end",[]],
  
  [anyone, "outpost_patrol_end", [], "Aye, {sir/madam}.", "close_window", [(assign, "$g_leave_encounter", 1),(jump_to_menu, "mnu_auto_return")]],
 
  [anyone ,"fort_captain_pretalk", [], "Anything else, Commander?", "fort_captain",[]],
  
  [anyone|plyr, "fort_captain", [], "Is there anything I should know?.", "fort_captain_nothing", []],
  
  [anyone|plyr, "fort_captain", [], "That'll be all.", "close_window", [(assign, "$g_leave_encounter", 1),(change_screen_return, 0)]],
  
  [anyone ,"fort_captain_nothing", [], "Nothing right now.", "fort_captain_pretalk",[]],
  
  [anyone|plyr,"fort_guard_talk", [], "How goes the watch, soldier?", "fort_guard_talk_2",[]],
  [anyone,"fort_guard_talk_2", [], "All is quiet {sir/madam}. Nothing to report.", "fort_guard_talk_3",[]],
  [anyone|plyr,"fort_guard_talk_3", [], "Good. Keep your eyes open.", "close_window",[]],
#-## Outposts end  
]

from util_common import *
from util_wrappers import *

# Used by modmerger framework version >= 200 to merge stuff
def modmerge(var_set):
    try:
		var_name_1 = "dialogs"
		orig_dialogs = var_set[var_name_1]
		orig_dialogs.extend(dialogs)
		pos = FindDialog_i(orig_dialogs, anyone, "start", "dplmc_patrol_talk") #comment this out if you don't use diplomacy and use one of the lower two lines
		#pos = FindDialog_i(orig_dialogs, anyone, "start", "prison_guard_players") #for mods that don't include Diplomacy 
		#OpBlockWrapper(orig_dialogs).extend(start_dialogs) #non-Diplomacy alternative to put them at the end, too; use the above line or this one, not both
		OpBlockWrapper(orig_dialogs).InsertBefore(pos, start_dialogs)
    except KeyError:
        errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
        raise ValueError(errstring)