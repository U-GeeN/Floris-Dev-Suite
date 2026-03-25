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

scripts_part2 = [

    
    #script_multiplayer_event_mission_end
    # Input: none
    # Output: none
    ("multiplayer_event_mission_end",
      [
        #EVERY_BREATH_YOU_TAKE achievement
        (try_begin),
          (multiplayer_get_my_player, ":my_player_no"),
          (is_between, ":my_player_no", 0, multiplayer_max_possible_player_id),
          (player_get_kill_count, ":kill_count", ":my_player_no"),
          (player_get_death_count, ":death_count", ":my_player_no"),
          (gt, ":kill_count", ":death_count"),
          (unlock_achievement, ACHIEVEMENT_EVERY_BREATH_YOU_TAKE),
        (try_end),
        #EVERY_BREATH_YOU_TAKE achievement end
    ]),
    
    
    #script_multiplayer_event_agent_killed_or_wounded
    # Input: arg1 = dead_agent_no, arg2 = killer_agent_no
    # Output: none
    ("multiplayer_event_agent_killed_or_wounded",
      [
        (store_script_param, ":dead_agent_no", 1),
        (store_script_param, ":killer_agent_no", 2),
        
        (multiplayer_get_my_player, ":my_player_no"),
        (try_begin),
          (is_between, ":my_player_no", 0, multiplayer_max_possible_player_id),
          (player_get_agent_id, ":my_player_agent", ":my_player_no"),
          (ge, ":my_player_agent", 0),
          (try_begin),
            (eq, ":my_player_agent", ":dead_agent_no"),
            (store_mission_timer_a, "$g_multiplayer_respawn_start_time"),
          (try_end),
          (try_begin),
            (eq, ":my_player_agent", ":killer_agent_no"),
            (neq, ":my_player_agent", ":dead_agent_no"),
            (agent_is_human, ":dead_agent_no"),
            (agent_is_alive, ":my_player_agent"),
            (neg|agent_is_ally, ":dead_agent_no"),
            (agent_get_horse, ":my_horse_agent", ":my_player_agent"),
            (agent_get_wielded_item, ":my_wielded_item", ":my_player_agent", 0),
            (assign, ":my_item_class", -1),
            (try_begin),
              (ge, ":my_wielded_item", 0),
              (item_get_slot, ":my_item_class", ":my_wielded_item", slot_item_multiplayer_item_class),
            (try_end),
            #SPOIL_THE_CHARGE achievement
            (try_begin),
              (lt, ":my_horse_agent", 0),
              (agent_get_horse, ":dead_agent_horse_agent", ":dead_agent_no"),
              (ge, ":dead_agent_horse_agent", 0),
              (get_achievement_stat, ":achievement_stat", ACHIEVEMENT_SPOIL_THE_CHARGE, 0),
              (lt, ":achievement_stat", 50),
              (val_add, ":achievement_stat", 1),
              (set_achievement_stat, ACHIEVEMENT_SPOIL_THE_CHARGE, 0, ":achievement_stat"),
              (ge, ":achievement_stat", 50),
              (unlock_achievement, ACHIEVEMENT_SPOIL_THE_CHARGE),
            (try_end),
            #SPOIL_THE_CHARGE achievement end
            #HARASSING_HORSEMAN achievement
            (try_begin),
              (ge, ":my_horse_agent", 0),
              (this_or_next|eq, ":my_item_class", multi_item_class_type_bow),
              (this_or_next|eq, ":my_item_class", multi_item_class_type_crossbow),
              (this_or_next|eq, ":my_item_class", multi_item_class_type_throwing),
              (eq, ":my_item_class", multi_item_class_type_throwing_axe),
              (get_achievement_stat, ":achievement_stat", ACHIEVEMENT_HARASSING_HORSEMAN, 0),
              (lt, ":achievement_stat", 100),
              (val_add, ":achievement_stat", 1),
              (set_achievement_stat, ACHIEVEMENT_HARASSING_HORSEMAN, 0, ":achievement_stat"),
              (ge, ":achievement_stat", 100),
              (unlock_achievement, ACHIEVEMENT_HARASSING_HORSEMAN),
            (try_end),
            #HARASSING_HORSEMAN achievement end
            #THROWING_STAR achievement
            (try_begin),
              (this_or_next|eq, ":my_item_class", multi_item_class_type_throwing),
              (eq, ":my_item_class", multi_item_class_type_throwing_axe),
              (get_achievement_stat, ":achievement_stat", ACHIEVEMENT_THROWING_STAR, 0),
              (lt, ":achievement_stat", 25),
              (val_add, ":achievement_stat", 1),
              (set_achievement_stat, ACHIEVEMENT_THROWING_STAR, 0, ":achievement_stat"),
              (ge, ":achievement_stat", 25),
              (unlock_achievement, ACHIEVEMENT_THROWING_STAR),
            (try_end),
            #THROWING_STAR achievement end
            #SHISH_KEBAB achievement
            (try_begin),
              (ge, ":my_horse_agent", 0),
              (eq, ":my_item_class", multi_item_class_type_lance),
              (get_achievement_stat, ":achievement_stat", ACHIEVEMENT_SHISH_KEBAB, 0),
              (lt, ":achievement_stat", 25),
              (val_add, ":achievement_stat", 1),
              (set_achievement_stat, ACHIEVEMENT_SHISH_KEBAB, 0, ":achievement_stat"),
              (ge, ":achievement_stat", 25),
              (unlock_achievement, ACHIEVEMENT_SHISH_KEBAB),
            (try_end),
            #SHISH_KEBAB achievement end
            #CHOPPY_CHOP_CHOP achievement
            (try_begin),
              (this_or_next|eq, ":my_item_class", multi_item_class_type_sword),
              (this_or_next|eq, ":my_item_class", multi_item_class_type_axe),
              (this_or_next|eq, ":my_item_class", multi_item_class_type_cleavers),
              (this_or_next|eq, ":my_item_class", multi_item_class_type_two_handed_sword),
              (this_or_next|eq, ":my_item_class", multi_item_class_type_two_handed_axe),
              (this_or_next|eq, ":my_wielded_item", "itm_we_sar_axe_onehanded"), #sarranid item exception
              (this_or_next|eq, ":my_wielded_item", "itm_we_sar_axe_battle"), #sarranid item exception
              (eq, ":my_wielded_item", "itm_we_sar_axe_wariron"), #sarranid item exception
              (neq, ":my_wielded_item", "itm_we_sar_axe_war"), #sarranid item exception
              (neq, ":my_wielded_item", "itm_we_sar_axe_battle"), #sarranid item exception
              (get_achievement_stat, ":achievement_stat", ACHIEVEMENT_CHOPPY_CHOP_CHOP, 0),
              (lt, ":achievement_stat", 50),
              (val_add, ":achievement_stat", 1),
              (set_achievement_stat, ACHIEVEMENT_CHOPPY_CHOP_CHOP, 0, ":achievement_stat"),
              (ge, ":achievement_stat", 50),
              (unlock_achievement, ACHIEVEMENT_CHOPPY_CHOP_CHOP),
            (try_end),
            #CHOPPY_CHOP_CHOP achievement end
            #MACE_IN_YER_FACE achievement
            (try_begin),
              (this_or_next|eq, ":my_item_class", multi_item_class_type_blunt),
              (eq, ":my_wielded_item", "itm_we_sar_blunt_mace_ironlong"), #sarranid item exception
              (neq, ":my_wielded_item", "itm_we_sar_blunt_club"), #sarranid item exception
              (neq, ":my_wielded_item", "itm_we_sar_blunt_maceiron"), #sarranid item exception
              (neq, ":my_wielded_item", "itm_we_sar_blunt_maceflanged"), #sarranid item exception
              (neq, ":my_wielded_item", "itm_we_sar_blunt_macespiked"), #sarranid item exception
              (neq, ":my_wielded_item", "itm_we_sar_blunt_maceknobbedlong"), #sarranid item exception
              (neq, ":my_wielded_item", "itm_we_sar_blunt_macespikedlong"), #sarranid item exception
              (get_achievement_stat, ":achievement_stat", ACHIEVEMENT_MACE_IN_YER_FACE, 0),
              (lt, ":achievement_stat", 25),
              (val_add, ":achievement_stat", 1),
              (set_achievement_stat, ACHIEVEMENT_MACE_IN_YER_FACE, 0, ":achievement_stat"),
              (ge, ":achievement_stat", 25),
              (unlock_achievement, ACHIEVEMENT_MACE_IN_YER_FACE),
            (try_end),
            #MACE_IN_YER_FACE achievement end
            #THE_HUSCARL achievement
            (try_begin),
              (eq, ":my_item_class", multi_item_class_type_throwing_axe),
              (get_achievement_stat, ":achievement_stat", ACHIEVEMENT_THE_HUSCARL, 0),
              (lt, ":achievement_stat", 50),
              (val_add, ":achievement_stat", 1),
              (set_achievement_stat, ACHIEVEMENT_THE_HUSCARL, 0, ":achievement_stat"),
              (ge, ":achievement_stat", 50),
              (unlock_achievement, ACHIEVEMENT_THE_HUSCARL),
            (try_end),
            #THE_HUSCARL achievement end
          (try_end),
        (try_end),
        
        (try_begin),
          (is_between, ":my_player_no", 0, multiplayer_max_possible_player_id),
          (player_get_agent_id, ":player_agent", ":my_player_no"),
          (eq, ":dead_agent_no", ":player_agent"),
          
          (assign, ":show_respawn_counter", 0),
          (try_begin),
            #TODO: add other game types with no respawns here
            (neq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
            (neq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
            (assign, ":show_respawn_counter", 1),
          (else_try),
            (eq, "$g_multiplayer_player_respawn_as_bot", 1),
            (player_get_team_no, ":my_player_team", ":my_player_no"),
            (assign, ":is_found", 0),
            (try_for_agents, ":cur_agent"),
              (eq, ":is_found", 0),
              (agent_is_alive, ":cur_agent"),
              (agent_is_human, ":cur_agent"),
              (agent_is_non_player, ":cur_agent"),
              (agent_get_team ,":cur_team", ":cur_agent"),
              (eq, ":cur_team", ":my_player_team"),
              (assign, ":is_found", 1),
            (try_end),
            (eq, ":is_found", 1),
            (assign, ":show_respawn_counter", 1),
          (try_end),
          
          (try_begin),
            #(player_get_slot, ":spawn_count", ":player_no", slot_player_spawn_count),
            (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
            (gt, "$g_multiplayer_number_of_respawn_count", 0),
            
            (ge, "$g_my_spawn_count", "$g_multiplayer_number_of_respawn_count"),
            
            (multiplayer_get_my_player, ":my_player_no"),
            (player_get_team_no, ":my_player_team", ":my_player_no"),
            
            (this_or_next|eq, ":my_player_team", 0),
            (ge, "$g_my_spawn_count", 999),
            
            (assign, "$g_show_no_more_respawns_remained", 1),
          (else_try),
            (assign, "$g_show_no_more_respawns_remained", 0),
          (try_end),
          
          (eq, ":show_respawn_counter", 1),
          
          (start_presentation, "prsnt_multiplayer_respawn_time_counter"),
        (try_end),
    ]),
    
    #script_multiplayer_get_item_value_for_troop
    # Input: arg1 = item_no, arg2 = troop_no
    # Output: reg0: item_value
    ("multiplayer_get_item_value_for_troop",
      [
        (store_script_param, ":item_no", 1),
        (store_script_param, ":troop_no", 2),
        (try_begin),
          (call_script, "script_cf_multiplayer_is_item_default_for_troop", ":item_no", ":troop_no"),
          (assign, ":item_value", 0),
        (else_try),
          (store_item_value, ":item_value", ":item_no"),
          (store_troop_faction, ":faction_no", ":troop_no"),
          (store_sub, ":faction_slot", ":faction_no", npc_kingdoms_begin),
          (val_add, ":faction_slot", slot_item_multiplayer_faction_price_multipliers_begin),
          (item_get_slot, ":price_multiplier", ":item_no", ":faction_slot"),
          (val_mul, ":item_value", ":price_multiplier"),
          (val_div, ":item_value", 100),
        (try_end),
        (assign, reg0, ":item_value"),
    ]),
    
    #script_multiplayer_get_previous_item_for_item_and_troop
    # Input: arg1 = item_no, arg2 = troop_no
    # Output: reg0: previous_item_no (-1 if it is the root item, 0 if the item is invalid)
    ("multiplayer_get_previous_item_for_item_and_troop",
      [
        (store_script_param, ":item_no", 1),
        (store_script_param, ":troop_no", 2),
        (item_get_slot, ":item_class", ":item_no", slot_item_multiplayer_item_class),
        (call_script, "script_multiplayer_get_item_value_for_troop", ":item_no", ":troop_no"),
        (assign, ":item_value", reg0),
        (store_sub, ":troop_index", ":troop_no", multiplayer_troops_begin),
        (val_add, ":troop_index", slot_item_multiplayer_availability_linked_list_begin),
        (assign, ":max_item_no", -1),
        (assign, ":max_item_value", -1),
        (try_for_range, ":i_item", all_items_begin, all_items_end),
          (item_slot_eq, ":i_item", slot_item_multiplayer_item_class, ":item_class"),
          (item_slot_ge, ":i_item", ":troop_index", 1),
          (call_script, "script_multiplayer_get_item_value_for_troop", ":i_item", ":troop_no"),
          (assign, ":i_item_value", reg0),
          (try_begin),
            (eq, ":i_item_value", 0),
            (eq, ":max_item_value", 0),
            #choose between 2 default items
            (store_item_value, ":i_item_real_value", ":i_item"),
            (store_item_value, ":max_item_real_value", ":max_item_no"),
            (try_begin),
              (gt, ":i_item_real_value", ":max_item_real_value"),
              (assign, ":max_item_value", ":i_item_value"),
              (assign, ":max_item_no", ":i_item"),
            (try_end),
          (else_try),
            (gt, ":i_item_value", ":max_item_value"),
            (lt, ":i_item_value", ":item_value"),
            (assign, ":max_item_value", ":i_item_value"),
            (assign, ":max_item_no", ":i_item"),
          (try_end),
        (try_end),
        (try_begin),
          (eq, ":max_item_no", -1),
          (assign, ":item_upper_class", -1),
          (try_begin),
            (is_between, ":item_class", multi_item_class_type_melee_weapons_begin, multi_item_class_type_melee_weapons_end),
            (assign, ":item_upper_class", 0),
          (else_try),
            (is_between, ":item_class", multi_item_class_type_shields_begin, multi_item_class_type_shields_end),
            (assign, ":item_upper_class", 1),
          (else_try),
            (eq, ":item_class", multi_item_class_type_bow),
            (assign, ":item_upper_class", 2),
          (else_try),
            (eq, ":item_class", multi_item_class_type_crossbow),
            (assign, ":item_upper_class", 3),
          (else_try),
            (eq, ":item_class", multi_item_class_type_arrow),
            (assign, ":item_upper_class", 4),
          (else_try),
            (eq, ":item_class", multi_item_class_type_bolt),
            (assign, ":item_upper_class", 5),
          (else_try),
            (eq, ":item_class", multi_item_class_type_throwing),
            (assign, ":item_upper_class", 6),
          (else_try),
            (is_between, ":item_class", multi_item_class_type_heads_begin, multi_item_class_type_heads_end),
            (assign, ":item_upper_class", 7),
          (else_try),
            (is_between, ":item_class", multi_item_class_type_bodies_begin, multi_item_class_type_bodies_end),
            (assign, ":item_upper_class", 8),
          (else_try),
            (is_between, ":item_class", multi_item_class_type_feet_begin, multi_item_class_type_feet_end),
            (assign, ":item_upper_class", 9),
          (else_try),
            (is_between, ":item_class", multi_item_class_type_gloves_begin, multi_item_class_type_gloves_end),
            (assign, ":item_upper_class", 10),
          (else_try),
            (is_between, ":item_class", multi_item_class_type_horses_begin, multi_item_class_type_horses_end),
            (assign, ":item_upper_class", 11),
          (try_end),
          (neq, ":item_upper_class", 0),
          #search for the default item for non-weapon classes (only 1 slot is easy to fill)
          (assign, ":end_cond", all_items_end),
          (try_for_range, ":i_item", all_items_begin, ":end_cond"),
            (item_slot_ge, ":i_item", ":troop_index", 1),
            (item_get_slot, ":i_item_class", ":i_item", slot_item_multiplayer_item_class),
            (try_begin),
              (is_between, ":i_item_class", multi_item_class_type_melee_weapons_begin, multi_item_class_type_melee_weapons_end),
              (assign, ":i_item_upper_class", 0),
            (else_try),
              (is_between, ":i_item_class", multi_item_class_type_shields_begin, multi_item_class_type_shields_end),
              (assign, ":i_item_upper_class", 1),
            (else_try),
              (eq, ":i_item_class", multi_item_class_type_bow),
              (assign, ":i_item_upper_class", 2),
            (else_try),
              (eq, ":i_item_class", multi_item_class_type_crossbow),
              (assign, ":i_item_upper_class", 3),
            (else_try),
              (eq, ":i_item_class", multi_item_class_type_arrow),
              (assign, ":i_item_upper_class", 4),
            (else_try),
              (eq, ":i_item_class", multi_item_class_type_bolt),
              (assign, ":i_item_upper_class", 5),
            (else_try),
              (eq, ":i_item_class", multi_item_class_type_throwing),
              (assign, ":i_item_upper_class", 6),
            (else_try),
              (is_between, ":i_item_class", multi_item_class_type_heads_begin, multi_item_class_type_heads_end),
              (assign, ":i_item_upper_class", 7),
            (else_try),
              (is_between, ":i_item_class", multi_item_class_type_bodies_begin, multi_item_class_type_bodies_end),
              (assign, ":i_item_upper_class", 8),
            (else_try),
              (is_between, ":i_item_class", multi_item_class_type_feet_begin, multi_item_class_type_feet_end),
              (assign, ":i_item_upper_class", 9),
            (else_try),
              (is_between, ":i_item_class", multi_item_class_type_gloves_begin, multi_item_class_type_gloves_end),
              (assign, ":i_item_upper_class", 10),
            (else_try),
              (is_between, ":i_item_class", multi_item_class_type_horses_begin, multi_item_class_type_horses_end),
              (assign, ":i_item_upper_class", 11),
            (try_end),
            (eq, ":i_item_upper_class", ":item_upper_class"),
            (call_script, "script_cf_multiplayer_is_item_default_for_troop", ":i_item", ":troop_no"),
            (assign, ":max_item_no", ":i_item"),
            (assign, ":end_cond", 0), #break
          (try_end),
        (try_end),
        (assign, reg0, ":max_item_no"),
    ]),
    
    #script_cf_multiplayer_is_item_default_for_troop
    # Input: arg1 = item_no, arg2 = troop_no
    # Output: reg0: total_cost
    ("cf_multiplayer_is_item_default_for_troop",
      [
        (store_script_param, ":item_no", 1),
        (store_script_param, ":troop_no", 2),
        (assign, ":default_item", 0),
        (try_begin),
          (neg|is_between, ":item_no", horses_begin, horses_end),
          
          (troop_get_inventory_capacity, ":end_cond", ":troop_no"), #troop no can come -1 here error occured at friday
          (try_for_range, ":i_slot", 0, ":end_cond"),
            (troop_get_inventory_slot, ":default_item_id", ":troop_no", ":i_slot"),
            (eq, ":item_no", ":default_item_id"),
            (assign, ":default_item", 1),
            (assign, ":end_cond", 0), #break
          (try_end),
        (try_end),
        (eq, ":default_item", 1),
    ]),
    
    #script_multiplayer_calculate_cur_selected_items_cost
    # Input: arg1 = player_no
    # Output: reg0: total_cost
    ("multiplayer_calculate_cur_selected_items_cost",
      [
        (store_script_param, ":player_no", 1),
        (store_script_param, ":calculation_type", 2), #0 for normal calculation
        (assign, ":total_cost", 0),
        (player_get_troop_id, ":troop_no", ":player_no"),
        
        (try_begin),
          (eq, ":calculation_type", 0),
          (assign, ":begin_cond", slot_player_cur_selected_item_indices_begin),
          (assign, ":end_cond", slot_player_cur_selected_item_indices_end),
        (else_try),
          (assign, ":begin_cond", slot_player_selected_item_indices_begin),
          (assign, ":end_cond", slot_player_selected_item_indices_end),
        (try_end),
        
        (try_for_range, ":i_item", ":begin_cond", ":end_cond"),
          (player_get_slot, ":item_id", ":player_no", ":i_item"),
          (ge, ":item_id", 0), #might be -1 for horses etc.
          (call_script, "script_multiplayer_get_item_value_for_troop", ":item_id", ":troop_no"),
          (val_add, ":total_cost", reg0),
        (try_end),
        (assign, reg0, ":total_cost"),
    ]),
    
    #script_multiplayer_set_item_available_for_troop
    # Input: arg1 = item_no, arg2 = troop_no
    # Output: none
    ("multiplayer_set_item_available_for_troop",
      [
        (store_script_param, ":item_no", 1),
        (store_script_param, ":troop_no", 2),
        (store_sub, ":item_troop_slot", ":troop_no", multiplayer_troops_begin),
        (val_add, ":item_troop_slot", slot_item_multiplayer_availability_linked_list_begin),
        (item_set_slot, ":item_no", ":item_troop_slot", 1),
    ]),
    
    #script_multiplayer_send_item_selections
    # Input: none
    # Output: none
    ("multiplayer_send_item_selections",
      [
        (multiplayer_get_my_player, ":my_player_no"),
        (try_for_range, ":i_item", slot_player_selected_item_indices_begin, slot_player_selected_item_indices_end),
          (player_get_slot, ":item_id", ":my_player_no", ":i_item"),
          (multiplayer_send_2_int_to_server, multiplayer_event_set_item_selection, ":i_item", ":item_id"),
        (try_end),
    ]),
    
    #script_multiplayer_set_default_item_selections_for_troop
    # Input: arg1 = troop_no
    # Output: none
    ("multiplayer_set_default_item_selections_for_troop",
      [
        (store_script_param, ":troop_no", 1),
        (multiplayer_get_my_player, ":my_player_no"),
        (call_script, "script_multiplayer_clear_player_selected_items", ":my_player_no"),
        (assign, ":cur_weapon_slot", 0),
        (troop_get_inventory_capacity, ":inv_cap", ":troop_no"),
        (try_for_range, ":i_slot", 0, ":inv_cap"),
          (troop_get_inventory_slot, ":item_id", ":troop_no", ":i_slot"),
          (ge, ":item_id", 0),
          (item_get_slot, ":item_class", ":item_id", slot_item_multiplayer_item_class),
          (try_begin),
            (is_between, ":item_class", multi_item_class_type_weapons_begin, multi_item_class_type_weapons_end),
            (this_or_next|eq, "$g_multiplayer_disallow_ranged_weapons", 0),
            (neg|is_between, ":item_class", multi_item_class_type_ranged_weapons_begin, multi_item_class_type_ranged_weapons_end),
            (store_add, ":selected_item_slot", slot_player_selected_item_indices_begin, ":cur_weapon_slot"),
            (player_set_slot, ":my_player_no", ":selected_item_slot", ":item_id"),
            (val_add, ":cur_weapon_slot", 1),
          (else_try),
            (is_between, ":item_class", multi_item_class_type_heads_begin, multi_item_class_type_heads_end),
            (store_add, ":selected_item_slot", slot_player_selected_item_indices_begin, 4),
            (player_set_slot, ":my_player_no", ":selected_item_slot", ":item_id"),
          (else_try),
            (is_between, ":item_class", multi_item_class_type_bodies_begin, multi_item_class_type_bodies_end),
            (store_add, ":selected_item_slot", slot_player_selected_item_indices_begin, 5),
            (player_set_slot, ":my_player_no", ":selected_item_slot", ":item_id"),
          (else_try),
            (is_between, ":item_class", multi_item_class_type_feet_begin, multi_item_class_type_feet_end),
            (store_add, ":selected_item_slot", slot_player_selected_item_indices_begin, 6),
            (player_set_slot, ":my_player_no", ":selected_item_slot", ":item_id"),
          (else_try),
            (is_between, ":item_class", multi_item_class_type_gloves_begin, multi_item_class_type_gloves_end),
            (store_add, ":selected_item_slot", slot_player_selected_item_indices_begin, 7),
            (player_set_slot, ":my_player_no", ":selected_item_slot", ":item_id"),
          (else_try),
            (is_between, ":item_class", multi_item_class_type_horses_begin, multi_item_class_type_horses_end),
            (eq, "$g_horses_are_avaliable", 1),
            (store_add, ":selected_item_slot", slot_player_selected_item_indices_begin, 8),
            (player_set_slot, ":my_player_no", ":selected_item_slot", ":item_id"),
          (try_end),
        (try_end),
    ]),
    
    #script_multiplayer_display_available_items_for_troop_and_item_classes
    # Input: arg1 = troop_no, arg2 = item_classes_begin, arg3 = item_classes_end, arg4 = pos_x_begin, arg5 = pos_y_begin
    # Output: none
    ("multiplayer_display_available_items_for_troop_and_item_classes",
      [
        (store_script_param, ":troop_no", 1),
        (store_script_param, ":item_classes_begin", 2),
        (store_script_param, ":item_classes_end", 3),
        (store_script_param, ":pos_x_begin", 4),
        (store_script_param, ":pos_y_begin", 5),
        
        (assign, ":x_adder", 100),
        (try_begin),
          (gt, ":pos_x_begin", 500),
          (assign, ":x_adder", -100),
        (try_end),
        
        (store_sub, ":item_troop_slot", ":troop_no", multiplayer_troops_begin),
        (val_add, ":item_troop_slot", slot_item_multiplayer_availability_linked_list_begin),
        
        (try_for_range, ":cur_slot", multi_data_item_button_indices_begin, multi_data_item_button_indices_end),
          (troop_set_slot, "trp_multiplayer_data", ":cur_slot", -1),
        (try_end),
        
        (assign, ":num_available_items", 0),
        
        (try_for_range, ":item_no", all_items_begin, all_items_end),
          (item_get_slot, ":item_class", ":item_no", slot_item_multiplayer_item_class),
          (is_between, ":item_class", ":item_classes_begin", ":item_classes_end"),
          (this_or_next|eq, "$g_multiplayer_disallow_ranged_weapons", 0),
          (neg|is_between, ":item_class", multi_item_class_type_ranged_weapons_begin, multi_item_class_type_ranged_weapons_end),
          (item_slot_ge, ":item_no", ":item_troop_slot", 1),
          (store_add, ":cur_slot_index", ":num_available_items", multi_data_item_button_indices_begin),
          #using the result array for item_ids
          (troop_set_slot, "trp_multiplayer_data", ":cur_slot_index", ":item_no"),
          (val_add, ":num_available_items", 1),
        (try_end),
        
        #sorting
        (store_add, ":item_slots_end", ":num_available_items", multi_data_item_button_indices_begin),
        (store_sub, ":item_slots_end_minus_one", ":item_slots_end", 1),
        (try_for_range, ":cur_slot", multi_data_item_button_indices_begin, ":item_slots_end_minus_one"),
          (store_add, ":cur_slot_2_begin", ":cur_slot", 1),
          (try_for_range, ":cur_slot_2", ":cur_slot_2_begin", ":item_slots_end"),
            (troop_get_slot, ":item_1", "trp_multiplayer_data", ":cur_slot"),
            (troop_get_slot, ":item_2", "trp_multiplayer_data", ":cur_slot_2"),
            (call_script, "script_multiplayer_get_item_value_for_troop", ":item_1", ":troop_no"),
            (assign, ":item_1_point", reg0),
            (call_script, "script_multiplayer_get_item_value_for_troop", ":item_2", ":troop_no"),
            (assign, ":item_2_point", reg0),
            (item_get_slot, ":item_1_class", ":item_1", slot_item_multiplayer_item_class),
            (item_get_slot, ":item_2_class", ":item_2", slot_item_multiplayer_item_class),
            (val_mul, ":item_1_class", 1000000), #assuming maximum item price is 1000000
            (val_mul, ":item_2_class", 1000000), #assuming maximum item price is 1000000
            (val_add, ":item_1_point", ":item_1_class"),
            (val_add, ":item_2_point", ":item_2_class"),
            (lt, ":item_2_point", ":item_1_point"),
            (troop_set_slot, "trp_multiplayer_data", ":cur_slot", ":item_2"),
            (troop_set_slot, "trp_multiplayer_data", ":cur_slot_2", ":item_1"),
          (try_end),
        (try_end),
        
        (troop_get_slot, ":last_item_no", "trp_multiplayer_data", multi_data_item_button_indices_begin),
        (assign, ":num_item_classes", 0),
        (try_begin),
          (ge, ":last_item_no", 0),
          (item_get_slot, ":last_item_class", ":last_item_no", slot_item_multiplayer_item_class),
          
          (try_for_range, ":cur_slot", multi_data_item_button_indices_begin, ":item_slots_end"),
            (troop_get_slot, ":item_no", "trp_multiplayer_data", ":cur_slot"),
            (item_get_slot, ":item_class", ":item_no", slot_item_multiplayer_item_class),
            (neq, ":item_class", ":last_item_class"),
            (val_add, ":num_item_classes", 1),
            (assign, ":last_item_class", ":item_class"),
          (try_end),
          
          (try_begin),
            (store_mul, ":required_y", ":num_item_classes", 100),
            (gt, ":required_y", ":pos_y_begin"),
            (store_sub, ":dif", ":required_y", ":pos_y_begin"),
            (val_div, ":dif", 100),
            (val_add, ":dif", 1),
            (val_mul, ":dif", 100),
            (val_add, ":pos_y_begin", ":dif"),
          (try_end),
          
          (item_get_slot, ":last_item_class", ":last_item_no", slot_item_multiplayer_item_class),
        (try_end),
        (assign, ":cur_x", ":pos_x_begin"),
        (assign, ":cur_y", ":pos_y_begin"),
        (try_for_range, ":cur_slot", multi_data_item_button_indices_begin, ":item_slots_end"),
          (troop_get_slot, ":item_no", "trp_multiplayer_data", ":cur_slot"),
          (item_get_slot, ":item_class", ":item_no", slot_item_multiplayer_item_class),
          (try_begin),
            (neq, ":item_class", ":last_item_class"),
            (val_sub, ":cur_y", 100),
            (assign, ":cur_x", ":pos_x_begin"),
            (assign, ":last_item_class", ":item_class"),
          (try_end),
          (create_image_button_overlay, ":cur_obj", "mesh_mp_inventory_choose", "mesh_mp_inventory_choose"),
          (position_set_x, pos1, 800),
          (position_set_y, pos1, 800),
          (overlay_set_size, ":cur_obj", pos1),
          (position_set_x, pos1, ":cur_x"),
          (position_set_y, pos1, ":cur_y"),
          (overlay_set_position, ":cur_obj", pos1),
          (create_mesh_overlay_with_item_id, reg0, ":item_no"),
          (store_add, ":item_x", ":cur_x", 50),
          (store_add, ":item_y", ":cur_y", 50),
          (position_set_x, pos1, ":item_x"),
          (position_set_y, pos1, ":item_y"),
          (overlay_set_position, reg0, pos1),
          (val_add, ":cur_x", ":x_adder"),
        (try_end),
    ]),
    
    # script_multiplayer_fill_map_game_types
    # Input: game_type
    # Output: num_maps
    ("multiplayer_fill_map_game_types",
    [
      (store_script_param, ":game_type", 1),
      (try_for_range, ":i_multi", multi_data_maps_for_game_type_begin, multi_data_maps_for_game_type_end),
        (troop_set_slot, "trp_multiplayer_data", ":i_multi", -1),
      (try_end),
      (assign, ":num_maps", 0),
      (try_begin),
        (this_or_next|eq, ":game_type", multiplayer_game_type_deathmatch),
        (this_or_next|eq, ":game_type", multiplayer_game_type_duel),
        (eq, ":game_type", multiplayer_game_type_team_deathmatch),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin, "scn_multi_scene_1"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 1, "scn_multi_scene_2"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 2, "scn_multi_scene_4"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 3, "scn_multi_scene_7"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 4, "scn_multi_scene_9"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 5, "scn_multi_scene_11"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 6, "scn_multi_scene_12"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 7, "scn_multi_scene_14"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 8, "scn_multi_scene_17"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 9, "scn_multi_scene_18"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 10, "scn_multi_scene_19"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 11, "scn_multi_scene_20"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 12, "scn_random_multi_plain_medium"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 13, "scn_random_multi_plain_large"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 14, "scn_random_multi_steppe_medium"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 15, "scn_random_multi_steppe_large"),
        (assign, ":num_maps", 16),
      (else_try),
        (eq, ":game_type", multiplayer_game_type_battle),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin, "scn_multi_scene_1"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 1, "scn_multi_scene_2"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 2, "scn_multi_scene_4"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 3, "scn_multi_scene_7"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 4, "scn_multi_scene_9"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 5, "scn_multi_scene_11"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 6, "scn_multi_scene_12"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 7, "scn_multi_scene_14"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 8, "scn_multi_scene_17"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 9, "scn_multi_scene_18"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 10, "scn_multi_scene_19"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 11, "scn_multi_scene_20"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 12, "scn_random_multi_plain_medium"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 13, "scn_random_multi_plain_large"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 14, "scn_random_multi_steppe_medium"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 15, "scn_random_multi_steppe_large"),
        (assign, ":num_maps", 16),
      (else_try),
        (eq, ":game_type", multiplayer_game_type_destroy),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin, "scn_multi_scene_1"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 1, "scn_multi_scene_2"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 2, "scn_multi_scene_4"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 3, "scn_multi_scene_7"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 4, "scn_multi_scene_9"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 5, "scn_multi_scene_12"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 6, "scn_multi_scene_14"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 7, "scn_multi_scene_19"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 8, "scn_multi_scene_20"),
        (assign, ":num_maps", 9),
      (else_try),
        (eq, ":game_type", multiplayer_game_type_capture_the_flag),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin, "scn_multi_scene_1"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 1, "scn_multi_scene_2"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 2, "scn_multi_scene_4"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 3, "scn_multi_scene_7"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 4, "scn_multi_scene_9"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 5, "scn_multi_scene_11"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 6, "scn_multi_scene_12"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 7, "scn_multi_scene_14"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 8, "scn_multi_scene_17"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 9, "scn_multi_scene_18"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 10, "scn_multi_scene_19"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 11, "scn_multi_scene_20"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 12, "scn_random_multi_plain_medium"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 13, "scn_random_multi_plain_large"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 14, "scn_random_multi_steppe_medium"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 15, "scn_random_multi_steppe_large"),
        (assign, ":num_maps", 16),
      (else_try),
        (eq, ":game_type", multiplayer_game_type_headquarters),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin, "scn_multi_scene_1"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 1, "scn_multi_scene_2"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 2, "scn_multi_scene_4"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 3, "scn_multi_scene_7"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 4, "scn_multi_scene_9"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 5, "scn_multi_scene_11"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 6, "scn_multi_scene_12"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 7, "scn_multi_scene_14"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 8, "scn_multi_scene_17"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 9, "scn_multi_scene_18"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 10, "scn_multi_scene_19"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 11, "scn_multi_scene_20"),
        (assign, ":num_maps", 12),
      (else_try),
        (eq, ":game_type", multiplayer_game_type_siege),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin, "scn_multi_scene_3"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 1, "scn_multi_scene_8"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 2, "scn_multi_scene_10"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 3, "scn_multi_scene_13"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 4, "scn_multi_scene_15"),
        (troop_set_slot, "trp_multiplayer_data", multi_data_maps_for_game_type_begin + 5, "scn_multi_scene_16"),
        (assign, ":num_maps", 6),
      (try_end),
      (assign, reg0, ":num_maps"),
      ]),
    
    
    # script_multiplayer_count_players_bots
    # Input: none
    # Output: none
    ("multiplayer_count_players_bots",
      [
        (get_max_players, ":num_players"),
        (try_for_range, ":cur_player", 0, ":num_players"),
          (player_is_active, ":cur_player"),
          (player_set_slot, ":cur_player", slot_player_last_bot_count, 0),
        (try_end),
        
        (try_for_agents, ":cur_agent"),
          (agent_is_human, ":cur_agent"),
          (agent_is_alive, ":cur_agent"),
          (agent_get_player_id, ":agent_player", ":cur_agent"),
          (lt, ":agent_player", 0), #not a player
          (agent_get_group, ":agent_group", ":cur_agent"),
          (player_is_active, ":agent_group"),
          (player_get_slot, ":bot_count", ":agent_group", slot_player_last_bot_count),
          (val_add, ":bot_count", 1),
          (player_set_slot, ":agent_group", slot_player_last_bot_count, ":bot_count"),
        (try_end),
    ]),
    
    # script_multiplayer_find_player_leader_for_bot
    # Input: arg1 = team_no
    # Output: reg0 = player_no
    ("multiplayer_find_player_leader_for_bot",
      [
        (store_script_param, ":team_no", 1),
        (store_script_param, ":look_only_actives", 2),
        
        (team_get_faction, ":team_faction", ":team_no"),
        (assign, ":num_ai_troops", 0),
        (try_for_range, ":cur_ai_troop", multiplayer_ai_troops_begin, multiplayer_ai_troops_end),
          (store_troop_faction, ":ai_troop_faction", ":cur_ai_troop"),
          (eq, ":ai_troop_faction", ":team_faction"),
          (val_add, ":num_ai_troops", 1),
        (try_end),
        
        (call_script, "script_multiplayer_count_players_bots"),
        
        (assign, ":team_player_count", 0),
        
        (get_max_players, ":num_players"),
        (try_for_range, ":cur_player", 0, ":num_players"),
          (assign, ":continue", 0),
          (player_is_active, ":cur_player"),
          (try_begin),
            (eq, ":look_only_actives", 0),
            (assign, ":continue", 1),
          (else_try),
            (neq, ":look_only_actives", 0),
            (player_get_agent_id, ":cur_agent", ":cur_player"),
            (ge, ":cur_agent", 0),
            (agent_is_alive, ":cur_agent"),
            (assign, ":continue", 1),
          (try_end),
          
          (eq, ":continue", 1),
          
          (player_get_team_no, ":player_team", ":cur_player"),
          (eq, ":team_no", ":player_team"),
          (val_add, ":team_player_count", 1),
        (try_end),
        (assign, ":result_leader", -1),
        (try_begin),
          (gt, ":team_player_count", 0),
          (assign, ":total_bot_count", "$g_multiplayer_num_bots_team_1"),
          (try_begin),
            (eq, ":team_no", 1),
            (assign, ":total_bot_count", "$g_multiplayer_num_bots_team_2"),
          (try_end),
          (store_div, ":num_bots_for_each_player", ":total_bot_count", ":team_player_count"),
          (store_mul, ":check_remainder", ":num_bots_for_each_player", ":team_player_count"),
          (try_begin),
            (lt, ":check_remainder", ":total_bot_count"),
            (val_add, ":num_bots_for_each_player", 1),
          (try_end),
          
          (assign, ":total_bot_req", 0),
          (try_for_range, ":cur_player", 0, ":num_players"),
            (player_is_active, ":cur_player"),
            
            (player_get_agent_id, ":cur_agent", ":cur_player"),
            (ge, ":cur_agent", 0),
            (agent_is_alive, ":cur_agent"),
            
            (player_get_team_no, ":player_team", ":cur_player"),
            (eq, ":team_no", ":player_team"),
            (assign, ":ai_wanted", 0),
            (store_add, ":end_cond", slot_player_bot_type_1_wanted, ":num_ai_troops"),
            (try_for_range, ":bot_type_wanted_slot", slot_player_bot_type_1_wanted, ":end_cond"),
              (player_slot_ge, ":cur_player", ":bot_type_wanted_slot", 1),
              (assign, ":ai_wanted", 1),
              (assign, ":end_cond", 0), #break
            (try_end),
            (eq, ":ai_wanted", 1),
            (player_get_slot, ":player_bot_count", ":cur_player", slot_player_last_bot_count),
            (lt, ":player_bot_count", ":num_bots_for_each_player"),
            (val_add, ":total_bot_req", ":num_bots_for_each_player"),
            (val_sub, ":total_bot_req", ":player_bot_count"),
          (try_end),
          (gt, ":total_bot_req", 0),
          
          (store_random_in_range, ":random_bot", 0, ":total_bot_req"),
          (try_for_range, ":cur_player", 0, ":num_players"),
            (player_is_active, ":cur_player"),
            
            (player_get_agent_id, ":cur_agent", ":cur_player"),
            (ge, ":cur_agent", 0),
            (agent_is_alive, ":cur_agent"),
            
            (player_get_team_no, ":player_team", ":cur_player"),
            (eq, ":team_no", ":player_team"),
            (assign, ":ai_wanted", 0),
            (store_add, ":end_cond", slot_player_bot_type_1_wanted, ":num_ai_troops"),
            (try_for_range, ":bot_type_wanted_slot", slot_player_bot_type_1_wanted, ":end_cond"),
              (player_slot_ge, ":cur_player", ":bot_type_wanted_slot", 1),
              (assign, ":ai_wanted", 1),
              (assign, ":end_cond", 0), #break
            (try_end),
            (eq, ":ai_wanted", 1),
            (player_get_slot, ":player_bot_count", ":cur_player", slot_player_last_bot_count),
            (lt, ":player_bot_count", ":num_bots_for_each_player"),
            (val_sub, ":random_bot", ":num_bots_for_each_player"),
            (val_add, ":random_bot", ":player_bot_count"),
            (lt, ":random_bot", 0),
            (assign, ":result_leader", ":cur_player"),
            (assign, ":num_players", 0), #break
          (try_end),
        (try_end),
        (assign, reg0, ":result_leader"),
    ]),
    
    # script_multiplayer_find_bot_troop_and_group_for_spawn
    # Input: arg1 = team_no
    # Output: reg0 = troop_id, reg1 = group_id
    ("multiplayer_find_bot_troop_and_group_for_spawn",
      [
        (store_script_param, ":team_no", 1),
        (store_script_param, ":look_only_actives", 2),
        
        (call_script, "script_multiplayer_find_player_leader_for_bot", ":team_no", ":look_only_actives"),
        (assign, ":leader_player", reg0),
        
        (assign, ":available_troops_in_faction", 0),
        (assign, ":available_troops_to_spawn", 0),
        (team_get_faction, ":team_faction_no", ":team_no"),
        
        (try_for_range, ":troop_no", multiplayer_ai_troops_begin, multiplayer_ai_troops_end),
          (store_troop_faction, ":troop_faction", ":troop_no"),
          (eq, ":troop_faction", ":team_faction_no"),
          (store_add, ":wanted_slot", slot_player_bot_type_1_wanted, ":available_troops_in_faction"),
          (val_add, ":available_troops_in_faction", 1),
          (try_begin),
            (this_or_next|lt, ":leader_player", 0),
            (player_slot_ge, ":leader_player", ":wanted_slot", 1),
            (val_add, ":available_troops_to_spawn", 1),
          (try_end),
        (try_end),
        
        (assign, ":available_troops_in_faction", 0),
        
        (store_random_in_range, ":random_troop_index", 0, ":available_troops_to_spawn"),
        (assign, ":end_cond", multiplayer_ai_troops_end),
        (try_for_range, ":troop_no", multiplayer_ai_troops_begin, ":end_cond"),
          (store_troop_faction, ":troop_faction", ":troop_no"),
          (eq, ":troop_faction", ":team_faction_no"),
          (store_add, ":wanted_slot", slot_player_bot_type_1_wanted, ":available_troops_in_faction"),
          (val_add, ":available_troops_in_faction", 1),
          (this_or_next|lt, ":leader_player", 0),
          (player_slot_ge, ":leader_player", ":wanted_slot", 1),
          (val_sub, ":random_troop_index", 1),
          (lt, ":random_troop_index", 0),
          (assign, ":end_cond", 0),
          (assign, ":selected_troop", ":troop_no"),
        (try_end),
        (assign, reg0, ":selected_troop"),
        (assign, reg1, ":leader_player"),
    ]),
    
    # script_multiplayer_change_leader_of_bot
    # Input: arg1 = agent_no
    # Output: none
    ("multiplayer_change_leader_of_bot",
      [
        (store_script_param, ":agent_no", 1),
        (agent_get_team, ":team_no", ":agent_no"),
        (call_script, "script_multiplayer_find_player_leader_for_bot", ":team_no", 1),
        (assign, ":leader_player", reg0),
        (agent_set_group, ":agent_no", ":leader_player"),
    ]),
    
    ("multiplayer_find_spawn_point",
      [
        (store_script_param, ":team_no", 1),
        (store_script_param, ":examine_all_spawn_points", 2), #0-dm, 1-tdm, 2-cf, 3-hq, 4-sg
        (store_script_param, ":is_horseman", 3), #0:no, 1:yes, -1:do not care
        
        (set_fixed_point_multiplier, 100),
        
        (assign, ":flags", 0),
        
        (try_begin),
          (eq, ":examine_all_spawn_points", 1),
          (val_or, ":flags", spf_examine_all_spawn_points),
        (try_end),
        
        (try_begin),
          (eq, ":is_horseman", 1),
          (val_or, ":flags", spf_is_horseman),
        (try_end),
        
        (try_begin),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
          (val_or, ":flags", spf_all_teams_are_enemy),
          (val_or, ":flags", spf_try_to_spawn_close_to_at_least_one_enemy),
        (else_try),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_team_deathmatch),
          (val_or, ":flags", spf_try_to_spawn_close_to_at_least_one_enemy),
        (else_try),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
          (val_or, ":flags", spf_team_1_spawn_far_from_entry_66), #team 1 agents will not spawn 70 meters around of entry 0
          (val_or, ":flags", spf_team_0_walkers_spawn_at_high_points),
          (val_or, ":flags", spf_team_0_spawn_near_entry_66),
          (val_or, ":flags", spf_care_agent_to_agent_distances_less),
        (else_try),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
          (val_or, ":flags", spf_team_1_spawn_far_from_entry_0), #team 1 agents will not spawn 70 meters around of entry 0
          (val_or, ":flags", spf_team_0_spawn_far_from_entry_32), #team 0 agents will not spawn 70 meters around of entry 32
          (val_or, ":flags", spf_try_to_spawn_close_to_at_least_one_enemy),
        (else_try),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters),
          (assign, ":assigned_flag_count", 0),
          
          (store_sub, ":maximum_moved_flag_distance", multi_headquarters_pole_height, 50), #900 - 50 = 850
          (store_mul, ":maximum_moved_flag_distance_sq", ":maximum_moved_flag_distance", ":maximum_moved_flag_distance"),
          (val_div, ":maximum_moved_flag_distance_sq", 100), #dividing 100, because fixed point multiplier is 100 and it is included twice, look above line.
          
          (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
            (store_add, ":cur_flag_owner_slot", multi_data_flag_owner_begin, ":flag_no"),
            (troop_get_slot, ":cur_flag_owner", "trp_multiplayer_data", ":cur_flag_owner_slot"),
            
            (scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":flag_no"),
            (prop_instance_get_position, pos0, ":pole_id"),
            
            (try_begin),
              (eq, ":cur_flag_owner", 1),
              (scene_prop_get_instance, ":flag_of_team_1", "$team_1_flag_scene_prop", ":flag_no"),
              
              (prop_instance_get_position, pos1, ":flag_of_team_1"),
              (get_sq_distance_between_positions, ":flag_height_sq", pos0, pos1),
              (ge, ":flag_height_sq", ":maximum_moved_flag_distance_sq"),
              
              (set_spawn_effector_scene_prop_id, ":assigned_flag_count", ":flag_of_team_1"),
              (val_add, ":assigned_flag_count", 1),
            (else_try),
              (eq, ":cur_flag_owner", 2),
              (scene_prop_get_instance, ":flag_of_team_2", "$team_2_flag_scene_prop", ":flag_no"),
              
              (prop_instance_get_position, pos1, ":flag_of_team_2"),
              (get_sq_distance_between_positions, ":flag_height_sq", pos0, pos1),
              (ge, ":flag_height_sq", ":maximum_moved_flag_distance_sq"),
              
              (set_spawn_effector_scene_prop_id, ":assigned_flag_count", ":flag_of_team_2"),
              (val_add, ":assigned_flag_count", 1),
            (try_end),
          (try_end),
          (set_spawn_effector_scene_prop_id, ":assigned_flag_count", -1),
        (try_end),
        
        (multiplayer_find_spawn_point, reg0, ":team_no", ":flags"),
    ]),
    
    # script_multiplayer_find_spawn_point_2
    # Input: arg1 = team_no, arg2 = examine_all_spawn_points, arg3 = is_horseman
    # Output: reg0 = entry_point_no
    ("multiplayer_find_spawn_point_2",
      [
        (store_script_param, ":team_no", 1),
        (store_script_param, ":examine_all_spawn_points", 2), #0-dm, 1-tdm, 2-cf, 3-hq, 4-sg
        (store_script_param, ":is_horseman", 3), #0:no, 1:yes, -1:do not care
        
        (assign, ":best_entry_point_score", -10000000),
        (assign, ":best_entry_point", 0),
        
        (assign, ":num_operations", 0),
        
        (assign, ":num_human_agents_div_3_plus_one", 0),
        (try_begin), #counting number of agents
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
          (try_for_agents, ":i_agent"),
            (agent_is_alive, ":i_agent"),
            (agent_is_human, ":i_agent"),
            (val_add, ":num_human_agents_div_3_plus_one", 1),
          (try_end),
        (try_end),
        
        (assign, ":num_human_agents_plus_one", ":num_human_agents_div_3_plus_one"),
        
        (try_begin),
          (le, ":num_human_agents_plus_one", 4),
          (assign, ":random_number_upper_limit", 2), #this is not typo-mistake this should be 2 too, not 1.
        (else_try),
          (le, ":num_human_agents_plus_one", 8),
          (assign, ":random_number_upper_limit", 2),
        (else_try),
          (le, ":num_human_agents_plus_one", 16),
          (assign, ":random_number_upper_limit", 3),
        (else_try),
          (le, ":num_human_agents_plus_one", 24),
          (assign, ":random_number_upper_limit", 4),
        (else_try),
          (le, ":num_human_agents_plus_one", 32),
          (assign, ":random_number_upper_limit", 5),
        (else_try),
          (le, ":num_human_agents_plus_one", 40),
          (assign, ":random_number_upper_limit", 6),
        (else_try),
          (assign, ":random_number_upper_limit", 7),
        (try_end),
        
        (val_div, ":num_human_agents_div_3_plus_one", 3),
        (val_add, ":num_human_agents_div_3_plus_one", 1),
        (store_mul, ":negative_num_human_agents_div_3_plus_one", ":num_human_agents_div_3_plus_one", -1),
        
        (try_begin),
          (eq, ":examine_all_spawn_points", 1),
          (assign, ":random_number_upper_limit", 1),
        (try_end),
        
        (try_begin), #counting number of our flags and enemy flags
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters),
          (assign, ":our_flag_count", 0),
          (assign, ":enemy_flag_count", 0),
          (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
            (store_add, ":cur_flag_owner_slot", multi_data_flag_owner_begin, ":flag_no"),
            (troop_get_slot, ":cur_flag_owner", "trp_multiplayer_data", ":cur_flag_owner_slot"),
            (neq, ":cur_flag_owner", 0),
            (val_sub, ":cur_flag_owner", 1),
            (try_begin),
              (eq, ":cur_flag_owner", ":team_no"),
              (val_add, ":our_flag_count", 1),
            (else_try),
              (val_add, ":enemy_flag_count", 1),
            (try_end),
          (try_end),
        (try_end),
        
        (assign, ":first_agent", 0),
        (try_begin), #first spawned agents will be spawned at their base points in tdm, cf and hq mods.
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_team_deathmatch),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters),
          (try_begin),
            (eq, ":team_no", 0),
            (eq, "$g_multiplayer_team_1_first_spawn", 1),
            (assign, ":first_agent", 1),
            (assign, "$g_multiplayer_team_1_first_spawn", 0),
          (else_try),
            (eq, ":team_no", 1),
            (eq, "$g_multiplayer_team_2_first_spawn", 1),
            (assign, ":first_agent", 1),
            (assign, "$g_multiplayer_team_2_first_spawn", 0),
          (try_end),
        (try_end),
        
        (try_begin),
          (eq, ":first_agent", 1),
          (store_mul, ":best_entry_point", ":team_no", multi_num_valid_entry_points_div_2),
        (else_try),
          (try_for_range, ":i_entry_point", 0, multi_num_valid_entry_points),
            (assign, ":minimum_enemy_distance", 3000),
            (assign, ":second_minimum_enemy_distance", 3000),
            
            (assign, ":entry_point_score", 0),
            (store_random_in_range, ":random_value", 0, ":random_number_upper_limit"), #in average it is 5
            (eq, ":random_value", 0),
            (entry_point_get_position, pos0, ":i_entry_point"), #pos0 holds current entry point position
            (try_for_agents, ":i_agent"),
              (agent_is_alive, ":i_agent"),
              (agent_is_human, ":i_agent"),
              (agent_get_team, ":agent_team", ":i_agent"),
              (try_begin),
                (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_team_deathmatch),
                (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
                (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters),
                (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
                (try_begin),
                  (teams_are_enemies, ":team_no", ":agent_team"),
                  (assign, ":multiplier", -2),
                (else_try),
                  (assign, ":multiplier", 1),
                (try_end),
              (else_try),
                (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
                (eq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
                (assign, ":multiplier", -1),
              (try_end),
              (agent_get_position, pos1, ":i_agent"),
              (get_distance_between_positions_in_meters, ":distance", pos0, pos1),
              (val_add, ":num_operations", 1),
              (try_begin),
                (try_begin), #find closest enemy soldiers
                  (lt, ":multiplier", 0),
                  (try_begin),
                    (lt, ":distance", ":minimum_enemy_distance"),
                    (assign, ":second_minimum_enemy_distance", ":minimum_enemy_distance"),
                    (assign, ":minimum_enemy_distance", ":distance"),
                  (else_try),
                    (lt, ":distance", ":second_minimum_enemy_distance"),
                    (assign, ":second_minimum_enemy_distance", ":distance"),
                  (try_end),
                (try_end),
                
                (lt, ":distance", 100),
                (try_begin), #do not spawn over or too near to another agent (limit is 2 meters, squared 4 meters)
                  (lt, ":distance", 3),
                  (try_begin),
                    (this_or_next|eq, ":examine_all_spawn_points", 0),
                    (this_or_next|lt, ":multiplier", 0), #new added 20.08.08
                    (neq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
                    (try_begin),
                      (lt, ":distance", 1),
                      (assign, ":dist_point", -1000000), #never place
                    (else_try),
                      (lt, ":distance", 2),
                      (try_begin),
                        (lt, ":multiplier", 0),
                        (assign, ":dist_point", -20000),
                      (else_try),
                        (assign, ":dist_point", -2000), #can place, friend and distance is between 1-2 meters
                      (try_end),
                    (else_try),
                      (try_begin),
                        (lt, ":multiplier", 0),
                        (assign, ":dist_point", -10000),
                      (else_try),
                        (assign, ":dist_point", -1000), #can place, friend and distance is between 2-3 meters
                      (try_end),
                    (try_end),
                  (else_try),
                    #if examinining all spawn points and mod is siege only. This happens in new round start placings.
                    (try_begin),
                      (lt, ":distance", 1),
                      (assign, ":dist_point", -20000), #very hard to place distance is < 1 meter
                    (else_try),
                      (lt, ":distance", 2),
                      (assign, ":dist_point", -2000),
                    (else_try),
                      (assign, ":dist_point", -1000), #can place, distance is between 2-3 meters
                    (try_end),
                  (try_end),
                  
                  (val_mul, ":dist_point", ":num_human_agents_div_3_plus_one"),
                (else_try),
                  (assign, ":dist_point", 0),
                  (this_or_next|neq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
                  (this_or_next|lt, ":multiplier", 0),
                  (eq, ":team_no", 1), #only attackers are effected by positive enemy & friend distance at siege mod, defenders only get negative score effect a bit
                  
                  (try_begin), #in siege give no positive or negative score to > 40m distance. (6400 = 10000 - 3600(60 * 60))
                    (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
                    
                    (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch), #new added after moving below part to above
                    (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_duel), #new added after moving below part to above
                    (eq, "$g_multiplayer_game_type", multiplayer_game_type_team_deathmatch), #new added after moving below part to above
                    
                    (store_sub, ":dist_point", multiplayer_spawn_min_enemy_dist_limit, ":distance"), #up to 40 meters give (positive(if friend) or negative(if enemy)) points
                    (val_max, ":dist_point", 0),
                    (val_mul, ":dist_point", ":dist_point"),
                  (else_try),
                    (store_mul, ":one_and_half_limit", multiplayer_spawn_min_enemy_dist_limit, 3),
                    (val_div, ":one_and_half_limit", 2),
                    (store_sub, ":dist_point", ":one_and_half_limit", ":distance"), #up to 60 meters give (positive(if friend) or negative(if enemy)) points
                    (val_mul, ":dist_point", ":dist_point"),
                  (try_end),
                  
                  (val_mul, ":dist_point", ":multiplier"),
                (try_end),
                (val_add, ":entry_point_score", ":dist_point"),
              (try_end),
            (try_end),
            
            (try_begin),
              (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
              (store_mul, ":max_enabled_agent_distance_score", 1000, ":num_human_agents_div_3_plus_one"),
              (ge, ":entry_point_score", ":max_enabled_agent_distance_score"),
              (assign, ":entry_point_score", ":max_enabled_agent_distance_score"),
            (try_end),
            
            (try_begin),
              (neq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
              
              #(assign, ":minimum_enemy_dist_score", 0), #close also these with displays
              #(assign, ":second_minimum_enemy_dist_score", 0), #close also these with displays
              #(assign, reg2, ":minimum_enemy_distance"), #close also these with displays
              #(assign, reg3, ":second_minimum_enemy_distance"), #close also these with displays
              
              (try_begin), #if minimum enemy dist score is greater than 40(multiplayer_spawn_above_opt_enemy_dist_point) meters then give negative score
                (lt, ":minimum_enemy_distance", 3000),
                (try_begin),
                  (gt, ":minimum_enemy_distance", multiplayer_spawn_above_opt_enemy_dist_point),
                  (val_sub, ":minimum_enemy_distance", multiplayer_spawn_above_opt_enemy_dist_point),
                  (store_mul, ":minimum_enemy_dist_score", ":minimum_enemy_distance", -50),
                  (val_mul, ":minimum_enemy_dist_score", ":num_human_agents_div_3_plus_one"),
                  (val_add, ":entry_point_score", ":minimum_enemy_dist_score"),
                (try_end),
              (try_end),
              
              (try_begin), #if second minimum enemy dist score is greater than 40(multiplayer_spawn_above_opt_enemy_dist_point) meters then give negative score
                (lt, ":second_minimum_enemy_distance", 3000), #3000 x 3000
                (try_begin),
                  (gt, ":second_minimum_enemy_distance", multiplayer_spawn_above_opt_enemy_dist_point),
                  (val_sub, ":second_minimum_enemy_distance", multiplayer_spawn_above_opt_enemy_dist_point),
                  (store_mul, ":second_minimum_enemy_dist_score", ":second_minimum_enemy_distance", -50),
                  (val_mul, ":second_minimum_enemy_dist_score", ":num_human_agents_div_3_plus_one"),
                  (val_add, ":entry_point_score", ":second_minimum_enemy_dist_score"),
                (try_end),
              (try_end),
              
              #(assign, reg0, ":minimum_enemy_dist_score"), #close also above assignment lines with these displays
              #(assign, reg1, ":second_minimum_enemy_dist_score"), #close also above assignment lines with these displays
              #(display_message, "@{!}minimum enemy distance : {reg2}, score : {reg0}"), #close also above assignment lines with these displays
              #(display_message, "@{!}second minimum enemy distance : {reg3}, score : {reg1}"), #close also above assignment lines with these displays
            (try_end),
            
            (try_begin), #giving positive points for "distance of entry point position to ground" while searching for entry point for defender team
              (neq, ":is_horseman", -1), #if being horseman or rider is not (not important)
              
              #additional score to entry points which has distance to ground value of > 0 meters
              (position_get_distance_to_terrain, ":height_to_terrain", pos0),
              (val_max, ":height_to_terrain", 0),
              (val_min, ":height_to_terrain", 300),
              (ge, ":height_to_terrain", 40),
              
              (store_mul, ":height_to_terrain_score", ":height_to_terrain", ":num_human_agents_div_3_plus_one"), #it was 8
              
              (try_begin),
                (eq, "$g_multiplayer_game_type", multiplayer_game_type_team_deathmatch),
                (val_mul, ":height_to_terrain_score", 16),
              (else_try),
                (val_mul, ":height_to_terrain_score", 4),
              (try_end),
              
              (try_begin),
                (eq, ":is_horseman", 0),
                (try_begin),
                  (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege), #but only in siege mod, defender infantries will get positive points for spawning in high places.
                  (eq, ":team_no", 0),
                  (val_add, ":entry_point_score", ":height_to_terrain_score"),
                (try_end),
              (else_try),
                (val_mul, ":height_to_terrain_score", 5),
                (val_sub, ":entry_point_score", ":height_to_terrain_score"),
              (try_end),
            (try_end),
            
            (try_begin), #additional random entry point score at deathmatch, teamdethmatch, capture the flag and siege
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
              (eq, "$g_multiplayer_game_type", multiplayer_game_type_team_deathmatch),
              (try_begin),
                (neq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
                (store_random_in_range, ":random_value", 0, 400),
                
                (try_begin),
                  (eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
                  (val_mul, ":random_value", 5),
                (try_end),
              (else_try),
                (eq, ":team_no", 1),
                (store_random_in_range, ":random_value", 0, 600), #siege-attacker
              (else_try),
                (store_random_in_range, ":random_value", 0, 200), #siege-defender
              (try_end),
              (val_mul, ":random_value", ":num_human_agents_div_3_plus_one"),
              (val_add, ":entry_point_score", ":random_value"),
            (try_end),
            
            (try_begin),
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
              (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
              
              (try_begin),
                (eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
                (try_begin),
                  (eq, ":team_no", 0),
                  (entry_point_get_position, pos1, multi_base_point_team_1), #our base is at pos1
                  (entry_point_get_position, pos2, multi_base_point_team_2), #enemy base is at pos2
                (else_try),
                  (entry_point_get_position, pos1, multi_base_point_team_2), #our base is at pos2
                  (entry_point_get_position, pos2, multi_base_point_team_1), #enemy base is at pos1
                (try_end),
              (else_try),
                (try_begin), #siege
                  (eq, ":team_no", 0),
                  (entry_point_get_position, pos1, multi_siege_flag_point), #our base is at pos1 (it was multi_initial_spawn_point_team_1 changed at v622)
                  (entry_point_get_position, pos2, multi_initial_spawn_point_team_2), #enemy base is at pos2
                (else_try),
                  (entry_point_get_position, pos1, multi_initial_spawn_point_team_2), #our base is at pos2
                  (entry_point_get_position, pos2, multi_siege_flag_point), #enemy base is at pos1 (it was multi_initial_spawn_point_team_1 changed at v622)
                (try_end),
              (try_end),
              
              (try_begin),
                (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
                (position_get_z, ":pos0_z", pos0),
                (position_set_z, pos1, ":pos0_z"), #make z of our base same with entry point position z
                (position_set_z, pos2, ":pos0_z"), #make z of enemy base same with entry point position z
              (try_end),
              
              (get_sq_distance_between_positions_in_meters, ":sq_dist_to_our_base", pos0, pos1),
              (get_sq_distance_between_positions_in_meters, ":sq_dist_to_enemy_base", pos0, pos2),
              (get_distance_between_positions_in_meters, ":dist_to_enemy_base", pos0, pos2),
              
              #give positive points if this entry point is near to our base.
              (assign, ":dist_to_our_base_point", 0),
              (try_begin), #capture the flag (points for being near to base)
                (eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
                
                (get_distance_between_positions_in_meters, ":dist_to_our_base", pos0, pos1),
                (lt, ":dist_to_our_base", 100),
                (store_sub, ":dist_to_our_base_point", 100, ":dist_to_our_base"),
                
                (try_begin), #assign all 75-100's to 75
                  (gt, ":dist_to_our_base_point", 75),
                  (assign, ":dist_to_our_base_point", 75),
                (try_end),
                
                (val_mul, ":dist_to_our_base_point", 50), #0..5000 (increase is linear)
                
                (val_mul, ":dist_to_our_base_point", ":num_human_agents_div_3_plus_one"),
              (else_try), #siege (points for being near to base)
                (lt, ":sq_dist_to_our_base", 10000), #in siege give entry points score until 100m distance is reached
                (try_begin),
                  (eq, ":team_no", 0),
                  (try_begin),
                    (lt, ":sq_dist_to_our_base", 2500), #if distance is < 50m in siege give all highest point possible
                    (assign, ":sq_dist_to_our_base", 0),
                  (else_try),
                    (val_sub, ":sq_dist_to_our_base", 2500),
                    (val_mul, ":sq_dist_to_our_base", 2),
                  (try_end),
                (try_end),
                
                (store_sub, ":dist_to_our_base_point", 10000, ":sq_dist_to_our_base"),
                
                #can be (10000 - (10000 - 2500) * 2) = -5000 (for only defenders) so we are adding this loss.
                (val_add, ":dist_to_our_base_point", 5000), #so score getting from being near to base changes between 0 to 15000
                
                (try_begin),
                  (eq, ":team_no", 0),
                (else_try), #in siege mod for attackers being near to base entry point has 45 times less importance
                  (val_div, ":dist_to_our_base_point", 45),
                (try_end),
                (val_mul, ":dist_to_our_base_point", ":num_human_agents_div_3_plus_one"),
              (try_end),
              
              (val_add, ":entry_point_score", ":dist_to_our_base_point"),
              
              
              #give negative points if this entry point is near to enemy base.
              (assign, ":dist_to_enemy_base_point", 0),
              (try_begin), #capture the flag
                (eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
                
                (lt, ":dist_to_enemy_base", 150),
                (store_sub, ":dist_to_enemy_base_point", 150, ":dist_to_enemy_base"),
                
                (try_begin), #assign 150 to 150 + (150 - 50) * 2 = 350, assign 100 to 100 + (100 - 50) * 2 = 200
                  (gt, ":dist_to_enemy_base_point", 50),
                  (store_sub, ":dist_to_enemy_base_point_minus_50", ":dist_to_enemy_base_point", 50),
                  (val_mul, ":dist_to_enemy_base_point_minus_50", 2),
                  (val_add, ":dist_to_enemy_base_point", ":dist_to_enemy_base_point_minus_50"),
                (try_end),
                
                (val_mul, ":dist_to_enemy_base_point", -50), #-7500(with extras 350 * 50 = -17500)..0 (increase is linear)
                
                (val_mul, ":dist_to_enemy_base_point", ":num_human_agents_div_3_plus_one"),
              (else_try),
                (this_or_next|neq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
                (eq, ":team_no", 1),
                
                (assign, ":dist_to_enemy_base_point", 0),
                
                (try_begin),
                  (neq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
                  
                  (try_begin),
                    (lt, ":sq_dist_to_enemy_base", 10000),
                    (store_sub, ":dist_to_enemy_base_point", 10000, ":sq_dist_to_enemy_base"),
                    (val_div, ":dist_to_enemy_base_point", 4),
                    (val_mul, ":dist_to_enemy_base_point", ":negative_num_human_agents_div_3_plus_one"),
                  (try_end),
                (else_try),
                  (val_max, ":dist_to_enemy_base", 60), #<60 meters has all most negative score
                  
                  (try_begin),
                    (eq, ":is_horseman", 1),
                    (assign, ":optimal_distance", 120),
                  (else_try),
                    (assign, ":optimal_distance", 80),
                  (try_end),
                  
                  (try_begin),
                    (le, ":dist_to_enemy_base", ":optimal_distance"),
                    (store_sub, ":dist_to_enemy_base_point", ":optimal_distance", ":dist_to_enemy_base"),
                    (val_mul, ":dist_to_enemy_base_point", 180), #-3600 max
                  (else_try),
                    (store_sub, ":dist_to_enemy_base_point", ":dist_to_enemy_base", ":optimal_distance"),
                    (val_mul, ":dist_to_enemy_base_point", 30), #-unlimited max but lower slope
                  (try_end),
                  
                  (val_sub, ":dist_to_enemy_base_point", 600),
                  (val_max, ":dist_to_enemy_base_point", 0),
                  
                  (val_mul, ":dist_to_enemy_base_point", ":negative_num_human_agents_div_3_plus_one"),
                (try_end),
              (try_end),
              
              (val_add, ":entry_point_score", ":dist_to_enemy_base_point"),
            (else_try),
              (eq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters),
              
              (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
                (store_add, ":cur_flag_owner_slot", multi_data_flag_owner_begin, ":flag_no"),
                (troop_get_slot, ":cur_flag_owner", "trp_multiplayer_data", ":cur_flag_owner_slot"),
                (neq, ":cur_flag_owner", 0),
                (val_sub, ":cur_flag_owner", 1),
                
                (scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":flag_no"),
                (prop_instance_get_position, pos1, ":pole_id"), #pos1 holds pole position.
                
                (get_sq_distance_between_positions_in_meters, ":sq_dist_to_cur_pole", pos0, pos1),
                (lt, ":sq_dist_to_cur_pole", 6400),
                
                (try_begin),
                  (eq, ":cur_flag_owner", ":team_no"),
                  (store_sub, ":dist_to_flag_point", 6400, ":sq_dist_to_cur_pole"), #up to 80 meters give positive points if entry point is near our base
                  (val_mul, ":dist_to_flag_point", 2),
                  (val_div, ":dist_to_flag_point", ":our_flag_count"),
                  (val_mul, ":dist_to_flag_point", ":num_human_agents_div_3_plus_one"),
                (else_try),
                  (store_sub, ":dist_to_flag_point", 6400, ":sq_dist_to_cur_pole"), #up to 80 meters give negative points if entry point is near enemy base
                  (val_mul, ":dist_to_flag_point", 2),
                  (val_div, ":dist_to_flag_point", ":enemy_flag_count"),
                  (val_mul, ":dist_to_flag_point", ":negative_num_human_agents_div_3_plus_one"),
                (try_end),
                (val_add, ":entry_point_score", ":dist_to_flag_point"),
              (try_end),
            (try_end),
            
            #(assign, reg1, ":i_entry_point"),
            #(assign, reg2, ":entry_point_score"),
            #(display_message, "@{!}entry_no : {reg1} , entry_score : {reg2}"),
            
            (gt, ":entry_point_score", ":best_entry_point_score"),
            (assign, ":best_entry_point_score", ":entry_point_score"),
            (assign, ":best_entry_point", ":i_entry_point"),
          (try_end),
          
          #(assign, reg0, ":best_entry_point"),
          #(assign, reg1, ":best_entry_point_score"),
          #(assign, reg2, ":num_operations"),
          #(assign, reg7, ":is_horseman"),
          #(display_message, "@{!},is horse:{reg7}, best entry:{reg0}, best entry score:{reg1}, num_operations:{reg2}"),
        (try_end),
        (assign, reg0, ":best_entry_point"),
    ]),
    
    #script_multiplayer_buy_agent_equipment
    # Input: arg1 = player_no
    # Output: none
    ("multiplayer_buy_agent_equipment",
      [
        (store_script_param, ":player_no", 1),
        (player_get_troop_id, ":player_troop", ":player_no"),
        (player_get_gold, ":player_gold", ":player_no"),
        (player_get_slot, ":added_gold", ":player_no", slot_player_last_rounds_used_item_earnings),
        (player_set_slot, ":player_no", slot_player_last_rounds_used_item_earnings, 0),
        (val_add, ":player_gold", ":added_gold"),
        (assign, ":armor_bought", 0),
        
        #moving original values to temp slots
        (try_for_range, ":i_item", slot_player_selected_item_indices_begin, slot_player_selected_item_indices_end),
          (player_get_slot, ":selected_item_index", ":player_no", ":i_item"),
          (store_sub, ":i_cur_selected_item", ":i_item", slot_player_selected_item_indices_begin),
          (try_begin),
            (player_item_slot_is_picked_up, ":player_no", ":i_cur_selected_item"),
            (assign, ":selected_item_index", -1),
          (try_end),
          (val_add, ":i_cur_selected_item", slot_player_cur_selected_item_indices_begin),
          (player_set_slot, ":player_no", ":i_cur_selected_item", ":selected_item_index"),
        (try_end),
        (assign, ":end_cond", 1000),
        (try_for_range, ":unused", 0, ":end_cond"),
          (call_script, "script_multiplayer_calculate_cur_selected_items_cost", ":player_no", 0),
          (assign, ":total_cost", reg0),
          (try_begin),
            (gt, ":total_cost", ":player_gold"),
            #downgrade one of the selected items
            #first normalize the prices
            #then prioritize some of the weapon classes for specific troop classes
            (call_script, "script_multiplayer_get_troop_class", ":player_troop"),
            (assign, ":player_troop_class", reg0),
            
            (assign, ":max_cost_value", 0),
            (assign, ":max_cost_value_index", -1),
            (try_for_range, ":i_item", slot_player_cur_selected_item_indices_begin, slot_player_cur_selected_item_indices_end),
              (player_get_slot, ":item_id", ":player_no", ":i_item"),
              (ge, ":item_id", 0), #might be -1 for horses etc.
              (call_script, "script_multiplayer_get_item_value_for_troop", ":item_id", ":player_troop"),
              (assign, ":item_value", reg0),
              (store_sub, ":item_type", ":i_item", slot_player_cur_selected_item_indices_begin),
              (try_begin), #items
                (this_or_next|eq, ":item_type", 0),
                (this_or_next|eq, ":item_type", 1),
                (this_or_next|eq, ":item_type", 2),
                (eq, ":item_type", 3),
                (val_mul, ":item_value", 5),
              (else_try), #head
                (eq, ":item_type", 4),
                (val_mul, ":item_value", 4),
              (else_try), #body
                (eq, ":item_type", 5),
                (val_mul, ":item_value", 2),
              (else_try), #foot
                (eq, ":item_type", 6),
                (val_mul, ":item_value", 8),
              (else_try), #gloves
                (eq, ":item_type", 7),
                (val_mul, ":item_value", 8),
              (else_try), #horse
                #base value (most expensive)
              (try_end),
              (item_get_slot, ":item_class", ":item_id", slot_item_multiplayer_item_class),
              (try_begin),
                (eq, ":player_troop_class", multi_troop_class_infantry),
                (this_or_next|eq, ":item_class", multi_item_class_type_sword),
                (this_or_next|eq, ":item_class", multi_item_class_type_axe),
                (this_or_next|eq, ":item_class", multi_item_class_type_blunt),
                (this_or_next|eq, ":item_class", multi_item_class_type_war_picks),
                (this_or_next|eq, ":item_class", multi_item_class_type_two_handed_sword),
                (this_or_next|eq, ":item_class", multi_item_class_type_small_shield),
                (eq, ":item_class", multi_item_class_type_two_handed_axe),
                (val_div, ":item_value", 2),
              (else_try),
                (eq, ":player_troop_class", multi_troop_class_spearman),
                (this_or_next|eq, ":item_class", multi_item_class_type_spear),
                (eq, ":item_class", multi_item_class_type_large_shield),
                (val_div, ":item_value", 2),
              (else_try),
                (eq, ":player_troop_class", multi_troop_class_cavalry),
                (this_or_next|eq, ":item_class", multi_item_class_type_lance),
                (this_or_next|eq, ":item_class", multi_item_class_type_sword),
                (eq, ":item_class", multi_item_class_type_horse),
                (val_div, ":item_value", 2),
              (else_try),
                (eq, ":player_troop_class", multi_troop_class_archer),
                (this_or_next|eq, ":item_class", multi_item_class_type_bow),
                (eq, ":item_class", multi_item_class_type_arrow),
                (val_div, ":item_value", 2),
              (else_try),
                (eq, ":player_troop_class", multi_troop_class_crossbowman),
                (this_or_next|eq, ":item_class", multi_item_class_type_crossbow),
                (eq, ":item_class", multi_item_class_type_bolt),
                (val_div, ":item_value", 2),
              (else_try),
                (eq, ":player_troop_class", multi_troop_class_mounted_archer),
                (this_or_next|eq, ":item_class", multi_item_class_type_bow),
                (this_or_next|eq, ":item_class", multi_item_class_type_arrow),
                (eq, ":item_class", multi_item_class_type_horse),
                (val_div, ":item_value", 2),
              (else_try),
                (eq, ":player_troop_class", multi_troop_class_mounted_crossbowman),
                (this_or_next|eq, ":item_class", multi_item_class_type_crossbow),
                (this_or_next|eq, ":item_class", multi_item_class_type_bolt),
                (eq, ":item_class", multi_item_class_type_horse),
                (val_div, ":item_value", 2),
              (try_end),
              
              (try_begin),
                (gt, ":item_value", ":max_cost_value"),
                (assign, ":max_cost_value", ":item_value"),
                (assign, ":max_cost_value_index", ":i_item"),
              (try_end),
            (try_end),
            
            #max_cost_value and max_cost_value_index will definitely be valid
            #unless no items are left (therefore some items must cost 0 gold)
            (player_get_slot, ":item_id", ":player_no", ":max_cost_value_index"),
            (call_script, "script_multiplayer_get_previous_item_for_item_and_troop", ":item_id", ":player_troop"),
            (assign, ":item_id", reg0),
            (player_set_slot, ":player_no", ":max_cost_value_index", ":item_id"),
          (else_try),
            (assign, ":end_cond", 0),
            (val_sub, ":player_gold", ":total_cost"),
            (player_set_gold, ":player_no", ":player_gold", multi_max_gold_that_can_be_stored),
            (try_for_range, ":i_item", slot_player_cur_selected_item_indices_begin, slot_player_cur_selected_item_indices_end),
              (player_get_slot, ":item_id", ":player_no", ":i_item"),
              #checking if different class default item replace is needed for weapons
              (try_begin),
                (ge, ":item_id", 0),
                #then do nothing
              (else_try),
                (store_sub, ":base_index_slot", ":i_item", slot_player_cur_selected_item_indices_begin),
                (store_add, ":selected_item_index_slot", ":base_index_slot", slot_player_selected_item_indices_begin),
                (player_get_slot, ":selected_item_index", ":player_no", ":selected_item_index_slot"),
                (this_or_next|eq, ":selected_item_index", -1),
                (player_item_slot_is_picked_up, ":player_no", ":base_index_slot"),
                #then do nothing
              (else_try),
                #an item class without a default value is -1, then find a default weapon
                (item_get_slot, ":item_class", ":selected_item_index", slot_item_multiplayer_item_class),
                (is_between, ":item_class", multi_item_class_type_weapons_begin, multi_item_class_type_weapons_end),
                (assign, ":dc_replaced_item", -1),
                (try_for_range, ":i_dc_item_class", multi_item_class_type_melee_weapons_begin, multi_item_class_type_melee_weapons_end),
                  (lt, ":dc_replaced_item", 0),
                  (assign, ":dc_item_class_used", 0),
                  (try_for_range, ":i_dc_item", slot_player_cur_selected_item_indices_begin, slot_player_cur_selected_item_indices_end),
                    (player_get_slot, ":dc_cur_item", ":player_no", ":i_dc_item"),
                    (ge, ":dc_cur_item", 0),
                    (item_get_slot, ":dc_item_class", ":dc_cur_item", slot_item_multiplayer_item_class),
                    (eq, ":dc_item_class", ":i_dc_item_class"),
                    (assign, ":dc_item_class_used", 1),
                  (try_end),
                  (eq, ":dc_item_class_used", 0),
                  (assign, ":dc_end_cond", all_items_end),
                  (try_for_range, ":i_dc_new_item", all_items_begin, ":dc_end_cond"),
                    (item_slot_eq, ":i_dc_new_item", slot_item_multiplayer_item_class, ":i_dc_item_class"),
                    (call_script, "script_cf_multiplayer_is_item_default_for_troop", ":i_dc_new_item", ":player_troop"),
                    (assign, ":dc_end_cond", 0), #break
                    (assign, ":dc_replaced_item", ":i_dc_new_item"),
                  (try_end),
                (try_end),
                (ge, ":dc_replaced_item", 0),
                (player_set_slot, ":player_no", ":i_item", ":dc_replaced_item"),
                (assign, ":item_id", ":dc_replaced_item"),
              (try_end),
              
              #finally, add the item to agent
              (try_begin),
                (ge, ":item_id", 0), #might be -1 for horses etc.
                (store_sub, ":item_slot", ":i_item", slot_player_cur_selected_item_indices_begin),
                (player_add_spawn_item, ":player_no", ":item_slot", ":item_id"),
                (try_begin),
                  (eq, ":item_slot", ek_body), #ek_body is the slot for armor
                  (assign, ":armor_bought", 1),
                (try_end),
              (try_end),
            (try_end),
            
            (player_set_slot, ":player_no", slot_player_total_equipment_value, ":total_cost"),
          (try_end),
        (try_end),
        (try_begin),
          (eq, ":armor_bought", 0),
          (eq, "$g_multiplayer_force_default_armor", 1),
          (assign, ":end_cond", all_items_end),
          (try_for_range, ":i_new_item", all_items_begin, ":end_cond"),
            (this_or_next|item_slot_eq, ":i_new_item", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
            (this_or_next|item_slot_eq, ":i_new_item", slot_item_multiplayer_item_class, multi_item_class_type_medium_armor),
            (item_slot_eq, ":i_new_item", slot_item_multiplayer_item_class, multi_item_class_type_heavy_armor),
            (call_script, "script_cf_multiplayer_is_item_default_for_troop", ":i_new_item", ":player_troop"),
            (assign, ":end_cond", 0), #break
            (player_add_spawn_item, ":player_no", ek_body, ":i_new_item"), #ek_body is the slot for armor
          (try_end),
        (try_end),
    ]),
    
    # script_party_get_ideal_size @used for NPC parties.
    # Input: arg1 = party_no
    # Output: reg0: ideal size
    ("party_get_ideal_size",
      [
        (store_script_param_1, ":party_no"),
        (assign, ":limit", 30),
        (try_begin),
          (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
          (party_stack_get_troop_id, ":party_leader", ":party_no", 0),
          (store_faction_of_party, ":faction_id", ":party_no"),
          (assign, ":limit", 10),
          
          (store_skill_level, ":skill", "skl_leadership", ":party_leader"),
          (store_attribute_level, ":charisma", ":party_leader", ca_charisma),
          (val_mul, ":skill", 5),
          (val_add, ":limit", ":skill"),
          (val_add, ":limit", ":charisma"),
          
          (troop_get_slot, ":troop_renown", ":party_leader", slot_troop_renown),
          (store_div, ":renown_bonus", ":troop_renown", 25),
          (val_add, ":limit", ":renown_bonus"),
#TEMPERED changed ideal size for kingdom leader parties to reflect territory held instead of a flat 100
        (try_begin),
          (faction_slot_eq, ":faction_id", slot_faction_leader, ":party_leader"),
		  (faction_get_slot,":num_castles",":faction_id",slot_faction_num_castles),
		  (faction_get_slot,":num_towns",":faction_id",slot_faction_num_towns),
		  (val_mul,":num_castles",5),
		  (val_mul,":num_towns",10),
		  (val_add,":num_towns",":num_castles"),
		  (val_add, ":limit", ":num_towns"),
        (try_end),
#        (try_begin),
#          (faction_slot_eq, ":faction_id", slot_faction_leader, ":party_leader"),
#          (val_add, ":limit", 100),
#        (try_end),
#Tempered changes end
          
          ##diplomacy begin
          (assign, ":percent", 100),
          ##diplomacy end
          
		##diplomacy start+
		#Limit effects of policies for nascent kingdoms.
		(assign, ":policy_min", -3),
		(assign, ":policy_max", 4),#one greater than the maximum
		
		(try_begin),
			(this_or_next|eq, ":faction_id", "fac_player_supporters_faction"),
				(faction_slot_eq, ":faction_id", slot_faction_leader, "trp_player"),
			(faction_get_slot, ":policy_max", ":faction_id", slot_faction_num_towns),
			(faction_get_slot, reg0, ":faction_id", slot_faction_num_castles),
			(val_add, ":policy_max", reg0),
			(val_clamp, ":policy_max", 0, 4),#0, 1, 2, 3
			(store_mul, ":policy_min", ":policy_max", -1),
			(val_add, ":policy_max", 1),#one greater than the maximum
		(try_end),
		##diplomacy end+

        (try_begin),
          (faction_slot_eq, ":faction_id", slot_faction_leader, ":party_leader"),
          (val_add, ":limit", 100),
          ##diplomacy begin
          (try_begin),
            (faction_get_slot, ":centralization", ":faction_id", dplmc_slot_faction_centralization),
            (neq, ":centralization", 0),
			##diplomacy start+ Apply constraint
			(val_clamp, ":centralization", ":policy_min", ":policy_max"),
			##diplomacy end+
            (val_mul, ":centralization", 10),
            (val_add, ":percent", ":centralization"),
          (try_end),

        (else_try),
          (try_begin),
            (faction_get_slot, ":centralization", ":faction_id", dplmc_slot_faction_centralization),
            (neq, ":centralization", 0),
			##diplomacy start+ Apply constraint
			(val_clamp, ":centralization", ":policy_min", ":policy_max"),
			##diplomacy end+
            (val_mul, ":centralization", -3),
            (val_add, ":percent", ":centralization"),
          (try_end),
          (try_begin),
            (faction_get_slot, ":aristocraty", ":faction_id", dplmc_slot_faction_aristocracy),
            (neq, ":aristocraty", 0),
			##diplomacy start+ Apply constraint
			(val_clamp, ":aristocraty", ":policy_min", ":policy_max"),
			##diplomacy end+
            (val_mul, ":aristocraty", 3),
            (val_add, ":percent", ":aristocraty"),
          (try_end),
          (try_begin),
            (faction_get_slot, ":quality", ":faction_id", dplmc_slot_faction_quality),
            (neq, ":quality", 0),
			##diplomacy start+ Apply constraint
			(val_clamp, ":quality", ":policy_min", ":policy_max"),
			##diplomacy end+
            (val_mul, ":quality", -4),
            (val_add, ":percent", ":quality"),
          (try_end),
          ##diplomacy end
        (try_end),

        ##diplomacy begin
        (try_begin),
          (faction_get_slot, ":serfdom", ":faction_id", dplmc_slot_faction_serfdom),
          (neq, ":serfdom", 0),
		  ##diplomacy start+ Apply constraint
		  (val_clamp, ":serfdom", ":policy_min", ":policy_max"),
		  ##diplomacy end+
          (val_mul, ":serfdom", 3),
          (val_add, ":percent", ":serfdom"),
        (try_end),

        (val_mul, ":limit", ":percent"),
		##nested diplomacy start+ Round correctly
		(val_add, ":limit", 50),
		##nested diplomacy end+
        (val_div, ":limit", 100),
        ##diplomacy end

        (try_begin),
          (faction_slot_eq, ":faction_id", slot_faction_marshall, ":party_leader"),
          (val_add, ":limit", 20),
        (try_end),

        (try_for_range, ":cur_center", castles_begin, castles_end),
          (party_slot_eq, ":cur_center", slot_town_lord, ":party_leader"),
          (val_add, ":limit", 20),
        (try_end),
      ##diplomacy start+
      ##Extend this script so it will also work with garrisons 
      (else_try),
         (party_slot_eq, ":party_no", slot_party_type, spt_town),
         (assign, ":limit", 380),#average starting town garrison size
      (else_try),
         (this_or_next|is_between, ":party_no", walled_centers_begin, walled_centers_end),
         (party_slot_eq, ":party_no", slot_party_type, spt_castle),
         (assign, ":limit", 142),#average starting castle garrison size
         #(store_faction_of_party, ":faction_id", ":party_no"),
      ##diplomacy end+
      (try_end),

      #if player has level of 0 then ideal limit will be exactly same, if player has level of 80 then ideal limit will be multiplied by 2 ((80 + 80) / 80)
      #below code will increase limits a little as the game progresses and player gains level
      (store_character_level, ":level", "trp_player"),
      (val_min, ":level", 80),      
      (store_add, ":level_factor", 80, ":level"),
      (val_mul, ":limit", ":level_factor"),
      (val_div, ":limit", 80),
      (assign, reg0, ":limit"),
  ]),
    
    
    #script_game_get_party_prisoner_limit:
    # This script is called from the game engine when the prisoner limit is needed for a party.
    # INPUT: arg1 = party_no
    # OUTPUT: reg0 = prisoner_limit
    ("game_get_party_prisoner_limit",
      [
        # Bypassed prisoner limit to allow infinite scaling
        (assign, reg0, 1000000),
        (set_trigger_result, reg0),
    ]),
    
    #script_game_get_item_extra_text:
    # This script is called from the game engine when an item's properties are displayed.
    # INPUT: arg1 = item_no, arg2 = extra_text_id (this can be between 0-7 (7 included)), arg3 = item_modifier
    # OUTPUT: result_string = item extra text, trigger_result = text color (0 for default)
    ("game_get_item_extra_text",
      [
        (store_script_param, ":item_no", 1),
        (store_script_param, ":extra_text_id", 2),
        (store_script_param, ":item_modifier", 3),

        (item_get_type, ":type", ":item_no"), ## CC
        (try_begin),
          (is_between, ":item_no", food_begin, food_end),
          (try_begin),
            (eq, ":extra_text_id", 0),
            (assign, ":continue", 1),
            (try_begin),
              (this_or_next|eq, ":item_no", "itm_trade_cattle_meat"),
              (this_or_next|eq, ":item_no", "itm_trade_pork"),
              (eq, ":item_no", "itm_trade_chicken"),
              (eq, ":item_modifier", imod_rotten),
              (assign, ":continue", 0),
            (try_end),
            (eq, ":continue", 1),
            (item_get_slot, ":food_bonus", ":item_no", slot_item_food_bonus),
            ## CC
            (store_add, ":food_bonus_multi", "$g_twice_consum_food", 1),
            (val_mul, ":food_bonus", ":food_bonus_multi"),
            ## CC
########################################################################################################################
# LAV MODIFICATIONS START (TRADE GOODS MOD)
########################################################################################################################
          (try_begin),
            (eq, ":item_modifier", imod_cheap),
            (val_sub, ":food_bonus", 2),
          (else_try),
            (eq, ":item_modifier", imod_fine),
            (val_add, ":food_bonus", 1),
          (else_try),
            (eq, ":item_modifier", imod_well_made),
            (val_add, ":food_bonus", 2),
          (else_try),
            (eq, ":item_modifier", imod_strong),
            (val_add, ":food_bonus", 3),
          (else_try),
            (eq, ":item_modifier", imod_lordly),
            (val_add, ":food_bonus", 5),
          (else_try),
            (eq, ":item_modifier", imod_exquisite),
            (val_add, ":food_bonus", 6),
          (try_end),
		  (val_max, ":food_bonus", 0), # Floris 2.5 Bugfix - Windyplains - Prevents cheap, raw olives being -1 or anything other combo < 0.
          (assign, reg1, ":food_bonus"),
#          (set_result_string, "@+{reg1} to party morale"),
#          (set_trigger_result, 0x4444FF),
          (try_begin),
            (ge, reg1, 0),
            (set_result_string, "@+{reg1} to party morale"),
            (set_trigger_result, 0x4444FF),
          (else_try),
            (set_result_string, "@{reg1} to party morale"),
            (set_trigger_result, 0xFF4444),
          (try_end),
########################################################################################################################
# LAV MODIFICATIONS END (TRADE GOODS MOD)
########################################################################################################################
          (try_end),
        (else_try),
          (is_between, ":item_no", readable_books_begin, readable_books_end),
          ## CC
          (try_begin),
            (eq, ":extra_text_id", 0),
            (try_begin),
              (eq, ":item_no", "itm_book_tactics"),
              (str_store_string, s1, "@tactics"),
            (else_try),
              (eq, ":item_no", "itm_book_persuasion"),
              (str_store_string, s1, "@persuasion"),
            (else_try),
              (eq, ":item_no", "itm_book_leadership"),
              (str_store_string, s1, "@leadership"),
            (else_try),
              (eq, ":item_no", "itm_book_intelligence"),
              (str_store_string, s1, "@intelligence"),
            (else_try),
              (eq, ":item_no", "itm_book_prisoner_management"),
              (str_store_string, s1, "@prisoner management"),
            (else_try),
              (eq, ":item_no", "itm_book_trade"),
              (str_store_string, s1, "@trade"),
            (else_try),
              (eq, ":item_no", "itm_book_weapon_mastery"),
              (str_store_string, s1, "@weapon mastery"),
            (else_try),
              (eq, ":item_no", "itm_book_engineering"),
              (str_store_string, s1, "@engineer"),
              ## Floris 2.5 Bugfix - Windyplains - Books not covered resulting in +1 to X odd strings.
            (else_try),
              (eq, ":item_no", "itm_book_bible"),
              (str_store_string, s1, "@charisma"),
            (else_try),
              (eq, ":item_no", "itm_book_necronomicon"),
              (str_store_string, s1, "@looting"),
			# (else_try),
              # (eq, ":item_no", "itm_book_first_aid_reference"), # Primo Auxilium
              # (str_store_string, s1, "@first aid"),
            # (else_try),
              # (eq, ":item_no", "itm_book_spotting_reference"), # Scientia Servandi
              # (str_store_string, s1, "@spotting"),
            # (else_try),
              # (eq, ":item_no", "itm_book_pathfinding_reference"), # Lore of Calradia
              # (str_store_string, s1, "@path-finding"),
              ## Floris books end
            (try_end),
			## Floris 2.5 Bugfix end
            (set_result_string, "@+1 to {s1} after reading"),
            (set_trigger_result, 0x4444FF),
          (else_try),
            (eq, ":extra_text_id", 1),
            (item_get_slot, reg1, ":item_no", slot_item_intelligence_requirement),
            (set_result_string, "@Requires {reg1} intelligence to read"),
            (store_attribute_level, ":int", "trp_player", ca_intelligence),
            (try_begin),
              (lt, ":int", reg1),
              (set_trigger_result, 0xFF4444),
            (else_try),
              (set_trigger_result, 0x44FF44),
            (try_end),
          (else_try),
            (eq, ":extra_text_id", 2),
            (item_get_slot, ":progress", ":item_no", slot_item_book_reading_progress),
            (store_div, reg1, ":progress", 10),
            (store_mod, reg2, ":progress", 10),
            (str_store_string, s0, "@Reading Progress:^{playername}:{reg1}.{reg2}%"),
            (try_for_range, ":stack_troop", companions_begin, companions_end),
              (main_party_has_troop, ":stack_troop"),
              (str_store_troop_name, s1, ":stack_troop"),
              (call_script, "script_get_book_read_slot", ":stack_troop", ":item_no"),
              (assign, ":slot_no", reg0),
              (troop_get_slot, ":progress_npc", "trp_book_reading_progress", ":slot_no"),
              (store_div, reg1, ":progress_npc", 10),
              (store_mod, reg2, ":progress_npc", 10),
              (str_store_string, s0, "@{s0}^{s1}:{reg1}.{reg2}%"),
            (try_end),
            (set_result_string, s0),
            (set_trigger_result, 0xFFEEDD),
            ## CC
          (try_end),
        (else_try),
          (is_between, ":item_no",reference_books_begin,reference_books_end),
          (try_begin),
            (eq, ":extra_text_id", 0),
            (try_begin),
              (eq, ":item_no", "itm_book_wound_treatment_reference"),
              (str_store_string, s1, "@wound treament"),
            (else_try),
              (eq, ":item_no", "itm_book_training_reference"),
              (str_store_string, s1, "@trainer"),
            (else_try),
              (eq, ":item_no", "itm_book_surgery_reference"),
              (str_store_string, s1, "@surgery"),
              ## CC
            (else_try),
              (eq, ":item_no", "itm_book_spotting_reference"),
              (str_store_string, s1, "@spotting"),
            (else_try),
              (eq, ":item_no", "itm_book_first_aid_reference"),
              (str_store_string, s1, "@first aid"),
            (else_try),
              (eq, ":item_no", "itm_book_pathfinding_reference"),
              (str_store_string, s1, "@pathfinding"),
            (try_end),
            ## CC
			(neq, ":item_no", "itm_book_trade_ledger"), # Caba's Trade Ledger since it doesn't provide a bonus.
            (set_result_string, "@+1 to {s1} while in inventory"),
            (set_trigger_result, 0x4444FF),
          (try_end),
        (else_try),
		    (try_begin), #Floris 2.52 addition for the "all_items" presentation to add difficulty
            ## CC
			  (neq, ":item_modifier", imod_plain),
			  (try_begin),
			  	(eq, ":extra_text_id", 0),
				(set_result_string, "@ ^"),
				(set_trigger_result, 0xFFFFFF),
			  (else_try),
				(eq, ":extra_text_id", 1),
				(item_get_slot, ":imod_multiplier", ":item_modifier", slot_item_modifier_multiplier),
				(store_div, reg1, ":imod_multiplier", 100),
				(store_mod, reg2, ":imod_multiplier", 100),
				(set_result_string, "@price: base price*{reg1}.{reg2}"),
				(set_trigger_result, 0xFFFFFF),
			  (else_try),
				(eq, ":extra_text_id", 2),
				(try_begin),
				  (eq, ":type", itp_type_horse),
				  (try_begin),
					(eq, ":item_modifier", imod_swaybacked),
					(set_result_string, "@-2 speed^-2 maneuver"),
				  (else_try),
					(eq, ":item_modifier", imod_lame),
					(set_result_string, "@-5 speed^-5 maneuver"),
				  (else_try),
					(eq, ":item_modifier", imod_heavy),
					(set_result_string, "@+3 armor^+4 charge^+10 hit points"),
				  (else_try),
					(eq, ":item_modifier", imod_timid),
					(set_result_string, "@-1 requirement of riding"),
				  (else_try),
					(eq, ":item_modifier", imod_stubborn),
					(set_result_string, "@+1 requirement of riding^+5 hit points"),
				  (else_try),
					(eq, ":item_modifier", imod_spirited),
					(set_result_string, "@+1 speed^+1 armor^+1 charge"),
				  (else_try),
					(eq, ":item_modifier", imod_champion),
					(set_result_string, "@+2 requirement of riding^+2 speed^+2 armor^+2 charge"),
				  (try_end),
				(else_try),
				  (eq, ":type", itp_type_shield),
				  (try_begin),
					(eq, ":item_modifier", imod_cracked),
					(set_result_string, "@-56 hit points^-4 resistance"),
				  (else_try),
					(eq, ":item_modifier", imod_battered),
					(set_result_string, "@-26 hit points^-2 resistance"),
				  (else_try),
					(eq, ":item_modifier", imod_thick),
					(set_result_string, "@+47 hit points^+2 resistance"),
				  (else_try),
					(eq, ":item_modifier", imod_reinforced),
					(set_result_string, "@+83 hit points^+4 resistance"),
				  (try_end),
				(else_try),
				  (this_or_next|eq, ":type", itp_type_head_armor),
				  (this_or_next|eq, ":type", itp_type_body_armor),
				  (this_or_next|eq, ":type", itp_type_foot_armor),
				  (eq, ":type", itp_type_hand_armor),
				  
				  (item_get_slot, ":head_armor", ":item_no", slot_item_head_armor),
				  (item_get_slot, ":body_armor", ":item_no", slot_item_body_armor),
				  (item_get_slot, ":leg_armor", ":item_no", slot_item_leg_armor),
				  
				  (assign, reg1, 0),
				  (assign, reg2, 0),
				  (assign, reg3, 0),
				  (try_begin),
					(gt, ":head_armor", 0),
					(assign, reg1, 1),
				  (try_end),
				  (try_begin),
					(gt, ":body_armor", 0),
					(assign, reg2, 1),
				  (try_end),
				  (try_begin),
					(gt, ":leg_armor", 0),
					(assign, reg3, 1),
				  (try_end),
				  
				  (try_begin),
					(eq, ":item_modifier", imod_cracked),
					(str_store_string, s1, "@ -"),
					(assign, reg4, 4),
				  (else_try),
					(eq, ":item_modifier", imod_rusty),
					(str_store_string, s1, "@ -"),
					(assign, reg4, 3),
				  (else_try),
					(eq, ":item_modifier", imod_battered),
					(str_store_string, s1, "@ -"),
					(assign, reg4, 2),
				  (else_try),
					(eq, ":item_modifier", imod_crude),
					(str_store_string, s1, "@ -"),
					(assign, reg4, 1),
				  (else_try),
					(eq, ":item_modifier", imod_tattered),
					(str_store_string, s1, "@ -"),
					(assign, reg4, 3),
				  (else_try),
					(eq, ":item_modifier", imod_ragged),
					(str_store_string, s1, "@ -"),
					(assign, reg4, 2),
				  (else_try),
					(eq, ":item_modifier", imod_sturdy),
					(str_store_string, s1, "@ +"),
					(assign, reg4, 1),
				  (else_try),
					(eq, ":item_modifier", imod_thick),
					(str_store_string, s1, "@ +"),
					(assign, reg4, 2),
				  (else_try),
					(eq, ":item_modifier", imod_hardened),
					(str_store_string, s1, "@ +"),
					(assign, reg4, 3),
				  (else_try),
					(eq, ":item_modifier", imod_reinforced),
					(str_store_string, s1, "@ +"),
					(assign, reg4, 4),
				  (else_try),
					(eq, ":item_modifier", imod_lordly),
					(str_store_string, s1, "@ +"),
					(assign, reg4, 6),
				  (try_end),
				  (set_result_string, "@{reg1?{s1}{reg4} to head armor^:}{reg2?{s1}{reg4} to body armor^:}{reg3?{s1}{reg4} to leg armor:}"),
				(else_try),
				  (this_or_next|eq, ":type", itp_type_one_handed_wpn),
				  (this_or_next|eq, ":type", itp_type_two_handed_wpn),
				  (this_or_next|eq, ":type", itp_type_polearm),
				  (eq, ":type", itp_type_crossbow),
				  
				  (item_get_slot, ":swing_damage", ":item_no", slot_item_swing_damage),
				  (item_get_slot, ":thrust_damage", ":item_no", slot_item_thrust_damage),
				  (store_mod, reg1, ":swing_damage", 256),
				  (store_mod, reg2, ":thrust_damage", 256),
				  (item_get_slot, reg3, ":item_no", slot_item_difficulty),
				  
				  (try_begin),
					(eq, ":item_modifier", imod_cracked),
					(set_result_string, "@{reg1?-5 swing damage^:}{reg2?-5 thrust damage^:}"),
				  (else_try),
					(eq, ":item_modifier", imod_rusty),
					(set_result_string, "@{reg1?-3 swing damage^:}{reg2?-3 thrust damage^:}"),
				  (else_try),
					(eq, ":item_modifier", imod_bent),
					(set_result_string, "@{reg1?-3 swing damage^:}{reg2?-3 thrust damage^:}-3 speed"),
				  (else_try),
					(eq, ":item_modifier", imod_chipped),
					(set_result_string, "@{reg1?-1 swing damage^:}{reg2?-1 thrust damage^:}"),
				  (else_try),
					(eq, ":item_modifier", imod_balanced),
					(set_result_string, "@{reg1?+3 swing damage^:}{reg2?+3 thrust damage^:}+3 speed"),
				  (else_try),
					(eq, ":item_modifier", imod_tempered),
					(set_result_string, "@{reg1?+4 swing damage^:}{reg2?+4 thrust damage^:}"),
				  (else_try),
					(eq, ":item_modifier", imod_masterwork),
					(set_result_string, "@{reg1?+5 swing damage^:}{reg2?+5 thrust damage^:}+1 speed{reg3?^+4 requirement of strength:}"),
				  (else_try),
					(eq, ":item_modifier", imod_heavy),
					(set_result_string, "@{reg1?+2 swing damage^:}{reg2?+2 thrust damage^:}-2 speed{reg3?^+1 requirement of strength:}"),
				  (try_end),
				(else_try),
				  (eq, ":type", itp_type_bow),
				  (item_get_slot, reg3, ":item_no", slot_item_difficulty),
				  
				  (try_begin),
					(eq, ":item_modifier", imod_cracked),
					(set_result_string, "@-5 damage"),
				  (else_try),
					(eq, ":item_modifier", imod_bent),
					(set_result_string, "@-3 damage^-3 speed"),
				  (else_try),
					(eq, ":item_modifier", imod_strong),
					(set_result_string, "@+3 damage^-3 speed{reg3?^+2 requirement of power draw:}"),
				  (else_try),
					(eq, ":item_modifier", imod_masterwork),
					(set_result_string, "@+5 damage^+1 speed{reg3?^+4 requirement of power draw:}"),
				  (try_end),
				(else_try),
				  (eq, ":type", itp_type_thrown),
				  (item_get_slot, reg3, ":item_no", slot_item_difficulty),
				  
				  (try_begin),
					(eq, ":item_modifier", imod_large_bag),
					(set_result_string, "@+13% max ammo"),
				  (else_try),
					(eq, ":item_modifier", imod_bent),
					(set_result_string, "@-3 damage^-3 speed"),
				  (else_try),
					(eq, ":item_modifier", imod_heavy),
					(set_result_string, "@+2 damage^-2 speed{reg3?^+1 requirement of power throw:}"),
				  (else_try),
					(eq, ":item_modifier", imod_balanced),
					(set_result_string, "@+3 damage^+3 speed"),
				  (try_end),
				(else_try),
				  (this_or_next|eq, ":type", itp_type_arrows),
				  (eq, ":type", itp_type_bolts),
				  (try_begin),
					(eq, ":item_modifier", imod_large_bag),
					(set_result_string, "@+13% max ammo"),
				  (else_try),
					(eq, ":item_modifier", imod_bent),
					(set_result_string, "@-3 damage"),
				  (try_end),
				(try_end),
				(set_trigger_result, 0x8080FF),
			  (try_end),
		    ## CC
            (else_try), #Floris 2.52 - begin - addition for the "all_items" presentation to add difficulty
			    (eq, ":extra_text_id", 0),
				(is_presentation_active, "prsnt_all_items"),
				(item_get_slot, reg3, ":item_no", slot_item_difficulty),
				(gt, reg3, 0),
				(str_clear, s1),
				(try_begin),
					(eq, ":type", itp_type_horse),
					(str_store_string, s1, "@Riding"),
				(else_try),
					(this_or_next|is_between, ":type", itp_type_one_handed_wpn, itp_type_arrows), #all melee weapons
					(this_or_next|is_between, ":type", itp_type_head_armor, itp_type_bullets), #all armors, pistols and muskets
					(eq, ":type", itp_type_crossbow),
					(str_store_string, s1, "@Strength"),
				(else_try),
					(eq, ":type", itp_type_bow),
					(str_store_string, s1, "@Power Draw"),
				(else_try),
					(eq, ":type", itp_type_thrown),
					(str_store_string, s1, "@Power Throw"),
				(else_try),
					(eq, ":type", itp_type_shield),
					(str_store_string, s1, "@Shield"),
				(try_end),
				(set_result_string, "@Requires {s1}: {reg3}"),
				(set_trigger_result, 0x8080FF),
            (try_end), #Floris - end
        (try_end),
    ]),
    
    #script_game_on_disembark:
    # This script is called from the game engine when the player reaches the shore with a ship.
    # INPUT: pos0 = disembark position
    # OUTPUT: none
    ("game_on_disembark",
      [	#(party_get_position, pos1, "p_main_party"),
		#(party_set_position, "p_main_party", pos0),
		#(try_begin),
		#	(map_get_land_position_around_position, pos2, pos1, 0.5),
		#	(party_set_position, "p_main_party", pos2),
		#	(party_get_current_terrain, ":terrain", "p_main_party"),
		#	(this_or_next|neq, ":terrain", 1),
		#	(neq, ":terrain", 9),
		#	(party_set_position, "p_main_party", pos0),
			(jump_to_menu, "mnu_disembark"),
		#(else_try),
		#	(display_message, "@You cant land on these cliffs. Look for a location that is less dangerous, unless you wish to lose your life."),
		#(try_end),
    ]),
    
    
    #script_game_context_menu_get_buttons:
    # This script is called from the game engine when the player clicks the right mouse button over a party on the map.
    # INPUT: arg1 = party_no
    # OUTPUT: none, fills the menu buttons
    ("game_context_menu_get_buttons",
      [
        (store_script_param, ":party_no", 1),
        (try_begin),
          (neq, ":party_no", "p_main_party"),
          (context_menu_add_item, "@Move here", cmenu_move),
		  (assign, "$g_camp_mode", 1),
        (try_end),
        
		 (try_begin),
		   (is_between, ":party_no", centers_begin, centers_end),
		   (context_menu_add_item, "@View notes", 1),
		 (else_try),
		   (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
		   (gt, ":num_stacks", 0),
		   (party_stack_get_troop_id, ":troop_no", ":party_no", 0),
		   ##diplomacy start+ support for promoted kingdom ladies
		   (is_between, ":troop_no", heroes_begin, heroes_end),
		   (this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
		   ##diplomacy end+
		   (is_between, ":troop_no", active_npcs_begin, active_npcs_end),
		   (context_menu_add_item, "@View notes", 2),
		 (try_end),
        
        (try_begin),
          (neq, ":party_no", "p_main_party"),
          (store_faction_of_party, ":party_faction", ":party_no"),
          
          (this_or_next|eq, ":party_faction", "$players_kingdom"),
          (this_or_next|eq, ":party_faction", "fac_player_supporters_faction"),
          (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_caravan),
          
          (neg|is_between, ":party_no", centers_begin, centers_end),
          
          (context_menu_add_item, "@Accompany", cmenu_follow),
        (try_end),
    ]),
    
    #script_game_event_context_menu_button_clicked:
    # This script is called from the game engine when the player clicks on a button at the right mouse menu.
    # INPUT: arg1 = party_no, arg2 = button_value
    # OUTPUT: none
    ("game_event_context_menu_button_clicked",
      [(store_script_param, ":party_no", 1),
        (store_script_param, ":button_value", 2),
        (try_begin),
          (eq, ":button_value", 1),
          (change_screen_notes, 3, ":party_no"),
        (else_try),
          (eq, ":button_value", 2),
          (party_stack_get_troop_id, ":troop_no", ":party_no", 0),
          (change_screen_notes, 1, ":troop_no"),
        (try_end),
    ]),
    
    #script_game_get_skill_modifier_for_troop
    # This script is called from the game engine when a skill's modifiers are needed
    # INPUT: arg1 = troop_no, arg2 = skill_no
    # OUTPUT: trigger_result = modifier_value
    ("game_get_skill_modifier_for_troop",
      [(store_script_param, ":troop_no", 1),
        (store_script_param, ":skill_no", 2),
        (assign, ":modifier_value", 0),
        (try_begin),
          (eq, ":skill_no", "skl_wound_treatment"),
          (call_script, "script_get_troop_item_amount", ":troop_no", "itm_book_wound_treatment_reference"),
          (gt, reg0, 0),
          (val_add, ":modifier_value", 1),
        (else_try),
          (eq, ":skill_no", "skl_trainer"),
          (call_script, "script_get_troop_item_amount", ":troop_no", "itm_book_training_reference"),
          (gt, reg0, 0),
          (val_add, ":modifier_value", 1),
        (else_try),
          (eq, ":skill_no", "skl_surgery"),
          (call_script, "script_get_troop_item_amount", ":troop_no", "itm_book_surgery_reference"),
          (gt, reg0, 0),
          (val_add, ":modifier_value", 1),
          ## CC
        (else_try),
          (eq, ":skill_no", "skl_pathfinding"),
          (call_script, "script_get_troop_item_amount", ":troop_no", "itm_book_pathfinding_reference"),
          (gt, reg0, 0),
          (val_add, ":modifier_value", 1),
        (else_try),
          (eq, ":skill_no", "skl_spotting"),
          (call_script, "script_get_troop_item_amount", ":troop_no", "itm_book_spotting_reference"),
          (gt, reg0, 0),
          (val_add, ":modifier_value", 1),
        (else_try),
          (eq, ":skill_no", "skl_first_aid"),
          (call_script, "script_get_troop_item_amount", ":troop_no", "itm_book_first_aid_reference"),
          (gt, reg0, 0),
          (val_add, ":modifier_value", 1),
        (else_try),
          (eq, ":skill_no", "skl_riding"),
          (eq, "$g_encumbrance_penalty", 1),
          (this_or_next|eq, ":troop_no", "trp_player"),
          (is_between, ":troop_no", companions_begin, companions_end),
		  (main_party_has_troop, ":troop_no"), ##Floris fix so companions-as-lords aren't affected
          (store_attribute_level, ":agi", ":troop_no", ca_agility),
          (call_script, "script_get_total_equipment_weight", ":troop_no"),
          (assign, ":total_weight", reg0),
          (val_sub, ":total_weight", 10),
          (val_sub, ":total_weight", ":agi"),
          (val_div, ":total_weight", 10),
          (store_sub, ":modifier_value", 0, ":total_weight"),
          (val_min, ":modifier_value", 0),
        (else_try),
          (eq, ":skill_no", "skl_power_draw"),
          (eq, "$g_encumbrance_penalty", 1),
          (this_or_next|eq, ":troop_no", "trp_player"),
          (is_between, ":troop_no", companions_begin, companions_end),
		  (main_party_has_troop, ":troop_no"), ##Floris fix so companions-as-lords aren't affected
          (store_attribute_level, ":str", ":troop_no", ca_strength),
          (call_script, "script_get_total_equipment_weight", ":troop_no"),
          (assign, ":total_weight", reg0),
          (val_sub, ":total_weight", 10),
          (val_sub, ":total_weight", ":str"),
          (val_div, ":total_weight", 10),
          (store_sub, ":modifier_value", 0, ":total_weight"),
          (val_min, ":modifier_value", 0),
        (else_try),
          (eq, ":skill_no", "skl_horse_archery"),
          (eq, "$g_encumbrance_penalty", 1),
          (this_or_next|eq, ":troop_no", "trp_player"),
          (is_between, ":troop_no", companions_begin, companions_end),
		  (main_party_has_troop, ":troop_no"), ##Floris fix so companions-as-lords aren't affected
          (store_attribute_level, ":agi", ":troop_no", ca_agility),
          (store_attribute_level, ":str", ":troop_no", ca_strength),
          (call_script, "script_get_total_equipment_weight", ":troop_no"),
          (assign, ":total_weight", reg0),
          (val_mul, ":total_weight", 2),
          (val_sub, ":total_weight", 20),
          (val_sub, ":total_weight", ":agi"),
          (val_sub, ":total_weight", ":str"),
          (val_div, ":total_weight", 10),
          (store_sub, ":modifier_value", 0, ":total_weight"),
          (val_min, ":modifier_value", 0),
          ## CC
        (try_end),
		#Floris Stat Bonus Begins
		(try_begin),
			(troop_is_hero, ":troop_no"),
			(assign, ":party", -1),
			(try_begin),
				(neg|main_party_has_troop, ":troop_no"),
				(troop_get_slot, ":leaded_party", ":troop_no", slot_troop_leaded_party),
				(ge, ":leaded_party", 1), #it needs to be 1, not 0. 0 means the troop doesn't lead a party
				(assign, ":party", ":leaded_party"),
			(else_try),
				(main_party_has_troop, ":troop_no"), #add this to take into account the player and hero companions
				(assign, ":party", "p_main_party"),
			(try_end),
			(ge, ":party", 0),
			(party_is_active, ":party"),
			(try_begin),
				(eq, ":skill_no", "skl_trade"),
				(call_script, "script_get_party_troop_count", ":party", "trp_skill_merchant"),
				(try_begin),
					(gt, reg0, 7),
					(val_add, ":modifier_value", 3),
				(else_try),
					(gt, reg0, 4),
					(val_add, ":modifier_value", 2),	
				(else_try),
					(gt, reg0, 0),
					(val_add, ":modifier_value", 1),
				(try_end),
			(else_try),
				(eq, ":skill_no", "skl_wound_treatment"),
				(call_script, "script_get_party_troop_count", ":party", "trp_skill_monk"),
				(assign, ":count", reg0),
				(call_script, "script_get_party_troop_count", ":party", "trp_skill_priest"),
				(val_add, ":count", reg0),
				(try_begin),
					(gt, ":count", 9),
					(val_add, ":modifier_value", 3),
				(else_try),
					(gt, ":count", 4),
					(val_add, ":modifier_value", 2),	
				(else_try),
					(gt, ":count", 0),
					(val_add, ":modifier_value", 1),
				(try_end),				
			(else_try),
				(eq, ":skill_no", "skl_surgery"),
				(call_script, "script_get_party_troop_count", ":party", "trp_skill_surgeon"),
				(try_begin),
					(gt, reg0, 9),
					(val_add, ":modifier_value", 3),
				(else_try),
					(gt, reg0, 4),
					(val_add, ":modifier_value", 2),	
				(else_try),
					(gt, reg0, 0),
					(val_add, ":modifier_value", 1),
				(try_end),				
			(else_try),
				(eq, ":skill_no", "skl_leadership"),
				(call_script, "script_get_party_troop_count", ":party", "trp_skill_bishop"),
				(try_begin),
					(gt, reg0, 0),
					(val_add, ":modifier_value", 1),
				(try_end),					
			(else_try),
				(eq, ":skill_no", "skl_foraging"),
				(call_script, "script_get_party_troop_count", ":party", "trp_skill_hunter"),
				(try_begin),
					(gt, reg0, 9),
					(val_add, ":modifier_value", 3),
				(else_try),
					(gt, reg0, 4),
					(val_add, ":modifier_value", 2),	
				(else_try),
					(gt, reg0, 0),
					(val_add, ":modifier_value", 1),
				(try_end),					
			(else_try),
				(eq, ":skill_no", "skl_tracking"),
				(call_script, "script_get_party_troop_count", ":party", "trp_skill_hunter"),
				(try_begin),
					(gt, reg0, 4),
					(val_add, ":modifier_value", 2),	
				(else_try),
					(gt, reg0, 0),
					(val_add, ":modifier_value", 1),
				(try_end),
			(else_try),
				(eq, ":skill_no", "skl_spotting"),
				(call_script, "script_get_party_troop_count", ":party", "trp_skill_scout"),
				(try_begin),
					(gt, reg0, 9),
					(val_add, ":modifier_value", 2),
				(else_try),
					(gt, reg0, 4),
					(val_add, ":modifier_value", 1),	
				(try_end),	
			(else_try),
				(eq, ":skill_no", "skl_looting"),
				(troop_get_slot,":bandit_looter","$troop_trees",slot_bandit_looter),
				(call_script, "script_get_party_troop_count", ":party", ":bandit_looter"),
				(try_begin),
					(gt, reg0, 29),
					(val_add, ":modifier_value", 3),	
				(else_try),
					(gt, reg0, 19),
					(val_add, ":modifier_value", 2),	
				(else_try),
					(gt, reg0, 9),
					(val_add, ":modifier_value", 1),
				(try_end),
			(else_try),
				(eq, ":skill_no", "skl_prisoner_management"),
				(assign, ":count", 0),
				##Floris MTT begin
				(troop_get_slot,":bandit_slave_driver","$troop_trees",slot_bandit_slave_driver),
				(call_script, "script_get_party_troop_count", ":party", ":bandit_slave_driver"),
				(val_add, ":count", reg0),
				(troop_get_slot,":bandit_slave_hunter","$troop_trees",slot_bandit_slave_hunter),
				(call_script, "script_get_party_troop_count", ":party", ":bandit_slave_hunter"),
				(val_add, ":count", reg0),				
				(troop_get_slot,":bandit_slave_crusher","$troop_trees",slot_bandit_slave_crusher),
				(call_script, "script_get_party_troop_count", ":party", ":bandit_slave_crusher"),
				(val_add, ":count", reg0),			
				(troop_get_slot,":bandit_slaver_chief","$troop_trees",slot_bandit_slaver_chief),
				(call_script, "script_get_party_troop_count", ":party", ":bandit_slaver_chief"),
				(val_add, ":count", reg0),
				(troop_get_slot,":bandit_manhunter","$troop_trees",slot_bandit_manhunter),
				(call_script, "script_get_party_troop_count", ":party", ":bandit_manhunter"),
				(val_add, ":count", reg0),
				##Floris MTT end
				(try_begin),
					(gt, ":count", 39),
					(val_add, ":modifier_value", 3),	
				(else_try),
					(gt, ":count", 24),
					(val_add, ":modifier_value", 2),	
				(else_try),
					(gt, ":count", 9),
					(val_add, ":modifier_value", 1),
				(try_end),
			(else_try),			
				(eq, ":skill_no", "skl_inventory_management"),
				(assign, ":count", 0),
				(call_script, "script_get_party_troop_count", ":party", "trp_slave_swadian"),
				(val_add, ":count", reg0),
				(call_script, "script_get_party_troop_count", ":party", "trp_slave_vaegir"),
				(val_add, ":count", reg0),			
				(call_script, "script_get_party_troop_count", ":party", "trp_slave_khergit"),
				(val_add, ":count", reg0),			
				(call_script, "script_get_party_troop_count", ":party", "trp_slave_nord"),
				(val_add, ":count", reg0),			
				(call_script, "script_get_party_troop_count", ":party", "trp_slave_rhodok"),
				(val_add, ":count", reg0),
				(call_script, "script_get_party_troop_count", ":party", "trp_slave_sarranid"),
				(val_add, ":count", reg0),	
				(try_begin),
					(gt, ":count", 29),
					(val_add, ":modifier_value", 3),	
				(else_try),		
					(gt, ":count", 19),
					(val_add, ":modifier_value", 2),	
				(else_try),
					(gt, ":count", 9),
					(val_add, ":modifier_value", 1),
				(try_end),			
			(try_end),
      (try_end),
      (set_trigger_result, ":modifier_value"),
    ]),
    #Floris Stat Bonus Ends
	
    # Note to modders: Uncomment these if you'd like to use the following.
    
    ##  #script_game_check_party_sees_party
    ##  # This script is called from the game engine when a party is inside the range of another party
    ##  # INPUT: arg1 = party_no_seer, arg2 = party_no_seen
    ##  # OUTPUT: trigger_result = true or false (1 = true, 0 = false)
    ##  ("game_check_party_sees_party",
    ##   [
    ##     (store_script_param, ":party_no_seer", 1),
    ##     (store_script_param, ":party_no_seen", 2),
    ##     (set_trigger_result, 1),
    ##    ]),
    ##
    
	##diplomacy start+
	#Enable script_game_check_party_sees_party to prevent compassionate lords from
	#attacking villagers and merchant caravans.

	#script_game_check_party_sees_party
	# This script is called from the game engine when a party is inside the range of another party
	# INPUT: arg1 = party_no_seer, arg2 = party_no_seen
	# OUTPUT: trigger_result = true or false (1 = true, 0 = false)
		("game_check_party_sees_party",	
		[
		(store_script_param_1, ":party_no_seer"),
		(store_script_param_2, ":party_no_seen"),
		
		(assign, ":trigger_result", 1),
		(assign, ":save_reg0", reg0),
		
		#Lords who dislike raiding caravans should not attack village_farmer or kingdom_caravan
		#parties.  Achieve this by stopping them from seeing them.
		(try_begin),
		(gt, ":party_no_seer", spawn_points_end),
		(gt, ":party_no_seen", spawn_points_end),
			
			#Only apply this when the "seer" is a kingdom hero party
			(party_slot_eq, ":party_no_seer", slot_party_type, spt_kingdom_hero_party),
			
			#Only needed if the seen party is of a hostile faction
			(call_script, "script_get_relation_between_parties", ":party_no_seer", ":party_no_seen"),
			(lt, reg0, 0),
			
			#Only apply this when the seen party is a merchant caravan or villagers
			#(party_get_template_id, ":template", ":party_no_seen"),
			(this_or_next|party_slot_eq, ":party_no_seen", slot_party_type, spt_kingdom_caravan),
			(this_or_next|party_slot_eq,":party_no_seen", slot_party_type, dplmc_spt_gift_caravan),#custom diplomacy caravan
				(party_slot_eq, ":party_no_seen", slot_party_type, spt_village_farmer),
				
			#Never apply this when the seen party is engaging in hostile actions
			(party_get_battle_opponent, reg0, ":party_no_seen"),
			(lt, reg0, 0),
			(neg|party_slot_eq, ":party_no_seen", slot_party_ai_state, spai_besieging_center),
			(neg|party_slot_eq, ":party_no_seen", slot_party_ai_state, spai_raiding_around_center),
			(neg|party_slot_eq, ":party_no_seen", slot_party_ai_state, spai_engaging_army),
			(neg|party_slot_eq, ":party_no_seen", slot_party_ai_state, spai_accompanying_army),
			(neg|party_slot_eq, ":party_no_seen", slot_party_ai_state, spai_screening_army),
			
			
			#Only apply this when the leader is tmt_humanitarian, lrep_benefactor, or lrep_moralist
			(party_get_num_companion_stacks, ":num_stacks", ":party_no_seer"),
			(ge, ":num_stacks", 1),
			(party_stack_get_troop_id, ":leader", ":party_no_seer", 0),
			(ge, ":leader", 1),
			(troop_is_hero, ":leader"),
			(call_script, "script_dplmc_get_troop_morality_value", ":leader", tmt_humanitarian),
			(ge, reg0, 0),# (never apply for leaders who like raiding caravans and attacking villagers)
			(this_or_next|ge, reg0, 1),
			(this_or_next|troop_slot_eq, ":leader", slot_lord_reputation_type, lrep_benefactor),
				(troop_slot_eq, ":leader", slot_lord_reputation_type, lrep_moralist),
			(assign, ":trigger_result", 0),
		(try_end),
		
		(assign, reg0, ":save_reg0"),
		(set_trigger_result, ":trigger_result"),
		]),
	##diplomacy end+
	
    ##diplomacy 3.2 begin
    #script_game_get_party_speed_multiplier
    # This script is called from the game engine when a skill's modifiers are needed
    # INPUT: arg1 = party_no
    # OUTPUT: trigger_result = multiplier (scaled by 100, meaning that giving 100 as the trigger result does not change the party speed)
 ("game_get_party_speed_multiplier",
  [
    (store_script_param_1, ":party_no"),

    (assign,":speed_multiplier",100),

    (try_begin),
      (this_or_next|eq,":party_no","p_main_party"),
      (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
      (party_get_skill_level, ":pathfinding_skill", ":party_no", skl_pathfinding),
      (val_mul,":pathfinding_skill",3),
      (val_add,":speed_multiplier",":pathfinding_skill"),
    (try_end),

    (try_begin),
      (eq,":party_no","p_main_party"),
      (eq,"$g_move_fast", 1),
      (val_mul,":speed_multiplier",2),
	##CC #Floris
	(else_try),
	  (eq,":party_no","p_main_party"),
	  (call_script, "script_get_inventory_weight_of_whole_party"),
	  (val_div, reg0, 100),
	  (val_sub,":speed_multiplier", reg0),
	##CC #Floris
    (try_end),

    (val_max, ":speed_multiplier", 0),
    (set_trigger_result, ":speed_multiplier"),
   ]),

    ##diplomacy 3.2 end
    
    # script_npc_get_troop_wage
    # This script is called from module system to calculate troop wages for npc parties.
    # Input:
    # param1: troop_id
    # Output: reg0: weekly wage
    
    ("npc_get_troop_wage",
      [
        (store_script_param_1, ":troop_id"),
        (assign,":wage", 0),
        (try_begin),
          (troop_is_hero, ":troop_id"),
        (else_try),
          (store_character_level, ":wage", ":troop_id"),
          (val_mul, ":wage", ":wage"),
          (val_add, ":wage", 50),
          (val_div, ":wage", 30),
          (troop_is_mounted, ":troop_id"),
          (val_mul, ":wage", 5),
          (val_div, ":wage", 4),
        (try_end),
        (assign, reg0, ":wage"),
    ]),
    
    #script_setup_talk_info
    # INPUT: $g_talk_troop, $g_talk_troop_relation
    ("setup_talk_info",
		[
		  ##diplomacy start+ Ensure $character_gender is set correctly (it should have been set during character creation)
		  (try_begin),
			 (call_script, "script_cf_dplmc_troop_is_female", "trp_player"),
			 (assign, "$character_gender", 1),
		  (else_try),
			 (assign, "$character_gender", 0),
		  (try_end),
		  ##diplomacy end+
        (talk_info_set_relation_bar, "$g_talk_troop_relation"),
        (str_store_troop_name, s61, "$g_talk_troop"),
        (str_store_string, s61, "@{!} {s61}"),
        (assign, reg1, "$g_talk_troop_relation"),
        (str_store_string, s62, "str_relation_reg1"),
        (talk_info_set_line, 0, s61),
        (talk_info_set_line, 1, s62),
        (call_script, "script_describe_relation_to_s63", "$g_talk_troop_relation"),
        (talk_info_set_line, 3, s63),
    ]),
    
    ## CC
    #NPC companion changes begin
    #script_setup_talk_info_companions
    ("setup_talk_info_companions",
		[
		  ##diplomacy start+ Ensure $character_gender is set correctly (it should have been set during character creation)
		  (try_begin),
			 (call_script, "script_cf_dplmc_troop_is_female", "trp_player"),
			 (assign, "$character_gender", 1),
		  (else_try),
			 (assign, "$character_gender", 0),
		  (try_end),
		  ##diplomacy end+
        (call_script, "script_npc_morale", "$g_talk_troop"),
        (assign, ":troop_morale", reg0),
        
        (talk_info_set_relation_bar, ":troop_morale"),
        
        (str_store_troop_name, s61, "$g_talk_troop"),
        (assign, reg1, ":troop_morale"),
        (str_store_string, s62, "str_morale_reg1"),
        (str_store_string, s61, "@ {s61}({s62})"),
        
        (troop_get_slot, reg1, "$g_talk_troop", slot_troop_kill_count),
        (str_store_string, s11, "str_number_of_troops_killed_reg1"),
        (troop_get_slot, reg1, "$g_talk_troop", slot_troop_wound_count),
        (str_store_string, s12, "str_number_of_troops_wounded_reg1"),
        
        (talk_info_set_line, 0, s61),
        (talk_info_set_line, 1, s11),
        (talk_info_set_line, 2, s12),
        (talk_info_set_line, 3, s63),
    ]),
    #NPC companion changes end
    ## CC
    
    #script_update_party_creation_random_limits
    # INPUT: none
    ("update_party_creation_random_limits",
      [
        (store_character_level, ":player_level", "trp_player"),
        (store_mul, ":upper_limit", ":player_level", 3),
        (val_add, ":upper_limit", 25),
        (val_min, ":upper_limit", 100),
        (set_party_creation_random_limits, 0, ":upper_limit"),
        (assign, reg0, ":upper_limit"),
    ]),
    
    #script_set_trade_route_between_centers
    # INPUT:
    # param1: center_no_1
    # param1: center_no_2
    ("set_trade_route_between_centers",
      [(store_script_param, ":center_no_1", 1),
        (store_script_param, ":center_no_2", 2),
        (assign, ":center_1_added", 0),
        (assign, ":center_2_added", 0),
        (try_for_range, ":cur_slot", slot_town_trade_routes_begin, slot_town_trade_routes_end),
          (try_begin),
            (eq, ":center_1_added", 0),
            (party_slot_eq, ":center_no_1", ":cur_slot", 0),
            (party_set_slot, ":center_no_1", ":cur_slot", ":center_no_2"),
            (assign, ":center_1_added", 1),
          (try_end),
          (try_begin),
            (eq, ":center_2_added", 0),
            (party_slot_eq, ":center_no_2", ":cur_slot", 0),
            (party_set_slot, ":center_no_2", ":cur_slot", ":center_no_1"),
            (assign, ":center_2_added", 1),
          (try_end),
        (try_end),
        (try_begin),
          (eq, ":center_1_added", 0),
          (str_store_party_name, s1, ":center_no_1"),
          (display_message, "@{!}DEBUG -- ERROR: More than 15 trade routes are given for {s1}."),
        (try_end),
        (try_begin),
          (eq, ":center_2_added", 0),
          (str_store_party_name, s1, ":center_no_2"),
          (display_message, "@{!}DEBUG -- ERROR: More than 15 trade routes are given for {s1}."),
        (try_end),
    ]),
    
    #script_center_change_trade_good_production
    # INPUT:
    # param1: center_no
    # param2: item_id
    # param3: production_rate (should be between -100 (for net consumption) and 100 (for net production)
    # param4: randomness (between 0-100)
    #("center_change_trade_good_production",
     # [
      #  (store_script_param, ":center_no", 1),
       # (store_script_param, ":item_no", 2),
        #(store_script_param, ":production_rate", 3),
        #      (val_mul, ":production_rate", 5),
        #(store_script_param, ":randomness", 4),
        #(store_random_in_range, ":random_num", 0, ":randomness"),
        #(store_random_in_range, ":random_sign", 0, 2),
        #(try_begin),
        #  (eq, ":random_sign", 0),
        #  (val_add, ":production_rate", ":random_num"),
        #(else_try),
        #  (val_sub, ":production_rate", ":random_num"),
        #(try_end),
        #(val_sub, ":item_no", trade_goods_begin),
        #(val_add, ":item_no", slot_town_trade_good_productions_begin),
        
        #(party_get_slot, ":old_production_rate", ":center_no", ":item_no"),
        #(val_add, ":production_rate", ":old_production_rate"),
        #(party_set_slot, ":center_no", ":item_no", ":production_rate"),
    #]),
    
    ("average_trade_good_prices", #Called from start
      [
	#This should be done by route rather than distance
      (store_sub, ":item_to_slot", slot_town_trade_good_prices_begin, trade_goods_begin),

      (try_for_range, ":center_no", towns_begin, towns_end),
        (this_or_next|is_between, ":center_no", towns_begin, towns_end),
		(is_between, ":center_no", villages_begin, villages_end),

        (try_for_range, ":other_center", centers_begin, centers_end),
          (this_or_next|is_between, ":center_no", towns_begin, towns_end),
		  (is_between, ":center_no", villages_begin, villages_end),

          (neq, ":other_center", ":center_no"),
          (store_distance_to_party_from_party, ":cur_distance", ":center_no", ":other_center"),
          (lt, ":cur_distance", 50), #Reduced from 110
          (store_sub, ":dist_factor", 50, ":cur_distance"),

          (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
            (store_add, ":cur_good_slot", ":cur_good", ":item_to_slot"),
            (party_get_slot, ":center_price", ":center_no", ":cur_good_slot"),
            (party_get_slot, ":other_center_price", ":other_center", ":cur_good_slot"),
            (store_sub, ":price_dif", ":center_price", ":other_center_price"),

            (assign, ":price_dif_change", ":price_dif"),

            (val_mul ,":price_dif_change", ":dist_factor"),
            (val_div ,":price_dif_change", 1000), #Maximum of 1/20 per center
            (val_add, ":other_center_price", ":price_dif_change"),
            (party_set_slot, ":other_center", ":cur_good_slot", ":other_center_price"),

            (val_sub, ":center_price", ":price_dif_change"),
            (party_set_slot, ":center_no", ":cur_good_slot", ":center_price"),
          (try_end),
        (try_end),
      (try_end),
  ]),

  ("average_trade_good_prices_2", #Called from start
    [
	
	#This should be done by route rather than distance
      (store_sub, ":item_to_slot", slot_town_trade_good_prices_begin, trade_goods_begin),

      (try_for_range, ":center_no", towns_begin, towns_end),       		
        (try_for_range, ":other_center", centers_begin, centers_end),
          (this_or_next|is_between, ":other_center", towns_begin, towns_end),
			(is_between, ":other_center", villages_begin, villages_end),
            
            (this_or_next|party_slot_eq, ":other_center", slot_village_market_town, ":center_no"),
            (this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_1, ":other_center"),
            (this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_2, ":other_center"),
            (this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_3, ":other_center"),
            (this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_4, ":other_center"),
            (this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_5, ":other_center"),
            (this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_6, ":other_center"),
            (this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_7, ":other_center"),
            (this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_8, ":other_center"),
            (this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_9, ":other_center"),
            (this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_10, ":other_center"),
            (this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_11, ":other_center"),
            (this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_12, ":other_center"),
            (this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_13, ":other_center"),
            (this_or_next|party_slot_eq, ":center_no", slot_town_trade_route_14, ":other_center"),
            (party_slot_eq, ":center_no", slot_town_trade_route_15, ":other_center"),
            
            #          (neq, ":other_center", ":center_no"),
            #          (store_distance_to_party_from_party, ":cur_distance", ":center_no", ":other_center"),
            #          (lt, ":cur_distance", 50), #Reduced from 110
            #          (store_sub, ":dist_factor", 50, ":cur_distance"),
            
            (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
              (store_add, ":cur_good_slot", ":cur_good", ":item_to_slot"),
              (party_get_slot, ":center_price", ":center_no", ":cur_good_slot"),
              (party_get_slot, ":other_center_price", ":other_center", ":cur_good_slot"),
              (store_sub, ":price_dif", ":center_price", ":other_center_price"),
              
              (store_div, ":price_dif_change", ":price_dif", 5), #this is done twice, reduced from 4
              #            (assign, ":price_dif_change", ":price_dif"),
              
              #            (val_mul ,":price_dif_change", ":dist_factor"),
              #            (val_div ,":price_dif_change", 500), #Maximum of 1/10 per center
              (val_add, ":other_center_price", ":price_dif_change"),
              (party_set_slot, ":other_center", ":cur_good_slot", ":other_center_price"),
              
              (val_sub, ":center_price", ":price_dif_change"),
              (party_set_slot, ":center_no", ":cur_good_slot", ":center_price"),
              
            (try_end),
          (try_end),
        (try_end),
    ]),
    
    
    
    #script_average_trade_good_productions
    # INPUT: none (called only from game start?)
    #This is currently deprecated, as I was going to try to fine-tune production
    ("average_trade_good_productions",
      [
        (store_sub, ":item_to_slot", slot_town_trade_good_productions_begin, trade_goods_begin),
        #      (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
        (try_for_range, ":center_no", towns_begin, towns_end),
          (this_or_next|is_between, ":center_no", towns_begin, towns_end),
          (is_between, ":center_no", villages_begin, villages_end),
          (try_for_range, ":other_center", centers_begin, centers_end),
            (this_or_next|is_between, ":center_no", towns_begin, towns_end),
            (is_between, ":center_no", villages_begin, villages_end),
            (neq, ":other_center", ":center_no"),
            (store_distance_to_party_from_party, ":cur_distance", ":center_no", ":other_center"),
            (lt, ":cur_distance", 110),
            (store_sub, ":dist_factor", 110, ":cur_distance"),
            (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
              (store_add, ":cur_good_slot", ":cur_good", ":item_to_slot"),
              (party_get_slot, ":center_production", ":center_no", ":cur_good_slot"),
              (party_get_slot, ":other_center_production", ":other_center", ":cur_good_slot"),
              (store_sub, ":prod_dif", ":center_production", ":other_center_production"),
              (gt, ":prod_dif", 0),
              (store_mul, ":prod_dif_change", ":prod_dif", 1),
              ##            (try_begin),
              ##              (is_between, ":center_no", towns_begin, towns_end),
              ##              (is_between, ":other_center", towns_begin, towns_end),
              ##              (val_mul, ":cur_distance", 2),
              ##            (try_end),
              (val_mul ,":prod_dif_change", ":dist_factor"),
              (val_div ,":prod_dif_change", 110),
              (val_add, ":other_center_production", ":prod_dif_change"),
              (party_set_slot, ":other_center", ":cur_good_slot", ":other_center_production"),
            (try_end),
          (try_end),
        (try_end),
    ]),
    
    #script_normalize_trade_good_productions
    #Adjusts productions according to the amount of the item produced
    # INPUT: none
    # This currently deprecated, as I was going to try to fine-tune productions
    ("normalize_trade_good_productions",
      [
        (store_sub, ":item_to_slot", slot_town_trade_good_productions_begin, trade_goods_begin),
        (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
          (assign, ":total_production", 0),
          (assign, ":num_centers", 0),
          (store_add, ":cur_good_slot", ":cur_good", ":item_to_slot"),
          (try_for_range, ":center_no", centers_begin, centers_end),
            (val_add, ":num_centers", 1),
            (try_begin),
              (is_between, ":center_no", towns_begin, towns_end), #each town is weighted as 5 villages...
              (val_add, ":num_centers", 4),
            (try_end),
            (party_get_slot, ":center_production", ":center_no", ":cur_good_slot"),
            (val_add, ":total_production", ":center_production"),
          (try_end),
          (store_div, ":new_production_difference", ":total_production", ":num_centers"),
          (neq, ":new_production_difference", 0),
          (try_for_range, ":center_no", centers_begin, centers_end),
            (this_or_next|is_between, ":center_no", towns_begin, towns_end),
            (is_between, ":center_no", villages_begin, villages_end),
            (party_get_slot, ":center_production", ":center_no", ":cur_good_slot"),
            (val_sub, ":center_production", ":new_production_difference"),
            (party_set_slot, ":center_no", ":cur_good_slot", ":center_production"),
          (try_end),
        (try_end),
    ]),
    
    #script_update_trade_good_prices
    # INPUT: none
    ("update_trade_good_prices",
      [
        (try_for_range, ":center_no", centers_begin, centers_end),
          (this_or_next|is_between, ":center_no", towns_begin, towns_end),
          (is_between, ":center_no", villages_begin, villages_end),
          (call_script, "script_update_trade_good_price_for_party", ":center_no"),
        (try_end),
        #      (call_script, "script_update_trade_good_price_for_party", "p_zendar"),
        #      (call_script, "script_update_trade_good_price_for_party", "p_salt_mine"),
        #      (call_script, "script_update_trade_good_price_for_party", "p_four_ways_inn"),

      (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),							#	1.143 Port	// Newly added
	    (assign, ":total_price", 0),
		(assign, ":total_constants", 0),

	    (try_for_range, ":center_no", centers_begin, centers_end),
          (this_or_next|is_between, ":center_no", towns_begin, towns_end),
          (is_between, ":center_no", villages_begin, villages_end),

          (store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
          (val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
          (party_get_slot, ":cur_price", ":center_no", ":cur_good_price_slot"),

		  (try_begin),
		    (is_between, ":center_no", towns_begin, towns_end),
			(assign, ":constant", 5),
          (else_try),
		    (assign, ":constant", 1),
		  (try_end),

		  (val_mul, ":cur_price", ":constant"),

		  (val_add, ":total_price", ":cur_price"),
		  (val_add, ":total_constants", ":constant"),
		(try_end),

		(try_for_range, ":center_no", centers_begin, centers_end),
          (this_or_next|is_between, ":center_no", towns_begin, towns_end),
          (is_between, ":center_no", villages_begin, villages_end),

          (store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
          (val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
          (party_get_slot, ":cur_price", ":center_no", ":cur_good_price_slot"),

		  (val_mul, ":cur_price", 1000),
		  (val_mul, ":cur_price", ":total_constants"),
		  (val_div, ":cur_price", ":total_price"),		  

		  (val_clamp, ":cur_price", minimum_price_factor, maximum_price_factor),
		  (party_set_slot, ":center_no", ":cur_good_price_slot", ":cur_price"),
		(try_end),
      (try_end),																				#	End

	  ]),
    
    #script_update_trade_good_price_for_party
    # INPUT: arg1 = party_no
    #Called once every 72 hours
    ("update_trade_good_price_for_party",
      [
        (store_script_param, ":center_no", 1),
        (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
          (store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
          (val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
          (party_get_slot, ":cur_price", ":center_no", ":cur_good_price_slot"),
          
          (call_script, "script_center_get_production", ":center_no", ":cur_good"),
          (assign, ":production", reg0),
          
          (call_script, "script_center_get_consumption", ":center_no", ":cur_good"),
          (assign, ":consumption", reg0),
          (val_sub, ":production", ":consumption"),
          
		#Change averages production x 2(1+random(2)) (was 4, random(8)) for excess demand						#	1.143 Port // Compare to native 1.134 to see changes
        (try_begin),
		  #supply is greater than demand
          (gt, ":production", 0), 
		  (store_mul, ":change_factor", ":production", 1), #price will be decreased by his factor
		  (store_random_in_range, ":random_change", 0, ":change_factor"),
		  (val_add, ":random_change", ":change_factor"),
		  (val_add, ":random_change", ":change_factor"),		  

		  #simulation starts
          (store_sub, ":final_price", ":cur_price", ":random_change"),
		  (val_clamp, ":final_price", minimum_price_factor, maximum_price_factor),		  		  		  
		  (try_begin), #Excess of supply decelerates over time, as low price reduces output
		    #if expected final price is 100 then it will multiply random_change by 0.308x ((100+300)/(1300) = 400/1300).
			(lt, ":final_price", 1000),
			(store_add, ":final_price_plus_300", ":final_price", 300),
			(val_mul, ":random_change", ":final_price_plus_300"),
			(val_div, ":random_change", 1300),
          (try_end),
          (val_sub, ":cur_price", ":random_change"),
        (else_try),
          (lt, ":production", 0), 
		  (store_sub, ":change_factor", 0, ":production"), #price will be increased by his factor
		  (val_mul, ":change_factor", 1), 
		  (store_random_in_range, ":random_change", 0, ":change_factor"),
		  (val_add, ":random_change", ":change_factor"),
		  (val_add, ":random_change", ":change_factor"),
          (val_add, ":cur_price", ":random_change"),
        (try_end),
			
        #Move price towards average by 3%...
		#Equilibrium is 33 cycles, or 100 days
		#Change per cycle is Production x 4
		#Thus, max differential = -5 x 4 x 33 = -660 for -5
		(try_begin),
		  (is_between, ":center_no", villages_begin, villages_end),
          (store_sub, ":price_difference", ":cur_price", average_price_factor),
          (val_mul, ":price_difference", 96),
          (val_div, ":price_difference", 100),
          (store_add, ":new_price", average_price_factor, ":price_difference"),
        (else_try),
          (store_sub, ":price_difference", ":cur_price", average_price_factor),
          (val_mul, ":price_difference", 96),
          (val_div, ":price_difference", 100),
          (store_add, ":new_price", average_price_factor, ":price_difference"),
        (try_end),
		
		#Price of manufactured goods drift towards primary raw material 
		(try_begin),
			(item_get_slot, ":raw_material", ":cur_good", slot_item_primary_raw_material),
            (neq, ":raw_material", 0),
	        (store_sub, ":raw_material_price_slot", ":raw_material", trade_goods_begin),
	        (val_add, ":raw_material_price_slot", slot_town_trade_good_prices_begin),

			(party_get_slot, ":total_raw_material_price", ":center_no", ":raw_material_price_slot"),
			(val_mul, ":total_raw_material_price", 3),
            (assign, ":number_of_centers", 3),

			(try_for_range, ":village_no", villages_begin, villages_end),
			  (party_slot_eq, ":village_no", slot_village_bound_center, ":center_no"),
			  (party_get_slot, ":raw_material_price", ":village_no", ":raw_material_price_slot"),
			  (val_add, ":total_raw_material_price", ":raw_material_price"),
			  (val_add, ":number_of_centers", 1),
            (try_end),

			(store_div, ":average_raw_material_price", ":total_raw_material_price", ":number_of_centers"),					

			(gt, ":average_raw_material_price", ":new_price"),
			(store_sub, ":raw_material_boost", ":average_raw_material_price", ":new_price"),
			(val_div, ":raw_material_boost", 10), 
			(val_add, ":new_price", ":raw_material_boost"),
		(try_end),
		
        (val_clamp, ":new_price", minimum_price_factor, maximum_price_factor),
        (party_set_slot, ":center_no", ":cur_good_price_slot", ":new_price"),

		#(assign, reg3, ":new_price"),
		#(str_store_item_name, s2, ":cur_good"),
		#(display_log_message, "@DEBUG : {s1}-{s2}, prod:{reg1}, cons:{reg2}, price:{reg3}"),
      (try_end),																								#	End
    ]),
    
    ("center_get_production",
      [
        #Actually, this could be reset somewhat to yield supply and demand as raw numbers
        #Demand could be set values for rural and urban
        #Supply could be based on capital goods -- head of cattle, head of sheep, fish ponds, fishing fleets, acres of grain fields, olive orchards, olive presses, wine presses, mills, smithies, salt pans, potters' kilns, etc
        #Prosperity would increase both demand and supply
        (store_script_param_1, ":center_no"),
        (store_script_param_2, ":cur_good"),
        
        (assign, ":base_production", 0),
        
        #Grain products
        (try_begin),
          (eq, ":cur_good", "itm_trade_bread"), #Demand = 3000 across Calradia
          (party_get_slot, ":base_production", ":center_no", slot_center_mills),
          (val_mul, ":base_production", 20), #one mills per village, five mills per town = 160 mills
        (else_try),
          (eq, ":cur_good", "itm_trade_grain"), #Demand =  3200+, 1600 to mills, 1500 on its own, extra to breweries
          (party_get_slot, ":base_production", ":center_no", slot_center_acres_grain),
          (val_div, ":base_production", 125), #10000 acres is the average across Calradia, extra in Swadia, less in snows and steppes, a bit from towns
        (else_try),
          (eq, ":cur_good", "itm_trade_ale"), #
          (party_get_slot, ":base_production", ":center_no", slot_center_breweries),
          (val_mul, ":base_production", 25),														#	1.143	//	Decreased from 35
          
        (else_try),
          (eq, ":cur_good", "itm_trade_smoked_fish"), #Demand = 20
          (party_get_slot, ":base_production", ":center_no", slot_center_fishing_fleet),
          (val_mul, ":base_production", 4), #was originally 5
        (else_try),
          (eq, ":cur_good", "itm_trade_salt"),
          (party_get_slot, ":base_production", ":center_no", slot_center_salt_pans),
          (val_mul, ":base_production", 35),
          
          #Cattle products
        (else_try),
          (eq, ":cur_good", "itm_trade_cattle_meat"), #Demand = 5
          (party_get_slot, ":base_production", ":center_no", slot_center_head_cattle),
          (val_div, ":base_production", 4), 														#	1.143 Port // Decreased from 9
        (else_try),
          (eq, ":cur_good", "itm_trade_dried_meat"), #Demand = 15
          (party_get_slot, ":base_production", ":center_no", slot_center_head_cattle),
          (val_div, ":base_production", 2), 														#	1.143 Port // Decreased from 3
        (else_try),
          (eq, ":cur_good", "itm_trade_cheese"), 	 #Demand = 10
          (party_get_slot, ":base_production", ":center_no", slot_center_head_cattle),
          (party_get_slot, ":sheep_addition", ":center_no", slot_center_head_sheep),
		  (val_div, ":sheep_addition", 2),
		  (val_add, ":base_production", ":sheep_addition"),
		  (party_get_slot, ":gardens", ":center_no", slot_center_household_gardens),
		  (val_mul, ":base_production", ":gardens"),
		  (val_div, ":base_production", 10), 		 														#	1.143 Port // Decreased from 4
        (else_try),
          (eq, ":cur_good", "itm_trade_butter"), 	 #Demand = 2
          (party_get_slot, ":base_production", ":center_no", slot_center_head_cattle),
          (party_get_slot, ":gardens", ":center_no", slot_center_household_gardens),
		  (val_mul, ":base_production", ":gardens"),
		  (val_div, ":base_production", 15),																	#	1.143 Port // Decreased from 20
          
        (else_try),
          (eq, ":cur_good", "itm_trade_raw_leather"), 	 #Demand = ??
          (party_get_slot, ":base_production", ":center_no", slot_center_head_cattle),
          (val_div, ":base_production", 6),
          (party_get_slot, ":sheep_addition", ":center_no", slot_center_head_sheep),
          (val_div, ":sheep_addition", 12),
          (val_add, ":base_production", ":sheep_addition"),
          
        (else_try),
          (eq, ":cur_good", "itm_trade_leatherwork"), 	 #Demand = ??
          (party_get_slot, ":base_production", ":center_no", slot_center_tanneries),
          (val_mul, ":base_production", 20),
          
          
        (else_try),
          (eq, ":cur_good", "itm_trade_honey"), 	 #Demand = 5
          (party_get_slot, ":base_production", ":center_no", slot_center_apiaries),
          (val_mul, ":base_production", 6),
        (else_try),
			(eq, ":cur_good", "itm_trade_cabbages"), 	 #Demand = 7
			(party_get_slot, ":base_production", ":center_no", slot_center_household_gardens),
			(val_mul, ":base_production", 10),														#	1.143 Port // Increased from 8
		(else_try),
			(eq, ":cur_good", "itm_trade_apples"), 	 #Demand = 7
			(party_get_slot, ":base_production", ":center_no", slot_center_household_gardens),
			(val_mul, ":base_production", 10),														#	1.143 Port // Increased from 5
          
          #Sheep products
        (else_try),
          (eq, ":cur_good", "itm_trade_sausages"), 	 #Demand = 5
          (party_get_slot, ":base_production", ":center_no", slot_center_head_sheep), #average of 90 sheep
          (val_div, ":base_production", 15),
        (else_try),
          (eq, ":cur_good", "itm_trade_wool"), 	 #(Demand = 0, but 15 averaged out perhaps)
          (party_get_slot, ":base_production", ":center_no", slot_center_head_sheep), #average of 90 sheep
          (val_div, ":base_production", 5),
        (else_try),
          (eq, ":cur_good", "itm_trade_wool_cloth"), 	 #(Demand = 1500 across Calradia)
          (party_get_slot, ":base_production", ":center_no", slot_center_wool_looms),
          (val_mul, ":base_production", 5), #300 across Calradia
          
        (else_try),
			(this_or_next|eq, ":cur_good", "itm_trade_pork"), 	 										#	1.143 Port // Newly Added
			(eq, ":cur_good", "itm_trade_chicken"), 	 
			(try_begin),
			  (is_between, ":center_no", villages_begin, villages_end),
			  (assign, ":base_production", 30), 
			(else_try),
			  (assign, ":base_production", 0), 
			(try_end),																				#	End
		(else_try),
          (eq, ":cur_good", "itm_trade_iron"), 	 #Demand = 5, one supplies three smithies
          (party_get_slot, ":base_production", ":center_no", slot_center_iron_deposits),
          (val_mul, ":base_production", 10),
        (else_try),
          (eq, ":cur_good", "itm_trade_tools"), 	 #Demand = 560 across Calradia
          (party_get_slot, ":base_production", ":center_no", slot_center_smithies),
          (val_mul, ":base_production", 3),
          
          #Other artisanal goods
        (else_try),
          (eq, ":cur_good", "itm_trade_pottery"), #560 is total demand
          (party_get_slot, ":base_production", ":center_no", slot_center_pottery_kilns),
          (val_mul, ":base_production", 5),															#	1.143 Port // Increased from 2
          
        (else_try),
          (eq, ":cur_good", "itm_trade_raw_grapes"),
          (party_get_slot, ":base_production", ":center_no", slot_center_acres_vineyard),
          (val_div, ":base_production", 100),
        (else_try),
          (eq, ":cur_good", "itm_trade_wine"),
          (party_get_slot, ":base_production", ":center_no", slot_center_wine_presses),
          (val_mul, ":base_production", 25),														#	1.143 Port // Decreased from 30
        (else_try),
          (eq, ":cur_good", "itm_trade_raw_olives"),
          (party_get_slot, ":base_production", ":center_no", slot_center_acres_olives),
          (val_div, ":base_production", 150),
        (else_try),
          (eq, ":cur_good", "itm_trade_oil"),
          (party_get_slot, ":base_production", ":center_no", slot_center_olive_presses),
          (val_mul, ":base_production", 12),
          
          #Flax and linen
        (else_try),
          (eq, ":cur_good", "itm_trade_linen"),
          (party_get_slot, ":base_production", ":center_no", slot_center_linen_looms),
          (val_mul, ":base_production", 5),
        (else_try),
          (eq, ":cur_good", "itm_trade_raw_flax"),
          (party_get_slot, ":base_production", ":center_no", slot_center_acres_flax),
          (val_div, ":base_production", 80),														#	1.143 Port // Increased from 65
          
          
        (else_try),
          (eq, ":cur_good", "itm_trade_velvet"),
          (party_get_slot, ":base_production", ":center_no", slot_center_silk_looms),
          (val_mul, ":base_production", 5),
        (else_try),
          (eq, ":cur_good", "itm_trade_raw_silk"),
          (party_get_slot, ":base_production", ":center_no", slot_center_silk_farms),
          (val_div, ":base_production", 20),
        (else_try),
          (eq, ":cur_good", "itm_trade_raw_dyes"),
			(party_get_slot, ":base_production", ":center_no", slot_center_kirmiz_farms),			#	1.143 Port // Decreased from 50 , Check slot instead of town id (5,22)
			(val_div, ":base_production", 20),
        (else_try),
          (eq, ":cur_good", "itm_trade_raw_date_fruit"),
          (party_get_slot, ":base_production", ":center_no", slot_center_acres_dates),
          (val_div, ":base_production", 120),
        (else_try),
          (eq, ":cur_good", "itm_trade_furs"), 	 #Demand = 90 across Calradia
          (party_get_slot, ":base_production", ":center_no", slot_center_fur_traps),
          (val_mul, ":base_production", 25),															#	1.143 Port // Increased from 3
        (else_try),
          (eq, ":cur_good", "itm_trade_spice"),
          (try_begin),
            (eq, ":center_no", "p_town_10"), #Tulga
            (assign, ":base_production", 100),
          (else_try),
            (eq, ":center_no", "p_town_17"), #Ichamur
			(assign, ":base_production", 50),															#	1.143 Port // Increased from 40
		(else_try),
			(eq, ":center_no", "p_town_19"), #Shariz
			(assign, ":base_production", 50),															#	1.143 Port // Increased from 30
          (else_try),
            (eq, ":center_no", "p_town_22"), #Bariyye
            (assign, ":base_production", 50),															#	1.143 Port // Increased from 30
          (else_try),
			(this_or_next|eq, ":center_no", "p_village_11"), #Dusturil (village of Tulga)
			(eq, ":center_no", "p_village_25"), #Dashbigha (village of Tulga)
			(assign, ":base_production", 50),
		  (else_try),
			(this_or_next|eq, ":center_no", "p_village_37"), #Ada Kulun (village of Ichlamur)
			(this_or_next|eq, ":center_no", "p_village_42"), #Dirigh Aban (village of Ichlamur)
			(this_or_next|eq, ":center_no", "p_village_99"), #Fishara (village of Bariyye)
			(eq, ":center_no", "p_village_100"), #Iqbayl (village of Bariyye)
			(assign, ":base_production", 25),		
		  (try_end),
        (try_end),
        
        #Modify production by other goods
		
        (assign, ":modified_production", ":base_production"),
        (try_begin),
          (eq, ":cur_good", "itm_trade_bread"),
          (call_script, "script_good_price_affects_good_production", ":center_no", "itm_trade_grain", ":base_production", 1),
          (assign, ":modified_production", reg0),
        (else_try),
          (eq, ":cur_good", "itm_trade_ale"),
          (call_script, "script_good_price_affects_good_production", ":center_no", "itm_trade_grain", ":base_production", 2),
          (assign, ":modified_production", reg0),
        (else_try),
          (eq, ":cur_good", "itm_trade_dried_meat"),
          (call_script, "script_good_price_affects_good_production", ":center_no", "itm_trade_salt", ":base_production", 2),
          (assign, ":modified_production", reg0),
        (else_try),
          (eq, ":cur_good", "itm_trade_smoked_fish"),
          (call_script, "script_good_price_affects_good_production", ":center_no", "itm_trade_salt", ":base_production", 2),
          (assign, ":modified_production", reg0),
        (else_try),
          (eq, ":cur_good", "itm_trade_tools"),
          (call_script, "script_good_price_affects_good_production", ":center_no", "itm_trade_iron", ":base_production", 1),
          (assign, ":modified_production", reg0),
        (else_try),
          (eq, ":cur_good", "itm_trade_wool_cloth"),
          (call_script, "script_good_price_affects_good_production", ":center_no", "itm_trade_wool", ":base_production", 1),
          (assign, ":modified_production", reg0),
        (else_try),
          (eq, ":cur_good", "itm_trade_wine"),
          (call_script, "script_good_price_affects_good_production", ":center_no", "itm_trade_raw_grapes", ":base_production", 1),
          (assign, ":modified_production", reg0),
        (else_try),
          (eq, ":cur_good", "itm_trade_oil"),
          (call_script, "script_good_price_affects_good_production", ":center_no", "itm_trade_raw_olives", ":base_production", 1),
          (assign, ":modified_production", reg0),
        (else_try),
          (eq, ":cur_good", "itm_trade_velvet"),
          (call_script, "script_good_price_affects_good_production", ":center_no", "itm_trade_raw_silk", ":base_production", 1),
          (assign, ":initially_modified_production", reg0),
          
          (call_script, "script_good_price_affects_good_production", ":center_no", "itm_trade_raw_dyes", ":initially_modified_production", 2),
          (assign, ":modified_production", reg0),
        (else_try),
          (eq, ":cur_good", "itm_trade_leatherwork"),
          (call_script, "script_good_price_affects_good_production", ":center_no", "itm_trade_raw_leather", ":base_production", 1),
          (assign, ":modified_production", reg0),
        (else_try),
          (eq, ":cur_good", "itm_trade_linen"),
          (call_script, "script_good_price_affects_good_production", ":center_no", "itm_trade_raw_flax", ":base_production", 1),
          (assign, ":modified_production", reg0),
        (try_end),
        
        
        (assign, ":base_production_modded_by_raw_materials", ":modified_production"), #this is just logged for the report screen
        
        #Increase both positive and negative production by the center's prosperity
        #Richer towns have more people and consume more, but also produce more
        (try_begin),
          (party_get_slot, ":prosperity_plus_75", ":center_no", slot_town_prosperity),
          (val_add, ":prosperity_plus_75", 75),
          (val_mul, ":modified_production", ":prosperity_plus_75"),
          (val_div, ":modified_production", 125),
        (try_end),
        
        (try_begin),
          (this_or_next|party_slot_eq, ":center_no", slot_village_state, svs_being_raided),
          (party_slot_eq, ":center_no", slot_village_state, svs_looted),
          (assign, ":modified_production", 0),
        (try_end),
        
        (assign, reg0, ":modified_production"), #modded by prosperity
        (assign, reg1, ":base_production_modded_by_raw_materials"),
        (assign, reg2, ":base_production"),
        
    ]),
    
    ("center_get_consumption",
      [
        (store_script_param_1, ":center_no"),
        (store_script_param_2, ":cur_good"),
        
        (assign, ":consumer_consumption", 0),
        (try_begin),
          (this_or_next|is_between, ":center_no", "p_town_19", "p_castle_1"),
          (ge, ":center_no", "p_village_91"),
          (item_slot_ge, ":cur_good", slot_item_desert_demand, 0), #Otherwise use rural or urban
          (item_get_slot, ":consumer_consumption", ":cur_good", slot_item_desert_demand),
        (else_try),
          (is_between, ":center_no", villages_begin, villages_end),
          (item_get_slot, ":consumer_consumption", ":cur_good", slot_item_rural_demand),
        (else_try),
          (is_between, ":center_no", towns_begin, towns_end),
          (item_get_slot, ":consumer_consumption", ":cur_good", slot_item_urban_demand),
        (try_end),
        
        
        (assign, ":raw_material_consumption", 0),
        (try_begin),
          (eq, ":cur_good", "itm_trade_grain"),
          (party_get_slot, ":grain_for_bread", ":center_no", slot_center_mills),
          (val_mul, ":grain_for_bread", 20),
          
          (party_get_slot, ":grain_for_ale", ":center_no", slot_center_breweries),
          (val_mul, ":grain_for_ale", 5),
          
          (store_add, ":raw_material_consumption", ":grain_for_bread", ":grain_for_ale"),
          
        (else_try),
          (eq, ":cur_good", "itm_trade_iron"),
          (party_get_slot, ":raw_material_consumption", ":center_no", slot_center_smithies),
          (val_mul, ":raw_material_consumption", 3),
          
        (else_try),
          (eq, ":cur_good", "itm_trade_wool"),
          (party_get_slot, ":raw_material_consumption", ":center_no", slot_center_wool_looms),
          (val_mul, ":raw_material_consumption", 5),
          
        (else_try),
          (eq, ":cur_good", "itm_trade_raw_flax"),
          (party_get_slot, ":raw_material_consumption", ":center_no", slot_center_linen_looms),
          (val_mul, ":raw_material_consumption", 5),
          
        (else_try),
          (eq, ":cur_good", "itm_trade_raw_leather"),
          (party_get_slot, ":raw_material_consumption", ":center_no", slot_center_tanneries),
          (val_mul, ":raw_material_consumption", 20),
          
        (else_try),
          (eq, ":cur_good", "itm_trade_raw_grapes"),
          (party_get_slot, ":raw_material_consumption", ":center_no", slot_center_wine_presses),
          (val_mul, ":raw_material_consumption", 30),
          
        (else_try),
          (eq, ":cur_good", "itm_trade_raw_olives"),
          (party_get_slot, ":raw_material_consumption", ":center_no", slot_center_olive_presses),
          (val_mul, ":raw_material_consumption", 12),
          
          
        (else_try),
          (eq, ":cur_good", "itm_trade_raw_dyes"),
          (party_get_slot, ":raw_material_consumption", ":center_no", slot_center_silk_looms),
          (val_mul, ":raw_material_consumption", 1),
        (else_try),
          (eq, ":cur_good", "itm_trade_raw_silk"),
          (party_get_slot, ":raw_material_consumption", ":center_no", slot_center_silk_looms),
          (val_mul, ":raw_material_consumption", 5),
          
          
        (else_try),
          (eq, ":cur_good", "itm_trade_salt"),
          (party_get_slot, ":salt_for_beef", ":center_no", slot_center_head_cattle),
          (val_div, ":salt_for_beef", 10),
          
          (party_get_slot, ":salt_for_fish", ":center_no", slot_center_fishing_fleet),
          (val_div, ":salt_for_fish", 5),
          
          (store_add, ":raw_material_consumption", ":salt_for_beef", ":salt_for_fish"),
        (try_end),
        
		(try_begin), #Reduce consumption of raw materials if their cost is high
			(gt, ":raw_material_consumption", 0),
			(store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
	        (store_add, ":cur_good_price_slot", ":cur_good", ":item_to_price_slot"),
	        (party_get_slot, ":cur_center_price", ":center_no", ":cur_good_price_slot"),
			##diplomacy start+
			(gt, ":cur_center_price", average_price_factor),#replace the hardcoded constant 1000 with average_price_factor
			(val_mul, ":raw_material_consumption", average_price_factor),#again replace the hardcoded constant 1000 with average_price_factor
			##diplomacy end+
			(val_div, ":raw_material_consumption", ":cur_center_price"),
		(try_end),
        
        
        
        (store_add, ":modified_consumption", ":consumer_consumption", ":raw_material_consumption"),
        (try_begin),
          (party_get_slot, ":prosperity_plus_75", ":center_no", slot_town_prosperity),
          (val_add, ":prosperity_plus_75", 75),
          (val_mul, ":modified_consumption", ":prosperity_plus_75"),
          (val_div, ":modified_consumption", 125),
        (try_end),
        
        
        (assign, reg0, ":modified_consumption"), #modded by prosperity
        (assign, reg1, ":raw_material_consumption"),
        (assign, reg2, ":consumer_consumption"),
    ]),
    
    #script_get_enterprise_name
    # INPUT: arg1 = item_no
    # Output: reg0: production string
    ("get_enterprise_name",
      [
        (store_script_param_1, ":item_produced"),
        (assign, ":enterprise_name", "str_bread_site"),
        (try_begin),
          (eq, ":item_produced", "itm_trade_bread"),
          (assign, ":enterprise_name", "str_bread_site"),
        (else_try),
          (eq, ":item_produced", "itm_trade_ale"),
          (assign, ":enterprise_name", "str_ale_site"),
        (else_try),
          (eq, ":item_produced", "itm_trade_oil"),
          (assign, ":enterprise_name", "str_oil_site"),
        (else_try),
          (eq, ":item_produced", "itm_trade_wine"),
          (assign, ":enterprise_name", "str_wine_site"),
        (else_try),
          (eq, ":item_produced", "itm_trade_leatherwork"),
          (assign, ":enterprise_name", "str_leather_site"),
        (else_try),
          (eq, ":item_produced", "itm_trade_wool_cloth"),
          (assign, ":enterprise_name", "str_wool_cloth_site"),
        (else_try),
          (eq, ":item_produced", "itm_trade_linen"),
          (assign, ":enterprise_name", "str_linen_site"),
        (else_try),
          (eq, ":item_produced", "itm_trade_velvet"),
          (assign, ":enterprise_name", "str_velvet_site"),
        (else_try),
          (eq, ":item_produced", "itm_trade_tools"),
          (assign, ":enterprise_name", "str_tool_site"),
        (try_end),
        (assign, reg0, ":enterprise_name"),
    ]),
    
    #script_do_merchant_town_trade
	  ##diplomacy start+
	  # If optional economic changes are enabled, the benefits are applied to both
	  # the town of origin and the destination, instead of just the latter.
	  ##diplomacy end+
	  ("do_merchant_town_trade",
		[
		  (store_script_param_1, ":party_no"),
		  (store_script_param_2, ":center_no"),
        
        (party_get_slot, ":origin", ":party_no", slot_party_last_traded_center),
        
        (try_begin),
          (eq, "$cheat_mode", 2),
          (str_store_party_name, s4, ":center_no"),
          (str_store_party_name, s5, ":origin"),
          (display_message, "@{!}DEBUG -- Caravan trades in {s4}, originally from {s5}"),
        (try_end),
        
        (call_script, "script_add_log_entry", logent_party_traded, ":party_no", ":origin", ":center_no", -1),
        
      (call_script, "script_do_party_center_trade", ":party_no", ":center_no", 4), #it was first 10 then increased 20 then increased 30, now I decrease it to back 6. Because otherwise prices do not differiate much. Trade becomes useless in game.
																					#		1.143 Port // see above, price_adjustment was used previously, no number
        (assign, ":total_change", reg0),
        #Adding the earnings to the wealth (maximum changed price is the earning)
        (val_div, ":total_change", 2),
        (str_store_party_name, s1, ":party_no"),
        (str_store_party_name, s2, ":center_no"),
        (assign, reg1, ":total_change"),
        
        #Adding tariffs to the town
        (party_get_slot, ":accumulated_tariffs", ":center_no", slot_center_accumulated_tariffs),
        (party_get_slot, ":prosperity", ":center_no", slot_town_prosperity),
        
	  (assign, ":tariffs_generated", ":total_change"),
      (val_mul, ":tariffs_generated", ":prosperity"),
	  ##diplomacy start+
	  #Move the next two lines further down to reduce rounding error
	  #(val_div, ":tariffs_generated", 100),
	  #(val_div, ":tariffs_generated", 10), #10 for caravans, 20 for villages
	  
	  #Re-wrote the "diplomacy" section here for greater clarity.
	  (assign, ":percent", 100),
      (try_begin), # trade agreement
        (store_faction_of_party, ":party_faction", ":party_no"),
        (store_faction_of_party, ":center_faction", ":center_no"),

        (store_add, ":truce_slot", ":party_faction", slot_faction_truce_days_with_factions_begin),
        (val_sub, ":truce_slot", kingdoms_begin),
  	    (faction_get_slot, ":truce_days", ":center_faction", ":truce_slot"),
  	    ##nested diplomacy start+ replace "20" with a named constant
  	    #(gt, ":truce_days", 20),
  	    (gt, ":truce_days", dplmc_treaty_trade_days_expire),
  	    ##nested diplomacy end+
  	    (val_add, ":percent", 30),
      (try_end),
	  
	  #If economic changes are enabled, divide the tariffs between the source and destination.
	  (assign, ":origin_tariffs_generated", 0),#we will need this variable later, if it is set
	  (try_begin),
	    #Economic changes must be enabled
		(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
		#verify the origin is a real town or village and not a placeholder value
		(ge, ":origin", 0),
		(this_or_next|is_between, ":origin", towns_begin, towns_end),
		(this_or_next|is_between, ":origin", villages_begin, villages_end),
		(this_or_next|party_slot_eq, ":origin", slot_party_type, spt_town),
			(party_slot_eq, ":origin", slot_party_type, spt_village),
		#give half the tariffs to the origin
		(ge, ":tariffs_generated", 0),
		(party_get_slot, ":origin_accumulated_tariffs", ":origin", slot_center_accumulated_tariffs),
		(store_div, ":origin_tariffs_generated", ":tariffs_generated", 2),
		(val_sub, ":tariffs_generated", ":origin_tariffs_generated"),
		#apply plutocracy/aristocracy modifier, and any modifier from a trade treaty
		(store_faction_of_party, ":origin_faction", ":center_no"),
		(faction_get_slot, ":aristocracy", ":origin_faction", dplmc_slot_faction_aristocracy),
        (val_mul, ":aristocracy", -5),
        (store_add, ":origin_percent", ":percent", ":aristocracy"),
		(val_mul, ":origin_tariffs_generated", ":origin_percent"),
		(val_add, ":origin_tariffs_generated", 50),#for rounding
		(val_div, ":origin_tariffs_generated", 100),
		#apply the delayed division from before (leaving the steps separated for clarity)
		(val_add, ":origin_tariffs_generated", 50),
		(val_div, ":origin_tariffs_generated", 100),#adjust for having been multiplied by prosperity
		(val_add, ":tariffs_generated", 5),
		(val_div, ":tariffs_generated", 10), #10 for caravans, 20 for villages
		#now we have the final value of origin_tariffs_generated 
		(val_add, ":origin_accumulated_tariffs", ":origin_tariffs_generated"),
		(party_set_slot, ":origin", slot_center_accumulated_tariffs, ":origin_accumulated_tariffs"),
		#print economic debug message if enabled
		(ge, "$cheat_mode", 3),
		(assign, reg4, ":origin_tariffs_generated"),
		(str_store_party_name, s4, ":origin"),
		(assign, reg5, ":origin_accumulated_tariffs"),
		(display_message, "@{!}New tariffs at {s4} = {reg4}, total = {reg5}"),
	  (try_end),
	 
	  #For this town: apply the faction plutocracy/aristocracy modifier
      (faction_get_slot, ":aristocracy", ":center_faction", dplmc_slot_faction_aristocracy),
      (val_mul, ":aristocracy", -5),
      (val_add, ":percent", ":aristocracy"),
      (val_mul, ":tariffs_generated", ":percent"),
   	  (val_add, ":tariffs_generated", 50),
      (val_div, ":tariffs_generated", 100),
	  #apply the delayed division from before (leaving the steps separated for clarity)
   	  (val_add, ":tariffs_generated", 50),
 	  (val_div, ":tariffs_generated", 100),#adjust for having been multiplied by prosperity
	  (val_add, ":tariffs_generated", 5),
	  (val_div, ":tariffs_generated", 10), #10 for caravans, 20 for villages
	  ##diplomacy end+
	  (val_add, ":accumulated_tariffs", ":tariffs_generated"),

	  (try_begin),
		(ge, "$cheat_mode", 3),
		(assign, reg4, ":tariffs_generated"),
		(str_store_party_name, s4, ":center_no"),
		(assign, reg5, ":accumulated_tariffs"),
		(display_message, "@{!}New tariffs at {s4} = {reg4}, total = {reg5}"),
	  (try_end),

      (party_set_slot, ":center_no", slot_center_accumulated_tariffs, ":accumulated_tariffs"),
      ##diplomacy start+
	  #If economic changes are enabled, 50% chance that the origin rather than
	  #the destination will receive the chance for prosperity increase.
	  (assign, ":benefit_center", ":center_no"),
	  (try_begin),
		#Economic changes must be enabled
		(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
		#verify the origin is a real town or village and not a placeholder value
		(ge, ":origin", 0),
		(this_or_next|is_between, ":origin", towns_begin, towns_end),
		(this_or_next|is_between, ":origin", villages_begin, villages_end),
		(this_or_next|party_slot_eq, ":origin", slot_party_type, spt_town),
			(party_slot_eq, ":origin", slot_party_type, spt_village),
		(ge, ":tariffs_generated", 0),
		#50% chance
		(store_random_in_range, ":rand", 0, 64),
		(lt, ":rand", 32),
		(assign, ":benefit_center", ":origin"),
	  (try_end),
	  ##diplomacy end+
      #Adding 1 to center prosperity in many circumstances
      (try_begin),
        (store_random_in_range, ":rand", 0, 80),
		##diplomacy start+ in next line, changed center_no to benefit_center
        (call_script, "script_center_get_goods_availability", ":benefit_center"),
		##diplomacy end+
		(assign, ":hardship_index", reg0),
		(gt, ":rand", ":hardship_index"),
		(try_begin),
          (store_random_in_range, ":rand", 0, 100),
          (gt, ":rand", 82),
	    ##diplomacy start+ in next line, changed center_no to benefit_center
        (call_script, "script_change_center_prosperity", ":benefit_center", 1),
		##diplomacy end+
		(val_add, "$newglob_total_prosperity_from_caravan_trade", 1),
		(try_end),
      (try_end),
	  # Warband v1.153  comment out--to end
      # ##Repeat, but harder
      # (try_begin),
        # (store_random_in_range, ":rand", -20, 40),
		# ##diplomacy start+ in next line, changed center_no to benefit_center
        # (call_script, "script_center_get_goods_availability", ":benefit_center"),
		# ##diplomacy end+
		# (assign, ":hardship_index", reg0),
		# (gt, ":rand", ":hardship_index"),
        # ##diplomacy start+ in next line, changed center_no to benefit_center
        # (call_script, "script_change_center_prosperity", ":benefit_center", 1),
		# ##diplomacy end+
		# (val_add, "$newglob_total_prosperity_from_caravan_trade", 1),
      # (try_end),

	]),
    
    #script_party_calculate_regular_strength:
    # INPUT:
    # param1: Party-id
    ("party_calculate_regular_strength",
      [
        (store_script_param_1, ":party"), #Party_id
        
        (assign, reg0,0),
        (party_get_num_companion_stacks, ":num_stacks",":party"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", ":party", ":i_stack"),
          (neg|troop_is_hero, ":stack_troop"),
          (store_character_level, ":stack_strength", ":stack_troop"),
#TEMPERED#   ADD BONUS FOR MOUNTED TROOPS
			(try_begin),
				(troop_is_mounted, ":stack_troop"),
				(val_add, ":stack_strength", 5),
			(try_end),
#TEMPERED#    ADD BONUS FOR HIGH LEVEL TROOPS
			(store_div,":strength_bonus",":stack_strength",4),
			(val_add, ":stack_strength",":strength_bonus"),
#TEMPERED#    BONUSES END 
          (val_add, ":stack_strength", 12),
          (val_mul, ":stack_strength", ":stack_strength"),
          (val_div, ":stack_strength", 100),
          (party_stack_get_size, ":stack_size",":party",":i_stack"),
          (party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
          (val_sub, ":stack_size", ":num_wounded"),
          (val_mul, ":stack_strength", ":stack_size"),
          (val_add,reg0, ":stack_strength"),
        (try_end),
    ]),
    
    
    
    
    #script_party_calculate_strength:
    # INPUT: arg1 = party_id, arg2 = exclude leader
    # OUTPUT: reg0 = strength
    
    ("party_calculate_strength",
      [
        (store_script_param_1, ":party"), #Party_id
        (store_script_param_2, ":exclude_leader"), #Party_id
        
        (assign, reg0,0),
        (party_get_num_companion_stacks, ":num_stacks", ":party"),
        (assign, ":first_stack", 0),
#TEMPERED ADDED FOR ENTRENCHMENT BONUS
	  (assign,":entrench",0),
	  (try_begin),
		(eq,":party","p_main_party"),
        (party_get_slot,":entrench","p_main_party",slot_party_entrenched),
	  (try_end),
#TEMPERED CHANGES END	  
        (try_begin),
          (neq, ":exclude_leader", 0),
          (assign, ":first_stack", 1),
        (try_end),
        (try_for_range, ":i_stack", ":first_stack", ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop",":party", ":i_stack"),
          (store_character_level, ":stack_strength", ":stack_troop"),
#TEMPERED#  ADDED BONUS FOR HEROES, BONUSES ARE FOR MORE REALISTIC AUTOCALC BATTLE RESULTS
			(try_begin),
				(troop_is_hero, ":stack_troop"),
				(val_add, ":stack_strength", 2),
			(try_end),			
#TEMPERED#   ADD BONUS FOR MOUNTED TROOPS
			(try_begin),
				(troop_is_mounted, ":stack_troop"),
				(val_add, ":stack_strength", 5),
			(try_end),
#TEMPERED#    ADD BONUS FOR HIGH LEVEL TROOPS
			(store_div,":strength_bonus",":stack_strength",4),
			(val_add, ":stack_strength",":strength_bonus"),
#TEMPERED    ADDED BONUS FOR ENTRENCHMENT
			(try_begin),
				(eq,":entrench",1),
				(val_add,":stack_strength",2),
			(try_end),
#TEMPERED#    BONUSES END 	
          (val_add, ":stack_strength", 4), #new was 12 (patch 1.125)
          (val_mul, ":stack_strength", ":stack_strength"),
          (val_mul, ":stack_strength", 2), #new (patch 1.125)
          (val_div, ":stack_strength", 100),
          (val_max, ":stack_strength", 1), #new (patch 1.125)
          ##AotE terrain advantages
          (party_get_current_terrain, ":terrain_type", ":party"),
          (try_begin),
            (eq, ":terrain_type", rt_steppe),
            (troop_is_guarantee_horse, ":stack_troop"),
            (val_mul, ":stack_strength", 150),
          (else_try),
            (eq, ":terrain_type", rt_plain),
            (troop_is_guarantee_horse, ":stack_troop"),
            (val_mul, ":stack_strength", 110),
          (else_try),
            (eq, ":terrain_type", rt_snow),
            #        (try_for_range,":items","itm_zrak_wildman_chest","itm_zrak_berserker_chest"),
            #          (troop_has_item_equipped,":stack_troop",":items"),
            #          (val_mul, ":stack_strength", 1.4),
            #        (try_end),
            #        (try_for_range,":items","itm_vaegir_woodcutter_coat","itm_vaegir_woodcutter_helmet"),
            #          (troop_has_item_equipped,":stack_troop",":items"),
            #          (val_mul, ":stack_strength", 1.5),
            #        (try_end),
            (val_mul, ":stack_strength", 95),
          (else_try),
            (eq, ":terrain_type", rt_desert),
            #        (try_for_range,":items","itm_kabiel_villager_chest","itm_kabiel_villager_helmet"),
            #          (troop_is_guarantee_horse, ":stack_troop"),
            #          (troop_has_item_equipped,":stack_troop",":items"),
            #          (val_mul, ":stack_strength", 1.8 ),
            #        (else_try),
            #          (troop_is_guarantee_horse, ":stack_troop"),
            #          (val_mul, ":stack_strength", 1.4),
            #        (try_end),
            (val_mul, ":stack_strength", 95),
          (else_try),
            (eq, ":terrain_type", rt_steppe_forest),
            (troop_is_guarantee_horse, ":stack_troop"),
            (val_mul, ":stack_strength", 120),
          (else_try),
            (eq, ":terrain_type", rt_forest),
            (neg|troop_is_guarantee_horse, ":stack_troop"),
            (neg|troop_is_guarantee_ranged, ":stack_troop"),
            (val_mul, ":stack_strength", 120),
          (else_try),
            (eq, ":terrain_type", rt_snow_forest),
            #        (try_for_range,":items","itm_zrak_wildman_chest","itm_zrak_berserker_chest"),
            #          (troop_has_item_equipped,":stack_troop",":items"),
            #          (val_mul, ":stack_strength", 1.2),
            #        (try_end),
            #        (try_for_range,":items","itm_vaegir_woodcutter_coat","itm_vaegir_woodcutter_helmet"),
            #          (troop_has_item_equipped,":stack_troop",":items"),
            #          (val_mul, ":stack_strength", 1.2),
            #        (try_end),
            (neg|troop_is_guarantee_horse, ":stack_troop"),
            (neg|troop_is_guarantee_ranged, ":stack_troop"),
            (val_mul, ":stack_strength", 120),
		  (else_try),
		    (val_mul, ":stack_strength", 100), ##Caba - ensure the division isn't problematic
          (try_end),
		  (val_div, ":stack_strength", 100), ##Bugfix - Caba, from vhan
          ##AotE terrain advantages
          (try_begin),
            (neg|troop_is_hero, ":stack_troop"),
            (party_stack_get_size, ":stack_size",":party",":i_stack"),
            (party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
            (val_sub, ":stack_size", ":num_wounded"),
            (val_mul, ":stack_strength", ":stack_size"),
          (else_try),
            (troop_is_wounded, ":stack_troop"), #hero & wounded
            (assign, ":stack_strength", 0),
          (try_end),
          (val_add, reg0, ":stack_strength"),
        (try_end),
        (party_set_slot, ":party", slot_party_cached_strength, reg0),
    ]),
    
    
    #script_loot_player_items:
    # INPUT: arg1 = enemy_party_no
    # Output: none
    ("loot_player_items",
		  [
		  (store_script_param, ":enemy_party_no", 1),
		  ##diplomacy start+ some enemy lords will not loot the personal equipment of a player who surrendered
		  (assign, ":save_reg0", reg0),
		  (assign, ":extra_gold", 0),
		  #I am not sure if this is historical or not, but it gives the player a reason to
		  #surrender (rather than fight to the end) even before permanent attribute loss is
		  #a possibility (or even if it is disabled outright).
		  #
		  #This also adds another layer of interaction, and makes different lords feel
		  #different from each other.
		  #
		  #Other changes:
		  # Enemy lords will receive gold they loot from the player,
		  # Books will not be looted from the player (it turns out a bug was responsible for this being possible)
		  # The enemy leader's looting skill will affect the amount of gold lootable.
		  (assign, ":merciful", 0),
		  (assign, ":party_leader", -1),
		  (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
		  (try_begin),
			(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),#only use this if it is explicitly enabled
			#Possibility the player's personal equipment will be untouched if he surrendered
			(ge, "$g_player_surrenders", 1),
			(gt, ":enemy_party_no", 0),
			(party_stack_get_troop_id, ":party_leader", ":enemy_party_no", 0),		
		   #(party_slot_eq, ":enemy_party_no", slot_party_type, spt_kingdom_hero_party),		#Diplo 4.1 Commented
			(ge, ":party_leader", walkers_end),													#Diplo 4.1 Change
			(troop_is_hero, ":party_leader"),
			(call_script, "script_troop_get_player_relation", ":party_leader"),
			(assign, ":relation", reg0),
			(assign, ":probability_modifier", 0),
			(try_begin),
				#Upstanding lords are inclined to honor deals in general, and will automatically
				#do so with honorable lords they do not extremely dislike.  However, this does not
				#extend to commoners.
				(troop_slot_ge, "trp_player", slot_troop_banner_scene_prop, 1),# the player has a coat of arms
				(troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_upstanding),
				(val_max, ":probability_modifier", 10),#set to +10 unless already higher
				#They will automatically honor deals with the honorable, if they do not
				#excessively dislike them.
				(ge, "$player_honor", 1),
				(val_add, reg0, 10),
				(val_clamp, reg0, 11, 21),
				(val_max, ":probability_modifier", reg0),#set somewhere from +11 to +20 unless already higher
				(ge, ":relation", -10),
				(assign, ":merciful", 1),
			(else_try),
				#Martial lords are inclined to honor deals with lords who likewise follow the rules of war,
				#and will do so as long as they are neutral or friendly towards them.  This does not extend
				#to commoners.
				(troop_slot_ge, "trp_player", slot_troop_banner_scene_prop, 1),# the player has a coat of arms
				(this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_moralist),
				(troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_martial),
				(ge, "$player_honor", 1),
				(assign, reg0, "$player_honor"),
				(val_clamp, reg0, 1, 6),
				(val_max, ":probability_modifier", reg0),#set somewhere from +1 to +5 unless already higher
				(ge, ":relation", 0),
				(assign, ":merciful", 1),
			(else_try),
				#Good-natured lords are inclined to honor deals with everyone, commoner or not.
				#They will do so automatically unless they particularly dislike someone.
				#This also goes for Moralist ladies if they someone end up accepting your surrender.
				(this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_goodnatured),
				(troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_moralist),
				(val_max, ":probability_modifier", 21),#set to +20 unless already higher
				(ge, ":relation", -10),
				(assign, ":merciful", 1),
			(else_try),
				#Honest lords are inclined honor deals with everyone, commoner or not.
				#They will do so automatically unless they particularly dislike someone.
				(call_script, "script_dplmc_get_troop_morality_value", ":party_leader", tmt_honest),
				(assign, ":honest_val", reg0),
				(ge, ":honest_val", 1),
				(store_add, reg0, ":honest_val", 14),
				(val_max, ":probability_modifier", reg0),#set to (14 + honesty ) unless already higher
				(ge, "$player_honor", 1),
				(val_mul, reg0, -1),
				(ge, ":relation", reg0),
				(assign, ":merciful", 1),
			(else_try),
				(try_begin),
					#Penalty instead of bonus for vicious lord personalities, unless they are
					#explicitly set as honest.  (None are by default.)
					(lt, ":honest_val", 1),#Must either be negative or not given
					(this_or_next|lt, ":honest_val", 0),
					(this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_debauched),
					(this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_selfrighteous),
					(this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_cunning),
					(troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_quarrelsome),
					(val_min, ":probability_modifier", -10),#set to -10 unless already lower
				(try_end),
				#Now store into reg0 the percent chance of mercy
				(try_begin),
					(le, ":reduce_campaign_ai", 0),#Hard: base chance 25% + relation
					(store_add, reg0, ":relation", 25),
				(else_try),
					(eq, ":reduce_campaign_ai", 1),#Medium: base chance 50% + relation
					(store_add, reg0, ":relation", 50),
				(else_try),
					(ge, ":reduce_campaign_ai", 2),#Easy: base chance 75% + relation
					(store_add, reg0, ":relation", 75),
				(try_end),
				(val_add, reg0, ":probability_modifier"),#modify the chance based on the captor's personality
				(val_max, reg0, ":probability_modifier"),#at least this much of a chance
				(val_max, reg0, 5),#at least a 5% chance
				(store_random_in_range, ":probability_modifier", 1, 101),
				(lt, reg0, ":probability_modifier"),
				(assign, ":merciful", 1),
			(try_end),
		  (else_try),
			(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),#only use this if it is explicitly enabled
			#Surrendered to a non-hero party
			(gt, ":enemy_party_no", 0),
			(ge, "$g_player_surrenders", 1),
			(store_random_in_range, reg0, 1, 101),
			(this_or_next|lt, reg0, 25),#Hard: 25% chance
				(ge, ":reduce_campaign_ai", 1),
			(this_or_next|lt, reg0, 50),#Medium: 50% chance
				(ge, ":reduce_campaign_ai", 2),
			(lt, reg0, 75),#Easy: 75% chance
			(assign, ":merciful", 1),
		  (try_end),
		  (try_begin),
			(ge, "$cheat_mode", 1),
			(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),#don't display when nonapplicable
			(assign, ":save_reg1", reg1),
			(assign, reg0, "$g_player_surrenders"),
			(assign, reg1, ":merciful"),
			(display_message, "@{!} DEBUG loot_player_items: g_player_surrenders = {reg0}, merciful = {reg1}"),
			(assign, reg1, ":save_reg1"),
		  (try_end),
		  ##diplomacy end+
		  (troop_get_inventory_capacity, ":inv_cap", "trp_player"),
		  (try_for_range, ":i_slot", 0, ":inv_cap"),
			(troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
			(ge, ":item_id", 0),
			##diplomacy start+ looting changes
			(neg|is_between, ":item_id", books_begin, books_end),#shouldn't be necessary, but just in case
			(assign, ":randomness", 0),#properly initialize variables
			##diplomacy end+
			(troop_get_inventory_slot_modifier, ":item_modifier", "trp_player", ":i_slot"),
			(try_begin),
			  (is_between, ":item_id", trade_goods_begin, trade_goods_end),
			  (assign, ":randomness", 20),
			(else_try),
			  (is_between, ":item_id", horses_begin, horses_end),
			  (assign, ":randomness", 15),
			(else_try),
			  (this_or_next|is_between, ":item_id", weapons_begin, weapons_end),
			  (is_between, ":item_id", weapons_ranged_begin, weapons_ranged_end),
			  (assign, ":randomness", 5),
			(else_try),
			  (this_or_next|is_between, ":item_id", armors_begin, armors_end),
			  (this_or_next|eq, ":item_id", footgear_begin,footgear_end), #added to the end because of not breaking the save games
			  (is_between, ":item_id", shields_begin, shields_end),
			  (assign, ":randomness", 5),
			(try_end),
			(store_random_in_range, ":random_no", 0, 100),
			(lt, ":random_no", ":randomness"),
			##diplomacy start+ changes
			(try_begin),
				#If this option is enabled, personal items may be spared, and instead
				#sligthly more gold is taken (but not as much as the thing's worth).
				(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
				(ge, ":merciful", 1),
				(is_between, ":i_slot", ek_item_0, dplmc_ek_alt_items_end),
				(assign, ":random_no", 101),
				#(store_item_value, reg0, ":item_id"),#don't bother with imods
				#(val_div, reg0, 2),
				#(ge, reg0, 1),
				#(val_add, ":extra_gold", reg0),##disable, as it defeats the point!
			(try_end),
			(lt, ":random_no", ":randomness"),
			##diplomacy end+
			(troop_remove_item, "trp_player", ":item_id"),

			(try_begin),
			  (gt, ":enemy_party_no", 0),
			  (party_get_slot, ":cur_loot_slot", ":enemy_party_no", slot_party_next_looted_item_slot),
			  (val_add, ":cur_loot_slot", slot_party_looted_item_1),
			  (party_set_slot, ":enemy_party_no", ":cur_loot_slot", ":item_id"),
			  (val_sub, ":cur_loot_slot", slot_party_looted_item_1),
			  (val_add, ":cur_loot_slot", slot_party_looted_item_1_modifier),
			  (party_set_slot, ":enemy_party_no", ":cur_loot_slot", ":item_modifier"),
			  (val_sub, ":cur_loot_slot", slot_party_looted_item_1_modifier),
			  (val_add, ":cur_loot_slot", 1),
			  (val_mod, ":cur_loot_slot", num_party_loot_slots),
			  (party_set_slot, ":enemy_party_no", slot_party_next_looted_item_slot, ":cur_loot_slot"),
			(try_end),
		  (try_end),
		  (store_troop_gold, ":cur_gold", "trp_player"),
		  (store_div, ":max_lost", ":cur_gold", 5),
		  (store_div, ":min_lost", ":cur_gold", 10),
		  (store_random_in_range, ":lost_gold", ":min_lost", ":max_lost"),
		  ##diplomacy start+
		  (try_begin),
			#This does nothing unless the option is enabled.
			(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
			#add extra gold from enemy's looting skill
			(gt, ":enemy_party_no", 0),
			(party_get_skill_level, reg0, ":enemy_party_no", "skl_looting"),
			(val_clamp, reg0, 0, 11),#allow range +0 to +10
			(val_add, reg0, 10),
			(val_mul, ":lost_gold", reg0),
			(val_div, ":lost_gold", 10),
			#Add any gold from items not looted.
			(val_add, ":lost_gold", ":extra_gold"),
			#gold looted can't exceed player's actual gold
			(val_min, ":lost_gold", ":cur_gold"),
			(val_max, ":lost_gold", 0),
		  (try_end),
		  #diplomacy end+
		  (troop_remove_gold, "trp_player", ":lost_gold"),
		  ##diplomacy start+
		  (try_begin),
			#add looted gold to the enemy, if he's a valid hero
			(is_between, ":party_leader", heroes_begin, heroes_end),
			(troop_is_hero, ":party_leader"),
			(neq, ":party_leader", "trp_player"),
			(neq, ":party_leader", "trp_kingdom_heroes_including_player_begin"),
			(ge, ":lost_gold", 1),
			#(call_script, "script_troop_add_gold", ":party_leader", ":lost_gold"),#add looted gold to enemy
			(troop_get_slot, reg0, ":party_leader", slot_troop_wealth),
			(val_add, reg0, ":lost_gold"),
			(val_max, reg0, 0),
			(troop_set_slot, ":party_leader", slot_troop_wealth, reg0),#add looted gold to enemy
		  (try_end),
		  (assign, reg0, ":save_reg0"),#revert register
		  ##diplomacy end+
	  ]),
    
    
    #script_party_calculate_loot:
    # INPUT:
    # param1: Party-id
    # Returns num looted items in reg(0)
    ("party_calculate_loot",
      [
        (store_script_param_1, ":enemy_party"), #Enemy Party_id
        
        (call_script, "script_calculate_main_party_shares"),
        (assign, ":num_player_party_shares", reg0),
        #(assign, ":num_ally_shares", reg1),
        #(store_add, ":num_shares",  ":num_player_party_shares", ":num_ally_shares"),
        
        #Calculate player loot probability
        #(assign, ":loot_probability", 100),
        #(val_mul, ":loot_probability", 10),
        #(val_div, ":loot_probability", ":num_shares"),
        
        (try_for_range, ":i_loot", 0, num_party_loot_slots),
          (store_add, ":cur_loot_slot", ":i_loot", slot_party_looted_item_1),
          (party_get_slot, ":item_no", "$g_enemy_party", ":cur_loot_slot"),
          (gt, ":item_no", 0),
          (party_set_slot, "$g_enemy_party", ":cur_loot_slot", 0),
          (val_sub, ":cur_loot_slot", slot_party_looted_item_1),
          (val_add, ":cur_loot_slot", slot_party_looted_item_1_modifier),
          (party_get_slot, ":item_modifier", "$g_enemy_party", ":cur_loot_slot"),
          (troop_add_item, "trp_temp_troop", ":item_no", ":item_modifier"),
        (try_end),
        (party_set_slot, "$g_enemy_party", slot_party_next_looted_item_slot, 0),
        
        (assign, ":num_looted_items",0),
        (try_begin),
          (this_or_next|party_slot_eq, "$g_enemy_party", slot_party_type, spt_kingdom_caravan),
		  (this_or_next|party_slot_eq, "$g_enemy_party", slot_party_type, spt_merchant_caravan), #Floris Seafaring / Seatrade
          (this_or_next|party_slot_eq, "$g_enemy_party", slot_party_type, spt_bandit_lair),
          (party_slot_eq, "$g_enemy_party", slot_party_type, spt_village_farmer),
          (store_mul, ":plunder_amount", player_loot_share, 30),
          (val_mul, ":plunder_amount", "$g_strength_contribution_of_player"),
          (val_div, ":plunder_amount", 100),
          (val_div, ":plunder_amount", ":num_player_party_shares"),
		  (assign, ":skip", 0), ## Floris
          (try_begin),
			(this_or_next|party_slot_eq, "$g_enemy_party", slot_party_type, spt_merchant_caravan),
            (party_slot_eq, "$g_enemy_party", slot_party_type, spt_kingdom_caravan),
            #(reset_item_probabilities, 100), ## Floris
            #(assign, ":range_min", trade_goods_begin), ## Floris
            #(assign, ":range_max", trade_goods_end), ## Floris
		    (assign, ":skip", 1), ## Floris
          (else_try),
            (party_slot_eq, "$g_enemy_party", slot_party_type, spt_bandit_lair),
            (val_div, ":plunder_amount", 2),
            (reset_item_probabilities, 1),
            (assign, ":range_min", food_begin),
            (assign, ":range_max", food_end),
          (else_try),
            (val_div, ":plunder_amount", 5),
            (reset_item_probabilities, 1),
            (assign, ":range_min", food_begin),
            (assign, ":range_max", food_end),
          (try_end),
		  (try_begin), ## Floris
		    (eq, ":skip", 0), ## Floris
            (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
            (try_for_range, ":cur_goods", ":range_min", ":range_max"),
				(try_begin),
				  (neg|party_slot_eq, "$g_enemy_party", slot_party_type, spt_bandit_lair),
				  (store_add, ":cur_price_slot", ":cur_goods", ":item_to_price_slot"),
				  (party_get_slot, ":cur_price", "$g_enemy_party", ":cur_price_slot"),
				(else_try),
				  (assign, ":cur_price", maximum_price_factor),
				  (val_add, ":cur_price", average_price_factor),
				  (val_div, ":cur_price", 3),
				(try_end),
            
				(assign, ":cur_probability", 100),
				(val_mul, ":cur_probability", average_price_factor),
				(val_div, ":cur_probability", ":cur_price"),
				(assign, reg0, ":cur_probability"),													#	1.143 Port // Removed a few duplicate lines, see native 1.134
				(set_item_probability_in_merchandise, ":cur_goods", ":cur_probability"),
			(try_end),
            (troop_add_merchandise, "trp_temp_troop", itp_type_goods, ":plunder_amount"),
            (val_add, ":num_looted_items", ":plunder_amount"),
		 (else_try),  ## Floris - Trade with Merchant Caravans - this whole else try
		    (eq, ":skip", 1),
			(try_begin),
			    (party_slot_ge, "$g_enemy_party", slot_town_trade_good_productions_begin, ":plunder_amount"),
				(party_set_slot, "$g_enemy_party", slot_town_trade_good_productions_begin, ":plunder_amount"),
			(try_end),
			(call_script, "script_merchant_inventory_from_party_slot", "trp_temp_troop", "$g_enemy_party"),		
		 (try_end), ## Floris - Trade with Merchant Caravans
        (try_end),
        
        #Now loot the defeated party
        (store_mul, ":loot_probability", player_loot_share, 3),
        (val_mul, ":loot_probability", "$g_strength_contribution_of_player"),
        (party_get_skill_level, ":player_party_looting", "p_main_party", "skl_looting"),
        (val_add, ":player_party_looting", 10),
        (val_mul, ":loot_probability", ":player_party_looting"),
        (val_div, ":loot_probability", 10),
        (val_div, ":loot_probability", ":num_player_party_shares"),
        
        ## CC
        (store_add, ":temp_array_c_plus_one", "trp_temp_array_c", 1),
        (try_for_range, ":cur_troop", "trp_temp_array_a", ":temp_array_c_plus_one"),
          (troop_clear_inventory, ":cur_troop"), # clear_inventory
          # raise skl_inventory_management level to 10
          (store_skill_level, ":cur_level", skl_inventory_management, ":cur_troop"),
          (store_sub, ":dest_level", 10, ":cur_level"),
          (troop_raise_skill, ":cur_troop", skl_inventory_management, ":dest_level"),
        (try_end),
        
        (call_script, "script_copy_inventory", "trp_temp_troop", "trp_temp_array_a"),
        
        (party_get_num_companion_stacks, ":num_stacks", ":enemy_party"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop",":enemy_party",":i_stack"),
          (neg|troop_is_hero, ":stack_troop"),
          (party_stack_get_size, ":stack_size",":enemy_party",":i_stack"),
          (try_for_range, ":unused", 0, ":stack_size"),
            (try_begin),
              (store_free_inventory_capacity, ":inv_cap_a", "trp_temp_array_a"),
              (gt, ":inv_cap_a", 0),
              (troop_loot_troop, "trp_temp_array_a", ":stack_troop", ":loot_probability"),
            (else_try),
              (store_free_inventory_capacity, ":inv_cap_b", "trp_temp_array_b"),
              (gt, ":inv_cap_b", 0),
              (troop_loot_troop, "trp_temp_array_b", ":stack_troop", ":loot_probability"),
            (else_try),
              (troop_loot_troop, "trp_temp_array_c", ":stack_troop", ":loot_probability"),
            (try_end),
          (try_end),
        (try_end),
        
        (troop_clear_inventory, "trp_temp_troop"),
        (try_for_range, ":unused", 0, 96), # for 96 times
          # find the best item
          (assign, ":best_score", 0),
          (assign, ":best_troop", -1),
          (assign, ":best_slot", -1),
          (try_for_range, ":cur_troop", "trp_temp_array_a", ":temp_array_c_plus_one"),
            (troop_get_inventory_capacity, ":inv_cap", ":cur_troop"),
            (try_for_range, ":i_slot", 10, ":inv_cap"),
              (troop_get_inventory_slot, ":item", ":cur_troop", ":i_slot"),
              (troop_get_inventory_slot_modifier, ":imod", ":cur_troop", ":i_slot"),
              (gt, ":item", -1),
              (call_script, "script_get_item_value_with_imod", ":item", ":imod"),
              (assign, ":score", reg0),
              (val_div, ":score", 100),
              (val_max, ":score",1),
              (gt, ":score", ":best_score"),
              (assign, ":best_score", ":score"),
              (assign, ":best_troop", ":cur_troop"),
              (assign, ":best_slot", ":i_slot"),
            (try_end),
          (try_end),
          (gt, ":best_score", 0),
          # already found
          (troop_get_inventory_slot, ":item", ":best_troop", ":best_slot"),
          (troop_get_inventory_slot_modifier, ":imod", ":best_troop", ":best_slot"),
          (troop_add_item, "trp_temp_troop", ":item", ":imod"), # add to trp_temp_troop
          (troop_set_inventory_slot, ":best_troop", ":best_slot", -1), # remove it
        (try_end),
        ## CC
        
        #(troop_get_inventory_capacity, ":inv_cap", "trp_temp_troop"),
        #(try_for_range, ":i_slot", 0, ":inv_cap"),
        #  (troop_get_inventory_slot, ":item_id", "trp_temp_troop", ":i_slot"),
        #  (is_between, ":item_id", horses_begin, horses_end),
        #  (troop_set_inventory_slot, "trp_temp_troop", ":i_slot", -1),
        #(try_end),
        
        (troop_get_inventory_capacity, ":inv_cap", "trp_temp_troop"),
        (try_for_range, ":i_slot", 0, ":inv_cap"),
          (troop_get_inventory_slot, ":item_id", "trp_temp_troop", ":i_slot"),
          (ge, ":item_id", 0),
          (val_add, ":num_looted_items", 1),
        (try_end),
        ## CC
        (try_begin),
          (gt, ":num_looted_items", 0),
          (troop_sort_inventory, "trp_temp_troop"),
          (call_script, "script_give_good_item_modifier", ":enemy_party", ":num_looted_items"),
        (try_end),
        ## CC
        (assign, reg0, ":num_looted_items"),
    ]),
    
    #script_calculate_main_party_shares:
    # INPUT:
    # Returns number of player party shares in reg0
    ("calculate_main_party_shares",
      [
        (assign, ":num_player_party_shares", player_loot_share),
        # Add shares for player's party
        (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
        (try_for_range, ":i_stack", 1, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
          (try_begin),
            (neg|troop_is_hero, ":stack_troop"),
            (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
            (val_add, ":num_player_party_shares", ":stack_size"),
          (else_try),
            (val_add, ":num_player_party_shares", hero_loot_share),
          (try_end),
        (try_end),
        
        (assign, reg0, ":num_player_party_shares"),
    ]),
    
    #script_party_give_xp_and_gold:
    # INPUT:
    # param1: destroyed Party-id
    # calculates and gives player paty's share of gold and xp.
    
    ("party_give_xp_and_gold",
      [
        (store_script_param_1, ":enemy_party"), #Party_id
        
        (call_script, "script_calculate_main_party_shares"),
        (assign, ":num_player_party_shares", reg0),
        
        (assign, ":total_gain", 0),
        (party_get_num_companion_stacks, ":num_stacks",":enemy_party"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id,     ":stack_troop",":enemy_party",":i_stack"),
          (neg|troop_is_hero, ":stack_troop"),
          (party_stack_get_size, ":stack_size",":enemy_party",":i_stack"),
          (store_character_level, ":level", ":stack_troop"),
          (store_add, ":gain", ":level", 10),
          (val_mul, ":gain", ":gain"),
          (val_div, ":gain", 10),
          (store_mul, ":stack_gain", ":gain", ":stack_size"),
          (val_add, ":total_gain", ":stack_gain"),
        (try_end),
        
        (val_mul, ":total_gain", "$g_strength_contribution_of_player"),
        (val_div, ":total_gain", 100),
        
        (val_min, ":total_gain", 40000), #eliminate negative results
        
        (assign, ":player_party_xp_gain", ":total_gain"),
        
        (store_random_in_range, ":r", 50, 100),
        (val_mul, ":player_party_xp_gain", ":r"),
        (val_div, ":player_party_xp_gain", 100),
        
        (party_add_xp, "p_main_party", ":player_party_xp_gain"),
        
        (store_mul, ":player_gold_gain", ":total_gain", player_loot_share),
        (val_min, ":player_gold_gain", 60000), #eliminate negative results
        (store_random_in_range, ":r", 50, 100),
        (val_mul, ":player_gold_gain", ":r"),
        (val_div, ":player_gold_gain", 100),
		## Floris - Trade with Merchant Caravans
	    (try_begin),
	        (party_slot_eq, ":enemy_party", slot_party_type, spt_kingdom_caravan),
		    (party_get_slot, ":wealth", ":enemy_party", slot_town_wealth),
		    (val_add, ":player_gold_gain", ":wealth"),
	    (try_end),
	    ## Floris - Trade with Merchant Caravans
        (val_div, ":player_gold_gain", ":num_player_party_shares"),
		
        
        #add gold now
        (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop","p_main_party",":i_stack"),
          (try_begin),
            (troop_is_hero, ":stack_troop"),
            (call_script, "script_troop_add_gold", ":stack_troop", ":player_gold_gain"),
          (try_end),
        (try_end),
    ]),
    
    
    #script_setup_troop_meeting:
    # INPUT:
    # param1: troop_id with which meeting will be made.
    # param2: troop_dna (optional)
    
    ("setup_troop_meeting",
      [
        (store_script_param_1, ":meeting_troop"),
        (store_script_param_2, ":troop_dna"),
        (call_script, "script_get_meeting_scene"),
        (assign, ":meeting_scene", reg0),
        (modify_visitors_at_site,":meeting_scene"),
        (reset_visitors),
        (set_visitor,0,"trp_player"),
        (try_begin),
          (gt, ":troop_dna", -1),
          (set_visitor,17,":meeting_troop",":troop_dna"),
        (else_try),
          (set_visitor,17,":meeting_troop"),
        (try_end),
        (set_jump_mission,"mt_conversation_encounter"),
        (jump_to_scene,":meeting_scene"),
        (change_screen_map_conversation, ":meeting_troop"),
    ]),
    
    #script_setup_party_meeting:
    # INPUT:
    # param1: Party-id with which meeting will be made.
    
    ("setup_party_meeting",
      [
        (store_script_param_1, ":meeting_party"),
        (try_begin),
          (lt, "$g_encountered_party_relation", 0), #hostile
          #        (call_script, "script_music_set_situation_with_culture", mtf_sit_encounter_hostile),
        (try_end),
        (call_script, "script_get_meeting_scene"), (assign, ":meeting_scene", reg0),
        (modify_visitors_at_site,":meeting_scene"),(reset_visitors),
        (set_visitor,0,"trp_player"),
        (party_stack_get_troop_id, ":meeting_troop",":meeting_party",0),
        (party_stack_get_troop_dna,":troop_dna",":meeting_party",0),
        (set_visitor,17,":meeting_troop",":troop_dna"),
        (set_jump_mission,"mt_conversation_encounter"),
        (jump_to_scene,":meeting_scene"),
        (change_screen_map_conversation, ":meeting_troop"),
    ]),
    
    #script_get_meeting_scene:
    # INPUT: none
    # OUTPUT: reg0 contain suitable scene_no
    
    ("get_meeting_scene",
      [
        (party_get_current_terrain, ":terrain_type", "p_main_party"),
        (assign, ":scene_to_use", "scn_random_scene"),
        (try_begin),
          (eq, ":terrain_type", rt_steppe),
          (assign, ":scene_to_use", "scn_meeting_scene_steppe"),
        (else_try),
          (eq, ":terrain_type", rt_plain),
          (assign, ":scene_to_use", "scn_meeting_scene_plain"),
        (else_try),
          (eq, ":terrain_type", rt_snow),
          (assign, ":scene_to_use", "scn_meeting_scene_snow"),
        (else_try),
          (eq, ":terrain_type", rt_desert),
          (assign, ":scene_to_use", "scn_meeting_scene_desert"),
        (else_try),
          (eq, ":terrain_type", rt_steppe_forest),
          (assign, ":scene_to_use", "scn_meeting_scene_steppe"),
        (else_try),
          (eq, ":terrain_type", rt_forest),
          (assign, ":scene_to_use", "scn_meeting_scene_plain"),
        (else_try),
          (eq, ":terrain_type", rt_snow_forest),
          (assign, ":scene_to_use", "scn_meeting_scene_snow"),
        (else_try),
          (eq, ":terrain_type", rt_desert_forest),
          (assign, ":scene_to_use", "scn_meeting_scene_desert"),
        (else_try),
          (assign, ":scene_to_use", "scn_meeting_scene_plain"),
        (try_end),
        (assign, reg0, ":scene_to_use"),
    ]),
    
    
    #script_party_remove_all_companions:
    # INPUT:
    # param1: Party-id from which  companions will be removed.
    # "$g_move_heroes" : controls if heroes will also be removed.
    
    ("party_remove_all_companions",
      [
        (store_script_param_1, ":party"), #Source Party_id
        (party_get_num_companion_stacks, ":num_companion_stacks",":party"),
        (try_for_range_backwards, ":stack_no", 0, ":num_companion_stacks"),
          (party_stack_get_troop_id, ":stack_troop",":party",":stack_no"),
          
          (party_stack_get_size, ":stack_size", ":party", ":stack_no"),
          
        (try_begin),
			##diplomacy start+
			  #To avoid problems with temporarily-rejoined promoted companions and ladies
			  #suddenly forgetting that they're lords, check this.
				#If the troop is a companion or a kingdom lady...
				(this_or_next|is_between, ":stack_troop", companions_begin, companions_end),
					(is_between, ":stack_troop", kingdom_ladies_begin, kingdom_ladies_end),
				#...but has since become a lord
				(this_or_next|troop_slot_eq, ":stack_troop", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
				(this_or_next|troop_slot_eq, ":stack_troop", slot_troop_playerparty_history, dplmc_pp_history_lord_rejoined),
					(troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
				#...and the troop would be removed
				(this_or_next|eq, "$g_move_heroes", 1),
					(eq, ":party", "p_main_party"),
				#Then set up the troop as if it was a lord that was just defeated but escaped
				(troop_set_slot, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
				(troop_set_slot, ":stack_troop", slot_troop_leaded_party, -1),
				(troop_set_slot, ":stack_troop", slot_troop_prisoner_of_party, -1),
				(troop_set_slot, ":stack_troop", slot_troop_cur_center, -1),
				(party_remove_members, ":party", ":stack_troop", ":stack_size"),
			#Fall through to standard behavior:
		(else_try),
			##diplomacy end+
            (troop_is_hero, ":stack_troop"),
            (neg|is_between, ":stack_troop", pretenders_begin, pretenders_end),
            (neq, ":stack_troop", "trp_player"),
            (eq, "$g_prison_heroes", 1),
            (eq, ":party", "p_main_party"),
            (store_random_in_range, ":succeed_escaping", 0, 2),
            (neq, ":succeed_escaping", 0), #50% chance companion stays with us.
            (troop_set_health, ":stack_troop", 100), #heal before leaving
            (store_faction_of_party, ":enemy_faction", "$g_enemy_party"),
            (assign, ":minimum_distance", 99999),
            (assign, ":prison_center", -1),
            (try_for_range, ":center", walled_centers_begin, walled_centers_end),
              (store_faction_of_party, ":center_faction", ":center"),
              (eq, ":center_faction", ":enemy_faction"),
              (store_distance_to_party_from_party, ":dist", ":center", "p_main_party"),
              (lt, ":dist", ":minimum_distance"),
              (assign, ":minimum_distance", ":dist"),
              (assign, ":prison_center", ":center"),
            (try_end),
            (assign, reg1, ":prison_center"),
            #(display_message, "@{!}DEBUG : prison center is {reg1}"),
            (try_begin),
              (ge, ":prison_center", 0),
              (store_random_in_range, ":succeed_escaping", 0, 4),
              (neq, ":succeed_escaping", 0), #25% chance companion escapes to a tavern.
              (party_add_prisoners, ":prison_center", ":stack_troop", ":stack_size"),
              (troop_set_slot, ":stack_troop", slot_troop_prisoner_of_party, ":prison_center"),
              (troop_set_slot, ":stack_troop", slot_troop_playerparty_history, pp_history_scattered),
              (troop_set_slot, ":stack_troop", slot_troop_turned_down_twice, 0),
              (troop_set_slot, ":stack_troop", slot_troop_occupation, 0),
              (party_remove_members, ":party", ":stack_troop", ":stack_size"),
              (try_begin),
                (eq, "$cheat_mode", 1),
                (str_store_party_name, s1, ":prison_center"),
                (display_message, "str_your_hero_prisoned_at_s1"),
              (try_end),
            (else_try),
              #bandits or deserters won and captured companion. So place it randomly in a town's tavern.
              (assign, ":end_condition", 1000),
              (try_for_range, ":unused", 0, ":end_condition"),
              (store_random_in_range, ":town_no", towns_begin, towns_end),
			  ##diplomacy start+
			  #OLD (NATIVE) VERSION:
			  #(neg|troop_slot_eq, ":stack_troop", slot_troop_home, ":town_no"),
              #(neg|troop_slot_eq, ":stack_troop", slot_troop_first_encountered, ":town_no"),
			  #
			  #NEW (DIPLOMACY+) VERSION:
			  #If the player owns the town, the companion is no longer in "never return" mode.
			  (party_get_slot, ":town_lord", ":town_no", slot_town_lord),
			  (this_or_next|eq, ":town_lord", "trp_player"),
			  (this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, ":town_lord"),
				(neg|troop_slot_eq, ":stack_troop", slot_troop_home, ":town_no"),
              (this_or_next|eq, ":town_lord", "trp_player"),
			  (this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, ":town_lord"),
			     (neg|troop_slot_eq, ":stack_troop", slot_troop_first_encountered, ":town_no"),
			  ##diplomacy end+
              (assign, ":end_condition", -1),
			(try_end),
              (troop_set_slot, ":stack_troop", slot_troop_cur_center, ":town_no"),
              (troop_set_slot, ":stack_troop", slot_troop_playerparty_history, pp_history_scattered),
              (troop_set_slot, ":stack_troop", slot_troop_turned_down_twice, 0),
              (troop_set_slot, ":stack_troop", slot_troop_occupation, 0),
              (party_remove_members, ":party", ":stack_troop", ":stack_size"),
              (try_begin),
                (eq, "$cheat_mode", 1),
                (str_store_troop_name, 4, ":stack_troop"),
                (str_store_party_name, 5, ":town_no"),
                (display_message, "@{!}{s4} is sent to {s5} after defeat"),
              (try_end),
            (try_end),
          (else_try),
            (this_or_next|neg|troop_is_hero, ":stack_troop"),
            (eq, "$g_move_heroes", 1),
            (party_remove_members, ":party", ":stack_troop", ":stack_size"),
          (try_end),
        (try_end),
    ]),
    
    #script_party_remove_all_prisoners:
    # INPUT:
    # param1: Party-id from which  prisoners will be removed.
    # "$g_move_heroes" : controls if heroes will also be removed.
    
    ("party_remove_all_prisoners",
      [
        (store_script_param_1, ":party"), #Source Party_id
        (party_get_num_prisoner_stacks, ":num_prisoner_stacks",":party"),
        (try_for_range_backwards, ":stack_no", 0, ":num_prisoner_stacks"),
          (party_prisoner_stack_get_troop_id, ":stack_troop",":party",":stack_no"),
          (this_or_next|neg|troop_is_hero, ":stack_troop"),
          (eq, "$g_move_heroes", 1),
          (party_prisoner_stack_get_size, ":stack_size",":party",":stack_no"),
          (party_remove_prisoners, ":party", ":stack_troop", ":stack_size"),
        (try_end),
    ]),
    
    #script_party_add_party_companions:
    # INPUT:
    # param1: Party-id to add the second part
    # param2: Party-id which will be added to the first one.
    # "$g_move_heroes" : controls if heroes will also be added.
    
    ("party_add_party_companions",
      [
        (store_script_param_1, ":target_party"), #Target Party_id
        (store_script_param_2, ":source_party"), #Source Party_id
        (party_get_num_companion_stacks, ":num_stacks",":source_party"),
        (try_for_range, ":stack_no", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop",":source_party",":stack_no"),
          (this_or_next|neg|troop_is_hero, ":stack_troop"),
          (eq, "$g_move_heroes", 1),
          (party_stack_get_size, ":stack_size",":source_party",":stack_no"),
          (party_add_members, ":target_party", ":stack_troop", ":stack_size"),
          (party_stack_get_num_wounded, ":num_wounded", ":source_party", ":stack_no"),
          (party_wound_members, ":target_party", ":stack_troop", ":num_wounded"),
        (try_end),
    ]),
    
    #script_party_add_party_prisoners:
    # INPUT:
    # param1: Party-id to add the second party
    # param2: Party-id which will be added to the first one.
    # "$g_move_heroes" : controls if heroes will also be added.
    
    ("party_add_party_prisoners",
      [
        (store_script_param_1, ":target_party"), #Target Party_id
        (store_script_param_2, ":source_party"), #Source Party_id
        (party_get_num_prisoner_stacks, ":num_stacks",":source_party"),
        (try_for_range, ":stack_no", 0, ":num_stacks"),
          (party_prisoner_stack_get_troop_id, ":stack_troop",":source_party",":stack_no"),
          (this_or_next|neg|troop_is_hero, ":stack_troop"),
          (eq, "$g_move_heroes", 1),
          (party_prisoner_stack_get_size, ":stack_size",":source_party",":stack_no"),
          (party_add_members, ":target_party", ":stack_troop", ":stack_size"),
        (try_end),
    ]),
    
    #script_party_prisoners_add_party_companions:
    # INPUT:
    # param1: Party-id to add the second part
    # param2: Party-id which will be added to the first one.
    # "$g_move_heroes" : controls if heroes will also be added.
    
    ("party_prisoners_add_party_companions",
      [
        (store_script_param_1, ":target_party"), #Target Party_id
        (store_script_param_2, ":source_party"), #Source Party_id
        (party_get_num_companion_stacks, ":num_stacks",":source_party"),
        (try_for_range, ":stack_no", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop",":source_party",":stack_no"),
          (this_or_next|neg|troop_is_hero, ":stack_troop"),
          (eq, "$g_move_heroes", 1),
          (party_stack_get_size, ":stack_size",":source_party",":stack_no"),
          (party_add_prisoners, ":target_party", ":stack_troop", ":stack_size"),
        (try_end),
    ]),
    
    #script_party_prisoners_add_party_prisoners:
    # INPUT:
    # param1: Party-id to add the second part
    # param2: Party-id which will be added to the first one.
    # "$g_move_heroes" : controls if heroes will also be added.
    
    ("party_prisoners_add_party_prisoners",
      [
        (store_script_param_1, ":target_party"), #Target Party_id
        (store_script_param_2, ":source_party"), #Source Party_id
        (party_get_num_prisoner_stacks, ":num_stacks",":source_party"),
        (try_for_range, ":stack_no", 0, ":num_stacks"),
          (party_prisoner_stack_get_troop_id, ":stack_troop",":source_party",":stack_no"),
          (this_or_next|neg|troop_is_hero, ":stack_troop"),
          (eq, "$g_move_heroes", 1),
          (party_prisoner_stack_get_size, ":stack_size",":source_party",":stack_no"),
          (party_add_prisoners, ":target_party", ":stack_troop", ":stack_size"),
        (try_end),
    ]),
    
    # script_party_add_party:
    # INPUT:
    # param1: Party-id to add the second part
    # param2: Party-id which will be added to the first one.
    # "$g_move_heroes" : controls if heroes will also be added.
    
    ("party_add_party",
      [
        (store_script_param_1, ":target_party"), #Target Party_id
        (store_script_param_2, ":source_party"), #Source Party_id
        (call_script, "script_party_add_party_companions",          ":target_party", ":source_party"),
        (call_script, "script_party_prisoners_add_party_prisoners", ":target_party", ":source_party"),
    ]),
    
    
    #script_party_copy:
    # INPUT:
    # param1: Party-id to copy the second party
    # param2: Party-id which will be copied to the first one.
    
    ("party_copy",
      [
        (assign, "$g_move_heroes", 1),
        (store_script_param_1, ":target_party"), #Target Party_id
        (store_script_param_2, ":source_party"), #Source Party_id
        (party_clear, ":target_party"),
        (call_script, "script_party_add_party", ":target_party", ":source_party"),
    ]),
    
    
    #script_clear_party_group:
    # INPUT:
    # param1: Party-id of the root of the group.
    # This script will clear the root party and all parties attached to it recursively.
    
    ("clear_party_group",
      [
        (store_script_param_1, ":root_party"),
        
        (party_clear, ":root_party"),
        (party_get_num_attached_parties, ":num_attached_parties", ":root_party"),
        (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
          (party_get_attached_party_with_rank, ":attached_party", ":root_party", ":attached_party_rank"),
          (call_script, "script_clear_party_group", ":attached_party"),
        (try_end),
    ]),
    
    
    #script_party_add_wounded_members_as_prisoners:
    # INPUT:
    # param1: Party-id to add the second party
    # param2: Party-id which will be added to the first one.
    # "$g_move_heroes" : controls if heroes will also be added.
    
    ("party_add_wounded_members_as_prisoners",
      [
        (store_script_param_1, ":target_party"), #Target Party_id
        (store_script_param_2, ":source_party"), #Source Party_id
        (party_get_num_companion_stacks, ":num_stacks", ":source_party"),
        (try_for_range, ":stack_no", 0, ":num_stacks"),
          (party_stack_get_num_wounded, ":num_wounded", ":source_party", ":stack_no"),
          (ge, ":num_wounded", 1),
          (party_stack_get_troop_id, ":stack_troop", ":source_party", ":stack_no"),
          (this_or_next|neg|troop_is_hero, ":stack_troop"),
          (eq, "$g_move_heroes", 1),
          #(party_prisoner_stack_get_size, ":stack_size",":source_party",":stack_no"),
          (party_add_prisoners, ":target_party", ":stack_troop", ":num_wounded"),
        (try_end),
    ]),
    
    
    #script_get_nonempty_party_in_group:
    # INPUT:
    # param1: Party-id of the root of the group.
    # OUTPUT: reg0: nonempy party-id
    
    ("get_nonempty_party_in_group",
      [
        (store_script_param_1, ":party_no"),
        (party_get_num_companion_stacks, ":num_companion_stacks", ":party_no"),
        (try_begin),
          (gt, ":num_companion_stacks", 0),
          (assign, reg0, ":party_no"),
        (else_try),
          (assign, reg0, -1),
          
          (party_get_num_attached_parties, ":num_attached_parties", ":party_no"),
          (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
            (lt, reg0, 0),
            (party_get_attached_party_with_rank, ":attached_party", ":party_no", ":attached_party_rank"),
            (call_script, "script_get_nonempty_party_in_group", ":attached_party"),
          (try_end),
        (try_end),
    ]),
    
    #script_collect_prisoners_from_empty_parties:
    # INPUT:
    # param1: Party-id of the root of the group.
    # param2: Party to collect prisoners in.
    # make sure collection party is cleared before calling this.
    
    ("collect_prisoners_from_empty_parties",
      [
        (store_script_param_1, ":party_no"),
        (store_script_param_2, ":collection_party"),
        
        (party_get_num_companions, ":num_companions", ":party_no"),
        (try_begin),
          (eq, ":num_companions", 0), #party is empty (has no companions). Collect its prisoners.
          (party_get_num_prisoner_stacks, ":num_stacks",":party_no"),
          (try_for_range, ":stack_no", 0, ":num_stacks"),
            (party_prisoner_stack_get_troop_id, ":stack_troop", ":party_no", ":stack_no"),
            (troop_is_hero, ":stack_troop"),
            (party_add_members, ":collection_party", ":stack_troop", 1),
          (try_end),
        (try_end),
        (party_get_num_attached_parties, ":num_attached_parties", ":party_no"),
        (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
          (party_get_attached_party_with_rank, ":attached_party", ":party_no", ":attached_party_rank"),
          (call_script, "script_collect_prisoners_from_empty_parties", ":attached_party", ":collection_party"),
        (try_end),
    ]),
    
    #script_change_party_morale:
    # INPUT: party_no, morale_gained
    # OUTPUT: none
    
    ("change_party_morale",
      [
        (store_script_param_1, ":party_no"),
        (store_script_param_2, ":morale_dif"),
        
        (party_get_morale, ":cur_morale", ":party_no"),
        (store_add, ":new_morale", ":cur_morale", ":morale_dif"),
        (val_clamp, ":new_morale", 0, 100),
        (party_set_morale, ":party_no", ":new_morale"),
        (str_store_party_name, s1, ":party_no"),
        
        (try_begin),
          (lt, ":new_morale", ":cur_morale"),
          (store_sub, reg1, ":cur_morale", ":new_morale"),
        (else_try),
          (gt, ":new_morale", ":cur_morale"),
          (store_sub, reg1, ":new_morale", ":cur_morale"),
        (try_end),
    ]),
    
    #script_count_casualties_and_adjust_morale:
    # INPUT: none
    # OUTPUT: none
    
    ("count_casualties_and_adjust_morale",
      [
        (call_script, "script_calculate_main_party_shares"),
        (assign, ":num_player_party_shares", reg0),
        
        (assign, ":our_loss_score", 0),
        (party_get_num_companion_stacks, ":num_stacks","p_player_casualties"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", "p_player_casualties", ":i_stack"),
          (party_stack_get_size, ":stack_size", "p_player_casualties", ":i_stack"),
          
          (party_stack_get_num_wounded, ":num_wounded", "p_player_casualties", ":i_stack"),
          (store_mul, ":stack_size_mul_2", ":stack_size", 2),
	      ##diplomacy start+ Fix what appears to be a mistake in Native
	      #(store_sub, ":stack_size_mul_2_sub_wounded", ":num_wounded"),##OLD
	      (store_sub, ":stack_size_mul_2_sub_wounded", ":stack_size_mul_2", ":num_wounded"),##NEW
	      ##diplomacy end+
          
          (store_character_level, ":level", ":stack_troop"),
          (store_add, ":gain", ":level", 3),
          
          #if died/wounded troop is player troop then give its level +30 while calculating troop die effect on morale
          (try_begin),
            (eq, ":stack_troop", "trp_player"),
            (val_add, ":level", 75),
          (else_try),
            (troop_is_hero, ":stack_troop"),
            (val_add, ":level", 50),
          (try_end),
          
          (val_mul, ":gain", ":gain"),
          (val_div, ":gain", 10),
          (assign, reg0, ":gain"),
          (val_mul, ":gain", ":stack_size"),
          
          (try_begin),
            (neg|troop_is_hero, ":stack_troop"),
            (val_mul, ":gain", ":stack_size_mul_2_sub_wounded"),
            (val_div, ":gain", ":stack_size_mul_2"),
          (try_end),
          
          (try_begin),
            (eq, "$cheat_mode", 1),
            (assign, reg1, ":stack_size"),
            (assign, reg2, ":gain"),
            (display_message, "str_our_per_person__reg0_num_people__reg1_total_gain__reg2"),
          (try_end),
          (val_add, ":our_loss_score", ":gain"),
        (try_end),
        
        (assign, ":died_enemy_population", 0),
        (assign, ":enemy_loss_score", 0),
        (party_get_num_companion_stacks, ":num_stacks","p_enemy_casualties"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", "p_enemy_casualties", ":i_stack"),
          (party_stack_get_size, ":stack_size", "p_enemy_casualties", ":i_stack"),
          
          (party_stack_get_num_wounded, ":num_wounded", "p_enemy_casualties", ":i_stack"),
          (store_mul, ":stack_size_mul_2", ":stack_size", 2),
	        ##diplomacy start+ Fix what appears to be a mistake in Native
	        #(store_sub, ":stack_size_mul_2_sub_wounded", ":num_wounded"),##OLD
	        (store_sub, ":stack_size_mul_2_sub_wounded", ":stack_size_mul_2", ":num_wounded"),##NEW
	        ##diplomacy end+
          
          (store_character_level, ":level", ":stack_troop"),
          (store_add, ":gain", ":level", 3),
          
          #if troop is hero give extra +15 level while calculating troop die effect on morale
          (try_begin),
            (troop_is_hero, ":stack_troop"),
            (val_add, ":level", 50),
          (try_end),
          
          (val_mul, ":gain", ":gain"),
          (val_div, ":gain", 10),
          (assign, reg0, ":gain"),
          (val_mul, ":gain", ":stack_size"),
          
          (try_begin),
            (neg|troop_is_hero, ":stack_troop"),
            (val_mul, ":gain", ":stack_size_mul_2_sub_wounded"),
            (val_div, ":gain", ":stack_size_mul_2"),
          (try_end),
          
          (try_begin),
            (eq, "$cheat_mode", 1),
            (assign, reg1, ":stack_size"),
            (assign, reg2, ":gain"),
            (display_message, "str_ene_per_person__reg0_num_people__reg1_total_gain__reg2"),
          (try_end),
          (val_add, ":enemy_loss_score", ":gain"),
          (val_add, ":died_enemy_population", ":stack_size"),
        (try_end),
        
        (assign, ":ally_loss_score", 0),
        (try_begin),
          (eq, "$any_allies_at_the_last_battle", 1),
          (party_get_num_companion_stacks, ":num_stacks","p_ally_casualties"),
          (try_for_range, ":i_stack", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", "p_ally_casualties", ":i_stack"),
            (party_stack_get_size, ":stack_size", "p_ally_casualties", ":i_stack"),
            
            (party_stack_get_num_wounded, ":num_wounded", "p_ally_casualties", ":i_stack"),
            (store_mul, ":stack_size_mul_2", ":stack_size", 2),
            (store_sub, ":stack_size_mul_2_sub_wounded", ":num_wounded"),
            
            (store_character_level, ":level", ":stack_troop"),
            (store_add, ":gain", ":level", 3),
            
            #if troop is hero give extra +15 level while calculating troop die effect on morale
            (try_begin),
              (troop_is_hero, ":stack_troop"),
              (val_add, ":level", 50),
            (try_end),
            
            (val_mul, ":gain", ":gain"),
            (val_div, ":gain", 10),
            (assign, reg0, ":gain"),
            (val_mul, ":gain", ":stack_size"),
            
            (try_begin),
              (neg|troop_is_hero, ":stack_troop"),
              (val_mul, ":gain", ":stack_size_mul_2_sub_wounded"),
              (val_div, ":gain", ":stack_size_mul_2"),
            (try_end),
            
            (try_begin),
              (eq, "$cheat_mode", 1),
              (assign, reg1, ":stack_size"),
              (assign, reg2, ":gain"),
              (display_message, "str_all_per_person__reg0_num_people__reg1_total_gain__reg2"),
            (try_end),
            (val_add, ":ally_loss_score", ":gain"),
          (try_end),
        (try_end),
        
        (store_add, ":our_losses", ":our_loss_score", ":ally_loss_score"),
        (assign, ":enemy_losses", ":enemy_loss_score"),
        (val_mul, ":our_losses", 100),
        
        (try_begin),
          (eq, "$cheat_mode", 1),
          (assign, reg0, ":enemy_losses"),
          (display_message, "@{!}DEBUGS : enemy_loses : {reg0}"),
        (try_end),
        
        (try_begin),
          (gt, ":enemy_losses", 0),
          (store_div, ":loss_ratio", ":our_losses", ":enemy_losses"),
        (else_try),
          (assign, ":loss_ratio", 1000),
        (try_end),
        
        (try_begin),
          (eq, "$cheat_mode", 1),
          (assign, reg1, ":loss_ratio"),
          (display_message, "str_loss_ratio_is_reg1"),
        (try_end),
        
        (try_begin),
          (neg|is_between, "$g_enemy_party", centers_begin, centers_end),
          (store_sub, ":total_gain", 60, ":loss_ratio"),
        (else_try),
          (store_sub, ":total_gain", 100, ":loss_ratio"),
        (try_end),
        
        (try_begin),
          (lt, ":total_gain", 0),
          (val_div, ":total_gain", 2),
        (try_end),
        
        (try_begin),
          (eq, "$cheat_mode", 1),
          (assign, reg0, ":total_gain"),
          (display_message, "@{!}DEBUGS1 : total_gain : {reg0}"),
        (try_end),
        
        (val_max, ":total_gain", -60), #total gain changes between -60(1.8+ loss ratio) and 60(0 loss ratio). We assumed average loss ratio is 0.6
        (val_mul, ":total_gain", ":enemy_losses"),
        (val_div, ":total_gain", 100),
        
        (store_mul, ":total_enemy_morale_gain", ":total_gain", -1), #enemies get totally negative of the morale we get
        (val_mul, ":total_gain", "$g_strength_contribution_of_player"),
        (val_div, ":total_gain", 100),
        
        (try_begin),
          (eq, "$cheat_mode", 1),
          (assign, reg0, ":total_gain"),
          (display_message, "@{!}DEBUGS2 : total_gain : {reg0}"),
        (try_end),
        
        (try_begin),
          (party_is_active, "$g_enemy_party"), #change enemy morale if and only if there is a valid enemy party
          
          #main enemy party
          (assign, ":total_enemy_population", 0),
          (val_add, ":total_enemy_population", 10), #every part effect total population by number of agents they have plus 10
          (party_get_num_companion_stacks, ":num_stacks", "$g_enemy_party"),
          (try_for_range, ":i_stack", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", "$g_enemy_party", ":i_stack"),
            (party_stack_get_size, ":stack_size", "$g_enemy_party", ":i_stack"),
            (val_add, ":total_enemy_population", ":stack_size"),
          (try_end),
          (assign, ":main_enemy_party_population", ":total_enemy_population"),
          
          #enemy attachers
          (party_get_num_attached_parties, ":num_attached_parties", "$g_enemy_party"),
          (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
            (val_add, ":total_enemy_population", 10), #every part effect total population by number of agents they have plus 10
            (party_get_attached_party_with_rank, ":attached_party", "$g_enemy_party", ":attached_party_rank"),
            (party_get_num_companion_stacks, ":num_stacks", ":attached_party"),
            (try_for_range, ":i_stack", 0, ":num_stacks"),
              (party_stack_get_troop_id, ":stack_troop", ":attached_party", ":i_stack"),
              (party_stack_get_size, ":stack_size", ":attached_party", ":i_stack"),
              (val_add, ":total_enemy_population", ":stack_size"),
            (try_end),
          (try_end),
          
          #(assign, reg3, ":total_enemy_population"),
          #(assign, reg4, ":died_enemy_population"),
          #(store_sub, ":remaining_enemy_population", ":total_enemy_population", ":died_enemy_population"),
          #(val_add, ":remaining_enemy_population", 10),
          #(assign, reg5, ":remaining_enemy_population"),
          #(display_message, "@total : {reg3}, died : {reg4}, remaining : {reg5}"),
          
          #remaining enemy population has 10+remaining soldiers in enemy party
          (assign, ":remaining_enemy_population", ":total_enemy_population"),
          
          (assign, reg5, ":remaining_enemy_population"),
          (assign, reg6, ":total_enemy_morale_gain"),
          
          (set_fixed_point_multiplier, 100),
          (val_mul, ":remaining_enemy_population", 100),
          (store_sqrt, ":sqrt_remaining_enemy_population", ":remaining_enemy_population"),
          (val_div, ":sqrt_remaining_enemy_population", 100),
          (val_div, ":total_enemy_morale_gain", ":sqrt_remaining_enemy_population"),
          (val_div, ":total_enemy_morale_gain", 4),
          
          (try_begin),
            (eq, "$cheat_mode", 1),
            (assign, reg7, ":total_enemy_morale_gain"),
            (display_message, "str_total_enemy_morale_gain__reg6_last_total_enemy_morale_gain__reg7_remaining_enemy_population__reg5"),
          (try_end),
          
          (store_mul, ":party_morale_gain", ":total_enemy_morale_gain", ":main_enemy_party_population"),
          (val_div, ":party_morale_gain", ":total_enemy_population"),
          
          (try_begin),
            (party_is_active, "$g_enemy_party"),
            
            (call_script, "script_change_party_morale", "$g_enemy_party", ":party_morale_gain"),
            
            (party_get_num_attached_parties, ":num_attached_parties", "$g_enemy_party"),
            (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
              (party_get_attached_party_with_rank, ":attached_party", "$g_enemy_party", ":attached_party_rank"),
              (party_get_num_companion_stacks, ":num_stacks", ":attached_party"),
              (assign, ":party_population", 0),
              (try_for_range, ":i_stack", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":stack_troop", ":attached_party", ":i_stack"),
                (party_stack_get_size, ":stack_size", ":attached_party", ":i_stack"),
                (val_add, ":party_population", ":stack_size"),
              (try_end),
              #(store_div, ":party_ratio", ":total_enemy_population_multiplied_by_100", ":party_population"), #party ratio changes between 0..100, shows population ratio of that party among all enemy parties
              (store_mul, ":party_morale_gain", ":total_enemy_morale_gain", ":party_population"),
              (val_div, ":party_morale_gain", ":total_enemy_population"),
              (call_script, "script_change_party_morale", ":attached_party", ":party_morale_gain"),
            (try_end),
          (try_end),
        (try_end),
        
        #Add morale
        (assign, ":morale_gain", ":total_gain"),
        (val_div, ":morale_gain", ":num_player_party_shares"),#if there are lots of soldiers in my party there will be less morale increase.
        
        (try_begin),
          (eq, "$cheat_mode", 1),
          (assign, reg0, ":num_player_party_shares"),
          (assign, reg1, ":total_gain"),
          (display_message, "@{!}DEBUGS3 : num_player_party_shares:{reg0}, total_gain:{reg1}"),
        (try_end),
        
        (call_script, "script_change_player_party_morale", ":morale_gain"),
        
        (store_mul, ":killed_enemies_by_our_soldiers", ":died_enemy_population", "$g_strength_contribution_of_player"),
        (store_div, ":faction_morale_change", ":killed_enemies_by_our_soldiers", 8), #each 8 killed agent with any faction decreases morale of troops belong to that faction in our party by 1.
        (try_begin),
          (gt, ":faction_morale_change", 2000),
          (assign, ":faction_morale_change", 2000),
        (try_end),
        
        (try_begin), #here we give positive morale to our troops of with same faction of ally party with 2/3x multipication.
          (ge, "$g_ally_party", 0),
          
          (store_div, ":ally_faction_morale_change", ":faction_morale_change", 3), #2/3x multipication (less than normal)
          (val_mul, ":ally_faction_morale_change", 2),
          (store_faction_of_party, ":ally_faction", "$g_ally_party"),
          (faction_get_slot, ":faction_morale", ":ally_faction",  slot_faction_morale_of_player_troops),
          (val_add, ":faction_morale", ":ally_faction_morale_change"),
          (faction_set_slot, ":ally_faction",  slot_faction_morale_of_player_troops, ":faction_morale"),
        (try_end),
        
        (try_begin), #here we give positive morale to our troops of owner of rescued village's faction after saving village from bandits by x3 bonus.
          (neg|party_is_active, "$g_enemy_party"),
          (ge, "$current_town", 0),
          
          (val_mul, ":faction_morale_change", 2), #2x bonus (more than normal)
          (store_faction_of_party, ":ally_faction", "$current_town"),
          (faction_get_slot, ":faction_morale", ":ally_faction",  slot_faction_morale_of_player_troops),
          (val_add, ":faction_morale", ":faction_morale_change"),
          (faction_set_slot, ":ally_faction",  slot_faction_morale_of_player_troops, ":faction_morale"),
        (else_try),
          (party_is_active, "$g_enemy_party"),
          (assign, ":currently_in_rebellion", 0),
          (try_begin),
            (eq, "$players_kingdom", "fac_player_supporters_faction"),
            (neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
            (assign, ":currently_in_rebellion", 1),
          (try_end),
          (eq, ":currently_in_rebellion", 0),
          
          (store_div, ":faction_morale_change", ":faction_morale_change", 3), #2/3x multipication (less than normal)
          (val_mul, ":faction_morale_change", 2),
          (store_faction_of_party, ":enemy_faction", "$g_enemy_party"),
          (faction_get_slot, ":faction_morale", ":enemy_faction",  slot_faction_morale_of_player_troops),
          (val_sub, ":faction_morale", ":faction_morale_change"),
          (faction_set_slot, ":enemy_faction",  slot_faction_morale_of_player_troops, ":faction_morale"),
        (try_end),
        
    ]),
    
    #script_print_casualties_to_s0:
    # INPUT:
    # param1: Party_id, param2: 0 = use new line, 1 = use comma
    
    #OUTPUT:
    # string register 0.
    
    ("print_casualties_to_s0",
      [(store_script_param, ":party_no", 1),
        (store_script_param, ":use_comma", 2),
        (str_clear, s0),
        (assign, ":total_reported", 0),
        (assign, ":total_wounded", 0),
        (assign, ":total_killed", 0),
        (assign, ":total_routed", 0),
        (party_get_num_companion_stacks, ":num_stacks",":party_no"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop_id", ":party_no", ":i_stack"),
          (party_stack_get_size, ":stack_size", ":party_no", ":i_stack"),
          (party_stack_get_num_wounded, ":num_wounded", ":party_no", ":i_stack"),
          #get number of routed agent numbers
          (try_begin),
            (this_or_next|eq, ":party_no", "p_main_party"),
            (eq, ":party_no", "p_player_casualties"),
            (troop_get_slot, ":num_routed", ":stack_troop_id", slot_troop_player_routed_agents),
            (troop_set_slot, ":stack_troop_id", slot_troop_player_routed_agents, 0),
          (else_try),
            (party_get_attached_to, ":attached_to", ":party_no"),
            (this_or_next|eq, ":party_no", "p_ally_casualties"),
            (ge, ":attached_to", 0),
            (this_or_next|eq, ":party_no", "p_ally_casualties"),
            (eq, ":attached_to", "p_main_party"),
            (troop_get_slot, ":num_routed", ":stack_troop_id", slot_troop_ally_routed_agents),
            (troop_set_slot, ":stack_troop_id", slot_troop_ally_routed_agents, 0),
          (else_try),
            (troop_get_slot, ":num_routed", ":stack_troop_id", slot_troop_enemy_routed_agents),
            (troop_set_slot, ":stack_troop_id", slot_troop_enemy_routed_agents, 0),
          (try_end),
          (store_sub, ":num_killed", ":stack_size", ":num_wounded"),
          (val_sub, ":num_killed", ":num_routed"),
          (val_add, ":total_killed", ":num_killed"),
          (val_add, ":total_wounded", ":num_wounded"),
          (val_add, ":total_routed", ":num_routed"),
          (try_begin),
            (this_or_next|gt, ":num_killed", 0),
            (this_or_next|gt, ":num_wounded", 0),
            (gt, ":num_routed", 0),
            (store_add, reg3, ":num_killed", ":num_wounded"),
            (store_add, reg3, reg3, ":num_routed"),
            (str_store_troop_name_by_count, s1, ":stack_troop_id", reg3),
            (try_begin),
              (troop_is_hero, ":stack_troop_id"),
              (assign, reg3, 0),
            (try_end),
            (try_begin), #there are people who killed, wounded and routed.
              (gt, ":num_killed", 0),
              (gt, ":num_wounded", 0),
              (gt, ":num_routed", 0),
              (assign, reg4, ":num_killed"),
              (assign, reg5, ":num_wounded"),
              (assign, reg6, ":num_routed"),
              (str_store_string, s2, "str_reg4_killed_reg5_wounded_reg6_routed"),
            (else_try), #there are people who killed and routed.
              (gt, ":num_killed", 0),
              (gt, ":num_routed", 0),
              (assign, reg4, ":num_killed"),
              (assign, reg5, ":num_routed"),
              (str_store_string, s2, "str_reg4_killed_reg5_routed"),
            (else_try), #there are people who killed and wounded.
              (gt, ":num_killed", 0),
              (gt, ":num_wounded", 0),
              (assign, reg4, ":num_killed"),
              (assign, reg5, ":num_wounded"),
              (str_store_string, s2, "str_reg4_killed_reg5_wounded"),
            (else_try), #there are people who wounded and routed.
              (gt, ":num_wounded", 0),
              (gt, ":num_routed", 0),
              (assign, reg4, ":num_wounded"),
              (assign, reg5, ":num_routed"),
              (str_store_string, s2, "str_reg4_wounded_reg5_routed"),
            (else_try), #there are people who only killed.
              (gt, ":num_killed", 0),
              (assign, reg1, ":num_killed"),
              (str_store_string, s3, "@killed"),
              (str_store_string, s2, "str_reg1_blank_s3"),
            (else_try), #there are people who only wounded.
              (gt, ":num_wounded", 0),
              (assign, reg1, ":num_wounded"),
              (str_store_string, s3, "@wounded"),
              (str_store_string, s2, "str_reg1_blank_s3"),
            (else_try), #there are people who only routed.
              (assign, reg1, ":num_routed"),
              (str_store_string, s3, "str_routed"),
              (str_store_string, s2, "str_reg1_blank_s3"),
            (try_end),
            (try_begin),
              (eq, ":use_comma", 1),
              (try_begin),
                (eq, ":total_reported", 0),
                (str_store_string, s0, "@{!}{reg3?{reg3}:} {s1} ({s2})"),
              (else_try),
                (str_store_string, s0, "@{!}{s0}, {reg3?{reg3}:} {s1} ({s2})"),
              (try_end),
            (else_try),
              (str_store_string, s0, "@{!}{s0}^{reg3?{reg3}:} {s1} ({s2})"),
            (try_end),
            (val_add, ":total_reported", 1),
          (try_end),
        (try_end),
        (try_begin),
          (this_or_next|gt, ":total_killed", 0),
          (this_or_next|gt, ":total_wounded", 0),
          (gt, ":total_routed", 0),
          (store_add, ":total_agents", ":total_killed", ":total_wounded"),
          (val_add, ":total_agents", ":total_routed"),
          (assign, reg3, ":total_agents"),
          (try_begin),
            (gt, ":total_killed", 0),
            (gt, ":total_wounded", 0),
            (gt, ":total_routed", 0),
            (assign, reg4, ":total_killed"),
            (assign, reg5, ":total_wounded"),
            (assign, reg6, ":total_routed"),
            (str_store_string, s2, "str_reg4_killed_reg5_wounded_reg6_routed"),
          (else_try),
            (gt, ":total_killed", 0),
            (gt, ":total_routed", 0),
            (assign, reg4, ":total_killed"),
            (assign, reg5, ":total_routed"),
            (str_store_string, s2, "str_reg4_killed_reg5_routed"),
          (else_try),
            (gt, ":total_killed", 0),
            (gt, ":total_wounded", 0),
            (assign, reg4, ":total_killed"),
            (assign, reg5, ":total_wounded"),
            (str_store_string, s2, "str_reg4_killed_reg5_wounded"),
          (else_try),
            (gt, ":total_wounded", 0),
            (gt, ":total_routed", 0),
            (assign, reg4, ":total_wounded"),
            (assign, reg5, ":total_routed"),
            (str_store_string, s2, "str_reg4_wounded_reg5_routed"),
          (else_try),
            (gt, ":total_killed", 0),
            (str_store_string, s2, "@killed"),
          (else_try),
            (gt, ":total_wounded", 0),
            (str_store_string, s2, "@wounded"),
          (else_try),
            (str_store_string, s2, "str_routed"),
          (else_try),
          (try_end),
          (str_store_string, s0, "@{s0}^TOTAL: {reg3} ({s2})"),
        (else_try),
          (try_begin),
            (eq, ":use_comma", 1),
            (str_store_string, s0, "@None"),
          (else_try),
            (str_store_string, s0, "@^None"),
          (try_end),
        (try_end),
    ]),
    
    #script_write_fit_party_members_to_stack_selection
    # INPUT:
    # param1: party_no, exclude_leader
    #OUTPUT:
    # trp_stack_selection_amounts slots (slot 0 = number of stacks, 1 = number of men fit, 2..n = stack sizes (fit))
    # trp_stack_selection_ids slots (2..n = stack troops)
    ("write_fit_party_members_to_stack_selection",
      [
        (store_script_param, ":party_no", 1),
        (store_script_param, ":exclude_leader", 2),
        (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
        (assign, ":slot_index", 2),
        (assign, ":total_fit", 0),
        (try_for_range, ":stack_index", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", ":party_no", ":stack_index"),
          (assign, ":num_fit", 0),
          (try_begin),
            (troop_is_hero, ":stack_troop"),
            (try_begin),
              (neg|troop_is_wounded, ":stack_troop"),
              (this_or_next|eq, ":exclude_leader", 0),
              (neq, ":stack_index", 0),
              (assign, ":num_fit",1),
            (try_end),
          (else_try),
            (party_stack_get_size, ":num_fit", ":party_no", ":stack_index"),
            (party_stack_get_num_wounded, ":num_wounded", ":party_no", ":stack_index"),
            (val_sub, ":num_fit", ":num_wounded"),
          (try_end),
          (try_begin),
            (gt, ":num_fit", 0),
            (troop_set_slot, "trp_stack_selection_amounts", ":slot_index", ":num_fit"),
            (troop_set_slot, "trp_stack_selection_ids", ":slot_index", ":stack_troop"),
            (val_add, ":slot_index", 1),
          (try_end),
          (val_add, ":total_fit", ":num_fit"),
        (try_end),
        (val_sub, ":slot_index", 2),
        (troop_set_slot, "trp_stack_selection_amounts", 0, ":slot_index"),
        (troop_set_slot, "trp_stack_selection_amounts", 1, ":total_fit"),
    ]),
    
    #script_remove_fit_party_member_from_stack_selection
    # INPUT:
    # param1: slot_index
    #OUTPUT:
    # reg0 = troop_no
    # trp_stack_selection_amounts slots (slot 0 = number of stacks, 1 = number of men fit, 2..n = stack sizes (fit))
    # trp_stack_selection_ids slots (2..n = stack troops)
    ("remove_fit_party_member_from_stack_selection",
      [
        (store_script_param, ":slot_index", 1),
        (val_add, ":slot_index", 2),
        (troop_get_slot, ":amount", "trp_stack_selection_amounts", ":slot_index"),
        (troop_get_slot, ":troop_no", "trp_stack_selection_ids", ":slot_index"),
        (val_sub, ":amount", 1),
        (troop_set_slot, "trp_stack_selection_amounts", ":slot_index", ":amount"),
        (troop_get_slot, ":total_amount", "trp_stack_selection_amounts", 1),
        (val_sub, ":total_amount", 1),
        (troop_set_slot, "trp_stack_selection_amounts", 1, ":total_amount"),
        (try_begin),
          (le, ":amount", 0),
          (troop_get_slot, ":num_slots", "trp_stack_selection_amounts", 0),
          (store_add, ":end_cond", ":num_slots", 2),
          (store_add, ":begin_cond", ":slot_index", 1),
          (try_for_range, ":index", ":begin_cond", ":end_cond"),
            (store_sub, ":prev_index", ":index", 1),
            (troop_get_slot, ":value", "trp_stack_selection_amounts", ":index"),
            (troop_set_slot, "trp_stack_selection_amounts", ":prev_index", ":value"),
            (troop_get_slot, ":value", "trp_stack_selection_ids", ":index"),
            (troop_set_slot, "trp_stack_selection_ids", ":prev_index", ":value"),
          (try_end),
          (val_sub, ":num_slots", 1),
          (troop_set_slot, "trp_stack_selection_amounts", 0, ":num_slots"),
        (try_end),
        (assign, reg0, ":troop_no"),
    ]),
    
    #script_remove_random_fit_party_member_from_stack_selection
    # INPUT:
    # none
    #OUTPUT:
    # reg0 = troop_no
    # trp_stack_selection_amounts slots (slot 0 = number of stacks, 1 = number of men fit, 2..n = stack sizes (fit))
    # trp_stack_selection_ids slots (2..n = stack troops)
    ("remove_random_fit_party_member_from_stack_selection",
      [
        (troop_get_slot, ":total_amount", "trp_stack_selection_amounts", 1),
        (store_random_in_range, ":random_troop", 0, ":total_amount"),
        (troop_get_slot, ":num_slots", "trp_stack_selection_amounts", 0),
        (store_add, ":end_cond", ":num_slots", 2),
        (try_for_range, ":index", 2, ":end_cond"),
          (troop_get_slot, ":amount", "trp_stack_selection_amounts", ":index"),
          (val_sub, ":random_troop", ":amount"),
          (lt, ":random_troop", 0),
          (assign, ":end_cond", 0),
          (store_sub, ":slot_index", ":index", 2),
        (try_end),
        (call_script, "script_remove_fit_party_member_from_stack_selection", ":slot_index"),
    ]),
    
    
    #script_add_routed_party
    #INPUT: none
    #OUTPUT: none
    ("add_routed_party",
      [
        (party_get_num_companion_stacks, ":num_stacks", "p_routed_enemies"), #question, I changed (total_enemy_casualties) with (p_routed_enemies) because this is not prisoner in p_routed_enemies party.
        (assign, ":num_regulars", 0),
        (assign, ":deleted_stacks", 0),
        (try_for_range, ":stack_no", 0, ":num_stacks"),
          (store_sub, ":difference", ":num_stacks", ":stack_no"),
          (ge, ":difference", ":deleted_stacks"),
          (store_sub, ":stack_no_minus_deleted", ":stack_no", ":deleted_stacks"),
          (party_stack_get_troop_id, ":stack_troop", "p_routed_enemies", ":stack_no_minus_deleted"),
          (try_begin),
            (troop_is_hero, ":stack_troop"),
            (party_stack_get_size, ":stack_size", "p_routed_enemies", ":stack_no_minus_deleted"),
            (party_remove_members, "p_routed_enemies", ":stack_troop", 1),
            (try_begin),
              (le, ":stack_size", 1),
              (val_add, ":deleted_stacks", 1), #if deleted hero is the only one in his troop, now we have one less stacks
            (try_end),
          (else_try),
            (val_add, ":num_regulars", 1),
          (try_end),
        (try_end),
        
        #add new party to map if there is at least one routed agent. (new party name : routed_party, template : routed_warriors)
        (try_begin),
          (ge, ":num_regulars", 1),
          
          (set_spawn_radius, 2),
          (spawn_around_party, "p_main_party", "pt_routed_warriors"),
          (assign, ":routed_party", reg0),
          
          (party_set_slot, ":routed_party", slot_party_commander_party, -1), #we need this because 0 is player's party!
          
          (assign, ":max_routed_agents", 0),
          (assign, ":routed_party_faction", "fac_neutral"),
          (try_for_range, ":cur_faction", fac_kingdom_1, fac_kingdoms_end),
            (faction_get_slot, ":num_routed_agents_in_this_faction", ":cur_faction", slot_faction_num_routed_agents),
            (gt, ":num_routed_agents_in_this_faction", ":max_routed_agents"),
            (assign, ":max_routed_agents", ":num_routed_agents_in_this_faction"),
            (assign, ":routed_party_faction", ":cur_faction"),
          (try_end),
          
          (party_set_faction, ":routed_party", ":routed_party_faction"),
          
          (party_set_ai_behavior, ":routed_party", ai_bhvr_travel_to_party),
          
          (assign, ":minimum_distance", 1000000),
          (try_for_parties, ":party_no"),
            (party_is_active, ":party_no"),
            (party_get_slot, ":cur_party_type", ":party_no", slot_party_type),
            (this_or_next|eq, ":cur_party_type", spt_town),
            (eq, ":cur_party_type", spt_castle),
            (store_faction_of_party, ":cur_faction", ":party_no"),
            (this_or_next|eq, ":routed_party_faction", "fac_neutral"),
            (eq, ":cur_faction", ":routed_party_faction"),
            (party_get_position, pos1, ":party_no"),
            (store_distance_to_party_from_party, ":dist", ":party_no", "p_main_party"),
            (try_begin),
              (lt, ":dist", ":minimum_distance"),
              (assign, ":minimum_distance", ":dist"),
              (assign, ":nearest_ally_city", ":party_no"),
            (try_end),
          (try_end),
          
          (party_get_position, pos1, "p_main_party"), #store position information of main party in pos1
          (party_get_position, pos2, ":nearest_ally_city"), #store position information of target city in pos2
          
          (assign, ":minimum_distance", 1000000),
          (try_for_range, ":unused", 0, 10),
            (map_get_random_position_around_position, pos3, pos1, 2), #store position of found random position (possible placing position for new routed party) around battle position in pos3
            (get_distance_between_positions, ":dist", pos2, pos3), #store distance between found position and target city in ":dist".
            (try_begin),
              (lt, ":dist", ":minimum_distance"),
              (assign, ":minimum_distance", ":dist"),
              (copy_position, pos63, pos3),
            (try_end),
          (end_try),
          
          (party_set_position, ":routed_party", pos63),
          
          (party_set_ai_object, ":routed_party", ":nearest_ally_city"),
          (party_set_flags, ":routed_party", pf_default_behavior, 1),
          
          #adding party members of p_routed_enemies to routed_party
          (party_clear, ":routed_party"),
          (party_get_num_companion_stacks, ":num_stacks", "p_routed_enemies"), #question, I changed (total_enemy_casualties) with (p_routed_enemies) because this is not prisoner in p_routed_enemies party.
          (try_for_range, ":stack_no", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", "p_routed_enemies", ":stack_no"),
            (try_begin),
              (neg|troop_is_hero, ":stack_troop"), #do not add routed heroes to (new created) routed party for now.
              
              (party_stack_get_size, ":stack_size", "p_routed_enemies", ":stack_no"),
              (party_add_members, ":routed_party", ":stack_troop", ":stack_size"),
            (try_end),
          (try_end),
        (try_end),
    ]), #ozan
    
    
    #script_cf_training_ground_sub_routine_1_for_melee_details
    # INPUT:
    # value
    #OUTPUT:
    # none
    ("cf_training_ground_sub_routine_1_for_melee_details",
      [
        (store_script_param, ":value", 1),
        (ge, "$temp_3", ":value"),
        (val_add, ":value", 1),
        (troop_get_slot, ":troop_id", "trp_stack_selection_ids", ":value"),
        (str_store_troop_name, s0, ":troop_id"),
    ]),
    
    #script_training_ground_sub_routine_2_for_melee_details
    # INPUT:
    # value
    #OUTPUT:
    # none
    ("training_ground_sub_routine_2_for_melee_details",
      [
        (store_script_param, ":value", 1),
        (val_sub, ":value", 1),
        (try_begin),
          (lt, ":value", 0),
          (call_script, "script_remove_random_fit_party_member_from_stack_selection"),
        (else_try),
          (call_script, "script_remove_fit_party_member_from_stack_selection", ":value"),
        (try_end),
        (assign, ":troop_id", reg0),
        (store_sub, ":slot_index", "$temp_2", 1),
        (troop_set_slot, "trp_temp_array_a", ":slot_index", ":troop_id"),
        (try_begin),
          (eq, "$temp", "$temp_2"),
          (call_script, "script_start_training_at_training_ground", -1, "$temp"),
        (else_try),
          (val_add, "$temp_2", 1),
          (jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
        (try_end),
    ]),
    
    #script_cf_training_ground_sub_routine_for_training_result
    # INPUT:
    # arg1: troop_id, arg2: stack_no, arg3: troop_count, arg4: xp_ratio_to_add
    #OUTPUT:
    # none
    ("cf_training_ground_sub_routine_for_training_result",
      [
        (store_script_param, ":troop_id", 1),
        (store_script_param, ":stack_no", 2),
        (store_script_param, ":amount", 3),
        (store_script_param, ":xp_ratio_to_add", 4),
        
        (store_character_level, ":level", ":troop_id"),
        (store_add, ":level_added", ":level", 5),
        (store_mul, ":min_hardness", ":level_added", 3),
        (val_min, ":min_hardness", 100),
        (store_sub, ":hardness_dif", ":min_hardness", "$g_training_ground_training_hardness"),
        (val_max, ":hardness_dif", 0),
        (store_sub, ":hardness_dif", 100, ":hardness_dif"),
        (val_mul, ":hardness_dif", ":hardness_dif"),
        (val_div, ":hardness_dif", 10), # value over 1000
        ##     (assign, reg0, ":hardness_dif"),
        ##     (display_message, "@Hardness difference: {reg0}/1000"),
        (store_mul, ":xp_ratio_to_add_for_stack", ":xp_ratio_to_add", ":hardness_dif"),
        (val_div, ":xp_ratio_to_add_for_stack", 1000),
        (try_begin),
          (eq, ":troop_id", "trp_player"),
          (val_mul, ":xp_ratio_to_add_for_stack", 1),
        (else_try),
          (try_begin),
            (eq, "$g_mt_mode", ctm_melee),
            (try_begin),
              (this_or_next|troop_is_guarantee_ranged, ":troop_id"),
              (troop_is_guarantee_horse, ":troop_id"),
              (val_div, ":xp_ratio_to_add_for_stack", 4),
            (try_end),
          (else_try),
            (eq, "$g_mt_mode", ctm_mounted),
            (try_begin),
              (neg|troop_is_guarantee_horse, ":troop_id"),
              (assign, ":xp_ratio_to_add_for_stack", 0),
            (try_end),
          (else_try),
            (neg|troop_is_guarantee_ranged, ":troop_id"),
            (assign, ":xp_ratio_to_add_for_stack", 0),
          (try_end),
        (try_end),
        (val_add,  ":level", 1),
        (store_mul, ":xp_to_add", 100, ":level"),
        (val_mul, ":xp_to_add", ":amount"),
        (val_div, ":xp_to_add", 20),
        (val_mul, ":xp_to_add", ":xp_ratio_to_add_for_stack"),
        (val_div, ":xp_to_add", 1000),
        (store_mul, ":max_xp_to_add", ":xp_to_add", 3),
        (val_div, ":max_xp_to_add", 2),
        (store_div, ":min_xp_to_add", ":xp_to_add", 2),
        (store_random_in_range, ":random_xp_to_add", ":min_xp_to_add", ":max_xp_to_add"),
        (gt, ":random_xp_to_add", 0),
        (try_begin),
          (troop_is_hero, ":troop_id"),
          (add_xp_to_troop, ":random_xp_to_add", ":troop_id"),
          (store_div, ":proficiency_to_add", ":random_xp_to_add", 50),
          (try_begin),
            (gt, ":proficiency_to_add", 0),
            (troop_raise_proficiency, ":troop_id", "$g_training_ground_used_weapon_proficiency", ":proficiency_to_add"),
          (try_end),
        (else_try),
          (party_add_xp_to_stack, "p_main_party", ":stack_no", ":random_xp_to_add"),
        (try_end),
        (assign, reg0, ":random_xp_to_add"),
    ]),
    
    
    ##  #script_cf_print_troop_name_with_stack_index_to_s0
    ##  # INPUT:
    ##  # param1: stack_index
    ##
    ##  #OUTPUT:
    ##  # string register 0.
    ##  ("cf_print_troop_name_with_stack_index_to_s0",
    ##   [
    ##     (store_script_param_1, ":stack_index"),
    ##     (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
    ##     (lt, ":stack_index", ":num_stacks"),
    ##     (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_index"),
    ##     (str_store_troop_name, s0, ":stack_troop"),
    ##    ]),
    
    #script_print_troop_owned_centers_in_numbers_to_s0
    # INPUT:
    # param1: troop_no
    #OUTPUT:
    # string register 0.
    ("print_troop_owned_centers_in_numbers_to_s0",
      [
        (store_script_param_1, ":troop_no"),
        (str_store_string, s0, "@nothing"),
        (assign, ":owned_towns", 0),
        (assign, ":owned_castles", 0),
        (assign, ":owned_villages", 0),
        (try_for_range_backwards, ":cur_center", centers_begin, centers_end),
          (party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
          (try_begin),
            (party_slot_eq, ":cur_center", slot_party_type, spt_town),
            (val_add, ":owned_towns", 1),
          (else_try),
            (party_slot_eq, ":cur_center", slot_party_type, spt_castle),
            (val_add, ":owned_castles", 1),
          (else_try),
            (val_add, ":owned_villages", 1),
          (try_end),
        (try_end),
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
    
    #script_get_random_melee_training_weapon
    # INPUT: none
    # OUTPUT: reg0 = weapon_1, reg1 = weapon_2
    ("get_random_melee_training_weapon",
      [
        (assign, ":weapon_1", -1),
        (assign, ":weapon_2", -1),
        (store_random_in_range, ":random_no", 0, 3),
        (try_begin),
          (eq, ":random_no", 0),
          (assign, ":weapon_1", "itm_practice_staff"),
        (else_try),
          (eq, ":random_no", 1),
          (assign, ":weapon_1", "itm_practice_sword"),
          (assign, ":weapon_2", "itm_practice_shield"),
        (else_try),
          (assign, ":weapon_1", "itm_practice_sword_heavy"),
        (try_end),
        (assign, reg0, ":weapon_1"),
        (assign, reg1, ":weapon_2"),
    ]),
    
    #script_start_training_at_training_ground
    # INPUT:
    # param1: training_weapon_type, param2: training_param
    ("start_training_at_training_ground",
      [
        (val_add, "$g_training_ground_training_count", 1),
        (store_script_param, ":mission_weapon_type", 1),
        (store_script_param, ":training_param", 2),
        
        (set_jump_mission, "mt_training_ground_training"),
        
        (assign, ":training_default_weapon_1", -1),
        (assign, ":training_default_weapon_2", -1),
        (assign, ":training_default_weapon_3", -1),
        (assign, "$scene_num_total_gourds_destroyed", 0),
        (try_begin),
          (eq, ":mission_weapon_type", itp_type_bow),
          (assign, "$g_training_ground_used_weapon_proficiency", wpt_archery),
          (assign, ":training_default_weapon_1", "itm_practice_bow"),
          (try_begin),
            (eq, "$g_mt_mode", ctm_mounted),
            (assign, ":training_default_weapon_2", "itm_practice_arrows_100_amount"),
          (else_try),
            (assign, ":training_default_weapon_2", "itm_practice_arrows_10_amount"),
          (try_end),
        (else_try),
          (eq, ":mission_weapon_type", itp_type_crossbow),
          (assign, "$g_training_ground_used_weapon_proficiency", wpt_crossbow),
          (assign, ":training_default_weapon_1", "itm_practice_crossbow"),
          (assign, ":training_default_weapon_2", "itm_practice_bolts_9_amount"),
        (else_try),
          (eq, ":mission_weapon_type", itp_type_thrown),
          (assign, "$g_training_ground_used_weapon_proficiency", wpt_throwing),
          (try_begin),
            (eq, "$g_mt_mode", ctm_mounted),
            (assign, ":training_default_weapon_2", "itm_practice_throwing_daggers_100_amount"),
          (else_try),
            (assign, ":training_default_weapon_2", "itm_practice_throwing_daggers"),
          (try_end),
        (else_try),
          (eq, ":mission_weapon_type", itp_type_one_handed_wpn),
          (assign, "$g_training_ground_used_weapon_proficiency", wpt_one_handed_weapon),
          (assign, ":training_default_weapon_1", "itm_practice_sword"),
        (else_try),
          (eq, ":mission_weapon_type", itp_type_polearm),
          (assign, "$g_training_ground_used_weapon_proficiency", wpt_polearm),
          (assign, ":training_default_weapon_1", "itm_practice_lance"),
        (else_try),
          #weapon_type comes as -1 when melee training is selected
          (assign, "$g_training_ground_used_weapon_proficiency", wpt_one_handed_weapon),
          (call_script, "script_get_random_melee_training_weapon"),
          (assign, ":training_default_weapon_1", reg0),
          (assign, ":training_default_weapon_2", reg1),
        (try_end),
        
        ##     (assign, "$g_training_ground_training_troop_stack_index", ":stack_index"),
        (try_begin),
          (eq, "$g_mt_mode", ctm_mounted),
          (assign, ":training_default_weapon_3", "itm_practice_horse"),
          (store_add, "$g_training_ground_training_scene", "scn_training_ground_horse_track_1", "$g_encountered_party"),
          (val_sub, "$g_training_ground_training_scene", training_grounds_begin),
        (else_try),
          (store_add, "$g_training_ground_training_scene", "scn_training_ground_ranged_melee_1", "$g_encountered_party"),
          (val_sub, "$g_training_ground_training_scene", training_grounds_begin),
        (try_end),
        
        (modify_visitors_at_site, "$g_training_ground_training_scene"),
        (reset_visitors),
        (set_visitor, 0, "trp_player"),
        
        (assign, ":selected_weapon", -1),
        (try_for_range, ":cur_slot", 0, 4),#equipment slots
          (troop_get_inventory_slot, ":cur_item", "trp_player", ":cur_slot"),
          (ge, ":cur_item", 0),
          (item_get_type, ":item_type", ":cur_item"),
          (try_begin),
            (eq, ":item_type", ":mission_weapon_type"),
            (eq, ":selected_weapon", -1),
            (assign, ":selected_weapon", ":cur_item"),
          (try_end),
        (try_end),
        (mission_tpl_entry_clear_override_items, "mt_training_ground_training", 0),
        (mission_tpl_entry_add_override_item, "mt_training_ground_training", 0, "itm_practice_boots"),
        (try_begin),
          (ge, ":training_default_weapon_1", 0),
          (try_begin),
            (ge, ":selected_weapon", 0),
            (mission_tpl_entry_add_override_item, "mt_training_ground_training", 0, ":selected_weapon"),
          (else_try),
            (mission_tpl_entry_add_override_item, "mt_training_ground_training", 0, ":training_default_weapon_1"),
          (try_end),
        (try_end),
        (try_begin),
          (ge, ":training_default_weapon_2", 0),
          (mission_tpl_entry_add_override_item, "mt_training_ground_training", 0, ":training_default_weapon_2"),
        (try_end),
        (try_begin),
          (ge, ":training_default_weapon_3", 0),
          (mission_tpl_entry_add_override_item, "mt_training_ground_training", 0, ":training_default_weapon_3"),
        (try_end),
        
        (assign, ":cur_visitor_point", 5),
        (troop_get_slot, ":num_fit", "trp_stack_selection_amounts", 1),
        (store_add, ":end_cond", 5, ":num_fit"),
        (val_min, ":end_cond", 13),
        (try_for_range, ":cur_visitor_point", 5, ":end_cond"),
          (call_script, "script_remove_random_fit_party_member_from_stack_selection"),
          (set_visitor, ":cur_visitor_point", reg0),
          (val_add, ":cur_visitor_point", 1),
        (try_end),
        (try_begin),
          (eq, "$g_mt_mode", ctm_melee),
          (assign, ":total_difficulty", 0),
          (try_for_range, ":i", 0, ":training_param"),
            (troop_get_slot, ":cur_troop", "trp_temp_array_a", ":i"),
            (store_add, ":cur_entry_point", ":i", 1),
            (set_visitor, ":cur_entry_point", ":cur_troop"),
            (mission_tpl_entry_clear_override_items, "mt_training_ground_training", ":cur_entry_point"),
            (mission_tpl_entry_add_override_item, "mt_training_ground_training", ":cur_entry_point", "itm_practice_boots"),
            (call_script, "script_get_random_melee_training_weapon"),
            (mission_tpl_entry_add_override_item, "mt_training_ground_training", ":cur_entry_point", reg0),
            (try_begin),
              (ge, reg1, 0),
              (mission_tpl_entry_add_override_item, "mt_training_ground_training", ":cur_entry_point", reg1),
            (try_end),
            (store_character_level, ":cur_troop_level", ":cur_troop"),
            (val_add, ":cur_troop_level", 10),
            (val_mul, ":cur_troop_level", ":cur_troop_level"),
            (val_add, ":total_difficulty", ":cur_troop_level"),
          (try_end),
          
          (assign, "$g_training_ground_training_num_enemies", ":training_param"),
          (assign, "$g_training_ground_training_hardness",  ":total_difficulty"),
          (store_add, ":number_multiplier", "$g_training_ground_training_num_enemies", 4),
          (val_mul, "$g_training_ground_training_hardness", ":number_multiplier"),
          (val_div, "$g_training_ground_training_hardness", 2400),
          (str_store_string, s0, "@Your opponents are ready for the fight."),
        (else_try),
          (eq, "$g_mt_mode", ctm_mounted),
          (try_begin),
            (eq, ":mission_weapon_type", itp_type_bow),
            (assign, "$g_training_ground_training_hardness", 350),
            (assign, "$g_training_ground_training_num_gourds_to_destroy", 30),
          (else_try),
            (eq, ":mission_weapon_type", itp_type_thrown),
            (assign, "$g_training_ground_training_hardness", 400),
            (assign, "$g_training_ground_training_num_gourds_to_destroy", 30),
          (else_try),
            (eq, ":mission_weapon_type", itp_type_one_handed_wpn),
            (assign, "$g_training_ground_training_hardness", 200),
            (assign, "$g_training_ground_training_num_gourds_to_destroy", 45),
          (else_try),
            (eq, ":mission_weapon_type", itp_type_polearm),
            (assign, "$g_training_ground_training_hardness", 280),
            (assign, "$g_training_ground_training_num_gourds_to_destroy", 35),
          (try_end),
          (str_store_string, s0, "@Try to destroy as many targets as you can. You have two and a half minutes to clear the track."),
        (else_try),
          (eq, "$g_mt_mode", ctm_ranged),
          (store_mul, "$g_training_ground_ranged_distance", ":training_param", 100),
          (assign, ":hardness_modifier", ":training_param"),
          (val_mul, ":hardness_modifier", ":hardness_modifier"),
          (try_begin),
            (eq, ":mission_weapon_type", itp_type_bow),
            (val_mul, ":hardness_modifier", 3),
            (val_div, ":hardness_modifier", 2),
          (else_try),
            (eq, ":mission_weapon_type", itp_type_thrown),
            (val_mul, ":hardness_modifier", 5),
            (val_div, ":hardness_modifier", 2),
            (val_mul, ":hardness_modifier", ":training_param"),
            (val_div, ":hardness_modifier", 2),
          (try_end),
          (store_mul, "$g_training_ground_training_hardness", 100, ":hardness_modifier"),
          (val_div, "$g_training_ground_training_hardness", 6000),
          (str_store_string, s0, "@Stay behind the line on the ground and shoot the targets. Try not to waste any shots."),
        (try_end),
        (jump_to_menu, "mnu_training_ground_description"),
    ]),
    
    
    #script_print_party_to_s0:
    # INPUT:
    # param1: Party-id
    
    #OUTPUT:
    # string register 0.
    
    ##  ("print_party_to_s0",
    ##    [
    ##      (store_script_param_1, ":party"), #Party_id
    ##      (party_get_num_companion_stacks, ":num_stacks",":party"),
    ##      (str_store_string, s50, "str_none"),
    ##      (try_for_range, ":i_stack", 0, ":num_stacks"),
    ##        (party_stack_get_troop_id,     ":stack_troop",":party",":i_stack"),
    ##        (party_stack_get_size,         ":stack_size",":party",":i_stack"),
    ##        (str_store_troop_name_by_count, s61, ":stack_troop", ":stack_size"),
    ##        (try_begin),
    ##          (troop_is_hero, ":stack_troop"),
    ##          (str_store_string_reg, s51, s61),
    ##        (else_try),
    ##          (assign, reg60, ":stack_size"),
    ##          (str_store_string, s63, "str_reg60_s61"),
    ##        (try_end),
    ##        (try_begin),
    ##          (eq, ":i_stack", 0),
    ##          (str_store_string_reg, s50, s51),
    ##        (else_try),
    ##          (str_store_string, s50, "str_s50_comma_s51"),
    ##        (try_end),
    ##      (try_end),
    ##      (str_store_string_reg, s0, s50),
    ##  ]),
    
    
    
    #script_party_count_fit_regulars:
    # Returns the number of unwounded regular companions in a party
    # INPUT:
    # param1: Party-id
    
    ("party_count_fit_regulars",
      [
        (store_script_param_1, ":party"), #Party_id
        (party_get_num_companion_stacks, ":num_stacks", ":party"),
        (assign, reg0, 0),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop", ":party", ":i_stack"),
          (neg|troop_is_hero, ":stack_troop"),
          (party_stack_get_size, ":stack_size",":party",":i_stack"),
          (party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
          (val_sub, ":stack_size", ":num_wounded"),
          (val_add, reg0, ":stack_size"),
        (try_end),
    ]),
    
    
    #script_party_count_fit_for_battle:
    # Returns the number of unwounded companions in a party
    # INPUT:
    # param1: Party-id
    # OUTPUT: reg0 = result
    ("party_count_fit_for_battle",
      [
        (store_script_param_1, ":party"), #Party_id
        (party_get_num_companion_stacks, ":num_stacks",":party"),
        (assign, reg0, 0),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop",":party",":i_stack"),
          (assign, ":num_fit",0),
          (try_begin),
            (troop_is_hero, ":stack_troop"),
            (try_begin),
              (neg|troop_is_wounded, ":stack_troop"),
              (assign, ":num_fit", 1),
            (try_end),
          (else_try),
            (party_stack_get_size, ":num_fit",":party",":i_stack"),
            (party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
            (val_sub, ":num_fit", ":num_wounded"),
          (try_end),
          (val_add, reg0, ":num_fit"),
        (try_end),
    ]),
    
    
    #script_party_count_members_with_full_health
    # Returns the number of unwounded regulars, and heroes other than player with 100% hitpoints in a party
    # INPUT:
    # param1: Party-id
    # OUTPUT: reg0 = result
	  ("party_count_members_with_full_health",
		[
		  (store_script_param_1, ":party"), #Party_id
		  (party_get_num_companion_stacks, ":num_stacks",":party"),
		  (assign, reg0, 0),
		  (try_for_range, ":i_stack", 0, ":num_stacks"),
			(party_stack_get_troop_id, ":stack_troop",":party",":i_stack"),
			(neq, ":stack_troop", "trp_player"),
			(assign, ":num_fit",0),
			(try_begin),
			  (troop_is_hero, ":stack_troop"),
			  (store_troop_health, ":troop_hp", ":stack_troop"),
			  (try_begin),
				(ge, ":troop_hp", 80),
				(assign, ":num_fit",1),
			  (try_end),
			(else_try),
			  (party_stack_get_size, ":num_fit",":party",":i_stack"),
			  (party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
			  (val_sub, ":num_fit", ":num_wounded"),
			  (val_max, ":num_fit", 0),
			(try_end),
			(val_add, reg0, ":num_fit"),
		  (try_end),
	  ]),
    
    
    ##  ("get_fit_stack_with_rank",
    ##    [
    ##      (store_script_param_1, ":party"), #Party_id
    ##      (store_script_param_2, ":rank"), #Rank
    ##      (party_get_num_companion_stacks, ":num_stacks",":party"),
    ##      (assign, reg0, -1),
    ##      (assign, ":num_total", 0),
    ##      (try_for_range, ":i_stack", 0, ":num_stacks"),
    ##        (eq, reg(0), -1), #continue only if we haven't found the result yet.
    ##        (party_stack_get_troop_id,     ":stack_troop",":party",":i_stack"),
    ##        (assign, ":num_fit",0),
    ##        (try_begin),
    ##          (troop_is_hero, ":stack_troop"),
    ##          (store_troop_health, ":troop_hp", ":stack_troop"),
    ##          (try_begin),
    ##            (ge,  ":troop_hp", 20),
    ##            (assign, ":num_fit",1),
    ##          (try_end),
    ##        (else_try),
    ##          (party_stack_get_size,         ":num_fit",":party",":i_stack"),
    ##          (party_stack_get_num_wounded, ":num_wounded",":party",":i_stack"),
    ##          (val_sub, ":num_fit", ":num_wounded"),
    ##        (try_end),
    ##        (val_add, ":num_total", ":num_fit"),
    ##        (try_begin),
    ##          (lt, ":rank", ":num_total"),
    ##          (assign, reg(0), ":i_stack"),
    ##        (try_end),
    ##      (try_end),
    ##  ]),
    
    #script_get_stack_with_rank:
    # Returns the stack no, containing unwounded regular companions with rank rank.
    # INPUT:
    # param1: Party-id
    # param2: rank
    
    ("get_stack_with_rank",
      [
        (store_script_param_1, ":party"), #Party_id
        (store_script_param_2, ":rank"), #Rank
        (party_get_num_companion_stacks, ":num_stacks",":party"),
        (assign, reg(0), -1),
        (assign, ":num_total", 0),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (eq, reg(0), -1), #continue only if we haven't found the result yet.
          (party_stack_get_troop_id,     ":stack_troop",":party",":i_stack"),
          (neg|troop_is_hero, ":stack_troop"),
          (party_stack_get_size,         ":stack_size",":party",":i_stack"),
          (party_stack_get_num_wounded,  ":num_wounded",":party",":i_stack"),
          (val_sub, ":stack_size", ":num_wounded"),
          (val_add, ":num_total", ":stack_size"),
          (try_begin),
            (lt, ":rank", ":num_total"),
            (assign, reg(0), ":i_stack"),
          (try_end),
        (try_end),
    ]),
    
    #script_inflict_casualties_to_party:
    # INPUT:
    # param1: Party-id
    # param2: number of rounds
    
    #OUTPUT:
    # This script doesn't return a value but populates the parties p_temp_wounded and p_temp_killed with the wounded and killed.
    #Example:
    #  (script_inflict_casualties_to_party, "_p_main_party" ,50),
    #  Simulate 50 rounds of casualties to main_party.
    
    ("inflict_casualties_to_party",
      [
        (party_clear, "p_temp_casualties"),
        (store_script_param_1, ":party"), #Party_id
        (call_script, "script_party_count_fit_regulars", ":party"),
        (assign, ":num_fit", reg(0)), #reg(47) = number of fit regulars.
        (store_script_param_2, ":num_attack_rounds"), #number of attacks
        (try_for_range, ":unused", 0, ":num_attack_rounds"),
          (gt, ":num_fit", 0),
          (store_random_in_range, ":attacked_troop_rank", 0 , ":num_fit"), #attack troop with rank reg(46)
          (assign, reg1, ":attacked_troop_rank"),
          (call_script, "script_get_stack_with_rank", ":party", ":attacked_troop_rank"),
          (assign, ":attacked_stack", reg(0)), #reg(53) = stack no to attack.
          (party_stack_get_troop_id,     ":attacked_troop",":party",":attacked_stack"),
          (store_character_level, ":troop_toughness", ":attacked_troop"),
          (val_add, ":troop_toughness", 5),  #troop-toughness = level + 5
#TEMPERED#     MAKE HARDER TO KILL HIGHER LEVEL TROOPS IN SIMULATED BATTLE 
		(store_div,":level_bonus",":troop_toughness",5),
		(val_mul,":level_bonus",10),
		(val_add,":troop_toughness",":level_bonus"),
#TEMPERED END CHANGES
          (assign, ":casualty_chance", 10000),
          (val_div, ":casualty_chance", ":troop_toughness"), #dying chance
          (try_begin),
            (store_random_in_range, ":rand_num", 0 ,10000),
            (lt, ":rand_num", ":casualty_chance"), #check chance to be a casualty
            (store_random_in_range, ":rand_num2", 0, 2), #check if this troop will be wounded or killed
            (try_begin),
              (troop_is_hero,":attacked_troop"), #currently troop can't be a hero, but no harm in keeping this.
              (store_troop_health, ":troop_hp",":attacked_troop"),
              (val_sub, ":troop_hp", 45),
              (val_max, ":troop_hp", 1),
              (troop_set_health, ":attacked_troop", ":troop_hp"),
            (else_try),
              (lt, ":rand_num2", 1), #wounded
              (party_add_members, "p_temp_casualties", ":attacked_troop", 1),
              (party_wound_members, "p_temp_casualties", ":attacked_troop", 1),
              (party_wound_members, ":party", ":attacked_troop", 1),
            (else_try), #killed
              (party_add_members, "p_temp_casualties", ":attacked_troop", 1),
              (party_remove_members, ":party", ":attacked_troop", 1),
            (try_end),
            (val_sub, ":num_fit", 1), #adjust number of fit regulars.
          (try_end),
        (try_end),
    ]),
    
    
    #script_move_members_with_ratio:
    # INPUT:
    # param1: Source Party-id
    # param2: Target Party-id
    # pin_number = ratio of members to move, multiplied by 1000
    
    #OUTPUT:
    # This script doesn't return a value but moves some of the members of source party to target party according to the given ratio.
    ("move_members_with_ratio",
      [
        (store_script_param_1, ":source_party"), #Source Party_id
        (store_script_param_2, ":target_party"), #Target Party_id
        (party_get_num_prisoner_stacks, ":num_stacks",":source_party"),
        (try_for_range_backwards, ":stack_no", 0, ":num_stacks"),
          (party_prisoner_stack_get_troop_id,     ":stack_troop",":source_party",":stack_no"),
          (party_prisoner_stack_get_size,    ":stack_size",":source_party",":stack_no"),
          (store_mul, ":number_to_move",":stack_size","$pin_number"),
          (val_div, ":number_to_move", 1000),
          (party_remove_prisoners, ":source_party", ":stack_troop", ":number_to_move"),
          (assign, ":number_moved", reg0),
          (party_add_prisoners, ":target_party", ":stack_troop", ":number_moved"),
        (try_end),
        (party_get_num_companion_stacks, ":num_stacks",":source_party"),
        (try_for_range_backwards, ":stack_no", 0, ":num_stacks"),
          (party_stack_get_troop_id,     ":stack_troop",":source_party",":stack_no"),
          (party_stack_get_size,    ":stack_size",":source_party",":stack_no"),
          (store_mul, ":number_to_move",":stack_size","$pin_number"),
          (val_div, ":number_to_move", 1000),
          (party_remove_members, ":source_party", ":stack_troop", ":number_to_move"),
          (assign, ":number_moved", reg0),
          (party_add_members, ":target_party", ":stack_troop", ":number_moved"),
        (try_end),
    ]),
    
    
    # script_count_parties_of_faction_and_party_type:
    # counts number of active parties with a template and faction.
    # Input: arg1 = faction_no, arg2 = party_type
    # Output: reg0 = count
    
    ("count_parties_of_faction_and_party_type",
      [
        (store_script_param_1, ":faction_no"),
        (store_script_param_2, ":party_type"),
        (assign, reg0, 0),
        (try_for_parties, ":party_no"),
          (party_is_active, ":party_no"),
          (party_get_slot, ":cur_party_type", ":party_no", slot_party_type),
          (store_faction_of_party, ":cur_faction", ":party_no"),
          (eq, ":cur_party_type", ":party_type"),
          (eq, ":cur_faction", ":faction_no"),
          (val_add, reg0, 1),
        (try_end),
    ]),
    
    # script_faction_get_number_of_armies
    # Input: arg1 = faction_no
    # Output: reg0 = number_of_armies
    ("faction_get_number_of_armies",
    [
		  (store_script_param_1, ":faction_no"),
		  (assign, ":num_armies", 0),
		  ##diplomacy start+ support for promoted kingdom ladies
		  (try_for_range, ":troop_no", heroes_begin, heroes_end),#<- changed from active_npcs to heroes
		  ##diplomacy end+
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (store_troop_faction, ":hero_faction_no", ":troop_no"),
          (eq, ":hero_faction_no", ":faction_no"),
          (troop_get_slot, ":hero_party", ":troop_no", slot_troop_leaded_party),
          (ge, ":hero_party", 0),
          (party_is_active, ":hero_party"),
          (call_script, "script_party_count_fit_regulars", ":hero_party"),
          (assign, ":party_size", reg0),
          (call_script, "script_party_get_ideal_size", ":hero_party"),
          (assign, ":ideal_size", reg0),
          (val_mul, ":ideal_size", 60),
          (val_div, ":ideal_size", 100),
          (gt, ":party_size", ":ideal_size"),
          (val_add, ":num_armies", 1),
        (try_end),
        (assign, reg0, ":num_armies"),
    ]),
    
    
    # script_faction_recalculate_strength
    # Input: arg1 = faction_no
    # Output: reg0 = strength
    ("faction_recalculate_strength",
      [
        (store_script_param_1, ":faction_no"),
        
        (call_script, "script_faction_get_number_of_armies", ":faction_no"),
        (assign, ":num_armies", reg0),
        (assign, ":num_castles", 0),
        (assign, ":num_towns", 0),
        
        (try_for_range, ":center_no", centers_begin, centers_end),
          (store_faction_of_party, ":center_faction", ":center_no"),
          (eq, ":center_faction", ":faction_no"),
          (try_begin),
            (party_slot_eq, ":center_no", slot_party_type, spt_castle),
            (val_add, ":num_castles", 1),
          (else_try),
            (party_slot_eq, ":center_no", slot_party_type, spt_town),
            (val_add, ":num_towns", 1),
          (try_end),
        (try_end),
        
        (faction_set_slot, ":faction_no", slot_faction_num_armies, ":num_armies"),
        (faction_set_slot, ":faction_no", slot_faction_num_castles, ":num_castles"),
        (faction_set_slot, ":faction_no", slot_faction_num_towns, ":num_towns"),
        
    ]),
    
    #script_select_random_town:
    # This script selects a random town in range [towns_begin, towns_end)
    # INPUTS:
    # none
    
    #OUTPUT:
    # reg0: id of the selected random town
    ##  ("select_random_town",
    ##    [
    ##      (assign, ":num_towns", towns_end),
    ##      (val_sub,":num_towns", towns_begin),
    ##      (store_random, ":random_town", ":num_towns"),
    ##      (val_add,":random_town", towns_begin),
    ##      (assign, reg0, ":random_town"),
    ##  ]),
    
    #  ("select_random_spawn_point",
    #    [
    #      (assign, reg(20), spawn_points_end),
    #      (val_sub,reg(20), spawn_points_begin),
    #      (store_random, reg(21), reg(20)),
    #      (val_add,reg(21), spawn_points_begin),
    #      (assign, "$pout_town", reg(21)),
    # ]),
    
    #script_cf_select_random_town_with_faction:
    # This script selects a random town in range [towns_begin, towns_end)
    # such that faction of the town is equal to given_faction
    # INPUT:
    # arg1 = faction_no
    
    #OUTPUT:
    # This script may return false if there is no matching town.
    # reg0 = town_no
    ("cf_select_random_town_with_faction",
      [
        (store_script_param_1, ":faction_no"),
        (assign, ":result", -1),
        # First count num matching spawn points
        (assign, ":no_towns", 0),
        (try_for_range,":cur_town", towns_begin, towns_end),
          (store_faction_of_party, ":cur_faction", ":cur_town"),
          (eq, ":cur_faction", ":faction_no"),
          (val_add, ":no_towns", 1),
        (try_end),
        (gt, ":no_towns", 0), #Fail if there are no towns
        (store_random_in_range, ":random_town", 0, ":no_towns"),
        (assign, ":no_towns", 0),
        (try_for_range,":cur_town", towns_begin, towns_end),
          (eq, ":result", -1),
          (store_faction_of_party, ":cur_faction", ":cur_town"),
          (eq, ":cur_faction", ":faction_no"),
          (val_add, ":no_towns", 1),
          (gt, ":no_towns", ":random_town"),
          (assign, ":result", ":cur_town"),
        (try_end),
        (assign, reg0, ":result"),
    ]),
    
    #script_cf_select_random_village_with_faction:
    # This script selects a random village in range [villages_begin, villages_end)
    # such that faction of the village is equal to given_faction
    # INPUT:
    # arg1 = faction_no
    
    #OUTPUT:
    # This script may return false if there is no matching village.
    # reg0 = village_no
    ("cf_select_random_village_with_faction",
      [
        (store_script_param_1, ":faction_no"),
        (assign, ":result", -1),
        # First count num matching spawn points
        (assign, ":no_villages", 0),
        (try_for_range,":cur_village", villages_begin, villages_end),
          (store_faction_of_party, ":cur_faction", ":cur_village"),
          (eq, ":cur_faction", ":faction_no"),
          (val_add, ":no_villages", 1),
        (try_end),
        (gt, ":no_villages", 0), #Fail if there are no villages
        (store_random_in_range, ":random_village", 0, ":no_villages"),
        (assign, ":no_villages", 0),
        (try_for_range,":cur_village", villages_begin, villages_end),
          (eq, ":result", -1),
          (store_faction_of_party, ":cur_faction", ":cur_village"),
          (eq, ":cur_faction", ":faction_no"),
          (val_add, ":no_villages", 1),
          (gt, ":no_villages", ":random_village"),
          (assign, ":result", ":cur_village"),
        (try_end),
        (assign, reg0, ":result"),
    ]),
    
    
    #script_cf_select_random_walled_center_with_faction:
    # This script selects a random center in range [centers_begin, centers_end)
    # such that faction of the town is equal to given_faction
    # INPUT:
    # arg1 = faction_no
    # arg2 = preferred_center_no
    
    #OUTPUT:
    # This script may return false if there is no matching town.
    # reg0 = town_no (Can fail)
    ("cf_select_random_walled_center_with_faction",
      [
        (store_script_param, ":faction_no", 1),
        (store_script_param, ":preferred_center_no", 2),
        (assign, ":result", -1),
        # First count num matching spawn points
        (assign, ":no_centers", 0),
        (try_for_range,":cur_center", walled_centers_begin, walled_centers_end),
          (store_faction_of_party, ":cur_faction", ":cur_center"),
          (eq, ":cur_faction", ":faction_no"),
          (val_add, ":no_centers", 1),
          (eq, ":cur_center", ":preferred_center_no"),
          (val_add, ":no_centers", 99),
        (try_end),
        (gt, ":no_centers", 0), #Fail if there are no centers
        (store_random_in_range, ":random_center", 0, ":no_centers"),
        (try_for_range,":cur_center", walled_centers_begin, walled_centers_end),
          (eq, ":result", -1),
          (store_faction_of_party, ":cur_faction", ":cur_center"),
          (eq, ":cur_faction", ":faction_no"),
          (val_sub, ":random_center", 1),
          (try_begin),
            (eq, ":cur_center", ":preferred_center_no"),
            (val_sub, ":random_center", 99),
          (try_end),
          (lt, ":random_center", 0),
          (assign, ":result", ":cur_center"),
        (try_end),
        (assign, reg0, ":result"),
    ]),
    
    
    #script_cf_select_random_walled_center_with_faction_and_owner_priority_no_siege:
    # INPUT:
    # arg1 = faction_no
    # arg2 = owner_troop_no
    #OUTPUT:
    # This script may return false if there is no matching town.
    # reg0 = center_no (Can fail)
    ("cf_select_random_walled_center_with_faction_and_owner_priority_no_siege",
      [
        (store_script_param, ":faction_no", 1),
        (store_script_param, ":troop_no", 2),
        (assign, ":result", -1),
        (assign, ":no_centers", 0),
        
        (call_script, "script_lord_get_home_center", ":troop_no"),
        (assign, ":home_center", reg0),
        
        (try_for_range,":cur_center", walled_centers_begin, walled_centers_end),
          (store_faction_of_party, ":cur_faction", ":cur_center"),
          (eq, ":cur_faction", ":faction_no"),
          (party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
          (val_add, ":no_centers", 1),
          
          #(party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
        (eq, ":home_center", ":cur_center"), #I changed it with above line, now if lord is owner of any village its bound walled center is counted as 1000. Better this way. ozan-18.01.09		#	1.143 Port, Changed comment
          
          (val_add, ":no_centers", 1000),
        (try_end),
	  ##PBOD - Caba defeated lords fix begin
      (gt, ":no_centers", 0), #Fail if there are no centers
	  (assign, "$g_there_is_no_avaliable_centers", 0),
	  ## REMOVE??
	  
      #if no center is available count all centers not besieged do not care its faction.
	  (try_begin),
        (le, ":no_centers", 0), 

		(assign, "$g_there_is_no_avaliable_centers", 1),

        (try_for_range,":cur_center", walled_centers_begin, walled_centers_end),
	      (party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
          (val_add, ":no_centers", 1),                                   
        (try_end),
	  (else_try),
	    (assign, "$g_there_is_no_avaliable_centers", 0),
	  (try_end),

      (faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
	  (this_or_next|eq, "$g_there_is_no_avaliable_centers", 0),
      (neq, ":troop_no", ":faction_leader"), #faction leaders cannot spawn if they have no centers.

        (store_random_in_range, ":random_center", 0, ":no_centers"),
        (try_for_range,":cur_center", walled_centers_begin, walled_centers_end),
          (eq, ":result", -1),
          (store_faction_of_party, ":cur_faction", ":cur_center"),
		  (this_or_next|eq, "$g_there_is_no_avaliable_centers", 1),									#	1.143 Port // New line
          (eq, ":cur_faction", ":faction_no"),
          (party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
          (val_sub, ":random_center", 1),
          (try_begin),
            #(party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
          (eq, ":home_center", ":cur_center"), #I changed it with above line, now if lord is owner of any village its bound walled center is counted as 1000. Better this way. ozan-18.01.09
		  (eq, "$g_there_is_no_avaliable_centers", 0),												#	1.143 Port // Changed comment, New line
            
            (val_sub, ":random_center", 1000),
          (try_end),
          (lt, ":random_center", 0),
          (assign, ":result", ":cur_center"),
        (try_end),
        (assign, reg0, ":result"),
    ]),
    
    
    #script_cf_select_random_walled_center_with_faction_and_less_strength_priority:
    # This script selects a random center in range [centers_begin, centers_end)
    # such that faction of the town is equal to given_faction
    # INPUT:
    # arg1 = faction_no
    # arg2 = preferred_center_no
    
    #OUTPUT:
    # This script may return false if there is no matching town.
    # reg0 = town_no (Can fail)
    ("cf_select_random_walled_center_with_faction_and_less_strength_priority",
      [
        (store_script_param, ":faction_no", 1),
        (store_script_param, ":preferred_center_no", 2),
        (assign, ":result", -1),
        # First count num matching spawn points
        (assign, ":no_centers", 0),
        (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
          (store_faction_of_party, ":cur_faction", ":cur_center"),
          (eq, ":cur_faction", ":faction_no"),
          (party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
          (val_add, ":no_centers", 1),
          (try_begin),
            (eq, ":cur_center", ":preferred_center_no"),
            (val_add, ":no_centers", 99),
          (try_end),
          ##        (call_script, "script_party_calculate_regular_strength", ":cur_center"),
          ##        (assign, ":strength", reg0),
          ##        (lt, ":strength", 80),
          ##        (store_sub, ":strength", 100, ":strength"),
          ##        (val_div, ":strength", 20),
          ##        (val_add, ":no_centers", ":strength"),
        (try_end),
        (gt, ":no_centers", 0), #Fail if there are no centers
        (store_random_in_range, ":random_center", 0, ":no_centers"),
        (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
          (eq, ":result", -1),
          (store_faction_of_party, ":cur_faction", ":cur_center"),
          (eq, ":cur_faction", ":faction_no"),
          (party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
          (val_sub, ":random_center", 1),
          (try_begin),
            (eq, ":cur_center", ":preferred_center_no"),
            (val_sub, ":random_center", 99),
          (try_end),
          ##        (try_begin),
          ##          (call_script, "script_party_calculate_regular_strength", ":cur_center"),
          ##          (assign, ":strength", reg0),
          ##          (lt, ":strength", 80),
          ##          (store_sub, ":strength", 100, ":strength"),
          ##          (val_div, ":strength", 20),
          ##          (val_sub, ":random_center", ":strength"),
          ##        (try_end),
          (lt, ":random_center", 0),
          (assign, ":result", ":cur_center"),
        (try_end),
        (assign, reg0, ":result"),
    ]),
    
    
    #script_cf_select_random_town_at_peace_with_faction:
    # This script selects a random town in range [towns_begin, towns_end)
    # such that faction of the town is friendly to given_faction
    # INPUT:
    # arg1 = faction_no
    
    #OUTPUT:
    # This script may return false if there is no matching town.
    # reg0 = town_no
    ("cf_select_random_town_at_peace_with_faction",
      [
        (store_script_param_1, ":faction_no"),
        (assign, ":result", -1),
        # First count num matching towns
        (assign, ":no_towns", 0),
        (try_for_range,":cur_town", towns_begin, towns_end),
          (store_faction_of_party, ":cur_faction", ":cur_town"),
          (store_relation,":reln", ":cur_faction", ":faction_no"),
          (ge, ":reln", 0),
          (val_add, ":no_towns", 1),
        (try_end),
        (gt, ":no_towns", 0), #Fail if there are no towns
        (store_random_in_range, ":random_town", 0, ":no_towns"),
        (assign, ":no_towns", 0),
        (try_for_range,":cur_town", towns_begin, towns_end),
          (eq, ":result", -1),
          (store_faction_of_party, ":cur_faction", ":cur_town"),
          (store_relation,":reln", ":cur_faction", ":faction_no"),
          (ge, ":reln", 0),
          (val_add, ":no_towns", 1),
          (gt, ":no_towns", ":random_town"),
          (assign, ":result", ":cur_town"),
        (try_end),
        (assign, reg0, ":result"),
    ]),
    
    #script_cf_select_random_town_at_peace_with_faction_in_trade_route
    # INPUT:
    # arg1 = town_no
    # arg2 = faction_no
    
    #OUTPUT:
    # This script may return false if there is no matching town.
    # reg0 = town_no
    ("cf_select_random_town_at_peace_with_faction_in_trade_route",
      [
        (store_script_param, ":town_no", 1),
        (store_script_param, ":faction_no", 2),
        (assign, ":result", -1),
        (assign, ":no_towns", 0),
        (try_for_range, ":cur_slot", slot_town_trade_routes_begin, slot_town_trade_routes_end),
          (party_get_slot, ":cur_town", ":town_no", ":cur_slot"),
          (gt, ":cur_town", 0),
          (store_faction_of_party, ":cur_faction", ":cur_town"),
          (store_relation, ":reln", ":cur_faction", ":faction_no"),
          (ge, ":reln", 0),
          (val_add, ":no_towns", 1),
        (try_end),
        (gt, ":no_towns", 0), #Fail if there are no towns
        (store_random_in_range, ":random_town", 0, ":no_towns"),
        (try_for_range, ":cur_slot", slot_town_trade_routes_begin, slot_town_trade_routes_end),
          (eq, ":result", -1),
          (party_get_slot, ":cur_town", ":town_no", ":cur_slot"),
          (gt, ":cur_town", 0),
          (store_faction_of_party, ":cur_faction", ":cur_town"),
          (store_relation, ":reln", ":cur_faction", ":faction_no"),
          (ge, ":reln", 0),
          (val_sub, ":random_town", 1),
          (lt, ":random_town", 0),
          (assign, ":result", ":cur_town"),
        (try_end),
        (assign, reg0, ":result"),
    ]),
    
    
    
    #the following is a very simple adjustment - it measures the difference in prices between two towns
    #all goods are weighted equally except for luxuries
    #it does not take into account the prices of the goods, nor cargo capacity
    #to do that properly, a merchant would have to virtually fill his baggage, slot by slot, for each town
	#i also found that one needed to introduce demand inelasticity -- prices should vary a lot for grain,  relatively little for iron
    ##diplomacy start+
	#
    #Added a third parameter, the caravan party, for use in distance calculations and perhaps
	#other things in the future.  This may be -1, in which case the script attempts to find a
	#general answer without referring to any specific attributes.  It may also be a town,
	#in which case its position is used for distance calculations.
	##diplomacy end+
	("cf_select_most_profitable_town_at_peace_with_faction_in_trade_route",
    [
      (store_script_param, ":town_no", 1),
      (store_script_param, ":faction_no", 2),
	  ##diplomacy start+
	  (store_script_param, ":perspective_party", 3),
	  ##diplomacy end+

      (assign, ":result", -1),
	  (assign, ":best_town_score", 0),
      (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),

	  ##diplomacy start+
	  # If economics changes are enabled, the caravan may also take into account the distance
	  # to the destination or bias towards towns of its town faction.
	  (store_random_in_range, ":consider_distance", 0, 2),
	  (store_random_in_range, ":faction_bias", 0, 2),
	  (try_begin), 
		(lt, ":perspective_party", 0),
		(assign, ":perspective_party", ":town_no"),
	  (try_end),
      ##diplomacy end+
        
        (try_for_range, ":cur_slot", slot_town_trade_routes_begin, slot_town_trade_routes_end),
          (party_get_slot, ":cur_town", ":town_no", ":cur_slot"),
          (gt, ":cur_town", 0),
          
          (store_faction_of_party, ":cur_faction", ":cur_town"),
          (store_relation, ":reln", ":cur_faction", ":faction_no"),
          (ge, ":reln", 0),
          
          (assign, ":cur_town_score", 0),
          (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
            (neq, ":cur_goods", "itm_trade_butter"), #Don't count perishables
            (neq, ":cur_goods", "itm_trade_cattle_meat"),
            (neq, ":cur_goods", "itm_trade_chicken"),
            (neq, ":cur_goods", "itm_trade_pork"),
            
            (store_add, ":cur_goods_price_slot", ":cur_goods", ":item_to_price_slot"),
            (party_get_slot, ":origin_price", ":town_no", ":cur_goods_price_slot"),
            (party_get_slot, ":destination_price", ":cur_town", ":cur_goods_price_slot"),
            
            (gt, ":destination_price", ":origin_price"),
            (store_sub, ":price_dif", ":destination_price", ":origin_price"),
            
            (try_begin), #weight luxury goods double
              (this_or_next|eq, ":cur_goods", "itm_trade_spice"),
              (eq, ":cur_goods", "itm_trade_velvet"),
              (val_mul, ":price_dif", 2),
            (try_end),
            (val_add, ":cur_town_score", ":price_dif"),
          (try_end),
          
          ##		(try_begin),
          ##			(eq, "$cheat_mode", 1),
          ##			(str_store_party_name, s10, ":town_no"),
          ##			(str_store_party_name, s11, ":cur_town"),
          ##			(assign, reg3, ":cur_town_score"),
          ##			(display_message, "str_caravan_in_s10_considers_s11_total_price_dif_=_reg3"),
          ##		(try_end),
		  
		##diplomacy start+
		(try_begin),
			#Economic changes must be enabled, or the player must have decided
			#to use mercantilism settings (which expresses a desire to see changes
			#related to that setting applied), or a trade treaty must be in effect.
			(this_or_next|neg|faction_slot_eq, "fac_player_supporters_faction", dplmc_slot_faction_mercantilism, 0),
			(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
			#Take into account distance, or treat factions preferentially
			(try_begin),
				#Bias towards own faction
				(ge, ":faction_bias", 1),
				(neq, ":faction_no", ":cur_faction"),
				
				##The penalty is based on the source faction's mercantilism rating, as well as
				##the other faction's mercantilism rating.
				(faction_get_slot, ":source_mercantilism", ":faction_no", dplmc_slot_faction_mercantilism),
				(val_clamp, ":source_mercantilism", -3, 4),
				(faction_get_slot, ":dest_mercantilism", ":cur_faction", dplmc_slot_faction_mercantilism),
				(val_clamp, ":dest_mercantilism", -3, 4),
				##Default (if both factions have mercantilism 0) is a 6% reduction.  Possible range is 0% (least) to 12% (most).
				(store_sub, ":percent", 94, ":source_mercantilism"),
				(val_sub, ":percent", ":dest_mercantilism"),

				(val_mul, ":cur_town_score", ":percent"),
				(val_add, ":cur_town_score", 50),
				(val_div, ":cur_town_score", 100),
			(try_end),
			(try_begin),
				(ge, ":consider_distance", 1),#consider distance
				(store_distance_to_party_from_party, ":dist", ":perspective_party",":cur_town"),
				#Avoid asymptotic effects and undue weighting.
				#Further explanation: What we really care about is time, not distance.
				#It will take time to buy and sell once reaching our destination: halving
				#the distance doesn't double the expected profit per month.
				(val_max, ":dist", 0),
				(val_add, ":dist", 12),
				#Avoid possible problems trying to compare distant towns
				(val_mul, ":cur_town_score", 100),
				(val_div, ":cur_town_score", ":dist"),
			(try_end),
		(try_end),
		##diplomacy end+
          
          (gt, ":cur_town_score", ":best_town_score"),
          (assign, ":best_town_score", ":cur_town_score"),
          (assign, ":result", ":cur_town"),
          
        (try_end),
        
        (gt, ":result", -1), #Fail if there are no towns
        
        (assign, reg0, ":result"),
        
        #	  (store_current_hours, ":hour"),
        #	  (party_set_slot, ":result", slot_town_caravan_last_visit, ":hour"),
        
        ##	  (try_begin),
        ##		(eq, "$cheat_mode", 1),
        ##	    (assign, reg3, ":best_town_score"),
        ##	    (str_store_party_name, s3, ":town_no"),
        ##	    (str_store_party_name, s4, ":result"),
        ##	    (display_message, "str_test__caravan_in_s3_selects_for_s4_trade_score_reg3"),
        ##	  (try_end),
        
    ]),
    
    ("cf_select_most_profitable_coastal_town_at_peace_with_faction_in_trade_route",
      [
        (store_script_param, ":town_no", 1),
        (store_script_param, ":faction_no", 2),
        
        (assign, ":result", -1),
        (assign, ":best_town_score", 0),
        (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
        
        (try_for_range, ":cur_slot", slot_town_trade_routes_begin, slot_town_trade_routes_end),
          (party_get_slot, ":cur_town", ":town_no", ":cur_slot"),
          (gt, ":cur_town", 0),
          (party_slot_ge, ":cur_town", slot_town_is_coastal, 1), #Seatrade
          
          (store_faction_of_party, ":cur_faction", ":cur_town"),
          (store_relation, ":reln", ":cur_faction", ":faction_no"),
          (ge, ":reln", 0),
          
          (assign, ":cur_town_score", 0),
          (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
            (neq, ":cur_goods", "itm_trade_butter"), #Don't count perishables
            (neq, ":cur_goods", "itm_trade_cattle_meat"),
            (neq, ":cur_goods", "itm_trade_chicken"),
            (neq, ":cur_goods", "itm_trade_pork"),
            
            (store_add, ":cur_goods_price_slot", ":cur_goods", ":item_to_price_slot"),
            (party_get_slot, ":origin_price", ":town_no", ":cur_goods_price_slot"),
            (party_get_slot, ":destination_price", ":cur_town", ":cur_goods_price_slot"),
            
            (gt, ":destination_price", ":origin_price"),
            (store_sub, ":price_dif", ":destination_price", ":origin_price"),
            
            (try_begin), #weight luxury goods double
              (this_or_next|eq, ":cur_goods", "itm_trade_spice"),
              (eq, ":cur_goods", "itm_trade_velvet"),
              (val_mul, ":price_dif", 2),
            (try_end),
            (val_add, ":cur_town_score", ":price_dif"),
          (try_end),
          
          ##        (try_begin),
          ##            (eq, "$cheat_mode", 1),
          ##            (str_store_party_name, s10, ":town_no"),
          ##            (str_store_party_name, s11, ":cur_town"),
          ##            (assign, reg3, ":cur_town_score"),
          ##            (display_message, "str_caravan_in_s10_considers_s11_total_price_dif_=_reg3"),
          ##        (try_end),
          
          (gt, ":cur_town_score", ":best_town_score"),
          (assign, ":best_town_score", ":cur_town_score"),
          (assign, ":result", ":cur_town"),
          
        (try_end),
        
        (gt, ":result", -1), #Fail if there are no towns
        
        (assign, reg0, ":result"),
        
        #      (store_current_hours, ":hour"),
        #      (party_set_slot, ":result", slot_town_caravan_last_visit, ":hour"),
        
        # (try_begin),
        ###(eq, "$cheat_mode", 1),
        # (assign, reg3, ":best_town_score"),
        # (str_store_party_name, s3, ":town_no"),
        # (str_store_party_name, s4, ":result"),
        # (display_message, "str_test__caravan_in_s3_selects_for_s4_trade_score_reg3"),
        # (try_end),
        
    ]),
    
    
    ##  ("cf_select_faction_spawn_point",
    ##    [
    ##      # First count num matching spawn points
    ##      (assign, reg(24), 0),
    ##      (try_for_range,reg(25), spawn_points_begin, spawn_points_end),
    ##        (store_faction_of_party, reg(23), reg(25)),
    ##        (eq, reg(23), "$pin_faction"),
    ##        (val_add, reg(24), 1),
    ##      (end_try,0),
    ##      # reg4 now holds num towns of this faction.
    ##      (gt, reg(24), 0), #Fail if there are no towns
    ##      (store_random, reg(26), reg(24)),
    ##
    ##      (assign, reg(24), 0), # reg24 = num points of this faction.
    ##      (try_for_range,reg(25), spawn_points_begin, spawn_points_end),
    ##        (store_faction_of_party, reg(23), reg(25)),
    ##        (eq, reg(23), "$pin_faction"),
    ##        (try_begin,0),
    ##          (eq, reg(24), reg(26)),
    ##          (assign, "$pout_town", reg(25)), # result is this town
    ##        (end_try,0),
    ##        (val_add, reg(24), 1),
    ##      (end_try,0),
    ##  ]),
    
    
    #script_spawn_party_at_random_town:
    # This script selects a random town in range [towns_begin, towns_end)
    # such that faction of the town is equal to given_faction
    # and spawns a new party there.
    # INPUT:
    # $pin_faction: given_faction
    # $pin_party_template: given_party_template
    
    #OUTPUT:
    # This script may return false if party cannot be spawned.
    # $pout_party: id of the spawned party
    ##  ("spawn_party_at_random_town",
    ##    [
    ##      (call_script,"script_select_random_spawn_point"),
    ##      (set_spawn_radius,1),
    ##      (spawn_around_party,"$pout_town","$pin_party_template"),
    ##      (assign, "$pout_party", reg(0)),
    ##  ]),
    
    #script_cf_spawn_party_at_faction_town:
    # This script selects a random town in range [towns_begin, towns_end)
    # such that faction of the town is equal to given_faction
    # and spawns a new party there.
    # INPUT:
    # $pin_faction: given_faction
    # $pin_party_template: given_party_template
    
    #OUTPUT:
    # This script may return false if party cannot be spawned.
    # $pout_party: id of the spawned party
    ##  ("cf_spawn_party_at_faction_town",
    ##    [
    ##      (call_script,"script_cf_select_faction_spawn_point"),
    ##      (set_spawn_radius,1),
    ##      (spawn_around_party,"$pout_town","$pin_party_template"),
    ##      (assign, "$pout_party", reg(0)),
    ##  ]),
    
    #script_spawn_party_at_random_town_if_below_limit:
    # This script checks if number of parties
    # of specified template is less than limit,
    # If so, it selects a random town in range [towns_begin, towns_end)
    # and spawns a new party there.
    # INPUT:
    # $pin_party_template: given_party_template
    # $pin_limit: limit value
    
    #OUTPUT:
    # $pout_party: id of the spawned party
    # $pout_town: id of the selected faction town
    # Note:
    # This script may return false if number of parties
    # of specified template is greater or equal to limit,
    # or if party cannot be spawned.
    ##  ("cf_spawn_party_at_random_town_if_below_limit",
    ##    [
    ##      (store_num_parties_of_template, reg(22), "$pin_party_template"),
    ##      (lt,reg(22),"$pin_limit"), #check if we are below limit.
    ##      (call_script,"script_select_random_spawn_point"),
    ##      (set_spawn_radius,1),
    ##      (spawn_around_party,"$pout_town","$pin_party_template"),
    ##      (assign, "$pout_party", reg(0)),
    ##  ]),
    
    ##  #script_spawn_party_at_faction_town_if_below_limit:
    ##  # This script checks if number of parties
    ##  # of specified template is less than limit,
    ##  # If so, it selects a random town in range [towns_begin, towns_end)
    ##  # such that faction of the town is equal to given_faction
    ##  # and spawns a new party there.
    ##  # INPUT:
    ##  # $pin_faction: given_faction
    ##  # $pin_party_template: given_party_template
    ##  # $pin_limit: limit value
    ##
    ##  #OUTPUT:
    ##  # $pout_party: id of the spawned party
    ##  # $pout_town: id of the selected faction town
    ##  # Note:
    ##  # This script may return false if number of parties
    ##  # of specified template is greater or equal to limit,
    ##  # or if party cannot be spawned.
    ##  ("cf_spawn_party_at_faction_town_if_below_limit",
    ##    [
    ##      (store_num_parties_of_template, reg(22), "$pin_party_template"),
    ##      (lt,reg(22),"$pin_limit"), #check if we are below limit.
    ##      (call_script,"script_cf_select_faction_spawn_point"),
    ##      (set_spawn_radius,1),
    ##      (spawn_around_party,"$pout_town","$pin_party_template"),
    ##      (assign, "$pout_party", reg(0)),
    ##  ]),
    
    # script_shuffle_troop_slots:
    # Shuffles a range of slots of a given troop.
    # Used for exploiting a troop as an array.
    # Input: arg1 = troop_no, arg2 = slot_begin, arg3 = slot_end
    ("shuffle_troop_slots",
      [
        (store_script_param, ":troop_no", 1),
        (store_script_param, ":slots_begin", 2),
        (store_script_param, ":slots_end", 3),
        (try_for_range, ":cur_slot_no", ":slots_begin", ":slots_end"),
          (store_random_in_range, ":random_slot_no", ":slots_begin", ":slots_end"), #reg(58) = random slot. Now exchange slots reg(57) and reg(58)
          (troop_get_slot, ":cur_slot_value", ":troop_no", ":cur_slot_no"), #temporarily store the value in slot reg(57) in reg(59)
          (troop_get_slot, ":random_slot_value", ":troop_no", ":random_slot_no"), #temporarily store the value in slot reg(58) in reg(60)
          (troop_set_slot, ":troop_no", ":cur_slot_no", ":random_slot_value"), # Now exchange the two...
          (troop_set_slot, ":troop_no", ":random_slot_no", ":cur_slot_value"),
        (try_end),
    ]),
    
    
    # script_get_quest - combines old get_random_quest with new get_dynamic_quest
    
    # Input: arg1 = troop_no (of the troop in conversation), arg2 = min_importance (of the quest)
    # Output: reg0 = quest_no (the slots of the quest will be filled after calling this script)
  ("get_quest",
    [
      (store_script_param_1, ":giver_troop"),

      (store_character_level, ":player_level", "trp_player"),
      (store_troop_faction, ":giver_faction_no", ":giver_troop"),

      (troop_get_slot, ":giver_party_no", ":giver_troop", slot_troop_leaded_party),
      (troop_get_slot, ":giver_reputation", ":giver_troop", slot_lord_reputation_type),

      (assign, ":giver_center_no", -1),
      (try_begin),
        (gt, ":giver_party_no", 0),
        (party_get_attached_to, ":giver_center_no", ":giver_party_no"),
      (else_try),
        (is_between, "$g_encountered_party", centers_begin, centers_end),
        (assign, ":giver_center_no", "$g_encountered_party"),
      (try_end),
	  
	  ##diplomacy start+
	  (call_script, "script_troop_get_player_relation", ":giver_troop"),
	  (assign, ":giver_relation", reg0),
	  (store_relation, ":giver_faction_relation", ":giver_faction_no", "fac_player_faction"),
	  #Assign some variables used later (mostly in lord checks) to re-enable
	  #quests which are usually disabled once the player has received homage.
	  (assign, ":is_close", 0),
	  (assign, ":nominal_superior", 0),
	  (try_begin),
		#is valid hero:
		(is_between, ":giver_troop", heroes_begin, heroes_end),
		(troop_slot_ge, ":giver_troop", slot_troop_occupation, slto_inactive + 1),
		(neg|troop_slot_ge, ":giver_troop", slot_troop_occupation, slto_retirement),
		
		#is close:
		(try_begin),
			#affiliates, and spouse
			(call_script, "script_dplmc_is_affiliated_family_member", ":giver_troop"),
			(this_or_next|ge, reg0, 1),
				(troop_slot_eq, "trp_player", slot_troop_spouse, ":giver_troop"),
			(assign, ":is_close", 1),
		(else_try),
			(ge, ":giver_faction_relation", 0),
			(ge, ":giver_relation", 50),
			(try_begin),
				(this_or_next|is_between, ":giver_troop", companions_begin, companions_end),
					(is_between, ":giver_troop", pretenders_begin, pretenders_end),
				(this_or_next|troop_slot_eq, ":giver_troop", slot_troop_occupation, slto_kingdom_hero),
					(troop_slot_eq, ":giver_troop", slot_troop_occupation, slto_player_companion),
				(neg|troop_slot_eq, ":giver_troop", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
				(assign, ":is_close", 1),
			(else_try),
				#(call_script, "script_troop_get_family_relation_to_troop", ":giver_troop", "trp_player"),
				(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":giver_troop", "trp_player"),
				(ge, reg0, 2),
				(assign, ":is_close", 1),
			(try_end),
		(try_end),
		
		#is nominally the social superior of the player (or even if not the superior,
		#is allowed to give the player orders in at least one context)
		(try_begin),
			#quest giver is faction leader or marshall, or player's father or mother
			(this_or_next|troop_slot_eq, "trp_player", slot_troop_father, ":giver_troop"),
			(this_or_next|troop_slot_eq, "trp_player", slot_troop_mother, ":giver_troop"),
			(this_or_next|faction_slot_eq, ":giver_faction_no", slot_faction_leader, ":giver_troop"),
				(faction_slot_eq, ":giver_faction_no", slot_faction_marshall, ":giver_troop"),
			(assign, ":nominal_superior", 1),
		(else_try),
			#player has less than 3/4 of the quest giver's renown
			(troop_get_slot, reg0, ":giver_troop", slot_troop_renown),
			(val_mul, reg0, 3),
			(val_div, reg0, 4),
			(neg|troop_slot_ge, "trp_player", slot_troop_renown, reg0),
			(assign, ":nominal_superior", 1),
		(else_try),
			#quest giver is player's father-in-law or mother-in-law
			(troop_get_slot, ":player_spouse", "trp_player", slot_troop_spouse),
			(is_between, ":player_spouse", heroes_begin, heroes_end),
			(this_or_next|troop_slot_eq, ":player_spouse", slot_troop_father, ":giver_troop"),
				(troop_slot_eq, ":player_spouse", slot_troop_mother, ":giver_troop"),
			(assign, ":nominal_superior", 1),
		(try_end),
	  (try_end),
	  ##diplomacy end+

      (try_begin),
        (troop_slot_eq, ":giver_troop", slot_troop_occupation, slto_kingdom_hero),
        (try_begin),
          (ge, "$g_talk_troop_faction_relation", 0),
          (assign, ":quests_begin", lord_quests_begin),
          (assign, ":quests_end", lord_quests_end),
          (assign, ":quests_begin_2", lord_quests_begin_2),
          (assign, ":quests_end_2", lord_quests_end_2),
        (else_try),
          (assign, ":quests_begin", enemy_lord_quests_begin),
          (assign, ":quests_end", enemy_lord_quests_end),
          (assign, ":quests_begin_2", 0),
          (assign, ":quests_end_2", 0),
        (try_end),
      (else_try),
        (is_between, ":giver_troop", village_elders_begin, village_elders_end),
        (assign, ":quests_begin", village_elder_quests_begin),
        (assign, ":quests_end", village_elder_quests_end),
        (assign, ":quests_begin_2", village_elder_quests_begin_2),
        (assign, ":quests_end_2", village_elder_quests_end_2),
      (else_try),
        (is_between, ":giver_troop", mayors_begin, mayors_end),
        (assign, ":quests_begin", mayor_quests_begin),
        (assign, ":quests_end", mayor_quests_end),
        (assign, ":quests_begin_2", mayor_quests_begin_2),
        (assign, ":quests_end_2", mayor_quests_end_2),
      (else_try),
        (assign, ":quests_begin", lady_quests_begin),
        (assign, ":quests_end", lady_quests_end),
        (assign, ":quests_begin_2", lady_quests_begin_2),
        (assign, ":quests_end_2", lady_quests_end_2),
      (try_end),

      (assign, ":result", -1),
	  (assign, ":quest_target_troop", -1),
	  (assign, ":quest_target_center", -1),
	  (assign, ":quest_target_faction", -1),
	  (assign, ":quest_object_faction", -1),
	  (assign, ":quest_object_troop", -1),
	  (assign, ":quest_object_center", -1),
	  (assign, ":quest_target_party", -1),
	  (assign, ":quest_target_party_template", -1),
	  (assign, ":quest_target_amount", -1),
	  (assign, ":quest_target_dna", -1),
	  (assign, ":quest_target_item", -1),
	  (assign, ":quest_importance", 1),
	  (assign, ":quest_xp_reward", 0),
	  (assign, ":quest_gold_reward", 0),
	  (assign, ":quest_convince_value", 0),
	  (assign, ":quest_expiration_days", 0),
	  (assign, ":quest_dont_give_again_period", 0),

	  (try_begin), #get dynamic quest is a separate script, so that we can scan a number of different troops at once for it
	   	(call_script, "script_get_dynamic_quest", "$g_talk_troop"),

	    (assign, ":result", reg0),
	    (assign, ":relevant_troop", reg1),
	    (assign, ":relevant_party", reg2),
	    (assign, ":relevant_faction", reg3),

	    #GUILDMASTER QUESTS
	    (try_begin),
			(eq, ":result", "qst_track_down_bandits"),
			(assign, ":quest_target_party", ":relevant_party"),
			(assign ,":quest_expiration_days", 60),
			(assign, ":quest_xp_reward", 1000),
			(assign, ":quest_gold_reward", 1000),

		(else_try),
			(eq, ":result", "qst_retaliate_for_border_incident"),
			(assign, ":quest_target_troop", ":relevant_troop"),
			(assign, ":quest_target_faction", ":relevant_faction"),

			(assign ,":quest_expiration_days", 30),
			(assign, ":quest_xp_reward", 1000),
			(assign, ":quest_gold_reward", 1000),

		#KINGDOM LORD QUESTS
		(else_try),
	        (eq, ":result", "qst_cause_provocation"),
			(assign, ":quest_target_faction", ":relevant_faction"),
	        (assign, ":quest_expiration_days", 30),
	        (assign, ":quest_dont_give_again_period", 100),
			(assign, ":quest_xp_reward", 1000),
			(assign, ":quest_gold_reward", 1000),

	    (else_try),
			(eq, ":result", "qst_destroy_bandit_lair"),
			(assign, ":quest_target_party", ":relevant_party"),
			(assign ,":quest_expiration_days", 60),
			(assign, ":quest_xp_reward", 3000),
			(assign, ":quest_gold_reward", 1500),

		#KINGDOM LADY OR KINGDOM HERO QUESTS
		(else_try),
	        (eq, ":result", "qst_rescue_prisoner"),
			(assign, ":quest_target_troop", ":relevant_troop"),
			(assign, ":quest_target_center", ":relevant_party"),

	        (assign, ":quest_expiration_days", 30),
	        (assign, ":quest_dont_give_again_period", 5),
			(assign, ":quest_xp_reward", 1500),
			(assign, ":quest_gold_reward", 3000),
		(try_end),
	  (try_end),

	  #no dynamic quest available
	  (try_begin),
		(eq, ":result", -1),

	    (try_for_range, ":unused", 0, 20), #Repeat trial twenty times
	        (eq, ":result", -1),
	        (assign, ":quest_target_troop", -1),
	        (assign, ":quest_target_center", -1),
	        (assign, ":quest_target_faction", -1),
	        (assign, ":quest_object_faction", -1),
	        (assign, ":quest_object_troop", -1),
	        (assign, ":quest_object_center", -1),
	        (assign, ":quest_target_party", -1),
	        (assign, ":quest_target_party_template", -1),
	        (assign, ":quest_target_amount", -1),
	        (assign, ":quest_target_dna", -1),
	        (assign, ":quest_target_item", -1),
	        (assign, ":quest_importance", 1),
	        (assign, ":quest_xp_reward", 0),
	        (assign, ":quest_gold_reward", 0),
	        (assign, ":quest_convince_value", 0),
	        (assign, ":quest_expiration_days", 0),
	        (assign, ":quest_dont_give_again_period", 0),

            (store_sub, ":num_possible_old_quests", ":quests_end", ":quests_begin"),
            (store_sub, ":num_possible_new_quests", ":quests_end_2", ":quests_begin_2"),
            (store_add, ":num_possible_total_quests", ":num_possible_old_quests", ":num_possible_new_quests"),

            (store_random_in_range, ":quest_no", 0, ":num_possible_total_quests"),
            (try_begin),
              (lt, ":quest_no", ":num_possible_old_quests"),
              (store_random_in_range, ":quest_no", ":quests_begin", ":quests_end"),
            (else_try),
              (store_random_in_range, ":quest_no", ":quests_begin_2", ":quests_end_2"),
            (try_end),

#TODO: Remove this when test is done
#       (assign, ":quest_no", "qst_meet_spy_in_enemy_town"),
#TODO: Remove this when test is done end
	        (neg|check_quest_active,":quest_no"),
	        (neg|quest_slot_ge, ":quest_no", slot_quest_dont_give_again_remaining_days, 1),
	        (try_begin),
	          # Village Elder quests
	          (eq, ":quest_no", "qst_deliver_grain"),
	          (try_begin),
	            (is_between, ":giver_center_no", villages_begin, villages_end),
	            #The quest giver is the village elder
	            (call_script, "script_get_troop_item_amount", ":giver_troop", "itm_trade_grain"),
	            (eq, reg0, 0),
	            (neg|party_slot_ge, ":giver_center_no", slot_town_prosperity, 40),
	            (assign, ":quest_target_center", ":giver_center_no"),
	            (store_random_in_range, ":quest_target_amount", 4, 8),
	            (assign, ":quest_expiration_days", 30),
	            (assign, ":quest_dont_give_again_period", 20),
	            (assign, ":result", ":quest_no"),
	          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_deliver_cattle"),
	          (try_begin),
	            (is_between, ":giver_center_no", villages_begin, villages_end),
	            #The quest giver is the village elder
	            (party_get_slot, ":num_cattle", ":giver_center_no", slot_village_number_of_cattle),
	            (lt, ":num_cattle", 50),
	            (assign, ":quest_target_center", ":giver_center_no"),
	            (store_random_in_range, ":quest_target_amount", 5, 10),
	            (assign, ":quest_expiration_days", 30),
	            (assign, ":quest_dont_give_again_period", 20),
	            (assign, ":result", ":quest_no"),
	          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_train_peasants_against_bandits"),
	          (try_begin),
	            (is_between, ":giver_center_no", villages_begin, villages_end),
	            #The quest giver is the village elder
	            (store_skill_level, ":player_trainer", "skl_trainer", "trp_player"),
	            (gt, ":player_trainer", 0),
	            (store_random_in_range, ":quest_target_amount", 5, 8),
	            (assign, ":quest_target_center", ":giver_center_no"),
	            (assign, ":quest_expiration_days", 20),
	            (assign, ":quest_dont_give_again_period", 40),
	            (assign, ":result", ":quest_no"),
	          (try_end),
	        (else_try),
	          # Mayor quests
	          (eq, ":quest_no", "qst_escort_merchant_caravan"),
	          (is_between, ":giver_center_no", centers_begin, centers_end),
	          (store_random_party_in_range, ":quest_target_center", towns_begin, towns_end),
	          (store_distance_to_party_from_party, ":dist", ":giver_center_no",":quest_target_center"),
	          (assign, ":quest_gold_reward", ":dist"),
	          (val_add, ":quest_gold_reward", 25),
	          (val_mul, ":quest_gold_reward", 25),
	          (val_div, ":quest_gold_reward", 20),
	          (store_random_in_range, ":quest_target_amount", 6, 12),
	          (assign, "$escort_merchant_caravan_mode", 0),
	          (assign, ":result", ":quest_no"),
	        (else_try),
	          (eq, ":quest_no", "qst_deliver_wine"),
	          (is_between, ":giver_center_no", centers_begin, centers_end),
	          (store_random_party_in_range, ":quest_target_center", towns_begin, towns_end),
	          (store_random_in_range, ":random_no", 0, 2),
	          (try_begin),
	            (eq, ":random_no", 0),
	            (assign, ":quest_target_item", "itm_quest_wine"),
	          (else_try),
	            (assign, ":quest_target_item", "itm_quest_ale"),
	          (try_end),
	          (store_random_in_range, ":quest_target_amount", 6, 12),
	          (store_distance_to_party_from_party, ":dist", ":giver_center_no",":quest_target_center"),
	          (assign, ":quest_gold_reward", ":dist"),
	          (val_add, ":quest_gold_reward", 2),
	          (assign, ":multiplier", 5),
	          (val_add, ":multiplier", ":quest_target_amount"),
	          (val_mul, ":quest_gold_reward", ":multiplier"),
	          (val_div, ":quest_gold_reward", 100),
	          (val_mul, ":quest_gold_reward", 10),
	          (store_item_value,"$qst_deliver_wine_debt",":quest_target_item"),
	          (val_mul,"$qst_deliver_wine_debt",":quest_target_amount"),
	          (val_mul,"$qst_deliver_wine_debt", 6),
	          (val_div,"$qst_deliver_wine_debt",5),
	          (assign, ":quest_expiration_days", 7),
	          (assign, ":quest_dont_give_again_period", 20),
	          (assign, ":result", ":quest_no"),
	        (else_try),
	          (eq, ":quest_no", "qst_troublesome_bandits"),
			  (is_between, ":giver_center_no", centers_begin, centers_end),
	          (store_character_level, ":quest_gold_reward", "trp_player"),
	          (val_add, ":quest_gold_reward", 20),
	          (val_mul, ":quest_gold_reward", 35),
	          (val_div, ":quest_gold_reward",100),
	          (val_mul, ":quest_gold_reward", 10),
	          (assign, ":quest_expiration_days", 30),
	          (assign, ":quest_dont_give_again_period", 30),
	          (assign, ":result", ":quest_no"),
	        (else_try),
	          (eq, ":quest_no", "qst_kidnapped_girl"),
	          (is_between, ":giver_center_no", centers_begin, centers_end),
	          (store_random_in_range, ":quest_target_center", villages_begin, villages_end),
	          (store_character_level, ":quest_target_amount"),
	          (val_add, ":quest_target_amount", 15),
	          (store_distance_to_party_from_party, ":dist", ":giver_center_no", ":quest_target_center"),
	          (val_add, ":dist", 15),
	          (val_mul, ":dist", 2),
	          (val_mul, ":quest_target_amount", ":dist"),
	          (val_div, ":quest_target_amount",100),
	          (val_mul, ":quest_target_amount",10),
	          (assign, ":quest_gold_reward", ":quest_target_amount"),
	          (val_div, ":quest_gold_reward", 40),
	          (val_mul, ":quest_gold_reward", 10),
                  (assign, ":quest_expiration_days", 15),
	          (assign, ":quest_dont_give_again_period", 30),
	          (assign, ":result", ":quest_no"),
	        (else_try),
	          (eq, ":quest_no", "qst_move_cattle_herd"),
	          (is_between, ":giver_center_no", centers_begin, centers_end),
	          (call_script, "script_cf_select_random_town_at_peace_with_faction", ":giver_faction_no"),
	          (neq, ":giver_center_no", reg0),
	          (assign, ":quest_target_center", reg0),
	          (store_distance_to_party_from_party, ":dist",":giver_center_no",":quest_target_center"),
	          (assign, ":quest_gold_reward", ":dist"),
	          (val_add, ":quest_gold_reward", 25),
	          (val_mul, ":quest_gold_reward", 50),
	          (val_div, ":quest_gold_reward", 20),
	          (assign, ":quest_expiration_days", 30),
	          (assign, ":quest_dont_give_again_period", 20),
	          (assign, ":result", ":quest_no"),
	        (else_try),
	          (eq, ":quest_no", "qst_persuade_lords_to_make_peace"),
	          (is_between, ":giver_center_no", centers_begin, centers_end),
	          (store_faction_of_party, ":cur_object_faction", ":giver_center_no"),
	          (call_script, "script_cf_faction_get_random_enemy_faction", ":cur_object_faction"),
	          (assign, ":cur_target_faction", reg0),
	          (call_script, "script_cf_get_random_lord_except_king_with_faction", ":cur_object_faction"),
	          (assign, ":cur_object_troop", reg0),
			  ##diplomacy start+
			  #may also be anyone with tmt_aristocrat > 0
			  (call_script, "script_dplmc_get_troop_morality_value", ":cur_object_troop", tmt_aristocratic),
			  (this_or_next|ge, reg0, 1),
			  ##diplomacy+
			  (this_or_next|troop_slot_eq, ":cur_object_troop", slot_lord_reputation_type, lrep_quarrelsome),
			  (this_or_next|troop_slot_eq, ":cur_object_troop", slot_lord_reputation_type, lrep_selfrighteous),
			  (this_or_next|troop_slot_eq, ":cur_object_troop", slot_lord_reputation_type, lrep_martial),
				(troop_slot_eq, ":cur_object_troop", slot_lord_reputation_type, lrep_debauched),

	          (call_script, "script_cf_get_random_lord_except_king_with_faction", ":cur_target_faction"),
	          (assign, ":quest_target_troop", reg0),
			  ##diplomacy start+
			  #may also be anyone with tmt_aristocrat > 0
			  (call_script, "script_dplmc_get_troop_morality_value", ":quest_target_troop", tmt_aristocratic),
			  (this_or_next|ge, reg0, 1),
			  ##diplomacy+
			  (this_or_next|troop_slot_eq, ":quest_target_troop", slot_lord_reputation_type, lrep_quarrelsome),
			  (this_or_next|troop_slot_eq, ":quest_target_troop", slot_lord_reputation_type, lrep_selfrighteous),
			  (this_or_next|troop_slot_eq, ":quest_target_troop", slot_lord_reputation_type, lrep_martial),
			  (troop_slot_eq, ":quest_target_troop", slot_lord_reputation_type, lrep_debauched),

	          (assign, ":quest_object_troop", ":cur_object_troop"),
	          (assign, ":quest_target_faction", ":cur_target_faction"),
	          (assign, ":quest_object_faction", ":cur_object_faction"),
	          (assign, ":quest_gold_reward", 12000),
	          (assign, ":quest_convince_value", 7000),
	          (assign, ":quest_expiration_days", 30),
	          (assign, ":quest_dont_give_again_period", 100),
	          (assign, ":result", ":quest_no"),
	        (else_try),
	          (eq, ":quest_no", "qst_deal_with_looters"),
                  ##diplomacy start+
                  #re-enable looters quest at all levels for variety
	          #(is_between, ":player_level", 0, 15),
                  ##diplomacy end+
	          (is_between, ":giver_center_no", centers_begin, centers_end),
	          (store_faction_of_party, ":cur_object_faction", ":giver_center_no"),
	          (store_num_parties_destroyed_by_player, ":num_looters_destroyed", "pt_looters"),
	          (party_template_set_slot,"pt_looters",slot_party_template_num_killed,":num_looters_destroyed"),
	          (quest_set_slot,":quest_no",slot_quest_current_state,0),
	          (quest_set_slot,":quest_no",slot_quest_target_party_template,"pt_looters"),
	          (assign, ":quest_gold_reward", 500),
	          (assign, ":quest_xp_reward", 500),
	          (assign, ":quest_expiration_days", 20),
	          (assign, ":quest_dont_give_again_period", 30),
		  ##diplomacy start+
                  (try_begin),
                  #don't give full quest reward if outside the normal level range
                     (ge, ":player_level", 15),
                     (store_sub, ":quest_xp_award", ":player_level", 14),
                     (val_mul, ":quest_xp_award", -10),
                     (val_add, ":quest_xp_award", 500),
                     (val_max, ":quest_xp_award", 100),#XP drops by 10 per level over limit, until level 40
                     #To avoid being pestered with trivia, increase :quest_dont_give_again_period with the player's level
                     (store_add, ":quest_dont_give_again_period", ":player_level", 16),
                  (try_end),
                  ##diplomacy end+
	          (assign, ":result", ":quest_no"),
	        (else_try),
	          (eq, ":quest_no", "qst_deal_with_night_bandits"),
                  ##diplomacy start+ 
                  #re-enable quest at all levels for variety
	          #(is_between, ":player_level", 0, 15),
                  ##diplomacy end+
	          (is_between, ":giver_center_no", centers_begin, centers_end),
	          (party_slot_ge, ":giver_center_no", slot_center_has_bandits, 1),
	          (assign, ":quest_target_center", ":giver_center_no"),
	          (assign, ":quest_expiration_days", 4),
	          (assign, ":quest_dont_give_again_period", 15),
                  ##diplomacy start+
                  (try_begin),
                   #To avoid being pestered with trivia, increase :quest_dont_give_again_period with the player's level
                     (ge, ":player_level", 15),
                     (store_add, ":quest_dont_give_again_period", ":player_level", 1),
                  (try_end),
                  ##diplomacy end+
	          (assign, ":result", ":quest_no"),
	        (else_try),
	          # Lady quests
	          (eq, ":quest_no", "qst_rescue_lord_by_replace"),
			  (eq, 1, 0),
	          (try_begin),
	            (ge, "$g_talk_troop_faction_relation", 0),
                    ##diplomacy start+
                    #if this quest is not disabled, remove the upper level limit to increase play variety
	            #(is_between, ":player_level", 5, 25),
                    (ge, ":player_level", 5),
                    ##diplomacy end+

	            (assign, ":prisoner_relative", -1),

	            (try_begin),
                  (troop_get_slot, ":cur_target_troop", ":giver_troop", slot_troop_father), #get giver_troop's father
	              (gt, ":cur_target_troop", 0), #if giver_troop has a father as a troop in game
                  (troop_slot_ge, ":cur_target_troop", slot_troop_prisoner_of_party, 0), #if giver_troop's father is in a prison
                  (assign, ":prisoner_relative", ":cur_target_troop"),
	            (try_end),

	            (try_begin),
	              (eq, ":prisoner_relative", -1), #if giver_troop has no father or giver_troop's father is not in prison.
	              (troop_get_slot, ":cur_target_troop", ":giver_troop", slot_troop_spouse), #get giver_troop's spouse
	              (gt, ":cur_target_troop", 0), #if giver_troop has a spouse as a troop in game
                  (troop_slot_ge, ":cur_target_troop", slot_troop_prisoner_of_party, 0), #if giver_troop's spouse is in a prison
	              (assign, ":prisoner_relative", ":cur_target_troop"),
				(try_end),

	            (try_begin),
	              (eq, ":prisoner_relative", -1), #if ((giver_troop has no father) or (giver_troop's father is not in prison)) and ((giver_troop has no spouse) or (giver_troop's spouse is not in prison)).
	              (troop_get_slot, ":cur_target_troop", ":giver_troop", slot_troop_guardian), #get giver_troop's spouse
	              (gt, ":cur_target_troop", 0), #if giver_troop has a guardian as a troop in game
                  (troop_slot_ge, ":cur_target_troop", slot_troop_prisoner_of_party, 0), #if giver_troop's guardian is in a prison
	              (assign, ":prisoner_relative", ":cur_target_troop"),
				(try_end),

				(try_begin),
				  (eq, "$cheat_mode", 1),
				  (assign, reg0, ":prisoner_relative"),
				  (display_message, "str_prisoner_relative_is_reg0"),
				(try_end),

				(gt, ":prisoner_relative", -1),
	            #(changed 2) no need to this anymore (troop_slot_ge, ":prisoner_relative", slot_troop_prisoner_of_party, 0),
	            (call_script, "script_search_troop_prisoner_of_party", ":prisoner_relative"),
	            (assign, ":cur_target_center", reg0),

	            #(changed 3) no need to check only towns anymore (is_between, ":cur_target_center", towns_begin, towns_end),#Skip if he is not in a town
	            (is_between, ":cur_target_center", walled_centers_begin, walled_centers_end), #Skip if he is not in a walled center

	            (assign, ":quest_target_center", ":cur_target_center"),
	            (assign, ":quest_target_troop", ":prisoner_relative"),
	            (assign, ":quest_expiration_days", 30),
	            (assign, ":quest_dont_give_again_period", 73),
	            (assign, ":result", ":quest_no"),
	          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_deliver_message_to_prisoner_lord"),
			  ##diplomacy start+ enable this quest even when a vassal from an affiliated family member
			  ##...or from a faction leader, a faction marshall, or your spouse
			  (this_or_next|ge, ":is_close", 1),
			  (this_or_next|ge, ":nominal_superior", 1),
			  ##diplomacy end+
			  (eq, "$player_has_homage", 0),

	          (try_begin),
	            (ge, "$g_talk_troop_faction_relation", 0),
				##diplomacy start+
				#Remove the upper level limit to increase play variety
	            #(is_between, ":player_level", 5, 25),
				(ge, ":player_level", 5),
				##diplomacy end+
	            (troop_get_slot, ":cur_target_troop", ":giver_troop", slot_troop_father),
	            (try_begin),
	              (eq, ":cur_target_troop", 0),
	              (troop_get_slot, ":cur_target_troop", ":giver_troop", slot_troop_spouse),
	            (try_end),
	            #(troop_slot_eq, ":cur_target_troop", slot_troop_is_prisoner, 1),#Skip if the lady's father/husband is not in prison
				(gt, ":cur_target_troop", -1),
	            (troop_slot_ge, ":cur_target_troop", slot_troop_prisoner_of_party, 0),
	            (call_script, "script_search_troop_prisoner_of_party", ":cur_target_troop"),
	            (assign, ":cur_target_center", reg0),
	            (is_between, ":cur_target_center", towns_begin, towns_end),#Skip if he is not in a town
	            (assign, ":quest_target_center", ":cur_target_center"),
	            (assign, ":quest_target_troop", ":cur_target_troop"),
	            (assign, ":quest_expiration_days", 30),
	            (assign, ":quest_dont_give_again_period", 30),
	            (assign, ":result", ":quest_no"),
	          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_duel_for_lady"),
	          (try_begin),
	            (ge, "$g_talk_troop_faction_relation", 0),
	            (ge, ":player_level", 10),
	            (call_script, "script_cf_troop_get_random_enemy_troop_with_occupation", ":giver_troop", slto_kingdom_hero),#Can fail
	            (assign, ":cur_target_troop", reg0),
	            (neg|troop_slot_eq, ":giver_troop", slot_troop_spouse, ":cur_target_troop"), #must not be in the family
	            (neg|troop_slot_eq, ":giver_troop", slot_troop_father, ":cur_target_troop"),
	            (neg|troop_slot_ge, ":cur_target_troop", slot_troop_prisoner_of_party, 0),
	            (troop_slot_ge, ":cur_target_troop", slot_troop_leaded_party, 0),

                ##diplomacy start+ add benefactor ~ goodnatured/upstanding equivalence
                (neg|troop_slot_eq, ":cur_target_troop", slot_lord_reputation_type, lrep_benefactor),
                #also disable challenging conventional & moralist ladies
                (neg|troop_slot_eq, ":cur_target_troop", slot_lord_reputation_type, lrep_conventional),
                (neg|troop_slot_eq, ":cur_target_troop", slot_lord_reputation_type, lrep_moralist),
                #diplomacy end+
	            (neg|troop_slot_eq, ":cur_target_troop", slot_lord_reputation_type, lrep_goodnatured),
	            (neg|troop_slot_eq, ":cur_target_troop", slot_lord_reputation_type, lrep_upstanding),
	            (neg|troop_slot_eq, ":cur_target_troop", slot_lord_reputation_type, lrep_martial),

	            (assign, ":quest_target_troop", ":cur_target_troop"),
	            (assign, ":quest_expiration_days", 30),
	            (assign, ":quest_dont_give_again_period", 50),
	            (assign, ":result", ":quest_no"),
	          (try_end),
	          # Enemy Lord Quests
	        (else_try),
	          (eq, ":quest_no", "qst_lend_surgeon"),
	          (try_begin),
	            (eq, "$g_defending_against_siege", 0),#Skip if the center is under siege (because of resting)
				##diplomacy start+
				#also disable for roguish lords with negative tmt_humanitarian ratings
				(call_script, "script_dplmc_get_troop_morality_value", ":giver_troop", tmt_humanitarian),
				(this_or_next|neq, ":giver_reputation", lrep_roguish),
					(lt, reg0, 0),
            #Disable for anyone with a negative tmt_egalitarian rating, as this would be out of character.
				(call_script, "script_dplmc_get_troop_morality_value", ":giver_troop", tmt_egalitarian),
				(ge, reg0, 0),
				##diplomacy end+
	            (neq, ":giver_reputation", lrep_quarrelsome),
	            (neq, ":giver_reputation", lrep_debauched),
	            (assign, ":max_surgery_level", 0),
	            (assign, ":best_surgeon", -1),
	            (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
	            (try_for_range, ":i_stack", 1, ":num_stacks"),
	              (party_stack_get_troop_id, ":stack_troop","p_main_party",":i_stack"),
	              (troop_is_hero, ":stack_troop"),
	              (store_skill_level, ":cur_surgery_skill", skl_surgery, ":stack_troop"),
	              (gt, ":cur_surgery_skill", ":max_surgery_level"),
	              (assign, ":max_surgery_level", ":cur_surgery_skill"),
	              (assign, ":best_surgeon", ":stack_troop"),
	            (try_end),

	            (store_character_level, ":cur_level", "trp_player"),
	            (assign, ":required_skill", 5),
	            (val_div, ":cur_level", 10),
	            (val_add, ":required_skill", ":cur_level"),
	            (ge, ":max_surgery_level", ":required_skill"), #Skip if party skill level is less than the required value

	            (assign, ":quest_object_troop", ":best_surgeon"),
	            (assign, ":quest_importance", 1),
	            (assign, ":quest_xp_reward", 10),
	            (assign, ":quest_gold_reward", 10),
	            (assign, ":quest_dont_give_again_period", 50),
	            (assign, ":result", ":quest_no"),
	          (try_end),
	          # Lord Quests
	        (else_try),
	          (eq, ":quest_no", "qst_meet_spy_in_enemy_town"),
			  ##diplomacy start+ enable this quest even when a vassal from an affiliated family member
			  #...or from a faction leader, a faction marshall, or your spouse
			  (this_or_next|ge, ":is_close", 1),
			  (this_or_next|ge, ":nominal_superior", 1),
			  ##diplomacy end+
			  (eq, "$player_has_homage", 0),

	          (try_begin),
	            (eq, "$players_kingdom", ":giver_faction_no"),
	            (neq, ":giver_reputation", lrep_goodnatured),
	            (neq, ":giver_reputation", lrep_martial),

	            (call_script, "script_troop_get_player_relation", ":giver_troop"),
	            (assign, ":giver_relation", reg0),
	            (gt, ":giver_relation", 3),
	            (call_script, "script_cf_faction_get_random_enemy_faction", ":giver_faction_no"),
	            (assign, ":enemy_faction", reg0),
	            (store_relation, ":reln", ":enemy_faction", "fac_player_supporters_faction"),
	            (lt, ":reln", 0),
	            (call_script, "script_cf_select_random_town_with_faction", ":enemy_faction"),
	            (assign, ":cur_target_center", reg0),
	            #Just to make sure that there is a free walker
	            (call_script, "script_cf_center_get_free_walker", ":cur_target_center"),
	            (assign, ":quest_target_center", ":cur_target_center"),
	            (store_random_in_range, ":quest_target_amount", secret_signs_begin, secret_signs_end),
	            (assign, ":result", ":quest_no"),
	            (assign, ":quest_gold_reward", 500),
	            (assign, ":quest_expiration_days", 30),
	            (assign, ":quest_dont_give_again_period", 50),
	            (quest_set_slot, "qst_meet_spy_in_enemy_town", slot_quest_gold_reward, 500),
	          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_raid_caravan_to_start_war"),
			  (eq, 1, 0), #disable this as a random quest

	          (try_begin),
	            (eq, "$players_kingdom", ":giver_faction_no"),
                ##diplomacy start+
				#no lords who are opposed to raiding will suggest this, even if they match
				#one of the listed personalities.
				(call_script, "script_dplmc_get_troop_morality_value", ":giver_troop", tmt_humanitarian),
				(lt, reg0, 1),
				#roguish lords can give this quest unless they're opposed to raiding
	            (this_or_next|eq, ":giver_reputation", lrep_roguish),
                ##diplomacy end+
	            (this_or_next|eq, ":giver_reputation", lrep_cunning),
	            (this_or_next|eq, ":giver_reputation", lrep_quarrelsome),
	            (             eq, ":giver_reputation", lrep_debauched),
	            (gt, ":player_level", 10),
				(eq, 1, 0), #disable this as a random quest

	            (neg|faction_slot_eq, ":giver_faction_no", slot_faction_leader, ":giver_troop"),#Can not take the quest from the king
	            (call_script, "script_cf_faction_get_random_friendly_faction", ":giver_faction_no"),#Can fail
	            (assign, ":quest_target_faction", reg0),
	            (store_troop_faction, ":quest_object_faction", ":giver_troop"),
				##Floris MTT begin
				(try_begin),
		 			(eq, "$troop_trees", troop_trees_0),
					(assign, ":quest_target_party_template", "pt_kingdom_caravan_party"),
				(else_try),
		 			(eq, "$troop_trees", troop_trees_1),
					(assign, ":quest_target_party_template", "pt_kingdom_caravan_party_r"),
				(else_try),
					(eq, "$troop_trees", troop_trees_2),
					(assign, ":quest_target_party_template", "pt_kingdom_caravan_party_e"),
				(try_end),
				##Floris MTT end
	            (assign, ":quest_target_amount", 2),
	            (assign, ":result", ":quest_no"),
	            (assign, ":quest_expiration_days", 30),
	            (assign, ":quest_dont_give_again_period", 100),
	          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_deliver_message"),
			  ##diplomacy start+ enable this quest even when a vassal from an affiliated family member
			  #...or from a faction leader, a faction marshall, or your spouse
			  (this_or_next|ge, ":is_close", 1),
			  (this_or_next|ge, ":nominal_superior", 1),
			  ##diplomacy end+
			  (eq, "$player_has_homage", 0),

	          (try_begin),
	            (ge, "$g_talk_troop_faction_relation", 0),
				##diplomacy start+
				#increase the level/renown range validity of this quest
	            #(lt, ":player_level", 20),
			    #(neg|troop_slot_ge, "trp_player", slot_troop_renown, 125),
				(store_character_level, reg0, ":giver_troop"),
				(val_max, reg0, 20),#20 or quest-giver's level, whichever is greater
				(lt, ":player_level", reg0),
				(troop_get_slot, reg0, ":giver_troop", slot_troop_renown),
				(val_div, reg0, 2),
				(val_max, reg0, 125),#125 or 50% of quest-giver's renown, whichever is greater
				##diplomacy end+
	            (call_script, "script_cf_get_random_lord_in_a_center_with_faction", ":giver_faction_no"),#Can fail
	            (assign, ":cur_target_troop", reg0),
	            (neq, ":cur_target_troop", ":giver_troop"),#Skip himself
	            (call_script, "script_get_troop_attached_party", ":cur_target_troop"),
	            (assign, ":cur_target_center", reg0),#cur_target_center will definitely be a valid center
	            (neq,":giver_center_no", ":cur_target_center"),#Skip current center

	            (assign, ":quest_target_center", ":cur_target_center"),
	            (assign, ":quest_target_troop", ":cur_target_troop"),
	            (assign, ":quest_xp_reward", 30),
	            (assign, ":quest_gold_reward", 40),
	            (assign, ":quest_dont_give_again_period", 10),
				##diplomacy start+
				(try_begin),
					(this_or_next|troop_slot_ge, "trp_player", slot_troop_renown, 125),
						(ge, ":player_level", 20),
					(assign, ":quest_dont_give_again_period", ":player_level"),
					(val_clamp, ":quest_dont_give_again_period", 10, 61),
				(try_end),
				##diplomacy end+

	            (assign, ":result", ":quest_no"),

	            (assign, ":quest_expiration_days", 30),
	          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_escort_lady"),
	          (try_begin),
	            (ge, "$g_talk_troop_faction_relation", 0),
	            (ge, ":player_level", 10),
				(ge, ":giver_troop", 0), #skip troops without fathers in range				

				(assign, ":cur_object_troop", -1),
                (try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
				  (troop_slot_eq, ":lady", slot_troop_father, ":giver_troop"),
				  (assign, ":cur_object_troop", ":lady"),
				(try_end),

				(ge, ":cur_object_troop", 0),
							
				(troop_get_slot, ":giver_troop_confirm", ":cur_object_troop", slot_troop_father),  # just to make sure
				(eq, ":giver_troop", ":giver_troop_confirm"), # just to make sure
				(store_random_in_range, ":random_no", 0, 2),
	            (try_begin),
	              (eq, ":random_no", 0),
	              (troop_get_slot, ":cur_object_troop_2", ":giver_troop", slot_troop_spouse),
	              (is_between, ":cur_object_troop_2", kingdom_ladies_begin, kingdom_ladies_end),
				  (troop_get_slot, ":giver_troop_confirm", ":cur_object_troop_2", slot_troop_spouse),  # just to make sure
				  (eq, ":giver_troop", ":giver_troop_confirm"), # just to make sure
	              (assign, ":cur_object_troop", ":cur_object_troop_2"),
	            (try_end),
	            (gt, ":cur_object_troop", 0),#Skip lords without a lady
				##diplomacy start+ use a script for gender
	            #(troop_get_type, ":cur_troop_gender", ":cur_object_troop"),
				(call_script, "script_dplmc_store_troop_is_female", ":cur_object_troop"),
				(assign, ":cur_troop_gender", reg0),
	            #(eq, ":cur_troop_gender", 1),#Skip if it is not female
				(neq, ":cur_troop_gender", 0),
				##diplomacy end+
	            (gt, ":giver_center_no", 0),#Skip if lord is outside the center
	            (troop_slot_eq, ":cur_object_troop", slot_troop_cur_center, ":giver_center_no"),#Skip if the lady is not at the same center
	            (call_script, "script_cf_select_random_town_with_faction", ":giver_faction_no"),#Can fail
	            (assign, ":cur_target_center", reg0),
	            (neq, ":cur_target_center", ":giver_center_no"),
	            (hero_can_join),#Skip if player has no available slots

	            (assign, ":quest_object_troop", ":cur_object_troop"),
	            (assign, ":quest_target_center", ":cur_target_center"),
	            (assign, ":quest_expiration_days", 20),
	            (assign, ":quest_dont_give_again_period", 30),
	            (assign, ":result", ":quest_no"),
	          (try_end),
##        (else_try),
##          (eq, ":quest_no", "qst_hunt_down_raiders"),
##          (try_begin),
##            (gt, ":player_level", 10),
##            (faction_slot_eq, ":giver_faction_no", slot_faction_leader, ":giver_troop"),
##            (call_script, "script_cf_select_random_town_with_faction", ":giver_faction_no"),#Can fail
##            (assign, ":cur_object_center", reg0),
##            (neq, ":cur_object_center", ":giver_center_no"),#Skip current center
##            (call_script, "script_get_random_enemy_center", ":giver_party_no"),
##            (assign, ":cur_target_center", reg0),
##            (ge, ":cur_target_center", 0),
##            (store_faction_of_party, ":cur_target_faction", ":cur_target_center"),
##            (is_between,  ":cur_target_faction", kingdoms_begin, kingdoms_end),
##
##            (assign, ":quest_object_center", ":cur_object_center"),
##            (assign, ":quest_target_center", ":cur_target_center"),
##            (assign, ":quest_importance", 1),
##            (assign, ":quest_xp_reward", 1500),
##            (assign, ":quest_gold_reward", 1000),
##            (assign, ":result", ":quest_no"),
##          (try_end),
##        (else_try),
##          (eq, ":quest_no", "qst_bring_back_deserters"),
##          (try_begin),
##            (gt, ":player_level", 5),
##            (faction_get_slot, ":cur_target_party_template", ":giver_faction_no", slot_faction_deserter_party_template),
##            (faction_get_slot, ":cur_target_troop", ":giver_faction_no", slot_faction_deserter_troop),
##            (gt, ":cur_target_party_template", 0),#Skip factions with no deserter party templates
##            (store_num_parties_of_template, ":num_deserters", ":cur_target_party_template"),
##            (ge, ":num_deserters", 2),#Skip if there are less than 2 active deserter parties
##
##            (assign, ":quest_target_troop", ":cur_target_troop"),
##            (assign, ":quest_target_party_template", ":cur_target_party_template"),
##            (assign, ":quest_target_amount", 5),
##            (assign, ":quest_importance", 1),
##            (assign, ":quest_xp_reward", 500),
##            (assign, ":quest_gold_reward", 300),
##            (assign, ":result", ":quest_no"),
##          (try_end),
##        (else_try),
##          (eq, ":quest_no", "qst_deliver_supply_to_center_under_siege"),
##          (try_begin),
##            (gt, ":player_level", 10),
##            (gt, ":giver_center_no", 0),#Skip if lord is outside the center
##            (call_script, "script_cf_get_random_siege_location_with_faction", ":giver_faction_no"),#Can fail
##            (assign, ":quest_target_center", reg0),
##            (assign, ":quest_target_amount", 10),
##            (assign, ":quest_importance", 1),
##            (assign, ":quest_xp_reward", 500),
##            (assign, ":quest_gold_reward", 300),
##            (assign, ":result", ":quest_no"),
##          (try_end),
##        (else_try),
##          (eq, ":quest_no", "qst_rescue_lady_under_siege"),
##          (try_begin),
##            (gt, ":player_level", 15),
##            (troop_get_slot, ":cur_object_troop", ":giver_troop", slot_troop_daughter),
##            (store_random_in_range, ":random_no", 0, 2),
##            (try_begin),
##              (this_or_next|eq,  ":cur_object_troop", 0),
##              (eq, ":random_no", 0),
##              (troop_get_slot, ":cur_object_troop_2", ":giver_troop", slot_troop_spouse),
##              (gt, ":cur_object_troop_2", 0),
##              (assign, ":cur_object_troop", ":cur_object_troop_2"),
##            (try_end),
##            (gt, ":cur_object_troop", 0),#Skip lords without a lady
##            (troop_get_type, ":cur_troop_gender", ":cur_object_troop"),
##            (eq, ":cur_troop_gender", 1),#Skip if lady is not female
##            (troop_get_slot, ":cur_target_center", ":cur_object_troop", slot_troop_cur_center),
##            (is_between, ":cur_target_center", centers_begin, centers_end),#Skip if she is not in a center
##            (neq,":giver_center_no", ":cur_target_center"),#Skip current center
##            (call_script, "script_cf_get_random_siege_location_with_faction", ":giver_faction_no"),#Can fail
##            (assign, ":cur_target_center", reg0),
##            (troop_set_slot, ":cur_object_troop", slot_troop_cur_center, ":cur_target_center"),#Move lady to the siege location
##            (assign, ":quest_object_troop", ":cur_object_troop"),
##            (assign, ":quest_target_center", ":cur_target_center"),
##            (assign, ":quest_target_troop", ":giver_troop"),
##            (assign, ":quest_importance", 1),
##            (assign, ":quest_xp_reward", 200),
##            (assign, ":quest_gold_reward", 750),
##            (assign, ":result", ":quest_no"),
##          (try_end),
##        (else_try),
##          (eq, ":quest_no", "qst_deliver_message_to_lover"),
##          (try_begin),
##            (is_between, ":player_level", 5, 30),
##            (troop_get_slot, ":cur_target_troop", ":giver_troop", slot_troop_lover),
##            (gt, ":cur_target_troop", 0),#Skip lords without a lover
##            (troop_get_slot, ":cur_target_center", ":cur_target_troop", slot_troop_cur_center),
##            (is_between, ":cur_target_center", centers_begin, centers_end),#Skip if she is not in a center
##            (neq,":giver_center_no", ":cur_target_center"),#Skip current center
##            (assign, ":quest_target_troop", ":cur_target_troop"),
##            (assign, ":quest_target_center", ":cur_target_center"),
##            (assign, ":result", ":quest_no"),
##          (try_end),
##        (else_try),
##          (eq, ":quest_no", "qst_bring_reinforcements_to_siege"),
##          (try_begin),
##            (gt, ":player_level", 10),
##            (call_script, "script_cf_get_random_siege_location_with_attacker_faction", ":giver_faction_no"),#Can fail
##            (assign, ":cur_target_center", reg0),
##            (store_random_in_range, ":random_no", 5, 11),
##            (troops_can_join, ":random_no"),#Skip if the player doesn't have enough room
##            (call_script, "script_cf_get_number_of_random_troops_from_party", ":giver_party_no", ":random_no"),#Can fail
##            (assign, ":cur_object_troop", reg0),
##            (party_get_battle_opponent, ":cur_target_party", ":cur_target_center"),
##            (party_get_num_companion_stacks, ":num_stacks", ":cur_target_party"),
##            (gt, ":num_stacks", 0),#Skip if the besieger party has no troops
##            (party_stack_get_troop_id, ":cur_target_troop", ":cur_target_party", 0),
##            (troop_is_hero, ":cur_target_troop"),#Skip if the besieger party has no heroes
##            (neq, ":cur_target_troop", ":giver_troop"),#Skip if the quest giver is the same troop
##            (assign, ":quest_target_troop", ":cur_target_troop"),
##            (assign, ":quest_object_troop", ":cur_object_troop"),
##            (assign, ":quest_target_party", ":cur_target_party"),
##            (assign, ":quest_target_center", ":cur_target_center"),
##            (assign, ":quest_target_amount", ":random_no"),
##            (assign, ":quest_importance", 1),
##            (assign, ":quest_xp_reward", 400),
##            (assign, ":quest_gold_reward", 200),
##            (assign, ":result", ":quest_no"),
##          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_deliver_message_to_enemy_lord"),
	          (try_begin),
	            (ge, "$g_talk_troop_faction_relation", 0),
				##diplomacy start+
				#remove upper level limit to increase play variety
	            #(is_between, ":player_level", 5,25),
				(ge, ":player_level", 5),
				##diplomacy end+
	            (call_script, "script_cf_get_random_lord_from_another_faction_in_a_center", ":giver_faction_no"),#Can fail
	            (assign, ":cur_target_troop", reg0),
	            (call_script, "script_get_troop_attached_party", ":cur_target_troop"),
	            (assign, ":quest_target_center", reg0),#quest_target_center will definitely be a valid center
	            (assign, ":quest_target_troop", ":cur_target_troop"),
	            (assign, ":quest_importance", 1),
	            (assign, ":quest_xp_reward", 200),
				##diplomacy start+
				#decrease XP reward as you exceed the maximum level
				(try_begin),
					(ge, ":player_level", 26),
					(store_sub, ":quest_xp_reward", 25, ":player_level"),
					(val_add, ":quest_xp_reward", 200),
					(val_max, ":quest_xp_reward", 50),#minus 10 xp for every level above 25, to a minimum of 50 XP at level 40
				(try_end),
				##diplomacy end+
	            (assign, ":quest_gold_reward", 0),
	            (assign, ":result", ":quest_no"),
	            (assign, ":quest_expiration_days", 40),
	          (try_end),
##        (else_try),
##          (eq, ":quest_no", "qst_bring_prisoners_to_enemy"),
##          (try_begin),
##            (gt, ":player_level", 10),
##            (is_between, ":giver_center_no", centers_begin, centers_end),#Skip if the quest giver is not at a center
##            (store_random_in_range, ":random_no", 5, 11),
##            (troops_can_join_as_prisoner, ":random_no"),#Skip if the player doesn't have enough room
##            (call_script, "script_get_random_enemy_town", ":giver_center_no"),
##            (assign, ":cur_target_center", reg0),
##            (ge, ":cur_target_center", 0),#Skip if there are no enemy towns
##            (store_faction_of_party, ":cur_target_faction", ":cur_target_center"),
##            (faction_get_slot, ":cur_object_troop", ":cur_target_faction", slot_faction_tier_5_troop),
##            (assign, ":quest_target_center", ":cur_target_center"),
##            (assign, ":quest_object_troop", ":cur_object_troop"),
##            (assign, ":quest_target_amount", ":random_no"),
##            (assign, ":quest_importance", 1),
##            (assign, ":quest_xp_reward", 300),
##            (assign, ":quest_gold_reward", 200),
##            (assign, ":result", ":quest_no"),
##          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_deal_with_bandits_at_lords_village"),
	          (try_begin),
			    ##diplomacy start+
				#Does not have negative "tmt_humanitarian" rating
				(call_script, "script_dplmc_get_troop_morality_value", ":giver_troop", tmt_humanitarian),
				(ge, reg0, 0),
				##diplomacy end+
	            (neq, ":giver_reputation", lrep_debauched),
	            (neq, ":giver_reputation", lrep_quarrelsome),
	            (ge, "$g_talk_troop_faction_relation", 0),
	            (assign, ":end_cond", villages_end),
	            (assign, ":cur_target_center", -1),
	            (try_for_range, ":cur_village", villages_begin, ":end_cond"),
	              (party_slot_eq, ":cur_village", slot_town_lord, ":giver_troop"),
	              (party_slot_eq, ":cur_village", slot_village_infested_by_bandits, 1),
	              (party_slot_eq, ":cur_village", slot_village_state, svs_normal),
	              (assign, ":cur_target_center", ":cur_village"),
	              (assign, ":end_cond", 0),
	            (try_end),
	            (ge, ":cur_target_center", 0),
	            (neg|check_quest_active, "qst_eliminate_bandits_infesting_village"),
	            (assign, ":quest_target_center", ":cur_target_center"),
	            (assign, ":result", ":quest_no"),
	            (assign, ":quest_expiration_days", 30),
	          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_raise_troops"),
	          (try_begin),
	            (neq, ":giver_reputation", lrep_martial),
				##diplomacy start+
				#RE-ENABLE for player's faction
	            #(neq, ":giver_faction_no", "fac_player_supporters_faction"), #we need tier_1_troop a valid value
				(assign, ":faction_for_troop", ":giver_faction_no"),
				(try_begin),
					(eq, ":giver_faction_no", "fac_player_supporters_faction"),
					(assign, ":faction_for_troop", "$g_player_culture"),
					(neg|is_between, ":faction_for_troop", npc_kingdoms_begin, npc_kingdoms_end),
					(troop_get_slot, ":faction_for_troop", ":giver_troop", slot_troop_original_faction),
				(try_end),
				(is_between, ":faction_for_troop", npc_kingdoms_begin, npc_kingdoms_end), #we need tier_1_troop a valid value
				##diplomacy end+
	            (ge, "$g_talk_troop_faction_relation", 0),
	            (store_character_level, ":cur_level", "trp_player"),
	            (gt, ":cur_level", 5),
	            (troop_slot_ge, "trp_player", slot_troop_renown, 100),

	            (store_random_in_range, ":quest_target_amount", 5, 8),
	            (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
	            (le, ":quest_target_amount", ":free_capacity"),
	            (faction_get_slot, ":quest_object_troop", ":giver_faction_no", slot_faction_tier_1_troop),
	            (store_random_in_range, ":level_up", 20, 40),
	            (val_add, ":level_up", ":cur_level"),
	            (val_div, ":level_up", 10),

	            (store_mul, ":quest_gold_reward", ":quest_target_amount", 10),

	            (assign, ":quest_target_troop", ":quest_object_troop"),
	            (try_for_range, ":unused", 0, ":level_up"),
	              (troop_get_upgrade_troop, ":level_up_troop", ":quest_target_troop", 0),
	              (gt, ":level_up_troop", 0),
	              (assign, ":quest_target_troop", ":level_up_troop"),
				  ##diplomacy start+ Fix what appears to be a native bug,
	              #(val_mul, ":quest_gold_reward", ":quest_gold_reward", 7),
	              #(val_div, ":quest_gold_reward", ":quest_gold_reward", 4),
				  (val_mul, ":quest_gold_reward", 7),
				  (val_div, ":quest_gold_reward", 4),
				  ##diplomacy end+
	            (try_end),

	            (assign, ":quest_xp_reward", ":quest_gold_reward"),
	            (val_mul, ":quest_xp_reward", 3),
	            (val_div, ":quest_xp_reward", 10),
	            (assign, ":result", ":quest_no"),
	            (assign, ":quest_expiration_days", 120),
	            (assign, ":quest_dont_give_again_period", 15),
	          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_collect_taxes"),
			  ##diplomacy start+ enable this quest even when a vassal,
   			  #if the quest giver is an affiliated family member
			  #...or from the faction leader, the faction marshall, or your spouse
			  (this_or_next|ge, ":is_close", 1),
			  (this_or_next|ge, ":nominal_superior", 1),
			  ##diplomacy end+
			  (eq, "$player_has_homage", 0),

	          (try_begin),
                ##diplomacy start+ benefactor lords do not give tax-collection quest because good-natured/upstanding do not
	            (neq, ":giver_reputation", lrep_benefactor),
				#neither do certain lady personalities either (only ambitious do)
				(neg|is_between, ":giver_reputation", lrep_conventional, lrep_ambitious),
				(neq, ":giver_reputation", lrep_moralist),
                ##diplomacy end+
	            (neq, ":giver_reputation", lrep_goodnatured),
	            (neq, ":giver_reputation", lrep_upstanding),
	            (ge, "$g_talk_troop_faction_relation", 0),
	            (call_script, "script_cf_troop_get_random_leaded_town_or_village_except_center", ":giver_troop", ":giver_center_no"),
	            (assign, ":quest_target_center", reg0),
	            (assign, ":quest_importance", 1),
	            (assign, ":quest_gold_reward", 0),
	            (assign, ":quest_xp_reward", 100),
	            (assign, ":result", ":quest_no"),
	            (assign, ":quest_expiration_days", 50),
	            (assign, ":quest_dont_give_again_period", 20),
	          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_hunt_down_fugitive"),
	          (try_begin),
	            (ge, "$g_talk_troop_faction_relation", 0),
	            (call_script, "script_cf_select_random_village_with_faction", ":giver_faction_no"),
	            (assign, ":quest_target_center", reg0),
	            (store_random_in_range, ":quest_target_dna", 0, 1000000),
	            (assign, ":result", ":quest_no"),
	            (assign, ":quest_expiration_days", 30),
	            (assign, ":quest_dont_give_again_period", 30),
	          (try_end),
##        (else_try),
##          (eq, ":quest_no", "qst_capture_messenger"),
##          (try_begin),
##            (call_script, "script_cf_faction_get_random_enemy_faction", ":giver_faction_no"),
##            (assign, ":cur_target_faction", reg0),
##            (faction_get_slot, ":cur_target_troop", ":cur_target_faction", slot_faction_messenger_troop),
##            (gt, ":cur_target_troop", 0),#Checking the validiy of cur_target_troop
##            (store_num_parties_destroyed_by_player, ":quest_target_amount", "pt_messenger_party"),
##
##            (assign, ":quest_target_troop", ":cur_target_troop"),
##            (assign, ":quest_target_party_template", ":cur_target_party_template"),
##            (assign, ":quest_importance", 1),
##            (assign, ":quest_xp_reward", 700),
##            (assign, ":quest_gold_reward", 400),
##            (assign, ":result", ":quest_no"),
##          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_kill_local_merchant"),
			  ##diplomacy start+ enable this quest even when a vassal from an affiliated family member or your spouse
			  (this_or_next|ge, ":is_close", 1),
			  ##diplomacy end+
			  (eq, "$player_has_homage", 0),

	          (try_begin),
                ##diplomacy start+
				#Lords who dislike breaking deals do not give this quest
				(call_script, "script_dplmc_get_troop_morality_value", ":giver_troop", tmt_honest),
				(lt, reg0, 1),
				#Roguish lords can give the Kill Local Merchant quest, unless they dislike murder.
				(call_script, "script_dplmc_get_troop_morality_value", ":giver_troop", tmt_humanitarian),
	            (this_or_next|neq, ":giver_reputation", lrep_roguish),
					(lt, reg0, 1),
				#Ambitious ladies can give this quest
				(this_or_next|eq, ":giver_reputation", lrep_ambitious),
				(this_or_next|eq, ":giver_reputation", lrep_roguish),
                ##diplomacy end+
	            (this_or_next|eq, ":giver_reputation", lrep_quarrelsome),
	            (this_or_next|eq, ":giver_reputation", lrep_cunning),
	            (             eq, ":giver_reputation", lrep_debauched),
	            (neg|faction_slot_eq, ":giver_faction_no", slot_faction_leader, ":giver_troop"),#Can not take the quest from the king
	            (ge, "$g_talk_troop_faction_relation", 0),
	            (gt, ":player_level", 5),
	            (is_between, ":giver_center_no", towns_begin, towns_end),
	            (assign, ":quest_importance", 1),
	            (assign, ":quest_xp_reward", 300),
	            (assign, ":quest_gold_reward", 1000),
	            (assign, ":result", ":quest_no"),
	            (assign, ":quest_expiration_days", 10),
	            (assign, ":quest_dont_give_again_period", 30),
	          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_bring_back_runaway_serfs"),
	          (try_begin),
                ##diplomacy start+
				#companions who have compassion for commoners do not give the Runaway Serfs quest
				(call_script, "script_dplmc_get_troop_morality_value", ":giver_troop", tmt_humanitarian),
				(lt, reg0, 1),
				#neither do Benefactor lords
	            (neq, ":giver_reputation", lrep_benefactor),
				#neither do most lady personalities (only ambitious do)
				(neg|is_between, ":giver_reputation", lrep_conventional, lrep_ambitious),
				(neq, ":giver_reputation", lrep_moralist),
                ##diplomacy end+
	            (neq, ":giver_reputation", lrep_goodnatured),
	            (neq, ":giver_reputation", lrep_upstanding),
	            (ge, "$g_talk_troop_faction_relation", 0),
	            (ge, ":player_level", 5),
	            (gt, ":giver_center_no", 0),#Skip if lord is outside the center
	            (eq, "$g_defending_against_siege", 0),#Skip if the center is under siege (because of resting)

	            (assign, ":cur_object_center", -1),
	            (try_for_range, ":cur_village", villages_begin, villages_end),
	              (party_slot_eq, ":cur_village", slot_town_lord, ":giver_troop"),
	              (store_distance_to_party_from_party, ":dist", ":cur_village", ":giver_center_no"),
	              (lt, ":dist", 25),
	              (assign, ":cur_object_center", ":cur_village"),
	            (try_end),
	            (ge, ":cur_object_center", 0),#Skip if the quest giver is not the owner of any villages around the center
	            (call_script, "script_cf_select_random_town_with_faction", ":giver_faction_no"),
	            (assign, ":cur_target_center", reg0),
	            (neq, ":cur_target_center", ":giver_center_no"),#Skip current center
	            (store_distance_to_party_from_party, ":dist", ":cur_target_center", ":giver_center_no"),
	            (ge, ":dist", 20),
				##Floris MTT begin
				(try_begin),
		 			(eq, "$troop_trees", troop_trees_0),
					(assign, ":quest_target_party_template", "pt_runaway_serfs"),
				(else_try),
		 			(eq, "$troop_trees", troop_trees_1),
					(assign, ":quest_target_party_template", "pt_runaway_serfs_r"),
				(else_try),
					(eq, "$troop_trees", troop_trees_2),
					(assign, ":quest_target_party_template", "pt_runaway_serfs_e"),
				(try_end),
				##Floris MTT end
	            (assign, ":quest_object_center", ":cur_object_center"),
	            (assign, ":quest_target_center", ":cur_target_center"),
	            (assign, ":quest_importance", 1),
	            (assign, ":quest_xp_reward", 200),
	            (assign, ":quest_gold_reward", 150),
	            (assign, ":result", ":quest_no"),
	            (assign, ":quest_expiration_days", 30),
	            (assign, ":quest_dont_give_again_period", 20),
	            (assign, "$qst_bring_back_runaway_serfs_num_parties_returned", 0),
	            (assign, "$qst_bring_back_runaway_serfs_num_parties_fleed", 0),
	          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_follow_spy"),
			  ##diplomacy start+ enable this quest even when a vassal from an affiliated family member or your spouse
			  #or a nominal superior
			  (this_or_next|ge, ":is_close", 1),
			  (this_or_next|ge, ":nominal_superior", 1),
			  ##diplomacy end+
			  (eq, "$player_has_homage", 0),

	          (try_begin),
	            (ge, "$g_talk_troop_faction_relation", 0),
				##diplomacy start+
				#Ladies other than the ambitious do not give this quest
                                (this_or_next|lt, reg0, 0),
				(this_or_next|eq, ":giver_reputation", lrep_ambitious),
                                (neg|is_between, ":giver_reputation", lrep_conventional, lrep_moralist + 1),
                                #As the "success" dialogue refers to torture, humanitarians do not either
                                (call_script, "script_dplmc_get_troop_morality_value", ":giver_troop", tmt_humanitarian),
                                (lt, reg0, 1),
                                #This is more open to interpretation, but I will also bar custodians from
										  #this, unless they have a negative tmt_humanitarian score.
                                (this_or_next|lt, reg0, 0),
                                   (neq, ":giver_reputation", lrep_custodian),
                                (neq, ":giver_reputation", lrep_benefactor),
				##diplomacy end+
	            (neq, ":giver_reputation", lrep_goodnatured),
	            (party_get_skill_level, ":tracking_skill", "p_main_party", "skl_tracking"),
	            (ge, ":tracking_skill", 2),
	            (ge, ":player_level", 10),
	            (eq, "$g_defending_against_siege", 0), #Skip if the center is under siege (because of resting)
	            (gt, ":giver_party_no", 0), #Skip if the quest giver doesn't have a party
	            (gt, ":giver_center_no", 0), #skip if the quest giver is not in a center
	            (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town), #skip if we are not in a town.
	            (party_get_position, pos2, "p_main_party"),
	            (assign, ":min_distance", 99999),
                    (assign, ":cur_object_center", -1),
	            (try_for_range, ":unused_2", 0, 10),
	              (call_script, "script_cf_get_random_enemy_center", ":giver_party_no"),
	              (assign, ":random_object_center", reg0),
	              (party_get_position, pos3, ":random_object_center"),
	              (map_get_random_position_around_position, pos4, pos3, 6),
	              (get_distance_between_positions, ":cur_distance", pos2, pos4),
	              (lt, ":cur_distance", ":min_distance"),
	              (assign, ":min_distance", ":cur_distance"),
	              (assign, ":cur_object_center", ":random_object_center"),
	              (copy_position, pos63, pos4), #Do not change pos63 until quest is accepted
	            (try_end),
	            (gt, ":cur_object_center", 0), #Skip if there are no enemy centers

	            (assign, ":quest_object_center", ":cur_object_center"),
	            (assign, ":quest_dont_give_again_period", 50),
	            (assign, ":result", ":quest_no"),
	            (assign, "$qst_follow_spy_run_away", 0),
	            (assign, "$qst_follow_spy_meeting_state", 0),
	            (assign, "$qst_follow_spy_meeting_counter", 0),
	            (assign, "$qst_follow_spy_spy_back_in_town", 0),
	            (assign, "$qst_follow_spy_partner_back_in_town", 0),
	            (assign, "$qst_follow_spy_no_active_parties", 0),
	          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_capture_enemy_hero"),
	          (try_begin),
	            (eq, "$players_kingdom", ":giver_faction_no"),
				##diplomacy start+
				(this_or_next|ge, ":is_close", 1),
			    (this_or_next|ge, ":nominal_superior", 1),
				##diplomacy end+
	            (neg|faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
	            (ge, ":player_level", 15),
	            (call_script, "script_cf_faction_get_random_enemy_faction", ":giver_faction_no"),#Can fail
	            (assign, ":quest_target_faction", reg0),
	            (assign, ":quest_expiration_days", 30),
                ##diplomacy start+ change from 80 to 30
	            (assign, ":quest_dont_give_again_period", 30),#was 80
                ##diplomacy end+
	            (assign, ":quest_gold_reward", 2000),
	            (assign, ":result", ":quest_no"),
	          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_lend_companion"),
	          (try_begin),
	            (ge, "$g_talk_troop_faction_relation", 0),
	            (assign, ":total_heroes", 0),
	            (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
	            (try_for_range, ":i_stack", 0, ":num_stacks"),
	              (party_stack_get_troop_id, ":stack_troop","p_main_party",":i_stack"),
	              (troop_is_hero, ":stack_troop"),
	              (is_between, ":stack_troop", companions_begin, companions_end),
	              (store_character_level, ":stack_level", ":stack_troop"),
	              (ge, ":stack_level", 15),
	              (assign, ":is_quest_hero", 0),
	              (try_for_range, ":i_quest", 0, all_quests_end),
	                (check_quest_active, ":i_quest"),
	                (this_or_next|quest_slot_eq, ":i_quest", slot_quest_target_troop, ":stack_troop"),
	                (quest_slot_eq, ":i_quest", slot_quest_object_troop, ":stack_troop"),
	                (assign, ":is_quest_hero", 1),
	              (try_end),
	              (eq, ":is_quest_hero", 0),
	              (val_add, ":total_heroes", 1),
	            (try_end),
	            (gt, ":total_heroes", 0),#Skip if party has no eligible heroes
	            (store_random_in_range, ":random_hero", 0, ":total_heroes"),
	            (assign, ":total_heroes", 0),
	            (assign, ":cur_target_troop", -1),
	            (try_for_range, ":i_stack", 0, ":num_stacks"),
	              (eq, ":cur_target_troop", -1),
	              (party_stack_get_troop_id, ":stack_troop","p_main_party",":i_stack"),
	              (troop_is_hero, ":stack_troop"),
	              (is_between, ":stack_troop", companions_begin, companions_end),
	              (neq, ":stack_troop", "trp_player"),
	              (store_character_level, ":stack_level", ":stack_troop"),
	              (ge, ":stack_level", 15),
	              (assign, ":is_quest_hero", 0),
	              (try_for_range, ":i_quest", 0, all_quests_end),
	                (check_quest_active, ":i_quest"),
	                (this_or_next|quest_slot_eq, ":i_quest", slot_quest_target_troop, ":stack_troop"),
	                (quest_slot_eq, ":i_quest", slot_quest_object_troop, ":stack_troop"),
	                (assign, ":is_quest_hero", 1),
	              (try_end),
	              (eq, ":is_quest_hero", 0),
	              (val_add, ":total_heroes", 1),
	              (gt, ":total_heroes", ":random_hero"),
	              (assign, ":cur_target_troop", ":stack_troop"),
	            (try_end),
	            (is_between, ":cur_target_troop", companions_begin, companions_end),

	            (assign, ":quest_target_troop", ":cur_target_troop"),
	            (store_current_day, ":quest_target_amount"),
	            (val_add, ":quest_target_amount", 8),

	            (assign, ":quest_importance", 1),
	            (assign, ":quest_xp_reward", 300),
	            (assign, ":quest_gold_reward", 400),
	            (assign, ":result", ":quest_no"),
	            (assign, ":quest_dont_give_again_period", 30),
	          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_collect_debt"),
			  (eq, 1, 0), #disable this quest pending talk with armagan
	          (try_begin),
	            (ge, "$g_talk_troop_faction_relation", 0),
	          # Find a vassal (within the same kingdom?)
	            (call_script, "script_cf_get_random_lord_in_a_center_with_faction", ":giver_faction_no"),#Can fail
	            (assign, ":quest_target_troop", reg0),
	            (neq, ":quest_target_troop", ":giver_troop"),#Skip himself
	            (call_script, "script_get_troop_attached_party", ":quest_target_troop"),
	            (assign, ":quest_target_center", reg0),#cur_target_center will definitely be a valid center
	            (neq,":giver_center_no", ":quest_target_center"),#Skip current center

	            (assign, ":quest_xp_reward", 30),
	            (assign, ":quest_gold_reward", 40),
	            (assign, ":result", ":quest_no"),
	            (store_random_in_range, ":quest_target_amount", 6, 9),
	            (val_mul, ":quest_target_amount", 500),
	            (store_div, ":quest_convince_value", ":quest_target_amount", 5),
	            (assign, ":quest_expiration_days", 90),
	            (assign, ":quest_dont_give_again_period", 20),
	          (try_end),
##        (else_try),
##          (eq, ":quest_no", "qst_capture_conspirators"),
##          (try_begin),
##            (eq, 1,0), #TODO: disable this for now
##            (ge, ":player_level", 10),
##            (is_between, ":giver_center_no", towns_begin, towns_end),#Skip if quest giver's center is not a town
##            (party_slot_eq, ":giver_center_no", slot_town_lord, ":giver_troop"),#Skip if the current center is not ruled by the quest giver
##            (call_script, "script_cf_get_random_kingdom_hero", ":giver_faction_no"),#Can fail
##
##            (assign, ":quest_target_troop", reg0),
##            (assign, ":quest_target_center", ":giver_center_no"),
##            (assign, ":quest_importance", 1),
##            (assign, ":quest_xp_reward", 10),
##            (assign, ":quest_gold_reward", 10),
##            (assign, ":result", ":quest_no"),
##            (store_character_level, ":cur_level"),
##            (val_div, ":cur_level", 5),
##            (val_max, ":cur_level", 3),
##            (store_add, ":max_parties", 4, ":cur_level"),
##            (store_random_in_range, "$qst_capture_conspirators_num_parties_to_spawn", 4, ":max_parties"),
##            (assign, "$qst_capture_conspirators_num_troops_to_capture", 0),
##            (assign, "$qst_capture_conspirators_num_parties_spawned", 0),
##            (assign, "$qst_capture_conspirators_leave_meeting_counter", 0),
##            (assign, "$qst_capture_conspirators_party_1", 0),
##            (assign, "$qst_capture_conspirators_party_2", 0),
##            (assign, "$qst_capture_conspirators_party_3", 0),
##            (assign, "$qst_capture_conspirators_party_4", 0),
##            (assign, "$qst_capture_conspirators_party_5", 0),
##            (assign, "$qst_capture_conspirators_party_6", 0),
##            (assign, "$qst_capture_conspirators_party_7", 0),
##          (try_end),
##        (else_try),
##          (eq, ":quest_no", "qst_defend_nobles_against_peasants"),
##          (try_begin),
##            (eq, 1,0), #TODO: disable this for now
##            (ge, ":player_level", 10),
##            (is_between, ":giver_center_no", towns_begin, towns_end),#Skip if quest giver's center is not a town
##            (party_slot_eq, ":giver_center_no", slot_town_lord, ":giver_troop"),#Skip if the current center is not ruled by the quest giver
##
##            (assign, ":quest_target_center", ":giver_center_no"),
##            (assign, ":quest_importance", 1),
##            (assign, ":quest_xp_reward", 10),
##            (assign, ":quest_gold_reward", 10),
##            (assign, ":result", ":quest_no"),
##            (store_character_level, ":cur_level"),
##            (val_div, ":cur_level", 5),
##            (val_max, ":cur_level", 4),
##            (store_add, ":max_parties", 4, ":cur_level"),
##            (store_random_in_range, "$qst_defend_nobles_against_peasants_num_peasant_parties_to_spawn", 4, ":cur_level"),
##            (store_random_in_range, "$qst_defend_nobles_against_peasants_num_noble_parties_to_spawn", 4, ":cur_level"),
##            (assign, "$qst_defend_nobles_against_peasants_num_nobles_to_save", 0),
##            (assign, "$qst_defend_nobles_against_peasants_num_nobles_saved", 0),
##            (assign, "$qst_defend_nobles_against_peasants_peasant_party_1", 0),
##            (assign, "$qst_defend_nobles_against_peasants_peasant_party_2", 0),
##            (assign, "$qst_defend_nobles_against_peasants_peasant_party_3", 0),
##            (assign, "$qst_defend_nobles_against_peasants_peasant_party_4", 0),
##            (assign, "$qst_defend_nobles_against_peasants_peasant_party_5", 0),
##            (assign, "$qst_defend_nobles_against_peasants_peasant_party_6", 0),
##            (assign, "$qst_defend_nobles_against_peasants_peasant_party_7", 0),
##            (assign, "$qst_defend_nobles_against_peasants_peasant_party_8", 0),
##            (assign, "$qst_defend_nobles_against_peasants_noble_party_1", 0),
##            (assign, "$qst_defend_nobles_against_peasants_noble_party_2", 0),
##            (assign, "$qst_defend_nobles_against_peasants_noble_party_3", 0),
##            (assign, "$qst_defend_nobles_against_peasants_noble_party_4", 0),
##            (assign, "$qst_defend_nobles_against_peasants_noble_party_5", 0),
##            (assign, "$qst_defend_nobles_against_peasants_noble_party_6", 0),
##            (assign, "$qst_defend_nobles_against_peasants_noble_party_7", 0),
##            (assign, "$qst_defend_nobles_against_peasants_noble_party_8", 0),
##          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_incriminate_loyal_commander"),
			  ##diplomacy start+ enable this quest even when a vassal from an affiliated family member
			  (this_or_next|ge, ":is_close", 1),
			  ##diplomacy end+
			  (eq, "$player_has_homage", 0),

	          (try_begin),
                ##diplomacy start+ benefactors & moralists will not give this quest
	            (neq, ":giver_reputation", lrep_benefactor),
	            (neq, ":giver_reputation", lrep_moralist),
				#neither will most lady personalities (only ambitious do)
				(neg|is_between, ":giver_reputation", lrep_conventional, lrep_ambitious),
				(neq, ":giver_reputation", lrep_moralist),
				#neither will lords who dislike mistreating their own men, or who
				#are forthright in their dealings
				(call_script, "script_dplmc_get_troop_morality_value", ":giver_troop", tmt_egalitarian),
				(lt, reg0, 1),
				(call_script, "script_dplmc_get_troop_morality_value", ":giver_troop", tmt_honest),
				(lt, reg0, 1),
				#neither will other lords who dislike murder
				(call_script, "script_dplmc_get_troop_morality_value", ":giver_troop", tmt_humanitarian),
				(lt, reg0, 1),
                ##diplomacy end+
	            (neq, ":giver_reputation", lrep_upstanding),
	            (neq, ":giver_reputation", lrep_goodnatured),
	            (eq, "$players_kingdom", ":giver_faction_no"),
	            (ge, ":player_level", 10),
	            (faction_slot_eq, ":giver_faction_no", slot_faction_leader, ":giver_troop"),
	            (assign, ":try_times", 1),
	            (assign, ":found", 0),
	            (try_for_range, ":unused", 0, ":try_times"),
	              (call_script, "script_cf_faction_get_random_enemy_faction", ":giver_faction_no"),#Can fail
	              (assign, ":cur_target_faction", reg0),

	              (faction_get_slot, ":cur_target_troop", ":cur_target_faction", slot_faction_leader),
	              (assign, ":num_centerless_heroes", 0),
	              ##diplomacy start+ add support for promoted ladies
	              (try_for_range, ":cur_kingdom_hero", heroes_begin, heroes_end),#<- changed active_npcs to heroes
	              ##diplomacy end+
	                (troop_slot_eq, ":cur_kingdom_hero", slot_troop_occupation, slto_kingdom_hero),
	                #(troop_slot_eq, ":cur_kingdom_hero", slot_troop_is_prisoner, 0),
	                (neg|troop_slot_ge, ":cur_kingdom_hero", slot_troop_prisoner_of_party, 0),
	                (neq, ":cur_target_troop", ":cur_kingdom_hero"),
	                (store_troop_faction, ":cur_kingdom_hero_faction", ":cur_kingdom_hero"),
	                (eq, ":cur_target_faction", ":cur_kingdom_hero_faction"),
##                (call_script, "script_get_number_of_hero_centers", ":cur_kingdom_hero"),
##                (eq, reg0, 0),
	                (val_add, ":num_centerless_heroes", 1),
	              (try_end),
	              (gt, ":num_centerless_heroes", 0),
	              (assign, ":cur_object_troop", -1),
	              (store_random_in_range, ":random_kingdom_hero", 0, ":num_centerless_heroes"),
	              ##diplomacy start+ add support for promoted ladies
	              (try_for_range, ":cur_kingdom_hero", heroes_begin, heroes_end),#<- changed active_npcs to heroes
	              ##diplomacy end+
	                (eq, ":cur_object_troop", -1),
	                (troop_slot_eq, ":cur_kingdom_hero", slot_troop_occupation, slto_kingdom_hero),
	                (neq, ":cur_target_troop", ":cur_kingdom_hero"),
	                (store_troop_faction, ":cur_kingdom_hero_faction", ":cur_kingdom_hero"),
	                (eq, ":cur_target_faction", ":cur_kingdom_hero_faction"),
##                (call_script, "script_get_number_of_hero_centers", ":cur_kingdom_hero"),
##                (eq, reg0, 0),
	                (val_sub, ":random_kingdom_hero", 1),
	                (lt, ":random_kingdom_hero", 0),
	                (assign, ":cur_object_troop", ":cur_kingdom_hero"),
	              (try_end),

	              (assign, ":cur_target_center", -1),
	              (call_script, "script_get_troop_attached_party", ":cur_target_troop"),
	              (is_between, reg0, towns_begin, towns_end),
	              (party_slot_eq, reg0, slot_town_lord, ":cur_target_troop"),
	              (assign, ":cur_target_center", reg0),

	              (assign, ":try_times", -1),#Exit the second loop
	              (assign, ":found", 1),
	            (try_end),
	            (eq, ":found", 1),

	            (assign, "$incriminate_quest_sacrificed_troop", 0),

	            (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
	            (try_for_range, ":i_stack", 1, ":num_stacks"),
	              (eq ,"$incriminate_quest_sacrificed_troop", 0),
	              (party_stack_get_troop_id, ":stack_troop","p_main_party",":i_stack"),
	              (neg|troop_is_hero, ":stack_troop"),
	              (store_character_level, ":stack_troop_level", ":stack_troop"),
	              (ge, ":stack_troop_level", 25),
	              (assign, "$incriminate_quest_sacrificed_troop", ":stack_troop"),
	            (try_end),
	            (gt, "$incriminate_quest_sacrificed_troop", 0),

	            (assign, ":quest_target_troop", ":cur_target_troop"),
	            (assign, ":quest_object_troop", ":cur_object_troop"),
	            (assign, ":quest_target_center", ":cur_target_center"),
	            (assign, ":quest_target_faction", ":cur_target_faction"),

	            (assign, ":quest_importance", 1),
	            (assign, ":quest_xp_reward", 700),
	            (assign, ":quest_gold_reward", 1000),
	            (assign, ":result", ":quest_no"),
	            (assign, ":quest_expiration_days", 30),
	            (assign, ":quest_dont_give_again_period", 180),
	          (try_end),
	        (else_try),
	          (eq, ":quest_no", "qst_capture_prisoners"),
			  ##diplomacy start+ enable this quest even when a vassal from an affiliated family member
			  (this_or_next|ge, ":is_close", 1),
			  (this_or_next|ge, ":nominal_superior", 1),
			  ##diplomacy end+
			  (eq, "$player_has_homage", 0),

	          (try_begin),
	            (eq, "$players_kingdom", ":giver_faction_no"),
	            (call_script, "script_cf_faction_get_random_enemy_faction", ":giver_faction_no"),#Can fail
	            (assign, ":cur_target_faction", reg0),
	            (store_add, ":max_tier_no", slot_faction_tier_5_troop, 1),
	            (store_random_in_range, ":random_tier_no", slot_faction_tier_2_troop, ":max_tier_no"),
	            (faction_get_slot, ":cur_target_troop", ":cur_target_faction", ":random_tier_no"),
	            (gt, ":cur_target_troop", 0),
	            (store_random_in_range, ":quest_target_amount", 3, 7),
	            (assign, ":quest_target_troop", ":cur_target_troop"),
	            (assign, ":quest_target_faction", ":cur_target_faction"),
	            (assign, ":quest_importance", 1),
	            (store_character_level, ":quest_gold_reward", ":cur_target_troop"),
	            (val_add, ":quest_gold_reward", 5),
	            (val_mul, ":quest_gold_reward", ":quest_gold_reward"),
	            (val_div, ":quest_gold_reward", 5),
	            (val_mul, ":quest_gold_reward", ":quest_target_amount"),
	            (assign, ":quest_xp_reward", ":quest_gold_reward"),
	            (assign, ":result", ":quest_no"),
	            (assign, ":quest_expiration_days", 90),
	            (assign, ":quest_dont_give_again_period", 20),
	          (try_end),
	        (try_end),
		(try_end),
	  (try_end),
	  #end of quest finding


      (try_begin),
        (neq, ":result", -1),

        (try_begin),
          (party_is_active, ":quest_target_center"),
          (store_faction_of_party, ":quest_target_faction", ":quest_target_center"),
        (try_end),

        (quest_set_slot, ":result", slot_quest_target_troop, ":quest_target_troop"),
        (quest_set_slot, ":result", slot_quest_target_center, ":quest_target_center"),
        (quest_set_slot, ":result", slot_quest_object_troop, ":quest_object_troop"),
        (quest_set_slot, ":result", slot_quest_target_faction, ":quest_target_faction"),
        (quest_set_slot, ":result", slot_quest_object_faction, ":quest_object_faction"),
        (quest_set_slot, ":result", slot_quest_object_center, ":quest_object_center"),
        (quest_set_slot, ":result", slot_quest_target_party, ":quest_target_party"),
        (quest_set_slot, ":result", slot_quest_target_party_template, ":quest_target_party_template"),
        (quest_set_slot, ":result", slot_quest_target_amount, ":quest_target_amount"),
        (quest_set_slot, ":result", slot_quest_importance, ":quest_importance"),
        (quest_set_slot, ":result", slot_quest_xp_reward, ":quest_xp_reward"),
        (quest_set_slot, ":result", slot_quest_gold_reward, ":quest_gold_reward"),
        (quest_set_slot, ":result", slot_quest_convince_value, ":quest_convince_value"),
        (quest_set_slot, ":result", slot_quest_expiration_days, ":quest_expiration_days"),
        (quest_set_slot, ":result", slot_quest_dont_give_again_period, ":quest_dont_give_again_period"),
        (quest_set_slot, ":result", slot_quest_current_state, 0),
        (quest_set_slot, ":result", slot_quest_giver_troop, ":giver_troop"),
        (quest_set_slot, ":result", slot_quest_giver_center, ":giver_center_no"),
        (quest_set_slot, ":result", slot_quest_target_dna, ":quest_target_dna"),
        (quest_set_slot, ":result", slot_quest_target_item, ":quest_target_item"),
      (try_end),

      (assign, reg0, ":result"),
  ]),
    
    ("get_dynamic_quest",
      #Dynamic quests are rarer, more important quests
      #this is a separate script from get_quest, so that tavern keepers can scan all NPCs for quests
      [
        (store_script_param_1, ":giver_troop"),
        
	(assign, ":result", -1),
	(assign, ":relevant_troop", -1),
	(assign, ":relevant_party", -1),
	(assign, ":relevant_faction", -1),

	(try_begin),
		##diplomacy start+
		##OLD:
		#(eq, ":giver_troop", -1),
		##NEW:
		(lt, ":giver_troop", 0),
		##diplomacy end+
	(else_try),
		#1 rescue prisoner
		(neg|check_quest_active, "qst_rescue_prisoner"),
		(this_or_next|troop_slot_eq, ":giver_troop", slot_troop_occupation, slto_kingdom_hero),
			(troop_slot_eq, ":giver_troop", slot_troop_occupation, slto_kingdom_lady),

		(assign, ":target_troop", -1),
		##diplomacy start+ add support for promoted ladies
		#(try_for_range, ":possible_prisoner", active_npcs_begin, active_npcs_end),
		(try_for_range, ":possible_prisoner", heroes_begin, heroes_end),
			(this_or_next|troop_slot_eq, ":possible_prisoner", slot_troop_occupation, slto_kingdom_hero),
				(is_between, ":possible_prisoner", active_npcs_begin, active_npcs_end),
		##diplomacy end+
			(troop_get_slot, ":captor_location", ":possible_prisoner", slot_troop_prisoner_of_party),
			(is_between, ":captor_location", walled_centers_begin, walled_centers_end),
			(store_troop_faction, ":giver_troop_faction_no", ":giver_troop"),
			(store_faction_of_party, ":captor_location_faction_no", ":captor_location"),
			(store_relation, ":giver_captor_relation", ":giver_troop_faction_no", ":captor_location_faction_no"),
			(lt, ":giver_captor_relation", 0),

			(call_script, "script_troop_get_family_relation_to_troop", ":giver_troop", ":possible_prisoner"),
			##diplomacy start+
			#If optional behavior changes are enabled, allow this for more relatives.
			#(In-laws, uncles, nieces.)
		   (try_begin),
			   (ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
				(ge, reg0, 4),
				(val_max, reg0, 10),
			(else_try),
			#If the characters are related to each other, and both are
			#affiliated with the player, consider them to be close enough.
				 (ge, reg0, 1),
				 (lt, reg0, 10),
				 (call_script, "script_dplmc_is_affiliated_family_member", ":giver_troop"),
				 (ge, reg0, 1),
				 (call_script, "script_dplmc_is_affiliated_family_member", ":possible_prisoner"),
				 (ge, reg0, 1),
				 (assign, reg0, 10),
			(try_end),
			##diplomacy end+
			(ge, reg0, 10),

			(assign, ":offered_parole", 0),
			(try_begin),
				(call_script, "script_cf_prisoner_offered_parole", ":possible_prisoner"),
				(assign, ":offered_parole", 1),
			(try_end),
			(eq, ":offered_parole", 0),

			(neg|party_slot_eq, ":captor_location", slot_town_lord, "trp_player"),

			(assign, ":target_troop", ":possible_prisoner"),
			(assign, ":target_party", ":captor_location"),
		(try_end),

		(gt, ":target_troop", -1),
		(assign, ":result", "qst_rescue_prisoner"),
		(assign, ":relevant_troop", ":target_troop"),
		(assign, ":relevant_party", ":target_party"),

	(else_try),
		#2 retaliate for border incident
		(is_between, ":giver_troop", mayors_begin, mayors_end),
		(store_faction_of_troop, ":giver_faction", ":giver_troop"),

		(neg|check_quest_active, "qst_retaliate_for_border_incident"),
		(quest_slot_eq, "qst_retaliate_for_border_incident", slot_quest_dont_give_again_remaining_days, 0),
		(assign, ":target_leader", 0),

		(try_for_range, ":kingdom", "fac_kingdom_1", kingdoms_end),
			(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":giver_faction", ":kingdom"),
			(assign, ":diplomatic_status", reg0),
			(eq, ":diplomatic_status", -1),
			(assign, ":duration", reg1),
			(ge, ":duration", 10),

			##diplomacy start+ add support for promoted kingdom ladies
			#(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
			(try_for_range, ":lord", heroes_begin, heroes_end),
				(this_or_next|is_between, ":lord", active_npcs_begin, active_npcs_end),
					(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
			##diplomacy end+
				(store_faction_of_troop, ":lord_faction", ":lord"),
				(eq, ":lord_faction", ":kingdom"),

				(troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_debauched),

				(assign, ":target_leader", ":lord"),
				(assign, ":target_faction", ":kingdom"),
			(try_end),
		(try_end),
		##diplomacy start+ add support for promoted kingdom ladies
		#(is_between, ":target_leader", active_npcs_begin, active_npcs_end),
		(is_between, ":target_leader", heroes_begin, heroes_end),
		##diplomacy end+

		(assign, ":result", "qst_retaliate_for_border_incident"),
		(assign, ":relevant_troop", ":target_leader"),
		(assign, ":relevant_faction", ":target_faction"),
	(else_try), #Find bandit hideout
		(troop_slot_eq, ":giver_troop", slot_troop_occupation, slto_kingdom_hero),
		(neg|check_quest_active, "qst_destroy_bandit_lair"),
		(quest_slot_eq, "qst_destroy_bandit_lair", slot_quest_dont_give_again_remaining_days, 0),

#		(display_message, "@Checking for bandit lair quest"),
          
          (assign, ":lair_found", -1),
		  
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
				(party_template_get_slot, ":bandit_lair", ":bandit_template", slot_party_template_lair_party),
				
				#No party is active because bandit lairs are removed as soon as they are attacked, by the player -- but can only be removed by the player. This will reset bandit lair to zero
				(gt, ":bandit_lair", "p_spawn_points_end"),
				
				(assign, ":closest_town", -1),
				(assign, ":score_to_beat", 99999),
				
				(try_for_range, ":town_no", towns_begin, towns_end),
				  (store_distance_to_party_from_party, ":distance", ":bandit_lair", ":town_no"),
				  (lt, ":distance", ":score_to_beat"),
				  (assign, ":closest_town", ":town_no"),
				  (assign, ":score_to_beat", ":distance"),
				(try_end),
				
				# (str_store_party_name, s7, ":closest_town"),
				# (party_get_slot, ":closest_town_lord", ":closest_town", slot_town_lord),
				# (str_store_troop_name, s8, ":closest_town_lord"),
				
				(party_slot_eq, ":closest_town", slot_town_lord, ":giver_troop"),
				(assign, ":lair_found", ":bandit_lair"),
			(try_end),
          
          (gt, ":lair_found", "p_spawn_points_end"),
          
          (assign ,":result", "qst_destroy_bandit_lair"),
          (assign, ":relevant_party", ":lair_found"),
        (else_try),  #3 - bounty on bandit party
          (is_between, ":giver_troop", mayors_begin, mayors_end),
          (neg|check_quest_active, "qst_track_down_bandits"),
          (quest_slot_eq, "qst_track_down_bandits", slot_quest_dont_give_again_remaining_days, 0),
          
          (assign, ":cur_town", -1),
          (try_for_range, ":town", towns_begin, towns_end),
            (party_slot_eq, ":town", slot_town_elder, ":giver_troop"),
            (assign, ":cur_town", ":town"),
          (try_end),
          (gt, ":cur_town", -1),
          
          (call_script, "script_merchant_road_info_to_s42", ":cur_town"),
          (assign, ":bandit_party_found", reg0),
          (party_is_active, ":bandit_party_found"),
          (gt, ":bandit_party_found", 0),
          
          (try_begin),
            (eq, "$cheat_mode", 1),
            (display_message, "str_traveller_attack_found"),
          (try_end),
          
          (assign ,":result", "qst_track_down_bandits"),
          (assign, ":relevant_party", ":bandit_party_found"),
	(else_try),  #raid a caravan to start war
		##diplomacy start+
	    ##Roguish and tmt_humanitarian < 0 also should qualify.
		(call_script, "script_dplmc_get_troop_morality_value", ":giver_troop", tmt_humanitarian),
		(assign, ":humanitarian_value", reg0),
		(lt, ":humanitarian_value", 1),
		(assign, reg0, 0),#<-- satisfies requirement
		(try_begin),
			#Originally, only lrep_debauched qualified
			(troop_slot_eq, ":giver_troop", slot_lord_reputation_type, lrep_debauched),
			(assign, reg0, 1),
		(else_try),
			#Roguish qualifies for anti-humanitarians
			(troop_slot_eq, ":giver_troop", slot_lord_reputation_type, lrep_roguish),
			(lt, ":humanitarian_value", 1),
			(assign, reg0, 1),
		(try_end),
		(eq, reg0, 1),
		##diplomacy end+
		(store_faction_of_troop, ":giver_troop_faction", ":giver_troop"),
         
		(assign, ":junior_debauched_lord_in_faction", -1),
      ##diplomacy start+
		#Add support for promoted kingdom ladies
		#(try_for_range, ":lord_in_faction", active_npcs_begin, active_npcs_end),
		(try_for_range, ":lord_in_faction", heroes_begin, heroes_end),
			(this_or_next|is_between, ":lord_in_faction", active_npcs_begin, active_npcs_end),
				(troop_slot_eq, ":lord_in_faction", slot_troop_occupation, slto_kingdom_hero),
			(call_script, "script_dplmc_get_troop_morality_value", ":giver_troop", tmt_humanitarian),
			(assign, ":other_humanitarian", reg0),
			(lt, ":other_humanitarian", 1),
			(assign, reg0, 0),#<-- satisfies personality requirement
			(try_begin),
				#originally just debauched lords
				(troop_slot_eq, ":lord_in_faction", slot_lord_reputation_type, lrep_debauched),
				(assign, reg0, 1),
			(else_try),
				#roguish qualifies for anti-humanitarians
				(troop_slot_eq, ":giver_troop", slot_lord_reputation_type, lrep_roguish),
				(lt, ":humanitarian_value", 1),
				(assign, reg0, 1),
			(try_end),
			(eq, reg0, 1),
	  ##diplomacy end+
			(store_faction_of_troop, ":debauched_lord_faction", ":lord_in_faction"),
			(eq, ":debauched_lord_faction", ":giver_troop_faction"),
			(assign, ":junior_debauched_lord_in_faction", ":lord_in_faction"),
		(try_end),
		(eq, ":giver_troop", ":junior_debauched_lord_in_faction"),

          
          (assign, ":faction_to_attack", -1),												#	1.143 Port // Changed from 0
          (assign, ":faction_to_attack_score", -1),											#	1.143 Port // Changed from 0
          
          (try_for_range, ":faction_candidate", kingdoms_begin, kingdoms_end),
        #    (neq, ":faction_to_attack", -1),												#	1.143 Port // Removed
            (neq, ":faction_candidate", ":giver_troop_faction"),
            (faction_slot_eq, ":faction_candidate", slot_faction_state, sfs_active),
            (neq, ":faction_candidate", "$players_kingdom"),
            
            (store_relation, ":relation", ":faction_candidate", ":giver_troop_faction"),
            
            (store_add, ":provocation_slot", ":giver_troop_faction", slot_faction_provocation_days_with_factions_begin),
            (val_sub, ":provocation_slot", kingdoms_begin),
            (faction_get_slot, ":provocation_days", ":faction_candidate", ":provocation_slot"),
            
			(ge, ":relation", 0), #disqualifies if the faction is already at war							#	1.143 Port // Changed a few lines, see native, possible conflict with cabas stuff?
			(le, ":provocation_days", 0), #disqualifies if the faction has already provoked someone
			
			(store_random_in_range, ":faction_candidate_score", 0, 100),
			#add in scores - no truce?																		#	End
              
				(store_add, ":truce_slot", ":giver_troop_faction", slot_faction_truce_days_with_factions_begin),
				(store_add, ":provocation_slot", ":giver_troop_faction", slot_faction_provocation_days_with_factions_begin),
				(val_sub, ":truce_slot", kingdoms_begin),
				(val_sub, ":provocation_slot", kingdoms_begin),
		#		(try_begin), ##CABA
		#			(faction_slot_eq, ":faction_candidate", ":provocation_slot", 0),
		#			(try_begin),
		#				(faction_slot_ge, ":faction_candidate", ":truce_slot", 1),
		#				(val_sub, ":faction_to_attack_temp_score", 1),
		#			(try_end),
		#		(else_try), ##CABA
		#		    (val_add, ":faction_to_attack_temp_score", 1), ##CABA
		#		(try_end), ##CABA
				
			(gt, ":faction_candidate_score", ":faction_to_attack_score"),									#	1.143 Port // Changed a few lines, see native, possible conflict with cabas stuff?
			(assign, ":faction_to_attack", ":faction_candidate"),
			(assign, ":faction_to_attack_score", ":faction_candidate_score"),								#	End

          (try_end),
          
          (is_between, ":faction_to_attack", kingdoms_begin, kingdoms_end),
          
          (assign ,":result", "qst_cause_provocation"),
          (assign, ":relevant_faction", ":faction_to_attack"),
          
        (try_end),
        
        (assign, reg0, ":result"),
        (assign, reg1, ":relevant_troop"),
        (assign, reg2, ":relevant_party"),
        (assign, reg3, ":relevant_faction"),
        
    ]),
    
    ("get_political_quest",
      #Political quests are given by the player's political "coach" -- ie, a spouse or the minister -- to improve standing in the faction
      [
        (store_script_param, ":giver_troop", 1),
        
        (assign, ":result", -1),
        (assign, ":quest_target_troop", -1),
        (assign, ":quest_object_troop", -1),
        (assign, ":quest_dont_give_again_period", 7), #one week on average
        
        
        
        (try_begin), #this for kingdom hero, "we have a mutual enemy"
          (neg|check_quest_active, "qst_denounce_lord"),
          (try_begin),
            (ge, "$cheat_mode", 1),
            (quest_get_slot, reg4, "qst_denounce_lord", slot_quest_dont_give_again_remaining_days),
            (display_message, "@{!}DEBUG -- Checking for denounce lord, eligible in {reg4} days"),
          (try_end),
          
          (neg|quest_slot_ge, "qst_denounce_lord", slot_quest_dont_give_again_remaining_days, 1),
          (neq, ":giver_troop", "$g_player_minister"),
          (neg|troop_slot_eq, "trp_player", slot_troop_spouse, ":giver_troop"),
          (neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
          
          
          #		(neg|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_martial),
          (neg|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_quarrelsome),
          (neg|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_goodnatured),
          
          #		(neg|troop_slot_ge, "trp_player", slot_troop_controversy, 10),
          
          
          (assign, ":target_lord", -1),
          (assign, ":score_to_beat", 1),
          
		##diplomacy start+ support promoted ladies
		#(try_for_range, ":potential_target", active_npcs_begin, active_npcs_end),
		(try_for_range, ":potential_target", heroes_begin, heroes_end),
		   (this_or_next|is_between, ":potential_target", active_npcs_begin, active_npcs_end),
			   (troop_slot_eq, ":potential_target", slot_troop_occupation, slto_kingdom_hero),
            (neg|troop_slot_ge, ":potential_target", slot_troop_occupation, slto_retirement),
            ##diplomacy end+
            (store_faction_of_troop, ":potential_target_faction", ":potential_target"),
            (eq, ":potential_target_faction", "$players_kingdom"),
            (neq, ":potential_target", ":giver_troop"),
            (neg|faction_slot_eq, ":potential_target_faction", slot_faction_leader, ":potential_target"),
            
            #cannot denounce if you also have an intrigue against lord active
            (this_or_next|neg|check_quest_active, "qst_intrigue_against_lord"),
            (neg|quest_slot_eq, "qst_intrigue_against_lord", slot_quest_target_troop, ":potential_target"),
            
            (call_script, "script_troop_get_relation_with_troop", ":potential_target", ":giver_troop"),
            (assign, ":relation_with_giver_troop", reg0),
            (lt, ":relation_with_giver_troop", ":score_to_beat"),
            
            (str_store_troop_name, s4, ":potential_target"),
            (try_begin),
              (ge, "$cheat_mode", 1),
              (display_message, "@{!}DEBUG -- Rival found in {s4}"),
            (try_end),
            
			(try_begin),
				(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_debauched),
				(assign, ":max_rel_w_player", 15),
			(else_try),
				##diplomacy start+
				(this_or_next|troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_ambitious),
				##diplomacy end+
				(troop_slot_eq, "$g_talk_troop", slot_lord_reputation_type, lrep_quarrelsome),
				(assign, ":max_rel_w_player", 10),
			(else_try),
				(assign, ":max_rel_w_player", 5),
			(try_end),
            
            (call_script, "script_troop_get_relation_with_troop", ":potential_target", "trp_player"),
            (assign, ":relation_with_player", reg0),
            (lt, ":relation_with_player", ":max_rel_w_player"),
            
            (str_store_troop_name, s4, ":potential_target"),
            (try_begin),
              (ge, "$cheat_mode", 1),
              (display_message, "@{!}DEBUG -- {s4} is not close friend of player"),
            (try_end),
            
			(assign, ":enemies_in_faction", 0),
			##diplomacy start+ support promoted ladies
			#(try_for_range, ":other_lord", active_npcs_begin, active_npcs_end),
			(try_for_range, ":other_lord", heroes_begin, heroes_end),
			   (this_or_next|is_between, ":other_lord", active_npcs_begin, active_npcs_end),
				   (troop_slot_eq, ":other_lord", slot_troop_occupation, slto_kingdom_hero),
                ##diplomacy start+ do not scheme regarding dead/exiled lords
                (neg|troop_slot_eq, ":other_lord", slot_troop_occupation, dplmc_slto_dead),
                (neg|troop_slot_eq, ":other_lord", slot_troop_occupation, dplmc_slto_exile),
                (neg|troop_slot_ge, ":other_lord", slot_troop_occupation, slto_retirement),
                ##diplomacy end+
				(store_faction_of_troop, ":other_lord_faction", ":other_lord"),
				(eq, ":other_lord_faction", "$players_kingdom"),
				(call_script, "script_troop_get_relation_with_troop", ":potential_target", ":other_lord"),
				(lt, reg0, 0),
				(val_add, ":enemies_in_faction", 1),
			(try_end),
            
            (str_store_troop_name, s4, ":potential_target"),
            (try_begin),
              (ge, "$cheat_mode", 1),
              (assign, reg3, ":enemies_in_faction"),
              (display_message, "@{!}DEBUG -- {s4} has {reg3} rivals"),
            (try_end),
            
            (this_or_next|ge, ":enemies_in_faction", 3),
            (ge, "$cheat_mode", 1),
            
            (assign, ":score_to_beat", ":relation_with_giver_troop"),
            (assign, ":target_lord", ":potential_target"),
          (try_end),
          
		##diplomacy start+ support promoted ladies
		#(is_between, ":target_lord", active_npcs_begin, active_npcs_end),
		(is_between, ":target_lord", heroes_begin, heroes_end),
		##diplomacy end+
          
          
          (assign, ":result", "qst_denounce_lord"),
          (assign, ":quest_target_troop", ":target_lord"),
          
        (else_try),
          (neg|check_quest_active, "qst_intrigue_against_lord"),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (quest_get_slot, reg4, "qst_intrigue_against_lord", slot_quest_dont_give_again_remaining_days),
            (display_message, "@{!}DEBUG -- Checking for intrigue, eligible in {reg4} days"),
          (try_end),
          
          (neg|quest_slot_ge, "qst_intrigue_against_lord", slot_quest_dont_give_again_remaining_days, 1),
          
          
          
          (neq, ":giver_troop", "$g_player_minister"),
          (neg|troop_slot_eq, "trp_player", slot_troop_spouse, ":giver_troop"),
          (neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
          
          (try_begin),
            (ge, "$cheat_mode", 1),
            (display_message, "@{!}DEBUG -- Trying for intrigue against lord"),
          (try_end),
          
          
          (assign, ":target_lord", -1),
          (assign, ":score_to_beat", 10),
          
		#(try_for_range, ":potential_target", active_npcs_begin, active_npcs_end),
		(try_for_range, ":potential_target", heroes_begin, heroes_end),
		    (this_or_next|is_between, ":potential_target", active_npcs_begin, active_npcs_end),
		    (troop_slot_eq, ":potential_target", slot_troop_occupation, slto_kingdom_hero),
            ##diplomacy start+ do not scheme regarding dead/exiled lords
            (neg|troop_slot_ge, ":potential_target", slot_troop_occupation, slto_retirement),
            ##diplomacy end+
            (store_faction_of_troop, ":potential_target_faction", ":potential_target"),
            (eq, ":potential_target_faction", "$players_kingdom"),
            (neq, ":potential_target", ":giver_troop"),
            (neg|faction_slot_eq, ":potential_target_faction", slot_faction_leader, ":potential_target"),
            
            
            (this_or_next|neg|check_quest_active, "qst_denounce_lord"),
            (neg|quest_slot_eq, "qst_denounce_lord", slot_quest_target_troop, ":potential_target"),
            
            (faction_get_slot, ":faction_liege", "$players_kingdom", slot_faction_leader),
            (call_script, "script_troop_get_relation_with_troop", ":potential_target", ":faction_liege"),
            (assign, ":relation_with_liege", reg0),
            (lt, ":relation_with_liege", ":score_to_beat"),
            
            (str_store_troop_name, s4, ":potential_target"),
            (try_begin),
              (ge, "$cheat_mode", 1),
              (display_message, "@{!}DEBUG -- {s4} has sufficiently low relation with liege"),
            (try_end),
            
            
            (call_script, "script_troop_get_relation_with_troop", ":potential_target", ":giver_troop"),
            (assign, ":relation_with_giver_troop", reg0),
            (lt, ":relation_with_giver_troop", 0),
            
            (str_store_troop_name, s4, ":potential_target"),
            (try_begin),
              (ge, "$cheat_mode", 1),
              (display_message, "@{!}DEBUG -- {s4} has sufficiently low relation with giver troop"),
            (try_end),
            
            
            (call_script, "script_troop_get_relation_with_troop", ":potential_target", "trp_player"),
            (assign, ":relation_with_player", reg0),
            (lt, ":relation_with_player", 0),
            
            (str_store_troop_name, s4, ":potential_target"),
            (try_begin),
              (ge, "$cheat_mode", 1),
              (display_message, "@{!}DEBUG -- {s4} has sufficiently low relation with player"),
            (try_end),
            
            (assign, ":score_to_beat", ":relation_with_liege"),
            (assign, ":target_lord", ":potential_target"),
          (try_end),
          
		##diplomacy start+ support promoted ladies
		#(is_between, ":target_lord", active_npcs_begin, active_npcs_end),
		(is_between, ":target_lord", heroes_begin, heroes_end),
		##diplomacy end+
          
          
          (assign, ":result", "qst_intrigue_against_lord"),
          (assign, ":quest_target_troop", ":target_lord"),
          
          
        (else_try),
          #Resolve dispute, if there is a good chance of achieving the result
          (try_begin),
            (ge, "$cheat_mode", 1),
            (quest_get_slot, reg4, "qst_resolve_dispute", slot_quest_dont_give_again_remaining_days),
            (display_message, "@{!}DEBUG -- Checking for resolve dispute, eligible in {reg4} days"),
          (try_end),
          
          (neg|quest_slot_ge, "qst_resolve_dispute", slot_quest_dont_give_again_remaining_days, 1),
          
          
          
		##diplomacy start+
		#Add additional relative options
		##(call_script, "script_troop_get_family_relation_to_troop", "trp_player", ":giver_troop"),
		(call_script, "script_dplmc_troop_get_family_relation_to_troop", "trp_player", ":giver_troop"),
		(this_or_next|ge, reg0, 4),
		##diplomacy end+
		(this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, "$g_talk_troop"),
			(eq, "$g_talk_troop", "$g_player_minister"),

		(assign, ":target_lord", -1),
		(assign, ":object_lord", -1),
		(assign, ":best_chance_of_success", 20),

		#(try_for_range, ":lord_1", active_npcs_begin, active_npcs_end),
      (try_for_range, ":lord_1", heroes_begin, heroes_end),
		   (this_or_next|is_between, ":lord_1", active_npcs_begin, active_npcs_end),
			   (troop_slot_eq, ":lord_1", slot_troop_occupation, slto_kingdom_hero),
            ##diplomacy start+ do not use dead/exiled lords
            (neg|troop_slot_eq, ":lord_1", slot_troop_occupation, dplmc_slto_exile),
            (neg|troop_slot_eq, ":lord_1", slot_troop_occupation, dplmc_slto_dead),
            (neg|troop_slot_ge, ":lord_1", slot_troop_occupation, slto_retirement),
            ##diplomacy end+
			(store_faction_of_troop, ":lord_1_faction", ":lord_1"),
			(eq, ":lord_1_faction", "$players_kingdom"),
			(neq, ":lord_1", "$g_talk_troop"),

			#(try_for_range, ":lord_2", active_npcs_begin, active_npcs_end),
			(try_for_range, ":lord_2", heroes_begin, heroes_end),
			   (this_or_next|is_between, ":lord_2", active_npcs_begin, active_npcs_end),
				   (troop_slot_eq, ":lord_2", slot_troop_occupation, slto_kingdom_hero),
                ##diplomacy start+ do not use dead/exiled lords
                (neg|troop_slot_ge, ":lord_2", slot_troop_occupation, slto_retirement),
                ##diplomacy end+
				(store_faction_of_troop, ":lord_2_faction", ":lord_2"),
				(eq, ":lord_2_faction", "$players_kingdom"),

				(neq, ":lord_1", ":lord_2"),
				(neq, ":lord_2", "$g_talk_troop"),

				(call_script, "script_troop_get_relation_with_troop", ":lord_1", ":lord_2"),
				(assign, ":lord_1_relation_with_lord_2", reg0),
				(lt, ":lord_1_relation_with_lord_2", -5),

				(call_script, "script_troop_get_relation_with_troop", ":lord_1", "trp_player"),
				(assign, ":relation_with_lord_1", reg0),

				(call_script, "script_troop_get_relation_with_troop", ":lord_2", "trp_player"),
				(assign, ":relation_with_lord_2", reg0),

				(gt, ":relation_with_lord_1", 0),
				(gt, ":relation_with_lord_2", 0),

				(store_mul, ":chance_of_success", ":relation_with_lord_1", ":relation_with_lord_2"),


				(gt, ":chance_of_success", ":best_chance_of_success"),
				(assign, ":best_chance_of_success", ":chance_of_success"),
				(assign, ":target_lord", ":lord_1"),
				(assign, ":object_lord", ":lord_2"),
			(try_end),
		(try_end),


		##diplomacy start+ support promoted ladies
		#(is_between, ":target_lord", active_npcs_begin, active_npcs_end),
		(is_between, ":target_lord", heroes_begin, heroes_end),
		##diplomacy end+

		(assign, ":result", "qst_resolve_dispute"),
		(assign, ":quest_target_troop", ":target_lord"),
		(assign, ":quest_object_troop", ":object_lord"),

	(else_try),
		(try_begin),
			(ge, "$cheat_mode", 1),
			(quest_get_slot, reg4, "qst_offer_gift", slot_quest_dont_give_again_remaining_days),
			(display_message, "@{!}DEBUG -- Checking for offer gift, eligible in {reg4} days"),
		(try_end),

		##diplomacy start+ conventional ladies have a quicker "reset" time on this quest
		(neg|quest_slot_ge, "qst_offer_gift", slot_quest_dont_give_again_remaining_days, 4),
        (this_or_next|troop_slot_eq, ":giver_troop", slot_lord_reputation_type, lrep_conventional),
		##diplomacy end+
		(neg|quest_slot_ge, "qst_offer_gift", slot_quest_dont_give_again_remaining_days, 1),

		(assign, ":relative_found", -1),
		(assign, ":score_to_beat", 5),
		##diplomacy start+
		#Slightly expand the range of potential targets if changes are enabled
		(try_begin),
         (ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
		   (assign, ":score_to_beat", 4),
		   (troop_slot_eq, ":giver_troop", slot_lord_reputation_type, lrep_conventional),
		   (assign, ":score_to_beat", 3),
	   (try_end),
		##diplomacy end+

		##diplomacy start+
		#(try_for_range, ":potential_relative", active_npcs_begin, active_npcs_end),
		#Add support for promoted ladies (TODO: add a variant for ordinary ladies as well)
		(try_for_range, ":potential_relative", heroes_begin, heroes_end),
			#do not use dead/exiled lords
			(this_or_next|is_between, ":potential_relative", active_npcs_begin, active_npcs_end),
				(troop_slot_eq, ":potential_relative", slot_troop_occupation, slto_kingdom_hero),
         (neg|troop_slot_ge, ":potential_relative", slot_troop_occupation, slto_retirement),
        ##diplomacy end+
			(store_faction_of_troop, ":relative_faction", ":potential_relative"),
			(eq, ":relative_faction", "$players_kingdom"),
			(neq, ":potential_relative", ":giver_troop"),
			(neg|faction_slot_eq, ":relative_faction", slot_faction_leader, ":potential_relative"),

			(call_script, "script_troop_get_family_relation_to_troop", ":giver_troop", ":potential_relative"),
			(assign, ":family_relation", reg0),
			(ge, ":family_relation", ":score_to_beat"),

			(store_sub, ":min_relation_w_player", 0, ":family_relation"),

			(call_script, "script_troop_get_relation_with_troop", "trp_player", ":potential_relative"),
			(assign, ":relation_with_player", reg0),
			(is_between, ":relation_with_player", ":min_relation_w_player", 0),

			(assign, ":score_to_beat", ":family_relation"),
			(assign, ":relative_found", ":potential_relative"),

		(try_end),

		(is_between, ":relative_found", active_npcs_begin, active_npcs_end),

		(assign, ":result", "qst_offer_gift"),
		(assign, ":quest_target_troop", ":relative_found"),
	(try_end),
        
        
        (try_begin),
          (gt, ":result", -1),
          (quest_set_slot, ":result", slot_quest_target_troop, ":quest_target_troop"),
          (quest_set_slot, ":result", slot_quest_object_troop, ":quest_object_troop"), ##CABA - bugfix was slot_quest_target_troop
          
          (quest_set_slot, ":result", slot_quest_giver_troop, ":giver_troop"),
          (quest_set_slot, ":result", slot_quest_dont_give_again_period, ":quest_dont_give_again_period"),
        (try_end),
        
        (assign, reg0, ":result"),
        (assign, reg1, ":quest_target_troop"),
        (assign, reg2, ":quest_object_troop"),
        
    ]),
    
    
    ("npc_find_quest_for_player_to_s11",
      [
        (store_script_param, ":faction", 1),
        
        (assign, ":quest_giver_found", -1),
        (try_for_range, ":quest_giver", active_npcs_begin, mayors_end),
          (eq, ":quest_giver_found", -1),
          
          (neg|troop_slot_eq, "trp_player", slot_troop_spouse, ":quest_giver"), ##1.132, new line
          
          (gt, ":quest_giver", "$g_troop_list_no"),
          
          (assign, "$g_troop_list_no", ":quest_giver"),
          
          (this_or_next|troop_slot_eq, ":quest_giver", slot_troop_occupation, slto_kingdom_hero),
          (is_between, ":quest_giver", mayors_begin, mayors_end),
          
          (neg|troop_slot_ge, ":quest_giver", slot_troop_prisoner_of_party, centers_begin),
          
          (try_begin),
            (is_between, ":quest_giver", mayors_begin, mayors_end),
            (assign, ":quest_giver_faction", -1),
            (try_for_range,":town", towns_begin, towns_end),
              (party_slot_eq, ":town", slot_town_elder, ":quest_giver"),
              (store_faction_of_party, ":quest_giver_faction", ":town"),
            (try_end),
          (else_try),
            (store_faction_of_troop, ":quest_giver_faction", ":quest_giver"),
          (try_end),
          (eq, ":faction", ":quest_giver_faction"),
          
          (call_script, "script_get_dynamic_quest", ":quest_giver"),
          (gt, reg0, -1),
          
          (assign, ":quest_giver_found", ":quest_giver"),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_troop_name, s4, ":quest_giver_found"),
            (display_message, "str_test_diagnostic_quest_found_for_s4"),
          (try_end),
          
        (try_end),
        
        (assign, reg0, ":quest_giver_found"),
        
    ]),
    
    
    
    # script_cf_get_random_enemy_center_within_range
    # Input: arg1 = party_no, arg2 = range (in kms)
    # Output: reg0 = center_no
    ("cf_get_random_enemy_center_within_range",
      [
        (store_script_param, ":party_no", 1),
        (store_script_param, ":range", 2),
        
        (assign, ":num_centers", 0),
        (store_faction_of_party, ":faction_no", ":party_no"),
        (try_for_range, ":cur_center", centers_begin, centers_end),
          (store_faction_of_party, ":cur_faction", ":cur_center"),
          (store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
          (lt, ":cur_relation", 0),
          (store_distance_to_party_from_party, ":dist", ":party_no", ":cur_center"),
          (le, ":dist", ":range"),
          (val_add, ":num_centers", 1),
        (try_end),
        (gt, ":num_centers", 0),
        (store_random_in_range, ":random_center", 0, ":num_centers"),
        (assign, ":end_cond", centers_end),
        (try_for_range, ":cur_center", centers_begin, ":end_cond"),
          (store_faction_of_party, ":cur_faction", ":cur_center"),
          (store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
          (lt, ":cur_relation", 0),
          (store_distance_to_party_from_party, ":dist", ":party_no", ":cur_center"),
          (le, ":dist", ":range"),
          (val_sub, ":random_center", 1),
          (lt, ":random_center", 0),
          (assign, ":result", ":cur_center"),
          (assign, ":end_cond", 0),#break
        (try_end),
        (assign, reg0, ":result"),
    ]),
    
    # script_cf_faction_get_random_enemy_faction
    # Input: arg1 = faction_no
    # Output: reg0 = faction_no (Can fail)
    ("cf_faction_get_random_enemy_faction",
      [
        (store_script_param_1, ":faction_no"),
        
        (assign, ":result", -1),
        (assign, ":count_factions", 0),
        (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
          (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
          (store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
          (le, ":cur_relation", -1),
          (val_add, ":count_factions", 1),
        (try_end),
        (store_random_in_range,":random_faction",0,":count_factions"),
        (assign, ":count_factions", 0),
        (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
          (eq, ":result", -1),
          (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
          (store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
          (le, ":cur_relation", -1),
          (val_add, ":count_factions", 1),
          (gt, ":count_factions", ":random_faction"),
          (assign, ":result", ":cur_faction"),
        (try_end),
        
        (neq, ":result", -1),
        (assign, reg0, ":result"),
    ]),
    
    # script_cf_faction_get_random_friendly_faction
    # Input: arg1 = faction_no
    # Output: reg0 = faction_no (Can fail)
    ("cf_faction_get_random_friendly_faction",
      [
        (store_script_param_1, ":faction_no"),
        
        (assign, ":result", -1),
        (assign, ":count_factions", 0),
        (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
          (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
          (neq, ":cur_faction", ":faction_no"),
          (store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
          (ge, ":cur_relation", 0),
          (val_add, ":count_factions", 1),
        (try_end),
        (store_random_in_range,":random_faction",0,":count_factions"),
        (assign, ":count_factions", 0),
        (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
          (eq, ":result", -1),
          (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
          (neq, ":cur_faction", ":faction_no"),
          (store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
          (ge, ":cur_relation", 0),
          (val_add, ":count_factions", 1),
          (gt, ":count_factions", ":random_faction"),
          (assign, ":result", ":cur_faction"),
        (try_end),
        
        (neq, ":result", -1),
        (assign, reg0, ":result"),
    ]),
    
    # script_cf_troop_get_random_enemy_troop_with_occupation
    # Input: arg1 = troop_no,
    # Output: reg0 = enemy_troop_no (Can fail)
    ("cf_troop_get_random_enemy_troop_with_occupation",
      [
        (store_script_param_1, ":troop_no"),
        (store_script_param_2, ":occupation"),
        
        (assign, ":result", -1),
        (assign, ":count_enemies", 0),
        (try_for_range, ":enemy_troop_no", active_npcs_begin, active_npcs_end),
          (troop_slot_eq, ":enemy_troop_no", slot_troop_occupation, ":occupation"),
          (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":enemy_troop_no"),
          (lt, reg0, -10),
          (val_add, ":count_enemies", 1),
        (try_end),
        
        (gt, ":count_enemies", 0),
        (store_random_in_range,":random_enemy",0,":count_enemies"),
        
        (assign, ":count_enemies", 0),
        (try_for_range, ":enemy_troop_no", active_npcs_begin, active_npcs_end),
          (troop_slot_eq, ":enemy_troop_no", slot_troop_occupation, ":occupation"),
          (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":enemy_troop_no"),
          (lt, reg0, -10),
          (val_add, ":count_enemies", 1),
          (eq, ":random_enemy", ":count_enemies"),
          (assign, ":result", ":enemy_troop_no"),
        (try_end),
        
        (neq, ":result", -1),
        (assign, reg0, ":result"),
    ]),
    
    
    ##  # script_cf_troop_get_random_enemy_troop_as_a_town_lord
    ##  # Input: arg1 = troop_no
    ##  # Output: reg0 = enemy_troop_no (Can fail)
    ##  ("cf_troop_get_random_enemy_troop_as_a_town_lord",
    ##    [
    ##      (store_script_param_1, ":troop_no"),
    ##
    ##      (assign, ":result", -1),
    ##      (assign, ":count_enemies", 0),
    ##      (try_for_range, ":cur_slot", slot_troop_enemies_begin, slot_troop_enemies_end),
    ##        (troop_get_slot, ":cur_enemy", ":troop_no", ":cur_slot"),
    ##        (gt, ":cur_enemy", 0),
    ##        (troop_slot_eq, ":cur_enemy", slot_troop_occupation, slto_kingdom_hero),
    ##        (call_script, "script_get_number_of_hero_centers", ":cur_enemy"),
    ##        (gt, reg0, 0),
    ##        (val_add, ":count_enemies", 1),
    ##      (try_end),
    ##      (store_random_in_range,":random_enemy",0,":count_enemies"),
    ##      (assign, ":count_enemies", 0),
    ##      (try_for_range, ":cur_slot", slot_troop_enemies_begin, slot_troop_enemies_end),
    ##        (eq, ":result", -1),
    ##        (troop_get_slot, ":cur_enemy", ":troop_no", ":cur_slot"),
    ##        (gt, ":cur_enemy", 0),
    ##        (troop_slot_eq, ":cur_enemy", slot_troop_occupation, slto_kingdom_hero),
    ##        (call_script, "script_get_number_of_hero_centers", ":cur_enemy"),
    ##        (gt, reg0, 0),
    ##        (val_add, ":count_enemies", 1),
    ##        (gt, ":count_enemies", ":random_enemy"),
    ##        (assign, ":result", ":cur_enemy"),
    ##      (try_end),
    ##      (neq, ":result", -1),
    ##      (assign, reg0, ":result"),
    ##  ]),
    
    
    ##  # script_cf_get_random_enemy_with_valid_slot
    ##  # Input: arg1 = faction_no, arg2 = slot_no
    ##  # Output: reg0 = faction_no (Can fail)
    ##  ("cf_get_random_enemy_with_valid_slot",
    ##    [
    ##      (store_script_param_1, ":faction_no"),
    ##      (store_script_param_2, ":slot_no"),
    ##
    ##      (assign, ":result", -1),
    ##      (assign, ":count_factions", 0),
    ##      (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
    ##        (store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
    ##        (le, ":cur_relation", -10),
    ##        (faction_get_slot, ":cur_value", ":cur_faction", ":slot_no"),
    ##        (gt, ":cur_value", 0),#Checking validity
    ##        (val_add, ":count_factions", 1),
    ##      (try_end),
    ##      (store_random_in_range,":random_faction",0,":count_factions"),
    ##      (assign, ":count_factions", 0),
    ##      (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
    ##        (eq, ":result", -1),
    ##        (store_relation, ":cur_relation", ":faction_no", ":cur_faction"),
    ##        (le, ":cur_relation", -10),
    ##        (faction_get_slot, ":cur_value", ":cur_faction", ":slot_no"),
    ##        (gt, ":cur_value", 0),#Checking validity
    ##        (val_add, ":count_factions", 1),
    ##        (gt, ":count_factions", ":random_faction"),
    ##        (assign, ":result", ":cur_faction"),
    ##      (try_end),
    ##
    ##      (neq, ":result", -1),
    ##      (assign, reg0, ":result"),
    ##  ]),
    
    
    ##  # script_cf_get_random_kingdom_hero
    ##  # Input: arg1 = faction_no
    ##  # Output: reg0 = troop_no (Can fail)
    ##  ("cf_get_random_kingdom_hero",
    ##    [
    ##      (store_script_param_1, ":faction_no"),
    ##      (assign, ":count_heroes", 0),
    ##      (try_for_range, ":center_no", centers_begin, centers_end),
    ##        (store_faction_of_party, ":cur_faction", ":center_no"),
    ##        (eq, ":cur_faction", ":faction_no"),
    ##        (party_get_slot, ":cur_lord", ":center_no", slot_town_lord),
    ##        (is_between, ":cur_lord", heroes_begin, heroes_end),
    ##        (val_add, ":count_heroes", 1),
    ##      (try_end),
    ##      (store_random_in_range, ":random_hero", 0, ":count_heroes"),
    ##      (assign, ":result", -1),
    ##      (assign, ":count_heroes", 0),
    ##      (try_for_range, ":center_no", centers_begin, centers_end),
    ##        (eq, ":result", -1),
    ##        (store_faction_of_party, ":cur_faction", ":center_no"),
    ##        (eq, ":cur_faction", ":faction_no"),
    ##        (party_get_slot, ":cur_lord", ":center_no", slot_town_lord),
    ##        (is_between, ":cur_lord", heroes_begin, heroes_end),
    ##        (val_add, ":count_heroes", 1),
    ##        (lt, ":random_hero", ":count_heroes"),
    ##        (assign, ":result", ":cur_lord"),
    ##      (try_end),
    ##      (neq, ":result", -1),
    ##      (assign, reg0, ":result"),
    ##  ]),
    
    
    # script_cf_get_random_kingdom_hero_as_lover - removed
    
    
    
    ##  # script_cf_get_random_siege_location_with_faction
    ##  # Input: arg1 = faction_no
    ##  # Output: reg0 = center_no, Can Fail!
    ##  ("cf_get_random_siege_location_with_faction",
    ##    [
    ##      (store_script_param_1, ":faction_no"),
    ##      (assign, ":result", -1),
    ##      (assign, ":count_sieges", 0),
    ##      (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
    ##        (party_get_battle_opponent, ":besieger_party", ":center_no"),
    ##        (gt, ":besieger_party", 0),
    ##        (store_faction_of_party, ":cur_faction_no", ":center_no"),
    ##        (eq, ":cur_faction_no", ":faction_no"),
    ##        (val_add, ":count_sieges", 1),
    ##      (try_end),
    ##      (store_random_in_range,":random_center",0,":count_sieges"),
    ##      (assign, ":count_sieges", 0),
    ##      (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
    ##        (eq, ":result", -1),
    ##        (party_get_battle_opponent, ":besieger_party", ":center_no"),
    ##        (gt, ":besieger_party", 0),
    ##        (store_faction_of_party, ":cur_faction_no", ":center_no"),
    ##        (eq, ":cur_faction_no", ":faction_no"),
    ##        (val_add, ":count_sieges", 1),
    ##        (gt, ":count_sieges", ":random_center"),
    ##        (assign, ":result", ":center_no"),
    ##      (try_end),
    ##      (neq, ":result", -1),
    ##      (assign, reg0, ":result"),
    ##  ]),
    
    ##  # script_cf_get_random_siege_location_with_attacker_faction
    ##  # Input: arg1 = faction_no
    ##  # Output: reg0 = center_no, Can Fail!
    ##  ("cf_get_random_siege_location_with_attacker_faction",
    ##    [
    ##      (store_script_param_1, ":faction_no"),
    ##      (assign, ":result", -1),
    ##      (assign, ":count_sieges", 0),
    ##      (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
    ##        (party_get_battle_opponent, ":besieger_party", ":center_no"),
    ##        (gt, ":besieger_party", 0),
    ##        (store_faction_of_party, ":cur_faction_no", ":besieger_party"),
    ##        (eq, ":cur_faction_no", ":faction_no"),
    ##        (val_add, ":count_sieges", 1),
    ##      (try_end),
    ##      (store_random_in_range,":random_center",0,":count_sieges"),
    ##      (assign, ":count_sieges", 0),
    ##      (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
    ##        (eq, ":result", -1),
    ##        (party_get_battle_opponent, ":besieger_party", ":center_no"),
    ##        (gt, ":besieger_party", 0),
    ##        (store_faction_of_party, ":cur_faction_no", ":besieger_party"),
    ##        (eq, ":cur_faction_no", ":faction_no"),
    ##        (val_add, ":count_sieges", 1),
    ##        (gt, ":count_sieges", ":random_center"),
    ##        (assign, ":result", ":center_no"),
    ##      (try_end),
    ##      (neq, ":result", -1),
    ##      (assign, reg0, ":result"),
    ##  ]),
    
    
    
    ##  # script_cf_get_number_of_random_troops_from_party
    ##  # Input: arg1 = party_no, arg2 = number of troops to remove
    ##  # Output: reg0 = troop_no, Can fail if there are no slots having the required number of units!
    ##  ("cf_get_number_of_random_troops_from_party",
    ##    [
    ##      (store_script_param_1, ":party_no"),
    ##      (store_script_param_2, ":no_to_remove"),
    ##
    ##      (assign, ":result", -1),
    ##      (assign, ":count_stacks", 0),
    ##
    ##      (party_get_num_companion_stacks, ":num_stacks",":party_no"),
    ##      (try_for_range, ":i_stack", 0, ":num_stacks"),
    ##        (party_stack_get_size, ":stack_size",":party_no",":i_stack"),
    ##        (party_stack_get_num_wounded, ":num_wounded",":party_no",":i_stack"),
    ##        (val_sub, ":stack_size", ":num_wounded"),
    ##        (ge, ":stack_size", ":no_to_remove"),
    ##        (party_stack_get_troop_id, ":stack_troop",":party_no",":i_stack"),
    ##        (neg|troop_is_hero, ":stack_troop"),
    ##        (val_add, ":count_stacks", 1),
    ##      (try_end),
    ##      (store_random_in_range,":random_stack",0,":count_stacks"),
    ##      (assign, ":count_stacks", 0),
    ##      (try_for_range, ":i_stack", 0, ":num_stacks"),
    ##        (eq, ":result", -1),
    ##        (party_stack_get_size, ":stack_size",":party_no",":i_stack"),
    ##        (party_stack_get_num_wounded, ":num_wounded",":party_no",":i_stack"),
    ##        (val_sub, ":stack_size", ":num_wounded"),
    ##        (ge, ":stack_size", ":no_to_remove"),
    ##        (party_stack_get_troop_id, ":stack_troop",":party_no",":i_stack"),
    ##        (neg|troop_is_hero, ":stack_troop"),
    ##        (val_add, ":count_stacks", 1),
    ##        (gt, ":count_stacks", ":random_stack"),
    ##        (assign, ":result", ":stack_troop"),
    ##      (try_end),
    ##
    ##      (neq, ":result", -1),
    ##      (assign, reg0, ":result"),
    ##  ]),
    
    
    
    
    # script_cf_get_random_lord_in_a_center_with_faction
    # Input: arg1 = faction_no
    # Output: reg0 = troop_no, Can Fail!
    ("cf_get_random_lord_in_a_center_with_faction",
      [
        (store_script_param_1, ":faction_no"),
        (assign, ":result", -1),
        (assign, ":count_lords", 0),
        (try_for_range, ":lord_no", heroes_begin, heroes_end),
          (store_troop_faction, ":lord_faction_no", ":lord_no"),
          (eq, ":faction_no", ":lord_faction_no"),
          (troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
          #(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
          (neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
          (troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
          (ge, ":lord_party", 0),
          (party_get_attached_to, ":lord_attachment", ":lord_party"),
          (is_between, ":lord_attachment", centers_begin, centers_end), #is troop in a center?
          (val_add, ":count_lords", 1),
        (try_end),
        (store_random_in_range, ":random_lord", 0, ":count_lords"),
        (assign, ":count_lords", 0),
        (try_for_range, ":lord_no", heroes_begin, heroes_end),
          (eq, ":result", -1),
          (store_troop_faction, ":lord_faction_no", ":lord_no"),
          (eq, ":faction_no", ":lord_faction_no"),
          (troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
          #(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
          (neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
          (troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
          (ge, ":lord_party", 0),
          (party_get_attached_to, ":lord_attachment", ":lord_party"),
          (is_between, ":lord_attachment", centers_begin, centers_end), #is troop in a center?
          (val_add, ":count_lords", 1),
          (lt, ":random_lord", ":count_lords"),
          (assign, ":result", ":lord_no"),
        (try_end),
        (neq, ":result", -1),
        (assign, reg0, ":result"),
    ]),
    
    # script_cf_get_random_lord_except_king_with_faction
    # Input: arg1 = faction_no
    # Output: reg0 = troop_no, Can Fail!
    ("cf_get_random_lord_except_king_with_faction",
      [
        (store_script_param_1, ":faction_no"),
        (assign, ":result", -1),
        (assign, ":count_lords", 0),
        (try_for_range, ":lord_no", heroes_begin, heroes_end),
          (store_troop_faction, ":lord_faction_no", ":lord_no"),
          (eq, ":faction_no", ":lord_faction_no"),
          (neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
          (troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
          #(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
          (neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
          (troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
          (ge, ":lord_party", 0),
          (val_add, ":count_lords", 1),
        (try_end),
        (store_random_in_range, ":random_lord", 0, ":count_lords"),
        (assign, ":count_lords", 0),
        (try_for_range, ":lord_no", heroes_begin, heroes_end),
          (eq, ":result", -1),
          (store_troop_faction, ":lord_faction_no", ":lord_no"),
          (eq, ":faction_no", ":lord_faction_no"),
          (neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":lord_no"),
          (troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
          #(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
          (neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
          (troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
          (ge, ":lord_party", 0),
          (val_add, ":count_lords", 1),
          (lt, ":random_lord", ":count_lords"),
          (assign, ":result", ":lord_no"),
        (try_end),
        (neq, ":result", -1),
        (assign, reg0, ":result"),
    ]),
    
    
    # script_cf_get_random_lord_from_another_faction_in_a_center
    # Input: arg1 = faction_no
    # Output: reg0 = troop_no, Can Fail!
    ("cf_get_random_lord_from_another_faction_in_a_center",
      [
        (store_script_param_1, ":faction_no"),
        (assign, ":result", -1),
        (assign, ":count_lords", 0),
        (try_for_range, ":lord_no", heroes_begin, heroes_end),
          (store_troop_faction, ":lord_faction_no", ":lord_no"),
          (neq, ":lord_faction_no", ":faction_no"),
          (store_relation, ":our_relation", ":lord_faction_no", "fac_player_supporters_faction"),
          (store_relation, ":lord_relation", ":lord_faction_no", ":faction_no"),
          (lt, ":lord_relation", 0),
          (ge, ":our_relation", 0),
          (troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
          #(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
          (neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
          (troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
          (ge, ":lord_party", 0),
          (party_get_attached_to, ":lord_attachment", ":lord_party"),
          (is_between, ":lord_attachment", centers_begin, centers_end), #is troop in a center?
          (val_add, ":count_lords", 1),
        (try_end),
        (store_random_in_range, ":random_lord", 0, ":count_lords"),
        (assign, ":count_lords", 0),
        (try_for_range, ":lord_no", heroes_begin, heroes_end),
          (eq, ":result", -1),
          (store_troop_faction, ":lord_faction_no", ":lord_no"),
          (neq, ":lord_faction_no", ":faction_no"),
          (store_relation, ":our_relation", ":lord_faction_no", "fac_player_supporters_faction"),
          (store_relation, ":lord_relation", ":lord_faction_no", ":faction_no"),
          (lt, ":lord_relation", 0),
          (ge, ":our_relation", 0),
          (troop_slot_eq, ":lord_no", slot_troop_occupation, slto_kingdom_hero),
          #(troop_slot_eq, ":lord_no", slot_troop_is_prisoner, 0),
          (neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of_party, 0),
          (troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
          (ge, ":lord_party", 0),
          (party_get_attached_to, ":lord_attachment", ":lord_party"),
          (is_between, ":lord_attachment", centers_begin, centers_end), #is troop in a center?
          (val_add, ":count_lords", 1),
          (lt, ":random_lord", ":count_lords"),
          (assign, ":result", ":lord_no"),
        (try_end),
        (neq, ":result", -1),
        (assign, reg0, ":result"),
    ]),
    
    # script_get_closest_walled_center
    # Input: arg1 = party_no
    # Output: reg0 = center_no (closest)
    ("get_closest_walled_center",
      [
        (store_script_param_1, ":party_no"),
        (assign, ":min_distance", 9999999),
        (assign, reg0, -1),
        (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
          (store_distance_to_party_from_party, ":party_distance", ":party_no", ":center_no"),
          (lt, ":party_distance", ":min_distance"),
          (assign, ":min_distance", ":party_distance"),
          (assign, reg0, ":center_no"),
        (try_end),
    ]),
    
    # script_get_closest_center
    # Input: arg1 = party_no
    # Output: reg0 = center_no (closest)
    ("get_closest_center",
      [
        (store_script_param_1, ":party_no"),
        (assign, ":min_distance", 9999999),
        (assign, reg0, -1),
        (try_for_range, ":center_no", centers_begin, centers_end),
          (store_distance_to_party_from_party, ":party_distance", ":party_no", ":center_no"),
          (lt, ":party_distance", ":min_distance"),
          (assign, ":min_distance", ":party_distance"),
          (assign, reg0, ":center_no"),
        (try_end),
    ]),
    
    
    # script_get_closest_center_of_faction
    # Input: arg1 = party_no, arg2 = kingdom_no
    # Output: reg0 = center_no (closest)
    ("get_closest_center_of_faction",
      [
        (store_script_param_1, ":party_no"),
        (store_script_param_2, ":kingdom_no"),
        (assign, ":min_distance", 99999),
        (assign, ":result", -1),
        (try_for_range, ":center_no", centers_begin, centers_end),
          (store_faction_of_party, ":faction_no", ":center_no"),
          (eq, ":faction_no", ":kingdom_no"),
          (store_distance_to_party_from_party, ":party_distance", ":party_no", ":center_no"),
          (lt, ":party_distance", ":min_distance"),
          (assign, ":min_distance", ":party_distance"),
          (assign, ":result", ":center_no"),
        (try_end),
        (assign, reg0, ":result"),
    ]),
    
    # script_get_closest_walled_center_of_faction
    # Input: arg1 = party_no, arg2 = kingdom_no
    # Output: reg0 = center_no (closest)
    ("get_closest_walled_center_of_faction",
      [
        (store_script_param_1, ":party_no"),
        (store_script_param_2, ":kingdom_no"),
        (assign, ":min_distance", 99999),
        (assign, ":result", -1),
        (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
          (store_faction_of_party, ":faction_no", ":center_no"),
          (eq, ":faction_no", ":kingdom_no"),
          (store_distance_to_party_from_party, ":party_distance", ":party_no", ":center_no"),
          (lt, ":party_distance", ":min_distance"),
          (assign, ":min_distance", ":party_distance"),
          (assign, ":result", ":center_no"),
        (try_end),
        (assign, reg0, ":result"),
    ]),
    
    
    ##  # script_get_closest_town_of_faction
    ##  # Input: arg1 = party_no, arg2 = kingdom_no
    ##  # Output: reg0 = center_no (closest)
    ##  ("get_closest_town_of_faction",
    ##    [
    ##      (store_script_param_1, ":party_no"),
    ##      (store_script_param_2, ":kingdom_no"),
    ##      (assign, ":min_distance", 9999999),
    ##      (assign, ":result", -1),
    ##      (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
    ##        (store_faction_of_party, ":faction_no", ":center_no"),
    ##        (eq, ":faction_no", ":kingdom_no"),
    ##        (party_slot_eq, ":center_no", slot_party_type, spt_town),
    ##        (store_distance_to_party_from_party, ":party_distance", ":party_no", ":center_no"),
    ##        (lt, ":party_distance", ":min_distance"),
    ##        (assign, ":min_distance", ":party_distance"),
    ##        (assign, ":result", ":center_no"),
    ##      (try_end),
    ##      (assign, reg0, ":result"),
    ##  ]),
    
    
    # script_let_nearby_parties_join_current_battle
    # Input: arg1 = besiege_mode, arg2 = dont_add_friends_other_than_accompanying
    # Output: none
    ("let_nearby_parties_join_current_battle",
      [
        (store_script_param, ":besiege_mode", 1),
        (store_script_param, ":dont_add_friends_other_than_accompanying", 2),
        
        #(store_character_level, ":player_level", "trp_player"), ## CC
        (try_for_parties, ":party_no"),
          (party_is_active, ":party_no"),
          (party_get_battle_opponent, ":opponent",":party_no"),
          (lt, ":opponent", 0), #party is not itself involved in a battle
          (party_get_attached_to, ":attached_to",":party_no"),
          (lt, ":attached_to", 0), #party is not attached to another party
          (get_party_ai_behavior, ":behavior", ":party_no"),
          (neq, ":behavior", ai_bhvr_in_town),
          
          (party_stack_get_troop_id, ":stack_troop", ":party_no", 0),
          (try_begin),
			##Floris MTT begin
			(troop_get_slot,":bandit_looter","$troop_trees",slot_bandit_looter),
			(troop_get_slot,":bandit_black_khergit_horseman","$troop_trees",slot_bandit_black_khergit_horseman),
			(neg|is_between, ":stack_troop", ":bandit_looter", ":bandit_black_khergit_horseman"),
			##Floris MTT end
            
            (assign, ":join_distance", 5), #day/not bandit
            (try_begin),
              (is_currently_night),
              (assign, ":join_distance", 3), #nigh/not bandit
            (try_end),
          (else_try),
            (assign, ":join_distance", 3), #day/bandit
            (try_begin),
              (is_currently_night),
              (assign, ":join_distance", 2), #night/bandit
            (try_end),
          (try_end),
          
          #Quest bandits do not join battle ##1.132, 5 new lines
          (this_or_next|neg|check_quest_active, "qst_track_down_bandits"),
          (neg|quest_slot_eq, "qst_track_down_bandits", slot_quest_target_party, ":party_no"),
          (this_or_next|neg|check_quest_active, "qst_troublesome_bandits"),
          (neg|quest_slot_eq, "qst_troublesome_bandits", slot_quest_target_party, ":party_no"), ##
          
          
          (store_distance_to_party_from_party, ":distance", ":party_no", "p_main_party"),
          (lt, ":distance", ":join_distance"),
          
          (store_faction_of_party, ":faction_no", ":party_no"),
          (store_faction_of_party, ":enemy_faction", "$g_enemy_party"),
          (try_begin),
            (eq, ":faction_no", "fac_player_supporters_faction"),
            (assign, ":reln_with_player", 100),
          (else_try),
            (store_relation, ":reln_with_player", ":faction_no", "fac_player_supporters_faction"),
          (try_end),
          (try_begin),
            (eq, ":faction_no", ":enemy_faction"),
            (assign, ":reln_with_enemy", 100),
          (else_try),
            (store_relation, ":reln_with_enemy", ":faction_no", ":enemy_faction"),
          (try_end),
          
          (assign, ":enemy_side", 1),
          (try_begin),
            (neq, "$g_enemy_party", "$g_encountered_party"),
            (assign, ":enemy_side", 2),
          (try_end),
          
          (try_begin),
            (eq, ":besiege_mode", 0),
            (lt, ":reln_with_player", 0),
            (gt, ":reln_with_enemy", 0),
	          ##zerilius changes begin
	          ##wrong use of operation (native bug)
	          #(party_get_slot, ":party_type", ":party_no"),
	        (party_get_slot, ":party_type", ":party_no", slot_party_type),
	          ##zerilius changes end
            
            #(assign, ":enemy_is_bandit_party_and_level_is_greater_than_6", 0),
            #(try_begin),
            #(party_stack_get_troop_id, ":stack_troop", ":party_no", 0),
            #(is_between, ":stack_troop", "trp_bandit_e_looter", "trp_bandit_e_black_khergit_horseman"),
            #(gt, ":player_level", 6),
            #(assign, ":enemy_is_bandit_party_and_level_is_greater_than_6", 1),
            #(try_end),
            ## CC
            (party_get_template_id,":template_id",":party_no"),
			##Floris MTT begin
				(this_or_next|is_between,":template_id","pt_looters","pt_looters_r"),
				(this_or_next|is_between,":template_id","pt_looters_r","pt_looters_e"),
				(this_or_next|is_between,":template_id","pt_looters_e","pt_deserters"),
			##Floris MTT end
            ## CC
			(this_or_next|eq, ":party_type", spt_patrol), #Floris - Diplo bugfix
            (eq, ":party_type", spt_kingdom_hero_party),
            (get_party_ai_behavior, ":ai_bhvr", ":party_no"),
            (neq, ":ai_bhvr", ai_bhvr_avoid_party),
            (party_quick_attach_to_current_battle, ":party_no", ":enemy_side"), #attach as enemy
            (str_store_party_name, s1, ":party_no"),
            (display_message, "str_s1_joined_battle_enemy", 0xff3333), # CC
          (else_try),
            (try_begin),
              (party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
              (party_slot_eq, ":party_no", slot_party_ai_object, "trp_player"),
              (assign, ":party_is_accompanying_player", 1),
            (else_try),
              (assign, ":party_is_accompanying_player", 0),
            (try_end),
            
            (this_or_next|eq, ":dont_add_friends_other_than_accompanying", 0),
            (eq, ":party_is_accompanying_player", 1),
            (gt, ":reln_with_player", 0),
            (lt, ":reln_with_enemy", 0),
            
            (assign, ":following_player", 0),
            (try_begin),
              (party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
              (party_slot_eq, ":party_no", slot_party_ai_object, "p_main_party"),
              (assign, ":following_player", 1),
            (try_end),
            
            (assign, ":do_join", 1),
            (try_begin),
              (eq, ":besiege_mode", 1),
              (eq, ":following_player", 0),
              (assign, ":do_join", 0),
              (eq, ":faction_no", "$players_kingdom"),
              (faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
              (assign, ":do_join", 1),
            (try_end),
            (eq, ":do_join", 1),
            
	          ##zerilius changes begin
	          ##wrong use of operation (native bug)
	          #(party_get_slot, ":party_type", ":party_no"),
	        (party_get_slot, ":party_type", ":party_no", slot_party_type),
	          ##zerilius changes end
			(this_or_next|eq, ":party_type", spt_patrol), #Floris - Diplo bugfix
			(eq, ":party_type", spt_kingdom_hero_party),
			(try_begin), #Floris - Diplo bugfix
				(eq, ":party_type", spt_kingdom_hero_party), #Floris - Diplo bugifx
				(party_stack_get_troop_id, ":leader", ":party_no", 0),
				#(troop_get_slot, ":player_relation", ":leader", slot_troop_player_relation),
				(call_script, "script_troop_get_player_relation", ":leader"),
				(assign, ":player_relation", reg0),
			(else_try), #Floris - Diplo bugfix begin
			    (eq, ":party_type", spt_patrol),
				(assign, ":player_relation", 1), #force join
			(try_end), #Floris - Diplo bugfix end
            
          (assign, ":join_even_you_do_not_like_player", 0),
          (try_begin),
            (faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"), #new added, if player is marshal and if he is accompanying then join battle even lord do not like player
            (eq, ":following_player", 1),
            (assign, ":join_even_you_do_not_like_player", 1),
          ##diplomacy start+
	      #Affiliates will assist the player.
	      (else_try),
             (lt, ":player_relation", 0),
	         (call_script, "script_dplmc_is_affiliated_family_member", ":leader"),
	         (val_max, ":player_relation", reg0),
          ##diplomacy end+
          (try_end),

          (this_or_next|ge, ":player_relation", 0),
          (eq, ":join_even_you_do_not_like_player", 1),

          (party_quick_attach_to_current_battle, ":party_no", 0), #attach as friend
          (str_store_party_name, s1, ":party_no"),
          (display_message, "str_s1_joined_battle_friend"),
        (try_end),
      (try_end),
  ]),
    
    # script_party_wound_all_members_aux
    # Input: arg1 = party_no
    ("party_wound_all_members_aux",
      [
        (store_script_param_1, ":party_no"),
        
        (party_get_num_companion_stacks, ":num_stacks",":party_no"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop",":party_no",":i_stack"),
          (try_begin),
            (neg|troop_is_hero, ":stack_troop"),
            (party_stack_get_size, ":stack_size",":party_no",":i_stack"),
            (party_wound_members, ":party_no", ":stack_troop", ":stack_size"),
          (else_try),
            (troop_set_health, ":stack_troop", 0),
          (try_end),
        (try_end),
        (party_get_num_attached_parties, ":num_attached_parties", ":party_no"),
        (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
          (party_get_attached_party_with_rank, ":attached_party", ":party_no", ":attached_party_rank"),
          (call_script, "script_party_wound_all_members_aux", ":attached_party"),
        (try_end),
    ]),
    
    # script_party_wound_all_members
    # Input: arg1 = party_no
    ("party_wound_all_members",
      [
        (store_script_param_1, ":party_no"),
        
        (call_script, "script_party_wound_all_members_aux", ":party_no"),
    ]),
    
    
    
    # script_calculate_battle_advantage
    # Output: reg0 = battle advantage
    ("calculate_battle_advantage",
      [
        ## CC
        (assign, ":total_gain", 0),
        (party_get_num_companion_stacks, ":num_stacks","p_encountered_party_backup"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop","p_encountered_party_backup",":i_stack"),
          (store_character_level, ":stack_strength", ":stack_troop"),
          (val_add, ":stack_strength", 12),
          (val_mul, ":stack_strength", ":stack_strength"),
          (val_div, ":stack_strength", 100),
          (try_begin),
            (neg|troop_is_hero, ":stack_troop"),
            (party_stack_get_size, ":stack_size","p_encountered_party_backup",":i_stack"),
            (store_mul, ":stack_gain", ":stack_strength", ":stack_size"),
          (else_try),
            (store_mul, ":stack_gain", ":stack_strength", 2),
          (try_end),
          (val_add, ":total_gain", ":stack_gain"),
        (try_end),
        (val_max, ":total_gain", 50),
        (val_sub, ":total_gain", 50),
        
        (store_div, ":bonus_chance", ":total_gain", 40),
        (val_min, ":bonus_chance", 100),
        (assign, reg0, ":bonus_chance"),
        (display_message, "@Bonus chance of loot: {reg0}%.", 0xFFFFFFFF),
        ## CC
        (call_script, "script_party_count_fit_for_battle", "p_collective_friends"),
        (assign, ":friend_count", reg(0)),
        
        (party_get_skill_level, ":player_party_tactics",  "p_main_party", skl_tactics),
        (party_get_skill_level, ":ally_party_tactics",  "p_collective_friends", skl_tactics),
        (val_max, ":player_party_tactics", ":ally_party_tactics"),
        
        (call_script, "script_party_count_fit_for_battle", "p_collective_enemy"),
        (assign, ":enemy_count", reg(0)),
        
        (party_get_skill_level, ":enemy_party_tactics",  "p_collective_enemy", skl_tactics),
        
        (val_add, ":friend_count", 1),
        (val_add, ":enemy_count", 1),
        
        (try_begin),
          (ge, ":friend_count", ":enemy_count"),
          (val_mul, ":friend_count", 100),
          (store_div, ":ratio", ":friend_count", ":enemy_count"),
          (store_sub, ":raw_advantage", ":ratio", 100),
        (else_try),
          (val_mul, ":enemy_count", 100),
          (store_div, ":ratio", ":enemy_count", ":friend_count"),
          (store_sub, ":raw_advantage", 100, ":ratio"),
        (try_end),
        (val_mul, ":raw_advantage", 2),
        
        (val_mul, ":player_party_tactics", 30),
        (val_mul, ":enemy_party_tactics", 30),
        (val_add, ":raw_advantage", ":player_party_tactics"),
        (val_sub, ":raw_advantage", ":enemy_party_tactics"),
        (val_div, ":raw_advantage", 100),
        
        
        (assign, reg0, ":raw_advantage"),
        (display_message, "@Battle Advantage = {reg0}.", 0xFFFFFFFF),
    ]),
    
    
    # script_cf_check_enemies_nearby
    # Input: none
    # Output: none, fails when enemies are nearby
    ("cf_check_enemies_nearby",
      [
        (get_player_agent_no, ":player_agent"),
        (agent_is_alive, ":player_agent"),
        (agent_get_position, pos1, ":player_agent"),
        (assign, ":result", 0),
        (set_fixed_point_multiplier, 100),
        (try_for_agents,":cur_agent"),
          (neq, ":cur_agent", ":player_agent"),
          (agent_is_alive, ":cur_agent"),
          (agent_is_human, ":cur_agent"),
          (neg|agent_is_ally, ":cur_agent"),
          (agent_get_position, pos2, ":cur_agent"),
          (get_distance_between_positions, ":cur_distance", pos1, pos2),
          (le, ":cur_distance", 1500), #15 meters
          (assign, ":result", 1),
        (try_end),
        (eq, ":result", 0),
    ]),
    
    # script_get_heroes_attached_to_center_aux
    # For internal use only
    ("get_heroes_attached_to_center_aux",
      [
        (store_script_param_1, ":center_no"),
        (store_script_param_2, ":party_no_to_collect_heroes"),
        (party_get_num_companion_stacks, ":num_stacks",":center_no"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop",":center_no",":i_stack"),
          (troop_is_hero, ":stack_troop"),
          (party_add_members, ":party_no_to_collect_heroes", ":stack_troop", 1),
        (try_end),
        (party_get_num_attached_parties, ":num_attached_parties", ":center_no"),
        (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
          (party_get_attached_party_with_rank, ":attached_party", ":center_no", ":attached_party_rank"),
          (call_script, "script_get_heroes_attached_to_center_aux", ":attached_party", ":party_no_to_collect_heroes"),
        (try_end),
    ]),
    
    # script_get_heroes_attached_to_center
    # Input: arg1 = center_no, arg2 = party_no_to_collect_heroes
    # Output: none, adds heroes to the party_no_to_collect_heroes party
    ("get_heroes_attached_to_center",
      [
        (store_script_param_1, ":center_no"),
        (store_script_param_2, ":party_no_to_collect_heroes"),
        (party_clear, ":party_no_to_collect_heroes"),
        (call_script, "script_get_heroes_attached_to_center_aux", ":center_no", ":party_no_to_collect_heroes"),
        
        #rebellion changes begin -Arma
        (try_for_range, ":pretender", pretenders_begin, pretenders_end),
          (neq, ":pretender", "$supported_pretender"),
          (troop_slot_eq, ":pretender", slot_troop_cur_center, ":center_no"),
          (party_add_members, ":party_no_to_collect_heroes", ":pretender", 1),
        (try_end),
        
        #     (try_for_range, ":rebel_faction", rebel_factions_begin, rebel_factions_end),
        #        (faction_slot_eq, ":rebel_faction", slot_faction_state, sfs_inactive_rebellion),
        #        (faction_slot_eq, ":rebel_faction", slot_faction_inactive_leader_location, ":center_no"),
        #        (faction_get_slot, ":pretender", ":rebel_faction", slot_faction_leader),
        #        (party_add_members, ":party_no_to_collect_heroes", ":pretender", 1),
        #     (try_end),
        #rebellion changes end
        
        
    ]),
    
    
    # script_get_heroes_attached_to_center_as_prisoner_aux
    # For internal use only
    ("get_heroes_attached_to_center_as_prisoner_aux",
      [
        (store_script_param_1, ":center_no"),
        (store_script_param_2, ":party_no_to_collect_heroes"),
        (party_get_num_prisoner_stacks, ":num_stacks",":center_no"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_prisoner_stack_get_troop_id, ":stack_troop",":center_no",":i_stack"),
          (troop_is_hero, ":stack_troop"),
          (party_add_members, ":party_no_to_collect_heroes", ":stack_troop", 1),
        (try_end),
        (party_get_num_attached_parties, ":num_attached_parties", ":center_no"),
        (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
          (party_get_attached_party_with_rank, ":attached_party", ":center_no", ":attached_party_rank"),
          (call_script, "script_get_heroes_attached_to_center_as_prisoner_aux", ":attached_party", ":party_no_to_collect_heroes"),
        (try_end),
    ]),
    
    
    # script_get_heroes_attached_to_center_as_prisoner
    # Input: arg1 = center_no, arg2 = party_no_to_collect_heroes
    # Output: none, adds heroes to the party_no_to_collect_heroes party
    ("get_heroes_attached_to_center_as_prisoner",
      [
        (store_script_param_1, ":center_no"),
        (store_script_param_2, ":party_no_to_collect_heroes"),
        (party_clear, ":party_no_to_collect_heroes"),
        (call_script, "script_get_heroes_attached_to_center_as_prisoner_aux", ":center_no", ":party_no_to_collect_heroes"),
    ]),
    
    ##
    ##  # script_cf_get_party_leader
    ##  # Input: arg1 = party_no
    ##  # Output: reg0 = troop_no of the leader (Can fail)
    ##  ("cf_get_party_leader",
    ##    [
    ##      (store_script_param_1, ":party_no"),
    ##
    ##      (party_get_num_companion_stacks, ":num_stacks",":party_no"),
    ##      (gt, ":num_stacks", 0),
    ##      (party_stack_get_troop_id, ":stack_troop", ":party_no", 0),
    ##      (troop_is_hero, ":stack_troop"),
    ##      (assign, reg0, ":stack_troop"),
    ##  ]),
    
    # script_give_center_to_faction
    # Input: arg1 = center_no, arg2 = faction
    ("give_center_to_faction",
      [
        (store_script_param_1, ":center_no"),
        (store_script_param_2, ":faction_no"),
        
        ##diplomacy begin
        (party_set_slot, ":center_no", dplmc_slot_center_taxation, 0),
        (try_begin),
			##Floris MTT begin
			(troop_get_slot,":woman_peasant","$troop_trees",slot_woman_peasant),
			(party_slot_eq, ":center_no", slot_village_infested_by_bandits, ":woman_peasant"),
			##Floris MTT end
          (party_set_slot, ":center_no", slot_village_infested_by_bandits, 0),
        (try_end),
        (try_begin),
          (eq, "$g_constable_training_center", ":center_no"),
          (assign, "$g_constable_training_center", -1),
        (try_end),
        ##diplomacy end
        (try_begin),
          (eq, ":faction_no", "fac_player_supporters_faction"),
          (faction_get_slot, ":player_faction_king", "fac_player_supporters_faction", slot_faction_leader),
          (eq, ":player_faction_king", "trp_player"),
          
          (try_begin),
            (is_between, ":center_no", walled_centers_begin, walled_centers_end),
            (assign, ":number_of_walled_centers_players_kingdom_has", 1),
          (else_try),
            (assign, ":number_of_walled_centers_players_kingdom_has", 0),
          (try_end),
          
          (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
            (store_faction_of_party, ":owner_faction_no", ":walled_center"),
            (eq, ":owner_faction_no", "fac_player_supporters_faction"),
            (val_add, ":number_of_walled_centers_players_kingdom_has", 1),
          (try_end),
          
          (ge, ":number_of_walled_centers_players_kingdom_has", 10),
          (unlock_achievement, ACHIEVEMENT_VICTUM_SEQUENS),
        (try_end),
        
        (try_begin),
          (check_quest_active, "qst_join_siege_with_army"),
          (quest_slot_eq, "qst_join_siege_with_army", slot_quest_target_center, ":center_no"),
          (call_script, "script_abort_quest", "qst_join_siege_with_army", 0),
          #Reactivating follow army quest
          (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
          (str_store_troop_name_link, s9, ":faction_marshall"),
          (setup_quest_text, "qst_follow_army"),
          (str_store_string, s2, "@{s9} wants you to resume following his army until further notice."),
          (call_script, "script_start_quest", "qst_follow_army", ":faction_marshall"),
          (assign, "$g_player_follow_army_warnings", 0),
        (try_end),
        
        #(store_faction_of_party, ":old_faction", ":center_no"),
        (call_script, "script_give_center_to_faction_aux", ":center_no", ":faction_no"),
        (call_script, "script_update_village_market_towns"),
        
        (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
          (call_script, "script_faction_recalculate_strength", ":cur_faction"),
        (try_end),
        (assign, "$g_recalculate_ais", 1),
        
        (try_begin),
          (eq, ":faction_no", "fac_player_supporters_faction"),
          (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
          (call_script, "script_activate_player_faction", "trp_player"),
        (try_end),
        
        #(call_script, "script_activate_deactivate_player_faction", ":old_faction"),
        #(try_begin),
        #(eq, ":faction_no", "fac_player_supporters_faction"),
        #(faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
        #(call_script, "script_give_center_to_lord", ":center_no", "trp_player", 0),
        
        #check with Armagan -- what is this here for?
        #(try_for_range, ":cur_village", villages_begin, villages_end),
        #(store_faction_of_party, ":cur_village_faction", ":cur_village"),
        #(eq, ":cur_village_faction", "fac_player_supporters_faction"),
        #(neg|party_slot_eq, ":cur_village", slot_town_lord, "trp_player"),
        #(call_script, "script_give_center_to_lord", ":cur_village", "trp_player", 0),
        #(try_end),
        #(try_end),
    ]),
    
  # script_give_center_to_faction_aux
  # Input: arg1 = center_no, arg2 = faction
  ("give_center_to_faction_aux",
    [
      (store_script_param_1, ":center_no"),
      (store_script_param_2, ":faction_no"),

      (store_faction_of_party, ":old_faction", ":center_no"),
      (party_set_faction, ":center_no", ":faction_no"),

      (try_begin),
        (party_slot_eq, ":center_no", slot_party_type, spt_village),
        (party_get_slot, ":farmer_party", ":center_no", slot_village_farmer_party),
        (gt, ":farmer_party", 0),
        (party_is_active, ":farmer_party"),
        (party_set_faction, ":farmer_party", ":faction_no"),
      (try_end),

      (try_begin),
	    #This bit of seemingly redundant code (the neq condition) is designed to prevent a bug that occurs when a player first conquers a center -- apparently this script is called again AFTER it is handed to a lord
		#Without this line, then the player's dialog selection does not have any affect, because town_lord is set again to stl_unassigned after the player makes his or her choice
	    (neq, ":faction_no", ":old_faction"),
		##diplomacy start+
		(party_get_slot, ":old_ex_faction", ":center_no", slot_center_ex_faction),
		##diplomacy end+
        (party_set_slot, ":center_no", slot_center_ex_faction, ":old_faction"),
        (party_get_slot, ":old_town_lord", ":center_no", slot_town_lord),
		##diplomacy start+
		(store_current_hours, ":hours"),
		(party_get_slot, ":old_ex_lord", ":center_no", dplmc_slot_center_ex_lord),
		#(party_get_slot, ":old_last_transfer", ":center_no", dplmc_slot_center_last_transfer_time),
		(try_begin),
			#When a faction regains a lost fief, if the ex-lord is a member of that faction,
			#don't erase that information.
			(this_or_next|party_slot_eq, ":center_no", slot_center_original_faction, ":faction_no"),#Handle several rapid sequential transfers
				(eq, ":old_ex_faction", ":faction_no"),
			(is_between, ":old_ex_lord", heroes_begin, heroes_end),
			(store_faction_of_troop, ":old_ex_lord_faction", ":old_ex_lord"),
			(eq, ":old_ex_lord_faction", ":faction_no"),
		(else_try),
			#Otherwise, if the center had a lord before this transfer, set the
			#ex-lord to the lord losing this.
			(neq, ":old_town_lord", stl_unassigned),
			(ge, ":old_town_lord", 0),
			(this_or_next|ge, ":old_town_lord", 1),#Don't apply to the player at the start of the game
				(gt, ":hours", 0),
			
			#Don't apply to fiefs lost by the faction leader, except for his "home",
			#and any fiefs with him marked as the original lord.
			(call_script, "script_dplmc_get_troop_standing_in_faction", ":old_town_lord", ":old_faction"),
			(this_or_next|lt, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
			(this_or_next|troop_slot_eq, ":old_faction", slot_troop_home, ":center_no"),
				(party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":old_town_lord"),
			
			(party_set_slot, ":center_no", dplmc_slot_center_ex_lord, ":old_town_lord"),
		(try_end),
        (party_set_slot, ":center_no", dplmc_slot_center_last_transfer_time, ":hours"),
		##diplomacy end+
        (party_set_slot, ":center_no", slot_town_lord, stl_unassigned),
        (party_set_banner_icon, ":center_no", 0),#Removing banner
        (call_script, "script_update_faction_notes", ":old_faction"),
        #Invalidate old lord's cached center points
        (gt, ":old_town_lord", -1),
        (troop_set_slot, ":old_town_lord", dplmc_slot_troop_center_points_plus_one, 0),
      (try_end),

      (call_script, "script_update_faction_notes", ":faction_no"),
      (call_script, "script_update_center_notes", ":center_no"),

      (try_begin),
        (ge, ":old_town_lord", 0),
        (neq, ":faction_no", "fac_player_supporters_faction"),
        (call_script, "script_update_troop_notes", ":old_town_lord"),
      (try_end),

      (try_for_range, ":other_center", centers_begin, centers_end),
        (party_slot_eq, ":other_center", slot_village_bound_center, ":center_no"),
        ##diplomacy start+ Avoid infinite recursion even if some foolish modder (such as myself)
        #has set up bizarre cyclic dependencies
        (store_faction_of_party, ":other_center_faction", ":other_center"),
        ##The "this or next" is so that any weird uses of this function
        ##in Native (to change something to its own faction) will be
        ##replicated.  The reason this works is that all villages have
        ##higher ID numbers than castles or towns.
        (this_or_next|gt, ":other_center", ":center_no"),
        (neq, ":other_center_faction", ":old_faction"),
        ##diplomacy end+
        (call_script, "script_give_center_to_faction_aux", ":other_center", ":faction_no"),
      (try_end),
  ]),
    
	  # script_change_troop_faction
	  # Input: arg1 = troop_no, arg2 = faction
	  ("change_troop_faction",
		[
		  (store_script_param_1, ":troop_no"),
		  (store_script_param_2, ":faction_no"),
		  (try_begin),
			#Reactivating inactive or defeated faction
			(is_between, ":faction_no", kingdoms_begin, kingdoms_end),
			(neg|faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
			(faction_set_slot, ":faction_no", slot_faction_state, sfs_active),
			#(call_script, "script_store_average_center_value_per_faction"),
		  (try_end),

		  #Political ramifications
		  (store_faction_of_troop, ":orig_faction", ":troop_no"),
		  ##diplomacy start+ save these for reference
		  #(faction_get_slot, ":orig_faction_leader", ":orig_faction", slot_faction_leader),
		  (faction_get_slot, ":new_faction_leader", ":faction_no", slot_faction_leader),
		  (try_begin),
			  #Avoid letting heroes get stuck as slto_inactive if petitioners switch away from the player's faction
			  (eq, ":orig_faction", "fac_player_supporters_faction"),
		     (gt, ":troop_no", 0),
		     (troop_is_hero, ":troop_no"),
			  (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive),
			  (this_or_next|is_between, ":troop_no", lords_begin, lords_end),
			  (this_or_next|is_between, ":troop_no", kings_begin, kings_end),
			  (this_or_next|is_between, ":troop_no", pretenders_begin, pretenders_end),
			  (this_or_next|troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
			     (troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_lord_rejoined),
			  (troop_set_slot, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
		  (try_end),
		  ##diplomacy end+

		  #remove if he is marshal
		  (try_begin),
			(faction_slot_eq, ":orig_faction", slot_faction_marshall, ":troop_no"),
			(call_script, "script_check_and_finish_active_army_quests_for_faction", ":orig_faction"),

			#No current issue on the agenda
			(try_begin),
				(faction_slot_eq, ":orig_faction", slot_faction_political_issue, 0),

				(faction_set_slot, ":orig_faction", slot_faction_political_issue, 1), #Appointment of marshal
				(store_current_hours, ":hours"),
				(val_max, ":hours", 0),
				(faction_set_slot, ":orig_faction", slot_faction_political_issue_time, ":hours"), #Appointment of marshal
				##diplomacy start+ Reset political stance for kingdom ladies as well
				#(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),##OLD
				(try_for_range, ":active_npc", heroes_begin, heroes_end),##NEW
				##diplomacy end+
					(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
					(eq, ":active_npc_faction", ":orig_faction"),
					(troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
				(try_end),
				(try_begin),
					(eq, "$players_kingdom", ":orig_faction"),
					(troop_set_slot, "trp_player", slot_troop_stance_on_faction_issue, -1),
				(try_end),
			(try_end),

			(try_begin),
			  (troop_get_slot, ":old_marshall_party", ":troop_no", slot_troop_leaded_party),
			  (party_is_active, ":old_marshall_party"),
			  (party_set_marshall, ":old_marshall_party", 0),
			(try_end),

			(faction_set_slot, ":orig_faction", slot_faction_marshall, -1),
		  (try_end),
		  #Removal as marshal ends

		  #Other political ramifications
		  (troop_set_slot, ":troop_no", slot_troop_stance_on_faction_issue, -1),
		  ##diplomacy start+ Support promoted kingdom ladies
		  #(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
		  (try_for_range, ":active_npc", heroes_begin, heroes_end),
		  ##diplomacy end+
			(troop_slot_eq, ":active_npc", slot_troop_stance_on_faction_issue, ":troop_no"),
			(troop_set_slot, ":active_npc", slot_troop_stance_on_faction_issue, -1),
		  (try_end),
		  #Political ramifications end
        
        ## Begin 1.134
        (try_begin),
          (ge, "$cheat_mode", 1),
          (str_store_troop_name, s4, ":troop_no"),
          (display_message, "@{!}DEBUG - {s4} faction changed in normal faction change"),
        (try_end),
        ## End 1.134
        
		  (troop_set_faction, ":troop_no", ":faction_no"),
		  ##diplomacy start+
		  ##Don't give lords amnesia about what the player said to recruit them.
		  ##OLD:
		  #(troop_set_slot, ":troop_no", slot_troop_recruitment_random, 0),
		  #(troop_set_slot, ":troop_no", slot_lord_recruitment_argument, 0),
		  #(troop_set_slot, ":troop_no", slot_lord_recruitment_candidate, 0),
		  #(troop_set_slot, ":troop_no", slot_troop_promised_fief, 0),
		  ##NEW
		  (try_begin),
			 (eq, ":troop_no", "trp_player"),
			 #Don't change of this for the player.
		  (else_try),
			(is_between, ":faction_no", kingdoms_begin, kingdoms_end),
			 (this_or_next|eq, ":faction_no", "fac_player_supporters_faction"),
				(eq, ":faction_no", "$players_kingdom"),
			 (ge, ":new_faction_leader", 0),
			 (this_or_next|eq, ":faction_no", "fac_player_supporters_faction"),
			 (this_or_next|eq, ":new_faction_leader", "trp_player"),
			 (this_or_next|troop_slot_eq, ":new_faction_leader", slot_troop_spouse, "trp_player"),
				(troop_slot_eq, "trp_player", slot_troop_spouse, ":new_faction_leader"),
			 #Joined faction that player is ruler or co-ruler of.  Don't forget
			 #any promises received.
			 (troop_set_slot, ":troop_no", slot_troop_recruitment_random, 0),
		  (else_try),
			 #Joined a new faction.  Previous promises moot.
			 (troop_set_slot, ":troop_no", slot_troop_recruitment_random, 0),
			 (troop_set_slot, ":troop_no", slot_lord_recruitment_argument, 0),
			 (troop_set_slot, ":troop_no", slot_lord_recruitment_candidate, 0),
			 (troop_set_slot, ":troop_no", slot_troop_promised_fief, 0),
		  (try_end),
		  ##diplomacy end+

		  #Give new title
		  (call_script, "script_troop_set_title_according_to_faction", ":troop_no", ":faction_no"),

		  (try_begin),
			(this_or_next|eq, ":faction_no", "$players_kingdom"),
			(eq, ":faction_no", "fac_player_supporters_faction"),
			(call_script, "script_check_concilio_calradi_achievement"),
		  (try_end),
        
	  #Takes walled centers and dependent villages with him
      (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
        (party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
        (party_set_faction, ":center_no", ":faction_no"),
        (try_for_range, ":village_no", villages_begin, villages_end),
          (party_slot_eq, ":village_no", slot_village_bound_center, ":center_no"),
          (party_set_faction, ":village_no", ":faction_no"),
          (party_get_slot, ":farmer_party_no", ":village_no", slot_village_farmer_party),
          (try_begin),
            (gt, ":farmer_party_no", 0),
            (party_is_active, ":farmer_party_no"),
            (party_set_faction, ":farmer_party_no", ":faction_no"),
          (try_end),
          (try_begin),
            (party_get_slot, ":old_town_lord", ":village_no", slot_town_lord),
            (neq, ":old_town_lord", ":troop_no"),
            (party_set_slot, ":village_no", slot_town_lord, stl_unassigned),
            ##diplomacy start+ Invalidate old lord's cached center points
            (gt, ":old_town_lord", -1),
            (troop_set_slot, ":old_town_lord", dplmc_slot_troop_center_points_plus_one, 0),
            ##diplomacy end+
          (try_end),
        (try_end),
      (try_end),

        
        #LAZERAS MODIFIED  {ENTK}
        #Remove his control over villages under another fortress
        (try_for_range, ":village_no", villages_begin, villages_end),
          (party_slot_eq, ":village_no", slot_town_lord, ":troop_no"),
          (store_faction_of_party, ":village_faction", ":village_no"),
          (try_begin),
            (neq, ":village_faction", ":faction_no"),
            (party_set_slot, ":village_no", slot_town_lord, stl_unassigned),
	          ##diplomacy start+ invalidate cached center points
	          (gt, ":old_town_lord", -1),
	          (troop_set_slot, ":troop_no", dplmc_slot_troop_center_points_plus_one, 0),
	          ##diplomacy end+
	        (try_end),
        (try_end),
        
        # Jrider + TITLES v0.0 Give new title
        (call_script, "script_troop_set_title_according_to_faction", ":troop_no", ":faction_no"),
        # Jrider -
        
        #Dependant kingdom ladies switch faction
		(try_for_range, ":kingdom_lady", kingdom_ladies_begin, kingdom_ladies_end),
		##diplomacy start+ This is required if kingdom ladies can be promoted to other roles
        (this_or_next|troop_slot_eq, ":kingdom_lady", slot_troop_occupation, 0),#for prisoners
		   (troop_slot_eq, ":kingdom_lady", slot_troop_occupation, slto_kingdom_lady),
			(store_faction_of_troop, reg0, ":kingdom_lady"),
			(this_or_next|eq, reg0, ":orig_faction"),
			(neg|faction_slot_eq, reg0, slot_faction_state, sfs_active),
			##diplomacy end+
          (call_script, "script_get_kingdom_lady_social_determinants", ":kingdom_lady"),
          (assign, ":closest_male_relative", reg0),
          (assign, ":new_center", reg1),
          
          (eq, ":closest_male_relative", ":troop_no"),
          ## Begin 1.134
          (try_begin),
            (ge, "$cheat_mode", 1),
            (str_store_troop_name, s4, ":kingdom_lady"),
            (display_message, "@{!}DEBUG - {s4} faction changed by guardian moving"),
          (try_end),
          ## End 1.134
		  
          (troop_set_faction, ":kingdom_lady", ":faction_no"),
          # Jrider + TITLES v0.0 change ladies title
          (call_script, "script_troop_set_title_according_to_faction", ":kingdom_lady", ":faction_no"),
          # Jrider -
          (troop_slot_eq, ":kingdom_lady", slot_troop_prisoner_of_party, -1),
          (troop_set_slot, ":kingdom_lady", slot_troop_cur_center, ":new_center"),
        (try_end),
        #LAZERAS MODIFIED  {ENTK}
        
        #Free prisoners
        (try_begin),
          (troop_get_slot, ":leaded_party", ":troop_no", slot_troop_leaded_party),
          (gt, ":leaded_party", 0),
          (party_set_faction, ":leaded_party", ":faction_no"),
          (party_get_num_prisoner_stacks, ":num_stacks", ":leaded_party"),
          (try_for_range_backwards, ":troop_iterator", 0, ":num_stacks"),
            (party_prisoner_stack_get_troop_id, ":cur_troop_id", ":leaded_party", ":troop_iterator"),
            (store_troop_faction, ":cur_faction", ":cur_troop_id"),
            (troop_is_hero, ":cur_troop_id"),
            (eq, ":cur_faction", ":faction_no"),
            (call_script, "script_remove_troop_from_prison", ":cur_troop_id"),
            (party_remove_prisoners, ":leaded_party", ":cur_troop_id", 1),
          (try_end),
        (try_end),
        
        #Annull all quests of which the lord is giver
        (try_for_range, ":quest", all_quests_begin, all_quests_end),
          (check_quest_active, ":quest"),
          (quest_slot_eq, ":quest", slot_quest_giver_troop, ":troop_no"),
          
          (str_store_troop_name, s4, ":troop_no"),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (display_message, "str_s4_changing_sides_aborts_quest"),
          (try_end),
          (call_script, "script_abort_quest", ":quest", 0),
        (try_end),
        
	  #Boot all lords out of centers whose faction has changed
	  ##diplomacy start+ add check for promoted kingdom ladies
	  #(try_for_range, ":lord_to_move", active_npcs_begin, active_npcs_end),
	  (try_for_range, ":lord_to_move", heroes_begin, heroes_end),
		 (troop_slot_ge, ":lord_to_move", slot_troop_leaded_party, 1),
	  ##diplomacy end+
		(troop_get_slot, ":lord_led_party", ":lord_to_move", slot_troop_leaded_party),
	    (party_is_active, ":lord_led_party"),
		(party_get_attached_to, ":led_party_attached", ":lord_led_party"),
		(is_between, ":led_party_attached", walled_centers_begin, walled_centers_end),
		(store_faction_of_party, ":led_party_faction", ":lord_led_party"),
		(store_faction_of_party, ":attached_party_faction", ":led_party_attached"),
		(neq, ":led_party_faction", ":attached_party_faction"),

		(party_detach, ":lord_led_party"),
	  (try_end),
        
        #Increase relation with lord in new faction by 5
        #Or, if player kingdom, make inactive pending confirmation
        (faction_get_slot, ":faction_liege", ":faction_no", slot_faction_leader),
        (try_begin),
          (eq, ":faction_liege", "trp_player"),
          (neq, ":troop_no", "$g_talk_troop"),
          (troop_set_slot, ":troop_no", slot_troop_occupation, slto_inactive), #POSSIBLE REASON 1
	  (else_try),
		   ##diplomacy start+ Add support for promoted ladies
			##OLD:
			#(is_between, ":faction_liege", active_npcs_begin, active_npcs_end),
			#(is_between, ":troop_no", active_npcs_begin, active_npcs_end),
			##NEW:
			(is_between, ":faction_liege", heroes_begin, heroes_end),
			(is_between, ":troop_no", heroes_begin, heroes_end),
			##diplomacy end+
          (call_script, "script_troop_change_relation_with_troop", ":faction_liege", ":troop_no", 5),
          (val_add, "$total_indictment_changes", 5),
        (try_end),
        
	  #Break courtship relations
	  (try_begin),
	  	(troop_slot_ge, ":troop_no", slot_troop_spouse, 0),
		#Already married, do nothing
	  (else_try),
		(is_between, ":troop_no", active_npcs_begin, active_npcs_end),
		##diplomacy start+
		#Bug fix: don't do this for pretenders.
		(neg|is_between, ":troop_no", kings_begin, kings_end),
		(neg|is_between, ":troop_no", pretenders_begin, pretenders_end),
		##diplomacy end+
	    (try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
			(troop_get_slot, ":courted_lady", ":troop_no", ":love_interest_slot"),
            ##diplomacy start+ don't call this for bad values
            (is_between, ":courted_lady", kingdom_ladies_begin, kingdom_ladies_end),			
            ##diplomacy end+
			(call_script, "script_courtship_event_lady_break_relation_with_suitor", ":courted_lady", ":troop_no"),
	    (try_end),
		##diplomacy start+
		# Don't call this script for married troops / rulers
		#(call_script, "script_assign_troop_love_interests", ":troop_no"),
		(try_begin),
			(neg|troop_slot_ge, ":troop_no", slot_troop_spouse, 0),
			(neg|is_between, ":troop_no", kings_begin, kings_end),
			(neg|is_between, ":troop_no", pretenders_begin, pretenders_end),
			(call_script, "script_assign_troop_love_interests", ":troop_no"),
		(try_end),
		##diplomacy end+
	  (else_try),
		(is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
		(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
			(try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
				(troop_slot_eq, ":active_npc", ":love_interest_slot", ":troop_no"),
				(call_script, "script_courtship_event_lady_break_relation_with_suitor", ":troop_no", ":active_npc"),
			(try_end),
		(try_end),
	  (try_end),

	  #Stop raidings/sieges of new faction's fief if there is any
	  (troop_get_slot, ":troop_party", ":troop_no", slot_troop_leaded_party),
	  (try_for_range, ":center_no", centers_begin, centers_end),
	    (party_slot_eq, ":center_no", slot_party_type, spt_village),
	    (party_get_slot, ":raided_by", ":center_no", slot_village_raided_by),
	    (eq, ":raided_by", ":troop_party"),
	    (party_set_slot, ":center_no", slot_village_raided_by, -1),
	    (try_begin),
	      (party_slot_eq, ":center_no", slot_village_state, svs_being_raided),
	      (party_set_slot, ":center_no", slot_village_state, svs_normal),
	      (party_set_extra_text, ":center_no", "str_empty_string"),
	    (try_end),
	  (else_try),
	    (party_get_slot, ":besieged_by", ":center_no", slot_center_is_besieged_by),
	    (eq, ":besieged_by", ":troop_party"),
	    (party_set_slot, ":center_no", slot_center_is_besieged_by, -1),
	    (try_begin),
	      (party_slot_eq, ":center_no", slot_village_state, svs_under_siege),
	      (party_set_slot, ":center_no", slot_village_state, svs_normal),
	      (party_set_extra_text, ":center_no", "str_empty_string"),
	    (try_end),
	  (try_end),

      (call_script, "script_update_all_notes"),

      (call_script, "script_update_village_market_towns"),
      (assign, "$g_recalculate_ais", 1),
      ]),

  # script_troop_set_title_according_to_faction
  # Input: arg1 = troop_no, arg2 = faction_no
  # EDITED FROM NATIVE TO ALLOW CUSTOM PLAYER KINGDOM TITLES	  
  ("troop_set_title_according_to_faction",
   [
      (store_script_param, ":troop_no", 1),
      (store_script_param, ":faction_no", 2),
      (try_begin), #Floris 2.52 bugfix #Caba
	    (ge, ":troop_no", 0), #Floris bugfix #Caba
        (assign, ":custom_name", 0),
        (try_begin),
            (eq, ":faction_no", "fac_player_supporters_faction"),
			(neq, ":troop_no", "trp_player"),
            (try_begin),
			  (eq, ":troop_no", "trp_npc10"), #For Bunduk
			  (str_store_troop_name_plural, s12, ":troop_no"),
              (str_store_string, s1, "str_tribune_s12"),
			  (assign, ":custom_name", 1),
			(else_try),
			  (troop_get_type, ":gender", ":troop_no"),
              (eq, ":gender", 0), #male
              (troop_slot_eq, "trp_heroes_end", 0, 1),
              (str_store_troop_name, s0, "trp_heroes_end"),
              (str_store_troop_name_plural, s1, ":troop_no"),
              (str_store_string, s1, "str_s0_s1"),
              (assign, ":custom_name", 1),              
            (else_try),
              (eq, ":gender", 1), #female
              (troop_slot_eq, "trp_heroes_end", 1, 1),
              (str_store_troop_name_plural, s0, "trp_heroes_end"),
              (str_store_troop_name_plural, s1, ":troop_no"),
              (str_store_string, s1, "str_s0_s1"),
              (assign, ":custom_name", 1),              
            (try_end),
            (eq, ":custom_name", 1), #So if it fails, will rename normally
            (troop_set_name, ":troop_no", s1),
            (troop_get_slot, ":troop_party", ":troop_no", slot_troop_leaded_party),
            (try_begin),
                (gt, ":troop_party", 0),
                (str_store_troop_name, s5, ":troop_no"),
                (party_set_name, ":troop_party", "str_s5_s_party"),
            (try_end),
        (else_try),
        #LAZERAS MODIFIED  {ENTK}
		    (neq, ":troop_no", "trp_player"), # exclude player
            (call_script, "script_troop_set_title_according_to_faction_gender_and_lands", ":troop_no", ":faction_no"),
        #        (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
        #        (str_store_troop_name_plural, s0, ":troop_no"),
        #        (troop_get_type, ":gender", ":troop_no"),
        #        (store_sub, ":title_index", ":faction_no", kingdoms_begin),
        #        (try_begin),
        ##Floris: Updated from CC 1.321, which is disabled in 1.322.
        #          ## CC
        #          (is_between, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
        #          (faction_slot_eq, ":faction_no", slot_faction_leader, ":troop_no"),
        #          (val_add, ":title_index", king_titles_begin),
        #          ## CC
        #        (else_try),    
        ##
        #          (eq, ":gender", 0), #male
        #          (val_add, ":title_index", kingdom_titles_male_begin),
        #        (else_try),
        #          (val_add, ":title_index", kingdom_titles_female_begin),
        #        (try_end),
        #        ## CC 1.322, 11 new lines
        #        (try_begin),
        #          (is_between, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
        #          (faction_slot_eq, ":faction_no", slot_faction_leader, ":troop_no"),
        #          (store_sub, ":title_index", ":faction_no", npc_kingdoms_begin),
        #          (try_begin),
        #            (eq, ":gender", 0), #male
        #            (val_add, ":title_index", king_titles_begin),
        #          (else_try),
        #            (val_add, ":title_index", king_titles_female_begin),
        #          (try_end),
        #        (try_end),
        #        ## CC
        #        (str_store_string, s1, ":title_index"),
        #        (troop_set_name, ":troop_no", s1),
        #        (troop_get_slot, ":troop_party", ":troop_no", slot_troop_leaded_party),
        #        (gt, ":troop_party", 0),
        #        (str_store_troop_name, s5, ":troop_no"),
        #        (party_set_name, ":troop_party", "str_s5_s_party"),
        (try_end),
	  (try_end), #Floris bugfix #Caba
    ]),
    
    # script_give_center_to_lord
    # Input: arg1 = center_no, arg2 = lord_troop, arg3 = add_garrison_to_center
  ("give_center_to_lord",
      [
        (store_script_param, ":center_no", 1),
        (store_script_param, ":lord_troop_id", 2), #-1 only in the case of a player deferring ownership of a center
        (store_script_param, ":add_garrison", 3),
        ##diplomacy begin
        (party_set_slot, ":center_no", dplmc_slot_center_taxation, 0),
        (try_begin),
			##Floris MTT begin
			(troop_get_slot,":woman_peasant","$troop_trees",slot_woman_peasant),
			(party_slot_eq, ":center_no", slot_village_infested_by_bandits, ":woman_peasant"),
			##Floris MTT end          
          (party_set_slot, ":center_no", slot_village_infested_by_bandits, 0),
        (try_end),
        ##diplomacy end
        
	  ##diplomacy start+
	  #For relation changes below, store all heroes' center points and closest fiefs.
	  (call_script, "script_dplmc_prepare_hero_center_points_ignoring_center", ":center_no"),

	  #(assign, ":player_declines_honor", 0),
	  #(try_begin),
	  #	  (gt, "$g_dont_give_fief_to_player_days", 1),
	  #	  (assign, ":player_declines_honor", 1),
	  #(try_end),
	  ##diplomacy end+

	  (try_begin),
	  ##diplomacy start+ notable events like this should be logged by default
	   (ge, ":lord_troop_id", 0),
		(str_store_party_name_link, s4, ":center_no"),
		(str_store_troop_name_link, s5, ":lord_troop_id"),
		(store_troop_faction, ":msg_faction_no", ":lord_troop_id"),
		#Floris - refine text
		(try_begin),
			(eq, ":msg_faction_no", "fac_player_faction"),
			(is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
			(assign, ":msg_faction_no", "$players_kingdom"),
		(try_end),
		#Floris - refine text end
		(str_store_faction_name_link, s7, ":msg_faction_no"),
		(try_begin),
		   (faction_slot_eq, ":msg_faction_no", slot_faction_leader, ":lord_troop_id"),
		   (display_log_message, "@{s5} of the {s7} has taken ownership of {s4}."),
		(else_try),
		   (display_log_message, "@{s4} has been awarded to {s5} of the {s7}."),
		(try_end),
	  (else_try),
	  ##diplomacy end+
          (eq, "$cheat_mode", 1),
          (ge, ":lord_troop_id", 0),
          (str_store_party_name, s4, ":center_no"),
          (str_store_troop_name, s5, ":lord_troop_id"),
          (display_message, "@{!}DEBUG -- {s4} awarded to {s5}"),
        (try_end),
        
        (try_begin),
          (eq, ":lord_troop_id", "trp_player"),
          (unlock_achievement, ACHIEVEMENT_ROYALITY_PAYMENT),
          
          (assign, ":number_of_fiefs_player_have", 1),
          (try_for_range, ":cur_center", centers_begin, centers_end),
            (neq, ":cur_center", ":center_no"),
            (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
            (val_add, ":number_of_fiefs_player_have", 1),
          (try_end),
          
          (ge, ":number_of_fiefs_player_have", 5),
          (unlock_achievement, ACHIEVEMENT_MEDIEVAL_EMLAK),
        (try_end),
        
        (party_get_slot, ":old_lord_troop_id", ":center_no", slot_town_lord),
        
        (try_begin), #This script is ONLY called with lord_troop_id = -1 when it is the player faction
		  ##diplomacy start+
		  #The player can now also be co-ruler of a NPC kingdom.
			 (eq, ":lord_troop_id", -1),

			 (is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
			 (faction_get_slot, ":players_kingdom_liege", "$players_kingdom", slot_faction_leader),
			 (gt, ":players_kingdom_liege", -1),
			 (this_or_next|eq, ":players_kingdom_liege", "trp_player"),
			 (this_or_next|troop_slot_eq, ":players_kingdom_liege", slot_troop_spouse, "trp_player"),
				(troop_slot_eq, "trp_player", slot_troop_spouse, ":players_kingdom_liege"),

			(assign, ":lord_troop_faction", "$players_kingdom"),
			(party_set_banner_icon, ":center_no", 0),#Removing banner
		  (else_try),
		  ##diplomacy end+
			(eq, ":lord_troop_id", -1),
			(assign, ":lord_troop_faction", "fac_player_supporters_faction"),
			(party_set_banner_icon, ":center_no", 0),#Removing banner
          
        (else_try),
          (eq, ":lord_troop_id", "trp_player"),
          (assign, ":lord_troop_faction", "$players_kingdom"), #was changed on Apr 27 from fac_plyr_sup_fac
          
        (else_try),
          (store_troop_faction, ":lord_troop_faction", ":lord_troop_id"),
        (try_end),
        (faction_get_slot, ":faction_leader", ":lord_troop_faction", slot_faction_leader),
        
	  (try_begin),															#	1.143 Port // Newly Added
	    (eq, ":faction_leader", "trp_player"),

        (try_begin),
            (troop_get_type, ":is_female", "trp_player"),
            (eq, ":is_female", 1),
            (unlock_achievement, ACHIEVEMENT_QUEEN),
        (try_end),
	  (try_end),															#	End
		
        (try_begin),
          (eq, ":faction_leader", ":old_lord_troop_id"),
          (call_script, "script_add_log_entry", logent_liege_grants_fief_to_vassal, ":faction_leader", ":center_no", ":lord_troop_id", ":lord_troop_faction"),
          (troop_set_slot, ":lord_troop_id", slot_troop_promised_fief, 0),
        (try_end),
        
        (try_begin),
          (eq, ":lord_troop_id", -1), #Lord troop ID -1 is only used when a player is deferring assignment of a fief
          (party_set_faction, ":center_no", "$players_kingdom"),
        (else_try),
          (eq, ":lord_troop_id", "trp_player"),
          (gt, "$players_kingdom", 0),
          (party_set_faction, ":center_no", "$players_kingdom"),
        (else_try),
          (eq, ":lord_troop_id", "trp_player"),
          (neg|is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
          (party_set_faction, ":center_no", "fac_player_supporters_faction"),
        (else_try),
          (party_set_faction, ":center_no", ":lord_troop_faction"),
        (try_end),
        (party_set_slot, ":center_no", slot_town_lord, ":lord_troop_id"),
        
        (try_begin),
          (party_slot_eq, ":center_no", slot_party_type, spt_village),
          (party_get_slot, ":farmer_party_no", ":center_no", slot_village_farmer_party),
          (gt, ":farmer_party_no", 0),
          (party_is_active, ":farmer_party_no"),
          (store_faction_of_party, ":center_faction", ":center_no"),
          (party_set_faction, ":farmer_party_no", ":center_faction"),
        (try_end),
        
        (try_begin),
          (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
          (party_slot_eq, ":center_no", slot_party_type, spt_castle),
          (gt, ":lord_troop_id", -1),
          
          #normal_banner_begin
          (troop_get_slot, ":cur_banner", ":lord_troop_id", slot_troop_banner_scene_prop),
          (gt, ":cur_banner", 0),
          (val_sub, ":cur_banner", banner_scene_props_begin),
          (val_add, ":cur_banner", banner_map_icons_begin),
          (party_set_banner_icon, ":center_no", ":cur_banner"),
          # custom_banner_begin
          #        (troop_get_slot, ":flag_icon", ":lord_troop_id", slot_troop_custom_banner_map_flag_type),
          #        (ge, ":flag_icon", 0),
          #        (val_add, ":flag_icon", custom_banner_map_icons_begin),
          #        (party_set_banner_icon, ":center_no", ":flag_icon"),
        (try_end),
        
        #    (try_begin),
        #		(eq, 1, 0),
        #       (eq, ":lord_troop_id", "trp_player"),
        #       (neq, ":old_lord_troop_id", "trp_player"),
        #       (party_get_slot, ":center_relation", ":center_no", slot_center_player_relation),
        #       (is_between, ":center_relation", -4, 5),
        #       (call_script, "script_change_player_relation_with_center", ":center_no", 5),
        #       (gt, ":old_lord_troop_id", 0),
        #       (call_script, "script_change_player_relation_with_troop", ":old_lord_troop_id", -25),
        #   (try_end),
        (try_begin),
          (gt, ":lord_troop_id", -1),
          (call_script, "script_update_troop_notes", ":lord_troop_id"),
        (try_end),
        
        (call_script, "script_update_center_notes", ":center_no"),
        
        (try_begin),
          (gt, ":lord_troop_faction", 0),
          (call_script, "script_update_faction_notes", ":lord_troop_faction"),
        (try_end),
        
        (try_begin),
          (ge, ":old_lord_troop_id", 0),
          (call_script, "script_update_troop_notes", ":old_lord_troop_id"),
          (store_troop_faction, ":old_lord_troop_faction", ":old_lord_troop_id"),
          (call_script, "script_update_faction_notes", ":old_lord_troop_faction"),
        (try_end),
        
        (try_begin),
          (eq, ":add_garrison", 1),
          (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
          (party_slot_eq, ":center_no", slot_party_type, spt_castle),
          (assign, ":garrison_strength", 3),
          (try_begin),
            (party_slot_eq, ":center_no", slot_party_type, spt_town),
            (assign, ":garrison_strength", 9),
          (try_end),
          (try_for_range, ":unused", 0, ":garrison_strength"),
            (call_script, "script_cf_reinforce_party", ":center_no"),
          (try_end),
          ## ADD some XP initially
          (try_for_range, ":unused", 0, 7),
            (store_mul, ":xp_range_min", 150, ":garrison_strength"),
            (store_mul, ":xp_range_max", 200, ":garrison_strength"),
            (store_random_in_range, ":xp", ":xp_range_min", ":xp_range_max"),
            (party_upgrade_with_xp, ":center_no", ":xp", 0),
          (try_end),
        (try_end),
        
        (faction_get_slot, ":faction_leader", ":lord_troop_faction", slot_faction_leader),
        (store_current_hours, ":hours"),
        
        #the next block handles gratitude, objections and jealousies
        (try_begin),
          (gt, ":hours", 0),
          (gt, ":lord_troop_id", 0),
          
          (call_script, "script_troop_change_relation_with_troop", ":lord_troop_id", ":faction_leader", 10),
          (val_add, "$total_promotion_changes", 10),
          
          #smaller factions are more dramatically influenced by internal jealousies
          ## Start 1.134
          #Disabled as of NOV 2010
          #		(try_begin),
          #			(neg|faction_slot_ge, ":lord_troop_faction", slot_faction_number_of_parties, 4),
          #			(assign, ":faction_size_multiplier", 6),
          #		(else_try),
          #			(neg|faction_slot_ge, ":lord_troop_faction", slot_faction_number_of_parties, 8),
          #			(assign, ":faction_size_multiplier", 5),
          #		(else_try),
          #			(neg|faction_slot_ge, ":lord_troop_faction", slot_faction_number_of_parties, 16),
          #			(assign, ":faction_size_multiplier", 4),
          #		(else_try),
          #			(neg|faction_slot_ge, ":lord_troop_faction", slot_faction_number_of_parties, 32),
          #			(assign, ":faction_size_multiplier", 3),
          #		(else_try),
          #			(assign, ":faction_size_multiplier", 2),
          #		(try_end),
          ## End 1.134
          
		#factional politics -- each lord in the faction adjusts his relation according to the relation with the lord receiving the faction
		##diplomacy start+ add support for kingdom ladies
		#(try_for_range, ":other_lord", active_npcs_begin, active_npcs_end),
		(try_for_range, ":other_lord", heroes_begin, heroes_end),
		##diplomacy end+
			(troop_slot_eq, ":other_lord", slot_troop_occupation, slto_kingdom_hero),
			(neq, ":other_lord", ":lord_troop_id"),

            (store_troop_faction, ":other_troop_faction", ":other_lord"),
            (eq, ":lord_troop_faction", ":other_troop_faction"),
            
            (neq, ":other_lord", ":faction_leader"),
            
            (call_script, "script_troop_get_relation_with_troop", ":other_lord", ":lord_troop_id"),
            ## Begin 1.134
            (assign, ":relation_with_troop", reg0),
            
            #relation reduction = relation/10 minus 2. So,0 = -2, 8 = -1, 16+ = no change or bonus, 24+ gain one point
            (store_div, ":relation_with_liege_change", ":relation_with_troop", 8), #changed from 16
            (val_sub, ":relation_with_liege_change", 2),
            
            (val_clamp, ":relation_with_liege_change", -5, 3),
            
            (try_begin),
              #upstanding and goodnatured lords will not lose relation unless they actively dislike the other lord
              (this_or_next|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_upstanding),
              (troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_goodnatured),
              (ge, ":relation_with_troop", 0),
              (val_max, ":relation_with_liege_change", 0),
            (else_try),
              #penalty is increased for lords who have the more unpleasant reputation types
              (this_or_next|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_selfrighteous),
              (this_or_next|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_debauched),
              (troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_quarrelsome),
              (lt, ":relation_with_liege_change", 0),
              (val_mul, ":relation_with_liege_change", 3),
              (val_div, ":relation_with_liege_change", 2),
            (try_end),
            
						##diplomacy start+

			#TODO (idea for "high"): instead of being absolute, the sliding score system should be used.
			#(So you can use a score instead of using relations.)  The greater the
			#difference in score, the greater the relation loss -- so if the lord
			#was nearly indifferent between two candidates, the difference would be
			#lesser.
			(try_begin),
				(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
				(try_begin),
					#Optional change: Non-jerkish lords will not object to giving a village to
					#someone fiefless, unless they dislike him.
					(neg|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_debauched),
					(neg|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_selfrighteous),
					(neg|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_quarrelsome),
					(lt, ":relation_with_liege_change", 0),
					(is_between, ":center_no", villages_begin, villages_end),
					(troop_slot_eq, ":lord_troop_id", slot_troop_temp_slot, 0),
					(ge, ":relation_with_troop", 0),
					(val_max, ":relation_with_liege_change", 0),
				(try_end),
				(try_begin),
					#Optional change: because taking a penalty for 'thrashing' the same fief
					#back and forth is silly, if you're giving the fief back to the lord who
					#last had it, reduce any penalty.
					(lt, ":relation_with_liege_change", 0),
					(party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":lord_troop_id"),
					(neq, ":lord_troop_id", 0),
					(val_add, ":relation_with_liege_change", 1),

					#If the other lord doesn't have any claim of his own on the center,
					#attenuate the penalty more.
					(lt, ":relation_with_liege_change", 0),
					(ge, ":relation_with_troop", 0),
					(neg|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":other_lord"),
					(neg|troop_slot_eq, ":other_lord", slot_troop_home, ":center_no"),
					(this_or_next|neg|troop_slot_ge, ":other_lord", slot_troop_stance_on_faction_issue, 0),
						(neg|party_slot_eq, ":center_no", slot_center_last_taken_by_troop, ":other_lord"),
					(val_add, ":relation_with_liege_change", 1),
				(else_try),
					#Similar logic, but for "original lord" instead of most recent lord
					(lt, ":relation_with_liege_change", 0),
					(neg|party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":lord_troop_id"),#don't apply this if the above "ex-center" check was applied
					(this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":lord_troop_id"),
						(troop_slot_eq, ":lord_troop_id", slot_troop_home, ":center_no"),

					#Only attenuate the panelty if the other lord doesn't have any claim of his own on the center
					(ge, ":relation_with_troop", 0),
					(neg|troop_slot_eq, ":other_lord", slot_troop_home, ":center_no"),
					(neg|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":other_lord"),
					(neg|party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":other_lord"),
					(this_or_next|neg|troop_slot_ge, ":other_lord", slot_troop_stance_on_faction_issue, 0),
						(neg|party_slot_eq, ":center_no", slot_center_last_taken_by_troop, ":other_lord"),

					(val_add, ":relation_with_liege_change", 1),
				(try_end),
				(try_begin),
					#On the minus side, lords whose homes and/or original fiefs are not
					#disposed according to their wishes are that much more cross.
					(lt, ":relation_with_liege_change", 1),
					(this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":other_lord"),
					(this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":other_lord"),
					   (troop_slot_eq, ":other_lord", slot_troop_home, ":center_no"),
					(val_sub, ":relation_with_liege_change", 1),
				(else_try),
					#Optional change: martial lords are less displeased by awarding a fief to
					#the one who conquered it.
					(lt, ":relation_with_liege_change", 0),
					(party_slot_eq, ":center_no", slot_center_last_taken_by_troop, ":lord_troop_id"),
					(this_or_next|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_upstanding),
					(troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_martial),
					(val_add, ":relation_with_liege_change", 1),
				(try_end),
			(try_end),
			##diplomacy end+
            
            (neq, ":relation_with_liege_change", 0),
            #removed Nov 2010
            #		  	(val_mul, ":relation_reduction", ":faction_size_multiplier"),
            #		  	(val_div, ":relation_reduction", 2),
            #removed Nov 2010
            ## End 1.134
            
            (try_begin),
              (troop_slot_eq, ":other_lord", slot_troop_stance_on_faction_issue, ":lord_troop_id"),
              (val_add, ":relation_with_liege_change", 1), ##1.134
              (val_max, ":relation_with_liege_change", 1), ##1.134
            (try_end),
            
            (call_script, "script_troop_change_relation_with_troop", ":other_lord", ":faction_leader", ":relation_with_liege_change"), ## 1.134
            (val_add, "$total_promotion_changes", ":relation_with_liege_change"), ##1.134
            
            (try_begin),
              (this_or_next|le, ":relation_with_liege_change", -4), #Nov 2010 - changed from -8 ##1.134
              (this_or_next|troop_slot_eq, ":other_lord", slot_troop_promised_fief, 1), #1 is any fief
              (troop_slot_eq, ":other_lord", slot_troop_promised_fief, ":center_no"),
              (call_script, "script_add_log_entry", logent_troop_feels_cheated_by_troop_over_land, ":other_lord", ":center_no", ":lord_troop_id", ":lord_troop_faction"),
            (try_end),
            
          (try_end),
        (try_end),
        
		##diplomacy start+ invalidate cached center points
		(try_begin),
			(neq, ":old_lord_troop_id", ":lord_troop_id"),
			(try_begin),
				(gt, ":old_lord_troop_id", -1),
				(troop_set_slot, ":old_lord_troop_id", dplmc_slot_troop_center_points_plus_one, 0),
			(try_end),
			(try_begin),
				(gt, ":lord_troop_id", -1),
				(troop_set_slot, ":lord_troop_id", dplmc_slot_troop_center_points_plus_one, 0),
			(try_end),
		(try_end),
		##diplomacy end+
		
        #Villages from another faction will also be transferred along with a fortress
        (try_begin),
          (is_between, ":center_no", walled_centers_begin, walled_centers_end),
          (try_for_range, ":cur_village", villages_begin, villages_end),
            (party_slot_eq, ":cur_village", slot_village_bound_center, ":center_no"),
            (store_faction_of_party, ":cur_village_faction", ":cur_village"),
            (neq, ":cur_village_faction", ":lord_troop_faction"),
            
            (call_script, "script_give_center_to_lord", ":cur_village", ":lord_troop_id", 0),
          (try_end),
        (try_end),
        #LAZERAS MODIFIED  {ENTK}
        # Jrider + TITLES v0.3.3 update title, fixed opcode error for spouse when you don't assign the center
        (call_script, "script_troop_set_title_according_to_faction", ":lord_troop_id", ":lord_troop_faction"),
        # Update his wife/husband too if  the lord has one
        (try_begin),
          (ge, ":lord_troop_id", 0), # v0.3.3 fix
          (troop_slot_ge, ":lord_troop_id", slot_troop_spouse, 0),
          (troop_get_slot, ":lord_spouse_troop_id", ":lord_troop_id", slot_troop_spouse),
          (call_script, "script_troop_set_title_according_to_faction", ":lord_spouse_troop_id", ":lord_troop_faction"),
        (try_end),
        # Jrider -
        #LAZERAS MODIFIED  {ENTK}
    ]),

    ("start_give_center_to_lord",
      [
        (store_script_param, ":center_no", 1),
        (store_script_param, ":lord_troop_id", 2), #-1 only in the case of a player deferring ownership of a center
        (store_script_param, ":add_garrison", 3),
        ##diplomacy begin
        (party_set_slot, ":center_no", dplmc_slot_center_taxation, 0),
        (try_begin),
			##Floris MTT begin
			(troop_get_slot,":woman_peasant","$troop_trees",slot_woman_peasant),
			(party_slot_eq, ":center_no", slot_village_infested_by_bandits, ":woman_peasant"),
			##Floris MTT end
          (party_set_slot, ":center_no", slot_village_infested_by_bandits, 0),
        (try_end),
        ##diplomacy end
        
        (try_begin),
          (eq, "$cheat_mode", 1),
          (ge, ":lord_troop_id", 0),
          (str_store_party_name, s4, ":center_no"),
          (str_store_troop_name, s5, ":lord_troop_id"),
          (display_message, "@{!}DEBUG -- {s4} awarded to {s5}"),
        (try_end),
        
        (try_begin),
          (eq, ":lord_troop_id", "trp_player"),
          (unlock_achievement, ACHIEVEMENT_ROYALITY_PAYMENT),
          
          (assign, ":number_of_fiefs_player_have", 1),
          (try_for_range, ":cur_center", centers_begin, centers_end),
            (neq, ":cur_center", ":center_no"),
            (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
            (val_add, ":number_of_fiefs_player_have", 1),
          (try_end),
          
          (ge, ":number_of_fiefs_player_have", 5),
          (unlock_achievement, ACHIEVEMENT_MEDIEVAL_EMLAK),
        (try_end),
        
        (party_get_slot, ":old_lord_troop_id", ":center_no", slot_town_lord),
        
		  (try_begin), #This script is ONLY called with lord_troop_id = -1 when it is the player faction
		  ##diplomacy start+
		  #The player can now also be co-ruler of a NPC kingdom.
			 (eq, ":lord_troop_id", -1),
			 
			 (is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
			 (faction_get_slot, ":players_kingdom_liege", "$players_kingdom", slot_faction_leader),
			 (gt, ":players_kingdom_liege", -1),
			 (this_or_next|eq, ":players_kingdom_liege", "trp_player"),
			 (this_or_next|troop_slot_eq, ":players_kingdom_liege", slot_troop_spouse, "trp_player"),
				(troop_slot_eq, "trp_player", slot_troop_spouse, ":players_kingdom_liege"),
				
			(assign, ":lord_troop_faction", "$players_kingdom"),
			(party_set_banner_icon, ":center_no", 0),#Removing banner
		  (else_try),
		  ##diplomacy end+
			(eq, ":lord_troop_id", -1),
			(assign, ":lord_troop_faction", "fac_player_supporters_faction"),
			(party_set_banner_icon, ":center_no", 0),#Removing banner
          
        (else_try),
          (eq, ":lord_troop_id", "trp_player"),
          (assign, ":lord_troop_faction", "$players_kingdom"), #was changed on Apr 27 from fac_plyr_sup_fac
          
        (else_try),
          (store_troop_faction, ":lord_troop_faction", ":lord_troop_id"),
        (try_end),
        (faction_get_slot, ":faction_leader", ":lord_troop_faction", slot_faction_leader),
        
        (try_begin),
          (eq, ":faction_leader", ":old_lord_troop_id"),
          (call_script, "script_add_log_entry", logent_liege_grants_fief_to_vassal, ":faction_leader", ":center_no", ":lord_troop_id", ":lord_troop_faction"),
          (troop_set_slot, ":lord_troop_id", slot_troop_promised_fief, 0),
        (try_end),
        
        (try_begin),
          (eq, ":lord_troop_id", -1), #Lord troop ID -1 is only used when a player is deferring assignment of a fief
          (party_set_faction, ":center_no", "$players_kingdom"),
        (else_try),
          (eq, ":lord_troop_id", "trp_player"),
          (gt, "$players_kingdom", 0),
          (party_set_faction, ":center_no", "$players_kingdom"),
        (else_try),
          (eq, ":lord_troop_id", "trp_player"),
          (neg|is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
          (party_set_faction, ":center_no", "fac_player_supporters_faction"),
        (else_try),
          (party_set_faction, ":center_no", ":lord_troop_faction"),
        (try_end),
        (party_set_slot, ":center_no", slot_town_lord, ":lord_troop_id"),
        
        (try_begin),
          (party_slot_eq, ":center_no", slot_party_type, spt_village),
          (party_get_slot, ":farmer_party_no", ":center_no", slot_village_farmer_party),
          (gt, ":farmer_party_no", 0),
          (party_is_active, ":farmer_party_no"),
          (store_faction_of_party, ":center_faction", ":center_no"),
          (party_set_faction, ":farmer_party_no", ":center_faction"),
        (try_end),
        
        (try_begin),
          (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
          (party_slot_eq, ":center_no", slot_party_type, spt_castle),
          (gt, ":lord_troop_id", -1),
          
          #normal_banner_begin
          (troop_get_slot, ":cur_banner", ":lord_troop_id", slot_troop_banner_scene_prop),
          (gt, ":cur_banner", 0),
          (val_sub, ":cur_banner", banner_scene_props_begin),
          (val_add, ":cur_banner", banner_map_icons_begin),
          (party_set_banner_icon, ":center_no", ":cur_banner"),
          # custom_banner_begin
          #        (troop_get_slot, ":flag_icon", ":lord_troop_id", slot_troop_custom_banner_map_flag_type),
          #        (ge, ":flag_icon", 0),
          #        (val_add, ":flag_icon", custom_banner_map_icons_begin),
          #        (party_set_banner_icon, ":center_no", ":flag_icon"),
        (try_end),
        
        #    (try_begin),
        #		(eq, 1, 0),
        #       (eq, ":lord_troop_id", "trp_player"),
        #       (neq, ":old_lord_troop_id", "trp_player"),
        #       (party_get_slot, ":center_relation", ":center_no", slot_center_player_relation),
        #       (is_between, ":center_relation", -4, 5),
        #       (call_script, "script_change_player_relation_with_center", ":center_no", 5),
        #       (gt, ":old_lord_troop_id", 0),
        #       (call_script, "script_change_player_relation_with_troop", ":old_lord_troop_id", -25),
        #   (try_end),
        (try_begin),
          (gt, ":lord_troop_id", -1),
          (call_script, "script_update_troop_notes", ":lord_troop_id"),
        (try_end),
        
        (call_script, "script_update_center_notes", ":center_no"),
        
        (try_begin),
          (gt, ":lord_troop_faction", 0),
          (call_script, "script_update_faction_notes", ":lord_troop_faction"),
        (try_end),
        
        (try_begin),
          (ge, ":old_lord_troop_id", 0),
          (call_script, "script_update_troop_notes", ":old_lord_troop_id"),
          (store_troop_faction, ":old_lord_troop_faction", ":old_lord_troop_id"),
          (call_script, "script_update_faction_notes", ":old_lord_troop_faction"),
        (try_end),
        
        (try_begin),
          (eq, ":add_garrison", 1),
          (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
          (party_slot_eq, ":center_no", slot_party_type, spt_castle),
          (assign, ":garrison_strength", 3),
          (try_begin),
            (party_slot_eq, ":center_no", slot_party_type, spt_town),
            (assign, ":garrison_strength", 9),
          (try_end),
          (try_for_range, ":unused", 0, ":garrison_strength"),
            (call_script, "script_cf_reinforce_party", ":center_no"),
          (try_end),
          ## ADD some XP initially
          (try_for_range, ":unused", 0, 7),
            (store_mul, ":xp_range_min", 150, ":garrison_strength"),
            (store_mul, ":xp_range_max", 200, ":garrison_strength"),
            (store_random_in_range, ":xp", ":xp_range_min", ":xp_range_max"),
            (party_upgrade_with_xp, ":center_no", ":xp", 0),
          (try_end),
        (try_end),
        
        (faction_get_slot, ":faction_leader", ":lord_troop_faction", slot_faction_leader),
        (store_current_hours, ":hours"),
        
        #the next block handles gratitude, objections and jealousies
        (try_begin),
          (gt, ":hours", 0),
          (gt, ":lord_troop_id", 0),
          
          (call_script, "script_troop_change_relation_with_troop", ":lord_troop_id", ":faction_leader", 10),
          (val_add, "$total_promotion_changes", 10),
          
          #smaller factions are more dramatically influenced by internal jealousies
          ## Start 1.134
          #Disabled as of NOV 2010
          #		(try_begin),
          #			(neg|faction_slot_ge, ":lord_troop_faction", slot_faction_number_of_parties, 4),
          #			(assign, ":faction_size_multiplier", 6),
          #		(else_try),
          #			(neg|faction_slot_ge, ":lord_troop_faction", slot_faction_number_of_parties, 8),
          #			(assign, ":faction_size_multiplier", 5),
          #		(else_try),
          #			(neg|faction_slot_ge, ":lord_troop_faction", slot_faction_number_of_parties, 16),
          #			(assign, ":faction_size_multiplier", 4),
          #		(else_try),
          #			(neg|faction_slot_ge, ":lord_troop_faction", slot_faction_number_of_parties, 32),
          #			(assign, ":faction_size_multiplier", 3),
          #		(else_try),
          #			(assign, ":faction_size_multiplier", 2),
          #		(try_end),
          ## End 1.134
          
          #factional politics -- each lord in the faction adjusts his relation according to the relation with the lord receiving the faction
          (try_for_range, ":other_lord", active_npcs_begin, active_npcs_end),
            (troop_slot_eq, ":other_lord", slot_troop_occupation, slto_kingdom_hero),
            (neq, ":other_lord", ":lord_troop_id"),
            
            #		    (store_troop_faction, ":lord_troop_faction", ":lord_troop_id"),
            (store_troop_faction, ":other_troop_faction", ":other_lord"),
            (eq, ":lord_troop_faction", ":other_troop_faction"),
            
            (neq, ":other_lord", ":faction_leader"),
            
            (call_script, "script_troop_get_relation_with_troop", ":other_lord", ":lord_troop_id"),
            ## Begin 1.134
            (assign, ":relation_with_troop", reg0),
            
            #relation reduction = relation/10 minus 2. So,0 = -2, 8 = -1, 16+ = no change or bonus, 24+ gain one point
            (store_div, ":relation_with_liege_change", ":relation_with_troop", 8), #changed from 16
            (val_sub, ":relation_with_liege_change", 2),
            
            (val_clamp, ":relation_with_liege_change", -5, 3),
            
            (try_begin),
              #upstanding and goodnatured lords will not lose relation unless they actively dislike the other lord
				 ##diplomacy start+ add companion/lady personality types
				 (this_or_next|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_benefactor),
				 (this_or_next|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_conventional),
				 (this_or_next|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_moralist),
				 (this_or_next|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_otherworldly),
				 ##diplomacy end+
              (troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_goodnatured),
              (ge, ":relation_with_troop", 0),
              (val_max, ":relation_with_liege_change", 0),
            (else_try),
              #penalty is increased for lords who have the more unpleasant reputation types
              (this_or_next|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_selfrighteous),
              (this_or_next|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_debauched),
              (troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_quarrelsome),
              (lt, ":relation_with_liege_change", 0),
              (val_mul, ":relation_with_liege_change", 3),
              (val_div, ":relation_with_liege_change", 2),
			(try_end),
			##diplomacy start+

			#TODO (idea for "high"): instead of being absolute, the sliding score system should be used.
			#(So you can use a score instead of using relations.)  The greater the
			#difference in score, the greater the relation loss -- so if the lord
			#was nearly indifferent between two candidates, the difference would be
			#lesser.
			(try_begin),
				(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
				(try_begin),
					#Optional change: Non-jerkish lords will not object to giving a village to
					#someone fiefless, unless they dislike him.
					(neg|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_debauched),
					(neg|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_selfrighteous),
					(neg|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_quarrelsome),
					(lt, ":relation_with_liege_change", 0),
					(is_between, ":center_no", villages_begin, villages_end),
					(troop_slot_eq, ":lord_troop_id", slot_troop_temp_slot, 0),
					(ge, ":relation_with_troop", 0),
					(val_max, ":relation_with_liege_change", 0),				
				(try_end),
				(try_begin),
					#Optional change: because taking a penalty for 'thrashing' the same fief
					#back and forth is silly, if you're giving the fief back to the lord who
					#last had it, reduce any penalty.
					(lt, ":relation_with_liege_change", 0),
					(party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":lord_troop_id"),
					(neq, ":lord_troop_id", 0),
					(val_add, ":relation_with_liege_change", 1),
					
					#If the other lord doesn't have any claim of his own on the center,
					#attenuate the penalty more.
					(lt, ":relation_with_liege_change", 0),
					(ge, ":relation_with_troop", 0),
					(neg|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":other_lord"),
					(neg|troop_slot_eq, ":other_lord", slot_troop_home, ":center_no"),
					(this_or_next|neg|troop_slot_ge, ":other_lord", slot_troop_stance_on_faction_issue, 0),
						(neg|party_slot_eq, ":center_no", slot_center_last_taken_by_troop, ":other_lord"),
					(val_add, ":relation_with_liege_change", 1),
				(else_try),
					#Similar logic, but for "original lord" instead of most recent lord
					(lt, ":relation_with_liege_change", 0),
					(neg|party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":lord_troop_id"),#don't apply this if the above "ex-center" check was applied
					(this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":lord_troop_id"),
						(troop_slot_eq, ":lord_troop_id", slot_troop_home, ":center_no"),
					
					#Only attenuate the panelty if the other lord doesn't have any claim of his own on the center
					(ge, ":relation_with_troop", 0),
					(neg|troop_slot_eq, ":other_lord", slot_troop_home, ":center_no"),
					(neg|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":other_lord"),
					(neg|party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":other_lord"),
					(this_or_next|neg|troop_slot_ge, ":other_lord", slot_troop_stance_on_faction_issue, 0),
						(neg|party_slot_eq, ":center_no", slot_center_last_taken_by_troop, ":other_lord"),
					
					(val_add, ":relation_with_liege_change", 1),
				(try_end),
				(try_begin),
					#On the minus side, lords whose homes and/or original fiefs are not
					#disposed according to their wishes are that much more cross.
					(lt, ":relation_with_liege_change", 1),
					(this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, ":other_lord"),
					(this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":other_lord"),
					   (troop_slot_eq, ":other_lord", slot_troop_home, ":center_no"),
					(val_sub, ":relation_with_liege_change", 1),
				(else_try),
					#Optional change: martial lords are less displeased by awarding a fief to
					#the one who conquered it.
					(lt, ":relation_with_liege_change", 0),
					(party_slot_eq, ":center_no", slot_center_last_taken_by_troop, ":lord_troop_id"),
					(this_or_next|troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_upstanding),
					(troop_slot_eq, ":other_lord", slot_lord_reputation_type, lrep_martial),
					(val_add, ":relation_with_liege_change", 1),
				(try_end),
			(try_end),
			##diplomacy end+ 
			
            (neq, ":relation_with_liege_change", 0),
            #removed Nov 2010
            #		  	(val_mul, ":relation_reduction", ":faction_size_multiplier"),
            #		  	(val_div, ":relation_reduction", 2),
            #removed Nov 2010
            ## End 1.134
            
            (try_begin),
              (troop_slot_eq, ":other_lord", slot_troop_stance_on_faction_issue, ":lord_troop_id"),
              (val_add, ":relation_with_liege_change", 1), ##1.134
              (val_max, ":relation_with_liege_change", 1), ##1.134
            (try_end),
            
            (call_script, "script_troop_change_relation_with_troop", ":other_lord", ":faction_leader", ":relation_with_liege_change"), ## 1.134
            (val_add, "$total_promotion_changes", ":relation_with_liege_change"), ##1.134
            
            (try_begin),
              (this_or_next|le, ":relation_with_liege_change", -4), #Nov 2010 - changed from -8 ##1.134
              (this_or_next|troop_slot_eq, ":other_lord", slot_troop_promised_fief, 1), #1 is any fief
              (troop_slot_eq, ":other_lord", slot_troop_promised_fief, ":center_no"),
              (call_script, "script_add_log_entry", logent_troop_feels_cheated_by_troop_over_land, ":other_lord", ":center_no", ":lord_troop_id", ":lord_troop_faction"),
            (try_end),
            
          (try_end),
        (try_end),
        
        #Villages from another faction will also be transferred along with a fortress
        (try_begin),
          (is_between, ":center_no", walled_centers_begin, walled_centers_end),
          (try_for_range, ":cur_village", villages_begin, villages_end),
            (party_slot_eq, ":cur_village", slot_village_bound_center, ":center_no"),
            (store_faction_of_party, ":cur_village_faction", ":cur_village"),
            (neq, ":cur_village_faction", ":lord_troop_faction"),
            
            (call_script, "script_give_center_to_lord", ":cur_village", ":lord_troop_id", 0),
          (try_end),
        (try_end),
        #LAZERAS MODIFIED  {ENTK}
        # Jrider + TITLES v0.3.3 update title, fixed opcode error for spouse when you don't assign the center
        (call_script, "script_troop_set_title_according_to_faction", ":lord_troop_id", ":lord_troop_faction"),
        # Update his wife/husband too if  the lord has one
        (try_begin),
          (ge, ":lord_troop_id", 0), # v0.3.3 fix
          (troop_slot_ge, ":lord_troop_id", slot_troop_spouse, 0),
          (troop_get_slot, ":lord_spouse_troop_id", ":lord_troop_id", slot_troop_spouse),
          (call_script, "script_troop_set_title_according_to_faction", ":lord_spouse_troop_id", ":lord_troop_faction"),
        (try_end),
        # Jrider -
        #LAZERAS MODIFIED  {ENTK}
    ]),
    
    ##  # script_give_town_to_besiegers
    ##  # Input: arg1 = center_no, arg2 = besieger_party
    ##  ("give_town_to_besiegers",
    ##    [
    ##      (store_script_param_1, ":center_no"),
    ##      (store_script_param_2, ":besieger_party"),
    ##      (store_faction_of_party, ":besieger_faction", ":besieger_party"),
    ##
    ##      (try_begin),
    ##        (call_script, "script_cf_get_party_leader", ":besieger_party"),
    ##        (assign, ":new_leader", reg0),
    ##      (else_try),
    ##        (call_script, "script_select_kingdom_hero_for_new_center", ":besieger_faction"),
    ##        (assign, ":new_leader", reg0),
    ##      (try_end),
    ##
    ##      (call_script, "script_give_center_to_lord", ":center_no", ":new_leader"),
    ##
    ##      (try_for_parties, ":party_no"),
    ##        (get_party_ai_object, ":object", ":party_no"),
    ##        (get_party_ai_behavior, ":behavior", ":party_no"),
    ##        (eq, ":object", ":center_no"),
    ##        (this_or_next|eq, ":behavior", ai_bhvr_travel_to_party),
    ##        (eq, ":behavior", ai_bhvr_attack_party),
    ##        (party_set_ai_behavior, ":party_no", ai_bhvr_hold),
    ##        (party_set_slot, ":party_no", slot_party_ai_state, spai_undefined),
    ##        (party_set_flags, ":party_no", pf_default_behavior, 0),
    ##      (try_end),
    ##
    ##      #Staying at the center for a while
    ##      (party_set_ai_behavior, ":besieger_party", ai_bhvr_hold),
    ##      (party_set_slot, ":besieger_party", slot_party_ai_state, spai_undefined),
    ##      (party_set_flags, ":besieger_party", pf_default_behavior, 0),
    ##
    ##      (faction_get_slot, ":reinforcement_a", ":besieger_faction", slot_faction_reinforcements_a),
    ##      (faction_get_slot, ":reinforcement_b", ":besieger_faction", slot_faction_reinforcements_b),
    ##      (party_add_template, ":center_no", ":reinforcement_a"),
    ##      (party_add_template, ":center_no", ":reinforcement_b"),
    ##  ]),
    ##
    
    # script_get_number_of_hero_centers
    # Input: arg1 = troop_no
    # Output: reg0 = number of centers that are ruled by the hero
    ("get_number_of_hero_centers",
      [
        (store_script_param_1, ":troop_no"),
        (assign, ":result", 0),
        (try_for_range, ":center_no", centers_begin, centers_end),
          (party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
          (val_add, ":result", 1),
        (try_end),
        (assign, reg0, ":result"),
    ]),
    
    
    ##  # script_cf_get_new_center_leader_chance_for_troop
    ##  # Input: arg1 = troop_no
    ##  # Output: reg0 = chance of the troop to rule a new center
    ##  ("cf_get_new_center_leader_chance_for_troop",
    ##    [
    ##      (store_script_param_1, ":troop_no"),
    ##      (troop_get_slot, ":troop_rank", ":troop_no", slot_troop_kingdom_rank),
    ##      (try_begin),
    ##        (eq, ":troop_rank", 4),
    ##        (assign, ":troop_chance", 1000),
    ##      (else_try),
    ##        (eq, ":troop_rank", 3),
    ##        (assign, ":troop_chance", 800),
    ##      (else_try),
    ##        (eq, ":troop_rank", 2),
    ##        (assign, ":troop_chance", 400),
    ##      (else_try),
    ##        (eq, ":troop_rank", 1),
    ##        (assign, ":troop_chance", 100),
    ##      (else_try),
    ##        (assign, ":troop_chance", 10),
    ##      (try_end),
    ##
    ##      (call_script, "script_get_number_of_hero_centers", ":troop_no"),
    ##      (assign, ":number_of_hero_centers", reg0),
    ##      (try_begin),
    ##        (gt, ":number_of_hero_centers", 0),
    ##        (val_mul, ":number_of_hero_centers", 2),
    ##        (val_mul, ":number_of_hero_centers", ":number_of_hero_centers"),
    ##        (val_div, ":troop_chance", ":number_of_hero_centers"),
    ##      (try_end),
    ##      (assign, reg0, ":troop_chance"),
    ##      (eq, reg0, 0),
    ##      (assign, reg0, 1),
    ##  ]),
    
    
    ##  # script_select_kingdom_hero_for_new_center
    ##  # Input: arg1 = faction_no
    ##  # Output: reg0 = troop_no as the new leader
    ##  ("select_kingdom_hero_for_new_center",
    ##    [
    ##      (store_script_param_1, ":kingdom"),
    ##
    ##      (assign, ":min_num_centers", -1),
    ##      (assign, ":min_num_centers_troop", -1),
    ##
    ##      (try_for_range, ":troop_no", kingdom_heroes_begin, kingdom_heroes_end),
    ##        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
    ##        (store_troop_faction, ":troop_faction", ":troop_no"),
    ##        (eq, ":troop_faction", ":kingdom"),
    ##        (call_script, "script_get_number_of_hero_centers", ":troop_no"),
    ##        (assign, ":num_centers", reg0),
    ##        (try_begin),
    ##          (lt, ":num_centers", ":min_num_centers"),
    ##          (assign, ":min_num_centers", ":num_centers"),
    ##          (assign, ":min_num_centers_troop", ":troop_no"),
    ##        (try_end),
    ##      (try_end),
    ##      (assign, reg0, ":min_num_centers_troop"),
    ##  ]),
    
    
    # script_cf_get_random_enemy_center
    # Input: arg1 = party_no
    # Output: reg0 = center_no
    ("cf_get_random_enemy_center",
      [
        (store_script_param_1, ":party_no"),
        
        (assign, ":result", -1),
        (assign, ":total_enemy_centers", 0),
        (store_faction_of_party, ":party_faction", ":party_no"),
        
        (try_for_range, ":center_no", centers_begin, centers_end),
          (store_faction_of_party, ":center_faction", ":center_no"),
          (store_relation, ":party_relation", ":center_faction", ":party_faction"),
          (lt, ":party_relation", 0),
          (val_add, ":total_enemy_centers", 1),
        (try_end),
        
        (gt, ":total_enemy_centers", 0),
        (store_random_in_range, ":random_center", 0, ":total_enemy_centers"),
        (assign, ":total_enemy_centers", 0),
        (try_for_range, ":center_no", centers_begin, centers_end),
          (eq, ":result", -1),
          (store_faction_of_party, ":center_faction", ":center_no"),
          (store_relation, ":party_relation", ":center_faction", ":party_faction"),
          (lt, ":party_relation", 0),
          (val_sub, ":random_center", 1),
          (lt, ":random_center", 0),
          (assign, ":result", ":center_no"),
        (try_end),
        (assign, reg0, ":result"),
    ]),
    
    
    ##  # script_get_random_enemy_town
    ##  # Input: arg1 = party_no
    ##  # Output: reg0 = center_no
    ##  ("get_random_enemy_town",
    ##    [
    ##      (store_script_param_1, ":party_no"),
    ##
    ##      (assign, ":result", -1),
    ##      (assign, ":total_enemy_centers", 0),
    ##      (store_faction_of_party, ":party_faction", ":party_no"),
    ##
    ##      (try_for_range, ":center_no", towns_begin, towns_end),
    ##        (store_faction_of_party, ":center_faction", ":center_no"),
    ##        (neq, ":center_faction", ":party_faction"),
    ##        (val_add, ":total_enemy_centers", 1),
    ##      (try_end),
    ##
    ##      (try_begin),
    ##        (eq, ":total_enemy_centers", 0),
    ##      (else_try),
    ##        (store_random_in_range, ":random_center", 0, ":total_enemy_centers"),
    ##        (assign, ":total_enemy_centers", 0),
    ##        (try_for_range, ":center_no", towns_begin, towns_end),
    ##          (eq, ":result", -1),
    ##          (store_faction_of_party, ":center_faction", ":center_no"),
    ##          (neq, ":center_faction", ":party_faction"),
    ##          (store_relation, ":party_relation", ":center_faction", ":party_faction"),
    ##          (le, ":party_relation", -10),
    ##          (val_add, ":total_enemy_centers", 1),
    ##          (lt, ":random_center", ":total_enemy_centers"),
    ##          (assign, ":result", ":center_no"),
    ##        (try_end),
    ##      (try_end),
    ##      (assign, reg0, ":result"),
    ##  ]),
    
    
    
    # script_find_travel_location
    # Input: arg1 = center_no
    # Output: reg0 = new_center_no (to travel within the same faction)
    ("find_travel_location",
      [
        (store_script_param_1, ":center_no"),
        (store_faction_of_party, ":faction_no", ":center_no"),
        (assign, ":total_weight", 0),
        (try_for_range, ":cur_center_no", centers_begin, centers_end),
          (neq, ":center_no", ":cur_center_no"),
          (store_faction_of_party, ":center_faction_no", ":cur_center_no"),
          (eq, ":faction_no", ":center_faction_no"),
          
          (store_distance_to_party_from_party, ":cur_distance", ":center_no", ":cur_center_no"),
          (val_add, ":cur_distance", 1),
          
          (assign, ":new_weight", 100000),
          (val_div, ":new_weight", ":cur_distance"),
          (val_add, ":total_weight", ":new_weight"),
        (try_end),
        
        (assign, reg0, -1),
        
        (try_begin),
          (eq, ":total_weight", 0),
        (else_try),
          (store_random_in_range, ":random_weight", 0 , ":total_weight"),
          (assign, ":total_weight", 0),
          (assign, ":done", 0),
          (try_for_range, ":cur_center_no", centers_begin, centers_end),
            (eq, ":done", 0),
            (neq, ":center_no", ":cur_center_no"),
            (store_faction_of_party, ":center_faction_no", ":cur_center_no"),
            (eq, ":faction_no", ":center_faction_no"),
            
            (store_distance_to_party_from_party, ":cur_distance", ":center_no", ":cur_center_no"),
            (val_add, ":cur_distance", 1),
            
            (assign, ":new_weight", 100000),
            (val_div, ":new_weight", ":cur_distance"),
            (val_add, ":total_weight", ":new_weight"),
            (lt, ":random_weight", ":total_weight"),
            (assign, reg0, ":cur_center_no"),
            (assign, ":done", 1),
          (try_end),
        (try_end),
    ]),
    
    
    # script_get_relation_between_parties
    # Input: arg1 = party_no_1, arg2 = party_no_2
    # Output: reg0 = relation between parties
    ("get_relation_between_parties",
      [
        (store_script_param_1, ":party_no_1"),
        (store_script_param_2, ":party_no_2"),
        
        (store_faction_of_party, ":party_no_1_faction", ":party_no_1"),
        (store_faction_of_party, ":party_no_2_faction", ":party_no_2"),
        (try_begin),
          (eq, ":party_no_1_faction", ":party_no_2_faction"),
          (assign, reg0, 100),
        (else_try),
          (store_relation, ":relation", ":party_no_1_faction", ":party_no_2_faction"),
          (assign, reg0, ":relation"),
        (try_end),
    ]),
    # script_calculate_weekly_party_wage
    # Input: arg1 = party_no
    # Output: reg0 = weekly wage
    ("calculate_weekly_party_wage",
      [
        (store_script_param_1, ":party_no"),
        
        (assign, ":result", 0),
        (party_get_num_companion_stacks, ":num_stacks",":party_no"),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
          (party_stack_get_troop_id, ":stack_troop",":party_no",":i_stack"),
          (party_stack_get_size, ":stack_size",":party_no",":i_stack"),
          (call_script, "script_npc_get_troop_wage", ":stack_troop", ":party_no"),
          (assign, ":cur_wage", reg0),
          (val_mul, ":cur_wage", ":stack_size"),
          (val_add, ":result", ":cur_wage"),
        (try_end),
        (assign, reg0, ":result"),
    ]),
    
    # script_calculate_player_faction_wage
    # Input: arg1 = party_no
    # Output: reg0 = weekly wage
    ("calculate_player_faction_wage",
      [(assign, ":nongarrison_wages", 0),
        (assign, ":garrison_wages", 0),
        (try_for_parties, ":party_no"),
          (assign, ":garrison_troop", 0),
          (try_begin),
            (this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_town),
            (party_slot_eq, ":party_no", slot_party_type, spt_castle),
            (party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
            (assign, ":garrison_troop", 1),
          (try_end),
          (this_or_next|eq, ":party_no", "p_main_party"),
          (eq, ":garrison_troop", 1),
          (party_get_num_companion_stacks, ":num_stacks",":party_no"),
          (try_for_range, ":i_stack", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop",":party_no",":i_stack"),
            (party_stack_get_size, ":stack_size",":party_no",":i_stack"),
            (call_script, "script_game_get_troop_wage", ":stack_troop", ":party_no"),
            (assign, ":cur_wage", reg0),
            (val_mul, ":cur_wage", ":stack_size"),
            (try_begin),
              (eq, ":garrison_troop", 1),
              (val_add, ":garrison_wages", ":cur_wage"),
            (else_try),
              (val_add, ":nongarrison_wages", ":cur_wage"),
            (try_end),
          (try_end),
        (try_end),
		 (val_div, ":garrison_wages", 2),#Half payment for garrisons
		 (store_sub, ":total_payment", 14, "$g_cur_week_half_daily_wage_payments"), #between 0 and 7
		 (val_mul, ":nongarrison_wages", ":total_payment"),
		 (val_div, ":nongarrison_wages", 14),
		 ##diplomacy start+ centralization affects this in the player's kingdom
	###xxx TODO: This appears to be missing.     
		 ##diplomacy end+
		 (store_add, reg0, ":nongarrison_wages", ":garrison_wages"),
    ]),
    
    # script_calculate_hero_weekly_net_income_and_add_to_wealth
    # Input: arg1 = troop_no
    # Output: none
    ("calculate_hero_weekly_net_income_and_add_to_wealth",
      [
        (store_script_param_1, ":troop_no"),
        
        (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
        (troop_get_slot, ":cur_wealth", ":troop_no", slot_troop_wealth),
        
        (assign, ":weekly_income", 750), #let every hero receive 750 denars by default
        
        (store_character_level, ":troop_level", ":troop_no"),
        (store_mul, ":level_income", ":troop_level", 10),
        (val_add, ":weekly_income", ":level_income"),
        
        (store_troop_faction,":faction_no", ":troop_no"),
	  ##diplomacy start+
	  #Bonus for marshall and/or faction leader (is 1000 in native)
	  (assign, ":leader_bonus_gold", 1000),
	  (assign, ":bonus_applied", 0),
	  (try_begin),
		   #OPTIONAL CHANGE (HIGH)
		   (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),
 		   #Scale marshall and king bonus gold by number of remaining kingdoms,
           #so the total amount paid out remains the same even as kingdoms disappear.
           #This is only enabled if changes are on "HIGH".
           (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
           (store_sub, ":original_kingdoms", npc_kingdoms_end, npc_kingdoms_begin),#deliberately excludes player kingdom
           (ge, ":original_kingdoms", 2),
           (assign, ":current_kingdoms", 0),
           (try_for_range, ":other_fac", kingdoms_begin, kingdoms_end),#deliberately include player kingdom
             (faction_slot_eq, ":other_fac", slot_faction_state, sfs_active),
             (val_add, ":current_kingdoms", 1),
           (try_end),
           (ge, ":current_kingdoms", 1),
           (lt, ":current_kingdoms", ":original_kingdoms"),
           (val_mul, ":leader_bonus_gold", ":original_kingdoms"),
           (val_div, ":leader_bonus_gold", ":current_kingdoms"),
		   #Examples, assuming 6 starting kingdoms and no player kingdom:
		   #6 kingdoms: 1000 each, 1000 * 6 = 6000 total
		   #5 kingdoms: 1200 each, 1200 * 5 = 6000 total
		   #4 kingdoms: 1500 each, 1500 * 4 = 6000 total
		   #3 kingdoms: 2000 each, 2000 * 3 = 6000 total
		   #2 kingdoms: 3000 each, 3000 * 2 = 6000 total
		   #1 kingdom:  6000 each, 6000 * 1 = 6000 total
      (try_end),
	  ##diplomacy end+

      (try_begin), #check if troop is kingdom leader
        (faction_slot_eq, ":faction_no", slot_faction_leader, ":troop_no"),
        ##diplomacy start+
		#OLD BEHAVIOR:
        #(val_add, ":weekly_income", 1000),
		#NEW BEHAVIOR:
		(val_add, ":weekly_income", ":leader_bonus_gold"),
		(val_add, ":bonus_applied", 1),
        ##diplomacy end+
      (try_end),

      (try_begin), #check if troop is marshall
        (faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
        ##diplomacy start+
		#OLD BEHAVIOR:
        #(val_add, ":weekly_income", 1000),
		#NEW BEHAVIOR:
	    (val_add, ":weekly_income", ":leader_bonus_gold"),
		(val_add, ":bonus_applied", 1),
        ##diplomacy end+
      (try_end),
	  
	  ##diplomacy start+
	  (try_begin),
	  	  #OPTIONAL CHANGE (MEDIUM)
		  (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
		  #If the lord is the spouse of the faction leader and no better bonus
		  #applied, the lord gets half of the bonus if either (1) there is no
		  #marshall, or (2) the faction leader is the player.
		  (eq, ":bonus_applied", 0),
		  (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
  		  #Don't do the usual polygamy check: the bonus only applies to
		  #one of the spouses.
		  (faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
		  (ge, ":faction_leader", 0),
		  (troop_slot_eq, ":faction_leader", slot_troop_spouse, ":troop_no"),
		  #Don't apply the bonus unless the faction leader bonus is going
		  #all/partially uncollected, or the marshal bonus is going uncollected.
		  (this_or_next|neg|faction_slot_ge, ":faction_no", slot_faction_marshall, 0),
			(eq, ":faction_leader", "trp_player"),
		  #Apply bonus
		  (val_add, ":bonus_applied", 1),
		  (store_div, reg0, ":leader_bonus_gold", 2),
		  (val_add, ":weekly_income", reg0),
	  (try_end),
	  ##diplomacy end+

      (assign, ":cur_weekly_wage", 0),
      (try_begin),
        (gt, ":party_no",0),
        (call_script, "script_calculate_weekly_party_wage", ":party_no"),
        (assign, ":cur_weekly_wage", reg0),
      (try_end),
      ##diplomacy start+
      (try_begin),
	     #take into account leader's leadership skill, like in CC
	     #economics changes must be enabled
         (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),
         (store_skill_level, ":leadership_level", "skl_leadership", ":troop_no"),
         (val_clamp, ":leadership_level", 0, 11),
         (store_mul, ":leadership_bonus", 5, ":leadership_level"),
         (store_sub, ":leadership_factor", 100, ":leadership_bonus"),
         (val_mul, ":cur_weekly_wage", ":leadership_factor"),  #wage = wage * (100 - 5*leadership)/100
         (val_div, ":cur_weekly_wage", 100),
      (try_end),
	  
	  #Store the change in income for use below
	  (store_sub, ":net_income", ":weekly_income", ":cur_weekly_wage"),
      ##diplomacy end+
      (val_sub, ":weekly_income", ":cur_weekly_wage"),

      (val_add, ":cur_wealth", ":weekly_income"),

	  (try_begin),
		(lt, ":cur_wealth", 0),
		(store_sub, ":percent_under", 0, ":cur_wealth"),
		(val_mul, ":percent_under", 100),
		(val_div, ":percent_under", ":cur_weekly_wage"),
		(val_div, ":percent_under", 5), #Max 20 percent
		##diplomacy start+
		#The above assumption could be violated if the lord entered this
		#script with a negative wealth.  Add a failsafe.
		(val_clamp, ":percent_under", 0, 21),
		##diplomacy end+
		(call_script, "script_party_inflict_attrition", ":party_no", ":percent_under", 1),
	  (try_end),

	  ##diplomacy start+
	  #Apply gold change
	  (try_begin),
	     #If the wealth change was positive, some of it may go to the lord's holdings.
	     (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),
	     (ge, ":net_income", 1),
		 (call_script, "script_dplmc_distribute_gold_to_lord_and_holdings", ":net_income", ":troop_no"),
	  (else_try),
	     #Fall through to old version:
		 #OLD VERSION:
         (val_max, ":cur_wealth", 0),
         (troop_set_slot, ":troop_no", slot_troop_wealth, ":cur_wealth"),
	  (try_end),
	  ##diplomacy end+
  ]),
    
    # script_cf_reinforce_party
    # Input: arg1 = party_no,
    # Output: none
    # Adds reinforcement to party according to its type and faction
    # Called from several places, simple_triggers for centers, script_hire_men_to_kingdom_hero_party for hero parties
    ("cf_reinforce_party",
      [
        (store_script_param_1, ":party_no"),
        
        (store_faction_of_party, ":party_faction", ":party_no"),
		  ##diplomacy start+ The party faction may be changed for culture, but we still need the original
		  (assign, ":real_party_faction", ":party_faction"),
		  ##diplomacy end+
		  (party_get_slot, ":party_type",":party_no", slot_party_type),

	#Rebellion changes begin:
		(try_begin),
			(eq, ":party_type", spt_kingdom_hero_party),
			(party_stack_get_troop_id, ":leader", ":party_no"),
			(troop_get_slot, ":party_faction",  ":leader", slot_troop_original_faction),
			##diplomacy start+ Use player culture for companions and spouse (and any hypothetical non-hero mercenaries)
			(eq, ":real_party_faction", "fac_player_supporters_faction"),
			(is_between, "$g_player_culture", npc_kingdoms_begin, npc_kingdoms_end),
			(this_or_next|is_between, ":leader", companions_begin, companions_end),
			(this_or_next|troop_slot_eq, "trp_player", slot_troop_spouse, ":leader"),
			(neg|is_between, ":leader", heroes_begin, heroes_end),
			(assign, ":party_faction", "$g_player_culture"),
			##diplomacy end+
		(try_end),
	#Rebellion changes end
        
		(try_begin),
			(eq, ":party_faction", "fac_player_supporters_faction"),
			(party_get_slot, ":town_lord", ":party_no", slot_town_lord),
			(try_begin),
	##diplomacy begin
			  (is_between, "$g_player_culture", kingdoms_begin, kingdoms_end), #Player Faction
			  (assign, ":party_faction", "$g_player_culture"),
	
			  (try_begin), #debug
				(eq, "$cheat_mode", 1),
				(str_store_party_name, s11, ":party_no"),
				(display_message, "@pt in {s11}"),
			  (try_end),
	
	#Player Faction
			(else_try),
	##diplomacy end
			  (gt, ":town_lord", 0),
			  (troop_get_slot, ":party_faction", ":town_lord", slot_troop_original_faction),
			(else_try),
			  (party_get_slot, ":party_faction", ":party_no", slot_center_original_faction),
			(try_end),
		(try_end),
	
	##diplomacy start+ Player culture cleanup (do this once here, instead of separately for each type)
		(try_begin),
			(gt, ":real_party_faction", "fac_commoners"),
			(this_or_next|eq, ":real_party_faction", "fac_player_faction"),
			(this_or_next|eq, ":real_party_faction", "fac_player_supporters_faction"),
			(eq, ":real_party_faction", "$players_kingdom"),
			(neg|is_between, ":party_faction", npc_kingdoms_begin, npc_kingdoms_end),
			(is_between, "$g_player_culture", npc_kingdoms_begin, npc_kingdoms_end),
			(assign, ":party_faction", "$g_player_culture"),
		(try_end),
		  ##diplomacy end+
		  
        (faction_get_slot, ":party_template_a", ":party_faction", slot_faction_reinforcements_a),
        (faction_get_slot, ":party_template_b", ":party_faction", slot_faction_reinforcements_b),
        (faction_get_slot, ":party_template_c", ":party_faction", slot_faction_reinforcements_c),
        (faction_get_slot, ":party_template_d", ":party_faction", slot_faction_reinforcements_d),
        (faction_get_slot, ":party_template_e", ":party_faction", slot_faction_reinforcements_e),
        (faction_get_slot, ":party_template_f", ":party_faction", slot_faction_reinforcements_f),
        
      (assign, ":party_template", 0),
      (store_random_in_range, ":rand", 0, 100),
  	  ##diplomacy start+
	  #Implement "quality vs. quantity" in a way that is visible in player battles
	  #(previously, quantity increased party size, but quality only had an effect
	  #in autocalc battles)
	  (try_begin),
		(is_between, ":real_party_faction", kingdoms_begin, kingdoms_end),
		(faction_get_slot, ":dplmc_quality", ":real_party_faction", dplmc_slot_faction_quality),
		(val_clamp, ":dplmc_quality", -3, 4),
		(val_add, ":rand", ":dplmc_quality"),
		(val_clamp, ":rand", 0, 101),
	  (try_end),
	  ##diplomacy end+
        (try_begin),
          (this_or_next|eq, ":party_type", spt_town),
          (eq, ":party_type", spt_castle),  #CASTLE OR TOWN
          (try_begin),
            (lt, ":rand", 65),
            (assign, ":party_template", ":party_template_a"),
          (else_try),
            (lt, ":rand", 65),
            (assign, ":party_template", ":party_template_c"),
          (else_try),
            (lt, ":rand", 65),
            (assign, ":party_template", ":party_template_d"),
          (else_try),
            (assign, ":party_template", ":party_template_e"),
          (try_end),
        (else_try),
          (eq, ":party_type", spt_kingdom_hero_party),
          (try_begin),
            (lt, ":rand", 50),
            (assign, ":party_template", ":party_template_b"),
          (else_try),
            (lt, ":rand", 75),
            (assign, ":party_template", ":party_template_c"),
          (else_try),
            (lt, ":rand", 75),
            (assign, ":party_template", ":party_template_d"),
          (else_try),
            (lt, ":rand", 75),
            (assign, ":party_template", ":party_template_e"),
          (else_try),
            (assign, ":party_template", ":party_template_f"),
          (try_end),
        (else_try),
			##diplomacy start+ Reinforcements for patrols
			(eq, ":party_type", spt_patrol),
			(try_begin),
				(lt, ":rand", 65),
				(assign, ":party_template", ":party_template_a"),
			(else_try),
				(lt, ":rand", 65),
				(assign, ":party_template", ":party_template_c"),
			(else_try),
				(lt, ":rand", 65),
				(assign, ":party_template", ":party_template_d"),
			(else_try),
			   (assign, ":party_template", ":party_template_e"),
			(try_end),
		  ##diplomacy end+
        (try_end),
        
        (try_begin),
          (gt, ":party_template", 0),
          (party_add_template, ":party_no", ":party_template"),
        (try_end),
  ]),
    
    # script_hire_men_to_kingdom_hero_party
    # Input: arg1 = troop_no (hero of the party)
    # Output: none
    ("hire_men_to_kingdom_hero_party",
      [
        (store_script_param_1, ":troop_no"),
        
        (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
        (troop_get_slot, ":cur_wealth", ":troop_no", slot_troop_wealth),
        
        #while hiring reinforcements party leaders can only use 3/4 of their budget. This value is holding in ":hiring budget".
        (assign, ":hiring_budget", ":cur_wealth"),
        (val_mul, ":hiring_budget", 3),
        (val_div, ":hiring_budget", 4),
        
        (call_script, "script_party_get_ideal_size", ":party_no"),
        (assign, ":ideal_size", reg0),
        (store_mul, ":ideal_top_size", ":ideal_size", 3),
        (val_div, ":ideal_top_size", 2),
        
        #(try_begin),
        #	(ge, "$cheat_mode", 1),
        #  (str_store_troop_name, s7, ":troop_no"),
        #  (assign, reg9, ":cur_wealth"),
        #  (display_message, "@{!}DEBUGS : {s7} total budget is {reg9}"),
        #  (assign, reg6, ":ideal_size"),
        #  (assign, reg7, ":ideal_top_size"),
        #  (assign, reg8, ":hiring_budget"),
        #  (display_message, "str_debug__hiring_men_to_s7_ideal_size__reg6_ideal_top_size__reg7_hiring_budget__reg8"),
        #(try_end),
        
        (party_get_num_companions, ":party_size", ":party_no"),
        
        (store_faction_of_party, ":party_faction", ":party_no"),
        (try_begin),
          (this_or_next|eq, ":party_faction", "fac_player_supporters_faction"),
          (eq, ":party_faction", "$players_kingdom"),
          (assign, ":reinforcement_cost", reinforcement_cost_moderate),
        (else_try),
          (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
          (assign, ":reinforcement_cost", reinforcement_cost_moderate),
          (try_begin),
            (eq, ":reduce_campaign_ai", 0), #hard
            (assign, ":reinforcement_cost", reinforcement_cost_hard),
          (else_try),
            (eq, ":reduce_campaign_ai", 1), #moderate
            (assign, ":reinforcement_cost", reinforcement_cost_moderate),
          (else_try),
            (eq, ":reduce_campaign_ai", 2), #easy
            (assign, ":reinforcement_cost", reinforcement_cost_easy),
          (try_end),
        (try_end),
        
        (assign, ":num_rounds", 1),
        (try_for_range, ":unused", 0 , ":num_rounds"),
          (try_begin),
            (lt, ":party_size", ":ideal_size"),
            (gt, ":hiring_budget", ":reinforcement_cost"),
            (gt, ":party_no", 0),
            (call_script, "script_cf_reinforce_party", ":party_no"),
            (val_sub, ":cur_wealth", ":reinforcement_cost"),
            (troop_set_slot, ":troop_no", slot_troop_wealth, ":cur_wealth"),
          (else_try),
            (gt, ":party_size", ":ideal_top_size"),
            (store_troop_faction, ":troop_faction", ":troop_no"),
            (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
            (assign, ":total_regulars", 0),
            (assign, ":total_regular_levels", 0),
            (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
              (party_stack_get_troop_id, ":stack_troop", ":party_no", ":i_stack"),
              (neg|troop_is_hero, ":stack_troop"),
              (party_stack_get_size, ":stack_size", ":party_no", ":i_stack"),
              (store_character_level, ":stack_level", ":stack_troop"),
              (store_troop_faction, ":stack_faction", ":stack_troop"),
              (try_begin),
                (eq, ":troop_faction", ":stack_faction"),
                (val_mul, ":stack_level", 3), #reducing the chance of the faction troops' removal
              (try_end),
              (val_mul, ":stack_level", ":stack_size"),
              (val_add, ":total_regulars", ":stack_size"),
              (val_add, ":total_regular_levels", ":stack_level"),
            (try_end),
            (gt, ":total_regulars", 0),
            (store_div, ":average_level", ":total_regular_levels", ":total_regulars"),
            (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
              (party_stack_get_troop_id, ":stack_troop", ":party_no", ":i_stack"),
              (neg|troop_is_hero, ":stack_troop"),
              (party_stack_get_size, ":stack_size", ":party_no", ":i_stack"),
              (store_character_level, ":stack_level", ":stack_troop"),
              (store_troop_faction, ":stack_faction", ":stack_troop"),
              (try_begin),
                (eq, ":troop_faction", ":stack_faction"),
                (val_mul, ":stack_level", 3),
              (try_end),
              (store_sub, ":level_dif", ":average_level", ":stack_level"),
              (val_div, ":level_dif", 3),
              (store_add, ":prune_chance", 10, ":level_dif"),
              (gt, ":prune_chance", 0),
              (call_script, "script_get_percentage_with_randomized_round", ":stack_size", ":prune_chance"),
              (gt, reg0, 0),
              (party_remove_members, ":party_no", ":stack_troop", reg0),
            (try_end),
          (try_end),
        (try_end),
    ]),
    
    # script_get_percentage_with_randomized_round
    # Input: arg1 = value, arg2 = percentage
    # Output: none
    ("get_percentage_with_randomized_round",
      [
        (store_script_param, ":value", 1),
        (store_script_param, ":percentage", 2),
        
        (store_mul, ":result", ":value", ":percentage"),
        (val_div, ":result", 100),
        (store_mul, ":used_amount", ":result", 100),
        (val_div, ":used_amount", ":percentage"),
        (store_sub, ":left_amount", ":value", ":used_amount"),
        (try_begin),
          (gt, ":left_amount", 0),
          (store_mul, ":chance", ":left_amount", ":percentage"),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", ":chance"),
          (val_add, ":result", 1),
        (try_end),
        (assign, reg0, ":result"),
    ]),
    
    # script_cf_create_merchant_party
    # Input: arg1 = troop_no,
    # Output: $pout_party = party_no
    ##  ("cf_create_merchant_party",
    ##    [
    ##      (store_script_param_1, ":troop_no"),
    ##      (store_troop_faction, ":troop_faction", ":troop_no"),
    ##
    ##      (call_script, "script_cf_select_random_town_at_peace_with_faction", ":troop_faction"),
    ##      (assign, ":center_no", reg0),
    ##
    ##      (assign, "$pout_party", -1),
    ##      (set_spawn_radius,0),
    ##      (spawn_around_party,":center_no", "pt_merchant_party"),
    ##      (assign, "$pout_party", reg0),
    ##
    ##      (party_set_faction, "$pout_party", ":troop_faction"),
    ##      (party_set_slot, "$pout_party", slot_party_type, spt_merchant_caravan),
    ##      (party_set_slot, "$pout_party", slfot_party_ai_state, spai_undefined),
    ##      (troop_set_slot, ":troop_no", slot_troop_leaded_party, "$pout_party"),
    ##      (party_add_leader, "$pout_party", ":troop_no"),
    ##      (str_store_troop_name, s5, ":troop_no"),
    ##      (party_set_name, "$pout_party", "str_s5_s_caravan"),
    ##      (party_set_ai_behavior, "$pout_party", ai_bhvr_travel_to_party),
    ##      (party_set_ai_object, "$pout_party", ":center_no"),
    ##      (party_set_flags, "$pout_party", pf_default_behavior, 0),
    ##      (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
    ##      (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
    ##        (store_add, ":cur_goods_price_slot", ":cur_goods", ":item_to_price_slot"),
    ##        (party_set_slot, "$pout_party", ":cur_goods_price_slot", average_price_factor),
    ##      (try_end),
    ##      (troop_set_slot, ":troop_no", slot_troop_wealth, 2000),
    ##  ]),
    
    # script_create_cattle_herd
    # Input: arg1 = center_no, arg2 = amount (0 = default)
    # Output: reg0 = party_no
    ("create_cattle_herd",
      [
        (store_script_param_1, ":center_no"),
        (store_script_param_2, ":amount"),
        
        (assign, ":herd_party", -1),
        (set_spawn_radius,1),
        
        (spawn_around_party,":center_no", "pt_cattle_herd"),
        (assign, ":herd_party", reg0),
        (party_get_position, pos1, ":center_no"),
        (call_script, "script_map_get_random_position_around_position_within_range", 1, 2),
        (party_set_position, ":herd_party", pos2),
        
        (party_set_slot, ":herd_party", slot_party_type, spt_cattle_herd),
        (party_set_slot, ":herd_party", slot_party_ai_state, spai_undefined),
        (party_set_ai_behavior, ":herd_party", ai_bhvr_hold),
        
        (party_set_slot, ":herd_party", slot_party_commander_party, -1), #we need this because 0 is player's party!
        
        (try_begin),
          (gt, ":amount", 0),
          (party_clear, ":herd_party"),
          (party_add_members, ":herd_party", "trp_cattle", ":amount"),
        (try_end),
        
        (assign, reg0, ":herd_party"),
    ]),
    
    #script_buy_cattle_from_village
    # Input: arg1 = village_no, arg2 = amount, arg3 = single_cost
    # Output: reg0 = party_no
    ("buy_cattle_from_village",
      [
        (store_script_param, ":village_no", 1),
        (store_script_param, ":amount", 2),
        (store_script_param, ":single_cost", 3),
        
        #Changing price of the cattle
        (try_for_range, ":unused", 0, ":amount"),
          (call_script, "script_game_event_buy_item", "itm_trade_cattle_meat", 0),
          (call_script, "script_game_event_buy_item", "itm_trade_cattle_meat", 0),
        (try_end),
        
        (party_get_slot, ":num_cattle", ":village_no", slot_village_number_of_cattle),
        (val_sub, ":num_cattle", ":amount"),
        (party_set_slot, ":village_no", slot_village_number_of_cattle, ":num_cattle"),
        (store_mul, ":cost", ":single_cost", ":amount"),
        (troop_remove_gold, "trp_player", ":cost"),
        
        (assign, ":continue", 1),
        (try_for_parties, ":cur_party"),
          (eq, ":continue", 1),
          (party_slot_eq, ":cur_party", slot_party_type, spt_cattle_herd),
          (store_distance_to_party_from_party, ":dist", ":village_no", ":cur_party"),
          (lt, ":dist", 6),
          (assign, ":subcontinue", 1),
          (try_begin),
            (check_quest_active, "qst_move_cattle_herd"),
            (quest_slot_eq, "qst_move_cattle_herd", slot_quest_target_party, ":cur_party"),
            (assign, ":subcontinue", 0),
          (try_end),
          (eq, ":subcontinue", 1),
          (party_add_members, ":cur_party", "trp_cattle", ":amount"),
          (assign, ":continue", 0),
          (assign, reg0, ":cur_party"),
        (try_end),
        (try_begin),
          (eq, ":continue", 1),
          (call_script, "script_create_cattle_herd", ":village_no", ":amount"),
        (try_end),
    ]),
    
    #script_kill_cattle_from_herd
    # Input: arg1 = party_no, arg2 = amount
    # Output: none (fills trp_temp_troop's inventory)
    ("kill_cattle_from_herd",
      [
        (store_script_param_1, ":party_no"),
        (store_script_param_2, ":amount"),
        
        (troop_clear_inventory, "trp_temp_troop"),
        (store_mul, ":meat_amount", ":amount", 2),
        (troop_add_items, "trp_temp_troop", "itm_trade_cattle_meat", ":meat_amount"),
        
        (troop_get_inventory_capacity, ":inv_size", "trp_temp_troop"),
        (try_for_range, ":i_slot", 0, ":inv_size"),
          (troop_get_inventory_slot, ":item_id", "trp_temp_troop", ":i_slot"),
          (eq, ":item_id", "itm_trade_cattle_meat"),
          (troop_set_inventory_slot_modifier, "trp_temp_troop", ":i_slot", imod_fresh),
        (try_end),
        
        (party_get_num_companions, ":num_cattle", ":party_no"),
        (try_begin),
          (ge, ":amount", ":num_cattle"),
          (remove_party, ":party_no"),
        (else_try),
          (party_remove_members, ":party_no", "trp_cattle", ":amount"),
        (try_end),
    ]),
    
    # script_create_kingdom_hero_party
    # Input: arg1 = troop_no, arg2 = center_no
    # Output: $pout_party = party_no
    ("create_kingdom_hero_party",
      [
        (store_script_param, ":troop_no", 1),
        (store_script_param, ":center_no", 2),
        
        (store_troop_faction, ":troop_faction_no", ":troop_no"),
        
        (assign, "$pout_party", -1),
        (try_begin),															#	1.143 Port // Added to (set_spawn_radius, 0),
			(eq, "$g_there_is_no_avaliable_centers", 0),
			(set_spawn_radius, 0),
		(else_try),
			(set_spawn_radius, 15),
		(try_end),																#	End
        (spawn_around_party, ":center_no", "pt_kingdom_hero_party"),
        
        (assign, "$pout_party", reg0),
        
        (party_set_faction, "$pout_party", ":troop_faction_no"),
        (party_set_slot, "$pout_party", slot_party_type, spt_kingdom_hero_party),
        (call_script, "script_party_set_ai_state", "$pout_party", spai_undefined, -1),
        (troop_set_slot, ":troop_no", slot_troop_leaded_party, "$pout_party"),
        (party_add_leader, "$pout_party", ":troop_no"),
        (str_store_troop_name, s5, ":troop_no"),
        (party_set_name, "$pout_party", "str_s5_s_party"),
        
        (party_set_slot, "$pout_party", slot_party_commander_party, -1), #we need this because 0 is player's party!
        
        #Setting the flag icon
        #normal_banner_begin
        (troop_get_slot, ":cur_banner", ":troop_no", slot_troop_banner_scene_prop),
        (try_begin),
          (gt, ":cur_banner", 0),
          (val_sub, ":cur_banner", banner_scene_props_begin),
          (val_add, ":cur_banner", banner_map_icons_begin),
          (party_set_banner_icon, "$pout_party", ":cur_banner"),
          #custom_banner_begin
          #(troop_get_slot, ":flag_icon", ":troop_no", slot_troop_custom_banner_map_flag_type),
          #(try_begin),
          #  (ge, ":flag_icon", 0),
          #  (val_add, ":flag_icon", custom_banner_map_icons_begin),
          #  (party_set_banner_icon, "$pout_party", ":flag_icon"),
        (try_end),
        
        (try_begin),
          #because of below two lines, lords can only hire more than one party_template(stack) at game start once a time during all game.
          (troop_slot_eq, ":troop_no", slot_troop_spawned_before, 0),
          (troop_set_slot, ":troop_no", slot_troop_spawned_before, 1),
          (assign, ":num_tries", 20),
          (try_begin),
            (store_troop_faction, ":troop_kingdom", ":troop_no"),
            (faction_slot_eq, ":troop_kingdom", slot_faction_leader, ":troop_no"),
            (assign, ":num_tries", 50),
          (try_end),
          
          #(str_store_troop_name, s0, ":troop_no"),
          #(display_message, "{!}str_debug__hiring_men_to_party_for_s0"),
          
          (try_for_range, ":unused", 0, ":num_tries"),
            (call_script, "script_hire_men_to_kingdom_hero_party", ":troop_no"),
          (try_end),
          
          (assign, ":xp_rounds", 0),
          
          (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
          (try_begin),
            (this_or_next|eq, ":troop_faction_no", "$players_kingdom"),
            (eq, ":troop_faction_no", "fac_player_supporters_faction"),
            (assign, ":xp_rounds", 0),
          (else_try),
            (eq, ":reduce_campaign_ai", 0), #hard
            (assign, ":xp_rounds", 2),
          (else_try),
            (eq, ":reduce_campaign_ai", 1), #moderate
            (assign, ":xp_rounds", 1),
          (else_try),
            (eq, ":reduce_campaign_ai", 2), #easy
            (assign, ":xp_rounds", 0),
          (try_end),
          
          (troop_get_slot, ":renown", ":troop_no", slot_troop_renown),
          (store_div, ":renown_xp_rounds", ":renown", 100),
          (val_add, ":xp_rounds", ":renown_xp_rounds"),
          (try_for_range, ":unused", 0, ":xp_rounds"),
            (call_script, "script_upgrade_hero_party", "$pout_party", 4000),
          (try_end),
        (try_end),
    ]),
    
    
    
    # script_create_kingdom_party_if_below_limit
    # Input: arg1 = faction_no, arg2 = party_type (variables beginning with spt_)
    # Output: reg0 = party_no
    ("create_kingdom_party_if_below_limit",
      [
        (store_script_param_1, ":faction_no"),
        (store_script_param_2, ":party_type"),
        
        (call_script, "script_count_parties_of_faction_and_party_type", ":faction_no", ":party_type"),
        (assign, ":party_count", reg0),
        
        (assign, ":party_count_limit", 0),
        
        (faction_get_slot, ":num_towns", ":faction_no", slot_faction_num_towns),
        
        (try_begin),
          ##        (eq, ":party_type", spt_forager),
          ##        (assign, ":party_count_limit", 1),
          ##      (else_try),
          ##        (eq, ":party_type", spt_scout),
          ##        (assign, ":party_count_limit", 1),
          ##      (else_try),
          ##        (eq, ":party_type", spt_patrol),
          ##        (assign, ":party_count_limit", 1),
          ##      (else_try),
          ##        (eq, ":party_type", spt_messenger),
          ##        (assign, ":party_count_limit", 1),
          ##      (else_try),

          (eq, ":party_type", spt_kingdom_caravan),
          (try_begin),
            (eq, ":num_towns", 0),
            (assign, ":party_count_limit", 0),
          (else_try),
            (eq, ":num_towns", 1),
            (assign, ":party_count_limit", 1),
          (else_try),
            (eq, ":num_towns", 2),
            (assign, ":party_count_limit", 3),
          (else_try),
            (assign, ":party_count_limit", 5),
          (try_end),
          ##      (else_try),
          ##        (eq, ":party_type", spt_prisoner_train),
          ##        (assign, ":party_count_limit", 1),
        (try_end),
		
		(try_begin),
		(eq, ":party_type", spt_merchant_caravan),
		(try_begin),
			(eq, ":num_towns", 0),
			(assign, ":party_count_limit", 0),
		(else_try),	
			(eq, ":num_towns", 1),
            (assign, ":party_count_limit", 1),
		(else_try),
			(eq, ":num_towns", 2),
            (assign, ":party_count_limit", 1),
		(else_try),	
            (assign, ":party_count_limit", 2),
		(try_end),
		(try_end),
        
        (assign, reg0, -1),
        (try_begin),
          (lt, ":party_count", ":party_count_limit"),
          (call_script,"script_cf_create_kingdom_party", ":faction_no", ":party_type"),
        (try_end),
    ]),
    
    
    # script_cf_create_kingdom_party
    # Input: arg1 = faction_no, arg2 = party_type (variables beginning with spt_)
    # Output: reg0 = party_no
    ("cf_create_kingdom_party",
      [
        (store_script_param_1, ":faction_no"),
        (store_script_param_2, ":party_type"),
        
        (str_store_faction_name, s7, ":faction_no"),
        (assign, ":party_name_str", "str_no_string"),
        
        ##      (faction_get_slot, ":reinforcements_a", ":faction_no", slot_faction_reinforcements_a),
        (faction_get_slot, ":reinforcements_b", ":faction_no", slot_faction_reinforcements_b),
        ##      (faction_get_slot, ":reinforcements_c", ":faction_no", slot_faction_reinforcements_c),
        
        (try_begin),
          ##        (eq, ":party_type", spt_forager),
          ##        (assign, ":party_template", "pt_forager_party"),
          #        (assign, ":party_name_str", "str_s7_foragers"),
          ##      (else_try),
          ##        (eq, ":party_type", spt_scout),
          ##        (assign, ":party_template", "pt_scout_party"),
          #        (assign, ":party_name_str", "str_s7_scouts"),
          ##      (else_try),
          ##        (eq, ":party_type", spt_patrol),
          ##        (assign, ":party_template", "pt_patrol_party"),
          #        (assign, ":party_name_str", "str_s7_patrol"),
          ##      (else_try),
          (eq, ":party_type", spt_kingdom_caravan),
          (assign, ":party_template", "pt_kingdom_caravan_party"),
          #        (assign, ":party_name_str", "str_s7_caravan"),
        (else_try),
          (eq, ":party_type", spt_merchant_caravan),
				##Floris MTT begin
				(try_begin),
		 			(eq, "$troop_trees", troop_trees_0),
					(assign, ":party_template", "pt_sea_traders"),            #####SEATRADE Marker#####
				(else_try),
		 			(eq, "$troop_trees", troop_trees_1),
					(assign, ":party_template", "pt_sea_traders_r"),            #####SEATRADE Marker#####
				(else_try),
					(eq, "$troop_trees", troop_trees_2),
					(assign, ":party_template", "pt_sea_traders_e"),            #####SEATRADE Marker#####
				(try_end),
				##Floris MTT end
          ##      (else_try),
          ##        (eq, ":party_type", spt_messenger),
          ##        (assign, ":party_template", "pt_messenger_party"),
          #        (assign, ":party_name_str", "str_s7_messenger"),
          ##      (else_try),
          ##        (eq, ":party_type", spt_raider),
          ##        (assign, ":party_template", "pt_raider_party"),
          ##        (assign, ":party_name_str", "str_s7_raiders"),
          ##      (else_try),
          ##        (eq, ":party_type", spt_prisoner_train),
          ##        (assign, ":party_template", "pt_prisoner_train_party"),
          #        (assign, ":party_name_str", "str_s7_prisoner_train"),
        (try_end),
        
        (assign, ":result", -1),
        (try_begin),
          (try_begin),
            (this_or_next|eq, ":party_type", spt_merchant_caravan),   ##SEA TRADE
            (eq, ":party_type", spt_kingdom_caravan),
            (call_script,"script_cf_select_random_town_with_faction", ":faction_no", -1),
            (set_spawn_radius, 0),
          (else_try), #not used at the moment
            (call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),
            (set_spawn_radius, 1),
          (try_end),
          (assign, ":spawn_center", reg0),
          (is_between, ":spawn_center", centers_begin, centers_end),
        (assign, ":continue", 0), ## SEA TRADE
        (try_begin),
            (eq, ":party_type", spt_kingdom_caravan),
            (spawn_around_party,":spawn_center",":party_template"),
            (assign, ":result", reg0),
            (assign, ":continue", 1),
        (else_try),        
            (eq, ":party_type", spt_merchant_caravan),
            (party_slot_ge, ":spawn_center", slot_town_is_coastal, 1),
            (party_get_slot, ":radius", ":spawn_center", slot_town_is_coastal),
            (party_get_position, pos0 , ":spawn_center"),
            (map_get_water_position_around_position, pos1, pos0, ":radius"),
            (spawn_around_party,":spawn_center",":party_template"),
            (assign, ":result", reg0),
            (party_set_position, ":result", pos1),
            (assign, ":continue", 1),
        (try_end),    
        (eq, ":continue", 1), ## SEA TRADE END

          (party_set_faction, ":result", ":faction_no"),
          (try_begin),
            (this_or_next|eq, ":party_type", spt_merchant_caravan), ##SEA TRADE
            (eq, ":party_type", spt_kingdom_caravan),
            (party_set_slot, ":result", slot_party_home_center, ":spawn_center"),
            (party_set_slot, ":result", slot_party_last_traded_center, ":spawn_center"),
          (try_end),
          (party_set_slot, ":result", slot_party_type, ":party_type"),
          (party_set_slot, ":result", slot_party_ai_state, spai_undefined),
          (try_begin),
            (neq, ":party_name_str", "str_no_string"),
            (party_set_name, ":result", ":party_name_str"),
          (try_end),
          
          (try_begin),
            ##          (eq, ":party_type", spt_forager),
            ##          (party_add_template, ":result", ":reinforcements_a"),
            ##        (else_try),
            ##          (eq, ":party_type", spt_scout),
            ##          (party_add_template, ":result", ":reinforcements_c"),
            ##        (else_try),
            ##          (eq, ":party_type", spt_patrol),
            ##          (party_add_template, ":result", ":reinforcements_a"),
            ##          (party_add_template, ":result", ":reinforcements_b"),
            ##        (else_try),
            (this_or_next|eq, ":party_type", spt_merchant_caravan),   ##SEA TRADE
            (eq, ":party_type", spt_kingdom_caravan),
            (try_begin),
              (eq, ":faction_no", "fac_player_supporters_faction"),
              (party_get_slot, ":reinforcement_faction", ":spawn_center", slot_center_original_faction),
              (faction_get_slot, ":reinforcements_b", ":reinforcement_faction", slot_faction_reinforcements_b),
            (try_end),
            (party_add_template, ":result", ":reinforcements_b"),
            (party_add_template, ":result", ":reinforcements_b"),
            (party_set_ai_behavior,":result",ai_bhvr_travel_to_party),
            (party_set_ai_object,":result",":spawn_center"),
            (party_set_flags, ":result", pf_default_behavior, 1),
            (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
            (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
              (store_add, ":cur_goods_price_slot", ":cur_goods", ":item_to_price_slot"),
              (party_set_slot, ":result", ":cur_goods_price_slot", average_price_factor),
            (try_end),
	        (party_set_bandit_attraction, ":result", 75), ##ADDED THIS LINE
	  		  ## Floris - Trade with Merchant Caravans
			  (party_get_slot, ":town_prosperity", ":spawn_center", slot_town_prosperity),
			  (val_max, ":town_prosperity", 40),
			  (store_random_in_range, ":prosperity", 30, ":town_prosperity"),
			  (party_set_slot, ":result", slot_town_prosperity, ":prosperity"),
			  #(assign, reg1, ":prosperity"), #DEBUG
			  (val_mul, ":prosperity", 50),
			  (store_random_in_range, ":wealth", 600, ":prosperity"),
			  (party_set_slot, ":result", slot_town_wealth, ":wealth"),
			  #(assign, reg0, ":result"), #DEBUG
			  #(assign, reg2, ":wealth"), #DEBUG
			  #(display_message, "@Pty{reg0} - Prosperity: {reg1}; Wealth: {reg2}"), #DEBUG
			  (party_set_slot, ":result", slot_center_player_relation, 0),
			  (assign, reg1, 0), #Profit, typically
			  (call_script, "script_refresh_travelling_merchant_inventory", ":result"),
			  ## Floris - Trade with Merchant Caravans
            ##        (else_try),
            ##          (eq, ":party_type", spt_messenger),
            ##          (faction_get_slot, ":messenger_troop", ":faction_no", slot_faction_messenger_troop),
            ##          (party_add_leader, ":result", ":messenger_troop"),
            ##          (party_set_ai_behavior,":result",ai_bhvr_travel_to_party),
            ##          (party_set_ai_object,":result",":spawn_center"),
            ##          (party_set_flags, ":result", pf_default_behavior, 0),
            ##        (else_try),
            ##          (eq, ":party_type", spt_raider),
            ##          (party_add_template, ":result", ":reinforcements_c"),
            ##          (party_add_template, ":result", ":reinforcements_b"),
            ##          (party_add_template, ":result", "pt_raider_captives"),
            ##        (else_try),
            ##          (eq, ":party_type", spt_prisoner_train),
            ##          (party_add_template, ":result", ":reinforcements_b"),
            ##          (party_add_template, ":result", ":reinforcements_a"),
            ##          (try_begin),
            ##            (call_script,"script_cf_faction_get_random_enemy_faction",":faction_no"),
            ##            (store_random_in_range,":r",0,3),
            ##            (try_begin),
            ##              (lt, ":r", 1),
            ##              (faction_get_slot, ":captive_reinforcements", reg0, slot_faction_reinforcements_b),
            ##            (else_try),
            ##              (faction_get_slot, ":captive_reinforcements", reg0, slot_faction_reinforcements_a),
            ##            (try_end),
            ##            (party_add_template, ":result", ":captive_reinforcements",1),
            ##          (else_try),
            ##            (party_add_template, ":result", "pt_default_prisoners"),
            ##          (try_end),
          (try_end),
        (try_end),
        (ge, ":result", 0),
        (assign, reg0, ":result"),
    ]),
    
    
    # script_get_troop_attached_party
    # Input: arg1 = troop_no
    # Output: reg0 = party_no (-1 if troop's party is not attached to a party)
    ("get_troop_attached_party",
      [
        (store_script_param_1, ":troop_no"),
        
        (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
        (assign, ":attached_party_no", -1),
        (try_begin),
          (ge, ":party_no", 0),
          (party_get_attached_to, ":attached_party_no", ":party_no"),
        (try_end),
        (assign, reg0, ":attached_party_no"),
    ]),
    
    
  # script_center_get_food_consumption
  # Input: arg1 = center_no
  # Output: reg0: food consumption (1 food item counts as 100 units)
  ("center_get_food_consumption",
    [
      (store_script_param_1, ":center_no"),
      (assign, ":food_consumption", 0),
      (try_begin),
        (party_slot_eq, ":center_no", slot_party_type, spt_town),
        (assign, ":food_consumption", 500),
      (else_try),
        (party_slot_eq, ":center_no", slot_party_type, spt_castle),
        (assign, ":food_consumption", 50),
      (try_end),
      ##diplomacy start+
      (try_begin),
         (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),
		 #Optional change: increase food consumption with garrison size
		 #The rationale goes like this:
		 #The average reinforcement size for a town or castle is 9.5 per round.
		 #At the start of the game:
		 #
		 #  Castles get 15 reinforcement rounds, for around 142.5 troops
		 #  Towns   get 40 reinforcement rounds, for around 380 troops
		 #
		 #Of course both the castles and the towns have other people living
		 #there as well.
		 (party_get_num_companions, ":garrison_size", ":center_no"),
		 (try_begin),
			(party_slot_eq, ":center_no", slot_party_type, spt_castle),
			(gt, ":garrison_size", 150),
			#Assume that the garrison accounts for most of the food consumption.
			(store_div, ":food_consumption", ":garrison_size", 3),
		 (else_try),
			(party_slot_eq, ":center_no", slot_party_type, spt_town),
			(gt, ":garrison_size", 380),
			#Assume that the garrison makes the same contribution to size for towns.
			(store_div, ":food_consumption", ":garrison_size", 3),#for 381, equals 127
			(val_add, ":food_consumption", 500 - 127),
		 (try_end),
		 
		 #Optional change: increase food consumption with prosperity
		 (party_slot_eq, ":center_no", slot_party_type, spt_town),
         (party_get_slot, reg0, ":center_no", slot_town_prosperity),
			(gt, reg0, 50),#<- increase only
         (val_add, reg0, 75),
         (val_mul, ":food_consumption", reg0),
         (val_add, ":food_consumption", 62),
         (val_div, ":food_consumption", 125),
      (try_end),
      ##diplomacy+
      (assign, reg0, ":food_consumption"),
  ]),
    
    # script_center_get_food_store_limit
    # Input: arg1 = center_no
    # Output: reg0: food consumption (1 food item counts as 100 units)
    ("center_get_food_store_limit",
      [
        (store_script_param_1, ":center_no"),
        (assign, ":food_store_limit", 0),
        (try_begin),
          (party_slot_eq, ":center_no", slot_party_type, spt_town),
        (assign, ":food_store_limit", 10000), #TEMPERED CHANGED FROM 50000 TO 10000
        (else_try),
          (party_slot_eq, ":center_no", slot_party_type, spt_castle),
          (assign, ":food_store_limit", 1500),
        (try_end),
        (assign, reg0, ":food_store_limit"),
    ]),
    

  # script_refresh_village_merchant_inventory
  # Input: arg1 = village_no
  # Output: none
  ("refresh_village_merchant_inventory",
    [
      (store_script_param_1, ":village_no"),
      (party_get_slot, ":merchant_troop", ":village_no", slot_town_elder),
      (reset_item_probabilities,0),

	  (party_get_slot, ":bound_center", ":village_no", slot_village_bound_center),

	  (assign, ":total_probability", 0),
      (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),		
	    (call_script, "script_center_get_production", ":village_no", ":cur_good"),
		(assign, ":cur_probability", reg0),

        (call_script, "script_center_get_production", ":bound_center", ":cur_good"),
		(val_div, reg0, 5), #also add 1/5 of bound center production to village's inventory.
		(val_add, ":cur_probability", reg0),

		(val_max, ":cur_probability", 5),	  	  
		(val_add, ":total_probability", ":cur_probability"),
      (try_end),
	  
	  (try_begin),
		(party_get_slot, ":prosperity", ":village_no", slot_town_prosperity),
		(val_div, ":prosperity", 15), #up to 6
		(store_add, ":number_of_items_in_village", ":prosperity", 1),
	  (try_end),

      (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
	    (call_script, "script_center_get_production", ":village_no", ":cur_good"),
		(assign, ":cur_probability", reg0),

        (call_script, "script_center_get_production", ":bound_center", ":cur_good"),
		(val_div, reg0, 5), #also add 1/5 of bound center production to village's inventory.
		(val_add, ":cur_probability", reg0),

		(val_max, ":cur_probability", 5),
        (val_mul, ":cur_probability", ":number_of_items_in_village"),
		(val_mul, ":cur_probability", 100),
		(val_div, ":cur_probability", ":total_probability"),

        (set_item_probability_in_merchandise, ":cur_good", ":cur_probability"),
      (try_end),

      (troop_clear_inventory, ":merchant_troop"),
      (troop_add_merchandise, ":merchant_troop", itp_type_goods, ":number_of_items_in_village"),
      (troop_ensure_inventory_space, ":merchant_troop", 80),

      #Adding 1 prosperity to the village while reducing each 3000 gold from the elder
      (store_troop_gold, ":gold",":merchant_troop"),
      (try_begin),
        (gt, ":gold", 3500),
        (store_div, ":prosperity_added", ":gold", 3000),
        (store_mul, ":gold_removed", ":prosperity_added", 3000),
        (troop_remove_gold, ":merchant_troop", ":gold_removed"),
        (call_script, "script_change_center_prosperity", ":village_no", ":prosperity_added"),
      (try_end),
  ]),
    
    # script_refresh_village_defenders
    # Input: arg1 = village_no
    # Output: none
    ("refresh_village_defenders",
      [
        (store_script_param_1, ":village_no"),
        
        (assign, ":ideal_size", 50),
        (try_begin),
          (party_get_num_companions, ":party_size", ":village_no"),
          (lt, ":party_size", ":ideal_size"),
			##Floris MTT begin
			(try_begin),
				(eq, "$troop_trees", troop_trees_0),
				(party_add_template, ":village_no", "pt_village_defenders"),
			(else_try),
				(eq, "$troop_trees", troop_trees_1),
				(party_add_template, ":village_no", "pt_village_defenders_r"),
			(else_try),
				(eq, "$troop_trees", troop_trees_2),
				(party_add_template, ":village_no", "pt_village_defenders_e"),
			(try_end),
			##Floris MTT end
        (try_end),
    ]),

				##Floris MTT begin
    ("start_refresh_village_defenders",
      [
        (store_script_param_1, ":village_no"),
        
        (assign, ":ideal_size", 50),
        (try_begin),
            (party_get_num_companions, ":party_size", ":village_no"),
            (lt, ":party_size", ":ideal_size"),
			(party_add_template, ":village_no", "pt_village_defenders_e"),  ## BUG - CABA
        (try_end),
    ]),
				##Floris MTT end
    
  # script_village_set_state
  # Input: arg1 = center_no arg2:new_state
  # Output: reg0: food consumption (1 food item counts as 100 units)
  ("village_set_state",
    [
      (store_script_param_1, ":village_no"),
      (store_script_param_2, ":new_state"),
#      (party_get_slot, ":old_state", ":village_no", slot_village_state),
	  ##diplomacy start+
	  (store_current_hours, ":hours"),
	  (party_get_slot, ":attacker_party", ":village_no", slot_village_raided_by),
	  (try_begin),
		(ge, ":attacker_party", 0),
		(party_is_active, ":attacker_party"),#added 2011-06-07
		(party_stack_get_troop_id, ":attack_leader", ":attacker_party", 0),
		(ge, ":attack_leader", 0),
		(party_set_slot, ":village_no", dplmc_slot_center_last_attacked_time, ":hours"),
		(party_set_slot, ":village_no", dplmc_slot_center_last_attacker, ":attack_leader"),
	  (try_end),
	  ##diplomacy end+
	  
      (try_begin),
        (eq, ":new_state", 0),
        (party_set_extra_text, ":village_no", "str_empty_string"),
        (party_set_slot, ":village_no", slot_village_raided_by, -1),
      (else_try),
        (eq, ":new_state", svs_being_raided),
        (party_set_extra_text, ":village_no", "@(Being Raided)"),
      (else_try),
        (eq, ":new_state", svs_looted),
        (party_set_extra_text, ":village_no", "@(Looted)"),

        (party_set_slot, ":village_no", slot_village_raided_by, -1),
        (call_script, "script_change_center_prosperity", ":village_no", -60), #reduced from 30
		(val_add, "$newglob_total_prosperity_from_villageloot", -60),

		(try_begin), #optional - lowers the relationship between a lord and his liege if his fief is looted
			(eq, 5, 0),
			(party_get_slot, ":town_lord", ":village_no", slot_town_lord),
			(is_between, ":town_lord", active_npcs_begin, active_npcs_end),
			(store_faction_of_troop, ":town_lord_faction", ":town_lord"),
			(faction_get_slot, ":faction_leader", ":town_lord_faction", slot_faction_leader),
			(call_script, "script_troop_change_relation_with_troop", ":town_lord", ":faction_leader", -1),
			(val_add, "$total_battle_ally_changes", -1),
		(try_end),
      (else_try),
        (eq, ":new_state", svs_under_siege),
        (party_set_extra_text, ":village_no", "@(Under Siege)"),

		#Divert all caravans heading to the center
		#Note that occasionally, no alternative center will be found. In that case, the caravan will try to run the blockade
		(try_for_parties, ":party_no"),
			(gt, ":party_no", "p_spawn_points_end"),
			(party_slot_eq, ":party_no", slot_party_type, spt_kingdom_caravan),
            (party_slot_eq, ":party_no", slot_party_ai_object, ":village_no"),

			(party_get_slot, ":origin", ":party_no", slot_party_last_traded_center),
			(store_faction_of_party, ":merchant_faction", ":party_no"),
            ##diplomacy start+ added new third parameter, the caravan party itself
            (call_script, "script_cf_select_most_profitable_town_at_peace_with_faction_in_trade_route", ":origin", ":merchant_faction",
				":party_no"),
			##diplomacy end+
            (assign, ":target_center", reg0),
			(is_between, ":target_center", centers_begin, centers_end),

            (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
            (party_set_ai_object, ":party_no", ":target_center"),
            (party_set_flags, ":party_no", pf_default_behavior, 0),
            (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
            (party_set_slot, ":party_no", slot_party_ai_object, ":target_center"),
		(try_end),
      (try_end),
      (party_set_slot, ":village_no", slot_village_state, ":new_state"),
  ]),
    
    
    # script_process_village_raids
    # Input: none
    # Output: none
    # called from triggers every two hours
  ("process_village_raids",
    [
	   ##diplomacy start+
	   (store_current_hours, ":hours"),
	   ##diplomacy end+
       (try_for_range, ":village_no", villages_begin, villages_end),
		##CABA Fix 																												#	1.143 Port // Newly Added
        (try_begin), 
          (this_or_next|is_between, ":village_no", "p_village_16", "p_village_23"), #Shapeshte through Shulus (up to Ilvia) 
          (this_or_next|is_between, ":village_no", "p_village_49", "p_village_51"), #Tismirr and Karindi 
          (this_or_next|eq, ":village_no", "p_village_75"), #Bhulaban 
          (is_between, ":village_no", "p_village_85", "p_village_87"), #Ismirala and Slezkh 
          (assign, ":normal_village_icon", "icon_village_snow_a"),  
          (assign, ":burnt_village_icon", "icon_village_snow_burnt_a"), 
          (assign, ":deserted_village_icon", "icon_village_snow_deserted_a"), 
        (else_try), 
          (is_between, ":village_no", "p_village_91", "p_salt_mine"), #Ayn Assuadi through Rushdigh 
          (assign, ":normal_village_icon", "icon_village_c"),  
          (assign, ":burnt_village_icon", "icon_village_burnt_c"), 
          (assign, ":deserted_village_icon", "icon_village_deserted_c"), 
        (else_try), 
          (assign, ":normal_village_icon", "icon_village_a"), 
          (assign, ":burnt_village_icon", "icon_village_burnt_a"), 
          (assign, ":deserted_village_icon", "icon_village_deserted_a"), 
        (try_end), 
        ##CABA Fix        																										#	End
          (party_get_slot, ":village_raid_progress", ":village_no", slot_village_raid_progress),
          (try_begin),
            (party_slot_eq, ":village_no", slot_village_state, 0), #village is normal
            (val_sub, ":village_raid_progress", 5),
            (val_max, ":village_raid_progress", 0),
            (party_set_slot, ":village_no", slot_village_raid_progress, ":village_raid_progress"),
            (try_begin),
              (lt, ":village_raid_progress", 50),
              
              (try_begin),
                (party_get_icon, ":village_icon", ":village_no"),
              (neq, ":village_icon", ":normal_village_icon"), ##CABA FIX 														#	1.143 Port // Changed line (village_icon_a)
              (party_set_icon, ":village_no", ":normal_village_icon"), ##CABA FIX 												#	1.143 Port // Changed line (village_icon_a)
              (try_end),
              
              (party_slot_ge, ":village_no", slot_village_smoke_added, 1),
              (party_set_slot, ":village_no", slot_village_smoke_added, 0),
              (party_clear_particle_systems, ":village_no"),
            (try_end),
          (else_try),
            (party_slot_eq, ":village_no", slot_village_state, svs_being_raided), #village is being raided
            #End raid unless there is an enemy party nearby
            (assign, ":raid_ended", 1),
            (party_get_slot, ":raider_party", ":village_no", slot_village_raided_by),
            
            (try_begin),
              (ge, ":raider_party", 0),
              (party_is_active, ":raider_party"),
              (this_or_next|neq, ":raider_party", "p_main_party"),
              (eq, "$g_player_is_captive", 0),
              (store_distance_to_party_from_party, ":distance", ":village_no", ":raider_party"),
              (lt, ":distance", raid_distance),
              (assign, ":raid_ended", 0),
            (try_end),
            
            (try_begin),
              (eq, ":raid_ended", 1),
              (call_script, "script_village_set_state", ":village_no", svs_normal), #clear raid flag
              (party_set_slot, ":village_no", slot_village_smoke_added, 0),
              (party_clear_particle_systems, ":village_no"),
            (else_try),
              (assign, ":raid_progress_increase", 11),
              (party_get_slot, ":looter_party", ":village_no", slot_village_raided_by),
              (try_begin),
                (party_get_skill_level, ":looting_skill", ":looter_party", "skl_looting"),
                (val_add, ":raid_progress_increase", ":looting_skill"),
              (try_end),
              (try_begin),
                (party_slot_eq, ":village_no", slot_center_has_watch_tower, 1),
                (val_mul, ":raid_progress_increase", 2),
                (val_div, ":raid_progress_increase", 3),
              (try_end),
              (val_add, ":village_raid_progress", ":raid_progress_increase"),
              (party_set_slot, ":village_no", slot_village_raid_progress, ":village_raid_progress"),
              (try_begin),
                (ge, ":village_raid_progress", 50),
                (party_slot_eq, ":village_no", slot_village_smoke_added, 0),
                (party_add_particle_system, ":village_no", "psys_map_village_fire"),
                (party_add_particle_system, ":village_no", "psys_map_village_fire_smoke"),
              (party_set_icon, ":village_no", ":burnt_village_icon"), ##CABA FIX 						#	1.143 Port // Changed icon_village_burnt_a
                (party_set_slot, ":village_no", slot_village_smoke_added, 1),
              (try_end),
			 ##diplomacy start+ set values of slots
			 (try_begin),
				(ge, ":looter_party", 0),
				(party_stack_get_troop_id, ":raid_leader", ":looter_party", 0),
				(ge, ":raid_leader", 0),
				(party_set_slot, ":village_no", dplmc_slot_center_last_attacked_time, ":hours"),
				(party_set_slot, ":village_no", dplmc_slot_center_last_attacker, ":raid_leader"),
			 (try_end),
			 ##diplomacy end+
              (try_begin),
                (gt, ":village_raid_progress", 100),
                (str_store_party_name_link, s1, ":village_no"),
                (party_stack_get_troop_id, ":raid_leader", ":looter_party", 0),
                (ge, ":raid_leader", 0),
                (str_store_party_name, s2, ":looter_party"),
                (display_log_message, "@The village of {s1} has been looted by {s2}."),
                
                (try_begin),
                  (party_get_slot, ":village_lord", ":village_no", slot_town_lord),
                  (is_between, ":village_lord", active_npcs_begin, active_npcs_end),
                  (call_script, "script_troop_change_relation_with_troop", ":raid_leader", ":village_lord", -1),
                  (val_add, "$total_battle_enemy_changes", -1),
                (try_end),
                
                #give loot gold to raid leader
                (troop_get_slot, ":raid_leader_gold", ":raid_leader", slot_troop_wealth),
			   ##diplomacy start+
			   #How did the next line ever work?  isn't it missing a slot number?!
               #  (party_get_slot, ":village_prosperity", ":village_no"),
			   #Replace it with the following:
			   (party_get_slot, ":village_prosperity", ":village_no", slot_town_prosperity),
			   ##diplomacy end+
                (store_mul, ":value_of_loot", ":village_prosperity", 60), #average is 3000
                (val_add, ":raid_leader_gold", ":value_of_loot"),
                (troop_set_slot, ":raid_leader", slot_troop_wealth, ":raid_leader_gold"),
                
                #take loot gold from village lord #new 1.126
##diplomacy start+
			   #With economic changes enabled, this will first withdraw from accumulated taxes at center
               (try_begin),
				 #To support the possibility of kingdom_ladies becoming enfeoffed, changed the
				 #below line from active_npcs_begin/active_npcs_end to heroes_begin/heroes_end
                 (is_between, ":village_lord", heroes_begin, heroes_end),
				 (neq, ":village_lord", "trp_kingdom_heroes_including_player_begin"),
                 (troop_get_slot, ":village_lord_gold", ":village_lord", slot_troop_wealth),
				 (try_begin),
					#Optional behavior: subtract the looted wealth from the village's uncollected
					#rents and tariffs
					(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_HIGH),#<-- check experimental changes are enabled
					(assign, ":gold_lost_by_lord", ":value_of_loot"),
					#Accumulated rents & tariffs get zeroed further down, so we don't need to worry
					#about modifying the slot's value to reflect the loss.
					(party_get_slot, ":x", ":village_no", slot_center_accumulated_rents),
					(val_max, ":x", 0),
					(val_sub, ":gold_lost_by_lord", ":x"),
					(party_get_slot, ":x", ":village_no", slot_center_accumulated_tariffs),
					(val_max, ":x", 0),
					(val_sub, ":gold_lost_by_lord", ":x"),
					#Only then subtract the remainder from the lord
					(val_max, ":gold_lost_by_lord", 0),
					(val_sub, ":village_lord_gold", ":gold_lost_by_lord"),
				 (else_try),
					#Unaltered behavior
					(val_sub, ":village_lord_gold", ":value_of_loot"),
				 (try_end),
				 #Apply the gold change
                 (val_max, ":village_lord_gold", 0),
                 (troop_set_slot, ":village_lord", slot_troop_wealth, ":village_lord_gold"),
			   (else_try), 
			      #Option: player loses gold when his fiefs are raided, just as an NPC does
				  #(default behavior in Native is the player loses no gold).  The gold is
				  #lost from the treasury, and is reduced by uncollected taxes.
				  #
				  #Only do this if the option is explicitly enabled and the player has
				  # a chamberlain.
				  (eq, ":village_lord", "trp_player"),
				  (gt, "$g_player_chamberlain", 0),#check the player has a chamberlain
			      (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),#<-- check experimental changes are enabled
				  (party_slot_eq, ":village_no", slot_town_lord, "trp_player"),
				  #Do some double-checking, to avoid potential erroneous gold loss
				  #if some careless code has improperly left the "slot_town_lord"
				  #slot of the village initialized to zero.
				  (store_faction_of_party, ":village_faction", ":village_no"),
				 ##diplomacy start+ Handle player is co-ruler of faction
				 (assign, ":is_coruler", 0),
 				 (try_begin),
				    (eq, ":village_faction", "$players_kingdom"),
					(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
					(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
					(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
					(assign, ":is_coruler", 1),
				 (try_end),
				 (this_or_next|eq, ":is_coruler", 1),
				 ##diplomacy end+
				  (this_or_next|eq, "fac_player_supporters_faction", ":village_faction"),
				     (eq, "$players_kingdom", ":village_faction"),
				  #Adjust the amount lost by difficulty setting.
				  (assign, ":gold_lost_by_lord", ":value_of_loot"),
				  (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
				  (try_begin),
				    (eq, ":reduce_campaign_ai", 0),#hard, 125% loss
					(val_mul, ":gold_lost_by_lord", 5),
					(val_div, ":gold_lost_by_lord", 4),
				  (else_try),
					(eq, ":reduce_campaign_ai", 1),#medium, 100% loss
				  (else_try),
					(eq, ":reduce_campaign_ai", 2),#easy, 50% loss
					(val_div, ":gold_lost_by_lord", 2),
				  (try_end), 
				  
				  #First defray the lost gold with rents and tarriffs from the village
				  (party_get_slot, ":x", ":village_no", slot_center_accumulated_rents),
				  (val_max, ":x", 0),
				  (val_sub, ":gold_lost_by_lord", ":x"),
				  (party_get_slot, ":x", ":village_no", slot_center_accumulated_tariffs),
				  (val_max, ":x", 0),
				  (val_sub, ":gold_lost_by_lord", ":x"),
				  (val_max, ":gold_lost_by_lord", 0),
				  #Remove the remainder (if any) from the player's treasury
				  (store_troop_gold, ":x", "trp_household_possessions"),
				  (val_min, ":gold_lost_by_lord", ":x"),
				  (ge, ":gold_lost_by_lord", 1),
				  (call_script, "script_dplmc_withdraw_from_treasury", ":gold_lost_by_lord"),
               (try_end),
			   ##diplomacy end+
                
                (call_script, "script_village_set_state",  ":village_no", svs_looted),
                (party_set_slot, ":village_no", slot_center_accumulated_rents, 0), #new 1.126
                (party_set_slot, ":village_no", slot_center_accumulated_tariffs, 0), #new 1.126
                
                (party_set_slot, ":village_no", slot_village_raid_progress, 0),
                (party_set_slot, ":village_no", slot_village_recover_progress, 0),
                (try_begin),
                 (store_faction_of_party, ":village_faction", ":village_no"),
				 ##diplomacy start+ Handle player is co-ruler of faction
				 (assign, ":is_coruler", 0),
 				 (try_begin),
				    (eq, ":village_faction", "$players_kingdom"),
					(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
					(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
					(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
					(assign, ":is_coruler", 1),
				 (try_end),
				 (this_or_next|eq, ":is_coruler", 1),
				 ##diplomacy end+
                  (this_or_next|party_slot_eq, ":village_no", slot_town_lord, "trp_player"),
                  (eq, ":village_faction", "fac_player_supporters_faction"),
                  (call_script, "script_add_notification_menu", "mnu_notification_village_raided", ":village_no", ":raid_leader"),
                (try_end),
                (call_script, "script_add_log_entry", logent_village_raided, ":raid_leader",  ":village_no", -1, -1),
                (store_faction_of_party, ":looter_faction", ":looter_party"),
                (call_script, "script_faction_inflict_war_damage_on_faction", ":looter_faction", ":village_faction", 5),
              (try_end),
            (try_end),
          (else_try),
            (party_slot_eq, ":village_no", slot_village_state, svs_looted), #village is looted
            (party_get_slot, ":recover_progress", ":village_no", slot_village_recover_progress),
            (val_add, ":recover_progress", 1),
            (party_set_slot, ":village_no", slot_village_recover_progress, ":recover_progress"), #village looted
            (try_begin),
              (ge, ":recover_progress", 10),
              (party_slot_eq, ":village_no", slot_village_smoke_added, 1),
              (party_clear_particle_systems, ":village_no"),
              (party_add_particle_system, ":village_no", "psys_map_village_looted_smoke"),
              (party_set_slot, ":village_no", slot_village_smoke_added, 2),
            (try_end),
            (try_begin),
              (gt, ":recover_progress", 50),
              (party_slot_eq, ":village_no", slot_village_smoke_added, 2),
              (party_clear_particle_systems, ":village_no"),
              (party_set_slot, ":village_no", slot_village_smoke_added, 3),
              (party_set_icon, ":village_no", ":deserted_village_icon"), ##CABA FIX 				#	1.143 Port // Changed icon_village_deserted_a
           (try_end),
           (try_begin),
             (gt, ":recover_progress", 100),
             (call_script, "script_village_set_state",  ":village_no", 0),#village back to normal
             (party_set_slot, ":village_no", slot_village_recover_progress, 0),
             (party_clear_particle_systems, ":village_no"),
             (party_set_slot, ":village_no", slot_village_smoke_added, 0),
            (party_set_icon, ":village_no", ":normal_village_icon"), ##CABA FIX 					#	1.143 Port // Changed icon_village_a
            (try_end),
          (try_end),
        (try_end),
    ]),
    
    
    # script_process_sieges
    # Input: none
    # Output: none
    #called from triggers
    ("process_sieges",
      [
        (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
          #Reducing siege hardness every day by 20
          (party_get_slot, ":siege_hardness", ":center_no", slot_center_siege_hardness),
          (val_sub, ":siege_hardness", 20),
          (val_max, ":siege_hardness", 0),
          (party_set_slot, ":center_no", slot_center_siege_hardness, ":siege_hardness"),
          
          (party_get_slot, ":town_food_store", ":center_no", slot_party_food_store),
          (call_script, "script_center_get_food_store_limit", ":center_no"),
          (assign, ":food_store_limit", reg0),
          (try_begin),
            (party_get_slot, ":besieger_party", ":center_no", slot_center_is_besieged_by),
            (ge, ":besieger_party", 0), #town is under siege
            
            #Reduce prosperity of besieged center by -1 with a 33% chance every day.
            (try_begin),
             (try_begin),
               (is_between, ":center_no", castles_begin, castles_end),
               (store_random_in_range, ":random_value", 0, 3),
               (try_begin),
                 (eq, ":random_value", 0),
                 (assign, ":daily_siege_effect_on_prosperity", -1),
               (else_try),
                 (assign, ":daily_siege_effect_on_prosperity", 0),
               (try_end),
             (else_try),
               (assign, ":daily_siege_effect_on_prosperity", -4),
             (try_end),
       
             (call_script, "script_change_center_prosperity", ":center_no", ":daily_siege_effect_on_prosperity"),
             (val_add, "$newglob_total_prosperity_from_townloot", ":daily_siege_effect_on_prosperity"),
            (try_end),
            
            (store_faction_of_party, ":center_faction", ":center_no"),
            # Lift siege unless there is an enemy party nearby
            (assign, ":siege_lifted", 0),
            (try_begin),
              (try_begin),
                (neg|party_is_active, ":besieger_party"),
                (assign, ":siege_lifted", 1),
              (else_try),
                (store_distance_to_party_from_party, ":besieger_distance", ":center_no", ":besieger_party"),
                (gt, ":besieger_distance", 5),
                (assign, ":siege_lifted", 1),
              (else_try),
                ##diplomacy begin
				##Floris MTT begin
				(troop_get_slot,":woman_peasant","$troop_trees",slot_woman_peasant),
                (neg|party_slot_eq, ":center_no", slot_village_infested_by_bandits, ":woman_peasant"),
				##Floris MTT end
                ##diplomacy end
                (store_faction_of_party, ":besieger_faction", ":besieger_party"),
                (store_relation, ":reln", ":besieger_faction", ":center_faction"),
                (ge, ":reln", 0),
                (assign, ":siege_lifted", 1),
              (try_end),
              
              
              (eq, ":siege_lifted", 1),
              #If another lord can take over the siege, it isn't lifted
             ##diplomacy start+ Support promoted kingdom ladies
             #(try_for_range, ":enemy_hero", active_npcs_begin, active_npcs_end),
             (try_for_range, ":enemy_hero", heroes_begin, heroes_end),
             ##diplomacy end+
                (troop_slot_eq, ":enemy_hero", slot_troop_occupation, slto_kingdom_hero),
                (troop_get_slot, ":enemy_party", ":enemy_hero", slot_troop_leaded_party),
                (ge, ":enemy_party", 0),
                (party_is_active, ":enemy_party"),
                (store_faction_of_party, ":party_faction", ":enemy_party"),
                (store_relation, ":reln", ":party_faction", ":center_faction"),
                (lt, ":reln", 0),
                (store_distance_to_party_from_party, ":distance", ":center_no", ":enemy_party"),
                (lt, ":distance", 4),
                (assign, ":besieger_party", ":enemy_party"),
                (party_set_slot, ":center_no", slot_center_is_besieged_by, ":enemy_party"),
                (assign, ":siege_lifted", 0),
              (try_end),
            (try_end),
            (try_begin),
              (eq, ":siege_lifted", 1),
              (call_script, "script_lift_siege", ":center_no", 1),
            (else_try),
              (call_script, "script_center_get_food_consumption", ":center_no"),
              (assign, ":food_consumption", reg0),
              (val_sub, ":town_food_store", ":food_consumption"), # reduce food only under siege???
              (try_begin),
                (le, ":town_food_store", 0), #town is starving
                (store_random_in_range, ":r", 0, 100),
                (lt, ":r", 10),
                (call_script, "script_party_wound_all_members", ":center_no"), # town falls with 10% chance if starving
              (try_end),
            (try_end),
          (else_try),
            #town is not under siege...
            (val_add, ":town_food_store", 30), #add 30 food (significant for castles only.
          (try_end),
          
          (val_min, ":town_food_store", ":food_store_limit"),
          (val_max, ":town_food_store", 0),
          (party_set_slot, ":center_no", slot_party_food_store, ":town_food_store"),
        (try_end),
    ]),
    
    # script_lift_siege
    # Input: arg1 = center_no, arg2 = display_message
    # Output: none
    #called from triggers
    ("lift_siege",
      [
        (store_script_param, ":center_no", 1),
        (store_script_param, ":display_message", 2),
        (party_set_slot, ":center_no", slot_center_is_besieged_by, -1), #clear siege
        (call_script, "script_village_set_state",  ":center_no", 0), #clear siege flag
        (try_begin),
          (eq, ":center_no", "$g_player_besiege_town"),
          (assign, "$g_siege_method", 0), #remove siege progress
        (try_end),
        (try_begin),
          (eq, ":display_message", 1),
          (str_store_party_name_link, s3, ":center_no"),
          (display_message, "@{s3} is no longer under siege."),
        (try_end),
    ]),
    
    
    # script_process_alarms
    # Input: none
    # Output: none
    #called from triggers
    ("process_alarms",
      [
        (assign, ":current_modula", "$g_alarm_modula"),
        (val_add, "$g_alarm_modula", 1),
        (try_begin),
          (eq, "$g_alarm_modula", 3),
          (assign, "$g_alarm_modula", 0),
        (try_end),
        
        (try_for_range, ":center_no", centers_begin, centers_end),
          (store_mod, ":center_modula", ":center_no", 3),
          (eq, ":center_modula", ":current_modula"),
          
          (party_set_slot, ":center_no", slot_center_last_spotted_enemy, -1),
          (party_set_slot, ":center_no", slot_center_sortie_strength, 0),
          (party_set_slot, ":center_no", slot_center_sortie_enemy_strength, 0),
          
          (assign, ":spotting_range", 3),
          (try_begin),
            (is_currently_night),
            (assign, ":spotting_range", 2),
          (try_end),
          
          (try_begin),
            (party_slot_eq, ":center_no", slot_center_has_watch_tower, 1),
            (val_mul, ":spotting_range", 2),
          (else_try),
            (neg|is_between, ":center_no", villages_begin, villages_end),
            (val_add, ":spotting_range", 1),
            (val_mul, ":spotting_range", 2),
          (try_end),
          
          (store_faction_of_party, ":center_faction", ":center_no"),
          
          (try_for_parties, ":party_no"),
            (this_or_next|party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
            (eq, ":party_no", "p_main_party"),
            
            (store_faction_of_party, ":party_faction", ":party_no"),
            
            (try_begin),
              (eq, ":party_no", "p_main_party"),
              (assign, ":party_faction", "$players_kingdom"),
            (try_end),
            
            (try_begin),
              (eq, ":party_faction", ":center_faction"),
              
              (store_distance_to_party_from_party, ":distance", ":party_no", ":center_no"),
              (le, ":distance", ":spotting_range"),
              
              (party_get_slot, ":cached_strength", ":party_no", slot_party_cached_strength),
              (party_get_slot, ":sortie_strength", ":center_no", slot_center_sortie_strength),
              (val_add, ":sortie_strength", ":cached_strength"),
              (party_set_slot, ":center_no", slot_center_sortie_strength, ":sortie_strength"),
            (else_try),
              (neq, ":party_faction", ":center_faction"),
              
              (store_distance_to_party_from_party, ":distance", ":party_no", ":center_no"),
              
              (try_begin),
                (lt, ":distance", 10),
                (store_current_hours, ":hours"),
                (store_sub, ":faction_recce_slot", ":party_faction", kingdoms_begin),
                (val_add, ":faction_recce_slot", slot_center_last_reconnoitered_by_faction_time),
                (party_set_slot, ":center_no", ":faction_recce_slot", ":hours"),
                
                #(eq, "$cheat_mode", 1),
                #(str_store_faction_name, s4, ":party_faction"),
                #(str_store_party_name, s5, ":center_no"),
                #(display_message, "@{!}DEBUG -- {s4} reconnoiters {s5}"),
              (try_end),
              
              (store_relation, ":reln", ":center_faction", ":party_faction"),
              (lt, ":reln", 0),
              (try_begin),
                (le, ":distance", ":spotting_range"),
                
                (party_get_slot, ":cached_strength", ":party_no", slot_party_cached_strength),
                (party_get_slot, ":enemy_strength", ":center_no", slot_center_sortie_enemy_strength),
                (val_add, ":enemy_strength", ":cached_strength"),
                (party_set_slot, ":center_no", slot_center_sortie_enemy_strength, ":enemy_strength"),
                (party_set_slot, ":center_no", slot_center_last_spotted_enemy, ":party_no"),
              (try_end),
              
            (try_end),
          (try_end),
        (try_end),
        
        (try_for_range, ":center_no", centers_begin, centers_end),
          (store_mod, ":center_modula", ":center_no", 3),
          (eq, ":center_modula", ":current_modula"),
          
          (try_begin), #eligible units sortie out of castle
            (is_between, ":center_no", walled_centers_begin, walled_centers_end),
            (party_slot_ge, ":center_no", slot_center_last_spotted_enemy, 0),
            
            (party_get_slot, ":sortie_strength", ":center_no", slot_center_sortie_strength),
            (party_get_slot, ":enemy_strength", ":center_no", slot_center_sortie_enemy_strength),
            
            #Below two lines are new added by ozan. While AI want to drive nearby besieging enemy parties by making sortie them, they give up current battle if they are already joining one.
            #Lets assume there is a battle inside the castle, because enemies are inside castle and they are so close to castle they will be also added to slot_center_sortie_enemy_strength
            #But in this scenario, they are not outside the castle, so searching/patrolling enemy outside the castle is useless at this point.
            #So if there is already a battle inside the center, do not sortie and search enemy outside.
            (party_get_battle_opponent, ":center_battle_opponent", ":center_no"),
            (try_begin),
              (ge, "$cheat_mode", 1),
              (ge, ":center_battle_opponent", 0),
              (str_store_party_name, s7, ":center_no"),
              (str_store_party_name, s6, ":center_battle_opponent"),
              (display_message, "@{!}DEBUG : There are already enemies ({s6}) inside {s7}."),
            (try_end),
            (lt, ":center_battle_opponent", 0),
            #New added by ozan ended.
            
            (try_begin),
              (eq, "$cheat_mode", 1),
              (str_store_party_name, s4, ":center_no"),
              (assign, reg3, ":sortie_strength"),
              (assign, reg4, ":enemy_strength"),
              (display_message, "@{!}DEBUG -- Calculating_sortie for {s4} strength of {reg3} vs {reg4} enemies"),
            (try_end),
            
            (store_mul, ":enemy_strength_mul_14_div_10", ":enemy_strength", 14),
            (val_div, ":enemy_strength_mul_14_div_10", 10),
            (gt, ":sortie_strength", ":enemy_strength_mul_14_div_10"),
            
            (assign, ":at_least_one_party_sorties", 0),
            (try_for_parties, ":sortie_party"),
              (party_get_attached_to, ":town", ":sortie_party"),
              (eq, ":town", ":center_no"),
              
              (party_slot_eq, ":sortie_party", slot_party_type, spt_kingdom_hero_party),
              
              (party_get_slot, ":cached_strength", ":sortie_party", slot_party_cached_strength),
              (ge, ":cached_strength", 100),
              
              (party_detach, ":sortie_party"),
              (call_script, "script_party_set_ai_state", ":sortie_party",  spai_patrolling_around_center, ":center_no"),
              
              (try_begin),
                (eq, "$cheat_mode", 1),
                (str_store_party_name, s4, ":sortie_party"),
                (display_message, "str_s4_sorties"),
              (try_end),
              
              (eq, ":at_least_one_party_sorties", 0),
              (assign, ":at_least_one_party_sorties", ":sortie_party"),
            (try_end),
            
            (try_begin),
              (party_is_in_town, "p_main_party", ":center_no"),
              (eq, "$g_player_is_captive", 0),
              (gt, ":at_least_one_party_sorties", 0),
              (call_script, "script_add_notification_menu", "mnu_notification_sortie_possible", ":center_no", ":sortie_party"),
            (try_end),
          (try_end),
          
          (store_faction_of_party, ":center_faction", ":center_no"),
          
          #Send message
          (this_or_next|eq, "$cheat_mode", 1), #this is message
          (this_or_next|party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
          (eq, ":center_faction", "$players_kingdom"),
          
          (party_get_slot, ":enemy_party", ":center_no", slot_center_last_spotted_enemy),
          (ge, ":enemy_party", 0),
          (store_distance_to_party_from_party, ":dist", "p_main_party", ":center_no"),
          (assign, ":has_messenger", 0),
			(try_begin),
			 ##diplomacy start+ Handle player is co-ruler of faction
			 (assign, ":is_coruler", 0),
			 (try_begin),
				(eq, ":center_faction", "$players_kingdom"),
				(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
				(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
				(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
				(assign, ":is_coruler", 1),
			 (try_end),
			 (this_or_next|eq, ":is_coruler", 1),
			 ##diplomacy end+
			  (this_or_next|party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
			  (eq, ":center_faction", "fac_player_supporters_faction"),
			  (party_slot_eq, ":center_no", slot_center_has_messenger_post, 1),
			  (assign, ":has_messenger", 1),
			(try_end),
          
          (this_or_next|eq, "$cheat_mode", 1),
          (this_or_next|lt, ":dist", 30),
          (eq, ":has_messenger", 1),
          
          (str_store_party_name_link, s1, ":center_no"),
          (party_get_slot, ":exact_enemy_strength", ":center_no", slot_center_sortie_enemy_strength),
          
          (try_begin),
            (lt, ":exact_enemy_strength", 500),
            (display_message, "@Small bands of enemies spotted near {s1}."),
          (else_try),
            (lt, ":exact_enemy_strength", 1000),
            (display_message, "@Enemy patrols spotted near {s1}."),
          (else_try),
            (lt, ":exact_enemy_strength", 2000),
            (display_message, "@Medium-sized group of enemies spotted near {s1}."),
          (else_try),
            (lt, ":exact_enemy_strength", 4000),
            (display_message, "@Significant group of enemies spotted near {s1}."),
          (else_try),
            (lt, ":exact_enemy_strength", 8000),
            (display_message, "@Army of enemies spotted near {s1}."),
          (else_try),
            (lt, ":exact_enemy_strength", 16000),
            (display_message, "@Large army of enemies spotted near {s1}."),
          (else_try),
            (display_message, "@Great host of enemies spotted near {s1}."),
          (try_end),
          #maybe do audio sound?
          
        (try_end),
    ]),
    
    # script_allow_vassals_to_join_indoor_battle
    # Input: none
    # Output: none
    ("allow_vassals_to_join_indoor_battle",
      [
        #if our commander attacks an enemy army
		 ##diplomacy start+ Support promoted kingdom ladies
		 #(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
		 (try_for_range, ":troop_no", heroes_begin, heroes_end),
		 ##diplomacy end+
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
          (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
          (gt, ":party_no", 0),
          (party_is_active, ":party_no"),
          
          (party_get_attached_to, ":party_is_attached_to", ":party_no"),
          (lt, ":party_is_attached_to", 0),
          
          (store_troop_faction, ":faction_no", ":troop_no"),
          
          (try_begin),
            #(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemies_around_center),
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
            (party_get_slot, ":commander_party", ":party_no", slot_party_ai_object),
            (gt, ":commander_party", 0),
            (party_is_active, ":commander_party"),
            
            (assign, ":besieged_center", -1),
            (try_begin),
              (party_slot_eq, ":commander_party", slot_party_ai_state, spai_holding_center), #if commander is holding a center
              (party_get_slot, ":commander_object", ":commander_party", slot_party_ai_object), #get commander's ai object (center they are holding)
              (party_get_battle_opponent, ":besieger_enemy", ":commander_object"), #get this object's battle opponent
              (party_is_active, ":besieger_enemy"), ##1.132
              #           (ge, ":besieger_enemy", 0), ##1.131
              (assign, ":besieged_center", ":commander_object"),
              (assign, ":commander_object", ":besieger_enemy"),
            (else_try),
              (party_slot_eq, ":commander_party", slot_party_ai_state, spai_engaging_army), #if commander is engaging an army
              (party_get_slot, ":commander_object", ":commander_party", slot_party_ai_object), #get commander's ai object (army which they engaded)
              (ge, ":commander_object", 0), #if commander has an object
              (neg|is_between, ":commander_object", centers_begin, centers_end), #if this object is not a center, so it is a party
              (party_is_active, ":commander_object"),
              (party_get_battle_opponent, ":besieged_center", ":commander_object"), #get this object's battle opponent
            (else_try),
              (assign, ":besieged_center", -1),
            (try_end),
            
            (is_between, ":besieged_center", walled_centers_begin, walled_centers_end), #if battle opponent of our commander's ai object is a walled center
            
            (party_get_attached_to, ":attached_to_party", ":commander_party"), #if commander is attached to besieged center already.
            (eq, ":attached_to_party", ":besieged_center"),
            
            (store_faction_of_party, ":besieged_center_faction", ":besieged_center"),#get (battle opponent of our commander's ai object)'s faction
            (eq, ":besieged_center_faction", ":faction_no"), #if battle opponent of our commander's ai object is from same faction with current party
            (party_is_active, ":commander_object"), ##1.132, new line
            #make also follow_or_not check if needed
            
            (call_script, "script_party_set_ai_state", ":party_no", spai_engaging_army, ":commander_object"), #go and help commander
            
            (try_begin),
              (eq, "$cheat_mode", 1),
              (str_store_party_name, s7, ":party_no"),
              (str_store_party_name, s6, ":commander_object"),
              (display_message, "@{!}DEBUG : {s7} is helping his commander by fighting with {s6}."),
            (try_end),
          (else_try),
            #(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_center),
            
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
            (party_get_slot, ":commander_party", ":party_no", slot_party_ai_object),
            (gt, ":commander_party", 0),
            (party_is_active, ":commander_party"),
            
            (party_get_battle_opponent, ":besieged_center", ":commander_party"), #get this object's battle opponent
            
            #make also follow_or_not check if needed
            
            (is_between, ":besieged_center", walled_centers_begin, walled_centers_end), #if this object is a center
            (party_get_attached_to, ":attached_to_party", ":party_no"),
            (neq, ":attached_to_party", ":besieged_center"),
            (party_is_active, ":besieged_center"), ##1.132, new line
            
            (call_script, "script_party_set_ai_state", ":party_no", spai_engaging_army, ":besieged_center"), #go and help commander
            
            #(try_begin),
            #  (eq, "$cheat_mode", 1),
            #  (str_store_party_name, s7, ":party_no"),
            #  (str_store_party_name, s6, ":besieged_center"),
            #  (display_message, "@{!}DEBUG : {s7} is helping his commander by attacking {s6}."),
            #(try_end),
            
            #(party_set_ai_behavior, ":party_no", ai_bhvr_attack_party),
            #(party_set_ai_object, ":party_no", ":besieged_center"),
            #(party_set_flags, ":party_no", pf_default_behavior, 1), #is these needed?
            #(party_set_slot, ":party_no", slot_party_ai_substate, 1), #is these needed?
          (try_end),
        (try_end),
    ]),
    
    # script_party_set_ai_state
    # Input: arg1 = party_no, arg2 = new_ai_state, arg3 = action_object (if necessary)
    # Output: none (Can fail)
    
    #Redone somewhat on Feb 18 to make sure that initative is set properly
    
    ("party_set_ai_state",
      [
        (store_script_param, ":party_no", 1),
        (store_script_param, ":new_ai_state", 2),
        (store_script_param, ":new_ai_object", 3),
        
        (party_get_slot, ":old_ai_state", ":party_no", slot_party_ai_state),
        (party_get_slot, ":old_ai_object", ":party_no", slot_party_ai_object),
        (party_get_attached_to, ":attached_to_party", ":party_no"),
        (assign, ":party_is_in_town", 0),
        (try_begin),
          (is_between, ":attached_to_party", centers_begin, centers_end),
          (assign, ":party_is_in_town", ":attached_to_party"),
        (try_end),
        
        (assign, ":commander", -1),
        (try_begin),
          (party_is_active, ":party_no"),
          (party_stack_get_troop_id, ":commander", ":party_no", 0),
          (store_faction_of_party, ":faction_no", ":party_no"),
        (try_end),
        
        (try_begin),
          (lt, ":commander", 0),
          #sometimes 0 sized parties enter "party_set_ai_state" script. So only discard them
          #(try_begin),
          #  (eq, "$cheat_mode", 1),
          #  (str_store_troop_name, s6, ":party_no"),
          #  (party_get_num_companions, reg6, ":party_no"),
          #  (display_message, "@{!}DEBUGS : party name is : {s6}, party size is : {reg6}, new ai discarded."),
          #(try_end),
        (else_try),
          #Party does any business in town
          (try_begin),
            (is_between, ":party_is_in_town", walled_centers_begin, walled_centers_end),
            (party_slot_eq, ":party_is_in_town", slot_center_is_besieged_by, -1),
            (call_script, "script_troop_does_business_in_center", ":commander", ":party_is_in_town"),
          (else_try),
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_visiting_village),
            (party_get_slot, ":party_is_in_village", ":party_no", slot_party_ai_object),
            (is_between, ":party_is_in_village", villages_begin, villages_end),
            #(party_slot_eq, ":party_is_in_village", slot_center_is_looted_by, -1),
            (neg|party_slot_eq, ":party_is_in_village", slot_village_state, svs_being_raided),
            (neg|party_slot_eq, ":party_is_in_village", slot_village_state, svs_looted),
            (store_distance_to_party_from_party, ":distance", ":party_no", ":party_is_in_village"),
            (lt, ":distance", 3),
            (call_script, "script_troop_does_business_in_center", ":commander", ":party_is_in_village"),
          (try_end),
          
          (party_set_slot, ":party_no", slot_party_follow_me, 0),
          
          (try_begin),
            (eq, ":old_ai_state", ":new_ai_state"),
            (eq, ":old_ai_object", ":new_ai_object"),
            #do nothing. Nothing is changed.
          (else_try),
            (assign, ":initiative", 100),
            (assign, ":aggressiveness", 8),
            (assign, ":courage", 8),
            
            (try_begin),
              (this_or_next|eq, ":new_ai_state", spai_accompanying_army),
              (eq, ":new_ai_state", spai_screening_army),
              
              (party_set_ai_behavior, ":party_no", ai_bhvr_escort_party),
              (party_set_ai_object, ":party_no", ":new_ai_object"),
              (party_set_flags, ":party_no", pf_default_behavior, 0),
              
              (try_begin),
                (gt, ":party_is_in_town", 0),
                (party_detach, ":party_no"),
              (try_end),
              
              (try_begin),
                (eq, ":new_ai_state", spai_screening_army),
                (assign, ":aggressiveness", 9),
                (assign, ":courage", 9),
                (assign, ":initiative", 80),
              (else_try),
                (assign, ":aggressiveness", 6),
                (assign, ":courage", 9),
                (assign, ":initiative", 10),
              (try_end),
            (else_try),
              (eq, ":new_ai_state", spai_besieging_center),
              
              (party_get_position, pos1, ":new_ai_object"),
              (map_get_random_position_around_position, pos2, pos1, 2),
              (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_point),
              (party_set_ai_target_position, ":party_no", pos2),
              (party_set_ai_object, ":party_no", ":new_ai_object"),
              (party_set_flags, ":party_no", pf_default_behavior, 0),
              (party_set_slot, ":party_no", slot_party_follow_me, 1),
              (party_set_slot, ":party_no", slot_party_ai_substate, 0),
              
              (try_begin),
                (gt, ":party_is_in_town", 0),
                (neq, ":party_is_in_town", ":new_ai_object"),
                (party_detach, ":party_no"),
              (try_end),
              
              (assign, ":aggressiveness", 1),
              (assign, ":courage", 9),
              (assign, ":initiative", 20),
              #(assign, ":initiative", 100),
            (else_try),
              (eq, ":new_ai_state", spai_holding_center),
              
              (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
              (party_set_ai_object, ":party_no", ":new_ai_object"),
              (party_set_flags, ":party_no", pf_default_behavior, 0),
              
              (try_begin),
                (gt, ":party_is_in_town", 0),
                (neq, ":party_is_in_town", ":new_ai_object"),
                (party_detach, ":party_no"),
              (try_end),
              
              (assign, ":aggressiveness", 7),
              (assign, ":courage", 9),
              (assign, ":initiative", 100),
              #(party_set_ai_initiative, ":party_no", 99),
            (else_try),
              (eq, ":new_ai_state", spai_patrolling_around_center),
              (party_get_position, pos1, ":new_ai_object"),
              (map_get_random_position_around_position, pos2, pos1, 1),
              (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_point),
              (party_set_ai_target_position, ":party_no", pos2),
              (party_set_ai_object, ":party_no", ":new_ai_object"),
              
              (try_begin),
                (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemies_around_center),
                (party_set_ai_patrol_radius, ":party_no", 1), #line 100
              (else_try),
                (party_set_ai_patrol_radius, ":party_no", 5), #line 100
              (try_end),
              
              (party_set_flags, ":party_no", pf_default_behavior, 0),
              (party_set_slot, ":party_no", slot_party_follow_me, 1),
              (party_set_slot, ":party_no", slot_party_ai_substate, 0),
              
              (try_begin),
                (gt, ":party_is_in_town", 0),
                (party_detach, ":party_no"),
              (try_end),
              
              (try_begin),
                #new to avoid losing time of marshal with attacking unimportant targets while there is a threat in our centers.
                (ge, ":commander", 0),
                (faction_slot_eq, ":faction_no", slot_faction_marshall, ":commander"),
                (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemies_around_center),
                
                (party_get_position, pos3, ":party_no"),
                (get_distance_between_positions, ":distance_to_center", pos1, pos3),
                
                (try_begin),
                  (ge, ":distance_to_center", 800), #added new (1.122)
                  (assign, ":initiative", 10),
                  (assign, ":aggressiveness", 1),
                  (assign, ":courage", 8),
                (else_try), #below added new (1.122)
                  (assign, ":initiative", 100),
                  (assign, ":aggressiveness", 8),
                  (assign, ":courage", 8),
                (try_end),
              (else_try),
                (assign, ":aggressiveness", 8),
                (assign, ":courage", 8),
                (assign, ":initiative", 100),
              (try_end),
            (else_try),
              (eq, ":new_ai_state", spai_visiting_village),
              (party_get_position, pos1, ":new_ai_object"),
              (map_get_random_position_around_position, pos2, pos1, 2),
              (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_point),
              (party_set_ai_target_position, ":party_no", pos2),
              (party_set_ai_object, ":party_no", ":new_ai_object"),
              (party_set_flags, ":party_no", pf_default_behavior, 0),
              (party_set_slot, ":party_no", slot_party_ai_substate, 0),
              (try_begin),
                (gt, ":party_is_in_town", 0),
                (neq, ":party_is_in_town", ":new_ai_object"),
                (party_detach, ":party_no"),
              (try_end),
              
              (assign, ":aggressiveness", 8),
              (assign, ":courage", 8),
              (assign, ":initiative", 100),
            (else_try), #0.660: this is where the 1625/1640 bugs happen with an improper ai_object
              (eq, ":new_ai_state", spai_raiding_around_center),
              (party_get_position, pos1, ":new_ai_object"),
              (map_get_random_position_around_position, pos2, pos1, 1),
              (party_set_ai_behavior, ":party_no", ai_bhvr_patrol_location),
              (party_set_ai_patrol_radius, ":party_no", 10),
              (party_set_ai_target_position, ":party_no", pos2),
              (party_set_ai_object, ":party_no", ":new_ai_object"),
              (party_set_flags, ":party_no", pf_default_behavior, 0),
              (party_set_slot, ":party_no", slot_party_follow_me, 1),
              (party_set_slot, ":party_no", slot_party_ai_substate, 0),
              (try_begin),
                (gt, ":party_is_in_town", 0),
                (neq, ":party_is_in_town", ":new_ai_object"),
                (party_detach, ":party_no"),
              (try_end),
              
              (try_begin),
                (ge, ":commander", 0),
                (faction_slot_eq, ":faction_no", slot_faction_marshall, ":commander"),
                (assign, ":aggressiveness", 1),
                (assign, ":courage", 8),
                (assign, ":initiative", 20),
              (else_try),
                (assign, ":aggressiveness", 7),
                (assign, ":courage", 8),
                (assign, ":initiative", 100),
              (try_end),
            (else_try),
              (eq, ":new_ai_state", spai_engaging_army),
              
              (party_set_ai_behavior, ":party_no", ai_bhvr_attack_party),
              (party_set_ai_object, ":party_no", ":new_ai_object"),
              (party_set_flags, ":party_no", pf_default_behavior, 0),
              (try_begin),
                (gt, ":party_is_in_town", 0),
                (party_detach, ":party_no"),
              (try_end),
              
              (try_begin),
                #new to avoid losing time of marshal with attacking unimportant targets while there is a threat in our centers.
                (ge, ":commander", 0),
                (faction_slot_eq, ":faction_no", slot_faction_marshall, ":commander"),
                (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemies_around_center),
                (assign, ":initiative", 10),
                (assign, ":aggressiveness", 1),
                (assign, ":courage", 8),
              (else_try),
                (assign, ":aggressiveness", 8),
                (assign, ":courage", 8),
                (assign, ":initiative", 100),
              (try_end),
            (else_try),
              (eq, ":new_ai_state", spai_retreating_to_center),
              (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
              (party_set_ai_object, ":party_no", ":new_ai_object"),
              (party_set_flags, ":party_no", pf_default_behavior, 1),
              (party_set_slot, ":party_no", slot_party_commander_party, -1),
              (try_begin),
                (gt, ":party_is_in_town", 0),
                (neq, ":party_is_in_town", ":new_ai_object"),
                (party_detach, ":party_no"),
              (try_end),
              
              (assign, ":aggressiveness", 3),
              (assign, ":courage", 4),
              (assign, ":initiative", 100),
            (else_try),
              (eq, ":new_ai_state", spai_undefined),
              (party_set_ai_behavior, ":party_no", ai_bhvr_hold),
              (party_set_flags, ":party_no", pf_default_behavior, 0),
            (try_end),
            
            (try_begin),
              (troop_slot_eq, ":commander", slot_lord_reputation_type, lrep_martial),
              (val_add, ":aggressiveness", 2),
              (val_add, ":courage", 2),
            (else_try),
			  ##diplomacy start+ support lady personality types
			  (neg|troop_slot_eq, ":commander", slot_lord_reputation_type, lrep_adventurous),
			  (this_or_next|troop_slot_ge, ":commander", slot_lord_reputation_type, dplmc_lrep_ladies_begin),
			  ##diplomacy end+
              (troop_slot_eq, ":commander", slot_lord_reputation_type, lrep_debauched),
              (val_sub, ":aggressiveness", 1),
              (val_sub, ":courage", 1),
            (try_end),
            
            (party_set_slot, ":party_no", slot_party_ai_state, ":new_ai_state"),
            (party_set_slot, ":party_no", slot_party_ai_object, ":new_ai_object"),
            (party_set_aggressiveness, ":party_no", ":aggressiveness"),
            (party_set_courage, ":party_no", ":courage"),
            (party_set_ai_initiative, ":party_no", ":initiative"),
          (try_end),
        (try_end),
        
        #Helpfulness
        (try_begin),
          (ge, ":commander", 0),
          
          (party_set_helpfulness, ":party_no", 101),
          (try_begin),
            (troop_slot_eq, ":commander", slot_lord_reputation_type, lrep_martial),
            (party_set_helpfulness, ":party_no", 200),
          (else_try),
            (troop_slot_eq, ":commander", slot_lord_reputation_type, lrep_upstanding),
            (party_set_helpfulness, ":party_no", 150),
          (else_try),
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
            (party_set_helpfulness, ":party_no", 110),
          (else_try),
            (troop_slot_eq, ":commander", slot_lord_reputation_type, lrep_quarrelsome),
            (party_set_helpfulness, ":party_no", 90),
          (else_try),
            (troop_slot_eq, ":commander", slot_lord_reputation_type, lrep_selfrighteous),
            (party_set_helpfulness, ":party_no", 80),
          (else_try),
            (troop_slot_eq, ":commander", slot_lord_reputation_type, lrep_debauched),
            (party_set_helpfulness, ":party_no", 50),
          (try_end),
        (try_end),
    ]),
    
    ("cf_party_under_player_suggestion",
      [
        (store_script_param, ":party_no", 1),
        
        (party_slot_eq, ":party_no", slot_party_following_orders_of_troop, "trp_kingdom_heroes_including_player_begin"),
        
        (party_get_slot, ":ai_state", ":party_no", slot_party_ai_state),
        (party_slot_eq, ":party_no", slot_party_orders_type, ":ai_state"),
        
        (party_get_slot, ":ai_object", ":party_no", slot_party_ai_object),
        (party_slot_eq, ":party_no", slot_party_orders_object, ":ai_object"),
        
        (store_current_hours, ":hours_since_orders_given"),
        (party_get_slot, ":orders_time", ":party_no", slot_party_orders_time),
        
        (val_sub, ":hours_since_orders_given", ":orders_time"),
        (lt, ":hours_since_orders_given", 12),
    ]),
    
    #Currently called from process_ai_state, could be called from elsewhere
    #It is used for lord to (1)Court ladies (2)Collect rents (3)Look for volunteers
    ("troop_does_business_in_center",
      [
		(store_script_param, ":troop_no", 1),
		(store_script_param, ":center_no", 2),
		##diplomacy start+
		#Call this once and reuse below.
		(call_script, "script_dplmc_is_affiliated_family_member", ":troop_no"),
		(assign, ":is_affiliated", reg0),
		#Also enable for the spouse, unless you're on bad terms
		(try_begin),
			(lt, ":is_affiliated", 0),
			(this_or_next|troop_slot_eq,":troop_no",slot_troop_spouse, "trp_player"),
				(troop_slot_eq,"trp_player",slot_troop_spouse, ":troop_no"),
			(call_script, "script_troop_get_player_relation", ":troop_no"),
			(store_skill_level, ":persuasion", "skl_persuasion", "trp_player"),
			(val_add, reg0, ":persuasion"),
			#reduce magnitude, since >= 0 succeeds
			(store_sub, ":persuasion_modifier", 20, ":persuasion"),
			(val_mul, reg0, ":persuasion_modifier"),
			(val_div, reg0, 20),
			#final number must be >= -5
			(ge, reg0, -5),
			(assign, ":is_affiliated", 1),
		(try_end),
		##diplomacy end+
        
        (troop_get_slot, ":led_party", ":troop_no", slot_troop_leaded_party),
        
        (store_current_hours, ":current_time"),
        (try_begin),
          #     (party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),##Floris: by nullifying this line, heroes without a fief will act normally. Thanks to Caba`drin for this fix. It was also officially fixed in version 1.132.
          (is_between, ":center_no", walled_centers_begin, walled_centers_end),
          (party_set_slot, ":led_party", slot_party_last_in_any_center, ":current_time"),
          (try_begin),
            (call_script, "script_lord_get_home_center", ":troop_no"),
            (eq, ":center_no", reg0),
            (party_set_slot, ":led_party", slot_party_last_in_home_center, ":current_time"),
          (try_end),
        (try_end),
        
        #Collect the rents
        (try_begin),
          (party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
          
          (party_get_slot, ":accumulated_rents", ":center_no", slot_center_accumulated_rents),
          (party_get_slot, ":accumulated_tariffs", ":center_no", slot_center_accumulated_tariffs),
          (troop_get_slot, ":troop_wealth", ":troop_no", slot_troop_wealth),
          (val_add, ":troop_wealth", ":accumulated_rents"),
          (val_add, ":troop_wealth", ":accumulated_tariffs"),
          
          (troop_set_slot, ":troop_no", slot_troop_wealth, ":troop_wealth"),
          (party_set_slot, ":center_no", slot_center_accumulated_rents, 0),
          (party_set_slot, ":center_no", slot_center_accumulated_tariffs, 0),
          
		  ##diplomacy start+
		  #Modify the next block to display for affiliates
		  (try_begin),
			(this_or_next|ge, ":is_affiliated", 1),#<-- dplmc+ added
			(this_or_next|eq, "$cheat_mode", 1),
			(eq, "$cheat_mode", 3),
			(assign, reg1, ":troop_wealth"),
			(str_store_party_name, s4, ":center_no"),
			(add_troop_note_from_sreg, ":troop_no", 1, "str_current_wealth_reg1_taxes_last_collected_from_s4", 0),
			#New section, print a message for affiliates:
			(ge, ":is_affiliated", 1),
			(store_add, reg0, ":accumulated_rents", ":accumulated_tariffs"),
			(str_store_troop_name, s0, ":troop_no"),
			(try_begin),
			   (gt, reg0, 0),
			   (display_message, "@{s0} collects {reg0} denars from {s4}, current wealth: {reg1} denars"),
			(try_end),
		  (try_end),
		  ##diplomacy end+
		(try_end),
        
        #Recruit volunteers
        (try_begin),
          (is_between, ":center_no", villages_begin, villages_end),
          
          (party_get_slot, ":troop_type", ":center_no", slot_center_npc_volunteer_troop_type),
          (party_get_slot, ":troop_amount", ":center_no", slot_center_npc_volunteer_troop_amount),
          (party_set_slot, ":center_no", slot_center_npc_volunteer_troop_amount, -1),
          ##diplomacy begin
          (try_begin),
            (store_faction_of_party, ":party_faction", ":led_party"),
            (eq, ":party_faction", "fac_player_supporters_faction"),
            (is_between, "$g_player_culture", npc_kingdoms_begin, npc_kingdoms_end),
            (faction_get_slot, ":troop_type", "$g_player_culture", slot_faction_tier_1_troop),
          (try_end),
          
        (try_begin), #debug
          (eq, "$cheat_mode", 1),
		  ##nested diplomacy start+
		  (this_or_next|ge, ":is_affiliated", 1),#<- Show for affiliates
		  ##nested diplomacy end+
          (assign, reg2, ":troop_amount"),
          (str_store_string, s11, "@{reg2}"),
          (str_store_troop_name, s12, ":troop_type"),
          (str_store_faction_name, s13, ":party_faction"),
          (str_store_party_name, s14, ":center_no"),
          (str_store_party_name, s10, ":led_party"),
          (display_message, "@ {s10} of {s13} recruits {s11} {s12} in {s14}"),
        (try_end),
        ##diplomacy end
        (party_add_members, ":led_party", ":troop_type", ":troop_amount"),
    (try_end),

        
        #Courtship
        (try_begin),
          (party_get_slot, ":time_of_last_courtship", ":led_party", slot_party_leader_last_courted),
          (store_sub, ":hours_since_last_courtship", ":current_time", ":time_of_last_courtship"),
          (gt, ":hours_since_last_courtship", 72),
          
          (troop_slot_eq, ":troop_no", slot_troop_spouse, -1),
			##diplomacy start+ Disable this for inappropriate types
			(neg|is_between, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),#They use the last visited slots for other purposes
			(neg|is_between, ":troop_no", kings_begin, kings_end),#They should not be participating in this system
			(neg|is_between, ":troop_no", pretenders_begin, pretenders_end),#They should not be participating in this system
			##diplomacy end+		  
          (try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
            (troop_get_slot, ":love_interest", ":troop_no", ":love_interest_slot"),
            (gt, ":love_interest", 0),
            (troop_get_slot, ":love_interest_town", ":love_interest", slot_troop_cur_center),
            (eq, ":center_no", ":love_interest_town"),
            
            (call_script, "script_courtship_event_troop_court_lady", ":troop_no", ":love_interest"),
            (party_set_slot, ":led_party", slot_party_leader_last_courted, ":current_time"),
          (try_end),
        (try_end),
    ]),
    
    # script_process_kingdom_parties_ai
    # This is called more frequently than decide_kingdom_parties_ai
    # Input: none
    # Output: none
    #called from triggers
  ("process_kingdom_parties_ai",
    [
		##diplomacy start+ add support for promoted kingdom ladies
       (try_for_range, ":troop_no", heroes_begin, heroes_end),#<- change active_npcs to heroes
	   ##diplomacy end+
         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
         (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
         (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
         (gt, ":party_no", 0),
         (call_script, "script_process_hero_ai", ":troop_no"),
       (try_end),
  ]),
    
		# script_process_hero_ai
		# This is called more frequently than script_decide_kingdom_party_ais
		#Handles sieges, raids, etc -- does not change the party's basic mission.
		# Input: none
		# Output: none
		#called from triggers
	  ("process_hero_ai",
		[
		  (store_script_param_1, ":troop_no"),
		  (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
		  (try_begin),
			(party_is_active, ":party_no"),
			(store_faction_of_party, ":faction_no", ":party_no"),
			(party_get_slot, ":ai_state", ":party_no", slot_party_ai_state),
			(party_get_slot, ":ai_object", ":party_no", slot_party_ai_object),
			(try_begin),
			  (eq, ":ai_state", spai_besieging_center),
			  (try_begin),
				(party_slot_eq, ":ai_object", slot_center_is_besieged_by, -1),
				(store_distance_to_party_from_party, ":distance", ":party_no", ":ai_object"),
				(lt, ":distance", 3),
				(try_begin),
				  (party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
				  (party_get_slot, ":commander_party", ":party_no", slot_party_ai_object),
				  (party_set_slot, ":ai_object", slot_center_is_besieged_by, ":commander_party"),
				(else_try),
				  (party_set_slot, ":ai_object", slot_center_is_besieged_by, ":party_no"),
				(try_end),
				(store_current_hours, ":cur_hours"),
				(party_set_slot, ":ai_object", slot_center_siege_begin_hours, ":cur_hours"),

				(str_store_party_name_link, s1, ":ai_object"),
				(str_store_troop_name_link, s2, ":troop_no"),
				(str_store_faction_name_link, s3, ":faction_no"),
				(display_log_message, "@{s1} has been besieged by {s2} of the {s3}."),
				(try_begin),
				  (store_faction_of_party, ":ai_object_faction", ":ai_object"),
					 ##diplomacy start+ Handle player is co-ruler of faction
					 (assign, ":is_coruler", 0),
					 (try_begin),
						(eq, ":ai_object_faction", "$players_kingdom"),
						(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
						(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
						(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
						(assign, ":is_coruler", 1),
					 (try_end),
					 (this_or_next|eq, ":is_coruler", 1),
					 ##diplomacy end+
				  (this_or_next|party_slot_eq, ":ai_object", slot_town_lord, "trp_player"),
				  (eq, ":ai_object_faction", "fac_player_supporters_faction"),
				  (call_script, "script_add_notification_menu", "mnu_notification_center_under_siege", ":ai_object", ":troop_no"),
				(try_end),
				(call_script, "script_village_set_state", ":ai_object", svs_under_siege),
				(assign, "$g_recalculate_ais", 1),
			  (try_end),
			(else_try),
			  (eq, ":ai_state", spai_raiding_around_center),
			  (party_slot_eq, ":party_no", slot_party_ai_substate, 0),
			  (assign, ":selected_village", 0),
			  (try_for_range, ":enemy_village_no", villages_begin, villages_end),
				(eq, ":selected_village", 0),
				(store_faction_of_party, ":enemy_village_faction", ":enemy_village_no"),
				(try_begin),
				  (party_slot_eq, ":enemy_village_no", slot_town_lord, "trp_player"),
				  (store_relation, ":reln", "fac_player_supporters_faction", ":faction_no"),
				(else_try),
				  (store_relation, ":reln", ":enemy_village_faction", ":faction_no"),
				(try_end),
				(lt, ":reln", 0),
				(store_distance_to_party_from_party, ":dist", ":enemy_village_no", ":party_no"),
				(lt, ":dist", 15),
				(party_slot_eq, ":enemy_village_no", slot_village_state, 0), #village is not already raided
				#CHANGE STATE TO RAID THIS VILLAGE
				(assign, ":selected_village", ":enemy_village_no"),
			  (try_end),
			  (try_begin),
				(eq, ":selected_village", 0),
				(is_between, ":ai_object", villages_begin, villages_end),
				(assign, ":selected_village", ":ai_object"),
			  (try_end),
			  (try_begin),
				(gt, ":selected_village", 0),
				(call_script, "script_party_set_ai_state", ":party_no", spai_raiding_around_center, ":selected_village"),
				(try_begin),
				  (faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
				  (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_raiding_village),
				  (faction_set_slot, ":faction_no", slot_faction_ai_object, ":selected_village"),
				(try_end),
				(party_get_position, pos1, ":selected_village"),
				(map_get_random_position_around_position, pos2, pos1, 1),
				(party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_point),
				(party_set_ai_target_position, ":party_no", pos2),
				(party_set_ai_object, ":party_no", ":selected_village"),
				(party_set_slot, ":party_no", slot_party_ai_substate, 1),
			  (try_end),
			(else_try),
			  (eq, ":ai_state", spai_raiding_around_center),#substate is 1
			  (try_begin),
				(store_distance_to_party_from_party, ":distance", ":party_no", ":ai_object"),
				(lt, ":distance", 2),
				(try_begin),
				  (party_slot_eq, ":ai_object", slot_village_state, 0),
				  (call_script, "script_village_set_state", ":ai_object", svs_being_raided),
				  (party_set_slot, ":ai_object", slot_village_raided_by, ":party_no"),
				  (try_begin),
					(store_faction_of_party, ":village_faction", ":ai_object"),
					 ##diplomacy start+ Handle player is co-ruler of faction
					 (assign, ":is_coruler", 0),
					 (try_begin),
						(eq, ":village_faction", "$players_kingdom"),
						(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
						(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
						(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
						(assign, ":is_coruler", 1),
					 (try_end),
					 (this_or_next|eq, ":is_coruler", 1),
					 ##diplomacy end+
					(this_or_next|party_slot_eq, ":ai_object", slot_town_lord, "trp_player"),
					(eq, ":village_faction", "fac_player_supporters_faction"),
					(store_distance_to_party_from_party, ":dist", "p_main_party", ":ai_object"),
					(this_or_next|lt, ":dist", 30),
					(party_slot_eq, ":ai_object", slot_center_has_messenger_post, 1),
					(call_script, "script_add_notification_menu", "mnu_notification_village_raid_started", ":ai_object", ":troop_no"),
				  (try_end),
				(else_try),
				  (party_slot_eq, ":ai_object", slot_village_state, svs_being_raided),
				(else_try),
				  #if anything other than being_raided leave
				  (party_set_slot, ":party_no", slot_party_ai_substate, 0),
				(try_end),
			  (try_end),
			(else_try),
			  (eq, ":ai_state", spai_retreating_to_center),
			  (try_begin),
				(party_get_battle_opponent, ":enemy_party", ":party_no"),
				(ge, ":enemy_party", 0), #we are in a battle! we may be caught in a loop!
				(call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
				(party_set_flags, ":party_no", pf_default_behavior, 0),
				(party_set_slot, ":party_no", slot_party_commander_party, -1),
			  (try_end),
			(else_try),
			  (eq, ":ai_state", spai_patrolling_around_center),

			  (try_begin),
				(party_slot_eq, ":party_no", slot_party_ai_substate, 0),
				(store_distance_to_party_from_party, ":distance", ":party_no", ":ai_object"),
				(lt, ":distance", 6),
				(party_set_slot, ":party_no", slot_party_ai_substate, 1),

				(party_set_aggressiveness, ":party_no", 8),
				(party_set_courage, ":party_no", 8),
				(party_set_ai_initiative, ":party_no", 100),

				(party_set_ai_behavior, ":party_no", ai_bhvr_patrol_party),
				(party_set_ai_object, ":party_no", ":ai_object"),
			  (try_end),
			(else_try),
			  (eq, ":ai_state", spai_holding_center),
			(try_end),
		  (try_end),
	  ]),
    
    # script_begin_assault_on_center
    # Input: arg1: faction_no
    # Output: none
    #called from triggers
    ("begin_assault_on_center",
      [
     (store_script_param, ":center_no", 1),
	 ##diplomacy start+ add support for promoted kingdom ladies
     (try_for_range, ":troop_no", heroes_begin, heroes_end),#<- change active_npcs to heroes
	 ##diplomacy end+
       (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
       (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
       (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
       (gt, ":party_no", 0),
       (party_is_active, ":party_no"),
          
          (assign, ":continue", 0),
          (try_begin),
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
            (party_slot_eq, ":party_no", slot_party_ai_object, ":center_no"),
            (party_slot_eq, ":party_no", slot_party_ai_substate, 0),
            (assign, ":continue", 1),
          (else_try),
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
            (party_get_slot, ":commander_party", ":party_no", slot_party_ai_object),
            (gt, ":commander_party", 0),
            (party_is_active, ":commander_party"),
            (party_slot_eq, ":commander_party", slot_party_ai_state, spai_besieging_center),
            (party_slot_eq, ":commander_party", slot_party_ai_object, ":center_no"),
            (call_script, "script_party_set_ai_state", ":party_no", spai_besieging_center, ":center_no"),
            (assign, ":continue", 1),
          (try_end),
          
          (eq, ":continue", 1),
          
          (party_set_ai_behavior, ":party_no", ai_bhvr_attack_party),
          (party_set_ai_object, ":party_no", ":center_no"),
          (party_set_flags, ":party_no", pf_default_behavior, 1),
          (party_set_slot, ":party_no", slot_party_ai_substate, 1),
        (try_end),
    ]),
    
    #DEPRECATED - Using new political issue system instead
    ("select_faction_marshall",
      [
        #     (store_script_param_1, ":faction_no"),
        #    (faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
        #   (faction_get_slot, ":old_faction_marshall", ":faction_no", slot_faction_marshall),
        
        #  (assign, ":old_marshal_is_avaliable", 0),
        # (try_begin),
        #  (gt, ":old_faction_marshall", 0),
        # (troop_get_slot, ":old_marshal_party", ":old_faction_marshall", slot_troop_leaded_party),
        #  (party_is_active, ":old_marshal_party"),
        #   (assign, ":old_marshal_is_avaliable", 1),
        #  (try_end),
        
        #Ozan : I am adding some codes here because sometimes armies demobilize during last seconds of an
        #important event like taking a castle, ext because of marshal change. When marshal changes during
        #an important event occurs new marshal's followers become 0 and continueing siege attack seems less
        #valuable then armies demobilize, faction ai become "do nothing", "I cannot think anything to do" ext.
        
        #  (assign, ":there_is_an_important_situation", 0),
        #  (faction_get_slot, ":current_ai_object", ":faction_no", slot_faction_ai_object),
        
        #  (try_begin), #do not demobilize during taking a castle/town (fighting in the castle)
        #    (is_between, ":current_ai_object", walled_centers_begin, walled_centers_end),
        #    (party_get_battle_opponent, ":besieger_party", ":current_ai_object"),
        #    (ge, ":besieger_party", 0),
        #    (party_is_active, ":besieger_party"),
        #    (store_faction_of_party, ":besieger_faction", ":besieger_party"),
        #    (this_or_next|eq, ":besieger_faction", ":faction_no"),
        #    (eq, ":besieger_faction", "fac_player_faction"),
        #    (assign, ":there_is_an_important_situation", 1),
        #  (try_end),
        
        #  (try_begin), #do not demobilize during raiding a village (holding around village)
        #    (is_between, ":current_ai_object", centers_begin, centers_end),
        #    (neg|is_between, ":current_ai_object", walled_centers_begin, walled_centers_end),
        #    (party_slot_eq, ":current_ai_object", slot_village_state, svs_being_raided),
        #    (assign, ":there_is_an_important_situation", 1),
        #  (try_end),
        
        #  (try_begin), #do not demobilize during besigning a siege (holding around castle)
        #    (is_between, ":current_ai_object", walled_centers_begin, walled_centers_end),
        #    #(str_store_party_name, s7, ":current_ai_object"),
        #    (party_get_slot, ":besieger_party", ":current_ai_object", slot_center_is_besieged_by),
        #    (ge, ":besieger_party", 0),
        #    (party_is_active, ":besieger_party"),
        #    #(str_store_party_name, s7, ":besieger_party"),
        #    (store_faction_of_party, ":besieger_faction", ":besieger_party"),
        #    (this_or_next|eq, ":besieger_faction", ":faction_no"),
        #    (eq, ":besieger_faction", "fac_player_faction"),
        #    (assign, ":there_is_an_important_situation", 1),
        #  (try_end),
        
        #  (try_begin),
        #    (this_or_next|eq, ":there_is_an_important_situation", 0),
        #    (eq, ":old_marshal_is_avaliable", 0),
        #end addition ozan
        
        
        #   (assign, ":total_renown", 0),
        #   (try_for_range, ":loop_var", active_npcs_including_player_begin, active_npcs_end),
        #     (assign, ":cur_troop", ":loop_var"),
        #     (assign, ":continue", 0),
        #     (try_begin),
        #       (eq, ":loop_var", "trp_kingdom_heroes_including_player_begin"),
        #       (assign, ":cur_troop", "trp_player"),
        #       (try_begin),
        #         (eq, ":faction_no", "$players_kingdom"),
        #         (assign, ":continue", 1),
        #       (try_end),
        #     (else_try),
        #       (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
        #       (store_troop_faction, ":cur_faction", ":cur_troop"),
        #       (eq, ":cur_faction", ":faction_no"),
        #       (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
        #       (gt, ":cur_party", 0),
        #       (party_is_active, ":cur_party"),
        #       (call_script, "script_party_count_fit_for_battle", ":cur_party"),
        #       (assign, ":party_fit_for_battle", reg0),
        #       (call_script, "script_party_get_ideal_size", ":cur_party"),
        #       (assign, ":ideal_size", reg0),
        #       (store_mul, ":relative_strength", ":party_fit_for_battle", 100),
        #       (val_div, ":relative_strength", ":ideal_size"),
        #       (ge, ":relative_strength", 25),
        #       (assign, ":continue", 1),
        #     (try_end),
        
        #    (eq, ":continue", 1),
        
        #     (troop_get_slot, ":renown", ":cur_troop", slot_troop_renown),
        #     (call_script, "script_troop_get_relation_with_troop", ":cur_troop", ":faction_leader"),
        #     (store_mul, ":relation_modifier", reg0, 15),
        #     (val_add, ":renown", ":relation_modifier"),
        #     (val_max, ":renown", 1),
        #
        #     (try_begin),
        #       (eq, ":cur_troop", "trp_player"),
        #       (neq, ":old_faction_marshall", "trp_player"),
        #       (assign, ":renown", 0),
        #      (try_end),
        #     (try_begin),
        #       (eq, ":cur_troop", ":faction_leader"),
        #       (val_mul, ":renown", 3),
        #       (val_div, ":renown", 4),
        #     (try_end),
        #     (try_begin),
        #       (eq, ":cur_troop", ":old_faction_marshall"),
        #       (val_mul, ":renown", 1000),
        #     (try_end),
        #     (val_add, ":total_renown", ":renown"),
        #   (try_end),
        #   (assign, ":result", -1),
        #   (try_begin),
        #     (gt, ":total_renown", 0),
        #     (store_random_in_range, ":random_renown", 0, ":total_renown"),
        #     (try_for_range, ":loop_var", active_npcs_including_player_begin, active_npcs_end),
        #       (eq, ":result", -1),
        #       (assign, ":cur_troop", ":loop_var"),
        #       (assign, ":continue", 0),
        #       (try_begin),
        #         (eq, ":loop_var", "trp_kingdom_heroes_including_player_begin"),
        #         (assign, ":cur_troop", "trp_player"),
        #          (try_begin),
        #            (eq, ":faction_no", "$players_kingdom"),
        #            (assign, ":continue", 1),
        #          (try_end),
        #        (else_try),
        #          (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
        #          (store_troop_faction, ":cur_faction", ":cur_troop"),
        #          (eq, ":cur_faction", ":faction_no"),
        #          (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
        #          (gt, ":cur_party", 0),
        #          (party_is_active, ":cur_party"),
        #          (call_script, "script_party_count_fit_for_battle", ":cur_party"),
        #          (assign, ":party_fit_for_battle", reg0),
        #       (call_script, "script_party_get_ideal_size", ":cur_party"),
        #       (assign, ":ideal_size", reg0),
        #       (store_mul, ":relative_strength", ":party_fit_for_battle", 100),
        #       (val_div, ":relative_strength", ":ideal_size"),
        #       (ge, ":relative_strength", 25),
        #       (assign, ":continue", 1),
        #     (try_end),
        #     (eq, ":continue", 1),
        
        #   (troop_get_slot, ":renown", ":cur_troop", slot_troop_renown),
        #   (call_script, "script_troop_get_relation_with_troop", ":cur_troop", ":faction_leader"),
        #   (store_mul, ":relation_modifier", reg0, 15),
        #   (val_add, ":renown", ":relation_modifier"),
        #   (val_max, ":renown", 1),
        #
        #   (try_begin),
        #     (eq, ":cur_troop", "trp_player"),
        #     (neq, ":old_faction_marshall", "trp_player"),
        #     (assign, ":renown", 0),
        #   (try_end),
        #   (try_begin),
        #     (eq, ":cur_troop", ":faction_leader"),
        #     (val_mul, ":renown", 3),
        #    (val_div, ":renown", 4),
        #  (try_end),
        #  (try_begin),
        #      (eq, ":cur_troop", ":old_faction_marshall"),
        #      (val_mul, ":renown", 1000),
        #    (try_end),
        #    (val_sub, ":random_renown", ":renown"),
        #    (lt, ":random_renown", 0),
        #    (assign, ":result", ":cur_troop"),
        #  (try_end),
        # (try_end),
        # (try_begin),
        #(eq, "$cheat_mode", 1),
        # (ge, ":result", 0),
        #  (str_store_troop_name, s1, ":result"),
        #   (str_store_faction_name, s2, ":faction_no"),
        #    (display_message, "@{!}{s1} is chosen as the marshall of {s2}."),
        #   (try_end),
        #  (else_try),
        #    (faction_get_slot, ":old_faction_marshall", ":faction_no", slot_faction_marshall),
        #    (assign, ":result", ":old_faction_marshall"),
        #  (try_end),
        
        #  (assign, reg0, ":result"),
    ]),
    
    
    
    
    # script_get_center_faction_relation_including_player
    # Input: arg1: center_no, arg2: target_faction_no
    # Output: reg0: relation
    #called from triggers
    ("get_center_faction_relation_including_player",
      [
        (store_script_param, ":center_no", 1),
        (store_script_param, ":target_faction_no", 2),
        (store_faction_of_party, ":center_faction", ":center_no"),
        (store_relation, ":relation", ":center_faction", ":target_faction_no"),
        (try_begin),
          (party_slot_eq, ":center_no", slot_town_lord, "trp_player"),
          (store_relation, ":relation", "fac_player_supporters_faction", ":target_faction_no"),
        (try_end),
        (assign, reg0, ":relation"),
    ]),
    
    #script_update_report_to_army_quest_note
    ("update_report_to_army_quest_note",
      [
        (store_script_param, ":faction_no", 1),
        (store_script_param, ":new_strategy", 2),
        (store_script_param, ":old_faction_ai_state", 3),
        
        (try_begin),
          (le, "$number_of_report_to_army_quest_notes", 13),
          
          (faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
          
          (try_begin), #updating quest notes for only report to army quest
            (eq, ":faction_no", "$players_kingdom"),
            (neq, ":new_strategy", ":old_faction_ai_state"),
            (check_quest_active, "qst_report_to_army"),
            (ge, ":faction_marshal", 0), ##1.134
            
            (str_store_troop_name_link, s11, ":faction_marshal"),
            (store_current_hours, ":hours"),
            (call_script, "script_game_get_date_text", 0, ":hours"),
            
            (try_begin),
              (this_or_next|eq, ":new_strategy", sfai_attacking_enemies_around_center),
              (this_or_next|eq, ":new_strategy", sfai_attacking_center),
              (eq, ":new_strategy", sfai_gathering_army),
              (faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
              (ge, ":faction_object", 0),
              (str_store_party_name_link, s21, ":faction_object"),
            (try_end),
            
            (try_begin),
              (eq, ":new_strategy", sfai_gathering_army),
              
              (try_begin),
                (ge, "$g_gathering_reason", 0),
                (str_store_party_name_link, s21, "$g_gathering_reason"),
                (str_store_string, s14, "str_we_should_prepare_to_defend_s21_but_we_should_gather_our_forces_until_we_are_strong_enough_to_engage_them"),
              (else_try),
                (str_store_string, s14, "str_it_is_time_to_go_on_the_offensive_and_we_must_first_assemble_the_army"),
              (try_end),
              
              (str_store_string, s14, "@({s1}) {s11}: {s14}"),
              (add_quest_note_from_sreg, "qst_report_to_army", "$number_of_report_to_army_quest_notes", s14, 0),
              (val_add, "$number_of_report_to_army_quest_notes", 1),
            (else_try),
              (eq, ":new_strategy", sfai_attacking_enemies_around_center),
              
              (try_begin),
                (is_between, ":faction_object", walled_centers_begin, walled_centers_end),
                (str_store_string, s14, "str_we_should_ride_to_break_the_siege_of_s21"),
                (str_store_string, s14, "@({s1}) {s11}: {s14}"),
                (add_quest_note_from_sreg, "qst_report_to_army", "$number_of_report_to_army_quest_notes", s14, 0),
                (val_add, "$number_of_report_to_army_quest_notes", 1),
              (else_try),
                (is_between, ":faction_object", villages_begin, villages_end),
                (str_store_string, s14, "str_we_should_ride_to_defeat_the_enemy_gathered_near_s21"),
                (str_store_string, s14, "@({s1}) {s11}: {s14}"),
                (add_quest_note_from_sreg, "qst_report_to_army", "$number_of_report_to_army_quest_notes", s14, 0),
                (val_add, "$number_of_report_to_army_quest_notes", 1),
              (try_end),
            (else_try),
              (this_or_next|eq, ":new_strategy", sfai_attacking_center),
              (eq, ":new_strategy", sfai_raiding_village),
              
              (try_begin),
                (is_between, ":faction_object", walled_centers_begin, walled_centers_end),
                (str_store_string, s14, "str_we_believe_the_fortress_will_be_worth_the_effort_to_take_it"),
                (str_store_string, s14, "@{s14} ({s21})"),
                (str_store_string, s14, "@({s1}) {s11}: {s14}"),
                (add_quest_note_from_sreg, "qst_report_to_army", "$number_of_report_to_army_quest_notes", s14, 0),
                (val_add, "$number_of_report_to_army_quest_notes", 1),
              (else_try),
                (is_between, ":faction_object", villages_begin, villages_end),
                (str_store_string, s14, "str_we_shall_leave_a_fiery_trail_through_the_heart_of_the_enemys_lands_targeting_the_wealthy_settlements_if_we_can"),
                (str_store_string, s14, "@{s14} ({s21})"),
                (str_store_string, s14, "@({s1}) {s11}: {s14}"),
                (add_quest_note_from_sreg, "qst_report_to_army", "$number_of_report_to_army_quest_notes", s14, 0),
                (val_add, "$number_of_report_to_army_quest_notes", 1),
              (try_end),
            (try_end),
          (try_end),
        (try_end),
    ]),
]
