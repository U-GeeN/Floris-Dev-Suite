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



simple_triggers_part4 = [

   
  (24,
    [
      (try_for_parties, ":party_no"),
        (neq, ":party_no", "p_main_party"),
        (neq, ":party_no", "p_temp_party"),
        (assign, ":continue", 0),
        (try_begin),
          (this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
          (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_caravan),
          (party_is_active, ":party_no"),
          (assign, ":continue", 1),
          (try_begin),
            (party_stack_get_troop_id, ":cur_troop", ":party_no", 0),
            (this_or_next|troop_is_hero, ":cur_troop"),
            (eq, ":cur_troop", "trp_caravan_master"),
            (assign, ":first_stack", 1),
          (else_try),
            (assign, ":first_stack", 0),
          (try_end),
        (else_try),
          (this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_castle),
          (party_slot_eq, ":party_no", slot_party_type, spt_town),
          (neg|party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
          (assign, ":first_stack", 0),
          (assign, ":continue", 1),
        (try_end),
        (eq, ":continue", 1),
        (call_script, "script_sort_party_by_troop_level", ":party_no", ":first_stack"),
      (try_end),
    ]),
   
   (24,
     [
       (try_for_range, ":cur_village", villages_begin, villages_end),
         (party_get_slot, ":cur_bound_center", ":cur_village", slot_village_bound_center),
         (store_faction_of_party, ":village_faction", ":cur_village"),
         (store_faction_of_party, ":town_faction", ":cur_bound_center"),
         (neq,  ":village_faction", ":town_faction"),
         (call_script, "script_give_center_to_faction", ":cur_village", ":town_faction"),
       (try_end),
     ]),
## CC 1.322
  (24,
    [
      #(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
        #(try_begin),
          #(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          #(call_script, "script_get_troop_backup_hp_times_factor", ":troop_no"),
          #(assign, ":hp_times_factor", reg0),
          #(call_script, "script_get_troop_max_hp", ":troop_no"),
          #(assign, ":max_hp", reg0),
          #(store_mul, ":max_backup_hp", ":max_hp", ":hp_times_factor"),
          #(val_div, ":max_backup_hp", 100),
          #(troop_get_slot, ":backup_hp", ":troop_no", slot_troop_backup_hp),
          #(store_character_level, ":troop_level", ":troop_no"),
          #(store_div, ":refill_speed", ":troop_level", 10),
          #(val_add, ":backup_hp", ":refill_speed"),
          ## refill hp if needed
          #(store_troop_health, ":troop_hp", ":troop_no", 1),
          #(call_script, "script_get_troop_max_hp", ":troop_no"),
          #(assign, ":max_hp", reg0),
          #(store_sub, ":lost_hp", ":max_hp", ":troop_hp"),
          #(val_min, ":lost_hp", ":backup_hp"),
          #(val_add, ":troop_hp", ":lost_hp"),
          #(troop_set_health, ":troop_no", ":troop_hp", 1),
          #(val_sub, ":backup_hp", ":lost_hp"),
          ## set backup_hp
          #(val_min, ":backup_hp", ":max_backup_hp"),
          #(troop_set_slot, ":troop_no", slot_troop_backup_hp, ":backup_hp"),
        #(else_try),
          #(troop_set_slot, ":troop_no", slot_troop_backup_hp, 0),
        #(try_end),
      #(try_end),
    ]),
##
   
   (12,
     [
       (try_for_range, ":troop_no", original_kingdom_heroes_begin, active_npcs_end),
         (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
         (ge, ":party_no", 1),
         (call_script, "script_process_ransom_for_party", ":party_no"),
         (assign, ":total_ransom_cost", reg0),
         (troop_get_slot, ":cur_wealth", ":troop_no", slot_troop_wealth),
         (val_add, ":cur_wealth", ":total_ransom_cost"),
         (troop_set_slot, ":troop_no", slot_troop_wealth, ":cur_wealth"),
         (call_script, "script_process_outlaws_for_party", ":party_no"),
         (call_script, "script_update_troop_notes", ":troop_no"),
       (try_end),
       
       #  walled centers
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
         (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
         (neq, ":town_lord", "trp_player"), #center does not belong to player.
#         (ge, ":town_lord", 1), #center belongs to someone. ##CC 1.324
         (neg|is_between, ":town_lord", companions_begin, companions_end), # not companions
         (call_script, "script_process_ransom_for_party", ":center_no"),
         (assign, ":total_ransom_cost", reg0),
         (party_get_slot, ":cur_wealth", ":center_no", slot_town_wealth),
         (val_add, ":cur_wealth", ":total_ransom_cost"),
         (party_set_slot, ":center_no", slot_town_wealth, ":cur_wealth"),
         ## recruit after processing ransom
         (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
         (assign, ":reinforcement_cost", reinforcement_cost_moderate),
         (try_begin), 
           (eq, ":reduce_campaign_ai", 0),
           (assign, ":reinforcement_cost", reinforcement_cost_hard),
         (else_try), 
           (eq, ":reduce_campaign_ai", 1),
           (assign, ":reinforcement_cost", reinforcement_cost_moderate),
         (else_try), 
           (eq, ":reduce_campaign_ai", 2),
           (assign, ":reinforcement_cost", reinforcement_cost_easy),
         (try_end),
         (store_div, ":num_hiring_rounds", ":total_ransom_cost", 2), # one half
         (val_div, ":num_hiring_rounds", ":reinforcement_cost"),
         (try_begin), 
           (gt, ":num_hiring_rounds", 0),
           (try_for_range, ":unused", 0, ":num_hiring_rounds"), 
             (party_get_slot, ":cur_wealth", ":center_no", slot_town_wealth),
             (assign, ":hiring_budget", ":cur_wealth"),
             (val_div, ":hiring_budget", 2),
             (gt, ":hiring_budget", ":reinforcement_cost"),       
             (call_script, "script_cf_reinforce_party", ":center_no"),       
             (val_sub, ":cur_wealth", ":reinforcement_cost"),
             (party_set_slot, ":center_no", slot_town_wealth, ":cur_wealth"),
           (try_end),
           (store_mul, ":xp_gain", ":num_hiring_rounds", 1000), ##CC 1.324
           (party_upgrade_with_xp, ":center_no", ":xp_gain"),
         (try_end),
         (call_script, "script_process_outlaws_for_party", ":center_no"),
       (try_end),
     ]),
   
   (1,
     [
       (party_get_morale, ":cur_morale", "p_main_party"),
       (try_begin),
         (lt, ":cur_morale", "$g_morale_threshold"),
         (assign, "$g_twice_consum_food", 1),
       (else_try),
         (assign, "$g_twice_consum_food", 0),
       (try_end),
     ]),
   
  (3,
   [
      (try_for_parties, ":party_no"),
        (party_get_slot, ":party_type", ":party_no", slot_party_type),
        (try_begin),
          (this_or_next|eq, ":party_type", spt_town),
          (eq, ":party_type", spt_castle),
          (party_get_slot, ":town_lord", ":party_no", slot_town_lord),
          (assign, ":root_troop", ":town_lord"),
        (else_try),
          (eq, ":party_type", spt_kingdom_hero_party),
          (party_stack_get_troop_id, ":party_leader", ":party_no", 0),
          (assign, ":root_troop", ":party_leader"),
        (else_try),
          (party_stack_get_troop_id, ":party_leader", ":party_no", 0),
          (assign, ":root_troop", ":party_leader"),
        (try_end),
        
        (gt, ":root_troop", 0),
        (neg|is_between, ":root_troop", companions_begin, companions_end),
        (try_begin),
          (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
          (troop_get_slot, ":party_faction", ":root_troop", slot_troop_original_faction),
        (else_try),
          (store_troop_faction, ":party_faction", ":root_troop"),
        (try_end),
##Floris: Updated from CC 1.321.
        (store_troop_faction, ":party_cur_faction", ":root_troop"),
        
        # combine same troops from prisoners
        (call_script, "script_combine_same_troops_from_prisoners", ":party_no"),
##

        (party_get_num_prisoner_stacks, ":num_prisoner_stacks", ":party_no"),
        (try_for_range_backwards, ":cur_prisoner_stack", 0, ":num_prisoner_stacks"),
          (party_prisoner_stack_get_troop_id, ":cur_prisoner_id", ":party_no", ":cur_prisoner_stack"),
          (gt, ":cur_prisoner_id", -1),
          (neg|troop_is_hero, ":cur_prisoner_id"),
          (store_troop_faction, ":troop_faction", ":cur_prisoner_id"),
          (assign, ":continue", 0),
          (try_begin),
##Floris: Updated from CC 1.321.
            (this_or_next|eq, ":troop_faction", ":party_faction"),
            (eq, ":troop_faction", ":party_cur_faction"),
##
            (assign, ":continue", 1),
          (else_try),
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
			   (is_between, ":cur_prisoner_id", ":outlaws_begin", ":outlaws_end"), ## changed from outlaws_troops_begin to outlaws_troops_end
			   ##Floris MTT end
            (troop_get_slot, ":original_faction", ":cur_prisoner_id", slot_troop_original_faction),
            (eq, ":original_faction", ":party_faction"),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
          (party_get_num_companion_stacks, ":num_companion_stacks", ":party_no"),
          (assign, ":continue_2", 0),
          (try_begin),
            (lt, ":num_companion_stacks", 32),
            (assign, ":continue_2", 1),
          (else_try),
            #(eq, ":num_companion_stacks", 32),
            (try_for_range, ":cur_companion_stack", 0, ":num_companion_stacks"),
              (party_stack_get_troop_id, ":cur_companion_id", ":party_no", ":cur_companion_stack"),
              (eq, ":cur_companion_id", ":cur_prisoner_id"),
              (assign, ":continue_2", 1),
              (assign, ":num_companion_stacks", 0), # end the loop
            (try_end),
          (try_end),
          (eq, ":continue_2", 1),
          (party_prisoner_stack_get_size, ":prisoner_size", ":party_no", ":cur_prisoner_stack"),
          (party_remove_prisoners,":party_no",":cur_prisoner_id", ":prisoner_size"),
          (try_begin),
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
		   (is_between, ":cur_prisoner_id", ":outlaws_begin", ":outlaws_end"), ## changed from outlaws_troops_begin to outlaws_troops_end
		   ##Floris MTT end
            (store_random_in_range, ":random_no", 0, 2),
            (troop_get_upgrade_troop, ":upgrade_troop_no", ":cur_prisoner_id", ":random_no"),
            (try_begin),
              (le, ":upgrade_troop_no", 0),
              (troop_get_upgrade_troop, ":upgrade_troop_no", ":cur_prisoner_id", 0),
            (try_end),
            (party_add_members, ":party_no", ":upgrade_troop_no", ":prisoner_size"),
          (else_try),
            (party_add_members, ":party_no", ":cur_prisoner_id", ":prisoner_size"),
          (try_end),
        (try_end),
      (try_end),
   ]),
   
  (3,	#Removes Prisoners from bandit parties // Adds bandits to party
   [
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
   ##Floris MTT end
    (try_for_parties, ":party_no"),
      (party_get_template_id, ":party_template", ":party_no"),
      (is_between, ":party_template", ":templates_begin", ":templates_end"), ##Floris MTT begin and end; changed from bandit_party_template_begin to bandit_party_template_end ## CC
		##Floris MTT begin
		(try_begin),
		 	(eq, "$troop_trees", troop_trees_0),
			(store_sub, ":original_faction", ":party_template", "pt_forest_bandits"),
		(else_try),
		 	(eq, "$troop_trees", troop_trees_1),
			(store_sub, ":original_faction", ":party_template", "pt_forest_bandits_r"),
		(else_try),
			(eq, "$troop_trees", troop_trees_2),
			(store_sub, ":original_faction", ":party_template", "pt_forest_bandits_e"),
		(try_end),
		##Floris MTT end
      (val_add, ":original_faction", "fac_kingdom_1"),
      ## prisoners
      (party_get_num_prisoner_stacks, ":num_prisoner_stacks", ":party_no"),
      (try_for_range_backwards, ":cur_prisoner_stack", 0, ":num_prisoner_stacks"),
        (party_prisoner_stack_get_troop_id, ":cur_prisoner_id", ":party_no", ":cur_prisoner_stack"),
        (gt, ":cur_prisoner_id", -1),
        (neg|troop_is_hero, ":cur_prisoner_id"),
        (store_troop_faction, ":troop_faction", ":cur_prisoner_id"),
        (this_or_next|eq, ":troop_faction", "fac_outlaws"),
        (eq, ":troop_faction", ":original_faction"),
        (party_prisoner_stack_get_size, ":prisoner_size", ":party_no", ":cur_prisoner_stack"),
        (party_remove_prisoners,":party_no",":cur_prisoner_id", ":prisoner_size"),
        (try_begin),
          (eq, ":troop_faction", "fac_outlaws"),
          (party_add_members, ":party_no", ":cur_prisoner_id", ":prisoner_size"),
        (else_try),
          (store_sub, ":outlaws_troop", ":troop_faction", "fac_kingdom_1"),
			##Floris MTT begin
			(troop_get_slot,":bandit_forest","$troop_trees",slot_bandit_forest),
			(val_add, ":outlaws_troop", ":bandit_forest"),
			##Floris MTT end
          (party_add_members, ":party_no", ":outlaws_troop", ":prisoner_size"),
        (try_end),
      (try_end),
      ## companions
      (party_get_num_companion_stacks, ":num_companion_stacks", ":party_no"),
      (try_for_range_backwards, ":cur_stack", 0, ":num_companion_stacks"),
        (party_stack_get_troop_id, ":cur_troop", ":party_no", ":cur_stack"),
        (gt, ":cur_troop", -1),
        (neg|troop_is_hero, ":cur_troop"),
        (store_troop_faction, ":troop_faction", ":cur_troop"),
        (eq, ":troop_faction", ":original_faction"),
        (party_stack_get_size, ":stack_size", ":party_no", ":cur_stack"),
        (party_stack_get_num_wounded, ":num_wounded", ":party_no", ":cur_stack"),
        (party_remove_members,":party_no", ":cur_troop", ":stack_size"),
        (store_sub, ":outlaws_troop", ":troop_faction", "fac_kingdom_1"),
		##Floris MTT begin
		(troop_get_slot,":bandit_forest","$troop_trees",slot_bandit_forest),
		(val_add, ":outlaws_troop", ":bandit_forest"),
		##Floris MTT end
        (party_add_members, ":party_no", ":outlaws_troop", ":stack_size"),
        (party_wound_members, ":party_no", ":outlaws_troop", ":num_wounded"),
      (try_end),
    (try_end),
   ]),
   
  (24,
    [
      (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
        (party_slot_eq, ":center_no", slot_town_lord, "trp_player"), #center belongs to player.
        (party_slot_eq, ":center_no", slot_center_is_besieged_by, -1), #center not under siege
        (party_slot_ge, ":center_no", slot_town_recruit_gold, reinforcement_cost_player),
        (call_script, "script_get_town_faction_for_recruiting", ":center_no"),
        (assign, ":party_faction", reg0),
        (faction_get_slot, ":party_template_a", ":party_faction", slot_faction_reinforcements_a),
        (faction_get_slot, ":party_template_b", ":party_faction", slot_faction_reinforcements_b),
        (faction_get_slot, ":party_template_c", ":party_faction", slot_faction_reinforcements_c),
        (faction_get_slot, ":party_template_d", ":party_faction", slot_faction_reinforcements_d),
        (faction_get_slot, ":party_template_e", ":party_faction", slot_faction_reinforcements_e),
        (faction_get_slot, ":party_template_f", ":party_faction", slot_faction_reinforcements_f),
        
        (party_get_slot, ":party_type",":center_no", slot_party_type),
        (assign, ":party_template", 0),
        (store_random_in_range, ":rand", 0, 100),
		(try_begin), #CABA #Floris 2.52 addition for barracks (Training Yard)
			(party_slot_ge, ":center_no", slot_center_has_barracks, 1),
			(val_sub, ":rand", 15), #bump up recruit quality
		(try_end), #CABA #Floris 2.52 addition for barracks (Training Yard)
        (try_begin),
          (eq, ":party_type", spt_castle),  #CASTLE
          (try_begin),
            (lt, ":rand", 50),
            (assign, ":party_template", ":party_template_e"),
          (else_try),
            (lt, ":rand", 65), #CABA #Floris 2.5 was 75, duplicating the next one
            (assign, ":party_template", ":party_template_d"),
          (else_try),
            (lt, ":rand", 80), #CABA #Floris 2.5 was 75
            (assign, ":party_template", ":party_template_c"),
          (else_try),
            (assign, ":party_template", ":party_template_a"),
          (try_end),
        (else_try),
          (eq, ":party_type", spt_town),  #TOWN
          (try_begin),
            (lt, ":rand", 20),
            (assign, ":party_template", ":party_template_f"),
          (else_try),
            (lt, ":rand", 40), #CABA #Floris 2.5 was 60
            (assign, ":party_template", ":party_template_e"),
          (else_try),
            (lt, ":rand", 60), #CABA #Floris 2.5 was 80, duplicating the next one
            (assign, ":party_template", ":party_template_d"),
          (else_try),
            (lt, ":rand", 80),
            (assign, ":party_template", ":party_template_c"),
          (else_try),
            (assign, ":party_template", ":party_template_b"),
          (try_end),
        (try_end),
  
        (try_begin),
          (gt, ":party_template", 0),
          (party_add_template, ":center_no", ":party_template"),
        (try_end),
        (party_get_slot, ":recruit_gold", ":center_no", slot_town_recruit_gold),
        (val_sub, ":recruit_gold", reinforcement_cost_player),
        (party_set_slot, ":center_no", slot_town_recruit_gold, ":recruit_gold"),
      (try_end),
    ]),

  (24*15, 
   [
	 ## WINDYPLAINS+ ## - MOD OPTION: Direct block to prevent Bandit Heroes.
	 (eq, "$enable_bandit_heroes", 1),
	 ## WINDYPLAINS- ##
	 (call_script, "script_centers_init_bandit_leader_quest"),
	 ##Floris MTT begin
	 (try_begin),
		(eq, "$troop_trees", troop_trees_0),
        (assign, ":steppe_bandits", "pt_steppe_bandits"),
        (assign, ":desert_bandits", "pt_desert_bandits"),
		(assign, ":templates_begin", bandit_party_template_begin),
		(assign, ":templates_end", bandit_party_template_end),
	 (else_try),
		(eq, "$troop_trees", troop_trees_1),
        (assign, ":steppe_bandits", "pt_steppe_bandits_r"),
        (assign, ":desert_bandits", "pt_desert_bandits_r"),
		(assign, ":templates_begin", bandit_party_template_r_begin),
		(assign, ":templates_end", bandit_party_template_r_end),
	 (else_try),
		(eq, "$troop_trees", troop_trees_2),
        (assign, ":steppe_bandits", "pt_steppe_bandits_e"),
        (assign, ":desert_bandits", "pt_desert_bandits_e"),
		(assign, ":templates_begin", bandit_party_template_e_begin),
		(assign, ":templates_end", bandit_party_template_e_end),
	 (try_end),
     (try_for_range, ":pt_no", ":templates_begin", ":templates_end"), #changed from bandit_party_template_begin to bandit_party_template_end
	 ##Floris MTT end	 
       (party_template_set_slot, ":pt_no", slot_party_template_has_hero, 0),
       (try_for_parties, ":party_no"),
         (party_get_template_id, ":party_template", ":party_no"),
         (eq, ":party_template", ":pt_no"),
         (party_stack_get_troop_id, ":leader", ":party_no", 0),
         (troop_is_hero, ":leader"),
         (party_template_set_slot, ":pt_no", slot_party_template_has_hero, 1),
       (try_end),
       (party_template_slot_eq, ":pt_no", slot_party_template_has_hero, 0),
       
       (party_template_get_slot, ":spawn_point", ":pt_no", slot_party_template_spawn_point),
       (party_template_get_slot, ":hero_id", ":pt_no", slot_party_template_hero_id),
       (party_template_get_slot, ":hero_name_begin", ":pt_no", slot_party_template_hero_name_begin),
       ## compare level 
       (store_character_level, ":player_level", "trp_player"),
       (store_character_level, ":hero_level", ":hero_id"),
       (try_begin),
	     ##Floris MTT begin
         (this_or_next|eq, ":pt_no", ":steppe_bandits"),
		 (eq, ":pt_no", ":desert_bandits"),
		 ##Floris MTT end	
         (val_mul, ":hero_level", 3),
         (val_div, ":hero_level", 2),
       (try_end),
       (val_div, ":hero_level", 2),
       (ge, ":player_level", ":hero_level"),
       
       (set_spawn_radius, 25),
       (spawn_around_party, ":spawn_point", ":pt_no"),
       (assign, ":new_party", reg0),
       (party_add_template, ":new_party", ":pt_no"),
       (party_add_template, ":new_party", ":pt_no"),
       ## new name for hero
       (assign, ":end_cond", 1),
       (try_for_range, ":unused", 0, ":end_cond"),
         (store_random_in_range, ":new_name", 0, 5),
         (val_add, ":new_name", ":hero_name_begin"),
         (party_template_get_slot, ":pre_name", ":pt_no", slot_party_template_hero_pre_name),
         (party_template_get_slot, ":pre_pre_name", ":pt_no", slot_party_template_hero_pre_pre_name),
         (neq, ":new_name", ":pre_name"),
         (neq, ":new_name", ":pre_pre_name"),
         (troop_set_name, ":hero_id", ":new_name"),
         (party_template_set_slot, ":pt_no", slot_party_template_hero_pre_name, ":new_name"),
         (party_template_set_slot, ":pt_no", slot_party_template_hero_pre_pre_name, ":pre_name"),
         (assign, ":end_cond", 0),
       (else_try),
         (val_add, ":end_cond", 1),
       (try_end),
        
       (party_add_leader, ":new_party", ":hero_id"),
       (str_store_troop_name, s5, ":hero_id"),
       (party_set_name, ":new_party", "str_s5_s_party"),
       (store_sub, ":cur_banner", ":hero_id", bandit_heroes_begin),
       (val_add, ":cur_banner", "icon_map_flag_bandit_f"),
       (party_set_banner_icon, ":new_party", ":cur_banner"), ## BUG - invalid map icon id
       (party_template_set_slot, ":pt_no", slot_party_template_has_hero, 1),
       (party_template_set_slot, ":pt_no", slot_party_template_hero_party_id, ":new_party"),
     (try_end),
   ]),
  
  (3, 
    [
		## WINDYPLAINS+ ## - MOD OPTION: Direct block to prevent Bandit Heroes.
		(eq, "$enable_bandit_heroes", 1),
		## WINDYPLAINS- ##
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
      (try_for_range, ":pt_no", ":templates_begin", ":templates_end"), ##Floris MTT begin and end; changed from bandit_party_template_begin to bandit_party_template_end ## CC
	   	##Floris MTT end    
        (party_template_set_slot, ":pt_no", slot_party_template_has_hero, 0), ##BUG
        (try_for_parties, ":party_no"),
		  (party_template_slot_eq, ":pt_no", slot_party_template_has_hero, 0), ##BUG
          (party_get_template_id, ":party_template", ":party_no"), 
          (eq, ":party_template", ":pt_no"),
          (party_stack_get_troop_id, ":leader", ":party_no", 0),
          (troop_is_hero, ":leader"),
          (party_template_set_slot, ":pt_no", slot_party_template_has_hero, 1),
        (try_end),
        (party_template_slot_eq, ":pt_no", slot_party_template_has_hero, 1), ##BUG
        (party_template_get_slot, ":hero_party", ":pt_no", slot_party_template_hero_party_id),
        (party_is_active, ":hero_party"),
		(assign, ":escort_counter", 0), ##Floris 2.5b2 addon
        (try_for_parties, ":party_no"),
          (party_get_template_id, ":party_template", ":party_no"),
          (eq, ":party_template", ":pt_no"),
          (party_stack_get_troop_id, ":leader", ":party_no", 0),
          (neg|troop_is_hero, ":leader"),
		  (assign, ":continue", 1),##Floris 2.5b2 addon - start
		  (try_begin),
			(get_party_ai_behavior, ":bhvr",":party_no"),
			(eq, ":bhvr", ai_bhvr_escort_party),
			(val_add, ":escort_counter", 1),
			(assign, ":continue", 0),
		  (try_end),
		  (eq, ":continue", 1),
		  ## WINDYPLAINS+ ## - Put in option scaled limit to bandit hero parties.
		  (lt, ":escort_counter", "$bandit_hero_limiter"),
		  # (lt, ":escort_counter", 8),
		  ## WINDYPLAINS- ##
		  (val_add, ":escort_counter", 1), ##Floris 2.5b2 addon - end
          #(store_distance_to_party_from_party, ":distance", ":party_no", ":hero_party"),
          #(le, ":distance", 30),
          (party_set_ai_behavior, ":party_no", ai_bhvr_escort_party),
          (party_set_ai_object, ":party_no", ":hero_party"),
        (try_end),
      (try_end),
    ]),

  
  (24,
    [
      (party_get_num_prisoners, ":num_prisoners", "p_main_party"),
      (call_script, "script_game_get_party_prisoner_limit"),
      (assign, ":limit", reg0),
      (gt, ":num_prisoners", ":limit"),
      (store_mul, ":escape_prob", ":num_prisoners", 10),
	  (val_max, ":limit", 1), # Floris+ Bugfix to prevent Div/0 errors when combined with +prison management troops, gaining a prisoner and then losing your stat bonus.
      (val_div, ":escape_prob", ":limit"),
      (val_min, ":escape_prob", 50),
      
      (assign, ":kinds_of_escape_troop", 0),
      (assign, ":num_of_escaped", 0),
      (party_get_num_prisoner_stacks, ":num_prisoner_stacks", "p_main_party"),
      (try_for_range_backwards, ":stack_no", 0, ":num_prisoner_stacks"),
        (party_prisoner_stack_get_troop_id, ":stack_troop","p_main_party",":stack_no"),
        (neg|troop_is_hero, ":stack_troop"),
        (party_prisoner_stack_get_size, ":stack_size","p_main_party",":stack_no"),
        (assign, ":num_removed", 0),
        (try_for_range, ":unused", 0, ":stack_size"),
          (store_random_in_range, ":rand_no", 0, 100),
          (lt, ":rand_no", ":escape_prob"),
          (val_add, ":num_removed", 1),
        (try_end),
        (gt, ":num_removed", 0),
        (party_remove_prisoners, "p_main_party", ":stack_troop", ":num_removed"),
        (val_add, ":kinds_of_escape_troop", 1),
        (val_add, ":num_of_escaped", ":num_removed"),
        (try_begin),
          (eq, ":kinds_of_escape_troop", 1),
          (str_store_troop_name_by_count, s1, ":stack_troop", ":num_removed"),
          (assign, reg1, ":num_removed"),
          (str_store_string, s0, "@{reg1} {s1}"),
        (else_try),
          (eq, ":kinds_of_escape_troop", 2),
          (str_store_troop_name_by_count, s1, ":stack_troop", ":num_removed"),
          (assign, reg1, ":num_removed"),
          (str_store_string, s0, "@{reg1} {s1} and {s0}"),
        (else_try),
          (ge, ":kinds_of_escape_troop", 3),
          (str_store_troop_name_by_count, s1, ":stack_troop", ":num_removed"),
          (assign, reg1, ":num_removed"),
          (str_store_string, s0, "@{reg1} {s1}, {s0}"),
        (try_end),
      (try_end),
      (try_begin),
        (ge, ":kinds_of_escape_troop", 1),
        (try_begin),
          (eq, ":num_of_escaped", 1),
          (str_store_string, s0, "@{s0} has escaped."),
        (else_try),
          (str_store_string, s0, "@{s0} hava escaped."),
        (try_end),
        (str_store_string, s0, "@Number of prisoners exceeds prisoner management limit. {s0}"),
        (tutorial_box, s0, "str_weekly_report"),
      (try_end),
    ]
  ),
  
  (24,
    [
      (try_for_range, ":cur_faction", npc_kingdoms_begin, npc_kingdoms_end),
        (neg|faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
        (troop_get_slot, ":pretender_original_faction", "$supported_pretender",  slot_troop_original_faction),
        (neq, ":pretender_original_faction", ":cur_faction"),
        
        (assign, ":fitful_faction", -1),
        (assign, ":fitful_lords", 0),
        (try_for_range, ":faction_2", npc_kingdoms_begin, npc_kingdoms_end),
          (neq, ":faction_2", ":cur_faction"),
          (neq, ":faction_2", ":pretender_original_faction"),
          (faction_slot_eq, ":faction_2", slot_faction_state, sfs_active),
          (assign, ":fitful_lords_this_faction", 0),
          (try_for_range, ":cur_troop", lords_begin, lords_end),
            (store_troop_faction, ":troop_cur_faction", ":cur_troop"),
            (eq, ":troop_cur_faction", ":faction_2"),
            (troop_get_slot, ":troop_original_faction", ":cur_troop", slot_troop_original_faction),
            (eq, ":troop_original_faction", ":cur_faction"),
            (val_add, ":fitful_lords_this_faction", 1),
          (try_end),
          # centers 
          (assign, ":fitful_centers", 0),
          (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
            (party_get_slot, ":center_lord", ":center_no", slot_town_lord),
            (ge, ":center_lord", 1),
            (store_troop_faction, ":troop_cur_faction", ":center_lord"),
            (eq, ":troop_cur_faction", ":faction_2"),
            (troop_get_slot, ":troop_original_faction", ":center_lord", slot_troop_original_faction),
            (eq, ":troop_original_faction", ":cur_faction"),
            (val_add, ":fitful_centers", 1),
          (try_end),
          (try_begin),
            (gt, ":fitful_centers", 0),
            (gt, ":fitful_lords_this_faction", ":fitful_lords"),
            (assign, ":fitful_lords", ":fitful_lords_this_faction"),
            (assign, ":fitful_faction", ":faction_2"),
          (try_end),
        (try_end),
        (try_begin),
          (lt, ":fitful_lords", 5),
          (assign, ":fitful_faction", -1),
        (try_end),
        
        (gt, ":fitful_faction", -1),
        (faction_get_slot, ":original_king", ":cur_faction", slot_faction_leader),
        (call_script, "script_change_troop_faction", ":original_king", ":cur_faction"),
        (troop_set_slot, ":original_king", slot_troop_occupation, slto_kingdom_hero),
        (call_script, "script_add_notification_menu", "mnu_notification_kingdom_restoration", ":cur_faction", ":fitful_faction"),
      (try_end),
    ]),
  
  (1,
    [
      (try_for_range, ":cur_quest", "qst_deal_with_forest_bandit", "qst_quests_end"),
        (check_quest_active, ":cur_quest"),
        (neg|check_quest_succeeded, ":cur_quest"),

        (quest_get_slot, ":dest_pt_no", ":cur_quest", slot_quest_target_party_template),
        (assign, ":has_hero", 0),
        (try_for_parties, ":party_no"),
          (party_get_template_id, ":party_template", ":party_no"),
          (eq, ":party_template", ":dest_pt_no"),
          (party_stack_get_troop_id, ":leader", ":party_no", 0),
          (troop_is_hero, ":leader"),
          (assign, ":has_hero", 1),
        (try_end),
        (eq, ":has_hero", 0),
        (party_template_set_slot, ":dest_pt_no", slot_party_template_has_hero, 0),
        (party_template_set_slot, ":dest_pt_no", slot_party_template_hero_party_id, -1),
#        (party_template_get_slot, ":bandit_hero_name", ":dest_pt_no", slot_party_template_hero_pre_name), ##Floris: Removed due to savegame compatibility.
#        (str_store_string, s1, ":bandit_hero_name"), ##Floris: Removed due to savegame compatibility.
        (display_message, "@{s1} has been eliminated by another party.", 0xff3333),
        (call_script, "script_cancel_quest", ":cur_quest"),
      (try_end),
    ]),

## CC 1.322, disabled in 1.324
#  (1,
#    [
#      (try_for_range, ":center_no", centers_begin, centers_end),
#        (party_set_flags, ":center_no", pf_always_visible, 1),
#        (is_between, ":center_no", walled_centers_begin, walled_centers_end),
#        (store_faction_of_party, ":town_faction", ":center_no"),
#        (store_relation, ":cur_relation", "fac_player_supporters_faction", ":town_faction"),
#        (try_begin),
#          (lt, ":cur_relation", 0),
#          (party_set_flags, ":center_no", pf_hide_defenders, 1),
#        (else_try),
#          (party_set_flags, ":center_no", pf_hide_defenders, 0),
#        (try_end),
#      (try_end),
#    ]),
##
## CC 1.322   
  (1,
    [
      (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
        #Give new title for faction leaders
        (store_troop_faction, ":faction_no", ":troop_no"),
        (is_between, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
        (faction_slot_eq, ":faction_no", slot_faction_leader, ":troop_no"),
        (call_script, "script_troop_set_title_according_to_faction", ":troop_no", ":faction_no"),
      (try_end),
    ]),
##
  
#Custom Troops Begin
# Note: make sure there is a comma in the entry behind this one
  (0,
    [
	 (try_for_range, ":cur_troop", customizable_troops_begin, customizable_troops_end),
        (neg|troop_is_hero, ":cur_troop"),
        (store_add, ":cur_troop_cur_name", ":cur_troop", 1),
        (str_store_troop_name, s1, ":cur_troop_cur_name"),
        (str_store_troop_name_plural, s2, ":cur_troop_cur_name"),
        (troop_set_name, ":cur_troop", s1),
        (troop_set_plural_name, ":cur_troop", s2),
      (try_end),
	  
      (map_free),
      (troop_get_inventory_slot, ":item", customizable_troops_end, 10),
      (eq,":item","itm_trade_velvet"),
      (call_script, "script_reload_custom_troops"),
      (troop_clear_inventory, customizable_troops_end),
    ]
  ),
#Custom Troops End
   
  ##diplomacy begin
  #Troop AI Spouse: Spouse thinking
  (3,
   [
    ##diplomacy start+
	(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),#<-- moved from (1) below
	(ge, ":player_spouse", active_npcs_begin),#<-- skip the rest of the check when there is no spouse
	##diplomacy end+
    (try_for_parties, ":spouse_party"),  
      (party_slot_eq, ":spouse_party", slot_party_type, dplmc_spt_spouse),
	  ##diplomacy start+
      #(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),#(1) <-- moved before loop
	  ##diplomacy end+
      (party_get_slot, ":spouse_target", ":spouse_party", slot_party_orders_object),
      (party_get_slot, ":home_center", ":spouse_party", slot_party_home_center),
      (store_distance_to_party_from_party, ":distance", ":spouse_party", ":spouse_target"),

      #Moving spouse to home village
      (try_begin),
        (le, ":distance", 1),
        (try_begin),
          (this_or_next|eq, ":spouse_target", "$g_player_court"),
		      (eq, ":spouse_target", ":home_center"),
          (remove_party, ":spouse_party"),
          (troop_set_slot, ":player_spouse", slot_troop_cur_center, ":spouse_target"),
        (else_try),
          (try_begin),
            (is_between, ":spouse_target", villages_begin, villages_end),
            (party_get_slot,":cur_merchant",":spouse_target", slot_town_elder),
          (else_try),
            (party_get_slot,":cur_merchant",":spouse_target", slot_town_merchant),
          (try_end),
          (troop_get_slot, ":amount", ":player_spouse", dplmc_slot_troop_mission_diplomacy),
          (troop_remove_items, ":cur_merchant", "itm_trade_bread", ":amount"),
          (party_set_ai_behavior, ":spouse_party", ai_bhvr_travel_to_party),
          (try_begin),
            (gt, "$g_player_court", 0),
            (party_set_slot, ":spouse_party", slot_party_ai_object, "$g_player_court"),
            (party_set_ai_object, ":spouse_party", "$g_player_court"),
          (else_try),
            (party_set_slot, ":spouse_party", slot_party_ai_object, ":home_center"),
            (party_set_ai_object, ":spouse_party", ":home_center"),
          (try_end),

          (troop_add_items, "trp_household_possessions", "itm_trade_bread", ":amount"),
        (try_end),
      (try_end),
    (try_end),
    ]),

#Recruiter kit begin
## This trigger keeps the recruiters moving by assigning them targets.
 (0.5,
   [
   (try_for_parties, ":party_no"),
      (party_slot_eq,":party_no", slot_party_type, dplmc_spt_recruiter),

      (party_get_slot, ":needed", ":party_no", dplmc_slot_party_recruiter_needed_recruits),

      (party_get_num_companion_stacks, ":stacks", ":party_no"),
      (assign, ":destruction", 1),
      (assign, ":quit", 0),

      (try_for_range, ":stack_no", 0, ":stacks"),
         (party_stack_get_troop_id, ":troop_id", ":party_no", ":stack_no"),
         (eq, ":troop_id", "trp_dplmc_recruiter"),
         (assign, ":destruction",0),
      (try_end),
      (try_begin),
         (party_get_battle_opponent, ":opponent", ":party_no"),
         (lt, ":opponent", 0),
         (eq, ":destruction", 1),
         (party_get_slot, ":party_origin", ":party_no", dplmc_slot_party_recruiter_origin),
         (str_store_party_name_link, s13, ":party_origin"),
         (assign, reg10, ":needed"),
         (display_log_message, "@Your recruiter who was commissioned to recruit {reg10} recruits to {s13} has been defeated!", 0xFF0000),
         (remove_party, ":party_no"),
         (assign, ":quit", 1),
      (try_end),

      #waihti
      (try_begin),
        (eq, ":quit", 0),
        (party_get_slot, ":party_origin", ":party_no", dplmc_slot_party_recruiter_origin),
        (store_faction_of_party, ":origin_faction", ":party_origin"),
        (neq, ":origin_faction", "$players_kingdom"),
        (str_store_party_name_link, s13, ":party_origin"),
        (assign, reg10, ":needed"),
        (display_log_message, "@{s13} has been taken by the enemy and your recruiter who was commissioned to recruit {reg10} recruits vanished  without a trace!", 0xFF0000),
        (remove_party, ":party_no"),
        (assign, ":quit", 1),
      (try_end),
      #waihti

      (eq, ":quit", 0),

      (party_get_num_companions, ":amount", ":party_no"),
      (val_sub, ":amount", 1),   #the recruiter himself doesn't count.

   #daedalus begin
      (party_get_slot, ":recruit_faction", ":party_no", dplmc_slot_party_recruiter_needed_recruits_faction),
   #daedalus end
      (lt, ":amount", ":needed"),  #If the recruiter has less troops than player ordered, new village will be set as target.
      (try_begin),
         #(get_party_ai_current_behavior, ":ai_bhvr", ":party_no"),
         #(eq, ":ai_bhvr", ai_bhvr_hold),
         (get_party_ai_object, ":previous_target", ":party_no"),
         (get_party_ai_behavior, ":previous_behavior", ":party_no"),
         (try_begin),
            (neq, ":previous_behavior", ai_bhvr_hold),
            (neq, ":previous_target", -1),
            (party_set_slot, ":previous_target", dplmc_slot_village_reserved_by_recruiter, 0),
         (try_end),
         (assign, ":min_distance", 999999),
         (assign, ":closest_village", -1),
         (try_for_range, ":village", villages_begin, villages_end),
            (store_distance_to_party_from_party, ":distance", ":party_no", ":village"),
            (lt, ":distance", ":min_distance"),
            (try_begin),
               (store_faction_of_party, ":village_current_faction", ":village"),
               (assign, ":faction_relation", 100),
               (try_begin),
                  (neq, ":village_current_faction", "$players_kingdom"),    # faction relation will be checked only if the village doesn't belong to the player's current faction
                  (store_relation, ":faction_relation", "$players_kingdom", ":village_current_faction"),
               (try_end),
               (ge, ":faction_relation", 0),
               (party_get_slot, ":village_relation", ":village", slot_center_player_relation),
               (ge, ":village_relation", 0),
               (party_get_slot, ":volunteers_in_village", ":village", slot_center_volunteer_troop_amount),
               (gt, ":volunteers_in_village", 0),
            #daedalus begin
               (party_get_slot, ":village_faction", ":village", slot_center_original_faction),
               (assign,":stop",1),
               (try_begin),
                  (eq,":recruit_faction",-1),
                  (assign,":stop",0),
               (else_try),
                  (eq, ":village_faction", ":recruit_faction"),
                  (assign,":stop",0),
               (try_end),
               (neq,":stop",1),
            #daedalus end
               (neg|party_slot_eq, ":village", slot_village_state, svs_looted),
               (neg|party_slot_eq, ":village", slot_village_state, svs_being_raided),
               (neg|party_slot_ge, ":village", slot_village_infested_by_bandits, 1),
               (neg|party_slot_eq, ":village", dplmc_slot_village_reserved_by_recruiter, 1),
               (assign, ":min_distance", ":distance"),
               (assign, ":closest_village", ":village"),
            (try_end),
         (try_end),
         (gt, ":closest_village", -1),
         (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
         (party_set_ai_object, ":party_no", ":closest_village"),
         (party_set_slot, ":party_no", slot_party_ai_object, ":closest_village"),
         (party_set_slot, ":closest_village", dplmc_slot_village_reserved_by_recruiter, 1),
      (try_end),
      (party_get_slot, ":target", ":party_no", slot_party_ai_object),
      (gt, ":target", -1),
      (store_distance_to_party_from_party, ":distance_from_target", ":party_no", ":target"),
      (try_begin),
         (store_faction_of_party, ":target_current_faction", ":target"),
         (assign, ":faction_relation", 100),
         (try_begin),
            (neq, ":target_current_faction", "$players_kingdom"),    # faction relation will be checked only if the target doesn't belong to the player's current faction
            (store_relation, ":faction_relation", "$players_kingdom", ":target_current_faction"),
         (try_end),
         (ge, ":faction_relation", 0),
         (party_get_slot, ":target_relation", ":target", slot_center_player_relation),
         (ge, ":target_relation", 0),
      #daedalus begin
            (party_get_slot, ":target_faction", ":target", slot_center_original_faction),
            (assign,":stop",1),
            (try_begin),
            (eq,":recruit_faction",-1),
            (assign,":stop",0),
        (else_try),
            (eq, ":target_faction", ":recruit_faction"),
            (assign,":stop",0),
            (try_end),
            (neq,":stop",1),
      #daedalus end
         (neg|party_slot_eq, ":target", slot_village_state, svs_looted),
            (neg|party_slot_eq, ":target", slot_village_state, svs_being_raided),
            (neg|party_slot_ge, ":target", slot_village_infested_by_bandits, 1),
         (le, ":distance_from_target", 0),
         (party_get_slot, ":volunteers_in_target", ":target", slot_center_volunteer_troop_amount),
         (party_get_slot, ":target_volunteer_type", ":target", slot_center_volunteer_troop_type),
         (assign, ":still_needed", ":needed"),
         (val_sub, ":still_needed", ":amount"),
         (try_begin),
            (gt, ":volunteers_in_target", ":still_needed"),
            (assign, ":santas_little_helper", ":volunteers_in_target"),
            (val_sub, ":santas_little_helper", ":still_needed"),
            (assign, ":amount_to_recruit", ":volunteers_in_target"),
            (val_sub, ":amount_to_recruit", ":santas_little_helper"),
            (assign, ":new_target_volunteer_amount", ":volunteers_in_target"),
            (val_sub, ":new_target_volunteer_amount", ":amount_to_recruit"),
            (party_set_slot, ":target", slot_center_volunteer_troop_amount, ":new_target_volunteer_amount"),
            (party_add_members, ":party_no", ":target_volunteer_type", ":amount_to_recruit"),
            (party_set_ai_behavior, ":party_no", ai_bhvr_hold),
            (party_set_slot, ":target", dplmc_slot_village_reserved_by_recruiter, 0),
         (else_try),
            (le, ":volunteers_in_target", ":still_needed"),
            (gt, ":volunteers_in_target", 0),
            (party_set_slot, ":target", slot_center_volunteer_troop_amount, -1),
            (party_add_members, ":party_no", ":target_volunteer_type", ":volunteers_in_target"),
            (party_set_ai_behavior, ":party_no", ai_bhvr_hold),
            (party_set_slot, ":target", dplmc_slot_village_reserved_by_recruiter, 0),
         (else_try),
            (le, ":volunteers_in_target", 0),
            (party_set_ai_behavior, ":party_no", ai_bhvr_hold),
            (party_set_slot, ":target", dplmc_slot_village_reserved_by_recruiter, 0),
         (else_try),
            (display_message, "@ERROR IN THE RECRUITER KIT SIMPLE TRIGGERS!",0xFF2222),
            (party_set_slot, ":target", dplmc_slot_village_reserved_by_recruiter, 0),
         (try_end),
      (try_end),
   (try_end),

   (try_for_parties, ":party_no"),
      (party_slot_eq,":party_no", slot_party_type, dplmc_spt_recruiter),
      (party_get_num_companions, ":amount", ":party_no"),
      (val_sub, ":amount", 1),   #the recruiter himself doesn't count
      (party_get_slot, ":needed", ":party_no", dplmc_slot_party_recruiter_needed_recruits),
      (eq, ":amount", ":needed"),
      (party_get_slot, ":party_origin", ":party_no", dplmc_slot_party_recruiter_origin),
      (try_begin),
         (neg|party_slot_eq, ":party_no", slot_party_ai_object, ":party_origin"),
         (party_set_slot, ":party_no", slot_party_ai_object, ":party_origin"),
         (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
         (party_set_ai_object, ":party_no", ":party_origin"),
      (try_end),
      (store_distance_to_party_from_party, ":distance_from_origin", ":party_no", ":party_origin"),
      (try_begin),
         (le, ":distance_from_origin", 0),
         (party_get_num_companion_stacks, ":stacks", ":party_no"),
         (try_for_range, ":stack_no", 1, ":stacks"),
            (party_stack_get_size, ":size", ":party_no", ":stack_no"),
            (party_stack_get_troop_id, ":troop_id", ":party_no", ":stack_no"),
            (party_add_members, ":party_origin", ":troop_id", ":size"),
         (try_end),
         (str_store_party_name_link, s13, ":party_origin"),
         (assign, reg10, ":amount"),
         (display_log_message, "@A recruiter has brought {reg10} recruits to {s13}.", 0x00FF00),
         (remove_party, ":party_no"),
      (try_end),
   (try_end),
   ]),

#This trigger makes sure that no village is left reserved forever.
(12,
   [
   (try_for_range, ":village", villages_begin, villages_end),
      (party_set_slot, ":village", dplmc_slot_village_reserved_by_recruiter, 0),
   (try_end),
   ]),
#Recruiter kit end

 #process gift_carvans
 (0.5,
 [
  (eq, "$g_player_chancellor", "trp_dplmc_chancellor"),
  ##nested diplomacy start+
  #These gifts are far too efficient.  To be balanced with Native, they
  #should not (at the best case) exceed an efficiency of 1000 gold per point.
  (assign, ":save_reg0", reg0),
  (assign, ":save_reg1", reg1),
  (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),#store for use below
  ##nested diplomacy end+
  (try_for_parties, ":party_no"),
    (party_slot_eq,":party_no", slot_party_type, dplmc_spt_gift_caravan),
    (party_is_active, ":party_no"),
    (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),
    (party_get_slot, ":target_troop", ":party_no", slot_party_orders_object),

    (try_begin),
      (party_is_active, ":target_party"),

      (store_distance_to_party_from_party, ":distance_to_target", ":party_no", ":target_party"),
      (str_store_party_name, s14, ":party_no"),
      (str_store_party_name, s15,":target_party"),

      (try_begin), #debug
        (eq, "$cheat_mode", 1),
        (assign, reg0, ":distance_to_target"),
        (display_message, "@Distance between {s14} and {s15}: {reg0}"),
      (try_end),

      (try_begin),
        (le, ":distance_to_target", 1),

        (party_get_slot, ":gift", ":party_no", dplmc_slot_party_mission_diplomacy),
        (str_store_item_name, s12, ":gift"),

        (try_begin),
          (gt, ":target_troop", 0),
          (str_store_troop_name, s13, ":target_troop"),
        (else_try),
          (str_store_party_name, s13, ":target_party"),
        (end_try),
        (display_log_message, "@Your caravan has brought {s12} to {s13}.", 0x00FF00),

        (assign, ":relation_boost", 0),
        (store_faction_of_party, ":target_faction", ":target_party"),

        (try_begin),
          (gt, ":target_troop", 0),
          (faction_slot_eq,":target_faction",slot_faction_leader,":target_troop"),
          (try_begin),
            (eq, ":gift", "itm_trade_wine"),
            (assign, ":relation_boost", 1),
          (else_try),
            (eq, ":gift", "itm_trade_oil"),
            (assign, ":relation_boost", 2),
          (try_end),
        (else_try),
          (store_random_in_range, ":random", 1, 3),
          (try_begin),
            (eq, ":gift", "itm_trade_ale"),
            (val_add, ":relation_boost", ":random"),
          (else_try),
            (eq, ":gift", "itm_trade_wine"),
            (store_add, ":relation_boost", 1, ":random"),
          (else_try),
            (eq, ":gift", "itm_trade_oil"),
            (store_add, ":relation_boost", 2, ":random"),
          (else_try),
            (eq, ":gift", "itm_trade_raw_dyes"),
            (val_add, ":relation_boost", 1),
          (else_try),
            (eq, ":gift", "itm_trade_raw_silk"),
            (val_add, ":relation_boost", 2),
          (else_try),
            (eq, ":gift", "itm_trade_velvet"),
            (val_add, ":relation_boost", 4),
          (else_try),
            (eq, ":gift", "itm_trade_smoked_fish"),
            (try_begin),
              (party_slot_eq, ":target_party", slot_party_type, spt_village),
              (val_add, ":relation_boost", 1),
            (try_end),
          (else_try),
            (eq, ":gift", "itm_trade_cheese"),
            (val_add, ":relation_boost", 1),
            (try_begin),
              (party_slot_eq, ":target_party", slot_party_type, spt_village),
              (val_add, ":relation_boost", 1),
            (try_end),
          (else_try),
            (eq, ":gift", "itm_trade_honey"),
            (val_add, ":relation_boost", 2),
            (try_begin),
              (party_slot_eq, ":target_party", slot_party_type, spt_village),
              (val_add, ":relation_boost", 2),
            (try_end),
          (try_end),
        (try_end),

        (try_begin),
          (this_or_next|eq, ":target_faction", "fac_player_supporters_faction"),
          (eq, ":target_faction", "$players_kingdom"),
          (val_add, ":relation_boost", 1),
        (try_end),

		##nested diplomacy start+
		#Determine the gold cost of the gifts.
		(store_item_value, ":gift_value", ":gift"),
		(party_get_slot, ":gift_value_factor", ":party_no", dplmc_slot_party_mission_parameter_1),
		(try_begin),
			(gt, ":gift_value_factor", 0),
			(val_mul, ":gift_value", ":gift_value_factor"),
		(else_try),
			(this_or_next|is_between, ":target_troop", kingdom_ladies_begin, kingdom_ladies_end),
			(neg|is_between, ":gift", trade_goods_begin, trade_goods_end),
		(else_try),
			(is_between, ":target_troop", active_npcs_begin, active_npcs_end),
			(val_mul, ":gift_value", 150),
		(else_try),
			(is_between, ":target_party", centers_begin, centers_end),
			(val_mul, ":gift_value", 300),
		(try_end),
		(assign, ":gift_value_factor", 100),
		
		#(store_sub, ":gift_slot_no", ":gift", trade_goods_begin),
		#(val_add, ":gift_slot_no", slot_town_trade_good_prices_begin),
		
		(try_begin),
			#Gift isn't a trade good: this should never happen
			(neg|is_between, ":gift", trade_goods_begin, trade_goods_end),
			(try_begin),
				(this_or_next|gt, ":target_troop", 0),
					(party_slot_eq, ":target_party", slot_party_type, spt_town),
				(assign, ":gift_value_factor", 115),
			(else_try),
				(assign, ":gift_value_factor", 130),
			(try_end),				
		(else_try),
			#Given to a lord.
			(gt, ":target_troop", 0),
			
			(assign, ":global_price_factor", 0),
			(assign, ":faction_price_factor", 0),
			(assign, ":faction_markets", 0),
			(assign, ":personal_price_factor", 0),
			(assign, ":personal_markets", 0),
			
			(try_for_range, ":center_no", towns_begin, towns_end),
				(call_script, "script_dplmc_get_item_buy_price_factor", ":gift", ":center_no", -2, -2),
				(val_add, ":global_price_factor", reg0),
				
				(store_faction_of_party, ":center_faction", ":center_no"),
				(eq, ":center_faction", ":target_faction"),
				(val_add, ":faction_price_factor", reg0),
				(val_add, ":faction_markets", 1),
				
				(party_slot_eq, ":center_no", slot_town_lord, ":target_troop"),
				(val_add, ":personal_price_factor", reg0),
				(val_add, ":personal_markets", 1),
			(try_end),
			
			(try_begin),
				(eq, ":personal_markets", 0),
				(try_for_range, ":center_no", villages_begin, villages_end),
					(try_begin),
						(party_slot_eq, ":center_no", slot_town_lord, ":target_troop"),
						(call_script, "script_dplmc_get_item_buy_price_factor", ":gift", ":center_no", -2, -2),
						(val_add, ":faction_markets", reg0),
						(val_add, ":personal_markets", 1),
					(try_end),
					#Check for castles (deliberately allow multiple-counting)
					(try_begin),
						(party_get_slot, reg1, ":center_no", slot_village_bound_center),
						(gt, reg1, 0),
						(party_slot_eq, reg1, slot_party_type, spt_castle),
						(party_slot_eq, reg1, slot_town_lord, ":target_troop"),
						(call_script, "script_dplmc_get_item_buy_price_factor", ":gift", ":center_no", -2, -2),
						(val_add, ":faction_markets", reg0),
						(val_add, ":personal_markets", 1),
					(try_end),
				(try_end),
			(try_end),

			(try_begin),
				#First use any markets at or near the target's fiefs
				(gt, ":personal_markets", 0),
				(store_div, ":gift_value_factor", ":personal_price_factor", ":personal_markets"),
			(else_try),
				#Alternately use any faction markets
				(gt, ":faction_markets", 0),
				(val_mul, ":faction_price_factor", 130),#Convert trade penalty from 115% to 130%
				(val_div, ":faction_price_factor", 115),
				(store_div, ":gift_value_factor", ":faction_price_factor", ":faction_markets"),
			(else_try),
				#As a final option use the global average price
				(gt, towns_end, towns_begin),#should always be true (if not, then the gift price factor stays average)
				(store_sub, reg1, towns_end, towns_begin),
				(val_mul, ":global_price_factor", 130),#Convert trade penalty from 115% to 130%
				(val_div, ":global_price_factor", 115),
				(store_div, ":gift_value_factor", ":global_price_factor", reg1),
			(try_end),
		(else_try),
			#Given to a town or village
			(gt, ":target_party", 0),
			(call_script, "script_dplmc_get_item_buy_price_factor", ":gift", ":center_no", -2, -2),
			(assign, ":gift_value_factor", reg0),
		(else_try),
			#This should never happen
			(assign, ":gift_value_factor", 115),
		(try_end),
		
		#(try_begin),
		#	(eq, ":reduce_campaign_ai", 0), #hard: don't use less than 50% of the item's base value
		#	(val_max, ":gift_value_factor", 50),
		#(else_try),
		#	(eq, ":reduce_campaign_ai", 1), #normal: don't use less than 75% of the item's base value
		#	(val_max, ":gift_value_factor", 75),
		#(else_try),
		#	(eq, ":reduce_campaign_ai", 2), #easy: don't use less than 100% of item's base value
		#	(val_max, ":gift_value_factor", 100),
		#(try_end),
		
		#(val_mul, ":gift_value", ":gift_value_factor"),
		#(val_add, ":gift_value", 50),
		#(val_div, ":gift_value", 100),
		 
		(try_begin),
			(ge, "$cheat_mode", 1),
			(assign, reg0, ":gift_value_factor"),
			(store_mul, reg1, ":gift_value", ":gift_value_factor"),
			(val_add, reg1, 50),
			(val_div, reg1, 100),
			(val_add, reg1, 50),
			(display_message, "@{!} Gift price factor {reg0}/100, effective value {reg1}"),
		(try_end),
		
		(val_mul, ":gift_value", ":gift_value_factor"),
		(val_add, ":gift_value", 50),
		(val_div, ":gift_value", 100),

		(val_add, ":gift_value", 50),#the cost of the messenger
	    (store_random_in_range, ":random", 0, 1000),#randomly round up or down later, when dividing by 1000
		(assign, reg0, ":gift_value"),#<-- see (1) below, store gold value of gift
		(val_add, ":gift_value", ":random"),
		(val_div, ":gift_value", 1000),
		
		(try_begin),
		   (eq, ":reduce_campaign_ai", 0), #hard: do not exceed 1/1000 efficiency (with a 40% increase, can actually reach about 1/714)
		   (val_min, ":relation_boost", ":gift_value"),
		   (try_begin),	
			  (eq, ":relation_boost", 0),
			  (store_random_in_range, ":random", 0, 1000),
			  (lt, ":random", reg0),#<-- (1) see above, has gold value of gift
			  (assign, ":relation_boost", 1),
		   (try_end),
		(else_try),
		   (eq, ":reduce_campaign_ai", 1), #medium: use a blend of the two
		   (lt, ":gift_value", ":relation_boost"),
		   (val_add, ":relation_boost", ":gift_value"),
		   (val_add, ":relation_boost", 1),
		   (val_div, ":relation_boost", 2),
	    (else_try),
		   (eq, ":reduce_campaign_ai", 2), #easy: do not use
		(try_end),
		
		(val_max, ":gift_value", 1),
		(val_min, ":relation_boost", ":gift_value"),
		##nested diplomacy end+

        (try_begin),
		##nested diplomacy start+
		#Write a message so the player doesn't think the lack of relation gain is an error.
			(lt, ":relation_boost", 1),
			(try_begin),
				(gt, ":target_troop", 0),
				(display_message, "@{s13} is unimpressed by your paltry gift."),
			(else_try),
				(display_message, "@The people of {s13} are unimpressed by your paltry gift."),
			(try_end),
		(else_try),
		##nested diplomacy+
          (gt, ":target_troop", 0),
		  (call_script, "script_change_player_relation_with_troop", ":target_troop", ":relation_boost"),
        (else_try),
          (call_script, "script_change_player_relation_with_center", ":target_party", ":relation_boost"),
        (try_end),
        (remove_party, ":party_no"),
      (try_end),
    (else_try),
      (display_log_message, "@Your caravan has lost it's way and gave up your mission!", 0xFF0000),
      (remove_party, ":party_no"),
    (try_end),
  (try_end),
  ##nested diplomacy start+
  (assign, reg0, ":save_reg0"),
  (assign, reg1, ":save_reg1"),
  ##nested diplomacy start+
 ]),

 #process messengers
 (0.5,
 [
  (try_for_parties, ":party_no"),
    (party_slot_eq,":party_no", slot_party_type, spt_messenger),

    (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),
    (party_get_slot, ":orders_object", ":party_no", slot_party_orders_object),

    (try_begin),
      (party_is_active, ":target_party"),
      (store_distance_to_party_from_party, ":distance_to_target", ":party_no", ":target_party"),
      (str_store_party_name, s14, ":party_no"),
      (str_store_party_name, s15,":target_party"),

      (try_begin), #debug
        (eq, "$cheat_mode", 1),
        (assign, reg0, ":distance_to_target"),
        (display_message, "@Distance between {s14} and {s15}: {reg0}"),
      (try_end),

      (try_begin),
        (le, ":distance_to_target", 1),

        (try_begin), # returning to p_main_party
          (eq, ":target_party", "p_main_party"),
          (party_get_slot, ":party_leader", ":party_no", slot_party_orders_object),
          (party_get_slot, ":success", ":party_no", dplmc_slot_party_mission_diplomacy),
          (call_script, "script_add_notification_menu", "mnu_dplmc_messenger", ":party_leader", ":success"),
          (remove_party, ":party_no"),
        (else_try), # patrols
          (party_slot_eq, ":target_party", slot_party_type, spt_patrol),
          (party_get_slot, ":message", ":party_no", dplmc_slot_party_mission_diplomacy),

          (try_begin),
            (eq, ":message", spai_undefined),
            (remove_party, ":target_party"),
          (else_try),
            (eq, ":message", spai_retreating_to_center),
            (str_store_party_name, s6, ":orders_object"),
            (party_set_name, ":target_party", "@Transfer to {s6}"),
            (party_set_ai_behavior, ":target_party", ai_bhvr_travel_to_party),
            (party_set_ai_object, ":target_party", ":orders_object"),
            (party_set_slot, ":target_party", slot_party_ai_object, ":orders_object"),
            (party_set_slot, ":target_party", slot_party_ai_state, spai_retreating_to_center),  
            (party_set_aggressiveness, ":target_party", 0), #Diplomacy 3.3.2
            (party_set_courage, ":target_party", 3), #Diplomacy 3.3.2
            (party_set_ai_initiative, ":target_party", 100),   #Diplomacy 3.3.2                   
          (else_try),
            (str_store_party_name, s6, ":orders_object"),
            (party_set_name, ":target_party", "@{s6} patrol"),
            (party_set_ai_behavior, ":target_party", ai_bhvr_travel_to_party),
            (party_set_ai_object, ":target_party", ":orders_object"),
            (party_set_slot, ":target_party", slot_party_ai_object, ":orders_object"),
            (party_set_slot, ":target_party", slot_party_orders_type, ":message"),
          (try_end),

          (remove_party, ":party_no"),
        (else_try), # reached any other target
          (party_stack_get_troop_id, ":party_leader", ":target_party", 0),
          (str_store_troop_name, s13, ":party_leader"),

          (try_begin), #debug
            (eq, "$cheat_mode", 1),
            (display_log_message, "@Your messenger reached {s13}.", 0x00FF00),
            (assign, "$g_talk_troop", ":party_leader"), #debug
          (try_end),

          (party_get_slot, ":message", ":party_no", dplmc_slot_party_mission_diplomacy),
          (assign, ":success", 0),
          (try_begin),
            (party_set_slot, ":target_party", slot_party_commander_party, "p_main_party"),
          	(store_current_hours, ":hours"),
          	(party_set_slot, ":target_party", slot_party_following_orders_of_troop, "trp_kingdom_heroes_including_player_begin"),
          	(party_set_slot, ":target_party", slot_party_orders_object, ":orders_object"),
          	(party_set_slot, ":target_party", slot_party_orders_type, ":message"),

          	(party_set_slot, ":target_party", slot_party_orders_time, ":hours"),
            (call_script, "script_npc_decision_checklist_party_ai", ":party_leader"), #This handles AI for both marshal and other parties


            (try_begin), #debug
              (eq, "$cheat_mode", 1),
              (display_message, "@{s14}"), #debug
            (try_end),

            (try_begin),
              (eq, reg0, ":message"),
              (eq, reg1, ":orders_object"),
              (assign, ":success", 1),
            (try_end),
            (call_script, "script_party_set_ai_state", ":target_party", reg0, reg1),
          (try_end),

          (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
          (party_set_ai_object, ":party_no", "p_main_party"),
          (party_set_slot, ":party_no", slot_party_ai_object, "p_main_party"),
          (party_set_slot, ":party_no", slot_party_orders_object, ":party_leader"),
          (party_set_slot, ":party_no", dplmc_slot_party_mission_diplomacy, ":success"),
        (try_end),
      (try_end),
    (else_try),
      (display_log_message, "@Your messenger has lost it's way and gave up your mission!", 0xFF0000),
      (remove_party, ":party_no"),
    (try_end),
  (try_end),
 ]),


  # Constable training
   (24,
   [
   (eq, "$g_player_constable", "trp_dplmc_constable"),
   (is_between, "$g_constable_training_center", walled_centers_begin, walled_centers_end),
   (party_slot_eq, "$g_constable_training_center", slot_town_lord, "trp_player"),

   (store_skill_level, ":trainer_level", skl_trainer, "trp_player"),
   (val_add, ":trainer_level", 4),
   (store_div, ":xp_gain", ":trainer_level", 2),

   (try_for_parties, ":party_no"),
    (party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
    (eq, ":party_no", "$g_constable_training_center"),

    (party_get_num_companion_stacks, ":num_stacks", ":party_no"),

    (assign, ":trained", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (eq, ":trained", 0),
      (party_stack_get_troop_id, ":troop_id", ":party_no", ":i_stack"),
      (neg|troop_is_hero, ":troop_id"),

##Diplomacy 3.2.1  
      ##Floris - rewrite to actually address melee vs ranged as set in the dialog (0=melee, 1=ranged)    
      # (troop_get_upgrade_troop, ":upgrade_troop", ":troop_id" , "$g_constable_training_type"),
      # (try_begin),
       # (le, ":upgrade_troop", 0),
       # (troop_get_upgrade_troop, ":upgrade_troop", ":troop_id", 0),
      # (try_end),
	  (troop_get_upgrade_troop, ":upgrade_troop",   ":troop_id", 0),
      (troop_get_upgrade_troop, ":upgrade_troop_2", ":troop_id", 1),
	  (try_begin),
		(eq, "$g_constable_training_type", 0), #melee
		(try_begin),
		    (gt, ":upgrade_troop", 0),
			(neg|troop_is_guarantee_ranged, ":upgrade_troop"),
		(else_try),
			(gt, ":upgrade_troop_2", 0),
			(neg|troop_is_guarantee_ranged, ":upgrade_troop_2"),
			(assign, ":upgrade_troop", ":upgrade_troop_2"),
		(try_end),
	  (else_try),
	    (eq, "$g_constable_training_type", 1), #ranged
		(try_begin),
		    (gt, ":upgrade_troop", 0),
			(troop_is_guarantee_ranged, ":upgrade_troop"),
		(else_try),
			(gt, ":upgrade_troop_2", 0),
			(troop_is_guarantee_ranged, ":upgrade_troop_2"),
			(assign, ":upgrade_troop", ":upgrade_troop_2"),
		(try_end),
      (try_end),
	  ##Floris - end

      #only proceed if troop is upgradable
      (gt, ":upgrade_troop", 0),
##
      
      (store_character_level, ":troop_level", ":troop_id"),
      (assign, ":troop_limit" , 6),##Diplomacy 3.2
      
      (try_begin),
        (eq, "$g_constable_training_improved", 1),
        (assign, ":troop_limit" , 10),
        (try_begin),
          (le, ":troop_level", 6),
          (val_add, ":xp_gain", 2), #more recruits are trained during improved training
        (try_end),
      (try_end),

      (le, ":troop_level", ":troop_limit"),

      (party_count_members_of_type,":cur_number",":party_no",":troop_id"),
      (val_min, ":xp_gain", ":cur_number"),

      (call_script, "script_game_get_upgrade_cost", ":troop_id"),
      (store_mul, ":upgrade_cost", ":xp_gain", reg0),
#Diplomacy 3.2 begin      
      (try_begin),
        (eq, "$g_constable_training_improved", 1),
        (val_add, ":upgrade_cost", 10), #+10 denars during improved training
      (try_end),
#Diplomacy 3.2 end
      (store_troop_gold, ":gold", "trp_household_possessions"),
      (try_begin),
        (lt, ":gold", ":upgrade_cost"),
        (store_div, ":money_limit", ":gold", reg0),
        (val_min, ":xp_gain", ":money_limit"),
        (store_mul, ":upgrade_cost", ":xp_gain", reg0),
        (display_message, "@Not enough money in treasury to upgrade troops."),
      (try_end),

      (party_remove_members,":party_no",":troop_id",":xp_gain"),
      (party_add_members, ":party_no", ":upgrade_troop", ":xp_gain"),

      (call_script, "script_dplmc_withdraw_from_treasury", ":upgrade_cost"),

      (assign, reg5, ":xp_gain"),
      (str_store_troop_name, s6, ":troop_id"),
      (str_store_troop_name, s7, ":upgrade_troop"),
      (str_store_party_name, s8, ":party_no"),
      (display_message, "@Your constable upgraded {reg5} {s6} to {s7} in {s8}"),
      (assign, ":trained", 1),
    (try_end),
   (try_end),
    ]),

  # Patrol wages
   (24 * 7,
   [

    (try_for_parties, ":party_no"),
      (party_slot_eq,":party_no", slot_party_type, spt_patrol),

      

      (party_get_slot, ":ai_state", ":party_no", slot_party_ai_state),
      (eq, ":ai_state", spai_patrolling_around_center),

      (try_begin),
		(party_slot_eq, ":party_no", dplmc_slot_party_mission_diplomacy, "trp_player"),
        (assign, ":total_wage", 0),
        (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", ":party_no", ":i_stack"),
          (party_stack_get_size, ":stack_size", ":party_no", ":i_stack"),
          (call_script, "script_game_get_troop_wage", ":stack_troop", 0),
          (val_mul, reg0, ":stack_size"),
          (val_add, ":total_wage", reg0),
        (try_end),
        (store_troop_gold, ":gold", "trp_household_possessions"),
        (try_begin),
          (lt, ":gold", ":total_wage"),
          (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),
          (str_store_party_name, s6, ":target_party"),
          (display_log_message, "@Your soldiers patrolling {s6} disbanded because you can't pay the wages!", 0xFF0000),
          (remove_party, ":party_no"),
        (try_end),
      (try_end),
    (try_end),
    ]),

  #create ai patrols
   (24 * 7,
   [      
    (try_for_range, ":kingdom", npc_kingdoms_begin, npc_kingdoms_end),

      (assign, ":max_patrols", 0),
      (try_for_range, ":center", towns_begin, towns_end),
        (store_faction_of_party, ":center_faction", ":center"),
        (eq, ":center_faction", ":kingdom"),
        (val_add, ":max_patrols", 1),
      (try_end),

      (assign, ":count", 0),
      (try_for_parties, ":party_no"),
        (party_slot_eq, ":party_no", slot_party_type, spt_patrol),
        (store_faction_of_party, ":party_faction", ":party_no"),
        (eq, ":party_faction", ":kingdom"),
        (neg|party_slot_eq, ":party_no", dplmc_slot_party_mission_diplomacy, "trp_player"), #not player ordered
        (try_begin),
           #Remove patrols above the maximum number allowed.
           (ge, ":count", ":max_patrols"),
           (try_begin),
              (ge, "$cheat_mode", 1),
              (str_store_faction_name, s4, ":kingdom"),
              (str_store_party_name, s5, ":party_no"),
              (display_message, "@{!}DEBUG - Removed {s5} because {s4} cannot support that many patrols"),
           (try_end),
           (remove_party, ":party_no"),
        (else_try),
           (val_add, ":count", 1),
        (try_end),
      (try_end),

      (try_begin),
        (lt, ":count", ":max_patrols"),

        (store_random_in_range, ":random", 0, 10),
        (le, ":random", 3),

        (assign, ":start_center", -1),
        (assign, ":target_center", -1),

        (try_for_range, ":center", towns_begin, towns_end),
          (store_faction_of_party, ":center_faction", ":center"),
          (eq, ":center_faction", ":kingdom"),

          (eq, ":start_center", -1),
          (eq, ":target_center", -1),

          (assign, ":continue", 1),
          (try_for_parties, ":party_no"),
            (party_slot_eq, ":party_no", slot_party_type, spt_patrol),
            (store_faction_of_party, ":party_faction", ":party_no"),
            (eq, ":party_faction", ":kingdom"),
            (party_get_slot, ":target", ":party_no", slot_party_ai_object),
            (eq, ":target", ":center"),
            (assign, ":continue", 0),
          (try_end),
          (eq, ":continue", 1),

          (call_script, "script_cf_select_random_town_with_faction", ":kingdom"),
          (neq, reg0, -1),

          (assign, ":start_center", reg0),
          (assign, ":target_center", ":center"),
        (try_end),

        (try_begin),
          (neq, ":start_center", -1),
          (neq, ":target_center", -1),
          (store_random_in_range, ":random_size", 0, 3),
          (faction_get_slot, ":faction_leader", ":kingdom", slot_faction_leader), #Diplomacy 3.3.2
          (call_script, "script_dplmc_send_patrol", ":start_center", ":target_center", ":random_size",":kingdom", ":faction_leader"), #Diplomacy 3.3.2
        (try_end),
      (try_end),
    (try_end),
    ]),

  # Patrol ai
   (2,
   [

    (try_for_parties, ":party_no"),
      (party_slot_eq,":party_no", slot_party_type, spt_patrol),

      (call_script, "script_party_remove_all_prisoners", ":party_no"),

      (try_begin),
        (get_party_ai_behavior, ":ai_behavior", ":party_no"),
        (eq, ":ai_behavior", ai_bhvr_travel_to_party),
        (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),

        (try_begin),
          (gt, ":target_party", 0),
          (store_distance_to_party_from_party, ":distance_to_target", ":party_no", ":target_party"),
          (le, ":distance_to_target", 5),
          (try_begin),
            (party_get_slot, ":ai_state", ":party_no", slot_party_ai_state),
            (eq, ":ai_state", spai_retreating_to_center),
            (try_begin),
              (le, ":distance_to_target", 1),
              (call_script, "script_party_add_party", ":target_party", ":party_no"),
              (remove_party, ":party_no"),
            (try_end),
          (else_try),
            (party_get_position, pos1, ":target_party"),
            (party_set_ai_behavior,":party_no", ai_bhvr_patrol_location),
            (party_set_ai_patrol_radius, ":party_no", 1),
            (party_set_ai_target_position, ":party_no", pos1),
          (try_end),
        (else_try),
          #remove party?
        (try_end),

      (try_end),
    (try_end),
    ]),

  # Scout ai
   (0.2,
   [

    (try_for_parties, ":party_no"),
      (party_slot_eq,":party_no", slot_party_type, spt_scout),

      (try_begin),
        (get_party_ai_behavior, ":ai_behavior", ":party_no"),
        (this_or_next|eq, ":ai_behavior", ai_bhvr_travel_to_point),
        (eq, ":ai_behavior", ai_bhvr_travel_to_party),

        (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),
        (store_distance_to_party_from_party, ":distance_to_target", ":party_no", ":target_party"),
        (le, ":distance_to_target", 1),

        (try_begin),
          (eq, ":target_party", "p_main_party"),

          (party_get_slot, ":mission_target", ":party_no", dplmc_slot_party_mission_diplomacy),
          (call_script, "script_add_notification_menu", "mnu_dplmc_scout", ":mission_target", 0),

          (remove_party, ":party_no"),
        (else_try),
          (neq, ":target_party", "p_main_party"),
          (party_get_slot, ":hours", ":party_no", dplmc_slot_party_mission_diplomacy),

          (try_begin),
            (le, ":hours", 100),
            (disable_party, ":party_no"),
            (val_add, ":hours", 1),
            (party_set_slot, ":party_no", dplmc_slot_party_mission_diplomacy, ":hours"),

            (try_begin),
              (store_random_in_range, ":random", 0, 1000),
              (eq, ":random", 0),
              (str_store_party_name, s11, ":target_party"),
              (display_log_message, "@It is rumoured that a spy has been caught in {s11}.", 0xFF0000),
              (remove_party, ":party_no"),
            (try_end),

          (else_try),
            (enable_party, ":party_no"),
            (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
            (party_set_ai_object, ":party_no", "p_main_party"),
            (party_set_slot, ":party_no", slot_party_ai_object, "p_main_party"),
            (party_set_slot, ":party_no", dplmc_slot_party_mission_diplomacy, ":target_party"),
          (try_end),

        (try_end),
      (try_end),
    (try_end),
    ]),

  # Policy
   (30 * 24,
   [
	##nested diplomacy start+
	##If the player is ruler or co-ruler of an NPC kingdom, make sure the
	#policy matches fac_player_supporters_faction.  (It should be synchronized
	#elsewhere, but do it here in case there has been an error.)
	(assign, ":player_is_coruler_of_npc_faction", 0),
	  (try_begin),
		(neq, "$players_kingdom", "fac_player_supporters_faction"),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
		(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		
		(assign, ":player_is_coruler_of_npc_faction", 1),

		(faction_get_slot, reg0, "$players_kingdom", dplmc_slot_faction_serfdom),
		(faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_serfdom,  reg0),

		(faction_get_slot, reg0, "$players_kingdom", dplmc_slot_faction_centralization),
		(faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_centralization,  reg0),

		(faction_get_slot, reg0, "$players_kingdom", dplmc_slot_faction_quality),
		(faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_quality,  reg0),

		(faction_get_slot, reg0, "$players_kingdom", dplmc_slot_faction_aristocracy),
		(faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_aristocracy,  reg0),

		(faction_get_slot, reg0, "$players_kingdom", dplmc_slot_faction_mercantilism),
		(faction_set_slot, "fac_player_supporters_faction", dplmc_slot_faction_mercantilism,  reg0),
	(try_end),
	##nested diplomacy end+
  (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
    (faction_slot_eq, ":kingdom", slot_faction_state, sfs_active),

    (faction_get_slot, ":centralization", ":kingdom", dplmc_slot_faction_centralization),
    (faction_get_slot, ":aristocracy", ":kingdom", dplmc_slot_faction_aristocracy),
    (faction_get_slot, ":quality", ":kingdom", dplmc_slot_faction_quality),
    (faction_get_slot, ":serfdom", ":kingdom", dplmc_slot_faction_serfdom),
	 ##nested diplomacy start+
    (faction_get_slot, ":mercantilism", ":kingdom", dplmc_slot_faction_mercantilism),
	 ##nested diplomacy end+

#Diplomacy 3.2 begin
    (try_begin),
      (eq, "$cheat_mode", 1),
      (str_store_faction_name, s9, ":kingdom"),
      (assign, reg1, ":centralization"),
      (display_message, "@{!}DEBUG - centralization {reg1}"),
      (assign, reg1, ":aristocracy"),
      (display_message, "@{!}DEBUG - aristocracy {reg1}"),
      (assign, reg1, ":quality"),
      (display_message, "@{!}DEBUG - quality {reg1}"),
      (assign, reg1, ":serfdom"),
      (display_message, "@{!}DEBUG - serfdom {reg1}"),
		##nested diplomacy start+
      (assign, reg1, ":mercantilism"),
      (display_message, "@{!}DEBUG - mercantilism {reg1}"),
		##nested diplomacy end+
    (try_end),
#Diplomacy 3.2 end

    (try_begin),
      (is_between, ":kingdom", npc_kingdoms_begin, npc_kingdoms_end),
      ##nested diplomacy start+
      ##Ensure the player isn't the kingdom's ruler or co-ruler
      (this_or_next|neq, ":kingdom", "$players_kingdom"),
		(eq, ":player_is_coruler_of_npc_faction", 0), 
	  ##Add the chance to move around mercantilism.
      #(store_random_in_range, ":random", 0, 8),
	  (store_random_in_range, ":random", 0, 10),
      ##nested diplomacy end+

      (try_begin),
		  ##nested diplomacy start+
        #(is_between, ":random", 1, 5),
		  (is_between, ":random", 1, 6),
		  ##nested diplomacy end+
        (store_random_in_range, ":change", -1, 2),

        (try_begin),
          (eq, "$cheat_mode", 1),
          (str_store_faction_name, s12, ":kingdom"),
          (assign, reg1, ":change"),
          (assign, reg2, ":random"),
          (display_message, "@{!}DEBUG - changing {reg1} of {reg2} for {s12}"),
        (try_end),

        (try_begin),
          (eq, ":random", 1),
          (val_add, ":centralization", ":change"),
          (val_max, ":centralization", -3),
          (val_min, ":centralization", 3),
          (faction_set_slot, ":kingdom", dplmc_slot_faction_centralization, ":centralization"),
        (else_try),
          (eq, ":random", 2),
          (val_add, ":aristocracy", ":change"),
          (val_max, ":aristocracy", -3),
          (val_min, ":aristocracy", 3),
          (faction_set_slot, ":kingdom", dplmc_slot_faction_aristocracy, ":aristocracy"),
        (else_try),
          (eq, ":random", 3),
          (val_add, ":quality", ":change"),
          (val_max, ":quality", -3),
          (val_min, ":quality", 3),
          (faction_set_slot, ":kingdom", dplmc_slot_faction_quality, ":quality"),
        (else_try),
          (eq, ":random", 4),
          (val_add, ":serfdom", ":change"),
          (val_max, ":serfdom", -3),
          (val_min, ":serfdom", 3),
          (faction_set_slot, ":kingdom", dplmc_slot_faction_serfdom, ":serfdom"),
		  ##nested diplomacy start+
          (eq, ":random", 5),
          (val_add, ":mercantilism", ":change"),
			 (val_clamp, ":mercantilism", -3, 4),#-3 min, +3 max
          (faction_set_slot, ":kingdom", dplmc_slot_faction_mercantilism, ":mercantilism"),
		  ##nested diplomacy end+
        (try_end),
      (try_end),

    (else_try),

      #only player faction is affected by relation hits
      ##nested diplomacy start+
      ##Don't alter the values of centralization and aristocracy, since that's confusing.
      #(store_mul, ":centralization", ":centralization", -1),
      #(store_mul, ":aristocracy", ":aristocracy", 1),
      #(store_add, ":relation_change", ":centralization", ":aristocracy"),

		(store_sub, ":relation_change", ":aristocracy", ":centralization"),
      ##custodian (merchant) lords like plutocracy, unlike ordinary lords
      (store_mul, ":custodian_change", ":aristocracy", -1),
		(val_sub, ":custodian_change", ":centralization"),
      #benefactor lords like freedom and dislike serfdom
		(store_mul, ":benefactor_change", ":serfdom", -1),
		(val_sub, ":custodian_change", ":centralization"),
      ##nested diplomacy end+           
      (try_begin),
        ##nested diplomacy start+
        (this_or_next|neq, ":benefactor_change", 0),
        (this_or_next|neq, ":custodian_change", 0),
        ##nested diplomacy end+
        (neq, ":relation_change", 0),

        (try_begin),
          (eq, "$cheat_mode", 1),
          (str_store_faction_name, s9, ":kingdom"),
          (assign, reg1, ":relation_change"),
          (display_message, "@{!}DEBUG - relation_change =  {reg1} for {s9}"),
        (try_end),

        ##diplomacy start+ also include kingdom ladies who are kingdom heroes
        #(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
        (try_for_range, ":troop_no", heroes_begin, heroes_end),
        ##diplomacy end+
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (store_troop_faction, ":faction_no", ":troop_no"),
          (eq, ":kingdom", ":faction_no"),
          (faction_get_slot, ":faction_leader", ":kingdom", slot_faction_leader),
          ##diplomacy start+
          (neq, ":troop_no", ":faction_leader"),
          (assign, ":change_for_troop", ":relation_change"),
          (try_begin),
             (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_custodian),
             (assign, ":change_for_troop", ":custodian_change"),
          (else_try),
             (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_benefactor),
             (assign, ":change_for_troop", ":benefactor_change"),
          (try_end),
          ##Extra penalty for going back on a promise, extra bonus for keeping it
          (assign, ":promise_mod", 0),
          (try_begin),
             ##Following are only relevant for companions
				 (is_between, ":troop_no", companions_begin, companions_end),
             (troop_slot_eq, ":troop_no", slot_troop_kingsupport_state, 1),
             (try_begin),
                #Argument: Lords
                (troop_slot_eq, ":troop_no", slot_troop_kingsupport_argument, argument_lords),
                (try_begin),
                  #If more than slightly centralized, or more than slightly balanced against aristocrats  
                  (this_or_next|neg|faction_slot_ge, ":faction_no", dplmc_slot_faction_aristocracy, -1),
                     (faction_slot_ge, ":faction_no", dplmc_slot_faction_centralization, 2),
                  (val_sub, ":promise_mod", 1),
                (else_try),
                  #If more than slightly decentralized or more than slightly balanced in favor of aristocrats
                  (this_or_next|faction_slot_ge, ":faction_no", dplmc_slot_faction_aristocracy, 2),
                  (neg|faction_slot_ge, ":faction_no", dplmc_slot_faction_centralization, -2),
                  (faction_slot_ge, ":faction_no", dplmc_slot_faction_aristocracy, -1),#redundant
                  (val_add, ":promise_mod", 1),
                (try_end),
             (else_try),
                  #Argument: Commons
                  (troop_slot_eq, ":troop_no", slot_troop_kingsupport_argument, argument_commons),
                  (try_begin),
                    (faction_slot_ge, ":faction_no", dplmc_slot_faction_serfdom, 2),
                    (val_sub, ":promise_mod", 1),
                  (else_try),
                    (neg|faction_slot_ge, ":faction_no", dplmc_slot_faction_serfdom, 0),
                    (store_add, ":local_temp", ":serfdom", ":aristocracy"),
                    (lt, ":local_temp", 0),
                    (val_add, ":promise_mod", 1),
                  (try_end),
             (try_end),
         (try_end),
         #Check other broken promises
         (try_begin),
             (troop_slot_eq, ":troop_no", slot_lord_recruitment_argument, argument_lords),
             (this_or_next|neg|faction_slot_ge, ":faction_no", dplmc_slot_faction_aristocracy, -1),
                (faction_slot_ge, ":faction_no", dplmc_slot_faction_centralization, 2),
             #Lord must actually have cared about argument
             (neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
             (neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
             (val_sub, ":promise_mod", 1),
         (else_try),
             (troop_slot_eq, ":troop_no", slot_lord_recruitment_argument, argument_commons),
             (faction_slot_ge, ":faction_no", dplmc_slot_faction_serfdom, 2),
             #Lord must actually have cared about argument
             (neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
             (neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
             (neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
             (val_sub, ":promise_mod", 1),
         (try_end),
         (val_clamp, ":promise_mod", -1, 2),#-1, 0, or 1
         (val_add, ":change_for_troop", ":promise_mod"),
         
		 (neq, ":change_for_troop", 0),
		 (call_script, "script_change_player_relation_with_troop", ":troop_no", ":change_for_troop"),
        ##diplomacy end+
        (try_end),
      (try_end),
    (try_end),
  (try_end),
  ]),
]
