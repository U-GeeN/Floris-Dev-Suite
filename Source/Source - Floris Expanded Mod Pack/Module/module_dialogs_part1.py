# -*- coding: cp1254 -*-
from header_common import *
from header_dialogs import *
from header_operations import *
from header_parties import *
from header_item_modifiers import *
from header_skills import *
from header_triggers import *
from ID_troops import *
from ID_party_templates import *
##diplomacy start+
from header_troops import ca_intelligence
from header_terrain_types import *
from header_items import * #For ek_food, and so forth
##diplomacy end+
from module_constants import *
## CC
from header_items import *
from header_troops import *
## CC


####################################################################################################################
# During a dialog, the dialog lines are scanned from top to bottom.
# If the dialog-line is spoken by the player, all the matching lines are displayed for the player to pick from.
# If the dialog-line is spoken by another, the first (top-most) matching line is selected.
#
#  Each dialog line contains the following fields:
# 1) Dialogue partner: This should match the person player is talking to.
#    Usually this is a troop-id.
#    You can also use a party-template-id by appending '|party_tpl' to this field.
#    Use the constant 'anyone' if you'd like the line to match anybody.
#    Appending '|plyr' to this field means that the actual line is spoken by the player
#    Appending '|other(troop_id)' means that this line is spoken by a third person on the scene.
#       (You must make sure that this third person is present on the scene)
#
# 2) Starting dialog-state:
#    During a dialog there's always an active Dialog-state.
#    A dialog-line's starting dialog state must be the same as the active dialog state, for the line to be a possible candidate.
#    If the dialog is started by meeting a party on the map, initially, the active dialog state is "start"
#    If the dialog is started by speaking to an NPC in a town, initially, the active dialog state is "start"
#    If the dialog is started by helping a party defeat another party, initially, the active dialog state is "party_relieved"
#    If the dialog is started by liberating a prisoner, initially, the active dialog state is "prisoner_liberated"
#    If the dialog is started by defeating a party led by a hero, initially, the active dialog state is "enemy_defeated"
#    If the dialog is started by a trigger, initially, the active dialog state is "event_triggered"
# 3) Conditions block (list): This must be a valid operation block. See header_operations.py for reference.
# 4) Dialog Text (string):
# 5) Ending dialog-state:
#    If a dialog line is picked, the active dialog-state will become the picked line's ending dialog-state.
# 6) Consequences block (list): This must be a valid operation block. See header_operations.py for reference.
# 7) Voice-over (string): sound filename for the voice over. Leave here empty for no voice over
####################################################################################################################

dialogs_part1 = [

####################################################################################################################################
# LAV MODIFICATIONS START (COMPANIONS OVERSEER MOD)
####################################################################################################################################
  [anyone, "start", [(eq,"$g_lco_operation",lco_view_character)],"Here you are.","lco_conversation_end",[(change_screen_view_character)]],
####################################################################################################################################
# LAV MODIFICATIONS END (COMPANIONS OVERSEER MOD)
####################################################################################################################################
  [anyone ,"start", [(store_conversation_troop, "$g_talk_troop"),
                     (store_conversation_agent, "$g_talk_agent"),
                     (store_troop_faction, "$g_talk_troop_faction", "$g_talk_troop"),
#                     (troop_get_slot, "$g_talk_troop_relation", "$g_talk_troop", slot_troop_player_relation),
                     (call_script, "script_troop_get_player_relation", "$g_talk_troop"),
                     (assign, "$g_talk_troop_relation", reg0),
					 
					 #This may be different way to handle persuasion, which might be a little more transparent to the player in its effects
					 #Persuasion will affect the player's relation with the other character -- but only for 1 on 1 conversations
					 (store_skill_level, ":persuasion", "skl_persuasion", "trp_player"),
					 (assign, "$g_talk_troop_effective_relation", "$g_talk_troop_relation"),
					 (val_add, "$g_talk_troop_effective_relation", ":persuasion"),
					 (try_begin),
						(gt, "$g_talk_troop_effective_relation", 0),
						(store_add, ":persuasion_modifier", 10, ":persuasion"),
						(val_mul, "$g_talk_troop_effective_relation", ":persuasion_modifier"),
						(val_div, "$g_talk_troop_effective_relation", 10),
					 (else_try),
						(lt, "$g_talk_troop_effective_relation", 0),
						(store_sub, ":persuasion_modifier", 20, ":persuasion"),
						(val_mul, "$g_talk_troop_effective_relation", ":persuasion_modifier"),
						(val_div, "$g_talk_troop_effective_relation", 20),
					 (try_end),
					 (val_clamp, "$g_talk_troop_effective_relation", -100, 101), 
					 (try_begin),
						(eq, "$cheat_mode", 1),
						(assign, reg3, "$g_talk_troop_effective_relation"),
						(display_message, "str_test_effective_relation_=_reg3"),
					 (try_end),
					 
                     (try_begin),
                       (this_or_next|is_between, "$g_talk_troop", village_elders_begin, village_elders_end),
                       (is_between, "$g_talk_troop", mayors_begin, mayors_end),
                       (party_get_slot, "$g_talk_troop_relation", "$current_town", slot_center_player_relation),
                     (try_end),
                     (store_relation, "$g_talk_troop_faction_relation", "$g_talk_troop_faction", "fac_player_faction"),
                     
                     (assign, "$g_talk_troop_party", "$g_encountered_party"),
                     (try_begin),
                       (troop_slot_ge, "$g_talk_troop", slot_troop_leaded_party, 1),
                       (troop_get_slot, "$g_talk_troop_party", "$g_talk_troop", slot_troop_leaded_party),
                     (try_end),
                     
#                     (assign, "$g_talk_troop_kingdom_relation", 0),
#                     (try_begin),
#                       (gt, "$players_kingdom", 0),
#                       (store_relation, "$g_talk_troop_kingdom_relation", "$g_talk_troop_faction", "$players_kingdom"),
#                     (try_end),


                     
                     (store_current_hours, "$g_current_hours"),
                     (troop_get_slot, "$g_talk_troop_last_talk_time", "$g_talk_troop", slot_troop_last_talk_time),
                     (troop_set_slot, "$g_talk_troop", slot_troop_last_talk_time, "$g_current_hours"),
                     (store_sub, "$g_time_since_last_talk","$g_current_hours","$g_talk_troop_last_talk_time"),
                     (troop_get_slot, "$g_talk_troop_met", "$g_talk_troop", slot_troop_met),
## CC 1.322
           (val_min, "$g_talk_troop_met", 1), #the global variable goes no higher than one
           (try_begin),
              (troop_slot_eq, "$g_talk_troop", slot_troop_met, 0),
              (troop_set_slot, "$g_talk_troop", slot_troop_met, 1),
           
			 #Possible later activations of notes
            (try_begin),
              (is_between, "$g_talk_troop", kingdom_ladies_begin, kingdom_ladies_end),
            (try_end),

          (try_end),
##
##CC: Disabled in 3.124           
#              ## CC
#              (try_for_range, ":troop_no", ransom_brokers_begin, companions_end),
#                (neq, ":troop_no", "trp_kingdom_heroes_including_player_begin"),
#                (str_store_troop_name_plural, s0, ":troop_no"),
#                (troop_set_name,":troop_no", s0),
#              (try_end),
#              ## CC
##			  
## Old lines from 1.321
#					 (val_min, "$g_talk_troop_met", 1), #the global variable goes no higher than one
#					 (try_begin),
#					    (troop_slot_eq, "$g_talk_troop", slot_troop_met, 0),
#						  (troop_set_slot, "$g_talk_troop", slot_troop_met, 1),
##Floris: Update from CC 1.321
#						  ## CC
#						  (try_begin),
#                (is_between, "$g_talk_troop", ransom_brokers_begin, companions_end),
#                (neq, "$g_talk_troop", "trp_kingdom_heroes_including_player_begin"),
#                (str_store_troop_name_plural, s0, "$g_talk_troop"),
#                (troop_set_name, "$g_talk_troop", s0),
#						  (try_end),
#						  ## CC
##
#						#Possible later activations of notes
#						(try_begin),
#							(is_between, "$g_talk_troop", kingdom_ladies_begin, kingdom_ladies_end),
#						(try_end),
#						
#					 (try_end),
##

		               (try_begin),
#             	          (this_or_next|eq, "$talk_context", tc_party_encounter),
#             	          (this_or_next|eq, "$talk_context", tc_castle_commander),
		                 ##diplomacy start+
						 (try_begin),
							#Use terrain advantage if appropriate
					        (ge, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
							(assign, ":terrain_code", -1),
						    (try_begin),
								(encountered_party_is_attacker),
								(call_script, "script_dplmc_get_terrain_code_for_battle", "$g_encountered_party", "p_main_party"),
								(assign, ":terrain_code", reg0),
						    (else_try),
								(call_script, "script_dplmc_get_terrain_code_for_battle", "p_main_party", "$g_encountered_party"),
								(assign, ":terrain_code", reg0),
						    (try_end),
							#Call adjusting for terrain
							(call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_collective_enemy",":terrain_code",0,1),
							(assign, "$g_enemy_strength", reg0),
							(call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_main_party",":terrain_code",0,1),
							(assign, "$g_ally_strength", reg0),
						 (else_try),
						     #Old method: no terrain advantage
							 (call_script, "script_party_calculate_strength", "p_collective_enemy",0),
							 (assign, "$g_enemy_strength", reg0),
							 (call_script, "script_party_calculate_strength", "p_main_party",0),
							 (assign, "$g_ally_strength", reg0),
				         (try_end),
						 ##diplomacy end+
		                 (store_mul, "$g_strength_ratio", "$g_ally_strength", 100),
		            (assign, ":enemy_strength", "$g_enemy_strength"), #these two lines added to avoid div by zero error
		            (val_max, ":enemy_strength", 1),
		                 (val_div, "$g_strength_ratio", ":enemy_strength"),
		               (try_end),

                     (assign, "$g_comment_found", 0),

					 (assign, "$g_comment_has_rejoinder", 0),
					 (assign, "$g_romantic_comment_made", 0),
					 (assign, "$skip_lord_assumes_argument", 0), #a lord pre-empts a player's issue, ie, when the player is conducting a rebellion
					 (assign, "$bypass_female_vassal_explanation", 0),
					 (assign, "$g_done_wedding_comment", 0),
					 
#					 (assign, "$g_time_to_spare", 0),
					 
					 
                     (try_begin),
                       (troop_is_hero, "$g_talk_troop"),
                       (talk_info_show, 1),
                       (call_script, "script_setup_talk_info"),
                     (try_end),

					 (assign, "$g_last_comment_copied_to_s42", 0),
                     (try_begin),
                       (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
                       (call_script, "script_get_relevant_comment_to_s42"),
                       (assign, "$g_comment_found", reg0),
                     (try_end),

			   ##diplomacy start+
			   #(troop_get_type, reg65, "$g_talk_troop"),
			   ##Override reg65 with script for gender
		           (assign, reg65, 0),
		           (try_begin),
		              (call_script, "script_cf_dplmc_troop_is_female", "$g_talk_troop"),
		              (assign, reg65, 1),
		           (try_end),
			   ##diplomacy end+
               (try_begin),
                 (faction_slot_eq,"$g_talk_troop_faction",slot_faction_leader,"$g_talk_troop"),
                 (str_store_string,s64,"@{reg65?my Lady:my Lord}"), #bug fix
                 (str_store_string,s65,"@{reg65?my Lady:my Lord}"),
                 (str_store_string,s66,"@{reg65?My Lady:My Lord}"),
                 (str_store_string,s67,"@{reg65?My Lady:My Lord}"), #bug fix
               (else_try),
                 (str_store_string,s64,"@{reg65?madame:sir}"), #bug fix
                 (str_store_string,s65,"@{reg65?madame:sir}"),
                 (str_store_string,s66,"@{reg65?Madame:Sir}"),
                 (str_store_string,s67,"@{reg65?Madame:Sir}"), #bug fix
               (try_end),

					 (try_begin),
						(gt, "$cheat_mode", 0),
						(assign, reg4, "$talk_context"),
						(display_message, "@{!}DEBUG -- Talk context: {reg4}"),
					 (try_end),

					 (try_begin),
						(gt, "$cheat_mode", 0),
						(assign, reg4, "$g_time_since_last_talk"),
						(display_message, "@{!}DEBUG -- Time since last talk: {reg4}"),
					 (try_end),
					 
					 
					 (try_begin),
						(eq, "$cheat_mode", 0),
						(store_partner_quest, ":quest"),
						(ge, ":quest", 0),
						(str_store_quest_name, s4, ":quest"),
						
					 (try_end),
					 
                     (eq, 1, 0)],
   "{!}Warning: This line is never displayed. It is just for storing conversation variables.", "close_window", []],

  [anyone ,"member_chat", [
					(store_conversation_troop, "$g_talk_troop"),
                    (try_begin),
                        (is_between, "$g_talk_troop", companions_begin, companions_end),
                        (talk_info_show, 1),
                        (call_script, "script_setup_talk_info_companions"),
                    (else_try),
                        (is_between, "$g_talk_troop", pretenders_begin, pretenders_end),
                        (talk_info_show, 1),
                        (call_script, "script_setup_talk_info"),
                    (try_end),
	   
			##diplomacy start+ Get gender for troop
			##OLD: #(troop_get_type, reg65, "$g_talk_troop"),
			(assign, reg65, 0),
			(try_begin),		
				(call_script, "script_cf_dplmc_troop_is_female", "$g_talk_troop"),
				(assign, reg65, 1),
			(try_end),

            ##ALSO OLD: #  (troop_get_type, reg65, "$g_talk_troop"),
 			##diplomacy end+
              (try_begin),
                  (faction_slot_eq,"$g_talk_troop_faction",slot_faction_leader,"$g_talk_troop"),
                  (str_store_string,s64,"@{reg65?my Lady:my Lord}"), #bug fix
                  (str_store_string,s65,"@{reg65?my Lady:my Lord}"),
                  (str_store_string,s66,"@{reg65?My Lady:My Lord}"),
              (else_try),
                  (str_store_string,s64,"@{reg65?madame:sir}"), #bug fix
                  (str_store_string,s65,"@{reg65?madame:sir}"),
                  (str_store_string,s66,"@{reg65?Madame:Sir}"),
              (try_end),

					(store_current_hours, "$g_current_hours"),
					(troop_set_slot, "$g_talk_troop", slot_troop_last_talk_time, "$g_current_hours"),					 
					 
                    (eq, 1, 0)],  
   "{!}Warning: This line is never displayed. It is just for storing conversation variables.", "close_window", []],

  [anyone ,"event_triggered", [(store_conversation_troop, "$g_talk_troop"),
                           (try_begin),
                               (is_between, "$g_talk_troop", companions_begin, companions_end),
                               (talk_info_show, 1),
                               (call_script, "script_setup_talk_info_companions"),
                           (try_end),
                               
	 			##diplomacy start+ Get gender for troop
				##OLD:
				#(troop_get_type, reg65, "$g_talk_troop"),
				##NEW:
				(try_begin),
					(call_script, "script_cf_dplmc_troop_is_female", "$g_talk_troop"),
					(assign, reg65, 1),
				(else_try),
					(assign, reg65, 0),
				(try_end),
				##diplomacy end+
               (try_begin),
                 (faction_slot_eq,"$g_talk_troop_faction",slot_faction_leader,"$g_talk_troop"),
                 (str_store_string,s64,"@{reg65?my Lady:my Lord}"), #bug fix
                 (str_store_string,s65,"@{reg65?my Lady:my Lord}"),
                 (str_store_string,s66,"@{reg65?My Lady:My Lord}"),
               (else_try),
                 (str_store_string,s64,"@{reg65?madame:sir}"), #bug fix
                 (str_store_string,s65,"@{reg65?madame:sir}"),
                 (str_store_string,s66,"@{reg65?Madame:Sir}"),
               (try_end),

					 
                     (eq, 1, 0)],  
   "{!}Warning: This line is never displayed. It is just for storing conversation variables.", "close_window", []],

  [anyone, "event_triggered",
   [
     (eq, "$talk_context", tc_give_center_to_fief),

     (assign, ":there_are_vassals", 0),
	##diplomacy start+ Handle player is co-ruler of kingdom
	(assign, ":alt_faction", "fac_player_supporters_faction"),
	(try_begin),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":alt_faction", "$players_kingdom"),
	(try_end),
#Support promoted ladies
#(assign, ":end_cond", active_npcs_end),
(assign, ":end_cond", heroes_end),
##diplomacy end+
	(try_for_range, ":troop_no", active_npcs_begin, ":end_cond"),
	 (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
	 (neq, "trp_player", ":troop_no"),
	 (store_troop_faction, ":faction_no", ":troop_no"),
	 ##diplomacy start+
	 (this_or_next|eq, ":faction_no", ":alt_faction"),
	 ##diplomacy end+
	 (eq, ":faction_no", "fac_player_supporters_faction"),
	 (val_add, ":there_are_vassals", 1),
	 (assign, ":end_cond", 0),
	(try_end),
	
	(try_begin),
	 (gt, ":there_are_vassals", 0),
	 (str_store_string, s2, "str_do_you_wish_to_award_it_to_one_of_your_vassals"),
	(else_try),
	 (str_store_string, s2, "str_who_do_you_wish_to_give_it_to"),
	(try_end),
	
	(str_store_party_name, s1, "$g_center_taken_by_player_faction"),
	(str_store_string, s5, "str_sire_my_lady_we_have_taken_s1_s2"),
	],
	"{!}{s5}", "award_fief_to_vassal",
	[]],
	
	[anyone|plyr, "award_fief_to_vassal",
	[
	(is_between, "$g_player_court", centers_begin, centers_end),
	(store_faction_of_party, ":player_court_faction", "$g_player_court"),
	##diplomacy start+ Handle player is co-ruler of kingdom
	(assign, ":is_coruler", 0),
	(try_begin),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":is_coruler", 1),
	(try_end),
	(this_or_next|eq, ":is_coruler", 1),
	##diplomacy end+
   (eq, ":player_court_faction", "fac_player_supporters_faction"),
	 ],
   "I wish to defer the appointment of a lord, until I take the counsel of my subjects.", "award_fief_to_vassal_defer",
   [
     ]],

  [anyone, "award_fief_to_vassal_defer",
   [
     ],
   "As you wish, {sire/my lady}. You may decide this matter at a later date.", "close_window",
   [
	 (try_begin),
		(faction_slot_eq, "$players_kingdom", slot_faction_political_issue, -1),
		(faction_set_slot, "$players_kingdom", slot_faction_political_issue, "$g_center_taken_by_player_faction"),
	 (try_end),	 
	 (call_script, "script_give_center_to_lord", "$g_center_taken_by_player_faction", -1, 0), #-1 for the faction lord in this script is used exclusively in this context
	 #It is only used because script_give_center_to_faction does not reset the town lord if fac_player_supporters_faction is the attacker

     (assign, "$g_center_taken_by_player_faction", -1),
	 
     #new start
     (try_begin),
       (eq, "$g_next_menu", "mnu_castle_taken"), 
       (jump_to_menu, "$g_next_menu"),
     (try_end),  
     #new end
	 
     ]],
   
   
   
   [anyone|plyr|repeat_for_troops,"award_fief_to_vassal",
   [  
(store_repeat_object, ":troop_no"),
(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
(neq, "trp_player", ":troop_no"),
(store_troop_faction, ":faction_no", ":troop_no"),
##diplomacy start+ Handle player is co-ruler of kingdom
(assign, ":alt_faction", "fac_player_supporters_faction"),
(try_begin),
	(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
	(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
	(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
	(assign, ":alt_faction", "$players_kingdom"),
(try_end),
(this_or_next|eq, ":faction_no", ":alt_faction"),
##diplomacy end+
(eq, ":faction_no", "fac_player_supporters_faction"),
(str_store_troop_name, s11, ":troop_no"),
(call_script, "script_print_troop_owned_centers_in_numbers_to_s0", ":troop_no"),

(try_begin),
##diplomacy start+ fixed bug that was preventing "promised fief" from appearing
(troop_slot_eq, ":troop_no", slot_lord_recruitment_argument, argument_benefit),
##diplomacy end+
(str_store_string, s12, "str__promised_fief"),
(else_try),
(str_clear, s12),
(try_end),

(try_begin),
 (eq, reg0, 0),
  ##diplomacy start+ write to s0 instead of s1
 (str_store_string, s0, "str_no_fiefss12"),
 ##diplomacy end+
(else_try),
 ##diplomacy start+ write to s0 instead of s1
 (str_store_string, s0, "str_fiefs_s0s12"),
 ##diplomacy end+
(try_end),

##diplomacy start+ add relation to list of lords
#add relation string
(str_store_string_reg, s12, s63),#save s63, clobbering s12 (overwritten earlier)
(call_script, "script_troop_get_player_relation", ":troop_no"),
(call_script, "script_describe_relation_to_s63", reg0),
(str_store_string_reg, s1, s63),#clobber s1
(str_store_string_reg, s63, s12),#revert s63
(str_store_string, s1, "str_dplmc_s0_comma_s1"),#write to s1
##diplomacy end+
],
   "{!}{s11} {s1}.", "award_fief_to_vassal_2",[(store_repeat_object, "$temp")]],

  [anyone|plyr, "award_fief_to_vassal",
   [
     (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", "trp_player"),
     (str_store_party_name, s1, "$g_center_taken_by_player_faction"),

	 (try_begin),
		(is_between, "$g_talk_troop", pretenders_begin, pretenders_end),
		(str_store_string, s12, "str_please_s65_"),
	 (else_try),	
		(str_clear, s12),
	 (try_end),	
	 
     (assign, ":there_are_vassals", 0),
##diplomacy start+ 
#Support promoted ladies
#(assign, ":end_cond", active_npcs_end),
(assign, ":end_cond", heroes_end),
#Handle player is co-ruler of kingdom
	(assign, ":alt_faction", "fac_player_supporters_faction"),
	(try_begin),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":alt_faction", "$players_kingdom"),
	(try_end),
	##diplomacy end+
     (try_for_range, ":troop_no", active_npcs_begin, ":end_cond"),
       (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
       (neq, "trp_player", ":troop_no"),
       (store_troop_faction, ":faction_no", ":troop_no"),
	 ##diplomacy start+
	 (this_or_next|eq, ":faction_no", ":alt_faction"),
	 ##diplomacy end+
       (eq, ":faction_no", "fac_player_supporters_faction"),
       (val_add, ":there_are_vassals", 1),
       (assign, ":end_cond", 0),
     (try_end),
     
     (try_begin),
       (gt, ":there_are_vassals", 0),
  	   (str_store_string, s2, "str_fiefs_s0"),
  	 (else_try),
  	   (str_clear, s2),
  	 (try_end),
  	 
  	 (str_store_string, s5, "str_s12i_want_to_have_s1_for_myself"),
	 ],
   "{!}{s5}", "award_fief_to_vassal_2",      
   [
     (assign, "$temp", "trp_player"),
     ]],  

  [anyone, "award_fief_to_vassal_2",
   [
     ],
   "As you wish, {sire/my lady}. {reg6?I:{reg7?You:{s11}}} will be the new {reg3?lady:lord} of {s1}.", "close_window",
   [
     (assign, ":new_owner", "$temp"),
	 
     (call_script, "script_give_center_to_lord", "$g_center_taken_by_player_faction", ":new_owner", 0),
	 (try_begin),
		(faction_slot_eq, "$players_kingdom", slot_faction_political_issue, "$g_center_taken_by_player_faction"),
		(faction_set_slot, "$players_kingdom", slot_faction_political_issue, -1),
	 (try_end),
   
     (assign, reg6, 0),
     (assign, reg7, 0),
     (try_begin),
       (eq, ":new_owner", "$g_talk_troop"),
       (assign, reg6, 1),
     (else_try),
       (eq, ":new_owner", "trp_player"),
       (assign, reg7, 1),
     (else_try),
       (str_store_troop_name, s11, ":new_owner"),
     (try_end),
     (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
     ##diplomacy start+
	##OLD: #(troop_get_type, reg3, ":new_owner"),
	##NEW:
	(assign, reg3, 0),
	(try_begin),
		(call_script, "script_cf_dplmc_troop_is_female", ":new_owner"),
		(assign, reg3, 1),
	(try_end),
	##diplomacy end+
     
     (assign, "$g_center_taken_by_player_faction", -1),	 	           

     #new start
     (try_begin),
       (eq, "$g_next_menu", "mnu_castle_taken"), 
       (jump_to_menu, "$g_next_menu"),
     (try_end),  
     #new end
     ]],

# Awarding fiefs in rebellion...
	 
  [anyone, "event_triggered",
   [
	##diplomacy start+ Handle g_talk_troop and player are co-rulers of kingdom
	(assign, ":is_coruler", 0),
	(try_begin),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(faction_slot_eq, "$players_kingdom", slot_faction_leader, "$g_talk_troop"),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":is_coruler", 1),
	(try_end),
	(this_or_next|eq, ":is_coruler", 1),
	##diplomacy end+
     (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "$g_talk_troop"),
     (ge, "$g_center_taken_by_player_faction", 0),
     (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
     ],
   "{s1} is not being managed by anyone. Whom shall I put in charge?", "center_captured_rebellion",
   []],

  [anyone|plyr|repeat_for_troops, "center_captured_rebellion",
   [
     (store_repeat_object, ":troop_no"),
     (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
     (neq, "$g_talk_troop", ":troop_no"),
     (neq, "trp_player", ":troop_no"),
     (store_troop_faction, ":faction_no", ":troop_no"),
	##diplomacy start+ Handle player is co-ruler of kingdom
	(assign, ":alt_faction", "fac_player_supporters_faction"),
	(try_begin),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":alt_faction", "$players_kingdom"),
	(try_end),
	(this_or_next|eq, ":faction_no", ":alt_faction"),
	##diplomacy end+
     (eq, ":faction_no", "fac_player_supporters_faction"),
     (str_store_troop_name, s11, ":troop_no"),
     (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", ":troop_no"),
     (try_begin),
       (eq, reg0, 0),
       (str_store_string, s1, "@(no fiefs)"),
     (else_try),
       (str_store_string, s1, "@(fiefs: {s0})"),
     (try_end),
     ],
   "{s11}. {s1}", "center_captured_rebellion_2",
   [
     (store_repeat_object, "$temp"),
     ]],

  [anyone|plyr, "center_captured_rebellion",
   [
     (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", "trp_player"),
     (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
	##diplomacy start+
	#Remove the "please" if the player is co-ruler
	(assign, reg0, 0),
	(try_begin),
		(this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, "$g_talk_troop"),
		(troop_slot_eq, "$g_talk_troop", slot_troop_spouse, "trp_player"),
	(try_end),
	],
	#"Please {s65}, I want to have {s1} for myself. (fiefs: {s0})", "center_captured_rebellion_2",
	"{reg0?{s65}:Please {s65}}, I want to have {s1} for myself. (fiefs: {s0})", "center_captured_rebellion_2",
	##diplomacy end+
   [
     (assign, "$temp", "trp_player"),
     ]],

  [anyone|plyr, "center_captured_rebellion",
   [
     (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", "$g_talk_troop"),
     (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
     ],
   "{s66}, you should have {s1} for yourself. (fiefs: {s0})", "center_captured_rebellion_2",
   [
     (assign, "$temp", "$g_talk_troop"),
     ]],

	##diplomacy start+ allow not assigning newly-captured territories in a claimant quest
	[anyone|plyr, "center_captured_rebellion",
	[
	(str_store_party_name, s1, "$g_center_taken_by_player_faction"),
	],
	"You should appoint no one yet, and decide later.",
	 "center_captured_rebellion_2_defer",
	[
	]],
	
	[anyone, "center_captured_rebellion_2_defer",
	[
	],
	"Hmmm. All right, {playername}. I value your counsel highly.  I shall defer appointment of a lord for {s1} for the time.", "close_window",
	[
	 (call_script, "script_give_center_to_lord", "$g_center_taken_by_player_faction", -1, 0),
	 (try_begin),
	          (faction_slot_eq, "$players_kingdom", slot_faction_political_issue, "$g_center_taken_by_player_faction"),
	(faction_set_slot, "$players_kingdom", slot_faction_political_issue, -1),
	(try_end),
	 (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
	 (assign, "$g_center_taken_by_player_faction", -1),
	 #new start
	 (try_begin),
	    (eq, "$g_next_menu", "mnu_castle_taken"),
	    (jump_to_menu, "$g_next_menu"),
	 (try_end),
	],
	],
	##diplomacy end+

  [anyone, "center_captured_rebellion_2",
   [
#     (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "$g_talk_troop"),
#     (ge, "$g_center_taken_by_player_faction", 0),
     ],
   "Hmmm. All right, {playername}. I value your counsel highly. {reg6?I:{reg7?You:{s11}}} will be the new {reg3?lady:lord} of {s1}.", "close_window",
   [
     (assign, ":new_owner", "$temp"),
     (call_script, "script_calculate_troop_score_for_center", ":new_owner", "$g_center_taken_by_player_faction"),
     (assign, ":new_owner_score", reg0),
	##diplomacy start+ 
	#(assign, ":total_negative_effect"),
	(assign, ":total_negative_effect", 0),
	##Handle player is co-ruler of kingdom
	(assign, ":alt_faction", "fac_player_supporters_faction"),
	(try_begin),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":alt_faction", "$players_kingdom"),
	(try_end),
	##Change next line to support promoted kingdom ladies:
	#(try_for_range, ":cur_troop", active_npcs_begin, active_npcs_end),
	(try_for_range, ":cur_troop", heroes_begin, heroes_end),
	##diplomacy end+
	(troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
	 (store_troop_faction, ":cur_faction", ":cur_troop"),
	 ##diplomacy start+
	 (this_or_next|eq, ":cur_faction", ":alt_faction"),
	 ##diplomacy end+
       (eq, ":cur_faction", "fac_player_supporters_faction"),
       (neq, ":cur_troop", ":new_owner"),
	   (neg|troop_slot_eq, ":cur_troop", slot_troop_stance_on_faction_issue, ":new_owner"),
	   (call_script, "script_troop_get_relation_with_troop", ":cur_troop", ":new_owner"),
	   (lt, reg0, 25),
	   
	   
       (call_script, "script_calculate_troop_score_for_center", ":cur_troop", "$g_center_taken_by_player_faction"),
       (assign, ":cur_troop_score", reg0),
       (gt, ":cur_troop_score", ":new_owner_score"),
       (store_sub, ":difference", ":cur_troop_score", ":new_owner_score"),
       (store_random_in_range, ":random_dif", 0, ":difference"),
       (val_div, ":random_dif", 1000),
       (gt, ":random_dif", 0),
       (val_add, ":total_negative_effect", ":random_dif"),
       (val_mul, ":random_dif", -1),
       (call_script, "script_change_player_relation_with_troop", ":cur_troop", ":random_dif"),
     (try_end),
     (val_mul, ":total_negative_effect", 2),
     (val_div, ":total_negative_effect", 3),
     (val_add, ":total_negative_effect", 5),
     (try_begin),
       (neq, ":new_owner", "trp_player"),
       (val_min, ":total_negative_effect", 30),
       (call_script, "script_change_player_relation_with_troop", ":new_owner", ":total_negative_effect"),
     (try_end),
     
     (call_script, "script_give_center_to_lord", "$g_center_taken_by_player_faction", ":new_owner", 0),
	 (try_begin),
		(faction_slot_eq, "$players_kingdom", slot_faction_political_issue, "$g_center_taken_by_player_faction"),
		(faction_set_slot, "$players_kingdom", slot_faction_political_issue, -1),
	 (try_end),
	    
     (assign, reg6, 0),
     (assign, reg7, 0),
     (try_begin),
       (eq, ":new_owner", "$g_talk_troop"),
       (assign, reg6, 1),
     (else_try),
       (eq, ":new_owner", "trp_player"),
       (assign, reg7, 1),
     (else_try),
       (str_store_troop_name, s11, ":new_owner"),
     (try_end),
     (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
     ##diplomacy start+
	##OLD:
	#(troop_get_type, reg3, ":new_owner"),
	##NEW:
	(assign, reg3, 0),
	(try_begin),
		(call_script, "script_cf_dplmc_troop_is_female", ":new_owner"),
		(assign, reg3, 1),
	(try_end),
	##diplomacy end+
     
     (assign, "$g_center_taken_by_player_faction", -1),	 	           

     #new start
     (try_begin),
       (eq, "$g_next_menu", "mnu_castle_taken"), 
       (jump_to_menu, "$g_next_menu"),
     (try_end),  
     #new end
     ]],

  #TUTORIAL START
  [anyone, "start",
   [
     (is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
     (eq, "$g_tutorial_training_ground_conversation_state", 0),
     (eq, "$g_tutorial_fighter_talk_before", 0)],
   "Hello there. We are polishing off our combat skills here with a bit of sparring practice.\
 You look like you could use a bit of training. Why don't you join us, and we can show you a few tricks.\
 And if you need explanation of any combat concepts, just ask, and I will do my best to fill you in.", "fighter_talk",
   [
     (try_begin),
       (eq, "$g_tutorial_training_ground_intro_message_being_displayed", 1),
       (assign, "$g_tutorial_training_ground_intro_message_being_displayed", 0),
       (tutorial_message, -1), #remove tutorial intro immediately before a conversation
     (try_end),
     (assign, "$g_tutorial_fighter_talk_before", 1)]],

   [anyone, "start",
   [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   (eq, "$g_tutorial_training_ground_conversation_state", 0)],
   "What do you want to practice?", "fighter_talk", []],

   [anyone, "fighter_pretalk", [],
   "Tell me what kind of practice you want.", "fighter_talk", []],
   
   [anyone|plyr, "fighter_talk",
   [],
   "I want to practice attacking.", "fighter_talk_train_attack", []],

  [anyone|plyr, "fighter_talk",
   [],
   "I want to practice blocking with my weapon.", "fighter_talk_train_parry", []],

  [anyone|plyr, "fighter_talk",
   [],
   "Let's do some sparring practice.", "fighter_talk_train_combat", []],

  [anyone|plyr, "fighter_talk",
   [(eq,1,0)],
   "{!}TODO: Let's train chamber blocking.", "fighter_talk_train_chamber", []],

  [anyone|plyr, "fighter_talk",
   [],
   "[Leave]", "close_window", []],
  
  [anyone, "fighter_talk_train_attack",
   [
     (get_player_agent_no, ":player_agent"),
     (agent_has_item_equipped, ":player_agent", "itm_practice_sword"), #TODO: add other melee weapons
     ],
   "All right. There are four principle directions for attacking. These are overhead swing, right swing, left swing and thrust.\
 Now, I will tell you which direction to attack from and you must try to do the correct attack.\
 ^^(Move your mouse while you press the left mouse button to specify attack direction. For example, to execute an overhead attack, move the mouse up at the instant you press the left mouse button.\
 The icons on your screen will help you do the correct action.)" , "fighter_talk_train_attack_2",
   []],

  [anyone|plyr, "fighter_talk_train_attack_2",  [],
   "Let's begin then. I am ready.", "close_window",
   [
     (assign, "$g_tutorial_training_ground_melee_trainer_attack", "$g_talk_troop"),
     (assign, "$g_tutorial_training_ground_melee_state", 0),
     (assign, "$g_tutorial_training_ground_melee_trainer_action_state", 0),
     (assign, "$g_tutorial_training_ground_current_score", 0),
     (assign, "$g_tutorial_training_ground_current_score_2", 0),
     (assign, "$g_tutorial_update_mouse_presentation", 0),
     ]],

  [anyone|plyr, "fighter_talk_train_attack_2",  [],
   "Actually I want to do something else.", "fighter_pretalk", []],
	 
  [anyone, "fighter_talk_train_attack",
   [(str_store_string, s3, "str_tutorial_training_ground_warning_no_weapon")],
   "{!}{s3}", "close_window",
   []],

  [anyone, "fighter_talk_train_parry",
   [
     (get_player_agent_no, ":player_agent"),
     (agent_has_item_equipped, ":player_agent", "itm_practice_sword"), #TODO: add other melee weapons
     ],
   "Unlike a shield, blocking with a weapon can only stop attacks coming from one direction.\
 For example if you block up, you'll deflect overhead attacks, but you can still be hit by side swings or thrust attacks.\
 ^^(You must press and hold down the right mouse button to block.)", "fighter_talk_train_parry_2", [ ]],

	 [anyone, "fighter_talk_train_parry_2", [],
   "I'll now attack you with different types of strokes, and I will wait until you do the correct block before attacking.\
 Try to do the correct block as soon as you can.\
 ^^(This practice is easy to do with the 'automatic block direction' setting which is the default.\
 If you go to the Options menu and change defend direction control to 'mouse movement' or 'keyboard', you'll need to manually choose block direction. This is much more challenging, but makes the game much more interesting.\
 This practice can be very useful if you use manual blocking.)", "fighter_talk_train_parry_3",
   []],
	 
  [anyone|plyr, "fighter_talk_train_parry_3",  [],
   "Let's begin then. I am ready.", "close_window",
   [
     (assign, "$g_tutorial_training_ground_melee_trainer_parry", "$g_talk_troop"),
     (assign, "$g_tutorial_training_ground_melee_state", 0),
     (assign, "$g_tutorial_training_ground_melee_trainer_action_state", 0),
     (assign, "$g_tutorial_training_ground_current_score", 0),
     ]],

  [anyone|plyr, "fighter_talk_train_parry_3",  [],
   "Actually I want to do something else.", "fighter_pretalk", []],
	 
	 

  [anyone, "fighter_talk_train_parry",
   [(str_store_string, s3, "str_tutorial_training_ground_warning_no_weapon")],
   "{!}{s3}", "close_window",
   []],

  [anyone, "fighter_talk_train_chamber",
   [
     (get_player_agent_no, ":player_agent"),
     (agent_has_item_equipped, ":player_agent", "itm_practice_sword"), #TODO: add other melee weapons
     ],
   "{!}TODO: OK.", "close_window",
   [
     (assign, "$g_tutorial_training_ground_melee_trainer_chamber", "$g_talk_troop"),
     (assign, "$g_tutorial_training_ground_melee_state", 0),
     (assign, "$g_tutorial_training_ground_melee_trainer_action_state", 0),
     (assign, "$g_tutorial_training_ground_current_score", 0),
     ]],

  [anyone, "fighter_talk_train_chamber",
   [(str_store_string, s3, "str_tutorial_training_ground_warning_no_weapon")],
   "{!}{s3}", "close_window",
   []],

  [anyone, "fighter_talk_train_combat",
   [
     (get_player_agent_no, ":player_agent"),
     (agent_has_item_equipped, ":player_agent", "itm_practice_sword"), #TODO: add other melee weapons
     ],
   "Sparring is an excellent way to prepare for actual combat.\
 We'll fight each other with non-lethal weapons now, until one of us falls to the ground.\
 You can get some bruises of course, but better that than being cut down in the real thing.", "fighter_talk_train_combat_2",
   []],

  [anyone|plyr, "fighter_talk_train_combat_2",  [],
   "Let's begin then. I am ready.", "close_window", [
     (assign, "$g_tutorial_training_ground_melee_trainer_combat", "$g_talk_troop"),
     (assign, "$g_tutorial_training_ground_melee_state", 0),
     (assign, "$g_tutorial_training_ground_melee_trainer_action_state", 0),
     ]],

  [anyone|plyr, "fighter_talk_train_combat_2",  [],
   "Actually I want to do something else.", "fighter_pretalk", []],
	 
  [anyone, "fighter_talk_train_combat",
   [(str_store_string, s3, "str_tutorial_training_ground_warning_no_weapon")],
   "{!}{s3}", "close_window",
   []],

  [anyone, "start",
   [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   (eq, "$g_tutorial_training_ground_conversation_state", 1)], #parry complete
   "Good. You were able to block my attacks successfully. You may repeat this practice and try to get faster each time, until you are confident of your defense skills. Do you want to have another go?", "fighter_parry_try_again",
   [
     (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],
	 
  [anyone, "start",
   [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   (eq, "$g_tutorial_training_ground_conversation_state", 2)], #player knocked down in parry
   "Well that didn't go too well, did it? (Remember, you must press and hold down the right mouse button to keep your block effective.) Do you want to try again?", "fighter_parry_try_again",
   [
     (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],
	 
  [anyone|plyr, "fighter_parry_try_again",
   [],
   "Yes. Let's try again.", "fighter_talk_train_parry", []],

  [anyone|plyr, "fighter_parry_try_again",
   [],
   "No, I think I am done for now.", "fighter_talk_leave_parry", []],
	 
  [anyone, "start",
   [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   (eq, "$g_tutorial_training_ground_conversation_state", 3)], #trainer knocked down in parry
   "Hey! We are doing a blocking practice, mate! You are supposed to block my attacks, not attack me back.", "fighter_parry_warn",
   [
     (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],
	 
  [anyone|plyr, "fighter_parry_warn",
   [],
   "I am sorry. Let's try once again.", "fighter_talk_train_parry", []],

  [anyone|plyr, "fighter_parry_warn",
   [],
   "Sorry. I must leave this practice now.", "fighter_talk_leave_parry", []],

  [anyone, "fighter_talk_leave_parry",
   [],
   "All right. As you wish.", "close_window", []],

  [anyone, "start",
   [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   (eq, "$g_tutorial_training_ground_conversation_state", 4)], #player knocked down in combat
   "Well that didn't go too well, did it?  Don't feel bad, and try not to do same mistakes next time. Do you want to have a go again?", "fighter_combat_try_again",
   [
     (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],
	 
  [anyone|plyr, "fighter_combat_try_again",
   [],
   "Yes. Let's do another round.", "fighter_talk_train_combat", []],

  [anyone|plyr, "fighter_combat_try_again",
   [],
   "No. That was enough for me.", "fighter_talk_leave_combat", []],

  [anyone, "fighter_talk_leave_combat",
   [],
   "Well, all right. Talk to me again if you change your mind.", "close_window", []],

  [anyone, "start",
   [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   (eq, "$g_tutorial_training_ground_conversation_state", 5)], #trainer knocked down in combat
   "Hey, that was good sparring. You defeated me, but next time I'll be more careful. Do you want to have a go again?", "fighter_combat_try_again",
   [
     (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],
	 
  # [anyone, "start",
   # [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   # (eq, "$g_tutorial_training_ground_conversation_state", 6)], #chamber complete
   # "{!}TODO: Congratulations. Anything else?", "fighter_talk",
   # [
     # (assign, "$g_tutorial_training_ground_conversation_state", 0),
     # ]],
	 
  # [anyone, "start",
   # [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   # (eq, "$g_tutorial_training_ground_conversation_state", 7)], #player knocked down in chamber
   # "{!}TODO: Want to try again?", "fighter_chamber_try_again",
   # [
     # (assign, "$g_tutorial_training_ground_conversation_state", 0),
     # ]],

  # [anyone|plyr, "fighter_chamber_try_again",
   # [],
   # "{!}TODO: OK let's try again.", "fighter_talk_train_chamber", []],

  # [anyone|plyr, "fighter_chamber_try_again",
   # [],
   # "TODO: No, let's leave it there.", "fighter_talk_leave_chamber", []],

  # [anyone, "fighter_talk_leave_chamber",
   # [],
   # "{!}TODO: OK. Bye.", "close_window", []],

  [anyone, "start",
   [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   (eq, "$g_tutorial_training_ground_conversation_state", 8)], #trainer knocked down in chamber
   "{!}TODO: What are you doing? Don't attack me except while chambering!", "fighter_chamber_warn",
   [
     (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],
	 
  [anyone, "start",
   [(is_between, "$g_talk_troop", tutorial_fighters_begin, tutorial_fighters_end),
   (eq, "$g_tutorial_training_ground_conversation_state", 9)], #attack complete
   "Very good. You have learned how to attack from any direction you want. If you like we can try this again or move to a different exercise.", "fighter_talk",
   [
     (assign, "$g_tutorial_training_ground_conversation_state", 0),
     ]],
	 

  [anyone|plyr, "fighter_chamber_warn", # unused
   [],
   "{!}TODO: Sorry, let's try once again.", "fighter_talk_train_chamber", []],

  [anyone|plyr, "fighter_chamber_warn", # unused
   [],
   "{!}TODO: Sorry. I want to leave the exercise.", "close_window", []],

  [trp_tutorial_archer_1|auto_proceed, "start",
   [],
   "{!}.", "tutorial_troop_default",
   []],

  [trp_tutorial_master_archer, "start",
   [
     (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 1),
     ],
   "Not bad. Not bad at all! You seem to have grasped the basics of archery. Now, try to do the same thing with a crossbow.\
 Take the crossbow and the bolts over there and shoot those three targets. The crossbow is much easier to shoot with compared with the bow,\
 but you need to reload it after each shot.", "archer_challenge_2", []],

	 [trp_tutorial_master_archer, "start",
   [
     (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 2),
     ],
   "Good. You didn't have too much difficulty using the crossbow either. Next you will learn to use throwing weapons.\
 Pick up the javelins you see over there and try to hit those three targets. ", 
 "archer_challenge_2", []],

  [trp_tutorial_master_archer, "start",
   [
     (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 3),
     ],
   "Well, with that you have recevied the basic skills to use all three types of ranged weapons. The rest will come with practice. Train each and every day, and in time you will be as good as the best marksmen in Calradia.", 
   "ranged_end", []],
	 
	 [trp_tutorial_master_archer, "ranged_end", [],
   "Now, you can go talk with the melee fighters or the horsemanship trainer if you haven't already done so. They can teach you important skills too.", 
   "close_window", []],

  [trp_tutorial_master_archer, "start",
   [
     (try_begin),
       (eq, "$g_tutorial_training_ground_intro_message_being_displayed", 1),
       (assign, "$g_tutorial_training_ground_intro_message_being_displayed", 0),
       (tutorial_message, -1), #remove tutorial intro immediately before a conversation
     (try_end),

     ],
   "Good day to you, young fellow. I spend my days teaching about ranged weapons to anyone that is willing to learn.\
 If you need a tutor, let me know and I'll teach you how to use the bow, the crossbow and the javelin.", "archer_talk",
   []],

  [anyone|plyr, "archer_talk",
   [
     (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
     ],
   "Yes, show me how to use ranged weapons.", "archer_challenge", []],

  # [anyone|plyr, "archer_talk",
   # [
     # (gt, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
     # ],
   # "{!}TODO: I want to move to the next stage.", "archer_challenge", []],

  [anyone|plyr, "archer_talk",
   [],
   "No, not now.", "close_window", []],

  [trp_tutorial_master_archer, "archer_challenge",
   [
     (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
     ],
   "All right. Your first training will be in bowmanship. The bow is a difficult weapon to master. But once you are sufficiently good at it, you can shoot quickly and with great power.\
 Go pick up the bow and arrows you see over there now and shoot those targets.", "archer_challenge_2",
   []],

  # [trp_tutorial_master_archer, "archer_challenge",
   # [
     # (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 1),
     # ],
   # "{!}TODO: Make 3 shots with crossbow.", "archer_challenge_2",
   # []],

  # [trp_tutorial_master_archer, "archer_challenge",
   # [],
   # "{!}TODO: Make 3 shots with javelin.", "archer_challenge_2",
   # []],

  [anyone|plyr, "archer_challenge_2",
   [],
   "All right. I am ready.", "close_window",
   [
     (assign, "$g_tutorial_training_ground_archer_trainer_state", 1),
     (try_begin),
       (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
       (assign, "$g_tutorial_training_ground_archer_trainer_item_1", "itm_practice_bow"),
       (assign, "$g_tutorial_training_ground_archer_trainer_item_2", "itm_practice_arrows"),
     (else_try),
       (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 1),
       (assign, "$g_tutorial_training_ground_archer_trainer_item_1", "itm_practice_crossbow"),
       (assign, "$g_tutorial_training_ground_archer_trainer_item_2", "itm_practice_bolts"),
     (else_try),
       (assign, "$g_tutorial_training_ground_archer_trainer_item_1", "itm_practice_javelin"),
       (assign, "$g_tutorial_training_ground_archer_trainer_item_2", -1),
     (try_end),
     ]],

  [anyone|plyr, "archer_challenge_2",
   [],
   "Just a minute. I want to do something else first.", "close_window",
   []],


  [trp_tutorial_master_horseman, "start",
   [
     (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 1),
     ],
   "I hope you enjoyed the ride. Now we move on to something a bit more difficult. Grab the lance you see over there and ride around the course hitting each target at least once.", 
   "horseman_melee_challenge_2", []],
   
  [trp_tutorial_master_horseman, "start",
   [
     (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 2),
     ],
   "Good! You have been able to hit all targets on horseback. That's no easy feat for a starter. Your next challange will be using a bow and arrows to shoot at the archery targets by the road. You need to put an arrow to each target to consider yourself successful.", 
 "horseman_melee_challenge_2", []],

  [trp_tutorial_master_horseman, "start",
   [
     (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 3),
     ],
   "Very good. You were able to shoot all targets from horseback. Keep riding and practicing each day and in time you will be an expert horseman.", "horsemanship_end",
   [
     ]],
	 
	 [trp_tutorial_master_horseman, "horsemanship_end",
   [
     ],
   "Now, you can go talk with the melee fighters or the archery trainer if you haven't already done so. You need to learn everything you can to be prepared when you have to defend yourself.", "close_window",
   []],
	 

	 
  [trp_tutorial_master_horseman, "start",
   [
     (try_begin),
       (eq, "$g_tutorial_training_ground_intro_message_being_displayed", 1),
       (assign, "$g_tutorial_training_ground_intro_message_being_displayed", 0),
       (tutorial_message, -1), #remove tutorial intro immediately before a conversation
     (try_end),
     ],
   "Good day! I have come here for some riding practice, but my old bones are aching badly so I decided to give myself a rest today.\
 If you would like to practice your horsemanship, you can take my horse here. The exercise would be good for her.", "horseman_talk",
   []],

  [anyone|plyr, "horseman_talk",
   [],
   "Yes, I would like to practice riding.", "horseman_challenge", []],

  [anyone|plyr, "horseman_talk",
   [],
   "Uhm. Maybe later.", "close_window", []],

  # [trp_tutorial_master_horseman, "horseman_challenge",
   # [
     # (eq, "$g_tutorial_training_ground_player_continue_without_basics", 0),
     # (this_or_next|eq, "$g_tutorial_training_ground_melee_trainer_attack_completed", 0),
     # (eq, "$g_tutorial_training_ground_archer_trainer_completed_chapters", 0),
    # ],
   # "Hmm. Do you know how to use your weapons? You'd better learn to use those on foot before you start to train using them on horseback.", "horseman_ask",
   # []],

  # [anyone|plyr, "horseman_ask",
   # [],
   # "Yes, I know ", "horseman_challenge",
   # [
     # (assign, "$g_tutorial_training_ground_player_continue_without_basics", 1),
     # ]],

  # [anyone|plyr, "horseman_ask",
   # [],
   # "{!}TODO: No", "horseman_ask_2",
   # []],

  # [trp_tutorial_master_horseman, "horseman_ask_2",
   # [],
   # "{!}TODO: Come back later then.", "close_window",
   # []],

  [trp_tutorial_master_horseman, "horseman_challenge",
   [
     (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 0),
    ],
   "Good. Now, I will give you a few exercises that'll teach you riding and horseback weapon use.\
 Your first assignment is simple. Just take your horse for a ride around the course.\
 Go as slow or as fast as you like.\
 Come back when you feel confident as a rider and I'll give you some tougher exercises.", "horseman_melee_challenge_2",
   []],

  [anyone|plyr, "horseman_melee_challenge_2",
   [],
   "All right. I am ready.", "close_window",
   [
     (assign, "$g_tutorial_training_ground_horseman_trainer_state", 1),
     (try_begin),
       (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 0),
       (assign, "$g_tutorial_training_ground_horseman_trainer_item_1", -1),
       (assign, "$g_tutorial_training_ground_horseman_trainer_item_2", -1),
     (else_try),
       (eq, "$g_tutorial_training_ground_horseman_trainer_completed_chapters", 1),
       (assign, "$g_tutorial_training_ground_horseman_trainer_item_1", "itm_arena_lance"),
       (assign, "$g_tutorial_training_ground_horseman_trainer_item_2", -1),
     (else_try),
       (assign, "$g_tutorial_training_ground_horseman_trainer_item_1", "itm_practice_bow"),
       (assign, "$g_tutorial_training_ground_horseman_trainer_item_2", "itm_practice_arrows"),
     (try_end),
     ]],

  [anyone|plyr, "horseman_melee_challenge_2",
   [],
   "Just a minute. I need to do something else first.", "close_window", []],

  [trp_tutorial_rider_1|auto_proceed, "start",
   [],
   "{!}Warning: This line is never displayed.", "tutorial_troop_default",
   []],

  [trp_tutorial_rider_2|auto_proceed, "start",
   [],
   "{!}Warning: This line is never displayed.", "tutorial_troop_default",
   []],

  [anyone, "tutorial_troop_default",
   [
     (try_begin),
       (eq, "$g_tutorial_training_ground_intro_message_being_displayed", 1),
       (assign, "$g_tutorial_training_ground_intro_message_being_displayed", 0),
       (tutorial_message, -1), #remove tutorial intro immediately before a conversation
     (try_end),
     ],
   "Hey, I am trying to practice here. Go, talk with the archery trainer if you need guidance about ranged weapons.", "close_window", []],


   #PRISON BREAK START
   [anyone,"start",
   [                    
     (eq, "$talk_context", tc_prison_break),                    
     (troop_slot_eq, "$g_talk_troop", slot_troop_prisoner_of_party, "$g_encountered_party"),
     (troop_slot_ge, "$g_talk_troop", slot_troop_mission_participation, mp_stay_out),
   ],
   "Is there a change of plans?", "lord_prison_break_confirm_3",[]],
   
   [anyone,"start",
   [
     (eq, "$talk_context", tc_prison_break),
     (try_begin),
       (eq, "$cheat_mode", 1),
       (assign, reg0, "$g_talk_troop"),
       (assign, reg1, "$g_encountered_party"),
       (troop_get_slot, reg2, "$g_talk_troop", slot_troop_prisoner_of_party),
       (display_message, "@{!}g_talk_troop = {reg0} , g_encountered_party = {reg1} , slot value = {reg2}"),
     (try_end),
     (troop_slot_eq, "$g_talk_troop", slot_troop_prisoner_of_party, "$g_encountered_party"),
   ],
   "What's going on?", "lord_prison_break",[]],
   
   
   #TAVERN DRUNK DIALOGS
   [anyone, "start", 
   [
	(eq, "$g_talk_troop", "trp_belligerent_drunk"),
	],
   "What are you looking at?", "drunk_response", 
   [
     (try_begin),
       (eq, "$g_main_attacker_agent", 0),
       (call_script, "script_activate_tavern_attackers"),       
     (try_end),
     (mission_disable_talk),
   ]],

   [anyone, "start", 
   [
	(eq, "$g_talk_troop", "trp_hired_assassin"),
	],
   "Are you looking at me?", "drunk_response", 
   [
     (try_begin),
       (eq, "$g_main_attacker_agent", 0),
       (call_script, "script_activate_tavern_attackers"),       
     (try_end),
     (mission_disable_talk),
   ]],

   [anyone, "start", 
   [
	(eq, "$g_talk_troop", "trp_hired_assassin"),
		(eq,1,0),
	],
   "{!}Added to match dialog ids with translations.", "close_window", 
   []],
 
   
  [anyone, "start", [
  (is_between, "$g_talk_troop", tavernkeepers_begin, tavernkeepers_end),
  (gt, "$g_main_attacker_agent", 0),
  (neg|agent_is_alive, "$g_main_attacker_agent"),
  
  (try_begin),
 	(neg|agent_is_alive, "$g_main_attacker_agent"),
	(agent_get_troop_id, ":type", "$g_main_attacker_agent"),
	(eq, ":type", "trp_hired_assassin"),
	(str_store_string, s9, "str_strange_that_one_didnt_seem_like_your_ordenary_troublemaker_he_didnt_drink_all_that_much__he_just_stood_there_quietly_and_watched_the_door_you_may_wish_to_consider_whether_you_have_any_enemies_who_know_you_are_in_town_a_pity_that_blood_had_to_be_spilled_in_my_establishment"),

    (assign, "$g_main_attacker_agent", 0),
	(troop_add_gold, "trp_player", 50),
	(troop_add_item, "trp_player", "itm_we_nor_sword_pict", 0),
	
  (else_try),
	#(display_message, "str_wielded_item_reg3"),
	
	(lt, "$g_attacker_drawn_weapon", "itm_tutorial_spear"),
	(str_store_string, s9, "str_you_never_let_him_draw_his_weapon_still_it_looked_like_he_was_going_to_kill_you_take_his_sword_and_purse_i_suppose_he_was_trouble_but_its_not_good_for_an_establishment_to_get_a_name_as_a_place_where_men_are_killed"),

    (assign, "$g_main_attacker_agent", 0),
	(troop_add_gold, "trp_player", 50),
	(troop_add_item, "trp_player", "itm_we_nor_sword_pict", 0),
	(call_script, "script_troop_change_relation_with_troop", "trp_player", "$g_talk_troop", -1),
  (else_try),
	(neg|agent_is_alive, "$g_main_attacker_agent"),
	(str_store_string, s9, "str_well_id_say_that_he_started_it_that_entitles_you_to_his_sword_and_purse_i_suppose_have_a_drink_on_the_house_as_i_daresay_youve_saved_a_patron_or_two_a_broken_skull_still_i_hope_he_still_has_a_pulse_its_not_good_for_an_establishment_to_get_a_name_as_a_place_where_men_are_killed"),
    (assign, "$g_main_attacker_agent", 0),
	(troop_add_gold, "trp_player", 50),
	(troop_add_item, "trp_player", "itm_we_nor_sword_pict", 0),
	(call_script, "script_troop_change_relation_with_troop", "trp_player", "$g_talk_troop", 1),
  (try_end),	
  (troop_set_slot, "trp_hired_assassin", slot_troop_cur_center, -1),
  ],
   "{!}{s9}", "player_duel_response", [
   ]],

   
  [anyone, "start", [
  (is_between, "$g_talk_troop", tavernkeepers_begin, tavernkeepers_end),
  (gt, "$g_main_attacker_agent", 0),
  (try_begin),
	(get_player_agent_no, ":player_agent"),
	(agent_get_wielded_item, ":wielded_item", ":player_agent", 0),
	(is_between, ":wielded_item", "itm_we_swa_bow_practice", "itm_we_swa_throw_stone"),
	(str_store_string, s9, "str_stop_no_shooting_no_shooting"),

    (assign, ":default_item", -1),
	(troop_get_inventory_capacity, ":end_cond", "trp_player"), 
	(try_for_range, ":i_slot", 0, ":end_cond"),
      (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
      
      (is_between, ":item_id", weapons_begin, weapons_end),
      (neg|is_between, ":item_id", weapons_ranged_begin, weapons_ranged_end),
      
      (assign, ":default_item", ":item_id"),
      (assign, ":end_cond", 0), #break
    (try_end),
	
	(agent_set_wielded_item, ":player_agent", ":default_item"),
  (else_try),
	(str_store_string, s9, "str_em_ill_stay_out_of_this"),
  (try_end),
  ],
   "{!}{s9}", "close_window", [
   ]],

  [anyone|plyr, "player_duel_response", [],
   "Such a waste...", "close_window", [
   ]],
   
  [anyone|plyr, "player_duel_response", [],
   "Better him than me.", "close_window", [
   ]],

   
  [anyone|plyr, "drunk_response", [],
   "I'm not sure... Some sort of animal, clearly.", "drunk_fight_start", [
   ]],
   
[anyone|plyr, "drunk_response", [],
##diplomacy start+ Change this so there is some chance of success
#to avoid a fight.
##OLD:
#"Excuse me -- please accept my apologies", "drunk_fight_start", [
#]],
##NEW:
"Excuse me -- please accept my apologies", "dplmc_drunk_attempt_placate", [
]],

[anyone, "dplmc_drunk_attempt_placate", [
(neq, "$g_talk_troop", "trp_hired_assassin"),
#Right now this is the same as the check in Native to persuade a companion to stay in your party
(store_skill_level, reg1, "skl_persuasion", "trp_player"),
(store_random_in_range, reg0, -2, 13),
(try_begin),
   (ge, "$cheat_mode", 1),
	(display_message, "@{!}Persuasion attempt: skill {reg1} versus random roll {reg0} (-2 through 12)"),
(try_end),
(le, reg0, reg1),
#The persuasion attempt succeeded.
(call_script, "script_deactivate_tavern_attackers"),
],
"I'll let it slide... this time.  Now buzz off.", "close_window", [
]],

[anyone, "dplmc_drunk_attempt_placate", [],
#The persuasion attempt failed.  Fall back to the standard behavior.
"I'll wipe that smirk right off your face!", "close_window", [
(troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, 0),
]],
##diplomacy end+

  [anyone, "drunk_fight_start", [],
   "I'll wipe that smirk right off your face!", "close_window", [
	(troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, 0),	
   ]],
      
  [anyone|plyr, "drunk_response", 
  [
##diplomacy start+
#In Native this only shows up when it is guaranteed to succeed, but that
#isn't particularly interesting.
##REMOVED:
#(troop_slot_ge, "trp_player", slot_troop_renown, 150),
##diplomacy end+
],
"Do you have any idea who I am?", "drunk_player_high_renown", [
]],

[anyone, "drunk_player_high_renown", [
##diplomacy start+ Failure is also possible because you can get to this line with insufficient renown
(this_or_next|neg|troop_slot_ge, "trp_player", slot_troop_renown, 150),
##diplomacy end+
(eq, "$g_talk_troop", "trp_hired_assassin"),
],
"Do I care?", "drunk_fight_start", [
]],

##diplomacy start+ If prejudice is high, possibly increase the renown threshold required
[anyone, "drunk_player_high_renown", [
   (lt, "$g_disable_condescending_comments", 0),#prejudice mode: high
   (call_script, "script_cf_dplmc_faction_has_bias_against_gender", "$g_encountered_party_faction", "$character_gender"),
   (neg|troop_slot_ge, "trp_player", slot_troop_renown, 300),
],
"Big talk from a little runt.  I'll put you in your place!", "drunk_fight_start", [
]],
##diplomacy end+

[anyone, "drunk_player_high_renown", [
##diplomacy start+ change to use script_dplmc_print_subordinate_says_sir_madame_to_s0
(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
##diplomacy end+
],
##diplomacy start+ change to use script_dplmc_print_subordinate_says_sir_madame_to_s0
"Emmm... Actually... Yes, yes, I do know who you are, {s0}. Please forgive me, your grace -- it must be the drink. I'll be leaving, now...", "drunk_player_high_renown", [
##diplomacy end+
]],
   
  [anyone|plyr, "drunk_player_high_renown", [],
   "Why, if you want a fight, you shall have one!", "drunk_fight_start", [
   ]],
   
  [anyone|plyr, "drunk_player_high_renown", [],
   "I thought as much. Now, remove yourself from here", "close_window", 
   [
     (assign, "$drunks_dont_pick_fights", 1),
     (troop_set_slot, "trp_belligerent_drunk", slot_troop_cur_center, 0),
          
     (call_script, "script_deactivate_tavern_attackers"),
     
     (assign, "$g_belligerent_drunk_leaving", "$g_main_attacker_agent"),
     
     (mission_enable_talk),
     
     (try_for_agents, ":agent"),
       (agent_is_alive, ":agent"),
       (agent_get_position, pos4, ":agent"),
       (agent_set_scripted_destination, ":agent", pos4),
     (try_end),
     
     (entry_point_get_position, pos1, 0),
     (agent_set_scripted_destination, "$g_main_attacker_agent", pos1),
     
     (assign, "$g_main_attacker_agent", 0),
   ]],
   
   
   [anyone, "start", 
   [
	 (eq, "$g_talk_troop", "trp_fight_promoter"),	
   ],
   "You look like a {fellow/lady} who can take a few hard knocks -- and deal them out, too. I have a business proposition for you.", "fistfight_response", [
   ]],
   
  [anyone|plyr, "fistfight_response", [],
   "How's that?", "fistfight_response_2", [
   ]],

  [anyone, "fistfight_response_2", [
  ],
   "Good -- I'm glad you're interested. Here's the plan... It's a little complicated, so listen well. ", "fistfight_response_2a", [
   ]],

  [anyone, "fistfight_response_2a", [
  ],
	"You and this other fellow will start up a fight here. No weapons, no armor -- I'll sit back and take bets, and split the profits with the winner. If we make a loss, then I'll cover it. You've got nothing to lose -- except a bit of blood, of course.", "fistfight_response_3", [
   ]],

  [anyone, "fistfight_response_3", [
  ],
   "However, we can't organize this like one of those nice arena bouts, where everyone places their bets beforehand. People will walk in, drawn by the noise, and put a denar or two on whichever one of your two they think is winning. I'll give 'em even odds -- anything else is going to be too tricky for someone who's already on his third flagon of ale.", "fistfight_response_4", [
   ]],
   
  [anyone, "fistfight_response_4", [
  ],
   "So, as you can see, the trick is to stretch things out for as long as possible where it looks like you're losing, and people bet against you -- and then come back fast, and win, before the betting can turn. The best way to make money is for you to be battered almost to the floor, and then jump back off your feet and take the other guy down. However, you have to win in the end in order for me, and you, to make money. ", "fistfight_response_4a", [
   ]],
   
  [anyone, "fistfight_response_4a", [
  ],
   "Also, you can't stretch the fight out too long, or people will suspect a fix. So, one of you has to take a punch every so often. I don't care whose blood is spilled, but there has to be some blood.", "fistfight_response_5", [
   ]],

  [anyone, "fistfight_response_5", [
  ],
   "And one other thing -- my mate, your opponent, he doesn't take to well to complexity. So he's just going to come straight at you. It's up to you to supply the artistry.", "fistfight_response_5a", [
   ]],
   
  [anyone, "fistfight_response_5a", [
  ],
   "So, what do you think?", "fistfight_response_confirm", [
   ]],

  [anyone|plyr, "fistfight_response_confirm", [
  ],
   "{!}[Yes -- not yet implemented]", "close_window", [
   ]],

  [anyone|plyr, "fistfight_response_confirm", [
  ],
   "I have better things to do", "close_window", [
   ]],
   
   
   
  [trp_ramun_the_slave_trader, "start", [
   (troop_slot_eq, "$g_talk_troop", slot_troop_met_previously, 0),
   ], "Good day to you, {young man/lassie}.", "ramun_introduce_1",[]],
  [trp_ramun_the_slave_trader|plyr, "ramun_introduce_1", [], "Forgive me, you look like a trader, but I see none of your merchandise.", "ramun_introduce_2",[
   (troop_set_slot, "$g_talk_troop", slot_troop_met_previously, 1),
  ]],
  [trp_ramun_the_slave_trader|plyr, "ramun_introduce_1", [], "Never mind.", "close_window",[]],
  [trp_ramun_the_slave_trader, "ramun_introduce_2", [], "A trader? Oh, aye, I certainly am that.\
 My merchandise is a bit different from most, however. It has to be fed and watered twice a day and tries to run away if I turn my back.", "ramun_introduce_3",[]],
  [trp_ramun_the_slave_trader|plyr, "ramun_introduce_3", [], "Livestock?", "ramun_introduce_4",[]],
  [trp_ramun_the_slave_trader, "ramun_introduce_4", [], "Close enough. I like to call myself the man who keeps every boat on this ocean moving.\
 Boats are driven by oars, you see, and oars need men to pull them or they stop. That's where I come in.", "ramun_introduce_5",[]],
  [trp_ramun_the_slave_trader|plyr, "ramun_introduce_5", [], "Galley slaves.", "ramun_introduce_6",[]],
  [trp_ramun_the_slave_trader, "ramun_introduce_6", [], "Now you're catching on! A trading port like this couldn't survive without them.\
 The ships lose a few hands on every voyage, so there's always a high demand. The captains come to me and they pay well.", "ramun_introduce_7",[]],
  [trp_ramun_the_slave_trader|plyr, "ramun_introduce_7", [], "Where do the slaves come from?", "ramun_introduce_8",[]],
  [trp_ramun_the_slave_trader, "ramun_introduce_8", [], "Mostly I deal in convicted criminals bought from the authorities.\
 Others are prisoners of war from various nations, brought to me because I offer the best prices.\
 However, on occasion I'll buy from privateers and other . . . 'individuals'. You can't be picky about your suppliers in this line of work.\
 You wouldn't happen to have any prisoners with you, would you?", "ramun_introduce_9",[]],
  [trp_ramun_the_slave_trader|plyr, "ramun_introduce_9", [], "Me? ", "ramun_introduce_10",[]],
  [trp_ramun_the_slave_trader, "ramun_introduce_10", [], "Why not? If you intend to set foot outside this town,\
 you're going to cross swords with someone sooner or later. And, God willing, you'll come out on top.\
 Why not make some extra money off the whole thing? Take them alive, bring them back to me, and I'll pay you fifty denars for each head.\
 Don't much care who they are or where they come from.", "ramun_introduce_11",[]],
  [trp_ramun_the_slave_trader|plyr, "ramun_introduce_11", [], "Hmm. I'll think about it.", "ramun_introduce_12",[]],
  [trp_ramun_the_slave_trader, "ramun_introduce_12", [], "Do think about it!\
 There's a lot of silver to be made, no mistake. More than enough for the both of us.", "close_window",[]],

  [trp_ramun_the_slave_trader,"start", [], "Hello, {playername}.", "ramun_talk",[]],
  [trp_ramun_the_slave_trader,"ramun_pre_talk", [], "Anything else?", "ramun_talk",[]],

  [trp_ramun_the_slave_trader|plyr,"ramun_talk",
   [[store_num_regular_prisoners,reg(0)],[ge,reg(0),1]],
   "I've brought you some prisoners, Ramun. Would you like a look?", "ramun_sell_prisoners",[]],
   # #Floris Slaves
   # [trp_ramun_the_slave_trader|plyr,"ramun_talk",
   # [],
   # "I would like to purchase some helping hands. Do you happen to have some in stock?", "ramun_sell_slaves",[]],  
   
	 ##diplomacy start+
	#Sell all prisoneers, a la rubik's Custom Commander, except when you are asked
	#to confirm he tells you the number/price.
	  [trp_ramun_the_slave_trader|plyr,"ramun_talk",
	   [(store_num_regular_prisoners,reg0),(ge,reg0,1)],
	   "I want to sell all the prisoners I have with me.", "ramun_sell_prisoners_all",[]],
	  [trp_ramun_the_slave_trader,"ramun_sell_prisoners_all", [
	  (store_num_regular_prisoners,reg0),
	  (store_mul, reg1, reg0, 50),
	  (store_sub, reg2, reg0, 1),
	  ],
	  "I'll take your {reg0} {reg2?prisoners:prisoner} off your hands for {reg1} denars.  We have a deal?", "ramun_sell_prisoners_all_2", []],
	  [trp_ramun_the_slave_trader|plyr,"ramun_sell_prisoners_all_2", [],
	   "We have a deal.", "ramun_sell_prisoners_2", [
		(call_script, "script_dplmc_sell_all_prisoners", 1, 50),]
	  ],
	  [trp_ramun_the_slave_trader|plyr,"ramun_sell_prisoners_all_2", [],
	   "Let me think about it again.", "ramun_pre_talk",[]],
	##diplomacy end+
  [trp_ramun_the_slave_trader,"ramun_sell_prisoners", [],
  "Let me see what you have...", "ramun_sell_prisoners_2",
   [[change_screen_trade_prisoners]]],
  [trp_ramun_the_slave_trader, "ramun_sell_prisoners_2", [], "A pleasure doing business with you.", "close_window",[]],

  [trp_ramun_the_slave_trader|plyr,"ramun_talk", [(neg|troop_slot_ge,"$g_talk_troop",slot_troop_met_previously,1)], "How do I take somebody as prisoner?", "ramun_ask_about_capturing",[]],
  [trp_ramun_the_slave_trader|plyr,"ramun_talk", [(troop_slot_ge,"$g_talk_troop", slot_troop_met_previously, 1)], "Can you tell me again about capturing prisoners?", "ramun_ask_about_capturing",[(troop_set_slot,"$g_talk_troop", slot_troop_met_previously, 2)]],

  [trp_ramun_the_slave_trader,"ramun_ask_about_capturing", [(neg|troop_slot_ge,"$g_talk_troop",slot_troop_met_previously,1)],
 "You're new to this, aren't you? Let me explain it in simple terms.\
 The basic rule of taking someone prisoner is knocking him down with a blunt weapon, like a mace or a club,\
 rather than cutting him open with a sword. That way he goes to sleep for a little while rather than bleeding to death, you see?\
 I'm assuming you have a blunt weapon with you . . .", "ramun_have_blunt_weapon",[]],
  [trp_ramun_the_slave_trader|plyr,"ramun_have_blunt_weapon", [],
 "Of course.", "ramun_have_blunt_weapon_yes",[]],
  [trp_ramun_the_slave_trader|plyr,"ramun_have_blunt_weapon", [],
 "As a matter of fact, I don't.", "ramun_have_blunt_weapon_no",[]],
  [trp_ramun_the_slave_trader,"ramun_have_blunt_weapon_yes", [],
 "Good. Then all you need to do is beat the bugger down with your weapon, and when the fighting's over you clap him in irons.\
 It's a bit different for nobles and such, they tend to be protected enough that it won't matter what kind of weapon you use,\
 but your average rabble-rouser will bleed like a stuck pig if you get him with something sharp. I don't have many requirements in my merchandise,\
 but I do insist they be breathing when I buy them.", "ramun_ask_about_capturing_2",[]],
  [trp_ramun_the_slave_trader,"ramun_have_blunt_weapon_no", [],
 "No? Heh, well, this must be your lucky day. I've got an old club lying around that I was going to throw away.\
 It a bit battered, but still good enough bash someone until he stops moving.\
 Here, have it.","ramun_have_blunt_weapon_no_2",[(troop_add_item, "trp_player","itm_we_vae_blunt_club",imod_cracked)]],
  [trp_ramun_the_slave_trader|plyr,"ramun_have_blunt_weapon_no_2", [],
 "Thanks, Ramun. Perhaps I may try my hand at it.", "ramun_have_blunt_weapon_yes",[]],
  [trp_ramun_the_slave_trader,"ramun_ask_about_capturing", [],
 "Alright, I'll try and expain it again in simple terms. The basic rule of taking someone prisoner is knocking him down with a blunt weapon, like a mace or a club,\
 rather than cutting him open with a sword. That way he goes to sleep for a little while rather than bleeding to death, you see?\
 It's a bit different for nobles and such, they tend to be protected enough that it won't matter what kind of weapon you use,\
 but your average rabble-rouser will bleed like a stuck pig if you get him with something sharp.", "ramun_ask_about_capturing_2",[]],
  [trp_ramun_the_slave_trader|plyr,"ramun_ask_about_capturing_2", [], "Alright, I think I understand. Anything else?", "ramun_ask_about_capturing_3",[]],
  [trp_ramun_the_slave_trader,"ramun_ask_about_capturing_3", [],
 "Well, it's not as simple as all that. Blunt weapons don't do as much damage as sharp ones, so they won't bring your enemies down as quickly.\
 And trust me, given the chance, most of the scum you run across would just as soon kill you as look at you, so don't expect any courtesy when you pull out a club instead of a sword.\
 Moreover, having to drag prisoners to and fro will slow down your party, which is why some people simply set their prisoners free after the fighting's done.\
 It's madness. How could anyone turn down all that silver, eh?", "ramun_ask_about_capturing_4",[]],
  [trp_ramun_the_slave_trader|plyr,"ramun_ask_about_capturing_4", [],
 "Is that everything?", "ramun_ask_about_capturing_5",[]],
  [trp_ramun_the_slave_trader,"ramun_ask_about_capturing_5", [],
 "Just one final thing. Managing prisoners safely is not an easy thing to do, you could call it a skill in itself.\
 If you want to capture a lot of prisoners, you should try and learn the tricks of it yourself,\
 or you won't be able to hang on to a single man you catch.", "ramun_ask_about_capturing_7",[]],
  [trp_ramun_the_slave_trader|plyr,"ramun_ask_about_capturing_7", [],
 "Thanks, I'll keep it in mind.", "ramun_pre_talk",[]],

  [trp_ramun_the_slave_trader|plyr,"ramun_talk", [], "I'd better be going.", "ramun_leave",[]],
  [trp_ramun_the_slave_trader,"ramun_leave", [], "Remember, any prisoners you've got, bring them to me. I'll pay you good silver for every one.", "close_window",[]],

  

  
  
  
  [trp_nurse_for_lady, "start", [
#  (eq, "$talk_context", tc_garden),
	##diplomacy start+ just in case make gender-correct
	], "I humbly request that your {lordship/ladyship} keeps {his/her} hands where I can see them.", "close_window",[]],
	##diplomacy end+

##  [trp_tutorial_trainer, "start", [(eq, "$tutorial_1_state", 1),], "TODO: Watch me.", "tutorial_1_1_1",[]],
##  [trp_tutorial_trainer, "tutorial_1_1_1", [], "TODO: This is up.", "tutorial_1_1_2",[(agent_set_attack_action, "$g_talk_agent", 3),]],
##  [trp_tutorial_trainer, "tutorial_1_1_2", [], "TODO: This is left.", "tutorial_1_1_3",[(agent_set_attack_action, "$g_talk_agent", 2),]],
##  [trp_tutorial_trainer, "tutorial_1_1_3", [], "TODO: This is right.", "tutorial_1_1_4",[(agent_set_attack_action, "$g_talk_agent", 1),]],
##  [trp_tutorial_trainer|plyr, "tutorial_1_1_4", [], "TODO: OK.", "close_window",[]],


#old tutorial is below

##  [trp_tutorial_trainer,"start", [(eq, "$tutorial_quest_award_taken", 1),], "I think you have trained enough. Perhaps you should go to Zendar for the next step of your adventure.", "close_window",[]],
##  [trp_tutorial_trainer,"start", [(store_character_level, ":player_level", "trp_player"),(gt, ":player_level", 1)], "I think you have trained enough. Perhaps you should go to Zendar for the next step of your adventure.", "close_window",[]],
##  [trp_tutorial_trainer,"start", [(eq, "$tutorial_quest_taken", 0),], "Greetings stranger. What's your name?", "tutorial1_1",[]],
##  [trp_tutorial_trainer|plyr, "tutorial1_1", [], "Greetings sir, it's {playername}.", "tutorial1_2", []],
##  [trp_tutorial_trainer, "tutorial1_2", [], "Well {playername}, this place you see is the training ground. Locals come here to practice their combat skills. Since you are here you may have a go as well.", "tutorial1_3", []],
##  [trp_tutorial_trainer|plyr, "tutorial1_3", [], "I'd like that very much sir. Thank you.", "tutorial1_4", []],
##  [trp_tutorial_trainer, "tutorial1_4", [], "You will learn the basics of weapons and riding a horse here.\
##  First you'll begin with melee weapons. Then you'll enter an archery range to test your skills. And finally you'll see a horse waiting for you.\
##  I advise you to train in all these 3 areas. But you can skip some of them, it's up to you.", "tutorial1_6", []],
##  [trp_tutorial_trainer, "tutorial1_6", [], "Tell you what, if you destroy at least 10 dummies while training, I will give you my old knife as a reward. It's a little rusty but it's a good blade.", "tutorial1_7", []],
##  [trp_tutorial_trainer|plyr, "tutorial1_7", [], "Sounds nice, I'm ready for training.", "tutorial1_9", []],
##  [trp_tutorial_trainer, "tutorial1_9", [], "Good. Return to me when you have earned your reward.", "close_window", [(eq, "$tutorial_quest_taken", 0),
##                                                                                                                     (str_store_troop_name, 1, "trp_tutorial_trainer"),
##                                                                                                                     (str_store_party_name, 2, "p_training_ground"),
##                                                                                                                     (setup_quest_giver, "qst_destroy_dummies", "str_given_by_s1_at_s2"),
##                                                                                                                     (str_store_string, s2, "@Trainer ordered you to destroy 10 dummies in the training camp."),
##                                                                                                                     (call_script, "script_start_quest", "qst_destroy_dummies", "$g_talk_troop"),
##                                                                                                                     (assign, "$tutorial_quest_taken", 1)]],
##
##  [trp_tutorial_trainer,"start", [(eq, "$tutorial_quest_taken", 1),
##                                  (eq, "$tutorial_quest_succeeded", 1),], "Well done {playername}. Now you earned this knife. There you go.", "tutorial2_1",[]],
##  [trp_tutorial_trainer|plyr, "tutorial2_1", [], "Thank you master.", "close_window", [(call_script, "script_end_quest", "qst_destroy_dummies"),(assign, "$tutorial_quest_award_taken", 1),(add_xp_to_troop, 100, "trp_player"),(troop_add_item, "trp_player","itm_knife",imod_chipped),]],
##
##  [trp_tutorial_trainer,"start", [(eq, "$tutorial_quest_taken", 1),
##                                  (eq, "$tutorial_quest_succeeded", 1),], "Greetings {playername}. Feel free to train with the targets.", "tutorial2_1",[]],
##
##  [trp_tutorial_trainer,"start", [(eq, "$tutorial_quest_taken", 1),
##                                  (eq, "$tutorial_quest_succeeded", 0),], "I don't see 10 dummies on the floor from here. You haven't earned your reward yet.", "tutorial3_1",[]],
##  [trp_tutorial_trainer|plyr, "tutorial3_1", [], "Alright alright, I was just tired and wanted to talk to you while resting.", "tutorial3_2", []],
##  [trp_tutorial_trainer, "tutorial3_2", [], "Less talk, more work.", "close_window", []],


##  [party_tpl|pt_peasant,"start", [(eq,"$talk_context",tc_party_encounter)], "Greetings traveller.", "peasant_talk_1",[(play_sound,"snd_encounter_farmers")]],
##  [party_tpl|pt_peasant|plyr,"peasant_talk_1", [[eq,"$quest_accepted_zendar_looters"]], "Greetings to you too.", "close_window",[(assign, "$g_leave_encounter",1)]],
##  [party_tpl|pt_peasant|plyr,"peasant_talk_1", [[neq,"$quest_accepted_zendar_looters"],[eq,"$peasant_misunderstanding_said"]], "I have been charged with hunting down outlaws in this area...", "peasant_talk_2",[[assign,"$peasant_misunderstanding_said",1]]],
##  [party_tpl|pt_peasant|plyr,"peasant_talk_1", [[neq,"$quest_accepted_zendar_looters"],[neq,"$peasant_misunderstanding_said"]], "Greetings. I am hunting outlaws. Have you seen any around here?", "peasant_talk_2b",[]],
##  [party_tpl|pt_peasant,"peasant_talk_2", [], "I swear to God {sir/madam}. I am not an outlaw... I am just a simple peasant. I am taking my goods to the market, see.", "peasant_talk_3",[]],
##  [party_tpl|pt_peasant|plyr,"peasant_talk_3", [], "I was just going to ask if you saw any outlaws around here.", "peasant_talk_4",[]],
##  [party_tpl|pt_peasant,"peasant_talk_4", [], "Oh... phew... yes, outlaws are everywhere. They are making life miserable for us.\
## I pray to God you will kill them all.", "close_window",[(assign, "$g_leave_encounter",1)]],
##  [party_tpl|pt_peasant,"peasant_talk_2b", [], "Outlaws? They are everywhere. They are making life miserable for us.\
## I pray to God you will kill them all.", "close_window",[(assign, "$g_leave_encounter",1)]],

  [party_tpl|pt_manhunters,"start", [(eq,"$talk_context",tc_party_encounter)], "Hey, you there! You seen any outlaws around here?", "manhunter_talk_b",[]],
  ##Floris MTT begin
  [party_tpl|pt_manhunters_r,"start", [(eq,"$talk_context",tc_party_encounter)], "Hey, you there! You seen any outlaws around here?", "manhunter_talk_b",[]],
  [party_tpl|pt_manhunters_e,"start", [(eq,"$talk_context",tc_party_encounter)], "Hey, you there! You seen any outlaws around here?", "manhunter_talk_b",[]],
  ##Floris MTT end
  [anyone|plyr,"manhunter_talk_b", [], "Yes, they went this way about an hour ago.", "manhunter_talk_b1",[]], ##Floris MTT - was party_tpl|pt_manhunters
  [anyone,"manhunter_talk_b1", [], "I knew it! Come on, lads, lets go get these bastards! Thanks a lot, friend.", "close_window",[(assign, "$g_leave_encounter",1)]],##Floris MTT - was party_tpl|pt_manhunters
  [anyone|plyr,"manhunter_talk_b", [], "No, haven't seen any outlaws lately.", "manhunter_talk_b2",[]], ##Floris MTT - was party_tpl|pt_manhunters
  [anyone,"manhunter_talk_b2", [], "Bah. They're holed up in this country like rats, but we'll smoke them out yet. Sooner or later.", "close_window",[(assign, "$g_leave_encounter",1)]],##Floris MTT - was party_tpl|pt_manhunters

  [party_tpl|pt_looters|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker),], "{!}Warning: This line should never be displayed.", "looters_1",[
	(str_store_string, s11, "@It's your money or your life, {mate/girlie}. No sudden moves or we'll run you through."),
	(str_store_string, s12, "@Lucky for you, you caught me in a good mood. Give us all your coin and I might just let you live."),
	(str_store_string, s13, "@This a robbery, eh? I givin' you one chance to hand over everythin' you got, or me and my mates'll kill you. Understand?"),
	(store_random_in_range, ":random", 11, 14),
	(str_store_string_reg, s4, ":random"),
	(play_sound, "snd_encounter_looters")
  ]],
  
  ##Floris MTT Begin
    [party_tpl|pt_looters_r|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker),], "{!}Warning: This line should never be displayed.", "looters_1",[
	(str_store_string, s11, "@It's your money or your life, {mate/girlie}. No sudden moves or we'll run you through."),
	(str_store_string, s12, "@Lucky for you, you caught me in a good mood. Give us all your coin and I might just let you live."),
	(str_store_string, s13, "@This a robbery, eh? I givin' you one chance to hand over everythin' you got, or me and my mates'll kill you. Understand?"),
	(store_random_in_range, ":random", 11, 14),
	(str_store_string_reg, s4, ":random"),
	(play_sound, "snd_encounter_looters")
  ]],
    [party_tpl|pt_looters_e|auto_proceed,"start", [(eq,"$talk_context",tc_party_encounter),(encountered_party_is_attacker),], "{!}Warning: This line should never be displayed.", "looters_1",[
	(str_store_string, s11, "@It's your money or your life, {mate/girlie}. No sudden moves or we'll run you through."),
	(str_store_string, s12, "@Lucky for you, you caught me in a good mood. Give us all your coin and I might just let you live."),
	(str_store_string, s13, "@This a robbery, eh? I givin' you one chance to hand over everythin' you got, or me and my mates'll kill you. Understand?"),
	(store_random_in_range, ":random", 11, 14),
	(str_store_string_reg, s4, ":random"),
	(play_sound, "snd_encounter_looters")
  ]],
  ##Floris MTT end
  
  [anyone,"looters_1", [], "{s4}", "looters_2",[]], ##Floris MTT - was party_tpl|pt_looters
  [anyone|plyr,"looters_2", [[store_character_level,reg(1),"trp_player"],[lt,reg(1),4]], "I'm not afraid of you lot. Fight me if you dare!", "close_window",  ##Floris MTT - was party_tpl|pt_looters
   [[encounter_attack]]],
  [anyone|plyr,"looters_2", [[store_character_level,reg(1),"trp_player"],[ge,reg(1),4]], "You'll have nothing of mine but cold steel, scum.", "close_window", ##Floris MTT - was party_tpl|pt_looters
   [[encounter_attack]]],

  [party_tpl|pt_village_farmers,"start", [(eq,"$talk_context",tc_party_encounter),
                                          (agent_play_sound, "$g_talk_agent", "snd_encounter_farmers"),
  ],
   " My {lord/lady}, we're only poor farmers from the village of {s11}. {reg1?We are taking our products to the market at {s12}.:We are returning from the market at {s12} back to our village.}", "village_farmer_talk",
   [(party_get_slot, ":target_center", "$g_encountered_party", slot_party_ai_object),
    (party_get_slot, ":home_center", "$g_encountered_party", slot_party_home_center),
    (party_get_slot, ":market_town", ":home_center", slot_village_market_town),
    (str_store_party_name, s11, ":home_center"),
    (str_store_party_name, s12, ":market_town"),
    (assign, reg1, 1),
    (try_begin),
      (party_slot_eq, ":target_center", slot_party_type, spt_village),
      (assign, reg1, 0),
    (try_end),
    ]],
	
	##Floris MTT begin
	[party_tpl|pt_village_farmers_r,"start", [(eq,"$talk_context",tc_party_encounter),
                                          (agent_play_sound, "$g_talk_agent", "snd_encounter_farmers"),
  ],
   " My {lord/lady}, we're only poor farmers from the village of {s11}. {reg1?We are taking our products to the market at {s12}.:We are returning from the market at {s12} back to our village.}", "village_farmer_talk",
   [(party_get_slot, ":target_center", "$g_encountered_party", slot_party_ai_object),
    (party_get_slot, ":home_center", "$g_encountered_party", slot_party_home_center),
    (party_get_slot, ":market_town", ":home_center", slot_village_market_town),
    (str_store_party_name, s11, ":home_center"),
    (str_store_party_name, s12, ":market_town"),
    (assign, reg1, 1),
    (try_begin),
      (party_slot_eq, ":target_center", slot_party_type, spt_village),
      (assign, reg1, 0),
    (try_end),
    ]],
	  [party_tpl|pt_village_farmers_e,"start", [(eq,"$talk_context",tc_party_encounter),
                                          (agent_play_sound, "$g_talk_agent", "snd_encounter_farmers"),
  ],
   " My {lord/lady}, we're only poor farmers from the village of {s11}. {reg1?We are taking our products to the market at {s12}.:We are returning from the market at {s12} back to our village.}", "village_farmer_talk",
   [(party_get_slot, ":target_center", "$g_encountered_party", slot_party_ai_object),
    (party_get_slot, ":home_center", "$g_encountered_party", slot_party_home_center),
    (party_get_slot, ":market_town", ":home_center", slot_village_market_town),
    (str_store_party_name, s11, ":home_center"),
    (str_store_party_name, s12, ":market_town"),
    (assign, reg1, 1),
    (try_begin),
      (party_slot_eq, ":target_center", slot_party_type, spt_village),
      (assign, reg1, 0),
    (try_end),
    ]],
	##Floris MTT end

  [anyone|plyr,"village_farmer_talk",
  [(check_quest_active, "qst_track_down_bandits"),
   (neg|check_quest_succeeded, "qst_track_down_bandits"),
  ], "I am hunting a group of bandits with the following description... Have you seen them?", "farmer_bandit_information",[]],
  
  [anyone,"farmer_bandit_information", [
	(call_script, "script_get_manhunt_information_to_s15", "qst_track_down_bandits"),
  ], "{s15}", "village_farmer_talk",[]],
			
	
  [anyone|plyr,"village_farmer_talk", 
  [ 
    (store_faction_of_party, ":faction_of_villager", "$g_encountered_party"),
    
    (neq, ":faction_of_villager", "$players_kingdom"),
    (neq, ":faction_of_villager", "fac_player_supporters_faction"),
  ], 
  "We'll see how poor you are after I take what you've got!", "close_window",
   [(party_get_slot, ":home_center", "$g_encountered_party", slot_party_home_center),
    (party_get_slot, ":market_town", ":home_center", slot_village_market_town),
    (party_get_slot, ":village_owner", ":home_center", slot_town_lord),
    (call_script, "script_change_player_relation_with_center", ":home_center", -4),
    (call_script, "script_change_player_relation_with_center", ":market_town", -2),
    (call_script, "script_change_player_relation_with_troop", ":village_owner", -2),
	(call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$g_encountered_party"),
	
    (store_relation,":rel", "$g_encountered_party_faction","fac_player_supporters_faction"),
    (try_begin),
      (gt, ":rel", 0),
      (val_sub, ":rel", 5),
    (try_end),
    (val_sub, ":rel", 3),
    (call_script, "script_set_player_relation_with_faction", "$g_encountered_party_faction", ":rel"),
    
    (assign,"$encountered_party_hostile",1),
    (assign,"$encountered_party_friendly",0),
    ]],
  [anyone|plyr,"village_farmer_talk", [], "Carry on, then. Farewell.", "close_window",[(assign, "$g_leave_encounter",1)]],


### COMPANIONS

  [anyone,"start", [(gt,"$g_talk_troop", 0),
                    (eq, "$g_talk_troop", "$g_player_minister"),
					 ##diplomacy start+ Handle non-reflexive spouse slots (for example, for polygamy)
					 (this_or_next|neg|is_between, "$g_talk_troop", heroes_begin, heroes_end),#slot_troop_spouse may not be initialized to -1
						(neg|troop_slot_eq, "$g_talk_troop", slot_troop_spouse, "trp_player"),
					 ##diplomacy end+
					(neg|troop_slot_eq, "trp_player", slot_troop_spouse, "$g_talk_troop")],
   "I am at your service, {sire/my lady}.", "minister_issues",[]],

  [anyone,"start", [(eq,"$g_talk_troop", "trp_temporary_minister"),
                    (neq, "$g_talk_troop", "$g_player_minister")],
   "It has been an honor to serve you, {sire/my lady}.", "close_window",[]],
   
   
  [anyone,"start", [(troop_slot_eq,"$g_talk_troop", slot_troop_occupation, slto_player_companion),
                    (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                    (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
                    (ge, ":num_stacks", 1),
                    (party_stack_get_troop_id, ":castle_leader", "$g_encountered_party", 0),
                    (eq, ":castle_leader", "$g_talk_troop"),
                    (eq, "$talk_context", 0)],
   "Yes, {playername}? What can I do for you?", "member_castellan_talk",[]],
  
  [anyone,"member_castellan_pretalk", [], "Anything else?", "member_castellan_talk",[]],
  
  [anyone|plyr,"member_castellan_talk", [],
   "I want to review the castle garrison.", "member_review_castle_garrison",[]],
  [anyone,"member_review_castle_garrison", [], "Of course. Here are our lists, let me know of any changes you require...", "member_castellan_pretalk",[(change_screen_exchange_members,0)]],
  [anyone|plyr,"member_castellan_talk", [],
   "Let me see your equipment.", "member_review_castellan_equipment",[]],
  [anyone,"member_review_castellan_equipment", [], "Very well, it's all here...", "member_castellan_pretalk",[(change_screen_equip_other)]],
  [anyone|plyr,"member_castellan_talk", [],
   "I want you to abandon the castle and join my party.", "member_castellan_join",[]],
  [anyone,"member_castellan_join", [(party_can_join_party,"$g_encountered_party","p_main_party")],
   "I've grown quite fond of the place... But if it is your wish, {playername}, I'll come with you.", "close_window", [
       (assign, "$g_move_heroes", 1),
       (call_script, "script_party_add_party", "p_main_party", "$g_encountered_party"),
       (party_clear, "$g_encountered_party"),
       ]],
  [anyone,"member_castellan_join", [],
   "And where would we sleep? You're dragging a whole army with you, {playername}, there's no more room for all of us.", "member_castellan_pretalk",[]],
  
  [anyone|plyr,"member_castellan_talk", [], "[Leave]", "close_window",[]],


  [anyone,"start", [(troop_slot_eq,"$g_talk_troop", slot_troop_occupation, slto_player_companion),
                    (neg|main_party_has_troop,"$g_talk_troop"),
                    (eq, "$talk_context", tc_party_encounter)],
   "{!}Do you want me to rejoin you?", "close_window",[]], # unused
  [anyone,"start", [(neg|main_party_has_troop,"$g_talk_troop"),(eq, "$g_encountered_party", "p_four_ways_inn")], "{!}Do you want me to rejoin you?", "close_window",[]], # unused
#  [anyone,"member_separate_inn", [], "I don't know what you will do without me, but you are the boss. I'll wait for you at the Four Ways inn.", "close_window",
#  [anyone,"member_separate_inn", [], "All right then. I'll meet you at the four ways inn. Good luck.", "close_window",
#   [(remove_member_from_party,"$g_talk_troop", "p_main_party"),(add_troop_to_site, "$g_talk_troop", "scn_four_ways_inn", borcha_inn_entry)]],

#Quest heroes member chats

  [trp_kidnapped_girl,"member_chat", [], "Are we home yet?", "kidnapped_girl_chat_1",[]],
  [trp_kidnapped_girl|plyr,"kidnapped_girl_chat_1", [], "Not yet.", "kidnapped_girl_chat_2",[]],
  [trp_kidnapped_girl,"kidnapped_girl_chat_2", [], "I can't wait to get back. I've missed my family so much, I'd give anything to see them again.", "close_window",[]],

  [anyone,"member_chat",
   [
    (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
    ], "{playername}, when do you think we can reach our destination?", "member_lady_1",[]],
  [anyone|plyr, "member_lady_1", [],  "We still have a long way ahead of us.", "member_lady_2a", []],
  [anyone|plyr, "member_lady_1", [],  "Very soon. We're almost there.", "member_lady_2b", []],

  [anyone ,"member_lady_2a", [],  "Ah, I am going to enjoy the road for a while longer then. I won't complain.\
 I find riding out in the open so much more pleasant than sitting in the castle all day.\
 You know, I envy you. You can live like this all the time.", "close_window", []],
  [anyone ,"member_lady_2b", [],  "That's good news. Not that I don't like your company, but I did miss my little luxuries.\
 Still I am sorry that I'll leave you soon. You must promise me, you'll come visit me when you can.", "close_window", []],

  [anyone ,"member_chat", [(is_between, "$g_talk_troop", pretenders_begin, pretenders_end),],
   "Greetings, {playername}, my first and foremost vassal. I await your counsel.", "supported_pretender_talk", []],
  [anyone ,"supported_pretender_pretalk", [],
   "Anything else?", "supported_pretender_talk", []],

  [anyone|plyr,"supported_pretender_talk", [],
   "What do you think about our progress so far?", "pretender_progress",[]],

  [anyone,"pretender_progress", [
       (assign, reg11, 0),(assign, reg13, 0),(assign, reg14, 0),(assign, reg15, 0),
       (assign, reg21, 0),(assign, reg23, 0),(assign, reg24, 0),(assign, reg25, 0),
       
       (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
	     (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
         (store_troop_faction, ":troop_faction", ":troop_no"),
         (try_begin),
           (eq, ":troop_faction", "fac_player_supporters_faction"),
           (neq, ":troop_no", "trp_player"),
           (neq, ":troop_no", "$supported_pretender"),
           (val_add, reg11, 1),
         (else_try),
           (eq, ":troop_faction", "$supported_pretender_old_faction"),
           (neg|faction_slot_eq, "$supported_pretender_old_faction", slot_faction_leader, ":troop_no"),
           (val_add, reg21, 1),
         (try_end),
       (try_end),
       (try_for_range, ":center_no", centers_begin, centers_end),
         (store_faction_of_party, ":center_faction", ":center_no"),
         (try_begin),
           (eq, ":center_faction", "fac_player_supporters_faction"),
           (try_begin),
             (party_slot_eq, ":center_no", slot_party_type, spt_town),
             (val_add, reg13, 1),
           (else_try),
             (party_slot_eq, ":center_no", slot_party_type, spt_castle),
             (val_add, reg14, 1),
           (else_try),
             (party_slot_eq, ":center_no", slot_party_type, spt_village),
             (val_add, reg15, 1),
           (try_end),
         (else_try),
           (eq, ":center_faction", "$supported_pretender_old_faction"),
           (try_begin),
             (party_slot_eq, ":center_no", slot_party_type, spt_town),
             (val_add, reg23, 1),
           (else_try),
             (party_slot_eq, ":center_no", slot_party_type, spt_castle),
             (val_add, reg24, 1),
           (else_try),
             (party_slot_eq, ":center_no", slot_party_type, spt_village),
             (val_add, reg25, 1),
           (try_end),
         (try_end),
       (try_end),
       (store_add, reg19, reg13, reg14),
       (val_add, reg19, reg15),
       (store_add, reg29, reg23, reg24),
       (val_add, reg29, reg25),
       (store_add, ":our_score", reg13, reg14),
       (val_add, ":our_score", reg11),
       (store_add, ":their_score", reg23, reg24),
       (val_add, ":their_score", reg21),
       (store_add, ":total_score", ":our_score", ":their_score"),
       (val_mul, ":our_score", 100),
       (store_div, ":our_ratio", ":our_score", ":total_score"),
       (try_begin),
         (lt, ":our_ratio", 10),
         (str_store_string, s30, "@we have made very little progress so far"),
       (else_try),
         (lt, ":our_ratio", 30),
         (str_store_string, s30, "@we have suceeded in gaining some ground, but we still have a long way to go"),
       (else_try),
         (lt, ":our_ratio", 50),
         (str_store_string, s30, "@we have become a significant force, and we have an even chance of victory"),
       (else_try),
         (lt, ":our_ratio", 75),
         (str_store_string, s30, "@we are winning the war, but our enemies are still holding on."),
       (else_try),
         (str_store_string, s30, "@we are on the verge of victory. The remaining enemies pose no threat, but we still need to hunt them down."),
       (try_end),
       (faction_get_slot, ":enemy_king", "$supported_pretender_old_faction", slot_faction_leader),
       (str_store_troop_name, s9, ":enemy_king"),
		##diplomacy start+: Replace "lords" with "{s0}"; "no lord" with "no {s0}"; and use correct gender for enemy king
		(call_script, "script_dplmc_print_cultural_word_to_sreg", "$g_talk_troop", DPLMC_CULTURAL_TERM_LORD_PLURAL, 0),
		(call_script, "script_dplmc_store_troop_is_female", ":enemy_king"),
		],
		##OLD:
		#"{reg11?We have {reg11} lords on our side:We have no lord with us yet},\
		#whereas {reg21?{s9} still has {reg21} lords supporting him:{s9} has no loyal lords left}.\
		#{reg19?We control {reg13?{reg13} towns:} {reg14?{reg14} castles:} {reg15?and {reg15} villages:}:We don't control any settlements},\
		#while {reg29?they have {reg23?{reg23} towns:} {reg24?{reg24} castles:} {reg25?and {reg25} villages:}:they have no remaining settlements}.\
		#Overall, {s30}.", "pretender_progress_2",[]],
		##NEW:
 "{reg11?We have {reg11} {s0} on our side:We have no {s0} with us yet},\
 whereas {reg21?{s9} still has {reg21} {s0} supporting {reg0?her:him}:{s9} has no loyal {s0} left}.\
 {reg19?We control {reg13?{reg13} towns:} {reg14?{reg14} castles:} {reg15?and {reg15} villages:}:We don't control any settlements},\
 while {reg29?they have {reg23?{reg23} towns:} {reg24?{reg24} castles:} {reg25?and {reg25} villages:}:they have no remaining settlements}.\
 Overall, {s30}.", "pretender_progress_2",[]],
		##diplomacy end+

  [anyone|plyr,"pretender_progress_2", [],
   "Then, we must keep fighting and rally our supporters!", "supported_pretender_pretalk",[]],

  [anyone|plyr,"pretender_progress_2", [],
   "It seems this rebellion is not going anywhere. We must give up.", "pretender_quit_rebel_confirm",[]],
  
  [anyone,"pretender_quit_rebel_confirm", [],
   "{playername}, you can't abandon me now. Are you serious?", "pretender_quit_rebel_confirm_2",[]],
  
  [anyone|plyr,"pretender_quit_rebel_confirm_2", [],
   "Indeed, I am. I can't support you any longer.", "pretender_quit_rebel_confirm_3",[]],
  
  [anyone|plyr,"pretender_quit_rebel_confirm_2", [],
   "I was jesting. I will fight for you until we succeed.", "supported_pretender_pretalk",[]],
 
   [anyone,"pretender_quit_rebel_confirm_3", [],
   "Are you absolutely sure? I will never forgive you if you abandon my cause.", "pretender_quit_rebel_confirm_4",[]],
  
  [anyone|plyr,"pretender_quit_rebel_confirm_4", [],
   "I am sure.", "pretender_quit_rebel",[]],
  
  [anyone|plyr,"pretender_quit_rebel_confirm_4", [],
   "Let me think about this some more.", "supported_pretender_pretalk",[]],
 
  [anyone,"pretender_quit_rebel", [],
   "So be it. Then my cause is lost. There is only one thing to do for me now. I will go from Calradia and never come back. With me gone, you may try to make your peace with {s4}.", "close_window",
   [
     (troop_get_slot, ":original_faction", "$g_talk_troop", slot_troop_original_faction),
	 (faction_get_slot, ":original_faction_leader", ":original_faction", slot_faction_leader),
	 (str_store_troop_name, s4, ":original_faction_leader"),
	 
##diplomacy start+ Support promoted kingdom ladies
#(try_for_range, ":cur_troop", active_npcs_begin, active_npcs_end),##OLD
(try_for_range, ":cur_troop", heroes_begin, heroes_end),##NEW
##diplomacy end+
	   (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
	   (neq, "$supported_pretender", ":cur_troop"),
       (store_troop_faction, ":cur_faction", ":cur_troop"),
       (eq, ":cur_faction", "fac_player_supporters_faction"),
       (call_script, "script_change_troop_faction", ":cur_troop", ":original_faction"),
     (try_end),
     (troop_set_faction, "$g_talk_troop", "fac_neutral"),
     (faction_set_slot, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
     (assign, ":has_center", 0),
     (try_for_range, ":cur_center", centers_begin, centers_end),
       (store_faction_of_party, ":cur_faction", ":cur_center"),
       (eq, ":cur_faction", "fac_player_supporters_faction"),
       (assign, ":has_center", 1),
       (neg|party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
       (call_script, "script_give_center_to_lord", ":cur_center", "trp_player", 0),
     (try_end),
     (party_remove_members, "p_main_party", "$supported_pretender", 1),
     (faction_set_slot, ":original_faction", slot_faction_has_rebellion_chance, 0),
     (assign, "$supported_pretender", 0),
     (try_begin), #Still has center
       (eq, ":has_center", 1),
       (faction_set_color, "fac_player_supporters_faction", 0xFF0000),
	   (try_begin), #added to prevent no minister if player gives up rebellion
		(eq, "$g_player_minister", 0),
		(assign, "$g_player_minister", "trp_temporary_minister"),
	   (try_end), 
     (else_try), #No center
       (call_script, "script_deactivate_player_faction"),
     (try_end),
     (call_script, "script_change_player_honor", -20),
     (call_script, "script_fail_quest", "qst_rebel_against_kingdom"),
     (call_script, "script_end_quest", "qst_rebel_against_kingdom"),
    ]],


  [anyone|plyr,"supported_pretender_talk", [],
   "{reg65?My lady:My lord}, would you allow me to check out your equipment?", "supported_pretender_equip",[]],
  [anyone,"supported_pretender_equip", [], "Very well, it's all here...", "supported_pretender_pretalk",[
      (change_screen_equip_other),
      ]],

  [anyone|plyr,"supported_pretender_talk", [], "If it would please you, can you tell me about your skills?", "pretneder_view_char_requested",[]],
  [anyone,"pretneder_view_char_requested", [], "Well, all right.", "supported_pretender_pretalk",[(change_screen_view_character)]],

  
  [anyone|plyr,"supported_pretender_talk", [
	##diplomacy start+ Handle player is co-ruler of NPC kingdom
	(assign, ":alt_faction", "fac_player_supporters_faction"),
	(try_begin),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":alt_faction", "$players_kingdom"),
	(try_end),
	##diplomacy end+  
  (assign, ":center_found", 0),
  (try_for_range, ":fief_to_grant", centers_begin, centers_end),
	(store_faction_of_party, ":fief_faction", ":fief_to_grant"),
##diplomacy start+
(this_or_next|eq, ":fief_faction", ":alt_faction"),
##diplomacy end+
	(eq, ":fief_faction", "fac_player_supporters_faction"),  
	(party_slot_eq, ":fief_to_grant", slot_town_lord, -1),
    (assign, ":center_found", 1),
  (try_end),
  (eq, ":center_found", 1),
  
  ],
   "I suggest that you decide who should hold a fief that does not have a lord.", "supported_pretender_grant_fief",[]],
  
  [anyone,"supported_pretender_grant_fief", [
  ],
   "Which fief did you have in mind?", "supported_pretender_grant_fief_select",[]],

[anyone|plyr|repeat_for_parties,"supported_pretender_grant_fief_select", [
(store_repeat_object, ":fief_to_grant"),
(is_between, ":fief_to_grant", centers_begin, centers_end),
(store_faction_of_party, ":fief_faction", ":fief_to_grant"),
##diplomacy start+ Handle player is co-ruler of NPC kingdom
(assign, ":alt_faction", "fac_player_supporters_faction"),
(try_begin),
	(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
	(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
	(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
	(assign, ":alt_faction", "$players_kingdom"),
(try_end),
(this_or_next|eq, ":fief_faction", ":alt_faction"),
##diplomacy end+
(eq, ":fief_faction", "fac_player_supporters_faction"),
(party_slot_eq, ":fief_to_grant", slot_town_lord, -1),
(str_store_party_name, s4, ":fief_to_grant"),
],
"{s4}", "supported_pretender_grant_fief_choose_recipient",[
(store_repeat_object, "$g_center_taken_by_player_faction"),
]],

  [anyone,"supported_pretender_grant_fief_choose_recipient", [
  ],
   "And who should receive it?", "center_captured_rebellion",[
   (str_store_party_name, s4, "$g_center_taken_by_player_faction"),
   ]],
   
  [anyone|plyr,"supported_pretender_grant_fief_select", [
  ],
   "Never mind.", "supported_pretender_pretalk",[]],
  
  
  

  [anyone|plyr,"supported_pretender_talk", [],
   "Let us keep going, {reg65?your highness:your highness}.", "close_window",[]],


  [anyone,"do_member_trade", [], "Anything else?", "member_talk",[]],

  [anyone,"member_pretalk", [], "Anything else?", "member_talk",[]],

  
  
  
  [anyone,"member_chat", 
  [
    (store_conversation_troop,"$g_talk_troop"),
    (troop_is_hero,"$g_talk_troop"),
    (troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
    (str_store_string, s5, ":honorific"),
  ], "Yes, {s5}?", "member_talk",
  [
    (try_begin),
      (is_between, "$g_talk_troop", companions_begin, companions_end),
      (unlock_achievement, ACHIEVEMENT_TALKING_HELPS),
    (try_end),
  ]],
						  
  [anyone|plyr,"member_talk", [
	(is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
	(faction_slot_eq,  "$players_kingdom", slot_faction_marshall, "trp_player"),
  ], "As marshal, I wish you to send a message to the vassals of the realm", "member_direct_campaign",[]],


## CC
################################################################
##### Custom Commander(CC)
################################################################

  [anyone|plyr,"member_talk", [], "Let's talk about books.", "member_talk_about_books",[]],
  [anyone, "member_talk_about_books", [], "Well, what do you want to do? ", "player_talk_about_books",[]],

################################################################
##### npc_exchange_book
################################################################
  [anyone|plyr,"player_talk_about_books", [], "Let us exchange books.", "member_exchange_books",[]],
  [anyone,"member_exchange_books", [], "Very well, what kind of books do you want to exchange?", "member_exchange_books_type",[]],

  [anyone|plyr,"member_exchange_books_type", [], "Readable books.", "member_exchange_readable_books",[]],
  [anyone|plyr,"member_exchange_books_type", [], "Reference books.", "member_exchange_reference_books",[]],
  [anyone|plyr,"member_exchange_books_type", [], "Never mind.", "member_talk_about_books",[]],

  [anyone,"member_exchange_readable_books", [], "Very well, let's exchange readable books.", "member_exchange_readable_books_1",[]],
  [anyone,"member_exchange_reference_books", [], "Very well, let's exchange reference books.", "member_exchange_reference_books_1",[]],

############## exchange_readable_book   ##############
  [anyone|plyr|repeat_for_100,"member_exchange_readable_books_1",
   [
     (store_repeat_object, ":item_no"),
     (is_between, ":item_no",readable_books_begin,readable_books_end),
     (call_script, "script_get_troop_item_amount", "$g_talk_troop", ":item_no"),
     (gt, reg0, 0),
     (store_free_inventory_capacity, ":space", "trp_player"),
     (gt, ":space", 0),
     (str_store_item_name, s1, ":item_no"),
     (troop_get_type, reg1, "$g_talk_troop"),

     (try_begin),
       (store_attribute_level, ":int", "$g_talk_troop", ca_intelligence),
       (item_get_slot, ":int_req", ":item_no", slot_item_intelligence_requirement),
       (gt, ":int_req", ":int"),
       (str_store_string, s2, "@{reg1?She:He} can't read it."),
     (else_try),
       (call_script, "script_get_book_read_slot", "$g_talk_troop", ":item_no"),
       (assign, ":slot_no", reg0),
       (troop_slot_eq, "trp_book_read", ":slot_no", 1),
       
       (str_store_string, s2, "@{reg1?She:He} have already read it."),
     (else_try),
       (troop_get_slot, ":cur_read_book", "$g_talk_troop", slot_troop_current_reading_book),
       (eq, ":cur_read_book", ":item_no"),
       (call_script, "script_get_troop_item_amount", "$g_talk_troop", ":item_no"),
       (gt, reg0, 0),
       (str_store_string, s2, "@{reg1?She:He} is reading it."),
     (else_try),
       (str_store_string, s2, "@{reg1?She:He} can read it."),
     (try_end),

   ],
  "Take back {s1} ({s2}).", "member_take_back_readable_books",[(store_repeat_object, "$readable_book_to_take_back")]],

  [anyone|plyr|repeat_for_100,"member_exchange_readable_books_1",
   [
     (store_repeat_object, ":item_no"),
     (is_between, ":item_no",readable_books_begin,readable_books_end),
     (call_script, "script_get_troop_item_amount", "trp_player", ":item_no"),
     (gt, reg0, 0),
     (store_free_inventory_capacity, ":space", "$g_talk_troop"),
     (gt, ":space", 0),
     (str_store_item_name, s1, ":item_no"),
     (troop_get_type, reg1, "$g_talk_troop"),

     (try_begin),
       (store_attribute_level, ":int", "$g_talk_troop", ca_intelligence),
       (item_get_slot, ":int_req", ":item_no", slot_item_intelligence_requirement),
       (gt, ":int_req", ":int"),
       (str_store_string, s2, "@{reg1?She:He} can't read it."),
     (else_try),
       (call_script, "script_get_book_read_slot", "$g_talk_troop", ":item_no"),
       (assign, ":slot_no", reg0),
       (troop_slot_eq, "trp_book_read", ":slot_no", 1),
       (str_store_string, s2, "@{reg1?She:He} have already read it."),
     (else_try),
       (troop_get_slot, ":cur_read_book", "$g_talk_troop", slot_troop_current_reading_book),
       (eq, ":cur_read_book", ":item_no"),
       (call_script, "script_get_troop_item_amount", "$g_talk_troop", ":item_no"),
       (gt, reg0, 0),
       (str_store_string, s2, "@{reg1?She:He} is reading it."),
     (else_try),
       (str_store_string, s2, "@{reg1?She:He} can read it."),
     (try_end),

   ],
  "Give away {s1} ({s2}).", "member_give_away_readable_books",[(store_repeat_object, "$readable_book_to_give_away")]],

  [anyone|plyr,"member_exchange_readable_books_1", [],
  "Never mind.", "member_talk_about_books",[]],

  [anyone,"member_take_back_readable_books", [],
  "OK, very well.", "member_exchange_readable_books_1",
  [
    (troop_add_item,"trp_player","$readable_book_to_take_back"),
    (troop_remove_item,"$g_talk_troop","$readable_book_to_take_back"),
    ]],

  [anyone,"member_give_away_readable_books", [],
  "OK, very well.", "member_exchange_readable_books_1",
  [
    (troop_add_item,"$g_talk_troop","$readable_book_to_give_away"),
    (troop_remove_item,"trp_player","$readable_book_to_give_away"),
    ]],
############## exchange_readable_book   ##############

############## exchange_reference_book   ##############
  [anyone|plyr|repeat_for_100,"member_exchange_reference_books_1",
   [
    (store_repeat_object, ":item_no"),
     (is_between, ":item_no",reference_books_begin,reference_books_end),
     (call_script, "script_get_troop_item_amount", "$g_talk_troop", ":item_no"),
     (gt, reg0, 0),
     (store_free_inventory_capacity, ":space", "trp_player"),
     (gt, ":space", 0),
     (str_store_item_name, s1, ":item_no"),
   ],
  "Take back {s1}.", "member_take_back_reference_books",[(store_repeat_object, "$reference_book_to_take_back")]],

  [anyone|plyr|repeat_for_100,"member_exchange_reference_books_1",
   [
     (store_repeat_object, ":item_no"),
     (is_between, ":item_no",reference_books_begin,reference_books_end),
     (call_script, "script_get_troop_item_amount", "trp_player", ":item_no"),
     (gt, reg0, 0),
     (store_free_inventory_capacity, ":space", "$g_talk_troop"),
     (gt, ":space", 0),
     (str_store_item_name, s1, ":item_no"),
   ],
  "Give away {s1}.", "member_give_away_reference_books",[(store_repeat_object, "$reference_book_to_give_away")]],

  [anyone|plyr,"member_exchange_reference_books_1", [],
  "Never mind.", "member_talk_about_books",[]],

  [anyone,"member_take_back_reference_books", [],
  "OK, very well.", "member_exchange_reference_books_1",
  [
    (troop_add_item,"trp_player","$reference_book_to_take_back"),
    (troop_remove_item,"$g_talk_troop","$reference_book_to_take_back"),
    ]],

  [anyone,"member_give_away_reference_books", [],
  "OK, very well.", "member_exchange_reference_books_1",
  [
    (troop_add_item,"$g_talk_troop","$reference_book_to_give_away"),
    (troop_remove_item,"trp_player","$reference_book_to_give_away"),
    ]],
############## exchange_reference_book   ##############

################################################################
##### npc_exchange_book
################################################################

################################################################
##### npc_select_book_to_read
################################################################
  [anyone|plyr,"player_talk_about_books",
  [
     (troop_get_inventory_capacity, ":inv_cap", "$g_talk_troop"),
     (assign, ":count", 0),
     (try_for_range, ":i_slot", 0, ":inv_cap"),
       (troop_get_inventory_slot, ":cur_item", "$g_talk_troop", ":i_slot"),
       (is_between, ":cur_item", readable_books_begin, readable_books_end),
       (val_add, ":count", 1),
     (try_end),
     (gt, ":count", 0),
  ],
  "I want you to read a book which I had gave to you.", "member_read_books",[]],

  [anyone,"member_read_books", [], "Very well, which book do you want me to read? ", "member_select_read_books",[]],

  [anyone|plyr|repeat_for_100, "member_select_read_books",
  [
     (store_repeat_object, ":item_no"),
     (is_between, ":item_no", readable_books_begin, readable_books_end),
     (call_script, "script_get_troop_item_amount", "$g_talk_troop", ":item_no"),
     (gt, reg0, 0),
     (str_store_item_name, s1, ":item_no"),
  ], "{s1}.", "member_read_books_begin",[(store_repeat_object, "$readable_book_to_read")]],

  [anyone|plyr,"member_select_read_books", [], "OK.", "member_talk_about_books",[]],

  [anyone,"member_read_books_begin",
  [
     (assign, ":new_book", "$readable_book_to_read"),
     (str_store_item_name, s1, ":new_book"),
     (store_attribute_level, ":int", "$g_talk_troop", ca_intelligence),
     (item_get_slot, ":int_req", ":new_book", slot_item_intelligence_requirement),
     (gt, ":int_req", ":int"),
  ], "I am sorry that I can't read {s1}.", "member_select_read_books",[]],

  [anyone,"member_read_books_begin",
  [
     (assign, ":new_book", "$readable_book_to_read"),
     (str_store_item_name, s1, ":new_book"),
     (call_script, "script_get_book_read_slot", "$g_talk_troop", ":new_book"),
     (assign, ":slot_no", reg0),
     (troop_slot_eq, "trp_book_read", ":slot_no", 1),
  ], "I am sorry that I have already read {s1}.", "member_select_read_books",[]],

  [anyone,"member_read_books_begin",
  [
     (assign, ":new_book", "$readable_book_to_read"),
     (str_store_item_name, s1, ":new_book"),
     (call_script, "script_get_book_read_slot", "$g_talk_troop", ":new_book"),
     (assign, ":slot_no", reg0),
     (troop_slot_eq, "trp_book_read", ":slot_no", 0),
     (store_attribute_level, ":int", "$g_talk_troop", ca_intelligence),
     (item_get_slot, ":int_req", ":new_book", slot_item_intelligence_requirement),
     (le, ":int_req", ":int"),
     (troop_set_slot, "$g_talk_troop", slot_troop_current_reading_book, ":new_book"),
  ], "OK, I will read {s1} whenever I have the time.", "member_select_read_books", []],
################################################################
##### npc_select_book_to_read
################################################################

################################################################
##### npc_tell_read_books_condition
################################################################
  [anyone|plyr,"player_talk_about_books", [], "Tell me about the condition of your reading.", "member_tell_read_books_condition",[]],

  [anyone,"member_tell_read_books_condition",
  [
  (assign, ":num_books_read", 0),
  (str_store_string, s0, "@none"),
  (try_for_range, ":cur_book", readable_books_begin, readable_books_end),
    (call_script, "script_get_book_read_slot", "$g_talk_troop", ":cur_book"),
    (assign, ":slot_no", reg0),
    (troop_slot_eq, "trp_book_read", ":slot_no", 1),
    (try_begin),
      (eq, ":num_books_read", 0),
      (str_store_item_name, s0, ":cur_book"),
    (else_try),
      (eq, ":num_books_read", 1),
      (str_store_item_name, s1, ":cur_book"),
      (str_store_string, s0, "@{s1} and {s0}"),
    (else_try),
      (str_store_item_name, s1, ":cur_book"),
      (str_store_string, s0, "@{s1}, {s0}"),
    (try_end),
    (val_add, ":num_books_read", 1),
  (try_end),
  (assign, reg4, ":num_books_read"),

  (troop_get_slot, ":item_no", "$g_talk_troop", slot_troop_current_reading_book),
  (assign, reg1, ":item_no"),
  (str_store_item_name, s1, ":item_no"),
  (call_script, "script_get_troop_item_amount", "$g_talk_troop", ":item_no"),
  (try_begin),
    (eq, reg0, 0),
    (troop_set_slot, "$g_talk_troop", slot_troop_current_reading_book, 0),
    (assign, reg1, 0),
  (try_end),
  (call_script, "script_get_book_read_slot", "$g_talk_troop", ":item_no"),
  (assign, ":slot_no", reg0),
  (troop_get_slot, ":progress", "trp_book_reading_progress", ":slot_no"),
  (store_div, reg2, ":progress", 10),
  (store_mod, reg3, ":progress", 10),

  ], "{reg4?I had read these books: {s0}:I had read no books}.^{reg1?I am currently reading: {s1}, reading progress:{reg2}.{reg3}%:I am not reading any books now}.", "member_tell_read_books_condition_1", []],

  [anyone|plyr,"member_tell_read_books_condition_1", [], "OK, I have got it.", "member_talk_about_books",[]],
################################################################
##### npc_tell_read_books_condition
################################################################
  [anyone|plyr,"player_talk_about_books", [], "Never mind.", "member_chat",[]],

  [anyone|plyr,"member_talk", [],
   "I'd like to ask you something about your equipment.", "member_personal_talk",[]],
  [anyone,"member_personal_talk", [], "What do you want to do?", "member_personal_action",[]],
## transfer inventory
  [anyone|plyr,"member_personal_action", [],
   "Give me all items in your inventory.", "member_transfer_inventory",[]],
  [anyone,"member_transfer_inventory", [], "Ok, at your will.", "do_member_personal_action",[
    (call_script, "script_transfer_inventory", "$g_talk_troop", "trp_player", 0),
  ]],

  [anyone|plyr,"member_personal_action", [],
   "Let me see your equipment.", "member_equipment",[]],
  [anyone,"member_equipment", [], "Very well, it's all here...", "do_member_personal_action",[
      #(change_screen_loot),
      (change_screen_equip_other),
      ]],

  [anyone|plyr,"member_personal_action", [],
   "Let me see your inventory.", "member_inventory",[]],
  [anyone,"member_inventory", [], "Very well, it's all here...", "do_member_personal_action",[
      (change_screen_loot, "$g_talk_troop"),
      #(change_screen_equip_other),
      ]],
      
  [anyone|plyr,"member_personal_action", [], "Never mind.", "member_chat",[]],
  [anyone,"do_member_personal_action", [], "Anything else?", "member_personal_action",[]],
## CC
  [anyone,"do_member_trade", [], "Anything else?", "member_talk",[]],

  [anyone|plyr,"member_talk", [], "What can you tell me about your skills?", "view_member_char_requested",[]],
  [anyone,"view_member_char_requested", [], "All right, let me tell you...", "do_member_view_char",[(change_screen_view_character)]],

  [anyone|plyr,"member_talk", [], "We need to separate for a while.", "member_separate",[
            (call_script, "script_npc_morale", "$g_talk_troop"),
            (assign, "$npc_quit_morale", reg0),
      ]],
	  
		 ##diplomacy start+
		#Kingdom hero leaves party
		[anyone,"member_separate", [
			#Determine if g_talk_troop is an enfeoffed lord in his own right who
			#had been temporarily with the party.
			(call_script, "script_get_number_of_hero_centers", "$g_talk_troop"),
			
			(this_or_next|gt, reg0, 0),
			(this_or_next|is_between, "$g_talk_troop", lords_begin, lords_end),
			(this_or_next|is_between, "$g_talk_troop", kings_begin, kings_end),
			(this_or_next|is_between, "$g_talk_troop", pretenders_begin, pretenders_end),
			(this_or_next|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),#<- I think that would be an error, since kingdom heroes are supposed to be leading parties, but it would mean that the character is really a lord
			(this_or_next|is_between, "$g_talk_troop", lords_begin, lords_end),
				(troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_lord_rejoined),
		], "Very well, I will return to managing my own estate.", "close_window",
		[
			(troop_set_slot, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
			(remove_member_from_party, "$g_talk_troop"),
		]],
		##diplomacy end+

  [anyone,"member_separate", [
            (gt, "$npc_quit_morale", 30),
      ], "Oh really? Well, I'm not just going to wait around here. I'm going to go to the towns to look for other work. Is that what you want?", "member_separate_confirm",
   []],

  [anyone,"member_separate", [
      ], "Well, actually, there was something I needed to tell you.", "companion_quitting",
   [
        (assign, "$player_can_refuse_npc_quitting", 0),
        (assign, "$player_can_persuade_npc", 0),
       ]],


  [anyone|plyr,"member_separate_confirm", [], "That's right. We need to part ways.", "member_separate_yes",[]],
  [anyone|plyr,"member_separate_confirm", [], "No, I'd rather have you at my side.", "do_member_trade",[]],

  [anyone,"member_separate_yes", [
      ], "Well. I'll be off, then. Look me up if you need me.", "close_window",
   [
     (try_begin),
       (is_between, "$g_talk_troop", "trp_lieutenant_l14", "trp_lieutenant_l42_end"),
       (troop_set_slot, "$g_talk_troop", slot_troop_occupation, slto_inactive),
       (troop_set_slot, "$g_talk_troop", slot_troop_cur_center, -1),
       (remove_member_from_party, "$g_talk_troop"),
     (else_try),
            (troop_set_slot, "$g_talk_troop", slot_troop_occupation, 0),
            (troop_set_slot, "$g_talk_troop", slot_troop_playerparty_history, pp_history_dismissed),
            (remove_member_from_party, "$g_talk_troop"),
#LAZERAS MODIFIED  {ENTK}
            # Jrider + TITLES v 0.2, change companion title back to unattached one(s) when he/she leaves the party
            (store_troop_faction, ":faction_no", "$g_talk_troop"),
            (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", "$g_talk_troop", ":faction_no"),
            # Jrider -
#LAZERAS MODIFIED  {ENTK}
     (try_end),
       ]],



  [anyone|plyr,"member_talk", [], "I'd like to ask you something.", "member_question",[]],

  [anyone|plyr,"member_talk", [], "Never mind.", "close_window",[]],

  [anyone,"member_question", [], "Very well. What did you want to ask?", "member_question_2",[]],

  [anyone|plyr,"member_question_2", [], "How do you feel about the way things are going in this company?", "member_morale",[]],
  [anyone|plyr,"member_question_2", [
	##diplomacy start+ Prevent this from appearing for non-"companion" troops
	(is_between, "$g_talk_troop", companions_begin, companions_end),
	##diplomacy end+
	], "Tell me your story again.", "member_background_recap",[]],
  [anyone|plyr,"member_question_2", [
	##diplomacy start+ Prevent this from appearing for non-"companion" troops
	(is_between, "$g_talk_troop", companions_begin, companions_end),
	(troop_slot_ge, "$g_talk_troop", slot_troop_home, 1),
	(troop_slot_ge, "$g_talk_troop", slot_troop_home_recap, 1),
	(troop_slot_ge, "$g_talk_troop", slot_troop_backstory_b, 1),
	##diplomacy end+
	(troop_slot_eq, "$g_talk_troop", slot_troop_kingsupport_state, 0),
  ], "I suppose you know that I aspire to be {king/queen} of this land?", "member_kingsupport_1",[]],

  [anyone|plyr,"member_question_2", [
	##diplomacy start+ Prevent this from appearing for non-"companion" troops
	(is_between, "$g_talk_troop", companions_begin, companions_end),
	##diplomacy end+
  ], "Do you have any connections that we could use to our advantage?", "member_intelgathering_1",[]],
  
  [anyone|plyr,"member_question_2", [
	##diplomacy start+ Prevent this from appearing for already-enfeoffed troops
	(call_script, "script_get_number_of_hero_centers", "$g_talk_troop"),
	(eq, reg0, 0),
	(neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_lord_rejoined),
	(neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
	(neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
	(neg|is_between, "$g_talk_troop", lords_begin, lords_end),
	(neg|is_between, "$g_talk_troop", kings_begin, kings_end),
	(neg|is_between, "$g_talk_troop", pretenders_begin, pretenders_end),
	##Enable promotion when player is co-ruler
	(assign, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE - 1),
	(try_begin),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
	(try_end),
	(this_or_next|ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
	##diplomacy end+
	(faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
  ], "Would you be interested in holding a fief?", "member_fief_grant_1",[]],
  
  
  [anyone,"member_morale", [
        (call_script, "script_npc_morale", "$g_talk_troop"),
      ], "{s21}", "do_member_trade",[]],

  [anyone,"member_background_recap", [
          (troop_get_slot, ":first_met", "$g_talk_troop", slot_troop_first_encountered),
          (str_store_party_name, 20, ":first_met"),
          (troop_get_slot, ":home", "$g_talk_troop", slot_troop_home),
          (str_store_party_name, 21, ":home"),
          (troop_get_slot, ":recap", "$g_talk_troop", slot_troop_home_recap),
          (str_store_string, 5, ":recap"),
      ], "{s5}", "member_background_recap_2",[]],

  [anyone,"member_background_recap_2", [
          (str_clear, 19),
          (troop_get_slot, ":background", "$g_talk_troop", slot_troop_backstory_b),
          (str_store_string, 5, ":background"),
      ], "{s5}", "member_background_recap_3",[]],

	  [anyone,"member_background_recap_3", [
      ], "Then shortly after, I joined up with you.", "do_member_trade",[]],

  [anyone,"do_member_view_char", [], "Anything else?", "member_talk",[]],

  
  [anyone,"member_kingsupport_1", [
		 (troop_get_slot, ":morality_grievances", "$g_talk_troop", slot_troop_morality_penalties),
		 (gt, ":morality_grievances", 10),
        ], "Um... Yes. I had heard.", "do_member_trade",[]],

  [anyone,"member_kingsupport_1", [
		 (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
		 (store_add, ":string", "str_npc1_kingsupport_1", ":npc_no"),
#		 (troop_get_slot, ":string", "$g_talk_troop", slot_troop_kingsupport_string_1),
		 (str_store_string, s21, ":string"),
        ], "{s21}", "member_kingsupport_1a",[]],
  
  [anyone|plyr,"member_kingsupport_1a", [
        ], "Would you then support my cause?", "member_kingsupport_2",[]],

  [anyone|plyr,"member_kingsupport_1a", [
        ], "Very good. I shall keep that in mind.", "do_member_trade",[]],


  [anyone,"member_kingsupport_2", [
		(assign, ":companion_already_on_mission", -1),
		(try_for_range, ":companion", companions_begin, companions_end),
			(troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),
			(troop_get_slot, ":days_on_mission", ":companion", slot_troop_days_on_mission),
			(gt, ":days_on_mission", 17),
			(neg|main_party_has_troop, ":companion"),
			(assign, ":companion_already_on_mission", ":companion"),
		(try_end),

		(gt, ":companion_already_on_mission", -1),
		(troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
		(str_store_string, s21, ":honorific"),
		(str_store_troop_name, s22, ":companion_already_on_mission"),

		], "I would, {s21}. Moreover, I have a proposal on how I might help you attain your throne. But you recently sent {s22} off on a similar mission. Perhaps we should wait for a couple of weeks to avoid drawing too much attention to ourselves.", "do_member_trade",[]],

		
  [anyone,"member_kingsupport_2", [
		 (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
		 (store_add, ":string", "str_npc1_kingsupport_2", ":npc_no"),
#		 (troop_get_slot, ":string", "$g_talk_troop", slot_troop_kingsupport_string_2),
		 (str_store_string, s21, ":string"),
        ], "{s21}", "member_kingsupport_2a",[]],
  
  [anyone|plyr,"member_kingsupport_2a", [
		 (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
		 (store_add, ":string", "str_npc1_kingsupport_2a", ":npc_no"),
#  		 (troop_get_slot, ":string", "$g_talk_troop", slot_troop_kingsupport_string_2a),
		 (str_store_string, s21, ":string"),
        ], "{s21}", "member_kingsupport_3",[]],

  [anyone|plyr,"member_kingsupport_2a", [
		 (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
		 (store_add, ":string", "str_npc1_kingsupport_2b", ":npc_no"),
#    	 (troop_get_slot, ":string", "$g_talk_troop", slot_troop_kingsupport_string_2b),
		 (str_store_string, s21, ":string"),

        ], "{s21}", "do_member_trade",[]],

  [anyone,"member_kingsupport_3", [
		 (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
		 (store_add, ":string", "str_npc1_kingsupport_3", ":npc_no"),
#		 (troop_get_slot, ":string", "$g_talk_troop", slot_troop_kingsupport_string_3),
		 (str_store_string, s21, ":string"),
        ], "{s21}", "member_kingsupport_3a",[]],


  [anyone|plyr,"member_kingsupport_3a", [
        ], "Very good. You do that", "member_kingsupport_4",[
		]],

  [anyone|plyr,"member_kingsupport_3a", [
        ], "On second thought, stay with me for a while", "do_member_trade",[]],

  [anyone,"member_kingsupport_4", [
  		 (troop_set_slot, "$g_talk_troop", slot_troop_days_on_mission, 21),
  		 (troop_set_slot, "$g_talk_troop", slot_troop_current_mission, npc_mission_kingsupport),

		 (remove_member_from_party, "$g_talk_troop", "p_main_party"),
		 		 
		 (troop_get_slot, ":string", "$g_talk_troop", slot_troop_honorific),
		 (str_store_string, s21, ":string"),

		 ], "Farewell then, {s21}, for a little while", "close_window",[]],

  [anyone,"member_intelgathering_1", [
		 (troop_get_slot, ":town_with_contacts", "$g_talk_troop", slot_troop_town_with_contacts),
		 (str_store_party_name, s17, ":town_with_contacts"),
		 (store_faction_of_party, ":contact_town_faction", ":town_with_contacts"),
		 (str_store_faction_name, s18, ":contact_town_faction"),
		 
		 (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
		 (store_add, ":connections_string", "str_npc1_intel_mission", ":npc_no"),
		 (str_store_string, s21, ":connections_string"),
		 ], "{s21}", "member_intelgathering_3",[]],
		
  [anyone,"member_intelgathering_3", [ #change back to member_intelgathering_2 if this will be used
		(eq, 1, 0),
  ], "Of course, as few people should know of this as possible. If you want to collect the information, or pull me out, then don't send a messenger. Come and get me yourself -- even if that means you have to sneak through the gates.", "member_intelgathering_3",[]],
		
  [anyone|plyr,"member_intelgathering_3", [
		 ], "Splendid idea -- you do that.", "member_intelgathering_4",[]],
		
  [anyone|plyr,"member_intelgathering_3", [
		 ], "Actually, hold off for now.", "do_member_trade",[]],

  [anyone,"member_intelgathering_4", [
  		 (troop_set_slot, "$g_talk_troop", slot_troop_days_on_mission, 5),
  		 (troop_set_slot, "$g_talk_troop", slot_troop_current_mission, npc_mission_gather_intel),
		 
		 (remove_member_from_party, "$g_talk_troop", "p_main_party"),
		 		 
		 (troop_get_slot, ":string", "$g_talk_troop", slot_troop_honorific),
		 (str_store_string, s21, ":string"),

		 ], "Good. I should be ready to report in about five days. Farewell then, {s21}, for a little while.", "close_window",[]],
		 
		 
		 
[anyone|auto_proceed, "start", 
  [  
    (is_between, "$g_talk_troop", "trp_swadian_merchant", "trp_startup_merchants_end"),
    (eq, "$talk_context", tc_town_talk),    
  ],  
  "{!}.", "merchant_quest_4_start", 
  [
  ]],
  
[anyone, "merchant_quest_4_start", 
  [
  ],  
  "It's time, lads! Up and at them!", "close_window", 
  [
    (try_for_agents, ":agent_no"),
  	  (agent_get_troop_id, ":agent_troop_id", ":agent_no"),
	  ##Floris MTT Begin
  	  #(ge, ":agent_troop_id", "trp_bandit_e_looter"),
  	  #(le, ":agent_troop_id", "trp_bandit_e_desert"),
	  (try_begin),
		(eq, "$troop_trees", troop_trees_0),
		(assign, ":outlaws_begin", outlaws_troops_begin),
		(assign, ":outlaws_end", outlaws_troops_end),
	  (else_try),
		(eq, "$troop_trees", troop_trees_1),
		(assign, ":outlaws_begin", outlaws_troops_r_begin),
		(assign, ":outlaws_end", outlaws_troops_r_end),
	  (else_try),
		(eq, "$troop_trees", troop_trees_2),
		(assign, ":outlaws_begin", outlaws_troops_e_begin),
		(assign, ":outlaws_end", outlaws_troops_e_end),
	  (try_end),
	  (is_between, ":agent_troop_id", ":outlaws_begin", ":outlaws_end"),
	  ##Floris MTT end
  	  (agent_set_team, ":agent_no", 1),
  	(try_end),      

    (get_player_agent_no, ":player_agent"),

    (assign, ":minimum_distance", 1000),
    (try_for_agents, ":agent_id_1"),
      (neq, ":agent_id_1", ":player_agent"),
      (agent_get_team, ":agent_team_1", ":agent_id_1"),
      (eq, ":agent_team_1", 0),
      (agent_get_position, pos0, ":agent_id_1"),
      
      (try_for_agents, ":agent_id_2"),
        (agent_get_team, ":agent_team_2", ":agent_id_2"),
        (eq, ":agent_team_2", 1),
        (agent_get_position, pos1, ":agent_id_2"),
        
        (get_distance_between_positions, ":dist", pos0, pos1),
        
        (le, ":dist", ":minimum_distance"),
        (assign, ":minimum_distance", ":dist"),
        (copy_position, pos2, pos1),
      (try_end),	
			
      (agent_set_scripted_destination, ":agent_id_1", pos2, 0),
      (agent_set_speed_limit, ":agent_id_1", 10),
    (try_end),
  ]],

[anyone, "start", 
  [
    (is_between, "$g_talk_troop", "trp_relative_of_merchant", "trp_relative_of_merchants_end"),
    
    (try_begin),
      (check_quest_active, "qst_save_relative_of_merchant"),
      (call_script, "script_succeed_quest", "qst_save_relative_of_merchant"),      
    (try_end),  
    
    (str_store_party_name, s9, "$g_starting_town"),
    
    (assign, "$relative_of_merchant_is_found", 1),
  ],  
  "Thank you! Thank you, {sir/my lady}, for rescuing me from those fiends. Did my brother in {s9} put you onto their track?", "relative_saved_1a", 
  [
  ]],
  
[anyone|plyr, "relative_saved_1a", 
  [],  
  "Yes. I told him that I would find you. I advise you to return to your family as quickly as you can -- and be careful on the road.", "close_window", 
  [    
  ]],


  
[anyone, "start", 
  [
    (is_between, "$g_talk_troop", "trp_sea_raider_leader", "trp_bandit_leaders_end"),
    (eq,"$talk_context",tc_hero_defeated),
  ],  
  "Ay! Spare me! Spare my life! Let me go, and I'll go far away from here, and learn an honest trade, and you'll never hear of me again!", "bandit_leader_1a", 
  []],

[anyone|plyr, "bandit_leader_1a", 
  [
    (is_between, "$g_talk_troop", "trp_sea_raider_leader", "trp_bandit_leaders_end"),
  ],  
  "I'll spare your life -- but in exchange, I want information. Either you or your mates kidnapped the brother of a prominent merchant in town. Tell me where you're hiding him, and give me your word that you'll stop troubling the people of these parts, and you can go free.", "bandit_leader_1b", 
  []],





[anyone,"start", 
  [
    (eq,"$talk_context",tc_party_encounter),
    (is_between, "$g_talk_troop", "trp_sea_raider_leader", "trp_bandit_leaders_end"),
  ],
   "What do you want?", "looter_leader_1",
   []],

[anyone|plyr,"looter_leader_1", 
  [
    (store_faction_of_party, ":starting_town_faction", "$g_starting_town"),    
    (try_begin),
      (eq, ":starting_town_faction", "fac_kingdom_1"),
      (assign, ":troop_of_merchant", "trp_swadian_merchant"),
    (else_try),  
      (eq, ":starting_town_faction", "fac_kingdom_2"),
      (assign, ":troop_of_merchant", "trp_vaegir_merchant"),
    (else_try),                   
      (eq, ":starting_town_faction", "fac_kingdom_3"),
      (assign, ":troop_of_merchant", "trp_khergit_merchant"),
    (else_try),  
      (eq, ":starting_town_faction", "fac_kingdom_4"),
      (assign, ":troop_of_merchant", "trp_nord_merchant"),
    (else_try),  
      (eq, ":starting_town_faction", "fac_kingdom_5"),
      (assign, ":troop_of_merchant", "trp_rhodok_merchant"),
    (else_try),  
      (eq, ":starting_town_faction", "fac_kingdom_6"),
      (assign, ":troop_of_merchant", "trp_sarranid_merchant"),
    (try_end),
    
    (str_store_troop_name, s9, ":troop_of_merchant"),
  ],
   "I've been looking for you. Tell me where you keep your prisoners, and I'll let you go.", "looter_leader_2", 
  []],

[anyone|plyr,"looter_leader_1", 
  [],
   "Nothing. We'll leave you in peace.", "close_window", 
   [
     (assign, "$g_leave_encounter", 1),     
   ]],

[anyone,"looter_leader_2", 
  [],
   "Hah! Those prisoners are only going free if you pay their ransom. Did you bring any silver?", "looter_leader_3", 
   []],

[anyone|plyr,"looter_leader_3", 
  [],
   "No, but I brought steel.", "close_window", 
   []],



[anyone, "bandit_leader_1b", 
  [
    (is_between, "$g_talk_troop", "trp_sea_raider_leader", "trp_bandit_leaders_end"),

    (assign, ":possible_villages", 0),
    (try_for_range, ":village_no", villages_begin, villages_end),
      (party_slot_eq, ":village_no", slot_village_bound_center, "$g_starting_town"),      
      (val_add, ":possible_villages", 1),
    (try_end),
    
    (store_random_in_range, ":random_village", 0, ":possible_villages"),
    (val_add, ":random_village", 1),
      
    (try_for_range, ":village_no", villages_begin, villages_end),
      (party_slot_eq, ":village_no", slot_village_bound_center, "$g_starting_town"),      
      (val_sub, ":random_village", 1),
      (eq, ":random_village", 0),
      (assign, "$lair_neighboor_village", ":village_no"),
    (try_end), 
       
    (str_store_party_name_link, s9, "$lair_neighboor_village"),   

    (set_spawn_radius, 4),
		##Floris MTT begin
		(try_begin),
			(eq, "$troop_trees", troop_trees_0),
			(spawn_around_party, "$lair_neighboor_village", "pt_looter_lair"),
		(else_try),
			(eq, "$troop_trees", troop_trees_1),
			(spawn_around_party, "$lair_neighboor_village", "pt_looter_lair_r"),
		(else_try),
			(eq, "$troop_trees", troop_trees_2),
			(spawn_around_party, "$lair_neighboor_village", "pt_looter_lair_e"),
		(try_end),
		##Floris MTT end
   	(party_set_slot, reg0, slot_party_type, spt_bandit_lair), ##Floris MTT - needed for "script_game_event_party_encounter"
	(party_set_flags, reg0, pf_always_visible, 1),
  ],  
  "Oh bless you, {sir/my lady}. Bless you. We've done the lad no harm. We've been keeping him in our hideout near {s9}. I'll describe the area nearby in detail, so there's no mistaking it...", "close_window", 
  [
    (call_script, "script_succeed_quest", "qst_learn_where_merchant_brother_is"),
    (call_script, "script_end_quest", "qst_learn_where_merchant_brother_is"),
    
    (store_faction_of_party, ":starting_town_faction", "$g_starting_town"),    
    (try_begin),
      (eq, ":starting_town_faction", "fac_kingdom_1"),
      (assign, ":troop_of_merchant", "trp_swadian_merchant"),
    (else_try),  
      (eq, ":starting_town_faction", "fac_kingdom_2"),
      (assign, ":troop_of_merchant", "trp_vaegir_merchant"),
    (else_try),                   
      (eq, ":starting_town_faction", "fac_kingdom_3"),
      (assign, ":troop_of_merchant", "trp_khergit_merchant"),
    (else_try),  
      (eq, ":starting_town_faction", "fac_kingdom_4"),
      (assign, ":troop_of_merchant", "trp_nord_merchant"),
    (else_try),  
      (eq, ":starting_town_faction", "fac_kingdom_5"),
      (assign, ":troop_of_merchant", "trp_rhodok_merchant"),
    (else_try),  
      (eq, ":starting_town_faction", "fac_kingdom_6"),
      (assign, ":troop_of_merchant", "trp_sarranid_merchant"),
    (try_end),
    (str_store_troop_name, s10, ":troop_of_merchant"),
	
    (str_store_string, s2, "str_find_the_lair_near_s9_and_free_the_brother_of_the_prominent_s10_merchant"),            
    (call_script, "script_start_quest", "qst_save_relative_of_merchant", ":troop_of_merchant"),
  ]],




  [anyone,"start", [        
    (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
    (check_quest_active, "qst_rescue_prisoner"),
    (check_quest_succeeded, "qst_rescue_prisoner"),
    (quest_slot_eq, "qst_rescue_prisoner", slot_quest_giver_troop, "$g_talk_troop"),
	(quest_get_slot, ":cur_lord", "qst_rescue_prisoner", slot_quest_target_troop), 
    (call_script, "script_troop_get_family_relation_to_troop", ":cur_lord", "$g_talk_troop"),
    ],
	##diplomacy start+ Use correct pronoun (family relation script wrote gender to reg4)
 "{playername}, you saved {reg4?her:him}! Thank you ever so much for rescuing my {s11}.\
 Please, take this as some small repayment for your noble deed.", "rescue_prisoner_succeed_2",
	##diplomacy end+
   [   
     (call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 8),
     (add_xp_as_reward, 2000),
     (call_script, "script_troop_add_gold", "trp_player", 1500),
     (call_script, "script_end_quest", "qst_rescue_prisoner"),
     ]],#rescuerescue               
   [anyone|plyr,"rescue_prisoner_succeed_2", [], "Always an honour to serve, {s65}.", "lord_pretalk",[]],     



  #Quest 0 - Alley talk
  [anyone|auto_proceed, "start", 
  [
    (is_between, "$g_talk_troop", "trp_swadian_merchant", "trp_startup_merchants_end"),
    (eq, "$talk_context", tc_back_alley),
    (eq, "$talked_with_merchant", 0),    
  ],  
  "{!}.", "start_up_quest_1_next", 
  []],

  [anyone, "start_up_quest_1_next", 
  [],  
  "Are you all right? Well.... I guess you're alive, at any rate. I'm not sure that we can say the same for the other fellow. That's one less thief to trouble our streets at night, although Heaven knows he won't be the last.... Anyway, maybe you can help me with something. Let's talk more inside. Out here, we don't know who's listening", "close_window", 
  [    
    (assign, "$talked_with_merchant", 1),
    (mission_disable_talk),
  ]],


  #Quest 1 - Repeating dialog sentence
  [anyone|auto_proceed, "start", 
  [
    (is_between, "$g_talk_troop", "trp_swadian_merchant", "trp_startup_merchants_end"),
    (eq, "$talk_context", tc_tavern_talk),
    
    (call_script, "script_party_count_members_with_full_health", "p_main_party"),
    (assign, ":total_party_size", reg0),

    (assign, ":continue", 0),
    (try_begin),
      (check_quest_active, "qst_collect_men"),
      (neg|check_quest_succeeded, "qst_collect_men"),        

      (lt, ":total_party_size", 5),
      
      (try_begin),
        (le, ":total_party_size", 1),
        (str_store_string, s11, "str_please_sir_my_lady_go_find_some_volunteers_i_do_not_know_how_much_time_we_have"),
      (else_try),  
        (str_store_string, s11, "str_you_need_more_men_sir_my_lady"),
      (try_end),  
      (assign, ":continue", 1),
    (else_try),  
      (check_quest_active, "qst_learn_where_merchant_brother_is"),
      (neg|check_quest_succeeded, "qst_learn_where_merchant_brother_is"),              
      (str_store_string, s11, "str_do_not_waste_time_go_and_learn_where_my_brother_is"),
      (assign, ":continue", 1),
    (try_end),      
    (eq, ":continue", 1),
  ],  
  "{!}.", "start_up_quest_2_next", 
  []],
  
  [anyone, "start_up_quest_2_next", 
  [],
  "{!}{s11}", "close_window", 
  []],

  #Quest 2 - First dialog sentence
  [anyone, "start", 
  [
    (is_between, "$g_talk_troop", "trp_swadian_merchant", "trp_startup_merchants_end"),
    (eq, "$talk_context", tc_tavern_talk),
    
    (check_quest_active, "qst_collect_men"),
    (neg|check_quest_succeeded, "qst_duel_for_lady"),
    (call_script, "script_party_count_members_with_full_health", "p_main_party"),
    (ge, reg0, 5),
    
    (str_store_party_name, s9, "$current_town"),
  ],
  "Splendid work. You have hired enough men to take on the bandits. Now -- travellers entering {s9} have told us that there is a small group of robbers lurking on the outside of town. I suspect that they are all from the same band, the one that took my brother. Hunt them down and defeat them, and make them disclose the location of their lair!", "merchant_quest_2a", 
  [    
    (call_script, "script_succeed_quest", "qst_collect_men"),          
    (call_script, "script_end_quest", "qst_collect_men"),
  ]],

  #Quest 3 - First dialog sentence/Repeating dialog sentence
  [anyone, "start", 
  [
    (is_between, "$g_talk_troop", "trp_swadian_merchant", "trp_startup_merchants_end"),
    (eq, "$talk_context", tc_tavern_talk),
        
    (check_quest_active, "qst_save_relative_of_merchant"),
    (neg|check_quest_succeeded, "qst_save_relative_of_merchant"),
        
    (str_store_party_name, s9, "$current_town"),
  ],
  "So, you've found out where they hid my brother? Splendid work. I flatter myself that I'm a fine judge of character, and you look to be a {man/woman} who can get things done. Now, go out and save his unworthy hide!", "merchant_quest_3a", 
  [    
  ]],

  #Quest 3 - All succeeded - First dialog sentence
  [anyone, "start", 
  [
    (is_between, "$g_talk_troop", "trp_swadian_merchant", "trp_startup_merchants_end"),
    (eq, "$talk_context", tc_tavern_talk),
        
    (check_quest_active, "qst_save_relative_of_merchant"),
    (check_quest_succeeded, "qst_save_relative_of_merchant"),
  ],
  "Well... My brother is home safe. I'm not sure what to do with him -- maybe pack him off to a university outside Calradia. That way, if he gets knocked on the head in a street brawl, no one can say it's my fault. But that's not your problem. Here's the rest of your reward. It was well-earned.", "merchant_quest_3b", 
  [    
    (call_script, "script_finish_quest", "qst_save_relative_of_merchant", 100),
    (troop_add_gold, "trp_player", 200),
  ]],

  [anyone|plyr, "merchant_quest_3b", #was startup
  [
  ],
  "The money is most welcome, and I am glad to have been of service", "merchant_quest_4a", 
  [  
  ]],

  [anyone, "merchant_quest_4a", #was startup
  [
  ],
  "Good! Now... Are you interested in making some more?", "merchant_quest_4b", 
  [  
  ]],

  [anyone|plyr, "merchant_quest_4b",
  [
  ],
  "Possibly. What do you need?", "merchant_quest_4b1", 
  [  
  ]],
  
  
  [anyone, "merchant_quest_4b1", 
  [],
  "Remember how I told you that the bandits had an ally inside the walls? I think I know who it is -- the captain of the watch, no less. Some months ago this captain, seeing the amount of profit we merchants were making from trade across the frontiers, decided to borrow some money to sponsor a caravan. Unfortunately, like many who are new to commerce, he failed to realize that great profit only comes with great risk. So he sank all his money into the most expensive commodities, and of course his caravan was captured and looted, and he lost everything.", "merchant_quest_4b2", 
  []],
  
  [anyone, "merchant_quest_4b2", 
  [],
  "As a consequence, it seems, our captain turned to villainy to recoup his fortune. I supposed I'd do the same if, the Heavens forbid, I ever faced indebtedness and ruination. Now, any watch captain worth his salary will have a few thieves and robbers on his payroll, to inform on the rest, but our captain decides to employ these bastards wholesale. He brings them into the town, lets them do as they will, and takes a share of their take. You've heard of poachers turning gamekeepers? Well, in the unfortunate land of Calradia, sometimes gamekeepers will turn poacher. Luckily, there's are still a few brave, honest souls in the watch who've told me how he works.", "merchant_quest_4b3", 
  []],

  [anyone, "merchant_quest_4b3", 
  [
  (faction_get_slot, ":local_ruler", "$g_encountered_party_faction", slot_faction_leader),
  (str_store_troop_name, s4, ":local_ruler"),
	##diplomacy start+ Gender-correct, and replace "king" with "{s0}"
	(call_script, "script_dplmc_store_troop_is_female_reg", ":local_ruler", 4),
	(call_script, "script_dplmc_print_cultural_word_to_sreg", ":local_ruler", DPLMC_CULTURAL_TERM_KING, 0),
	],
	#"Now -- here's my plan. I could bring this to the attention of {s4}, lord of the city, but that would mean an inquiry, my word against the captain's, and witnesses can be bought and evidence destroyed, or maybe the whole thing will be forgotten if the enemy comes across the border again, and all I'll get for my trouble is a knife in the ribs. In time of war, you see, a king's eye wanders far from his domain, and his subjects suffer. So I've got another idea. I've got a small group of townsfolk together, some men in my employ and some others who've lost relatives to these bandits, and we'll storm the captain's home and bring him in chains before {s4}, hopefully with a few captured bandits to explain how things stack up.", "merchant_quest_4b4",
 "Now -- here's my plan. I could bring this to the attention of {s4}, lord of the city, but that would mean an inquiry, my word against the captain's, and witnesses can be bought and evidence destroyed, or maybe the whole thing will be forgotten if the enemy comes across the border again, and all I'll get for my trouble is a knife in the ribs. In time of war, you see, a {s0}'s eye wanders far from {reg4?her:his} domain, and {reg4?her:his} subjects suffer. So I've got another idea. I've got a small group of townsfolk together, some men in my employ and some others who've lost relatives to these bandits, and we'll storm the captain's home and bring him in chains before {s4}, hopefully with a few captured bandits to explain how things stack up.", "merchant_quest_4b4",
	[]],
	##diplomacy end+

  [anyone, "merchant_quest_4b4", 
  [
  ],
  "All I need now is someone to lead my little army into battle -- and I can't think of anyone better than you. So, what do you say?", "merchant_quest_4b5", 
  [ 
  ]],

   [anyone|plyr, "merchant_quest_4b5", 
  [
  ],
  "How do I know that you're telling me the truth?", "merchant_quest_4b6", 
  [ 
  ]], 
  
   [anyone, "merchant_quest_4b6", 
  [
  (str_store_party_name, s4, "$g_encountered_party"),
  ],
  "Oh, well, I suppose it's possible that I found a dozen bandits who were willing to give their lives to give a passing stranger a false impression of life in old {s4}... Well, I guess you can't really know if my word is good, but I reckon you've learned by now that my money is good, and there's another 100 denars, or maybe a bit more, that's waiting for you if you'll do me this last little favor. So what do you say?", "merchant_quest_4b7", 
  [ 
  ]], 
  
  
  [anyone|plyr, "merchant_quest_4b7", 
  [
  ],
  "All right. I'll lead your men.", "merchant_quest_4b8", 
  [ 
  ]],
  
  [anyone|plyr, "merchant_quest_4b7", 
  [
  ],
  "I'm sorry. This is too much, too fast. I need time to think.", "merchant_quest_4_decline", 
  [  
  ]],

  [anyone, "merchant_quest_4b8", 
  [
  ],
  "Splendid. It's been a long time since I staked so much on a single throw of the dice, and frankly I find it exhilarating. My men are ready to move on your word. Are you ready?", "merchant_quest_4b9", 
  [  
  ]],
 
  [anyone|plyr, "merchant_quest_4b9", 
  [
  ],
  "Yes. Give them the sign.", "merchant_quest_4_accept", 
  [  
  ]],
  
  [anyone|plyr, "merchant_quest_4b9", 
  [
  ],
  "Not now. I will need to rest before I can fight again.", "merchant_quest_4_decline", 
  [  
  ]],

  [anyone, "merchant_quest_4_accept", 
  [
  ],
  "Good! Now -- strike hard, strike fast, and the captain and his henchmen won't know what hit them. May the heavens be with you!", "close_window", 
  [            
    (assign, "$current_startup_quest_phase", 3),
    (jump_to_menu, "mnu_start_phase_3"),
    (finish_mission),
  ]],
 
  [anyone, "merchant_quest_4_decline", #was startup
  [
  ],
  "Right. I can keep my men standing by. If you let this go too long, then I suppose that I shall have to finish this affair without you, but I would be most pleased if you could be part of it as well. For now, take what time you need.", "close_window", 
  []],
  
  
  
  #QUEST 2 - Learning where prominent's brother is.
  [anyone|plyr, "merchant_quest_2a", 
  [
  ],
  "Very well. I shall hunt for bandits.", "close_window", 
  [  
    (str_store_party_name, s9, "$current_town"),
    (str_store_string, s2, "str_start_up_quest_message_2"),
    (call_script, "script_start_quest", "qst_learn_where_merchant_brother_is", "$g_talk_troop"),    
        
    (set_spawn_radius, 2),
		##Floris MTT begin
		(try_begin),
			(eq, "$troop_trees", troop_trees_0),
			(spawn_around_party, "$current_town", "pt_leaded_looters"),
		(else_try),
			(eq, "$troop_trees", troop_trees_1),
			(spawn_around_party, "$current_town", "pt_leaded_looters_r"),
		(else_try),
			(eq, "$troop_trees", troop_trees_2),
			(spawn_around_party, "$current_town", "pt_leaded_looters_e"),
		(try_end),
		##Floris MTT end
    (assign, ":spawned_bandits", reg0),    
    
    (party_get_position, pos0, "$current_town"),    
    (party_set_ai_behavior, ":spawned_bandits", ai_bhvr_patrol_location),
    (party_set_ai_patrol_radius, ":spawned_bandits", 3),
    (party_set_ai_target_position, ":spawned_bandits", pos0),                                                         
  ]],
  
  [anyone|plyr, "merchant_quest_2a", 
  [
  ],
  "Why don't you come with us?", "merchant_quest_2a_whynotcome", 
  [  
  ]],
  
  [anyone, "merchant_quest_2a_whynotcome", 
  [
  ],
  "Because I'm paying you to go take care of it. That's the short answer. The long answer is that I've got some leads to follow up here in town, and I have just as much chance of getting knocked on my head as you, if that's what you're asking. But I respect your question. Now, what do you say?", "merchant_quest_2a", 
  [  
  ]],
  
  
  [anyone|plyr, "merchant_quest_2a", 
  [
  ],
  "I cannot deal with this matter at this time.", "close_window", 
  [  
  ]],

  #Quest 3 - Saving merchant's brother.
  [anyone|plyr, "merchant_quest_3a", 
  [
  ],
  "Very well. I go now to attack the bandits in their lair, and find your brother.", "close_window", 
  [    
    #no need to below three lines anymore, this quest is auto starting after player learn where bandits are hiding merchant's brother.
    #(str_store_party_name, s9, "$lair_neighboor_village"),    
    #(str_store_string, s2, "str_start_up_quest_message_3"),
    #(call_script, "script_start_quest", "qst_save_relative_of_merchant", "$g_talk_troop"),    
  ]],


  
  
  
  [anyone|plyr, "merchant_quest_3a", 
  [
  ],
  "I cannot deal with this matter at this time.", "close_window", 
  [  
    #think about placing end_quest here. Because it is auto-starting. If player do not want this quest he/she should have a way to avoid it.
  ]],


  [anyone, "start", 
  [
    (is_between, "$g_talk_troop", "trp_swadian_merchant", "trp_startup_merchants_end"),
    
    (this_or_next|eq, "$talk_context", tc_tavern_talk),
    (neq, "$dialog_with_merchant_ended", 0), 
    
    (assign, ":continue", 0),
    (try_begin),
      (neg|check_quest_succeeded, "qst_collect_men"),
      (neg|check_quest_active, "qst_collect_men"),
      (assign, ":continue", 1),
    (else_try),  
      (neg|check_quest_active, "qst_collect_men"),
      (neg|check_quest_succeeded, "qst_learn_where_merchant_brother_is"),
      (neg|check_quest_active, "qst_learn_where_merchant_brother_is"),
      (assign, ":continue", 1),
    (else_try),  
      (neg|check_quest_active, "qst_collect_men"),
      (neg|check_quest_active, "qst_learn_where_merchant_brother_is"),
      (neg|check_quest_succeeded, "qst_save_relative_of_merchant"),
      (neg|check_quest_active, "qst_save_relative_of_merchant"),
      (assign, ":continue", 1),
    (try_end),  
    
    (eq, ":continue", 1),
  ],
	##diplomacy start+ replaced "a rich men" with "a rich {reg65?woman:man}"
	#"You may do as you wish, {sir/my lady}, but I am disappointed. You would do well to reconsider. I am a rich men, and would show you my gratitude in coin.", "merchant_quest_persuasion",
 "You may do as you wish, {sir/my lady}, but I am disappointed. You would do well to reconsider. I am a rich {reg65?woman:man}, and would show you my gratitude in coin.", "merchant_quest_persuasion",
	##diplomacy end+
  [        
  ]],

  [anyone|auto_proceed, "start", 
  [
    (is_between, "$g_talk_troop", "trp_swadian_merchant", "trp_startup_merchants_end"),
    
    (this_or_next|eq, "$talk_context", tc_tavern_talk),
    (neq, "$dialog_with_merchant_ended", 0), 

    (check_quest_finished, "qst_save_relative_of_merchant"),
    (neg|check_quest_succeeded, "qst_save_town_from_bandits"),
    (neg|check_quest_active, "qst_save_town_from_bandits"),
  ],
  "{!}.", "merchant_quest_4b4",
  [        
  ]],

  [anyone|plyr, "merchant_quest_persuasion", 
  [
    (neg|check_quest_finished, "qst_collect_men"),
    (neg|check_quest_active, "qst_collect_men"),
  ],
  "You make a persuasive case. I will help you.", "merchant_quest_1_prologue_3", 
  [  
  ]],

  [anyone|plyr, "merchant_quest_persuasion", 
  [
    (check_quest_finished, "qst_collect_men"),
    (neg|check_quest_finished, "qst_learn_where_merchant_brother_is"),
    (neg|check_quest_active, "qst_learn_where_merchant_brother_is"),
  ],
  "You make a persuasive case. I will help you.", "merchant_quest_2", 
  [  
  ]],

  [anyone|plyr, "merchant_quest_persuasion", 
  [
    (check_quest_finished, "qst_collect_men"),
    (check_quest_finished, "qst_learn_where_merchant_brother_is"),
    (neg|check_quest_finished, "qst_save_relative_of_merchant"),
    (neg|check_quest_active, "qst_save_relative_of_merchant"),
  ],
  "You make a persuasive case. I will help you.", "merchant_quest_3", 
  [  
  ]],

  [anyone|plyr, "merchant_quest_persuasion", 
  [
    (check_quest_finished, "qst_collect_men"),
    (check_quest_finished, "qst_learn_where_merchant_brother_is"),
    (check_quest_finished, "qst_save_relative_of_merchant"),
    (neg|check_quest_finished, "qst_save_town_from_bandits"),
    (neg|check_quest_active, "qst_save_town_from_bandits"),
  ],
  "You make a persuasive case. I will help you.", "merchant_quest_4b8", 
  [  
  ]],

  [anyone|plyr, "merchant_quest_persuasion", 
  [
  ],
  "As I say, I have more important business elsewhere.", "close_window", 
  [  
  ]],

##diplomacy start+ Allow skipping the tutorial.
[anyone|plyr,"merchant_quest_persuasion",
[
(ge, "$cheat_mode", 1),
],
"{!}[CHEAT] I have played this before, and would prefer to skip the tutorial.", "dplmc_devel_merchant_quest_skip",
[]],
##diplomacy end+

  [anyone, "merchant_quest_2", 
  [
  ],
  "Now -- go find and defeat that group of bandits.", "merchant_quest_2a", 
  [  
  ]],

  [anyone, "merchant_quest_3", 
  [
  ],
  "Now -- go attack that bandit hideout, get my brother back, and show those brigands what happens to those who threaten my household.", "merchant_quest_3a", 
  [  
  ]],
  
  [anyone, "start", 
  [
    (is_between, "$g_talk_troop", "trp_relative_of_merchant", "trp_relative_of_merchants_end"), ##Floris - bugfix
  ],
  "Oh -- thank the heavens... Thank the heavens... Am I safe?", "close_window",
  []],


  [anyone,"start", 
  [
	(is_between, "$g_talk_troop", "trp_swadian_merchant", "trp_startup_merchants_end"),
	(eq, "$g_do_one_more_meeting_with_merchant", 1),
	(faction_get_slot, ":faction_leader", "$g_encountered_party_faction", slot_faction_leader),
	(str_store_troop_name, s5, ":faction_leader"),
	##diplomacy start+ fix the pronouns
	(call_script, "script_dplmc_store_troop_is_female_reg", ":faction_leader", 4),
	],
 "Ah... {playername}. Things didn't go quite so well as I had hoped. {s5} couldn't quite find it in {reg4?her:him} to overlook my little breach of the peace. Oh, {reg4?she:he}'s grateful enough that I got rid of {reg4?her:his} crooked captain -- a guard who'll let in bandits will let in an enemy army, if the price is right -- but {reg4?she:he} can't exactly have me running around here as a lasting reminder of {reg4?her:his} failure to take care of things {reg4?herself:himself}.", "merchant_closing_statement_2",
	##diplomacy end+
	[]],

	[anyone|plyr,"merchant_closing_statement_2",
	[],
 "That hardly seems fair...", "merchant_closing_statement_3",
	[]],

	[anyone,"merchant_closing_statement_3",
	[
	##diplomacy start+ fix pronouns
	(faction_get_slot, ":faction_leader", "$g_encountered_party_faction", slot_faction_leader),
	(call_script, "script_dplmc_store_troop_is_female_reg", ":faction_leader", 4),
	],
	#"my boy" = "my girl", not "my lady"
	#change "He" to "{reg4?She:He}" and so forth
 "Fair? This is Calradia, {my boy/my girl}! Kings do what they will, and the rest of us do as they must. {reg4?She:He} didn't string me up, and instead gave me time to sell my properties -- even put in a word with the other merchants that they best pay me a fair price, too. That's gracious enough, as kings go -- but {reg4?she:he}'s a weak king, as they all are here, and weak kings must always look to their authority first, and justice second. I suppose I'd do the same, in {reg4?her:his} shoes.", "merchant_closing_statement_4",
	#diplomacy end+
  []],    
  
  [anyone,"merchant_closing_statement_4", 
  [
	#diplomacy start+ fix pronouns
	(call_script, "script_dplmc_print_cultural_word_to_sreg", "$g_talk_troop", DPLMC_CULTURAL_TERM_WEAPON, 0),
	(faction_get_slot, ":faction_leader", "$g_encountered_party_faction", slot_faction_leader),
	(call_script, "script_dplmc_store_troop_is_female_reg", ":faction_leader", 4),
	],
	#change "He" to "{reg4?She:He}" and so forth.  Replace "sell your sword" with "sell your {s0}".
 "Anyway, I wouldn't go rubbing your part in this affair in {s5}'s face -- but {reg4?she:he}'s taken note of you, and decided that you're not worth hanging, and that's something to which I'll raise a glass any day of the week. {reg4?She:He} might even have work for you, further down the road. Or, you can sell your {s0} to one of {reg4?her:his} competitors. Anyway, I hope you've learned a bit about what it will take to stay alive in this troubled land, and I suspect that the money you've earned won't go to waste. Good luck.", "close_window",
	#diplomacy end+
  [
    (assign, "$g_do_one_more_meeting_with_merchant", 2),
  ]], 
  
  [anyone|auto_proceed, "start",
   [
    (is_between, "$g_talk_troop", "trp_swadian_merchant", "trp_startup_merchants_end"),
    (check_quest_finished, "qst_save_town_from_bandits"),
    (eq, "$g_do_one_more_meeting_with_merchant", 2),
   ],
   "{!}.", "merchant_quests_last_word",
   []],
  
  [anyone,"merchant_quests_last_word", 
  [
  ],   
  "I am preparing to leave town in a short while. It's been an honor to know you. Good luck.", "close_window",
  [
  ]], 
  
  
\
	
  

  
  
  [anyone|plyr, "member_intel_liaison", [],
   "What have you discovered?", "member_intel_liaison_results", []],


  [anyone, "start", [(is_between, "$g_talk_troop", companions_begin, companions_end),
                     (eq, "$talk_context", tc_tavern_talk),
                     (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_gather_intel)],
   "Greetings, stranger.", "member_intel_liaison", []],

  [anyone|plyr, "member_intel_liaison", [
],
   "What have you discovered?", "member_intel_liaison_results", []],

  [anyone|plyr, "member_intel_liaison", [],
   "It's time to pull you out. Let's leave town separately, but join me soon after", "close_window", [
   (assign, "$npc_to_rejoin_party", "$g_talk_troop"),
   ]],
   
  [anyone|plyr, "member_intel_liaison", [],
   "You're doing good work. Stay here for a little longer", "close_window", []],


   
  [anyone, "member_intel_liaison_results", [
		(store_faction_of_party, ":town_faction", "$g_encountered_party"),
		(call_script, "script_update_faction_political_notes", ":town_faction"),
		(assign, ":instability_index", reg0),
		(val_add, ":instability_index", reg0),
		(val_add, ":instability_index", reg1),
		
		#diplomacy start+ Also include promoted kingdom ladies
		#(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
		(try_for_range, ":lord", heroes_begin, heroes_end),
		#diplomacy end+
			(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
			(store_faction_of_troop, ":lord_faction", ":lord"),
			(eq, ":lord_faction", ":town_faction"),
			(call_script, "script_update_troop_political_notes", ":lord"),
		(try_end),
		
		(str_store_faction_name, s12, ":town_faction"),
		(try_begin),
			(gt, ":instability_index", 60),
			(str_store_string, s11, "str_the_s12_is_a_labyrinth_of_rivalries_and_grudges_lords_ignore_their_lieges_summons_and_many_are_ripe_to_defect"),
		(else_try),	
			(is_between, ":instability_index", 40, 60),
			(str_store_string, s11, "str_the_s12_is_shaky_many_lords_do_not_cooperate_with_each_other_and_some_might_be_tempted_to_defect_to_a_liege_that_they_consider_more_worthy"),
		(else_try),	
			(is_between, ":instability_index", 20, 40),
			(str_store_string, s11, "str_the_s12_is_fairly_solid_some_lords_bear_enmities_for_each_other_but_they_tend_to_stand_together_against_outside_enemies"),
		(else_try),	
			(lt, ":instability_index", 20),
			(str_store_string, s11, "str_the_s12_is_a_rock_of_stability_politically_speaking_whatever_the_lords_may_think_of_each_other_they_fight_as_one_against_the_common_foe"),
		(try_end),
  
],
   "{s11} I notice that you have been keeping some notes about individual lords. I have annotated those with my findings.", "member_intel_liaison", []],
		 

		 
  [anyone,"member_fief_grant_1", [
        ], "Which fief did you have in mind?", "member_fief_grant_2",[]],
		 
  [anyone|plyr|repeat_for_parties,"member_fief_grant_2", [
		(store_repeat_object, ":center"),
        (is_between, ":center", centers_begin, centers_end),
		(neq, ":center", "$g_player_court"),
		(store_faction_of_party, ":center_faction", ":center"),
		##diplomacy start+ Handle player is co-ruler of kingdom
		(assign, ":alt_faction", 0),
		(try_begin),
			(eq, ":center_faction", "$players_kingdom"),
			(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
			(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
			(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
			(assign, ":alt_faction", 1),
		(try_end),
		(this_or_next|eq, ":alt_faction", 1),
		##diplomacy end+
		(eq, ":center_faction", "fac_player_supporters_faction"),
		(neg|party_slot_ge, ":center", slot_town_lord, active_npcs_begin), #ie, owned by player or unassigned
		(str_store_party_name, s11, ":center"),
		
        ], "{s11}", "member_fief_grant_3",[
		(store_repeat_object, "$temp"),
		]],
		 
  [anyone|plyr, "member_fief_grant_2", [
        ], "Never mind -- there is no fief I can offer.", "do_member_trade",[
		]],

		
  [anyone,"member_fief_grant_3", [
        ], "{s5}", "close_window",[
		(call_script, "script_npc_morale", "$g_talk_troop"),
		(assign, ":npc_morale", reg0),
		
		(remove_member_from_party, "$g_talk_troop", "p_main_party"),
		
		
		(try_begin),
		##diplomacy start+ Spouses use your banner
			(neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
			(this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, "$g_talk_troop"),
			(troop_slot_eq, "$g_talk_troop", slot_troop_spouse, "trp_player"),
			(this_or_next|is_between, "$g_talk_troop", heroes_begin, heroes_end),
			(troop_slot_eq, "trp_player", slot_troop_spouse, "$g_talk_troop"),
			(troop_get_slot, ":banner_id", "trp_player", slot_troop_banner_scene_prop),
			(gt, ":banner_id", 0),
			(troop_set_slot, "$g_talk_troop", slot_troop_banner_scene_prop, ":banner_id"),
			(troop_set_slot, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
		(else_try),
		##diplomacy end+
		#Floris Begin - companion-specific noble heraldry/banners
			(neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
			(is_between, "$g_talk_troop", companions_begin, companions_end),
			(store_sub, ":banner_offset", "$g_talk_troop", companions_begin),
			(store_add, ":banner_id", "spr_banner_companions01", ":banner_offset"),
			(troop_set_slot, "$g_talk_troop", slot_troop_banner_scene_prop, ":banner_id"), 
			(troop_set_slot, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),			
		(else_try),
		#Floris end -- leaving native code here...for error catching??
          (neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
          
          (assign, ":banner_offset", banners_end_offset),
          (val_sub, ":banner_offset", 1),
          (val_sub, ":banner_offset", "$g_companions_banner_id"),                            
          (store_add, ":banner_id", banner_scene_props_begin, ":banner_offset"),                    
          (troop_set_slot, "$g_talk_troop", slot_troop_banner_scene_prop, ":banner_id"),          
          (val_add, "$g_companions_banner_id", 1), 
		  
          (troop_set_slot, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
		(try_end),
				
		##diplomacy start+
		##Alternate use of this slot so we don't forget the enfeoffment, even if later
		##the companion's occupation changes and he loses the fief.
		(troop_set_slot, "$g_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),

		#Handle player is co-ruler of NPC faction
		##OLD:
		#(troop_set_faction, "$g_talk_troop", "fac_player_supporters_faction"),
		##NEW:
		(assign, ":is_coruler", 0),
		(try_begin),
			(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
			(neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
			(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
			(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),#player is co-ruler of an NPC faction
			(assign, ":is_coruler", 1),
			(troop_set_faction, "$g_talk_troop", "$players_kingdom"),
		(else_try),
			(troop_set_faction, "$g_talk_troop", "fac_player_supporters_faction"),
		(try_end),
		##diplomacy end+
		(call_script, "script_give_center_to_lord", "$temp", "$g_talk_troop", 0),
		(try_begin),
			(faction_slot_eq, "$players_kingdom", slot_faction_political_issue, "$temp"),
			(faction_set_slot, "$players_kingdom", slot_faction_political_issue, -1),
		(try_end),
   
		(try_begin),
		  (troop_slot_eq, "$g_talk_troop", slot_troop_original_faction, 0),
		  (party_get_slot, ":fief_culture", "$temp", slot_center_original_faction),
		  (troop_set_slot, "$g_talk_troop", slot_troop_original_faction, ":fief_culture"),
		(try_end),

		## WINDYPLAINS+ ## - Increased maximum starting renown of companion from 200 to 400 & let them keep their initial renown value.
		(troop_get_slot, ":renown_base", "$g_talk_troop", slot_troop_renown),
		(store_character_level, ":renown", "$g_talk_troop"),
		(val_mul, ":renown", 15),
		(val_add, ":renown", ":renown_base"),
		(val_max, ":renown", 400),
		## WINDYPLAINS- ##
		(troop_set_slot, "$g_talk_troop", slot_troop_renown, ":renown"),
		
		##diplomacy start+
		##Adjust starting gold by Looting and Trade skills
		##(troop_set_slot, "$g_talk_troop", slot_troop_wealth, 2500), #represents accumulated loot
		(assign, ":initial_gold", 2500),
		(try_begin),
			#Changes must be enabled
			(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
			#initial gold is 2500 * (10 + trade + looting) / 10, rounded.
			(store_skill_level, ":modifier", "skl_trade", "$g_talk_troop"),
			(store_skill_level, ":skill_level", "skl_looting", "$g_talk_troop"),
			(val_add, ":modifier", ":skill_level"),
			(val_add, ":modifier", 10),
			(val_mul, ":initial_gold", ":modifier"),
			(val_add, ":initial_gold", 5),
			(val_div, ":initial_gold", 10),
		(try_end),
		(troop_set_slot, "$g_talk_troop", slot_troop_wealth, ":initial_gold"), #represents accumulated loot
		##diplomacy end+
#		(troop_set_slot, "$g_talk_troop", slot_troop_readiness_to_join_army, 100), 
#		(troop_set_slot, "$g_talk_troop", slot_troop_readiness_to_follow_orders, 100), 
		
		(str_store_troop_name_plural, s12, "$g_talk_troop"),
		   ##diplomacy start+
		#(troop_get_type, ":is_female", "$g_talk_troop"),
		(call_script, "script_dplmc_store_troop_is_female", "$g_talk_troop"),
		(assign, reg65, reg0),
		(assign, ":is_female", reg65),
		(try_begin),
		   ##Enable the "Tribune" dialogue option for all Custodian or Benefactor companions
		   ##from the Rhodok lands, instead of just Bunduk.  Currently there are no others
		   ##besides him, but other mods may add them.   
		   #(eq, "$g_talk_troop", "trp_npc10"),
		   (this_or_next|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_benefactor),
			  (troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_custodian),
		   (troop_slot_eq, "$g_talk_troop", slot_troop_original_faction, "fac_kingdom_5"),
		   ##diplomacy end+
		   (str_store_string, s14, "str_tribune_s12"),
		(else_try),
		   (eq, ":is_female", 1),
		   (str_store_string, s14, "str_lady_s12"),
		(else_try),
		   (str_store_string, s14, "str_lord_s12"),
		(try_end),
		(troop_set_name, "$g_talk_troop", s14),
		##diplomacy start+
		##Custom player kingdom vassal titles, credit Caba`drin start
		(try_begin),
			(eq, ":is_coruler", 1),
			(call_script, "script_troop_set_title_according_to_faction", "$g_talk_troop", "$players_kingdom"),
		(else_try),
			(call_script, "script_troop_set_title_according_to_faction", "$g_talk_troop", "fac_player_supporters_faction"),
		(try_end),
		  ##Custom player kingdom vassal titles, credit Caba`drin start
		  ##diplomacy end+
			  
		(unlock_achievement, ACHIEVEMENT_I_DUB_THEE),
	
                (call_script, "script_check_concilio_calradi_achievement"),
		
		## WINDYPLAINS+ ## - Prevent companions that are upgraded to vassals from having their equipment replaced.
		# (try_begin),
			# (troop_add_item, "$g_talk_troop", "itm_ho_swa_saddle_black", 0),
			# (troop_add_item, "$g_talk_troop", "itm_ho_nor_courser_greysteel", 0),
			# (troop_add_item, "$g_talk_troop", "itm_ar_swa_nob_outfit",0),
			# (troop_add_item, "$g_talk_troop", "itm_ar_pla_t3_tabard_a",0),
			# (troop_add_item, "$g_talk_troop", "itm_ar_swa_t2_gambeson_a",0),
			# (troop_add_item, "$g_talk_troop", "itm_we_swa_sword_senlac",0),
			# (troop_add_item, "$g_talk_troop", "itm_sh_vae_kit_vaegir_a",0),
			# (troop_add_item, "$g_talk_troop", "itm_we_swa_spear_lance_light",0),
		# (try_end),
		# (troop_equip_items, "$g_talk_troop"),
		## WINDYPLAINS- ##
		
		(store_div, ":relation_boost", ":npc_morale", 3),
#		(val_add, ":relation_boost", 10),
		(call_script, "script_troop_change_relation_with_troop", "$g_talk_troop", "trp_player", ":relation_boost"), 
		
		# FLORIS 2.5: Windy+ - Clean out troop's inventory to prevent using these items as a lord.
		(troop_get_inventory_capacity, ":inv_cap", "$g_talk_troop"),
		(try_for_range, ":slot_no", 9, ":inv_cap"),
			(troop_get_inventory_slot, ":item_no", "$g_talk_troop", ":slot_no"),
			(ge, ":item_no", 1), # Filter out invalid items.
			(troop_set_inventory_slot, "$g_talk_troop", ":slot_no", -1),
		(try_end),
		# FLORIS 2.5: Windy-
		
		(str_store_party_name, s17, "$temp"),
		(store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
		(store_add, ":speech", "str_npc1_fief_acceptance", ":npc_no"),
#        (troop_get_slot, ":speech", "$g_talk_troop", slot_troop_fief_acceptance_string),
        (str_store_string, s5, ":speech"),  		
		]],
		

		 
  [anyone, "start", [(is_between, "$g_talk_troop", companions_begin, companions_end),
                     (this_or_next|eq, "$talk_context", tc_tavern_talk),
                     (this_or_next|eq, "$talk_context", tc_town_talk), #ADD THIS LINE FOR BODYGUARD CODE
						(eq, "$talk_context", tc_court_talk),
                     (main_party_has_troop, "$g_talk_troop")],
   "Let's leave whenever you are ready.", "close_window", []],

  [anyone, "start", [(is_between, "$g_talk_troop", companions_begin, companions_end),
                     (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, 0),
                     (troop_slot_eq, "$g_talk_troop", slot_troop_turned_down_twice, 1),
   ],
   "Please do not waste any more of my time today, {sir/madame}. Perhaps we shall meet again in our travels.", "close_window", [
       ]],


  [anyone, "start", [(is_between, "$g_talk_troop", companions_begin, companions_end),
                     (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, 0),
                     (eq, "$g_talk_troop_met", 0),
                     (troop_get_slot, ":intro", "$g_talk_troop", slot_troop_intro),
                     (str_store_string, 5, ":intro"),
                     (str_store_party_name, 20, "$g_encountered_party"),
   ],
   "{s5}", "companion_recruit_intro_response", [
                    (troop_set_slot, "$g_talk_troop", slot_troop_first_encountered, "$g_encountered_party"),
       ]],


  [anyone|plyr, "companion_recruit_intro_response", [
                     (troop_get_slot, ":intro_response", "$g_talk_troop", slot_troop_intro_response_1),
                     (str_store_string, 6, ":intro_response")
      ], "{s6}", "companion_recruit_backstory_a", []],

  [anyone|plyr, "companion_recruit_intro_response", [
                     (troop_get_slot, ":intro_response", "$g_talk_troop", slot_troop_intro_response_2),
                     (str_store_string, 7, ":intro_response")
      ],  "{s7}", "close_window", [
          ]],

  [anyone, "companion_recruit_backstory_a", [(troop_get_slot, ":backstory_a", "$g_talk_troop", slot_troop_backstory_a),
                     (str_store_string, 5, ":backstory_a"),
                     (str_store_string, 19, "str_here_plus_space"),
                     (str_store_party_name, 20, "$g_encountered_party"),
   ],
   "{s5}", "companion_recruit_backstory_b", []],

  [anyone, "companion_recruit_backstory_b", [(troop_get_slot, ":backstory_b", "$g_talk_troop", slot_troop_backstory_b),
                     (str_store_string, 5, ":backstory_b"),
                     (str_store_party_name, 20, "$g_encountered_party"),
   ],
   "{s5}", "companion_recruit_backstory_c", []],

  [anyone, "companion_recruit_backstory_c", [(troop_get_slot, ":backstory_c", "$g_talk_troop", slot_troop_backstory_c),
                     (str_store_string, 5, ":backstory_c"),
   ],
   "{s5}", "companion_recruit_backstory_response", []],

  [anyone|plyr, "companion_recruit_backstory_response", [
                     (troop_get_slot, ":backstory_response", "$g_talk_troop", slot_troop_backstory_response_1),
                     (str_store_string, 6, ":backstory_response")
      ], "{s6}", "companion_recruit_signup", []],

  [anyone|plyr, "companion_recruit_backstory_response", [
                     (troop_get_slot, ":backstory_response", "$g_talk_troop", slot_troop_backstory_response_2),
                     (str_store_string, 7, ":backstory_response")
      ],  "{s7}", "close_window", [
          ]],

  [anyone, "companion_recruit_signup", [(troop_get_slot, ":signup", "$g_talk_troop", slot_troop_signup),
                     (str_store_string, 5, ":signup"),
                     (str_store_party_name, 20, "$g_encountered_party"),

   ],
   "{s5}", "companion_recruit_signup_b", []],

  [anyone, "companion_recruit_signup_b", [
      (troop_get_slot, ":signup", "$g_talk_troop", slot_troop_signup_2),
      (troop_get_slot, reg3, "$g_talk_troop", slot_troop_payment_request),#

      (str_store_string, 5, ":signup"),
      (str_store_party_name, 20, "$g_encountered_party"),

   ],
   "{s5}", "companion_recruit_signup_response", []],

  [anyone|plyr, "companion_recruit_signup_response", [(neg|hero_can_join, "p_main_party"),], "Unfortunately, I can't take on any more hands in my company right now.", "close_window", [
     ]],

  [anyone|plyr, "companion_recruit_signup_response", [
                    (hero_can_join, "p_main_party"),
                    (troop_get_slot, ":signup_response", "$g_talk_troop", slot_troop_signup_response_1),
                    (str_store_string, 6, ":signup_response")
      ], "{s6}", "companion_recruit_payment", []],

  [anyone|plyr, "companion_recruit_signup_response", [
                    (hero_can_join, "p_main_party"),
                     (troop_get_slot, ":signup_response", "$g_talk_troop", slot_troop_signup_response_2),
                     (str_store_string, 7, ":signup_response")
      ],  "{s7}", "close_window", [
          ]],

  [anyone|auto_proceed, "companion_recruit_payment", [
      (troop_slot_eq, "$g_talk_troop", slot_troop_payment_request, 0),
   ],
   ".", "companion_recruit_signup_confirm", []],
  
  [anyone, "companion_recruit_payment", [
      (store_sub, ":npc_offset", "$g_talk_troop", "trp_npc1"),
      (store_add, ":dialog_line", "str_npc1_payment", ":npc_offset"),
      (str_store_string, s5, ":dialog_line"),
      (troop_get_slot, reg3, "$g_talk_troop", slot_troop_payment_request),
      (str_store_party_name, s20, "$g_encountered_party"),
   ],
   "{s5}", "companion_recruit_payment_response", []],

  [anyone|plyr, "companion_recruit_payment_response", [
                    (hero_can_join, "p_main_party"),
                    (troop_get_slot, ":amount_requested", "$g_talk_troop", slot_troop_payment_request),#
                    (store_troop_gold, ":gold", "trp_player"),#
                    (ge, ":gold", ":amount_requested"),#
                    (assign, reg3, ":amount_requested"),
                    (store_sub, ":npc_offset", "$g_talk_troop", "trp_npc1"),
                    (store_add, ":dialog_line", "str_npc1_payment_response", ":npc_offset"),
                    (str_store_string, s6, ":dialog_line"),
      ], "{s6}", "companion_recruit_signup_confirm", [
                    (troop_get_slot, ":amount_requested", "$g_talk_troop", slot_troop_payment_request),#
                    (gt, ":amount_requested", 0),#
                    (troop_remove_gold, "trp_player", ":amount_requested"),  #                  
                    (troop_set_slot, "$g_talk_troop", slot_troop_payment_request, 0),#
          ]],

  [anyone|plyr, "companion_recruit_payment_response", [
                     (troop_get_slot, ":signup_response", "$g_talk_troop", slot_troop_signup_response_2),
                     (str_store_string, s7, ":signup_response")
      ],  "Sorry. I can't afford that at the moment.", "close_window", [
          ]],

  [anyone, "start", [(is_between, "$g_talk_troop", companions_begin, companions_end),
                     (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, 0),
                     (troop_slot_eq, "$g_talk_troop", slot_troop_met_previously, 1),
                     (troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, 0),

    ],
   "We meet again.", "companion_recruit_meet_again", [
                     (troop_set_slot, "$g_talk_troop", slot_troop_turned_down_twice, 1),
       ]],

  [anyone|plyr, "companion_recruit_meet_again", [
      ], "So... What have you been doing since our last encounter?", "companion_recruit_backstory_delayed", []],

  [anyone|plyr, "companion_recruit_meet_again", [
      ],  "Good day to you.", "close_window", [
          ]],


  [anyone, "start", [(is_between, "$g_talk_troop", companions_begin, companions_end),
                     (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, 0),
                     (troop_slot_eq, "$g_talk_troop", slot_troop_met_previously, 0),
                     (troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, 0),
   ],
   "Yes?", "companion_recruit_secondchance", [
                     (troop_set_slot, "$g_talk_troop", slot_troop_turned_down_twice, 1),
       ]],


  [anyone|plyr, "companion_recruit_secondchance", [
      ], "My apologies if I was rude, earlier. What was your story again?", "companion_recruit_backstory_b", []],

  [anyone|plyr, "companion_recruit_secondchance", [
      ],  "Never mind.", "close_window", [
          ]],

  [anyone, "companion_recruit_backstory_delayed",
   [(troop_get_slot, ":backstory_delayed", "$g_talk_troop", slot_troop_backstory_delayed),
     (str_store_string, 5, ":backstory_delayed")
   ],
   "{s5}", "companion_recruit_backstory_delayed_response", []],

  [anyone|plyr, "companion_recruit_backstory_delayed_response", [
      ], "I might be able to use you in my company.", "companion_recruit_signup_b", [
          ]],

  [anyone|plyr, "companion_recruit_backstory_delayed_response", [
      ],  "I'll let you know if I hear of anything.", "close_window", [
          ]],

  [anyone, "companion_recruit_signup_confirm", [], "Good! Give me a few moments to prepare and I'll be ready to move.", "close_window",
   [(call_script, "script_recruit_troop_as_companion", "$g_talk_troop")]],



### Rehire dialogues
  [anyone, "start", [(is_between, "$g_talk_troop", companions_begin, companions_end),
					 (neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
                     (troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, pp_history_indeterminate),
					 
                     (troop_get_slot, ":prison_center", "$g_talk_troop", slot_troop_prisoner_of_party),
                     (lt, ":prison_center", centers_begin),
   ],
   "My offer to rejoin you still stands, if you'll have me.", "companion_rehire", []],

### If the companion and the player were separated in battle
  [anyone, "start", 
  [
    (is_between, "$g_talk_troop", companions_begin, companions_end),
	(neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
    (troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, pp_history_scattered),
        
    (this_or_next|eq, "$talk_context", tc_hero_freed),
    (neg|troop_slot_ge, "$g_talk_troop", slot_troop_prisoner_of_party, 0),
    
    (neq, "$talk_context", tc_prison_break),
					 
    (assign, ":battle_fate", "str_battle_fate_1"),
    (store_random_in_range, ":fate_roll", 0, 5),
    (val_add, ":battle_fate", ":fate_roll"),
    (str_store_string, s6, ":battle_fate"),
    (troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
    (str_store_string, s5, ":honorific"),
  ],
  "It is good to see you alive, {s5}! {s6}, and I did not know whether you had been captured, or slain, or got away. I've been roaming around since then, looking for you. Shall I get my gear together and rejoin your company?","companion_rehire", 
  [
    (troop_set_slot, "$g_talk_troop", slot_troop_playerparty_history, pp_history_indeterminate),
    (troop_set_slot, "$g_talk_troop", slot_troop_prisoner_of_party, -1),
  ]],

  [anyone|plyr,"start", 
  [
    (is_between, "$g_talk_troop", companions_begin, companions_end),
	(neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
    (troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, pp_history_scattered),
                     
    (troop_slot_ge, "$g_talk_troop", slot_troop_prisoner_of_party, 0),
    
    (neq, "$talk_context", tc_prison_break),
					 
    (assign, ":battle_fate", "str_battle_fate_1"),
    (store_random_in_range, ":fate_roll", 0, 5),
    (val_add, ":battle_fate", ":fate_roll"),
    (str_store_string, s6, ":battle_fate"),
    (troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
    (str_store_string, s5, ":honorific"),
  ],
  "I've come to break you out of here.", "companion_prison_break_chains",[]],

  [anyone,"companion_prison_break_chains", [],   
  "Thank the heavens you came! However, I'm not going anywhere with these chains on my legs. You'll need to get the key away from the guard somehow.", "close_window",[]],			




### If the player and the companion parted on bad terms
  [anyone, "start", [(is_between, "$g_talk_troop", companions_begin, companions_end),
                     (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, 0),
                     (troop_slot_eq, "$g_talk_troop", slot_troop_turned_down_twice, 0),
                     (troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, pp_history_quit),
                     (troop_get_slot, ":speech", "$g_talk_troop", slot_troop_rehire_speech),
                     (str_store_string, 5, ":speech"),
   ],
   "{s5}", "companion_rehire", [
                     (troop_set_slot, "$g_talk_troop", slot_troop_playerparty_history, pp_history_indeterminate),
      ]],


###If the player and the companion parted on good terms
  [anyone, "start", [(is_between, "$g_talk_troop", companions_begin, companions_end),
                     (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, 0),
                     (troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, pp_history_dismissed),
                     (troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
                     (str_store_string, 21, ":honorific"),
                     (troop_get_slot, ":speech", "$g_talk_troop", slot_troop_backstory_delayed),
                     (str_store_string, 5, ":speech"),
   ],
   "It is good to see you, {s21}! To tell you the truth, I had hoped to run into you.",
   "companion_was_dismissed", [
                     (troop_set_slot, "$g_talk_troop", slot_troop_playerparty_history, pp_history_indeterminate),
      ]],

  [anyone, "companion_was_dismissed", [
					 (neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
                      (troop_get_slot, ":speech", "$g_talk_troop", slot_troop_backstory_delayed),
                     (str_store_string, 5, ":speech"),
   ],
   "{s5}. Would you want me to rejoin your company?", "companion_rehire", [
      ]],


  [anyone|plyr, "companion_rehire", 
  [
    (hero_can_join, "p_main_party"),
  ], "Welcome back, my friend!", "companion_recruit_signup_confirm", []],

  [anyone|plyr, "companion_rehire", 
  [],  
  "Sorry, I can't take on anyone else right now.", "companion_rehire_refused", []],

  [anyone, "companion_rehire_refused", [], "Well... Look me up if you change your mind, eh?", "close_window",
   [
     (troop_get_slot, ":current_town_no", "$g_talk_troop", slot_troop_cur_center),  
   
     (try_begin),
       (neg|is_between, ":current_town_no", towns_begin, towns_end),
              
       (store_random_in_range, ":town_no", towns_begin, towns_end),       
       (troop_set_slot, "$g_talk_troop", slot_troop_cur_center, ":town_no"),  
     
       (try_begin),
         (ge, "$cheat_mode", 1),
         (assign, reg1, ":current_town_no"),
         (str_store_party_name, s7, ":town_no"),
         (display_message, "@{!}current town was {reg1}, now moved to {s7}"),
       (try_end),
     (try_end),  
   ]],

   #Default dialog added - for rehire
  [anyone, "start", [
  (is_between, "$g_talk_troop", companions_begin, companions_end),  
  (neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
  
  (troop_get_slot, ":prison_center", "$g_talk_troop", slot_troop_prisoner_of_party),
  (lt, ":prison_center", centers_begin),  
  ], "So... Do you want me back yet?", "companion_rehire",
   []],
#Ministerial issues
   



   [anyone, "minister_issues",
   [
    (check_quest_active, "qst_consult_with_minister"),
	(eq, "$g_minister_notification_quest", "qst_resolve_dispute"),

    (setup_quest_text,"qst_resolve_dispute"),
	
	(quest_get_slot, ":lord_1", "qst_resolve_dispute", slot_quest_target_troop),
	(str_store_troop_name, s11, ":lord_1"),
	
	(quest_get_slot, ":lord_2", "qst_resolve_dispute", slot_quest_object_troop),
	(str_store_troop_name, s12, ":lord_2"),	

	(str_store_string, s2, "str_resolve_the_dispute_between_s11_and_s12"),
	(call_script, "script_start_quest", "qst_resolve_dispute", -1),
	(quest_set_slot, "qst_resolve_dispute", slot_quest_expiration_days, 30),
	(quest_set_slot, "qst_resolve_dispute", slot_quest_giver_troop, "$g_player_minister"),
	(quest_set_slot, "qst_resolve_dispute", slot_quest_target_state, 0),
	(quest_set_slot, "qst_resolve_dispute", slot_quest_object_state, 0),
	
	(quest_get_slot, ":lord_1", "qst_resolve_dispute", slot_quest_target_troop), #this block just to check if the slots work
	(str_store_troop_name, s11, ":lord_1"),
	(quest_get_slot, ":lord_2", "qst_resolve_dispute", slot_quest_object_troop),
	(str_store_troop_name, s12, ":lord_2"),	
	
     ],
   "There is a matter which needs your attention. The quarrel between {s11} and {s12} has esclatated to a point where it has become unseemly. If you do intervene, you risk offending one of the lords. However, if you do nothing, you risk appearing weak. Such are the burdens of kingship, {sire/my lady}.", "minister_pretalk",
   [
   (call_script, "script_end_quest", "qst_consult_with_minister"),
   ]],
   
   [anyone, "minister_issues",
   [
    (assign, "$g_center_taken_by_player_faction", -1),
    (try_for_range, ":center_no", centers_begin, centers_end),
      (eq, "$g_center_taken_by_player_faction", -1),
      (store_faction_of_party, ":center_faction", ":center_no"),
		##diplomacy start+ Handle player is co-ruler of kingdom
		(assign, ":alt_faction", 0),
		(try_begin),
			(eq, ":center_faction", "$players_kingdom"),
			(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
			(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
			(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
			(assign, ":alt_faction", 1),
		(try_end),
		(this_or_next|eq, ":alt_faction",  1),
		##diplomacy end+
      (eq, ":center_faction", "fac_player_supporters_faction"),
      (neg|party_slot_ge, ":center_no", slot_town_lord, 0),
      (assign, "$g_center_taken_by_player_faction", ":center_no"),
    (try_end),
    (is_between, "$g_center_taken_by_player_faction", centers_begin, centers_end),
    (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
     ],
   "{s1} currently does not have a lord. You may wish to keep it this way, as lords will sometimes gravitate towards lieges who have land to offer, but for the time being, no one is collecting any of its rents.", "minister_talk",
   []],
   
   [anyone, "minister_issues",
   [
   (neg|is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),
   ],
   "At this point, there are no particularly urgent matters which need your attention. I should point out though, sire, that I am not very skilled in the ways of politics, and that I am anxious to return to private life. If you wish to issue any but the most basic directives, I suggest appointing a trusted companion in my stead. In the meantime, is there anything you wish done?", "minister_talk",[]],

   [anyone, "minister_issues",
   [
   (eq, 1, 0),
   ],
   "{!}[Should not appear - there to prevent error related to center_captured_lord_advice]", "center_captured_lord_advice",[]],
   
   [anyone, "minister_issues",
   [
   (lt, "$player_right_to_rule", 30),
   ],
   "If I may offer you a word of advice, my {lord/lady}, it seems that your right to rule as an independent monarch is not sufficiently recognized, and this may bring us problems further down the road. It may be advisable to find a kingdom with whom you have shared interests and seek its recognition, to establish yourself as an equal with Calradia's other rulers.", "minister_talk",[]],

   
   [anyone, "minister_issues",
   [],
   "At this point, there are no particularly urgent matters which need your attention. Is there anything you wish done?", "minister_talk",[]],

   [anyone, "minister_pretalk",
   [],
   "Is there anything you wish done?", "minister_talk", 
   []],
   
  [anyone|plyr,"minister_talk",
   [
   (is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),
   ],
   "Do you have any ideas to strengthen our sovereignty's unity?", "combined_political_quests",[
   (call_script, "script_get_political_quest", "$g_talk_troop"),
   (assign, "$political_quest_found", reg0),
   (assign, "$political_quest_target_troop", reg1),
   (assign, "$political_quest_object_troop", reg2),
   
 ]],
   
   
  [anyone|plyr,"minister_talk",
   [
   (assign, "$political_quest_to_cancel", -1),
   (try_begin),
	(check_quest_active, "qst_offer_gift"),
	(quest_slot_eq, "qst_offer_gift", slot_quest_giver_troop, "$g_talk_troop"),
    (assign, "$political_quest_to_cancel", "qst_offer_gift"),
	(str_store_string, s10, "str_offer_gift_description"),
   (else_try),
	(check_quest_active, "qst_resolve_dispute"),
	(quest_slot_eq, "qst_resolve_dispute", slot_quest_giver_troop, "$g_talk_troop"),
    (assign, "$political_quest_to_cancel", "qst_resolve_dispute"),
	(str_store_string, s10, "str_resolve_dispute_description"),
   (try_end),	
   (gt, "$political_quest_to_cancel", 0),
   ],
   "Let's abandon our plan to {s10}.", "minister_cancel_political_quest",[
 ]],
 
  [anyone,"minister_cancel_political_quest",
   [],
   "Are you sure you want to drop that idea?", "minister_cancel_political_quest_confirm",[
 ]],
 
  [anyone|plyr,"minister_cancel_political_quest_confirm",
   [],
   "Yes, I am sure. Let's abandon that idea.", "minister_pretalk",[
   (call_script, "script_abort_quest", "$political_quest_to_cancel", 1), ##Native 1.132
#   (call_script, "script_abort_quest", "$political_quest_to_cancel"), ##Native 1.131
 ]],
 
  [anyone|plyr,"minister_cancel_political_quest_confirm",
   [],
   "Actually, never mind.", "minister_pretalk",[
 ]],   
   
   
   
   [anyone|plyr, "minister_talk",
   [
   (is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),
   ],
   "I wish to dispatch an emissary.", "minister_diplomatic_kingdoms",
   []],

   [anyone|plyr, "minister_talk",
   [
   (is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),
   ],
   "I wish to indict a disloyal vassal for treason.", "minister_indict",
   []],   

   [anyone|plyr, "minister_talk",
   [
   (faction_get_slot, ":current_marshal", "$players_kingdom", slot_faction_marshall),
   (ge, ":current_marshal", 0),
   (try_begin),
    (gt, ":current_marshal", 0),
	(str_store_troop_name, s4, ":current_marshal"),
   (else_try),	
	(str_store_string, s4, "str_myself"),
   (try_end),
   ],
   "I wish to replace {s4} as marshal.", "minister_change_marshal",
   []],
   
   [anyone|plyr, "minister_talk",
   [
   (faction_slot_eq,  "$players_kingdom", slot_faction_marshall, -1),
   ],
   "I wish to appoint a new marshal.", "minister_change_marshal",
   []],
   
   [anyone, "minister_change_marshal",
   [
	(store_current_hours, ":hours"),
	(val_sub, ":hours", "$g_player_faction_last_marshal_appointment"),
	##diplomacy start+ Change based on centralization
	#(lt, ":hours", 48), (Standard 48 hours, minimum 24 hours, maximum 72 hours)
	(faction_get_slot, ":centralization", "fac_player_supporters_faction", dplmc_slot_faction_centralization),
	(val_clamp, ":centralization", -3, 4),
	(store_mul, ":reset_time", ":centralization", 8),
	(val_add, ":reset_time", 48),
	(lt, ":hours", ":reset_time"),
	##diplomacy end+
   ],
   "You have just made such an appointment, {sire/my lady}. If you countermand your decree so soon, there will be great confusion. We will need to wait a few days.", "minister_pretalk",
   []],

   
   [anyone|plyr, "minister_talk",
   [
   (neg|is_between, "$g_player_minister", active_npcs_begin, active_npcs_end),
   ],
   "I wish for you to retire as minister.", "minister_replace",
   []],

   [anyone|plyr, "minister_talk",
   [
   (is_between, "$g_player_minister", active_npcs_begin, active_npcs_end),
	(neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
   
   ],
   "I wish you to rejoin my direct retinue.", "minister_replace",
   []],

   [anyone|plyr, "minister_talk",
   [
   (is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),
   ],
   "I wish you to grant one of my vassals a fief.", "minister_grant_fief",
   []],

   [anyone|plyr, "minister_talk",
   [
   (is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),
   (assign, ":fief_found", -1),
	##diplomacy start+ Handle player is co-ruler of kingdom
	(assign, ":alt_faction", "fac_player_supporters_faction"),
	(try_begin),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":alt_faction", "$players_kingdom"),
	(try_end),
	##diplomacy end+
	(try_for_range, ":center", centers_begin, centers_end),
	(eq, ":fief_found", -1),
	(store_faction_of_party, ":center_faction", ":center"),
	##diplomacy start+ Handle player is co-ruler of kingdom
	(this_or_next|eq, ":center_faction", ":alt_faction"),
	##diploamcy end+
    (eq, ":center_faction", "fac_player_supporters_faction"),
	(party_get_slot, ":town_lord", ":center", slot_town_lord),
	(try_begin),
		(ge, ":town_lord", active_npcs_begin),
		(store_faction_of_troop, ":town_lord_faction", ":town_lord"),
		##diplomacy start+ Handle player is co-ruler of kingdom
		(neq, ":town_lord_faction", ":alt_faction"),
		##diplomacy end+
		(neq, ":town_lord_faction", "fac_player_supporters_faction"),
		(assign, ":town_lord", -1),
	(try_end),
	(lt, ":town_lord", 0),
	(assign, ":fief_found", ":center"),
   (try_end),
   (gt, ":fief_found", -1),
   (str_store_party_name, s4, ":fief_found"),
   ],
   "I wish to make myself lord of {s4}.", "minister_grant_self_fief",
   []],

   [anyone, "minister_grant_self_fief",
   [
   ],
   "As you wish. You shall be lord of {s4}.", "minister_pretalk",
   [
   (assign, ":fief_found", -1),
   ##diplomacy start+ Handle player is co-ruler of kingdom
	(assign, ":alt_faction", "fac_player_supporters_faction"),
	(try_begin),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":alt_faction", "$players_kingdom"),
	(try_end),
	##diplomacy end+
   (try_for_range, ":center", centers_begin, centers_end),
    (eq, ":fief_found", -1),
	(store_faction_of_party, ":center_faction", ":center"),
	##diplomacy start+ Handle player is co-ruler of kingdom
	(this_or_next|eq, ":center_faction", ":alt_faction"),
	##diploamcy end+
    (eq, ":center_faction", "fac_player_supporters_faction"),
	(party_get_slot, ":town_lord", ":center", slot_town_lord),
	(try_begin),
		(ge, ":town_lord", active_npcs_begin),
		(store_faction_of_troop, ":town_lord_faction", ":town_lord"),
		##diplomacy start+ Handle player is co-ruler of kingdom
		(neq, ":town_lord_faction", ":alt_faction"),
		##diplomacy end+
		(neq, ":town_lord_faction", "fac_player_supporters_faction"),
		(assign, ":town_lord", -1),
	(try_end),
	(lt, ":town_lord", 0),
	(assign, ":fief_found", ":center"),	
   (try_end),
   
   
   (call_script, "script_give_center_to_lord", ":fief_found", "trp_player", 0),
   (try_begin),
	(faction_slot_eq, "$players_kingdom", slot_faction_political_issue, ":fief_found"),
	(faction_set_slot, "$players_kingdom", slot_faction_political_issue, -1),
   (try_end),   
   (str_store_party_name, s4, ":fief_found"),
   
   ]],
   

##diplomacy begin
	# Recruiter kit begin
	[trp_dplmc_recruiter, "start", [
	##diplomacy start+ replace {reg65?madame:sir} with {s0}.  Also replace "okay to you" with "okay with you".
	(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
	], "Hello {s0}. If it's ok with you, I would like to get on with my assignment.", "dplmc_recruiter_talk",[]],
	##diplomacy end+
	[trp_dplmc_recruiter|plyr, "dplmc_recruiter_talk", [], "Ok, keep going.", "close_window",[(assign, "$g_leave_encounter",1)]],
	[trp_dplmc_recruiter|plyr, "dplmc_recruiter_talk", [], "I want you to recruit different troops.", "dplmc_recruiter_talk_2",[]],

	[trp_dplmc_recruiter, "dplmc_recruiter_talk_2", [
	(party_get_slot, reg1, "$g_encountered_party", dplmc_slot_party_recruiter_needed_recruits),
	(party_get_slot, ":recruit_faction", "$g_encountered_party", dplmc_slot_party_recruiter_needed_recruits_faction),

	(store_sub, ":offset", ":recruit_faction", "fac_kingdom_1"),
	(val_add, ":offset", "str_kingdom_1_adjective"),
	(str_store_string, s1, ":offset"),

	], "My current task is to recruit {reg1} {s1} troops for you. Should I recruit different soldiers from now on?", "dplmc_recruiter_talk_3",[]],
	[trp_dplmc_recruiter|plyr, "dplmc_recruiter_talk_3", [], "No, keep going.", "close_window",[(assign, "$g_leave_encounter",1)]],

	[trp_dplmc_recruiter|plyr|repeat_for_factions, "dplmc_recruiter_talk_3",
	[
	(store_repeat_object, ":faction_no"),
	##diplomacy start+ Sometimes the player may be the ruler or co-ruler of an NPC kingdom.
	#Do not allow sending emissaries in those cases.
	(neq, ":faction_no", "$players_kingdom"),
	##diplomacy end+
	(is_between, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
	(store_sub, ":offset", ":faction_no", "fac_kingdom_1"),
	(val_add, ":offset", "str_kingdom_1_adjective"),
	(str_store_string, s11, ":offset"),
	],
	"{s11}.", "dplmc_recruiter_talk_4",
	[
	(store_repeat_object, ":faction_no"),
	(assign, "$temp", ":faction_no"),
	]],

	[trp_dplmc_recruiter|plyr, "dplmc_recruiter_talk_3", [], "Recruit any troops.", "dplmc_recruiter_talk_4",[(assign,"$temp",-1)]],

	[trp_dplmc_recruiter, "dplmc_recruiter_talk_4", [(party_set_slot, "$g_encountered_party", dplmc_slot_party_recruiter_needed_recruits_faction, "$temp"),
	##diplomacy start+ replace {reg65?madame:sir} with {s0}
	(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
	], "Sure {s0}. I will. Anything else you want?", "dplmc_recruiter_talk",[]],
	##diplomacy end+
	# Recruiter kit end

  ##Messenger
  [trp_dplmc_messenger, "start", [], "Greetings. Sorry but I don't have time to talk now. I am delivering a very important message to {s6}.", "dplmc_messenger_talk", []],
  
  [trp_dplmc_messenger|plyr, "dplmc_messenger_talk", [], "Alright, I don't want to delay you. Godspeed!", "dplmc_messenger_talk_farewell",[]],
  
  [trp_dplmc_messenger, "dplmc_messenger_talk_farewell", [], "Thank you. Farewell!", "close_window", [(assign, "$g_leave_encounter", 1),]],


  ##patrol
	[anyone, "start",
		[
		(party_slot_eq, "$g_encountered_party", slot_party_type, spt_patrol),
		(party_slot_eq, "$g_encountered_party", dplmc_slot_party_mission_diplomacy, "trp_player"),
		(party_get_slot, ":target_party", "$g_encountered_party", slot_party_ai_object),
		(str_store_party_name, s6, ":target_party"),
		##nested diplomacy start+ Replace "Sire" with {s0}
		(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
	#], "Greetings, Sire. We are still patrolling {s6}. Do you have new orders?", "dplmc_patrol_talk", []
	], "Greetings, {s0}. We are still patrolling {s6}. Do you have new orders?", "dplmc_patrol_talk", []
	##nested diplomacy end+
	],

	##nested diplomacy start+ Replace "Sire" with {s0}
	#[anyone, "dplmc_patrol_pretalk", [], "Greetings, Sire. Do you have new orders?", "dplmc_patrol_talk",
	[anyone, "dplmc_patrol_pretalk", [
	(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
	], "Greetings, {s0}. Do you have new orders?", "dplmc_patrol_talk",
	##nested diplomacy end+
	[]],
  
  ##patrol new area
  [anyone|plyr, "dplmc_patrol_talk", [], "Please patrol a new area.", "dplmc_patrol_orders_area_ask", 
  []],
  
  [anyone, "dplmc_patrol_orders_area_ask", [], "Where should we go?", "dplmc_patrol_orders_area", 
  []],
  
  [anyone|plyr|repeat_for_parties, "dplmc_patrol_orders_area",
  [
    (store_repeat_object, ":party_no"),
    (is_between, ":party_no", centers_begin, centers_end),
    (store_faction_of_party, ":party_faction", ":party_no"),
    (eq, ":party_faction", "$players_kingdom"),
    (str_store_party_name, s11, ":party_no"),
  ],
  "{s11}.", "dplmc_patrol_confirm_ask", 
  [
    (store_repeat_object, "$diplomacy_var"),
  ]
  ],
  
  [anyone|plyr, "dplmc_patrol_orders_area", [], "Nevermind.", "dplmc_patrol_pretalk", 
  []],
  
  [anyone, "dplmc_patrol_confirm_ask", 
   [(str_store_party_name, s5, "$diplomacy_var"),], 
   "As you wish, we will patrol {s5}.", "dplmc_patrol_confirm", 
   []
  ],
  
  [anyone|plyr, "dplmc_patrol_confirm", [(str_store_party_name, s5, "$diplomacy_var"),], "Thank you.", "close_window", 
  [
    (party_set_name, "$g_encountered_party", "@{s5} patrol"),
    (party_set_slot, "$g_encountered_party", slot_party_ai_object, "$diplomacy_var"),
    (party_set_slot, "$g_encountered_party", slot_party_ai_state, spai_patrolling_around_center),
    (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_travel_to_party),
    (party_set_ai_object, "$g_encountered_party", "$diplomacy_var"),
    (assign, "$g_leave_encounter", 1),
   ]],
  
  [anyone|plyr, "dplmc_patrol_confirm", [], "Wait, I changed my mind.", "dplmc_patrol_pretalk", 
  []],
  
     
  ##reinforce garrison
  [anyone|plyr, "dplmc_patrol_talk", [], "I need you to reinforce a garrison.", "dplmc_patrol_orders_garrison_ask", 
  []],
  
  [anyone, "dplmc_patrol_orders_garrison_ask", [], "Where should we go?", "dplmc_patrol_garrison_target", 
  []],
  
  [anyone|plyr|repeat_for_parties, "dplmc_patrol_garrison_target",
  [
    (store_repeat_object, ":party_no"),
    (is_between, ":party_no", centers_begin, centers_end),
    (store_faction_of_party, ":party_faction", ":party_no"),
    (eq, ":party_faction", "$players_kingdom"),
    (str_store_party_name, s11, ":party_no"),
  ],
  "{!}{s11}.", "dplmc_patrol_garrison_confirm_ask", 
  [
    (store_repeat_object, "$diplomacy_var"),
  ]
  ],
  
  [anyone|plyr, "dplmc_patrol_garrison_target", [], "Nevermind.", "dplmc_patrol_pretalk", 
  []],
  
  [anyone, "dplmc_patrol_garrison_confirm_ask", 
   [(str_store_party_name, s5, "$diplomacy_var"),], 
   "As you wish, we will reinforce {s5}.", "dplmc_patrol_garrison_confirm", 
   []
  ],
  
  [anyone|plyr, "dplmc_patrol_garrison_confirm", [(str_store_party_name, s5, "$diplomacy_var"),], "Thank you.", "close_window", 
  [
    (party_set_name, "$g_encountered_party", "@{s5} patrol"),
    (party_set_slot, "$g_encountered_party", slot_party_ai_object, "$diplomacy_var"),
    (party_set_slot, "$g_encountered_party", slot_party_ai_state, spai_retreating_to_center),
    (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_travel_to_party),
    (party_set_ai_object, "$g_encountered_party", "$diplomacy_var"),
    (assign, "$g_leave_encounter", 1),
   ]],
  
  [anyone|plyr, "dplmc_patrol_garrison_confirm", [], "Wait, I changed my mind.", "dplmc_patrol_pretalk", 
  []],

  ##give troops
  [anyone|plyr,"dplmc_patrol_talk", [],
   "I want to give some troops to you.", "dplmc_patrol_give_troops",[]],
   

  [anyone,"dplmc_patrol_give_troops", [],
   "Well, I could use some good soldiers. Thank you.", "dplmc_patrol_pretalk",
   [
     (change_screen_give_members, "$g_talk_troop_party"),
     (change_screen_exchange_members,0),
     ]],

  ##disband
  [anyone|plyr, "dplmc_patrol_talk", [], "I don't need you any longer. Please disband.", "close_window", 
  [
    (remove_party, "$g_encountered_party"),
    (assign, "$g_leave_encounter", 1),
  ]],
  
  [anyone|plyr, "dplmc_patrol_talk", [], "Please continue.", "close_window", 
  [(assign, "$g_leave_encounter", 1),]],
  
  ##gift caravan
  [pt_dplmc_gift_caravan|party_tpl, "start", 
  [
    (party_slot_eq, "$g_talk_troop_party", slot_party_type, dplmc_spt_gift_caravan), 
    (party_get_slot, ":target_party", "$g_talk_troop_party", slot_party_ai_object),
    (party_get_slot, ":gift", "$g_talk_troop_party", dplmc_slot_party_mission_diplomacy),
    (str_store_item_name, s12, ":gift"),
    
    (try_begin),
      (party_slot_ge, "$g_talk_troop_party",  slot_party_orders_object,  0), 
      (party_get_slot, ":target_troop", "$g_talk_troop_party",  slot_party_orders_object),
      (str_store_troop_name, s13, ":target_troop"),
    (else_try), 
      (str_store_party_name, s13, ":target_party"),
    (try_end),
    
  ], 
  "Greetings. I' am currently delivering {s12} to {s13}.", "dplmc_gift_talk", []],
  
  ##Floris MTT begin
    [pt_dplmc_gift_caravan_r|party_tpl, "start", 
  [
    (party_slot_eq, "$g_talk_troop_party", slot_party_type, dplmc_spt_gift_caravan), 
    (party_get_slot, ":target_party", "$g_talk_troop_party", slot_party_ai_object),
    (party_get_slot, ":gift", "$g_talk_troop_party", dplmc_slot_party_mission_diplomacy),
    (str_store_item_name, s12, ":gift"),
    
    (try_begin),
      (party_slot_ge, "$g_talk_troop_party",  slot_party_orders_object,  0), 
      (party_get_slot, ":target_troop", "$g_talk_troop_party",  slot_party_orders_object),
      (str_store_troop_name, s13, ":target_troop"),
    (else_try), 
      (str_store_party_name, s13, ":target_party"),
    (try_end),
    
  ], 
  "Greetings. I' am currently delivering {s12} to {s13}.", "dplmc_gift_talk", []],
    [pt_dplmc_gift_caravan_e|party_tpl, "start", 
  [
    (party_slot_eq, "$g_talk_troop_party", slot_party_type, dplmc_spt_gift_caravan), 
    (party_get_slot, ":target_party", "$g_talk_troop_party", slot_party_ai_object),
    (party_get_slot, ":gift", "$g_talk_troop_party", dplmc_slot_party_mission_diplomacy),
    (str_store_item_name, s12, ":gift"),
    
    (try_begin),
      (party_slot_ge, "$g_talk_troop_party",  slot_party_orders_object,  0), 
      (party_get_slot, ":target_troop", "$g_talk_troop_party",  slot_party_orders_object),
      (str_store_troop_name, s13, ":target_troop"),
    (else_try), 
      (str_store_party_name, s13, ":target_party"),
    (try_end),
    
  ], 
  "Greetings. I' am currently delivering {s12} to {s13}.", "dplmc_gift_talk", []],
  ##Floris MTT End
  
	[anyone, "dplmc_gift_talk", [], "Very well! Have a nice trip.", "dplmc_gift_talk_farewell",[]], ##Floris MTT - was pt_dplmc_gift_caravan|party_tpl

	[anyone, "dplmc_gift_talk_farewell", [], "Thank you. Farewell!", "close_window", [(assign, "$g_leave_encounter", 1),]], ##Floris MTT - was pt_dplmc_gift_caravan|party_tpl

  [trp_dplmc_scout, "start",
  [], "Sire, I haven't finished my mission yet.", "dplmc_scout_talk", 
  []],

  [anyone|plyr,"dplmc_scout_talk",[
  ],
   "Ok, please go on.", "close_window",
   []],

  
  ##Chancellor
  [anyone,"start",
   [
    (eq, "$g_player_chancellor","$g_talk_troop"),
    ],
##nested diplomacy start+ Change "Milord" to "Milord/Milady"
"{Milord/Milady}?", "dplmc_chancellor_talk",[
##nested diplomacy end+
]],
   
  [anyone,"dplmc_chancellor_pretalk",
   [],
   "Do you need anything else, Sire?", "dplmc_chancellor_talk",[
 ]],
 
  [anyone|plyr,"dplmc_chancellor_talk",[
  ],
   "Let's talk about domestic policy.", "dplmc_chancellor_domestic_policy_options_ask",
##nested diplomacy start+
[
(try_begin),
	(neq, "$players_kingdom", "fac_player_supporters_faction"),
	(is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
	(try_for_range, ":slot_no", dplmc_slot_faction_policies_begin, dplmc_slot_faction_policies_end),
		(faction_get_slot, reg0, "$players_kingdom", ":slot_no"),
		(faction_set_slot, "fac_player_supporters_faction", ":slot_no",  reg0),
	(try_end),
(try_end),
##nested diplomacy end+
	]],
   
  [anyone,"dplmc_chancellor_domestic_policy_options_ask",
   [],
   "As you wish, Sire.", "dplmc_chancellor_domestic_policy_options",[
 ]],
 
	##select kingdom culture
	[anyone|plyr, "dplmc_chancellor_domestic_policy_options",
	[
	(is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),
	],
	##diplomacy start+ add apostrophe
	"I wish to select the kingdom's culture.", "dplmc_chancellor_kingdom_culture_ask",
	##diplomacy end+
	[]],
   
##diplomacy start+
#Don't enable this when the player is co-ruler of one of the original kingdoms.
[anyone, "dplmc_chancellor_kingdom_culture_ask",
[
(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
(assign, ":end_cond", active_npcs_end),
(try_for_range, ":lord", active_npcs_begin, ":end_cond"),
	(store_faction_of_troop, reg0, ":lord"),
	(eq, reg0, "$players_kingdom"),
	(troop_slot_eq, ":lord", slot_troop_original_faction, "$players_kingdom"),
	(assign, ":end_cond", ":lord"),
(try_end),
(lt, ":end_cond", active_npcs_end),
(str_store_faction_name, s11, "$players_kingdom"),
(call_script, "script_dplmc_print_cultural_word_to_sreg", ":end_cond", DPLMC_CULTURAL_TERM_LORD_PLURAL,0),
], "The {s0} of the {s11} would be unlikely to accept the imposition of other culture.", "dplmc_chancellor_talk",
[]],
##diplomacy end+
[anyone, "dplmc_chancellor_kingdom_culture_ask",
[
    (try_begin),
      (this_or_next|le, "$g_player_culture", 0),
      (neg|is_between, "$g_player_culture", kingdoms_begin, kingdoms_end), #Player Faction
      (str_store_string, s11, "@Your sovereignty has no specified culture"),
    (else_try),
      (store_sub, ":offset", "$g_player_culture", "fac_kingdom_1"),
      (val_add, ":offset", "str_kingdom_1_adjective"),
      (str_store_string, s11, ":offset"),   
      (str_store_string, s11, "@Your sovereignty culture is: {s11}"),
    (try_end),
   ],
   "{s11}. Do you want to change it?", "dplmc_chancellor_kingdom_culture_select",
   []],
   
 [anyone|plyr|repeat_for_factions, "dplmc_chancellor_kingdom_culture_select",
   [
    (store_repeat_object, ":faction_no"),
    (is_between, ":faction_no", kingdoms_begin, kingdoms_end), #Player Faction
##nested diplomacy start+
#To be eligible to establish a culture, you need some connection to it.
(assign, ":faction_allowed", 0),
(try_begin),
   #If it is the faction you left (or is otherwise somehow your faction)
   (this_or_next|eq, ":faction_no", "$players_oath_renounced_against_kingdom"),
   (eq, ":faction_no", "$players_kingdom"),
   (assign, ":faction_allowed", 1),
(else_try),
   #If it's the faction of the town you started in
   (is_between, "$g_starting_town", centers_begin, centers_end),
   (party_slot_eq, "$g_starting_town", slot_center_original_faction, ":faction_no"),
   (assign, ":faction_allowed", 1),
(else_try),
   #If you currently control any centers of that faction
   (assign, ":end_cond", walled_centers_end),
   (try_for_range, ":iter_no", walled_centers_begin, ":end_cond"),
      (store_faction_of_party, ":iter_faction", ":iter_no"),
      (eq, ":iter_faction", "$players_kingdom"),
      (party_slot_eq, ":iter_no", slot_center_original_faction, ":faction_no"),
#      (party_slot_eq, ":iter_no", slot_town_lord, "trp_player"),
      (assign, ":end_cond", ":iter_no"),
      (assign, ":faction_allowed", 1),
   (try_end),
   (eq, ":faction_allowed", 1),
(else_try),
   #If any of your lords come from that faction
   (assign, ":end_cond", heroes_end),
   (try_for_range, ":iter_no", heroes_begin, ":end_cond"),
      (store_faction_of_troop, ":iter_faction", ":iter_no"),
      (eq, ":iter_faction", "$players_kingdom"),
      (troop_slot_eq, ":iter_no", slot_troop_original_faction, ":faction_no"),
      (assign, ":end_cond", ":iter_no"),
      (assign, ":faction_allowed", 1),
   (try_end),
(try_end),
(eq, ":faction_allowed", 1),
##nested diplomacy end+
    (store_sub, ":offset", ":faction_no", "fac_kingdom_1"),
    (val_add, ":offset", "str_kingdom_1_adjective"),
    (str_store_string, s11, ":offset"),    
     ],
   "{s11}.", "dplmc_chancellor_pretalk",
   [
    (store_repeat_object, ":faction_no"),
    (assign, "$g_player_culture", ":faction_no"),
    (try_begin),
      (this_or_next|le, "$g_player_culture", 0),
      (neg|is_between, "$g_player_culture", kingdoms_begin, kingdoms_end), #Player Faction
      (str_store_string, s11, "@Sovereignty culture: None"),
    (else_try),
      (store_sub, ":offset", "$g_player_culture", "fac_kingdom_1"),
      (val_add, ":offset", "str_kingdom_1_adjective"),
      (str_store_string, s11, ":offset"),   
      (str_store_string, s11, "@Sovereignty culture: {s11}"),
    (try_end),
    (display_message, "@{s11}")
   ]],

   ##select kingdom culture
 [anyone|plyr, "dplmc_chancellor_kingdom_culture_select",
   [],
##diplomacy start+ Reword
#"None.", "dplmc_chancellor_pretalk",
"Favor no culture over others.", "dplmc_chancellor_pretalk",
##diplomacy end+
   [(assign, "$g_player_culture", 0),
   ]],
 
##diplomacy start+
[anyone|plyr, "dplmc_chancellor_kingdom_culture_select",
[],
"Make no change.", "dplmc_chancellor_pretalk",
[]],
##diplomacy end+

  [anyone|plyr,"dplmc_chancellor_domestic_policy_options",[
    (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
  ],
   "I require information about the domestic policy of another sovereignty.", "dplmc_chancellor_domestic_policy_info_ask",
   []],
   
  [anyone,"dplmc_chancellor_domestic_policy_info_ask",
   [],
   "About which sovereignty do you need information?", "dplmc_chancellor_domestic_policy_info_select",[
 ]],
 
  [anyone|plyr|repeat_for_factions,"dplmc_chancellor_domestic_policy_info_select",[
    (store_repeat_object, ":faction"),
    (is_between, ":faction", npc_kingdoms_begin, npc_kingdoms_end),
    (str_store_faction_name, s10, ":faction"),
  ],
   "{s10}.", "dplmc_chancellor_domestic_policy_info",
   [(store_repeat_object, "$diplomacy_var"),]],
   
  [anyone|plyr,"dplmc_chancellor_domestic_policy_info_select",[],
   "None.", "dplmc_chancellor_pretalk",
   []],
 
  [anyone,"dplmc_chancellor_domestic_policy_info",
   [
    (str_store_faction_name_link, s10, "$diplomacy_var"),
    (assign, ":string", "str_dplmc_neither_centralize_nor_decentralized"),
    (faction_get_slot, ":centralization", "$diplomacy_var", dplmc_slot_faction_centralization),
    (val_add, ":string", ":centralization"),
    (str_store_string, s4, ":string"),
    (str_store_string, s4, "@The goverment of the {s10} is {s4}."),

    (assign, ":string", "str_dplmc_neither_aristocratic_nor_plutocratic"),
    (faction_get_slot, ":aristocraty", "$diplomacy_var", dplmc_slot_faction_aristocracy),
    (val_add, ":string", ":aristocraty"),
    (str_store_string, s5, ":string"),
    (str_store_string, s5, "@The upper class society is {s5}."),
    
    (assign, ":string", "str_dplmc_mixture_serfs"),
    (faction_get_slot, ":serfdom", "$diplomacy_var", dplmc_slot_faction_serfdom),
    (val_add, ":string", ":serfdom"),
    (str_store_string, s6, ":string"),
    (str_store_string, s6, "@The people are {s6}."),
    
    (assign, ":string", "str_dplmc_mediocre_quality"),
    (faction_get_slot, ":quality", "$diplomacy_var", dplmc_slot_faction_quality),
    (val_add, ":string", ":quality"),
    (str_store_string, s7, ":string"),  
    (str_store_string, s7, "@The troops have {s7}."),     

	##nested diplomacy start+ add mercantilism
	(assign, ":string", "str_dplmc_neither_mercantilist_nor_laissez_faire"),
	(faction_get_slot, ":mercantilism", "$diplomacy_var", dplmc_slot_faction_mercantilism),
	(val_add, ":string", ":mercantilism"),
	(str_store_string, s0, ":string"),
	(str_store_string, s0, "@The government's approach to trade is {s0}."),
	],
	"{s4} {s5} {s6} {s7} {s0}", "dplmc_chancellor_domestic_policy_info_ask",[#<- dplmc+ added {s0}
	]],##nested diplomacy end+
 
  [anyone|plyr,"dplmc_chancellor_domestic_policy_options",[
    (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
  ],
   "Let's change our domestic policy.", "dplmc_chancellor_domestic_policy_ask",
   []],
   
  [anyone|plyr,"dplmc_chancellor_domestic_policy_options",[
  ],
   "Nevermind.", "dplmc_chancellor_pretalk",
   []],
     

  [anyone,"dplmc_chancellor_domestic_policy_ask",[
	(store_current_hours, ":current_hours"),
	##zParsifal 2011-10-07: Change the policy change interval from always 30 days to (Centralization * 5) + 30 days.
	(faction_get_slot, ":policy_time", "fac_player_supporters_faction", dplmc_slot_faction_centralization),
	(val_mul, ":policy_time", -5),
	(val_add, ":policy_time", 30),
	(val_clamp, ":policy_time", 15, 46),#This line should be unnecessary
	(val_mul, ":policy_time", 24),
	(val_sub, ":current_hours", ":policy_time"),
	(faction_get_slot, ":policy_time", "fac_player_supporters_faction", dplmc_slot_faction_policy_time),
	(this_or_next|ge, "$cheat_mode", 1), #Floris - allow cheating to change
	(ge, ":current_hours", ":policy_time"),    
    
    (assign, ":string", "str_dplmc_neither_centralize_nor_decentralized"),
    (faction_get_slot, ":centralization", "fac_player_supporters_faction", dplmc_slot_faction_centralization),
    (val_add, ":string", ":centralization"),
    (str_store_string, s4, ":string"),
    (str_store_string, s4, "@Our goverment is {s4}."),

    (assign, ":string", "str_dplmc_neither_aristocratic_nor_plutocratic"),
    (faction_get_slot, ":aristocraty", "fac_player_supporters_faction", dplmc_slot_faction_aristocracy),
    (val_add, ":string", ":aristocraty"),
    (str_store_string, s5, ":string"),
    (str_store_string, s5, "@The upper class society is {s5}."),
    
    (assign, ":string", "str_dplmc_mixture_serfs"),
    (faction_get_slot, ":serfdom", "fac_player_supporters_faction", dplmc_slot_faction_serfdom),
    (val_add, ":string", ":serfdom"),
    (str_store_string, s6, ":string"),
    (str_store_string, s6, "@Our people are {s6}."),
    
    (assign, ":string", "str_dplmc_mediocre_quality"),
    (faction_get_slot, ":quality", "fac_player_supporters_faction", dplmc_slot_faction_quality),
    (val_add, ":string", ":quality"),
    (str_store_string, s7, ":string"),  
    (str_store_string, s7, "@Our troops have {s7}."),    

	##nested diplomacy start+ add mercantilism
	(assign, ":string", "str_dplmc_neither_mercantilist_nor_laissez_faire"),
	(faction_get_slot, ":mercantilism", "fac_player_supporters_faction", dplmc_slot_faction_mercantilism),
	(val_add, ":string", ":mercantilism"),
	(str_store_string, s0, ":string"),
	(str_store_string, s0, "@Our approach to trade is {s0}."),
	],
	"{s4} {s5} {s6} {s7} {s0} What do you want to change?", "dplmc_chancellor_domestic_policy",#<- dplmc+ added {s0}
	[]],##nested diplomacy end+ 
   

  [anyone,"dplmc_chancellor_domestic_policy_ask",[ 
    (assign, ":string", "str_dplmc_neither_centralize_nor_decentralized"),
    (faction_get_slot, ":centralization", "fac_player_supporters_faction", dplmc_slot_faction_centralization),
    (val_add, ":string", ":centralization"),
    (str_store_string, s4, ":string"),
    (str_store_string, s4, "@Our goverment is {s4}."),

    (assign, ":string", "str_dplmc_neither_aristocratic_nor_plutocratic"),
    (faction_get_slot, ":aristocraty", "fac_player_supporters_faction", dplmc_slot_faction_aristocracy),
    (val_add, ":string", ":aristocraty"),
    (str_store_string, s5, ":string"),
    (str_store_string, s5, "@The upper class society is {s5}."),
    
    (assign, ":string", "str_dplmc_mixture_serfs"),
    (faction_get_slot, ":serfdom", "fac_player_supporters_faction", dplmc_slot_faction_serfdom),
    (val_add, ":string", ":serfdom"),
    (str_store_string, s6, ":string"),
    (str_store_string, s6, "@Our people are {s6}."),
    
    (assign, ":string", "str_dplmc_mediocre_quality"),
    (faction_get_slot, ":quality", "fac_player_supporters_faction", dplmc_slot_faction_quality),
    (val_add, ":string", ":quality"),
    (str_store_string, s7, ":string"),  
    (str_store_string, s7, "@Our troops have {s7}."),  
	
	##nested diplomacy start+ add mercantilism
	(assign, ":string", "str_dplmc_neither_mercantilist_nor_laissez_faire"),
	(faction_get_slot, ":mercantilism", "fac_player_supporters_faction", dplmc_slot_faction_mercantilism),
	(val_add, ":string", ":mercantilism"),
	(str_store_string, s0, ":string"),
	(str_store_string, s0, "@Our approach to trade is {s0}."),
	##nested diplomacy end+

	(store_current_hours, ":current_hours"),
	##zParsifal 2011-10-07: Change the policy change interval from always 30 days to (Centralization * 5) + 30 days.
	(store_mul, reg1, ":centralization", -5),#Use reg1 for the number of days you have to wait, to display further below.
	(val_add, reg1, 30),
	(val_clamp, reg1, 15, 46),#This line should be unnecessary
	(store_mul, ":policy_time", reg1, 24),
	(val_sub, ":current_hours", ":policy_time"),
	(faction_get_slot, ":policy_time", "fac_player_supporters_faction", dplmc_slot_faction_policy_time),
	(store_sub, ":wait_hours" , ":policy_time", ":current_hours"),
	(store_div, ":wait_days", ":wait_hours", 24),
	(store_mod, ":wait_mod", ":wait_hours", 24),
	(try_begin),
	(lt, ":wait_mod", 0),
	(val_add, ":wait_days", 1),
	(try_end),
	(assign, reg0, ":wait_days"),
	],
	##nested diplomacy start+
	"{s4} {s5} {s6} {s7} {s0} We can only change the policy every {reg1} days, the people have to get used to it. We have to wait {reg0} days.",#<- dplmc+ added {s0}
	 "dplmc_chancellor_pretalk",[]],
	##nested diplomacy end+

   
  [anyone|plyr,"dplmc_chancellor_domestic_policy",
  [
    (faction_get_slot, ":serfdom", "fac_player_supporters_faction", dplmc_slot_faction_serfdom),
    (lt, ":serfdom", 3),
  ],
   "Bring more people into serfdom.", "dplmc_chancellor_domestic_policy_confirm",
   [
    (faction_get_slot, ":serfdom", "fac_player_supporters_faction", dplmc_slot_faction_serfdom),
    (val_add, ":serfdom", 1),
    (faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_serfdom ,":serfdom"),
   ]],   
   
  [anyone|plyr,"dplmc_chancellor_domestic_policy",
  [
    (faction_get_slot, ":serfdom", "fac_player_supporters_faction", dplmc_slot_faction_serfdom),
    (gt, ":serfdom", -3),
  ],
   "I want more freedom for the people.", "dplmc_chancellor_domestic_policy_confirm",
   [
    (faction_get_slot, ":serfdom", "fac_player_supporters_faction", dplmc_slot_faction_serfdom),
    (val_sub, ":serfdom", 1),
    (faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_serfdom ,":serfdom"),
   ]], 
   
  [anyone|plyr,"dplmc_chancellor_domestic_policy",
  [
    (faction_get_slot, ":centralization", "fac_player_supporters_faction", dplmc_slot_faction_centralization),
    (lt, ":centralization", 3),
  ],
   "Let's centralize the decisions.", "dplmc_chancellor_domestic_policy_confirm",
   [
    (faction_get_slot, ":centralization", "fac_player_supporters_faction", dplmc_slot_faction_centralization),
    (val_add, ":centralization", 1),
    (faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_centralization,  ":centralization"),
   ]],
   
  [anyone|plyr,"dplmc_chancellor_domestic_policy",
  [
    (faction_get_slot, ":centralization", "fac_player_supporters_faction", dplmc_slot_faction_centralization),
    (gt, ":centralization", -3),
  ],
	#diplomacy start+
	#changed "Give the lords more authority to decide" to "Grant increased autonomy to local regions"
	"Grant increased autonomy to local authorities.", "dplmc_chancellor_domestic_policy_confirm",
	#diplomacy end+
   [
     (faction_get_slot, ":centralization", "fac_player_supporters_faction", dplmc_slot_faction_centralization),
     (val_sub, ":centralization", 1),
     (faction_set_slot,  "fac_player_supporters_faction", dplmc_slot_faction_centralization, ":centralization"),
   ]],   
   
  [anyone|plyr,"dplmc_chancellor_domestic_policy",
  [
    (faction_get_slot, ":quality", "fac_player_supporters_faction", dplmc_slot_faction_quality),
    (lt, ":quality", 3),
  ],
   "I prefer quality troops to many troops.", "dplmc_chancellor_domestic_policy_confirm",
   [
     (faction_get_slot, ":quality", "fac_player_supporters_faction", dplmc_slot_faction_quality),
     (val_add, ":quality", 1),
     (faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_quality, ":quality"),
   ]],
   
  [anyone|plyr,"dplmc_chancellor_domestic_policy",
  [
    (faction_get_slot, ":quality", "fac_player_supporters_faction", dplmc_slot_faction_quality),
    (gt, ":quality", -3),
  ],
	#diplomacy start+
	"Quantity has a quality of its own.  I prefer many troops to few quality troops.", "dplmc_chancellor_domestic_policy_confirm",
	#diplomacy start+
   [
     (faction_get_slot, ":quality", "fac_player_supporters_faction", dplmc_slot_faction_quality),
     (val_sub, ":quality", 1),
     (faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_quality, ":quality"),
   ]],   
   
  [anyone|plyr,"dplmc_chancellor_domestic_policy",
  [
    (faction_get_slot, ":aristocraty", "fac_player_supporters_faction", dplmc_slot_faction_aristocracy),
    (lt, ":aristocraty", 3),
  ],
   "Give the nobles more power.", "dplmc_chancellor_domestic_policy_confirm",
   [
     (faction_get_slot, ":aristocraty", "fac_player_supporters_faction", dplmc_slot_faction_aristocracy),
     (val_add, ":aristocraty", 1),
     (faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_aristocracy,  ":aristocraty"),
   ]],

  [anyone|plyr,"dplmc_chancellor_domestic_policy",
  [
    (faction_get_slot, ":aristocraty", "fac_player_supporters_faction", dplmc_slot_faction_aristocracy),
    (gt, ":aristocraty", -3),
  ],
	#diplomacy start+
	"Give the merchants and trade guilds more power.", "dplmc_chancellor_domestic_policy_confirm",#dplmc+ edited
	#diplomacy end+
   [
     (faction_get_slot, ":aristocraty", "fac_player_supporters_faction", dplmc_slot_faction_aristocracy),
     (val_sub, ":aristocraty", 1),
     (faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_aristocracy,  ":aristocraty"),
   ]],

	##diplomacy start+ add mercantilism
	[anyone|plyr,"dplmc_chancellor_domestic_policy",
	[
	(faction_get_slot, ":mercantilism", "fac_player_supporters_faction", dplmc_slot_faction_mercantilism),
	(lt, ":mercantilism", 3),
	],
	"Manage the economy more actively to increase production and maximize exports.", "dplmc_chancellor_domestic_policy_confirm",
	[
	(faction_get_slot, ":mercantilism", "fac_player_supporters_faction", dplmc_slot_faction_mercantilism),
	(val_add, ":mercantilism", 1),
	(faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_mercantilism,  ":mercantilism"),
	]],

	[anyone|plyr,"dplmc_chancellor_domestic_policy",
	[
	(faction_get_slot, ":mercantilism", "fac_player_supporters_faction", dplmc_slot_faction_mercantilism),
	(gt, ":mercantilism", -3),
	],
	"Reduce the crown's role in managing industry and commerce.", "dplmc_chancellor_domestic_policy_confirm",
	[
	(faction_get_slot, ":mercantilism", "fac_player_supporters_faction", dplmc_slot_faction_mercantilism),
	(val_sub, ":mercantilism", 1),
	(faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_mercantilism,  ":mercantilism"),
	]],
	##diplomacy end+
   
  [anyone|plyr,"dplmc_chancellor_domestic_policy",
  [],
   "Never mind.", "dplmc_chancellor_pretalk",
   []],
   
  [anyone,"dplmc_chancellor_domestic_policy_confirm",
   [],
   "I will initiate all necessary steps.", "dplmc_chancellor_pretalk",[
    (store_current_hours, ":current_hours"),
    (faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_policy_time, ":current_hours"),
##diplomacy start+
(try_begin),
	(neq, "$players_kingdom", "fac_player_supporters_faction"),
	(is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
	(try_for_range, ":slot_no", dplmc_slot_faction_policies_begin, dplmc_slot_faction_policies_end),
	   (faction_get_slot, reg0, "fac_player_supporters_faction", ":slot_no"),
		(faction_set_slot, "$players_kingdom", ":slot_no",  reg0),
	(try_end),
(try_end),
##diplomacy end+
]],


  [anyone|plyr,"dplmc_chancellor_talk",[
                            ],
   "I require information about a lord.", "dplmc_chancellor_info_kingdom_ask",[]],
   
  [anyone,"dplmc_chancellor_info_kingdom_ask",
   [],
   "Where is he from?", "dplmc_chancellor_info_kingdom_select",[
 ]],
 
  [anyone|plyr|repeat_for_factions, "dplmc_chancellor_info_kingdom_select", 
   [
   (store_repeat_object, ":faction_no"),
   (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
   (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
   (str_store_faction_name, s11, ":faction_no"),
   ],
   "{s11}.", "dplmc_chancellor_info_person_ask",
  [
   (store_repeat_object, "$g_faction_selected"),
  ]],
  
  [anyone|plyr, "dplmc_chancellor_info_kingdom_select", 
   [
   ],
   "Never mind.", "dplmc_chancellor_pretalk",[
 ]],
 
  [anyone,"dplmc_chancellor_info_person_ask",
   [],
   "About which lord do you want information?", "dplmc_chancellor_info_person_select",[
 ]],
 
   [anyone|plyr|repeat_for_troops, "dplmc_chancellor_info_person_select",
   [
    (store_repeat_object, ":troop_no"),
    (neq, "$g_talk_troop", ":troop_no"),
    (is_between, ":troop_no", active_npcs_begin, kingdom_ladies_end),
    (neq, ":troop_no", "trp_player"),
    (neg|faction_slot_eq, "$g_faction_selected", slot_faction_leader, ":troop_no"),
    (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
    (store_troop_faction, ":faction_no", ":troop_no"),
    (eq, "$g_faction_selected", ":faction_no"),
    (str_store_troop_name, s1, ":troop_no"),
   
   ],"{s1}.", "dplmc_chancellor_info_person",
   [
      (store_repeat_object, "$lord_selected"),
   ]],
   
  [anyone|plyr, "dplmc_chancellor_info_person_select", 
   [
   ],
   "About no one.", "dplmc_chancellor_pretalk",[
 ]], 
   
  [anyone,"dplmc_chancellor_info_person",
   [
    (call_script, "script_dplmc_troop_political_notes_to_s47", "$lord_selected"),
   ],
   "{s47}", "dplmc_chancellor_pretalk",[
 ]],
 
  [anyone|plyr,"dplmc_chancellor_talk",[
							(faction_get_slot, ":political_issue", "$players_kingdom", slot_faction_political_issue),
							(is_between, ":political_issue", centers_begin, centers_end),
							(str_store_party_name, s4, ":political_issue"),
                            ],
   "What's the mood of the lords regarding the fief of {s4}?", "dplmc_chancellor_cur_stance",[]],
   
  [anyone, "dplmc_chancellor_cur_stance", 
   [
		 ##diplomacy start+ Handle player is co-ruler of kingdom
	(assign, ":alt_faction", "fac_player_supporters_faction"),
	(try_begin),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":alt_faction", "$players_kingdom"),
	(try_end),
	##diplomacy end+
	(try_for_parties, ":party_no"),
	(party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
	(store_faction_of_party, ":faction_no", ":party_no"),
	##diplomacy start+
	(this_or_next|eq, ":alt_faction", ":faction_no"),
	##diplomacy end+
	(eq, "fac_player_supporters_faction", ":faction_no"),
	(party_stack_get_troop_id, ":party_leader", ":party_no", 0),
	(is_between, ":party_leader", heroes_begin, heroes_end),
	(troop_set_slot, ":party_leader", dplmc_slot_troop_political_stance, 0),
	(try_end),

	(try_for_parties, ":party_no"),
	(party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
	(store_faction_of_party, ":faction_no", ":party_no"),
	##diplomacy start+
	(this_or_next|eq, ":alt_faction", ":faction_no"),
	##diplomacy end+
	(eq, "fac_player_supporters_faction", ":faction_no"),
	(party_stack_get_troop_id, ":party_leader", ":party_no", 0),
	(is_between, ":party_leader", heroes_begin, heroes_end),
	(troop_get_slot, ":fav_troop", ":party_leader", slot_troop_stance_on_faction_issue),
	(is_between, ":fav_troop", heroes_begin, heroes_end),
	(troop_get_slot, ":stance", ":fav_troop", dplmc_slot_troop_political_stance),
	(val_add, ":stance", 1),
	(troop_set_slot, ":fav_troop", dplmc_slot_troop_political_stance, ":stance"),
	(try_end),

	(assign, ":report", 0),
	(str_store_string, s10, "@According  to the report of our spies"),
	(try_for_parties, ":party_no"),
	(party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
	(store_faction_of_party, ":faction_no", ":party_no"),
	##diplomacy start+
	(this_or_next|eq, ":alt_faction", ":faction_no"),
	##diplomacy end+
	(eq, "fac_player_supporters_faction", ":faction_no"),
	(party_stack_get_troop_id, ":party_leader", ":party_no", 0),
	(is_between, ":party_leader", heroes_begin, heroes_end),
	(troop_get_slot, ":stance", ":party_leader", dplmc_slot_troop_political_stance),
	(try_begin),
	  (gt, ":stance", 0),
	  (str_store_troop_name, s9, ":party_leader"),
	  (assign, reg3, ":stance"),
	  (str_store_string, s10, "@{s10} {reg3} lords support {s9}."),
	  (assign, ":report", 1),
	(try_end),
	(try_end),
    
    (try_begin),
      (eq, ":report",0),
      (str_store_string, s10, "@Sorry, currently I can't provide any information about the lord's mood, our spies haven't reported back yet."),
    (try_end),
   ],
   "{s10}", "dplmc_chancellor_pretalk",[
 ]],

 

  ##send messenger to another lord
   [anyone|plyr, "dplmc_chancellor_talk",
   [],
   "Please send a message to another lord.", "dplmc_chancellor_message_ask_type",
   []], 
   
  [anyone, "dplmc_chancellor_message_ask_type", 
   [
   ],
   "To whom do you like to send the message?", "dplmc_chancellor_message_lord_select",[
 ]],
 

    ##select the lord who shall receive the message to hand over
   [anyone|plyr|repeat_for_troops, "dplmc_chancellor_message_lord_select",
   [
    (store_repeat_object, ":troop_no"),
    (neq, "$g_talk_troop", ":troop_no"),
    (is_between, ":troop_no", active_npcs_begin, kingdom_ladies_end),
    (neq, ":troop_no", "trp_player"),
    (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
    (store_troop_faction, ":faction_no", ":troop_no"),
    (eq, "$players_kingdom", ":faction_no"),
    (str_store_troop_name, s1, ":troop_no"),
   
   ],"{s1}.", "dplmc_chancellor_message_ask",
   [
      (store_repeat_object, "$lord_selected"),
   ]], 
   
   [anyone|plyr, "dplmc_chancellor_message_lord_select",
   [],"Nevermind.", "dplmc_chancellor_pretalk",
   []], 
 
  [anyone|plyr, "dplmc_chancellor_gift_lord_select", 
   [
   ],
   "I can't think of anyone.", "dplmc_chancellor_pretalk",[
 ]],
 
  [anyone, "dplmc_chancellor_message_ask", 
   [
    (str_store_troop_name, s6, "$lord_selected"),
	##diplomacy start+ Save gender to reg4
	(assign, reg4, 0),
	(try_begin),
	(call_script, "script_cf_dplmc_troop_is_female", "$lord_selected"),
	(assign, reg4, 1),
	(try_end),
	##diplomacy end+
   ],
   "What do you want to tell {s6}?", "dplmc_chancellor_message_select",[
 ]], 
 
    ##ask to accompany to another lord
   [anyone|plyr, "dplmc_chancellor_message_select",
   [
   ],
	##diplomacy start+ make gender correct using reg4 (set above)
	"Ask {reg4?her:him} if {reg4?she:he} is willing to accompany me in the field.", "dplmc_chancellor_message_lord_ask",
	##diplomacy end+
   [
    (assign, "$temp", spai_accompanying_army),
    (assign, "$temp_2", "p_main_party"),
   ]], 
   
	##ask to goto a center
	[anyone|plyr, "dplmc_chancellor_message_select",
	[
	],
	##diplomacy start+ make gender correct using reg4 (set above)
	"Ask {reg4?her:him} if {reg4?she:he} is willing to go to a location.", "dplmc_chancellor_message_goto_lord_ask",
	##diplomacy end+
	[
	(assign, "$temp", spai_holding_center),
	]],

	##ask to patrol a center
	[anyone|plyr, "dplmc_chancellor_message_select",
	[
	],
	##diplomacy start+ make gender correct using reg4 (set above)
	"Ask {reg4?her:him} if {reg4?she:he} is willing to patrol a location.", "dplmc_chancellor_message_goto_lord_ask",
	##diplomacy end+
	[
	(assign, "$temp", spai_patrolling_around_center),
	]],

	##ask to flee to a center
	[anyone|plyr, "dplmc_chancellor_message_select",
	[
	],
	##diplomacy start+ make gender correct using reg4 (set above)
	"Ask {reg4?her:him} if {reg4?she:he} is willing to flee to a location.", "dplmc_chancellor_message_goto_lord_ask",
	##diplomacy end+
	[
	(assign, "$temp", spai_retreating_to_center),
	]],

	##ask to besiege a center
	[anyone|plyr, "dplmc_chancellor_message_select",
	[
	],
	##diplomacy start+ make gender correct using reg4 (set above)
	"Ask {reg4?her:him} if {reg4?she:he} is willing to besiege a location.", "dplmc_chancellor_message_goto_lord_ask",
	##diplomacy end+
	[
	(assign, "$temp", spai_besieging_center),
	]],

	##ask to besiege a center
	[anyone|plyr, "dplmc_chancellor_message_select",
	[
	],
	##diplomacy start+ make gender correct using reg4 (set above)
	"Ask {reg4?her:him} if {reg4?she:he} is willing to raid around a location.", "dplmc_chancellor_message_goto_lord_ask",
	##diplomacy end+
	[
	(assign, "$temp", spai_raiding_around_center),
	]],
   
   [anyone|plyr, "dplmc_chancellor_message_select",
   [
   ],
   "Never mind.", "dplmc_chancellor_pretalk",
   []], 
   
	[anyone,"dplmc_chancellor_message_goto_lord_ask", [],
	##diplomacy start+ make gender correct using reg4 (set above)
	"Where do you order {reg4?her:him}?", "dplmc_chancellor_message_order_details",[]],
	##diplomacy end+

  [anyone|plyr|repeat_for_parties, "dplmc_chancellor_message_order_details",
   [
     (store_repeat_object, ":party_no"),
     (store_faction_of_party, ":party_faction", ":party_no"),
     (store_relation, ":relation", ":party_faction", "$players_kingdom"),
     (assign, ":continue", 0),
     (try_begin),
       (this_or_next|eq, "$temp", spai_retreating_to_center),
         (eq, "$temp", spai_holding_center),
       (try_begin),
         (this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_castle),
			(party_slot_eq, ":party_no", slot_party_type, spt_town),
         (eq, ":party_faction", "$players_kingdom"),
         (assign, ":continue", 1),
       (try_end),
     (else_try),
       (eq, "$temp", spai_raiding_around_center),
       (try_begin),
         (party_slot_eq, ":party_no", slot_party_type, spt_village),
         (lt, ":relation", 0),
         (assign, ":continue", 1),
       (try_end),
     (else_try),
       (eq, "$temp", spai_besieging_center),
       (try_begin),
         (this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_castle),
			(party_slot_eq, ":party_no", slot_party_type, spt_town),
		 (party_slot_eq, ":party_no", slot_center_is_besieged_by, -1),
         (lt, ":relation", 0),
         (assign, ":continue", 1),
       (try_end),
	   
	   
     (else_try),
       (eq, "$temp", spai_patrolling_around_center),
       (try_begin),
         (eq, ":party_faction", "$players_kingdom"),
         (is_between, ":party_no", centers_begin, centers_end),
         (assign, ":continue", 1),
	   (else_try),	 
         (is_between, ":party_no", centers_begin, centers_end),
	   
		 (store_distance_to_party_from_party, ":distance", ":party_no", "p_main_party"),
		 (le, ":distance", 25),
         (assign, ":continue", 1),
		 
       (try_end),
     (try_end),
     (eq, ":continue", 1),
     (neq, ":party_no", "$g_encountered_party"),
     (str_store_party_name, s1, ":party_no")],
   "{s1}", "dplmc_chancellor_message_lord_ask",
   [
    (store_repeat_object, "$temp_2"),
	(store_current_hours, ":hours"),
	(party_set_slot, "$g_talk_troop_party", slot_party_following_orders_of_troop, "trp_kingdom_heroes_including_player_begin"),
	(party_set_slot, "$g_talk_troop_party", slot_party_orders_type, "$temp"),
	(party_set_slot, "$g_talk_troop_party", slot_party_orders_object, "$temp_2"),
	(party_set_slot, "$g_talk_troop_party", slot_party_orders_time, ":hours"),
	 
     ]],
   
   [anyone|plyr, "dplmc_chancellor_message_order_details",
   [
   ],
   "Nowhere.", "dplmc_chancellor_pretalk",
   []], 
   
   
  [anyone, "dplmc_chancellor_message_lord_ask", 
   [
	##diplomacy start+ make center correct
	(assign, reg4, 0),
	(try_begin),
		(call_script, "script_cf_dplmc_troop_is_female", "$lord_selected"),
		(assign, reg4, 1),
	(try_end),
	##diplomacy end+
	(eq, "$temp", spai_accompanying_army),
	(str_store_troop_name, s11, "$lord_selected"),
	],
	##diplomacy start+ make gender correct using reg4 (set above)
	"Of course, I will send a messenger to {s11} and ask {reg4?her:him} if {reg4?she:he} is willing to accompany you in the field.", "dplmc_message_send_confirm",[
	##diplomacy end+
	]],
 
	[anyone, "dplmc_chancellor_message_lord_ask",
	[
	(eq, "$temp", spai_holding_center),
	(str_store_troop_name, s11, "$lord_selected"),
	(str_store_party_name, s12, "$temp_2"),
	],
	##diplomacy start+ make gender correct using reg4 (set above)
	"Of course, I will send a messenger to {s11} and ask {reg4?her:him} if {reg4?she:he} is willing to go to {s12}.", "dplmc_message_send_confirm",[
	##diplomacy end+
	]],

	[anyone, "dplmc_chancellor_message_lord_ask",
	[
	(eq, "$temp", spai_patrolling_around_center),
	(str_store_troop_name, s11, "$lord_selected"),
	(str_store_party_name, s12, "$temp_2"),
	],
	##diplomacy start+ make gender correct using reg4 (set above)
	"Of course, I will send a messenger to {s11} and ask {reg4?her:him} if {reg4?she:he} is willing to patrol around {s12}.", "dplmc_message_send_confirm",[
	##diplomacy end+
	]],

	[anyone, "dplmc_chancellor_message_lord_ask",
	[
	(eq, "$temp", spai_retreating_to_center),
	(str_store_troop_name, s11, "$lord_selected"),
	(str_store_party_name, s12, "$temp_2"),
	],
	##diplomacy start+ make gender correct using reg4 (set above)
	"Of course, I will send a messenger to {s11} and ask {reg4?her:him} if {reg4?she:he} is willing to retreat to {s12}.", "dplmc_message_send_confirm",[
	##diplomacy end+
	]],

	[anyone, "dplmc_chancellor_message_lord_ask",
	[
	(eq, "$temp", spai_besieging_center),
	(str_store_troop_name, s11, "$lord_selected"),
	(str_store_party_name, s12, "$temp_2"),
	],
	##diplomacy start+ make gender correct using reg4 (set above)
	"Of course, I will send a messenger to {s11} and ask {reg4?her:him} if {reg4?she:he} is willing to besiege {s12}.", "dplmc_message_send_confirm",[
	##diplomacy end+
	]],

	[anyone, "dplmc_chancellor_message_lord_ask",
	[
	(eq, "$temp", spai_raiding_around_center),
	(str_store_troop_name, s11, "$lord_selected"),
	(str_store_party_name, s12, "$temp_2"),
	],
	##diplomacy start+ make gender correct using reg4 (set above)
	"Of course, I will send a messenger to {s11} and ask {reg4?her:him} if {reg4?she:he} is willing to raid around {s12}.", "dplmc_message_send_confirm",[
	##diplomacy end+
	]],
 
  [anyone|plyr, "dplmc_message_send_confirm", 
   [
   ],
   "Thank you.", "dplmc_chancellor_pretalk",[  
    (call_script, "script_dplmc_send_messenger_to_troop", "$lord_selected", "$temp", "$temp_2"),	
 ]],
 
  [anyone|plyr, "dplmc_message_send_confirm", 
   [
   ],
   "I changed my mind.", "dplmc_chancellor_pretalk",[
 ]],

   
  ##send gift
   [anyone|plyr, "dplmc_chancellor_talk",
   [],
   "Please send a gift.", "dplmc_chancellor_gift_ask_where",
   []], 

   [anyone, "dplmc_chancellor_gift_ask_where",
   [
    (store_troop_gold, ":gold", "trp_household_possessions"),
    (le, ":gold", 50),
   ],
   "We don't have enough money in our treasury to send a gift! It will cost us 50 denars to send a gift.", "dplmc_chancellor_pretalk",
   []],  

   [anyone, "dplmc_chancellor_gift_ask_where",
   [
    (store_troop_gold, ":gold", "trp_household_possessions"),
    (ge, ":gold", 50),
   ],
   "Sending a gift will cost us 50 denars. I will withdraw the money from the treasury. Do you want to send your gift to a person or a settlement?", "dplmc_chancellor_gift_where",
   []],  
   
   [anyone|plyr, "dplmc_chancellor_gift_where",
   [],
   "To a person.", "dplmc_chancellor_gift_ask_person",
   []], 
   
   [anyone|plyr, "dplmc_chancellor_gift_where",
   [],
   "To a settlement.", "dplmc_chancellor_center_gift_ask_type",
   []], 
   
   [anyone|plyr, "dplmc_chancellor_gift_where",
   [],
   "Nowhere.", "dplmc_chancellor_pretalk",
   []],  
   
  [anyone, "dplmc_chancellor_center_gift_ask_type", 
   [
   ],
   "I recommend to send 300 units of smoked fish, cheese, or honey. If we have enough in our household I will induce a servant to deliver it.", "dplmc_chancellor_center_gift_select",[
 ]],
 
  ##send fish
  [anyone|plyr, "dplmc_chancellor_center_gift_select", 
   [
   	(troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),
   	(assign, ":amount", 0),
	  (try_for_range, ":inventory_slot", 0, ":capacity"),
		  (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
		  (eq, ":item", "itm_trade_smoked_fish"),
		  (troop_inventory_slot_get_item_amount, ":tmp_amount", "trp_household_possessions", ":inventory_slot"),
		  (val_add, ":amount", ":tmp_amount"),
    (try_end),
	  (ge, ":amount", 300),
   ],
   "Send some fish.", "dplmc_chancellor_center_gift_kingdom_ask",[
   (assign, "$diplomacy_var", "itm_trade_smoked_fish"),
(assign, "$diplomacy_var2", 300),
]],
 
  ##send cheese
  [anyone|plyr, "dplmc_chancellor_center_gift_select", 
   [
    (troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),
	  (assign, ":amount", 0),
    (try_for_range, ":inventory_slot", 0, ":capacity"),
		  (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
		  (eq, ":item", "itm_trade_cheese"),
		  (troop_inventory_slot_get_item_amount, ":tmp_amount", "trp_household_possessions", ":inventory_slot"),
      (val_add, ":amount", ":tmp_amount"),
		(try_end),
	  (ge, ":amount", 300),
   ],
   "Send some cheese.", "dplmc_chancellor_center_gift_kingdom_ask",[
   (assign, "$diplomacy_var", "itm_trade_cheese"),
(assign, "$diplomacy_var2", 300),
]],
 
  ##send honey
  [anyone|plyr, "dplmc_chancellor_center_gift_select", 
   [
    (troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),
	  (assign, ":amount", 0),    
	  (try_for_range, ":inventory_slot", 0, ":capacity"),
		  (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
		  (eq, ":item", "itm_trade_honey"),
		  (troop_inventory_slot_get_item_amount, ":tmp_amount", "trp_household_possessions", ":inventory_slot"),
      (val_add, ":amount", ":tmp_amount"),
		(try_end),
	  (ge, ":amount", 300),
   ],
   "Send some honey.", "dplmc_chancellor_center_gift_kingdom_ask",[
   (assign, "$diplomacy_var", "itm_trade_honey"),
(assign, "$diplomacy_var2", 300),
]],
 
  [anyone|plyr, "dplmc_chancellor_center_gift_select", 
   [
   ],
   "Never mind.", "dplmc_chancellor_pretalk",[
 ]],
   
  [anyone, "dplmc_chancellor_center_gift_kingdom_ask", 
   [
   ],
   "Where is the settlement?", "dplmc_chancellor_center_gift_kingdom_select",[
 ]],
 
  [anyone|plyr|repeat_for_factions, "dplmc_chancellor_center_gift_kingdom_select", 
   [
   (store_repeat_object, ":faction_no"),
   (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
   (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
   (str_store_faction_name, s11, ":faction_no"),
   ],
   "In {s11}.", "dplmc_chancellor_center_gift_lord_ask",
  [
   (store_repeat_object, "$g_faction_selected"),
  ]],
  
  [anyone|plyr, "dplmc_chancellor_center_gift_kingdom_select", 
   [
   ],
   "Never mind.", "dplmc_chancellor_pretalk",[
 ]],

##nested diplomacy start+ Disable gift-sending during a war with a nation that doesn't recognize you
[anyone, "dplmc_chancellor_center_gift_lord_ask",
[
(is_between, "$g_faction_selected", npc_kingdoms_begin, npc_kingdoms_end),
(neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
(store_relation, reg0, "$players_kingdom", "$g_faction_selected"),
(lt, reg0, 0),
(neg|faction_slot_ge, "$g_faction_selected", slot_faction_recognized_player, 1),
],
"Given that we are currently at war with the {s11} and they do not officially recognize your legitimacy, any messengers we sent would run the risk of being hanged as bandits.", "dplmc_chancellor_pretalk",[
]],
##nested diplomacy end+
  [anyone, "dplmc_chancellor_center_gift_lord_ask", 
   [
   ],
   "To which settlement do you like to send the gift?", "dplmc_chancellor_center_gift_lord_select",[
 ]], 
 
    ##select the lord who shall receive the gift to hand over
   [anyone|plyr|repeat_for_parties, "dplmc_chancellor_center_gift_lord_select",
   [
     (store_repeat_object, ":party_no"),
     (this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_town),
     (party_slot_eq, ":party_no", slot_party_type, spt_village),
     (store_faction_of_party, ":faction_no", ":party_no"),
     (eq, ":faction_no", "$g_faction_selected"),
     (str_store_party_name, s11, ":party_no"),
   
   ],"{s11}.", "dplmc_chancellor_center_gift_send_ask",
   [
      (store_repeat_object, "$lord_selected"),
   ]], 
   
  [anyone|plyr, "dplmc_chancellor_center_gift_lord_select", 
   [
   ],
   "I changed my mind.", "dplmc_chancellor_pretalk",[
 ]],
 
  [anyone, "dplmc_chancellor_center_gift_send_ask", 
   [
      (str_store_item_name,s6,"$diplomacy_var"),
      (str_store_party_name, s11, "$lord_selected"),
   ],
   "I will send a servant with the {s6} to {s11}.", "dplmc_chancellor_center_gift_send_confirm",[
   
 ]],
 
[anyone|plyr, "dplmc_chancellor_center_gift_send_confirm",
[
],
"Thank you.", "dplmc_chancellor_pretalk",[
(call_script, "script_dplmc_send_gift_to_center", "$lord_selected", "$diplomacy_var", "$diplomacy_var2"),
]],
 
  [anyone|plyr, "dplmc_chancellor_center_gift_send_confirm", 
   [
   ],
   "Never mind.", "dplmc_chancellor_pretalk",[
 ]],
 

    ##send gift to person
   [anyone, "dplmc_chancellor_gift_ask_person",
   [],
   "Do you want to send your gift to a lady or to a lord?.", "dplmc_chancellor_gift_lady_or_lord",
   []], 
   

  ##send gift to a lord
   [anyone|plyr, "dplmc_chancellor_gift_lady_or_lord",
   [],
   "Please send a gift to a lord.", "dplmc_chancellor_gift_ask_type",
   []], 
   
 
  [anyone, "dplmc_chancellor_gift_ask_type", 
   [
   ],
   "I recommend to send 150 units of Ale, Wine or Oil. If we have enough in our household I will induce a servant to deliver it.", "dplmc_chancellor_gift_select",[
 ]],
 
  ##send ale
  [anyone|plyr, "dplmc_chancellor_gift_select", 
   [
   	(troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),
   	(assign, ":amount", 0),
	  (try_for_range, ":inventory_slot", 0, ":capacity"),
		  (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
		  (eq, ":item", "itm_trade_ale"),
		  (troop_inventory_slot_get_item_amount, ":tmp_amount", "trp_household_possessions", ":inventory_slot"),
		  (val_add, ":amount", ":tmp_amount"),
    (try_end),
	  (ge, ":amount", 150),
   ],
   "Send some ale.", "dplmc_chancellor_gift_kingdom_ask",[
   (assign, "$diplomacy_var", "itm_trade_ale"),
(assign, "$diplomacy_var2", 150),
 ]],
 
  ##send wine
  [anyone|plyr, "dplmc_chancellor_gift_select", 
   [
    (troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),
	  (assign, ":amount", 0),
    (try_for_range, ":inventory_slot", 0, ":capacity"),
		  (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
		  (eq, ":item", "itm_trade_wine"),
		  (troop_inventory_slot_get_item_amount, ":tmp_amount", "trp_household_possessions", ":inventory_slot"),
      (val_add, ":amount", ":tmp_amount"),
		(try_end),
	  (ge, ":amount", 150),
   ],
   "Send some wine.", "dplmc_chancellor_gift_kingdom_ask",[
   (assign, "$diplomacy_var", "itm_trade_wine"),
(assign, "$diplomacy_var2", 150),
 ]],
 
  ##send oil
  [anyone|plyr, "dplmc_chancellor_gift_select", 
   [
    (troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),
	  (assign, ":amount", 0),    
	  (try_for_range, ":inventory_slot", 0, ":capacity"),
		  (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
		  (eq, ":item", "itm_trade_oil"),
		  (troop_inventory_slot_get_item_amount, ":tmp_amount", "trp_household_possessions", ":inventory_slot"),
      (val_add, ":amount", ":tmp_amount"),
		(try_end),
	  (ge, ":amount", 150),
   ],
   "Send some oil.", "dplmc_chancellor_gift_kingdom_ask",[
   (assign, "$diplomacy_var", "itm_trade_oil"),
(assign, "$diplomacy_var2", 150),
 ]],
 
  [anyone|plyr, "dplmc_chancellor_gift_select", 
   [
   ],
   "Never mind.", "dplmc_chancellor_pretalk",[
 ]],
 
  [anyone, "dplmc_chancellor_gift_kingdom_ask", 
   [
   ],
   "Where does the lord live whom you want to make a present?", "dplmc_chancellor_gift_kingdom_select",[
 ]],
 
  [anyone|plyr|repeat_for_factions, "dplmc_chancellor_gift_kingdom_select", 
   [
   (store_repeat_object, ":faction_no"),
   (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
   (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
   (str_store_faction_name, s11, ":faction_no"),
   ],
   "In {s11}.", "dplmc_chancellor_gift_lord_ask",
  [
   (store_repeat_object, "$g_faction_selected"),
  ]],
  
  [anyone|plyr, "dplmc_chancellor_gift_kingdom_select", 
   [
   ],
   "Never mind.", "dplmc_chancellor_pretalk",[
 ]],

##nested diplomacy start+ Disable gift-sending during a war with a nation that doesn't recognize you
[anyone, "dplmc_chancellor_gift_lord_ask",
[
(is_between, "$g_faction_selected", npc_kingdoms_begin, npc_kingdoms_end),
(neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
(store_relation, reg0, "$players_kingdom", "$g_faction_selected"),
(lt, reg0, 0),
(neg|faction_slot_ge, "$g_faction_selected", slot_faction_recognized_player, 1),
],
"Given that we are currently at war with the {s11} but they do not officially recognize your legitimacy, any messengers we sent would run the risk of being hanged as bandits.", "dplmc_chancellor_pretalk",[
]],
##nested diplomacy end+
  [anyone, "dplmc_chancellor_gift_lord_ask", 
   [
   ],
   "To whom do you like to send the gift?", "dplmc_chancellor_gift_lord_select",[
 ]], 
 
    ##select the lord who shall receive the gift to hand over
   [anyone|plyr|repeat_for_troops, "dplmc_chancellor_gift_lord_select",
   [
     (store_repeat_object, ":troop_no"),
     (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
     (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
     (troop_slot_eq, ":troop_no", slot_troop_met, 1),
     (neq, "trp_player", ":troop_no"),
     (troop_get_slot, ":target_party", ":troop_no", slot_troop_leaded_party),
     (gt, ":target_party", 0),
     (store_troop_faction, ":faction_no", ":troop_no"),
     (eq, ":faction_no", "$g_faction_selected"),
     (str_store_troop_name, s11, ":troop_no"),
   
   ],"{s11}.", "dplmc_chancellor_gift_send_ask",
   [
      (store_repeat_object, "$lord_selected"),
   ]], 
   
  [anyone|plyr, "dplmc_chancellor_gift_lord_select", 
   [
   ],
   "I can't think of anyone.", "dplmc_chancellor_pretalk",[
 ]],
   
  [anyone, "dplmc_chancellor_gift_send_ask", 
   [
      (str_store_item_name,s6,"$diplomacy_var"),
      (str_store_troop_name, s11, "$lord_selected"),
   ],
   "I will send a servant with the {s6} to {s11}.", "dplmc_chancellor_gift_send_confirm",[
   
 ]],
 
[anyone|plyr, "dplmc_chancellor_gift_send_confirm",
[
],
"Thank you.", "dplmc_chancellor_pretalk",[
(call_script, "script_dplmc_send_gift", "$lord_selected", "$diplomacy_var", "$diplomacy_var2"),
]],
 
  [anyone|plyr, "dplmc_chancellor_gift_send_confirm", 
   [
   ],
   "Never mind.", "dplmc_chancellor_pretalk",[
 ]],


   
 
  ##send gift to a lady
   [anyone|plyr, "dplmc_chancellor_gift_lady_or_lord",
   [],
   "Please send a gift to a lady.", "dplmc_chancellor_lady_gift_ask_type",
   []], 
   
   [anyone|plyr, "dplmc_chancellor_gift_lady_or_lord",
   [],
   "Never mind.", "dplmc_chancellor_pretalk",
   []],  

 
  [anyone, "dplmc_chancellor_lady_gift_ask_type", 
   [
   ],
   "I recommend to send dyes, silk or velvets. If we have enough in our household I will induce a servant to deliver it.", "dplmc_chancellor_lady_gift_select",[
 ]],
 
  ##send ale
  [anyone|plyr, "dplmc_chancellor_lady_gift_select", 
   [
   	(troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),
   	(assign, ":amount", 0),
	  (try_for_range, ":inventory_slot", 0, ":capacity"),
		  (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
		  (eq, ":item", "itm_trade_raw_dyes"),
		  (val_add, ":amount", 1),
    (try_end),
	  (ge, ":amount", 1),
   ],
   "Send dyes.", "dplmc_chancellor_lady_gift_kingdom_ask",[
   (assign, "$diplomacy_var", "itm_trade_raw_dyes"),
(assign, "$diplomacy_var2", 1),
 ]],
 
  ##send wine
  [anyone|plyr, "dplmc_chancellor_lady_gift_select", 
   [
   	(troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),
   	(assign, ":amount", 0),
	  (try_for_range, ":inventory_slot", 0, ":capacity"),
		  (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
		  (eq, ":item", "itm_trade_raw_silk"),
		  (val_add, ":amount", 1),
    (try_end),
	  (ge, ":amount", 1),
   ],
   "Send silk.", "dplmc_chancellor_lady_gift_kingdom_ask",[
   (assign, "$diplomacy_var", "itm_trade_raw_silk"),
(assign, "$diplomacy_var2", 1),
 ]],
 
  ##send oil
  [anyone|plyr, "dplmc_chancellor_lady_gift_select", 
   [
   	(troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),
   	(assign, ":amount", 0),
	  (try_for_range, ":inventory_slot", 0, ":capacity"),
		  (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
		  (eq, ":item", "itm_trade_velvet"),
		  (val_add, ":amount", 1),
    (try_end),
	  (ge, ":amount", 1),
   ],
   "Send velvet.", "dplmc_chancellor_lady_gift_kingdom_ask",[
   (assign, "$diplomacy_var", "itm_trade_velvet"),
(assign, "$diplomacy_var2", 1),
 ]],
 
  [anyone|plyr, "dplmc_chancellor_lady_gift_select", 
   [
   ],
   "Never mind.", "dplmc_chancellor_pretalk",[
 ]],
 
  [anyone, "dplmc_chancellor_lady_gift_kingdom_ask", 
   [
   ],
   "Where does the lady live?", "dplmc_chancellor_lady_gift_kingdom_select",[
 ]],
 
  [anyone|plyr|repeat_for_factions, "dplmc_chancellor_lady_gift_kingdom_select", 
   [
   (store_repeat_object, ":faction_no"),
   (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
   (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
   (str_store_faction_name, s11, ":faction_no"),
   ],
   "In {s11}.", "dplmc_chancellor_lady_gift_lady_ask",
  [
   (store_repeat_object, "$g_faction_selected"),
  ]],
  
  [anyone|plyr, "dplmc_chancellor_lady_gift_kingdom_select", 
   [
   ],
   "Never mind.", "dplmc_chancellor_pretalk",[
 ]],

##nested diplomacy start+ Disable gift-sending during a war with a nation that doesn't recognize you
[anyone, "dplmc_chancellor_lady_gift_lady_ask",
[
(is_between, "$g_faction_selected", npc_kingdoms_begin, npc_kingdoms_end),
(neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
(store_relation, reg0, "$players_kingdom", "$g_faction_selected"),
(lt, reg0, 0),
(neg|faction_slot_ge, "$g_faction_selected", slot_faction_recognized_player, 1),
],
"Given that we are currently at war with the {s11} but they do not officially recognize your legitimacy, any messengers we sent would run the risk of being hanged as bandits.", "dplmc_chancellor_pretalk",[
]],
##nested diplomacy end+
  [anyone, "dplmc_chancellor_lady_gift_lady_ask", 
   [
   ],
   "Which lady should receive the gift?", "dplmc_chancellor_lady_gift_lady_select",[
 ]], 
 
    ##select the lord who shall receive the gift to hand over
   [anyone|plyr|repeat_for_troops, "dplmc_chancellor_lady_gift_lady_select",
   [
     (store_repeat_object, ":troop_no"),
     (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_lady),
     (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
     (troop_slot_eq, ":troop_no", slot_troop_met, 1),
     (neq, "trp_player", ":troop_no"),
     (store_troop_faction, ":faction_no", ":troop_no"),
     (eq, ":faction_no", "$g_faction_selected"),
     (str_store_troop_name, s11, ":troop_no"),
   
   ],"{s11}.", "dplmc_chancellor_lady_gift_send_ask",
   [
      (store_repeat_object, "$lord_selected"),
   ]], 
   
  [anyone|plyr, "dplmc_chancellor_lady_gift_lady_select", 
   [
   ],
   "I can't think of anyone.", "dplmc_chancellor_pretalk",[
 ]],
   
  [anyone, "dplmc_chancellor_lady_gift_send_ask", 
   [
      (str_store_item_name,s6,"$diplomacy_var"),
      (str_store_troop_name, s11, "$lord_selected"),
   ],
   "I will send a servant with the {s6} to {s11}.", "dplmc_chancellor_lady_gift_send_confirm",[
   
 ]],
 
  [anyone|plyr, "dplmc_chancellor_lady_gift_send_confirm", 
   [
   ],
   "Thank you.", "dplmc_chancellor_pretalk",[  
(call_script, "script_dplmc_send_gift", "$lord_selected", "$diplomacy_var", "$diplomacy_var2"),
 ]],
 
  [anyone|plyr, "dplmc_chancellor_lady_gift_send_confirm", 
   [
   ],
   "Never mind.", "dplmc_chancellor_pretalk",[
 ]],
 
  ##chancellor household
  [anyone|plyr, "dplmc_chancellor_talk", 
   [
   ],
   "Let us check our household possessions.", "dplmc_chancellor_talk_household",[
   (change_screen_loot, "trp_household_possessions"),
 ]],

  [anyone, "dplmc_chancellor_talk_household", 
   [
   ],
   "You should store all important things in the household.", "dplmc_chancellor_pretalk",[
 ]],
 
	 ##diplomacy start+
	[anyone|plyr, "dplmc_chancellor_talk",
	[(eq, 0, 1),], #Floris - needs gear fix if re-activated
	"I would like to take a look through the items in my secondary storage houses.", "dplmc_chancellor_pretalk",
	[(change_screen_loot, "trp_dplmc_chancellor"),]],
##diplomacy end+

##zerilius changes begin
#dismiss chancellor
[anyone|plyr, "dplmc_chancellor_talk",
[],
"I no longer need your services.", "dplmc_chancellor_dismiss_confirm_ask",
[]],

[anyone, "dplmc_chancellor_dismiss_confirm_ask",
[
],
"Are you sure that you don't need me anymore?", "dplmc_chancellor_dismiss_confirm",
[]],

[anyone|plyr, "dplmc_chancellor_dismiss_confirm",
[
],
"Yes I am.", "dplmc_chancellor_dismiss_confirm_yes",
[]],

[anyone, "dplmc_chancellor_dismiss_confirm_yes",
[
],
"As you wish.", "close_window",
[
(assign, "$g_player_chancellor", -1),
]],

[anyone|plyr, "dplmc_chancellor_dismiss_confirm",
[
],
"No I am not.", "dplmc_chancellor_pretalk",
[]],
##zerilius changes end
   [anyone|plyr, "dplmc_chancellor_talk",
   [],
   "Farewell!", "close_window",
   []], 
 
##Constable
  [anyone,"start",
   [
    (eq, "$g_player_constable","$g_talk_troop"),
    ],
   "Always at your service!", "dplmc_constable_talk",[
   ]],
   
  [anyone,"dplmc_constable_pretalk",
##diplomacy start+ Replace "Sire" with {s0}
#[],
#"Do you need anything else, Sire?", "dplmc_constable_talk",[
[(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
],
"Do you need anything else, {s0}?", "dplmc_constable_talk",[
##diplomacy end+
 ]],
  
  ##ask about war
  [anyone|plyr,"dplmc_constable_talk", [],
   "How goes the war?", "dplmc_constable_talk_ask_war",[]],
   
  [anyone,"dplmc_constable_talk_ask_war", [],
   "{s12}", "dplmc_constable_talk_ask_war_2",
   [
    (assign, ":num_enemies", 0),
    (try_for_range_backwards, ":cur_faction", kingdoms_begin, kingdoms_end),
      (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
      (store_relation, ":cur_relation", ":cur_faction", "fac_player_supporters_faction"),
      (lt, ":cur_relation", 0),
      (try_begin),
        (eq, ":num_enemies", 0),
        (str_store_faction_name_link, s12, ":cur_faction"),
      (else_try),
        (eq, ":num_enemies", 1),
        (str_store_faction_name_link, s11, ":cur_faction"),
        (str_store_string, s12, "@{s11} and {s12}"),
      (else_try),
        (str_store_faction_name_link, s11, ":cur_faction"),
        (str_store_string, s12, "@{!}{s11}, {s12}"),
      (try_end),
      (val_add, ":num_enemies", 1),
    (try_end),
    (try_begin),
      (eq, ":num_enemies", 0),
      (str_store_string, s12, "@We are not at war with anyone."),
    (else_try),
      (str_store_string, s12, "@We are at war with {s12}."),
    (try_end),
    ]],

  [anyone|plyr|repeat_for_factions, "dplmc_constable_talk_ask_war_2", [(store_repeat_object, ":faction_no"),
                                                                  (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
                                                                  (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
                                                                     (store_relation, ":cur_relation", ":faction_no", "fac_player_supporters_faction"),
                                                                     (lt, ":cur_relation", 0),
                                                                     (str_store_faction_name, s1, ":faction_no")],
   "Tell me more about the war with {s1}.", "dplmc_constable_talk_ask_war_details",[(store_repeat_object, "$faction_requested_to_learn_more_details_about_the_war_against")]],

  [anyone|plyr,"dplmc_constable_talk_ask_war_2", [], "That's all I wanted to know. Thank you.", "dplmc_constable_pretalk",[]],

  [anyone,"dplmc_constable_talk_ask_war_details", [],
   "{!}{s9}.",
   "dplmc_constable_talk_ask_war_2",
   [
		(store_add, ":war_damage_slot", "$faction_requested_to_learn_more_details_about_the_war_against", slot_faction_war_damage_inflicted_on_factions_begin),
		(val_sub, ":war_damage_slot", kingdoms_begin),
	    (faction_get_slot, ":war_damage_inflicted", "$players_kingdom", ":war_damage_slot"), #Floris 2.52 - Diplo bugfix was "fac_player_supporters_faction"
		
		(store_add, ":war_damage_slot", "$players_kingdom", slot_faction_war_damage_inflicted_on_factions_begin), #Floris 2.52 - Diplo bugfix was "fac_player_supporters_faction"
		(val_sub, ":war_damage_slot", kingdoms_begin),
	    (faction_get_slot, ":war_damage_suffered", "$faction_requested_to_learn_more_details_about_the_war_against", ":war_damage_slot"),

		(val_max, ":war_damage_suffered", 1),

		(store_mul, ":war_damage_ratio", ":war_damage_inflicted", 100),
		(val_div, ":war_damage_ratio", ":war_damage_suffered"),
		
		(try_begin),
			(eq, "$cheat_mode", 1),
			(assign, reg3, ":war_damage_inflicted"),
			(assign, reg4, ":war_damage_suffered"),
			(assign, reg5, ":war_damage_ratio"),
			(display_message, "str_war_damage_inflicted_reg3_suffered_reg4_ratio_reg5"),
		(try_end),
		
		(str_store_string, s9, "str_error__did_not_calculate_war_progress_string_properly"),
		(try_begin),
			(lt, ":war_damage_inflicted", 5),
			(str_store_string, s9, "str_the_war_has_barely_begun_so_and_it_is_too_early_to_say_who_is_winning_and_who_is_losing"),
		(else_try),	
			(gt, ":war_damage_inflicted", 100),
			(gt, ":war_damage_ratio", 200),
			(str_store_string, s9, "str_we_have_been_hitting_them_very_hard_and_giving_them_little_chance_to_recover"),
		(else_try),	
			(gt, ":war_damage_inflicted", 80),
			(gt, ":war_damage_ratio", 150),
			(str_store_string, s9, "str_the_fighting_has_been_hard_but_we_have_definitely_been_getting_the_better_of_them"),
		(else_try),	
			(gt, ":war_damage_suffered", 100),
			(lt, ":war_damage_ratio", 50),
			(str_store_string, s9, "str_they_have_been_hitting_us_very_hard_and_causing_great_suffering"),
		(else_try),	
			(gt, ":war_damage_suffered", 80),
			(lt, ":war_damage_ratio", 68),
			(str_store_string, s9, "str_the_fighting_has_been_hard_and_i_am_afraid_that_we_have_been_having_the_worst_of_it"),
		(else_try),	
			(gt, ":war_damage_suffered", 50),
			(gt, ":war_damage_inflicted", 50),
			(gt, ":war_damage_ratio", 65),
			(str_store_string, s9, "str_both_sides_have_suffered_in_the_fighting"),
		(else_try),
			(gt, ":war_damage_ratio", 125),
			(str_store_string, s9, "str_no_clear_winner_has_yet_emerged_in_the_fighting_but_i_think_we_are_getting_the_better_of_them"),
		(else_try),
			(gt, ":war_damage_ratio", 80),
			(str_store_string, s9, "str_no_clear_winner_has_yet_emerged_in_the_fighting_but_i_fear_they_may_be_getting_the_better_of_us"),
		(else_try),
			(str_store_string, s9, "str_no_clear_winner_has_yet_emerged_in_the_fighting"),
		(try_end),

		(try_begin),
			#(neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "$g_talk_troop"), ##Floirs 2.52 - not needed
			(call_script, "script_npc_decision_checklist_peace_or_war", "$players_kingdom", "$faction_requested_to_learn_more_details_about_the_war_against", -1),
			(str_store_string, s9, "str_s9_s14"),
        (try_end),
		]],
		
  ##send scout
   [anyone|plyr, "dplmc_constable_talk",
   [],
   "I want information about a settlement.", "dplmc_constable_scout_ask",
   []], 
   
  [anyone, "dplmc_constable_scout_ask", 
   [
   ],
   "We can send a spy which will cost you 300 denars. Where do you want to send the spy?", "dplmc_constable_scout_location",[
 ]],
 
  [anyone|plyr|repeat_for_factions, "dplmc_constable_scout_location",
  [
    (store_troop_gold, ":cur_gold", "trp_household_possessions"),
    (ge, ":cur_gold", 300),
    (store_repeat_object, ":faction"), 
    (is_between, ":faction", kingdoms_begin, kingdoms_end),
    (str_store_faction_name, s11, ":faction"),
  ],
  "{!}{s11}.", "dplmc_constable_scout_location_confirm_ask", 
  [
    (store_repeat_object, "$diplomacy_var"),
  ]
  ],
  
   [anyone|plyr, "dplmc_constable_scout_location",
   [],
   "I changed my mind.", "dplmc_constable_pretalk",
   []], 
   
  [anyone, "dplmc_constable_scout_location_confirm_ask", 
   [
   ],
   "Which settlement do you want to spy out?", "dplmc_constable_scout_location2",[
 ]],
 
  [anyone|plyr|repeat_for_parties, "dplmc_constable_scout_location2",
  [
    (store_repeat_object, ":party_no"),
    (is_between, ":party_no", walled_centers_begin, walled_centers_end),  
    (store_faction_of_party, ":faction", ":party_no"),
    (eq, ":faction", "$diplomacy_var"),
    (str_store_party_name, s11, ":party_no"),
  ],
  "{!}{s11}.", "dplmc_constable_scout_location_confirm_ask2", 
  [
    (store_repeat_object, "$diplomacy_var"),
  ]
  ],
  
   [anyone|plyr, "dplmc_constable_scout_location2",
   [],
   "I changed my mind.", "dplmc_constable_pretalk",
   []], 
   
  [anyone, "dplmc_constable_scout_location_confirm_ask2", 
   [(str_store_party_name, s11, "$diplomacy_var"),
   ],
   "As you wish, I will send a spy to {s11} and withdraw 300 denars from your treasury.", "dplmc_constable_scout_location_confirm",[
 ]],
 
   [anyone|plyr, "dplmc_constable_scout_location_confirm",
   [
   ],
   "Great.", "dplmc_constable_pretalk",
   [  (call_script, "script_dplmc_withdraw_from_treasury", 300),
      (call_script, "script_dplmc_send_scout_party", "$current_town", "$diplomacy_var", "$players_kingdom"),
   ]], 

   [anyone|plyr, "dplmc_constable_scout_location_confirm",
   [],
   "Hold on!", "dplmc_constable_pretalk",
   []], 
		
  ##release prisoner
  [anyone|plyr,"dplmc_constable_talk", [],
   "I want to release a prisoner.", "dplmc_constable_talk_ask_prisoner",[]],
   
  [anyone,"dplmc_constable_talk_ask_prisoner",
   [],
   "Alright, which prisoner do you want to release?", "dplmc_constable_talk_prisoner_select",[
 ]],
   
  ##select enemy prisoner
 [anyone|plyr|repeat_for_troops, "dplmc_constable_talk_prisoner_select",
   [
     (store_repeat_object, ":troop_no"),
     (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
     (is_between, ":troop_no", kings_begin, lords_end),
     (troop_get_slot, ":party", ":troop_no", slot_troop_prisoner_of_party),

     (assign, ":can_release", 0),
     (try_begin),
      (is_between, ":party", walled_centers_begin, walled_centers_end),
      (party_slot_eq, ":party", slot_town_lord, "trp_player"),
      (assign, ":can_release", 1),
     (else_try),
      (eq, ":party", "p_main_party"),
      (assign, ":can_release", 1),
     (try_end),
     (eq, ":can_release", 1),

     (str_store_troop_name, s10, ":troop_no"),
     (store_faction_of_troop, ":faction_no", ":troop_no"),
     (str_store_faction_name_link, s11, ":faction_no"),
     ],
   "{s10} of {s11}.", "dplmc_constable_exchange_prisoner_ask_confirm",
   [
     (store_repeat_object, "$diplomacy_var"),
     (store_faction_of_troop, "$g_faction_selected", "$diplomacy_var"),
     ]],
     
  [anyone|plyr,"dplmc_constable_talk_prisoner_select", [],
   "No one.", "dplmc_constable_pretalk",
   [
   ]],
     
  [anyone,"dplmc_constable_exchange_prisoner_ask_confirm",
   [
     (str_store_troop_name, s10, "$diplomacy_var"),
     (store_faction_of_troop, ":faction_no", "$diplomacy_var"),
     (str_store_faction_name_link, s11, ":faction_no"),
   ],
   "As you wish, I will tell the prison guard to release {s10} of {s11}.", "dplmc_constable_exchange_prisoner_confirm",[
 ]],
 
  [anyone|plyr,"dplmc_constable_exchange_prisoner_confirm", [],
   "Very well.", "dplmc_constable_pretalk",
   [
      (troop_get_slot, ":party", "$diplomacy_var", slot_troop_prisoner_of_party),
      
      (try_begin),
        (eq, "$cheat_mode", 1),
        (str_store_party_name, s7, ":party"), #debug
        (display_message, "@{!}DEBUG - prisoner of: {s7}"),
      (try_end),   

      (party_remove_prisoners, ":party", "$diplomacy_var", 1),    
      (try_begin),
        (main_party_has_troop, "$diplomacy_var"),
        (party_remove_prisoners, "p_main_party", "$diplomacy_var", 1),  
      (try_end),
      (call_script, "script_remove_troop_from_prison", "$diplomacy_var"),
      (str_store_troop_name, s7, "$diplomacy_var"),
      (display_message, "str_dplmc_has_been_set_free"),
      (call_script, "script_change_player_relation_with_troop", "$diplomacy_var", 3),
      (call_script, "script_change_player_honor", 1),
   ]],
    
  [anyone|plyr,"dplmc_constable_exchange_prisoner_confirm", [],
   "No, I changed my mind.", "dplmc_constable_pretalk",[]], 

   [anyone|plyr, "dplmc_constable_talk",
   [],
   "Please give me a report.", "dplmc_constable_reports_ask",
   []],
   
   [anyone, "dplmc_constable_reports_ask",
   [],
   "About what do you want to have a report?", "dplmc_constable_reports",
   []],  
 
   [anyone|plyr, "dplmc_constable_reports",
	[
		##diplomacy start+ Handle player is co-ruler of kingdom
		(assign, ":is_coruler", 0),
		(try_begin),
			(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
			(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
			(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
			(assign, ":is_coruler", 1),
		(try_end),
		(this_or_next|eq, ":is_coruler", 1),
		##diplomacy end+
		 (eq, "$players_kingdom", "fac_player_supporters_faction"),
	],
   "Please give me a report about the sovereignty's army.", "dplmc_constable_kingdom_overview",
   []], 
   
   [anyone, "dplmc_constable_kingdom_overview",
   [    
		(assign, ":garrison_size", 0),
		(assign, ":field_size", 0),
		(assign, ":castle_count", 0),
		(assign, ":town_count", 0),
		##diplomacy start+ Handle player is co-ruler of kingdom
		(assign, ":alt_faction", "fac_player_supporters_faction"),
		(try_begin),
			(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
			(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
			(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
			(assign, ":alt_faction", "$players_kingdom"),
		(try_end),
		##diplomacy end+

		(try_for_parties, ":selected_party"),
		(try_begin),
		  (this_or_next|party_slot_eq, ":selected_party", slot_party_type, spt_town),
		  (party_slot_eq, ":selected_party", slot_party_type, spt_castle),
		  (store_faction_of_party, ":party_faction", ":selected_party"),
		  ##diplomacy start+
		  (this_or_next|eq, ":party_faction", ":alt_faction"),
		  ##diplomacy end+
		  (eq, ":party_faction", "fac_player_supporters_faction"),

		  (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
		  (try_for_range, ":i_stack", 0, ":num_stacks"),
			(party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
			(val_add, ":garrison_size", ":stack_size"),
		  (try_end),

		  (try_begin),
			(party_slot_eq, ":selected_party", slot_party_type, spt_castle),
			(val_add, ":castle_count", 1),
		  (else_try),
			(val_add, ":town_count", 1),
		  (try_end),
		(else_try),
		  (party_slot_eq, ":selected_party", slot_party_type, spt_kingdom_hero_party),
		  (store_faction_of_party, ":party_faction", ":selected_party"),
		  ##diplomacy start+
		  (this_or_next|eq, ":party_faction", ":alt_faction"),
		  ##diplomacy end+
		  (eq, ":party_faction", "fac_player_supporters_faction"),
		  (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
		  (try_for_range, ":i_stack", 0, ":num_stacks"),
			(party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
			(val_add, ":field_size", ":stack_size"),
		  (try_end),
		(else_try),
		  (eq, ":selected_party", "p_main_party"),
		  (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
		  (try_for_range, ":i_stack", 0, ":num_stacks"),
			(party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
			(val_add, ":field_size", ":stack_size"),
		  (try_end),
		(try_end),

    (try_end),   
    (assign, reg2, ":garrison_size"),
    (str_store_string, s6, "@Our sovereignty currently has {reg2} soldiers"),
    (assign, reg2, ":town_count"),
    (str_store_string, s6, "@{s6} garrisoned in {reg2} towns"),
    (assign, reg2, ":castle_count"),
    (str_store_string, s6, "@{s6} and {reg2} castles."),
    (try_begin),
      (gt, ":field_size", 0),
      (assign, reg2, ":field_size"),
      (str_store_string, s6, "@{s6} In addition we have {reg2} soldiers in the field."),
    (try_end),
    
   ],
   "{!}{s6}", "dplmc_constable_reports_ask",
   []], 
 
   [anyone|plyr, "dplmc_constable_reports",
   [
   ],
   "Please give me a report about my army.", "dplmc_constable_overview",
   []], 
   
   [anyone, "dplmc_constable_overview",
   [

    (assign, ":garrison_size", 0),
    (assign, ":field_size", 0),
    (assign, ":patrol_size", 0),
    (assign, ":castle_count", 0),
    (assign, ":town_count", 0),
    (try_for_parties, ":selected_party"),
         
      (try_begin),
        (this_or_next|party_slot_eq, ":selected_party", slot_party_type, spt_town),
        (party_slot_eq, ":selected_party", slot_party_type, spt_castle),
        (party_slot_eq, ":selected_party", slot_town_lord, "trp_player"),
        
        (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
          (val_add, ":garrison_size", ":stack_size"),
        (try_end),

        (try_begin),
          (party_slot_eq, ":selected_party", slot_party_type, spt_castle),
          (val_add, ":castle_count", 1),
        (else_try),
          (val_add, ":town_count", 1),
        (try_end),  
      (else_try),
        (eq, ":selected_party", "p_main_party"),
        (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
          (val_add, ":field_size", ":stack_size"),
        (try_end),
      (else_try),
        (party_slot_eq, ":selected_party", slot_party_type, spt_patrol),
        (store_faction_of_troop, ":player_faction", "trp_player"),
        (store_faction_of_party, ":party_faction", ":selected_party"),
        (eq, ":party_faction", ":player_faction"),
        (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
          (val_add, ":patrol_size", ":stack_size"),
        (try_end),
      (try_end),     

    (try_end),   
    (assign, reg2, ":garrison_size"),
    (str_store_string, s6, "@We currently have {reg2} soldiers"),
    (assign, reg2, ":town_count"),
    (str_store_string, s6, "@{s6} garrisoned in {reg2} towns"),
    (assign, reg2, ":castle_count"),
    (str_store_string, s6, "@{s6} and {reg2} castles."),
    (try_begin),
      (gt, ":field_size", 0),
      (assign, reg2, ":field_size"),
      (assign, reg3, ":patrol_size"),
      (str_store_string, s6, "@{s6} In addition you have {reg2} soldiers in your convoy and {reg3} soldiers in patrols."),
    (try_end),
    
   ],
   "{!}{s6}", "dplmc_constable_reports_ask",
   []], 
   
   [anyone|plyr, "dplmc_constable_reports",
   [
   ],
   "Please give me a status report about the convoy of a lord.", "dplmc_constable_lord",
   []], 
   
   [anyone, "dplmc_constable_lord",
   [],
   "About which lord do you like to be informed?", "dplmc_constable_status_lord_select",
   []],  
   
   [anyone|plyr|repeat_for_troops, "dplmc_constable_status_lord_select",
   [
     (store_repeat_object, ":troop_no"),
     (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
     (neq, "trp_player", ":troop_no"),
     (troop_slot_ge, ":troop_no", slot_troop_leaded_party, 0),
     (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
     (store_troop_faction, ":faction_no", ":troop_no"),
	##diplomacy start+ Handle player is co-ruler of faction
	##OLD:
	#(eq, ":faction_no", "fac_player_supporters_faction"),
	##NEW:
	(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":faction_no"),
	(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
	##diplomacy end+
     (str_store_troop_name, s11, ":troop_no"),
   ],
   "{!}{s11}.", "dplmc_constable_status_lord_info",
   [
    (store_repeat_object, "$diplomacy_var"),
   ]],
   
   [anyone|plyr, "dplmc_constable_status_lord_select",
   [],
   "Never mind.", "dplmc_constable_reports_ask",
   []],
   
   [anyone, "dplmc_constable_status_lord_info",
   [
    (assign, ":selected_troop", "$diplomacy_var"),
    (str_store_troop_name, s60, ":selected_troop"),
    

    (call_script, "script_update_troop_location_notes", ":selected_troop", 1),
    (call_script, "script_get_information_about_troops_position", ":selected_troop", 0),
    
    (assign, ":party_size", 0),
    (troop_get_slot, ":selected_party", ":selected_troop", slot_troop_leaded_party),
    (str_store_string, s52, "str_empty_string"),
    (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
    
    (le, ":num_stacks", 20),    

    (try_for_range, ":i_stack", 1, ":num_stacks"),
      (party_stack_get_troop_id, ":stack_troop", ":selected_party", ":i_stack"),
      (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
      (val_add, ":party_size", ":stack_size"),
      (assign, reg2, ":stack_size"),
      (str_store_troop_name, s53, ":stack_troop"),
      (str_store_string, s52, "@{!}{s52} {reg2} {s53}."),
    (try_end),   
  
    (assign, reg2, ":party_size"),
    (str_store_string, s51, "@He fields {reg2} soldiers."),
   ],
   "{!}{s1} {s51} {s52}", "dplmc_constable_lord",
   []],   
   
   [anyone, "dplmc_constable_status_lord_info",
   [
    (assign, ":selected_troop", "$diplomacy_var"),
    (str_store_troop_name, s60, ":selected_troop"),
    

    (call_script, "script_update_troop_location_notes", ":selected_troop", 1),
    (call_script, "script_get_information_about_troops_position", ":selected_troop", 0),
    
    (assign, ":party_size", 0),
    (troop_get_slot, ":selected_party", ":selected_troop", slot_troop_leaded_party),
    (str_store_string, s52, "str_empty_string"),
    (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),

    (try_for_range, ":i_stack", 1, ":num_stacks"),
      (party_stack_get_troop_id, ":stack_troop", ":selected_party", ":i_stack"),
      (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
      (val_add, ":party_size", ":stack_size"),
      (try_begin),
        (le, ":i_stack", 20),
        (assign, reg2, ":stack_size"),
        (str_store_troop_name, s53, ":stack_troop"),
        (str_store_string, s52, "@{!}{s52} {reg2} {s53}."),
      (try_end),
    (try_end),   
  
    (assign, reg2, ":party_size"),
    (str_store_string, s51, "@He fields {reg2} soldiers."),
   ],
   "{!}{s1} {s51} {s52}", "dplmc_constable_status_lord_info_6",
   []], 
   
   [anyone, "dplmc_constable_status_lord_info_6",
   [
    (assign, ":selected_troop", "$diplomacy_var"),
    (str_store_troop_name, s60, ":selected_troop"),
    
    (assign, ":party_size", 0),
    (troop_get_slot, ":selected_party", ":selected_troop", slot_troop_leaded_party),
    (str_store_string, s52, "str_empty_string"),
    (party_get_num_companion_stacks, ":num_stacks", ":selected_party"), 

    (try_for_range, ":i_stack", 20, ":num_stacks"),
      (party_stack_get_troop_id, ":stack_troop", ":selected_party", ":i_stack"),
      (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
      (val_add, ":party_size", ":stack_size"),
      (assign, reg2, ":stack_size"),
      (str_store_troop_name, s53, ":stack_troop"),
      (str_store_string, s52, "@{!}{s52} {reg2} {s53}."),
    (try_end),   
  
    (assign, reg2, ":party_size"),
   ],
   "{!}{s52}", "dplmc_constable_lord",
   []],  
 
   
    ##garrison status
   [anyone|plyr, "dplmc_constable_reports",
   [
   ],
   "Please give me a status report about the garrison of a fief.", "dplmc_constable_status",
   []], 
   
   
   [anyone, "dplmc_constable_status",
   [],
   "About which fief do you like to be informed?", "dplmc_constable_status_select_fief",
   []],  
   
   [anyone|plyr|repeat_for_parties, "dplmc_constable_status_select_fief",
   [
    (store_repeat_object, ":party_no"),
    (is_between, ":party_no", walled_centers_begin, walled_centers_end),
    (store_faction_of_party, ":party_faction", ":party_no"),
    (this_or_next|party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
	##diplomacy start+ Handle player is co-ruler of faction
	##OLD:
	#(eq, ":party_faction", "fac_player_supporters_faction"),
	##NEW:
	(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":party_faction"),
	(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
	##diplomacy end+
    (str_store_party_name, s60, ":party_no"),
   ],
   "{!}{s60}.", "dplmc_constable_status_info",
   [
    (store_repeat_object, "$diplomacy_var"),
   ]],
   


   [anyone, "dplmc_constable_status_info",
   [
    (assign, ":selected_party", "$diplomacy_var"),
    (str_store_party_name, s60, ":selected_party"),
    
    (assign, ":garrison_size", 0),
         
    (str_store_string, s52, "str_empty_string"),
    (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
    
    (le, ":num_stacks", 20),

    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_stack_get_troop_id, ":stack_troop", ":selected_party", ":i_stack"),
      (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
      (val_add, ":garrison_size", ":stack_size"),
      (assign, reg2, ":stack_size"),
      (str_store_troop_name, s53, ":stack_troop"),
      (str_store_string, s52, "@{!}{s52} {reg2} {s53}."),
    (try_end),   
  
    (assign, reg2, ":garrison_size"),
    (str_store_string, s51, "@We currently have {reg2} soldiers garrisoned in {s60}."),
   ],
   "{!}{s51} {s52}", "dplmc_constable_status",
   []],   
   
   [anyone, "dplmc_constable_status_info",
   [
    (assign, ":selected_party", "$diplomacy_var"),
    (str_store_party_name, s60, ":selected_party"),
    
    (assign, ":garrison_size", 0),
         
    (str_store_string, s52, "str_empty_string"),
    (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),

    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_stack_get_troop_id, ":stack_troop", ":selected_party", ":i_stack"),
      (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
      (val_add, ":garrison_size", ":stack_size"),
      (try_begin),
        (le, ":i_stack", 20),
        (assign, reg2, ":stack_size"),
        (str_store_troop_name, s53, ":stack_troop"),
        (str_store_string, s52, "@{!}{s52} {reg2} {s53}."),
      (try_end),
    (try_end),   
  
    (assign, reg2, ":garrison_size"),
    (str_store_string, s51, "@We currently have {reg2} soldiers garrisoned in {s60}."),
   ],
   "{!}{s51} {s52}", "dplmc_constable_status_info_6",
   []], 
   
   [anyone, "dplmc_constable_status_info_6",
   [
    (assign, ":selected_party", "$diplomacy_var"),
    (str_store_party_name, s60, ":selected_party"),
         
    (str_store_string, s52, "str_empty_string"),
    (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),

    (try_for_range, ":i_stack", 20, ":num_stacks"),
      (party_stack_get_troop_id, ":stack_troop", ":selected_party", ":i_stack"),
      (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
      (assign, reg2, ":stack_size"),
      (str_store_troop_name, s53, ":stack_troop"),
      (str_store_string, s52, "@{!}{s52} {reg2} {s53}."),
    (try_end),   
  
   ],
   "{!}{s52}", "dplmc_constable_status",
   []], 
   
   [anyone|plyr, "dplmc_constable_status_select_fief",
   [],
   "Never mind.", "dplmc_constable_reports_ask",
   []],
   
   [anyone|plyr, "dplmc_constable_reports",
   [
   ],
   "Thank you, that's all for now.", "dplmc_constable_pretalk",
   []], 
   
   ##diplomacy start+
	[anyone|plyr, "dplmc_constable_talk",
	[],
	"I would like to take a look at the armory.", "dplmc_constable_armory_end", #Floris - gear fix "dplmc_constable_pretalk",
	[
	#Floris - gear fix
	(try_for_range, ":i", ek_item_0, ek_food), #Double check worn gear is gone
		(agent_get_item_slot, ":item", "$g_talk_agent", ":i"),
		(gt, ":item", 0),
		(troop_remove_item, "$g_talk_troop", ":item"),
	(try_end),
	#Floris - end	
	(change_screen_loot, "trp_dplmc_constable"),]],
	##diplomacy end+
	
   #Floris - gear fix - to allow for delay in returning gear
   [anyone,"dplmc_constable_armory_end",[(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0")],"Do you need anything else, {s0}?", "dplmc_constable_armory_end_2",[]],
   [anyone,"dplmc_constable_armory_end_2",[(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0")],"Do you need anything else, {s0}?", "dplmc_constable_talk",
   [
    (try_begin),
		(neg|agent_has_item_equipped,"$g_talk_agent", "itm_ar_swa_dip_coatplate_a"),
		(agent_equip_item, "$g_talk_agent", "itm_ar_swa_dip_coatplate_a"),
		(agent_equip_item, "$g_talk_agent", "itm_bo_swa_t5_hose"),
	(try_end),
   ]],
   #Floris - end
   
   [anyone|plyr, "dplmc_constable_talk",
   [],
   "Let's talk about recruits and training.", "dplmc_constable_recruits_and_training_ask",
   []],
   
   [anyone, "dplmc_constable_recruits_and_training_ask",
   [],
   "Of course.", "dplmc_constable_recruits_and_training",
   []],  
   
  ##train recruits
  [anyone|plyr, "dplmc_constable_recruits_and_training",
  [
    (neg|is_between, "$g_constable_training_center", walled_centers_begin, walled_centers_end),
  ],
  "Can you train some recruits, please?", "dplmc_constable_train_ask", 
  []
  ],
  
  [anyone, "dplmc_constable_train_ask",
  [],
  "Of course, where should I train them?", "dplmc_constable_train_select", 
  []
  ],
  
  [anyone|plyr|repeat_for_parties, "dplmc_constable_train_select",
  [
    (store_repeat_object, ":party_no"),
    (this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_town),
    (party_slot_eq, ":party_no", slot_party_type, spt_castle),
    (party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
    (str_store_party_name, s11, ":party_no"),
  ],
  "{!}{s11}.", "dplmc_constable_train_type_ask", 
  [
    (store_repeat_object, "$diplomacy_var"),
  ]
  ],
  
  [anyone, "dplmc_constable_train_type_ask",
  [
    (str_store_party_name, s11, "$diplomacy_var"),
  ],
  "Do you prefer melee or ranged units?", "dplmc_constable_train_type", 
  []
  ],

  [anyone|plyr, "dplmc_constable_train_type",
  [],
  "Melee.", "dplmc_constable_train_improved_ask", #Diplomacy 3.2
  [(assign, "$g_constable_training_type", 0),]
  ],
  
  [anyone|plyr, "dplmc_constable_train_type",
  [],
  "Ranged.", "dplmc_constable_train_improved_ask", #Diplomacy 3.2
  [(assign, "$g_constable_training_type", 1),]
  ],
  
  [anyone|plyr, "dplmc_constable_train_type",
  [],
  "Neither.", "dplmc_constable_pretalk", 
  []
  ],
##Diplomacy 3.2 begin
  [anyone, "dplmc_constable_train_improved_ask",
  [],
  "If you want I can hire additional trainers so we can train the recruits faster and better. This will cost 10 denars extra per day.", "dplmc_constable_train_improved", 
  []
  ],
  
  [anyone|plyr, "dplmc_constable_train_improved",
  [],
  "Yes, please hire additional trainers.", "dplmc_constable_train_center", 
  [(assign, "$g_constable_training_improved", 1),]
  ],
  
  [anyone|plyr, "dplmc_constable_train_improved",
  [],
  "No, you have to train them alone.", "dplmc_constable_train_center", 
  [(assign, "$g_constable_training_improved", 0),]
  ],
##Diplomacy 3.2 end

  [anyone, "dplmc_constable_train_center",
  [
    (str_store_party_name, s11, "$diplomacy_var"),
    (try_begin),
      (eq, "$g_constable_training_type", 0),
      (str_store_string, s12, "@You are preferring melee units."),
    (else_try),
      (str_store_string, s12, "@You are preferring ranged units."),
    (try_end),
#Diplomacy 3.2 begin
    (str_clear, s13),
    (try_begin),
      (eq, "$g_constable_training_improved", 1),
      (str_store_string, s13, "@ and the additional trainers"),
    (try_end),
#Diplomacy 3.2 end
  ],
  "Alright, I will train the recruits in {s11}. {s12} Please, make sure we have enough money in the treasury to pay for the equipment{s13}.", "dplmc_constable_pretalk", #Diplomacy 3.2
  [(assign, "$g_constable_training_center", "$diplomacy_var"),]
  ],
  
  [anyone|plyr, "dplmc_constable_train_select",
  [],
  "I changed my mind, maybe you shouldn't train them.", "dplmc_constable_pretalk", 
  []
  ],
  
  [anyone|plyr, "dplmc_constable_recruits_and_training",
  [
    (is_between, "$g_constable_training_center", walled_centers_begin, walled_centers_end),
    (str_store_party_name, s11, "$g_constable_training_center"),
    
  ],
  "Please stop training the recruits in {s11}.", "dplmc_constable_train_stop", 
  []
  ],
  
  [anyone, "dplmc_constable_train_stop",
  [
    (is_between, "$g_constable_training_center", walled_centers_begin, walled_centers_end),
    
  ],
  "As you wish.", "dplmc_constable_pretalk", 
  [(assign, "$g_constable_training_center", -1),]
  ],

   [anyone|plyr, "dplmc_constable_recruits_and_training",
   [
   ],
   "I want to recruit new soldiers.", "dplmc_constable_recruit",
   []],
   
   [anyone, "dplmc_constable_recruit",
   [
      (le, "$g_player_chamberlain", 0),
   ],
   "We need a treasury to recruit new soldiers. You have to appoint a chamberlain first.", "dplmc_constable_pretalk",
   []],

   [anyone, "dplmc_constable_recruit",
   [
     (gt, "$g_player_chamberlain", 0),
     (assign, ":recruiter_amount", 0),
   
     (try_begin),
        (party_slot_eq, "$current_town", slot_party_type, spt_town),
        (assign, ":max_recruiters", 4),
        (assign, reg0, 0),
     (else_try),
        (assign, ":max_recruiters", 2),
        (assign, reg0, 1),
     (try_end),
   
     (try_for_parties, ":party_no"),
        (party_slot_eq,":party_no", slot_party_type, dplmc_spt_recruiter),
        (party_slot_eq, ":party_no", dplmc_slot_party_recruiter_origin, "$current_town"),
        (val_add, ":recruiter_amount", 1),
     (try_end),
     
     (ge, ":recruiter_amount", ":max_recruiters"),
   ],
   "You have already hired the maximum amount of {reg0?4:2} recruiters from this {reg0?town:castle}.", "dplmc_constable_pretalk",
   []],


   [anyone, "dplmc_constable_recruit",
   [
     (gt, "$g_player_chamberlain", 0),
     (assign, ":recruiter_amount", 0),
   
     (try_begin),
        (party_slot_eq, "$current_town", slot_party_type, spt_town),
        (assign, ":max_recruiters", 4),
     (else_try),
        (assign, ":max_recruiters", 2),
     (try_end),
   
     (try_for_parties, ":party_no"),
        (party_slot_eq,":party_no", slot_party_type, dplmc_spt_recruiter),
        (party_slot_eq, ":party_no", dplmc_slot_party_recruiter_origin, "$current_town"),
        (val_add, ":recruiter_amount", 1),
     (try_end),
     
     (lt, ":recruiter_amount", ":max_recruiters"),
   ],
   "If you want, I will send someone to visit villages and recruit population to your forces. \
After he has collected the amount you ordered he returns to this {reg0?town:castle} and puts the recruits in the garrison. \
There's a limit for concurrent recruiters, which is 2 for castles and 4 for towns. \
What kind of recruits do you want?", "dplmc_constable_recruit_select",
   []],
   
 [anyone|plyr|repeat_for_factions, "dplmc_constable_recruit_select",
   [
    (store_repeat_object, ":faction_no"),
    (is_between, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
    (store_sub, ":offset", ":faction_no", "fac_kingdom_1"),
    (val_add, ":offset", "str_kingdom_1_adjective"),
    (str_store_string, s11, ":offset"),    
     ],
   "{s11}.", "dplmc_constable_recruit_amount",
   [
      (store_repeat_object, ":faction_no"),
      (assign, "$temp", ":faction_no"),
     ]],
     
   [anyone, "dplmc_constable_recruit_amount",
   [
   ],
   "You have to pay 20 denars for each recruit and 10 denars for the recruiter. I will take the money from the treasury. How many recruits are you willing to pay for?", "dplmc_constable_recruit_amount_select",
   []],
   
  [anyone|plyr,"dplmc_constable_recruit_amount_select",
   [(store_troop_gold,":gold","trp_household_possessions"), (ge,":gold",110),],
   "5.", "dplmc_constable_recruit_confirm_ask",[

   (assign, "$diplomacy_var", 5),
 ]],
 
  [anyone|plyr,"dplmc_constable_recruit_amount_select",
   [(store_troop_gold,":gold","trp_household_possessions"), (ge,":gold",210),],
   "10.", "dplmc_constable_recruit_confirm_ask",[
   (assign, "$diplomacy_var", 10),
 ]],
 
  [anyone|plyr,"dplmc_constable_recruit_amount_select",
   [(store_troop_gold,":gold","trp_household_possessions"), (ge,":gold",410),],
   "20.", "dplmc_constable_recruit_confirm_ask",[
   (assign, "$diplomacy_var", 20),
 ]],
 
  [anyone|plyr,"dplmc_constable_recruit_amount_select",
   [(store_troop_gold,":gold","trp_household_possessions"), (ge,":gold",610),],
   "30.", "dplmc_constable_recruit_confirm_ask",[
   (assign, "$diplomacy_var", 30),
 ]],
 
  [anyone|plyr,"dplmc_constable_recruit_amount_select",
   [(store_troop_gold,":gold","trp_household_possessions"), (ge,":gold",810),],
   "40.", "dplmc_constable_recruit_confirm_ask",[
   (assign, "$diplomacy_var", 40),
 ]],
 
  [anyone|plyr,"dplmc_constable_recruit_amount_select",
   [(store_troop_gold,":gold","trp_household_possessions"), (ge,":gold",1110),],
   "50.", "dplmc_constable_recruit_confirm_ask",[
   (assign, "$diplomacy_var", 50),
 ]],
 
  [anyone|plyr,"dplmc_constable_recruit_confirm_ask",
   [
    (assign, reg2, "$diplomacy_var"),
    (str_store_string, s6, "@{!}{reg2}"),
    (store_sub, ":offset", "$temp", "fac_kingdom_1"),
    (val_add, ":offset", "str_kingdom_1_adjective"),
    (str_store_string, s11, ":offset"),   
   ],
   "Do you really want to recruit {s6} {s11} peasants?", "dplmc_constable_recruit_confirm",[
 ]],
  
  [anyone|plyr,"dplmc_constable_recruit_confirm",
   [],
   "Yes.", "dplmc_constable_pretalk",[
    (call_script, "script_dplmc_send_recruiter", "$diplomacy_var", "$temp"),
 ]],

  [anyone|plyr,"dplmc_constable_recruit_confirm",
   [],
   "No.", "dplmc_constable_pretalk",[
 ]],

 
  [anyone|plyr,"dplmc_constable_recruit_amount_select",
   [],
   "None.", "dplmc_constable_pretalk",[
 ]],
 
  [anyone|plyr, "dplmc_constable_recruits_and_training",
  [
  ],
  "I changed my mind.", "dplmc_constable_pretalk", 
  []
  ],
 
  ##talk about security
   [anyone|plyr, "dplmc_constable_talk",
   [
   ],
   "Let's talk about patrols and troop movement.", "dplmc_constable_security_ask",
   []],
   
   [anyone, "dplmc_constable_security_ask",
   [
   ],
   "Of course.", "dplmc_constable_security",
   []],

  ##move tropps
   [anyone|plyr, "dplmc_constable_security",
   [],
   "I want to move troops to another location.", "dplmc_constable_move_troops",
   [
    (party_clear, "p_temp_party"),
    (assign, "$g_move_heroes", 1), 
    (call_script, "script_party_add_party", "p_temp_party", "p_main_party"),
    (party_clear, "p_main_party"),
    (party_remove_members, "p_main_party", "trp_player", 1), 
    
    (change_screen_exchange_members, 1),
   ]],   
   
   [anyone, "dplmc_constable_move_troops",
   [
   ],
   "Where do you want to move the troops?", "dplmc_constable_move_troops_location",
   []],

  [anyone|plyr|repeat_for_parties, "dplmc_constable_move_troops_location",
  [
    (store_repeat_object, ":party_no"),
    (is_between, ":party_no", towns_begin, castles_end),
    (neq, ":party_no", "$current_town"),
    (store_faction_of_party, ":party_faction", ":party_no"),
    (eq, ":party_faction", "$players_kingdom"),
    (str_store_party_name, s11, ":party_no"),
  ],
  "{!}{s11}.", "dplmc_constable_move_troops_location_confirm_ask", 
  [
    (store_repeat_object, "$diplomacy_var"),
    (party_clear, "p_temp_party_2"),
    (try_begin),
      (store_party_size, ":party_size", "p_main_party"),
      (gt, ":party_size", 0),
      (call_script, "script_party_add_party","p_temp_party_2", "p_main_party"),
      (party_clear, "p_main_party"),
      (party_stack_get_troop_id, ":troop_id", "p_main_party", 0), 
      
      (try_begin),
        (ge, ":troop_id", 0),
        (party_stack_get_size, ":troop_size", "p_main_party", 0),   
        (party_remove_members, "p_main_party",":troop_id",":troop_size"),
      (try_end),
      (party_stack_get_troop_id, ":troop_id", "p_main_party", 1), 
      (try_begin),
        (ge, ":troop_id", 0),
        (party_stack_get_size, ":troop_size", "p_main_party", 1),   
        (party_remove_members, "p_main_party",":troop_id",":troop_size"),
      (try_end),      
    (try_end),
    
    (call_script, "script_party_add_party", "p_main_party", "p_temp_party"),
    (assign, "$g_move_heroes", 0),
  ]],
  
  [anyone|plyr, "dplmc_constable_move_troops_location",
  [],
  "Nowhere.", "dplmc_constable_pretalk", 
  [
    (party_clear, "p_temp_party_2"),
    (try_begin),
      (store_party_size, ":party_size", "p_main_party"),
      (gt, ":party_size", 0),
      (call_script, "script_party_add_party","p_temp_party_2", "p_main_party"),
      (party_clear, "p_main_party"),
      (party_stack_get_troop_id, ":troop_id", "p_main_party", 0), 
      
      (try_begin),
        (ge, ":troop_id", 0),
        (party_stack_get_size, ":troop_size", "p_main_party", 0),   
        (party_remove_members, "p_main_party",":troop_id",":troop_size"),
      (try_end),
      (party_stack_get_troop_id, ":troop_id", "p_main_party", 1), 
      (try_begin),
        (ge, ":troop_id", 0),
        (party_stack_get_size, ":troop_size", "p_main_party", 1),   
        (party_remove_members, "p_main_party",":troop_id",":troop_size"),
      (try_end),      
    (try_end),
    
    (call_script, "script_party_add_party", "p_main_party", "p_temp_party"),
    (assign, "$g_move_heroes", 0),
    
    #reset town party
    (call_script, "script_party_add_party", "$current_town", "p_temp_party_2"),  
    (party_clear, "p_temp_party_2"),
  ]],
  
   [anyone, "dplmc_constable_move_troops_location_confirm_ask",
   [ 
    (store_party_size, ":party_size", "p_temp_party_2"),

  (assign, ":prisoner_size", 0),
  (party_get_num_prisoner_stacks, ":num_prisoner_stacks","p_temp_party_2"),
  (try_for_range_backwards, ":stack_no", 0, ":num_prisoner_stacks"),
    (party_prisoner_stack_get_size, ":stack_size","p_temp_party_2",":stack_no"),
    (val_add, ":prisoner_size", ":stack_size"),
  (try_end),

  (le, ":party_size", ":prisoner_size"),

   ],
   "You didn't choose any soldiers. Seems like you changed your mind.", "dplmc_constable_pretalk",
   []],
   
   [anyone, "dplmc_constable_move_troops_location_confirm_ask",
   [ 
    (str_store_party_name, s9, "$diplomacy_var"),
    (store_party_size, ":party_size", "p_temp_party_2"), #Diplomacy 3.2
    (store_mul, reg5, ":party_size", 5), #Diplomacy 3.2
   ],
   "Do you really want to send the troops to {s9}? This will cost us {reg5} denars.", "dplmc_constable_move_troops_location_confirm", #Diplomacy 3.2
   []],

   [anyone|plyr, "dplmc_constable_move_troops_location_confirm",
#Diplomacy 3.2 begin
   [
      (store_troop_gold, ":player_wealth", "trp_household_possessions"),
      (ge, ":player_wealth", reg5),
   ],
#Diplomacy 3.2 end
   "Yes.", "dplmc_constable_pretalk",
   [
    (call_script, "script_dplmc_withdraw_from_treasury", reg5), #Diplomacy 3.2
    (call_script, "script_dplmc_move_troops_party", "$current_town", "$diplomacy_var", "p_temp_party_2", "fac_player_faction", "trp_player"), #FLORIS BUGFIX adds "trp_player" argument
    (party_clear, "p_temp_party_2"),
   ]
   ],
   
   [anyone|plyr, "dplmc_constable_move_troops_location_confirm",
   [],
   "No. Let me check if we can afford that.", "dplmc_constable_pretalk", #Diplomacy 3.2
   [
    (call_script, "script_party_add_party", "$current_town", "p_temp_party_2"),  
    (party_clear, "p_temp_party_2"),
   ]], 
 
  ##send patrol
   [anyone|plyr, "dplmc_constable_security",
   [],
   "I want to enlist a patrol.", "dplmc_constable_patrol_size_ask",
   []],
   
   [anyone, "dplmc_constable_patrol_size_ask",
   [  
    (store_current_hours, ":current_hours"),
    (val_sub, ":current_hours", 24 * 7),
    (faction_get_slot, ":policy_time", "fac_player_faction", dplmc_slot_faction_patrol_time),
    (ge, ":current_hours", ":policy_time"),    
   ],
"You can take troops from your garrison or enlist fresh troops. In the latter case you can enlist a small patrol for 1000 denars, a medium patrol for 2000 denars or a big patrol for 3000 denars. You can also enlist a small elite patrol for 2000 denars. We have to pay weekly wages for the soldiers so make sure you have enough money in the treasury.", "dplmc_constable_patrol_size",
   []],
   

   [anyone, "dplmc_constable_patrol_size_ask",
   [  
   
    (store_current_hours, ":current_hours"),
    (val_sub, ":current_hours", 24 * 7),
    (faction_get_slot, ":policy_time", "fac_player_faction", dplmc_slot_faction_patrol_time),   
    (store_sub, ":wait_hours" , ":policy_time", ":current_hours"),
    (store_div, ":wait_days", ":wait_hours", 24),
    (store_mod, ":wait_mod", ":wait_hours", 24),
    (try_begin),
      (lt, ":wait_mod", 0),
      (val_add, ":wait_days", 1),
    (try_end),
    (assign, reg0, ":wait_days"), 
    
   ],
   "Currently there are no fresh troops available. We have to wait {reg0} days. But you can take troops from your garrison.", "dplmc_constable_patrol_size",
   []],

[anyone|plyr, "dplmc_constable_patrol_size",
[],
"Take troops out of the garrison.", "dplmc_constable_patrol_garrison",
[
(store_party_size_wo_prisoners, ":garrison_size", "$current_town"),			#zerilius changes
(gt, ":garrison_size", 0),								#zerilius changes
(party_clear, "p_temp_party"),
(assign, "$g_move_heroes", 1),
(call_script, "script_party_add_party", "p_temp_party", "p_main_party"),
(party_clear, "p_main_party"),
(party_remove_members, "p_main_party", "trp_player", 1),
       
    (change_screen_exchange_members, 1),
   ]],
   
#zerilius changes begin
[anyone, "dplmc_constable_patrol_garrison",
[
 (store_party_size_wo_prisoners, ":garrison_size", "$current_town"),
 (le, ":garrison_size", 0),
],
"We do not have any troops in the garrison.", "dplmc_constable_patrol_size",
[]],

[anyone, "dplmc_constable_patrol_garrison",
[],
"My {lord/lady}, lets muster the patrol troops.", "dplmc_constable_patrol_garrison_2",
[]],

[anyone, "dplmc_constable_patrol_garrison_2",
[
 (store_party_size_wo_prisoners, ":garrison_size", "p_main_party"),
 (le, ":garrison_size", 0),
 (party_add_members, "p_main_party", "trp_temp_troop", 1),				#zerilius included otherwise gives errors
],
"You didn't choose any soldiers. Seems like you changed your mind.", "dplmc_constable_pretalk",
[
(party_remove_members, "p_main_party", "trp_temp_troop", 1),
(call_script, "script_party_add_party", "p_main_party", "p_temp_party"),
(assign, "$g_move_heroes", 0),
]],
#zerilius changes end

[anyone, "dplmc_constable_patrol_garrison_2",
[
],
"Where do you want to send the patrol?", "dplmc_constable_patrol_garrison_location",
[]],

  [anyone|plyr|repeat_for_parties, "dplmc_constable_patrol_garrison_location",
  [
    (store_repeat_object, ":party_no"),
    (is_between, ":party_no", centers_begin, centers_end),
    (store_faction_of_party, ":party_faction", ":party_no"),
    (eq, ":party_faction", "$players_kingdom"),
    (str_store_party_name, s11, ":party_no"),
  ],
  "{!}{s11}.", "dplmc_constable_patrol_garrison_confirm_ask", 
  [
    (store_repeat_object, "$diplomacy_var"),
    (party_clear, "p_temp_party_2"),
    (call_script, "script_party_add_party","p_temp_party_2", "p_main_party"),
    (party_clear, "p_main_party"),
    (party_stack_get_troop_id, ":troop_id", "p_main_party", 0), 
    (try_begin),
      (ge, ":troop_id", 0),
      (party_stack_get_size, ":troop_size", "p_main_party", 0),   
      (party_remove_members, "p_main_party",":troop_id",":troop_size"),
    (try_end),
    (party_stack_get_troop_id, ":troop_id", "p_main_party", 1), 
    (try_begin),
      (ge, ":troop_id", 0),
      (party_stack_get_size, ":troop_size", "p_main_party", 1),   
      (party_remove_members, "p_main_party",":troop_id",":troop_size"),
    (try_end),
    
    (call_script, "script_party_add_party", "p_main_party", "p_temp_party"),
    (assign, "$g_move_heroes", 0),
  ]],


[anyone, "dplmc_constable_patrol_garrison_confirm_ask",
[
(store_party_size, ":party_size", "p_temp_party_2"),

  (assign, ":prisoner_size", 0),
  (party_get_num_prisoner_stacks, ":num_prisoner_stacks","p_temp_party_2"),
  (try_for_range_backwards, ":stack_no", 0, ":num_prisoner_stacks"),
    (party_prisoner_stack_get_size, ":stack_size","p_temp_party_2",":stack_no"),
    (val_add, ":prisoner_size", ":stack_size"),
  (try_end),

  (le, ":party_size", ":prisoner_size"),

],
"You didn't choose any soldiers. Seems like you changed your mind.", "dplmc_constable_pretalk",
[]],



[anyone, "dplmc_constable_patrol_garrison_confirm_ask",
[
    (str_store_party_name, s9, "$diplomacy_var"),
   ],
   "Do you really want to send the patrol to {s9}?", "dplmc_constable_patrol_garrison_confirm",
   []],

   [anyone|plyr, "dplmc_constable_patrol_garrison_confirm",
   [],
   "Yes.", "dplmc_constable_pretalk",
   [
	(call_script, "script_dplmc_send_patrol_party", "$current_town", "$diplomacy_var", "p_temp_party_2", "fac_player_faction", "trp_player"), #FLORIS BUGFIX adds "trp_player" argument
    (party_clear, "p_temp_party_2"),
   ]
   ],
   
   [anyone|plyr, "dplmc_constable_patrol_garrison_confirm",
   [],
   "No.", "dplmc_constable_pretalk",
   [
    (call_script, "script_party_add_party", "$current_town", "p_temp_party_2"),  
    (party_clear, "p_temp_party_2"),
   ]], 
   
   [anyone|plyr, "dplmc_constable_patrol_size",
   [ 
    (store_current_hours, ":current_hours"),
    (val_sub, ":current_hours", 24 * 7),
    (faction_get_slot, ":policy_time", "fac_player_faction", dplmc_slot_faction_patrol_time),
    (ge, ":current_hours", ":policy_time"), 
    
    (store_troop_gold,":gold","trp_household_possessions"), 
    (ge,":gold",1000),
   ],
   "A small one.", "dplmc_constable_patrol_location_ask",
   [
    (assign, "$temp", 0),
   ]],
   
   [anyone|plyr, "dplmc_constable_patrol_size",
   [
    (store_current_hours, ":current_hours"),
    (val_sub, ":current_hours", 24 * 7),
    (faction_get_slot, ":policy_time", "fac_player_faction", dplmc_slot_faction_patrol_time),
    (ge, ":current_hours", ":policy_time"),    
 
    (store_troop_gold,":gold","trp_household_possessions"), 
    (ge,":gold",2000),
   ],
   "A medium one.", "dplmc_constable_patrol_location_ask",
   [
    (assign, "$temp", 1),
   ]],
   
   [anyone|plyr, "dplmc_constable_patrol_size",
   [ 
    (store_current_hours, ":current_hours"),
    (val_sub, ":current_hours", 24 * 7),
    (faction_get_slot, ":policy_time", "fac_player_faction", dplmc_slot_faction_patrol_time),
    (ge, ":current_hours", ":policy_time"),     
    
    (store_troop_gold,":gold","trp_household_possessions"), 
    (ge,":gold",3000),
   ],
   "A big one.", "dplmc_constable_patrol_location_ask",
   [
    (assign, "$temp", 2),
   ]],
   
   [anyone|plyr, "dplmc_constable_patrol_size",
   [ 
    (store_current_hours, ":current_hours"),
    (val_sub, ":current_hours", 24 * 7),
    (faction_get_slot, ":policy_time", "fac_player_faction", dplmc_slot_faction_patrol_time),
    (ge, ":current_hours", ":policy_time"),     
       
    (store_troop_gold,":gold","trp_household_possessions"), 
    (ge,":gold",2000),
   ],
   "Get the best troops around.", "dplmc_constable_patrol_location_ask",
   [
    (assign, "$temp", 3),
   ]],
   
   [anyone|plyr, "dplmc_constable_patrol_size",
   [],
   "None.", "dplmc_constable_pretalk",
   []],
   
   [anyone, "dplmc_constable_patrol_location_ask",
   [],
   "Where do you want to send the patrol?", "dplmc_constable_patrol_location",
   []],
   
  [anyone|plyr|repeat_for_parties, "dplmc_constable_patrol_location",
  [
    (store_repeat_object, ":party_no"),
    (is_between, ":party_no", centers_begin, centers_end),
    (store_faction_of_party, ":party_faction", ":party_no"),
    (eq, ":party_faction", "$players_kingdom"),
    (str_store_party_name, s11, ":party_no"),
  ],
  "{!}{s11}.", "dplmc_constable_patrol_confirm_ask", 
  [
    (store_repeat_object, "$diplomacy_var"),
  ]
  ],  
  
   [anyone|plyr, "dplmc_constable_patrol_location",
   [],
   "Nowhere.", "dplmc_constable_pretalk",
   []],
  
   [anyone, "dplmc_constable_patrol_confirm_ask",
   [
    (assign, ":size", "str_dplmc_small"),
    (val_add, ":size", "$temp"),
    (str_store_string, s8, ":size"),
    (str_store_party_name, s9, "$diplomacy_var"),
   ],
   "Do you really want to send a {s8} patrol to {s9}?", "dplmc_constable_patrol_confirm",
   []],

   [anyone|plyr, "dplmc_constable_patrol_confirm",
   [],
   "Yes.", "dplmc_constable_pretalk",
   [
    (store_current_hours, ":current_hours"),
    (faction_set_slot, "fac_player_faction", dplmc_slot_faction_patrol_time, ":current_hours"),
    (call_script, "script_dplmc_send_patrol", "$current_town", "$diplomacy_var", "$temp", "$players_kingdom", "trp_player"), #Diplomacy 3.3.2
   ]
   ],
   
   [anyone|plyr, "dplmc_constable_patrol_confirm",
   [],
   "No.", "dplmc_constable_pretalk",
   []],  
   
   ##change patrol target
   [anyone|plyr, "dplmc_constable_security",
   [],
   "I want to change the target of a patrol.", "dplmc_constable_patrol_change_ask", #Diplomacy 3.3.2
   []],
   
   [anyone, "dplmc_constable_patrol_change_ask",
   [],
   "Which patrol should change the target?", "dplmc_constable_patrol_change",
   []],
   
  [anyone|plyr|repeat_for_parties, "dplmc_constable_patrol_change",
  [
    (store_repeat_object, ":party_no"),
    (party_slot_eq,":party_no", slot_party_type, spt_patrol),
    (party_slot_eq, ":party_no", dplmc_slot_party_mission_diplomacy, "trp_player"), #Diplomacy 3.3.2
    (str_store_party_name, s11, ":party_no"),
  ],
  "{!}{s11}.", "dplmc_constable_patrol_change_target_ask", 
  [
    (store_repeat_object, "$diplomacy_var"),
  ]],  
  
   [anyone|plyr, "dplmc_constable_patrol_change",
   [],
   "None.", "dplmc_constable_security_ask",
   []],  
  
   [anyone, "dplmc_constable_patrol_change_target_ask",
   [],
   "Where do you want to send it?", "dplmc_constable_patrol_change_target",
   []],
   
  [anyone|plyr|repeat_for_parties, "dplmc_constable_patrol_change_target",
  [
    (store_repeat_object, ":party_no"),
    (is_between, ":party_no", centers_begin, centers_end),
    (store_faction_of_party, ":party_faction", ":party_no"),
    (eq, ":party_faction", "$players_kingdom"),
    (str_store_party_name, s11, ":party_no"),
  ],
  "{!}{s11}.", "dplmc_constable_patrol_change_target_confirm_ask", 
  [
    (store_repeat_object, "$temp"),
  ]
  ],
  
   [anyone|plyr, "dplmc_constable_patrol_change_target",
   [],
   "Nowhere.", "dplmc_constable_security_ask",
   []],  
   
   [anyone, "dplmc_constable_patrol_change_target_confirm_ask",
   [
    (str_store_party_name, s5, "$diplomacy_var"),
    (str_store_party_name, s6, "$temp"),
   ],
   "As you wish, I will send a messenger carrying the orders to patrol {s6} to the {s5}.", "dplmc_constable_patrol_change_target_confirm",
   []],  
   
   [anyone|plyr, "dplmc_constable_patrol_change_target_confirm",
   [],
   "Thank you.", "dplmc_constable_security_ask",
   [    
    (call_script, "script_dplmc_send_messenger_to_party", "$diplomacy_var", spai_patrolling_around_center, "$temp"),
   ]],
   
   [anyone|plyr, "dplmc_constable_patrol_change_target_confirm",
   [],
   "Oh maybe not.", "dplmc_constable_security_ask",
   []],

   ##move patrol to center
   [anyone|plyr, "dplmc_constable_security",
   [],
   "I want a patrol to return to a center.", "dplmc_constable_patrol_to_center_ask",
   []],
   
   [anyone, "dplmc_constable_patrol_to_center_ask",
   [],
   "Which patrol should move to a center?", "dplmc_constable_patrol_to_center",
   []],
   
  [anyone|plyr|repeat_for_parties, "dplmc_constable_patrol_to_center",
  [
    (store_repeat_object, ":party_no"),
    (party_slot_eq,":party_no", slot_party_type, spt_patrol),
    (party_slot_eq, ":party_no", dplmc_slot_party_mission_diplomacy, "trp_player"), #Diplomacy 3.3.2
    (str_store_party_name, s11, ":party_no"),
  ],
  "{!}{s11}.", "dplmc_constable_patrol_to_center_target_ask", 
  [
    (store_repeat_object, "$diplomacy_var"),
  ]],  
  
   [anyone|plyr, "dplmc_constable_patrol_to_center",
   [],
   "None.", "dplmc_constable_security_ask",
   []],  
  
   [anyone, "dplmc_constable_patrol_to_center_target_ask",
   [],
   "Where do you want to send it?", "dplmc_constable_patrol_to_center_target",
   []],
   
  [anyone|plyr|repeat_for_parties, "dplmc_constable_patrol_to_center_target",
  [
    (store_repeat_object, ":party_no"),
    (is_between, ":party_no", centers_begin, centers_end),
    (store_faction_of_party, ":party_faction", ":party_no"),
    (eq, ":party_faction", "$players_kingdom"),
    (str_store_party_name, s11, ":party_no"),
  ],
  "{!}{s11}.", "dplmc_constable_patrol_change_to_center_confirm_ask", 
  [
    (store_repeat_object, "$temp"),
  ]
  ],
  
   [anyone|plyr, "dplmc_constable_patrol_to_center_target",
   [],
   "Nowhere.", "dplmc_constable_security_ask",
   []],  
   
   [anyone, "dplmc_constable_patrol_change_to_center_confirm_ask",
   [
    (str_store_party_name, s5, "$diplomacy_var"),
    (str_store_party_name, s6, "$temp"),
   ],
   "As you wish, I will send a messenger carrying the orders to move to {s6} to the {s5}.", "dplmc_constable_patrol_to_center_confirm",
   []],  
   
   [anyone|plyr, "dplmc_constable_patrol_to_center_confirm",
   [],
   "Thank you.", "dplmc_constable_security_ask",
   [    
    (call_script, "script_dplmc_send_messenger_to_party", "$diplomacy_var", spai_retreating_to_center, "$temp"),
   ]],
   
   [anyone|plyr, "dplmc_constable_patrol_to_center_confirm",
   [],
   "Oh maybe not.", "dplmc_constable_security_ask",
   []],
   
   ##disband patrol
   [anyone|plyr, "dplmc_constable_security",
   [],
   "I want to disband a patrol.", "dplmc_constable_patrol_disband_ask",
   []],
   
   [anyone, "dplmc_constable_patrol_disband_ask",
   [],
   "Which patrol do you want to disband?", "dplmc_constable_patrol_disband",
   []],
   
  [anyone|plyr|repeat_for_parties, "dplmc_constable_patrol_disband",
  [
    (store_repeat_object, ":party_no"),
    (party_slot_eq,":party_no", slot_party_type, spt_patrol),
    (party_slot_eq, ":party_no", dplmc_slot_party_mission_diplomacy, "trp_player"), #Diplomacy 3.3.2
    (str_store_party_name, s11, ":party_no"),
  ],
  "{!}{s11}.", "dplmc_constable_patrol_disband_confirm_ask", 
  [
    (store_repeat_object, "$diplomacy_var"),
  ]],  
  
   [anyone|plyr, "dplmc_constable_patrol_disband",
   [],
   "None.", "dplmc_constable_pretalk",
   []],   
  
   [anyone, "dplmc_constable_patrol_disband_confirm_ask",
   [
    (str_store_party_name, s5, "$diplomacy_var"),
   ],
   "As you wish, I will send a messenger who will tell {s5} to disband.", "dplmc_constable_patrol_disband_confirm",
   []],
   
   [anyone|plyr, "dplmc_constable_patrol_disband_confirm",
   [],
   "Thank you.", "dplmc_constable_security_ask",
   [
	##diplomacy start+
	#fix for the disbanding bug, credit Caba`drin
	#OLD:
	#(call_script, "script_dplmc_send_messenger_to_party", "$diplomacy_var", spai_retreating_to_center, -1),
	#NEW:
	(call_script, "script_dplmc_send_messenger_to_party", "$diplomacy_var", spai_undefined, -1),
	##diplomacy end+
   ]],  
   
   [anyone|plyr, "dplmc_constable_patrol_disband_confirm",
   [],
   "No.", "dplmc_constable_security_ask",
   []],  
   
   [anyone|plyr, "dplmc_constable_security",
   [],
   "Nevermind.", "dplmc_constable_pretalk",
   []],  
   
  ##prisoner
  [anyone|plyr,"dplmc_constable_talk",
   [(store_num_regular_prisoners,reg0),(ge,reg0,1)],
   "I have some prisoners can you sell them for me?", "dplmc_constable_prisoner",[]],

  [anyone,"dplmc_constable_prisoner", [],
  "Of course, Sire", "dplmc_constable_pretalk",
   [[change_screen_trade_prisoners]]],
   

  ##dismiss constable   
   [anyone|plyr, "dplmc_constable_talk",
   [
   ],
   "You are dismissed.", "dplmc_constable_dismiss_confirm_ask",
   []],
   
   [anyone, "dplmc_constable_dismiss_confirm_ask",
   [
   ],
   "Are you sure that you don't need me anymore?", "dplmc_constable_dismiss_confirm",
   []],
   
   [anyone|plyr, "dplmc_constable_dismiss_confirm",
   [
   ],
   "Yes I am.", "dplmc_constable_dismiss_confirm_yes",
   []],
   
   [anyone, "dplmc_constable_dismiss_confirm_yes",
   [
   ],
   "As you wish.", "close_window",
   [
    (assign, "$g_player_constable", -1),
    (assign, "$g_constable_training_center", -1),
   ]],
   
   [anyone|plyr, "dplmc_constable_dismiss_confirm",
   [
   ],
   "No I am not.", "dplmc_constable_pretalk",
   []],

   
  [anyone|plyr,"dplmc_constable_talk",
   [],
   "Thank you, I will come back to you later.", "close_window",[
 ]],



  [anyone,"start",
   [
    (eq, "$g_player_chamberlain","$g_talk_troop"),
    ],
   "Yes, Sire?", "dplmc_chamberlain_talk",[
   ]],
 
  [anyone,"dplmc_chamberlain_pretalk",
   [(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),],
    "Do you need anything else, {s0}?",  "dplmc_chamberlain_talk",[
    ]],
 
 
   [anyone|plyr, "dplmc_chamberlain_talk",
   [],
   "Please give me a report about the financial affairs.", "dplmc_chamberlain_overview",
   []], 
   
   [anyone, "dplmc_chamberlain_overview",
   [
    (assign, ":income", 0),  
    (assign, ":total_wage", 0),
    (assign, ":num_owned_center_values_for_tax_efficiency", 0),
    (try_for_range, ":selected_party", centers_begin, centers_end),
      (party_slot_eq, ":selected_party", slot_town_lord, "trp_player"),    
      
      (val_add, ":num_owned_center_values_for_tax_efficiency", 1),
  
      (party_get_slot, ":accumulated_rents", ":selected_party", slot_center_accumulated_rents),
      (val_add, ":income", ":accumulated_rents"),  
    
      (str_clear, s60),
      (try_begin),
        (this_or_next|party_slot_eq, ":selected_party", slot_party_type, spt_town),
        (party_slot_eq, ":selected_party", slot_party_type, spt_castle),
        (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
        
        (assign, ":troop_size", 0),
        (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", ":selected_party", ":i_stack"),
          (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
          (val_add, ":troop_size", ":stack_size"),
          (call_script, "script_game_get_troop_wage", ":stack_troop", ":selected_party"),
          (assign, ":cur_wage", reg0),
          (val_mul, ":cur_wage", ":stack_size"),
          (val_add, ":total_wage", ":cur_wage"),
        (try_end),
       
        (try_begin),
          (party_slot_eq, ":selected_party", slot_party_type, spt_town),
          
          (val_add, ":num_owned_center_values_for_tax_efficiency", 1),
          (party_get_slot, ":accumulated_tariffs", ":selected_party", slot_center_accumulated_tariffs),
          (assign, reg0, ":accumulated_tariffs"),
          (val_add, ":income", ":accumulated_tariffs"),
        (try_end),
      (try_end),   
    (try_end),
    (val_div, ":total_wage", 2), #Half payment for garrisons
    (assign, reg0, ":income"),
    (assign, reg1, ":total_wage"),
    
    (str_store_string, s6, "@We currently have an income of {reg0} denars and costs of {reg1} denars from fiefs and garrions."),
     
    (assign, ":tax_lost", 0),
    (try_begin),
      (gt, ":num_owned_center_values_for_tax_efficiency", 3),
      (store_sub, ":ratio_lost", ":num_owned_center_values_for_tax_efficiency", 3),
      (val_mul, ":ratio_lost", 9), 
      (val_min, ":ratio_lost", 140),
      (store_mul, ":tax_lost", ":income", ":ratio_lost"),
      (val_div, ":tax_lost", 200),
    (try_end),
    
    (try_begin),
      (gt, ":tax_lost", 0),
      (store_mul, ":tax_lost_percent", ":tax_lost", 100),
      (val_div, ":tax_lost_percent", ":income"),
      (assign, reg0, ":tax_lost"),
      (assign, reg1, ":tax_lost_percent"),
      (str_store_string, s6, "@{s6} We are losing {reg0} denars due to tax inefficiency. That means {reg1} percent."),
    (try_end),
    
    (assign, ":overall", ":income"),
    (val_sub, ":overall", ":total_wage"),
    (val_sub, ":overall", ":tax_lost"),
    (assign, reg0, ":overall"),
    (str_store_string, s6, "@{s6} Overall this sums up to {reg0} denars."),
   ],
   "{!}{s6}", "dplmc_chamberlain_pretalk",
   []], 
   
   [anyone|plyr, "dplmc_chamberlain_talk",
   [
   ],
   "Let us inspect the treasury.", "dplmc_chamberlain_treasury",
   []],  
   
   [anyone, "dplmc_chamberlain_treasury",
   [
     (store_troop_gold, ":treasury", "trp_household_possessions"),
     (assign, reg0, ":treasury"),
     (str_store_string, s4, "@{!}{reg0}"),
     (try_begin),
      (gt, "$g_player_debt_to_party_members", 0),
      (assign, reg0, "$g_player_debt_to_party_members"),
      (str_store_string, s6, "@{reg0} denars"),
     (else_try),
      (str_store_string, s6, "@no"),
     (try_end),
   ],
   "There are currently {s4} denars in the treasury and we have {s6} debts. What do you want to do?", "dplmc_chamberlain_treasury_action",
   []], 
  
   [anyone|plyr, "dplmc_chamberlain_treasury_action",
   [
   ],
   "I would like to pay into the treasury.", "dplmc_chamberlain_treasury_action_pay",
   []],  
   
   [anyone, "dplmc_chamberlain_treasury_action_pay",
   [
     (store_troop_gold, ":treasury", "trp_household_possessions"),
     (assign, reg0, ":treasury"),
     (str_store_string, s4, "@{!}{reg0}"),
   ],
   "We currently have {s4} denars in the treasury. How much money do you like to pay into the treasury, Sire?", "dplmc_chamberlain_treasury_action_pay_select",
   []],  
   
   [anyone|plyr, "dplmc_chamberlain_treasury_action_pay_select",
   [
    (store_troop_gold, ":gold", "trp_player"),
    (ge, ":gold", 100),
   ],
   "100.", "dplmc_chamberlain_treasury_action_pay",
   [
    (troop_remove_gold, "trp_player", 100),
    (call_script, "script_dplmc_pay_into_treasury", 100),
   ]], 
   
   [anyone|plyr, "dplmc_chamberlain_treasury_action_pay_select",
   [
    (store_troop_gold, ":gold", "trp_player"),
    (ge, ":gold", 200),
   ],
   "200.", "dplmc_chamberlain_treasury_action_pay",
   [
    (troop_remove_gold, "trp_player", 200),
    (call_script, "script_dplmc_pay_into_treasury", 200),
   ]], 
   
   [anyone|plyr, "dplmc_chamberlain_treasury_action_pay_select",
   [
    (store_troop_gold, ":gold", "trp_player"),
    (ge, ":gold", 500),
   ],
   "500.", "dplmc_chamberlain_treasury_action_pay",
   [
    (troop_remove_gold, "trp_player", 500),
    (call_script, "script_dplmc_pay_into_treasury", 500),
   ]], 
   
   [anyone|plyr, "dplmc_chamberlain_treasury_action_pay_select",
   [
    (store_troop_gold, ":gold", "trp_player"),
    (ge, ":gold", 1000),
   ],
   "1000.", "dplmc_chamberlain_treasury_action_pay",
   [
    (troop_remove_gold, "trp_player", 1000),
    (call_script, "script_dplmc_pay_into_treasury", 1000),
   ]],
   
   [anyone|plyr, "dplmc_chamberlain_treasury_action_pay_select",
   [
    (store_troop_gold, ":gold", "trp_player"),
    (ge, ":gold", 2000),
   ],
   "2000.", "dplmc_chamberlain_treasury_action_pay",
   [
    (troop_remove_gold, "trp_player", 2000),
    (call_script, "script_dplmc_pay_into_treasury", 2000),
   ]],
   
   [anyone|plyr, "dplmc_chamberlain_treasury_action_pay_select",
   [
    (store_troop_gold, ":gold", "trp_player"),
    (ge, ":gold", 5000),
   ],
   "5000.", "dplmc_chamberlain_treasury_action_pay",
   [
    (troop_remove_gold, "trp_player", 5000),
    (call_script, "script_dplmc_pay_into_treasury", 5000),
   ]],
   
   [anyone|plyr, "dplmc_chamberlain_treasury_action_pay_select",
   [
    (store_troop_gold, ":gold", "trp_player"),
    (ge, ":gold", 10000),
   ],
   "10000.", "dplmc_chamberlain_treasury_action_pay",
   [
    (troop_remove_gold, "trp_player", 10000),
    (call_script, "script_dplmc_pay_into_treasury", 10000),
   ]],
   
   [anyone|plyr, "dplmc_chamberlain_treasury_action_pay_select",
   [],
   "Never mind.", "dplmc_chamberlain_pretalk",
   []],
   
   [anyone|plyr, "dplmc_chamberlain_treasury_action",
   [
   ],
   "I would like to withdraw money from the treasury.", "dplmc_chamberlain_treasury_action_withdraw",
   []], 
   
   [anyone, "dplmc_chamberlain_treasury_action_withdraw",
   [
     (store_troop_gold, ":treasury", "trp_household_possessions"),
     (assign, reg0, ":treasury"),
     (str_store_string, s4, "@{!}{reg0}"),   
   ],
   "We currently have {s4} denars in the treasury. How much money do you like to withdraw from the treasury, Sire?", "dplmc_chamberlain_treasury_action_withdraw_select",
   []],  
   
   [anyone|plyr, "dplmc_chamberlain_treasury_action_withdraw_select",
   [
    (store_troop_gold, ":gold", "trp_household_possessions"),
    (ge, ":gold", 100),
   ],
   "100.", "dplmc_chamberlain_treasury_action_withdraw",
   [
    (call_script, "script_dplmc_withdraw_from_treasury", 100),
    (troop_add_gold, "trp_player", 100),
   ]],
   

   [anyone|plyr, "dplmc_chamberlain_treasury_action_withdraw_select",
   [
    (store_troop_gold, ":gold", "trp_household_possessions"),
    (ge, ":gold", 200),
   ],
   "200.", "dplmc_chamberlain_treasury_action_withdraw",
   [
    (call_script, "script_dplmc_withdraw_from_treasury", 200),
    (troop_add_gold, "trp_player", 200),
   ]],
   
   [anyone|plyr, "dplmc_chamberlain_treasury_action_withdraw_select",
   [
    (store_troop_gold, ":gold", "trp_household_possessions"),
    (ge, ":gold", 500),
   ],
   "500.", "dplmc_chamberlain_treasury_action_withdraw",
   [
    (call_script, "script_dplmc_withdraw_from_treasury", 500),
    (troop_add_gold, "trp_player", 500),
   ]],

   [anyone|plyr, "dplmc_chamberlain_treasury_action_withdraw_select",
   [
    (store_troop_gold, ":gold", "trp_household_possessions"),
    (ge, ":gold", 1000),
   ],
   "1000.", "dplmc_chamberlain_treasury_action_withdraw",
   [
    (call_script, "script_dplmc_withdraw_from_treasury", 1000),
    (troop_add_gold, "trp_player", 1000),
   ]],

   [anyone|plyr, "dplmc_chamberlain_treasury_action_withdraw_select",
   [
    (store_troop_gold, ":gold", "trp_household_possessions"),
    (ge, ":gold", 2000),
   ],
   "2000.", "dplmc_chamberlain_treasury_action_withdraw",
   [
    (call_script, "script_dplmc_withdraw_from_treasury", 2000),
    (troop_add_gold, "trp_player", 2000),
   ]],
   
   [anyone|plyr, "dplmc_chamberlain_treasury_action_withdraw_select",
   [
    (store_troop_gold, ":gold", "trp_household_possessions"),
    (ge, ":gold", 5000),
   ],
   "5000.", "dplmc_chamberlain_treasury_action_withdraw",
   [
    (call_script, "script_dplmc_withdraw_from_treasury", 5000),
    (troop_add_gold, "trp_player", 5000),
   ]], 
   
   [anyone|plyr, "dplmc_chamberlain_treasury_action_withdraw_select",
   [
    (store_troop_gold, ":gold", "trp_household_possessions"),
    (ge, ":gold", 10000),
   ],
   "10000.", "dplmc_chamberlain_treasury_action_withdraw",
   [
    (call_script, "script_dplmc_withdraw_from_treasury", 10000),
    (troop_add_gold, "trp_player", 10000),
   ]], 
   
   [anyone|plyr, "dplmc_chamberlain_treasury_action_withdraw_select",
   [],
   "Never mind.", "dplmc_chamberlain_pretalk",
   []],
 
   [anyone|plyr, "dplmc_chamberlain_treasury_action",
   [
   ],
   "Thank you, let's talk about something else.", "dplmc_chamberlain_pretalk",
   []],  


   [anyone|plyr, "dplmc_chamberlain_talk",
   [
   ],
   "Please give me a status report about the financial situation of a fief.", "dplmc_chamberlain_status",
   []], 
   
   [anyone, "dplmc_chamberlain_status",
   [],
   "About which fief do you like to be informed?", "dplmc_chamberlain_status_select_fief",
   []],  
   
   [anyone|plyr|repeat_for_parties, "dplmc_chamberlain_status_select_fief",
   [
    (store_repeat_object, ":party_no"),
    (is_between, ":party_no", centers_begin, centers_end),
    (party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
    (str_store_party_name, s60, ":party_no"),
   ],
   "{!}{s60}", "dplmc_chamberlain_status_info",
   [
    (store_repeat_object, "$diplomacy_var"),
   ]],
   
   [anyone|plyr, "dplmc_chamberlain_status_select_fief",
   [],
   "Never mind.", "dplmc_chamberlain_pretalk",
   []],
   
   [anyone, "dplmc_chamberlain_status_info",
   [
    (assign, ":selected_party", "$diplomacy_var"),
    (str_store_party_name, s60, ":selected_party"),
    (try_begin),
      (party_slot_ge, ":selected_party", slot_village_infested_by_bandits, 1),
      (str_store_string, s51, "@{s60} is currently occupied by outlaws you should counter them as soon as possible."),
    (else_try),
      (party_get_slot, ":relation", ":selected_party", slot_center_player_relation),
      (call_script, "script_describe_center_relation_to_s3", ":relation"),
      (party_get_slot, ":tax_rate", ":selected_party", dplmc_slot_center_taxation),
      (call_script, "script_dplmc_describe_tax_rate_to_s50", ":tax_rate"),
      
      (party_get_slot, ":accumulated_rents", ":selected_party", slot_center_accumulated_rents),
      (assign, reg0, ":accumulated_rents"),
      (str_store_string, s61, "@ We are expecting {reg0} denars for rents"),
      
      (assign, ":overall", ":accumulated_rents"),  
      (assign, ":total_wage", 0),
      (str_clear, s59),
      (try_begin),
        (this_or_next|party_slot_eq, ":selected_party", slot_party_type, spt_town),
        (party_slot_eq, ":selected_party", slot_party_type, spt_castle),
        (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
        
        (assign, ":troop_size", 0),
        (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", ":selected_party", ":i_stack"),
          (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
          (val_add, ":troop_size", ":stack_size"),
          (call_script, "script_game_get_troop_wage", ":stack_troop", ":selected_party"),
          (assign, ":cur_wage", reg0),
          (val_mul, ":cur_wage", ":stack_size"),
          (val_add, ":total_wage", ":cur_wage"),
        (try_end),
        (val_div, ":total_wage", 2), #Half payment for garrisons
        (assign, reg0, ":troop_size"),
        (assign, reg1, ":total_wage"),
        (str_store_string, s59, "@ The troop wages for {reg0} troops cost us {reg1} denars."),


        (try_begin),
          (party_slot_eq, ":selected_party", slot_party_type, spt_town),
          (party_get_slot, ":accumulated_tariffs", ":selected_party", slot_center_accumulated_tariffs),
          (assign, reg0, ":accumulated_tariffs"),
          (str_store_string, s61, "@{s61} and {reg0} denars for tariffs"),
          (val_add, ":overall", ":accumulated_tariffs"),
        (try_end),            
      (try_end),
      
      (try_begin),
        (this_or_next|is_between, ":selected_party", villages_begin, villages_end),
        (is_between, ":selected_party", towns_begin, towns_end),
        (call_script, "script_dplmc_describe_prosperity_to_s4", ":selected_party"),
      (else_try),
        (str_store_string, s4, "@Well, {s60}."),
      (try_end),
      
      (val_sub, ":overall", ":total_wage"),
      (assign, reg0, ":overall"),
      (str_store_string, s62, "@{!}{reg0}"),

      (str_store_string, s51, "@{s4} {s3}. The tax rate is {s50}.{s59}{s61}. Overall this sums up to {s62} denars."),
    (try_end),
   ],
   "{!}{s51}", "dplmc_chamberlain_status",
   []],    

   ##set taxes
   [anyone|plyr, "dplmc_chamberlain_talk",
   [
   ],
   "I wish to change the tax rate for a fief.", "dplmc_chamberlain_tax",
   []],
   
   [anyone, "dplmc_chamberlain_tax",
   [
   ],
   "For which fief?", "dplmc_chamberlain_tax_select_center",
   []],

   [anyone|plyr|repeat_for_parties, "dplmc_chamberlain_tax_select_center",
   [
    (store_repeat_object, ":center_no"),
    (this_or_next|is_between, ":center_no", towns_begin, towns_end),
    (is_between, ":center_no", villages_begin, villages_end),
    (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
    (store_faction_of_party, ":center_faction", ":center_no"),
    (this_or_next|eq, ":center_faction", "fac_player_supporters_faction"),
    (eq, ":center_faction", "$players_kingdom"),
    (str_store_party_name, s6, ":center_no"),
   ],
   "{!}{s6}", "dplmc_chamberlain_tax_ask_rate",
   [
    (store_repeat_object, "$diplomacy_var"), 
   ]],

   [anyone|plyr, "dplmc_chamberlain_tax_select_center",
   [
   ],
   "Never mind.", "dplmc_chamberlain_pretalk",
   []],
   
   [anyone, "dplmc_chamberlain_tax_ask_rate",
   [
    (str_store_party_name, s6, "$diplomacy_var"),
   ],
   "How high do you want to set the tax rate for {s6}?", "dplmc_chamberlain_tax_select_rate",
   [
   ]],
   
   [anyone|plyr, "dplmc_chamberlain_tax_select_rate",
   [
    (neg|party_slot_eq, "$diplomacy_var", dplmc_slot_center_taxation, -50),
   ],
   "Very low.", "dplmc_chamberlain_tax_ask_confirm",
   [
    (str_store_string, s11, "str_dplmc_tax_very_low"),
    (assign, "$diplomacy_tax_rate", -50),
   ]],
   
   [anyone|plyr, "dplmc_chamberlain_tax_select_rate",
   [
    (neg|party_slot_eq, "$diplomacy_var", dplmc_slot_center_taxation, -25),
   ],
   "Low.", "dplmc_chamberlain_tax_ask_confirm",
   [
    (str_store_string, s11, "str_dplmc_tax_low"),
    (assign, "$diplomacy_tax_rate", -25),
   ]],
   
   [anyone|plyr, "dplmc_chamberlain_tax_select_rate",
   [
    (neg|party_slot_eq, "$diplomacy_var", dplmc_slot_center_taxation, 0),
   ],
   "Normal.", "dplmc_chamberlain_tax_ask_confirm",
   [
    (str_store_string, s11, "str_dplmc_tax_normal"),   
    (assign, "$diplomacy_tax_rate", 0),
   ]],
   
   [anyone|plyr, "dplmc_chamberlain_tax_select_rate",
   [
    (neg|party_slot_eq, "$diplomacy_var", dplmc_slot_center_taxation, 25),
   ],
   "High.", "dplmc_chamberlain_tax_ask_confirm",
   [
    (str_store_string, s11, "str_dplmc_tax_high"),
    (assign, "$diplomacy_tax_rate", 25),
   ]],
   
   [anyone|plyr, "dplmc_chamberlain_tax_select_rate",
   [
    (neg|party_slot_eq, "$diplomacy_var", dplmc_slot_center_taxation, 50),
   ],
   "Very High.", "dplmc_chamberlain_tax_ask_confirm",
   [
    (str_store_string, s11, "str_dplmc_tax_very_high"),
    (assign, "$diplomacy_tax_rate", 50),   
   ]],
   
   [anyone|plyr, "dplmc_chamberlain_tax_select_rate",
   [
   ],
   "Never mind.", "dplmc_chamberlain_pretalk",
   []],
   
   [anyone, "dplmc_chamberlain_tax_ask_confirm",
   [
   ],
   "Do you really want to set the tax rate for {s6} to {s11}?", "dplmc_chamberlain_tax_confirm",
   []],
   
   [anyone|plyr, "dplmc_chamberlain_tax_confirm",
   [
   ],
   "Yes.", "dplmc_chamberlain_pretalk",
   [
    (party_set_slot, "$diplomacy_var", dplmc_slot_center_taxation, "$diplomacy_tax_rate"), 
    (display_message, "@Tax rate for {s6}: {s11}"),
   ]],
   
   [anyone|plyr, "dplmc_chamberlain_tax_confirm",
   [
   ],
   "No I changed, my mind.", "dplmc_chamberlain_pretalk",
   [  
   ]],
  
  ##buildings
   [anyone|plyr, "dplmc_chamberlain_talk",
   [  
   ],
   "I would like to manage fief improvements.", "dplmc_chamberlain_manage_fiefs",
   []], 
   
   [anyone, "dplmc_chamberlain_manage_fiefs",
   [
    (assign, ":fief_count", 0),
    (assign, ":center_count", 0),
    (assign, ":num_improvements", 0),
    (try_for_parties, ":center_no"),
      (this_or_next|is_between, ":center_no", towns_begin, towns_end),
      (is_between, ":center_no", villages_begin, villages_end),
      (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
      (store_faction_of_party, ":center_faction", ":center_no"),
      (this_or_next|eq, ":center_faction", "fac_player_supporters_faction"),
      (eq, ":center_faction", "$players_kingdom"),  
      
      (val_add, ":fief_count", 1),

      (try_begin),
        (party_slot_eq, ":center_no", slot_party_type, spt_village),
        (assign, ":begin", village_improvements_begin),
        (assign, ":end", village_improvements_end),
      (else_try),
        (party_slot_eq, ":center_no", slot_party_type, spt_town),
        (assign, ":begin", walled_center_improvements_begin),
        (assign, ":end", walled_center_improvements_end),
      (try_end),

      (assign, ":has_building", 0),
      (try_for_range, ":improvement_no", ":begin", ":end"),
        (party_slot_ge, ":center_no", ":improvement_no", 1),
        (val_add,  ":num_improvements", 1),
        (assign, ":has_building", 1),
      (try_end),
      
      (val_add, ":center_count", ":has_building"),
    
    (try_end), 
    
    (assign, reg0, ":num_improvements"),     
    (assign, reg1, ":center_count"),
    (assign, reg2, ":fief_count"),
      
   ],
   "We are currently have {reg0} improvements in {reg1} of your {reg2} fiefs. Do you want to build another one?", "dplmc_chamberlain_manage_fiefs_options",
   []],
 
   [anyone|plyr, "dplmc_chamberlain_manage_fiefs_options",
   [
   ],
   "Yes, I want to build an improvement.", "dplmc_chamberlain_manage_fiefs_build",
   []],
   
   [anyone|plyr, "dplmc_chamberlain_manage_fiefs_options",
   [
   ],
   "No.", "dplmc_chamberlain_pretalk",
   []],
   
   [anyone, "dplmc_chamberlain_manage_fiefs_build",
   [
   ],
   "Where do you want to build an improvement?", "dplmc_chamberlain_manage_fiefs_build_location",
   []],

  [anyone|plyr|repeat_for_parties, "dplmc_chamberlain_manage_fiefs_build_location",
   [
    (store_repeat_object, ":center_no"),
    (is_between, ":center_no", centers_begin, centers_end),
    (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
    (store_faction_of_party, ":center_faction", ":center_no"),
    (this_or_next|eq, ":center_faction", "fac_player_supporters_faction"),
    (eq, ":center_faction", "$players_kingdom"),  

    (assign, ":improvement_possible", 0),
    (try_begin),
      (party_slot_eq, ":center_no", slot_party_type, spt_village),
      (assign, ":begin", village_improvements_begin),
      (assign, ":end", village_improvements_end),
    (else_try),
      (assign, ":begin", walled_center_improvements_begin),
      (assign, ":end", walled_center_improvements_end),
    (try_end),

    (try_for_range, ":improvement_no", ":begin", ":end"),
      (party_slot_eq, ":center_no", ":improvement_no", 0),
      (assign, ":improvement_possible", 1),
    (try_end),
    (eq, ":improvement_possible", 1),
    
    (str_store_party_name, s2, ":center_no"),
    
   ],
   "{s2}.", "dplmc_chamberlain_manage_fiefs_build_ask",
   [
    (store_repeat_object, "$diplomacy_var"),
   ]],
   
  [anyone|plyr, "dplmc_chamberlain_manage_fiefs_build_location",
   [    
   ],
   "Nowhere.", "dplmc_chamberlain_pretalk",
   []],

   [anyone, "dplmc_chamberlain_manage_fiefs_build_ask",
   [

     (try_begin),
       (party_slot_eq, "$diplomacy_var", slot_party_type, spt_village),
       (assign, ":begin", village_improvements_begin),
       (assign, ":end", village_improvements_end),
       (str_store_string, s17, "@village"),
     (else_try),
       (assign, ":begin", walled_center_improvements_begin),
       (assign, ":end", walled_center_improvements_end),
       (party_slot_eq, "$diplomacy_var", slot_party_type, spt_town),
       (str_store_string, s17, "@town"),
     (else_try),
       (str_store_string, s17, "@castle"),
     (try_end),
     
     (assign, ":num_improvements", 0),
     (try_for_range, ":improvement_no", ":begin", ":end"),
       (party_slot_ge, "$diplomacy_var", ":improvement_no", 1),
       (val_add,  ":num_improvements", 1),
       (call_script, "script_get_improvement_details", ":improvement_no"),
       (try_begin),
         (eq,  ":num_improvements", 1),
         (str_store_string, s18, "@{!}{s0}"),
       (else_try),
         (str_store_string, s18, "@{!}{s18}, {s0}"),
       (try_end),
     (try_end),
     
     (try_begin),
       (eq,  ":num_improvements", 0),
       (str_store_string, s19, "@The {s17} has no improvements."),
     (else_try),
       (str_store_string, s19, "@The {s17} has the following improvements: {s18}."),
     (try_end),   

     (party_get_slot, ":cur_improvement", "$diplomacy_var", slot_center_current_improvement),
     (gt, ":cur_improvement", 0),
     (call_script, "script_get_improvement_details", ":cur_improvement"),
     (str_store_string, s7, s0),
     (assign, reg6, 1),
     (store_current_hours, ":cur_hours"),
     (party_get_slot, ":finish_time", "$diplomacy_var", slot_center_improvement_end_hour),
     (val_sub, ":finish_time", ":cur_hours"),
     (store_div, reg8, ":finish_time", 24),
     (val_max, reg8, 1),
     (store_sub, reg9, reg8, 1),

   ],
   "{s19}  You are currently building {s7}. The building will be completed after {reg8} day{reg9?s:}. We have to wait until it's finished.", "dplmc_chamberlain_pretalk",
   []],

   [anyone, "dplmc_chamberlain_manage_fiefs_build_ask",
   [

     (try_begin),
       (party_slot_eq, "$diplomacy_var", slot_party_type, spt_village),
       (assign, ":begin", village_improvements_begin),
       (assign, ":end", village_improvements_end),
       (str_store_string, s17, "@village"),
     (else_try),
       (assign, ":begin", walled_center_improvements_begin),
       (assign, ":end", walled_center_improvements_end),
       (party_slot_eq, "$diplomacy_var", slot_party_type, spt_town),
       (str_store_string, s17, "@town"),
     (else_try),
       (str_store_string, s17, "@castle"),
     (try_end),
     
     (assign, ":num_improvements", 0),
     (try_for_range, ":improvement_no", ":begin", ":end"),
       (party_slot_ge, "$diplomacy_var", ":improvement_no", 1),
       (val_add,  ":num_improvements", 1),
       (call_script, "script_get_improvement_details", ":improvement_no"),
       (try_begin),
         (eq,  ":num_improvements", 1),
         (str_store_string, s18, "@{!}{s0}"),
       (else_try),
         (str_store_string, s18, "@{!}{s18}, {s0}"),
       (try_end),
     (try_end),
     
     (try_begin),
       (eq,  ":num_improvements", 0),
       (str_store_string, s19, "@The {s17} has no improvements."),
     (else_try),
       (str_store_string, s19, "@The {s17} has the following improvements: {s18}."),
     (try_end),   
   ],
   "{s19}  What do you want to build?", "dplmc_chamberlain_manage_fiefs_build_ask2",
   []],
   
  [anyone|plyr, "dplmc_chamberlain_manage_fiefs_build_ask2",
   [
     (party_slot_eq, "$diplomacy_var", slot_party_type, spt_village),
     (party_slot_eq, "$diplomacy_var", slot_center_has_manor, 0),       
   ],
   "Build a manor.", "dplmc_chamberlain_manage_fiefs_build_confirm_ask",
   [(assign, "$g_improvement_type", slot_center_has_manor),]
   ],

  [anyone|plyr, "dplmc_chamberlain_manage_fiefs_build_ask2",
   [
     (party_slot_eq, "$diplomacy_var", slot_party_type, spt_village),
     (party_slot_eq, "$diplomacy_var", slot_center_has_fish_pond, 0),       
   ],
   "Build a mill.", "dplmc_chamberlain_manage_fiefs_build_confirm_ask",
   [(assign, "$g_improvement_type", slot_center_has_fish_pond),]
   ],

  [anyone|plyr, "dplmc_chamberlain_manage_fiefs_build_ask2",
   [
     (party_slot_eq, "$diplomacy_var", slot_party_type, spt_village),
     (party_slot_eq, "$diplomacy_var", slot_center_has_watch_tower, 0),       
   ],
   "Build a watch tower.", "dplmc_chamberlain_manage_fiefs_build_confirm_ask",
   [(assign, "$g_improvement_type", slot_center_has_watch_tower),]
   ],
   
  [anyone|plyr, "dplmc_chamberlain_manage_fiefs_build_ask2",
   [
     (party_slot_eq, "$diplomacy_var", slot_party_type, spt_village),
     (party_slot_eq, "$diplomacy_var", slot_center_has_school, 0),       
   ],
   "Build a school.", "dplmc_chamberlain_manage_fiefs_build_confirm_ask",
   [(assign, "$g_improvement_type", slot_center_has_school),]
   ],
   
  [anyone|plyr, "dplmc_chamberlain_manage_fiefs_build_ask2",
   [
     (party_slot_eq, "$diplomacy_var", slot_party_type, spt_village),
     (party_slot_eq, "$diplomacy_var", slot_center_has_messenger_post, 0),       
   ],
   "Build a messenger post.", "dplmc_chamberlain_manage_fiefs_build_confirm_ask",
   [(assign, "$g_improvement_type", slot_center_has_messenger_post),]
   ],

  [anyone|plyr, "dplmc_chamberlain_manage_fiefs_build_ask2",
   [
     (this_or_next|party_slot_eq, "$diplomacy_var", slot_party_type, spt_town),
     (party_slot_eq, "$diplomacy_var", slot_party_type, spt_castle),
     (party_slot_eq, "$diplomacy_var", slot_center_has_prisoner_tower, 0),       
   ],
   "Build a prisoner tower.", "dplmc_chamberlain_manage_fiefs_build_confirm_ask",
   [(assign, "$g_improvement_type", slot_center_has_prisoner_tower),]
   ],   

#Lazeras MODIFIED (Training Yard)
  [anyone|plyr, "dplmc_chamberlain_manage_fiefs_build_ask2",
   [
     (this_or_next|party_slot_eq, "$diplomacy_var", slot_party_type, spt_town),
     (party_slot_eq, "$diplomacy_var", slot_party_type, spt_castle),
     (party_slot_eq, "$diplomacy_var", slot_center_has_barracks, 0),       
   ],
   "Build a Barracks.", "dplmc_chamberlain_manage_fiefs_build_confirm_ask",
   [(assign, "$g_improvement_type", slot_center_has_barracks),]
   ], 
#Lazeras MODIFIED (Training Yard)

  [anyone|plyr, "dplmc_chamberlain_manage_fiefs_build_ask2",
   [    
   ],
   "Nothing.", "dplmc_chamberlain_pretalk",
   []],
   
   [anyone, "dplmc_chamberlain_manage_fiefs_build_confirm_ask",
   [
    (str_store_party_name, s2, "$diplomacy_var"),
    
     (call_script, "script_get_improvement_details", "$g_improvement_type"),
     (assign, ":improvement_cost", reg0),
     (str_store_string, s4, s0),
     (str_store_string, s19, s1),
     (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),
     (assign, reg2, ":max_skill"),

(store_sub, ":multiplier", 21, ":max_skill"),
(val_mul, ":improvement_cost", ":multiplier"),
(val_div, ":improvement_cost", 20),

(store_div, ":improvement_time", ":improvement_cost", 100),
(val_add, ":improvement_time", 4),

(assign, reg5, ":improvement_cost"),
(assign, reg6, ":improvement_time"),

(try_begin),
 (eq, ":max_skill_owner", "trp_player"),
 (assign, reg3, 1),
(else_try),
 (assign, reg3, 0),
 (str_store_troop_name, s3, ":max_skill_owner"),
(try_end),

(store_troop_gold, reg7, "trp_household_possessions"),
],
"Are you sure that you want to build a {s4} for {reg5} in {s2}? It will take {reg6} days. We currently have {reg7} denars in the treasury.", "dplmc_chamberlain_manage_fiefs_confirm",
[]],

[anyone|plyr, "dplmc_chamberlain_manage_fiefs_confirm",
[
(store_troop_gold, ":cur_gold", "trp_household_possessions"),
(ge, ":cur_gold", reg5),
],
"Yes.", "dplmc_chamberlain_pretalk",
[
(call_script, "script_dplmc_withdraw_from_treasury", reg5),
(party_set_slot, "$diplomacy_var", slot_center_current_improvement, "$g_improvement_type"),
(store_current_hours, ":cur_hours"),
(store_mul, ":hours_takes", reg6, 24),
(val_add, ":hours_takes", ":cur_hours"),
(party_set_slot, "$diplomacy_var", slot_center_improvement_end_hour, ":hours_takes"),
]],

[anyone|plyr, "dplmc_chamberlain_manage_fiefs_confirm",
[],
"No, I don't have the money.", "dplmc_chamberlain_pretalk",
[]],


##manage pools
   [anyone|plyr, "dplmc_chamberlain_talk",
   [
   ],
#Diplomacy 3.2 begin
   "I would like to manage the item pool and household.", "dplmc_chamberlain_pools_ask",
   []], 

   [anyone|plyr, "dplmc_chamberlain_pools_ask",
   [
   ],
   "What do you want to do?", "dplmc_chamberlain_pools",
   []],  

  ##item pool
   [anyone|plyr, "dplmc_chamberlain_pools",
   [
   ],
   "I would like to manage the item pool.", "dplmc_chamberlain_pools_end", #Floris - gear fix "dplmc_chamberlain_pretalk",
   [
   	#Floris - gear fix
	(try_for_range, ":i", ek_item_0, ek_food), #Double check worn gear is gone
		(agent_get_item_slot, ":item", "$g_talk_agent", ":i"),
		(gt, ":item", 0),
		(troop_remove_item, "$g_talk_troop", ":item"),
	(try_end),
	#Floris - end
   (change_screen_loot, "trp_dplmc_chamberlain"),]], 
   
    #Floris - gear fix - to allow for delay in returning gear
   [anyone,"dplmc_chamberlain_pools_end",[(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0")],"Do you need anything else, {s0}?", "dplmc_chamberlain_pools_end_2",[]],
   [anyone,"dplmc_chamberlain_pools_end_2",[(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0")],"Do you need anything else, {s0}?", "dplmc_chamberlain_talk",
   [
	(try_begin),
		(neg|agent_has_item_equipped,"$g_talk_agent", "itm_ar_swa_tun_tabard"),
		(agent_equip_item, "$g_talk_agent", "itm_ar_swa_tun_tabard"),
		(agent_equip_item, "$g_talk_agent", "itm_bo_swa_t2_hose"),
	(try_end),
   ]],
   #Floris - end

   [anyone|plyr, "dplmc_chamberlain_pools",
   [
   		(eq, "$g_autoloot", 1),  
      (store_skill_level, ":inv_skill", "skl_inventory_management", "trp_player"),
      (gt, "$g_player_chamberlain", 0),
      (ge, ":inv_skill", 3),   
   ],
   "Let my companions take the items out of the item pool.", "dplmc_chamberlain_item_pool",
   []],
   
   [anyone, "dplmc_chamberlain_item_pool",
   [
   ],
   "Are you sure you wish to do this?", "dplmc_chamberlain_item_pool_confirm",
   []],

   [anyone|plyr, "dplmc_chamberlain_item_pool_confirm",
   [
   ],
   "Yes.", "dplmc_chamberlain_pretalk",
   [
    (call_script, "script_auto_loot_all"),
   ]],
   
   [anyone|plyr, "dplmc_chamberlain_item_pool_confirm",
   [
   ],
   "No I changed, my mind.", "dplmc_chamberlain_pretalk",
   [  
   ]],

  ##household
   [anyone|plyr, "dplmc_chamberlain_pools",
   [
   ],
#Diplomacy 3.2 end
   "I would like to manage the household.", "dplmc_chamberlain_pretalk",
   [(change_screen_loot, "trp_household_possessions"),]],

#Diplomacy 3.2 begin
   [anyone|plyr, "dplmc_chamberlain_pools",
   [],
   "Nevermind.", "dplmc_chamberlain_pretalk",
   []],
#Diplomacy 3.2
   [anyone|plyr, "dplmc_chamberlain_talk",
   [
   ],
   "You are dismissed.", "dplmc_chamberlain_dismiss_confirm_ask",
   []],
   
   [anyone, "dplmc_chamberlain_dismiss_confirm_ask",
   [
   ],
   "Are you sure that you want to handle all financial affairs by yourself?", "dplmc_chamberlain_dismiss_confirm",
   []],
   
   [anyone|plyr, "dplmc_chamberlain_dismiss_confirm",
   [
   ],
   "Yes I am.", "dplmc_chamberlain_dismiss_confirm_yes",
   []],
   
   [anyone|plyr, "dplmc_chamberlain_dismiss_confirm",
   [
   ],
   "No I am not.", "dplmc_chamberlain_pretalk",
   []],
  
   [anyone, "dplmc_chamberlain_dismiss_confirm_yes",
   [
   ],
   "As you wish. Let's go through the documents and hand over your estate.", "close_window",
   [
    (assign, "$g_player_chamberlain", -1),
    (store_troop_gold, ":treasury", "trp_household_possessions"),
    (call_script, "script_dplmc_withdraw_from_treasury",  ":treasury"),
    (troop_add_gold, "trp_player", ":treasury"),
   ]],
   
  [anyone|plyr,"dplmc_chamberlain_talk",
   [],
   "Oh nothing, I just wanted to check the documents.", "close_window",[
 ]],
 

   ##hire staff
[anyone|plyr, "spouse_talk",
[
(assign, ":has_fief", 0),
(try_for_range, ":center_no", centers_begin, centers_end),
(party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
(eq, ":lord_troop_id", "trp_player"),
(assign, ":has_fief", 1),
(try_end),
	##diplomacy start+ remove superfluous
	#(try_begin),
	##diplomacy end+
	(eq, ":has_fief", 1),
	],
	"I want to hire a new staff member.", "dplmc_spouse_staff_talk_ask",
	[]],

	[anyone, "dplmc_spouse_staff_talk_ask",
	[
	],
	##diplomacy start+ rephrase
	#"Which staff member do you like to hire?", "dplmc_talk_staff",
	"What sort of staff member would you like to hire?", "dplmc_talk_staff",
	##diplomacy end+
	[]],

	##appoint constable
	[anyone|plyr, "dplmc_talk_staff",
	[
	(le, "$g_player_constable", 0),
	(assign, ":has_fief", 0),
	(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
		(party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
		(eq, ":lord_troop_id", "trp_player"),
		(assign, ":has_fief", 1),
	(try_end),
	##diplomacy start+ remove superfluous
	#(try_begin),
	##diplomacy end+
	(eq, ":has_fief", 1),
	],
	"I want to appoint a constable.", "dplmc_talk_appoint_constable",
	[]],

	##diplomacy start+
	#Variant: rehiring your constable
	[anyone, "dplmc_talk_appoint_constable",
	[(troop_slot_ge, "trp_dplmc_constable", slot_troop_met, 1),
	],
	"I assume you will want to rehire your former constable Miles de Gloucester?  His rate is still 15 denars each week, and the appointment will cost us 20 denars.", "dplmc_talk_appoint_constable_confirm", []],

	#Variant: Don't give the "friend of the family" description if it is not appropriate
	#(it might be for some companions in some mods, but by default it probably isn't)
	[anyone, "dplmc_talk_appoint_constable",
	[(is_between, "$g_talk_troop", companions_begin, companions_end),
	],
	"I have heard good things about a local nobleman by the name of Miles de Gloucester, and I believe he would be well-suited for the job. He demands 15 denars each week, though. The appointment will cost us 20 denars.", "dplmc_talk_appoint_constable_confirm",
	[]],
	##diplomacy end+

	[anyone, "dplmc_talk_appoint_constable",
	[
	],
	"That's a wise idea. May I suggest a very capable nobleman and friend of my family? His name is Miles de Gloucester. He demands 15 denars each week, though. The appointment will cost us 20 denars.", "dplmc_talk_appoint_constable_confirm",
	[]],

	[anyone|plyr, "dplmc_talk_appoint_constable_confirm",
	[
	(store_troop_gold, ":gold", "trp_player"),
	(ge, ":gold", 20),
	],
	"So be it.", "dplmc_talk_appoint_confirm_yes",
	[
	(call_script, "script_dplmc_appoint_constable"),
	(troop_remove_gold, "trp_player", 20),
	]],

	[anyone|plyr, "dplmc_talk_appoint_constable_confirm",
	[
	(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
	##diplomacy start+ Handle non-reflexive spouse slots (for example, for polygamy)
	(this_or_next|troop_slot_eq, "$g_talk_troop", slot_troop_spouse, "trp_player"),
		(eq, "$g_talk_troop", ":player_spouse"),
	(this_or_next|is_between, "$g_talk_troop", heroes_begin, heroes_end),#slot_troop_spouse may not be initialized to -1
	 ##diplomacy end+
	(eq, "$g_talk_troop", ":player_spouse"),
	(this_or_next|is_between, "$g_talk_troop", heroes_begin, heroes_end),#slot_troop_spouse may not be initialized to -1
	 ##diplomacy end+
	(eq, "$g_talk_troop", ":player_spouse"),
	],
	"Maybe later.", "spouse_pretalk",
	[]],

	[anyone|plyr, "dplmc_talk_appoint_constable_confirm",
	[
	(eq, "$g_talk_troop", "$g_player_minister"),
	(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
	##diplomacy start+ Handle non-reflexive spouse slots (for example, for polygamy)
	(this_or_next|neg|is_between, "$g_talk_troop", heroes_begin, heroes_end),#slot_troop_spouse may not be initialized to -1
	   (neg|troop_slot_eq, "$g_talk_troop", slot_troop_spouse, "trp_player"),
	##diplomacy end+
	(neq, ":player_spouse", "$g_player_minister"),
	],
	"Maybe later.", "minister_pretalk",
	[]],

	[anyone, "dplmc_talk_appoint_confirm_yes",
	[
	(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
	##diplomacy start+ Handle non-reflexive spouse slots (for example, for polygamy)
	(this_or_next|troop_slot_eq, "$g_talk_troop", slot_troop_spouse, "trp_player"),
		(eq, "$g_talk_troop", ":player_spouse"),
	(this_or_next|is_between, "$g_talk_troop", heroes_begin, heroes_end),#slot_troop_spouse may not be initialized to -1
	 ##diplomacy end+
	(eq, "$g_talk_troop", ":player_spouse"),
	],
	"I will send him a letter he should arrive at the court soon.", "spouse_pretalk",
	[]],

	[anyone, "dplmc_talk_appoint_confirm_yes",
	[
	(eq, "$g_talk_troop", "$g_player_minister"),
	],
	"I will send him a letter he should arrive at the court soon.", "minister_pretalk",
	[]],


	##appoint chamberlain
[anyone|plyr, "dplmc_talk_staff",
[
(le, "$g_player_chamberlain", 0),
(assign, ":has_fief", 0),
(try_for_range, ":center_no", centers_begin, centers_end),
	(party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
	(eq, ":lord_troop_id", "trp_player"),
	(assign, ":has_fief", 1),
(try_end),
	##diplomacy start+ remove superfluous
	#(try_begin),
	##diplomacy end+
	(eq, ":has_fief", 1),
	],
	"I want to appoint a chamberlain to handle financial affairs.", "dplmc_talk_appoint_chamberlain",
	[]],

	##diplomacy start+
	#Variant: rehiring a former employee
	[anyone, "dplmc_talk_appoint_chamberlain",
	[(troop_slot_ge, "trp_dplmc_chamberlain", slot_troop_met, 1),
	],
	"I assume you will want to rehire your former chamberlain Aubrey de Vere?  His rate is still 15 denars each week, and the appointment will cost us 20 denars.", "dplmc_talk_appoint_chamberlain_confirm", []],

	#Variant: Don't give the "friend of the family" description if it is not appropriate
	#(it might be for some companions in some mods, but by default it probably isn't)
	[anyone, "dplmc_talk_appoint_chamberlain",
	[(is_between, "$g_talk_troop", companions_begin, companions_end),
	],
	"I have heard good things about a local nobleman by the name of Aubrey de Vere, and I believe he would be well-suited for the job. He demands 15 denars each week, though. The appointment will cost us 20 denars.", "dplmc_talk_appoint_chamberlain_confirm",
	[]],
	##diplomacy end+
	[anyone, "dplmc_talk_appoint_chamberlain",
	[
	],
   "That's a wise idea. May I suggest a very capable nobleman and friend of my family? His name is Aubrey de Vere. He demands 15 denars each week, though. The appointment will cost us 20 denars.", "dplmc_talk_appoint_chamberlain_confirm",
   []],
   
   [anyone|plyr, "dplmc_talk_appoint_chamberlain_confirm",
   [
     (store_troop_gold, ":gold", "trp_player"),
     (ge, ":gold", 20),
   ],
   "So be it.", "dplmc_talk_appoint_confirm_yes",
   [
        (call_script, "script_dplmc_appoint_chamberlain"),
        (troop_remove_gold, "trp_player", 20),
   ]],
   
	[anyone|plyr, "dplmc_talk_appoint_chamberlain_confirm",
	[
	(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
	##diplomacy start+
	(this_or_next|troop_slot_eq, "$g_talk_troop", slot_troop_spouse, "trp_player"),
		(troop_slot_eq, "trp_player", slot_troop_spouse, "$g_talk_troop"),
	(this_or_next|is_between, "$g_talk_troop", heroes_begin, heroes_end),
	##diplomacy end+
	(eq, "$g_talk_troop", ":player_spouse"),
	],
	"Maybe later.", "spouse_pretalk",
	[]],

	[anyone|plyr, "dplmc_talk_appoint_chamberlain_confirm",
	[
	(eq, "$g_talk_troop", "$g_player_minister"),
	(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
	##diplomacy start+
	(this_or_next|neg|troop_slot_eq, "$g_talk_troop", slot_troop_spouse, "trp_player"),
		(neg|is_between, "$g_talk_troop", heroes_begin, heroes_end),
	##diplomacy end+
	(neq, ":player_spouse", "$g_player_minister"),
	],
	"Maybe later.", "minister_pretalk",
	[]],

	##appoint chancellor
	[anyone|plyr, "dplmc_talk_staff",
	[
	(le, "$g_player_chancellor", 0),
	(assign, ":has_fief", 0),
	(try_for_range, ":center_no", towns_begin, towns_end),
		(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
		(assign, ":has_fief", 1),
	(try_end),
	(eq, ":has_fief", 1),
	],
	"I want to appoint a chancellor.", "dplmc_talk_appoint_chancellor",
	[]],

	##diplomacy start+
	#Variant: rehiring a former employee
	[anyone, "dplmc_talk_appoint_chancellor",
	[(troop_slot_ge, "trp_dplmc_chamberlain", slot_troop_met, 1),
	],
	"I assume you will want to rehire your former chancellor Herfast?  His rate is still 20 denars each week, and the appointment will cost us 20 denars.", "dplmc_talk_appoint_chancellor_confirm", []],

	#Variant: Don't give the "friend of the family" description if it is not appropriate
	#(it might be for some companions in some mods, but by default it probably isn't)
	[anyone, "dplmc_talk_appoint_chancellor",
	[(is_between, "$g_talk_troop", companions_begin, companions_end),
	],
	"I have heard good things about a local nobleman by the name of Herfast, and I believe he would be well-suited for the job. He demands 20 denars each week, though. The appointment will cost us 20 denars.", "dplmc_talk_appoint_chancellor_confirm",
	[]],
	##diplomacy end+
	[anyone, "dplmc_talk_appoint_chancellor",
	[
	],
	"That's a wise idea. May I suggest a very capable nobleman and friend of my family? His name is Herfast. He demands 20 denars each week, though. The appointment will cost us 20 denars.", "dplmc_talk_appoint_chancellor_confirm",
	[]],
   
   [anyone|plyr, "dplmc_talk_appoint_chancellor_confirm",
   [
     (store_troop_gold, ":gold", "trp_player"),
     (ge, ":gold", 20),
   ],
   "So be it.", "dplmc_talk_appoint_confirm_yes",
   [
        (call_script, "script_dplmc_appoint_chancellor"),
        (troop_remove_gold, "trp_player", 20),
   ]],
   
   [anyone|plyr, "dplmc_talk_appoint_chancellor_confirm",
   [
    (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
    (eq, "$g_talk_troop", ":player_spouse"),
   ],
   "Maybe later.", "spouse_pretalk",
   []],
   
   [anyone|plyr, "dplmc_talk_appoint_chancellor_confirm",
   [
     (eq, "$g_talk_troop", "$g_player_minister"),
     (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
     (neq, ":player_spouse", "$g_player_minister"),     
   ],
   "Maybe later.", "minister_pretalk",
   []],
   
   [anyone|plyr, "dplmc_talk_staff",
   [
   (eq, "$g_talk_troop", "$g_player_minister"),
   ],
   "None.", "minister_pretalk",
   []],
   
   [anyone|plyr, "dplmc_talk_staff",
   [
    (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
    (eq, "$g_talk_troop", ":player_spouse"),
    (neq, ":player_spouse", "$g_player_minister"),
   ],
   "None.", "spouse_pretalk",
   []],

   ##buy food
   [anyone|plyr, "spouse_talk",
	[ ##diplomacy start+
	#
	##OLD:
	#(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
	#(troop_slot_ge, ":player_spouse", slot_troop_cur_center, -1),
	##NEW:
	(assign, ":player_spouse", "$g_talk_troop"),
	(troop_slot_ge, ":player_spouse", slot_troop_cur_center, -1),#what is the point of this?
	##Also, to avoid strange bugs, do not enable this for heroes or ministers
(neg|troop_slot_eq, ":player_spouse", slot_troop_occupation, slto_kingdom_hero),
(neq, "$g_talk_troop", "$g_player_minister"),
(neg|troop_slot_ge, ":player_spouse", slot_troop_leaded_party, 1),
(neg|troop_slot_ge, ":player_spouse", slot_troop_prisoner_of_party, 0),
	##diplomacy end+

#make sure no spouse party exists
(assign, ":spouse_party_exists", 0),
(try_for_parties, ":spouse_party"),
  (party_slot_eq, ":spouse_party", slot_party_type, dplmc_spt_spouse),
  (assign, ":spouse_party_exists", 1),
(try_end),
(neq, ":spouse_party_exists", 1),

	],
	"Can you please buy some bread?", "dplmc_spouse_talk_buy_food_amount_ask",
	[]],

	[anyone, "dplmc_spouse_talk_buy_food_amount_ask",
	[
	],
	##diplomacy start+ "like" to "want"
	"How much bread do you want?", "dplmc_spouse_talk_buy_food_amount",
	##diplomacy end+
	[]],
   
   [anyone|plyr, "dplmc_spouse_talk_buy_food_amount",
   [
   ],
   "{!}50.", "dplmc_spouse_talk_buy_food",
   [
    (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse), 
    (troop_set_slot, ":player_spouse", dplmc_slot_troop_mission_diplomacy, 1),   
   ]],
   
   [anyone|plyr, "dplmc_spouse_talk_buy_food_amount",
   [
   ],
   "{!}100.", "dplmc_spouse_talk_buy_food",
   [
    (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse), 
    (troop_set_slot, ":player_spouse", dplmc_slot_troop_mission_diplomacy, 2),
   ]],
   
   [anyone|plyr, "dplmc_spouse_talk_buy_food_amount",
   [
   ],
   "{!}150.", "dplmc_spouse_talk_buy_food",
   [
    (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse), 
    (troop_set_slot, ":player_spouse", dplmc_slot_troop_mission_diplomacy, 3),
   ]],
   
   [anyone|plyr, "dplmc_spouse_talk_buy_food_amount",
   [
   ],
   "{!}200.", "dplmc_spouse_talk_buy_food",
   [
    (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse), 
    (troop_set_slot, ":player_spouse", dplmc_slot_troop_mission_diplomacy, 4),
   ]],
   
   [anyone|plyr, "dplmc_spouse_talk_buy_food_amount",
   [
   ],
   "Nothing.", "spouse_pretalk",
   []],

   [anyone, "dplmc_spouse_talk_buy_food",
   [  
    (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse), 
    (troop_slot_eq, ":player_spouse", slot_troop_cur_center, "$current_town"), 
    (troop_get_slot, ":amount", ":player_spouse", dplmc_slot_troop_mission_diplomacy), 
     
    (assign, ":can_leave", 1),
    (try_begin),
      (is_between,"$current_town",castles_begin, castles_end),
      (try_begin),
       (is_between, "$current_town", walled_centers_begin, walled_centers_end),
       (neg|party_slot_eq, "$current_town", slot_center_is_besieged_by, -1),
       (assign, ":can_leave", 0),
      (try_end),
    (try_end),
    (eq, ":can_leave", 1),

    (assign, ":mission_object", -1),
    (try_begin),
      (store_faction_of_party, ":party_faction", "$current_town"),
      (assign, ":distance", 1000),
      (try_for_range, ":center_no", centers_begin, centers_end),
        (neg|is_between, ":center_no", castles_begin, castles_end),
        (store_faction_of_party, ":center_faction", ":center_no"),          
        (eq, ":center_faction", ":party_faction"),        
        
        (assign, ":proceed", 1),
        (try_begin),
          (is_between, ":center_no", towns_begin, towns_end),
          (party_get_slot,":cur_merchant",":center_no",slot_town_merchant),
        (else_try),
          (is_between, ":center_no", villages_begin, villages_end),
          (party_get_slot,":cur_merchant",":center_no", slot_town_elder),
          (neg|party_slot_eq, ":center_no", slot_village_state, svs_normal),
          (assign, ":proceed", 0),
        (try_end),
        (eq, ":proceed", 1),
        
        
        (troop_get_inventory_capacity, ":capacity", ":cur_merchant"),  
        (assign, ":bread_amount", 0),
    	  (try_for_range, ":inventory_slot", 0, ":capacity"),
    		  (troop_get_inventory_slot, ":item", ":cur_merchant", ":inventory_slot"),	  
    		  (eq, ":item", "itm_trade_bread"),
    		  (val_add, ":bread_amount", 1),
    		(try_end),
    		(ge, ":bread_amount", ":amount"),
        
        (store_distance_to_party_from_party, ":tmp_distance", ":center_no", "$current_town"),
        (lt, ":tmp_distance", ":distance"),
        (assign, ":distance", ":tmp_distance"),
        
        (assign, ":mission_object", ":center_no"),
      (try_end),
    (try_end),
    
    (neq, ":mission_object", -1),
    (troop_set_slot, ":player_spouse", slot_troop_mission_object, ":mission_object"),   

	##nested diplomacy start+
	#(call_script, "script_dplmc_get_item_buy_price_factor", "itm_trade_bread", ":mission_object"),
	#Use player skill for now (we could revisit this, but it's not important)
	(call_script, "script_dplmc_get_item_buy_price_factor", "itm_trade_bread", ":mission_object", "trp_player", -1),
	##nested diplomacy end+
	(store_item_value, ":value", "itm_trade_bread"),
	(store_mul, ":price", ":value", reg0),
	(val_div, ":price", 100),
	(val_max, ":price", 1),
	(val_mul, ":price", ":amount"),
	(assign, reg0, ":price"),
	(str_store_party_name, s6, ":mission_object"),
   ],
   "Yes of course, I will go to the merchant in {s6} and buy some bread. This will cost us {reg0} denars.", "dplmc_spouse_talk_buy_food_confirm",
   []],
   
   [anyone, "dplmc_spouse_talk_buy_food",
   [   
   ],
   "Currently no merchant has enough bread. We have to wait.", "spouse_pretalk",
   []],
   
   ##confirm spouse buy food
   [anyone|plyr, "dplmc_spouse_talk_buy_food_confirm",
   [
     (store_troop_gold, ":gold", "trp_player"),
     (ge, ":gold", reg0),
   ],
   "Ok, we can afford that, please go. Thank you.", "close_window",
   [
    (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse), 
    (troop_get_slot, ":mission_object", ":player_spouse", slot_troop_mission_object),
    (troop_remove_gold, "trp_player", reg0),
    (try_begin),
      (neq, ":mission_object", "$current_town"),
      
      (try_begin),               
        (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),    

        (set_spawn_radius, 1),
        (spawn_around_party, "$g_encountered_party", "pt_dplmc_spouse"),
        (assign, ":spouse_party", reg0),
        
        (party_add_members, ":spouse_party", ":player_spouse", 1),
        (party_set_faction, ":spouse_party", "fac_neutral"), #no capture
        (party_set_slot, ":spouse_party", slot_party_home_center, "$g_encountered_party"),
        (party_set_slot, ":spouse_party", slot_party_type, dplmc_spt_spouse), 
        (party_set_slot, ":spouse_party", slot_party_orders_object, ":mission_object"),     
        (party_set_ai_object, ":spouse_party", ":mission_object"),   
        (party_set_ai_behavior, ":spouse_party", ai_bhvr_travel_to_party),
        (party_set_slot, ":spouse_party", slot_party_ai_state, spai_undefined),
        (troop_set_slot, ":player_spouse", slot_troop_cur_center, -1), 
      (try_end),
    (else_try), 
      (party_get_slot,":cur_merchant",":mission_object",slot_town_merchant), 
      (troop_remove_items, ":cur_merchant", "itm_trade_bread", 2),
      (troop_add_items, "trp_household_possessions", "itm_trade_bread", 2),
    (try_end),
   ]],
   
   [anyone|plyr, "dplmc_spouse_talk_buy_food_confirm",
   [
   ],
   "Oh, maybe later.", "close_window",
   [
   ]],
 
   ##hire staff
   [anyone|plyr, "minister_talk",
	[
	(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
	(neq,"$g_talk_troop",":player_spouse"), #only if spouse != minister
	(assign, ":has_fief", 0),
(try_for_range, ":center_no", centers_begin, centers_end),
		(party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
		(eq, ":lord_troop_id", "trp_player"),
		(assign, ":has_fief", 1),
	(try_end),
	##diplomacy start+ remove superfluous
	#(try_begin),
	##diplomacy end+
	(eq, ":has_fief", 1),
	],
	"I want to hire a new staff member.", "dplmc_minister_staff_talk_ask",
	[]],

	[anyone, "dplmc_minister_staff_talk_ask",
	[
	],
	##diplomacy start+ rephrase
	#"Which staff member do you like to hire?", "dplmc_talk_staff",
	"What sort of staff member would you like to hire?", "dplmc_talk_staff",
	##diplomacy end+
	[]],
  
  ## FLORIS 2.52+ ## - Allow players to end mercenary contract by speaking to liege. - Windyplains
  ##return fief to king
	[anyone|plyr,"lord_talk", 
		[
			(le,"$talk_context", tc_party_encounter),
			(ge, "$g_talk_troop_faction_relation", 0),
			(neg|troop_slot_ge, "$g_talk_troop", slot_troop_prisoner_of_party, 0),
			(faction_slot_eq, "$g_talk_troop_faction", slot_faction_leader, "$g_talk_troop"),
			(store_current_day, ":date"),
			(lt, ":date", "$mercenary_service_next_renew_day"),
			(eq, "$players_kingdom", "$g_talk_troop_faction"),
			(eq, "$player_has_homage", 0),
			(neq, reg51, ":date"),
		], "{s66}, my men and I wish to end our contract with you.", "floris_end_mercenary_contract",
		[
			(store_current_day, reg51),
		]],
	
	[anyone,"floris_end_mercenary_contract", 
		[], "I see.  Well you serve only at the loyalty of my coin.  Are you sure wish to leave my service?", "floris_end_mercenary_contract_verify",
		[]],
		
	[anyone|plyr,"floris_end_mercenary_contract_verify", 
		[], "Yes, {s66}.  My men have had enough of war for the time being.", "floris_end_mercenary_contract_leaving",
		[]],
		
	[anyone|plyr,"floris_end_mercenary_contract_verify", 
		[], "On second thought, we are in no rush to be any where else.", "floris_end_mercenary_contract_staying",
		[]],
		
	[anyone,"floris_end_mercenary_contract_leaving", 
		[], "Very well, your path is your own, but I warn you not to take up arms for my enemies or my men will run you through all the same.", "lord_talk",
		[
			(call_script, "script_player_leave_faction", 1),
			(str_store_troop_name_link, s21, "$g_talk_troop"),
			(display_message, "@You have left the service of {s21}."),
		]],
		
	[anyone,"floris_end_mercenary_contract_staying", 
		[], "Glad to hear it.  Keep up the good work and perhaps one day you will join me as a vassal with lands of your own.", "lord_talk",
		[]],
  ## FLORIS 2.52- ##
  
  ##return fief to king
  [anyone|plyr,"lord_talk", [
    (le,"$talk_context", tc_party_encounter),
    (ge, "$g_talk_troop_faction_relation", 0),
    #(troop_slot_eq, "$g_talk_troop", slot_troop_is_prisoner, 0),
    (neg|troop_slot_ge, "$g_talk_troop", slot_troop_prisoner_of_party, 0),
    (faction_slot_eq, "$g_talk_troop_faction", slot_faction_leader, "$g_talk_troop"),
    (eq, "$players_kingdom", "$g_talk_troop_faction"),
    (eq, "$player_has_homage", 1),
  ],
   "{s66}, I want to give up a fief you enfeoffed to me.", "dplmc_lord_give_back_fief",[
  ]],
  
   [anyone, "dplmc_lord_give_back_fief",
   [
   ], "Oh, so you can't manage it? Well, which fief do you have in mind?", "dplmc_lord_give_back_fief_select",
   []],

  [anyone|plyr|repeat_for_parties,"dplmc_lord_give_back_fief_select", [
		(store_repeat_object, ":center"),
    (is_between, ":center", centers_begin, centers_end),
		(neq, ":center", "$g_player_court"), #court can't be returned
    (party_slot_eq, ":center", slot_center_is_besieged_by, -1), 
		(party_slot_eq, ":center", slot_town_lord, "trp_player"),
		(str_store_party_name, s11, ":center"),
  ],
   "{!}{s11}.", "dplmc_lord_give_back_fief_confirm_ask",[
   (store_repeat_object, "$diplomacy_var"),
  ]],
  
  [anyone|plyr,"dplmc_lord_give_back_fief_select", [],
   "Never mind.", "lord_pretalk",[
  ]],
  
   [anyone, "dplmc_lord_give_back_fief_confirm_ask",
   [
    (str_store_party_name, s11, "$diplomacy_var"),
   ], "So you think you can't fulfill your promise and manage {s11}?", "dplmc_lord_give_back_fief_confirm",
   []],

   [anyone|plyr, "dplmc_lord_give_back_fief_confirm",
   [
    (str_store_party_name, s11, "$diplomacy_var"),
   ], "Yes I want to give up on {s11}.", "lord_pretalk",
   [
    (call_script, "script_change_player_honor", -1),
    (call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -3),
    (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
    (val_sub, ":player_renown", 5),
    (val_max, ":player_renown", 0),
    (troop_set_slot, "trp_player", slot_troop_renown, ":player_renown"),
    (call_script, "script_give_center_to_faction", "$diplomacy_var", "fac_neutral"),
    (call_script, "script_give_center_to_faction", "$diplomacy_var", "$players_kingdom"),
   ]],
   
   [anyone|plyr, "dplmc_lord_give_back_fief_confirm",
   [
    (str_store_party_name, s11, "$diplomacy_var"),
   ], "No, I will keep the promise.", "lord_pretalk",
   []],

  ##persuade king to declare war
  [anyone|plyr,"lord_talk", [(le,"$talk_context", tc_party_encounter),
                             (ge, "$g_talk_troop_faction_relation", 0),
                             #(troop_slot_eq, "$g_talk_troop", slot_troop_is_prisoner, 0),
                             (neg|troop_slot_ge, "$g_talk_troop", slot_troop_prisoner_of_party, 0),
                             (faction_slot_eq, "$g_talk_troop_faction", slot_faction_leader, "$g_talk_troop"),
                             (eq, "$players_kingdom", "$g_talk_troop_faction"),
                             (eq, "$player_has_homage", 1),
                            ],
   "{s66}, you should declare war on another sovereignty.", "dplmc_lord_declare_war",[
  ]],

   [anyone, "dplmc_lord_declare_war",
   [
    (troop_get_slot, ":renown", "trp_player", slot_troop_renown), #reown
    (lt, ":renown", 150),
    (troop_get_slot, ":relation_to_king", "$g_talk_troop", slot_troop_player_relation),
    (lt, ":relation_to_king", 5),
    (val_sub, ":relation_to_king", 5),
    (assign, ":sum", ":renown"),
    (val_mul, ":relation_to_king", 5),
    (val_add, ":sum", ":relation_to_king"),
    (val_add, ":sum", "$player_honor"),
    
    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, ":sum"),
      (display_message, "@{!}DEBUG : sum: {reg0}"),
    (try_end), 
    
    (lt, ":sum", 300),
   ], "How can you dare? Who do you think you are? Get out of my sight!", "close_window",
   [
    (call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -1),
	(eq,"$talk_context",tc_party_encounter), #Added line by zerilius
	(assign, "$g_leave_encounter", 1), #Added line by zerilius
   ]],

   [anyone, "dplmc_lord_declare_war",
   [], "Against whom?", "dplmc_lord_declare_war_kingdoms_select",
   []],


  ##select war target
 [anyone|plyr|repeat_for_factions, "dplmc_lord_declare_war_kingdoms_select",
   [
    (store_repeat_object, ":faction_no"),
    (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
	##diplomacy start+
	(neq, ":faction_no", "fac_player_supporters_faction"),
	(neq, ":faction_no", "$g_talk_troop_faction"),
	##diplomacy end+
    (neq, ":faction_no", "$players_kingdom"),
    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "$players_kingdom", ":faction_no"),
    (ge, reg0, -1),
    (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
    (faction_get_slot, ":leader_no", ":faction_no", slot_faction_leader),
    (str_store_troop_name, s10, ":leader_no"),
    (str_store_faction_name, s11, ":faction_no"),
     ],
   "{s11}", "dplmc_lord_declare_war_ask_why",
   [
    (store_repeat_object, "$g_faction_selected"),
    (call_script, "script_npc_decision_checklist_peace_or_war", "$players_kingdom", "$g_faction_selected", "trp_player"),
    (assign, "$diplomacy_var", reg0),
    (val_mul, "$diplomacy_var", -6),
    (val_min, "$diplomacy_var", 2),
    
    (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
      (neq, ":kingdom", "$players_kingdom"),
      (neq, ":kingdom", "$g_faction_selected"),
      (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",  "$players_kingdom", ":kingdom"),
      (eq, reg0, -2),
      (val_sub, "$diplomacy_var", 4),
    (try_end),
    
    (store_skill_level, ":player_persuasion_skill", "skl_persuasion", "trp_player"),
    (val_add, "$diplomacy_var", ":player_persuasion_skill"),  
    
    (assign, reg50, 0),
    (assign, reg51, 0),
    (assign, reg52, 0),
    (assign, reg53, 0),    
    
    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, "$diplomacy_var"),
      (display_message, "@{!}DEBUG : diplomacy_var: {reg0}"),
    (try_end),    
   ]],
   
   [anyone|plyr, "dplmc_lord_declare_war_kingdoms_select",
   [], "Never mind.", "lord_pretalk",
   []],
     
   [anyone, "dplmc_lord_declare_war_ask_why",
	[
	(str_store_faction_name, s11, "$g_faction_selected"),
	##nested diplomacy start+ Fix capitalization
	], "Why should I declare war against the {s11}?", "dplmc_lord_declare_war_why",
	##nested diplomacy end+
   []],
   
   [anyone|plyr, "dplmc_lord_declare_war_why",
   [ 
    (eq, reg50, 0),
   ], "They are weaker and we can easily beat them.", "dplmc_lord_declare_war_anything_else",
   [
    (assign, reg50, 1),
    (assign, ":persuasion", -1),   
    (assign, ":player_kingdom_str", 0),
    (assign, ":target_kingdom_str", 0),
    
    (try_for_parties, ":party_no"), 
    	(assign, ":party_value", 0),
      (try_begin),
      	(is_between, ":party_no", towns_begin, towns_end),
      	(assign, ":party_value", 3),
      (else_try),	
      	(is_between, ":party_no", castles_begin, castles_end),
      	(assign, ":party_value", 2),
      (else_try),
      	(is_between, ":party_no", villages_begin, villages_end),
      	(assign, ":party_value", 1),
      (else_try),	
      	(party_get_template_id, ":template", ":party_no"),
      	(eq, ":template", "pt_kingdom_hero_party"),
      	(assign, ":party_value", 2),
      (try_end), 
    	
      (store_faction_of_party, ":party_current_faction", ":party_no"),
      (try_begin),
        (eq, ":party_current_faction", "$players_kingdom"),
        (val_add, ":player_kingdom_str", ":party_value"),
      (else_try),
        (eq, ":party_current_faction", "$g_faction_selected"),
        (val_add, ":target_kingdom_str", ":party_value"),
      (try_end),  
    (try_end),
    
    (try_begin),
      (gt, ":player_kingdom_str", ":target_kingdom_str"),
      (assign, ":persuasion", 1),
    (try_end),
    
    (store_skill_level, ":player_persuasion_skill", "skl_persuasion", "trp_player"),
    (val_mul, ":player_persuasion_skill", ":persuasion"),
    (val_add, ":persuasion", ":player_persuasion_skill"),
    (val_add, "$diplomacy_var", ":persuasion"),
      
    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, ":persuasion"),
      (display_message, "@{!}DEBUG : persuasion: {reg0}"),
      (assign, reg0, "$diplomacy_var"),
      (display_message, "@{!}DEBUG : diplomacy_var: {reg0}"),
    (try_end),
   ]],
   
   [anyone|plyr, "dplmc_lord_declare_war_why",
   [ 
    (eq, reg51, 0),
   ], "We can't tolerate their provocations any longer.", "dplmc_lord_declare_war_anything_else",
   [
    (assign, reg51, 1),
    (assign, ":persuasion", -1),
    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "$players_kingdom", "$g_faction_selected"),
    (assign, ":war_peace_truce_status", reg0),
    
    (try_begin),
    	(eq, ":war_peace_truce_status", -1), 
      (assign, ":persuasion", 1),
    (try_end),
    (store_skill_level, ":player_persuasion_skill", "skl_persuasion", "trp_player"),
    (val_mul, ":player_persuasion_skill", ":persuasion"),
    (val_add, ":persuasion", ":player_persuasion_skill"),
    (val_add, "$diplomacy_var", ":persuasion"),
    
    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, ":persuasion"),
      (display_message, "@{!}DEBUG : persuasion: {reg0}"),
      (assign, reg0, "$diplomacy_var"),
      (display_message, "@{!}DEBUG : diplomacy_var: {reg0}"),
    (try_end),
   ]],
   
   [anyone|plyr, "dplmc_lord_declare_war_why",
   [ 
    (eq, reg52, 0),
   ], "They are already in war and currently distracted.", "dplmc_lord_declare_war_anything_else",
   [  
    (assign, reg52, 1),
    (assign, ":persuasion", -1),
    (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
      (neq, ":kingdom", "$players_kingdom"),
      (neq, ":kingdom", "$g_faction_selected"),
      (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",  "$g_faction_selected", ":kingdom"),
      (eq, reg0, -2),
      (assign, ":persuasion", 1),
    (try_end),
    (store_skill_level, ":player_persuasion_skill", "skl_persuasion", "trp_player"),
    (val_mul, ":player_persuasion_skill", ":persuasion"),
    (val_add, ":persuasion", ":player_persuasion_skill"),
	  (val_add, "$diplomacy_var", ":persuasion"),  
	  
    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, ":persuasion"),
      (display_message, "@{!}DEBUG : persuasion: {reg0}"),
      (assign, reg0, "$diplomacy_var"),
      (display_message, "@{!}DEBUG : diplomacy_var: {reg0}"),
    (try_end),
   ]],
   
   [anyone|plyr, "dplmc_lord_declare_war_why",
   [ 
    (eq, reg53, 0),
   ], "It's the right time to attack.", "dplmc_lord_declare_war_anything_else",
   [
    (assign, reg53, 1),   
    (assign, ":persuasion", 1),
    (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
      (neq, ":kingdom", "$g_faction_selected"),
      (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",  "$players_kingdom", ":kingdom"),
      (eq, reg0, -2),
      (assign, ":persuasion", -1),
    (try_end),
    (store_skill_level, ":player_persuasion_skill", "skl_persuasion", "trp_player"),
    (val_mul, ":player_persuasion_skill", ":persuasion"),
    (val_add, ":persuasion", ":player_persuasion_skill"),
	  (val_add, "$diplomacy_var", ":persuasion"),  
	  
    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, ":persuasion"),
      (display_message, "@{!}DEBUG : persuasion: {reg0}"),
      (assign, reg0, "$diplomacy_var"),
      (display_message, "@{!}DEBUG : diplomacy_var: {reg0}"),
    (try_end),
   ]],

   [anyone|plyr, "dplmc_lord_declare_war_why",
   [ 
    (eq, reg54, 0),   
   ], "We should get back our lost land.", "dplmc_lord_declare_war_anything_else",
   [
    (assign, reg54, 1),   
    (assign, ":persuasion", -1),
    (try_for_parties, ":party_no"), 
  		(store_faction_of_party, ":party_current_faction", ":party_no"),
  		(party_get_slot, ":party_original_faction", ":party_no", slot_center_original_faction),
  		(party_get_slot, ":party_ex_faction", ":party_no", slot_center_ex_faction),
			(eq, ":party_current_faction", "$g_faction_selected"),
			(this_or_next|eq, ":party_original_faction", "$players_kingdom"),
		  (eq, ":party_ex_faction", "$players_kingdom"),
		  (assign, ":persuasion", 1),
    (try_end),  
    (store_skill_level, ":player_persuasion_skill", "skl_persuasion", "trp_player"),
    (val_mul, ":player_persuasion_skill", ":persuasion"),
    (val_add, ":persuasion", ":player_persuasion_skill"),
	  (val_add, "$diplomacy_var", ":persuasion"),  
	  
    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, ":persuasion"),
      (display_message, "@{!}DEBUG : persuasion: {reg0}"),
      (assign, reg0, "$diplomacy_var"),
      (display_message, "@{!}DEBUG : diplomacy_var: {reg0}"),
    (try_end),
]],
   
   [anyone|plyr, "dplmc_lord_declare_war_why",
   [ 
   ], "I mentioned all reasons for war. Please think about it!", "dplmc_lord_declare_war_decision",
   []],
   
   [anyone|plyr, "dplmc_lord_declare_war_why",
   [], "I need to think about that in peace and quiet.", "lord_pretalk",
   []],
   
   [anyone, "dplmc_lord_declare_war_anything_else",
   [ 
   ], "Well, anything else?", "dplmc_lord_declare_war_why",
   []],
   
   [anyone, "dplmc_lord_declare_war_decision",
	[
	(troop_get_slot, ":relation_to_king", "$g_talk_troop", slot_troop_player_relation),
	(val_sub, ":relation_to_king", 15),
	(val_min, ":relation_to_king", 35),
	(val_add, "$diplomacy_var", ":relation_to_king"),
	##nested diplomacy start+
	#If there is currently a treaty, apply a penalty to the persuasion attempt.
	(call_script, "script_dplmc_get_faction_truce_length_with_faction", "$players_kingdom", "$g_faction_selected"),
	(try_begin),
		(gt, reg0, 0),
		
		(try_begin),
		   (eq, "$cheat_mode", 1),
		   (assign, reg0, "$diplomacy_var"),
		   (display_message, "@{!}DEBUG : pre-treaty diplomacy_var: {reg0}"),
		(try_end),

			##TODO: Perhaps re-enable this later, but also balance it with the
			##lords who would be pleased by the declaration of war.
		#(try_for_range, ":troop_no", heroes_begin, heroes_end),
		#   (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
		#   (neq, ":troop_no", "$g_talk_troop"),
		#   (store_troop_faction, ":troop_faction"),
		#   (eq, ":troop_faction", "$g_talk_troop_faction"),
		#   #Would be angered by breaking the treaty
		#   (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
		#   (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
		#   (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
		#   (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_benefactor), #new for enfiefed commoners
		#   (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_custodian), #new for enfiefed commoners
		#      (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
		#   (val_sub, "$diplomacy_var", 1),
		#(try_end),
		(try_begin),
		(gt, reg0, dplmc_treaty_alliance_days_expire),
		  (val_div, "$diplomacy_var", 5),
		  (val_min, "$diplomacy_var", 15),
		(else_try),
		  (gt, reg0, dplmc_treaty_defense_days_expire),
		  (val_div, "$diplomacy_var", 4),
		  (val_min, "$diplomacy_var", 17),
		(else_try),
		  (gt, reg0, dplmc_treaty_trade_days_expire),
		  (val_div, "$diplomacy_var", 3),
		  (val_min, "$diplomacy_var", 19),
		(else_try),
		  (gt, reg0, dplmc_treaty_truce_days_expire),
		  (val_div, "$diplomacy_var", 2),
		  (val_min, "$diplomacy_var", 21),
		(try_end),
	(try_end),
	##diplomacy end+
	(store_random_in_range, ":random", 5, 25),

	(try_begin), #debug
	(eq, "$cheat_mode", 1),
	(assign, reg0, ":random"),
	(display_message, "@{!}DEBUG : random: {reg0}"),
	(assign, reg0, "$diplomacy_var"),
	(display_message, "@{!}DEBUG : final diplomacy_var: {reg0}"),
	(try_end),

	(gt, "$diplomacy_var", ":random"),

	##diplomacy start+
	#Replace "sword" with a culturally-appropriate alternative (TODO: does "gird" make sense for everythign?)
	(call_script, "script_dplmc_print_cultural_word_to_sreg", "$g_talk_troop", DPLMC_CULTURAL_TERM_WEAPON, 0),
	], "Gird your {s0} we are going to war against {s11}.", "close_window",
	##nested diplomacy end+
	[
	(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 1),
	(call_script, "script_diplomacy_start_war_between_kingdoms", "$players_kingdom", "$g_faction_selected", 1),
	(eq,"$talk_context",tc_party_encounter), #Added line by zerilius
	(assign, "$g_leave_encounter", 1), #Added line by zerilius
	]],
   
   [anyone, "dplmc_lord_declare_war_decision",
   [ 
   ], "No, I am not convinced. We won't attack {s11}.", "close_window",
   [
     (call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -1),
	(eq,"$talk_context",tc_party_encounter), #Added line by zerilius
	(assign, "$g_leave_encounter", 1), #Added line by zerilius
   ]],
   
   ##affiliate to family
  #leave
  [anyone|plyr,"lord_talk_ask_something_2", [
       (call_script, "script_dplmc_is_affiliated_family_member", "$g_talk_troop"),
       (eq, reg0, 1),],
   "I have done my share with your family, I want to be discharged of my pledge.", "dplmc_lord_family_affiliate_end",[
  ]], 

  [anyone,"dplmc_lord_family_affiliate_end", [],
   "What did you say?.", "script_dplmc_affiliate_confirm",[
  ]],
  
  [anyone|plyr,"script_dplmc_affiliate_confirm", [],
   "I do not want to be related to your house anymore.", "dplmc_lord_family_affiliate_leave",[
  ]],
  
  [anyone|plyr,"script_dplmc_affiliate_confirm", [],
   "Oh nothing.", "lord_pretalk",[
  ]],

  [anyone,"dplmc_lord_family_affiliate_leave", [],
   "You dare stand and face me to declaim your disavowal ! Well, your betrayal cannot make up for frankness. You disappoint the confidence my clan have put in you, {playername}. Each will condemn you in all conscience... but since I avouched your phoney allegiance, I will personally report to Calradia noblemen about your frivolous plot.", "close_window",[
    (call_script, "script_dplmc_affiliate_end", 0),
  ]],
  

  #join
  [anyone|plyr,"lord_talk_ask_something_2", [
   (store_current_hours, ":current_hours"),
   (val_sub, ":current_hours", 24 * 6),
   (ge, ":current_hours", "$g_last_affiliate_attempt"), 
   
	(ge, "$g_talk_troop_faction_relation", 0),
	(neg|troop_slot_ge, "$g_talk_troop", slot_troop_prisoner_of_party, 0),
	(eq, "$players_kingdom", "$g_talk_troop_faction"),
	(eq, "$player_has_homage", 1),
	##diplomacy start+
	#(eq, "$g_player_affiliated_troop", 0),
	(lt, "$g_player_affiliated_troop", 1),
	##diplomacy end+
	(troop_slot_eq, "$g_talk_troop", dplmc_slot_troop_affiliated, 0),
	(call_script, "script_troop_get_player_relation", "$g_talk_troop"),
	(gt, reg0, 0),
	(call_script, "script_troop_get_family_relation_to_troop", "trp_player", "$g_talk_troop"),
	(le, reg0, 0),
                            ],
   "I have great respect for your lineage, I wish to be affiliated to your family.", "dplmc_lord_family_affiliate",[
  ]],

  [anyone, "dplmc_lord_family_affiliate", 
   [
    (str_clear, s10),
    (assign, ":approved", 0),
    (troop_get_slot, ":lord_renown", "$g_talk_troop", slot_troop_renown),
    (try_begin),
      (troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_martial),
      (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
      (try_begin),
        (ge, ":player_renown", ":lord_renown"),
        (str_store_string, s10, "@You have shown great strength on the battlefield. But why should I enlist you within us?"),
        (assign, ":approved", 1),
      (try_end),
      
    (else_try),
##diplomacy start+ Add support for additional types
(this_or_next|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_ambitious),
##diplomacy end+
      (troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_cunning),
      (assign, ":has_center", 0), 
      (try_for_range, ":center_no", centers_begin, centers_end),
        (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
        (party_slot_eq, ":center_no", slot_party_type, spt_castle),        
        (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
        (assign, ":has_center", 1),
      (try_end),
      (try_begin),
        (eq, ":has_center", 1),
        (str_store_string, s10, "@All of life is about pros and cons. Why would we allow you to be our fellow?"),
        (assign, ":approved", 1),
      (try_end),
    (else_try),
      (troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_debauched),
      (try_begin),
        (le, "$player_honor", -10),
        (str_store_string, s10, "@I know, people do fear your harshness. Should we though?"),
        (assign, ":approved", 1),
      (try_end),
    (else_try),
##diplomacy start+ Add support for additional types
(this_or_next|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_moralist),
##diplomacy end+
      (troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_upstanding),
      (try_begin),
        (ge, "$player_honor", 10),
        (str_store_string, s10, "@Indeed, I have heard of your loyalty and valor. But is it enough to join us?"),
        (assign, ":approved", 1),
      (try_end),
    (else_try),
##diplomacy start+ Add support for additional types
(this_or_next|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_conventional),
##diplomacy end+
      (troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_goodnatured),      
      (try_begin),
        (ge, "$g_talk_troop_faction_relation", 60),
        (str_store_string, s10, "@I'm glad you want to support us. But, would it be wise for you, to affiliate to our family?"),
        (assign, ":approved", 1),
      (try_end),
    (else_try),
      (troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_selfrighteous),
      (try_begin),
        (store_troop_gold, ":wealth", "trp_household_possessions"),
        (store_troop_gold, ":cash", "trp_player"),
        (val_add, ":wealth", ":cash"),
        (val_sub, ":wealth", "$g_player_debt_to_party_members"),
        
        (val_mul, ":lord_renown", 65),
        (ge, ":wealth", ":lord_renown"),
        
        (str_store_string, s10, "@Beside your wealth, how could you possibly serve me and my family?"),
        (assign, ":approved", 1),
      (try_end),
    (else_try),
      (try_begin),
		  (call_script, "script_troop_get_player_relation", "$g_talk_troop"),
		  (gt, reg0, 18),
  ##diplomacy start+ Reworded
  #(str_store_string, s10, "@My friend, I see you reasoning. But would you really risk our friendship on partnership?"),
  (str_store_string, s10, "@My friend, I see your reasoning. But would you really risk straining our friendship by entering into a formal partnership?"),
  ##diplomacy end+
		  (assign, ":approved", 1),
		(try_end),
	(try_end),
	(eq, ":approved", 1),
	],
	"{!}{s10}", "dplmc_lord_family_affiliate_response",[
	]],
	
	##diplomacy start+ Give a less confusing error message when the lord likes the player
	[anyone, "dplmc_lord_family_affiliate",
	[(ge, "$g_talk_troop_relation", 0),
	(assign, reg0, 0),
	(try_begin),
	  (ge, "$g_talk_troop_relation", 18),
	  (assign, reg0, 1),
	(try_end),
	],
	"I {reg0?like you well enough:have nothing against you}, but I just don't think it would work out, so I will not sponsor you.", "lord_pretalk",[
	]],
	##diplomacy end+
 
  [anyone, "dplmc_lord_family_affiliate", 
   [
   ],
   "Not a chance. Since I dislike you, I will not sponsor you.", "lord_pretalk",[
 ]],

  [anyone|plyr, "dplmc_lord_family_affiliate_response", 
   [
   ],
   "Please Sire, let me serve your family.", "dplmc_lord_family_affiliate_persuasion",[
 ]],

  [anyone|plyr, "dplmc_lord_family_affiliate_response", 
   [
   ],
   "On second thought, I have to reconsider this decision.", "lord_pretalk",[
 ]],
 
  [anyone, "dplmc_lord_family_affiliate_persuasion", 
   [
    (troop_get_slot, ":lord_renown", "$g_talk_troop", slot_troop_renown),
    (store_skill_level, ":player_persuasion_skill", "skl_persuasion", "trp_player"),
    (val_add, ":player_persuasion_skill", 1),

    (call_script, "script_troop_get_player_relation", "$g_talk_troop"),
    (assign, ":relation", 0),
    (try_for_range, ":aristocrat", lords_begin, kingdom_ladies_end),
      (neq, ":aristocrat", "$g_talk_troop"),
      (call_script, "script_troop_get_family_relation_to_troop", ":aristocrat", "$g_talk_troop"),
      (gt, reg0, 0),
      (call_script, "script_troop_get_player_relation", "$g_talk_troop"),
      (val_add, ":relation", reg0),
    (try_end),
    
    (ge, ":relation", 0),
     
    (assign, ":approved", 0),
    (try_for_range, ":skill_level", 0, ":player_persuasion_skill"),
      (store_random_in_range, ":random_lord_renown", 0, ":lord_renown"),
      (store_random_in_range, ":random_lord_relation", 0, ":relation"),
      (val_add, ":random_lord_relation", ":skill_level"),
      
      (try_begin),
        (le, ":random_lord_renown", ":random_lord_relation"),
        (assign, ":approved", 1),
      (try_end),
    (try_end),
    
    (eq, ":approved", 1),

    (str_clear, s10),
    (try_begin),
      (troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_martial),
      (str_store_string, s10, "@Agreed! Your words convice me as much as your blade."),     
    (else_try),
      (troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_cunning),
      (str_store_string, s10, "@I trust you, my family could use your resourcefulness. Together we will spread our influence all over Calradia."),
    (else_try),
      (troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_debauched),
      (str_store_string, s10, "@May God have mercy on our enemy souls, because we won't!"),
    (else_try),
      (troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_upstanding),
      (str_store_string, s10, "@So be it. We are honored to accept you into our family."),
    (else_try),
      (troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_goodnatured),      
      (str_store_string, s10, "@ I will appreciate you as much as a son."),
    (else_try),
      (troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_selfrighteous),
      (str_store_string, s10, "@I accept your request. We will support you if you support my family."),
    (else_try),
      (str_store_string, s10, "@Since you have turned out to be a worthy fellow, you should be worthy for our entire family."),   
    (try_end),   
   ],
   "{!}{s10}", "dplmc_lord_family_affiliate_thank",[
   (assign, "$g_player_affiliated_troop", "$g_talk_troop"),
   (store_current_hours, ":cur_hours"),
   (assign, "$g_player_affiliated_time", ":cur_hours"),
   
   (try_for_range, ":family_member", lords_begin, kingdom_ladies_end),
    (call_script, "script_dplmc_is_affiliated_family_member", ":family_member"),
    (gt, reg0, 0),
    (troop_set_slot, ":family_member", dplmc_slot_troop_affiliated, 1),
   (try_end),
 ]],
 
  [anyone, "dplmc_lord_family_affiliate_persuasion", 
   [],
   "Maybe I have not good enough appraisal from my family about you. Or maybe I just need some time to get used to the idea. Let's talk further about it next week.", "lord_pretalk",
   [
     (store_current_hours, "$g_last_affiliate_attempt"),
  ]],
 
  [anyone|plyr, "dplmc_lord_family_affiliate_thank", 
   [],
   "I am honored and grateful to be affiliated with your family.", "dplmc_lord_family_affiliate_conclusion",[
 ]],
 
  [anyone, "dplmc_lord_family_affiliate_conclusion", 
   [],
   "You have pledged allegiance to our family, now all of my brethen are your brethren. Our fellowship is about knighthood : Never betray your family, always protect it.", "lord_pretalk",[

    (try_for_range, ":aristocrat", lords_begin, kingdom_ladies_end),
      (neq, ":aristocrat", "$g_talk_troop"),
      (call_script, "script_troop_get_family_relation_to_troop", ":aristocrat", "$g_talk_troop"),
      (gt, reg0, 0),
      (call_script, "script_change_player_relation_with_troop", ":aristocrat", 10),
    (try_end),    
    
    (try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
      (call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", ":kingdom_hero"),
      (lt, reg0, -10),
      (call_script, "script_change_player_relation_with_troop", ":kingdom_hero", -8),
	(try_end),
 ]],

		
  ##move court
  [anyone|plyr, "spouse_talk", 
   [
    (assign, ":has_fief", 0),
    (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
      (party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
      (eq, ":lord_troop_id", "trp_player"),
      (val_add, ":has_fief", 1),
    (try_end),
    (gt, ":has_fief", 1),
   ],
   "I want to move our residence.", "dplmc_spouse_move_residence_ask",[
 ]],
 

  [anyone, "dplmc_spouse_move_residence_ask", 
   [
   ],
   "To move our residence will require a small refurbishment. In particular, we need a set of tools and two piles of wool cloth in our househould.", "dplmc_spouse_move_residence_tools",[
 ]],
 
  [anyone|plyr, "dplmc_spouse_move_residence_tools", 
   [
    (troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),

	  (assign, ":amount", 0),
    (try_for_range, ":inventory_slot", 0, ":capacity"),
		  (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
		  (eq, ":item", "itm_trade_wool_cloth"),
      (val_add, ":amount", 1),
		(try_end),
	  (ge, ":amount", 2),
	  
	  (assign, ":amount", 0),
    (try_for_range, ":inventory_slot", 0, ":capacity"),
		  (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
		  (eq, ":item", "itm_trade_tools"),
      (val_add, ":amount", 1),
		(try_end),
	  (ge, ":amount", 1),
   ],
   "Ok, I think we have all necessary things to establish the residence.", "dplmc_spouse_move_residence_select_ask",[
 ]],
 
  [anyone|plyr, "dplmc_spouse_move_residence_tools", 
   [],
   "Well, I guess I have to get the set of tools and the piles of wool first.", "spouse_pretalk",[ #Diplomacy 3.2
 ]],
 
  [anyone, "dplmc_spouse_move_residence_select_ask", 
   [],
   "Where do you want to move the residence?", "dplmc_spouse_move_residence_select",[
 ]],
 
  [anyone|plyr|repeat_for_parties, "dplmc_spouse_move_residence_select", 
   [
    (store_repeat_object, ":center"),
    (is_between, ":center", walled_centers_begin, walled_centers_end),
    (troop_get_slot, ":cur_residence", "$g_talk_troop", slot_troop_cur_center),
    (neq, ":center", ":cur_residence"),
    (party_slot_eq, ":center", slot_town_lord, "trp_player"),
    (str_store_party_name, s6, ":center"),
   ],
   "{s6}.", "dplmc_spouse_move_residence_ask_confirm",[
    (store_repeat_object, "$diplomacy_var"),
 ]], 
 
  [anyone|plyr, "dplmc_spouse_move_residence_select", 
   [],
   "I changed my mind.", "spouse_pretalk",[
 ]],
 
  [anyone, "dplmc_spouse_move_residence_ask_confirm", 
   [
       (str_store_party_name, s6, "$diplomacy_var"),
   ],
   "Are you sure that you want to move your residence to {s6}?", "dplmc_spouse_move_residence_confirm",[
 ]], 
 
  [anyone|plyr, "dplmc_spouse_move_residence_confirm", 
	[],
	"Yes,  please arrange everything.", "dplmc_spouse_move_residence_moved",[
	(troop_remove_items, "trp_household_possessions", "itm_trade_wool_cloth", 2),
	(troop_remove_item, "trp_household_possessions", "itm_trade_tools"),
	##diplomacy start+
	#Fix bug: do not set spouse's current center if spouse is active or a party member
	(try_begin),
		(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
		(troop_slot_eq, ":player_spouse", slot_troop_occupation, slto_kingdom_lady),
	##diplomacy end+
		(troop_set_slot, "$g_talk_troop", slot_troop_cur_center, "$diplomacy_var"),
	##diplomacy start+
	(try_end),
	##diplomacy end+
	]],
 
  [anyone|plyr, "dplmc_spouse_move_residence_confirm", 
   [],
   "No.", "spouse_pretalk",[
 ]],
 
  [anyone, "dplmc_spouse_move_residence_moved", 
   [],
   "As you wish, I will move the residence to {s6}.", "spouse_pretalk",[
 ]],

  ##threaten with war
  [anyone|plyr, "minister_diplomatic_initiative_type_select",
   [
     (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "$players_kingdom", "$g_faction_selected"),
     (is_between, reg0, -1, 1), #no war, no truce
     (gt, "$g_player_chamberlain", 0),
   ],
   "Threaten them with war and see what you can squeeze out of them.", "minister_diplomatic_emissary",
   [(assign, "$g_initiative_selected", dplmc_npc_mission_threaten_request)]],   
   
 ##companion returning after threaten request
  [anyone, "event_triggered", [
      (store_conversation_troop, "$map_talk_troop"),
      (eq, "$map_talk_troop", "$npc_to_rejoin_party"), 
      (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, dplmc_npc_mission_threaten_request), 
      (troop_get_slot, ":string", "$map_talk_troop", slot_troop_honorific),
      (str_store_string, 21, ":string"),
		  (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
			(str_store_faction_name, s31, ":mission_object"),		
      (call_script, "script_npc_decision_checklist_peace_or_war", ":mission_object", "fac_player_supporters_faction", "$g_talk_troop"),
      (assign, "$g_mission_result", reg0),		 
  ],
   "Well, {s21}, at last I've found you. I have returned from my mission to {s31}.","dplmc_companion_threaten_request_response", 
   [
   (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
   (store_relation, ":player_relation", ":mission_object", "fac_player_supporters_faction"),
   (val_sub, ":player_relation", 3),
   (val_max, ":player_relation", 0),
   (set_relation, ":mission_object", "fac_player_supporters_faction", ":player_relation"),                   
   ]],
                    
  ##response to threaten request		
  [anyone, "dplmc_companion_threaten_request_response", [
    (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
    (gt, "$g_player_chamberlain", 0),
    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "$players_kingdom", ":mission_object"),
    (neq, reg0, -2), #no war                            
    (ge, "$g_mission_result", 2), #doesn't want war with us
    (store_random_in_range, ":random", 1000, 8000),
    
    (val_div, ":random", 100),
    (val_mul, ":random", 100),
    (assign, reg0, ":random"),
    (str_store_string, s21, "@{!}{reg0}"),
  ],					
   "They paid {s21} denars and are expecting that you leave them alone. I agreed on a truce of 40 days.","companion_rejoin_response", 
   [
     (call_script, "script_dplmc_pay_into_treasury", reg0),
     (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object), 
     (call_script, "script_diplomacy_start_peace_between_kingdoms", ":mission_object", "fac_player_supporters_faction", 1),
	  ]],
					
  ##response to threaten request		
  [anyone, "dplmc_companion_threaten_request_response", [
    (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "$players_kingdom", ":mission_object"),
    (neq, reg0, -2), #no war                                 
    (le, "$g_mission_result", 0), #they want war or are undecided
  ],					
   "They send you a declaration of war.","companion_rejoin_response", [
   (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),    
   (call_script, "script_diplomacy_start_war_between_kingdoms", ":mission_object", "fac_player_supporters_faction", 1),
	]],
	
  ##response to threaten request		
  [anyone, "dplmc_companion_threaten_request_response", [
  ],					
   "They are not willing to fold facing your threats.","companion_rejoin_response", [
					]],

  ##send a gift to another kingdom
  [anyone|plyr, "minister_diplomatic_initiative_type_select",
   [],
   "I want to send a gift.", "dplmc_minister_gift_type",
   [(assign, "$g_initiative_selected", npc_mission_peace_request)]],   

     
   [anyone, "dplmc_minister_gift_type",
   [
    (gt, "$g_player_chamberlain", 0),
    (assign, ":companion_found", 0),
    (try_for_range, ":emissary", companions_begin, companions_end),
      (main_party_has_troop, ":emissary"),
      (assign, ":companion_found", 1),
    (try_end),
    (eq, ":companion_found", 1),
   
   ],
   "We can send them some excellent horses from the best horse breeder in our sovereignty or we can hand over a fief.", "dplmc_minister_gift_type_select",
   []],
   
   [anyone, "dplmc_minister_gift_type",
   [
    (le, "$g_player_chamberlain", 0),
    (assign, ":companion_found", 0),
    (try_for_range, ":emissary", companions_begin, companions_end),
      (main_party_has_troop, ":emissary"),
      (assign, ":companion_found", 1),
    (try_end),
    (eq, ":companion_found", 1),
   ],
   "We currently only have the option to hand over a fief since we don't have a chamberlain.", "dplmc_minister_gift_type_select",
   []],
     
    ##send few horses
   [anyone|plyr, "dplmc_minister_gift_type_select",
   [
    (gt, "$g_player_chamberlain", 0),
    (store_troop_gold, ":gold", "trp_household_possessions"),
    (try_begin),
      (lt, ":gold", 3000),
      (store_troop_gold, ":gold", "trp_player"),
    (try_end),
    (ge, ":gold", 3000),
   ],
   "Send horses for 3000 denars.", "minister_diplomatic_emissary",
   [     
     (assign, "$g_initiative_selected", dplmc_npc_mission_gift_horses_request),
     (assign, "$diplomacy_var", 3000), # 6000 denars
   ]],
   
    ##send many horses
   [anyone|plyr, "dplmc_minister_gift_type_select",
   [
    (gt, "$g_player_chamberlain", 0),
    (store_troop_gold, ":gold", "trp_household_possessions"),
    (try_begin),
      (lt, ":gold", 6000),
      (store_troop_gold, ":gold", "trp_player"),
    (try_end),    
    (ge, ":gold", 6000),
   ],
   "Send horses for 6000 denars.", "minister_diplomatic_emissary",
   [
     (assign, "$g_initiative_selected", dplmc_npc_mission_gift_horses_request),
     (assign, "$diplomacy_var", 6000), # 6000 denars
   ]],
   
    ##hand over a fief
   [anyone|plyr, "dplmc_minister_gift_type_select",
   [
   ],
   "Hand over a fief", "dplmc_minister_gift_fief",
   []],
    
    ##never mind
   [anyone|plyr, "dplmc_minister_gift_type_select",
   [
   ],
   "Never mind.", "minister_pretalk",
   []],

    ##ask which fief to hand over
   [anyone, "dplmc_minister_gift_fief",
   [
   ],
   "Which fief do you want to hand over?", "dplmc_minister_gift_fief_select",
   []],
   
    ##select the fief to hand over
   [anyone|plyr|repeat_for_parties, "dplmc_minister_gift_fief_select",
   [
	(store_repeat_object, ":center_no"),
	(is_between, ":center_no", centers_begin, centers_end),
	(neq, ":center_no", "$g_player_court"),
	(store_faction_of_party, ":center_faction", ":center_no"),
	##diplomacy start+ Handle player is co-ruler of faction
	##OLD:
	#(eq, ":center_faction", "fac_player_supporters_faction"),
	##NEW:
	(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":center_faction"),
	(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
	##diplomacy end+
	(str_store_party_name, s1, ":center_no"),
   
   ],"{s1}", "minister_diplomatic_emissary",
   [
    (store_repeat_object, "$diplomacy_var"),
    (assign, "$g_initiative_selected", dplmc_npc_mission_gift_fief_request),
   ]],   
   
  ##dispatch emissary to bring gift
  [anyone, "minister_emissary_dispatch",
   [
    (str_store_troop_name, s11, "$g_emissary_selected"),
    (str_store_faction_name, s12, "$g_faction_selected"),
    (this_or_next|eq, "$g_initiative_selected", dplmc_npc_mission_gift_fief_request),
    (eq, "$g_initiative_selected", dplmc_npc_mission_gift_horses_request),
    (str_store_string, s14, "str_dplmc_bring_gift"),
   ], "Very well -- I shall send {s11} to the {s12} to {s14}.", "minister_diplomatic_dispatch_confirm",[
   ]],
   
 ##companion returning after gift request
  [anyone, "event_triggered", [
    (store_conversation_troop, "$map_talk_troop"),
    (eq, "$map_talk_troop", "$npc_to_rejoin_party"), 
    (troop_get_slot, ":mission", "$g_talk_troop", slot_troop_current_mission), 
    (this_or_next|eq, ":mission", dplmc_npc_mission_gift_fief_request),
    (eq, ":mission", dplmc_npc_mission_gift_horses_request),
    (troop_get_slot, ":string", "$map_talk_troop", slot_troop_honorific),
    (str_store_string, 21, ":string"),
    (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
    (str_store_faction_name, s31, ":mission_object"),				 				 
   ],
   "Well, {s21}, at last I've found you. I have returned from my mission to {s31}. They were agreeably surprised.","companion_rejoin_response", [
    (troop_get_slot, ":dipomacy_var", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy),
    (troop_get_slot, ":mission", "$g_talk_troop", slot_troop_current_mission), 
    (try_begin),
      (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object), 
      (eq, ":mission", dplmc_npc_mission_gift_fief_request),
      (call_script, "script_give_center_to_faction", ":dipomacy_var", ":mission_object"),
      (assign, ":concession_value", 1),
      (try_begin),
       (is_between, ":dipomacy_var", towns_begin, towns_end),
       (assign, ":concession_value", 6),
      (else_try),	
        (is_between, ":dipomacy_var", castles_begin, castles_end),
        (assign, ":concession_value", 4),
      (else_try),
        (is_between, ":dipomacy_var", villages_begin, villages_end),
        (assign, ":concession_value", 2),
      (try_end), 
      (call_script, "script_change_troop_renown", "trp_player", ":concession_value"),   
      (val_mul, ":concession_value", 2),   
      (call_script, "script_change_player_relation_with_faction", ":mission_object", ":concession_value"),
    (else_try),
      (eq, ":mission", dplmc_npc_mission_gift_horses_request), 
      (try_begin),
        (le, ":dipomacy_var", 3000),
        (call_script, "script_change_player_relation_with_faction", ":mission_object", 2),
        (call_script, "script_change_troop_renown", "trp_player", 1),
      (else_try),
        (gt, ":dipomacy_var", 3000),
        (call_script, "script_change_player_relation_with_faction", ":mission_object", 4),
        (call_script, "script_change_troop_renown", "trp_player", 2),
      (try_end),   
    (try_end), 
   ]],    

   ##prisoner exchange mission
   [anyone|plyr, "minister_talk",
   [
     (is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),     
   ],
   "I wish to exchange a prisoner.", "dplmc_minister_exchange_prisoner_ask",
   []],
   
   ## ask for prisoner
   [anyone, "dplmc_minister_exchange_prisoner_ask",
   [
    (assign, ":companion_found", 0),
    (try_for_range, ":emissary", companions_begin, companions_end),
      (main_party_has_troop, ":emissary"),
      (assign, ":companion_found", 1),
    (try_end),
    (eq, ":companion_found", 1),
   
   ],
   "Which prisoner do you want to exchange?", "dplmc_minister_exchange_prisoner_select",
   []],
   
   [anyone, "dplmc_minister_exchange_prisoner_ask",
   [
   ],
   "Unfortunately, there is no one to send right now.", "minister_pretalk",
   []],
   
  ##select enemy prisoner
 [anyone|plyr|repeat_for_troops, "dplmc_minister_exchange_prisoner_select",
   [
     (store_repeat_object, ":troop_no"),
     (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
     (troop_get_slot, ":party", ":troop_no", slot_troop_prisoner_of_party),
     (is_between, ":party", walled_centers_begin, walled_centers_end),
     (party_slot_eq, ":party", slot_town_lord, "trp_player"),
     (str_store_troop_name, s10, ":troop_no"),
     (store_faction_of_troop, ":faction_no", ":troop_no"),
     (str_store_faction_name, s11, ":faction_no"),
     ],
   "{s10} of {s11}", "dplmc_minister_exchange_prisoner_lord_ask",
   [
     (store_repeat_object, "$diplomacy_var"),
     (store_faction_of_troop, "$g_faction_selected", "$diplomacy_var"),
     (assign, "$g_initiative_selected", dplmc_npc_mission_prisoner_exchange)
     ]],
     
 [anyone|plyr, "dplmc_minister_exchange_prisoner_select",
   [],
   "Nobody.", "minister_pretalk",
   []],
   
   [anyone, "dplmc_minister_exchange_prisoner_lord_ask",
   [
   ],
   "Which of our lords do you like to you want to set free?", "dplmc_minister_exchange_prisoner_lord_select",
   []],
   
  ##select own prisoner
 [anyone|plyr|repeat_for_troops, "dplmc_minister_exchange_prisoner_lord_select",
   [
	(store_repeat_object, ":troop_no"),
	(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
	(store_faction_of_troop, ":troop_faction", ":troop_no"),
	##diplomacy start+ Handle player is co-ruler of kingdom
	##OLD:
	#(eq, ":troop_faction", "fac_player_supporters_faction"),
	##NEW:
	(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":troop_faction"),
	(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
	##diplomacy end+
	(troop_get_slot, ":party", ":troop_no", slot_troop_prisoner_of_party),
	(is_between, ":party", walled_centers_begin, walled_centers_end),
	(store_faction_of_party, ":party_faction", ":party"),
	(eq, ":party_faction", "$g_faction_selected"),
	(str_store_troop_name, s10, ":troop_no"),
	],
   "{s10}.", "dplmc_minister_prisoner_emissary",
   [
     (store_repeat_object, "$diplomacy_var2"),
     ]],
     
 [anyone|plyr, "dplmc_minister_exchange_prisoner_lord_select",
   [],
   "Nobody.", "minister_pretalk",
   []],   
     
   [anyone, "dplmc_minister_prisoner_emissary",
   [], "Who shall negotiate the exchange?", "minister_emissary_select",
   []],
   
  ##exchange prisoner
  [anyone, "minister_emissary_dispatch",
   [
    (str_store_troop_name, s11, "$g_emissary_selected"),
    (str_store_faction_name, s12, "$g_faction_selected"),
    (eq, "$g_initiative_selected", dplmc_npc_mission_prisoner_exchange),
    (str_store_troop_name, s10, "$diplomacy_var"),
    (str_store_troop_name, s11, "$diplomacy_var2"),
    (str_store_string, s14, "str_dplmc_exchange_prisoner"),
   ], "Very well -- I shall send {s11} to the {s12} to {s14}.", "minister_diplomatic_dispatch_confirm",[]],
   
 ##companion returning after exchange request
  [anyone, "event_triggered", [
      (store_conversation_troop, "$map_talk_troop"),
      (eq, "$map_talk_troop", "$npc_to_rejoin_party"), 
      
      (troop_get_slot, ":mission", "$g_talk_troop", slot_troop_current_mission), 
		  (eq, ":mission", dplmc_npc_mission_prisoner_exchange),
		  
      (troop_get_slot, ":enemy_prisoner", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy), 
      (troop_get_slot, ":own_prisoner", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy2), 
      
      (troop_get_slot, ":own_prison", ":enemy_prisoner", slot_troop_prisoner_of_party),
      (troop_get_slot, ":enemy_prison", ":own_prisoner", slot_troop_prisoner_of_party),
      (is_between, ":own_prison", walled_centers_begin, walled_centers_end),
      (is_between, ":enemy_prison", walled_centers_begin, walkers_end),
      

      (call_script, "script_calculate_ransom_amount_for_troop", ":enemy_prisoner"),
      (assign, ":enemy_value", reg0),
      (call_script, "script_calculate_ransom_amount_for_troop", ":own_prisoner"),
      (assign, ":own_value", reg0),
      (ge, ":enemy_value", ":own_value"),
      
      (troop_get_slot, ":string", "$map_talk_troop", slot_troop_honorific),
      (str_store_string, 21, ":string"),
      (str_store_troop_name, s32, ":enemy_prisoner"),
      (str_store_troop_name, s33, ":own_prisoner"),			 				 
##diplomacy start+ Make pronouns correct
(call_script, "script_dplmc_store_troop_is_female", ":enemy_prisoner"),
(assign, reg4, reg0),
               ],#Next line, "exchange {s32} against {s33}"  -> "exchange {s32} for {s33}" 
"Well, {s21}, at last I've found you.They agreed to exchange {s32} for {s33}. {s33} has accompanied me back here. Do you want to set {s32} free?","dplmc_companion_prisoner_exchange_confirm", [
              ]],
##diplomacy end+
   [anyone|plyr, "dplmc_companion_prisoner_exchange_confirm",
   [],
"Yes set {reg4?her:him} free.", "companion_rejoin_response",
   [  (troop_get_slot, ":enemy_prisoner", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy), 
      (troop_get_slot, ":own_prisoner", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy2),
      (call_script, "script_remove_troop_from_prison", ":enemy_prisoner"),
      (call_script, "script_remove_troop_from_prison", ":own_prisoner"), 
      (str_store_troop_name, s7, ":enemy_prisoner"),
      (display_message, "str_dplmc_has_been_set_free"),
      (str_store_troop_name, s7, ":own_prisoner"),
      (display_message, "str_dplmc_has_been_set_free"),
      (call_script, "script_change_player_relation_with_troop", ":own_prisoner", 3),
      (call_script, "script_change_player_relation_with_troop", ":enemy_prisoner", 1),
      (call_script, "script_change_player_honor", 1),
      (call_script, "script_update_troop_notes", ":enemy_prisoner"),
      (call_script, "script_update_troop_notes", ":own_prisoner"), 
   ]],
   
   [anyone|plyr, "dplmc_companion_prisoner_exchange_confirm",
   [],
"No don't set {reg4?her:him} free.", "companion_rejoin_response",
   [
      (troop_get_slot, ":enemy_prisoner", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy), 
      (troop_get_slot, ":own_prisoner", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy2), 
      (troop_set_slot, ":own_prisoner", slot_troop_prisoner_of_party, -1),
      (str_store_troop_name, s7, ":own_prisoner"),
      (display_message, "str_dplmc_has_been_set_free"),
      (call_script, "script_change_player_relation_with_troop", ":own_prisoner", 1),
      (store_faction_of_troop, ":enemy_faction", ":enemy_prisoner"),
      (call_script, "script_change_player_relation_with_faction", ":enemy_faction", -6),
      (call_script, "script_change_player_honor", -2),
      (call_script, "script_update_troop_notes", ":own_prisoner"), 
   ]],
      
  [anyone, "event_triggered", [
      (store_conversation_troop, "$map_talk_troop"),
      (eq, "$map_talk_troop", "$npc_to_rejoin_party"),
      
      (troop_get_slot, ":mission", "$g_talk_troop", slot_troop_current_mission), 
		  (eq, ":mission", dplmc_npc_mission_prisoner_exchange),
		   
      (troop_get_slot, ":enemy_prisoner", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy), 
      (troop_get_slot, ":own_prisoner", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy2), 

      (troop_get_slot, ":string", "$map_talk_troop", slot_troop_honorific),
      (str_store_string, 21, ":string"),
      (str_store_troop_name, s32, ":enemy_prisoner"),
      (str_store_troop_name, s33, ":own_prisoner"),					 				 
               ],##diplomacy start+ Change "exchange against" to "exchange for"
"Well, {s21}, at last I've found you. They didn't agree to exchange {s32} for {s33}.","companion_rejoin_response", [
              ]],
			  ##diplomacy end+

##persuasion mission
   [anyone|plyr, "minister_talk",
   [
	(is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),
	(faction_get_slot, ":faction_leader", "fac_player_supporters_faction", slot_faction_leader),
	##diplomacy start+ Handle player is co-ruler of kingdom
	(assign, ":is_coruler", 0),
	(try_begin),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":is_coruler", 1),
	(try_end),
	(this_or_next|eq, ":is_coruler", 1),
	##diplomacy end+
	(eq, ":faction_leader", "trp_player"),
	],
   "I want to persuade a lord of joining our sovereignty.", "dplmc_minister_persuasion_fief_ask",
   []],
   
   [anyone, "dplmc_minister_persuasion_fief_ask",
   [
    (assign, ":companion_found", 0),
    (try_for_range, ":emissary", companions_begin, companions_end),
      (main_party_has_troop, ":emissary"),
      (assign, ":companion_found", 1),
    (try_end),
    (eq, ":companion_found", 1),
   
   ],
   "Your emissary can't go with empty hands we have to offer a fief. Which one do you want to offer?", "dplmc_minister_persuasion_fief",
   []],
   
   [anyone, "dplmc_minister_persuasion_fief_ask",
   [
   ],
   "Unfortunately, there is no one to send right now.", "minister_pretalk",
   []],

     
  [anyone|plyr|repeat_for_parties,"dplmc_minister_persuasion_fief", [
		(store_repeat_object, ":center"),
        (is_between, ":center", centers_begin, centers_end),
		(neq, ":center", "$g_player_court"),
		(store_faction_of_party, ":center_faction", ":center"),
		##diplomacy start+ Handle player is co-ruler of kingdom
		(assign, ":alt_faction", "fac_player_supporters_faction"),
		(try_begin),
			(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
			(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
			(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
			(assign, ":alt_faction", "$players_kingdom"),
		(try_end),
		(this_or_next|eq, ":alt_faction", ":center_faction"),
		##diplomacy end+
		(eq, ":center_faction", "fac_player_supporters_faction"),
		(neg|party_slot_ge, ":center", slot_town_lord, active_npcs_begin), #ie, owned by player or unassigned
		(str_store_party_name, s11, ":center"),
		
        ], "{s11}", "dplmc_minister_persuade_lord_faction_ask",[
		(store_repeat_object, "$diplomacy_var2"),
		]],
		 
  [anyone|plyr, "dplmc_minister_persuasion_fief", [
        ], "Never mind -- there is no fief I can offer.", "minister_pretalk",[
		]],
		
   [anyone, "dplmc_minister_persuade_lord_faction_ask",
   [ ],
   "Where does the lord live you want to persuade?", "dplmc_minister_persuade_lord_faction",
   []],
   
 [anyone|plyr|repeat_for_factions, "dplmc_minister_persuade_lord_faction",
   [
     (store_repeat_object, ":faction_no"),
	   (is_between, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
     (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
     (str_store_faction_name, s11, ":faction_no"),
     ],
   "{s11}", "dplmc_minister_persuade_lord_ask",
   [
     (store_repeat_object, "$g_faction_selected"),
     ]],
     
  [anyone|plyr, "dplmc_minister_persuade_lord_faction", [
        ], "Nowhere.", "minister_pretalk",[
		]],
     
   [anyone, "dplmc_minister_persuade_lord_ask",
   [
   ],
   "Who shall be convinced?", "dplmc_minister_persuade_lord",
   []],

 [anyone|plyr|repeat_for_troops, "dplmc_minister_persuade_lord",
   [
     (store_repeat_object, ":troop_no"),
     (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
	   (store_faction_of_troop, ":faction", ":troop_no"),
	   (is_between, ":faction", npc_kingdoms_begin, npc_kingdoms_end),
	   (faction_get_slot, ":faction_leader", ":faction", slot_faction_leader),
	   (neq, ":faction_leader", ":troop_no"),
	   
	   (eq, ":faction", "$g_faction_selected"),
	  (troop_slot_eq, ":troop_no", slot_troop_met, 1),
      #target still wants to talk
	   (neg|troop_slot_ge, ":troop_no", slot_troop_intrigue_impatience, 100),	   
     (str_store_troop_name, s11, ":troop_no"),
     ],
   "{s11}", "dplmc_minister_persuasion_emissary",
   [
     (store_repeat_object, "$diplomacy_var"),
     (assign, "$g_initiative_selected", dplmc_npc_mission_persuasion),
     ]],
     
  [anyone|plyr, "dplmc_minister_persuade_lord", [
        ], "I can't think of anyone.", "minister_pretalk",[
		]],
     
     
   [anyone, "dplmc_minister_persuasion_emissary",
   [], "Who shall I send? You should choose one who has skills in persuasion!", "minister_emissary_select",
   []],

  ##dispatch emissary to persuade
  [anyone, "minister_emissary_dispatch",
   [
    (str_store_troop_name, s11, "$g_emissary_selected"),
    (str_store_faction_name, s12, "$g_faction_selected"),
    (eq, "$g_initiative_selected", dplmc_npc_mission_persuasion),
    (str_store_troop_name, s13, "$diplomacy_var"),
    (str_store_party_name, s14, "$diplomacy_var2"),
##diplomacy start+ Use correct pronoun
(call_script, "script_dplmc_store_troop_is_female", "$diplomacy_var"),
(assign, reg4, reg0),#Next line, "him" -> {reg4?her:him}
], "Very well -- I shall send {s11} to {s12} to persuade {s13} and offer {reg4?her:him} {s14}.", "minister_diplomatic_dispatch_confirm",[
##diplomacy end+
]],
   
 ##companion returning after persuasion request
  [anyone, "event_triggered", [
      (store_conversation_troop, "$map_talk_troop"),
      (eq, "$map_talk_troop", "$npc_to_rejoin_party"), 
      (troop_get_slot, ":mission", "$g_talk_troop", slot_troop_current_mission), 
	  (eq, ":mission", dplmc_npc_mission_persuasion),    
      (troop_get_slot, ":string", "$map_talk_troop", slot_troop_honorific),
      (str_store_string, 21, ":string"),
	  (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
	  (str_store_faction_name, s30, ":mission_object"), #Diplomacy 3.2
	  (troop_get_slot, ":target_troop", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy),
      (str_store_troop_name, s14, ":target_troop"),	#Diplomacy 3.2
	  (troop_set_slot, "$g_talk_troop", slot_troop_intrigue_impatience, 500),

      (assign, ":no_join", 0), #Diplomacy 3.2
      (str_clear, s40), #Diplomacy 3.2
      
        #player is still king
      (faction_get_slot, ":faction_leader", "fac_player_supporters_faction", slot_faction_leader),
#Diplomacy 3.2 begin
      (try_begin),
        (neq, ":faction_leader", "trp_player"),
        (str_store_string, s40, "@Your leader is not even a king and I shall join you?"),  	        
        (assign, ":no_join", 1),
      (try_end),
#Diplomacy 3.2 end
      #player has fief
    	(assign, ":one_fortress_found", 0),
    	(try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
    		(this_or_next|party_slot_eq, ":walled_center", slot_town_lord, "$g_talk_troop"),
    		(party_slot_eq, ":walled_center", slot_town_lord, "trp_player"),
    		(assign, ":one_fortress_found", 1),
    	(try_end),
#Diplomacy 3.2 begin  	
    	(try_begin),
			(eq, ":one_fortress_found", 0),
			(str_store_string, s40, "@{s40} I would never join someone who doesn't own a town or castle."),  	
			(assign, ":no_join", 1),
		(try_end),

      (assign, ":enough_renown", 1),
#Diplomacy 3.2 end
      (try_begin),
        (troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_martial),
        (this_or_next|lt, "$player_right_to_rule", 10),##Diplomacy 3.2
        (neg|troop_slot_ge, "trp_player", slot_troop_renown, 400),
        (assign, ":enough_renown", 0),##
      (else_try),      
        (troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_upstanding),
        (this_or_next|lt, "$player_right_to_rule", 20),##Diplomacy 3.2
        (neg|troop_slot_ge, "trp_player", slot_troop_renown, 200),
        (assign, ":enough_renown", 0),##
      (else_try),           
        (troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_selfrighteous),
        (this_or_next|lt, "$player_right_to_rule", 10),##Diplomacy 3.2
        (neg|troop_slot_ge, "trp_player", slot_troop_renown, 200),
        (assign, ":enough_renown", 0),##
      (else_try),      
        (troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_cunning),
        (neg|troop_slot_ge, "trp_player", slot_troop_renown, 400),##Diplomacy 3.2
		(assign, ":enough_renown", 0),##
      (else_try),     
#Diplomacy 3.2 begin
        (neg|troop_slot_ge, "trp_player", slot_troop_renown, 200),
        (assign, ":enough_renown", 0),
      (try_end),
      
		(try_begin),
		  (eq, ":enough_renown", 0),
		  ##diplomacy start+ "to" to "too"
		  (str_store_string, s40, "@{s40} I know too little about your leader."),
		  ##diplomacy end+
		  (assign, ":no_join", 1),
		(try_end),

        #init random seed
        (troop_get_slot, ":temp_ai_seed", ":target_troop", slot_troop_temp_decision_seed),
		(store_div, ":persuasion_random", ":temp_ai_seed", 100),  #I used div instead of mod to have a different random value, value generated from (mod 100) will be used in next steps. These two values should be non-related.
		##diplomacy start+
		(troop_get_slot, ":target_reputation", ":target_troop", slot_lord_reputation_type),
		(try_begin),
			(store_mod, reg0, ":target_troop", 2),
			(eq, reg0, 0),
			(val_add, ":persuasion_random", 50),#because we take mod 100, the average effect of this is zero, but it addresses problems such as "all high" or "all low"
		(try_end),
		(val_mod, ":persuasion_random", 100),#should take mod 100 after division
		##diplomacy end+
		(val_add, ":persuasion_random", 1),
		(store_skill_level, ":persuasion_skill", "skl_persuasion", "$g_talk_troop"),
		(val_mul, ":persuasion_skill", 7),
		##diplomacy start+
		#Add a base success chance, so that skill 5 has a 50% chance of failure instead of a 65% chance of failure.
		(val_add, ":persuasion_skill", 15),
		##diplomacy end+
		(try_begin),
		  (lt, ":persuasion_skill", ":persuasion_random"),
		##diplomacy start+
		##OLD:
		#  (str_store_string, s40, "@{s40} Next time I prefer to talk to someone who doesn't act like a fool."),
		#  (assign, ":no_join", 1),
		##NEW:
		  (try_begin),
			 (ge, "$cheat_mode", 1),
			 (assign, reg0, ":persuasion_random"),
			 (assign, reg1, ":persuasion_skill"),
			 (display_message, "@{!} Emissary persuasion attempt: skill factor {reg1} versus random number {reg0}"),
		  (try_end),
		  (store_mul, reg0, ":persuasion_skill", 2),
		  (try_begin),
			 (this_or_next|ge, reg0, ":persuasion_random"),
			 (eq, ":target_reputation", lrep_goodnatured),
			 (neq, ":target_reputation", lrep_debauched),
			 (neq, ":target_reputation", lrep_quarrelsome),
			 (str_store_string, s40, "@{s40} I found your messenger unconvincing."),
		  (else_try),
			 (this_or_next|eq, ":target_reputation", lrep_debauched),
			 (this_or_next|eq, ":target_reputation", lrep_quarrelsome),
			 (this_or_next|eq, ":target_reputation", lrep_selfrighteous),
			 (this_or_next|eq, ":target_reputation", lrep_ambitious),
			 (is_between, ":target_reputation", lrep_roguish, lrep_conventional),
			 (str_store_string, s40, "@{s40} Next time I would prefer to talk to someone who doesn't act like a fool."),
		  (else_try),
			 (str_store_string, s40, "@{s40} Next time I would prefer to talk to someone more versed in courtly manners."),
		  (try_end),
		  (assign, ":no_join", 1),
		(try_end),
		##diplomacy end+

		(call_script, "script_calculate_troop_political_factors_for_liege", ":target_troop", "trp_player"),
		(assign, ":result_for_security", reg2),		
		(assign, ":result_for_political", reg4),		
		(assign, ":change_penalty", reg10),		
		(assign, ":result_for_new_liege", reg0),		
		(store_faction_of_troop, ":target_faction", ":target_troop"),
		(faction_get_slot, ":cur_liege", ":target_faction", slot_faction_leader),
		(call_script, "script_calculate_troop_political_factors_for_liege", ":target_troop", ":cur_liege"),

		(store_sub, ":result_for_security_comparative", ":result_for_security", reg2),
		(store_sub, ":result_for_political_comparative", ":result_for_political", reg4),		
		(assign, ":result_for_old_liege", reg0),
		(store_sub, "$pledge_chance", ":result_for_new_liege", ":result_for_old_liege"),
		(val_add, "$pledge_chance", 50),
		(val_div, "$pledge_chance", 2),	
#Diplomacy 3.2 begin
      (store_mod, ":random", ":temp_ai_seed", 100), 
      
      (try_begin), 
        (eq, "$cheat_mode", 1),
        (assign, reg2, ":result_for_security"),
        (display_message, "@{!}DEBUG - result_for_security: {reg2} > 10"),
        (assign, reg2, ":result_for_political"),
        (display_message, "@{!}DEBUG - result_for_political: {reg2} > 0"),
        (assign, reg2, ":change_penalty"),
        (display_message, "@{!}DEBUG - change_penalty: {reg2} < 20"),
        (assign, reg2, ":random"),
        (display_message, "@{!}DEBUG - random: {reg2}"),
        (assign, reg2, "$pledge_chance"),                
        (display_message, "@{!}DEBUG - > pledge_chance: {reg2}"), 
        (assign, reg2, ":result_for_security_comparative"),
        (display_message, "@{!}DEBUG - result_for_security_comparative: {reg2} > 0"),
        (assign, reg2, ":result_for_political_comparative"),                
        (display_message, "@{!}DEBUG - result_for_political_comparative: {reg2} > 0"),               
      (try_end),
    
      (try_begin),            
        (le, ":random", "$pledge_chance"),
        (assign, ":no_join", 1),
        (str_store_string, s40, "@{s40} I rather stay with my current king."),  
      (try_end),  

      (try_begin),
        (eq, ":no_join", 0),
  		(try_begin),
  			(lt, ":result_for_political", 0),
			(assign, ":no_join", 1),        
  
			(try_begin),
				(troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_upstanding),
				(str_store_string, s31, "str_i_worry_about_those_with_whom_you_have_chosen_to_surround_yourself" ),
			(else_try),
				 (troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_martial),
				 (str_store_string, s31, "str_there_are_some_outstanding_matters_between_me_and_some_of_your_vassals_"),
				 (try_begin),
				   (assign, reg41, ":result_for_political"),
				   ##diplomacy start+ Only show debug messages with cheat mode on
				   (ge, "$cheat_mode", 1),
				   ##diplomacy end+
				   (display_message, "str_result_for_political_=_reg41"),
				 (try_end), 					  
			(else_try),
				(troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_quarrelsome),
				(str_store_string, s31, "str_my_liege_has_his_faults_but_i_dont_care_for_your_toadies"),
			(else_try),
				(troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_goodnatured),
				(str_store_string, s31, "str_i_think_youre_a_good_man_but_im_worried_that_you_might_be_pushed_in_the_wrong_direction_by_some_of_those_around_you"),
			(else_try),
				(troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_selfrighteous),
				(str_store_string, s31, "str_i_am_loathe_to_fight_alongside_you_so_long_as_you_take_under_your_wing_varlots_and_base_men"),
			(else_try),
				(troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_cunning),
				(str_store_string, s31, "str_ill_be_honest__with_some_of_those_who_follow_you_i_think_id_be_more_comfortable_fighting_against_you_than_with_you"),
			(else_try),
				(troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_debauched),
				(str_store_string, s31, "str_i_say_that_you_can_judge_a_man_by_the_company_he_keeps_and_you_have_surrounded_yourself_with_vipers_and_vultures"),
			(else_try),
				(troop_slot_ge, ":target_troop", slot_lord_reputation_type, lrep_roguish),
				(str_store_string, s31, "str_you_know_that_i_have_always_had_a_problem_with_some_of_our_companions"),										
			(try_end),				
		(else_try),
			(lt, ":result_for_political_comparative", 0),
			(assign, ":no_join", 1),
			(str_store_string, s31, "str_politically_i_would_be_a_better_position_in_the_court_of_my_current_liege_than_in_yours"),
		(else_try),
			(str_store_string, s31, "str_i_am_more_comfortable_with_you_and_your_companions_than_with_my_current_liege"),
		(try_end),
  			
		(try_begin),
			(lt, ":result_for_security", 10),
			(assign, ":no_join", 1),
			
			(try_begin),
				(this_or_next|troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_cunning),
				(troop_slot_ge, ":target_troop", slot_lord_reputation_type, lrep_roguish),
				(str_store_string, s32, "str_militarily_youre_in_no_position_to_protect_me_should_i_be_attacked_id_be_reluctant_to_join_you_until_you_could"),
			(else_try),	
				(troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_upstanding),
				(str_store_string, s32, "str_militarily_when_i_consider_the_lay_of_the_land_i_realize_that_to_pledge_myself_to_you_now_would_endanger_my_faithful_retainers_and_my_family"),
			(else_try),	
				(troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_martial),
				(str_store_string, s32, "str_militarily_youre_in_no_position_to_come_to_my_help_if_someone_attacked_me_i_dont_mind_a_good_fight_but_i_like_to_have_a_chance_of_winning"),
			(else_try),	
				(troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_goodnatured),
				(str_store_string, s32, "str_militarily_youre_in_no_position_to_come_to_my_help_if_someone_attacked_me_i_dont_mind_a_good_fight_but_i_like_to_have_a_chance_of_winning"),									
			(else_try),	
				(troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_debauched),
				(str_store_string, s32, "str_militarily_you_would_have_me_join_you_only_to_find_myself_isolated_amid_a_sea_of_enemies"),
			(else_try),	
				(troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_selfrighteous),
				(str_store_string, s32, "str_militarily_you_would_have_me_join_you_only_to_find_myself_isolated_amid_a_sea_of_enemies"),
			(else_try),	 
				(troop_slot_eq, ":target_troop", slot_lord_reputation_type, lrep_quarrelsome),
				(str_store_string, s32, "str_militarily_youre_in_no_position_to_come_to_my_help_if_someone_attacked_me_youd_let_me_be_cut_down_like_a_dog_id_bet"),					
			(try_end),
		(else_try),
			(lt, ":result_for_security_comparative", 0),
			(assign, ":no_join", 1),
			(str_store_string, s32, "str_militarily_i_wouldnt_be_any_safer_if_i_joined_you"),
		(else_try),
			(str_store_string, s32, "str_militarily_i_might_be_safer_if_i_joined_you"),
		(try_end),
		
		(try_begin),
			(gt, ":change_penalty", 40),
			(assign, ":no_join", 1),
			(str_store_string, s34, "str_finally_there_is_a_cost_to_ones_reputation_to_change_sides_in_this_case_the_cost_would_be_very_high"),
		(else_try),
			(gt, ":change_penalty", 20),
			(assign, ":no_join", 1),
			(str_store_string, s34, "str_finally_there_is_a_cost_to_ones_reputation_to_change_sides_in_this_case_the_cost_would_be_significant"),
		(else_try),
			(str_store_string, s34, "str_finally_there_is_a_cost_to_ones_reputation_to_change_sides_in_this_case_however_many_men_would_understand"),
		(else_try),
  			(str_store_string, s40, "@{s31} {s32} {s34}"),
		(try_end),
			
		(eq, ":no_join", 1),
		##diplomacy start+ use reg0 for gender
		(call_script, "script_dplmc_store_troop_is_female", ":target_troop"),
	],	#Next line "He" to {reg0?She:he}
		"Well, {s21}, at last I've found you. I have returned from my persuasion mission to {s30}. {s14} doesn't want to join you. {reg0?She:He} said: {s40}","companion_rejoin_response",
		##diplomacy end+
	[               
   ]],


 ##companion returning after persuasion request
  [anyone, "event_triggered", [
      (store_conversation_troop, "$map_talk_troop"),
      (eq, "$map_talk_troop", "$npc_to_rejoin_party"), 
      (troop_get_slot, ":mission", "$g_talk_troop", slot_troop_current_mission), 
	  (eq, ":mission", dplmc_npc_mission_persuasion),    
      (troop_get_slot, ":string", "$map_talk_troop", slot_troop_honorific),
      (str_store_string, 21, ":string"),
	  (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
	  (str_store_faction_name, s31, ":mission_object"),		
	  (troop_get_slot, ":target_troop", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy),
      
      (str_store_troop_name, s14, ":target_troop"),			 
                     ],
   "Well, {s21}, at last I've found you. I have returned from my persuasion mission to {s31}. {s14} agreed to join you.","companion_rejoin_response", [ 
	  (troop_get_slot, ":target_troop", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy),       
      (call_script, "script_change_troop_faction", ":target_troop", "$players_kingdom"),
#Diplomacy 3.2 end  
      (store_faction_of_troop, ":target_faction", ":target_troop"),
      (faction_get_slot, ":other_liege", ":target_faction", slot_faction_leader),
      (try_begin),
        (store_relation, ":relation", "$players_kingdom", ":target_faction"), 
        (ge, ":relation", 0),
        
        (call_script, "script_add_log_entry", logent_border_incident_troop_suborns_lord, "trp_player", -1, ":target_troop",":target_faction"),
        (store_add, ":slot_provocation_days", "$players_kingdom", slot_faction_provocation_days_with_factions_begin),
        (val_sub, ":slot_provocation_days", kingdoms_begin),
        (faction_set_slot, ":target_faction", ":slot_provocation_days", 30),
        
        (faction_get_slot, ":other_liege", ":target_faction", slot_faction_leader),
        (call_script, "script_troop_change_relation_with_troop", "trp_player", ":other_liege", -3),
      (try_end),
      
	  (call_script, "script_change_player_right_to_rule", 2), 
     ]],
   
   ##spy mission
   [anyone|plyr, "minister_talk",
   [
   (is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),
   ],
   "I wish to spy out another sovereignty.", "dplmc_minister_spy_kingdoms",
   []],

   ## ask for spy target
   [anyone, "dplmc_minister_spy_kingdoms",
   [
    (assign, ":companion_found", 0),
    (try_for_range, ":emissary", companions_begin, companions_end),
      (main_party_has_troop, ":emissary"),
      (assign, ":companion_found", 1),
    (try_end),
    (eq, ":companion_found", 1),
   
   ],
   "To whom do you wish to send this spy?", "dplmc_minister_spy_kingdoms_select",
   []],
   
   [anyone, "dplmc_minister_spy_kingdoms",
   [
   ],
   "Unfortunately, there is no one to send right now.", "minister_pretalk",
   []],
   
  ##select spy target
 [anyone|plyr|repeat_for_factions, "dplmc_minister_spy_kingdoms_select",
   [
     (store_repeat_object, ":faction_no"),
	 (is_between, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
     (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
     (faction_get_slot, ":leader_no", ":faction_no", slot_faction_leader),
     (str_store_troop_name, s10, ":leader_no"),
     (str_store_faction_name, s11, ":faction_no"),
	 (str_clear, s14),
     ],
   "{s11}{s14}", "dplmc_minister_spy_emissary",
   [
     (store_repeat_object, "$g_faction_selected"),
     (assign, "$g_initiative_selected", dplmc_npc_mission_spy_request)
     ]],
     
   [anyone, "dplmc_minister_spy_emissary",
   [], "Who shall be your spy? You should choose one whom you trust - and who has skills in spotting!", "minister_emissary_select",
   []],

  ##dispatch spy
  [anyone, "minister_emissary_dispatch",
   [
   (str_store_troop_name, s11, "$g_emissary_selected"),
   (str_store_faction_name, s12, "$g_faction_selected"),
   (eq, "$g_initiative_selected", dplmc_npc_mission_spy_request),
	 (str_store_string, s14, "str_dplmc_gather_information"),
	 (store_skill_level, ":emissary_spotting", "skl_spotting", "$g_emissary_selected"),
	 (val_mul, ":emissary_spotting", 5),
	 (val_add, ":emissary_spotting", 65),
	 (val_min, ":emissary_spotting", 95),	 
	 (store_random_in_range, ":random", 0, 100),

   (try_begin),#debug
     (eq, "$cheat_mode", 1),  
     (assign, reg0, ":emissary_spotting"),
     (display_message, "@{!}DEBUG : emissary_spotting: {reg0}"),
     (assign, reg0, ":random"),
     (display_message, "@{!}DEBUG : random: {reg0}"),
   (try_end),	 
   
	 (try_begin),
	   (ge, ":emissary_spotting", ":random"),
	   (assign, "$diplomacy_var", 0), # not caught
   (else_try),
   	 (lt, ":emissary_spotting", ":random"),
	   (assign, "$diplomacy_var", 1), # caught
   (try_end), 
   ], "Very well -- I shall send {s11} to the {s12} to {s14}.", "minister_diplomatic_dispatch_confirm",[]],

	##companion returning after spy request
	[anyone, "event_triggered", [
		(store_conversation_troop, "$map_talk_troop"),
		(eq, "$map_talk_troop", "$npc_to_rejoin_party"),
		(troop_get_slot, ":mission", "$g_talk_troop", slot_troop_current_mission),
		(eq, ":mission", dplmc_npc_mission_spy_request),
		(troop_get_slot, ":emissary_caught", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy),
		(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
		(this_or_next|eq, ":emissary_caught", 0),
		(faction_slot_eq, ":mission_object", slot_faction_state, sfs_defeated),
		(troop_get_slot, ":string", "$map_talk_troop", slot_troop_honorific),
		(str_store_string, 21, ":string"),
		(str_store_faction_name, s31, ":mission_object"),
	],
	"Well, {s21}, at last I've found you. I have returned from my reconnaissance mission to {s31}. About which location do you need information?","dplmc_companion_spy_request_select_center", [
				  ]],
                    
 ##companion caught after spy request
  [anyone, "event_triggered", [ ##Floris MTT was trp_XXX
      (store_conversation_troop, "$map_talk_troop"),
	  ##Floris MTT begin
	  (troop_slot_eq, "$troop_trees", slot_mercenary_armbrust_miliz, "$map_talk_troop"),
	  ##Floris MTT end
      (troop_get_slot, "$g_talk_troop", "$g_talk_troop", slot_troop_mission_object), #switching npc
      (troop_get_slot, ":mission", "$g_talk_troop", slot_troop_current_mission), 
		  (eq, ":mission", dplmc_npc_mission_spy_request),      
      (troop_get_slot, ":emissary_caught", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy),
      (gt, ":emissary_caught", 0),

		  (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
			(str_store_faction_name, s31, ":mission_object"),		
			(str_store_troop_name, s11, "$g_talk_troop"),		 				 
                     ],
   "My, lord. I am coming back from the reconnaissance mission to {s31}. I am sorry, we were caught  off  guard and they got {s11}. I barely escaped.","close_window", [
        (troop_set_slot, "$g_talk_troop", slot_troop_current_mission, 0), 
		    (troop_set_slot, "$g_talk_troop", slot_troop_days_on_mission, 0),
        (troop_set_slot, "$g_talk_troop", slot_troop_occupation, 0), 
        (assign, "$npc_to_rejoin_party", 0),
       
        (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
        
        (call_script, "script_change_player_relation_with_faction", ":mission_object", -3),
        (call_script, "script_change_player_honor", -2),
        (call_script, "script_change_troop_renown", "trp_player", -5),
         
        (faction_get_slot, ":faction_leader", ":mission_object", slot_faction_leader),
        (call_script, "script_lord_get_home_center", ":faction_leader"),
        (try_begin),
          (neq, reg0, -1),
          (assign, ":target_party", reg0),
        (else_try),
          (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
            (store_faction_of_party, ":center_faction", ":walled_center"),
			      (eq, ":mission_object", ":center_faction"),
			      (assign, ":target_party", ":walled_center"),
			    (try_end),
        (try_end),
        (try_begin),
          (is_between, ":target_party", walled_centers_begin, walled_centers_end),
          (party_add_prisoners, ":target_party", "$g_talk_troop", 1), 
        (try_end),               
   ]],
					
   [anyone|plyr|repeat_for_parties, "dplmc_companion_spy_request_select_center",
   [
     (store_repeat_object, ":center_no"),
     (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),	
     (is_between, ":center_no", centers_begin, centers_end),
     (store_faction_of_party, ":center_faction", ":center_no"),
     (eq, ":center_faction", ":mission_object"),
     (str_store_party_name, s60, ":center_no"),
   ],"{s60}", "dplmc_companion_spy_request_center_selected",
   [
   (store_repeat_object, "$spy_center_selected"),
   ]], 
   
  [anyone, "dplmc_companion_spy_request_center_selected", [
      (call_script, "script_dplmc_party_calculate_strength", "$spy_center_selected", 0),
      (try_begin),
        (le, reg0, 1),
        (str_store_string, s31, "str_dplmc_nearly_no"),
      (else_try),
        (is_between, reg0, 1, 100),
        (str_store_string, s31, "str_dplmc_less_than_one_hundred"),
      (else_try),
        (is_between, reg0, 101, 200),
        (str_store_string, s31, "str_dplmc_more_than_one_hundred"),
      (else_try),
        (is_between, reg0, 201, 500),
        (str_store_string, s31, "str_dplmc_more_than_two_hundred"), 
      (else_try),
        (ge, reg0, 500),
        (str_store_string, s31, "str_dplmc_more_than_five_hundred"),
      (try_end),     

      (call_script, "script_dplmc_describe_prosperity_to_s4", "$spy_center_selected"),
      
      (party_get_slot, ":center_relation", "$spy_center_selected", slot_center_player_relation),
      (call_script, "script_describe_center_relation_to_s3", ":center_relation"),     

      ],  "{s4} {s3} and there are {s31} troops around.", "dplmc_companion_spy_request_select_newcenter", [
          ]],
          
  [anyone, "dplmc_companion_spy_request_select_newcenter", [
      ],  "Do you need information about another location?", "dplmc_companion_spy_request_select_center", [
          ]],
   
  [anyone|plyr, "dplmc_companion_spy_request_select_center", [
      ],  "Never mind.", "companion_rejoin_response", [
          ]],

    ##alliance request
  [anyone|plyr, "minister_diplomatic_initiative_type_select",
   [
    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_player_supporters_faction", "$g_faction_selected"),
    (eq, reg0, 1),  #player is at truce with the mission_faction

    (assign, ":proceed", 0),
    (try_begin),
      (store_add, ":slot_truce_days", "$g_faction_selected", slot_faction_truce_days_with_factions_begin),
      (val_sub, ":slot_truce_days", kingdoms_begin),
      (faction_get_slot, ":truce_days", "fac_player_supporters_faction", ":slot_truce_days"),
      (is_between, ":truce_days", 20, 50), #you need a trade aggreement or defensive pact for an alliance
      (assign, ":proceed", 1), 
    (try_end),
    (eq, ":proceed", 1),

    (faction_slot_eq, "$g_faction_selected", slot_faction_recognized_player, 1), #recognized us
    (faction_slot_eq, "$g_faction_selected", slot_faction_state, sfs_active),
    (faction_get_slot, ":leader_no", "$g_faction_selected", slot_faction_leader),

	(str_store_troop_name, s10, ":leader_no"),
	(str_store_faction_name, s11, "$g_faction_selected"),
	(str_clear, s14),
	###diplomacy start+ Use reg0 for gender
	(call_script, "script_dplmc_store_troop_is_female", ":leader_no"),
	],#Next line "him" to {reg0?her:him}
	"Tell {s10} that I want to conclude a defensive pact with {reg0?her:him}.", "minister_diplomatic_emissary",
	##diplomacy end+
	[ (assign, "$g_initiative_selected", dplmc_npc_mission_defensive_request),
	]],

 ##companion returning after alliance request
  [anyone, "event_triggered", [
           (store_conversation_troop, "$map_talk_troop"),
           (eq, "$map_talk_troop", "$npc_to_rejoin_party"), 
           (troop_get_slot, ":mission", "$g_talk_troop", slot_troop_current_mission), 
					 (eq, ":mission", dplmc_npc_mission_alliance_request),
					 				
					 (troop_get_slot, ":string", "$map_talk_troop", slot_troop_honorific),
           (str_store_string, 21, ":string"),
					 (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
					 (str_store_faction_name, s31, ":mission_object"),				 

					 (call_script, "script_npc_decision_checklist_peace_or_war", ":mission_object", "fac_player_supporters_faction", "$g_talk_troop"),
					 (assign, "$g_mission_result_with_player", reg0),					 
                     ],
   "Well, {s21}, at last I've found you. I have returned from my mission to {s31}. ","dplmc_companion_alliance_request_response", [
                    ]],
                    
  ##response to alliance request success		
  [anyone, "dplmc_companion_alliance_request_response", [
    (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, dplmc_npc_mission_alliance_request), 
    (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),                   
    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_player_supporters_faction", ":mission_object"),
    (ge, reg0, 0),  #player is at peace or truce with the mission_faction
    (eq, "$g_concession_demanded", 0), #doesn't want a center from us
    (ge, "$g_mission_result_with_player", 1), #doesn't want war with us
    (store_relation, ":relation", "fac_player_supporters_faction", ":mission_object"),
    (store_random_in_range,":random", 20, 95),
    (ge, ":relation", ":random"),  
    (store_random_in_range,":random", 5, 75),
    (ge, "$player_honor", ":random"),
    (store_random_in_range,":random", 5, 50),
    (ge, "$player_right_to_rule", ":random"),
    (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
    (str_store_troop_name, s4, ":emissary_object"),
  ],					
   "{s4} is willing to form an alliance with you.","dplmc_companion_alliance_confirm", [
					]],
					
  [anyone|plyr, "dplmc_companion_alliance_confirm", [
	(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
	(str_store_faction_name, s4, ":mission_object"),
  ],					
   "Very well - let this alliance with {s4} be concluded.","companion_rejoin_response", [
	(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
    (call_script, "script_dplmc_start_alliance_between_kingdoms", ":mission_object", "$players_kingdom", 1), 
	(str_store_faction_name, s4, ":mission_object"),
	]],

  [anyone|plyr, "dplmc_companion_alliance_confirm", [],					
   "On second thought, perhaps this is not now in our interests.","companion_rejoin_response", [
					]],
					
  ##response to alliance request failed						
  [anyone, "dplmc_companion_alliance_request_response", [
    (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, dplmc_npc_mission_alliance_request), 
    (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
    (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
    (str_store_troop_name, s4, ":emissary_object"),
    ],					
   "{s4} is not willing to form an alliance with you.","companion_rejoin_response", [
					]],
					
    ##defensive request
  [anyone|plyr, "minister_diplomatic_initiative_type_select",
   [
    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_player_supporters_faction", "$g_faction_selected"),
    (eq, reg0, 1),  #player is at truce with the mission_faction

    (assign, ":proceed", 0),
    (try_begin),
      (store_add, ":slot_truce_days", "$g_faction_selected", slot_faction_truce_days_with_factions_begin),
      (val_sub, ":slot_truce_days", kingdoms_begin),
      (faction_get_slot, ":truce_days", "fac_player_supporters_faction", ":slot_truce_days"),
      #(gt, ":truce_days", 20), #if we have more than 20 truce days left don't proceed   
      (is_between, ":truce_days", 0, 30), #you need a non-aggression or trade aggreement for an defensive pact
      (assign, ":proceed", 1), 
    (try_end),
    (eq, ":proceed", 1),

    (faction_slot_eq, "$g_faction_selected", slot_faction_recognized_player, 1), #recognized us
    (faction_slot_eq, "$g_faction_selected", slot_faction_state, sfs_active),
    (faction_get_slot, ":leader_no", "$g_faction_selected", slot_faction_leader),

(str_store_troop_name, s10, ":leader_no"),
(str_store_faction_name, s11, "$g_faction_selected"),
(str_clear, s14),
###diplomacy start+ Use reg0 for gender
(call_script, "script_dplmc_store_troop_is_female", ":leader_no"),
],#Next line "him" to {reg0?her:him}
"Tell {s10} that I want to conclude a defensive pact with {reg0?her:him}.", "minister_diplomatic_emissary",
##diplomacy end+
[ (assign, "$g_initiative_selected", dplmc_npc_mission_defensive_request),
]],

 ##companion returning after defensive request
  [anyone, "event_triggered", [
           (store_conversation_troop, "$map_talk_troop"),
           (eq, "$map_talk_troop", "$npc_to_rejoin_party"), 
           (troop_get_slot, ":mission", "$g_talk_troop", slot_troop_current_mission), 
					 (eq, ":mission", dplmc_npc_mission_defensive_request),
					 				
					 (troop_get_slot, ":string", "$map_talk_troop", slot_troop_honorific),
           (str_store_string, 21, ":string"),
					 (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
					 (str_store_faction_name, s31, ":mission_object"),				 

					 (call_script, "script_npc_decision_checklist_peace_or_war", ":mission_object", "fac_player_supporters_faction", "$g_talk_troop"),
					 (assign, "$g_mission_result_with_player", reg0),					 
                     ],
   "Well, {s21}, at last I've found you. I have returned from my mission to {s31}. ","dplmc_companion_defensive_request_response", [
                    ]],
                    
  ##response to defensive request success		
  [anyone, "dplmc_companion_defensive_request_response", [
    (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, dplmc_npc_mission_defensive_request), 
    (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),                   
    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_player_supporters_faction", ":mission_object"),
    (ge, reg0, 0),  #player is at peace or truce with the mission_faction
    (eq, "$g_concession_demanded", 0), #doesn't want a center from us
    (ge, "$g_mission_result_with_player", 1), #doesn't want war with us
    (store_relation, ":relation", "fac_player_supporters_faction", ":mission_object"),
    (store_random_in_range,":random", 15, 70), #20 96 alliance
    (ge, ":relation", ":random"),  
    (store_random_in_range,":random", 0, 50), #5 75 alliance
    (ge, "$player_honor", ":random"),
    (store_random_in_range,":random", 5, 30), #5 50 alliance
    (ge, "$player_right_to_rule", ":random"),
    (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
    (str_store_troop_name, s4, ":emissary_object"),
  ],					
   "{s4} is willing to form a defensive pact with you.","dplmc_companion_defensive_confirm", [
					]],
					
  [anyone|plyr, "dplmc_companion_defensive_confirm", [
	(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
	(str_store_faction_name, s4, ":mission_object"),
  ],					
   "Very well - let this defensive pact with {s4} be concluded.","companion_rejoin_response", [
	(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
    (call_script, "script_dplmc_start_defensive_between_kingdoms", ":mission_object", "$players_kingdom", 1), 
	(str_store_faction_name, s4, ":mission_object"),
	]],

  [anyone|plyr, "dplmc_companion_defensive_confirm", [],					
   "On second thought, perhaps this is not now in our interests.","companion_rejoin_response", [
					]],
					
  ##response to defensive request failed						
  [anyone, "dplmc_companion_defensive_request_response", [
    (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, dplmc_npc_mission_defensive_request), 
    (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
    (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
    (str_store_troop_name, s4, ":emissary_object"),
    ],					
   "{s4} is not willing to conclude a defensive pact with you.","companion_rejoin_response", [
					]],
					
    ##trade request
  [anyone|plyr, "minister_diplomatic_initiative_type_select",
   [
    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_player_supporters_faction", "$g_faction_selected"),
    (ge, reg0, 0),  #player is at peace or truce with the mission_faction

    (assign, ":proceed", 0),
    (try_begin),
      (store_add, ":slot_truce_days", "$g_faction_selected", slot_faction_truce_days_with_factions_begin),
      (val_sub, ":slot_truce_days", kingdoms_begin),
      (faction_get_slot, ":truce_days", "fac_player_supporters_faction", ":slot_truce_days"), 
      (lt, ":truce_days", 10), #you need a non-aggression or peace for a trade pact
      (assign, ":proceed", 1), 
    (try_end),
    (eq, ":proceed", 1),

    (faction_slot_eq, "$g_faction_selected", slot_faction_recognized_player, 1), #recognized us
    (faction_slot_eq, "$g_faction_selected", slot_faction_state, sfs_active),
    (faction_get_slot, ":leader_no", "$g_faction_selected", slot_faction_leader),

    (str_store_troop_name, s10, ":leader_no"),
    (str_store_faction_name, s11, "$g_faction_selected"),
    (str_clear, s14),
##diplomacy start+ correct pronouns
(call_script, "script_dplmc_store_troop_is_female", ":leader_no"),
],
"Tell {s10} that I want to sign a trade agreement with {reg0?her:him}.", "minister_diplomatic_emissary",
##diplomacy end+
   [ (assign, "$g_initiative_selected", dplmc_npc_mission_trade_request),
     ]],

 ##companion returning after trade request
  [anyone, "event_triggered", [
           (store_conversation_troop, "$map_talk_troop"),
           (eq, "$map_talk_troop", "$npc_to_rejoin_party"), 
           (troop_get_slot, ":mission", "$g_talk_troop", slot_troop_current_mission), 
					 (eq, ":mission", dplmc_npc_mission_trade_request),
					 				
					 (troop_get_slot, ":string", "$map_talk_troop", slot_troop_honorific),
           (str_store_string, 21, ":string"),
					 (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
					 (str_store_faction_name, s31, ":mission_object"),				 

					 (call_script, "script_npc_decision_checklist_peace_or_war", ":mission_object", "fac_player_supporters_faction", "$g_talk_troop"),
					 (assign, "$g_mission_result_with_player", reg0),					 
                     ],
   "Well, {s21}, at last I've found you. I have returned from my mission to {s31}. ","dplmc_companion_trade_request_response", [
                    ]],
                    
  ##response to trade request success		
  [anyone, "dplmc_companion_trade_request_response", [
    (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, dplmc_npc_mission_trade_request), 
    (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),                   
    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_player_supporters_faction", ":mission_object"),
    (ge, reg0, 0),  #player is at peace or truce with the mission_faction
    (eq, "$g_concession_demanded", 0), #doesn't want a center from us
    (ge, "$g_mission_result_with_player", 1), #doesn't want war with us
    (store_relation, ":relation", "fac_player_supporters_faction", ":mission_object"),
    (store_random_in_range,":random", 10, 50), #20 96 alliance
    (ge, ":relation", ":random"),  
    (store_random_in_range,":random", 0, 25), #5 75 alliance
    (ge, "$player_honor", ":random"),
    (store_random_in_range,":random", 5, 15), #5 50 alliance
    (ge, "$player_right_to_rule", ":random"),
    (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
    (str_store_troop_name, s4, ":emissary_object"),
  ],					
   "{s4} is willing to sign a trade agreement with you.","dplmc_companion_trade_confirm", [
					]],
					
  [anyone|plyr, "dplmc_companion_trade_confirm", [
	(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
	(str_store_faction_name, s4, ":mission_object"),
  ],					
   "Very well - let's sign the trade agreement with {s4}.","companion_rejoin_response", [
	(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
    (call_script, "script_dplmc_start_trade_between_kingdoms", ":mission_object", "$players_kingdom", 1), 
	(str_store_faction_name, s4, ":mission_object"),
	]],

  [anyone|plyr, "dplmc_companion_trade_confirm", [],					
   "On second thought, perhaps this is not now in our interests.","companion_rejoin_response", [
					]],
					
  ##response to trade request failed						
  [anyone, "dplmc_companion_trade_request_response", [
    (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, dplmc_npc_mission_trade_request), 
    (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
    (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
    (str_store_troop_name, s4, ":emissary_object"),
    ],					
   "{s4} is not willing to sign a trade agreement.","companion_rejoin_response", [
					]],
					
    ##nonaggression request
  [anyone|plyr, "minister_diplomatic_initiative_type_select",
   [
    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_player_supporters_faction", "$g_faction_selected"),
    (eq, reg0, 0),  #player is at peace

    (faction_slot_eq, "$g_faction_selected", slot_faction_state, sfs_active),
    (faction_get_slot, ":leader_no", "$g_faction_selected", slot_faction_leader),

    (str_store_troop_name, s10, ":leader_no"),
    (str_store_faction_name, s11, "$g_faction_selected"),
	(str_clear, s14),
	###diplomacy start+ Use reg0 for gender
	(call_script, "script_dplmc_store_troop_is_female", ":leader_no"),
	],#next line "him" to {reg0?her:him}
	"Tell {s10} that I want to conclude a non-aggression treaty with {reg0?her:him}.", "minister_diplomatic_emissary",
	##diplomacy end+
	[ (assign, "$g_initiative_selected", dplmc_npc_mission_nonaggression_request),
     ]],

 ##companion returning after nonaggression request
  [anyone, "event_triggered", [
           (store_conversation_troop, "$map_talk_troop"),
           (eq, "$map_talk_troop", "$npc_to_rejoin_party"), 
           (troop_get_slot, ":mission", "$g_talk_troop", slot_troop_current_mission), 
					 (eq, ":mission", dplmc_npc_mission_nonaggression_request),
					 				
					 (troop_get_slot, ":string", "$map_talk_troop", slot_troop_honorific),
           (str_store_string, 21, ":string"),
					 (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
					 (str_store_faction_name, s31, ":mission_object"),				 

					 (call_script, "script_npc_decision_checklist_peace_or_war", ":mission_object", "fac_player_supporters_faction", "$g_talk_troop"),
					 (assign, "$g_mission_result_with_player", reg0),					 
                     ],
   "Well, {s21}, at last I've found you. I have returned from my mission to {s31}. ","dplmc_companion_nonaggression_request_response", [
                    ]],
                    
  ##response to nonaggression request success		
  [anyone, "dplmc_companion_nonaggression_request_response", [
    (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, dplmc_npc_mission_nonaggression_request), 
    (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),                   
    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_player_supporters_faction", ":mission_object"),
    (ge, reg0, 0),  #player is at peace or truce with the mission_faction
    (eq, "$g_concession_demanded", 0), #doesn't want a center from us
    (ge, "$g_mission_result_with_player", 1), #doesn't want war with us
    (store_relation, ":relation", "fac_player_supporters_faction", ":mission_object"),
    (store_random_in_range,":random", 5, 25), #20 96 alliance
    (ge, ":relation", ":random"),  
    (store_random_in_range,":random", 0, 20), #5 75 alliance
    (ge, "$player_honor", ":random"),
    (store_random_in_range,":random", 5, 10), #5 50 alliance
    (ge, "$player_right_to_rule", ":random"),
    (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
    (str_store_troop_name, s4, ":emissary_object"),
  ],					
   "{s4} is willing to conclude a non-aggression treaty with you.","dplmc_companion_nonaggression_confirm", [
					]],
					
  [anyone|plyr, "dplmc_companion_nonaggression_confirm", [
	(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
	(str_store_faction_name, s4, ":mission_object"),
  ],					
   "Very well - let this non-aggression treaty with {s4} be concluded.","companion_rejoin_response", [
	(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
    (call_script, "script_dplmc_start_nonaggression_between_kingdoms", ":mission_object", "$players_kingdom", 1), 
	(str_store_faction_name, s4, ":mission_object"),
	]],

  [anyone|plyr, "dplmc_companion_nonaggression_confirm", [],					
   "On second thought, perhaps this is not now in our interests.","companion_rejoin_response", [
					]],
					
  ##response to nonaggression request failed						
  [anyone, "dplmc_companion_nonaggression_request_response", [
    (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, dplmc_npc_mission_nonaggression_request), 
    (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
    (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
    (str_store_troop_name, s4, ":emissary_object"),
    ],					
   "{s4} is not willing to conclude a non-aggression treaty with you.","companion_rejoin_response", [
					]],
                    
    ##war request
  [anyone|plyr|repeat_for_factions, "minister_diplomatic_initiative_type_select",
   [
    (assign, ":proceed", 1),
    (try_begin),
      (eq, reg0, 2), #truce
      (store_add, ":slot_truce_days", "$g_faction_selected", slot_faction_truce_days_with_factions_begin),
      (val_sub, ":slot_truce_days", kingdoms_begin),
      (faction_get_slot, ":truce_days", "fac_player_supporters_faction", ":slot_truce_days"), 
      (gt, ":truce_days", 0), #you need at least a non-aggression pact
      (assign, ":proceed", 0), 
    (try_end),
    (eq, ":proceed", 1),   

    (store_repeat_object, ":faction_no"),
    (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
    (neq, ":faction_no", "fac_player_supporters_faction"),
    (neq, ":faction_no", "$g_faction_selected"),
    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_player_supporters_faction", ":faction_no"),
    (eq, reg0, -2), #player is at war with the target faction
    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_player_supporters_faction", "$g_faction_selected"),
    (ge, reg0, 0),  #player is at peace or truce with the mission_faction
    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "$g_faction_selected", ":faction_no"),
    (is_between, reg0, -1, 1),  #mission_faction provocated or peace with target_faction
    (faction_slot_eq, "$g_faction_selected", slot_faction_recognized_player, 1), #recognized us
    (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
    (faction_get_slot, ":leader_no", ":faction_no", slot_faction_leader),
    (str_store_troop_name, s10, ":leader_no"),
    (str_store_faction_name, s11, ":faction_no"),
	(str_clear, s14),
	###diplomacy start+ Use reg0 for gender
	(call_script, "script_dplmc_store_troop_is_female", ":leader_no"),
	],#next line "him" to {reg0?her:him}
	"That I want {reg0?her:him} to help me and attack {s11}{s14}.", "minister_diplomatic_emissary",
	##diplomacy end+
	[ (assign, "$g_initiative_selected", dplmc_npc_mission_war_request),
	(store_repeat_object, "$diplomacy_var"),
	]],

 ##companion returning after war request
  [anyone, "event_triggered", [
    (store_conversation_troop, "$map_talk_troop"),
    (eq, "$map_talk_troop", "$npc_to_rejoin_party"), 
    (troop_get_slot, ":mission", "$g_talk_troop", slot_troop_current_mission), 
    (eq, ":mission", dplmc_npc_mission_war_request),
    
    (troop_get_slot, ":string", "$map_talk_troop", slot_troop_honorific),
    (str_store_string, 21, ":string"),
    (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
    (str_store_faction_name, s31, ":mission_object"),				 
    
    (call_script, "script_npc_decision_checklist_peace_or_war", ":mission_object", "fac_player_supporters_faction", "$g_talk_troop"),
    (assign, "$g_mission_result_with_player", reg0),	
    (call_script, "script_npc_decision_checklist_peace_or_war", ":mission_object", "$diplomacy_var", -1),
	(assign, "$g_mission_result_with_target", reg0),
	##diplomacy start+
	#Disable agreeing to declare war when the kingdoms are allied.
	#Make it less likely when they have other treaties.
	(call_script, "script_dplmc_get_faction_truce_length_with_faction", ":mission_object", "$diplomacy_var"),
	(try_begin),
		#TODO: Later there should be other intrigue options, but for now let's just
		#make it so refusal is automatic for alliances, and possible for other types.
		(gt, reg0, dplmc_treaty_defense_days_expire),
		(val_max, "$g_mission_result_with_target", 3),#Positive means does not want war
	(else_try),
		(gt, reg0, dplmc_treaty_truce_days_expire),
		(store_random_in_range, reg0, 0, 2),
		(try_begin),
			(eq, reg0, 1),
			(val_max, "$g_mission_result_with_target", 3),#Positive means does not want war
		(else_try),
			(val_add, "$g_mission_result_with_target", 1),#If was undecided, choose no
			(val_max, "$g_mission_result_with_target", 0),#Best result is "undecided"
		(try_end),
	(try_end),
	##diplomacy end+
					],
   "Well, {s21}, at last I've found you. I have returned from my mission to {s31}. ","dplmc_companion_war_request_response", [
                    ]],

  ##response to war request success		
  [anyone, "dplmc_companion_war_request_response", [
    (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, dplmc_npc_mission_war_request), 
    (lt, "$g_mission_result_with_target", 0), #<0 want's war with target
    (ge, "$g_mission_result_with_player", 2), #doesn't want war with us
    (eq, "$g_concession_demanded", 0), #doesn't want a center from us
    (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_player_supporters_faction", ":mission_object"),
    (ge, reg0, 0),  #player is at peace or truce with the mission_faction
	(troop_get_slot, ":war_target_faction", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy),
	##diplomacy start+
	#The other kingdom will only agree to declare war without asking for money in return
	#if the player's kingdom is also at war with it, or if it is in an alliance with the
	#player's kingdom.
	(store_relation, ":player_faction_relation_with_war_target", ":war_target_faction", "$players_kingdom"),
	(call_script, "script_dplmc_get_faction_truce_length_with_faction", ":mission_object", "$players_kingdom"),
	(this_or_next|ge, reg0, dplmc_treaty_defense_days_half_done),
	   (lt, ":player_faction_relation_with_war_target", 0),
	##diplomacy end+
	(str_store_faction_name, s31, ":war_target_faction"),
	(faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
	(str_store_troop_name, s4, ":emissary_object"),
	],
	"{s4} is willing to start a war with {s31}.","companion_rejoin_response", [
	(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
	(troop_get_slot, ":war_target_faction", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy),
	(call_script, "script_diplomacy_start_war_between_kingdoms",  ":mission_object", ":war_target_faction", 1)
			 ]],

	##response to war request success
	[anyone, "dplmc_companion_war_request_response", [
	(troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, dplmc_npc_mission_war_request),
	##diplomacy start+
	(this_or_next|lt, "$g_mission_result_with_target", 0),
	##diplomacy end+
	(eq, "$g_mission_result_with_target", 0), #undecided about war
	(ge, "$g_mission_result_with_player", 2), #doesn't want war with us
	(eq, "$g_concession_demanded", 0), #doesn't want a center from us
	(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
	(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_player_supporters_faction", ":mission_object"),
	(ge, reg0, 0),  #player is at peace or truce with the mission_faction
	(troop_get_slot, ":war_target_faction", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy),
	(str_store_faction_name, s31, ":war_target_faction"),
	(faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
	(str_store_troop_name, s4, ":emissary_object"),
	##diplomacy start+
	#Set the payment amount to something less arbitrary than a flat 5000.
	#For example, using the same mercenary payment calculation used for the player.
	(assign, ":total_fee", 0),
	(try_for_parties, ":party_no"),
	   (gt, ":party_no", centers_end),
		(party_is_active, ":party_no"),
	   (store_faction_of_party, ":party_faction", ":party_no"),
		(eq, ":party_faction", ":mission_object"),
		(this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
		   (party_slot_eq, ":party_no", slot_party_type, spt_patrol),
		(try_begin),
		   (eq, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
			(call_script, "script_dplmc_get_terrain_code_for_battle", -1, ":party_no"),
			(call_script, "script_dplmc_party_calculate_strength_in_terrain", ":party_no", reg0, 0, 1),
			#Cache terrain value, but use non-terrain value for cost
			(assign, reg0, reg1),
		(else_try),
		   (call_script, "script_party_calculate_strength", ":party_no", 0),
		(try_end),
		(val_div, reg0, 2),
		(val_add, reg0, 30),
		(call_script, "script_round_value", reg0),
		(val_max, reg0, 50),#at least 50 denars per party
		(val_add, ":total_fee", reg0),
	(try_end),
	(val_mul, ":total_fee", 2),#The mercenary fee for two weeks

	(try_begin),
		#Lessen the fee if the other kingdom particularly wants war
		(lt, "$g_mission_result_with_target", 0),
		(val_div, ":total_fee", 2),
	(try_end),
	(try_begin),
		#Increase the fee if the player's faction is allied with the target
		#(note: this should probably be disabled altogether...)
		(call_script, "script_dplmc_get_faction_truce_length_with_faction", ":mission_object", "$players_kingdom"),
		(ge, reg0, dplmc_treaty_defense_days_expire),
		(val_mul, ":total_fee", 3),
	(else_try),
		(store_relation, reg0, ":war_target_faction", "$players_kingdom"),
		(val_mul, reg0, 2),
	(try_end),		

	(game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
	(try_begin),
	   (eq, ":reduce_campaign_ai", 0),#Hard: 150%
		(val_mul, ":total_fee", 3),
		(val_div, ":total_fee", 2),
	(else_try),
	   (eq, ":reduce_campaign_ai", 1),#Medium: 100%
	(else_try),
	   (eq, ":reduce_campaign_ai", 2),#Easy: 50%
		(val_div, ":total_fee", 2),
	(try_end),

	(val_max, ":total_fee", 5000),

	(call_script, "script_dplmc_store_troop_is_female", ":mission_object"),
	(assign, reg1, ":total_fee"),
	(assign, "$temp_2", ":total_fee"),#save for later
	],
	#"{s4} is willing to start a war with {s31} but needs 5000 denars to prepare his army.","dplmc_companion_war_pay", [
	"{s4} is willing to start a war with {s31} but needs {reg1} denars to prepare {reg0?her:his} army.","dplmc_companion_war_pay", [
			 ]],
	##diplomacy end+
					
  ##option to pay for war					
  [anyone|plyr, "dplmc_companion_war_pay", [
	  (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
	  (str_store_faction_name, s4, ":mission_object"),
	  (gt, "$g_player_chamberlain", 0),
	(store_troop_gold, ":gold", "trp_household_possessions"),
	##diplomacy start+
	#(ge, ":gold", 5000),
	(ge, ":gold", "$temp_2"),
	(call_script, "script_dplmc_store_troop_is_female", ":mission_object"),
	(assign, reg1, "$temp_2"),
	],
	#"Pay 5000 denars from the treasury and tell him to start the war.","companion_rejoin_response", [
	"Pay {reg1} denars from the treasury and tell {reg0?her:him} to start the war.","companion_rejoin_response", [
	#(call_script, "script_dplmc_withdraw_from_treasury", 5000),
	(assign, ":paid_gold", "$temp_2"),
	(call_script, "script_dplmc_withdraw_from_treasury", ":paid_gold"),
	##diplomacy end+
	(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
	##diplomacy start+ actually give gold to other kingdom
	(call_script, "script_dplmc_faction_leader_splits_gold", ":mission_object", ":paid_gold"),
	##diplomacy end+
	(troop_get_slot, ":war_target_faction", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy),
	(call_script, "script_diplomacy_start_war_between_kingdoms",  ":mission_object", ":war_target_faction", 1)
	]],
	
	
  [anyone|plyr, "dplmc_companion_war_pay", [],					
   "On second thought, I don't think we can take so much money from the treasury.","companion_rejoin_response", [
					]],
					
  ##response to war request failed						
  [anyone, "dplmc_companion_war_request_response", [
    (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, dplmc_npc_mission_war_request), 
    (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
    (troop_get_slot, ":war_target_faction", "$g_talk_troop", dplmc_slot_troop_mission_diplomacy),
    (str_store_faction_name, s31, ":war_target_faction"),
    (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
    (str_store_troop_name, s4, ":emissary_object"),                   
  ],					
   "{s4} is not willing to start a war with {s31}.","companion_rejoin_response", [
					]],
	
  ##he doesn't want a center but we can pay him			
  [anyone, "companion_embassy_results", [
    (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_peace_request), 
	(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
	##diplomacy start+ save the results of the script to avoid unnecessary repeated calls,
	#which may introduce unexpected behavior if it's changed to used random numbers.
	(call_script, "script_dplmc_get_truce_pay_amount", "fac_player_supporters_faction", ":mission_object", "$g_mission_result"),
	(assign, "$temp", reg0),
	(assign, "$temp_2", reg1),
	##diplomacy end+
	(faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
	(str_store_troop_name, s12, ":emissary_object"),
	(is_between, "$g_mission_result", -2, 1), #-2 or -1 or 0
	##diplomacy start+
	#(call_script, "script_dplmc_get_truce_pay_amount", "fac_player_supporters_faction", ":mission_object", "$g_mission_result"),
	(gt, "$temp", 0),
	(lt, "$temp_2", 0),
	(assign, reg4, 0),#Use reg4 for gender
	(try_begin),
		(call_script, "script_cf_dplmc_troop_is_female", ":emissary_object"),
		(assign, reg4, 1),
	(try_end),
	],
	"{s12} says that {reg4?she:he} is willing to consider a truce of twenty days if you pay {reg4?her:him} {reg0} denars.","dplmc_companion_truce_pay", [
			 ]],
	##diplomacy end+

  ##we can pay him or pay him and give a center					
  [anyone, "companion_embassy_results", [
    (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_peace_request), 
    (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
    (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),  
    (str_store_troop_name, s12, ":emissary_object"),
	(is_between, "$g_mission_result", -2, 1), #-2 or -1 or 0
	##diplomacy start+
	#(call_script, "script_dplmc_get_truce_pay_amount", "fac_player_supporters_faction", ":mission_object", "$g_mission_result"),
	(gt, "$temp", 0),
	(gt, "$temp_2", 0),
	(assign, reg0, "$temp"),
	(assign, reg1, "$temp_2"),
	(str_store_party_name, s18, "$g_concession_demanded"),
	(assign, reg4, 0),#Use reg4 for gender
	(try_begin),
		(call_script, "script_cf_dplmc_troop_is_female", ":emissary_object"),
		(assign, reg4, 1),
	(try_end),
	],
	##next line fixed diplomacy bug, companion_truce_pay -> dplmc_companion_truce_pay; also gender from reg4
	"{s12} says that {reg4?she:he} is willing to consider a truce of twenty days if you yield to {reg4?her:his} terms. Either you pay {reg0} denars or you pay {reg1} denars and give {reg4?her:him} {s18}.","dplmc_companion_truce_pay", [
			 ]],
	##diplomacy end+

	##diplomacy start+
	#Missing options: will only accept a center / will only accept a center and money
	[anyone, "companion_embassy_results", [
	(troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_peace_request),
	(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
	(faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
	(str_store_troop_name, s12, ":emissary_object"),
	(is_between, "$g_mission_result", -2, 1), #-2 or -1 or 0,
	(le, "$temp", 0),
	(eq, "$temp_2", 0),
	(str_store_party_name, s18, "$g_concession_demanded"),
	(assign, reg4, 0),
	(try_begin),
		(call_script, "script_cf_dplmc_troop_is_female", ":emissary_object"),
		(assign, reg4, 1),
	(try_end),
	],#Next line: gender from reg4
	"{s12} says that {reg4?she:he} is willing to consider a truce of twenty days if you give {reg4?her:him} {s18}.","dplmc_companion_truce_pay", [
			 ]],
	 ##diplomacy end+	 

	[anyone, "companion_embassy_results", [
	(troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_peace_request),
	(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
	(faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
	(str_store_troop_name, s12, ":emissary_object"),
	(is_between, "$g_mission_result", -2, 1), #-2 or -1 or 0,
	(le, "$temp", 0),
	(ge, "$temp_2", 1),
	(assign, reg0, "$temp_2"),
	(str_store_party_name, s18, "$g_concession_demanded"),
	##diplomacy start+ Make gender correct
	(assign, reg4, 0),
	(try_begin),
		(call_script, "script_cf_dplmc_troop_is_female", ":emissary_object"),
		(assign, reg4, 1),
	(try_end),
	],#Next line: gender from reg4
	"{s12} says that {reg4?she:he} is willing to consider a truce of twenty days if you pay {reg4?her:him} {reg0} denars and give {reg4?her:him} {s18}.","dplmc_companion_truce_pay", [
			 ]],
	##diplomacy end+

	##we can pay him or give the center
	[anyone, "companion_embassy_results", [
	(troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_peace_request),
	(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
	(faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
	(str_store_troop_name, s12, ":emissary_object"),
	(is_between, "$g_mission_result", -2, 1), #-2 or -1 or 0
	##diplomacy start+
	#(call_script, "script_dplmc_get_truce_pay_amount", "fac_player_supporters_faction", ":mission_object", "$g_mission_result"),
	(gt, "$temp", 0),
	(eq, "$temp_2", 0),
	(assign, reg0, "$temp"),
	(str_store_party_name, s18, "$g_concession_demanded"),
	(assign, reg4, 0),
	(try_begin),
		(call_script, "script_cf_dplmc_troop_is_female", ":emissary_object"),
		(assign, reg4, 1),
	(try_end),
	],#Next line gender from reg4
	"{s12} says that {reg4?she:he} is willing to consider a truce of twenty days if you pay {reg4?her:him} {reg0} or give {reg4?her:him} {s18}.","dplmc_companion_truce_pay", [
			 ]],

	#This was bugged, and should logically never occur.
	##we have so many prisoners we don't have to pay
	#[anyone, "companion_embassy_results", [
	#  (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_peace_request),#
	#		(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
	#		(faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
	#		(str_store_troop_name, s12, ":emissary_object"),
	#		(is_between, "$g_mission_result", -2, 1), #-2 or -1 or 0
	#  (call_script, "script_dplmc_get_truce_pay_amount", "fac_player_supporters_faction", ":mission_object", "$g_mission_result"),
	#  (eq, reg0, 0),
	#  (le, reg1, 0),
	#],
	# "{s12} says that he is willing to consider a truce of twenty days.","companion_truce_confirm", [
	#					]],
	##diplomacy end+

  ##option to pay him					
  [anyone|plyr, "dplmc_companion_truce_pay", [
	  (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
	  (str_store_faction_name, s4, ":mission_object"),
		(store_troop_gold, ":gold", "trp_player"),#
		##diplomacy start+
		(assign, reg0, "$temp"),
		(gt, reg0, 0),
		(ge, ":gold", reg0),
		],
		"Pay {reg0} denars and let the truce with the {s4} be concluded","companion_rejoin_response", [
		(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
		(troop_remove_gold, "trp_player", "$temp"),#todo change amount
		#actually give gold to other kingdom
		(call_script, "script_dplmc_faction_leader_splits_gold", ":mission_object", "$temp"),
		##diplomacy end+
		(call_script, "script_diplomacy_start_peace_between_kingdoms", ":mission_object", "$players_kingdom", 1),
		(str_store_faction_name, s4, ":mission_object"),
		]],

	##option to pay him and give him a center
	[anyone|plyr, "dplmc_companion_truce_pay", [
		(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
		(str_store_faction_name, s4, ":mission_object"),
		(store_troop_gold, ":gold", "trp_player"),
		##diplomacy start+ 
		(assign, reg1, "$temp_2"),
		(gt, reg1, 0),
		(ge, ":gold", reg1),
		(faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
		(assign, reg4, 0),
		(try_begin),
			(call_script, "script_cf_dplmc_troop_is_female", ":emissary_object"),
			(assign, reg4, 1),
		(try_end),
		],
		"Pay {reg1} denars and give {reg4?her:him} {s18} let this truce with the {s4} be concluded","companion_rejoin_response", [
		(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
		(troop_remove_gold, "trp_player", reg1),#todo change amount
		#actually give gold to other kingdom
		(call_script, "script_dplmc_faction_leader_splits_gold", ":mission_object", reg0),
		##diplomacy end+
		(call_script, "script_give_center_to_faction", "$g_concession_demanded", ":mission_object"),
		(call_script, "script_diplomacy_start_peace_between_kingdoms", ":mission_object", "$players_kingdom", 1),
		(str_store_faction_name, s4, ":mission_object"),
	]],

	##option to give him a center
	[anyone|plyr, "dplmc_companion_truce_pay", [
		(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
		(str_store_faction_name, s4, ":mission_object"),
		(gt, "$g_concession_demanded", 0),
		##diplomacy start+
		(eq, "$temp_2", 0),
		(faction_get_slot, ":leader_no", ":mission_object", slot_faction_leader),
		(call_script, "script_dplmc_store_troop_is_female", ":leader_no"),
		],#next line "him" to {reg0?her:him}
		"Give {reg0?her:him} {s18} let this truce with the {s4} be concluded","companion_rejoin_response", [
		##diplomacy end+
		(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
		(call_script, "script_give_center_to_faction", "$g_concession_demanded", ":mission_object"),
		(call_script, "script_diplomacy_start_peace_between_kingdoms", ":mission_object", "$players_kingdom", 1),
		(str_store_faction_name, s4, ":mission_object"),
	]],

	[anyone|plyr, "dplmc_companion_truce_pay", [],
		"On second thought, perhaps this is not now in our interests..","companion_rejoin_response", [
	 ]],

	##diplomacy end
   
   
   [anyone|plyr, "minister_talk",
   [],
   "That is all for now.", "close_window",
   []],


   [anyone, "minister_change_marshal",
	[],
	"Who should be the new marshal?", "minister_change_marshal_choose",
	[]],

   [anyone|plyr, "minister_change_marshal_choose",
	[],
	"I shall be marshal", "minister_pretalk",
	[
	(call_script, "script_appoint_faction_marshall", "fac_player_supporters_faction", "trp_player"),
	(store_current_hours, ":hours"),
	(assign, "$g_recalculate_ais", 1),
	(assign, "$g_player_faction_last_marshal_appointment", ":hours"),

	##diplomacy start+ Handle player is co-ruler of NPC kingdom
	#Added section begin
	(assign, ":ruled_faction", "fac_player_supporters_faction"),
	(try_begin),
		(neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":ruled_faction", "$players_kingdom"),
	(try_end),
	#Added section end
	#In the following section, replace references to "fac_player_supporter_faction" with ":ruled_faction"
	(try_begin),
		#(faction_slot_eq, "fac_player_supporters_faction", slot_faction_political_issue, 1),
		#(faction_set_slot, "fac_player_supporters_faction", slot_faction_political_issue, 0),
		(faction_slot_eq, ":ruled_faction", slot_faction_political_issue, 1),
		(faction_set_slot, ":ruled_faction", slot_faction_political_issue, 0),
		(faction_set_slot, "fac_player_supporters_faction", slot_faction_political_issue, 0),

		(troop_set_slot, "trp_player",  slot_troop_stance_on_faction_issue, -1),
		#Also change to support promoted kingdom ladies
		#(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
		(try_for_range, ":active_npc", heroes_begin, heroes_end),
		   (this_or_next|is_between, ":active_npc", active_npcs_begin, active_npcs_end),
			  (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
		   (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
		   (eq, ":active_npc_faction", ":ruled_faction"),
		   (troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
		(try_end),
	(try_end),
	##diplomacy end+
	]],

	[anyone|plyr, "minister_change_marshal_choose",
	[],
	"For a short while, we should have no marshal", "minister_pretalk",
	[
	##diplomacy start+ Handle player is co-ruler of NPC kingdom
	#Added section begin
	(assign, ":ruled_faction", "fac_player_supporters_faction"),
	(try_begin),
		(neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":ruled_faction", "$players_kingdom"),
	(try_end),
	#Added section end
	#In the following section, replace references to "fac_player_supporter_faction" with ":ruled_faction"
	(call_script, "script_appoint_faction_marshall", ":ruled_faction", -1),
	(try_begin),
		(faction_slot_eq, ":ruled_faction", slot_faction_political_issue, 1),
		(faction_set_slot, ":ruled_faction", slot_faction_political_issue, 0),
		(faction_set_slot, "fac_player_supporters_faction", slot_faction_political_issue, 0),#if not the same as ruled faction

		(troop_set_slot, "trp_player",  slot_troop_stance_on_faction_issue, -1),
		(try_for_range, ":active_npc", heroes_begin, heroes_end),#Also change this to support all herose
		   (this_or_next|is_between, ":active_npc", active_npcs_begin, active_npcs_end),
			  (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
		   (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
		   (eq, ":active_npc_faction", ":ruled_faction"),
		   (troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
		(try_end),
	(try_end),
	##diplomacy end+ (replacing fac_player_supporters_faction with :ruled_faction)
	(assign, "$g_recalculate_ais", 1),
	
	]],
	
   [anyone|plyr|repeat_for_troops, "minister_change_marshal_choose",
	[
	(store_repeat_object, ":lord"),
##diplomacy start+ support promoted ladies
#(is_between, ":lord", active_npcs_begin, active_npcs_end),
(is_between, ":lord", heroes_begin, heroes_end),
##diplomacy end+
	(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
	(store_faction_of_troop, ":lord_faction", ":lord"),
	##diplomacy start+ Handle player is co-ruler of NPC kingdom
	(assign, ":is_faction_member", 0),
	(try_begin),
		(eq, ":lord_faction", "$players_kingdom"),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":is_faction_member", 1),
	(try_end),
	(this_or_next|eq, ":is_faction_member", 1),
	##diplomacy end+
	(eq, ":lord_faction", "fac_player_supporters_faction"),
	(str_store_troop_name, s4, ":lord"),
	],
	"{s4}", "minister_pretalk",
	[
	(store_repeat_object, ":lord"),
	##diplomacy start+ Handle player is co-ruler of NPC kingdom
	#Added section begin
	(assign, ":ruled_faction", "fac_player_supporters_faction"),
	(try_begin),
		(neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":ruled_faction", "$players_kingdom"),
	(try_end),
	#Added section end
	#In the following section, replace references to "fac_player_supporter_faction" with ":ruled_faction"
	(call_script, "script_appoint_faction_marshall", ":ruled_faction", ":lord"),#dplmc+ changed
	(store_current_hours, ":hours"),
	(assign, "$g_player_faction_last_marshal_appointment", ":hours"),
	#xxx TODO: Modify both fac_player_supporters_faction and players_kingdom in parallel
	(try_begin),
		(faction_slot_eq, ":ruled_faction", slot_faction_political_issue, 1),#dplmc+ changed
		(faction_set_slot, ":ruled_faction", slot_faction_political_issue, 0),#dplmc+ changed
		(faction_set_slot, "fac_player_supporters_faction", slot_faction_political_issue, 0),#dplmc+ added

		(troop_set_slot, "trp_player",  slot_troop_stance_on_faction_issue, -1),
		#(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),#Changed this to support promoted kingdom ladies
		(try_for_range, ":active_npc", heroes_begin, heroes_end),
			(this_or_next|is_between, ":active_npc", active_npcs_begin, active_npcs_end),
				(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
		   (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
		   (eq, ":active_npc_faction", ":ruled_faction"),#dplmc+ changed
		   (troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
		(try_end),
	(try_end),
	##diplomacy end+
	(assign, "$g_recalculate_ais", 1),
	]],
	
	
   [anyone|plyr, "minister_change_marshal_choose",
	[],
	"Never mind.", "minister_pretalk",
	[]],



	[anyone, "minister_diplomatic_kingdoms",
	[
	##diplomacy start+
	#Speed up, and also support non-traditional companions.
	##OLD:
	#(assign, ":companion_found", 0),
	#(try_for_range, ":emissary", companions_begin, companions_end),
	#(main_party_has_troop, ":emissary"),
	#(assign, ":companion_found", 1),
	#(try_end),
	#(eq, ":companion_found", 1),
	(assign, ":end_cond", heroes_end),
	(try_for_range, ":emissary", heroes_begin, ":end_cond"),
		(this_or_next|is_between, ":emissary", companions_begin, companions_end),
			(troop_slot_eq, ":emissary", slot_troop_occupation, slto_player_companion),
		(main_party_has_troop, ":emissary"),
		(assign, ":end_cond", ":emissary"),
	(try_end),
	(lt, ":end_cond", heroes_end),
	],
	"To whom do you wish to send this emissary?", "minister_diplomatic_kingdoms_select",
	[]],

   [anyone, "minister_diplomatic_kingdoms",
   [
   ],
   "Unfortunately, there is no one to send right now.", "minister_pretalk",
   []],


   
   [anyone, "minister_diplomatic_kingdoms",
   [],
   "To whom do you wish to send this emissary?", "minister_diplomatic_kingdoms_select",
   []],

 [anyone|plyr|repeat_for_factions, "minister_diplomatic_kingdoms_select",
   [
	(store_repeat_object, ":faction_no"),
	(is_between, ":faction_no", kingdoms_begin, kingdoms_end),
	##diplomacy start+ Required if the player can be ruler or co-ruler of another faction
	(neg|faction_slot_eq, ":faction_no", slot_faction_leader, "trp_player"),
	(neq, ":faction_no", "$players_kingdom"),
	##diplomacy end+
	(neq, ":faction_no", "fac_player_supporters_faction"),
	(faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
	(faction_get_slot, ":leader_no", ":faction_no", slot_faction_leader),
	(str_store_troop_name, s10, ":leader_no"),
	(str_store_faction_name, s11, ":faction_no"),
	(str_clear, s14),
	#Has/has not recognized us a monarch
	],
   "{s10} of the {s11}{s14}", "minister_diplomatic_initiative_type",
   [
     (store_repeat_object, "$g_faction_selected"),
     ]],

## Start 1.134
   [anyone|plyr, "minister_diplomatic_kingdoms_select",
   [],
   "Never mind", "minister_pretalk",
   []],
## End 1.134
	 
	[anyone, "minister_diplomatic_initiative_type",
	##diplomacy start+
	[
	(faction_get_slot, ":leader_no", "$g_faction_selected", slot_faction_leader),#Use reg0 for gender
	(call_script, "script_dplmc_store_troop_is_female", ":leader_no"),
	],#next line "him" to {reg0?her:him}
	"What do you wish to tell {reg0?her:him}?", "minister_diplomatic_initiative_type_select",
	[]],
	##diplomacy end+

  [anyone|plyr, "minister_diplomatic_initiative_type_select",
   [(store_relation, ":relation", "fac_player_supporters_faction", "$g_faction_selected"),
    (lt, ":relation", 0),],
   "That our two sovereignties should enter into truce.", "minister_diplomatic_emissary",
   [(assign, "$g_initiative_selected", npc_mission_peace_request)]],

	[anyone|plyr, "minister_diplomatic_initiative_type_select",
	##diplomacy start+
	#[],
	[
	#Disable when the player is the ruler or co-ruler of an NPC kingdom.
	#Setting up a separate dialog for this is something to do later, but
	#not a high priority.
	#TODO: Consider if there should be an alternative when the player is married to a pretender.
	(neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
	(faction_get_slot, ":leader_no", "$g_faction_selected", slot_faction_leader),#Use reg0 for gender
	(call_script, "script_dplmc_store_troop_is_female", ":leader_no"),
	],#next line "his" to {reg0?her:his}
	"That I wish to put myself under {reg0?her:his} protection, as {reg0?her:his} vassal.", "minister_diplomatic_emissary",
	##diplomacy end+
	[(assign, "$g_initiative_selected", npc_mission_pledge_vassal)]],

	[anyone|plyr, "minister_diplomatic_initiative_type_select",
	[(store_relation, ":relation", "fac_player_supporters_faction", "$g_faction_selected"),
	(faction_slot_eq, "$g_faction_selected", slot_faction_recognized_player, 0),
	(ge, ":relation", 0),],
	"That I wish to express my goodwill, as one monarch to another.", "minister_diplomatic_emissary",
	[(assign, "$g_initiative_selected", npc_mission_seek_recognition),]],

	[anyone|plyr, "minister_diplomatic_initiative_type_select",
	[(store_relation, ":relation", "fac_player_supporters_faction", "$g_faction_selected"),
	(ge, ":relation", 0),##diplomacy start+],
#(neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),#Disable when the player shares power
	(faction_get_slot, ":leader_no", "$g_faction_selected", slot_faction_leader),#Use reg0 for gender
	(call_script, "script_dplmc_store_troop_is_female", ":leader_no"),
	],#next line "him" to {reg0?her:him}
	"That I declare war upon {reg0?her:him}.", "minister_declare_war",
						 ##diplomacy end+
	[]],
 
  [anyone|plyr, "minister_diplomatic_initiative_type_select",[], "Never mind", "close_window",[]],

##diplomacy start+
##
#Disable when the player is the ruler or co-ruler of an NPC kingdom.
#Setting up a separate dialog for this is something to do later, but
#not a high priority.
#TODO: Consider if there should be an alternative when the player is married to a pretender.
[anyone, "minister_declare_war",
[
   (assign, ":veto_troop", 0),
   (try_begin),
      (gt, "$players_kingdom", -1),
      (faction_get_slot, reg0, "$players_kingdom", slot_faction_leader),
      (gt, reg0, "trp_player"),
      (assign, ":veto_troop", reg0),
   (else_try),
      (is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
      (troop_get_slot, reg0, "trp_player", slot_troop_spouse),
	  (gt, reg0, 0),
      (assign, ":veto_troop", reg0),
   (try_end),
   (gt, ":veto_troop", 0),
   (str_store_troop_name, s0, ":veto_troop"),
], "For that you should first speak to {s0}.", "dplmc_minister_nevermind", []],

[anyone|plyr, "dplmc_minister_nevermind", [],
	"I might go do so.", "close_window",[]],

[anyone|plyr, "dplmc_minister_nevermind", [],
	"Never mind.", "minister_pretalk",[]],
##diplomacy end+
[anyone, "minister_declare_war",
[(try_begin),
   		(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_player_supporters_faction", "$g_faction_selected"),
		(eq, reg0, 1),
		(str_store_string, s12, "str_in_doing_so_you_will_be_in_violation_of_your_truce_is_that_what_you_want"),
	(else_try),
   		(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_player_supporters_faction", "$g_faction_selected"),
		(neq, reg0, -1),
		(str_store_string, s12, "str_if_you_attack_without_provocation_some_of_your_vassals_may_consider_you_to_be_too_warlike_is_that_what_you_want"),
	(else_try),
		(str_store_string, s12, "str_our_men_are_ready_to_ride_forth_at_your_bidding_are_you_sure_this_is_what_you_want"),
    (try_end),
   ], "{s12}", "minister_declare_war_confirm",
   []],

  [anyone|plyr, "minister_declare_war_confirm",
   [(str_store_faction_name, s12, "$g_faction_selected"),
   ],
   "It is. I wish to make war on {s12}.", "minister_declare_war_confirm_yes",
   [
    (call_script, "script_diplomacy_start_war_between_kingdoms",  "fac_player_supporters_faction", "$g_faction_selected", 1),
	]],

  [anyone|plyr, "minister_declare_war_confirm",
   [(str_store_faction_name, s12, "$g_faction_selected"),
   ],
   "Hmm. Perhaps not.", "minister_pretalk",
   [
	]],
	
  [anyone, "minister_declare_war_confirm_yes",
   [(str_store_faction_name, s12, "$g_faction_selected"),
   ],
   "As you command. We are now at war with the {s12}. May the heavens grant us victory.", "minister_pretalk",
   [
	]],
   

   [anyone, "minister_diplomatic_emissary",					#Diplo+ Port Marker
   [], "Who shall be your emissary? You should choose one whom you trust, but who is also persuasive -- one who can negotiate without giving offense.", "minister_emissary_select",
   []],

  [anyone|plyr|repeat_for_troops, "minister_emissary_select",[
  (store_repeat_object, ":emissary"),
  (main_party_has_troop, ":emissary"),
	##diplomacy start+
	##OLD:
	#(is_between, ":emissary", companions_begin, companions_end),
	#(troop_slot_eq, ":emissary", slot_troop_prisoner_of_party, -1),
	#(is_between, ":emissary", active_npcs_begin, active_npcs_end),
	##NEW:
	# Support alternate possible companions
	(is_between, ":emissary", heroes_begin, heroes_end),
	(troop_slot_eq, ":emissary", slot_troop_prisoner_of_party, -1),
	(this_or_next|is_between, ":emissary", companions_begin, companions_end),
	(troop_slot_eq, ":emissary", slot_troop_occupation, slto_player_companion),
	##diplomacy end+
  #LAZERAS MODIFIED  {Expanded Dialog Kit}
  ## Jrider + DIALOGS v1.0 evaluate emissary skill level
  #(str_store_troop_name, s11, ":emissary"),
  (call_script, "script_set_diplomatic_emissary_skill_level_string", ":emissary", "skl_persuasion", 0),
  ## Jrider -
  #LAZERAS MODIFIED  {Expanded Dialog Kit}
  ], "{s11}", "minister_emissary_dispatch",[
  (store_repeat_object, "$g_emissary_selected"),
  ]],
   
  [anyone|plyr, "minister_emissary_select",[
  ], "Actually, I can't think of anyone.", "minister_pretalk",[]],

  [anyone, "minister_emissary_dispatch",
   [
   (str_store_troop_name, s11, "$g_emissary_selected"),
   (str_store_faction_name, s12, "$g_faction_selected"),
   (try_begin),
		(eq, "$g_initiative_selected", npc_mission_seek_recognition),
		(str_store_string, s14, "str_seek_recognition"),
   (else_try),
		(eq, "$g_initiative_selected", npc_mission_pledge_vassal),
		(str_store_string, s14, "str_seek_vassalhood"),
   (else_try),
		(eq, "$g_initiative_selected", npc_mission_peace_request),
		(str_store_string, s14, "str_seek_a_truce"),
    ##Diplomacy 3.3.2 begin
    (else_try),
		(eq, "$g_initiative_selected", dplmc_npc_mission_nonaggression_request),
		(str_store_string, s14, "str_dplmc_conclude_non_agression"),
    ##Diplomacy 3.3.2 end
   (try_end),
   ], "Very well -- I shall send {s11} to the {s12} to {s14}.", "minister_diplomatic_dispatch_confirm",[]],

  [anyone|plyr, "minister_diplomatic_dispatch_confirm",[], "Yes, do that", "minister_pretalk",[
    (troop_set_slot, "$g_emissary_selected", slot_troop_days_on_mission, 3),
  	(troop_set_slot, "$g_emissary_selected", slot_troop_current_mission, "$g_initiative_selected"),
  	(troop_set_slot, "$g_emissary_selected", slot_troop_mission_object, "$g_faction_selected"),
	##diplomacy begin
	(try_begin),
		(eq, "$g_initiative_selected", dplmc_npc_mission_gift_horses_request),
		(call_script, "script_dplmc_withdraw_from_treasury", "$diplomacy_var"),
	(try_end),

	(troop_set_slot, "$g_emissary_selected", dplmc_slot_troop_mission_diplomacy, "$diplomacy_var"),
	(troop_set_slot, "$g_emissary_selected", dplmc_slot_troop_mission_diplomacy2, "$diplomacy_var2"),
	##diplomacy end

	(remove_member_from_party, "$g_emissary_selected", "p_main_party"),
  ]],
   
   
  [anyone|plyr, "minister_diplomatic_dispatch_confirm",[], "Actually, hold off on that", "minister_pretalk",[]],

  [anyone, "minister_replace",
   [], "Very good. Whom will you appoint in my stead?", "minister_replace_select",
   []],

  [anyone|plyr|repeat_for_troops, "minister_replace_select",
   [
   (store_repeat_object, ":troop_no"),
   (is_between, ":troop_no", companions_begin, companions_end),
   (main_party_has_troop, ":troop_no"),
   (troop_slot_eq, ":troop_no", slot_troop_prisoner_of_party, -1),
	##diplomacy start+
	##OLD:
	#(str_store_troop_name, s4, ":troop_no"),
	##NEW:
	(call_script, "script_dplmc_cap_troop_describes_troop_to_troop_s1", 1, "trp_player", ":troop_no", "$g_talk_troop"),
	(str_store_string_reg, s4, s1),
	##diplomacy end+
   ], "{s4}", "minister_replace_confirm",
   [
   (store_repeat_object, "$g_player_minister"),
   ]],

   [anyone|plyr, "minister_replace_select",
   [
   (troop_get_slot, ":spouse", "trp_player", slot_troop_spouse),
   (gt, ":spouse", 0),
	##diplomacy start+
	##OLD:
	#(troop_get_type, ":is_female", ":spouse"),
	#(neg|troop_slot_eq, ":spouse", slot_troop_occupation, slto_kingdom_hero),
	#(eq, ":is_female", 1),
	##NEW:
	#Most of this logic has been moved to the next dialog.  Use this solely for handling
	#spouses outside the normal hero range.
	(neg|is_between, ":spouse", heroes_begin, heroes_end),
	(troop_slot_eq, ":spouse", slot_troop_occupation, slto_kingdom_hero),
	(neg|troop_slot_ge, ":spouse", slot_troop_occupation, slto_retirement),#not retired, in exile, or dead
	(call_script, "script_dplmc_store_troop_is_female", ":spouse"),
	##diplomacy end+

	(str_store_troop_name, s4, ":spouse"),
	(neq, ":spouse", "$g_talk_troop"),
	##diplomacy start+
	##OLD:
	#], "My wife, {s4}.", "minister_replace_confirm", #husband disabled, as he's an active lord
	##NEW:
	], "My {reg0?wife:husband}, {s4}.", "minister_replace_confirm", #Gender assumptions like that aren't useful
	##diplomacy end+
	[
	(troop_get_slot, "$g_player_minister", "trp_player", slot_troop_spouse),
	]],

	##diplomacy start+
	#Support for multiple spouses, or for other dependents.
	[anyone|plyr|repeat_for_troops, "minister_replace_select",
	[
	(store_repeat_object, ":troop_no"),
	(is_between, ":troop_no", heroes_begin, heroes_end),#is a valid hero
	(this_or_next|is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),#is a kingdom lady
		(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_lady),
	(neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),#Not a promoted kingdom lady
	(neg|troop_slot_ge, ":troop_no", slot_troop_occupation, slto_retirement),#Not retired, dead, exiled, etc.
	(neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),#Not a prisoner
	(this_or_next|neg|is_between, ":troop_no", companions_begin, companions_end),#Don't double-list companions
		(neg|main_party_has_troop, ":troop_no"),

	(neq, ":troop_no", "$g_talk_troop"),

	(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_no", "trp_player"),
	(gt, reg0, 0),#Related
	#(assign, ":relation_string_index", reg1),

	(try_begin),
		(this_or_next|ge, reg0, 15),#Spouse, child, parent
		(this_or_next|eq, reg1, "str_dplmc_sister_wife"),
			(eq, reg1, "str_dplmc_co_husband"),
	(else_try),
		#Otherwise, disallow if the troop has a (valid) guardian who is not the
		#player or themself
		(call_script, "script_get_kingdom_lady_social_determinants", ":troop_no"),
		(try_begin),
			(this_or_next|le, reg0, "trp_player"),#the player or a negative value
				(eq, reg0, ":troop_no"),
			(assign, reg0, 1),
		(else_try),
			(assign, reg0, 0),
		(try_end),
	(try_end),
	(ge, reg0, 0),
	#(str_store_string, s11, ":relation_string_index"),
	#(str_store_troop_name, s4, ":troop_no"),
	(call_script, "script_dplmc_cap_troop_describes_troop_to_troop_s1", 1, "trp_player", ":troop_no", "$g_talk_troop"),
	(str_store_string_reg, s4, s1),
	], "{s4}.", "minister_replace_confirm", #husband disabled, as he's an active lord
	[
	(store_repeat_object, "$g_player_minister"),
	]],
	##diplomacy end+

	[anyone|plyr, "minister_replace_select",
	[], "Actually, hold off on that.", "minister_pretalk",
	[]],



   
  [anyone, "minister_replace_confirm",
   [
   (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_player_companion),
   ], "Very good. {s9} is your new minister. I shall make ready to rejoin you.", "close_window",
   [
   (str_store_troop_name, s9, "$g_player_minister"),
   (party_add_members, "p_main_party", "$g_talk_troop", 1), 
   (assign, "$g_leave_encounter", 1),
   (try_begin),
	  (main_party_has_troop, "$g_player_minister"),
      (party_remove_members, "p_main_party", "$g_player_minister", 1), 
   (try_end),
   
   (try_for_range, ":minister_quest", all_quests_begin, all_quests_end),
	(quest_slot_eq, ":minister_quest", slot_quest_giver_troop, "$g_talk_troop"),
	(call_script, "script_abort_quest", ":minister_quest", 0), ##1.132
#	(call_script, "script_abort_quest", ":minister_quest"), ##1.131
   (try_end),
   ]],
   
  [anyone, "minister_replace_confirm",
   [
   ], "Very good. {s9} is your new minister. It has been an honor to serve you.", "close_window",
   [
   (str_store_troop_name, s9, "$g_player_minister"),
   (try_begin),
	(main_party_has_troop, "$g_player_minister"),
    (party_remove_members, "p_main_party", "$g_player_minister", 1), 
   (try_end),
	##diplomacy start+ Occupation cleanup
	(try_begin),
		#Nothing needs to be done for non-heroes, or if the occupation is already kingdom hero or kingdom lady.
		(this_or_next|neg|is_between, "$g_talk_troop", heroes_begin, heroes_end),
		(this_or_next|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
			(troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
	(else_try),
		(is_between, "$g_talk_troop", kingdom_ladies_begin, kingdom_ladies_end),
		(neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
		(neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_lord_rejoined),
		(troop_set_slot, "$g_talk_troop", slot_troop_occupation, slto_kingdom_lady),
	(else_try),
		#This can't be reached right now, but if it is, make sure that the companion goes
		#back to the taverns instead of suddenly becoming a hero.
		(is_between, "$g_talk_troop", companions_begin, companions_end),
		(neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
		(neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_lord_rejoined),
		(neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
		(troop_set_slot, "$g_talk_troop", slot_troop_occupation, slto_inactive),
	(else_try),
		(troop_set_slot, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
	(else_try),

	(try_end),
	##diplomacy end+   
   ]],
   


   [anyone, "minister_grant_fief",
   [
   (faction_get_slot, ":fief_on_agenda", "$players_kingdom", slot_faction_political_issue),
   (str_clear, s12),
   (try_begin),
	(is_between, ":fief_on_agenda", centers_begin, centers_end),
    (str_store_party_name, s4, ":fief_on_agenda"),
	(str_store_string, s12, "str_minister_advice_select_fief"),
   (else_try),
    (eq, ":fief_on_agenda", 1),
	(str_store_string, s12, "str_minister_advice_select_fief_wait"),
   (try_end),
   ],
   "Which of your fiefs did you wish to grant?{s12}", "minister_grant_fief_select",
   []],


   [anyone|plyr|repeat_for_parties, "minister_grant_fief_select",
   [
   (store_repeat_object, ":center_no"),
   (is_between, ":center_no", centers_begin, centers_end),
   (store_faction_of_party, ":center_faction", ":center_no"),
   (eq, ":center_faction", "fac_player_supporters_faction"),
   ##diplomacy begin
   (neg|party_slot_eq, ":center_no", slot_village_infested_by_bandits, "trp_woman_e_peasant"),
    ##diplomacy end
   (neq, ":center_no", "$g_player_court"),
	(party_get_slot, ":town_lord", ":center_no", slot_town_lord),
	(try_begin),
		(ge, ":town_lord", active_npcs_begin),
		(store_faction_of_troop, ":town_lord_faction", ":town_lord"),
		(neq, ":town_lord_faction", "fac_player_supporters_faction"),
		(assign, ":town_lord", -1),
	(try_end),
	(le, ":town_lord", 0),
   
   (str_store_party_name, s1, ":center_no"),
   (str_clear, s12),
   (try_begin),
	(party_slot_eq, ":center_no", slot_town_lord, -1),
	(str_store_string, s12, "str_unassigned_center"),
   (try_end),
   
   ],"{s1}{s12}", "minister_grant_fief_select_recipient",
   [
   (store_repeat_object, "$fief_selected"),
   ]],   

   [anyone|plyr, "minister_grant_fief_select",
   [
   ],"Never mind", "minister_pretalk",
   []],   
   
   [anyone, "minister_grant_fief_select_recipient",
   [
   (str_clear, s12),
   (try_begin),
	(faction_slot_eq, "$players_kingdom", slot_faction_political_issue, "$fief_selected"),
   
##diplomacy start+ support promoted ladies
#(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
(try_for_range, ":active_npc", heroes_begin, heroes_end),
##diplomacy end+
		(troop_set_slot, ":active_npc", slot_troop_temp_slot, 0),
	(try_end),
   
(assign, ":popular_favorite", -1),
(assign, ":votes_for_popular_favorite", 0),
##diplomacy start+
(troop_set_slot, "trp_player", slot_troop_temp_slot, 0),
#support promoted ladies
#(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
(try_for_range, ":active_npc", heroes_begin, heroes_end),
    (this_or_next|is_between, ":active_npc", active_npcs_begin, active_npcs_end),
       (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),    
##dipolomacy end+
		(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
		(eq, ":active_npc_faction", "fac_player_supporters_faction"),
		(troop_get_slot, ":selected_npc", ":active_npc", slot_troop_stance_on_faction_issue),
		(ge, ":selected_npc", 0),
		
		(troop_get_slot, ":votes_accumulated", ":selected_npc", slot_troop_temp_slot),
		(val_add, ":votes_accumulated", 1),
		(troop_set_slot, ":selected_npc", slot_troop_temp_slot, ":votes_accumulated"),
		
		(gt, ":votes_accumulated", ":votes_for_popular_favorite"),
		(assign,  ":votes_for_popular_favorite", ":votes_accumulated"),
		(assign, ":popular_favorite", ":selected_npc"),
	(try_end),
   
##diplomacy start+ support promoted ladies
#(is_between, ":popular_favorite", active_npcs_begin, active_npcs_end),
(is_between, ":popular_favorite", heroes_begin, heroes_end),
##diplomacy end+
    (str_store_troop_name, s4, ":popular_favorite"),
    (assign, reg4, ":votes_for_popular_favorite"),
	
	(str_store_string, s12, "str_minister_advice_fief_leading_vassal"),
  (try_end),
   
   ],"And who will you choose to receive the fief?{s12}", "minister_grant_fief_select_recipient_choice",
   []],   
      
   [anyone|plyr|repeat_for_troops, "minister_grant_fief_select_recipient_choice",
   [
	(store_repeat_object, ":troop_no"),
	(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
	##diplomacy start+ add support for promoted ladies
	#(is_between, ":troop_no", active_npcs_begin, active_npcs_end),
	(is_between, ":troop_no", heroes_begin, heroes_end),
	##diplomacy end+
	(store_faction_of_troop, ":troop_faction", ":troop_no"),
	##diplomacy start+ add support for player is ruler/co-ruler of NPC kingdom
	(is_between, ":troop_faction", kingdoms_begin, kingdoms_end),
	(this_or_next|eq, ":troop_faction", "$players_kingdom"),
	##diplomacy end+
	(eq, ":troop_faction", "fac_player_supporters_faction"),
	##diplomacy start+ show number of fiefs
	#(str_store_troop_name, s1, ":troop_no"),
	(str_store_troop_name, s11, ":troop_no"),
	(call_script, "script_print_troop_owned_centers_in_numbers_to_s0", ":troop_no"),
	(try_begin),
		(troop_slot_eq, "$g_talk_troop", slot_lord_recruitment_argument, argument_benefit),
		(str_store_string, s12, "str__promised_fief"),
	(else_try),
		(str_clear, s12),
	(try_end),
	(try_begin),
		(eq, reg0, 0),
		(str_store_string, s0, "str_no_fiefss12"),
	(else_try),
		(str_store_string, s0, "str_fiefs_s0s12"),
	(try_end),
	#add relation string
	(str_store_string_reg, s12, s63),#save s63, clobbering s12 (perhaps already overwritten)
	(call_script, "script_troop_get_player_relation", ":troop_no"),
	(call_script, "script_describe_relation_to_s63", reg0),
	(str_store_string_reg, s1, s63),#clobber s1
	(str_store_string_reg, s63, s12),#revert s63
	(str_store_string, s1, "str_dplmc_s0_comma_s1"),#write to s1

	#(try_end),
	##diplomacy end+

	],"{!}{s11} {s1}.", "minister_grant_fief_complete",
	[
	(store_repeat_object, "$lord_selected"),
	]],
   
   [anyone|plyr, "minister_grant_fief_select_recipient_choice",
   [
   ],"Never mind", "minister_pretalk",
   []],   
   
   [anyone, "minister_grant_fief_complete",
   [
   ## WINDYPLAINS+ ## - Native bugfix to repair fief granting dialog.
   (str_store_party_name, s1, "$fief_selected"),
   (str_store_troop_name, s2, "$lord_selected"),
   ## WINDYPLAINS- ##
   ],"Very well - {s2} shall receive {s1}.", "minister_pretalk",
   [
   (call_script, "script_give_center_to_lord", "$fief_selected", "$lord_selected", 0),
   (str_store_party_name, s1, "$fief_selected"),
   (str_store_troop_name, s2, "$lord_selected"),
   
   (try_begin),
	(faction_slot_eq, "$players_kingdom", slot_faction_political_issue, "$fief_selected"),
	(faction_set_slot, "$players_kingdom", slot_faction_political_issue, -1),
   (try_end),
   
   (call_script, "script_add_log_entry", logent_castle_given_to_lord_by_player, "trp_player", "$fief_selected", "$lord_selected", "$g_encountered_party_faction"),
   ]],   
   
   
   
   
   
   
   [anyone, "minister_indict",
   [], "Grim news, {sire/my lady}. Who do you believe is planning to betray you?", "minister_indict_select",
   []],   
   
   [anyone|plyr|repeat_for_troops, "minister_indict_select",
   [
	(store_repeat_object, ":troop_no"),
	(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
	(store_faction_of_troop, ":faction", ":troop_no"),
##diplomacy start+
(troop_is_hero, ":troop_no"),
(neq, ":troop_no", "trp_player"),
#Prevent problems when the player is co-ruler of a kingdom.
(neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, ":troop_no"),
(neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, ":troop_no"),
##diplomacy end+
	(eq, ":faction", "fac_player_supporters_faction"),
	(str_store_troop_name, s11, ":troop_no"),
	], "{s11}", "minister_indict_confirm",
	[
	(store_repeat_object, "$lord_selected"),
	]],

	[anyone|plyr, "minister_indict_select",
	[], "Never mind.", "minister_pretalk",
	[]],


	[anyone, "minister_indict_confirm",
	[
	(str_store_troop_name, s4, "$lord_selected"),
	##diplomacy start+
	##OLD:
	#(troop_get_type, reg4, "$lord_selected"),
	##NEW:
	(assign, reg4, 0),
	(try_begin),
		(call_script, "script_cf_dplmc_troop_is_female", "$lord_selected"),
		(assign, reg4, 1),
	(try_end),
	##diplomacy end+
	], "Think carefully on this, {sire/my lady}. If you indict {s4} for treason unjustly, you may find that others become nervous about serving you. On the other hand, if you truly believe that {reg4?she:he} is about to betray you, then perhaps it is best to move first, to secure control of {reg4?her:his} fortresses.", "minister_indict_confirm_answer",
	[]],

  [anyone|plyr, "minister_indict_confirm_answer",[], "I have thought long enough. Issue the indictment!", "minister_indict_conclude",[]],
  
  [anyone|plyr, "minister_indict_confirm_answer",[], "Perhaps I should wait a little while longer..", "minister_pretalk",[]],
   
   [anyone, "minister_indict_conclude",
   [], "It has been sent, {sire/my lady}.", "minister_pretalk",
   [
   (call_script, "script_indict_lord_for_treason", "$lord_selected", "fac_player_supporters_faction"),
   ]],      	


	 
	 
	 
	 
	 
	 
	 

   [anyone|plyr|repeat_for_troops, "center_captured_lord_advice",
   [
	(store_repeat_object, ":troop_no"),
	(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
	(neq, "$g_talk_troop", ":troop_no"),
	(neq, "trp_player", ":troop_no"),
	(store_troop_faction, ":faction_no", ":troop_no"),
	##diplomacy start+ Handle player is co-ruler of kingdom
	(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":faction_no"),
	(this_or_next|ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
	##diplomacy end+
	(eq, ":faction_no", "fac_player_supporters_faction"),
	(str_store_troop_name, s11, ":troop_no"),
	(call_script, "script_print_troop_owned_centers_in_numbers_to_s0", ":troop_no"),

	(try_begin),
		##diplomacy start+ fixed bug that was preventing "promised fief" from appearing
		(troop_slot_eq, ":troop_no", slot_lord_recruitment_argument, argument_benefit),#changed "$g_talk_troop" to ":troop_no"
		##diplomacy end+
		(str_store_string, s12, "str__promised_fief"),
	(else_try),
		(str_clear, s12),
	(try_end),

	(try_begin),
		(eq, reg0, 0),
		##diplomacy start+ write to s0 instead of s1
		(str_store_string, s0, "str_no_fiefss12"),
		##diplomacy end_
	(else_try),
		##diplomacy start+ write to s0 instead of s1
		(str_store_string, s0, "str_fiefs_s0s12"),
		##diplomacy end+
	(try_end),
	##diplomacy start+ add relation to list of lords
	#add relation string
	(str_store_string_reg, s12, s63),#save s63, clobbering s12 (perhaps overwritten earlier)
	(call_script, "script_troop_get_player_relation", ":troop_no"),
	(call_script, "script_describe_relation_to_s63", reg0),
	(str_store_string_reg, s1, s63),#clobber s1
	(str_store_string_reg, s63, s12),#revert s63
	(str_store_string, s1, "str_dplmc_s0_comma_s1"),#write to s1
	##diplomacy end+
	],
	"{s11}. {s1}", "center_captured_lord_advice_2",
	[
	(store_repeat_object, "$temp"),
	]],


  [anyone|plyr, "center_captured_lord_advice",
   [
     (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", "trp_player"),
     (str_store_party_name, s1, "$g_center_taken_by_player_faction"),

	 (try_begin),
		(is_between, "$g_talk_troop", pretenders_begin, pretenders_end),
		(str_store_string, s12, "str_please_s65_"),
	 (else_try),	
		(str_clear, s12),
	 (try_end),	
	 ],
   "{s12}I want to have {s1} for myself. (fiefs: {s0})", "center_captured_lord_advice_2",
   [
     (assign, "$temp", "trp_player"),
     ]],

  [anyone|plyr, "center_captured_lord_advice",
   [
     (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", "$g_talk_troop"),
     (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
	 (is_between, "$g_talk_troop", pretenders_begin, pretenders_end),
     ],
   "{s66}, you should have {s1} for yourself. (fiefs: {s0})", "center_captured_lord_advice_2",
   [
     (assign, "$temp", "$g_talk_troop"),
     ]],

	 
  [anyone, "center_captured_lord_advice_2",
   [
     (eq, "$g_talk_troop", "$g_player_minister"),
     ],
   "As you wish, {sire/my lady}. {reg6?I:{reg7?You:{s11}}} will be the new {reg3?lady:lord} of {s1}.", "minister_issues",
   [
     (assign, ":new_owner", "$temp"),
	 
     (call_script, "script_give_center_to_lord", "$g_center_taken_by_player_faction", ":new_owner", 0),
	 
	 (try_begin),
		(faction_slot_eq, "$players_kingdom", slot_faction_political_issue, "$g_center_taken_by_player_faction"),
		(faction_set_slot, "$players_kingdom", slot_faction_political_issue, -1),
	 (try_end),	 
	 
     (try_begin),
       (neq, ":new_owner", "trp_player"),
       (try_for_range, ":unused", 0, 4),
         (call_script, "script_cf_reinforce_party", "$g_center_taken_by_player_faction"),
       (try_end),
     (try_end),

	(assign, reg6, 0),
	(assign, reg7, 0),
	(try_begin),
		(eq, ":new_owner", "$g_talk_troop"),
		(assign, reg6, 1),
	(else_try),
		(eq, ":new_owner", "trp_player"),
		(assign, reg7, 1),
	(else_try),
		(str_store_troop_name, s11, ":new_owner"),
	(try_end),
	(str_store_party_name, s1, "$g_center_taken_by_player_faction"),
	##diplomacy start+
	##OLD:
	#(troop_get_type, reg3, ":new_owner"),
	##NEW:
	(assign, reg3, 0),
	(try_begin),
		(call_script, "script_cf_dplmc_troop_is_female", ":new_owner"),
		(assign, reg3, 1),
	(try_end),
	##diplomacy end+
	(assign, "$g_center_taken_by_player_faction", -1),
	]],
	 
	 
	 
  [anyone, "center_captured_lord_advice_2",
   [
     ],
   "Hmmm. All right, {playername}. I value your counsel highly. {reg6?I:{reg7?You:{s11}}} will be the new {reg3?lady:lord} of {s1}.", "close_window",
   [
     (assign, ":new_owner", "$temp"),
	 
	 (troop_set_slot, ":new_owner", slot_lord_recruitment_argument, 0),
	 
     (call_script, "script_give_center_to_lord", "$g_center_taken_by_player_faction", ":new_owner", 0),
	 (try_begin),
		(faction_slot_eq, "$players_kingdom", slot_faction_political_issue, "$g_center_taken_by_player_faction"),
		(faction_set_slot, "$players_kingdom", slot_faction_political_issue, -1),
	 (try_end),	 
   
     (try_begin),
       (neq, ":new_owner", "trp_player"),
       (try_for_range, ":unused", 0, 4),
         (call_script, "script_cf_reinforce_party", "$g_center_taken_by_player_faction"),
       (try_end),
     (try_end),

     (assign, reg6, 0),
     (assign, reg7, 0),
     (try_begin),
       (eq, ":new_owner", "$g_talk_troop"),
       (assign, reg6, 1),
     (else_try),
       (eq, ":new_owner", "trp_player"),
       (assign, reg7, 1),
     (else_try),
       (str_store_troop_name, s11, ":new_owner"),
     (try_end),
	(str_store_party_name, s1, "$g_center_taken_by_player_faction"),
	##diplomacy start+
	##OLD:
	#(troop_get_type, reg3, ":new_owner"),
	##NEW:
	(assign, reg3, 0),
	(try_begin),
		(call_script, "script_cf_dplmc_troop_is_female", ":new_owner"),
		(assign, reg3, 1),
	(try_end),
	##diplomacy end+
	(assign, "$g_center_taken_by_player_faction", -1),
	]],



  [anyone, "event_triggered", [
                     (eq, "$g_infinite_camping", 0),
                     (store_conversation_troop, "$map_talk_troop"),
					 (is_between, "$map_talk_troop", companions_begin, companions_end),
                     (eq, "$map_talk_troop", "$npc_is_quitting"), 
                     (troop_get_slot, ":honorific", "$map_talk_troop", slot_troop_honorific), 
                     (str_store_string, 5, ":honorific")],
   "Excuse me {s5} -- there is something I need to tell you.", "companion_quitting", [
                    (assign, "$npc_is_quitting", 0),
                    (assign, "$player_can_persuade_npc", 1),
                    (assign, "$player_can_refuse_npc_quitting", 1),
       ]],

	### This is also where the dialogue jumps if the player initiates quitting dialogue and the companion has low morale
	##diplomacy start+
	#Hijack this for lorded companions who temporarily rejoined your party, and the like.
	[anyone, "companion_quitting", [
				   (store_conversation_troop, "$map_talk_troop"),
				   (assign, ":has_fief", 0),
				   (try_for_range_backwards, ":center_no", centers_begin, centers_end),
					  (party_slot_eq, ":center_no", slot_town_lord, "$map_talk_troop"),
					  (assign, ":has_fief", 1),
				   (try_end),
				   (this_or_next|eq, ":has_fief", 1),
				   (this_or_next|is_between, "$map_talk_troop", lords_begin, lords_end),
				   (this_or_next|is_between, "$map_talk_troop", pretenders_begin, pretenders_end),
				   (this_or_next|is_between, "$map_talk_troop", kings_begin, kings_end),
				   (this_or_next|troop_slot_eq, "$map_talk_troop", slot_troop_occupation, slto_kingdom_hero),
				   (this_or_next|troop_slot_eq, "$map_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
				   (troop_slot_eq, "$map_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_lord_rejoined),
				   ],
	"It has been good travelling with you, but I must return to my own affairs.", "dplmc_companion_quitting_lord_1",
		[]],

	[anyone|plyr, "dplmc_companion_quitting_lord_1", [
	], "Farewell, then.", "dplmc_companion_quitting_lord_2", [
		]],
		
	[anyone|plyr, "dplmc_companion_quitting_lord_1", [
	(eq, "$player_can_persuade_npc", 1),
	], "Perhaps I can persuade you to change your mind.", "dplmc_companion_quitting_lord_persuasion", [
	(assign, "$player_can_persuade_npc", 0),
		]],
		
	[anyone, "dplmc_companion_quitting_lord_persuasion", [
			  (store_random_in_range, ":random", -2, 13),
			  (store_skill_level, ":persuasion", "skl_persuasion", "trp_player"),
			  (le, ":random", ":persuasion"),
				   ],
	"Hm.  I suppose I can afford to put it off a bit longer.", "close_window",
	[
			  (troop_get_slot, ":morality_penalties", "$map_talk_troop", slot_troop_morality_penalties),
			  (val_div, ":morality_penalties", 2),
			  (troop_set_slot, "$map_talk_troop", slot_troop_morality_penalties, ":morality_penalties"),

			  (troop_get_slot, ":personalityclash_penalties", "$map_talk_troop", slot_troop_personalityclash_penalties),
			  (val_div, ":personalityclash_penalties", 2),
			  (troop_set_slot, "$map_talk_troop", slot_troop_personalityclash_penalties, ":personalityclash_penalties"),
	 ]],
	 
	 [anyone, "dplmc_companion_quitting_lord_persuasion", [
				   ],
	"I'm sorry, but I can't put it off any longer.", "dplmc_companion_quitting_lord_1",
	[
	 ]],
	 
	 [anyone|plyr, "dplmc_companion_quitting_lord_2", [
	], "Farewell, then.", "lord_leave", [#Jump to standard lord farewell dialog
		(try_begin),
			(this_or_next|troop_slot_eq, "$map_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
			(this_or_next|troop_slot_eq, "$map_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_lord_rejoined),
			#(troop_slot_eq, "$map_talk_troop", slot_troop_occupation, slto_player_companion),
			(troop_set_slot, "$map_talk_troop", slot_troop_occupation, slto_kingdom_hero),
		(try_end),
		(remove_member_from_party, "$map_talk_troop", "p_main_party"),
		
		(troop_set_slot, "$map_talk_troop", slot_troop_personalityclash_penalties, 0),
		(troop_set_slot, "$map_talk_troop", slot_troop_morality_penalties, 0),
	]],

	##diplomacy end+	   
	   
	   
### This is also where the dialogue jumps if the player initiates quitting dialogue and the companion has low morale
  [anyone, "companion_quitting", [
                     (store_conversation_troop, "$map_talk_troop"),
                     (troop_get_slot, ":speech", "$map_talk_troop", slot_troop_retirement_speech), 
                     (str_store_string, 5, ":speech")
                     ],
   "{s5}", "companion_quitting_2", [
       ]],
	   
## The companion explains his/her reasons for quitting
  [anyone, "companion_quitting_2", [
                    (call_script, "script_npc_morale", "$map_talk_troop"),
                     ],
   "To tell you the truth, {s21}", "companion_quitting_response", [
       ]],

  [anyone|plyr, "companion_quitting_response", [
      ], "Very well. You be off, then.", "companion_quitting_yes", [
          ]],

	##diplomacy start+  Alter the "persuade to stay" conversation, and redirect it.
	[anyone|plyr, "companion_quitting_response", [
			  (eq, "$player_can_persuade_npc", 1),
	#], "Perhaps I can persuade you to change your mind.", "companion_quitting_persuasion", [#<- dplmc replace
	], "Perhaps I can persuade you to change your mind.", "dplmc_companion_quitting_persuasion_start", [#<- dplmc add
	##diplomacy end+
		  (assign, "$player_can_persuade_npc", 0),
		]],
		
	##diplomacy start+
	[anyone, "dplmc_companion_quitting_persuasion_start", [
		#First line, respond in slightly-more-formal diction.
		(troop_get_slot, ":personality", "$map_talk_troop", slot_lord_reputation_type),
		(assign, ":formal_response", 0),#accept or reject
		(try_begin),
			#Nobles and well-educated commoners answer this way.
			(this_or_next|ge, ":personality", lrep_benefactor),#includes lrep_benefactor and all kingdom lady personalities
				(is_between, ":personality", lrep_none, lrep_roguish),
			#Exclude quarrelsome and debauched.  They are not inclined to mince words when they're discontent.
			(neq, ":personality", lrep_quarrelsome),
			(neq, ":personality", lrep_debauched),
			(assign, ":formal_response", 1),
		(else_try),
			#"Well-educated commoners" includes some custodians but not others.
			#(For example, in Native compare Katrin with Artimenner.)
			(eq, ":personality", lrep_custodian),
			
			#Checking intelligence by itself isn't enough, since there isn't all
			#that much variation at the starting levels, and many companions
			#will have their intelligence raised for party skills regardless of
			#their background.		
			(store_attribute_level, ":intelligence", "$map_talk_troop", ca_intelligence),
			(ge, ":intelligence", 12),
			
			#As the lesser of several evils, I'll add a secondary check for Engineer,
			#which is obviously arbitrary somewhat targeted but may catch Artimenner-like
			#characters in other mods.
			(store_skill_level, ":engineer", "$map_talk_troop", "skl_engineer"),
			(ge, ":engineer", 4),
			(assign, ":formal_response", 1),
		(try_end),
		(neq, ":formal_response", 0),
	], "Very well, I shall hear you out.", "dplmc_companion_quitting_persuasion_1", [
	]],

	[anyone, "dplmc_companion_quitting_persuasion_start", [#Less-formal response
	], "I'm listening.", "dplmc_companion_quitting_persuasion_1", [
	]],

	#This goes to the standard persuasion dialog.	
	[anyone|plyr, "dplmc_companion_quitting_persuasion_1", [
	], "We've had some good times.  Things might not be going to your liking now, but stay with me a while longer and the situation will turn around.", "companion_quitting_persuasion", [
	]],
		
	#This removes money if successful.
	[anyone|plyr, "dplmc_companion_quitting_persuasion_1", [
		#The same calculation as ransoming a companion from a ransom broker.
		#(From a game balance perspective, the effect is similar: you are
		#paying to avoid losing access to your companion.)
		(store_character_level, ":companion_level", "$map_talk_troop"),
		(store_add, ":cost", ":companion_level", 20),
		(val_mul, ":cost", ":companion_level"),
		(val_mul, ":cost", 5), #Level 1: 110, level 40: 12,000
		
		#Since there's no random check here, instead the persuasion skill
		#is used to reduce the price.
		(store_skill_level, ":persuasion", "skl_persuasion", "trp_player"),
		
		#Because this pertains to the handling of subordinates, in my
		#opinion skl_leadership is also directly relevant (since this is
		#how it works with non-hero troops, where your leadership
		#raises their morale and makes them less likely to desert).
		(store_skill_level, reg0, "skl_leadership", "trp_player"),
		(val_max, ":persuasion", reg0),
		
		(val_clamp, ":persuasion", 0, 19),
		(store_sub, reg0, 20, ":persuasion"),
		(val_mul, ":cost", reg0),
		(val_div, ":cost", 20),
		
		#Check if the player can afford it.
		(store_troop_gold, ":treasury", "trp_household_possessions"),
		(store_troop_gold, ":purse", "trp_player"),
		(store_add, ":available_funds", ":treasury", ":purse"),
		(ge, ":available_funds", ":cost"),
		
		(assign, "$temp", ":cost"),
		(assign, reg0, "$temp"), # Diplomacy bugfix - Windyplains - Cost wasn't being displayed because it wasn't registered.
	], "Would {reg0} denars convince you to remain a while longer?", "dplmc_companion_quitting_persuasion_bribe", [
		  (assign, "$player_can_persuade_npc", 0),
		]],

	#Return to previous
	[anyone|plyr, "dplmc_companion_quitting_persuasion_1", [
	], "Actually, nevermind.  I meant to say something else.", "companion_quitting_response", [
		(assign, "$player_can_persuade_npc", 1),#revert
	]],

	[anyone, "dplmc_companion_quitting_persuasion_bribe", [
		#Player bribes companion to remain
				   ],
	"Hm. When you put it like that, I suppose I can stay a while longer, see if things improve.", "close_window",
	[
			  (assign, reg0, "$temp"),#cost to pay
			  #Remove the gold from the player
			  (val_max, reg0, 0),
			  (store_troop_gold, ":funds", "trp_player"),
			  (val_min, ":funds", reg0),
			  (val_sub, reg0, ":funds"),
			  (troop_remove_gold, "trp_player", ":funds"),
			  
			  #Remove any remaining gold from the treasury
			  (store_troop_gold, ":funds", "trp_household_possessions"),
			  (val_min, ":funds", reg0),
			  (val_sub, reg0, ":funds"),
			  (call_script, "script_dplmc_withdraw_from_treasury", ":funds"),

			  #Reduce penalties per a successful persuasion attempt
			  (troop_get_slot, ":morality_penalties", "$map_talk_troop", slot_troop_morality_penalties),
			  (val_div, ":morality_penalties", 2),
			  (troop_set_slot, "$map_talk_troop", slot_troop_morality_penalties, ":morality_penalties"),

			  (troop_get_slot, ":personalityclash_penalties", "$map_talk_troop", slot_troop_personalityclash_penalties),
			  (val_div, ":personalityclash_penalties", 2),
			  (troop_set_slot, "$map_talk_troop", slot_troop_personalityclash_penalties, ":personalityclash_penalties"),
	 ]],
	##diplomacy end+

	[anyone, "companion_quitting_persuasion", [
			  (store_random_in_range, ":random", -2, 13),
			  (store_skill_level, ":persuasion", "skl_persuasion", "trp_player"),
			  ##diplomacy start+
			  #Because this pertains to the handling of subordinates, in my
			  #opinion skl_leadership is also directly relevant (especially since
			  #this is how it works with non-hero troops, where your leadership
			  #raises their morale and makes them less likely to desert).	
			  (store_skill_level, reg0, "skl_leadership", "trp_player"),
			  (val_max, ":persuasion", reg0),
			  ##diplomacy end+

			  (le, ":random", ":persuasion"),
				   ],
   "Hm. When you put it like that, I suppose I can stay a while longer, see if things improve.", "close_window",
   [
                (troop_get_slot, ":morality_penalties", "$map_talk_troop", slot_troop_morality_penalties),
                (val_div, ":morality_penalties", 2),
                (troop_set_slot, "$map_talk_troop", slot_troop_morality_penalties, ":morality_penalties"),

                (troop_get_slot, ":personalityclash_penalties", "$map_talk_troop", slot_troop_personalityclash_penalties),
                (val_div, ":personalityclash_penalties", 2),
                (troop_set_slot, "$map_talk_troop", slot_troop_personalityclash_penalties, ":personalityclash_penalties"),
       ]],

  [anyone, "companion_quitting_persuasion", [
                     ],
   "I'm sorry, but I don't see your point. I am leaving whether you like it or not.", "companion_quitting_response",
   [
       ]],

	##diplomacy start+  ##FLORIS OVERRIDE
	#Enable refusing to allow party members to quit in cheat mode.
	#
	#OLD VERSION:
	[anyone|plyr, "companion_quitting_response", [
	     (eq, "$disable_npc_complaints", 1),  #Floris - enable this option, based on the Mod Option re complaints, not cheat as diplo had it below
		 #(eq, 1, 0),
	     (eq, "$player_can_refuse_npc_quitting", 1),
	], "We hang deserters in this company.", "companion_quitting_no", [
	   ]],
	#
	# [anyone|plyr, "companion_quitting_response", [
		  # (ge, "$cheat_mode", 1),#only enable in cheat mode
		  # (eq, "$player_can_refuse_npc_quitting", 1),
	# ], "CHEAT -- We hang deserters in this company.", "companion_quitting_no", [
		# ]],
		
	#Add a response with a slightly different flavor for less mild personalities.
	[anyone, "companion_quitting_no", [
		(troop_get_slot, ":talk_troop_personality", "$g_talk_troop", slot_lord_reputation_type),
		(this_or_next|eq, ":talk_troop_personality", lrep_martial),
		(this_or_next|eq, ":talk_troop_personality", lrep_selfrighteous),
			(eq, ":talk_troop_personality", lrep_quarrelsome),
	],
	"I believe I misheard you.  You certainly could not have been threatening me.", "companion_quitting_no_confirm", [
	 ]],
	##diplomacy end+

  [anyone, "companion_quitting_no", [],
   "Oh... Right... Do you mean that?", "companion_quitting_no_confirm", [
       ]],

	[anyone|plyr, "companion_quitting_no_confirm", [],
	"Absolutely. You either leave this company by my command, or are carried out on your shield.", "companion_quitting_no_confirmed", [
	##diplomacy start+
	#I imagine that most companions wouldn't be too happy about being threatened
	#with death.
	(call_script, "script_dplmc_get_troop_morality_value", "$g_talk_troop", tmt_egalitarian),
	(try_begin),
		(lt, reg0, 0),
		#I am adding an exception.  If you know who this applies to in Native, you
		#might agree with this character interpretation.  My reasons for adding this
		#are:
		# (1) I like it when companions react to circumstances differently.
		# (2) I find this possible scenario funny.
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 1),
	(else_try),
		#This is the default case.  A larger relation drop might be more
		#appropriate.  I started off with -5.
		(call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -5),
	(try_end),

	#It might be interesting to develop this branch further (for example, being
	#challenged to single combat) but I'm not sure something like this would have
	#wide enough appeal to justify it.

	##Approval/disapproval from other NPCs
	(try_for_range, ":npc", companions_begin, companions_end),
	   (neq, ":npc", "$g_talk_troop"),
	   (main_party_has_troop, ":npc"),
	   (call_script, "script_dplmc_get_troop_morality_value", ":npc", tmt_egalitarian),
	   (try_begin),
		  (lt, reg0, 0),
		  (call_script, "script_change_player_relation_with_troop", ":npc", 1),
	   (else_try),
		  (gt, reg0, 0),
		  (call_script, "script_change_player_relation_with_troop", ":npc", -1),
	   (try_end),
	(try_end),
	##diplomacy end+
	 ]],

  [anyone|plyr, "companion_quitting_no_confirm", [],
   "No, actually I don't mean that. You are free to leave.", "companion_quitting_yes", [
       ]],

  [anyone, "companion_quitting_yes", [
                     ],
   "Then this is goodbye. Perhaps I'll see you around, {playername}.", "close_window", [
          (troop_set_slot, "$map_talk_troop", slot_troop_playerparty_history, pp_history_quit), 
          (call_script, "script_retire_companion", "$map_talk_troop", 100),
       ]],

  [anyone, "companion_quitting_no_confirmed", [
      ],
   "Hm. I suppose I'm staying, then.", "close_window", [
       ]],


#Morality objections
  [anyone, "event_triggered", [
                     (store_conversation_troop, "$map_talk_troop"),
					 (is_between, "$map_talk_troop", companions_begin, companions_end),	
					 
                     (eq, "$map_talk_troop", "$npc_with_grievance"), 
                     (eq, "$npc_map_talk_context", slot_troop_morality_state), 

					 
                     (try_begin),
                         (eq, "$npc_grievance_slot", slot_troop_morality_state),
                         (troop_get_slot, ":speech", "$map_talk_troop", slot_troop_morality_speech),
                     (else_try),
                         (troop_get_slot, ":speech", "$map_talk_troop", slot_troop_2ary_morality_speech),
                     (try_end),
                     (str_store_string, 21, "$npc_grievance_string"),
                     (str_store_string, 5, ":speech"),
                     ],
   "{s5}", "companion_objection_response", [
                    (assign, "$npc_with_grievance", 0),
       ]],



  [anyone|plyr, "companion_objection_response", [
                    (eq, "$npc_praise_not_complaint", 1),
      ], "Thanks, I appreciate your support.", "close_window", [
                    (troop_set_slot, "$map_talk_troop", "$npc_grievance_slot", tms_acknowledged),
          ]],

  [anyone|plyr, "companion_objection_response", [
                    (eq, "$npc_praise_not_complaint", 0),
      ], "Hopefully it won't happen again.", "close_window", [
                    (troop_set_slot, "$map_talk_troop", "$npc_grievance_slot", tms_acknowledged),
          ]],

  [anyone|plyr, "companion_objection_response", [
                    (eq, "$npc_praise_not_complaint", 0),
      ],  "Your objection is noted. Now fall back in line.", "close_window", [
                    (troop_set_slot, "$map_talk_troop", "$npc_grievance_slot", tms_dismissed),
                    (troop_get_slot, ":grievance", "$map_talk_troop", slot_troop_morality_penalties),
                    (val_add, ":grievance", 10),
                    (troop_set_slot, "$map_talk_troop", slot_troop_morality_penalties, ":grievance"),
          ]],


##  [anyone|plyr, "companion_objection_response", [
##      ],  "I prefer my followers to keep their opinions to themselves.", "close_window", [
##                    (troop_set_slot, "$map_talk_troop", "$npc_grievance_slot", tms_dismissed),
##                    (troop_get_slot, ":grievance", "$map_talk_troop", slot_troop_morality_penalties),
##                    (val_add, ":grievance", 10),
##                    (troop_set_slot, "$map_talk_troop", slot_troop_morality_penalties, ":grievance"),
##                    (assign, "$disable_npc_complaints", 1),
##          ]],



# Personality clash 2 objections
  [anyone, "event_triggered", [
                     (store_conversation_troop, "$map_talk_troop"),
					 (is_between, "$map_talk_troop", companions_begin, companions_end),
					 
                     (eq, "$map_talk_troop", "$npc_with_personality_clash_2"), 
                     (eq, "$npc_map_talk_context", slot_troop_personalityclash2_state), 

                     (troop_get_slot, ":speech", "$map_talk_troop", slot_troop_personalityclash2_speech),
                     (troop_get_slot, ":object", "$map_talk_troop", slot_troop_personalityclash2_object),
                     (str_store_troop_name, 11, ":object"),
                     (str_store_string, 5, ":speech"),
                     ],
   "{s5}", "companion_personalityclash2_b", [
                    (assign, "$npc_with_personality_clash_2", 0),
                    (troop_get_slot, ":grievance", "$map_talk_troop", slot_troop_personalityclash_penalties),
                    (val_add, ":grievance", 5),
                    (troop_set_slot, "$map_talk_troop", slot_troop_personalityclash_penalties, ":grievance"),
					
                    (troop_get_slot, ":object", "$map_talk_troop", slot_troop_personalityclash2_object),
					(call_script, "script_troop_change_relation_with_troop", "$map_talk_troop", ":object", -15),
       ]],

  [anyone, "companion_personalityclash2_b", [
      ],  "{s5}", "companion_personalityclash2_response", [
                     (troop_get_slot, ":speech", "$map_talk_troop", slot_troop_personalityclash2_speech_b),
                     (troop_get_slot, ":object", "$map_talk_troop", slot_troop_personalityclash2_object),
                     (str_store_troop_name, 11, ":object"),
                     (str_store_string, 5, ":speech"),
          ]],



  [anyone|plyr, "companion_personalityclash2_response", [
      (troop_get_slot, ":object", "$map_talk_troop", slot_troop_personalityclash2_object),
		(str_store_troop_name, s11, ":object"),
		##diplomacy start+
		##OLD:
		#(troop_get_type, reg11, ":object"),
		##NEW:
		(assign, reg11, 0),
		(try_begin),
			(call_script, "script_cf_dplmc_troop_is_female", ":object"),
			(assign, reg11, 1),
		(try_end),
		##diplomacy end+
		],  "{s11} is a valuable member of this company. I don't want you picking any more fights with {reg11?her:him}.", "close_window", [
					  (troop_set_slot, "$map_talk_troop", slot_troop_personalityclash2_state, pclash_penalty_to_self),
			]],

		[anyone|plyr, "companion_personalityclash2_response", [
		(troop_get_slot, ":object", "$map_talk_troop", slot_troop_personalityclash2_object),
		(str_store_troop_name, s11, ":object"),
		##diplomacy start+
		##OLD:
		#(troop_get_type, reg11, ":object"),
		##NEW:
		(assign, reg11, 0),
		(try_begin),
			(call_script, "script_cf_dplmc_troop_is_female", ":object"),
			(assign, reg11, 1),
		(try_end),
		##diplomacy end+
		],  "Tell {s11} you have my support in this, and {reg11?she:he} should hold {reg11?her:his} tongue.", "close_window", [
					  (troop_set_slot, "$map_talk_troop", slot_troop_personalityclash2_state, pclash_penalty_to_other),
			]],
  
  [anyone|plyr, "companion_personalityclash2_response", [
      ],  "I don't have time for your petty dispute. Do not bother me with this again.", "close_window", [
                    (troop_set_slot, "$map_talk_troop", slot_troop_personalityclash2_state, pclash_penalty_to_both),
          ]],

  
##  [anyone|plyr, "companion_personalityclash2_response", [
##      ],  "Your grievance is noted. Now fall back in line.", "close_window", [
##                    (troop_set_slot, "$map_talk_troop", slot_troop_personalityclash2_state, 1),
##          ]],

##  [anyone|plyr, "companion_personalityclash2_response", [
##      ],  "I prefer my followers to keep their opinions to themselves.", "close_window", [
##                    (troop_set_slot, "$map_talk_troop", slot_troop_personalityclash2_state, 1),
##                    (assign, "$disable_npc_complaints", 1),
##          ]],




# Personality clash objections

  [anyone, "event_triggered", [
                     (store_conversation_troop, "$map_talk_troop"),
					 (is_between, "$map_talk_troop", companions_begin, companions_end),
					 
                     (eq, "$map_talk_troop", "$npc_with_personality_clash"),
                     (eq, "$npc_map_talk_context", slot_troop_personalityclash_state), 

                     (troop_get_slot, ":speech", "$map_talk_troop", slot_troop_personalityclash_speech),
                     (troop_get_slot, ":object", "$map_talk_troop", slot_troop_personalityclash_object),
                     (str_store_troop_name, 11, ":object"),
                     (str_store_string, 5, ":speech"),
                     ],
   "{s5}", "companion_personalityclash_b", [
                    (assign, "$npc_with_personality_clash", 0),
                    (troop_get_slot, ":grievance", "$map_talk_troop", slot_troop_personalityclash_penalties),
                    (val_add, ":grievance", 5),
                    (troop_set_slot, "$map_talk_troop", slot_troop_personalityclash_penalties, ":grievance"),

                    (troop_get_slot, ":object", "$map_talk_troop", slot_troop_personalityclash_object),
					(call_script, "script_troop_change_relation_with_troop", "$map_talk_troop", ":object", -15),
				
       ]],

  [anyone, "companion_personalityclash_b", [
      ],  "{s5}", "companion_personalityclash_response", [
                     (troop_get_slot, ":speech", "$map_talk_troop", slot_troop_personalityclash_speech_b),
                     (troop_get_slot, ":object", "$map_talk_troop", slot_troop_personalityclash_object),
                     (str_store_troop_name, 11, ":object"),
                     (str_store_string, 5, ":speech"),
          ]],

	[anyone|plyr, "companion_personalityclash_response", [
	(troop_get_slot, ":object", "$map_talk_troop", slot_troop_personalityclash_object),
	(str_store_troop_name, s11, ":object"),
	##diplomacy start+
	##OLD:
	#(troop_get_type, reg11, ":object"),
	##NEW:
	(assign, reg11, 0),
	(try_begin),
		(call_script, "script_cf_dplmc_troop_is_female", ":object"),
		(assign, reg11, 1),
	(try_end),
	##diplomacy end+
	],  "{s11} is a capable member of this company. I don't want you picking any more fights with {reg11?her:him}.", "close_window", [
				  (troop_set_slot, "$map_talk_troop", slot_troop_personalityclash_state, pclash_penalty_to_self),
		]],

	[anyone|plyr, "companion_personalityclash_response", [
	(troop_get_slot, ":object", "$map_talk_troop", slot_troop_personalityclash_object),
	(str_store_troop_name, s11, ":object"),
	##diplomacy start+
	##OLD:
	#(troop_get_type, reg11, ":object"),
	##NEW:
	(assign, reg11, 0),
	(try_begin),
		(call_script, "script_cf_dplmc_troop_is_female", ":object"),
		(assign, reg11, 1),
	(try_end),
	##diplomacy end+
	],  "Tell {s11} you have my support in this, and {reg11?she:he} should hold {reg11?her:his} tongue.", "close_window", [
				  (troop_set_slot, "$map_talk_troop", slot_troop_personalityclash_state, pclash_penalty_to_other),
		]],  
		
  [anyone|plyr, "companion_personalityclash_response", [
      ],  "I don't have time for your petty dispute. Do not bother me with this again.", "close_window", [
                    (troop_set_slot, "$map_talk_troop", slot_troop_personalityclash_state, pclash_penalty_to_both),
          ]],


##  [anyone|plyr, "companion_personalityclash_response", [
##      ],  "Your grievance is noted. Now fall back in line.", "close_window", [
##                    (troop_set_slot, "$map_talk_troop", slot_troop_personalityclash_state, 1),
##          ]],

##  [anyone|plyr, "companion_personalityclash_response", [
##      ],  "I prefer my followers to keep their opinions to themselves.", "close_window", [
##                    (troop_set_slot, "$map_talk_troop", slot_troop_personalityclash_state, 1),
##                    (assign, "$disable_npc_complaints", 1),
##          ]],



# Personality match

  [anyone, "event_triggered", [
                     (eq, "$npc_map_talk_context", slot_troop_personalitymatch_state), 
                     (store_conversation_troop, "$map_talk_troop"),
					 (is_between, "$map_talk_troop", companions_begin, companions_end),
					 
                     (eq, "$map_talk_troop", "$npc_with_personality_match"),

                     (troop_get_slot, ":speech", "$map_talk_troop", slot_troop_personalitymatch_speech),
                     (troop_get_slot, ":object", "$map_talk_troop", slot_troop_personalitymatch_object),
                     (str_store_troop_name, 11, ":object"),
                     (str_store_string, 5, ":speech"),
					 
                     ],
   "{s5}", "companion_personalitymatch_b", [
                    (assign, "$npc_with_personality_match", 0),
                    (troop_get_slot, ":object", "$map_talk_troop", slot_troop_personalitymatch_object),
					(call_script, "script_troop_change_relation_with_troop", "$map_talk_troop", ":object", 15),					 
					
       ]],

  [anyone, "companion_personalitymatch_b", [
                    (troop_get_slot, ":speech", "$map_talk_troop", slot_troop_personalitymatch_speech_b),
                    (troop_get_slot, ":object", "$map_talk_troop", slot_troop_personalitymatch_object),
                    (str_store_troop_name, 11, ":object"),
                    (str_store_string, 5, ":speech"),
					 
                     ],
   "{s5}", "companion_personalitymatch_response", [
       ]],


  [anyone|plyr, "companion_personalitymatch_response", [
      ],  "Very good.", "close_window", [
                    (troop_set_slot, "$map_talk_troop", slot_troop_personalitymatch_state, 1),

					]],

					
					
##  [anyone|plyr, "companion_personalitymatch_response", [
##      ],  "I prefer my followers to keep their opinions to themselves.", "close_window", [
##                    (troop_set_slot, "$map_talk_troop", slot_troop_personalitymatch_state, 1),
##                    (assign, "$disable_npc_complaints", 1),
##          ]],

  [anyone, "event_triggered", [
                     (eq, "$npc_map_talk_context", slot_troop_woman_to_woman_string), 
                     (store_conversation_troop, "$map_talk_troop"),
					 (is_between, "$map_talk_troop", companions_begin, companions_end),					 
					 
		             (store_sub, ":npc_no", "$map_talk_troop", "trp_npc1"),
		             (store_add, ":speech", "str_npc1_woman_to_woman", ":npc_no"),
#                     (troop_get_slot, ":speech", "$map_talk_troop", slot_troop_woman_to_woman_string),
                     (str_store_string, s5, ":speech"),
                     ],
   "{s5}", "companion_sisterly_advice", [
                    (troop_set_slot, "$map_talk_troop", slot_troop_woman_to_woman_string, -1),
					(assign, "$npc_with_sisterly_advice", 0),
       ]],

  [anyone|plyr, "companion_sisterly_advice", [
      ],  "Thank you.", "close_window", [
          ]],

  [anyone|plyr, "companion_sisterly_advice", [
      ],  "I would prefer not to discuss such things.", "close_window", [
	  (assign, "$disable_sisterly_advice", 1),
          ]],
	   
	   

  [anyone, "event_triggered", [
                     (eq, "$g_infinite_camping", 0),
                     (eq, "$npc_map_talk_context", slot_troop_home), 
                     (store_conversation_troop, "$map_talk_troop"),
					 (is_between, "$map_talk_troop", companions_begin, companions_end),					 
					 
                     (troop_get_slot, ":speech", "$map_talk_troop", slot_troop_home_intro),
                     (str_store_string, s5, ":speech"),
                     ],
   "{s5}", "companion_home_description", [
                    (troop_set_slot, "$map_talk_troop", slot_troop_home_speech_delivered, 1),
       ]],

  [anyone|plyr, "companion_home_description", [
      ],  "Tell me more.", "companion_home_description_2", [
          ]],

  [anyone|plyr, "companion_home_description", [
      ],  "We don't have time to chat just now.", "close_window", [
          ]],

  [anyone|plyr, "companion_home_description", [
      ],  "I prefer my companions not to bother me with such trivialities.", "close_window", [
                    (assign, "$disable_local_histories", 1),
          ]],


  [anyone, "companion_home_description_2", [
                     (troop_get_slot, ":speech", "$map_talk_troop", slot_troop_home_description),
                     (str_store_string, 5, ":speech"),
      ],  "{s5}", "companion_home_description_3", [
          ]],

  [anyone, "companion_home_description_3", [
                     (troop_get_slot, ":speech", "$map_talk_troop", slot_troop_home_description_2),
                     (str_store_string, 5, ":speech"),
      ],  "{s5}", "close_window", [
          ]],

  [anyone,"event_triggered", [
    (eq, "$talk_context", tc_rebel_thanks),
    (store_conversation_troop, "$g_talk_troop"),
	(is_between, "$g_talk_troop", pretenders_begin, pretenders_end),	
	
    (troop_get_slot, ":old_faction", "$g_talk_troop", slot_troop_original_faction),
    (str_store_faction_name, s3, ":old_faction"),
    (str_store_string, s6, "@{playername}, when we started our long walk, few people had the courage to support me.\
 And fewer still would be willing to put their lives at risk for my cause.\
 But you didn't hesitate for a moment in throwing yourself at my enemies.\
 We have gone through a lot together, and there were times I came close to losing all hope.\
 But with God's help, we prevailed. It is now time for me to leave your company and take what's rightfully mine.\
 From now on, I will carry out the great responsibility of ruling {s3}.\
 There still lie many challanges ahead and I count on your help in overcoming those.\
 And of course, you will always remain as my foremost vassal."),
    ],
   "{s6}", "rebel_thanks_answer",
   [
   
     (unlock_achievement, ACHIEVEMENT_KINGMAKER),
     (call_script, "script_end_quest", "qst_rebel_against_kingdom"),
       ],

     (try_begin),
       (troop_get_type, ":is_female", "trp_player"),
       (eq, ":is_female", 1),

       (troop_get_type, ":is_female", "$g_talk_troop"),
       (eq, ":is_female", 1),	   

       (unlock_achievement, ACHIEVEMENT_GIRL_POWER),
     (try_end),
	 ],

  [anyone|plyr,"rebel_thanks_answer", [], "It was an honour to fight for your cause, {reg65?madame:my lord}.", "rebel_thanks_answer_2", []],
  [anyone|plyr,"rebel_thanks_answer", [], "You will always have my loyal support, {reg65?my lady:sir}.", "rebel_thanks_answer_2", []],

  [anyone,"rebel_thanks_answer_2", [], "I will miss living this life of adventure with you, but my duties await me. So... farewell for now, {playername}.\
 I hope I'll see you again soon.", "close_window", []],


 
  [anyone, "event_triggered", [
                     (store_conversation_troop, "$map_talk_troop"),
					 (is_between, "$map_talk_troop", companions_begin, companions_end),
					 
                     (eq, "$map_talk_troop", "$npc_with_political_grievance"), 
                     (eq, "$npc_map_talk_context", slot_troop_kingsupport_objection_state), 

					 (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
					 (store_add, ":string", "str_npc1_kingsupport_objection", ":npc_no"),
#					 (troop_get_slot, ":string", "$map_talk_troop", slot_troop_kingsupport_objection_string),
                     (str_store_string, 21, ":string"),
                     ],
   "{s21}", "companion_political_grievance_response", [
                    (assign, "$npc_with_political_grievance", 0),
					(troop_set_slot, "$map_talk_troop", slot_troop_kingsupport_objection_state, 2),
					
       ]],

  [anyone|plyr, "companion_political_grievance_response", [
#                    (eq, "$npc_praise_not_complaint", 0),
      ],  "Your opinion is noted.", "close_window", [
                    (troop_get_slot, ":grievance", "$map_talk_troop", slot_troop_morality_penalties),
                    (val_add, ":grievance", 25),
                    (troop_set_slot, "$map_talk_troop", slot_troop_morality_penalties, ":grievance"),
          ]],


		  
  [anyone, "event_triggered", [
                     (store_conversation_troop, "$map_talk_troop"),
					 (is_between, "$map_talk_troop", companions_begin, companions_end),
					 
                     (eq, "$map_talk_troop", "$npc_to_rejoin_party"),
					 (neg|main_party_has_troop, "$map_talk_troop"), ##1.132 extra line
                     (troop_slot_eq, "$map_talk_troop", slot_troop_current_mission, npc_mission_rejoin_when_possible),
					 (troop_slot_eq, "$map_talk_troop", slot_troop_occupation, slto_player_companion),
					 (troop_get_slot, ":string", "$map_talk_troop", slot_troop_honorific),
                     (str_store_string, 21, ":string"),
					 ],
	"Greetings, {s21}. Are you ready for me to rejoin you?"	,			 
					 "companion_rejoin_response",
					[
                    (assign, "$npc_to_rejoin_party", 0),
					]],
					
  [anyone, "event_triggered", [
                     (store_conversation_troop, "$map_talk_troop"),
					 (is_between, "$map_talk_troop", companions_begin, companions_end),					 
					 
                     (eq, "$map_talk_troop", "$npc_to_rejoin_party"), 
#                     (eq, "$npc_map_talk_context", slot_troop_days_on_mission), 
                     (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_kingsupport), 
					 
					 (troop_get_slot, ":string", "$map_talk_troop", slot_troop_honorific),
                     (str_store_string, 21, ":string"),
                     ],
   "Well, {s21}, at last I've found you. I've been out spreading the word about your claim, and am now ready to rejoin the company.", "companion_rejoin_response", [
                    (assign, "$npc_to_rejoin_party", 0),
					(call_script, "script_change_player_right_to_rule", 3),
					(troop_set_slot, "$g_talk_troop", slot_troop_kingsupport_state, 1),
					
					(try_begin),
						(is_between, "$player_right_to_rule", 10, 15),
						(call_script, "script_add_log_entry", logent_player_claims_throne_1, "trp_player", 0, 0, 0),
					(else_try),
						(is_between, "$player_right_to_rule", 20, 25),
						(call_script, "script_add_log_entry", logent_player_claims_throne_2, "trp_player", 0, 0, 0),
					(try_end),
					]],

					
	[anyone, "event_triggered", [
	    (store_conversation_troop, "$map_talk_troop"),
		(is_between, "$map_talk_troop", companions_begin, companions_end),		
	    (eq, "$map_talk_troop", "$npc_to_rejoin_party"), 
	#                     (eq, "$npc_map_talk_context", slot_troop_days_on_mission), 
	    (troop_slot_eq, "$map_talk_troop", slot_troop_current_mission, npc_mission_gather_intel), 
						 
		(troop_get_slot, ":string", "$map_talk_troop", slot_troop_honorific),
	    (str_store_string, 21, ":string"),
		
		(troop_get_slot, ":town_with_contacts", "$map_talk_troop", slot_troop_town_with_contacts),			
		(store_faction_of_party, ":town_faction", ":town_with_contacts"),

		(call_script, "script_update_faction_political_notes", ":town_faction"),
		(assign, ":instability_index", reg0),
		(val_add, ":instability_index", reg0),
		(val_add, ":instability_index", reg1),

		
		(str_store_faction_name, s12, ":town_faction"),
		(try_begin),
			(ge, ":instability_index", 60), ##1.132
#			(gt, ":instability_index", 60), ##1.131
			(str_store_string, s11, "str_the_s12_is_a_labyrinth_of_rivalries_and_grudges_lords_ignore_their_lieges_summons_and_many_are_ripe_to_defect"),
		(else_try),
			(ge, ":instability_index", 40), ##1.132
#			(is_between, ":instability_index", 40, 60), ##1.131
			(str_store_string, s11, "str_the_s12_is_shaky_many_lords_do_not_cooperate_with_each_other_and_some_might_be_tempted_to_defect_to_a_liege_that_they_consider_more_worthy"),
		(else_try),
			(ge, ":instability_index", 20), ##1.132
#			(is_between, ":instability_index", 20, 40), ##1.131
			(str_store_string, s11, "str_the_s12_is_fairly_solid_some_lords_bear_enmities_for_each_other_but_they_tend_to_stand_together_against_outside_enemies"),
		(else_try),
#			(lt, ":instability_index", 20), ##1.131, to be removed in 1.132
			(str_store_string, s11, "str_the_s12_is_a_rock_of_stability_politically_speaking_whatever_the_lords_may_think_of_each_other_they_fight_as_one_against_the_common_foe"),
		(try_end),

		(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
			(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
			(store_faction_of_troop, ":lord_faction", ":lord"),
			(eq, ":lord_faction", ":town_faction"),
			(call_script, "script_update_troop_political_notes", ":lord"),
		(try_end),		
		
	    ],
	   "Well, {s21}, at last I've found you. {s11}. The rest of my report I submit to you in writing.", "companion_rejoin_response", [
		]],
					

					
  [anyone, "event_triggered", [
                     (store_conversation_troop, "$map_talk_troop"),
					 (is_between, "$map_talk_troop", companions_begin, companions_end),
					 
                     (eq, "$map_talk_troop", "$npc_to_rejoin_party"), 
#                     (eq, "$npc_map_talk_context", slot_troop_days_on_mission), 
                     (troop_get_slot, ":mission", "$g_talk_troop", slot_troop_current_mission), 
					 (this_or_next|eq, ":mission", npc_mission_peace_request),
					 (this_or_next|eq, ":mission", npc_mission_pledge_vassal),
					 (this_or_next|eq, ":mission", npc_mission_test_waters),
					 (this_or_next|eq, ":mission", npc_mission_non_aggression),
						(eq, ":mission", npc_mission_seek_recognition),
						
					 (troop_get_slot, ":string", "$map_talk_troop", slot_troop_honorific),
                     (str_store_string, 21, ":string"),
					 (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
					 (str_store_faction_name, s31, ":mission_object"),
					 
					 (call_script, "script_npc_decision_checklist_peace_or_war", ":mission_object", "fac_player_supporters_faction", "$g_talk_troop"),
					 (assign, "$g_mission_result", reg0),
					##diplomacy start+
							(try_begin),
								(ge, "$cheat_mode", 1),
								(display_message, "@{!} DEBUG - Native checklist-peace-or-war result {reg0}, because {s14}"),
							(try_end),
							#make gender correct
							(faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
							(call_script, "script_dplmc_store_troop_is_female", ":emissary_object"),
						   ],#next line "him" to {reg0?her:him}
	#diplomacy begin
	"Well, {s21}, at last I've found you. I have returned from my mission to {s31}. In general, I would say, {s14}. Nevertheless I tried to convince {reg0?her:him}.","companion_embassy_results", [
	#diplomacy end
	 ]],
	##diplomacy end+

	##diplomacy start+ Alternate check for recognition
	[anyone, "companion_embassy_results", [
		(troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_seek_recognition),
		(troop_get_slot, ":target_faction", "$g_talk_troop", slot_troop_mission_object),
		(neg|faction_slot_ge, ":target_faction", slot_faction_recognized_player, 1),	
		(assign, ":check_peace_war", "$g_mission_result"),#Negative is wants war, positive is wants peace, 0 is undecided
		(ge, ":check_peace_war", 0),
		
		#Check to see if the player might be ruler of an NPC faction
		(assign, ":player_faction", "fac_player_supporters_faction"),
		(try_begin),
			(neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
			(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
			(assign, ":player_faction", "$players_kingdom"),
		(try_end),

		#Must either be at peace or want to be at peace
		(store_relation, reg0, ":player_faction", ":target_faction"),
		(this_or_next|ge, reg0, 0),
			(ge, ":check_peace_war", 1),
		
		(is_between, "$g_player_court", centers_begin, centers_end),
		(faction_get_slot, ":target_liege", ":target_faction", slot_faction_leader),
		(neg|party_slot_eq, "$g_player_court", dplmc_slot_center_original_lord, ":target_liege"),
		(neg|troop_slot_eq, ":target_liege", slot_troop_home, "$g_player_court"),

		(assign, ":global_points", 0),
		(assign, ":target_points", 0),
		(assign, ":player_points", 0),

		(store_current_hours, ":now"),
		(store_sub, ":recently", ":now", 24 * 21),#within last 3 weeks
		
		#2 points for a castle, 4 points for a town, ignore villages
		(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
			(assign, ":center_value", 2),
			(try_begin),
				(party_slot_eq, ":center_no", slot_party_type, spt_town),
				(assign, ":center_value", 4),
			(try_end),
			(val_add, ":global_points", ":center_value"),

			(store_faction_of_party, ":center_faction", ":center_no"),
			
			(try_begin),
				(eq, ":center_faction", ":target_faction"),
				(val_add, ":target_points", ":center_value"),
			(else_try),
				(assign, ":is_occupied", 0),
				(try_begin),
					(this_or_next|troop_slot_eq, ":target_liege", slot_troop_home, ":center_no"),
					(this_or_next|party_slot_eq, ":center_no", slot_center_original_faction, ":target_faction"),
						(party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":target_liege"),
					(assign, ":is_occupied", 1),
				(else_try),
					(this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":target_liege"),
						(party_slot_eq, ":center_no", slot_center_ex_faction, ":target_faction"),
					(party_slot_ge, ":center_no", dplmc_slot_center_last_transfer_time, ":recently"),
					(assign, ":is_occupied", 1),
				(try_end),
				(eq, ":is_occupied", 0),		
				(this_or_next|eq, ":center_faction", "fac_player_supporters_faction"),
					(eq, ":center_faction", "$players_kingdom"),
				(val_add, ":player_points", ":center_value"),
			(try_end),
		(try_end),
		
		#Needs to hold territory (aside from territory the target faction considers to belong to itself)
		(try_begin),
			(ge, "$cheat_mode", 1),
			(lt,  ":player_points", 1),
			(display_message, "@{!} Recognition refused because player owns no fortresses not claimed by target faction"),
		(try_end),
		(ge, ":player_points", 1),
		
		#2 points for a lord
		(val_add, ":global_points", 2),#for the player
		(val_add, ":player_points", 2),
		(try_for_range, ":active_npc", heroes_begin, heroes_end),
			(assign, ":lord_value", 2),
			(try_begin),
				#Give less weight to commoners
				(troop_slot_ge, ":active_npc", slot_lord_reputation_type, lrep_roguish),
				(assign, ":lord_value", 1),
			(try_end),
			(try_begin),
				#current lords + original lords
				(this_or_next|is_between, ":active_npc", kings_begin, kings_end),
				(this_or_next|is_between, ":active_npc", lords_begin, lords_end),
				(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
				(val_add, ":global_points", ":lord_value"),
			(try_end),
			(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
			(store_faction_of_troop, ":cur_faction", ":active_npc"),
			(try_begin),
				(eq, ":cur_faction", ":target_faction"),
				(val_add, ":target_points", ":lord_value"),
			(else_try),
				(this_or_next|eq, ":cur_faction", "fac_player_supporters_faction"),
				(eq, ":cur_faction", "$players_kingdom"),
				(val_add, ":player_points", ":lord_value"),
			(try_end),
		(try_end),
		
	(store_sub, ":num_kingdoms", npc_kingdoms_end, npc_kingdoms_begin),#Not necessarily number of active kingdoms
		(val_max, ":num_kingdoms", 2),
		(store_div, ":average_points", ":global_points", ":num_kingdoms"),
		
		(try_begin),
			(ge, "$cheat_mode", 1),
			(assign, reg0, ":player_points"),
			(assign, reg1, ":target_points"),
			(assign, reg2, ":average_points"),
			(display_message, "@{!} Military strength check: Player faction score {reg0}, target faction score {reg1}, benchmark score {reg2}"),
		(try_end),
		
		#Calculate adjustment for player score
		(store_add, ":subjective_percent_modifier", "$player_right_to_rule", 1),#Because it is capped at 99 instead of 100 in Native
		(val_mul, ":subjective_percent_modifier", 2),
		(val_add, ":subjective_percent_modifier", 2),
		(val_div, ":subjective_percent_modifier", 5),
		(val_add, ":subjective_percent_modifier", 60),#100 if you have full right-to-rule, 60 if you have no right-to-rule	
		(call_script, "script_troop_get_player_relation", ":target_liege"),
		(try_begin),
			#Maximum positive modifier +20%
			(ge, reg0, 0),
			(val_div, reg0, 5),
		(else_try),
			#Minimum negative modifier -40%
			(lt, reg0, 0),
			(val_mul, reg0, 2),
			(val_div, reg0, 5),
		(try_end),
		(val_add, ":subjective_percent_modifier", reg0),#adjusts % by +20 to -40; minimum possible is 20, maximum possible is 120
		
		#Apply adjustment to player score
	(val_clamp, ":subjective_percent_modifier", 20, 121),#<-- This should have no effect unless there is a mistake above
		(val_mul, ":player_points", ":subjective_percent_modifier"),
		(val_div, ":player_points", 100),
		
		#Calculate adjustment for target score
		#Adjust standards towards the mean
		(try_begin),
			(le, ":check_peace_war", -1),
			#Right now the code can't get this far if the check-peace-war
			#result was negative, but leave this in here to handle it if
			#that gets changed.
			(val_max, ":target_points", ":average_points"),
		(else_try),
			(le, ":check_peace_war", 1),
			(val_add, ":target_points", ":average_points"),
			(val_div, ":target_points", 2),
		(else_try),
			(ge, ":check_peace_war", 2),
			(val_min, ":target_points", ":average_points"),
		(try_end),
		#For some variability, adjust the target score by + or - 10%
		(store_random_in_range, reg0, 0, 21),
		(store_add, ":subjective_percent_modifier", 90, reg0),
		#Apply modifier based on check_peace_war
		(val_max, ":check_peace_war", -5),#In Native this result won't ever reach these bounds, but add these in case
		(val_min, ":check_peace_war", 5),#the script behavior is altered later.
		(store_mul, reg0, ":check_peace_war", -10),
		(try_begin),
			(lt, ":check_peace_war", 0),
			(val_mul, reg0, 2),
		(try_end),
		(val_add, ":subjective_percent_modifier", reg0),
		#Apply penalty based on war and/or betrayal
		(try_begin),
			(eq, ":target_faction", "$players_oath_renounced_against_kingdom"),
			(val_add, ":subjective_percent_modifier", 20),
		(else_try),
			(store_relation, reg0, ":player_faction", ":target_faction"),
			(lt, reg0, 0),
			(lt, ":check_peace_war", 1),
			(val_add, ":subjective_percent_modifier", 10),
		(try_end),

		#Apply adjustment to target score
		(val_mul, ":target_points", reg0),
		(val_div, ":target_points", 100),
		
		(try_begin),
			(ge, "$cheat_mode", 1),
			(assign, reg0, ":player_points"),
			(assign, reg1, ":target_points"),
			(display_message, "@{!} Player faction score for recognition is {reg0}, needs to be at least {reg1}"),
		(try_end),
		#Moment of truth
		(ge, ":player_points", ":target_points"),

		(str_store_troop_name, s12, ":target_liege"),
		(str_store_party_name, s4, "$g_player_court"),
	],
	"In this letter, {s12} addresses you as {Lord/Lady} of {s4}, which implies some sort of recognition that you are a sovereign and independent monarch.","companion_rejoin_response", [
				(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
			 (try_begin),
				(faction_slot_eq, ":mission_object", slot_faction_recognized_player, 0),
				(faction_set_slot, ":mission_object", slot_faction_recognized_player, 1),
				(call_script, "script_change_player_right_to_rule", 10),
			 (try_end),
			 ]],
			 
	##For the standard refusal logic, give more insight into why they refused.
	[anyone, "companion_embassy_results", [
		(troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_seek_recognition),
		(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
		(faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
		#Would have recognized
		(this_or_next|ge, "$g_mission_result", 2),
			(faction_slot_eq, ":mission_object", slot_faction_recognized_player, 1),
		#Except there is no court
		(neg|is_between, "$g_player_court", centers_begin, centers_end),
		(str_store_troop_name, s12, ":emissary_object"),
		(call_script, "script_dplmc_store_troop_is_female", ":emissary_object"),
	],
	"In {reg0?her:his} letter, {s12} merely refers to you as {playername}, omitting any title. This does not constitute recognition of your right to rule. The letter implies that {reg0?she:he} is unwilling to extend recognition due to your lack of a court.","companion_rejoin_response", [
			 ]],

	[anyone, "companion_embassy_results", [
		(troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_seek_recognition),
		(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
		(faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
		#Would have recognized
		(this_or_next|ge, "$g_mission_result", 2),
			(faction_slot_eq, ":mission_object", slot_faction_recognized_player, 1),
		(is_between, "$g_player_court", centers_begin, centers_end),
		#Except our court is in one of his original centers, or we occupy a fief
		#that is a sticking point.
		(assign, ":number_of_fiefs", 0),
		(str_clear, s0),
		(str_clear, s1),
		(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
			(store_faction_of_party, ":center_faction", ":center_no"),
			(this_or_next|eq, ":center_faction", "fac_player_supporters_faction"),
				(eq, ":center_faction", "$players_kingdom"),
			(assign, reg0, 0),
			(try_begin),
				(this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":emissary_object"),
					(troop_slot_eq, ":emissary_object", slot_troop_home, ":center_no"),
				(assign, reg0, 1),
			(else_try),
				(eq, ":center_no", "$g_player_court"),
				(party_slot_eq, ":center_no", slot_center_original_faction, ":mission_object"),
				(assign, reg0, 1),
			(try_end),
			(eq, reg0, 1),
			(try_begin),
				(ge, ":number_of_fiefs", 2),
				(str_store_string, s0, "str_dplmc_s0_comma_s1"),
			(else_try),
				(eq, ":number_of_fiefs", 1),
				(str_store_string_reg, s0, s1),
			(try_end),
			(str_store_party_name, s1, ":center_no"),
			(val_add, ":number_of_fiefs", 1),
		(try_end),
		#Fief objections found
		(ge, ":number_of_fiefs", 1),
		(try_begin),
			(eq, ":number_of_fiefs", 1),
			(str_store_string_reg, s0, s1),
		(else_try),
			(str_store_string, s0, "str_dplmc_s0_and_s1"),
		(try_end),
		(str_clear, s1),
		
		(str_store_troop_name, s12, ":emissary_object"),
		(call_script, "script_dplmc_store_troop_is_female", ":emissary_object"),
	],
	"In {reg0?her:his} letter, {s12} merely refers to you as {playername}, omitting any title. This does not constitute recognition of your right to rule. The letter implies that {reg0?she:he} is unwilling to extend recognition due to your occupation of {s0}.","companion_rejoin_response", [
			 ]],

	##diplomacy end+

	[anyone, "companion_embassy_results", [
				 (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_seek_recognition),
			 (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),

			 (this_or_next|ge, "$g_mission_result", 2),
				(faction_slot_eq, ":mission_object", slot_faction_recognized_player, 1),

			 (is_between, "$g_player_court", centers_begin, centers_end),

			 (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
			 (str_store_troop_name, s12, ":emissary_object"),
			 (neg|party_slot_eq, "$g_player_court", slot_center_original_faction, ":mission_object"),
			 ##diplomacy start+
			 ##Add a check regarding any territory that would be a sore point with the liege.
			 (assign, ":end_cond", walled_centers_end),
			 (try_for_range, ":center_no", walled_centers_begin, ":end_cond"),
				(store_faction_of_party, ":center_faction", ":center_no"),
				(this_or_next|eq, ":center_faction", "fac_player_supporters_faction"),
					(eq, ":center_faction", "$players_kingdom"),
				(this_or_next|troop_slot_eq, ":emissary_object", slot_troop_home, ":center_no"),
					(party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":emissary_object"),
				(assign, ":end_cond", ":center_no"),
			 (try_end),
			 (eq, ":end_cond", walled_centers_end),
			 ##diplomacy end+
			 (str_store_party_name, s4, "$g_player_court"),
	],
	"In this letter, {s12} addresses you as {Lord/Lady} of {s4}, which implies some sort of recognition that you are a sovereign and independent monarch.","companion_rejoin_response", [
				(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
			 (try_begin),
				(faction_slot_eq, ":mission_object", slot_faction_recognized_player, 0),
				(faction_set_slot, ":mission_object", slot_faction_recognized_player, 1),
				(call_script, "script_change_player_right_to_rule", 10),
			 (try_end),
			 ]],

	##diplomacy start+
	#For flavor, if the recognition mission failed, give an alternate refusal message
	#when the player is co-ruler of a kingdom.
	[anyone, "companion_embassy_results", [
		(troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_seek_recognition),
		(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
		(faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
		#Check in case the player faction shouldn't be fac_player_supporters_faction
		(assign, ":player_faction", "fac_player_supporters_faction"),
		(try_begin),
			(neg|faction_slot_eq, ":player_faction", slot_faction_state, sfs_active),
			(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
			(assign, ":player_faction", "$players_kingdom"),
		(try_end),
		#The player is not the sole faction leader
		(faction_get_slot, ":player_faction_leader", ":player_faction", slot_faction_leader),
		(neq, ":player_faction_leader", "trp_player"),
		#The leader is a king or pretender
		(this_or_next|is_between, ":player_faction_leader", kings_begin, kings_end),
			(is_between, ":player_faction_leader", pretenders_begin, pretenders_end),
		(str_store_troop_name, s0, ":player_faction_leader"),
		(str_store_troop_name, s12, ":emissary_object"),
		(call_script, "script_dplmc_store_troop_is_female", ":emissary_object"),
		],
		"In this letter, {s12} addresses {reg0?her:his} response to {s0}, referring to you only as {s0}'s faithful vassal. This does not constitute recognition of your right to rule.","companion_rejoin_response", [
		]],
	##diplomacy end+
	[anyone, "companion_embassy_results", [
				  (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_seek_recognition),
			 (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
			 (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
			 (str_store_troop_name, s12, ":emissary_object"),
			##diplomacy start+ Use proper pronoun
			(call_script, "script_dplmc_store_troop_is_female", ":emissary_object"),
	],#Next line replace "his" with {reg0?her:his}
	"In {reg0?her:his} letter, {s12} merely refers to you as {playername}, omitting any title. This does not constitute recognition of your right to rule.","companion_rejoin_response", [
	##diplomacy end+
			 ]],

	[anyone, "companion_embassy_results", [
				  (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_peace_request),
			 (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
			 (faction_slot_ge, ":mission_object", slot_faction_truce_days_with_factions_begin, 1),
			 (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
			 (str_store_troop_name, s12, ":emissary_object"),

	],
	"{s12} says that your current truce should suffice.","companion_rejoin_response", [
			 ]],


	[anyone, "companion_embassy_results", [
				  (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_peace_request),
			 (ge, "$g_mission_result", 1),
			 (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
			 (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
			 (str_store_troop_name, s12, ":emissary_object"),
	##diplomacy start+ make gender correct
	(call_script, "script_dplmc_store_troop_is_female", ":emissary_object"),
	],#Next line "he" to {reg0?she:he}
	##diplomacy begin
	"{s12} says that {reg0?she:he} is willing to consider a truce of twenty days.","companion_truce_confirm", [
	##diplomacy end
	##diplomacy end+
			 ]],

	[anyone, "companion_embassy_results", [
				 (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_peace_request),
			 (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
			 (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
			 (str_store_troop_name, s12, ":emissary_object"),
	##diplomacy start+ make gender correct
	(call_script, "script_dplmc_store_troop_is_female", ":emissary_object"),
	],#Next line "he" to {reg0?she:he}
	"{s12} says that {reg0?she:he} is unwilling to conclude a peace.","companion_rejoin_response", [
	##diplomacy end+
			 ]],
					

  [anyone|plyr, "companion_truce_confirm", [
	(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
	(str_store_faction_name, s4, ":mission_object"),
  ],					
   "Very well - let this truce with the {s4} be concluded.","companion_rejoin_response", [
	(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
    (call_script, "script_diplomacy_start_peace_between_kingdoms", ":mission_object", "$players_kingdom", 1), 
	(str_store_faction_name, s4, ":mission_object"),
	]],

  [anyone|plyr, "companion_truce_confirm", [],					
   "On second thought, perhaps this is currently not in our interests.","companion_rejoin_response", [
					]],


  [anyone, "companion_embassy_results", [
                    (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_pledge_vassal),
#					(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
					(this_or_next|check_quest_active, "qst_join_faction"),
						(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
				   (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
				   (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
				   (str_store_troop_name, s12, ":emissary_object"),
						
  ],					
   "{s12} says that you are already pledged to another ruler.","companion_rejoin_response", [
					]],
					
	[anyone, "companion_embassy_results", [
				  (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_pledge_vassal),
	#					(troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
			 (lt, "$g_mission_result", -2),
			 (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
			 (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
			 (str_store_troop_name, s12, ":emissary_object"),
	##diplomacy start+ make gender correct
	(call_script, "script_dplmc_store_troop_is_female", ":emissary_object"),
	],#next line "he" to {reg0?she:he}
	"{s12} says that {reg0?she:he} does not believe that you would honor your obligations as a vassal, and suspects that your offer is just a ploy.","companion_rejoin_response", [
			 ]],
	##diplomacy end+

	[anyone, "companion_embassy_results", [
				  (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_pledge_vassal),
			 (troop_get_slot, ":mission_object", "$g_talk_troop", slot_troop_mission_object),
			 (faction_get_slot, ":emissary_object", ":mission_object", slot_faction_leader),
			 (str_store_troop_name, s12, ":emissary_object"),
	##diplomacy start+ make gender correct
	(call_script, "script_dplmc_store_troop_is_female", ":emissary_object"),
	],#next line "he" to {reg0?she:he}, etc.
	"{s12} says that {reg0?she:he} accepts your offer of vassalage. {reg0?She:He} will give you 20 days to seek {reg0?her:him} out, in which time {reg0?she:he} will refrain from making war on you.","vassalage_offer_confirm", [
			 ]],
	##diplomacy end+

	[anyone|plyr, "vassalage_offer_confirm", [],
	##diplomacy start+ next line "him" to {reg0?her:him}
	"Tell {reg0?her:him} that I accept {reg0?her:his} terms...", "companion_rejoin_response", [
	##diplomacy end+
   
		(troop_get_slot, "$g_invite_faction", "$g_talk_troop", slot_troop_mission_object),
		(faction_get_slot, "$g_invite_faction_lord", "$g_invite_faction", slot_faction_leader),

		(str_store_troop_name,s1,"$g_invite_faction_lord"),
        (setup_quest_text,"qst_join_faction"),

        (str_store_troop_name_link, s3, "$g_invite_faction_lord"),
        (str_store_faction_name_link, s4, "$g_invite_faction"),
        (quest_set_slot, "qst_join_faction", slot_quest_giver_troop, "$g_invite_faction_lord"),
        (quest_set_slot, "qst_join_faction", slot_quest_expiration_days, 20),
		
		(try_begin),
			(store_relation, ":relation", "$g_invite_faction", "fac_player_supporters_faction"),
			(lt, ":relation", 0),
			(call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_invite_faction", "fac_player_supporters_faction", 0),
			(quest_set_slot, "qst_join_faction", slot_quest_failure_consequence, 1),
		(try_end),
		
        (str_store_string, s2, "@Find and speak with {s3} of {s4} to give him your oath of homage."),
        (call_script, "script_start_quest", "qst_join_faction", "$g_invite_faction_lord"),
        (call_script, "script_report_quest_troop_positions", "qst_join_faction", "$g_invite_faction_lord", 3),
		]],	



		

					
					
  [anyone|plyr, "companion_rejoin_response", [
	(hero_can_join, "p_main_party"),
	(neg|main_party_has_troop, "$map_talk_troop"), ##1.132, new line
      ],  "Welcome back, friend!", "close_window", [
        (party_add_members, "p_main_party", "$map_talk_troop", 1),
		(assign, "$npc_to_rejoin_party", 0),
        (troop_set_slot, "$map_talk_troop", slot_troop_current_mission, 0), 
		(troop_set_slot, "$map_talk_troop", slot_troop_days_on_mission, 0),
          ]],

  [anyone|plyr, "companion_rejoin_response", [
      ],  "Unfortunately, I cannot take you back just yet.", "companion_rejoin_refused", [
        (troop_set_slot, "$map_talk_troop", slot_troop_current_mission, npc_mission_rejoin_when_possible), 
		(troop_set_slot, "$map_talk_troop", slot_troop_days_on_mission, 0),
		(assign, "$npc_to_rejoin_party", 0),
          ]],

  [anyone, "companion_rejoin_refused", [
      ],  "As you wish. I will take care of some business, and try again in a few days.", "close_window", [
          ]],

  [anyone, "event_triggered", [
	(is_between, "$g_talk_troop", companions_begin, companions_end),
	(neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
	(neg|main_party_has_troop, "$g_talk_troop"),
                     ],
   "Would you have me rejoin you?", "companion_rejoin_response", [
    (assign, "$map_talk_troop", "$g_talk_troop"), ##1.132, new line
       ]],

#caravan merchants
  [anyone, "event_triggered",  
   [(eq, "$caravan_escort_state",1),
    (eq, "$g_encountered_party","$caravan_escort_party_id"),
    (le, "$talk_context",tc_party_encounter),
    (store_distance_to_party_from_party, reg0, "$caravan_escort_destination_town", "$caravan_escort_party_id"),
    (lt, reg0, 5),
    (str_store_party_name, s3, "$caravan_escort_destination_town"),
    (assign, reg3, "$caravan_escort_agreed_reward"),
    ],
   "There! I can see the walls of {s3} in the distance. We've made it safely.\
 Here, take this purse of {reg3} denars, as I promised. I hope we can travel together again someday.", "close_window",
   [
    (assign,"$caravan_escort_state",0),
    (call_script, "script_troop_add_gold", "trp_player", "$caravan_escort_agreed_reward"),
    (assign,reg(4), "$caravan_escort_agreed_reward"),
    (val_mul,reg(4), 1),
    (add_xp_as_reward,reg(4)),
    (assign, "$g_leave_encounter",1),
    ]],
 
  # [anyone, "event_triggered", [
                     # ],
   # "{!}Sorry -- just talking to myself [ERROR- {s51}]", "close_window", [
       # ]],






#KINGDOM LORD DIALOGS BEGINS HERE




#FEMALE PLAYER CHACTER WEDDING (also go to the feast, 'lift a glass' speeches for npc lords)
#Feast not yet organized  
  [anyone, "start", [
  (lt, "$talk_context", tc_siege_commander),
  
  (check_quest_active, "qst_wed_betrothed_female"),
  (quest_slot_eq, "qst_wed_betrothed_female", slot_quest_giver_troop, "$g_talk_troop"),
  (neg|faction_slot_eq, "$g_talk_troop_faction", slot_faction_ai_state, sfai_feast),
  
  (store_current_hours, ":hours_since_betrothal"),
  (troop_get_slot, ":betrothal_time", "$g_talk_troop", slot_troop_betrothal_time),
  (val_sub, ":hours_since_betrothal", ":betrothal_time"),
  (lt, ":hours_since_betrothal", 720), #30 days
  (str_clear, s12),
  (try_begin),
	(neg|faction_slot_eq, "$g_talk_troop_faction", slot_faction_ai_state, sfai_feast),
	(neg|faction_slot_eq, "$g_talk_troop_faction", slot_faction_ai_state, sfai_default),
    (str_store_string, s12, "@ We will of course need to wait until the realm is no longer on campaign."),
  (try_end),
	],
	#diplomacy start+ gender-correct language
	"My {lord/lady}, I look forward to our marriage, as soon as there is an opportunity to hold a proper feast.{s12}", "lord_start", [
	#diplomacy end+
	]],

	#Feast, but not at the venue
	[anyone, "start", [
	(lt, "$talk_context", tc_siege_commander),

	(check_quest_active, "qst_wed_betrothed_female"),
	(quest_slot_eq, "qst_wed_betrothed_female", slot_quest_giver_troop, "$g_talk_troop"),
	(faction_slot_eq, "$g_talk_troop_faction", slot_faction_ai_state, sfai_feast),
	(faction_get_slot, ":feast_venue", "$g_talk_troop_faction", slot_faction_ai_object),
	(party_slot_eq, "$g_talk_troop_party", slot_party_ai_state, spai_holding_center),
	(party_slot_eq, "$g_talk_troop_party", slot_party_ai_object, ":feast_venue"),

	(neq, ":feast_venue", "$g_encountered_party"),
	(str_store_party_name, s4, ":feast_venue"),
	],
	#diplomacy start+ gender-correct language
	"My {lord/lady}, if you wish to marry, we can proceed to the feast at {s4} to exchange vows before the lords of the realm.", "lord_start", [
	#diplomacy end+
	]],

#Over a month, and heading to a center  
  [anyone, "start", [
  (lt, "$talk_context", tc_siege_commander),
  
  (check_quest_active, "qst_wed_betrothed_female"),
  (quest_slot_eq, "qst_wed_betrothed_female", slot_quest_giver_troop, "$g_talk_troop"),

  (store_current_hours, ":hours_since_betrothal"),
  (troop_get_slot, ":betrothal_time", "$g_talk_troop", slot_troop_betrothal_time),
  (val_sub, ":hours_since_betrothal", ":betrothal_time"),
  (ge, ":hours_since_betrothal", 720), #30 days

  (party_get_attached_to, ":attached", "$g_talk_troop_party"),
  (neg|is_between, ":attached", walled_centers_begin, walled_centers_end),

  (party_slot_eq, "$g_talk_troop_party", slot_party_ai_state, spai_holding_center),
  (party_get_slot, ":object", "$g_talk_troop_party", slot_party_ai_object),
  (str_store_party_name, s4, ":object"),
  ],
	#diplomacy start+ gender-correct language
	"My {lord/lady}, I grow tired of waiting for the lords of this realm to assemble. Come with me to {s4} exchange our vows.", "lord_start", [
	#diplomacy end+
	]],

#Over a month, but not in a center  
  [anyone, "start", [
  (lt, "$talk_context", tc_siege_commander),
  (check_quest_active, "qst_wed_betrothed_female"),
  (quest_slot_eq, "qst_wed_betrothed_female", slot_quest_giver_troop, "$g_talk_troop"),

  (store_current_hours, ":hours_since_betrothal"),
  (troop_get_slot, ":betrothal_time", "$g_talk_troop", slot_troop_betrothal_time),
  (val_sub, ":hours_since_betrothal", ":betrothal_time"),
  (ge, ":hours_since_betrothal", 0), #30 days

  (party_get_attached_to, ":attached", "$g_talk_troop_party"),
  (neg|is_between, ":attached", walled_centers_begin, walled_centers_end),

	],
	#diplomacy start+ gender-correct language
	"My {lord/lady}, I grow tired of waiting for the lords of this realm to assemble. Perhaps we should take the first opportunity to marry, in any great hall that is open to us.", "lord_start", [
	#diplomacy end+
	]],

  [anyone, "start", [
  (lt, "$talk_context", tc_siege_commander),
  (check_quest_active, "qst_wed_betrothed_female"),
  (quest_slot_eq, "qst_wed_betrothed_female", slot_quest_giver_troop, "$g_talk_troop"),
  (this_or_next|neg|faction_slot_eq, "$g_talk_troop_faction", slot_faction_ai_state, sfai_feast),
  (neg|faction_slot_eq, "$g_talk_troop_faction", slot_faction_ai_object, "$g_encountered_party"),
	],
	#diplomacy start+ gender-correct language
	"My {lord/lady}, I have grown tired of waiting. Let us proceed with the vows immediately.", "lord_groom_vows", [
	#diplomacy end+
	]],
   
	[anyone, "start", [
	(lt, "$talk_context", tc_siege_commander),
	(check_quest_active, "qst_wed_betrothed_female"),
	(quest_slot_eq, "qst_wed_betrothed_female", slot_quest_giver_troop, "$g_talk_troop"),
	],
	#diplomacy start+ gender-correct language
	"My {lord/lady}, my eyes rejoice to see you. We may proceed with the vows.", "lord_groom_vows", [
	#diplomacy end+
	]],

	[anyone, "lord_groom_vows", [
	],
	#diplomacy start+ gender-correct language
	"My {lord/lady}, with this assembly as my witness, I vow to take you as my {husband/wife}, to honor, cherish, and {obey/protect} you. My the heavens bless us with health, prosperity, and children.", "female_pc_marriage_vow", [
	#diplomacy end+
	]],

	[anyone|plyr, "female_pc_marriage_vow", [
	],
	#diplomacy start+ (female player/male lord) or (male player/female lord)
"I vow to take you as my {reg65?wife:husband}.", "lord_groom_wedding_complete", [
	#diplomacy end+
	(call_script, "script_courtship_event_bride_marry_groom", "trp_player", "$g_talk_troop", 0),
	(call_script, "script_end_quest", "qst_wed_betrothed_female"),
	]],
   
  [anyone|plyr, "female_pc_marriage_vow", [
  ],
   "Wait -- I need to think about this.", "close_window", [
   (assign, "$g_leave_encounter", 1),
   ]],
   
  [anyone, "lord_groom_wedding_complete", [
  ],
   "We are now husband and wife. Let the festivities commence!", "close_window",
   []],   

   
# KINGDOM LORD DUEL OUTCOMES
  [anyone,"start",
  [(eq, "$talk_context", tc_after_duel),
   (check_quest_active, "qst_denounce_lord"),
   (check_quest_succeeded, "qst_denounce_lord"),
   (quest_slot_eq, "qst_denounce_lord", slot_quest_target_troop, "$g_talk_troop"),
  ],
   "Very well. You've made your point. I have nothing more to say.", "close_window", [
   (call_script, "script_change_troop_renown", "trp_player", 10),
   (assign, "$g_leave_encounter", 1),
   ]],

  [anyone,"start",
  [(eq, "$talk_context", tc_after_duel),
   (check_quest_active, "qst_denounce_lord"),
   (check_quest_failed, "qst_denounce_lord"),
   (quest_slot_eq, "qst_denounce_lord", slot_quest_target_troop, "$g_talk_troop"),
  ],
   "Well, {sir/my lady}! Please, do not trouble yourself to rise from the ground, as I would simply have to knock you down again. I shall take your silence as an apology. Good day to you.", "close_window", [
   (call_script, "script_change_troop_renown", "trp_player", -10),
   (assign, "$g_leave_encounter", 1),
   ]],



  [anyone,"start",
  [(eq, "$talk_context", tc_after_duel),
   (assign, "$temp", 0),
   (try_begin),
     (check_quest_active, "qst_duel_avenge_insult"),
     (check_quest_succeeded, "qst_duel_avenge_insult"),
     (quest_slot_eq, "qst_duel_avenge_insult", slot_quest_target_troop, "$g_talk_troop"),
     (assign, "$temp", 1),
   (else_try),
     (check_quest_active, "qst_duel_for_lady"),
     (check_quest_succeeded, "qst_duel_for_lady"),
     (quest_slot_eq, "qst_duel_for_lady", slot_quest_target_troop, "$g_talk_troop"),
     (assign, "$temp", 2),
   (try_end),
   (gt, "$temp", 0),
  ],
   "Very well. You've made your point. I retract what I said. I hope you have obtained satisfaction.", "close_window", [
   (try_begin),
     (eq, "$temp", 1),
     (call_script, "script_change_troop_renown", "trp_player", 10),
     (call_script, "script_end_quest", "qst_duel_avenge_insult"),
   (try_end),
   (assign, "$g_leave_encounter", 1),
   ]],

   [anyone,"start",
  [(eq, "$talk_context", tc_after_duel),
   (assign, "$temp", 0),
   (try_begin),
     (check_quest_active, "qst_duel_avenge_insult"),
     (check_quest_failed, "qst_duel_avenge_insult"),
     (quest_slot_eq, "qst_duel_avenge_insult", slot_quest_target_troop, "$g_talk_troop"),
     (assign, "$temp", 1),
   (else_try),
     (check_quest_active, "qst_duel_for_lady"),
     (check_quest_failed, "qst_duel_for_lady"),
     (quest_slot_eq, "qst_duel_for_lady", slot_quest_target_troop, "$g_talk_troop"),
     (assign, "$temp", 2),
   (try_end),
   (gt, "$temp", 0),
  ],
   "Hah! Not so gallant now, are we? Now trouble me no more.", "close_window", [
   (try_begin),
     (eq, "$temp", 1),
     (call_script, "script_change_troop_renown", "trp_player", -10),
     (call_script, "script_end_quest", "qst_duel_avenge_insult"),
   (try_end),
   (assign, "$g_leave_encounter", 1),
   ]],
   
  [anyone,"start",
  [(eq, "$talk_context", tc_after_duel),
   (check_quest_active, "qst_duel_courtship_rival"),
   (check_quest_succeeded, "qst_duel_courtship_rival"),
   (quest_slot_eq, "qst_duel_courtship_rival", slot_quest_target_troop, "$g_talk_troop"),
   (quest_get_slot, ":duel_object", "qst_duel_courtship_rival", slot_quest_giver_troop),
   (str_store_troop_name, s10, ":duel_object"),
	],
	##diplomacy start+ replace bastard with gender-appropriate insult
	#(TODO: perhaps a culturally-appropriate reference instead)
	"Very well -- you have won. Let all those present today witness that you have defeated me, and I shall abandon my suit of {s10}. Are you satisfied, you heartless {bastard/bitch}?", "close_window", [
	##diplomacy end+
	(quest_get_slot, ":duel_object", "qst_duel_courtship_rival", slot_quest_giver_troop),
	(call_script, "script_courtship_event_lady_break_relation_with_suitor", ":duel_object", "$g_talk_troop"),
	(assign, "$g_leave_encounter", 1),
   ]],
   
   
	[anyone,"start",
	[(eq, "$talk_context", tc_after_duel),
	(check_quest_active, "qst_duel_courtship_rival"),
	(check_quest_failed, "qst_duel_courtship_rival"),
	(quest_slot_eq, "qst_duel_courtship_rival", slot_quest_target_troop, "$g_talk_troop"),
	(quest_get_slot, ":duel_object", "qst_duel_courtship_rival", slot_quest_giver_troop),
	(str_store_troop_name, s10, ":duel_object"),
	##diplomacy start+
	(call_script, "script_dplmc_store_troop_is_female", ":duel_object"),#enable the male version
	],
	##replace "man" with "{man/woman}", and "her" with "{reg0?her:him}"
	"Get up. Let all those present today witness that I have defeated you, and you are now bound to relinquish your suit of the {s10}. I will permit you one final visit, to make your farewells. After that, if you persist in attempting to see {reg0?her:him}, everyone shall know that you are a {man/woman} of scant honor.", "close_window", [
	##diplomacy end+
	(assign, "$g_leave_encounter", 1),
	]],



	[anyone,"start", [(eq, "$talk_context", tc_castle_commander)],
	"What do you want?", "player_siege_castle_commander_1", []],
	[anyone|plyr,"player_siege_castle_commander_1", [],
	"Surrender! Your situation is hopeless!", "player_siege_ask_surrender", []],
	[anyone|plyr,"player_siege_castle_commander_1", [], "Nothing. I'll leave you now.", "close_window", []],


	[anyone,"player_siege_ask_surrender", [(lt, "$g_enemy_strength", 100), (store_mul,":required_str","$g_enemy_strength",5),(ge, "$g_ally_strength", ":required_str")],
	"Perhaps... Do you give your word of honour that we'll be treated well?", "player_siege_ask_surrender_treatment", []],
	[anyone,"player_siege_ask_surrender", [(lt, "$g_enemy_strength", 200), (store_mul,":required_str","$g_enemy_strength",3),(ge, "$g_ally_strength", ":required_str")],
	"We are ready to leave this castle to you and march away if you give me your word of honour that you'll let us leave unmolested.", "player_siege_ask_leave_unmolested", []],
	##diplomacy start+
	#Make the AI willing to surrender in other situations when it is utterly outclassed
	[anyone,"player_siege_ask_surrender", [
		(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),#only enable if AI changes are active
		(assign, reg0, 0),
		(try_begin),
			#I assume that $g_encountered_party is the town, but this could be wrong
			(neg|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
			(neg|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
			(try_begin),
				(ge, "$cheat_mode", 1),
				(assign, reg0, "$g_encountered_party"),
				(str_store_party_name, s0, "$g_encountered_party"),
				(party_get_slot, reg1, "$g_encountered_party", slot_party_type),
				(display_message, "@{!}Party at address {reg0} named {s0} has slot_party_type {reg1} (not castle or town)"),
			(try_end),
			(assign, reg0, 1),#<- don't continue
		(try_end),
		(eq, reg0, 0),
		#Don't bother continuing if the attackers don't outnumber the defenders by a decent ratio.
		(store_mul, reg0,"$g_enemy_strength", 3),
		(ge, "$g_ally_strength", reg0),
		
		#Enemy must be below a certain strength to even consider giving up.
		(game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
		(this_or_next|lt, "$g_enemy_strength", 500),# Hard (would be described as "small bands" on the world map)
			(ge, ":reduce_campaign_ai", 1),
		(this_or_next|lt, "$g_enemy_strength", 1000),# Medium ("enemy patrols")
			(ge, ":reduce_campaign_ai", 2),
		(lt, "$g_enemy_strength", 2000),# Easy ("medium-sized group")
			
		#Prevent forts from surrendering to five men and a mule.
		(assign, ":defender_str", "$g_enemy_strength"),
		(val_max, ":defender_str", 5),#establish a minimum (if you can't just walk in, there must be some defenders)
		(try_begin),
			#Not that it matters much, given how extremely low it is, but increase the minimum for towns.
			(party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
			(val_max, ":defender_str", 10),
		(try_end),
		
		#Count fortresses and original fortresses for use below
		(assign, ":forts_held", 0),
		(assign, ":starting_forts", 0),	
		(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
			(store_faction_of_party, reg0, ":center_no"),
			(try_begin),
				(eq, reg0, "$g_encountered_party_faction"),
				(val_add, ":forts_held", 1),
			(try_end),
			(try_begin),
				(party_slot_eq, ":center_no", slot_center_original_faction, "$g_encountered_party_faction"),
				(val_add, ":starting_forts", 1),
			(try_end),
		(try_end),
		
		#Always refuse to retreat if this is the last fortress
		(gt, ":forts_held", 1),
		
		#Always refuse to abandon a fort if they don't have more than 50% of their original size.
		(store_mul, reg0, ":forts_held", 2),
		(gt, reg0, ":starting_forts"),

		#Always refuse to abandon a native fort if they don't have more than 100% of their original size
		(assign, ":is_native", 0),
		(try_begin),
			(is_between, "$g_encountered_party_faction", npc_kingdoms_begin, npc_kingdoms_end),#this bonus is only intended for ordinary factions
			#(this_or_next|party_slot_eq, "$g_talk_troop", slot_troop_original_faction, "$g_encountered_party_faction"), # This was the original line from diplomacy.
			(this_or_next|troop_slot_eq, "$g_talk_troop", slot_troop_original_faction, "$g_encountered_party_faction"),
				(party_slot_eq, "$g_encountered_party", slot_center_original_faction, "$g_encountered_party_faction"),
			(assign, ":is_native", 1),
		(try_end),
		
		(this_or_next|gt, ":forts_held", ":starting_forts"),
			(eq, ":is_native", 0),
		
		#Now determine the number of attacking troops required to surrender.
		#Default requirement is being outnumbered 8-to-1
		(assign, ":surrender_ratio_10", 80), 
		
		#Adjust values based on defending commander's personality
		(try_begin),
			#Companions who like retreating are more likely to surrender
			(call_script, "script_dplmc_get_troop_morality_value", "$g_talk_troop", tmt_aristocratic),
			(lt, reg0, 0),
			#On normal will agree if outnumbered 4-to-1
			(val_div, ":surrender_ratio_10", 2),
		(else_try),
			#Companions who dislike retreating will be less likely to surrender
			(this_or_next|ge, reg0, 1),#<- value for tmt_aristocratic
			#The same goes for martial, self-righteous, and quarrelsome lords.
			(this_or_next|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_martial),
			(this_or_next|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_quarrelsome),
			(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_selfrighteous),
			#Exaggerate the effect of this to make it more noticable.
			#On normal will agree if outnumbered 16-to-1.
			(val_mul, ":surrender_ratio_10", 2),
		(else_try),
			#Faction leaders are more tenacious either when defending native territory, or when
			#their faction is at less than 80% strength.
			(this_or_next|is_between, "$g_talk_troop", kings_begin, kings_end),
			(this_or_next|is_between, "$g_talk_troop", pretenders_begin, pretenders_end),
				(faction_slot_eq, "$g_talk_troop_faction", slot_faction_leader, "$g_talk_troop"),
			(store_mul, reg0, ":forts_held", 5),
			(val_div, reg0, 4),
			(this_or_next|lt, reg0, ":starting_forts"),
				(ge, ":is_native", 1),
			#On normal will agree if outnumbered 16-to-1.
			(val_mul, ":surrender_ratio_10", 2),
		(else_try),
			#Ladies with traditional upbringings (other than adventurous ones) are also more likely to run away.
			#So are roguish commoners without a positive tmt_aristocratic value.
			(neg|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_adventurous),
			(this_or_next|troop_slot_ge, "$g_talk_troop", slot_lord_reputation_type, lrep_conventional),
			(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_roguish),
			#On normal will agree if outnumbered 4-to-1
			(val_div, ":surrender_ratio_10", 2),
		(try_end),
		
		#Certain lords consider certain locations "native" and will not easily surrender their homes.
		#Normally the following is just for companions, but I've set it to also include things
		#like Lord Harringoth and Harringoth Castle, etc.  This is applied after personality factors,
		#since it can enhance or counteract someone's native disposition.
		(try_begin),
			(is_between, "$g_talk_troop", active_npcs_begin, kingdom_ladies_end),
			(troop_slot_eq, "$g_talk_troop", slot_troop_home, "$g_encountered_party"),
			#On normal, most will agree if outnumbered 16-to-1, 8-to-1 if cowardly, 32-to-1 if brave
			(val_mul, ":surrender_ratio_10", 2),
		(try_end),
			
		(val_clamp, ":surrender_ratio_10", 40, 320),#If the value is not in this range, there was a coding mistake
		#Adjust threshold for campaign difficulty
		(try_begin),
			(lt, ":reduce_campaign_ai", 1),#hard, 150% (ordinarily 14-to-1, 8-to-1 for cowards, 28-to-1 for brave)
			(val_mul, ":surrender_ratio_10", 3),
			(val_div, ":surrender_ratio_10", 2),
		(else_try),
			(eq, ":reduce_campaign_ai", 0),#medium, 100% (ordinarily 8-to-1, 4-to-1 for cowards, 16-to-1 for brave)
		(else_try),
			(ge, ":reduce_campaign_ai", 2),#easy, 75% (ordinarily 6-to-1, 3-to-1 for cowards, 12-to-1 for brave)
			(val_mul, ":surrender_ratio_10", 3),
			(val_add, ":surrender_ratio_10", 2),
			(val_div, ":surrender_ratio_10", 4),
		(try_end),
		
		#Compare the besiegers' strength to the "surrender threshold"
		(store_mul, ":required_strength", ":defender_str", ":surrender_ratio_10"),
		(store_mul, reg0, "$g_ally_strength", 10),
		(ge, reg0, ":required_strength"),
		],
		"We are ready to leave this castle to you and march away if you give me your word of honour that you'll let us leave unmolested.", "player_siege_ask_leave_unmolested", []],

	#Make a defiant remark if the enemy is vastly outnumbered but refusing to surrender.
	[anyone,"player_siege_ask_surrender", [
		#I assume that $g_encountered_party is the town, but this could be wrong
		(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
			(party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
		(is_between, "$g_encountered_party_faction", kingdoms_begin, kingdoms_end),
		#The attackers outnumber the defenders by a decent ratio.
		(store_mul, reg0,"$g_enemy_strength", 4),
		(ge, "$g_ally_strength", reg0),
		#The attack is on native soil, or the odds are REALLY bad.
		(store_mul, reg0, "$g_enemy_strength", 8),
		(this_or_next|party_slot_eq, "$g_encountered_party", slot_center_original_faction, "$g_encountered_party_faction"),
			(ge, "$g_ally_strength", reg0),
		#Store name of castle and name of faction
		(str_store_faction_name, s0, "$g_talk_troop_faction"),
		(str_store_party_name, s1, "$g_encountered_party"),],
		"The {s0} will never abandon {s1}!", "close_window", []],
		
	##diplomacy end+
	[anyone,"player_siege_ask_surrender", [],
	"Surrender? Hah! We can hold these walls until we all die of old age.", "close_window", []],


  
	[anyone|plyr,"player_siege_ask_surrender_treatment", [],
	"I give you nothing. Surrender now or prepare to die!", "player_siege_ask_surrender_treatment_reject", []],
	[anyone,"player_siege_ask_surrender_treatment_reject", [
	##diplomacy start+ Make both-gender version.
	],
	"{Bastard/Bitch}. We will fight you to the last man!", "close_window", []],
	##diplomacy end+
	[anyone|plyr,"player_siege_ask_surrender_treatment", [],
	"You will be ransomed and your soldiers will live. I give you my word.", "player_siege_ask_surrender_treatment_accept", []],
	[anyone,"player_siege_ask_surrender_treatment_accept", [],
	"Very well then. Under those terms, I offer you my surrender.", "close_window", [(assign,"$g_enemy_surrenders",1)]],

  [anyone|plyr,"player_siege_ask_leave_unmolested", [],
   "You have my word. You will not come under attack if you leave the castle.", "player_siege_ask_leave_unmolested_accept", []],
  [anyone,"player_siege_ask_leave_unmolested_accept", [],
   "Very well. Then we leave this castle to you. You have won this day. But we'll meet again.", "close_window", [(assign,"$g_castle_left_to_player",1)]],
  [anyone|plyr,"player_siege_ask_leave_unmolested", [],
   "Unacceptable. I want prisoners.", "player_siege_ask_leave_unmolested_reject", []],
  [anyone,"player_siege_ask_leave_unmolested_reject", [],
   "Then we will defend this castle to the death, and this parley is done. Farewell.", "close_window", []],


#Prison break

  [anyone|plyr,"lord_prison_break", [],
   "I've come to get you out of here", "lord_prison_break_confirm",
   []],
   
  [anyone|plyr,"lord_prison_break", [],
   "Never mind -- just stay quiet", "close_window",
   [
   (troop_set_slot, "$g_talk_troop", slot_troop_mission_participation, mp_stay_out),
   (assign, "$g_reset_mission_participation", 1),
   ]],
]
