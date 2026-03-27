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



simple_triggers_part1 = [

# This trigger is deprecated. Use "script_game_event_party_encounter" in module_scripts.py instead
  (ti_on_party_encounter,
   [
    ]),


# This trigger is deprecated. Use "script_game_event_simulate_battle" in module_scripts.py instead
  (ti_simulate_battle,
   [
    ]),


  (1,
   [
      (try_begin),
        (eq, "$training_ground_position_changed", 0),
        (assign, "$training_ground_position_changed", 1),
		(set_fixed_point_multiplier, 100),
        (position_set_x, pos0, 7050),
        (position_set_y, pos0, 7200),
        (party_set_position, "p_training_ground_3", pos0),
      (try_end),

      (gt,"$auto_besiege_town",0),
      (gt,"$g_player_besiege_town", 0),
      (ge, "$g_siege_method", 1),
      (store_current_hours, ":cur_hours"),
      (eq, "$g_siege_force_wait", 0),
      (ge, ":cur_hours", "$g_siege_method_finish_hours"),
      (neg|is_currently_night),
      (rest_for_hours, 0, 0, 0), #stop resting
    ]),
####CromCrom Rigale Explore

		#####Reworked
      (24 ,
   [

		# (map_free),	#rigale exploration script code base
          # (assign, ":min_distance_1", 100000),
          # (assign, ":min_distance_2", 100000),
          # (assign, ":min_distance_3", 100000),
          # (assign, ":walled_center_1", -1),
          # (assign, ":walled_center_2", -1),
          # (assign, ":walled_center_3", -1),
          # (try_for_parties, ":party_no"),
            # (party_is_active, ":party_no"),
            # (party_get_slot, ":cur_party_type", ":party_no", slot_party_type),
            # (this_or_next|eq, ":cur_party_type", spt_town),
            # (eq, ":cur_party_type", spt_castle),
            # (party_get_position, pos1, ":party_no"),
            # (store_distance_to_party_from_party, ":cur_dist", ":party_no", "p_main_party"),
            # (try_begin),
              # (lt, ":cur_dist", ":min_distance_1"),
              # (assign, ":min_distance_3", ":min_distance_2"),
              # (assign, ":walled_center_3", ":walled_center_2"),
              # (assign, ":min_distance_2", ":min_distance_1"),
              # (assign, ":walled_center_2", ":walled_center_1"),
              # (assign, ":min_distance_1", ":cur_dist"),
              # (assign, ":walled_center_1", ":party_no"),
            # (else_try),
              # (lt, ":cur_dist", ":min_distance_2"),
              # (assign, ":min_distance_3", ":min_distance_2"),
              # (assign, ":walled_center_3", ":walled_center_2"),
              # (assign, ":min_distance_2", ":cur_dist"),
              # (assign, ":walled_center_2", ":party_no"),
            # (else_try),
              # (lt, ":cur_dist", ":min_distance_3"),
              # (assign, ":min_distance_3", ":cur_dist"),
              # (assign, ":walled_center_3", ":party_no"),
            # (try_end),
          # (try_end),
          # (try_begin),
            # (neq, ":walled_center_1", -1),
            # (str_store_party_name, s63, ":walled_center_1"),
          # (try_end),    
          # (try_begin),
            # (neq, ":walled_center_2", -1),
            # (str_store_party_name, s62, ":walled_center_2"),
          # (try_end),    
          # (try_begin),
            # (neq, ":walled_center_3", -1),
            # (str_store_party_name, s61, ":walled_center_3"),
          # (try_end),              
          # #(display_message,"@You are now in the area of {s63}, {s62}, {s61}"),   
	]),
		
	(24, 																				#Floris Seafaring Wilderness Check
	[
		(try_for_parties, ":party_no"),													
		    (party_slot_eq, ":party_no", slot_party_type, spt_ship),
			(party_slot_eq, ":party_no", slot_ship_center, ship_wild_no_guard),
			(party_get_slot, ":timer", ":party_no", slot_ship_time),
			(store_current_hours, ":cur_time"),
			(ge, ":cur_time", ":timer"),
			(store_random_in_range, ":luck", 0, 10),
			(ge, ":luck", 5),
			(str_store_party_name, s1, ":party_no"),
			(display_message, "@You have a bad feeling about your ship {s1}."),
			(remove_party, ":party_no"),			
		(try_end),
		
		(try_for_parties, ":center_no"),												#Floris Population Resetting // Forced Recruiting
			(this_or_next|party_slot_eq, ":center_no", slot_center_recruits, 1),
			(party_slot_eq, ":center_no", slot_center_recruits, 2),
			(party_set_slot, ":center_no", slot_center_recruits, 0),
		(try_end),
		
		]),
		
	(1, 																				#Floris fishing
	[	
		(try_begin),
			(party_get_current_terrain, ":terrain", "p_main_party"),
			(eq, ":terrain", 0),
			(neq, "$g_player_icon_state", pis_ship),
			(assign, "$g_player_icon_state", pis_ship),
		(try_end),
		
		(try_begin),
			(party_get_slot, ":timer", "p_main_party", slot_ship_time),
			(gt, ":timer", 0),
			(store_current_hours, ":cur_time"),			
			(ge, ":cur_time", ":timer"),
			(try_begin),
				(party_get_current_terrain, ":terrain", "p_main_party"),
				(eq, ":terrain", 0),
				(store_skill_level, ":skill", skl_foraging,"trp_player"),
				(val_mul, ":skill", 10),
				(store_random_in_range, ":luck", 0, 100),
				(ge, ":skill", ":luck"),
				(store_free_inventory_capacity, ":i_space", "trp_player"),
				(try_begin),
					(ge, ":i_space", 1),
					(display_message, "@You caught some fish."),
					(troop_add_item, "trp_player", "itm_trade_smoked_fish"),
					#(troop_add_merchandise, "trp_player", "itm_trade_smoked_fish", 1),
				(else_try),
					(display_message, "@Due to insufficient space, you had to throw the fish back into the ocean"),
				(try_end),				
				(assign,"$g_camp_mode", 0),
				(rest_for_hours_interactive, 0, 5, 1),
				(party_set_slot, "p_main_party", slot_ship_time, 0),
			(else_try),
				(display_message, "@All you caught were some seaweeds."),
				(assign,"$g_camp_mode", 0),
				(rest_for_hours_interactive, 0, 5, 1),
				(party_set_slot, "p_main_party", slot_ship_time, -1),
			(try_end),
		(try_end),
		
		(set_fixed_point_multiplier, 10),
		(try_for_parties, ":party_no"),													#Floris Get Back to Shore Check
			(party_get_template_id,":template",":party_no"),
			(this_or_next|eq, ":template", "pt_sea_raiders_ships"),
			(this_or_next|eq, ":template", "pt_sea_raiders_ships_r"),
			(eq, ":template", "pt_sea_raiders_ships_e"),
			(try_begin),
				(party_get_position, pos1, ":party_no"),
				(position_get_y, ":value_y", pos1),
				(position_get_x, ":value_x", pos1),
				(val_div, ":value_y", 10),
				(val_div, ":value_x", 10),
				(this_or_next|gt, ":value_y", 155),
				(lt, ":value_x", -180),
				(assign, reg1, ":value_y"),
				(assign, reg2, ":value_x"),
				(get_party_ai_current_behavior, ":behavior", ":party_no"),
				(assign, reg3, ":behavior"),
				#(display_message, "@Behavior was {reg3}, X is {reg2} and Y is {reg1}"), 
				#(party_set_flags, ":party_no", pf_default_behavior, 0),
				(party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),      ###test if   ai_bhvr_travel_to_point (with the point being the spawn_point location, or a randomized point around it)
				(party_set_ai_object, ":party_no", "p_ship_raider_spawn_point_1"),   ##### prevents the ships from going invisible/inactive when they return to the spawn point
				#(display_message, "@Get Back to Shore TEST"),
			(else_try),
				(store_distance_to_party_from_party, ":distance", ":party_no", "p_ship_raider_spawn_point_1"),
				(lt, ":distance", 4),
				#(party_set_flags, ":party_no", pf_default_behavior, 1),
				(party_get_position, pos2, "p_ship_raider_spawn_point_1"),
				(party_set_ai_behavior, ":party_no", ai_bhvr_patrol_location),
				(party_set_ai_patrol_radius, ":party_no", 10),
				(party_set_ai_target_position, ":party_no", pos2),  
				#(party_set_ai_behavior, ":party_no", ai_bhvr_patrol_party),
				#(party_set_ai_patrol_radius, ":party_no", 10),
				#(party_set_ai_object, ":party_no", "p_ship_raider_spawn_point_1"),
				#(party_set_aggressiveness, ":party_no" , 15),
				#(display_message, "@Now get back to sea TEST"),
			(try_end),
		(try_end),
		
				
		(try_for_range, ":town_no", towns_begin, towns_end),							#	Floris Moneylenders // Not paying debts has consequences
			(party_get_slot, ":debt", ":town_no", slot_town_bank_debt),
			(gt, ":debt", 0),															#	If a debt exists, a deadline exists
			(party_get_slot, ":deadline", ":town_no", slot_town_bank_deadline),
			(store_current_hours, ":date"),
			(ge, ":date", ":deadline"),
			(call_script, "script_change_player_relation_with_center", ":town_no", -5, 0xff3333),
			(try_begin),
				(lt, ":debt", 100000),
				(val_mul, ":debt", 14),
				(val_div, ":debt", 10),
				(try_begin),
					(gt, ":debt", 100000),												#Debt doesnt get higher than 100000 denars
					(assign, ":debt", 100000),
				(try_end),
				(val_add, ":deadline", 24*14),
				(party_set_slot, ":town_no", slot_town_bank_debt, ":debt"),
				(party_set_slot, ":town_no", slot_town_bank_deadline, ":deadline"),
				(str_store_party_name, s1, ":town_no"),
				(display_message, "@You missed the deadline to pay back your debts in {s1}. They now grow at an interest of 50%."),
			(else_try),
				(assign, ":debt", 100000),												#If debt = 100000 denars, then additionally to -5 relation with town, you get -1 relation with Faction.
				(val_add, ":deadline", 24*14),
				(party_set_slot, ":town_no", slot_town_bank_debt, ":debt"),
				(party_set_slot, ":town_no", slot_town_bank_deadline, ":deadline"),
				(store_faction_of_party, ":faction_no", ":town_no"),
				(call_script, "script_change_player_relation_with_faction_ex", ":faction_no", -1),
				(str_store_party_name, s1, ":town_no"),
				(display_message, "@Your debt in {s1} is now so high that the King himself has taken notice. He has frozen your debt, but is displeased with the situation.", 0xff3333),
			(try_end),
		(try_end),			
		
		
																						#	Floris Simple Fog of War // Parties in reach are set to become visible
		(try_for_range, ":center_no", centers_begin, spawn_points_begin),		
			(party_slot_eq, ":center_no", slot_center_explored, 0),
			(store_distance_to_party_from_party,":distance", ":center_no", "p_main_party"),
			(le, ":distance", 20),
			(party_set_slot, ":center_no", slot_center_explored, 1),
			(eq, "$g_fog", 1),
			(party_set_flags, ":center_no", pf_always_visible, 1),
		(try_end),
		
		
	]),
	
	(24*14,
	[
		(try_for_range, ":town_no", towns_begin, towns_end),							#	Floris	//	Adjust Population Depending on Prosperity
			(party_get_slot, ":prosperity", ":town_no", slot_town_prosperity),
			(party_get_slot, ":population", ":town_no", slot_center_population),
			(assign,":change",0),
			(try_begin),
				(ge, ":prosperity", 60),
				(store_sub, ":change", ":prosperity",60),
				(val_div, ":change", 5),
				(val_add, ":change", 3),
			(else_try),
				(le, ":prosperity", 40),
				(store_sub, ":change", ":prosperity", 40),                              # Fixed typo
				(val_div, ":change", 5),
				(val_sub, ":change", 3),
			(try_end),
			(store_div,":base",":population",100),										#	Base population change is 1% of pop
			(val_mul,":change",":base"),				
			(val_add,":population", ":change"),			
			(try_begin),
				(gt, ":population", 30000),
				(assign, ":population", 30000),
				(party_set_slot, ":town_no", slot_center_population, ":population"),
			(else_try),
				(lt, ":population", 5000),
				(assign, ":population", 5000),
				(party_set_slot, ":town_no", slot_center_population, ":population"),
			(else_try),
				(party_set_slot, ":town_no", slot_center_population, ":population"),
			(try_end),
		(try_end),	
	
		(try_for_range, ":town_no", towns_begin, towns_end),							#	Floris	//	Calculating Land Demand and Consequences for supply, pricing and renting
			(party_get_slot, ":population", ":town_no", slot_center_population),
			(party_get_slot, ":land_town", ":town_no", slot_town_acres),
			(party_get_slot, ":land_player", ":town_no", slot_town_player_acres),
			(party_get_slot, ":prosperity", ":town_no", slot_town_prosperity),
			(store_sub, ":revenue", ":prosperity", 50),
			(val_add, ":revenue", 100),
			(try_begin),
				(store_div, ":acres_needed", ":population", 200),						#	200 People warrant 1 acre of cultivated land
				(store_add, ":total_land", ":land_town", ":land_player"),
				(store_sub, ":surplus", ":total_land", ":acres_needed"),
				
				(try_begin),															#	AI Consequences
					(lt, ":total_land", ":acres_needed"),
					(store_sub, ":new_acres", ":acres_needed", ":total_land"),
					(val_add, ":land_town", ":new_acres"),
					(party_set_slot, ":town_no", slot_town_acres, ":land_town"),
				(else_try),
					(ge, ":surplus", 20),
					(ge, ":land_town", 10),
					(val_sub, ":land_town", 10),										#	Changed from 2 / Faster rebalancing in case of player screw up
					(party_set_slot, ":town_no", slot_town_acres, ":land_town"),
				(try_end),
				
				(try_begin),
					(gt, ":land_player", 0),												# 	New Fix / Before it was possible for the towns land to cause the player a deficit
					(try_begin),															#	Player Consequences
						(le, ":total_land", ":acres_needed"),
						(val_mul, ":land_player", ":revenue"),										
						(party_set_slot, ":town_no", slot_town_bank_rent, ":land_player"),
					(else_try),
						(store_mul, ":penalty", ":surplus", -1),
						(val_add, ":penalty", ":revenue"),
						(try_begin),
							(ge, ":penalty", 85),
							(val_mul, ":land_player", ":penalty"),
							(party_set_slot, ":town_no", slot_town_bank_rent, ":land_player"),
						(else_try),
							(store_sub, ":non_rented", ":surplus", 15),
							(val_sub, ":land_player", ":non_rented"),
							(try_begin),													#	Safety check // No penalty on rent should turn rent negative.
								(lt, ":penalty", 0),
								(assign, ":penalty", 0),
							(try_end),
							(val_mul, ":land_player", ":penalty"),
							(party_set_slot, ":town_no", slot_town_bank_rent, ":land_player"),
							(val_mul, ":non_rented", -50),
							(party_set_slot, ":town_no", slot_town_bank_upkeep, ":non_rented"),
						(try_end),
					(try_end),
					(party_get_slot, ":assets", ":town_no", slot_town_bank_assets),						#	Adding/Subtracting profits/losses
					(party_get_slot, ":rent", ":town_no", slot_town_bank_rent),
					(party_get_slot, ":upkeep", ":town_no", slot_town_bank_upkeep),
					(val_add, ":assets", ":rent"),
					(val_add, ":assets", ":upkeep"),
					(party_set_slot, ":town_no", slot_town_bank_assets, ":assets"),	
				(try_end),
				
			(try_end),
		
		(try_end),
	
	]),	
		
  (0,
   [
      (try_begin),
        (eq, "$bug_fix_version", 0),

        #fix for hiding test_scene in older savegames
        (disable_party, "p_test_scene"),
        #fix for correcting town_1 siege type
        (party_set_slot, "p_town_1", slot_center_siege_with_belfry, 0),
        #fix for hiding player_faction notes
        (faction_set_note_available, "fac_player_faction", 0),
        #fix for hiding faction 0 notes
        (faction_set_note_available, "fac_no_faction", 0),
        #fix for removing kidnapped girl from party
        (try_begin),
          (neg|check_quest_active, "qst_kidnapped_girl"),
          (party_remove_members, "p_main_party", "trp_kidnapped_girl", 1),
        (try_end),
        #fix for not occupied but belong to a faction lords
        (try_for_range, ":cur_troop", lords_begin, lords_end),
          (try_begin),
            (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_inactive),
            (store_troop_faction, ":cur_troop_faction", ":cur_troop"),
            (is_between, ":cur_troop_faction", "fac_kingdom_1", kingdoms_end),
            (troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
          (try_end),
        (try_end),
        #fix for an error in 1.105, also fills new slot values
        (call_script, "script_initialize_item_info"),

        (assign, "$bug_fix_version", 1),
      (try_end),

      (eq,"$g_player_is_captive",1),
      (gt, "$capturer_party", 0),
      (party_is_active, "$capturer_party"),
      (party_relocate_near_party, "p_main_party", "$capturer_party", 0),
    ]),


#Auto-menu
  (0,
   [
     (try_begin),
       (gt, "$g_last_rest_center", 0),
       (party_get_battle_opponent, ":besieger_party", "$g_last_rest_center"),
       (gt, ":besieger_party", 0),
       (store_faction_of_party, ":encountered_faction", "$g_last_rest_center"),
       (store_relation, ":faction_relation", ":encountered_faction", "fac_player_supporters_faction"),
       (store_faction_of_party, ":besieger_party_faction", ":besieger_party"),
       (store_relation, ":besieger_party_relation", ":besieger_party_faction", "fac_player_supporters_faction"),
       (ge, ":faction_relation", 0),
       (lt, ":besieger_party_relation", 0),
       (start_encounter, "$g_last_rest_center"),
       (rest_for_hours, 0, 0, 0), #stop resting
     (else_try),
       (store_current_hours, ":cur_hours"),
       (assign, ":check", 0),
       (try_begin),
         (neq, "$g_check_autos_at_hour", 0),
         (ge, ":cur_hours", "$g_check_autos_at_hour"),
         (assign, ":check", 1),
         (assign, "$g_check_autos_at_hour", 0),
       (try_end),
       (this_or_next|eq, ":check", 1),
       (map_free),
       (try_begin),
         (ge,"$auto_menu",1),
         (jump_to_menu,"$auto_menu"),
         (assign,"$auto_menu",-1),
       (else_try),
         (ge,"$auto_enter_town",1),
         (start_encounter, "$auto_enter_town"),
       ##Floris - to allow player to access inventory during siege, or to entrench during siege ; other part of code in Floris version trigger    
	  # (else_try),
         # (ge,"$auto_besiege_town",1),
         # (start_encounter, "$auto_besiege_town"),
	  ##Floris - end
       (else_try),
         (ge,"$g_camp_mode", 1),
         (assign, "$g_camp_mode", 0),
         (assign, "$g_infinite_camping", 0),
		 (try_begin),						#Floris Seafaring Addendum // Failsafe
			(party_get_current_terrain, ":terrain", "p_main_party"),
			(gt, ":terrain", 0),
			(assign, "$g_player_icon_state", pis_normal),		
         (else_try),
			(party_get_current_terrain, ":terrain", "p_main_party"),
			(eq, ":terrain", 0),
			(assign, "$g_player_icon_state", pis_ship),	 
			(party_set_flags, "p_main_party", pf_is_ship, 1),
		 (try_end),
         (rest_for_hours, 0, 0, 0), #stop camping

         (display_message, "@Breaking camp..."),
       (try_end),
     (try_end),
     ]),


#Notification menus
  (0,
   [
     (troop_slot_ge, "trp_notification_menu_types", 0, 1),
     (troop_get_slot, ":menu", "trp_notification_menu_types", 0),
     (try_begin),
       (neq, ":menu", "mnu_lieutenant_recruitment"),
       (jump_to_menu, ":menu"),
       (troop_get_slot, "$g_notification_menu_var1", "trp_notification_menu_var1", 0),
       (troop_get_slot, "$g_notification_menu_var2", "trp_notification_menu_var2", 0),
     (try_end),
     
     # Always shift the queue to remove the processed (shown or blocked) element at 0
     (try_for_range, ":idx", 0, 79),
       (store_add, ":next_idx", ":idx", 1),
       (troop_get_slot, ":next_menu", "trp_notification_menu_types", ":next_idx"),
       (troop_set_slot, "trp_notification_menu_types", ":idx", ":next_menu"),
       (troop_get_slot, ":next_var1", "trp_notification_menu_var1", ":next_idx"),
       (troop_set_slot, "trp_notification_menu_var1", ":idx", ":next_var1"),
       (troop_get_slot, ":next_var2", "trp_notification_menu_var2", ":next_idx"),
       (troop_set_slot, "trp_notification_menu_var2", ":idx", ":next_var2"),
     (try_end),
     (troop_set_slot, "trp_notification_menu_types", 79, 0),
    ]),

  #Music,
  (1,
   [
       (map_free),
       (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
	    ]),

  (0,
	[
	  #escort caravan quest auto dialog trigger
	  (try_begin),
        (eq, "$caravan_escort_state", 1),
        (party_is_active, "$caravan_escort_party_id"),

        (store_distance_to_party_from_party, ":caravan_distance_to_destination","$caravan_escort_destination_town","$caravan_escort_party_id"),
        (lt, ":caravan_distance_to_destination", 2),

        (store_distance_to_party_from_party, ":caravan_distance_to_player","p_main_party","$caravan_escort_party_id"),
        (lt, ":caravan_distance_to_player", 5),

        (assign, "$talk_context", tc_party_encounter),
        (assign, "$g_encountered_party", "$caravan_escort_party_id"),
        (party_stack_get_troop_id, ":caravan_leader", "$caravan_escort_party_id", 0),
        (party_stack_get_troop_dna, ":caravan_leader_dna", "$caravan_escort_party_id", 0),

        (start_map_conversation, ":caravan_leader", ":caravan_leader_dna"),
      (try_end),

      (try_begin),
        (gt, "$g_reset_mission_participation", 1),

        (try_for_range, ":troop", active_npcs_begin, kingdom_ladies_end),
          (troop_set_slot, ":troop", slot_troop_mission_participation, 0),
        (try_end),
      (try_end),
	]),

(24,
[
    (try_for_range, ":kingdom_no", kingdoms_begin, kingdoms_end), #Player Faction
      (faction_get_slot, ":faction_morale", ":kingdom_no",  slot_faction_morale_of_player_troops),

	  (store_sub, ":divisor", 140, "$player_right_to_rule"),
	  (val_div, ":divisor", 14),
	  (val_max, ":divisor", 1),

      (store_div, ":faction_morale_div_10", ":faction_morale", ":divisor"), #10 is the base, down to 2 for 100 rtr
      (val_sub, ":faction_morale", ":faction_morale_div_10"),

      (faction_set_slot, ":kingdom_no",  slot_faction_morale_of_player_troops, ":faction_morale"),
    (try_end),
]),


 (4, #Locate kingdom ladies
    [
      #change location for all ladies
      (try_for_range, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
        ##diplomacy start+ do not set the troop's center when the troop is leading a party
        (troop_slot_eq, ":troop_id", slot_troop_occupation, slto_kingdom_lady),
        (troop_get_slot, ":leaded_party", ":troop_id", slot_troop_leaded_party),
		(try_begin),
			(gt, ":leaded_party", 0),
			(neg|party_is_active, ":leaded_party"),
			(assign, ":leaded_party", -1),
		(try_end),
        (lt, ":leaded_party", 1),#if the value is 0, it's a bug, so overlook it
        ##diplomacy end+
        (neg|troop_slot_ge, ":troop_id", slot_troop_prisoner_of_party, 0),
        (call_script, "script_get_kingdom_lady_social_determinants", ":troop_id"),
        (assign, ":location", reg1),
        (troop_set_slot, ":troop_id", slot_troop_cur_center, ":location"),
      (try_end),
	]),


 (2, #Error check for multiple parties on the map
	[
	(eq, "$cheat_mode", 1),
	(assign, ":debug_menu_noted", 0),
	(try_for_parties, ":party_no"),
		(gt, ":party_no", "p_spawn_points_end"),
		(party_stack_get_troop_id, ":commander", ":party_no", 0),
		##diplomacy start+
		(is_between, ":commander", heroes_begin, heroes_end),
		(this_or_next|troop_slot_eq, ":commander", slot_troop_occupation, slto_kingdom_hero),
		##diplomacy end+
		(is_between, ":commander", active_npcs_begin, active_npcs_end),
		(troop_get_slot, ":commander_party", ":commander", slot_troop_leaded_party),
		(neq, ":party_no", ":commander_party"),
		(assign, reg4, ":party_no"),
		(assign, reg5, ":commander_party"),

		(str_store_troop_name, s3, ":commander"),
		(display_message, "@{!}{s3} commander of party #{reg4} which is not his troop_leaded party {reg5}"),
		##diplomacy start+ Make it clear what the error was
		(try_begin),
			(gt, reg4, 0),
			(gt, reg5, 0),
			(str_store_party_name, s3, reg4),
			(str_store_party_name, s65, reg5),
			(display_message, "@{!} Commanded party #{reg4} is {s3}, troop_leaded party #{reg5} is {s65}"),
			(str_store_troop_name, s3, ":commander"),
		(try_end),
		##diplomacy end+
		(str_store_string, s65, "str_party_with_commander_mismatch__check_log_for_details_"),

		(try_begin),
			(eq, ":debug_menu_noted", 0),
			(call_script, "script_add_notification_menu", "mnu_debug_alert_from_s65", 0, 0),
			(assign, ":debug_menu_noted", 1),
		(try_end),
	(try_end),
	]),


 (24, #Kingdom ladies send messages
 [
	(try_begin),
		(neg|check_quest_active, "qst_visit_lady"),
		(neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 1),
		(neg|troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),

		(assign, ":lady_not_visited_longest_time", -1),
		(assign, ":longest_time_without_visit", 120), #five days

		(try_for_range, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
            ##diplomacy start+ not dead, exiled, etc.
			(neg|troop_slot_ge, ":troop_id", slot_troop_occupation, slto_retirement),
            #not already betrothed
            (neg|troop_slot_eq, "trp_player", slot_troop_betrothed, ":troop_id"),
			##diplomacy end+
			#set up message for ladies the player is courting
			(troop_slot_ge, ":troop_id", slot_troop_met, 2),
			(neg|troop_slot_eq, ":troop_id", slot_troop_met, 4),

			(troop_slot_eq, ":troop_id", slot_lady_no_messages, 0),
			(troop_slot_eq, ":troop_id", slot_troop_spouse, -1),

			(troop_get_slot, ":location", ":troop_id", slot_troop_cur_center),
			(is_between, ":location", walled_centers_begin, walled_centers_end),
			(call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop_id"),
			(gt, reg0, 1),

			(store_current_hours, ":hours_since_last_visit"),
			(troop_get_slot, ":last_visit_hour", ":troop_id", slot_troop_last_talk_time),
			(val_sub, ":hours_since_last_visit", ":last_visit_hour"),

			(gt, ":hours_since_last_visit", ":longest_time_without_visit"),
			(assign, ":longest_time_without_visit", ":hours_since_last_visit"),
			(assign, ":lady_not_visited_longest_time", ":troop_id"),
			(assign, ":visit_lady_location", ":location"),

		(try_end),

		(try_begin),
			(gt, ":lady_not_visited_longest_time", 0),
			(call_script, "script_add_notification_menu", "mnu_notification_lady_requests_visit", ":lady_not_visited_longest_time", ":visit_lady_location"),
		(try_end),

	(try_end),
	]),


#Player raiding a village
# This trigger will check if player's raid has been completed and will lead control to village menu.
  (1,
   [
      (ge,"$g_player_raiding_village",1),
      (try_begin),
        (neq, "$g_player_is_captive", 0),
        #(rest_for_hours, 0, 0, 0), #stop resting - abort
        (assign,"$g_player_raiding_village",0),
	 ##Floris - comment out to allow player to cancel ; other part of code in Floris version trigger
      # (else_try),
        # (map_free), #we have been attacked during raid
        # (assign,"$g_player_raiding_village",0),
	 ##Floris - end
      (else_try),
        (this_or_next|party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_looted),
        (party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_deserted),
        (start_encounter, "$g_player_raiding_village"),
        (rest_for_hours, 0),
        (assign,"$g_player_raiding_village",0),
        (assign,"$g_player_raid_complete",1),
      (else_try),
        (party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_being_raided),
        (rest_for_hours_interactive, 3, 5, 1), ##Floris - change to interactive to allow player to cancel; #rest while attackable
      (else_try),
        (rest_for_hours, 0, 0, 0), #stop resting - abort
        (assign,"$g_player_raiding_village",0),
        (assign,"$g_player_raid_complete",0),
      (try_end),
    ]),

  #Pay day.
  (24 * 7,
   [
     ##diplomacy begin
     (store_current_hours, "$g_next_pay_time"),
     (val_add, "$g_next_pay_time", 24 * 7),
     ##diplomacy end
     (assign, "$g_presentation_lines_to_display_begin", 0),
     (assign, "$g_presentation_lines_to_display_end", 15),
     (assign, "$g_apply_budget_report_to_gold", 1),
     (try_begin),
       (eq, "$g_infinite_camping", 0),
       (start_presentation, "prsnt_budget_report"),
        ##diplomacy begin
        (try_begin),
          (gt, "$g_player_debt_to_party_members", 5000),
          (call_script, "script_add_notification_menu", "mnu_dplmc_deserters",20,0),
        (try_end),
        ##diplomacy end
     (try_end),
    ]),

  # Oath fulfilled -- ie, mercenary contract expired?
  (24,
   [
      (le, "$auto_menu", 0),
      (gt, "$players_kingdom", 0),
      (neq, "$players_kingdom", "fac_player_supporters_faction"),
      (eq, "$player_has_homage", 0),

	  (troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),

	  #A player bound to a kingdom by marriage will not have the contract expire. This should no longer be the case, as I've counted wives as having homage, but is in here as a fallback
	  (assign, ":player_has_marriage_in_faction", 0),
	  (try_begin),
		(is_between, ":player_spouse", active_npcs_begin, active_npcs_end),
		(store_faction_of_troop, ":spouse_faction", ":player_spouse"),
		(eq, ":spouse_faction", "$players_kingdom"),
	    (assign, ":player_has_marriage_in_faction", 1),
	  (try_end),
	  (eq, ":player_has_marriage_in_faction", 0),

      (store_current_day, ":cur_day"),
      (gt, ":cur_day", "$mercenary_service_next_renew_day"),
      (jump_to_menu, "mnu_oath_fulfilled"),
    ]),

  # Reducing luck by 1 in every 180 hours
  (180,
   [
     (val_sub, "$g_player_luck", 1),
     (val_max, "$g_player_luck", 0),
    ]),

	#courtship reset
  (72,
   [
     (assign, "$lady_flirtation_location", 0),
    ]),

	#reset time to spare
  (4,
   [
     (assign, "$g_time_to_spare", 1),

    (try_begin),
		(troop_slot_ge, "trp_player", slot_troop_spouse, active_npcs_begin),
		(assign, "$g_player_banner_granted", 1),
	(try_end),

	 ]),


  # Banner selection menu
  (24,
   [
    (eq, "$g_player_banner_granted", 1),
    (troop_slot_eq, "trp_player", slot_troop_banner_scene_prop, 0),
    (le,"$auto_menu",0),
#normal_banner_begin
    (start_presentation, "prsnt_banner_selection"),
#custom_banner_begin
#    (start_presentation, "prsnt_custom_banner"),
    ]),

  # Party Morale: Move morale towards target value.
  (24,
   [
      (call_script, "script_get_player_party_morale_values"),
      (assign, ":target_morale", reg0),
      (party_get_morale, ":cur_morale", "p_main_party"),
      (store_sub, ":dif", ":target_morale", ":cur_morale"),
      (store_div, ":dif_to_add", ":dif", 5),
      (store_mul, ":dif_to_add_correction", ":dif_to_add", 5),
      (try_begin),#finding ceiling of the value
        (neq, ":dif_to_add_correction", ":dif"),
        (try_begin),
          (gt, ":dif", 0),
          (val_add, ":dif_to_add", 1),
        (else_try),
          (val_sub, ":dif_to_add", 1),
        (try_end),
      (try_end),
      (val_add, ":cur_morale", ":dif_to_add"),
      (party_set_morale, "p_main_party", ":cur_morale"),
    ]),


#Party AI: pruning some of the prisoners in each center (once a week)
  (24*7,
   [
       (try_for_range, ":center_no", centers_begin, centers_end),
         (party_get_num_prisoner_stacks, ":num_prisoner_stacks",":center_no"),
         (try_for_range_backwards, ":stack_no", 0, ":num_prisoner_stacks"),
           (party_prisoner_stack_get_troop_id, ":stack_troop",":center_no",":stack_no"),
           (neg|troop_is_hero, ":stack_troop"),
           (party_prisoner_stack_get_size, ":stack_size",":center_no",":stack_no"),
           (store_random_in_range, ":rand_no", 0, 40),
           (val_mul, ":stack_size", ":rand_no"),
           (val_div, ":stack_size", 100),
           (party_remove_prisoners, ":center_no", ":stack_troop", ":stack_size"),
		   ##diplomacy start+ add prisoner value to center wealth
		   (try_begin),
		      (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),#must be explicitly enabled
			  (ge, ":center_no", 1),
			  (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
				(party_slot_eq, ":center_no", slot_party_type, spt_castle),
			  (party_slot_ge, ":center_no", slot_town_lord, 1),#"wealth" isn't used for player garrisons
			  (party_get_slot, ":cur_wealth", ":center_no", slot_town_wealth),
			  (lt, ":cur_wealth", 6000),
			  (store_mul, ":ransom_profits", ":stack_size", 10),#a fraction of what it could be sold for (50 would be a rule of thumb)
			  (val_add, ":cur_wealth", ":ransom_profits"),
			  (party_set_slot, ":center_no", slot_town_wealth, ":cur_wealth"),
		   (try_end),
		   ##diplomacy end+
         (try_end),
       (try_end),
    ]),

  #Adding net incomes to heroes (once a week)
  #Increasing debts to heroes by 1% (once a week)
  #Adding net incomes to centers (once a week)
  (24*7,
   [
		##diplomacy start+ Save register
		(assign, ":save_reg0", reg0),
		##Change to support kingdom ladies
       #(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
	   (try_for_range, ":troop_no", heroes_begin, heroes_end),
	     (this_or_next|is_between, ":troop_no", active_npcs_begin, active_npcs_end),
		 (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
	   ##diplomacy end+
         (troop_get_slot, ":cur_debt", ":troop_no", slot_troop_player_debt),#Increasing debt
         (val_mul, ":cur_debt", 101),
         (val_div, ":cur_debt", 100),
         (troop_set_slot, ":troop_no", slot_troop_player_debt, ":cur_debt"),
         (call_script, "script_calculate_hero_weekly_net_income_and_add_to_wealth", ":troop_no"),#Adding net income
       (try_end),
	   
	   ##diplomacy start+
	   (store_current_hours, ":two_weeks_ago"),
	   (val_sub, ":two_weeks_ago", 24 * 14),
	   ##diplomacy end+

       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
         #If non-player center, adding income to wealth
         (neg|party_slot_eq, ":center_no", slot_town_lord, "trp_player"), #center does not belong to player.
		 ##diplomacy start+
		 #Defer the ownership check so attrition can still occur for unowned centers.
		 #Give a slight grace period first, though.
		 (neg|party_slot_eq, ":center_no", slot_town_lord, 0),
		 (this_or_next|party_slot_ge, ":center_no", dplmc_slot_center_last_transfer_time, ":two_weeks_ago"),
			(party_slot_ge, ":center_no", slot_town_lord, 1), #center belongs to someone.
		 (this_or_next|ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
		 ##diplomacy end+
		 (party_slot_ge, ":center_no", slot_town_lord, 1), #center belongs to someone.
         (party_get_slot, ":cur_wealth", ":center_no", slot_town_wealth),
         (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
         (store_mul, ":added_wealth", ":prosperity", 15),
         (val_add, ":added_wealth", 700),
         (try_begin),
           (party_slot_eq, ":center_no", slot_party_type, spt_town),
           (val_mul, ":added_wealth", 3),
           (val_div, ":added_wealth", 2),
         (try_end),
         (val_add, ":cur_wealth", ":added_wealth"),
         (call_script, "script_calculate_weekly_party_wage", ":center_no"),
         (val_sub, ":cur_wealth", reg0),
		 ##diplomacy start+ Allow attrition to occur
		 (try_begin),
			(lt, ":cur_wealth", 0),
			(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
			(assign, ":cur_weekly_wage", reg0),
			(store_party_size_wo_prisoners, ":garrison_size", ":center_no"),
			(call_script, "script_party_get_ideal_size", ":center_no"),#This script has been modified to support this use
			(val_mul, reg0, 5),
			(val_div, reg0, 4),
			(ge, ":garrison_size", reg0),
			
			(store_sub, ":percent_under", 0, ":cur_wealth"),
			(val_mul, ":percent_under", 100),
			(val_div, ":percent_under", ":cur_weekly_wage"),
			(val_div, ":percent_under", 5), #Max 20 percent (won't take garrison below ideal size)
			(call_script, "script_party_inflict_attrition", ":center_no", ":percent_under", 1),
		 (try_end),
		 (party_slot_ge, ":center_no", slot_town_lord, 1), #center belongs to someone.
		 ##diplomacy end+
         (val_max, ":cur_wealth", 0),
         (party_set_slot, ":center_no", slot_town_wealth, ":cur_wealth"),
       (try_end),
	   ##diplomacy end+
	   (assign, reg0, ":save_reg0"),
	   ##diplomacy end+
    ]),

  #Hiring men with hero wealths (once a day)
  #Hiring men with center wealths (once a day)
  (24,
   [
     ##diplomacy start+
     ##change to allow promoted kingdom ladies to hire troops
     #(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
     (try_for_range, ":troop_no", active_npcs_begin, kingdom_ladies_end),
     ##diplomacy end+
       (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
       (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
       (ge, ":party_no", 1),
       (party_is_active, ":party_no"),
       (party_get_attached_to, ":cur_attached_party", ":party_no"),
       (is_between, ":cur_attached_party", centers_begin, centers_end),
       (party_slot_eq, ":cur_attached_party", slot_center_is_besieged_by, -1), #center not under siege

       (store_faction_of_party, ":party_faction", ":party_no"),
       (try_begin),
         (this_or_next|eq, ":party_faction", "fac_player_supporters_faction"),
         (eq, ":party_faction", "$players_kingdom"),
         (assign, ":num_hiring_rounds", 1),
         (store_random_in_range, ":random_value", 0, 2),
         (val_add, ":num_hiring_rounds", ":random_value"),
       (else_try),
         (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
         (try_begin),
           (eq, ":reduce_campaign_ai", 0), #hard (2x reinforcing)
           (assign, ":num_hiring_rounds", 2),
         (else_try),
           (eq, ":reduce_campaign_ai", 1), #medium (1x or 2x reinforcing)
           (assign, ":num_hiring_rounds", 1),
           (store_random_in_range, ":random_value", 0, 2),
           (val_add, ":num_hiring_rounds", ":random_value"),
         (else_try),
           (eq, ":reduce_campaign_ai", 2), #easy (1x reinforcing)
           (assign, ":num_hiring_rounds", 1),
         (try_end),
       (try_end),

       (try_begin),
         (this_or_next|faction_slot_eq,  ":party_faction", slot_faction_leader, ":troop_no"), ## CC
         (faction_slot_eq,  ":party_faction", slot_faction_marshall, ":troop_no"),
         (val_add, ":num_hiring_rounds", 1),
       (try_end),

       ## CC
       (troop_get_slot, ":cur_wealth", ":troop_no", slot_troop_wealth),
       (store_div, ":num_rounds", ":cur_wealth", 10000),
       (val_add, ":num_rounds", 1),
       
       (assign, ":center_score", 0),
       (store_troop_faction, ":troop_faction", ":troop_no"),
       (try_for_range, ":cur_center", centers_begin, centers_end),
         (store_faction_of_party, ":town_faction", ":cur_center"),
         (eq, ":town_faction", ":troop_faction"),
         (try_begin),
           (party_slot_eq, ":cur_center", slot_party_type, spt_village),
           (val_add, ":center_score", 1),
         (else_try),
           (party_slot_eq, ":cur_center", slot_party_type, spt_castle),
           (val_add, ":center_score", 2),
         (else_try),
           (party_slot_eq, ":cur_center", slot_party_type, spt_town),
           (val_add, ":center_score", 4),
         (try_end),
       (try_end),
       (val_max, ":center_score", 1),
       (store_div, ":rounds_multi", 9, ":center_score"),
       (val_add, ":rounds_multi", 1),
       (val_mul, ":num_rounds", ":rounds_multi"),
       (val_add, ":num_hiring_rounds", ":num_rounds"),
       ## CC

       (try_for_range, ":unused", 0, ":num_hiring_rounds"),         
         (call_script, "script_hire_men_to_kingdom_hero_party", ":troop_no"), #Hiring men with current wealth        
       (try_end),
     (try_end),

     (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
       (neg|party_slot_eq, ":center_no", slot_town_lord, "trp_player"), #center does not belong to player.
       (party_slot_ge, ":center_no", slot_town_lord, 1), #center belongs to someone.
       (party_slot_eq, ":center_no", slot_center_is_besieged_by, -1), #center not under siege

       (store_faction_of_party, ":center_faction", ":center_no"),
       (try_begin),
         (this_or_next|eq, ":center_faction", "fac_player_supporters_faction"),
         (eq, ":center_faction", "$players_kingdom"),
         (assign, ":num_hiring_rounds", 1), ## CC
         (assign, ":reinforcement_cost", reinforcement_cost_moderate),
       (else_try),
         (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
         (assign, ":reinforcement_cost", reinforcement_cost_moderate),
         (try_begin),
           (eq, ":reduce_campaign_ai", 0), #hard (1x or 2x reinforcing)
           (assign, ":reinforcement_cost", reinforcement_cost_hard),
           (store_random_in_range, ":num_hiring_rounds", 0, 2),
           (val_add, ":num_hiring_rounds", 1),
         (else_try),
           (eq, ":reduce_campaign_ai", 1), #moderate (1x reinforcing)
           (assign, ":reinforcement_cost", reinforcement_cost_moderate),
           (assign, ":num_hiring_rounds", 1),
         (else_try),
           (eq, ":reduce_campaign_ai", 2), #easy (none or 1x reinforcing)
           (assign, ":reinforcement_cost", reinforcement_cost_easy),
           (store_random_in_range, ":num_hiring_rounds", 0, 2),
         (try_end),
       (try_end),
       ## CC
       (try_begin),
         (is_between, ":center_no", towns_begin, towns_end),
         (val_add, ":num_hiring_rounds", 1),
       (try_end),
       ## CC
       (try_for_range, ":unused", 0, ":num_hiring_rounds"), 
         (party_get_slot, ":cur_wealth", ":center_no", slot_town_wealth),
         (assign, ":hiring_budget", ":cur_wealth"),
         (val_div, ":hiring_budget", 2),
         (gt, ":hiring_budget", ":reinforcement_cost"),
         (call_script, "script_cf_reinforce_party", ":center_no"),
         (val_sub, ":cur_wealth", ":reinforcement_cost"),
         (party_set_slot, ":center_no", slot_town_wealth, ":cur_wealth"),
       (try_end),
     (try_end),

     #this is moved up from below , from a 24 x 15 slot to a 24 slot
     (try_for_range, ":center_no", centers_begin, centers_end),
       #(neg|is_between, ":center_no", castles_begin, castles_end),
       (store_random_in_range, ":random", 0, 30),
       (le, ":random", 10),
	   
       (call_script, "script_get_center_ideal_prosperity", ":center_no"),
       (assign, ":ideal_prosperity", reg0),
       (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),       
       (try_begin),
	     (eq, ":random", 0), #with 3% probability it will gain +10/-10 prosperity even it has higher prosperity than its ideal prosperity.
         (try_begin),
           (store_random_in_range, ":random", 0, 2),
           (try_begin),
             (eq, ":random", 0),
             (neg|is_between, ":center_no", castles_begin, castles_end), #castles always gain positive prosperity from surprise income to balance their prosperity.
             (call_script, "script_change_center_prosperity", ":center_no", -10),
             (val_add, "$newglob_total_prosperity_from_convergence", -10),
           (else_try),     
             (call_script, "script_change_center_prosperity", ":center_no", 10),
             (val_add, "$newglob_total_prosperity_from_convergence", 10),
           (try_end),
         (try_end),
	   (else_try),
         (gt, ":prosperity", ":ideal_prosperity"),		 
         (call_script, "script_change_center_prosperity", ":center_no", -1),
         (val_add, "$newglob_total_prosperity_from_convergence", -1),
       (else_try),
         (lt, ":prosperity", ":ideal_prosperity"),		 
         (call_script, "script_change_center_prosperity", ":center_no", 1),
         (val_add, "$newglob_total_prosperity_from_convergence", 1),
	   (try_end),
     (try_end),	
    ]),

  #Converging center prosperity to ideal prosperity once in every 15 days
  (24*15,
   [#(try_for_range, ":center_no", centers_begin, centers_end),
    #  (call_script, "script_get_center_ideal_prosperity", ":center_no"),
    #  (assign, ":ideal_prosperity", reg0),
    #  (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
    #  (try_begin),
    #    (gt, ":prosperity", ":ideal_prosperity"),
    #    (call_script, "script_change_center_prosperity", ":center_no", -1),
    #  (else_try),
    #    (lt, ":prosperity", ":ideal_prosperity"),
    #    (call_script, "script_change_center_prosperity", ":center_no", 1),
    #  (try_end),
    #(try_end),
    ]),

  #Checking if the troops are resting at a half payment point
  (6,
   [(store_current_day, ":cur_day"),
    (try_begin),
      (neq, ":cur_day", "$g_last_half_payment_check_day"),
      (assign, "$g_last_half_payment_check_day", ":cur_day"),
      (try_begin),
        (eq, "$g_half_payment_checkpoint", 1),
        (val_add, "$g_cur_week_half_daily_wage_payments", 1), #half payment for yesterday
      (try_end),
      (assign, "$g_half_payment_checkpoint", 1),
    (try_end),
    (assign, ":resting_at_manor_or_walled_center", 0),
    (try_begin),
      (neg|map_free),
      (ge, "$g_last_rest_center", 0),
      (this_or_next|party_slot_eq, "$g_last_rest_center", slot_center_has_manor, 1),
      (is_between, "$g_last_rest_center", walled_centers_begin, walled_centers_end),
      (assign, ":resting_at_manor_or_walled_center", 1),
    (try_end),
    (eq, ":resting_at_manor_or_walled_center", 0),
    (assign, "$g_half_payment_checkpoint", 0),
    ]),

#diplomatic indices
  (24,
   [
   (call_script, "script_randomly_start_war_peace_new", 1),

   (try_begin),
		(store_random_in_range, ":acting_village", villages_begin, villages_end),
		(store_random_in_range, ":target_village", villages_begin, villages_end),
		(store_faction_of_party, ":acting_faction", ":acting_village"),
		(store_faction_of_party, ":target_faction", ":target_village"), #target faction receives the provocation
		(neq, ":acting_village", ":target_village"),
		(neq, ":acting_faction", ":target_faction"),

		(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":target_faction", ":acting_faction"),
		(eq, reg0, 0),

		(try_begin),
			(party_slot_eq, ":acting_village", slot_center_original_faction, ":target_faction"),

			(call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", -1),
		(else_try),
			(party_slot_eq, ":acting_village", slot_center_ex_faction, ":target_faction"),

			(call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", -1),

		(else_try),
			(set_fixed_point_multiplier, 1),
			(store_distance_to_party_from_party, ":distance", ":acting_village", ":target_village"),
			(lt, ":distance", 25),

			(call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", ":target_village"),
		(try_end),
   (try_end),

   (try_for_range, ":faction_1", kingdoms_begin, kingdoms_end),
		(faction_slot_eq, ":faction_1", slot_faction_state, sfs_active),
		(try_for_range, ":faction_2", kingdoms_begin, kingdoms_end),
			(neq, ":faction_1", ":faction_2"),
			(faction_slot_eq, ":faction_2", slot_faction_state, sfs_active),

			#remove provocations
			(store_add, ":slot_truce_days", ":faction_2", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":slot_truce_days", kingdoms_begin),
			(faction_get_slot, ":truce_days", ":faction_1", ":slot_truce_days"),
			(try_begin),
				(ge, ":truce_days", 1),
				(try_begin),
					(eq, ":truce_days", 1),
					(call_script, "script_update_faction_notes", ":faction_1"),
					(lt, ":faction_1", ":faction_2"),
					(call_script, "script_add_notification_menu", "mnu_notification_truce_expired", ":faction_1", ":faction_2"),
				##diplomacy begin
				##nested diplomacy start+ Replace "magic numbers" with named constants
				(else_try),
				  (eq, ":truce_days", dplmc_treaty_alliance_days_expire + 1),#replaced 61
				  (call_script, "script_update_faction_notes", ":faction_1"),
				  (lt, ":faction_1", ":faction_2"),
				  (call_script, "script_add_notification_menu", "mnu_dplmc_notification_alliance_expired", ":faction_1", ":faction_2"),
				(else_try),
				  (eq, ":truce_days",dplmc_treaty_defense_days_expire + 1),#replaced 41
				  (call_script, "script_update_faction_notes", ":faction_1"),
				  (lt, ":faction_1", ":faction_2"),
				  (call_script, "script_add_notification_menu", "mnu_dplmc_notification_defensive_expired", ":faction_1", ":faction_2"),
				(else_try),
				  (eq, ":truce_days", dplmc_treaty_trade_days_expire + 1),#replaced 21
				  (call_script, "script_update_faction_notes", ":faction_1"),
				  (lt, ":faction_1", ":faction_2"),
				  (call_script, "script_add_notification_menu", "mnu_dplmc_notification_trade_expired", ":faction_1", ":faction_2"),
				##nested diplomacy end+
				##diplomacy end
				(try_end),
				(val_sub, ":truce_days", 1),
				(faction_set_slot, ":faction_1", ":slot_truce_days", ":truce_days"),
			(try_end),

			(store_add, ":slot_provocation_days", ":faction_2", slot_faction_provocation_days_with_factions_begin),
			(val_sub, ":slot_provocation_days", kingdoms_begin),
			(faction_get_slot, ":provocation_days", ":faction_1", ":slot_provocation_days"),
			(try_begin),
				(ge, ":provocation_days", 1),
				(try_begin),#factions already at war
					(store_relation, ":relation", ":faction_1", ":faction_2"),
					(lt, ":relation", 0),
					(faction_set_slot, ":faction_1", ":slot_provocation_days", 0),
				(else_try), #Provocation expires
					(eq, ":provocation_days", 1),
					(call_script, "script_add_notification_menu", "mnu_notification_casus_belli_expired", ":faction_1", ":faction_2"),
					(faction_set_slot, ":faction_1", ":slot_provocation_days", 0),
				(else_try),
					(val_sub, ":provocation_days", 1),
					(faction_set_slot, ":faction_1", ":slot_provocation_days", ":provocation_days"),
				(try_end),
			(try_end),

			(try_begin), #at war
				(store_relation, ":relation", ":faction_1", ":faction_2"),
				(lt, ":relation", 0),
				(store_add, ":slot_war_damage", ":faction_2", slot_faction_war_damage_inflicted_on_factions_begin),
				(val_sub, ":slot_war_damage", kingdoms_begin),
				(faction_get_slot, ":war_damage", ":faction_1", ":slot_war_damage"),
				(val_add, ":war_damage", 1),
				(faction_set_slot, ":faction_1", ":slot_war_damage", ":war_damage"),
			(try_end),

		(try_end),
		(call_script, "script_update_faction_notes", ":faction_1"),
	(try_end),
    ]),

  # Give some xp to hero parties
   (48,
   [
       ##diplomacy start+
       ##change to allow promoted kingdom ladies to hire troops
       #(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
       (try_for_range, ":troop_no", heroes_begin, heroes_end),
       ##diplomacy end+
         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),

         (troop_get_slot, ":hero_party", ":troop_no", slot_troop_leaded_party),
         (gt, ":hero_party", centers_end),
         (party_is_active, ":hero_party"),

         (store_skill_level, ":trainer_level", skl_trainer, ":troop_no"),
         (val_add, ":trainer_level", 5), #average trainer level is 3 for npc lords, worst : 0, best : 6
         (store_mul, ":xp_gain", ":trainer_level", 1000), #xp gain in two days of period for each lord, average : 8000.

         (assign, ":max_accepted_random_value", 30),
         (try_begin),
           (store_troop_faction, ":cur_troop_faction", ":troop_no"),
           (neq, ":cur_troop_faction", "$players_kingdom"),
           
           (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
           (try_begin),
             (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
             (assign, ":max_accepted_random_value", 35),
             (val_mul, ":xp_gain", 3),
             (val_div, ":xp_gain", 2),
           (else_try),
             (eq, ":reduce_campaign_ai", 2), #easy (0.5x)
             (assign, ":max_accepted_random_value", 25),
             (val_div, ":xp_gain", 2),
           (try_end),
         (try_end),
         
         (store_random_in_range, ":rand", 0, 100),
         (le, ":rand", ":max_accepted_random_value"),

         (party_upgrade_with_xp, ":hero_party", ":xp_gain"),
       (try_end),
       
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),         
         (party_get_slot, ":center_lord", ":center_no", slot_town_lord),
         (neq, ":center_lord", "trp_player"),
         
         (assign, ":xp_gain", 3000), #xp gain in two days of period for each center, average : 3000.
         
         (assign, ":max_accepted_random_value", 30),
         (try_begin),            
           (assign, ":cur_center_lord_faction", -1),
           (try_begin),
             (ge, ":center_lord", 0),
             (store_troop_faction, ":cur_center_lord_faction", ":center_lord"),
           (try_end),             
           (neq, ":cur_center_lord_faction", "$players_kingdom"),
           
           (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
           (try_begin),
             (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
             (assign, ":max_accepted_random_value", 35),
             (val_mul, ":xp_gain", 3),
             (val_div, ":xp_gain", 2),
           (else_try),
             (eq, ":reduce_campaign_ai", 2), #easy (0.5x)
             (assign, ":max_accepted_random_value", 25),
             (val_div, ":xp_gain", 2),
           (try_end),
         (try_end),

         (store_random_in_range, ":rand", 0, 100),
         (le, ":rand", ":max_accepted_random_value"),

         (party_upgrade_with_xp, ":center_no", ":xp_gain"),
       (try_end),
    ]),

  # Process sieges
   (24,
   [
       (call_script, "script_process_sieges"),
    ]),

  # Process village raids
   (2,
   [
       (call_script, "script_process_village_raids"),
    ]),


  # Decide vassal ai
   (7,
    [
      (call_script, "script_init_ai_calculation"),
      #(call_script, "script_decide_kingdom_party_ais"),
	  ##diplomacy start+
	  #Also call script_calculate_troop_ai for kingdom ladies who have become slto_kingdom_heroes
      #(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
	  (try_for_range, ":troop_no", heroes_begin, heroes_end),
	  ##diplomacy end+
        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (call_script, "script_calculate_troop_ai", ":troop_no"),
      (try_end),
      ]),

  # Hold regular marshall elections for players_kingdom
   (24, #Disabled in favor of new system
    [
    #  (val_add, "$g_election_date", 1),
    #  (ge, "$g_election_date", 90), #elections holds once in every 90 days.
    #  (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
    #  (neq, "$players_kingdom", "fac_player_supporters_faction"),
    #  (assign, "$g_presentation_input", -1),
    #  (assign, "$g_presentation_marshall_selection_1_vote", 0),
    #  (assign, "$g_presentation_marshall_selection_2_vote", 0),

    #  (assign, "$g_presentation_marshall_selection_max_renown_1", -10000),
    #  (assign, "$g_presentation_marshall_selection_max_renown_2", -10000),
    #  (assign, "$g_presentation_marshall_selection_max_renown_3", -10000),
    #  (assign, "$g_presentation_marshall_selection_max_renown_1_troop", -10000),
    #  (assign, "$g_presentation_marshall_selection_max_renown_2_troop", -10000),
    #  (assign, "$g_presentation_marshall_selection_max_renown_3_troop", -10000),
    #  (assign, ":num_men", 0),
    #  (try_for_range, ":loop_var", "trp_kingdom_heroes_including_player_begin", active_npcs_end),
    #    (assign, ":cur_troop", ":loop_var"),
    #    (assign, ":continue", 0),
    #    (try_begin),
    #      (eq, ":loop_var", "trp_kingdom_heroes_including_player_begin"),
    #      (assign, ":cur_troop", "trp_player"),
    #      (try_begin),
    #        (eq, "$g_player_is_captive", 0),
    #        (assign, ":continue", 1),
    #      (try_end),
    #    (else_try),
#		  (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
 #         (store_troop_faction, ":cur_troop_faction", ":cur_troop"),
 #         (eq, "$players_kingdom", ":cur_troop_faction"),
  #        #(troop_slot_eq, ":cur_troop", slot_troop_is_prisoner, 0),
  #        (neg|troop_slot_ge, ":cur_troop", slot_troop_prisoner_of_party, 0),
   #       (troop_slot_ge, ":cur_troop", slot_troop_leaded_party, 1),
    #      (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
    #      (neg|faction_slot_eq, ":cur_troop_faction", slot_faction_leader, ":cur_troop"),
    #      (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
    #      (gt, ":cur_party", 0),
    #      (party_is_active, ":cur_party"),
    #      (call_script, "script_party_count_fit_for_battle", ":cur_party"),
    #      (assign, ":party_fit_for_battle", reg0),
    #      (call_script, "script_party_get_ideal_size", ":cur_party"),
    #      (assign, ":ideal_size", reg0),
    #      (store_mul, ":relative_strength", ":party_fit_for_battle", 100),
    #      (val_div, ":relative_strength", ":ideal_size"),
    #      (ge, ":relative_strength", 25),
    #      (assign, ":continue", 1),
    #    (try_end),
    #    (eq, ":continue", 1),
    #    (val_add, ":num_men", 1),
    #    (troop_get_slot, ":renown", ":cur_troop", slot_troop_renown),
    #    (try_begin),
    #      (gt, ":renown", "$g_presentation_marshall_selection_max_renown_1"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3", "$g_presentation_marshall_selection_max_renown_2"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_2", "$g_presentation_marshall_selection_max_renown_1"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_1", ":renown"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3_troop", "$g_presentation_marshall_selection_max_renown_2_troop"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_2_troop", "$g_presentation_marshall_selection_max_renown_1_troop"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_1_troop", ":cur_troop"),
    #    (else_try),
    #      (gt, ":renown", "$g_presentation_marshall_selection_max_renown_2"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3", "$g_presentation_marshall_selection_max_renown_2"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_2", ":renown"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3_troop", "$g_presentation_marshall_selection_max_renown_2_troop"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_2_troop", ":cur_troop"),
    #    (else_try),
    #      (gt, ":renown", "$g_presentation_marshall_selection_max_renown_3"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3", ":renown"),
    #      (assign, "$g_presentation_marshall_selection_max_renown_3_troop", ":cur_troop"),
    #    (try_end),
    #  (try_end),
    #  (ge, "$g_presentation_marshall_selection_max_renown_1_troop", 0),
    #  (ge, "$g_presentation_marshall_selection_max_renown_2_troop", 0),
    #  (ge, "$g_presentation_marshall_selection_max_renown_3_troop", 0),
    #  (gt, ":num_men", 2), #at least 1 voter
    #  (assign, "$g_election_date", 0),
    #  (assign, "$g_presentation_marshall_selection_ended", 0),
    #  (try_begin),
    #    (neq, "$g_presentation_marshall_selection_max_renown_1_troop", "trp_player"),
    #    (neq, "$g_presentation_marshall_selection_max_renown_2_troop", "trp_player"),
    #    (start_presentation, "prsnt_marshall_selection"),
    #  (else_try),
    #    (jump_to_menu, "mnu_marshall_selection_candidate_ask"),
    #  (try_end),
      ]),#

   (24,
    [
	##diplomacy start+ Add support for promoted kingdom ladies
	##OLD:
	#(try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
	##NEW:
	(try_for_range, ":kingdom_hero", heroes_begin, heroes_end),
		(this_or_next|is_between, ":kingdom_hero", active_npcs_begin, active_npcs_end),
		(troop_slot_eq, ":kingdom_hero", slot_troop_occupation, slto_kingdom_hero),
	##diplomacy end+
		(troop_get_slot, ":impatience", ":kingdom_hero", slot_troop_intrigue_impatience),
		(val_sub, ":impatience", 5),
		(val_max, ":impatience", 0),
		(troop_set_slot, ":kingdom_hero", slot_troop_intrigue_impatience, ":impatience"),
	(try_end),


	(store_random_in_range, ":controversy_deduction", 1, 3),
	(val_min, ":controversy_deduction", 2),
#	(assign, ":controversy_deduction", 1),

	#This reduces controversy by one each round
	##diplomacy start+ Add support for promoted kingdom ladies
	##OLD:
	#(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
	##NEW:
	(try_for_range, ":active_npc", heroes_begin, heroes_end),
		(this_or_next|is_between, ":active_npc", active_npcs_begin, active_npcs_end),
		(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
	##diplomacy end+
		(troop_get_slot, ":controversy", ":active_npc", slot_troop_controversy),
		(ge, ":controversy", 1),
		(val_sub, ":controversy", ":controversy_deduction"),
		(val_max, ":controversy", 0),
		(troop_set_slot, ":active_npc", slot_troop_controversy, ":controversy"),
	(try_end),

	(troop_get_slot, ":controversy", "trp_player", slot_troop_controversy),
	(val_sub, ":controversy", ":controversy_deduction"),
	(val_max, ":controversy", 0),
	(troop_set_slot, "trp_player", slot_troop_controversy, ":controversy"),

	]),

    #POLITICAL TRIGGERS
	#POLITICAL TRIGGER #1`
   (8, #increased from 12
    [
	(call_script, "script_cf_random_political_event"),

	#Added Nov 2010 begins - do this twice
	(call_script, "script_cf_random_political_event"),
	#Added Nov 2010 ends

	#This generates quarrels and occasional reconciliations and interventions
	]),

	#Individual lord political calculations
	#Check for lords without fiefs, auto-defections, etc
   (0.5,
    [
	##diplomacy start+
	#This is fairly complicated, and it was getting nearly unreadable so I reformatted it.
	#The old version is visible in version control.
	(assign, ":save_reg0", reg0),
	(val_add, "$g_lord_long_term_count", 1),
	(try_begin),
		(neg|is_between, "$g_lord_long_term_count", active_npcs_including_player_begin, active_npcs_end),
		(assign, "$g_lord_long_term_count", active_npcs_including_player_begin),
	(try_end),

	##Add political calculations for kingdom ladies.  Just extending the range would
	##slow down the political calculations cycle, which would have possibly-unforeseen results.
	##Instead, add a second iteration to deal with extensions.
	(try_for_range, ":iteration", 0, 2),
		(assign, ":troop_no", "$g_lord_long_term_count"),
		(try_begin),
			(eq, ":iteration", 1),
			(val_sub, ":troop_no", active_npcs_including_player_begin),
			(val_add, ":troop_no", active_npcs_end),
		(try_end),
		#Crude check to make sure that a careless modder (i.e. me) didn't decide it
		#would be a good idea to redefine active_npcs to include kingdom_ladies,
		#which would make the second iteration run off the end of the heroes list.
		(is_between, ":troop_no", active_npcs_including_player_begin, heroes_end),

		#Special handling for trp_player, and get the troop's faction
		(try_begin),
			(eq, ":troop_no", "trp_kingdom_heroes_including_player_begin"),
			(assign, ":troop_no", "trp_player"),
			(assign, ":faction", "$players_kingdom"),
		(else_try),
			(store_faction_of_troop, ":faction", ":troop_no"),
		(try_end),

		(try_begin),
			(eq, "$cheat_mode", 1),
			(str_store_troop_name, s9, ":troop_no"),
			(display_message, "@{!}DEBUG -- Doing political calculations for {s9}"),
		(try_end),

        #Tally the fiefs owned by the hero, and cache the value in slot.
		#If a lord owns no fiefs, his relations with his liege may deteriorate.
        (try_begin),
			(assign, reg0, 1),#Center points + 1
			(try_for_range, ":center", centers_begin, centers_end),
				(party_slot_eq, ":center", slot_town_lord, ":troop_no"),
				(try_begin),
					(is_between, ":center", towns_begin, towns_end),
					(val_add, reg0, 3),#3 points per town
				(else_try),
					(is_between, ":center", walled_centers_begin, walled_centers_end),
					(val_add, reg0, 2),#2 points per castle
				(else_try),
					(val_add, reg0, 1),#1 point per village
				(try_end),
			(try_end),
			#Update cached total
			(troop_set_slot, ":troop_no", dplmc_slot_troop_center_points_plus_one, reg0),
			#If a lord has no fiefs, relation loss potentially results.
			#Do not apply this to the player.
			(eq, reg0, 1),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			(neq, ":troop_no", "trp_player"),

			#Don't apply this to the leader
			(faction_get_slot, ":faction_leader", ":faction", slot_faction_leader),
			(gt, ":faction_leader", -1),
			(neq, ":faction_leader", ":troop_no"),
			(neg|troop_slot_eq, ":faction_leader", slot_troop_spouse, ":troop_no"),
			(neg|troop_slot_eq, ":troop_no", slot_troop_spouse, ":faction_leader"),

			(troop_get_slot, ":troop_reputation", ":troop_no", slot_lord_reputation_type),
			(try_begin),
				(this_or_next|eq, ":troop_reputation", lrep_quarrelsome),
				(this_or_next|eq, ":troop_reputation", lrep_selfrighteous),
				(this_or_next|eq, ":troop_reputation", lrep_cunning),
				(eq, ":troop_reputation", lrep_debauched),
				(call_script, "script_troop_change_relation_with_troop", ":troop_no", ":faction_leader", -4),
				(val_add, "$total_no_fief_changes", -4),
			(else_try),
				(this_or_next|eq, ":troop_reputation", lrep_ambitious),#add support for lady personalities
				(eq, ":troop_reputation", lrep_martial),
				(call_script, "script_troop_change_relation_with_troop", ":troop_no", ":faction_leader", -2),
				(val_add, "$total_no_fief_changes", -2),
			(try_end),
        (try_end),

        #Auto-indictment or defection
        (try_begin),
			(this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			(eq, ":troop_no", "trp_player"),

			#There must be a valid faction leader.  The faction leader won't defect from his own kingdom.
			#To avoid certain potential complications, also skip the defection/indictment check for the
			#spouse of the faction leader.  (Code to make that possible can be added elsewhere if
			#necessary.)
			(faction_get_slot, ":faction_leader", ":faction", slot_faction_leader),
			(gt, ":faction_leader", -1),
			(neq, ":troop_no", ":faction_leader"),
			(neg|troop_slot_eq, ":troop_no", slot_troop_spouse, ":faction_leader"),
			(neg|troop_slot_eq, ":faction_leader", slot_troop_spouse, ":troop_no"),

			#"I don't know why these are necessary, but they appear to be"
			#I am not about to put that to the test, even if I think it's silly.
			(neg|is_between, ":troop_no", "trp_kingdom_1_lord", "trp_knight_1_1"),
			(neg|is_between, ":troop_no", pretenders_begin, pretenders_end),

		  (assign, ":num_centers", 0),		  
		  (try_for_range,":cur_center", walled_centers_begin, walled_centers_end),		    
		    (store_faction_of_party, ":faction_of_center", ":cur_center"),
			(eq, ":faction_of_center", ":faction"),			
			(val_add, ":num_centers", 1),
		  (try_end),

		  #we are counting num_centers to allow defection although there is high relation between faction leader and troop. 
		  #but this rule should not applied for player's faction and player_supporters_faction so thats why here 1 is added to num_centers in that case.
		  (try_begin), 
		    (this_or_next|eq, ":faction", "$players_kingdom"),
			(eq, ":faction", "fac_player_supporters_faction"),
			(val_add, ":num_centers", 1),
		  (try_end),
			
          (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
          (this_or_next|le, reg0, -50), #was -75
		  (eq, ":num_centers", 0), #if there is no walled centers that faction has defection happens 100%.

			(call_script, "script_cf_troop_can_intrigue", ":troop_no", 0), #Should include battle, prisoner, in a castle with others

			#The more centralized the faction, the greater the chance the liege will indict
			#the lord before he defects.
			(faction_get_slot, reg0, ":faction", dplmc_slot_faction_centralization),
			(val_clamp, reg0, -3, 4),
			(val_add, reg0, 10),#7 minimum, 13 maximum
			(store_random_in_range, ":random", 0, reg0),
			#Random  < 5: The lord defects
			#Random >= 5: The liege indicts the lord for treason

			(try_begin),
				(this_or_next|eq, ":num_centers", 0), #Thanks Caba`drin & Osviux				
				(lt, ":random", 5),
				(neq, ":troop_no", "trp_player"),
				#do a defection
                (try_begin), 
                   (neq, ":num_centers", 0),                 
				   (assign, "$g_give_advantage_to_original_faction", ":troop_no"),#Note that I assign the troop number instead of 1 as is done in Native
	            (try_end),
                (call_script, "script_lord_find_alternative_faction", ":troop_no"),
				(assign, ":new_faction", reg0),
				(assign, "$g_give_advantage_to_original_faction", 0),
				(neq, ":new_faction", ":faction"),
				(is_between, ":new_faction", kingdoms_begin, kingdoms_end),
				(str_store_troop_name_link, s1, ":troop_no"),
				(str_store_faction_name_link, s2, ":new_faction"),
				(str_store_faction_name_link, s3, ":faction"),
				(call_script, "script_change_troop_faction", ":troop_no", ":new_faction"),
				(try_begin),
					(ge, "$cheat_mode", 1),
					(str_store_troop_name, s4, ":troop_no"),
					(display_message, "@{!}DEBUG - {s4} faction changed in defection"),
				(try_end),
				(call_script, "script_dplmc_store_troop_is_female", ":troop_no"),
				(assign, reg4, reg0),
				(str_store_string, s4, "str_lord_defects_ordinary"),
				(display_log_message, "@{!}{s4}"),
				(try_begin),
					(eq, "$cheat_mode", 1),
					(this_or_next|eq, ":new_faction", "$players_kingdom"),
					(eq, ":faction", "$players_kingdom"),
					(call_script, "script_add_notification_menu", "mnu_notification_lord_defects", ":troop_no", ":faction"),
				(try_end),
			(else_try),
				(neq, ":faction_leader", "trp_player"),
                (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
                (le, reg0, -75),
				#do an indictment
				(call_script, "script_indict_lord_for_treason", ":troop_no", ":faction"),
			(try_end),

			#Update :faction if it has changed
			(try_begin),
				(eq, ":troop_no", "trp_player"),
				(assign, reg0, "$players_kingdom"),
			(else_try),
				(store_faction_of_troop, reg0, ":troop_no"),
			(try_end),
			(neq, reg0, ":faction"),#Fall through if indictment/defection didn't happen
			(assign, ":faction", reg0),
		(else_try),  #Take a stand on an issue
			(neq, ":troop_no", "trp_player"),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
			(faction_slot_ge, ":faction", slot_faction_political_issue, 1),
			#This bit of complication is needed for savegame compatibility -- if zero is in the slot, they'll choose anyway
			(neg|troop_slot_ge, ":troop_no", slot_troop_stance_on_faction_issue, 1),
			(this_or_next|troop_slot_eq, ":troop_no", slot_troop_stance_on_faction_issue, -1),
				(neq, "$players_kingdom", ":faction"),

			(call_script, "script_npc_decision_checklist_take_stand_on_issue", ":troop_no"),
			(troop_set_slot, ":troop_no", slot_troop_stance_on_faction_issue, reg0),
        (else_try),
			#OPTIONAL CHANGE (AI CHANGES HIGH):
			(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_HIGH),
			#If an AI kingdom has fiefless lords and no free fiefs, the king
			#will consider giving up a village.  The king will not give up fiefs if
			#doing so would give him less territory than another lord of his faction.
			#(For simplicity, the AI will not do this while a marshall appointment
			#is pending.)
			(faction_slot_eq, ":faction", slot_faction_leader, ":troop_no"),
			(neq, ":troop_no", "trp_player"),
			#With fewer than 3 points we don't need to bother continuing, since 2 points means he only owns a single village.
			(troop_get_slot, ":local_temp", ":troop_no", dplmc_slot_troop_center_points_plus_one),
			(ge, ":local_temp", 3),
			#Don't do this while other business is pending
			(neg|faction_slot_ge, ":faction", slot_faction_political_issue, 1),
			#Find the fiefless lord of his faction that the king likes best.
			#Terminate the search early if he finds another lord whose fiefs
			#equal or exceed his own, or a lord whose fief point slot is not
			#initialized.
			(assign, ":end_cond", heroes_end),
			(assign, ":any_found", -200),
			(assign, ":best_active_npc", -1),
			(try_for_range, ":active_npc", heroes_begin, ":end_cond"),
				(neq, ":active_npc", ":troop_no"),
				(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
				(store_faction_of_troop, reg0, ":active_npc"),
				(eq, reg0, ":faction"),
				(troop_get_slot, reg0, ":active_npc", dplmc_slot_troop_center_points_plus_one),
				(try_begin),
					#Terminate.  The king cannot give up any points without being outfieffed (if he isn't already)
					(ge, reg0, ":local_temp"),
					(assign, ":end_cond", ":active_npc"),
				(else_try),
					#Terminate.  The first pass of political calculations aren't done, or things are in flux.
					(lt, reg0, 1),
					(assign, ":end_cond", ":active_npc"),
				(else_try),
					(eq, reg0, 1),
					(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":active_npc"),
					(gt, reg0, ":any_found"),
					(assign, ":any_found", reg0),
					(assign, ":best_active_npc", ":active_npc"),
				(try_end),
			(try_end),
			(eq, ":end_cond", heroes_end),
			(is_between, ":best_active_npc", heroes_begin, heroes_end),
			(gt, ":any_found", -10),
			#Give up the least prosperous fief.
			(assign, ":local_temp", 101),
			(assign, ":any_found", -1),
			(try_for_range, ":center", villages_begin, villages_end),
				(party_slot_eq, ":center", slot_town_lord, ":troop_no"),
				(party_get_slot, reg0, ":center", slot_town_prosperity),
				(this_or_next|eq, ":any_found", -1),
				(lt, reg0, ":local_temp"),
				(assign, ":local_temp", reg0),
				(assign, ":any_found", ":center"),
			(try_end),
			#Clear village's lord
			(is_between, ":any_found", centers_begin, centers_end),
			(party_set_slot, ":any_found", slot_town_lord, -1),
			(troop_get_slot, reg0, ":troop_no", dplmc_slot_troop_center_points_plus_one),
			(val_sub, reg0, 1),
			(troop_set_slot, ":troop_no", dplmc_slot_troop_center_points_plus_one, reg0),
			(str_store_party_name_link, s4, ":any_found"),
			(str_store_troop_name_link, s5, ":troop_no"),
			(str_store_faction_name_link, s7, ":faction"),
			(display_log_message, "@{s5} has decided to grant {s4} to another lord of the {s7}."),
			#Reset faction issue
			(try_for_range, ":active_npc", heroes_begin, heroes_end),
				(store_faction_of_troop, reg0, ":active_npc"),
				(eq, reg0, ":faction"),
				(troop_set_slot, ":troop_no", slot_troop_stance_on_faction_issue, -1),
			(try_end),
			(store_current_hours, reg0),
			(faction_set_slot, ":faction", slot_faction_political_issue_time, reg0),
			(faction_set_slot, ":faction", slot_faction_political_issue, ":any_found"),
			#Set the liege's position on the issue, since he gave up the village with
			#something specific in mind.
			(troop_set_slot, ":troop_no", slot_troop_stance_on_faction_issue, ":best_active_npc"),
		(try_end),

		#Reduce grudges over time
		(try_begin),
			#Skip this for the dead
			(neg|troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_dead),
			#Do not perform this for kingdom ladies, since it will potentially mess up courtship.
			(neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_lady),

			(try_for_range, ":active_npc", heroes_begin, heroes_end),
				(neq, ":active_npc", ":troop_no"),
				(neg|troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_lady),#Don't do for ladies
				(neg|troop_slot_eq, ":active_npc", slot_troop_occupation, dplmc_slto_dead),#Don't do for the dead

				#Fix: there are some NPCs that have "initial" relations with the player set,
				#but they can decay before ever meeting him, so keep them until the first meeting.
				(this_or_next|neq, ":troop_no", "trp_player"),
				(troop_slot_ge, ":troop_no", slot_troop_met, 1),

				(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":active_npc"),
				(lt, reg0, 0),
				(store_sub, ":chance_of_convergence", 0, reg0),
				(store_random_in_range, ":random", 0, 300),
				(lt, ":random", ":chance_of_convergence"),
				(call_script, "script_troop_change_relation_with_troop", ":troop_no", ":active_npc", 1),
				(val_add, "$total_relation_changes_through_convergence", 1),
			(try_end),

			#Accelerate forgiveness for lords in exile (with their original faction only)
			(neq, ":troop_no", "trp_player"),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_exile),
			(troop_get_slot, ":original_faction", ":troop_no", slot_troop_original_faction),
			(gt, ":original_faction", 0),

			(try_for_range, ":active_npc", heroes_begin, heroes_end),
				(neq, ":active_npc", ":troop_no"),
				(neg|troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_lady),#Don't do for ladies
				(neg|troop_slot_eq, ":active_npc", slot_troop_occupation, dplmc_slto_dead),#Don't do for the dead
				#Only apply to heroes with the same original faction
				(troop_slot_eq, ":active_npc", slot_troop_original_faction, ":original_faction"),
				(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":active_npc"),
				(lt, reg0, 0),
				(store_sub, ":chance_of_convergence", 0, reg0),
				(store_random_in_range, ":random", 0, 300),
				(lt, ":random", ":chance_of_convergence"),
				(call_script, "script_troop_change_relation_with_troop", ":troop_no", ":active_npc", 1),
				(val_add, "$total_relation_changes_through_convergence", 1),
			(try_end),
		(try_end),
	#Finish loop over the ":iteration" variable.
	(try_end),
	(assign, reg0, ":save_reg0"),
	##diplomacy end+
   ]),

#TEMPORARILY DISABLED, AS READINESS IS NOW A PRODUCT OF NPC_DECISION_CHECKLIST
  # Changing readiness to join army
#   (10,
 #   [
 #     (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
#		(eq, 1, 0),
#	    (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
#        (assign, ":modifier", 1),
#        (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
#        (try_begin),
#          (gt, ":party_no", 0),
#          (party_get_slot, ":commander_party", ":party_no", slot_party_commander_party),
#          (ge, ":commander_party", 0),
#          (store_faction_of_party, ":faction_no", ":party_no"),
#          (faction_get_slot, ":faction_marshall", ":faction_no", slot_faction_marshall),
#          (ge, ":faction_marshall", 0),
#          (troop_get_slot, ":marshall_party", ":faction_marshall", slot_troop_leaded_party),
#          (eq, ":commander_party", ":marshall_party"),
#          (assign, ":modifier", -1),
#        (try_end),
#        (troop_get_slot, ":readiness", ":troop_no", slot_troop_readiness_to_join_army),
#        (val_add, ":readiness", ":modifier"),
#        (val_clamp, ":readiness", 0, 100),
#        (troop_set_slot, ":troop_no", slot_troop_readiness_to_join_army, ":readiness"),
#        (assign, ":modifier", 1),
#        (try_begin),
#          (gt, ":party_no", 0),
#          (store_troop_faction, ":troop_faction", ":troop_no"),
#          (eq, ":troop_faction", "fac_player_supporters_faction"),
#          (neg|troop_slot_eq, ":troop_no", slot_troop_player_order_state, spai_undefined),
#          (party_get_slot, ":party_ai_state", ":party_no", slot_party_ai_state),
#          (party_get_slot, ":party_ai_object", ":party_no", slot_party_ai_object),
#          #Check if party is following player orders
#          (try_begin),
#            (troop_slot_eq, ":troop_no", slot_troop_player_order_state, ":party_ai_state"),
#            (troop_slot_eq, ":troop_no", slot_troop_player_order_object, ":party_ai_object"),
#            (assign, ":modifier", -1),
#          (else_try),
#            #Leaving following player orders if the current party order is not the same.
#            (troop_set_slot, ":troop_no", slot_troop_player_order_state, spai_undefined),
#            (troop_set_slot, ":troop_no", slot_troop_player_order_object, -1),
#          (try_end),
#        (try_end),
#        (troop_get_slot, ":readiness", ":troop_no", slot_troop_readiness_to_follow_orders),
#        (val_add, ":readiness", ":modifier"),
#        (val_clamp, ":readiness", 0, 100),
#        (troop_set_slot, ":troop_no", slot_troop_readiness_to_follow_orders, ":readiness"),
#        (try_begin),
#          (lt, ":readiness", 10),
#          (troop_set_slot, ":troop_no", slot_troop_player_order_state, spai_undefined),
#          (troop_set_slot, ":troop_no", slot_troop_player_order_object, -1),
#        (try_end),
#      (try_end),
 #     ]),

  # Process vassal ai
   (2,
   [
     #(call_script, "script_process_kingdom_parties_ai"), #moved to below trigger (per 1 hour) in order to allow it processed more frequent.
   ]),

  # Process alarms - perhaps break this down into several groups, with a modula
   (1, #this now calls 1/3 of all centers each time, thus hopefully lightening the CPU load
   [
     (call_script, "script_process_alarms"),

     (call_script, "script_allow_vassals_to_join_indoor_battle"),

     (call_script, "script_process_kingdom_parties_ai"),
   ]),

  # Process siege ai
   (3,
   [
      ##diplomacy start+
	  (assign, ":save_reg0", reg0),#Save registers
	  (assign, ":save_reg1", reg1),
	  ##diplomacy end+
      (store_current_hours, ":cur_hours"),
      (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
        (party_get_slot, ":besieger_party", ":center_no", slot_center_is_besieged_by),
        (gt, ":besieger_party", 0),
        (party_is_active, ":besieger_party"),
        (store_faction_of_party, ":besieger_faction", ":besieger_party"),
        (party_slot_ge, ":center_no", slot_center_is_besieged_by, 1),
        (party_get_slot, ":siege_begin_hours", ":center_no", slot_center_siege_begin_hours),
        (store_sub, ":siege_begin_hours", ":cur_hours", ":siege_begin_hours"),
        (assign, ":launch_attack", 0),
        (assign, ":call_attack_back", 0),
        (assign, ":attacker_strength", 0),
        (assign, ":marshall_attacking", 0),
        (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
          (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
          (gt, ":party_no", 0),
          (party_is_active, ":party_no"),

          (store_troop_faction, ":troop_faction_no", ":troop_no"),
          (eq, ":troop_faction_no", ":besieger_faction"),
          (assign, ":continue", 0),
          (try_begin),
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
            (party_slot_eq, ":party_no", slot_party_ai_object, ":center_no"),
            (assign, ":continue", 1),
          (else_try),
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
            (party_get_slot, ":commander_party", ":party_no", slot_party_ai_object),
            (gt, ":commander_party", 0),
            (party_is_active, ":commander_party"),
            (party_slot_eq, ":commander_party", slot_party_ai_state, spai_besieging_center),
            (party_slot_eq, ":commander_party", slot_party_ai_object, ":center_no"),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
          (party_get_battle_opponent, ":opponent", ":party_no"),
          (this_or_next|lt, ":opponent", 0),
          (eq, ":opponent", ":center_no"),
          (try_begin),
            (faction_slot_eq, ":besieger_faction", slot_faction_marshall, ":troop_no"),
            (assign, ":marshall_attacking", 1),
          (try_end),
          (call_script, "script_party_calculate_regular_strength", ":party_no"),
		  ##diplomacy start+ terrain advantage
		  (try_begin),
			(ge, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
			(call_script, "script_dplmc_party_calculate_strength_in_terrain", ":party_no", dplmc_terrain_code_siege, 0, 0),
          (try_end),
		  ##diplomacy end+
          (val_add, ":attacker_strength", reg0),
        (try_end),
        (try_begin),
          (gt, ":attacker_strength", 0),
          (party_collect_attachments_to_party, ":center_no", "p_collective_enemy"),
          (call_script, "script_party_calculate_regular_strength", "p_collective_enemy"),
		  ##diplomacy start+ terrain advantage
		  (try_begin),
			(ge, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
			(call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_collective_enemy", dplmc_terrain_code_siege, 0, 0),
          (try_end),
		  ##diplomacy end+
          (assign, ":defender_strength", reg0),
          (try_begin),
            (eq, "$auto_enter_town", ":center_no"),
            (eq, "$g_player_is_captive", 0),
            (call_script, "script_party_calculate_regular_strength", "p_main_party"),
			##diplomacy start+ terrain advantage
			(try_begin),
				(ge, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
				(call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_collective_enemy", dplmc_terrain_code_siege, 0, 0),
			(try_end),
			##diplomacy end+
            (val_add, ":defender_strength", reg0),
            (val_mul, ":attacker_strength", 2), #double the power of attackers if the player is in the campaign
          (try_end),
          (party_get_slot, ":siege_hardness", ":center_no", slot_center_siege_hardness),
          (val_add, ":siege_hardness", 100),
          (val_mul, ":defender_strength", ":siege_hardness"),
          (val_div, ":defender_strength", 100),
          (val_max, ":defender_strength", 1),
          (try_begin),
            (eq, ":marshall_attacking", 1),
            (eq, ":besieger_faction", "$players_kingdom"),
            (check_quest_active, "qst_follow_army"),
            (val_mul, ":attacker_strength", 2), #double the power of attackers if the player is in the campaign
          (try_end),
          (store_mul, ":strength_ratio", ":attacker_strength", 100),
          (val_div, ":strength_ratio", ":defender_strength"),
          (store_sub, ":random_up_limit", ":strength_ratio", 250), #was 300 (1.126)

          (try_begin),
            (gt, ":random_up_limit", -100), #never attack if the strength ratio is less than 150%
            (store_div, ":siege_begin_hours_effect", ":siege_begin_hours", 2), #was 3 (1.126)
            (val_add, ":random_up_limit", ":siege_begin_hours_effect"),
          (try_end),

          (val_div, ":random_up_limit", 5),
          (val_max, ":random_up_limit", 0),
          (store_sub, ":random_down_limit", 175, ":strength_ratio"), #was 200 (1.126)
          (val_max, ":random_down_limit", 0),
          (try_begin),
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", ":random_up_limit"),
            (gt, ":siege_begin_hours", 24),#initial preparation
            (assign, ":launch_attack", 1),
          (else_try),
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", ":random_down_limit"),
            (assign, ":call_attack_back", 1),
          (try_end),
        (else_try),
          (assign, ":call_attack_back", 1),
        (try_end),

        #Assault the fortress
        (try_begin),
          (eq, ":launch_attack", 1),
          (call_script, "script_begin_assault_on_center", ":center_no"),
        (else_try),
          (eq, ":call_attack_back", 1),
          (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
            (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
            (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
            (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
            (gt, ":party_no", 0),
            (party_is_active, ":party_no"),

            (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
            (party_slot_eq, ":party_no", slot_party_ai_object, ":center_no"),
            (party_slot_eq, ":party_no", slot_party_ai_substate, 1),
            (call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
            (call_script, "script_party_set_ai_state", ":party_no", spai_besieging_center, ":center_no"),
            #resetting siege begin time if at least 1 party retreats
            (party_set_slot, ":center_no", slot_center_siege_begin_hours, ":cur_hours"),
          (try_end),
        (try_end),
      (try_end),
	  ##diplomacy start+
	  #Revert registers
	  (assign, reg0, ":save_reg0"),
	  (assign, reg1, ":save_reg1"),
	  ##diplomacy end+
    ]),

    # Decide faction ais
    (6, #it was 23
    [
      (assign, "$g_recalculate_ais", 1),
    ]),
]
