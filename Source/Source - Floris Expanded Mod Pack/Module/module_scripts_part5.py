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

scripts_part5 = [

                        
                        (
                          "npc_decision_checklist_faction_ai_alt", #This is called from within decide_faction_ai, or from
                          [
                            (store_script_param, ":troop_no", 1),
                            
                            (store_faction_of_troop, ":faction_no", ":troop_no"),
                            
                            (str_store_troop_name, s4, ":troop_no"),
                            (str_store_faction_name, s33, ":faction_no"),
                            (try_begin),
                              (eq, "$cheat_mode", 1),
                              (display_message, "@{!}DEBUG -- {s4} produces a faction strategy for {s33}"),
                            (try_end),
                            
                            #INFORMATIONS COLLECTING STEP 0: Here we obtain general information about current faction like how much parties that faction has, which lord is the marshall, current ai state and current ai target object
                            #(faction_get_slot, ":faction_strength", ":faction_no", slot_faction_number_of_parties),
                            (faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
                            (faction_get_slot, ":current_ai_state", ":faction_no", slot_faction_ai_state),
                            (faction_get_slot, ":current_ai_object", ":faction_no", slot_faction_ai_object),
                            
                            (assign, ":marshal_party", -1),
                            (assign, ":marshal_party_strength", 0),
                            
                            (try_begin),
                              (gt, ":faction_marshal", 0),
                              (troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
                              (party_is_active, ":marshal_party"),
                              (party_get_slot, ":marshal_party_itself_strength", ":marshal_party", slot_party_cached_strength),
                              (party_get_slot, ":marshal_party_follower_strength", ":marshal_party", slot_party_follower_strength),
                              (store_add, ":marshal_party_strength", ":marshal_party_itself_strength", ":marshal_party_follower_strength"),
                            (try_end),
                            
                            #INFORMATIONS COLLECTING STEP 1: Here we are learning how much hours past from last offensive situation/feast concluded/current state started
                            (store_current_hours, ":hours_since_last_offensive"),
                            (faction_get_slot, ":last_offensive_time", ":faction_no", slot_faction_last_offensive_concluded),
                            (val_sub, ":hours_since_last_offensive", ":last_offensive_time"),
                            
                            (store_current_hours, ":hours_since_last_feast_start"),
                            (faction_get_slot, ":last_feast_time", ":faction_no", slot_faction_last_feast_start_time),
                            (val_sub, ":hours_since_last_feast_start", ":last_feast_time"),
                            
                            (store_current_hours, ":hours_at_current_state"),
                            (faction_get_slot, ":current_state_started", ":faction_no", slot_faction_ai_current_state_started),
                            (val_sub, ":hours_at_current_state", ":current_state_started"),
                            
                            (store_current_hours, ":hours_since_last_faction_rest"),
                            (faction_get_slot, ":last_rest_time", ":faction_no", slot_faction_ai_last_rest_time),
                            (val_sub, ":hours_since_last_faction_rest", ":last_rest_time"),
                            
                            (try_begin), #calculating ":last_offensive_time_score", this will be used in #11 and #12
                              (ge, ":hours_since_last_offensive", 1080), #more than 45 days (100p)
                              (assign, ":last_offensive_time_score", 100),
                            (else_try),
                              (ge, ":hours_since_last_offensive", 480), #more than 20 days (65p..99p)
                              (store_sub, ":last_offensive_time_score", ":hours_since_last_offensive", 480),
                              (val_div, ":last_offensive_time_score", 20),
                              (val_add, ":last_offensive_time_score", 64),
                            (else_try),
                              (ge, ":hours_since_last_offensive", 240), #more than 10 days (41p..64p)
                              (store_sub, ":last_offensive_time_score", ":hours_since_last_offensive", 240),
                              (val_div, ":last_offensive_time_score", 10),
                              (val_add, ":last_offensive_time_score", 40),
                            (else_try), #less than 10 days (0p..40p)
                              (store_div, ":last_offensive_time_score", ":hours_since_last_offensive", 6), #0..40
                            (try_end),
                            
                            #INFORMATION COLLECTING STEP 3: Here we are finding the most threatened center
                            (call_script, "script_find_center_to_defend", ":troop_no"),
                            (assign, ":most_threatened_center", reg0),
                            (assign, ":threat_danger_level", reg1),
                            (assign, ":enemy_strength_near_most_threatened_center", reg2), #NOTE! This will be off by as much as 50%
                            
                            #INFORMATION COLLECTING STEP 4: Here we are finding number of vassals who are already following the marshal, and the assigned vassal ratio of current faction.
							(assign, ":vassals_already_assembled", 0),
							(assign, ":total_vassals", 0),
							##diplomacy start+ add support for promoted kingdom ladies
							#(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
							(try_for_range, ":lord", heroes_begin, heroes_end),
								(this_or_next|is_between, ":lord", active_npcs_begin, active_npcs_end),
									(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
							##diplomacy end+
								(store_faction_of_troop, ":lord_faction", ":lord"),
								(eq, ":lord_faction", ":faction_no"),
								(troop_get_slot, ":led_party", ":lord", slot_troop_leaded_party),
								(party_is_active, ":led_party"),
								(val_add, ":total_vassals", 1),
                              
                              (party_slot_eq, ":led_party", slot_party_ai_state, spai_accompanying_army),
                              (party_slot_eq, ":led_party", slot_party_ai_object, ":marshal_party"),
                              
                              (party_is_active, ":marshal_party"),
                              (store_distance_to_party_from_party, ":distance_to_marshal", ":led_party", ":marshal_party"),
                              (lt, ":distance_to_marshal", 15),
                              (val_add, ":vassals_already_assembled", 1),
                            (try_end),
                            (assign, ":ratio_of_vassals_assembled", -1),
                            (try_begin),
                              (gt, ":total_vassals", 0),
                              (store_mul, ":ratio_of_vassals_assembled", ":vassals_already_assembled", 100),
                              (val_div, ":ratio_of_vassals_assembled", ":total_vassals"),
                            (try_end),
                            
                            #50% of vassals means that the campaign hour limit is ten days
                            (store_mul, ":campaign_hour_limit", ":ratio_of_vassals_assembled", 3),
                            (val_add, ":campaign_hour_limit", 90),
                            
                            #To Steve - I understand your concern about some marshals will gather army and some will not be able to find any valueable center to attack after gathering,
                            #and these marshals will be questioned by other marshals ext. This is ok but if we search for a target without adding all other vassals what if
                            #AI cannot find any target for long time because of its low power ratio if enemy cities are equal defended? Do not forget if we do not count other vassals in
                            #faction while making target search we can only add marshal army's power and vassals around him. And if there is any threat in our centers even it is smaller,
                            #its threat_danger_level will be more than target_value_level if marshal new started gathering for ofensive. Because we only assume marshal and around vassals
                            #will join attack. And in our scenarios currently there are less vassals are around him. So power ratio will be low and any small threat will be enought to stop
                            #an offensive. Then when players finds out this they periodically will take under siege to enemy's any center and they will be saved from any kind of newly started
                            #offensive they will be faced. So we have to calculate both attack levels and select highest one to compare with threat level. Please do not change this part.
                            
                            (try_begin),
                              (ge, ":faction_marshal", 0),
                              (ge, ":marshal_party", 0),
                              (party_is_active, ":marshal_party"),
                              
                              (call_script, "script_party_count_fit_for_battle", ":marshal_party"),
                              (assign, ":number_of_fit_soldiers_in_marshal_party", reg0),
                              (ge, ":number_of_fit_soldiers_in_marshal_party", 40),
                              
                              (call_script, "script_find_center_to_attack_alt", ":troop_no", 1, 0),
                              (assign, ":center_to_attack_all_vassals_included", reg0),
                              (assign, ":target_value_level_all_vassals_included", reg1),
                              
                              (call_script, "script_find_center_to_attack_alt", ":troop_no", 1, 1),
                              (assign, ":center_to_attack_only_marshal_and_followers", reg0),
                              (assign, ":target_value_level_only_marshal_and_followers", reg1),
                            (else_try),
                              (assign, ":target_value_level_all_vassals_included", 0),
                              (assign, ":target_value_level_only_marshal_and_followers", 0),
                              (assign, ":center_to_attack_all_vassals_included", -1),
                              (assign, ":center_to_attack_only_marshal_and_followers", -1),
                            (try_end),
                            
                            (try_begin),
                              (ge, ":target_value_level_all_vassals_included", ":center_to_attack_only_marshal_and_followers"),
                              (assign, ":center_to_attack", ":center_to_attack_all_vassals_included"),
                              (assign, ":target_value_level", ":target_value_level_all_vassals_included"),
                            (else_try),
                              (assign, ":center_to_attack", ":center_to_attack_only_marshal_and_followers"),
                              (assign, ":target_value_level", ":target_value_level_only_marshal_and_followers"),
                            (try_end),
                            
                            (try_begin),
                              (eq, ":current_ai_state", sfai_attacking_center),
                              (val_mul, ":target_value_level", 3),
                              (val_div, ":target_value_level", 2),
                            (try_end),
                            
                            (try_begin),
                              (eq, "$cheat_mode", 1),
                              (try_begin),
                                (is_between, ":center_to_attack", centers_begin, centers_end),
                                (str_store_party_name, s4, ":center_to_attack"),
                                (display_message, "@{!}Best offensive target {s4} has value level of {reg1}"),
                              (else_try),
                                (display_message, "@{!}No center found to attack"),
                              (try_end),
                              
                              (try_begin),
                                (is_between, ":most_threatened_center", centers_begin, centers_end),
                                (str_store_party_name, s4, ":most_threatened_center"),
                                (assign, reg1, ":threat_danger_level"),
                                (display_message, "@{!}Best threat of {s4} has value level of {reg1}"),
                              (else_try),
                                (display_message, "@{!}No center found to defend"),
                              (try_end),
                            (try_end),
                            
                            (try_begin),
                              (eq, "$cheat_mode", 1),
                              
                              (try_begin),
                                (is_between, ":most_threatened_center", centers_begin, centers_end),
                                (str_store_party_name, s4, ":most_threatened_center"),
                                (assign, reg1, ":threat_danger_level"),
                                (display_message, "@Best threat of {s4} has value level of {reg1}"),
                              (else_try),
                                (display_message, "@No center found to defend"),
                              (try_end),
                            (try_end),
                            
                            (assign, "$g_target_after_gathering", -1),
                            
                            (store_current_hours, ":hours"),
                            (try_begin),
                              (ge, ":target_value_level", ":threat_danger_level"),
                              (faction_set_slot, ":faction_no", slot_faction_last_safe_hours, ":hours"),
                            (try_end),
                            (faction_get_slot, ":last_safe_hours", ":faction_no", slot_faction_last_safe_hours),
                            (try_begin),
                              (eq, ":last_safe_hours", 0),
                              (faction_set_slot, ":faction_no", slot_faction_last_safe_hours, ":hours"),
                            (try_end),
                            (faction_get_slot, ":last_safe_hours", ":faction_no", slot_faction_last_safe_hours),
                            (store_sub, ":hours_since_days_defensive_started", ":hours", ":last_safe_hours"),
                            (str_store_faction_name, s7, ":faction_no"),
                            
                            (assign, ":at_peace_with_everyone", 1),
                            (try_for_range, ":faction_at_war", kingdoms_begin, kingdoms_end),
                              (store_relation, ":relation", ":faction_no", ":faction_at_war"),
                              (lt, ":relation", 0),
                              (assign, ":at_peace_with_everyone", 0),
                            (try_end),
                            
                            
                            #INFORMATIONS ARE COLLECTED, NOW CHECK ALL POSSIBLE ACTIONS AND DECIDE WHAT TO DO	NEXT
                            #Player marshal
                            (try_begin), # a special case to end long-running feasts
                              (eq, ":troop_no", "trp_player"),
                              
                              (eq, ":current_ai_state", sfai_feast),
                              (ge, ":hours_at_current_state", 72),
                              
                              (assign, ":action", sfai_default),
                              (assign, ":object", -1),
                              
                              #Normally you are not supposed to set permanent values in this state, but this is a special case to end player-called feasts
                              (assign, "$player_marshal_ai_state", sfai_default),
                              (assign, "$player_marshal_ai_object", -1),
                            (else_try), #another special state, to make player-called feasts last for a while when the player is the leader of the faction, but not the marshal
                              (eq, "$players_kingdom", "fac_player_supporters_faction"),
                              (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
                              (neq, ":troop_no", "trp_player"),
                              
                              (eq, ":current_ai_state", sfai_feast),
                              (le, ":hours_at_current_state", 48),
                              
                              (party_slot_eq, ":current_ai_object", slot_town_lord, "trp_player"),
                              (store_faction_of_party, ":current_ai_object_faction", ":current_ai_object"),
                              (eq, ":current_ai_object_faction", "$players_kingdom"),
                              
                              (assign, ":action", sfai_feast),
                              (assign, ":object", ":current_ai_object"),
                              
                              
                            (else_try), #this is the main player marshal state
                              (eq, ":troop_no", "trp_player"),
                              
                              (str_clear, s14),
                              (assign, ":action", "$player_marshal_ai_state"),
                              (assign, ":object", "$player_marshal_ai_object"),
                              
                              #1-RESTING IF NEEDED
                              #If not currently attacking a besieging a center and vassals did not rest for long time, let them rest.
                              #If we do not take this part to toppest level, tired vassals already did not accept any order, so that
                              #faction cannot do anything already. So first let vassals rest if they need. Thats why it should be toppest.
                            (else_try),
                              (neq, ":current_ai_state", sfai_default),
                              (neq, ":current_ai_state", sfai_feast),
                              (party_is_active, ":marshal_party"),
                              
                              (party_slot_eq, ":marshal_party", slot_party_ai_state, spai_retreating_to_center),
                              
                              (assign, ":action", sfai_default),
                              (assign, ":object", -1),
                              (str_store_string, s14, "str_the_enemy_temporarily_has_the_field"),
                              
                            (else_try),
                              (neq, ":current_ai_state", sfai_feast),
                              
                              (assign, ":currently_besieging", 0),
                              (try_begin),
                                (eq, ":current_ai_state", sfai_attacking_center),
                                (is_between, ":current_ai_object", walled_centers_begin, walled_centers_end),
                                (party_get_slot, ":besieger_party", ":current_ai_object", slot_center_is_besieged_by),
                                (party_is_active, ":besieger_party"),
                                (store_faction_of_party, ":besieger_faction", ":besieger_party"),
                                (eq, ":besieger_faction", ":faction_no"),
                                (assign, ":currently_besieging", 1),
                              (try_end),
                              
                              (assign, ":currently_defending_center", 0),
                              (try_begin),
                                (eq, ":current_ai_state", sfai_attacking_enemies_around_center),
                                (gt, ":marshal_party", 0),
                                (party_is_active, ":marshal_party"),
                                
                                (assign, ":besieged_center", -1),
                                (try_begin),
                                  (party_slot_eq, ":marshal_party", slot_party_ai_state, spai_holding_center), #if commander is holding a center
                                  (party_get_slot, ":marshal_object", ":marshal_party", slot_party_ai_object), #get commander's ai object (center they are holding)
                                  (party_get_battle_opponent, ":besieger_enemy", ":marshal_object"), #get this object's battle opponent
                                  (ge, ":besieger_enemy", 0),
                                  (assign, ":besieged_center", ":marshal_object"),
                                (else_try),
                                  (party_slot_eq, ":marshal_party", slot_party_ai_state, spai_engaging_army), #if commander is engaging an army
                                  (party_get_slot, ":marshal_object", ":marshal_party", slot_party_ai_object), #get commander's ai object (army which they engaded)
                                  (ge, ":marshal_object", 0), #if commander has an object
                                  (neg|is_between, ":marshal_object", centers_begin, centers_end), #if this object is not a center, so it is a party
                                  (party_is_active, ":marshal_object"),
                                  (party_get_battle_opponent, ":besieged_center", ":marshal_object"), #get this object's battle opponent
                                (try_end),
                                
                                (eq, ":besieged_center", ":current_ai_object"),
                                (assign, ":currently_defending_center", 1),
                              (try_end),
                              
                              (eq, ":currently_besieging", 0),
                              (eq, ":currently_defending_center", 0),
                              (ge, ":hours_since_last_faction_rest", 1240),
                              
                              (assign, ":action", sfai_default),
                              (assign, ":object", -1),
                              (str_store_string, s14, "str_the_vassals_are_tired_we_let_them_rest_for_some_time"),
                              
                              #2-DEFENSIVE ACTIONS : GATHERING ARMY FOR DEFENDING
                            (else_try),
                              (party_is_active, ":marshal_party"),
                              (eq, ":at_peace_with_everyone", 0),
                              
                              (is_between, ":most_threatened_center", centers_begin, centers_end),
                              (this_or_next|eq, ":current_ai_state", sfai_default),    #MOTO not going to attack anyway 
							  (this_or_next|eq, ":current_ai_state", sfai_feast),    #MOTO not going to attack anyway (THIS is the emergency to stop feast) 
            				  (gt, ":threat_danger_level", ":target_value_level"),
                              
                              (assign, ":continue_gathering", 0),
                              (assign, ":start_gathering", 0),
                              
                              (try_begin),
                                (is_between, ":most_threatened_center", villages_begin, villages_end),
                                
                                (assign, ":continue_gathering", 0),
                              (else_try),
                                (try_begin),
                                  (lt, ":hours_since_days_defensive_started", 3),
                                  (assign, ":multiplier", 150),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 6),
                                  (assign, ":multiplier", 140),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 9),
                                  (assign, ":multiplier", 132),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 12),
                                  (assign, ":multiplier", 124),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 15),
                                  (assign, ":multiplier", 118),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 18),
                                  (assign, ":multiplier", 114),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 21),
                                  (assign, ":multiplier", 110),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 24),
                                  (assign, ":multiplier", 106),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 27),
                                  (assign, ":multiplier", 102),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 31),
                                  (assign, ":multiplier", 98),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 34),
                                  (assign, ":multiplier", 94),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 37),
                                  (assign, ":multiplier", 90),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 40),
                                  (assign, ":multiplier", 86),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 43),
                                  (assign, ":multiplier", 82),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 46),
                                  (assign, ":multiplier", 79),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 49),
                                  (assign, ":multiplier", 76),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 52),
                                  (assign, ":multiplier", 73),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 56),
                                  (assign, ":multiplier", 70),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 60),
                                  (assign, ":multiplier", 68),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 66),
                                  (assign, ":multiplier", 66),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 72),
                                  (assign, ":multiplier", 64),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 80),
                                  (assign, ":multiplier", 62),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 90),
                                  (assign, ":multiplier", 60),
                                (else_try),
                                  (lt, ":hours_since_days_defensive_started", 100),
                                  (assign, ":multiplier", 58),
                                (else_try),
                                  (assign, ":multiplier", 56),
                                (try_end),
                                
                                (store_mul, ":enemy_strength_multiplied", ":enemy_strength_near_most_threatened_center", ":multiplier"),
                                (val_div, ":enemy_strength_multiplied", 100),
                                
                                (try_begin),
                                  (lt, ":marshal_party_strength", ":enemy_strength_multiplied"),
                                  (assign, ":continue_gathering", 1),
                                (try_end),
                              (else_try),
                                (eq, ":current_ai_state", sfai_attacking_enemies_around_center),
                                (neq, ":most_threatened_center", ":current_ai_object"),
                                
                                (assign, ":marshal_is_already_defending_a_center", 0),
                                (try_begin),
                                  (gt, ":marshal_party", 0),
                                  (party_is_active, ":marshal_party"),
                                  
                                  (assign, ":besieged_center", -1),
                                  (try_begin),
                                    (party_slot_eq, ":marshal_party", slot_party_ai_state, spai_holding_center), #if commander is holding a center
                                    (party_get_slot, ":marshal_object", ":marshal_party", slot_party_ai_object), #get commander's ai object (center they are holding)
                                    (party_get_battle_opponent, ":besieger_enemy", ":marshal_object"), #get this object's battle opponent
                                    (ge, ":besieger_enemy", 0),
                                    (assign, ":besieged_center", ":marshal_object"),
                                  (else_try),
                                    (party_slot_eq, ":marshal_party", slot_party_ai_state, spai_engaging_army), #if commander is engaging an army
                                    (party_get_slot, ":marshal_object", ":marshal_party", slot_party_ai_object), #get commander's ai object (army which they engaded)
                                    (ge, ":marshal_object", 0), #if commander has an object
                                    (neg|is_between, ":marshal_object", centers_begin, centers_end), #if this object is not a center, so it is a party
                                    (party_is_active, ":marshal_object"),
                                    (party_get_battle_opponent, ":besieged_center", ":marshal_object"), #get this object's battle opponent
                                  (try_end),
                                  
                                  (eq, ":besieged_center", ":current_ai_object"),
                                  
                                  (assign, ":marshal_is_already_defending_a_center", 1),
                                (try_end),
                                
                                (eq, ":marshal_is_already_defending_a_center", 0),
                                
                                (store_mul, ":enemy_strength_multiplied", ":enemy_strength_near_most_threatened_center", 80),
                                (val_div, ":enemy_strength_multiplied", 100),
                                (lt, ":marshal_party_strength", ":enemy_strength_multiplied"),
                                
                                (this_or_next|is_between, ":most_threatened_center", walled_centers_begin, walled_centers_end),
                                (neq, ":faction_no", "$players_kingdom"),
                                
                                (assign, ":start_gathering", 1),
                              (try_end),
                              
                              (this_or_next|eq, ":continue_gathering", 1),
                              (eq, ":start_gathering", 1),
                              
                              (assign, ":action", sfai_gathering_army),
                              (assign, ":object", -1),
                              (str_store_party_name, s21, ":most_threatened_center"),
                              (str_store_string, s14, "str_we_should_prepare_to_defend_s21_but_we_should_gather_our_forces_until_we_are_strong_enough_to_engage_them"),
                              
                              (try_begin),
                                (eq, ":faction_no", "$players_kingdom"),
                                (assign, "$g_gathering_reason", ":most_threatened_center"),
                              (try_end),
                              
                              #3-DEFENSIVE ACTIONS : RIDE TO BREAK ENEMY SIEGE / DEFEAT ENEMIES NEAR OUR CENTER
                            (else_try),
                              (party_is_active, ":marshal_party"),
                              (is_between, ":most_threatened_center", walled_centers_begin, walled_centers_end),
                              (this_or_next|eq, ":current_ai_state", sfai_default),    #MOTO not going to attack anyway 
							  (this_or_next|eq, ":current_ai_state", sfai_feast),    #MOTO not going to attack anyway (THIS is the emergency to stop feast) 
            				  (ge, ":threat_danger_level", ":target_value_level"),
                              (party_slot_ge, ":most_threatened_center", slot_center_is_besieged_by, 0),
                              
                              (assign, ":action", sfai_attacking_enemies_around_center),
                              (assign, ":object", ":most_threatened_center"),
                              
                              (str_store_party_name, s21, ":most_threatened_center"),
                              (str_store_string, s14, "str_we_should_ride_to_break_the_siege_of_s21"),
                              
                              #3b - DEFEAT ENEMIES NEAR CENTER - similar to above, but a different string
                            (else_try),
                              (party_is_active, ":marshal_party"),
                              (this_or_next|eq, ":current_ai_state", sfai_default),    #MOTO not going to attack anyway 
							  (this_or_next|eq, ":current_ai_state", sfai_feast),    #MOTO not going to attack anyway (THIS is the emergency to stop feast) 
          					  (ge, ":threat_danger_level", ":target_value_level"),
                              (is_between, ":most_threatened_center", villages_begin, villages_end),
                              
                              (assign, ":action", sfai_attacking_enemies_around_center),
                              (assign, ":object", ":most_threatened_center"),
                              (str_store_party_name, s21, ":most_threatened_center"),
                              (str_store_string, s14, "str_we_should_ride_to_defeat_the_enemy_gathered_near_s21"),
                              
                              #4-DEMOBILIZATION
                              #Let vassals attend their own business
                            (else_try),
                              (this_or_next|eq, ":current_ai_state", sfai_gathering_army),
                              (this_or_next|eq, ":current_ai_state", sfai_attacking_center),
                              (eq, ":current_ai_state", sfai_raiding_village),
                              
                              (ge, ":hours_since_last_faction_rest", ":campaign_hour_limit"), #Effected by ratio of vassals
                              (ge, ":hours_at_current_state", 24),
                              
                              #Ozan : I am adding some codes here because sometimes armies demobilize during last seconds of an important event like taking a castle, ext.
                              (assign, ":there_is_an_important_situation", 0),
                              (try_begin), #do not demobilize during taking a castle/town (fighting in the castle)
                                (is_between, ":current_ai_object", walled_centers_begin, walled_centers_end),
                                (party_get_battle_opponent, ":besieger_party", ":current_ai_object"),
                                (party_is_active, ":besieger_party"),
                                (store_faction_of_party, ":besieger_faction", ":besieger_party"),
                                (this_or_next|eq, ":besieger_faction", ":faction_no"),
                                (eq, ":besieger_faction", "fac_player_faction"),
                                (assign, ":there_is_an_important_situation", 1),
                              (else_try), #do not demobilize during besieging a siege (holding around castle)
                                (is_between, ":current_ai_object", walled_centers_begin, walled_centers_end),
                                (party_get_slot, ":besieger_party", ":current_ai_object", slot_center_is_besieged_by),
                                (party_is_active, ":besieger_party"),
                                (store_faction_of_party, ":besieger_faction", ":besieger_party"),
                                (this_or_next|eq, ":besieger_faction", ":faction_no"),
                                (eq, ":besieger_faction", "fac_player_faction"),
                                (assign, ":there_is_an_important_situation", 1),
                              (else_try), #do not demobilize during raiding a village (holding around village)
                                (is_between, ":current_ai_object", centers_begin, centers_end),
                                (neg|is_between, ":current_ai_object", walled_centers_begin, walled_centers_end),
                                (party_slot_eq, ":current_ai_object", slot_village_state, svs_being_raided),
                                (assign, ":there_is_an_important_situation", 1),
                              (try_end),
                              
                              (eq, ":there_is_an_important_situation", 0),
                              #end addition ozan
                              
                              (assign, reg7, ":hours_since_last_faction_rest"),
                              (assign, reg8, ":campaign_hour_limit"),
                              
                              (str_store_string, s14, "str_this_offensive_needs_to_wind_down_soon_so_the_vassals_can_attend_to_their_own_business"),
                              (assign, ":action", sfai_default),
                              (assign, ":object", -1),
                              
                              #6-GATHERING BECAUSE OF NO REASON
                              #Start to gather the army
                            (else_try),
                              (party_is_active, ":marshal_party"),
                              (eq, ":at_peace_with_everyone", 0),
                              
                              
                              (eq, ":current_ai_state", sfai_default),
                              (ge, ":hours_since_last_offensive", 60),
                              (lt, ":hours_since_last_faction_rest", 120),
                              
                              #There should not be a center as a precondition for attack
                              #Otherwise, we are unlikely to have a situation in which the army gathers, but does nothing -- which is important to have for role-playing purposes
                              
                              (assign, ":action", sfai_gathering_army),
                              (assign, ":object", -1),
                              (str_store_string, s14, "str_it_is_time_to_go_on_the_offensive_and_we_must_first_assemble_the_army"),
                              
                              (try_begin),
                                (eq, ":faction_no", "$players_kingdom"),
                                (assign, "$g_gathering_reason", -1),
                              (try_end),
                              
                              #7-OFFENSIVE ACTIONS : CONTINUE GATHERING
                            (else_try),
                              (party_is_active, ":marshal_party"),
                              (eq, ":current_ai_state", sfai_gathering_army),
                              (eq, ":at_peace_with_everyone", 0),
                              
                              (lt, ":hours_at_current_state", 54), #gather army for 54 hours
                              
                              (lt, ":ratio_of_vassals_assembled", 12),
                              
                              (str_store_string, s14, "str_we_must_continue_to_gather_the_army_before_we_ride_forth_on_an_offensive_operation"),
                              (assign, ":action", sfai_gathering_army),
                              (assign, ":object", -1),
                              
                              #7-OFFENSIVE ACTIONS PART 2 : CONTINUE GATHERING
                            (else_try),
                              (assign, ":minimum_possible_attackable_target_value_level", 50),
                              (eq, ":at_peace_with_everyone", 0),
                              
							 (try_begin), #agressive marshal
								  ##diplomacy start+
								  ##OLD:
								  #(troop_get_slot, ":reputation", ":troop_no", slot_lord_reputation_type),
								  #(this_or_next|eq, ":reputation", lrep_martial),
								  #(this_or_next|eq, ":reputation", lrep_quarrelsome),
								  #(eq, ":reputation", lrep_selfrighteous),
								  ##NEW:
								  (call_script, "script_dplmc_store_troop_personality_caution_level", ":troop_no"),
								  (lt, reg0, 0),
								  ##diplomacy end+
								  (val_mul, ":minimum_possible_attackable_target_value_level", 9),
								  (val_div, ":minimum_possible_attackable_target_value_level", 10),
							(try_end),
                              
                              (party_is_active, ":marshal_party"),
                              (eq, ":current_ai_state", sfai_gathering_army),
                              
                              (try_begin),
                                (lt, ":hours_at_current_state", 6),
                                (assign, ":minimum_needed_target_value_level", 1500),
                              (else_try),
                                (lt, ":hours_at_current_state", 10),
                                (assign, ":minimum_needed_target_value_level", 1000),
                              (else_try),
                                (lt, ":hours_at_current_state", 14),
                                (assign, ":minimum_needed_target_value_level", 720),
                              (else_try),
                                (lt, ":hours_at_current_state", 18),
                                (assign, ":minimum_needed_target_value_level", 480),
                              (else_try),
                                (lt, ":hours_at_current_state", 22),
                                (assign, ":minimum_needed_target_value_level", 360),
                              (else_try),
                                (lt, ":hours_at_current_state", 26),
                                (assign, ":minimum_needed_target_value_level", 240),
                              (else_try),
                                (lt, ":hours_at_current_state", 30),
                                (assign, ":minimum_needed_target_value_level", 180),
                              (else_try),
                                (lt, ":hours_at_current_state", 34),
                                (assign, ":minimum_needed_target_value_level", 120),
                              (else_try),
                                (lt, ":hours_at_current_state", 38),
                                (assign, ":minimum_needed_target_value_level", 100),
                              (else_try),
                                (lt, ":hours_at_current_state", 42),
                                (assign, ":minimum_needed_target_value_level", 80),
                              (else_try),
                                (lt, ":hours_at_current_state", 46),
                                (assign, ":minimum_needed_target_value_level", 65),
                              (else_try),
                                (lt, ":hours_at_current_state", 50),
                                (assign, ":minimum_needed_target_value_level", 55),
                              (else_try),
                                (assign, ":minimum_needed_target_value_level", ":minimum_possible_attackable_target_value_level"),
                              (try_end),
                              
							(try_begin), #agressive marshal
							  ##diplomacy start+
							  ##OLD:
							  #(troop_get_slot, ":reputation", ":troop_no", slot_lord_reputation_type),
							  #(this_or_next|eq, ":reputation", lrep_martial),
							  #(this_or_next|eq, ":reputation", lrep_quarrelsome),
							  #(eq, ":reputation", lrep_selfrighteous),
							  ##NEW:
							  (call_script, "script_dplmc_store_troop_personality_caution_level", ":troop_no"),
							  (lt, reg0, 0),
							  ##diplomacy end+
							  (val_mul, ":minimum_needed_target_value_level", 9),
							  (val_div, ":minimum_needed_target_value_level", 10),
							(try_end),
                              
                              (le, ":target_value_level", ":minimum_needed_target_value_level"),
                              (le, ":hours_at_current_state", 54),
                              
                              (str_store_string, s14, "str_we_have_assembled_some_vassals"),
                              (assign, ":action", sfai_gathering_army),
                              (assign, ":object", -1),
                              
                              #8-ATTACK AN ENEMY CENTER case 1, reconnaissance against walled center
                              #(else_try),
                              #(party_is_active, ":marshal_party"),
                              #(neq, ":current_ai_state", sfai_default),
                              #(neq, ":current_ai_state", sfai_feast),
                              #(is_between, ":center_to_attack", walled_centers_begin, walled_centers_end),
                              
                              #(store_sub, ":faction_recce_slot", ":faction_no", kingdoms_begin),
                              #(val_add, ":faction_recce_slot", slot_center_last_reconnoitered_by_faction_time),
                              #(store_current_hours, ":hours_since_last_recon"),
                              #(party_get_slot, ":last_recon_time", ":center_to_attack", ":faction_recce_slot"),
                              #(val_sub, ":hours_since_last_recon", ":last_recon_time"),
                              #(this_or_next|eq, ":last_recon_time", 0),
                              #(gt, ":hours_since_last_recon", 96),
                              
                              #(assign, ":action", sfai_attacking_center),
                              #(assign, ":object", ":center_to_attack"),
                              #(str_store_string, s14, "str_we_are_conducting_recce"),
                              
                              #8-ATTACK AN ENEMY CENTER case 2, reconnaissance against village
                              #(else_try),
                              #(party_is_active, ":marshal_party"),
                              #(neq, ":current_ai_state", sfai_default),
                              #(neq, ":current_ai_state", sfai_feast),
                              #(is_between, ":center_to_attack", villages_begin, villages_end),
                              
                              #(store_sub, ":faction_recce_slot", ":faction_no", kingdoms_begin),
                              #(val_add, ":faction_recce_slot", slot_center_last_reconnoitered_by_faction_time),
                              #(store_current_hours, ":hours_since_last_recon"),
                              #(party_get_slot, ":last_recon_time", ":center_to_attack", ":faction_recce_slot"),
                              #(val_sub, ":hours_since_last_recon", ":last_recon_time"),
                              #(this_or_next|eq, ":last_recon_time", 0),
                              #(gt, ":hours_since_last_recon", 96),
                              
                              
                              #(assign, ":action", sfai_raiding_village),
                              #(assign, ":object", ":center_to_attack"),
                              #(str_store_string, s14, "str_we_are_conducting_recce"),
                            (else_try),
                              (party_is_active, ":marshal_party"),
                              (neq, ":current_ai_state", sfai_default),
                              (neq, ":current_ai_state", sfai_feast),
                              
                              (assign, ":center_to_attack", ":center_to_attack_only_marshal_and_followers"),
                              
                              (is_between, ":center_to_attack", walled_centers_begin, walled_centers_end),
                              
                              (ge, ":target_value_level", ":minimum_possible_attackable_target_value_level"),
                              
                              (assign, ":action", sfai_attacking_center),
                              (assign, ":object", ":center_to_attack"),
                              (str_store_string, s14, "str_we_believe_the_fortress_will_be_worth_the_effort_to_take_it"),
                            (else_try),
                              (party_is_active, ":marshal_party"),
                              (neq, ":current_ai_state", sfai_default),
                              (neq, ":current_ai_state", sfai_feast),
                              
                              (assign, ":center_to_attack", ":center_to_attack_only_marshal_and_followers"),
                              
                              (is_between, ":center_to_attack", villages_begin, villages_end),
                              
                              (ge, ":target_value_level", ":minimum_possible_attackable_target_value_level"),
                              
                              (assign, ":action", sfai_raiding_village),
                              (assign, ":object", ":center_to_attack"),
                              (str_store_string, s14, "str_we_shall_leave_a_fiery_trail_through_the_heart_of_the_enemys_lands_targeting_the_wealthy_settlements_if_we_can"),
                              
                              #9 -- DISBAND THE ARMY
                            (else_try),
                              (eq, ":current_ai_state", sfai_gathering_army),
                              
                              (str_store_string, s14, "str_the_army_will_be_disbanded_because_we_have_been_waiting_too_long_without_a_target"),
                              
                              (assign, ":action", sfai_default),
                              (assign, ":object", -1),
                              #OFFENSIVE OPERATIONS END
                              
                              #FEAST-RELATED OPERATIONS BEGIN
                              #10-CONCLUDE CURRENT FEAST
                            (else_try),
                              (eq, ":current_ai_state", sfai_feast),
                              (gt, ":hours_at_current_state", 72),
                              
                              (assign, ":action", sfai_default),
                              (assign, ":object", -1),
                              (str_store_string, s14, "str_it_is_time_for_the_feast_to_conclude"),
                              
                              #11-CONTINE FEAST UNLESS THERE IS AN EMERGENCY
                            (else_try),
                              (eq, ":current_ai_state", sfai_feast),
                              (le, ":hours_at_current_state", 72),
                              
                              (assign, ":action", sfai_feast),
                              (assign, ":object", ":current_ai_object"),
                              (str_store_string, s14, "str_we_should_continue_the_feast_unless_there_is_an_emergency"),
                              
                              #12-HOLD A FEAST BECAUSE THE PLAYER WANTS TO ORGANIZE ONE
                            (else_try),
                              (check_quest_active, "qst_organize_feast"),
                              (eq, "$players_kingdom", ":faction_no"),
                              
                              (quest_get_slot, ":target_center", "qst_organize_feast", slot_quest_target_center),
                              
                              (assign, ":action", sfai_feast),
                              (assign, ":object", ":target_center"),
                              (str_store_string, s14, "str_you_had_wished_to_hold_a_feast"),
                              
                              #13-HOLD A FEAST BECAUSE FEMALE PLAYER SCHEDULED TO GET MARRIED
                            (else_try),
                              (check_quest_active, "qst_wed_betrothed_female"),
                              
                              (quest_get_slot, ":groom", "qst_wed_betrothed_female", slot_quest_giver_troop),
                              (troop_slot_eq, ":groom", slot_troop_prisoner_of_party, -1),
                              
                              (store_faction_of_troop, ":groom_faction", ":groom"),
                              (eq, ":groom_faction", ":faction_no"),
                              
                              (faction_get_slot, ":faction_leader", ":groom_faction", slot_faction_leader),
                              
                              (assign, ":location_feast", -1),
                              (try_for_range, ":possible_location", walled_centers_begin, walled_centers_end),
                                (eq, ":location_feast", -1),
                                (party_slot_eq, ":possible_location", slot_town_lord, ":groom"),
                                (party_slot_ge, ":possible_location", slot_center_is_besieged_by, 0),
                                (assign, ":location_feast", ":possible_location"),
                              (try_end),
                              
                              (try_for_range, ":possible_location", walled_centers_begin, walled_centers_end),
                                (eq, ":location_feast", -1),
                                (party_slot_eq, ":possible_location", slot_town_lord, ":faction_leader"),
                                (party_slot_ge, ":possible_location", slot_center_is_besieged_by, 0),
                                (assign, ":location_feast", ":possible_location"),
                              (try_end),
                              
                              (is_between, ":location_feast", walled_centers_begin, walled_centers_end),
                              
                              (assign, ":action", sfai_feast),
                              (assign, ":object", ":location_feast"),
                              (str_store_string, s14, "str_your_wedding_day_approaches_my_lady"),
                              
                              #14-HOLD A FEAST BECAUSE A MALE CHARACTER WANTS TO GET MARRIED
                            (else_try),
                              (check_quest_active, "qst_wed_betrothed"),
                              (neg|quest_slot_ge, "qst_wed_betrothed", slot_quest_expiration_days, 362),
                              
                              (quest_get_slot, ":bride", "qst_wed_betrothed", slot_quest_target_troop),
                              (call_script, "script_get_kingdom_lady_social_determinants", ":bride"),
                              (assign, ":feast_host", reg0),
                              (store_faction_of_troop, ":feast_host_faction", ":feast_host"),
                              (eq, ":feast_host_faction", ":faction_no"),
                              
                              (troop_slot_eq, ":feast_host", slot_troop_prisoner_of_party, -1),
                              (assign, ":wedding_venue", reg1),
                              
                              (is_between, ":wedding_venue", centers_begin, centers_end),
                              (party_slot_eq, ":wedding_venue", slot_center_is_besieged_by, -1),
                              
                              (assign, ":action", sfai_feast),
                              (assign, ":object", ":wedding_venue"),
                              (str_store_string, s14, "str_your_wedding_day_approaches"),
                              
                              #15-HOLD A FEAST BECAUSE AN NPC WANTS TO GET MARRIED
                            (else_try),
                              (ge, ":hours_since_last_feast_start", 192), #If at least eight days past last feast start time
                              
                              (assign, ":location_feast", -1),
                              
                              (try_for_range, ":kingdom_lady", kingdom_ladies_begin, kingdom_ladies_end),
                                (troop_get_slot, ":groom", ":kingdom_lady", slot_troop_betrothed),
                                (gt, ":groom", 0), #not the player
                                
                                (store_faction_of_troop, ":lady_faction", ":kingdom_lady"),
                                (store_faction_of_troop, ":groom_faction", ":groom"),
                                
                                (try_begin), #The groom checks if he wants to continue or break off relations. This causes actions, rather than just returns a value, so it probably should be moved elsewhere
                                  (troop_slot_ge, ":groom", slot_troop_prisoner_of_party, 0),
                                (else_try),
                                  (neq, ":groom_faction", ":lady_faction"),
                                  (neq, ":groom_faction", "fac_player_faction"),
                                  (call_script, "script_courtship_event_lady_break_relation_with_suitor", ":kingdom_lady", ":groom"),
								(else_try),
									(eq, ":lady_faction", ":faction_no"),
									##diplomacy start+
									#neither the bride nor the groom is in retirement, dead, etc.
									(neg|troop_slot_ge, ":groom", slot_troop_occupation, slto_retirement),
									(neg|troop_slot_ge, ":kingdom_lady", slot_troop_occupation, slto_retirement), #Floris - Bugfix (was ":bride" but that variable doesn't hold a meaningful value here)
									##diplomacy end+
									(store_current_hours, ":hours_since_betrothal"),
									(troop_get_slot, ":betrothal_time", ":kingdom_lady", slot_troop_betrothal_time),
									(val_sub, ":hours_since_betrothal", ":betrothal_time"),
									(ge, ":hours_since_betrothal", 719), #30 days
                                  
                                  (call_script, "script_get_kingdom_lady_social_determinants", ":kingdom_lady"),
                                  (assign, ":wedding_venue", reg1),
                                  
                                  (assign, ":location_feast", ":wedding_venue"),
                                  (assign, ":final_bride", ":kingdom_lady"),
                                  (assign, ":final_groom", ":groom"),
                                (try_end),
                              (try_end),
                              
                              (ge, ":location_feast", centers_begin),
                              
                              (assign, ":action", sfai_feast),
                              (assign, ":object", ":location_feast"),
                              
                              (str_store_troop_name, s22, ":final_bride"),
                              (str_store_troop_name, s23, ":final_groom"),
                              (str_store_string, s14, "str_s22_and_s23_wish_to_marry"),
                              
                              #16-HOLD A FEAST ANYWAY
                            (else_try),
                              (eq, ":current_ai_state", sfai_default),
                              (gt, ":hours_since_last_feast_start", 240), #If at least 10 days past after last feast. (added by ozan)
                              
                              (assign, ":location_high_score", 0),
                              (assign, ":location_feast", -1),
                              
                              (try_for_range, ":location", walled_centers_begin, walled_centers_end),
                                (store_faction_of_party, ":location_faction", ":location"),
                                (eq, ":location_faction", ":faction_no"),
                                
                                (try_begin),
                                  (neg|party_slot_eq, ":location", slot_village_state, svs_under_siege),
                                  (party_get_slot, ":location_lord", ":location", slot_town_lord),
                                  (is_between, ":location_lord", active_npcs_begin, active_npcs_end),
                                  (troop_get_slot, ":location_score", ":location_lord", slot_troop_renown),
                                  (store_random_in_range, ":random", 0, 1000), #will probably be king or senior lord
                                  (val_add, ":location_score", ":random"),
                                  (gt, ":location_score", ":location_high_score"),
                                  (assign, ":location_high_score", ":location_score"),
                                  (assign, ":location_feast", ":location"),
                                (else_try), #do not start new feasts if any place is under siege or being raided
                                  (this_or_next|party_slot_eq, ":location", slot_village_state, svs_under_siege),
                                  (party_slot_eq, ":location", slot_village_state, svs_being_raided),
                                  (assign, ":location_high_score", 9999),
                                  (assign, ":location_feast", -1),
                                (try_end),
                              (try_end),
                              
                              (is_between, ":location_feast", walled_centers_begin, walled_centers_end),
                              (party_get_slot, ":feast_host", ":location_feast", slot_town_lord),
                              (troop_slot_eq, ":feast_host", slot_troop_prisoner_of_party, -1),
                              
                              (assign, ":action", sfai_feast),
                              (assign, ":object", ":location_feast"),
                              (str_store_string, s14, "str_it_has_been_a_long_time_since_the_lords_of_the_realm_gathered_for_a_feast"),
                              
                              #17-DO NOTHING
                            (else_try),
                              (neq, ":current_ai_state", sfai_default),
                              
                              (assign, ":action", sfai_default),
                              (assign, ":object", -1),
                              (str_store_string, s14, "str_the_circumstances_which_led_to_this_decision_no_longer_apply_so_we_should_stop_and_reconsider_shortly"),
                              
                              #18-DO NOTHING
                            (else_try),
                              (eq, ":current_ai_state", sfai_default),
                              
                              (eq, ":at_peace_with_everyone", 1),
                              
                              (assign, ":action", sfai_default),
                              (assign, ":object", -1),
                              (str_store_string, s14, "str_we_are_currently_at_peace"),
                            (else_try),
                              (eq, ":current_ai_state", sfai_default),
                              (faction_slot_eq, ":faction_no", slot_faction_marshall, -1),
                              (assign, ":action", sfai_default),
                              (assign, ":object", -1),
                              (str_store_string, s14, "str_we_are_waiting_for_selection_of_marshal"),
                              
                            (else_try),
                              (eq, ":current_ai_state", sfai_default),
                              
                              (assign, ":action", sfai_default),
                              (assign, ":object", -1),
                              (str_store_string, s14, "str_the_vassals_still_need_time_to_attend_to_their_own_business"),
                            (try_end),
                            
                            (assign, reg0, ":action"),
                            (assign, reg1, ":object"),
                        ]),
                        
                        (
                          "faction_last_reconnoitered_center", #This is called from within decide_faction_ai, or from
                          [
                            (store_script_param, ":faction_no", 1),
                            (store_script_param, ":center_no", 2),
                            
                            (store_sub, ":faction_recce_slot", ":faction_no", kingdoms_begin),
                            (val_add, ":faction_recce_slot", slot_center_last_reconnoitered_by_faction_time),
                            (store_current_hours, ":hours_since_last_recon"),
                            (party_get_slot, ":last_recon_time", ":center_no", ":faction_recce_slot"),
                            
                            (try_begin),
                              (lt, ":last_recon_time", 1),
                              (assign, ":hours_since_last_recon", 1000),
                            (else_try),
                              (val_sub, ":hours_since_last_recon", ":last_recon_time"),
                            (try_end),
                            
                            (assign, reg0, ":hours_since_last_recon"),
                            (assign, reg1, ":last_recon_time"),
                        ]),
                        
                        (
                          "reduce_exact_number_to_estimate",
                          #This is used to simulate limited intelligence
                          #It is roughly analogous to the descriptive strings which the player will receive from alarms
                          #Information is presumed to be accurate for four days
                          #This is obviously cheating for the AI, as the AI will have exact info for four days, and no info at all after that.
                          #It would be fairly easy to log the strength at a center when it is scouted, if we want, but I have not done that at this point,
                          #The AI also has a hive mind -- ie, each party knows what its allies are thinking. In this, AI factions have an advantage over the player
                          #It would be a simple matter to create a set of arrays in which each party's knowledge is individually updated, but that would also take up a lot of data space
                          
                          [
                            (store_script_param, ":exact_number", 1),
                            
                            (try_begin),
                              (lt, ":exact_number", 500),
                              (assign, ":estimate", 0),
                            (else_try),
                              (lt, ":exact_number", 1000),
                              (assign, ":estimate", 750),
                            (else_try),
                              (lt, ":exact_number", 2000),
                              (assign, ":estimate", 1500),
                            (else_try),
                              (lt, ":exact_number", 4000),
                              (assign, ":estimate", 3000),
                            (else_try),
                              (lt, ":exact_number", 8000),
                              (assign, ":estimate", 6000),
                            (else_try),
                              (lt, ":exact_number", 16000),
                              (assign, ":estimate", 12000),
                            (else_try),
                              (assign, ":estimate", 24000),
                            (try_end),
							
							##diplomacy start+
							#This currently isn't used anywhere, but modify it if we're thinking about changing that.
							#Take into account campaign AI difficulty -- assume that the difference is either a good
							#spy network or intelligent inference.
							(game_get_reduce_campaign_ai, reg0),
							(try_begin),
								(lt, reg0, 1),#Hard mode
								(assign, ":estimate", ":exact_number"),
							(else_try),
								(eq, reg0, 1),#Medium Mode
								(val_add, ":estimate", ":exact_number"),
								(val_div, ":estimate", 2),
							(try_end),
							##diplomacy end+
                            
                            (assign, reg0, ":estimate"),
                        ]),
                        
                        #script_calculate_castle_prosperities_by_using_its_villages
                        (
                          "calculate_castle_prosperities_by_using_its_villages", #This is called from within decide_faction_ai, or from
                          [
                            (try_for_range, ":cur_castle", castles_begin, castles_end),
                              (assign, ":total_prosperity", 0),
                              (assign, ":total_villages", 0),
                              
                              (try_for_range, ":cur_village", villages_begin, villages_end),
                                (party_get_slot, ":bound_center", ":cur_village", slot_village_bound_center),
                                (eq, ":cur_castle", ":bound_center"),
                                
                                (party_get_slot, ":village_prosperity", ":cur_village", slot_town_prosperity),
                                
                                (val_add, ":total_prosperity", ":village_prosperity"),
                                (val_add, ":total_villages", 1),
                              (try_end),
                              
                              (try_begin),
							    (ge, ":total_villages", 1), # Bugfix - Windy - Preventing Div/0 errors.
                                (store_div, ":castle_prosperity", ":total_prosperity", ":total_villages"),
                              (else_try),
                                (assign, ":castle_prosperity", 50),
                              (try_end),
                              
                              (party_set_slot, ":cur_castle", slot_town_prosperity, ":castle_prosperity"),
                            (try_end),
                        ]),
                        
                        #script_initialize_tavern_variables
                        (
                          "initialize_tavern_variables",
                          [
                            (assign, "$g_main_attacker_agent", 0),
                            (assign, "$g_attacker_drawn_weapon", 0),
                            (assign, "$g_start_belligerent_drunk_fight", 0),
                            (assign, "$g_start_hired_assassin_fight", 0),
                            (assign, "$g_belligerent_drunk_leaving", 0),
                        ]),
                        
                        #script_prepare_alley_to_fight
                        (
                          "prepare_alley_to_fight",
                          [
                            (party_get_slot, ":scene_no", "$current_town", slot_town_alley),
                            
                            #(store_faction_of_party, ":faction_no", "$current_town"),
                            
                            (modify_visitors_at_site, ":scene_no"),
                            
                            (reset_visitors),
                            (set_visitor, 0, "trp_player"),
                            
                            #(try_begin),
                            #  (eq, ":faction_no", "fac_kingdom_1"), #swadian
                            #  (assign, ":bandit_troop", "trp_steppe_bandit"),
                            #(else_try),
                            #  (eq, ":faction_no", "fac_kingdom_2"), #vaegir
                            #  (assign, ":bandit_troop", "trp_taiga_bandit"),
                            #(else_try),
                            #  (eq, ":faction_no", "fac_kingdom_3"), #khergit
                            #  (assign, ":bandit_troop", "trp_mountain_bandit"),
                            #(else_try),
                            #  (eq, ":faction_no", "fac_kingdom_4"), #nord
                            #  (assign, ":bandit_troop", "trp_sea_raider"),
                            #(else_try),
                            #  (eq, ":faction_no", "fac_kingdom_5"), #rhodok
                            #  (assign, ":bandit_troop", "trp_forest_bandit"),
                            #(else_try),
                            #  (eq, ":faction_no", "fac_kingdom_6"), #sarradin
                            #  (assign, ":bandit_troop", "trp_desert_bandit"),
                            #(try_end),
                            
                            #(set_visitor, 3, ":bandit_troop"),
							##Floris MTT begin
							(troop_get_slot,":bandit_bandit","$troop_trees",slot_bandit_bandit),
                             (set_visitor, 3, ":bandit_bandit"),
							##Floris MTT end
                            
                            (assign, "$talked_with_merchant", 0),
                            (set_jump_mission, "mt_alley_fight"),
                            (jump_to_scene, ":scene_no"),
                            (change_screen_mission),
                        ]),
                        
                        #script_prepare_town_to_fight
                        (
                          "prepare_town_to_fight",
                          [
                            (str_store_party_name_link, s9, "$g_starting_town"),
                            (str_store_string, s2, "str_save_town_from_bandits"),
                            (call_script, "script_start_quest", "qst_save_town_from_bandits", "$g_talk_troop"),
                            
                            (assign, "$g_mt_mode", tcm_default),
                            (store_faction_of_party, ":town_faction", "$current_town"),
                            (faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_3_troop),
                            (faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
                            (faction_get_slot, ":tier_4_troop", ":town_faction", slot_faction_tier_4_troop),
                            
                            (party_get_slot, ":town_scene", "$current_town", slot_town_center),
                            (modify_visitors_at_site, ":town_scene"),
                            (reset_visitors),
                            
                            #people spawned at #32, #33, #34, #35, #36, #37, #38 and #39 are town walkers.
                            (try_begin),
                              #(eq, "$town_nighttime", 0),
                              (try_for_range, ":walker_no", 0, num_town_walkers),
                                (store_add, ":troop_slot", slot_center_walker_0_troop, ":walker_no"),
                                (party_get_slot, ":walker_troop_id", "$current_town", ":troop_slot"),
                                (gt, ":walker_troop_id", 0),
                                (store_add, ":entry_no", town_walker_entries_start, ":walker_no"),
                                (set_visitor, ":entry_no", ":walker_troop_id"),
                              (try_end),
                            (try_end),
                            
                            #guards will be spawned at #25, #26 and #27
                            (set_visitors, 25, ":tier_2_troop", 1),
                            (set_visitors, 26, ":tier_3_troop", 1),
                            (set_visitors, 27, ":tier_4_troop", 1),

							##Floris MTT begin
							(troop_get_slot,":bandit_looter","$troop_trees",slot_bandit_looter),
							(troop_get_slot,":bandit_bandit","$troop_trees",slot_bandit_bandit),
                             (set_visitors, 10, ":bandit_looter", 1),
                             (set_visitors, 11, ":bandit_bandit", 1),
                             (set_visitors, 12, ":bandit_looter", 1),
							##Floris MTT end
                            
                            (store_faction_of_party, ":starting_town_faction", "$g_starting_town"),
                            (try_begin),
                              (eq, ":starting_town_faction", "fac_kingdom_1"),
                              (assign, ":troop_of_merchant", "trp_swadian_merchant"),
                              #(assign, ":troop_of_bandit", "trp_forest_bandit"),
                            (else_try),
                              (eq, ":starting_town_faction", "fac_kingdom_2"),
                              (assign, ":troop_of_merchant", "trp_vaegir_merchant"),
                              #(assign, ":troop_of_bandit", "trp_mountain_bandit"),
                            (else_try),
                              (eq, ":starting_town_faction", "fac_kingdom_3"),
                              (assign, ":troop_of_merchant", "trp_khergit_merchant"),
                              #(assign, ":troop_of_bandit", "trp_steppe_bandit"),
                            (else_try),
                              (eq, ":starting_town_faction", "fac_kingdom_4"),
                              (assign, ":troop_of_merchant", "trp_nord_merchant"),
                              #(assign, ":troop_of_bandit", "trp_sea_raider"),
                            (else_try),
                              (eq, ":starting_town_faction", "fac_kingdom_5"),
                              (assign, ":troop_of_merchant", "trp_rhodok_merchant"),
                              #(assign, ":troop_of_bandit", "trp_mountain_bandit"),
                            (else_try),
                              (eq, ":starting_town_faction", "fac_kingdom_6"),
                              (assign, ":troop_of_merchant", "trp_sarranid_merchant"),
                              #(assign, ":troop_of_bandit", "trp_desert_bandit"),
                            (try_end),
                            (str_store_troop_name, s10, ":troop_of_merchant"),

							##Floris MTT begin
							(troop_get_slot,":bandit_looter","$troop_trees",slot_bandit_looter),
                             (set_visitors, 24, ":bandit_looter", 1),
                             (set_visitors, 2, ":bandit_looter", 2),
                             (set_visitors, 4, ":bandit_looter", 1),
                             (set_visitors, 5, ":bandit_looter", 2),
                             (set_visitors, 6, ":bandit_looter", 1),
                             (set_visitors, 7, ":bandit_looter", 1),
							##Floris MTT end
                            
                            (set_visitors, 3, ":troop_of_merchant", 1),
                            
                            (set_jump_mission,"mt_town_fight"),
                            (jump_to_scene, ":town_scene"),
                            (change_screen_mission),
                        ]),
                        
                        (
                          "change_player_right_to_rule",
                          [
                            (store_script_param_1, ":right_to_rule_dif"),
                            (val_add, "$player_right_to_rule", ":right_to_rule_dif"),
                            (val_clamp, "$player_right_to_rule", 0, 100),
                            (try_begin),
                              (gt, ":right_to_rule_dif", 0),
                              (display_message, "@You gain right to rule."),
                            (else_try),
                              (lt, ":right_to_rule_dif", 0),
                              (display_message, "@You lose right to rule."),
                            (try_end),
                        ]),
                        
                        ("indict_lord_for_treason",#originally included in simple_triggers. Needed to be moved here to allow player to indict
                          [
                            (store_script_param, ":troop_no", 1),
                            (store_script_param, ":faction", 2),
                            
							##diplomacy start+ use gender script
							#(troop_get_type, reg4, ":troop_no"),
							(assign, ":save_reg0", reg0),
							(assign, ":save_reg3", reg3),
							(assign, ":save_reg4", reg4),
							##diplomacy end+
                            
							(try_for_range, ":center", centers_begin, centers_end), #transfer properties to liege
								(party_slot_eq, ":center", slot_town_lord, ":troop_no"),
								(party_set_slot, ":center", slot_town_lord, stl_unassigned),
							(try_end),

							(faction_get_slot, ":faction_leader", ":faction", slot_faction_leader),
							(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
							(assign, ":liege_to_lord_relation", reg0),
							(store_sub, ":base_relation_modifier", -150, ":liege_to_lord_relation"),
							(val_div, ":base_relation_modifier", 40),#-1 at -100, -2 at -70, -3 at -30,etc.
							(val_min, ":base_relation_modifier", -1),
							
							#Indictments, cont: Influence relations
							##diplomacy start+ Alter to include promoted ladies
							##OLD:
							#(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end), #this effects all lords in all factions
							##NEW:
							(try_for_range, ":active_npc", heroes_begin, heroes_end), #this effects all lords in all factions
								(this_or_next|is_between, ":active_npc", active_npcs_begin, active_npcs_end),
									(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
							##diplomacy end+
								(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
								(eq, ":faction", ":active_npc_faction"),

								(call_script, "script_troop_get_family_relation_to_troop", ":troop_no", ":active_npc"),
								(assign, ":family_relation", reg0),

								##diplomacy start+
								(val_max, ":family_relation", 0),
								#Take into account friendship or enmity
								(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
								(assign, ":liking_relation", reg0),
								(try_begin),
									(ge, ":liking_relation", 20),
									(store_div, reg0, ":liking_relation", 20),
									(val_add, ":family_relation", reg0),
								(else_try),
									(lt, ":liking_relation", 0),
									(store_div, reg0, ":liking_relation", 20),
									(val_sub, reg0, 1),
									(val_add, ":family_relation", reg0),
								(try_end),
								(store_random_in_range, reg0, 0, 3),#+0, +1, or +2 (because below we divide by three...)
								(val_add, ":family_relation", reg0),
								(assign, reg0, ":family_relation"),
								##diplomacy end+
								(assign, ":relation_modifier", ":base_relation_modifier"),
								(try_begin),
									##diplomacy start+
									#(gt, ":family_relation", 1),##OLD
									(neq, ":family_relation", 0),##NEW (allow lessening penalty for hated characters)
									##diplomacy end+
									(store_div, ":family_multiplier", reg0, 3),
									(val_sub, ":relation_modifier", ":family_multiplier"),
								(try_end),

								(lt, ":relation_modifier", 0),

								(call_script, "script_troop_change_relation_with_troop", ":faction_leader", ":active_npc", ":relation_modifier"),
								(val_add, "$total_indictment_changes", ":relation_modifier"),
								(try_begin),
									(eq, "$cheat_mode", 1),
									(str_store_troop_name, s17, ":active_npc"),
									(str_store_troop_name, s18, ":faction_leader"),

									(assign, reg3, ":relation_modifier"),
									(display_message, "str_trial_influences_s17s_relation_with_s18_by_reg3"),
								(try_end),
							(try_end),
                            
                            #Indictments, cont: Check for other factions
                            (assign, ":new_faction", "fac_outlaws"),
                            (try_begin),
                              (eq, ":troop_no", "trp_player"),
                              (assign, ":new_faction", 0), #kicked out of faction
                            (else_try),
                              (call_script, "script_lord_find_alternative_faction", ":troop_no"),
                              (assign, ":new_faction", reg0),
                            (try_end),
                            
                            #Indictments, cont: Finalize where the lord goes
                            (try_begin),
                              (is_between, ":new_faction", kingdoms_begin, kingdoms_end),
                              ## Begin 1.134
                              (try_begin),
                                (ge, "$cheat_mode", 1),
                                (str_store_troop_name, s4, ":troop_no"),
                                (display_message, "@{!}DEBUG - {s4} faction changed in indictment"),
                              (try_end),
                              ## End 1.134
                              (call_script, "script_change_troop_faction", ":troop_no", ":new_faction"),
                              (try_begin), #new-begin
                                (neq, ":new_faction", "fac_player_supporters_faction"), ##1.134
                                (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive),
                                (troop_set_slot, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
                              (try_end), #new-end
                              (str_store_faction_name, s10, ":new_faction"),
                              (str_store_string, s11, "str_with_the_s10"),
							(else_try),
								(neq, ":troop_no", "trp_player"),
								##diplomacy start+
								#Set "exile" occupation to differentiate between someone outside of Calradia
								#and an outlaw lord leading a party of bandits.
								(troop_set_slot, ":troop_no", slot_troop_occupation, dplmc_slto_exile),
								##diplomacy end+
								(call_script, "script_change_troop_faction", ":troop_no", "fac_outlaws"),
								(str_store_string, s11, "str_outside_calradia"),
							(else_try),
								(eq, ":troop_no", "trp_player"),
								(call_script, "script_player_leave_faction", 1),
							(try_end),

							#Indictments, cont: Set up string
							(try_begin),
								(eq, ":troop_no", "trp_player"),
								(str_store_string, s9, "str_you_have_been_indicted_for_treason_to_s7_your_properties_have_been_confiscated_and_you_would_be_well_advised_to_flee_for_your_life"),
							(else_try),
								(str_store_troop_name, s4, ":troop_no"),
								(str_store_faction_name, s5, ":faction"),
								(str_store_troop_name, s6, ":faction_leader"),

								##diplomacy start+
								#(troop_get_type, reg4, ":troop_no"),
								(call_script, "script_dplmc_store_troop_is_female", ":troop_no"),
								(assign, reg4, reg0),
								##diplomacy end+
								(str_store_string, s9, "str_by_order_of_s6_s4_of_the_s5_has_been_indicted_for_treason_the_lord_has_been_stripped_of_all_reg4herhis_properties_and_has_fled_for_reg4herhis_life_he_is_rumored_to_have_gone_into_exile_s11"),
							(try_end),
							##diplomacy start+ important political events should be in the log
							(display_log_message, "@{!}{s9}"),#display_message changed to display_log_message
							##diplomacy end+

							#Indictments, cont: Remove party
							(troop_get_slot, ":led_party", ":troop_no", slot_troop_leaded_party),
							(try_begin),
								(party_is_active, ":led_party"),
								(neq, ":led_party", "p_main_party"),
								(remove_party, ":led_party"),
								(troop_set_slot, ":troop_no", slot_troop_leaded_party, -1),
							(try_end),

							(try_begin),
								(eq, "$cheat_mode", 1),
								##diplomacy start+
								(this_or_next|eq, ":faction", "fac_player_supporters_faction"),
								(this_or_next|eq, ":new_faction", "fac_player_supporters_faction"),
								##diplomacy end+
								(this_or_next|eq, ":faction", "$players_kingdom"),
									(eq, ":new_faction", "$players_kingdom"),
								(call_script, "script_add_notification_menu", "mnu_notification_treason_indictment", ":troop_no", ":faction"),
							(try_end),
							##diplomacy start+
							(assign, reg0, ":save_reg0"),
							(assign, reg3, ":save_reg3"),
							(assign, reg4, ":save_reg4"),
							##diplomacy end+
						   ]),
                        
                        
                        # script_give_center_to_faction_aux
                        # Input: arg1 = center_no, arg2 = faction
						  ("give_center_to_faction_while_maintaining_lord",
							[
							  (store_script_param_1, ":center_no"),
							  (store_script_param_2, ":faction_no"),

							  (store_faction_of_party, ":old_faction", ":center_no"),
							  ##diplomacy start+
							  #If the player, previously the head of his own faction, is now joining
							  #an NPC faction, don't reset the "last taken" time or the "ex faction"
							  #slots.
							  (try_begin),
								#Friendly transfer: don't update transfer time or ex-faction
								(eq, ":old_faction", "fac_player_supporters_faction"),
								(eq, ":faction_no", "$players_kingdom"),
							  (else_try),
								#Defection: update transfer time and ex-faction
								(party_set_slot, ":center_no", slot_center_ex_faction, ":old_faction"),
								(store_current_hours, ":cur_hours"),
								(party_set_slot, ":center_no", dplmc_slot_center_last_transfer_time, ":cur_hours"),
							  (try_end),
							  ##diplomacy end+
							  (party_set_faction, ":center_no", ":faction_no"),

							  (try_begin),
								(party_slot_eq, ":center_no", slot_party_type, spt_village),
								(party_get_slot, ":farmer_party", ":center_no", slot_village_farmer_party),
								(gt, ":farmer_party", 0),
								(party_is_active, ":farmer_party"),
								(party_set_faction, ":farmer_party", ":faction_no"),
							  (try_end),

							  (call_script, "script_update_faction_notes", ":faction_no"),
							  (call_script, "script_update_center_notes", ":center_no"),

							  (try_for_range, ":other_center", centers_begin, centers_end),
								(party_slot_eq, ":other_center", slot_village_bound_center, ":center_no"),
								(call_script, "script_give_center_to_faction_while_maintaining_lord", ":other_center", ":faction_no"),
							  (try_end),
						  ]),
                        
                        # script_check_concilio_calradi_achievement
                        ("check_concilio_calradi_achievement",
                          [
                            (try_begin),
                              (eq, "$players_kingdom", "fac_player_supporters_faction"),
                              (faction_get_slot, ":player_faction_king", "fac_player_supporters_faction", slot_faction_leader),
                              (eq, ":player_faction_king", "trp_player"),
                              (assign, ":number_of_vassals", 0),
                              (try_for_range, ":cur_troop", active_npcs_begin, active_npcs_end),
                                (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
                                (store_faction_of_troop, ":cur_faction", ":cur_troop"),
                                (eq, ":cur_faction", "fac_player_supporters_faction"),
                                (val_add, ":number_of_vassals", 1),
                              (try_end),
                              (ge, ":number_of_vassals", 3),
                              (unlock_achievement, ACHIEVEMENT_CONCILIO_CALRADI),
                            (try_end),
                        ]),
						
						  # script_refresh_center_inventories																		#	1.143 Port // Script newly added
					    ("refresh_center_inventories",
 					   [   	
 					     (set_merchandise_modifier_quality,150),
 					     (reset_item_probabilities,100),	    

 					     # Add trade goods to merchant inventories
					      (try_for_range,":cur_center",towns_begin, towns_end),
					        (party_get_slot,":cur_merchant",":cur_center",slot_town_merchant),
					        (reset_item_probabilities,100),
					        (assign, ":total_production", 0),
					        (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
 					         (call_script, "script_center_get_production", ":cur_center", ":cur_goods"),
					  		(assign, ":cur_production", reg0),
					  
 					         (try_for_range, ":cur_village", villages_begin, villages_end),
					  		  (party_slot_eq, ":cur_village", slot_village_bound_center, ":cur_center"),
 					           (call_script, "script_center_get_production", ":cur_village", ":cur_goods"),
					  		  (val_div, reg0, 3),
					  		  (val_add, ":cur_production", reg0),
					  		(try_end),		

					  		(val_max, ":cur_production", 1),
					  		(val_mul, ":cur_production", 4),

					  		(val_add, ":total_production", ":cur_production"),
 					       (try_end),
					  
					  	  (party_get_slot, ":town_prosperity", ":cur_center", slot_town_prosperity),
					  	  (assign, ":number_of_items_in_town", 25),
					  
					  	  (try_begin), #1.0x - 2.0x (50 - 100 prosperity)
					  	    (ge, ":town_prosperity", 50),
					  		(store_sub, ":ratio", ":town_prosperity", 50),
					  		(val_mul, ":ratio", 2),
					  		(val_add, ":ratio", 100),
					  		(val_mul, ":number_of_items_in_town", ":ratio"),
					  		(val_div, ":number_of_items_in_town", 100),
					  	  (else_try), #0.5x - 1.0x (0 - 50 prosperity)
					  		(store_sub, ":ratio", ":town_prosperity", 50),
					  		(val_add, ":ratio", 100),
					  		(val_mul, ":number_of_items_in_town", ":ratio"),
					  		(val_div, ":number_of_items_in_town", 100),
					  	  (try_end),
					  
					  	  (val_clamp, ":number_of_items_in_town", 10, 40),	
					  
					  	  (try_begin),
					  	    (is_between, ":cur_center", castles_begin, castles_end),
					  	    (val_div, ":number_of_items_in_town", 2),
 					       (try_end),
					  
 					       (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
 					         (call_script, "script_center_get_production", ":cur_center", ":cur_goods"),
					  		(assign, ":cur_production", reg0),
					  
 					         (try_for_range, ":cur_village", villages_begin, villages_end),
					  		  (party_slot_eq, ":cur_village", slot_village_bound_center, ":cur_center"),
 					           (call_script, "script_center_get_production", ":cur_village", ":cur_goods"),
						  	  (val_div, reg0, 3),
						  	  (val_add, ":cur_production", reg0),
						  	(try_end),		
					  
					  		(val_max, ":cur_production", 1),
						  	(val_mul, ":cur_production", 4),
					  
   					       (val_mul, ":cur_production", ":number_of_items_in_town"),
						  	(val_mul, ":cur_production", 100),
						  	(val_div, ":cur_production", ":total_production"),
  					        (set_item_probability_in_merchandise, ":cur_goods", ":cur_production"),						  
 					       (try_end),

						    (troop_clear_inventory, ":cur_merchant"),
  					      (troop_add_merchandise, ":cur_merchant", itp_type_goods, ":number_of_items_in_town"),
					  
 					       (troop_ensure_inventory_space, ":cur_merchant", 20),
 					       (troop_sort_inventory, ":cur_merchant"),
 					       (store_troop_gold, ":cur_gold",":cur_merchant"),
							(party_get_slot, ":prosperity", ":cur_center", slot_town_prosperity), #prosperty changes between 0..100 Floris
							(try_begin),
								(ge,":prosperity", 75),							
								(lt,":cur_gold",8000),
								(store_random_in_range,":new_gold",2000,4000),
								(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
							(else_try),
								(ge,":prosperity", 50),							
								(lt,":cur_gold",4000),
								(store_random_in_range,":new_gold",1000,2000),
								(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),	
							(else_try),
								(ge,":prosperity", 0),							
								(lt,":cur_gold",400),
								(store_random_in_range,":new_gold",300,500),
								(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
							(try_end),
  					    (try_end), 	
 					   ]), 

					    # script_refresh_center_armories																			#	1.143 Port // Script newly added
					    ("refresh_center_armories",
 					   [
 					     (reset_item_probabilities, 100),
					  	(set_merchandise_modifier_quality, 150),    
					  	(try_for_range, ":cur_merchant", armor_merchants_begin, armor_merchants_end),    
							  (store_sub, ":cur_town", ":cur_merchant", armor_merchants_begin),
							  (val_add, ":cur_town", towns_begin),
							  (troop_clear_inventory, ":cur_merchant"),
							  (party_get_slot, ":cur_faction", ":cur_town", slot_center_original_faction),    
							  (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_body_armor, 16),
							  (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_head_armor, 16),
							  (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_foot_armor, 8),
							  (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_hand_armor, 4),
							  (troop_ensure_inventory_space, ":cur_merchant", merchant_inventory_space),
							  (troop_sort_inventory, ":cur_merchant"),
							  (store_troop_gold, ":cur_gold", ":cur_merchant"),
							(party_get_slot, ":prosperity", ":cur_town", slot_town_prosperity), #prosperty changes between 0..100 Floris
							(try_begin),
								(ge,":prosperity", 75),							
								(lt,":cur_gold",8000),
								(store_random_in_range,":new_gold",2000,4000),
								(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
							(else_try),
								(ge,":prosperity", 50),							
								(lt,":cur_gold",4000),
								(store_random_in_range,":new_gold",1000,2000),
								(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),	
							(else_try),
								(ge,":prosperity", 0),							
								(lt,":cur_gold",400),
								(store_random_in_range,":new_gold",300,500),
								(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
							(try_end),
 					     (end_try),
 					   ]),

					    # script_refresh_center_weaponsmiths																		#	1.143 Port // Script newly added
					    ("refresh_center_weaponsmiths",
					    [
 					     (reset_item_probabilities, 100),
					      (set_merchandise_modifier_quality, 150),
 					     (try_for_range, ":cur_merchant", weapon_merchants_begin, weapon_merchants_end),
							  (store_sub, ":cur_town", ":cur_merchant", weapon_merchants_begin),
							   (val_add, ":cur_town", towns_begin), 
							  (troop_clear_inventory, ":cur_merchant"),
							   (party_get_slot, ":cur_faction", ":cur_town", slot_center_original_faction),
							 (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_one_handed_wpn, 5),
							  (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_two_handed_wpn, 5),
							  (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_polearm, 5),
							  (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_shield, 6),
							  (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_bow, 4),
							  (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_crossbow, 3),
							  (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_thrown, 5),
							  (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_arrows, 2),
							  (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_bolts, 2),
							  (troop_ensure_inventory_space, ":cur_merchant", merchant_inventory_space),
							 (troop_sort_inventory, ":cur_merchant"),
							 (store_troop_gold, ":cur_gold", ":cur_merchant"),
							(party_get_slot, ":prosperity", ":cur_town", slot_town_prosperity), #prosperty changes between 0..100 Floris
							(try_begin),
								(ge,":prosperity", 75),							
								(lt,":cur_gold",8000),
								(store_random_in_range,":new_gold",2000,4000),
								(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
							(else_try),
								(ge,":prosperity", 50),							
								(lt,":cur_gold",4000),
								(store_random_in_range,":new_gold",1000,2000),
								(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),	
							(else_try),
								(ge,":prosperity", 0),							
								(lt,":cur_gold",400),
								(store_random_in_range,":new_gold",300,500),
								(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
							(try_end),
  					    (try_end),
 					   ]),

 					   # script_refresh_center_stables																				#	1.143 Port // Script newly added
 					   ("refresh_center_stables",
 					   [
  					    (reset_item_probabilities, 100),
 					     (set_merchandise_modifier_quality, 150),
 					     (try_for_range, ":cur_merchant", horse_merchants_begin, horse_merchants_end),
							  (troop_clear_inventory, ":cur_merchant"),
							  (store_sub, ":cur_town", ":cur_merchant", horse_merchants_begin),
							 (val_add, ":cur_town", towns_begin),
							  (party_get_slot, ":cur_faction", ":cur_town", slot_center_original_faction),
							  (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_horse, 10), #Floris, was 5
							  (troop_ensure_inventory_space, ":cur_merchant", 65),
							  (troop_sort_inventory, ":cur_merchant"),
							  (store_troop_gold, ":cur_gold", ":cur_merchant"),
							(party_get_slot, ":prosperity", ":cur_town", slot_town_prosperity), #prosperty changes between 0..100 Floris
							(try_begin),
								(ge,":prosperity", 75),							
								(lt,":cur_gold",8000),
								(store_random_in_range,":new_gold",2000,4000),
								(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
								(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_horse, 5), #Floris
							(else_try),
								(ge,":prosperity", 50),							
								(lt,":cur_gold",4000),
								(store_random_in_range,":new_gold",1000,2000),
								(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),	
								(troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_horse, 2), #Floris
							(else_try),
								(ge,":prosperity", 0),							
								(lt,":cur_gold",400),
								(store_random_in_range,":new_gold",300,500),
								(call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"), #Floris
							(try_end),
  					    (try_end),
 					   ]),

                        
                        ##diplomacy 3.2 begin
                        #recruiter kit begin
                        ("dplmc_send_recruiter",
                          [
                            (store_script_param, ":number_of_recruits", 1),
                            #daedalus begin
                            (store_script_param, ":faction_of_recruits", 2),
                            #daedalus end
                            (assign, ":expenses", ":number_of_recruits"),
                            (val_mul, ":expenses", 20),
                            (val_add, ":expenses", 10),
                            (call_script, "script_dplmc_withdraw_from_treasury", ":expenses"),
                            (set_spawn_radius, 1),
                            (spawn_around_party, "$current_town", "pt_dplmc_recruiter"),
                            (assign,":spawned_party",reg0),
                            (party_set_ai_behavior, ":spawned_party", ai_bhvr_hold),
                            (party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_recruiter),
                            (party_set_slot, ":spawned_party", dplmc_slot_party_recruiter_needed_recruits, ":number_of_recruits"),
                            #daedalus begin
                            (party_set_slot, ":spawned_party", dplmc_slot_party_recruiter_needed_recruits_faction, ":faction_of_recruits"),
                            #daedalus end
                            (party_set_slot, ":spawned_party", dplmc_slot_party_recruiter_origin, "$current_town"),
                            (assign, ":faction", "$players_kingdom"),
                            (party_set_faction, ":spawned_party", ":faction"),
                        ]),
                        #recruiter kit end
                        #Diplomacy 3.2 end
                        
                        ## CC
                        ####################################################################################
                        #
						# Autoloot Scripts begin
						# ---------------------------------------------------
						####################################################################################

                        ###################################
                        # Can a troop qualify to use this item?
                        # Returns 1 = yes, 0 = no.
                        ("troop_can_use_item",
                          [
                            (store_script_param, ":troop", 1),
                            (store_script_param, ":item", 2),
                            (store_script_param, ":item_modifier", 3),
                            
                            (item_get_type, ":type", ":item"),
                            (try_begin),
                              (eq, ":type", itp_type_book),
                              (item_get_slot, ":difficulty", ":item", slot_item_intelligence_requirement),
                            (else_try),
                              (item_get_slot, ":difficulty", ":item", slot_item_difficulty),
                            (try_end),
                            
                            (try_begin),
                              (eq, ":difficulty", 0), # don't apply imod modifiers if item has no requirement
                            (else_try),
                              (eq, ":item_modifier", imod_stubborn),
                              (val_add, ":difficulty", 1),
                            (else_try),
                              (eq, ":item_modifier", imod_timid),
                              (val_sub, ":difficulty", 1),
                            (else_try),
                              (eq, ":item_modifier", imod_heavy),
                              (neq, ":type", itp_type_horse), #heavy horses don't increase difficulty
                              (val_add, ":difficulty", 1),
                            (else_try),
                              (eq, ":item_modifier", imod_strong),
                              (val_add, ":difficulty", 2),
                            (else_try),
                              (eq, ":item_modifier", imod_masterwork),
                              (val_add, ":difficulty", 4),
                            (try_end),
                            
                            (try_begin),
                              (eq, ":type", itp_type_horse),
                              (store_skill_level, ":skill", skl_riding, ":troop"),
                            (else_try),
                              (this_or_next|eq, ":type", itp_type_crossbow),
                              (this_or_next|eq, ":type", itp_type_one_handed_wpn),
                              (this_or_next|eq, ":type", itp_type_two_handed_wpn),
                              (this_or_next|eq, ":type", itp_type_polearm),
                              (this_or_next|eq, ":type", itp_type_head_armor),
                              (this_or_next|eq, ":type", itp_type_body_armor),
                              (this_or_next|eq, ":type", itp_type_foot_armor),
                              (eq, ":type", itp_type_hand_armor),
                              (store_attribute_level, ":skill", ":troop", ca_strength),
                            (else_try),
                              (eq, ":type", itp_type_shield),
                              (store_skill_level, ":skill", skl_shield, ":troop"),
                            (else_try),
                              (eq, ":type", itp_type_bow),
                              (store_skill_level, ":skill", skl_power_draw, ":troop"),
                            (else_try),
                              (eq, ":type", itp_type_thrown),
                              (store_skill_level, ":skill", skl_power_throw, ":troop"),
                            (else_try),
                              (eq, ":type", itp_type_book),
                              (store_attribute_level, ":skill", ":troop", ca_intelligence),
                            (try_end),
                            
                            (try_begin),
								(this_or_next|lt, ":skill", ":difficulty"),
								(this_or_next|is_between, ":item", itm_book_tactics, itm_trade_spice),
								#(this_or_next|is_between, ":item",reference_books_begin,reference_books_end),
								#(this_or_next|is_between, ":item", itm_book_spotting_reference, itm_pavise),
                              (eq, ":item_modifier", imod_lame),
                              (assign, reg0, 0),
                            (else_try),
                              (troop_slot_eq, ":troop", slot_upgrade_horse, 1),
                              (item_slot_eq, ":item", slot_item_cant_on_horseback, 1),
                              (assign, reg0, 0),
                            (else_try),
                              (assign, reg0, 1),
                            (try_end),
                        ]),
                        
                        #####################################################################
                        # gets an item's value
                        # Param1: item ID
                        # Param2: item modifier
                        #####################################################################
                        
                        ################################################################
                        ##### Custom Commander(CC)
                        ################################################################
                        
                        # deprecated, old code of script_get_item_value_with_imod
                        #("get_item_value_with_imod",
                        #[# returns the sell price based on the item's money value and its imod
                        #(store_script_param, ":item", 1),
                        #(store_script_param, ":imod", 2),
                        
                        #(store_item_value, ":score", ":item"),
                        #(try_begin),
                        #(eq, ":imod", imod_plain),
                        #(assign, ":imod_multiplier", 100),
                        #(else_try),
                        #(eq, ":imod", imod_cracked),
                        #(assign, ":imod_multiplier", 50),
                        #(else_try),
                        #(eq, ":imod", imod_rusty),
                        #(assign, ":imod_multiplier", 55),
                        #(else_try),
                        #(eq, ":imod", imod_bent),
                        #(assign, ":imod_multiplier", 65),
                        #(else_try),
                        #(eq, ":imod", imod_chipped),
                        #(assign, ":imod_multiplier", 72),
                        #(else_try),
                        #(eq, ":imod", imod_battered),
                        #(assign, ":imod_multiplier", 75),
                        #(else_try),
                        #(eq, ":imod", imod_poor),
                        #(assign, ":imod_multiplier", 80),
                        #(else_try),
                        #(eq, ":imod", imod_crude),
                        #(assign, ":imod_multiplier", 83),
                        #(else_try),
                        #(eq, ":imod", imod_old),
                        #(assign, ":imod_multiplier", 86),
                        #(else_try),
                        #(eq, ":imod", imod_cheap),
                        #(assign, ":imod_multiplier", 90),
                        #(else_try),
                        #(eq, ":imod", imod_fine),
                        #(assign, ":imod_multiplier", 190),
                        #(else_try),
                        #(eq, ":imod", imod_well_made),
                        #(assign, ":imod_multiplier", 250),
                        #(else_try),
                        #(eq, ":imod", imod_sharp),
                        #(assign, ":imod_multiplier", 160),
                        #(else_try),
                        #(eq, ":imod", imod_balanced),
                        #(assign, ":imod_multiplier", 350),
                        #(else_try),
                        #(eq, ":imod", imod_tempered),
                        #(assign, ":imod_multiplier", 670),
                        #(else_try),
                        #(eq, ":imod", imod_deadly),
                        #(assign, ":imod_multiplier", 850),
                        #(else_try),
                        #(eq, ":imod", imod_exquisite),
                        #(assign, ":imod_multiplier", 1450),
                        #(else_try),
                        #(eq, ":imod", imod_masterwork),
                        #(assign, ":imod_multiplier", 1750),
                        #(else_try),
                        #(eq, ":imod", imod_heavy),
                        #(assign, ":imod_multiplier", 190),
                        #(else_try),
                        #(eq, ":imod", imod_strong),
                        #(assign, ":imod_multiplier", 490),
                        #(else_try),
                        #(eq, ":imod", imod_powerful),
                        #(assign, ":imod_multiplier", 320),
                        #(else_try),
                        #(eq, ":imod", imod_tattered),
                        #(assign, ":imod_multiplier", 50),
                        #(else_try),
                        #(eq, ":imod", imod_ragged),
                        #(assign, ":imod_multiplier", 70),
                        #(else_try),
                        #(eq, ":imod", imod_rough),
                        #(assign, ":imod_multiplier", 60),
                        #(else_try),
                        #(eq, ":imod", imod_sturdy),
                        #(assign, ":imod_multiplier", 170),
                        #(else_try),
                        #(eq, ":imod", imod_thick),
                        #(assign, ":imod_multiplier", 260),
                        #(else_try),
                        #(eq, ":imod", imod_hardened),
                        #(assign, ":imod_multiplier", 390),
                        #(else_try),
                        #(eq, ":imod", imod_reinforced),
                        #(assign, ":imod_multiplier", 650),
                        #(else_try),
                        #(eq, ":imod", imod_superb),
                        #(assign, ":imod_multiplier", 250),
                        #(else_try),
                        #(eq, ":imod", imod_lordly),
                        #(assign, ":imod_multiplier", 1150),
                        #(else_try),
                        #(eq, ":imod", imod_lame),
                        #(assign, ":imod_multiplier", 40),
                        #(else_try),
                        #(eq, ":imod", imod_swaybacked),
                        #(assign, ":imod_multiplier", 60),
                        #(else_try),
                        #(eq, ":imod", imod_stubborn),
                        #(assign, ":imod_multiplier", 90),
                        #(else_try),
                        #(eq, ":imod", imod_timid),
                        #(assign, ":imod_multiplier", 180),
                        #(else_try),
                        #(eq, ":imod", imod_meek),
                        #(assign, ":imod_multiplier", 180),
                        #(else_try),
                        #(eq, ":imod", imod_spirited),
                        #(assign, ":imod_multiplier", 650),
                        #(else_try),
                        #(eq, ":imod", imod_champion),
                        #(assign, ":imod_multiplier", 1450),
                        #(else_try),
                        #(eq, ":imod", imod_fresh),
                        #(assign, ":imod_multiplier", 100),
                        #(else_try),
                        #(eq, ":imod", imod_day_old),
                        #(assign, ":imod_multiplier", 100),
                        #(else_try),
                        #(eq, ":imod", imod_two_day_old),
                        #(assign, ":imod_multiplier", 90),
                        #(else_try),
                        #(eq, ":imod", imod_smelling),
                        #(assign, ":imod_multiplier", 40),
                        #(else_try),
                        #(eq, ":imod", imod_rotten),
                        #(assign, ":imod_multiplier", 5),
                        #(else_try),
                        #(eq, ":imod", imod_large_bag),
                        #(assign, ":imod_multiplier", 190),
                        #(try_end),
                        #(val_mul, ":score", ":imod_multiplier"),
                        #(assign, reg0, ":score"),
                        #]),
                        
                        ("get_item_value_with_imod",
                          [# returns the sell price based on the item's money value and its imod
                            (store_script_param, ":item", 1),
                            (store_script_param, ":imod", 2),
                            
                            (store_item_value, ":score", ":item"),
                            (item_get_slot, ":imod_multiplier", ":imod", slot_item_modifier_multiplier),
                            (val_mul, ":score", ":imod_multiplier"),
                            (assign, reg0, ":score"),
                        ]),
                        
                        ("get_item_score_with_imod",
                          [
                            (store_script_param, ":item", 1),
                            (store_script_param, ":imod", 2),
                            
							(item_get_type, ":type", ":item"),
                            (try_begin),
                              (eq, ":type", itp_type_book),
                              (item_get_slot, ":i_score", ":item", slot_item_intelligence_requirement),
                            (else_try),
                              (eq, ":type", itp_type_horse),
                              (item_get_slot, ":horse_speed", ":item", slot_item_horse_speed),
                              (item_get_slot, ":horse_armor", ":item", slot_item_horse_armor),
                              (item_get_slot, ":horse_charge", ":item", slot_item_horse_charge),
                              
							  (try_begin),
                                (eq, ":imod", imod_swaybacked),
                                (val_add, ":horse_speed", -2),
                              (else_try),
                                (eq, ":imod", imod_lame),
                                (val_add, ":horse_speed", -5),
                              (else_try),
                                (eq, ":imod", imod_heavy),
                                (val_add, ":horse_armor", 3),
                                (val_add, ":horse_charge", 4),
                              (else_try),
                                (eq, ":imod", imod_spirited),
                                (val_add, ":horse_speed", 1),
                                (val_add, ":horse_armor", 1),
                                (val_add, ":horse_charge", 1),
                              (else_try),
                                (eq, ":imod", imod_champion),
                                (val_add, ":horse_speed", 2),
                                (val_add, ":horse_armor", 2),
                                (val_add, ":horse_charge", 2),
                              (try_end),
                              
							  (store_mul, ":speed_factor", 2, ":horse_speed"),
							  (store_mul, ":armor_factor", 2, ":horse_armor"),
							  (store_mul, ":charge_factor", 1, ":horse_charge"),
							  
							  (assign, ":i_score", 1),
							  (val_add, ":i_score", ":speed_factor"),
							  (val_add, ":i_score", ":armor_factor"),
							  (val_add, ":i_score", ":charge_factor"),
							  
                              # (store_mul, ":i_score", ":horse_speed", ":horse_armor"),
                              # (val_mul, ":i_score", ":horse_charge"),
                            (else_try),
                              (eq, ":type", itp_type_shield),
                              (item_get_slot, ":shield_size", ":item", slot_item_length),
                              (item_get_slot, ":shield_armor", ":item", slot_item_body_armor),
                              (item_get_slot, ":shield_speed", ":item", slot_item_speed),
                              (try_begin),
                                (eq, ":imod", imod_cracked),
                                (val_add, ":shield_armor", -4),
                              (else_try),
                                (eq, ":imod", imod_battered),
                                (val_add, ":shield_armor", -2),
                              (else_try),
                                (eq, ":imod", imod_thick),
                                (val_add, ":shield_armor", 2),
                              (else_try),
                                (eq, ":imod", imod_reinforced),
                                (val_add, ":shield_armor", 4),
                              (try_end),
                              
                              (val_add, ":shield_armor", 5),
                              (store_mul, ":i_score", ":shield_armor", ":shield_size"),
                              (val_mul, ":i_score", ":shield_speed"),
                            (else_try),
                              (this_or_next|eq, ":type", itp_type_head_armor),
                              (this_or_next|eq, ":type", itp_type_body_armor),
                              (this_or_next|eq, ":type", itp_type_foot_armor),
                              (eq, ":type", itp_type_hand_armor),
                              (item_get_slot, ":head_armor", ":item", slot_item_head_armor),
                              (item_get_slot, ":body_armor", ":item", slot_item_body_armor),
                              (item_get_slot, ":leg_armor", ":item", slot_item_leg_armor),
                              (store_add, ":i_score", ":head_armor", ":body_armor"),
                              (val_add, ":i_score", ":leg_armor"),
                              
							  # FLORIS 2.5: Windy+ - Trying to use a different method of creating the score calculation for armor that doesn't let imods dominate low level items.
							  (store_mul, ":head_factor", 2, ":head_armor"),
							  (store_mul, ":body_factor", 2, ":body_armor"),
							  (store_mul, ":leg_factor", 1, ":leg_armor"),
							  
							  (assign, ":i_score", 1),
							  (val_add, ":i_score", ":head_factor"),
							  (val_add, ":i_score", ":body_factor"),
							  (val_add, ":i_score", ":leg_factor"),
							  
							  (try_begin), # FLORIS 2.52 patch: If no armor value found for head gear use item value instead.
								  (eq, ":type", itp_type_head_armor),
								  (lt, ":head_factor", 1),
								  (store_item_value, ":i_score", ":item"),
							  (try_end),
							  # FLORIS: Windy-
							  
                              (assign, ":imod_effect_mul", 0),
                              (try_begin),
                                (gt, ":head_armor", 0),
                                (val_add, ":imod_effect_mul", 1),
                              (try_end),
                              (try_begin),
                                (gt, ":body_armor", 0),
                                (val_add, ":imod_effect_mul", 1),
                              (try_end),
                              (try_begin),
                                (gt, ":leg_armor", 0),
                                (val_add, ":imod_effect_mul", 1),
                              (try_end),
                              
                              # (try_begin),
                                # (eq, ":imod", imod_plain),
                                # (assign, ":imod_effect", 0),
                              # (else_try),
                                # (eq, ":imod", imod_cracked),
                                # (assign, ":imod_effect", -4),
                              # (else_try),
                                # (eq, ":imod", imod_rusty),
                                # (assign, ":imod_effect", -3),
                              # (else_try),
                                # (eq, ":imod", imod_battered),
                                # (assign, ":imod_effect", -2),
                              # (else_try),
                                # (eq, ":imod", imod_crude),
                                # (assign, ":imod_effect", -1),
                              # (else_try),
                                # (eq, ":imod", imod_tattered),
                                # (assign, ":imod_effect", -3),
                              # (else_try),
                                # (eq, ":imod", imod_ragged),
                                # (assign, ":imod_effect", -2),
                              # (else_try),
                                # (eq, ":imod", imod_sturdy),
                                # (assign, ":imod_effect", 1),
                              # (else_try),
                                # (eq, ":imod", imod_thick),
                                # (assign, ":imod_effect", 2),
                              # (else_try),
                                # (eq, ":imod", imod_hardened),
                                # (assign, ":imod_effect", 3),
                              # (else_try),
                                # (eq, ":imod", imod_reinforced),
                                # (assign, ":imod_effect", 4),
                              # (else_try),
                                # (eq, ":imod", imod_lordly),
                                # (assign, ":imod_effect", 6),
                              # (try_end),
                              
							  # FLORIS 2.5: Windy+ - Changing how imods effect armor scores to prevent them dominating low level items.
							  (try_begin),
                                (eq, ":imod", imod_plain),
                                (assign, ":imod_effect", 0),
                              (else_try),
                                (eq, ":imod", imod_cracked),
                                (assign, ":imod_effect", -20),
                              (else_try),
                                (eq, ":imod", imod_rusty),
                                (assign, ":imod_effect", -15),
                              (else_try),
                                (eq, ":imod", imod_battered),
                                (assign, ":imod_effect", -10),
                              (else_try),
                                (eq, ":imod", imod_crude),
                                (assign, ":imod_effect", -5),
                              (else_try),
                                (eq, ":imod", imod_tattered),
                                (assign, ":imod_effect", -15),
                              (else_try),
                                (eq, ":imod", imod_ragged),
                                (assign, ":imod_effect", -10),
                              (else_try),
                                (eq, ":imod", imod_sturdy),
                                (assign, ":imod_effect", 5),
                              (else_try),
                                (eq, ":imod", imod_thick),
                                (assign, ":imod_effect", 10),
                              (else_try),
                                (eq, ":imod", imod_hardened),
                                (assign, ":imod_effect", 15),
                              (else_try),
                                (eq, ":imod", imod_reinforced),
                                (assign, ":imod_effect", 20),
                              (else_try),
                                (eq, ":imod", imod_lordly),
                                (assign, ":imod_effect", 30),
                              (try_end),
							  (val_mul, ":imod_effect", ":i_score"),
							  (val_div, ":imod_effect", 100),
                              # FLORIS: Windy-
							  
							  (val_mul, ":imod_effect", ":imod_effect_mul"),
                              (val_add, ":i_score", ":imod_effect"),
                            (else_try),
                              (this_or_next|eq, ":type", itp_type_one_handed_wpn),
                              (this_or_next|eq, ":type", itp_type_two_handed_wpn),
                              (this_or_next|eq, ":type", itp_type_bow),
                              (this_or_next|eq, ":type", itp_type_crossbow),
                              (this_or_next|eq, ":type", itp_type_pistol),
                              (this_or_next|eq, ":type", itp_type_musket),
                              (eq, ":type", itp_type_polearm),
                              (item_get_slot, ":item_speed", ":item", slot_item_speed),
                              (item_get_slot, ":item_length", ":item", slot_item_length),
                              (item_get_slot, ":swing_damage", ":item", slot_item_swing_damage),
                              (item_get_slot, ":thrust_damage", ":item", slot_item_thrust_damage),
                              (val_mod, ":swing_damage", 256),
                              (val_mod, ":thrust_damage", 256),
                              (assign, ":item_damage", ":swing_damage"),
                              (val_max, ":item_damage", ":thrust_damage"),
                              
                              (try_begin),
                                (eq, ":imod", imod_cracked),
                                (val_add, ":item_damage", -5),
                              (else_try),
                                (eq, ":imod", imod_rusty),
                                (val_add, ":item_damage", -3),
                              (else_try),
                                (eq, ":imod", imod_bent),
                                (val_add, ":item_damage", -3),
                                (val_add, ":item_speed", -3),
                              (else_try),
                                (eq, ":imod", imod_chipped),
                                (val_add, ":item_damage", -1),
                              (else_try),
                                (eq, ":imod", imod_balanced),
                                (val_add, ":item_damage", 3),
                                (val_add, ":item_speed", 3),
                              (else_try),
                                (eq, ":imod", imod_tempered),
                                (val_add, ":item_damage", 4),
                              (else_try),
                                (eq, ":imod", imod_masterwork),
                                (val_add, ":item_damage", 5),
                                (val_add, ":item_speed", 1),
                              (else_try),
                                (eq, ":imod", imod_heavy),
                                (val_add, ":item_damage", 2),
                                (val_add, ":item_speed", -2),
                              (else_try),
                                (eq, ":imod", imod_strong),
                                (val_add, ":item_damage", 3),
                                (val_add, ":item_speed", -3),
                              (try_end),
                              
                              (try_begin),
                                (this_or_next|eq, ":type", itp_type_bow),
                                (this_or_next|eq, ":type", itp_type_crossbow),
                                (this_or_next|eq, ":type", itp_type_pistol),
                                (eq, ":type", itp_type_musket),
                                (store_mul, ":i_score", ":item_damage", ":item_speed"),
                              (else_try),
                                (this_or_next|eq, ":type", itp_type_one_handed_wpn),
                                (this_or_next|eq, ":type", itp_type_two_handed_wpn),
                                (eq, ":type", itp_type_polearm),
                                (store_mul, ":i_score", ":item_damage", ":item_speed"),
                                (val_mul, ":i_score", ":item_length"),
                              (try_end),
                            (else_try),
                              (this_or_next|eq, ":type", itp_type_arrows),
                              (this_or_next|eq, ":type", itp_type_bolts),
                              (this_or_next|eq, ":type", itp_type_bullets),
                              (eq, ":type", itp_type_thrown),
                              (item_get_slot, ":thrust_damage", ":item", slot_item_thrust_damage),
                              (val_mod, ":thrust_damage", 256),
                              (assign, ":i_score", ":thrust_damage"),
                              (val_add, ":i_score", 3), # +3 to make sure damage > 0
                              
                              (try_begin),
                                (eq, ":imod", imod_plain),
                                (val_mul, ":i_score", 2),
                              (else_try),
                                (eq, ":imod", imod_large_bag),
                                (val_mul, ":i_score", 2),
                                (val_add, ":i_score", 1),
                              (else_try),
                                (eq, ":imod", imod_bent),
                                (val_sub, ":i_score", 3),
                                (val_mul, ":i_score", 2),
                              (else_try),
                                (eq, ":imod", imod_heavy),
                                (val_add, ":i_score", 2),
                                (val_mul, ":i_score", 2),
                              (else_try),
                                (eq, ":imod", imod_balanced),
                                (val_add, ":i_score", 3),
                                (val_mul, ":i_score", 2),
                              (try_end),
                            (try_end),
                            
                            (assign, reg0, ":i_score"),
                        ]),
                        ################################################################
                        ##### Custom Commander(CC)
                        ################################################################
                        
                        ###################
                        # Used in conversations
                        
                        ("print_wpn_upgrades_to_s0",
                          [
                            (store_script_param_1, ":troop"),
                            
                            ## CC, disabled in 1.324
                            #    (troop_get_slot,":upgrade_wpn_set_sel", ":troop", slot_upgrade_wpn_set_sel),
                            #    (store_mul, ":offset", ":upgrade_wpn_set_sel", offset_of_two_sets_slot),
                            #    (store_add, ":slot_upgrade_wpn_0", slot_upgrade_wpn_0, ":offset"),
                            #    (store_add, ":slot_upgrade_wpn_1", slot_upgrade_wpn_1, ":offset"),
                            #    (store_add, ":slot_upgrade_wpn_2", slot_upgrade_wpn_2, ":offset"),
                            #    (store_add, ":slot_upgrade_wpn_3", slot_upgrade_wpn_3, ":offset"),
                            ## CC
                            
                            (str_store_string, s0, "str_empty_string"),
                            (troop_get_slot, ":upg", ":troop", slot_upgrade_wpn_0), ##CC 1.324
                            (troop_get_inventory_slot, ":item", ":troop", 0),
                            (try_begin),
                              (ge, ":item", 0),
                              (str_store_item_name, s10, ":item"),
                            (else_try),
                              (str_store_string, s10, "str_none"),
                            (try_end),
                            (val_add, ":upg", "str_hero_wpn_slot_none"),
                            (str_store_string, s1, ":upg"),
                            (str_store_string, s0, "@{s0}^{s1}"),
                            (troop_get_slot, ":upg", ":troop", slot_upgrade_wpn_1), ##CC 1.324
                            (troop_get_inventory_slot, ":item", ":troop", 1),
                            (try_begin),
                              (ge, ":item", 0),
                              (str_store_item_name, s10, ":item"),
                            (else_try),
                              (str_store_string, s10, "str_none"),
                            (try_end),
                            (val_add, ":upg", "str_hero_wpn_slot_none"),
                            (str_store_string, s1, ":upg"),
                            (str_store_string, s0, "@{s0}^{s1}"),
                            (troop_get_slot, ":upg", ":troop", slot_upgrade_wpn_2), ##CC 1.324
                            (troop_get_inventory_slot, ":item", ":troop", 2),
                            (try_begin),
                              (ge, ":item", 0),
                              (str_store_item_name, s10, ":item"),
                            (else_try),
                              (str_store_string, s10, "str_none"),
                            (try_end),
                            (val_add, ":upg", "str_hero_wpn_slot_none"),
                            (str_store_string, s1, ":upg"),
                            (str_store_string, s0, "@{s0}^{s1}"),
                            (troop_get_slot, ":upg", ":troop", slot_upgrade_wpn_3), ##1.324
                            (troop_get_inventory_slot, ":item", ":troop", 3),
                            (try_begin),
                              (ge, ":item", 0),
                              (str_store_item_name, s10, ":item"),
                            (else_try),
                              (str_store_string, s10, "str_none"),
                            (try_end),
                            (val_add, ":upg", "str_hero_wpn_slot_none"),
                            (str_store_string, s1, ":upg"),
                            (str_store_string, s0, "@{s0}^{s1}"),
                        ]),
                        
                        ################################
                        # Copy this troop's upgrade options to everyone
                        
                        ("copy_upgrade_to_all_heroes",
                          [
                            (store_script_param_1, ":troop"),
                            (store_script_param_2, ":type"),
                            
                            (try_begin),
                              (eq, ":type", wpn_setting), ##CC 1.324
                              (troop_get_slot,":upg_wpn0", ":troop",slot_upgrade_wpn_0),
                              (troop_get_slot,":upg_wpn1", ":troop",slot_upgrade_wpn_1),
                              (troop_get_slot,":upg_wpn2", ":troop",slot_upgrade_wpn_2),
                              (troop_get_slot,":upg_wpn3", ":troop",slot_upgrade_wpn_3),
                              (try_for_range, ":hero", companions_begin, companions_end),
                                (troop_set_slot,":hero",slot_upgrade_wpn_0,":upg_wpn0"),
                                (troop_set_slot,":hero",slot_upgrade_wpn_1,":upg_wpn1"),
                                (troop_set_slot,":hero",slot_upgrade_wpn_2,":upg_wpn2"),
                                (troop_set_slot,":hero",slot_upgrade_wpn_3,":upg_wpn3"),
                              (try_end),
                            (else_try),
                              ## CC disabled in 1.324
                              #      (eq, ":type", wpn_setting_2),
                              #      (troop_get_slot,":upg_wpn0", ":troop",slot_upgrade_wpn_0_set_2),
                              #      (troop_get_slot,":upg_wpn1", ":troop",slot_upgrade_wpn_1_set_2),
                              #      (troop_get_slot,":upg_wpn2", ":troop",slot_upgrade_wpn_2_set_2),
                              #      (troop_get_slot,":upg_wpn3", ":troop",slot_upgrade_wpn_3_set_2),
                              #      (try_for_range, ":hero", companions_begin, companions_end),
                              #        (troop_set_slot,":hero",slot_upgrade_wpn_0_set_2,":upg_wpn0"),
                              #        (troop_set_slot,":hero",slot_upgrade_wpn_1_set_2,":upg_wpn1"),
                              #        (troop_set_slot,":hero",slot_upgrade_wpn_2_set_2,":upg_wpn2"),
                              #        (troop_set_slot,":hero",slot_upgrade_wpn_3_set_2,":upg_wpn3"),
                              #      (try_end),
                              #    (else_try),
                              ##
                              (eq, ":type", armor_setting),
                              (troop_get_slot,":upg_armor", ":troop",slot_upgrade_armor),
                              (try_for_range, ":hero", companions_begin, companions_end),
                                (troop_set_slot,":hero",slot_upgrade_armor,":upg_armor"),
                              (try_end),
                            (else_try),
                              (eq, ":type", horse_setting),
                              (troop_get_slot,":upg_horse", ":troop",slot_upgrade_horse),
                              (try_for_range, ":hero", companions_begin, companions_end),
                                (troop_set_slot,":hero",slot_upgrade_horse,":upg_horse"),
                              (try_end),
                            (try_end),
                        ]),
                        
                        ####################################
                        # Talk to this troop from the loot menu
                        
                        #("loot_menu_talk",
                        #[
                        #(store_script_param, ":troop", 1),
                        #(modify_visitors_at_site,"scn_conversation_scene"),
                        #(reset_visitors),
                        #(set_visitor,0,"trp_player"),
                        #(set_visitor,17,":troop"),
                        #(set_jump_mission,"mt_conversation_encounter"),
                        #(jump_to_scene,"scn_conversation_scene"),
                        #(assign, "$g_camp_talk",1),
                        #(change_screen_map_conversation, ":troop"),
                        #]),
                        
                        ####################################
                        # Let each hero loot from the pool
                        
                        ("auto_loot_all",
                          [
                            # once more to pick up any discards
                            (try_for_range, ":unused", 0, 2),
                              (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
                              (try_for_range, ":i_stack", 0, ":num_stacks"),
                                (party_stack_get_troop_id, ":this_hero","p_main_party",":i_stack"),
                                (is_between, ":this_hero", companions_begin, companions_end),
                                (call_script, "script_auto_loot_troop", ":this_hero", "$pool_troop"),
                                ##CC disabled in 1.324
                                #        # switch to another set
                                #        (troop_get_slot, ":wpn_set_sel", ":this_hero", slot_upgrade_wpn_set_sel),
                                #        (val_add, ":wpn_set_sel", 1),
                                #        (val_mod, ":wpn_set_sel", 2),
                                #        (troop_set_slot, ":this_hero", slot_upgrade_wpn_set_sel, ":wpn_set_sel"),
                                #        (call_script, "script_exchange_equipments_between_two_sets", ":this_hero"),
                                ##
                                # auto_loot once more
                                (call_script, "script_auto_loot_troop", ":this_hero", "$pool_troop"),
                                ##CC disabled in 1.324
                                #        # switch back
                                #        (troop_get_slot, ":wpn_set_sel", ":this_hero", slot_upgrade_wpn_set_sel),
                                #        (val_add, ":wpn_set_sel", 1),
                                #        (val_mod, ":wpn_set_sel", 2),
                                #        (troop_set_slot, ":this_hero", slot_upgrade_wpn_set_sel, ":wpn_set_sel"),
                                #        (call_script, "script_exchange_equipments_between_two_sets", ":this_hero"),
                                ##
                              (try_end),
                            (try_end),
                            #Done. Now sort the remainder
                            (troop_sort_inventory, "$pool_troop"),
                        ]),
                        
                        
                        ####################################
                        # let this troop take its pick from the loot pool
                        
                        ("auto_loot_troop",
                          [
                            (store_script_param, ":troop", 1),
                            (store_script_param, ":pool", 2),
                            
                            (troop_get_slot,":upg_armor", ":troop",slot_upgrade_armor),
                            (troop_get_slot,":upg_horses",":troop",slot_upgrade_horse),
                            
                            ## CC disabled in 1.324
                            #    (troop_get_slot,":upgrade_wpn_set_sel", ":troop", slot_upgrade_wpn_set_sel),
                            #    (store_mul, ":offset", ":upgrade_wpn_set_sel", offset_of_two_sets_slot),
                            #    (store_add, ":slot_upgrade_wpn_0", slot_upgrade_wpn_0, ":offset"),
                            #    (store_add, ":slot_upgrade_wpn_1", slot_upgrade_wpn_1, ":offset"),
                            #    (store_add, ":slot_upgrade_wpn_2", slot_upgrade_wpn_2, ":offset"),
                            #    (store_add, ":slot_upgrade_wpn_3", slot_upgrade_wpn_3, ":offset"),
                            ## CC
                            
                            # dump whatever rubbish is in the main inventory
                            ## CC
                            (call_script, "script_transfer_inventory", ":troop", ":pool", 0),
                            ## CC
                            
                            # dispose of the troop's equipped items if necessary
                            (try_begin),
                              (store_free_inventory_capacity, ":pool_inv_cap", ":pool"),
                              (gt, ":pool_inv_cap", 0),
                              (troop_slot_ge, ":troop", slot_upgrade_wpn_0, 1), ##CC 1.324
                              (troop_get_inventory_slot, ":item", ":troop", 0),
                              (ge, ":item", 0),
							  (assign, ":old_weapon_0", ":item"),
                              (troop_get_inventory_slot_modifier, ":imod", ":troop", 0),
                              (troop_set_inventory_slot, ":troop", 0, -1), #delete it
                              (troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
                            (try_end),
                            
                            (try_begin),
                              (store_free_inventory_capacity, ":pool_inv_cap", ":pool"),
                              (gt, ":pool_inv_cap", 0),
                              (troop_slot_ge, ":troop", slot_upgrade_wpn_1, 1), ##CC 1.324
                              (troop_get_inventory_slot, ":item", ":troop", 1),
                              (ge, ":item", 0),
                              (assign, ":old_weapon_1", ":item"),
                              (troop_get_inventory_slot_modifier, ":imod", ":troop", 1),
                              (troop_set_inventory_slot, ":troop", 1, -1), #delete it
                              (troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
                            (try_end),
                            
                            (try_begin),
                              (store_free_inventory_capacity, ":pool_inv_cap", ":pool"),
                              (gt, ":pool_inv_cap", 0),
                              (troop_slot_ge, ":troop", slot_upgrade_wpn_2, 1), ##CC 1.324
                              (troop_get_inventory_slot, ":item", ":troop", 2),
                              (ge, ":item", 0),
                              (assign, ":old_weapon_2", ":item"),
                              (troop_get_inventory_slot_modifier, ":imod", ":troop", 2),
                              (troop_set_inventory_slot, ":troop", 2, -1), #delete it
                              (troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
                            (try_end),
                            
                            (try_begin),
                              (store_free_inventory_capacity, ":pool_inv_cap", ":pool"),
                              (gt, ":pool_inv_cap", 0),
                              (troop_slot_ge, ":troop", slot_upgrade_wpn_3, 1), ##CC 1.324
                              (troop_get_inventory_slot, ":item", ":troop", 3),
                              (ge, ":item", 0),
                              (assign, ":old_weapon_3", ":item"),
                              (troop_get_inventory_slot_modifier, ":imod", ":troop", 3),
                              (troop_set_inventory_slot, ":troop", 3, -1), #delete it
                              (troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
                            (try_end),
                            
                            (try_for_range, ":i_slot", 4, 9),
                              (store_free_inventory_capacity, ":pool_inv_cap", ":pool"),
                              (gt, ":pool_inv_cap", 0),
                              (troop_get_inventory_slot, ":item", ":troop", ":i_slot"),
                              (ge, ":item", 0),
							  (try_begin),
								(eq, ":i_slot", ek_head),
								(assign, ":old_helmet", ":item"),
							  (else_try),
							    (eq, ":i_slot", ek_body),
								(assign, ":old_body", ":item"),
							  (else_try),
							    (eq, ":i_slot", ek_foot),
								(assign, ":old_boots", ":item"),
							  (else_try),
							    (eq, ":i_slot", ek_gloves),
								(assign, ":old_gloves", ":item"),
							  (else_try),
							    (eq, ":i_slot", ek_horse),
								(assign, ":old_horse", ":item"),
							  (try_end),
                              (troop_get_inventory_slot_modifier, ":imod", ":troop", ":i_slot"),
                              (item_get_type, ":i_type", ":item"),
                              (try_begin),
                                (this_or_next|eq, ":i_type", itp_type_head_armor),
                                (this_or_next|eq, ":i_type", itp_type_body_armor),
                                (this_or_next|eq, ":i_type", itp_type_foot_armor),
                                (eq, ":i_type", itp_type_hand_armor),
                                (neq, ":upg_armor", 0), # we're uprgrading armors
                                (troop_set_inventory_slot, ":troop", ":i_slot", -1), #delete it
                                (troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
                              (else_try),
                                (eq, ":i_type", itp_type_horse),
                                (neq, ":upg_horses", 0), # we're uprgrading horses
                                (troop_set_inventory_slot, ":troop", ":i_slot", -1), #delete it
                                (troop_add_item, ":pool", ":item", ":imod"), # chuck it in the pool
                              (try_end),
                            (try_end),
                            
                            # clear best matches
                            (assign, ":best_helmet_slot", -1),
                            (assign, ":best_helmet_val", 0),
                            (assign, ":best_body_slot", -1),
                            (assign, ":best_body_val", 0),
                            (assign, ":best_boots_slot", -1),
                            (assign, ":best_boots_val", 0),
                            (assign, ":best_gloves_slot", -1),
                            (assign, ":best_gloves_val", 0),
                            (assign, ":best_horse_slot", -1),
                            (assign, ":best_horse_val", 0),
							## Floris 2.52+ ## - Removed book upgrading. - Windyplains
                            # (assign, ":best_book_slot", -1),
                            # (assign, ":best_book_val", 0), 
							## Floris 2.52- ## 
                            
                            # Now search through the pool for the best items
                            (troop_get_inventory_capacity, ":inv_cap", ":pool"),
                            (try_for_range, ":i_slot", 0, ":inv_cap"),
                              (troop_get_inventory_slot, ":item", ":pool", ":i_slot"),
                              (ge, ":item", 0),
                              (troop_get_inventory_slot_modifier, ":imod", ":pool", ":i_slot"),
                              (call_script, "script_troop_can_use_item", ":troop", ":item", ":imod"),
                              (eq, reg0, 1), # can use
                              (call_script, "script_get_item_score_with_imod", ":item", ":imod"),
                              (assign, ":score", reg0),
                              
                              (item_get_type, ":item_type", ":item"),
                              (try_begin),
								## FLORIS 2.52+ ## - Removed book upgrading - Windyplains
# #                                (is_between, ":item", readable_books_begin, readable_books_end), #it's a readable book
								# (is_between, ":item", itm_book_tactics, itm_book_wound_treatment_reference),
								# #(this_or_next|is_between, ":item", itm_book_necronomicon, itm_boots_plate_boots2),
								# #(is_between, ":item", itm_book_prisoner_management, itm_book_spotting_reference),
                                # (call_script, "script_get_book_read_slot", ":troop", ":item"),
                                # (assign, ":slot_no", reg0),
                                # (troop_slot_eq, "trp_book_read", ":slot_no", 0),
                                # (gt, ":score", ":best_book_val"),
                                # (assign, ":best_book_slot", ":i_slot"),
                                # (assign, ":best_book_val", ":score"),
                              # (else_try),
							    ## FLORIS 2.52- ##
                                (eq, ":item_type", itp_type_horse), #it's a horse
                                (eq, ":upg_horses", 1), # we're uprgrading horses
								(gt, ":score", ":best_horse_val"),
                                (assign, ":best_horse_slot", ":i_slot"),
                                (assign, ":best_horse_val", ":score"),
                              (else_try),
                                (try_begin),
                                  (eq, ":item_type", itp_type_head_armor),
                                  (eq, ":upg_armor", 1), # we're uprgrading armor
                                  (gt, ":score", ":best_helmet_val"),
                                  (assign, ":best_helmet_slot", ":i_slot"),
                                  (assign, ":best_helmet_val", ":score"),
                                (else_try),
                                  (eq, ":item_type", itp_type_body_armor),
                                  (eq, ":upg_armor", 1), # we're uprgrading armor
                                  (gt, ":score", ":best_body_val"),
                                  (assign, ":best_body_slot", ":i_slot"),
                                  (assign, ":best_body_val", ":score"),
                                (else_try),
                                  (eq, ":item_type", itp_type_foot_armor),
                                  (eq, ":upg_armor", 1), # we're uprgrading armor
                                  (gt, ":score", ":best_boots_val"),
                                  (assign, ":best_boots_slot", ":i_slot"),
                                  (assign, ":best_boots_val", ":score"),
                                (else_try),
                                  (eq, ":item_type", itp_type_hand_armor),
                                  (eq, ":upg_armor", 1), # we're uprgrading armor
                                  (gt, ":score", ":best_gloves_val"),
                                  (assign, ":best_gloves_slot", ":i_slot"),
                                  (assign, ":best_gloves_val", ":score"),
                                (try_end),
                              (try_end),
                            (try_end),
                            # Now we know which ones are the best. Give them to the troop.
                            (try_begin),
                              (assign, ":best_slot", ":best_helmet_slot"),
                              (ge, ":best_slot", 0),
                              (troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
                              (ge, ":item", 0),
                              ## CC
                              (troop_get_inventory_slot, ":head_item", ":troop", ek_head),
                              (eq, ":head_item", -1),
                              ## CC
                              (troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
                              (troop_set_inventory_slot, ":troop", ek_head, ":item"),
                              (troop_set_inventory_slot_modifier, ":troop", ek_head, ":imod"),
                              (troop_set_inventory_slot, ":pool", ":best_slot", -1),
							  ## Floris 2.52+ ## "Show us what they took" - by Windyplains
						      (neq, ":item", ":old_helmet"),
							  (str_store_troop_name, s31, ":troop"),
							  (str_store_item_name, s32, ":item"),
							  (troop_get_type, reg31, ":troop"),
							  (str_store_string, s50, "@{s50}{s31} upgrades {reg31?her:his} helmet with {s32}.^"),
							  ## Floris 2.52- ##
                            (try_end),
                            
                            (try_begin),
                              (assign, ":best_slot", ":best_body_slot"),
                              (ge, ":best_slot", 0),
                              (troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
                              (ge, ":item", 0),
                              ## CC
                              (troop_get_inventory_slot, ":body_item", ":troop", ek_body),
                              (eq, ":body_item", -1),
                              ## CC
                              (troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
                              (troop_set_inventory_slot, ":troop", ek_body, ":item"),
                              (troop_set_inventory_slot_modifier, ":troop", ek_body, ":imod"),
                              (troop_set_inventory_slot, ":pool", ":best_slot", -1),
							  ## Floris 2.52+ ## "Show us what they took" - by Windyplains
						      (neq, ":item", ":old_body"),
							  (str_store_troop_name, s31, ":troop"),
							  (str_store_item_name, s32, ":item"),
							  (troop_get_type, reg31, ":troop"),
							  (str_store_string, s50, "@{s50}{s31} upgrades {reg31?her:his} armor with {s32}.^"),
							  ## Floris 2.52- ##
                            (try_end),
                            
                            (try_begin),
                              (assign, ":best_slot", ":best_boots_slot"),
                              (ge, ":best_slot", 0),
                              (troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
                              (ge, ":item", 0),
                              ## CC
                              (troop_get_inventory_slot, ":foot_item", ":troop", ek_foot),
                              (eq, ":foot_item", -1),
                              ## CC
                              (troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
                              (troop_set_inventory_slot, ":troop", ek_foot, ":item"),
                              (troop_set_inventory_slot_modifier, ":troop", ek_foot, ":imod"),
                              (troop_set_inventory_slot, ":pool", ":best_slot", -1),
							  ## Floris 2.52+ ## "Show us what they took" - by Windyplains
						      (neq, ":item", ":old_boots"),
							  (str_store_troop_name, s31, ":troop"),
							  (str_store_item_name, s32, ":item"),
							  (troop_get_type, reg31, ":troop"),
							  (str_store_string, s50, "@{s50}{s31} upgrades {reg31?her:his} boots with {s32}.^"),
							  ## Floris 2.52- ##
                            (try_end),
                            
                            (try_begin),
                              (assign, ":best_slot", ":best_gloves_slot"),
                              (ge, ":best_slot", 0),
                              (troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
                              (ge, ":item", 0),
                              ## CC
                              (troop_get_inventory_slot, ":gloves_item", ":troop", ek_gloves),
                              (eq, ":gloves_item", -1),
                              ## CC
                              (troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
                              (troop_set_inventory_slot, ":troop", ek_gloves, ":item"),
                              (troop_set_inventory_slot_modifier, ":troop", ek_gloves, ":imod"),
                              (troop_set_inventory_slot, ":pool", ":best_slot", -1),
							  ## Floris 2.52+ ## "Show us what they took" - by Windyplains
						      (neq, ":item", ":old_gloves"),
							  (str_store_troop_name, s31, ":troop"),
							  (str_store_item_name, s32, ":item"),
							  (troop_get_type, reg31, ":troop"),
							  (str_store_string, s50, "@{s50}{s31} upgrades {reg31?her:his} gloves with {s32}.^"),
							  ## Floris 2.52- ##
                            (try_end),
                            
                            (try_begin),
                              (assign, ":best_slot", ":best_horse_slot"),
                              (ge, ":best_slot", 0),
                              (troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
                              (ge, ":item", 0),
                              ## CC
                              (troop_get_inventory_slot, ":horse_item", ":troop", ek_horse),
                              (eq, ":horse_item", -1),
                              ## CC
                              (troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
                              (troop_set_inventory_slot, ":troop", ek_horse, ":item"),
                              (troop_set_inventory_slot_modifier, ":troop", ek_horse, ":imod"),
                              (troop_set_inventory_slot, ":pool", ":best_slot", -1),
							  ## Floris 2.52+ ## "Show us what they took" - by Windyplains
						      (neq, ":item", ":old_horse"),
							  (str_store_troop_name, s31, ":troop"),
							  (str_store_item_name, s32, ":item"),
							  (troop_get_type, reg31, ":troop"),
							  (str_store_string, s50, "@{s50}{s31} upgrades {reg31?her:his} horse with {s32}.^"),
							  ## Floris 2.52- ##
                            (try_end),
                            
							## Floris 2.52+ ## - Removed upgrading books. - Windyplains
                            # (try_begin),
                              # (assign, ":best_slot", ":best_book_slot"),
                              # (ge, ":best_slot", 0),
                              # (troop_get_inventory_slot, ":item", ":pool", ":best_slot"),
                              # (ge, ":item", 0),
                              # (store_free_inventory_capacity, ":troop_inv_cap", ":troop"),
                              # (gt, ":troop_inv_cap", 0),
                              # (troop_slot_eq, ":troop", slot_troop_current_reading_book, 0),
                              # (troop_add_item, ":troop", ":item"),
                              # (troop_set_slot, ":troop", slot_troop_current_reading_book, ":item"),
                              # (troop_set_inventory_slot, ":pool", ":best_slot", -1),
                            # (try_end),
                            ## Floris 2.52- ##
							
                            (try_for_range, ":i_slot", 0, 4),
                              (store_add, ":trp_slot", ":i_slot", slot_upgrade_wpn_0), ##CC 1.324
                              (troop_get_slot, ":type", ":troop", ":trp_slot"),
                              (gt, ":type", 0), #we're upgrading for this slot
                              (call_script, "script_scan_for_best_item_of_type", ":pool", ":type", ":troop"), #search for the best
                              (assign, ":best_slot", reg0),
                              (neq, ":best_slot", -1), #got something
                              (troop_get_inventory_slot, ":item", ":pool", ":best_slot"), #get it
                              (ge, ":item", 0),
                              ## CC
                              (troop_get_inventory_slot, ":wpn_item", ":troop", ":i_slot"),
                              (eq, ":wpn_item", -1),
                              ## CC
                              (troop_get_inventory_slot_modifier, ":imod", ":pool", ":best_slot"),
                              (troop_set_inventory_slot, ":pool", ":best_slot", -1), #remove from pool
                              (troop_set_inventory_slot, ":troop", ":i_slot", ":item"), #add to slot
                              (troop_set_inventory_slot_modifier, ":troop", ":i_slot", ":imod"),
							  ## Floris 2.52+ ## "Show us what they took" - by Windyplains
						      (neq, ":item", ":old_weapon_0"),
							  (neq, ":item", ":old_weapon_1"),
							  (neq, ":item", ":old_weapon_2"),
							  (neq, ":item", ":old_weapon_3"),
							  (str_store_troop_name, s31, ":troop"),
							  (str_store_item_name, s32, ":item"),
							  (troop_get_type, reg31, ":troop"),
							  (str_store_string, s50, "@{s50}{s31} upgrades {reg31?her:his} weapon with {s32}.^"),
							  ## Floris 2.52- ##
                            (try_end),
							## Floris 2.52+ ## "Show us what they took" - by Windyplains
							(assign, reg50, 1), # Tells the menu to show s50.
						    ## Floris 2.52- ##
                        ]),
                        
                        #######################
                        # Search for the most expensive item of a specified type
                        
                        ("scan_for_best_item_of_type",
                          [
                            (store_script_param, ":troop",1),
                            (store_script_param, ":item_type",2),
                            (store_script_param, ":troop_using", 3),
                            
                            (assign, ":best_slot", -1),
                            (assign, ":best_value", -1),
                            # iterate through the list of items
                            (troop_get_inventory_capacity, ":inv_cap", ":troop"),
                            (try_for_range, ":i_slot", 0, ":inv_cap"),
                              (troop_get_inventory_slot, ":item", ":troop", ":i_slot"),
                              (ge, ":item", 0),
                              (troop_get_inventory_slot_modifier, ":imod", ":troop", ":i_slot"),
                              #### Autoloot improved by rubik begin
                              (try_begin),
                                (item_slot_eq, ":item", slot_item_two_hand_one_hand, 1),
                                (assign, ":this_item_type", itp_type_one_handed_wpn),
                              (else_try),
                                (item_get_type, ":this_item_type", ":item"),
                              (try_end),
                              #### Autoloot improved by rubik end
                              (eq, ":this_item_type", ":item_type"), # it's one of the kind we're looking for
                              (call_script, "script_troop_can_use_item", ":troop_using", ":item", ":imod"),
                              (eq, reg0, 1), # can use
                              (call_script, "script_get_item_score_with_imod", ":item", ":imod"),
                              (gt, reg0, ":best_value"), # best one we've seen yet
                              (assign, ":best_slot", ":i_slot"),
                              (assign, ":best_value", reg0),
                            (try_end),
                            
                            # return the slot of the best one
                            (assign, reg0, ":best_slot"),
                        ]),
                        ##CC disabled in 1.324
                        # # script_exchange_equipments_between_two_sets
                        #  # Input: none
                        #  # Output: none
                        #  ("exchange_equipments_between_two_sets",
                        #    [
                        #      (store_script_param, ":troop_no", 1),
                        #
                        #      (try_for_range, ":cur_slot", 0, 4),
                        #        (store_sub, ":dest_slot", ":troop_no", companions_begin),
                        #        (val_mul, ":dest_slot", 4),
                        #        (val_add, ":dest_slot", 10),
                        #        (val_add, ":dest_slot", ":cur_slot"),
                        #        (troop_get_inventory_slot, ":dest_item", "trp_merchants_end", ":dest_slot"),
                        #        (troop_get_inventory_slot_modifier, ":dest_imod", "trp_merchants_end", ":dest_slot"),
                        #        (troop_get_inventory_slot, ":cur_item", ":troop_no", ":cur_slot"),
                        #        (troop_get_inventory_slot_modifier, ":cur_imod", ":troop_no", ":cur_slot"),
                        #        (troop_set_inventory_slot, "trp_merchants_end", ":dest_slot", ":cur_item"),
                        #        (troop_set_inventory_slot_modifier, "trp_merchants_end", ":dest_slot", ":cur_imod"),
                        #        (troop_set_inventory_slot, ":troop_no", ":cur_slot", ":dest_item"),
                        #        (troop_set_inventory_slot_modifier, ":troop_no", ":cur_slot", ":dest_imod"),
                        #      (try_end),
                        #    ]),
                        ##
                        ("transfer_inventory", [
                            (store_script_param, ":source", 1),
                            (store_script_param, ":dest", 2),
                            (store_script_param, ":trans_book", 3),
                            
                            (store_free_inventory_capacity, ":space", ":dest"),
                            (troop_sort_inventory, ":source"),
                            
                            (troop_get_inventory_capacity, ":inv_cap", ":source"),
                            (try_for_range, ":i_slot", 10, ":inv_cap"),
                              (troop_get_inventory_slot, ":item", ":source", ":i_slot"),
                              (troop_get_inventory_slot_modifier, ":imod", ":source", ":i_slot"),
                              (gt, ":item", -1),
                              
                              (assign, ":continue", 1),
                              (try_begin),
							(is_between, ":item", readable_books_begin, readable_books_end),
							#(is_between, ":item", itm_book_tactics, itm_book_wound_treatment_reference),
							#(this_or_next|is_between, ":item", readable_books_begin, readable_books_end),
							#(this_or_next|is_between, ":item", itm_book_necronomicon, itm_boots_plate_boots2),
							#(is_between, ":item", itm_book_prisoner_management, itm_book_spotting_reference),
                                (eq, ":trans_book", 0),
                                (troop_slot_eq, ":source", slot_troop_current_reading_book, ":item"),
                                (call_script, "script_get_book_read_slot", ":source", ":item"),
                                (assign, ":slot_no", reg0),
                                (troop_get_slot, ":progress", "trp_book_reading_progress", ":slot_no"),
                                (lt, ":progress", 1000),
                                (assign, ":continue", 0),
                              (else_try),
                                (eq, ":trans_book", 0),
								(is_between, ":item",reference_books_begin,reference_books_end),
								#(is_between, ":item", itm_book_wound_treatment_reference, itm_trade_spice),
							#(this_or_next|is_between, ":item",reference_books_begin,reference_books_end),
							#(is_between, ":item", itm_book_spotting_reference, itm_pavise),
                                (assign, ":continue", 0),
                              (try_end),
                              (eq, ":continue", 1),
                              
                              (gt, ":space", 0),
                              (troop_add_item, ":dest", ":item", ":imod"),
                              (val_sub, ":space", 1),
                              (try_begin),
                                (is_between, ":item", trade_goods_begin, trade_goods_end),
                                (troop_inventory_slot_get_item_amount, ":amount", ":source", ":i_slot"),
                                (troop_get_inventory_capacity, ":dest_inv_cap", ":dest"),
                                (store_sub, ":dest_slot", ":dest_inv_cap", ":space"),
                                (troop_inventory_slot_set_item_amount, ":dest", ":dest_slot", ":amount"),
                              (try_end),
                              (troop_set_inventory_slot, ":source", ":i_slot", -1),
                            (try_end),
                        ]),
                        
                        ("transfer_special_inventory", [
                            (store_script_param, ":source", 1),
                            (store_script_param, ":dest", 2),
                            
                            (store_free_inventory_capacity, ":space", ":dest"),
                            (troop_sort_inventory, ":source"),
                            
                            (troop_get_inventory_capacity, ":inv_cap", ":source"),
                            (try_for_range, ":i_slot", 10, ":inv_cap"),
                              (troop_get_inventory_slot, ":item", ":source", ":i_slot"),
                              (troop_get_inventory_slot_modifier, ":imod", ":source", ":i_slot"),
                              (gt, ":item", -1),
                              
                              (assign, ":continue", 0),
                              (try_begin),
                                (call_script, "script_get_item_value_with_imod", ":item", ":imod"),
                                (assign, ":item_value", reg0),
                                (val_div, ":item_value", 100),
                                (ge, ":item_value", "$g_price_threshold_for_picking"),
                                (assign, ":continue", 1),
                              (else_try),
                                (item_get_type, ":item_type", ":item"),
                                (this_or_next|eq, ":item_type", itp_type_goods),
                                (this_or_next|eq, ":item_type", itp_type_animal),
                                (eq, ":item_type", itp_type_book),
                                (assign, ":continue", 1),
                              (try_end),
                              (eq, ":continue", 1),
                              
                              (gt, ":space", 0),
                              (troop_add_item, ":dest", ":item", ":imod"),
                              (val_sub, ":space", 1),
                              (try_begin),
                                (is_between, ":item", trade_goods_begin, trade_goods_end),
                                (troop_inventory_slot_get_item_amount, ":amount", ":source", ":i_slot"),
                                (troop_get_inventory_capacity, ":dest_inv_cap", ":dest"),
                                (store_sub, ":dest_slot", ":dest_inv_cap", ":space"),
                                (troop_inventory_slot_set_item_amount, ":dest", ":dest_slot", ":amount"),
                              (try_end),
                              (troop_set_inventory_slot, ":source", ":i_slot", -1),
                            (try_end),
                        ]),
                        ####################################################################################
                        #
                        # Autoloot Scripts end
                        # ---------------------------------------------------
                        ####################################################################################
                        
                        ("init_item_score", set_item_score()),
                        
                        ###################################
                        # Custom Troops Scripts Begin
                        
                          ("start_customizing", [
                            (store_script_param_1, ":troop"),
                        
                            (store_skill_level, "$g_player_inventory_management", skl_inventory_management, "$g_player_troop"),
                            (store_sub, ":skill_raise", 10, "$g_player_inventory_management"),
                            (troop_raise_skill, "$g_player_troop", skl_inventory_management, ":skill_raise"),
                            (call_script, "script_copy_inventory", "$g_player_troop", "trp_inventory_backup"),
                            (call_script, "script_unequip_troop", ":troop"),
                            (store_add, ":selection_troop", 2, ":troop"),
                            (call_script, "script_copy_inventory", ":selection_troop", "$g_player_troop"),
                            (change_screen_loot, ":troop"),
                          ]),
                        
                          ("finish_customizing", [
                            (store_script_param_1, ":troop"),
                        
                            (store_sub, ":skill_raise", "$g_player_inventory_management", 10),
                            (troop_raise_skill, "$g_player_troop", skl_inventory_management, ":skill_raise"),
                            (call_script, "script_copy_inventory", "trp_inventory_backup", "$g_player_troop"),
                            (call_script, "script_unequip_troop", ":troop"),
                            (store_add, ":bak_troop", 1, ":troop"),
                            (call_script, "script_copy_inventory", ":troop", ":bak_troop"),
                            (troop_equip_items, ":troop"),
                          ]),
                        
                          ("unequip_troop", [
                            (store_script_param_1, ":troop"),
                            (try_for_range, ":i_slot", 0, 10),
                              (troop_get_inventory_slot, ":item",":troop", ":i_slot"),
                              (gt, ":item", 0),
                              (troop_get_inventory_slot_modifier, ":imod",":troop", ":i_slot"),
                              (troop_set_inventory_slot, ":troop", ":i_slot", -1),
                              (troop_add_item, ":troop", ":item", ":imod"),
                            (try_end),
                          ]),
                        
                          ("reload_custom_troops", [
                            (try_for_range, ":troop", customizable_troops_begin,  customizable_troops_end),
                              (neg|troop_is_hero, ":troop"),
                              (store_add, ":bak_troop", 1, ":troop"),
                              (call_script, "script_copy_inventory", ":bak_troop", ":troop"),
                              (troop_equip_items, ":troop"),
                            (try_end),
                          ]),
                        # Custom Troops End
                        
						##Floris - Duplicated by Diplomacy
                        #script_game_get_party_speed_multiplier
                        # This script is called from the game engine when a skill's modifiers are needed
                        # INPUT: arg1 = party_no
                        # OUTPUT: trigger_result = multiplier (scaled by 100, meaning that giving 100 as the trigger result does not change the party speed)
                        # ("game_get_party_speed_multiplier",
                          # [
                            # (store_script_param_1, ":party_no"),
                            
                            # (try_begin),
                              # (this_or_next|eq,":party_no","p_main_party"),
                              # (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
                              # (party_get_skill_level, ":speed_multiplier", ":party_no", skl_pathfinding),
                              # (val_mul,":speed_multiplier",3),
                              # (val_add,":speed_multiplier",100),
                            # (else_try),
                              # (assign,":speed_multiplier",100),
                            # (try_end),
                            
                            # (try_begin),
                              # (eq,":party_no","p_main_party"),
                              # (call_script, "script_get_inventory_weight_of_whole_party"),
                              # (assign, ":total_weight", reg0),
                              # (val_div, ":total_weight", 100),
                              # (val_sub,":speed_multiplier", ":total_weight"),
                            # (try_end),
                            
                            # (val_max, ":speed_multiplier", 0),
                            # (set_trigger_result, ":speed_multiplier"),
                        # ]),
						## Floris - Duplicated by Diplomacy
                        
                        ("get_inventory_weight_of_whole_party",
                          [
                            (assign, ":total_weight", 0),
                            
                            (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
                            (try_for_range, ":i_stack", 0, ":num_stacks"),
                              (party_stack_get_troop_id,":stack_troop","p_main_party",":i_stack"),
                              (is_between, ":stack_troop", companions_begin, companions_end),
                              (troop_get_inventory_capacity, ":inv_cap", ":stack_troop"),
                              (try_for_range, ":cur_slot", 10, ":inv_cap"),#inventory slots
                                (troop_get_inventory_slot, ":cur_item", ":stack_troop", ":cur_slot"),
                                (ge, ":cur_item", 0),
                                (item_get_slot, ":cur_item_weight", ":cur_item", slot_item_weight),
                                (val_add, ":total_weight", ":cur_item_weight"),
                              (try_end),
                            (try_end),
                            
                            (val_div, ":total_weight", 100),
                            (assign, reg0, ":total_weight"),
                        ]),
                        
                        ####### mouse fix pos system #######
                        ("mouse_fix_pos_ready",
                          [
                            (create_text_overlay, "$g_presentation_obj_38", "@ ", tf_center_justify|tf_vertical_align_center),
                            
                            (create_mesh_overlay, "$g_presentation_obj_37", "mesh_white_plane"),
                            (position_set_x, pos1, 50),
                            (position_set_y, pos1, 37500),
                            (overlay_set_size, "$g_presentation_obj_37", pos1),
                            
                            (create_mesh_overlay, "$g_presentation_obj_36", "mesh_white_plane"),
                            (position_set_x, pos1, 50000),
                            (position_set_y, pos1, 50),
                            (overlay_set_size, "$g_presentation_obj_36", pos1),
                        ]),
                        
                        ("mouse_fix_pos_run",
                          [
                            (set_fixed_point_multiplier, 1000),
                            (mouse_get_position, pos1),
                            (position_get_x, reg50, pos1),
                            (position_get_y, reg51, pos1),
                            
                            (position_set_x, pos1, reg50),
                            (position_set_y, pos1, 0),
                            (overlay_set_position, "$g_presentation_obj_37", pos1),
                            
                            (position_set_x, pos1, 0),
                            (position_set_y, pos1, reg51),
                            (overlay_set_position, "$g_presentation_obj_36", pos1),
                            
                            (try_begin),
                              (le, reg50, 500),
                              (assign, ":x_offset", 70),
                            (else_try),
                              (assign, ":x_offset", -70),
                            (try_end),
                            (try_begin),
                              (le, reg51, 375),
                              (assign, ":y_offset", 20),
                            (else_try),
                              (assign, ":y_offset", -20),
                            (try_end),
                            (store_add, ":pos_x", reg50, ":x_offset"),
                            (store_add, ":pos_y", reg51, ":y_offset"),
                            (position_set_x, pos1, ":pos_x"),
                            (position_set_y, pos1, ":pos_y"),
                            (overlay_set_position, "$g_presentation_obj_38", pos1),
                            (overlay_set_text, "$g_presentation_obj_38", "@({reg50},{reg51})"),
                        ]),
                        ####### mouse fix pos system #######
                        
                        ("get_book_read_slot",
                          [
                            (store_script_param, ":troop_no", 1),
                            (store_script_param, ":item_no", 2),
                            
                            (store_sub, ":num_companions", companions_end, companions_begin),
                            (store_sub, ":item_offset", ":item_no", readable_books_begin),
                            (store_sub, ":troop_offset", ":troop_no", companions_begin),
                            
                            (store_mul, ":slot_no", ":item_offset", ":num_companions"),
                            (val_add, ":slot_no", ":troop_offset"),
                            (assign, reg0, ":slot_no"),
                        ]),
                        
                        ("sort_food",
                          [
                            (store_script_param, ":troop_no", 1),
                            
                            (troop_get_inventory_capacity, ":inv_cap", ":troop_no"),
                            (try_for_range, ":i_slot", 10, ":inv_cap"),
                              (troop_get_inventory_slot, ":item", ":troop_no", ":i_slot"),
                              (troop_get_inventory_slot_modifier, ":imod", ":troop_no", ":i_slot"),
                              (gt, ":item", -1),
                              (is_between, ":item", food_begin, food_end),
                              (try_for_range, ":i_slot_2", ":i_slot", ":inv_cap"),
                                (neq, ":i_slot_2", ":i_slot"),
                                (troop_get_inventory_slot, ":item_2", ":troop_no", ":i_slot_2"),
                                (troop_get_inventory_slot_modifier, ":imod_2", ":troop_no", ":i_slot_2"),
                                (gt, ":item_2", -1),
                                (eq, ":item_2", ":item"),
                                (eq, ":imod_2", ":imod"),
                                (troop_inventory_slot_get_item_max_amount, ":max_amount", ":troop_no", ":i_slot"),
                                (troop_inventory_slot_get_item_amount, ":item_amount", ":troop_no", ":i_slot"),
                                (troop_inventory_slot_get_item_amount, ":item_amount_2", ":troop_no", ":i_slot_2"),
                                (store_add, ":total_amount", ":item_amount", ":item_amount_2"),
                                (store_sub, ":dest_amount_i_slot_2", ":total_amount", ":max_amount"),
                                (try_begin),
                                  (gt, ":dest_amount_i_slot_2", 0),
                                  (troop_inventory_slot_set_item_amount, ":troop_no", ":i_slot", ":max_amount"),
                                  (troop_inventory_slot_set_item_amount, ":troop_no", ":i_slot_2", ":dest_amount_i_slot_2"),
                                  (assign, ":i_slot_2", 0), # stop
                                (else_try),
                                  (troop_inventory_slot_set_item_amount, ":troop_no", ":i_slot", ":total_amount"),
                                  (troop_set_inventory_slot, ":troop_no", ":i_slot_2", -1), # delete it
                                (try_end),
                              (try_end),
                            (try_end),
                        ]),
                        
						  ("dplmc_get_troop_max_hp",
						   [
							(store_script_param_1, ":troop"),

							(store_skill_level, ":skill", skl_ironflesh, ":troop"),
							(store_attribute_level, ":attrib", ":troop", ca_strength),
							(val_mul, ":skill", 2),
							(val_add, ":skill", ":attrib"),
							(val_add, ":skill", 35),
							(assign, reg0, ":skill"),
						  ]),
						  #cc end
						  
						("get_troop_max_hp",
                          [
                            (store_script_param_1, ":troop"),
                            
                            (store_skill_level, ":skill", skl_ironflesh, ":troop"),
                            (store_attribute_level, ":attrib", ":troop", ca_strength),
                            (val_mul, ":skill", 2),
                            (val_add, ":skill", ":attrib"),
                            (val_add, ":skill", 35),
                            (assign, reg0, ":skill"),
                        ]),
						
				#	Custom Troops begin		
						
				  ("update_ranger_master",
					[
					(try_begin),
						(troop_slot_eq, "trp_custom_master", slot_troop_state, 1),
						(assign, ":num_barracks", 0),
						(try_for_range, ":town_no", walled_centers_begin, walled_centers_end),
							(party_slot_eq, ":town_no", slot_town_lord, "trp_player"),
							(party_slot_ge, ":town_no", slot_center_has_barracks, 1),
							(val_add, ":num_barracks", 1),
						(try_end),
						(val_mul, ":num_barracks", 2),
						(store_add, ":min", 8, ":num_barracks"),
						(store_add, ":max", 19, ":num_barracks"),
						(store_random_in_range, "$g_num_ranger_recruits", ":min", ":max"),
					(else_try),
						(troop_slot_eq, "trp_custom_master", slot_troop_state, 2),
						(troop_get_slot, ":town_no", "trp_custom_master", slot_troop_cur_center),
						(is_between, ":town_no", towns_begin, towns_end),
						(try_begin),
							(party_slot_ge, ":town_no", slot_center_has_barracks, 1),
							(store_random_in_range, "$g_num_ranger_recruits", 10, 21), #decrease off-set by barracks
						(else_try),
							(store_random_in_range, "$g_num_ranger_recruits", 8, 17), #decreased from staying in the same area
						(try_end),
					(else_try),	
						(troop_set_slot, "trp_custom_master", slot_troop_state, 0),
						(store_random_in_range, ":town_no", towns_begin, towns_end),
						(troop_set_slot, "trp_custom_master", slot_troop_cur_center, ":town_no"),
						(store_random_in_range, "$g_num_ranger_recruits", 10, 21),
					(try_end),
				   ]),			

				#	Custom Troops End
                        
                        ##Floris: CC 1.321
                        ("update_mystic_merchant",
                          [(try_for_range, ":town_no", towns_begin, towns_end),
                              (party_set_slot, ":town_no", slot_center_tavern_mystic_merchant, 0),
                            (try_end),
                            
                            (try_for_range, ":troop_no", mystic_merchant_begin, mystic_merchant_end),
                              (store_random_in_range, ":town_no", towns_begin, towns_end),
                              (party_set_slot, ":town_no", slot_center_tavern_mystic_merchant, ":troop_no"),
                              
                              ## clear items
                              (troop_get_inventory_capacity, ":inv_cap", ":troop_no"),
                              (try_for_range, ":i_slot", 10, ":inv_cap"),
                                (troop_set_inventory_slot, ":troop_no", ":i_slot", -1),
                              (try_end),
                              ## clear items
                              (reset_item_probabilities, 100),
                              (set_merchandise_modifier_quality, 120),
                              (troop_add_merchandise, ":troop_no", itp_type_horse,15),
                              (troop_add_merchandise, ":troop_no", itp_type_body_armor,16),
                              (troop_add_merchandise, ":troop_no", itp_type_head_armor,8),
                              (troop_add_merchandise, ":troop_no", itp_type_foot_armor,8),
                              (troop_add_merchandise, ":troop_no", itp_type_hand_armor,4),
                              (troop_add_merchandise, ":troop_no", itp_type_one_handed_wpn,5),
                              (troop_add_merchandise, ":troop_no", itp_type_two_handed_wpn,5),
                              (troop_add_merchandise, ":troop_no", itp_type_polearm,5),
                              (troop_add_merchandise, ":troop_no", itp_type_shield,6),
                              (troop_add_merchandise, ":troop_no", itp_type_bow,4),
                              (troop_add_merchandise, ":troop_no", itp_type_crossbow,3),
                              (troop_add_merchandise, ":troop_no", itp_type_thrown,5),
                            (try_end),
                        ]),
                        ##
                        
                        ("auto_sell", [
                            (store_script_param_1, ":customer"),
                            (store_script_param_2, ":merchant"),
                            
                            (store_free_inventory_capacity, ":space", ":merchant"),
                            (troop_sort_inventory, ":customer"),
                            
                            (troop_get_inventory_capacity, ":inv_cap", ":customer"),
                            (try_for_range_backwards, ":i_slot", 10, ":inv_cap"),
                              (troop_get_inventory_slot, ":item", ":customer", ":i_slot"),
                              (troop_get_inventory_slot_modifier, ":imod", ":customer", ":i_slot"),
                              (gt, ":item", -1),
                              (item_get_type, ":type", ":item"),
                              (item_slot_eq, ":type", slot_item_type_not_for_sell, 0),
                              
                              (call_script, "script_get_item_value_with_imod", ":item", ":imod"),
                              (assign, ":score", reg0),
                              (val_div, ":score", 100),
                              (call_script, "script_game_get_item_sell_price_factor", ":item"),
                              (assign, ":sell_price_factor", reg0),
                              (val_mul, ":score", ":sell_price_factor"),
                              (val_div, ":score", 100),
                              (val_max, ":score",1),
                              
                              (le, ":score", "$g_auto_sell_price_limit"),
                              (store_troop_gold, ":m_gold", ":merchant"),
                              (le, ":score", ":m_gold"),
                              (gt, ":space", 0),
                              
                              (troop_add_item, ":merchant", ":item", ":imod"),
                              (val_sub, ":space", 1),
                              (troop_set_inventory_slot, ":customer", ":i_slot", -1),
                              (troop_remove_gold, ":merchant", ":score"),
                              (troop_add_gold, ":customer", ":score"),
                            (try_end),
                        ]),
                        
                        ## CC 1.322 new lines
                        ("auto_sell_all", [
                            (try_begin),
                              (is_between, "$current_town", towns_begin, towns_end),
                              (party_get_slot, ":town_weaponsmith", "$current_town", slot_town_weaponsmith),
                              (party_get_slot, ":town_armorer", "$current_town", slot_town_armorer),
                              (party_get_slot, ":town_horse_merchant", "$current_town", slot_town_horse_merchant),
                              (party_get_slot, ":town_merchant", "$current_town", slot_town_merchant),
                            (else_try),
                              (is_between, "$current_town", villages_begin, villages_end),
                              (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
                            (try_end),
                            
                            (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
                            (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
                              (party_stack_get_troop_id,":stack_troop","p_main_party",":i_stack"),
                              (is_between, ":stack_troop", companions_begin, companions_end),
                              (store_free_inventory_capacity, ":begin_space", ":stack_troop"),
                              (store_troop_gold, ":begin_gold", ":stack_troop"),
                              (try_begin),
                                (is_between, "$current_town", towns_begin, towns_end),
                                (call_script, "script_auto_sell", ":stack_troop", ":town_weaponsmith"),
                                (call_script, "script_auto_sell", ":stack_troop", ":town_armorer"),
                                (call_script, "script_auto_sell", ":stack_troop", ":town_horse_merchant"),
                                (call_script, "script_auto_sell", ":stack_troop", ":town_merchant"),
                              (else_try),
                                (is_between, "$current_town", villages_begin, villages_end),
                                (call_script, "script_auto_sell", ":stack_troop", ":merchant_troop"),
                              (try_end),
                              (store_free_inventory_capacity, ":end_space", ":stack_troop"),
                              (store_troop_gold, ":end_gold", ":stack_troop"),
                              (neq, ":end_gold", ":begin_gold"),
                              (store_sub, ":gained_gold", ":end_gold", ":begin_gold"),
                              (set_show_messages, 0),
                              (troop_remove_gold, ":stack_troop", ":gained_gold"),
                              (troop_add_gold, "trp_player", ":gained_gold"),
                              (set_show_messages, 1),
                              (store_sub, reg1, ":end_space", ":begin_space"),
                              (assign, reg2, ":gained_gold"),
                              (store_sub, reg3, reg1, 1),
                              (store_sub, reg4, reg2, 1),
                              (str_store_troop_name, s1, ":stack_troop"),
                              (display_message, "@{s1} have sold {reg1} {reg3?items:item} and you gained {reg2} {reg4?denars:denar}."),
                            (try_end),
                        ]),
                        ##
                        
                        ("auto_buy_food", [
                            ## CC 1.322 replaced one native line by these
                            (try_begin),
                              (is_between, "$current_town", towns_begin, towns_end),
                              (party_get_slot, ":merchant_troop", "$current_town", slot_town_merchant),
                            (else_try),
                              (is_between, "$current_town", villages_begin, villages_end),
                              (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
                            (try_end),
                            ##
                            
                            (store_troop_gold, ":begin_gold", "trp_player"),
                            (store_free_inventory_capacity, ":begin_space", "trp_player"),
                            (troop_get_inventory_capacity, ":inv_cap", ":merchant_troop"),
                            (set_show_messages, 0),
                            (try_for_range, ":i_slot", 10, ":inv_cap"),
                              (troop_get_inventory_slot, ":item", ":merchant_troop", ":i_slot"),
                              (gt, ":item", -1),
                              (is_between, ":item", food_begin, food_end),
                              (troop_inventory_slot_get_item_amount, ":amount", ":merchant_troop", ":i_slot"),
                              (troop_inventory_slot_get_item_max_amount, ":max_amount", ":merchant_troop", ":i_slot"),
                              (eq, ":amount", ":max_amount"),
                              
                              (item_get_slot, ":food_portion", ":item", slot_item_food_portion),
                              (store_item_kind_count, ":food_count", ":item", "trp_player"),
                              (lt, ":food_count", ":food_portion"),
                              (store_free_inventory_capacity, ":free_inv_cap", "trp_player"),
                              (gt, ":free_inv_cap", 0),
                              
                              (call_script, "script_game_get_item_buy_price_factor", ":item"),
                              (assign, ":buy_price_factor", reg0),
                              (store_item_value,":score",":item"),
                              (val_mul, ":score", ":buy_price_factor"),
                              (val_div, ":score", 100),
                              (val_max, ":score",1),
                              (store_troop_gold, ":player_gold", "trp_player"),
                              (ge, ":player_gold", ":score"),
                              
                              (troop_add_item, "trp_player", ":item"),
                              (troop_set_inventory_slot, ":merchant_troop", ":i_slot", -1),
                              (troop_remove_gold, "trp_player", ":score"),
                              (troop_add_gold, ":merchant_troop", ":score"),
                            (try_end),
                            (set_show_messages, 1),
                            (store_troop_gold, ":end_gold", "trp_player"),
                            (store_free_inventory_capacity, ":end_space", "trp_player"),
                            (try_begin),
                              (neq, ":end_gold", ":begin_gold"),
                              (store_sub, reg1, ":begin_gold", ":end_gold"),
                              (store_sub, reg2, ":begin_space", ":end_space"),
                              (store_sub, reg3, reg1, 1),
                              (store_sub, reg4, reg2, 1),
                              (display_message, "@You have bought {reg2} {reg4?kinds:kind} of food and lost {reg1} {reg3?denars:denar}."),
                            (try_end),
                            
                            # sell rotten food
                            (store_troop_gold, ":begin_gold", "trp_player"),
                            (store_free_inventory_capacity, ":begin_space", "trp_player"),
                            (troop_get_inventory_capacity, ":inv_cap", "trp_player"),
                            (set_show_messages, 0),
                            (try_for_range, ":i_slot", 10, ":inv_cap"),
                              (troop_get_inventory_slot, ":item", "trp_player", ":i_slot"),
                              (gt, ":item", -1),
                              (is_between, ":item", food_begin, food_end),
                              (troop_get_inventory_slot_modifier, ":imod", "trp_player", ":i_slot"),
                              (eq, ":imod", imod_rotten),
                              (store_free_inventory_capacity, ":free_inv_cap", ":merchant_troop"),
                              (gt, ":free_inv_cap", 0),
                              
                              (call_script, "script_get_item_value_with_imod", ":item", ":imod"),
                              (assign, ":score", reg0),
                              (val_div, ":score", 100),
                              (call_script, "script_game_get_item_sell_price_factor", ":item"),
                              (assign, ":sell_price_factor", reg0),
                              (val_mul, ":score", ":sell_price_factor"),
                              (troop_inventory_slot_get_item_amount, ":amount", "trp_player", ":i_slot"),
                              (troop_inventory_slot_get_item_max_amount, ":max_amount", "trp_player", ":i_slot"),
                              (val_mul, ":score", ":amount"),
                              (val_div, ":score", ":max_amount"),
                              (val_div, ":score", 100),
                              (val_max, ":score",1),
                              (store_troop_gold, ":merchant_gold", ":merchant_troop"),
                              (ge, ":merchant_gold", ":score"),
                              
                              #(troop_add_item, ":merchant_troop", ":item", ":imod"),
                              (troop_set_inventory_slot, "trp_player", ":i_slot", -1),
                              (troop_remove_gold, ":merchant_troop", ":score"),
                              (troop_add_gold, "trp_player", ":score"),
                            (try_end),
                            (set_show_messages, 1),
                            (store_troop_gold, ":end_gold", "trp_player"),
                            (store_free_inventory_capacity, ":end_space", "trp_player"),
                            (try_begin),
                              (neq, ":end_gold", ":begin_gold"),
                              (store_sub, reg1, ":end_gold", ":begin_gold"),
                              (store_sub, reg2, ":end_space", ":begin_space"),
                              (store_sub, reg3, reg1, 1),
                              (store_sub, reg4, reg2, 1),
                              (display_message, "@You have sold {reg2} {reg4?kinds:kind} of rotten food and gained {reg1} {reg3?denars:denar}."),
                            (try_end),
                        ]),
                        
                        ("start_town_conversation",
                          [
                            (store_script_param, ":troop_slot_no", 1),
                            (store_script_param, ":entry_no", 2),
                            
                            (try_begin),
                              (eq, ":troop_slot_no", slot_town_merchant),
                              (assign, ":scene_slot_no", slot_town_store),
                            (else_try),
                              (eq, ":troop_slot_no", slot_town_tavernkeeper),
                              (assign, ":scene_slot_no", slot_town_tavern),
                            (else_try),
                              (assign, ":scene_slot_no", slot_town_center),
                            (try_end),
                            
                            (party_get_slot, ":conversation_scene", "$current_town", ":scene_slot_no"),
                            (modify_visitors_at_site, ":conversation_scene"),
                            (reset_visitors),
                            (set_visitor, 0, "trp_player"),
                            (party_get_slot, ":conversation_troop", "$current_town", ":troop_slot_no"),
                            (set_visitor, ":entry_no", ":conversation_troop"),
                            (set_jump_mission,"mt_conversation_encounter"),
                            (jump_to_scene, ":conversation_scene"),
                            (change_screen_map_conversation, ":conversation_troop"),
                        ]),
                        
                        # script_troop_raise_skill_limit:
                        # INPUT:
                        # param1: troop_no
                        # param2: skill_no
                        # param3: amout(ideal amout)
                        # OUTPUT: result amout
                        ("troop_raise_skill_limit",
                          [
                            (store_script_param, ":troop_no", 1),
                            (store_script_param, ":skill_no", 2),
                            (store_script_param, ":amout", 3),
                            
                            (store_skill_level, ":skill_level", ":skill_no", ":troop_no"),
                            (store_add, ":ideal_skill_level", ":skill_level", ":amout"),
                            
                            (try_begin),
                              (this_or_next|eq, ":skill_no", "skl_leadership"),
                              (this_or_next|eq, ":skill_no", "skl_prisoner_management"),
                              (this_or_next|eq, ":skill_no", "skl_spotting"),
                              (this_or_next|eq, ":skill_no", "skl_pathfinding"),
                              (this_or_next|eq, ":skill_no", "skl_tactics"),
                              (this_or_next|eq, ":skill_no", "skl_tracking"),
                              (this_or_next|eq, ":skill_no", "skl_looting"),
                              (this_or_next|eq, ":skill_no", "skl_power_draw"),
                              (this_or_next|eq, ":skill_no", "skl_power_throw"),
                              (this_or_next|eq, ":skill_no", "skl_power_strike"),
                              (eq, ":skill_no", "skl_ironflesh"),
                              (assign, ":skill_limit", 15),
                            (else_try),
                              (assign, ":skill_limit", 10),
                            (try_end),
                            
                            (try_begin),
                              (gt, ":ideal_skill_level", ":skill_limit"),
                              (store_sub, ":result_amout", ":skill_limit", ":skill_level"),
                            (else_try),
                              (assign, ":result_amout", ":amout"),
                            (try_end),
                            (troop_raise_skill,":troop_no", ":skill_no", ":result_amout"),
                        ]),
                        
                        # script_give_good_item_modifier:
                        # INPUT:
                        # param1: party_no
                        # param2: num_item_in_loot
                        # OUTPUT:
                        ("give_good_item_modifier",
                          [
                            (store_script_param_1, ":party"),
                            (store_script_param_2, ":num_item"),
                            
                            (assign, ":total_gain", 0),
                            (party_get_num_companion_stacks, ":num_stacks",":party"),
                            (try_for_range, ":i_stack", 0, ":num_stacks"),
                              (party_stack_get_troop_id, ":stack_troop",":party",":i_stack"),
                              (store_character_level, ":stack_strength", ":stack_troop"),
                              (val_add, ":stack_strength", 12),
                              (val_mul, ":stack_strength", ":stack_strength"),
                              (val_div, ":stack_strength", 100),
                              (try_begin),
                                (neg|troop_is_hero, ":stack_troop"),
                                (party_stack_get_size, ":stack_size",":party",":i_stack"),
                                (store_mul, ":stack_gain", ":stack_strength", ":stack_size"),
                              (else_try),
                                (store_mul, ":stack_gain", ":stack_strength", 2),
                              (try_end),
                              (val_add, ":total_gain", ":stack_gain"),
                            (try_end),
                            (val_max, ":total_gain", 50),
                            (val_sub, ":total_gain", 50),
                            
                            (party_get_skill_level, ":loot_level", "p_main_party", "skl_looting"),
                            (val_div, ":loot_level", 4),
                            (val_add, ":loot_level", 2),
                            (store_random_in_range, ":rounds", 1, ":loot_level"),
                            (store_add, ":num_item_temp", ":num_item", 10),
                            (val_min, ":num_item_temp", 16),
                            
                            (store_random_in_range, ":random", 0, 4000),
                            (try_begin),
                              (lt, ":random", ":total_gain"),
                              (try_for_range, ":unused", 0, ":rounds"),
                                (store_random_in_range, ":i_slot", 10, ":num_item_temp"),
                                (troop_get_inventory_slot, ":item_id", "trp_temp_troop", ":i_slot"),
								(ge, ":item_id", 1), # Bugfix: Filter for invalid items.  Floris 2.5
                                (troop_get_inventory_slot_modifier, ":imod", "trp_temp_troop", ":i_slot"),
                                (item_get_slot, ":best_imod", ":item_id", slot_item_best_modifier),
                                
                                (try_begin),
                                  (neq, ":imod", ":best_imod"),
                                  (troop_set_inventory_slot_modifier, "trp_temp_troop", ":i_slot",":best_imod"),
                                  (str_store_item_name, s2, ":item_id"),
                                  (troop_get_inventory_slot_modifier, ":item_modifier", "trp_temp_troop", ":i_slot"),
                                  (store_sub, ":out_string", ":item_modifier", imod_plain),
                                  (val_add, ":out_string", "str_imod_plain"),
                                  (str_store_string, s1, ":out_string"),
                                  (display_message, "@Bonus! A {s1}{s2}.", 0x00ff00),
                                  (play_sound,"snd_quest_succeeded"),
                                (else_try),
                                  (lt, ":rounds", 20),
                                  (val_add, ":rounds", 1),
                                (try_end),
                                
                              (try_end),
                            (try_end),
                        ]),
                        
                        ("get_num_defender_left",
                          [
                            (store_script_param, ":player_is_defender", 1),
                            
                            (assign, ":spawn_num", 0),
                            (try_for_agents, ":agent_no"),
                              (agent_is_human, ":agent_no"),
                              (agent_is_defender, ":agent_no"),
                              (val_add, ":spawn_num", 1),
                            (try_end),
                            (try_begin),
                              (eq, ":player_is_defender", 1),
                              (party_get_num_companions, ":total_num", "p_collective_friends"),
                            (else_try),
                              (party_get_num_companions, ":total_num", "p_collective_enemy"),
                            (try_end),
                            (store_sub, ":num_left", ":total_num", ":spawn_num"),
                            (assign, reg0, ":num_left"),
                        ]),
                        
                        ("generate_random_pt_three_types",
                          [
                            
                            (store_script_param, ":troop_no", 1),
                            (store_script_param, ":pt_no_1b", 2),
                            (store_script_param, ":pt_no_2b", 3),
                            (store_script_param, ":pt_no_3b", 4),
                            
                            (store_add, ":pt_no_1c", ":pt_no_1b", 1),
                            (store_add, ":pt_no_2c", ":pt_no_2b", 1),
                            (store_add, ":pt_no_3c", ":pt_no_3b", 1),
                            
                            (troop_get_slot, ":party_faction",  ":troop_no", slot_troop_original_faction),
                            (faction_get_slot, ":hero_party_template_a", ":party_faction", slot_faction_reinforcements_a),
                            (store_random_in_range, ":rand", 0, 100),
                            (try_begin),
                              (lt, ":rand", 70),
                              (assign, ":hero_party_template_b", ":pt_no_1b"),
                              (assign, ":hero_party_template_c", ":pt_no_1c"),
                            (else_try),
                              (lt, ":rand", 85),
                              (assign, ":hero_party_template_b", ":pt_no_2b"),
                              (assign, ":hero_party_template_c", ":pt_no_2c"),
                            (else_try),
                              (assign, ":hero_party_template_b", ":pt_no_3b"),
                              (assign, ":hero_party_template_c", ":pt_no_3c"),
                            (try_end),
                            (troop_set_slot, ":troop_no", slot_troop_hero_pt_a, ":hero_party_template_a"),
                            (troop_set_slot, ":troop_no", slot_troop_hero_pt_b, ":hero_party_template_b"),
                            (troop_set_slot, ":troop_no", slot_troop_hero_pt_c, ":hero_party_template_c"),
                        ]),
                        
                        ("generate_random_pt_two_types",
                          [
                            
                            (store_script_param, ":troop_no", 1),
                            (store_script_param, ":pt_no_1b", 2),
                            (store_script_param, ":pt_no_2b", 3),
                            
                            (store_add, ":pt_no_1c", ":pt_no_1b", 1),
                            (store_add, ":pt_no_2c", ":pt_no_2b", 1),
                            
                            (troop_get_slot, ":party_faction",  ":troop_no", slot_troop_original_faction),
                            (faction_get_slot, ":hero_party_template_a", ":party_faction", slot_faction_reinforcements_a),
                            (store_random_in_range, ":rand", 0, 100),
                            (try_begin),
                              (lt, ":rand", 75),
                              (assign, ":hero_party_template_b", ":pt_no_1b"),
                              (assign, ":hero_party_template_c", ":pt_no_1c"),
                            (else_try),
                              (assign, ":hero_party_template_b", ":pt_no_2b"),
                              (assign, ":hero_party_template_c", ":pt_no_2c"),
                            (try_end),
                            (troop_set_slot, ":troop_no", slot_troop_hero_pt_a, ":hero_party_template_a"),
                            (troop_set_slot, ":troop_no", slot_troop_hero_pt_b, ":hero_party_template_b"),
                            (troop_set_slot, ":troop_no", slot_troop_hero_pt_c, ":hero_party_template_c"),
                        ]),
                        
                        ("print_kill_count_to_s0",
                          [
                            (assign, ":total_reported", 0),
                            (str_clear, s0),
                            (try_for_agents, ":cur_agent"),
                              (agent_is_human, ":cur_agent"),
                              (agent_get_troop_id, ":agent_troop_id", ":cur_agent"),
                              (troop_is_hero, ":agent_troop_id"),
                              (agent_get_kill_count, ":num_killed", ":cur_agent"),
                              (agent_get_kill_count, ":num_wounded", ":cur_agent", 1),
                              (troop_get_slot, ":troop_kill_count", ":agent_troop_id", slot_troop_kill_count),
                              (troop_get_slot, ":troop_wound_count", ":agent_troop_id", slot_troop_wound_count),
                              (val_add, ":troop_kill_count", ":num_killed"),
                              (val_add, ":troop_wound_count", ":num_wounded"),
                              (troop_set_slot, ":agent_troop_id", slot_troop_kill_count, ":troop_kill_count"),
                              (troop_set_slot, ":agent_troop_id", slot_troop_wound_count, ":troop_wound_count"),
                              (this_or_next|gt, ":num_killed", 0),
                              (gt, ":num_wounded", 0),
                              (str_store_troop_name, s1, ":agent_troop_id"),
                              (store_add, reg3, ":num_killed", ":num_wounded"),
                              (assign, reg4, ":num_killed"),
                              (assign, reg5, ":num_wounded"),
                              (str_store_string, s2, "@{reg4} killed, {reg5} wounded"),
                              (try_begin),
                                (this_or_next|eq, ":agent_troop_id", "trp_player"),
                                (is_between, ":agent_troop_id", companions_begin, companions_end),
                                (str_store_string, s0, "@{s0}^{s1}: {reg3} ({s2})"),
                              (else_try),
                                (agent_is_ally, ":cur_agent"),
                                (str_store_string, s0, "@{s0}^{s1} (ally): {reg3} ({s2})"),
                              (else_try),
                                (str_store_string, s0, "@{s0}^{s1} (enemy): {reg3} ({s2})"),
                              (try_end),
                              (val_add, ":total_reported", 1),
                            (try_end),
                            (try_begin),
                              (eq, ":total_reported", 0),
                              (str_store_string, s0, "@^None"),
                            (try_end),
                        ]),
                        
                        ## CC 1.322 disabled here: in native it's active.
                        #("init_backup_hp",
                        #[
                        #(store_script_param_1, ":agent_no"),
                        
                        #(try_begin),
                        #(agent_is_human, ":agent_no"),
                        #(agent_get_troop_id, ":troop_no", ":agent_no"),
                        #(neg|troop_is_hero, ":troop_no"),
                        #(try_begin),
                        #(neg|agent_is_ally, ":agent_no"),
                        #(assign, ":backup_hp_times", "$g_game_difficulty"),
                        #(val_sub, ":backup_hp_times", 1),
                        #(else_try),
                        #(assign, ":backup_hp_times", 0),
                        #(try_end),
                        
                        #(call_script, "script_get_troop_max_hp", ":troop_no"),
                        #(assign, ":max_hp", reg0),
                        #(val_mul, ":max_hp", ":backup_hp_times"),
                        #(agent_set_slot, ":agent_no", slot_agent_backup_hp, ":max_hp"),
                        #(try_end),
                        
                        #(agent_get_slot, ":backup_hp", ":agent_no", slot_agent_backup_hp),
                        #(try_begin),
                        #(gt, ":backup_hp", 0),
                        #(agent_set_no_death_knock_down_only, ":agent_no", 1),
                        #(else_try),
                        #(agent_set_no_death_knock_down_only, ":agent_no", 0),
                        #(try_end),
                        #]),
                        
                        #("init_backup_hp_tournament",
                        #[
                        #(get_player_agent_no, ":player_agent"),
                        #(agent_get_team, ":player_team", ":player_agent"),
                        #(try_for_agents, ":agent_no"),
                        #(agent_is_human, ":agent_no"),
                        #(agent_get_troop_id, ":troop_no", ":agent_no"),
                        #(neg|troop_is_hero, ":troop_no"),
                        #(agent_get_team, ":agent_team", ":agent_no"),
                        #(try_begin),
                        #(neq, ":agent_team", ":player_team"),
                        #(assign, ":backup_hp_times", "$g_game_difficulty"),
                        #(val_sub, ":backup_hp_times", 1),
                        #(else_try),
                        #(assign, ":backup_hp_times", 0),
                        #(try_end),
                        
                        #(call_script, "script_get_troop_max_hp", ":troop_no"),
                        #(assign, ":max_hp", reg0),
                        #(val_mul, ":max_hp", ":backup_hp_times"),
                        #(agent_set_slot, ":agent_no", slot_agent_backup_hp, ":max_hp"),
                        #(try_end),
                        #]),
                        ##
                        
					 ("change_rain_or_snow",
					   [
						(party_get_current_terrain, ":terrain_type", "p_main_party"),
						(try_begin),
						  (this_or_next|eq, ":terrain_type", rt_snow),
						  (eq, ":terrain_type", rt_snow_forest),
						  (assign, ":rain_type", 2),
						(else_try),
						  (assign, ":rain_type", 1),
						(try_end),
						
						(assign, reg0, -1), #Floris - weather effects
						(assign, reg1, -1), #Floris - weather effects
						(store_random_in_range, ":rand_rain", 1, 100),
						(try_begin),
						  (get_global_cloud_amount, ":clouds"), #Floris - weather effects
						  (ge, ":clouds", 40), #Floris - weather effects #This fixes rain without any clouds that players have been experiencing
						  (lt, ":rand_rain", "$g_rand_rain_limit"),
						  (store_mul, ":rand_strength", ":rand_rain", "$g_rand_rain_limit"),
						  (val_div, ":rand_strength", 100),
						  (gt, ":rand_strength", 0),
						  (set_rain, ":rain_type", ":rand_strength"),
						  (assign, reg0, ":rain_type"), #Floris - weather effects
						  (assign, reg1, ":rand_strength"), #Floris - weather effects
						(try_end),
					  ]),

                        
                        ("sell_all_prisoners",
                          [
                            (assign, ":total_income", 0),
                            (party_get_num_prisoner_stacks, ":num_stacks", "p_main_party"),
                            (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
                              (party_prisoner_stack_get_troop_id, ":troop_no", "p_main_party", ":i_stack"),
                              (neg|troop_is_hero, ":troop_no"),
                              (party_prisoner_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),
                              (call_script, "script_game_get_prisoner_price", ":troop_no"),
                              (assign, ":sell_price", reg0),
                              (store_mul, ":stack_total_price", ":sell_price", ":stack_size"),
                              (val_add, ":total_income", ":stack_total_price"),
                              (party_remove_prisoners, "p_main_party", ":troop_no", ":stack_size"),
                            (try_end),
                            (troop_add_gold, "trp_player", ":total_income"),
                        ]),
                        
                        ("prsnt_upgrade_tree_ready",
                          [
                            ## next presentation
                            (assign, "$g_presentation_next_presentation", -1),
                            
                            (create_combo_button_overlay, "$g_presentation_obj_1"),
                            (position_set_x, pos1, 500),
                            (position_set_y, pos1, 690),
                            (overlay_set_position, "$g_presentation_obj_1", pos1),
                            # factions
                            (try_for_range_backwards, ":i_upgrade_tree", 0, 10), #This determines the amount of troop trees displayed: the first number is the first tree in the list, and the last number the total amount.
                              (store_add, ":faction_no", ":i_upgrade_tree", "fac_kingdom_1"),
                              ## faction name
                              (try_begin),
                                (eq, ":faction_no", "fac_kingdoms_end"),
                                (str_store_string, s0, "@Mercenaries"),
                              (else_try),
                                (eq, ":faction_no", "fac_robber_knights"),
                                (str_store_string, s0, "@Outlaws"),
                              (else_try),
                                (eq, ":faction_no", "fac_khergits"),
                                (str_store_string, s0, "@Sword Sisters"),
                              (else_try),
                                (eq, ":faction_no", "fac_manhunters"),
                                (str_store_string, s0, "@Freelancers"),
                              (else_try),
                                (str_store_faction_name, s0, ":faction_no"),
                              (try_end),
                              (overlay_add_item, "$g_presentation_obj_1", s0),
                            (try_end),
                            (store_sub, ":presentation_obj_val", 9, "$temp_2"),
                            (overlay_set_val, "$g_presentation_obj_1", ":presentation_obj_val"),
                            
                            ## back
                            (create_game_button_overlay, "$g_presentation_obj_5", "@Done"),
                            (position_set_x, pos1, 900),
                            (position_set_y, pos1, 25),
                            (overlay_set_position, "$g_presentation_obj_5", pos1),
                        ]),
                        
                        ("prsnt_upgrade_tree_troop_and_name",
                          [
                            (store_script_param, ":slot_no", 1),
                            (store_script_param, ":troop_no", 2),
                            (store_script_param, ":pos_x", 3),
                            (store_script_param, ":pos_y", 4),
                            
                            (str_store_troop_name, s1, ":troop_no"),
                            (create_text_overlay, reg1, "@{s1}", tf_center_justify|tf_vertical_align_center),
                            (position_set_x, pos1, 400), #These numbers influence the name of the displayed unit.
                            (position_set_y, pos1, 700),
                            (overlay_set_size, reg1, pos1),
                            (position_set_x, pos1, ":pos_x"),
                            (position_set_y, pos1, ":pos_y"),
                            (overlay_set_position, reg1, pos1),
                            
                            (val_sub, ":pos_x", 30),
                            (val_add, ":pos_y", 10),
                            (store_mul, ":cur_troop", ":troop_no", 2), #with weapons
                            (create_image_button_overlay_with_tableau_material, reg1, -1, "tableau_game_party_window", ":cur_troop"),
                            (position_set_x, pos1, 250), #These numbers influence the size of the displayed unit.
                            (position_set_y, pos1, 250),
                            (overlay_set_size, reg1, pos1),
                            (position_set_x, pos1, ":pos_x"),
                            (position_set_y, pos1, ":pos_y"),
                            (overlay_set_position, reg1, pos1),
                            (troop_set_slot, "trp_temp_array_a", ":slot_no", reg1),
                            (troop_set_slot, "trp_temp_array_b", ":slot_no", ":troop_no"),
                            
                        ]),
                        
                        ##Floris: Removed for ease of prog
                        #  ("prsnt_upgrade_tree_custom_troop_and_name",
                        #    [
                        #      (store_script_param, ":slot_no", 1),
                        #      (store_script_param, ":troop_no", 2),
                        #      (store_script_param, ":pos_x", 3),
                        #      (store_script_param, ":pos_y", 4),
                        #
                        #      # name
                        #      (create_simple_text_box_overlay, reg1),
                        #      (str_store_troop_name, s1, ":troop_no"),
                        #      (overlay_set_text, reg1, s1),
                        #      (position_set_x, pos1, 140),
                        #      (position_set_y, pos1, 800),
                        #      (overlay_set_size, reg1, pos1),
                        #      (store_sub, ":pos_y_single", ":pos_y", 10),
                        #      (store_sub, ":pos_x_single", ":pos_x", 70),
                        #      (position_set_x, pos1, ":pos_x_single"),
                        #      (position_set_y, pos1, ":pos_y_single"),
                        #      (overlay_set_position, reg1, pos1),
                        #      (troop_set_slot, "trp_temp_array_c", ":slot_no", reg1),
                        #      (troop_set_slot, "trp_temp_array_b", ":slot_no", ":troop_no"),
                        #
                        #      # plural_name
                        #      (create_simple_text_box_overlay, reg1),
                        #      (str_store_troop_name_plural, s1, ":troop_no"),
                        #      (overlay_set_text, reg1, s1),
                        #      (position_set_x, pos1, 140),
                        #      (position_set_y, pos1, 800),
                        #      (store_sub, ":pos_y_plural", ":pos_y", 35),
                        #      (store_sub, ":pos_x_plural", ":pos_x", 70),
                        #      (position_set_x, pos1, ":pos_x_plural"),
                        #      (position_set_y, pos1, ":pos_y_plural"),
                        #      (overlay_set_position, reg1, pos1),
                        #     (store_add, ":slot_no_plural", ":slot_no", 8),
                        #      (troop_set_slot, "trp_temp_array_c", ":slot_no_plural", reg1),
                        #      (troop_set_slot, "trp_temp_array_b", ":slot_no_plural", ":troop_no"),
                        #
                        #      # default_name
                        #      (create_button_overlay, reg1, "@Default", tf_center_justify|tf_vertical_align_center),
                        #      (position_set_x, pos1, 800),
                        #      (position_set_y, pos1, 800),
                        #      (overlay_set_size, reg1, pos1),
                        #      (store_sub, ":pos_y_default", ":pos_y", 55),
                        #      (position_set_x, pos1, ":pos_x"),
                        #      (position_set_y, pos1, ":pos_y_default"),
                        #      (overlay_set_position, reg1, pos1),
                        #      (store_add, ":slot_no_default", ":slot_no", 16),
                        #      (troop_set_slot, "trp_temp_array_c", ":slot_no_default", reg1),
                        #      (troop_set_slot, "trp_temp_array_b", ":slot_no_default", ":troop_no"),
                        #
                        #      (val_sub, ":pos_x", 90),
                        #      (val_add, ":pos_y", 10),
                        #      (store_mul, ":cur_troop", ":troop_no", 2), #with weapons
                        #      (create_image_button_overlay_with_tableau_material, reg1, -1, "tableau_game_party_window", ":cur_troop"),
                        #      (position_set_x, pos1, 600),
                        #      (position_set_y, pos1, 600),
                        #      (overlay_set_size, reg1, pos1),
                        #      (position_set_x, pos1, ":pos_x"),
                        #      (position_set_y, pos1, ":pos_y"),
                        #      (overlay_set_position, reg1, pos1),
                        #      (troop_set_slot, "trp_temp_array_a", ":slot_no", reg1),
                        #  ]),
                        ##
                        
                        ("prsnt_upgrade_tree_troop_cost",
                          [
                            (store_script_param, ":troop_no", 1),
                            (store_script_param, ":pos_x", 2),
                            (store_script_param, ":pos_y", 3),
                            
                            (call_script, "script_game_get_upgrade_cost", ":troop_no"),
                            
                            (create_text_overlay, reg1, "@{reg0}", tf_center_justify|tf_vertical_align_center),
                            (position_set_x, pos1, 800),
                            (position_set_y, pos1, 800),
                            (overlay_set_size, reg1, pos1),
                            (position_set_x, pos1, ":pos_x"),
                            (position_set_y, pos1, ":pos_y"),
                            (overlay_set_position, reg1, pos1),
                        ]),
                        
                        ("prsnt_lines",
                          [
                            (store_script_param, ":size_x", 1),
                            (store_script_param, ":size_y", 2),
                            (store_script_param, ":pos_x", 3),
                            (store_script_param, ":pos_y", 4),
                            
                            (create_mesh_overlay, reg1, "mesh_white_plane"),
                            (val_mul, ":size_x", 50),
                            (val_mul, ":size_y", 50),
                            (position_set_x, pos1, ":size_x"),
                            (position_set_y, pos1, ":size_y"),
                            (overlay_set_size, reg1, pos1),
                            (position_set_x, pos1, ":pos_x"),
                            (position_set_y, pos1, ":pos_y"),
                            (overlay_set_position, reg1, pos1),
                            (overlay_set_color, reg1, 0x000000),
                        ]),
                        
                        #Floris: The troop trees
                        ("prsnt_upgrade_tree_switch",
                          [
                            (store_trigger_param_1, ":object"),
                            (store_trigger_param_2, ":value"),
                            
                            (try_begin),
                              (eq, ":object", "$g_presentation_obj_1"),
                              (store_sub, "$temp_2", 9, ":value"),
								##Floris MTT begin
								(try_begin),
									(eq, "$troop_trees", troop_trees_0),
									(store_add, ":cur_presentation", "$temp_2", "prsnt_upgrade_tree_1"),
#									(start_presentation, "prsnt_upgrade_tree_1"),
								(else_try),
									(eq, "$troop_trees", troop_trees_1),
									(store_add, ":cur_presentation", "$temp_2", "prsnt_upgrade_tree_11"),
#									(start_presentation, "prsnt_upgrade_tree_11"),
								(else_try),
									(eq, "$troop_trees", troop_trees_2),
									(store_add, ":cur_presentation", "$temp_2", "prsnt_upgrade_tree_21"),
#									(start_presentation, "prsnt_upgrade_tree_21"),
								(try_end),
								##Floris MTT end
                              (start_presentation, ":cur_presentation"),
                            (else_try),
                              (eq, ":object", "$g_presentation_obj_5"),
                              (presentation_set_duration, 0),
                            (try_end),
                        ]),
                        ##
						
						("copy_inventory",
                          [
                            (store_script_param_1, ":source"),
                            (store_script_param_2, ":target"),
                            
                            (troop_clear_inventory, ":target"),
                            (troop_get_inventory_capacity, ":inv_cap", ":source"),
                            (try_for_range, ":i_slot", 0, ":inv_cap"),
                              (troop_get_inventory_slot, ":item", ":source", ":i_slot"),
                              (troop_set_inventory_slot, ":target", ":i_slot", ":item"),
                              (troop_get_inventory_slot_modifier, ":imod", ":source", ":i_slot"),
                              (troop_set_inventory_slot_modifier, ":target", ":i_slot", ":imod"),
                              (troop_inventory_slot_get_item_amount, ":amount", ":source", ":i_slot"),
                              (gt, ":amount", 0),
                              (troop_inventory_slot_set_item_amount, ":target", ":i_slot", ":amount"),
                            (try_end),
                        ]),						
                        
					##diplomacy start+
					#Importing a script used in Custom Commander.  The inventory copying is used
					#as a clever way to make "unmodifiable" views of others' equipment (both the
					#PC and NPC have their inventory copied before viewing, and after the window
					#closes the copies are written back over the originals).
					  ("dplmc_copy_inventory",
						[
						  (store_script_param_1, ":source"),
						  (store_script_param_2, ":target"),

						  (troop_clear_inventory, ":target"),
						  (troop_get_inventory_capacity, ":inv_cap", ":source"),
						  (try_for_range, ":i_slot", 0, ":inv_cap"),
							(troop_get_inventory_slot, ":item", ":source", ":i_slot"),
							(troop_set_inventory_slot, ":target", ":i_slot", ":item"),
							(troop_get_inventory_slot_modifier, ":imod", ":source", ":i_slot"),
							(troop_set_inventory_slot_modifier, ":target", ":i_slot", ":imod"),
							(troop_inventory_slot_get_item_amount, ":amount", ":source", ":i_slot"),
							(gt, ":amount", 0),
							(troop_inventory_slot_set_item_amount, ":target", ":i_slot", ":amount"),
						  (try_end),
						]),
                        
                        ("move_prisoners_to_defeated_center",
                          [
                            (store_script_param, ":defeated_center", 1),
                            (store_script_param, ":winner_faction", 2),
                            
                            (try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
                              (troop_get_slot, ":kingdom_hero_party", ":kingdom_hero", slot_troop_leaded_party),
                              (gt, ":kingdom_hero_party", 0),
                              (store_distance_to_party_from_party, ":dist", ":kingdom_hero_party", ":defeated_center"),
                              (lt, ":dist", 5),
                              (store_faction_of_party, ":kingdom_hero_party_faction", ":kingdom_hero_party"),
                              (eq, ":winner_faction", ":kingdom_hero_party_faction"),
                              (party_get_num_prisoner_stacks, ":num_stacks", ":kingdom_hero_party"),
                              (gt, ":num_stacks", 0),
                              (assign, "$g_move_heroes", 1),
                              (call_script, "script_party_prisoners_add_party_prisoners", ":defeated_center", ":kingdom_hero_party"),#Moving prisoners to the center
                              (assign, "$g_move_heroes", 1),
                              (call_script, "script_party_remove_all_prisoners", ":kingdom_hero_party"),
                            (try_end),
                        ]),
                        
                        ("calculate_ransom_for_party",
                          [
                            (store_script_param, ":party_no", 1),
                            
                            (assign, ":total_ransom_cost", 0),
                            (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
                            (try_begin),
                              (gt, ":num_stacks", 0),
                              (try_for_range, ":stack_no", 0, ":num_stacks"),
                                (party_stack_get_troop_id, ":troop_no", ":party_no", ":stack_no"),
                                (call_script, "script_game_get_join_cost", ":troop_no"),
                                (assign, ":ransom_cost", reg0),
                                (val_div, ":ransom_cost", 4),
                                (party_stack_get_size, ":stack_size", ":party_no", ":stack_no"),
                                (val_mul, ":ransom_cost", ":stack_size"),
                                (val_add, ":total_ransom_cost", ":ransom_cost"),
                              (try_end),
                            (try_end),
                            (assign, reg0, ":total_ransom_cost"),
                        ]),
                        
                        ("process_ransom_for_party",
                          [
                            (store_script_param, ":party_no", 1),
                            
                            (store_faction_of_party, ":party_cur_faction", ":party_no"),##Floris: Updated from CC 1.321.
                            (store_faction_of_party, ":party_faction", ":party_no"),
                            (party_get_slot, ":party_type",":party_no", slot_party_type),
                            (try_begin),
                              (eq, ":party_type", spt_kingdom_hero_party),
                              (party_stack_get_troop_id, ":leader", ":party_no"),
                              (ge, ":leader", 0),
                              (troop_get_slot, ":party_faction",  ":leader", slot_troop_original_faction),
                              (store_troop_faction, ":party_cur_faction", ":leader"),##Floris: Updated from CC 1.321.
                            (try_end),
                            
                            (try_begin),
                              (eq, ":party_faction", "fac_player_supporters_faction"),##Floris: From Custom Commander?
                              (party_get_slot, ":town_lord", ":party_no", slot_town_lord),
                              (try_begin),
                                (gt, ":town_lord", 0),
                                (troop_get_slot, ":party_faction", ":town_lord", slot_troop_original_faction),
                              (else_try),
                                (party_get_slot, ":party_faction", ":party_no", slot_center_original_faction),
                              (try_end),
                            (try_end),
                            
                            ##Floris: Updated from CC 1.321.
                            # combine same troops from prisoners
                            (call_script, "script_combine_same_troops_from_prisoners", ":party_no"),
                            ##
                            
                            (party_clear, "p_temp_party"),
                            (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
                            (try_for_range_backwards, ":stack_no", 0, ":num_stacks"),
                              (party_stack_get_troop_id, ":troop_no", ":party_no", ":stack_no"),
                              (neg|troop_is_hero, ":troop_no"),
                              (assign, ":contiue", 0),
                              (try_begin),
                                (is_between, ":troop_no", kingdom_troops_begin, kingdom_troops_end),
                                (store_troop_faction, ":troop_faction", ":troop_no"),
                                (neq, ":troop_faction", ":party_faction"),
                                (neq, ":troop_faction", ":party_cur_faction"),##Floris: Updated from CC 1.321.
                                (assign, ":contiue", 1),
                              (else_try),
                                (this_or_next|eq, ":troop_no", "trp_caravan_master"),
								##Floris MTT begin
								(troop_get_slot,":mercenary_townsman","$troop_trees",slot_mercenary_townsman),
								(troop_get_slot,":mercenary_extra5","$troop_trees",slot_mercenary_extra5),
                                (is_between, ":troop_no", ":mercenary_townsman", ":mercenary_extra5"),
								##Floris MTT end
                                (assign, ":contiue", 1),
                              (try_end),
                              (eq, ":contiue", 1),
                              (party_stack_get_size, ":stack_size", ":party_no", ":stack_no"),
                              (lt, ":stack_size", 20),##Floris: Updated from CC 1.321 to 10, and from 1.324 to 20.
                              (party_remove_members, ":party_no", ":troop_no", ":stack_size"),
                              (party_add_members, "p_temp_party", ":troop_no", ":stack_size"),
                            (try_end),
                            (party_get_num_prisoner_stacks, ":prisoner_stacks", ":party_no"),
                            (try_for_range_backwards, ":prisoner_stack_no", 0, ":prisoner_stacks"),
                              (party_prisoner_stack_get_troop_id, ":prisoner_troop_no", ":party_no", ":prisoner_stack_no"),
                              (neg|troop_is_hero, ":prisoner_troop_no"),
                              (assign, ":contiue", 0),
                              (try_begin),
                                (is_between, ":prisoner_troop_no", kingdom_troops_begin, kingdom_troops_end),
                                (store_troop_faction, ":troop_faction", ":prisoner_troop_no"),
                                (neq, ":troop_faction", ":party_faction"),
                                (neq, ":troop_faction", ":party_cur_faction"),##Floris: Updated from CC 1.321.
                                (assign, ":contiue", 1),
                              (else_try),
                                (this_or_next|eq, ":prisoner_troop_no", "trp_caravan_master"),
								##Floris MTT begin
								(troop_get_slot,":mercenary_townsman","$troop_trees",slot_mercenary_townsman),
								(troop_get_slot,":mercenary_extra5","$troop_trees",slot_mercenary_extra5),
                                (is_between, ":prisoner_troop_no", ":mercenary_townsman", ":mercenary_extra5"),
								##Floris MTT end
                                (assign, ":contiue", 1),
                              (try_end),
                              (eq, ":contiue", 1),
                              (party_prisoner_stack_get_size, ":prisoner_stack_size", ":party_no", ":prisoner_stack_no"),
                              (party_remove_prisoners, ":party_no", ":prisoner_troop_no", ":prisoner_stack_size"),
                              (party_add_members, "p_temp_party", ":prisoner_troop_no", ":prisoner_stack_size"),
                            (try_end),
                            (call_script, "script_calculate_ransom_for_party", "p_temp_party"),
                            (set_trigger_result, reg0),
                        ]),
                        
                        ##Floris: Updated from CC 1.321.
                        ("combine_same_troops_from_prisoners",
                          [
                            (store_script_param, ":party_no", 1),
                            
                            (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
                            (try_for_range, ":stack_no", 0, ":num_stacks"),
                              (party_stack_get_troop_id, ":troop_no", ":party_no", ":stack_no"),
                              (neg|troop_is_hero, ":troop_no"),
                              (party_get_num_prisoner_stacks, ":prisoner_stacks", ":party_no"),
                              (try_for_range, ":prisoner_stack_no", 0, ":prisoner_stacks"),
                                (party_prisoner_stack_get_troop_id, ":prisoner_troop_no", ":party_no", ":prisoner_stack_no"),
                                (eq, ":prisoner_troop_no", ":troop_no"),
                                (party_prisoner_stack_get_size, ":prisoner_stack_size", ":party_no", ":prisoner_stack_no"),
                                (party_remove_prisoners, ":party_no", ":prisoner_troop_no", ":prisoner_stack_size"),
                                (party_add_members, ":party_no", ":prisoner_troop_no", ":prisoner_stack_size"),
                              (try_end),
                            (try_end),
                        ]),
                        ##
                        
                        ("process_outlaws_for_party",
                          [
                            (store_script_param, ":party_no", 1),
                            
                            (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
                            (try_for_range_backwards, ":stack_no", 0, ":num_stacks"),
                              (party_stack_get_troop_id, ":troop_no", ":party_no", ":stack_no"),
                              (neg|troop_is_hero, ":troop_no"),
                               ##Floris MTT begin
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
							   (is_between, ":troop_no", ":outlaws_begin", ":outlaws_end"), ## changed from outlaws_troops_begin to outlaws_troops_end
							   ##Floris MTT end
                              (party_stack_get_size, ":stack_size", ":party_no", ":stack_no"),
                              (party_remove_members, ":party_no", ":troop_no", ":stack_size"),
                              (party_add_prisoners, ":party_no", ":troop_no", ":stack_size"),
                            (try_end),
                        ]),
                        
                        ("get_lord_weekly_income",
                          [
                            (store_script_param, ":troop_no", 1),
                            
                            (assign, ":weekly_income", 750), #let every hero receive 750 denars by default
                            
                            (store_character_level, ":troop_level", ":troop_no"),
                            (store_mul, ":level_income", ":troop_level", 10),
                            (val_add, ":weekly_income", ":level_income"),
                            
                            (store_troop_faction,":faction_no", ":troop_no"),
                            (try_begin), #check if troop is kingdom leader
                              (faction_slot_eq, ":faction_no", slot_faction_leader, ":troop_no"),
                              (val_add, ":weekly_income", 1000),
                            (try_end),
                            
                            (try_begin), #check if troop is marshall
                              (faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
                              (val_add, ":weekly_income", 1000),
                            (try_end),
                            
                            #     ## CC
                            #     (store_character_level, ":troop_level", "trp_player"),
                            #     (val_mul, ":troop_level", 2),
                            #     (val_add, ":troop_level", 100),
                            #     (val_mul, ":weekly_income", ":troop_level"),
                            #     (val_div, ":weekly_income", 100),
                            #     ## CC
                            (assign, reg0, ":weekly_income"),
                        ]),
                        
                        # script_get_total_equipment_weight:
                        # INPUT:
                        # param1: troop_no
                        # OUTPUT: total equipment weight
                        ("get_total_equipment_weight",
                          [
                            (store_script_param_1, ":troop_no"),
                            
                            (assign, ":total_weight", 0),
                            (try_for_range, ":cur_slot", 0, 8),#equipment slots
                              (troop_get_inventory_slot, ":cur_item", ":troop_no", ":cur_slot"),
                              (ge, ":cur_item", 0),
                              (item_get_slot, ":cur_item_weight", ":cur_item", slot_item_weight),
                              (val_add, ":total_weight", ":cur_item_weight"),
                            (try_end),
                            (val_div, ":total_weight", 100),
                            (assign, reg0, ":total_weight"),
                        ]),
                        
                        ("get_current_item_for_autoloot",
                          [
                            (store_script_param_1, ":slot_no"), #CC 1.324
                            
                            (troop_get_inventory_slot, ":item", "$temp", ":slot_no"), #CC 1.324
                            ##CC disabled in 1.324
                            #    (store_script_param_1, ":wpn_set"),
                            #    (store_script_param_2, ":slot_no"),
                            #
                            #    (try_begin),
                            #      (eq, ":wpn_set", 0),
                            #      (assign, ":dest_slot", ":slot_no"),
                            #      (troop_get_inventory_slot, ":item", "$temp", ":dest_slot"),
                            #    (else_try),
                            #      (store_sub, ":dest_slot", "$temp", companions_begin),
                            #      (val_mul, ":dest_slot", 4),
                            #      (val_add, ":dest_slot", 10),
                            #      (val_add, ":dest_slot", ":slot_no"),
                            #      (troop_get_inventory_slot, ":item", "trp_merchants_end", ":dest_slot"),
                            #    (try_end),
                            ##
                            (try_begin),
                              (ge, ":item", 0),
                              (str_store_item_name, s10, ":item"),
                            (else_try),
                              (str_store_string, s10, "str_none"),
                            (try_end),
                        ]),
                        
                        ("get_town_faction_for_recruiting",
                          [
                            (store_script_param, ":party_no", 1),
                                  
							
                            (try_begin), ##CABA addition, this first try section, for Diplomacy-set cultures
							  (is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),
                              (is_between, "$g_player_culture", kingdoms_begin, kingdoms_end), #Player Faction
  							  (assign, ":party_faction", "$g_player_culture"),
							(else_try),
                              (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end), #Player Faction
                              (assign, ":party_faction", "$players_kingdom"),
                            (else_try),
                              (is_between, "$supported_pretender", pretenders_begin, pretenders_end),
                              (assign, ":party_faction", "$supported_pretender_old_faction"),
                            (else_try),
                              (party_get_slot, ":party_faction", ":party_no", slot_center_original_faction),
                            (try_end),
                            (assign, reg0, ":party_faction"),
                        ]),
                        
                        ("get_dest_color_from_rgb",
                          [
                            (store_script_param, ":red", 1),
                            (store_script_param, ":green", 2),
                            (store_script_param, ":blue", 3),
                            
                            (assign, ":cur_color", 0xFF000000),
                            (val_mul, ":green", 0x100),
                            (val_mul, ":red", 0x10000),
                            (val_add, ":cur_color", ":blue"),
                            (val_add, ":cur_color", ":green"),
                            (val_add, ":cur_color", ":red"),
                            (assign, reg0, ":cur_color"),
                        ]),
                        
                        ("convert_rgb_code_to_html_code",
                          [
                            (store_script_param, ":red", 1),
                            (store_script_param, ":green", 2),
                            (store_script_param, ":blue", 3),
                            
                            (str_store_string, s0, "@#"),
                              
                              (store_div, ":r_1", ":red", 0x10),
                              (store_add, ":dest_string", "str_key_0", ":r_1"),
                              (str_store_string, s1, ":dest_string"),
                              (str_store_string, s0, "@{s0}{s1}"),
                              
                              (store_mod, ":r_2", ":red", 0x10),
                              (store_add, ":dest_string", "str_key_0", ":r_2"),
                              (str_store_string, s1, ":dest_string"),
                              (str_store_string, s0, "@{s0}{s1}"),
                              
                              (store_div, ":g_1", ":green", 0x10),
                              (store_add, ":dest_string", "str_key_0", ":g_1"),
                              (str_store_string, s1, ":dest_string"),
                              (str_store_string, s0, "@{s0}{s1}"),
                              
                              (store_mod, ":g_2", ":green", 0x10),
                              (store_add, ":dest_string", "str_key_0", ":g_2"),
                              (str_store_string, s1, ":dest_string"),
                              (str_store_string, s0, "@{s0}{s1}"),
                              
                              (store_div, ":b_1", ":blue", 0x10),
                              (store_add, ":dest_string", "str_key_0", ":b_1"),
                              (str_store_string, s1, ":dest_string"),
                              (str_store_string, s0, "@{s0}{s1}"),
                              
                              (store_mod, ":b_2", ":blue", 0x10),
                              (store_add, ":dest_string", "str_key_0", ":b_2"),
                              (str_store_string, s1, ":dest_string"),
                              (str_store_string, s0, "@{s0}{s1}"),
                          ]),
                          
                          ("convert_slot_no_to_color",
                            [
                              (store_script_param, ":cur_color", 1),
                              
                              (store_mod, ":blue", ":cur_color", 6),
                              (val_div, ":cur_color", 6),
                              (store_mod, ":green", ":cur_color", 6),
                              (val_div, ":cur_color", 6),
                              (store_mod, ":red", ":cur_color", 6),
                              (val_mul, ":blue", 0x33),
                              (val_mul, ":green", 0x33),
                              (val_mul, ":red", 0x33),
                              (assign, ":dest_color", 0xFF000000),
                              (val_mul, ":green", 0x100),
                              (val_mul, ":red", 0x10000),
                              (val_add, ":dest_color", ":blue"),
                              (val_add, ":dest_color", ":green"),
                              (val_add, ":dest_color", ":red"),
                              (assign, reg0, ":dest_color"),
                          ]),
                          
                          #("init_keys_array", keys_array()),
                          
                          ("move_one_stack_to_the_bottom",
                            [
                              (store_script_param, ":party_no", 1),
                              (store_script_param, ":stack_no", 2),
                              (store_script_param, ":times", 3),
                              
                              (try_for_range, ":unused", 0, ":times"),
                                (party_stack_get_troop_id, ":troop_no", ":party_no", ":stack_no"),
                                (party_stack_get_size, ":stack_size", ":party_no", ":stack_no"),
                                (party_stack_get_num_wounded, ":num_wounded", ":party_no", ":stack_no"),
                                (party_remove_members, ":party_no", ":troop_no", ":stack_size"),
                                (party_add_members, ":party_no", ":troop_no", ":stack_size"),
                                (party_wound_members, ":party_no", ":troop_no", ":num_wounded"),
                              (try_end),
                          ]),
                          
                            ("centers_init_bandit_leader_quest",
                              [
                                (try_for_range, ":cur_center", centers_begin, centers_end),
                                  (party_get_slot, ":original_faction", ":cur_center", slot_center_original_faction),
                                  (store_sub, ":off_set", ":original_faction", "fac_kingdom_1"),
                                  (store_add, ":dest_quest", ":off_set", "qst_deal_with_forest_bandit"),
								##Floris MTT begin
								(try_begin),
									(eq, "$troop_trees", troop_trees_0),
                                  (store_add, ":dest_pt_no", ":off_set", "pt_forest_bandits"),
								(else_try),
									(eq, "$troop_trees", troop_trees_1),
                                  (store_add, ":dest_pt_no", ":off_set", "pt_forest_bandits_r"),
								(else_try),
									(eq, "$troop_trees", troop_trees_2),
                                  (store_add, ":dest_pt_no", ":off_set", "pt_forest_bandits_e"),
								(try_end),
								##Floris MTT end
                                  (party_set_slot, ":cur_center", slot_center_bandit_leader_quest, ":dest_quest"),
                                  (party_set_slot, ":cur_center", slot_center_bandit_leader_pt_no, ":dest_pt_no"),
                                (try_end),
                                # party templats
				##Floris MTT begin
				(try_begin),
		 			(eq, "$troop_trees", troop_trees_0),
                                (party_template_set_slot, "pt_forest_bandits",   slot_party_template_spawn_point, "p_forest_bandit_spawn_point"),
                                (party_template_set_slot, "pt_taiga_bandits",    slot_party_template_spawn_point, "p_taiga_bandit_spawn_point"),
                                (party_template_set_slot, "pt_steppe_bandits",   slot_party_template_spawn_point, "p_steppe_bandit_spawn_point"),
                                (party_template_set_slot, "pt_sea_raiders",      slot_party_template_spawn_point, "p_sea_raider_spawn_point_1"),
                                (party_template_set_slot, "pt_mountain_bandits", slot_party_template_spawn_point, "p_mountain_bandit_spawn_point"),
                                (party_template_set_slot, "pt_desert_bandits",   slot_party_template_spawn_point, "p_desert_bandit_spawn_point"),
                          
                                (party_template_set_slot, "pt_forest_bandits",   slot_party_template_hero_id, "trp_forest_bandit_hero"),
                                (party_template_set_slot, "pt_taiga_bandits",    slot_party_template_hero_id, "trp_taiga_bandit_hero"),
                                (party_template_set_slot, "pt_steppe_bandits",   slot_party_template_hero_id, "trp_steppe_bandit_hero"),
                                (party_template_set_slot, "pt_sea_raiders",      slot_party_template_hero_id, "trp_sea_raider_hero"),
                                (party_template_set_slot, "pt_mountain_bandits", slot_party_template_hero_id, "trp_mountain_bandit_hero"),
                                (party_template_set_slot, "pt_desert_bandits",   slot_party_template_hero_id, "trp_desert_bandit_hero"),
                          
                                (party_template_set_slot, "pt_forest_bandits",   slot_party_template_hero_name_begin, "str_bandit_name_10"),
                                (party_template_set_slot, "pt_taiga_bandits",    slot_party_template_hero_name_begin, "str_bandit_name_20"),
                                (party_template_set_slot, "pt_steppe_bandits",   slot_party_template_hero_name_begin, "str_bandit_name_30"),
                                (party_template_set_slot, "pt_sea_raiders",      slot_party_template_hero_name_begin, "str_bandit_name_40"),
                                (party_template_set_slot, "pt_mountain_bandits", slot_party_template_hero_name_begin, "str_bandit_name_50"),
                                (party_template_set_slot, "pt_desert_bandits",   slot_party_template_hero_name_begin, "str_bandit_name_60"),
				(else_try),
		 			(eq, "$troop_trees", troop_trees_1),
                                (party_template_set_slot, "pt_forest_bandits_r",   slot_party_template_spawn_point, "p_forest_bandit_spawn_point"),
                                (party_template_set_slot, "pt_taiga_bandits_r",    slot_party_template_spawn_point, "p_taiga_bandit_spawn_point"),
                                (party_template_set_slot, "pt_steppe_bandits_r",   slot_party_template_spawn_point, "p_steppe_bandit_spawn_point"),
                                (party_template_set_slot, "pt_sea_raiders_r",      slot_party_template_spawn_point, "p_sea_raider_spawn_point_1"),
                                (party_template_set_slot, "pt_mountain_bandits_r", slot_party_template_spawn_point, "p_mountain_bandit_spawn_point"),
                                (party_template_set_slot, "pt_desert_bandits_r",   slot_party_template_spawn_point, "p_desert_bandit_spawn_point"),
                          
                                (party_template_set_slot, "pt_forest_bandits_r",   slot_party_template_hero_id, "trp_forest_bandit_hero"),
                                (party_template_set_slot, "pt_taiga_bandits_r",    slot_party_template_hero_id, "trp_taiga_bandit_hero"),
                                (party_template_set_slot, "pt_steppe_bandits_r",   slot_party_template_hero_id, "trp_steppe_bandit_hero"),
                                (party_template_set_slot, "pt_sea_raiders_r",      slot_party_template_hero_id, "trp_sea_raider_hero"),
                                (party_template_set_slot, "pt_mountain_bandits_r", slot_party_template_hero_id, "trp_mountain_bandit_hero"),
                                (party_template_set_slot, "pt_desert_bandits_r",   slot_party_template_hero_id, "trp_desert_bandit_hero"),
                          
                                (party_template_set_slot, "pt_forest_bandits_r",   slot_party_template_hero_name_begin, "str_bandit_name_10"),
                                (party_template_set_slot, "pt_taiga_bandits_r",    slot_party_template_hero_name_begin, "str_bandit_name_20"),
                                (party_template_set_slot, "pt_steppe_bandits_r",   slot_party_template_hero_name_begin, "str_bandit_name_30"),
                                (party_template_set_slot, "pt_sea_raiders_r",      slot_party_template_hero_name_begin, "str_bandit_name_40"),
                                (party_template_set_slot, "pt_mountain_bandits_r", slot_party_template_hero_name_begin, "str_bandit_name_50"),
                                (party_template_set_slot, "pt_desert_bandits_r",   slot_party_template_hero_name_begin, "str_bandit_name_60"),
				(else_try),
					(eq, "$troop_trees", troop_trees_2),
                                (party_template_set_slot, "pt_forest_bandits_e",   slot_party_template_spawn_point, "p_forest_bandit_spawn_point"),
                                (party_template_set_slot, "pt_taiga_bandits_e",    slot_party_template_spawn_point, "p_taiga_bandit_spawn_point"),
                                (party_template_set_slot, "pt_steppe_bandits_e",   slot_party_template_spawn_point, "p_steppe_bandit_spawn_point"),
                                (party_template_set_slot, "pt_sea_raiders_e",      slot_party_template_spawn_point, "p_sea_raider_spawn_point_1"),
                                (party_template_set_slot, "pt_mountain_bandits_e", slot_party_template_spawn_point, "p_mountain_bandit_spawn_point"),
                                (party_template_set_slot, "pt_desert_bandits_e",   slot_party_template_spawn_point, "p_desert_bandit_spawn_point"),
                          
                                (party_template_set_slot, "pt_forest_bandits_e",   slot_party_template_hero_id, "trp_forest_bandit_hero"),
                                (party_template_set_slot, "pt_taiga_bandits_e",    slot_party_template_hero_id, "trp_taiga_bandit_hero"),
                                (party_template_set_slot, "pt_steppe_bandits_e",   slot_party_template_hero_id, "trp_steppe_bandit_hero"),
                                (party_template_set_slot, "pt_sea_raiders_e",      slot_party_template_hero_id, "trp_sea_raider_hero"),
                                (party_template_set_slot, "pt_mountain_bandits_e", slot_party_template_hero_id, "trp_mountain_bandit_hero"),
                                (party_template_set_slot, "pt_desert_bandits_e",   slot_party_template_hero_id, "trp_desert_bandit_hero"),
                          
                                (party_template_set_slot, "pt_forest_bandits_e",   slot_party_template_hero_name_begin, "str_bandit_name_10"),
                                (party_template_set_slot, "pt_taiga_bandits_e",    slot_party_template_hero_name_begin, "str_bandit_name_20"),
                                (party_template_set_slot, "pt_steppe_bandits_e",   slot_party_template_hero_name_begin, "str_bandit_name_30"),
                                (party_template_set_slot, "pt_sea_raiders_e",      slot_party_template_hero_name_begin, "str_bandit_name_40"),
                                (party_template_set_slot, "pt_mountain_bandits_e", slot_party_template_hero_name_begin, "str_bandit_name_50"),
                                (party_template_set_slot, "pt_desert_bandits_e",   slot_party_template_hero_name_begin, "str_bandit_name_60"),
				(try_end),
				##Floris MTT end
                              ]),
                          
                          ("sort_party_by_troop_level",
                            [
                              (store_script_param, ":party_no", 1),
                              (store_script_param, ":first_stack", 2),
                              
                              (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
                              (try_begin),
                                (gt, ":num_stacks", ":first_stack"),
                                (assign, ":last_stack", ":num_stacks"),
                                
                                # start to sort
                                (store_sub, ":num_times", ":num_stacks", ":first_stack"),
                                (try_for_range, ":unused", 0, ":num_times"),
                                  # find highest-level troop
                                  # level*3 with extra bonuse to differentiate troop types with the same level
                                  (assign, ":best_stack", -1),
                                  (assign, ":best_level", -1),
                                  (try_for_range, ":cur_stack", ":first_stack", ":last_stack"),
                                    (party_stack_get_troop_id, ":cur_troop", ":party_no", ":cur_stack"),
                                    (store_character_level, ":troop_level", ":cur_troop"),
                                    (val_mul, ":troop_level", 3),
                                    (try_begin),
                                      (troop_is_guarantee_horse, ":cur_troop"),
                                      (val_add, ":troop_level", 2), # horseman
                                    (else_try),
                                      (troop_is_guarantee_ranged, ":cur_troop"), # archers
                                    (else_try),
                                      (val_add, ":troop_level", 1), # footman
                                    (try_end),
                                    (gt, ":troop_level", ":best_level"),
                                    (assign, ":best_level", ":troop_level"),
                                    (assign, ":best_stack", ":cur_stack"),
                                  (try_end),
                                  # move to the end
                                  (try_begin),
                                    (gt, ":best_level", -1),
                                    (party_stack_get_troop_id, ":stack_troop", ":party_no", ":best_stack"),
                                    (party_stack_get_size, ":stack_size", ":party_no", ":best_stack"),
                                    (party_stack_get_num_wounded, ":num_wounded", ":party_no", ":best_stack"),
                                    (party_remove_members, ":party_no", ":stack_troop", ":stack_size"),
                                    (party_add_members, ":party_no", ":stack_troop", ":stack_size"),
                                    (party_wound_members, ":party_no", ":stack_troop", ":num_wounded"),
                                    (val_sub, ":last_stack", 1),
                                  (try_end),
                                (try_end),
                              (try_end),
                          ]),
                          
                          # script_update_order_panel_map
                          # Input: none
                          # Output: none
                          ("update_order_panel_map",
                            [
                              (set_fixed_point_multiplier, 1000),
                              
                              (get_scene_boundaries, pos2, pos3),
                              (try_for_agents,":cur_agent"),
                                (agent_is_human, ":cur_agent"),
                                (agent_get_slot, ":agent_overlay", ":cur_agent", slot_agent_map_overlay_id),
                                (try_begin),
                                  (agent_is_alive, ":cur_agent"),
                                  (call_script, "script_update_agent_position_on_map", ":cur_agent"),
                                (else_try),
                                  (overlay_set_alpha, ":agent_overlay", 0),
                                (try_end),
                              (try_end),
                              (try_begin),
                                (scene_prop_get_instance, ":player_chest", "spr_inventory", 0),
                                (ge, ":player_chest", 0),
                                (prop_instance_get_position, pos1, ":player_chest"),
                                (call_script, "script_convert_3d_pos_to_map_pos"),
                                (overlay_set_position, "$g_presentation_obj_39", pos0),
                              (try_end),
                          ]),
                          
                          # script_convert_map_pos_to_3d_pos
                          ("convert_map_pos_to_3d_pos",
                            [
                              (set_fixed_point_multiplier, 1000),
                              (store_sub, ":map_x", 980, "$g_battle_map_width"),
                              (store_sub, ":map_y", 730, "$g_battle_map_height"),
                              (position_get_x, ":point_x_pos", pos1),
                              (position_get_y, ":point_y_pos", pos1),
                              (val_sub, ":point_x_pos", ":map_x"),
                              (val_sub, ":point_y_pos", ":map_y"),
                              (val_mul, ":point_x_pos", "$g_battle_map_scale"),
                              (val_mul, ":point_y_pos", "$g_battle_map_scale"),
                              (position_set_x, pos3, ":point_x_pos"),
                              (position_set_y, pos3, ":point_y_pos"),
                              (set_fixed_point_multiplier, 1000),
                              (position_transform_position_to_parent, pos0, pos2, pos3),
                          ]),
                          
                          ("update_agent_hp_bar",
                            [
                              (set_fixed_point_multiplier, 1000),
                              
                              (get_player_agent_no, ":player_agent"),
                              (try_for_agents,":agent_no"),
                                (agent_is_human, ":agent_no"),
                                (neq, ":agent_no", ":player_agent"),
                                (agent_get_slot, ":agent_hp_overlay", ":agent_no", slot_agent_hp_bar_overlay_id),
                                (agent_get_slot, ":agent_hp_bg_overlay", ":agent_no", slot_agent_hp_bar_bg_overlay_id),
                                (try_begin),
                                  (agent_is_alive, ":agent_no"),
                                  (agent_get_slot, ":agent_hp_overlay", ":agent_no", slot_agent_hp_bar_overlay_id),
                                  (agent_get_slot, ":agent_hp_bg_overlay", ":agent_no", slot_agent_hp_bar_bg_overlay_id),
                                  (try_begin),
                                    (le, ":agent_hp_overlay", 0),
                                    (le, ":agent_hp_bg_overlay", 0),
                                    (set_fixed_point_multiplier, 1000),
                                    # hp bg
                                    (create_mesh_overlay, reg1, "mesh_white_plane"),
                                    (overlay_set_alpha, reg1, 0x44),
                                    (agent_set_slot, ":agent_no", slot_agent_hp_bar_bg_overlay_id, reg1),
                                    (assign, ":agent_hp_bg_overlay", reg1),
                                    # hp
                                    (create_mesh_overlay, reg1, "mesh_white_plane"),
                                    (overlay_set_alpha, reg1, 0x44),
                                    (agent_set_slot, ":agent_no", slot_agent_hp_bar_overlay_id, reg1),
                                    (assign, ":agent_hp_overlay", reg1),
                                  (try_end),
                                  
                                  # color
                                  (agent_get_team, ":player_team", ":player_agent"),
                                  (agent_get_team, ":agent_team", ":agent_no"),
                                  (try_begin),
                                    (eq, ":agent_team", ":player_team"),
                                    (overlay_set_color, ":agent_hp_overlay", 0x00FF00),
                                  (else_try),
                                    (agent_is_ally, ":agent_no"),
                                    (overlay_set_color, ":agent_hp_overlay", 0x0000FF),
                                  (else_try),
                                    (overlay_set_color, ":agent_hp_overlay", 0xFF0000),
                                  (try_end),
                                  (overlay_set_color, ":agent_hp_bg_overlay", 0x000000),
                                  
                                  # size & position
                                  (agent_get_position, pos1, ":agent_no"),
                                  (agent_get_horse, ":horse_agent", ":agent_no"),
                                  (try_begin),
                                    (ge, ":horse_agent", 0),
                                    (position_move_z, pos1, 280, 1),
                                  (else_try),
                                    (position_move_z, pos1, 180, 1),
                                  (try_end),
                                  (position_get_screen_projection, pos2, pos1),
                                  (position_get_x, ":head_x_pos", pos2),
                                  (position_get_y, ":head_y_pos", pos2),
                                  # base size
                                  (copy_position, pos6, pos1),
                                  (copy_position, pos7, pos1),
                                  (position_move_z, pos7, 100, 1),
                                  (position_get_screen_projection, pos6, pos6),
                                  (position_get_screen_projection, pos7, pos7),
                                  (position_get_y, ":screen_y_pos_1", pos6),
                                  (position_get_y, ":screen_y_pos_2", pos7),
                                  (store_sub, ":base_x", ":screen_y_pos_2", ":screen_y_pos_1"),
                                  (val_clamp, ":base_x", 20, 161),
                                  (store_div, ":base_y", ":base_x", 20),
                                  (try_begin),
                                    (is_between, ":head_x_pos", -100, 1100),
                                    (is_between, ":head_y_pos", -100, 850),
                                    (agent_get_position, pos3, ":agent_no"),
                                    (agent_get_position, pos4, ":player_agent"),
                                    (get_distance_between_positions_in_meters, ":distance", pos3, pos4),
                                    (le, ":distance", "$g_hp_bar_dis_limit"),
                                    # agent no
                                    (agent_get_horse, ":horse_agent", ":agent_no"),
                                    (try_begin),
                                      (ge, ":horse_agent", 0),
                                      (position_move_z, pos3, 280, 1),
                                    (else_try),
                                      (position_move_z, pos3, 180, 1),
                                    (try_end),
                                    # player agent
                                    (agent_get_horse, ":player_horse", ":player_agent"),
                                    (try_begin),
                                      (ge, ":player_horse", 0),
                                      (position_move_z, pos4, 280, 1),
                                    (else_try),
                                      (position_move_z, pos4, 180, 1),
                                    (try_end),
                                    (position_move_z, pos3, 50, 1),
                                    (position_move_z, pos4, 50, 1),
                                    (position_has_line_of_sight_to_position, pos3, pos4),
                                    ## hp bg
                                    ## CC 1.322 disabled here, was active in native
                                    #(agent_get_troop_id, ":troop_id", ":agent_no"),
                                    #(try_begin),
                                    #(neg|troop_is_hero, ":troop_id"),
                                    #(call_script, "script_get_agent_backup_hp_times_factor", ":agent_no"),
                                    #(assign, ":hp_times_factor", reg0),
                                    #(else_try),
                                    #(troop_slot_eq, ":troop_id", slot_troop_occupation, slto_kingdom_hero),
                                    #(call_script, "script_get_troop_backup_hp_times_factor", ":troop_id"),
                                    #(assign, ":hp_times_factor", reg0),
                                    #(else_try),
                                    #(assign, ":hp_times_factor", 0),
                                    #(try_end),
                                    #(val_add,":hp_times_factor", 100),
                                    #(store_mul, ":x_offset", ":hp_times_factor", ":base_x"),
                                    #(val_div, ":x_offset", 100),
                                    (assign, ":x_offset", ":base_x"), ##This line was added in CC 1.322
                                    ##
                                    (val_div, ":x_offset", 2),
                                    (val_add, ":x_offset", 1),
                                    (store_sub, ":hp_bg_x", ":head_x_pos", ":x_offset"),
                                    (store_sub, ":hp_bg_y", ":head_y_pos", 1),
                                    (position_set_x, pos1, ":hp_bg_x"),
                                    (position_set_y, pos1, ":hp_bg_y"),
                                    (overlay_set_position, ":agent_hp_bg_overlay", pos1),
                                    #CC 1.322 diasbled here, but active in native
                                    #(store_mul, ":bg_width", ":hp_times_factor", ":base_x"),
                                    #(val_div, ":bg_width", 100),
                                    #(assign, ":bg_width", ":base_x"),
                                    #(val_add, ":bg_width", 2),
                                    (store_add, ":bg_width", ":base_x", 2), ## CC 1.322 added this line
                                    ##
                                    (val_mul, ":bg_width", 50),
                                    (store_add, ":bg_height", ":base_y", 2),
                                    (val_mul, ":bg_height", 50),
                                    (position_set_x, pos1, ":bg_width"),
                                    (position_set_y, pos1, ":bg_height"),
                                    (overlay_set_size, ":agent_hp_bg_overlay", pos1),
                                    ## hp
                                    (store_add, ":hp_x", ":hp_bg_x", 1),
                                    (store_add, ":hp_y", ":hp_bg_y", 1),
                                    (position_set_x, pos1, ":hp_x"),
                                    (position_set_y, pos1, ":hp_y"),
                                    (overlay_set_position, ":agent_hp_overlay", pos1),
                                    
                                    ## CC 1.322 disabled here, but active in native          #(try_begin),
                                    #(neg|troop_is_hero, ":troop_id"),
                                    #(agent_get_slot, ":backup_hp", ":agent_no", slot_agent_backup_hp),
                                    #(store_agent_hit_points, ":agent_hp",":agent_no", 1),
                                    #(store_add, ":total_hp", ":backup_hp", ":agent_hp"),
                                    #(call_script, "script_get_troop_max_hp", ":troop_id"),
                                    #(assign, ":max_hp", reg0),
                                    #(store_mul, ":hp_width", ":total_hp", 50),
                                    #(val_mul, ":hp_width", ":base_x"),
                                    #(val_div, ":hp_width", ":max_hp"),
                                    #(else_try),
                                    #(troop_slot_eq, ":troop_id", slot_troop_occupation, slto_kingdom_hero),
                                    #(troop_get_slot, ":backup_hp", ":troop_id", slot_troop_backup_hp),
                                    #(store_agent_hit_points, ":agent_hp",":agent_no", 1),
                                    #(store_add, ":total_hp", ":backup_hp", ":agent_hp"),
                                    #(call_script, "script_get_troop_max_hp", ":troop_id"),
                                    #(assign, ":max_hp", reg0),
                                    #(store_mul, ":hp_width", ":total_hp", 50),
                                    #(val_mul, ":hp_width", ":base_x"),
                                    #(val_div, ":hp_width", ":max_hp"),
                                    #(else_try),
                                    ##
                                    (store_agent_hit_points, ":agent_hp",":agent_no"),
                                    (store_mul, ":hp_width", ":agent_hp", 50),
                                    (val_mul, ":hp_width", ":base_x"),
                                    (val_div, ":hp_width", 100),
                                    #          (try_end), ## CC 1.322, ah, disabled this line too.
                                    (val_min, ":hp_width", ":bg_width"),
                                    (store_mul, ":hp_height", ":base_y", 50),
                                    (position_set_x, pos1, ":hp_width"),
                                    (position_set_y, pos1, ":hp_height"),
                                    (overlay_set_size, ":agent_hp_overlay", pos1),
                                    
                                    (try_begin),
                                      (agent_is_ally, ":agent_no"),
                                      (store_mul, ":dest_alpha", "$g_hp_bar_ally", 0x44),
                                    (else_try),
                                      (store_mul, ":dest_alpha", "$g_hp_bar_enemy", 0x44),
                                    (try_end),
                                    (overlay_set_alpha, ":agent_hp_overlay", ":dest_alpha"),
                                    (overlay_set_alpha, ":agent_hp_bg_overlay", ":dest_alpha"),
                                  (else_try),
                                    (overlay_set_alpha, ":agent_hp_overlay", 0),
                                    (overlay_set_alpha, ":agent_hp_bg_overlay", 0),
                                  (try_end),
                                (else_try),
                                  (overlay_set_alpha, ":agent_hp_overlay", 0),
                                  (overlay_set_alpha, ":agent_hp_bg_overlay", 0),
                                (try_end),
                              (try_end),
                          ]),
                          
                          ## CC 1.322, disabled here, but active in native
                          #("get_troop_backup_hp_times_factor",
                          #[
                          #(store_script_param, ":troop_no", 1),
                          
                          #(store_character_level, ":troop_level", ":troop_no"),
                          #(store_mul, ":backup_hp_factor", ":troop_level", 4),
                          #(assign, reg0, ":backup_hp_factor"),
                          #]),
                          
                          #("get_agent_backup_hp_times_factor",
                          #[
                          #(store_script_param, ":agent_no", 1),
                          
                          #(agent_get_party_id, ":party_no", ":agent_no"),
                          #(try_begin),
                          #(le, ":party_no", -1),
                          #(assign, ":backup_hp_factor", 0),
                          #(else_try),
                          #(party_stack_get_troop_id, ":leader", ":party_no", 0),
                          #(troop_is_hero, ":leader"),
                          #(store_skill_level, ":leadership_level", "skl_leadership", ":leader"),
                          #(store_mul, ":backup_hp_factor", ":leadership_level", 6),
                          #(try_begin),
                          #(eq, ":party_no", "p_main_party"),
                          #(agent_get_troop_id, ":troop_no", ":agent_no"),
                          #(call_script, "script_game_get_morale_of_troops_from_faction", ":troop_no"),
                          #(assign, ":troop_morale", reg0),
                          #(val_clamp, ":troop_morale", 0, 100),
                          #(val_mul, ":backup_hp_factor", ":troop_morale"),
                          #(val_div, ":backup_hp_factor", 99),
                          #(try_end),
                          #(else_try),
                          #(assign, ":backup_hp_factor", 0),
                          #(try_end),
                          #(assign, reg0, ":backup_hp_factor"),
                          #]),
                          ##
                          
                          ("get_character_background_text",
                            [
                              (str_clear,s1),
                              (assign, reg3, "$character_gender"),
                              ## father
                              (try_begin),
                                (eq, "$background_type", cb_noble),
                                (str_store_string,s2,"@an impoverished noble"),
                                (str_store_string,s3,"@You came into the world a {reg3?daughter:son} of declining nobility,\
                                  owning only the house in which they lived. However, despite your family's hardships,\
                                they afforded you a good education and trained you from childhood for the rigors of aristocracy and life at court."),
                              (else_try),
                                (eq, "$background_type", cb_merchant),
                                (str_store_string,s2,"@a travelling merchant"),
                                (str_store_string,s3,"@You were born the {reg3?daughter:son} of travelling merchants,\
                                  always moving from place to place in search of a profit. Although your parents were wealthier than most\
                                  and educated you as well as they could, you found little opportunity to make friends on the road,\
                                living mostly for the moments when you could sell something to somebody."),
                              (else_try),
                                (eq, "$background_type", cb_guard),
                                (str_store_string,s2,"@a veteran warrior"),
                                (str_store_string,s3,"@As a child, your family scrabbled out a meagre living from your father's wages\
                                  as a guardsman to the local lord. It was not an easy existence, and you were too poor to get much of an\
                                education. You learned mainly how to defend yourself on the streets, with or without a weapon in hand."),
                              (else_try),
                                (eq, "$background_type", cb_forester),
                                (str_store_string,s2,"@a hunter"),
                                (str_store_string,s3,"@You were the {reg3?daughter:son} of a family who lived off the woods,\
                                  doing whatever they needed to make ends meet. Hunting, woodcutting, making arrows,\
                                  even a spot of poaching whenever things got tight. Winter was never a good time for your family\
                                  as the cold took animals and people alike, but you always lived to see another dawn,\
                                though your brothers and sisters might not be so fortunate."),
                              (else_try),
                                (eq, "$background_type", cb_nomad),
                                (str_store_string,s2,"@a steppe nomad"),
                                (str_store_string,s3,"@You were a child of the steppe, born to a tribe of wandering nomads who lived\
                                  in great camps throughout the arid grasslands.\
                                  Like the other tribesmen, your family revered horses above almost everything else, and they taught you\
                                how to ride almost before you learned how to walk. "),
                              (else_try),
                                (eq, "$background_type", cb_thief),
                                (str_store_string,s2,"@a thief"),
                                (str_store_string,s3,"@As the {reg3?daughter:son} of a thief, you had very little 'formal' education.\
                                  Instead you were out on the street, begging until you learned how to cut purses, cutting purses\
                                  until you learned how to pick locks, all the way through your childhood.\
                                Still, these long years made you streetwise and sharp to the secrets of cities and shadowy backways."),
                              (try_end),
                              (str_store_string,s1,"@ You were born years ago, in a land far away. Your father was {s2}. {s3}"),
                              
                              ## early life
                              (try_begin),
                                (eq, "$background_answer_2", cb2_page),
                                (str_store_string,s2,"@a page at a nobleman's court"),
                                (str_store_string,s3,"@As a {reg3?girl:boy} growing out of childhood,\
                                  you were sent to live in the court of one of the nobles of the land.\
                                  There, your first lessons were in humility, as you waited upon the lords and ladies of the household.\
                                  But from their chess games, their gossip, even the poetry of great deeds and courtly love, you quickly began to learn about the adult world of conflict\
                                and competition. You also learned from the rough games of the other children, who battered at each other with sticks in imitation of their elders' swords."),
                              (else_try),
                                (eq, "$background_answer_2", cb2_apprentice),
                                (str_store_string,s2,"@a craftsman's apprentice"),
                                (str_store_string,s3,"@As a {reg3?girl:boy} growing out of childhood,\
                                  you apprenticed with a local craftsman to learn a trade. After years of hard work and study under your\
                                  new master, he promoted you to journeyman and employed you as a fully paid craftsman for as long as\
                                you wished to stay."),
                              (else_try),
                                (eq, "$background_answer_2", cb2_merchants_helper),
                                (str_store_string,s2,"@a shop assistant"),
                                (str_store_string,s3,"@As a {reg3?girl:boy} growing out of childhood,\
                                  you apprenticed to a wealthy merchant, picking up the trade over years of working shops and driving caravans.\
                                  You soon became adept at the art of buying low, selling high, and leaving the customer thinking they'd\
                                got the better deal."),
                              (else_try),
                                (eq, "$background_answer_2", cb2_urchin),
                                (str_store_string,s2,"@a street urchin"),
                                (str_store_string,s3,"@As a {reg3?girl:boy} growing out of childhood,\
                                  you took to the streets, doing whatever you must to survive.\
                                  Begging, thieving and working for gangs to earn your bread, you lived from day to day in this violent world,\
                                always one step ahead of the law and those who wished you ill."),
                              (else_try),
                                (eq, "$background_answer_2", cb2_steppe_child),
                                (str_store_string,s2,"@a steppe child"),
                                (str_store_string,s3,"@As a {reg3?girl:boy} growing out of childhood,\
                                  you rode the great steppes on a horse of your own, learning the ways of the grass and the desert.\
                                  Although you sometimes went hungry, you became a skillful hunter and pathfinder in your trackless country.\
                                Your body too started to harden with muscle as you grew into the life of a nomad {reg3?woman:man}."),
                              (try_end),
                              (str_store_string,s1,"@{s1}^^ You started to learn about the world almost as soon as you could walk and talk.\
                              You spent your early life as {s2}. {s3}"),
                              
                              ## later
                              (try_begin),
                                (eq, "$background_answer_3", cb3_squire),
                                (str_store_string,s2,"@a squire"),
                                (str_store_string,s3,"@Though the distinction felt sudden to you,\
                                  somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
                                  When you were named squire to a noble at court, you practiced long hours with weapons,\
                                  learning how to deal out hard knocks and how to take them, too.\
                                  You were instructed in your obligations to your lord, and of your duties to those who might one day be your vassals.\
                                  But in addition to learning the chivalric ideal, you also learned about the less uplifting side\
                                  -- old warriors' stories of ruthless power politics, of betrayals and usurpations,\
                                of men who used guile as well as valor to achieve their aims."),
                              (else_try),
                                (eq, "$background_answer_3", cb3_lady_in_waiting),
                                (str_store_string,s2,"@a lady-in-waiting"),
                                (str_store_string,s3,"@Though the distinction felt sudden to you,\
                                  somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
                                  You joined the tightly-knit circle of women at court, ladies who all did proper ladylike things,\
                                  the wives and mistresses of noble men as well as maidens who had yet to find a husband.\
                                  However, even here you found politics at work as the ladies schemed for prominence and fought each other\
                                  bitterly to catch the eye of whatever unmarried man was in fashion at court.\
                                  You soon learned ways of turning these situations and goings-on to your advantage. With it came the\
                                  realisation that you yourself could wield great influence in the world, if only you applied yourself\
                                with a little bit of subtlety."),
                              (else_try),
                                (eq, "$background_answer_3", cb3_troubadour),
                                (str_store_string,s2,"@a troubadour"),
                                (str_store_string,s3,"@Though the distinction felt sudden to you,\
                                  somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
                                  You set out on your own with nothing except the instrument slung over your back and your own voice.\
                                  It was a poor existence, with many a hungry night when people failed to appreciate your play,\
                                  but you managed to survive on your music alone. As the years went by you became adept at playing the\
                                drunken crowds in your taverns, and even better at talking anyone out of anything you wanted."),
                              (else_try),
                                (eq, "$background_answer_3", cb3_student),
                                (str_store_string,s2,"@a university student"),
                                (str_store_string,s3,"@Though the distinction felt sudden to you,\
                                  somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
                                  You found yourself as a student in the university of one of the great cities,\
                                  where you studied theology, philosophy, and medicine.\
                                  But not all your lessons were learned in the lecture halls.\
                                  You may or may not have joined in with your fellows as they roamed the alleys in search of wine, women, and a good fight.\
                                  However, you certainly were able to observe how a broken jaw is set,\
                                or how an angry townsman can be persuaded to set down his club and accept cash compensation for the destruction of his shop."),
                              (else_try),
                                (eq, "$background_answer_3", cb3_peddler),
                                (str_store_string,s2,"@a goods peddler"),
                                (str_store_string,s3,"@Though the distinction felt sudden to you,\
                                  somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
                                  Heeding the call of the open road, you travelled from village to village buying and selling what you could.\
                                  It was not a rich existence, but you became a master at haggling even the most miserly elders into\
                                giving you a good price. Soon, you knew, you would be well-placed to start your own trading empire..."),
                              (else_try),
                                (eq, "$background_answer_3", cb3_craftsman),
                                (str_store_string,s2,"@a smith"),
                                (str_store_string,s3,"@Though the distinction felt sudden to you,\
                                  somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
                                  You pursued a career as a smith, crafting items of function and beauty out of simple metal.\
                                  As time wore on you became a master of your trade, and fine work started to fetch fine prices.\
                                With food in your belly and logs on your fire, you could take pride in your work and your growing reputation."),
                              (else_try),
                                (eq, "$background_answer_3", cb3_poacher),
                                (str_store_string,s2,"@a game poacher"),
                                (str_store_string,s3,"@Though the distinction felt sudden to you,\
                                  somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
                                  Dissatisfied with common men's desperate scrabble for coin, you took to your local lord's own forests\
                                  and decided to help yourself to its bounty, laws be damned. You hunted stags, boars and geese and sold\
                                  the precious meat under the table. You cut down trees right under the watchmen's noses and turned them into\
                                firewood that warmed many freezing homes during winter. All for a few silvers, of course."),
                              (try_end),
                              (str_store_string,s1,"@{s1}^^ Then, as a young adult, life changed as it always does. You became {s2}. {s3}"),
                              
                              ## reason
                              (try_begin),
                                (eq, "$background_answer_4", cb4_revenge),
                                (str_store_string,s2,"@personal revenge"),
                                (str_store_string,s3,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
                                  Still, it was not a difficult choice to leave, with the rage burning brightly in your heart.\
                                  You want vengeance. You want justice. What was done to you cannot be undone,\
                                and these debts can only be paid in blood..."),
                              (else_try),
                                (eq, "$background_answer_4", cb4_loss),
                                (str_store_string,s2,"@the loss of a loved one"),
                                (str_store_string,s3,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
                                  All you can say is that you couldn't bear to stay, not with the memories of those you loved so close and so\
                                  painful. Perhaps your new life will let you forget,\
                                or honour the name that you can no longer bear to speak..."),
                              (else_try),
                                (eq, "$background_answer_4", cb4_wanderlust),
                                (str_store_string,s2,"@wanderlust"),
                                (str_store_string,s3,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
                                  You're not even sure when your home became a prison, when the familiar became mundane, but your dreams of\
                                  wandering have taken over your life. Whether you yearn for some faraway place or merely for the open road and the\
                                freedom to travel, you could no longer bear to stay in the same place. You simply went and never looked back..."),
                              (else_try),
                                (eq, "$background_answer_4", cb4_disown),
                                (str_store_string,s2,"@being forced out of your home"),
                                (str_store_string,s3,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
                                  However, you know you cannot go back. There's nothing to go back to. Whatever home you may have had is gone\
                                now, and you must face the fact that you're out in the wide wide world. Alone to sink or swim..."),
                              (else_try),
                                (eq, "$background_answer_4", cb4_greed),
                                (str_store_string,s2,"@lust for money and power"),
                                (str_store_string,s3,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
                                  To everyone else, it's clear that you're now motivated solely by personal gain.\
                                  You want to be rich, powerful, respected, feared.\
                                  You want to be the one whom others hurry to obey.\
                                  You want people to know your name, and tremble whenever it is spoken.\
                                You want everything, and you won't let anyone stop you from having it..."),
                              (try_end),
                              (str_store_string,s1,"@{s1}^^ But soon everything changed and you decided to strike out on your own as an adventurer.\
                              What made you take this decision was {s2}. {s3}"),
                              
                              ## choose skill
                              (assign, ":difficulty", 0),
                              (try_begin),
                                (eq, "$character_gender", tf_female),
                                (str_store_string, s2, "str_woman"),
                                (val_add, ":difficulty", 1),
                              (else_try),
                                (str_store_string, s2, "str_man"),
                              (try_end),
                              (try_begin),
                                (eq,"$background_type",cb_noble),
                                (str_store_string, s3, "str_noble"),
                                (val_sub, ":difficulty", 1),
                              (else_try),
                                (str_store_string, s3, "str_common"),
                              (try_end),
                              
                              (try_begin),
                                (eq, ":difficulty", -1),
                                (str_store_string, s4, "str_may_find_that_you_are_able_to_take_your_place_among_calradias_great_lords_relatively_quickly"),
                              (else_try),
                                (eq, ":difficulty", 0),
                                (str_store_string, s4, "str_may_face_some_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
                              (else_try),
                                (eq, ":difficulty", 1),
                                (str_store_string, s4, "str_may_face_great_difficulties_establishing_yourself_as_an_equal_among_calradias_great_lords"),
                              (try_end),
                              (str_store_string,s1,"@{s1}^^ As a {s3} {s2}. You {s4}"),
                          ]),
						  
						  #Floris Ship Description and interactive Interface
						#  ("get_ship_background_text",
						#  
						#	(str_clear,s1),
						#	[
						#	(try_begin),
                       #         (eq, slot_ship, 5),
                        #        (str_store_string,s2,"@a travelling merchant"),
                       #         (str_store_string,s3,"@Line2."),
                        #      (else_try),
                        #        (eq, slot_ship, 4),
                        #        (str_store_string,s2,"@a veteran warrior"),
                        #        (str_store_string,s3,"@Line3."),
                        #      (else_try),
                        #        (eq, slot_ship, 3),
                        #        (str_store_string,s2,"@a hunter"),
                        #        (str_store_string,s3,"@Line4."),
                        #      (else_try),
                        #        (eq, slot_ship, 2),
                        #        (str_store_string,s2,"@a steppe nomad"),
                        #        (str_store_string,s3,"@Line5."),
                         #     (else_try),
                         #       (eq, slot_ship, 1),
                        #        (str_store_string,s2,"@a thief"),
                        #        (str_store_string,s3,"@Line6."),
                        #      (try_end),
                        #      (str_store_string,s1,"@ You were born years ago, in a land far away. Your father was {s2}. {s3}"),
						#	]),
                          
                          ("start_adventuring_raise_skills",
                            [
                              (set_show_messages, 0),
                              (try_begin),
                                (eq,"$character_gender",0),		#Male
                                (troop_raise_attribute, "trp_player",ca_strength,1),
                                (troop_raise_attribute, "trp_player",ca_charisma,1),
                              (else_try),						#Female
                                (troop_raise_attribute, "trp_player",ca_agility,1),
                                (troop_raise_attribute, "trp_player",ca_intelligence,1),
                              (try_end),
                              
                              (troop_raise_attribute, "trp_player",ca_strength,1),
                              (troop_raise_attribute, "trp_player",ca_agility,1),
                              (troop_raise_attribute, "trp_player",ca_charisma,1),
                              
                              (troop_raise_skill, "trp_player","skl_leadership",1),
                              (troop_raise_skill, "trp_player","skl_riding",1),
                              
                              (try_begin), #You father was a...
                                (eq,"$background_type",cb_noble),
                                (eq,"$character_gender",tf_male),
                                (troop_raise_attribute, "trp_player",ca_intelligence,1),
                                (troop_raise_attribute, "trp_player",ca_charisma,2),
                                (troop_raise_skill, "trp_player",skl_weapon_master,1),
                                (troop_raise_skill, "trp_player",skl_power_strike,1),
                                (troop_raise_skill, "trp_player",skl_riding,1),
                                (troop_raise_skill, "trp_player",skl_tactics,1),
                                (troop_raise_skill, "trp_player",skl_leadership,1),
                                (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
                                (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
                                (troop_raise_proficiency, "trp_player",wpt_polearm,10),
                                (troop_add_item, "trp_player","itm_sh_khe_rou_old",imod_battered),
                                (troop_add_item, "trp_player","itm_ho_pla_sumpter_white",0),
                                (troop_set_slot, "trp_player", slot_troop_renown, 100),
                                (call_script, "script_change_player_honor", 3),
                                (troop_add_gold, "trp_player", 100),
                              (else_try),
                                (eq,"$background_type",cb_noble),
                                (eq,"$character_gender",tf_female),
                                (troop_raise_attribute, "trp_player",ca_intelligence,2),
                                (troop_raise_attribute, "trp_player",ca_charisma,1),
                                (troop_raise_skill, "trp_player",skl_wound_treatment,1),
                                (troop_raise_skill, "trp_player",skl_riding,2),
                                (troop_raise_skill, "trp_player",skl_first_aid,1),
                                (troop_raise_skill, "trp_player",skl_leadership,1),
                                (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
                                (troop_set_slot, "trp_player", slot_troop_renown, 50),
                                (troop_add_item, "trp_player","itm_sh_khe_rou_old",imod_battered),
                                (troop_add_item, "trp_player","itm_ho_pla_sumpter_white",0),
                                (troop_add_gold, "trp_player", 100),
                              (else_try),
                                (eq,"$background_type",cb_merchant),
                                (troop_raise_attribute, "trp_player",ca_intelligence,2),
                                (troop_raise_attribute, "trp_player",ca_charisma,1),
                                (troop_raise_skill, "trp_player",skl_riding,1),
                                (troop_raise_skill, "trp_player",skl_leadership,1),
                                (troop_raise_skill, "trp_player",skl_trade,2),
                                (troop_raise_skill, "trp_player",skl_inventory_management,1),
                                (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
                                (troop_add_item, "trp_player","itm_ho_nor_mule",imod_swaybacked),
                                (troop_add_gold, "trp_player", 250),
                                (troop_set_slot, "trp_player", slot_troop_renown, 20),
                              (else_try),
                                (eq,"$background_type",cb_guard),
                                (troop_raise_attribute, "trp_player",ca_strength,1),
                                (troop_raise_attribute, "trp_player",ca_agility,1),
                                (troop_raise_attribute, "trp_player",ca_charisma,1),
                                (troop_raise_skill, "trp_player","skl_ironflesh",1),
                                (troop_raise_skill, "trp_player","skl_power_strike",1),
                                (troop_raise_skill, "trp_player","skl_weapon_master",1),
                                (troop_raise_skill, "trp_player","skl_leadership",1),
                                (troop_raise_skill, "trp_player","skl_trainer",1),
                                (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
                                (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,15),
                                (troop_raise_proficiency, "trp_player",wpt_polearm,20),
                                (troop_raise_proficiency, "trp_player",wpt_throwing,10),
                                (troop_add_item, "trp_player","itm_sh_vae_kit_old",imod_battered),
                                (troop_add_item, "trp_player","itm_ho_swa_saddle_black",imod_swaybacked),
                                (troop_add_gold, "trp_player", 50),
                                (troop_set_slot, "trp_player", slot_troop_renown, 10),
                              (else_try),
                                (eq,"$background_type",cb_forester),
                                (troop_raise_attribute, "trp_player",ca_strength,1),
                                (troop_raise_attribute, "trp_player",ca_agility,2),
                                (troop_raise_skill, "trp_player","skl_power_draw",1),
                                (troop_raise_skill, "trp_player","skl_tracking",1),
                                (troop_raise_skill, "trp_player","skl_pathfinding",1),
                                (troop_raise_skill, "trp_player","skl_spotting",1),
                                (troop_raise_skill, "trp_player","skl_athletics",1),
                                (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
                                (troop_raise_proficiency, "trp_player",wpt_archery,30),
                                (troop_add_gold, "trp_player", 30),
                                (troop_add_item, "trp_player","itm_ho_rho_donkey_brown",0),
                              (else_try),
                                (eq,"$background_type",cb_nomad),
                                (eq,"$character_gender",tf_male),
                                (troop_raise_attribute, "trp_player",ca_strength,1),
                                (troop_raise_attribute, "trp_player",ca_agility,1),
                                (troop_raise_attribute, "trp_player",ca_intelligence,1),
                                (troop_raise_skill, "trp_player","skl_power_draw",1),
                                (troop_raise_skill, "trp_player","skl_horse_archery",1),
                                (troop_raise_skill, "trp_player","skl_pathfinding",1),
                                (troop_raise_skill, "trp_player","skl_riding",2),
                                (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
                                (troop_raise_proficiency, "trp_player",wpt_archery,30),
                                (troop_raise_proficiency, "trp_player",wpt_throwing,10),
                                (troop_add_item, "trp_player","itm_sh_khe_rou_old",imod_battered),
                                (troop_add_gold, "trp_player", 15),
                                (troop_add_item, "trp_player","itm_ho_khe_saddle_coloured",imod_heavy),
                                (troop_set_slot, "trp_player", slot_troop_renown, 10),
                              (else_try),
                                (eq,"$background_type",cb_nomad),
                                (eq,"$character_gender",tf_female),
                                (troop_raise_attribute, "trp_player",ca_strength,1),
                                (troop_raise_attribute, "trp_player",ca_agility,1),
                                (troop_raise_attribute, "trp_player",ca_intelligence,1),
                                (troop_raise_skill, "trp_player","skl_wound_treatment",1),
                                (troop_raise_skill, "trp_player","skl_first_aid",1),
                                (troop_raise_skill, "trp_player","skl_pathfinding",1),
                                (troop_raise_skill, "trp_player","skl_riding",2),
                                (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,5),
                                (troop_raise_proficiency, "trp_player",wpt_archery,20),
                                (troop_raise_proficiency, "trp_player",wpt_throwing,5),
                                (troop_add_item, "trp_player","itm_sh_khe_rou_old",imod_battered),
                                (troop_add_gold, "trp_player", 20),
                                (troop_add_item, "trp_player","itm_ho_khe_saddle_coloured",imod_heavy),
                              (else_try),
                                (eq,"$background_type",cb_thief),
                                (troop_raise_attribute, "trp_player",ca_agility,3),
                                (troop_raise_skill, "trp_player","skl_athletics",2),
                                (troop_raise_skill, "trp_player","skl_power_throw",1),
                                (troop_raise_skill, "trp_player","skl_inventory_management",1),
                                (troop_raise_skill, "trp_player","skl_looting",1),
                                (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
                                (troop_raise_proficiency, "trp_player",wpt_throwing,20),
                                (troop_add_item, "trp_player","itm_we_vae_sword_throw_knives",0),
                                (troop_add_gold, "trp_player", 25),
                                (troop_add_item, "trp_player","itm_ho_vae_rus_brown",0),
                              (try_end),
                              
                              (try_begin), #Early life
                                (eq,"$background_answer_2",cb2_page),
                                (troop_raise_attribute, "trp_player",ca_charisma,1),
                                (troop_raise_attribute, "trp_player",ca_strength,1),
                                (troop_raise_skill, "trp_player","skl_power_strike",1),
                                (troop_raise_skill, "trp_player","skl_persuasion",1),
                                (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
                                (troop_raise_proficiency, "trp_player",wpt_polearm,5),
                              (else_try),
                                (eq,"$background_answer_2",cb2_apprentice),
                                (troop_raise_attribute, "trp_player",ca_intelligence,1),
                                (troop_raise_attribute, "trp_player",ca_strength,1),
                                (troop_raise_skill, "trp_player","skl_engineer",1),
                                (troop_raise_skill, "trp_player","skl_trade",1),
                              (else_try),
                                (eq,"$background_answer_2",cb2_urchin),
                                (troop_raise_attribute, "trp_player",ca_agility,1),
                                (troop_raise_attribute, "trp_player",ca_intelligence,1),
                                (troop_raise_skill, "trp_player","skl_spotting",1),
                                (troop_raise_skill, "trp_player","skl_looting",1),
                                (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
                                (troop_raise_proficiency, "trp_player",wpt_throwing,5),
                              (else_try),
                                (eq,"$background_answer_2",cb2_steppe_child),
                                (troop_raise_attribute, "trp_player",ca_strength,1),
                                (troop_raise_attribute, "trp_player",ca_agility,1),
                                (troop_raise_skill, "trp_player","skl_horse_archery",1),
                                (troop_raise_skill, "trp_player","skl_power_throw",1),
                                (troop_raise_proficiency, "trp_player",wpt_archery,15),
                                (call_script,"script_change_troop_renown", "trp_player", 5),
                              (else_try),
                                (eq,"$background_answer_2",cb2_merchants_helper),
                                (troop_raise_attribute, "trp_player",ca_intelligence,1),
                                (troop_raise_attribute, "trp_player",ca_charisma,1),
                                (troop_raise_skill, "trp_player","skl_inventory_management",1),
                                (troop_raise_skill, "trp_player","skl_trade",1),
                              (try_end),
                              
                              (try_begin), #Adulthood
                                (eq,"$background_answer_3",cb3_poacher),
                                (troop_raise_attribute, "trp_player",ca_strength,1),
                                (troop_raise_attribute, "trp_player",ca_agility,1),
                                (troop_raise_skill, "trp_player","skl_power_draw",1),
                                (troop_raise_skill, "trp_player","skl_tracking",1),
                                (troop_raise_skill, "trp_player","skl_spotting",1),
                                (troop_raise_skill, "trp_player","skl_athletics",1),
                                (troop_add_gold, "trp_player", 10),
                                (troop_raise_proficiency, "trp_player",wpt_polearm,10),
                                (troop_raise_proficiency, "trp_player",wpt_archery,35),
                                (troop_add_item, "trp_player","itm_ar_khe_t2_armor_a",0),
                                (troop_add_item, "trp_player","itm_bo_khe_t2_boots",0),
                                (troop_add_item, "trp_player","itm_we_khe_axe_steppe",imod_chipped),
                                (troop_add_item, "trp_player","itm_we_khe_bow_practice",0),
                                (troop_add_item, "trp_player","itm_we_khe_arrow_khergit",0),
                                (troop_add_item, "trp_player","itm_trade_furs",0),
                              (else_try),
                                (eq,"$background_answer_3",cb3_craftsman),
                                (troop_raise_attribute, "trp_player",ca_strength,1),
                                (troop_raise_attribute, "trp_player",ca_intelligence,1),
                                (troop_raise_skill, "trp_player","skl_weapon_master",1),
                                (troop_raise_skill, "trp_player","skl_engineer",1),
                                (troop_raise_skill, "trp_player","skl_tactics",1),
                                (troop_raise_skill, "trp_player","skl_trade",1),
                                (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
                                (troop_add_gold, "trp_player", 100),
                                (troop_add_item, "trp_player","itm_ar_rho_tun_vest",0),
                                (troop_add_item, "trp_player","itm_bo_rho_t1_bear",imod_ragged),
                                (troop_add_item, "trp_player","itm_we_rho_sword_short", imod_balanced),
                                (troop_add_item, "trp_player","itm_we_rho_crossbow_hunting",0),
                                (troop_add_item, "trp_player","itm_we_rho_bolt",0),
                                (troop_add_item, "trp_player","itm_trade_tools",0),
                              (else_try),
                                (eq,"$background_answer_3",cb3_peddler),
                                (troop_raise_attribute, "trp_player",ca_charisma,1),
                                (troop_raise_attribute, "trp_player",ca_intelligence,1),
                                (troop_raise_skill, "trp_player","skl_riding",1),
                                (troop_raise_skill, "trp_player","skl_trade",1),
                                (troop_raise_skill, "trp_player","skl_pathfinding",1),
                                (troop_raise_skill, "trp_player","skl_inventory_management",1),
                                (troop_add_gold, "trp_player", 90),
                                (troop_raise_proficiency, "trp_player",wpt_polearm,15),
                                (troop_add_item, "trp_player","itm_ar_vae_tun_red",0),
                                (troop_add_item, "trp_player","itm_bo_vae_t1_sandal",imod_ragged),                                
                                (troop_add_item, "trp_player","itm_ga_vae_a2_leather",imod_plain),
                                (troop_add_item, "trp_player","itm_he_vae_t1_common_a",0),
                                (troop_add_item, "trp_player","itm_we_vae_spear_scythe",0),
                                (troop_add_item, "trp_player","itm_we_vae_bow_hunting",0),
                                (troop_add_item, "trp_player","itm_we_vae_arrow_sharp",0),
                                (troop_add_item, "trp_player","itm_trade_linen",0),
                                (troop_add_item, "trp_player","itm_trade_pottery",0),
                                (troop_add_item, "trp_player","itm_trade_wool",0),
                              (else_try),
                                (eq,"$background_answer_3",cb3_troubadour),
                                (troop_raise_attribute, "trp_player",ca_charisma,2),
                                (troop_raise_skill, "trp_player","skl_weapon_master",1),
                                (troop_raise_skill, "trp_player","skl_persuasion",1),
                                (troop_raise_skill, "trp_player","skl_leadership",1),
                                (troop_raise_skill, "trp_player","skl_pathfinding",1),
                                (troop_add_gold, "trp_player", 80),
                                (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,25),
                                (troop_raise_proficiency, "trp_player",wpt_crossbow,10),
                                (troop_add_item, "trp_player","itm_ar_nor_tun_blue",imod_sturdy),
                                (troop_add_item, "trp_player","itm_bo_nor_t1_sandal",imod_ragged),
                                (troop_add_item, "trp_player","itm_we_nor_sword_pict", imod_rusty),
                                (troop_add_item, "trp_player","itm_we_nor_bow_hunting", 0),
                                (troop_add_item, "trp_player","itm_we_nor_arrow_bodkin", 0),
                              (else_try),
                                (eq,"$background_answer_3",cb3_squire),
                                (troop_raise_attribute, "trp_player",ca_strength,1),
                                (troop_raise_attribute, "trp_player",ca_agility,1),
                                (troop_raise_skill, "trp_player","skl_riding",1),
                                (troop_raise_skill, "trp_player","skl_weapon_master",1),
                                (troop_raise_skill, "trp_player","skl_power_strike",1),
                                (troop_raise_skill, "trp_player","skl_leadership",1),
                                (troop_add_gold, "trp_player", 20),
                                (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,30),
                                (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,30),
                                (troop_raise_proficiency, "trp_player",wpt_polearm,30),
                                (troop_raise_proficiency, "trp_player",wpt_archery,10),
                                (troop_raise_proficiency, "trp_player",wpt_crossbow,10),
                                (troop_raise_proficiency, "trp_player",wpt_throwing,10),
                                (troop_add_item, "trp_player","itm_ar_swa_t2_gambeson_a",imod_ragged),
                                (troop_add_item, "trp_player","itm_bo_swa_t2_hose",imod_tattered),
                                (troop_add_item, "trp_player","itm_we_swa_sword_senlac", imod_rusty),
                                (troop_add_item, "trp_player","itm_we_swa_bow_practice",0),
                                (troop_add_item, "trp_player","itm_we_swa_arrow_gromite",0),
                              (else_try),
                                (eq,"$background_answer_3",cb3_lady_in_waiting),
                                (eq,"$character_gender",tf_female),
                                (troop_raise_attribute, "trp_player",ca_intelligence,1),
                                (troop_raise_attribute, "trp_player",ca_charisma,1),
                                (troop_raise_skill, "trp_player","skl_persuasion",2),
                                (troop_raise_skill, "trp_player","skl_riding",1),
                                (troop_raise_skill, "trp_player","skl_wound_treatment",1),
                                (troop_add_gold, "trp_player", 100),
                                (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
                                (troop_raise_proficiency, "trp_player",wpt_crossbow,15),
                                (troop_add_item, "trp_player","itm_dress_swadia_common_b",imod_sturdy),
                                (troop_add_item, "trp_player","itm_bo_swa_t1_sandal",0),
                                (troop_add_item, "trp_player","itm_he_swa_lad_common_a",imod_sturdy),
                                (troop_add_item, "trp_player","itm_we_swa_sword_clamshelldagger", 0),
                                (troop_add_item, "trp_player","itm_we_swa_bow_practice",0),
                                (troop_add_item, "trp_player","itm_we_swa_arrow_gromite",0),
                              (else_try),
                                (eq,"$background_answer_3",cb3_student),
                                (troop_raise_attribute, "trp_player",ca_intelligence,2),
                                (troop_raise_skill, "trp_player","skl_weapon_master",1),
                                (troop_raise_skill, "trp_player","skl_surgery",1),
                                (troop_raise_skill, "trp_player","skl_wound_treatment",1),
                                (troop_raise_skill, "trp_player","skl_persuasion",1),
                                (troop_add_gold, "trp_player", 80),
                                (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
                                (troop_raise_proficiency, "trp_player",wpt_crossbow,20),
                                (troop_add_item, "trp_player","itm_ar_sar_tun_robeblack",imod_sturdy),
                                (troop_add_item, "trp_player","itm_bo_sar_t1_sandal",0),
                                (troop_add_item, "trp_player","itm_we_sar_sword_sarranid", imod_rusty),
                                (troop_add_item, "trp_player","itm_we_sar_bow_practice", 0),
                                (troop_add_item, "trp_player","itm_we_sar_arrow_sarranid", 0),
                                (store_random_in_range, ":book_no", books_begin, books_end),
                                (troop_add_item, "trp_player",":book_no",0),
                              (try_end),
                              
                              (try_begin), #Reason for adventuring
                                (eq,"$background_answer_4",cb4_revenge),
                                (troop_raise_attribute, "trp_player",ca_strength,2),
                                (troop_raise_skill, "trp_player","skl_power_strike",1),
                                (troop_add_item, "trp_player","itm_trade_smoked_fish",0),
                              (else_try),
                                (eq,"$background_answer_4",cb4_loss),
                                (troop_raise_attribute, "trp_player",ca_charisma,2),
                                (troop_raise_skill, "trp_player","skl_ironflesh",1),
                                (troop_add_item, "trp_player","itm_trade_dried_meat",0),
                              (else_try),
                                (eq,"$background_answer_4",cb4_wanderlust),
                                (troop_raise_attribute, "trp_player",ca_agility,2),
                                (troop_raise_skill, "trp_player","skl_pathfinding",1),
                                (troop_add_item, "trp_player","itm_trade_bread",0),
                              (else_try),
                                (eq,"$background_answer_4",cb4_disown),
                                (troop_raise_attribute, "trp_player",ca_strength,1),
                                (troop_raise_attribute, "trp_player",ca_intelligence,1),
                                (troop_raise_skill, "trp_player","skl_weapon_master",1),
                                (troop_add_item, "trp_player","itm_trade_apples",0),
                              (else_try),
                                (eq,"$background_answer_4",cb4_greed),
                                (troop_raise_attribute, "trp_player",ca_agility,1),
                                (troop_raise_attribute, "trp_player",ca_intelligence,1),
                                (troop_raise_skill, "trp_player","skl_looting",1),
                                (troop_add_item, "trp_player","itm_trade_sausages",0),
                              (try_end),
                              (set_show_messages, 1),
                          ]),
                          
                          ("cf_agent_check_enemies_nearby",
                            [
                              (store_script_param, ":agent_no", 1),
                              (store_script_param, ":distance", 2),
                              
                              (agent_is_alive, ":agent_no"),
                              (agent_is_human, ":agent_no"),
                              (agent_get_position, pos1, ":agent_no"),
                              (assign, ":result", 0),
                              (set_fixed_point_multiplier, 100),
                              (try_for_agents,":cur_agent"),
                                (neq, ":cur_agent", ":agent_no"),
                                (agent_is_alive, ":cur_agent"),
                                (agent_is_human, ":cur_agent"),
                                (assign, ":continue", 0),
                                (try_begin),
                                  (agent_is_ally, ":agent_no"),
                                  (neg|agent_is_ally, ":cur_agent"),
                                  (assign, ":continue", 1),
                                (else_try),
                                  (neg|agent_is_ally, ":agent_no"),
                                  (agent_is_ally, ":cur_agent"),
                                  (assign, ":continue", 1),
                                (try_end),
                                (eq, ":continue", 1),
                                (agent_get_position, pos2, ":cur_agent"),
                                (get_distance_between_positions, ":cur_distance", pos1, pos2),
                                (le, ":cur_distance", ":distance"),
                                (assign, ":result", 1),
                              (try_end),
                              (eq, ":result", 1),
                          ]),
                          ## CC
                          
                          
                          ##diplomacy begin
                          #recruiter kit begin
                          ("dplmc_send_recruiter",
                            [
                              (store_script_param, ":number_of_recruits", 1),
                              #daedalus begin
                              (store_script_param, ":faction_of_recruits", 2),
                              #daedalus end
                              (assign, ":expenses", ":number_of_recruits"),
                              (val_mul, ":expenses", 20),
                              (val_add, ":expenses", 10),
                              (call_script, "script_dplmc_withdraw_from_treasury", ":expenses"),
                              (set_spawn_radius, 1),
                              (spawn_around_party, "$current_town", "pt_dplmc_recruiter"),
                              (assign,":spawned_party",reg0),
                              (party_set_ai_behavior, ":spawned_party", ai_bhvr_hold),
                              (party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_recruiter),
                              (party_set_slot, ":spawned_party", dplmc_slot_party_recruiter_needed_recruits, ":number_of_recruits"),
                              #daedalus begin
                              (party_set_slot, ":spawned_party", dplmc_slot_party_recruiter_needed_recruits_faction, ":faction_of_recruits"),
                              #daedalus end
                              (party_set_slot, ":spawned_party", dplmc_slot_party_recruiter_origin, "$current_town"),
                              (assign, ":faction", "$players_kingdom"),
                              (party_set_faction, ":spawned_party", ":faction"),
                          ]),
                          #recruiter kit end
                          
						  ("dplmc_describe_prosperity_to_s4",
							[
							  (store_script_param_1, ":center_no"),

							  (str_store_party_name, s60,":center_no"),
							  (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
							  (str_store_string, s4, "str_empty_string"),
							  (try_begin),
								(is_between, ":center_no", towns_begin, towns_end),
								(try_begin),
								  (eq, ":prosperity", 0),
								  (str_store_string, s4, "str_town_prosperity_0"),
								(else_try),
								  (is_between, ":prosperity", 1, 11),
								  (str_store_string, s4, "str_town_prosperity_10"),
								(else_try),
								  (is_between, ":prosperity", 11, 21),
								  (str_store_string, s4, "str_town_prosperity_20"),
								(else_try),
								  (is_between, ":prosperity", 21, 31),
								  (str_store_string, s4, "str_town_prosperity_30"),
								(else_try),
								  (is_between, ":prosperity", 31, 41),
								  (str_store_string, s4, "str_town_prosperity_40"),
								(else_try),
								  (is_between, ":prosperity", 41, 51),
								  (str_store_string, s4, "str_town_prosperity_50"),
								(else_try),
								  (is_between, ":prosperity", 51, 61),
								  (str_store_string, s4, "str_town_prosperity_60"),
								(else_try),
								  (is_between, ":prosperity", 61, 71),
								  (str_store_string, s4, "str_town_prosperity_70"),
								(else_try),
								  (is_between, ":prosperity", 71, 81),
								  (str_store_string, s4, "str_town_prosperity_80"),
								(else_try),
								  (is_between, ":prosperity", 81, 91),
								  (str_store_string, s4, "str_town_prosperity_90"),
								(else_try),
								  (is_between, ":prosperity", 91, 101),
								  (str_store_string, s4, "str_town_prosperity_100"),
								(try_end),
							  (else_try),
								(is_between, ":center_no", villages_begin, villages_end),
								(try_begin),
								  (eq, ":prosperity", 0),
								  (str_store_string, s4, "str_village_prosperity_0"),
								(else_try),
								  (is_between, ":prosperity", 1, 11),
								  (str_store_string, s4, "str_village_prosperity_10"),
								(else_try),
								  (is_between, ":prosperity", 11, 21),
								  (str_store_string, s4, "str_village_prosperity_20"),
								(else_try),
								  (is_between, ":prosperity", 21, 31),
								  (str_store_string, s4, "str_village_prosperity_30"),
								(else_try),
								  (is_between, ":prosperity", 31, 41),
								  (str_store_string, s4, "str_village_prosperity_40"),
								(else_try),
								  (is_between, ":prosperity", 41, 51),
								  (str_store_string, s4, "str_village_prosperity_50"),
								(else_try),
								  (is_between, ":prosperity", 51, 61),
								  (str_store_string, s4, "str_village_prosperity_60"),
								(else_try),
								  (is_between, ":prosperity", 61, 71),
								  (str_store_string, s4, "str_village_prosperity_70"),
								(else_try),
								  (is_between, ":prosperity", 71, 81),
								  (str_store_string, s4, "str_village_prosperity_80"),
								(else_try),
								  (is_between, ":prosperity", 81, 91),
								  (str_store_string, s4, "str_village_prosperity_90"),
								(else_try),
								  (is_between, ":prosperity", 91, 101),
								  (str_store_string, s4, "str_village_prosperity_100"),
								(try_end),
							  (try_end),
								]),
                          
							  ("dplmc_pay_into_treasury",
								[
								  (store_script_param_1, ":amount"),
								  (troop_add_gold, "trp_household_possessions", ":amount"),
								  (assign, reg0, ":amount"),
								  (play_sound, "snd_money_received"),
								  (display_message, "@{reg0} denars added to treasury."),
							  ]),

							  ("dplmc_withdraw_from_treasury",
								[
								  (store_script_param_1, ":amount"),
								  (troop_remove_gold, "trp_household_possessions", ":amount"),
								  (assign, reg0, ":amount"),
								  (play_sound, "snd_money_paid"),
								  (display_message, "@{reg0} denars removed from treasury."),
							  ]),

							  ("dplmc_describe_tax_rate_to_s50",
								[
								  (store_script_param_1, ":tax_rate"),
								  (val_div, ":tax_rate", 25),
								  (store_add, ":str_id","str_dplmc_tax_normal", ":tax_rate"),
								  (str_store_string, s50, ":str_id"),
							  ]),


							  ("dplmc_player_troops_leave",
							   [
								(store_script_param_1, ":percent"),

								(try_begin),#debug
								 (eq, "$cheat_mode", 1),
								 (assign, reg0, ":percent"),
								 (display_message, "@{!}DEBUG : removing player troops: {reg0}%"),
								(try_end),

								(assign, ":deserters", 0),
								(try_for_parties, ":party_no"),
								  (assign, ":remove_troops", 0),
								  (try_begin),
									(this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_town),
									(party_slot_eq, ":party_no", slot_party_type, spt_castle),
									(party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
									(assign, ":remove_troops", 1),
								  (else_try),
									 (eq, "p_main_party", ":party_no"),
									 (assign, ":remove_troops", 1),
								  (try_end),

								  (eq, ":remove_troops", 1),
								  (party_get_num_companion_stacks, ":num_stacks",":party_no"),
								  (try_for_range, ":i_stack", 0, ":num_stacks"),
									(party_stack_get_size, ":stack_size",":party_no",":i_stack"),
									(val_mul, ":stack_size", ":percent"),
									(val_div, ":stack_size", 100),
									(party_stack_get_troop_id, ":troop_id", ":party_no", ":i_stack"),
									(party_remove_members, ":party_no", ":troop_id", ":stack_size"),
									(val_add, ":deserters", ":stack_size"),
								  (try_end),
								(try_end),
								(assign, reg0, ":deserters"),
							   ]
							  ),
                          
							  ("dplmc_get_item_buy_price_factor",
								[
								##nested diplomacy start+
								#(store_script_param_1, ":item_kind_id"),
								#(store_script_param_2, ":center_no"),
								#Add two parameters
								(store_script_param, ":item_kind_id", 1),
								(store_script_param, ":center_no", 2),
								(store_script_param, ":customer_no", 3),
								(store_script_param, ":merchant_no", 4),
								##nested diplomacy start+
								(assign, ":price_factor", 100),

								##nested diplomacy start+
								#(call_script, "script_get_trade_penalty", ":item_kind_id"),
								(call_script, "script_dplmc_get_trade_penalty", ":item_kind_id", ":center_no", ":customer_no", ":merchant_no"),
								##nested diplomacy end+
								(assign, ":trade_penalty", reg0),

								(try_begin),
								  ##nested diplomacy start+
								  (gt, ":center_no", 0),
								  (this_or_next|is_between, ":center_no", centers_begin, centers_end),
									(party_is_active, ":center_no"),
								  
								  (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
								  (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_village),
								  ##nested diplomacy end+
								  (is_between, ":center_no", centers_begin, centers_end),
								  (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
								  (store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
								  (val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
								  (party_get_slot, ":price_factor", ":center_no", ":item_slot_no"),

								  (try_begin),
									##nested diplomacy start+
									#OLD:
									#(is_between, ":center_no", villages_begin, villages_end),
									#(party_get_slot, ":market_town", ":center_no", slot_village_market_town),
									##NEW:
									(gt, ":center_no", 0),
									(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_village),
										(is_between, ":center_no", villages_begin, villages_end),
									(party_get_slot, ":market_town", ":center_no", slot_village_market_town),
									
									(ge, ":market_town", centers_begin),
									(this_or_next|party_slot_eq, ":market_town", slot_party_type, spt_town),
									(this_or_next|party_slot_eq, ":market_town", slot_party_type, spt_village),
										(is_between, ":market_town", centers_begin, centers_end),
									##nested diplomacy end+
									(party_get_slot, ":price_in_market_town", ":market_town", ":item_slot_no"),
									(val_max, ":price_factor", ":price_in_market_town"),
								  (try_end),
								  ##nested diplomacy start+
								  #Enforce constraints
								  (val_clamp, ":price_factor", minimum_price_factor, maximum_price_factor + 1),
								  ##nested diplomacy end+

								  #For villages, the good will be sold no cheaper than in the market town
								  #This represents the absence of a permanent market -- ie, the peasants retain goods to sell on their journeys to town, and are not about to do giveaway deals with passing adventurers

								  (val_mul, ":price_factor", 100), #normalize price factor to range 0..100
								  (val_div, ":price_factor", average_price_factor),
								(try_end),

								(store_add, ":penalty_factor", 100, ":trade_penalty"),

								(val_mul, ":price_factor", ":penalty_factor"),
								(val_div, ":price_factor", 100),

								(assign, reg0, ":price_factor"),
								(set_trigger_result, reg0),
							  ]),
                          
							  ("dplmc_party_calculate_strength",
								[
								  (store_script_param_1, ":party"), #Party_id
								  (store_script_param_2, ":exclude_leader"), #Party_id

								  (assign, reg0,0),
								  (party_get_num_companion_stacks, ":num_stacks", ":party"),
								  (assign, ":first_stack", 0),
								  (try_begin),
									(neq, ":exclude_leader", 0),
									(assign, ":first_stack", 1),
								  (try_end),

								  (assign, ":sum", 0),
								  (try_for_range, ":i_stack", ":first_stack", ":num_stacks"),
									(party_stack_get_troop_id, ":stack_troop",":party", ":i_stack"),

									(try_begin),
									  (neg|troop_is_hero, ":stack_troop"),
									  (party_stack_get_size, ":stack_size",":party",":i_stack"),
									(try_end),
									(val_add, ":sum", ":stack_size"),
								  (try_end),
								  (assign, reg0, ":sum"),

								  (try_begin), #debug
									(eq, "$cheat_mode", 1),
									(display_message, "@{!}DEBUG : sum: {reg0}"),
								  (try_end),
							  ]),
                          
							#script_dplmc_start_alliance_between_kingdoms, 20 days alliance, 40 days truce after that
							  # Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
							  # Output: none
							  ("dplmc_start_alliance_between_kingdoms", #sets relations between two kingdoms
								[
								  (store_script_param, ":kingdom_a", 1),
								  (store_script_param, ":kingdom_b", 2),
								  (store_script_param, ":initializing_war_peace_cond", 3),
								  ##diplomacy start+
								  #Since "fac_player_supporters_faction" is used as a shorthand for the faction
								  #run by the player, intercept that here instead of the various places this is
								  #called from.
								  (assign, ":save_reg1", reg1),
								  (call_script, "script_dplmc_translate_inactive_player_supporter_faction_2", ":kingdom_a", ":kingdom_b"),
								  (assign, ":kingdom_a", reg0),
								  (assign, ":kingdom_b", reg1),
								  (assign, reg1, ":save_reg1"),
								  ##diplomacy end+

								  (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
								  (val_add, ":relation", 15),
								  (val_max, ":relation", 40),
								  (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
								  (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

								  (try_begin),
									(eq, "$players_kingdom", ":kingdom_a"),
									(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
									(val_add, ":relation", 15),
									(val_max, ":relation", 40),
									(call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
									#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
								  (else_try),
									(eq, "$players_kingdom", ":kingdom_b"),
									(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
									(val_add, ":relation", 15),
									(val_max, ":relation", 40),
									(call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
									#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
								  (try_end),

								  (try_begin),
									(eq, ":initializing_war_peace_cond", 1),
									(str_store_faction_name_link, s1, ":kingdom_a"),
									(str_store_faction_name_link, s2, ":kingdom_b"),
									##diplomacy start+ #Due to complaints about the wording
									#(display_log_message, "@{s1} and {s2} have concluded an alliance with each other."),
									(display_log_message, "@{s1} and {s2} have entered into an alliance with each other."),
									##diplomacy end+

									(call_script, "script_add_notification_menu", "mnu_dplmc_notification_alliance_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu

									(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
									(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
									(assign, "$g_recalculate_ais", 1),


								  (try_end),

								  (try_begin), #add truce
									(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
									(val_sub, ":truce_slot", kingdoms_begin),
									##nested diplomacy start+ replace 80 with a named constant
									#(faction_set_slot, ":kingdom_b", ":truce_slot", 80),
									(faction_set_slot, ":kingdom_b", ":truce_slot", dplmc_treaty_alliance_days_initial),
									##nested diplomacy end+

									(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
									(val_sub, ":truce_slot", kingdoms_begin),
									##nested diplomacy start+ replace 80 with a named constant
									#(faction_set_slot, ":kingdom_a", ":truce_slot", 80),
									(faction_set_slot, ":kingdom_a", ":truce_slot", dplmc_treaty_alliance_days_initial),
									##nested diplomacy end+

									(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
									(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
									(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
									(try_begin),
										(lt, ":damage_inflicted_by_a", 100),
										#controversial policy
									(try_end),
									(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),

									(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
									(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
									(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
									(try_begin),
										(lt, ":damage_inflicted_by_b", 100),
										#controversial policy
									(try_end),
									(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),

								  (try_end),
                              
								 # share wars
								(try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
								  (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
								  (neq, ":kingdom_a", ":faction_no"),
								  (neq, ":kingdom_b", ":faction_no"),
								  (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_a", ":faction_no"),
								  #result: -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
								  (eq, reg0, -2),
								  (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_b", ":faction_no"),
								  (ge, reg0, -1),
								  (call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_b", ":faction_no", 2),
								(try_end),
								(try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
								  (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
								  (neq, ":kingdom_a", ":faction_no"),
								  (neq, ":kingdom_b", ":faction_no"),
								  (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_b", ":faction_no"),
								  #result: -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
								  (eq, reg0, -2),
								  (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_a", ":faction_no"),
								  (ge, reg0, -1),
								  (call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_a", ":faction_no", 2),
								(try_end),
							  ]),
                          
							 #script_dplmc_start_defensive_between_kingdoms, 20 days defensive: 20 days trade aggreement, 20 days non-aggression after that
							  # Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
							  # Output: none
							  ("dplmc_start_defensive_between_kingdoms", #sets relations between two kingdoms
								[
								  (store_script_param, ":kingdom_a", 1),
								  (store_script_param, ":kingdom_b", 2),
								  (store_script_param, ":initializing_war_peace_cond", 3),
								  ##diplomacy start+
								  #Since "fac_player_supporters_faction" is used as a shorthand for the faction
								  #run by the player, intercept that here instead of the various places this is
								  #called from.
								  (assign, ":save_reg1", reg1),
								  (call_script, "script_dplmc_translate_inactive_player_supporter_faction_2", ":kingdom_a", ":kingdom_b"),
								  (assign, ":kingdom_a", reg0),
								  (assign, ":kingdom_b", reg1),
								  (assign, reg1, ":save_reg1"),
								  ##diplomacy end+

								  (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
								  (val_add, ":relation", 10),
								  (val_max, ":relation", 30),
								  (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
								  (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

								  (try_begin),
									(eq, "$players_kingdom", ":kingdom_a"),
									(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
									(val_add, ":relation", 10),
									(val_max, ":relation", 30),
									(call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
									#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
								  (else_try),
									(eq, "$players_kingdom", ":kingdom_b"),
									(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
									(val_add, ":relation", 10),
									(val_max, ":relation", 30),
									(call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
									#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
								  (try_end),

								  (try_begin),
									(eq, ":initializing_war_peace_cond", 1),
									(str_store_faction_name_link, s1, ":kingdom_a"),
									(str_store_faction_name_link, s2, ":kingdom_b"),
									(display_log_message, "@{s1} and {s2} have concluded a defensive pact with each other."),

									(call_script, "script_add_notification_menu", "mnu_dplmc_notification_defensive_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu

									(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
									(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
									(assign, "$g_recalculate_ais", 1),


								  (try_end),

								  (try_begin), #add truce
									(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
									(val_sub, ":truce_slot", kingdoms_begin),
									##diplomacy start+ replace 60 with named variable
									#(faction_set_slot, ":kingdom_b", ":truce_slot", 60),
									(faction_set_slot, ":kingdom_b", ":truce_slot", dplmc_treaty_defense_days_initial),
									##diplomacy end+

									(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
									(val_sub, ":truce_slot", kingdoms_begin),
									##diplomacy start+ replace 60 with named variable
									#(faction_set_slot, ":kingdom_a", ":truce_slot", 60),
									(faction_set_slot, ":kingdom_a", ":truce_slot", dplmc_treaty_defense_days_initial),
									##diplomacy end+

									(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
									(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
									(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
									(try_begin),
										(lt, ":damage_inflicted_by_a", 100),
										#controversial policy
									(try_end),
									(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),

									(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
									(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
									(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
									(try_begin),
										(lt, ":damage_inflicted_by_b", 100),
										#controversial policy
									(try_end),
									(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),

								  (try_end),
							  ]),
                          
							#script_dplmc_start_trade_between_kingdoms, 20 days trade aggreement, 20 days non-aggression after that
							  # Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
							  # Output: none
							  ("dplmc_start_trade_between_kingdoms", #sets relations between two kingdoms
								[
								  (store_script_param, ":kingdom_a", 1),
								  (store_script_param, ":kingdom_b", 2),
								  (store_script_param, ":initializing_war_peace_cond", 3),
								  ##diplomacy start+
								  #Since "fac_player_supporters_faction" is used as a shorthand for the faction
								  #run by the player, intercept that here instead of the various places this is
								  #called from.
								  (assign, ":save_reg1", reg1),
								  (call_script, "script_dplmc_translate_inactive_player_supporter_faction_2", ":kingdom_a", ":kingdom_b"),
								  (assign, ":kingdom_a", reg0),
								  (assign, ":kingdom_b", reg1),
								  (assign, reg1, ":save_reg1"),
								  ##diplomacy end+

								  (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
								  (val_add, ":relation", 5),
								  (val_max, ":relation", 20),
								  (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
								  (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

								  (try_begin),
									(eq, "$players_kingdom", ":kingdom_a"),
									(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
									(val_add, ":relation", 5),
									(val_max, ":relation", 20),
									(call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
									#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
								  (else_try),
									(eq, "$players_kingdom", ":kingdom_b"),
									(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
									(val_add, ":relation", 5),
									(val_max, ":relation", 20),
									(call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
									#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
								  (try_end),

								  (try_begin),
									(eq, ":initializing_war_peace_cond", 1),
									(str_store_faction_name_link, s1, ":kingdom_a"),
									(str_store_faction_name_link, s2, ":kingdom_b"),
									(display_log_message, "@{s1} and {s2} have concluded a trade agreement with each other."),

									(call_script, "script_add_notification_menu", "mnu_dplmc_notification_trade_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu

									(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
									(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
									(assign, "$g_recalculate_ais", 1),


								  (try_end),

								  (try_begin), #add truce
									(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
									(val_sub, ":truce_slot", kingdoms_begin),
									##nested diplomacy start+ replace hardcoded number of days with a variable
									#(faction_set_slot, ":kingdom_b", ":truce_slot", 40),
									(faction_set_slot, ":kingdom_b", ":truce_slot", dplmc_treaty_trade_days_initial),
									##nested diplomacy end+

									(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
									(val_sub, ":truce_slot", kingdoms_begin),
									##nested diplomacy start+ replace hardcoded number of days with a variable
									#(faction_set_slot, ":kingdom_a", ":truce_slot", 40),
									(faction_set_slot, ":kingdom_a", ":truce_slot", dplmc_treaty_trade_days_initial),
									##nested diplomacy end+

									(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
									(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
									(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
									(try_begin),
										(lt, ":damage_inflicted_by_a", 100),
										#controversial policy
									(try_end),
									(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),

									(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
									(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
									(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
									(try_begin),
										(lt, ":damage_inflicted_by_b", 100),
										#controversial policy
									(try_end),
									(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),

								  (try_end),
							  ]),
                          
							#script_dplmc_start_nonaggression_between_kingdoms, 20 days non-aggression
							  # Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
							  # Output: none
							  ("dplmc_start_nonaggression_between_kingdoms", #sets relations between two kingdoms
								[
								  (store_script_param, ":kingdom_a", 1),
								  (store_script_param, ":kingdom_b", 2),
								  (store_script_param, ":initializing_war_peace_cond", 3),
								  ##diplomacy start+
								  #Since "fac_player_supporters_faction" is used as a shorthand for the faction
								  #run by the player, intercept that here instead of the various places this is
								  #called from.
								  (assign, ":save_reg1", reg1),
								  (call_script, "script_dplmc_translate_inactive_player_supporter_faction_2", ":kingdom_a", ":kingdom_b"),
								  (assign, ":kingdom_a", reg0),
								  (assign, ":kingdom_b", reg1),
								  (assign, reg1, ":save_reg1"),
								  ##diplomacy end+

								  (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
								  (val_add, ":relation", 3),
								  (val_max, ":relation", 10),
								  (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
								  (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

								  (try_begin),
									(eq, "$players_kingdom", ":kingdom_a"),
									(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
									(val_add, ":relation", 3),
									(val_max, ":relation", 10),
									(call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
									#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
								  (else_try),
									(eq, "$players_kingdom", ":kingdom_b"),
									(store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
									(val_add, ":relation", 3),
									(val_max, ":relation", 10),
									(call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
									#(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
								  (try_end),

								  (try_begin),
									(eq, ":initializing_war_peace_cond", 1),
									(str_store_faction_name_link, s1, ":kingdom_a"),
									(str_store_faction_name_link, s2, ":kingdom_b"),
									(display_log_message, "@{s1} and {s2} have concluded a non aggression pact with each other."),

									(call_script, "script_add_notification_menu", "mnu_dplmc_notification_nonaggression_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu

									(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
									(call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
									(assign, "$g_recalculate_ais", 1),


								  (try_end),

								  (try_begin), #add truce
									(store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
									(val_sub, ":truce_slot", kingdoms_begin),
									##nested diplomacy start+ replace hardcoded number with a variable
									#(faction_set_slot, ":kingdom_b", ":truce_slot", 20),
									(faction_set_slot, ":kingdom_b", ":truce_slot", dplmc_treaty_truce_days_initial),
									##nested diplomacy end+

									(store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
									(val_sub, ":truce_slot", kingdoms_begin),
									##nested diplomacy start+ replace hardcoded number with a variable
									#(faction_set_slot, ":kingdom_a", ":truce_slot", 20),
									(faction_set_slot, ":kingdom_a", ":truce_slot", dplmc_treaty_truce_days_initial),
									##nested diplomacy end+

									(store_add, ":slot_war_damage_inflicted_on_b", ":kingdom_b", slot_faction_war_damage_inflicted_on_factions_begin),
									(val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
									(faction_get_slot, ":damage_inflicted_by_a", ":kingdom_a", ":slot_war_damage_inflicted_on_b"),
									(try_begin),
										(lt, ":damage_inflicted_by_a", 100),
										#controversial policy
									(try_end),
									(faction_set_slot, ":kingdom_a", ":slot_war_damage_inflicted_on_b", 0),

									(store_add, ":slot_war_damage_inflicted_on_a", ":kingdom_a", slot_faction_war_damage_inflicted_on_factions_begin),
									(val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
									(faction_get_slot, ":damage_inflicted_by_b", ":kingdom_b", ":slot_war_damage_inflicted_on_a"),
									(try_begin),
										(lt, ":damage_inflicted_by_b", 100),
										#controversial policy
									(try_end),
									(faction_set_slot, ":kingdom_b", ":slot_war_damage_inflicted_on_a", 0),

								  (try_end),
							  ]),
                          
                          
                          
                          # Input: arg1 = faction_no_1, arg2 = faction_no_2
						  ("dplmc_get_prisoners_value_between_factions",
						   [
							   (store_script_param, ":faction_no_1", 1),
							   (store_script_param, ":faction_no_2", 2),

							   (assign, ":faction_no_1_value", 0),
							   (assign, ":faction_no_2_value", 0),

							   (try_for_parties, ":party_no"),
								 (store_faction_of_party, ":party_faction", ":party_no"),
								 (try_begin),
								   (eq, ":party_faction", ":faction_no_1"),
								   (party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
								   (try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
									 (party_prisoner_stack_get_troop_id, ":cur_troop_id", ":party_no", ":troop_iterator"),
									 (store_troop_faction, ":cur_faction", ":cur_troop_id"),

									 (eq, ":cur_faction", ":faction_no_2"),
									 (try_begin),
									   (troop_is_hero, ":cur_troop_id"),
									   (call_script, "script_calculate_ransom_amount_for_troop", ":cur_troop_id"),
									   (val_add, ":faction_no_1_value", reg0),

									   (try_begin),#debug
										 (eq, "$cheat_mode", 1),
										 (assign, reg0, ":faction_no_1_value"),
										 (display_message, "@{!}DEBUG : faction_no_1_value: {reg0}"),
									   (try_end),

									 (try_end),
								   (try_end),
								 (else_try),
								   (eq, ":party_faction", ":faction_no_2"),
								   (party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
								   (try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
									 (party_prisoner_stack_get_troop_id, ":cur_troop_id", ":party_no", ":troop_iterator"),
									 (store_troop_faction, ":cur_faction", ":cur_troop_id"),

									 (eq, ":cur_faction", ":faction_no_1"),
									 (try_begin),
									   (troop_is_hero, ":cur_troop_id"),
									   (call_script, "script_calculate_ransom_amount_for_troop", ":cur_troop_id"),
									   (val_add, ":faction_no_2_value", reg0),

									   (try_begin), #debug
										 (eq, "$cheat_mode", 1),
										 (assign, reg0, ":faction_no_2_value"),
										 (display_message, "@{!}DEBUG : faction_no_2_value: {reg0}"),
									   (try_end),

									 (try_end),
								   (try_end),
								 (try_end),
							   (try_end),
							   (store_sub, reg0, ":faction_no_1_value", ":faction_no_2_value"),
							]),
                          
							# Input: arg1 = faction_no_1, arg2 = faction_no_2
							  ("dplmc_get_truce_pay_amount",
							   [
								   (store_script_param, ":faction_no_1", 1),
								   (store_script_param, ":faction_no_2", 2),
								   (store_script_param, ":check_peace_war_result", 3),
								   ##diplomacy start+
								   #Since "fac_player_supporters_faction" is used as a shorthand for the faction
								   #run by the player, intercept that here instead of the various places this is
								   #called from.
								   (call_script, "script_dplmc_translate_inactive_player_supporter_faction_2", ":faction_no_1", ":faction_no_2"),
								   (assign, ":faction_no_1", reg0),
								   (assign, ":faction_no_2", reg1),
								   ##diplomacy end+

								   (try_begin),
									 (eq, "$cheat_mode", 1),
									 (assign, reg0, ":check_peace_war_result"), #debug
									 (display_message, "@{!}DEBUG : peace_war_result: {reg0}"),#debug
								   (try_end),
								   
								   ##nested diplomacy start+
								   #Improve this script; costs were too low befow.
								   #faction_no_1 is player faction asking for peace
								   #faction_no_2 is NPC faction that already considered peace and considers
								   #      it a bad idea, so the price should not be nominal.

								   #(Also, a sign error meant that the amount asked was almost always
								   #zero.)

								   #Because the PC wants peace and the NPC doesn't, we aren't going to
								   #bother calculating relative strength or the like.  Instead, we are
								   #going to assume the NPC can achieve his strategic objectives if he
								   #does not make peace, and set the price accordingly.

								   #Add a generic cost for check_peace_war_result
								   #These are the same as in Wahiti's original script.
								   (assign, ":base_cost",  4000),
								   (try_begin),
									  #It's dubious that this is ever currently called if the check-peace-war
									  #result was >= 0, but include this for completeness.
									  (ge, ":check_peace_war_result", 0),
									  (assign, ":base_cost", 4000),
								   (else_try),
									  (ge, ":check_peace_war_result", -1),
									  (assign, ":base_cost", 8000),
								   (else_try),
									  (ge, ":check_peace_war_result", -2),
									  (assign, ":base_cost", 12000),
								   (else_try),
									  #It shouldn't be used with this parameter; this is for the
									  #sake of completeness.
									  (le, ":check_peace_war_result", -3),
									  (store_mul, ":base_cost", -6000, ":check_peace_war_result"),
								   (try_end),
										
								   #Get reparations for held centers.  A truce lasts 20 days, so the
								   #value "lost" in rents and tarriffs by declaring peace now cannot be
								   #is not greater than 3 times the weekly average (that upper bound is
								   #if the NPC is in a position to immediately recapture all of them).
								   
								   #If the NPC kingdom is currently attacking a specific village or walled
								   #center, even if it isn't an ex-possession it effectively becomes one.
								   #(Also, assign it or its center as a demanded fief if there wasn't one
								   #already.)
							   (assign, ":target_fief", -1),
							   (try_begin),
								  (lt, ":check_peace_war_result", 1),#This should always be true anyway, but still.
								  (this_or_next|faction_slot_eq, ":faction_no_2", slot_faction_ai_state, sfai_attacking_center),
								  (faction_slot_eq, ":faction_no_2", slot_faction_ai_state, sfai_raiding_village),
								  (faction_get_slot, reg0, ":faction_no_2", slot_faction_ai_object),
								  (is_between, reg0, centers_begin, centers_end),
								  (assign, ":target_fief", reg0),
							   (try_end),

							   (assign, ":center_cost", 0),
							   (assign, ":concession_value", 0),
							   #This this old are newer are considered "recently conquered", meaning that
							   #faction_no_2 thinks there's a good chance they could reclaim them if the
							   #fighting continued.
							   (store_current_hours, ":recently_conquered"),
							   (try_begin),
								  (ge, ":check_peace_war_result", 1),#ordinarily this should not be true
								  (val_sub, ":recently_conquered", 24 * 2),#only the last two days
							   (else_try),
								  (eq, ":check_peace_war_result", 0),
								  (val_sub, ":recently_conquered", 24 * 15),#last 15 days
							   (else_try),
								  (eq, ":check_peace_war_result", -1),
								  (val_sub, ":recently_conquered", 24 * 20),#last 20 days
							   (else_try),
								  (eq, ":check_peace_war_result", -2),
								  (val_sub, ":recently_conquered", 24 * 30),#last 30 days
							   (else_try),
								  (val_sub, ":recently_conquered", 24 * 60),#last 60 days
							   (try_end),

							   (try_for_range, ":party_no", centers_begin, centers_end),
								  (store_faction_of_party, ":party_current_faction", ":party_no"),
								  (eq, ":party_current_faction", ":faction_no_1"),

								  #party_value is the estimated weekly income of the fief,
								  #applied three times and time discounted
								  (call_script, "script_dplmc_estimate_center_weekly_income", ":party_no"),
								  (store_mul, ":party_value", reg0, 3),

								  (try_begin),
									 (ge, "$g_concession_demanded", spawn_points_begin),
									 (this_or_next|eq, "$g_concession_demanded", ":party_no"),
									 (party_slot_eq, ":party_no", slot_village_bound_center, "$g_concession_demanded"),
									 (val_add, ":concession_value", ":party_value"),
								  (try_end),

								  (assign, ":continue", 0),

								  (try_begin),
									 #A former possession of faction 2 (must have recently changed hands, or
									 #faction 2 must be enthusiastic about the war)
									 (party_slot_eq, ":party_no", slot_center_original_faction, ":faction_no_2"),
									 (party_slot_ge, ":party_no", dplmc_slot_center_last_transfer_time, ":recently_conquered"),
									 (assign, ":continue", 1),
								  (else_try),
									 #A former possession of faction 2 (must have recently changed hands, or
									 #faction 2 must be enthusiastic about the war)
									 (party_slot_eq, ":party_no", slot_center_ex_faction, ":faction_no_2"),
									 (party_slot_ge, ":party_no", dplmc_slot_center_last_transfer_time, ":recently_conquered"),
									 (assign, ":continue", 1),
								  (else_try),
									 #The center is being attacked by faction 2, or is a village whose castle
									 #or town is being attacked by faction 2.
									 (ge, ":target_fief", centers_begin),
									 (this_or_next|eq, ":party_no", ":target_fief"),
									 (party_slot_eq, ":party_no", slot_village_bound_center, ":target_fief"),
									 (assign, ":continue", 1),
								  (else_try),
									 #The center is under siege by faction 2.
									 (party_get_slot, reg0, ":party_no", slot_center_is_besieged_by),
									 (gt, reg0, 0),
									 (party_is_active, reg0),
									 (store_faction_of_party, reg0, reg0),
									 (eq, reg0, ":faction_no_2"),
									 (assign, ":continue", 1),
								  (else_try),
									 #The center is a village, and the castle or town it is bound to
									 #is under siege by faction 2.
									 (is_between, ":party_no", villages_begin, villages_end),
									 (party_get_slot, reg0, ":party_no", slot_village_bound_center),
									 (is_between, reg0, centers_begin, centers_end),
									 (party_get_slot, reg0, reg0, slot_center_is_besieged_by),
									 (gt, reg0, -1),
									 (party_is_active, reg0),
									 (store_faction_of_party, reg0, reg0),
									 (eq, reg0, ":faction_no_2"),
									 (assign, ":continue", 1),
								  (try_end),

								  (gt, ":continue", 0),

								  (val_add, ":center_cost", ":party_value"),
							   (try_end),
								   
								   #If no held centers were found, assume the campaign objective is to
								   #conquer territory rather than recover lost territory, if the
								   #NPC is sufficiently enthusiastic about the war.
								   (try_begin),
									  #Equivalent of a castle and a village
									  (eq, ":check_peace_war_result", -1),
									  (val_max, ":center_cost", (1500 + 750) * 3),
								   (else_try),
									  #Equivalent of two castles with two villages
									  (le, ":check_peace_war_result", -2),
									  (val_max, ":center_cost", (1500 + 750) * 3 * 2),
								   (try_end),
								   
								   #If the war started very recently, or a center changed hands very recently,
								   #increase the cost.  The reasoning behind this is to make the AI less prone
								   #to whipsawing.
								   #
								   #The multiplier is 2x for the first 48 hours, then decreases linearly from
								   #the two-day mark until it reaches zero at the 8-day mark.
								   #
								   #As an example, here is how a cost of 10,000 would scale over this time:
								   # 1 day  - 20000
								   # 2 days - 20000
								   # 3 days - 18333
								   # 4 days - 16667
								   # 5 days - 15000
								   # 6 days - 13333
								   # 7 days - 11667
								   # 8 days - 10000
								   # 9 days - 10000
								   (store_current_hours, ":cur_hours"),
								   (faction_get_slot, ":faction_ai_last_decisive_event", ":faction_no_2", slot_faction_ai_last_decisive_event),
								   (store_sub, ":hours_since_last_decisive_event", ":cur_hours", ":faction_ai_last_decisive_event"),
								   (val_max, ":hours_since_last_decisive_event", 0),
								   (try_begin),
									  #First 48 hours, the base & center costs are doubled.
									  (lt, ":hours_since_last_decisive_event", 48 + 1),
									  (val_mul, ":base_cost", 2),
									  (val_mul, ":center_cost", 2),
								   (else_try),
									  #From 2 days to 8 days, the cost multiplier goes from 2 to 1
									  (lt, ":hours_since_last_decisive_event", 24 * 8),
									  (store_sub, reg0, 24 * 2, ":hours_since_last_decisive_event"),#0 to 6 days
									  (store_sub, ":multiplier", 24 * 12, reg0),# 6 to 12 days
									  
									  (val_mul, ":base_cost", ":multiplier"),
									  (val_add, ":base_cost", (24 * 6) // 2),
									  (val_div, ":base_cost", 24 * 6),
									  
									  (val_mul, ":center_cost", ":multiplier"),
									  (val_add, ":center_cost", (24 * 6) // 2),
									  (val_div, ":center_cost", 24 * 6),
								   (try_end),
								   
								   #Get (value of ransoms held by faction #1) - (value of ransoms held by faction #2)
								   (call_script, "script_dplmc_get_prisoners_value_between_factions", ":faction_no_1", ":faction_no_2"),
								   
								   (try_begin),
									 (eq, "$cheat_mode", 1),
									 (display_message, "@{!}DEBUG : prisoner_value: {reg0}"),#debug
								   (try_end),
								   (assign, ":prisoner_value", reg0),
								   
								   #Write result to reg0
								   (store_add, reg0, ":base_cost", ":center_cost"),
								   
								   #Scale for the player's wealth, to partially mitigate the problem
								   #of the cost becoming meaningless as the player's wealth increases.
								   #(Scale less than 1-to-1, so it is possible to become richer in real
								   #terms.)  This is also aimed at reducing the necessity of replacing
								   #the values in mods that alter gold scarcity.
								   (store_troop_gold, ":player_gold", "trp_household_possessions"),
								   (store_troop_gold, reg1, "trp_player"),
								   (val_add, ":player_gold", reg1),
								   (try_begin),
									  #Arbitrarily pick 100,000 as the target wealth, since that's when
									  #you get the Steam "gold farmer" achievement.
									  (gt, ":player_gold", 100000),
									  (store_div, reg1, ":player_gold", 1000),
									  (val_mul, reg1, reg0),
									  (val_div, reg1, 100),
									  
									  (val_add, reg0, reg1),
									  (val_div, reg0, 2),
									  
									  #Apply the same scaling to the concession value
									  (store_div, reg1, ":player_gold", 1000),
									  (val_mul, reg1, ":concession_value"),
									  (val_div, reg1, 100),
									  
									  (val_add, ":concession_value", reg1),
									  (val_div, ":concession_value", 2),
								   (try_end),

								   #Take into account campaign difficulty
								   (assign, ":min_cost", reg0),
								   (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
								   (try_begin),
									   (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
									   (val_mul, reg0, 3),
									   (val_div, reg0, 2),
									   (val_mul, ":min_cost", 87),#set min_cost to 87% of the original base_cost + center_cost
									   (val_div, ":min_cost", 100),
								   (else_try),
									   (eq, ":reduce_campaign_ai", 1), #moderate (1.0x)
									   (val_mul, ":min_cost", 3),
									   (val_div, ":min_cost", 4),#set min_cost to 75% (base cost + center cost)
								   (else_try),
										(eq, ":reduce_campaign_ai", 2), #easy (0.75x)
										(val_mul, reg0, 3),
										(val_div, reg0, 4),
										(val_mul, ":min_cost", 9),
										(val_div, ":min_cost", 16),#set min_cost to (75% squared) of (base cost + center cost)
								   (try_end),
								   
								   (val_sub, reg0, ":prisoner_value"),

								   #Because the NPC kingdom doesn't want peace, it will not agree to peace
								   #for free, as that would be a contradiction.
								   (val_max, reg0, ":min_cost"),

								   (try_begin),
									 (eq, "$cheat_mode", 1),
									 (display_message, "@{!}DEBUG : peace_war_result after prisoners: {reg0}"),#debug
								   (try_end),

								   #The value of the concession (if any) was already calculated above
								   (assign, reg1, -1),
								   (try_begin),
									  (gt, "$g_concession_demanded", 0),
									  (gt, ":concession_value", 0),
									  (store_sub, reg1, reg0, ":concession_value"),
									  (val_max, reg1, 0),
									  #Only accept cash alone in lieu of a fief if you don't partcularly
									  #want war, or if the AI is on "easy".
									  (try_begin),
										 (neq, ":reduce_campaign_ai", 2),#hard or medium
										 (lt, ":check_peace_war_result", 0),
										 (assign, reg0, -1),
									  (try_end),
								   (try_end),

								 (try_begin), #debug
								   (eq, "$cheat_mode", 1),
									 (display_message, "@{!}DEBUG : truce_pay_amount0: {reg0}"),
									 (display_message, "@{!}DEBUG : truce_pay_amount1: {reg1}"),
								 (try_end),
								 ##nested diplomacy end+
							]),
                          
						  ("dplmc_player_center_surrender",
						  [
							(store_script_param, ":center_no", 1),

							#protect player for 24 hours
							(store_current_hours,":protected_until"),
							(val_add, ":protected_until", 48),
							(party_get_slot, ":besieger", ":center_no", slot_center_is_besieged_by),
							(store_faction_of_party, ":besieger_faction",":besieger"),
							##nested diplomacy start+
							#In this version this variable currently isn't used for anything
							#(party_stack_get_troop_id, ":enemy_party_leader", ":besieger", 0),
							##nested diplomacy end+

							(party_set_slot,":besieger",slot_party_ignore_player_until,":protected_until"),
							(party_ignore_player, ":besieger", 48),
							##nested diplomacy start+
							#Add support for promoted kingdom ladies
							#(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
							(try_for_range, ":lord", heroes_begin, heroes_end),
							  (this_or_next|is_between, ":lord", active_npcs_begin, active_npcs_end),
							  (troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
							##nested diplomacy end+
							  (store_faction_of_troop, ":lord_faction", ":lord"),
							  (eq, ":lord_faction", ":besieger_faction"),
							  (troop_get_slot, ":led_party", ":lord", slot_troop_leaded_party),
							  (party_is_active, ":led_party"),

							  (party_slot_eq, ":led_party", slot_party_ai_state, spai_accompanying_army),
							  (party_slot_eq, ":led_party", slot_party_ai_object, ":besieger"),

							  (party_is_active, ":besieger"),
							  (store_distance_to_party_from_party, ":distance_to_marshal", ":led_party", ":besieger"),
							  (lt, ":distance_to_marshal", 20),

							  (party_set_slot,":led_party",slot_party_ignore_player_until,":protected_until"),
							  (party_ignore_player, ":led_party", 48),
							(try_end),

							(party_set_faction,"$current_town","fac_neutral"), #temporarily erase faction so that it is not the closest town
							(party_get_num_attached_parties, ":num_attached_parties_to_castle",":center_no"),
							(try_for_range_backwards, ":iap", 0, ":num_attached_parties_to_castle"),
							  (party_get_attached_party_with_rank, ":attached_party", ":center_no", ":iap"),
							  (party_detach, ":attached_party"),
							  (party_get_slot, ":attached_party_type", ":attached_party", slot_party_type),
							  (eq, ":attached_party_type", spt_kingdom_hero_party),
							  (neq, ":attached_party_type", "p_main_party"),
							  (store_faction_of_party, ":attached_party_faction", ":attached_party"),
							  (call_script, "script_get_closest_walled_center_of_faction", ":attached_party", ":attached_party_faction"),
							  (try_begin),
								(gt, reg0, 0),
								(call_script, "script_party_set_ai_state", ":attached_party", spai_holding_center, reg0),
							  (else_try),
								(call_script, "script_party_set_ai_state", ":attached_party", spai_patrolling_around_center, ":center_no"),
							  (try_end),
							(try_end),
							(call_script, "script_party_remove_all_companions", ":center_no"),
							(change_screen_return),
							(party_collect_attachments_to_party, ":center_no", "p_collective_enemy"), #recalculate so that
							(call_script, "script_party_copy", "p_encountered_party_backup", "p_collective_enemy"), #leaving troops will not be considered as captured

							##nested diplomacy start+
							#Anyone who lost a fief due to your surrender will be irritated
							(try_for_range, ":village_no", centers_begin, centers_end),
							   (party_slot_eq, ":village_no", slot_village_bound_center, ":center_no"),
							   (party_get_slot, ":village_lord", ":village_no", slot_town_lord),
							   (neq, ":village_lord", "trp_player"),
							   (is_between, ":village_lord", heroes_begin, heroes_end),
							   (call_script, "script_change_player_relation_with_troop", ":village_lord", -1),
							(try_end),
							##nested diplomacy end+
							##diplomacy
							(call_script, "script_give_center_to_faction", "$current_town", ":besieger_faction"),
							(call_script, "script_order_best_besieger_party_to_guard_center", ":center_no", ":besieger_faction"),

							#relation and controversy
							##nested diplomacy start+, There should be no relation bonus with the enemy lord
							#(call_script, "script_change_player_relation_with_troop", ":enemy_party_leader", 2),
							##nested diplomacy end+
							(try_begin),
							  (gt, "$players_kingdom", 0),
							  (neq, "$players_kingdom", "fac_player_supporters_faction"),
							  (neq, "$players_kingdom", "fac_player_faction"),
							  (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
							  ##diplomacy start+
							  ##OLD:
							  #(neq, ":faction_leader", "trp_player"),
							  ##NEW:
							  #Also guard against faction leader being some invalid negative number
							  (gt, ":faction_leader", "trp_player"),
							  ##diplomacy end+
							  (call_script, "script_change_player_relation_with_troop", ":faction_leader", -2),
							(try_end),

							(troop_get_slot, ":controversy", "trp_player", slot_troop_controversy),
							(val_add, ":controversy", 4),
							(val_min, ":controversy", 100),
							(troop_set_slot, "trp_player", slot_troop_controversy, ":controversy"),
							##nested diplmacy start+ add garrison to fief
							#The average # of troops added by script_cf_reinforce_party is 11.5.
							(assign, ":garrison_strength", 3),#easy: 34.5 for a castle
							(try_begin),
							   (party_slot_eq, ":center_no", slot_party_type, spt_town),
							   (assign, ":garrison_strength", 9),#easy: 103.5 for a town
							(try_end),
							#Take into account campaign difficulty.
							(game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
							(try_begin),
							   (eq, ":reduce_campaign_ai", 0), #hard 166% + 3 waves
							   (val_mul, ":garrison_strength", 5),
							   (val_div, ":garrison_strength", 3),
							   (val_add, ":garrison_strength", 3),
							(else_try),
							   (eq, ":reduce_campaign_ai", 1), #moderate 166%
							   (val_mul, ":garrison_strength", 5),
							   (val_div, ":garrison_strength", 3),
							#(else_try),
							#   (eq, ":reduce_campaign_ai", 2), #easy 100%
							#   (store_mul, ":garrison_strength", 1),
							(try_end),
								
							(try_for_range, ":unused", 0, ":garrison_strength"),
							   (call_script, "script_cf_reinforce_party", ":center_no"),
							(try_end),
							(try_for_range, ":unused", 0, 7),# ADD some XP initially
							   (store_mul, ":xp_range_min", 150, ":garrison_strength"),
							   (store_mul, ":xp_range_max", 200, ":garrison_strength"),
							   (store_random_in_range, ":xp", ":xp_range_min", ":xp_range_max"),
							   (party_upgrade_with_xp, ":center_no", ":xp", 0),
							(try_end),
							##nested diplomacy end+
						  ]),
                          
                          
                          ("dplmc_send_messenger_to_troop",
                            [
                              (store_script_param, ":target_troop", 1),
                              (store_script_param, ":message", 2),
                              (store_script_param, ":orders_object", 3),
                              
                              (troop_get_slot, ":target_party", ":target_troop", slot_troop_leaded_party),
                              
                              (try_begin),
                                (eq, ":message", spai_accompanying_army),
                                (assign, ":orders_object", "p_main_party"),
                              (try_end),
                              
                              (set_spawn_radius, 1),
                              (spawn_around_party, "$current_town", "pt_messenger_party"),
                              (assign,":spawned_party",reg0),
                              (party_add_members, ":spawned_party", "trp_dplmc_messenger", 1),
                              (store_faction_of_troop, ":player_faction", "trp_player"),
                              (party_set_faction, ":spawned_party", ":player_faction"),
                              (party_set_slot, ":spawned_party", slot_party_type, spt_messenger),
                              (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":message"),
                              (party_set_slot, ":spawned_party", slot_party_home_center, "$current_town"),
                              
                              (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
                              (party_set_ai_object, ":spawned_party", ":target_party"),
                              (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
                              (party_set_slot, ":spawned_party", slot_party_orders_object, ":orders_object"),
                              
                              (try_begin), #debug
                                (eq, "$cheat_mode", 1),
                                (str_store_party_name, s13, ":target_party"),
                                (display_message, "@{!}DEBUG - Send message to {s13}"),
                              (try_end),
                            ]
                          ),
                          
                          ("dplmc_send_messenger_to_party",
                            [
                              (store_script_param, ":target_party", 1),
                              (store_script_param, ":message", 2),
                              (store_script_param, ":orders_object", 3),
                              
                              (set_spawn_radius, 1),
                              (spawn_around_party, "$current_town", "pt_messenger_party"),
                              (assign,":spawned_party",reg0),
                              (party_add_members, ":spawned_party", "trp_dplmc_messenger", 1),
                              (party_set_faction, ":spawned_party", "fac_player_faction"),
                              (party_set_slot, ":spawned_party", slot_party_type, spt_messenger),
                              (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":message"),
                              (party_set_slot, ":spawned_party", slot_party_home_center, "$current_town"),
                              
                              (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
                              (party_set_ai_object, ":spawned_party", ":target_party"),
                              (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
                              (party_set_slot, ":spawned_party", slot_party_orders_object, ":orders_object"),
                              
                              (try_begin), #debug
                                (eq, "$cheat_mode", 1),
                                (str_store_party_name, s13, ":target_party"),
                                (display_message, "@{!}DEBUG - Send message to {s13}"),
                              (try_end),
                            ]
                          ),
                          
                          ("dplmc_send_gift",
                            [
                              (store_script_param, ":target_troop", 1),
                              (store_script_param, ":gift", 2),
							  (store_script_param, ":amount", 3),
                              
                              (try_begin),
                                (troop_slot_eq, ":target_troop", slot_troop_occupation, slto_kingdom_hero),
                                (troop_get_slot, ":target_party", ":target_troop", slot_troop_leaded_party),
                              (else_try),
                                (troop_slot_eq, ":target_troop", slot_troop_occupation, slto_kingdom_lady),
                                (troop_get_slot, ":target_party", ":target_troop", slot_troop_cur_center),
                              (try_end),
                              
                              
                              (try_begin), #debug
                                (eq, "$cheat_mode", 1),
                                (str_store_item_name, s12, ":gift"),
                                (str_store_party_name, s13, ":target_party"),
                                (display_message, "@{!}DEBUG - Bring {s12} to {s13}"),
                              (try_end),
                              
							(try_begin),
							   #Guard against this being called without an explicit amount
							   (lt, ":amount", 1),
							   (display_message, "@{!} ERROR: Bad gift amount {reg0}.  (Tell the mod writer he needs to update his code.)  Using a safe default."),
							   (assign, ":amount", 1),
							   (troop_slot_eq, ":target_troop", slot_troop_occupation, slto_kingdom_hero),
							   (assign, ":amount", 150),
							(try_end),
							  
                              (call_script, "script_dplmc_withdraw_from_treasury", 50),
                              (troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),

						  (try_for_range, ":inventory_slot", 0, ":capacity"),
							(gt, ":amount", 0),
							  (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
							  (eq, ":item", ":gift"),
							  (troop_inventory_slot_get_item_amount, ":tmp_amount", "trp_household_possessions", ":inventory_slot"),
							  (try_begin),
								(le, ":tmp_amount", ":amount"),
								(troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", 0),
								(val_sub, ":amount", ":tmp_amount"),
							  (else_try),
								(val_sub, ":tmp_amount", ":amount"),
								(troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", ":tmp_amount"),
								(assign, ":amount", 0),
							  (try_end),
						  (try_end),

                              
                              (set_spawn_radius, 1),
								##Floris MTT begin
								(try_begin),
									(eq, "$troop_trees", troop_trees_0),
								  (spawn_around_party, "$current_town", "pt_dplmc_gift_caravan"),
								(else_try),
									(eq, "$troop_trees", troop_trees_1),
								  (spawn_around_party, "$current_town", "pt_dplmc_gift_caravan_r"),
								(else_try),
									(eq, "$troop_trees", troop_trees_2),
									  (spawn_around_party, "$current_town", "pt_dplmc_gift_caravan_e"),
								(try_end),
								##Floris MTT end
                              (assign,":spawned_party",reg0),
                              (party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_gift_caravan),
                              (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":gift"),
                              (party_set_slot, ":spawned_party",  slot_party_orders_object,  ":target_troop"),
                              
                              (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
                              (party_set_ai_object, ":spawned_party", ":target_party"),
                              (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
                              (party_stack_get_troop_id, ":caravan_master", ":spawned_party", 0),
                              (troop_set_slot, ":caravan_master", slot_troop_leaded_party, ":spawned_party"),
							  (party_set_slot, ":spawned_party", dplmc_slot_party_mission_parameter_1, ":amount"),
                          ]),
                          
                          ("dplmc_send_gift_to_center",
                            [
                              (store_script_param, ":target_party", 1),
                              (store_script_param, ":gift", 2),
							  (store_script_param, ":amount", 3),
                              
                              (try_begin), #debug
                                (eq, "$cheat_mode", 1),
                                (str_store_item_name, s12, ":gift"),
                                (str_store_party_name, s13, ":target_party"),
                                (display_message, "@{!}DEBUG - Bring {s12} to {s13}"),
                              (try_end),
							  
							(try_begin),
							   #Guard against this being called without an explicit amount
							   (lt, ":amount", 1),
							   (display_message, "@{!} ERROR: Bad gift amount {reg0}.  (Tell the mod writer he needs to update his code.)  Using a safe default."),
							   (assign, ":amount", 300),
							(try_end),
                              
                              (call_script, "script_dplmc_withdraw_from_treasury", 50),
                              (troop_get_inventory_capacity, ":capacity", "trp_household_possessions"),
                              (try_for_range, ":inventory_slot", 0, ":capacity"),
                                (gt, ":amount", 0),
                                (troop_get_inventory_slot, ":item", "trp_household_possessions", ":inventory_slot"),
                                (eq, ":item", ":gift"),
                                (troop_inventory_slot_get_item_amount, ":tmp_amount", "trp_household_possessions", ":inventory_slot"),
                                (try_begin),
                                  (le, ":tmp_amount", ":amount"),
                                  (troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", 0),
                                  (val_sub, ":amount", ":tmp_amount"),
                                (else_try),
                                  (val_sub, ":tmp_amount", ":amount"),
                                  (troop_inventory_slot_set_item_amount, "trp_household_possessions", ":inventory_slot", ":tmp_amount"),
                                  (assign, ":amount", 0),
                                (try_end),
                              (try_end),
                              
                              (set_spawn_radius, 1),
								##Floris MTT begin
								(try_begin),
									(eq, "$troop_trees", troop_trees_0),
									(spawn_around_party, "$current_town", "pt_dplmc_gift_caravan"),
								(else_try),
									(eq, "$troop_trees", troop_trees_1),
								  (spawn_around_party, "$current_town", "pt_dplmc_gift_caravan_r"),
								(else_try),
									(eq, "$troop_trees", troop_trees_2),
								  (spawn_around_party, "$current_town", "pt_dplmc_gift_caravan_e"),
								(try_end),
								##Floris MTT end
                              (assign,":spawned_party",reg0),
                              (party_set_slot, ":spawned_party", slot_party_type, dplmc_spt_gift_caravan),
                              (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":gift"),
                              (party_set_slot, ":spawned_party",  slot_party_orders_object, 0),
                              
                              (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
                              (party_set_ai_object, ":spawned_party", ":target_party"),
                              (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
                              (party_stack_get_troop_id, ":caravan_master", ":spawned_party", 0),
                              (troop_set_slot, ":caravan_master", slot_troop_leaded_party, ":spawned_party"),
                              (troop_set_slot, ":caravan_master", slot_troop_leaded_party, ":spawned_party"),
							  (party_set_slot, ":spawned_party", dplmc_slot_party_mission_parameter_1, ":amount"),
                          ]),
                          
					   ("dplmc_troop_political_notes_to_s47",
						  [
						(store_script_param, ":troop_no", 1),
						##diplomacy start+
						(assign, ":save_reg1", reg1),#save to revert
						(assign, ":save_reg4", reg4),#save to revert
						
						(try_begin),
						   (eq, 0, 1),#Always disable this right now
						   (is_between, "$g_talk_troop", heroes_begin, heroes_end),#i.e. not your chancellor
						   (assign, ":troop_speaker", "$g_talk_troop"),
						   (call_script, "script_troop_get_player_relation", ":troop_speaker"),
						   (assign, ":speaker_player_relation", reg0),
						(else_try),
						   (assign, ":troop_speaker", -1),
						   (assign, ":speaker_player_relation", 100),
						(try_end),
						##diplomacy end+
						
						(try_begin),
						  (str_clear, s47),

						  (store_faction_of_troop, ":troop_faction", ":troop_no"),

						  (faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),

						  (str_clear, s40),
						  (assign, ":logged_a_rivalry", 0),
						  ##nested diplomacy start+
						  (str_clear, s41),
						  #lord can be married or related to player
						  #(try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
						  (try_for_range, ":kingdom_hero", active_npcs_including_player_begin, active_npcs_end),
							#Also, don't include rivalries with retired (or dead) characters
							(neg|troop_slot_ge, ":troop_no", slot_troop_occupation, slto_retirement), 
						  ##nested diplomacy end+
							(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":kingdom_hero"),
							(lt, reg0, -10),

							(str_store_troop_name_link, s39, ":kingdom_hero"),
							  ##nested diplomacy start+ use second person
							(try_begin),
							   (eq, ":kingdom_hero", "trp_player"),
							   (str_store_string, s39, "str_you"),
						(try_end),
							  ##nested diplomacy end+
							(try_begin),
							  (eq, ":logged_a_rivalry", 0),
							  ##nested diplomacy start+
							  (call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 4),#use reg4 for gender-correct pronoun
							  ##nested diplomacy end+
							  (str_store_string, s40, "str_dplmc_s39_rival"),
							  (assign, ":logged_a_rivalry", 1),
							(else_try),
							  (str_store_string, s41, "str_s40"),
							  (str_store_string, s40, "str_dplmc_s41_s39_rival"),
							(try_end),

						  (try_end),

						  (str_clear, s46),
						  ##nested diplomacy start+
						  #(troop_get_type, reg4, ":troop_no"),#use for gender-correct pronoun
							(call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 4),
						  (str_store_troop_name, s46,":troop_no"),
						  (assign, ":details_available", 0),
						  (try_begin),
							#Enable details for lords you have met
							(neg|troop_slot_eq, ":troop_no", slot_troop_met, 0),
							(assign, ":details_available", 1),
							  (else_try),
									#Enable details when using an "omniscient" or non-specific speaker
									(neg|is_between, ":troop_speaker", heroes_begin, heroes_end),
									(assign, ":details_available", 1),
							  (else_try),
									#Enable details for NPCs that aren't standard heroes, because the following checks don't apply
									(neg|is_between, ":troop_no", heroes_begin, heroes_end),
									(assign, ":details_available", 1),
							  (else_try),
									#Enable details for lords the speaker has met
									(is_between, ":troop_speaker", heroes_begin, heroes_end),
									(is_between, ":troop_no", heroes_begin, heroes_end),
									(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":troop_speaker"),
									(neq, reg0, 0),#between NPCs, relation 0 means "have not met"
									(assign, ":details_available", 1),
							  (else_try),
									#Enable details for v. notable lords (based on renown)
									(troop_slot_ge, ":troop_no", slot_troop_renown, 500),
									(assign, ":details_available", 1),
							  (else_try),
									#Enable details for v. notable lords (based on fiefs)
									(assign, reg0, 0),
									(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
									   (this_or_next|party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
									   (this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":troop_no"),
										 (troop_slot_eq, ":troop_no", slot_troop_home, ":center_no"),
									   (val_add, reg0, 2),
									   (party_slot_eq, ":center_no", slot_party_type, spt_town),
									   (val_add, reg0, 2),
									(try_end),
									(ge, reg0, 4),#one town, or 2+ castles
									(assign, ":details_available", 1),
							  (try_end),
						  #xxx TODO: Make a full implementation of the above that takes into account the time of the last spy report.
						  (try_begin),
							(eq, ":details_available", 0),
							(troop_get_slot, reg11, ":troop_no", slot_lord_reputation_type),
							(str_store_string, s46, "str_dplmc_reputation_unknown"),
						  (else_try),
						  ##nested diplomacy end+
							(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
							(str_store_string, s46, "str_dplmc_reputation_martial"),
						  (else_try),
							(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
							(str_store_string, s46, "str_dplmc_reputation_debauched"),
						  (else_try),
							(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
							(str_store_string, s46, "str_dplmc_reputation_pitiless"),
						  (else_try),
							(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
							(str_store_string, s46, "str_dplmc_reputation_calculating"),
						  (else_try),
							(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
							(str_store_string, s46, "str_dplmc_reputation_quarrelsome"),
						  (else_try),
							(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
							(str_store_string, s46, "str_dplmc_reputation_goodnatured"),
						  (else_try),
							(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
							(str_store_string, s46, "str_dplmc_reputation_upstanding"),
						  (else_try),
							(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_conventional),
							(str_store_string, s46, "str_dplmc_reputation_conventional"),
						  (else_try),
							(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_adventurous),
							(str_store_string, s46, "str_dplmc_reputation_adventurous"),
						  (else_try),
							(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_otherworldly),
							(str_store_string, s46, "str_dplmc_reputation_romantic"),
						  (else_try),
							(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_moralist),
							(str_store_string, s46, "str_dplmc_reputation_moralist"),
						  (else_try),
							(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_ambitious),
							(str_store_string, s46, "str_dplmc_reputation_ambitious"),
						  (else_try),
							(troop_get_slot, reg11, ":troop_no", slot_lord_reputation_type),
							(str_store_string, s46, "str_dplmc_reputation_unknown"),
						  (try_end),

						  ##diplomacy start+
						  (str_clear, s39),#remove annoying bug
						  (str_clear, s45),#remove annoying bug

						  #Special-case spouse into showing up if it doesn't get added below
						  (try_begin),
							 (troop_get_slot, ":spouse", ":troop_no", slot_troop_spouse),
							 (ge, ":spouse", 0),

							 #Because blank memory is initially zero, enforce this
							 (this_or_next|is_between, ":troop_no", heroes_begin, heroes_end),
								(neq, ":spouse", "trp_player"),
							 #Initialize s45
							 (str_store_troop_name, s39, ":spouse"),
							 (try_begin),
								(eq, ":spouse", "trp_player"),
								(str_store_string, s39, "str_you"),##<-- dplmc+ note, this was s59 before, probably an accidental bug
							 (try_end),
							 (str_store_string, s45, "str_dplmc_s40_married_s39"),
						  (try_end),
						  ##diplomacy end+

						  (try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
							(troop_get_slot, ":love_interest", ":troop_no", ":love_interest_slot"),
							##nested diplomacy start+ ; some lords could romance opposite-gender lords
							#(is_between, ":love_interest", kingdom_ladies_begin, kingdom_ladies_end),
							(is_between, ":love_interest", active_npcs_begin, kingdom_ladies_end),
							#Also prevent a bug for companions / claimants who are lords
							(neq, ":love_interest", "trp_knight_1_1_wife"),#<- should not appear in the game
							#Also prevent bad messages for married/betrothed lords
							(this_or_next|troop_slot_eq, ":troop_no", slot_troop_spouse, ":love_interest"),
							   (troop_slot_eq, ":troop_no", slot_troop_spouse, -1),
							(this_or_next|troop_slot_eq, ":troop_no", slot_troop_betrothed, ":love_interest"),
							   (troop_slot_eq, ":troop_no", slot_troop_betrothed, -1),
							##nested diplomacy end+
							(str_store_troop_name, s39, ":love_interest"),
							##nested diplomacy start+ Use second person properly
							(try_begin),
							   (eq, ":love_interest", "trp_player"),
							   (str_store_string, s39, "str_you"),
							(try_end),
							##nested diplomacy start+
							(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":love_interest"),
							##nested diplomacy start+
							(call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 4),#use reg4 for gender-correct pronoun
							##nested diplomacy end+
							(str_store_string, s45, "str_dplmc_s40_love_interest_s39"),
							(try_begin),
								(troop_slot_eq, ":troop_no", slot_troop_spouse, ":love_interest"),
								(str_store_string, s45, "str_dplmc_s40_married_s39"),
							(else_try),
								(troop_slot_eq, ":troop_no", slot_troop_betrothed, ":love_interest"),
								(str_store_string, s45, "str_dplmc_s40_betrothed_s39"),
							(try_end),
						  (try_end),

						(str_clear, s44),
						(try_begin),
						  (neq, ":troop_no", ":faction_leader"),
						  ##nested diplomacy start+
						  (gt, ":details_available", 0),
						  #Ensure leader is valid
						  (assign, reg0, 0),#continue if 0
						  (try_begin),
							 (neq, ":troop_no", "trp_player"),
							 (neq, ":faction_leader", "trp_player"),
							 (this_or_next|neg|is_between, ":troop_no", heroes_begin, heroes_end),
								(neg|is_between, ":faction_leader", heroes_begin, heroes_end),
							 (assign, reg0, 1),
						  (try_end),
						  (eq, reg0, 0),
						  
						  (try_begin),
							 (gt, ":troop_speaker", 0),
							 (call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_no", ":troop_speaker"),
							 #(val_min, reg0, 20),
							 #(neq, ":faction_leader", "trp_player"),
							 #(val_div, reg0, 2),
						  (try_end),
						  (this_or_next|lt, reg0, 1),
							(ge, ":speaker_player_relation", 1),
						  ##nested diplomacy end+
						  (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),

						  (assign, ":relation", reg0),
						  ##diplomacy start+ Don't mention anything for kingdom ladies at the beginning; it doesn't add information.
						  (this_or_next|lt, reg0, 0),
						  (this_or_next|gt, reg0, 1),#Remember that relation 1 is neutral (it just means "met") between NPCs
						  (this_or_next|neg|is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
						  (this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
						  (this_or_next|troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
							 (troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_lord_rejoined),
						  ##diplomacy end+
						  (store_add, ":normalized_relation", ":relation", 100),
						  (val_add, ":normalized_relation", 5),
						  (store_div, ":str_offset", ":normalized_relation", 10),
						  (val_clamp, ":str_offset", 0, 20),
						  ##nested diplomacy start+
						  #(troop_get_type, reg4, ":troop_no"),#use for gender-correct pronoun
						  (call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 4),
						  #TODO: Come back and add this (take into account spying)
						  #(neq, ":details_available", 0),#don't show unless more details are available
						  ##nested diplomacy end+
						  (store_add, ":str_id", "str_dplmc_relation_mnus_100_ns",  ":str_offset"),
						  (try_begin),
							(eq, ":faction_leader", "trp_player"),
							##nested diplomacy start+ "str_you" exists, so we might as well use it
							#(str_store_string, s59, "@you"),
							(str_store_string, s59, "str_you"),
							##diplomacy end+
						  (else_try),
							(str_store_troop_name, s59, ":faction_leader"),
						  (try_end),
						  (str_store_string, s59, ":str_id"),
						  (str_store_string, s44, "@{!}^{s59}"),
						(try_end),

						(str_clear, s48),

						(try_begin),
						  (eq, "$cheat_mode", 1),
						  (store_current_hours, ":hours"),
						  (gt, ":hours", 0),
						  (call_script, "script_calculate_troop_political_factors_for_liege", ":troop_no", ":faction_leader"),
						  (str_store_string, s48, "str_sense_of_security_military_reg1_court_position_reg3_"),
						(try_end),

						(str_store_string, s47, "str_s46s45s44s48"),

					  (try_end),
						 ##diplomacy start+
						 (assign, reg1, ":save_reg1"),#revert register
						 (assign, reg4, ":save_reg4"),#revert register to avoid clobbering
						 ##diplomacy end+
						]),
                          
                          ("dplmc_send_patrol",
                            [
                              (store_script_param, ":start_party", 1),
                              (store_script_param, ":target_party", 2),
                              (store_script_param, ":size", 3), #0 small, 1 medium, 2, big, 3 elite
                              (store_script_param, ":template_faction", 4),
                              (store_script_param, ":order_troop", 5), #Diplomacy 3.3.2
                              
                              (set_spawn_radius, 1),
                              (spawn_around_party, ":start_party", "pt_patrol_party"),
                              (assign,":spawned_party",reg0),
                              (party_set_faction, ":spawned_party", ":template_faction"),
                              (party_set_slot, ":spawned_party", slot_party_type, spt_patrol),
                              (party_set_slot, ":spawned_party", slot_party_home_center, ":start_party"),
                              (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":order_troop"), #Diplomacy 3.3.2
                              (str_store_party_name, s5, ":target_party"),
                              (party_set_name, ":spawned_party", "@{s5} patrol"),
                              
                              (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
                              (party_set_ai_object, ":spawned_party", ":target_party"),
                              (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
                              (party_set_slot, ":spawned_party", slot_party_ai_state, spai_patrolling_around_center),
                              
                              (try_begin),
                                (eq, ":template_faction", "fac_player_faction"),
                                
                                (party_get_slot, ":template_faction", ":start_party", slot_center_original_faction),
                                (try_begin),
                                  (is_between, "$g_player_culture", kingdoms_begin, kingdoms_end), #Player Faction
                                  (assign, ":template_faction", "$g_player_culture"),
                                (else_try),
                                  (party_get_slot, ":town_lord", ":start_party", slot_town_lord),
                                  (gt, ":town_lord", 0),
                                  (troop_get_slot, ":template_faction", ":town_lord", slot_troop_original_faction),
                                (try_end),
                                
                                (try_begin),
                                  (eq, ":size", 0),
                                  (call_script, "script_dplmc_withdraw_from_treasury", 1000),
                                (else_try),
                                  (this_or_next|eq, ":size", 1),
                                  (eq, ":size", 3),
                                  (call_script, "script_dplmc_withdraw_from_treasury", 2000),
                                (else_try),
                                  (eq, ":size", 2),
                                  (call_script, "script_dplmc_withdraw_from_treasury", 3000),
                                (try_end),
                              (try_end),
                              
                              (faction_get_slot, ":party_template_a", ":template_faction", slot_faction_reinforcements_a),
                              (faction_get_slot, ":party_template_b", ":template_faction", slot_faction_reinforcements_b),
                              (faction_get_slot, ":party_template_c", ":template_faction", slot_faction_reinforcements_c),
                              (faction_get_slot, ":party_template_d", ":template_faction", slot_faction_reinforcements_d),
                              (faction_get_slot, ":party_template_e", ":template_faction", slot_faction_reinforcements_e),
                              (faction_get_slot, ":party_template_f", ":template_faction", slot_faction_reinforcements_f),
                              
                              (try_begin),
                                (eq, ":size", 3),
                                (party_add_template, ":spawned_party", ":party_template_f"),
                                (party_add_template, ":spawned_party", ":party_template_f"),
                              (else_try),
                                (val_add, ":size", 1),
                                (val_mul, ":size", 2),
                                (try_for_range, ":cur_i", 0, ":size"),
                                  (store_random_in_range, ":random", 0, 3),
                                  (try_begin),
                                    (eq, ":random", 0),
                                    (party_add_template, ":spawned_party", ":party_template_a"),
                                  (else_try),
                                    (eq, ":random", 0),
                                    (party_add_template, ":spawned_party", ":party_template_b"),
                                  (else_try),
                                    (eq, ":random", 1),
                                    (party_add_template, ":spawned_party", ":party_template_c"),
                                  (else_try),
                                    (eq, ":random", 1),
                                    (party_add_template, ":spawned_party", ":party_template_d"),
                                  (else_try),
                                    (eq, ":random", 1),
                                    (party_add_template, ":spawned_party", ":party_template_e"),
                                  (else_try),
                                    (party_add_template, ":spawned_party", ":party_template_f"),
                                  (try_end),
                                  
                                  (try_begin), #debug
                                    (eq, "$cheat_mode", 1),
                                    (assign, reg0, ":cur_i"),
                                    (str_store_faction_name, s7, ":template_faction"),
                                    (display_message, "@{!}DEBUG - Added {reg0}.template of faction {s7} to patrol."),
                                  (try_end),
                                (try_end),
                              (try_end),
                              
                              
                              (try_begin), #debug
                                (eq, "$cheat_mode", 1),
                                (str_store_party_name, s13, ":target_party"),
                                (str_store_faction_name, s14, ":template_faction"),
                                (str_store_party_name, s15, ":start_party"),
                                (display_message, "@{!}DEBUG - Send {s14} patrol from {s15} to {s13}"),
                              (try_end),
							  
							  (assign, reg0, ":spawned_party"), ##Floris - allow to get party ID after creation (for outposts now, but may be useful later, too)
                          ]),
                          
                          ("dplmc_send_patrol_party",
                            [
                              (store_script_param, ":start_party", 1),
                              (store_script_param, ":target_party", 2),
                              (store_script_param, ":party_no", 3),
                              (store_script_param, ":template_faction", 4),
							  (store_script_param, ":order_troop", 5), #FLORIS BUGFIX
                              
                              (set_spawn_radius, 1),
                              (spawn_around_party, ":start_party", "pt_patrol_party"),
                              (assign,":spawned_party",reg0),
                              (party_set_faction, ":spawned_party", ":template_faction"),
                              (party_set_slot, ":spawned_party", slot_party_type, spt_patrol),
                              (party_set_slot, ":spawned_party", slot_party_home_center, ":start_party"),
							  (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":order_troop"), #FLORIS BUGFIX
                              (str_store_party_name, s5, ":target_party"),
                              (party_set_name, ":spawned_party", "@{s5} patrol"),
                              
                              (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
                              (party_set_ai_object, ":spawned_party", ":target_party"),
                              (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
                              (party_set_slot, ":spawned_party", slot_party_ai_state, spai_patrolling_around_center),
                              
                              (call_script, "script_party_add_party", ":spawned_party", ":party_no"),
                          ]),
                          
                          ("dplmc_move_troops_party",
                            [
                              (store_script_param, ":start_party", 1),
                              (store_script_param, ":target_party", 2),
                              (store_script_param, ":party_no", 3),
                              (store_script_param, ":template_faction", 4),
							  (store_script_param, ":order_troop", 5), #FLORIS BUGFIX
                              
                              (set_spawn_radius, 1),
                              (spawn_around_party, ":start_party", "pt_patrol_party"),
                              (assign,":spawned_party",reg0),
                              (party_set_faction, ":spawned_party", ":template_faction"),
                              (party_set_slot, ":spawned_party", slot_party_type, spt_patrol),
                              (party_set_slot, ":spawned_party", slot_party_home_center, ":start_party"),
							  (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":order_troop"), #FLORIS BUGFIX
                              (str_store_party_name, s5, ":target_party"),
                              (party_set_name, ":spawned_party", "@Transfer to {s5}"),
                              
                              (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
                              (party_set_ai_object, ":spawned_party", ":target_party"),
                              (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
                              (party_set_slot, ":spawned_party", slot_party_ai_state, spai_retreating_to_center),
                              (party_set_aggressiveness, ":spawned_party", 2),
                              (party_set_courage, ":spawned_party", 3),
                              (party_set_ai_initiative, ":spawned_party", 100),
                              
                              (call_script, "script_party_add_party", ":spawned_party", ":party_no"),
                          ]),
                          
                          ("dplmc_send_scout_party",
                            [
                              (store_script_param, ":start_party", 1),
                              (store_script_param, ":target_party", 2),
                              (store_script_param, ":faction", 3),
                              
                              (set_spawn_radius, 1),
                              (spawn_around_party, ":start_party", "pt_scout_party"),
                              (assign,":spawned_party",reg0),
                              (party_set_faction, ":spawned_party", ":faction"),
                              (party_set_slot, ":spawned_party", slot_party_type, spt_scout),
                              (party_set_slot, ":spawned_party", slot_party_home_center, ":start_party"),
                              (str_store_party_name, s5, ":target_party"),
                              (party_set_name, ":spawned_party", "@{s5} scout"),
                              
                              (party_add_members, ":spawned_party", "trp_dplmc_scout", 1),
                              
                              (party_get_position, pos1, ":target_party"),
                              (map_get_random_position_around_position, pos2, pos1, 1),
                              (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_point),
                              (party_set_ai_target_position, ":spawned_party", pos2),
                              (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
                              (party_set_slot, ":spawned_party", slot_party_orders_object, ":target_party"),
                              (party_set_aggressiveness, ":spawned_party", 2),
                              (party_set_courage, ":spawned_party", 3),
                              (party_set_ai_initiative, ":spawned_party", 100),
                          ]),
                          
                          ("dplmc_init_domestic_policy",
                            [
                              (try_for_range, ":kingdom", npc_kingdoms_begin, npc_kingdoms_end),
                                (try_begin),
                                  (store_random_in_range, ":random", -3, 4),
                                  (faction_set_slot, ":kingdom", dplmc_slot_faction_centralization, ":random"),
                                  (store_random_in_range, ":random", -3, 4),
                                  (faction_set_slot, ":kingdom", dplmc_slot_faction_aristocracy, ":random"),
                                  (store_random_in_range, ":random", -3, 4),
                                  (faction_set_slot, ":kingdom", dplmc_slot_faction_quality, ":random"),
                                  (store_random_in_range, ":random", -3, 4),
                                  (faction_set_slot, ":kingdom", dplmc_slot_faction_serfdom, ":random"),
                                (try_end),
                              (try_end),
                          ]),
                          
						  ("dplmc_is_affiliated_family_member",
						  [
							  (store_script_param, ":troop_id", 1),
							  
							  (assign, ":is_affiliated_family_member", 0),
							  ##nested diplomacy start+
							  (assign, ":save_reg1", reg1),#<- Save reg1 which gets overwritten by script_dplmc_troop_get_family_relation_to_troop
							  ##nested diplomacy end+
							  (try_begin),
								(is_between, "$g_player_affiliated_troop", lords_begin, kingdom_ladies_end),
								(try_begin),
								  ##nested diplomacy start+ add use of dplmc_slot_troop_affiliated
								  (this_or_next|troop_slot_eq, ":troop_id", dplmc_slot_troop_affiliated, 3),
								  ##diplomacy end+
								  (eq, "$g_player_affiliated_troop", ":troop_id"),
								  (assign, ":is_affiliated_family_member", 1),
								(else_try),
								  (is_between, ":troop_id", lords_begin, kingdom_ladies_end),
								  ##nested diplomacy start+
								  #(call_script, "script_troop_get_family_relation_to_troop", ":troop_id", "$g_player_affiliated_troop"),
								  (call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_id", "$g_player_affiliated_troop"),
								  ##nested diplomacy end+
								  (gt, reg0, 0),
								  (call_script, "script_troop_get_relation_with_troop", "$g_player_affiliated_troop", ":troop_id"),
								  (ge, reg0, -10),
								  (assign, ":is_affiliated_family_member", 1),
								(try_end),
							  (try_end),
							  ##nested diplomacy start+
							  (assign, reg1, ":save_reg1"),#revert register
							  ##nested diplomacy end+
							  (assign, reg0, ":is_affiliated_family_member"),
						  ]),
                          
						   ("dplmc_affiliate_end",
						  [
							(store_script_param, ":cause", 1),

							(assign, "$g_player_affiliated_troop", 0),

							(try_begin),
							  (eq, ":cause", 1),
							  (assign, ":max_penalty", -16),
							  (assign, ":term", 20),
							  (assign, ":honor_val", 10),
							(else_try),
							  (assign, ":max_penalty", -12),
							  (assign, ":honor_val", 5),
							  (assign, ":term", 15),
							(try_end),

							(try_for_range, ":family_member", lords_begin, kingdom_ladies_end),
							  (call_script, "script_dplmc_is_affiliated_family_member", ":family_member"),
							  (gt, reg0, 0),

							  (store_skill_level, ":value", "skl_persuasion", "trp_player"),
							  (store_random_in_range, ":value", 0, ":value"),
							  ##nested diplomacy start+   Fix mistake.
							  ##
							  ##OLD:
							  #(val_add, ":value", ":max_penalty", ":value"),
							  #
							  #NEW:
							  #I'm pretty sure this is what was intended.
							  (val_add, ":value", ":max_penalty"),
							  ##nested diplomacy end+
							  (val_min, ":value", 0),
							  (call_script, "script_change_player_relation_with_troop", ":family_member", ":value"),
							(try_end),

							(try_begin),
							  (gt, "$player_honor", ":honor_val"),
							  (val_add, ":term", ":honor_val"),
							(else_try),
							  (val_add, ":term", "$player_honor"),
							(try_end),

							(store_current_hours, ":cur_hours"),
							(store_sub, ":affiliated_hours", ":cur_hours", "$g_player_affiliated_time"),
							(store_div, ":affiliated_days", ":affiliated_hours", 24),
							(val_sub, ":term", ":affiliated_days"),
							(val_max, ":term", 0),
							(val_min, ":term", 40),


							(troop_get_slot, ":controversy", "trp_player", slot_troop_controversy),
							(val_add, ":controversy", ":term"),
							(val_min, ":controversy", 100),
							(troop_set_slot, "trp_player", slot_troop_controversy, ":controversy"),

						  ]),
												  
                          ("dplmc_appoint_chamberlain",
                            [
                              (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_body, "itm_ar_swa_tun_tabard"),##Diplomacy 3.2
                              (troop_set_inventory_slot, "trp_dplmc_chamberlain", ek_foot, "itm_bo_swa_t2_hose"),
                              (assign, "$g_player_chamberlain", "trp_dplmc_chamberlain"),##
                          ]),
                          
                          ("dplmc_appoint_chancellor",
                            [
                              (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_body, "itm_ar_vae_nob_outfit"),##Diplomacy 3.2
                              (troop_set_inventory_slot, "trp_dplmc_chancellor", ek_foot, "itm_bo_vae_t2_shoes"),
                              (assign, "$g_player_chancellor", "trp_dplmc_chancellor"), ##
                          ]),
                          
                          ("dplmc_appoint_constable",
                            [
                              (troop_set_inventory_slot, "trp_dplmc_constable", ek_body, "itm_ar_swa_dip_coatplate_a"),##Diplomacy 3.2
                              (troop_set_inventory_slot, "trp_dplmc_constable", ek_foot, "itm_bo_swa_t5_hose"),
                              (assign, "$g_player_constable", "trp_dplmc_constable"),##
                          ]),
                          
                          ##diplomacy end
                          
						  #Decide whether an NPC wants to exchange a fief or not.
						#
						# param#1 is NPC being asked
						# param#2 is that NPC's fief being asked for
						# param#3 is the one asking (usually the player)
						# param#4 is the fief being offered in exchange
						#
						# Result is returned in reg0.  Negative means "no", zero means "yes",
						# positive means "yes but you have to pay me this amount".
						# If the result is negative, the response string is stored in s14.
						  ("dplmc_evaluate_fief_exchange",
							[
							  (store_script_param, ":target_npc", 1),
							  (store_script_param, ":target_fief", 2),
							  (store_script_param, ":asker", 3),
							  (store_script_param, ":offered_fief", 4),

							  (assign, ":result", -1),
							  (assign, reg0, ":result"),
							  (str_store_string, s14, "str_ERROR_string"),

							  (try_begin),
								  #Both NPCs are valid, and are not same character.  One can be the player.
								  (neq, ":target_npc", ":asker"),
								  (is_between, ":target_npc", heroes_begin, heroes_end),
								  (this_or_next|is_between, ":asker", heroes_begin, heroes_end),
									 (eq,":asker","trp_player"),
								  #Both fiefs are valid and owned by the lords in the arguments
								  (is_between, ":target_fief", centers_begin, centers_end),
								  (party_slot_eq, ":target_fief", slot_town_lord, ":target_npc"),
								  (is_between, ":offered_fief", centers_begin, centers_end),
								  (party_slot_eq, ":offered_fief", slot_town_lord, ":asker"),
								  #The lords are in the same faction
								  (store_troop_faction, ":target_faction", ":target_npc"),
								  (store_troop_faction, ":asker_faction", ":asker"),
								  (try_begin),
									 #Special handling needed for player faction
									 (eq, ":asker", "trp_player"),
									 (neg|eq, ":target_faction", ":asker_faction"),
									 (assign, ":asker_faction", "$players_kingdom"),
								  (try_end),
								  (this_or_next|eq, ":target_faction", ":asker_faction"),
									 (this_or_next|faction_slot_eq,":target_faction",slot_faction_leader,":asker"),
									 (faction_slot_eq,":asker_faction",slot_faction_leader,":target_npc"),
								  #Get prosperity for use in later tests
								  (party_get_slot, ":target_prosperity", ":target_fief", slot_town_prosperity),
								  (party_get_slot, ":offered_prosperity", ":offered_fief", slot_town_prosperity),
								  (store_div, ":min_prosperity", ":target_prosperity", 10),
								  (val_mul, ":min_prosperity", 10),
								  #...take into account relation
								  (call_script, "script_troop_get_relation_with_troop", ":target_npc", ":asker"),
								  (store_div, ":relation_div_10", reg0, 10),
								  (val_sub, ":min_prosperity", ":relation_div_10"),
								  #...take into account persuasion
								  (store_skill_level, ":asker_persuasion", "skl_persuasion", ":asker"),
								  (val_sub, ":min_prosperity", ":asker_persuasion"),
								  #...take into account personal (not party) trade skill
								  (store_skill_level, ":asker_trade", "skl_trade", ":asker"),
								  (val_sub, ":min_prosperity", ":asker_trade"),
								  #...don't let it rise above original's prosperity.
								  (val_min, ":min_prosperity", ":target_prosperity"),
								  #target_type 1 = village, 2 = castle, 3 = town
								  (assign, ":target_type", 0),
								  (try_begin),
									(party_slot_eq, ":target_fief", slot_party_type, spt_town),
									(assign, ":target_type", 3),
								  (else_try),
									(party_slot_eq, ":target_fief", slot_party_type, spt_castle),
									(assign, ":target_type", 2),
								  (else_try),
									(party_slot_eq, ":target_fief", slot_party_type, spt_village),
									(assign, ":target_type", 1),
								  (try_end),
								  (ge, ":target_type", 1),#break with error if the type was bad
								  #offered_type: 1 = village, 2 = castle, 3 = town
								  (assign, ":offered_type", 0),
								  (try_begin),
									(party_slot_eq, ":offered_fief", slot_party_type, spt_town),
									(assign, ":offered_type", 3),
								  (else_try),
									(party_slot_eq, ":offered_fief", slot_party_type, spt_castle),
									(assign, ":offered_type", 2),
								  (else_try),
									(party_slot_eq, ":offered_fief", slot_party_type, spt_village),
									(assign, ":offered_type", 1),
								  (try_end),
								  (ge, ":offered_type", 1),#break with error if the type was bad
								  #Now execute comparison logic:
								  (try_begin),
									#refuse to trade town for a castle or village 
									(lt, ":offered_type", ":target_type"),
									(eq, ":target_type", 3), 
									(str_store_string, s14, "str_dplmc_fief_exchange_refuse_town"),
								  (else_try),
									#refuse to trade any better type for a worse type
									(lt, ":offered_type", ":target_type"),
									(str_store_string, s14, "str_dplmc_fief_exchange_refuse_castle"), 
								  (else_try),
									#refuse to trade for something under siege or being raided
									(this_or_next|party_slot_eq, ":offered_fief", slot_village_state, svs_under_siege), 
									(party_slot_eq, ":offered_fief", slot_village_state, svs_being_raided),
									(str_store_party_name, s14, ":offered_fief"),
									(str_store_string, s14, "str_dplmc_fief_exchange_refuse_s14_attack"),
								  (else_try),
									#accept a trade if the offered type is better
									(lt, ":target_type", ":offered_type"),
									(str_store_string, s14, "str_dplmc_fief_exchange_accept"),
									(assign, ":result", 0),
								  (else_try),
									#refuse to trade away home center (unless trading up for a better type)
									#Target fief is home of NPC...
									(this_or_next|party_slot_eq, ":target_fief", dplmc_slot_center_original_lord, ":target_npc"),
									   (troop_slot_eq, ":target_npc", slot_troop_home, ":target_fief"),
									(neg|party_slot_eq, ":offered_fief", dplmc_slot_center_original_lord, ":target_npc"),
									#...and offered fief is not.
									(neg|troop_slot_eq, ":target_npc", slot_troop_home, ":offered_fief"),
									(this_or_next|neg|is_between, ":target_npc", companions_begin, companions_end),
									(neg|troop_slot_eq, ":target_npc", slot_troop_town_with_contacts, ":offered_fief"),
									(str_store_party_name, s14, ":target_fief"), #Line added by zerilius
									(str_store_string, s14, "str_dplmc_fief_exchange_refuse_home"),
								  (else_try),
									#refuse trade if prosperity is too low
									(lt, ":offered_prosperity", ":min_prosperity"),
									(str_store_string, s14, "str_dplmc_fief_exchange_refuse_rich"),
								  (else_try),
									#accept trade for 0 or more denars
									(store_sub, ":result", ":target_prosperity", ":offered_prosperity"),
									(val_mul, ":result", ":target_type"),
									(val_mul, ":result", 36),#Should probably be 60 instead
									#(val_div, ":result", 100),
									(val_add, ":result", 2000),
									(val_max, ":result", 0),
									(try_begin),
									   (ge, ":result", 1),
									   (assign, reg3, ":result"),
									   (str_store_string, s14, "str_dplmc_fief_exchange_accept_reg3_denars"),
									(else_try),
									   (str_store_string, s14, "str_dplmc_fief_exchange_accept"),
									(try_end),
								  (try_end),
							  (try_end),
							  (assign, reg0, ":result"),
							]),
							
							  # script_dplmc_time_sorted_heroes_for_center_aux
						  # For internal use only
						  # param 1: center no
						  # param 2: party_no_to_collect_heroes
						  # param 3: minimum time since last met (inclusive), or negative for no restriction
						  # param 4: maximum time since last met (exclusive), or negative for no restriction
						  ("dplmc_time_sorted_heroes_for_center_aux",
							[
							  (store_script_param_1, ":center_no"),
							  (store_script_param_2, ":party_no_to_collect_heroes"),
							  (store_script_param, ":min_time", 3),
							  (store_script_param, ":max_time", 4),

							  (store_current_hours, ":current_hours"),
							  
							  (party_get_num_companion_stacks, ":num_stacks",":center_no"),
							  (try_for_range, ":i_stack", 0, ":num_stacks"),
								(party_stack_get_troop_id, ":stack_troop",":center_no",":i_stack"),
								(troop_is_hero, ":stack_troop"),
								#get time since last talk
								(troop_get_slot, ":troop_last_talk_time", ":stack_troop", slot_troop_last_talk_time),
								(store_sub, ":time_since_last_talk", ":current_hours", ":troop_last_talk_time"),
								#add if time meets constraints
								(this_or_next|ge, ":time_since_last_talk", ":min_time"),
								   (lt, ":min_time", 0),
								(this_or_next|lt, ":time_since_last_talk", ":max_time"),
								   (lt, ":max_time", 0),
								(party_add_members, ":party_no_to_collect_heroes", ":stack_troop", 1),
							  (try_end),
							  (party_get_num_attached_parties, ":num_attached_parties", ":center_no"),
							  (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
								(party_get_attached_party_with_rank, ":attached_party", ":center_no", ":attached_party_rank"),
								(gt, ":attached_party", 0), #Floris - bugfix
								(call_script, "script_dplmc_time_sorted_heroes_for_center_aux", ":attached_party", ":party_no_to_collect_heroes",":min_time",":max_time"),
							  (try_end),
						  ]),

						  # script_dplmc_time_sorted_heroes_for_center
						  # Input: arg1 = center_no, arg2 = party_no_to_collect_heroes
						  # Output: none, adds heroes to the party_no_to_collect_heroes party
						  # The catch is that it returns heroes who haven't been met in a day
						  # or more before others, for greater use in feasts.
						  ("dplmc_time_sorted_heroes_for_center",
							[
							  (store_script_param_1, ":center_no"),
							  (store_script_param_2, ":party_no_to_collect_heroes"),
							  (party_clear, ":party_no_to_collect_heroes"),

							 #Heroes you haven't spoken to in 24+ hours
							 (call_script, "script_dplmc_time_sorted_heroes_for_center_aux",
								 ":center_no", ":party_no_to_collect_heroes", 24, -1),

							 #Heroes you haven't spoken to in 12 to 24 hours
							 (call_script, "script_dplmc_time_sorted_heroes_for_center_aux",
								 ":center_no", ":party_no_to_collect_heroes", 12, 24),

							 #Everyone else
							 (call_script, "script_dplmc_time_sorted_heroes_for_center_aux",
								 ":center_no", ":party_no_to_collect_heroes", -1, 12),

							 #Non-attached pretenders
							 (try_for_range, ":pretender", pretenders_begin, pretenders_end),
								(neq, ":pretender", "$supported_pretender"),
								(troop_slot_eq, ":pretender", slot_troop_cur_center, ":center_no"),
								(party_add_members, ":party_no_to_collect_heroes", ":pretender", 1),
							 (try_end),
						  ]),
                          
						    # script_script_dplmc_faction_leader_splits_gold
						  # INPUT: arg1 = troop_id, arg2 = new faction_no
						  # OUTPUT: none
						  ("dplmc_faction_leader_splits_gold",
							[
							(store_script_param_1, ":faction_no"),
							(store_script_param_2, ":king_gold"),
							(assign, ":push_reg0", reg0),#revert register value at end of script
							(assign, ":push_reg1", reg1),#revert register value at end of script
							
							(faction_get_slot, ":faction_liege", ":faction_no", slot_faction_leader),
							(faction_get_slot, reg0, ":faction_no", dplmc_slot_faction_centralization),
							(val_clamp, reg0, -3, 4),
							(val_mul, reg0, -5),
							(try_begin),		
								(troop_slot_ge, ":faction_liege", slot_troop_wealth, 20000),
								(val_add, reg0, 20),#20% if the king is at or above his starting gold
							(else_try),
								(val_add, reg0, 50),#50% otherwise
							(try_end),
							(val_add, reg0, 50),
							(store_mul, ":lord_gold", ":king_gold", reg0),#king splits other half among lords
							(val_div, ":lord_gold", 100),
							(val_sub, ":king_gold", ":lord_gold"),
							(try_begin),
								#If there's enough gold to give a meaningful amount to everyone, do so.
								#(This accomplishes two things.  It makes the distribution more even, and
								#it prevents this script from taking an unreasonably long time for very
								#large amounts of gold.)
								#
								#"Meaningful" is at least 300, because that's the minimum amount of gold a
								#lord will to to a fief to collect (it is also the AI recruitment cost on
								#hard).
								(assign, ":num_lords", 0),#<-- number of lords in faction, not including faction leader
								(try_for_range, ":lord_no", heroes_begin, heroes_end),
									(store_troop_faction, ":lord_faction_no", ":lord_no"),
									(eq, ":faction_no", ":lord_faction_no"),
									(troop_set_slot, ":lord_no", slot_troop_temp_slot, 0),
									(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
									(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
									(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
									(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
									(ge, ":lord_party", 0),
									(val_add, ":num_lords", 1),
								(try_end),
								(try_begin),
									#handle player
									(eq, "$players_kingdom", ":faction_no"),
									(neq, "trp_player", ":faction_liege"),
									(neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
									(val_add, ":num_lords", 1),
								(try_end),
								(gt, ":num_lords", 0),#<-- can fail
								(store_div, ":gold_to_each", ":lord_gold", ":num_lords"),
								(ge, ":gold_to_each", 300),
								(val_div, ":gold_to_each", 150),#regularize (standard reinforcement costs for easy/medium/hard are 600/450/300, which are multiples of 150)
								(val_mul, ":gold_to_each", 150),
								
								#(try_begin),
								#	(ge, "$cheat_mode", 1),
								#	(assign, reg0, ":num_lords"),
								#	(assign, reg1, ":gold_to_each"),
								#	(str_store_faction_name, s5, ":faction_no"),		
								#	(display_message, "@ {reg0} vassals of the {s5} receive {reg1} denars each (dplmc_faction_leader_splits_gold)"),
								#(try_end),
								
								(try_for_range, ":lord_no", heroes_begin, heroes_end),
									(ge, ":lord_gold", ":gold_to_each"),
									#verify lord is vassal of kingdom
									(store_troop_faction, ":lord_faction_no", ":lord_no"),
									(eq, ":faction_no", ":lord_faction_no"),
									(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
									(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
									(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
									(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
									(ge, ":lord_party", 0),
									#give gold to lord
									(val_sub, ":lord_gold", ":gold_to_each"),
									#(troop_get_slot, reg0, ":lord_no", slot_troop_temp_slot),
									#(val_add, reg0, ":gold_to_each"),
									#(troop_set_slot, ":lord_no", slot_troop_temp_slot, reg0),
									##(call_script, "script_troop_add_gold", ":lord_no", ":gold_to_each"),
									(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", ":gold_to_each", ":lord_no"),
								(try_end),
								(try_begin),
									(ge, ":lord_gold", ":gold_to_each"),
									#give gold to player if player is vassal of kingdom
									(eq, "$players_kingdom", ":faction_no"),
									(neq, "trp_player", ":faction_liege"),
									(neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 0),
									(val_sub, ":lord_gold", ":gold_to_each"),
									(troop_get_slot, reg0, "trp_player", slot_troop_temp_slot),
									(val_add, reg0, ":gold_to_each"),
									(troop_set_slot, "trp_player", slot_troop_temp_slot, reg0),
									##(call_script, "script_troop_add_gold", ":lord_no", ":gold_to_each"),
								(try_end),
							(try_end),
							#Now, distribute the remaining gold.  Assign gold in increments of 300,
							#because that's the minimum amount of gold a lord will go to a fief for
							#(also the AI recruitment cost on hard).
							(store_div, ":count", ":lord_gold", 300),
							(val_max, ":count", 1),
							(try_for_range, ":unused", 0, ":count"),
								(ge, ":lord_gold", 300),
								(call_script, "script_cf_get_random_lord_except_king_with_faction", ":faction_no"),
								(is_between, reg0, heroes_begin, heroes_end),
								(assign, ":troop_no", reg0),
								(val_sub, ":lord_gold", 300),
								(troop_get_slot, reg0, ":troop_no", slot_troop_temp_slot),
								(val_add, reg0, 300),
								(troop_set_slot, ":troop_no", slot_troop_temp_slot, reg0),
								#(call_script, "script_troop_add_gold", ":troop_no", 300),
							(try_end),
							
							#Now the distribution is set.  Give each one his allotment.
							(try_for_range, ":lord_no", heroes_begin, heroes_end),
								(ge, ":lord_gold", ":gold_to_each"),
								#verify lord is vassal of kingdom
								(store_troop_faction, ":lord_faction_no", ":lord_no"),
								(eq, ":faction_no", ":lord_faction_no"),
								(neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
								(troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
								(neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
								(troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
								(ge, ":lord_party", 0),
								#get promised gold
								(troop_get_slot, reg0, ":lord_no", slot_troop_temp_slot),
								(neq, reg0, 0),
								#(try_begin),
								#	(ge, "$cheat_mode", 1),
								#	(str_store_troop_name, s4, ":lord_no"),
								#	(str_store_faction_name, s5, ":faction_no"),
								#	(str_store_troop_name, s6, ":faction_liege"),			
								#	(display_message, "@{!}{s4} of the {s5} receives {reg0} denars (dplmc_faction_leader_splits_gold)"),
								#(try_end),
								(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", reg0, ":lord_no"),
								(troop_set_slot, ":lord_no", slot_troop_temp_slot, 0),
							(try_end),
							
							(val_add, ":king_gold", ":lord_gold"),#Give remaining gold to king
							(try_begin),
								(ge, "$cheat_mode", 1),
								(str_store_troop_name, s4, ":troop_no"),
								(str_store_faction_name, s5, ":faction_no"),
								(str_store_troop_name, s6, ":faction_liege"),			
								(display_message, "@{!}{s6} of the {s5} retains the remaining {reg0} denars (dplmc_faction_leader_splits_gold)"),
							(try_end),
							
							#(call_script, "script_troop_add_gold", ":faction_liege", ":king_gold"),
							(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", ":king_gold", ":faction_liege"),
							(assign, reg0, ":push_reg0"),#revert register value
							(assign, reg1, ":push_reg1"),#revert register value
							]),
							
							  #script_dplmc_lord_return_from_exile
						  # INPUT: arg1 = troop_id, arg2 = new faction_no
						  # OUTPUT: none
						  ("dplmc_lord_return_from_exile",
							[
							  (store_script_param_1, ":troop_no"),
							  (store_script_param_2, ":faction_no"),
							  #Check validity
							  (try_begin),
								  (is_between, ":troop_no", heroes_begin, heroes_end),
								  (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
								  (neq, ":troop_no", "trp_player"),
								  (faction_get_slot, ":faction_liege", ":faction_no", slot_faction_leader),
								  #The lord definitely should not already belong to a kingdom
								  (store_troop_faction, ":old_faction", ":troop_no"),
								  (neg|is_between, ":old_faction", kingdoms_begin, kingdoms_end),
								  (try_begin),
									#Handle separately for adding to the player's faction
									#The player may decide to accept or reject the return
									(this_or_next|eq, ":faction_liege", "trp_player"),
									(eq, ":faction_no", "fac_player_supporters_faction"),
									#(eq, 1, 0),#<-- temporarily disable
									#Lord comes to petition the player instead of automatically returning
									(call_script, "script_change_troop_faction", ":troop_no", ":faction_no"),
									(troop_set_slot, ":troop_no", slot_troop_occupation, slto_inactive),
									#Show event (no log without actual faction change)
									(str_store_troop_name, s4, ":troop_no"),
									(str_store_faction_name, s5, ":faction_no"),
									(str_store_troop_name, s6, ":faction_liege"),
									(display_message, "@{s4} has returned from exile, seeking refuge with {s6} of {s5}."),
									#Remove party
									(troop_get_slot, ":led_party", ":troop_no", slot_troop_leaded_party),
									(try_begin),
										(party_is_active, ":led_party"),
										(neq, ":led_party", "p_main_party"),
										(remove_party, ":led_party"),
										(troop_set_slot, ":troop_no", slot_troop_leaded_party, -1),
									(try_end),
									#
								  (else_try),
									 #NPC king auto-accepts
									 #Normalize relation between NPC and king
									 (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_liege"),
									 (store_sub, ":relation_change", 0, reg0),#enough to increase to 0 if negative
									 (val_max, ":relation_change", 5),
									 (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":faction_liege", ":relation_change"),
									 #Perform reverse of relation change for exile
									 (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end), #all lords in own faction, and relatives regardless of faction
										(assign, ":relation_change", 0),#no change for non-relatives in other factions
										(try_begin),
											(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
											(eq, ":faction_no", ":active_npc_faction"),
											#Auto-exiling someone at -75 relation to his liege gives a -1 base
											#relation penalty from other lords, so the gain is 1 by default.
											(assign, ":relation_change", 1),
										(try_end),
										##(call_script, "script_troop_get_family_relation_to_troop", ":troop_no", ":active_npc"),
										(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_no", ":active_npc"),
										(assign, ":family_relation", reg0),
										(try_begin),
											(gt, ":family_relation", 1),
											(store_div, ":family_modifier", reg0, 3),
											(val_add, ":relation_change", ":family_modifier"),
										(try_end),
										
										(neq, ":relation_change", 0),
										
										(call_script, "script_troop_change_relation_with_troop", ":faction_liege", ":active_npc", ":relation_change"),
										(try_begin),
											(eq, "$cheat_mode", 1),
											(str_store_troop_name, s17, ":active_npc"),
											(str_store_troop_name, s18, ":faction_liege"),
											(assign, reg3, ":relation_change"),
											(display_message, "str_trial_influences_s17s_relation_with_s18_by_reg3"),
										(try_end),
									 (try_end),#end try for range :active_npc
									 
									#Now actually change the faction
									(call_script, "script_change_troop_faction", ":troop_no", ":faction_no"),
									(try_begin), #new-begin
										(neq, ":faction_no", "fac_player_supporters_faction"),
										(this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive),
											(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_retirement),
										(troop_set_slot, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
									(try_end), #new-end
									
									#Log event
									(str_store_troop_name, s4, ":troop_no"),
									(str_store_faction_name, s5, ":faction_no"),
									(str_store_troop_name, s6, ":faction_liege"),
									(display_log_message, "@{s4} has been granted a pardon by {s6} of {s5} and has returned from exile."),

									(troop_get_slot, ":led_party", ":troop_no", slot_troop_leaded_party),
									(try_begin),
										(party_is_active, ":led_party"),
										(neq, ":led_party", "p_main_party"),
										(remove_party, ":led_party"),
										(troop_set_slot, ":troop_no", slot_troop_leaded_party, -1),
									(try_end),
								  (try_end),#end NPC king auto-accepts
							  (else_try),
								#Failure.  Perform string register assignment first to avoid differences
								#between debug and non-debug behavior.
								(str_store_troop_name, s5, ":troop_no"),
								(str_store_faction_name, s7, ":faction_no"),
								#(ge, "$cheat_mode", 1),#<-- always show this
								(display_message, "@{!}DEBUG : failure in dplmc_lord_return_from_exile((s5}, {s7})"),
							  (try_end),
							]),
							
							#script_dplmc_get_troop_morality_value
							# INPUT: arg1 = troop_id, arg2 = morality type
							# OUTPUT: reg0 has morality value, or 0 if inapplicable
							("dplmc_get_troop_morality_value",
							[
								(store_script_param, ":troop_id", 1),
								(store_script_param, ":morality_type", 2),
								
								(assign, reg0, 0),
								(try_begin),
									(neg|is_between, ":troop_id", companions_begin, companions_end),#<-- result is 0 for non-companions
								(else_try),
									(troop_slot_eq, ":troop_id", slot_troop_morality_type, ":morality_type"),
									(troop_get_slot, reg0, ":troop_id", slot_troop_morality_value),
								(else_try),
									(troop_slot_eq, ":troop_id", slot_troop_2ary_morality_type, ":morality_type"),
									(troop_get_slot, reg0, ":troop_id", slot_troop_2ary_morality_value),
								(try_end),
								
							]),
							
							#script_dplmc_print_subordinate_says_sir_madame_to_s0
							#
							#In a number of circumstances a subordinate (a soldier in the player's employ) will refer
							#to him as "sir" or "madame".  This is intended as a sign of respect, but becomes
							#unintentionally disrespectful if the player would ordinarily merit a higher title.
							#
							#This function does not take into account the personal characteristics of the speaker in
							#any way.  That logic should occur elsewhere.        
							#
							#input: none
							#output: reg0 gets a number corresponding to the title used
							("dplmc_print_subordinate_says_sir_madame_to_s0",
								[
								(assign, ":highest_honor", 1),#{sir/madame}
								#1: str_dplmc_sirmadame
								#2: str_dplmc_my_lordlady
								#3: str_dplmc_your_highness
								(try_begin),
									#disable extra honors when the player is not recognized
									(eq, "$sneaked_into_town", 1),
									(assign, ":highest_honor", 1),
								(else_try),
									#initialize variables for following steps
									(troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
									(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
									#check if the player is the spouse of one of a widely recognized monarch,
									#or if the player is the ruler of one of the starting kingdoms (this can't happen but check anyway)
									(ge, ":player_spouse", 1),
									(try_for_range, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
										(this_or_next|faction_slot_eq, ":faction_no", slot_faction_leader, "trp_player"),
										(faction_slot_eq, ":faction_no", slot_faction_leader, ":player_spouse"),
										(val_max, ":highest_honor", 3),
									(try_end),
									(this_or_next|is_between, ":player_spouse", kings_begin, kings_end),
									(this_or_next|is_between, ":player_spouse", pretenders_begin, pretenders_end),
										(ge, ":highest_honor", 3),
									(val_max, ":highest_honor", 3),
									#Do not continue, since you've already used the highest available honor.
								(else_try),
									#the player is head of his own faction
									(ge, "$players_kingdom", 0),
									#faction leader is player, or faction leader is spouse and spouse is valid
									(this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
										(faction_slot_eq, "$players_kingdom", slot_faction_leader, ":player_spouse"),
									(this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
										(ge, ":player_spouse", 1),

									(faction_slot_eq, "$players_kingdom", slot_faction_state, sfs_active),
									(try_begin),
										#If you have sufficient right-to-rule and renown, your subjects
										#will call you "highness".
										(ge, "$player_right_to_rule", 10),
										(store_sub, reg0, 75 + 75, "$player_right_to_rule"),
										(val_mul, reg0, 1200 // 75),#minimum required renown (as an aside, 1200 is evenly divisibly by 75)
										#examples: at right to rule 50, renown must be at least 1600
										#          at right to rule 99, renown must be at least 816
										#          at right to rule 10, renown must be at least 2240
										(ge, ":player_renown", reg0),
										(val_max, ":highest_honor", 3),
									(else_try),
										#"Highness" is also used if the player's kingdom holds meaningful territory.
										(try_begin),
											#Recalculate the cached value if it's suspicious
											(faction_slot_eq, "$players_kingdom", slot_faction_num_castles, 0),
											(faction_slot_eq, "$players_kingdom", slot_faction_num_towns, 0),
											(call_script, "script_faction_recalculate_strength", "$players_kingdom"),
										(else_try),
											#Recalculate the cached value if it's obviously wrong
											(this_or_next|neg|faction_slot_ge, "$players_kingdom", slot_faction_num_castles, 0),
											(neg|faction_slot_ge, "$players_kingdom", slot_faction_num_towns, 0),
											(call_script, "script_faction_recalculate_strength", "$players_kingdom"),
										(try_end),
										#Territory points: castles = 2, towns = 3 (ignore villages)
										(faction_get_slot, ":territory_points", "$players_kingdom", slot_faction_num_towns),
										(val_mul, ":territory_points", 3),
										(faction_get_slot, reg0, "$players_kingdom", slot_faction_num_castles),
										(val_add, ":territory_points", reg0),
										(val_add, ":territory_points", reg0),
										#If the player owns even a single center, that's worth at least "my lord" from his followers
										(ge, ":territory_points", 1),
										(val_max, ":highest_honor", 2),
										#By default there are around 48 castles and 22 towns on the map, for a total of 70
										#centers, and 162 "points" if weighting castles = 2 and towns = 3.
										(store_sub, ":global_points", towns_end, towns_begin),
										(val_mul, ":global_points", 3),
										(store_sub, reg0, castles_end, castles_begin),
										(val_add, ":global_points", reg0),
										(val_add, ":global_points", reg0),
										#By default there are 6 NPC kingdoms, averaging 8 castles and 3.66... towns or
										#27 points each (although the initial distribution of territory is not even).
										(store_sub, ":number_kingdoms", npc_kingdoms_end, npc_kingdoms_begin),
										(val_max,  ":number_kingdoms", 1),
										#Territory must be at least 3/4 the total points divided by number of initial kingdoms.
										#Right to rule applied as a percentage bonus, scaled so that you gain recognition with
										#75% right to rule and a 50% size kingdom.
														
										#What I want is: ( (RtR * 2/3) + 100 ) * territory * kingdoms >= globe * 3/4
										#This is equivalent to: (RtR * 2 + 300) * territory * kingdoms * 4 >= globe * 9
										#The re-ordering is because of rounding.
										(store_mul, ":target_points", ":global_points", 9),
										(store_mul, reg0, "$player_right_to_rule", 2),
										(val_add, reg0, 300),
										(val_mul, reg0, ":territory_points"),
										(val_mul, reg0, ":number_kingdoms"),
										(val_mul, reg0, 4),
										(ge, reg0, ":target_points"),
										(val_max, ":highest_honor", 3),
									(try_end),
									#stop evaluation if you reached highest honor
									(ge, ":highest_honor", 3),
								(else_try),
									#the player is a vassal of one of the initial kingdoms
									(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
									(val_max, ":highest_honor", 1),
									(eq, "$player_has_homage", 1),#<- can fail
									(val_max, ":highest_honor", 2),
								(try_end),

								(try_begin),
								   (ge, ":highest_honor", 3),
								   (str_store_string, s0, "str_dplmc_your_highness"),
								(else_try),
								   (eq, ":highest_honor", 2),
								   (str_store_string, s0, "str_dplmc_my_lordlady"),
								(else_try),
								   (str_store_string, s0, "str_dplmc_sirmadam"),
								(try_end),

								  ##Special cases
								(try_begin),
								   (lt, "$sneaked_into_town", 1),
									 (is_between, "$g_talk_troop", companions_begin, companions_end),
									  (ge, ":highest_honor", 1),
									  (neg|troop_slot_eq, "$g_talk_troop", slot_troop_met, 0),
									  (this_or_next|neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_inactive),
										 (neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, 0),
									 (neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),			  
								   (troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
								   (ge, ":honorific", "str_npc1_honorific"),
									  (str_store_string, s0, ":honorific"),
								  (else_try),
									 (eq, ":highest_honor", 1),
									  (is_between, "$g_talk_troop", heroes_begin, heroes_end),
									  (str_store_string, s0, "str_dplmc_sirmadame"),
								(try_end),

								(assign, reg0, ":highest_honor"),
							]),
							
								#"script_dplmc_print_commoner_at_arg1_says_sir_madame_to_s0"
								#
								#In a number of circumstances a commoner, who might or might not be a subject of
								#the player, will refer to him as "sir" or "madame."  This script determines whether
								#a different title would be warranted.    
								#
								#input: party_no (usually a village or town)
								#output: reg0 gets a number corresponding to the title used
								("dplmc_print_commoner_at_arg1_says_sir_madame_to_s0", [
									(store_script_param_1, ":party_no"),
									
									(assign, ":title_level", 1),
									(str_store_string, s0, "str_dplmc_sirmadam"),
									(store_faction_of_party, ":party_faction"),

									(try_begin),
										(neq, "$sneaked_into_town", 1),#disable extra honors when the player is not recognized
										(ge, ":party_no", 0),
										
										#This is used in various conditions below, so I am calling it once
										#for simplicity.
										(assign, ":save_g_talk_troop", "$g_talk_troop"),
										(assign, ":save_g_encountered_party", "$g_encountered_party"),
										(try_begin),
										  (neq, ":party_no", "$g_encountered_party"),
											(assign, "$g_encountered_party", -1),
										   (assign, "$g_talk_troop", -1),
									 (try_end),
										(call_script, "script_dplmc_print_subordinate_says_sir_madame_to_s0"),
										(assign, ":title_level", reg0),
										(assign, "$g_encountered_party", ":save_g_encountered_party"),
										(assign, "$g_talk_troop", ":save_g_talk_troop"),
										
										(try_begin),
											#The player is a full member of the faction: use full honors
											(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":party_faction"),
											(ge, reg0, DPLMC_FACTION_STANDING_DEPENDENT),
											#(nothing more needs to be done)
										(else_try),
											#the faction has recognized him formally: use full honors
											(this_or_next|eq, ":party_no", "p_main_party"),
											(this_or_next|eq, ":party_faction", "fac_player_supporters_faction"),
											   (faction_slot_ge, ":party_faction", slot_faction_recognized_player, 1),
											#(nothing more needs to be done)
										(else_try),
											#The player is the lord of the town: keep result from script_dplmc_print_subordinate_says_sir_madame_to_s0
											(is_between, ":party_no", centers_begin, centers_end),
											(party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
											#(nothing more needs to be done)	
										(else_try),
											#Subjects of neutral kingdoms will use titles up to "my lord".
											(store_relation, ":relation", "fac_player_supporters_faction", ":party_faction"),
											(ge, ":relation", 0),
											(try_begin),
												(ge, ":title_level", 3),
												(assign, ":title_level", 2),
												(str_store_string, s0, "str_dplmc_my_lordlady"),
											(try_end),
										(else_try),
											#Subjects of kingdoms at war (that do not recognize the player) and all cases not
											#yet mentioned will reduce the "level" of the title awarded to the player by 1, to
											#a minimum of 1.
											(try_begin),
												(ge, ":title_level", 3),
												(assign, ":title_level", 2),
												(str_store_string, s0, "str_dplmc_my_lordlady"),
											(else_try),
												(eq, ":title_level", 2),
												(assign, ":title_level", 1),
											   (str_store_string, s0, "str_dplmc_sirmadam"),
											(try_end),
										(try_end),
									(try_end),

									##Special cases
									(try_begin),
										(neq, ":party_no", "$g_encountered_party"),
									(else_try),
										(lt, "$sneaked_into_town", 1),
										(ge, ":title_level", 1),
										(is_between, "$g_talk_troop", companions_begin, companions_end),
										(neg|troop_slot_eq, "$g_talk_troop", slot_troop_met, 0),
										(this_or_next|neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_inactive),
											(neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, 0),
										(neg|troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),			  
										(troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
										(ge, ":honorific", "str_npc1_honorific"),
										(str_store_string, s0, ":honorific"),
									(else_try),
										(eq, ":title_level", 1),
										(is_between, "$g_talk_troop", heroes_begin, heroes_end),
										(assign, ":title_level", "str_dplmc_sirmadame"),
									(try_end),

									(assign, reg0, ":title_level"),

									##Switch to cultural equivalents
								  #(try_begin),
									#   (eq, ":party_no", "$g_encountered_party"),
									#   (is_between, "$g_talk_troop", heroes_begin, heroes_end),
								   #   (troop_get_slot, ":culture_faction", "$g_talk_troop", slot_troop_original_faction),
									#   (is_between, ":culture_faction", npc_kingdoms_begin, npc_kingdoms_end),
									#(else_try),
									#   (eq, ":party_no", "$g_encountered_party"),
									#   (ge, "$g_talk_troop", soldiers_begin),
									#   (store_faction_of_troop, ":culture_faction", "$g_talk_troop"),
									#	(is_between, ":culture_faction", npc_kingdoms_begin, npc_kingdoms_end),
									#(else_try),
								  #   (is_between, ":party_no", centers_begin, centers_end),
								  #   (party_get_slot, ":culture_faction", ":party_no", slot_center_original_faction),
									#	(is_between, ":culture_faction", npc_kingdoms_begin, npc_kingdoms_end),
									#(else_try),
									#   (assign, ":culture_faction", ":party_faction"),
									#(try_end),
									#(try_begin),
									#   (is_between, "$g_talk_troop", companions_begin, companions_end),#do not switch
									#(else_try),
									#  (eq, ":title_level", 1),
									#	(eq, ":culture_faction", "fac_kingdom_6"),
									#	(str_store_string, s0, "@{!}{sahib/sahiba}"),
									#(try_end),
								]),
						  
						    ##script_cf_dplmc_troop_is_female
						  #
						  #This exists to make it easy to modify this to work with mods that redefine the troop types.
						  #See script_dplmc_store_troop_is_female
						  #
						  #INPUT: arg1: troop_no
						  #OUTPUT: none
						  ("cf_dplmc_troop_is_female",
						  [
							(store_script_param_1, ":troop_no"),
							(assign, ":is_female", 0),
							(ge, ":troop_no", 0),#Undefined behavior when the arguments are invalid.
							(try_begin),
							   (eq, ":troop_no", active_npcs_including_player_begin),
							   (assign, ":troop_no", "trp_player"),
							(try_end),
							(troop_get_type, ":is_female", ":troop_no"),
							#The following will make it so, for example, tf_undead does not appear to be female.
							#Mods where this is relevant will likely want to tweak it, but this will work in at
							#least one that I know of that has non-human lords.
							(eq, ":is_female", tf_female),
						  ]),

						  ##script_dplmc_store_troop_is_female
						  #
						  #This exists to make it easy to modify this to work with mods that redefine the troop types.
						  #
						  #If you change this, remember to also change script_cf_dplmc_troop_is_female and
						  #script_dplmc_store_is_female_troop_1_troop_2
						  #
						  #INPUT: arg1: troop_no
						  #
						  #OUTPUT:
						  #       reg0: 1 is yes, 0 is no
						  ("dplmc_store_troop_is_female",
						  [
							(store_script_param_1, ":troop_no"),
							(try_begin),
							   (eq, ":troop_no", active_npcs_including_player_begin),
							   (assign, ":troop_no", "trp_player"),
							(try_end),
							(troop_get_type, reg0, ":troop_no"),
							(try_begin),
								(neq, reg0, 0),
								(neq, reg0, 1),
								(assign, reg0, 0),#e.g. this would apply to tf_undead
							(try_end),
						  ]),

						  ("dplmc_store_troop_is_female_reg",
						  [
							(store_script_param_1, ":troop_no"),
							(store_script_param_2, ":reg_no"),
							(troop_get_type, ":is_female", ":troop_no"),
							#The following will make it so, for example, tf_undead does not appear to be female.
							#Mods where this is relevant will likely want to tweak it, but this will work in at
							#least one that I know of that has non-human lords.
							(try_begin),
								(neq, ":is_female", 0),
								(neq, ":is_female", 1),
								(assign, ":is_female", 0),
							(try_end),
								##Can asign to registers 0,1,2,3, 65, or 4
							(try_begin),
								  (eq, ":reg_no", 4),
								  (assign, reg4, ":is_female"),
							(else_try),
							  (eq, ":reg_no", 3),
							  (assign, reg3, ":is_female"),
							(else_try),
							  (eq, ":reg_no", 2),
							  (assign, reg2, ":is_female"),
							(else_try),
							  (eq, ":reg_no", 1),
							  (assign, reg1, ":is_female"),
							(else_try),
							  (eq, ":reg_no", 0),
							  (assign, reg0, ":is_female"),
							(else_try),
							  (eq, ":reg_no", 65),
							  (assign, reg65, ":is_female"),
								(else_try),
								  ##default to reg4
								  (assign, reg4, ":reg_no"),
								  (display_message, "@{!} ERROR: called script dplmc-store-troop-is-female-reg with bad argument {reg4}"),
								  (assign, reg4, ":is_female"),
								(try_end),
						  ]),
						  
						  ##script_dplmc_store_is_female_troop_1_troop_2
						  #
						  #This exists to make it easy to modify this to work with mods that redefine the troop types.
						  #See script_dplmc_store_troop_is_female
						  #
						  #INPUT:
						  #      arg1: troop_1
						  #      arg2: troop_2  
						  #OUTPUT:
						  #       reg0: 0 for not female, 1 for female
						  #       reg1: 0 for not female, 1 for female
						  ("dplmc_store_is_female_troop_1_troop_2",
						  [
							(store_script_param_1, ":troop_1"),
							(store_script_param_2, ":troop_2"),
							(troop_get_type, ":is_female_1", ":troop_1"),
							(troop_get_type, ":is_female_2", ":troop_2"),
							#The following will make it so, for example, tf_undead does not appear to be female.
							#Mods where this is relevant will likely want to tweak it, but this will work in at
							#least one that I know of that has non-human lords.
							(try_begin),
								(neq, ":is_female_1", 0),
								(neq, ":is_female_1", 1),
								(assign, ":is_female_1", 0),
							(try_end),
							(try_begin),
								(neq, ":is_female_2", 0),
								(neq, ":is_female_2", 1),
								(assign, ":is_female_2", 0),
							(try_end),
							(assign, reg0, ":is_female_1"),
							(assign, reg1, ":is_female_2"),
						  ]),
							
						  #script_cf_dplmc_evaluate_pretender_proposal
						  # INPUT: arg1 = troop_id for pretender
						  # OUTPUT: reg0 = answer
						  #
						  # Writes reason to s14
						  # May clobber s0, s1
						  #
						  ("cf_dplmc_evaluate_pretender_proposal",
							[
							  (store_script_param_1, ":pretender"),
							  (assign, ":answer", -1),
							  (assign, ":save_reg1", reg1),
							  (assign, ":save_reg65", reg65),
							  (call_script, "script_dplmc_store_troop_is_female", ":pretender"),
							  (assign, reg65, reg0),
							  
							  (str_store_string, s14, "str_ERROR_string"),
							  
							  (is_between, ":pretender", pretenders_begin, pretenders_end),
							  (troop_slot_eq, ":pretender", slot_troop_occupation, slto_kingdom_hero),

							  (store_troop_faction, ":pretender_faction", ":pretender"),
							  (is_between, ":pretender_faction", npc_kingdoms_begin, npc_kingdoms_end),
							  (troop_slot_eq, ":pretender", slot_troop_original_faction, ":pretender_faction"),
							  (faction_slot_eq, ":pretender_faction", slot_faction_leader, ":pretender"),
							  (faction_slot_eq, ":pretender_faction", slot_faction_state, sfs_active),
							  
							  (troop_slot_eq, ":pretender", slot_troop_spouse, -1),
							  (troop_slot_eq, ":pretender", slot_troop_betrothed, -1),
							  
							  (troop_get_slot, ":pretender_renown", ":pretender", slot_troop_renown),
							  (val_max, ":pretender_renown", 1),
							  
							  #There, we've covered the preliminaries: this should be a standard post-rebellion
							  #setup.  Now verify that the player is in a correct state.
							  
							  (eq, "$players_kingdom", ":pretender_faction"),
							  (eq, "$player_has_homage", 1),
							  (troop_slot_eq, "trp_player", slot_troop_spouse, -1),
							  (troop_slot_eq, "trp_player", slot_troop_betrothed, -1),
							  
							  (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
							  (call_script, "script_troop_get_player_relation", ":pretender"),
							  (assign, ":player_relation", reg0),
							  
							  #Find competitors
							  (assign, ":b", -1),
							  (assign, ":b_relation", -101),
							  (assign, ":c", -1),
							  (assign, ":c_renown", -1),
							  
							  (store_add, ":faction_renown", ":pretender_renown", ":player_renown"),
							  (assign, ":faction_lords", 2),#the player and the pretender
							  
							  (troop_set_slot, ":pretender", slot_troop_temp_slot, 0),#clear
							  (troop_set_slot, "trp_player", slot_troop_temp_slot, 0),#clear
							  
							  (try_for_range_backwards, ":competitor", heroes_begin, heroes_end),		 
							 (troop_slot_eq, ":competitor", slot_troop_occupation, slto_kingdom_hero),
								 (store_faction_of_troop, ":competitor_faction", ":competitor"),
								 (eq, ":competitor_faction", ":pretender_faction"),
							 (troop_set_slot, ":competitor", slot_troop_temp_slot, 0),#clear
								 
								 (neq, ":competitor", active_npcs_including_player_begin),
							 (neq, ":competitor", ":pretender"),
								  
								 (call_script, "script_troop_get_relation_with_troop", ":competitor", ":pretender"),
								 (assign, ":competitor_relation", reg0),
								 (troop_get_slot, ":competitor_renown", ":competitor", slot_troop_renown),

							 (val_add, ":faction_renown", ":competitor_renown"),
							 (val_add, ":faction_lords", 1),
								 
							 (try_begin),
								(ge, ":competitor_relation", ":b_relation"),
								(neg|troop_slot_eq, ":competitor", slot_troop_spouse, "trp_player"),
								(neg|troop_slot_eq, "trp_player", slot_troop_spouse, ":competitor"),
								(assign, ":b", ":competitor"),
								(assign, ":b_relation", ":competitor_relation"),
							 (try_end),
							 (try_begin),
								(ge, ":competitor_renown", ":c_renown"),
								(assign, ":c", ":competitor"),
								(assign, ":c_renown", ":competitor_renown"),
							 (try_end),
							  (try_end),
							  
							  (assign, ":pretender_towns", 0),
							  (assign, ":pretender_castles", 0),
							  (assign, ":pretender_villages", 0),
							  
							  (assign, ":player_towns", 0),
							  (assign, ":player_castles", 0),
							  (assign, ":player_villages", 0),
							  
							  (assign, ":faction_towns", 0),
							  (assign, ":faction_castles", 0),
							  (assign, ":faction_villages", 0),
							  
							  (assign, ":original_towns", 0),
							  (assign, ":original_castles", 0),
							  (assign, ":original_villages", 0),
							  
							  #(store_sub, ":global_towns", towns_end, towns_begin),
							  #(store_sub, ":global_castles", castles_end, castles_begin),
							  #(store_sub, ":global_villages", villages_end, villages_begin),
							  
							  (assign, ":highest_score", -1),
							  (assign, ":highest_score_lord", -1),

							  (try_for_range, ":center_no", towns_begin, towns_end),
								(store_faction_of_party, ":center_faction", ":center_no"),
								(try_begin),
									(party_slot_eq, ":center_no", slot_town_lord, ":pretender"),
									(val_add, ":pretender_towns", 1),
									(val_add, ":faction_towns", 1),
								(else_try),
									(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
									(val_add, ":player_towns", 1),
									(val_add, ":faction_towns", 1),
								(else_try),
									(this_or_next|eq, ":center_faction", ":pretender_faction"),
										(eq, ":center_faction", "fac_player_supporters_faction"),
									(val_add, ":faction_towns", 1),
									(party_get_slot, ":town_lord", ":center_no", slot_town_lord),
									(this_or_next|eq, ":town_lord", "trp_player"),
										(is_between, ":town_lord", heroes_begin, heroes_end),
									(troop_get_slot, ":local_temp", ":town_lord", slot_troop_temp_slot),
									(val_add, ":local_temp", 3),
									(troop_set_slot, ":town_lord", slot_troop_temp_slot, ":local_temp"),
									(ge, ":local_temp", ":highest_score"),
									(assign, ":highest_score", ":local_temp"),
									(assign, ":highest_score_lord", ":town_lord"),
								(try_end),
								(try_begin),
									(party_slot_eq, ":center_no", slot_center_original_faction, ":pretender_faction"),
									(val_add, ":original_towns", 1),
								(try_end),
							  (try_end),

							  (try_for_range, ":center_no", castles_begin, castles_end),
								(store_faction_of_party, ":center_faction", ":center_no"),
								(try_begin),
									(party_slot_eq, ":center_no", slot_town_lord, ":pretender"),
									(val_add, ":pretender_castles", 1),
									(val_add, ":faction_castles", 1),
								(else_try),
									(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
									(val_add, ":player_castles", 1),
									(val_add, ":faction_castles", 1),
								(else_try),
									(this_or_next|eq, ":center_faction", ":pretender_faction"),
										(eq, ":center_faction", "fac_player_supporters_faction"),
									(val_add, ":faction_castles", 1),
									(party_get_slot, ":town_lord", ":center_no", slot_town_lord),
									(this_or_next|eq, ":town_lord", "trp_player"),
										(is_between, ":town_lord", heroes_begin, heroes_end),
									(troop_get_slot, ":local_temp", ":town_lord", slot_troop_temp_slot),
									(val_add, ":local_temp", 2),
									(troop_set_slot, ":town_lord", slot_troop_temp_slot, ":local_temp"),
									(ge, ":local_temp", ":highest_score"),
									(assign, ":highest_score", ":local_temp"),
									(assign, ":highest_score_lord", ":town_lord"),
								(try_end),
								(try_begin),
									(party_slot_eq, ":center_no", slot_center_original_faction, ":pretender_faction"),
									(val_add, ":original_castles", 1),
								(try_end),
							  (try_end),
							  
							  (try_for_range, ":center_no", villages_begin, villages_end),
								(store_faction_of_party, ":center_faction", ":center_no"),
								(try_begin),
									(party_slot_eq, ":center_no", slot_town_lord, ":pretender"),
									(val_add, ":pretender_villages", 1),
									(val_add, ":faction_villages", 1),
								(else_try),
									(party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
									(val_add, ":player_villages", 1),
									(val_add, ":faction_villages", 1),
								(else_try),
									(this_or_next|eq, ":center_faction", ":pretender_faction"),
										(eq, ":center_faction", "fac_player_supporters_faction"),
									(val_add, ":faction_villages", 1),
									(party_get_slot, ":town_lord", ":center_no", slot_town_lord),
									(this_or_next|eq, ":town_lord", "trp_player"),
										(is_between, ":town_lord", heroes_begin, heroes_end),
									(troop_get_slot, ":local_temp", ":town_lord", slot_troop_temp_slot),
									(val_add, ":local_temp", 1),
									(troop_set_slot, ":town_lord", slot_troop_temp_slot, ":local_temp"),
									(ge, ":local_temp", ":highest_score"),
									(assign, ":highest_score", ":local_temp"),
									(assign, ":highest_score_lord", ":town_lord"),
								(try_end),
								(try_begin),
									(party_slot_eq, ":center_no", slot_center_original_faction, ":pretender_faction"),
									(val_add, ":original_villages", 1),
								(try_end),
							  (try_end),
							  
							  #Update stats
							  (faction_set_slot, ":pretender_faction", slot_faction_num_castles, ":faction_castles"),
							  (faction_set_slot, ":pretender_faction", slot_faction_num_towns, ":faction_towns"),
							  
							  #Point totals used below
							  #Faction Score A: (4 * towns) + (2 * castles) + villages
							  (store_mul, ":faction_score_a", ":faction_towns", 4),
							  (val_add, ":faction_score_a", ":faction_castles"),
							  (val_add, ":faction_score_a", ":faction_castles"),
							  (val_add, ":faction_score_a", ":faction_villages"),
								  
							  #Faction Score B: (3 * towns) + (2 * castles) + villages
							  (store_sub, ":faction_score_b", ":faction_score_a", ":faction_towns"),

							  #Original Score A: (4 * towns) + (2 * castles) + villages
							  (store_mul, ":original_score_a", ":original_towns", 4),
							  (val_add, ":original_score_a", ":original_castles"),
							  (val_add, ":original_score_a", ":original_castles"),
							  (val_add, ":original_score_a", ":original_villages"),
								  
							  #Original Score B: (3 * towns) + (2 * castles) + villages
							  (store_sub, ":original_score_b", ":faction_score_b", ":faction_towns"),
							  
							  #The first fail-condition encountered will be the explanation used,
							  #so make sure the most pressing ones go first.
							  (try_begin),
								  #relation low: using the same cutoff normally used for becoming a vassal
								  (lt, ":player_relation", 0),
								  (assign, ":answer", -1),
								  (str_store_string, s14, "@Given the way things stand between us at the moment, {playername}, I would not consider it prudent to enter into such an arrangement."),
							  (else_try),
								 #check player right to rule
								 (store_add, ":player_score", "$player_right_to_rule", ":player_relation"),
								 (this_or_next|lt, "$player_right_to_rule", 20),#the level required for your spouse to join a rebellion
									(lt, ":player_score", 100),
								 (assign, ":answer", -1),
								 (str_store_string, s14, "@{playername}, I am grateful to you, but in the eyes of the people you do not have sufficient legitimacy as a potential co-ruler.  Marrying you would undermine my own claim to the throne."),
							  (else_try),
								 #check player renown
								 (store_mul, ":min_score", ":pretender_renown", 2),
								 (val_div, ":min_score", 3),#2/3 pretender renown, 750 by default
								 (val_clamp, ":min_score", 500, 1200),#500 is the minimum to begin the claimant quest; 1200 is the initial value for claimants themselves
								 
								 (lt, ":player_renown", ":min_score"),
								 (assign, ":answer", -1),
								 (try_begin),
									(ge, "$cheat_mode", 1),
									(assign, reg0, ":player_renown"),
									(assign, reg1, ":min_score"),
									(display_message, "@{!}DEBUG - player renown {reg0}, required renown {reg1}"),
								  (try_end),
								 (str_store_string, s14, "@{playername}, I know that if it were not for you I would not sit on this throne, but your name is little renowned in Calradia.  Marrying you would be perceived as an uneven match and would call into question my own claim to the throne."),
							  (else_try),
								  #check player has sufficient fiefs
								  (store_mul, ":player_score", ":player_towns", 3),
								  (val_add, ":player_score", ":player_castles"),
								  (val_add, ":player_score", ":player_castles"),
								  (val_add, ":player_score", ":player_villages"),# player_score = (3 * towns) + (2 * castles) + villages
								  
								  (assign, ":min_score", 6),#A town, a castle, and a village; two towns; three castles; six villages; etc...

								  (try_begin),
									#Ensure the minimum is not unreasonable on small maps.
									(lt, ":original_score_b", 18),
									(lt, ":faction_score_b", 18),
									(assign, reg0, ":original_score_b"),
									(val_max, reg0, ":faction_score_b"),
									(store_div, ":min_score", reg0, 3),
								  (try_end),
								  
								  (troop_get_slot, ":two_thirds_pretender_score", ":pretender", slot_troop_temp_slot),
								  (val_mul, ":two_thirds_pretender_score", 2),
								  (val_add, ":two_thirds_pretender_score", 1),
								  (val_div, ":two_thirds_pretender_score", 3),
								  (val_max, ":min_score", ":two_thirds_pretender_score"),
								  
								  (lt, ":player_score", ":min_score"),
								  (assign, ":answer", -1),
								  (try_begin),
									(ge, "$cheat_mode", 1),
									(assign, reg0, ":player_score"),
									(assign, reg1, ":min_score"),
									(display_message, "@{!}DEBUG - player score {reg0} out of a required {reg1}"),
								  (try_end),
								  (str_store_string, s14, "@{playername}, I am grateful for your assistance in regaining my rightful throne, but you do not have sufficient personal holdings to be a suitable match for me.  It would be an uneven partnership."),
							 (else_try),
								  #does the player have as much renown as competitors?	
								  (lt, ":player_renown", ":c_renown"),
								  (assign, ":answer", -1),
								  (str_store_troop_name, s14, ":c"),
								  (try_begin),
									(ge, "$cheat_mode", 1),
									(assign, reg0, ":player_renown"),
									(assign, reg1, ":c_renown"),
									(display_message, "@{!}DEBUG - player score {reg0}, competitor score {reg1}"),
								  (try_end),
								  (str_store_string_reg, s0, s15),#clobber s0, save s15
								  (call_script, "script_troop_describes_troop_to_s15", ":pretender", ":c"),
								  (str_store_string, s14, "@{playername}, I am grateful to you, but if I were to accept at this time I would risk offending powerful lords such as {s15}, who may consider themselves to have honor equal to or greater than your own."),
								  (str_store_string_reg, s15, s0),#revert s15
							 (else_try),
								  #is the player outfieffed by a competitor?
								  (gt, ":highest_score_lord", "trp_player"),
								  (neq, ":highest_score_lord", ":pretender"),

								  (store_mul, ":player_score", ":player_towns", 3),
								  (val_add, ":player_score", ":player_castles"),
								  (val_add, ":player_score", ":player_castles"),
								  (val_add, ":player_score", ":player_villages"),# player_score = (3 * towns) + (2 * castles) + villages
									 (lt, ":player_score", ":highest_score"),
								  
								  (store_mul, reg0, ":highest_score", 3),#allow small differences
								  (val_add, reg0, 2),
								  (val_div, reg0, 4),
								  (gt, reg0, ":player_score"),

								 (assign, ":answer", -1),
								  (str_store_troop_name, s14, ":highest_score_lord"),
								  (try_begin),
									(ge, "$cheat_mode", 1),
									(assign, reg0, ":player_score"),
									(assign, reg1, ":highest_score"),
									(display_message, "@{!}DEBUG - player score {reg0}, competitor score {reg1}"),
								  (try_end),
								  (str_store_string_reg, s0, s15),#clobber s0, save s15
								  (call_script, "script_troop_describes_troop_to_s15", ":pretender", ":highest_score_lord"),
								  (str_store_string, s14, "@{playername}, I am grateful to you, but if I were to accept at this time I would risk offending great lords such as {s15}, who may consider themselves to have honor equal to or greater than your own."),
								  (str_store_string_reg, s15, s0),#revert s15
							  (else_try),
								  #does the player have as much relation as competitors?		  
								  (lt, ":player_relation", ":b_relation"),
								  (ge, ":b_relation", 5),
								  (assign, ":answer", -1),
								 (try_begin),
									(ge, "$cheat_mode", 1),
									(assign, reg0, ":player_relation"),
									(assign, reg1, ":b_relation"),
									(display_message, "@{!}DEBUG - player relation {reg0}, rival relation {reg1}"),
								  (try_end),
								  (str_store_string_reg, s0, s15),#clobber s0, save s15
								  (call_script, "script_troop_describes_troop_to_s15", ":pretender", ":b"),
								  (str_store_string, s14, "@{playername}, while I am grateful to you, I must confess I am fond of {s15}."),
								  (str_store_string_reg, s15, s0),#revert s15
							  (else_try),
								  #check: sufficient lords?
								  (assign, ":needed_lords", 1),
								  (try_for_range, ":troop_no", lords_begin, lords_end),
									(troop_slot_eq, ":troop_no", slot_troop_original_faction, ":pretender_faction"),
									(val_add, ":needed_lords", 1),
								  (try_end),
								  #Must be at least 75% of original size
								  (val_mul, ":needed_lords", 3),
								  (val_div, ":needed_lords", 4),

								  (lt, ":faction_lords", ":needed_lords"),
								  (assign, ":answer", -1),
								  (try_begin),
									(ge, "$cheat_mode", 1),
									(assign, reg0, ":faction_lords"),
									(assign, reg1, ":needed_lords"),
									(display_message, "@{!}DEBUG - lords in faction {reg0}, required lords {reg1}"),
								  (try_end),
								  
								  (str_store_string, s14, "@Our realm has too few vassals.  In the current precarious state of the affairs I must use the lure of a potential political alliance to attract new vassals, and cannot yet be seen to commit to any single {reg65?suitor:candidate}."),
							  (else_try),
								  #check: pretender has enough fiefs?
								  #Must not be exceeded in fiefs by anyone in the faction.
								  (store_mul, ":pretender_score", ":pretender_towns", 3),
								  (val_add, ":pretender_score", ":pretender_castles"),
								  (val_add, ":pretender_score", ":pretender_castles"),
								  (val_add, ":pretender_score", ":pretender_villages"),
								  (troop_set_slot, ":pretender", slot_troop_temp_slot, ":pretender_score"),
								  
								  (store_mul, reg0, ":highest_score", 3),#allow small differences
								  (val_add, reg0, 2),
								  (val_div, reg0, 4),

								  (gt, reg0, ":pretender_score"),
								  
								  (assign, ":answer", -1),
								  (try_begin),
									(ge, "$cheat_mode", 1),
									(assign, reg1, reg0),
									(assign, reg0, ":pretender_score"),
									(display_message, "@{!}DEBUG - liege has {reg0} center points, needs at least {reg1}"),
								  (try_end),
								  (str_store_string_reg, s0, s15),#clobber s0, save s15
								  (call_script, "script_troop_describes_troop_to_s15", ":pretender", ":highest_score_lord"),
								  (str_store_string, s14, "@Because I have insufficient personal holdings compared to {s15}, if I entered into such an arrangement I would risk appearing to be a puppet, throwing the stability of the realm into jeopardy."),
								  (str_store_string_reg, s15, s0),#revert s15
							 (else_try),
								  #Check if pretender has enough fiefs, part 2.
								  #Must not have fewer fief points than the number of faction points divided by the
								  #number of lords (so this condition can't be bypassed by just failing to assign
								  #centers to anyone during the rebellion)
								  (store_mul, ":points_per_lord", ":faction_towns", 3),
								  (val_add, ":points_per_lord", ":faction_castles"),
								  (val_add, ":points_per_lord", ":faction_castles"),
								  (val_add, ":points_per_lord", ":faction_villages"),
								  (val_div, ":points_per_lord", ":faction_lords"),#includes pretender so cannot be zero
								  
								  (gt, ":points_per_lord", ":pretender_score"),
								  
								  (assign, ":answer", -1),
								  (try_begin),
									(ge, "$cheat_mode", 1),
									(assign, reg0, ":pretender_score"),
									(assign, reg1, ":points_per_lord"),
									(display_message, "@{!}DEBUG - liege has {reg0} center points, needs at least {reg1}"),
								  (try_end),
								  (str_store_faction_name, s14, ":pretender_faction"),
								  (str_store_string, s14, "@Because my personal holdings are insufficiently large compared to other lords of the {s14}, if I entered into such an arrangement I would risk appearing to be a puppet, throwing the stability of the realm into jeopardy."),
							  (else_try),
								  #check if player is widely hated in faction
								  (assign, ":total_negative", 0),
								  (assign, ":total_enemies", 0),
								  (assign, ":total_positive", 0),
								  (assign, ":total_friends", 0),
								  (try_for_range, ":troop_no", heroes_begin, heroes_end),
									 (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
									 (store_troop_faction, reg0, ":troop_no"),
									 (eq, reg0, ":pretender_faction"),
									 (call_script, "script_troop_get_player_relation", ":troop_no"),
									 (try_begin),
										(lt, reg0, 0),
										(val_add, ":total_negative", 1),
										(lt, reg0, -19),
										(val_add, ":total_enemies", 1),
									 (else_try),
										(gt, reg0, 0),
										(val_add, ":total_positive", 1),
										(gt, reg0, 19),
										(val_add, ":total_friends", 1),
									 (try_end),
								  (try_end),
								  #Must not have a "disapproval rating" of over 33%
								  (val_mul, ":total_enemies", 2),
								  (val_mul, ":total_negative", 2),
								  (this_or_next|gt, ":total_enemies", ":total_friends"),
									 (gt, ":total_negative", ":total_positive"),
								  
								  (assign, ":answer", -1),
								  (str_store_faction_name, s14, ":pretender_faction"),
								  (str_store_string, s14, "@I am grateful to you, {playername}, but you have too many enemies among the lords of the {s14} for your proposal to be politically viable.  If I were to accept, there might be a revolt."),
							  (else_try),
								  #controversy must be less than 25, and less than half the relation with the liege
								  (troop_get_slot, ":controversy_2", "trp_player", slot_troop_controversy),
								  (ge, ":controversy_2", 1),
								  (val_mul, ":controversy_2", 2),
								  (this_or_next|ge, ":controversy_2", 50),
									 (ge, ":controversy_2", ":player_relation"),
								  (assign, ":answer", -1),
								  (str_store_faction_name, s14, ":pretender_faction"),
								  (str_store_string, s14, "@You have engendered too much controversy recently, {playername} .  If I were to accept at this time, there might be a revolt among the lords of the {s14}.  Let us speak of this later when the furor has died down."),
							  (else_try),
								  #check is marshall
								  (neg|faction_slot_eq, ":pretender_faction", slot_faction_marshall, "trp_player"),
								  (assign, ":answer", -2),#<-- negative two, not -1
								  (str_store_faction_name, s14, ":pretender_faction"),
								  (str_store_string, s14, "@If you desire to lead the {s14} alongside me, gather support among my vassals to become marshall, and demonstrate to them your abilities as a war leader."),
							  (else_try),
								  #player is marshall: is the territory sufficient?

								  #The faction must have at least 80% of its former territory under scoring system A or scoring system B.
								  (store_mul, ":four_fifths_original_score_a", ":original_score_a", 4),
								  (val_div, ":four_fifths_original_score_a", 5),
								  
								  (store_mul, ":four_fifths_original_score_b", ":original_score_b", 4),
								  (val_div, ":four_fifths_original_score_b", 5),
								  
								  (lt, ":faction_score_a", ":four_fifths_original_score_a"),
								  (lt, ":faction_score_b", ":four_fifths_original_score_b"),
								  (assign, ":answer", -3),
								  
								  (call_script, "script_dplmc_print_centers_in_numbers_to_s0", ":original_towns", ":original_castles", ":original_villages"),
								  (str_store_string_reg, s1, s0),
								  (call_script, "script_dplmc_print_centers_in_numbers_to_s0", ":faction_towns", ":faction_castles", ":faction_villages"),
								  
								  (str_store_faction_name, s14, ":pretender_faction"),
								  (str_store_string, s14, "@Our realm has lost too much territory.  We once held {s1} but now only hold {s0}.  In the current precarious state of affairs I must retain the possibility of a political alliance to use as a bargaining chip with the other sovereigns, so I yet be seen to commit to any single {reg65?suitor:candidate}.  Restore the {s14} to its former glory, and I will gladly have you rule beside me as my {husband/wife}."),
							  (else_try),
								 #player is marshall: are any native centers lost?
								 
								 (str_clear, s0),
								 (str_clear, s1),
								 (assign, ":num_lost_towns_and_castles", 0),
								 
								 (try_for_range, ":center_no", centers_begin, centers_end),
									(party_slot_eq, ":center_no", slot_center_original_faction, ":pretender_faction"),
									(store_faction_of_party, ":center_faction", ":center_no"),
									(neq, ":center_faction", ":pretender_faction"),
									(neq, ":center_faction", "fac_player_supporters_faction"),
									(try_begin),
										(eq, ":num_lost_towns_and_castles", 0),
										(str_store_party_name, s0, ":center_no"),
									(else_try),
										(eq, ":num_lost_towns_and_castles", 1),
										(str_store_party_name, s1, ":center_no"),
									(else_try),
										(str_store_string, s0, "str_dplmc_s0_comma_s1"),
										(str_store_party_name, s1, ":center_no"),
									(try_end),
									(val_add, ":num_lost_towns_and_castles", 1),
								 (try_end),
								 #post-loop cleanup
								 (try_begin),
									(ge, ":num_lost_towns_and_castles", 2),
									(str_store_string, s0, "str_dplmc_s0_and_s1"),
								 (try_end),
								 #native towns lost
								 (ge, ":num_lost_towns_and_castles", 1),
								 (store_sub, reg0, ":num_lost_towns_and_castles", 1),
								 (str_store_faction_name, s14, ":pretender_faction"),
								 (str_store_string, s14, "@{s0} {reg0?have:has} been lost to foreign hands.  Restore the {s14} to its rightful boundaries, and I will gladly have you rule beside me as my {husband/wife}."),
								 (assign, ":answer", -3),
							  (else_try),
							  #Timer answer
								 (lt, "$g_player_days_as_marshal", 14),
								  (assign, reg0, "$g_player_days_as_marshal"),
								  (store_sub, reg1, reg0, 1),
								  (str_store_faction_name, s14, ":pretender_faction"),
								  (str_store_string, s14, "@You have only been marshall for {reg0} {reg1?days:day}.  Let us speak of this after you have held the post for at least two weeks."),
								  (assign, ":answer", -4),
							  (else_try),
								#In the future we may need a proper quest of some kind, or at least a timer, but this will do for now.
								(assign, ":answer", 1),
								(str_store_faction_name, s14, ":pretender_faction"),
								(str_store_string, s14, "@If not for you I would not sit on this throne, {playername}.  When we started our long walk, few people had the courage to support me.  And fewer still would be willing to put their lives at risk for my cause.  But you didn't hesitate for a moment in throwing yourself at my enemies. We have gone through a lot together, and with God's help, we prevailed.  I will gladly accept you as both my {husband/wife} and co-ruler of the {s14}."),
							  (try_end),
							  
							  (assign, reg65, ":save_reg65"),
							  (assign, reg1, ":save_reg1"),
							  (assign, reg0, ":answer"),
						  ]),
						  
						    #script_dplmc_center_point_calc
						  # INPUT: arg1 = faction_id
						  #        arg2 = troop_1
						  #        arg2 = troop_2
						  #        arg3 = town_point_value (see explanation below)
						  #
						  # OUTPUT:
						  #        reg0 = total renown / total faction points (or 0 if no centers held)
						  #        reg1 = troop_1 total (not divided)
						  #        reg2 = troop_2 total (not divided)
						  #        reg3 = faction average lord renown (or 0 if no lords)
						  #
						  #In various places the game tallies center points differently.  The values of
						  #villages/castles/fiefs, respectively, in some places are 1/2/2, in other
						  #places are 1/2/3, and in others are 1/3/4.
						  #Specifying the town point value determines which scheme will be used to
						  #determine ceter points:
						  #        arg3 = 2 gives 1/2/2
						  #        arg3 = 3 gives 1/2/3
						  #        arg3 = 4 gives 1/2/4
						  #
						  #If the specified town_point_value is not 2,3, or 4, the script is allowed to
						  #clamp the value or substitute a default.
						  ("dplmc_center_point_calc",
							[
								(store_script_param, ":faction_id", 1),
								(store_script_param, ":troop_1", 2),
								(store_script_param, ":troop_2", 3),
								(store_script_param, ":town_point_value", 4),
								
								(val_clamp, ":town_point_value", 2, 5),
								
								#The outputs
								(assign, ":faction_score", 0),
								(assign, ":troop_1_score", 0),
								(assign, ":troop_2_score", 0),
								#(assign, ":average_renown", 0),
								
								#Intermediate values we use for computing outputs
								(assign, ":total_renown", 0),
								(assign, ":num_lords", 0),
								
								#Handle the player first
								#(assign, ":player_in_faction", 0),
								(assign, ":faction_alias", ":faction_id"),
								(try_begin),
									(this_or_next|eq, ":faction_id", "$players_kingdom"),
										(eq, ":faction_id", "fac_player_supporters_faction"),
									(val_add, ":num_lords", 1),
									(troop_get_slot, ":total_renown", "trp_player", slot_troop_renown),
									#(assign, ":player_in_faction", 1),
									(assign, ":faction_alias", "fac_player_supporters_faction"),
									(eq, ":faction_id", "fac_player_supporters_faction"),
									(assign, ":faction_alias", "$players_kingdom"),
								(try_end),
								
								#Get lords in faction
								(try_for_range, ":troop_no", heroes_begin, heroes_end),
									(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
									(neq, ":troop_no", "trp_kingdom_heroes_including_player_begin"),
									(store_troop_faction, ":faction_no", ":troop_no"),
									(this_or_next|eq, ":faction_no", ":faction_id"),
										(eq, ":faction_no", ":faction_alias"),
									
									(val_add, ":num_lords", 1),
									(troop_get_slot, ":renown", ":troop_no", slot_troop_renown),
									(val_max, ":renown", 0),
									(val_add, ":total_renown", ":renown"),
								(try_end),
								
								#Get stats for centers
								(try_for_parties, ":center_no"),
									(assign, ":points", 0),
									(try_begin),
										#Towns are 2, 3, or 4 points
										(this_or_next|is_between, ":center_no", towns_begin, towns_end),
										(party_slot_eq, ":center_no", slot_party_type, spt_town),
										(assign, ":points", ":town_point_value"),
									(else_try),
										#Castles are always 2 points
										(this_or_next|is_between, ":center_no", castles_begin, castles_end),
										(party_slot_eq, ":center_no", slot_party_type, spt_castle),
										(assign, ":points", 2),#castles are always 2
									(else_try),
										#Villages are always 1 point
										(this_or_next|is_between, ":center_no", villages_begin, villages_end),
										(party_slot_eq, ":center_no", slot_party_type, spt_village),
									(try_end),
									
									#Don't process parties that aren't centers.
									(ge, ":points", 1),
								
									#NB: We don't know for sure that troop_1 and troop_2 aren't the
									#same value, and we don't even necessarily know that they're part
									#of the specified faction.
									(try_begin),
										(party_slot_eq, ":center_no", slot_town_lord, ":troop_1"),
										(val_add, ":troop_1_score", ":points"),
									(try_end),
									
									(try_begin),
										(party_slot_eq, ":center_no", slot_town_lord, ":troop_2"),
										(val_add, ":troop_2_score", ":points"),
									(try_end),
									
									(store_faction_of_party, ":faction_no", ":center_no"),
									(this_or_next|eq, ":faction_no", ":faction_id"),
										(eq, ":faction_no", ":faction_alias"),
									(val_add, ":faction_score", ":points"),
								(try_end),
								
								# OUTPUT:
								#        reg0 = faction renown / faction points (or 0 if faction has no centers)
								#        reg1 = troop_1 total (not divided)
								#        reg2 = troop_2 total (not divided)
								#        reg3 = faction average lord renown (or 0 if no lords)
								(assign, reg0, 0),
								(try_begin),
									(neq, ":faction_score", 0),
									(store_div, reg0, ":total_renown", ":faction_score"),
								(try_end),
								(assign, reg1, ":troop_1_score"),
								(assign, reg2, ":troop_2_score"),
								(assign, reg3, 0),
								(try_begin),
									(neq, ":num_lords", 0),
									(store_div, reg0, ":total_renown", ":num_lords"),
								(try_end),
							]),
							
							
						  #script_dplmc_good_produced_at_center_or_its_villages
						  # For towns, also includes the villages that attach to it
						  #
						  # INPUT: arg1 = good_no
						  #        arg2 = center_no
						  # OUTPUT:
						  #        reg0 = 0 if no, 1 if yes
						  ("dplmc_good_produced_at_center_or_its_villages",
						  [
							(store_script_param, ":good_no", 1),
							(store_script_param, ":center_no", 2),
							
							(assign, ":has_good", 0),
							(assign, ":save_reg1", reg1),
							(assign, ":save_reg2", reg2),
							(store_current_hours, ":cur_hours"),
							(store_sub, ":recent_time", ":cur_hours", 3 * 24),

							
							(try_begin),
								(is_between, ":good_no", trade_goods_begin, trade_goods_end),
								(ge, ":center_no", 1),
								(this_or_next|is_between, ":center_no", centers_begin, centers_end),
									(party_is_active, ":center_no"),
								(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
								(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_castle),
								(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_village),
									(is_between, ":center_no", centers_begin, centers_end),
								(call_script, "script_center_get_production", ":good_no", ":center_no"),
								(try_begin),
									#Positive production
									(ge, reg0, 1),
									(assign, ":has_good", 1),
								(else_try),
									#Is a town or a castle, and one of its villages has positive prodution
									(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
										(party_slot_eq, ":center_no", slot_party_type, spt_castle),
									(try_for_range, ":cur_village", villages_begin, villages_end),
										(eq, ":has_good", 0),
										#is bound to center
										(this_or_next|party_slot_eq, ":cur_village", slot_village_market_town, ":center_no"),
											(party_slot_eq, ":cur_village", slot_village_bound_center, ":center_no"),#for castles
									   (assign, reg0, 0),
									   (try_begin),
										  #If a trading party from the village reached the town recently, its goods are
										  #available.
										  (party_slot_ge, ":cur_village", dplmc_slot_village_trade_last_arrived_to_market, ":recent_time"),
										  (assign, reg0, 1),
									   (else_try),
										  #If the village is not looted and this center is not under siege, the
										  #goods from the village could be acquired if they were needed.
											   (neg|party_slot_eq, ":cur_village", slot_village_state, svs_looted),
											   (neg|party_slot_eq, ":cur_village", slot_village_state, svs_deserted),
										  (neg|party_slot_eq, ":center_no", slot_village_state, svs_under_siege),
										  (assign, reg0, 1),
									   (try_end),
									   (eq, reg0, 1),
										#If an eligible village has positive production, set "has_good" to true.
										(call_script, "script_center_get_production", ":good_no", ":cur_village"),
										(ge, reg0, 1),
										(assign, ":has_good", 1),
									(try_end),
								(try_end),
							(try_end),
							
							(assign, reg0, ":has_good"),
							(assign, reg1, ":save_reg1"),
							(assign, reg2, ":save_reg2"),
						  ]),

						  #script_dplmc_assess_ability_to_purchase_good_from_center
						  # INPUT: arg1 = good_no
						  #        arg2 = center_no
						  # OUTPUT:
						  #        reg0 = actual price (may be theoretical if unavailable)
						  #        reg1 = 1 if available, 0 if unavailable
						  ("dplmc_assess_ability_to_purchase_good_from_center",
							[
								(store_script_param, ":good_no", 1),
								(store_script_param, ":center_no", 2),
								
								#This is still quite experimental.  This is a work in progress
										#rather than a finished formula.
								(assign, ":price_factor", average_price_factor),
								(assign, ":has_good", 0),
								
								(try_begin),
									(is_between, ":center_no", centers_begin, centers_end),			
									(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_village),
										(party_slot_eq, ":center_no", slot_party_type, spt_town),
									
									(is_between, ":good_no", trade_goods_begin, trade_goods_end),
									
									(store_sub, ":item_slot_no", ":good_no", trade_goods_begin),
									(val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
									(party_get_slot, ":price_factor", ":center_no", ":item_slot_no"),
									
									(call_script, "script_dplmc_good_produced_at_center_or_its_villages", ":good_no", ":center_no"),
									(assign, ":has_good", reg0),
									#abort if good is found
									(lt, ":has_good", 1),
									
									(store_faction_of_party, ":center_faction", ":center_no"),
									(faction_get_slot, ":mercantilism", ":center_faction", dplmc_slot_faction_mercantilism),
									(val_clamp, ":mercantilism", -3, 4),
									
									#For towns, check trade centers.
									(this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
										(is_between, ":center_no", towns_begin, towns_end),
														
									(store_current_hours, ":cur_hours"),
									(assign, ":best_foreign_price", maximum_price_factor),
								 (assign, ":worst_price_seen", ":price_factor"),
									
									(try_for_range, ":trade_town_index", slot_town_trade_routes_begin, slot_town_trade_routes_end),
										(party_get_slot, ":trade_town", ":center_no", ":trade_town_index"),
									(is_between, ":trade_town", centers_begin, centers_end),
										
										(party_get_slot, ":price_factor_2", ":trade_town", ":item_slot_no"),
										(val_max, ":worst_price_seen", ":price_factor_2"),
										
									(party_slot_eq, ":trade_town", slot_party_type, spt_town),
										(call_script, "script_dplmc_good_produced_at_center_or_its_villages", ":good_no", ":trade_town"),
										#The town has or produces the item
										(ge, reg0, 1),
										
										#Get the number of hours since the last caravan arrival, and set the penalty accordingly.
										(assign, ":hours_since", 0),
										#The slot storing the arrival time.  This may be uninitialized for old saved games used
										#with this mod.
										(store_sub, ":arrival_slot", ":trade_town_index", slot_town_trade_routes_begin),
										(val_add, ":arrival_slot", dplmc_slot_town_trade_route_last_arrivals_begin),
										(try_begin),
											#This condition can only occur if the number of trade route slots was increased
											#but the number of trade arrival time slots was not.  Check just in case, to avoid
											#strange errors.
											(neg|is_between, ":arrival_slot", dplmc_slot_town_trade_route_last_arrivals_begin, dplmc_slot_town_trade_route_last_arrivals_end),
											#Set "hours-since" to one week.
											(assign, ":hours_since", 7 * 24),
										(else_try),
											#If the slot is uninitialized, give it a random plausible value.
											(party_slot_eq, ":center_no", ":arrival_slot", 0),#Uninitialzed memory!
											(store_random_in_range, ":hours_since", 1, (24 * 7 * 5) + 1),#random time in last five weeks
											(party_get_slot, ":prosperity_factor", ":center_no", slot_town_prosperity),
											(val_clamp, ":prosperity_factor", 0, 101),
											(val_add, ":prosperity_factor", 75),
											(val_mul, ":hours_since", 125),
											(val_div, ":hours_since", ":prosperity_factor"),#last arrival some time in the last five weeks, plus or minus up to 40% based on prosperity
											(store_sub, ":last_arrival", ":cur_hours", ":hours_since"),
											(party_set_slot, ":center_no", ":arrival_slot", ":last_arrival"),
										(else_try),
											(party_get_slot, ":last_arrival", ":center_no", ":arrival_slot"),
											(store_sub, ":hours_since", ":cur_hours", ":last_arrival"),
											(val_max, ":hours_since", 0),
										(try_end),
										
										
										#Base penalty is 5%.  It stays at a flat 5% for the first week, then begins rising
										#at a rate of 5% per week afterwards (incremented continuously).
										#Clamp the maximum penalty at 50%.
										(store_mul, ":penalty", ":hours_since", 5),
										(val_add, ":penalty", (24 * 7) // 2),
										(val_div, ":penalty", 24 * 7),
										(val_max, ":penalty", 5),#required for the first week
										(val_min, ":penalty", 50),#don't increase above 50%
										
										#Apply mercantilism
										(store_faction_of_party, ":other_faction", ":trade_town"),
										(try_begin),
											#Decrease penalty for mercantilism, increase for free trade
											(eq, ":other_faction", ":center_faction"),
											(val_sub, ":penalty", ":mercantilism"),
										(else_try),
											#Increase penalty for mercantilism, decrease for free trade
											(val_add, ":penalty", ":mercantilism"),
										(try_end),
										
										(try_begin),
											(ge, ":price_factor_2", average_price_factor),
											(val_mul, ":price_factor_2", ":penalty"),
											(val_add, ":price_factor_2", 50),
											(val_div, ":price_factor_2", 100),
										(else_try),
											(store_add, reg0, 100, ":penalty"),
											(val_mul, reg0, average_price_factor),
											(val_add, reg0, 50),
											(val_div, reg0, 100),
											(val_add, ":price_factor_2", reg0),
										(try_end),
										#Make use of the source
										(assign, ":has_good", 1),
										(val_min, ":best_foreign_price", ":price_factor_2"),
									(try_end),
									(try_begin),
									   (ge, ":has_good", 1),
										(val_max, ":price_factor", ":best_foreign_price"),
									(else_try),
									  #Make it so that lack of supply will not make the price lower
									   (lt, ":has_good", 1),
									   (val_max, ":price_factor", ":worst_price_seen"),
									(try_end),
								(try_end),
								
								(try_begin),
									(lt, ":has_good", 1),
									(val_max, ":price_factor", average_price_factor),#don't give bargains if there is no supply
									(val_mul, ":price_factor", 8),#sixty percent penalty
									(val_div, ":price_factor", 5),
								(try_end),
								
								#Apply constraints at the last step
								(val_clamp, ":price_factor", minimum_price_factor, maximum_price_factor),
								
								(assign, reg0, ":price_factor"),
								(assign, reg1, ":has_good"),
							]),
						  
						  	# script_dplmc_get_faction_truce_length_with_faction
							# INPUT
							#   arg1:  faction_1
							#   arg2:  faction_2
							# OUTPUT
							#   reg0:  The length in days of faction_1's truce with faction_2, if any.
							#          If no truce exists, the appropriate value to return is zero.
							("dplmc_get_faction_truce_length_with_faction",
							   [
								(store_script_param, ":faction_1", 1),
								(store_script_param, ":faction_2", 2),
								
								(assign, ":truce_length", 0),
								
								(try_begin),
									(is_between, ":faction_1", kingdoms_begin, kingdoms_end),
									(is_between, ":faction_2", kingdoms_begin, kingdoms_end),
									(neq, ":faction_1", ":faction_2"),
									(store_add, ":truce_slot", ":faction_2", slot_faction_truce_days_with_factions_begin),
									(val_sub, ":truce_slot", kingdoms_begin),
									(faction_get_slot, ":truce_length", ":faction_1", ":truce_slot"),
								(try_end),
								(assign, reg0, ":truce_length"),
							   ]),

						  #script_dplmc_get_terrain_code_for_battle
						  #
						  # Gets the terrain code for a battle between two parties, which
						  # is usually a value like rt_desert, but can instead be two
						  # special values: -1 for 
						  #
						  # INPUT: arg1 = attacker_party
						  #        arg2 = defender_party
						  # OUTPUT: reg0 = terrain code (-1 for invalid, -2 for siege)
						  ("dplmc_get_terrain_code_for_battle",
						   [
							  (store_script_param, ":attacker_party", 1),
							  (store_script_param, ":defender_party", 2),

							  (assign, reg0, dplmc_terrain_code_unknown), #Terrain code, defined in header_terrain_types.py
							  
							  (try_begin),
								#Check for village missions
								 (this_or_next|eq, ":attacker_party", "p_main_party"),
									(eq, ":defender_party", "p_main_party"),
								 (ge, "$g_encounter_is_in_village", 1),
								 (assign, reg0, dplmc_terrain_code_village),#defined in header_terrain_types.py
							  (else_try),
								#If the attacker party is a town, a castle, a village, a bandit lair, or a ship,
								#set the terrain code to "none" since we don't have any specific ideas for modifying
								#the unit-type performance in scenarios of that type (whatever they are).
								 (ge, ":attacker_party", 0),
								 (this_or_next|party_slot_eq, ":attacker_party", slot_party_type, spt_town),#no modifier for being attacked by garrisoned troops
								 (this_or_next|party_slot_eq, ":attacker_party", slot_party_type, spt_castle),
								 (this_or_next|party_slot_eq, ":attacker_party", slot_party_type, spt_village),
								 (this_or_next|party_slot_eq, ":attacker_party", slot_party_type, spt_bandit_lair),
									(party_slot_eq, ":attacker_party", slot_party_type, spt_ship),#no modifier for being attacked by a ship
								 (assign, reg0, dplmc_terrain_code_unknown),#no terrain options, defined in header_terrain_types.py
							  (else_try),
								#If the attacker party is *attached* to a town/castle/village, a bandit lair, or a ship,
								#set the terrain code to "none" since we don't have any specific ideas for modifying
								#the unit-type performance in scenarios of that type (whatever they are).
								 (ge, ":attacker_party", 0),
								 (party_get_attached_to, ":attachment", ":attacker_party"),
								 (ge, ":attachment", 0),
								 (party_is_active, ":attachment"),
								 (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_town),#no modifier for being attacked by garrisoned troops
								 (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_castle),
								 (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_village),
								 (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_bandit_lair),
									(party_slot_eq, ":attachment", slot_party_type, spt_ship),#no modifier for being attacked by a ship
								 (assign, reg0, dplmc_terrain_code_unknown),#no terrain modifiers
							  (else_try),
								#If the attacker party isn't a weird type, the terrain is entirely based on the
								#defender (unless the defender is invalid).
								 (ge, ":defender_party", 0),
								 (try_begin),
									#If the defender is a walled center, use siege mode.
									(this_or_next|party_slot_eq, ":defender_party", slot_party_type, spt_town),
									(party_slot_eq, ":defender_party", slot_party_type, spt_castle),
									(assign, reg0, dplmc_terrain_code_siege),#siege mode, defined in header_terrain_types.py
								 (else_try),
									#If the defender is a village
									(party_slot_eq, ":defender_party", slot_party_type, spt_village),
									(assign, reg0, dplmc_terrain_code_village),
								 (else_try),
									#If the defender is a bandit lair or a ship, use no terrain modifier.
									(this_or_next|party_slot_eq, ":defender_party", slot_party_type, spt_bandit_lair),
										(party_slot_eq, ":defender_party", slot_party_type, spt_ship),
									(assign, reg0, dplmc_terrain_code_unknown),#no terrain modifiers
								 (else_try),
									#If the defender is attached, do the same checks but for the attachment.
									(party_get_attached_to, ":attachment", ":defender_party"),
									(ge, ":attachment", 0),
									(party_is_active, ":attachment"),
									(assign, ":attachment_value", -100),
									(try_begin),
										#Walled centers use siege modifiers
									   (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_town),
										  (party_slot_eq, ":attachment", slot_party_type, spt_castle),
									   (assign, ":attachment_value", dplmc_terrain_code_siege),
									(else_try),
										#Villages
									   (party_slot_eq, ":attachment", slot_party_type, spt_village),
									   (assign, ":attachment_value", dplmc_terrain_code_village),
									(else_try),
										#bandit-lairs and ships have no modifiers currently
									   (this_or_next|party_slot_eq, ":attachment", slot_party_type, spt_bandit_lair),
										(party_slot_eq, ":attachment", slot_party_type, spt_ship),
									   (assign, ":attachment_value", dplmc_terrain_code_unknown),#no terrain modifiers
									(try_end),
									#If neither of the above apply, fall through to the next condition.
									(neq, ":attachment_value", -100),
									(assign, reg0, ":attachment_value"),
								 (else_try),
									#Use the terrain under the defender.
									#In the future I might want to change this so there's a tactics contest
									#between the attacker and defender to choose the more favorable ground
									#from their immediate surroundings.  I would also have to change the actual
									#terrain-type code.
									(party_get_current_terrain, reg0, ":defender_party"),
								 (try_end),
							  (else_try),
								 #If we get here, it means the defender was invalid, so use the terrain under
								 #the attacker.
								 (ge, ":attacker_party", 0),
								 (party_get_current_terrain, reg0, ":attacker_party"),#terrain under attacker
							  (try_end),
						   ]),
						   
						  #script_dplmc_party_calculate_strength_in_terrain
						  # INPUT: arg1 = party_id
						  #        arg2 = terrain (from header_terrain_types.py)
						  #        arg3 = exclude leader (0 for do-not-exclude, 1 for exclude)
						  #        arg4 = cache policy (1 is use terrain, 2 is use non-terrain, 0 is do not use)
						  # OUTPUT: reg0 = strength with terrain
						  #         reg1 = strength ignoring terrain
						  ("dplmc_party_calculate_strength_in_terrain",
							[
							  (store_script_param, ":party", 1), #Party_id
							  (store_script_param, ":terrain_type", 2),#a value from header_terrain_types.py
							  (store_script_param, ":exclude_leader", 3),#(0 for do-not-exclude, 1 for exclude)
							  (store_script_param, ":cache_policy", 4),#1 is use terrain, 2 is use non-terrain, 0 is do not use)

							  (assign, ":total_strength_terrain", 0),
							  (assign, ":total_strength_no_terrain", 0),

							  (party_get_num_companion_stacks, ":num_stacks", ":party"),
							  (assign, ":first_stack", 0),
							  (try_begin),
								(neq, ":exclude_leader", 0),
								(assign, ":first_stack", 1),
							  (try_end),
							  #Bonus for heroes on top of the rest
							  (assign, ":hero_percent", 110),
							  ##Moved setting the multipliers out of the loop...
							  (assign, ":guaranteed_horse_percent", 100),
							  (assign, ":guaranteed_ranged_percent", 100),
							  (assign, ":guaranteed_neither_percent", 100),
							  #First, test for some special codes:
							  (try_begin),
								 (eq, ":terrain_type", dplmc_terrain_code_none),#Apply no modifiers
								 (assign, ":hero_percent", 100),
							  (else_try),
								(eq, ":terrain_type", dplmc_terrain_code_village),#A dismounted fight at a village (apply hero modifier, nothing else)
							  (else_try),
								(eq, ":terrain_type", dplmc_terrain_code_siege),#A siege battle, not including sorties.
								(assign, ":guaranteed_ranged_percent", 120),
							  #The rest are ordinary rt_* codes.
							  #I changed the balance of these to make the variations less extreme (e.g. 150% mounted strength on rt_steppe).
							  #I believe that the version from ArcherOS is trying to create certain map results, rather than solely
							  #make autocalc strength more accurate in terms of "what would happen if they fought the player".
							  (else_try),
								(eq, ":terrain_type", rt_steppe),
								#The 150% increase in the steppe strikes me as excessive.
								#Since the NPC cost increase for mounted troops is 20%, and the PC cost is 65%,
								#it isn't entirely implausible.
								#(assign, ":guaranteed_horse_percent", 150),
								#Archer uses 150%, Custom Commander uses a flat 125%.
								(assign, ":guaranteed_horse_percent", 120),
							  (else_try),
								#I am unaware of any game mechanic in live battles that gives any disadvantage
								#to horses on snow or sand as opposed to a plain.
								(this_or_next|eq, ":terrain_type", rt_snow),
								(this_or_next|eq, ":terrain_type", rt_desert),
									(eq, ":terrain_type", rt_plain),
								(assign, ":guaranteed_horse_percent", 120),
							 (else_try),
								#I suspect that the 120% mounted bonus for steppe forests is inaccurate,
								#but I haven't checked it out yet.
								(eq, ":terrain_type", rt_steppe_forest),
								(assign, ":guaranteed_horse_percent", 120),
							 (else_try),
								(this_or_next|eq, ":terrain_type", rt_forest),
								(this_or_next|eq, ":terrain_type", rt_mountain_forest),
									 (eq, ":terrain_type", rt_snow_forest),
								#(assign, ":guaranteed_neither_percent", 120),
								(assign, ":guaranteed_neither_percent", 110),
							 (try_end),
							  
							  (try_for_range, ":i_stack", ":first_stack", ":num_stacks"),
								(party_stack_get_troop_id, ":stack_troop",":party", ":i_stack"),
								(store_character_level, ":stack_strength", ":stack_troop"),
								(val_add, ":stack_strength", 4), #new was 12 (patch 1.125)
								(val_mul, ":stack_strength", ":stack_strength"),
								(val_mul, ":stack_strength", 2), #new (patch 1.125)
								#move the next two lines to after terrain advantage
								#(val_div, ":stack_strength", 100), 
								#(val_max, ":stack_strength", 1), #new (patch 1.125)
								(assign, ":terrain_free_strength", ":stack_strength"),
								##use Arch3r's terrain advantage code (bug-fix changes 2011-04-13; other changes 2011-04-25)
								(try_begin),
								   ##AotE terrain advantages
								   (assign, ":hero_horse", 0),#added for heroes (any positive number = has a horse)
								   (try_begin),
									  (this_or_next|eq, "trp_player", ":stack_troop"),
										(troop_is_hero, ":stack_troop"),
									  (gt, ":guaranteed_horse_percent", ":hero_percent"),#don't bother if we wouldn't use the result
									  (neg|troop_is_guarantee_horse, ":stack_troop"),#don't bother if we already know the troop has a horse
									  (store_skill_level, reg0, "skl_riding", ":stack_troop"),
									  (ge, reg0, 2),#don't bother if the troop has no/minimal riding skill
									  #Just checking ek_horse may not work for non-companions, so check the inventory
									  (troop_get_inventory_capacity, ":inv_cap", ":stack_troop"),
									  (ge, ":inv_cap", 1),
									  (val_min, ":inv_cap", dplmc_ek_alt_items_begin + 8),#Don't check too much of the inventory
									  (try_for_range, ":inv_slot", 0, ":inv_cap"),
										(troop_inventory_slot_get_item_amount, reg1, ":stack_troop", ":inv_slot"),
										(ge, reg1, 1),#quantity must be greater than zero
										(troop_get_inventory_slot, reg0, ":stack_troop", ":inv_slot"),
										(ge, reg0, 1),#must be a valid item
										(item_get_type, reg1, reg0),#check if the item is a horse
										(eq, reg1, itp_type_horse),
										(assign, ":inv_cap", ":inv_slot"),#break loop
									  (try_end),
									  #If no horse found, set to zero
									  (neg|is_between, ":hero_horse", horses_begin, horses_end),
									  (assign, ":hero_horse", 0),
								   (try_end),
								   (assign, ":stack_strength_multiplier", 100),#<-- percent multiplier
								   (try_begin),#Mounted troops
									  (this_or_next|ge, ":hero_horse", 1),
									  (troop_is_guarantee_horse, ":stack_troop"),
									  (assign, ":stack_strength_multiplier", ":guaranteed_horse_percent"),
								   (else_try),#Ranged troops
									  (troop_is_guarantee_ranged, ":stack_troop"),
									  (assign, ":stack_strength_multiplier", ":guaranteed_ranged_percent"),
								   (else_try),#Infantry
									  (assign, ":stack_strength_multiplier", ":guaranteed_neither_percent"),
								   (try_end),
									
								   #Use hero/player modifiers if a better one didn't apply
								   (try_begin),
									  (this_or_next|eq, ":stack_troop", "trp_player"),
										 (troop_is_hero, ":stack_troop"),
									  (val_max, ":stack_strength_multiplier", ":hero_percent"),#hero bonus
								   (try_end),
								   
								   (val_mul, ":stack_strength", ":stack_strength_multiplier"),		   
								   (val_add, ":stack_strength", 50),#add this before division for correct rounding
								   (val_div, ":stack_strength", 100),
								   ##AotE terrain advantages
								(try_end),
								#moved the next two lines here from above
								(val_div, ":stack_strength", 100),#<- moved here from above
								(val_max, ":stack_strength", 1), #new (patch 1.125) #<- moved here from above
								(val_div, ":terrain_free_strength", 100),
								(val_max, ":terrain_free_strength", 1),
								(try_begin),
								  (neg|troop_is_hero, ":stack_troop"),
								  (party_stack_get_size, ":stack_size",":party",":i_stack"),
								  (party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
								  (val_sub, ":stack_size", ":num_wounded"),
								  (val_mul, ":stack_strength", ":stack_size"),
								  (val_mul, ":terrain_free_strength", ":stack_size"),
								(else_try),
								  (troop_is_wounded, ":stack_troop"), #hero & wounded
								  (assign, ":stack_strength", 0),
								  (assign, ":terrain_free_strength", 0),
								(try_end),
								(val_add, ":total_strength_terrain", ":stack_strength"),
								(val_add, ":total_strength_no_terrain", ":terrain_free_strength"),
							  (try_end),
							  #Load results into registers and cache if appropriate
							  (assign, reg0, ":total_strength_terrain"),
							  (assign, reg1, ":total_strength_no_terrain"),
							  (try_begin),
								 (eq, ":cache_policy", 1),
								 (party_set_slot, ":party", slot_party_cached_strength, reg0),
							  (else_try),
								 (eq, ":cache_policy", 2),
								 (party_set_slot, ":party", slot_party_cached_strength, reg1),
							  (try_end),
						  ]),  
						  
						    #script_dplmc_player_can_give_troops_to_troop  (Warning, clobbers {s11}!)
						  #
						  # INPUT: arg1 = troop_id
						  # OUTPUT: reg0 = 1 or more is yes, 0 or less is no
						  #
						  # This script does not take into account things like whether the troop
						  # is a prisoner of a party, so it can be used for checking whether troops
						  # can be added to a garrison.
						  #
						  # The general logic is that you can give troops to a member of your
						  # own faction if any of the following are true:
						  #   - You are the faction leader or marshall
						  #   - You are the spouse of the faction leader, and the faction
						  #     leader is not on bad terms with you
						  #   - The troop is an affiliated family member
						  #   - The troop is your spouse, and is either pliable or not on bad terms
						  #   - The troop is a former companion with whom you are on good terms
						  #   - The troop is related to you by marriage and you are on good terms
						  #
						  # For allied factions, the conditions are similar to the above.
						  # However, being the marshall or leader of your own faction does not
						  # guarantee cooperation from lords who dislike you.
						  #
						  # For non-allied other factions, the check for faction leader or
						  # marshall are not relevant, and the faction must not be at war
						  # with the player's faction.
						  ("dplmc_player_can_give_troops_to_troop",
						  [
							(store_script_param, ":troop_id", 1), #Party_id
							(assign, ":can_give_troops", 0),
							(assign, ":save_reg1", reg1),

							(try_begin),
								(this_or_next|eq, ":troop_id", "trp_kingdom_heroes_including_player_begin"),
								(eq, ":troop_id", "trp_player"),
								(assign, ":can_give_troops", 1),
							(else_try),
								(lt, ":troop_id", 1),
								(assign, ":can_give_troops", 0),
							(else_try),
								(store_faction_of_troop, ":troop_faction", ":troop_id"),
								
								(call_script, "script_troop_get_player_relation", ":troop_id"),
								(assign, ":troop_relation", reg0),
								(troop_get_slot, ":troop_reputation", ":troop_id", slot_lord_reputation_type),
								
								(try_begin),
									#Troop is member of player supporters faction
									(eq, ":troop_faction", "fac_player_supporters_faction"),
									##Always yes in Native, but if centralization is negative allow non-compliance
									(faction_get_slot, reg0, ":troop_faction", dplmc_slot_faction_centralization),
									(try_begin),
										(ge, reg0, 0),
										(assign, reg0, -200),
									(else_try),
										(val_mul, reg0, -10),
										(val_add, reg0, -35),#Centralization -1 has -25, -2 has -15, and -3 has -5
									(try_end),
									(gt, ":troop_relation", reg0),
									(assign, ":can_give_troops", 1),
								(else_try),
									#Troop is a member of the same faction as the player
									(eq, ":troop_faction", "$players_kingdom"),
									(faction_get_slot, ":troop_faction_leader", ":troop_faction", slot_faction_leader),
									(try_begin),
										#Leader or marshall
										(this_or_next|eq, ":troop_faction_leader", "trp_player"),
											(faction_slot_eq, ":troop_faction", slot_faction_marshall, "trp_player"),
										#If centralization is negative allow non-compliance
										(faction_get_slot, reg0, ":troop_faction", dplmc_slot_faction_centralization),
										(try_begin),
											(ge, reg0, 0),
											(assign, reg0, -200),
										(else_try),
											(val_mul, reg0, -10),
											(val_add, reg0, -35),#Centralization -1 has -25, -2 has -15, and -3 has -5
										(try_end),
										(gt, ":troop_relation", reg0),
										(assign, ":can_give_troops", 1),
									(else_try),
										#Spouse of leader
										(gt, ":troop_faction_leader", 1),
										(neg|troop_slot_eq, "trp_player", slot_troop_spouse, -1),
										(this_or_next|troop_slot_eq, ":troop_faction_leader", slot_troop_spouse, "trp_player"),
											(troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_faction_leader"),
										(call_script, "script_troop_get_player_relation", ":troop_faction_leader"),
										(ge, reg0, 0),
										#If centralization is negative allow non-compliance
										(faction_get_slot, reg0, ":troop_faction", dplmc_slot_faction_centralization),
										(try_begin),
											(ge, reg0, 0),
											(assign, reg0, -200),
										(else_try),
											(val_mul, reg0, -10),
											(val_add, reg0, -35),#Centralization -1 has -25, -2 has -15, and -3 has -5
										(try_end),
										(gt, ":troop_relation", reg0),
										(assign, ":can_give_troops", 1),
									(else_try),
										#Spouse of troop
										(neg|troop_slot_eq, "trp_player", slot_troop_spouse, -1),
										(this_or_next|troop_slot_eq, ":troop_id", slot_troop_spouse, "trp_player"),
											(troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_id"),
										(this_or_next|ge, ":troop_relation", 0),
										(this_or_next|eq, ":troop_reputation", lrep_conventional),
										(this_or_next|eq, ":troop_reputation", lrep_moralist),
											(eq, ":troop_reputation", lrep_otherworldly),
										(assign, ":can_give_troops", 1),
									(else_try),
										#Affiliated family member
										(call_script, "script_dplmc_is_affiliated_family_member", ":troop_id"),
										(ge, reg0, 1),
										(assign, ":can_give_troops", 1),
									(else_try),
										#Close companion previously under arms
										(this_or_next|is_between, ":troop_id", companions_begin, companions_end),
											(is_between, ":troop_id", pretenders_begin, pretenders_end),
										(neg|troop_slot_eq, ":troop_id", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
										(ge, ":troop_relation", 20),
										(assign, ":can_give_troops", 1),
									(else_try),
										#In-law (or hypothetically a blood relative) who is close with the player
										(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_id", "trp_player"),
										(ge, reg0, 2),#<-- deliberately set the cutoff to 2, not 1
										(ge, ":troop_relation", 14),
										(this_or_next|ge, reg0, 10),
											(ge, ":troop_relation", 20),
										(assign, ":can_give_troops", 1),
									(try_end),
								(else_try),
									#Troop is member of a faction allied with the player's
									(call_script, "script_dplmc_get_faction_truce_length_with_faction", "$players_kingdom", ":troop_faction"),
									(gt, reg0, dplmc_treaty_defense_days_expire),
									(faction_get_slot, ":player_faction_leader", "$players_kingdom", slot_faction_leader),
									(try_begin),
										#Leader or marshall
										(this_or_next|eq, ":player_faction_leader", "trp_player"),
											(faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
										(ge, ":troop_relation", 0),#only for allied factions, not for the player's own faction
										(assign, ":can_give_troops", 1),
									(else_try),
										#Spouse of leader
										(gt, ":player_faction_leader", 1),
										(neg|troop_slot_eq, "trp_player", slot_troop_spouse, -1),
										(this_or_next|troop_slot_eq, ":player_faction_leader", slot_troop_spouse, "trp_player"),
											(troop_slot_eq, "trp_player", slot_troop_spouse, ":player_faction_leader"),
										(ge, ":troop_relation", 0),#only for allied factions, not for the player's own faction
										(call_script, "script_troop_get_player_relation", ":player_faction_leader"),
										(ge, reg0, 0),
										(assign, ":can_give_troops", 1),
									(else_try),
										#Spouse of troop
										(neg|troop_slot_eq, "trp_player", slot_troop_spouse, -1),
										(this_or_next|troop_slot_eq, ":troop_id", slot_troop_spouse, "trp_player"),
											(troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_id"),
										(this_or_next|ge, ":troop_relation", 0),
										(this_or_next|eq, ":troop_reputation", lrep_conventional),
										(this_or_next|eq, ":troop_reputation", lrep_moralist),
											(eq, ":troop_reputation", lrep_otherworldly),
										(assign, ":can_give_troops", 1),
									(else_try),
										#Affiliated family member
										(call_script, "script_dplmc_is_affiliated_family_member", ":troop_id"),
										(ge, reg0, 1),
										(assign, ":can_give_troops", 1),
									(else_try),
										#Close companion previously under arms
										(this_or_next|is_between, ":troop_id", companions_begin, companions_end),
											(is_between, ":troop_id", pretenders_begin, pretenders_end),
										(neg|troop_slot_eq, ":troop_id", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
										(ge, ":troop_relation", 20),
										(assign, ":can_give_troops", 1),
									(else_try),
										#In-law (or hypothetically a blood relative) who is close with the player
										(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_id", "trp_player"),
										(ge, reg0, 2),#<-- deliberately set the cutoff to 2, not 1
										(ge, ":troop_relation", 14),
										(this_or_next|ge, reg0, 10),
											(ge, ":troop_relation", 20),
										(assign, ":can_give_troops", 1),
									(try_end),
								(else_try),
									#Troop is a member of a faction that isn't hostile to the player's
									(store_relation, reg0, ":troop_faction", "fac_player_faction"),
									(ge, reg0, 0),
									(store_relation, reg0, ":troop_faction", "$players_kingdom"),
									(ge, reg0, 0),
									(try_begin),
										#Spouse of troop
										(neg|troop_slot_eq, "trp_player", slot_troop_spouse, -1),
										(this_or_next|troop_slot_eq, ":troop_id", slot_troop_spouse, "trp_player"),
											(troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_id"),
										(this_or_next|ge, ":troop_relation", 0),
										(this_or_next|eq, ":troop_reputation", lrep_conventional),
										(this_or_next|eq, ":troop_reputation", lrep_moralist),
											(eq, ":troop_reputation", lrep_otherworldly),
										(assign, ":can_give_troops", 1),
									(else_try),
										#Affiliated family member
										(call_script, "script_dplmc_is_affiliated_family_member", ":troop_id"),
										(ge, reg0, 1),
										(assign, ":can_give_troops", 1),
									(else_try),
										#Close companion previously under arms
										(this_or_next|is_between, ":troop_id", companions_begin, companions_end),
											(is_between, ":troop_id", pretenders_begin, pretenders_end),
										(neg|troop_slot_eq, ":troop_id", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
										(ge, ":troop_relation", 20),
										(assign, ":can_give_troops", 1),
									(else_try),
										#In-law (or hypothetically a blood relative) who is close with the player
										(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_id", "trp_player"),
										(ge, reg0, 2),#<-- deliberately set the cutoff to 2, not 1
										(ge, ":troop_relation", 14),
										(this_or_next|ge, reg0, 10),
											(ge, ":troop_relation", 20),
										(assign, ":can_give_troops", 1),
									(try_end),
								(try_end),
							(try_end),
							
							(assign, reg1, ":save_reg1"),
							(assign, reg0, ":can_give_troops"),
						  ]),
						  
						    #script_dplmc_print_centers_in_numbers_to_s0
						  #
						  #similar to script_print_troop_owned_centers_in_numbers_to_s0
						  #
						  #INPUT:
						  #  arg1: owned_towns
						  #  arg2: owned_castles
						  #  arg3: owned_villages
						  #
						  #OUTPUT:
						  #  reg0: owned_towns + owned_castles + owned_villages
						  #    s0: a string describing the numbers of centers
							("dplmc_print_centers_in_numbers_to_s0",
						   [
							 (store_script_param_1, ":owned_towns"),
							 (store_script_param_2, ":owned_castles"),
							 (store_script_param, ":owned_villages", 3),
							 (str_store_string, s0, "@nothing"),
							 
							 (assign, ":num_types", 0),
							 (try_begin),
							   (gt, ":owned_villages", 0),
							   (assign, reg0, ":owned_villages"),
							   (store_sub, reg1, reg0, 1),
							   (str_store_string, s0, "@{reg0} village{reg1?s:}"),
							   (val_add, ":num_types", 1),
							 (try_end),
							 
							 (try_begin),
							   (gt, ":owned_castles", 0),
							   (assign, reg0, ":owned_castles"),
							   (store_sub, reg1, reg0, 1),
							   (try_begin),
								 (eq, ":num_types", 0),
								 (str_store_string, s0, "@{reg0} castle{reg1?s:}"),
							   (else_try),
								 (str_store_string, s0, "@{reg0} castle{reg1?s:} and {s0}"),
							   (try_end),
							   (val_add, ":num_types", 1),
							 (try_end),
							 
							 (try_begin),
							   (gt, ":owned_towns", 0),
							   (assign, reg0, ":owned_towns"),
							   (store_sub, reg1, reg0, 1),
							   (try_begin),
								 (eq, ":num_types", 0),
								 (str_store_string, s0, "@{reg0} town{reg1?s:}"),
							   (else_try),
								 (eq, ":num_types", 1),
								 (str_store_string, s0, "@{reg0} town{reg1?s:} and {s0}"),
							   (else_try),
								 (str_store_string, s0, "@{reg0} town{reg1?s:}, {s0}"),
							   (try_end),
							 (try_end),
							 
							 (store_add, reg0, ":owned_villages", ":owned_castles"),
							 (val_add, reg0, ":owned_towns"),
							 ]),

						  #"script_dplmc_distribute_gold_to_lord_and_holdings"
						  #
						  #Related to script_dplmc_remove_gold_from_lord_and_holdings, divides the gold
						  #between the lord and his fortresses in a semi-intelligent way.
						  #
						  #INPUT:
						  #   arg1: the amount of gold
						  #   arg2: the lord's ID
						  ("dplmc_distribute_gold_to_lord_and_holdings",
						   [
							(store_script_param_1, ":gold_left"),
							(store_script_param_2, ":lord_no"),
							
							(try_begin),
								(lt, ":lord_no", 0),#Invalid ID
							(else_try),
								#If the number is negative, handle this using script_dplmc_remove_gold_from_lord_and_holdings
								(lt, ":gold_left", 0),
								(val_mul, ":gold_left", -1),
								(call_script, "script_dplmc_remove_gold_from_lord_and_holdings", ":gold_left", ":lord_no"),
								(assign, ":gold_left", 0),
							(else_try),
								(neq, ":lord_no", "trp_player"),
								(neg|troop_is_hero, ":lord_no"),#Not hero or player
								(troop_add_gold, ":lord_no", ":gold_left"),
								(assign, ":gold_left", 0),
							(else_try),
								#The player doesn't use center wealth to pay garrison wages, so just
								#give it directly.
								(eq, ":lord_no", "trp_player"),
								(troop_add_gold, "trp_player", ":gold_left"),
								(assign, ":gold_left", 0),
							(else_try),
								(neg|troop_is_hero, ":lord_no"),#If the lord isn't the player, and isn't a hero, do nothing
							(else_try),	
								(troop_get_slot, ":target_gold", ":lord_no", slot_troop_wealth),
								(val_max, ":target_gold", 0),
								#If the lord is low on gold, first he takes enough gold so he isn't low on funds,
								#or all of the gold, whichever is less.
								(store_sub, ":gold_to_give", 6000, ":target_gold"),#6000 is the standard starting gold for lords (kings start with more, but don't increase this for them, since I'm using this number as a "low on gold" threshold)
								(val_max, ":gold_to_give", 0),
								(val_min, ":gold_to_give", ":gold_left"),
									
								(val_add, ":target_gold", ":gold_to_give"),
								(troop_set_slot, ":lord_no", slot_troop_wealth, ":target_gold"),
								(val_sub, ":gold_left", ":gold_to_give"),
								#If gold remains, the lord gives some to any castles or towns he owns that have
								#low wealth.  Note that iterating in this order means that towns get checked
								#before castles do.
								(gt, ":gold_left", 0),
								(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
									(party_slot_eq, ":center_no", slot_town_lord, ":lord_no"),
									(party_get_slot, ":target_gold", ":center_no", slot_town_wealth),
									#Don't give gold to centers with garrisons more than 50% above the ideal size
									(store_party_size_wo_prisoners, ":garrison_size", ":center_no"),
									(call_script, "script_party_get_ideal_size", ":center_no"),#This script has been modified to support this use
									(val_mul, reg0, 3),
									(val_div, reg0, 2),
									(ge, reg0, ":garrison_size"),
									
									(try_begin),
										(party_slot_eq, ":center_no", slot_party_type, spt_town),
										(store_sub, ":gold_to_give", 4000, ":target_gold"),#4000 is the standard starting gold for towns
									(else_try),
										(store_sub, ":gold_to_give", 2000, ":target_gold"),#2000 is the standard starting gold for castles
									(try_end),
											
									(val_max, ":gold_to_give", 0),
									(val_min, ":gold_to_give", ":gold_left"),
									(gt, ":gold_to_give", 0),
									(val_add, ":target_gold", ":gold_to_give"),
									(party_set_slot, ":center_no", slot_town_wealth, ":target_gold"),
									(val_sub, ":gold_left", ":gold_to_give"),
								(try_end),
								#If gold is left -- the lord isn't low on gold, and none of his walled centers are --
								#he pockets the remainder.
								(gt, ":gold_left", 0),
								(troop_get_slot, ":target_gold", ":lord_no", slot_troop_wealth),
								(val_add, ":target_gold", ":gold_left"),
								(val_max, ":target_gold", 0),
								(troop_set_slot, ":lord_no", slot_troop_wealth, ":target_gold"),
								(assign, ":gold_left", 0),
							(try_end),
							]),
							
							  #"script_dplmc_remove_gold_from_lord_and_holdings"
							  #
							  #
							  #INPUT:
							  #   arg1: the amount of money to remove (greater than zero)
							  #   arg2: the ID of the lord spending the money
							  #
							  #OUTPUT:
							  #   None
								("dplmc_remove_gold_from_lord_and_holdings",
							   [
								(store_script_param_1, ":gold_cost"),
								(store_script_param_2, ":lord_no"),

								(try_begin),
									(lt, ":lord_no", 0),#Invalid ID
								(else_try),
									(neq, ":lord_no", "trp_player"),
									(neg|troop_is_hero, ":lord_no"),#Not player or hero
								(else_try),
									#If the number is negative, give gold instead of taking it.
									#Handle this using script_dplmc_distribute_gold_to_lord_and_holdings
									(lt, ":gold_cost", 0),
									(val_mul, ":gold_cost", -1),
									(call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", ":gold_cost", ":lord_no"),
									(assign, ":gold_cost", 0),
								(else_try),
									#For the player, first subtract the gold from his treasury (if any).
									(eq, ":lord_no", "trp_player"),
									(store_troop_gold, ":treasury", "trp_household_possessions"),
									(try_begin),
										(ge, ":treasury", 1),
										(val_min, ":treasury", ":gold_cost"),
										(call_script, "script_dplmc_withdraw_from_treasury", ":treasury"),
										(val_sub, ":gold_cost", ":treasury"),
									(try_end),
									(store_troop_gold, ":treasury", "trp_player"),
									(try_begin),
										(ge, ":treasury", 1),
										(val_min, ":treasury", ":gold_cost"),
										(troop_remove_gold, "trp_player", ":treasury"),
										(val_sub, ":gold_cost", ":treasury"),
									(try_end),
									#Fall through to the next section if the treasury didn't cover it.
									(lt, ":gold_cost", 1),
								(else_try),
									#Remove the gold directly from the lord's wealth slot
									(ge, ":gold_cost", 1),
									(ge, ":lord_no", 1),#not the player
									(troop_get_slot, ":treasure", ":lord_no", slot_troop_wealth),
									(ge, ":treasure", 1),
									(try_begin),
										(ge, ":treasure", ":gold_cost"),
										(val_sub, ":treasure", ":gold_cost"),
										(assign, ":gold_cost", 0),
									(else_try),
										(val_sub, ":gold_cost", ":treasure"),
										(assign, ":treasure", 0),
									(try_end),
									(troop_set_slot, ":lord_no", slot_troop_wealth, ":treasure"),
									#Fall through to the next section if his personal wealth didn't cover it.
									(lt, ":gold_cost", 1),
								(else_try),
									#Remove remaining gold from uncollected taxes.
									#We iterate backwards in order to remove from villages before castles and towns.
									(ge, ":gold_cost", 1),
									(try_for_range_backwards, ":center_no", centers_begin, centers_end),
										(ge, ":gold_cost", 1),
										(party_slot_eq, ":center_no", slot_town_lord, ":lord_no"),
										(party_get_slot, ":treasure", ":center_no", slot_center_accumulated_rents),
										(try_begin),
											(gt, ":treasure", 0),
											(ge, ":treasure", ":gold_cost"),
											(val_sub, ":treasure", ":gold_cost"),
											(assign, ":gold_cost", 0),
										(else_try),
											(gt, ":treasure", 0),
											(val_sub, ":gold_cost", ":treasure"),
											(assign, ":treasure", 0),
										(try_end),
										(party_set_slot, ":center_no", slot_center_accumulated_rents, ":treasure"),

										(ge, ":gold_cost", 1),
										(party_get_slot, ":treasure", ":center_no", slot_center_accumulated_tariffs),
										(try_begin),
											(gt, ":treasure", 0),
											(ge, ":treasure", ":gold_cost"),
											(val_sub, ":treasure", ":gold_cost"),
											(assign, ":gold_cost", 0),
										(else_try),
											(gt, ":treasure", 0),
											(val_sub, ":gold_cost", ":treasure"),
											(assign, ":treasure", 0),
										(try_end),
										(party_set_slot, ":center_no", slot_center_accumulated_tariffs, ":treasure"),
									(try_end),
									#Fall through to the next section if the uncollected taxes didn't cover it.
									(lt, ":gold_cost", 1),
								(else_try),
									#Remove remaining gold from center wealth.  We iterate backwards to remove from
									#castles before towns.
									(ge, ":gold_cost", 1),
									(try_for_range_backwards, ":center_no", centers_begin, centers_end),
										(ge, ":gold_cost", 1),
										(party_slot_eq, ":center_no", slot_town_lord, ":lord_no"),
										(party_get_slot, ":treasure", ":center_no", slot_town_wealth),
										(ge, ":treasure", 1),
										(try_begin),
											(ge, ":treasure", ":gold_cost"),
											(val_sub, ":treasure", ":gold_cost"),
											(assign, ":gold_cost", 0),
										(else_try),
											(val_sub, ":gold_cost", ":treasure"),
											(assign, ":treasure", 0),
										(try_end),
										(party_set_slot, ":center_no", slot_town_wealth, ":treasure"),
									(try_end),
									(lt, ":gold_cost", 1),
								(else_try),
									#Try to remove the gold from the hero himself
									(store_troop_gold, ":treasure", ":lord_no"),
									(gt, ":treasure", 0),
									(try_begin),
										(ge, ":treasure", ":gold_cost"),
										(troop_remove_gold, ":lord_no", ":gold_cost"),
										(assign, ":gold_cost", 0),
									(else_try),
										(troop_remove_gold, ":lord_no", ":treasure"), #Floris - bugfix for Diplomacy, was missing lord argument
										(val_sub, ":gold_cost", ":treasure"),
									(try_end),
								(try_end),

							   ]),

							  # dplmc_prepare_hero_center_points_ignoring_center
							  #  
							  # Input: arg1 = target_center
							   ("dplmc_prepare_hero_center_points_ignoring_center",[
								  (store_script_param, ":target_center", 1),
								  
								  (troop_set_slot, "trp_player", slot_troop_temp_slot, 0),
								  (troop_set_slot, "trp_player", dplmc_slot_troop_temp_slot, 0),
								  
								  (try_for_range, ":troop_no", heroes_begin, heroes_end),
									(troop_set_slot, ":troop_no", slot_troop_temp_slot, 0),
									(troop_set_slot, ":troop_no", dplmc_slot_troop_temp_slot, 0),
								  (try_end),
								  
								  (try_for_range, ":center_no", centers_begin, centers_end),
									#Skip "target center"
									(neq, ":center_no", ":target_center"),
								  
									#Lord is player or a hero
									(party_get_slot, ":troop_no", ":center_no", slot_town_lord),
									(this_or_next|eq, ":troop_no", "trp_player"),
										(is_between, ":troop_no", heroes_begin, heroes_end),
									
									#Update lord point total
									(assign, ":center_points", 1),
									(try_begin),
										(party_slot_eq, ":center_no", slot_party_type, spt_town),
										(assign, ":center_points", 3),
									(else_try),
										(party_slot_eq, ":center_no", slot_party_type, spt_castle),
										(assign, ":center_points", 2),
									(try_end),
									
									(troop_get_slot, ":slot_value", ":troop_no", slot_troop_temp_slot),
									(val_add, ":slot_value", ":center_points"),
									(troop_set_slot, ":troop_no", slot_troop_temp_slot, ":slot_value"),
									
									#Update distance from closest owned center to target
									(is_between, ":target_center", centers_begin, centers_end),
									(troop_get_slot, ":slot_value", ":troop_no", dplmc_slot_troop_temp_slot),
									(store_distance_to_party_from_party, ":cur_distance", ":target_center", ":center_no"),
									(val_max, ":cur_distance", 1),
									(try_begin),
										(eq, ":slot_value", 0),
										(assign, ":slot_value", ":cur_distance"),
									(try_end),
									(val_min, ":slot_value", ":cur_distance"),
									(troop_set_slot, ":troop_no", dplmc_slot_troop_temp_slot, ":slot_value"),
								  (try_end),
							   ]),
							   
							 # script_dplmc_calculate_troop_score_for_center_aux
							  #  Similar to script_calculate_troop_score_for_center
							  #
							  # slot_troop_temp_slot must already be loaded with center points;
							  # dplmc_slot_troop_temp_slot must already be loaded with distance.
							  #
							  # Input: arg1 = evaluator
							  #        arg2 = troop_no
							  #        arg3 = center_no
							  # Output: reg0 = score
							  #         reg1 = explanation string
							  ("dplmc_calculate_troop_score_for_center_aux",
							   [(store_script_param, ":troop_1", 1),
								(store_script_param, ":troop_2", 2),
								 (store_script_param, ":center_no", 3),

								 (assign, ":explanation", "str_political_explanation_most_deserving_in_faction"),
								 (assign, ":explanation_priority", -1),

							   (try_begin),
								  (lt, ":troop_1", 0),
								  (assign, ":relation", 0),
								  (assign, ":reputation", lrep_none),
							   (else_try),
								  (eq, ":troop_1", ":troop_2"),
								  (assign, ":relation", 50),
								   (troop_get_slot, ":reputation", ":troop_1", slot_lord_reputation_type),
							   (else_try),
								  (call_script, "script_troop_get_relation_with_troop", ":troop_1", ":troop_2"),
								  (assign, ":relation", reg0),
								  (troop_get_slot, ":reputation", ":troop_1", slot_lord_reputation_type),
							   (try_end),
							   (val_clamp, ":relation", -100, 101),

							   (troop_get_slot, reg0, ":troop_2", slot_troop_renown),
							   (val_max, reg0, 0),
							   (store_add, ":score", 500, reg0),
								(troop_get_slot, ":num_center_points", ":troop_2", slot_troop_temp_slot),
								(val_max, ":num_center_points", 0),
								(val_add, ":num_center_points", 1),

								#Subtract distance from closest other fief owned, except when
								#considering the lord's original holdings.
								(try_begin),
								  (troop_slot_ge, ":troop_2", slot_troop_temp_slot, 1),
								  (neg|troop_slot_eq, ":troop_2", slot_troop_home, ":center_no"),
								  (neg|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":troop_2"),

								  (troop_get_slot, reg0, ":troop_2", dplmc_slot_troop_temp_slot),
								  (gt, reg0, 1),
								  (val_min, reg0, 250),#upper cap on distance effect (bear in mind that this is subtracted from 500 + troop renown)
								  (val_sub, ":score", reg0),
								(try_end),

							   #(store_random_in_range, ":random", 50, 100),
							   #(val_mul, ":score", ":random"),
								(val_mul, ":score", 75),
							   (val_div, ":score", ":num_center_points"),
								
								(assign, ":fiefless_bonus_used", 0),
								(try_begin),
								   #Bonus for lords with no other fiefs when a village is being considered.
								  (lt, ":num_center_points", 2),
								  (party_slot_eq, ":center_no", slot_party_type, spt_village),
								  (neq, ":reputation", lrep_debauched),
								  (neq, ":reputation", lrep_selfrighteous),
								  (neq, ":reputation", lrep_quarrelsome),

									(val_mul, ":score", 2),
									(try_begin),
									  (lt, ":explanation_priority", 100),
									  (assign, ":explanation_priority", 100),
									  (assign, ":explanation", "str_political_explanation_lord_lacks_center"),
									(try_end),
									(assign, ":fiefless_bonus_used", 1),#because it has already been applied
								(try_end),
								
								(assign, ":troop_2_slot_alias", ":troop_2"),
								(try_begin),
									(eq, ":troop_2", "trp_player"),
									(assign, ":troop_2_slot_alias", "trp_kingdom_heroes_including_player_begin"),
								(try_end),

							   (try_begin),
								#Bonus for conquerer
								(neq, ":reputation",  lrep_debauched),
								(this_or_next|neq, ":reputation", lrep_selfrighteous),
								   (eq, ":troop_1", ":troop_2"),
								(neq, ":reputation", lrep_cunning),
							  (neg|party_slot_eq, ":center_no", slot_party_type, spt_village),
							  (party_slot_eq, ":center_no", slot_center_last_taken_by_troop, ":troop_2_slot_alias"),
							  (try_begin),
								 (lt, ":num_center_points", 2),
								 (eq, ":fiefless_bonus_used", 0),
								 (assign, reg1, 50),#50% increase
							  (else_try),
								 (this_or_next|troop_slot_eq, ":troop_2", slot_troop_home, ":center_no"),
								 (this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":troop_2_slot_alias"),
								 (this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":troop_2_slot_alias"),
									(eq, ":reputation", lrep_martial),
								 (assign, reg1, 50),#50% increase
							  (else_try),
								 (assign, reg1, 25),#25% increase
							  (try_end),
							  (store_add, reg0, 100, reg1),
							  (val_mul, ":score", reg0),
							  (val_div, ":score", 100),
								(try_begin),
								  (ge, reg1, ":explanation_priority"),
								  (assign, ":explanation_priority", reg1),
								  (assign, ":explanation", "str_political_explanation_lord_took_center"),
								(try_end),
							(else_try),
								#Bonus for original owner
								(gt, ":troop_2", 0),
								(party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":troop_2_slot_alias"),
								(try_begin),
									(lt, ":num_center_points", 2),
									(eq, ":fiefless_bonus_used", 0),
									(assign, reg1, 50),#50% increase
								(else_try),
									(this_or_next|eq, ":troop_2", ":troop_1"),
									(this_or_next|troop_slot_eq, ":troop_2", slot_troop_home, ":center_no"),
										(party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":troop_2_slot_alias"),
									(assign, reg1, 50),#50% increase
								(else_try),
									(assign, reg1, 25),#25% increase
								(try_end),
								(store_add, reg0, 100, reg1),
								(val_mul, ":score", reg0),
								(val_div, ":score", 100),
								(try_begin),
								  (ge, reg1, ":explanation_priority"),
								  (assign, ":explanation_priority", reg1),
								(assign, ":explanation", "str_dplmc_political_explanation_original_lord"),
								(try_end),
							(else_try),
							#Bonus for previous owner, lord
								(gt, ":troop_2", 0),
								(party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":troop_2_slot_alias"),
								(try_begin),
									(lt, ":num_center_points", 2),
									(eq, ":fiefless_bonus_used", 0),
									(assign, reg1, 50),#50% increase
								(else_try),
								(troop_slot_eq, ":troop_2", slot_troop_home, ":center_no"),
									(assign, reg1, 50),
								(else_try),
									(assign, reg1, 25),#25% increase
								(try_end),
								(store_add, reg0, 100, reg1),
								(val_mul, ":score", reg0),
								(val_div, ":score", 100),
								(try_begin),
								  (ge, reg1, ":explanation_priority"),
								  (assign, ":explanation_priority", reg1),
								(assign, ":explanation", "str_dplmc_political_explanation_original_lord"),
								(try_end),
							(else_try),
							#Bonus for lord claiming the center as home
								(troop_slot_eq, ":troop_2", slot_troop_home, ":center_no"),
								(val_mul, ":score", 5),
								(val_div, ":score", 4),
								(try_begin),
								  (ge, 25, ":explanation_priority"),
								  (assign, ":explanation_priority", 25),
								(assign, ":explanation", "str_dplmc_political_explanation_original_lord"),
								(try_end),
							(else_try),
							#Aesthetic penalty (doesn't apply when there was a bonus)
							#To try to make the late game less mixed, have a preference towards
							#assigning lords to their own faction types.
								(troop_get_slot, reg0, ":troop_2", slot_troop_original_faction),
								(party_get_slot, reg1, ":center_no", slot_center_original_faction),
								(neq, reg0, reg1),
							#These extra checks are to avoid penalizing the player or promoted companions
							#unintentionally.
								(is_between, reg0, npc_kingdoms_begin, npc_kingdoms_end),
								(is_between, reg1, npc_kingdoms_begin, npc_kingdoms_end),
								#Take 95% of score
									(val_mul, ":score", 19),
									(val_add, ":score", 10),
									(val_div, ":score", 20),
							   (try_end),

								#add 2 x relation (minus controversy) to score
							   (troop_get_slot, ":controversy", ":troop_2", slot_troop_controversy),
							   (val_clamp, ":controversy", 0, 101),
								(store_mul, ":relation_mod", ":relation", 2),
								(val_sub, ":relation_mod", ":controversy"),
								#this modifier will not raise the score by more than 50%
								(store_add, reg0, ":score", 1),
								(val_div, reg0, 2),
								(val_max, reg0, 1),
								(val_min, ":relation_mod", reg0),
								
								(store_mul, reg0, ":score", 100),#rego has pre-relationship modified score
								(val_add, ":score", ":relation_mod"),
								(val_div, reg0, ":score"),
								(store_sub, reg1, ":score", 100),#reg1 has percentage change (i.e. 1.5 times becomes 50% change) from relation/controversy

								(try_begin),
									(ge, reg1, 0),
									(ge, reg1, ":explanation_priority"),
									  (ge, ":relation", 15),
									(assign, ":explanation_priority", reg1),
									  (assign, ":explanation", "str_political_explanation_most_deserving_friend"),
								(try_end),

							   (assign, reg0, ":score"),
								(assign, reg1, ":explanation"),
							   ]),
							   

							##Auto-Buy-Food from rubik's Custom Commander end

							  # script_dplmc_get_trade_penalty
							  #
							  #This is similar to the old script_get_trade_penalty,
							  #except it uses parameters instead of relying on global variables.
							  #
							  # Input:
							  # param1: item_kind_id
							  # param2: market center
							  # param3: customer troop (-1 for a non-troop-specific answer, -2 to notify the script that this is being used to evaluate a gift)
							  # param4: merchant troop (-1 for a non-troop-specific answer)
							  # Output: reg0

							  ("dplmc_get_trade_penalty",
								[
								  #Additions begin:
								 (store_script_param, ":item_kind_id", 1),
								  (store_script_param, ":market_center", 2),
								  (store_script_param, ":customer_troop", 3),
								  (store_script_param, ":merchant_troop", 4),
								  #End Additions
								  (assign, ":penalty",0),

								  ##Change this to support alternative customers
								  ##(party_get_skill_level, ":trade_skill", "p_main_party", skl_trade),
								  (try_begin),
									 #Player: use skill of player party
									(eq, ":customer_troop", "trp_player"),
									 (party_get_skill_level, ":trade_skill", "p_main_party", skl_trade),
								  (else_try),
									 #Hero leading a party: use skill of led party
									(gt, ":customer_troop", -1),
									(troop_is_hero, ":customer_troop"),
									 (troop_get_slot, ":customer_party", ":customer_troop", slot_troop_leaded_party),
									 (gt, ":customer_party", 0),
									 (party_is_active, ":customer_party"),
									 (party_get_skill_level, ":trade_skill", ":customer_party", skl_trade),
								  (else_try),
									 #Troop: use troop skill
									 (gt, ":customer_troop", -1),
									 (store_skill_level, ":trade_skill", ":customer_troop"),
								  (else_try),
									 (assign, ":trade_skill", 0),
								  (try_end),
								  ##End Change
								  (try_begin),
									(is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
									(assign, ":penalty",15), #reduced slightly
									(store_mul, ":skill_bonus", ":trade_skill", 1),
									(val_sub, ":penalty", ":skill_bonus"),
								  (else_try),
									(assign, ":penalty",100),
									(store_mul, ":skill_bonus", ":trade_skill", 5),
									(val_sub, ":penalty", ":skill_bonus"),
								  (try_end),

								  (assign, ":penalty_multiplier", average_price_factor),#<-- replaced 1000 with average_price_factor
							##       # Apply penalty if player is hostile to merchants faction
							##      (store_relation, ":merchants_reln", "fac_merchants", "fac_player_supporters_faction"),
							##      (try_begin),
							##        (lt, ":merchants_reln", 0),
							##        (store_sub, ":merchants_reln_dif", 10, ":merchants_reln"),
							##        (store_mul, ":merchants_relation_penalty", ":merchants_reln_dif", 20),
							##        (val_add, ":penalty_multiplier", ":merchants_relation_penalty"),
							##      (try_end),

								   # Apply penalty if player is on bad terms with the town
								  (try_begin),
									(eq, ":customer_troop", "trp_player"),#added
									(is_between, ":market_center", centers_begin, centers_end),#changed $g_encountered_party to :market_center
									(party_get_slot, ":center_relation", ":market_center", slot_center_player_relation),#changed $g_encountered_party to :market_center
									(store_mul, ":center_relation_penalty", ":center_relation", -3),
									(val_add, ":penalty_multiplier", ":center_relation_penalty"),
									(try_begin),
									  (lt, ":center_relation", 0),
									  (store_sub, ":center_penalty_multiplier", 100, ":center_relation"),
									  (val_mul, ":penalty_multiplier", ":center_penalty_multiplier"),
									  (val_div, ":penalty_multiplier", 100),
									(try_end),
								  (try_end),

								   # Apply penalty if player is on bad terms with the merchant (not currently used)
								   ##Begin Change
								  #(call_script, "script_troop_get_player_relation", "$g_talk_troop"),
								  #(assign, ":troop_reln", reg0),
								  (try_begin),
									 (this_or_next|eq, ":merchant_troop", "trp_player"),
										(eq, ":customer_troop", "trp_player"),
									 (gt, ":merchant_troop", -1),
									 (gt, ":customer_troop", -1),
									 (call_script, "script_troop_get_player_relation", ":merchant_troop"),
									 (assign, ":troop_reln", reg0),
								  (else_try),
									(is_between, ":merchant_troop", heroes_begin, heroes_end),
									 (is_between, ":customer_troop", heroes_begin, heroes_end),		 
									 (call_script, "script_troop_get_relation_with_troop", ":merchant_troop", ":customer_troop"),
									 (assign, ":troop_reln", reg0),
								  (else_try),
									 (assign, ":troop_reln", 0),
								  (try_end),
								  ##End Change
								  #(troop_get_slot, ":troop_reln", "$g_talk_troop", slot_troop_player_relation),
								  (try_begin),
									(lt, ":troop_reln", 0),
									(store_sub, ":troop_reln_dif", 0, ":troop_reln"),
									(store_mul, ":troop_relation_penalty", ":troop_reln_dif", 20),
									(val_add, ":penalty_multiplier", ":troop_relation_penalty"),
								  (try_end),


								  (try_begin),
									##Begin Change
									#(is_between, "$g_encountered_party", villages_begin, villages_end),
									(is_between, ":market_center", centers_begin, centers_end),
									(party_slot_eq, ":market_center", slot_party_type, spt_village),
									##End Change
									(val_mul, ":penalty", 2),
								  (try_end),

								  (try_begin),
									(is_between, ":market_center", centers_begin, centers_end),#changed $g_encountered_party to :market_center
									#Double trade penalty if no local production or consumption
									(is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
									##Begin Change
									#(OPTIONAL CHANGE: Do not apply this to food)
									(this_or_next|eq, ":customer_troop", -2),
									(this_or_next|lt, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
									   (neg|is_between, ":item_kind_id", food_begin, food_end),
									   
									(assign, ":save_reg1", reg1),
									(assign, ":save_reg2", reg2),
									##End Change
									(call_script, "script_center_get_production", ":market_center", ":item_kind_id"),#changed $g_encountered_party to :market_center
									(eq, reg0, 0),
									(call_script, "script_center_get_consumption", ":market_center", ":item_kind_id"),#changed $g_encountered_party to :market_center
									(eq, reg0, 0),
									(val_mul, ":penalty", 2),
									##Begin Change
									(assign, reg1, ":save_reg1"),
									(assign, reg2, ":save_reg2"),
									##End Change
								  (try_end),
								  
								  ## Floris - Trade with Merchant Caravans	## BUG ? CABA - THIS Wasn't writen for these diplo changes...not sure if it is balanced
								  (try_begin),
									(party_is_active, ":market_center"), ## to fix script errors
									(party_slot_eq, ":market_center", slot_party_type, spt_kingdom_caravan),
									(val_mul, ":penalty", 2),
									(party_get_slot, ":center_relation", ":market_center", slot_center_player_relation),
									(store_mul, ":center_relation_penalty", ":center_relation", -3),
									(val_add, ":penalty_multiplier", ":center_relation_penalty"),
									(try_begin),
									  (lt, ":center_relation", 0),
									  (store_sub, ":center_penalty_multiplier", 100, ":center_relation"),
									  (val_mul, ":penalty_multiplier", ":center_penalty_multiplier"),
									  (val_div, ":penalty_multiplier", 100),
									(try_end),
									(is_between, reg60, 2, 6), #Penalty from forcing trade
									(val_mul, ":penalty", reg60),
								  (try_end),
								  ## Floris - Trade with Merchant Caravans	

								  (val_mul, ":penalty",  ":penalty_multiplier"),
								  ##Begin Change
								  (val_add, ":penalty", average_price_factor // 2),#round in the correct direction (we don't need to worry about penalty < 0)
								  (val_div, ":penalty", average_price_factor),#replace the hardcoded constant 1000 with average_price_factor
								  ##End Change
								  (val_max, ":penalty", 1),
								  (assign, reg0, ":penalty"),
							  ]),
							  
							  ##"script_dplmc_print_cultural_word_to_sreg"
							##INPUTS:
							#  arg1  - speaker troop
							#  arg2  - which word/phrase to retrieve (arbitrary code)
							#  arg3  - string register
							#OUTPUTS:
							#  writes result to string register
						   ("dplmc_print_cultural_word_to_sreg", [
							 (store_script_param, ":speaker", 1),
							 (store_script_param, ":context", 2),
							 (store_script_param, ":string_register", 3),

							 #Right now this is entirely faction-based, but you could give different
							 #results for individual lords.
							 #(Note: Now certain parts of it do vary for heroes, to mimic the behavior in Native
							 #feast dialogs for the word for wine.)

							 (assign, ":speaker_faction", -1),
							 (try_begin),
								#Player faction
								(this_or_next|eq, ":speaker", "trp_player"),
									(eq, ":speaker", "trp_kingdom_heroes_including_player_begin"),
								(assign, ":speaker_faction", "fac_player_supporters_faction"),#<- This will potentially get translated later
							 (else_try),
								#Hero original faction
								(is_between, ":speaker", heroes_begin, heroes_end),
								(troop_get_slot, ":speaker_faction", ":speaker", slot_troop_original_faction),
							 (else_try),
								#Hero original faction
								(gt, ":speaker", -1),
								(troop_is_hero, ":speaker"),
								(troop_slot_ge, ":speaker", slot_troop_original_faction, npc_kingdoms_begin),
								(neg|troop_slot_ge, ":speaker", slot_troop_original_faction, npc_kingdoms_end),
								(troop_get_slot, ":speaker_faction", ":speaker", slot_troop_original_faction),
							 (else_try),
								#Troop current faction
								(gt, ":speaker", -1),
								(store_troop_faction, ":speaker_faction", ":speaker"),
							 (try_end),

							 (try_begin),
							  (lt, ":speaker", 1),
							 (else_try),
							   ##Only continue if the current faction isn't associated with a distinctive culture
							   (lt, ":speaker_faction", dplmc_non_generic_factions_begin),
							   ##This will work unless the order of the first factions gets changed
							 (else_try),
							   #Translate raiders into the equivalent kingdoms
							   (is_between, ":speaker", bandits_begin, bandits_end),
							   	##Floris MTT begin
								(try_begin),
									(eq, "$troop_trees", troop_trees_0),
									(assign, ":mountain_bandit", "trp_bandit_n_mountain"),
									(assign, ":forest_bandit", "trp_bandit_n_forest"),
									(assign, ":sea_raider", "trp_bandit_n_sea_raider"),
									(assign, ":steppe_bandit", "trp_bandit_n_steppe"),
									(assign, ":taiga_bandit", "trp_bandit_n_taiga"),
									(assign, ":desert_bandit", "trp_bandit_n_desert"),
								(else_try),
									(eq, "$troop_trees", troop_trees_1),
									(assign, ":mountain_bandit", "trp_bandit_r_mountain"),
									(assign, ":forest_bandit", "trp_bandit_r_forest"),
									(assign, ":sea_raider", "trp_bandit_r_sea_raider"),
									(assign, ":steppe_bandit", "trp_bandit_r_steppe"),
									(assign, ":taiga_bandit", "trp_bandit_r_taiga"),
									(assign, ":desert_bandit", "trp_bandit_r_desert"),
									(else_try),
									(eq, "$troop_trees", troop_trees_2),
									(assign, ":mountain_bandit", "trp_bandit_e_mountain"),
									(assign, ":forest_bandit", "trp_bandit_e_forest"),
									(assign, ":sea_raider", "trp_bandit_e_sea_raider"),
									(assign, ":steppe_bandit", "trp_bandit_e_steppe"),
									(assign, ":taiga_bandit", "trp_bandit_e_taiga"),
									(assign, ":desert_bandit", "trp_bandit_e_desert"),					
								(try_end),
								##Floris MTT end
								 (try_begin),
									(eq, ":speaker", ":mountain_bandit"),#Mountain bandits
									(assign, ":speaker_faction", "fac_kingdom_5"),#Rhodoks
								 (else_try),
									(eq, ":speaker", ":forest_bandit"),#Forest bandits
									(assign, ":speaker_faction", "fac_kingdom_1"),#Swadian
								 (else_try),
									(eq, ":speaker", ":sea_raider"),#Sea raiders
									(assign, ":speaker_faction", "fac_kingdom_4"),#Nords
								 (else_try),
									(eq, ":speaker", ":steppe_bandit"),#Steppe bandits
									(assign, ":speaker_faction", "fac_kingdom_3"),#Khergits
								 (else_try),
									(eq, ":speaker", ":taiga_bandit"),#Taiga bandits
									(assign, ":speaker_faction", "fac_kingdom_2"),#Vaegir
								 (else_try),
									(eq, ":speaker", ":desert_bandit"),#Desert bandits
									(assign, ":speaker_faction", "fac_kingdom_6"),#Sarranid
								 (try_end),
								 (ge, ":speaker_faction", dplmc_non_generic_factions_begin),
							 (else_try),
								#For companions without default initial cultures, infer one from their home.
								#(Actually, don't limit this to companions, since there's a chance that others
								#could have a valid home slot.)
								#(is_between, ":speaker", companions_begin, companions_end),
								#(is_between, ":speaker", heroes_begin, heroes_end),
								(troop_is_hero, ":speaker"),
								(troop_get_slot, ":home_center", ":speaker", slot_troop_home),
								(is_between, ":home_center", centers_begin, centers_end),
								(party_get_slot, ":speaker_faction", ":home_center", slot_center_original_faction),
							 (else_try),
								#For villagers, merchants, etc.
								(eq, ":speaker", "$g_talk_troop"),
								(neg|is_between, ":speaker", heroes_begin, heroes_end),#Not a character that might have an explicitly-set faction
								(neg|is_between, ":speaker", training_gound_trainers_begin, tavern_minstrels_end),#Not a trainer, ransom broker, traveler, bookseller, or minstrel
								(ge, "$g_encountered_party", 0),
								(try_begin),
									#For towns / castles / villages, use the original faction
									(is_between, "$g_encountered_party", centers_begin, centers_end),
									(party_get_slot, ":speaker_faction", "$g_encountered_party", slot_center_original_faction),
								(else_try),
									#Use faction of encountered party
									(party_is_active, "$g_encountered_party"),
									(store_faction_of_party, ":speaker_faction", "$g_encountered_party"),
									#For generic factions, use the closest center
									(lt, ":speaker_faction", dplmc_non_generic_factions_begin),
									(assign, ":speaker_faction", reg0),#save register
									(call_script, "script_get_closest_center", "$g_encountered_party"),
									(assign, ":home_center", reg0),
									(assign, reg0, ":speaker_faction"),#revert register
									(party_get_slot, ":speaker_faction", ":home_center", slot_center_original_faction),
								(try_end),
							 (try_end),

							#Translate for player's kingdom
							 (try_begin),
								(ge, "$players_kingdom", dplmc_non_generic_factions_begin),
								(this_or_next|eq, ":speaker_faction", "fac_player_faction"),
								(this_or_next|eq, ":speaker_faction", "fac_player_supporters_faction"),
								(eq, ":speaker_faction", "$players_kingdom"),
								(assign, ":speaker_faction", "$players_kingdom"),
								(neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
								(this_or_next|is_between, "$g_player_culture", cultures_begin, cultures_end),
								(is_between,"$g_player_culture", npc_kingdoms_begin, npc_kingdoms_end),
								(assign, ":speaker_faction", "$g_player_culture"),
							 (try_end),

							 #Store variant
							 (try_begin),
								#Iconic cultural weapon that can be used metonymously for force of arms.
								#Native equivalent is "sword".
								#Non-Warband example: "He who lives by the {sword}, dies by the {sword}."
								#Example usage: "My {sword} is at the disposal of my liege."
								(eq, ":context", DPLMC_CULTURAL_TERM_WEAPON),
								(try_begin),
								   (this_or_next|eq, ":speaker_faction", "fac_kingdom_4"),#Nords
								   (eq, ":speaker_faction", "fac_kingdom_2"),#Vaegirs
								   (str_store_string, ":string_register", "@axe"),
								(else_try),
								   (eq, ":speaker_faction", "fac_kingdom_5"),#Rhodoks
								   (str_store_string, ":string_register", "@spear"),
								(else_try),
								   (eq, ":speaker_faction", "fac_kingdom_3"),#Khergits
								   (str_store_string, ":string_register", "@bow"),
								(else_try),
									#Default: Swadia, Sarranid, others
								   (str_store_string, ":string_register", "@sword"),
								(try_end),
							(else_try),
								#Plural version of iconic cultural weapon that can be used metonymously for force of arms.
								#Native equivalent is "swords".
								(eq, ":context", DPLMC_CULTURAL_TERM_WEAPON_PLURAL),
								(try_begin),
								   (this_or_next|eq, ":speaker_faction", "fac_kingdom_4"),#Nords
								   (eq, ":speaker_faction", "fac_kingdom_2"),#Vaegirs
								   (str_store_string, ":string_register", "@axes"),
								(else_try),
								   (eq, ":speaker_faction", "fac_kingdom_5"),#Rhodoks
								   (str_store_string, ":string_register", "@spears"),
								(else_try),
								   (eq, ":speaker_faction", "fac_kingdom_3"),#Khergits
								   (str_store_string, ":string_register", "@bows"),
								(else_try),
									#Default: Swadia, Sarranid, others
								   (str_store_string, ":string_register", "@swords"),
								(try_end),
							 (else_try),
								#Cultural phrase that means "fight" (first person singular)
								#Native equivalent is "swing my sword."
								#Example usage: "I want to be able to {swing my sword} with a good conscience."
								(eq, ":context", DPLMC_CULTURAL_TERM_USE_MY_WEAPON),
								(try_begin),
								   (eq, ":speaker_faction", "fac_kingdom_4"),#Nords
								   (eq, ":speaker_faction", "fac_kingdom_2"),#Vaegirs
								   (str_store_string, ":string_register", "@swing my axe"),
								(else_try),
								   (eq, ":speaker_faction", "fac_kingdom_5"),#Rhodoks
								   (str_store_string, ":string_register", "@lift my spear"),
								(else_try),
								   (eq, ":speaker_faction", "fac_kingdom_3"),#Khergits
								   (str_store_string, ":string_register", "@loose my arrows"),
								(else_try),
									#Default: Swadia, Sarranid, others
								   (str_store_string, ":string_register", "@swing my sword"),
								(try_end),
							(else_try),
								#equivalent to lowercase "king" or "queen"
								(this_or_next|eq, ":context", DPLMC_CULTURAL_TERM_KING_FEMALE),
								(eq, ":context", DPLMC_CULTURAL_TERM_KING),
								(try_begin),
								   (eq, ":speaker_faction", "fac_kingdom_3"),#Khergit
								   (str_store_string, ":string_register", "str_khan"),
								(else_try),
								   (eq, ":speaker_faction", "fac_kingdom_6"),#Sarranid
								   (str_store_string, ":string_register", "@sultan"),
								(else_try),
								   #Default: Swadia, Rhodok, Nord, Vaegir, others
								   (str_store_string, ":string_register", "str_king"),
								   (eq, ":context", DPLMC_CULTURAL_TERM_KING_FEMALE),
								   (str_store_string, ":string_register", "str_queen"),
								(try_end),
							(else_try),
								#equivalent to lowercase "kings"
								(eq, ":context", DPLMC_CULTURAL_TERM_KING_PLURAL),
								(try_begin),
								   (eq, ":speaker_faction", "fac_kingdom_3"),#Khergit
								   (str_store_string, ":string_register", "@khans"),
								(else_try),
								   (eq, ":speaker_faction", "fac_kingdom_6"),#Sarranid
								   (str_store_string, ":string_register", "@sultans"),
								(else_try),
								   #Default: Swadia, Rhodok, Nord, Vaegir, others
								   (str_store_string, ":string_register", "@kings"),
								(try_end),
							(else_try),
								#equivalent to lowercase "lord"
								(eq, ":context", DPLMC_CULTURAL_TERM_LORD),
							   (str_store_string, ":string_register", "@lord"),
							(else_try),
								#equivalent to lowercase "lords"
								(eq, ":context", DPLMC_CULTURAL_TERM_LORD_PLURAL),
								(str_store_string, ":string_register", "@lords"),
							(else_try),
								#As in, "I shall tell my {swineherd} about your sweet promises" or "Any {swineherd} can claim to be king".
								(eq, ":context", DPLMC_CULTURAL_TERM_SWINEHERD),
								(assign, ":mode", ":speaker"),
								(try_begin),
								   (gt, ":speaker", 0),
								   (neg|troop_is_hero, ":speaker"),
								   (store_current_hours, ":mode"),
								   (val_add, ":mode", "$g_encountered_party"),
								(try_end),
								(val_max, ":mode", 0),#Default to mode 0 for negative speakers
								(val_mod, ":mode", 2),
								(try_begin),
								   (eq, ":speaker_faction", "fac_kingdom_2"),#Vaegirs
								   (try_begin),
									  (eq, ":mode", 0),
									  (str_store_string, ":string_register", "@goatherd"),
								   (else_try),
									   (str_store_string, ":string_register", "@swineherd"),
								   (try_end),
								(else_try),
								   (eq, ":speaker_faction", "fac_kingdom_3"),#Khergits
								   (try_begin),
									  (eq, ":mode", 0),
									  (str_store_string, ":string_register", "@stable {boy/girl}"),
								(else_try),
									  (str_store_string, ":string_register", "@shepherd {boy/girl}"),
								   (try_end),
								(else_try),
								   (eq, ":speaker_faction", "fac_kingdom_6"),#Sarranids
								   (try_begin),
									  (eq, ":mode", 0),
									  (str_store_string, ":string_register", "@goatherd"),
								   (else_try),
									  (str_store_string, ":string_register", "@shepherd {boy/girl}"),
								   (try_end),
								(else_try),
								   #Swadia, Rhodok, Nord, others
								   (str_store_string, ":string_register", "@swineherd"),
								(try_end),
							(else_try),
								#As in, "I'd like to buy every man who comes in here tonight a jar of your best wine."
								(this_or_next|eq, ":context", DPLMC_CULTURAL_TERM_TAVERNWINE),
								#Follow the pattern used in Native for lords in feasts
								#(c.f. "str_flagon_of_mead", "str_skin_of_kumis", "str_mug_of_kvass", "str_cup_of_wine")

								(try_begin),
									#For lords, use "mode" so it works the same as in feast dialogs
									(is_between, ":speaker", heroes_begin, heroes_end),
									(this_or_next|neg|is_between, ":speaker", companions_begin, companions_end),
										(neg|troop_slot_eq, ":speaker", slot_troop_original_faction, ":speaker_faction"),
									(store_mod, ":mode", ":speaker", 2),
								(else_try),
									#Otherwise set mode to 0, to always use the cultural alternative
									(assign, ":mode", 0),
								(try_end),

								(try_begin),
									(eq, ":speaker_faction", "fac_kingdom_2"),
									(eq, ":mode", 0),#From feast: 50% chance of falling through to "wine"
									(str_store_string, ":string_register", "@kvass"),#Vaegirs: kvass
								(else_try),
									(eq, ":speaker_faction", "fac_kingdom_3"),
									(eq, ":mode", 0),#From feast: 50% chance of falling through to "wine"
									(str_store_string, ":string_register", "@kumis"),#Khergits: kumis
								(else_try),
									(eq, ":speaker_faction", "fac_kingdom_4"),
									(str_store_string, ":string_register", "@mead"),#Nords: mead
								(else_try),
									(str_store_string, ":string_register", "@wine"),#Default: wine
								(try_end),
							(else_try),
							#Error string
								(assign, ":save_reg0", reg0),
								(assign, reg0, ":context"),
								(display_message, "@{!}ERROR - dplmc_print_cultural_word_to_sreg called for bad context {reg0}"),
								(str_store_string, ":string_register", "str_ERROR_string"),
								(assign, reg0, ":save_reg0"),
							(try_end),

						   ]),
							   
							   
							  #script_dplmc_print_player_spouse_says_my_husband_wife_to_s0
							  #
							  #INPUT:
							  #  arg1: troop_no
							  #  arg2: whether the first letter must be capitalized
							  #
							  #OUTPUT:
							  #    s0: a string that can be substituted for "my {husband/wife}" or "my love"
							  ("dplmc_print_player_spouse_says_my_husband_wife_to_s0",
							   [
								 (store_script_param_1, ":troop_no"),
								 (store_script_param_2, ":capitalized"),
								 
								 (assign, ":save_reg0", reg0),
								 (assign, ":save_reg6", reg6),
								 (assign, ":save_reg7", reg7),
								 #(assign, reg6, ":capitalized"),
								 (assign, reg7, 0),
								 
								#Base switch is 50 (i.e. where the "brave champion" greeting starts)
								(try_begin),
								  (lt, ":troop_no", 1),#bad value
								  (assign, reg0, 0),
								  (assign, reg6, lrep_none),
								(else_try),
								   (call_script, "script_troop_get_player_relation", ":troop_no"),#write relation to reg0
								  (troop_get_slot, reg6, ":troop_no", slot_lord_reputation_type),#write relation to reg6
								  (eq, reg6, lrep_conventional),#...jumps to next branch (keeping reg0 and reg6) if this isn't true
									(val_add, reg0, 25),#from 25+
								 (else_try),
								  (eq, reg6, lrep_otherworldly),
									(val_add, reg0, 30),#from 20+
								 (else_try),
								  (eq, reg6, lrep_moralist),
								  (store_sub, reg7, "$player_honor", 10),
								  (val_clamp, reg7, -40, 31),
								  (val_add, reg0, reg7),
								  (assign, reg7, 0),
								(else_try),
								  (eq, reg6, lrep_ambitious),
								  (assign, reg7, -10),
								  (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
									 (this_or_next|party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
										(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
									 (val_add, reg7, 10),
									 (party_slot_eq, ":center_no", slot_party_type, spt_town),
									 (val_add, reg7,  10),
								  (try_end),
								  (val_clamp, reg7, -10, 30),
								  (val_add, reg0, reg7),
								  (assign, reg7, 0),
								(else_try),
								  (eq, reg6, lrep_adventurous),
								  (val_add, reg7, 20),#from 30+
								(else_try),
								  (eq, reg6, lrep_none),
								  (is_between, reg6, heroes_begin, heroes_end),
								  (val_sub, reg0, 20),#from 70+
								(else_try),
								  (eq, reg6, lrep_cunning),
								  (val_sub, reg0, 20),#from 70+
								(else_try),
								  (this_or_next|eq, reg6, lrep_debauched),
								  (this_or_next|eq, reg6, lrep_quarrelsome),
								  (this_or_next|eq, reg6, lrep_selfrighteous),
								  (val_sub, reg0, 30),#from 80+
								 (try_end),

								(try_begin),
								   (ge, reg0, 50),
								   (assign, reg7, 1),
								(try_end),
								
								(try_begin),
								   #Embellishment: diminuitive pet-names
								   (eq, reg6, lrep_debauched),
								   (gt, ":troop_no", 0),
								   (store_character_level, ":player_level", "trp_player"),
								   (store_character_level, ":troop_level", ":troop_no"),
								   (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
								   (this_or_next|ge, ":troop_level", ":player_level"),
								   (this_or_next|troop_slot_ge, ":troop_no", slot_troop_renown, ":player_renown"),
									  (lt, reg0, 50),
								   (assign, reg6, ":capitalized"),#Whether the first letter needs to be upper case
								   (str_store_string, s0, "@{reg6?M:m}y poppet"),
								(else_try),
								   #The basic idea.  Further embellishments may come.
								   (assign, reg6, ":capitalized"),#Whether the first letter needs to be upper case
								   (str_store_string, s0, "str_dplmc_reg6my_reg7spouse"),
								(try_end),

								 #Revert registers
								 (assign, reg0, ":save_reg0"),
								 (assign, reg6, ":save_reg6"),
								 (assign, reg7, ":save_reg7"),
							   ]),
							  
					  
							  ##"script_dplmc_get_troop_standing_in_faction"
							#
							#INPUT: arg1  :troop_no
							#       arg2  :faction_no
							#
							#OUTPUT:
							#       reg0  A constant with the value DPLMC_FACTION_STANDING_<something>
							#
							## Constants defined in module_constants.py
							#DPLMC_FACTION_STANDING_LEADER = 60
							#DPLMC_FACTION_STANDING_LEADER_SPOUSE = 50
							#DPLMC_FACTION_STANDING_MARSHALL = 40
							#DPLMC_FACTION_STANDING_LORD = 30
							#DPLMC_FACTION_STANDING_DEPENDENT = 20
							#DPLMC_FACTION_STANDING_MEMBER = 10#includes mercenaries 
							#DPLMC_FACTION_STANDING_PETITIONER = 5
							#DPLMC_FACTION_STANDING_UNAFFILIATED = 0
							##diplomacy end+
							 ("dplmc_get_troop_standing_in_faction",
							 [
								(store_script_param_1, ":troop_no"),
								(store_script_param_2, ":faction_no"),

								(assign, ":standing", DPLMC_FACTION_STANDING_UNAFFILIATED),
								(assign, ":original_faction_no", ":faction_no"),
								(try_begin),
									#Translate fac_player_faction
									(eq, ":faction_no", "fac_player_faction"),
									(assign, ":faction_no", "fac_player_supporters_faction"),
								(try_end),

								(try_begin),
								   (this_or_next|lt, ":troop_no", 0),#Do nothing, bad troop ID
									  (lt, ":faction_no", 0),#Do nothing, bad faction
								(else_try),
								   #Because of how this script is used, if fac_player_supporters_faction is active,
								   # this always reports that the player is its leader (even though that is sometimes
								   # untrue, for example in a claimant quest)
								   (eq, ":troop_no", "trp_player"),#Short-circuit the remainder if these are true
								   (eq, ":faction_no", "fac_player_supporters_faction"),
								   (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
								   (assign, ":standing", DPLMC_FACTION_STANDING_LEADER),
								(else_try),
									(try_begin),
										#Translate fac_player_supporters_faction
										(eq, ":faction_no", "fac_player_supporters_faction"),
										(gt, "$players_kingdom", 0),
										(assign, ":faction_no", "$players_kingdom"),
									(try_end),

									(store_faction_of_troop, ":troop_faction", ":troop_no"),
									(try_begin),
									   #Translate fac_player_supporters_faction
									   (this_or_next|eq, ":troop_no", "trp_player"),
									   (this_or_next|eq, ":troop_faction", "fac_player_faction"),
										  (eq, ":troop_faction", "fac_player_supporters_faction"),
									   (assign, ":troop_faction", "fac_player_supporters_faction"),
									   (gt, "$players_kingdom", 0),
									   (assign, ":troop_faction", "$players_kingdom"),
									(try_end),
									(eq, ":troop_faction", ":faction_no"),#<- Short-circuit the remainder if this is false
									(assign, ":standing", DPLMC_FACTION_STANDING_MEMBER),

									(faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
									(try_begin),
									   #Faction leader
									   (eq, ":faction_leader", ":troop_no"),
									   (assign, ":standing", DPLMC_FACTION_STANDING_LEADER),
									(else_try),
									   #Spouse of faction leader
									   (gt, ":faction_leader", -1),
									   (this_or_next|troop_slot_eq, ":troop_no", slot_troop_spouse, ":faction_leader"),
										  (troop_slot_eq, ":faction_leader", slot_troop_spouse, ":troop_no"),
									   #Deal with possible uninitialized slot
									   (this_or_next|troop_slot_eq, ":faction_leader", slot_troop_spouse, ":troop_no"),
									   (this_or_next|neq, ":faction_leader", 0),
										  (is_between, ":troop_no", heroes_begin, heroes_end),
									   (assign, ":standing", DPLMC_FACTION_STANDING_LEADER_SPOUSE),
									(else_try),
									   #Faction marshall
									   (faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
									   (assign, ":standing", DPLMC_FACTION_STANDING_MARSHALL),
									(else_try),
									   #If the troop is the player, if he has homage he is a lord.
									   #Otherwise he is a mercenary.
									   (eq, ":troop_no", "trp_player"),
									   (try_begin),
										  (this_or_next|eq, ":faction_no", "fac_player_supporters_faction"),
										  (ge, "$player_has_homage", 1),
										  (assign, ":standing", DPLMC_FACTION_STANDING_LORD),
									   (else_try),
										  #If the player is married to a lord/lady in the faction, the
										  #homage variable should always be set to 1+, but add a separate
										  #check just in case.
										  (troop_get_slot, reg0, "trp_player", slot_troop_spouse),
										  (is_between, reg0, heroes_begin, heroes_end),
										  (store_faction_of_troop, reg0, reg0),
										  (this_or_next|eq, reg0, "fac_player_supporters_faction"),
										  (eq, reg0, ":faction_no"),
										  (assign, ":standing", DPLMC_FACTION_STANDING_LORD),
									   (try_end),
									(else_try),
										#None of the following conditions apply for non-heroes
										(this_or_next|lt, ":troop_no", heroes_begin),
											(neg|troop_is_hero, ":troop_no"),
									(else_try),
									   #For kingdom heroes, part 1 (check lordship based on occupation)
									   (this_or_next|troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
									   (this_or_next|troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_lord_rejoined),
									   (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
									   (assign, ":standing", DPLMC_FACTION_STANDING_LORD),
									(else_try),
									   #For kingdom ladies
									   (this_or_next|is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
										  (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_lady),
									   (assign, ":standing", DPLMC_FACTION_STANDING_DEPENDENT),
									(else_try),
									   #For petitioners
									   (eq, ":original_faction_no", "fac_player_supporters_faction"),
									   (is_between, ":troop_no", lords_begin, lords_end),
									   (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive),
									   (neg|troop_slot_ge, ":troop_no", slot_troop_leaded_party, 0),
									   (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
									   (assign, ":standing", DPLMC_FACTION_STANDING_PETITIONER),
									(else_try),
										#For kingdom heroes, part 2 (all non-companion active NPCs)
										(is_between, ":troop_no", active_npcs_begin, active_npcs_end),
										(neg|is_between, ":troop_no", companions_begin, companions_end),
										(assign, ":standing", DPLMC_FACTION_STANDING_LORD),
									(try_end),
								(try_end),

								(assign, reg0,  ":standing"),
							 ]),

							 ## ""script_dplmc_store_troop_is_eligible_for_affiliate_messages"
							 ("dplmc_store_troop_is_eligible_for_affiliate_messages",
							 [
								(store_script_param_1, ":troop_no"),
								(assign, ":is_eligible", 0),
								(assign, ":save_reg1", reg1),
								(try_begin),
									(lt, ":troop_no", 1),
								(else_try),
									(neg|troop_is_hero, ":troop_no"),
								(else_try),
									#Initialize :faction_no and :faction_relation
									(store_faction_of_troop, ":faction_no", ":troop_no"),
									(store_relation, ":faction_relation", ":faction_no", "fac_player_supporters_faction"),
									(try_begin),
										(eq, ":faction_no", "$players_kingdom"),
										(val_max, ":faction_relation", 1),
									(try_end),
									#Companion
									(gt, ":faction_relation", -1),
									(is_between, ":troop_no", companions_begin, companions_end),
									(neg|troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
									(troop_slot_ge, ":troop_no", slot_troop_player_relation, 20),
									(assign, ":is_eligible", 1),
								(else_try),
									#Faction marshall (if the player is the faction leader)
									#Faction leader (if the player is the faction marshall)
									(eq, ":faction_no", "$players_kingdom"),
									(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
									(ge, reg0, DPLMC_FACTION_STANDING_MARSHALL),
									(call_script, "script_dplmc_get_troop_standing_in_faction", ":troop_no", "$players_kingdom"),
									(ge, reg0, DPLMC_FACTION_STANDING_MARSHALL),
									(assign, ":is_eligible", 1),
								(else_try),
									#Spouse / relatives / in-laws
									(gt, ":faction_relation", -1),
									#(is_between, ":troop_no", heroes_begin, heroes_end),## should be safe even for non-heroes
									(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":troop_no", "trp_player"),
									(ge, reg0, 2),
									(troop_get_slot, reg1, ":troop_no", slot_troop_player_relation),
									(val_add, reg0, reg1),
									(ge, reg0, 20),
									(assign, ":is_eligible", 1),
								(else_try),
									#Affiliates
									(call_script, "script_dplmc_is_affiliated_family_member", ":troop_no"),
									(ge, reg0, 1),
									(assign, ":is_eligible", 1),
								(else_try),
									#Cheat mode: add faction leaders to test this out
									(gt, "$cheat_mode", 0),
									(is_between, ":faction_no", kingdoms_begin, kingdoms_end),
									(faction_slot_eq, ":faction_no", slot_faction_leader, ":troop_no"),
									(assign, ":is_eligible", 1),
								(try_end),
								(assign, reg1, ":save_reg1"),
								(assign, reg0, ":is_eligible"),
							 ]),
							 
							# "script_dplmc_sell_all_prisoners"
							#
							# Taken from rubik's Custom Commander, and altered to have parameters
							# and return feedback.
							#
							#INPUT:
							#Arg 1: actually remove (0 for no)
							#Arg 2: if non-zero, use this as a fixed price instead of calculating dynamically
							#OUTPUT:
							#reg0: amount of gold gained (or would have been gained if the sale occurred)
							#reg1: number of prisoners sold (or would have been sold if the sale occurred)
						  ("dplmc_sell_all_prisoners",
						   [
							(store_script_param_1, ":actually_remove"),
							(store_script_param_2, ":fixed_price"),

							 (assign, ":total_removed", 0),
							(assign, ":total_income", 0),
							(party_get_num_prisoner_stacks, ":num_stacks", "p_main_party"),
							(try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
							  (party_prisoner_stack_get_troop_id, ":troop_no", "p_main_party", ":i_stack"),
							  (neg|troop_is_hero, ":troop_no"),
							  (party_prisoner_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),
							  (try_begin),
								 (gt, ":fixed_price", 0),
								 (assign, ":sell_price", ":fixed_price"),
							  (else_try),
								 (call_script, "script_game_get_prisoner_price", ":troop_no"),
								 (assign, ":sell_price", reg0),
							  (try_end),
							  (store_mul, ":stack_total_price", ":sell_price", ":stack_size"),
							  (val_add, ":total_income", ":stack_total_price"),
							  (val_add, ":total_removed", ":stack_size"),
							  (gt, ":actually_remove", 0),#Stop short if this is a dry run
							  (party_remove_prisoners, "p_main_party", ":troop_no", ":stack_size"),
							(try_end),
							 (try_begin),
							   (gt, ":actually_remove", 0),#Stop short if this is a dry run
							   (troop_add_gold, "trp_player", ":total_income"),
							 (try_end),
							 (assign, reg0, ":total_income"),
							 (assign, reg1, ":total_removed"),
						  ]),
							  
							  #"script_dplmc_translate_inactive_player_supporter_faction_2"
							#
							#Since "fac_player_supporters_faction" is often used as a parameter when what
							#is really meant is "the faction led by the player" (which is never a different
							#faction in Native), there are many calls we want to change.  Another solution
							#is to approach the problem from the other side, and "correct" the arguments.
							#
							#If exactly one argument is equal to fac_player_supporters_faction, and fac_player_supporters_faction
							#is not sfs_active, and $players_kingdom is an NPC kingdom of which the player is ruler or co-ruler,
							#and the other argument is not equal to $players_kingdom, then the argument equal to fac_player_supporters_faction
							#will be replaced with $players_kingdom.
							#
							#INPUT:
							# arg1 - faction_1
							# arg2 - faction_2
							#OUTPUT:
							# reg0 - faction_1, possibly replacing fac_player_supporters_faction with $players_kingdom (see above)
							# reg1 - faction_2, possibly replacing fac_player_supporters_faction with $players_kingdom (see above)
							("dplmc_translate_inactive_player_supporter_faction_2",
							[
								(store_script_param_1, ":faction_1"),
								(store_script_param_2, ":faction_2"),

								(try_begin),
									(this_or_next|faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
									(this_or_next|neg|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
									(this_or_next|eq, ":faction_1", "$players_kingdom"),
									(this_or_next|eq, ":faction_2", "$players_kingdom"),
										(eq, ":faction_1", ":faction_2"),
								  #Do nothing
								(else_try),
									(eq, ":faction_1", "fac_player_supporters_faction"),
									(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
									(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
									(assign, ":faction_1", "$players_kingdom"),
								(else_try),
									(eq, ":faction_2", "fac_player_supporters_faction"),
									(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
									(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
									(assign, ":faction_2", "$players_kingdom"),
								(try_end),
								
								(assign, reg0, ":faction_1"),
								(assign, reg1, ":faction_2"),
							]),

				  
						  ##"script_dplmc_troop_get_family_relation_to_troop"
						##
						##Like troop_get_family_relation_to_troop, except instead of writing to s11,
						##it writes the index of the relation string to reg1, and writes nothing at
						##all to reg4.
						  ("dplmc_troop_get_family_relation_to_troop",
							[
							(store_script_param_1, ":troop_1"),
							(store_script_param_2, ":troop_2"),

							##dplmc start+
							
							(try_begin),
								(eq, ":troop_1", active_npcs_including_player_begin),
								(assign, ":troop_1", "trp_player"),
							(try_end),
							(try_begin),
								(eq, ":troop_2", active_npcs_including_player_begin),
								(assign, ":troop_2", "trp_player"),
							(try_end),
							
							#use gender script
							#(troop_get_type, ":gender_1", ":troop_1"),
							(call_script, "script_dplmc_store_troop_is_female", ":troop_1"),
							(assign, ":gender_1", reg0),
							(assign, ":relation_string", "str_no_relation"),
							##dplmc end+
							(assign, ":relation_strength", 0),
							
							##dplmc start+
							#Uninitialized memory is 0, which equals "trp_player", which is the cause
							#of some annoying bugs.  In Native the game doesn't set the various family
							#slots to -1 except for the player and in the heroes_begin to heroes_end
							#range.
							
							(troop_get_slot, ":spouse_of_1", ":troop_1", slot_troop_spouse),#just do this to get an error if the troop ID is bad
							(troop_get_slot, ":spouse_of_2", ":troop_2", slot_troop_spouse),#just do this to get an error if the troop ID is bad
							
							(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":troop_1", ":troop_2", slot_troop_spouse),
							(assign, ":spouse_of_1", reg0),
							(assign, ":spouse_of_2", reg1),

							(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":spouse_of_1", ":spouse_of_2", slot_troop_father),
							(assign, ":father_of_spouse_of_1", reg0),
							(assign, ":father_of_spouse_of_2", reg1),
							
							(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":spouse_of_1", ":spouse_of_2", slot_troop_mother),
							#(assign, ":mother_of_spouse_of_1", reg0),
							(assign, ":mother_of_spouse_of_2", reg1),
							
							(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":troop_1", ":troop_2", slot_troop_father),
							(assign, ":father_of_1", reg0),
							(assign, ":father_of_2", reg1),
							
							(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":troop_1", ":troop_2", slot_troop_mother),
							(assign, ":mother_of_1", reg0),
							(assign, ":mother_of_2", reg1),
							
							(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":father_of_1", ":father_of_2", slot_troop_father),
							(assign, ":paternal_grandfather_of_1", reg0),
							(assign, ":paternal_grandfather_of_2", reg1),
							
							(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":father_of_1", ":father_of_2", slot_troop_mother),
							(assign, ":paternal_grandmother_of_1", reg0),
							(assign, ":paternal_grandmother_of_2", reg1),
							
							(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":mother_of_1", ":mother_of_2", slot_troop_father),
							(assign, ":maternal_grandfather_of_1", reg0),
							(assign, ":maternal_grandfather_of_2", reg1),
							
							(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":mother_of_1", ":mother_of_2", slot_troop_mother),
							(assign, ":maternal_grandmother_of_1", reg0),
							(assign, ":maternal_grandmother_of_2", reg1),
							
							(call_script, "script_dplmc_helper_get_troop1_troop2_family_slot_aux", ":troop_1", ":troop_2", slot_troop_guardian),
							(assign, ":guardian_of_1", reg0),
							(assign, ":guardian_of_2", reg1),
							##diplomacy end+

							#(str_store_string, s11, "str_no_relation"),

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
								(assign, ":relation_string", "str_wife"),
							  (else_try),
								(assign, ":relation_string", "str_husband"),
							  (try_end),
							(else_try),
							  (eq, ":father_of_2", ":troop_1"),
							  (assign, ":relation_strength", 15),
							  (assign, ":relation_string", "str_father"),
							(else_try),
							  (eq, ":mother_of_2", ":troop_1"),
							  (assign, ":relation_strength", 15),
							  (assign, ":relation_string", "str_mother"),
							(else_try),
							  (this_or_next|eq, ":father_of_1", ":troop_2"),
							  (eq, ":mother_of_1", ":troop_2"),
							  (assign, ":relation_strength", 15),
							  (try_begin),
								(eq, ":gender_1", 1),
								(assign, ":relation_string", "str_daughter"),
							  (else_try),
								(assign, ":relation_string", "str_son"),
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
								 (assign, ":relation_string", "str_dplmc_half_sister"),
							   (else_try),
								 (assign, ":relation_string", "str_dplmc_half_brother"),
							   (try_end),
						   (else_try),
							   #Check for half-siblings: sharing a mother
							   (neq, ":mother_of_1", -1),
							   (eq, ":mother_of_1", ":mother_of_2"),
							   (neq, ":father_of_1", ":father_of_2"),
							   (assign, ":relation_strength", 10),
							   (try_begin),
								 (eq, ":gender_1", 1),
								 (assign, ":relation_string", "str_dplmc_half_sister"),
							   (else_try),
								 (assign, ":relation_string", "str_dplmc_half_brother"),
							   (try_end),
							##diplomacy end+
							(else_try),
							  #(gt, ":father_of_1", -1), #necessary, as some lords do not have the father registered #dplmc+ replaced
							  (neq, ":father_of_1", -1), #dplmc+ added
							  (eq, ":father_of_1", ":father_of_2"),
							  (assign, ":relation_strength", 10),
							  (try_begin),
								(eq, ":gender_1", 1),
								(assign, ":relation_string", "str_sister"),
							  (else_try),
								(assign, ":relation_string", "str_brother"),
							  (try_end),
							(else_try),
							  (eq, ":guardian_of_2", ":troop_1"),
							  (assign, ":relation_strength", 10),
							  (try_begin),
								(eq, ":gender_1", 1),
								(assign, ":relation_string", "str_sister"),
							  (else_try),
								(assign, ":relation_string", "str_brother"),
							  (try_end),
							(else_try),
							  (eq, ":guardian_of_1", ":troop_2"),
							  (assign, ":relation_strength", 10),
							  (try_begin),
								(eq, ":gender_1", 1),
								(assign, ":relation_string", "str_sister"),
							  (else_try),
								(assign, ":relation_string", "str_brother"),
							  (try_end),
							##diplomacy start+
							(else_try),#polygamy, between two people married to the same person
							   (neq, ":spouse_of_1", -1),
							   (eq, ":spouse_of_2", ":spouse_of_1"),
							   (assign, ":relation_strength", 10),
							   (try_begin),
								  (call_script, "script_dplmc_store_troop_is_female", ":troop_2"),
								  (neq, ":gender_1", reg0),
								  (assign, ":relation_string", "str_dplmc_co_spouse"),
							   (else_try),
								  (eq, ":gender_1", 1),
								 (assign, ":relation_string", "str_dplmc_sister_wife"),
							   (else_try),
								  (assign, ":relation_string", "str_dplmc_co_husband"),
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
								(assign, ":relation_string", "str_niece"),
							  (else_try),
								(assign, ":relation_string", "str_nephew"),
							  (try_end),
							##diplomacy start+: add niece/nephew through mother
							(else_try),
							  (neq, ":mother_of_2", -1),
							  (this_or_next|eq, ":maternal_grandmother_of_1", ":mother_of_2"),
							  (eq, ":paternal_grandmother_of_1", ":mother_of_2"),
							  (assign, ":relation_strength", 4),
							  (try_begin),
								(eq, ":gender_1", 1),
								(assign, ":relation_string", "str_niece"),
							  (else_try),
								(assign, ":relation_string", "str_nephew"),
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
								(assign, ":relation_string", "str_aunt"),
							  (else_try),
								(assign, ":relation_string", "str_uncle"),
							  (try_end),
							##diplomacy start+
							#blood uncles & blood aunts, continued (via mother)
							(else_try),
							  (neq, ":mother_of_1", -1),
							  (this_or_next|eq, ":maternal_grandmother_of_2", ":mother_of_1"),
							  (eq, ":paternal_grandmother_of_2", ":mother_of_1"),
							  (assign, ":relation_strength", 4),
							  (try_begin),
								(eq, ":gender_1", 1),
								(assign, ":relation_string", "str_aunt"),
							  (else_try),
								(assign, ":relation_string", "str_uncle"),
							  (try_end),
							##diplomacy end+
							(else_try),
							  #(gt, ":paternal_grandfather_of_1", 0),#dplmc+ replaced (why was this one "gt 0" but the previous "gt -1"?)
							  (neq, ":paternal_grandfather_of_1", -1),#dplmc+ added
							  (this_or_next|eq, ":maternal_grandfather_of_2", ":paternal_grandfather_of_1"),#dplmc+ added
							  (eq, ":paternal_grandfather_of_2", ":paternal_grandfather_of_1"),
							  (assign, ":relation_strength", 2),
							  (assign, ":relation_string", "str_cousin"),
							##diplomacy start+
							#Add cousin via paternal grandmother or maternal grandparents
							(else_try),
							  (neq, ":maternal_grandfather_of_1", -1),
							  (this_or_next|eq, ":maternal_grandfather_of_2", ":maternal_grandfather_of_1"),
							  (eq, ":paternal_grandfather_of_2", ":maternal_grandfather_of_1"),
							  (assign, ":relation_strength", 2),
							  (assign, ":relation_string", "str_cousin"),
							(else_try),
							  (neq, ":paternal_grandmother_of_1", -1),
							  (this_or_next|eq, ":maternal_grandmother_of_2", ":paternal_grandmother_of_1"),
							  (eq, ":paternal_grandmother_of_2", ":paternal_grandmother_of_1"),
							  (assign, ":relation_strength", 2),
							  (assign, ":relation_string", "str_cousin"),
							(else_try),
							  (neq, ":maternal_grandmother_of_1", -1),
							  (this_or_next|eq, ":maternal_grandmother_of_2", ":maternal_grandmother_of_1"),
							  (eq, ":paternal_grandmother_of_2", ":maternal_grandmother_of_1"),
							  (assign, ":relation_strength", 2),
							  (assign, ":relation_string", "str_cousin"),
							##diplomacy end+
							(else_try),
							  (eq, ":father_of_spouse_of_1", ":troop_2"),
							  (assign, ":relation_strength", 5),
							  (try_begin),
								(eq, ":gender_1", 1),
								(assign, ":relation_string", "str_daughterinlaw"),
							  (else_try),
								(assign, ":relation_string", "str_soninlaw"),
							  (try_end),
							(else_try),
							  (eq, ":father_of_spouse_of_2", ":troop_1"),
							  (assign, ":relation_strength", 5),
							  (assign, ":relation_string", "str_fatherinlaw"),
							(else_try),
							  (eq, ":mother_of_spouse_of_2", ":troop_1"),
							  (neq, ":mother_of_spouse_of_2", "trp_player"), #May be necessary if mother for troops not set to -1
							  (assign, ":relation_strength", 5),
							  (assign, ":relation_string", "str_motherinlaw"),

							(else_try),
							  #(gt, ":father_of_spouse_of_1", -1), #necessary #dplmc+ replaced
							  (neq, ":father_of_spouse_of_1", -1), #dplmc+ added
							  (eq, ":father_of_spouse_of_1", ":father_of_2"),
							  (assign, ":relation_strength", 5),
							  (try_begin),
								(eq, ":gender_1", 1),
								(assign, ":relation_string", "str_sisterinlaw"),
							  (else_try),
								(assign, ":relation_string", "str_brotherinlaw"),
							  (try_end),
							(else_try),
							  #(gt, ":father_of_spouse_of_2", -1), #necessary #dplmc+ replaced
							  (neq, ":father_of_spouse_of_2", -1), #dplmc+ added
							  (eq, ":father_of_spouse_of_2", ":father_of_1"),
							  (assign, ":relation_strength", 5),
							  (try_begin),
								(eq, ":gender_1", 1),
								(assign, ":relation_string", "str_sisterinlaw"),
							  (else_try),
								(assign, ":relation_string", "str_brotherinlaw"),
							  (try_end),
							(else_try),
						#	  (gt, ":spouse_of_2", -1), #necessary to avoid bug #dplmc+ replaced
							  (neq, ":spouse_of_2", -1), #dplmc+ added
							  (troop_slot_eq, ":spouse_of_2", slot_troop_guardian, ":troop_1"),
							  (assign, ":relation_strength", 5),
							  (try_begin),
								#(eq, ":gender_1", 1),#dplmc+ replaced
								(eq, ":gender_1", tf_female),#dplmc+ added
								(assign, ":relation_string", "str_sisterinlaw"),
							  (else_try),
								(assign, ":relation_string", "str_brotherinlaw"),
							  (try_end),
							(else_try),
							  #(gt, ":spouse_of_1", -1), #necessary to avoid bug #dplmc+ replaced
							  (neq, ":spouse_of_1", -1), #dplmc+ added
							  (troop_slot_eq, ":spouse_of_1", slot_troop_guardian, ":troop_2"),
							  (assign, ":relation_strength", 5),
							  (try_begin),
								(eq, ":gender_1", 1),
								(assign, ":relation_string", "str_sisterinlaw"),
							  (else_try),
								(assign, ":relation_string", "str_brotherinlaw"),
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
								(assign, ":relation_string", "str_dplmc_granddaughter"),
							  (else_try),
								(assign, ":relation_string", "str_dplmc_grandson"),
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
								(assign, ":relation_string", "str_dplmc_grandmother"),
							  (else_try),
								(assign, ":relation_string", "str_dplmc_grandfather"),
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
									(assign, ":relation_string", "str_cousin"),
								(else_try),
									#Prince Valdym's uncle was Regent Burelek, father of King Yaroglek,
									#making the two of them first cousins.
									(this_or_next|eq, ":troop_1", "trp_kingdom_2_lord"),
										(eq, ":troop_1", "trp_kingdom_2_pretender"),
									(this_or_next|eq, ":troop_2", "trp_kingdom_2_lord"),
										(eq, ":troop_2", "trp_kingdom_2_pretender"),
									(assign, ":relation_strength", 2),
									(assign, ":relation_string", "str_cousin"),
								(else_try),
									#Sanjar Khan and Dustum Khan were both sons of Janakir Khan
									#(although by different mothers) making them half-brothers.
									(this_or_next|eq, ":troop_1", "trp_kingdom_3_lord"),
										(eq, ":troop_1", "trp_kingdom_3_pretender"),
									(this_or_next|eq, ":troop_2", "trp_kingdom_3_lord"),
										(eq, ":troop_2", "trp_kingdom_3_pretender"),
									(assign, ":relation_strength", 10),
									(assign, ":relation_string", "str_dplmc_half_brother"),
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
									(eq, ":gender_1", 1),
									(assign, ":relation_string", "str_aunt"),
								(else_try),
									(assign, ":relation_string", "str_uncle"),
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
									(eq, ":gender_1", 1),
									(assign, ":relation_string", "str_aunt"),
								(else_try),
									(assign, ":relation_string", "str_uncle"),
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
									(eq, ":gender_1", 1),
									(assign, ":relation_string", "str_niece"),
								(else_try),
									(assign, ":relation_string", "str_nephew"),
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
									(eq, ":gender_1", 1),
									(assign, ":relation_string", "str_niece"),
								(else_try),
									(assign, ":relation_string", "str_nephew"),
								(try_end),
							(try_end),
							
							(try_begin),
								(this_or_next|neg|troop_is_hero, ":troop_1"),
								(neg|troop_is_hero, ":troop_2"),
								(assign, ":relation_string", "str_no_relation"),
								(assign, ":relation_strength", 0),
							(try_end),

							(assign, reg0, ":relation_strength"),
							(assign, reg1, ":relation_string"),
							]),
							
							##"script_cf_dplmc_faction_has_bias_against_gender"
							("cf_dplmc_faction_has_bias_against_gender", [
								(store_script_param_1, ":faction_no"),
								(store_script_param_2, ":test_gender"),#Special: 1 is female

								(assign, reg0, 0),
								(lt, "$g_disable_condescending_comments", 2),#If bias is disabled, do not continue
								(is_between, ":test_gender", 0, 2),#valid genders are 0 and 1

								(try_begin),
									(eq, ":faction_no", "fac_player_supporters_faction"),
									(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
									(assign, ":faction_no", "$players_kingdom"),
								(try_end),

								(try_begin),
									#For a-typical factions, nothing by default.
									(neg|is_between, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
								(else_try),
									#If the leader has that gender, no prejudice.
									(faction_get_slot, ":active_npc", ":faction_no", slot_faction_leader),
									(gt, ":active_npc", -1),
									(call_script, "script_dplmc_store_troop_is_female", ":active_npc"),
									(eq, reg0, ":test_gender"),
									(assign, reg0, 0),
								(else_try),
									#Traditional gender prejudice if both are true:
									#1.  The faction has no original members of the specified gender.
									#2.  The faction has original members with non-accepting lord personalities.

									(assign, ":num_closeminded", 0),
									(assign, ":end_cond", active_npcs_end),

									(try_for_range, ":active_npc", active_npcs_begin, ":end_cond"),#Deliberately do not include kingdom ladies
										#Also deliberately exclude companions and pretenders
										#(Pretenders are marginalized at the start of the game, and
										#companions don't necessarily start in positions of power either)
										(this_or_next|is_between, ":active_npc", kings_begin, kings_end),
											(is_between, ":active_npc", lords_begin, lords_end),
										(troop_slot_eq, ":active_npc", slot_troop_original_faction, ":faction_no"),

										(call_script, "script_dplmc_store_troop_is_female", ":active_npc"),
										(try_begin),
											(eq, reg0, ":test_gender"),
											(assign, ":num_closeminded", -1000),
											(assign, ":end_cond", ":active_npc"),
										(else_try),
											(troop_get_slot, reg0, ":active_npc", slot_lord_reputation_type),
											(is_between, reg0, lrep_none + 1, lrep_roguish),#Lord (non-commoner, non-liege, non-lady) personality type
											(neq, reg0, lrep_cunning),
											(neq, reg0, lrep_goodnatured),
											(val_add, ":num_closeminded", 1),
										(try_end),
									(try_end),

									(store_sub, reg0, ":num_closeminded", 1),#Needs at least one
									(val_clamp, reg0, 0, 2),
								(try_end),

								(try_begin),
									(ge, "$cheat_mode", 1),
									(assign, ":end_cond", reg1),#just save reg1 and reg2 (ignore the normal meaning of the variable names)
									(assign, ":active_npc", reg2),
									(assign, reg1, ":faction_no"),
									(assign, reg2, ":test_gender"),
									(display_message, "@{!} Checked if faction {reg1} is prejudiced against {reg2?women:men}: {reg0?true:false}"),
									(assign, reg1, ":end_cond"),#revert reg1 and reg2 (ignore the normal meaning of the variable names)
									(assign, reg2, ":active_npc"),
								(try_end),
								(gt, reg0, 0),
							]),

						#"script_dplmc_store_troop_personality_caution_level"
						#
						# INPUT:
						#   arg1 :troop_no
						# OUTPUT:
						#   reg0 -1 for aggressive
						#         0 for neither
						#         1 for cautious
						("dplmc_store_troop_personality_caution_level", [
							#Used a number of places to determine whether a lord is cautious
							#or aggressive.  The standard is something like:
							#
							#For cautious:
							#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
							#    (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
							#    (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
							#    (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
							#
							#For aggressive:
							#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
							#    (this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
							#    (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
							#
							#I've expanded this for companion/lady personalities.
							#The result can be either:
							# -1  =  aggressive
							#  0  =  neutral
							#  1  =  cautious
							(store_script_param_1, ":troop_no"),
							
							(try_begin),
								(neg|is_between, ":troop_no", heroes_begin, heroes_end),#The player or troops that don't have slot_lord_reputation_type
								(assign, reg0, 0),#neither cautious nor aggressive
							(else_try),
								(call_script, "script_dplmc_get_troop_morality_value", ":troop_no", tmt_aristocratic),
								(lt, reg0, 0),#compliments when the player retreats
								(assign, reg0, 1),#cautious
							(else_try),
								(gt, reg0, 0),#complains when the player retreats
								(assign, reg0, -1),#aggressive
							(else_try),
								(troop_get_slot, ":reputation", ":troop_no", slot_lord_reputation_type),
								(this_or_next|eq, ":reputation", lrep_adventurous),
								(this_or_next|eq, ":reputation", lrep_martial),
								(this_or_next|eq, ":reputation", lrep_quarrelsome),
									(eq, ":reputation", lrep_selfrighteous),
								(assign, reg0, -1),#aggressive
							(else_try),
								(this_or_next|ge, ":reputation", lrep_conventional),
								(this_or_next|eq, ":reputation", lrep_upstanding),
								(this_or_next|eq, ":reputation", lrep_debauched),
								(this_or_next|eq, ":reputation", lrep_goodnatured),
									(eq, ":reputation", lrep_cunning),
								(assign, reg0, 1),#cautious
							(else_try),
								(assign, reg0, 0),#neither cautious nor aggressive
							(try_end),
						]),

						##"script_dplmc_cap_troop_describes_troop_to_troop_s1"
						#
						# e.g.
						#
						#(call_script, "script_dplmc_cap_troop_describes_troop_to_troop_s1", 1, "trp_player", ":third_lord", "$g_talk_troop"),
						#
						#INPUT:
						#        arg1  :capitalization (0 if middle of sentence, 1 if sentence start)
						#        arg2  :speaker (the one doing the talking)
						#        arg3  :described (the one being named)
						#        arg4  :listener (the one being spoken to)
						#
						#OUTPUT:
						#        Writes result to s1, clobbers s0
						#
						#Similar to "script_troop_describes_troop_to_s15", except
						#it takes into account the perspective of the one being
						#spoken to, and writes to s1
						  ("dplmc_cap_troop_describes_troop_to_troop_s1",
						  [
							(store_script_param, ":capitalization", 1),
							(store_script_param, ":speaker", 2),
							(store_script_param, ":described", 3),
							(store_script_param, ":listener", 4),
							
							(assign, ":save_reg0", reg0),
							(assign, ":save_reg1", reg1),
							
							(str_store_troop_name, s0, ":described"),
							
							(assign, reg0, ":capitalization"),
							(try_begin),
								(eq, ":described", ":listener"),
								(neq, ":speaker", ":listener"),
								(str_store_string, s0, "@{reg0?Y:y}ou"),
								(assign, reg0, 1),
							(else_try),
								(eq, ":described", ":speaker"),
								(str_store_string, s0, "@{reg0?M:m}yself"),
								(assign, reg0, 1),
							(else_try),
								(this_or_next|eq, ":described", "trp_player"),#only calculate family relationships for the player and heroes
									(is_between, ":described", heroes_begin, heroes_end),
								(assign, ":speaker_relation", 0),
								(assign, ":speaker_relation_string", 0),
								(try_begin),
									(this_or_next|eq, ":speaker", "trp_player"),#only calculate family relationships for the player and heroes
										(is_between, ":speaker", heroes_begin, heroes_end),
									(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":described", ":speaker"),
									(assign, ":speaker_relation", reg0),
									(assign, ":speaker_relation_string", reg1),
								(try_end),
								(assign, reg0, 0),
								(try_begin),
									(this_or_next|eq, ":described", "trp_player"),#only calculate family relationships for the player and heroes
										(is_between, ":described", heroes_begin, heroes_end),
									(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":described", ":listener"),
								(try_end),
								(this_or_next|ge, ":speaker_relation", 1),
									(ge, reg0, 1),
								(try_begin),
									(eq, ":speaker_relation", reg0),
									(eq, reg1, ":speaker_relation_string"),
									(neq, ":speaker", ":listener"),
									(assign, reg0, ":capitalization"),
									(str_store_string, s1, ":speaker_relation_string"),
									(str_store_string, s1, "@{reg0?O:o}ur {s1} {s0}"),
								(else_try),
									(ge, ":speaker_relation", reg0),
									(assign, reg0, ":capitalization"),
									(str_store_string, s1, ":speaker_relation_string"),
									(str_store_string, s1, "@{reg0?M:m}y {s1} {s0}"),
								(else_try),
									(assign, reg0, ":capitalization"),
									(str_store_string, s1, reg1),
									(str_store_string, s1, "@{reg0?Y:y}our {s1} {s0}"),
								(try_end),
							###Disable "marshall/liege", because that's done elsewhere anyway
							#(else_try),
							#	(store_faction_of_troop, ":speaker_faction", ":speaker"),
							#	(try_begin),
							#		(eq, ":speaker", "trp_player"),
							#		(assign, ":speaker_faction", "$players_kingdom"),
							#	(try_end),
							#	
							#	(store_faction_of_troop, ":listener_faction", ":listener"),
							#	(try_begin),
							#		(eq, ":listener", "trp_player"),
							#		(assign, ":listener_faction", "$players_kingdom"),
							#	(try_end),
							#	
							#	(faction_slot_eq, ":speaker_faction", slot_faction_leader, ":described"),
							#	(this_or_next|is_between, ":speaker_faction", npc_kingdoms_begin, npc_kingdoms_end),
							#		(faction_slot_eq, ":speaker_faction", slot_faction_state, sfs_active),
							#	(this_or_next|neq, ":described", "trp_player"),
							#		(eq, ":speaker_faction", "$players_kingdom"),
							#	(assign, reg0, ":capitalization"),
							#	(try_begin),
							#		(eq, ":speaker_faction", ":listener_faction"),
							#		(neq, ":speaker", ":listener"),
							#		(str_store_string, s1, "@{reg0?O:o}ur liege {s0}"),
							#	(else_try),
							#		(str_store_string, s1, "@{reg0?M:m}y liege {s0}"),
							#	(try_end),
							#(else_try),
							#	(faction_slot_eq, ":speaker_faction", slot_faction_marshall, ":described"),
							#	(this_or_next|is_between, ":speaker_faction", npc_kingdoms_begin, npc_kingdoms_end),
							#		(faction_slot_eq, ":speaker_faction", slot_faction_state, sfs_active),
							#	(this_or_next|neq, ":described", "trp_player"),
							#		(eq, ":speaker_faction", "$players_kingdom"),
							#	(try_begin),
							#		(eq, ":speaker_faction", ":listener_faction"),
							#		(neq, ":speaker", ":listener"),
							#		(str_store_string, s1, "@{reg0?O:o}ur marshall {s0}"),
							#	(else_try),
							#		(str_store_string, s1, "@{reg0?M:m}y marshall {s0}"),
							#	(try_end),
							#(else_try),
							#	(this_or_next|is_between, ":listener_faction", npc_kingdoms_begin, npc_kingdoms_end),
							#		(faction_slot_eq, ":listener_faction", slot_faction_state, sfs_active),
							#	(faction_slot_eq, ":listener_faction", slot_faction_leader, ":described"),
							#	(this_or_next|neq, ":described", "trp_player"),
							#		(eq, ":listener_faction", "$players_kingdom"),
							#	(assign, reg0, ":capitalization"),
							#	(str_store_string, s1, "@{reg0?Y:y}our liege {s0}"),
							
							###Disable "friend", because it gets really spammy.  (It looks really stupid to have
							###a list of fifty names, all of them starting with "Your Friend So-and-So".)
							#(else_try),
							#	(call_script, "script_troop_get_relation_with_troop", ":described", ":listener"),
							#	(ge, reg0, 20),
							#	(this_or_next|neq, ":listener", "trp_player"),
							#		(ge, reg0, 50),
							#	(call_script, "script_troop_get_relation_with_troop", ":described", ":speaker"),
							#	(this_or_next|neq, ":listener", "trp_player"),
							#		(neq, ":speaker_trp_player"),
							#	(try_begin),
							#		(ge, reg0, 20),
							#		(this_or_next|neq, ":speaker", "trp_player"),
							#			(ge, reg0, 50),
							#		(assign, reg0, ":capitalization"),
							#		(str_store_string, s1, "@{reg0?O:o}ur friend {s0}"),
							#	(else_try),
							#		(assign, reg0, ":capitalization"),
							#		(str_store_string, s1, "@{reg0?Y:y}our friend {s0}"),
							#	(try_end),
							#(else_try),
							#	(call_script, "script_troop_get_relation_with_troop", ":described", ":speaker"),
							#	(ge, reg0, 20),
							#	(this_or_next|neq, ":speaker", "trp_player"),
							#		(ge, reg0, 50),
							#	(assign, reg0, ":capitalization"),
							#	(str_store_string, s1, "@{reg0?M:m}y friend {s0}"),
							
							###The "<Jarl Aedin> of <Tihr>" condition works fine, but I'm not particularly impressed.
							###I'm not sure it's an improvement over just using their name, so I'm disabling it for now.
							#(else_try),
							#	#Did not use relation string: name by owned town.
							#	#Do not use names of castles, due to potential absurdities like "Count Harringoth of Harringoth Castle".
							#	#Skip kings and pretenders because of "Lady Isolla of Suno of Suno" and similar things.
							#	(neg|is_between, ":described", kings_begin, kings_end),
							#	(neg|is_between, ":described", pretenders_begin, pretenders_end),
							#	(this_or_next|eq, ":described", "trp_player"),
							#		(is_between, ":described", heroes_begin, heroes_end),
							#	
							#	(assign, ":owned_town", -1),
							#	(assign, ":owned_town_score", -1),
							#	(troop_get_slot, ":original_faction", ":described", slot_troop_original_faction),
							#	(try_for_range, ":town_no", towns_begin, towns_end),
							#		(party_get_slot, ":town_lord", ":town_no", slot_town_lord),
							#		(ge, ":town_lord", 0),
							#		(assign, reg0, 0),
							#		(try_begin),
							#			(eq, ":town_lord", ":described"),
							#			(assign, reg0, 10),
							#		(else_try),
							#			(this_or_next|troop_slot_eq, ":town_lord", slot_troop_spouse, ":described"),
							#				(troop_slot_eq, ":described", slot_troop_spouse, ":town_lord"),
							#			(this_or_next|is_between, ":described", kingdom_ladies_begin, kingdom_ladies_end),
							#				(troop_slot_eq, ":described", slot_troop_occupation, slto_kingdom_lady),
							#			(assign, reg0, 1),
							#		(else_try),
							#			(assign, reg0, 0),
							#		(try_end),
							#		(gt, reg0, 0),
							#		(try_begin),
							#			(party_slot_eq, ":town_no", slot_center_original_faction, ":original_faction"),
							#			(val_add, reg0, 1),
							#		(try_end),
							#		(try_begin),
							#			(this_or_next|party_slot_eq, ":town_no", dplmc_slot_center_original_lord, ":described"),
							#				(party_slot_eq, ":town_no", dplmc_slot_center_original_lord, ":town_lord"),
							#			(val_add, reg0, 2),
							#		(try_end),
							#		(try_begin),
							#			(this_or_next|troop_slot_eq, ":town_lord", slot_troop_home, ":town_no"),
							#				(troop_slot_eq, ":town_lord", slot_troop_home, ":town_no"),
							#			(val_add, reg0, 2),
							#		(try_end),
							#		(gt, reg0, ":owned_town_score"),
							#		(assign, ":owned_town_score", reg0),
							#		(assign, ":owned_town", ":town_no"),
							#	(try_end),
							#	(is_between, ":owned_town", towns_begin, towns_end),
							#	(str_store_party_name, s1, ":owned_town"),
							#	(str_store_string, s1, "@{s0} of {s1}"),
							(else_try),
								(str_store_string, s1, "str_s0"),
							(try_end),

							(assign, reg0, ":save_reg0"),
							(assign, reg1, ":save_reg1"),
							(str_store_string_reg, s0, s1),
							]),
							
							##"script_dplmc_helper_get_troop1_troop2_family_slot_aux"
							##
							## Helper function that does something specific that I want in
							## script_dplmc_troop_get_family_relation_to_troop.
							##
							## Gets the slot value, but for troops that aren't trp_player
							## and are not within (heroes_begin, heroes_end), values of "0"
							## are transformed to -1.  Also gives a result of -1 (instead of
							## an error) for negative troop IDs, which is what I want in
							## this situation (otherwise I'd be explicitly checking this and
							## setting the result to -1 if it was bad).
							##
							## Also, values equal to "active_npcs_including_player_begin" are
							## transformed to "trp_player" (i.e. 0), to allow storing that
							## value.
							##
							##INPUT:  arg1   :troop_1
							##        arg2   :troop_2
							##        arg3   :slot_no
							##
							##OUTPUT: reg0   value of slot for troop_1, or -1
							##        reg1   value of slot for troop_2, or -1
							("dplmc_helper_get_troop1_troop2_family_slot_aux",
								[
									(store_script_param, ":troop_1", 1),
									(store_script_param, ":troop_2", 2),
									(store_script_param, ":slot_no", 3),
									
									#(1) Get the value for the first troop into reg0
									(try_begin),
										#Negative numbers are placeholders for invalid family members
										(lt, ":troop_1", 0),
										(assign, reg0, -1),
									(else_try),
										#For active_npcs_including_player_begin, use the family slot from trp_player
										(eq, ":troop_1", active_npcs_including_player_begin),
										(troop_get_slot, reg0, "trp_player", ":slot_no"),
									(else_try),
										#Otherwise get the family member slot
										(troop_get_slot, reg0, ":troop_1", ":slot_no"),
										#However, for non-heroes, the memory might not be initialized,
										#so don't take a value of 0 at face-value.
										(eq, reg0, 0),
										(neg|is_between, ":troop_1", heroes_begin, heroes_end),
										(neq, ":troop_1", "trp_player"),
										(assign, reg0, -1),
									(try_end),
									
									#Translate from active_npcs_including_player_begin to trp_player
									(try_begin),
										(eq, reg0, active_npcs_including_player_begin),
										(assign, reg0, "trp_player"),
									(try_end),
									
									#(2) Get the value for the second troop into reg1
									(try_begin),
										#Negative numbers are placeholders for invalid family members
										(lt, ":troop_2", 0),
										(assign, reg1, -1),
									(else_try),
										#For active_npcs_including_player_begin, use the family slot from trp_player
										(eq, ":troop_2", active_npcs_including_player_begin),
										(troop_get_slot, reg1, "trp_player", ":slot_no"),
									(else_try),
										#Otherwise get the family member slot
										(troop_get_slot, reg1, ":troop_2", ":slot_no"),
										#However, for non-heroes, the memory might not be initialized,
										#so don't take a value of 0 at face-value.
										(eq, reg1, 0),
										(neg|is_between, ":troop_2", heroes_begin, heroes_end),
										(neq, ":troop_2", "trp_player"),
										(assign, reg1, -1),
									(try_end),

									#Translate from active_npcs_including_player_begin to trp_player
									(try_begin),
										(eq, reg1, active_npcs_including_player_begin),
										(assign, reg1, "trp_player"),
									(try_end),
								]),
								
		##"script_dplmc_estimate_center_weekly_income"
		#
		#  INPUT:  arg1   :center_no
		# OUTPUT:  reg0   estimated value of weekly income
		#
		#TODO: Add a better explanation for why this function does not include tarrifs.
		("dplmc_estimate_center_weekly_income", [
			(store_script_param_1, ":center_no"),
			(party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
			(try_begin),
			  #If there is some sort of aberration, assign to 50 instead of
			  #clamping, on the assumption that the value bears no relation
			  #to the true prosperity at all.
			  (neg|is_between, ":prosperity", 0, 101),
			  (assign, ":prosperity", 50),
			(try_end),
			(store_add, reg0, 20, ":prosperity"),
			(val_mul, reg0, 1200),
			(val_div, reg0, 120),
			(try_begin),
			  (party_slot_eq, ":center_no", slot_party_type, spt_town),
			  #Towns have higher base rent than castles and villages
			  (val_mul, reg0, 2),
			  #Include town garrison allowance
			  (val_mul, ":prosperity", 15),
			  (val_add, ":prosperity", 700),
			  (val_mul, ":prosperity", 3),
			  (val_div, ":prosperity", 2),
			  (val_add, reg0, ":prosperity"),
			(else_try),
			  (party_slot_eq, ":center_no", slot_party_type, spt_castle),
			  #Include castle garrison allowance
			  (val_mul, ":prosperity", 15),
			  (val_add, ":prosperity", 700),
			  (val_add, reg0, ":prosperity"),
			(try_end),
			#At this point, the final result is in reg0.
		]),

	  # "script_dplmc_get_closest_center_or_two"
	  # Input: arg1 = party_no
	  # Output: reg0 = center_no (closest)
	  #         reg1 = center_no2 (another close center or -1)
	  #
	  # If reg1 is non-negative, it should make some sense to say "<party_no> is
	  # between <reg0> and <reg1>".
	  #
	  # The way I do this is:
	  #   1.  Find the closest center to the party.
	  #   2.  Excluding the center from (1), find the closest center to the
	  #       party which is not closer to the center from (1) than it is to
	  #       the party.  (There might not be any centers matching this
	  #       description.)
	  #
	  # If the party is much closer to center_1 than center_2, I discard
	  # the second center.  (The rationale is that if I'm standing on my
	  # doorstep, it is be helpful to say "I am between my house and the
	  # grocery store".  It is less misleading to just say "I am near my
	  # house.")
	  ("dplmc_get_closest_center_or_two",
		[
		  (store_script_param_1, ":party_no"),
		  (call_script, "script_get_closest_center", ":party_no"),#writes closest center to reg0
		  (store_distance_to_party_from_party, ":distance_to_beat", ":party_no", reg0),
		  (val_mul, ":distance_to_beat", 2),
		  (val_add, ":distance_to_beat", 1),

		  (assign, reg1, -1),
		  (try_for_range, ":center_no", centers_begin, centers_end),
			(neq, ":center_no", reg0),
			(store_distance_to_party_from_party, ":party_to_center_distance", ":party_no", ":center_no"),
			(lt, ":party_to_center_distance", ":distance_to_beat"),
			(store_distance_to_party_from_party, ":center_to_center_distance", reg0, ":center_no"),
			(gt, ":center_to_center_distance", ":party_to_center_distance"),
			(assign, ":distance_to_beat", ":party_to_center_distance"),
			(assign, reg1, ":center_no"),
		  (try_end),
	  ]),
								
	##diplomacy end+
							
						  
# TEMPERED  BEGIN ADDED SCRIPTS   ###########################################################################################################################
#TEMPERED      PARTY ENTRENCH TIME

	("party_entrench_time",
		[
#			(store_current_hours,":cur_hour"),		 
			(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
			(assign, ":max_skill", reg0),
			(val_mul, ":max_skill",2),
			(val_max,":max_skill",1),
			(party_get_num_companions,":party_size","p_main_party"),
			(val_mul,":party_size",3),
			(val_max,":party_size",3),
			(store_mul,":man_hours",":party_size",":max_skill"),
			(store_div,":construct_time",2000,":man_hours"),		 
			(val_max,":construct_time",2),
			(val_min,":construct_time",32),
			(assign,reg5,":construct_time"),
#			(display_message,"@_Fortifications will take {reg5} hours to complete."),
#			(store_add,"$entrench_time",":cur_hour",":construct_time"),  Tempered moved to game menu
		]
	),

#TEMPERED    GET NUMBER OF HORSES FOR CAMP SITE
#input: party id of camper
#output: reg0, number of horses based on mounted troops
	("count_horses",
		[	
			(assign,":horse_count",0),
			(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
			(try_for_range,":cur_stack",0,":num_stacks"),
				(party_stack_get_troop_id,":cur_troop","p_main_party",":cur_stack"),
				(assign,":add_horses",0),
				(try_begin),					
					(troop_is_mounted,":cur_troop"),
					(party_stack_get_size,":add_horses","p_main_party",":cur_stack"),
					(val_add,":horse_count",":add_horses"),
				(try_end),
			(try_end),
			(assign,reg0,":horse_count"),
			
		]
	),

#TEMPERED  RANSACK PLAYER CAMP SITE

  ("loot_camp",
    [ (assign,":food_loss",0),
	  (assign,":horse_loss",0),
	  (store_random_in_range, ":max_horse", 0, 2),
	  (store_random_in_range, ":max_food", 1, 4),
	  (store_random_in_range, ":tool_loss", 0,500),
      (troop_get_inventory_capacity, ":inv_cap", "trp_player"),
	  (str_clear,s1),
	  (str_clear,s2),
	  (str_clear,s3),
	  (str_clear,s4),
	  (str_clear,s5),
	  (str_clear,s6),
      (try_for_range, ":i_slot", 9, ":inv_cap"), #start at 9 so no player items are looted, only inventory items.
        (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
        (ge, ":item_id", 0),
        (try_begin),
          (is_between, ":item_id", food_begin,food_end),
		  (val_add, ":food_loss", 1),
		  (le,":food_loss",":max_food"),          
		  (troop_remove_item, "trp_player", ":item_id"),
		  (str_store_item_name,s1,":item_id"),
		  (str_store_string,s2,"@{s2}{s1}, "),
		  (str_store_string,s3,"@_The following food items were destroyed or looted: {s2}. "),
        (else_try),
          (is_between, ":item_id", horses_begin, horses_end),
		  (neq,":max_horse",0),
		  (val_add, ":horse_loss", 1),
		  (le,":horse_loss",":max_horse"),          
		  (str_store_string,s5,"@_A pack horse has ran off!!"),
		  (troop_remove_item, "trp_player", ":item_id"),
		(else_try),
		  (eq,":item_id","itm_trade_tools"),
		  (le,":tool_loss",100),
		  (troop_remove_item, "trp_player", ":item_id"),
		  (str_store_string,s6,"@_Some tools have been broken or misplaced."),
        (try_end),
      (try_end),
      (store_troop_gold, ":cur_gold", "trp_player"),
      (store_div, ":max_lost", ":cur_gold", 20),
      (store_div, ":min_lost", ":cur_gold", 40),
      (store_random_in_range, ":lost_gold", ":min_lost", ":max_lost"),
      (troop_remove_gold, "trp_player", ":lost_gold"),
	  (assign,reg3,":lost_gold"),
	  (str_store_string,s4,"@ {reg3}"),
	  (dialog_box,"str_camp_loss","str_camp_overrun"),
      ]),

 # Tempered                                           ############################# SET GLOBAL VARIABLES AND SLOTS AT GAME START  ###################################
  ("init_temp_var",
	[
	 (party_set_slot,"p_main_party",slot_party_entrenched,0),
	 (assign,"$entrench_time",0),
	 (assign,"$camp_supply",1), #used for camp over run supply loss
	 (assign,"$drowning",1), #used to toggle drowning in mission templates off and on
	 (assign,"$current_camp_party",-1), #used for camp entrenchment, value is -1 or entrenchment party id
	 (party_set_slot,"p_main_party",slot_party_siege_camp,0), #used for sieges. 0 for not entrenched,-1 for entrenching, 1 for entrenched	 
#	 (assign,"$temp_presentation_shown",0), #used for presentations and menus
#	 (assign,"$temp_scene_type",0), #used for cheat menu scene selection
	]), 

#Tempered                                       ########################  Remove siege camp props  ########################################################
	("siege_camp_init",
		[	(try_begin),
				(this_or_next|party_slot_eq,"p_main_party",slot_party_siege_camp,0),
				(party_slot_eq,"p_main_party",slot_party_siege_camp,-1),
				(replace_scene_props, "spr_siege_wall_a", "spr_empty"),
				(replace_scene_props, "spr_siege_large_shield_a", "spr_empty"),
				(replace_scene_props, "spr_siege_camp_spikes", "spr_empty"),
				(replace_scene_props, "spr_siege_camp_tower", "spr_empty"),
			(try_end),
		]),
#Tempered                                   ##########################  Remove siege camp for visit #####################################################
	("siege_camp_remove",
		[	
			(replace_scene_props, "spr_siege_wall_a", "spr_empty"),
			(replace_scene_props, "spr_siege_large_shield_a", "spr_empty"),
			(replace_scene_props, "spr_siege_camp_spikes", "spr_empty"),
			(replace_scene_props, "spr_bell_tent", "spr_empty"),
			(replace_scene_props, "spr_bell_tent_inventory", "spr_empty"),
			(replace_scene_props, "spr_arena_sign", "spr_empty"),
			(replace_scene_props, "spr_siege_camp_tower", "spr_empty"),
			(replace_scene_props, "spr_siege_camp_bridge", "spr_empty"),
		]),

#Tempered populate entrenchment scene

## Lieutenant System - preview the current camp terrain scene (no horses, no companions)
  ("ssp_preview_camp_scene",
    [
      (party_get_current_terrain, ":terrain_type", "p_main_party"),
      (assign, ":scene_to_use", "scn_dhorak_keep"), # fallback: small enclosed map
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
      (assign, "$g_training_ground_training_scene", ":scene_to_use"),
      (set_jump_mission, "mt_ai_training"),
      (jump_to_scene, ":scene_to_use"),
      (change_screen_mission),
    ]),
## End ssp_preview_camp_scene

  ("visit_camp",
    [	(party_get_current_terrain, ":terrain_type", "p_main_party"),
		(party_get_slot,":entrench","p_main_party",slot_party_entrenched),		
		(assign, ":scene_to_use", "scn_not_entrenched_steppe"),
		(try_begin),
			(this_or_next|eq,":entrench",1),#entrenched camp
			(party_slot_eq,"p_main_party",slot_party_siege_camp,1),#entrenched siege camp
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
		(try_end),
		(modify_visitors_at_site, ":scene_to_use"),
        (reset_visitors),
#        (assign, "$talk_context", tc_camp),
		(assign,":count",15),
		(try_for_range,":current_npc",companions_begin,companions_end),
			(try_begin),
				(main_party_has_troop,":current_npc"),
				(set_visitor,":count",":current_npc"),
			(try_end),
			(val_add,":count",1),
		(try_end),
        (set_jump_mission,"mt_visit_entrenchment"),
        (set_jump_entry, 11),
        (jump_to_scene, ":scene_to_use"),
        (change_screen_mission),

  ]),
                          
                          # Jrider +
                          ###################################################################################
                          # REPORT PRESENTATIONS v1.2 scripts
                          # Script overlay_container_add_listbox_item
                          # use ...
                          # return ...
                          ("overlay_container_add_listbox_item", [
                              (store_script_param, ":line_y", 1),
                              (store_script_param, ":npc_id", 2),
                              
                              (set_container_overlay, "$g_jrider_character_relation_listbox"),
                              
                              # create text overlay for entry
                              (create_text_overlay, reg10, s1, tf_left_align),
                              (overlay_set_color, reg10, 0xDDDDDD),
                              (position_set_x, pos1, 650),
                              (position_set_y, pos1, 750),
                              (overlay_set_size, reg10, pos1),
                              (position_set_x, pos1, 0),
                              (position_set_y, pos1, ":line_y"),
                              (overlay_set_position, reg10, pos1),
                              
                              # create button
                              (create_image_button_overlay, reg10, "mesh_white_plane", "mesh_white_plane"),
                              (position_set_x, pos1, 0), # 590 real, 0 scrollarea
                              (position_set_y, pos1, ":line_y"),
                              (overlay_set_position, reg10, pos1),
                              (position_set_x, pos1, 16000),
                              (position_set_y, pos1, 750),
                              (overlay_set_size, reg10, pos1),
                              (overlay_set_alpha, reg10, 0),
                              (overlay_set_color, reg10, 0xDDDDDD),
                              
                              # store relation of button id to character number for use in triggers
                              (store_add, ":current_storage_index", "$g_base_character_presentation_storage_index", reg10),
                              (troop_set_slot, "trp_temp_array_b", ":current_storage_index", "$num_charinfo_candidates"),
                              
                              # reset variables if appropriate flags are up
                              (try_begin),
                                (try_begin),
                                  (this_or_next|eq, "$g_jrider_pres_called_from_menu", 1),
                                  (ge, "$g_jrider_reset_selected_on_faction", 1),
                                  
                                  (assign, "$character_info_id", ":npc_id"),
                                  (assign, "$g_jrider_last_checked_indicator", reg10),
                                  (assign, "$g_latest_character_relation_entry", "$num_charinfo_candidates"),
                                (try_end),
                              (try_end),
                              
                              # close the container
                              (set_container_overlay, -1),
                          ]),
                          
                          # script get_relation_candidate_list_for_presentation
                          # return a list of candidate according to type of list and restrict options
                          # Use ...
                          ("fill_relation_canditate_list_for_presentation",
                            [
                              (store_script_param, ":pres_type", 1),
                              (store_script_param, ":base_candidates_y", 2),
                              
                              # Type of list from global variable: 0 courtship, 1 known lords
                              (try_begin),
                                ## For courtship:
                                (eq, ":pres_type", 0),
                                
                                (try_for_range_backwards, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
                                  (troop_slot_ge, ":lady", slot_troop_met, 1), # met or better
                                  (troop_slot_eq, ":lady", slot_troop_spouse, -1), # unmarried
                                  
                                  # use faction filter
                                  (store_troop_faction, ":lady_faction", ":lady"),
                                  (val_sub, ":lady_faction", kingdoms_begin),
                                  (this_or_next|eq, "$g_jrider_faction_filter", -1),
                                  (eq, "$g_jrider_faction_filter", ":lady_faction"),
                                  
                                  (call_script, "script_troop_get_relation_with_troop", "trp_player", ":lady"),
                                  (gt, reg0, 0),
                                  (assign, reg3, reg0),
                                  
                                  (str_store_troop_name, s2, ":lady"),
                                  
                                  (store_current_hours, ":hours_since_last_visit"),
                                  (troop_get_slot, ":last_visit_hour", ":lady", slot_troop_last_talk_time),
                                  (val_sub, ":hours_since_last_visit", ":last_visit_hour"),
                                  (store_div, ":days_since_last_visit", ":hours_since_last_visit", 24),
                                  (assign, reg4, ":days_since_last_visit"),
                                  
                                  #(str_store_string, s1, "str_s1_s2_relation_reg3_last_visit_reg4_days_ago"),
                                  (str_store_string, s1, "@{s2}: {reg3}, {reg4} days"),
                                  
                                  # create custom listbox entry, set the container first
                                  (store_mul, ":y_mult", "$num_charinfo_candidates", 16), # adapt y position to entry number, was 18
                                  (store_add, ":line_y", ":base_candidates_y", ":y_mult"),
                                  
                                  (call_script, "script_overlay_container_add_listbox_item", ":line_y", ":lady"),
                                  
                                  # candidate found, store troop id for later use
                                  (store_add, ":current_storage_index", "$g_base_character_presentation_storage_index", "$num_charinfo_candidates"),
                                  (troop_set_slot, "trp_temp_array_c", ":current_storage_index", ":lady"),
                                  
                                  # update entry counter
                                  (val_add, "$num_charinfo_candidates", 1),
                                (try_end),
                                ## End courtship relations
                              (else_try),
                                ## For lord relations
                                (eq, ":pres_type", 1),
                                
                                # Loop to identify
                                (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
                                  (troop_set_slot, ":active_npc", slot_troop_temp_slot, 0),
                                (try_end),
                                
                                (try_for_range, ":unused", active_npcs_begin, active_npcs_end),
                                  
                                  (assign, ":score_to_beat", 101),
                                  (assign, ":best_relation_remaining_npc", -1),
                                  
                                  (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
                                    (troop_slot_eq, ":active_npc", slot_troop_temp_slot, 0),
                                    (troop_slot_ge, ":active_npc", slot_troop_met, 1),
                                    (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
                                    
                                    (call_script, "script_troop_get_player_relation", ":active_npc"),
                                    (assign, ":relation_with_player", reg0),
                                    (le, ":relation_with_player", ":score_to_beat"),
                                    
                                    (assign, ":score_to_beat", ":relation_with_player"),
                                    (assign, ":best_relation_remaining_npc", ":active_npc"),
                                  (try_end),
                                  (gt, ":best_relation_remaining_npc", -1),
                                  
                                  (str_store_troop_name, s4, ":best_relation_remaining_npc"),
                                  (assign, reg4, ":score_to_beat"),
                                  
                                  (str_store_string, s1, "@{s4}: {reg4}"),
                                  (troop_set_slot, ":best_relation_remaining_npc", slot_troop_temp_slot, 1),
                                  
                                  # use faction filter
                                  (store_troop_faction, ":npc_faction", ":best_relation_remaining_npc"),
                                  (val_sub, ":npc_faction", kingdoms_begin),
                                  (this_or_next|eq, "$g_jrider_faction_filter", -1),
                                  (eq, "$g_jrider_faction_filter", ":npc_faction"),
                                  
                                  # candidate found,
                                  # create custom listbox entry, set the container first
                                  (store_mul, ":y_mult", "$num_charinfo_candidates", 16), # adapt y position to entry number, was 18
                                  (store_add, ":line_y", ":base_candidates_y", ":y_mult"),
                                  
                                  (call_script, "script_overlay_container_add_listbox_item", ":line_y", ":best_relation_remaining_npc"),
                                  
                                  #store troop id for later use (could be merged with the object id)
                                  (store_add, ":current_storage_index", "$g_base_character_presentation_storage_index", "$num_charinfo_candidates"),
                                  (troop_set_slot, "trp_temp_array_c", ":current_storage_index", ":best_relation_remaining_npc"),
                                  
                                  # update entry counter
                                  (val_add, "$num_charinfo_candidates", 1),
                                (try_end),
                                ## END Lords relations
                              (else_try),
                                ## Character and Companions
                                (eq, ":pres_type", 2),
                                
                                # companions
                                (try_for_range_backwards, ":companion", companions_begin, companions_end),
                                  (troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),
                                  
                                  (str_store_troop_name, s1, ":companion"),
                                  
                                  (try_begin),
                                    (troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_kingsupport),
                                    (str_store_string, s1, "@{s1}(gathering support)"),
                                  (else_try),
                                    (troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_gather_intel),
                                    (str_store_string, s1, "@{s1} (intelligence)" ),
                                  (else_try),
                                    (troop_slot_ge, ":companion", slot_troop_current_mission, npc_mission_peace_request),
                                    (neg|troop_slot_eq, ":companion", slot_troop_current_mission, 8),
                                    (str_store_string, s1, "@{s1} (ambassy)"),
                                  (else_try),
                                    (eq, ":companion", "$g_player_minister"),
                                    (str_store_string, s1, "@{s1} (minister"),
                                    (else_try),
                                      (main_party_has_troop, ":companion"),
                                      (str_store_string, s1, "@{s1} (under arms)"),
                                    (else_try),
                                      (troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_rejoin_when_possible),
                                      (str_store_string, s1, "@{s1} (attempting to rejoin)"),
                                    (else_try),
                                      (troop_slot_ge, ":companion", slot_troop_cur_center, 1),
                                      (str_store_string, s1, "@{s1} (separated after battle)"),
                                    (try_end),
                                    # candidate found,
                                    # create custom listbox entry, set the container first
                                    (store_mul, ":y_mult", "$num_charinfo_candidates", 16), # adapt y position to entry number, was 18
                                    (store_add, ":line_y", ":base_candidates_y", ":y_mult"),
                                    
                                    (call_script, "script_overlay_container_add_listbox_item", ":line_y", ":companion"),
                                    
                                    #store troop id for later use (could be merged with the object id)
                                    (store_add, ":current_storage_index", "$g_base_character_presentation_storage_index", "$num_charinfo_candidates"),
                                    (troop_set_slot, "trp_temp_array_c", ":current_storage_index", ":companion"),
                                    
                                    # update entry counter
                                    (val_add, "$num_charinfo_candidates", 1),
                                  (try_end),
                                  # END companions
                                  
                                  # Wife/Betrothed
                                  # END Wife/Betrothed
                                  
                                  (try_begin),
                                    # Character
                                    (str_store_troop_name, s1, "trp_player"),
                                    
                                    # candidate found,
                                    # create custom listbox entry, set the container first
                                    (store_mul, ":y_mult", "$num_charinfo_candidates", 16), # adapt y position to entry number, was 18
                                    (store_add, ":line_y", ":base_candidates_y", ":y_mult"),
                                    
                                    (call_script, "script_overlay_container_add_listbox_item", ":line_y", "trp_player"),
                                    
                                    #store troop id for later use (could be merged with the object id)
                                    (store_add, ":current_storage_index", "$g_base_character_presentation_storage_index", "$num_charinfo_candidates"),
                                    (troop_set_slot, "trp_temp_array_c", ":current_storage_index", "trp_player"),
                                    
                                    # update entry counter
                                    (val_add, "$num_charinfo_candidates", 1),
                                  (try_end),
                                  # End Character
                                  
                                (try_end),
                                ## END Character and Companions
                            ]),
                            
                            # script get_troop_relation_to_player_string
                            # return relation to player string in the specified parameters
                            #
                            ("get_troop_relation_to_player_string",
                              [
                                (store_script_param, ":target_string", 1),
                                (store_script_param, ":troop_no", 2),
                                
                                (call_script, "script_troop_get_player_relation", ":troop_no"),
                                (assign, ":relation", reg0),
                                (str_clear, s61),
                                
                                (store_add, ":normalized_relation", ":relation", 100),
                                (val_add, ":normalized_relation", 5),
                                (store_div, ":str_offset", ":normalized_relation", 10),
                                (val_clamp, ":str_offset", 0, 20),
                                (store_add, ":str_rel_id", "str_relation_mnus_100_ns",  ":str_offset"),
                                
                                ## Make something if troop has relation but not strong enought to warrant a string
                                (try_begin),
                                  (neq, ":str_rel_id", "str_relation_plus_0_ns"),
                                  (str_store_string, s61, ":str_rel_id"),
                                (else_try),
                                  (neg|eq, reg0, 0),
                                  (str_is_empty, s61),
                                  (str_store_string, s61, "@ knows of you."),
                                (else_try),
                                  (eq, reg0, 0),
                                  (str_is_empty, s61),
                                  (str_store_string, s61, "@ has no opinion about you."),
                                (try_end),
                                
                                ## copy result string to target string
                                (str_store_string_reg, ":target_string", s61),
                            ]),
                            
                            # script get_troop_holdings
                            # returns number of fief and list name (reg50, s50)
                            ("get_troop_holdings",
                              [
                                (store_script_param, ":troop_no", 1),
                                
                                (assign, ":owned_centers", 0),
                                (assign, ":num_centers", 0),
                                (try_for_range_backwards, ":cur_center", centers_begin, centers_end),
                                  (party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
                                  (try_begin),
                                    (eq, ":num_centers", 0),
                                    (str_store_party_name, s50, ":cur_center"),
                                    (val_add, ":owned_centers", 1),
                                  (else_try),
                                    (eq, ":num_centers", 1),
                                    (str_store_party_name, s57, ":cur_center"),
                                    (str_store_string, s50, "@{s57} and {s50}"),
                                    (val_add, ":owned_centers", 1),
                                  (else_try),
                                    (str_store_party_name, s57, ":cur_center"),
                                    (str_store_string, s50, "@{!}{s57}, {s50}"),
                                    (val_add, ":owned_centers", 1),
                                  (try_end),
                                  (val_add, ":num_centers", 1),
                                (try_end),
                                (assign, reg50, ":owned_centers"),
                            ]),
                            # script generate_extended_troop_relation_information_string
                            # return information about troop according to type (lord, lady, maiden)
                            # Use (hm lots of registers and strings)
                            # result stored in s1
                            ("generate_extended_troop_relation_information_string",
                              [
                                (store_script_param, ":troop_no", 1),
                                
                                # clear the strings and registers we'll use to prevent external interference
                                (str_clear, s1),
                                (str_clear, s2),
                                (str_clear, s60),
                                (str_clear, s42),
                                (str_clear, s43),
                                (str_clear, s44),
                                (str_clear, s45),
                                (str_clear, s46),
                                (str_clear, s47),
                                (str_clear, s48),
                                (str_clear, s49),
                                (str_clear, s50),
                                (assign, reg40,0),
                                (assign, reg41,0),
                                (assign, reg43,0),
                                (assign, reg44,0),
                                (assign, reg46,0),
                                (assign, reg47,0),
                                (assign, reg48,0),
                                (assign, reg49,0),
                                (assign, reg50,0),
                                (assign, reg51,0),
                                
                                (try_begin),
                                  (eq, ":troop_no", "trp_player"),
                                  (overlay_set_display, "$g_jrider_character_faction_filter", 0),
                                  
                                  # Troop name
                                  (str_store_troop_name, s1, ":troop_no"),
                                  
                                  # Get renown - slot_troop_renown
                                  (troop_get_slot, ":renown", ":troop_no", slot_troop_renown),
                                  (assign, reg40, ":renown"),
                                  
                                  # Controversy - slot_troop_controversy
                                  (troop_get_slot, ":controversy", ":troop_no", slot_troop_controversy),
                                  (assign, reg41, ":controversy"),
                                  
                                  # Honor - $player_honor
                                  (assign, reg42, "$player_honor"),
                                  
                                  # Right to rule - $player_right_to_rule
                                  (assign, reg43, "$player_right_to_rule"),
                                  
                                  # Current faction
                                  (store_add, reg45, "$players_kingdom"),
                                  (try_begin),
                                    (is_between, "$players_kingdom", "fac_player_supporters_faction", npc_kingdoms_end),
                                    (str_store_faction_name, s45, "$players_kingdom"),
                                  (else_try),
                                    (assign, reg45, 0),
                                    (str_store_string, s45, "@Calradia."),
                                  (try_end),
                                  
                                  # status
                                  (assign, ":origin_faction", "$players_kingdom"),
                                  (try_begin),
                                    (is_between, ":origin_faction", npc_kingdoms_begin, npc_kingdoms_end),
                                    (str_store_string, s44, "@sworn man"),
                                  (else_try),
                                    (eq, ":origin_faction", "fac_player_supporters_faction"),
                                    (str_store_string, s44, "@ruler"),
                                  (else_try),
                                    (str_store_string, s44, "@free man"),
                                  (try_end),
                                  
                                  # Current liege and relation
                                  (faction_get_slot, ":liege", "$players_kingdom", slot_faction_leader),
                                  (str_store_troop_name, s46, ":liege"),
                                  (try_begin),
                                    (eq, ":liege", ":troop_no"),
                                    (assign, reg46, 0),
                                  (else_try),
                                    (assign, reg46, ":liege"),
                                    (str_clear, s47),
                                    (str_clear, s60),
                                    
                                    # Relation to liege
                                    (call_script, "script_get_troop_relation_to_player_string", s47, ":liege"),
                                  (end_try),
                                  
                                  # Holdings
                                  (call_script, "script_get_troop_holdings", ":troop_no"),
                                  
                                  #### Final Storage
                                  (str_store_string, s1, "@{s1} Renown: {reg40}, Controversy: {reg41}^Honor: {reg42}, Right to rule: {reg43}^\
                                  You are a {s44} of {s45}^{reg45?{reg46?Your liege, {s46},{s47}:You are the ruler of {s45}}:}^^Friends: ^Enemies: ^^Fiefs:^  {reg50?{s50}:no fief}"),
                                  #######################
                                  # END Player information
                                (else_try),
                                  #######################
                                  # Lord information
                                  (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
                                  
                                  # Troop name
                                  (str_store_troop_name, s1, ":troop_no"),
                                  
                                  # relation to player
                                  (str_clear, s2),
                                  (str_clear, s60),
                                  (call_script, "script_get_troop_relation_to_player_string", s2, ":troop_no"),
                                  
                                  # Get renown - slot_troop_renown
                                  (troop_get_slot, ":renown", ":troop_no", slot_troop_renown),
                                  (assign, reg40, ":renown"),
                                  
                                  # Controversy - slot_troop_controversy
                                  (troop_get_slot, ":controversy", ":troop_no", slot_troop_controversy),
                                  (assign, reg41, ":controversy"),
                                  
                                  # Get Reputation type - slot_lord_reputation_type
                                  (troop_get_slot, ":reputation", ":troop_no", slot_lord_reputation_type),
                                  (assign, reg42, "str_personality_archetypes"),
                                  (val_add, reg42, ":reputation"),
                                  (str_store_string, s42, reg42),
                                  
                                  (assign, reg42, ":reputation"),
                                  # Intrigue impatience - slot_troop_intrigue_impatience
                                  (troop_get_slot, ":impatience", ":troop_no", slot_troop_intrigue_impatience),
                                  (assign, reg43, ":impatience"),
                                  
                                  # Current faction - store_troop_faction
                                  (store_troop_faction, ":faction", ":troop_no"),
                                  (troop_get_slot, ":origin_faction", ":troop_no", slot_troop_original_faction),
                                  
                                  # Original faction - slot_troop_original_faction
                                  (try_begin),
                                    (val_sub, ":origin_faction", npc_kingdoms_begin),
                                    (val_add, ":origin_faction", "str_kingdom_1_adjective"),
                                    (str_store_string, s44, ":origin_faction"),
                                  (end_try),
                                  (str_store_faction_name, s45, ":faction"),
                                  
                                  # Current liege - deduced from current faction
                                  (faction_get_slot, ":liege", ":faction", slot_faction_leader),
                                  (str_store_troop_name, s46, ":liege"),
                                  (try_begin),
                                    (eq, ":liege", ":troop_no"),
                                    (assign, reg46, 0),
                                  (else_try),
                                    (assign, reg46, ":liege"),
                                    # Relation to liege
                                    (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":liege"),
                                    (assign, reg47, reg0),
                                  (end_try),
                                  
                                  # Promised a fief ?
                                  (troop_get_slot, reg51, ":troop_no", slot_troop_promised_fief),
                                  
                                  # Holdings
                                  (call_script, "script_get_troop_holdings", ":troop_no"),
                                  
                                  # slot_troop_prisoner_of_party
                                  (assign, reg48, 0),
                                  (try_begin),
                                    (troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
                                    (assign, reg48, 1),
                                    (troop_get_slot, ":prisoner_party", ":troop_no", slot_troop_prisoner_of_party),
                                    (store_faction_of_party, ":party_faction", ":prisoner_party"),
                                    (str_store_faction_name, s48, ":party_faction"),
                                  (try_end),
                                  
                                  # Days since last meeting
                                  (store_current_hours, ":hours_since_last_visit"),
                                  (troop_get_slot, ":last_visit_hour", ":troop_no", slot_troop_last_talk_time),
                                  (val_sub, ":hours_since_last_visit", ":last_visit_hour"),
                                  (store_div, reg49, ":hours_since_last_visit", 24),
                                  
                                  #### Final Storage (8 lines)
                                  (str_store_string, s1, "@{s1}{s2} {reg46?Reputed to be {s42}:}^Renown: {reg40}, Controversy: {reg41} {reg46?Impatience: {reg43}:}^\
                                    {s44} noble of the {s45}^{reg46?Liege: {s46}, Relation: {reg47}:Ruler of the {s45}}^^{reg48?Currently prisoner of the {s48}:}^\
                                    Days since last meeting: {reg49}^^Fiefs {reg51?(was promised a fief):}:^  {reg50?{s50}:no fief}"),
                                  ######################
                                  ## END lord infomation
                                (else_try),
                                  #########################
                                  # kingdom lady, unmarried
                                  (is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
                                  (troop_slot_eq, ":troop_no", slot_troop_spouse, -1),
                                  
                                  (str_store_troop_name, s1, ":troop_no"),
                                  
                                  # relation to player
                                  (str_clear, s2),
                                  (str_clear, s60),
                                  (call_script, "script_get_troop_relation_to_player_string", s2, ":troop_no"),
                                  
                                  # Controversy - slot_troop_controversy
                                  (troop_get_slot, ":controversy", ":troop_no", slot_troop_controversy),
                                  (assign, reg41, ":controversy"),
                                  
                                  # Reputation type
                                  (troop_get_slot, ":reputation", ":troop_no", slot_lord_reputation_type),
                                  (try_begin),
                                    (eq, ":reputation", lrep_conventional),
                                    (str_store_string, s42, "@conventional"),
                                  (else_try),
                                    (eq, ":reputation", lrep_adventurous),
                                    (str_store_string, s42, "@adventurous"),
                                  (else_try),
                                    (eq, ":reputation", lrep_otherworldly),
                                    (str_store_string, s42, "@otherwordly"),
                                  (else_try),
                                    (eq, ":reputation", lrep_ambitious),
                                    (str_store_string, s42, "@ambitious"),
                                  (else_try),
                                    (eq, ":reputation", lrep_moralist),
                                    (str_store_string, s42, "@moralist"),
                                  (else_try),
                                    (assign, reg42, "str_personality_archetypes"),
                                    (val_add, reg42, ":reputation"),
                                    (str_store_string, s42, reg42),
                                  (try_end),
                                  
                                  # courtship state - slot_troop_courtship_state
                                  (troop_get_slot, ":courtship_state", ":troop_no", slot_troop_courtship_state),
                                  (try_begin),
                                    (eq, ":courtship_state", 1),
                                    (str_store_string, s43, "@just met"),
                                  (else_try),
                                    (eq, ":courtship_state", 2),
                                    (str_store_string, s43, "@admirer"),
                                  (else_try),
                                    (eq, ":courtship_state", 3),
                                    (str_store_string, s43, "@promised"),
                                  (else_try),
                                    (eq, ":courtship_state", 4),
                                    (str_store_string, s43, "@breakup"),
                                  (else_try),
                                    (str_store_string, s43, "@unknown"),
                                  (try_end),
                                  
                                  # Current faction - store_troop_faction
                                  (store_troop_faction, ":faction", ":troop_no"),
                                  (troop_get_slot, ":origin_faction", ":troop_no", slot_troop_original_faction),
                                  
                                  # Original faction - slot_troop_original_faction
                                  (try_begin),
                                    (val_sub, ":origin_faction", npc_kingdoms_begin),
                                    (val_add, ":origin_faction", "str_kingdom_1_adjective"),
                                    (str_store_string, s44, ":origin_faction"),
                                  (end_try),
                                  (str_store_faction_name, s45, ":faction"),
                                  
                                  # Father/Guardian
                                  (assign, reg46, 0),
                                  (try_begin),
                                    (troop_slot_ge, ":troop_no", slot_troop_father, 0),
                                    (troop_get_slot, ":guardian", ":troop_no", slot_troop_father),
                                    (assign, reg46, 1),
                                  (else_try),
                                    (troop_get_slot, ":guardian", ":troop_no", slot_troop_guardian),
                                  (try_end),
                                  (str_store_troop_name, s46, ":guardian"),
                                  
                                  # Relation with player
                                  (str_clear, s47),
                                  (str_clear, s60),
                                  (call_script, "script_get_troop_relation_to_player_string", s47, ":guardian"),
                                  
                                  # courtship permission - slot_lord_granted_courtship_permission
                                  (try_begin),
                                    (troop_slot_ge, ":guardian", slot_lord_granted_courtship_permission, 1),
                                    (assign, reg45, 1),
                                  (else_try),
                                    (assign, reg45, 0),
                                  (try_end),
                                  
                                  # betrothed
                                  (assign, reg48, 0),
                                  (try_begin),
                                    (troop_slot_ge, ":troop_no", slot_troop_betrothed, 0),
                                    (troop_get_slot, reg48, ":troop_no", slot_troop_betrothed),
                                    (str_store_troop_name, s48, reg48),
                                    (assign, reg48, 1),
                                  (try_end),
                                  
                                  # Days since last meeting
                                  (store_current_hours, ":hours_since_last_visit"),
                                  (troop_get_slot, ":last_visit_hour", ":troop_no", slot_troop_last_talk_time),
                                  (val_sub, ":hours_since_last_visit", ":last_visit_hour"),
                                  (store_div, reg49, ":hours_since_last_visit", 24),
                                  
                                  # Heard poems
                                  (assign, reg50, 0),
                                  (str_clear, s50),
                                  
                                  (try_begin),
                                    (troop_slot_eq, ":troop_no", slot_lady_courtship_heroic_recited, 1),
                                    (val_add, reg50, 1),
                                    (str_store_string, s50, "@Heroic {s50}"),
                                  (try_end),
                                  (try_begin),
                                    (troop_slot_eq, ":troop_no", slot_lady_courtship_allegoric_recited, 1),
                                    (val_add, reg50, 1),
                                    (str_store_string, s50, "@Allegoric {s50}"),
                                  (try_end),
                                  (try_begin),
                                    (troop_slot_eq, ":troop_no", slot_lady_courtship_comic_recited, 1),
                                    (val_add, reg50, 1),
                                    (str_store_string, s50, "@Comic {s50}"),
                                  (try_end),
                                  (try_begin),
                                    (troop_slot_eq, ":troop_no", slot_lady_courtship_mystic_recited, 1),
                                    (val_add, reg50, 1),
                                    (str_store_string, s50, "@Mystic {s50}"),
                                  (try_end),
                                  (try_begin),
                                    (troop_slot_eq, ":troop_no", slot_lady_courtship_tragic_recited, 1),
                                    (val_add, reg50, 1),
                                    (str_store_string, s50, "@Tragic {s50}"),
                                  (try_end),
                                  
                                  #### Final Storage (8 lines)
                                  (str_store_string, s1, "@{s1}{s2} Controversy: {reg41}^Reputation: {s42}, Courtship state: {s43}^\
                                    Belongs to the {s45}^{reg46?Her father, {s46}:Her guardian, {s46}}{s47}^Allowed to visit: {reg45?yes:no} {reg48?Betrothed to {s48}:}^^\
                                  Days since last meeting: {reg49}^^Poems:^  {reg50?{s50}:no poem heard}"),
                                  #########################
                                  # END kingdom lady, unmarried
                                (else_try),
                                  #########################
                                  # companions
                                  (is_between, ":troop_no", companions_begin, companions_end),
                                  (overlay_set_display, "$g_jrider_character_faction_filter", 0),
                                  
                                  (str_store_troop_name, s1, ":troop_no"),
                                  
                                  (troop_get_slot, ":reputation", ":troop_no", slot_lord_reputation_type),
                                  
                                  (assign, reg42, "str_personality_archetypes"),
                                  (val_add, reg42, ":reputation"),
                                  (str_store_string, s42, reg42),
                                  
                                  # birthplace
                                  (troop_get_slot, ":home", ":troop_no", slot_troop_home),
                                  (str_store_party_name, s43, ":home"),
                                  
                                  # contacts town - slot_troop_town_with_contacts
                                  (troop_get_slot, ":contact_town", ":troop_no", slot_troop_town_with_contacts),
                                  (str_store_party_name, s44, ":contact_town"),
                                  
                                  # current faction of contact town
                                  (store_faction_of_party, ":town_faction", ":contact_town"),
                                  (str_store_faction_name, s45, ":town_faction"),
                                  
                                  # slot_troop_prisoner_of_party
                                  (assign, reg48, 0),
                                  (try_begin),
                                    (troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
                                    (assign, reg48, 1),
                                    (troop_get_slot, ":prisoner_party", ":troop_no", slot_troop_prisoner_of_party),
                                    (store_faction_of_party, ":party_faction", ":prisoner_party"),
                                    (str_store_faction_name, s48, ":party_faction"),
                                  (try_end),
                                  
                                  # Days since last meeting
                                  (store_current_hours, ":hours_since_last_visit"),
                                  (troop_get_slot, ":last_visit_hour", ":troop_no", slot_troop_last_talk_time),
                                  (val_sub, ":hours_since_last_visit", ":last_visit_hour"),
                                  (store_div, reg49, ":hours_since_last_visit", 24),
                                  
                                  (try_begin), # Companion gathering support for Right to Rule
                                    (troop_slot_eq, ":troop_no", slot_troop_current_mission, npc_mission_kingsupport),
                                    (str_store_string, s50, "@Gathering support"),
                                  (else_try), # Companion gathering intelligence
                                    (troop_slot_eq, ":troop_no", slot_troop_current_mission, npc_mission_gather_intel),
                                    (troop_get_slot, ":contact_town", ":troop_no", slot_troop_town_with_contacts),
                                    (store_faction_of_party, ":town_faction", ":contact_town"),
                                    (str_store_faction_name, s66, ":town_faction"),
                                    (str_store_string, s50, "@Gathering intelligence in the {s66}"),
                                  (else_try), # Companion on peace mission
                                    (troop_slot_ge, ":troop_no", slot_troop_current_mission, npc_mission_peace_request),
                                    (neg|troop_slot_ge, ":troop_no", slot_troop_current_mission, 8),
                                    
                                    (troop_get_slot, ":troop_no", ":troop_no", slot_troop_mission_object),
                                    (str_store_faction_name, s66, ":faction"),
                                    
                                    (str_store_string, s50, "@Ambassy to {s66}"),
                                  (else_try), # Companion is serving as minister player has court
                                    (eq, ":troop_no", "$g_player_minister"),
                                    (str_store_string, s50, "@Minister"),
                                  (else_try),
                                    (str_store_string, s50, "@none"),
                                  (try_end),
                                  
                                  # days left
                                  (troop_get_slot, reg50, ":troop_no", slot_troop_days_on_mission),
                                  
                                  #### Final Storage (8 lines)
                                  (str_store_string, s1, "@{s1}, {s2}^Reputation: {s42}^\
                                    Born at {s43}^Contact in {s44} of the {s45}.^\
                                  ^{reg48?Currently prisoner of the {s48}:}^Days since last talked to: {reg49}^^Current mission:^  {s50}{reg50?, back in {reg50} days.:}"),
                                  #########################
                                  # END companions
                                (try_end),
                            ]),
                            
                            # Script generate_known_poems_string
                            # generate in s1 list of known poems filling with blank lines for unknown ones
                            ("generate_knonwn_poems_string",
                              [
                                # Known poems string
                                (assign, ":num_poems", 0),
                                (str_store_string, s1, "str_s1__poems_known"),
                                (try_begin),
                                  (gt, "$allegoric_poem_recitations", 0),
                                  (str_store_string, s1, "str_s1_storming_the_castle_of_love_allegoric"),
                                  (val_add, ":num_poems", 1),
                                (try_end),
                                (try_begin),
                                  (gt, "$tragic_poem_recitations", 0),
                                  (str_store_string, s1, "str_s1_kais_and_layali_tragic"),
                                  (val_add, ":num_poems", 1),
                                (try_end),
                                (try_begin),
                                  (gt, "$comic_poem_recitations", 0),
                                  (str_store_string, s1, "str_s1_a_conversation_in_the_garden_comic"),
                                  (val_add, ":num_poems", 1),
                                (try_end),
                                (try_begin),
                                  (gt, "$heroic_poem_recitations", 0),
                                  (str_store_string, s1, "str_s1_helgered_and_kara_epic"),
                                  (val_add, ":num_poems", 1),
                                (try_end),
                                (try_begin),
                                  (gt, "$mystic_poem_recitations", 0),
                                  (str_store_string, s1, "str_s1_a_hearts_desire_mystic"),
                                  (val_add, ":num_poems", 1),
                                (try_end),
                                
                                # fill blank lines
                                (try_for_range, ":num_poems", 5),
                                  (str_store_string, s1, "@{s1}^"),
                                (try_end),
                            ]),
                            # Jrider -
                            
	## FORAGING v1.0 #######################################################################
	## Script food_consumption_display_message
	## display food consumption
	## use reg1 and reg2 and reg4 from forage
	## hooked in simple trigger for food consumption every 14 hours
	("food_consumption_display_message",
	  [
		(store_script_param, ":num_men", 1),
		
		(assign, reg1, ":num_men"),
		# Display day of food left with current amount and party size
		(assign, ":available_food", 0),
		(troop_get_inventory_capacity, ":capacity", "trp_player"),
		(try_for_range, ":cur_slot", 0, ":capacity"),
		  (troop_get_inventory_slot, ":cur_item", "trp_player", ":cur_slot"),
		  (try_begin),
			(is_between, ":cur_item", food_begin, food_end),
			(troop_get_inventory_slot_modifier, ":item_modifier", "trp_player", ":cur_slot"),
			(neq, ":item_modifier", imod_rotten),
			(troop_inventory_slot_get_item_amount, ":cur_amount", "trp_player", ":cur_slot"),
			(val_add, ":available_food", ":cur_amount"),
		  (try_end),
		(try_end),
		
		(assign, ":num_food_hours", ":available_food"),
		(val_mul, ":num_food_hours", 14),
		(val_div, ":num_food_hours", 24),
		(val_div, ":num_food_hours", ":num_men"),
		(assign, ":num_food_days", ":num_food_hours"),
		(assign, reg2, ":num_food_days"),
		
		(try_begin),
		  (lt, reg2, 4),
		  (display_message, "@Your party consumed {reg1} units of food{reg4?, {reg4} from foraging : }({reg2} days left).", 0xFF0000),
		(else_try),
		  (display_message, "@Your party consumed {reg1} units of food{reg4?, {reg4} from foraging : }({reg2} days left)."),
		(try_end),
	]),
	
	# Script forage_for_food
	# Compute foraging amount
	# use s2, reg0, reg1 and reg10
	# for DEBUG, use s1 and reg11
	# use reg4 for return value
	("forage_for_food",
	  [
		# Get max skill in party for foraging
		(call_script, "script_get_max_skill_of_player_party", "skl_foraging"),
		(assign, ":max_foraging_in_party", reg0),
		(assign, ":max_skill_owner", reg1),
		
		# Initialize foraged food amount and register
		(assign, ":foraged_food", 0),
		(assign, reg4, 0),
		
		(try_begin),
		  # stop if no-one has foraging skill
		  (gt, ":max_foraging_in_party", 0),
		  
		  (try_begin),
			# set limits and range for foraging
			(assign,  ":foraging_limit", ":max_foraging_in_party"),
			(val_mul, ":foraging_limit", 5),
			(assign,  ":foraging_distance", ":max_foraging_in_party"),
			(val_mul, ":foraging_distance", 2),
			
			# Check distance from village or town
			(try_for_parties,":foraging_site"),
			  (assign, ":foraged_food_at_site", 0),
			  (this_or_next|party_slot_eq, ":foraging_site", slot_party_type, spt_town),
			  (party_slot_eq, ":foraging_site", slot_party_type, spt_village),
			  (neg|party_slot_eq, ":foraging_site", slot_village_state, svs_looted), # no foraging from looted village
			  
			  # Compute center distance to party
			  (store_distance_to_party_from_party, ":distance", ":foraging_site", "p_main_party"),
			  (try_begin),
				(le,":distance",":foraging_distance"), # we can forage from this center
				
				# Forage from fields
				(party_get_slot, ":temp_forage", ":foraging_site", slot_center_acres_grain),
				(val_div, ":temp_forage", 1000), # 500 was too low, try 1000
				(val_add, ":foraged_food_at_site", ":temp_forage"),
				
				(party_get_slot, ":temp_forage", ":foraging_site", slot_center_acres_vineyard),
				(val_div, ":temp_forage", 800), # 400 was too low, try 800
				(val_add, ":foraged_food_at_site", ":temp_forage"),
				
				(party_get_slot, ":temp_forage", ":foraging_site", slot_center_acres_vineyard), # second time for fruits
				(val_div, ":temp_forage", 1000), # 500 was too low, try 1000
				(val_add, ":foraged_food_at_site", ":temp_forage"),
				
				(party_get_slot, ":temp_forage", ":foraging_site", slot_center_acres_olives),
				(val_div, ":temp_forage", 1200), # 600 was too low, try 1200
				(val_add, ":foraged_food_at_site", ":temp_forage"),
				
				(party_get_slot, ":temp_forage", ":foraging_site", slot_center_acres_dates),
				(val_div, ":temp_forage", 960), # 480 was to low, try 960
				(val_add, ":foraged_food_at_site", ":temp_forage"),
				
				# Forage from herds
				(party_get_slot, ":temp_forage", ":foraging_site", slot_center_head_cattle),
				(val_div, ":temp_forage", 36),
				(val_add, ":foraged_food_at_site", ":temp_forage"),
				
				(party_get_slot, ":temp_forage", ":foraging_site", slot_center_head_sheep),
				(val_div, ":temp_forage", 60),
				(val_add, ":foraged_food_at_site", ":temp_forage"),
				
				# Forage from gardens and apiaries
				(party_get_slot, ":temp_forage", ":foraging_site", slot_center_household_gardens),
				(val_add, ":foraged_food_at_site", 2),
				
				(party_get_slot, ":temp_forage", ":foraging_site", slot_center_apiaries),
				(val_add, ":foraged_food_at_site", 1),
				
				# Forage game in traps
				(party_get_slot, ":temp_forage", ":foraging_site", slot_center_fur_traps),
				(val_add, ":foraged_food_at_site", ":temp_forage"),
				
				# Add amount foraged off the center to the total
				(val_add, ":foraged_food", ":foraged_food_at_site"),
				
				# DEBUG message to tweak values, uncomment to display
				#(str_store_party_name, s1, ":foraging_site"),
				#(assign, reg11, ":foraged_food_at_site"),
				#(display_message, "@DEBUG foraging: foraged {reg11} units from {s1}.", 0xFF00FF),
			  (try_end),
			(try_end), # end of centers loop
			
			# Check terrain for foraging from the countryside
			(party_get_current_terrain, ":cur_terrain", "p_main_party"),
			(try_begin),
			  (is_between, ":cur_terrain", rt_bridge, rt_desert_forest),
			  (assign, reg10, 4),
			(else_try),
			  (is_between, ":cur_terrain", rt_steppe, rt_plain),
			  (assign, reg10, 2),
			(else_try),
			  (assign, reg10, 0),
			(try_end),
			
			# Add foraged amount from countryside to total amount
			(val_add, ":foraged_food", reg10),
			
			# DEBUG message to tweak values, uncomment to display
			#(display_message, "@DEBUG foraging: foraged {reg10} units from countryside.", 0xFF00FF),
			
			# Tier Multiplier, foraging value multiplied by foraging skill tier bonus
			# Represent experience, less time to find forage means more food foraged
			(try_begin),
			  # between 2-4, x1.5 bonus
			  (gt, ":max_foraging_in_party", 1),
			  (lt, ":max_foraging_in_party", 5),
			  (val_mul, ":foraged_food", 3),
			  (val_div, ":foraged_food", 2),
			(else_try),
			  # between 5-7, x2 bonus
			  (gt, ":max_foraging_in_party", 4),
			  (lt, ":max_foraging_in_party"),
			  (val_mul, ":foraged_food", 2),
			(else_try),
			  # between 8-9, x2.5 bonus
			  (gt, ":max_foraging_in_party", 7),
			  (lt, ":max_foraging_in_party", 10),
			  (val_mul, ":foraged_food", 5),
			  (val_div, ":foraged_food", 2),
			(else_try),
			  # 10 and more, x3 bonus
			  (ge, ":max_foraging_in_party", 10),
			  (val_mul, ":foraged_food", 3),
			(try_end),
			
			# Apply Camp bonus x1.5 (represent more time to forage)
			(try_begin),
			  #(this_or_next|ge, "$current_camp_party", -1), # uncomment if using Entrenchment
			  (this_or_next|eq, "$g_camp_mode", 1),
			  (eq, "$g_siege_force_wait", 1),
			  (val_mul, ":foraged_food", 3),
			  (val_div, ":foraged_food", 2),
			(try_end),
			
			# Apply foraging limit according to skill level (modified by party bonus)
			(try_begin),
			  (gt, ":foraged_food", ":foraging_limit"),
			  (assign, ":foraged_food", ":foraging_limit"),
			(try_end),
			
			# assign amount foraged to register to deduct from party consumption
			(assign, reg4, ":foraged_food"),
			
			# End of foraging message
			(try_begin),
			  (gt, ":foraged_food", 0),
			  (str_store_troop_name, s2, ":max_skill_owner"),
			  (display_message, "@{s2} managed to forage {reg4} units of food to complement supplies.", 0x00FF00),
			(try_end),
		  (try_end),
		(try_end),
	]),
	## Jrider -
	
	#LAZERAS MODIFIED  {ENTK}
	# Jrider + Begin new scripts
	# TITLES v0.3.3 #####
	# script troop_set_title_according_to_faction_gender_and_lands
	# calculate and set new title for lords, ladies and companions
	# use s0 and s1
	# change v0.3: use s61 and reg10
	("troop_set_title_according_to_faction_gender_and_lands",
	  [
		(store_script_param, ":troop_no", 1),
		(store_script_param, ":faction_no", 2),
		(troop_get_type, ":gender", ":troop_no"),
		# Ensure we process only npcs member of a kingdom, including player
		(try_begin), # Npcs serving as lord and ladies
		  # v0.1 change +
		  (is_between, ":faction_no", kingdoms_begin, kingdoms_end), # normaly this one should exclude companions that are not vassals
		  (neg|is_between, ":troop_no", pretenders_begin, pretenders_end), # exclude pretenders
		  (this_or_next|is_between, ":troop_no", active_npcs_begin, kingdom_ladies_end), # v0.3.1 change to include player
		  (eq, ":troop_no", "trp_player"), # include player player # v0.3.1 change
		  (neq, ":troop_no", "trp_player"), # exclude player # v0.3.1 commented, wasn't relevant anyway
		  
		  (faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
		  (str_store_troop_name_plural, s0, ":troop_no"),
		  # v0.1 change -
		  # External computation blocks
		  # Get Gender
		  (troop_get_type, ":gender", ":troop_no"),
		  # NPC's largest fief (works for male and female, compute spouse fief as well)
		  # 1 no fief, 2 village, 3 castle, 4 town
		  (assign, ":largest_fief", 0),
		  (try_for_range, ":cur_center", centers_begin, centers_end),
			(troop_get_slot, ":spouse_no", ":troop_no", slot_troop_spouse),
			(neq, ":troop_no", ":faction_leader"), # exclude research for ruler
			(neq, ":spouse_no", ":faction_leader"), # exclude research for ruler's wife
			(lt, ":largest_fief", 3),
			(party_slot_ge, ":cur_center", slot_town_lord, 0),
			(this_or_next|party_slot_eq, ":cur_center", slot_town_lord, ":spouse_no"),
			(party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
			
			(try_begin),
			  (party_slot_eq, ":cur_center", slot_party_type, spt_town),
			  (lt, ":largest_fief", 3),
			  (assign, ":largest_fief", 3),
			(else_try),
			  (party_slot_eq, ":cur_center", slot_party_type, spt_castle),
			  (lt, ":largest_fief", 2),
			  (assign, ":largest_fief", 2),
			(else_try),
			  (party_slot_eq, ":cur_center", slot_party_type, spt_village),
			  (lt, ":largest_fief", 1),
			  (assign, ":largest_fief", 1),
			(try_end),
		  (try_end),
		  
		  # base title(s) computation blocks
		  # Determine NPCs quality in order of importance
		  # for male NPCs: 4 Ruler, 3 town, 2 castle, 1 village, 0 landless
		  # for female NPCs: 5 unmarried (kingdom lady only), 4 queen, 3 wife or town, 2 wife or castle, 1 wife or village, 0 wife or landless
		  (assign, ":quality", 0),
		  (troop_get_type, ":gender", ":troop_no"),
		  (try_begin), # Male npcs
			(eq, ":gender", 0),
			(try_begin),
			  (eq, ":troop_no", ":faction_leader"), # is king
			  (assign, ":quality", 4),
			(else_try),
			  (assign, ":quality", ":largest_fief"),
			(try_end),
		  (else_try), # Female npcs, a bit more complex queen, landowner, companions without a fief,
			(try_begin), # wife of faction leader
			  # v0.3.3 change +
			  (this_or_next|troop_slot_eq, ":troop_no", slot_troop_spouse, ":faction_leader"),
			  (eq, ":troop_no", ":faction_leader"), # is queen
			  # v0.3.3 change -
			  (assign, ":quality", 4),
			(else_try), # is a landowner - index 1 to 3
			  (gt, ":largest_fief", 0),
			  (assign, ":quality", ":largest_fief"),
			(else_try), # a companion vassal without fief
			  (is_between, ":troop_no", companions_begin, companions_end),
			  (assign, ":quality", 0),
			(else_try), # married lady whose husband has no fief
			  (troop_slot_ge, ":troop_no", slot_troop_spouse, 0),
			  (assign, ":quality", 0),
			(else_try), # unmarried lady without fief
			  (assign, ":quality", 5),
			(try_end),
		  (try_end),
		  
		  # v0.3 changes +
		  # compute troop relation to ruler suffix
		  (try_begin),
			(neq, ":troop_no", ":faction_leader"), # exclude from suffix if king v0.3.2 change
			(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
			(assign, ":relation", reg0),
			(str_clear, s61),
			(assign, reg10, 0),
			(try_begin), # update reg10
			  (this_or_next|gt, ":relation", 19),
			  (lt, ":relation", -19),
			  (assign, reg10, ":relation"),
			  (store_add, ":normalized_relation", ":relation", 100),
			  (store_div, ":str_offset", ":normalized_relation", 20),
			  (val_clamp, ":str_offset", 0, 10), # does 10 work ? only 10 strings in there
			  (store_add, ":str_rel_id", "str_ruler_relation_mnus_100_ns",  ":str_offset"),
			  (str_store_string, s61, ":str_rel_id"),
			(try_end),
		  (else_try), # clear register and string
			(str_clear, s61),
			(assign, reg10, 0),
		  (try_end),
		  # v0.3 changes -
		  
		  # Find title index in strings block
		  (store_sub, ":title_index", ":faction_no", kingdoms_begin), # 0 player, 1 swadian ...
		  (try_begin), #male, 5 title entries
			(troop_get_type, ":gender", ":troop_no"),
			(eq, ":gender", 0),
			(val_mul, ":title_index", 5),
			(val_add, ":title_index", kingdom_titles_male_begin),
		  (else_try), # female, 6 title entries
			(val_mul, ":title_index", 6),
			(val_add, ":title_index", kingdom_titles_female_begin),
		  (try_end),
		  (val_add, ":title_index", ":quality"),
		  
		  # Set title and party name block
		  # assign title
		  (str_store_string, s1, ":title_index"),
		  (troop_set_name, ":troop_no", s1),
		  # rename party
		  (troop_get_slot, ":troop_party", ":troop_no", slot_troop_leaded_party),
		  (try_begin),
			# v0.2 change to prevent opcode error
			(gt, ":troop_party", 0),
			(str_store_troop_name, s5, ":troop_no"),
			(party_set_name, ":troop_party", "str_s5_s_party"),
		  (try_end), # v0.2 change
		(try_end),
		
		# Special titles for companions not used as vassals
		(try_begin),
		  (neg|eq, ":faction_no", "fac_player_supporters_faction"), # v0.2 change
		  (neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero), # v0.3 change, exclude companion if he became a kingdom lord
		  (is_between, ":troop_no", companions_begin, companions_end),
		  # Store the plural name
		  (str_store_troop_name_plural, s0, ":troop_no"),
		  # Set the title
		  (try_begin), # Male npcs
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_player_companion),
			(str_store_string, s1, "str_hero_titles_party"),
		  (else_try),
			(call_script, "script_get_troop_specialisation", ":troop_no", ":faction_no"),
			(assign, ":title_index", reg0),
			(val_add, ":title_index", hero_titles_begin),
			(str_store_string, s1, ":title_index"),
		  (try_end),
		  # assign title
		  (troop_set_name, ":troop_no", s1),
		(try_end),
	]),
	
	# Script get_troop_specialisation
	# Assess companion current skills to find the strongest trend
	("get_troop_specialisation",
	  [
		(store_script_param, ":troop_no", 1),
		(store_script_param, ":faction_no", 2),
		(try_begin),
		  (neg|eq, ":faction_no", "fac_player_supporters_faction"), # v0.2 change
		  (is_between, ":troop_no", companions_begin, companions_end),
		  # Other titles according to function in group
		  # Scout (Ausculare) - PathFinding, Tracking and Spotting
		  (store_skill_level, ":scout", "skl_spotting", ":troop_no"),
		  (store_skill_level, ":scout_skill", "skl_pathfinding", ":troop_no"),
		  (val_add, ":scout", ":scout_skill"),
		  (store_skill_level, ":scout_skill", "skl_tracking", ":troop_no"),
		  (val_add, ":scout", ":scout_skill"),
		  
		  # Physician (Fisique) - Wound Treatment, Surgery, First Aid
		  (store_skill_level, ":physician", "skl_wound_treatment", ":troop_no"),
		  (store_skill_level, ":physician_skill", "skl_first_aid", ":troop_no"),
		  (val_add, ":physician", ":physician_skill"),
		  (store_skill_level, ":physician_skill", "skl_surgery", ":troop_no"),
		  (val_add, ":physician", ":physician_skill"),
		  
		  # Tactician (Tassein) - Tactics, Engineer, Trainer
		  (store_skill_level, ":tactician", "skl_tactics", ":troop_no"),
		  (store_skill_level, ":tactician_skill", "skl_engineer", ":troop_no"),
		  (val_add, ":tactician", ":tactician_skill"),
		  (store_skill_level, ":tactician_skill", "skl_trainer", ":troop_no"),
		  (val_add, ":tactician", ":tactician_skill"),
		  
		  # Trader (Empori) - Trade Looting, Foraging (foraging is a new skill I'm working on)
		  (store_skill_level, ":trader", "skl_trade", ":troop_no"),
		  (store_skill_level, ":trader_skill", "skl_looting", ":troop_no"),
		  (val_add, ":trader", ":trader_skill"),
		  #(store_skill_level, ":trader_skill", "skl_foraging", ":troop_no"), # uncomment if using foraging
		  #(val_add, ":trader", ":trader_skill"), # uncomment if using foraging
		  (val_mul, ":trader", 3), # comment if using foraging
		  (val_div, ":trader", 2), # comment if using foraging
		  
		  # Diplomat (Missi) - Persuasion
		  (store_skill_level, ":diplomat", "skl_persuasion", ":troop_no"),
		  (val_mul, ":diplomat", 3),
		  
		  (try_begin), # Just your basic hero
			(eq, ":diplomat", 0),
			(eq, ":tactician", 0),
			(eq, ":scout", 0),
			(eq, ":physician", 0),
			(eq, ":trader", 0),
			(assign, reg0, 0),
		  (else_try), # Diplomat - skilled in Persuasion and Trainer
			(gt, ":diplomat", 0),
			(ge, ":diplomat", ":tactician"),
			(ge, ":diplomat", ":scout"),
			(ge, ":diplomat", ":physician"),
			(ge, ":diplomat", ":trader"),
			(assign, reg0, 1),
		  (else_try), # Tactician - skilled in Tactics and Engineer
			(gt, ":tactician", 0),
			(ge, ":diplomat", ":scout"),
			(ge, ":diplomat", ":physician"),
			(ge, ":diplomat", ":trader"),
			(assign, reg0, 2),
		  (else_try), # Scout - skilled in Spotting, Tracking and Pathfinding
			(gt, ":scout", 0),
			(ge, ":diplomat", ":physician"),
			(ge, ":diplomat", ":trader"),
			(assign, reg0, 3),
		  (else_try), # Physician - skilled in Wound Treatment, Surgery and First Aid
			(gt, ":physician", 0),
			(ge, ":physician", ":trader"),
			(assign, reg0, 4),
		  (else_try), # Trader - skilled in Trade
			(gt, ":trader", 0),
			(assign, reg0, 5),
		  (try_end),
		(try_end),
	]),
	#LAZERAS MODIFIED  {ENTK}
	
	#LAZERAS MODIFIED  {Expanded Dialog Kit}
	## DIALOGS v1.0 #########################################################################
	## Script troop_get_relation_to_player_string (to include in dialogs)
	## Use reg0, reg1 (unused here, though can be used to set a display context or use the faction relation number)
	## fills s60 for storage of troop relation and s61 for storage of faction relation
	("get_relation_to_player_string",
	  [
		(store_script_param, ":target_no", 1),
		(store_script_param, ":troop_or_faction", 2),
		
		(assign, reg0, 0),
		(assign, reg1, 0),
		(try_begin), # target is troop
		  (eq, ":troop_or_faction", 0),
		  (str_clear, s60),
		  
		  (call_script, "script_troop_get_player_relation", ":target_no"),
		  (assign, ":relation", reg0),
		  
		  (store_add, ":normalized_relation", ":relation", 100),
		  (val_add, ":normalized_relation", 5),
		  (store_div, ":str_offset", ":normalized_relation", 10),
		  (val_clamp, ":str_offset", 0, 20), # does 20 works ? only 20 strings in there
		  (store_add, ":str_rel_id", "str_relation_mnus_100_ns",  ":str_offset"),
		  
		  ## Make something if troop has relation but not strong enought to warrant a string
		  (try_begin),
			(neq, ":str_rel_id", "str_relation_plus_0_ns"),
			(str_store_string, s60, ":str_rel_id"),
		  (else_try),
			(neg|eq, reg0, 0),
			(str_is_empty, s60),
			(str_store_string, s60, "@ knows of you"),
		  (try_end),
		(else_try), # target is Faction
		  (eq, ":troop_or_faction", 1),
		  (str_clear, s61),
		  
		  (store_relation, ":relation", "fac_player_supporters_faction", ":target_no"),
		  (try_begin), # update reg0
			(neg|eq, ":relation", 0),
			(assign, reg1, ":relation"),
		  (try_end),
		  
		  (store_add, ":normalized_relation", ":relation", 100),
		  (store_div, ":str_offset", ":normalized_relation", 10),
		  (val_clamp, ":str_offset", 0, 20),
		  (store_add, ":str_rel_id", "str_faction_relation_mnus_100_ns",  ":str_offset"),
		  (str_store_string, s61, ":str_rel_id"),
		(try_end),
	]),
	
	## Script change_looking_for_dialog_string
	## Modify string s1
	## Use s60 (from relation script), s3, s5, s6
	## Use reg0, reg1 and reg4
	("change_looking_for_dialog_string",
	  [
		(store_script_param, ":troop_no", 1),
		
		## Get general relation to use in name strings
		(call_script, "script_get_relation_to_player_string", ":troop_no", 0),
		
		## Add family relationship for ladies and relation to player computed earlier and prisoner status
		(try_begin), ## wife of | relation
		  (is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end), # gender check, only for ladies
		  (troop_slot_ge, ":troop_no", slot_troop_spouse, 0),
		  (troop_get_slot, ":spouse_of", ":troop_no", slot_troop_spouse),
		  (str_store_troop_name, s3, ":spouse_of"),
		  (str_store_string, s1, "@{s1}, wife of {s3}{reg0?,{s60}:}"),
		(else_try), ## unmarried daughter/sister of | relation
		  (is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end), # gender check, for ladies only
		  (troop_slot_eq, ":troop_no", slot_troop_spouse, -1), # unmarried ones
		  (assign, reg1, -1),
		  (try_begin),
			(troop_slot_ge, ":troop_no", slot_troop_father,0), # daughters first
			(troop_get_slot, ":daughter_of", ":troop_no", slot_troop_father),
			(str_store_troop_name, s3, ":daughter_of"),
			(assign, reg1, 1),
		  (else_try),
			(troop_slot_ge, ":troop_no", slot_troop_guardian,0), # else sister or niece
			(troop_get_slot, ":sister_of", ":troop_no", slot_troop_guardian),
			(str_store_troop_name, s3, ":sister_of"),
			(assign, reg1, 0),
		  (try_end),
		  
		  # check if betrothed
		  (assign, reg4, 0),
		  (try_begin),
			(troop_slot_ge, ":troop_no", slot_troop_betrothed, 0),
			(troop_get_slot, ":fiance", ":troop_no", slot_troop_betrothed),
			(str_store_troop_name, s5, ":fiance"),
			(assign, reg4, 1),
		  (try_end),
		  (str_store_string, s1, "@{s1}, {reg1?daughter of:pupil of} {s3}{reg4?, betrothed to {s5}:}{reg0?,{s60}:}"),
		  ## For prisoners
		(else_try), # male
		  (neg|is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
		  
		  (assign, reg1, 0),
		  (assign, reg4, 0),
		  
		  (try_begin), # check if both parents are assigned
			(troop_slot_ge, ":troop_no", slot_troop_father, 0),
			(troop_slot_ge, ":troop_no", slot_troop_mother, 0),
			
			(troop_get_slot, ":father", ":troop_no", slot_troop_father),
			(troop_get_slot, ":mother", ":troop_no", slot_troop_mother),
			(is_between, ":father", active_npcs_begin, active_npcs_end), # keep only if active npc
			(is_between, ":mother", active_npcs_begin, kingdom_ladies_end), # keep only if active npc
			
			(str_store_troop_name, s3, ":father"),
			(str_store_troop_name, s6, ":mother"),
			
			(assign, reg4, 1,),
			(str_store_string, s5, "@{s3} and {s6}"),
		  (else_try),
			(troop_slot_ge, ":troop_no", slot_troop_father, 0),
			(troop_get_slot, ":father", ":troop_no", slot_troop_father),
			(is_between, ":father", active_npcs_begin, active_npcs_end), # keep only if active npc
			
			(str_store_troop_name, s3, ":father"),
			(assign, reg4, 1,),
			(str_store_string, s5, "@{s3}"),
		  (else_try),
			(troop_slot_ge, ":troop_no", slot_troop_mother, 0),
			(troop_get_slot, ":mother", ":troop_no", slot_troop_mother),
			(is_between, ":mother", active_npcs_begin, kingdom_ladies_end), # keep only if active npc
			
			(str_store_troop_name, s3, ":mother"),
			(assign, reg4, 1,),
			(str_store_string, s5, "@{s3}"),
		  (try_end),
		  
		  # prisoner
		  (try_begin),
			(troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
			(assign, reg1, 1),
		  (try_end),
		  
		  (str_store_string, s1, "@{s1}{reg4?, son of {s5}{reg1?,:{reg0?,:}}:}{reg1? prisoner{reg0?,:}:}{reg0?{s60}:}"),
		(try_end),
	]),
	
	## Script change_minstrel_maiden_dialog_string
	## Modify string s10
	## Use s60 (from relation script), s3 and s5
	## Use reg0, reg1 and reg4
	("change_minstrel_maiden_dialog_string",
	  [
		(store_script_param, ":troop_no", 1),
		
		## Get general relation to use in name strings
		(call_script, "script_get_relation_to_player_string", ":troop_no", 0),
		
		## modify maiden display name to include closest male relative and current relation with player
		(assign, reg1, -1),
		(try_begin),
		  (troop_slot_ge, ":troop_no", slot_troop_father,0), # daughters first
		  (troop_get_slot, ":daughter_of", ":troop_no", slot_troop_father),
		  (str_store_troop_name, s3, ":daughter_of"),
		  (assign, reg1, 1),
		(else_try),
		  (troop_slot_ge, ":troop_no", slot_troop_guardian,0), # else sister or niece
		  (troop_get_slot, ":sister_of", ":troop_no", slot_troop_guardian),
		  (str_store_troop_name, s3, ":sister_of"),
		  (assign, reg1, 0),
		(try_end),
		
		# check if betrothed
		(assign, reg4, 0),
		(try_begin),
		  (troop_slot_ge, ":troop_no", slot_troop_betrothed, 0),
		  (troop_get_slot, ":fiance", ":troop_no", slot_troop_betrothed),
		  (str_store_troop_name, s5, ":fiance"),
		  (assign, reg4, 1),
		(try_end),
		## Modify the display string
		(str_store_string, s10, "@{s10}, {reg1?daughter of:pupil of} {s3}{reg4?, betrothed to {s5}:}{reg0?,{s60}:}"), #Floris - bugfix was {ss5}
	]),
	
	## Script set_diplomatic_emissary_skill_level_string
	## diplomatic emissary is evaluated by tiers of the Persuation skill
	## Use s65
	## Replace s11
	## Note: this one is in a slightly unfinished state, as it provides only persusuation skill strings,
	##       the idea is to extend it other skills, like spotting which is used in diplomacy for some mission types
	("set_diplomatic_emissary_skill_level_string",
	  [
		(store_script_param, ":troop_no", 1),
		(store_script_param, ":skill_selected", 2),
		(store_script_param, ":set_title", 3), # don't forget to reset at end of mission
		
		# store plural name of troop, (ie. without the title)
		(str_store_troop_name_plural, s65, ":troop_no"),
		
		(try_begin),
		  # get skill level
		  (store_skill_level, ":skill_level", ":skill_selected", ":troop_no"),
		  
		  # get title index according to tiers of the selected skill
		  (assign, ":title_index", -1), # no change by default
		  (try_begin),
			(eq, ":skill_level", 1), # tier 0, novice
			(assign, ":title_index", 0),
			(str_store_string, s65, "@Messenger {s65}"),
		  (else_try), # tier 1, between 2-4, some experience
			(is_between, ":skill_level", 2, 4),
			(assign, ":title_index", 1),
			(str_store_string, s65, "@Envoy {s65}"),
		  (else_try),  # tier 2, between 5-7, good experience
			(is_between, ":skill_level", 5, 7),
			(assign, ":title_index", 2),
			(str_store_string, s65, "@Consul {s65}"),
		  (else_try),  # tier 3, between 8-9, very good experience
			(is_between, ":skill_level", 8, 9),
			(assign, ":title_index", 3),
			(str_store_string, s65, "@Legate {s65}"),
		  (else_try),  # tier 4, 10 or higher, the best
			(ge, ":title_index", 10),
			(assign, ":title_index", 4),
			(str_store_string, s65, "@Missi Dominici {s65}"),
		  (try_end),
		  
		  # TODO: use strings
		  
		  # replace dialog display string (only if there's something to change)
		  (try_begin),
			(ge, ":title_index", 0),
			(str_store_string, s11, "@{s65}"),
			
			# set title if you want to keep it
			(eq, ":set_title", 1),
			(troop_set_name, ":troop_no", s65),
		  (else_try), # reset standard troop name in s11
			(str_store_troop_name, s11, ":troop_no"),
		  (try_end),
		(try_end),
	]),
	
	## Script change_diplomatic_action_ruler_kingdom_strings
	## Add ruler's relation to you and kingdom's relation in dialog string
	## Modify s10 (ruler relation) and s1 (kingdom relation)
	## Use s60 and s61 from get_relation_to_player
	## Modify s10 (for ruler relation) and s11 (for kingdom relation)
	("change_diplomatic_action_ruler_kingdom_strings",
	  [
		(store_script_param, ":target_ruler", 1),
		(store_script_param, ":target_faction", 2),
		
		## Get general relation to use in ruler name string
		(call_script, "script_get_relation_to_player_string", ":target_ruler", 0),
		
		## Get faction relation to use in kingdom string
		(call_script, "script_get_relation_to_player_string", ":target_faction", 1),
		
		# replace dialog display strings
		(str_store_string, s10, "@{s10}{reg0? (who{s60}):}"),
		(str_store_string, s11, "@{s11} ({s61})"),
	]),
	#LAZERAS MODIFIED  {Expanded Dialog Kit}
                                                     
	#LAZERAS MODIFIED  {Top Tier Troops Recruit}
	# ##script_upgrade_troop_to_hero
	# ##usage   : (call_script,"script_upgrade_troop_to_hero",<troop_ID>,<hero_ID>),
	# ##Input 1 : <troop_ID> should be one of troop_id of top tier troop
	# ##Input 2 : <hero_ID> should be one of troop_id of inactive hero on module_troops.py
	# ##This must be passed.  The code block calling this script should have already checked if there is that troop.
	# ##Output: None, will adjust p_main_party
	# ##May call a dialog to communicate this happening
	("upgrade_troop_to_hero",
	  [(store_script_param,":troop_id",1),
		(store_script_param,":hero_id",2),
		(try_begin),
		  (main_party_has_troop, ":troop_id"),
		  (troop_slot_eq, ":hero_id", slot_troop_occupation, ":troop_id"),
		  (troop_set_slot,":hero_id", slot_troop_occupation, slto_player_companion),
		  (party_remove_members,"p_main_party",":troop_id",1),      # ##remove the regular troop
		  (party_add_members,"p_main_party",":hero_id",1),          # ##Add the hero found
		(try_end),
	]),
	#LAZERAS MODIFIED  {Top Tier Troops Recruit}

                      

# script_mmfix_item_max_amount
# This script was developed as a workaround for the fact that troop_inventory_slot_get_item_max_amount is not working with modmergered scripts. - Windyplains
# INPUTS:  troop_id, inventory_slot
# OUTPUTS: reg0 (max amount)
("mmfix_item_max_amount",
[
	(store_script_param, ":troop_id", 1),
	(store_script_param, ":inv_slot", 2),
	(troop_inventory_slot_get_item_max_amount, reg0, ":troop_id", ":inv_slot"),
]),					  
  
  ## Floris - Trade Ledger
  ("trade_ledger_create",	
   [
    (store_script_param_1, ":troop"),
	(call_script, "script_array_create"),
	(assign, ":ledger", reg0),
	(party_set_slot, ":ledger", slot_party_type, spt_array),
	(str_store_troop_name_plural, s0, ":troop"),
	(party_set_name, ":ledger", "@{s0} Trade Ledger Array"), #For DEBUG
	(troop_set_slot, ":troop", slot_troop_trade_ledger, ":ledger"),
	(try_begin), #Not really needed yet...but maybe eventually
		(neq, ":troop", "trp_player"),
		(troop_get_slot, ":owner", ":troop", slot_troop_leaded_party),
		(gt, ":owner", 0),
		(party_is_active, ":owner"),
		(call_script, "script_array_set_owner", ":ledger", ":owner"),
	(try_end),
	(str_clear, s0),
	(try_for_range, ":unused", 0, num_ledger_sub_arrays),
		(call_script, "script_array_create"),
		(call_script, "script_array_pushback", ":ledger", reg0), #Add value at end
		(call_script, "script_array_set_owner", reg0, ":ledger"),
		(party_set_name, reg0, s0),
	(try_end), 
	
	(assign, reg0, ":ledger"),
   ]),	

 ("trade_ledger_write",
   [
    (store_script_param_1, ":num_entries"),
	(store_script_param_2, ":troop"),
	(try_begin),
	    (troop_slot_ge, ":troop", slot_troop_trade_ledger, 1),
		(troop_get_slot, ":ledger", ":troop", slot_troop_trade_ledger),
		(call_script, "script_cf_array_is_array", ":ledger"),
	(else_try),
	    (call_script, "script_trade_ledger_create", ":troop"),
	    (assign, ":ledger", reg0),
	(try_end),
	
	(call_script, "script_array_get_element", ":ledger", date_array),
	(assign, ":date_array", reg0),
	(call_script, "script_array_get_element", ":ledger", town_array),
	(assign, ":town_array", reg0),
	(call_script, "script_array_get_element", ":ledger", item_array),
	(assign, ":item_array", reg0),
	(call_script, "script_array_get_element", ":ledger", destination_array),
	(assign, ":destination_array", reg0),
	(call_script, "script_array_get_element", ":ledger", profit_array),
	(assign, ":profit_array", reg0),
	
	(store_current_hours, ":cur_hours"),	
	(assign, ":params_begin", 3), #1 is number of entries, 2 is troop, 3 is first item
	(try_for_range, ":unused", 0, ":num_entries"),
		(call_script, "script_array_insert", ":date_array", 0, ":cur_hours"),
	    (call_script, "script_array_insert", ":town_array", 0, "$current_town"),
		(store_add, ":params_end", ":params_begin", 3),
	    (try_for_range, ":param", ":params_begin", ":params_end"),
			(store_script_param, ":value", ":param"),
			(store_sub, reg1, ":param", ":params_begin"),
			(eq, reg1, 0), #Item ID
			(call_script, "script_array_insert", ":item_array", 0, ":value"),
		(else_try),
			(eq, reg1, 1), #Dest Town
			(call_script, "script_array_insert", ":destination_array", 0, ":value"),
		(else_try),
			(eq, reg1, 2), #Profit
			(call_script, "script_array_insert", ":profit_array", 0, ":value"),			
		(try_end), #Item Details Loop
		(assign, ":params_begin", ":params_end"),
    (try_end), #Entries Loop
   ]),

  ("cf_trade_ledger_trim_entries",
   [
    (store_script_param_1, ":troop"),
	(store_script_param_2, ":condition"), #Num of Days, Item, or Town, or Profit Level
	(store_script_param, ":trim_type", 3),

	(troop_get_slot, ":ledger", ":troop", slot_troop_trade_ledger),
	(ge, ":ledger", 1),
	(call_script, "script_cf_array_is_array", ":ledger"),
	
	(call_script, "script_array_get_element", ":ledger", date_array),
	(assign, ":date_array", reg0),
	(call_script, "script_array_get_element", ":ledger", town_array),
	(assign, ":town_array", reg0),
	(call_script, "script_array_get_element", ":ledger", item_array),
	(assign, ":item_array", reg0),
	(call_script, "script_array_get_element", ":ledger", destination_array),
	(assign, ":destination_array", reg0),
	(call_script, "script_array_get_element", ":ledger", profit_array),
	(assign, ":profit_array", reg0),	
	
	(call_script, "script_array_get_size", ":date_array"),
	(assign, ":ledger_length", reg0),
	
	(call_script, "script_array_get_element", ":ledger", ":trim_type"),
	(assign, ":target_array", reg0),	
	
	(try_begin),
	    (this_or_next|eq, ":trim_type", date_array),
		(eq, ":trim_type", profit_array),
		(try_begin),
		    (eq, ":trim_type", date_array),
			(store_current_hours, ":cur_hours"),
			(val_mul, ":condition", 24),
			(store_sub, ":condition", ":cur_hours", ":condition"),
			(val_add, ":condition", 12), #Just to be a bit on the liberal side of keeping entries	
        (try_end),	
		(try_for_range_backwards, ":i", 0, ":ledger_length"),
			(call_script, "script_cf_array_get_element", ":target_array", ":i"),
			(lt, reg0, ":condition"), #older than the cutoff point / less than profit
			(call_script, "script_cf_array_remove", ":date_array", ":i"),
			(call_script, "script_cf_array_remove", ":town_array", ":i"),
			(call_script, "script_cf_array_remove", ":item_array", ":i"),
			(call_script, "script_cf_array_remove", ":destination_array", ":i"),
			(call_script, "script_cf_array_remove", ":profit_array", ":i"),	
		(try_end),
	(else_try),
	    (is_between, ":trim_type", town_array, profit_array), #item or prod/demand towns
		(try_for_range_backwards, ":i", 0, ":ledger_length"),
			(call_script, "script_cf_array_get_element", ":target_array", ":i"),
			(eq, reg0, ":condition"), #matches item or town
			(call_script, "script_cf_array_remove", ":date_array", ":i"),
			(call_script, "script_cf_array_remove", ":town_array", ":i"),
			(call_script, "script_cf_array_remove", ":item_array", ":i"),
			(call_script, "script_cf_array_remove", ":destination_array", ":i"),
			(call_script, "script_cf_array_remove", ":profit_array", ":i"),	
		(try_end),	
	(try_end),
	
	(call_script, "script_array_get_size", ":date_array"),
	(store_sub, reg0, ":ledger_length", reg0), #Number of Entries Removed
	(gt, reg0, 0),
   ]),

  ("cf_trade_ledger_custom_assess_item",
   [
    (store_script_param_1, ":item"),
	(store_script_param_2, ":index"),
	(try_begin),
	    (troop_slot_ge, "trp_player", slot_troop_trade_ledger, 1),
		(troop_get_slot, ":ledger", "trp_player", slot_troop_trade_ledger),
		(call_script, "script_cf_array_is_array", ":ledger"),
	(else_try),
	    (call_script, "script_trade_ledger_create", "trp_player"),
	    (assign, ":ledger", reg0),
	(try_end),
    
	(ge, ":index", custom_assess_begin),
    (assign, ":item_added", 0),	
	(try_begin),
	    (call_script, "script_cf_array_get_element", ":ledger", ":index"),
		(is_between, reg0, trade_goods_begin, trade_goods_end),
		(call_script, "script_cf_array_set_element", ":ledger", ":index", ":item"),
		(assign, ":item_added", 1),	
	(else_try),
	    (call_script, "script_cf_array_insert", ":ledger", ":index", ":item"),
		(assign, ":item_added", 1),	
	(try_end),
	(eq, ":item_added", 1),
   ]),	
  
 ("cf_trade_ledger_custom_assess_duplicates",
   [
	#Test for duplication among custom assesment items
	(troop_get_slot, ":ledger", "trp_player", slot_troop_trade_ledger),
	(ge, ":ledger", 1),
	(call_script, "script_cf_array_is_array", ":ledger"),
	(assign, ":dupe_removed", 0),
	(call_script, "script_get_max_skill_of_player_party", "skl_trade"),
	(assign, ":max_skill", reg0),
	(val_max, ":max_skill", 1), #at least 1 
	(val_add, ":max_skill", custom_assess_begin), ##do i need to add another +1?
	(try_for_range, ":index", custom_assess_begin, ":max_skill"),
		(call_script, "script_cf_array_get_element", ":ledger", ":index"),
		(assign, ":item", reg0),
		(try_for_range_backwards, ":i", custom_assess_begin, ":max_skill"),
			(neq, ":i", ":index"),
			(call_script, "script_cf_array_get_element", ":ledger", ":i"),
			(eq, reg0, ":item"),
			(call_script, "script_cf_array_remove", ":ledger", ":i"),
			(assign, ":dupe_removed", 1),
		(try_end),
	(try_end),
	(eq, ":dupe_removed", 1),
   ]),
   ## Floris - Trade Ledger End  
  
  ## Floris - Trade with Merchant Caravans  
  # script_merchant_inventory_to_party_slot
  # Input: arg1 = merchant_troop_id, arg2 = party_no
  # Output: none
  ("merchant_inventory_to_party_slot",
   [
	(store_script_param_1, ":merchant_troop"),
	(store_script_param_2, ":party_no"),
	
  	(assign, ":num_goods", 0),
	(troop_get_inventory_capacity, ":cap", ":merchant_troop"),
	(try_for_range, ":i", 0, ":cap"),
	    (troop_get_inventory_slot, ":item", ":merchant_troop", ":i"),
		(gt, ":item", 0),
		(item_get_type, ":type", ":item"),
		(eq, ":type", itp_type_goods),
		(val_add, ":num_goods", 1),
		(store_add, ":end", ":cap", 1),
		(try_for_range, ":n", 1, ":end"),
		    (store_add, ":slot", slot_town_trade_good_productions_begin, ":n"),
			(party_slot_eq, ":party_no", ":slot", 0),
			(party_set_slot, ":party_no", ":slot", ":item"),
			#(str_store_item_name, s0, ":item"), #DEBUG
		    #(assign, reg0, ":slot"), #DEBUG
	        #(display_message, "@Party stores {s0} in slot {reg0}"), #DEBUG
			(assign, ":end",0),		
		(try_end), #Slot Loop
	(try_end), #Inventory Loop
	(party_set_slot, ":party_no", slot_town_trade_good_productions_begin, ":num_goods"),
	(troop_clear_inventory, ":merchant_troop"),
   ]),
   
  # script_merchant_inventory_from_party_slot
  # Input: arg1 = merchant_troop_id, arg2 = party_no
  # Output: none
  ("merchant_inventory_from_party_slot",
   [
	(store_script_param_1, ":merchant_troop"),
	(store_script_param_2, ":party_no"),
	
	(troop_clear_inventory, ":merchant_troop"),
	
  	(party_get_slot, ":num_goods", ":party_no", slot_town_trade_good_productions_begin),
	(val_add, ":num_goods", 1),
	(troop_ensure_inventory_space, ":merchant_troop", ":num_goods"),
	(try_for_range, ":i", 1, ":num_goods"),
		(store_add, ":slot", slot_town_trade_good_productions_begin, ":i"),
		(party_slot_ge, ":party_no", ":slot", 1),
		(party_get_slot, ":item", ":party_no", ":slot"),
		#(str_store_item_name, s0, ":item"), #DEBUG
		#(assign, reg0, ":slot"), #DEBUG
	    #(display_message, "@Party Carries {s0} in slot {reg0}"), #DEBUG
		(troop_add_item, ":merchant_troop", ":item"),
		(party_set_slot, ":party_no", ":slot", 0),
	(try_end), #Slot Loop
	(troop_sort_inventory, ":merchant_troop"),
   ]),
   
  # script_refresh_travelling_merchant_inventory
  # Input: arg1 = merchant_party_no
  # Output: none
  ("refresh_travelling_merchant_inventory",
    [
      (store_script_param_1, ":party_no"),
	  (assign, ":profit", reg1), #From do_merchant_town_trade (this is the value that tariffs are taken from)
	  #(display_message, "@Profit {reg1}"), #DEBUG	  
      (party_get_slot, ":town_no", ":party_no", slot_party_last_traded_center),
	  (assign, ":merchant_troop", "trp_temp_troop"),
	  
	  (val_div, ":profit", 2),
	  (party_get_slot, ":num_goods", ":party_no", slot_town_trade_good_productions_begin),
	  (val_mul, ":profit", ":num_goods"),
	  (val_div, ":profit", num_merchandise_goods / 3), #Scale profit based on number of goods carried, normalized
	  (call_script, "script_merchant_inventory_from_party_slot", ":merchant_troop", ":party_no"),
	  (troop_clear_inventory, ":merchant_troop"), #Clear's party's previous inventory
	  
	  (reset_item_probabilities,0),
      (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
      (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
	    (call_script, "script_center_get_production", ":town_no", ":cur_goods"),
		(assign, ":cur_probability", reg0),
	    (call_script, "script_center_get_consumption", ":town_no", ":cur_goods"),
		(val_add, ":cur_probability", reg0),
	  
	    (try_begin),
			(this_or_next|eq, ":cur_goods", "itm_trade_cattle_meat"),
            (this_or_next|eq, ":cur_goods", "itm_trade_chicken"),
		    (eq, ":cur_goods", "itm_trade_pork"),
			(assign, ":cur_probability", 0),
	    (try_end),
	  
	    (val_mul, ":cur_probability", 3),
	  
        (store_add, ":cur_price_slot", ":cur_goods", ":item_to_price_slot"),
        (party_get_slot, ":cur_price", ":party_no", ":cur_price_slot"),
        (val_mul, ":cur_probability", average_price_factor),
        (val_div, ":cur_probability", ":cur_price"),
        (val_mul, ":cur_probability", average_price_factor),
        (val_div, ":cur_probability", ":cur_price"),
        (val_mul, ":cur_probability", average_price_factor),
        (val_div, ":cur_probability", ":cur_price"),
#        (val_mul, ":cur_probability", average_price_factor),
#        (val_div, ":cur_probability", ":cur_price"),
        (set_item_probability_in_merchandise, ":cur_goods", ":cur_probability"),
      (try_end),

	  (store_random_in_range, ":number_of_goods", num_merchandise_goods / 4, num_merchandise_goods / 2),
	  (try_begin),
		(party_get_slot, ":party_prosperity", ":party_no", slot_town_prosperity),
		(store_div, ":prosperity_mod", ":party_prosperity", 10), #up to 5
		(val_add, ":number_of_goods", ":prosperity_mod"),
	  (try_end),

      (troop_add_merchandise, ":merchant_troop", itp_type_goods, ":number_of_goods"),
      (troop_ensure_inventory_space, ":merchant_troop", ":number_of_goods"),
	  (troop_sort_inventory, ":merchant_troop"),

	  (call_script, "script_merchant_inventory_to_party_slot", ":merchant_troop", ":party_no"),

	  (party_get_slot, ":wealth", ":party_no", slot_town_wealth),
	  ## Floris - Companion Caravans
	  # (try_begin),
	    # (party_stack_get_troop_id, ":leader", ":party_no", 0),
		# (is_between, ":leader", companions_begin, companions_end),
	    # (party_slot_eq, ":party_no", 1, -1), #Hire Initial
		# (val_sub, ":wealth", 1500),
		# (party_set_slot, ":party_no", 1, 0),
		# (store_random_in_range, ":rand", 10, 30),
		# (party_add_members, ":party_no", "trp_mercenary_n_page", ":rand"),
	  # (try_end),
	  ## Floris - Companion Caravans
	  (val_add, ":wealth", ":profit"),
	  (store_sub, ":wealth_to_prosperity", ":wealth", 1000),
	  (try_begin),
	    (gt, ":wealth_to_prosperity", 1000),
		(store_mod, ":remainder", ":wealth_to_prosperity", 500),
		(val_sub, ":wealth", ":wealth_to_prosperity"),
		(val_add, ":wealth", ":remainder"),
		(val_div, ":wealth_to_prosperity", 500),
		(try_begin),
		    (store_party_size_wo_prisoners, ":size", ":party_no"),
			(lt, ":size", 60),
			(val_div, ":size", 10),
			(store_random_in_range, ":rand", 0, 10),
			(val_sub, ":rand", ":size"),
		    (ge, ":rand", 6),
			##Floris MTT begin
			(try_begin),
				(eq, "$troop_trees", troop_trees_0),
				(party_add_members, ":party_no", "trp_mercenary_n_page", ":wealth_to_prosperity"), #At least 2
			(else_try),
				(eq, "$troop_trees", troop_trees_1),
				(party_add_members, ":party_no", "trp_mercenary_r_page", ":wealth_to_prosperity"), #At least 2
			(else_try),
				(eq, "$troop_trees", troop_trees_2),
				(party_add_members, ":party_no", "trp_mercenary_e_page", ":wealth_to_prosperity"), #At least 2
			(try_end),
			#(display_message, "@{reg0} guards added."), #DEBUG
		(else_try),
			(val_add, ":party_prosperity", ":wealth_to_prosperity"),
			(val_clamp, ":party_prosperity", 0, 101),
		(try_end),
	  (try_end),
	  (party_set_slot, ":party_no", slot_town_wealth, ":wealth"),
	  (party_set_slot, ":party_no", slot_town_prosperity, ":party_prosperity"),  
  ]), 

  # script_trade_with_travelling_merchant
  # Input: arg1 = begin or end; arg2 = trading penalty state
  # Output: none
  ("trade_with_travelling_merchant", 
   [
    (store_script_param_1, ":state"),
	(assign, ":merchant_troop", "$g_talk_troop"),
	
  	(try_begin),
	    (eq, ":state", begin),		
		(call_script, "script_copy_inventory", ":merchant_troop", "trp_temp_troop"),

		(call_script, "script_merchant_inventory_from_party_slot", ":merchant_troop", "$g_encountered_party"), #Give merchant trade goods
		(store_troop_gold, ":gold", ":merchant_troop"),
	    (troop_remove_gold, ":merchant_troop", ":gold"),		
		(party_get_slot, ":wealth", "$g_encountered_party", slot_town_wealth),
		#(assign, reg0, ":wealth"), #DEBUG
		#(display_message, "@Has {reg0} gold"), #DEBUG
		(troop_add_gold, ":merchant_troop", ":wealth"),
		
		(try_for_range, ":i", ek_item_0, ek_food), #Double check merchant's gear is gone
		    (agent_get_item_slot, ":item", "$g_talk_agent", ":i"),
		    (gt, ":item", 0),
			(troop_remove_item, "$g_talk_troop", ":item"),
		(try_end),
		
		(store_script_param_2, reg60), #Forced trading penalty
		(change_screen_trade),		
	(else_try),
	    (eq, ":state", end),
		(call_script, "script_merchant_inventory_to_party_slot", ":merchant_troop", "$g_encountered_party"), #Store trade goods
		 
		(party_get_slot, ":wealth", "$g_encountered_party", slot_town_wealth),
		(store_troop_gold, ":gold", ":merchant_troop"),
	    (party_set_slot, "$g_encountered_party", slot_town_wealth, ":gold"), 
		(troop_remove_gold, ":merchant_troop", ":gold"),	
        (try_begin),
		    (lt, reg60, 4), #Not forced to trade
			(troop_slot_ge, "trp_player", slot_troop_renown, 200), #Player is memorable enough to matter
            (val_sub, ":wealth", ":gold"),
			(val_abs, ":wealth"),
			(val_div, ":wealth", 100),
			(gt, ":wealth", 0),
			(store_random_in_range, ":relation_change", 0, 3),
			(gt, ":relation_change", 0),
			(val_mul, ":relation_change", ":wealth"),
			(call_script, "script_change_player_relation_with_center", "$g_encountered_party", ":relation_change"),
        (try_end),		
		
		(call_script, "script_copy_inventory", "trp_temp_troop", ":merchant_troop"),	
		(assign, reg60, 0), #Reset forced trading penalty
	(try_end),   
   ]), 
  ## Floris - Trade with Merchant Caravans 

  
	#Script initialize fog, used to make fog of war optional
    ("initialize_fog", 
   [
	(try_for_range, ":center_no", centers_begin, spawn_points_begin),
		(eq, "$g_fog", 0),
		(party_set_flags, ":center_no", pf_always_visible, 1),
	(else_try),
		(eq, "$g_fog", 1),
		(party_slot_eq, ":center_no", slot_center_explored, 0),
		(party_set_flags, ":center_no", pf_always_visible, 0),	
	(try_end),
	]),
 
	# Floris reports

	("initialize_reports",
	[
	(store_script_param_1, ":input"),
	
	(try_begin),
		(eq, ":input", 1),																	#Character Report
		(troop_get_slot, reg1, "trp_player", slot_troop_renown),
		(assign, reg2, "$player_honor"),
		(str_store_string, s11, "@Character Renown: {reg1}^Honor Rating: {reg2}"),
		
		(assign, reg1, "$player_right_to_rule"),
		(str_store_string, s11, "@{s11}^^Your right to rule is {reg1}."),
			(assign, ":num_friends", 0),
		(assign, ":num_enemies", 0),
		(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
			(this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive_pretender),
			(call_script, "script_troop_get_player_relation", ":troop_no"),
			(assign, ":player_relation", reg0),
			(try_begin),
				(gt, ":player_relation", 20),
				(val_add, ":num_friends", 1),
			(else_try),
				(lt, ":player_relation", -20),
				(val_add, ":num_enemies", 1),
			(try_end),
		(try_end),			
		(assign, reg1, ":num_friends"),
		(assign, reg2, ":num_enemies"),
		(str_store_string, s11, "@{s11}^^You have {reg1} friends.^You have {reg2} enemies."),
		
		(call_script, "script_get_number_of_hero_centers", "trp_player"),
		(str_store_string, s11, "@{s11}^^You own {reg0} centers."),
		
		(try_begin),
			(gt, "$players_kingdom", 0),
			(str_store_faction_name, s12, "$players_kingdom"),
			(try_begin),
				(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
				(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
				(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
				(str_store_string, s11, "@{s11}^^You are a co-ruler of the {s12} faction."),
			(else_try),
				(this_or_next|is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
				(neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
				(str_store_string, s11, "@{s11}^^You are a member of the {s12} faction."),
			(else_try),
				(str_store_string, s11, "@{s11}^^You are the ruler of the {s12} faction."),
			(try_end),
		(else_try),
			(str_store_string, s11, "@{s11}^^You are not part of any faction."),
		(try_end),			
		
		(try_begin),
			(player_has_item, "$g_player_reading_book"),
			(str_store_item_name, s13, "$g_player_reading_book"),				
			(str_store_string, s11, "@{s11}^^You are currently reading: {s13}."),
		(else_try),
			(str_store_string, s11, "@{s11}^^You are currently not reading a book."),
		(try_end),
	(else_try),
		(eq, ":input", 2),																	# Force Size Report
		(call_script, "script_game_get_party_companion_limit"),
		(assign, ":party_size_limit", reg0),

		(store_skill_level, ":leadership", "skl_leadership", "trp_player"),
		(val_mul, ":leadership", 5),
		(store_attribute_level, ":charisma", "trp_player", ca_charisma),
			(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
		(val_div, ":renown", 25),
		(try_begin),
		  (gt, ":leadership", 0),
		  (str_store_string, s2, "@{!} +"),
		(else_try),
		  (str_store_string, s2, "str_space"),
		(try_end),
		(try_begin),
		  (gt, ":charisma", 0),
		  (str_store_string, s3, "@{!} +"),
		(else_try),
		  (str_store_string, s3, "str_space"),
		(try_end),
		(try_begin),
		  (gt, ":renown", 0),
		  (str_store_string, s4, "@{!} +"),
		(else_try),
		  (str_store_string, s4, "str_space"),
		(try_end),
		(assign, reg5, ":party_size_limit"),
		(assign, reg1, ":leadership"),
		(assign, reg2, ":charisma"),
		(assign, reg3, ":renown"),
		#Size Tweak Additions
		(try_begin),
		   (gt, reg9, 0), #Lord
		   (str_store_string, s5, "@{!} +{reg9}"),
		(else_try),
		  (str_store_string, s5, "str_space"),
		(try_end),
		(try_begin),
		   (gt, reg8, 0), #Castles
		   (str_store_string, s6, "@{!} +{reg8}"),
		(else_try),
		  (str_store_string, s6, "str_space"),
		(try_end),
		(try_begin),
		   (gt, reg7, 0), #Marshall
		   (str_store_string, s7, "@{!} +{reg7}"),
		(else_try),
		  (str_store_string, s7, "str_space"),
		(try_end),
		(try_begin),
		   (gt, reg6, 0), #King
		   (str_store_string, s8, "@{!} +{reg6}"),
		(else_try),
		  (str_store_string, s8, "str_space"),
		(try_end),

		(str_store_string, s11, "@Current party size limit is {reg5}.^Current party size modifiers are:^^Base size:  +30^Leadership: {s2}{reg1}^Charisma: {s3}{reg2}^Renown: {s4}{reg3}^^Lord: {s5}^Castles: {s6}^Marshall: {s7}^King: {s8}^TOTAL:  {reg5}"),
	(else_try),
		(eq, ":input", 3),																	# Morale Report
		(call_script, "script_get_player_party_morale_values"),
		 #(party_set_morale, "p_main_party", reg0),
		 (assign, ":ideal_morale", reg1), ## CC

		 (assign, ":target_morale", reg0),
		 (assign, reg1, "$g_player_party_morale_modifier_party_size"),
		 (try_begin),
		   (gt, reg1, 0),
		   (str_store_string, s2, "@{!} -"),
		 (else_try),
		   (str_store_string, s2, "str_space"),
		 (try_end),

		 (assign, reg2, "$g_player_party_morale_modifier_leadership"),
		 (try_begin),
		   (gt, reg2, 0),
		   (str_store_string, s3, "@{!} +"),
		 (else_try),
		   (str_store_string, s3, "str_space"),
		 (try_end),

		 (try_begin),
		   (gt, "$g_player_party_morale_modifier_no_food", 0),
		   (assign, reg7, "$g_player_party_morale_modifier_no_food"),
		   (str_store_string, s5, "@^No food:  -{reg7}"),
		 (else_try),
		   (str_store_string, s5, "str_space"),
		 (try_end),
		 (assign, reg3, "$g_player_party_morale_modifier_food"),
		 (try_begin),
		   (gt, reg3, 0),
		   (str_store_string, s4, "@{!} +"),
		 (else_try),
		   (str_store_string, s4, "str_space"),
		 (try_end),
		 
		 (try_begin),
		   (gt, "$g_player_party_morale_modifier_debt", 0),
		   (assign, reg6, "$g_player_party_morale_modifier_debt"),
		   (str_store_string, s6, "@^Wage debt:  -{reg6}"),
		 (else_try),
		   (str_store_string, s6, "str_space"),
		 (try_end),
	 
		 (party_get_morale, reg5, "p_main_party"),
		 (store_sub, reg4, reg5, ":target_morale"),
		 (try_begin),
		   (gt, reg4, 0),
		   (str_store_string, s7, "@{!} +"),
		 (else_try),
		   (str_store_string, s7, "str_space"),
		 (try_end),

		 ## CC
		(store_sub, ":dif", ":ideal_morale", reg5),
		# leadership modifier 
		(store_skill_level, ":skill", "skl_leadership", "trp_player"),
		(try_begin),
		  (gt, ":dif", 0),
		  (store_add, ":morale_change_factor", 20, ":skill"),
		(else_try),
		  (store_sub, ":morale_change_factor", 20, ":skill"),
		(try_end),
		(store_mul, ":dif_to_add", ":dif", ":morale_change_factor"),
		(val_div, ":dif_to_add", 100),
		(store_mul, ":dif_to_add_correction", ":dif_to_add", 100),
		(val_div, ":dif_to_add_correction", ":morale_change_factor"),
		# leadership modifier 
		(try_begin),#finding ceiling of the value
		  (neq, ":dif_to_add_correction", ":dif"),
		  (try_begin),
			(gt, ":dif", 0),
			(val_add, ":dif_to_add", 1),
		  (else_try),
			(val_sub, ":dif_to_add", 1),
		  (try_end),
		(try_end),
		(store_add, reg10, reg5, ":dif_to_add"),
		(val_clamp, reg10, 0, 100),
		(store_sub, reg8, reg10, reg5),
		(try_begin),
		  (gt, reg8, 0),
		  (str_store_string, s8, "@ +"),
		(else_try),
		  (str_store_string, s8, "@ "),
		(try_end),
		(str_store_string, s11, "@Current force morale is {reg5}.^Current force morale modifiers are:^^Base morale:  +50^Party size: {s2}{reg1}^Leadership: {s3}{reg2}^Food variety: {s4}{reg3}{s5}{s6}^Recent events: {s7}{reg4}^TOTAL:  {reg5}^^Morale value to change: {s8}{reg8}^Prospective party morale: {reg10}^^^"),
		## CC
			
		(try_for_range, ":kingdom_no", kingdoms_begin, kingdoms_end), #Player Faction
			(faction_get_slot, ":faction_morale", ":kingdom_no",  slot_faction_morale_of_player_troops),
			(val_div, ":faction_morale", 100),
			(neq, ":faction_morale", 0),
			(assign, reg6, ":faction_morale"),
			(str_store_faction_name, s9, ":kingdom_no"),
			(str_store_string, s11, "@{s11}Extra morale for {s9} troops : {reg6}^"), ## CC
		(try_end),
	(else_try),																			##	Companion Mission Report 
		(eq, ":input", 4),

		(str_clear, s11),
		(str_store_string, s12, "str_no_companions_in_service"),

		(try_begin),
			(troop_get_slot, ":spouse_or_betrothed", "trp_player", slot_troop_spouse),
			(try_begin),
				##diplomacy start+ Test gender with script
				(call_script, "script_cf_dplmc_troop_is_female", "trp_player"),
				##diplomacy end+
				(str_store_string, s8, "str_husband"),
			(else_try),
				(str_store_string, s8, "str_wife"),
			(try_end),
			
			(try_begin),
				(le, ":spouse_or_betrothed", 0),
				(troop_get_slot, ":spouse_or_betrothed", "trp_player", slot_troop_betrothed),
				(str_store_string, s8, "str_betrothed"),
			(try_end),	
			(gt, ":spouse_or_betrothed", 0),	
				
			(str_store_troop_name, s4, ":spouse_or_betrothed"),
			(troop_get_slot, ":cur_center", ":spouse_or_betrothed", slot_troop_cur_center),
			(try_begin),
				(is_between, ":cur_center", centers_begin, centers_end),
				(str_store_party_name, s5, ":cur_center"),
			(else_try),
				(troop_slot_eq, ":spouse_or_betrothed", slot_troop_occupation, slto_kingdom_hero),
				(str_store_string, s5, "str_leading_party"),
			(else_try),	
				(str_store_string, s5, "str_whereabouts_unknown"),
			(try_end),
			(str_store_string, s3, "str_s4_s8_s5"),
			(str_store_string, s2, s11),
			(str_store_string, s11, "str_s2_s3"),
			
		(try_end),
		   
		   
		(try_begin),
			(ge, "$cheat_mode", 1),
			(ge, "$npc_to_rejoin_party", 0),
			(str_store_troop_name, s5, "$npc_to_rejoin_party"),
			(str_store_string, s11, "@{!}DEBUG -- {s11}^NPC in rejoin queue: {s5}^"),
		(try_end),
   
   
		(try_for_range, ":companion", companions_begin, companions_end),
			(str_clear, s2),
			(str_clear, s3),

			(try_begin),
				(troop_get_slot, ":days_left", ":companion", slot_troop_days_on_mission),

				(troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),

				(str_store_troop_name, s4, ":companion"),

				(try_begin),
					(troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_kingsupport),
					(str_store_string, s8, "str_gathering_support"),
					(try_begin),
						(eq, ":days_left", 1),
						(str_store_string, s5, "str_expected_back_imminently"),
					(else_try),	
						(assign, reg3, ":days_left"),
						(str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
					(try_end),
				(else_try),
					(troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_gather_intel),
					(troop_get_slot, ":town_with_contacts", ":companion", slot_troop_town_with_contacts),
					(str_store_party_name, s11, ":town_with_contacts"),
					
					(str_store_string, s8, "str_gathering_intelligence"),
					(try_begin),
						(eq, ":days_left", 1),
						(str_store_string, s5, "str_expected_back_imminently"),
					(else_try),	
						(assign, reg3, ":days_left"),
						(str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
					(try_end),
				(else_try),	#This covers most diplomatic missions
					
					(troop_slot_ge, ":companion", slot_troop_current_mission, npc_mission_peace_request),
					##diplomacy begin
					(neg|troop_slot_eq, ":companion", slot_troop_current_mission, 8),
					##diplomacy end
					(troop_get_slot, ":faction", ":companion", slot_troop_mission_object),
					(str_store_faction_name, s9, ":faction"),
					(str_store_string, s8, "str_diplomatic_embassy_to_s9"),
					(try_begin),
						(eq, ":days_left", 1),
						(str_store_string, s5, "str_expected_back_imminently"),
					(else_try),	
						(assign, reg3, ":days_left"),
						(str_store_string, s5, "str_expected_back_in_approximately_reg3_days"),
					(try_end),
				(else_try),
					(eq, ":companion", "$g_player_minister"),
					(str_store_string, s8, "str_serving_as_minister"),
					(try_begin),
						(is_between, "$g_player_court", centers_begin, centers_end),
						(str_store_party_name, s9, "$g_player_court"),
						(str_store_string, s5, "str_in_your_court_at_s9"),
					(else_try),	
						(str_store_string, s5, "str_whereabouts_unknown"),
					(try_end),	
				(else_try),
					(main_party_has_troop, ":companion"),
					(str_store_string, s8, "str_under_arms"),
					(str_store_string, s5, "str_in_your_party"),
				(else_try),	
					(troop_slot_eq, ":companion", slot_troop_current_mission, npc_mission_rejoin_when_possible),
					(str_store_string, s8, "str_attempting_to_rejoin_party"),
					(str_store_string, s5, "str_whereabouts_unknown"),
				(else_try),	#Companions who are in a center
					(troop_slot_ge, ":companion", slot_troop_cur_center, 1),

					(str_store_string, s8, "str_separated_from_party"),
					(str_store_string, s5, "str_whereabouts_unknown"),
				(else_try), #Excludes companions who have occupation = retirement
					
					(troop_set_slot, ":companion", slot_troop_current_mission, npc_mission_rejoin_when_possible),
				
					(str_store_string, s8, "str_attempting_to_rejoin_party"),
					(str_store_string, s5, "str_whereabouts_unknown"),
					
					(try_begin),
						(ge, "$cheat_mode", 1),
						(troop_get_slot, reg2, ":companion", slot_troop_current_mission),
						(troop_get_slot, reg3, ":companion", slot_troop_days_on_mission),
						(troop_get_slot, reg4, ":companion", slot_troop_prisoner_of_party),
						(troop_get_slot, reg4, ":companion", slot_troop_playerparty_history),
							
						(display_message, "@{!}DEBUG: {s4} current mission: {reg2}, days on mission: {reg3}, prisoner: {reg4}, pphistory: {reg5}"),
					(try_end),
				(try_end),	
					
				(str_store_string, s3, "str_s4_s8_s5"),
					
				(str_store_string, s2, s11),
				(str_store_string, s11, "str_s2_s3"),

				(str_clear, s12), #"no companions in service"
			(else_try),
				(neg|troop_slot_eq, ":companion", slot_troop_occupation, slto_kingdom_hero),
				(troop_slot_ge, ":companion", slot_troop_prisoner_of_party, centers_begin),
				(str_store_troop_name, s4, ":companion"),
				(str_store_string, s8, "str_missing_after_battle"),
				(str_store_string, s5, "str_whereabouts_unknown"),
					
				(str_store_string, s3, "str_s4_s8_s5"),
				(str_store_string, s2, s11),
				(str_store_string, s11, "str_s2_s3"),			
				(str_clear, s12), #"no companions in service"
			(try_end),

		(try_end),
		(str_store_string, s11, "@{s11}{s12}"),
	(else_try),
		(eq, ":input", 5),																	#	Other Informtation
		(call_script, "script_get_number_of_hero_centers", "trp_player"),
		(assign, ":no_centers", reg0),
		(try_begin),
			(gt, ":no_centers", 0),
			(try_for_range, ":i_center", 0, ":no_centers"),
				(call_script, "script_troop_get_leaded_center_with_index", "trp_player", ":i_center"),
				(assign, ":cur_center", reg0),
				(try_begin),
					(eq, ":i_center", 0),
					(str_store_party_name, s8, ":cur_center"),
				(else_try),
					(eq, ":i_center", 1),
					(str_store_party_name, s7, ":cur_center"),
					(str_store_string, s8, "@{s7} and {s8}"),
				(else_try),
					(str_store_party_name, s7, ":cur_center"),
					(str_store_string, s8, "@{!}{s7}, {s8}"),
				(try_end),
			(try_end),
			(str_store_string, s11, "@Your estates are:^^{s8}."),
		(else_try),
			(str_store_string, s11, "@You dont own any estates."),
		(try_end),
	
		(try_begin),
			(this_or_next|gt, "$claim_arguments_made", 0),
			(this_or_next|gt, "$ruler_arguments_made", 0),
			(this_or_next|gt, "$victory_arguments_made", 0),
			(this_or_next|gt, "$lords_arguments_made", 0),
			(eq, 1, 0),
			
			(assign, reg3, "$claim_arguments_made"),
			(assign, reg4, "$ruler_arguments_made"),
			(assign, reg5, "$victory_arguments_made"),
			(assign, reg6, "$lords_arguments_made"),
			(assign, reg7, "$benefit_arguments_made"),
			
			(str_store_string, s12, "str_political_arguments_made_legality_reg3_rights_of_lords_reg4_unificationpeace_reg5_rights_of_commons_reg6_fief_pledges_reg7"),
			(str_store_string, s11, "@{s11}^^{s12}"),
		(try_end),
					
	(try_end),
	
	(start_presentation, "prsnt_reports"),	
	]),	
	#Reports over

## WINDYPLAINS+ ## - 2.54
# script_post_combat_relation_changes
# This script gets inserted in the add_log_event script to catch any allied heroes you fight alongside.
("post_combat_relation_changes",
	[
		(store_script_param_1, ":troop_no"),
		
		(store_faction_of_troop, ":faction_no", ":troop_no"),
		(call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop_no"),
		(assign, ":relation", reg0),
		
		(try_begin),
			# Capture non-party heroes.
			(neg|main_party_has_troop, ":troop_no"),
			(assign, ":relation_boost", 1),
			(try_begin),
				(faction_slot_eq, ":faction_no", slot_faction_leader, ":troop_no"), # Kings like you helping out.
				(val_add, ":relation_boost", 1),
			(else_try),
				(faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"), # Marshalls appreciate your support.
				(val_add, ":relation_boost", 1),
			(try_end),
			
			# If relation with player is poor then may not get any relation gain.
			(try_begin),
				(lt, ":relation", 0),
				(val_mul, ":relation", -3),
				(store_random_in_range, ":roll", 0, 100),
				(ge, ":roll", ":relation"),
				(val_sub, ":relation_boost", 1),
			(try_end),
			
			(store_add, ":cap", ":relation", ":relation_boost"),
			(lt, ":cap", 50),
			(call_script, "script_change_player_relation_with_troop", ":troop_no", ":relation_boost"),
		# (else_try),
			# # Party companions only gain relation if they were not wounded in the fight.
			# (neg|troop_is_wounded, ":troop_no"),
			# (store_add, ":cap", ":relation", ":relation_boost"),
			# (lt, ":cap", 50),
			# (set_show_messages, 0),
			# (call_script, "script_change_player_relation_with_troop", ":troop_no", 1),
			# (set_show_messages, 1),
		(try_end),
	]),  
## WINDYPLAINS- ##
 
  ("floris_set_default_prefs",
   [
    (store_script_param_1, ":skip_select_prefs"),
	
	(assign, "$drowning", 1),
	(assign, "$g_encumbrance_penalty", 1),
	(assign, "$g_dplmc_horse_speed", 0),
	(assign, "$cheat_mode", 0),
	(assign, "$disable_npc_complaints", 0),
	# (assign, "$g_player_carry_banner", 0),
	# (assign, "$g_others_carry_banner", 0),
	(assign, "$g_date", 0),
	(try_begin), #skip those set in the game-setup screens
		(eq, ":skip_select_prefs", 0),
		(assign, "$g_fog", 0),
		(call_script, "script_initialize_fog"),
	(try_end),
	(assign, "$g_wp_tpe_active", 1),
	
	(assign, "$g_disable_condescending_comments", 0),
	(assign, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
	(assign, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
	(assign, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_ENABLE),
	(assign, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
	
	(assign, "$g_hp_bar_dis_limit", 30),
    (assign, "$g_hp_bar_ally", 0),
    (assign, "$g_hp_bar_enemy", 0),
	  
	(assign, "$g_report_extra_xp_and_wpt", 0), ##CC 1.324
    (assign, "$g_report_shot_distance", 1), ##CC 1.324
    (assign, "$g_speed_ai_battles", 1),
    #(assign, "$g_game_difficulty", 1), ##CC 1.324
    (assign, "$g_rand_rain_limit", 30),      
    (assign, "$g_show_minimap", 0),
    (assign, "$g_minimap_ratio", 80),
	
	(call_script, "script_prebattle_set_default_prefs"),
	## WINDYPLAINS+ ## - 2.55 - Defaults for new mod options.
	(assign, "$enable_bandit_heroes", 1), # Enable Bandit Heroes
	(assign, "$bandit_hero_limiter", 8), # Set initial bandit hero limiter to 8.
	(assign, "$g_ft_force_pause", 2), # Set fast travel auto-pause to actual threats.
	## WINDYPLAINS- ##
   ]),   

  # script_cf_lieutenant_system_init_recruitment
  # Logic to calculate volunteers and determine if recruitment can proceed
  ("cf_lieutenant_system_init_recruitment", [
    (assign, ":total_volunteers", 0),
    (assign, ":total_eligible", 0),
    
    # Clear volunteer pool storage (trp_temp_array_c)
    # Slot 0 = unique type count
    # 1..50 = troop_ids
    # 51..100 = counts
    (troop_set_slot, "trp_temp_array_c", 0, 0),
    (try_for_range, ":i", 1, 101),
      (troop_set_slot, "trp_temp_array_c", ":i", 0),
    (try_end),

    # Count current lieutenants for penalty calculations
    (assign, ":lt_count", 0),
    (try_for_range, ":lt", lieutenants_begin, lieutenants_end),
      (main_party_has_troop, ":lt"),
      (val_add, ":lt_count", 1),
    (try_end),
    (store_mul, ":lt_penalty", ":lt_count", 8), # -8% chance per existing Lt

    (store_skill_level, ":persuasion", "skl_persuasion", "trp_player"),
    (store_skill_level, ":leadership", "skl_leadership", "trp_player"),
    
    (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
    (try_for_range, ":stack_no", 0, ":num_stacks"),
      (party_stack_get_troop_id, ":troop_id", "p_main_party", ":stack_no"),
      (neg|troop_is_hero, ":troop_id"),
      
      (store_character_level, ":level", ":troop_id"),
      (try_begin),
        (is_between, ":level", 14, 43), # Require level 14-42 (matching templates)
        
        (party_stack_get_size, ":stack_size", "p_main_party", ":stack_no"),
        (party_stack_get_num_wounded, ":num_wounded", "p_main_party", ":stack_no"),
        (store_sub, ":num_available", ":stack_size", ":num_wounded"),
        (try_begin),
          (gt, ":num_available", 0),
          (val_add, ":total_eligible", ":num_available"),
          
          # Chance calculation: troop level % + skill bonuses
          (assign, ":chance", ":level"),
          (store_mul, ":lead_bonus", ":leadership", 2), # +2% per leadership
          (val_add, ":chance", ":lead_bonus"),
          (val_add, ":chance", ":persuasion"), # +1% per persuasion
          (val_sub, ":chance", ":lt_penalty"), # increasingly difficult to get more Lts
          (val_clamp, ":chance", 0, 101), # Cap chance at 100% and min 0
          
          # Count volunteers in this stack
          (assign, ":volunteers_in_stack", 0),
          (try_for_range, ":unused", 0, ":num_available"),
            (store_random_in_range, ":random", 0, 100),
            (lt, ":random", ":chance"),
            (val_add, ":volunteers_in_stack", 1),
          (try_end),
          
          (try_begin),
            (gt, ":volunteers_in_stack", 0),
            (val_add, ":total_volunteers", ":volunteers_in_stack"),
            
            # Combine into unique types
            (troop_get_slot, ":num_unique", "trp_temp_array_c", 0),
            (assign, ":found", 0),
            (store_add, ":end_search", ":num_unique", 1),
            (try_for_range, ":i", 1, ":end_search"),
              (eq, ":found", 0),
              (troop_slot_eq, "trp_temp_array_c", ":i", ":troop_id"),
              (assign, ":found", 1),
              (store_add, ":count_slot", ":i", 50),
              (troop_get_slot, ":cur_count", "trp_temp_array_c", ":count_slot"),
              (val_add, ":cur_count", ":volunteers_in_stack"),
              (troop_set_slot, "trp_temp_array_c", ":count_slot", ":cur_count"),
            (try_end),
            (try_begin),
              (eq, ":found", 0),
              (lt, ":num_unique", 50), # Max 50 types
              (val_add, ":num_unique", 1),
              (troop_set_slot, "trp_temp_array_c", 0, ":num_unique"),
              (troop_set_slot, "trp_temp_array_c", ":num_unique", ":troop_id"),
              (store_add, ":count_slot", ":num_unique", 50),
              (troop_set_slot, "trp_temp_array_c", ":count_slot", ":volunteers_in_stack"),
            (try_end),
          (try_end),
        (try_end),
      (try_end),
    (try_end),

    (assign, "$g_lieutenant_total_volunteers", ":total_volunteers"),
    (gt, "$g_lieutenant_total_volunteers", 0),
  ]),

  # script_lieutenant_system_calculate_projected_stats
  # Replicates promotion logic to show "final" stats in menus without modifying troops
  ("lieutenant_system_calculate_projected_stats", [
    (store_script_param_1, ":source_troop"),

    # Determine template
    (store_character_level, ":source_level", ":source_troop"),
    (store_sub, ":slot_idx", ":source_level", 14),
    (val_clamp, ":slot_idx", 0, 29),
    (store_add, ":template", lieutenants_begin, ":slot_idx"),

    # 1. Virtual Attributes
    (store_attribute_level, ":v_str", ":template", 0),
    (store_attribute_level, ":v_agi", ":template", 1),
    (store_attribute_level, ":v_int", ":template", 2),
    (store_attribute_level, ":v_cha", ":template", 3),

    (store_add, ":target_attr_points", ":source_level", 32),
    (store_add, ":current_attr_total", ":v_str", ":v_agi"),
    (val_add, ":current_attr_total", ":v_int"),
    (val_add, ":current_attr_total", ":v_cha"),
    (store_sub, ":attr_points_to_add", ":target_attr_points", ":current_attr_total"),
    (try_for_range, ":unused", 0, ":attr_points_to_add"),
      (assign, ":best_attr", -1),
      (assign, ":max_diff", -100),
      (try_for_range, ":attr", 0, 4),
        (store_attribute_level, ":s_val", ":source_troop", ":attr"),
        (try_begin), (eq, ":attr", 0), (assign, ":l_val", ":v_str"),
        (else_try), (eq, ":attr", 1), (assign, ":l_val", ":v_agi"),
        (else_try), (eq, ":attr", 2), (assign, ":l_val", ":v_int"),
        (else_try), (assign, ":l_val", ":v_cha"), (try_end),
        (store_sub, ":diff", ":s_val", ":l_val"),
        (try_begin), (eq, ":attr", 3), (val_add, ":diff", 2), (try_end), # Favor CHA as per promote logic
        (gt, ":diff", ":max_diff"), (assign, ":max_diff", ":diff"), (assign, ":best_attr", ":attr"),
      (try_end),
      (try_begin),
        (eq, ":best_attr", 0), (val_add, ":v_str", 1),
        (else_try), (eq, ":best_attr", 1), (val_add, ":v_agi", 1),
        (else_try), (eq, ":best_attr", 2), (val_add, ":v_int", 1),
        (else_try), (val_add, ":v_cha", 1),
      (try_end),
    (try_end),

    # 2. Virtual Skills (using trp_temp_array_b for staging)
    (troop_set_slot, "trp_temp_array_b", 10, 0), (troop_set_slot, "trp_temp_array_b", 11, 1), (troop_set_slot, "trp_temp_array_b", 12, 2),
    (troop_set_slot, "trp_temp_array_b", 13, 7), (troop_set_slot, "trp_temp_array_b", 14, 8), (troop_set_slot, "trp_temp_array_b", 15, 9),
    (troop_set_slot, "trp_temp_array_b", 16, 10), (troop_set_slot, "trp_temp_array_b", 17, 11), (troop_set_slot, "trp_temp_array_b", 18, 12),
    (troop_set_slot, "trp_temp_array_b", 19, 13), (troop_set_slot, "trp_temp_array_b", 20, 14), (troop_set_slot, "trp_temp_array_b", 21, 15),
    (troop_set_slot, "trp_temp_array_b", 22, 16), (troop_set_slot, "trp_temp_array_b", 23, 17), (troop_set_slot, "trp_temp_array_b", 24, 21),
    (troop_set_slot, "trp_temp_array_b", 25, 22), (troop_set_slot, "trp_temp_array_b", 26, 23), (troop_set_slot, "trp_temp_array_b", 27, 24),
    (troop_set_slot, "trp_temp_array_b", 28, 25), (troop_set_slot, "trp_temp_array_b", 29, 26), (troop_set_slot, "trp_temp_array_b", 30, 27),
    (troop_set_slot, "trp_temp_array_b", 31, 33), (troop_set_slot, "trp_temp_array_b", 32, 34), (troop_set_slot, "trp_temp_array_b", 33, 35),
    (troop_set_slot, "trp_temp_array_b", 34, 36),

    (assign, ":current_skill_total", 0),
    (try_for_range, ":i", 10, 35),
      (troop_get_slot, ":skl", "trp_temp_array_b", ":i"),
      (store_skill_level, ":val", ":skl", ":template"),
      (store_add, ":val_slot", ":i", 30),
      (troop_set_slot, "trp_temp_array_b", ":val_slot", ":val"), # virtual levels in slots 40-64
      (val_add, ":current_skill_total", ":val"),
    (try_end),

    (store_add, ":target_skill_points", ":source_level", ":v_int"),
    (val_add, ":target_skill_points", 5),
    (store_sub, ":points_remaining", ":target_skill_points", ":current_skill_total"),
    
    (try_for_range, ":unused", 0, 100),
      (gt, ":points_remaining", 0),
      (assign, ":best_skill_idx", -1), (assign, ":max_pri", -100),
      (try_for_range, ":i", 10, 35),
        (troop_get_slot, ":skl", "trp_temp_array_b", ":i"),
        (store_add, ":val_slot", ":i", 30),
        (troop_get_slot, ":l_val", "trp_temp_array_b", ":val_slot"),
        (lt, ":l_val", 10),
        # Cap check using virtual attributes
        (assign, ":base_attr_val", -1),
        (try_begin), (this_or_next|eq, ":skl", 33), (this_or_next|eq, ":skl", 34), (this_or_next|eq, ":skl", 35), (eq, ":skl", 36), (assign, ":base_attr_val", ":v_str"),
        (else_try), (this_or_next|ge, ":skl", 21), (assign, ":base_attr_val", ":v_agi"),
        (else_try), (is_between, ":skl", 7, 18), (assign, ":base_attr_val", ":v_int"),
        (else_try), (assign, ":base_attr_val", ":v_cha"), (try_end),
        (store_div, ":cap", ":base_attr_val", 3),
        (lt, ":l_val", ":cap"),
        # Priority
        (store_skill_level, ":s_val", ":skl", ":source_troop"),
        (store_sub, ":priority", ":s_val", ":l_val"), (val_mul, ":priority", 2),
        (try_begin), (eq, ":skl", 1), (val_add, ":priority", 15), (else_try), (this_or_next|ge, ":skl", 33), (is_between, ":skl", 21, 28), (val_add, ":priority", 5), (try_end),
        (gt, ":priority", ":max_pri"), (assign, ":max_pri", ":priority"), (assign, ":best_skill_idx", ":i"),
      (try_end),
      (try_begin), (ge, ":best_skill_idx", 0),
        (store_add, ":val_slot", ":best_skill_idx", 30),
        (troop_get_slot, ":val", "trp_temp_array_b", ":val_slot"), 
        (val_add, ":val", 1), 
        (troop_set_slot, "trp_temp_array_b", ":val_slot", ":val"), 
        (val_sub, ":points_remaining", 1),
      (else_try), (assign, ":unused", 100), (try_end),
    (try_end),

    # Map to registers
    (assign, reg10, ":v_str"), (assign, reg11, ":v_agi"), (assign, reg12, ":v_int"), (assign, reg13, ":v_cha"),
    (try_for_range, ":i", 10, 35),
      (troop_get_slot, ":skl", "trp_temp_array_b", ":i"), 
      (store_add, ":val_slot", ":i", 30),
      (troop_get_slot, ":val", "trp_temp_array_b", ":val_slot"),
      (try_begin), (eq, ":skl", 36), (assign, reg14, ":val"), (else_try), (eq, ":skl", 35), (assign, reg15, ":val"), (else_try), (eq, ":skl", 34), (assign, reg16, ":val"), (else_try), (eq, ":skl", 33), (assign, reg17, ":val"), (else_try), (eq, ":skl", 27), (assign, reg18, ":val"), (else_try), (eq, ":skl", 26), (assign, reg19, ":val"), (else_try), (eq, ":skl", 25), (assign, reg20, ":val"), (else_try), (eq, ":skl", 24), (assign, reg21, ":val"), (else_try), (eq, ":skl", 16), (assign, reg22, ":val"), (else_try), (eq, ":skl", 15), (assign, reg23, ":val"), (else_try), (eq, ":skl", 14), (assign, reg24, ":val"), (else_try), (eq, ":skl", 13), (assign, reg25, ":val"), (else_try), (eq, ":skl", 1), (assign, reg26, ":val"), (try_end),
    (try_end),
  ]),

  # Helper for starting the mission safely using the camp scene
  ("lieutenant_system_start_sparring_mission", [
    (store_script_param, ":num_enemies", 1),
    
    (assign, "$g_lieutenant_sparring_mode", 1),
    (assign, "$g_training_ground_training_num_enemies", ":num_enemies"),
    (assign, "$g_training_ground_training_num_gourds_to_destroy", 0),
    (assign, "$g_mt_mode", ctm_melee),
    (try_begin),
      (le, "$g_training_ground_training_scene", 0),
      (assign, "$g_training_ground_training_scene", "scn_training_ground_ranged_melee_4"),
    (try_end),

    (modify_visitors_at_site, "$g_training_ground_training_scene"),
    (reset_visitors),
    (set_visitor, 0, "trp_player"),

    (try_for_range, ":i", 0, ":num_enemies"),
      (troop_get_slot, ":opponent_troop", "trp_temp_array_a", ":i"),
      (store_add, ":visitor_point", 1, ":i"),
      (set_visitor, ":visitor_point", ":opponent_troop"),
    (try_end),

    (set_jump_mission, "mt_lieutenant_sparring"),
    (set_jump_entry, 0),
    (jump_to_scene, "$g_training_ground_training_scene"),
    (change_screen_mission),
  ]),



  ("lieutenant_system_finish_promotion", [
    (store_script_param, ":source_troop", 1),
    (assign, ":lieutenant_troop", -1),

    # Count how many lieutenant slots are currently active (in party)
    (assign, ":active_count", 0),
    (try_for_range, ":lt", lieutenants_begin, lieutenants_end),
      (try_begin),
        (main_party_has_troop, ":lt"),
        (val_add, ":active_count", 1),
      (try_end),
    (try_end),

    (try_begin),
      (ge, ":active_count", 10),
      (display_message, "@You already have the maximum number of Lieutenants (10)!"),
    (else_try),
      # Determine which level slot to pick (levels 14-42 = indices 0-20)
      (store_character_level, ":source_level", ":source_troop"),
      (val_clamp, ":source_level", 14, 42),
      (store_sub, ":slot_idx", ":source_level", 14), # 0-28
      (store_add, ":lieutenant_troop", lieutenants_begin, ":slot_idx"),

      # If that slot is already in use, scan from the same index upward then wrap around
      (try_begin),
        (main_party_has_troop, ":lieutenant_troop"),
        # Search upward first (higher levels free)
        (assign, ":found", 0),
        (try_for_range, ":offset", 1, 29),
          (eq, ":found", 0),
          (store_add, ":candidate", ":slot_idx", ":offset"),
          (val_mod, ":candidate", 29), # wrap around 0-28
          (store_add, ":lt", lieutenants_begin, ":candidate"),
          (neg|main_party_has_troop, ":lt"),
          (assign, ":lieutenant_troop", ":lt"),
          (assign, ":found", 1),
          (assign, ":offset", 29), # break
        (try_end),
      (try_end),

      (call_script, "script_lieutenant_system_promote", ":lieutenant_troop", ":source_troop"),
    (try_end),
  ]),



  ("lieutenant_system_promote", [
    (store_script_param, ":lieutenant_troop", 1),
    (store_script_param, ":source_troop", 2),

    # VERSION 9: DUMMY NPC - No XP injection needed; level is baked into the template.
    (party_remove_members, "p_main_party", ":lieutenant_troop", 1),

    # Phase 0: Reset Identity & Type
    (troop_get_type, ":type", ":source_troop"),
    (troop_set_type, ":lieutenant_troop", ":type"),

    # Phase 1: Distribute Attributes (Target: Level + 32)
    (store_character_level, ":source_level", ":source_troop"),
    (store_add, ":target_attr_points", ":source_level", 32),
    
    # Calculate current attribute total (base engine stats for hero level)
    (assign, ":current_attr_total", 0),
    (try_for_range, ":attr", 0, 4),
      (store_attribute_level, ":val", ":lieutenant_troop", ":attr"),
      (val_add, ":current_attr_total", ":val"),
    (try_end),

    (store_sub, ":attr_points_to_add", ":target_attr_points", ":current_attr_total"),
    (try_for_range, ":unused", 0, ":attr_points_to_add"),
      (assign, ":best_attr", -1),
      (assign, ":max_diff", -100),
      (try_for_range, ":attr", 0, 4),
        (store_attribute_level, ":s_val", ":source_troop", ":attr"),
        (store_attribute_level, ":l_val", ":lieutenant_troop", ":attr"),
        (store_sub, ":diff", ":s_val", ":l_val"),
        (try_begin),
          (eq, ":attr", 3), # Favor Charisma (attribute index 3)
          (val_add, ":diff", 2), # Slightly favoring as requested
        (try_end),
        (gt, ":diff", ":max_diff"),
        (assign, ":max_diff", ":diff"),
        (assign, ":best_attr", ":attr"),
      (try_end),
      (try_begin),
        (ge, ":best_attr", 0),
        (troop_raise_attribute, ":lieutenant_troop", ":best_attr", 1),
      (try_end),
    (try_end),

    # Phase 2: Distribute Skills (Target: Level + Current_INT + 5)
    (store_attribute_level, ":l_int", ":lieutenant_troop", 2),
    (assign, ":target_skill_points", ":source_level"),
    (val_add, ":target_skill_points", ":l_int"),
    (val_add, ":target_skill_points", 5),
    (assign, reg2, ":target_skill_points"),
    
    # Native Skill mapping (25 real skills)
    (troop_set_slot, "trp_temp_array_a", 0, 0),        # Trade (CHA)
    (troop_set_slot, "trp_temp_array_a", 1, 1),        # Leadership (CHA)
    (troop_set_slot, "trp_temp_array_a", 2, 2),        # Prisoner Man. (CHA)
    (troop_set_slot, "trp_temp_array_a", 3, 7),        # Persuasion (INT)
    (troop_set_slot, "trp_temp_array_a", 4, 8),        # Engineer (INT)
    (troop_set_slot, "trp_temp_array_a", 5, 9),        # First Aid (INT)
    (troop_set_slot, "trp_temp_array_a", 6, 10),       # Surgery (INT)
    (troop_set_slot, "trp_temp_array_a", 7, 11),       # Wound Treatment (INT)
    (troop_set_slot, "trp_temp_array_a", 8, 12),       # Inventory Man. (INT)
    (troop_set_slot, "trp_temp_array_a", 9, 13),       # Spotting (INT)
    (troop_set_slot, "trp_temp_array_a", 10, 14),      # Pathfinding (INT)
    (troop_set_slot, "trp_temp_array_a", 11, 15),      # Tactics (INT)
    (troop_set_slot, "trp_temp_array_a", 12, 16),      # Tracking (INT)
    (troop_set_slot, "trp_temp_array_a", 13, 17),      # Trainer (INT)
    (troop_set_slot, "trp_temp_array_a", 14, 21),      # Foraging (AGI)
    (troop_set_slot, "trp_temp_array_a", 15, 22),      # Looting (AGI)
    (troop_set_slot, "trp_temp_array_a", 16, 23),      # Horse Archery (AGI)
    (troop_set_slot, "trp_temp_array_a", 17, 24),      # Riding (AGI)
    (troop_set_slot, "trp_temp_array_a", 18, 25),      # Athletics (AGI)
    (troop_set_slot, "trp_temp_array_a", 19, 26),      # Shield (AGI)
    (troop_set_slot, "trp_temp_array_a", 20, 27),      # Weapon Master (AGI)
    (troop_set_slot, "trp_temp_array_a", 21, 33),      # Power Draw (STR)
    (troop_set_slot, "trp_temp_array_a", 22, 34),      # Power Throw (STR)
    (troop_set_slot, "trp_temp_array_a", 23, 35),      # Power Strike (STR)
    (troop_set_slot, "trp_temp_array_a", 24, 36),      # Ironflesh (STR)

    # Calculate current skill total
    (assign, ":current_skill_total", 0),
    (try_for_range, ":i_map", 0, 25),
      (troop_get_slot, ":skl", "trp_temp_array_a", ":i_map"),
      (store_skill_level, ":val", ":skl", ":lieutenant_troop"),
      (val_add, ":current_skill_total", ":val"),
    (try_end),

    (store_sub, ":points_remaining", ":target_skill_points", ":current_skill_total"),
    
    # Allocation loop
    (try_for_range, ":unused", 0, 100),
      (gt, ":points_remaining", 0),
      
      (assign, ":best_skill", -1),
      (assign, ":max_pri", -100),
      
      (try_for_range, ":i_map", 0, 25),
        (troop_get_slot, ":skl", "trp_temp_array_a", ":i_map"),
        (store_skill_level, ":l_val", ":skl", ":lieutenant_troop"),
        (lt, ":l_val", 10), # Soft cap 10
        
        # Determine attribute cap
        (assign, ":base_attr_idx", -1),
        (try_begin),
          (this_or_next|eq, ":skl", 33), # STR skills
          (this_or_next|eq, ":skl", 34),
          (this_or_next|eq, ":skl", 35),
          (eq, ":skl", 36),
          (assign, ":base_attr_idx", 0),
        (else_try),
          (is_between, ":skl", 21, 28), # AGI skills
          (assign, ":base_attr_idx", 1),
        (else_try),
          (is_between, ":skl", 7, 18),  # INT skills
          (assign, ":base_attr_idx", 2),
        (else_try),
          (assign, ":base_attr_idx", 3), # CHA skills
        (try_end),
        
        (store_attribute_level, ":attr_val", ":lieutenant_troop", ":base_attr_idx"),
        (store_div, ":cap", ":attr_val", 3),
        (lt, ":l_val", ":cap"),
        
        # Calculate Priority
        (store_skill_level, ":s_val", ":skl", ":source_troop"),
        (store_sub, ":priority", ":s_val", ":l_val"),
        (val_mul, ":priority", 2),
        
        # Priority weights: Focus on Leadership
        (try_begin),
          (eq, ":skl", 1), # Leadership
          (val_add, ":priority", 15),
        (else_try),
          (this_or_next|ge, ":skl", 33), # Combat
          (is_between, ":skl", 21, 28), # Athletic/Horse
          (val_add, ":priority", 5),
        (try_end),
        
        (gt, ":priority", ":max_pri"),
        (assign, ":max_pri", ":priority"),
        (assign, ":best_skill", ":skl"),
      (try_end),
      
      (try_begin),
        (ge, ":best_skill", 0),
        (troop_raise_skill, ":lieutenant_troop", ":best_skill", 1),
        (val_sub, ":points_remaining", 1),
      (else_try),
        (assign, ":unused", 100), # Break if no skill can be raised
      (try_end),
    (try_end),

    # Phase 3: Mirror Proficiencies
    (try_for_range, ":prof", 0, 7),
      (store_proficiency_level, ":val", ":source_troop", ":prof"),
      (store_proficiency_level, ":cur_val", ":lieutenant_troop", ":prof"),
      (store_sub, ":diff", ":val", ":cur_val"),
      (try_begin),
        (gt, ":diff", 0),
        (troop_raise_proficiency_linear, ":lieutenant_troop", ":prof", ":diff"),
      (try_end),
    (try_end),

    # Phase 4: Mirror Equipment
    (troop_clear_inventory, ":lieutenant_troop"),
    (try_for_range, ":slot", 0, 96),
      (troop_get_inventory_slot, ":item", ":source_troop", ":slot"),
      (try_begin),
        (ge, ":item", 0),
        (troop_get_inventory_slot_modifier, ":imod", ":source_troop", ":slot"),
        (troop_add_item, ":lieutenant_troop", ":item", ":imod"),
      (try_end),
    (try_end),
    (troop_equip_items, ":lieutenant_troop"),

    # Clear excess items left in the inventory/backpack (slots 10-95)
    # Warband equipment slots are 0-9.
    (try_for_range, ":slot", 10, 96),
      (troop_set_inventory_slot, ":lieutenant_troop", ":slot", -1),
    (try_end),

    # Phase 5: Identity Naming (Ordinal based on active lieutenants count)
    (assign, ":active_count", 0),
    (try_for_range, ":lt", lieutenants_begin, lieutenants_end),
      (try_begin),
        (main_party_has_troop, ":lt"),
        (val_add, ":active_count", 1),
      (try_end),
    (try_end),
    (val_add, ":active_count", 1), # This is the Nth lieutenant

    (try_begin),
      (eq, ":active_count", 1), (str_store_string, s5, "@Lt. I"),
    (else_try),
      (eq, ":active_count", 2), (str_store_string, s5, "@Lt. II"),
    (else_try),
      (eq, ":active_count", 3), (str_store_string, s5, "@Lt. III"),
    (else_try),
      (eq, ":active_count", 4), (str_store_string, s5, "@Lt. IV"),
    (else_try),
      (eq, ":active_count", 5), (str_store_string, s5, "@Lt. V"),
    (else_try),
      (eq, ":active_count", 6), (str_store_string, s5, "@Lt. VI"),
    (else_try),
      (eq, ":active_count", 7), (str_store_string, s5, "@Lt. VII"),
    (else_try),
      (eq, ":active_count", 8), (str_store_string, s5, "@Lt. VIII"),
    (else_try),
      (eq, ":active_count", 9), (str_store_string, s5, "@Lt. IX"),
    (else_try),
      (eq, ":active_count", 10), (str_store_string, s5, "@Lt. X"),
    (else_try),
      (str_store_string, s5, "@Lt. X+"), # Fallback so string isn't empty buffer
    (try_end),

    (try_begin),
      (eq, ":type", 1), # female
      (store_random_in_range, ":name_no", female_names_begin, female_names_end),
    (else_try),
      (store_random_in_range, ":name_no", names_begin, names_end),
    (try_end),
    (str_store_string, s1, ":name_no"),
    (str_store_string, s1, "@{s5} {s1}"),
    (troop_set_name, ":lieutenant_troop", s1),

    # Phase 6: Finalize Recruitment
    (party_remove_members, "p_main_party", ":source_troop", 1),
    (troop_set_slot, ":lieutenant_troop", slot_troop_occupation, slto_lieutenant),
    (party_add_members, "p_main_party", ":lieutenant_troop", 1),

    (str_store_troop_name, s1, ":lieutenant_troop"),
    (display_message, "@{s1} has been promoted and joined your ranks!"),
  ]),

  
]
