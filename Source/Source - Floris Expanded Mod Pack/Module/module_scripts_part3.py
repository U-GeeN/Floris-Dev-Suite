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

scripts_part3 = [

    
    
    # script_decide_faction_ai
    # Input: arg1: faction_no
    # Output: none
    #called from triggers
    ("decide_faction_ai",
      #This handles political issues and faction issues
      [
        (store_script_param_1, ":faction_no"),
        
        
        (faction_get_slot, ":old_faction_ai_state", ":faction_no", slot_faction_ai_state),
        (faction_get_slot, ":old_faction_ai_object", ":faction_no", slot_faction_ai_object),
        (faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
        
        
        #Remove marshal if he has become too controversial,, or he has defected, or has been taken prisoner
        (try_begin),
          (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
          (neq, ":faction_no", "fac_player_supporters_faction"),
          (ge, ":faction_marshal", "trp_player"),
          
          (store_faction_of_troop, ":marshal_faction", ":faction_marshal"),
          (try_begin),
            (eq, ":faction_marshal", "trp_player"),
            (assign, ":marshal_faction", "$players_kingdom"),
          (try_end),
          
          
          (assign, ":player_marshal_is_prisoner", 0),
          (try_begin),
            (eq, ":faction_marshal", "trp_player"),
            (eq, "$g_player_is_captive", 1),
            (assign, ":player_marshal_is_prisoner", 1),
          (try_end),
          
          
          #High controversy level, or marshal has defected, or is prisoner
          (this_or_next|neq, ":marshal_faction", ":faction_no"),
          (this_or_next|troop_slot_ge, ":faction_marshal", slot_troop_controversy, 80),
          (this_or_next|eq, ":player_marshal_is_prisoner", 1),
          (troop_slot_ge, ":faction_marshal", slot_troop_prisoner_of_party, 0),
          
          (assign, ":few_following_player_campaign", 0),
          (try_begin),
            (eq, ":faction_marshal", "trp_player"),
            (assign, ":vassals_following_player_campaign", 0),
            (gt, "$g_player_days_as_marshal", 1),
            (try_for_range, ":vassal", active_npcs_begin, active_npcs_end),
              (troop_slot_eq, ":vassal", slot_troop_occupation, slto_kingdom_hero),
              (store_faction_of_troop, ":vassal_faction", ":vassal"),
              (eq, ":vassal_faction", ":faction_no"),
              (call_script, "script_npc_decision_checklist_troop_follow_or_not", ":vassal"),
              (eq, reg0, 1),
              (val_add, ":vassals_following_player_campaign", 1),
            (try_end),
            (lt, ":vassals_following_player_campaign", 4),
            (assign, ":few_following_player_campaign", 1),
          (try_end),
          
          #Only remove marshal for controversy if offensive campaign in progress
          (this_or_next|eq, ":old_faction_ai_state", sfai_default),
          (this_or_next|eq, ":old_faction_ai_state", sfai_feast),
          (this_or_next|neq, ":marshal_faction", ":faction_no"),
          (this_or_next|eq, ":few_following_player_campaign", 1),
          (this_or_next|eq, ":player_marshal_is_prisoner", 1),
          (troop_slot_ge, ":faction_marshal", slot_troop_prisoner_of_party, 0),
          
          #No current issue on the agenda
          (this_or_next|faction_slot_eq, ":faction_no", slot_faction_political_issue, 0),
          (this_or_next|eq, ":player_marshal_is_prisoner", 1),
          (troop_slot_ge, ":faction_marshal", slot_troop_prisoner_of_party, 0),
          
          (faction_set_slot, ":faction_no", slot_faction_political_issue, 1), #Appointment of marshal
          (store_current_hours, ":hours"),
          (val_max, ":hours", 0),
          (faction_set_slot, ":faction_no", slot_faction_political_issue_time, ":hours"), #Appointment of marshal
          
          (faction_get_slot, ":old_marshall", ":faction_no", slot_faction_marshall),
          (try_begin),
            (ge, ":old_marshall", 0),
            (troop_get_slot, ":old_marshall_party", ":old_marshall", slot_troop_leaded_party),
            (party_is_active, ":old_marshall_party"),
            (party_set_marshall, ":old_marshall_party", 0),
          (try_end),
          
          (try_begin),
            (eq, "$players_kingdom", ":faction_no"),
            (faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
            (call_script, "script_add_notification_menu", "mnu_notification_relieved_as_marshal", 0, 0),
          (else_try),
            (neq, ":old_marshall", "trp_player"),
            (call_script, "script_change_troop_renown", ":old_marshall", 15),
          (try_end),
          (faction_set_slot, ":faction_no", slot_faction_marshall, -1),
          (assign, ":faction_marshal", -1),
          
          
          
		##diplomacy start+ add support for promoted kingdom ladies
		(try_for_range, ":active_npc", heroes_begin, heroes_end),#<- change active_npcs to heroes
		##diplomacy end+
			(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
			(eq, ":active_npc_faction", ":faction_no"),
			(troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
		(try_end),
		(try_begin),
			(eq, "$players_kingdom", ":faction_no"),
			(troop_set_slot, "trp_player", slot_troop_stance_on_faction_issue, -1),
		(try_end),
          
        (else_try),	 #If marshal not present, and not already on agenda, make political issue
          (eq, ":faction_marshal", -1),
          (neg|faction_slot_ge, ":faction_no", slot_faction_political_issue, 1), #This to avoid resetting votes every time
          
          (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
          (neq, ":faction_no", "fac_player_supporters_faction"),
          
          (faction_set_slot, ":faction_no", slot_faction_political_issue, 1), #Appointment of marshal
          (store_current_hours, ":hours"),
          (val_max, ":hours", 0),
          (faction_set_slot, ":faction_no", slot_faction_political_issue_time, ":hours"), #Appointment of marshal
          
			##diplomacy start+ add support for promoted kingdom ladies
			(try_for_range, ":active_npc", heroes_begin, heroes_end),#<- change active_npcs to heroes
			##diplomacy end+
				(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
				(eq, ":active_npc_faction", ":faction_no"),
				(troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
			(try_end),
			(try_begin),
				(eq, "$players_kingdom", ":faction_no"),
				(troop_set_slot, "trp_player", slot_troop_stance_on_faction_issue, -1),
			(try_end),
          
          
        (else_try),	#If player is marshal, but not part of faction
          (eq, ":faction_marshal", "trp_player"),
          (neq, "$players_kingdom", ":faction_no"),
          
          (faction_set_slot, ":faction_no", slot_faction_political_issue, 1), #Appointment of marshal
          (store_current_hours, ":hours"),
          (val_max, ":hours", 0),
          (faction_set_slot, ":faction_no", slot_faction_political_issue_time, ":hours"), #Appointment of marshal
          
          (faction_get_slot, ":old_marshall", ":faction_no", slot_faction_marshall),
          (try_begin),
            (ge, ":old_marshall", 0),
            (troop_get_slot, ":old_marshall_party", ":old_marshall", slot_troop_leaded_party),
            (party_is_active, ":old_marshall_party"),
            (party_set_marshall, ":old_marshall_party", 0),
          (try_end),
          
          (faction_set_slot, ":faction_no", slot_faction_marshall, -1),
          (assign, ":faction_marshal", -1),
          
			##diplomacy start+ add support for promoted kingdom ladies
			(try_for_range, ":active_npc", heroes_begin, heroes_end),#<- change active_npcs to heroes
			##diplomacy end+
				(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
				(eq, ":active_npc_faction", ":faction_no"),
				(troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
			(try_end),
			(try_begin),
				(eq, "$players_kingdom", ":faction_no"),
				(troop_set_slot, "trp_player", slot_troop_stance_on_faction_issue, -1),
			(try_end),
          
        (try_end),
        
        #If the faction issue is a center no longer under faction control, remove and reset
        (try_begin),
          (faction_get_slot, ":faction_political_issue", ":faction_no", slot_faction_political_issue),
          (is_between, ":faction_political_issue", centers_begin, centers_end),
          (store_faction_of_party, ":disputed_center_faction", ":faction_political_issue"),
          (neq, ":disputed_center_faction", ":faction_no"),
          
          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_faction_name, s4, ":faction_no"),
            (str_store_party_name, s5, ":disputed_center_faction"),
            (display_message, "@{!}DEBUG -- {s4} drops {s5} as issue as it has changed hands"),
          (try_end),
          
			#Reset political issue
			(faction_set_slot, ":faction_no", slot_faction_political_issue, 0),
			##diplomacy start+ add support for promoted kingdom ladies
			(try_for_range, ":active_npc", heroes_begin, heroes_end),#<- change active_npcs to heroes
			##diplomacy end+
				(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
				(eq, ":active_npc_faction", ":faction_no"),
				(troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
			(try_end),
			(try_begin),
				(eq, "$players_kingdom", ":faction_no"),
				(troop_set_slot, "trp_player", slot_troop_stance_on_faction_issue, -1),
			(try_end),
          
        (try_end),
        
        
        #Resolve the political issue on the agenda
        (try_begin),
          (faction_slot_ge, ":faction_no", slot_faction_political_issue, 1),
          (neq, ":faction_no", "fac_player_supporters_faction"),
          
          #Do not switch marshals during a campaign
          (this_or_next|faction_slot_ge, ":faction_no", slot_faction_political_issue, centers_begin),
          (this_or_next|faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_default),
          (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_feast),
          
          
          (faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
          
          (assign, ":total_lords", 0),
          (assign, ":lords_who_have_voted", 0),
          (assign, ":popular_favorite", -1),
          
		#Reset number of votes
		(troop_set_slot, "trp_player", slot_troop_temp_slot, 0),
		##diplomacy start+ add support for promoted kingdom ladies
		(try_for_range, ":active_npc", heroes_begin, heroes_end),#<- change active_npcs to heroes
		##diplomacy end+
			(troop_set_slot, ":active_npc", slot_troop_temp_slot, 0),
		(try_end),

		#Tabulate votes

		##diplomacy start+
		(try_begin),#count the player's vote
			(eq, "$players_kingdom", ":faction_no"),
			(ge, "$player_has_homage", 1),
			(troop_get_slot, ":lord_chosen_candidate", "trp_player", slot_troop_stance_on_faction_issue),
      			(gt, ":lord_chosen_candidate", -1),
			#You may notice that I don't count the player for "total_lords" if he was undecided.
			#This is so faction behavior will not be changed from Native if the player did not
			#support anyone.
			(val_add, ":total_lords", 1),
			(val_add, ":lords_who_have_voted", 1),
			(troop_set_slot, ":lord_chosen_candidate", slot_troop_temp_slot, 1),
			(assign, ":popular_favorite", ":lord_chosen_candidate"),
		(try_end),
		#add support for promoted kingdom ladies
		(try_for_range, ":voting_lord", heroes_begin, heroes_end),#<- changed active_npcs_begin/end to heroes_begin/end
			(this_or_next|troop_slot_eq, ":voting_lord", slot_troop_occupation, slto_kingdom_hero),
				(is_between, ":voting_lord", active_npcs_begin, active_npcs_end),
		       	#the dead / retired / exiled do not vote
			(neg|troop_slot_ge, ":voting_lord", slot_troop_occupation, slto_retirement),
		##diplomacy end+
			(store_faction_of_troop, ":voting_lord_faction", ":voting_lord"),
			(eq, ":voting_lord_faction", ":faction_no"),
			(val_add, ":total_lords", 1),
			(troop_get_slot, ":lord_chosen_candidate", ":voting_lord", slot_troop_stance_on_faction_issue),
			(gt, ":lord_chosen_candidate", -1),
			(val_add, ":lords_who_have_voted", 1),
			(troop_get_slot, ":total_votes", ":lord_chosen_candidate", slot_troop_temp_slot),
			(val_add, ":total_votes", 1),
			(troop_set_slot, ":lord_chosen_candidate", slot_troop_temp_slot, ":total_votes"),
			(try_begin),
				(gt, ":popular_favorite", -1),
				(troop_get_slot, ":current_winner_votes", ":popular_favorite", slot_troop_temp_slot),
				(gt, ":total_votes", ":current_winner_votes"),
				(assign, ":popular_favorite", ":lord_chosen_candidate"),
			(else_try),
				(eq, ":popular_favorite", -1),
				(assign, ":popular_favorite", ":lord_chosen_candidate"),
			(try_end),
		(try_end),

		#Check to see if enough lords have voted
		(store_div, ":number_required_for_quorum", ":total_lords", 5),
		(val_mul, ":number_required_for_quorum", 4),
		##diplomacy start+
		#Replace number required for quorum, altering it based on the centralization
		#value.  Do the same for the minimum time left on the agenda.
		(faction_get_slot, ":centralization", ":faction_no", dplmc_slot_faction_centralization),
		(val_clamp, ":centralization", -3, 4),
		(try_begin),
			#Disable this for now, since NPC kingdoms set their policies randomly.
			(eq, 0, 1),
			(neq, ":centralization", 0),
			(store_sub, ":number_required_for_quorum", 15, ":centralization"),#fully centralized = 12/20 , fully decentralized = 18/20
			(try_begin),
				#If the plutocracy/aristocracy slider is negative, allow it to offset
				#a negative centralization value for the purpose of quorum, on the
				#assumption that part of the "quorum" is accounted for by the influence
				#of merchants.  They do not vote currently, although integrating guild masters
				#and/or village elders into the faction issue system is something to consider
				#for the future.
				(ge, ":number_required_for_quorum", 16),
				(faction_get_slot, ":aristocracy", ":faction_no", dplmc_slot_faction_aristocracy),
				(lt, ":aristocracy", 0),
				(val_clamp, ":aristocracy", -3, 4),
				(val_add, ":number_required_for_quorum", ":aristocracy"),
				(val_max, ":number_required_for_quorum", 15),
			(try_end),
			(val_mul, ":number_required_for_quorum", ":total_lords"),
			(val_div, ":number_required_for_quorum", 20),
		(try_end),
		##diplomacy end+

#		(gt, ":lords_who_have_voted", ":number_required_for_quorum"),

		(store_current_hours, ":hours_on_agenda"),
		(faction_get_slot, ":hours_when_put_on_agenda", ":faction_no", slot_faction_political_issue_time), #Appointment of marshal
		(val_sub, ":hours_on_agenda", ":hours_when_put_on_agenda"),

		##diplomacy start+
		#Before, the maximum number of hours on the agenda for an issue before it became
		#eligible for resolution regardless of quorum was fixed at 120 (five days).
		#Modify this by 16 hours for every point of centralization, for a minimum
		#of 3 days and a maximum of 7 days.
		(assign, ":hours_on_agenda_threshold", 120),
		(try_begin),
			#Disable this for now, since arguably all of the NPC kingdoms are
			#supposed to have fairly similar structures.  From a gameplay perspective,
			#they choose their kingdom policy at random, so enabling this is  probably
			#not going to have good effects, unless more thought is given to balancing
			#centralization/decentralization for NPC kingdoms.
			(eq, 0, 1),
			(store_mul, ":hours_on_agenda_threshold", ":centralization", 16),
			(val_add, ":hours_on_agenda_threshold", 120),
			(try_begin),
				(neq, ":centralization", 0),
			(try_end),
		(try_end),
		
		#(this_or_next|gt, ":lords_who_have_voted", ":number_required_for_quorum"),
		#	(ge, ":hours_on_agenda", 120),
		
		(this_or_next|gt, ":lords_who_have_voted", ":number_required_for_quorum"),
			(ge, ":hours_on_agenda", ":hours_on_agenda_threshold"),
		##diplomacy end+
          
          (try_begin),
            (eq, "$cheat_mode", 1),
            (assign, reg4, ":lords_who_have_voted"),
            (assign, reg5, ":number_required_for_quorum"),
            (assign, reg7, ":hours_on_agenda"),
            (str_store_faction_name, s4, ":faction_no"),
            (display_message, "@{!}DEBUG -- Issue resolution for {s4}: {reg4} votes for a quorum of {reg5}, {reg7} hours on agenda"),
          (try_end),
          
          
          (try_begin),
            (eq, "$cheat_mode", 1),
            (display_message, "@{!}DEBUG -- Faction resolves political issue"),
          (try_end),
          
          
          #Resolve faction political issue
          (assign, ":winning_candidate", -1),
		  
			##diplomacy start+
			#Change "liege overrules lords" check.  The version in Native caused relation death spirals:
			#a lord who has no fiefs becomes unhappy, and since relation is symmetrical, this can result
			#in the liege never granting him fiefs.
			#
			#OLD BEHAVIOR:
	#		(else_try)
	#			(call_script, "script_troop_get_relation_with_troop", ":faction_leader", ":popular_favorite"),
	#			(this_or_next|ge, reg0, 10),
	#			(this_or_next|troop_slot_eq, ":faction_leader", slot_troop_stance_on_faction_issue, ":popular_favorite"),
	#				(troop_slot_eq, ":faction_leader", slot_troop_stance_on_faction_issue, -1),
	#
	#			(assign, ":winning_candidate", ":popular_favorite"),
	#		(else_try),#Lord overrules lords' opinion
	#			(gt, ":faction_leader", -1), #not sure why this is necessary
	#			(troop_get_slot, ":liege_choice", ":faction_leader", slot_troop_stance_on_faction_issue),
	#			(ge, ":liege_choice", -1),
	#
	#			(assign, ":winning_candidate", ":liege_choice"),
	#      (try_end),
	#
	#      NEW BEHAVIOR
			(troop_get_slot, ":liege_choice", ":faction_leader", slot_troop_stance_on_faction_issue),
			(assign, ":min_liege_relation", 10),#<-- Same as in default
			(faction_get_slot, ":issue_on_table", ":faction_no", slot_faction_political_issue),
			(try_begin),
			  (ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
			  #Alter the minimum for villages and castles, but not towns or the marshall.
			  (this_or_next|is_between, ":issue_on_table", villages_begin, villages_end),
			  (is_between, ":issue_on_table", castles_begin, castles_end),
			  (store_random_in_range, ":min_liege_relation", 0, 16),
			  (val_sub, ":min_liege_relation", 5),#-5 to 10
			(try_end),
			#New override check
			(try_begin),
				#When the player is co-ruler of the kingdom, his/her support for the popular
				#candidate can be sufficient to guarantee success over the opposition of the
				#king/queen.
				(ge, ":faction_leader", 1),
				(eq, "$players_kingdom", ":faction_no"),
				(this_or_next|troop_slot_eq, ":faction_leader", slot_troop_spouse, "trp_player"),
					(troop_slot_eq, "trp_player", slot_troop_spouse, ":faction_leader"),
				(troop_slot_eq, "trp_player", slot_troop_stance_on_faction_issue, ":popular_favorite"),
				(assign, ":winning_candidate", ":popular_favorite"),
			(else_try),
				#The leader may overrule a choice he disagrees with, if he dislikes the candidate
				#sufficiently and has someone else in mind.
            	(ge, ":faction_leader", 1),
				(neq, ":liege_choice", ":popular_favorite"),
				(gt, ":liege_choice", -1),
				(call_script, "script_troop_get_relation_with_troop", ":faction_leader", ":liege_choice"),
				(val_min, ":min_liege_relation", reg0),
					(call_script, "script_troop_get_relation_with_troop", ":faction_leader", ":popular_favorite"),
				(gt, ":min_liege_relation", reg0),
				(assign, reg0, 0),
					(try_begin),
				   (troop_slot_ge, ":faction_leader", slot_troop_prisoner_of_party, 0),
				   (store_random_in_range, reg0, 0, 2),
				(try_end),
				(try_begin),
					#The leader would have overruled the choice, but cannot because he is a prisoner.
						#Print a message letting people know when this happens.
					(eq, reg0, 1),
					(gt, ":popular_favorite", -1),
						(this_or_next|eq, "$players_kingdom", ":faction_no"),
						(ge, "$cheat_mode", 1),
						(str_store_faction_name, s4, ":faction_no"),
						(str_store_troop_name, s5, ":popular_favorite"),
						(str_store_troop_name, s0, ":faction_leader"),
						(try_begin),
							(eq, ":issue_on_table", 1),
						(display_message, "@{s5} has the greatest support among the lords of the {s4} to be the next marshall.  {s0} is indisposed and cannot overrule their choice."),
						(else_try),
							(is_between, ":issue_on_table", centers_begin, centers_end),
							(str_store_party_name, s1, ":issue_on_table"),
						(display_message, "@{s5} has the greatest support among the lords of the {s4} to receive {s1}.  {s0} is indisposed and cannot overrule their choice."),
						(try_end),
					(try_end),
				(eq, reg0, 0),
				(assign, ":winning_candidate", ":liege_choice"),
				(try_begin),
					#Print a message letting people know when this happens.
					(gt, ":popular_favorite", -1),
					(this_or_next|eq, "$players_kingdom", ":faction_no"),
						(ge, "$cheat_mode", 1),
					(str_store_faction_name, s4, ":faction_no"),
					(str_store_troop_name, s5, ":popular_favorite"),
					(str_store_troop_name, s0, ":faction_leader"),
					(try_begin),
						(eq, ":issue_on_table", 1),
						(display_message, "@{s5} has the greatest support among the lords of the {s4} to be the next marshall, but {s0} overrules their choice."),
					(else_try),
						(is_between, ":issue_on_table", centers_begin, centers_end),
						(str_store_party_name, s1, ":issue_on_table"),
						(display_message, "@{s5} has the greatest support among the lords of the {s4} to receive {s1}, but {s0} overrules their choice."),
					(try_end),
				(try_end),
			(else_try),
				#No override: use popular candidate
				(assign, ":winning_candidate", ":popular_favorite"),
			(try_end),
			##diplomacy end+
          
			  #Carry out faction decision
			  (try_begin), #Nothing happens
				(eq, ":winning_candidate", -1),
				
			  (else_try), #For player, create a menu to accept or refuse
				(eq, ":winning_candidate", "trp_player"),
				(eq, "$players_kingdom", ":faction_no"),
				(call_script, "script_add_notification_menu", "mnu_notification_player_faction_political_issue_resolved_for_player", 0, 0),
			  (else_try),
				(eq, ":winning_candidate", "trp_player"),
				(neq, "$players_kingdom", ":faction_no"),
				
				(try_begin),
				  (eq, "$cheat_mode", 1),
				  (str_store_faction_name, s4, ":faction_no"),
				  (str_store_party_name, s5, ":winning_candidate"),
				  (display_message, "@{!}DEBUG -- {s4} drops {s5} as winner, for having changed sides"),
				(try_end),
				
				##diplomacy start+ add support for promoted kingdom ladies
				(try_for_range, ":active_npc", heroes_begin, heroes_end),#<- change active_npcs to heroes
					(this_or_next|troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
						(is_between, ":active_npc", active_npcs_begin, active_npcs_end),
				##diplomacy end+
					(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
					(eq, ":active_npc_faction", ":faction_no"),
					(troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
				(try_end),
				(try_begin),
					(eq, "$players_kingdom", ":faction_no"),
					(troop_set_slot, "trp_player", slot_troop_stance_on_faction_issue, -1),
				(try_end),
				
			  (else_try),	#If candidate is not of winning faction, reset lrod votes
				(store_faction_of_troop, ":winning_candidate_faction", ":winning_candidate"),
				(neq, ":winning_candidate_faction", ":faction_no"),
				
				(try_begin),
				  (eq, "$cheat_mode", 1),
				  (str_store_faction_name, s4, ":faction_no"),
				  (str_store_party_name, s5, ":winning_candidate"),
				  (display_message, "@{!}DEBUG -- {s4} drops {s5} as winner, for having changed sides"),
				(try_end),
				##diplomacy start+ add support for promoted kingdom ladies
				(try_for_range, ":active_npc", heroes_begin, heroes_end),#<- change active_npcs to heroes
					(this_or_next|troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
						(is_between, ":active_npc", active_npcs_begin, active_npcs_end),
				##diplomacy end+
					(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
					(eq, ":active_npc_faction", ":faction_no"),
					(troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
				(try_end),
				(try_begin),
					(eq, "$players_kingdom", ":faction_no"),
					(troop_set_slot, "trp_player", slot_troop_stance_on_faction_issue, -1),
				(try_end),

			(else_try), #Honor awarded to another
				(faction_get_slot, ":issue_on_table", ":faction_no", slot_faction_political_issue),
				(try_begin), #A marshalship awarded to another
					(eq, ":issue_on_table", 1),
					(is_between, ":winning_candidate", active_npcs_begin, active_npcs_end),

					##diplomacy start+ add support for promoted kingdom ladies
					(this_or_next|is_between, ":winning_candidate", heroes_begin, heroes_end),
						(eq, "$players_kingdom", ":faction_no"),
					(this_or_next|troop_slot_eq, ":winning_candidate", slot_troop_occupation, slto_kingdom_hero),
					##diplomacy end+
					(this_or_next|is_between, ":winning_candidate", active_npcs_begin, active_npcs_end), #Prevents bug in which player given marshaldom of kingdom of which he/she is not a member
						(eq, "$players_kingdom", ":faction_no"),

					(assign, ":faction_marshal", ":winning_candidate"),
				(else_try), #A fief awarded to another
					(is_between, ":issue_on_table", centers_begin, centers_end),

					#If given to the player, resolved above
					(call_script, "script_give_center_to_lord", ":issue_on_table", ":winning_candidate", 0), #Zero means don't add garrison

					#If the player had requested a captured castle
					(try_begin),
						(eq, ":issue_on_table", "$g_castle_requested_by_player"),
						(party_slot_ge, ":issue_on_table", slot_town_lord, active_npcs_begin),
						(store_faction_of_party, ":faction_of_issue", ":issue_on_table"),
						(eq, ":faction_of_issue", "$players_kingdom"),
						(assign, "$g_center_to_give_to_player", ":issue_on_table"),
						(try_begin),
							(troop_get_slot, ":husband", "trp_player", slot_troop_spouse),
							##diplomacy start+ add support for promotede kingdom ladies
							(is_between, ":husband", heroes_begin, heroes_end),
							(this_or_next|troop_slot_eq, ":winning_candidate", slot_troop_occupation, slto_kingdom_hero),
							##diplomacy end+
							(is_between, ":husband", active_npcs_begin, active_npcs_end),
							(eq, "$g_castle_requested_for_troop", ":husband"),
							(neq, ":winning_candidate", ":husband"),
							(jump_to_menu, "mnu_requested_castle_granted_to_another_female"),
						(else_try),
							(jump_to_menu, "mnu_requested_castle_granted_to_another"),
						(try_end),
					(try_end),

				(try_end),

				(try_begin),
					(eq, ":faction_no", "$players_kingdom"),
					(call_script, "script_add_notification_menu", "mnu_notification_player_faction_political_issue_resolved", ":issue_on_table", ":winning_candidate"),
				(try_end),

			#Reset political issue
				(faction_set_slot, ":faction_no", slot_faction_political_issue, 0),
				##diplomacy start+ add support for promoted kingdom ladies
				(try_for_range, ":active_npc", heroes_begin, heroes_end),#<- change active_npcs to heroes
				##diplomacy end+
					(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
					(eq, ":active_npc_faction", ":faction_no"),
					(troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
				(try_end),
				(try_begin),
					(eq, "$players_kingdom", ":faction_no"),
					(troop_set_slot, "trp_player", slot_troop_stance_on_faction_issue, -1),
				(try_end),
			(try_end),
		(try_end),
        
		#Add fief to faction issues
		(try_begin),
			(faction_get_slot, ":faction_issue", ":faction_no", slot_faction_political_issue),
			(le, ":faction_issue", 0),

			(assign, ":landless_lords", 0),
			(assign, ":unassigned_centers", 0),
			(assign, ":first_unassigned_center_found", 0),

			(troop_set_slot, "trp_player", slot_troop_temp_slot, 0),
			##diplomacy start+ add support for promoted kingdom ladies
			(try_for_range, ":active_npc", heroes_begin, heroes_end),#<- change active_npcs to heroes
			##diplomacy end+
				(troop_set_slot, ":active_npc", slot_troop_temp_slot, 0),
			(try_end),

			(try_for_range, ":center", centers_begin, centers_end),
				(store_faction_of_party, ":center_faction", ":center"),
				(eq, ":center_faction", ":faction_no"),

				(party_get_slot, ":town_lord", ":center", slot_town_lord),

				(try_begin),
					(lt, ":town_lord", 0),
					(val_add, ":unassigned_centers", 1),
					(try_begin),
						(eq, ":first_unassigned_center_found", 0),
						(assign, ":first_unassigned_center_found", ":center"),
					(try_end),
				(else_try),
					(troop_set_slot, ":town_lord", slot_troop_temp_slot, 1),
				(try_end),
			(try_end),

			(store_add, ":landless_lords_plus_unassigned_centers", ":landless_lords", ":unassigned_centers"),
			(ge, ":landless_lords_plus_unassigned_centers", 2),

			(faction_set_slot, ":faction_no", slot_faction_political_issue, ":first_unassigned_center_found"),
			(store_current_hours, ":hours"),
			(faction_set_slot, ":faction_no", slot_faction_political_issue_time, ":hours"), #Fief put on agenda

			##diplomacy start+ add support for promoted kingdom ladies
			(try_for_range, ":active_npc", heroes_begin, heroes_end),#<- change active_npcs to heroes
			##diplomacy end+
				(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
				(eq, ":active_npc_faction", ":faction_no"),
				(troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
			(try_end),
			(try_begin),
				(eq, "$players_kingdom", ":faction_no"),
				(troop_set_slot, "trp_player", slot_troop_stance_on_faction_issue, -1),
			(try_end),
		(try_end),
        
        
        (try_begin), #If the marshal is changed
          (neg|faction_slot_eq, ":faction_no", slot_faction_marshall, ":faction_marshal"),
          #(assign, ":marshall_changed", 1),
          (eq, "$players_kingdom", ":faction_no"),
          (str_store_troop_name_link, s1, ":faction_marshal"),
          (str_store_faction_name_link, s2, ":faction_no"),
          (display_message, "@{s1} is the new marshal of the {s2}."),
          (call_script, "script_check_and_finish_active_army_quests_for_faction", ":faction_no"),
        (try_end),
        
        (try_begin), #If the marshal is changed
          (neg|faction_slot_eq, ":faction_no", slot_faction_marshall, ":faction_marshal"),
          (gt, ":faction_marshal", -1),
          (call_script, "script_appoint_faction_marshall", ":faction_no", ":faction_marshal"),
        (try_end),
        
        #DO FACTION AI HERE
        (try_begin),
          (eq, ":faction_no", "$players_kingdom"),
          (eq, ":faction_marshal", "trp_player"),
          (assign, ":faction_ai_decider", "trp_player"),
		(else_try),
			##diplomacy start+ add support for promoted kingdom ladies
			(is_between, ":faction_marshal", heroes_begin, heroes_end),
			#(this_or_next|troop_slot_eq, ":faction_marshal", slot_troop_occupation, slto_kingdom_hero),
			#(is_between, ":faction_marshal", active_npcs_begin, active_npcs_end),
			##diplomacy end+
          (assign, ":faction_ai_decider", ":faction_marshal"),
        (else_try),
          (faction_get_slot, ":faction_ai_decider", ":faction_no", slot_faction_leader),
        (try_end),
        
        (call_script, "script_npc_decision_checklist_faction_ai_alt",  ":faction_ai_decider"),
        (assign, ":new_strategy", reg0),
        (assign, ":new_object", reg1),
        
        #new ozan
        (try_begin),
          (neq, ":new_strategy", ":old_faction_ai_state"),
          (eq, ":new_strategy", sfai_gathering_army),
          (faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
          ##diplomacy 3.3.2 begin
          #native script error bug fix when no marshal
          (gt, ":faction_marshal", -1),															#	1.143 Port // In 1.143 its (ge, ":faction_marshal", 0) // This remained intact
          ##diplomacy 3.3.2 end
          (troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
          (party_set_slot, ":marshal_party", slot_party_ai_object, -1),
          (assign, "$g_gathering_new_started", 1),
          (call_script, "script_npc_decision_checklist_party_ai", ":faction_marshal"), #This handles AI for both marshal and other parties
          (call_script, "script_party_set_ai_state", ":marshal_party", reg0, reg1),
          (assign, "$g_gathering_new_started", 0),
        (else_try),
          #check if marshal arrived his target city during active gathering
          
          #for now i disabled below lines because after always/active gathering armies become very large.
          #in current style marshal makes active gathering only at first, it travels to a city and waits there.
          
          (eq, ":new_strategy", ":old_faction_ai_state"),
          (eq, ":new_strategy", sfai_gathering_army),
          (faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
          ##diplomacy 3.3.2 begin
          #native script error bug fix when no marshal
          (gt, ":faction_marshal", -1),															#	1.143 Port // In 1.143 its (ge, ":faction_marshal", 0) // This remained intact
          ##diplomacy 3.3.2 end
          (troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
			##diplomacy start+ 2011-06-08 Fix bug when the marshall leaded party is set negative!
		   (gt, ":marshal_party", -1),
		   ##diplomacy end+
          (party_get_slot, ":party_ai_object", ":marshal_party", slot_party_ai_object),
          (ge, ":party_ai_object", 0),
		  (ge, ":marshal_party", 0),															#	1.143 Port // Newly added
		  (party_is_active, ":marshal_party"),
		  (party_is_active, ":party_ai_object"),  												#	End
          (store_distance_to_party_from_party, ":dist", ":marshal_party", ":party_ai_object"),
          (le, ":dist", 5),
          (party_set_slot, ":marshal_party", slot_party_ai_object, -1),
        (try_end),
        #end ozan
        
        #The following logic is mostly transplanted to the new decision_checklist
        #Decision_checklist is used because I want to be able to reproduce the logic for strings
        #(call_script, "script_old_faction_ai"),
        #ozan - I collected all comment-out lines in here (faction ai script) and placed most bottom of scripts.py to avoid confusing.
        
        (faction_set_slot, ":faction_no", slot_faction_ai_state, ":new_strategy"),
        (faction_set_slot, ":faction_no", slot_faction_ai_object, ":new_object"),
        
        (call_script, "script_update_report_to_army_quest_note", ":faction_no", ":new_strategy", ":old_faction_ai_state"),
        
        (try_begin),
          (eq, ":new_strategy", sfai_feast),
          
          (store_current_hours, ":hours"),
          (faction_set_slot, ":faction_no", slot_faction_last_feast_start_time, ":hours"), #new
          
          (try_begin),
            (eq, "$g_player_eligible_feast_center_no", ":new_object"),
            (assign, "$g_player_eligible_feast_center_no", -1), #reset needed
          (try_end),
          (try_begin),
            (is_between, ":new_object", towns_begin, towns_end),
            (party_set_slot, ":new_object", slot_town_has_tournament, 2),
          (try_end),
        (try_end),
        
        #Change of strategy
        (try_begin),
          (neq, ":new_strategy", ":old_faction_ai_state"),
          
          (try_begin),
            (ge, "$cheat_mode", 1),
            (str_store_faction_name, s5, ":faction_no"),
            (display_message, "str_s5_decides_s14"),
          (try_end),
          
          (store_current_hours, ":hours"),
          (faction_set_slot, ":faction_no", slot_faction_ai_current_state_started, ":hours"),
          
          #Feast ends
          (try_begin),
            (eq, ":old_faction_ai_state", sfai_feast),
            (call_script, "script_faction_conclude_feast", ":faction_no", ":old_faction_ai_object"),
          (try_end),
          
          
          #Feast begins
          (try_begin),
            (eq, ":new_strategy", sfai_feast),
            (faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
            
            ##         (str_store_faction_name, s1, ":faction_no"),
            ##         (str_store_party_name, s2, ":faction_object"),
            ##         (display_message, "str_lords_of_the_s1_gather_for_a_feast_at_s2"),
            
            (party_get_slot, ":feast_host", ":faction_object", slot_town_lord),
            
            (try_begin),
              (check_quest_active, "qst_wed_betrothed"),
              
              (quest_slot_eq, "qst_wed_betrothed", slot_quest_giver_troop, ":feast_host"),
              (neg|quest_slot_ge, "qst_wed_betrothed", slot_quest_expiration_days, 362),
              (call_script, "script_add_notification_menu", "mnu_notification_player_wedding_day", ":feast_host", ":faction_object"),
            (else_try),
              (check_quest_active, "qst_wed_betrothed_female"),
              
              (quest_get_slot, ":player_betrothed", "qst_wed_betrothed", slot_quest_giver_troop),
              (store_faction_of_troop, ":player_betrothed_faction", ":player_betrothed"),
              (eq, ":player_betrothed_faction", ":faction_no"),
              (neg|quest_slot_ge, "qst_wed_betrothed", slot_quest_expiration_days, 362),
              (call_script, "script_add_notification_menu", "mnu_notification_player_kingdom_holds_feast", ":feast_host", ":faction_object"),
            (else_try),
              (eq, "$players_kingdom", ":faction_no"),
              (troop_slot_ge, "trp_player", slot_troop_renown, 150),
              
              
              (party_get_slot, ":feast_host", ":faction_object", slot_town_lord),
              (call_script, "script_add_notification_menu", "mnu_notification_player_kingdom_holds_feast", ":feast_host", ":faction_object"),
            (try_end),
          (try_end),
          
          
          #Offensive begins
          (try_begin),
            (eq, ":old_faction_ai_state", sfai_gathering_army),
            (is_between, ":new_strategy", sfai_attacking_center, sfai_feast),
            (try_begin),
              (eq, "$cheat_mode", 1),
              (str_store_faction_name, s5, ":faction_no"),
              (display_message, "str_s5_begins_offensive"),
            (try_end),
            
            #Appoint screening party
            (try_begin),
              (assign, ":total_lords_participating", 0),
              (assign, ":best_screening_party", -1),
              (assign, ":score_to_beat", 30), #closest in size to 50
              (troop_get_slot, ":faction_marshal_party", ":faction_marshal", slot_troop_leaded_party),
              (party_is_active, ":faction_marshal_party"),
              
		   ##diplomacy start+
           #(try_for_range, ":screen_leader", active_npcs_begin, active_npcs_end),##OLD
           (try_for_range, ":screen_leader", heroes_begin, heroes_end),##NEW
		   ##diplomacy end+
                (store_faction_of_troop, ":screen_leader_faction", ":screen_leader"),
                (eq, ":screen_leader_faction", ":faction_no"),
                
                (troop_get_slot, ":screening_party", ":screen_leader", slot_troop_leaded_party),
				 ##diplomacy start+ Guard against things such as the party being 0 (p_main_party)
				 (gt, ":screening_party", 0),
				 ##diplomacy end+				
                (party_is_active, ":screening_party"),
                (party_slot_eq, ":screening_party", slot_party_ai_state, spai_accompanying_army),
                (party_slot_eq, ":screening_party", slot_party_ai_object, ":faction_marshal_party"),
                (val_add, ":total_lords_participating", 1),
                
                (try_begin),
                  (ge, "$cheat_mode", 1),
                  (str_store_party_name, s4, ":screening_party"),
                  (display_message, "@{!}DEBUG -- {s4} participates in offensive"),
                (try_end),
                
                
                (store_party_size_wo_prisoners, ":screening_party_score", ":screening_party"),
                (val_sub, ":screening_party_score", 50),
                (val_abs, ":screening_party_score"),
                
                
                (lt, ":screening_party_score", ":score_to_beat"),
                
                #set party and score
                (assign, ":best_screening_party", ":screening_party"),
                (assign, ":score_to_beat", ":screening_party_score"),
              (try_end),
              
              (gt, ":total_lords_participating", 2),
              (party_is_active, ":best_screening_party"),
              (party_is_active, ":faction_marshal_party"), ##1.132, new line
              (call_script, "script_party_set_ai_state", ":best_screening_party", spai_screening_army, ":faction_marshal_party"),
              (try_begin),
                (ge, "$cheat_mode", 1),
                (str_store_party_name, s4, ":best_screening_party"),
                (display_message, "@{!}DEBUG -- {s4} chosen as screen"),
              (try_end),
              #after this - dialogs on what doing, npc_decision_checklist
            (try_end),
            
            #Offensive concludes
          (else_try),
            (store_current_hours, ":hours"),
            (this_or_next|eq, ":old_faction_ai_state", sfai_gathering_army),
            (this_or_next|eq, ":old_faction_ai_state", sfai_attacking_center),
            (this_or_next|eq, ":old_faction_ai_state", sfai_raiding_village),
            #(this_or_next|eq, ":old_faction_ai_state", sfai_attacking_enemies_around_center),
            (eq, ":old_faction_ai_state", sfai_attacking_enemy_army),
            
            (this_or_next|eq, ":new_strategy", sfai_default),
            (eq, ":new_strategy", sfai_feast),
            
            #         (faction_set_slot, ":faction_no", slot_faction_last_offensive_concluded, ":hours"), ##1.131: indeed, this line is moved downwards in 1.132
            (call_script, "script_check_and_finish_active_army_quests_for_faction", ":faction_no"),
            (faction_set_slot, ":faction_no", slot_faction_last_offensive_concluded, ":hours"), ##1.132
          (try_end),
        (try_end),
        
        (try_begin),
          (eq, "$players_kingdom", ":faction_no"),
          (neg|faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_center),
          (check_quest_active, "qst_join_siege_with_army"),
          (call_script, "script_abort_quest", "qst_join_siege_with_army", 0),
        (try_end),
        
        (try_begin),
          #old condition to rest, I changed below part - ozan, to rest (a faction's old strategy should be feast or default) and (a faction's new strategy should be feast or default)
          #(this_or_next|eq, ":new_strategy", sfai_default),
          #(this_or_next|eq, ":new_strategy", sfai_feast),
          #(this_or_next|eq, ":old_faction_ai_state", sfai_default),
          #(eq, ":old_faction_ai_state", sfai_feast),
          
          #new condition to rest, (a faction's new strategy should be feast or default) and (":hours_at_current_state" > 20)
          (this_or_next|eq, ":new_strategy", sfai_default),
          (eq, ":new_strategy", sfai_feast),
          
          (store_current_hours, ":hours_at_current_state"),
          (faction_get_slot, ":current_state_started", ":faction_no", slot_faction_ai_current_state_started),
          (val_sub, ":hours_at_current_state", ":current_state_started"),
          (ge, ":hours_at_current_state", 18), #Must have at least 18 hours to reset
          
          (store_current_hours, ":hours"),
          (faction_set_slot, ":faction_no", slot_faction_ai_last_rest_time, ":hours"),
        (try_end),
    ]),
    
    # script_check_and_finish_active_army_quests_for_faction
    # Input: faction_no
    # Output: none
    ("check_and_finish_active_army_quests_for_faction",
      [
        (store_script_param_1, ":faction_no"),
        (try_begin),
          (eq, "$players_kingdom", ":faction_no"),
          (try_begin),
            (check_quest_active, "qst_report_to_army"),
            (call_script, "script_cancel_quest", "qst_report_to_army"),
          (try_end),
          (assign, ":one_active", 0),
          (try_for_range, ":quest_no", army_quests_begin, army_quests_end),
            (check_quest_active, ":quest_no"),
            (call_script, "script_cancel_quest", ":quest_no"),
            (troop_get_slot, ":army_quest_giver_troop", ":quest_no", slot_quest_giver_troop),
            (assign, ":one_active", 1),
          (try_end),
          (try_begin),
            (check_quest_active, "qst_follow_army"),
            (assign, ":one_active", 1),
            (troop_get_slot, ":army_quest_giver_troop", "qst_follow_army", slot_quest_giver_troop),
            (call_script, "script_end_quest", "qst_follow_army"),
          (try_end),
          (eq, ":one_active", 1),
          (faction_get_slot, ":last_offensive_time", ":faction_no", slot_faction_last_offensive_concluded), ##1.132
          #       (faction_get_slot, ":last_offensive_time", ":faction_no", slot_faction_ai_last_offensive_time), ##1.131
          (store_current_hours, ":cur_hours"),
          (store_sub, ":total_time_served", ":cur_hours", ":last_offensive_time"),
          (store_mul, ":xp_reward", ":total_time_served", 5),
          (val_div, ":xp_reward", 50),
          (val_mul, ":xp_reward", 50),
          (val_add, ":xp_reward", 50),
          (add_xp_as_reward, ":xp_reward"),
          (call_script, "script_troop_change_relation_with_troop", "trp_player", ":army_quest_giver_troop", 2),
        (try_end),
    ]),
    
    # script_troop_get_player_relation
    # Input: arg1 = troop_no
    # Output: reg0 = effective relation (modified by troop reputation, honor, etc.)
    ("troop_get_player_relation",
      [
        (store_script_param_1, ":troop_no"),
        (troop_get_slot, ":reputation", ":troop_no", slot_lord_reputation_type),
        (troop_get_slot, ":effective_relation", ":troop_no", slot_troop_player_relation),
        (assign, ":honor_bonus", 0),
        (try_begin),
          (eq,  ":reputation", lrep_quarrelsome),
          (val_add, ":effective_relation", -3),
        (try_end),
        (try_begin),
          (ge, "$player_honor", 0),
          (try_begin),
            (this_or_next|eq,  ":reputation", lrep_upstanding),
            (             eq,  ":reputation", lrep_goodnatured),
             (store_div, ":honor_bonus", "$player_honor", 3),
		  ##diplomacy start+
		  (else_try),
			#In general this should not apply to ladies, as they operate by different
			#reputation rules, but if a "kingdom lady" has become a "kingdom hero" instead,
			#it should apply.
		     (eq,  ":reputation", lrep_moralist),#-- verify that the lady is effectively a lord:
		     (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			 (store_div, ":honor_bonus", "$player_honor", 3),
		  (else_try),
			 #Personality type that values keeping your word
			 (call_script, "script_dplmc_get_troop_morality_value", ":troop_no", tmt_honest),
			 (ge, reg0, 1),
			 (store_div, ":honor_bonus", "$player_honor", 3),
		  ##diplomacy end+
          (try_end),
        (try_end),
        (try_begin),
          (lt, "$player_honor", 0),
          (try_begin),
            (this_or_next|eq,  ":reputation", lrep_upstanding),
            (             eq,  ":reputation", lrep_goodnatured),
            (store_div, ":honor_bonus", "$player_honor", 3),
          ##diplomacy start+
		  (else_try),
			(call_script, "script_dplmc_get_troop_morality_value", ":troop_no", tmt_honest),
			(ge, reg0, 1),#Personality type that values keeping your word
			(store_div, ":honor_bonus", "$player_honor", 3),
		  (else_try),
		  	 #"My kind of scum" - a few rare individuals might actively approve.
		  	 (lt, reg0, 0),#<-- must have negative value for tmt_honest; by default this is only Rolf.
		  	 (this_or_next|eq, ":reputation", lrep_roguish),
		  	 (this_or_next|eq, ":reputation", lrep_custodian),
		  	 (this_or_next|eq, ":reputation", lrep_debauched),
		  	 (this_or_next|eq, ":reputation", lrep_ambitious),
		  		(eq, ":reputation", lrep_cunning),
		  	 (store_div, ":honor_bonus", "$player_honor", -5),
		  	 (val_clamp, ":honor_bonus", 1, 6),
          (else_try),
			#"Honorable" lords can be awful people, so no bonus with benefactors,
			#but dishonorable lords are *guaranteed* to be awful.
            (eq, ":reputation", lrep_benefactor),
            (store_div, ":honor_bonus", "$player_honor", 5),
		  (else_try),
			#Self-righteous lords are moralizing but hypocritical.
			(eq, ":reputation", lrep_selfrighteous),
			(store_div, ":honor_bonus", "$player_honor", 5),
		  (else_try),
			 #In general this should not apply to ladies, as they operate by different
			 #reputation rules, but if a "kingdom lady" has become a "kingdom hero" instead,
			 #it should apply.
			 (eq,  ":reputation", lrep_moralist),#-- verify that the lady is effectively a lord:
		     (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			 (store_div, ":honor_bonus", "$player_honor", 3),
		  (else_try),
			 (eq,  ":reputation", lrep_conventional),#-- verify that the lady is effectively a lord:
		     (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			 (store_div, ":honor_bonus", "$player_honor", 5),
          ##diplomacy end+
          (else_try),
            (eq,  ":reputation", lrep_martial),
            (store_div, ":honor_bonus", "$player_honor", 5),
          (try_end),
        (try_end),
        (val_add, ":effective_relation", ":honor_bonus"),
        (val_clamp, ":effective_relation", -100, 101),
        (assign, reg0, ":effective_relation"),
    ]),
    
    # script_change_troop_renown
    # Input: arg1 = troop_no, arg2 = relation difference
    # Output: none
    ("change_troop_renown",
      [
        (store_script_param_1, ":troop_no"),
        (store_script_param_2, ":renown_change"),
        
        (troop_get_slot, ":old_renown", ":troop_no", slot_troop_renown),
        
        (try_begin),
          (gt, ":renown_change", 0),
          (assign, reg4, ":renown_change"),
          
          (store_div, ":subtraction", ":old_renown", 200),
          (val_sub, ":renown_change", ":subtraction"),
          (val_max, ":renown_change", 0),
          
          (eq, ":troop_no", "trp_player"),
          (assign, reg5, ":renown_change"),
          
          (eq, "$cheat_mode", 1),
          (display_message, "str_renown_change_of_reg4_reduced_to_reg5_because_of_high_existing_renown"),
        (try_end),
        
        (store_add, ":new_renown", ":old_renown", ":renown_change"),
        (val_max, ":new_renown", 0),
        (troop_set_slot, ":troop_no", slot_troop_renown, ":new_renown"),
        
        (try_begin),
          (eq, ":troop_no", "trp_player"),

		(try_begin),															#	1.143 Port // Newly Added
		  (ge, ":new_renown", 50),

          (try_begin),																
            (troop_get_type, ":is_female", "trp_player"),
            (eq, ":is_female", 1),
            (unlock_achievement, ACHIEVEMENT_TALK_OF_THE_TOWN),
          (try_end),
		(try_end),																#	End
		
          (str_store_troop_name, s1, ":troop_no"),
          (assign, reg12, ":renown_change"),
          (val_abs, reg12),
          (try_begin),
            (gt, ":renown_change", 0),
            (display_message, "@You gained {reg12} renown.", 0x33ff33), ## CC
          (else_try),
            (lt, ":renown_change", 0),
            (display_message, "@You lose {reg12} renown.", 0xff3333), ## CC
          (try_end),
        (try_end),
        (call_script, "script_update_troop_notes", ":troop_no"),
    ]),
    
    
    # script_change_player_relation_with_troop
    # Input: arg1 = troop_no, arg2 = relation difference
    # Output: none
    ("change_player_relation_with_troop",
      [
        (store_script_param_1, ":troop_no"),
        (store_script_param_2, ":difference"),
        
        (try_begin),
          (neq, ":troop_no", "trp_player"),
          (neg|is_between, ":troop_no", soldiers_begin, soldiers_end),
			##diplomacy start+
		  (neq, ":troop_no", "trp_kingdom_heroes_including_player_begin"),
		  #(neq, ":troop_no", -1),#OLD
		  (ge, ":troop_no", 1),#NEW
			##diplomacy end+
          (neq, ":difference", 0),
          (call_script, "script_troop_get_player_relation", ":troop_no"),
          (assign, ":old_effective_relation", reg0),
          (troop_get_slot, ":player_relation", ":troop_no", slot_troop_player_relation),
          (val_add, ":player_relation", ":difference"),
          (val_clamp, ":player_relation", -100, 101),
          (try_begin),
            (troop_set_slot, ":troop_no", slot_troop_player_relation, ":player_relation"),
            
            (try_begin),
              (le, ":player_relation", -50),
              (unlock_achievement, ACHIEVEMENT_OLD_DIRTY_SCOUNDREL),
            (try_end),
            
            (str_store_troop_name_link, s1, ":troop_no"),
            (call_script, "script_troop_get_player_relation", ":troop_no"),
            (assign, ":new_effective_relation", reg0),
            (neq, ":old_effective_relation", ":new_effective_relation"),
            (assign, reg1, ":old_effective_relation"),
            (assign, reg2, ":new_effective_relation"),
            #LAZERAS MODIFIED  {ENTK}
            # Jrider + TITLES v0.3.2 update both player and troop titles
            (try_begin),
              (store_troop_faction, ":troop_faction", ":troop_no"),
              (eq, ":troop_faction", "$players_kingdom"),
              (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", "trp_player", "$players_kingdom"),
              (call_script, "script_troop_set_title_according_to_faction", ":troop_no", "$players_kingdom"),
            (try_end),
            # Jrider -
            #LAZERAS MODIFIED  {ENTK}
          (try_begin),
			##diplomacy start+ Suppress this message for dead people except in cheat mode
            (lt, "$cheat_mode", 1),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_dead),
			(neq, ":troop_no", "$g_talk_troop"),
		  (else_try),
		  ##diplomacy end+
              (gt, ":difference", 0),
              (display_message, "str_troop_relation_increased", 0x33ff33), ## CC
            (else_try),
              (lt, ":difference", 0),
              (display_message, "str_troop_relation_detoriated", 0xff3333), ## CC
            (try_end),
            (try_begin),
              (eq, ":troop_no", "$g_talk_troop"),
              (assign, "$g_talk_troop_relation", ":new_effective_relation"),
              (call_script, "script_setup_talk_info"),
            (try_end),
            (call_script, "script_update_troop_notes", ":troop_no"),
          (try_end),
        (try_end),
    ]),
    
    # script_change_player_relation_with_center
    # Input: arg1 = party_no, arg2 = relation difference
    # Output: none
    ("change_player_relation_with_center",
      [
        (store_script_param_1, ":center_no"),
        (store_script_param_2, ":difference"),
        
        (party_get_slot, ":player_relation", ":center_no", slot_center_player_relation),
        (assign, reg1, ":player_relation"),
        (val_add, ":player_relation", ":difference"),
        (val_clamp, ":player_relation", -100, 100),
        (assign, reg2, ":player_relation"),
        (party_set_slot, ":center_no", slot_center_player_relation, ":player_relation"),
        
        (try_begin),
          (le, ":player_relation", -50),
          (unlock_achievement, ACHIEVEMENT_OLD_DIRTY_SCOUNDREL),
        (try_end),
        
        
        (str_store_party_name_link, s1, ":center_no"),
        (try_begin),
          (gt, ":difference", 0),
          (display_message, "@Your relation with {s1} has improved.", 0x33ff33), ## CC
        (else_try),
          (lt, ":difference", 0),
          (display_message, "@Your relation with {s1} has deteriorated.", 0xff3333), ## CC
        (try_end),
        (try_begin),
          (party_slot_eq, ":center_no", slot_party_type, spt_village),
          (call_script, "script_update_volunteer_troops_in_village", ":center_no"),
        (try_end),
        
        (try_begin),
          (this_or_next|is_between, "$g_talk_troop", village_elders_begin, village_elders_end),
          (is_between, "$g_talk_troop", mayors_begin, mayors_end),
		 ##diplomacy start+
		  #Fix potential bug: don't adjust relations except with *that* center's
		  #mayor.
		  (party_slot_eq, ":center_no", slot_town_elder, "$g_talk_troop"),
	      ##diplomacy end+
          (assign, "$g_talk_troop_relation", ":player_relation"),
          (call_script, "script_setup_talk_info"),
        (try_end),
    ]),
    
    
    # script_change_player_relation_with_faction
    # Input: arg1 = faction_no, arg2 = relation difference
    # Output: none
    ("change_player_relation_with_faction",
      [
        (store_script_param_1, ":faction_no"),
        (store_script_param_2, ":difference"),
        
        (store_relation, ":player_relation", ":faction_no", "fac_player_supporters_faction"),
        (assign, reg1, ":player_relation"),
        (val_add, ":player_relation", ":difference"),
        (assign, reg2, ":player_relation"),
        (set_relation, ":faction_no", "fac_player_faction", ":player_relation"),
        (set_relation, ":faction_no", "fac_player_supporters_faction", ":player_relation"),
        
        (try_begin),
          (le, ":player_relation", -50),
          (unlock_achievement, ACHIEVEMENT_OLD_DIRTY_SCOUNDREL),
        (try_end),
        
        
        (str_store_faction_name_link, s1, ":faction_no"),
        (try_begin),
          (gt, ":difference", 0),
          (display_message, "str_faction_relation_increased", 0x33ff33), ## CC
        (else_try),
          (lt, ":difference", 0),
          (display_message, "str_faction_relation_detoriated", 0xff3333), ## CC
        (try_end),
        (call_script, "script_update_all_notes"),
    ]),
    
    # script_set_player_relation_with_faction
    # Input: arg1 = faction_no, arg2 = relation
    # Output: none
    ("set_player_relation_with_faction",
      [
        (store_script_param_1, ":faction_no"),
        (store_script_param_2, ":relation"),
        
        (store_relation, ":player_relation", ":faction_no", "fac_player_supporters_faction"),
        (store_sub, ":reln_dif", ":relation", ":player_relation"),
        (call_script, "script_change_player_relation_with_faction", ":faction_no", ":reln_dif"),
    ]),
    
    
    
    # script_change_player_relation_with_faction_ex
    # changes relations with other factions also (according to their relations between each other)
    # Input: arg1 = faction_no, arg2 = relation difference
    # Output: none
    ("change_player_relation_with_faction_ex", #Floris Marker
      [
        (store_script_param_1, ":faction_no"),
        (store_script_param_2, ":difference"),
        
        (store_relation, ":player_relation", ":faction_no", "fac_player_supporters_faction"),
        (assign, reg1, ":player_relation"),
        (val_add, ":player_relation", ":difference"),
        (assign, reg2, ":player_relation"),
        (set_relation, ":faction_no", "fac_player_faction", ":player_relation"),
        (set_relation, ":faction_no", "fac_player_supporters_faction", ":player_relation"),
        
        (str_store_faction_name_link, s1, ":faction_no"),
        (try_begin),
          (gt, ":difference", 0),
          (display_message, "str_faction_relation_increased", 0x33ff33), ## CC
        (else_try),
          (lt, ":difference", 0),
          (display_message, "str_faction_relation_detoriated", 0xff3333), ## CC
        (try_end),
        
        (try_for_range, ":other_faction", kingdoms_begin, kingdoms_end),
          (faction_slot_eq, ":other_faction", slot_faction_state, sfs_active),
          (neq, ":faction_no", ":other_faction"),
          (store_relation, ":other_faction_relation", ":faction_no", ":other_faction"),
          (store_relation, ":player_relation", ":other_faction", "fac_player_supporters_faction"),
          (store_mul, ":relation_change", ":difference", ":other_faction_relation"),
          (val_div, ":relation_change", 100),
          (val_add, ":player_relation", ":relation_change"),
        ##diplomacy start
        (try_begin),
            (store_add, ":truce_slot", "fac_player_supporters_faction", slot_faction_truce_days_with_factions_begin),
  		    (val_sub, ":truce_slot", kingdoms_begin),
  		    (faction_get_slot, ":truce_days", ":other_faction", ":truce_slot"),
			##nested diplomacy start+ Changed "eq 0", to "le 0", since now negative truce days track war length
            (this_or_next|le, ":truce_days", 0), #other faction only affected if no truce
			##nested diplomacy end+
            (gt, ":difference", 0), #or change > 0
            (store_relation, ":cur_relation", ":other_faction", "fac_player_supporters_faction"),

            #display relation change message
            (store_sub,  ":relation_change", ":player_relation", ":cur_relation"),
            (str_store_faction_name_link, s1, ":other_faction"),
            (assign, reg1, ":cur_relation"),
            (assign, reg2, ":player_relation"),
            (try_begin),
              (gt, ":relation_change", 0),
              (display_message, "str_faction_relation_increased"),
            (else_try),
              (lt, ":relation_change", 0),
              (display_message, "str_faction_relation_detoriated"),
            (try_end),
            
            #display war declaration
            (try_begin),
                (ge, ":cur_relation", 0), #old relation > 0 -> peace
                (lt, ":player_relation", 0), #new relation < 0 -> war
                ##nested diplomacy start+
                #This is the source of the "fake war" bug.  I think this should get rid of it:
                (try_begin),
                    (this_or_next|eq, "$players_kingdom", "fac_player_faction"),
                       (eq, "$players_kingdom", "fac_player_supporters_faction"),
                ##nested diplomacy end+
                (call_script, "script_add_notification_menu", "mnu_notification_war_declared", ":other_faction", "$players_kingdom"),
                ##nested diplomacy start+
				(else_try),
					(is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
					(store_relation, ":players_kingdom_relation", ":other_faction", "$players_kingdom"),
					(lt, ":players_kingdom_relation", 0),
					(call_script, "script_add_notification_menu", "mnu_notification_war_declared", ":other_faction", "$players_kingdom"),
				(else_try),
					#Display some sort of message so you know something happened
				    (display_message, "@{!} There is widespread ill-will towards you in the {s1}."),
                (try_end),
                ##nested diplomacy end+
            (try_end),
        ##diplomacy end
        (set_relation, ":other_faction", "fac_player_faction", ":player_relation"),
        (set_relation, ":other_faction", "fac_player_supporters_faction", ":player_relation"),
        ##diplomacy begin
        (try_end),
        ##diplomacy end
      (try_end),
      (try_begin),
        (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
        (try_for_range, ":kingdom_no", kingdoms_begin, kingdoms_end),
          (faction_slot_eq, ":kingdom_no", slot_faction_state, sfs_active),
          (call_script, "script_update_faction_notes", ":kingdom_no"),
        (try_end),
      (try_end),
  ]),
    
    # script_cf_get_random_active_faction_except_player_faction_and_faction
    # Input: arg1 = except_faction_no
    # Output: reg0 = random_faction
    ("cf_get_random_active_faction_except_player_faction_and_faction",
      [
        (store_script_param_1, ":except_faction_no"),
        (assign, ":num_factions", 0),
        (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
          (neq, ":faction_no", "fac_player_supporters_faction"),
          (neq, ":faction_no", ":except_faction_no"),
          (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
          (val_add, ":num_factions", 1),
        (try_end),
        (gt, ":num_factions", 0),
        (assign, ":selected_faction", -1),
        (store_random_in_range, ":random_faction", 0, ":num_factions"),
        (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
          (ge, ":random_faction", 0),
          (neq, ":faction_no", "fac_player_supporters_faction"),
          (neq, ":faction_no", ":except_faction_no"),
          (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
          (val_sub, ":random_faction", 1),
          (lt, ":random_faction", 0),
          (assign, ":selected_faction", ":faction_no"),
        (try_end),
        (assign, reg0, ":selected_faction"),
    ]),
    
    # script_make_kingdom_hostile_to_player
    # Input: arg1 = faction_no, arg2 = relation difference
    # Output: none
    ("make_kingdom_hostile_to_player",
      [
        (store_script_param_1, ":kingdom_no"),
        (store_script_param_2, ":difference"),
        
        (try_begin),
          (lt, ":difference", 0),
          (store_relation, ":player_relation", ":kingdom_no", "fac_player_supporters_faction"),
          (val_min, ":player_relation", 0),
          (val_add, ":player_relation", ":difference"),
          (call_script, "script_set_player_relation_with_faction", ":kingdom_no", ":player_relation"),
        (try_end),
    ]),
    
    # script_change_player_honor
    # Input: arg1 = honor difference
    # Output: none
    ("change_player_honor",
      [
		  (store_script_param_1, ":honor_dif"),
		  ##diplomacy start+
		  #Exacerbate the effect of honor losses as the player's honor increases
		  (try_begin),
			 (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),#<-- experimental settings must be enabled
			 (ge, "$player_honor", 10),
			 (lt, ":honor_dif", 0),
			 (store_add, ":honor_multiplier", "$player_honor", 100),
			 (val_mul, ":honor_dif", ":honor_multiplier"),
			 (val_sub, ":honor_dif", 50),
			 (val_div, ":honor_dif", 100),
		  (try_end),
		  ##diplomacy end+
        (val_add, "$player_honor", ":honor_dif"),
        (try_begin),
          (gt, ":honor_dif", 0),
          (display_message, "@You gain honour.", 0x33ff33), ## CC
        (else_try),
          (lt, ":honor_dif", 0),
          (display_message, "@You lose honour.", 0xff3333), ## CC
        (try_end),
    ]),
    
    # script_change_player_party_morale
    # Input: arg1 = morale difference
    # Output: none
    ("change_player_party_morale",
      [
        (store_script_param_1, ":morale_dif"),
        (party_get_morale, ":cur_morale", "p_main_party"),
        (val_clamp, ":cur_morale", 0, 100),
        
        (store_add, ":new_morale", ":cur_morale", ":morale_dif"),
        (val_clamp, ":new_morale", 0, 100),
        
        (party_set_morale, "p_main_party", ":new_morale"),
        (try_begin),
          (lt, ":new_morale", ":cur_morale"),
          (store_sub, reg1, ":cur_morale", ":new_morale"),
          (display_message, "str_party_lost_morale", 0xff3333), ## CC
        (else_try),
          (gt, ":new_morale", ":cur_morale"),
          (store_sub, reg1, ":new_morale", ":cur_morale"),
          (display_message, "str_party_gained_morale", 0x33ff33), ## CC
        (try_end),
    ]),
    
    # script_cf_player_has_item_without_modifier
    # Input: arg1 = item_id, arg2 = modifier
    # Output: none (can_fail)
    ("cf_player_has_item_without_modifier",
      [
        (store_script_param, ":item_id", 1),
        (store_script_param, ":modifier", 2),
        (player_has_item, ":item_id"),
        #checking if any of the meat is not rotten
        (assign, ":has_without_modifier", 0),
        (troop_get_inventory_capacity, ":inv_size", "trp_player"),
        (try_for_range, ":i_slot", 0, ":inv_size"),
          (troop_get_inventory_slot, ":cur_item", "trp_player", ":i_slot"),
          (eq, ":cur_item", ":item_id"),
          (troop_get_inventory_slot_modifier, ":cur_modifier", "trp_player", ":i_slot"),
          (neq, ":cur_modifier", ":modifier"),
          (assign, ":has_without_modifier", 1),

########################################################################################################################
# LAV MODIFICATIONS START (TRADE GOODS MOD)
########################################################################################################################
		  (assign, reg0, ":cur_modifier"),
########################################################################################################################
# LAV MODIFICATIONS END (TRADE GOODS MOD)
########################################################################################################################

          (assign, ":inv_size", 0), #break
        (try_end),
        (eq, ":has_without_modifier", 1),
    ]),
    
    # script_get_player_party_morale_values
    # Output: reg0 = player_party_morale_target
    ("get_player_party_morale_values",
      [
        #LAZERAS MODIFIED  {Troop morale based on quality}
        # calculate the total number of guys and the cumulative level of the
        # party.
        (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
        (assign, ":level_total",1),
        (assign, ":num_men", 1),
        (assign, ":num_companions",0), #Tempered added for companions positive adjustment to morale
        (try_for_range, ":i_stack", 1, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop","p_main_party", ":i_stack"),
          (store_character_level, ":level", ":stack_troop"),
          (try_begin),
            (troop_is_hero, ":stack_troop"),
            (val_add, ":num_men", 1), #it was 3 in "Mount&Blade", now it is 1 in Warband
            (val_add, ":num_companions",1), #Tempered added for companions positive adjustment to morale
            (val_add, ":level_total", ":level"),
          (else_try),
            (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
            (val_add, ":num_men", ":stack_size"),
            (val_mul, ":level", ":stack_size"),
            (val_add, ":level_total", ":level"),
          (try_end),
        (try_end),
        
        # take the total number of guys and put it in the right range to do more
        # maths on it.  divide this value by the cumulative level to get our
        # morale penalty based on size.  this results in lower level troops
        # being more inclined to be unhappy than higher level troops and higher
        # level troops can kick guys in line up to a point.
        # 5 * (count+5)^2 / (count * level)
        (store_add, ":morale_penalty_for_size", ":num_men", 5),
        (val_mul, ":morale_penalty_for_size", ":morale_penalty_for_size"),
        (val_mul, ":morale_penalty_for_size", 5),
        (val_div, ":morale_penalty_for_size", ":level_total"),
        
        # the math works great for large numbers but not so great for small ones.
        # if we get a value that's more than twice the size, min it to that.
        (try_begin),
          (store_mul, ":double", ":num_men", 2),
          (gt, ":morale_penalty_for_size", ":double"),
          (assign, ":morale_penalty_for_size", ":double"),
        (try_end),
        
        (val_mul,":num_companions", 4),   #Tempered added for companions positive adjustment to morale
        (assign, "$g_player_party_morale_modifier_party_size", ":morale_penalty_for_size"),
        #LAZERAS MODIFIED  {Troop morale based on quality}
        
        (store_skill_level, ":player_leadership", "skl_leadership", "trp_player"),
        
        (try_begin),
          (eq, "$players_kingdom", "fac_player_supporters_faction"),
          (faction_get_slot, ":cur_faction_king", "$players_kingdom", slot_faction_leader),
          (eq, ":cur_faction_king", "trp_player"),
          (store_mul, "$g_player_party_morale_modifier_leadership", ":player_leadership", 15),
        (else_try),
          (store_mul, "$g_player_party_morale_modifier_leadership", ":player_leadership", 12),
        (try_end),
        
        (assign, ":new_morale", "$g_player_party_morale_modifier_leadership"),
        (val_sub, ":new_morale", "$g_player_party_morale_modifier_party_size"),
        
        (val_add, ":new_morale", 50),
        (val_add, ":new_morale", ":num_companions"), #Tempered added for companions positive adjustment to morale
        
        ## CC 1.322, replaced some native lines and some CC 1.321 and earlier additions by new lines.
        (assign, ":kinds_of_food", 0),
        (assign, "$g_player_party_morale_modifier_food", 0),
        (try_for_range, ":cur_edible", food_begin, food_end),
          (call_script, "script_cf_player_has_item_without_modifier", ":cur_edible", imod_rotten),
          (item_get_slot, ":food_bonus", ":cur_edible", slot_item_food_bonus),
          (store_add, ":food_bonus_multi", "$g_twice_consum_food", 1),
          (val_mul, ":food_bonus", ":food_bonus_multi"),
        
########################################################################################################################
# LAV MODIFICATIONS START (TRADE GOODS MOD)
########################################################################################################################
        (try_begin),
          (eq, reg0, imod_cheap),
          (val_sub, ":food_bonus", 2),
        (else_try),
          (eq, reg0, imod_fine),
          (val_add, ":food_bonus", 1),
        (else_try),
          (eq, reg0, imod_well_made),
          (val_add, ":food_bonus", 2),
        (else_try),
          (eq, reg0, imod_strong),
          (val_add, ":food_bonus", 3),
        (else_try),
          (eq, reg0, imod_lordly),
          (val_add, ":food_bonus", 5),
        (else_try),
          (eq, reg0, imod_exquisite),
          (val_add, ":food_bonus", 6),
        (try_end),
########################################################################################################################
# LAV MODIFICATIONS END (TRADE GOODS MOD)
########################################################################################################################

          (val_mul, ":food_bonus", 3),
          (val_div, ":food_bonus", 2),
          (val_add, "$g_player_party_morale_modifier_food", ":food_bonus"),
          (val_add, ":kinds_of_food", 1),
        (try_end),
        (store_sub, ":total_kinds_of_food", food_end, food_begin),
        (val_add, ":kinds_of_food", ":total_kinds_of_food"),
        (val_mul, "$g_player_party_morale_modifier_food", ":kinds_of_food"),
        (val_div, "$g_player_party_morale_modifier_food", ":total_kinds_of_food"),
        (val_add, ":new_morale", "$g_player_party_morale_modifier_food"),
        ## CC
        
        (try_begin),
          (eq, "$g_player_party_morale_modifier_food", 0),
          (assign, "$g_player_party_morale_modifier_no_food", 30),
          (val_sub, ":new_morale", "$g_player_party_morale_modifier_no_food"),
        (else_try),
          (assign, "$g_player_party_morale_modifier_no_food", 0),
        (try_end),
        
        (assign, "$g_player_party_morale_modifier_debt", 0),
        (try_begin),
          (gt, "$g_player_debt_to_party_members", 0),
          (call_script, "script_calculate_player_faction_wage"),
          (assign, ":total_wages", reg0),
          (store_mul, "$g_player_party_morale_modifier_debt", "$g_player_debt_to_party_members", 10),
          (val_max, ":total_wages", 1),
          (val_div, "$g_player_party_morale_modifier_debt", ":total_wages"),
          (val_clamp, "$g_player_party_morale_modifier_debt", 1, 31),
          (val_sub, ":new_morale", "$g_player_party_morale_modifier_debt"),
        (try_end),
        ## CC
        (assign, reg1, ":new_morale"),
        ## CC
        (val_clamp, ":new_morale", 0, 100),
        (assign, reg0, ":new_morale"),
    ]),
    
    # script_diplomacy_start_war_between_kingdoms
    # Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
    # Output: none
    ("diplomacy_start_war_between_kingdoms", #sets relations between two kingdoms and their vassals.
      [
        (store_script_param, ":kingdom_a", 1),
        (store_script_param, ":kingdom_b", 2),
        (store_script_param, ":initializing_war_peace_cond", 3), #1 = after start of game
        
        (call_script, "script_npc_decision_checklist_peace_or_war", ":kingdom_a", ":kingdom_b", -1),
        (assign, ":explainer_string", reg1),
        
        #
        ##diplomacy begin
        (try_begin),
          (lt, ":initializing_war_peace_cond", 2),
          ##diplomacy end
          (try_begin),
            (eq, ":kingdom_a", "fac_player_supporters_faction"),
            (assign, ":war_event", logent_player_faction_declares_war),
          (else_try),
            (eq, ":explainer_string", "str_s12s15_declared_war_to_control_calradia"),
            (assign, ":war_event", logent_player_faction_declares_war), #for savegame compatibility, this event stands in for the attempt to declare war on all of calradia
          (else_try),
            (eq, ":explainer_string", "str_s12s15_considers_s16_to_be_dangerous_and_untrustworthy_and_shehe_wants_to_bring_s16_down"),
            (assign, ":war_event", logent_faction_declares_war_out_of_personal_enmity),
          (else_try),
            (eq, ":explainer_string", "str_s12s15_is_anxious_to_reclaim_old_lands_such_as_s18_now_held_by_s16"),
            (assign, ":war_event", logent_faction_declares_war_to_regain_territory),
          (else_try),
            (eq, ":explainer_string", "str_s12s15_faces_too_much_internal_discontent_to_feel_comfortable_ignoring_recent_provocations_by_s16s_subjects"),
            (assign, ":war_event", logent_faction_declares_war_to_respond_to_provocation),
          (else_try),
            (eq, ":explainer_string", "str_s12s15_is_alarmed_by_the_growing_power_of_s16"),
            (assign, ":war_event", logent_faction_declares_war_to_curb_power),
          (try_end),
          (call_script, "script_add_log_entry", ":war_event", ":kingdom_a", 0, 0, ":kingdom_b"),
          
          
          
          (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":kingdom_a", ":kingdom_b"),
          (assign, ":current_diplomatic_status", reg0),
          (try_begin), #effects of policy only after the start of the game
            (eq, ":initializing_war_peace_cond", 1),
            (eq, ":current_diplomatic_status", -1),
            (call_script, "script_faction_follows_controversial_policy", ":kingdom_a", logent_policy_ruler_declares_war_with_justification),
          (else_try),
            (eq, ":initializing_war_peace_cond", 1),
            (eq, ":current_diplomatic_status", 0),
            (call_script, "script_faction_follows_controversial_policy", ":kingdom_a", logent_policy_ruler_attacks_without_provocation),
          (else_try),
            (eq, ":current_diplomatic_status", 1),
            (call_script, "script_faction_follows_controversial_policy", ":kingdom_a", logent_policy_ruler_breaks_truce),
          (try_end),
          ##diplomacy begin
        (else_try),
          (assign, ":war_event", logent_faction_declares_war_to_fulfil_pact),
          (call_script, "script_faction_follows_controversial_policy", ":kingdom_a", logent_policy_ruler_declares_war_with_justification),
          (assign, ":initializing_war_peace_cond", 1),
        (try_end),
        ##diplomacy end
        
        (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
        (val_min, ":relation", -10),
        (val_add, ":relation", -30),
        (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
        
        (try_begin),
          (eq, "$players_kingdom", ":kingdom_a"),
          (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
          (val_min, ":relation", -30),
          (call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
        (else_try),
          (eq, "$players_kingdom", ":kingdom_b"),
          (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
          (val_min, ":relation", -30),
          (call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
        (try_end),
        
        (try_begin),
          (eq, ":initializing_war_peace_cond", 1),
          
          #Remove this -- this scrambles who declares war on whom
          #        (try_begin),
          #         (store_random_in_range, ":random_no", 0, 2),
          #        (this_or_next|eq, ":kingdom_a", "fac_player_supporters_faction"),
          #		(eq, ":random_no", 0),
          #     (assign, ":local_temp", ":kingdom_a"),
          #    (assign, ":kingdom_a", ":kingdom_b"),
          #   (assign, ":kingdom_b", ":local_temp"),
          #(try_end),
          
          (str_store_faction_name_link, s1, ":kingdom_a"),
          (str_store_faction_name_link, s2, ":kingdom_b"),
          (display_log_message, "@{s1} has declared war against {s2}."),
          
          (store_current_hours, ":hours"),
          (faction_set_slot, ":kingdom_a", slot_faction_ai_last_decisive_event, ":hours"),
          (faction_set_slot, ":kingdom_b", slot_faction_ai_last_decisive_event, ":hours"),
          
          #set provocation and truce days
          (store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
          (store_add, ":provocation_slot", ":kingdom_b", slot_faction_provocation_days_with_factions_begin),
          (val_sub, ":truce_slot", kingdoms_begin),
          (val_sub, ":provocation_slot", kingdoms_begin),
          (faction_set_slot, ":kingdom_a", ":truce_slot", 0),
          (faction_set_slot, ":kingdom_a", ":provocation_slot", 0),
          
          (store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
          (store_add, ":provocation_slot", ":kingdom_a", slot_faction_provocation_days_with_factions_begin),
          (val_sub, ":truce_slot", kingdoms_begin),
          (val_sub, ":provocation_slot", kingdoms_begin),
          (faction_set_slot, ":kingdom_b", ":truce_slot", 0),
          (faction_set_slot, ":kingdom_b", ":provocation_slot", 0),
          
          (call_script, "script_add_notification_menu", "mnu_notification_war_declared", ":kingdom_a", ":kingdom_b"),
          
          (call_script, "script_update_faction_notes", ":kingdom_a"),
          (call_script, "script_update_faction_notes", ":kingdom_b"),
          (assign, "$g_recalculate_ais", 1),
        (try_end),
        
        (try_begin),
          (check_quest_active, "qst_cause_provocation"),
          (neg|check_quest_succeeded, "qst_cause_provocation"),
          (this_or_next|eq, "$players_kingdom", ":kingdom_a"),
          (eq, "$players_kingdom", ":kingdom_b"),
          (call_script, "script_abort_quest", "qst_cause_provocation", 0),
        (try_end),
        ##diplomacy begin
        #check for defensive
        (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
          (neq, ":cur_kingdom", ":kingdom_a"),
          (neq, ":cur_kingdom", ":kingdom_b"),
          
          (store_relation, ":cur_relation", ":cur_kingdom", ":kingdom_a"),
          (ge, ":cur_relation", 0), #AT PEACE
          
		  (store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_get_slot, ":truce_days", ":cur_kingdom", ":truce_slot"),
			##nested diplomacy start+ replace "40" with a named constant
			#(gt, ":truce_days", 40),
			(gt, ":truce_days", dplmc_treaty_defense_days_expire),
			##nested diplomacy end+
			(try_begin),
			  (lt, ":initializing_war_peace_cond", 2), #only if war was not caused by defensive or alliance pact
			  (call_script, "script_diplomacy_start_war_between_kingdoms", ":cur_kingdom", ":kingdom_a", 2),
			(try_end),
		(try_end),

		#check for alliance
		(try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
		  (neq, ":cur_kingdom", ":kingdom_a"),
		  (neq, ":cur_kingdom", ":kingdom_b"),

		  (store_relation, ":cur_relation", ":cur_kingdom", ":kingdom_b"),
				(ge, ":cur_relation", 0), #AT PEACE

			(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":truce_slot", kingdoms_begin),
			(faction_get_slot, ":truce_days", ":cur_kingdom", ":truce_slot"),
			##nested diplomacy start+ replace "60" with a named constant
			#(gt, ":truce_days", 60),
			(gt, ":truce_days", dplmc_treaty_alliance_days_expire),
			##nested diplomacy end+
			(call_script, "script_diplomacy_start_war_between_kingdoms", ":cur_kingdom", ":kingdom_b", 3),
		(try_end),
		##diplomacy end
	  ]),
    
    
    ("diplomacy_party_attacks_neutral", #called from game_menus (plundering a village, raiding a village),  from dialogs: surprise attacking a neutral lord, any attack on caravan or villagers
      #Has no effect if factions are already at war
      [
        (store_script_param, ":attacker_party", 1),
        (store_script_param, ":defender_party", 2),
        
        (store_faction_of_party, ":attacker_faction", ":attacker_party"),
        (store_faction_of_party, ":defender_faction", ":defender_party"),
        
        (party_stack_get_troop_id, ":attacker_leader", ":attacker_party", 0),
        
        (try_begin),
          (eq, ":attacker_party", "p_main_party"),
          (neq, ":attacker_faction", "fac_player_supporters_faction"),
          (assign, ":attacker_faction", "$players_kingdom"),
        (else_try),
          (eq, ":attacker_party", "p_main_party"),
          (eq, ":attacker_faction", "fac_player_supporters_faction"),
        (try_end),
        
        (try_begin),
          (eq, ":attacker_party", "p_main_party"),
          (store_relation, ":relation", ":attacker_faction", ":defender_faction"),
          (ge, ":relation", 0),
          (call_script, "script_change_player_honor", -2),
        (try_end),
        
        
        (try_begin),
          (check_quest_active, "qst_cause_provocation"),
          (quest_slot_eq, "qst_cause_provocation", slot_quest_target_faction, ":defender_faction"),
          (quest_get_slot, ":giver_troop", "qst_cause_provocation", slot_quest_giver_troop),
          (store_faction_of_troop, ":attacker_faction", ":giver_troop"),
          (call_script, "script_succeed_quest", "qst_cause_provocation"),
        (try_end),
        
        (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":attacker_faction", ":defender_faction"),
        (assign, ":diplomatic_status", reg0),
        
        (try_begin),
          (eq, ":attacker_faction", "fac_player_supporters_faction"),
          (neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
          #player faction inactive, no effect
        (else_try),
          (eq, ":diplomatic_status", -2),
          #war, no effect
        (else_try),
          
          (eq, ":attacker_faction", "fac_player_supporters_faction"),
          (faction_slot_eq, ":attacker_faction", slot_faction_leader, "trp_player"),
          (call_script, "script_faction_follows_controversial_policy", "fac_player_supporters_faction",logent_policy_ruler_attacks_without_provocation),
        (else_try),
          (eq, ":diplomatic_status", 1),
          #truce
		  (party_stack_get_troop_id, ":defender_party_leader", ":defender_party", 0),
		  (try_begin),
			##diplomacy start+ add support for promoted kingdom ladies
			#(i.e. verify not a promoted kingdom lady, since they exist)
			(this_or_next|neg|is_between, ":defender_party_leader", kingdom_ladies_begin, kingdom_ladies_end),
				(neg|troop_slot_eq, ":defender_party_leader", slot_troop_occupation, slto_kingdom_hero),
			##diplomacy end+
			(neg|is_between, ":defender_party_leader", active_npcs_begin, active_npcs_end),
			(store_faction_of_party, ":defender_party_faction", ":defender_party"),
			(faction_get_slot, ":defender_party_leader", ":defender_party_faction", slot_faction_leader),
		   (try_end),
          
          (call_script, "script_add_log_entry", logent_border_incident_troop_breaks_truce, ":attacker_leader", -1, ":defender_party_leader", ":attacker_faction"),
        (else_try),
          #truce
          (call_script, "script_add_log_entry", logent_border_incident_troop_attacks_neutral, ":attacker_leader", -1, ":defender_party_leader", ":attacker_faction"),
        (try_end),
        
        (try_begin),
          (is_between, ":defender_party", villages_begin, villages_end),
          (call_script, "script_add_log_entry", logent_village_raided, ":attacker_leader",  ":defender_party", -1, ":defender_faction"),
        (else_try),
          (party_get_template_id, ":template", ":defender_party"),
          (neq, ":template", "pt_kingdom_hero_party"),
          (try_begin),
            (ge, "$cheat_mode", 1),
            (str_store_faction_name, s5, ":defender_faction"),
            (display_message, "@{!}DEbug - {s5} caravan attacked"),
          (try_end),
          
          (call_script, "script_add_log_entry", logent_caravan_accosted, ":attacker_leader",  -1, -1, ":defender_faction"),
        (try_end),
        
        (store_add, ":slot_truce_days", ":attacker_faction", slot_faction_provocation_days_with_factions_begin),
        (val_sub, ":slot_truce_days", kingdoms_begin),
        (faction_set_slot, ":defender_faction", ":slot_truce_days", 0),
        
        (store_add, ":slot_provocation_days", ":attacker_faction", slot_faction_provocation_days_with_factions_begin),
        (val_sub, ":slot_provocation_days", kingdoms_begin),
        (try_begin),
          (neq, ":diplomatic_status", -2),
          (faction_slot_eq, ":defender_faction", ":slot_provocation_days", 0),
          (faction_set_slot, ":defender_faction", ":slot_provocation_days", 30),
        (try_end),
    ]),
    
    # script_party_calculate_and_set_nearby_friend_enemy_follower_strengths
    # Input: party_no
    # Output: none
    ("party_calculate_and_set_nearby_friend_enemy_follower_strengths",
      [
        (store_script_param, ":party_no", 1),
        (assign, ":follower_strength", 0),
        (assign, ":friend_strength", 0),
        (assign, ":enemy_strength", 0),
      (store_faction_of_party, ":party_faction", ":party_no"),
	  ##diplomacy start+ add support for promoted kingdom ladies
      (store_add, ":end_cond", heroes_end, 1),#<- changed active_npcs to heroes
      (try_for_range, ":iteration", heroes_begin, ":end_cond"),#<- changed active_npcs to heroes
        (try_begin),
          (eq, ":iteration", heroes_end),#<- changed active_npcs to heroes
          (assign, ":cur_troop", "trp_player"),
        (else_try),
          (assign, ":cur_troop", ":iteration"),
        (try_end),
		##diplomacy end+
          
          (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
          (troop_get_slot, ":cur_troop_party", ":cur_troop", slot_troop_leaded_party),
          (ge, ":cur_troop_party", 0),
          (party_is_active, ":cur_troop_party"),
          
          
          #I moved these lines here from (*1) to faster process, ozan.
          (store_troop_faction, ":army_faction", ":cur_troop"),
          (store_relation, ":relation", ":army_faction", ":party_faction"),
          (this_or_next|neq, ":relation", 0),
          (eq, ":army_faction", ":party_faction"),
          #ozan end
          
          
          (neq, ":party_no", ":cur_troop_party"),
          (party_get_slot, ":str", ":cur_troop_party", slot_party_cached_strength),
          (try_begin),
            (neg|is_between, ":party_no", centers_begin, centers_end),
            (party_slot_eq, ":cur_troop_party", slot_party_ai_state, spai_accompanying_army),
            (party_get_slot, ":commander_party", ":cur_troop_party", slot_party_ai_object),
            (eq, ":commander_party", ":party_no"),
            (val_add, ":follower_strength", ":str"),
          (else_try),
            (store_distance_to_party_from_party, ":distance", ":cur_troop_party", ":party_no"),
            (lt, ":distance", 20),
            
            #(*1)
            
            (try_begin),
              (lt, ":distance", 5),
              (assign, ":str_divided", ":str"),
            (else_try),
              (lt, ":distance", 10),
              (store_div, ":str_divided", ":str", 2),
            (else_try),
              (lt, ":distance", 15),
              (store_div, ":str_divided", ":str", 4),
            (else_try),
              (store_div, ":str_divided", ":str", 8),
            (try_end),
            
            (try_begin),
              (this_or_next|eq, ":army_faction", ":party_faction"),
              (gt, ":relation", 0),
              (val_add, ":friend_strength", ":str_divided"),
            (else_try),
              (lt, ":relation", 0),
              (val_add, ":enemy_strength", ":str_divided"),
            (try_end),
          (try_end),
        (try_end),
        
        (party_set_slot, ":party_no", slot_party_follower_strength, ":follower_strength"),
        (party_set_slot, ":party_no", slot_party_nearby_friend_strength, ":friend_strength"),
        (party_set_slot, ":party_no", slot_party_nearby_enemy_strength, ":enemy_strength"),
    ]),
    
  # script_init_ai_calculation
  # Input: none
  # Output: none
  ("init_ai_calculation",
    [
      ##diplomacy start+
	  #(assign, ":real_party_strength"),
	  ##If terrain advantage is enabled, use it to calculate troop strengths.
      (try_begin),
         (eq, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
		 
		 #First update all lords
		 (try_for_range, ":cur_troop", heroes_begin, heroes_end),
            (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
            (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
			(gt, ":cur_party", 0),
            (party_is_active, ":cur_party"),
            
		    (party_get_current_terrain, ":terrain_code", ":cur_party"),
			
			(party_get_attached_to, ":attachment", ":cur_party"),			
			(try_begin),
				(ge, ":attachment", 0),
				(is_between, ":attachment", centers_begin, centers_end),
				(assign, ":terrain_code", dplmc_terrain_code_siege),#siege constant defined in header_terrain_types.py
			(try_end),
			
            (call_script, "script_dplmc_party_calculate_strength_in_terrain", ":cur_party", ":terrain_code", 0, 1), #will update slot_party_cached_strength
         (try_end),
		 
		 #Then update player
		 (party_get_current_terrain, ":terrain_code", "p_main_party"),
		 
		 (party_get_attached_to, ":attachment", "p_main_party"),			
			(try_begin),
				(ge, ":attachment", 0),
				(is_between, ":attachment", centers_begin, centers_end),
				(assign, ":terrain_code", dplmc_terrain_code_siege),#siege constant defined in header_terrain_types.py
			(try_end),
		 
		 (call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_main_party", ":terrain_code", 0, 1), #will update slot_party_cached_strength
		 
         (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
		    #Update with walled center alterations
            (call_script, "script_dplmc_party_calculate_strength_in_terrain", ":cur_center", -2, 0, 1),
         (try_end),
      (else_try),
	   #The old behavior, unchanged:
         (try_for_range, ":cur_troop", heroes_begin, heroes_end),
            (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
            (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
            (party_is_active, ":cur_party"),
            (call_script, "script_party_calculate_strength", ":cur_party", 0), #will update slot_party_cached_strength
         (try_end),
         (call_script, "script_party_calculate_strength", "p_main_party", 0), #will update slot_party_cached_strength
         (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
            (call_script, "script_party_calculate_strength", ":cur_center", 0), #will update slot_party_cached_strength
         (try_end),
      (try_end),
      ##diplomacy end+

      (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
        (call_script, "script_party_calculate_and_set_nearby_friend_enemy_follower_strengths", ":cur_center"),
      (try_end),

      (try_for_range, ":cur_troop", heroes_begin, heroes_end),
        (troop_get_slot, ":cur_troop_party", ":cur_troop", slot_troop_leaded_party),
        (gt, ":cur_troop_party", 0),
        (party_is_active, ":cur_troop_party"),
        (call_script, "script_party_calculate_and_set_nearby_friend_enemy_follower_strengths", ":cur_troop_party"),
      (try_end),
      (call_script, "script_party_calculate_and_set_nearby_friend_enemy_follower_strengths", "p_main_party"),
      ]),
    
    
	  # script_recalculate_ais
	  # Input: none
	  # Output: none

	  #When a lord changes factions
	  #When a center changes factions
	  #When a center is captured
	  #When a marshal is defeated
	  #Every 23 hours
		("recalculate_ais",
		[
		  (call_script, "script_init_ai_calculation"),

		  (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
		  (assign, reg8, ":faction_no"),
			(faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
			#(neg|faction_slot_eq, ":faction_no",  slot_faction_marshall, "trp_player"),
			(call_script, "script_decide_faction_ai", ":faction_no"),
		  (try_end),

		  ##diplomacy start+ add support for promoted kingdom ladies
		  (try_for_range, ":troop_no", heroes_begin, heroes_end),#<- change active_npcs to heroes
		  ##diplomacy end+
			(store_troop_faction, ":faction_no", ":troop_no"),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			(call_script, "script_calculate_troop_ai", ":troop_no"),
		  (try_end),
		]),
    
    # script_calculate_troop_ai
    # Input: troop_no
    # Output: none
    #Now called directly from scripts
  ("calculate_troop_ai",
    [
      (store_script_param, ":troop_no", 1),

      (try_begin),
        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
        (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
        (gt, ":party_no", 0),
		(party_is_active, ":party_no"),
		##diplomacy start+
		#Testing notifications
		(party_get_slot, ":old_ai_state", ":party_no", slot_party_ai_state),
		#(party_get_slot, ":old_ai_object", ":party_no", slot_party_ai_object),
		##diplomacy end+
		(call_script, "script_npc_decision_checklist_party_ai", ":troop_no"), #This handles AI for both marshal and other parties
		(call_script, "script_party_set_ai_state", ":party_no", reg0, reg1),
		##diplomacy start+
		#Notify the player of changes to spouse and affiliates
		(party_get_slot, ":new_ai_state", ":party_no", slot_party_ai_state),
		(party_get_slot, ":new_ai_object", ":party_no", slot_party_ai_object),
		
		##(this_or_next|neq, ":old_ai_object", ":new_ai_object",
		(neq, ":old_ai_state", ":new_ai_state"),
		(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
		#(assign, reg0, 0),
		#(try_begin),
		#	(this_or_next|troop_slot_eq, ":troop_no", slot_troop_spouse, "trp_player"),
		#	(troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_no"),
		#	(assign, reg0, 1),
		##(else_try),
		##	(store_faction_of_troop, ":troop_faction", ":troop_no"),
		##	(is_between,
		##(else_try),
		#	(call_script, "script_dplmc_is_affiliated_family_member", ":troop_no"),
		#(try_end),
		(call_script, "script_dplmc_store_troop_is_eligible_for_affiliate_messages", ":troop_no"),
		(gt, reg0, 0),
		
		
		#Some of these have non-obvious secondary uses.
		#xxx TODO: Later, I should go and verify all of them.
		(str_store_troop_name, s0, ":troop_no"),
		
		(try_begin),
			(eq, ":new_ai_state", spai_besieging_center),
			(is_between, ":new_ai_object", centers_begin, centers_end),
			(str_store_party_name, s1, ":new_ai_object"),
			(display_message, "@{s0} is laying siege to {s1}."),
		(else_try),
			(eq, ":new_ai_state", spai_patrolling_around_center),
			(is_between, ":new_ai_object", centers_begin, centers_end),
			(str_store_party_name, s1, ":new_ai_object"),
			(display_message, "@{s0} is patrolling around {s1}."),
		(else_try),
			(eq, ":new_ai_state", spai_raiding_around_center),
			(is_between, ":new_ai_object", centers_begin, centers_end),
			(str_store_party_name, s1, ":new_ai_object"),
			(display_message, "@{s0} is raiding around {s1}."),
		(else_try),
			(eq, ":new_ai_state", spai_engaging_army),
			(gt, ":new_ai_object", -1),
			(party_is_active, ":new_ai_object"),
			(str_store_party_name, s1, ":new_ai_object"),
			(display_message, "@{s0} is engaging {s1}."),
		(else_try),
			(eq, ":new_ai_state", spai_accompanying_army),
			(gt, ":new_ai_object", -1),
			(party_is_active, ":new_ai_object"),
			(str_store_party_name, s1, ":new_ai_object"),
			(display_message, "@{s0} is accompanying {s1}."),
		(else_try),
			(eq, ":new_ai_state", spai_screening_army),
			(gt, ":new_ai_object", -1),
			(party_is_active, ":new_ai_object"),
			(str_store_party_name, s1, ":new_ai_object"),
			(display_message, "@{s0} is screening the advance of {s1}."),
		(else_try),
			(eq, ":new_ai_state", spai_trading_with_town),
			(is_between, ":new_ai_object", centers_begin, centers_end),
			(str_store_party_name, s1, ":new_ai_object"),
			(display_message, "@{s0} is trading with {s1}."),
		(else_try),
			(eq, ":new_ai_state", spai_retreating_to_center),
			(is_between, ":new_ai_object", centers_begin, centers_end),
			(str_store_party_name, s1, ":new_ai_object"),
			(display_message, "@{s0} is retreating to {s1}."),
		(else_try),
			(eq, ":new_ai_state", spai_visiting_village),
			(is_between, ":new_ai_object", centers_begin, centers_end),
			(str_store_party_name, s1, ":new_ai_object"),
			(display_message, "@{s0} is visiting {s1}."),
		(try_end),
		#Make it obvious that something went wrong if something tries to use the registers
		(str_store_string, s0, "str_ERROR_string"),
		(str_store_string, s1, "str_ERROR_string"),
		##diplomacy end+
      (try_end),
    ]),
    
    # script_diplomacy_start_peace_between_kingdoms
    # Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
    # Output: none
    ("diplomacy_start_peace_between_kingdoms", #sets relations between two kingdoms
      [
        (store_script_param, ":kingdom_a", 1),
        (store_script_param, ":kingdom_b", 2),
        (store_script_param, ":initializing_war_peace_cond", 3), #set to 1 if not the start of the game
        
        (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
        (val_max, ":relation", 0),
        (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
        (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),
        
        (try_begin),
          (eq, "$players_kingdom", ":kingdom_a"),
          (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
          (val_max, ":relation", 0),
          (call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
          (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
        (else_try),
          (eq, "$players_kingdom", ":kingdom_b"),
          (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
          (val_max, ":relation", 0),
          (call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
          (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
        (try_end),
        
        (try_for_range, ":cur_center", centers_begin, centers_end),
          (store_faction_of_party, ":faction_no", ":cur_center"),
          (this_or_next|eq, ":faction_no", ":kingdom_a"),
          (eq, ":faction_no", ":kingdom_b"),
          (party_get_slot, ":besieger_party", ":cur_center", slot_center_is_besieged_by),
          (ge, ":besieger_party", 0), #town is under siege
          (party_is_active, ":besieger_party"),
          (store_faction_of_party, ":besieger_party_faction_no", ":besieger_party"),
          (this_or_next|eq, ":besieger_party_faction_no", ":kingdom_a"),
          (eq, ":besieger_party_faction_no", ":kingdom_b"),
          (call_script, "script_lift_siege", ":cur_center", 0),
        (try_end),
        
        (try_begin),
          (this_or_next|eq, "$players_kingdom", ":kingdom_a"),
          (eq, "$players_kingdom", ":kingdom_b"),
          
          (ge, "$g_player_besiege_town", 0),
          (party_is_active, "$g_player_besiege_town"),
          
          (store_faction_of_party, ":besieged_center_faction_no", "$g_player_besiege_town"),
          
          (this_or_next|eq, ":besieged_center_faction_no", ":kingdom_a"),
          (eq, ":besieged_center_faction_no", ":kingdom_b"),
          
          (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
          (assign, "$g_player_besiege_town", -1),
        (try_end),
        
        (try_begin),
          (eq, ":initializing_war_peace_cond", 1),
          (str_store_faction_name_link, s1, ":kingdom_a"),
          (str_store_faction_name_link, s2, ":kingdom_b"),
          (display_log_message, "@{s1} and {s2} have made peace with each other."),
          (call_script, "script_add_notification_menu", "mnu_notification_peace_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu
          (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
          (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
          (assign, "$g_recalculate_ais", 1),
        (try_end),
        
	  (try_begin), #add truce
		(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
		##diplomacy begin
	    #(faction_set_slot, ":kingdom_b", ":truce_slot", 40),
        ##nested diplomacy start+ replace "20" with constant for truce length
#        (faction_set_slot, ":kingdom_b", ":truce_slot", 20),
        (faction_set_slot, ":kingdom_b", ":truce_slot", dplmc_treaty_truce_days_initial),
        ##nested diplomacy end+
	    ##diplomacy end
		(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
		(val_sub, ":truce_slot", kingdoms_begin),
	    ##diplomacy begin
	    #(faction_set_slot, ":kingdom_a", ":truce_slot", 40),
        ##nested diplomacy start+ replace "20" with constant for truce length
        #(faction_set_slot, ":kingdom_a", ":truce_slot", 20),
        (faction_set_slot, ":kingdom_a", ":truce_slot", dplmc_treaty_truce_days_initial),
        ##nested diplomacy end+
        ##diplomacy end
		(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
		(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
		#(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
		(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),
		(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
		(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
		#(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
		(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),
	  (try_end),
  ]),

    
    
    
    ("event_kingdom_make_peace_with_kingdom",
      [
        (store_script_param_1, ":source_kingdom"),
        (store_script_param_2, ":target_kingdom"),
        (try_begin),
          (check_quest_active, "qst_capture_prisoners"),
          (try_begin),
            (eq, "$players_kingdom", ":source_kingdom"),
            (quest_slot_eq, "qst_capture_prisoners", slot_quest_target_faction, ":target_kingdom"),
            (call_script, "script_cancel_quest", "qst_capture_prisoners"),
          (else_try),
            (eq, "$players_kingdom", ":target_kingdom"),
            (quest_slot_eq, "qst_capture_prisoners", slot_quest_target_faction, ":source_kingdom"),
            (call_script, "script_cancel_quest", "qst_capture_prisoners"),
          (try_end),
        (try_end),
        
        (try_begin),
          (check_quest_active, "qst_capture_enemy_hero"),
          (try_begin),
            (eq, "$players_kingdom", ":source_kingdom"),
            (quest_slot_eq, "qst_capture_enemy_hero", slot_quest_target_faction, ":target_kingdom"),
            (call_script, "script_cancel_quest", "qst_capture_enemy_hero"),
          (else_try),
            (eq, "$players_kingdom", ":target_kingdom"),
            (quest_slot_eq, "qst_capture_enemy_hero", slot_quest_target_faction, ":source_kingdom"),
            (call_script, "script_cancel_quest", "qst_capture_enemy_hero"),
          (try_end),
        (try_end),
        
        
        
        (try_begin),
          (check_quest_active, "qst_persuade_lords_to_make_peace"),
          (quest_get_slot, ":lord_1", "qst_persuade_lords_to_make_peace", slot_quest_target_troop),
          (quest_get_slot, ":lord_2", "qst_persuade_lords_to_make_peace", slot_quest_object_troop),
          
          (try_begin),
            (lt, ":lord_1", 0),
            (val_mul, ":lord_1", -1),
          (try_end),
          (try_begin),
            (lt, ":lord_2", 0),
            (val_mul, ":lord_2", -1),
          (try_end),
          
          
          (store_faction_of_troop, ":lord_1_faction", ":lord_1"),
          (store_faction_of_troop, ":lord_2_faction", ":lord_2"),
          
          (this_or_next|eq, ":lord_1_faction", ":source_kingdom"),
          (eq, ":lord_2_faction", ":source_kingdom"),
          
          (this_or_next|eq, ":lord_1_faction", ":target_kingdom"),
          (eq, ":lord_2_faction", ":target_kingdom"),
          
          (call_script, "script_cancel_quest", "qst_persuade_lords_to_make_peace"),
          
        (try_end),
        
        #Rescue prisoners cancelled in simple_triggers
        
        (try_begin),
          (this_or_next|faction_slot_eq, ":target_kingdom", slot_faction_leader, "trp_player"),
          (faction_slot_eq, ":source_kingdom", slot_faction_leader, "trp_player"),
          
          (call_script, "script_change_player_right_to_rule", 3),
        (try_end),
        
    ]),
    
    # script_randomly_start_war_peace
    # Input: arg1 = initializing_war_peace_cond (1 = true, 0 = false)
    # Output: none
    
    #Aims to introduce a slightly simpler system in which the AI kings' reasoning could be made more  transparent to the player. At the start of the game, this may lead to less variation in outcomes, though
    ("randomly_start_war_peace_new",
      [
        (store_script_param_1, ":initializing_war_peace_cond"),
        
        (assign, ":players_kingdom_at_peace", 0), #if the player kingdom is at peace, then create an enmity
        (try_begin),
          (is_between, "$players_kingdom", "fac_kingdom_1", kingdoms_end),
          (assign, ":players_kingdom_at_peace", 1),
        (try_end),
        
		##diplomacy start+
		#Introduce some minor variation by changing the order in which factions consider things.
		##OLD:
		#(try_for_range, ":cur_kingdom", "fac_kingdom_1", kingdoms_end),
		#    (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
		#
		#	(try_for_range, ":cur_kingdom_2", kingdoms_begin, kingdoms_end),
		##NEW:
		(store_random_in_range, ":random_offset_1", "fac_kingdom_1", kingdoms_end),
		(val_sub, ":random_offset_1", "fac_kingdom_1"),
		(try_for_range, ":cur_kingdom", "fac_kingdom_1", kingdoms_end),
			(val_add, ":cur_kingdom", ":random_offset_1"),
			(try_begin),
				(ge, ":cur_kingdom", kingdoms_end),
				(val_sub, ":cur_kingdom", kingdoms_end),
				(val_add, ":cur_kingdom", "fac_kingdom_1"),
			(try_end),
			(faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
			(store_random_in_range, ":random_offset_2", kingdoms_begin, kingdoms_end),
			(val_sub, ":random_offset_2", kingdoms_begin),
			(try_for_range, ":cur_kingdom_2", kingdoms_begin, kingdoms_end),
				(val_add, ":cur_kingdom_2", ":random_offset_2"),
				(try_begin),
					(ge, ":cur_kingdom_2", kingdoms_end),
					(val_sub, ":cur_kingdom_2", kingdoms_end),
					(val_add, ":cur_kingdom_2", kingdoms_begin),
				(try_end),
		##diplomacy end+
				(neq, ":cur_kingdom", ":cur_kingdom_2"),
				(faction_slot_eq, ":cur_kingdom_2", slot_faction_state, sfs_active),

				(call_script, "script_npc_decision_checklist_peace_or_war", ":cur_kingdom", ":cur_kingdom_2", -1),
				(assign, ":kingdom_1_to_kingdom_2", reg0),

				(store_relation, ":cur_relation", ":cur_kingdom", ":cur_kingdom_2"),
				(try_begin),
					(lt, ":cur_relation", 0), #AT WAR

					(try_begin),
						(eq, ":cur_kingdom", "$players_kingdom"),
						(assign, ":players_kingdom_at_peace", 0),
					(try_end),

					(ge, ":kingdom_1_to_kingdom_2", 1),

			##diplomacy begin
			(try_begin),
			  (store_current_hours, ":cur_hours"),
			  (faction_get_slot, ":faction_ai_last_decisive_event", ":cur_kingdom", slot_faction_ai_last_decisive_event),
			  (store_sub, ":hours_since_last_decisive_event", ":cur_hours", ":faction_ai_last_decisive_event"),
			  (ge, ":hours_since_last_decisive_event", 96), #wait 4 days until you conclude peace after war
			##diplomacy end
			  (try_begin),
				(eq, ":cur_kingdom_2", "fac_player_supporters_faction"),

				(store_mul, ":goodwill_level", ":kingdom_1_to_kingdom_2", 2),
				(store_random_in_range, ":random", 0, 20),
				(try_begin),
				  (lt, ":random", ":goodwill_level"),
				  (call_script, "script_add_notification_menu", "mnu_question_peace_offer", ":cur_kingdom", 0),
				(try_end),
			  (else_try),
				(call_script, "script_npc_decision_checklist_peace_or_war", ":cur_kingdom_2", ":cur_kingdom", -1),
				(assign, ":kingdom_2_to_kingdom_1", reg0),
				(ge, ":kingdom_2_to_kingdom_1", 1),

				(store_mul, ":goodwill_level", ":kingdom_1_to_kingdom_2", ":kingdom_2_to_kingdom_1"),
				(store_random_in_range, ":random", 0, 20),
				(lt, ":random", ":goodwill_level"),

				(try_begin),
				  (eq, "$g_include_diplo_explanation", 0),
				  (assign, "$g_include_diplo_explanation", ":cur_kingdom"),
				  (str_store_string, s57, "str_s14"),
				(try_end),

				(call_script, "script_diplomacy_start_peace_between_kingdoms", ":cur_kingdom", ":cur_kingdom_2", ":initializing_war_peace_cond"),
			  (try_end),
			##diplomacy begin
			(try_end),
			##diplomacy end
				(else_try),
					(ge, ":cur_relation", 0), #AT PEACE
              
              (call_script, "script_npc_decision_checklist_peace_or_war", ":cur_kingdom", ":cur_kingdom_2", -1),
              
              #negative, leans towards war/positive, leans towards peace
              (le, reg0, 0), #still no chance of war unless provocation, or at start of game
              
              (assign, ":hostility", reg0),
              
              (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":cur_kingdom", ":cur_kingdom_2"),
              (le, reg0, 0), #no truce
              
              (val_add, ":hostility", reg0), #increase hostility if there is a provocation
              
              (val_sub, ":hostility", 1), #greater chance at start of game
              (val_add, ":hostility", ":initializing_war_peace_cond"), #this variable = 1 after the start
              
              (store_mul, ":hostility_squared", ":hostility", ":hostility"),
              (store_random_in_range, ":random", 0, 50),
              
			##diplomacy begin
			#check for pact and lower probability if there is one
			(try_for_range, ":third_kingdom", kingdoms_begin, kingdoms_end),
			  (neq, ":third_kingdom", ":cur_kingdom"),
			  (neq, ":third_kingdom", ":cur_kingdom_2"),
			  ##nested diplomacy start+  Faction must be active
			  (faction_slot_eq, ":third_kingdom", slot_faction_state, sfs_active),
			  ##nested diplomacy end+
                
                (store_relation, ":cur_relation", ":cur_kingdom_2", ":third_kingdom"),
                (ge, ":cur_relation", 0), #AT PEACE
                
                (store_add, ":truce_slot", ":third_kingdom", slot_faction_truce_days_with_factions_begin),
                (val_sub, ":truce_slot", kingdoms_begin),
                (faction_get_slot, ":truce_days", ":cur_kingdom_2", ":truce_slot"),
                (gt, ":truce_days", 40),
                (store_div, ":hostility_change", ":truce_days", 20),
                (val_sub, ":hostility_squared", ":hostility_change"),
              (try_end),
              ##diplomacy 3.2 end
              
              (lt, ":random", ":hostility_squared"),
              
              (try_begin),
                (eq, "$g_include_diplo_explanation", 0),
                (assign, "$g_include_diplo_explanation", ":cur_kingdom"),
                (str_store_string, s57, "str_s14"),
              (try_end),
              (call_script, "script_diplomacy_start_war_between_kingdoms", ":cur_kingdom", ":cur_kingdom_2", ":initializing_war_peace_cond"),
              
              (try_begin), #do some war damage for
                (eq, ":initializing_war_peace_cond", 0),
                (store_random_in_range, ":war_damage_inflicted", 10, 120),
                (store_add, ":slot_war_damage_inflicted", ":cur_kingdom", slot_faction_war_damage_inflicted_on_factions_begin),
                (val_sub, ":slot_war_damage_inflicted", kingdoms_begin),
                (faction_set_slot, ":cur_kingdom_2",  ":slot_war_damage_inflicted", ":war_damage_inflicted"),
                
                (store_add, ":slot_war_damage_inflicted", ":cur_kingdom_2", slot_faction_war_damage_inflicted_on_factions_begin),
                (val_sub, ":slot_war_damage_inflicted", kingdoms_begin),
                (faction_set_slot, ":cur_kingdom", ":slot_war_damage_inflicted", ":war_damage_inflicted"),
              (try_end),
              ##diplomacy begin
            (else_try),
              (ge, ":cur_relation", 0), #AT PEACE
              (ge, ":kingdom_1_to_kingdom_2", 1),
              
              #(assign, ":barrier", 2), ##Diplomacy 3.2
              (store_add, ":faction1_to_faction2_slot", ":cur_kingdom_2", dplmc_slot_faction_attitude_begin),
              (party_get_slot, ":barrier",":cur_kingdom", ":faction1_to_faction2_slot"), ##
              
              (try_for_range, ":third_kingdom", kingdoms_begin, kingdoms_end),
                (neq, ":third_kingdom", ":cur_kingdom"),
                (neq, ":third_kingdom", ":cur_kingdom_2"),
                
			  (store_add, ":slot_truce_days", ":cur_kingdom", slot_faction_truce_days_with_factions_begin),
			  (val_sub, ":slot_truce_days", kingdoms_begin),
			  (faction_get_slot, ":truce_days", ":third_kingdom", ":slot_truce_days"),
			  ##nested diplomacy start+ change to use constants
			  #(gt, ":truce_days", 10),
			  (gt, ":truce_days", dplmc_treaty_truce_days_half_done),
			  ##nested diplomacy end+
			  (val_sub, ":barrier", 1),
                
                (try_begin), #debug
                  (eq, "$cheat_mode", 1),
                  (str_store_faction_name, s5, ":cur_kingdom"),
                  (str_store_faction_name, s6, ":third_kingdom"),
                  (str_store_faction_name, s7, ":cur_kingdom_2"),
                  (display_message, "@{!}DEBUG: {s5} has truce with {s6}. Pact with {s7} is harder!"),
                (try_end),
                
              (try_end),
              
              (val_max, ":barrier", 0),
              (store_random_in_range, ":random", 0, 130),
              (le, ":random", ":barrier"),
              
              (store_add, ":slot_truce_days", ":cur_kingdom", slot_faction_truce_days_with_factions_begin),
              (val_sub, ":slot_truce_days", kingdoms_begin),
              (faction_get_slot, ":truce_days", ":cur_kingdom_2", ":slot_truce_days"),
              
			(store_random_in_range, ":random", 0, 3),
			(assign, ":continue", 0),
			(try_begin),
			  ##nested diplomacy start+ change to use constants
			  #(is_between, ":truce_days", 0, 50),
			  (is_between, ":truce_days", 0, dplmc_treaty_defense_days_half_done),#50 = halfway from a defensive alliance to a trade treaty
			  ##nested diplomacy end+
			  (ge, ":cur_relation", 20),
			  (try_begin),
				(le, ":random", 0), #1/3 for alliance, defensive
				(assign, ":continue", 1),
			  (try_end),
			(else_try),
			  ##nested diplomacy start+ change to use constants
			  #(is_between, ":truce_days", 0, 10),
			  (is_between, ":truce_days", 0, dplmc_treaty_truce_days_half_done),#10 = halfway done with a truce
			  ##nested diplomacy end+
			  (ge, ":cur_relation", 10),
			  (try_begin),
				(le, ":random", 1), #2/3 # for trade
				(assign, ":continue", 1),
			  (try_end),
			(else_try),
			  (assign, ":continue", 1),  # for non-aggression
			(try_end),
			(eq, ":continue", 1),

			(try_begin),
			  ##nested diplomacy start+
			  (call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":cur_kingdom_2"),
			  (this_or_next|ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
			  ##nested diplomacy end+
			  (eq, ":cur_kingdom_2", "fac_player_supporters_faction"),
			  (ge, ":kingdom_1_to_kingdom_2", 1),

			  (try_begin),
				##nested diplomacy start+ change to use constants
				#(is_between, ":truce_days", 20, 50),
				(is_between, ":truce_days", dplmc_treaty_trade_days_expire, dplmc_treaty_defense_days_half_done),
				##nested diplomacy end+
				(ge, ":cur_relation", 30),
				(faction_slot_eq, ":cur_kingdom", slot_faction_recognized_player, 1), #recognized us
				(call_script, "script_add_notification_menu", "mnu_dplmc_question_alliance_offer", ":cur_kingdom", 0),
			  (else_try),
				##nested diplomacy start+ change to use constants
				#(is_between, ":truce_days", 0, 30), #you need a non-aggression or trade aggreement for an defensive pact
				(is_between, ":truce_days", 0, dplmc_treaty_trade_days_half_done),
				##nested diplomacy end+
				(ge, ":cur_relation", 20),
				(faction_slot_eq, ":cur_kingdom", slot_faction_recognized_player, 1), #recognized us
				(call_script, "script_add_notification_menu", "mnu_dplmc_question_defensive_offer", ":cur_kingdom", 0),
			  (else_try),
				##nested diplomacy start+ change to use constants
				#(is_between, ":truce_days", 0, 10),
				(is_between, ":truce_days", 0, dplmc_treaty_truce_days_half_done),
				##diplomacy end+
				(ge, ":cur_relation", 10),
				(faction_slot_eq, ":cur_kingdom", slot_faction_recognized_player, 1), #recognized us
				(call_script, "script_add_notification_menu", "mnu_dplmc_question_trade_offer", ":cur_kingdom", 0),
			  (else_try),
				(eq, ":truce_days", 0),
				(ge, ":cur_relation", 5),
				(call_script, "script_add_notification_menu", "mnu_dplmc_question_nonaggression_offer", ":cur_kingdom", 0),
			  (try_end),
			(else_try),
			  (ge, ":kingdom_1_to_kingdom_2", 1),

			  (call_script, "script_npc_decision_checklist_peace_or_war", ":cur_kingdom_2", ":cur_kingdom", -1),
			  (assign, ":kingdom_2_to_kingdom_1", reg0),
			  (ge, ":kingdom_2_to_kingdom_1", 1),

			  (try_begin),
				##nested diplomacy start+ change to use constants
				#(is_between, ":truce_days", 20, 50),
				(is_between, ":truce_days", dplmc_treaty_trade_days_expire, dplmc_treaty_defense_days_half_done),
				##nested diplomacy end+
				(ge, ":cur_relation", 30),
				(call_script, "script_dplmc_start_alliance_between_kingdoms", ":cur_kingdom", ":cur_kingdom_2", ":initializing_war_peace_cond"),
			  (else_try),
				##nested diplomacy start+ change to use constants
				#(is_between, ":truce_days", 0, 30), #you need a non-aggression or trade aggreement for an defensive pact
				(is_between, ":truce_days", 0, dplmc_treaty_trade_days_half_done),
				##nested diplomacy end+
				(ge, ":cur_relation", 20),
				(call_script, "script_dplmc_start_defensive_between_kingdoms", ":cur_kingdom", ":cur_kingdom_2", ":initializing_war_peace_cond"),
			  (else_try),
				##nested diplomacy start+ change to use constants
				#(is_between, ":truce_days", 0, 10),
				(is_between, ":truce_days", 0, dplmc_treaty_truce_days_half_done),
				##nested diplomacy end+
				(ge, ":cur_relation", 10),
				(call_script, "script_dplmc_start_trade_between_kingdoms", ":cur_kingdom", ":cur_kingdom_2", ":initializing_war_peace_cond"),
			  (else_try),
				(eq, ":truce_days", 0),
				(call_script, "script_dplmc_start_nonaggression_between_kingdoms", ":cur_kingdom", ":cur_kingdom_2", ":initializing_war_peace_cond"),
			  (try_end),
			(try_end),
		  ##diplomacy end
		  (try_end),
			(try_end),
		(try_end),
        
        (try_begin),
          (eq, ":players_kingdom_at_peace", 1),
          (val_add, "$players_kingdom_days_at_peace", 1),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (assign, reg3, "$players_kingdom_days_at_peace"),
            (display_message, "@{!}DEBUG -- Player's kingdom has had {reg3} days of peace"),
          (try_end),
        (else_try),
          (assign, "$players_kingdom_days_at_peace", 0),
        (try_end),
        
    ]),
    
    
    # script_randomly_start_war_peace
    # Input: arg1 = initializing_war_peace_cond (1 = true, 0 = false)
    # Output: none
    #  ("randomly_start_war_peace",
    #    [
    #      (store_script_param_1, ":initializing_war_peace_cond"),
    #      (assign, ":total_resources", 0),
    #      (assign, ":total_active_kingdoms", 0),
    #      (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
    #        (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
    #        (val_add, ":total_active_kingdoms", 1),
    #        (faction_get_slot, ":num_towns", ":cur_kingdom", slot_faction_num_towns),
    #        (store_mul, ":kingdom_resources_value", ":num_towns", 2),
    #        (faction_get_slot, ":num_castles", ":cur_kingdom", slot_faction_num_castles),
    #        (val_add, ":kingdom_resources_value", ":num_castles"),
    #        (val_mul, ":kingdom_resources_value", 10),
    #        (val_max, ":kingdom_resources_value", 1),
    #        (val_mul, ":kingdom_resources_value", 1000),
    #        (faction_get_slot, ":num_armies", ":cur_kingdom", slot_faction_num_armies),
    #        (val_max, ":num_armies", 1),
    #        (val_div, ":kingdom_resources_value", ":num_armies"),
    #        (val_add, ":total_resources", ":kingdom_resources_value"),
    #      (try_end),
    #      (val_max, ":total_active_kingdoms", 1),
    #      (store_div, ":average_resources", ":total_resources", ":total_active_kingdoms"),
    
    #      (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
    ##       (neq, ":cur_kingdom", "fac_player_supporters_faction"),
    #        (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
    #        (assign, ":num_ongoing_wars", 0),
    #        (try_for_range, ":other_kingdom", kingdoms_begin, kingdoms_end),
    #          (faction_slot_eq, ":other_kingdom", slot_faction_state, sfs_active),
    #          (store_relation, ":other_relation", ":cur_kingdom", ":other_kingdom"),
    #          (lt, ":other_relation", 0),
    #          (val_add, ":num_ongoing_wars", 1),
    #        (try_end),
    
    #        (faction_get_slot, ":num_towns", ":cur_kingdom", slot_faction_num_towns),
    #        (store_mul, ":kingdom_1_resources_value", ":num_towns", 2),
    #        (faction_get_slot, ":num_castles", ":cur_kingdom", slot_faction_num_castles),
    #        (val_add, ":kingdom_1_resources_value", ":num_castles"),
    #        (val_mul, ":kingdom_1_resources_value", 10),
    #        (val_max, ":kingdom_1_resources_value", 1),
    #        (val_mul, ":kingdom_1_resources_value", 1000),
    #        (faction_get_slot, ":num_armies", ":cur_kingdom", slot_faction_num_armies),
    #        (val_max, ":num_armies", 1),
    #        (val_div, ":kingdom_1_resources_value", ":num_armies"),
    
    #        (store_add, ":start_cond", ":cur_kingdom", 1),
    #        (try_for_range, ":cur_kingdom_2", ":start_cond", kingdoms_end),
    ##         (neq, ":cur_kingdom", "fac_player_supporters_faction"),
    #          (faction_slot_eq, ":cur_kingdom_2", slot_faction_state, sfs_active),
    
    #          (assign, ":num_ongoing_wars_2", 0),
    #          (try_for_range, ":other_kingdom", kingdoms_begin, kingdoms_end),
    #            (faction_slot_eq, ":other_kingdom", slot_faction_state, sfs_active),
    #            (store_relation, ":other_relation", ":cur_kingdom_2", ":other_kingdom"),
    #            (lt, ":other_relation", 0),
    #            (val_add, ":num_ongoing_wars_2", 1),
    #          (try_end),
    
    #          (store_add, ":total_ongoing_wars", ":num_ongoing_wars", ":num_ongoing_wars_2"),
    
    #          (faction_get_slot, ":num_towns", ":cur_kingdom_2", slot_faction_num_towns),
    #          (store_mul, ":kingdom_2_resources_value", ":num_towns", 2),
    #          (faction_get_slot, ":num_castles", ":cur_kingdom_2", slot_faction_num_castles),
    #          (val_add, ":kingdom_2_resources_value", ":num_castles"),
    #          (val_mul, ":kingdom_2_resources_value", 10),
    #          (val_max, ":kingdom_2_resources_value", 1),
    #          (val_mul, ":kingdom_2_resources_value", 1000),
    #          (faction_get_slot, ":num_armies", ":cur_kingdom_2", slot_faction_num_armies),
    #          (val_max, ":num_armies", 1),
    #          (val_div, ":kingdom_2_resources_value", ":num_armies"),
    
    #          (assign, ":max_resources_value", ":kingdom_1_resources_value"),
    #          (val_max, ":max_resources_value", ":kingdom_2_resources_value"),
    #          (val_mul, ":max_resources_value", 100),
    #          (val_div, ":max_resources_value", ":average_resources"),
    
    #          (assign, ":cur_king", -1),
    #          (try_begin),
    #            (eq, ":cur_kingdom", "fac_player_supporters_faction"),
    #            (faction_get_slot, ":cur_king", ":cur_kingdom_2", slot_faction_leader),
    #            (assign, ":cur_relation", reg0),
    #            (store_sub, ":relation_effect", 200, ":cur_relation"),
    #            (val_mul, ":kingdom_1_resources_value", ":relation_effect"),
    #            (val_div, ":kingdom_1_resources_value", 200),
    #          (else_try),
    #            (eq, ":cur_kingdom_2", "fac_player_supporters_faction"),
    #            (faction_get_slot, ":cur_king", ":cur_kingdom", slot_faction_leader),
    #          (try_end),
    
    #          (try_begin),
    #            (ge, ":cur_king", 0),
    #            (call_script, "script_troop_get_player_relation", ":cur_king"),
    #            (assign, ":cur_relation", reg0),
    #            (store_sub, ":relation_effect", 200, ":cur_relation"),
    #            (val_mul, ":max_resources_value", ":relation_effect"),
    #            (val_div, ":max_resources_value", 200),
    #          (try_end),
    
    #max_resources_value is the obtained value that gives us how tempting the kingdom's values are
    #average is 100
    #         (val_clamp, ":max_resources_value", 20, 500),
    #not letting more than 5 times higher chance of declaring war or peace
    
    #        (store_random_in_range, ":random_no", 0, 10000),
    #         (store_relation, ":cur_relation", ":cur_kingdom", ":cur_kingdom_2"),
    #         (try_begin),
    #           (lt, ":cur_relation", 0), #AT WAR
    #           (store_mul, ":chance_to_make_peace", ":total_ongoing_wars", 50),
    #           (val_mul, ":chance_to_make_peace", 100),
    #           (val_div, ":chance_to_make_peace", ":max_resources_value"),
    #           (try_begin),
    #disable random peace for special conditions
    #             (this_or_next|eq, ":cur_kingdom", "fac_player_supporters_faction"),
    #             (eq, ":cur_kingdom_2", "fac_player_supporters_faction"),
    #             (assign, ":continue", 0),
    #    (try_begin),
    #     (gt, "$supported_pretender", 0),
    #    (this_or_next|eq, ":cur_kingdom", "$supported_pretender_old_faction"),
    #     (eq, ":cur_kingdom_2", "$supported_pretender_old_faction"),
    #      (assign, ":continue", 1),
    #     (else_try),
    #         (is_between, "$players_oath_renounced_against_kingdom", kingdoms_begin, kingdoms_end),
    #          (this_or_next|eq, ":cur_kingdom", "$players_oath_renounced_against_kingdom"),
    #           (eq, ":cur_kingdom_2", "$players_oath_renounced_against_kingdom"),
    #            (assign, ":continue", 1),
    #           (try_end),
    #     (eq, ":continue", 1),
    #      (assign, ":chance_to_make_peace", 0),
    #     (try_end),
    #      (try_begin),
    #         (lt, ":random_no", ":chance_to_make_peace"),
    #          (assign, ":continue", 1),
    #           (try_begin),
    #              (check_quest_active, "qst_persuade_lords_to_make_peace"),
    #  (quest_get_slot, ":quest_target_faction", "qst_persuade_lords_to_make_peace", slot_quest_target_faction),
    #   (quest_get_slot, ":quest_object_faction", "qst_persuade_lords_to_make_peace", slot_quest_object_faction),
    #    (this_or_next|eq, ":cur_kingdom", ":quest_target_faction"),
    #     (eq, ":cur_kingdom", ":quest_object_faction"),
    #      (this_or_next|eq, ":cur_kingdom_2", ":quest_target_faction"),
    #       (eq, ":cur_kingdom_2", ":quest_object_faction"),
    #        (assign, ":continue", 0), #Do not declare war if the quest is active for the specific kingdoms
    #       (try_end),
    #        (eq, ":continue", 1),
    #         (try_begin),
    #            (eq, ":cur_kingdom", "fac_player_supporters_faction"),
    #             (call_script, "script_add_notification_menu", "mnu_question_peace_offer", ":cur_kingdom_2", 0),
    #            (else_try),
    #    (eq, ":cur_kingdom_2", "fac_player_supporters_faction"),
    #     (call_script, "script_add_notification_menu", "mnu_question_peace_offer", ":cur_kingdom", 0),
    #    (else_try),
    #       (call_script, "script_diplomacy_start_peace_between_kingdoms", ":cur_kingdom", ":cur_kingdom_2", ":initializing_war_peace_cond"),
    #      (try_end),
    #     (try_end),
    #    (else_try), # AT PEACE
    #       (assign, ":chance_to_declare_war", 6),
    #        (val_sub, ":chance_to_declare_war", ":total_ongoing_wars"),
    #         (val_mul, ":chance_to_declare_war", 50),
    #  (val_mul, ":chance_to_declare_war", ":max_resources_value"),
    #   (val_div, ":chance_to_declare_war", 100),
    #    (try_begin),
    #       (lt, ":random_no", ":chance_to_declare_war"),
    #        (assign, ":continue", 1),
    #         (try_begin),
    #            (check_quest_active, "qst_raid_caravan_to_start_war"),
    # (quest_get_slot, ":quest_target_faction", "qst_raid_caravan_to_start_war", slot_quest_target_faction),
    #  (quest_get_slot, ":quest_object_faction", "qst_raid_caravan_to_start_war", slot_quest_object_faction),
    #   (this_or_next|eq, ":cur_kingdom", ":quest_target_faction"),
    #    (eq, ":cur_kingdom", ":quest_object_faction"),
    #     (this_or_next|eq, ":cur_kingdom_2", ":quest_target_faction"),
    #      (eq, ":cur_kingdom_2", ":quest_object_faction"),
    #       (assign, ":continue", 0), #Do not declare war if the quest is active for the specific kingdoms
    #      (try_end),
    #       (eq, ":continue", 1),
    #        (call_script, "script_diplomacy_start_war_between_kingdoms", ":cur_kingdom", ":cur_kingdom_2", ":initializing_war_peace_cond"),
    #       (try_end),
    #      (try_end),
    #     (try_end),
    #    (try_end),
    #    ]),
    
    
    
    # script_exchange_prisoners_between_factions
    # Input: arg1 = faction_no_1, arg2 = faction_no_2
    ("exchange_prisoners_between_factions",
      [
        (store_script_param_1, ":faction_no_1"),
        (store_script_param_2, ":faction_no_2"),
        (assign, ":faction_no_3", -1),
        (assign, ":faction_no_4", -1),
        (assign, ":free_companions_too", 0),
        (try_begin),
          (this_or_next|eq, "$players_kingdom", ":faction_no_1"),
          (eq, "$players_kingdom", ":faction_no_2"),
          (assign, ":faction_no_3", "fac_player_faction"),
          (assign, ":faction_no_4", "fac_player_supporters_faction"),
          (assign, ":free_companions_too", 1),
        (try_end),
        
        (try_for_parties, ":party_no"),
          (store_faction_of_party, ":party_faction", ":party_no"),
          (this_or_next|eq, ":party_faction", ":faction_no_1"),
          (this_or_next|eq, ":party_faction", ":faction_no_2"),
          (this_or_next|eq, ":party_faction", ":faction_no_3"),
          (eq, ":party_faction", ":faction_no_4"),
          (party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
          (try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
            (party_prisoner_stack_get_troop_id, ":cur_troop_id", ":party_no", ":troop_iterator"),
            
            (assign, ":continue", 0),
            (try_begin),
              (is_between, ":cur_troop_id", companions_begin, companions_end),
              (eq, ":free_companions_too", 1),
              (assign, ":continue", 1),
            (else_try),
              (neg|is_between, ":cur_troop_id", companions_begin, companions_end),
              (store_troop_faction, ":cur_faction", ":cur_troop_id"),
              (this_or_next|eq, ":cur_faction", ":faction_no_1"),
              (this_or_next|eq, ":cur_faction", ":faction_no_2"),
              (this_or_next|eq, ":cur_faction", ":faction_no_3"),
              (eq, ":cur_faction", ":faction_no_4"),
              (assign, ":continue", 1),
            (try_end),
            (eq, ":continue", 1),
            
            (try_begin),
              (troop_is_hero, ":cur_troop_id"),
              (call_script, "script_remove_troop_from_prison", ":cur_troop_id"),
            (try_end),
            (party_prisoner_stack_get_size, ":stack_size", ":party_no", ":troop_iterator"),
            (party_remove_prisoners, ":party_no", ":cur_troop_id", ":stack_size"),
          (try_end),
        (try_end),
        
    ]),
    
    # script_add_notification_menu
    # Input: arg1 = menu_no, arg2 = menu_var_1, arg3 = menu_var_2
    # Output: none
    ("add_notification_menu",
      [
        (try_begin),
          (eq, "$g_infinite_camping", 0),
          (store_script_param, ":menu_no", 1),
          (store_script_param, ":menu_var_1", 2),
          (store_script_param, ":menu_var_2", 3),
          (assign, ":end_cond", 1),
          (try_for_range, ":cur_slot", 0, ":end_cond"),
            (try_begin),
              (troop_slot_ge, "trp_notification_menu_types", ":cur_slot", 1),
              (val_add, ":end_cond", 1),
            (else_try),
              (troop_set_slot, "trp_notification_menu_types", ":cur_slot", ":menu_no"),
              (troop_set_slot, "trp_notification_menu_var1", ":cur_slot", ":menu_var_1"),
              (troop_set_slot, "trp_notification_menu_var2", ":cur_slot", ":menu_var_2"),
            (try_end),
          (try_end),
        (try_end),
    ]),
    
    # script_finish_quest
    # Input: arg1 = quest_no, arg2 = finish_percentage
    # Output: none
    ("finish_quest",
      [
        (store_script_param_1, ":quest_no"),
        (store_script_param_2, ":finish_percentage"),
        
        (quest_get_slot, ":quest_giver", ":quest_no", slot_quest_giver_troop),
        (quest_get_slot, ":quest_importance", ":quest_no", slot_quest_importance),
        (quest_get_slot, ":quest_xp_reward", ":quest_no", slot_quest_xp_reward),
        (quest_get_slot, ":quest_gold_reward", ":quest_no", slot_quest_gold_reward),
        
        (try_begin),
          (lt, ":finish_percentage", 100),
          (val_mul, ":quest_xp_reward", ":finish_percentage"),
          (val_div, ":quest_xp_reward", 100),
          (val_mul, ":quest_gold_reward", ":finish_percentage"),
          (val_div, ":quest_gold_reward", 100),
          #Changing the relation factor. Negative relation if less than 75% of the quest is finished.
          #Positive relation if more than 75% of the quest is finished.
          (assign, ":importance_multiplier", ":finish_percentage"),
          (val_sub, ":importance_multiplier", 75),
          (val_mul, ":quest_importance", ":importance_multiplier"),
          (val_div, ":quest_importance", 100),
        (else_try),
          (val_mul, ":quest_importance", 4), #was div 4. Relation was increasing very less. I changed it to mul 4.			#	1.143 Port // See comment for info
          (val_add, ":quest_importance", 1),
          (call_script, "script_change_player_relation_with_troop", ":quest_giver", ":quest_importance"),
        (try_end),
        
        (add_xp_as_reward, ":quest_xp_reward"),
        (call_script, "script_troop_add_gold", "trp_player", ":quest_gold_reward"),
        (call_script, "script_end_quest", ":quest_no"),
    ]),
    
    
    # script_get_information_about_troops_position
    # Input: arg1 = troop_no, arg2 = time (0 if present tense, 1 if past tense)
    # Output: s1 = String, reg0 = knows-or-not
    ("get_information_about_troops_position",
      [
		  (store_script_param_1, ":troop_no"),
		  (store_script_param_2, reg3),
		  ##diplomacy start+
		  #(troop_get_type, reg4, ":troop_no"),
		 (call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 4),
		  ##diplomacy end+
		  (str_store_troop_name, s2, ":troop_no"),
        
		  (assign, ":found", 0),
		  (troop_get_slot, ":center_no", ":troop_no", slot_troop_cur_center),
		  (try_begin),
			(gt, ":center_no", 0),
			(is_between, ":center_no", centers_begin, centers_end),
			(str_store_party_name_link, s3, ":center_no"),
			(str_store_string, s1, "@{s2} {reg3?was:is currently} at {s3}."),
			(assign, ":found", 1),
		  (else_try),
			(troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
			(gt, ":party_no", 0),
			(call_script, "script_get_troop_attached_party", ":troop_no"),
			(assign, ":center_no", reg0),
			(try_begin),
			  (is_between, ":center_no", centers_begin, centers_end),
			  (str_store_party_name_link, s3, ":center_no"),
			  (str_store_string, s1, "@{s2} {reg3?was:is currently} at {s3}."),
			  (assign, ":found", 1),
			(else_try),
			  (get_party_ai_behavior, ":ai_behavior", ":party_no"),
			  (eq, ":ai_behavior", ai_bhvr_travel_to_party),
			  (get_party_ai_object, ":ai_object", ":party_no"),
			  (is_between, ":ai_object", centers_begin, centers_end),
			  ##diplomacy start+
			  #(call_script, "script_get_closest_center", ":party_no"),
			  (call_script, "script_dplmc_get_closest_center_or_two", ":party_no"),
			  ##diplomacy end+
			  (str_store_party_name_link, s4, reg0),
			  (str_store_party_name_link, s3, ":ai_object"),
			  (str_store_string, s1, "@{s2} {reg3?was:is} travelling to {s3} and {reg4?she:he} {reg3?was:should be} close to {s4}{reg3?: at the moment}."),
			  (assign, ":found", 1),
			  ##diplomacy start+
			  (try_begin),
				 (gt, reg1, -1),
				 (str_store_party_name_link, s1, reg1),
				 (str_store_string, s1, "@{s2} {reg3?was:is} travelling to {s3} and {reg4?she:he} {reg3?was:should be} between {s4} and {s1}{reg3?: at the moment}."),
			  (try_end),
			  ##diplomacy end+
			(else_try),
			  ##diplomacy start+
			  #(call_script, "script_get_closest_center", ":party_no"),
			  (call_script, "script_dplmc_get_closest_center_or_two", ":party_no"),
			  ##diplomacy end+
			  (str_store_party_name_link, s3, reg0),
			  (str_store_string, s1, "@{s2} {reg3?was:is} in the field and {reg4?she:he} {reg3?was:should be} close to {s3}{reg3?: at the moment}."),
			  (assign, ":found", 1),
			  ##diplomacy start+
			  (try_begin),
				 (gt, reg1, -1),
				 (str_store_party_name_link, s1, reg1),
				 (str_store_string, s1, "@{s2} {reg3?was:is} in the field and {reg4?she:he} {reg3?was:should be} between {s3} and {s1}{reg3?: at the moment}."),
			  (try_end),
			  ##diplomacy end+
			(try_end),
		  (else_try),
			#(troop_slot_ge, ":troop_no", slot_troop_is_prisoner, 1),
			(troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
			(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
			  (party_count_prisoners_of_type, ":num_prisoners", ":center_no", ":troop_no"),
			  (gt, ":num_prisoners", 0),
			  (assign, ":found", 1),
			  (str_store_party_name_link, s3, ":center_no"),
			  (str_store_string, s1, "@{s2} {reg3?was:is} being held captive at {s3}."),
			(try_end),
			(try_begin),
			  (eq, ":found", 0),
			  (str_store_string, s1, "@{s2} {reg3?was:has been} taken captive by {reg4?her:his} enemies."),
			  (assign, ":found", 1),
			(try_end),
		  (try_end),
		  (try_begin),
			(eq, ":found", 0),
			(str_store_string, s1, "@{reg3?{s2}'s location was unknown:I don't know where {s2} is}."),
		  (try_end),
		  (assign, reg0, ":found"),
	  ]),
    
    # script_recruit_troop_as_companion
    # Input: arg1 = troop_no,
    # Output: none
    ("recruit_troop_as_companion",
      [
        (store_script_param_1, ":troop_no"),
        (troop_set_slot, ":troop_no", slot_troop_occupation, slto_player_companion),
        (troop_set_slot, ":troop_no", slot_troop_cur_center, -1),
        (troop_set_auto_equip, ":troop_no", 0),
        (party_add_members, "p_main_party", ":troop_no", 1),
        (str_store_troop_name, s6, ":troop_no"),
        (display_message, "@{s6} has joined your company."),
        (troop_set_note_available, ":troop_no", 1),
        
        (try_begin),
          (is_between, ":troop_no", companions_begin, companions_end),
          (store_sub, ":companion_number", ":troop_no", companions_begin),
          
          (set_achievement_stat, ACHIEVEMENT_KNIGHTS_OF_THE_ROUND, ":companion_number", 1),
          
          (assign, ":number_of_companions_hired", 0),
          (try_for_range, ":cur_companion", 0, 16),
            (get_achievement_stat, ":is_hired", ACHIEVEMENT_KNIGHTS_OF_THE_ROUND, ":cur_companion"),
            (eq, ":is_hired", 1),
            (val_add, ":number_of_companions_hired", 1),
          (try_end),
          
          (try_begin),
            (ge, ":number_of_companions_hired", 6),
            (unlock_achievement, ACHIEVEMENT_KNIGHTS_OF_THE_ROUND),
          (try_end),
        (try_end),
        #LAZERAS MODIFIED  {ENTK}
        # Jrider + TITLES v0.0 change companion title
        (store_troop_faction, ":faction_no", ":troop_no"),
        (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", ":troop_no", ":faction_no"),
        # Jrider -
        #LAZERAS MODIFIED  {ENTK}
    ]),
    
  
#TEMPERED  CHANGED SCRIPT FOR CAMP ENTRENCHMENT
  # script_setup_random_scene
  # Input: arg1 = center_no, arg2 = mission_template_no
  # Output: none
  ("setup_random_scene",
    [
		(party_get_current_terrain, ":terrain_type", "p_main_party"),
		(party_get_slot,":entrench","p_main_party",slot_party_entrenched),
		
		(assign, ":scene_to_use", "scn_random_scene"),
		(try_begin),
			(this_or_next|eq,":entrench",1),#entrenched camp
			(party_slot_eq,"p_main_party",slot_party_siege_camp,1),#entrenched siege camp
			(set_jump_mission,"mt_entrenched_encounter"),
			(assign,"$camp_supply",1), #Tempered  reset camp supplies before a battle
			(try_begin),
				(eq, ":terrain_type", rt_steppe),
				(assign, ":scene_to_use", "scn_entrenched_steppe"),
			(else_try),
				(eq, ":terrain_type", rt_plain),
				(assign, ":scene_to_use", "scn_entrenched_plain"),
			(else_try),
				(eq, ":terrain_type", rt_snow),
				(assign, ":scene_to_use", "scn_entrenched_snow"),
			(else_try),
				(eq, ":terrain_type", rt_desert),
				(assign, ":scene_to_use", "scn_entrenched_desert"),
			(else_try),
				(eq, ":terrain_type", rt_steppe_forest),
				(assign, ":scene_to_use", "scn_entrenched_steppe_forest"),
			(else_try),
				(eq, ":terrain_type", rt_forest),
				(assign, ":scene_to_use", "scn_entrenched_plain_forest"),
			(else_try),
				(eq, ":terrain_type", rt_snow_forest),
				(assign, ":scene_to_use", "scn_entrenched_snow_forest"),
			(else_try),
				(eq, ":terrain_type", rt_desert_forest),
				(assign, ":scene_to_use", "scn_entrenched_desert_forest"),
			(try_end),			
		(else_try),
			(eq,"$g_camp_mode", 1),#camping
			(neq,":entrench",1),#not entrenched
			(set_jump_mission,"mt_entrenched_encounter"),
			(assign,"$camp_supply",1), #Tempered  reset camp supplies before a battle
			(try_begin),
				(eq, ":terrain_type", rt_steppe),
				(assign, ":scene_to_use", "scn_not_entrenched_steppe"),
			(else_try),
				(eq, ":terrain_type", rt_plain),
				(assign, ":scene_to_use", "scn_not_entrenched_plain"),
			(else_try),
				(eq, ":terrain_type", rt_snow),
				(assign, ":scene_to_use", "scn_not_entrenched_snow"),
			(else_try),
				(eq, ":terrain_type", rt_desert),
				(assign, ":scene_to_use", "scn_not_entrenched_desert"),
			(else_try),
				(eq, ":terrain_type", rt_steppe_forest),
				(assign, ":scene_to_use", "scn_not_entrenched_steppe_forest"),
			(else_try),
				(eq, ":terrain_type", rt_forest),
				(assign, ":scene_to_use", "scn_not_entrenched_plain_forest"),
			(else_try),
				(eq, ":terrain_type", rt_snow_forest),
				(assign, ":scene_to_use", "scn_not_entrenched_snow_forest"),
			(else_try),
				(eq, ":terrain_type", rt_desert_forest),
				(assign, ":scene_to_use", "scn_not_entrenched_desert_forest"),
			(try_end),
		(else_try),
			(eq,":entrench",0),
			(eq,"$g_camp_mode", 0),
			(try_begin),
				(eq, ":terrain_type", rt_steppe),
				(assign, ":scene_to_use", "scn_random_scene_steppe"),
			(else_try),
				(eq, ":terrain_type", rt_plain),
				(assign, ":scene_to_use", "scn_random_scene_plain"),
			(else_try),
				(eq, ":terrain_type", rt_snow),
				(assign, ":scene_to_use", "scn_random_scene_snow"),
			(else_try),
				(eq, ":terrain_type", rt_desert),
				(assign, ":scene_to_use", "scn_random_scene_desert"),
			(else_try),
				(eq, ":terrain_type", rt_steppe_forest),
				(assign, ":scene_to_use", "scn_random_scene_steppe_forest"),
			(else_try),
				(eq, ":terrain_type", rt_forest),
				(assign, ":scene_to_use", "scn_random_scene_plain_forest"),
			(else_try),
				(eq, ":terrain_type", rt_snow_forest),
				(assign, ":scene_to_use", "scn_random_scene_snow_forest"),
			(else_try),
				(eq, ":terrain_type", rt_desert_forest),
				(assign, ":scene_to_use", "scn_random_scene_desert_forest"),
			(else_try),
				(eq, ":terrain_type", rt_water),
				(assign, ":scene_to_use", "scn_water"),
			(else_try),
				(eq, ":terrain_type", rt_bridge),
				(assign, ":scene_to_use", "scn_random_scene_plain"),
			(try_end),
		(try_end),
		(modify_visitors_at_site,":scene_to_use"),
		(reset_visitors),
		(jump_to_scene,":scene_to_use"),
  ]),
#TEMPERED CHANGES END
    
    # script_enter_dungeon
    # Input: arg1 = center_no, arg2 = mission_template_no
    # Output: none
    ("enter_dungeon",
      [
        (store_script_param_1, ":center_no"),
        (store_script_param_2, ":mission_template_no"),
        
        (set_jump_mission,":mission_template_no"),
        #new added...
        (mission_tpl_entry_set_override_flags, ":mission_template_no", 0, af_override_horse),
        (try_begin),
          (eq, "$sneaked_into_town", 1),
          (mission_tpl_entry_set_override_flags, ":mission_template_no", 0, af_override_all),
          
          (mission_tpl_entry_clear_override_items, ":mission_template_no", 0),
          (mission_tpl_entry_add_override_item, ":mission_template_no", 0, "itm_he_pla_pri_pilgrim"),
          (mission_tpl_entry_add_override_item, ":mission_template_no", 0, "itm_ar_pla_pri_pilgrimdisguise"),
          (mission_tpl_entry_add_override_item, ":mission_template_no", 0, "itm_practice_staff"),
          (mission_tpl_entry_add_override_item, ":mission_template_no", 0, "itm_we_vae_sword_throw_daggers"),
        (try_end),
        #new added end
        
        (party_get_slot, ":dungeon_scene", ":center_no", slot_town_prison),
        
        (modify_visitors_at_site,":dungeon_scene"),
        (reset_visitors),
        (assign, ":cur_pos", 16),
        
        
        (call_script, "script_get_heroes_attached_to_center_as_prisoner", ":center_no", "p_temp_party"),
		  (party_get_num_companion_stacks, ":num_stacks","p_temp_party"),
		  ##diplomacy start+ Allow some variation in which prisoners appear,
		  #when there are too many to all fit in the jail at once.
		  (try_begin),
				(gt, ":num_stacks", 15),
				(store_random_in_range, ":offset", 0, ":num_stacks"),
		  (else_try),
				(assign, ":offset", 0),
		  (try_end),
		  ##diplomacy end+
		  (try_for_range, ":i_stack", 0, ":num_stacks"),
		  ##diplomacy start+
			(val_add, ":i_stack", ":offset"),
			(try_begin),
			   (ge, ":i_stack", ":num_stacks"),
			   (val_sub, ":i_stack", ":num_stacks"),
			(try_end),
		  ##diplomacy end+
			(party_stack_get_troop_id, ":stack_troop","p_temp_party",":i_stack"),
          
          (assign, ":prisoner_offered_parole", 0),
          (try_begin),
            (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
          (else_try),
            (call_script, "script_cf_prisoner_offered_parole", ":stack_troop"),
            (assign, ":prisoner_offered_parole", 1),
          (else_try),
            (assign, ":prisoner_offered_parole", 0),
          (try_end),
          (eq, ":prisoner_offered_parole", 0),
          
          (lt, ":cur_pos", 32), # spawn up to entry point 32
          (set_visitor, ":cur_pos", ":stack_troop"),
          (val_add,":cur_pos", 1),
        (try_end),
        
        #	  (set_visitor, ":cur_pos", "trp_npc3"),
        #	  (troop_set_slot, "trp_npc3", slot_troop_prisoner_of_party, "$g_encountered_party"),
        
        (set_jump_entry, 0),
        (jump_to_scene,":dungeon_scene"),
        (scene_set_slot, ":dungeon_scene", slot_scene_visited, 1),
        (change_screen_mission),
    ]),
    
    # script_enter_court
    # Input: arg1 = center_no
    # Output: none
    #other search term: setup_court
    ("enter_court",
      [
        (store_script_param_1, ":center_no"),
        
        (assign, "$talk_context", tc_court_talk),
        
        (set_jump_mission,"mt_visit_town_castle"),
        
        (mission_tpl_entry_clear_override_items, "mt_visit_town_castle", 0),
        #(mission_tpl_entry_set_override_flags, "mt_visit_town_castle", 0, af_override_all),
        
        (party_get_slot, ":castle_scene", ":center_no", slot_town_castle),
        (modify_visitors_at_site,":castle_scene"),
        (reset_visitors),
        #Adding guards
        (store_faction_of_party, ":center_faction", ":center_no"),
        (faction_get_slot, ":guard_troop", ":center_faction", slot_faction_guard_troop),
        ##diplomacy begin
        (try_begin),
          (eq, ":center_faction", "$players_kingdom"), #Diplomacy 3.3.2
          (is_between, "$g_player_culture", kingdoms_begin, kingdoms_end), #Player Faction
          (faction_get_slot, ":guard_troop", "$g_player_culture", slot_faction_guard_troop),
		##nested diplomacy start+
	  (else_try),
	     #Reflect multicultural empires.
		 (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
		 (gt, ":town_lord", "trp_player"),
		 (troop_get_slot, ":lord_original_faction", ":town_lord", slot_troop_original_faction),
		 (neq, ":lord_original_faction", ":center_faction"),
		 (is_between, ":lord_original_faction", npc_kingdoms_begin, npc_kingdoms_end),
		 (this_or_next|party_slot_eq, ":center_no", slot_center_original_faction, ":lord_original_faction"),
			(troop_slot_eq, ":town_lord", slot_troop_home, ":center_no"),
		 (faction_get_slot, ":guard_troop", ":lord_original_faction", slot_faction_guard_troop),
	  ##nested diplomacy end+
      (try_end),
        ##diplomacy end
        (try_begin),
          (le, ":guard_troop", 0),
			##Floris MTT begin
			(troop_get_slot,":swadian_guard","$troop_trees",slot_swadian_guard),
			(assign, ":guard_troop", ":swadian_guard"),															#Not changed for Diplo+, since this serves MTT better
			##Floris MTT end
        (try_end),
        (set_visitor, 6, ":guard_troop"),
        (set_visitor, 7, ":guard_troop"),
        
        (assign, ":cur_pos", 16),
        
        (try_begin),
          (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
          (gt, ":player_spouse", 0),
          (troop_slot_eq, ":player_spouse", slot_troop_cur_center, ":center_no"),
          (set_visitor, ":cur_pos", ":player_spouse"),
          (val_add,":cur_pos", 1),
        (else_try),
          (troop_get_slot, ":player_betrothed", "trp_player", slot_troop_betrothed),
          (gt, ":player_betrothed", 0),
          (troop_slot_eq, ":player_betrothed", slot_troop_cur_center, ":center_no"),
          (set_visitor, ":cur_pos", ":player_betrothed"),
          (val_add,":cur_pos", 1),
        (try_end),
        
        (try_begin),
          (eq, "$g_player_court", ":center_no"),
          (gt, "$g_player_minister", 0),
          (neg|troop_slot_eq, "trp_player", slot_troop_spouse, "$g_player_minister"),
          (set_visitor, ":cur_pos", "$g_player_minister"),
          (val_add,":cur_pos", 1),
        (try_end),
        ##diplomacy begin
        (try_begin),
          (gt, "$g_player_chamberlain", 0),
          (call_script, "script_dplmc_appoint_chamberlain"),  #fix for wrong troops after update
          (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
          (eq, ":town_lord", "trp_player"),
          (set_visitor, ":cur_pos", "$g_player_chamberlain"),
          (val_add,":cur_pos", 1),
        (try_end),
        
        (try_begin),
          (gt, "$g_player_constable", 0),
          (call_script, "script_dplmc_appoint_constable"),  #fix for wrong troops after update
          (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
          (eq, ":town_lord", "trp_player"),
          (set_visitor, ":cur_pos", "$g_player_constable"),
          (val_add,":cur_pos", 1),
        (try_end),
        
        (try_begin),
          (gt, "$g_player_chancellor", 0),
          (call_script, "script_dplmc_appoint_chancellor"), #fix for wrong troops after update
          (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
          (eq, ":town_lord", "trp_player"),
          (set_visitor, ":cur_pos", "$g_player_chancellor"),
          (val_add,":cur_pos", 1),
        (try_end),
        ##diplomacy end
		
		#Custom troops master hired // at court
        (try_begin),
		  (troop_slot_eq, "trp_custom_master", slot_troop_state, 1), 
		  (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
          (set_visitor, ":cur_pos", "trp_custom_master"),
          (val_add,":cur_pos", 1),
        (try_end),		
        #Custom troops end
		
		  #Lords wishing to pledge allegiance - inactive, but part of player faction
		  (try_begin),
			(eq, "$g_player_court", ":center_no"),
			(faction_slot_eq, ":center_faction", slot_faction_leader, "trp_player"),
			##diplomacy start+
			#It's not exactly clear if this would work for kingdom ladies.  If they
			#can go from slto_kingdom_lady to slto_inactive, this could take them
			#from there to slto_kingdom_hero unintentionally.
			#
			#Because of this, don't enable this for now.  Elsewhere (where defections
			#occur) add alternate behavior for promoted kingdom ladies.
			#
			#TODO: Later, make sure that kingdom ladies are never inactive normally,
			#so this loop can be expanded to work with them.
			##diplomacy end+
			(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
			  (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
			  (eq, ":active_npc_faction", "fac_player_supporters_faction"),
			  (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_inactive),
			  (neg|troop_slot_ge, ":active_npc", slot_troop_prisoner_of_party, 0), #if he/she is not prisoner in any center.
			  (neq, ":active_npc", "$g_player_minister"),
			  (set_visitor, ":cur_pos", ":active_npc"),
			  (val_add,":cur_pos", 1),
			(try_end),
		  (try_end),

		  ##diplomacy start+
		  #Show heroes you haven't seen recently first, to deal with crowded feast halls
		  #(call_script, "script_get_heroes_attached_to_center", ":center_no", "p_temp_party"),
		  (call_script, "script_dplmc_time_sorted_heroes_for_center", ":center_no", "p_temp_party"),
		  #Reserve a certain number of feast positions for ladies, both for practical
		  #reasons of courtship and for visual variety.
		  (try_begin),
			#If the player is unmarried, reserve zero to 8 slots for women
			(lt, ":player_spouse", 1),
			(store_random_in_range, ":reserved", 0, 9),
		  (else_try),
			#If the player is married, reserve zero to four slots for women
			(store_random_in_range, ":reserved", 0, 5),
		  (try_end),
		  (store_sub, ":non_lady_max", 32, ":reserved"),
		  #diplomacy end+
		  (party_get_num_companion_stacks, ":num_stacks","p_temp_party"),
		  (try_for_range, ":i_stack", 0, ":num_stacks"),
			(party_stack_get_troop_id, ":stack_troop","p_temp_party",":i_stack"),
			##diplomacy start+
			#(lt, ":cur_pos", 32), # spawn up to entry point 32 - is it possible to add another 10 spots?
			(lt, ":cur_pos", ":non_lady_max"),#Leave some room for ladies in huge feasts
			##diplomacy end+
			(set_visitor, ":cur_pos", ":stack_troop"),
			(val_add,":cur_pos", 1),
		  (try_end),
		  (try_for_range, ":cur_troop", kingdom_ladies_begin, kingdom_ladies_end),
			(neq, ":cur_troop", "trp_knight_1_1_wife"), #The one who should not appear in game
			#(troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_lady),
			(troop_slot_eq, ":cur_troop", slot_troop_cur_center, ":center_no"),
			
			(assign, ":lady_meets_visitors", 0),
			(try_begin),
				(this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, ":cur_troop"), #player spouse goes in position of honor
				(this_or_next|troop_slot_eq, "trp_player", slot_troop_betrothed, ":cur_troop"), #player spouse goes in position of honor
				(this_or_next|troop_slot_eq, ":cur_troop", slot_troop_spouse, "trp_player"), #player spouse goes in position of honor
					(troop_slot_eq, ":cur_troop", slot_troop_betrothed, "trp_player"),

				(assign, ":lady_meets_visitors", 0), #She is already in the place of honor

				(try_begin),
					(eq, "$cheat_mode", 1),
					(str_store_troop_name, s4, ":cur_troop"),
					(display_message, "str_s4_is_present_at_the_center_and_in_place_of_honor"),
				(try_end),

			(else_try), #lady is troop
				(store_faction_of_troop, ":lady_faction", ":cur_troop"),
				(neq, ":lady_faction", ":center_faction"),

				(assign, ":lady_meets_visitors", 1),


				(try_begin),
					(eq, "$cheat_mode", 1),
					(str_store_troop_name, s4, ":cur_troop"),
					(display_message, "str_s4_is_present_at_the_center_as_a_refugee"),
				(try_end),

			(else_try),
				(troop_slot_ge, ":cur_troop", slot_troop_spouse, 1),

				(try_begin),
				 #married ladies at a feast will not mingle - this is ahistorical, as married women and widows probably had much more freedom than unmarried ones, at least in the West, but the game needs to leave slots for them to show off their unmarried daughters
					(faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
					(faction_slot_eq, ":center_faction", slot_faction_ai_object, ":center_no"),
					(assign, ":lady_meets_visitors", 0),

					(try_begin),
						(eq, "$cheat_mode", 1),
						(str_store_troop_name, s4, ":cur_troop"),
						(display_message, "str_s4_is_present_at_the_center_and_not_attending_the_feast"),
					(try_end),
				(else_try),
					(assign, ":lady_meets_visitors", 1),

					(try_begin),
						(eq, "$cheat_mode", 1),
						(str_store_troop_name, s4, ":cur_troop"),
						(display_message, "str_s4_is_present_at_the_center_and_is_married"),
					(try_end),
				(try_end),

			(else_try), #feast is in progress
				(faction_slot_eq, ":center_faction", slot_faction_ai_state, sfai_feast),
				(faction_slot_eq, ":center_faction", slot_faction_ai_object, ":center_no"),
				(assign, ":lady_meets_visitors", 1),

				(try_begin),
					(eq, "$cheat_mode", 1),
					(str_store_troop_name, s4, ":cur_troop"),
					(display_message, "@{!}DEBUG -- {s4} is present at the center and is attending the feast"),
				(try_end),

			(else_try), #already met - awaits in private
				(troop_slot_ge, ":cur_troop", slot_troop_met, 2),
				(assign, ":lady_meets_visitors", 0),

				(try_begin),
					(eq, "$cheat_mode", 1),
					(str_store_troop_name, s4, ":cur_troop"),
					(display_message, "@{!}DEBUG -- {s4} is present at the center and is awaiting the player in private"),
				(try_end),

			(else_try),
				(call_script, "script_get_kingdom_lady_social_determinants", ":cur_troop"),
				(call_script, "script_npc_decision_checklist_male_guardian_assess_suitor", reg0, "trp_player"),
				(gt, reg0, 0),
				(assign, ":lady_meets_visitors", 1),

				(try_begin),
					(eq, "$cheat_mode", 1),
					(str_store_troop_name, s4, ":cur_troop"),
					(display_message, "@{!}DEBUG -- {s4} is_present_at_the_center_and_is_allowed_to_meet_the_player"),
				(try_end),

			(else_try),
				(try_begin),
					(eq, "$cheat_mode", 1),
					(str_store_troop_name, s4, ":cur_troop"),
					(display_message, "@{!}DEBUG -- {s4}is_present_at_the_center_and_is_not_allowed_to_meet_the_player"),
				(try_end),

			(try_end),

			(eq, ":lady_meets_visitors", 1),

			(lt, ":cur_pos", 32), # spawn up to entry point 32
			(set_visitor, ":cur_pos", ":cur_troop"),
			(val_add,":cur_pos", 1),
		  (try_end),

		  (set_jump_entry, 0),

		  (jump_to_scene,":castle_scene"),
		  (scene_set_slot, ":castle_scene", slot_scene_visited, 1),
		  (change_screen_mission),
	  ]),
    
    
    ("setup_meet_lady",
      [
        (store_script_param_1, ":lady_no"),
        (store_script_param_2, ":center_no"),
        
        #(mission_tpl_entry_set_override_flags, "mt_visit_town_castle", 0, af_override_horse),
        (troop_set_slot, ":lady_no", slot_lady_last_suitor, "trp_player"),
        
        (set_jump_mission,"mt_visit_town_castle"),
        (party_get_slot, ":castle_scene", ":center_no", slot_town_castle),
        (modify_visitors_at_site,":castle_scene"),
        (reset_visitors),
        
        (troop_set_age, "trp_nurse_for_lady", 100),
        (set_visitor, 7, "trp_nurse_for_lady"),
        
        (assign, ":cur_pos", 16),
        (set_visitor, ":cur_pos", ":lady_no"),
        
        (assign, "$talk_context", tc_garden),
        
        (jump_to_scene,":castle_scene"),
        (scene_set_slot, ":castle_scene", slot_scene_visited, 1),
        (change_screen_mission),
    ]),
    
    # script_find_high_ground_around_pos1
    # Input: pos1 should hold center_position_no
    #        arg1: team_no
    #        arg2: search_radius (in meters)
    # Output: pos52 contains highest ground within <search_radius> meters of team leader
    # Destroys position registers: pos10, pos11, pos15
    ("find_high_ground_around_pos1",
      [
        (store_script_param, ":team_no", 1),
        (store_script_param, ":search_radius", 2),
        (val_mul, ":search_radius", 100),
        (get_scene_boundaries, pos10,pos11),
        (team_get_leader, ":ai_leader", ":team_no"),
        (agent_get_position, pos1, ":ai_leader"),
        (set_fixed_point_multiplier, 100),
        (position_get_x, ":o_x", pos1),
        (position_get_y, ":o_y", pos1),
        (store_sub, ":min_x", ":o_x", ":search_radius"),
        (store_sub, ":min_y", ":o_y", ":search_radius"),
        (store_add, ":max_x", ":o_x", ":search_radius"),
        (store_add, ":max_y", ":o_y", ":search_radius"),
        (position_get_x, ":scene_min_x", pos10),
        (position_get_x, ":scene_max_x", pos11),
        (position_get_y, ":scene_min_y", pos10),
        (position_get_y, ":scene_max_y", pos11),
        #do not find positions close to borders (20 m)
        (val_add, ":scene_min_x", 2000),
        (val_sub, ":scene_max_x", 2000),
        (val_add, ":scene_min_y", 2000),
        (val_sub, ":scene_max_y", 2000),
        (val_max, ":min_x", ":scene_min_x"),
        (val_max, ":min_y", ":scene_min_y"),
        (val_min, ":max_x", ":scene_max_x"),
        (val_min, ":max_y", ":scene_max_y"),
        
        (store_div, ":min_x_meters", ":min_x", 100),
        (store_div, ":min_y_meters", ":min_y", 100),
        (store_div, ":max_x_meters", ":max_x", 100),
        (store_div, ":max_y_meters", ":max_y", 100),
        
        (assign, ":highest_pos_z", -10000),
        (copy_position, pos52, pos1),
        (init_position, pos15),
        
        (try_for_range, ":i_x", ":min_x_meters", ":max_x_meters"),
          (store_mul, ":i_x_cm", ":i_x", 100),
          (try_for_range, ":i_y", ":min_y_meters", ":max_y_meters"),
            (store_mul, ":i_y_cm", ":i_y", 100),
            (position_set_x, pos15, ":i_x_cm"),
            (position_set_y, pos15, ":i_y_cm"),
            (position_set_z, pos15, 10000),
            (position_set_z_to_ground_level, pos15),
            (position_get_z, ":cur_pos_z", pos15),
            (try_begin),
              (gt, ":cur_pos_z", ":highest_pos_z"),
              (copy_position, pos52, pos15),
              (assign, ":highest_pos_z", ":cur_pos_z"),
            (try_end),
          (try_end),
        (try_end),
    ]),
    
    # script_select_battle_tactic
    # Input: none
    # Output: none
    ("select_battle_tactic",
      [
        (assign, "$ai_team_1_battle_tactic", 0),
        (get_player_agent_no, ":player_agent"),
        (agent_get_team, ":player_team", ":player_agent"),
        (try_begin),
          (num_active_teams_le, 2),
          (try_begin),
            (eq, ":player_team", 0),
            (assign, "$ai_team_1", 1),
          (else_try),
            (assign, "$ai_team_1", 0),
          (try_end),
          (assign, "$ai_team_2", -1),
        (else_try),
          (try_begin),
            (eq, ":player_team", 0),
            (assign, "$ai_team_1", 1),
          (else_try),
            (assign, "$ai_team_1", 0),
          (try_end),
          (store_add, "$ai_team_2", ":player_team", 2),
        (try_end),
        (call_script, "script_select_battle_tactic_aux", "$ai_team_1", 0),
        (assign, "$ai_team_1_battle_tactic", reg0),
        (try_begin),
          (ge, "$ai_team_2", 0),
          (assign, ":defense_not_an_option", 0),
          (try_begin),
            (eq, "$ai_team_1_battle_tactic", btactic_hold),
            (assign, ":defense_not_an_option", 1), #don't let two AI defend at the same time
          (try_end),
          (call_script, "script_select_battle_tactic_aux", "$ai_team_2", ":defense_not_an_option"),
          (assign, "$ai_team_2_battle_tactic", reg0),
        (try_end),
    ]),
    
    # script_select_battle_tactic_aux
    # Input: team_no
    # Output: battle_tactic
    ("select_battle_tactic_aux",
      [
        (store_script_param, ":team_no", 1),
        (store_script_param, ":defense_not_an_option", 2),
        (assign, ":battle_tactic", 0),
        (get_player_agent_no, ":player_agent"),
        (agent_get_team, ":player_team", ":player_agent"),
#TEMPERED CHANGED FOR PLAYER ENTRENCHMENT
	  (party_get_slot,":entrench","p_main_party",slot_party_entrenched),
	  (try_begin),
		(party_slot_eq,"p_main_party",slot_party_siege_camp,1),
        (teams_are_enemies, ":team_no", ":player_team"),
        (assign, ":defense_not_an_option", 1),		
	  (try_end),
      (try_begin),
        (this_or_next|eq, "$cant_leave_encounter", 1),
		(eq,":entrench",1),
#TEMPERED CHANGES END
          (teams_are_enemies, ":team_no", ":player_team"),
          (assign, ":defense_not_an_option", 1),
        (try_end),
        (call_script, "script_team_get_class_percentages", ":team_no", 0),
        #      (assign, ":ai_perc_infantry", reg0),
        (assign, ":ai_perc_archers",  reg1),
        (assign, ":ai_perc_cavalry",  reg2),
        (call_script, "script_team_get_class_percentages", ":team_no", 1),#enemies of the ai_team
        #      (assign, ":enemy_perc_infantry", reg0),
        #      (assign, ":enemy_perc_archers",  reg1),
        #      (assign, ":enemy_perc_cavalry",  reg2),
        
        (store_random_in_range, ":rand", 0, 100),
        (try_begin),
          (assign, ":continue", 0),
          (try_begin),
            (teams_are_enemies, ":team_no", ":player_team"),
            (party_slot_eq, "$g_enemy_party", slot_party_type, spt_kingdom_hero_party),
            (assign, ":continue", 1),
          (else_try),
            (neg|teams_are_enemies, ":team_no", ":player_team"),
            (gt, "$g_ally_party", 0),
            (party_slot_eq, "$g_ally_party", slot_party_type, spt_kingdom_hero_party),
            (assign, ":continue", 1),
          (try_end),
          #(this_or_next|lt, ":rand", 20),
          (eq, ":continue", 1),
          (store_faction_of_party, ":enemy_faction_no", "$g_enemy_party"),
          (neq, ":enemy_faction_no", "fac_kingdom_3"), #don't let khergits use battle tactics
          (try_begin),
            (eq, ":defense_not_an_option", 0),
            (gt, ":ai_perc_archers", 50),
            (lt, ":ai_perc_cavalry", 35),
            (assign, ":battle_tactic", btactic_hold),
          (else_try),
            (lt, ":rand", 80),
            (assign, ":battle_tactic", btactic_follow_leader),
          (try_end),
        (try_end),
        (assign, reg0, ":battle_tactic"),
    ]),
    
    # script_battle_calculate_initial_powers
    # Input: none
    # Output: none
    #("battle_calculate_initial_powers",
    #  [
    #    (try_for_agents, ":agent_no"),
    #      (agent_is_human, ":agent_no"),
    #
    #      (call_script, "script_calculate_team_powers", ":agent_no"),
    #      (assign, ":ally_power", reg0),
    #      (assign, ":enemy_power", reg1),
    #
    #      (agent_set_slot, ":agent_no", slot_agent_initial_ally_power, ":ally_power"),
    #      (agent_set_slot, ":agent_no", slot_agent_initial_enemy_power, ":enemy_power"),
    #    (try_end),
    #]),
    
    # script_battle_tactic_init
    # Input: none
    # Output: none
    ("battle_tactic_init",
      [
        (call_script, "script_battle_tactic_init_aux", "$ai_team_1", "$ai_team_1_battle_tactic"),
        (try_begin),
          (ge, "$ai_team_2", 0),
          (call_script, "script_battle_tactic_init_aux", "$ai_team_2", "$ai_team_2_battle_tactic"),
        (try_end),
        
        (try_for_agents, ":cur_agent"),
          (agent_set_slot, ":cur_agent",  slot_agent_is_running_away, 0), #initially nobody is running away.
        (try_end),
    ]),
    
    # script_battle_tactic_init_aux
    # Input: team_no, battle_tactic
    # Output: none
    ("battle_tactic_init_aux",
      [
        (store_script_param, ":team_no", 1),
        (store_script_param, ":battle_tactic", 2),
        (team_get_leader, ":ai_leader", ":team_no"),
        (try_begin),
          (eq, ":battle_tactic", btactic_hold),
          (agent_get_position, pos1, ":ai_leader"),
          (call_script, "script_find_high_ground_around_pos1", ":team_no", 30),
          (copy_position, pos1, pos52),
          (call_script, "script_find_high_ground_around_pos1", ":team_no", 30), # call again just in case we are not at peak point.
          (copy_position, pos1, pos52),
          (call_script, "script_find_high_ground_around_pos1", ":team_no", 30), # call again just in case we are not at peak point.
          (team_give_order, ":team_no", grc_everyone, mordr_hold),
          (team_set_order_position, ":team_no", grc_everyone, pos52),
          (team_give_order, ":team_no", grc_archers, mordr_advance),
          (team_give_order, ":team_no", grc_archers, mordr_advance),
        (else_try),
          (eq, ":battle_tactic", btactic_follow_leader),
          (team_get_leader, ":ai_leader", ":team_no"),
          (ge, ":ai_leader", 0),
          (agent_set_speed_limit, ":ai_leader", 8),
          (agent_get_position, pos60, ":ai_leader"),
          (team_give_order, ":team_no", grc_everyone, mordr_hold),
          (team_set_order_position, ":team_no", grc_everyone, pos60),
        (try_end),
    ]),
    
    # script_calculate_team_powers
    # Input: none
    # Output: ally_power, enemy_power
    ("calculate_team_powers",
      [
        (store_script_param, ":agent_no", 1),
        
        (try_begin),
          (assign, ":agent_side", 0),
          (agent_is_ally, ":agent_no"),
          (assign, ":agent_side", 1),
        (try_end),
        
        (assign, ":ally_power", 0),
        (assign, ":enemy_power", 0),
        
        (try_for_agents, ":cur_agent"),
          (agent_is_human, ":cur_agent"),
          (agent_is_alive, ":cur_agent"),
          
          (try_begin),
            (assign, ":agent_side_cur", 0),
            (agent_is_ally, ":cur_agent"),
            (assign, ":agent_side_cur", 1),
          (try_end),
          
          (try_begin),
            (agent_get_horse, ":agent_horse_id", ":cur_agent"),
            (neq, ":agent_horse_id", -1),
            (assign, ":agent_power", 2), #if this agent is horseman then his power effect is 2
          (else_try),
            (assign, ":agent_power", 1), #if this agent is walker then his power effect is 1
          (try_end),
          
          (try_begin),
            (eq, ":agent_side", ":agent_side_cur"),
            (val_add, ":ally_power", ":agent_power"),
          (else_try),
            (val_add, ":enemy_power", ":agent_power"),
          (try_end),
        (try_end),
        
        (assign, reg0, ":ally_power"),
        (assign, reg1, ":enemy_power"),
    ]), #ozan
    
    # script_apply_effect_of_other_people_on_courage_scores
    # Input: none
    # Output: none
  ("apply_effect_of_other_people_on_courage_scores",
    [
      (get_player_agent_no, ":player_agent"),

      (try_for_agents, ":centered_agent_no"),
        (agent_is_human, ":centered_agent_no"),
        (agent_is_alive, ":centered_agent_no"),
        (neq, ":centered_agent_no", ":player_agent"),
        (agent_get_position, pos0, ":centered_agent_no"),
        (try_begin),
          (agent_is_ally, ":centered_agent_no"),
          (assign, ":is_centered_agent_ally", 1),
        (else_try),
          (assign, ":is_centered_agent_ally", 0),
        (try_end),
       
        (try_for_agents, ":agent_no"),
          (agent_is_human, ":agent_no"),
          (agent_is_alive, ":agent_no"),
          (neq, ":centered_agent_no", ":agent_no"),      

          (try_begin),
            (agent_is_ally, ":agent_no"),
            (assign, ":is_agent_ally", 1),
          (else_try),
            (assign, ":is_agent_ally", 0),
          (try_end),

          (eq, ":is_centered_agent_ally", ":is_agent_ally"), #if centered agent and other agent is at same team then continue.
          (agent_get_slot, ":agent_is_running_away_or_not", ":agent_no", slot_agent_is_running_away),

          (try_begin),
            (eq, ":agent_no", ":player_agent"),
            (assign, ":agent_delta_courage_score", 6),
          (else_try),
            (agent_get_troop_id, ":troop_id", ":agent_no"),
            (troop_is_hero, ":troop_id"),
      
            #Hero Agent : if near agent (hero, agent_no) is not running away his positive effect on centered agent (centered_agent_no) fighting at his side is effected by his hit points.
            (try_begin),      
              (neq, ":agent_is_running_away_or_not", 1), #if agent is not running away
              (store_agent_hit_points, ":agent_hit_points", ":agent_no"),
              (try_begin),
                (eq, ":agent_hit_points", 100),
                (assign, ":agent_delta_courage_score", 6),
              (else_try),
                (ge, ":agent_hit_points", 75),
                (assign, ":agent_delta_courage_score", 5),
              (else_try),
                (ge, ":agent_hit_points", 60),
                (assign, ":agent_delta_courage_score", 4),
              (else_try),
                (ge, ":agent_hit_points", 45),
                (assign, ":agent_delta_courage_score", 3),
              (else_try),
                (ge, ":agent_hit_points", 30),
                (assign, ":agent_delta_courage_score", 2),
              (else_try),
                (ge, ":agent_hit_points", 15),
                (assign, ":agent_delta_courage_score", 1),
              (try_end),
            (else_try),
              (assign, ":agent_delta_courage_score", 4),
            (try_end),
          (else_try),
            #Normal Agent : if near agent (agent_no) is not running away his positive effect on centered agent (centered_agent_no) fighting at his side is effected by his hit points.
            (try_begin),      
              (neq, ":agent_is_running_away_or_not", 1), # if agent is not running away
              (store_agent_hit_points, ":agent_hit_points", ":agent_no"),
              (try_begin),
                (eq, ":agent_hit_points", 100),
                (assign, ":agent_delta_courage_score", 4),
              (else_try),
                (ge, ":agent_hit_points", 75),
                (assign, ":agent_delta_courage_score", 3),
              (else_try),
                (ge, ":agent_hit_points", 50),
                (assign, ":agent_delta_courage_score", 2),
              (else_try),
                (ge, ":agent_hit_points", 25),
                (assign, ":agent_delta_courage_score", 1),
              (try_end),
              (try_begin), # to make our warrior run away easier we decrease one, because they have player_agent (+6) advantage.
                (agent_is_ally, ":agent_no"),
                (val_sub, ":agent_delta_courage_score", 1),
              (try_end),
            (else_try),
              (assign, ":agent_delta_courage_score", 2),
            (try_end),
          (try_end),
      
          (try_begin),
            (neq, ":agent_is_running_away_or_not", 1),
            (val_mul, ":agent_delta_courage_score", 1),
            (try_begin), # centered agent not running away cannot take positive courage score from one another agent not running away.
              (agent_get_slot, ":agent_is_running_away_or_not", ":centered_agent_no", slot_agent_is_running_away),
              (eq, ":agent_is_running_away_or_not", 0),
              (val_mul, ":agent_delta_courage_score", 0),
            (try_end),
          (else_try),
            (try_begin), 
              (agent_get_slot, ":agent_is_running_away_or_not", ":agent_no", slot_agent_is_running_away),
              (eq, ":agent_is_running_away_or_not", 0),
              (val_mul, ":agent_delta_courage_score", -2), # running away agent fears not running away agent more.
            (else_try),
              (val_mul, ":agent_delta_courage_score", -1),
            (try_end),
          (try_end),

          (neq, ":agent_delta_courage_score", 0),

          (agent_get_position, pos1, ":agent_no"),
          (get_distance_between_positions, ":dist", pos0, pos1),

          (try_begin),
            (ge, ":agent_delta_courage_score", 0),
            (try_begin),
              (lt, ":dist", 2000), #0-20 meter
              (agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
              (val_mul, ":agent_delta_courage_score", 50),
              (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
              (agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),           
            (else_try),
              (lt, ":dist", 4000), #21-40 meter
              (agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
              (val_mul, ":agent_delta_courage_score", 40),
              (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
              (agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),           
            (else_try),
              (lt, ":dist", 7000), #41-70 meter
              (agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
              (val_mul, ":agent_delta_courage_score", 30),
              (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
              (agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),           
            (else_try),
              (lt, ":dist", 11000), #71-110 meter
              (agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
              (val_mul, ":agent_delta_courage_score", 20),
              (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
              (agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),           
            (else_try),      
              (lt, ":dist", 16000), # 111-160 meter, assumed that eye can see agents friendly at most 160 meters far while fighting. 
                                    # this is more than below limit (108 meters) because we hear that allies come from further.
              (agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
              (val_mul, ":agent_delta_courage_score", 10),
              (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
              (agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),           
            (try_end),      
          (else_try),                                               # negative effect of running agent on other ally agents are lower then positive effects above, to avoid starting  
            (try_begin),                                            # run away of all agents at a moment. I want to see agents running away one by one during battle, not all together.
              (lt, ":dist", 200), #1-2 meter,                       # this would create better game play.
              (agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
              (val_mul, ":agent_delta_courage_score", 15),
              (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
              (agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),           
            (else_try),
              (lt, ":dist", 400), #3-4 meter, 
              (agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
              (val_mul, ":agent_delta_courage_score", 13),
              (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
              (agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),           
            (else_try),
              (lt, ":dist", 600), #5-6 meter
              (agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
              (val_mul, ":agent_delta_courage_score", 11),
              (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
              (agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),           
            (else_try),
              (lt, ":dist", 800), #7-8 meter
              (agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
              (val_mul, ":agent_delta_courage_score", 9),
              (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
              (agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),           
            (else_try),
              (lt, ":dist", 1200), #9-12 meters
              (agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
              (val_mul, ":agent_delta_courage_score", 7),
              (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
              (agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),           
            (else_try),
              (lt, ":dist", 2400), #13-24 meters
              (agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
              (val_mul, ":agent_delta_courage_score", 5),
              (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
              (agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),           
            (else_try),
              (lt, ":dist", 4800), #25-48 meters
              (agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
              (val_mul, ":agent_delta_courage_score", 3),
              (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
              (agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),           
            (else_try),
              (lt, ":dist", 9600), #49-98 meters, assumed that eye can see agents running away at most 98 meters far while fighting.
              (agent_get_slot, ":agent_courage_score", ":centered_agent_no", slot_agent_courage_score),
              (val_mul, ":agent_delta_courage_score", 1),
              (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
              (agent_set_slot, ":centered_agent_no", slot_agent_courage_score, ":agent_courage_score"),           
            (try_end),      
          (try_end),
        (try_end), #Nested Agent Loop           
      (try_end), #Agent Loop
    ]), #ozan
        
        
        # script_apply_death_effect_on_courage_scores
        # Input: dead agent id, killer agent id
        # Output: none
        ("apply_death_effect_on_courage_scores",
          [
            (store_script_param, ":dead_agent_no", 1),
            (store_script_param, ":killer_agent_no", 2),
            
            (try_begin),
              (agent_is_human, ":dead_agent_no"),
              
              (try_begin),
                (agent_is_ally, ":dead_agent_no"),
                (assign, ":is_dead_agent_ally", 1),
              (else_try),
                (assign, ":is_dead_agent_ally", 0),
              (try_end),
              
              (agent_get_position, pos0, ":dead_agent_no"),
              (assign, ":number_of_near_allies_to_dead_agent", 0),
              
              (try_for_agents, ":agent_no"),
                (agent_is_human, ":agent_no"),
                (agent_is_alive, ":agent_no"),
                
                (agent_get_position, pos1, ":agent_no"),
                (get_distance_between_positions, ":dist", pos0, pos1),
                
                (le, ":dist", 1300), # to count number of allies within 13 meters to dead agent.
                
                (try_begin),
                  (agent_is_ally, ":agent_no"),
                  (assign, ":is_agent_ally", 1),
                (else_try),
                  (assign, ":is_agent_ally", 0),
                (try_end),
                
                (try_begin),
                  (eq, ":is_dead_agent_ally", ":is_agent_ally"),
                  (val_add, ":number_of_near_allies_to_dead_agent", 1), # (number_of_near_allies_to_dead_agent) is counted because if there are
                (try_end),                                              # many allies of dead agent around him, negative courage effect become less.
              (try_end),
              
              (try_for_agents, ":agent_no"),
                (agent_is_human, ":agent_no"),
                (agent_is_alive, ":agent_no"),
                
                (try_begin),
                  (agent_is_ally, ":agent_no"),
                  (assign, ":is_agent_ally", 1),
                (else_try),
                  (assign, ":is_agent_ally", 0),
                (try_end),
                
                (try_begin), # each agent is effected by a killed agent positively if he is rival or negatively if he is ally.
                  (neq, ":is_dead_agent_ally", ":is_agent_ally"),
                  (assign, ":agent_delta_courage_score", 10),  # if killed agent is agent of rival side, add points to fear score
                (else_try),
                  (assign, ":agent_delta_courage_score", -15), # if killed agent is agent of our side, decrease points from fear score
                  (val_add, ":agent_delta_courage_score", ":number_of_near_allies_to_dead_agent"), # ":number_of_near_allies_to_dead_agent" is added because if there are many
                  (try_begin),                                                                     # allies of dead agent around him, negative courage effect become less.
                    (gt, ":agent_delta_courage_score", -5),
                    (assign, ":agent_delta_courage_score", -5),
                  (try_end),
                  
                  (agent_get_slot, ":dead_agent_was_running_away_or_not", ":dead_agent_no",  slot_agent_is_running_away), #look dead agent was running away or not.
                  (try_begin),
                    (eq, ":dead_agent_was_running_away_or_not", 1),
                    (val_div, ":agent_delta_courage_score", 3),  # if killed agent was running away his negative effect on ally courage scores become very less. This added because
                  (try_end),                                     # running away agents are easily killed and courage scores become very in a running away group after a time, and
                (try_end),                                       # they do not stop running away althought they pass near a new powerfull ally party.
                (agent_get_position, pos1, ":agent_no"),
                (get_distance_between_positions, ":dist", pos0, pos1),
                
                (try_begin),
                  (eq, ":killer_agent_no", ":agent_no"),
                  (agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
                  (val_mul, ":agent_delta_courage_score", 20),
                  (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
                  (agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
                (try_end),
                
                (try_begin),
                  (lt, ":dist", 100), #0-1 meters
                  (agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
                  (val_mul, ":agent_delta_courage_score", 150),
                  (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
                  (agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
                (else_try),
                  (lt, ":dist", 200), #2 meters
                  (agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
                  (val_mul, ":agent_delta_courage_score", 120),
                  (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
                  (agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
                (else_try),
                  (lt, ":dist", 300), #3 meter
                  (agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
                  (val_mul, ":agent_delta_courage_score", 100),
                  (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
                  (agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
                (else_try),
                  (lt, ":dist", 400), #4 meters
                  (agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
                  (val_mul, ":agent_delta_courage_score", 90),
                  (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
                  (agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
                (else_try),
                  (lt, ":dist", 600), #5-6 meters
                  (agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
                  (val_mul, ":agent_delta_courage_score", 80),
                  (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
                  (agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
                (else_try),
                  (lt, ":dist", 800), #7-8 meters
                  (agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
                  (val_mul, ":agent_delta_courage_score", 70),
                  (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
                  (agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
                (else_try),
                  (lt, ":dist", 1000), #9-10 meters
                  (agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
                  (val_mul, ":agent_delta_courage_score", 60),
                  (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
                  (agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
                (else_try),
                  (lt, ":dist", 1500), #11-15 meter
                  (agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
                  (val_mul, ":agent_delta_courage_score", 50),
                  (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
                  (agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
                (else_try),
                  (lt, ":dist", 2500), #16-25 meters
                  (agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
                  (val_mul, ":agent_delta_courage_score", 40),
                  (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
                  (agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
                (else_try),
                  (lt, ":dist", 4000), #26-40 meters
                  (agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
                  (val_mul, ":agent_delta_courage_score", 30),
                  (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
                  (agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
                (else_try),
                  (lt, ":dist", 6500), #41-65 meters
                  (agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
                  (val_mul, ":agent_delta_courage_score", 20),
                  (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
                  (agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
                (else_try),
                  (lt, ":dist", 10000), #61-100 meters
                  (agent_get_slot, ":agent_courage_score", ":agent_no", slot_agent_courage_score),
                  (val_mul, ":agent_delta_courage_score", 10),
                  (val_add, ":agent_courage_score", ":agent_delta_courage_score"),
                  (agent_set_slot, ":agent_no", slot_agent_courage_score, ":agent_courage_score"),
                (try_end),
              (try_end),
            (try_end),
        ]), #ozan
        
        # script_decide_run_away_or_not
        # Input: none
        # Output: none
        ("decide_run_away_or_not",
          [
            (store_script_param, ":cur_agent", 1),
            (store_script_param, ":mission_time", 2),
            
            (assign, ":force_retreat", 0),
            (agent_get_team, ":agent_team", ":cur_agent"),
            (agent_get_division, ":agent_division", ":cur_agent"),
            (try_begin),
              (lt, ":agent_division", 9), #static classes
              (team_get_movement_order, ":agent_movement_order", ":agent_team", ":agent_division"),
              (eq, ":agent_movement_order", mordr_retreat),
              (assign, ":force_retreat", 1),
            (try_end),
            
            (agent_get_slot, ":is_cur_agent_running_away", ":cur_agent", slot_agent_is_running_away),
            (try_begin),
              (eq, ":is_cur_agent_running_away", 0),
              (try_begin),
                (eq, ":force_retreat", 1),
                (agent_start_running_away, ":cur_agent"),
                (agent_set_slot, ":cur_agent",  slot_agent_is_running_away, 1),
              (else_try),
                (ge, ":mission_time", 45), #first 45 seconds anyone does not run away whatever happens.
                (agent_get_slot, ":agent_courage_score", ":cur_agent",  slot_agent_courage_score),
                (store_agent_hit_points, ":agent_hit_points", ":cur_agent"),
                (val_mul, ":agent_hit_points", 4),
                ## CC
                (try_begin),
                  (agent_is_ally, ":cur_agent"),
                  (val_sub, ":agent_hit_points", 100), #ally agents will be more tend to run away, to make game more funnier/harder
                  (val_mul, ":agent_hit_points", 10),
                (else_try),
                  (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
                  (try_begin),
                    (eq, ":reduce_campaign_ai", 0), # hard
                    (val_mul, ":agent_hit_points", 20),
                  (else_try),
                    (eq, ":reduce_campaign_ai", 1), # normal
                    (val_mul, ":agent_hit_points", 15),
                  (else_try),
                    (val_mul, ":agent_hit_points", 10), # easy
                  (try_end),
                (try_end),
                ## CC
                (store_sub, ":start_running_away_courage_score_limit", 3500, ":agent_hit_points"),
                (lt, ":agent_courage_score", ":start_running_away_courage_score_limit"), #if (courage score < 3500 - (agent hit points * 40)) and (agent is not running away) then start running away, average hit points : 50, average running away limit = 1500
                
                (agent_get_troop_id, ":troop_id", ":cur_agent"), #for now do not let heroes to run away from battle
                (neg|troop_is_hero, ":troop_id"),
                
                (agent_start_running_away, ":cur_agent"),
                (agent_set_slot, ":cur_agent",  slot_agent_is_running_away, 1),
              (try_end),
            (else_try),
              (neq, ":force_retreat", 1),
              (agent_get_slot, ":agent_courage_score", ":cur_agent",  slot_agent_courage_score),
              (store_agent_hit_points, ":agent_hit_points", ":cur_agent"),
              (val_mul, ":agent_hit_points", 4),
              ## CC
              (try_begin),
                (agent_is_ally, ":cur_agent"),
                (val_sub, ":agent_hit_points", 100), #ally agents will be more tend to run away, to make game more funnier/harder
                (val_mul, ":agent_hit_points", 10),
              (else_try),
                (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
                (try_begin),
                  (eq, ":reduce_campaign_ai", 0), # hard
                  (val_mul, ":agent_hit_points", 20),
                (else_try),
                  (eq, ":reduce_campaign_ai", 1), # normal
                  (val_mul, ":agent_hit_points", 15),
                (else_try),
                  (val_mul, ":agent_hit_points", 10), # easy
                (try_end),
              (try_end),
              ## CC
              (store_sub, ":stop_running_away_courage_score_limit", 3700, ":agent_hit_points"),
              (ge, ":agent_courage_score", ":stop_running_away_courage_score_limit"), #if (courage score > 3700 - agent hit points) and (agent is running away) then stop running away, average hit points : 50, average running away limit = 1700
              (agent_stop_running_away, ":cur_agent"),
              (agent_set_slot, ":cur_agent",  slot_agent_is_running_away, 0),
            (try_end),
        ]), #ozan
        
        # script_battle_tactic_apply
        # Input: none
        # Output: none
        ("battle_tactic_apply",
          [
            (call_script, "script_battle_tactic_apply_aux", "$ai_team_1", "$ai_team_1_battle_tactic"),
            (assign, "$ai_team_1_battle_tactic", reg0),
            (try_begin),
              (ge, "$ai_team_2", 0),
              (call_script, "script_battle_tactic_apply_aux", "$ai_team_2", "$ai_team_2_battle_tactic"),
              (assign, "$ai_team_2_battle_tactic", reg0),
            (try_end),
        ]),
        
        # script_battle_tactic_apply_aux
        # Input: team_no, battle_tactic
        # Output: battle_tactic
        ("battle_tactic_apply_aux",
          [
            (store_script_param, ":team_no", 1),
            (store_script_param, ":battle_tactic", 2),
            (store_mission_timer_a, ":mission_time"),
            (try_begin),
              (eq, ":battle_tactic", btactic_hold),
              (copy_position, pos1, pos52),
              (call_script, "script_get_closest3_distance_of_enemies_at_pos1", ":team_no", 1),
              (assign, ":avg_dist", reg0),
              (assign, ":min_dist", reg1),
              (try_begin),
                (this_or_next|lt, ":min_dist", 1000),
                (lt, ":avg_dist", 4000),
                (assign, ":battle_tactic", 0),
                (team_give_order, ":team_no", grc_everyone, mordr_charge),
              (try_end),
            (else_try),
              (eq, ":battle_tactic", btactic_follow_leader),
              (team_get_leader, ":ai_leader", ":team_no"),
              (try_begin),
                (ge, ":ai_leader", 0), ##1.134, this line was moved up 4 lines
                (agent_is_alive, ":ai_leader"),
                (agent_set_speed_limit, ":ai_leader", 9),
                (call_script, "script_team_get_average_position_of_enemies", ":team_no"),
                (copy_position, pos60, pos0),
                (agent_get_position, pos61, ":ai_leader"),
                (position_transform_position_to_local, pos62, pos61, pos60), #pos62 = vector to enemy w.r.t leader
                (position_normalize_origin, ":distance_to_enemy", pos62),
                (convert_from_fixed_point, ":distance_to_enemy"),
                (assign, reg17, ":distance_to_enemy"),
                (position_get_x, ":dir_x", pos62),
                (position_get_y, ":dir_y", pos62),
                (val_mul, ":dir_x", 23),
                (val_mul, ":dir_y", 23), #move 23 meters
                (position_set_x, pos62, ":dir_x"),
                (position_set_y, pos62, ":dir_y"),
                
                (position_transform_position_to_parent, pos63, pos61, pos62), #pos63 is 23m away from leader in the direction of the enemy.
                (position_set_z_to_ground_level, pos63),
                
                (team_give_order, ":team_no", grc_everyone, mordr_hold),
                (team_set_order_position, ":team_no", grc_everyone, pos63),
                (agent_get_position, pos1, ":ai_leader"),
                (try_begin),
                  (lt, ":distance_to_enemy", 50),
                  (ge, ":mission_time", 30),
                  (assign, ":battle_tactic", 0),
                  (team_give_order, ":team_no", grc_everyone, mordr_charge),
                  (agent_set_speed_limit, ":ai_leader", 60),
                (try_end),
              (else_try),
                (assign, ":battle_tactic", 0),
                (team_give_order, ":team_no", grc_everyone, mordr_charge),
              (try_end),
            (try_end),
            
            (try_begin), # charge everyone after a while
              (neq, ":battle_tactic", 0),
              (ge, ":mission_time", 300),
              (assign, ":battle_tactic", 0),
              (team_give_order, ":team_no", grc_everyone, mordr_charge),
              (team_get_leader, ":ai_leader", ":team_no"),
              (agent_set_speed_limit, ":ai_leader", 60),
            (try_end),
            (assign, reg0, ":battle_tactic"),
        ]),
        
        
        ##  # script_siege_defender_tactic_apply
        ##  # Input: none
        ##  # Output: none
        ##  ("siege_defender_tactic_apply",
        ##    [
        ##      (try_begin),
        ##        (eq, "$defender_team", 1),
        ##        (ge, "$belfry_positioned", 2),
        ##
        ##        (assign, ":enemy_too_weak", 0),
        ##        (try_begin),
        ##          (ge, "$attacker_reinforcement_stage", 2),
        ##          (call_script, "script_calculate_team_strength", "$defender_team"),
        ##          (assign, ":defender_strength", reg0),
        ##          (call_script, "script_calculate_team_strength", "$attacker_team"),
        ##          (assign, ":attacker_strength", reg0),
        ##          (store_mul, ":attacker_strength_multiplied", ":attacker_strength", 2),
        ##          (ge, ":defender_strength", ":attacker_strength_multiplied"),
        ##          (assign, ":enemy_too_weak", 1),
        ##        (try_end),
        ##
        ##        (try_begin),
        ##          (eq, ":enemy_too_weak", 1),
        ##          (neq, "$ai_battle_tactic", btactic_charge),
        ##          (assign, "$ai_battle_tactic", btactic_charge),
        ##          (team_give_order, "$defender_team", grc_infantry, mordr_charge),
        ##        (else_try),
        ##          (neq, "$ai_battle_tactic", btactic_charge),
        ##          (neq, "$ai_battle_tactic", btactic_hold),
        ##          (assign, "$ai_battle_tactic", btactic_hold),
        ##          (team_give_order, "$defender_team", grc_infantry, mordr_hold),
        ##          (team_give_order, "$defender_team", grc_heroes, mordr_hold),
        ##          (entry_point_get_position,pos1,10),
        ##          (team_set_order_position, "$defender_team", grc_infantry, pos1),
        ##          (team_set_order_position, "$defender_team", grc_heroes, pos1),
        ##        (try_end),
        ##      (try_end),
        ##  ]),
        
        
        # script_team_get_class_percentages
        # Input: arg1: team_no, arg2: try for team's enemies
        # Output: reg0: percentage infantry, reg1: percentage archers, reg2: percentage cavalry
        ("team_get_class_percentages",
          [
            (assign, ":num_infantry", 0),
            (assign, ":num_archers", 0),
            (assign, ":num_cavalry", 0),
            (assign, ":num_total", 0),
            (store_script_param, ":team_no", 1),
            (store_script_param, ":negate", 2),
            (try_for_agents,":cur_agent"),
              (agent_is_alive, ":cur_agent"),
              (agent_is_human, ":cur_agent"),
              (agent_get_team, ":agent_team", ":cur_agent"),
              (assign, ":continue", 0),
              (try_begin),
                (eq, ":negate", 1),
                (teams_are_enemies, ":agent_team", ":team_no"),
                (assign, ":continue", 1),
              (else_try),
                (eq, ":agent_team", ":team_no"),
                (assign, ":continue", 1),
              (try_end),
              (eq, ":continue", 1),
              (val_add, ":num_total", 1),
              (agent_get_class, ":agent_class", ":cur_agent"),
              (try_begin),
                (eq, ":agent_class", grc_infantry),
                (val_add,  ":num_infantry", 1),
              (else_try),
                (eq, ":agent_class", grc_archers),
                (val_add,  ":num_archers", 1),
              (else_try),
                (eq, ":agent_class", grc_cavalry),
                (val_add,  ":num_cavalry", 1),
              (try_end),
            (try_end),
            (try_begin),
              (eq,  ":num_total", 0),
              (assign,  ":num_total", 1),
            (try_end),
            (store_mul, ":perc_infantry",":num_infantry",100),
            (val_div, ":perc_infantry",":num_total"),
            (store_mul, ":perc_archers",":num_archers",100),
            (val_div, ":perc_archers",":num_total"),
            (store_mul, ":perc_cavalry",":num_cavalry",100),
            (val_div, ":perc_cavalry",":num_total"),
            (assign, reg0, ":perc_infantry"),
            (assign, reg1, ":perc_archers"),
            (assign, reg2, ":perc_cavalry"),
        ]),
        
        # script_get_closest3_distance_of_enemies_at_pos1
        # Input: arg1: team_no, pos1
        # Output: reg0: distance in cms.
        ("get_closest3_distance_of_enemies_at_pos1",
          [
            (assign, ":min_distance_1", 100000),
            (assign, ":min_distance_2", 100000),
            (assign, ":min_distance_3", 100000),
            
            (store_script_param, ":team_no", 1),
            (try_for_agents,":cur_agent"),
              (agent_is_alive, ":cur_agent"),
              (agent_is_human, ":cur_agent"),
              (agent_get_team, ":agent_team", ":cur_agent"),
              (teams_are_enemies, ":agent_team", ":team_no"),
              
              (agent_get_position, pos2, ":cur_agent"),
              (get_distance_between_positions,":cur_dist",pos2,pos1),
              (try_begin),
                (lt, ":cur_dist", ":min_distance_1"),
                (assign, ":min_distance_3", ":min_distance_2"),
                (assign, ":min_distance_2", ":min_distance_1"),
                (assign, ":min_distance_1", ":cur_dist"),
              (else_try),
                (lt, ":cur_dist", ":min_distance_2"),
                (assign, ":min_distance_3", ":min_distance_2"),
                (assign, ":min_distance_2", ":cur_dist"),
              (else_try),
                (lt, ":cur_dist", ":min_distance_3"),
                (assign, ":min_distance_3", ":cur_dist"),
              (try_end),
            (try_end),
            
            (assign, ":total_distance", 0),
            (assign, ":total_count", 0),
            (try_begin),
              (lt, ":min_distance_1", 100000),
              (val_add, ":total_distance", ":min_distance_1"),
              (val_add, ":total_count", 1),
            (try_end),
            (try_begin),
              (lt, ":min_distance_2", 100000),
              (val_add, ":total_distance", ":min_distance_2"),
              (val_add, ":total_count", 1),
            (try_end),
            (try_begin),
              (lt, ":min_distance_3", 100000),
              (val_add, ":total_distance", ":min_distance_3"),
              (val_add, ":total_count", 1),
            (try_end),
            (assign, ":average_distance", 100000),
            (try_begin),
              (gt, ":total_count", 0),
              (store_div, ":average_distance", ":total_distance", ":total_count"),
            (try_end),
            (assign, reg0, ":average_distance"),
            (assign, reg1, ":min_distance_1"),
            (assign, reg2, ":min_distance_2"),
            (assign, reg3, ":min_distance_3"),
        ]),
        
        # script_team_get_average_position_of_enemies
        # Input: arg1: team_no,
        # Output: pos0: average position.
        ("team_get_average_position_of_enemies",
          [
            (store_script_param_1, ":team_no"),
            (init_position, pos0),
            (assign, ":num_enemies", 0),
            (assign, ":accum_x", 0),
            (assign, ":accum_y", 0),
            (assign, ":accum_z", 0),
            (try_for_agents,":enemy_agent"),
              (agent_is_alive, ":enemy_agent"),
              (agent_is_human, ":enemy_agent"),
              (agent_get_team, ":enemy_team", ":enemy_agent"),
              (teams_are_enemies, ":team_no", ":enemy_team"),
              
              (agent_get_position, pos62, ":enemy_agent"),
              
              (position_get_x, ":x", pos62),
              (position_get_y, ":y", pos62),
              (position_get_z, ":z", pos62),
              
              (val_add, ":accum_x", ":x"),
              (val_add, ":accum_y", ":y"),
              (val_add, ":accum_z", ":z"),
              (val_add, ":num_enemies", 1),
            (try_end),
            
            (try_begin), #to avoid division by zeros at below division part.
              (le, ":num_enemies", 0),
              (assign, ":num_enemies", 1),
            (try_end),
            
            (store_div, ":average_x", ":accum_x", ":num_enemies"),
            (store_div, ":average_y", ":accum_y", ":num_enemies"),
            (store_div, ":average_z", ":accum_z", ":num_enemies"),
            
            (position_set_x, pos0, ":average_x"),
            (position_set_y, pos0, ":average_y"),
            (position_set_z, pos0, ":average_z"),
            
            (assign, reg0, ":num_enemies"),
        ]),
        
        
        # script_search_troop_prisoner_of_party
        # Input: arg1 = troop_no
        # Output: reg0 = party_no (-1 if troop is not a prisoner.)
        ("search_troop_prisoner_of_party",
          [
            (store_script_param_1, ":troop_no"),
            (assign, ":prisoner_of", -1),
            (try_for_parties, ":party_no"),
              (eq,  ":prisoner_of", -1),
              (this_or_next|eq, ":party_no", "p_main_party"),
              (ge, ":party_no", centers_begin),
              (party_count_prisoners_of_type, ":troop_found", ":party_no", ":troop_no"),
              (gt, ":troop_found", 0),
              (assign, ":prisoner_of", ":party_no"),
            (try_end),
            (assign, reg0, ":prisoner_of"),
        ]),
        
        
        ##  # script_clear_last_quest
        ##  # Input: arg1 = troop_no
        ##  # Output: none
        ##  ("clear_last_quest",
        ##    [
        ##      (store_script_param_1, ":troop_no"),
        ##
        ##      (troop_set_slot, ":troop_no",slot_troop_last_quest, 0),
        ##      (troop_set_slot, ":troop_no",slot_troop_last_quest_betrayed, 0)
        ##  ]),
        
        
        
        # script_change_debt_to_troop
        # Input: arg1 = troop_no, arg2 = new debt amount
        # Output: none
        ("change_debt_to_troop",
          [
            (store_script_param_1, ":troop_no"),
            (store_script_param_2, ":new_debt"),
            
            (troop_get_slot, ":cur_debt", ":troop_no", slot_troop_player_debt),
            (assign, reg1, ":cur_debt"),
            (val_add, ":cur_debt", ":new_debt"),
            (assign, reg2, ":cur_debt"),
            (troop_set_slot, ":troop_no", slot_troop_player_debt, ":cur_debt"),
            (str_store_troop_name_link, s1, ":troop_no"),
            (display_message, "@You now owe {reg2} denars to {s1}."),
        ]),
        
        
        
        
        # script_abort_quest
        # Input: arg1 = quest_no, arg2 = apply relation penalty
        # Output: none
        ("abort_quest",
          [
            (store_script_param_1, ":quest_no"),
            (store_script_param_2, ":abort_type"), #0=aborted by event, 1=abort by talking 2=abort by expire
            
            (assign, ":quest_return_penalty", -1),
            (assign, ":quest_expire_penalty", -2),
            
            #      (quest_get_slot, ":quest_object_troop", ":quest_no", slot_quest_object_troop),
            (try_begin),
              (this_or_next|eq, ":quest_no", "qst_deliver_message"),
              (eq, ":quest_no", "qst_deliver_message_to_enemy_lord"),
              (assign, ":quest_return_penalty", -2),
              (assign, ":quest_expire_penalty", -3),
            (else_try),
              (eq, ":quest_no", "qst_kidnapped_girl"),
              (party_remove_members, "p_main_party", "trp_kidnapped_girl", 1),
              (quest_get_slot, ":quest_target_party", "qst_kidnapped_girl", slot_quest_target_party), ##1.132, 5 new lines
              (try_begin),
                (party_is_active, ":quest_target_party"),
                (remove_party, ":quest_target_party"),
              (try_end), ##
            (else_try),
              (eq, ":quest_no", "qst_escort_lady"),
              (quest_get_slot, ":quest_object_troop", "qst_escort_lady", slot_quest_object_troop),
              (party_remove_members, "p_main_party", ":quest_object_troop", 1),
              (assign, ":quest_return_penalty", -2),
              (assign, ":quest_expire_penalty", -3),
              ##      (else_try),
              ##        (eq, ":quest_no", "qst_rescue_lady_under_siege"),
              ##        (party_remove_members, "p_main_party", ":quest_object_troop", 1),
              ##      (else_try),
              ##        (eq, ":quest_no", "qst_deliver_message_to_lover"),
              ##      (else_try),
              ##        (eq, ":quest_no", "qst_bring_prisoners_to_enemy"),
              ##        (try_begin),
              ##          (check_quest_succeeded, ":quest_no"),
              ##          (quest_get_slot, ":quest_target_amount", ":quest_no", slot_quest_target_amount),
              ##          (quest_get_slot, ":quest_object_troop", ":quest_no", slot_quest_object_troop),
              ##          (quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
              ##          (call_script, "script_game_get_join_cost", ":quest_object_troop"),
              ##          (assign, ":reward", reg0),
              ##          (val_mul, ":reward", ":quest_target_amount"),
              ##          (val_div, ":reward", 2),
              ##        (else_try),
              ##          (quest_get_slot, ":reward", ":quest_no", slot_quest_target_amount),
              ##        (try_end),
              ##        (call_script, "script_change_debt_to_troop", ":quest_giver_troop", ":reward"),
              ##      (else_try),
              ##        (eq, ":quest_no", "qst_bring_reinforcements_to_siege"),
              ##        (quest_get_slot, ":quest_target_amount", ":quest_no", slot_quest_target_amount),
              ##        (quest_get_slot, ":quest_object_troop", ":quest_no", slot_quest_object_troop),
              ##        (quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
              ##        (call_script, "script_game_get_join_cost", ":quest_object_troop"),
              ##        (assign, ":reward", reg0),
              ##        (val_mul, ":reward", ":quest_target_amount"),
              ##        (val_mul, ":reward", 2),
              ##        (call_script, "script_change_debt_to_troop", ":quest_giver_troop", ":reward"),
              ##      (else_try),
              ##        (eq, ":quest_no", "qst_deliver_supply_to_center_under_siege"),
              ##        (quest_get_slot, ":quest_target_amount", ":quest_no", slot_quest_target_amount),
              ##        (quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
              ##        (store_item_value, ":reward", "itm_siege_supply"),
              ##        (val_mul, ":reward", ":quest_target_amount"),
              ##        (call_script, "script_change_debt_to_troop", ":quest_giver_troop", ":reward"),
            (else_try),
              (eq, ":quest_no", "qst_raise_troops"),
              (quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
              (call_script, "script_change_debt_to_troop", ":quest_giver_troop", 100),
              (assign, ":quest_return_penalty", -4),
              (assign, ":quest_expire_penalty", -5),
            (else_try),
              (eq, ":quest_no", "qst_deal_with_looters"),
              (try_for_parties, ":cur_party_no"),
                (party_get_template_id, ":cur_party_template", ":cur_party_no"),
			##Floris MTT begin
				(this_or_next|eq, ":cur_party_template", "pt_looters"),
				(this_or_next|eq, ":cur_party_template", "pt_looters_r"),
				(eq, ":cur_party_template", "pt_looters_e"),
			##Floris MTT end
                (party_set_flags, ":cur_party_no", pf_quest_party, 0),
              (try_end),
              (assign, ":quest_return_penalty", -4),
              (assign, ":quest_expire_penalty", -5),
            (else_try),
              (eq, ":quest_no", "qst_deal_with_bandits_at_lords_village"),
              (quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
              (call_script, "script_change_debt_to_troop", ":quest_giver_troop", 200),
              (assign, ":quest_return_penalty", -5),
              (assign, ":quest_expire_penalty", -6),
            (else_try),
              (eq, ":quest_no", "qst_collect_taxes"),
              (quest_get_slot, ":gold_reward", ":quest_no", slot_quest_gold_reward),
              (quest_set_slot, ":quest_no", slot_quest_gold_reward, 0),
              (quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
              (call_script, "script_change_debt_to_troop", ":quest_giver_troop", ":gold_reward"),
              (assign, ":quest_return_penalty", -4),
              (assign, ":quest_expire_penalty", -6),
              ##      (else_try),
              ##        (eq, ":quest_no", "qst_capture_messenger"),
              ##      (else_try),
              ##        (eq, ":quest_no", "qst_bring_back_deserters"),
            (else_try),
              (eq, ":quest_no", "qst_hunt_down_fugitive"),
              (assign, ":quest_return_penalty", -3),
              (assign, ":quest_expire_penalty", -4),
            (else_try),
              (eq, ":quest_no", "qst_kill_local_merchant"),
            (else_try),
              (eq, ":quest_no", "qst_bring_back_runaway_serfs"),
              (assign, ":quest_return_penalty", -1),
              (assign, ":quest_expire_penalty", -1),
            (else_try),
              (eq, ":quest_no", "qst_lend_companion"),
            (else_try),
              (eq, ":quest_no", "qst_collect_debt"),
              (try_begin),
                (quest_slot_eq, "qst_collect_debt", slot_quest_current_state, 1), #debt collected but not delivered
                (quest_get_slot, ":debt", "qst_collect_debt", slot_quest_target_amount),
                (quest_get_slot, ":quest_giver", "qst_collect_debt", slot_quest_giver_troop),
                (call_script, "script_change_debt_to_troop", ":quest_giver", ":debt"),
                (assign, ":quest_return_penalty", -3),
                (assign, ":quest_expire_penalty", -6),
              (else_try),
                (assign, ":quest_return_penalty", -3),
                (assign, ":quest_expire_penalty", -4),
              (try_end),
            (else_try),
              (eq, ":quest_no", "qst_deal_with_bandits_at_lords_village"),
              (assign, ":quest_return_penalty", -6),
              (assign, ":quest_expire_penalty", -6),
            (else_try),
              (eq, ":quest_no", "qst_cause_provocation"),
              (assign, ":quest_return_penalty", -10),
              (assign, ":quest_expire_penalty", -13),
            (else_try),
              (eq, ":quest_no", "qst_persuade_lords_to_make_peace"),
              (assign, ":quest_return_penalty", -10),
              (assign, ":quest_expire_penalty", -13),
            (else_try),
              (eq, ":quest_no", "qst_deal_with_night_bandits"),
              (assign, ":quest_return_penalty", -1),
              (assign, ":quest_expire_penalty", -1),
              
            (else_try),
              (eq, ":quest_no", "qst_follow_spy"),
              (assign, ":quest_return_penalty", -2),
              (assign, ":quest_expire_penalty", -3),
              (try_begin),
                (party_is_active, "$qst_follow_spy_spy_party"),
                (remove_party, "$qst_follow_spy_spy_party"),
              (try_end),
              (try_begin),
                (party_is_active, "$qst_follow_spy_spy_partners_party"),
                (remove_party, "$qst_follow_spy_spy_partners_party"),
              (try_end),
            (else_try),
              (eq, ":quest_no", "qst_capture_enemy_hero"),
              (assign, ":quest_return_penalty", -3),
              (assign, ":quest_expire_penalty", -4),
              ##      (else_try),
              ##        (eq, ":quest_no", "qst_lend_companion"),
              ##        (quest_get_slot, ":quest_target_troop", "qst_lend_companion", slot_quest_target_troop),
              ##        (party_add_members, "p_main_party", ":quest_target_troop", 1),
              ##      (else_try),
              ##        (eq, ":quest_no", "qst_capture_conspirators"),
              ##      (else_try),
              ##        (eq, ":quest_no", "qst_defend_nobles_against_peasants"),
            (else_try),
              (eq, ":quest_no", "qst_incriminate_loyal_commander"),
              (assign, ":quest_return_penalty", -5),
              (assign, ":quest_expire_penalty", -6),
              ##      (else_try),
              ##        (eq, ":quest_no", "qst_hunt_down_raiders"),
              ##      (else_try),
              ##        (eq, ":quest_no", "qst_capture_prisoners"),
              ##        #Enemy lord quests
            (else_try),
              (eq, ":quest_no", "qst_lend_surgeon"),
              
              #Kingdom lady quests
            (else_try),
              (eq, ":quest_no", "qst_rescue_lord_by_replace"),
              (assign, ":quest_return_penalty", -1),
              (assign, ":quest_expire_penalty", -1),
            (else_try),
              (eq, ":quest_no", "qst_deliver_message_to_prisoner_lord"),
              (assign, ":quest_return_penalty", 0),
              (assign, ":quest_expire_penalty", -1),
            (else_try),
              (eq, ":quest_no", "qst_duel_for_lady"),
              (assign, ":quest_return_penalty", -1),
              (assign, ":quest_expire_penalty", -1),
              
              #Kingdom Army quests
            (else_try),
              (eq, ":quest_no", "qst_follow_army"),
              (assign, ":quest_return_penalty", 0), #was -4
              (assign, ":quest_expire_penalty", 0), #was -5
            (else_try),
              (eq, ":quest_no", "qst_deliver_cattle_to_army"),
              (assign, ":quest_return_penalty", 0),
              (assign, ":quest_expire_penalty", 0),
            (else_try),
              (eq, ":quest_no", "qst_join_siege_with_army"),
              (assign, ":quest_return_penalty", -1),
              (assign, ":quest_expire_penalty", -2),
            (else_try),
              (eq, ":quest_no", "qst_scout_waypoints"),
              (assign, ":quest_return_penalty", 0),
              (assign, ":quest_expire_penalty", 0),
              
              #Village Elder quests
            (else_try),
              (eq, ":quest_no", "qst_deliver_grain"),
              (assign, ":quest_return_penalty", -6),
              (assign, ":quest_expire_penalty", -7),
            (else_try),
              (eq, ":quest_no", "qst_deliver_cattle"),
              (assign, ":quest_return_penalty", -3),
              (assign, ":quest_expire_penalty", -4),
            (else_try),
              (eq, ":quest_no", "qst_train_peasants_against_bandits"),
              (assign, ":quest_return_penalty", -4),
              (assign, ":quest_expire_penalty", -5),
              
              #Mayor quests
            (else_try),
              (eq, ":quest_no", "qst_deliver_wine"),
              (assign, ":quest_return_penalty", -1),
              (assign, ":quest_expire_penalty", -3),
              (val_add, "$debt_to_merchants_guild", "$qst_deliver_wine_debt"),
            (else_try),
              (eq, ":quest_no", "qst_move_cattle_herd"),
              (assign, ":quest_return_penalty", -1),
              (assign, ":quest_expire_penalty", -3),
            (else_try),
              (eq, ":quest_no", "qst_escort_merchant_caravan"),
              (assign, ":quest_return_penalty", -1),
              (assign, ":quest_expire_penalty", -3),
            (else_try),
              (eq, ":quest_no", "qst_troublesome_bandits"),
              (assign, ":quest_return_penalty", -1),
              (assign, ":quest_expire_penalty", -2),
              #Other quests
            (else_try),
              (eq, ":quest_no", "qst_join_faction"),
              (assign, ":quest_return_penalty", -3),
              (assign, ":quest_expire_penalty", -3),
              (try_begin),
                (call_script, "script_get_number_of_hero_centers", "trp_player"),
                (gt, reg0, 0),
                (call_script, "script_change_player_relation_with_faction", "$g_invite_faction", -10),
              (try_end),
              
              
              (try_begin), #if the vassalage is part of a surrender option, then the faction returns to a state of war
                (quest_slot_eq, "qst_join_faction", slot_quest_failure_consequence, 1),
                (call_script, "script_diplomacy_start_war_between_kingdoms", "fac_player_supporters_faction", "$g_invite_faction", 0),
                (call_script, "script_change_player_honor", -5),
                (quest_set_slot, "qst_join_faction", slot_quest_failure_consequence, 0),
              (try_end),
              
              
              (assign, "$g_invite_faction", 0),
              (assign, "$g_invite_faction_lord", 0),
              (assign, "$g_invite_offered_center", 0),
            (else_try),
              (eq, ":quest_no", "qst_eliminate_bandits_infesting_village"),
              (assign, ":quest_return_penalty", -3),
              (assign, ":quest_expire_penalty", -3),
            (else_try),
              (ge, ":quest_no", "qst_resolve_dispute"),
              (assign, ":authority_loss", -2),
              (assign, ":quest_return_penalty", 0),
              (assign, ":quest_expire_penalty", 0),
            (else_try),
              (ge, ":quest_no", "qst_consult_with_minister"),
              (assign, ":authority_loss", -2),
              (assign, ":quest_return_penalty", 0),
              (assign, ":quest_expire_penalty", 0),
            (try_end),
            
            (try_begin),
              (gt, ":abort_type", 0),
              (lt, ":quest_no", "qst_resolve_dispute"),
              
              (quest_get_slot, ":quest_giver", ":quest_no", slot_quest_giver_troop),
              (assign, ":relation_penalty", ":quest_return_penalty"),
              (try_begin),
                (eq, ":abort_type", 2),
                (assign, ":relation_penalty", ":quest_expire_penalty"),
              (try_end),
              (try_begin),
                (this_or_next|is_between, ":quest_giver", village_elders_begin, village_elders_end),
                (is_between, ":quest_giver", mayors_begin, mayors_end),
                (quest_get_slot, ":quest_giver_center", ":quest_no", slot_quest_giver_center),
                (call_script, "script_change_player_relation_with_center", ":quest_giver_center", ":relation_penalty"),
              (else_try),
                (call_script, "script_change_player_relation_with_troop", ":quest_giver", ":relation_penalty"),
              (try_end),
            (try_end),
            
            (fail_quest, ":quest_no"),
            
            #NPC companion changes begin
            (try_begin),
              (gt, ":abort_type", 0),
              (neq, ":quest_no", "qst_consult_with_minister"),
              (neq, ":quest_no", "qst_resolve_dispute"),
              (neq, ":quest_no", "qst_visit_lady"),
              (neq, ":quest_no", "qst_formal_marriage_proposal"),
              (neq, ":quest_no", "qst_duel_courtship_rival"),
              (neq, ":quest_no", "qst_follow_army"),
              (neq, ":quest_no", "qst_denounce_lord"),
              (neq, ":quest_no", "qst_intrigue_against_lord"),
              (neq, ":quest_no", "qst_offer_gift"),
              (neq, ":quest_no", "qst_organize_feast"),
              
              (call_script, "script_objectionable_action", tmt_honest, "str_fail_quest"),
            (try_end),
            #NPC companion changes end
            
		  (try_begin),
			(eq, ":quest_no", "qst_resolve_dispute"),
			##diplomacy start+
			#add support for "spouse of leader" arrangements
			#(faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
			(faction_get_slot, ":leader", "$players_kingdom", slot_faction_leader),#added
			(ge, ":leader", 0),
			(this_or_next|troop_slot_eq, ":leader", slot_troop_spouse, "trp_player"),
			(this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, ":leader"),
					   (eq, ":leader", "trp_player"),
			(call_script, "script_change_player_right_to_rule", ":authority_loss"),#<- unaltered
			#add support for promoted kingdom ladies
			(try_for_range, ":lord", heroes_begin, heroes_end),#<- changed active_npcs to heroes
				(this_or_next|troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
					(is_between, ":lord", active_npcs_begin, active_npcs_end),
				#exempt retired/exiled/dead lords
				(neg|troop_slot_ge, ":lord", slot_troop_occupation, slto_retirement),
				(store_faction_of_troop, ":lord_faction", ":lord"),#<- unaltered
				(this_or_next|eq, ":lord_faction", "$players_kingdom"),#added for "spouse of leader" arrangements
			##diplomacy end+
				(eq, ":lord_faction", "fac_player_supporters_faction"),
				(call_script, "script_troop_change_relation_with_troop", ":lord", "trp_player", ":authority_loss"),
			(try_end),
		  (try_end),
            
            
            (try_begin),
              (eq, ":quest_no", "qst_organize_feast"),
              (call_script, "script_add_notification_menu", "mnu_notification_feast_quest_expired", 0, 0),
            (try_end),
            
            
            (call_script, "script_end_quest", ":quest_no"),
        ]),
        
        
        ##  # script_event_center_captured
        ##  # Input: arg1 = center_no, arg2 = old_faction_no
        ##  # Output: none
        ##  ("event_center_captured",
        ##    [
        ##      #      (store_script_param_1, ":center_no"),
        ##      #       (store_script_param_2, ":old_faction_no"),
        ##      #       (store_faction_of_party, ":faction_no"),
        ##
        ##      (try_begin),
        ##        (check_quest_active, "qst_deliver_message"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_escort_lady"),
        ##        (quest_slot_eq, "qst_escort_lady", slot_quest_target_center, ":center_no"),
        ##        (call_script, "script_abort_quest", "qst_escort_lady"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_rescue_lady_under_siege"),
        ##        (quest_slot_eq, "qst_rescue_lady_under_siege", slot_quest_target_center, ":center_no"),
        ##        (quest_slot_eq, "qst_rescue_lady_under_siege", slot_quest_current_state, 0),
        ##        (call_script, "script_abort_quest", "qst_rescue_lady_under_siege", 1),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_deliver_message_to_lover"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_deliver_message_to_enemy_lord"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_bring_prisoners_to_enemy"),
        ##        (quest_slot_eq, "qst_bring_prisoners_to_enemy", slot_quest_target_center, ":center_no"),
        ##        (neg|check_quest_succeeded, "qst_bring_prisoners_to_enemy"),
        ##        (call_script, "script_abort_quest", "qst_bring_prisoners_to_enemy"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_bring_reinforcements_to_siege"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_deliver_supply_to_center_under_siege"),
        ##        (quest_slot_eq, "qst_deliver_supply_to_center_under_siege", slot_quest_target_center, ":center_no"),
        ##        (call_script, "script_abort_quest", "qst_deliver_supply_to_center_under_siege", 1),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_raise_troops"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_capture_messenger"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_bring_back_deserters"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_kill_local_merchant"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_bring_back_runaway_serfs"),
        ##        (quest_slot_eq, "qst_bring_back_runaway_serfs", slot_quest_object_center, ":center_no"),
        ##        (neg|check_quest_succeeded, "qst_bring_back_runaway_serfs"),
        ##        (neg|check_quest_failed, "qst_bring_back_runaway_serfs"),
        ##        (call_script, "script_abort_quest", "qst_bring_back_runaway_serfs"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_follow_spy"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_capture_enemy_hero"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_lend_companion"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_capture_conspirators"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_defend_nobles_against_peasants"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_incriminate_loyal_commander"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_hunt_down_raiders"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_capture_prisoners"),
        ##      (try_end),
        ##      #Enemy lord quests
        ##      (try_begin),
        ##        (check_quest_active, "qst_lend_surgeon"),
        ##      (try_end),
        ##      #Kingdom lady quests
        ##      (try_begin),
        ##        (check_quest_active, "qst_rescue_lord_by_replace"),
        ##        (quest_get_slot, ":quest_target_troop", "qst_rescue_lord_by_replace", slot_quest_target_troop),
        ##        (troop_slot_eq, ":quest_target_troop", slot_troop_is_prisoner, 0),
        ##        (neg|check_quest_succeeded, "qst_rescue_lord_by_replace"),
        ##        (call_script, "script_abort_quest", "qst_rescue_lord_by_replace"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_deliver_message_to_prisoner_lord"),
        ##      (try_end),
        ##      (try_begin),
        ##        (check_quest_active, "qst_duel_for_lady"),
        ##      (try_end),
        ##  ]),
        
        # script_cf_is_quest_troop
        # Input: arg1 = troop_no
        # Output: none (can fail)
        ("cf_is_quest_troop",
          [
            (store_script_param_1, ":troop_no"),
            (assign, ":is_quest_troop", 0),
            (try_for_range, ":cur_quest", all_quests_begin, all_quests_end),
              (check_quest_active, ":cur_quest"),
              (quest_get_slot, ":quest_troop_1", ":cur_quest", slot_quest_target_troop),
              (quest_get_slot, ":quest_troop_2", ":cur_quest", slot_quest_object_troop),
              (quest_get_slot, ":quest_troop_3", ":cur_quest", slot_quest_giver_troop),
              (this_or_next|eq, ":quest_troop_1", ":troop_no"),
              (this_or_next|eq, ":quest_troop_2", ":troop_no"),
              (eq, ":quest_troop_3", ":troop_no"),
              (assign, ":is_quest_troop", 1),
            (try_end),
            (eq, ":is_quest_troop", 1),
        ]),
        
        
        ##  # script_calculate_team_strength
        ##  # Input: arg1 = team_no
        ##  # Output: strength
        ##  ("calculate_team_strength",
        ##    [
        ##      (store_script_param_1, ":team_no"),
        ##      (assign, ":total_strength", 0),
        ##      (try_for_agents, ":cur_agent"),
        ##        (agent_get_team, ":agent_team", ":cur_agent"),
        ##        (eq, ":team_no", ":agent_team"),
        ##        (agent_is_human, ":cur_agent"),
        ##        (agent_is_alive, ":cur_agent"),
        ##
        ##        (agent_get_troop_id, ":cur_troop", ":cur_agent"),
        ##        (store_character_level, ":cur_level", ":cur_troop"),
        ##        (val_add, ":cur_level", 5),
        ##        (try_begin),
        ##          (troop_is_hero, ":cur_troop"),
        ##          (val_add, ":cur_level", 5),
        ##        (try_end),
        ##        (val_add, ":total_strength", ":cur_level"),
        ##      (try_end),
        ##      (assign, reg0, ":total_strength"),
        ##  ]),
        
        # script_check_friendly_kills
        # Input: none
        # Output: none (changes the morale of the player's party)
        ("check_friendly_kills",
          [(get_player_agent_own_troop_kill_count, ":count"),
            (try_begin),
              (neq, "$g_player_current_own_troop_kills", ":count"),
              (val_sub, ":count", "$g_player_current_own_troop_kills"),
              (val_add, "$g_player_current_own_troop_kills", ":count"),
              (val_mul, ":count", -1),
              (call_script, "script_change_player_party_morale", ":count"),
            (try_end),
        ]),
        
        # script_simulate_retreat
        # Input: arg1 = players_side_damage, arg2 = enemy_side_damage, arg3 = continue_battle s5 = title_string
        # Output: none
        ("simulate_retreat",
          [
            (call_script, "script_music_set_situation_with_culture", mtf_sit_killed),
            (set_show_messages, 0),
            (store_script_param, ":players_side_damage", 1),
            (store_script_param, ":enemy_side_damage", 2),
            (store_script_param, ":continue_battle", 3),
            
            (assign, ":players_side_strength", 0),
            (assign, ":enemy_side_strength", 0),
            
            (assign, ":do_calculate", 1),
            (try_begin),
              (try_for_agents, ":cur_agent"),
                (agent_is_human, ":cur_agent"),
                (agent_is_alive, ":cur_agent"),
                (agent_set_slot, ":cur_agent", slot_agent_is_alive_before_retreat, 1),#needed for simulation
                
                (agent_get_troop_id, ":cur_troop", ":cur_agent"),
                (store_character_level, ":cur_level", ":cur_troop"),
                (val_add, ":cur_level", 5),
                (try_begin),
                  (troop_is_hero, ":cur_troop"),
                  (val_add, ":cur_level", 5),
                (try_end),
                (try_begin),
                  (agent_is_ally, ":cur_agent"),
                  (val_add, ":players_side_strength", ":cur_level"),
                (else_try),
                  (val_add, ":enemy_side_strength", ":cur_level"),
                (try_end),
              (try_end),
              (eq, "$pin_player_fallen", 0),
              (lt, ":enemy_side_strength", ":players_side_strength"),
              (eq, ":continue_battle", 1),
              (assign, ":do_calculate", 0),
            (try_end),
            
            (try_begin),
              (eq, ":do_calculate", 1),
              
              (assign, "$g_last_mission_player_damage", 0),
              (party_clear, "p_temp_party"),
              (party_clear, "p_temp_party_2"),
              (call_script, "script_simulate_battle_with_agents_aux", 0, ":players_side_damage"),
              (call_script, "script_simulate_battle_with_agents_aux", 1, ":enemy_side_damage"),
              
              (assign, ":display_casualties", 0),
              
              (try_begin),
                (gt, "$g_last_mission_player_damage", 0),
                (assign, ":display_casualties", 1),
                (assign, reg1, "$g_last_mission_player_damage"),
                (str_store_string, s12, "str_casualty_display_hp"),
              (else_try),
                (str_clear, s12),
              (try_end),
              
              (call_script, "script_print_casualties_to_s0", "p_temp_party", 1),
              (try_begin),
                (party_get_num_companion_stacks, ":num_stacks", "p_temp_party"),
                (gt, ":num_stacks", 0),
                (assign, ":display_casualties", 1),
              (try_end),
              (str_store_string_reg, s10, s0),
              
              (call_script, "script_print_casualties_to_s0", "p_temp_party_2", 1),
              (try_begin),
                (party_get_num_companion_stacks, ":num_stacks", "p_temp_party_2"),
                (gt, ":num_stacks", 0),
                (assign, ":display_casualties", 1),
              (try_end),
              (str_store_string_reg, s11, s0),
              (try_begin),
                (eq, ":display_casualties", 1),
                (dialog_box,"str_casualty_display", s5),
              (try_end),
            (try_end),
            (set_show_messages, 1),
            
            #Calculating morale penalty (can be between 0-30)
            (assign, ":ally_casualties", 0),
            (assign, ":enemy_casualties", 0),
            (assign, ":total_allies", 0),
            
            (try_for_agents, ":cur_agent"),
              (agent_is_human, ":cur_agent"),
              (try_begin),
                (agent_is_ally, ":cur_agent"),
                (val_add, ":total_allies", 1),
                (try_begin),
                  (neg|agent_is_alive, ":cur_agent"),
                  (val_add, ":ally_casualties", 1),
                (try_end),
              (else_try),
                (neg|agent_is_alive, ":cur_agent"),
                (val_add, ":enemy_casualties", 1),
              (try_end),
            (try_end),
            (store_add, ":total_casualties", ":ally_casualties", ":enemy_casualties"),
            (try_begin),
              (gt, ":total_casualties", 0),
              (store_mul, ":morale_adder", ":ally_casualties", 100),
              (val_div, ":morale_adder", ":total_casualties"),
              (val_mul, ":morale_adder", ":ally_casualties"),
              (val_div, ":morale_adder", ":total_allies"),
              (val_mul, ":morale_adder", -30),
              (val_div, ":morale_adder", 100),
              (call_script, "script_change_player_party_morale", ":morale_adder"),
            (try_end),
        ]),
        
        
        
        # script_simulate_battle_with_agents_aux
        # For internal use only
        # Input: arg1 = attacker_side (0 = ally, 1 = enemy), arg2 = damage amount
        # Output: none
        ("simulate_battle_with_agents_aux",
          [
            (store_script_param_1, ":attacker_side"),
            (store_script_param_2, ":damage"),
            
            (get_player_agent_no, ":player_agent"),
            (try_for_agents, ":cur_agent"),
              (neq, ":player_agent", ":cur_agent"),
              (agent_is_human, ":cur_agent"),
              #do not check agent_is_alive, check slot_agent_is_alive_before_retreat instead, so that dead agents can still hit enemies
              (agent_slot_eq, ":cur_agent", slot_agent_is_alive_before_retreat, 1),
              (try_begin),
                (agent_is_ally, ":cur_agent"),
                (assign, ":cur_agents_side", 0),
              (else_try),
                (assign, ":cur_agents_side", 1),
              (try_end),
              (eq, ":cur_agents_side", ":attacker_side"),
              (agent_get_position, pos2, ":cur_agent"),
              (assign, ":closest_agent", -1),
              (assign, ":min_distance", 100000),
              (try_for_agents, ":cur_agent_2"),
                (agent_is_human, ":cur_agent_2"),
                (agent_is_alive, ":cur_agent_2"),
                (try_begin),
                  (agent_is_ally, ":cur_agent_2"),
                  (assign, ":cur_agents_side_2", 0),
                (else_try),
                  (assign, ":cur_agents_side_2", 1),
                (try_end),
                (this_or_next|neq, ":cur_agent_2", ":player_agent"),
                (eq, "$pin_player_fallen", 0),
                (neq, ":attacker_side", ":cur_agents_side_2"),
                (agent_get_position, pos3, ":cur_agent_2"),
                (get_distance_between_positions, ":cur_distance", pos2, pos3),
                (lt, ":cur_distance", ":min_distance"),
                (assign, ":min_distance", ":cur_distance"),
                (assign, ":closest_agent", ":cur_agent_2"),
              (try_end),
              (ge, ":closest_agent", 0),
              #Fight
              (agent_get_class, ":agent_class", ":cur_agent"),
              (assign, ":agents_speed", 1),
              (assign, ":agents_additional_hit", 0),
              (try_begin),
                (eq, ":agent_class", grc_archers),
                (assign, ":agents_additional_hit", 2),
              (else_try),
                (eq, ":agent_class", grc_cavalry),
                (assign, ":agents_speed", 2),
              (try_end),
              (agent_get_class, ":agent_class", ":closest_agent"),
              (assign, ":agents_speed_2", 1),
              (try_begin),
                (eq, ":agent_class", grc_cavalry),
                (assign, ":agents_speed_2", 2),
              (try_end),
              (assign, ":agents_hit", 18000),
              (val_add, ":min_distance", 3000),
              (val_div, ":agents_hit", ":min_distance"),
              (val_mul, ":agents_hit", 2),# max 10, min 2 hits within 150 meters
              
              (val_mul, ":agents_hit", ":agents_speed"),
              (val_div, ":agents_hit", ":agents_speed_2"),
              (val_add, ":agents_hit", ":agents_additional_hit"),
              
              (assign, ":cur_damage", ":damage"),
              (agent_get_troop_id, ":closest_troop", ":closest_agent"),
              (agent_get_troop_id, ":cur_troop", ":cur_agent"),
              (store_character_level, ":closest_level", ":closest_troop"),
              (store_character_level, ":cur_level", ":cur_troop"),
              (store_sub, ":level_dif", ":cur_level", ":closest_level"),
              (val_div, ":level_dif", 5),
              (val_add, ":cur_damage", ":level_dif"),
              
              (try_begin),
                (eq, ":closest_agent", ":player_agent"),
                (val_div, ":cur_damage", 2),
                (store_agent_hit_points, ":init_player_hit_points", ":player_agent", 1),
              (try_end),
              
              (try_for_range, ":unused", 0, ":agents_hit"),
                (store_random_in_range, ":random_damage", 0, 100),
                (lt, ":random_damage", ":cur_damage"),
                (agent_deliver_damage_to_agent, ":cur_agent", ":closest_agent"),
              (try_end),
              
              (try_begin),
                (eq, ":closest_agent", ":player_agent"),
                (store_agent_hit_points, ":final_player_hit_points", ":player_agent", 1),
                (store_sub, ":hit_points_difference", ":init_player_hit_points", ":final_player_hit_points"),
                (val_add, "$g_last_mission_player_damage", ":hit_points_difference"),
              (try_end),
              
              (neg|agent_is_alive, ":closest_agent"),
              (try_begin),
                (eq, ":attacker_side", 1),
                (party_add_members, "p_temp_party", ":closest_troop", 1),
                (try_begin),
                  (agent_is_wounded, ":closest_agent"),
                  (party_wound_members, "p_temp_party", ":closest_troop", 1),
                (try_end),
              (else_try),
                (party_add_members, "p_temp_party_2", ":closest_troop", 1),
                (try_begin),
                  (agent_is_wounded, ":closest_agent"),
                  (party_wound_members, "p_temp_party_2", ":closest_troop", 1),
                (try_end),
              (try_end),
            (try_end),
        ]),
        
        
        # script_map_get_random_position_around_position_within_range
        # Input: arg1 = minimum_distance in km, arg2 = maximum_distance in km, pos1 = origin position
        # Output: pos2 = result position
        ("map_get_random_position_around_position_within_range",
          [
            (store_script_param_1, ":min_distance"),
            (store_script_param_2, ":max_distance"),
            (val_mul, ":min_distance", 100),
            (assign, ":continue", 1),
            (try_for_range, ":unused", 0, 20),
              (eq, ":continue", 1),
              (map_get_random_position_around_position, pos2, pos1, ":max_distance"),
              (get_distance_between_positions, ":distance", pos2, pos1),
              (ge, ":distance", ":min_distance"),
              (assign, ":continue", 0),
            (try_end),
        ]),
        
        
        # script_get_number_of_unclaimed_centers_by_player
        # Input: none
        # Output: reg0 = number of unclaimed centers, reg1 = last unclaimed center_no
        ("get_number_of_unclaimed_centers_by_player",
          [
            (assign, ":unclaimed_centers", 0),
            (assign, reg1, -1),
            (try_for_range, ":center_no", centers_begin, centers_end),
              (store_faction_of_party, ":faction_no", ":center_no"),
              (eq, ":faction_no", "fac_player_supporters_faction"),
              (party_slot_eq, ":center_no", slot_town_claimed_by_player, 0),
              (party_get_num_companion_stacks, ":num_stacks", ":center_no"),
              (ge, ":num_stacks", 1), #castle is garrisoned
              (assign, reg1, ":center_no"),
              (val_add, ":unclaimed_centers", 1),
            (try_end),
            (assign, reg0, ":unclaimed_centers"),
        ]),
        
        # script_troop_count_number_of_enemy_troops
        # Input: arg1 = troop_no
        # Output: reg0 = number_of_enemy_troops
        #  ("troop_count_number_of_enemy_troops",
        #    [
        #      (store_script_param_1, ":troop_no"),
        #      (assign, ":enemy_count", 0),
        #      (try_for_range, ":i_enemy_slot", slot_troop_enemies_begin, slot_troop_enemies_end),
        #        (troop_slot_ge, ":troop_no", ":i_enemy_slot", 1),
        #        (val_add, ":enemy_count", 1),
        #      (try_end),
        #      (assign, reg0, ":enemy_count"),
        #  ]),
        
        
        # script_cf_troop_check_troop_is_enemy
        # Input: arg1 = troop_no, arg2 = checked_troop_no
        # Output: none (Can fail)
        ("cf_troop_check_troop_is_enemy",
          [
            (store_script_param_1, ":troop_no"),
            (store_script_param_2, ":checked_troop_no"),
            (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":checked_troop_no"),
            (lt, reg0, -10),
        ]),
        
        
        # script_troop_get_leaded_center_with_index
        # Input: arg1 = troop_no, arg2 = center index within range between zero and the number of centers that troop owns
        # Output: reg0 = center_no
        ("troop_get_leaded_center_with_index",
          [
            (store_script_param_1, ":troop_no"),
            (store_script_param_2, ":random_center"),
            (assign, ":result", -1),
            (assign, ":center_count", 0),
            (try_for_range, ":center_no", centers_begin, centers_end),
              (eq, ":result", -1),
              (party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
              (val_add, ":center_count", 1),
              (gt, ":center_count", ":random_center"),
              (assign, ":result", ":center_no"),
            (try_end),
            (assign, reg0, ":result"),
        ]),
        
        # script_cf_troop_get_random_leaded_walled_center_with_less_strength_priority
        # Input: arg1 = troop_no, arg2 = preferred_center_no
        # Output: reg0 = center_no (Can fail)
        ("cf_troop_get_random_leaded_walled_center_with_less_strength_priority",
          [
            (store_script_param, ":troop_no", 1),
            (store_script_param, ":preferred_center_no", 2),
            
            (assign, ":num_centers", 0),
            (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
              (party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
              (party_slot_eq, ":center_no", slot_center_is_besieged_by, -1),
              (val_add, ":num_centers", 1),
              (try_begin),
                (eq, ":center_no", ":preferred_center_no"),
                (val_add, ":num_centers", 99),
              (try_end),
              ##        (call_script, "script_party_calculate_regular_strength", ":center_no"),
              ##        (assign, ":strength", reg0),
              ##        (lt, ":strength", 80),
              ##        (store_sub, ":strength", 100, ":strength"),
              ##        (val_div, ":strength", 20),
              ##        (val_add, ":num_centers", ":strength"),
            (try_end),
            (gt, ":num_centers", 0),
            (store_random_in_range, ":random_center", 0, ":num_centers"),
            (assign, ":result", -1),
            (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
              (eq, ":result", -1),
              (party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
              (party_slot_eq, ":center_no", slot_center_is_besieged_by, -1),
              (val_sub, ":random_center", 1),
              (try_begin),
                (eq, ":center_no", ":preferred_center_no"),
                (val_sub, ":random_center", 99),
              (try_end),
              ##        (try_begin),
              ##          (call_script, "script_party_calculate_regular_strength", ":center_no"),
              ##          (assign, ":strength", reg0),
              ##          (lt, ":strength", 80),
              ##          (store_sub, ":strength", 100, ":strength"),
              ##          (val_div, ":strength", 20),
              ##          (val_sub, ":random_center", ":strength"),
              ##        (try_end),
              (lt, ":random_center", 0),
              (assign, ":result", ":center_no"),
            (try_end),
            (assign, reg0, ":result"),
        ]),
        
        # script_cf_troop_get_random_leaded_town_or_village_except_center
        # Input: arg1 = troop_no, arg2 = except_center_no
        # Output: reg0 = center_no (Can fail)
        ("cf_troop_get_random_leaded_town_or_village_except_center",
          [
            (store_script_param_1, ":troop_no"),
            (store_script_param_2, ":except_center_no"),
            
            (assign, ":num_centers", 0),
            (try_for_range, ":center_no", centers_begin, centers_end),
              (neg|party_slot_eq, ":center_no", slot_party_type, spt_castle),
              (party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
              (neq, ":center_no", ":except_center_no"),
              (val_add, ":num_centers", 1),
            (try_end),
            
            (gt, ":num_centers", 0),
            (store_random_in_range, ":random_center", 0, ":num_centers"),
            (assign, ":end_cond", centers_end),
            (try_for_range, ":center_no", centers_begin, ":end_cond"),
              (neg|party_slot_eq, ":center_no", slot_party_type, spt_castle),
              (party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
              (neq, ":center_no", ":except_center_no"),
              (val_sub, ":random_center", 1),
              (lt, ":random_center", 0),
              (assign, ":target_center", ":center_no"),
              (assign, ":end_cond", 0),
            (try_end),
            (assign, reg0, ":target_center"),
        ]),
        
        # script_troop_write_owned_centers_to_s2
        # Input: arg1 = troop_no
        # Output: none
        ("troop_write_owned_centers_to_s2",
          [
            (store_script_param_1, ":troop_no"),
            
            (call_script, "script_get_number_of_hero_centers", ":troop_no"),
            (assign, ":no_centers", reg0),
            
            (str_store_troop_name, s5, ":troop_no"),
            
            (try_begin),
              (gt, ":no_centers", 1),
              (try_for_range, ":i_center", 1, ":no_centers"),
                (call_script, "script_troop_get_leaded_center_with_index", ":troop_no", ":i_center"),
                (str_store_party_name_link, s50, reg0),
                (try_begin),
                  (eq, ":i_center", 1),
                  (call_script, "script_troop_get_leaded_center_with_index", ":troop_no", 0),
                  (str_store_party_name_link, s51, reg0),
                  (str_store_string, s51, "str_s50_and_s51"),
                (else_try),
                  (str_store_string, s51, "str_s50_comma_s51"),
                (try_end),
              (try_end),
              (str_store_string, s2, "str_s5_is_the_ruler_of_s51"),
            (else_try),
              (eq, ":no_centers", 1),
              (call_script, "script_troop_get_leaded_center_with_index", ":troop_no", 0),
              (str_store_party_name_link, s51, reg0),
              (str_store_string, s2, "str_s5_is_the_ruler_of_s51"),
		  (else_try),
			(store_troop_faction, ":faction_no", ":troop_no"),
			(str_store_faction_name_link, s6, ":faction_no"),
			##diplomacy start+ make gender-correct
			#(troop_get_type, reg4, ":troop_no"),
			(assign, ":save_reg4", reg4),
		  (call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 4),
			(str_store_string, s2, "str_s5_is_a_nobleman_of_s6"),
			(assign, reg4, ":save_reg4"),
			##diplomacy end+
		  (try_end),
	  ]),
        
        ("troop_write_family_relations_to_s1",
          [
            (str_clear, s1),
            #redo, possibly using base from update_troop_notes
            
        ]),
        
        # script_write_family_relation_as_s3s_s2_to_s4
        
        # Inputs: arg1 = troop_no, arg2 = family_no (valid slot no after slot_troop_family_begin)
        # Outputs: s11 = what troop_1 is to troop_2, reg0 = strength of relationship, reg4 gender of troop_1. Normally, "$g_talk_troop" should be troop_2
        
      ("troop_get_family_relation_to_troop",
		[
		(store_script_param_1, ":troop_1"),
		(store_script_param_2, ":troop_2"),

		##diplomacy start+ use gender script
		#(troop_get_type, ":gender_1", ":troop_1"),
		(call_script, "script_dplmc_store_troop_is_female", ":troop_1"),
		(assign, ":gender_1", reg0),
		##diplomacy end+
		(assign, ":relation_strength", 0),

		(troop_get_slot, ":spouse_of_1", ":troop_1", slot_troop_spouse),
		(troop_get_slot, ":spouse_of_2", ":troop_2", slot_troop_spouse),

		(try_begin),
			(gt, ":spouse_of_1", -1),
			(troop_get_slot, ":father_of_spouse_of_1", ":spouse_of_1", slot_troop_father),
		(else_try),
			(assign, ":father_of_spouse_of_1", -1),
		(try_end),

		(try_begin),
			(gt, ":spouse_of_2", -1),
			(troop_get_slot, ":father_of_spouse_of_2", ":spouse_of_2", slot_troop_father),
		(else_try),
			(assign, ":father_of_spouse_of_2", -1),
		(try_end),

		(try_begin),
			(gt, ":spouse_of_2", -1),
			(troop_get_slot, ":mother_of_spouse_of_2", ":spouse_of_2", slot_troop_mother),
		(else_try),
			(assign, ":mother_of_spouse_of_2", -1),
		(try_end),

		(troop_get_slot, ":father_of_1", ":troop_1", slot_troop_father),
		(troop_get_slot, ":father_of_2", ":troop_2", slot_troop_father),

		#For the sake of simplicity, we can assume that all male aristocrats in prior generations either married commoners or procured their brides from the Old Country, thus discounting intermarriage
		(troop_get_slot, ":mother_of_1", ":troop_1", slot_troop_mother),
		(troop_get_slot, ":mother_of_2", ":troop_2", slot_troop_mother),

		##diplomacy start+
		#Fix a native bug where daughters are their own mothers
			#(fixed in this mod, but still affects old saved games)
			#REMOVED - Instead this occurs once in simple triggers

		##Adding paternal grandmother (begin mostly-unaltered section)
		(try_begin),
			(this_or_next|eq, ":father_of_1", "trp_player"),#dplmc+ added
			(is_between, ":father_of_1", companions_begin, kingdom_ladies_end),
			(troop_get_slot, ":paternal_grandfather_of_1", ":father_of_1", slot_troop_father),
			(troop_get_slot, ":paternal_grandmother_of_1", ":father_of_1", slot_troop_mother),#added
		(else_try),
			(assign, ":paternal_grandfather_of_1", -1),
			(assign, ":paternal_grandmother_of_1", -1),#added
		(try_end),

		(try_begin),
			(this_or_next|eq, ":father_of_2", "trp_player"),#dplmc+ added
			(is_between, ":father_of_2", companions_begin, kingdom_ladies_end),
			(troop_get_slot, ":paternal_grandfather_of_2", ":father_of_2", slot_troop_father),
			(troop_get_slot, ":paternal_grandmother_of_2", ":father_of_2", slot_troop_mother),#added
		(else_try),
			(assign, ":paternal_grandfather_of_2", -1),
			(assign, ":paternal_grandmother_of_2", -1),#added
		(try_end),
		#(end mostly-unaltered section)

		##Adding maternal grandfather and maternal grandmother
		(try_begin),
			(this_or_next|eq, ":mother_of_1", "trp_player"),#dplmc+ added
			(is_between, ":mother_of_1", companions_begin, kingdom_ladies_end),
			(troop_get_slot, ":maternal_grandfather_of_1", ":mother_of_1", slot_troop_father),
			(troop_get_slot, ":maternal_grandmother_of_1", ":mother_of_1", slot_troop_mother),
		(else_try),
			(assign, ":maternal_grandfather_of_1", -1),
			(assign, ":maternal_grandmother_of_1", -1),
		(try_end),

		(try_begin),
			(this_or_next|eq, ":mother_of_2", "trp_player"),#dplmc+ added
			(is_between, ":mother_of_2", companions_begin, kingdom_ladies_end),
			(troop_get_slot, ":maternal_grandfather_of_2", ":mother_of_2", slot_troop_father),
			(troop_get_slot, ":maternal_grandmother_of_2", ":mother_of_2", slot_troop_mother),
		(else_try),
			(assign, ":maternal_grandfather_of_2", -1),
			(assign, ":maternal_grandmother_of_2", -1),
		(try_end),
		##diplomacy end+

		(troop_get_slot, ":guardian_of_1", ":troop_1", slot_troop_guardian),
		(troop_get_slot, ":guardian_of_2", ":troop_2", slot_troop_guardian),

		(str_store_string, s11, "str_no_relation"),

		(try_begin),
		  (eq, ":troop_1", ":troop_2"),
		  #self
		(else_try),
		  ##diplomacy start+
		  (this_or_next|eq, ":spouse_of_2", ":troop_1"),#polygamy helper
		  ##diplomacy end+
		  (eq, ":spouse_of_1", ":troop_2"),
		  (assign, ":relation_strength", 20),
		  (try_begin),
			(eq, ":gender_1", 1),
			(str_store_string, s11, "str_wife"),
		  (else_try),
			(str_store_string, s11, "str_husband"),
		  (try_end),
		(else_try),
		  (eq, ":father_of_2", ":troop_1"),
		  (assign, ":relation_strength", 15),
		  (str_store_string, s11, "str_father"),
		(else_try),
		  (eq, ":mother_of_2", ":troop_1"),
		  (assign, ":relation_strength", 15),
		  (str_store_string, s11, "str_mother"),
		(else_try),
		  (this_or_next|eq, ":father_of_1", ":troop_2"),
		  (eq, ":mother_of_1", ":troop_2"),
		  (assign, ":relation_strength", 15),
		  (try_begin),
			(eq, ":gender_1", 1),
			(str_store_string, s11, "str_daughter"),
		  (else_try),
			(str_store_string, s11, "str_son"),
		  (try_end),
		##diplomacy start+
		(else_try),
		   #Check for half-siblings: sharing a father
		   (neq, ":father_of_1", -1),
		   (eq, ":father_of_1", ":father_of_2"),
		   (neq, ":mother_of_1", ":mother_of_2"),
		   (assign, ":relation_strength", 10),
		   (try_begin),
			 (eq, ":gender_1", 1),
			 (str_store_string, s11, "str_dplmc_half_sister"),
		   (else_try),
			 (str_store_string, s11, "str_dplmc_half_brother"),
		   (try_end),
	   (else_try),
		   #Check for half-siblings: sharing a mother
		   (neq, ":mother_of_1", -1),
		   (eq, ":mother_of_1", ":mother_of_2"),
		   (neq, ":father_of_1", ":father_of_2"),
		   (assign, ":relation_strength", 10),
		   (try_begin),
			 (eq, ":gender_1", 1),
			 (str_store_string, s11, "str_dplmc_half_sister"),
		   (else_try),
			 (str_store_string, s11, "str_dplmc_half_brother"),
		   (try_end),
		##diplomacy end+
		(else_try),
		  #(gt, ":father_of_1", -1), #necessary, as some lords do not have the father registered #dplmc+ replaced
		  (neq, ":father_of_1", -1), #dplmc+ added
		  (eq, ":father_of_1", ":father_of_2"),
		  (assign, ":relation_strength", 10),
		  (try_begin),
			(eq, ":gender_1", 1),
			(str_store_string, s11, "str_sister"),
		  (else_try),
			(str_store_string, s11, "str_brother"),
		  (try_end),
		(else_try),
		  (eq, ":guardian_of_2", ":troop_1"),
		  (assign, ":relation_strength", 10),
		  (try_begin),
			(eq, ":gender_1", 1),
			(str_store_string, s11, "str_sister"),
		  (else_try),
			(str_store_string, s11, "str_brother"),
		  (try_end),
		(else_try),
		  (eq, ":guardian_of_1", ":troop_2"),
		  (assign, ":relation_strength", 10),
		  (try_begin),
			(eq, ":gender_1", 1),
			(str_store_string, s11, "str_sister"),
		  (else_try),
			(str_store_string, s11, "str_brother"),
		  (try_end),
		##diplomacy start+
		(else_try),#polygamy, between two people married to the same person
		   (neq, ":spouse_of_1", -1),
		   (eq, ":spouse_of_2", ":spouse_of_1"),
		   (assign, ":relation_strength", 10),
		   (try_begin),
			  (eq, ":gender_1", 1),
			  (str_store_string, s11, "str_dplmc_sister_wife"),
		   (else_try),
			  (str_store_string, s11, "str_dplmc_co_husband"),
		   (try_end),
		##diplomacy end+
		(else_try),
		  #(gt, ":paternal_grandfather_of_1", -1),#dplmc+ replaced
		  (neq, ":father_of_2", -1),#dplmc+ added
		  (this_or_next|eq, ":maternal_grandfather_of_1", ":father_of_2"),#dplmc+ added
		  (eq, ":paternal_grandfather_of_1", ":father_of_2"),
		  (assign, ":relation_strength", 4),
		  (try_begin),
			(eq, ":gender_1", 1),
			(str_store_string, s11, "str_niece"),
		  (else_try),
			(str_store_string, s11, "str_nephew"),
		  (try_end),
		##diplomacy start+: add niece/nephew through mother
		(else_try),
		  (neq, ":mother_of_2", -1),
		  (this_or_next|eq, ":maternal_grandmother_of_1", ":mother_of_2"),
		  (eq, ":paternal_grandmother_of_1", ":mother_of_2"),
		  (assign, ":relation_strength", 4),
		  (try_begin),
			(eq, ":gender_1", tf_female),
			(str_store_string, s11, "str_niece"),
		  (else_try),
			(str_store_string, s11, "str_nephew"),
		  (try_end),
		##diplomacy end+
		(else_try), #specifically aunt and uncle by blood -- i assume that in a medieval society with lots of internal family conflicts, they would not include aunts and uncles by marriage
		  #(gt, ":paternal_grandfather_of_2", -1),#dplmc+ replaced
		  (neq, ":father_of_1", -1),#dplmc+ added
		  (this_or_next|eq, ":maternal_grandfather_of_2", ":father_of_1"),#dplmc+ added
		  (eq, ":paternal_grandfather_of_2", ":father_of_1"),
		  (assign, ":relation_strength", 4),
		  (try_begin),
			(eq, ":gender_1", 1),
			(str_store_string, s11, "str_aunt"),
		  (else_try),
			(str_store_string, s11, "str_uncle"),
		  (try_end),
		##diplomacy start+
		#blood uncles & blood aunts, continued (via mother)
		(else_try),
		  (neq, ":mother_of_1", -1),
		  (this_or_next|eq, ":maternal_grandmother_of_2", ":mother_of_1"),
		  (eq, ":paternal_grandmother_of_2", ":mother_of_1"),
		  (assign, ":relation_strength", 4),
		  (try_begin),
			(eq, ":gender_1", tf_female),
			(str_store_string, s11, "str_aunt"),
		  (else_try),
			(str_store_string, s11, "str_uncle"),
		  (try_end),
		##diplomacy end+
		(else_try),
		  #(gt, ":paternal_grandfather_of_1", 0),#dplmc+ replaced (why was this one "gt 0" but the previous "gt -1"?)
		  (neq, ":paternal_grandfather_of_1", -1),#dplmc+ added
		  (this_or_next|eq, ":maternal_grandfather_of_2", ":paternal_grandfather_of_1"),#dplmc+ added
		  (eq, ":paternal_grandfather_of_2", ":paternal_grandfather_of_1"),
		  (assign, ":relation_strength", 2),
		  (str_store_string, s11, "str_cousin"),
		##diplomacy start+
		#Add cousin via paternal grandmother or maternal grandparents
		(else_try),
		  (neq, ":maternal_grandfather_of_1", -1),
		  (this_or_next|eq, ":maternal_grandfather_of_2", ":maternal_grandfather_of_1"),
		  (eq, ":paternal_grandfather_of_2", ":maternal_grandfather_of_1"),
		  (assign, ":relation_strength", 2),
		  (str_store_string, s11, "str_cousin"),
		(else_try),
		  (neq, ":paternal_grandmother_of_1", -1),
		  (this_or_next|eq, ":maternal_grandmother_of_2", ":paternal_grandmother_of_1"),
		  (eq, ":paternal_grandmother_of_2", ":paternal_grandmother_of_1"),
		  (assign, ":relation_strength", 2),
		  (str_store_string, s11, "str_cousin"),
		(else_try),
		  (neq, ":maternal_grandmother_of_1", -1),
		  (this_or_next|eq, ":maternal_grandmother_of_2", ":maternal_grandmother_of_1"),
		  (eq, ":paternal_grandmother_of_2", ":maternal_grandmother_of_1"),
		  (assign, ":relation_strength", 2),
		  (str_store_string, s11, "str_cousin"),
		##diplomacy end+
		(else_try),
		  (eq, ":father_of_spouse_of_1", ":troop_2"),
		  (assign, ":relation_strength", 5),
		  (try_begin),
			(eq, ":gender_1", 1),
			(str_store_string, s11, "str_daughterinlaw"),
		  (else_try),
			(str_store_string, s11, "str_soninlaw"),
		  (try_end),
		(else_try),
		  (eq, ":father_of_spouse_of_2", ":troop_1"),
		  (assign, ":relation_strength", 5),
		  (str_store_string, s11, "str_fatherinlaw"),
		(else_try),
		  (eq, ":mother_of_spouse_of_2", ":troop_1"),
		  (neq, ":mother_of_spouse_of_2", "trp_player"), #May be necessary if mother for troops not set to -1
		  (assign, ":relation_strength", 5),
		  (str_store_string, s11, "str_motherinlaw"),

		(else_try),
		  #(gt, ":father_of_spouse_of_1", -1), #necessary #dplmc+ replaced
		  (neq, ":father_of_spouse_of_1", -1), #dplmc+ added
		  (eq, ":father_of_spouse_of_1", ":father_of_2"),
		  (assign, ":relation_strength", 5),
		  (try_begin),
			(eq, ":gender_1", 1),
			(str_store_string, s11, "str_sisterinlaw"),
		  (else_try),
			(str_store_string, s11, "str_brotherinlaw"),
		  (try_end),
		(else_try),
		  #(gt, ":father_of_spouse_of_2", -1), #necessary #dplmc+ replaced
		  (neq, ":father_of_spouse_of_2", -1), #dplmc+ added
		  (eq, ":father_of_spouse_of_2", ":father_of_1"),
		  (assign, ":relation_strength", 5),
		  (try_begin),
			(eq, ":gender_1", 1),
			(str_store_string, s11, "str_sisterinlaw"),
		  (else_try),
			(str_store_string, s11, "str_brotherinlaw"),
		  (try_end),
		(else_try),
	#	  (gt, ":spouse_of_2", -1), #necessary to avoid bug #dplmc+ replaced
		  (neq, ":spouse_of_2", -1), #dplmc+ added
		  (troop_slot_eq, ":spouse_of_2", slot_troop_guardian, ":troop_1"),
		  (assign, ":relation_strength", 5),
		  (try_begin),
			#(eq, ":gender_1", 1),#dplmc+ replaced
			(eq, ":gender_1", tf_female),#dplmc+ added
			(str_store_string, s11, "str_sisterinlaw"),
		  (else_try),
			(str_store_string, s11, "str_brotherinlaw"),
		  (try_end),
		(else_try),
		  #(gt, ":spouse_of_1", -1), #necessary to avoid bug #dplmc+ replaced
		  (neq, ":spouse_of_1", -1), #dplmc+ added
		  (troop_slot_eq, ":spouse_of_1", slot_troop_guardian, ":troop_2"),
		  (assign, ":relation_strength", 5),
		  (try_begin),
			(eq, ":gender_1", 1),
			(str_store_string, s11, "str_sisterinlaw"),
		  (else_try),
			(str_store_string, s11, "str_brotherinlaw"),
		  (try_end),
		(else_try),
		  #grandchild
		  (neq, ":troop_2", -1),
		   (this_or_next|eq, ":paternal_grandfather_of_1", ":troop_2"),
		   (this_or_next|eq, ":maternal_grandfather_of_1", ":troop_2"),
		   (this_or_next|eq, ":paternal_grandmother_of_1", ":troop_2"),
			   (eq, ":maternal_grandmother_of_1", ":troop_2"),
		   (assign, ":relation_strength", 4),
		  (try_begin),
			(eq, ":gender_1", tf_female),
			(str_store_string, s11, "str_dplmc_granddaughter"),
		  (else_try),
			(str_store_string, s11, "str_dplmc_grandson"),
		  (try_end),
		(else_try),
		   #grandparent
		   (neq, ":troop_1", -1),
		   (this_or_next|eq, ":paternal_grandfather_of_2", ":troop_1"),
		   (this_or_next|eq, ":maternal_grandfather_of_2", ":troop_1"),
		   (this_or_next|eq, ":paternal_grandmother_of_2", ":troop_1"),
			   (eq, ":maternal_grandmother_of_2", ":troop_1"),
		  (assign, ":relation_strength", 4),
		  (try_begin),
			(eq, ":gender_1", tf_female),
			(str_store_string, s11, "str_dplmc_grandmother"),
		  (else_try),
			(str_store_string, s11, "str_dplmc_grandfather"),
		  (try_end),
		(try_end),

		##diplomacy start+
		##Add relations for rulers not already encoded
		(try_begin),
			(eq, ":relation_strength", 0),
			(neq, ":troop_1", ":troop_2"),
			(try_begin),
				#Lady Isolla of Suno's father King Esterich was King Harlaus's cousin,
				#making them first cousins once removed.  Assign a weight of "1"
				#to this (for reference, the lowest value normally given in Native is 2).
				(this_or_next|eq, ":troop_1", "trp_kingdom_1_lord"),
					(eq, ":troop_1", "trp_kingdom_1_pretender"),
				(this_or_next|eq, ":troop_2", "trp_kingdom_1_lord"),
					(eq, ":troop_2", "trp_kingdom_1_pretender"),
				(assign, ":relation_strength", 1),
				(str_store_string, s11, "str_cousin"),
			(else_try),
				#Prince Valdym's uncle was Regent Burelek, father of King Yaroglek,
				#making the two of them first cousins.
				(this_or_next|eq, ":troop_1", "trp_kingdom_2_lord"),
					(eq, ":troop_1", "trp_kingdom_2_pretender"),
				(this_or_next|eq, ":troop_2", "trp_kingdom_2_lord"),
					(eq, ":troop_2", "trp_kingdom_2_pretender"),
				(assign, ":relation_strength", 2),
				(str_store_string, s11, "str_cousin"),
			(else_try),
				#Sanjar Khan and Dustum Khan were both sons of Janakir Khan
				#(although by different mothers) making them half-brothers.
				(this_or_next|eq, ":troop_1", "trp_kingdom_3_lord"),
					(eq, ":troop_1", "trp_kingdom_3_pretender"),
				(this_or_next|eq, ":troop_2", "trp_kingdom_3_lord"),
					(eq, ":troop_2", "trp_kingdom_3_pretender"),
				(assign, ":relation_strength", 10),
				(str_store_string, s11, "str_dplmc_half_brother"),
				#Adjust their parentage to make this work automatically
				(try_begin),
					(troop_slot_eq, ":troop_1", slot_troop_father, -1),
					(troop_slot_eq, ":troop_2", slot_troop_father, -1),
					#Set their "father" slot to a number guaranteed not to have spurious collisions
					(store_mul, ":janakir_khan", "trp_kingdom_3_lord", DPLMC_VIRTUAL_RELATIVE_MULTIPLIER),#defined in module_constants.py
					(val_add, ":janakir_khan", DPLMC_VIRTUAL_RELATIVE_FATHER_OFFSET),#defined in module_constants.py
					(troop_set_slot, ":troop_1", slot_troop_father, ":janakir_khan"),
					(troop_set_slot, ":troop_2", slot_troop_father, ":janakir_khan"),
					#Differentiate their mothers, so they are half-brothers instead of full-brothers
					(try_begin),
						(troop_slot_eq, ":troop_1", slot_troop_mother, -1),
						(store_mul, reg0, ":troop_1", DPLMC_VIRTUAL_RELATIVE_MULTIPLIER),
						(val_add, reg0, DPLMC_VIRTUAL_RELATIVE_MULTIPLIER),
						(troop_set_slot, ":troop_1", slot_troop_mother, reg0),
					(try_end),
					(try_begin),
						(troop_slot_eq, ":troop_2", slot_troop_mother, -1),
						(store_mul, reg0, ":troop_2", DPLMC_VIRTUAL_RELATIVE_MULTIPLIER),
						(val_add, reg0, DPLMC_VIRTUAL_RELATIVE_MULTIPLIER),
						(troop_set_slot, ":troop_2", slot_troop_mother, reg0),
					(try_end),
				(try_end),
			(try_end),
		(try_end),
		##Add uncles and aunts by marriage.
		##In Native, the relation strength for blood uncles/aunts is 4, and for cousins is 2.
		##In light of this I've decided to set the relation strength for aunts/uncles by marriage to 2.
		(try_begin),
			(lt, ":relation_strength", 2),#Skip this check if a stronger relation has been found.
			#Test if troop_1 is married to a sibling of one of troop_2's parents, pt. 1
			(ge, ":spouse_of_1", 0),
			(neg|troop_slot_eq, ":spouse_of_1", slot_troop_father, -1),
			(this_or_next|troop_slot_eq, ":spouse_of_1", slot_troop_father, ":paternal_grandfather_of_2"),
				(troop_slot_eq, ":spouse_of_1", slot_troop_father, ":maternal_grandfather_of_2"),
			(assign, ":relation_strength", 2),
			(try_begin),
				(eq, ":gender_1", tf_female),
				(str_store_string, s11, "str_aunt"),
			(else_try),
				(str_store_string, s11, "str_uncle"),
			(try_end),
		(else_try),
			(lt, ":relation_strength", 2),#Skip this check if a stronger relation has been found.
			#Test if troop_1 is married to a sibling of one of troop_2's parents, pt. 2
			(ge, ":spouse_of_1", 0),
			(neg|troop_slot_eq, ":spouse_of_1", slot_troop_mother, -1),
			(this_or_next|troop_slot_eq, ":spouse_of_1", slot_troop_mother, ":paternal_grandmother_of_2"),
				(troop_slot_eq, ":spouse_of_1", slot_troop_mother, ":maternal_grandmother_of_2"),
			(assign, ":relation_strength", 2),
			(try_begin),
				(eq, ":gender_1", tf_female),
				(str_store_string, s11, "str_aunt"),
			(else_try),
				(str_store_string, s11, "str_uncle"),
			(try_end),
		(else_try),
			(lt, ":relation_strength", 2),#Skip this check if a stronger relation has been found.
			#Test if troop_2 is married to a sibling of one of troop_1's parents, pt. 1
			(ge, ":spouse_of_2", 0),
			(neg|troop_slot_eq, ":spouse_of_2", slot_troop_father, -1),
			(this_or_next|troop_slot_eq, ":spouse_of_2", slot_troop_father, ":paternal_grandfather_of_1"),
				(troop_slot_eq, ":spouse_of_2", slot_troop_father, ":maternal_grandfather_of_1"),
			(assign, ":relation_strength", 2),
			(try_begin),
				(eq, ":gender_1", tf_female),
				(str_store_string, s11, "str_niece"),
			(else_try),
				(str_store_string, s11, "str_nephew"),
			(try_end),
		(else_try),
			(lt, ":relation_strength", 2),#Skip this check if a stronger relation has been found.
			#Test if troop_2 is married to a sibling of one of troop_1's parents, pt. 2
			(ge, ":spouse_of_2", 0),
			(neg|troop_slot_eq, ":spouse_of_2", slot_troop_mother, -1),
			(this_or_next|troop_slot_eq, ":spouse_of_2", slot_troop_mother, ":paternal_grandmother_of_1"),
				(troop_slot_eq, ":spouse_of_2", slot_troop_mother, ":maternal_grandmother_of_1"),
			(assign, ":relation_strength", 2),
			(try_begin),
				(eq, ":gender_1", tf_female),
				(str_store_string, s11, "str_niece"),
			(else_try),
				(str_store_string, s11, "str_nephew"),
			(try_end),
		(try_end),
		##diplomacy end+
		(assign, reg4, ":gender_1"),
		(assign, reg0, ":relation_strength"),
	]),


        # script_complete_family_relations
        # Inputs: none
        # Outputs: none
        
        #complete family relations removed
        
        # script_collect_friendly_parties
        # Fills the party p_collective_friends with the members of parties attached to main_party and ally_party_no
        ("collect_friendly_parties",
          [
            (party_collect_attachments_to_party, "p_main_party", "p_collective_friends"),
            (try_begin),
              (gt, "$g_ally_party", 0),
              (party_collect_attachments_to_party, "$g_ally_party", "p_temp_party"),
              (assign, "$g_move_heroes", 1),
              (call_script, "script_party_add_party", "p_collective_friends", "p_temp_party"),
            (try_end),
        ]),
        
        # script_encounter_calculate_fit
        # Input: arg1 = troop_no
        # Output: none
        ("encounter_calculate_fit",
          [
            #(assign, "$g_enemy_fit_for_battle_old",  "$g_enemy_fit_for_battle"),
            #(assign, "$g_friend_fit_for_battle_old", "$g_friend_fit_for_battle"),
            #(assign, "$g_main_party_fit_for_battle_old", "$g_main_party_fit_for_battle"),
            (call_script, "script_party_count_fit_for_battle", "p_main_party"),
            #(assign, "$g_main_party_fit_for_battle", reg(0)),
            (call_script, "script_collect_friendly_parties"),
            (call_script, "script_party_count_fit_for_battle", "p_collective_friends"),
            (assign, "$g_friend_fit_for_battle", reg(0)),
            
            (party_clear, "p_collective_ally"),
            (try_begin),
              (gt, "$g_ally_party", 0),
              (party_is_active, "$g_ally_party"),
              (party_collect_attachments_to_party, "$g_ally_party", "p_collective_ally"),
              #(call_script, "script_party_count_fit_for_battle", "p_collective_ally"),
              #(val_add, "$g_friend_fit_for_battle", reg(0)),
            (try_end),
            
            (party_clear, "p_collective_enemy"),
            (try_begin),
              (party_is_active, "$g_enemy_party"),
              (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),
            (try_end),
            (call_script, "script_party_count_fit_for_battle", "p_collective_enemy"),
            (assign, "$g_enemy_fit_for_battle", reg(0)),
            (assign, reg11, "$g_enemy_fit_for_battle"),
            (assign, reg10, "$g_friend_fit_for_battle"),
        ]),
        
        # script_encounter_init_variables
        # Input: arg1 = troop_no
        # Output: none
        ("encounter_init_variables",
          [
            (assign, "$capture_screen_shown", 0),
            (assign, "$loot_screen_shown", 0),
            (assign, "$thanked_by_ally_leader", 0),
            (assign, "$g_battle_result", 0),
            (assign, "$cant_leave_encounter", 0),
            (assign, "$cant_talk_to_enemy", 0),
            (assign, "$last_defeated_hero", 0),
            (assign, "$last_freed_hero", 0),
            
			(call_script, "script_encounter_calculate_fit"),
			(call_script, "script_party_copy", "p_main_party_backup", "p_main_party"),
			##diplomacy start+
			#If terrain advantage is enabled, use it to initialize the variables.
			(assign, ":terrain_code", -1),
			(try_begin),
				(eq, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
				(lt, "$g_encounter_is_in_village", 1),#Do not apply to village encounters
				(try_begin),
					(encountered_party_is_attacker),
					(call_script, "script_dplmc_get_terrain_code_for_battle", "$g_encountered_party", "p_main_party"),
				(else_try),
					(call_script, "script_dplmc_get_terrain_code_for_battle", "p_main_party", "$g_encountered_party"),
				(try_end),
				(assign, ":terrain_code", reg0),
				#calculate party strength with terrain
				(call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_main_party", ":terrain_code", 0, 1),
				(assign, "$g_starting_strength_main_party", reg0),
				(try_begin),
					#Print debug Message
					(ge, "$cheat_mode", 1),
					(assign, reg2, ":terrain_code"),
					(display_message, "@{!}DEBUG - Main party raw strength {reg1}, terrain code {reg2}, modified strength {reg0}"),
				(try_end),
				#calculate enemy strength with terrain
				(call_script, "script_party_copy", "p_encountered_party_backup", "p_collective_enemy"),
				(call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_collective_enemy", ":terrain_code", 0, 1),
				(assign, "$g_starting_strength_enemy_party", reg0),
				(assign, "$g_strength_contribution_of_player", 100),
				(try_begin),
					(ge, "$cheat_mode", 1),#debug
					(assign, reg2, ":terrain_code"),
					(display_message, "@{!} DEBUG - Enemy party raw strength {reg1}, terrain code {reg2}, modified strength {reg0}"),
				(try_end),
				#calculate friends strength with terrain
				(call_script, "script_party_copy", "p_collective_friends_backup", "p_collective_friends"),
				(call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_collective_friends", ":terrain_code", 0, 1),
				(assign, "$g_starting_strength_friends", reg0),
			(else_try),
				##Calculate all party strengths without terrain:
				#calculate main party strength
				(call_script, "script_party_calculate_strength", "p_main_party", 0),
				(assign, "$g_starting_strength_main_party", reg0),
				#calculate enemy strength
				(call_script, "script_party_copy", "p_encountered_party_backup", "p_collective_enemy"),
				(call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
				(assign, "$g_starting_strength_enemy_party", reg0),
				(assign, "$g_strength_contribution_of_player", 100),
				#calculate friends strength
				(call_script, "script_party_copy", "p_collective_friends_backup", "p_collective_friends"),
				(call_script, "script_party_calculate_strength", "p_collective_friends", 0),
				(assign, "$g_starting_strength_friends", reg0),
			(try_end),
			##diplomacy end+
            
            (store_mul, "$g_strength_contribution_of_player","$g_starting_strength_main_party", 100), # reduce contribution if we are helping someone.
            
            (try_begin),
              (gt, "$g_starting_strength_friends", 0), #this new to prevent occasional div by zero error
              (val_div, "$g_strength_contribution_of_player","$g_starting_strength_friends"),
            (else_try),
              (assign, "$g_strength_contribution_of_player", 100), #Or zero, maybe
            (try_end),
            
            (party_clear, "p_routed_enemies"), #new
            (assign, "$num_routed_us", 0),#newtoday
            (assign, "$num_routed_allies", 0),#newtoday
            (assign, "$num_routed_enemies", 0),#newtoday
            (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
            (try_for_range, ":i_stack", 0, ":num_stacks"),
              (party_stack_get_troop_id, ":stack_troop_id", "p_main_party", ":i_stack"),
              (try_begin),
                (troop_set_slot, ":stack_troop_id", slot_troop_player_routed_agents, 0),
                #(troop_set_slot, ":stack_troop_id", slot_troop_enemy_routed_agents, 0),
                #(troop_set_slot, ":stack_troop_id", slot_troop_ally_routed_agents, 0),
              (try_end),
            (try_end),
            
            (party_get_num_companion_stacks, ":num_stacks", "p_collective_friends"),
            (try_for_range, ":i_stack", 0, ":num_stacks"),
              (party_stack_get_troop_id, ":stack_troop_id", "p_collective_friends", ":i_stack"),
              (try_begin),
                #(troop_set_slot, ":stack_troop_id", slot_troop_player_routed_agents, 0),
                #(troop_set_slot, ":stack_troop_id", slot_troop_enemy_routed_agents, 0),
                (troop_set_slot, ":stack_troop_id", slot_troop_ally_routed_agents, 0),
              (try_end),
            (try_end),
            
            (party_get_num_companion_stacks, ":num_stacks", "p_collective_enemy"),
            (try_for_range, ":i_stack", 0, ":num_stacks"),
              (party_stack_get_troop_id, ":stack_troop_id", "p_collective_enemy", ":i_stack"),
              (try_begin),
                #(troop_set_slot, ":stack_troop_id", slot_troop_player_routed_agents, 0),
                (troop_set_slot, ":stack_troop_id", slot_troop_enemy_routed_agents, 0),
                #(troop_set_slot, ":stack_troop_id", slot_troop_ally_routed_agents, 0),
              (try_end),
            (try_end),
            
            (try_for_range, ":cur_faction", fac_kingdom_1, fac_kingdoms_end),
              (faction_set_slot, ":cur_faction", slot_faction_num_routed_agents, 0),
            (try_end),
            
            (assign, "$routed_party_added", 0), #new
            (party_clear, "p_total_enemy_casualties"), #new
            
            #      (try_begin),
            #        (gt, "$g_ally_party", 0),
            #        (call_script, "script_party_copy", "p_ally_party_backup", "p_collective_ally"),
            #        (call_script, "script_party_calculate_strength", "p_collective_ally"),
            #        (assign, "$g_starting_strength_ally_party", reg0),
            #        (store_add, ":starting_strength_factor_combined","$g_starting_strength_ally_party","$g_starting_strength_main_party"),
            #         (store_mul, "$g_strength_contribution_of_player","$g_starting_strength_main_party", 80), #reduce contribution if we are helping someone.
            #        (val_div, "$g_strength_contribution_of_player",":starting_strength_factor_combined"),
            #      (try_end),
        ]),
        
        # script_calculate_renown_value
        # Input: arg1 = troop_no
        # Output: fills $battle_renown_value
		  ("calculate_renown_value",
		   [
			  ##diplomacy start+
			  #If terrain advantage is enabled, use it to avoid messing up cached
			  #strength values, but do not take it into consideration for renown
			  #granted.
			  (assign, ":main_party_strength", 1),
			  (assign, ":enemy_strength", 1),
			  (assign, ":friends_strength", 1),
			  (assign, ":terrain_code", -1),
			  (try_begin),
				 (eq, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
				 (try_begin),
					(encountered_party_is_attacker),
					(call_script, "script_dplmc_get_terrain_code_for_battle", "$g_encountered_party", "p_main_party"),
				 (else_try),
					(call_script, "script_dplmc_get_terrain_code_for_battle", "p_main_party", "$g_encountered_party"),
				 (try_end),
				 (assign, ":terrain_code", reg0),
				 ##Alternate option: calculate with terrain, but don't use it for renown
				 #(but do use it to update the cached strength for the party)
				 (call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_main_party", ":terrain_code",0,1),
				 (assign, ":main_party_strength", reg1),#use non-terrain version!
				 (call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_collective_enemy", ":terrain_code",0,1),
				 (assign, ":enemy_strength", reg1),#use non-terrain version!
				 (call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_collective_friends", ":terrain_code",0,1),
				 (assign, ":friends_strength", reg1),#use non-terrain version!
			  (else_try),
				  ##Original option: calculate without terrain
				  (call_script, "script_party_calculate_strength", "p_main_party", 0),
				  (assign, ":main_party_strength", reg0),
				  (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
				  (assign, ":enemy_strength", reg0),
				  (call_script, "script_party_calculate_strength", "p_collective_friends", 0),
				  (assign, ":friends_strength", reg0),
			  (try_end),
			  ##diplomacy end+

			  (val_add, ":friends_strength", 1),
			  (store_mul, ":enemy_strength_ratio", ":enemy_strength", 100),
			  (val_div, ":enemy_strength_ratio", ":friends_strength"),

			  (assign, ":renown_val", ":enemy_strength"),
			  (val_mul, ":renown_val", ":enemy_strength_ratio"),
			  (val_div, ":renown_val", 100),

			  (val_mul, ":renown_val", ":main_party_strength"),
			  (val_div, ":renown_val",":friends_strength"),

			  (store_div, "$battle_renown_value", ":renown_val", 5),
			  (val_min, "$battle_renown_value", 2500),
			  (convert_to_fixed_point, "$battle_renown_value"),
			  (store_sqrt, "$battle_renown_value", "$battle_renown_value"),
			  (convert_from_fixed_point, "$battle_renown_value"),
			  (assign, reg8, "$battle_renown_value"),
			  (display_message, "@Renown value for this battle is {reg8}.",0xFFFFFFFF),
		  ]),
        
        
        ##  # script_calculate_weekly_wage_for_player
        ##  # Input: none
        ##  # Output: none
        ##  ("calculate_weekly_wage_for_player",
        ##    [
        ##        (call_script, "script_calculate_weekly_party_wage", "p_main_party"),
        ##        (assign, ":result", reg0),
        ##        (try_for_parties, ":party_no"),
        ##          (store_faction_of_party, ":party_faction", ":party_no"),
        ##          (eq, ":party_faction", "fac_player_supporters_faction"),
        ##          (call_script, "script_calculate_weekly_party_wage", ":party_no"),
        ##          (val_add, ":result", reg0),
        ##        (try_end),
        ##        (assign, reg0, ":result"),
        ##  ]),
        
        
        # script_get_first_agent_with_troop_id
        # Input: arg1 = troop_no
        # Output: agent_id
        ("cf_get_first_agent_with_troop_id",
          [
            (store_script_param_1, ":troop_no"),
            #      (store_script_param_2, ":agent_no_to_begin_searching_after"),
            (assign, ":result", -1),
            (try_for_agents, ":cur_agent"),
              (eq, ":result", -1),
              ##        (try_begin),
              ##          (eq, ":cur_agent", ":agent_no_to_begin_searching_after"),
              ##          (assign, ":agent_no_to_begin_searching_after", -1),
              ##        (try_end),
              ##        (eq, ":agent_no_to_begin_searching_after", -1),
              (agent_get_troop_id, ":cur_troop_no", ":cur_agent"),
              (eq, ":cur_troop_no", ":troop_no"),
              (assign, ":result", ":cur_agent"),
            (try_end),
            (assign, reg0, ":result"),
            (neq, reg0, -1),
        ]),
        
        
        # script_cf_team_get_average_position_of_agents_with_type_to_pos1
        # Input: arg1 = team_no, arg2 = class_no (grc_everyone, grc_infantry, grc_cavalry, grc_archers, grc_heroes)
        # Output: none, pos1 = average_position (0,0,0 if there are no matching agents)
        ("cf_team_get_average_position_of_agents_with_type_to_pos1",
          [
            (store_script_param_1, ":team_no"),
            (store_script_param_2, ":division_no"),
            (assign, ":total_pos_x", 0),
            (assign, ":total_pos_y", 0),
            (assign, ":total_pos_z", 0),
            (assign, ":num_agents", 0),
            (set_fixed_point_multiplier, 100),
            (try_for_agents, ":cur_agent"),
              (agent_is_alive, ":cur_agent"),
              (agent_is_human, ":cur_agent"),
              (agent_get_team, ":cur_team_no", ":cur_agent"),
              (eq, ":cur_team_no", ":team_no"),
              (agent_get_division, ":cur_agent_division", ":cur_agent"),
              (this_or_next|eq, ":division_no", grc_everyone),
              (eq, ":division_no", ":cur_agent_division"),
              (agent_get_position, pos1, ":cur_agent"),
              (position_get_x, ":cur_pos_x", pos1),
              (val_add, ":total_pos_x", ":cur_pos_x"),
              (position_get_y, ":cur_pos_y", pos1),
              (val_add, ":total_pos_y", ":cur_pos_y"),
              (position_get_z, ":cur_pos_z", pos1),
              (val_add, ":total_pos_z", ":cur_pos_z"),
              (val_add, ":num_agents", 1),
            (try_end),
            (gt, ":num_agents", 1),
            (val_div, ":total_pos_x", ":num_agents"),
            (val_div, ":total_pos_y", ":num_agents"),
            (val_div, ":total_pos_z", ":num_agents"),
            (init_position, pos1),
            (position_move_x, pos1, ":total_pos_x"),
            (position_move_y, pos1, ":total_pos_y"),
            (position_move_z, pos1, ":total_pos_z"),
        ]),
        
        # script_cf_turn_windmill_fans
        # Input: arg1 = instance_no (none = 0)
        # Output: none
        ("cf_turn_windmill_fans",
          [(store_script_param_1, ":instance_no"),
            (scene_prop_get_instance, ":windmill_fan_object", "spr_windmill_fan_turning", ":instance_no"),
            (ge, ":windmill_fan_object", 0),
            (prop_instance_get_position, pos1, ":windmill_fan_object"),
            (position_rotate_y, pos1, 10),
            (prop_instance_animate_to_position, ":windmill_fan_object", pos1, 100),
            (val_add, ":instance_no", 1),
            (call_script, "script_cf_turn_windmill_fans", ":instance_no"),
        ]),
        
        # script_print_party_members
        # Input: arg1 = party_no
        # Output: s51 = output string. "noone" if the party is empty
        ("print_party_members",
          [
            (store_script_param_1, ":party_no"),
            (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
            (assign, reg10, ":num_stacks"),
            (try_for_range, ":i_stack", 0, ":num_stacks"),
              (party_stack_get_troop_id, ":stack_troop",":party_no",":i_stack"),
              (troop_is_hero, ":stack_troop"),
              (try_begin),
                (eq, ":i_stack", 0),
                (str_store_troop_name, s51, ":stack_troop"),
              (try_end),
              (str_store_troop_name, s52, ":stack_troop"),
              (try_begin),
                (eq, ":i_stack", 1),
                (str_store_string, s51, "str_s52_and_s51"),
              (else_try),
                (gt, ":i_stack", 1),
                (str_store_string, s51, "str_s52_comma_s51"),
              (try_end),
            (try_end),
            (try_begin),
              (eq, ":num_stacks", 0),
              (str_store_string, s51, "str_noone"),
            (try_end),
        ]),
        
        # script_round_value
        # Input: arg1 = value
        # Output: reg0 = rounded_value
        ("round_value",
          [
            (store_script_param_1, ":value"),
            (try_begin),
              (lt, ":value", 100),
              (neq, ":value", 0),
              (val_add, ":value", 5),
              (val_div, ":value", 10),
              (val_mul, ":value", 10),
              (try_begin),
                (eq, ":value", 0),
                (assign, ":value", 5),
              (try_end),
            (else_try),
              (lt, ":value", 300),
              (val_add, ":value", 25),
              (val_div, ":value", 50),
              (val_mul, ":value", 50),
            (else_try),
              (val_add, ":value", 50),
              (val_div, ":value", 100),
              (val_mul, ":value", 100),
            (try_end),
            (assign, reg0, ":value"),
        ]),
        
        
        ##  # script_print_productions_above_or_below_50
        ##  # Input: arg1 = center_no, arg2 = sign of the production, 1 if produced goods, -1 if consumed goods
        ##  # Output: s51 = output string. "nothing" if there are no productions above or below 50
        ##  ("print_productions_above_or_below_50",
        ##    [(store_script_param_1, ":center_no"),
        ##      (store_script_param_2, ":sign"),
        ##      (store_sub, ":item_to_slot", slot_town_trade_good_productions_begin, trade_goods_begin),
        ##      (assign, ":cur_print_index", 0),
        ##      (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
        ##        (store_add, ":cur_good_slot", ":cur_goods", ":item_to_slot"),
        ##        (party_get_slot, ":cur_production", ":center_no", ":cur_good_slot"),
        ##        (val_mul, ":cur_production", ":sign"),
        ##        (ge, ":cur_production", 50),
        ##        (try_begin),
        ##          (eq, ":cur_print_index", 0),
        ##          (str_store_item_name, s51, ":cur_goods"),
        ##        (try_end),
        ##        (str_store_item_name, s50, ":cur_goods"),
        ##        (try_begin),
        ##          (eq, ":cur_print_index", 1),
        ##          (str_store_string, s51, "str_s50_and_s51"),
        ##        (else_try),
        ##          (gt, ":cur_print_index", 1),
        ##          (str_store_string, s51, "str_s50_comma_s51"),
        ##        (try_end),
        ##        (val_add, ":cur_print_index", 1),
        ##      (try_end),
        ##      (try_begin),
        ##        (eq, ":cur_print_index", 0),
        ##        (str_store_string, s51, "str_nothing"),
        ##      (try_end),
        ##  ]),
        
        # script_change_banners_and_chest
        # Input: none
        # Output: none
        ("change_banners_and_chest",
          [(party_get_slot, ":cur_leader", "$g_encountered_party", slot_town_lord),
            (try_begin),
              (ge, ":cur_leader", 0),
              #normal_banner_begin
              (troop_get_slot, ":troop_banner_object", ":cur_leader", slot_troop_banner_scene_prop),
              (gt, ":troop_banner_object", 0),
              (replace_scene_props, banner_scene_props_begin, ":troop_banner_object"),
            (else_try),
              (replace_scene_props, banner_scene_props_begin, "spr_empty"),
              #custom_banner_begin
              #       (troop_get_slot, ":flag_spr", ":cur_leader", slot_troop_custom_banner_flag_type),
              #       (ge, ":flag_spr", 0),
              #       (val_add, ":flag_spr", custom_banner_flag_scene_props_begin),
              #       (replace_scene_props, banner_scene_props_begin, ":flag_spr"),
              #     (else_try),
              #       (replace_scene_props, banner_scene_props_begin, "spr_empty"),
            (try_end),
            (try_begin),
              (neq, ":cur_leader", "trp_player"),
              (replace_scene_props, "spr_player_chest", "spr_locked_player_chest"),
            (try_end),
        ]),
        
        
        # script_remove_siege_objects
        # Input: none
        # Output: none
        ("remove_siege_objects",
          [
            (replace_scene_props, "spr_battlement_a_destroyed", "spr_battlement_a"),
            (replace_scene_props, "spr_snowy_castle_battlement_a_destroyed", "spr_snowy_castle_battlement_a"),
            (replace_scene_props, "spr_castle_e_battlement_a_destroyed", "spr_castle_e_battlement_a"),
            (replace_scene_props, "spr_castle_battlement_a_destroyed", "spr_castle_battlement_a"),
            (replace_scene_props, "spr_castle_battlement_b_destroyed", "spr_castle_battlement_b"),
            (replace_scene_props, "spr_earth_wall_a2", "spr_earth_wall_a"),
            (replace_scene_props, "spr_earth_wall_b2", "spr_earth_wall_b"),
            (replace_scene_props, "spr_belfry_platform_b", "spr_empty"),
            (replace_scene_props, "spr_belfry_platform_a", "spr_empty"),
            (replace_scene_props, "spr_belfry_a", "spr_empty"),
            (replace_scene_props, "spr_belfry_wheel", "spr_empty"),
            (replace_scene_props, "spr_siege_ladder_move_6m", "spr_empty"),
            (replace_scene_props, "spr_siege_ladder_move_8m", "spr_empty"),
            (replace_scene_props, "spr_siege_ladder_move_10m", "spr_empty"),
            (replace_scene_props, "spr_siege_ladder_move_12m", "spr_empty"),
            (replace_scene_props, "spr_siege_ladder_move_14m", "spr_empty"),
            (replace_scene_props, "spr_siege_ladder_12m", "spr_empty"),
            (replace_scene_props, "spr_siege_ladder_14m", "spr_empty"),
            (replace_scene_props, "spr_mangonel", "spr_empty"),
            (replace_scene_props, "spr_trebuchet_old", "spr_empty"),
            (replace_scene_props, "spr_trebuchet_new", "spr_empty"),
            (replace_scene_props, "spr_stone_ball", "spr_empty"),
            (replace_scene_props, "spr_Village_fire_big", "spr_empty"),
        ]),
        
        # script_describe_relation_to_s63
        # Input: arg1 = relation (-100 .. 100)
        # Output: none
        ("describe_relation_to_s63",
          [(store_script_param_1, ":relation"),
            (store_add, ":normalized_relation", ":relation", 100),
            (val_add, ":normalized_relation", 5),
            (store_div, ":str_offset", ":normalized_relation", 10),
            (val_clamp, ":str_offset", 0, 20),
            (store_add, ":str_id", "str_relation_mnus_100",  ":str_offset"),
            (str_store_string, s63, ":str_id"),
        ]),
        
        # script_describe_center_relation_to_s3
        # Input: arg1 = relation (-100 .. 100)
        # Output: none
        ("describe_center_relation_to_s3",
          [(store_script_param_1, ":relation"),
            (store_add, ":normalized_relation", ":relation", 100),
            (val_add, ":normalized_relation", 5),
            (store_div, ":str_offset", ":normalized_relation", 10),
            (val_clamp, ":str_offset", 0, 20),
            (store_add, ":str_id", "str_center_relation_mnus_100",  ":str_offset"),
            (str_store_string, s3, ":str_id"),
        ]),
        
        
        # script_center_ambiance_sounds
        # Input: none
        # Output: none
        # to be called every two seconds
        ("center_ambiance_sounds",
          [
            (assign, ":sound_1", -1),
            (assign, ":sound_2", -1),
            (assign, ":sound_3", -1),
            (assign, ":sound_4", -1),
            (assign, ":sound_5", -1),
            (try_begin),
              (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
              (try_begin),
                (neg|is_currently_night),
                (assign, ":sound_3", "snd_distant_dog_bark"),
                (assign, ":sound_3", "snd_distant_chicken"),
              (else_try),
                (assign, ":sound_1", "snd_distant_dog_bark"),
                (assign, ":sound_2", "snd_distant_owl"),
              (try_end),
            (else_try),
              (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
              (try_begin),
                (neg|is_currently_night),
                (assign, ":sound_1", "snd_distant_carpenter"),
                (assign, ":sound_2", "snd_distant_blacksmith"),
                (assign, ":sound_3", "snd_distant_dog_bark"),
              (else_try),
                (assign, ":sound_1", "snd_distant_dog_bark"),
              (try_end),
            (try_end),
            (try_begin),
              (store_random_in_range, ":r", 0, 7),
              (try_begin),
                (eq, ":r", 1),
                (ge, ":sound_1", 0),
                (play_sound, ":sound_1"),
              (else_try),
                (eq, ":r", 2),
                (ge, ":sound_2", 0),
                (play_sound, ":sound_2"),
              (else_try),
                (eq, ":r", 3),
                (ge, ":sound_3", 0),
                (play_sound, ":sound_3"),
              (else_try),
                (eq, ":r", 4),
                (ge, ":sound_4", 0),
                (play_sound, ":sound_4"),
              (else_try),
                (eq, ":r", 5),
                (ge, ":sound_5", 0),
                (play_sound, ":sound_5"),
              (try_end),
            (try_end),
        ]),
        
        # script_center_set_walker_to_type
        # Input: arg1 = center_no, arg2 = walker_no, arg3 = walker_type,
        # Output: none
        ("center_set_walker_to_type",
          [
            (store_script_param, ":center_no", 1),
            (store_script_param, ":walker_no", 2),
            (store_script_param, ":walker_type", 3),
            (store_add, ":type_slot", slot_center_walker_0_type, ":walker_no"),
            (party_set_slot, ":center_no", ":type_slot", ":walker_type"),
            (party_get_slot, ":center_faction", ":center_no", slot_center_original_faction),
            (faction_get_slot, ":center_culture", ":center_faction", slot_faction_culture),
            (store_random_in_range, ":walker_troop_slot", 0, 2),
            (try_begin),
              (party_slot_eq, ":center_no", slot_party_type, spt_village),
              (val_add, ":walker_troop_slot", slot_faction_village_walker_male_troop),
            (else_try),
              (val_add, ":walker_troop_slot", slot_faction_town_walker_male_troop),
            (try_end),
            (try_begin),
              (eq,":walker_type", walkert_spy),
              (assign,":original_walker_slot",":walker_troop_slot"),
              (val_add,":walker_troop_slot",4), # select spy troop id slot
            (try_end),
            (faction_get_slot, ":walker_troop_id", ":center_culture", ":walker_troop_slot"),
            (try_begin),
              (eq,":walker_type", walkert_spy),
              (faction_get_slot, ":original_walker", ":center_culture", ":original_walker_slot"),
              # restore spy inventory
              (try_for_range,":item_no","itm_horse_meat","itm_items_end"),
                (store_item_kind_count,":num_items",":item_no",":original_walker"),
                (ge,":num_items",1),
                (store_item_kind_count,":num_items",":item_no",":walker_troop_id"),
                (lt,":num_items",1),
                (troop_add_items,":walker_troop_id",":item_no",1),
              (try_end),
              # determine spy recognition item
              (store_random_in_range,":spy_item_type",itp_type_head_armor,itp_type_hand_armor),
              (assign,":num",0),
              (try_for_range,":item_no","itm_horse_meat","itm_items_end"),
                (store_item_kind_count,":num_items",":item_no",":walker_troop_id"),
                (ge,":num_items",1),
                (item_get_type, ":itp", ":item_no"),
                (eq,":itp",":spy_item_type"),
                (val_add,":num",1),
                (troop_remove_items,":walker_troop_id",":item_no",":num_items"),
              (try_end),
              (store_random_in_range,":random_item",0,":num"),
              (assign,":num",-1),
              (try_for_range,":item_no","itm_horse_meat","itm_items_end"),
                (store_item_kind_count,":num_items",":item_no",":original_walker"),
                (ge,":num_items",1),
                (item_get_type, ":itp", ":item_no"),
                (eq,":itp",":spy_item_type"),
                (val_add,":num",1),
                (eq,":num",":random_item"),
                (troop_add_items,":walker_troop_id",":item_no",1),
                (assign,":spy_item",":item_no"),
              (try_end),
              (assign,"$spy_item_worn",":spy_item"),
              (assign,"$spy_quest_troop",":walker_troop_id"),
              (troop_equip_items,":walker_troop_id"),
            (try_end),
            (store_add, ":troop_slot", slot_center_walker_0_troop, ":walker_no"),
            (party_set_slot, ":center_no", ":troop_slot", ":walker_troop_id"),
            (store_random_in_range, ":walker_dna", 0, 1000000),
            (store_add, ":dna_slot", slot_center_walker_0_dna, ":walker_no"),
            (party_set_slot, ":center_no", ":dna_slot", ":walker_dna"),
        ]),
        
        
        # script_cf_center_get_free_walker
        # Input: arg1 = center_no
        # Output: reg0 = walker no (can fail)
        ("cf_center_get_free_walker",
          [
            (store_script_param, ":center_no", 1),
            (assign, ":num_free_walkers", 0),
            (try_for_range, ":walker_no", 0, num_town_walkers),
              (store_add, ":type_slot", slot_center_walker_0_type, ":walker_no"),
              (party_slot_eq, ":center_no", ":type_slot", walkert_default),
              (val_add, ":num_free_walkers", 1),
            (try_end),
            (gt, ":num_free_walkers", 0),
            (assign, reg0, -1),
            (store_random_in_range, ":random_rank", 0, ":num_free_walkers"),
            (try_for_range, ":walker_no", 0, num_town_walkers),
              (store_add, ":type_slot", slot_center_walker_0_type, ":walker_no"),
              (party_slot_eq, ":center_no", ":type_slot", walkert_default),
              (val_sub, ":num_free_walkers", 1),
              (eq, ":num_free_walkers", ":random_rank"),
              (assign, reg0, ":walker_no"),
            (try_end),
        ]),
        
        # script_center_remove_walker_type_from_walkers
        # Input: arg1 = center_no, arg2 = walker_type,
        # Output: reg0 = 1 if comment found, 0 otherwise; s61 will contain comment string if found
        ("center_remove_walker_type_from_walkers",
          [
            (store_script_param, ":center_no", 1),
            (store_script_param, ":walker_type", 2),
            (try_for_range, ":walker_no", 0, num_town_walkers),
              (store_add, ":type_slot", slot_center_walker_0_type, ":walker_no"),
              (party_slot_eq, ":center_no", ":type_slot", ":walker_type"),
              (call_script, "script_center_set_walker_to_type", ":center_no", ":walker_no", walkert_default),
            (try_end),
        ]),
        
        
        # script_init_town_walkers
        # Input: none
        # Output: none
        ("init_town_walkers",
          [
            (try_begin),
              (eq, "$town_nighttime", 0),
              (try_for_range, ":walker_no", 0, num_town_walkers),
                (store_add, ":troop_slot", slot_center_walker_0_troop, ":walker_no"),
                (party_get_slot, ":walker_troop_id", "$current_town", ":troop_slot"),
                (gt, ":walker_troop_id", 0),
                (store_add, ":entry_no", town_walker_entries_start, ":walker_no"),
                (set_visitor, ":entry_no", ":walker_troop_id"),
              (try_end),
            (try_end),
        ]),
        
        
        # script_cf_enter_center_location_bandit_check
        # Input: none
        # Output: none
        ("cf_enter_center_location_bandit_check",
          [
            (neq, "$town_nighttime", 0),
            (party_slot_ge, "$current_town", slot_center_has_bandits, 1),
            (eq, "$g_defending_against_siege", 0),#Skip if the center is under siege (because of resting)
            (eq, "$sneaked_into_town", 0),#Skip if sneaked
            (try_begin),
              (party_slot_eq, "$current_town", slot_party_type, spt_village),
              (party_get_slot, ":cur_scene", "$current_town", slot_castle_exterior),
            (else_try),
              (party_get_slot, ":cur_scene", "$current_town", slot_town_center),
            (try_end),
            (modify_visitors_at_site, ":cur_scene"),
            (reset_visitors),
            (party_get_slot, ":bandit_troop", "$current_town", slot_center_has_bandits),
            (store_character_level, ":level", "trp_player"),
            
            (set_jump_mission, "mt_bandits_at_night"),
            (try_begin),
              (party_slot_eq, "$current_town", slot_party_type, spt_village),
              (assign, ":spawn_amount", 2),
              (store_div, ":level_fac",  ":level", 10),
              (val_add, ":spawn_amount", ":level_fac"),
              (try_for_range, ":unused", 0, 3),
                (gt, ":level", 10),
                (store_random_in_range, ":random_no", 0, 100),
                (lt, ":random_no", ":level"),
                (val_add, ":spawn_amount", 1),
              (try_end),
              (set_visitors, 4, ":bandit_troop", ":spawn_amount"),
              (assign, "$num_center_bandits", ":spawn_amount"),
              (set_jump_entry, 2),
            (else_try),
              (assign, ":spawn_amount", 1),
              (assign, "$num_center_bandits", 0),
              (try_begin),
                (gt, ":level", 15),
                (store_random_in_range, ":random_no", 0, 100),
                (lt, ":random_no", ":level"),
                (assign, ":spawn_amount", 2),
              (try_end),
              (val_add, "$num_center_bandits",  ":spawn_amount"),
              (set_visitors, 11, ":bandit_troop", ":spawn_amount"),
              (assign, ":spawn_amount", 1),
              (try_begin),
                (gt, ":level", 20),
                (store_random_in_range, ":random_no", 0, 100),
                (lt, ":random_no", ":level"),
                (assign, ":spawn_amount", 2),
              (try_end),
              (set_visitors, 27, ":bandit_troop", ":spawn_amount"),
              (val_add, "$num_center_bandits",  ":spawn_amount"),
              (try_begin),
                (gt, ":level", 9),
                (assign, ":spawn_amount", 1),
                (try_begin),
                  (gt, ":level", 25),
                  (store_random_in_range, ":random_no", 0, 100),
                  (lt, ":random_no", ":level"),
                  (assign, ":spawn_amount", 2),
                (try_end),
                (set_visitors, 28, ":bandit_troop", ":spawn_amount"),
                (val_add, "$num_center_bandits",  ":spawn_amount"),
              (try_end),
              (assign, "$town_entered", 1),
              (assign, "$all_doors_locked", 1),
            (try_end),
            
            (display_message, "@You have run into a trap!", 0xFFFF2222),
            (display_message, "@You are attacked by a group of bandits!", 0xFFFF2222),
            
            (jump_to_scene, ":cur_scene"),
            (change_screen_mission),
        ]),
        
        # script_init_town_agent
        # Input: none
        # Output: none
        ("init_town_agent",
          [
            (store_script_param, ":agent_no", 1),
            (agent_get_troop_id, ":troop_no", ":agent_no"),
            (set_fixed_point_multiplier, 100),
            (assign, ":stand_animation", -1),
            (try_begin),
              (this_or_next|is_between, ":troop_no", armor_merchants_begin, armor_merchants_end),
              (is_between, ":troop_no", weapon_merchants_begin, weapon_merchants_end),
              (try_begin),
                (troop_get_type, ":cur_troop_gender", ":troop_no"),
                (eq, ":cur_troop_gender", 0),
                (agent_set_animation, ":agent_no", "anim_stand_townguard"),
              (else_try),
                (agent_set_animation, ":agent_no", "anim_stand_townguard"),
              (end_try),
            (else_try),
              (is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
              (assign, ":stand_animation", "anim_stand_lady"),
            (else_try),
              (is_between, ":troop_no", active_npcs_begin, active_npcs_end),
              (assign, ":stand_animation", "anim_stand_lord"),
            (else_try),
              (is_between, ":troop_no", soldiers_begin, soldiers_end),
              (assign, ":stand_animation", "anim_stand_townguard"),
            (try_end),
            (try_begin),
              (ge, ":stand_animation", 0),
              (agent_set_stand_animation, ":agent_no", ":stand_animation"),
              (agent_set_animation, ":agent_no", ":stand_animation"),
              (store_random_in_range, ":random_no", 0, 100),
              (agent_set_animation_progress, ":agent_no", ":random_no"),
            (try_end),
        ]),
        
        # script_init_town_walker_agents
        # Input: none
        # Output: none
        ("init_town_walker_agents",
          [(assign, ":num_walkers", 0),
            (try_for_agents, ":cur_agent"),
              (agent_get_troop_id, ":cur_troop", ":cur_agent"),
              (is_between, ":cur_troop", walkers_begin, walkers_end),
              (val_add, ":num_walkers", 1),
              (agent_get_position, pos1, ":cur_agent"),
              (try_for_range, ":i_e_p", 9, 40),#Entry points
                (entry_point_get_position, pos2, ":i_e_p"),
                (get_distance_between_positions, ":distance", pos1, pos2),
                (lt, ":distance", 200),
                (agent_set_slot, ":cur_agent", 0, ":i_e_p"),
              (try_end),
              (call_script, "script_set_town_walker_destination", ":cur_agent"),
            (try_end),
        ]),
        
        # script_agent_get_town_walker_details
        # This script assumes this is one of town walkers.
        # Input: agent_id
        # Output: reg0: town_walker_type, reg1: town_walker_dna
        ("agent_get_town_walker_details",
          [(store_script_param, ":agent_no", 1),
            (agent_get_entry_no, ":entry_no", ":agent_no"),
            (store_sub, ":walker_no", ":entry_no", town_walker_entries_start),
            
            (store_add, ":type_slot", slot_center_walker_0_type, ":walker_no"),
            (party_get_slot, ":walker_type", "$current_town", ":type_slot"),
            (store_add, ":dna_slot", slot_center_walker_0_dna,  ":walker_no"),
            (party_get_slot, ":walker_dna", "$current_town", ":dna_slot"),
            (assign, reg0, ":walker_type"),
            (assign, reg1, ":walker_dna"),
            (assign, reg2, ":walker_no"),
        ]),
        
        
		  ##diplomacy start+
		  ##WARNING: this will also clobber s0 now
		  ##diplomacy end+
		  ("town_walker_occupation_string_to_s14",
			[
			(store_script_param, ":agent_no", 1),

			#Cairo, approx 1799:
			#adult males = 114,000
			#military, 10,400
			#civil, including religious 5,000
			#commerce 3,500
			#merchants 4,500
			#coffee shops, 1,500 (maybe broaden to inns and taverns)
			#artisans 21,800
			#workmen 4,300
			#itinerants 8,600
			#servants (inc water carriers) 26,400
			(assign, ":check_for_good_price", 0),
			##diplomacy start+ escalate "sir/madame" to "my lord/lady" or "your highness" if appropriate
			(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
			##diplomacy end+
            (str_store_string, s14, "str_i_take_what_work_i_can_sirmadame_i_carry_water_or_help_the_merchants_with_their_loads_or_help_build_things_if_theres_things_to_be_built"),
            
            (call_script, "script_agent_get_town_walker_details", ":agent_no"),
            (assign, ":type", reg0),
            (assign, ":walker_dna", reg1),
            
            (assign, ":item", -1),
            (assign, ":total_item_production", 0),
            (try_for_range, ":trade_good", trade_goods_begin, trade_goods_end),
              (call_script, "script_center_get_production", "$g_encountered_party", ":trade_good"),
              (val_add, ":total_item_production", reg0),
            (try_end),
            
            (val_max, ":total_item_production", 1),
            
            (store_mod, ":semi_random_number", ":walker_dna", ":total_item_production"),
            
            
            (try_begin),
              (eq, "$cheat_mode", 1),
              (assign, reg4, ":walker_dna"),
              (assign, reg5, ":total_item_production"),
              (assign, reg7, ":semi_random_number"),
              (display_message, "str_dna_reg4_total_production_reg5_modula_reg7"),
            (try_end),
            
            (try_for_range, ":trade_good", trade_goods_begin, trade_goods_end),
              (gt, ":semi_random_number", -1),
              (call_script, "script_center_get_production", "$g_encountered_party", ":trade_good"),
              (val_sub, ":semi_random_number", reg0),
              (lt, ":semi_random_number", 0),
              (try_begin),
                (eq, "$cheat_mode", 1),
                (str_store_item_name, s9, ":trade_good"),
                (display_message, "str_agent_produces_s9"),
              (try_end),
              (assign, ":item", ":trade_good"),
            (try_end),
            
            
            (try_begin),
              (eq, ":type", walkert_needs_money),
              (is_between, "$g_encountered_party", towns_begin, towns_end),
              (str_store_string, s14, "str_im_not_doing_anything_sirmadame_theres_no_work_to_be_had_around_here_these_days"),
            (else_try),
              (eq, ":type", walkert_needs_money),
              (str_store_string, s14, "str_im_not_doing_anything_sirmadame_i_have_no_land_of_my_own_and_theres_no_work_to_be_had_around_here_these_days"),
            (else_try),
              (eq, ":type", walkert_needs_money_helped),
              (str_store_string, s14, "str_why_im_still_living_off_of_your_kindness_and_goodness_sirmadame_hopefully_there_will_be_work_shortly"),
            (else_try),
              (eq, ":item", "itm_trade_grain"),
              (is_between, "$g_encountered_party", towns_begin, towns_end),
              (str_store_string, s14, "str_i_work_in_the_fields_just_outside_the_walls_where_they_grow_grain_we_dont_quite_grow_enough_to_meet_our_needs_though_and_have_to_import_grain_from_the_surrounding_countryside"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_grain"),
              (str_store_string, s14, "str_i_work_mostly_in_the_fields_growing_grain_in_the_town_they_grind_it_to_make_bread_or_ale_and_we_can_also_boil_it_as_a_porridge"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_ale"),
              (str_store_string, s14, "str_i_work_in_the_breweries_making_ale_the_poor_folk_drink_a_lot_of_it_as_its_cheaper_than_wine_we_make_it_with_grain_brought_in_from_the_countryside"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_bread"),
              (str_store_string, s14, "str_i_work_in_a_mill_grinding_flour_to_make_bread_bread_is_cheap_keeps_well_and_fills_the_stomach"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_dried_meat"),
              (str_store_string, s14, "str_i_tend_cattle_we_dry_and_salt_meat_to_preserve_it_and_make_cheese_from_the_milk"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_cheese"),
              (str_store_string, s14, "str_i_tend_cattle_we_dry_and_salt_meat_to_preserve_it_and_make_cheese_from_the_milk_so_it_doesnt_spoil"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_butter"),
              (str_store_string, s14, "str_i_tend_cattle_we_dry_and_salt_meat_to_preserve_it_and_make_cheese_from_the_milk_so_it_doesnt_spoil"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_wool"),
              (str_store_string, s14, "str_i_tend_sheep_we_send_the_wool_to_the_cities_to_be_woven_into_cloth_and_make_mutton_sausage_when_we_cull_the_herds"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_sausages"),
              (str_store_string, s14, "str_i_tend_sheep_we_send_the_wool_to_the_cities_to_be_woven_into_cloth_and_make_mutton_sausage_when_we_cull_the_herds"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_wool_cloth"),
              (str_store_string, s14, "str_i_work_at_a_loom_spinning_cloth_from_wool_wool_is_some_of_the_cheapest_cloth_you_can_buy_but_it_will_still_keep_you_warm"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_smoked_fish"),
              (str_store_string, s14, "str_i_crew_a_fishing_boat_we_salt_and_smoke_the_flesh_to_sell_it_far_inland"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_salt"),
              (str_store_string, s14, "str_i_sift_salt_from_a_nearby_flat_they_need_salt_everywhere_to_preserve_meat_and_fish"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_iron"),
              (str_store_string, s14, "str_i_mine_iron_from_a_vein_in_a_nearby_cliffside_they_use_it_to_make_tools_arms_and_other_goods"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_pottery"),
              (str_store_string, s14, "str_i_make_pottery_which_people_use_to_store_grain_and_carry_water"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_tools"),
              (str_store_string, s14, "str_trade_explanation_tools"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_oil"),
              (str_store_string, s14, "str_trade_explanation_oil"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_linen"),
              (str_store_string, s14, "str_trade_explanation_linen"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_velvet"),
              (str_store_string, s14, "str_trade_explanation_velvet"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_spice"),
              (str_store_string, s14, "str_trade_explanation_spice"),
              (assign, ":check_for_good_price", 1),
              
            (else_try),
              (eq, ":item", "itm_trade_apples"),
              (str_store_string, s14, "str_trade_explanation_apples"),
              (assign, ":check_for_good_price", 1),
              
            (try_end),
            
            
            (try_begin),
              (eq, ":check_for_good_price", 1),
              
              (assign, ":trade_destination", -1),
              (store_skill_level, ":trade_skill", "skl_trade", "trp_player"),
              
              (try_begin),
                (is_between, "$g_encountered_party", villages_begin, villages_end),
                (party_get_slot, ":trade_town", "$g_encountered_party", slot_village_market_town),
              (else_try),
                (assign, ":trade_town", "$g_encountered_party"),
              (try_end),
              
              (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
              (store_add, ":cur_good_price_slot", ":item", ":item_to_price_slot"),
              (party_get_slot, ":score_to_beat", ":trade_town", ":cur_good_price_slot"),
              (val_add, ":score_to_beat", 400),
              (store_mul, ":deduction_for_trade_skill", ":trade_skill", 35),
              (try_begin),
                (is_between, "$g_encountered_party", villages_begin, villages_end),
                (val_add, ":score_to_beat", 200),
              (try_end),
              (val_sub, ":score_to_beat", ":deduction_for_trade_skill"),
              
              (try_for_range, ":trade_route_slot", slot_town_trade_routes_begin, slot_town_trade_routes_end),
                (party_get_slot, ":other_town", ":trade_town", ":trade_route_slot"),
                (party_get_slot, ":price_in_other_town", ":other_town", ":cur_good_price_slot"),
                
                
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (assign, reg4, ":price_in_other_town"),
                  (assign, reg5, ":score_to_beat"),
                  (str_store_party_name, s10, ":other_town"),
                  (display_message, "str_s10_has_reg4_needs_reg5"),
                (try_end),
                
                (gt, ":price_in_other_town", ":score_to_beat"),
                
                (assign, ":trade_destination", ":other_town"),
                (assign, ":score_to_beat", ":price_in_other_town"),
              (try_end),
              
              (is_between, ":trade_destination", centers_begin, centers_end),
              
              (str_store_party_name, s15, ":trade_destination"),
              (str_store_string, s14, "str_s14_i_hear_that_you_can_find_a_good_price_for_it_in_s15"),
              
              #Reasons -- raw material
              #Reason -- road cut
              #Reason -- villages looted
              
            (try_end),
            
            
        ]),
        
        
        
        
        
        
        
        # script_tick_town_walkers
        # Input: none
        # Output: none
        ("tick_town_walkers",
          [(try_for_agents, ":cur_agent"),
              (agent_get_troop_id, ":cur_troop", ":cur_agent"),
              (is_between, ":cur_troop", walkers_begin, walkers_end),
              (agent_get_slot, ":target_entry_point", ":cur_agent", 0),
              (entry_point_get_position, pos1, ":target_entry_point"),
              (try_begin),
                (lt, ":target_entry_point", 32),
                (init_position, pos2),
                (position_set_y, pos2, 250),
                (position_transform_position_to_parent, pos1, pos1, pos2),
              (try_end),
              (agent_get_position, pos2, ":cur_agent"),
              (get_distance_between_positions, ":distance", pos1, pos2),
              (lt, ":distance", 400),
              (assign, ":random_no", 0),
              (try_begin),
                (lt, ":target_entry_point", 32),
                (store_random_in_range, ":random_no", 0, 100),
              (try_end),
              (lt, ":random_no", 20),
              (call_script, "script_set_town_walker_destination", ":cur_agent"),
            (try_end),
        ]),
        
        
        # script_set_town_walker_destination
        # Input: arg1 = agent_no
        # Output: none
        ("set_town_walker_destination",
          [(store_script_param_1, ":agent_no"),
            (assign, reg0, 9),
            (assign, reg1, 10),
            (assign, reg2, 12),
            (assign, reg3, 32),
            (assign, reg4, 33),
            (assign, reg5, 34),
            (assign, reg6, 35),
            (assign, reg7, 36),
            (assign, reg8, 37),
            (assign, reg9, 38),
            (assign, reg10, 39),
            (try_for_agents, ":cur_agent"),
              (agent_get_troop_id, ":cur_troop", ":cur_agent"),
              (is_between, ":cur_troop", walkers_begin, walkers_end),
              (agent_get_slot, ":target_entry_point", ":cur_agent", 0),
              (try_begin),
                (eq, ":target_entry_point", 9),
                (assign, reg0, 0),
              (else_try),
                (eq, ":target_entry_point", 10),
                (assign, reg1, 0),
              (else_try),
                (eq, ":target_entry_point", 12),
                (assign, reg2, 0),
              (else_try),
                (eq, ":target_entry_point", 32),
                (assign, reg3, 0),
              (else_try),
                (eq, ":target_entry_point", 33),
                (assign, reg4, 0),
              (else_try),
                (eq, ":target_entry_point", 34),
                (assign, reg5, 0),
              (else_try),
                (eq, ":target_entry_point", 35),
                (assign, reg6, 0),
              (else_try),
                (eq, ":target_entry_point", 36),
                (assign, reg7, 0),
              (else_try),
                (eq, ":target_entry_point", 37),
                (assign, reg8, 0),
              (else_try),
                (eq, ":target_entry_point", 38),
                (assign, reg9, 0),
              (else_try),
                (eq, ":target_entry_point", 39),
                (assign, reg10, 0),
              (try_end),
            (try_end),
            (assign, ":try_limit", 100),
            (assign, ":target_entry_point", 0),
            (try_for_range, ":unused", 0, ":try_limit"),
              (shuffle_range, 0, 11),
              (gt, reg0, 0),
              (assign, ":target_entry_point", reg0),
              (assign, ":try_limit", 0),
            (try_end),
            (try_begin),
              (gt, ":target_entry_point", 0),
              (agent_set_slot, ":agent_no", 0, ":target_entry_point"),
              (entry_point_get_position, pos1, ":target_entry_point"),
              (try_begin),
                (lt, ":target_entry_point", 32),
                (init_position, pos2),
                (position_set_y, pos2, 250),
                (position_transform_position_to_parent, pos1, pos1, pos2),
              (try_end),
              (agent_set_scripted_destination, ":agent_no", pos1, 0),
              (agent_set_speed_limit, ":agent_no", 5),
            (try_end),
        ]),
        
        # script_town_init_doors
        # Input: door_state (-1 = closed, 1 = open, 0 = use $town_nighttime)
        # Output: none (required for siege mission templates)
        ("town_init_doors",
          [(store_script_param, ":door_state", 1),
            (try_begin),
              (assign, ":continue", 0),
              (try_begin),
                (eq, ":door_state", 1),
                (assign, ":continue", 1),
              (else_try),
                (eq, ":door_state", 0),
                (eq, "$town_nighttime", 0),
                (assign, ":continue", 1),
              (try_end),
              (eq, ":continue", 1),# open doors
              (assign, ":end_cond", 1),
              (try_for_range, ":i_instance", 0, ":end_cond"),
                (scene_prop_get_instance, ":object", "spr_towngate_door_left", ":i_instance"),
                (ge, ":object", 0),
                (val_add, ":end_cond", 1),
                (prop_instance_get_position, pos1, ":object"),
                (position_rotate_z, pos1, -100),
                (prop_instance_animate_to_position, ":object", pos1, 1),
              (try_end),
              (assign, ":end_cond", 1),
              (try_for_range, ":i_instance", 0, ":end_cond"),
                (scene_prop_get_instance, ":object", "spr_towngate_rectangle_door_left", ":i_instance"),
                (ge, ":object", 0),
                (val_add, ":end_cond", 1),
                (prop_instance_get_position, pos1, ":object"),
                (position_rotate_z, pos1, -80),
                (prop_instance_animate_to_position, ":object", pos1, 1),
              (try_end),
              (assign, ":end_cond", 1),
              (try_for_range, ":i_instance", 0, ":end_cond"),
                (scene_prop_get_instance, ":object", "spr_towngate_door_right", ":i_instance"),
                (ge, ":object", 0),
                (val_add, ":end_cond", 1),
                (prop_instance_get_position, pos1, ":object"),
                (position_rotate_z, pos1, 100),
                (prop_instance_animate_to_position, ":object", pos1, 1),
              (try_end),
              (assign, ":end_cond", 1),
              (try_for_range, ":i_instance", 0, ":end_cond"),
                (scene_prop_get_instance, ":object", "spr_towngate_rectangle_door_right", ":i_instance"),
                (ge, ":object", 0),
                (val_add, ":end_cond", 1),
                (prop_instance_get_position, pos1, ":object"),
                (position_rotate_z, pos1, 80),
                (prop_instance_animate_to_position, ":object", pos1, 1),
              (try_end),
            (try_end),
        ]),
        
        # script_siege_init_ai_and_belfry
        # Input: none
        # Output: none (required for siege mission templates)
        ("siege_init_ai_and_belfry",
          [(assign, "$cur_belfry_pos", 50),
            (assign, ":cur_belfry_object_pos", slot_scene_belfry_props_begin),
            (store_current_scene, ":cur_scene"),
            #Collecting belfry objects
            (try_for_range, ":i_belfry_instance", 0, 3),
              (scene_prop_get_instance, ":belfry_object", "spr_belfry_a", ":i_belfry_instance"),
              (ge, ":belfry_object", 0),
              (scene_set_slot, ":cur_scene", ":cur_belfry_object_pos", ":belfry_object"),
              (val_add, ":cur_belfry_object_pos", 1),
            (try_end),
            (try_for_range, ":i_belfry_instance", 0, 3),
              (scene_prop_get_instance, ":belfry_object", "spr_belfry_platform_a", ":i_belfry_instance"),
              (ge, ":belfry_object", 0),
              (scene_set_slot, ":cur_scene", ":cur_belfry_object_pos", ":belfry_object"),
              (val_add, ":cur_belfry_object_pos", 1),
            (try_end),
            (try_for_range, ":i_belfry_instance", 0, 3),
              (scene_prop_get_instance, ":belfry_object", "spr_belfry_platform_b", ":i_belfry_instance"),
              (ge, ":belfry_object", 0),
              (scene_set_slot, ":cur_scene", ":cur_belfry_object_pos", ":belfry_object"),
              (val_add, ":cur_belfry_object_pos", 1),
            (try_end),
            (assign, "$belfry_rotating_objects_begin", ":cur_belfry_object_pos"),
            (try_for_range, ":i_belfry_instance", 0, 5),
              (scene_prop_get_instance, ":belfry_object", "spr_belfry_wheel", ":i_belfry_instance"),
              (ge, ":belfry_object", 0),
              (scene_set_slot, ":cur_scene", ":cur_belfry_object_pos", ":belfry_object"),
              (val_add, ":cur_belfry_object_pos", 1),
            (try_end),
            (assign, "$last_belfry_object_pos", ":cur_belfry_object_pos"),
            
            #Lifting up the platform  at the beginning
            (try_begin),
              (scene_prop_get_instance, ":belfry_object_to_rotate", "spr_belfry_platform_a", 0),
            (try_end),
            
            #Moving the belfry objects to their starting position
            (entry_point_get_position,pos1,55),
            (entry_point_get_position,pos3,50),
            (try_for_range, ":i_belfry_object_pos", slot_scene_belfry_props_begin, "$last_belfry_object_pos"),
              (assign, ":pos_no", pos_belfry_begin),
              (val_add, ":pos_no", ":i_belfry_object_pos"),
              (val_sub, ":pos_no", slot_scene_belfry_props_begin),
              (scene_get_slot, ":cur_belfry_object", ":cur_scene", ":i_belfry_object_pos"),
              (prop_instance_get_position, pos2, ":cur_belfry_object"),
              (try_begin),
                (eq, ":cur_belfry_object", ":belfry_object_to_rotate"),
                (position_rotate_x, pos2, 90),
              (try_end),
              (position_transform_position_to_local, ":pos_no", pos1, pos2),
              (position_transform_position_to_parent, pos4, pos3, ":pos_no"),
              (prop_instance_animate_to_position, ":cur_belfry_object", pos4, 1),
            (try_end),
            (assign, "$belfry_positioned", 0),
            (assign, "$belfry_num_slots_positioned", 0),
            (assign, "$belfry_num_men_pushing", 0),
            
            (set_show_messages, 0),
            (team_give_order, "$attacker_team", grc_everyone, mordr_stand_ground),
            (team_give_order, "$attacker_team_2", grc_everyone, mordr_stand_ground),
            (set_show_messages, 1),
        ]),
        
        # script_cf_siege_move_belfry
        # Input: none
        # Output: none (required for siege mission templates)
        ("cf_siege_move_belfry",
          [(neq, "$last_belfry_object_pos", slot_scene_belfry_props_begin),
            (entry_point_get_position,pos1,50),
            (entry_point_get_position,pos4,55),
            (get_distance_between_positions, ":total_distance", pos4, pos1),
            (store_current_scene, ":cur_scene"),
            (scene_get_slot, ":first_belfry_object", ":cur_scene", slot_scene_belfry_props_begin),
            (prop_instance_get_position, pos2, ":first_belfry_object"),
            (entry_point_get_position,pos1,"$cur_belfry_pos"),
            (position_transform_position_to_parent, pos3, pos1, pos_belfry_begin),
            (position_transform_position_to_parent, pos5, pos4, pos_belfry_begin),
            (get_distance_between_positions, ":cur_distance", pos2, pos3),
            (get_distance_between_positions, ":distance_left", pos2, pos5),
            (try_begin),
              (le, ":cur_distance", 10),
              (val_add, "$cur_belfry_pos", 1),
              (entry_point_get_position,pos1,"$cur_belfry_pos"),
              (position_transform_position_to_parent, pos3, pos1, pos_belfry_begin),
              (get_distance_between_positions, ":cur_distance", pos2, pos3),
            (try_end),
            (neq, "$cur_belfry_pos", 50),
            
            (assign, ":base_speed", 20),
            (store_div, ":slow_range", ":total_distance", 60),
            (store_sub, ":distance_moved", ":total_distance", ":distance_left"),
            
            (try_begin),
              (lt, ":distance_moved", ":slow_range"),
              (store_mul, ":base_speed", ":distance_moved", -60),
              (val_div, ":base_speed", ":slow_range"),
              (val_add, ":base_speed", 80),
            (else_try),
              (lt, ":distance_left", ":slow_range"),
              (store_mul, ":base_speed", ":distance_left", -60),
              (val_div, ":base_speed", ":slow_range"),
              (val_add, ":base_speed", 80),
            (try_end),
            (store_mul, ":belfry_speed", ":cur_distance", ":base_speed"),
            (try_begin),
              (eq, "$belfry_num_men_pushing", 0),
              (assign, ":belfry_speed", 1000000),
            (else_try),
              (val_div, ":belfry_speed", "$belfry_num_men_pushing"),
            (try_end),
            
            (try_begin),
              (le, "$cur_belfry_pos", 55),
              (init_position, pos3),
              (position_rotate_x, pos3, ":distance_moved"),
              (scene_get_slot, ":base_belfry_object", ":cur_scene", slot_scene_belfry_props_begin),
              (prop_instance_get_position, pos4, ":base_belfry_object"),
              (entry_point_get_position,pos1,"$cur_belfry_pos"),
              (try_for_range, ":i_belfry_object_pos", slot_scene_belfry_props_begin, "$last_belfry_object_pos"),
                (scene_get_slot, ":cur_belfry_object", ":cur_scene", ":i_belfry_object_pos"),
                (try_begin),
                  (ge, ":i_belfry_object_pos", "$belfry_rotating_objects_begin"),
                  (prop_instance_get_starting_position, pos5, ":base_belfry_object"),
                  (prop_instance_get_starting_position, pos6, ":cur_belfry_object"),
                  (position_transform_position_to_local, pos7, pos5, pos6),
                  (position_transform_position_to_parent, pos5, pos4, pos7),
                  (position_transform_position_to_parent, pos6, pos5, pos3),
                  (prop_instance_set_position, ":cur_belfry_object", pos6),
                (else_try),
                  (assign, ":pos_no", pos_belfry_begin),
                  (val_add, ":pos_no", ":i_belfry_object_pos"),
                  (val_sub, ":pos_no", slot_scene_belfry_props_begin),
                  (position_transform_position_to_parent, pos2, pos1, ":pos_no"),
                  (prop_instance_animate_to_position, ":cur_belfry_object", pos2, ":belfry_speed"),
                (try_end),
              (try_end),
            (try_end),
            (gt, "$cur_belfry_pos", 55),
            (assign, "$belfry_positioned", 1),
        ]),
        
        # script_cf_siege_rotate_belfry_platform
        # Input: none
        # Output: none (required for siege mission templates)
        ("cf_siege_rotate_belfry_platform",
          [(eq, "$belfry_positioned", 1),
            (scene_prop_get_instance, ":belfry_object", "spr_belfry_platform_a", 0),
            (prop_instance_get_position, pos1, ":belfry_object"),
            (position_rotate_x, pos1, -90),
            (prop_instance_animate_to_position, ":belfry_object", pos1, 400),
            (assign, "$belfry_positioned", 2),
        ]),
        
        # script_cf_siege_assign_men_to_belfry
        # Input: none
        # Output: none (required for siege mission templates)
        ("cf_siege_assign_men_to_belfry",
          [
            ##    (store_mission_timer_a, ":cur_seconds"),
            (neq, "$last_belfry_object_pos", slot_scene_belfry_props_begin),
            (assign, ":end_trigger", 0),
            (try_begin),
              (lt, "$belfry_positioned", 3),
              (get_player_agent_no, ":player_agent"),
              (store_current_scene, ":cur_scene"),
              (scene_get_slot, ":first_belfry_object", ":cur_scene", slot_scene_belfry_props_begin),
              (prop_instance_get_position, pos2, ":first_belfry_object"),
              (assign, ":slot_1_positioned", 0),
              (assign, ":slot_2_positioned", 0),
              (assign, ":slot_3_positioned", 0),
              (assign, ":slot_4_positioned", 0),
              (assign, ":slot_5_positioned", 0),
              (assign, ":slot_6_positioned", 0),
              (assign, "$belfry_num_slots_positioned", 0),
              (assign, "$belfry_num_men_pushing", 0),
              (try_for_agents, ":cur_agent"),
                (agent_is_alive, ":cur_agent"),
                (agent_is_human, ":cur_agent"),
                (try_begin),
                  (agent_get_slot, ":x_pos", ":cur_agent", slot_agent_target_x_pos),
                  (neq, ":x_pos", 0),
                  (agent_get_slot, ":y_pos", ":cur_agent", slot_agent_target_y_pos),
                  (try_begin),
                    (eq, ":x_pos", -600),
                    (try_begin),
                      (eq, ":y_pos", 0),
                      (assign, ":slot_1_positioned", 1),
                    (else_try),
                      (eq, ":y_pos", -200),
                      (assign, ":slot_2_positioned", 1),
                    (else_try),
                      (assign, ":slot_3_positioned", 1),
                    (try_end),
                  (else_try),
                    (try_begin),
                      (eq, ":y_pos", 0),
                      (assign, ":slot_4_positioned", 1),
                    (else_try),
                      (eq, ":y_pos", -200),
                      (assign, ":slot_5_positioned", 1),
                    (else_try),
                      (assign, ":slot_6_positioned", 1),
                    (try_end),
                  (try_end),
                  (val_add, "$belfry_num_slots_positioned", 1),
                  (init_position, pos1),
                  (position_move_x, pos1, ":x_pos"),
                  (position_move_y, pos1, ":y_pos"),
                  (init_position, pos3),
                  (position_move_x, pos3, ":x_pos"),
                  (position_move_y, pos3, -1000),
                  (position_transform_position_to_parent, pos4, pos2, pos1),
                  (position_transform_position_to_parent, pos5, pos2, pos3),
                  (agent_get_position, pos6, ":cur_agent"),
                  (get_distance_between_positions, ":target_distance", pos6, pos4),
                  (get_distance_between_positions, ":waypoint_distance", pos6, pos5),
                  (try_begin),
                    (this_or_next|lt, ":target_distance", ":waypoint_distance"),
                    (lt, ":waypoint_distance", 600),
                    (agent_set_scripted_destination, ":cur_agent", pos4, 1),
                  (else_try),
                    (agent_set_scripted_destination, ":cur_agent", pos5, 1),
                  (try_end),
                  (try_begin),
                    (le, ":target_distance", 300),
                    (val_add, "$belfry_num_men_pushing", 1),
                  (try_end),
                  ##        (else_try),
                  ##          (agent_get_team, ":cur_agent_team", ":cur_agent"),
                  ##          (this_or_next|eq, "$attacker_team", ":cur_agent_team"),
                  ##          (             eq, "$attacker_team_2", ":cur_agent_team"),
                  ##          (try_begin),
                  ##            (gt, ":cur_seconds", 20),
                  ##            (agent_get_position, pos1, ":cur_agent"),
                  ##            (agent_set_scripted_destination, ":cur_agent", pos1, 0),
                  ##          (else_try),
                  ##            (try_begin),
                  ##              (team_get_movement_order, ":order1", "$attacker_team", grc_infantry),
                  ##              (team_get_movement_order, ":order2", "$attacker_team", grc_cavalry),
                  ##              (team_get_movement_order, ":order3", "$attacker_team", grc_archers),
                  ##              (this_or_next|neq, ":order1", mordr_stand_ground),
                  ##              (this_or_next|neq, ":order2", mordr_stand_ground),
                  ##              (neq, ":order3", mordr_stand_ground),
                  ##              (set_show_messages, 0),
                  ##              (team_give_order, "$attacker_team", grc_everyone, mordr_stand_ground),
                  ##              (set_show_messages, 1),
                  ##            (try_end),
                  ##          (try_end),
                (try_end),
              (try_end),
              (try_begin),
                (lt, "$belfry_num_slots_positioned", 6),
                (try_for_agents, ":cur_agent"),
                  (agent_is_alive, ":cur_agent"),
                  (agent_get_team, ":cur_agent_team", ":cur_agent"),
                  (this_or_next|eq, "$attacker_team", ":cur_agent_team"),
                  (eq, "$attacker_team_2", ":cur_agent_team"),
                  (neq, ":player_agent", ":cur_agent"),
                  (agent_get_class, ":agent_class", ":cur_agent"),
                  (this_or_next|eq, ":agent_class", grc_infantry),
                  (eq, ":agent_class", grc_cavalry),
                  (agent_get_slot, ":x_pos", ":cur_agent", 1),
                  (eq, ":x_pos", 0),
                  (assign, ":y_pos", 0),
                  (try_begin),
                    (eq, ":slot_1_positioned", 0),
                    (assign, ":x_pos", -600),
                    (assign, ":y_pos", 0),
                    (val_add, ":slot_1_positioned", 1),
                  (else_try),
                    (eq, ":slot_2_positioned", 0),
                    (assign, ":x_pos", -600),
                    (assign, ":y_pos", -200),
                    (val_add, ":slot_2_positioned", 1),
                  (else_try),
                    (eq, ":slot_3_positioned", 0),
                    (assign, ":x_pos", -600),
                    (assign, ":y_pos", -400),
                    (val_add, ":slot_3_positioned", 1),
                  (else_try),
                    (eq, ":slot_4_positioned", 0),
                    (assign, ":x_pos", 600),
                    (assign, ":y_pos", 0),
                    (val_add, ":slot_4_positioned", 1),
                  (else_try),
                    (eq, ":slot_5_positioned", 0),
                    (assign, ":x_pos", 600),
                    (assign, ":y_pos", -200),
                    (val_add, ":slot_5_positioned", 1),
                  (else_try),
                    (eq, ":slot_6_positioned", 0),
                    (assign, ":x_pos", 600),
                    (assign, ":y_pos", -400),
                    (val_add, ":slot_6_positioned", 1),
                  (try_end),
                  (val_add, "$belfry_num_slots_positioned", 1),
                  (agent_set_slot, ":cur_agent", 1, ":x_pos"),
                  (agent_set_slot, ":cur_agent", 2, ":y_pos"),
                (try_end),
              (try_end),
              (try_begin),
                (store_mission_timer_a, ":cur_timer"),
                (gt, ":cur_timer", 20),
                (lt, "$belfry_num_slots_positioned", 6),
                (try_for_agents, ":cur_agent"),
                  (agent_is_alive, ":cur_agent"),
                  (agent_get_team, ":cur_agent_team", ":cur_agent"),
                  (this_or_next|eq, "$attacker_team", ":cur_agent_team"),
                  (             eq, "$attacker_team_2", ":cur_agent_team"),
                  (neq, ":player_agent", ":cur_agent"),
                  (agent_get_slot, ":x_pos", ":cur_agent", 1),
                  (eq, ":x_pos", 0),
                  (assign, ":y_pos", 0),
                  (try_begin),
                    (eq, ":slot_1_positioned", 0),
                    (assign, ":x_pos", -600),
                    (assign, ":y_pos", 0),
                    (val_add, ":slot_1_positioned", 1),
                  (else_try),
                    (eq, ":slot_2_positioned", 0),
                    (assign, ":x_pos", -600),
                    (assign, ":y_pos", -200),
                    (val_add, ":slot_2_positioned", 1),
                  (else_try),
                    (eq, ":slot_3_positioned", 0),
                    (assign, ":x_pos", -600),
                    (assign, ":y_pos", -400),
                    (val_add, ":slot_3_positioned", 1),
                  (else_try),
                    (eq, ":slot_4_positioned", 0),
                    (assign, ":x_pos", 600),
                    (assign, ":y_pos", 0),
                    (val_add, ":slot_4_positioned", 1),
                  (else_try),
                    (eq, ":slot_5_positioned", 0),
                    (assign, ":x_pos", 600),
                    (assign, ":y_pos", -200),
                    (val_add, ":slot_5_positioned", 1),
                  (else_try),
                    (eq, ":slot_6_positioned", 0),
                    (assign, ":x_pos", 600),
                    (assign, ":y_pos", -400),
                    (val_add, ":slot_6_positioned", 1),
                  (try_end),
                  (val_add, "$belfry_num_slots_positioned", 1),
                  (agent_set_slot, ":cur_agent", 1, ":x_pos"),
                  (agent_set_slot, ":cur_agent", 2, ":y_pos"),
                (try_end),
              (try_end),
            (else_try),
              (assign, ":end_trigger", 1),
              (try_for_agents, ":cur_agent"),
                (agent_clear_scripted_mode, ":cur_agent"),
              (try_end),
              (set_show_messages, 0),
              (team_give_order, "$attacker_team", grc_everyone, mordr_charge),
              (set_show_messages, 1),
            (try_end),
            (eq, ":end_trigger", 1),
        ]),
        
        # script_siege_move_archers_to_archer_positions
        # Input: none
        # Output: none
        ("siege_move_archers_to_archer_positions",
          [
            (try_for_agents, ":agent_no"),
              (agent_is_alive, ":agent_no"),
              (agent_slot_eq, ":agent_no", slot_agent_is_not_reinforcement, 0),
              (agent_is_defender, ":agent_no"),
              (agent_get_class, ":agent_class", ":agent_no"),
              (agent_get_troop_id, ":agent_troop", ":agent_no"),
              (eq, ":agent_class", grc_archers),
              (try_begin),
                (agent_slot_eq, ":agent_no", slot_agent_target_entry_point, 0),
                (store_random_in_range, ":random_entry_point", 40, 44),
                (agent_set_slot, ":agent_no", slot_agent_target_entry_point, ":random_entry_point"),
              (try_end),
              (try_begin),
                (agent_get_position, pos0, ":agent_no"),
                (entry_point_get_position, pos1, ":random_entry_point"),
                (get_distance_between_positions, ":dist", pos0, pos1),
                (lt, ":dist", 300),
                (agent_clear_scripted_mode, ":agent_no"),
                (agent_set_slot, ":agent_no", slot_agent_is_in_scripted_mode, 0),
                (agent_set_slot, ":agent_no", slot_agent_is_not_reinforcement, 1),
                (str_store_troop_name, s1, ":agent_troop"),
                (assign, reg0, ":agent_no"),
                #         (display_message, "@{s1} ({reg0}) reached pos"),
              (else_try),
                (agent_get_simple_behavior, ":agent_sb", ":agent_no"),
                (agent_get_combat_state, ":agent_cs", ":agent_no"),
                (this_or_next|eq, ":agent_sb", aisb_ranged),
                (eq, ":agent_sb", aisb_go_to_pos),#scripted mode
                (eq, ":agent_cs", 7), # 7 = no visible targets (state for ranged units)
                (try_begin),
                  (agent_slot_eq, ":agent_no", slot_agent_is_in_scripted_mode, 0),
                  (agent_set_scripted_destination, ":agent_no", pos1, 0),
                  (agent_set_slot, ":agent_no", slot_agent_is_in_scripted_mode, 1),
                  (str_store_troop_name, s1, ":agent_troop"),
                  (assign, reg0, ":agent_no"),
                  #           (display_message, "@{s1} ({reg0}) moving to pos"),
                (try_end),
              (else_try),
                (try_begin),
                  (agent_slot_eq, ":agent_no", slot_agent_is_in_scripted_mode, 1),
                  (agent_clear_scripted_mode, ":agent_no"),
                  (agent_set_slot, ":agent_no", slot_agent_is_in_scripted_mode, 0),
                  (str_store_troop_name, s1, ":agent_troop"),
                  (assign, reg0, ":agent_no"),
                  #           (display_message, "@{s1} ({reg0}) seeing target or changed mode"),
                (try_end),
              (try_end),
            (try_end),
        ]),
        
        
        # script_store_movement_order_name_to_s1
        # Input: arg1 = team_no, arg2 = class_no
        # Output: s1 = order_name
        ("store_movement_order_name_to_s1",
          [(store_script_param_1, ":team_no"),
            (store_script_param_2, ":class_no"),
            (team_get_movement_order, ":cur_order", ":team_no", ":class_no"),
            (try_begin),
              (eq, ":cur_order", mordr_hold),
              (str_store_string, s1, "@Holding"),
            (else_try),
              (eq, ":cur_order", mordr_follow),
              (str_store_string, s1, "@Following"),
            (else_try),
              (eq, ":cur_order", mordr_charge),
              (str_store_string, s1, "@Charging"),
            (else_try),
              (eq, ":cur_order", mordr_advance),
              (str_store_string, s1, "@Advancing"),
            (else_try),
              (eq, ":cur_order", mordr_fall_back),
              (str_store_string, s1, "@Falling Back"),
            (else_try),
              (eq, ":cur_order", mordr_stand_closer),
              (str_store_string, s1, "@Standing Closer"),
            (else_try),
              (eq, ":cur_order", mordr_spread_out),
              (str_store_string, s1, "@Spreading Out"),
            (else_try),
              (eq, ":cur_order", mordr_stand_ground),
              (str_store_string, s1, "@Standing"),
            (else_try),
              (str_store_string, s1, "@N/A"),
            (try_end),
        ]),
        
        # script_store_riding_order_name_to_s1
        # Input: arg1 = team_no, arg2 = class_no
        # Output: s1 = order_name
        ("store_riding_order_name_to_s1",
          [(store_script_param_1, ":team_no"),
            (store_script_param_2, ":class_no"),
            (team_get_riding_order, ":cur_order", ":team_no", ":class_no"),
            (try_begin),
              (eq, ":cur_order", rordr_free),
              (str_store_string, s1, "@Free"),
            (else_try),
              (eq, ":cur_order", rordr_mount),
              (str_store_string, s1, "@Mount"),
            (else_try),
              (eq, ":cur_order", rordr_dismount),
              (str_store_string, s1, "@Dismount"),
            (else_try),
              (str_store_string, s1, "@N/A"),
            (try_end),
        ]),
        
        # script_store_weapon_usage_order_name_to_s1
        # Input: arg1 = team_no, arg2 = class_no
        # Output: s1 = order_name
        ("store_weapon_usage_order_name_to_s1",
          [(store_script_param_1, ":team_no"),
            (store_script_param_2, ":class_no"),
            (team_get_weapon_usage_order, ":cur_order", ":team_no", ":class_no"),
            (team_get_hold_fire_order, ":cur_hold_fire", ":team_no", ":class_no"),
            (try_begin),
              (eq, ":cur_order", wordr_use_any_weapon),
              (eq, ":cur_hold_fire", aordr_fire_at_will),
              (str_store_string, s1, "@Any Weapon"),
            (else_try),
              (eq, ":cur_order", wordr_use_blunt_weapons),
              (eq, ":cur_hold_fire", aordr_fire_at_will),
              (str_store_string, s1, "@Blunt Weapons"),
            (else_try),
              (eq, ":cur_order", wordr_use_any_weapon),
              (eq, ":cur_hold_fire", aordr_hold_your_fire),
              (str_store_string, s1, "str_hold_fire"),
            (else_try),
              (eq, ":cur_order", wordr_use_blunt_weapons),
              (eq, ":cur_hold_fire", aordr_hold_your_fire),
              (str_store_string, s1, "str_blunt_hold_fire"),
            (else_try),
              (str_store_string, s1, "@N/A"),
            (try_end),
        ]),
        
        # script_team_give_order_from_order_panel
        # Input: arg1 = leader_agent_no, arg2 = class_no
        # Output: none
        ("team_give_order_from_order_panel",
          [(store_script_param_1, ":leader_agent_no"),
            (store_script_param_2, ":order"),
            (agent_get_team, ":team_no", ":leader_agent_no"),
            (set_show_messages, 0),
            (try_begin),
              (eq, "$g_formation_group0_selected", 1),
              (team_give_order, ":team_no", 0, ":order"),
            (try_end),
            (try_begin),
              (eq, "$g_formation_group1_selected", 1),
              (team_give_order, ":team_no", 1, ":order"),
            (try_end),
            (try_begin),
              (eq, "$g_formation_group2_selected", 1),
              (team_give_order, ":team_no", 2, ":order"),
            (try_end),
            (try_begin),
              (eq, "$g_formation_group3_selected", 1),
              (team_give_order, ":team_no", 3, ":order"),
            (try_end),
            (try_begin),
              (eq, "$g_formation_group4_selected", 1),
              (team_give_order, ":team_no", 4, ":order"),
            (try_end),
            (try_begin),
              (eq, "$g_formation_group5_selected", 1),
              (team_give_order, ":team_no", 5, ":order"),
            (try_end),
            (try_begin),
              (eq, "$g_formation_group6_selected", 1),
              (team_give_order, ":team_no", 6, ":order"),
            (try_end),
            (try_begin),
              (eq, "$g_formation_group7_selected", 1),
              (team_give_order, ":team_no", 7, ":order"),
            (try_end),
            (try_begin),
              (eq, "$g_formation_group8_selected", 1),
              (team_give_order, ":team_no", 8, ":order"),
            (try_end),
            
            (try_begin),
              (eq, ":order", mordr_hold),
              (agent_get_position, pos1, ":leader_agent_no"),
              (try_begin),
                (eq, "$g_formation_group0_selected", 1),
                (team_set_order_position, ":team_no", 0, pos1),
              (try_end),
              (try_begin),
                (eq, "$g_formation_group1_selected", 1),
                (team_set_order_position, ":team_no", 1, pos1),
              (try_end),
              (try_begin),
                (eq, "$g_formation_group2_selected", 1),
                (team_set_order_position, ":team_no", 2, pos1),
              (try_end),
              (try_begin),
                (eq, "$g_formation_group3_selected", 1),
                (team_set_order_position, ":team_no", 3, pos1),
              (try_end),
              (try_begin),
                (eq, "$g_formation_group4_selected", 1),
                (team_set_order_position, ":team_no", 4, pos1),
              (try_end),
              (try_begin),
                (eq, "$g_formation_group5_selected", 1),
                (team_set_order_position, ":team_no", 5, pos1),
              (try_end),
              (try_begin),
                (eq, "$g_formation_group6_selected", 1),
                (team_set_order_position, ":team_no", 6, pos1),
              (try_end),
              (try_begin),
                (eq, "$g_formation_group7_selected", 1),
                (team_set_order_position, ":team_no", 7, pos1),
              (try_end),
              (try_begin),
                (eq, "$g_formation_group8_selected", 1),
                (team_set_order_position, ":team_no", 8, pos1),
              (try_end),
            (try_end),
            (set_show_messages, 1),
        ]),
        
        
        # script_update_order_panel
        # Input: arg1 = team_no
        # Output: none
        ("update_order_panel",
          [(store_script_param_1, ":team_no"),
            (set_fixed_point_multiplier, 1000),
            
            #ozan added
            (try_begin),
              (eq, "$group0_has_troops", 1),
              (call_script, "script_store_movement_order_name_to_s1", ":team_no", 0),
              (overlay_set_text, "$g_presentation_but0_movement", s1),
              (call_script, "script_store_riding_order_name_to_s1", ":team_no", 0),
              (overlay_set_text, "$g_presentation_but0_riding", s1),
              (call_script, "script_store_weapon_usage_order_name_to_s1", ":team_no", 0),
              (overlay_set_text, "$g_presentation_but0_weapon_usage", s1),
            (try_end),
            (try_begin),
              (eq, "$group1_has_troops", 1),
              (call_script, "script_store_movement_order_name_to_s1", ":team_no", 1),
              (overlay_set_text, "$g_presentation_but1_movement", s1),
              (call_script, "script_store_riding_order_name_to_s1", ":team_no", 1),
              (overlay_set_text, "$g_presentation_but1_riding", s1),
              (call_script, "script_store_weapon_usage_order_name_to_s1", ":team_no", 1),
              (overlay_set_text, "$g_presentation_but1_weapon_usage", s1),
            (try_end),
            (try_begin),
              (eq, "$group2_has_troops", 1),
              (call_script, "script_store_movement_order_name_to_s1", ":team_no", 2),
              (overlay_set_text, "$g_presentation_but2_movement", s1),
              (call_script, "script_store_riding_order_name_to_s1", ":team_no", 2),
              (overlay_set_text, "$g_presentation_but2_riding", s1),
              (call_script, "script_store_weapon_usage_order_name_to_s1", ":team_no", 2),
              (overlay_set_text, "$g_presentation_but2_weapon_usage", s1),
            (try_end),
            (try_begin),
              (eq, "$group3_has_troops", 1),
              (call_script, "script_store_movement_order_name_to_s1", ":team_no", 3),
              (overlay_set_text, "$g_presentation_but3_movement", s1),
              (call_script, "script_store_riding_order_name_to_s1", ":team_no", 3),
              (overlay_set_text, "$g_presentation_but3_riding", s1),
              (call_script, "script_store_weapon_usage_order_name_to_s1", ":team_no", 3),
              (overlay_set_text, "$g_presentation_but3_weapon_usage", s1),
            (try_end),
            (try_begin),
              (eq, "$group4_has_troops", 1),
              (call_script, "script_store_movement_order_name_to_s1", ":team_no", 4),
              (overlay_set_text, "$g_presentation_but4_movement", s1),
              (call_script, "script_store_riding_order_name_to_s1", ":team_no", 4),
              (overlay_set_text, "$g_presentation_but4_riding", s1),
              (call_script, "script_store_weapon_usage_order_name_to_s1", ":team_no", 4),
              (overlay_set_text, "$g_presentation_but4_weapon_usage", s1),
            (try_end),
            (try_begin),
              (eq, "$group5_has_troops", 1),
              (call_script, "script_store_movement_order_name_to_s1", ":team_no", 5),
              (overlay_set_text, "$g_presentation_but5_movement", s1),
              (call_script, "script_store_riding_order_name_to_s1", ":team_no", 5),
              (overlay_set_text, "$g_presentation_but5_riding", s1),
              (call_script, "script_store_weapon_usage_order_name_to_s1", ":team_no", 5),
              (overlay_set_text, "$g_presentation_but5_weapon_usage", s1),
            (try_end),
            (try_begin),
              (eq, "$group6_has_troops", 1),
              (call_script, "script_store_movement_order_name_to_s1", ":team_no", 6),
              (overlay_set_text, "$g_presentation_but6_movement", s1),
              (call_script, "script_store_riding_order_name_to_s1", ":team_no", 6),
              (overlay_set_text, "$g_presentation_but6_riding", s1),
              (call_script, "script_store_weapon_usage_order_name_to_s1", ":team_no", 6),
              (overlay_set_text, "$g_presentation_but6_weapon_usage", s1),
            (try_end),
            (try_begin),
              (eq, "$group7_has_troops", 1),
              (call_script, "script_store_movement_order_name_to_s1", ":team_no", 7),
              (overlay_set_text, "$g_presentation_but7_movement", s1),
              (call_script, "script_store_riding_order_name_to_s1", ":team_no", 7),
              (overlay_set_text, "$g_presentation_but7_riding", s1),
              (call_script, "script_store_weapon_usage_order_name_to_s1", ":team_no", 7),
              (overlay_set_text, "$g_presentation_but7_weapon_usage", s1),
            (try_end),
            (try_begin),
              (eq, "$group8_has_troops", 1),
              (call_script, "script_store_movement_order_name_to_s1", ":team_no", 8),
              (overlay_set_text, "$g_presentation_but8_movement", s1),
              (call_script, "script_store_riding_order_name_to_s1", ":team_no", 8),
              (overlay_set_text, "$g_presentation_but8_riding", s1),
              (call_script, "script_store_weapon_usage_order_name_to_s1", ":team_no", 8),
              (overlay_set_text, "$g_presentation_but8_weapon_usage", s1),
            (try_end),
            
            #ozan added
            (assign, ":stat_position_y", 660),
            (try_begin),
              (position_set_y, pos1, ":stat_position_y"),
              (eq, "$group0_has_troops", 1),
              (position_set_x, pos1, 270),
              (overlay_set_position, "$g_presentation_but0_movement", pos1),
              (position_set_x, pos1, 410),
              (overlay_set_position, "$g_presentation_but0_riding", pos1),
              (position_set_x, pos1, 550),
              (overlay_set_position, "$g_presentation_but0_weapon_usage", pos1),
              (val_add, ":stat_position_y", -40),
            (try_end),
            (try_begin),
              (position_set_y, pos1, ":stat_position_y"),
              (eq, "$group1_has_troops", 1),
              (position_set_x, pos1, 270),
              (overlay_set_position, "$g_presentation_but1_movement", pos1),
              (position_set_x, pos1, 410),
              (overlay_set_position, "$g_presentation_but1_riding", pos1),
              (position_set_x, pos1, 550),
              (overlay_set_position, "$g_presentation_but1_weapon_usage", pos1),
              (val_add, ":stat_position_y", -40),
            (try_end),
            (try_begin),
              (position_set_y, pos1, ":stat_position_y"),
              (eq, "$group2_has_troops", 1),
              (position_set_x, pos1, 270),
              (overlay_set_position, "$g_presentation_but2_movement", pos1),
              (position_set_x, pos1, 410),
              (overlay_set_position, "$g_presentation_but2_riding", pos1),
              (position_set_x, pos1, 550),
              (overlay_set_position, "$g_presentation_but2_weapon_usage", pos1),
              (val_add, ":stat_position_y", -40),
            (try_end),
            (try_begin),
              (position_set_y, pos1, ":stat_position_y"),
              (eq, "$group3_has_troops", 1),
              (position_set_x, pos1, 270),
              (overlay_set_position, "$g_presentation_but3_movement", pos1),
              (position_set_x, pos1, 410),
              (overlay_set_position, "$g_presentation_but3_riding", pos1),
              (position_set_x, pos1, 550),
              (overlay_set_position, "$g_presentation_but3_weapon_usage", pos1),
              (val_add, ":stat_position_y", -40),
            (try_end),
            (try_begin),
              (position_set_y, pos1, ":stat_position_y"),
              (eq, "$group4_has_troops", 1),
              (position_set_x, pos1, 270),
              (overlay_set_position, "$g_presentation_but4_movement", pos1),
              (position_set_x, pos1, 410),
              (overlay_set_position, "$g_presentation_but4_riding", pos1),
              (position_set_x, pos1, 550),
              (overlay_set_position, "$g_presentation_but4_weapon_usage", pos1),
              (val_add, ":stat_position_y", -40),
            (try_end),
            (try_begin),
              (position_set_y, pos1, ":stat_position_y"),
              (eq, "$group5_has_troops", 1),
              (position_set_x, pos1, 270),
              (overlay_set_position, "$g_presentation_but5_movement", pos1),
              (position_set_x, pos1, 410),
              (overlay_set_position, "$g_presentation_but5_riding", pos1),
              (position_set_x, pos1, 550),
              (overlay_set_position, "$g_presentation_but5_weapon_usage", pos1),
              (val_add, ":stat_position_y", -40),
            (try_end),
            (try_begin),
              (position_set_y, pos1, ":stat_position_y"),
              (eq, "$group6_has_troops", 1),
              (position_set_x, pos1, 270),
              (overlay_set_position, "$g_presentation_but6_movement", pos1),
              (position_set_x, pos1, 410),
              (overlay_set_position, "$g_presentation_but6_riding", pos1),
              (position_set_x, pos1, 550),
              (overlay_set_position, "$g_presentation_but6_weapon_usage", pos1),
              (val_add, ":stat_position_y", -40),
            (try_end),
            (try_begin),
              (position_set_y, pos1, ":stat_position_y"),
              (eq, "$group7_has_troops", 1),
              (position_set_x, pos1, 270),
              (overlay_set_position, "$g_presentation_but7_movement", pos1),
              (position_set_x, pos1, 410),
              (overlay_set_position, "$g_presentation_but7_riding", pos1),
              (position_set_x, pos1, 550),
              (overlay_set_position, "$g_presentation_but7_weapon_usage", pos1),
              (val_add, ":stat_position_y", -40),
            (try_end),
            (try_begin),
              (position_set_y, pos1, ":stat_position_y"),
              (eq, "$group8_has_troops", 1),
              (position_set_x, pos1, 270),
              (overlay_set_position, "$g_presentation_but8_movement", pos1),
              (position_set_x, pos1, 410),
              (overlay_set_position, "$g_presentation_but8_riding", pos1),
              (position_set_x, pos1, 550),
              (overlay_set_position, "$g_presentation_but8_weapon_usage", pos1),
              (val_add, ":stat_position_y", -40),
            (try_end),
        ]),
        
        # script_update_agent_position_on_map
        # Input: arg1 = agent_no, pos2 = map_size_pos
        # Output: none
        ("update_agent_position_on_map",
          [(store_script_param_1, ":agent_no"),
            (agent_get_slot, ":agent_overlay", ":agent_no", slot_agent_map_overlay_id),
            
            (get_player_agent_no, ":player_agent"),
            (try_begin),
              (le, ":agent_overlay", 0),
              (set_fixed_point_multiplier, 1000),
              (try_begin),
                (eq, ":agent_no", ":player_agent"),
                (create_mesh_overlay, reg1, "mesh_player_dot"),
                (position_set_x, pos1, 500),
                (position_set_y, pos1, 500),
                (overlay_set_size, reg1, pos1),
              (else_try),
                (create_mesh_overlay, reg1, "mesh_white_dot"),
                (position_set_x, pos1, 200),
                (position_set_y, pos1, 200),
                (overlay_set_size, reg1, pos1),
              (try_end),
              (overlay_set_alpha, reg1, 0x88),
              (agent_set_slot, ":agent_no", slot_agent_map_overlay_id, reg1),
              (assign, ":agent_overlay", reg1),
            (try_end),
            
            (try_begin),
              (neq, ":agent_no", ":player_agent"),
              (agent_get_party_id, ":agent_party", ":agent_no"),
              (try_begin),
                (eq, ":agent_party", "p_main_party"),
                (agent_get_division, ":agent_division", ":agent_no"),
                (try_begin),
                  (eq, ":agent_division", 0),
                  (overlay_set_color, ":agent_overlay", 0x8d5220),
                (else_try),
                  (eq, ":agent_division", 1),
                  (overlay_set_color, ":agent_overlay", 0x34c6e4),
                (else_try),
                  (eq, ":agent_division", 2),
                  (overlay_set_color, ":agent_overlay", 0x569619),
                (else_try),
                  (eq, ":agent_division", 3),
                  (overlay_set_color, ":agent_overlay", 0xFFE500),
                (else_try),
                  (eq, ":agent_division", 4),
                  (overlay_set_color, ":agent_overlay", 0x990099),
                (else_try),
                  (eq, ":agent_division", 5),
                  (overlay_set_color, ":agent_overlay", 0x99FE80),
                (else_try),
                  (eq, ":agent_division", 6),
                  (overlay_set_color, ":agent_overlay", 0x9DEFFE),
                (else_try),
                  (eq, ":agent_division", 7),
                  (overlay_set_color, ":agent_overlay", 0xFECB9D),
                (else_try),
                  (eq, ":agent_division", 8),
                  (overlay_set_color, ":agent_overlay", 0xB19C9C),
                (try_end),
              (else_try),
                (agent_is_ally, ":agent_no"),
                (overlay_set_color, ":agent_overlay", 0x5555FF),
              (else_try),
                (overlay_set_color, ":agent_overlay", 0xFF0000),
              (try_end),
            (try_end),
            
            (try_begin),
              (eq, ":agent_no", ":player_agent"),
              (agent_get_look_position, pos1, ":agent_no"),
              (position_get_rotation_around_z, ":rot", pos1),
              (init_position, pos10),
              (position_rotate_z, pos10, ":rot"),
              (overlay_set_mesh_rotation, ":agent_overlay", pos10),
              (call_script, "script_convert_3d_pos_to_map_pos"),
            (else_try),
              (agent_get_position, pos1, ":agent_no"),
              (call_script, "script_convert_3d_pos_to_map_pos"),
            (try_end),
            (overlay_set_position, ":agent_overlay", pos0),
        ]),
        
        # script_convert_3d_pos_to_map_pos
        # Input: pos1 = 3d_pos, pos2 = map_size_pos
        # Output: pos0 = map_pos
        ("convert_3d_pos_to_map_pos",
          [(set_fixed_point_multiplier, 1000),
            (position_transform_position_to_local, pos3, pos2, pos1),
            (position_get_x, ":agent_x_pos", pos3),
            (position_get_y, ":agent_y_pos", pos3),
            (val_div, ":agent_x_pos", "$g_battle_map_scale"),
            (val_div, ":agent_y_pos", "$g_battle_map_scale"),
            (set_fixed_point_multiplier, 1000),
            (store_sub, ":map_x", 980, "$g_battle_map_width"),
            (store_sub, ":map_y", 730, "$g_battle_map_height"),
            (val_add, ":agent_x_pos", ":map_x"),
            (val_add, ":agent_y_pos", ":map_y"),
            (position_set_x, pos0, ":agent_x_pos"),
            (position_set_y, pos0, ":agent_y_pos"),
        ]),
        
        # script_update_order_flags_on_map
        # Input: none
        # Output: none
        ("update_order_flags_on_map",
          [(set_fixed_point_multiplier, 1000),
            (get_player_agent_no, ":player_agent"),
            (agent_get_team, ":player_team", ":player_agent"),
            
            (get_scene_boundaries, pos2, pos3),
            
            (team_get_movement_order, ":cur_order", ":player_team", grc_infantry),
            (try_begin),
              (eq, ":cur_order", mordr_hold),
              (team_get_order_position, pos1, ":player_team", grc_infantry),
              (call_script, "script_convert_3d_pos_to_map_pos"),
              (overlay_set_alpha, "$g_battle_map_infantry_order_flag", 0xFF),
              (overlay_set_position, "$g_battle_map_infantry_order_flag", pos0),
            (else_try),
              (overlay_set_alpha, "$g_battle_map_infantry_order_flag", 0),
            (try_end),
            (team_get_movement_order, ":cur_order", ":player_team", grc_archers),
            (try_begin),
              (eq, ":cur_order", mordr_hold),
              (team_get_order_position, pos1, ":player_team", grc_archers),
              (call_script, "script_convert_3d_pos_to_map_pos"),
              (overlay_set_alpha, "$g_battle_map_archers_order_flag", 0xFF),
              (overlay_set_position, "$g_battle_map_archers_order_flag", pos0),
            (else_try),
              (overlay_set_alpha, "$g_battle_map_archers_order_flag", 0),
            (try_end),
            (team_get_movement_order, ":cur_order", ":player_team", grc_cavalry),
            (try_begin),
              (eq, ":cur_order", mordr_hold),
              (team_get_order_position, pos1, ":player_team", grc_cavalry),
              (call_script, "script_convert_3d_pos_to_map_pos"),
              (overlay_set_alpha, "$g_battle_map_cavalry_order_flag", 0xFF),
              (overlay_set_position, "$g_battle_map_cavalry_order_flag", pos0),
            (else_try),
              (overlay_set_alpha, "$g_battle_map_cavalry_order_flag", 0),
            (try_end),
        ]),
        
        # script_update_order_panel_checked_classes
        # Input: none
        # Output: none
        ("update_order_panel_checked_classes",
          [(get_player_agent_no, ":player_agent"),
            (agent_get_team, ":player_team", ":player_agent"),
            
            (try_begin),
              (eq, "$group0_has_troops", 1),
              (class_is_listening_order, ":player_team", 0),
              (overlay_set_val, "$g_presentation_obj_battle_check0", 1),
              (assign, "$g_formation_group0_selected", 1),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but0", 250, 0x44),
            (else_try),
              (eq, "$group0_has_troops", 1),
              (overlay_set_val, "$g_presentation_obj_battle_check0", 0),
              (assign, "$g_formation_group0_selected", 0),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but0", 250, 0),
            (try_end),
            (try_begin),
              (eq, "$group1_has_troops", 1),
              (class_is_listening_order, ":player_team", 1),
              (overlay_set_val, "$g_presentation_obj_battle_check1", 1),
              (assign, "$g_formation_group1_selected", 1),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but1", 250, 0x44),
            (else_try),
              (eq, "$group1_has_troops", 1),
              (overlay_set_val, "$g_presentation_obj_battle_check1", 0),
              (assign, "$g_formation_group1_selected", 0),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but1", 250, 0),
            (try_end),
            (try_begin),
              (eq, "$group2_has_troops", 1),
              (class_is_listening_order, ":player_team", 2),
              (overlay_set_val, "$g_presentation_obj_battle_check2", 1),
              (assign, "$g_formation_group2_selected", 1),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but2", 250, 0x44),
            (else_try),
              (eq, "$group2_has_troops", 1),
              (overlay_set_val, "$g_presentation_obj_battle_check2", 0),
              (assign, "$g_formation_group2_selected", 0),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but2", 250, 0),
            (try_end),
            (try_begin),
              (eq, "$group3_has_troops", 1),
              (class_is_listening_order, ":player_team", 3),
              (overlay_set_val, "$g_presentation_obj_battle_check3", 1),
              (assign, "$g_formation_group3_selected", 1),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but3", 250, 0x44),
            (else_try),
              (eq, "$group3_has_troops", 1),
              (overlay_set_val, "$g_presentation_obj_battle_check3", 0),
              (assign, "$g_formation_group3_selected", 0),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but3", 250, 0),
            (try_end),
            (try_begin),
              (eq, "$group4_has_troops", 1),
              (class_is_listening_order, ":player_team", 4),
              (overlay_set_val, "$g_presentation_obj_battle_check4", 1),
              (assign, "$g_formation_group4_selected", 1),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but4", 250, 0x44),
            (else_try),
              (eq, "$group4_has_troops", 1),
              (overlay_set_val, "$g_presentation_obj_battle_check4", 0),
              (assign, "$g_formation_group4_selected", 0),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but4", 250, 0),
            (try_end),
            (try_begin),
              (eq, "$group5_has_troops", 1),
              (class_is_listening_order, ":player_team", 5),
              (overlay_set_val, "$g_presentation_obj_battle_check5", 1),
              (assign, "$g_formation_group5_selected", 1),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but5", 250, 0x44),
            (else_try),
              (eq, "$group5_has_troops", 1),
              (overlay_set_val, "$g_presentation_obj_battle_check5", 0),
              (assign, "$g_formation_group5_selected", 0),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but5", 250, 0),
            (try_end),
            (try_begin),
              (eq, "$group6_has_troops", 1),
              (class_is_listening_order, ":player_team", 6),
              (overlay_set_val, "$g_presentation_obj_battle_check6", 1),
              (assign, "$g_formation_group6_selected", 1),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but6", 250, 0x44),
            (else_try),
              (eq, "$group6_has_troops", 1),
              (overlay_set_val, "$g_presentation_obj_battle_check6", 0),
              (assign, "$g_formation_group6_selected", 0),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but6", 250, 0),
            (try_end),
            (try_begin),
              (eq, "$group7_has_troops", 1),
              (class_is_listening_order, ":player_team", 7),
              (overlay_set_val, "$g_presentation_obj_battle_check7", 1),
              (assign, "$g_formation_group7_selected", 1),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but7", 250, 0x44),
            (else_try),
              (eq, "$group7_has_troops", 1),
              (overlay_set_val, "$g_presentation_obj_battle_check7", 0),
              (assign, "$g_formation_group7_selected", 0),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but7", 250, 0),
            (try_end),
            (try_begin),
              (eq, "$group8_has_troops", 1),
              (class_is_listening_order, ":player_team", 8),
              (overlay_set_val, "$g_presentation_obj_battle_check8", 1),
              (assign, "$g_formation_group8_selected", 1),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but8", 250, 0x44),
            (else_try),
              (eq, "$group8_has_troops", 1),
              (overlay_set_val, "$g_presentation_obj_battle_check8", 0),
              (assign, "$g_formation_group8_selected", 0),
              (overlay_animate_to_alpha, "$g_presentation_obj_battle_but8", 250, 0),
            (try_end),
        ]),
        
        # script_update_order_panel_statistics_and_map
        # Input: none
        # Output: none
        ("update_order_panel_statistics_and_map", #TODO: Call this in every battle mission template, once per second
          [(set_fixed_point_multiplier, 1000),
            
            (assign, ":num_us_ready_group0", 0),
            (assign, ":num_us_ready_group1", 0),
            (assign, ":num_us_ready_group2", 0),
            (assign, ":num_us_ready_group3", 0),
            (assign, ":num_us_ready_group4", 0),
            (assign, ":num_us_ready_group5", 0),
            (assign, ":num_us_ready_group6", 0),
            (assign, ":num_us_ready_group7", 0),
            (assign, ":num_us_ready_group8", 0),
            
            (assign, ":num_us_ready_men", 0),
            (assign, ":num_us_wounded_men", 0),
            (assign, ":num_us_routed_men", 0),
            (assign, ":num_us_dead_men", 0),
            (assign, ":num_allies_ready_men", 0),
            (assign, ":num_allies_wounded_men", 0),
            (assign, ":num_allies_routed_men", 0),
            (assign, ":num_allies_dead_men", 0),
            (assign, ":num_enemies_ready_men", 0),
            (assign, ":num_enemies_wounded_men", 0),
            (assign, ":num_enemies_routed_men", 0),
            (assign, ":num_enemies_dead_men", 0),
            
            (get_scene_boundaries, pos2, pos3),
            
            (try_for_agents,":cur_agent"),
              (agent_is_human, ":cur_agent"),
              (agent_get_division, ":agent_division", ":cur_agent"),
              (agent_get_party_id, ":agent_party", ":cur_agent"),
              (agent_get_slot, ":agent_overlay", ":cur_agent", slot_agent_map_overlay_id),
              (try_begin),
                (eq, ":agent_party", "p_main_party"),
                (try_begin),
                  (agent_is_alive, ":cur_agent"),
                  (call_script, "script_update_agent_position_on_map", ":cur_agent"),
                  (try_begin),
                    (eq, ":agent_division", 0),
                    (val_add, ":num_us_ready_group0", 1),
                    (eq, "$group0_has_troops", 1), #added to solve problem. test this.
                  (else_try),
                    (eq, ":agent_division", 1),
                    (val_add, ":num_us_ready_group1", 1),
                    (eq, "$group1_has_troops", 1), #added to solve problem.
                  (else_try),
                    (eq, ":agent_division", 2),
                    (val_add, ":num_us_ready_group2", 1),
                    (eq, "$group2_has_troops", 1), #added to solve problem.
                  (else_try),
                    (eq, ":agent_division", 3),
                    (val_add, ":num_us_ready_group3", 1),
                    (eq, "$group3_has_troops", 1), #added to solve problem.
                  (else_try),
                    (eq, ":agent_division", 4),
                    (val_add, ":num_us_ready_group4", 1),
                    (eq, "$group4_has_troops", 1), #added to solve problem.
                  (else_try),
                    (eq, ":agent_division", 5),
                    (val_add, ":num_us_ready_group5", 1),
                    (eq, "$group5_has_troops", 1), #added to solve problem.
                  (else_try),
                    (eq, ":agent_division", 6),
                    (val_add, ":num_us_ready_group6", 1),
                    (eq, "$group6_has_troops", 1), #added to solve problem.
                  (else_try),
                    (eq, ":agent_division", 7),
                    (val_add, ":num_us_ready_group7", 1),
                    (eq, "$group7_has_troops", 1), #added to solve problem.
                  (else_try),
                    (eq, ":agent_division", 8),
                    (val_add, ":num_us_ready_group8", 1),
                    (eq, "$group8_has_troops", 1), #added to solve problem.
                  (try_end),
                  (val_add, ":num_us_ready_men", 1),
                (else_try),
                  (overlay_set_alpha, ":agent_overlay", 0),
                  (agent_is_wounded, ":cur_agent"),
                  (val_add, ":num_us_wounded_men", 1),
                (else_try),
                  (agent_is_routed, ":cur_agent"),
                  (val_add, ":num_us_routed_men", 1),
                (else_try),
                  (val_add, ":num_us_dead_men", 1),
                (try_end),
              (else_try),
                (agent_is_ally, ":cur_agent"),
                (try_begin),
                  (agent_is_alive, ":cur_agent"),
                  (call_script, "script_update_agent_position_on_map", ":cur_agent"),
                  (val_add, ":num_allies_ready_men", 1),
                (else_try),
                  (overlay_set_alpha, ":agent_overlay", 0),
                  (agent_is_wounded, ":cur_agent"),
                  (val_add, ":num_allies_wounded_men", 1),
                (else_try),
                  (agent_is_routed, ":cur_agent"),
                  (val_add, ":num_allies_routed_men", 1),
                (else_try),
                  (val_add, ":num_allies_dead_men", 1),
                (try_end),
              (else_try),
                (try_begin),
                  (agent_is_alive, ":cur_agent"),
                  (call_script, "script_update_agent_position_on_map", ":cur_agent"),
                  (val_add, ":num_enemies_ready_men", 1),
                (else_try),
                  (overlay_set_alpha, ":agent_overlay", 0),
                  (agent_is_wounded, ":cur_agent"),
                  (val_add, ":num_enemies_wounded_men", 1),
                (else_try),
                  (agent_is_routed, ":cur_agent"),
                  (val_add, ":num_enemies_routed_men", 1),
                (else_try),
                  (val_add, ":num_enemies_dead_men", 1),
                (try_end),
              (try_end),
            (try_end),
            
            (assign, reg1, ":num_us_ready_group0"),
            (assign, reg2, ":num_us_ready_group1"),
            (assign, reg3, ":num_us_ready_group2"),
            (assign, reg4, ":num_us_ready_group3"),
            (assign, reg5, ":num_us_ready_group4"),
            (assign, reg6, ":num_us_ready_group5"),
            (assign, reg7, ":num_us_ready_group6"),
            (assign, reg8, ":num_us_ready_group7"),
            (assign, reg9, ":num_us_ready_group8"),
            (assign, reg10, ":num_us_ready_men"),
            (assign, reg11, ":num_us_wounded_men"),
            (assign, reg12, ":num_us_routed_men"),
            (assign, reg13, ":num_us_dead_men"),
            (assign, reg14, ":num_allies_ready_men"),
            (assign, reg15, ":num_allies_wounded_men"),
            (assign, reg16, ":num_allies_routed_men"),
            (assign, reg17, ":num_allies_dead_men"),
            (assign, reg18, ":num_enemies_ready_men"),
            (assign, reg19, ":num_enemies_wounded_men"),
            (assign, reg20, ":num_enemies_routed_men"),
            (assign, reg21, ":num_enemies_dead_men"),
            
            (try_begin),
              (eq, "$group0_has_troops", 1),
              (str_store_class_name, s1, 0),
              (overlay_set_text, "$g_presentation_obj_battle_name0", "str_s1_reg1"),
            (try_end),
            (try_begin),
              (eq, "$group1_has_troops", 1),
              (str_store_class_name, s1, 1),
              (overlay_set_text, "$g_presentation_obj_battle_name1", "str_s1_reg2"),
            (try_end),
            (try_begin),
              (eq, "$group2_has_troops", 1),
              (str_store_class_name, s1, 2),
              (overlay_set_text, "$g_presentation_obj_battle_name2", "str_s1_reg3"),
            (try_end),
            (try_begin),
              (eq, "$group3_has_troops", 1),
              (str_store_class_name, s1, 3),
              (overlay_set_text, "$g_presentation_obj_battle_name3", "str_s1_reg4"),
            (try_end),
            (try_begin),
              (eq, "$group4_has_troops", 1),
              (str_store_class_name, s1, 4),
              (overlay_set_text, "$g_presentation_obj_battle_name4", "str_s1_reg5"),
            (try_end),
            (try_begin),
              (eq, "$group5_has_troops", 1),
              (str_store_class_name, s1, 5),
              (overlay_set_text, "$g_presentation_obj_battle_name5", "str_s1_reg6"),
            (try_end),
            (try_begin),
              (eq, "$group6_has_troops", 1),
              (str_store_class_name, s1, 6),
              (overlay_set_text, "$g_presentation_obj_battle_name6", "str_s1_reg7"),
            (try_end),
            (try_begin),
              (eq, "$group7_has_troops", 1),
              (str_store_class_name, s1, 7),
              (overlay_set_text, "$g_presentation_obj_battle_name7", "str_s1_reg8"),
            (try_end),
            (try_begin),
              (eq, "$group8_has_troops", 1),
              (str_store_class_name, s1, 8),
              (overlay_set_text, "$g_presentation_obj_battle_name8", "str_s1_reg9"),
            (try_end),
            
            (overlay_set_text, "$g_battle_us_ready", "@{!}{reg10}"),
            (overlay_set_text, "$g_battle_us_wounded", "@{!}{reg11}"),
            (overlay_set_text, "$g_battle_us_routed", "@{!}{reg12}"),
            (overlay_set_text, "$g_battle_us_dead", "str_reg13"),
            (overlay_set_text, "$g_battle_allies_ready", "str_reg14"),
            (overlay_set_text, "$g_battle_allies_wounded", "str_reg15"),
            (overlay_set_text, "$g_battle_allies_routed", "str_reg16"),
            (overlay_set_text, "$g_battle_allies_dead", "str_reg17"),
            (overlay_set_text, "$g_battle_enemies_ready", "str_reg18"),
            (overlay_set_text, "$g_battle_enemies_wounded", "str_reg19"),
            (overlay_set_text, "$g_battle_enemies_routed", "str_reg20"),
            (overlay_set_text, "$g_battle_enemies_dead", "str_reg21"),
            
            (assign, ":stat_position_x", 675),
            (assign, ":stat_position_y", 280),
            (val_add, ":stat_position_x", 70),
            (val_add, ":stat_position_y", 60),
            (position_set_x, pos1, ":stat_position_x"),
            (position_set_y, pos1, ":stat_position_y"),
            (overlay_set_position, "$g_battle_us_ready", pos1),
            (val_add, ":stat_position_x", 70),
            (position_set_x, pos1, ":stat_position_x"),
            (overlay_set_position, "$g_battle_us_wounded", pos1),
            (val_add, ":stat_position_x", 70),
            (position_set_x, pos1, ":stat_position_x"),
            (overlay_set_position, "$g_battle_us_routed", pos1),
            (val_add, ":stat_position_x", 70),
            (position_set_x, pos1, ":stat_position_x"),
            (overlay_set_position, "$g_battle_us_dead", pos1),
            (val_add, ":stat_position_x", -210),
            (val_add, ":stat_position_y", -30),
            (position_set_x, pos1, ":stat_position_x"),
            (position_set_y, pos1, ":stat_position_y"),
            (overlay_set_position, "$g_battle_allies_ready", pos1),
            (val_add, ":stat_position_x", 70),
            (position_set_x, pos1, ":stat_position_x"),
            (overlay_set_position, "$g_battle_allies_wounded", pos1),
            (val_add, ":stat_position_x", 70),
            (position_set_x, pos1, ":stat_position_x"),
            (overlay_set_position, "$g_battle_allies_routed", pos1),
            (val_add, ":stat_position_x", 70),
            (position_set_x, pos1, ":stat_position_x"),
            (overlay_set_position, "$g_battle_allies_dead", pos1),
            (val_add, ":stat_position_x", -210),
            (val_add, ":stat_position_y", -30),
            (position_set_x, pos1, ":stat_position_x"),
            (position_set_y, pos1, ":stat_position_y"),
            (overlay_set_position, "$g_battle_enemies_ready", pos1),
            (val_add, ":stat_position_x", 70),
            (position_set_x, pos1, ":stat_position_x"),
            (overlay_set_position, "$g_battle_enemies_wounded", pos1),
            (val_add, ":stat_position_x", 70),
            (position_set_x, pos1, ":stat_position_x"),
            (overlay_set_position, "$g_battle_enemies_routed", pos1),
            (val_add, ":stat_position_x", 70),
            (position_set_x, pos1, ":stat_position_x"),
            (overlay_set_position, "$g_battle_enemies_dead", pos1),
            
            (call_script, "script_update_order_flags_on_map"),
            ## CC
            (try_begin),
              (scene_prop_get_instance, ":player_chest", "spr_inventory", 0),
              (ge, ":player_chest", 0),
              (prop_instance_get_position, pos1, ":player_chest"),
              (call_script, "script_convert_3d_pos_to_map_pos"),
              (overlay_set_position, "$g_presentation_obj_39", pos0),
            (try_end),
            ## CC
        ]),
        
        # script_set_town_picture
        # Input: none
        # Output: none
        ("set_town_picture",
          [
            (try_begin),
              (party_get_current_terrain, ":cur_terrain", "$current_town"),
              (party_slot_eq,"$current_town",slot_party_type, spt_town),
              (try_begin),
                (this_or_next|eq, ":cur_terrain", rt_steppe),
                (this_or_next|eq, ":cur_terrain", rt_steppe_forest),
                (this_or_next|eq, ":cur_terrain", rt_desert),
                (             eq, ":cur_terrain", rt_desert_forest),
                (set_background_mesh, "mesh_pic_towndes"),
              (else_try),
                (this_or_next|eq, ":cur_terrain", rt_snow),
                (             eq, ":cur_terrain", rt_snow_forest),
                (set_background_mesh, "mesh_pic_townsnow"),
              (else_try),
                (set_background_mesh, "mesh_pic_town1"),
              (try_end),
            (else_try),
              (try_begin),
                (this_or_next|eq, ":cur_terrain", rt_steppe),
                (this_or_next|eq, ":cur_terrain", rt_steppe_forest),
                (this_or_next|eq, ":cur_terrain", rt_desert),
                (             eq, ":cur_terrain", rt_desert_forest),
                (set_background_mesh, "mesh_pic_castledes"),
              (else_try),
                (this_or_next|eq, ":cur_terrain", rt_snow),
                (             eq, ":cur_terrain", rt_snow_forest),
                (set_background_mesh, "mesh_pic_castlesnow"),
              (else_try),
                (set_background_mesh, "mesh_pic_castle1"),
              (try_end),
            (try_end),
        ]),
        
        
        # script_consume_food
        # Input: arg1: order of the food to be consumed
        # Output: none
        ("consume_food",
          [(store_script_param, ":selected_food", 1),
            (troop_get_inventory_capacity, ":capacity", "trp_player"),
            (try_for_range, ":cur_slot", 0, ":capacity"),
              (troop_get_inventory_slot, ":cur_item", "trp_player", ":cur_slot"),
              (is_between, ":cur_item", food_begin, food_end),
              (troop_get_inventory_slot_modifier, ":item_modifier", "trp_player", ":cur_slot"),
              (neq, ":item_modifier", imod_rotten),
              (item_slot_eq, ":cur_item", slot_item_is_checked, 0),
              (item_set_slot, ":cur_item", slot_item_is_checked, 1),
              (val_sub, ":selected_food", 1),
              (lt, ":selected_food", 0),
              (assign, ":capacity", 0),
              (troop_inventory_slot_get_item_amount, ":cur_amount", "trp_player", ":cur_slot"),
              ## CC
              (store_add, ":food_consum_multi", "$g_twice_consum_food", 1),
              (val_sub, ":cur_amount", ":food_consum_multi"),
              (val_max, ":cur_amount", 0),
              ## CC
              (troop_inventory_slot_set_item_amount, "trp_player", ":cur_slot", ":cur_amount"),
            (try_end),
        ]),
        
        
        
        # script_calculate_troop_score_for_center
        # Input: arg1 = troop_no, arg2 = center_no
        # Output: reg0 = score
        ("calculate_troop_score_for_center",
          [(store_script_param, ":troop_no", 1),
            (store_script_param, ":center_no", 2),
            (assign, ":num_center_points", 1),
            (try_for_range, ":cur_center", centers_begin, centers_end),
              (assign, ":center_owned", 0),
              (try_begin),
                (eq, ":troop_no", "trp_player"),
                (party_slot_eq, ":cur_center", slot_town_lord, stl_reserved_for_player),
                (assign, ":center_owned", 1),
              (try_end),
              (this_or_next|party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
              (eq, ":center_owned", 1),
              (try_begin),
                (party_slot_eq, ":cur_center", slot_party_type, spt_town),
                (val_add, ":num_center_points", 4),
              (else_try),
                (party_slot_eq, ":cur_center", slot_party_type, spt_castle),
                (val_add, ":num_center_points", 2),
              (else_try),
                (val_add, ":num_center_points", 1),
              (try_end),
            (try_end),
            (troop_get_slot, ":troop_renown", ":troop_no", slot_troop_renown),
            (store_add, ":score", 500, ":troop_renown"),
            (val_div, ":score", ":num_center_points"),
            (store_random_in_range, ":random", 50, 100),
            (val_mul, ":score", ":random"),
            (try_begin),
              (party_slot_eq, ":center_no", slot_center_last_taken_by_troop, ":troop_no"),
              (val_mul, ":score", 3),
			  (val_div, ":score", 2),
			##diplomacy start+
			#Take into account original/most-recent lord and home slots.
			#Fief allocations during rebellions are an example of when this would apply.
			(else_try),
			#Bonus for original owner
				(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
				(party_slot_ge, ":center_no", dplmc_slot_center_original_lord, 1),
				(party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":troop_no"),
				(val_mul, ":score", 3),
				(val_div, ":score", 2),
			(else_try),
			#Bonus for previous owner
				(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
				(party_slot_ge, ":center_no", dplmc_slot_center_ex_lord, 1),
				(party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":troop_no"),
				(val_mul, ":score", 3),
				(val_div, ":score", 2),
			(else_try),
			#Bonus for lord claiming the center as home
				(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
				(troop_slot_eq, ":troop_no", slot_troop_home, ":center_no"),
				(val_mul, ":score", 3),
				(val_div, ":score", 2),
			##diplomacy end+
			(try_end),
			(try_begin),
			  (eq, ":troop_no", "trp_player"),
			   ##diplomacy start+ xxx Replaced next line (slot 0 is not the faction leader slot):
			  #(faction_get_slot, ":faction_leader", "$players_kingdom"),
			  (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
			  ##diplomacy end+
			  (call_script, "script_troop_get_player_relation", ":faction_leader"),
			  (assign, ":leader_relation", reg0),
			  #(troop_get_slot, ":leader_relation", ":faction_leader", slot_troop_player_relation),
			  (val_mul, ":leader_relation", 2),
			  (val_add, ":score", ":leader_relation"),
			(try_end),
			(assign, reg0, ":score"),
			]),
        
        
        # script_assign_lords_to_empty_centers
        # Input: none
        # Output: none
        #Now ONLY called from the start
        ("assign_lords_to_empty_centers",
          [
            
            (try_begin),
              (eq, "$cheat_mode", 1),
              (display_message, "str_assigning_lords_to_empty_centers"),
              (str_store_string, s65, "str_assign_lords_to_empty_centers_just_happened"),
              (call_script, "script_add_notification_menu", "mnu_debug_alert_from_s65", 0, 0),
            (try_end),
            
            (try_for_range, ":faction", kingdoms_begin, kingdoms_end),
              (faction_set_slot, ":faction", slot_faction_temp_slot, 0),
            (try_end),
            
            (try_for_range, ":active_npc", 0, active_npcs_end),
              (troop_set_slot, ":active_npc", slot_troop_temp_slot, 0),
            (try_end),
            
            #Factions will keep one unassigned center in reserve, unless they have landless lords
            (try_for_range, ":cur_center", centers_begin, centers_end),
              (party_get_slot, ":center_lord", ":cur_center", slot_town_lord),
              (try_begin),
                (this_or_next|eq, ":center_lord", stl_unassigned),
                (eq, ":center_lord", stl_rejected_by_player),
                (store_faction_of_party, ":center_faction", ":cur_center"),
                
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (str_store_party_name, s4, ":cur_center"),
                  (str_store_faction_name, s5, ":center_faction"),
                  (display_message, "str_s4_of_the_s5_is_unassigned"),
                (try_end),
                
                (faction_get_slot, ":number_of_unassigned_centers_plus_landless_lords", ":center_faction", slot_faction_temp_slot),
                (val_add, ":number_of_unassigned_centers_plus_landless_lords", 1),
                (faction_set_slot,  ":center_faction", slot_faction_temp_slot, ":number_of_unassigned_centers_plus_landless_lords"),
              (else_try),
                (eq, ":center_lord", stl_reserved_for_player),
                
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (str_store_party_name, s4, ":cur_center"),
                  (str_store_faction_name, s5, ":center_faction"),
                  (display_message, "str_s4_of_the_s5_is_reserved_for_player"),
                (try_end),
                
              (else_try),
                (ge, ":center_lord", 0),
                (troop_set_slot, ":center_lord", slot_troop_temp_slot, 1),
              (try_end),
            (try_end),
            
            (try_for_range, ":active_npc", 0, active_npcs_end),
              (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
              (this_or_next|gt, ":active_npc", "trp_player"),
              (eq, "$player_has_homage", 1),
              
              (troop_slot_eq, ":active_npc", slot_troop_temp_slot, 0),
              (store_faction_of_troop, ":npc_faction", ":active_npc"),
              
              (is_between, ":npc_faction", npc_kingdoms_begin, npc_kingdoms_end),
              
              (try_begin),
                (eq, "$cheat_mode", 1),
                (str_store_troop_name, s4, ":active_npc"),
                (str_store_faction_name, s5, ":npc_faction"),
                (display_message, "str_s4_of_the_s5_has_no_fiefs"),
              (try_end),
              
              (faction_get_slot, ":number_of_unassigned_centers_plus_landless_lords", ":npc_faction", slot_faction_temp_slot),
              (val_add, ":number_of_unassigned_centers_plus_landless_lords", 1),
              (faction_set_slot,  ":npc_faction", slot_faction_temp_slot, ":number_of_unassigned_centers_plus_landless_lords"),
            (try_end),
            
            (try_begin),
              (eq, "$cheat_mode", 1),
              (try_for_range, ":faction", kingdoms_begin, kingdoms_end),
                (faction_get_slot, reg4, ":faction", slot_faction_temp_slot),
                (str_store_faction_name, s4, ":faction"),
                (display_message, "str_s4_unassigned_centers_plus_landless_lords_=_reg4"),
              (try_end),
            (try_end),
            
            (try_for_range, ":cur_center", centers_begin, centers_end),
              (party_get_slot, ":center_lord", ":cur_center", slot_town_lord),
              (this_or_next|eq, ":center_lord", stl_unassigned),
              (eq, ":center_lord", stl_rejected_by_player),
              
              (store_faction_of_party, ":center_faction", ":cur_center"),
              (is_between, ":center_faction", kingdoms_begin, kingdoms_end),
              (neg|faction_slot_eq, ":center_faction", slot_faction_leader, "trp_player"),
              
              (try_begin),
                (eq, "$cheat_mode", 1),
                (str_store_party_name, s5, ":cur_center"),
                (try_begin),
                  (neg|faction_slot_ge, ":center_faction", slot_faction_temp_slot, 2),
                  (str_store_faction_name, s4, ":center_faction"),
                  (display_message, "str_s4_holds_s5_in_reserve"),
                (try_end),
              (try_end),
              
              (faction_slot_ge, ":center_faction", slot_faction_temp_slot, 2),
              
              #(display_message, "@Considering grant of {s5}"),
              
              (assign, ":best_lord", -1),
              (assign, ":best_lord_score", -1),
              (try_begin),
                (eq, ":center_lord", stl_unassigned),
                (try_begin),
                  (eq, "$players_kingdom", ":center_faction"),
                  (eq, "$player_has_homage", 1),
                  (assign, ":best_lord", stl_reserved_for_player),
                  (call_script, "script_calculate_troop_score_for_center", "trp_player", ":cur_center"),
                  (assign, ":best_lord_score", reg0),
                (try_end),
              (try_end),
              
              (try_for_range, ":cur_troop", active_npcs_begin, active_npcs_end),
                (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
                (store_troop_faction, ":troop_faction", ":cur_troop"),
                (eq, ":troop_faction", ":center_faction"),
                
                (call_script, "script_calculate_troop_score_for_center", ":cur_troop", ":cur_center"),
                (assign, ":score", reg0),
                
                #This prioritizes granting of centers for troops which do not already have one
                (try_begin),
                  (troop_slot_eq, ":cur_troop", slot_troop_temp_slot, 0),
                  (is_between, ":cur_center", villages_begin, villages_end),
                  (val_mul, ":score", 10),
                (try_end),
                
                (gt, ":score", ":best_lord_score"),
                (assign, ":best_lord_score", ":score"),
                (assign, ":best_lord", ":cur_troop"),
              (try_end),
              
              #Adjust count of centers and lords
              (try_begin),
                (this_or_next|ge, ":best_lord", 0),
                (eq, ":best_lord", stl_reserved_for_player),
                
                (faction_get_slot, ":landless_lords_plus_unassigned_centers", ":center_faction", slot_faction_temp_slot),
                (val_sub, ":landless_lords_plus_unassigned_centers", 1),
                
                (try_begin),
                  (eq, ":best_lord", stl_reserved_for_player),
                  (troop_slot_eq, "trp_player", slot_troop_temp_slot, 0),
                  (troop_set_slot, "trp_player", slot_troop_temp_slot, 1),
                  (val_sub, ":landless_lords_plus_unassigned_centers", 1),
                (else_try),
                  (troop_slot_eq, ":best_lord", slot_troop_temp_slot, 0),
                  (troop_set_slot, ":best_lord", slot_troop_temp_slot, 1),
                  (val_sub, ":landless_lords_plus_unassigned_centers", 1),
                (try_end),
                
                (faction_set_slot, ":center_faction", slot_faction_temp_slot, ":landless_lords_plus_unassigned_centers"),
              (try_end),
              
              #Give the center to the lord
              (try_begin),
                (ge, ":best_lord", 0),
                (call_script, "script_give_center_to_lord", ":cur_center", ":best_lord", 1),
              (else_try),
                (eq, ":best_lord", stl_reserved_for_player),
                (party_set_slot, ":cur_center", slot_town_lord, stl_reserved_for_player),
                (try_begin), #grant bound villages to player, if granting a castle
                  (party_slot_eq, ":cur_center", slot_party_type, spt_castle),
                  #				(assign, ":give_at_least_one_village", 0),
                  (try_for_range, ":cur_village", villages_begin, villages_end),
                    #					(eq, ":give_at_least_one_village", 0),
                    (party_slot_eq, ":cur_village", slot_village_bound_center, ":cur_center"),
                    (party_slot_eq, ":cur_village", slot_town_lord, stl_unassigned),
                    (party_set_slot, ":cur_village", slot_town_lord, stl_reserved_for_player),
                    #					(assign, ":give_at_least_one_village", 1),
                  (try_end),
                (try_end),
              (try_end),
            (try_end),
        ]),
        
        
        # script_create_village_farmer_party
        # Input: arg1 = village_no
        # Output: reg0 = party_no
        ("create_village_farmer_party",
          [(store_script_param, ":village_no", 1),
            (party_get_slot, ":town_no", ":village_no", slot_village_market_town),
            (store_faction_of_party, ":party_faction", ":town_no"),
            
            
            #    (store_faction_of_party, ":town_faction", ":town_no"),
            #    (try_begin),
            #		(neq, ":town_faction", ":party_faction"),
            #		(assign, ":town_no", -1),
            #		(assign, ":score_to_beat", 9999),
            #		(try_for_range, ":other_town", towns_begin, towns_end),
            #			(store_faction_of_party, ":other_town_faction", ":town_no"),
            #			(store_relation, ":relation", ":other_town_faction", ":party_faction"),
            #			(ge, ":relation", 0),
            
            #			(store_distance_to_party_from_party, ":distance", ":village_no", ":other_town"),
            #			(lt, ":distance", ":score_to_beat"),
            #			(assign, ":town_no", ":other_town"),
            #			(assign, ":score_to_beat", ":distance"),
            #		(try_end),
            #	(try_end),
            
            (try_begin),
              (is_between, ":town_no", towns_begin, towns_end),
              (set_spawn_radius, 0),
				##Floris MTT begin
				(try_begin),
		 			(eq, "$troop_trees", troop_trees_0),
					(spawn_around_party, ":village_no", "pt_village_farmers"),
				(else_try),
		 			(eq, "$troop_trees", troop_trees_1),
					(spawn_around_party, ":village_no", "pt_village_farmers_r"),
				(else_try),
					(eq, "$troop_trees", troop_trees_2),
					(spawn_around_party, ":village_no", "pt_village_farmers_e"),
				(try_end),
				##Floris MTT end
              (assign, ":new_party", reg0),
              
              (party_set_faction, ":new_party", ":party_faction"),
              (party_set_slot, ":new_party", slot_party_home_center, ":village_no"),
              (party_set_slot, ":new_party", slot_party_last_traded_center, ":village_no"),
              
              (party_set_slot, ":new_party", slot_party_type, spt_village_farmer),
              (party_set_slot, ":new_party", slot_party_ai_state, spai_trading_with_town),
              (party_set_slot, ":new_party", slot_party_ai_object, ":town_no"),
              (party_set_ai_behavior, ":new_party", ai_bhvr_travel_to_party),
              (party_set_ai_object, ":new_party", ":town_no"),
              (party_set_flags, ":new_party", pf_default_behavior, 0),
              (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
              (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
                (store_add, ":cur_good_price_slot", ":cur_goods", ":item_to_price_slot"),
                (party_get_slot, ":cur_village_price", ":village_no", ":cur_good_price_slot"),
                (party_set_slot, ":new_party", ":cur_good_price_slot", ":cur_village_price"),
              (try_end),
              (assign, reg0, ":new_party"),
            (try_end),
            
        ]),
        
        #script_do_party_center_trade
        # INPUT: arg1 = party_no, arg2 = center_no, arg3 = percentage_change_in_center
        # OUTPUT: reg0 = total_change
        ("do_party_center_trade",
          [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":center_no", 2),

			(try_begin),																											#	1.143 Port // Newly Added and altered, see native 1.134
				(eq, "$cheat_mode", 3),
				(str_store_party_name, s1, ":center_no"),
				(display_message, "@{!}DEBUG : {s1} is trading with villagers"),
			(try_end),

			(store_script_param, ":percentage_change", 3), #this should probably always be a constant. Currently it is 25.			#	End
            
            (party_get_slot, ":origin", ":party_no", slot_party_last_traded_center),
            (party_set_slot, ":party_no", slot_party_last_traded_center, ":center_no"),
            
			(assign, ":percentage_change", 30),
		  ##diplomacy start+
		  (party_get_slot, ":origin", ":party_no", slot_party_last_traded_center),
		  #If optional economic changes are enabled, reduce the percentage change in order
		  #to make prices feel less static.
		  (try_begin),
			(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
			#Only apply lessened price movements to towns.
			(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
				(is_between, ":center_no", towns_begin, towns_end),
			#This halves the average impact as well as making it more variable.
			(val_add, ":percentage_change", 1),
			(store_random_in_range, ":percentage_change", 0, ":percentage_change"),
			#Display economics diagnostic
			(ge, "$cheat_mode", 3),
			(str_store_party_name, s3, ":origin"),
			(str_store_party_name, s4, ":center_no"),
			(assign, reg4, ":percentage_change"),
			(display_message, "@{!}DEBUG -- Trade from {s3} to {s4}: rolled random impact of {reg4}"),
		  (try_end),
		  ##diplomacy end+

		  (party_get_slot, ":origin", ":party_no", slot_party_last_traded_center),
		  (party_set_slot, ":party_no", slot_party_last_traded_center, ":center_no"),
		  ##diplomacy start+
		  #Update the record of trade route arrival times
		  (try_begin),
			 (ge, ":origin", centers_begin),
			 ##zerilius changes begin
			 # (this_or_next|party_slot_eq, ":origin", villages_begin, villages_end),
			 (this_or_next|party_slot_eq, ":origin", slot_party_type, spt_village),
			 ##zerilius changes end
			 (is_between, ":origin", villages_begin, villages_end),
			 (store_current_hours, ":cur_hours"),
			 (party_set_slot, ":origin", dplmc_slot_village_trade_last_arrived_to_market, ":cur_hours"),
		  (try_end),
		  (try_begin),
			 (ge, ":origin", centers_begin),
			 (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
				(is_between, ":center_no", towns_begin, towns_end),
			 (store_current_hours, ":cur_hours"),
			 (try_for_range, ":trade_route_slot", slot_town_trade_routes_begin, slot_town_trade_routes_end),
				(party_slot_eq,  ":center_no", ":trade_route_slot", ":origin"),
				(store_sub, ":trade_route_arrival_slot", ":trade_route_slot", slot_town_trade_routes_begin),
				(val_add, ":trade_route_arrival_slot", dplmc_slot_town_trade_route_last_arrivals_begin),
				(is_between, ":trade_route_arrival_slot", dplmc_slot_town_trade_route_last_arrivals_begin, dplmc_slot_town_trade_route_last_arrivals_end),#this will always be true unless a modder increased the number of trade route slots without increasing the number of last arrival slots
				(party_set_slot, ":center_no", ":trade_route_arrival_slot", ":cur_hours"),
			 (try_end),
			 (else_try),
				(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_village),
				   (is_between, ":center_no", villages_begin, villages_end),
			 (store_current_hours, ":cur_hours"),
			 (party_set_slot, ":center_no", dplmc_slot_village_trade_last_returned_from_market, ":cur_hours"),
		  (try_end),
		  ##diplomacy end+
			
            (assign, ":total_change", 0),
            (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
            (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
              (store_add, ":cur_good_price_slot", ":cur_good", ":item_to_price_slot"),
              (party_get_slot, ":cur_merchant_price", ":party_no", ":cur_good_price_slot"),
              (party_get_slot, ":cur_center_price", ":center_no", ":cur_good_price_slot"),
              (store_sub, ":price_dif", ":cur_merchant_price", ":cur_center_price"),
              (assign, ":cur_change", ":price_dif"),
              (val_abs, ":cur_change"),
              (val_add, ":total_change", ":cur_change"),
              (val_mul, ":cur_change", ":percentage_change"),
              (val_div, ":cur_change", 100),
              
              #This is to reconvert from absolute value
              (try_begin),
                (lt, ":price_dif", 0),
                (val_mul, ":cur_change", -1),
              (try_end),
              
			  (assign, ":initial_price", ":cur_center_price"),					#	1.143 Port // Added line
			  
              #The new price for the caravan or peasant is set before the change, so the prices in the trading town have full effect on the next center
              (party_set_slot, ":party_no", ":cur_good_price_slot", ":cur_center_price"),
              
              (val_add, ":cur_center_price", ":cur_change"),
              (party_set_slot, ":center_no", ":cur_good_price_slot", ":cur_center_price"),
              
              (try_begin),
                (eq, "$cheat_mode", 3),
                (str_store_party_name, s3, ":origin"),
                (str_store_party_name, s4, ":center_no"),
                (str_store_item_name, s5, ":cur_good"),
				(assign, reg4, ":initial_price"),																				#	1.143 Port // Couple changes, see native 1.134
				(assign, reg5, ":cur_center_price"),
				(display_log_message, "@{!}DEBUG -- Trade of {s5} from {s3} to {s4} brings price from {reg4} to {reg5}"),		#	End
              (try_end),
              
            (try_end),
            (assign, reg0, ":total_change"),
        ]),
        
        #script_player_join_faction
        # INPUT: arg1 = faction_no
        # OUTPUT: none
        ("player_join_faction",
          [
            (store_script_param, ":faction_no", 1),
            (assign,"$players_kingdom",":faction_no"),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_ai_state, sfai_default),
            (assign, "$players_oath_renounced_against_kingdom", 0),
            (assign, "$players_oath_renounced_given_center", 0),
            (assign, "$players_oath_renounced_begin_time", 0),
            
            (try_for_range,":other_kingdom",kingdoms_begin,kingdoms_end),
              (faction_slot_eq, ":other_kingdom", slot_faction_state, sfs_active),
              (neq, ":other_kingdom", "fac_player_supporters_faction"),
              (try_begin),
                (neq, ":other_kingdom", ":faction_no"),
                (store_relation, ":other_kingdom_reln", ":other_kingdom", ":faction_no"),
              (else_try),
                (store_relation, ":other_kingdom_reln", "fac_player_supporters_faction", ":other_kingdom"),
                (val_max, ":other_kingdom_reln", 12),
              (try_end),
              (call_script, "script_set_player_relation_with_faction", ":other_kingdom", ":other_kingdom_reln"),
            (try_end),
            
            (try_for_range, ":cur_center", centers_begin, centers_end),
              #Give center to kingdom if player is the owner
              (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
              (call_script, "script_give_center_to_faction_while_maintaining_lord", ":cur_center", ":faction_no"),
            (else_try),
              #Give center to kingdom if part of player faction
              (store_faction_of_party, ":cur_center_faction", ":cur_center"),
              (eq, ":cur_center_faction", "fac_player_supporters_faction"),
              (call_script, "script_give_center_to_faction_while_maintaining_lord", ":cur_center", ":faction_no"),
            (try_end),
            
            (try_for_range, ":quest_no", lord_quests_begin, lord_quests_end),
              (check_quest_active, ":quest_no"),
              (quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
              (store_troop_faction, ":quest_giver_faction", ":quest_giver_troop"),
              (store_relation, ":quest_giver_faction_relation", "fac_player_supporters_faction", ":quest_giver_faction"),
              (lt, ":quest_giver_faction_relation", 0),
              (call_script, "script_abort_quest", ":quest_no", 0),
            (try_end),
            (try_for_range, ":quest_no", lord_quests_begin_2, lord_quests_end_2),
              (check_quest_active, ":quest_no"),
              (quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
              (store_troop_faction, ":quest_giver_faction", ":quest_giver_troop"),
              (store_relation, ":quest_giver_faction_relation", "fac_player_supporters_faction", ":quest_giver_faction"),
              (lt, ":quest_giver_faction_relation", 0),
              (call_script, "script_abort_quest", ":quest_no", 0),
            (try_end),
            (try_begin),
              (neq, ":faction_no", "fac_player_supporters_faction"),
              (faction_set_slot, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
              (faction_set_slot, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
            (try_end),
            
            (try_begin),
              (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
              (is_between, ":spouse", kingdom_ladies_begin, kingdom_ladies_end),
              ## Start 1.134
              (try_begin),
                (ge, "$cheat_mode", 1),
                (str_store_troop_name, s4, ":spouse"),
                (display_message, "@{!}DEBUG - {s4} faction changed by marriage, case 1"),
              (try_end),
              ## End 1.134
              (troop_set_faction, ":spouse", "$players_kingdom"),
              #LAZERAS MODIFIED  {ENTK}
              # Jrider + TITLES v 0.3.1 change spouse title according to new faction
              (call_script, "script_troop_set_title_according_to_faction", ":spouse", "$players_kingdom"),
              # Jrider -
              #LAZERAS MODIFIED  {ENTK}
            (try_end),
			##diplomacy start+
		  #Make other vassals follow the player.
		  ##(There are other possibilities that we might want to explore, but
		  ##what happens now is that they remain members of the defunct faction.)
		  (try_begin),
			(neq, ":faction_no", "fac_player_supporters_faction"),
			  (try_for_range, ":troop_no", heroes_begin, heroes_end),
				 (store_troop_faction, ":other_troop_faction", ":troop_no"),
				 (eq, ":other_troop_faction", "fac_player_supporters_faction"),
				 
				 (this_or_next|neg|is_between, ":troop_no", companions_begin, companions_end),
				 (this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
				 (this_or_next|troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
					(troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_lord_rejoined),
				 (this_or_next|neq, ":troop_no", ":spouse"),
					(neg|is_between, ":spouse", kingdom_ladies_begin, kingdom_ladies_end),
				(try_begin),
					(ge, "$cheat_mode", 1),
					(str_store_troop_name, s4, ":troop_no"),
					(display_message, "@{!} DEBUG - {s4} changed by player's defection"),
				(try_end),
				(troop_set_faction, ":troop_no", "$players_kingdom"),
				#Clear troop slots
				(troop_set_slot, ":troop_no", slot_troop_stance_on_faction_issue, -1),
				(troop_set_slot, ":troop_no", slot_troop_recruitment_random, 0),
				(troop_set_slot, ":troop_no", slot_lord_recruitment_argument, 0),
				(troop_set_slot, ":troop_no", slot_lord_recruitment_candidate, 0),
				(troop_set_slot, ":troop_no", slot_troop_promised_fief, 0),
				#Give new title
				(try_begin),
					(this_or_next|neg|is_between,":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
						(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
					(call_script, "script_troop_set_title_according_to_faction", ":troop_no", ":faction_no"),
				(try_end),
				#Change led party
				(try_begin),
					(troop_get_slot, ":troop_leaded_party", ":troop_no", slot_troop_leaded_party),
					(gt, ":troop_leaded_party", 0),
					(party_is_active, ":troop_leaded_party"),
					(party_set_faction, ":troop_leaded_party", ":faction_no"),
				(try_end),
			  (try_end),
		  (try_end),
		  ##diplomacy end+
            
            (try_for_range, ":center", centers_begin, centers_end),
              (store_faction_of_party, ":center_faction", ":faction_no"),
              (neq, ":center_faction", "$players_kingdom"),
              (party_slot_eq, ":center", slot_town_lord, stl_reserved_for_player),
              #		(party_set_slot, ":center", slot_town_lord, stl_unassigned),
            (try_end),
            
            (troop_set_slot, "trp_player", slot_troop_stance_on_faction_issue, -1),
            
            #remove prisoners of player's faction if he was member of his own faction. And free companions which is prisoned in that faction.
            (try_for_parties, ":party_no"),
              (store_faction_of_party, ":party_faction", ":party_no"),
              (eq, ":party_faction", ":faction_no"),
              
              (party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
              (try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
                (party_prisoner_stack_get_troop_id, ":cur_troop_id", ":party_no", ":troop_iterator"),
                (store_troop_faction, ":cur_faction", ":cur_troop_id"),
                
                (this_or_next|eq, ":cur_faction", "fac_player_supporters_faction"),
                (this_or_next|eq, ":cur_faction", ":faction_no"),
                (is_between, ":cur_troop_id", companions_begin, companions_end),
                
                (try_begin),
                  (troop_is_hero, ":cur_troop_id"),
                  (call_script, "script_remove_troop_from_prison", ":cur_troop_id"),
                (try_end),
                
                (party_prisoner_stack_get_size, ":stack_size", ":party_no", ":troop_iterator"),
                (party_remove_prisoners, ":party_no", ":cur_troop_id", ":stack_size"),
                
                (try_begin),
                  (is_between, ":cur_troop_id", companions_begin, companions_end),
                  
                  (try_begin),
                    (is_between, ":party_no", towns_begin, towns_end),
                    (troop_set_slot, ":cur_troop_id", slot_troop_cur_center, ":party_no"),
                  (else_try),
                    (store_random_in_range, ":random_town_no", towns_begin, towns_end),
                    (troop_set_slot, ":cur_troop_id", slot_troop_cur_center, ":random_town_no"),
                  (try_end),
                (try_end),
              (try_end),
            (try_end),
            #remove prisoners end.
            
            #(call_script, "script_store_average_center_value_per_faction"),
            #LAZERAS MODIFIED  {ENTK}
            # Jrider + TITLES v 0.3.1 set player new title
            (call_script, "script_troop_set_title_according_to_faction", "trp_player", "$players_kingdom"),
            # Jrider -
            #LAZERAS MODIFIED  {ENTK}
            (call_script, "script_update_all_notes"),
            (assign, "$g_recalculate_ais", 1),
        ]),
        
        #script_player_leave_faction
        # INPUT: arg1 = give_back_fiefs
        # OUTPUT: none
        ("player_leave_faction",
          [
            (store_script_param, ":give_back_fiefs", 1),
            
            (call_script, "script_check_and_finish_active_army_quests_for_faction", "$players_kingdom"),
            (assign, ":old_kingdom", "$players_kingdom"),
            (assign, ":old_has_homage", "$player_has_homage"),
            (assign, "$players_kingdom", 0),
            (assign, "$player_has_homage", 0),
            
            (try_begin),
              (neq, ":give_back_fiefs", 0), #ie, give back fiefs = 1, thereby do it
              (try_for_range, ":cur_center", centers_begin, centers_end),
                (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
                ##diplomacy begin
                #native bug fix when giving back fiefs
                (call_script, "script_give_center_to_faction", ":cur_center", "fac_neutral"),
                ##diplomacy end
                (call_script, "script_give_center_to_faction", ":cur_center", ":old_kingdom"),
                
                #The following line also occurs when a lord is stripped of his fiefs by an indictment
                (party_set_slot, ":cur_center", slot_town_lord, stl_unassigned),
              (try_end),
            (else_try),
              #If you retain the fiefs
              (try_for_range, ":cur_center", centers_begin, centers_end),
                (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
                (call_script, "script_give_center_to_faction", ":cur_center", "fac_player_supporters_faction"),
                (party_set_slot, ":cur_center", slot_town_lord, "trp_player"),
                (troop_get_slot, ":cur_banner", "trp_player", slot_troop_banner_scene_prop),
                (gt, ":cur_banner", 0),
                (val_sub, ":cur_banner", banner_scene_props_begin),
                (val_add, ":cur_banner", banner_map_icons_begin),
                (party_set_banner_icon, ":cur_center", ":cur_banner"),
              (try_end),
              
              (try_for_range, ":cur_center", villages_begin, villages_end),
                (party_get_slot, ":cur_bound_center", ":cur_center", slot_village_bound_center),
                (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
                (neg|party_slot_eq, ":cur_bound_center", slot_town_lord, "trp_player"),
                (call_script, "script_give_center_to_faction", ":cur_center", ":old_kingdom"),
              (try_end),
              
              (is_between, ":old_kingdom", kingdoms_begin, kingdoms_end),
              (neq, ":old_kingdom", "fac_player_supporters_faction"),
              (store_relation, ":reln", "fac_player_supporters_faction", ":old_kingdom"),
              (store_sub, ":req_dif", -40, ":reln"),
              (call_script, "script_change_player_relation_with_faction", ":old_kingdom", ":req_dif"),
            (try_end),
            
            (try_begin),
              (eq, ":old_has_homage", 1),
              (faction_get_slot, ":faction_leader", ":old_kingdom", slot_faction_leader),
              (call_script, "script_change_player_relation_with_troop", ":faction_leader", -20),
            (try_end),
            
            (try_begin),
              (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
              (is_between, ":spouse", kingdom_ladies_begin, kingdom_ladies_end),
              ##Begin 1.134
              (try_begin),
                (ge, "$cheat_mode", 1),
                (str_store_troop_name, s4, ":spouse"),
                (display_message, "@{!}DEBUG - {s4} faction changed by marriage, case 3"),
              (try_end),
              ##End 1.134
              (troop_set_faction, ":spouse", "fac_player_supporters_faction"),#LAZERAS MODIFIED  {ENTK}
              # Jrider + TITLES v 0.3.1 change spouse title according to new faction
              (call_script, "script_troop_set_title_according_to_faction", ":spouse", "fac_player_supporters_faction"),
              # Jrider -
              #LAZERAS MODIFIED  {ENTK}
            (try_end),
            
            #Change relations with players_kingdom when player changes factions
            (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
              (neq, ":kingdom", "fac_player_supporters_faction"),
              (store_relation, ":relation_with_old_faction", ":old_kingdom", ":kingdom"),
              (store_relation, ":relation_with_player_faction", "fac_player_faction", ":kingdom"),
              
			(try_begin),
			  (eq, ":old_kingdom", ":kingdom"),
			  (val_min, ":relation_with_player_faction", 0),
			(else_try),
			  (lt, ":relation_with_old_faction", 0),
			  (val_max, ":relation_with_player_faction", 0),
		   ##diplomacy start+ do not retain allies of former kingdom
		   (else_try),
			 (gt, ":relation_with_old_faction", 0),
			 (val_min, ":relation_with_player_faction", 0),
		   ##diplomacy end+
			(try_end),
			(set_relation, "fac_player_faction", ":kingdom", ":relation_with_player_faction"),
			(set_relation, "fac_player_supporters_faction", ":kingdom", ":relation_with_player_faction"),
		  (try_end),
            
            #LAZERAS MODIFIED  {ENTK}
            # Jrider + TITLES v 0.3.1 set player new title
            (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", "trp_player", "fac_player_supporters_faction"),
            # Jrider -
            #LAZERAS MODIFIED  {ENTK}
            
            (call_script, "script_update_all_notes"),
            (assign, "$g_recalculate_ais", 1),
            
            ##diplomacy 3.3.2 begin
            ##disband player patrols
            (try_for_parties, ":party_no"),
              (party_slot_eq,":party_no", slot_party_type, spt_patrol),
              (party_slot_eq, ":party_no", dplmc_slot_party_mission_diplomacy, "trp_player"),
              (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),
              (str_store_party_name, s6, ":target_party"),
              (display_log_message, "@Your soldiers patrolling {s6} disbanded because you abandoned your faction!", 0xFF0000),
              (remove_party, ":party_no"),
            (try_end),
            ##diplomacy 3.3.2 end
        ]),
        
        
        ("deactivate_player_faction",
          [
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
            (assign, "$players_kingdom", 0),
            (assign, "$players_oath_renounced_against_kingdom", 0),
            (assign, "$players_oath_renounced_given_center", 0),
            (assign, "$players_oath_renounced_begin_time", 0),
            #(call_script, "script_store_average_center_value_per_faction"),
            (call_script, "script_update_all_notes"),
            
            (try_begin),
              (is_between, "$g_player_minister", companions_begin, companions_end),
              (assign, "$npc_to_rejoin_party", "$g_player_minister"),
            (try_end),
            (assign, "$g_player_minister", -1),
            
            (call_script, "script_add_notification_menu", "mnu_notification_player_faction_deactive", 0, 0),
        ]),
        
        
        #script_activate_player_faction
        # INPUT: arg1 = last_interaction_with_faction
        # OUTPUT: none
        
        #When a player convinces her husband to rebel
        #When a player proclaims herself queen
        #When a player seizes control of a center
        #When a player recruits a lord through intrigue
        #When a player
        ("activate_player_faction",
          [
            (store_script_param, ":liege", 1),
            
            #This moved to top, so that mnu_notification does not occur twice
            (try_begin),
              (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
              (neg|is_between, ":liege", pretenders_begin, pretenders_end),
              (call_script, "script_add_notification_menu", "mnu_notification_player_faction_active", 0, 0),
              ##diplomacy begin
              (call_script, "script_add_notification_menu", "mnu_dplmc_domestic_policy", 0, 0),
              ##diplomacy end
            (try_end),
            
            
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_state, sfs_active),
            (faction_set_slot, "fac_player_supporters_faction", slot_faction_leader, ":liege"),
            
            (assign, ":original_kingdom", "$players_kingdom"),
            
            (try_begin),
              (is_between, ":original_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
              (call_script, "script_player_leave_faction", 0), #Ends quests, transfers control of centers
            (try_end),
            
            #Name faction
            (try_begin),
              (is_between, ":liege", active_npcs_begin, active_npcs_end),
              (store_faction_of_troop, ":liege_faction"),
              (is_between, ":liege_faction", npc_kingdoms_begin, npc_kingdoms_end),
              (faction_get_slot, ":adjective_string", ":liege_faction", slot_faction_adjective),
              (str_store_string, s1, ":adjective_string"),
              (faction_set_name, "fac_player_supporters_faction", "@{s1} Rebels"),
            (else_try),
              (str_store_troop_name, s2, ":liege"),
              (str_store_string, s1, "str_s2s_rebellion"),
            (try_end),
            (faction_set_color, "fac_player_supporters_faction", 0xFF0000),
            
            (assign, "$players_kingdom", "fac_player_supporters_faction"),
            (assign, "$g_player_banner_granted", 1),
            
            
            
            #Any oaths renounced?
            (try_begin),
              (is_between, ":original_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
              
              (faction_get_slot, ":old_leader", ":original_kingdom", slot_faction_leader),
              (call_script, "script_add_log_entry", logent_renounced_allegiance,   "trp_player",  -1, ":old_leader", "$players_kingdom"),
              
              #Initializing renounce war variables
              (assign, "$players_oath_renounced_against_kingdom", ":original_kingdom"),
              (assign, "$players_oath_renounced_given_center", 0),
              (store_current_hours, "$players_oath_renounced_begin_time"),
              
              (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
                (store_faction_of_party, ":cur_center_faction", ":cur_center"),
                (party_set_slot, ":cur_center", slot_center_faction_when_oath_renounced, ":cur_center_faction"),
              (try_end),
              (party_set_slot, "$g_center_to_give_to_player", slot_center_faction_when_oath_renounced, "$players_oath_renounced_against_kingdom"),
              
              (store_relation, ":relation", ":original_kingdom", "fac_player_supporters_faction"),
              (ge, ":relation", 0),
              (call_script, "script_diplomacy_start_war_between_kingdoms", ":original_kingdom", "fac_player_supporters_faction", 1),
            (try_end),
            
            
            (try_begin),
              (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
              (is_between, ":spouse", kingdom_ladies_begin, kingdom_ladies_end),
              ## Begin 1.134
              (try_begin),
                (ge, "$cheat_mode", 1),
                (str_store_troop_name, s4, ":spouse"),
                (display_message, "@{!}DEBUG - {s4} faction changed by marriage, case 2"),
              (try_end),
              ## End 1.134
              (troop_set_faction, ":spouse", "fac_player_supporters_faction"),
            (try_end),
            
            
            #(call_script, "script_store_average_center_value_per_faction"),
            (call_script, "script_update_all_notes"),
            (assign, "$g_recalculate_ais", 1),
            
        ]),
        
        
        
        #script_agent_reassign_team
        # INPUT: arg1 = agent_no
        # OUTPUT: none
        ("agent_reassign_team",
          [
            (store_script_param, ":agent_no", 1),
            (get_player_agent_no, ":player_agent"),
            (try_begin),
              (ge, ":player_agent", 0),
              (agent_is_human, ":agent_no"),
              (agent_is_ally, ":agent_no"),
              (agent_get_party_id, ":party_no", ":agent_no"),
              (ge, ":party_no", 0), ## CC
              (neq, ":party_no", "p_main_party"),
              (assign, ":continue", 1),
              (store_faction_of_party, ":party_faction", ":party_no"),
              (try_begin),
                (eq, ":party_faction", "$players_kingdom"),
                (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
                (faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
                (assign, ":continue", 0),
              (else_try),
                (party_stack_get_troop_id, ":leader_troop_id", ":party_no", 0),
                (neg|is_between, ":leader_troop_id", active_npcs_begin, active_npcs_end),
                (assign, ":continue", 0),
              (try_end),
              (eq, ":continue", 1),
              (agent_get_team, ":player_team", ":player_agent"),
              (val_add, ":player_team", 2),
              (agent_set_team, ":agent_no", ":player_team"),
            (try_end),
        ]),
        
        #script_start_quest
        # INPUT: arg1 = quest_no, arg2 = giver_troop_no, s2 = description_text
        # OUTPUT: none
        ("start_quest",
          [(store_script_param, ":quest_no", 1),
            (store_script_param, ":giver_troop_no", 2),
            
            (quest_set_slot, ":quest_no", slot_quest_giver_troop, ":giver_troop_no"),
            
            (try_begin),
              (eq, ":giver_troop_no", -1),
              (str_store_string, s63, "str_political_suggestion"),
            (else_try),
              (is_between, ":giver_troop_no", active_npcs_begin, active_npcs_end),
              (str_store_troop_name_link, s62, ":giver_troop_no"),
              (str_store_string, s63, "@Given by: {s62}"),
            (else_try),
              (str_store_troop_name, s62, ":giver_troop_no"),
              (str_store_string, s63, "@Given by: {s62}"),
            (try_end),
            (store_current_hours, ":cur_hours"),
            (str_store_date, s60, ":cur_hours"),
            (str_store_string, s60, "@Given on: {s60}"),
            (add_quest_note_from_sreg, ":quest_no", 0, s60, 0),
            (add_quest_note_from_sreg, ":quest_no", 1, s63, 0),
            (add_quest_note_from_sreg, ":quest_no", 2, s2, 0),
            
            (try_begin),
              (quest_slot_ge, ":quest_no", slot_quest_expiration_days, 1),
              (quest_get_slot, reg0, ":quest_no", slot_quest_expiration_days),
              (add_quest_note_from_sreg, ":quest_no", 7, "@You have {reg0} days to finish this quest.", 0),
            (try_end),
            
            #Adding dont_give_again_for_days value
            (try_begin),
              (quest_slot_ge, ":quest_no", slot_quest_dont_give_again_period, 1),
              (quest_get_slot, ":dont_give_again_period", ":quest_no", slot_quest_dont_give_again_period),
              (quest_set_slot, ":quest_no", slot_quest_dont_give_again_remaining_days, ":dont_give_again_period"),
            (try_end),
            (start_quest, ":quest_no", ":giver_troop_no"),
            
            (try_begin),
              (eq, ":quest_no", "qst_report_to_army"),
              (assign, "$number_of_report_to_army_quest_notes", 8),
              (faction_get_slot, ":faction_ai_state", "$players_kingdom", slot_faction_ai_state),
              (call_script, "script_update_report_to_army_quest_note", "$players_kingdom", ":faction_ai_state", -1),
            (try_end),
            
            (display_message, "str_quest_log_updated"),
        ]),
        
        #script_conclude_quest
        # INPUT: arg1 = quest_no
        # OUTPUT: none
        ("conclude_quest",
          [
            (store_script_param, ":quest_no", 1),
            (conclude_quest, ":quest_no"),
            (quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
            (str_store_troop_name, s59, ":quest_giver_troop"),
            (add_quest_note_from_sreg, ":quest_no", 7, "@This quest has been concluded. Talk to {s59} to finish it.", 0),
        ]),
        
        #script_succeed_quest
        # INPUT: arg1 = quest_no
        # OUTPUT: none
        ("succeed_quest",
          [
            (store_script_param, ":quest_no", 1),
            (succeed_quest, ":quest_no"),
            (quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
            (str_store_troop_name, s59, ":quest_giver_troop"),
            (add_quest_note_from_sreg, ":quest_no", 7, "@This quest has been successfully completed. Talk to {s59} to claim your reward.", 0),
        ]),
        
        #script_fail_quest
        # INPUT: arg1 = quest_no
        # OUTPUT: none
        ("fail_quest",
          [
            (store_script_param, ":quest_no", 1),
            (fail_quest, ":quest_no"),
            (quest_get_slot, ":quest_giver_troop", ":quest_no", slot_quest_giver_troop),
            (str_store_troop_name, s59, ":quest_giver_troop"),
            (add_quest_note_from_sreg, ":quest_no", 7, "@This quest has failed. Talk to {s59} to explain the situation.", 0),
        ]),
        
        #script_report_quest_troop_positions
        # INPUT: arg1 = quest_no, arg2 = troop_no, arg3 = note_index
        # OUTPUT: none
        ("report_quest_troop_positions",
          [
            (store_script_param, ":quest_no", 1),
            (store_script_param, ":troop_no", 2),
            (store_script_param, ":note_index", 3),
            (call_script, "script_get_information_about_troops_position", ":troop_no", 1),
            (str_store_string, s5, "@At the time quest was given:^{s1}"),
            (add_quest_note_from_sreg, ":quest_no", ":note_index", s5, 1),
            (call_script, "script_update_troop_location_notes", ":troop_no", 1),
        ]),
        
        #script_end_quest
        # INPUT: arg1 = quest_no
        # OUTPUT: none
        ("end_quest",
          [
            (store_script_param, ":quest_no", 1),
            (str_clear, s1),
            (add_quest_note_from_sreg, ":quest_no", 0, s1, 0),
            (add_quest_note_from_sreg, ":quest_no", 1, s1, 0),
            (add_quest_note_from_sreg, ":quest_no", 2, s1, 0),
            (add_quest_note_from_sreg, ":quest_no", 3, s1, 0),
            (add_quest_note_from_sreg, ":quest_no", 4, s1, 0),
            (add_quest_note_from_sreg, ":quest_no", 5, s1, 0),
            (add_quest_note_from_sreg, ":quest_no", 6, s1, 0),
            (add_quest_note_from_sreg, ":quest_no", 7, s1, 0),
            (try_begin),
              (neg|check_quest_failed, ":quest_no"),
              (val_add, "$g_total_quests_completed", 1),
            (try_end),
            (try_begin),
              (eq, ":quest_no", "qst_consult_with_minister"),
              (assign, "$g_minister_notification_quest", 0),
            (try_end),
            (complete_quest, ":quest_no"),
            (try_begin),
              (is_between, ":quest_no", mayor_quests_begin, mayor_quests_end),
              (assign, "$merchant_quest_last_offerer", -1),
              (assign, "$merchant_offered_quest", -1),
            (try_end),
        ]),
        
        #script_cancel_quest
        # INPUT: arg1 = quest_no
        # OUTPUT: none
        ("cancel_quest",
          [(store_script_param, ":quest_no", 1),
            (str_clear, s1),
            (add_quest_note_from_sreg, ":quest_no", 0, s1, 0),
            (add_quest_note_from_sreg, ":quest_no", 1, s1, 0),
            (add_quest_note_from_sreg, ":quest_no", 2, s1, 0),
            (add_quest_note_from_sreg, ":quest_no", 3, s1, 0),
            (add_quest_note_from_sreg, ":quest_no", 4, s1, 0),
            (add_quest_note_from_sreg, ":quest_no", 5, s1, 0),
            (add_quest_note_from_sreg, ":quest_no", 6, s1, 0),
            (add_quest_note_from_sreg, ":quest_no", 7, s1, 0),
            (cancel_quest, ":quest_no"),
            (try_begin),
              (is_between, ":quest_no", mayor_quests_begin, mayor_quests_end),
              (assign, "$merchant_quest_last_offerer", -1),
              (assign, "$merchant_offered_quest", -1),
            (try_end),
        ]),
        
        ##  #script_get_available_mercenary_troop_and_amount_of_center
        ##  # INPUT: arg1 = center_no
        ##  # OUTPUT: reg0 = mercenary_troop_type, reg1 = amount
        ##  ("get_available_mercenary_troop_and_amount_of_center",
        ##    [(store_script_param, ":center_no", 1),
        ##     (party_get_slot, ":mercenary_troop", ":center_no", slot_center_mercenary_troop_type),
        ##     (party_get_slot, ":mercenary_amount", ":center_no", slot_center_mercenary_troop_amount),
        ##     (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
        ##     (val_min, ":mercenary_amount", ":free_capacity"),
        ##     (store_troop_gold, ":cur_gold", "trp_player"),
        ##     (call_script, "script_game_get_join_cost", ":mercenary_troop"),
        ##     (assign, ":join_cost", reg0),
        ##     (try_begin),
        ##       (gt, ":join_cost", 0),
        ##       (val_div, ":cur_gold", ":join_cost"),
        ##       (val_min, ":mercenary_amount", ":cur_gold"),
        ##     (try_end),
        ##     (assign, reg0, ":mercenary_troop"),
        ##     (assign, reg1, ":mercenary_amount"),
        ##     ]),
        ##
        
        #script_update_village_market_towns
        # INPUT: none
        # OUTPUT: none
        ("update_village_market_towns",
          [(try_for_range, ":cur_village", villages_begin, villages_end),
              (store_faction_of_party, ":village_faction", ":cur_village"),
              (assign, ":min_dist", 999999),
              (assign, ":min_dist_town", -1),
              (try_for_range, ":cur_town", towns_begin, towns_end),
                (store_faction_of_party, ":town_faction", ":cur_town"),
                (eq, ":town_faction", ":village_faction"),
                (store_distance_to_party_from_party, ":cur_dist", ":cur_village", ":cur_town"),
                (lt, ":cur_dist", ":min_dist"),
                (assign, ":min_dist", ":cur_dist"),
                (assign, ":min_dist_town", ":cur_town"),
              (try_end),
              
              (try_begin),
                (gt, ":min_dist_town", -1),
                (party_set_slot, ":cur_village", slot_village_market_town, ":min_dist_town"),
              (else_try),
                (assign, ":min_dist", 999999),
                (assign, ":min_dist_town", -1),
                (try_for_range, ":cur_town", towns_begin, towns_end),
                  (store_faction_of_party, ":town_faction", ":cur_town"),
                  (store_relation, ":relation", ":town_faction", ":village_faction"),
                  (ge, ":relation", 0),
                  (store_distance_to_party_from_party, ":cur_dist", ":cur_village", ":cur_town"),
                  (lt, ":cur_dist", ":min_dist"),
                  (assign, ":min_dist", ":cur_dist"),
                  (assign, ":min_dist_town", ":cur_town"),
                (try_end),
                (gt, ":min_dist_town", -1),
                (party_set_slot, ":cur_village", slot_village_market_town, ":min_dist_town"),
              (try_end),
            (try_end),
        ]),
        
        
        
        #script_update_mercenary_units_of_towns				w/o Diplomacy 3.32+ for now
        # INPUT: none
        # OUTPUT: none
        ("update_mercenary_units_of_towns",
          [(try_for_range, ":town_no", towns_begin, towns_end),
				(troop_get_slot, ":merc_townsman", "$troop_trees", slot_mercenary_townsman),
				(troop_get_slot, ":merc_ritter", "$troop_trees", slot_mercenary_hochmeister),
			  (store_random_in_range, ":troop_no", ":merc_townsman", ":merc_ritter"),
              (party_set_slot, ":town_no", slot_center_mercenary_troop_type, ":troop_no"),
              (store_random_in_range, ":amount", 3, 15),
              (party_set_slot, ":town_no", slot_center_mercenary_troop_amount, ":amount"), #This adds a second mercanery to the tavern
				(troop_get_slot, ":merc_ritter", "$troop_trees", slot_woman_refugee),
				(troop_get_slot, ":merc_extra1", "$troop_trees", slot_woman_walkure),
			  (store_random_in_range, ":troop_no2", ":merc_ritter", ":merc_extra1"),
              (party_set_slot, ":town_no", slot_center_mercenary_troop_type_2, ":troop_no2"),
              (store_random_in_range, ":amount2", 3, 15),
              (party_set_slot, ":town_no", slot_center_mercenary_troop_amount_2, ":amount2"),
            (try_end),
        ]),

        ("start_update_mercenary_units_of_towns",
          [(try_for_range, ":town_no", towns_begin, towns_end),
			(troop_get_slot, ":merc_townsman", "$troop_trees", slot_mercenary_townsman),
				(troop_get_slot, ":merc_ritter", "$troop_trees", slot_mercenary_hochmeister),
			  (store_random_in_range, ":troop_no", ":merc_townsman", ":merc_ritter"),
              (party_set_slot, ":town_no", slot_center_mercenary_troop_type, ":troop_no"),
              (store_random_in_range, ":amount", 3, 15),
              (party_set_slot, ":town_no", slot_center_mercenary_troop_amount, ":amount"), #This adds a second mercanery to the tavern
				(troop_get_slot, ":merc_ritter", "$troop_trees", slot_woman_refugee),
				(troop_get_slot, ":merc_extra1", "$troop_trees", slot_woman_walkure),
			  (store_random_in_range, ":troop_no2", ":merc_ritter", ":merc_extra1"),
              (party_set_slot, ":town_no", slot_center_mercenary_troop_type_2, ":troop_no2"),
              (store_random_in_range, ":amount2", 3, 15),
              (party_set_slot, ":town_no", slot_center_mercenary_troop_amount_2, ":amount2"),
            (try_end),
        ]),
		
		#Floris begin
		#STAT
		#script_update_town_specialists 
		#Input: none
		#Output: none
		("update_town_specialists",
		   [(try_for_range, ":town_no", towns_begin, towns_end),
				(store_random_in_range, ":troop_no", town_specialist_begin, town_specialist_end),
				(party_set_slot, ":town_no", slot_center_specialist_type, ":troop_no"),
				(store_random_in_range, ":amount", 1, 3),
				(party_set_slot, ":town_no", slot_center_specialist_amount, ":amount"),				
			(try_end),
			(try_for_range, ":town_no", villages_begin, villages_end),
				(store_random_in_range, ":troop_no", village_specialist_begin, village_specialist_end),
				(party_set_slot, ":town_no", slot_center_specialist_type, ":troop_no"),
				(store_random_in_range, ":amount", 1, 3),
				(party_set_slot, ":town_no", slot_center_specialist_amount, ":amount"),				
			(try_end),
			(try_for_range, ":town_no", castles_begin, castles_end),
				(store_random_in_range, ":troop_no", castle_specialist_begin, castle_specialist_end),
				(party_set_slot, ":town_no", slot_center_specialist_type, ":troop_no"),
				(store_random_in_range, ":amount", 1, 3),
				(party_set_slot, ":town_no", slot_center_specialist_amount, ":amount"),					
			(try_end),
        ]),
			
			
        #script_update_volunteer_troops_in_village
        # INPUT: arg1 = center_no
        # OUTPUT: none
        ("update_volunteer_troops_in_village",
          [
            (store_script_param, ":center_no", 1),
            (party_get_slot, ":player_relation", ":center_no", slot_center_player_relation),
                   (party_get_slot, ":center_culture", ":center_no", slot_center_culture),
            #(store_faction_of_party, ":center_culture", ":center_no"), #Player Faction
            
            
            ##	   (try_begin),
            ##		(eq, "$cheat_mode", 2),
            ##	    (str_store_party_name, s4, ":center_no"),
            ##	    (str_store_faction_name, s5, ":center_culture"),
            ##	    (display_message, "str_updating_volunteers_for_s4_faction_is_s5"),
            ##	   (try_end),
            
            (faction_get_slot, ":volunteer_troop", ":center_culture", slot_faction_tier_1_troop),
            (assign, ":volunteer_troop_tier", 1),
            (store_div, ":tier_upgrades", ":player_relation", 10),
            (try_for_range, ":unused", 0, ":tier_upgrades"),
              (store_random_in_range, ":random_no", 0, 100),
              (lt, ":random_no", 10),
              (store_random_in_range, ":random_no", 0, 2),
              (troop_get_upgrade_troop, ":upgrade_troop_no", ":volunteer_troop", ":random_no"),
              (try_begin),
                (le, ":upgrade_troop_no", 0),
                (troop_get_upgrade_troop, ":upgrade_troop_no", ":volunteer_troop", 0),
              (try_end),
              (gt, ":upgrade_troop_no", 0),
              (val_add, ":volunteer_troop_tier", 1),
              (assign, ":volunteer_troop", ":upgrade_troop_no"),
            (try_end),
            
            (assign, ":upper_limit", 8),							#	1.143 Port // Increased from 7
            (try_begin),
              (ge, ":player_relation", 4),							#	1.143 Port // Decreased from 5
              (assign, ":upper_limit", ":player_relation"),
              (val_div, ":upper_limit", 2),
              (val_add, ":upper_limit", 6),							#	1.143 Port // Decreased from 10
            (else_try),
              (lt, ":player_relation", 0),
              (assign, ":upper_limit", 0),
            (try_end),
            
            
            ##diplomacy begin
            (assign, ":percent", 100),
            (try_begin), #-30% if not owner
              (neg|party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
              (val_sub, ":percent", 30),
            (try_end),
            (try_begin), #1%/4 renown
              (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
              (val_div, ":player_renown", 4),
              (val_add, ":percent", ":player_renown"),
            (try_end),
            (try_begin), #1%/3 honour
              (assign, ":player_honour", "$player_honor"),
              (val_div, ":player_honour", 3),
              (val_add, ":percent", ":player_honour"),
            (try_end),
            (try_begin), #+5% if king
              (faction_get_slot, ":faction_leader", "fac_player_supporters_faction", slot_faction_leader),
              (eq, ":faction_leader", "trp_player"),
              (val_add, ":percent", 5),
              
              (try_begin), #-5% for each point of serfdom
                (faction_get_slot, ":serfdom", "fac_player_supporters_faction", dplmc_slot_faction_serfdom),
                (neq, ":serfdom", 0),
                (val_mul, ":serfdom", 5),
                (val_sub, ":percent", ":serfdom"),
              (try_end),
              
              (try_begin),  #+5% if king of village
                (store_faction_of_party, ":faction", ":center_no"),
                (eq, ":faction", "fac_player_supporters_faction"),
                (val_add, ":percent", 5),
              (try_end),
            (try_end),
            
            (try_begin),
              (gt, ":upper_limit", 0),
              (val_clamp, ":percent", 0, 201),
              (val_mul, ":upper_limit", ":percent"),
              (val_div, ":upper_limit", 100),
            (try_end),
            
            ##diplomacy end
            
            
            (val_mul, ":upper_limit", 3),
            (store_add, ":amount_random_divider", 2, ":volunteer_troop_tier"),
            (val_div, ":upper_limit", ":amount_random_divider"),
            
            (store_random_in_range, ":amount", 0, ":upper_limit"),
            (party_set_slot, ":center_no", slot_center_volunteer_troop_type, ":volunteer_troop"),
            (party_set_slot, ":center_no", slot_center_volunteer_troop_amount, ":amount"),
        ]),
        
        #script_update_npc_volunteer_troops_in_village
        # INPUT: arg1 = center_no
        # OUTPUT: none
        ("update_npc_volunteer_troops_in_village",
          [
            (store_script_param, ":center_no", 1),
                   (party_get_slot, ":center_culture", ":center_no", slot_center_culture),
            #(store_faction_of_party, ":center_culture", ":center_no"), #Player Faction
            (faction_get_slot, ":volunteer_troop", ":center_culture", slot_faction_tier_1_troop),
            (assign, ":volunteer_troop_tier", 1),
            (try_for_range, ":unused", 0, 5),
              (store_random_in_range, ":random_no", 0, 100),
              (lt, ":random_no", 10),
              (store_random_in_range, ":random_no", 0, 2),
              (troop_get_upgrade_troop, ":upgrade_troop_no", ":volunteer_troop", ":random_no"),
              (try_begin),
                (le, ":upgrade_troop_no", 0),
                (troop_get_upgrade_troop, ":upgrade_troop_no", ":volunteer_troop", 0),
              (try_end),
              (gt, ":upgrade_troop_no", 0),
              (val_add, ":volunteer_troop_tier", 1),
              (assign, ":volunteer_troop", ":upgrade_troop_no"),
            (try_end),
            
            (assign, ":upper_limit", 12),
            
            (store_add, ":amount_random_divider", 2, ":volunteer_troop_tier"),
            (val_div, ":upper_limit", ":amount_random_divider"),
            
            (store_random_in_range, ":amount", 0, ":upper_limit"),
            (party_set_slot, ":center_no", slot_center_npc_volunteer_troop_type, ":volunteer_troop"),
            (party_set_slot, ":center_no", slot_center_npc_volunteer_troop_amount, ":amount"),
        ]),
        
        #script_update_companion_candidates_in_taverns
        # INPUT: none
        # OUTPUT: none
        ("update_companion_candidates_in_taverns",
		[
		  (try_begin),
			(eq, "$cheat_mode", 1),
			(display_message, "str_shuffling_companion_locations"),
		  (try_end),

		  (try_for_range, ":troop_no", companions_begin, companions_end),
			##diplomacy start+ Move this *after* the checks!
			#  (troop_set_slot, ":troop_no", slot_troop_cur_center, -1),
			##diplomacy end+
			(troop_slot_eq, ":troop_no", slot_troop_days_on_mission, 0),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive),

			(neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
			##diplomacy start+
			(troop_get_slot, ":town_no", ":troop_no", slot_troop_cur_center),
			(try_begin),
				(is_between, ":town_no", towns_begin, towns_end),
				(party_get_slot, ":town_lord", ":town_no", slot_town_lord),
				##zerilius changes begin
				##bug fix for red text
				(ge, ":town_lord", 0),
				##zerilius changes end				
				(this_or_next|eq, ":town_lord", "trp_player"),
				(this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, ":town_lord"),
					(troop_slot_eq, ":town_lord", slot_troop_spouse, "trp_player"),
			(else_try),
				#Moved from above:
				(troop_set_slot, ":troop_no", slot_troop_cur_center, -1),
			(try_end),
			(neg|troop_slot_ge, ":troop_no", slot_troop_cur_center, 1),
			##diplomacy end+
			(store_random_in_range, ":town_no", towns_begin, towns_end),
			(try_begin),
			  ##diplomacy start+ Remove the "you can't go home again" condition if the player owns the town
			  (assign, ":veto", 0),
			  (try_begin),
				(store_faction_of_party, ":town_faction", ":town_no"),
				(eq, ":town_faction", "fac_player_supporters_faction"),
			  (else_try),
				(party_get_slot, ":town_lord", ":town_no", slot_town_lord),
				(ge, ":town_lord", 0),
				(this_or_next|eq, ":town_lord", "trp_player"),
				(this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, ":town_lord"),
					(troop_slot_eq, ":town_lord", slot_troop_spouse, "trp_player"),
			  (else_try),
				#Native veto:
				(this_or_next|troop_slot_eq, ":troop_no", slot_troop_home, ":town_no"),
					(troop_slot_eq, ":troop_no", slot_troop_first_encountered, ":town_no"),
				(assign, ":veto", 1),
			  (try_end),
			  (eq, ":veto", 0),
					  ##diplomacy end+
			  (troop_set_slot, ":troop_no", slot_troop_cur_center, ":town_no"),
			  (try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_troop_name, 4, ":troop_no"),
				(str_store_party_name, 5, ":town_no"),
				(display_message, "@{!}{s4} is in {s5}"),
			  (try_end),
			(try_end),
		  (try_end),
		 ]),
        
        #script_update_ransom_brokers
        # INPUT: none
        # OUTPUT: none
        ("update_ransom_brokers",
          [(try_for_range, ":town_no", towns_begin, towns_end),
              (party_set_slot, ":town_no", slot_center_ransom_broker, 0),
            (try_end),
            
            (try_for_range, ":troop_no", ransom_brokers_begin, ransom_brokers_end),
              (store_random_in_range, ":town_no", towns_begin, towns_end),
              (party_set_slot, ":town_no", slot_center_ransom_broker, ":troop_no"),
            (try_end),
            
            (party_set_slot,"p_town_2",slot_center_ransom_broker,"trp_ramun_the_slave_trader"),
            ## CC 1.322 this doubles the incidence of ransom brokers
            (try_for_range, ":town_no", towns_begin, towns_end),
              (party_get_slot, ":ransom_broker", ":town_no", slot_center_ransom_broker),
              (le, ":ransom_broker", 0),
              (store_add, ":alternative_town", ":town_no", 9),
              (try_begin),
                (ge, ":alternative_town", towns_end),
                (val_sub, ":alternative_town", 22),
              (try_end),
              (party_get_slot, ":ransom_broker_2", ":alternative_town", slot_center_ransom_broker),
              (is_between, ":ransom_broker_2", ransom_brokers_begin, ransom_brokers_end),
              (party_set_slot, ":town_no", slot_center_ransom_broker, ":ransom_broker_2"),
            (try_end),
            ## CC
        ]),
        
        #script_update_tavern_travellers
        # INPUT: none
        # OUTPUT: none
        ("update_tavern_travellers",
          [(try_for_range, ":town_no", towns_begin, towns_end),
              (party_set_slot, ":town_no", slot_center_tavern_traveler, 0),
            (try_end),
            
            (try_for_range, ":troop_no", tavern_travelers_begin, tavern_travelers_end),
              (store_random_in_range, ":town_no", towns_begin, towns_end),
              (party_set_slot, ":town_no", slot_center_tavern_traveler, ":troop_no"),
              (assign, ":end_cond", 15),
              (try_for_range, ":unused", 0, ":end_cond"),
                (store_random_in_range, ":info_faction", kingdoms_begin, kingdoms_end),
                (faction_slot_eq, ":info_faction", slot_faction_state, sfs_active),
                (neq, ":info_faction", "$players_kingdom"),
                (neq, ":info_faction", "fac_player_supporters_faction"),
                (party_set_slot, ":town_no", slot_center_traveler_info_faction, ":info_faction"),
                (assign, ":end_cond", 0),
              (try_end),
            (try_end),
            
            (troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, "p_town_1"),
        ]),
        
        #script_update_villages_infested_by_bandits
        # INPUT: none
        # OUTPUT: none
        ("update_villages_infested_by_bandits",
          [(try_for_range, ":village_no", villages_begin, villages_end),
              (try_begin),
                (check_quest_active, "qst_eliminate_bandits_infesting_village"),
                (quest_slot_eq, "qst_eliminate_bandits_infesting_village", slot_quest_target_center, ":village_no"),
                (quest_get_slot, ":cur_state", "qst_eliminate_bandits_infesting_village", slot_quest_current_state),
                (val_add, ":cur_state", 1),
                (try_begin),
                  (lt, ":cur_state", 3),
                  (quest_set_slot, "qst_eliminate_bandits_infesting_village", slot_quest_current_state, ":cur_state"),
                (else_try),
                  (party_set_slot, ":village_no", slot_village_infested_by_bandits, 0),
                  (call_script, "script_abort_quest", "qst_eliminate_bandits_infesting_village", 2),
                (try_end),
              (else_try),
                (check_quest_active, "qst_deal_with_bandits_at_lords_village"),
                (quest_slot_eq, "qst_deal_with_bandits_at_lords_village", slot_quest_target_center, ":village_no"),
                (quest_get_slot, ":cur_state", "qst_deal_with_bandits_at_lords_village", slot_quest_current_state),
                (val_add, ":cur_state", 1),
                (try_begin),
                  (lt, ":cur_state", 3),
                  (quest_set_slot, "qst_deal_with_bandits_at_lords_village", slot_quest_current_state, ":cur_state"),
                (else_try),
                  (party_set_slot, ":village_no", slot_village_infested_by_bandits, 0),
                  (call_script, "script_abort_quest", "qst_deal_with_bandits_at_lords_village", 2),
                (try_end),
              (else_try),
                (party_set_slot, ":village_no", slot_village_infested_by_bandits, 0),
                (store_random_in_range, ":random_no", 0, 100),
				(assign, ":continue", 1),																				#	1.143 Port // Newly Added
				(try_begin),
					(check_quest_active, "qst_collect_taxes"),
					(quest_slot_eq, "qst_collect_taxes", slot_quest_target_center, ":village_no"),
					(assign, ":continue", 0),
				(else_try),
					(check_quest_active, "qst_train_peasants_against_bandits"),
					(quest_slot_eq, "qst_train_peasants_against_bandits", slot_quest_target_center, ":village_no"),
					(assign, ":continue", 0),
				(try_end),
				(eq, ":continue", 1),																					#	End
                (lt, ":random_no", 3),
                (store_random_in_range, ":random_no", 0, 3),
				##Floris MTT begin
                (try_begin),
                  (eq, ":random_no", 0),
					(troop_get_slot,":bandit_bandit","$troop_trees",slot_bandit_bandit),
					  (assign, ":bandit_troop", ":bandit_bandit"),
                (else_try),
                  (eq, ":random_no", 1),
					(troop_get_slot,":bandit_mountain","$troop_trees",slot_bandit_mountain),
					  (assign, ":bandit_troop", ":bandit_mountain"),
                (else_try),
					(troop_get_slot,":bandit_forest","$troop_trees",slot_bandit_forest),
					  (assign, ":bandit_troop", ":bandit_forest"),
                (try_end),
				##Floris MTT end
                (party_set_slot, ":village_no", slot_village_infested_by_bandits, ":bandit_troop"),
                #Reduce prosperity of the village by 3: reduce to -1
                (call_script, "script_change_center_prosperity", ":village_no", -1),
                (val_add, "$newglob_total_prosperity_from_bandits", -1),
                (try_begin),
                  (eq, "$cheat_mode", 2),
                  (str_store_party_name, s1, ":village_no"),
                  (display_message, "@{!}DEBUG --{s1} is infested by bandits."),
                (try_end),
              (try_end),
            (try_end),
        ]),
        
        #script_update_booksellers
        # INPUT: none
        # OUTPUT: none
        ("update_booksellers",
          [(try_for_range, ":town_no", towns_begin, towns_end),
              (party_set_slot, ":town_no", slot_center_tavern_bookseller, 0),
            (try_end),
            
            (try_for_range, ":troop_no", tavern_booksellers_begin, tavern_booksellers_end),
              (store_random_in_range, ":town_no", towns_begin, towns_end),
              (party_set_slot, ":town_no", slot_center_tavern_bookseller, ":troop_no"),
              ## CC
              (troop_get_inventory_capacity, ":inv_cap", ":troop_no"),
              (try_for_range, ":i_slot", 10, ":inv_cap"),
                (troop_get_inventory_slot, ":item", ":troop_no", ":i_slot"),
                (gt, ":item", -1),
                (item_get_type, ":type", ":item"),
                (neq, ":type", itp_type_book),
                (troop_set_inventory_slot, ":troop_no", ":i_slot", -1),
              (try_end),
              ## CC
            (try_end),
        ]),
        
        #script_update_tavern_minstels
        # INPUT: none
        # OUTPUT: none
        ("update_tavern_minstrels",
          [(try_for_range, ":town_no", towns_begin, towns_end),
              (party_set_slot, ":town_no", slot_center_tavern_minstrel, 0),
            (try_end),
            
            (try_for_range, ":troop_no", tavern_minstrels_begin, tavern_minstrels_end),
              (store_random_in_range, ":town_no", towns_begin, towns_end),
              (party_set_slot, ":town_no", slot_center_tavern_minstrel, ":troop_no"),
              (try_begin),
                (eq, "$cheat_mode", 1),
                (str_store_troop_name, s4, ":troop_no"),
                (str_store_party_name, s5, ":town_no"),
                
                (display_message, "str_s4_is_at_s5"),
              (try_end),
            (try_end),
            ## CC 1.322 this doubles the incidence of minstrels
            (try_for_range, ":town_no", towns_begin, towns_end),
              (party_get_slot, ":minstrel", ":town_no", slot_center_tavern_minstrel),
              (le, ":minstrel", 0),
              (store_add, ":alternative_town", ":town_no", 9),
              (try_begin),
                (ge, ":alternative_town", towns_end),
                (val_sub, ":alternative_town", 22),
              (try_end),
              (party_get_slot, ":minstrel_2", ":alternative_town", slot_center_tavern_minstrel),
              (is_between, ":minstrel_2", tavern_minstrels_begin, tavern_minstrels_end),
              (party_set_slot, ":town_no", slot_center_tavern_minstrel, ":minstrel_2"),
            (try_end),
            ## CC
            
            
        ]),
        
        ("update_other_taverngoers",
          [
            (store_random_in_range, ":fight_promoter_tavern", towns_begin, towns_end),
            (troop_set_slot, "trp_fight_promoter", slot_troop_cur_center, ":fight_promoter_tavern"),
            
            (store_random_in_range, ":belligerent_drunk_tavern", towns_begin, towns_end),
            (troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, ":belligerent_drunk_tavern"),
        ]),
        
        
        #script_update_faction_notes
        # INPUT: faction_no
        # OUTPUT: none
        ("update_faction_notes",
          [
            (store_script_param, ":faction_no", 1),
            
            (try_begin),
              (this_or_next|faction_slot_eq, ":faction_no", slot_faction_state, sfs_inactive),
              (eq, ":faction_no", "fac_player_faction"),
              (faction_set_note_available, ":faction_no", 0),
            (else_try),
              (faction_set_note_available, ":faction_no", 1),
            (try_end),
        ]),
        
        ("update_faction_political_notes",
          [(store_script_param, ":faction_no", 1),
            
            (call_script, "script_evaluate_realm_stability", ":faction_no"),
            (add_faction_note_from_sreg, ":faction_no", 2, "str_instability_reg0_of_lords_are_disgruntled_reg1_are_restless", 0),
        ]),
        
        
        
        #script_update_faction_traveler_notes
        # INPUT: faction_no
        # OUTPUT: none
        ("update_faction_traveler_notes",
          [(store_script_param, ":faction_no", 1),
            (assign, ":total_men", 0),
            (try_for_parties, ":cur_party"),
              (store_faction_of_party, ":center_faction", ":cur_party"),
              (eq, ":center_faction", ":faction_no"),
              (party_get_num_companions, ":num_men", ":cur_party"),
              (val_add, ":total_men", ":num_men"),
            (try_end),
            (str_store_faction_name, s5, ":faction_no"),
            (assign, reg1, ":total_men"),
            (add_faction_note_from_sreg, ":faction_no", 1, "@{s5} has a strength of {reg1} men in total.", 1),
        ]),
        
        
        #script_update_troop_notes
        # INPUT: troop_no
        # OUTPUT: none
        ("update_troop_notes",
          [
            ##      (store_script_param, ":troop_no", 1),
            ##     (str_store_troop_name, s54, ":troop_no"),
            ##     (try_begin),
            ##       (eq, ":troop_no", "trp_player"),
            ##       (this_or_next|eq, "$player_has_homage", 1),
            ##		(eq, "$players_kingdom", "fac_player_supporters_faction"),
            ##       (assign, ":troop_faction", "$players_kingdom"),
            ##     (else_try),
            ##       (store_troop_faction, ":troop_faction", ":troop_no"),
            ##     (try_end),
            ##
            ##	 (str_clear, s49),
            ##	 (try_begin),
            ##		(is_between, ":troop_no", lords_begin, kingdom_ladies_end),
            ##		(troop_get_slot, reg1, ":troop_no", slot_troop_age),
            ##		(str_store_string, s49, "str__age_reg1_family_"),
            ##
            ##		(try_for_range, ":aristocrat", lords_begin, kingdom_ladies_end),
            ##			(call_script, "script_troop_get_family_relation_to_troop", ":aristocrat", ":troop_no"),
            ##			(gt, reg0, 0),
            ##
            ##			(try_begin),
            ##				(neg|is_between, ":aristocrat", kingdom_ladies_begin, kingdom_ladies_end),
            ##				(str_store_troop_name_link, s12, ":aristocrat"),
            ##				(call_script, "script_troop_get_relation_with_troop", ":aristocrat", ":troop_no"),
            ##				(str_store_string, s49, "str_s49_s12_s11_rel_reg0"),
            ##			(else_try),
            ##				(str_store_troop_name, s12, ":aristocrat"),
            ##				(str_store_string, s49, "str_s49_s12_s11"),
            ##			(try_end),
            ##
            ##		(try_end),
            ##	 (try_end),
            ##
            ##     (try_begin),
            ##       (neq, ":troop_no", "trp_player"),
            ##       (neg|is_between, ":troop_faction", kingdoms_begin, kingdoms_end),
            ##       (str_clear, s54),
            ##       (add_troop_note_from_sreg, ":troop_no", 0, s54, 0),
            ##       (add_troop_note_from_sreg, ":troop_no", 1, s54, 0),
            ##       (add_troop_note_from_sreg, ":troop_no", 2, s54, 0),
            ###     (else_try),
            ###       (is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
            ###       (str_clear, s54),
            ###       (add_troop_note_from_sreg, ":troop_no", 0, s54, 0),
            ###       (add_troop_note_from_sreg, ":troop_no", 1, s54, 0),
            ###       (add_troop_note_from_sreg, ":troop_no", 2, s54, 0),
            ##     (else_try),
            ##       (is_between, ":troop_no", pretenders_begin, pretenders_end),
            ##       (neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
            ##       (neq, ":troop_no", "$supported_pretender"),
            ##       (troop_get_slot, ":orig_faction", ":troop_no", slot_troop_original_faction),
            ##       (try_begin),
            ##         (faction_slot_eq, ":orig_faction", slot_faction_state, sfs_active),
            ##         (faction_slot_eq, ":orig_faction", slot_faction_has_rebellion_chance, 1),
            ##         (str_store_faction_name_link, s56, ":orig_faction"),
            ##         (add_troop_note_from_sreg, ":troop_no", 0, "@{s54} is a claimant to the throne of {s56}.", 0),
            ##         (add_troop_note_tableau_mesh, ":troop_no", "tableau_troop_note_mesh"),
            ##       (else_try),
            ##         (str_clear, s54),
            ##         (add_troop_note_from_sreg, ":troop_no", 0, s54, 0),
            ##         (add_troop_note_from_sreg, ":troop_no", 1, s54, 0),
            ##         (add_troop_note_from_sreg, ":troop_no", 2, s54, 0),
            ##       (try_end),
            ##     (else_try),
            ##       (faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),
            ##       (str_store_troop_name_link, s55, ":faction_leader"),
            ##       (str_store_faction_name_link, s56, ":troop_faction"),
            ##       (assign, ":troop_is_player_faction", 0),
            ##       (assign, ":troop_is_faction_leader", 0),
            ##       (try_begin),
            ##         (eq, ":troop_faction", "fac_player_faction"),
            ##         (assign, ":troop_is_player_faction", 1),
            ##       (else_try),
            ##         (eq, ":faction_leader", ":troop_no"),
            ##         (assign, ":troop_is_faction_leader", 1),
            ##       (try_end),
            ##       (assign, ":num_centers", 0),
            ##       (str_store_string, s58, "@nowhere"),
            ##       (try_for_range_backwards, ":cur_center", centers_begin, centers_end),
            ##         (party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
            ##         (try_begin),
            ##           (eq, ":num_centers", 0),
            ##           (str_store_party_name_link, s58, ":cur_center"),
            ##         (else_try),
            ##           (eq, ":num_centers", 1),
            ##           (str_store_party_name_link, s57, ":cur_center"),
            ##           (str_store_string, s58, "@{s57} and {s58}"),
            ##         (else_try),
            ##           (str_store_party_name_link, s57, ":cur_center"),
            ##           (str_store_string, s58, "@{!}{s57}, {s58}"),
            ##         (try_end),
            ##         (val_add, ":num_centers", 1),
            ##       (try_end),
            ##       (troop_get_type, reg3, ":troop_no"),
            ##       (troop_get_slot, reg5, ":troop_no", slot_troop_renown),
            ##       (str_clear, s59),
            ##       (try_begin),
            ###         (troop_get_slot, ":relation", ":troop_no", slot_troop_player_relation),
            ##         (call_script, "script_troop_get_player_relation", ":troop_no"),
            ##         (assign, ":relation", reg0),
            ##         (store_add, ":normalized_relation", ":relation", 100),
            ##         (val_add, ":normalized_relation", 5),
            ##         (store_div, ":str_offset", ":normalized_relation", 10),
            ##         (val_clamp, ":str_offset", 0, 20),
            ##         (store_add, ":str_id", "str_relation_mnus_100_ns",  ":str_offset"),
            ##         (neq, ":str_id", "str_relation_plus_0_ns"),
            ##         (str_store_string, s60, "@{reg3?She:He}"),
            ##         (str_store_string, s59, ":str_id"),
            ##         (str_store_string, s59, "@{!}^{s59}"),
            ##       (try_end),
            ##
            ##	#lord recruitment changes begin
            ##	#This sends a bunch of political information to s47.
            ##
            ##
            ##
            ##
            ##	    #refresh registers
            ##        (assign, reg9, ":num_centers"),
            ##        (troop_get_type, reg3, ":troop_no"),
            ##        (troop_get_slot, reg5, ":troop_no", slot_troop_renown),
            ##		(assign, reg4, ":troop_is_faction_leader"),
            ##		(assign, reg6, ":troop_is_player_faction"),
            ##
            ##        (add_troop_note_from_sreg, ":troop_no", 0, "str_reg6reg4s54_is_the_ruler_of_s56_s54_is_a_vassal_of_s55_of_s56_renown_reg5_reg9reg3shehe_is_the_reg3ladylord_of_s58reg3shehe_has_no_fiefss59_s49", 0),
            ##	#lord recruitment changes end
            ##
            ##        (add_troop_note_tableau_mesh, ":troop_no", "tableau_troop_note_mesh"),
            ##     (try_end),
        ]),
        
        #script_update_troop_location_notes
        # INPUT: troop_no
        # OUTPUT: none
        ("update_troop_location_notes",
          [
            (store_script_param, ":troop_no", 1),
            (store_script_param, ":see_or_hear", 2),
            (try_begin),
              (call_script, "script_get_information_about_troops_position", ":troop_no", 1),
              (neq, reg0, 0),
              
			(call_script, "script_search_troop_prisoner_of_party", ":troop_no"),
			(eq, reg0, -1),
			##diplomacy start+ use gender script
			#(troop_get_type, reg1, ":troop_no"),
			(call_script, "script_dplmc_store_troop_is_female", ":troop_no"),
			(assign, reg1, reg0),
			##diplomacy end+
			(try_begin),
			  (eq, ":see_or_hear", 0),
			  (add_troop_note_from_sreg, ":troop_no", 2, "@The last time you saw {reg1?her:him}, {s1}", 1),
			(else_try),
			  (add_troop_note_from_sreg, ":troop_no", 2, "@The last time you heard about {reg1?her:him}, {s1}", 1),
			(try_end),
		  (try_end),
		 ]),
        
		  #script_update_troop_location_notes_prisoned
		  # INPUT: troop_no
		  # OUTPUT: none
		  ("update_troop_location_notes_prisoned",
			[
			  (store_script_param, ":troop_no", 1),
			  (store_script_param, ":capturer_faction_no", 2),
			  ##diplomacy start+ use gender script
			  #(troop_get_type, reg1, ":troop_no"),
			  (call_script, "script_dplmc_store_troop_is_female", ":troop_no"),
			  (assign, reg1, reg0),
			  ##diplomacy end+
			  (str_store_faction_name_link, s1, ":capturer_faction_no"),

			  (add_troop_note_from_sreg, ":troop_no", 2, "str_reg1shehe_is_prisoner_of_s1", 1),
			]),
				
        ("update_troop_political_notes",
          [
            (store_script_param, ":troop_no", 1),
            (try_begin),
              (str_clear, s47),
              
              (store_faction_of_troop, ":troop_faction", ":troop_no"),
              
              (faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),
              
              (str_clear, s40),
              (assign, ":logged_a_rivalry", 0),
              (try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
                (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":kingdom_hero"),
                (lt, reg0, -10),
                
                (str_store_troop_name_link, s39, ":kingdom_hero"),
                (try_begin),
                  (eq, ":logged_a_rivalry", 0),
                  (str_store_string, s40, "str_s39_rival"),
                  (assign, ":logged_a_rivalry", 1),
                (else_try),
                  (str_store_string, s41, "str_s40"),
                  (str_store_string, s40, "str_s41_s39_rival"),
                (try_end),
                
              (try_end),
              
              (str_clear, s46),
              (try_begin),
                (ge, "$cheat_mode", 1),
                (try_begin),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
                  (str_store_string, s46, "str_reputation_cheat_mode_only_martial_"),
                (else_try),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
                  (str_store_string, s46, "str_reputation_cheat_mode_only_debauched_"),
                (else_try),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
                  (str_store_string, s46, "str_reputation_cheat_mode_only_pitiless_"),
                (else_try),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
                  (str_store_string, s46, "str_reputation_cheat_mode_only_calculating_"),
                (else_try),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
                  (str_store_string, s46, "str_reputation_cheat_mode_only_quarrelsome_"),
                (else_try),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
                  (str_store_string, s46, "str_reputation_cheat_mode_only_goodnatured_"),
                (else_try),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
                  (str_store_string, s46, "str_reputation_cheat_mode_only_upstanding_"),
                (else_try),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_conventional),
                  (str_store_string, s46, "str_reputation_cheat_mode_only_conventional_"),
                (else_try),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_adventurous),
                  (str_store_string, s46, "str_reputation_cheat_mode_only_adventurous_"),
                (else_try),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_otherworldly),
                  (str_store_string, s46, "str_reputation_cheat_mode_only_romantic_"),
                (else_try),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_moralist),
                  (str_store_string, s46, "str_reputation_cheat_mode_only_moralist_"),
                (else_try),
                  (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_ambitious),
                  (str_store_string, s46, "str_reputation_cheat_mode_only_ambitious_"),
                (else_try),
                  (troop_get_slot, reg11, ":troop_no", slot_lord_reputation_type),
                  (str_store_string, s46, "str_reputation_cheat_mode_only_reg11_"),
                (try_end),
                
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
                    (troop_get_slot, ":love_interest", ":troop_no", ":love_interest_slot"),
                    (is_between, ":love_interest", kingdom_ladies_begin, kingdom_ladies_end),
                    (str_store_troop_name_link, s39, ":love_interest"),
                    (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":love_interest"),
                    (str_store_string, s2, "str_love_interest"),
                    (try_begin),
                      (troop_slot_eq, ":troop_no", slot_troop_betrothed, ":love_interest"),
                      (str_store_string, s2, "str_betrothed"),
                    (try_end),
                    (str_store_string, s40, "str_s40_s39_s2_reg0"),
                  (try_end),
                (try_end),
                
              (try_end),
              
              (str_store_string, s45, "str_other_relations_s40_"),
              
              (str_clear, s44),
              (try_begin),
                (neq, ":troop_no", ":faction_leader"),
                (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
                (str_store_string, s44, "str_relation_with_liege_reg0_"),
              (try_end),
              
              (str_clear, s48),
              
              (try_begin),
                (eq, "$cheat_mode", 1),
                (store_current_hours, ":hours"),
                (gt, ":hours", 0),
                #				(display_message, "@{!}Updating political factors"),
                (call_script, "script_calculate_troop_political_factors_for_liege", ":troop_no", ":faction_leader"),
                (str_store_string, s48, "str_sense_of_security_military_reg1_court_position_reg3_"),
              (try_end),
              (str_store_string, s47, "str_s46s45s44s48"),
              
              (add_troop_note_from_sreg, ":troop_no", 3, "str_political_details_s47_", 1),
              
            (try_end),
        ]),
        
        #script_update_center_notes
        # INPUT: center_no
        # OUTPUT: none
        ("update_center_notes",
          [
            ##      (store_script_param, ":center_no", 1),
            ##
            ##     (party_get_slot, ":lord_troop", ":center_no", slot_town_lord),
            ##     (try_begin),
            ##       (ge, ":lord_troop", 0),
            ##       (store_troop_faction, ":lord_faction", ":lord_troop"),
            ##       (str_store_troop_name_link, s1, ":lord_troop"),
            ##       (try_begin),
            ##         (eq, ":lord_troop", "trp_player"),
            ##         (gt, "$players_kingdom", 0),
            ##         (str_store_faction_name_link, s2, "$players_kingdom"),
            ##       (else_try),
            ##         (str_store_faction_name_link, s2, ":lord_faction"),
            ##       (try_end),
            ##       (str_store_party_name, s50, ":center_no"),
            ##       (try_begin),
            ##         (party_slot_eq, ":center_no", slot_party_type, spt_town),
            ##         (str_store_string, s51, "@The town of {s50}"),
            ##       (else_try),
            ##         (party_slot_eq, ":center_no", slot_party_type, spt_village),
            ##         (party_get_slot, ":bound_center", ":center_no", slot_village_bound_center),
            ##         (str_store_party_name_link, s52, ":bound_center"),
            ##         (str_store_string, s51, "@The village of {s50} near {s52}"),
            ##       (else_try),
            ##         (str_store_string, s51, "@{!}{s50}"),
            ##       (try_end),
            ##       (str_store_string, s2, "@{s51} belongs to {s1} of {s2}.^"),
            ##     (else_try),
            ##       (str_clear, s2),
            ##     (try_end),
            ##     (try_begin),
            ##       (is_between, ":center_no", villages_begin, villages_end),
            ##     (else_try),
            ##       (assign, ":num_villages", 0),
            ##       (try_for_range_backwards, ":village_no", villages_begin, villages_end),
            ##         (party_slot_eq, ":village_no", slot_village_bound_center, ":center_no"),
            ##         (try_begin),
            ##           (eq, ":num_villages", 0),
            ##           (str_store_party_name_link, s8, ":village_no"),
            ##         (else_try),
            ##           (eq, ":num_villages", 1),
            ##           (str_store_party_name_link, s7, ":village_no"),
            ##           (str_store_string, s8, "@{s7} and {s8}"),
            ##         (else_try),
            ##           (str_store_party_name_link, s7, ":village_no"),
            ##           (str_store_string, s8, "@{!}{s7}, {s8}"),
            ##         (try_end),
            ##         (val_add, ":num_villages", 1),
            ##       (try_end),
            ##       (try_begin),
            ##         (eq, ":num_villages", 0),
            ##         (str_store_string, s2, "@{s2}It has no villages.^"),
            ##       (else_try),
            ##         (store_sub, reg0, ":num_villages", 1),
            ##         (str_store_string, s2, "@{s2}{reg0?Its villages are:Its village is} {s8}.^"),
            ##       (try_end),
            ##     (try_end),
            ##     (call_script, "script_get_prosperity_text_to_s50", ":center_no"),
            ##     (add_party_note_from_sreg, ":center_no", 0, "@{s2}Its prosperity is: {s50}", 0),
            ##     (add_party_note_tableau_mesh, ":center_no", "tableau_center_note_mesh"),
        ]),
        
        
        #script_update_center_recon_notes
        # INPUT: center_no
        # OUTPUT: none
        ("update_center_recon_notes",
          [(store_script_param, ":center_no", 1),
            (try_begin),
              (this_or_next|is_between, ":center_no", towns_begin, towns_end),
              (is_between, ":center_no", castles_begin, castles_end),
              (party_get_slot, ":center_food_store", ":center_no", slot_party_food_store),
              (call_script, "script_center_get_food_consumption", ":center_no"),
              (assign, ":food_consumption", reg0),
              (store_div, reg6, ":center_food_store", ":food_consumption"),
              (party_collect_attachments_to_party, ":center_no", "p_collective_ally"),
              (party_get_num_companions, reg5, "p_collective_ally"),
              (add_party_note_from_sreg, ":center_no", 1, "@Current garrison consists of {reg5} men.^Has food stock for {reg6} days.", 1),
            (try_end),
        ]),
        
        #script_update_all_notes
        # INPUT: none
        # OUTPUT: none
        ("update_all_notes",
          [
            (call_script, "script_update_troop_notes", "trp_player"),
            (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
              (this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
              (this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_lady),
              (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive_pretender),
              (call_script, "script_update_troop_notes", ":troop_no"),
            (try_end),
            (try_for_range, ":center_no", centers_begin, centers_end),
              (call_script, "script_update_center_notes", ":center_no"),
            (try_end),
            (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
              (call_script, "script_update_faction_notes", ":faction_no"),
            (try_end),
        ]),
        
        #script_agent_troop_get_banner_mesh
        # INPUT: agent_no, troop_no
        # OUTPUT: banner_mesh
        ("agent_troop_get_banner_mesh",
          [
            (store_script_param, ":agent_no", 1),
            (store_script_param, ":troop_no", 2),
            (assign, ":banner_troop", -1),
            (assign, ":banner_mesh", "mesh_banners_default_b"),
            (try_begin),
              (lt, ":agent_no", 0),
              (try_begin),
                (ge, ":troop_no", 0),
                (this_or_next|troop_slot_ge, ":troop_no", slot_troop_banner_scene_prop, 1),
                (eq, ":troop_no", "trp_player"),
                (assign, ":banner_troop", ":troop_no"),
              (else_try),
                (is_between, ":troop_no", companions_begin, companions_end),
                (assign, ":banner_troop", "trp_player"),
              (else_try),
                (assign, ":banner_mesh", "mesh_banners_default_a"),
              (try_end),
            (else_try),
              (eq, "$g_is_quick_battle", 1),
              (agent_get_team, ":agent_team", ":agent_no"),
              (try_begin),
                (eq, ":agent_team", 0),
                (assign, ":banner_mesh", "$g_quick_battle_team_0_banner"),
              (else_try),
                (assign, ":banner_mesh", "$g_quick_battle_team_1_banner"),
              (try_end),
            (else_try),
              (game_in_multiplayer_mode),
              (agent_get_group, ":agent_group", ":agent_no"),
              (try_begin),
                (neg|player_is_active, ":agent_group"),
                (agent_get_player_id, ":agent_group", ":agent_no"),
              (try_end),
              (try_begin),
                #if player banners are not allowed, use the default banner mesh
                (eq, "$g_multiplayer_allow_player_banners", 1),
                (player_is_active, ":agent_group"),
                (player_get_banner_id, ":player_banner", ":agent_group"),
                (ge, ":player_banner", 0),
                (store_add, ":banner_mesh", ":player_banner", arms_meshes_begin),
                (assign, ":already_used", 0),
                (try_for_range, ":cur_faction", npc_kingdoms_begin, npc_kingdoms_end), #wrong client data check
                  (faction_slot_eq, ":cur_faction", slot_faction_banner, ":banner_mesh"),
                  (assign, ":already_used", 1),
                (try_end),
                (eq, ":already_used", 0), #otherwise use the default banner mesh
              (else_try),
                (agent_get_team, ":agent_team", ":agent_no"),
                (team_get_faction, ":team_faction_no", ":agent_team"),
                
                (try_begin),
                  (agent_is_human, ":agent_no"),
                  (faction_get_slot, ":banner_mesh", ":team_faction_no", slot_faction_banner),
                (else_try),
                  (agent_get_rider, ":rider_agent_no", ":agent_no"),
                  #(agent_get_position, pos1, ":agent_no"),
                  #(position_get_x, ":pos_x", pos1),
                  #(position_get_y, ":pos_y", pos1),
                  #(assign, reg0, ":pos_x"),
                  #(assign, reg1, ":pos_y"),
                  #(assign, reg2, ":agent_no"),
                  #(display_message, "@{!}agent_no:{reg2}, pos_x:{reg0} , posy:{reg1}"),
                  (try_begin),
                    (ge, ":rider_agent_no", 0),
                    (agent_is_active, ":rider_agent_no"),
                    (agent_get_team, ":rider_agent_team", ":rider_agent_no"),
                    (team_get_faction, ":rider_team_faction_no", ":rider_agent_team"),
                    (faction_get_slot, ":banner_mesh", ":rider_team_faction_no", slot_faction_banner),
                  (else_try),
                    (assign, ":banner_mesh", "mesh_banners_default_c"),
                  (try_end),
                (try_end),
              (try_end),
            (else_try),
              (agent_get_troop_id, ":troop_id", ":agent_no"),
              (this_or_next|troop_slot_ge,  ":troop_id", slot_troop_banner_scene_prop, 1),
              (eq, ":troop_no", "trp_player"),
              (assign, ":banner_troop", ":troop_id"),
            (else_try),
              (agent_get_party_id, ":agent_party", ":agent_no"),
              (try_begin),
                (lt, ":agent_party", 0),
                (is_between, ":troop_id", companions_begin, companions_end),
                (main_party_has_troop, ":troop_id"),
                (assign, ":agent_party", "p_main_party"),
              (try_end),
              (ge, ":agent_party", 0),
              (party_get_template_id, ":party_template", ":agent_party"),
              (try_begin),
                (eq, ":party_template", "pt_deserters"),
                (assign, ":banner_mesh", "mesh_banners_default_c"),
              (else_try),
                (is_between, ":agent_party", centers_begin, centers_end),
                (is_between, ":troop_id", companions_begin, companions_end),
                (neq, "$talk_context", tc_tavern_talk),
                #this should be a captured companion in prison
                (assign, ":banner_troop", "trp_player"),
              (else_try),
                (is_between, ":agent_party", centers_begin, centers_end),
                (party_get_slot, ":town_lord", "$g_encountered_party", slot_town_lord),
                (ge, ":town_lord", 0),
                (assign, ":banner_troop", ":town_lord"),
              (else_try),
                (this_or_next|party_slot_eq, ":agent_party", slot_party_type, spt_kingdom_hero_party),
                (eq, ":agent_party", "p_main_party"),
                (party_get_num_companion_stacks, ":num_stacks", ":agent_party"),
                (gt, ":num_stacks", 0),
                (party_stack_get_troop_id, ":leader_troop_id", ":agent_party", 0),
                (this_or_next|troop_slot_ge,  ":leader_troop_id", slot_troop_banner_scene_prop, 1),
                (eq, ":leader_troop_id", "trp_player"),
                (assign, ":banner_troop", ":leader_troop_id"),
              (try_end),
            (else_try), #Check if we are in a tavern
              (eq, "$talk_context", tc_tavern_talk),
              (neq, ":troop_no", "trp_player"),
              (assign, ":banner_mesh", "mesh_banners_default_d"),
            (else_try), #can't find party, this can be a town guard
              (neq, ":troop_no", "trp_player"),
              (is_between, "$g_encountered_party", walled_centers_begin, walled_centers_end),
              (party_get_slot, ":town_lord", "$g_encountered_party", slot_town_lord),
              (ge, ":town_lord", 0),
              (assign, ":banner_troop", ":town_lord"),
            (try_end),
            (try_begin),
              (ge, ":banner_troop", 0),
              (try_begin),
                (neg|troop_slot_ge, ":banner_troop", slot_troop_banner_scene_prop, 1),
                (assign, ":banner_mesh", "mesh_banners_default_b"),
              (else_try),
                (troop_get_slot, ":banner_spr", ":banner_troop", slot_troop_banner_scene_prop),
                (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
                (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
                (val_sub, ":banner_spr", banner_scene_props_begin),
                (store_add, ":banner_mesh", ":banner_spr", arms_meshes_begin),
              (try_end),
            (try_end),
            (assign, reg0, ":banner_mesh"),
        ]),
        #script_shield_item_set_banner
        # INPUT: agent_no
        # OUTPUT: none
        ("shield_item_set_banner",
          [
            (store_script_param, ":tableau_no",1),
            (store_script_param, ":agent_no", 2),
            (store_script_param, ":troop_no", 3),
            (call_script, "script_agent_troop_get_banner_mesh", ":agent_no", ":troop_no"),
            (cur_item_set_tableau_material, ":tableau_no", reg0),
        ]),
        
        
        #script_troop_agent_set_banner
        # INPUT: agent_no
        # OUTPUT: none
        ("troop_agent_set_banner",
          [
            (store_script_param, ":tableau_no",1),
            (store_script_param, ":agent_no", 2),
            (store_script_param, ":troop_no", 3),
            (call_script, "script_agent_troop_get_banner_mesh", ":agent_no", ":troop_no"),
            (cur_agent_set_banner_tableau_material, ":tableau_no", reg0),
        ]),
        
        ##  #script_shield_item_set_banner
        ##  # INPUT: agent_no
        ##  # OUTPUT: none
        ##  ("shield_item_set_banner",
        ##    [
        ##       (store_script_param, ":tableau_no",1),
        ##       (store_script_param, ":agent_no", 2),
        ##       (store_script_param, ":troop_no", 3),
        ##       (assign, ":banner_troop", -1),
        ##       (try_begin),
        ##         (lt, ":agent_no", 0),
        ##         (try_begin),
        ##           (ge, ":troop_no", 0),
        ##           (troop_slot_ge, ":troop_no", slot_troop_banner_scene_prop, 0),
        ##           (assign, ":banner_troop", ":troop_no"),
        ##         (else_try),
        ##           (assign, ":banner_troop", -2),
        ##         (try_end),
        ##       (else_try),
        ##         (agent_get_troop_id, ":troop_id", ":agent_no"),
        ##         (troop_slot_ge,  ":troop_id", slot_troop_custom_banner_flag_type, 0),
        ##         (assign, ":banner_troop", ":troop_id"),
        ##       (else_try),
        ##         (agent_get_party_id, ":agent_party", ":agent_no"),
        ##         (try_begin),
        ##           (lt, ":agent_party", 0),
        ##           (is_between, ":troop_id", companions_begin, companions_end),
        ##           (main_party_has_troop, ":troop_id"),
        ##           (assign, ":agent_party", "p_main_party"),
        ##         (try_end),
        ##         (ge, ":agent_party", 0),
        ##         (party_get_template_id, ":party_template", ":agent_party"),
        ##         (try_begin),
        ##           (eq, ":party_template", "pt_deserters"),
        ##           (assign, ":banner_troop", -3),
        ##         (else_try),
        ##           (is_between, ":agent_party", centers_begin, centers_end),
        ##           (party_get_slot, ":town_lord", "$g_encountered_party", slot_town_lord),
        ##           (ge, ":town_lord", 0),
        ##           (assign, ":banner_troop", ":town_lord"),
        ##         (else_try),
        ##           (this_or_next|party_slot_eq, ":agent_party", slot_party_type, spt_kingdom_hero_party),
        ##           (             eq, ":agent_party", "p_main_party"),
        ##           (party_get_num_companion_stacks, ":num_stacks", ":agent_party"),
        ##           (gt, ":num_stacks", 0),
        ##           (party_stack_get_troop_id, ":leader_troop_id", ":agent_party", 0),
        ##           (troop_slot_ge,  ":leader_troop_id", slot_troop_banner_scene_prop, 1),
        ##           (assign, ":banner_troop", ":leader_troop_id"),
        ##         (try_end),
        ##       (else_try), #Check if we are in a tavern
        ##         (eq, "$talk_context", tc_tavern_talk),
        ##         (neq, ":troop_no", "trp_player"),
        ##         (assign, ":banner_troop", -4),
        ##       (else_try), #can't find party, this can be a town guard
        ##         (neq, ":troop_no", "trp_player"),
        ##         (is_between, "$g_encountered_party", walled_centers_begin, walled_centers_end),
        ##         (party_get_slot, ":town_lord", "$g_encountered_party", slot_town_lord),
        ##         (ge, ":town_lord", 0),
        ##         (assign, ":banner_troop", ":town_lord"),
        ##       (try_end),
        ##       (cur_item_set_tableau_material, ":tableau_no", ":banner_troop"),
        ##     ]),
        
        #script_add_troop_to_cur_tableau
        # INPUT: troop_no
        # OUTPUT: none
        ("add_troop_to_cur_tableau",
          [
            (store_script_param, ":troop_no",1),
            
            (set_fixed_point_multiplier, 100),
            (assign, ":banner_mesh", -1),
            (troop_get_slot, ":banner_spr", ":troop_no", slot_troop_banner_scene_prop),
            (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
            (try_begin),
              (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
              (val_sub, ":banner_spr", banner_scene_props_begin),
              (store_add, ":banner_mesh", ":banner_spr", banner_meshes_begin),
            (try_end),
            
            (cur_tableau_clear_override_items),
            
            #       (cur_tableau_set_override_flags, af_override_fullhelm),
            (cur_tableau_set_override_flags, af_override_head|af_override_weapons),
            
            (init_position, pos2),
            (cur_tableau_set_camera_parameters, 1, 6, 6, 10, 10000),
            
            (init_position, pos5),
            (assign, ":eye_height", 162),
            (store_mul, ":camera_distance", ":troop_no", 87323),
            #       (val_mod, ":camera_distance", 5),
            (assign, ":camera_distance", 139),
            (store_mul, ":camera_yaw", ":troop_no", 124337),
            (val_mod, ":camera_yaw", 50),
            (val_add, ":camera_yaw", -25),
            (store_mul, ":camera_pitch", ":troop_no", 98123),
            (val_mod, ":camera_pitch", 20),
            (val_add, ":camera_pitch", -14),
            (assign, ":animation", "anim_stand_man"),
            
            ##       (troop_get_inventory_slot, ":horse_item", ":troop_no", ek_horse),
            ##       (try_begin),
            ##         (gt, ":horse_item", 0),
            ##         (assign, ":eye_height", 210),
            ##         (cur_tableau_add_horse, ":horse_item", pos2, anim_horse_stand, 0),
            ##         (assign, ":animation", anim_ride_0),
            ##         (position_set_z, pos5, 125),
            ##         (try_begin),
            ##           (is_between, ":camera_yaw", -10, 10), #make sure horse head doesn't obstruct face.
            ##           (val_min, ":camera_pitch", -5),
            ##         (try_end),
            ##       (try_end),
            (position_set_z, pos5, ":eye_height"),
            
            # camera looks towards -z axis
            (position_rotate_x, pos5, -90),
            (position_rotate_z, pos5, 180),
            
            # now apply yaw and pitch
            (position_rotate_y, pos5, ":camera_yaw"),
            (position_rotate_x, pos5, ":camera_pitch"),
            (position_move_z, pos5, ":camera_distance", 0),
            (position_move_x, pos5, 5, 0),
            
            (try_begin),
              (ge, ":banner_mesh", 0),
              
              (init_position, pos1),
              (position_set_z, pos1, -1500),
              (position_set_x, pos1, 265),
              (position_set_y, pos1, 400),
              (position_transform_position_to_parent, pos3, pos5, pos1),
              (cur_tableau_add_mesh, ":banner_mesh", pos3, 400, 0),
            (try_end),
            (cur_tableau_add_troop, ":troop_no", pos2, ":animation" , 0),
            
            (cur_tableau_set_camera_position, pos5),
            
            (copy_position, pos8, pos5),
            (position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
            (position_rotate_z, pos8, 30),
            (position_rotate_x, pos8, -60),
            (cur_tableau_add_sun_light, pos8, 175,150,125),
        ]),
        
        #script_add_troop_to_cur_tableau_for_character
        # INPUT: troop_no
        # OUTPUT: none
        ("add_troop_to_cur_tableau_for_character",
          [
            (store_script_param, ":troop_no",1),
            
            (set_fixed_point_multiplier, 100),
            
            (cur_tableau_clear_override_items),
            (cur_tableau_set_override_flags, af_override_fullhelm),
            ##       (cur_tableau_set_override_flags, af_override_head|af_override_weapons),
            
            (init_position, pos2),
            (cur_tableau_set_camera_parameters, 1, 4, 8, 10, 10000),
            
            (init_position, pos5),
            (assign, ":cam_height", 150),
            #       (val_mod, ":camera_distance", 5),
            (assign, ":camera_distance", 360),
            (assign, ":camera_yaw", -15),
            (assign, ":camera_pitch", -18),
            (assign, ":animation", anim_stand_man),
            
            ## Companions Overview, by Jedediah Q, modified by lazeras
            (try_begin),
              (eq, "$jq_override", 1),
              (cur_tableau_clear_override_items),
              (cur_tableau_set_override_flags, af_override_horse),
              (assign, ":animation", anim_stand_lord),
              (assign, ":camera_distance", 360),
              (assign, ":camera_yaw", -15),
              (assign, ":camera_pitch", -7),
            (try_end),
            ##
            
            (position_set_z, pos5, ":cam_height"),
            
            # camera looks towards -z axis
            (position_rotate_x, pos5, -90),
            (position_rotate_z, pos5, 180),
            
            # now apply yaw and pitch
            (position_rotate_y, pos5, ":camera_yaw"),
            (position_rotate_x, pos5, ":camera_pitch"),
            (position_move_z, pos5, ":camera_distance", 0),
            (position_move_x, pos5, 5, 0),
            
            (try_begin),
              (troop_is_hero, ":troop_no"),
              (cur_tableau_add_troop, ":troop_no", pos2, ":animation", -1),
            (else_try),
              (store_mul, ":random_seed", ":troop_no", 126233),
              (val_mod, ":random_seed", 1000),
              (val_add, ":random_seed", 1),
              (cur_tableau_add_troop, ":troop_no", pos2, ":animation", ":random_seed"),
            (try_end),
            (cur_tableau_set_camera_position, pos5),
            
            (copy_position, pos8, pos5),
            (position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
            (position_rotate_z, pos8, 30),
            (position_rotate_x, pos8, -60),
            (cur_tableau_add_sun_light, pos8, 175,150,125),
        ]),
        
        #script_add_troop_to_cur_tableau_for_inventory
        # INPUT: troop_no
        # OUTPUT: none
        ("add_troop_to_cur_tableau_for_inventory",
          [
            (store_script_param, ":troop_no",1),
            (store_mod, ":side", ":troop_no", 4), #side flag is inside troop_no value
            (val_div, ":troop_no", 4), #removing the flag bit
            (val_mul, ":side", 90), #to degrees
            
            (set_fixed_point_multiplier, 100),
            
            (cur_tableau_clear_override_items),
            
            (init_position, pos2),
            (position_rotate_z, pos2, ":side"),
            (cur_tableau_set_camera_parameters, 1, 4, 6, 10, 10000),
            
            (init_position, pos5),
            (assign, ":cam_height", 105),
            #       (val_mod, ":camera_distance", 5),
            (assign, ":camera_distance", 380),
            (assign, ":camera_yaw", -15),
            (assign, ":camera_pitch", -18),
            (assign, ":animation", anim_stand_man),
            
            (position_set_z, pos5, ":cam_height"),
            
            # camera looks towards -z axis
            (position_rotate_x, pos5, -90),
            (position_rotate_z, pos5, 180),
            
            # now apply yaw and pitch
            (position_rotate_y, pos5, ":camera_yaw"),
            (position_rotate_x, pos5, ":camera_pitch"),
            (position_move_z, pos5, ":camera_distance", 0),
            (position_move_x, pos5, 5, 0),
            
            (try_begin),
              (troop_is_hero, ":troop_no"),
              (cur_tableau_add_troop, ":troop_no", pos2, ":animation", -1),
            (else_try),
              (store_mul, ":random_seed", ":troop_no", 126233),
              (val_mod, ":random_seed", 1000),
              (val_add, ":random_seed", 1),
              (cur_tableau_add_troop, ":troop_no", pos2, ":animation", ":random_seed"),
            (try_end),
            (cur_tableau_set_camera_position, pos5),
            
            (copy_position, pos8, pos5),
            (position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
            (position_rotate_z, pos8, 30),
            (position_rotate_x, pos8, -60),
            (cur_tableau_add_sun_light, pos8, 175,150,125),
        ]),
        
        #script_add_troop_to_cur_tableau_for_profile
        # INPUT: troop_no
        # OUTPUT: none
        ("add_troop_to_cur_tableau_for_profile",
          [
            (store_script_param, ":troop_no",1),
            
            (set_fixed_point_multiplier, 100),
            
            (cur_tableau_clear_override_items),
            
            (cur_tableau_set_camera_parameters, 1, 4, 6, 10, 10000),
            
            (init_position, pos5),
            (assign, ":cam_height", 105),
            #       (val_mod, ":camera_distance", 5),
            (assign, ":camera_distance", 380),
            (assign, ":camera_yaw", -15),
            (assign, ":camera_pitch", -18),
            (assign, ":animation", anim_stand_man),
            
            (position_set_z, pos5, ":cam_height"),
            
            # camera looks towards -z axis
            (position_rotate_x, pos5, -90),
            (position_rotate_z, pos5, 180),
            
            # now apply yaw and pitch
            (position_rotate_y, pos5, ":camera_yaw"),
            (position_rotate_x, pos5, ":camera_pitch"),
            (position_move_z, pos5, ":camera_distance", 0),
            (position_move_x, pos5, 5, 0),
            
            (profile_get_banner_id, ":profile_banner"),
            (try_begin),
              (ge, ":profile_banner", 0),
              (init_position, pos2),
              (val_add, ":profile_banner", banner_meshes_begin),
              (position_set_x, pos2, -175),
              (position_set_y, pos2, -300),
              (position_set_z, pos2, 180),
              (position_rotate_x, pos2, 90),
              (position_rotate_y, pos2, -15),
              (cur_tableau_add_mesh, ":profile_banner", pos2, 0, 0),
            (try_end),
            
            (init_position, pos2),
            (try_begin),
              (troop_is_hero, ":troop_no"),
              (cur_tableau_add_troop, ":troop_no", pos2, ":animation", -1),
            (else_try),
              (store_mul, ":random_seed", ":troop_no", 126233),
              (val_mod, ":random_seed", 1000),
              (val_add, ":random_seed", 1),
              (cur_tableau_add_troop, ":troop_no", pos2, ":animation", ":random_seed"),
            (try_end),
            (cur_tableau_set_camera_position, pos5),
            
            (copy_position, pos8, pos5),
            (position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
            (position_rotate_z, pos8, 30),
            (position_rotate_x, pos8, -60),
            (cur_tableau_add_sun_light, pos8, 175,150,125),
        ]),
        
        #script_add_troop_to_cur_tableau_for_retirement
        # INPUT: type
        # OUTPUT: none
        ("add_troop_to_cur_tableau_for_retirement", [
            (store_script_param, ":type", 1),
            (cur_tableau_set_override_flags, af_override_everything),
            
            (try_begin),
              (eq, ":type", 0),
              (cur_tableau_add_override_item, "itm_he_pla_pri_pilgrim"),
              (cur_tableau_add_override_item, "itm_ar_pla_pri_pilgrimdisguise"),
              (cur_tableau_add_override_item, "itm_bo_swa_t3_wrapping"),
              (assign, ":animation", "anim_pose_1"),
            (else_try),
              (eq, ":type", 1),
              (cur_tableau_add_override_item, "itm_he_pla_pri_pilgrim"),
              (cur_tableau_add_override_item, "itm_arena_tunic_red"),
              (cur_tableau_add_override_item, "itm_bo_swa_t3_wrapping"),
              (cur_tableau_add_override_item, "itm_we_swa_sword_clamshelldagger"),
              (assign, ":animation", "anim_pose_1"),
            (else_try),
              (eq, ":type", 2),
              (cur_tableau_add_override_item, "itm_ar_swa_shi_linen"),
              (cur_tableau_add_override_item, "itm_bo_swa_t3_wrapping"),
              (assign, ":animation", "anim_pose_2"),
            (else_try),
              (eq, ":type", 3),
              (cur_tableau_add_override_item, "itm_ar_khe_mer_nomadvest"),
              (cur_tableau_add_override_item, "itm_bo_nor_t3_boots"),
              (assign, ":animation", "anim_pose_2"),
            (else_try),
              (eq, ":type", 4),
              (cur_tableau_add_override_item, "itm_ar_pla_mer_leatherapron"),
              (cur_tableau_add_override_item, "itm_bo_vae_t3_leather"),
              (assign, ":animation", "anim_pose_3"),
            (else_try),
              (eq, ":type", 5),
              (cur_tableau_add_override_item, "itm_ar_vae_tun_red"),
              (cur_tableau_add_override_item, "itm_bo_swa_t2_hose"),
              (cur_tableau_add_override_item, "itm_he_vae_t2_furcap_a"),
              (assign, ":animation", "anim_pose_3"),
            (else_try),
              (eq, ":type", 6),
              (cur_tableau_add_override_item, "itm_ar_swa_t2_gambeson_a"),
              (cur_tableau_add_override_item, "itm_bo_vae_t3_leather"),
              (cur_tableau_add_override_item, "itm_we_swa_sword_clamshell"),
              (assign, ":animation", "anim_pose_4"),
            (else_try),
              (eq, ":type", 7),
              (cur_tableau_add_override_item, "itm_ar_vae_nob_outfit"),
              (cur_tableau_add_override_item, "itm_bo_pla_t1_priest"),
              (cur_tableau_add_override_item, "itm_we_vae_sword_jarl"),
              (assign, ":animation", "anim_pose_4"),
            (else_try),
              (eq, ":type", 8),
              (cur_tableau_add_override_item, "itm_ar_swa_nob_outfit"),
              (cur_tableau_add_override_item, "itm_bo_swa_t2_hose"),
              (cur_tableau_add_override_item, "itm_we_swa_sword_knight"),
              (assign, ":animation", "anim_pose_4"),
            (else_try),
              ##      (eq, ":type", 9),
              (cur_tableau_add_override_item, "itm_ar_pla_t5_mailsurcoat_tableau"),
              (cur_tableau_add_override_item, "itm_bo_swa_t6_mail"),
              (cur_tableau_add_override_item, "itm_we_pla_sword_reeve"),
              (assign, ":animation", "anim_pose_5"),
              ##    (else_try), #not used
              ##      (cur_tableau_add_override_item, "itm_heraldic_mail_with_tabard"),
              ##      (cur_tableau_add_override_item, "itm_iron_greaves"),
              ##      (cur_tableau_add_override_item, "itm_sword_medieval_c"),
              ##      (assign, ":animation", "anim_pose_5"),
            (try_end),
            
            ##    (set_fixed_point_multiplier, 100),
            ##    (cur_tableau_set_background_color, 0x00000000),
            ##    (cur_tableau_set_ambient_light, 10,11,15),
            
            ##     (init_position, pos8),
            ##     (position_set_x, pos8, -210),
            ##     (position_set_y, pos8, 200),
            ##     (position_set_z, pos8, 300),
            ##     (cur_tableau_add_point_light, pos8, 550,500,450),
            
            
            (set_fixed_point_multiplier, 100),
            (cur_tableau_set_camera_parameters, 1, 6, 6, 10, 10000),
            (assign, ":cam_height", 155),
            (assign, ":camera_distance", 575),
            (assign, ":camera_yaw", -5),
            (assign, ":camera_pitch", 10),
            
            (init_position, pos5),
            (position_set_z, pos5, ":cam_height"),
            # camera looks towards -z axis
            (position_rotate_x, pos5, -90),
            (position_rotate_z, pos5, 180),
            # now apply yaw and pitch
            (position_rotate_y, pos5, ":camera_yaw"),
            (position_rotate_x, pos5, ":camera_pitch"),
            (position_move_z, pos5, ":camera_distance", 0),
            (position_move_x, pos5, 60, 0),
            
            (init_position, pos2),
            (cur_tableau_add_troop, "trp_player", pos2, ":animation", 0),
            (cur_tableau_set_camera_position, pos5),
            
            (copy_position, pos8, pos5),
            (position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
            (position_rotate_z, pos8, 30),
            (position_rotate_x, pos8, -60),
            (cur_tableau_add_sun_light, pos8, 175,150,125),
        ]),
        
        #script_add_troop_to_cur_tableau_for_party
        # INPUT: troop_no
        # OUTPUT: none
        ("add_troop_to_cur_tableau_for_party",
          [
            (store_script_param, ":troop_no",1),
            (store_mod, ":hide_weapons", ":troop_no", 2), #hide_weapons flag is inside troop_no value
            (val_div, ":troop_no", 2), #removing the flag bit
            
            (set_fixed_point_multiplier, 100),
            
            (cur_tableau_clear_override_items),
            (try_begin),
              (eq, ":hide_weapons", 1),
              (cur_tableau_set_override_flags, af_override_fullhelm|af_override_head|af_override_weapons),
            (try_end),
            
            (init_position, pos2),
            (cur_tableau_set_camera_parameters, 1, 6, 6, 10, 10000),
            
            (init_position, pos5),
            (assign, ":cam_height", 105),
            #       (val_mod, ":camera_distance", 5),
            (assign, ":camera_distance", 450),
            (assign, ":camera_yaw", 15),
            (assign, ":camera_pitch", -18),
            (assign, ":animation", anim_stand_man),
            
            (troop_get_inventory_slot, ":horse_item", ":troop_no", ek_horse),
            (try_begin),
              (gt, ":horse_item", 0),
              (eq, ":hide_weapons", 0),
              (cur_tableau_add_horse, ":horse_item", pos2, "anim_horse_stand", 0),
              (assign, ":animation", "anim_ride_0"),
              (assign, ":camera_yaw", 23),
              (assign, ":cam_height", 150),
              (assign, ":camera_distance", 550),
            (try_end),
            (position_set_z, pos5, ":cam_height"),
            
            # camera looks towards -z axis
            (position_rotate_x, pos5, -90),
            (position_rotate_z, pos5, 180),
            
            # now apply yaw and pitch
            (position_rotate_y, pos5, ":camera_yaw"),
            (position_rotate_x, pos5, ":camera_pitch"),
            (position_move_z, pos5, ":camera_distance", 0),
            (position_move_x, pos5, 5, 0),
            
            (try_begin),
              (troop_is_hero, ":troop_no"),
              (cur_tableau_add_troop, ":troop_no", pos2, ":animation", -1),
            (else_try),
              (store_mul, ":random_seed", ":troop_no", 126233),
              (val_mod, ":random_seed", 1000),
              (val_add, ":random_seed", 1),
              (cur_tableau_add_troop, ":troop_no", pos2, ":animation", ":random_seed"),
            (try_end),
            (cur_tableau_set_camera_position, pos5),
            
            (copy_position, pos8, pos5),
            (position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
            (position_rotate_z, pos8, 30),
            (position_rotate_x, pos8, -60),
            (cur_tableau_add_sun_light, pos8, 175,150,125),
        ]),
        
        #script_get_prosperity_text_to_s50
        # INPUT: center_no
        # OUTPUT: none
        ("get_prosperity_text_to_s50",
          [(store_script_param, ":center_no", 1),
            (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
            (val_div, ":prosperity", 20),
            (try_begin),
              (eq, ":prosperity", 0), #0..19
              (str_store_string, s50, "@Very Poor"),
            (else_try),
              (eq, ":prosperity", 1), #20..39
              (str_store_string, s50, "@Poor"),
            (else_try),
              (eq, ":prosperity", 2), #40..59
              (str_store_string, s50, "@Average"),
            (else_try),
              (eq, ":prosperity", 3), #60..79
              (str_store_string, s50, "@Rich"),
            (else_try),
              (str_store_string, s50, "@Very Rich"), #80..99
            (try_end),
        ]),
        
        #script_spawn_bandits
        # INPUT: none
        # OUTPUT: none
        ("spawn_bandits",
          [
            (set_spawn_radius,1),
            
            (try_begin),
              (eq, "$cheat_mode", 1),
              (display_message, "@{!}DEBUG : Doing spawn bandit script"),
            (try_end),
            
				##Floris MTT begin
				(try_begin),
		 			(eq, "$troop_trees", troop_trees_0),
					(party_template_set_slot, "pt_steppe_bandits", slot_party_template_lair_type, "pt_steppe_bandit_lair"),
					(party_template_set_slot, "pt_taiga_bandits", slot_party_template_lair_type, "pt_taiga_bandit_lair"),
					(party_template_set_slot, "pt_mountain_bandits", slot_party_template_lair_type, "pt_mountain_bandit_lair"),
					(party_template_set_slot, "pt_forest_bandits", slot_party_template_lair_type, "pt_forest_bandit_lair"),
					(party_template_set_slot, "pt_sea_raiders", slot_party_template_lair_type, "pt_sea_raider_lair"),
					(party_template_set_slot, "pt_desert_bandits", slot_party_template_lair_type, "pt_desert_bandit_lair"),
					
					(party_template_set_slot, "pt_steppe_bandits", slot_party_template_lair_spawnpoint, "p_steppe_bandit_spawn_point"),
					(party_template_set_slot, "pt_taiga_bandits", slot_party_template_lair_spawnpoint, "p_taiga_bandit_spawn_point"),
					(party_template_set_slot, "pt_mountain_bandits", slot_party_template_lair_spawnpoint, "p_mountain_bandit_spawn_point"),
					(party_template_set_slot, "pt_forest_bandits", slot_party_template_lair_spawnpoint, "p_forest_bandit_spawn_point"),
					(party_template_set_slot, "pt_sea_raiders", slot_party_template_lair_spawnpoint, "p_sea_raider_spawn_point_1"),
					(party_template_set_slot, "pt_desert_bandits", slot_party_template_lair_spawnpoint, "p_desert_bandit_spawn_point"),
				(else_try),
		 			(eq, "$troop_trees", troop_trees_1),
					(party_template_set_slot, "pt_steppe_bandits_r", slot_party_template_lair_type, "pt_steppe_bandit_lair_r"),
					(party_template_set_slot, "pt_taiga_bandits_r", slot_party_template_lair_type, "pt_taiga_bandit_lair_r"),
					(party_template_set_slot, "pt_mountain_bandits_r", slot_party_template_lair_type, "pt_mountain_bandit_lair_r"),
					(party_template_set_slot, "pt_forest_bandits_r", slot_party_template_lair_type, "pt_forest_bandit_lair_r"),
					(party_template_set_slot, "pt_sea_raiders_r", slot_party_template_lair_type, "pt_sea_raider_lair_r"),
					(party_template_set_slot, "pt_desert_bandits_r", slot_party_template_lair_type, "pt_desert_bandit_lair_r"),
					
					(party_template_set_slot, "pt_steppe_bandits_r", slot_party_template_lair_spawnpoint, "p_steppe_bandit_spawn_point"),
					(party_template_set_slot, "pt_taiga_bandits_r", slot_party_template_lair_spawnpoint, "p_taiga_bandit_spawn_point"),
					(party_template_set_slot, "pt_mountain_bandits_r", slot_party_template_lair_spawnpoint, "p_mountain_bandit_spawn_point"),
					(party_template_set_slot, "pt_forest_bandits_r", slot_party_template_lair_spawnpoint, "p_forest_bandit_spawn_point"),
					(party_template_set_slot, "pt_sea_raiders_r", slot_party_template_lair_spawnpoint, "p_sea_raider_spawn_point_1"),
					(party_template_set_slot, "pt_desert_bandits_r", slot_party_template_lair_spawnpoint, "p_desert_bandit_spawn_point"),
				(else_try),
					(eq, "$troop_trees", troop_trees_2),
					(party_template_set_slot, "pt_steppe_bandits_e", slot_party_template_lair_type, "pt_steppe_bandit_lair_e"),
					(party_template_set_slot, "pt_taiga_bandits_e", slot_party_template_lair_type, "pt_taiga_bandit_lair_e"),
					(party_template_set_slot, "pt_mountain_bandits_e", slot_party_template_lair_type, "pt_mountain_bandit_lair_e"),
					(party_template_set_slot, "pt_forest_bandits_e", slot_party_template_lair_type, "pt_forest_bandit_lair_e"),
					(party_template_set_slot, "pt_sea_raiders_e", slot_party_template_lair_type, "pt_sea_raider_lair_e"),
					(party_template_set_slot, "pt_desert_bandits_e", slot_party_template_lair_type, "pt_desert_bandit_lair_e"),
					
					(party_template_set_slot, "pt_steppe_bandits_e", slot_party_template_lair_spawnpoint, "p_steppe_bandit_spawn_point"),
					(party_template_set_slot, "pt_taiga_bandits_e", slot_party_template_lair_spawnpoint, "p_taiga_bandit_spawn_point"),
					(party_template_set_slot, "pt_mountain_bandits_e", slot_party_template_lair_spawnpoint, "p_mountain_bandit_spawn_point"),
					(party_template_set_slot, "pt_forest_bandits_e", slot_party_template_lair_spawnpoint, "p_forest_bandit_spawn_point"),
					(party_template_set_slot, "pt_sea_raiders_e", slot_party_template_lair_spawnpoint, "p_sea_raider_spawn_point_1"),
					(party_template_set_slot, "pt_desert_bandits_e", slot_party_template_lair_spawnpoint, "p_desert_bandit_spawn_point"),
				(try_end),
				##Floris MTT end
            
            (try_begin),
				##Floris MTT begin
				(try_begin),
		 			(eq, "$troop_trees", troop_trees_0),
					  (store_num_parties_of_template, ":num_parties", "pt_mountain_bandits"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_mountain_bandit_spawn_points),
					  (val_add,":spawn_point","p_mountain_bandit_spawn_point"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_mountain_bandits"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_mountain_bandits", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_mountain_bandits"),
                     ## CC
				(else_try),
		 			(eq, "$troop_trees", troop_trees_1),
					  (store_num_parties_of_template, ":num_parties", "pt_mountain_bandits_r"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_mountain_bandit_spawn_points),
					  (val_add,":spawn_point","p_mountain_bandit_spawn_point"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_mountain_bandits_r"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_mountain_bandits_r", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_mountain_bandits_r"),
                     ## CC
				(else_try),
					(eq, "$troop_trees", troop_trees_2),
					  (store_num_parties_of_template, ":num_parties", "pt_mountain_bandits_e"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_mountain_bandit_spawn_points),
					  (val_add,":spawn_point","p_mountain_bandit_spawn_point"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_mountain_bandits_e"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_mountain_bandits_e", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_mountain_bandits_e"),
                     ## CC
				(try_end),
				##Floris MTT end
            (try_end),

	 #Wulf
    (try_begin),
				##Floris MTT begin
				(try_begin),
		 			(eq, "$troop_trees", troop_trees_0),
					(store_num_parties_of_template, ":num_parties", "pt_sea_raiders_ships"),
					(lt,":num_parties",18),
					(store_random,":spawn_point",num_mountain_bandit_spawn_points),
					(val_add,":spawn_point","p_ship_raider_spawn_point_1"),
					(spawn_around_party, ":spawn_point", "pt_sea_raiders_ships"),
				(else_try),
		 			(eq, "$troop_trees", troop_trees_1),
					(store_num_parties_of_template, ":num_parties", "pt_sea_raiders_ships_r"),
					(lt,":num_parties",18),
					(store_random,":spawn_point",num_mountain_bandit_spawn_points),
					(val_add,":spawn_point","p_ship_raider_spawn_point_1"),
					(spawn_around_party, ":spawn_point", "pt_sea_raiders_ships_r"),
				(else_try),
					(eq, "$troop_trees", troop_trees_2),
					(store_num_parties_of_template, ":num_parties", "pt_sea_raiders_ships_e"),
					(lt,":num_parties",18),
					(store_random,":spawn_point",num_mountain_bandit_spawn_points),
					(val_add,":spawn_point","p_ship_raider_spawn_point_1"),
					(spawn_around_party, ":spawn_point", "pt_sea_raiders_ships_e"),
				(try_end),
				##Floris MTT end
    (try_end),
     #Wulf end        
	 
            (try_begin),
				##Floris MTT begin
				(try_begin),
		 			(eq, "$troop_trees", troop_trees_0),
					  (store_num_parties_of_template, ":num_parties", "pt_forest_bandits"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_forest_bandit_spawn_points),
					  (val_add,":spawn_point","p_forest_bandit_spawn_point"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_forest_bandits"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_forest_bandits", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_forest_bandits"),
                     ## CC
				(else_try),
		 			(eq, "$troop_trees", troop_trees_1),
					  (store_num_parties_of_template, ":num_parties", "pt_forest_bandits_r"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_forest_bandit_spawn_points),
					  (val_add,":spawn_point","p_forest_bandit_spawn_point"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_forest_bandits_r"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_forest_bandits_r", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_forest_bandits_r"),
                     ## CC
				(else_try),
					(eq, "$troop_trees", troop_trees_2),
					  (store_num_parties_of_template, ":num_parties", "pt_forest_bandits_e"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_forest_bandit_spawn_points),
					  (val_add,":spawn_point","p_forest_bandit_spawn_point"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_forest_bandits_e"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_forest_bandits_e", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_forest_bandits_e"),
                     ## CC
				(try_end),
				##Floris MTT end
            (try_end),
            (try_begin),
				##Floris MTT begin
				(try_begin),
		 			(eq, "$troop_trees", troop_trees_0),
					  (store_num_parties_of_template, ":num_parties", "pt_sea_raiders"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_sea_raider_spawn_points),
					  (val_add,":spawn_point","p_sea_raider_spawn_point_1"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_sea_raiders"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_sea_raiders", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_sea_raiders"),
                     ## CC
				(else_try),
		 			(eq, "$troop_trees", troop_trees_1),
					  (store_num_parties_of_template, ":num_parties", "pt_sea_raiders_r"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_sea_raider_spawn_points),
					  (val_add,":spawn_point","p_sea_raider_spawn_point_1"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_sea_raiders_r"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_sea_raiders_r", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_sea_raiders_r"),
                     ## CC
				(else_try),
					(eq, "$troop_trees", troop_trees_2),
					  (store_num_parties_of_template, ":num_parties", "pt_sea_raiders_e"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_sea_raider_spawn_points),
					  (val_add,":spawn_point","p_sea_raider_spawn_point_1"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_sea_raiders_e"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_sea_raiders_e", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_sea_raiders_e"),
                     ## CC
				(try_end),
				##Floris MTT end
            (try_end),
            (try_begin),
				##Floris MTT begin
				(try_begin),
		 			(eq, "$troop_trees", troop_trees_0),
					  (store_num_parties_of_template, ":num_parties", "pt_steppe_bandits"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_steppe_bandit_spawn_points),
					  (val_add,":spawn_point","p_steppe_bandit_spawn_point"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_steppe_bandits"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_steppe_bandits", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_steppe_bandits"),
                     ## CC
				(else_try),
		 			(eq, "$troop_trees", troop_trees_1),
					  (store_num_parties_of_template, ":num_parties", "pt_steppe_bandits_r"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_steppe_bandit_spawn_points),
					  (val_add,":spawn_point","p_steppe_bandit_spawn_point"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_steppe_bandits_r"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_steppe_bandits_r", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_steppe_bandits_r"),
                     ## CC
				(else_try),
					(eq, "$troop_trees", troop_trees_2),
					  (store_num_parties_of_template, ":num_parties", "pt_steppe_bandits_e"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_steppe_bandit_spawn_points),
					  (val_add,":spawn_point","p_steppe_bandit_spawn_point"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_steppe_bandits_e"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_steppe_bandits_e", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_steppe_bandits_e"),
                     ## CC
				(try_end),
				##Floris MTT end
            (try_end),
            (try_begin),
				##Floris MTT begin
				(try_begin),
		 			(eq, "$troop_trees", troop_trees_0),
					  (store_num_parties_of_template, ":num_parties", "pt_taiga_bandits"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_taiga_bandit_spawn_points),
					  (val_add,":spawn_point","p_taiga_bandit_spawn_point"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_taiga_bandits"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_taiga_bandits", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_taiga_bandits"),
                     ## CC
				(else_try),
		 			(eq, "$troop_trees", troop_trees_1),
					  (store_num_parties_of_template, ":num_parties", "pt_taiga_bandits_r"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_taiga_bandit_spawn_points),
					  (val_add,":spawn_point","p_taiga_bandit_spawn_point"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_taiga_bandits_r"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_taiga_bandits_r", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_taiga_bandits_r"),
                     ## CC
				(else_try),
					(eq, "$troop_trees", troop_trees_2),
					  (store_num_parties_of_template, ":num_parties", "pt_taiga_bandits_e"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_taiga_bandit_spawn_points),
					  (val_add,":spawn_point","p_taiga_bandit_spawn_point"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_taiga_bandits_e"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_taiga_bandits_e", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_taiga_bandits_e"),
                     ## CC
				(try_end),
				##Floris MTT end
            (try_end),
            (try_begin),
				##Floris MTT begin
				(try_begin),
		 			(eq, "$troop_trees", troop_trees_0),
					  (store_num_parties_of_template, ":num_parties", "pt_desert_bandits"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_desert_bandit_spawn_points),
					  (val_add,":spawn_point","p_desert_bandit_spawn_point"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_desert_bandits"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_desert_bandits", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_desert_bandits"),
                     ## CC
				(else_try),
		 			(eq, "$troop_trees", troop_trees_1),
					  (store_num_parties_of_template, ":num_parties", "pt_desert_bandits_r"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_desert_bandit_spawn_points),
					  (val_add,":spawn_point","p_desert_bandit_spawn_point"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_desert_bandits_r"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_desert_bandits_r", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_desert_bandits_r"),
                     ## CC
				(else_try),
					(eq, "$troop_trees", troop_trees_2),
					  (store_num_parties_of_template, ":num_parties", "pt_desert_bandits_e"),
					  (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
					  (store_random,":spawn_point",num_desert_bandit_spawn_points),
					  (val_add,":spawn_point","p_desert_bandit_spawn_point"),
					  (set_spawn_radius, 25),
					  (spawn_around_party,":spawn_point","pt_desert_bandits_e"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_desert_bandits_e", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_desert_bandits_e"),
                     ## CC
				(try_end),
				##Floris MTT end
            (try_end),
            (try_begin),
				##Floris MTT begin
				(try_begin),
		 			(eq, "$troop_trees", troop_trees_0),
					(store_num_parties_of_template, ":num_parties", "pt_looters"),
				(else_try),
		 			(eq, "$troop_trees", troop_trees_1),
					(store_num_parties_of_template, ":num_parties", "pt_looters_r"),
				(else_try),
					(eq, "$troop_trees", troop_trees_2),
					(store_num_parties_of_template, ":num_parties", "pt_looters_e"),
				(try_end),
				##Floris MTT end
              (lt,":num_parties",42), #was 33 at mount&blade, 50 in warband, 42 last decision
              (store_random_in_range,":spawn_point",villages_begin,villages_end), #spawn looters twice to have lots of them at the beginning
              (set_spawn_radius, 25),
				##Floris MTT begin
				(try_begin),
		 			(eq, "$troop_trees", troop_trees_0),
					(spawn_around_party,":spawn_point","pt_looters"),
				(else_try),
		 			(eq, "$troop_trees", troop_trees_1),
					(spawn_around_party,":spawn_point","pt_looters_r"),
				(else_try),
					(eq, "$troop_trees", troop_trees_2),
					(spawn_around_party,":spawn_point","pt_looters_e"),
				(try_end),
				##Floris MTT end
              (assign, ":spawned_party_id", reg0),
              (try_begin),
                (check_quest_active, "qst_deal_with_looters"),
                (party_set_flags, ":spawned_party_id", pf_quest_party, 1),
              (else_try),
                (party_set_flags, ":spawned_party_id", pf_quest_party, 0),
              (try_end),
            (try_end),
            (try_begin),
              (store_num_parties_of_template, ":num_parties", "pt_deserters"),
              (lt,":num_parties",15),
              (set_spawn_radius, 4),
              (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
                (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
                (store_random_in_range, ":random_no", 0, 100),
                (lt, ":random_no", 5),
                (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
                (store_troop_faction, ":troop_faction", ":troop_no"),
                (neq, ":troop_faction", "fac_player_supporters_faction"),
                (gt, ":party_no", 0),
                (neg|party_is_in_any_town, ":party_no"),
                ##         (party_get_attached_to, ":attached_party_no", ":party_no"),
                ##         (lt, ":attached_party_no", 0),#in wilderness
                (spawn_around_party, ":party_no", "pt_deserters"),
                (assign, ":new_party", reg0),
                (store_troop_faction, ":faction_no", ":troop_no"),
                (faction_get_slot, ":tier_1_troop", ":faction_no", slot_faction_tier_1_troop),
                (store_character_level, ":level", "trp_player"),
                (store_mul, ":max_number_to_add", ":level", 2),
                (val_add, ":max_number_to_add", 11),
                (store_random_in_range, ":number_to_add", 10, ":max_number_to_add"),
                (party_add_members, ":new_party", ":tier_1_troop", ":number_to_add"),
                (store_random_in_range, ":random_no", 1, 4),
                (try_for_range, ":unused", 0, ":random_no"),
                  (party_upgrade_with_xp, ":new_party", 1000000, 0),
                (try_end),
                ##         (str_store_party_name, s1, ":party_no"),
                ##         (call_script, "script_get_closest_center", ":party_no"),
                ##         (try_begin),
                ##           (gt, reg0, 0),
                ##           (str_store_party_name, s2, reg0),
                ##         (else_try),
                ##           (str_store_string, s2, "@unknown place"),
                ##         (try_end),
                ##         (assign, reg1, ":number_to_add"),
                ##         (display_message, "@{reg1} Deserters spawned from {s1}, near {s2}."),
              (try_end),
            (try_end), #deserters ends
            
            
            #Spawn bandit lairs
		  ##Floris MTT begin
			(try_begin),
				(eq, "$troop_trees", troop_trees_0),
				(assign, ":templates_begin", bandit_party_template_begin),
				(assign, ":templates_end", bandit_party_template_end),
			(else_try),
				(eq, "$troop_trees", troop_trees_1),
				(assign, ":templates_begin", bandit_party_template_r_begin),
				(assign, ":templates_end", bandit_party_template_r_end),
			(else_try),
				(eq, "$troop_trees", troop_trees_2),
				(assign, ":templates_begin", bandit_party_template_e_begin),
				(assign, ":templates_end", bandit_party_template_e_end),
			(try_end),
			(try_for_range, ":bandit_template", ":templates_begin", ":templates_end"), #changed from bandit_party_template_begin to bandit_party_template_end
			##Floris MTT end 
              (party_template_get_slot, ":bandit_lair_party", ":bandit_template", slot_party_template_lair_party),
              (le, ":bandit_lair_party", 1),
              
              (party_template_get_slot, ":bandit_lair_template", ":bandit_template", slot_party_template_lair_type),
              (party_template_get_slot, ":bandit_lair_template_spawnpoint", ":bandit_template", slot_party_template_lair_spawnpoint),
              
              (set_spawn_radius, 20),
              
              (spawn_around_party, ":bandit_lair_template_spawnpoint", ":bandit_lair_template"),
              (assign, ":new_camp", reg0),
              
              (party_set_slot, ":new_camp", slot_party_type, spt_bandit_lair),
              
              (str_store_party_name, s4, ":new_camp"),
              
              (party_get_position, pos4, ":new_camp"),
              #(party_set_flags, ":new_camp", pf_icon_mask, 1),
              
              (party_get_current_terrain, ":new_camp_terrain", ":new_camp"),
              (position_get_z, ":elevation", pos4),
              (position_get_y, ":lair_y", pos4),
              
              (assign, ":center_too_close", 0),
              (try_for_range, ":center", centers_begin, centers_end),
                (eq, ":center_too_close", 0),
                (store_distance_to_party_from_party, ":distance", ":new_camp", ":center"),
                (lt, ":distance", 3),
                (assign, ":center_too_close", 1),
              (try_end),
              
              (try_begin),
                (eq, ":center_too_close", 1),
                (party_is_active, ":new_camp"),
                (remove_party, ":new_camp"),
                (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, 0),
              (else_try),
				##Floris MTT begin
                (this_or_next|eq, ":bandit_template", "pt_sea_raiders"),
                (this_or_next|eq, ":bandit_template", "pt_sea_raiders_r"),
                (eq, ":bandit_template", "pt_sea_raiders_e"),
				##Floris MTT end
                (eq, ":new_camp_terrain", 3),
                (map_get_water_position_around_position, pos5, pos4, 4),
                (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, ":new_camp"),
                (party_set_flags, ":new_camp", pf_disabled, 1),
              (else_try),
				##Floris MTT begin
                (this_or_next|eq, ":bandit_template", "pt_mountain_bandits"),
                (this_or_next|eq, ":bandit_template", "pt_mountain_bandits_r"),
                (eq, ":bandit_template", "pt_mountain_bandits_e"),
				##Floris MTT end
                (eq, ":new_camp_terrain", 3),
                (gt, ":elevation", 250),
                (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, ":new_camp"),
                (party_set_flags, ":new_camp", pf_disabled, 1),
              (else_try),
				##Floris MTT begin
                (this_or_next|eq, ":bandit_template", "pt_desert_bandits"),
                (this_or_next|eq, ":bandit_template", "pt_desert_bandits_r"),
                (eq, ":bandit_template", "pt_desert_bandits_e"),
				##Floris MTT end
                (eq, ":new_camp_terrain", 5),
                (gt, ":lair_y", -9000),
                (gt, ":elevation", 125),
                (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, ":new_camp"),
                (party_set_flags, ":new_camp", pf_disabled, 1),
              (else_try),
				##Floris MTT begin
	            (this_or_next|eq, ":bandit_template", "pt_steppe_bandits"),
                (this_or_next|eq, ":bandit_template", "pt_steppe_bandits_r"),
                (eq, ":bandit_template", "pt_steppe_bandits_e"),
				##Floris MTT end
                (this_or_next|eq, ":new_camp_terrain", 2),
                (eq, ":new_camp_terrain", 10),
                (this_or_next|eq, ":new_camp_terrain", 10),
                (gt, ":elevation", 200),
                (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, ":new_camp"),
                (party_set_flags, ":new_camp", pf_disabled, 1),
              (else_try),
				##Floris MTT begin
                (this_or_next|eq, ":bandit_template", "pt_taiga_bandits"),
                (this_or_next|eq, ":bandit_template", "pt_taiga_bandits_r"),
                (eq, ":bandit_template", "pt_taiga_bandits_e"),
				##Floris MTT end
                (eq, ":new_camp_terrain", 12),
                (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, ":new_camp"),
                (party_set_flags, ":new_camp", pf_disabled, 1),
              (else_try),
				##Floris MTT begin
                (this_or_next|eq, ":bandit_template", "pt_forest_bandits"),
                (this_or_next|eq, ":bandit_template", "pt_forest_bandits_r"),
                (eq, ":bandit_template", "pt_forest_bandits_e"),
				##Floris MTT end
                (eq, ":new_camp_terrain", 11),
                (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, ":new_camp"),
                (party_set_flags, ":new_camp", pf_disabled, 1),
              (else_try),
                (party_is_active, ":new_camp"),
                (str_store_party_name, s4, ":new_camp"),
                (remove_party, ":new_camp"),
                (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, 0),
              (else_try),
              (try_end),
            (try_end),
        ]),

				##Floris MTT begin
        ("start_spawn_bandits",
          [
            (set_spawn_radius,1),
            
            (try_begin),
              (eq, "$cheat_mode", 1),
              (display_message, "@{!}DEBUG : Doing spawn bandit script"),
            (try_end),
            
            (party_template_set_slot, "pt_steppe_bandits_e", slot_party_template_lair_type, "pt_steppe_bandit_lair_e"),
            (party_template_set_slot, "pt_taiga_bandits_e", slot_party_template_lair_type, "pt_taiga_bandit_lair_e"),
            (party_template_set_slot, "pt_mountain_bandits_e", slot_party_template_lair_type, "pt_mountain_bandit_lair_e"),
            (party_template_set_slot, "pt_forest_bandits_e", slot_party_template_lair_type, "pt_forest_bandit_lair_e"),
            (party_template_set_slot, "pt_sea_raiders_e", slot_party_template_lair_type, "pt_sea_raider_lair_e"),
            (party_template_set_slot, "pt_desert_bandits_e", slot_party_template_lair_type, "pt_desert_bandit_lair_e"),
            
            (party_template_set_slot, "pt_steppe_bandits_e", slot_party_template_lair_spawnpoint, "p_steppe_bandit_spawn_point"),
            (party_template_set_slot, "pt_taiga_bandits_e", slot_party_template_lair_spawnpoint, "p_taiga_bandit_spawn_point"),
            (party_template_set_slot, "pt_mountain_bandits_e", slot_party_template_lair_spawnpoint, "p_mountain_bandit_spawn_point"),
            (party_template_set_slot, "pt_forest_bandits_e", slot_party_template_lair_spawnpoint, "p_forest_bandit_spawn_point"),
            (party_template_set_slot, "pt_sea_raiders_e", slot_party_template_lair_spawnpoint, "p_sea_raider_spawn_point_1"),
            (party_template_set_slot, "pt_desert_bandits_e", slot_party_template_lair_spawnpoint, "p_desert_bandit_spawn_point"),
            
            (try_begin),
              (store_num_parties_of_template, ":num_parties", "pt_mountain_bandits_e"),
              (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
              (store_random,":spawn_point",num_mountain_bandit_spawn_points),
              (val_add,":spawn_point","p_mountain_bandit_spawn_point"),
              (set_spawn_radius, 25),
              (spawn_around_party,":spawn_point","pt_mountain_bandits_e"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_mountain_bandits_e", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_mountain_bandits_e"),
                     ## CC
            (try_end),

	 #Wulf
    (try_begin),
		##Floris MTT begin
		(try_begin),
			(eq, "$troop_trees", troop_trees_0),
			(assign, ":sea_raider_ships", "pt_sea_raiders_ships"),
		(else_try),
			(eq, "$troop_trees", troop_trees_1),
			(assign, ":sea_raider_ships", "pt_sea_raiders_ships_r"),
		(else_try),
			(eq, "$troop_trees", troop_trees_2),
			(assign, ":sea_raider_ships", "pt_sea_raiders_ships_e"),
		(try_end),
		(store_num_parties_of_template, ":num_parties", ":sea_raider_ships"),
		(lt,":num_parties",18),
		(spawn_around_party, "p_ship_raider_spawn_point_1", ":sea_raider_ships"),
    (try_end),
     #Wulf end        
	 
            (try_begin),
              (store_num_parties_of_template, ":num_parties", "pt_forest_bandits_e"),
              (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
              (store_random,":spawn_point",num_forest_bandit_spawn_points),
              (val_add,":spawn_point","p_forest_bandit_spawn_point"),
              (set_spawn_radius, 25),
              (spawn_around_party,":spawn_point","pt_forest_bandits_e"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_forest_bandits_e", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_forest_bandits_e"),
                     ## CC
            (try_end),
            (try_begin),
              (store_num_parties_of_template, ":num_parties", "pt_sea_raiders_e"),
              (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
              (store_random,":spawn_point",num_sea_raider_spawn_points),
              (val_add,":spawn_point","p_sea_raider_spawn_point_1"),
              (set_spawn_radius, 25),
              (spawn_around_party,":spawn_point","pt_sea_raiders_e"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_sea_raiders_e", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_sea_raiders_e"),
                     ## CC
            (try_end),
            (try_begin),
              (store_num_parties_of_template, ":num_parties", "pt_steppe_bandits_e"),
              (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
              (store_random,":spawn_point",num_steppe_bandit_spawn_points),
              (val_add,":spawn_point","p_steppe_bandit_spawn_point"),
              (set_spawn_radius, 25),
              (spawn_around_party,":spawn_point","pt_steppe_bandits_e"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_steppe_bandits_e", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_steppe_bandits_e"),
                     ## CC
            (try_end),
            (try_begin),
              (store_num_parties_of_template, ":num_parties", "pt_taiga_bandits_e"),
              (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
              (store_random,":spawn_point",num_taiga_bandit_spawn_points),
              (val_add,":spawn_point","p_taiga_bandit_spawn_point"),
              (set_spawn_radius, 25),
              (spawn_around_party,":spawn_point","pt_taiga_bandits_e"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_taiga_bandits_e", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_taiga_bandits_e"),
                     ## CC
            (try_end),
            (try_begin),
              (store_num_parties_of_template, ":num_parties", "pt_desert_bandits_e"),
              (lt,":num_parties",16), #was 14 at mount&blade, 18 in warband, 16 last decision
              (store_random,":spawn_point",num_desert_bandit_spawn_points),
              (val_add,":spawn_point","p_desert_bandit_spawn_point"),
              (set_spawn_radius, 25),
              (spawn_around_party,":spawn_point","pt_desert_bandits_e"),
                     ## CC 1.325
                     (party_template_slot_eq, "pt_desert_bandits_e", slot_party_template_has_hero, 1),
                     (spawn_around_party,":spawn_point","pt_desert_bandits_e"),
                     ## CC
            (try_end),
            (try_begin),
              (store_num_parties_of_template, ":num_parties", "pt_looters_e"),
              (lt,":num_parties",42), #was 33 at mount&blade, 50 in warband, 42 last decision
              (store_random_in_range,":spawn_point",villages_begin,villages_end), #spawn looters twice to have lots of them at the beginning
              (set_spawn_radius, 25),
              (spawn_around_party,":spawn_point","pt_looters_e"),
              (assign, ":spawned_party_id", reg0),
              (try_begin),
                (check_quest_active, "qst_deal_with_looters"),
                (party_set_flags, ":spawned_party_id", pf_quest_party, 1),
              (else_try),
                (party_set_flags, ":spawned_party_id", pf_quest_party, 0),
              (try_end),
            (try_end),
            (try_begin),
              (store_num_parties_of_template, ":num_parties", "pt_deserters"),
              (lt,":num_parties",15),
              (set_spawn_radius, 4),
              (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
                (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
                (store_random_in_range, ":random_no", 0, 100),
                (lt, ":random_no", 5),
                (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
                (store_troop_faction, ":troop_faction", ":troop_no"),
                (neq, ":troop_faction", "fac_player_supporters_faction"),
                (gt, ":party_no", 0),
                (neg|party_is_in_any_town, ":party_no"),
                ##         (party_get_attached_to, ":attached_party_no", ":party_no"),
                ##         (lt, ":attached_party_no", 0),#in wilderness
                (spawn_around_party, ":party_no", "pt_deserters"),
                (assign, ":new_party", reg0),
                (store_troop_faction, ":faction_no", ":troop_no"),
                (faction_get_slot, ":tier_1_troop", ":faction_no", slot_faction_tier_1_troop),
                (store_character_level, ":level", "trp_player"),
                (store_mul, ":max_number_to_add", ":level", 2),
                (val_add, ":max_number_to_add", 11),
                (store_random_in_range, ":number_to_add", 10, ":max_number_to_add"),
                (party_add_members, ":new_party", ":tier_1_troop", ":number_to_add"),
                (store_random_in_range, ":random_no", 1, 4),
                (try_for_range, ":unused", 0, ":random_no"),
                  (party_upgrade_with_xp, ":new_party", 1000000, 0),
                (try_end),
                ##         (str_store_party_name, s1, ":party_no"),
                ##         (call_script, "script_get_closest_center", ":party_no"),
                ##         (try_begin),
                ##           (gt, reg0, 0),
                ##           (str_store_party_name, s2, reg0),
                ##         (else_try),
                ##           (str_store_string, s2, "@unknown place"),
                ##         (try_end),
                ##         (assign, reg1, ":number_to_add"),
                ##         (display_message, "@{reg1} Deserters spawned from {s1}, near {s2}."),
              (try_end),
            (try_end), #deserters ends
            
            
		  ##Floris MTT begin
			(try_begin),
				(eq, "$troop_trees", troop_trees_0),
				(assign, ":templates_begin", bandit_party_template_begin),
				(assign, ":templates_end", bandit_party_template_end),
			(else_try),
				(eq, "$troop_trees", troop_trees_1),
				(assign, ":templates_begin", bandit_party_template_r_begin),
				(assign, ":templates_end", bandit_party_template_r_end),
			(else_try),
				(eq, "$troop_trees", troop_trees_2),
				(assign, ":templates_begin", bandit_party_template_e_begin),
				(assign, ":templates_end", bandit_party_template_e_end),
			(try_end),
			(try_for_range, ":bandit_template", ":templates_begin", ":templates_end"), #changed from bandit_party_template_begin to bandit_party_template_end
			##Floris MTT end 
              (party_template_get_slot, ":bandit_lair_party", ":bandit_template", slot_party_template_lair_party),
              (le, ":bandit_lair_party", 1),
              
              (party_template_get_slot, ":bandit_lair_template", ":bandit_template", slot_party_template_lair_type),
              (party_template_get_slot, ":bandit_lair_template_spawnpoint", ":bandit_template", slot_party_template_lair_spawnpoint),
              
              (set_spawn_radius, 20),
              
              (spawn_around_party, ":bandit_lair_template_spawnpoint", ":bandit_lair_template"),
              (assign, ":new_camp", reg0),
              
              (party_set_slot, ":new_camp", slot_party_type, spt_bandit_lair),
              
              (str_store_party_name, s4, ":new_camp"),
              
              (party_get_position, pos4, ":new_camp"),
              #(party_set_flags, ":new_camp", pf_icon_mask, 1),
              
              (party_get_current_terrain, ":new_camp_terrain", ":new_camp"),
              (position_get_z, ":elevation", pos4),
              (position_get_y, ":lair_y", pos4),
              
              (assign, ":center_too_close", 0),
              (try_for_range, ":center", centers_begin, centers_end),
                (eq, ":center_too_close", 0),
                (store_distance_to_party_from_party, ":distance", ":new_camp", ":center"),
                (lt, ":distance", 3),
                (assign, ":center_too_close", 1),
              (try_end),
              
              (try_begin),
                (eq, ":center_too_close", 1),
                (party_is_active, ":new_camp"),
                (remove_party, ":new_camp"),
                (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, 0),
              (else_try),
                (eq, ":bandit_template", "pt_sea_raiders_e"),
                (eq, ":new_camp_terrain", 3),
                (map_get_water_position_around_position, pos5, pos4, 4),
                (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, ":new_camp"),
                (party_set_flags, ":new_camp", pf_disabled, 1),
              (else_try),
                (eq, ":bandit_template", "pt_mountain_bandits_e"),
                (eq, ":new_camp_terrain", 3),
                (gt, ":elevation", 250),
                (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, ":new_camp"),
                (party_set_flags, ":new_camp", pf_disabled, 1),
              (else_try),
                (eq, ":bandit_template", "pt_desert_bandits_e"),
                (eq, ":new_camp_terrain", 5),
                (gt, ":lair_y", -9000),
                (gt, ":elevation", 125),
                (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, ":new_camp"),
                (party_set_flags, ":new_camp", pf_disabled, 1),
              (else_try),
                (eq, ":bandit_template", "pt_steppe_bandits_e"),
                (this_or_next|eq, ":new_camp_terrain", 2),
                (eq, ":new_camp_terrain", 10),
                (this_or_next|eq, ":new_camp_terrain", 10),
                (gt, ":elevation", 200),
                (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, ":new_camp"),
                (party_set_flags, ":new_camp", pf_disabled, 1),
              (else_try),
                (eq, ":bandit_template", "pt_taiga_bandits_e"),
                (eq, ":new_camp_terrain", 12),
                (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, ":new_camp"),
                (party_set_flags, ":new_camp", pf_disabled, 1),
              (else_try),
                (eq, ":bandit_template", "pt_forest_bandits_e"),
                (eq, ":new_camp_terrain", 11),
                (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, ":new_camp"),
                (party_set_flags, ":new_camp", pf_disabled, 1),
              (else_try),
                (party_is_active, ":new_camp"),
                (str_store_party_name, s4, ":new_camp"),
                (remove_party, ":new_camp"),
                (party_template_set_slot, ":bandit_template", slot_party_template_lair_party, 0),
              (else_try),
              (try_end),
            (try_end),
        ]),
				##Floris MTT end
        
        #script_count_mission_casualties_from_agents
        # INPUT: none
        # OUTPUT: none
        ("count_mission_casualties_from_agents",
          [(party_clear, "p_player_casualties"),
            (party_clear, "p_enemy_casualties"),
            (party_clear, "p_ally_casualties"),
            (assign, "$any_allies_at_the_last_battle", 0),
            #(assign, "$num_routed_us", 0), #these should not assign to 0 here to protect routed agents to spawn again in next turns.
            #(assign, "$num_routed_allies", 0),
            #(assign, "$num_routed_enemies", 0),
            
            #initialize all routed counts of troops
            (try_for_agents, ":cur_agent"),
              (agent_is_human, ":cur_agent"),
              (agent_get_party_id, ":agent_party", ":cur_agent"),
              (agent_get_troop_id, ":agent_troop_id", ":cur_agent"),
              (troop_set_slot, ":agent_troop_id", slot_troop_player_routed_agents, 0),
              (troop_set_slot, ":agent_troop_id", slot_troop_ally_routed_agents, 0),
              (troop_set_slot, ":agent_troop_id", slot_troop_enemy_routed_agents, 0),
            (try_end),
            
            (try_for_agents, ":cur_agent"),
              (agent_is_human, ":cur_agent"),
              (agent_get_party_id, ":agent_party", ":cur_agent"),
              (try_begin),
                (neq, ":agent_party", "p_main_party"),
                (agent_is_ally, ":cur_agent"),
                (assign, "$any_allies_at_the_last_battle", 1),
              (try_end),
              #count routed agents in player party, ally parties and enemy parties
              (try_begin),
                (agent_is_routed, ":cur_agent"),
                (agent_get_slot, ":agent_was_running_away", ":cur_agent", slot_agent_is_running_away),
                (eq, ":agent_was_running_away", 1),
                (try_begin),
                  (agent_get_troop_id, ":routed_ag_troop_id", ":cur_agent"),
                  (agent_get_party_id, ":routed_ag_party_id", ":cur_agent"),
                  #only enemies
                  #only regulars
                  (store_faction_of_party, ":faction_of_routed_agent_party", ":routed_ag_party_id"),
                  
                  (try_begin),
                    (eq, ":agent_party", "p_main_party"),
                    (val_add, "$num_routed_us", 1),
                  (else_try),
                    (agent_is_ally, ":cur_agent"),
                    (val_add, "$num_routed_allies", 1),
                  (else_try),
                    #for now only count and include routed enemy agents in new routed party.
                    (val_add, "$num_routed_enemies", 1),
                    (faction_get_slot, ":num_routed_agents_in_this_faction", ":faction_of_routed_agent_party", slot_faction_num_routed_agents),
                    (val_add, ":num_routed_agents_in_this_faction", 1),
                    (faction_set_slot, ":faction_of_routed_agent_party", slot_faction_num_routed_agents, ":num_routed_agents_in_this_faction"),
                    (party_add_members, "p_routed_enemies", ":routed_ag_troop_id", 1),
                  (try_end),
                (try_end),
                (agent_get_troop_id, ":agent_troop_id", ":cur_agent"),
                (try_begin),
                  (eq, ":agent_party", "p_main_party"),
                  (troop_get_slot, ":player_routed_agents", ":agent_troop_id", slot_troop_player_routed_agents),
                  (val_add, ":player_routed_agents", 1),
                  (troop_set_slot, ":agent_troop_id", slot_troop_player_routed_agents, ":player_routed_agents"),
                  
                (else_try),
                  (agent_is_ally, ":cur_agent"),
                  (troop_get_slot, ":ally_routed_agents", ":agent_troop_id", slot_troop_ally_routed_agents),
                  (val_add, ":ally_routed_agents", 1),
                  (troop_set_slot, ":agent_troop_id", slot_troop_ally_routed_agents, ":ally_routed_agents"),
                  
                (else_try),
                  (troop_get_slot, ":enemy_routed_agents", ":agent_troop_id", slot_troop_enemy_routed_agents),
                  (val_add, ":enemy_routed_agents", 1),
                  (troop_set_slot, ":agent_troop_id", slot_troop_enemy_routed_agents, ":enemy_routed_agents"),
                  
                (try_end),
              (try_end),
              #count and save killed agents in player party, ally parties and enemy parties
              (neg|agent_is_alive, ":cur_agent"),
              (agent_get_troop_id, ":agent_troop_id", ":cur_agent"),
              (try_begin),
                (eq, ":agent_party", "p_main_party"),
                (party_add_members, "p_player_casualties", ":agent_troop_id", 1),
                (try_begin),
                  (agent_is_wounded, ":cur_agent"),
                  (party_wound_members, "p_player_casualties", ":agent_troop_id", 1),
                (try_end),
              (else_try),
                (agent_is_ally, ":cur_agent"),
                (party_add_members, "p_ally_casualties", ":agent_troop_id", 1),
                (try_begin),
                  (agent_is_wounded, ":cur_agent"),
                  (party_wound_members, "p_ally_casualties", ":agent_troop_id", 1),
                (try_end),
              (else_try),
                (party_add_members, "p_enemy_casualties", ":agent_troop_id", 1),
                (try_begin),
                  (agent_is_wounded, ":cur_agent"),
                  (party_wound_members, "p_enemy_casualties", ":agent_troop_id", 1),
                (try_end),
              (try_end),
            (try_end),
        ]),
        
        #script_get_max_skill_of_player_party
        # INPUT: arg1 = skill_no
        # OUTPUT: reg0 = max_skill, reg1 = skill_owner_troop_no
        ("get_max_skill_of_player_party",
          [(store_script_param, ":skill_no", 1),
            (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
            (store_skill_level, ":max_skill", ":skill_no", "trp_player"),
            (assign, ":skill_owner", "trp_player"),
            (try_for_range, ":i_stack", 0, ":num_stacks"),
              (party_stack_get_troop_id, ":stack_troop","p_main_party",":i_stack"),
              (troop_is_hero, ":stack_troop"),
              (neg|troop_is_wounded, ":stack_troop"),
              (store_skill_level, ":cur_skill", ":skill_no", ":stack_troop"),
              (gt, ":cur_skill", ":max_skill"),
              (assign, ":max_skill", ":cur_skill"),
              (assign, ":skill_owner", ":stack_troop"),
            (try_end),
            (party_get_skill_level, reg0, "p_main_party", ":skill_no"),
            ##     (assign, reg0, ":max_skill"),
            (assign, reg1, ":skill_owner"),
        ]),
        
        #script_upgrade_hero_party
        # INPUT: arg1 = party_id, arg2 = xp_amount
	  ("upgrade_hero_party",
		[
		  (store_script_param, ":party_no", 1),
		  (store_script_param, ":xp_amount", 2),
		  ##diplomacy start+
		  #Take into account faction quality/quantity settings.  Do not apply this
		  #to the player party or to special parties.
		  (try_begin),
			(ge, ":party_no", spawn_points_begin),
			(store_faction_of_party, ":var1", ":party_no"),
			(faction_get_slot, ":var1", ":var1", dplmc_slot_faction_quality),
			(val_add, ":var1", 100),
			(val_clamp, ":var1", 97, 104),#100 plus or minus three percent
			(val_mul, ":xp_amount", ":var1"),
			(val_div, ":xp_amount", 100),
		  (try_end),
		   ##diplomacy end+
		  (party_upgrade_with_xp, ":party_no", ":xp_amount", 0),
		]),
        
        #script_get_improvement_details
        # INPUT: arg1 = improvement
        # OUTPUT: reg0 = base_cost
        ("get_improvement_details",
          [(store_script_param, ":improvement_no", 1),
            (try_begin),
              (eq, ":improvement_no", slot_center_has_manor),
              (str_store_string, s0, "@Manor"),
              (str_store_string, s1, "@A manor lets you rest at the village and pay your troops half wages while you rest."),
              (assign, reg0, 8000),
            (else_try),
              (eq, ":improvement_no", slot_center_has_fish_pond),
              (str_store_string, s0, "@Mill"),
              (str_store_string, s1, "@A mill increases village prosperity by 5%."),
              (assign, reg0, 6000),
            (else_try),
              (eq, ":improvement_no", slot_center_has_watch_tower),
              (str_store_string, s0, "@Watch Tower"),
              (str_store_string, s1, "@A watch tower lets the villagers raise alarm earlier. The time it takes for enemies to loot the village increases by 50%."),
              (assign, reg0, 5000),
            (else_try),
              (eq, ":improvement_no", slot_center_has_school),
              (str_store_string, s0, "@School"),
              (str_store_string, s1, "@A shool increases the loyality of the villagers to you by +1 every month."),
              (assign, reg0, 9000),
            (else_try),
              (eq, ":improvement_no", slot_center_has_messenger_post),
              (str_store_string, s0, "@Messenger Post"),
              (str_store_string, s1, "@A messenger post lets the inhabitants send you a message whenever enemies are nearby, even if you are far away from here."),
              (assign, reg0, 4000),
              #Lazeras MODIFIED (Training Yard)
            (else_try),
              (eq, ":improvement_no", slot_center_has_barracks),
              (str_store_string, s0, "@Barracks"),
              (str_store_string, s1, "@A Barracks helps to train better troops."),
              (assign, reg0, 4000),
              #Lazeras MODIFIED (Training Yard)
            (else_try),
              (eq, ":improvement_no", slot_center_has_prisoner_tower),
              (str_store_string, s0, "@Prison Tower"),
              (str_store_string, s1, "@A prison tower reduces the chance of captives held here running away successfully."),
              (assign, reg0, 7000),
            (try_end),
        ]),
        
        #script_cf_troop_agent_is_alive
        # INPUT: arg1 = troop_id
        ("cf_troop_agent_is_alive",
          [(store_script_param, ":troop_no", 1),
            (assign, ":alive_count", 0),
            (try_for_agents, ":cur_agent"),
              (agent_get_troop_id, ":cur_agent_troop", ":cur_agent"),
              (eq, ":troop_no", ":cur_agent_troop"),
              (agent_is_alive, ":cur_agent"),
              (val_add, ":alive_count", 1),
            (try_end),
            (gt, ":alive_count", 0),
        ]),
        
        #script_cf_village_recruit_volunteers_cond
        # INPUT: none
        # OUTPUT: none
        ("cf_village_recruit_volunteers_cond",
          [
            
            (try_begin),
              (eq, "$cheat_mode", 1),
              (display_message, "str_checking_volunteer_availability_script"),
            (try_end),
            
            (neg|party_slot_eq, "$current_town", slot_village_state, svs_looted),
            (neg|party_slot_eq, "$current_town", slot_village_state, svs_being_raided),
            (neg|party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),
            (store_faction_of_party, ":village_faction", "$current_town"),
            (party_get_slot, ":center_relation", "$current_town", slot_center_player_relation),
            (store_relation, ":village_faction_relation", ":village_faction", "fac_player_faction"),
            
            (ge, ":center_relation", 0),
            (try_begin),
              (eq, "$cheat_mode", 1),
              (display_message, "str_center_relation_at_least_zero"),
            (try_end),
            
            
            
            
            (this_or_next|ge, ":center_relation", 5),
            (this_or_next|eq, ":village_faction", "$players_kingdom"),
            (this_or_next|ge, ":village_faction_relation", 0),
            (this_or_next|eq, ":village_faction", "$supported_pretender_old_faction"),
            (eq, "$players_kingdom", 0),
            
            (try_begin),
              (eq, "$cheat_mode", 1),
              (display_message, "str_relationfaction_conditions_met"),
            (try_end),
            
            
            (party_slot_ge, "$current_town", slot_center_volunteer_troop_amount, 0),
            (party_slot_ge, "$current_town", slot_center_volunteer_troop_type, 1),
            
            (try_begin),
              (eq, "$cheat_mode", 1),
              (display_message, "str_troops_available"),
            (try_end),
            
            
            (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
            (ge, ":free_capacity", 1),
            
            (try_begin),
              (eq, "$cheat_mode", 1),
              (display_message, "str_party_has_capacity"),
            (try_end),
            
            
        ]),
        
        #script_village_recruit_volunteers_recruit
        # INPUT: none
        # OUTPUT: none
        ("village_recruit_volunteers_recruit",
          [(party_get_slot, ":volunteer_troop", "$current_town", slot_center_volunteer_troop_type),
            (party_get_slot, ":volunteer_amount", "$current_town", slot_center_volunteer_troop_amount),
            (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
            (val_min, ":volunteer_amount", ":free_capacity"),
            (store_troop_gold, ":gold", "trp_player"),
            (store_div, ":gold_capacity", ":gold", 10),#10 denars per man
            (val_min, ":volunteer_amount", ":gold_capacity"),
            #Lazeras MODIFIED (Training Yard)
            (assign, ":volunteer_amount_new", 0),
            (try_begin),
			  (party_get_slot, ":bound_center", "$current_town", slot_village_bound_center), #CABA - 2.52 bugfix
			  (party_slot_ge, ":bound_center", slot_center_has_barracks, 1), #CABA - 2.52 bugfix
              (assign, ":rand", reg30),
              (lt, ":rand", 25),
              (assign,":type", reg31),
              (troop_get_upgrade_troop, ":upgrade_troop", ":volunteer_troop" , ":type"),
              (try_begin),
                (le, ":upgrade_troop", 0),
                (troop_get_upgrade_troop, ":upgrade_troop", ":volunteer_troop", 0),
              (try_end),
              #only proceed if troop is upgradable
              (gt, ":upgrade_troop", 0),
              (store_div, ":third", ":volunteer_amount", 3),
              (store_sub, ":volunteer_amount_new", ":volunteer_amount", ":third"),
              (store_sub, ":volunteer_amount", ":volunteer_amount", ":third"),
              (party_add_members, "p_main_party", ":upgrade_troop", ":volunteer_amount_new"),
            (try_end),
            #Lazeras MODIFIED (Training Yard)
            (party_add_members, "p_main_party", ":volunteer_troop", ":volunteer_amount"),
            (party_set_slot, "$current_town", slot_center_volunteer_troop_amount, -1),
            (store_mul, ":cost", ":volunteer_amount", 10),#10 denars per man
            (troop_remove_gold, "trp_player", ":cost"),
        ]),
        
        
        #script_get_troop_item_amount
        # INPUT: arg1 = troop_no, arg2 = item_no
        # OUTPUT: reg0 = item_amount
        ("get_troop_item_amount",
          [(store_script_param, ":troop_no", 1),
            (store_script_param, ":item_no", 2),
            (troop_get_inventory_capacity, ":inv_cap", ":troop_no"),
            (assign, ":count", 0),
            (try_for_range, ":i_slot", 0, ":inv_cap"),
              (troop_get_inventory_slot, ":cur_item", ":troop_no", ":i_slot"),
              (eq, ":cur_item", ":item_no"),
              (val_add, ":count", 1),
            (try_end),
            (assign, reg0, ":count"),
        ]),
        
        ##Floris/STAT
        #script_get_troop_amount
        # INPUT: arg1 = p_main_party, arg2 = troop_no
        # OUTPUT: reg0 = item_amount
        # script_get_party_troop_count
        # INPUT: arg1 = party_no, arg2 = troop_no
        # OUTPUT: reg0 = troop_count
        ("get_party_troop_count",
          [
            (store_script_param_1, ":party_no"),
            (store_script_param_2, ":troop_no"),
            
            (assign, ":stack_size", 0),
            (party_get_num_companion_stacks, ":num_of_stacks", ":party_no"),
            (try_for_range, ":i", 0, ":num_of_stacks"),
              (party_stack_get_troop_id, ":stack_troop", ":party_no", ":i"),
              (eq, ":stack_troop", ":troop_no"),
              (party_stack_get_size, ":stack_size", ":party_no", ":i"),
              (party_stack_get_num_wounded, ":stack_wounded", ":party_no", ":i"),
              (val_sub, ":stack_size", ":stack_wounded"),
              (assign, ":num_of_stacks", 0), #break loop
            (try_end),
            (assign, reg0, ":stack_size"),
        ]),
        ##Floris/STAT end
        
        #script_get_name_from_dna_to_s50
        # INPUT: arg1 = dna
        # OUTPUT: s50 = name
        ("get_name_from_dna_to_s50",
          [(store_script_param, ":dna", 1),
            (store_sub, ":num_names", names_end, names_begin),
            (store_sub, ":num_surnames", surnames_end, surnames_begin),
            (assign, ":selected_name", ":dna"),
            (val_mod, ":selected_name", ":num_names"),
            (assign, ":selected_surname", ":dna"),
            (val_div, ":selected_surname", ":num_names"),
            (val_mod, ":selected_surname", ":num_surnames"),
            (val_add, ":selected_name", names_begin),
            (val_add, ":selected_surname", surnames_begin),
            (str_store_string, s50, ":selected_name"),
            (str_store_string, s50, ":selected_surname"),
        ]),
        
        #script_change_center_prosperity
        # INPUT: arg1 = center_no, arg2 = difference
        # OUTPUT: none
        ("change_center_prosperity",
          [(store_script_param, ":center_no", 1),
            (store_script_param, ":difference", 2),
            (party_get_slot, ":old_prosperity", ":center_no", slot_town_prosperity),
            (store_add, ":new_prosperity", ":old_prosperity", ":difference"),
            (val_clamp, ":new_prosperity", 0, 100),
            (store_div, ":old_state", ":old_prosperity", 20),
            (store_div, ":new_state", ":new_prosperity", 20),
            
            (try_begin),
              (neq, ":old_state", ":new_state"),
              (neg|is_between, ":center_no", castles_begin, castles_end),
              
              (str_store_party_name_link, s2, ":center_no"),
              (call_script, "script_get_prosperity_text_to_s50", ":center_no"),
              (str_store_string, s3, s50),
              (party_set_slot, ":center_no", slot_town_prosperity, ":new_prosperity"),
              (call_script, "script_get_prosperity_text_to_s50", ":center_no"),
              (str_store_string, s4, s50),
              (try_begin),
                (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
                (display_message, "@Prosperity of {s2} has changed from {s3} to {s4}."),
              (try_end),
              (call_script, "script_update_center_notes", ":center_no"),
            (else_try),
              (party_set_slot, ":center_no", slot_town_prosperity, ":new_prosperity"),
            (try_end),
            
            (try_begin),
              (store_current_hours, ":hours"),
              (gt, ":hours", 1),
              (store_sub, ":actual_difference", ":new_prosperity", ":old_prosperity"),
              (try_begin),
                (lt, ":actual_difference", 0),
                (val_add, "$newglob_total_prosperity_losses", ":actual_difference"),
              (else_try),
                (gt, ":actual_difference", 0),
                (val_add, "$newglob_total_prosperity_gains", ":actual_difference"),
              (try_end),
            (try_end),
            
            #This will add up all non-trade prosperity
            (try_begin),
              (eq, "$cheat_mode", 3),
              (assign, reg4, "$newglob_total_prosperity_from_bandits"),
              (assign, reg5, "$newglob_total_prosperity_from_caravan_trade"),
              (assign, reg7, "$newglob_total_prosperity_from_villageloot"),
              (assign, reg8, "$newglob_total_prosperity_from_townloot"),
              (assign, reg9, "$newglob_total_prosperity_from_village_trade"),
              (assign, reg10, "$newglob_total_prosperity_from_convergence"),
              (assign, reg11, "$newglob_total_prosperity_losses"),
              (assign, reg12, "$newglob_total_prosperity_gains"),
              (display_message, "@{!}DEBUG: Total prosperity actual losses: {reg11}"),
              (display_message, "@{!}DEBUG: Total prosperity actual gains: {reg12}"),
              
              (display_message, "@{!}DEBUG: Prosperity changes from random bandits: {reg4}"),
              (display_message, "@{!}DEBUG: Prosperity changes from caravan trades: {reg5}"),
              (display_message, "@{!}DEBUG: Prosperity changes from farmer trades: {reg9}"),
              (display_message, "@{!}DEBUG: Prosperity changes from looted villages: {reg7}"),
              (display_message, "@{!}DEBUG: Prosperity changes from sieges: {reg8}"),
              (display_message, "@{!}DEBUG: Theoretical prosperity changes from convergence: {reg10}"),
            (try_end),
            
        ]),
        
        #script_get_center_ideal_prosperity
        # INPUT: arg1 = center_no
        # OUTPUT: reg0 = ideal_prosperity
        ("get_center_ideal_prosperity",
          [(store_script_param, ":center_no", 1),
            (assign, ":ideal", 65), #1.153 - was 100
            
            (call_script, "script_center_get_goods_availability", ":center_no"),
            (store_mul, ":hardship_index", reg0, 2), #currently x2          
            (val_sub, ":ideal", ":hardship_index"),
            
            (try_begin),
              (is_between, ":center_no", villages_begin, villages_end),
              (party_slot_eq, ":center_no", slot_center_has_fish_pond, 1),
              (val_add, ":ideal", 5),
            (try_end),
            
            #     (try_begin),
            #       (is_between, ":center_no", villages_begin, villages_end),
            #       (try_begin),
            #         (party_slot_eq, ":center_no", slot_center_has_fish_pond, 1),
            #         (val_add, ":ideal", 5),
            #       (try_end),
            #       (party_get_slot, ":land_quality", ":center_no", slot_village_land_quality),
            #       (val_mul, ":land_quality", 3),
            #       (val_add, ":ideal", ":land_quality"),
            #       (party_get_slot, ":num_cattle", ":center_no", slot_village_number_of_cattle),
            #       (val_div, ":num_cattle", 20),
            #       (val_add, ":ideal", ":num_cattle"),
            #     (else_try),
            #       (try_for_range, ":village_no", villages_begin, villages_end),
            #         (party_slot_eq, ":village_no", slot_village_bound_center, ":center_no"),
            #         (party_get_slot, ":prosperity", ":village_no", slot_town_prosperity),
            #         (val_div, ":prosperity", 20),
            #         (val_add, ":ideal", ":prosperity"),
            #       (try_end),
            #     (try_end),
			
            (val_max, ":ideal", 0),
            (assign, reg0, ":ideal"),
        ]),
        
        ("good_price_affects_good_production",
          [
            (store_script_param, ":center", 1),
            (store_script_param, ":input_item_no", 2),
            (store_script_param, ":production", 3),
            (store_script_param, ":impact_divisor", 4),
            
            (assign, reg4, ":production"),
            
            
            
            (try_begin),
              (gt, ":production", 0), #let's take -20 as the zero production rate, although in actuality production can go lower, representing increased demand
              
              (store_sub, ":input_good_price_slot", ":input_item_no", trade_goods_begin),
              (val_add, ":input_good_price_slot", slot_town_trade_good_prices_begin),
              (party_get_slot, ":input_price", ":center", ":input_good_price_slot"),
              
			(try_begin),																								#	1.143 Port // Newly Added
				(is_between, ":center", towns_begin, towns_end),

				(val_mul, ":input_price", 4),
				(assign, ":number_of_villages", 4),
				(try_for_range, ":village_no", villages_begin, villages_end),
					(party_slot_eq, ":village_no", slot_village_bound_center, ":center"),
					(party_get_slot, ":input_price_at_village", ":village_no", ":input_good_price_slot"),
					(val_add, ":input_price", ":input_price_at_village"),
					(val_add, ":number_of_villages", 1),
				(try_end),		  

				(val_div, ":input_price", ":number_of_villages"),
			(try_end),																									#	End		
              
			(try_begin), #1/2 impact for low prices
				##diplomacy start+		
				(lt, ":input_price", average_price_factor),#Replace 1000 with average_price_factor
				##diplomacy end+
				(val_mul, ":impact_divisor", 2),
			(try_end),

			(try_begin),
				(gt, ":impact_divisor", 1),
				##diplomacy start+
				(val_sub, ":input_price", average_price_factor),#Replace 1000 with average_price_factor
				(val_div, ":input_price", ":impact_divisor"),#<- unchanged
				(val_add, ":input_price", average_price_factor),#Replace 1000 with average_price_factor
				##diplomacy end+
			(try_end),

			##diplomacy start+
			(val_mul, ":production", average_price_factor),#Replace 1000 with average_price_factor
			##diplomacy end+
			(val_div, ":production", ":input_price"),
              
              #		(assign, reg5, ":production"),
			  #		(assign, reg3, ":input_price"),																		#	1.143 Port // Added Line
              #		(str_store_item_name, s4, ":input_item_no"),
              #		(display_message, "@{s4} price of {reg3} reduces production from {reg4} to {reg5}"),
              
            (try_end),
            
            
            (assign, reg0, ":production"),
            
        ]),
        
        
        
        
        #script_get_poorest_village_of_faction
        # INPUT: arg1 = center_no
        # OUTPUT: reg0 = ideal_prosperity
        ("get_poorest_village_of_faction",
          [(store_script_param, ":faction_no", 1),
            (assign, ":min_prosperity_village", -1),
            (assign, ":min_prosperity", 101),
            (try_for_range, ":village_no", villages_begin, villages_end),
              (store_faction_of_party, ":village_faction", ":village_no"),
              (eq, ":village_faction", ":faction_no"),
              (party_get_slot, ":prosperity", ":village_no", slot_town_prosperity),
              (lt, ":prosperity", ":min_prosperity"),
              (assign, ":min_prosperity", ":prosperity"),
              (assign, ":min_prosperity_village", ":village_no"),
            (try_end),
            (assign, reg0, ":min_prosperity_village"),
        ]),
        
        #script_troop_add_gold
        # INPUT: arg1 = troop_no, arg2 = amount
        # OUTPUT: none
        ("troop_add_gold",
          [
            (store_script_param, ":troop_no", 1),
            (store_script_param, ":amount", 2),
            
            (troop_add_gold, ":troop_no", ":amount"),
            (try_begin),
              (eq, ":troop_no", "trp_player"),
              (play_sound, "snd_money_received"),
            (try_end),
        ]),
        
        #NPC companion changes begin
        ("initialize_npcs",
          [
            
            # set strings
            
			#Native npc's
			
            (troop_set_slot, "trp_npc1", slot_troop_morality_type, tmt_egalitarian),  #borcha
            (troop_set_slot, "trp_npc1", slot_troop_morality_value, 4),  #borcha
            (troop_set_slot, "trp_npc1", slot_troop_2ary_morality_type, tmt_aristocratic),  #borcha
            (troop_set_slot, "trp_npc1", slot_troop_2ary_morality_value, -1),
            (troop_set_slot, "trp_npc1", slot_troop_personalityclash_object, "trp_npc7"),  #borcha - deshavi
            (troop_set_slot, "trp_npc1", slot_troop_personalityclash2_object, "trp_npc21"),  #borcha - ghazwan
            (troop_set_slot, "trp_npc1", slot_troop_personalitymatch_object, "trp_npc2"),  #borcha - marnid
            (troop_set_slot, "trp_npc1", slot_troop_home, "p_village_25"), #Dashbiga
            (troop_set_slot, "trp_npc1", slot_troop_payment_request, 300),
            (troop_set_slot, "trp_npc1", slot_troop_kingsupport_argument, argument_ruler),
            (troop_set_slot, "trp_npc1", slot_troop_kingsupport_opponent, "trp_npc14"), #Lezalit
            (troop_set_slot, "trp_npc1", slot_troop_town_with_contacts, "p_town_17"), #ichamur
            (troop_set_slot, "trp_npc1", slot_troop_original_faction, 0), #ichamur
            (troop_set_slot, "trp_npc1", slot_lord_reputation_type, lrep_roguish), #
            
            
            
            (troop_set_slot, "trp_npc2", slot_troop_morality_type, tmt_humanitarian), #marnid
            (troop_set_slot, "trp_npc2", slot_troop_morality_value, 2),
            (troop_set_slot, "trp_npc2", slot_troop_2ary_morality_type, tmt_honest),
            (troop_set_slot, "trp_npc2", slot_troop_2ary_morality_value, 1),
            (troop_set_slot, "trp_npc2", slot_troop_personalityclash_object, "trp_npc5"), #marnid - beheshtur
            (troop_set_slot, "trp_npc2", slot_troop_personalityclash2_object, "trp_npc18"), #marnid - nadia
            (troop_set_slot, "trp_npc2", slot_troop_personalitymatch_object, "trp_npc1"),  #marnid - borcha
            (troop_set_slot, "trp_npc2", slot_troop_home, "p_town_1"), #Sargoth
            (troop_set_slot, "trp_npc2", slot_troop_payment_request, 0),
            (troop_set_slot, "trp_npc2", slot_troop_kingsupport_argument, argument_victory),
            (troop_set_slot, "trp_npc2", slot_troop_kingsupport_opponent, "trp_npc16"), #Klethi
            (troop_set_slot, "trp_npc2", slot_troop_town_with_contacts, "p_town_1"), #Sargoth
            (troop_set_slot, "trp_npc2", slot_troop_original_faction, 0), #ichamur
            (troop_set_slot, "trp_npc2", slot_lord_reputation_type, lrep_custodian), #
            
            #
            (troop_set_slot, "trp_npc3", slot_troop_morality_type, tmt_humanitarian), #Ymira
            (troop_set_slot, "trp_npc3", slot_troop_morality_value, 4),
            (troop_set_slot, "trp_npc3", slot_troop_2ary_morality_type, tmt_aristocratic),
            (troop_set_slot, "trp_npc3", slot_troop_2ary_morality_value, -1),
            (troop_set_slot, "trp_npc3", slot_troop_personalityclash_object, "trp_npc19"), #Ymira - odval
            (troop_set_slot, "trp_npc3", slot_troop_personalityclash2_object, "trp_npc20"), #Ymira - sajjad
            (troop_set_slot, "trp_npc3", slot_troop_personalitymatch_object, "trp_npc9"), #Ymira - alayen
            (troop_set_slot, "trp_npc3", slot_troop_home, "p_town_3"), #Veluca
            (troop_set_slot, "trp_npc3", slot_troop_payment_request, 0),
            (troop_set_slot, "trp_npc3", slot_troop_kingsupport_argument, argument_lords),
            (troop_set_slot, "trp_npc3", slot_troop_kingsupport_opponent, "trp_npc5"), #Baheshtur
            (troop_set_slot, "trp_npc3", slot_troop_town_with_contacts, "p_town_15"), #yalen
            (troop_set_slot, "trp_npc3", slot_troop_original_faction, 0), #ichamur
            (troop_set_slot, "trp_npc3", slot_lord_reputation_type, lrep_benefactor), #
            
            
            
            (troop_set_slot, "trp_npc4", slot_troop_morality_type, tmt_aristocratic), #Rolf
            (troop_set_slot, "trp_npc4", slot_troop_morality_value, 4),
            (troop_set_slot, "trp_npc4", slot_troop_2ary_morality_type, tmt_honest),
            (troop_set_slot, "trp_npc4", slot_troop_2ary_morality_value, -1),
            (troop_set_slot, "trp_npc4", slot_troop_personalityclash_object, "trp_npc10"), #Rolf - bunduk
            (troop_set_slot, "trp_npc4", slot_troop_personalityclash2_object, "trp_npc7"), #Rolf - deshavi
            (troop_set_slot, "trp_npc4", slot_troop_personalitymatch_object, "trp_npc20"), #Rolf - sajjad
            (troop_set_slot, "trp_npc4", slot_troop_home, "p_village_34"), #Ehlerdah
            (troop_set_slot, "trp_npc4", slot_troop_payment_request, 300),
            (troop_set_slot, "trp_npc4", slot_troop_kingsupport_argument, argument_claim),
            (troop_set_slot, "trp_npc4", slot_troop_kingsupport_opponent, "trp_npc6"), #Firentis
            (troop_set_slot, "trp_npc4", slot_troop_town_with_contacts, "p_town_3"), #veluca
            (troop_set_slot, "trp_npc4", slot_troop_original_faction, 0), #ichamur
            (troop_set_slot, "trp_npc4", slot_lord_reputation_type, lrep_cunning), #
            
            
            (troop_set_slot, "trp_npc5", slot_troop_morality_type, tmt_egalitarian),  #beheshtur
            (troop_set_slot, "trp_npc5", slot_troop_morality_value, 3),  #beheshtur
            (troop_set_slot, "trp_npc5", slot_troop_2ary_morality_type, -1),
            (troop_set_slot, "trp_npc5", slot_troop_2ary_morality_value, 0),
            (troop_set_slot, "trp_npc5", slot_troop_personalityclash_object, "trp_npc2"),  #beheshtur - marnid
            (troop_set_slot, "trp_npc5", slot_troop_personalityclash2_object, "trp_npc11"),  #beheshtur- katrin
            (troop_set_slot, "trp_npc5", slot_troop_personalitymatch_object, "trp_npc21"),  #beheshtur - ghazwan
            (troop_set_slot, "trp_npc5", slot_troop_home, "p_town_14"), #Halmar
            (troop_set_slot, "trp_npc5", slot_troop_payment_request, 400),
            (troop_set_slot, "trp_npc5", slot_troop_kingsupport_argument, argument_ruler),
            (troop_set_slot, "trp_npc5", slot_troop_kingsupport_opponent, "trp_npc17"), #Floris
            (troop_set_slot, "trp_npc5", slot_troop_town_with_contacts, "p_town_10"), #tulga
            (troop_set_slot, "trp_npc5", slot_troop_original_faction, "fac_kingdom_3"), #khergit
            (troop_set_slot, "trp_npc5", slot_lord_reputation_type, lrep_cunning), #
            
            
            
            (troop_set_slot, "trp_npc6", slot_troop_morality_type, tmt_humanitarian), #firenz
            (troop_set_slot, "trp_npc6", slot_troop_morality_value, 2),  #beheshtur
            (troop_set_slot, "trp_npc6", slot_troop_2ary_morality_type, tmt_honest),
            (troop_set_slot, "trp_npc6", slot_troop_2ary_morality_value, 1),
            (troop_set_slot, "trp_npc6", slot_troop_personalityclash_object, "trp_npc11"), #firentis - katrin
            (troop_set_slot, "trp_npc6", slot_troop_personalityclash2_object, "trp_npc13"), #firenz - nizar
            (troop_set_slot, "trp_npc6", slot_troop_personalitymatch_object, "trp_npc17"),  #firenz - floris
            (troop_set_slot, "trp_npc6", slot_troop_home, "p_town_4"), #Suno
            (troop_set_slot, "trp_npc6", slot_troop_payment_request, 0),
            (troop_set_slot, "trp_npc6", slot_troop_kingsupport_argument, argument_victory),
            (troop_set_slot, "trp_npc6", slot_troop_kingsupport_opponent, "trp_npc8"), #Matheld
            (troop_set_slot, "trp_npc6", slot_troop_town_with_contacts, "p_town_7"), #uxkhal
            (troop_set_slot, "trp_npc6", slot_troop_original_faction, "fac_kingdom_1"), #swadia
            (troop_set_slot, "trp_npc6", slot_lord_reputation_type, lrep_upstanding), #
            
            
            
            (troop_set_slot, "trp_npc7", slot_troop_morality_type, tmt_egalitarian),  #deshavi
            (troop_set_slot, "trp_npc7", slot_troop_morality_value, 3),  #beheshtur
            (troop_set_slot, "trp_npc7", slot_troop_2ary_morality_type, -1),
            (troop_set_slot, "trp_npc7", slot_troop_2ary_morality_value, 0),
            (troop_set_slot, "trp_npc7", slot_troop_personalityclash_object, "trp_npc1"),  #deshavi - borcha
            (troop_set_slot, "trp_npc7", slot_troop_personalityclash2_object, "trp_npc4"),  #deshavi - rolf
            (troop_set_slot, "trp_npc7", slot_troop_personalitymatch_object, "trp_npc16"),  #deshavi - klethi
            (troop_set_slot, "trp_npc7", slot_troop_home, "p_village_5"), #Kulum
			(troop_set_slot, "trp_npc7", slot_troop_payment_request, 300),
            (troop_set_slot, "trp_npc7", slot_troop_kingsupport_argument, argument_victory),
            (troop_set_slot, "trp_npc7", slot_troop_kingsupport_opponent, "trp_npc22"), #Edwyn
            (troop_set_slot, "trp_npc7", slot_troop_town_with_contacts, "p_town_2"), #tihr
            (troop_set_slot, "trp_npc7", slot_troop_original_faction, 0), #swadia
            (troop_set_slot, "trp_npc7", slot_lord_reputation_type, lrep_custodian), #
            
            
            
            (troop_set_slot, "trp_npc8", slot_troop_morality_type, tmt_aristocratic), #matheld
            (troop_set_slot, "trp_npc8", slot_troop_morality_value, 3),  #beheshtur
            (troop_set_slot, "trp_npc8", slot_troop_2ary_morality_type, -1),
            (troop_set_slot, "trp_npc8", slot_troop_2ary_morality_value, 0),
            (troop_set_slot, "trp_npc8", slot_troop_personalityclash_object, "trp_npc12"), #matheld - jeremus
            (troop_set_slot, "trp_npc8", slot_troop_personalityclash2_object, "trp_npc22"), #matheld - edwyn
            (troop_set_slot, "trp_npc8", slot_troop_personalitymatch_object, "trp_npc13"),  #matheld - nizar
            (troop_set_slot, "trp_npc8", slot_troop_home, "p_sea_raider_spawn_point_2"), #Gundig's Point
            (troop_set_slot, "trp_npc8", slot_troop_payment_request, 500),
            (troop_set_slot, "trp_npc8", slot_troop_kingsupport_argument, argument_lords),
            (troop_set_slot, "trp_npc8", slot_troop_kingsupport_opponent, "trp_npc2"), #Marnid
            (troop_set_slot, "trp_npc8", slot_troop_town_with_contacts, "p_town_12"), #wercheg
            (troop_set_slot, "trp_npc8", slot_troop_original_faction, "fac_kingdom_4"), #nords
            (troop_set_slot, "trp_npc8", slot_lord_reputation_type, lrep_martial), #
            
            
            (troop_set_slot, "trp_npc9", slot_troop_morality_type, tmt_aristocratic), #alayen
            (troop_set_slot, "trp_npc9", slot_troop_morality_value, 2),  #beheshtur
            (troop_set_slot, "trp_npc9", slot_troop_2ary_morality_type, tmt_honest),
            (troop_set_slot, "trp_npc9", slot_troop_2ary_morality_value, 1),
            (troop_set_slot, "trp_npc9", slot_troop_personalityclash_object, "trp_npc17"), #alayen - floris
            (troop_set_slot, "trp_npc9", slot_troop_personalityclash2_object, "trp_npc19"), #alayen - odval
            (troop_set_slot, "trp_npc9", slot_troop_personalitymatch_object, "trp_npc3"),  #alayen - ymira
            (troop_set_slot, "trp_npc9", slot_troop_home, "p_town_13"), #Rivacheg
            (troop_set_slot, "trp_npc9", slot_troop_payment_request, 300),
            (troop_set_slot, "trp_npc9", slot_troop_kingsupport_argument, argument_lords),
            (troop_set_slot, "trp_npc9", slot_troop_kingsupport_opponent, "trp_npc1"), #Borcha
            (troop_set_slot, "trp_npc9", slot_troop_town_with_contacts, "p_town_8"), #reyvadin
            (troop_set_slot, "trp_npc9", slot_troop_original_faction, "fac_kingdom_2"), #vaegirs
            (troop_set_slot, "trp_npc9", slot_lord_reputation_type, lrep_martial), #
            
            
            (troop_set_slot, "trp_npc10", slot_troop_morality_type, tmt_humanitarian), #bunduk
            (troop_set_slot, "trp_npc10", slot_troop_morality_value, 2),
            (troop_set_slot, "trp_npc10", slot_troop_2ary_morality_type, tmt_egalitarian),
            (troop_set_slot, "trp_npc10", slot_troop_2ary_morality_value, 1),
            (troop_set_slot, "trp_npc10", slot_troop_personalityclash_object, "trp_npc4"), #bunduk - rolf
            (troop_set_slot, "trp_npc10", slot_troop_personalityclash2_object, "trp_npc14"), #bunduk - lazalet
            (troop_set_slot, "trp_npc10", slot_troop_personalitymatch_object, "trp_npc11"),  #bunduk likes katrin
            (troop_set_slot, "trp_npc10", slot_troop_home, "p_castle_28"), #Grunwalder Castle
            (troop_set_slot, "trp_npc10", slot_troop_payment_request, 200),
            (troop_set_slot, "trp_npc10", slot_troop_kingsupport_argument, argument_ruler),
            (troop_set_slot, "trp_npc10", slot_troop_kingsupport_opponent, "trp_npc7"), #Deshavi
            (troop_set_slot, "trp_npc10", slot_troop_town_with_contacts, "p_town_5"), #jelkala
            (troop_set_slot, "trp_npc10", slot_troop_original_faction, "fac_kingdom_5"), #rhodoks
            (troop_set_slot, "trp_npc10", slot_lord_reputation_type, lrep_benefactor), #
            
            
            
            (troop_set_slot, "trp_npc11", slot_troop_morality_type, tmt_egalitarian),  #katrin
            (troop_set_slot, "trp_npc11", slot_troop_morality_value, 3),
            (troop_set_slot, "trp_npc11", slot_troop_2ary_morality_type, -1),
            (troop_set_slot, "trp_npc11", slot_troop_2ary_morality_value, 0),
            (troop_set_slot, "trp_npc11", slot_troop_personalityclash_object, "trp_npc6"),  #katrin - firenz
            (troop_set_slot, "trp_npc11", slot_troop_personalityclash2_object, "trp_npc5"),  #katrin - beheshtur
            (troop_set_slot, "trp_npc11", slot_troop_personalitymatch_object, "trp_npc10"),  #katrin likes bunduk
            (troop_set_slot, "trp_npc11", slot_troop_home, "p_town_6"), #Praven
            (troop_set_slot, "trp_npc11", slot_troop_payment_request, 100),
            (troop_set_slot, "trp_npc11", slot_troop_kingsupport_argument, argument_claim),
            (troop_set_slot, "trp_npc11", slot_troop_kingsupport_opponent, "trp_npc15"), #Artimenner
            (troop_set_slot, "trp_npc11", slot_troop_town_with_contacts, "p_town_6"), #praven
            (troop_set_slot, "trp_npc11", slot_troop_original_faction, 0), #
            (troop_set_slot, "trp_npc11", slot_lord_reputation_type, lrep_custodian), #
            
            
            (troop_set_slot, "trp_npc12", slot_troop_morality_type, tmt_humanitarian), #jeremus
            (troop_set_slot, "trp_npc12", slot_troop_morality_value, 3),
            (troop_set_slot, "trp_npc12", slot_troop_2ary_morality_type, -1),
            (troop_set_slot, "trp_npc12", slot_troop_2ary_morality_value, 0),
            (troop_set_slot, "trp_npc12", slot_troop_personalityclash_object, "trp_npc8"), #jeremus - matheld
            (troop_set_slot, "trp_npc12", slot_troop_personalityclash2_object, "trp_npc15"), #jeremus - artimenner
            (troop_set_slot, "trp_npc12", slot_troop_personalitymatch_object, "trp_npc19"),  #jeremus - odval
            (troop_set_slot, "trp_npc12", slot_troop_home, "p_castle_16"), #Almerra Castle
            (troop_set_slot, "trp_npc12", slot_troop_payment_request, 0),
            (troop_set_slot, "trp_npc12", slot_troop_kingsupport_argument, argument_claim),
            (troop_set_slot, "trp_npc12", slot_troop_kingsupport_opponent, "trp_npc13"), #Nizar
            (troop_set_slot, "trp_npc12", slot_troop_town_with_contacts, "p_town_14"), #halmar
            (troop_set_slot, "trp_npc12", slot_troop_original_faction, 0), #
            (troop_set_slot, "trp_npc12", slot_lord_reputation_type, lrep_benefactor), #
            
            
            
            (troop_set_slot, "trp_npc13", slot_troop_morality_type, tmt_aristocratic), #nizar
            (troop_set_slot, "trp_npc13", slot_troop_morality_value, 3),
            (troop_set_slot, "trp_npc13", slot_troop_2ary_morality_type, -1),
            (troop_set_slot, "trp_npc13", slot_troop_2ary_morality_value, 0),
            (troop_set_slot, "trp_npc13", slot_troop_personalityclash_object, "trp_npc18"), #nizar - nadia
            (troop_set_slot, "trp_npc13", slot_troop_personalityclash2_object, "trp_npc6"), #nizar - firenz
            (troop_set_slot, "trp_npc13", slot_troop_personalitymatch_object, "trp_npc8"), #nizar - matheld
            (troop_set_slot, "trp_npc13", slot_troop_home, "p_castle_15"), #Ergellon Castle
            (troop_set_slot, "trp_npc13", slot_troop_payment_request, 300),
            (troop_set_slot, "trp_npc13", slot_troop_kingsupport_argument, argument_claim),
            (troop_set_slot, "trp_npc13", slot_troop_kingsupport_opponent, "trp_npc10"), #Bunduk
            (troop_set_slot, "trp_npc13", slot_troop_town_with_contacts, "p_town_4"), #suno
            (troop_set_slot, "trp_npc13", slot_troop_original_faction, 0), #
            (troop_set_slot, "trp_npc13", slot_lord_reputation_type, lrep_roguish), #
            
            
            
            (troop_set_slot, "trp_npc14", slot_troop_morality_type, tmt_aristocratic), #lezalit
            (troop_set_slot, "trp_npc14", slot_troop_morality_value, 4),
            (troop_set_slot, "trp_npc14", slot_troop_2ary_morality_type, tmt_egalitarian),
            (troop_set_slot, "trp_npc14", slot_troop_2ary_morality_value, -1),
            (troop_set_slot, "trp_npc14", slot_troop_personalityclash_object, "trp_npc22"), #lezalit - edwyn
            (troop_set_slot, "trp_npc14", slot_troop_personalityclash2_object, "trp_npc10"), #lezalit - bunduk
            (troop_set_slot, "trp_npc14", slot_troop_personalitymatch_object, "trp_npc15"), #lezalit - artimenner
            (troop_set_slot, "trp_npc14", slot_troop_home, "p_castle_18"), #Ismirala Castle
            (troop_set_slot, "trp_npc14", slot_troop_payment_request, 400),
            (troop_set_slot, "trp_npc14", slot_troop_kingsupport_argument, argument_victory),
            (troop_set_slot, "trp_npc14", slot_troop_kingsupport_opponent, "trp_npc11"), #Katrin
            (troop_set_slot, "trp_npc14", slot_troop_town_with_contacts, "p_town_16"), #dhirim
            (troop_set_slot, "trp_npc14", slot_troop_original_faction, 0), #
            (troop_set_slot, "trp_npc14", slot_lord_reputation_type, lrep_selfrighteous), #
            
            
            (troop_set_slot, "trp_npc15", slot_troop_morality_type, tmt_egalitarian),  #artimenner
            (troop_set_slot, "trp_npc15", slot_troop_morality_value, 2),
            (troop_set_slot, "trp_npc15", slot_troop_2ary_morality_type, tmt_honest),
            (troop_set_slot, "trp_npc15", slot_troop_2ary_morality_value, 1),
            (troop_set_slot, "trp_npc15", slot_troop_personalityclash_object, "trp_npc21"), #artimenner - ghazwan
            (troop_set_slot, "trp_npc15", slot_troop_personalityclash2_object, "trp_npc12"), #artimenner - jeremus
            (troop_set_slot, "trp_npc15", slot_troop_personalitymatch_object, "trp_npc14"), #lazalit - artimenner
            (troop_set_slot, "trp_npc15", slot_troop_home, "p_castle_1"), #Culmarr Castle
            (troop_set_slot, "trp_npc15", slot_troop_payment_request, 300),
            (troop_set_slot, "trp_npc15", slot_troop_kingsupport_argument, argument_ruler),
            (troop_set_slot, "trp_npc15", slot_troop_kingsupport_opponent, "trp_npc4"), #Rolf
            (troop_set_slot, "trp_npc15", slot_troop_town_with_contacts, "p_town_18"), #narra
            (troop_set_slot, "trp_npc15", slot_lord_reputation_type, lrep_custodian), #
            
            
            (troop_set_slot, "trp_npc16", slot_troop_morality_type, tmt_aristocratic), #klethi
            (troop_set_slot, "trp_npc16", slot_troop_morality_value, 4),
            (troop_set_slot, "trp_npc16", slot_troop_2ary_morality_type, tmt_humanitarian),
            (troop_set_slot, "trp_npc16", slot_troop_2ary_morality_value, -1),
            (troop_set_slot, "trp_npc16", slot_troop_personalityclash_object, "trp_npc20"), #klethi - sajjad
            (troop_set_slot, "trp_npc16", slot_troop_personalityclash2_object, "trp_npc17"), #klethi - floris
            (troop_set_slot, "trp_npc16", slot_troop_personalitymatch_object, "trp_npc7"),  #deshavi - klethi
            (troop_set_slot, "trp_npc16", slot_troop_home, "p_village_20"), #Uslum
            (troop_set_slot, "trp_npc16", slot_troop_payment_request, 200),
            (troop_set_slot, "trp_npc16", slot_troop_kingsupport_argument, argument_lords),
            (troop_set_slot, "trp_npc16", slot_troop_kingsupport_opponent, "trp_npc12"), #Jeremus
            (troop_set_slot, "trp_npc16", slot_troop_town_with_contacts, "p_town_9"), #khudan
            (troop_set_slot, "trp_npc16", slot_lord_reputation_type, lrep_roguish), #
            
            ##Floris begin
            #Note: this is one part of three. The other two can be found in module_strings.py and module_troops.py.
            (troop_set_slot, "trp_npc17", slot_troop_morality_type, tmt_egalitarian),  #floris
            (troop_set_slot, "trp_npc17", slot_troop_morality_value, 2),
            (troop_set_slot, "trp_npc17", slot_troop_2ary_morality_type, tmt_aristocratic),
            (troop_set_slot, "trp_npc17", slot_troop_2ary_morality_value, 1),
            (troop_set_slot, "trp_npc17", slot_troop_personalityclash_object, "trp_npc16"), #floris - klethi
            (troop_set_slot, "trp_npc17", slot_troop_personalityclash2_object, "trp_npc9"), #floris - alayen
            (troop_set_slot, "trp_npc17", slot_troop_personalitymatch_object, "trp_npc6"), #firentis - floris
            (troop_set_slot, "trp_npc17", slot_troop_home, "p_town_9"), #Khudan
            (troop_set_slot, "trp_npc17", slot_troop_payment_request, 20000),
            (troop_set_slot, "trp_npc17", slot_troop_kingsupport_argument, argument_ruler),
            (troop_set_slot, "trp_npc17", slot_troop_kingsupport_opponent, "trp_npc21"), #Ghazwan
            (troop_set_slot, "trp_npc17", slot_troop_town_with_contacts, "p_town_16"), #dhirim
            (troop_set_slot, "trp_npc17", slot_lord_reputation_type, lrep_goodnatured), #
            
            (troop_set_slot, "trp_npc18", slot_troop_morality_type, tmt_humanitarian),  #nadia
            (troop_set_slot, "trp_npc18", slot_troop_morality_value, 4),
            (troop_set_slot, "trp_npc18", slot_troop_2ary_morality_type, tmt_honest),
            (troop_set_slot, "trp_npc18", slot_troop_2ary_morality_value, 1),
            (troop_set_slot, "trp_npc18", slot_troop_personalityclash_object, "trp_npc2"), #nadia - marnid
            (troop_set_slot, "trp_npc18", slot_troop_personalityclash2_object, "trp_npc13"), #nadia - nizar
            (troop_set_slot, "trp_npc18", slot_troop_personalitymatch_object, "trp_npc22"), #nadia - edwyn
            (troop_set_slot, "trp_npc18", slot_troop_home, "p_village_97"), #Sekhtem
            (troop_set_slot, "trp_npc18", slot_troop_payment_request, 0),
            (troop_set_slot, "trp_npc18", slot_troop_kingsupport_argument, argument_claim),
            (troop_set_slot, "trp_npc18", slot_troop_kingsupport_opponent, "trp_npc9"), #Alayan
            (troop_set_slot, "trp_npc18", slot_troop_town_with_contacts, "p_town_21"), #ahmerrad
            (troop_set_slot, "trp_npc18", slot_troop_original_faction, "fac_kingdom_6"), #
            (troop_set_slot, "trp_npc18", slot_lord_reputation_type, lrep_benefactor), #
            
            (troop_set_slot, "trp_npc19", slot_troop_morality_type, tmt_egalitarian),  #odval
            (troop_set_slot, "trp_npc19", slot_troop_morality_value, 2),
            (troop_set_slot, "trp_npc19", slot_troop_2ary_morality_type, -1),
            (troop_set_slot, "trp_npc19", slot_troop_2ary_morality_value, 0),
            (troop_set_slot, "trp_npc19", slot_troop_personalityclash_object, "trp_npc3"), #odval - ymira
            (troop_set_slot, "trp_npc19", slot_troop_personalityclash2_object, "trp_npc9"), #odval - alayen
            (troop_set_slot, "trp_npc19", slot_troop_personalitymatch_object, "trp_npc12"), #odval - jeremus
            (troop_set_slot, "trp_npc19", slot_troop_home, "p_village_88"), #Tulbuk
            (troop_set_slot, "trp_npc19", slot_troop_payment_request, 200),
            (troop_set_slot, "trp_npc19", slot_troop_kingsupport_argument, argument_victory),
            (troop_set_slot, "trp_npc19", slot_troop_kingsupport_opponent, "trp_npc20"), #Sajjad
            (troop_set_slot, "trp_npc19", slot_troop_town_with_contacts, "p_town_17"), #ichamur
            (troop_set_slot, "trp_npc19", slot_troop_original_faction, "fac_kingdom_3"), #
            (troop_set_slot, "trp_npc19", slot_lord_reputation_type, lrep_roguish), #
            
            (troop_set_slot, "trp_npc20", slot_troop_morality_type, tmt_egalitarian),  #sajjad
            (troop_set_slot, "trp_npc20", slot_troop_morality_value, 2),
            (troop_set_slot, "trp_npc20", slot_troop_2ary_morality_type, tmt_honest),
            (troop_set_slot, "trp_npc20", slot_troop_2ary_morality_value, 1),
            (troop_set_slot, "trp_npc20", slot_troop_personalityclash_object, "trp_npc3"), #sajjad - ymira
            (troop_set_slot, "trp_npc20", slot_troop_personalityclash2_object, "trp_npc16"), #sajjad - klethi
            (troop_set_slot, "trp_npc20", slot_troop_personalitymatch_object, "trp_npc4"), #sajjad - rolf
            (troop_set_slot, "trp_npc20", slot_troop_home, "p_desert_bandit_spawn_point"), #Sarrdak Desert
            (troop_set_slot, "trp_npc20", slot_troop_payment_request, 300),
            (troop_set_slot, "trp_npc20", slot_troop_kingsupport_argument, argument_ruler),
            (troop_set_slot, "trp_npc20", slot_troop_kingsupport_opponent, "trp_npc18"), #Nadia
            (troop_set_slot, "trp_npc20", slot_troop_town_with_contacts, "p_town_20"), #durquba
            (troop_set_slot, "trp_npc20", slot_troop_original_faction, "fac_kingdom_6"), #
            (troop_set_slot, "trp_npc20", slot_lord_reputation_type, lrep_roguish), #
            
            (troop_set_slot, "trp_npc21", slot_troop_morality_type, tmt_aristocratic),  #ghazwan
            (troop_set_slot, "trp_npc21", slot_troop_morality_value, 2),
            (troop_set_slot, "trp_npc21", slot_troop_2ary_morality_type, tmt_humanitarian),
            (troop_set_slot, "trp_npc21", slot_troop_2ary_morality_value, 1),
            (troop_set_slot, "trp_npc21", slot_troop_personalityclash_object, "trp_npc1"), #ghazwan - borcha
            (troop_set_slot, "trp_npc21", slot_troop_personalityclash2_object, "trp_npc15"), #ghazwan - artimenner
            (troop_set_slot, "trp_npc21", slot_troop_personalitymatch_object, "trp_npc5"), #ghazwan - baheshtur
            (troop_set_slot, "trp_npc21", slot_troop_home, "p_town_19"), #shariz
            (troop_set_slot, "trp_npc21", slot_troop_payment_request, 400),
            (troop_set_slot, "trp_npc21", slot_troop_kingsupport_argument, argument_lords),
            (troop_set_slot, "trp_npc21", slot_troop_kingsupport_opponent, "trp_npc19"), #Odval
            (troop_set_slot, "trp_npc21", slot_troop_town_with_contacts, "p_town_19"), #shariz
            (troop_set_slot, "trp_npc21", slot_troop_original_faction, "fac_kingdom_6"), #
            (troop_set_slot, "trp_npc21", slot_lord_reputation_type, lrep_martial), #

            (troop_set_slot, "trp_npc22", slot_troop_morality_type, tmt_humanitarian),  #edwyn
            (troop_set_slot, "trp_npc22", slot_troop_morality_value, 2),
            (troop_set_slot, "trp_npc22", slot_troop_2ary_morality_type, tmt_honest),
            (troop_set_slot, "trp_npc22", slot_troop_2ary_morality_value, 1),
            (troop_set_slot, "trp_npc22", slot_troop_personalityclash_object, "trp_npc8"), #edwyn - matheld
            (troop_set_slot, "trp_npc22", slot_troop_personalityclash2_object, "trp_npc14"), #edwyn - lezalit
            (troop_set_slot, "trp_npc22", slot_troop_personalitymatch_object, "trp_npc18"), #edwyn - nadia
            (troop_set_slot, "trp_npc22", slot_troop_home, "p_village_38"), #ibiran
            (troop_set_slot, "trp_npc22", slot_troop_payment_request, 300),
            (troop_set_slot, "trp_npc22", slot_troop_kingsupport_argument, argument_victory),
            (troop_set_slot, "trp_npc22", slot_troop_kingsupport_opponent, "trp_npc3"), #Ymira
            (troop_set_slot, "trp_npc22", slot_troop_town_with_contacts, "p_town_7"), #uxkhal
            (troop_set_slot, "trp_npc22", slot_troop_original_faction, "fac_kingdom_1"), #
            (troop_set_slot, "trp_npc22", slot_lord_reputation_type, lrep_custodian), #

##Extra Companions set 1
#            (troop_set_slot, "trp_npc23", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc23", slot_troop_morality_value, 4),  #
#            (troop_set_slot, "trp_npc23", slot_troop_2ary_morality_type, tmt_aristocratic),  #
#            (troop_set_slot, "trp_npc23", slot_troop_2ary_morality_value, -1),
#            (troop_set_slot, "trp_npc23", slot_troop_personalityclash_object, "trp_npc29"),  #
#            (troop_set_slot, "trp_npc23", slot_troop_personalityclash2_object, "trp_npc43"),  #
#            (troop_set_slot, "trp_npc23", slot_troop_personalitymatch_object, "trp_npc24"),  #
#            (troop_set_slot, "trp_npc23", slot_troop_home, "p_village_1"), #
#            (troop_set_slot, "trp_npc23", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc23", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc23", slot_troop_kingsupport_opponent, "trp_npc31"), #
#            (troop_set_slot, "trp_npc23", slot_troop_town_with_contacts, "p_town_16"), #
#            (troop_set_slot, "trp_npc23", slot_troop_original_faction, fac_kingdom_1), #
#            (troop_set_slot, "trp_npc23", slot_lord_reputation_type, lrep_roguish), #
#            
#            
#            (troop_set_slot, "trp_npc24", slot_troop_morality_type, tmt_humanitarian), #
#            (troop_set_slot, "trp_npc24", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc24", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc24", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc24", slot_troop_personalityclash_object, "trp_npc27"), #
#            (troop_set_slot, "trp_npc24", slot_troop_personalityclash2_object, "trp_npc40"), #
#            (troop_set_slot, "trp_npc24", slot_troop_personalitymatch_object, "trp_npc23"),  #
#            (troop_set_slot, "trp_npc24", slot_troop_home, "p_town_8"), #
#            (troop_set_slot, "trp_npc24", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc24", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc24", slot_troop_kingsupport_opponent, "trp_npc30"), #
#            (troop_set_slot, "trp_npc24", slot_troop_town_with_contacts, "p_town_8"), #
#            (troop_set_slot, "trp_npc24", slot_troop_original_faction, fac_kingdom_2), #
#            (troop_set_slot, "trp_npc24", slot_lord_reputation_type, lrep_custodian), #
#
#
#            (troop_set_slot, "trp_npc25", slot_troop_morality_type, tmt_humanitarian), #
#            (troop_set_slot, "trp_npc25", slot_troop_morality_value, 4),
#            (troop_set_slot, "trp_npc25", slot_troop_2ary_morality_type, tmt_aristocratic),
#            (troop_set_slot, "trp_npc25", slot_troop_2ary_morality_value, -1),
#            (troop_set_slot, "trp_npc25", slot_troop_personalityclash_object, "trp_npc41"), #
#            (troop_set_slot, "trp_npc25", slot_troop_personalityclash2_object, "trp_npc42"), #
#            (troop_set_slot, "trp_npc25", slot_troop_personalitymatch_object, "trp_npc31"), #
#            (troop_set_slot, "trp_npc25", slot_troop_home, "p_castle_37"), #
#            (troop_set_slot, "trp_npc25", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc25", slot_troop_kingsupport_argument, argument_lords),
#            (troop_set_slot, "trp_npc25", slot_troop_kingsupport_opponent, "trp_npc44"), #
#            (troop_set_slot, "trp_npc25", slot_troop_town_with_contacts, "p_town_10"), #
#            (troop_set_slot, "trp_npc25", slot_troop_original_faction, fac_kingdom_3), #
#            (troop_set_slot, "trp_npc25", slot_lord_reputation_type, lrep_benefactor), #
#            
#            
#            (troop_set_slot, "trp_npc26", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc26", slot_troop_morality_value, 4),
#            (troop_set_slot, "trp_npc26", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc26", slot_troop_2ary_morality_value, -1),
#            (troop_set_slot, "trp_npc26", slot_troop_personalityclash_object, "trp_npc32"), #
#            (troop_set_slot, "trp_npc26", slot_troop_personalityclash2_object, "trp_npc29"), #
#            (troop_set_slot, "trp_npc26", slot_troop_personalitymatch_object, "trp_npc42"), #
#            (troop_set_slot, "trp_npc26", slot_troop_home, "p_village_80"), #
#            (troop_set_slot, "trp_npc26", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc26", slot_troop_kingsupport_argument, argument_claim),
#            (troop_set_slot, "trp_npc26", slot_troop_kingsupport_opponent, "trp_npc37"), #
#            (troop_set_slot, "trp_npc26", slot_troop_town_with_contacts, "p_town_1"), #
#            (troop_set_slot, "trp_npc26", slot_troop_original_faction, fac_kingdom_4), #ichamur
#            (troop_set_slot, "trp_npc26", slot_lord_reputation_type, lrep_cunning), #
#            
#            
#            (troop_set_slot, "trp_npc27", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc27", slot_troop_morality_value, 3),  #
#            (troop_set_slot, "trp_npc27", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc27", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc27", slot_troop_personalityclash_object, "trp_npc24"),  #
#            (troop_set_slot, "trp_npc27", slot_troop_personalityclash2_object, "trp_npc33"),  #
#            (troop_set_slot, "trp_npc27", slot_troop_personalitymatch_object, "trp_npc43"),  #
#            (troop_set_slot, "trp_npc27", slot_troop_home, "p_town_15"), #
#            (troop_set_slot, "trp_npc27", slot_troop_payment_request, 400),
#            (troop_set_slot, "trp_npc27", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc27", slot_troop_kingsupport_opponent, "trp_npc25"), #
#            (troop_set_slot, "trp_npc27", slot_troop_town_with_contacts, "p_town_15"), #
#            (troop_set_slot, "trp_npc27", slot_troop_original_faction, "fac_kingdom_5"), #
#            (troop_set_slot, "trp_npc27", slot_lord_reputation_type, lrep_cunning), #
#            
#            
#            (troop_set_slot, "trp_npc28", slot_troop_morality_type, tmt_humanitarian), #
#            (troop_set_slot, "trp_npc28", slot_troop_morality_value, 2),  #
#            (troop_set_slot, "trp_npc28", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc28", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc28", slot_troop_personalityclash_object, "trp_npc33"), #
#            (troop_set_slot, "trp_npc28", slot_troop_personalityclash2_object, "trp_npc35"), #
#            (troop_set_slot, "trp_npc28", slot_troop_personalitymatch_object, "trp_npc39"),  #
#            (troop_set_slot, "trp_npc28", slot_troop_home, "p_castle_44"), #
#            (troop_set_slot, "trp_npc28", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc28", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc28", slot_troop_kingsupport_opponent, "trp_npc26"), #
#            (troop_set_slot, "trp_npc28", slot_troop_town_with_contacts, "p_town_22"), #
#            (troop_set_slot, "trp_npc28", slot_troop_original_faction, "fac_kingdom_6"), #
#            (troop_set_slot, "trp_npc28", slot_lord_reputation_type, lrep_upstanding), #
#            
#            
#            (troop_set_slot, "trp_npc29", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc29", slot_troop_morality_value, 3),  #
#            (troop_set_slot, "trp_npc29", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc29", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc29", slot_troop_personalityclash_object, "trp_npc23"),  #
#            (troop_set_slot, "trp_npc29", slot_troop_personalityclash2_object, "trp_npc26"),  #
#            (troop_set_slot, "trp_npc29", slot_troop_personalitymatch_object, "trp_npc38"),  #
#            (troop_set_slot, "trp_npc29", slot_troop_home, "p_village_13"), #
#			 (troop_set_slot, "trp_npc29", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc29", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc29", slot_troop_kingsupport_opponent, "trp_npc32"), #
#            (troop_set_slot, "trp_npc29", slot_troop_town_with_contacts, "p_town_6"), #
#            (troop_set_slot, "trp_npc29", slot_troop_original_faction, fac_kingdom_1), #
#            (troop_set_slot, "trp_npc29", slot_lord_reputation_type, lrep_custodian), #
#            
#            
#            (troop_set_slot, "trp_npc30", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc30", slot_troop_morality_value, 3),  #
#            (troop_set_slot, "trp_npc30", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc30", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc30", slot_troop_personalityclash_object, "trp_npc34"), #
#            (troop_set_slot, "trp_npc30", slot_troop_personalityclash2_object, "trp_npc44"), #
#            (troop_set_slot, "trp_npc30", slot_troop_personalitymatch_object, "trp_npc35"),  #
#            (troop_set_slot, "trp_npc30", slot_troop_home, "p_village_74"), #
#            (troop_set_slot, "trp_npc30", slot_troop_payment_request, 500),
#            (troop_set_slot, "trp_npc30", slot_troop_kingsupport_argument, argument_lords),
#            (troop_set_slot, "trp_npc30", slot_troop_kingsupport_opponent, "trp_npc28"), #
#            (troop_set_slot, "trp_npc30", slot_troop_town_with_contacts, "p_town_11"), #
#            (troop_set_slot, "trp_npc30", slot_troop_original_faction, "fac_kingdom_2"), #
#            (troop_set_slot, "trp_npc30", slot_lord_reputation_type, lrep_martial), #
#            
#            
#            (troop_set_slot, "trp_npc31", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc31", slot_troop_morality_value, 2),  #
#            (troop_set_slot, "trp_npc31", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc31", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc31", slot_troop_personalityclash_object, "trp_npc39"), #
#            (troop_set_slot, "trp_npc31", slot_troop_personalityclash2_object, "trp_npc41"), #
#            (troop_set_slot, "trp_npc31", slot_troop_personalitymatch_object, "trp_npc25"),  #
#            (troop_set_slot, "trp_npc31", slot_troop_home, "p_castle_7"), #
#            (troop_set_slot, "trp_npc31", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc31", slot_troop_kingsupport_argument, argument_lords),
#            (troop_set_slot, "trp_npc31", slot_troop_kingsupport_opponent, "trp_npc40"), #
#            (troop_set_slot, "trp_npc31", slot_troop_town_with_contacts, "p_town_18"), #
#            (troop_set_slot, "trp_npc31", slot_troop_original_faction, "fac_kingdom_3"), #
#            (troop_set_slot, "trp_npc31", slot_lord_reputation_type, lrep_martial), #
#            
#            
#            (troop_set_slot, "trp_npc32", slot_troop_morality_type, tmt_humanitarian), #
#            (troop_set_slot, "trp_npc32", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc32", slot_troop_2ary_morality_type, tmt_egalitarian),
#            (troop_set_slot, "trp_npc32", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc32", slot_troop_personalityclash_object, "trp_npc26"), #
#            (troop_set_slot, "trp_npc32", slot_troop_personalityclash2_object, "trp_npc36"), #
#            (troop_set_slot, "trp_npc32", slot_troop_personalitymatch_object, "trp_npc33"),  #
#            (troop_set_slot, "trp_npc32", slot_troop_home, "p_castle_32"), #
#            (troop_set_slot, "trp_npc32", slot_troop_payment_request, 200),
#            (troop_set_slot, "trp_npc32", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc32", slot_troop_kingsupport_opponent, "trp_npc35"), #
#            (troop_set_slot, "trp_npc32", slot_troop_town_with_contacts, "p_town_12"), #
#            (troop_set_slot, "trp_npc32", slot_troop_original_faction, "fac_kingdom_4"), #
#            (troop_set_slot, "trp_npc32", slot_lord_reputation_type, lrep_benefactor), #
#            
#            
#            (troop_set_slot, "trp_npc33", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc33", slot_troop_morality_value, 3),
#            (troop_set_slot, "trp_npc33", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc33", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc33", slot_troop_personalityclash_object, "trp_npc28"),  #
#            (troop_set_slot, "trp_npc33", slot_troop_personalityclash2_object, "trp_npc27"),  #
#            (troop_set_slot, "trp_npc33", slot_troop_personalitymatch_object, "trp_npc32"),  #
#            (troop_set_slot, "trp_npc33", slot_troop_home, "p_castle_21"), #
#            (troop_set_slot, "trp_npc33", slot_troop_payment_request, 100),
#            (troop_set_slot, "trp_npc33", slot_troop_kingsupport_argument, argument_claim),
#            (troop_set_slot, "trp_npc33", slot_troop_kingsupport_opponent, "trp_npc36"), #
#            (troop_set_slot, "trp_npc33", slot_troop_town_with_contacts, "p_town_3"), #
#            (troop_set_slot, "trp_npc33", slot_troop_original_faction, fac_kingdom_5), #
#            (troop_set_slot, "trp_npc33", slot_lord_reputation_type, lrep_custodian), #
#            
#            
#            (troop_set_slot, "trp_npc34", slot_troop_morality_type, tmt_humanitarian), #
#            (troop_set_slot, "trp_npc34", slot_troop_morality_value, 3),
#            (troop_set_slot, "trp_npc34", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc34", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc34", slot_troop_personalityclash_object, "trp_npc30"), #
#            (troop_set_slot, "trp_npc34", slot_troop_personalityclash2_object, "trp_npc37"), #
#            (troop_set_slot, "trp_npc34", slot_troop_personalitymatch_object, "trp_npc41"),  #
#            (troop_set_slot, "trp_npc34", slot_troop_home, "p_castle_41"), #
#            (troop_set_slot, "trp_npc34", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc34", slot_troop_kingsupport_argument, argument_claim),
#            (troop_set_slot, "trp_npc34", slot_troop_kingsupport_opponent, "trp_npc38"), #
#            (troop_set_slot, "trp_npc34", slot_troop_town_with_contacts, "p_town_21"), #
#            (troop_set_slot, "trp_npc34", slot_troop_original_faction, fac_kingdom_6), #
#            (troop_set_slot, "trp_npc34", slot_lord_reputation_type, lrep_benefactor), #
#            
#
#            (troop_set_slot, "trp_npc35", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc35", slot_troop_morality_value, 3),
#            (troop_set_slot, "trp_npc35", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc35", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc35", slot_troop_personalityclash_object, "trp_npc40"), #
#            (troop_set_slot, "trp_npc35", slot_troop_personalityclash2_object, "trp_npc28"), #
#            (troop_set_slot, "trp_npc35", slot_troop_personalitymatch_object, "trp_npc30"), #
#            (troop_set_slot, "trp_npc35", slot_troop_home, "p_castle_13"), #
#            (troop_set_slot, "trp_npc35", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc35", slot_troop_kingsupport_argument, argument_claim),
#            (troop_set_slot, "trp_npc35", slot_troop_kingsupport_opponent, "trp_npc24"), #
#            (troop_set_slot, "trp_npc35", slot_troop_town_with_contacts, "p_town_7"), #
#            (troop_set_slot, "trp_npc35", slot_troop_original_faction, fac_kingdom_1), #
#            (troop_set_slot, "trp_npc35", slot_lord_reputation_type, lrep_roguish), #
#            
#            
#            (troop_set_slot, "trp_npc36", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc36", slot_troop_morality_value, 4),
#            (troop_set_slot, "trp_npc36", slot_troop_2ary_morality_type, tmt_egalitarian),
#            (troop_set_slot, "trp_npc36", slot_troop_2ary_morality_value, -1),
#            (troop_set_slot, "trp_npc36", slot_troop_personalityclash_object, "trp_npc44"), #
#            (troop_set_slot, "trp_npc36", slot_troop_personalityclash2_object, "trp_npc32"), #
#            (troop_set_slot, "trp_npc36", slot_troop_personalitymatch_object, "trp_npc37"), #
#            (troop_set_slot, "trp_npc36", slot_troop_home, "p_castle_19"), #
#            (troop_set_slot, "trp_npc36", slot_troop_payment_request, 400),
#            (troop_set_slot, "trp_npc36", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc36", slot_troop_kingsupport_opponent, "trp_npc23"), #
#            (troop_set_slot, "trp_npc36", slot_troop_town_with_contacts, "p_town_9"), #
#            (troop_set_slot, "trp_npc36", slot_troop_original_faction, fac_kingdom_2), #
#            (troop_set_slot, "trp_npc36", slot_lord_reputation_type, lrep_selfrighteous), #
#            
#            
#            (troop_set_slot, "trp_npc37", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc37", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc37", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc37", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc37", slot_troop_personalityclash_object, "trp_npc43"), #
#            (troop_set_slot, "trp_npc37", slot_troop_personalityclash2_object, "trp_npc34"), #
#            (troop_set_slot, "trp_npc37", slot_troop_personalitymatch_object, "trp_npc36"), #
#            (troop_set_slot, "trp_npc37", slot_troop_home, "p_castle_28"), #
#            (troop_set_slot, "trp_npc37", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc37", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc37", slot_troop_kingsupport_opponent, "trp_npc33"), #
#            (troop_set_slot, "trp_npc37", slot_troop_town_with_contacts, "p_town_14"), #
#            (troop_set_slot, "trp_npc37", slot_troop_original_faction, fac_kingdom_3), #
#            (troop_set_slot, "trp_npc37", slot_lord_reputation_type, lrep_custodian), #
#            
#            
#            (troop_set_slot, "trp_npc38", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc38", slot_troop_morality_value, 4),
#            (troop_set_slot, "trp_npc38", slot_troop_2ary_morality_type, tmt_humanitarian),
#            (troop_set_slot, "trp_npc38", slot_troop_2ary_morality_value, -1),
#            (troop_set_slot, "trp_npc38", slot_troop_personalityclash_object, "trp_npc42"), #
#            (troop_set_slot, "trp_npc38", slot_troop_personalityclash2_object, "trp_npc39"), #
#            (troop_set_slot, "trp_npc38", slot_troop_personalitymatch_object, "trp_npc29"),  #
#            (troop_set_slot, "trp_npc38", slot_troop_home, "p_village_77"), #
#            (troop_set_slot, "trp_npc38", slot_troop_payment_request, 200),
#            (troop_set_slot, "trp_npc38", slot_troop_kingsupport_argument, argument_lords),
#            (troop_set_slot, "trp_npc38", slot_troop_kingsupport_opponent, "trp_npc24"), #
#            (troop_set_slot, "trp_npc38", slot_troop_town_with_contacts, "p_town_2"), #
#            (troop_set_slot, "trp_npc38", slot_troop_original_faction, fac_kingdom_4), #
#            (troop_set_slot, "trp_npc38", slot_lord_reputation_type, lrep_roguish), #
#
#
#            (troop_set_slot, "trp_npc39", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc39", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc39", slot_troop_2ary_morality_type, tmt_aristocratic),
#            (troop_set_slot, "trp_npc39", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc39", slot_troop_personalityclash_object, "trp_npc38"), #
#            (troop_set_slot, "trp_npc39", slot_troop_personalityclash2_object, "trp_npc31"), #
#            (troop_set_slot, "trp_npc39", slot_troop_personalitymatch_object, "trp_npc28"), #
#            (troop_set_slot, "trp_npc39", slot_troop_home, "p_castle_33"), #
#            (troop_set_slot, "trp_npc39", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc39", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc39", slot_troop_kingsupport_opponent, "trp_npc27"), #
#            (troop_set_slot, "trp_npc39", slot_troop_town_with_contacts, "p_town_5"), #
#            (troop_set_slot, "trp_npc39", slot_troop_original_faction, fac_kingdom_5), #
#            (troop_set_slot, "trp_npc39", slot_lord_reputation_type, lrep_goodnatured), #
#            
#
#            (troop_set_slot, "trp_npc40", slot_troop_morality_type, tmt_humanitarian),  #
#            (troop_set_slot, "trp_npc40", slot_troop_morality_value, 4),
#            (troop_set_slot, "trp_npc40", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc40", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc40", slot_troop_personalityclash_object, "trp_npc24"), #
#            (troop_set_slot, "trp_npc40", slot_troop_personalityclash2_object, "trp_npc35"), #
#            (troop_set_slot, "trp_npc40", slot_troop_personalitymatch_object, "trp_npc44"), #
#            (troop_set_slot, "trp_npc40", slot_troop_home, "p_village_100"), #
#            (troop_set_slot, "trp_npc40", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc40", slot_troop_kingsupport_argument, argument_claim),
#            (troop_set_slot, "trp_npc40", slot_troop_kingsupport_opponent, "trp_npc42"), #
#            (troop_set_slot, "trp_npc40", slot_troop_town_with_contacts, "p_town_20"), #
#            (troop_set_slot, "trp_npc40", slot_troop_original_faction, "fac_kingdom_6"), #
#            (troop_set_slot, "trp_npc40", slot_lord_reputation_type, lrep_benefactor), #
#            
#
#            (troop_set_slot, "trp_npc41", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc41", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc41", slot_troop_2ary_morality_type, tmt_pious),
#            (troop_set_slot, "trp_npc41", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc41", slot_troop_personalityclash_object, "trp_npc25"), #
#            (troop_set_slot, "trp_npc41", slot_troop_personalityclash2_object, "trp_npc31"), #
#            (troop_set_slot, "trp_npc41", slot_troop_personalitymatch_object, "trp_npc34"), #
#            (troop_set_slot, "trp_npc41", slot_troop_home, "p_village_15"), #
#            (troop_set_slot, "trp_npc41", slot_troop_payment_request, 200),
#            (troop_set_slot, "trp_npc41", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc41", slot_troop_kingsupport_opponent, "trp_npc43"), #
#            (troop_set_slot, "trp_npc41", slot_troop_town_with_contacts, "p_town_4"), #
#            (troop_set_slot, "trp_npc41", slot_troop_original_faction, "fac_kingdom_1"), #
#            (troop_set_slot, "trp_npc41", slot_lord_reputation_type, lrep_custodian), #
#            
#
#            (troop_set_slot, "trp_npc42", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc42", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc42", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc42", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc42", slot_troop_personalityclash_object, "trp_npc25"), #
#            (troop_set_slot, "trp_npc42", slot_troop_personalityclash2_object, "trp_npc38"), #
#            (troop_set_slot, "trp_npc42", slot_troop_personalitymatch_object, "trp_npc26"), #
#            (troop_set_slot, "trp_npc42", slot_troop_home, "p_village_66"), #
#            (troop_set_slot, "trp_npc42", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc42", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc42", slot_troop_kingsupport_opponent, "trp_npc41"), #
#            (troop_set_slot, "trp_npc42", slot_troop_town_with_contacts, "p_town_13"), #
#            (troop_set_slot, "trp_npc42", slot_troop_original_faction, "fac_kingdom_2"), #
#            (troop_set_slot, "trp_npc42", slot_lord_reputation_type, lrep_roguish), #
#            
#
#            (troop_set_slot, "trp_npc43", slot_troop_morality_type, tmt_aristocratic),  #
#            (troop_set_slot, "trp_npc43", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc43", slot_troop_2ary_morality_type, tmt_humanitarian),
#            (troop_set_slot, "trp_npc43", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc43", slot_troop_personalityclash_object, "trp_npc23"), #
#            (troop_set_slot, "trp_npc43", slot_troop_personalityclash2_object, "trp_npc37"), #
#            (troop_set_slot, "trp_npc43", slot_troop_personalitymatch_object, "trp_npc27"), #
#            (troop_set_slot, "trp_npc43", slot_troop_home, "p_town_17"), #shariz
#            (troop_set_slot, "trp_npc43", slot_troop_payment_request, 400),
#            (troop_set_slot, "trp_npc43", slot_troop_kingsupport_argument, argument_lords),
#            (troop_set_slot, "trp_npc43", slot_troop_kingsupport_opponent, "trp_npc39"), #
#            (troop_set_slot, "trp_npc43", slot_troop_town_with_contacts, "p_town_17"), #
#            (troop_set_slot, "trp_npc43", slot_troop_original_faction, "fac_kingdom_3"), #
#            (troop_set_slot, "trp_npc43", slot_lord_reputation_type, lrep_martial), #
#
#
#            (troop_set_slot, "trp_npc44", slot_troop_morality_type, tmt_humanitarian),  #
#            (troop_set_slot, "trp_npc44", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc44", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc44", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc44", slot_troop_personalityclash_object, "trp_npc30"), #
#            (troop_set_slot, "trp_npc44", slot_troop_personalityclash2_object, "trp_npc36"), #
#            (troop_set_slot, "trp_npc44", slot_troop_personalitymatch_object, "trp_npc40"), #
#            (troop_set_slot, "trp_npc44", slot_troop_home, "p_village_31"), #
#            (troop_set_slot, "trp_npc44", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc44", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc44", slot_troop_kingsupport_opponent, "trp_npc29"), #
#            (troop_set_slot, "trp_npc44", slot_troop_town_with_contacts, "p_town_12"), #
#            (troop_set_slot, "trp_npc44", slot_troop_original_faction, "fac_kingdom_4"), #
#            (troop_set_slot, "trp_npc44", slot_lord_reputation_type, lrep_custodian), #
#
##Extra Companions set 2
#            (troop_set_slot, "trp_npc45", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc45", slot_troop_morality_value, 4),  #
#            (troop_set_slot, "trp_npc45", slot_troop_2ary_morality_type, tmt_aristocratic),  #
#            (troop_set_slot, "trp_npc45", slot_troop_2ary_morality_value, -1),
#            (troop_set_slot, "trp_npc45", slot_troop_personalityclash_object, "trp_npc51"),  #
#            (troop_set_slot, "trp_npc45", slot_troop_personalityclash2_object, "trp_npc65"),  #
#            (troop_set_slot, "trp_npc45", slot_troop_personalitymatch_object, "trp_npc46"),  #
#            (troop_set_slot, "trp_npc45", slot_troop_home, "p_village_32"), #
#            (troop_set_slot, "trp_npc45", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc45", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc45", slot_troop_kingsupport_opponent, "trp_npc53"), #
#            (troop_set_slot, "trp_npc45", slot_troop_town_with_contacts, "p_town_4"), #
#            (troop_set_slot, "trp_npc45", slot_troop_original_faction, fac_kingdom_1), #
#            (troop_set_slot, "trp_npc45", slot_lord_reputation_type, lrep_roguish), #
#            
#            
#            (troop_set_slot, "trp_npc46", slot_troop_morality_type, tmt_humanitarian), #
#            (troop_set_slot, "trp_npc46", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc46", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc46", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc46", slot_troop_personalityclash_object, "trp_npc49"), #
#            (troop_set_slot, "trp_npc46", slot_troop_personalityclash2_object, "trp_npc62"), #
#            (troop_set_slot, "trp_npc46", slot_troop_personalitymatch_object, "trp_npc45"),  #
#            (troop_set_slot, "trp_npc46", slot_troop_home, "p_town_20"), #
#            (troop_set_slot, "trp_npc46", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc46", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc46", slot_troop_kingsupport_opponent, "trp_npc52"), #
#            (troop_set_slot, "trp_npc46", slot_troop_town_with_contacts, "p_town_22"), #
#            (troop_set_slot, "trp_npc46", slot_troop_original_faction, fac_kingdom_6), #
#            (troop_set_slot, "trp_npc46", slot_lord_reputation_type, lrep_custodian), #
#            
#
#            (troop_set_slot, "trp_npc47", slot_troop_morality_type, tmt_humanitarian), #
#            (troop_set_slot, "trp_npc47", slot_troop_morality_value, 4),
#            (troop_set_slot, "trp_npc47", slot_troop_2ary_morality_type, tmt_aristocratic),
#            (troop_set_slot, "trp_npc47", slot_troop_2ary_morality_value, -1),
#            (troop_set_slot, "trp_npc47", slot_troop_personalityclash_object, "trp_npc63"), #
#            (troop_set_slot, "trp_npc47", slot_troop_personalityclash2_object, "trp_npc64"), #
#            (troop_set_slot, "trp_npc47", slot_troop_personalitymatch_object, "trp_npc53"), #
#            (troop_set_slot, "trp_npc47", slot_troop_home, "p_castle_29"), #
#            (troop_set_slot, "trp_npc47", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc47", slot_troop_kingsupport_argument, argument_lords),
#            (troop_set_slot, "trp_npc47", slot_troop_kingsupport_opponent, "trp_npc66"), #
#            (troop_set_slot, "trp_npc47", slot_troop_town_with_contacts, "p_town_8"), #
#            (troop_set_slot, "trp_npc47", slot_troop_original_faction, fac_kingdom_2), #
#            (troop_set_slot, "trp_npc47", slot_lord_reputation_type, lrep_benefactor), #
#            
#            
#            (troop_set_slot, "trp_npc48", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc48", slot_troop_morality_value, 4),
#            (troop_set_slot, "trp_npc48", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc48", slot_troop_2ary_morality_value, -1),
#            (troop_set_slot, "trp_npc48", slot_troop_personalityclash_object, "trp_npc54"), #
#            (troop_set_slot, "trp_npc48", slot_troop_personalityclash2_object, "trp_npc51"), #
#            (troop_set_slot, "trp_npc48", slot_troop_personalitymatch_object, "trp_npc64"), #
#            (troop_set_slot, "trp_npc48", slot_troop_home, "p_village_84"), #
#            (troop_set_slot, "trp_npc48", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc48", slot_troop_kingsupport_argument, argument_claim),
#            (troop_set_slot, "trp_npc48", slot_troop_kingsupport_opponent, "trp_npc59"), #
#            (troop_set_slot, "trp_npc48", slot_troop_town_with_contacts, "p_town_5"), #
#            (troop_set_slot, "trp_npc48", slot_troop_original_faction, fac_kingdom_5), #ichamur
#            (troop_set_slot, "trp_npc48", slot_lord_reputation_type, lrep_cunning), #
#            
#            
#            (troop_set_slot, "trp_npc49", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc49", slot_troop_morality_value, 3),  #
#            (troop_set_slot, "trp_npc49", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc49", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc49", slot_troop_personalityclash_object, "trp_npc46"),  #
#            (troop_set_slot, "trp_npc49", slot_troop_personalityclash2_object, "trp_npc55"),  #
#            (troop_set_slot, "trp_npc49", slot_troop_personalitymatch_object, "trp_npc65"),  #
#            (troop_set_slot, "trp_npc49", slot_troop_home, "p_town_10"), #
#            (troop_set_slot, "trp_npc49", slot_troop_payment_request, 400),
#            (troop_set_slot, "trp_npc49", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc49", slot_troop_kingsupport_opponent, "trp_npc47"), #
#            (troop_set_slot, "trp_npc49", slot_troop_town_with_contacts, "p_town_10"), #
#            (troop_set_slot, "trp_npc49", slot_troop_original_faction, "fac_kingdom_3"), #
#            (troop_set_slot, "trp_npc49", slot_lord_reputation_type, lrep_cunning), #
#            
#            
#            (troop_set_slot, "trp_npc50", slot_troop_morality_type, tmt_humanitarian), #
#            (troop_set_slot, "trp_npc50", slot_troop_morality_value, 2),  #
#            (troop_set_slot, "trp_npc50", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc50", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc50", slot_troop_personalityclash_object, "trp_npc55"), #
#            (troop_set_slot, "trp_npc50", slot_troop_personalityclash2_object, "trp_npc57"), #
#            (troop_set_slot, "trp_npc50", slot_troop_personalitymatch_object, "trp_npc61"),  #
#            (troop_set_slot, "trp_npc50", slot_troop_home, "p_town_12"), #
#            (troop_set_slot, "trp_npc50", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc50", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc50", slot_troop_kingsupport_opponent, "trp_npc48"), #
#            (troop_set_slot, "trp_npc50", slot_troop_town_with_contacts, "p_town_12"), #
#            (troop_set_slot, "trp_npc50", slot_troop_original_faction, "fac_kingdom_4"), #
#            (troop_set_slot, "trp_npc50", slot_lord_reputation_type, lrep_upstanding), #
#            
#            
#            (troop_set_slot, "trp_npc51", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc51", slot_troop_morality_value, 3),  #
#            (troop_set_slot, "trp_npc51", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc51", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc51", slot_troop_personalityclash_object, "trp_npc45"),  #
#            (troop_set_slot, "trp_npc51", slot_troop_personalityclash2_object, "trp_npc48"),  #
#            (troop_set_slot, "trp_npc51", slot_troop_personalitymatch_object, "trp_npc60"),  #
#            (troop_set_slot, "trp_npc51", slot_troop_home, "p_village_48"), #
#			 (troop_set_slot, "trp_npc51", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc51", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc51", slot_troop_kingsupport_opponent, "trp_npc54"), #
#            (troop_set_slot, "trp_npc51", slot_troop_town_with_contacts, "p_town_16"), #
#            (troop_set_slot, "trp_npc51", slot_troop_original_faction, fac_kingdom_1), #
#            (troop_set_slot, "trp_npc51", slot_lord_reputation_type, lrep_custodian), #
#            
#            
#            (troop_set_slot, "trp_npc52", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc52", slot_troop_morality_value, 3),  #
#            (troop_set_slot, "trp_npc52", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc52", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc52", slot_troop_personalityclash_object, "trp_npc56"), #
#            (troop_set_slot, "trp_npc52", slot_troop_personalityclash2_object, "trp_npc66"), #
#            (troop_set_slot, "trp_npc52", slot_troop_personalitymatch_object, "trp_npc57"),  #
#            (troop_set_slot, "trp_npc52", slot_troop_home, "p_village_105"), #
#            (troop_set_slot, "trp_npc52", slot_troop_payment_request, 500),
#            (troop_set_slot, "trp_npc52", slot_troop_kingsupport_argument, argument_lords),
#            (troop_set_slot, "trp_npc52", slot_troop_kingsupport_opponent, "trp_npc50"), #
#            (troop_set_slot, "trp_npc52", slot_troop_town_with_contacts, "p_town_20"), #
#            (troop_set_slot, "trp_npc52", slot_troop_original_faction, "fac_kingdom_6"), #
#            (troop_set_slot, "trp_npc52", slot_lord_reputation_type, lrep_martial), #
#            
#            
#            (troop_set_slot, "trp_npc53", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc53", slot_troop_morality_value, 2),  #
#            (troop_set_slot, "trp_npc53", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc53", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc53", slot_troop_personalityclash_object, "trp_npc61"), #
#            (troop_set_slot, "trp_npc53", slot_troop_personalityclash2_object, "trp_npc63"), #
#            (troop_set_slot, "trp_npc53", slot_troop_personalitymatch_object, "trp_npc47"),  #
#            (troop_set_slot, "trp_npc53", slot_troop_home, "p_castle_37"), #
#            (troop_set_slot, "trp_npc53", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc53", slot_troop_kingsupport_argument, argument_lords),
#            (troop_set_slot, "trp_npc53", slot_troop_kingsupport_opponent, "trp_npc62"), #
#            (troop_set_slot, "trp_npc53", slot_troop_town_with_contacts, "p_town_11"), #
#            (troop_set_slot, "trp_npc53", slot_troop_original_faction, "fac_kingdom_2"), #
#            (troop_set_slot, "trp_npc53", slot_lord_reputation_type, lrep_martial), #
#            
#            
#            (troop_set_slot, "trp_npc54", slot_troop_morality_type, tmt_humanitarian), #
#            (troop_set_slot, "trp_npc54", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc54", slot_troop_2ary_morality_type, tmt_egalitarian),
#            (troop_set_slot, "trp_npc54", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc54", slot_troop_personalityclash_object, "trp_npc48"), #
#            (troop_set_slot, "trp_npc54", slot_troop_personalityclash2_object, "trp_npc58"), #
#            (troop_set_slot, "trp_npc54", slot_troop_personalitymatch_object, "trp_npc55"),  #
#            (troop_set_slot, "trp_npc54", slot_troop_home, "p_castle_14"), #
#            (troop_set_slot, "trp_npc54", slot_troop_payment_request, 200),
#            (troop_set_slot, "trp_npc54", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc54", slot_troop_kingsupport_opponent, "trp_npc57"), #
#            (troop_set_slot, "trp_npc54", slot_troop_town_with_contacts, "p_town_15"), #
#            (troop_set_slot, "trp_npc54", slot_troop_original_faction, "fac_kingdom_5"), #
#            (troop_set_slot, "trp_npc54", slot_lord_reputation_type, lrep_benefactor), #
#            
#            
#            (troop_set_slot, "trp_npc55", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc55", slot_troop_morality_value, 3),
#            (troop_set_slot, "trp_npc55", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc55", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc55", slot_troop_personalityclash_object, "trp_npc50"),  #
#            (troop_set_slot, "trp_npc55", slot_troop_personalityclash2_object, "trp_npc49"),  #
#            (troop_set_slot, "trp_npc55", slot_troop_personalitymatch_object, "trp_npc54"),  #
#            (troop_set_slot, "trp_npc55", slot_troop_home, "p_castle_22"), #
#            (troop_set_slot, "trp_npc55", slot_troop_payment_request, 100),
#            (troop_set_slot, "trp_npc55", slot_troop_kingsupport_argument, argument_claim),
#            (troop_set_slot, "trp_npc55", slot_troop_kingsupport_opponent, "trp_npc58"), #
#            (troop_set_slot, "trp_npc55", slot_troop_town_with_contacts, "p_town_14"), #
#            (troop_set_slot, "trp_npc55", slot_troop_original_faction, fac_kingdom_3), #
#            (troop_set_slot, "trp_npc55", slot_lord_reputation_type, lrep_custodian), #
#            
#            
#            (troop_set_slot, "trp_npc56", slot_troop_morality_type, tmt_humanitarian), #
#            (troop_set_slot, "trp_npc56", slot_troop_morality_value, 3),
#            (troop_set_slot, "trp_npc56", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc56", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc56", slot_troop_personalityclash_object, "trp_npc52"), #
#            (troop_set_slot, "trp_npc56", slot_troop_personalityclash2_object, "trp_npc59"), #
#            (troop_set_slot, "trp_npc56", slot_troop_personalitymatch_object, "trp_npc63"),  #
#            (troop_set_slot, "trp_npc56", slot_troop_home, "p_castle_5"), #
#            (troop_set_slot, "trp_npc56", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc56", slot_troop_kingsupport_argument, argument_claim),
#            (troop_set_slot, "trp_npc56", slot_troop_kingsupport_opponent, "trp_npc60"), #
#            (troop_set_slot, "trp_npc56", slot_troop_town_with_contacts, "p_town_1"), #
#            (troop_set_slot, "trp_npc56", slot_troop_original_faction, fac_kingdom_4), #
#            (troop_set_slot, "trp_npc56", slot_lord_reputation_type, lrep_benefactor), #
#            
#
#            (troop_set_slot, "trp_npc57", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc57", slot_troop_morality_value, 3),
#            (troop_set_slot, "trp_npc57", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc57", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc57", slot_troop_personalityclash_object, "trp_npc62"), #
#            (troop_set_slot, "trp_npc57", slot_troop_personalityclash2_object, "trp_npc50"), #
#            (troop_set_slot, "trp_npc57", slot_troop_personalitymatch_object, "trp_npc52"), #
#            (troop_set_slot, "trp_npc57", slot_troop_home, "p_castle_26"), #
#            (troop_set_slot, "trp_npc57", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc57", slot_troop_kingsupport_argument, argument_claim),
#            (troop_set_slot, "trp_npc57", slot_troop_kingsupport_opponent, "trp_npc46"), #
#            (troop_set_slot, "trp_npc57", slot_troop_town_with_contacts, "p_town_6"), #
#            (troop_set_slot, "trp_npc57", slot_troop_original_faction, fac_kingdom_1), #
#            (troop_set_slot, "trp_npc57", slot_lord_reputation_type, lrep_roguish), #
#            
#            
#            (troop_set_slot, "trp_npc58", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc58", slot_troop_morality_value, 4),
#            (troop_set_slot, "trp_npc58", slot_troop_2ary_morality_type, tmt_egalitarian),
#            (troop_set_slot, "trp_npc58", slot_troop_2ary_morality_value, -1),
#            (troop_set_slot, "trp_npc58", slot_troop_personalityclash_object, "trp_npc66"), #
#            (troop_set_slot, "trp_npc58", slot_troop_personalityclash2_object, "trp_npc54"), #
#            (troop_set_slot, "trp_npc58", slot_troop_personalitymatch_object, "trp_npc59"), #
#            (troop_set_slot, "trp_npc58", slot_troop_home, "p_town_21"), #
#            (troop_set_slot, "trp_npc58", slot_troop_payment_request, 400),
#            (troop_set_slot, "trp_npc58", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc58", slot_troop_kingsupport_opponent, "trp_npc45"), #
#            (troop_set_slot, "trp_npc58", slot_troop_town_with_contacts, "p_town_21"), #
#            (troop_set_slot, "trp_npc58", slot_troop_original_faction, fac_kingdom_6), #
#            (troop_set_slot, "trp_npc58", slot_lord_reputation_type, lrep_selfrighteous), #
#            
#            
#            (troop_set_slot, "trp_npc59", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc59", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc59", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc59", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc59", slot_troop_personalityclash_object, "trp_npc65"), #
#            (troop_set_slot, "trp_npc59", slot_troop_personalityclash2_object, "trp_npc56"), #
#            (troop_set_slot, "trp_npc59", slot_troop_personalitymatch_object, "trp_npc58"), #
#            (troop_set_slot, "trp_npc59", slot_troop_home, "p_castle_8"), #
#            (troop_set_slot, "trp_npc59", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc59", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc59", slot_troop_kingsupport_opponent, "trp_npc55"), #
#            (troop_set_slot, "trp_npc59", slot_troop_town_with_contacts, "p_town_13"), #
#            (troop_set_slot, "trp_npc59", slot_troop_original_faction, fac_kingdom_2), #
#            (troop_set_slot, "trp_npc59", slot_lord_reputation_type, lrep_custodian), #
#            
#            
#            (troop_set_slot, "trp_npc60", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc60", slot_troop_morality_value, 4),
#            (troop_set_slot, "trp_npc60", slot_troop_2ary_morality_type, tmt_humanitarian),
#            (troop_set_slot, "trp_npc60", slot_troop_2ary_morality_value, -1),
#            (troop_set_slot, "trp_npc60", slot_troop_personalityclash_object, "trp_npc64"), #
#            (troop_set_slot, "trp_npc60", slot_troop_personalityclash2_object, "trp_npc61"), #
#            (troop_set_slot, "trp_npc60", slot_troop_personalitymatch_object, "trp_npc51"),  #
#            (troop_set_slot, "trp_npc60", slot_troop_home, "p_village_70"), #
#            (troop_set_slot, "trp_npc60", slot_troop_payment_request, 200),
#            (troop_set_slot, "trp_npc60", slot_troop_kingsupport_argument, argument_lords),
#            (troop_set_slot, "trp_npc60", slot_troop_kingsupport_opponent, "trp_npc46"), #
#            (troop_set_slot, "trp_npc60", slot_troop_town_with_contacts, "p_town_3"), #
#            (troop_set_slot, "trp_npc60", slot_troop_original_faction, fac_kingdom_5), #
#            (troop_set_slot, "trp_npc60", slot_lord_reputation_type, lrep_roguish), #
#
#
#            (troop_set_slot, "trp_npc61", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc61", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc61", slot_troop_2ary_morality_type, tmt_aristocratic),
#            (troop_set_slot, "trp_npc61", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc61", slot_troop_personalityclash_object, "trp_npc60"), #
#            (troop_set_slot, "trp_npc61", slot_troop_personalityclash2_object, "trp_npc53"), #
#            (troop_set_slot, "trp_npc61", slot_troop_personalitymatch_object, "trp_npc50"), #
#            (troop_set_slot, "trp_npc61", slot_troop_home, "p_town_18"), #
#            (troop_set_slot, "trp_npc61", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc61", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc61", slot_troop_kingsupport_opponent, "trp_npc49"), #
#            (troop_set_slot, "trp_npc61", slot_troop_town_with_contacts, "p_town_18"), #
#            (troop_set_slot, "trp_npc61", slot_troop_original_faction, fac_kingdom_3), #
#            (troop_set_slot, "trp_npc61", slot_lord_reputation_type, lrep_goodnatured), #
#            
#
#            (troop_set_slot, "trp_npc62", slot_troop_morality_type, tmt_humanitarian),  #
#            (troop_set_slot, "trp_npc62", slot_troop_morality_value, 4),
#            (troop_set_slot, "trp_npc62", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc62", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc62", slot_troop_personalityclash_object, "trp_npc46"), #
#            (troop_set_slot, "trp_npc62", slot_troop_personalityclash2_object, "trp_npc57"), #
#            (troop_set_slot, "trp_npc62", slot_troop_personalitymatch_object, "trp_npc66"), #
#            (troop_set_slot, "trp_npc62", slot_troop_home, "p_town_2"), #
#            (troop_set_slot, "trp_npc62", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc62", slot_troop_kingsupport_argument, argument_claim),
#            (troop_set_slot, "trp_npc62", slot_troop_kingsupport_opponent, "trp_npc64"), #
#            (troop_set_slot, "trp_npc62", slot_troop_town_with_contacts, "p_town_2"), #
#            (troop_set_slot, "trp_npc62", slot_troop_original_faction, "fac_kingdom_4"), #
#            (troop_set_slot, "trp_npc62", slot_lord_reputation_type, lrep_benefactor), #
#            
#
#            (troop_set_slot, "trp_npc63", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc63", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc63", slot_troop_2ary_morality_type, tmt_pious),
#            (troop_set_slot, "trp_npc63", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc63", slot_troop_personalityclash_object, "trp_npc47"), #
#            (troop_set_slot, "trp_npc63", slot_troop_personalityclash2_object, "trp_npc53"), #
#            (troop_set_slot, "trp_npc63", slot_troop_personalitymatch_object, "trp_npc56"), #
#            (troop_set_slot, "trp_npc63", slot_troop_home, "p_village_82"), #
#            (troop_set_slot, "trp_npc63", slot_troop_payment_request, 200),
#            (troop_set_slot, "trp_npc63", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc63", slot_troop_kingsupport_opponent, "trp_npc65"), #
#            (troop_set_slot, "trp_npc63", slot_troop_town_with_contacts, "p_town_7"), #
#            (troop_set_slot, "trp_npc63", slot_troop_original_faction, "fac_kingdom_1"), #
#            (troop_set_slot, "trp_npc63", slot_lord_reputation_type, lrep_custodian), #
#            
#
#            (troop_set_slot, "trp_npc64", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc64", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc64", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc64", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc64", slot_troop_personalityclash_object, "trp_npc47"), #
#            (troop_set_slot, "trp_npc64", slot_troop_personalityclash2_object, "trp_npc60"), #
#            (troop_set_slot, "trp_npc64", slot_troop_personalitymatch_object, "trp_npc48"), #
#            (troop_set_slot, "trp_npc64", slot_troop_home, "p_village_109"), #
#            (troop_set_slot, "trp_npc64", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc64", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc64", slot_troop_kingsupport_opponent, "trp_npc63"), #
#            (troop_set_slot, "trp_npc64", slot_troop_town_with_contacts, "p_town_19"), #
#            (troop_set_slot, "trp_npc64", slot_troop_original_faction, "fac_kingdom_6"), #
#            (troop_set_slot, "trp_npc64", slot_lord_reputation_type, lrep_roguish), #
#            
#
#            (troop_set_slot, "trp_npc65", slot_troop_morality_type, tmt_aristocratic),  #
#            (troop_set_slot, "trp_npc65", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc65", slot_troop_2ary_morality_type, tmt_humanitarian),
#            (troop_set_slot, "trp_npc65", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc65", slot_troop_personalityclash_object, "trp_npc45"), #
#            (troop_set_slot, "trp_npc65", slot_troop_personalityclash2_object, "trp_npc59"), #
#            (troop_set_slot, "trp_npc65", slot_troop_personalitymatch_object, "trp_npc49"), #
#            (troop_set_slot, "trp_npc65", slot_troop_home, "p_castle_39"), #
#            (troop_set_slot, "trp_npc65", slot_troop_payment_request, 400),
#            (troop_set_slot, "trp_npc65", slot_troop_kingsupport_argument, argument_lords),
#            (troop_set_slot, "trp_npc65", slot_troop_kingsupport_opponent, "trp_npc61"), #
#            (troop_set_slot, "trp_npc65", slot_troop_town_with_contacts, "p_town_9"), #
#            (troop_set_slot, "trp_npc65", slot_troop_original_faction, "fac_kingdom_2"), #
#            (troop_set_slot, "trp_npc65", slot_lord_reputation_type, lrep_martial), #
#
#
#            (troop_set_slot, "trp_npc66", slot_troop_morality_type, tmt_humanitarian),  #
#            (troop_set_slot, "trp_npc66", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc66", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc66", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc66", slot_troop_personalityclash_object, "trp_npc52"), #
#            (troop_set_slot, "trp_npc66", slot_troop_personalityclash2_object, "trp_npc58"), #
#            (troop_set_slot, "trp_npc66", slot_troop_personalitymatch_object, "trp_npc62"), #
#            (troop_set_slot, "trp_npc66", slot_troop_home, "p_village_79"), #
#            (troop_set_slot, "trp_npc66", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc66", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc66", slot_troop_kingsupport_opponent, "trp_npc51"), #
#            (troop_set_slot, "trp_npc66", slot_troop_town_with_contacts, "p_town_5"), #
#            (troop_set_slot, "trp_npc66", slot_troop_original_faction, "fac_kingdom_5"), #
#            (troop_set_slot, "trp_npc66", slot_lord_reputation_type, lrep_custodian), #
#
##Extra Companions set 3
#            (troop_set_slot, "trp_npc67", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc67", slot_troop_morality_value, 4),  #
#            (troop_set_slot, "trp_npc67", slot_troop_2ary_morality_type, tmt_aristocratic),  #
#            (troop_set_slot, "trp_npc67", slot_troop_2ary_morality_value, -1),
#            (troop_set_slot, "trp_npc67", slot_troop_personalityclash_object, "trp_npc73"),  #
#            (troop_set_slot, "trp_npc67", slot_troop_personalityclash2_object, "trp_npc87"),  #
#            (troop_set_slot, "trp_npc67", slot_troop_personalitymatch_object, "trp_npc68"),  #
#            (troop_set_slot, "trp_npc67", slot_troop_home, "p_village_92"), #
#            (troop_set_slot, "trp_npc67", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc67", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc67", slot_troop_kingsupport_opponent, "trp_npc75"), #
#            (troop_set_slot, "trp_npc67", slot_troop_town_with_contacts, "p_town_19"), #
#            (troop_set_slot, "trp_npc67", slot_troop_original_faction, fac_kingdom_6), #
#            (troop_set_slot, "trp_npc67", slot_lord_reputation_type, lrep_roguish), #
#            
#            
#            (troop_set_slot, "trp_npc68", slot_troop_morality_type, tmt_humanitarian), #
#            (troop_set_slot, "trp_npc68", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc68", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc68", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc68", slot_troop_personalityclash_object, "trp_npc71"), #
#            (troop_set_slot, "trp_npc68", slot_troop_personalityclash2_object, "trp_npc84"), #
#            (troop_set_slot, "trp_npc68", slot_troop_personalitymatch_object, "trp_npc67"),  #
#            (troop_set_slot, "trp_npc68", slot_troop_home, "p_town_5"), #
#            (troop_set_slot, "trp_npc68", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc68", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc68", slot_troop_kingsupport_opponent, "trp_npc74"), #
#            (troop_set_slot, "trp_npc68", slot_troop_town_with_contacts, "p_town_5"), #
#            (troop_set_slot, "trp_npc68", slot_troop_original_faction, fac_kingdom_5), #
#            (troop_set_slot, "trp_npc68", slot_lord_reputation_type, lrep_custodian), #
#            
#
#            (troop_set_slot, "trp_npc69", slot_troop_morality_type, tmt_humanitarian), #
#            (troop_set_slot, "trp_npc69", slot_troop_morality_value, 4),
#            (troop_set_slot, "trp_npc69", slot_troop_2ary_morality_type, tmt_aristocratic),
#            (troop_set_slot, "trp_npc69", slot_troop_2ary_morality_value, -1),
#            (troop_set_slot, "trp_npc69", slot_troop_personalityclash_object, "trp_npc85"), #
#            (troop_set_slot, "trp_npc69", slot_troop_personalityclash2_object, "trp_npc86"), #
#            (troop_set_slot, "trp_npc69", slot_troop_personalitymatch_object, "trp_npc75"), #
#            (troop_set_slot, "trp_npc69", slot_troop_home, "p_castle_30"), #
#            (troop_set_slot, "trp_npc69", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc69", slot_troop_kingsupport_argument, argument_lords),
#            (troop_set_slot, "trp_npc69", slot_troop_kingsupport_opponent, "trp_npc88"), #
#            (troop_set_slot, "trp_npc69", slot_troop_town_with_contacts, "p_town_2"), #
#            (troop_set_slot, "trp_npc69", slot_troop_original_faction, fac_kingdom_4), #
#            (troop_set_slot, "trp_npc69", slot_lord_reputation_type, lrep_benefactor), #
#            
#            
#            (troop_set_slot, "trp_npc70", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc70", slot_troop_morality_value, 4),
#            (troop_set_slot, "trp_npc70", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc70", slot_troop_2ary_morality_value, -1),
#            (troop_set_slot, "trp_npc70", slot_troop_personalityclash_object, "trp_npc76"), #
#            (troop_set_slot, "trp_npc70", slot_troop_personalityclash2_object, "trp_npc73"), #
#            (troop_set_slot, "trp_npc70", slot_troop_personalitymatch_object, "trp_npc86"), #
#            (troop_set_slot, "trp_npc70", slot_troop_home, "p_village_43"), #
#            (troop_set_slot, "trp_npc70", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc70", slot_troop_kingsupport_argument, argument_claim),
#            (troop_set_slot, "trp_npc70", slot_troop_kingsupport_opponent, "trp_npc81"), #
#            (troop_set_slot, "trp_npc70", slot_troop_town_with_contacts, "p_town_14"), #
#            (troop_set_slot, "trp_npc70", slot_troop_original_faction, fac_kingdom_3), #
#            (troop_set_slot, "trp_npc70", slot_lord_reputation_type, lrep_cunning), #
#            
#            
#            (troop_set_slot, "trp_npc71", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc71", slot_troop_morality_value, 3),  #
#            (troop_set_slot, "trp_npc71", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc71", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc71", slot_troop_personalityclash_object, "trp_npc68"),  #
#            (troop_set_slot, "trp_npc71", slot_troop_personalityclash2_object, "trp_npc77"),  #
#            (troop_set_slot, "trp_npc71", slot_troop_personalitymatch_object, "trp_npc87"),  #
#            (troop_set_slot, "trp_npc71", slot_troop_home, "p_town_11"), #
#            (troop_set_slot, "trp_npc71", slot_troop_payment_request, 400),
#            (troop_set_slot, "trp_npc71", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc71", slot_troop_kingsupport_opponent, "trp_npc69"), #
#            (troop_set_slot, "trp_npc71", slot_troop_town_with_contacts, "p_town_11"), #
#            (troop_set_slot, "trp_npc71", slot_troop_original_faction, "fac_kingdom_2"), #
#            (troop_set_slot, "trp_npc71", slot_lord_reputation_type, lrep_cunning), #
#            
#            
#            (troop_set_slot, "trp_npc72", slot_troop_morality_type, tmt_humanitarian), #
#            (troop_set_slot, "trp_npc72", slot_troop_morality_value, 2),  #
#            (troop_set_slot, "trp_npc72", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc72", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc72", slot_troop_personalityclash_object, "trp_npc77"), #
#            (troop_set_slot, "trp_npc72", slot_troop_personalityclash2_object, "trp_npc79"), #
#            (troop_set_slot, "trp_npc72", slot_troop_personalitymatch_object, "trp_npc83"),  #
#            (troop_set_slot, "trp_npc72", slot_troop_home, "p_town_16"), #
#            (troop_set_slot, "trp_npc72", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc72", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc72", slot_troop_kingsupport_opponent, "trp_npc80"), #
#            (troop_set_slot, "trp_npc72", slot_troop_town_with_contacts, "p_town_16"), #
#            (troop_set_slot, "trp_npc72", slot_troop_original_faction, "fac_kingdom_1"), #
#            (troop_set_slot, "trp_npc72", slot_lord_reputation_type, lrep_upstanding), #
#            
#            
#            (troop_set_slot, "trp_npc73", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc73", slot_troop_morality_value, 3),  #
#            (troop_set_slot, "trp_npc73", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc73", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc73", slot_troop_personalityclash_object, "trp_npc67"),  #
#            (troop_set_slot, "trp_npc73", slot_troop_personalityclash2_object, "trp_npc70"),  #
#            (troop_set_slot, "trp_npc73", slot_troop_personalitymatch_object, "trp_npc82"),  #
#            (troop_set_slot, "trp_npc73", slot_troop_home, "p_village_94"), #
#		     (troop_set_slot, "trp_npc73", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc73", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc73", slot_troop_kingsupport_opponent, "trp_npc76"), #
#            (troop_set_slot, "trp_npc73", slot_troop_town_with_contacts, "p_town_20"), #
#            (troop_set_slot, "trp_npc73", slot_troop_original_faction, fac_kingdom_6), #
#            (troop_set_slot, "trp_npc73", slot_lord_reputation_type, lrep_custodian), #
#            
#            
#            (troop_set_slot, "trp_npc74", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc74", slot_troop_morality_value, 3),  #
#            (troop_set_slot, "trp_npc74", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc74", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc74", slot_troop_personalityclash_object, "trp_npc78"), #
#            (troop_set_slot, "trp_npc74", slot_troop_personalityclash2_object, "trp_npc88"), #
#            (troop_set_slot, "trp_npc74", slot_troop_personalitymatch_object, "trp_npc79"),  #
#            (troop_set_slot, "trp_npc74", slot_troop_home, "p_village_27"), #
#            (troop_set_slot, "trp_npc74", slot_troop_payment_request, 500),
#            (troop_set_slot, "trp_npc74", slot_troop_kingsupport_argument, argument_lords),
#            (troop_set_slot, "trp_npc74", slot_troop_kingsupport_opponent, "trp_npc72"), #
#            (troop_set_slot, "trp_npc74", slot_troop_town_with_contacts, "p_town_3"), #
#            (troop_set_slot, "trp_npc74", slot_troop_original_faction, "fac_kingdom_5"), #
#            (troop_set_slot, "trp_npc74", slot_lord_reputation_type, lrep_martial), #
#            
#            
#            (troop_set_slot, "trp_npc75", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc75", slot_troop_morality_value, 2),  #
#            (troop_set_slot, "trp_npc75", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc75", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc75", slot_troop_personalityclash_object, "trp_npc83"), #
#            (troop_set_slot, "trp_npc75", slot_troop_personalityclash2_object, "trp_npc85"), #
#            (troop_set_slot, "trp_npc75", slot_troop_personalitymatch_object, "trp_npc69"),  #
#            (troop_set_slot, "trp_npc75", slot_troop_home, "p_castle_36"), #
#            (troop_set_slot, "trp_npc75", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc75", slot_troop_kingsupport_argument, argument_lords),
#            (troop_set_slot, "trp_npc75", slot_troop_kingsupport_opponent, "trp_npc84"), #
#            (troop_set_slot, "trp_npc75", slot_troop_town_with_contacts, "p_town_1"), #
#            (troop_set_slot, "trp_npc75", slot_troop_original_faction, "fac_kingdom_4"), #
#            (troop_set_slot, "trp_npc75", slot_lord_reputation_type, lrep_martial), #
#            
#            
#            (troop_set_slot, "trp_npc76", slot_troop_morality_type, tmt_humanitarian), #
#            (troop_set_slot, "trp_npc76", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc76", slot_troop_2ary_morality_type, tmt_egalitarian),
#            (troop_set_slot, "trp_npc76", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc76", slot_troop_personalityclash_object, "trp_npc70"), #
#            (troop_set_slot, "trp_npc76", slot_troop_personalityclash2_object, "trp_npc80"), #
#            (troop_set_slot, "trp_npc76", slot_troop_personalitymatch_object, "trp_npc77"),  #
#            (troop_set_slot, "trp_npc76", slot_troop_home, "p_castle_17"), #
#            (troop_set_slot, "trp_npc76", slot_troop_payment_request, 200),
#            (troop_set_slot, "trp_npc76", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc76", slot_troop_kingsupport_opponent, "trp_npc79"), #
#            (troop_set_slot, "trp_npc76", slot_troop_town_with_contacts, "p_town_17"), #
#            (troop_set_slot, "trp_npc76", slot_troop_original_faction, "fac_kingdom_3"), #
#            (troop_set_slot, "trp_npc76", slot_lord_reputation_type, lrep_benefactor), #
#            
#            
#            (troop_set_slot, "trp_npc77", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc77", slot_troop_morality_value, 3),
#            (troop_set_slot, "trp_npc77", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc77", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc77", slot_troop_personalityclash_object, "trp_npc72"),  #
#            (troop_set_slot, "trp_npc77", slot_troop_personalityclash2_object, "trp_npc71"),  #
#            (troop_set_slot, "trp_npc77", slot_troop_personalitymatch_object, "trp_npc76"),  #
#            (troop_set_slot, "trp_npc77", slot_troop_home, "p_castle_3"), #
#            (troop_set_slot, "trp_npc77", slot_troop_payment_request, 100),
#            (troop_set_slot, "trp_npc77", slot_troop_kingsupport_argument, argument_claim),
#            (troop_set_slot, "trp_npc77", slot_troop_kingsupport_opponent, "trp_npc80"), #
#            (troop_set_slot, "trp_npc77", slot_troop_town_with_contacts, "p_town_13"), #
#            (troop_set_slot, "trp_npc77", slot_troop_original_faction, fac_kingdom_2), #
#            (troop_set_slot, "trp_npc77", slot_lord_reputation_type, lrep_custodian), #
#            
#            
#            (troop_set_slot, "trp_npc78", slot_troop_morality_type, tmt_humanitarian), #
#            (troop_set_slot, "trp_npc78", slot_troop_morality_value, 3),
#            (troop_set_slot, "trp_npc78", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc78", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc78", slot_troop_personalityclash_object, "trp_npc74"), #
#            (troop_set_slot, "trp_npc78", slot_troop_personalityclash2_object, "trp_npc81"), #
#            (troop_set_slot, "trp_npc78", slot_troop_personalitymatch_object, "trp_npc85"),  #
#            (troop_set_slot, "trp_npc78", slot_troop_home, "p_castle_35"), #
#            (troop_set_slot, "trp_npc78", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc78", slot_troop_kingsupport_argument, argument_claim),
#            (troop_set_slot, "trp_npc78", slot_troop_kingsupport_opponent, "trp_npc82"), #
#            (troop_set_slot, "trp_npc78", slot_troop_town_with_contacts, "p_town_7"), #
#            (troop_set_slot, "trp_npc78", slot_troop_original_faction, fac_kingdom_1), #
#            (troop_set_slot, "trp_npc78", slot_lord_reputation_type, lrep_benefactor), #
#            
#
#            (troop_set_slot, "trp_npc79", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc79", slot_troop_morality_value, 3),
#            (troop_set_slot, "trp_npc79", slot_troop_2ary_morality_type, -1),
#            (troop_set_slot, "trp_npc79", slot_troop_2ary_morality_value, 0),
#            (troop_set_slot, "trp_npc79", slot_troop_personalityclash_object, "trp_npc84"), #
#            (troop_set_slot, "trp_npc79", slot_troop_personalityclash2_object, "trp_npc72"), #
#            (troop_set_slot, "trp_npc79", slot_troop_personalitymatch_object, "trp_npc74"), #
#            (troop_set_slot, "trp_npc79", slot_troop_home, "p_town_22"), #
#            (troop_set_slot, "trp_npc79", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc79", slot_troop_kingsupport_argument, argument_claim),
#            (troop_set_slot, "trp_npc79", slot_troop_kingsupport_opponent, "trp_npc68"), #
#            (troop_set_slot, "trp_npc79", slot_troop_town_with_contacts, "p_town_22"), #
#            (troop_set_slot, "trp_npc79", slot_troop_original_faction, fac_kingdom_6), #
#            (troop_set_slot, "trp_npc79", slot_lord_reputation_type, lrep_roguish), #
#            
#            
#            (troop_set_slot, "trp_npc80", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc80", slot_troop_morality_value, 4),
#            (troop_set_slot, "trp_npc80", slot_troop_2ary_morality_type, tmt_egalitarian),
#            (troop_set_slot, "trp_npc80", slot_troop_2ary_morality_value, -1),
#            (troop_set_slot, "trp_npc80", slot_troop_personalityclash_object, "trp_npc88"), #
#            (troop_set_slot, "trp_npc80", slot_troop_personalityclash2_object, "trp_npc76"), #
#            (troop_set_slot, "trp_npc80", slot_troop_personalitymatch_object, "trp_npc81"), #
#            (troop_set_slot, "trp_npc80", slot_troop_home, "p_village_23"), #
#            (troop_set_slot, "trp_npc80", slot_troop_payment_request, 400),
#            (troop_set_slot, "trp_npc80", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc80", slot_troop_kingsupport_opponent, "trp_npc67"), #
#            (troop_set_slot, "trp_npc80", slot_troop_town_with_contacts, "p_town_15"), #
#            (troop_set_slot, "trp_npc80", slot_troop_original_faction, fac_kingdom_5), #
#            (troop_set_slot, "trp_npc80", slot_lord_reputation_type, lrep_selfrighteous), #
#            
#            
#            (troop_set_slot, "trp_npc81", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc81", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc81", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc81", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc81", slot_troop_personalityclash_object, "trp_npc87"), #
#            (troop_set_slot, "trp_npc81", slot_troop_personalityclash2_object, "trp_npc78"), #
#            (troop_set_slot, "trp_npc81", slot_troop_personalitymatch_object, "trp_npc80"), #
#            (troop_set_slot, "trp_npc81", slot_troop_home, "p_town_12"), #
#            (troop_set_slot, "trp_npc81", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc81", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc81", slot_troop_kingsupport_opponent, "trp_npc77"), #
#            (troop_set_slot, "trp_npc81", slot_troop_town_with_contacts, "p_town_12"), #
#            (troop_set_slot, "trp_npc81", slot_troop_original_faction, fac_kingdom_4), #
#            (troop_set_slot, "trp_npc81", slot_lord_reputation_type, lrep_custodian), #
#            
#            
#            (troop_set_slot, "trp_npc82", slot_troop_morality_type, tmt_aristocratic), #
#            (troop_set_slot, "trp_npc82", slot_troop_morality_value, 4),
#            (troop_set_slot, "trp_npc82", slot_troop_2ary_morality_type, tmt_humanitarian),
#            (troop_set_slot, "trp_npc82", slot_troop_2ary_morality_value, -1),
#            (troop_set_slot, "trp_npc82", slot_troop_personalityclash_object, "trp_npc86"), #
#            (troop_set_slot, "trp_npc82", slot_troop_personalityclash2_object, "trp_npc83"), #
#            (troop_set_slot, "trp_npc82", slot_troop_personalitymatch_object, "trp_npc73"),  #
#            (troop_set_slot, "trp_npc82", slot_troop_home, "p_village_76"), #
#            (troop_set_slot, "trp_npc82", slot_troop_payment_request, 200),
#            (troop_set_slot, "trp_npc82", slot_troop_kingsupport_argument, argument_lords),
#            (troop_set_slot, "trp_npc82", slot_troop_kingsupport_opponent, "trp_npc68"), #
#            (troop_set_slot, "trp_npc82", slot_troop_town_with_contacts, "p_town_10"), #
#            (troop_set_slot, "trp_npc82", slot_troop_original_faction, fac_kingdom_3), #
#            (troop_set_slot, "trp_npc82", slot_lord_reputation_type, lrep_roguish), #
#
#
#            (troop_set_slot, "trp_npc83", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc83", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc83", slot_troop_2ary_morality_type, tmt_aristocratic),
#            (troop_set_slot, "trp_npc83", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc83", slot_troop_personalityclash_object, "trp_npc82"), #
#            (troop_set_slot, "trp_npc83", slot_troop_personalityclash2_object, "trp_npc75"), #
#            (troop_set_slot, "trp_npc83", slot_troop_personalitymatch_object, "trp_npc72"), #
#            (troop_set_slot, "trp_npc83", slot_troop_home, "p_village_18"), #
#            (troop_set_slot, "trp_npc83", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc83", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc83", slot_troop_kingsupport_opponent, "trp_npc71"), #
#            (troop_set_slot, "trp_npc83", slot_troop_town_with_contacts, "p_town_9"), #
#            (troop_set_slot, "trp_npc83", slot_troop_original_faction, fac_kingdom_2), #
#            (troop_set_slot, "trp_npc83", slot_lord_reputation_type, lrep_goodnatured), #
#            
#
#            (troop_set_slot, "trp_npc84", slot_troop_morality_type, tmt_humanitarian),  #
#            (troop_set_slot, "trp_npc84", slot_troop_morality_value, 4),
#            (troop_set_slot, "trp_npc84", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc84", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc84", slot_troop_personalityclash_object, "trp_npc68"), #
#            (troop_set_slot, "trp_npc84", slot_troop_personalityclash2_object, "trp_npc79"), #
#            (troop_set_slot, "trp_npc84", slot_troop_personalitymatch_object, "trp_npc88"), #
#            (troop_set_slot, "trp_npc84", slot_troop_home, "p_village_72"), #
#            (troop_set_slot, "trp_npc84", slot_troop_payment_request, 0),
#            (troop_set_slot, "trp_npc84", slot_troop_kingsupport_argument, argument_claim),
#            (troop_set_slot, "trp_npc84", slot_troop_kingsupport_opponent, "trp_npc86"), #
#            (troop_set_slot, "trp_npc84", slot_troop_town_with_contacts, "p_town_6"), #
#            (troop_set_slot, "trp_npc84", slot_troop_original_faction, "fac_kingdom_1"), #
#            (troop_set_slot, "trp_npc84", slot_lord_reputation_type, lrep_benefactor), #
#            
#
#            (troop_set_slot, "trp_npc85", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc85", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc85", slot_troop_2ary_morality_type, tmt_pious),
#            (troop_set_slot, "trp_npc85", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc85", slot_troop_personalityclash_object, "trp_npc69"), #
#            (troop_set_slot, "trp_npc85", slot_troop_personalityclash2_object, "trp_npc75"), #
#            (troop_set_slot, "trp_npc85", slot_troop_personalitymatch_object, "trp_npc78"), #
#            (troop_set_slot, "trp_npc85", slot_troop_home, "p_village_103"), #
#            (troop_set_slot, "trp_npc85", slot_troop_payment_request, 200),
#            (troop_set_slot, "trp_npc85", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc85", slot_troop_kingsupport_opponent, "trp_npc87"), #
#            (troop_set_slot, "trp_npc85", slot_troop_town_with_contacts, "p_town_21"), #
#            (troop_set_slot, "trp_npc85", slot_troop_original_faction, "fac_kingdom_6"), #
#            (troop_set_slot, "trp_npc85", slot_lord_reputation_type, lrep_custodian), #
#            
#
#            (troop_set_slot, "trp_npc86", slot_troop_morality_type, tmt_egalitarian),  #
#            (troop_set_slot, "trp_npc86", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc86", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc86", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc86", slot_troop_personalityclash_object, "trp_npc69"), #
#            (troop_set_slot, "trp_npc86", slot_troop_personalityclash2_object, "trp_npc82"), #
#            (troop_set_slot, "trp_npc86", slot_troop_personalitymatch_object, "trp_npc70"), #
#            (troop_set_slot, "trp_npc86", slot_troop_home, "p_village_40"), #
#            (troop_set_slot, "trp_npc86", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc86", slot_troop_kingsupport_argument, argument_ruler),
#            (troop_set_slot, "trp_npc86", slot_troop_kingsupport_opponent, "trp_npc85"), #
#            (troop_set_slot, "trp_npc86", slot_troop_town_with_contacts, "p_town_3"), #
#            (troop_set_slot, "trp_npc86", slot_troop_original_faction, "fac_kingdom_5"), #
#            (troop_set_slot, "trp_npc86", slot_lord_reputation_type, lrep_roguish), #
#            
#
#            (troop_set_slot, "trp_npc87", slot_troop_morality_type, tmt_aristocratic),  #
#            (troop_set_slot, "trp_npc87", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc87", slot_troop_2ary_morality_type, tmt_humanitarian),
#            (troop_set_slot, "trp_npc87", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc87", slot_troop_personalityclash_object, "trp_npc67"), #
#            (troop_set_slot, "trp_npc87", slot_troop_personalityclash2_object, "trp_npc81"), #
#            (troop_set_slot, "trp_npc87", slot_troop_personalitymatch_object, "trp_npc71"), #
#            (troop_set_slot, "trp_npc87", slot_troop_home, "p_castle_36"), #
#            (troop_set_slot, "trp_npc87", slot_troop_payment_request, 400),
#            (troop_set_slot, "trp_npc87", slot_troop_kingsupport_argument, argument_lords),
#            (troop_set_slot, "trp_npc87", slot_troop_kingsupport_opponent, "trp_npc83"), #
#            (troop_set_slot, "trp_npc87", slot_troop_town_with_contacts, "p_town_12"), #
#            (troop_set_slot, "trp_npc87", slot_troop_original_faction, "fac_kingdom_4"), #
#            (troop_set_slot, "trp_npc87", slot_lord_reputation_type, lrep_martial), #
#
#
#            (troop_set_slot, "trp_npc88", slot_troop_morality_type, tmt_humanitarian),  #
#            (troop_set_slot, "trp_npc88", slot_troop_morality_value, 2),
#            (troop_set_slot, "trp_npc88", slot_troop_2ary_morality_type, tmt_honest),
#            (troop_set_slot, "trp_npc88", slot_troop_2ary_morality_value, 1),
#            (troop_set_slot, "trp_npc88", slot_troop_personalityclash_object, "trp_npc74"), #
#            (troop_set_slot, "trp_npc88", slot_troop_personalityclash2_object, "trp_npc80"), #
#            (troop_set_slot, "trp_npc88", slot_troop_personalitymatch_object, "trp_npc84"), #
#            (troop_set_slot, "trp_npc88", slot_troop_home, "p_village_11"), #
#            (troop_set_slot, "trp_npc88", slot_troop_payment_request, 300),
#            (troop_set_slot, "trp_npc88", slot_troop_kingsupport_argument, argument_victory),
#            (troop_set_slot, "trp_npc88", slot_troop_kingsupport_opponent, "trp_npc73"), #
#            (troop_set_slot, "trp_npc88", slot_troop_town_with_contacts, "p_town_2"), #
#            (troop_set_slot, "trp_npc88", slot_troop_original_faction, "fac_kingdom_3"), #
#            (troop_set_slot, "trp_npc88", slot_lord_reputation_type, lrep_custodian), #
##Floris end
##Extra companions end
            
            (store_sub, "$number_of_npc_slots", slot_troop_strings_end, slot_troop_intro),
            
            (try_for_range, ":npc", companions_begin, companions_end),
              
              
              (try_for_range, ":slot_addition", 0, "$number_of_npc_slots"),
                (store_add, ":slot", ":slot_addition", slot_troop_intro),
                
                (store_mul, ":string_addition", ":slot_addition", 22), ##Floris: I've changed the number from 16 to 22, since there are now 22 active npc's
                (store_add, ":string", "str_npc1_intro", ":string_addition"),
                (val_add, ":string", ":npc"),
                (val_sub, ":string", companions_begin),
                
                (troop_set_slot, ":npc", ":slot", ":string"),
              (try_end),
            (try_end),
            
            
            #Post 0907 changes begin
            (call_script, "script_add_log_entry", logent_game_start, "trp_player", -1, -1, -1),
            #Post 0907 changes end
            
            #Rebellion changes begin
            (troop_set_slot, "trp_kingdom_1_pretender",  slot_troop_original_faction, "fac_kingdom_1"),
            (troop_set_slot, "trp_kingdom_2_pretender",  slot_troop_original_faction, "fac_kingdom_2"),
            (troop_set_slot, "trp_kingdom_3_pretender",  slot_troop_original_faction, "fac_kingdom_3"),
            (troop_set_slot, "trp_kingdom_4_pretender",  slot_troop_original_faction, "fac_kingdom_4"),
            (troop_set_slot, "trp_kingdom_5_pretender",  slot_troop_original_faction, "fac_kingdom_5"),
            (troop_set_slot, "trp_kingdom_6_pretender",  slot_troop_original_faction, "fac_kingdom_6"),
            
            #        (troop_set_slot, "trp_kingdom_1_pretender", slot_troop_support_base,     "p_town_4"), #suno
            #        (troop_set_slot, "trp_kingdom_2_pretender", slot_troop_support_base,     "p_town_11"), #curaw
            #        (troop_set_slot, "trp_kingdom_3_pretender", slot_troop_support_base,     "p_town_18"), #town_18
            #        (troop_set_slot, "trp_kingdom_4_pretender", slot_troop_support_base,     "p_town_12"), #wercheg
			#        (troop_set_slot, "trp_kingdom_5_pretender", slot_troop_support_base,     "p_town_3"), #veluca
			##diplomacy start+
			(troop_set_slot, "trp_kingdom_1_pretender", slot_troop_home, "p_town_4"),#Lady Isolle - Suno
			(troop_set_slot, "trp_kingdom_2_pretender", slot_troop_home, "p_town_11"),#Prince Valdym - Curaw
			(troop_set_slot, "trp_kingdom_3_pretender", slot_troop_home, "p_town_18"),#Dustum Khan - Narra
			(troop_set_slot, "trp_kingdom_4_pretender", slot_troop_home, "p_town_12"),#Lethwin Far-Seeker - Wercheg
			(troop_set_slot, "trp_kingdom_5_pretender", slot_troop_home, "p_town_3"),#Lord Kastor - Veluca
			(troop_set_slot, "trp_kingdom_6_pretender", slot_troop_home, "p_town_20"),#Arwa the Pearled One - Durquba
			##diplomacy end+
			(try_for_range, ":pretender", pretenders_begin, pretenders_end),
				(troop_set_slot, ":pretender", slot_lord_reputation_type, lrep_none),
				##diplomacy start+
				(troop_get_slot, ":home", ":pretender", slot_troop_home),
				(ge, ":home", 1),
				(neg|party_slot_ge, ":home", dplmc_slot_center_original_lord, 1),
				(party_set_slot, ":home", dplmc_slot_center_original_lord, ":pretender"),
				##diplomacy end+
			(try_end),
	#Rebellion changes end
		 ]),
        
        
        
        ("objectionable_action",
          [
            (store_script_param_1, ":action_type"),
            (store_script_param_2, ":action_string"),
            
            (assign, ":grievance_minimum", -2),
            (try_for_range, ":npc", companions_begin, companions_end),
              (main_party_has_troop, ":npc"),
              
              ###Primary morality check
              (try_begin),
                (troop_slot_eq, ":npc", slot_troop_morality_type, ":action_type"),
                (troop_get_slot, ":value", ":npc", slot_troop_morality_value),
                (try_begin),
                  (troop_slot_eq, ":npc", slot_troop_morality_state, tms_acknowledged),
                  # npc is betrayed, major penalty to player honor and morale
                  (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
                  (val_mul, ":value", 2),
                  (val_add, ":grievance", ":value"),
                  (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),
                (else_try),
                  (this_or_next|troop_slot_eq, ":npc", slot_troop_morality_state, tms_dismissed),
                  (eq, "$disable_npc_complaints", 1),
                  # npc is quietly disappointed
                  (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
                  (val_add, ":grievance", ":value"),
                  (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),
                (else_try),
                  # npc raises the issue for the first time
                  (troop_slot_eq, ":npc", slot_troop_morality_state, tms_no_problem),
                  (gt, ":value", ":grievance_minimum"),
                  (assign, "$npc_with_grievance", ":npc"),
                  (assign, "$npc_grievance_string", ":action_string"),
                  (assign, "$npc_grievance_slot", slot_troop_morality_state),
                  (assign, ":grievance_minimum", ":value"),
                  (assign, "$npc_praise_not_complaint", 0),
                  (try_begin),
                    (lt, ":value", 0),
                    (assign, "$npc_praise_not_complaint", 1),
                  (try_end),
                (try_end),
                
                ###Secondary morality check
              (else_try),
                (troop_slot_eq, ":npc", slot_troop_2ary_morality_type, ":action_type"),
                (troop_get_slot, ":value", ":npc", slot_troop_2ary_morality_value),
                (try_begin),
                  (troop_slot_eq, ":npc", slot_troop_2ary_morality_state, tms_acknowledged),
                  # npc is betrayed, major penalty to player honor and morale
                  (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
                  (val_mul, ":value", 2),
                  (val_add, ":grievance", ":value"),
                  (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),
                (else_try),
                  (this_or_next|troop_slot_eq, ":npc", slot_troop_2ary_morality_state, tms_dismissed),
                  (eq, "$disable_npc_complaints", 1),
                  # npc is quietly disappointed
                  (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
                  (val_add, ":grievance", ":value"),
                  (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),
                (else_try),
                  # npc raises the issue for the first time
                  (troop_slot_eq, ":npc", slot_troop_2ary_morality_state, tms_no_problem),
                  (gt, ":value", ":grievance_minimum"),
                  (assign, "$npc_with_grievance", ":npc"),
                  (assign, "$npc_grievance_string", ":action_string"),
                  (assign, "$npc_grievance_slot", slot_troop_2ary_morality_state),
                  (assign, ":grievance_minimum", ":value"),
                  (assign, "$npc_praise_not_complaint", 0),
                  (try_begin),
                    (lt, ":value", 0),
                    (assign, "$npc_praise_not_complaint", 1),
                  (try_end),
                (try_end),
              (try_end),
              
              (try_begin),
                (gt, "$npc_with_grievance", 0),
                (eq, "$npc_praise_not_complaint", 0),
                (str_store_troop_name, 4, "$npc_with_grievance"),
                (display_message, "@{s4} looks upset."),
              (try_end),
            (try_end),
        ]),
        
        
        ("post_battle_personality_clash_check",
          [
            (try_for_range, ":npc", companions_begin, companions_end),
              (eq, "$disable_npc_complaints", 0),
              
              (main_party_has_troop, ":npc"),
              (neg|troop_is_wounded, ":npc"),
              
              (troop_get_slot, ":other_npc", ":npc", slot_troop_personalityclash2_object),
              (main_party_has_troop, ":other_npc"),
              (neg|troop_is_wounded, ":other_npc"),
              
              #                (store_random_in_range, ":random", 0, 3),
              (try_begin),
                (troop_slot_eq, ":npc", slot_troop_personalityclash2_state, 0),
                (try_begin),
                  #                        (eq, ":random", 0),
                  (assign, "$npc_with_personality_clash_2", ":npc"),
                (try_end),
              (try_end),
              
            (try_end),
            
            (try_for_range, ":npc", companions_begin, companions_end),
              (troop_slot_eq, ":npc", slot_troop_personalitymatch_state, 0),
              (eq, "$disable_npc_complaints", 0),
              
              (main_party_has_troop, ":npc"),
              (neg|troop_is_wounded, ":npc"),
              
              (troop_get_slot, ":other_npc", ":npc", slot_troop_personalitymatch_object),
              (main_party_has_troop, ":other_npc"),
              (neg|troop_is_wounded, ":other_npc"),
              (assign, "$npc_with_personality_match", ":npc"),
            (try_end),
            
            
            (try_begin),
              (gt, "$npc_with_personality_clash_2", 0),
              (try_begin),
                (eq, "$cheat_mode", 1),
                (display_message, "str_personality_clash_conversation_begins"),
              (try_end),
              
              (try_begin),
                (main_party_has_troop, "$npc_with_personality_clash_2"),
                (assign, "$npc_map_talk_context", slot_troop_personalityclash2_state),
                (start_map_conversation, "$npc_with_personality_clash_2"),
              (else_try),
                (assign, "$npc_with_personality_clash_2", 0),
              (try_end),
            (else_try),
              (gt, "$npc_with_personality_match", 0),
              (try_begin),
                (eq, "$cheat_mode", 1),
                (display_message, "str_personality_match_conversation_begins"),
              (try_end),
              
              (try_begin),
                (main_party_has_troop, "$npc_with_personality_match"),
                (assign, "$npc_map_talk_context", slot_troop_personalitymatch_state),
                (start_map_conversation, "$npc_with_personality_match"),
              (else_try),
                (assign, "$npc_with_personality_match", 0),
              (try_end),
            (try_end),
        ]),
        
        #script_event_player_defeated_enemy_party
        # INPUT: none
        # OUTPUT: none
        ("event_player_defeated_enemy_party",
          [(try_begin),
              (check_quest_active, "qst_raid_caravan_to_start_war"),
              (neg|check_quest_concluded, "qst_raid_caravan_to_start_war"),
              (party_slot_eq, "$g_enemy_party", slot_party_type, spt_kingdom_caravan),
              (store_faction_of_party, ":enemy_faction", "$g_enemy_party"),
              (quest_slot_eq, "qst_raid_caravan_to_start_war", slot_quest_target_faction, ":enemy_faction"),
              (quest_get_slot, ":cur_state", "qst_raid_caravan_to_start_war", slot_quest_current_state),
              (quest_get_slot, ":quest_target_amount", "qst_raid_caravan_to_start_war", slot_quest_target_amount),
              (val_add, ":cur_state", 1),
              (quest_set_slot, "qst_raid_caravan_to_start_war", slot_quest_current_state, ":cur_state"),
              (try_begin),
                (ge, ":cur_state", ":quest_target_amount"),
                (quest_get_slot, ":quest_target_faction", "qst_raid_caravan_to_start_war", slot_quest_target_faction),
                (quest_get_slot, ":quest_giver_troop", "qst_raid_caravan_to_start_war", slot_quest_giver_troop),
                (store_troop_faction, ":quest_giver_faction", ":quest_giver_troop"),
                (call_script, "script_diplomacy_start_war_between_kingdoms", ":quest_target_faction", ":quest_giver_faction", 1),
                (call_script, "script_succeed_quest", "qst_raid_caravan_to_start_war"),
              (try_end),
            (try_end),
			## Floris - Trade with Merchant Caravans
			(try_begin),
				(party_slot_eq, "$g_enemy_party", slot_party_type, spt_kingdom_caravan),
				#(display_message, "@Called-player"), #DEBUG
				(party_get_slot, ":num_goods", "$g_enemy_party", slot_town_trade_good_productions_begin),
				(party_set_slot, "$g_enemy_party", slot_town_wealth, 0),
				(party_set_slot, "$g_enemy_party", slot_town_prosperity, 0),
				(gt, ":num_goods", 0),
				(val_add, ":num_goods", 1),
				(try_for_range, ":i", 1, ":num_goods"),
					(store_add, ":slot", slot_town_trade_good_productions_begin, ":i"), 
					(party_set_slot, "$g_enemy_party", ":slot", 0),	
				(try_end),
			(try_end),
			## Floris - Trade with Merchant Caravans
            
        ]),
        
        #script_event_player_captured_as_prisoner
        # INPUT: none
        # OUTPUT: none
        ("event_player_captured_as_prisoner",
          [
            (try_begin),
              (check_quest_active, "qst_raid_caravan_to_start_war"),
              (neg|check_quest_concluded, "qst_raid_caravan_to_start_war"),
              (quest_get_slot, ":quest_target_faction", "qst_raid_caravan_to_start_war", slot_quest_target_faction),
              (store_faction_of_party, ":capturer_faction", "$capturer_party"),
              (eq, ":quest_target_faction", ":capturer_faction"),
              (call_script, "script_fail_quest", "qst_raid_caravan_to_start_war"),
            (try_end),
            #Removing followers of the player
            (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
              (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
              (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
              (gt, ":party_no", 0),
              (party_is_active, ":party_no"),
              (party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
              (party_slot_eq, ":party_no", slot_party_ai_object, "p_main_party"),
              (call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
              #          (party_set_slot, ":party_no", slot_party_commander_party, -1),
              (assign, "$g_recalculate_ais", 1),
            (try_end),
            ## Companions Overview, by Jedediah Q, modified by lazeras
            #(assign, ":jq_companions_morale", ":personality_grievances"), 	# Choice of companions
            #(assign, ":jq_leadership_morale", ":morality_grievances"), 		# Your leadership
            #(assign, ":jq_general_morale", ":troop_morale"), 				# The general state of affairs
            ##
        ]),
        
        #NPC morale both returns a string and reg0 as the morale value
        ("npc_morale",
          [
            (store_script_param_1, ":npc"),
            
            (troop_get_slot, ":morality_grievances", ":npc", slot_troop_morality_penalties),
            (troop_get_slot, ":personality_grievances", ":npc", slot_troop_personalityclash_penalties),
            (party_get_morale, ":party_morale", "p_main_party"),
            
            (store_sub, ":troop_morale", ":party_morale", ":morality_grievances"),
            (val_sub, ":troop_morale", ":personality_grievances"),
            (val_add, ":troop_morale", 50),
            
            (assign, reg8, ":troop_morale"),
            
            (val_mul, ":troop_morale", 3),
            (val_div, ":troop_morale", 4),
            (val_clamp, ":troop_morale", 0, 100),
            
            (assign, reg5, ":party_morale"),
            (assign, reg6, ":morality_grievances"),
            (assign, reg7, ":personality_grievances"),
            (assign, reg9, ":troop_morale"),
            
            #        (str_store_troop_name, s11, ":npc"),
            #        (display_message, "@{!}{s11}'s morale = PM{reg5} + 50 - MG{reg6} - PG{reg7} = {reg8} x 0.75 = {reg9}"),
            
            (try_begin),
              (lt, ":morality_grievances", 3),
              (str_store_string, 7, "str_happy"),
            (else_try),
              (lt, ":morality_grievances", 15),
              (str_store_string, 7, "str_content"),
            (else_try),
              (lt, ":morality_grievances", 30),
              (str_store_string, 7, "str_concerned"),
            (else_try),
              (lt, ":morality_grievances", 45),
              (str_store_string, 7, "str_not_happy"),
            (else_try),
              (str_store_string, 7, "str_miserable"),
            (try_end),
            
            
            (try_begin),
              (lt, ":personality_grievances", 3),
              (str_store_string, 6, "str_happy"),
            (else_try),
              (lt, ":personality_grievances", 15),
              (str_store_string, 6, "str_content"),
            (else_try),
              (lt, ":personality_grievances", 30),
              (str_store_string, 6, "str_concerned"),
            (else_try),
              (lt, ":personality_grievances", 45),
              (str_store_string, 6, "str_not_happy"),
            (else_try),
              (str_store_string, 6, "str_miserable"),
            (try_end),
            
            
            (try_begin),
              (gt, ":troop_morale", 80),
              (str_store_string, 8, "str_happy"),
              (str_store_string, 63, "str_bar_enthusiastic"),
            (else_try),
              (gt, ":troop_morale", 60),
              (str_store_string, 8, "str_content"),
              (str_store_string, 63, "str_bar_content"),
            (else_try),
              (gt, ":troop_morale", 40),
              (str_store_string, 8, "str_concerned"),
              (str_store_string, 63, "str_bar_weary"),
            (else_try),
              (gt, ":troop_morale", 20),
              (str_store_string, 8, "str_not_happy"),
              (str_store_string, 63, "str_bar_disgruntled"),
            (else_try),
              (str_store_string, 8, "str_miserable"),
              (str_store_string, 63, "str_bar_miserable"),
            (try_end),
            
            
            (str_store_string, 21, "str_npc_morale_report"),
            (assign, reg0, ":troop_morale"),
            
        ]),
        #NPC morale both returns a string and reg0 as the morale value
        
        
        #
        ("retire_companion",
          [
            (store_script_param_1, ":npc"),
            (store_script_param_2, ":length"),
            
            (remove_member_from_party, ":npc", "p_main_party"),
            (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, 0),
            (troop_set_slot, ":npc", slot_troop_morality_penalties, 0),
            (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
            (store_add, ":return_renown", ":renown", ":length"),
            (troop_set_slot, ":npc", slot_troop_occupation, slto_retirement),
            (troop_set_slot, ":npc", slot_troop_return_renown, ":return_renown"),
        ]),
        
        #NPC companion changes end
        
        #script_reduce_companion_morale_for_clash
        #script_calculate_ransom_amount_for_troop
        # INPUT: arg1 = troop_no for companion1 arg2 = troop_no for companion2 arg3 = slot_for_clash_state
        # slot_for_clash_state means: 1=give full penalty to companion1; 2=give full penalty to companion2; 3=give penalty equally
        ("reduce_companion_morale_for_clash",
          [
            (store_script_param, ":companion_1", 1),
            (store_script_param, ":companion_2", 2),
            (store_script_param, ":slot_for_clash_state", 3),
            
            (troop_get_slot, ":clash_state", ":companion_1", ":slot_for_clash_state"),
            (troop_get_slot, ":grievance_1", ":companion_1", slot_troop_personalityclash_penalties),
            (troop_get_slot, ":grievance_2", ":companion_2", slot_troop_personalityclash_penalties),
            (try_begin),
              (eq, ":clash_state", pclash_penalty_to_self),
              (val_add, ":grievance_1", 5),
            (else_try),
              (eq, ":clash_state", pclash_penalty_to_other),
              (val_add, ":grievance_2", 5),
            (else_try),
              (eq, ":clash_state", pclash_penalty_to_both),
              (val_add, ":grievance_1", 3),
              (val_add, ":grievance_2", 3),
            (try_end),
            (troop_set_slot, ":companion_1", slot_troop_personalityclash_penalties, ":grievance_1"),
            (troop_set_slot, ":companion_2", slot_troop_personalityclash_penalties, ":grievance_2"),
        ]),
        
        #Hunting scripts end
        
        #script_calculate_ransom_amount_for_troop
        # INPUT: arg1 = troop_no
        # OUTPUT: reg0 = ransom_amount
        ("calculate_ransom_amount_for_troop",
          [(store_script_param, ":troop_no", 1),
            (store_troop_faction, ":faction_no", ":troop_no"),
            (assign, ":ransom_amount", 400),
            
            (assign, ":male_relative", -9), #for kingdom ladies, otherwise a number otherwise unused in slot_town_lord
            (try_begin),
              (faction_slot_eq, ":faction_no", slot_faction_leader, ":troop_no"),
              (val_add, ":ransom_amount", 4000),
            (else_try),
              (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_lady),
              (val_add, ":ransom_amount", 2500), #as though a renown of 1250 -- therefore significantly higher than for roughly equivalent lords
              (call_script, "script_get_kingdom_lady_social_determinants", ":troop_no"),
              (assign, ":male_relative", reg0),
            (try_end),
            
            (assign, ":num_center_points", 0),
            (try_for_range, ":cur_center", centers_begin, centers_end),
              (this_or_next|party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
              (party_slot_eq, ":cur_center", slot_town_lord, ":male_relative"),
              (try_begin),
                (party_slot_eq, ":cur_center", slot_party_type, spt_town),
                (val_add, ":num_center_points", 4),
              (else_try),
                (party_slot_eq, ":cur_center", slot_party_type, spt_castle),
                (val_add, ":num_center_points", 2),
              (else_try),
                (val_add, ":num_center_points", 1),
              (try_end),
            (try_end),
            (val_mul, ":num_center_points", 500),
            (val_add, ":ransom_amount", ":num_center_points"),
            (troop_get_slot, ":renown", ":troop_no", slot_troop_renown),
            (val_mul, ":renown", 2),
            (val_add, ":ransom_amount", ":renown"),
            (store_mul, ":ransom_max_amount", ":ransom_amount", 3),
            (val_div, ":ransom_max_amount", 2),
            (store_random_in_range, ":random_ransom_amount", ":ransom_amount", ":ransom_max_amount"),
            (val_div, ":random_ransom_amount", 100),
            (val_mul, ":random_ransom_amount", 100),
            (assign, reg0, ":random_ransom_amount"),
        ]),
        
        #script_offer_ransom_amount_to_player_for_prisoners_in_party
        # INPUT: arg1 = party_no
        # OUTPUT: reg0 = result (1 = offered, 0 = not offered)
        ("offer_ransom_amount_to_player_for_prisoners_in_party",
          [(store_script_param, ":party_no", 1),
            (assign, ":result", 0),
            (party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
            (try_for_range, ":i_stack", 0, ":num_stacks"),
              (eq, ":result", 0),
              (party_prisoner_stack_get_troop_id, ":stack_troop", ":party_no", ":i_stack"),
              (troop_is_hero, ":stack_troop"),
              (this_or_next|troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
              (troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_lady),
              (store_troop_faction, ":stack_troop_faction", ":stack_troop"),
              (store_random_in_range, ":random_no", 0, 100),
              (try_begin),
                (faction_slot_eq, ":stack_troop_faction", slot_faction_state, sfs_active),
                (le, ":random_no", 5),
                (neq, "$g_ransom_offer_rejected", 1),
                (assign, ":num_stacks", 0), #break
                (assign, ":result", 1),
                (assign, "$g_ransom_offer_troop", ":stack_troop"),
                (assign, "$g_ransom_offer_party", ":party_no"),
                (jump_to_menu, "mnu_enemy_offer_ransom_for_prisoner"),
              (try_end),
            (try_end),
            (assign, reg0, ":result"),
        ]),
        
        # script_event_hero_taken_prisoner_by_player
        # Input: arg1 = troop_no
        # Output: none
        ("event_hero_taken_prisoner_by_player",
          [
            (store_script_param_1, ":troop_no"),
            (try_begin),
              (check_quest_active, "qst_persuade_lords_to_make_peace"),
              (try_begin),
                (quest_slot_eq, "qst_persuade_lords_to_make_peace", slot_quest_target_troop, ":troop_no"),
                (val_mul, ":troop_no", -1),
                (quest_set_slot, "qst_persuade_lords_to_make_peace", slot_quest_target_troop, ":troop_no"),
                (val_mul, ":troop_no", -1),
              (else_try),
                (quest_slot_eq, "qst_persuade_lords_to_make_peace", slot_quest_object_troop, ":troop_no"),
                (val_mul, ":troop_no", -1),
                (quest_set_slot, "qst_persuade_lords_to_make_peace", slot_quest_object_troop, ":troop_no"),
                (val_mul, ":troop_no", -1),
              (try_end),
              (neg|check_quest_concluded, "qst_persuade_lords_to_make_peace"),
              (neg|quest_slot_ge, "qst_persuade_lords_to_make_peace", slot_quest_target_troop, 0),
              (neg|quest_slot_ge, "qst_persuade_lords_to_make_peace", slot_quest_object_troop, 0),
              (call_script, "script_succeed_quest", "qst_persuade_lords_to_make_peace"),
            (try_end),
            (call_script, "script_update_troop_location_notes", ":troop_no", 0),
        ]),
        
        # script_cf_check_hero_can_escape_from_player
        # Input: arg1 = troop_no
        # Output: none (can fail)
        ("cf_check_hero_can_escape_from_player",
          [
            (store_script_param_1, ":troop_no"),
            (assign, ":quest_target", 0),
            (try_begin),
              (check_quest_active, "qst_persuade_lords_to_make_peace"),
              (this_or_next|quest_slot_eq, "qst_persuade_lords_to_make_peace", slot_quest_target_troop, ":troop_no"),
              (quest_slot_eq, "qst_persuade_lords_to_make_peace", slot_quest_object_troop, ":troop_no"),
              (assign, ":quest_target", 1),
            (else_try),
              (ge, ":troop_no", "trp_sea_raider_leader"),
              (lt, ":troop_no", "trp_bandit_leaders_end"),
              (try_begin),
                (check_quest_active, "qst_learn_where_merchant_brother_is"),
                (assign, ":quest_target", 1), #always catched
              (else_try),
                (assign, ":quest_target", -1), #always run.
              (try_end),
            (try_end),
            
            (assign, ":continue", 0),
            (try_begin),
              (eq, ":quest_target", 0), #if not quest target
              (store_random_in_range, ":rand", 0, 100),
              (lt, ":rand", hero_escape_after_defeat_chance),
              (assign, ":continue", 1),
            (else_try),
              (eq, ":quest_target", -1), #if (always run) quest target
              (assign, ":continue", 1),
            (try_end),
                  ## CC
                  (try_begin),
                    (is_between, ":troop_no", bandit_heroes_begin, bandit_heroes_end),
                    (assign, ":continue", 1),
				  ##Floris MTT begin
					(try_begin),
						(eq, "$troop_trees", troop_trees_0),
						(assign, ":templates_begin", bandit_party_template_begin),
						(assign, ":templates_end", bandit_party_template_end),
					(else_try),
						(eq, "$troop_trees", troop_trees_1),
						(assign, ":templates_begin", bandit_party_template_r_begin),
						(assign, ":templates_end", bandit_party_template_r_end),
					(else_try),
						(eq, "$troop_trees", troop_trees_2),
						(assign, ":templates_begin", bandit_party_template_e_begin),
						(assign, ":templates_end", bandit_party_template_e_end),
					(try_end),
					(try_for_range, ":pt_no", ":templates_begin", ":templates_end"), #changed from bandit_party_template_begin to bandit_party_template_end
					##Floris MTT end 
                      (party_template_slot_eq, ":pt_no", slot_party_template_hero_id, ":troop_no"),
                      (party_template_set_slot, ":pt_no", slot_party_template_has_hero, 0),
                      (party_template_set_slot, ":pt_no", slot_party_template_hero_party_id, -1),
                    (try_end),
                  (try_end),
                  ## CC
            (eq, ":continue", 1),
        ]),
        
        # script_cf_party_remove_random_regular_troop
        # Input: arg1 = party_no
        # Output: troop_id that has been removed (can fail)
        ("cf_party_remove_random_regular_troop",
          [(store_script_param_1, ":party_no"),
            (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
            (assign, ":num_troops", 0),
            (try_for_range, ":i_stack", 0, ":num_stacks"),
              (party_stack_get_troop_id, ":stack_troop", ":party_no", ":i_stack"),
              (neg|troop_is_hero, ":stack_troop"),
              (party_stack_get_size, ":stack_size", ":party_no", ":i_stack"),
              (val_add, ":num_troops", ":stack_size"),
            (try_end),
            (assign, reg0, -1),
            (gt, ":num_troops", 0),
            (store_random_in_range, ":random_troop", 0, ":num_troops"),
            (try_for_range, ":i_stack", 0, ":num_stacks"),
              (party_stack_get_troop_id, ":stack_troop", ":party_no", ":i_stack"),
              (neg|troop_is_hero, ":stack_troop"),
              (party_stack_get_size, ":stack_size", ":party_no", ":i_stack"),
              (val_sub, ":random_troop", ":stack_size"),
              (lt, ":random_troop", 0),
              (assign, ":num_stacks", 0), #break
              (party_remove_members, ":party_no", ":stack_troop", 1),
              (assign, reg0, ":stack_troop"),
            (try_end),
        ]),
        
        # script_place_player_banner_near_inventory
        # Input: none
        # Output: none
        ("place_player_banner_near_inventory",
          [
            #normal_banner_begin
            (troop_get_slot, ":troop_banner_object", "trp_player", slot_troop_banner_scene_prop),
            #custom_banner_begin
            #    	(troop_get_slot, ":flag_spr", "trp_player", slot_troop_custom_banner_flag_type),
            
            (try_begin),
              #normal_banner_begin
              (gt, ":troop_banner_object", 0),
              (scene_prop_get_instance, ":flag_object", ":troop_banner_object", 0),
              #custom_banner_begin
              #       (ge, ":flag_spr", 0),
              #       (val_add, ":flag_spr", custom_banner_flag_scene_props_begin),
              #       (scene_prop_get_instance, ":flag_object", ":flag_spr", 0),
              (try_begin),
                (ge, ":flag_object", 0),
                (get_player_agent_no, ":player_agent"),
                (agent_get_look_position, pos1, ":player_agent"),
                (position_move_y, pos1, -500),
                (position_rotate_z, pos1, 180),
                (position_set_z_to_ground_level, pos1),
                (position_move_z, pos1, 300),
                (prop_instance_set_position, ":flag_object", pos1),
              (try_end),
              (scene_prop_get_instance, ":pole_object", "spr_banner_pole", 0),
              (try_begin),
                (ge, ":pole_object", 0),
                (position_move_z, pos1, -320),
                (prop_instance_set_position, ":pole_object", pos1),
              (try_end),
            (else_try),
              (init_position, pos1),
              (position_move_z, pos1, -1000000),
              (scene_prop_get_instance, ":flag_object", banner_scene_props_begin, 0),
              (try_begin),
                (ge, ":flag_object", 0),
                (prop_instance_set_position, ":flag_object", pos1),
              (try_end),
              (scene_prop_get_instance, ":pole_object", "spr_banner_pole", 0),
              (try_begin),
                (ge, ":pole_object", 0),
                (prop_instance_set_position, ":pole_object", pos1),
              (try_end),
            (try_end),
        ]),
        
        # script_place_player_banner_near_inventory_bms
        # Input: none
        # Output: none
        ("place_player_banner_near_inventory_bms",
          [
            #normal_banner_begin
            (troop_get_slot, ":troop_banner_object", "trp_player", slot_troop_banner_scene_prop),
            #custom_banner_begin
            #      (troop_get_slot, ":flag_spr", "trp_player", slot_troop_custom_banner_flag_type),
            (try_begin),
              #normal_banner_begin
              (gt, ":troop_banner_object", 0),
              (replace_scene_props, banner_scene_props_begin, ":troop_banner_object"),
              #custom_banner_begin
              #       (ge, ":flag_spr", 0),
              #       (val_add, ":flag_spr", custom_banner_flag_scene_props_begin),
              #       (replace_scene_props, banner_scene_props_begin, ":flag_spr"),
            (try_end),
        ]),
        
        # script_stay_captive_for_hours
        # Input: arg1 = num_hours
        # Output: none
        ("stay_captive_for_hours",
          [
            (store_script_param, ":num_hours", 1),
            (store_current_hours, ":cur_hours"),
            (val_add, ":cur_hours", ":num_hours"),
            (val_max, "$g_check_autos_at_hour", ":cur_hours"),
            (val_add, ":num_hours", 1),
            (rest_for_hours, ":num_hours", 0, 0),
        ]),
]
