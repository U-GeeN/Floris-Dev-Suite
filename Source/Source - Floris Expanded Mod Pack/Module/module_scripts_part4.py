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

scripts_part4 = [

        
        # script_set_parties_around_player_ignore_player
        # Input: arg1 = ignore_range, arg2 = num_hours_to_ignore
        # Output: none
        ("set_parties_around_player_ignore_player",
          [(store_script_param, ":ignore_range", 1),
            (store_script_param, ":num_hours", 2),
            (try_for_parties, ":party_no"),
              (party_is_active, ":party_no"),
              (store_distance_to_party_from_party, ":dist", "p_main_party", ":party_no"),
              (lt, ":dist", ":ignore_range"),
              (party_ignore_player, ":party_no", ":num_hours"),
            (try_end),
        ]),
        
        # script_randomly_make_prisoner_heroes_escape_from_party
        # Input: arg1 = party_no, arg2 = escape_chance_mul_1000
        # Output: none
        ("randomly_make_prisoner_heroes_escape_from_party",
          [(store_script_param, ":party_no", 1),
            (store_script_param, ":escape_chance", 2),
            (assign, ":quest_troop_1", -1),
            (assign, ":quest_troop_2", -1),
            (try_begin),
              (check_quest_active, "qst_rescue_lord_by_replace"),
              (quest_get_slot, ":quest_troop_1", "qst_rescue_lord_by_replace", slot_quest_target_troop),
            (try_end),
            (try_begin),
              (check_quest_active, "qst_deliver_message_to_prisoner_lord"),
              (quest_get_slot, ":quest_troop_2", "qst_deliver_message_to_prisoner_lord", slot_quest_target_troop),
            (try_end),
            (party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
            (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
              (party_prisoner_stack_get_troop_id, ":stack_troop", ":party_no", ":i_stack"),
              (troop_is_hero, ":stack_troop"),
              (neq, ":stack_troop", ":quest_troop_1"),
              (neq, ":stack_troop", ":quest_troop_2"),
              (troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_kingdom_hero),
              (store_random_in_range, ":random_no", 0, 1000),
              (lt, ":random_no", ":escape_chance"),
              (party_remove_prisoners, ":party_no", ":stack_troop", 1),
              (call_script, "script_remove_troop_from_prison", ":stack_troop"),
              (str_store_troop_name_link, s1, ":stack_troop"),
              (try_begin),
                (eq, ":party_no", "p_main_party"),
                (str_store_string, s2, "@your party"),
              (else_try),
                (str_store_party_name, s2, ":party_no"),
              (try_end),
              (assign, reg0, 0),
              (try_begin),
                (this_or_next|eq, ":party_no", "p_main_party"),
                (party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
                (assign, reg0, 1),
              (try_end),
              (store_troop_faction, ":troop_faction", ":stack_troop"),
              (str_store_faction_name_link, s3, ":troop_faction"),
              (display_message, "@{reg0?One of your prisoners, :}{s1} of the {s3} has escaped from captivity!"), ##BUGFIX - Caba
            (try_end),
        ]),
        
        
        # script_fill_tournament_participants_troop
        # Input: arg1 = center_no, arg2 = player_at_center
        # Output: none (fills trp_tournament_participants)
        ("fill_tournament_participants_troop",
          [(store_script_param, ":center_no", 1),
            (store_script_param, ":player_at_center", 2),
            (assign, ":cur_slot", 0),
            
            (try_begin),
              (eq, ":player_at_center", 1),
              (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
              (try_for_range, ":stack_no", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":cur_troop", "p_main_party", ":stack_no"),
                (troop_is_hero, ":cur_troop"),
                (neq, ":cur_troop", "trp_kidnapped_girl"),
                (troop_set_slot, "trp_tournament_participants", ":cur_slot", ":cur_troop"),
                (val_add, ":cur_slot", 1),
              (try_end),
            (try_end),
            
            (party_collect_attachments_to_party, ":center_no", "p_temp_party"),
            (party_get_num_companion_stacks, ":num_stacks", "p_temp_party"),
            (try_for_range, ":stack_no", 0, ":num_stacks"),
              (party_stack_get_troop_id, ":cur_troop", "p_temp_party", ":stack_no"),
              (troop_is_hero, ":cur_troop"),
              (troop_set_slot, "trp_tournament_participants", ":cur_slot", ":cur_troop"),
              (val_add, ":cur_slot", 1),
            (try_end),
            
            (try_begin),
              (store_random_in_range, ":random_no", 0, 100),
              (lt, ":random_no", 50),
              (troop_set_slot, "trp_tournament_participants", ":cur_slot", "trp_xerina"),
              (val_add, ":cur_slot", 1),
            (try_end),
            (try_begin),
              (store_random_in_range, ":random_no", 0, 100),
              (lt, ":random_no", 50),
              (troop_set_slot, "trp_tournament_participants", ":cur_slot", "trp_dranton"),
              (val_add, ":cur_slot", 1),
            (try_end),
            (try_begin),
              (store_random_in_range, ":random_no", 0, 100),
              (lt, ":random_no", 50),
              (troop_set_slot, "trp_tournament_participants", ":cur_slot", "trp_kradus"),
              (val_add, ":cur_slot", 1),
            (try_end),

				##Floris MTT begin
            (assign, ":begin_slot", ":cur_slot"),
            (try_for_range, ":cur_slot", ":begin_slot", 64),
              (store_random_in_range, ":random_no", 0, 6),
              (try_begin),
                (eq, ":random_no", 0),
                (troop_set_slot, "trp_tournament_participants", ":cur_slot", "trp_regular_fighter"),
              (else_try),
                (eq, ":random_no", 1),
                (troop_set_slot, "trp_tournament_participants", ":cur_slot", "trp_veteran_fighter"),
              (else_try),
                (eq, ":random_no", 2),
                (troop_set_slot, "trp_tournament_participants", ":cur_slot", "trp_champion_fighter"),
              (else_try),
                (eq, ":random_no", 3),
				(troop_get_slot,":woman_black_widow","$troop_trees",slot_woman_black_widow),
                 (troop_set_slot, "trp_tournament_participants", ":cur_slot", ":woman_black_widow"),
              (else_try),
                (eq, ":random_no", 4),
				(troop_get_slot,":mercenary_grosskomtur","$troop_trees",slot_mercenary_grosskomtur),
                 (troop_set_slot, "trp_tournament_participants", ":cur_slot", ":mercenary_grosskomtur"),
              (else_try),
				(troop_get_slot,":mercenary_hochmeister","$troop_trees",slot_mercenary_hochmeister),
                 (troop_set_slot, "trp_tournament_participants", ":cur_slot", ":mercenary_hochmeister"),
              (try_end),
				##Floris MTT end
            (try_end),
        ]),
        
        # script_get_num_tournament_participants
        # Input: none
        # Output: reg0 = num_participants
        ("get_num_tournament_participants",
          [(assign, ":num_participants", 0),
            (try_for_range, ":cur_slot", 0, 64),
              (troop_slot_ge, "trp_tournament_participants", ":cur_slot", 0),
              (val_add, ":num_participants", 1),
            (try_end),
            (assign, reg0, ":num_participants"),
        ]),
        
        # script_get_random_tournament_participant
        # Input: none
        # Output: reg0 = troop_no
        ("get_random_tournament_participant",
          [(call_script, "script_get_num_tournament_participants"),
            (assign, ":num_participants", reg0),
            (store_random_in_range, ":random_troop", 0, ":num_participants"),
            (assign, ":continue", 1),
            (try_for_range, ":cur_slot", 0, 64),
              (eq, ":continue", 1),
              (troop_slot_ge, "trp_tournament_participants", ":cur_slot", 0),
              (val_sub, ":random_troop", 1),
              (lt, ":random_troop", 0),
              (assign, ":continue", 0),
              (troop_get_slot, ":troop_no", "trp_tournament_participants", ":cur_slot"),
              (troop_set_slot, "trp_tournament_participants", ":cur_slot", -1),
            (try_end),
            (assign, reg0, ":troop_no"),
        ]),
        
        # script_add_tournament_participant
        # Input: arg1 = troop_no
        # Output: none
        ("add_tournament_participant",
          [(store_script_param, ":troop_no", 1),
            (assign, ":continue", 1),
            (try_for_range, ":cur_slot", 0, 64),
              (eq, ":continue", 1),
              (troop_slot_eq, "trp_tournament_participants", ":cur_slot", -1),
              (troop_set_slot, "trp_tournament_participants", ":cur_slot", ":troop_no"),
              (assign, ":continue", 0),
            (try_end),
        ]),
        
        # script_get_random_tournament_team_amount_and_size
        # Input: none
        # Output: reg0 = number_of_teams, reg1 = team_size
        ("get_random_tournament_team_amount_and_size",
          [
            (call_script, "script_get_num_tournament_participants"),
            (assign, ":num_participants", reg0),
            (party_get_slot, ":town_max_teams", "$current_town", slot_town_tournament_max_teams),
            (val_add, ":town_max_teams", 1),
            (party_get_slot, ":town_max_team_size", "$current_town", slot_town_tournament_max_team_size),
            (val_add, ":town_max_team_size", 1),
            (assign, ":max_teams", ":num_participants"),
            (val_min, ":max_teams", ":town_max_teams"),
            (assign, ":max_size", ":num_participants"),
            (val_min, ":max_size", ":town_max_team_size"),
            (assign, ":min_size", 1),
            (try_begin),
              (ge, ":num_participants", 32),
              (assign, ":min_size", 2),
              (val_min, ":min_size", ":town_max_team_size"),
            (try_end),
            (assign, ":end_cond", 500),
            (try_for_range, ":unused", 0, ":end_cond"),
              (store_random_in_range, ":random_teams", 2, ":max_teams"),
              (store_random_in_range, ":random_size", ":min_size", ":max_size"),
              (store_mul, ":total_men", ":random_teams", ":random_size"),
              (le, ":total_men", ":num_participants"),
              (store_sub, ":left_men", ":num_participants", ":total_men"),
              (neq, ":left_men", 1),
              (assign, ":end_cond", 0),
            (try_end),
            (try_begin),
              (gt, ":end_cond", 0),
              (assign, ":random_teams", 2),
              (assign, ":random_size", 1),
            (try_end),
            (assign, reg0, ":random_teams"),
            (assign, reg1, ":random_size"),
        ]),
        
        # script_get_troop_priority_point_for_tournament
        # Input: arg1 = troop_no
        # Output: reg0 = troop_point
        ("get_troop_priority_point_for_tournament",
          [(store_script_param, ":troop_no", 1),
            (assign, ":troop_point", 0),
            (try_begin),
              (ge, ":troop_no", 0),
              (val_add, ":troop_point", 40000),
              (try_begin),
                (eq, ":troop_no", "trp_player"),
                (val_add, ":troop_point", 80000),
              (try_end),
              (try_begin),
                (troop_is_hero, ":troop_no"),
                (val_add, ":troop_point", 20000),
              (try_end),
              (try_begin),
                (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_player_companion),
                (val_add, ":troop_point", 10000),
              (else_try),
                (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
                (troop_get_slot, ":renown", ":troop_no", slot_troop_renown),
                (val_add, ":troop_point", ":renown"),
                (val_add, ":troop_point", 1000), #in order to make it more prior than tournament heroes with higher levels
              (else_try),
                (store_character_level, ":level", ":troop_no"),
                (val_add, ":troop_point", ":level"),
              (try_end),
            (try_end),
            (assign, reg0, ":troop_point"),
        ]),
        
        # script_sort_tournament_participant_troops
        # Input: none
        # Output: none (sorts trp_tournament_participants)
        ("sort_tournament_participant_troops",
          [(try_for_range, ":cur_slot", 0, 63),
              (store_add, ":cur_slot_2_begin", ":cur_slot", 1),
              (try_for_range, ":cur_slot_2", ":cur_slot_2_begin", 64),
                (troop_get_slot, ":troop_1", "trp_tournament_participants", ":cur_slot"),
                (troop_get_slot, ":troop_2", "trp_tournament_participants", ":cur_slot_2"),
                (call_script, "script_get_troop_priority_point_for_tournament", ":troop_1"),
                (assign, ":troop_1_point", reg0),
                (call_script, "script_get_troop_priority_point_for_tournament", ":troop_2"),
                (assign, ":troop_2_point", reg0),
                (gt, ":troop_2_point", ":troop_1_point"),
                (troop_set_slot, "trp_tournament_participants", ":cur_slot", ":troop_2"),
                (troop_set_slot, "trp_tournament_participants", ":cur_slot_2", ":troop_1"),
              (try_end),
            (try_end),
        ]),
        
        # script_remove_tournament_participants_randomly
        # Input: arg1 = number_to_be_removed
        # Output: none
        ("remove_tournament_participants_randomly",
          [(store_script_param, ":number_to_be_removed", 1),
            (try_for_range, ":unused", 0, ":number_to_be_removed"),
              (assign, ":total_weight", 0),
              (try_for_range, ":cur_slot", 0, 64),
                (troop_get_slot, ":troop_no", "trp_tournament_participants", ":cur_slot"),
                (ge, ":troop_no", 0),
                (store_character_level, ":level", ":troop_no"),
                (val_min, ":level", 38),
                (store_sub, ":weight", 40, ":level"),
                (val_add, ":total_weight", ":weight"),
              (try_end),
              (store_random_in_range, ":random_weight", 0, ":total_weight"),
              (assign, ":continue", 1),
              (try_for_range, ":cur_slot", 0, 64),
                (eq, ":continue", 1),
                (troop_get_slot, ":troop_no", "trp_tournament_participants", ":cur_slot"),
                (ge, ":troop_no", 0),
                (store_character_level, ":level", ":troop_no"),
                (val_min, ":level", 38),
                (store_sub, ":weight", 40, ":level"),
                (val_sub, ":random_weight", ":weight"),
                (lt, ":random_weight", 0),
                (troop_set_slot, "trp_tournament_participants", ":cur_slot", -1),
                (assign, ":continue", 0),
              (try_end),
            (try_end),
        ]),
        
        # script_end_tournament_fight
        # Input: arg1 = player_team_won (1 or 0)
        # Output: none
        ("end_tournament_fight",
          [(store_script_param, ":player_team_won", 1),
            (call_script, "script_get_num_tournament_participants"),
            (assign, ":num_participants", reg0),
            (store_div, ":needed_to_remove_randomly", ":num_participants", 2),
            #Must remove other participants randomly earlier than adding the winners back to participants
            (call_script, "script_remove_tournament_participants_randomly", ":needed_to_remove_randomly"),
            
            (assign, ":num_needed", "$g_tournament_num_participants_for_fight"),
            (val_div, ":num_needed", 2),
            (get_player_agent_no, ":player_agent"),
            (agent_get_team, ":player_team", ":player_agent"),
            (try_for_agents, ":agent_no"),
              (agent_is_human, ":agent_no"),
              (agent_get_troop_id, ":troop_id", ":agent_no"),
              (neg|is_between, ":troop_id", arena_masters_begin, arena_masters_end),#omit tournament master
              (agent_get_team, ":agent_team", ":agent_no"),
              (assign, ":cur_point", 0),
              (try_begin),
                (eq, ":player_team_won", 1),
                (eq, ":agent_team", ":player_team"),
                (val_add, ":cur_point", 5000000),#Make sure that team members are chosen
              (try_end),
              (agent_get_kill_count, ":kill_count", ":agent_no", 1), #everyone is knocked unconscious
              (store_mul, ":kill_point", ":kill_count", 160000),#Make sure that kill count is the second most important variable
              (val_add, ":cur_point", ":kill_point"),
              (call_script, "script_get_troop_priority_point_for_tournament", ":troop_id"),
              (val_add, ":cur_point", reg0),
              (try_begin),#reset player's point if kill count is one after the first 2 rounds, or if it is zero
                (eq, ":agent_no", ":player_agent"),
                (eq, ":player_team_won", 0),
                (assign, ":not_passed", 1),
                (try_begin),
                  (ge, ":kill_count", 2),
                  (assign, ":not_passed", 0),
                (else_try),
                  (eq, ":kill_count", 1),
                  (le, "$g_tournament_cur_tier", 1),
                  (assign, ":not_passed", 0),
                (try_end),
                (eq, ":not_passed", 1),
                (assign, ":cur_point", 0),
              (try_end),
              (agent_set_slot, ":agent_no", slot_agent_tournament_point, ":cur_point"),
            (try_end),
            (try_for_range, ":unused", 0, ":num_needed"),
              (assign, ":best_point", 0),
              (assign, ":best_agent_no", -1),
              (try_for_agents, ":agent_no"),
                (agent_is_human, ":agent_no"),
                (agent_get_slot, ":point", ":agent_no", slot_agent_tournament_point),
                (gt, ":point", ":best_point"),
                (assign, ":best_agent_no", ":agent_no"),
                (assign, ":best_point", ":point"),
              (try_end),
              (agent_set_slot, ":best_agent_no", slot_agent_tournament_point, 0),#Do not select the same agent again
              (agent_get_troop_id, ":troop_id", ":best_agent_no"),
              (call_script, "script_add_tournament_participant", ":troop_id"),
            (try_end),
            (assign, "$g_tournament_player_team_won", ":player_team_won"),
            (jump_to_menu, "mnu_town_tournament"),
        ]),
        
        
        # script_get_win_amount_for_tournament_bet
        # Input: none
        # Output: reg0 = win_amount_with_100_denars
        ("get_win_amount_for_tournament_bet",
          [
            (party_get_slot, ":player_odds", "$current_town", slot_town_player_odds),
            (try_begin),
              (eq, "$g_tournament_cur_tier", 0),
              (assign, ":win_amount", 120),
            (else_try),
              (eq, "$g_tournament_cur_tier", 1),
              (assign, ":win_amount", 90),
            (else_try),
              (eq, "$g_tournament_cur_tier", 2),
              (assign, ":win_amount", 60),
            (else_try),
              (eq, "$g_tournament_cur_tier", 3),
              (assign, ":win_amount", 40),
            (else_try),
              (eq, "$g_tournament_cur_tier", 4),
              (assign, ":win_amount", 20),
            (else_try),
              (assign, ":win_amount", 8),
            (try_end),
            (val_mul, ":win_amount", ":player_odds"),
            (val_div, ":win_amount", 100),
            (val_add, ":win_amount", 100), #win amount when 100 denars is placed
            (assign, reg0, ":win_amount"),
        ]),
        
        # script_tournament_place_bet
        # Input: arg1 = bet_amount
        # Output: none
        ("tournament_place_bet",
          [
            (store_script_param, ":bet_amount", 1),
            (call_script, "script_get_win_amount_for_tournament_bet"),
            (assign, ":win_amount", reg0),
            (val_mul, ":win_amount", ":bet_amount"),
            (val_div, ":win_amount", 100),
            (val_sub, ":win_amount", ":bet_amount"),
            (val_add, "$g_tournament_bet_placed", ":bet_amount"),
            (val_add, "$g_tournament_bet_win_amount", ":win_amount"),
            (troop_remove_gold, "trp_player", ":bet_amount"),
            (assign, "$g_tournament_last_bet_tier", "$g_tournament_cur_tier"),
        ]),
        
        # script_calculate_amount_of_cattle_can_be_stolen
        # Input: arg1 = village_no
        # Output: reg0 = max_amount
        ("calculate_amount_of_cattle_can_be_stolen",
          [
            (store_script_param, ":village_no", 1),
            (call_script, "script_get_max_skill_of_player_party", "skl_looting"),
            (assign, ":max_skill", reg0),
            (store_mul, ":can_steal", ":max_skill", 2),
            (call_script, "script_party_count_fit_for_battle", "p_main_party"),
            (store_add, ":num_men_effect", reg0, 10),
            (val_div, ":num_men_effect", 10),
            (val_add, ":can_steal", ":num_men_effect"),
            (party_get_slot, ":num_cattle", ":village_no", slot_village_number_of_cattle),
            (val_min, ":can_steal", ":num_cattle"),
            (assign, reg0, ":can_steal"),
        ]),
        
        
        # script_draw_banner_to_region
        # Input: arg1 = troop_no, arg2 = center_pos_x, arg3 = center_pos_y, arg4 = width, arg5 = height, arg6 = stretch_width, arg7 = stretch_height, arg8 = default_scale, arg9 = max_charge_scale, arg10 = drawn_item_type
        # drawn_item_type is 0 for banners, 1 for shields, 2 for heater shield, 3 for armor
        # arguments will be used as fixed point values
        # Output: none
        ("draw_banner_to_region",
          [
            (store_script_param, ":troop_no", 1),
            (store_script_param, ":center_pos_x", 2),
            (store_script_param, ":center_pos_y", 3),
            (store_script_param, ":width", 4),
            (store_script_param, ":height", 5),
            (store_script_param, ":stretch_width", 6),
            (store_script_param, ":stretch_height", 7),
            (store_script_param, ":default_scale", 8),
            (store_script_param, ":max_charge_scale", 9),
            (store_script_param, ":drawn_item_type", 10),
            
            (troop_get_slot, ":bg_type", ":troop_no", slot_troop_custom_banner_bg_type),
            (val_add, ":bg_type", custom_banner_backgrounds_begin),
            (troop_get_slot, ":bg_color_1", ":troop_no", slot_troop_custom_banner_bg_color_1),
            (troop_get_slot, ":bg_color_2", ":troop_no", slot_troop_custom_banner_bg_color_2),
            (troop_get_slot, ":num_charges", ":troop_no", slot_troop_custom_banner_num_charges),
            (troop_get_slot, ":positioning", ":troop_no", slot_troop_custom_banner_positioning),
            (call_script, "script_get_troop_custom_banner_num_positionings", ":troop_no"),
            (assign, ":num_positionings", reg0),
            (val_mod, ":positioning", ":num_positionings"),
            
            (init_position, pos2),
            (position_set_x, pos2, ":width"),
            (position_set_y, pos2, ":height"),
            (assign, ":default_value", 1),
            (convert_to_fixed_point, ":default_value"),
            (position_set_z, pos2, ":default_value"),
            
            (init_position, pos1),
            (position_set_x, pos1, ":center_pos_x"),
            (position_set_y, pos1, ":center_pos_y"),
            (position_move_z, pos1, -20),
            
            (init_position, pos3),
            (position_set_x, pos3, ":default_scale"),
            (position_set_y, pos3, ":default_scale"),
            (position_set_z, pos3, ":default_value"),
            
            (try_begin),
              (this_or_next|eq, ":bg_type", "mesh_custom_banner_bg"),
              (this_or_next|eq, ":bg_type", "mesh_custom_banner_fg01"),
              (this_or_next|eq, ":bg_type", "mesh_custom_banner_fg02"),
              (this_or_next|eq, ":bg_type", "mesh_custom_banner_fg03"),
              (this_or_next|eq, ":bg_type", "mesh_custom_banner_fg08"),
              (this_or_next|eq, ":bg_type", "mesh_custom_banner_fg09"),
              (this_or_next|eq, ":bg_type", "mesh_custom_banner_fg10"),
              (this_or_next|eq, ":bg_type", "mesh_custom_banner_fg11"),
              (this_or_next|eq, ":bg_type", "mesh_custom_banner_fg12"),
              (this_or_next|eq, ":bg_type", "mesh_custom_banner_fg13"),
              (this_or_next|eq, ":bg_type", "mesh_custom_banner_fg16"),
              (eq, ":bg_type", "mesh_custom_banner_fg17"),
              (cur_tableau_add_mesh_with_scale_and_vertex_color, ":bg_type", pos1, pos2, 0, ":bg_color_1"),
            (else_try),
              (cur_tableau_add_mesh_with_scale_and_vertex_color, ":bg_type", pos1, pos3, 0, ":bg_color_1"),
            (try_end),
            (position_move_z, pos1, -20),
            (position_move_x, pos2, ":width"),
            (position_move_y, pos2, ":height"),
            (cur_tableau_add_mesh_with_scale_and_vertex_color, "mesh_custom_banner_bg", pos1, pos2, 0, ":bg_color_2"),
            
            (assign, ":charge_stretch", ":stretch_width"),
            (val_min, ":charge_stretch", ":stretch_height"),
            (val_min, ":charge_stretch", ":max_charge_scale"),
            (call_script, "script_get_custom_banner_charge_type_position_scale_color", "trp_player", ":positioning"),
            
            (try_begin),
              (this_or_next|eq, ":drawn_item_type", 2), #heater shield
              (eq, ":drawn_item_type", 3), #armor
              (assign, ":change_center_pos", 0),
              (try_begin),
                (eq, ":num_charges", 1),
                (assign, ":change_center_pos", 1),
              (else_try),
                (eq, ":num_charges", 2),
                (eq, ":positioning", 1),
                (assign, ":change_center_pos", 1),
              (else_try),
                (eq, ":num_charges", 3),
                (eq, ":positioning", 1),
                (assign, ":change_center_pos", 1),
              (try_end),
              (try_begin),
                (eq, ":change_center_pos", 1),
                (val_add, ":center_pos_y", 30),
              (try_end),
            (try_end),
            
            (try_begin),
              (ge, ":num_charges", 1),
              (val_mul, reg1, ":charge_stretch"),
              (val_div, reg1, 10000),
              (position_get_x, ":x", pos0),
              (position_get_y, ":y", pos0),
              (val_mul, ":x", ":stretch_width"),
              (val_mul, ":y", ":stretch_height"),
              (val_div, ":x", 10000),
              (val_div, ":y", 10000),
              (val_add, ":x", ":center_pos_x"),
              (val_add, ":y", ":center_pos_y"),
              (position_set_x, pos0, ":x"),
              (position_set_y, pos0, ":y"),
              (assign, ":scale_value", reg1),
              (convert_to_fixed_point, ":scale_value"),
              (store_mul, ":scale_value_inverse", ":scale_value", -1),
              (init_position, pos4),
              (position_set_x, pos4, ":scale_value"),
              (position_set_y, pos4, ":scale_value"),
              (position_set_z, pos4, ":scale_value"),
              (store_div, ":orientation", reg0, 256), #orientation flags
              (try_begin),
                (this_or_next|eq, ":orientation", 1),
                (eq, ":orientation", 3),
                (position_set_x, pos4, ":scale_value_inverse"),
              (try_end),
              (try_begin),
                (this_or_next|eq, ":orientation", 2),
                (eq, ":orientation", 3),
                (position_set_y, pos4, ":scale_value_inverse"),
              (try_end),
              (val_mod, reg0, 256), #remove orientation flags
              (cur_tableau_add_mesh_with_scale_and_vertex_color, reg0, pos0, pos4, 0, reg2),
            (try_end),
            (try_begin),
              (ge, ":num_charges", 2),
              (val_mul, reg4, ":charge_stretch"),
              (val_div, reg4, 10000),
              (position_get_x, ":x", pos1),
              (position_get_y, ":y", pos1),
              (val_mul, ":x", ":stretch_width"),
              (val_mul, ":y", ":stretch_height"),
              (val_div, ":x", 10000),
              (val_div, ":y", 10000),
              (val_add, ":x", ":center_pos_x"),
              (val_add, ":y", ":center_pos_y"),
              (position_set_x, pos1, ":x"),
              (position_set_y, pos1, ":y"),
              
              (assign, ":scale_value", reg4),
              (convert_to_fixed_point, ":scale_value"),
              (store_mul, ":scale_value_inverse", ":scale_value", -1),
              (init_position, pos4),
              (position_set_x, pos4, ":scale_value"),
              (position_set_y, pos4, ":scale_value"),
              (position_set_z, pos4, ":scale_value"),
              (store_div, ":orientation", reg3, 256), #orientation flags
              (try_begin),
                (this_or_next|eq, ":orientation", 1),
                (eq, ":orientation", 3),
                (position_set_x, pos4, ":scale_value_inverse"),
              (try_end),
              (try_begin),
                (this_or_next|eq, ":orientation", 2),
                (eq, ":orientation", 3),
                (position_set_y, pos4, ":scale_value_inverse"),
              (try_end),
              (val_mod, reg3, 256), #remove orientation flags
              
              (cur_tableau_add_mesh_with_scale_and_vertex_color, reg3, pos1, pos4, 0, reg5),
            (try_end),
            (try_begin),
              (ge, ":num_charges", 3),
              (val_mul, reg7, ":charge_stretch"),
              (val_div, reg7, 10000),
              (position_get_x, ":x", pos2),
              (position_get_y, ":y", pos2),
              (val_mul, ":x", ":stretch_width"),
              (val_mul, ":y", ":stretch_height"),
              (val_div, ":x", 10000),
              (val_div, ":y", 10000),
              (val_add, ":x", ":center_pos_x"),
              (val_add, ":y", ":center_pos_y"),
              (position_set_x, pos2, ":x"),
              (position_set_y, pos2, ":y"),
              
              (assign, ":scale_value", reg7),
              (convert_to_fixed_point, ":scale_value"),
              (store_mul, ":scale_value_inverse", ":scale_value", -1),
              (init_position, pos4),
              (position_set_x, pos4, ":scale_value"),
              (position_set_y, pos4, ":scale_value"),
              (position_set_z, pos4, ":scale_value"),
              (store_div, ":orientation", reg6, 256), #orientation flags
              (try_begin),
                (this_or_next|eq, ":orientation", 1),
                (eq, ":orientation", 3),
                (position_set_x, pos4, ":scale_value_inverse"),
              (try_end),
              (try_begin),
                (this_or_next|eq, ":orientation", 2),
                (eq, ":orientation", 3),
                (position_set_y, pos4, ":scale_value_inverse"),
              (try_end),
              (val_mod, reg6, 256), #remove orientation flags
              
              (cur_tableau_add_mesh_with_scale_and_vertex_color, reg6, pos2, pos4, 0, reg8),
            (try_end),
            (try_begin),
              (ge, ":num_charges", 4),
              (val_mul, reg10, ":charge_stretch"),
              (val_div, reg10, 10000),
              (position_get_x, ":x", pos3),
              (position_get_y, ":y", pos3),
              (val_mul, ":x", ":stretch_width"),
              (val_mul, ":y", ":stretch_height"),
              (val_div, ":x", 10000),
              (val_div, ":y", 10000),
              (val_add, ":x", ":center_pos_x"),
              (val_add, ":y", ":center_pos_y"),
              (position_set_x, pos3, ":x"),
              (position_set_y, pos3, ":y"),
              
              (assign, ":scale_value", reg10),
              (convert_to_fixed_point, ":scale_value"),
              (store_mul, ":scale_value_inverse", ":scale_value", -1),
              (init_position, pos4),
              (position_set_x, pos4, ":scale_value"),
              (position_set_y, pos4, ":scale_value"),
              (position_set_z, pos4, ":scale_value"),
              (store_div, ":orientation", reg9, 256), #orientation flags
              (try_begin),
                (this_or_next|eq, ":orientation", 1),
                (eq, ":orientation", 3),
                (position_set_x, pos4, ":scale_value_inverse"),
              (try_end),
              (try_begin),
                (this_or_next|eq, ":orientation", 2),
                (eq, ":orientation", 3),
                (position_set_y, pos4, ":scale_value_inverse"),
              (try_end),
              (val_mod, reg9, 256), #remove orientation flags
              
              (cur_tableau_add_mesh_with_scale_and_vertex_color, reg9, pos3, pos4, 0, reg11),
            (try_end),
        ]),
        
        # script_get_troop_custom_banner_num_positionings
        # Input: arg1 = troop_no
        # Output: reg0 = num_positionings
        ("get_troop_custom_banner_num_positionings",
          [
            (store_script_param, ":troop_no", 1),
            (troop_get_slot, ":num_charges", ":troop_no", slot_troop_custom_banner_num_charges),
            (try_begin),
              (eq, ":num_charges", 1),
              (assign, ":num_positionings", 2),
            (else_try),
              (eq, ":num_charges", 2),
              (assign, ":num_positionings", 4),
            (else_try),
              (eq, ":num_charges", 3),
              (assign, ":num_positionings", 6),
            (else_try),
              (assign, ":num_positionings", 2),
            (try_end),
            (assign, reg0, ":num_positionings"),
        ]),
        
        # script_get_custom_banner_charge_type_position_scale_color
        # Input: arg1 = troop_no, arg2 = positioning_index
        # Output: reg0 = type_1
        #         reg1 = scale_1
        #         reg2 = color_1
        #         reg3 = type_2
        #         reg4 = scale_2
        #         reg5 = color_2
        #         reg6 = type_3
        #         reg7 = scale_3
        #         reg8 = color_3
        #         reg9 = type_4
        #         reg10 = scale_4
        #         reg11 = color_4
        ("get_custom_banner_charge_type_position_scale_color",
          [
            (store_script_param, ":troop_no", 1),
            (store_script_param, ":positioning", 2),
            (troop_get_slot, ":num_charges", ":troop_no", slot_troop_custom_banner_num_charges),
            (init_position, pos0),
            (init_position, pos1),
            (init_position, pos2),
            (init_position, pos3),
            
            (troop_get_slot, reg0, ":troop_no", slot_troop_custom_banner_charge_type_1),
            (val_add, reg0, custom_banner_charges_begin),
            (troop_get_slot, reg2, ":troop_no", slot_troop_custom_banner_charge_color_1),
            (troop_get_slot, reg3, ":troop_no", slot_troop_custom_banner_charge_type_2),
            (val_add, reg3, custom_banner_charges_begin),
            (troop_get_slot, reg5, ":troop_no", slot_troop_custom_banner_charge_color_2),
            (troop_get_slot, reg6, ":troop_no", slot_troop_custom_banner_charge_type_3),
            (val_add, reg6, custom_banner_charges_begin),
            (troop_get_slot, reg8, ":troop_no", slot_troop_custom_banner_charge_color_3),
            (troop_get_slot, reg9, ":troop_no", slot_troop_custom_banner_charge_type_4),
            (val_add, reg9, custom_banner_charges_begin),
            (troop_get_slot, reg11, ":troop_no", slot_troop_custom_banner_charge_color_4),
            
            (try_begin),
              (eq, ":num_charges", 1),
              (try_begin),
                (eq, ":positioning", 0),
                (assign, reg1, 100),
              (else_try),
                (assign, reg1, 50),
              (try_end),
            (else_try),
              (eq, ":num_charges", 2),
              (try_begin),
                (eq, ":positioning", 0),
                (position_set_y, pos0, 25),
                (position_set_y, pos1, -25),
                (assign, reg1, 40),
                (assign, reg4, 40),
              (else_try),
                (eq, ":positioning", 1),
                (position_set_x, pos0, -25),
                (position_set_x, pos1, 25),
                (assign, reg1, 40),
                (assign, reg4, 40),
              (else_try),
                (eq, ":positioning", 2),
                (position_set_x, pos0, -25),
                (position_set_y, pos0, 25),
                (position_set_x, pos1, 25),
                (position_set_y, pos1, -25),
                (assign, reg1, 50),
                (assign, reg4, 50),
              (else_try),
                (position_set_x, pos0, -25),
                (position_set_y, pos0, -25),
                (position_set_x, pos1, 25),
                (position_set_y, pos1, 25),
                (assign, reg1, 50),
                (assign, reg4, 50),
              (try_end),
            (else_try),
              (eq, ":num_charges", 3),
              (try_begin),
                (eq, ":positioning", 0),
                (position_set_y, pos0, 33),
                (position_set_y, pos2, -33),
                (assign, reg1, 30),
                (assign, reg4, 30),
                (assign, reg7, 30),
              (else_try),
                (eq, ":positioning", 1),
                (position_set_x, pos0, -33),
                (position_set_x, pos2, 33),
                (assign, reg1, 30),
                (assign, reg4, 30),
                (assign, reg7, 30),
              (else_try),
                (eq, ":positioning", 2),
                (position_set_x, pos0, -30),
                (position_set_y, pos0, 30),
                (position_set_x, pos2, 30),
                (position_set_y, pos2, -30),
                (assign, reg1, 35),
                (assign, reg4, 35),
                (assign, reg7, 35),
              (else_try),
                (eq, ":positioning", 3),
                (position_set_x, pos0, -30),
                (position_set_y, pos0, -30),
                (position_set_x, pos2, 30),
                (position_set_y, pos2, 30),
                (assign, reg1, 35),
                (assign, reg4, 35),
                (assign, reg7, 35),
              (else_try),
                (eq, ":positioning", 4),
                (position_set_x, pos0, -25),
                (position_set_y, pos0, -25),
                (position_set_y, pos1, 25),
                (position_set_x, pos2, 25),
                (position_set_y, pos2, -25),
                (assign, reg1, 50),
                (assign, reg4, 50),
                (assign, reg7, 50),
              (else_try),
                (position_set_x, pos0, -25),
                (position_set_y, pos0, 25),
                (position_set_y, pos1, -25),
                (position_set_x, pos2, 25),
                (position_set_y, pos2, 25),
                (assign, reg1, 50),
                (assign, reg4, 50),
                (assign, reg7, 50),
              (try_end),
            (else_try),
              (try_begin),
                (eq, ":positioning", 0),
                (position_set_x, pos0, -25),
                (position_set_y, pos0, 25),
                (position_set_x, pos1, 25),
                (position_set_y, pos1, 25),
                (position_set_x, pos2, -25),
                (position_set_y, pos2, -25),
                (position_set_x, pos3, 25),
                (position_set_y, pos3, -25),
                (assign, reg1, 50),
                (assign, reg4, 50),
                (assign, reg7, 50),
                (assign, reg10, 50),
              (else_try),
                (position_set_y, pos0, 30),
                (position_set_x, pos1, -30),
                (position_set_x, pos2, 30),
                (position_set_y, pos3, -30),
                (assign, reg1, 35),
                (assign, reg4, 35),
                (assign, reg7, 35),
                (assign, reg10, 35),
              (try_end),
            (try_end),
        ]),
        
        # script_get_random_custom_banner
        # Input: arg1 = troop_no
        # Output: none
        ("get_random_custom_banner",
          [
            (store_script_param, ":troop_no", 1),
            (store_random_in_range, ":num_charges", 1, 5),
            (troop_set_slot, ":troop_no", slot_troop_custom_banner_num_charges, ":num_charges"),
            (store_random_in_range, ":random_color_index", 0, 42),
            (call_script, "script_get_custom_banner_color_from_index", ":random_color_index"),
            (assign, ":color_1", reg0),
            (troop_set_slot, ":troop_no", slot_troop_custom_banner_bg_color_1, ":color_1"),
            (assign, ":end_cond", 1),
            (try_for_range, ":unused", 0, ":end_cond"),
              (store_random_in_range, ":random_color_index", 0, 42),
              (call_script, "script_get_custom_banner_color_from_index", ":random_color_index"),
              (assign, ":color_2", reg0),
              (try_begin),
                (call_script, "script_cf_check_color_visibility", ":color_1", ":color_2"),
                (troop_set_slot, ":troop_no", slot_troop_custom_banner_bg_color_2, ":color_2"),
              (else_try),
                (val_add, ":end_cond", 1),
              (try_end),
            (try_end),
            (assign, ":end_cond", 4),
            (assign, ":cur_charge", 0),
            (try_for_range, ":unused", 0, ":end_cond"),
              (store_random_in_range, ":random_color_index", 0, 42),
              (call_script, "script_get_custom_banner_color_from_index", ":random_color_index"),
              (assign, ":charge_color", reg0),
              (try_begin),
                (call_script, "script_cf_check_color_visibility", ":charge_color", ":color_1"),
                (call_script, "script_cf_check_color_visibility", ":charge_color", ":color_2"),
                (store_add, ":cur_slot", ":cur_charge", slot_troop_custom_banner_charge_color_1),
                (troop_set_slot, ":troop_no", ":cur_slot", ":charge_color"),
                (store_random_in_range, ":random_charge", custom_banner_charges_begin, custom_banner_charges_end),
                (val_sub, ":random_charge", custom_banner_charges_begin),
                (store_add, ":cur_slot", ":cur_charge", slot_troop_custom_banner_charge_type_1),
                (troop_set_slot, ":troop_no", ":cur_slot", ":random_charge"),
                (val_add, ":cur_charge", 1),
              (else_try),
                (val_add, ":end_cond", 1),
              (try_end),
            (try_end),
            (store_random_in_range, ":random_bg", custom_banner_backgrounds_begin, custom_banner_backgrounds_end),
            (val_sub, ":random_bg", custom_banner_backgrounds_begin),
            (troop_set_slot, ":troop_no", slot_troop_custom_banner_bg_type, ":random_bg"),
            (store_random_in_range, ":random_flag", custom_banner_flag_types_begin, custom_banner_flag_types_end),
            (val_sub, ":random_flag", custom_banner_flag_types_begin),
            (troop_set_slot, ":troop_no", slot_troop_custom_banner_flag_type, ":random_flag"),
            (store_random_in_range, ":random_positioning", 0, 4),
            (troop_set_slot, ":troop_no", slot_troop_custom_banner_positioning, ":random_positioning"),
        ]),
        
        # script_get_custom_banner_color_from_index
        # Input: arg1 = color_index
        # Output: reg0 = color
        ("get_custom_banner_color_from_index",
          [
            (store_script_param, ":color_index", 1),
            
            (assign, ":cur_color", 0xFF000000),
            (assign, ":red", 0x00),
            (assign, ":green", 0x00),
            (assign, ":blue", 0x00),
            (store_mod, ":mod_i_color", ":color_index", 7),
            (try_begin),
              (eq, ":mod_i_color", 0),
              (assign, ":blue", 0xFF),
            (else_try),
              (eq, ":mod_i_color", 1),
              (assign, ":red", 0xEE),
            (else_try),
              (eq, ":mod_i_color", 2),
              (assign, ":red", 0xFB),
              (assign, ":green", 0xAC),
            (else_try),
              (eq, ":mod_i_color", 3),
              (assign, ":red", 0x5F),
              (assign, ":blue", 0xFF),
            (else_try),
              (eq, ":mod_i_color", 4),
              (assign, ":red", 0x05),
              (assign, ":green", 0x44),
            (else_try),
              (eq, ":mod_i_color", 5),
              (assign, ":red", 0xEE),
              (assign, ":green", 0xEE),
              (assign, ":blue", 0xEE),
            (else_try),
              (assign, ":red", 0x22),
              (assign, ":green", 0x22),
              (assign, ":blue", 0x22),
            (try_end),
            (store_div, ":cur_tone", ":color_index", 7),
            (store_sub, ":cur_tone", 8, ":cur_tone"),
            (val_mul, ":red", ":cur_tone"),
            (val_div, ":red", 8),
            (val_mul, ":green", ":cur_tone"),
            (val_div, ":green", 8),
            (val_mul, ":blue", ":cur_tone"),
            (val_div, ":blue", 8),
            (val_mul, ":green", 0x100),
            (val_mul, ":red", 0x10000),
            (val_add, ":cur_color", ":blue"),
            (val_add, ":cur_color", ":green"),
            (val_add, ":cur_color", ":red"),
            (assign, reg0, ":cur_color"),
        ]),
        
        # script_cf_check_color_visibility
        # Input: arg1 = color_1, arg2 = color_2
        # Output: none
        ("cf_check_color_visibility",
          [
            (store_script_param, ":color_1", 1),
            (store_script_param, ":color_2", 2),
            (store_mod, ":blue_1", ":color_1", 256),
            (store_div, ":green_1", ":color_1", 256),
            (val_mod, ":green_1", 256),
            (store_div, ":red_1", ":color_1", 256 * 256),
            (val_mod, ":red_1", 256),
            (store_mod, ":blue_2", ":color_2", 256),
            (store_div, ":green_2", ":color_2", 256),
            (val_mod, ":green_2", 256),
            (store_div, ":red_2", ":color_2", 256 * 256),
            (val_mod, ":red_2", 256),
            (store_sub, ":red_dif", ":red_1", ":red_2"),
            (val_abs, ":red_dif"),
            (store_sub, ":green_dif", ":green_1", ":green_2"),
            (val_abs, ":green_dif"),
            (store_sub, ":blue_dif", ":blue_1", ":blue_2"),
            (val_abs, ":blue_dif"),
            (assign, ":max_dif", 0),
            (val_max, ":max_dif", ":red_dif"),
            (val_max, ":max_dif", ":green_dif"),
            (val_max, ":max_dif", ":blue_dif"),
            (ge, ":max_dif", 64),
        ]),
        
        # script_get_next_active_kingdom
        # Input: arg1 = faction_no
        # Output: reg0 = faction_no (does not choose player faction)
        ("get_next_active_kingdom",
          [
            (store_script_param, ":faction_no", 1),
            (assign, ":end_cond", kingdoms_end),
            (try_for_range, ":unused", kingdoms_begin, ":end_cond"),
              (val_add, ":faction_no", 1),
              (try_begin),
                (ge, ":faction_no", kingdoms_end),
                (assign, ":faction_no", kingdoms_begin),
              (try_end),
              (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
              (neq, ":faction_no", "fac_player_supporters_faction"),
              (assign, ":end_cond", 0),
            (try_end),
            (assign, reg0, ":faction_no"),
        ]),
        
        #  # script_store_average_center_value_per_faction
        #  # Input: none
        #  # Output: none (sets $g_average_center_value_per_faction)
        #  ("store_average_center_value_per_faction",
        #    [
        #      (store_sub, ":num_towns", towns_end, towns_begin),
        #      (store_sub, ":num_castles", castles_end, castles_begin),
        #      (assign, ":num_factions", 0),
        #      (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        #        (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
        #        (val_add, ":num_factions", 1),
        #      (try_end),
        #      (val_max, ":num_factions", 1),
        #      (store_mul, "$g_average_center_value_per_faction", ":num_towns", 2),
        #      (val_add, "$g_average_center_value_per_faction", ":num_castles"),
        #      (val_mul, "$g_average_center_value_per_faction", 10),
        #      (val_div, "$g_average_center_value_per_faction", ":num_factions"),
        #     ]),
        
        # script_remove_cattles_if_herd_is_close_to_party
        # Input: arg1 = party_no, arg2 = maximum_number_of_cattles_required
        # Output: reg0 = number_of_cattles_removed
        ("remove_cattles_if_herd_is_close_to_party",
          [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":max_req", 2),
            (assign, ":cur_req", ":max_req"),
            (try_for_parties, ":cur_party"),
              (gt, ":cur_req", 0),
              (party_slot_eq, ":cur_party", slot_party_type, spt_cattle_herd),
              (store_distance_to_party_from_party, ":dist", ":cur_party", ":party_no"),
              (lt, ":dist", 3),
              
              #Do not use the quest herd for "move cattle herd"
              (assign, ":subcontinue", 1),
              (try_begin),
                (check_quest_active, "qst_move_cattle_herd"),
                (quest_slot_eq, "qst_move_cattle_herd", slot_quest_target_party, ":cur_party"),
                (assign, ":subcontinue", 0),
              (try_end),
              (eq, ":subcontinue", 1),
              #Do not use the quest herd for "move cattle herd" ends
              
              (party_count_companions_of_type, ":num_cattle", ":cur_party", "trp_cattle"),
              (try_begin),
                (le, ":num_cattle", ":cur_req"),
                (assign, ":num_added", ":num_cattle"),
                (remove_party, ":cur_party"),
              (else_try),
                (assign, ":num_added", ":cur_req"),
                (party_remove_members, ":cur_party", "trp_cattle", ":cur_req"),
              (try_end),
              (val_sub, ":cur_req", ":num_added"),
              
              
              (try_begin),
                (party_slot_eq, ":party_no", slot_party_type, spt_village),
                (party_get_slot, ":village_cattle_amount", ":party_no", slot_village_number_of_cattle),
                (val_add, ":village_cattle_amount", ":num_added"),
                (party_set_slot, ":party_no", slot_village_number_of_cattle, ":village_cattle_amount"),
              (try_end),
              
              (assign, reg3, ":num_added"),
              (str_store_party_name_link, s1, ":party_no"),
              (display_message, "@You brought {reg3} heads of cattle to {s1}."),
              (try_begin),
                (gt, "$cheat_mode", 0),
                (assign, reg4, ":village_cattle_amount"),
                (display_message, "@{!}Village now has {reg4}"),
              (try_end),
            (try_end),
            (store_sub, reg0, ":max_req", ":cur_req"),
        ]),
        
        # script_get_rumor_to_s61
        # Input: rumor_id
        # Output: reg0 = 1 if rumor found, 0 otherwise; s61 will contain rumor string if found
        ("get_rumor_to_s61",
          [
            (store_script_param, ":base_rumor_id", 1), # the script returns the same rumor for the same rumor id, so that one cannot hear all rumors by
            # speaking to a single person.
            
			 ##diplomacy start+ save reg4 in order to revert it at the end of the script
			 (assign, ":save_reg4", reg4),
			 ##diplomacy end+
			 (store_current_hours, ":cur_hours"),
			 (store_div, ":cur_day", ":cur_hours", 24),
			 (assign, ":rumor_found", 0),
			 (assign, ":num_tries", 3),
			 (try_for_range, ":try_no", 0, ":num_tries"),
			   (store_mul, ":rumor_id", ":try_no", 6781),
			   (val_add, ":rumor_id", ":base_rumor_id"),
			   (store_mod, ":rumor_type", ":rumor_id", 7),
			   (val_add, ":rumor_id", ":cur_hours"),
			   (try_begin),
				 (eq,  ":rumor_type", 0),
				 (try_begin),
				   (store_sub, ":range", towns_end, towns_begin),
				   (store_mod, ":random_center", ":rumor_id", ":range"),
				   (val_add, ":random_center", towns_begin),
				   (party_slot_ge, ":random_center", slot_town_has_tournament, 1),
				   (neq, ":random_center", "$current_town"),
				   (str_store_party_name, s62, ":random_center"),
				   (str_store_string, s61, "@I heard that there will be a tournament in {s62} soon."),
				   (assign, ":rumor_found", 1),
				 (try_end),
			   (else_try),
				 (eq,  ":rumor_type", 1),
				 (try_begin),
				   (store_sub, ":range", active_npcs_end, original_kingdom_heroes_begin), #was reversed
				   (store_mod, ":random_hero", ":rumor_id", ":range"),
				   (val_add, ":random_hero", original_kingdom_heroes_begin),
				   (is_between, ":random_hero", active_npcs_begin, active_npcs_end),
				   (troop_get_slot, ":personality", ":random_hero", slot_lord_reputation_type),
				   ##diplomacy start+ give rumors for non-noble personalities, and make pronouns gender-correct
				   (try_begin),
					  (ge, ":personality", lrep_roguish),
					  (try_begin),
						(eq, ":personality", lrep_benefactor),#Ymira, Bunduk, Jeremus
						(assign, ":personality", lrep_goodnatured),#treats people living in his lands decently
					  (else_try),
						(eq, ":personality", lrep_custodian),#Marnid, Artimenner, Deshavi, Katrin
						(assign, ":personality", lrep_goodnatured),#good to his followers, and rewards them if they work well
					  (else_try),
						(call_script, "script_dplmc_get_troop_morality_value", ":random_hero", tmt_humanitarian),
						(lt, reg0, 0),#Klethi
						(assign, ":personality", lrep_debauched),#likes to torture his enemies
					  (try_end),
					  (ge, ":personality", lrep_roguish),
					  (assign, ":personality", 0),#zero out to avoid jumping to a nonsensical string
				   (try_end),
				   (call_script, "script_dplmc_store_troop_is_female_reg", ":random_hero", 4),#store gender to reg4 to make pronouns gender-correct
				   ##diplomacy end+
				   (gt, ":personality", 0),
				   (store_add, ":rumor_string", ":personality", "str_gossip_about_character_default"),
				   (str_store_troop_name, s6, ":random_hero"),
				   (str_store_string, s61, ":rumor_string"),
				   (assign, ":rumor_found", 1),
				 (try_end),
				 ##diplomacy start+ Change the rumor string in some circumstances to avoid implying the hero is currently ruling a fief
				 (try_begin),
				   (neg|is_between, ":random_hero", heroes_begin, heroes_end),
				 (else_try),
				   #Dead
				   (troop_slot_eq, ":random_hero", slot_troop_occupation, dplmc_slto_dead),
				   (str_store_troop_name, s6, ":random_hero"),
				   (str_store_string, s61, "@I heard some people say they don't believe {s6} is really dead."),#The doubters are wrong, like with Tupac or Elvis.
				   (assign, ":rumor_found", 1),
				 (else_try),
				   #In exile
				   (this_or_next|troop_slot_eq, ":random_hero", slot_troop_occupation, slto_retirement),
				   (troop_slot_eq, ":random_hero", slot_troop_occupation, dplmc_slto_exile),
				   (str_store_troop_name, s6, ":random_hero"),
				   (str_store_string, s61, "@I heard a traveller say that he came across {s6} while journeying outside these lands."),
				   (assign, ":rumor_found", 1),
				 (else_try),
				   #Inactive pretender
				   (troop_slot_eq, ":random_hero", slot_troop_occupation, slto_inactive_pretender),
				   (neq, ":random_hero", "$supported_pretender"),
				   (troop_get_slot, reg4, ":random_hero", slot_troop_original_faction),
				   (is_between, reg4, npc_kingdoms_begin, npc_kingdoms_end),
				   (faction_slot_eq, reg4, slot_faction_state, sfs_active),
				   (faction_get_slot, reg4, reg4, slot_faction_leader),
				   (gt, reg4, -1),
				   (str_store_troop_name, s61, reg4),
				   (str_store_string, s6, ":random_hero"),
				   (str_store_string, s61, "@I heard that {s6} intends to raise an army and seize the throne from {s61}."),
				   (assign, ":rumor_found", 1),
				 (try_end),
				 ##diplomacy end+				 
			   (else_try),
				 (eq,  ":rumor_type", 2),
				 (try_begin),
				   (store_sub, ":range", trade_goods_end, trade_goods_begin),
				   (store_add, ":random_trade_good", ":rumor_id", ":cur_day"),
				   (store_mod, ":random_trade_good", ":random_trade_good", ":range"),
				   (store_add, ":random_trade_good_slot", ":random_trade_good", slot_town_trade_good_prices_begin),
				   (val_add, ":random_trade_good", trade_goods_begin),
				   (store_mul, ":min_price", average_price_factor, 3),
				   (val_div, ":min_price", 4),
				   (assign, ":min_price_center", -1),
				   (try_for_range, ":sub_try_no", 0, 10),
					 (store_sub, ":range", towns_end, towns_begin),
					 (store_add, ":center_rumor_id", ":rumor_id", ":sub_try_no"),
					 (store_mod, ":random_center", ":center_rumor_id", ":range"),
					 (val_add, ":random_center", towns_begin),
					 (neq, ":random_center", "$g_encountered_party"),
					 (party_get_slot, ":cur_price", ":random_center", ":random_trade_good_slot"),
					 (lt, ":cur_price", ":min_price"),
					 (assign, ":min_price", ":cur_price"),
					 (assign, ":min_price_center", ":random_center"),
				   (try_end),
				   (ge, ":min_price_center", 0),
				   (str_store_item_name, s62, ":random_trade_good"),
				   (str_store_party_name, s63, ":min_price_center"),
				   (str_store_string, s61, "@I heard that one can buy {s62} very cheap at {s63}."),
				   (assign, ":rumor_found", 1),
				 (try_end),
			   (else_try),
				 (eq,  ":rumor_type", 3),
				 (try_begin),
				   (store_sub, ":range", trade_goods_end, trade_goods_begin),
				   (store_add, ":random_trade_good", ":rumor_id", ":cur_day"),
				   (store_mod, ":random_trade_good", ":random_trade_good", ":range"),
				   (store_add, ":random_trade_good_slot", ":random_trade_good", slot_town_trade_good_prices_begin),
				   (val_add, ":random_trade_good", trade_goods_begin),
				   (store_mul, ":max_price", average_price_factor, 5),
				   (val_div, ":max_price", 4),
				   (assign, ":max_price_center", -1),
				   (try_for_range, ":sub_try_no", 0, 10),
					 (store_sub, ":range", towns_end, towns_begin),
					 (store_add, ":center_rumor_id", ":rumor_id", ":sub_try_no"),
					 (store_mod, ":random_center", ":center_rumor_id", ":range"),
					 (val_add, ":random_center", towns_begin),
					 (neq, ":random_center", "$g_encountered_party"),
					 (party_get_slot, ":cur_price", ":random_center", ":random_trade_good_slot"),
					 (gt, ":cur_price", ":max_price"),
					 (assign, ":max_price", ":cur_price"),
					 (assign, ":max_price_center", ":random_center"),
				   (try_end),
				   (ge, ":max_price_center", 0),
				   (str_store_item_name, s62, ":random_trade_good"),
				   (str_store_party_name, s63, ":max_price_center"),
				   (str_store_string, s61, "@I heard that they pay a very high price for {s62} at {s63}."),
				   (assign, ":rumor_found", 1),
				 (try_end),
			   (try_end),
			   (try_begin),
				 (gt, ":rumor_found", 0),
				 (assign, ":num_tries", 0),
			   (try_end),
			 (try_end),
			 (assign, reg0, ":rumor_found"),
			 ##diplomacy start+ revert reg4
			 (assign, reg4, ":save_reg4"),
			 ##diplomacy end+
		 ]),
        
        ("lord_comment_to_s43",
          [(store_script_param, ":lord", 1),
            (store_script_param, ":default_string", 2),
            
            (troop_get_slot,":reputation", ":lord", slot_lord_reputation_type),
            
            (try_begin),
			#some default strings will have added comments for the added commons reputation types
			##diplomacy start+
			(try_begin),
			#Don't reassign personalities of lords
				(is_between, ":reputation", lrep_none, lrep_upstanding + 1),
				(else_try),
			#Special case for anti-humanitarians (Klethi in Native)
				(neg|is_between, ":reputation", lrep_none, lrep_upstanding + 1),
					(neq, ":reputation", lrep_benefactor),
					(neq, ":reputation", lrep_moralist),
					(neq, ":reputation", lrep_conventional),
				(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_humanitarian),
					(lt, reg0, 0),#<- In Native, this only applies to Klethi
				#Use lrep_debauched by default, and refine further below.
				(assign, ":reputation", lrep_debauched),
				(try_begin),
				#If pious, anti-humanitarians use lrep_selfrighteous
					(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_pious),
				(ge, reg0, 1),#<- Describes no one in Native
				(assign, ":reputation", lrep_selfrighteous),
				(else_try),
				#If aggressive, anti-humanitarians use lrep_quarrelsome
					(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_aristocratic),
				(this_or_next|eq, ":reputation", lrep_adventurous),
					(ge, reg0, 1),#<- In Native describes Alayen, Matheld, Rolf, Nizar, Lezalit, Klethi (but only Klethi can even reach here)
				(assign, ":reputation", lrep_quarrelsome),
				(try_end),
			(else_try),
			#Special case for "pious" characters (no one in Native)
				(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_pious),
				(ge, reg0, 1),
				(try_begin),
					#Handle these separately to prevent inappropriate reassignment
					(this_or_next|eq, ":reputation", lrep_benefactor),
						(eq, ":reputation", lrep_moralist),
					(assign, ":reputation", lrep_upstanding),
				(else_try),
					#Ordinarily upstanding
					(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_humanitarian),
					(ge, reg0, 0),#<- In Native describes all but Klethi
					(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_egalitarian),
					(ge, reg0, 0),#<- In Native describes all but Lezalit
					(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_honest),
					(ge, reg0, 0),#<- In Native describes all but Rolf
					(assign, ":reputation", lrep_upstanding),
					(else_try),
					#If vicious, self-righteous is also a possibility
						(assign, ":reputation", lrep_selfrighteous),
					(try_end),
			(else_try),
			#Special case for dishonest commoners.
			#Pragmatic-style amoral: lrep_cunning
			#Jerk-style amoral: lrep_debauched
				(neg|is_between, ":reputation", lrep_none, lrep_upstanding + 1),
						(neq, ":reputation", lrep_moralist),
						(neq, ":reputation", lrep_benefactor),
				(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_honest),
				(lt, reg0, 0),#<- In Native only describes Rolf (who wouldn't reach here, since he is lrep_cunning)
				(try_begin),
					(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_egalitarian),
					(lt, reg0, 1),
					(assign, ":egalitarian", reg0),
					(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_humanitarian),
					(lt, reg0, 1),
					(this_or_next|lt, reg0, 0),
						(lt, ":egalitarian", 0),
					(assign, ":reputation", lrep_debauched),
				(else_try),
					(assign, ":reputation", lrep_cunning),
				(try_end),
			(else_try),
				(eq, ":reputation", lrep_roguish),
				(assign, ":reputation", lrep_goodnatured),
			(else_try),
				(eq, ":reputation", lrep_custodian),
				(assign, ":reputation", lrep_cunning),
			(else_try),
				(eq, ":reputation", lrep_benefactor),
				(assign, ":reputation", lrep_goodnatured),
			#add support for lady personalities
			(else_try),
				(eq, ":reputation", lrep_ambitious),
				(assign, ":reputation", lrep_cunning),
		(else_try),
			(this_or_next|eq, ":reputation", lrep_conventional),
				(eq, ":reputation", lrep_otherworldly),
			(assign, ":reputation", lrep_goodnatured),
		(else_try),
			(eq, ":reputation", lrep_adventurous),
			(assign, ":reputation", lrep_martial),
			(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_egalitarian),
			(try_begin),
				(lt, reg0, 0),#<- In Native describes no one
				(assign, ":reputation", lrep_quarrelsome),
			(try_end),
		(else_try),
			(eq, ":reputation", lrep_moralist),
			(assign, ":reputation", lrep_upstanding),
		(try_end),
		##diplomacy end+

		##diplomacy start+ Add some variability
		#For non-companion, non-monarchs who don't have any tmt_* morality values, this
		# just amounts to a 5% chance to use lrep_none instead of their real reputation
		# (except where that would cause problems).
		#Otherwise,
		# 16,17:
		#   tmt_pious > 0, with lrep_debauched or lrep_quarrelsome or lrep_selfrighteous: lrep_selfrighteous
		#   tmt_pious > 0, with one of (tmt_egalitarian, tmt_honest, tmt_humanitarian) < 0 and none > 0: lrep_selfrighteous
		#   (tmt_pious >= 0 and tmt_honest >= 0) and (tmt_pious > 0 or tmt_honest > 0): lrep_upstanding
		#   tmt_honest < 0: lrep_cunning
		#   lrep_none and is a king or pretender: lrep_cunning
		#   
		# 18,19:
		#   tmt_aristocratic > 0, with lrep_debauched or lrep_quarrelsome: lrep_quarrelsome
		#   lrep_martial, with (tmt_honest, tmt_egalitarian, tmt_humanitarian) all non-positive and
		#      at least one negative, and tmt_pious < 1 (so not to overlap with 16,17): lrep_quarrelsome
		#   tmt_aristocratic > 0: lrep_martial
		#   lrep_none and is a king or pretender: lrep_martial
		(store_random_in_range, ":random_chance", 0, 20),
		(assign, ":new_reputation", ":reputation"),
		(try_begin),
			(eq, 1, 1),#Disable this feature for now.
		(else_try),
			#Disable the first time you're talking to someone, or if you haven't
			#spoken to this NPC recently.
			(store_current_hours, ":recently"),
			(val_sub, ":recently", 24),
			(this_or_next|neq, "$g_talk_troop_met", 1),
			(this_or_next|neg|troop_slot_ge, ":lord", slot_troop_met, 1),
			(this_or_next|neg|troop_slot_ge, ":lord", slot_troop_last_talk_time, ":recently"),
			#Disable for things that come in sequences
			(this_or_next|eq, ":default_string", "str_rebellion_dilemma_default"),
				(eq, ":default_string", "str_rebellion_dilemma_2_default"),
			#Set this value to signal to the debug message at the end
			(assign, ":random_chance", -1),
		(else_try),
			#10% chance of lrep_martial or lrep_quarrelsome if appropriate...
			#if already lrep_martial, check separately here for possible conversion
			#to lrep_quarrelsome
			(is_between, ":random_chance", 18, 20),
			(eq, ":reputation", lrep_martial),
			(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_egalitarian),
			(lt, reg0, 1),
			(assign, ":bad_sum", reg0),
			(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_humanitarian),
			(lt, reg0, 1),
			(val_add, ":bad_sum", reg0),
			(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_honest),
			(lt, reg0, 1),
			(val_add, ":bad_sum", reg0),
			#at least one of tmt_egalitarian, tmt_humanitarian, and tmt_honest were negative (and none were positive)
			(lt, ":bad_sum", 0),
			#disable for positive tmt_pious, since that's handled separately as an alternative to lrep_upstanding for [16,17]
			(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_honest),
			(lt, reg0, 1),
			(assign, ":new_reputation", lrep_quarrelsome),
			(else_try),
			#10% chance of lrep_martial or lrep_quarrelsome if appropriate
			#Applies to: Rolf, Nizar, Lezalit, Klethi
			#(Also Alayen and Matheld, but they are already lrep_martial)
			(is_between, ":random_chance", 18, 20),
			(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_aristocratic),
			(ge, reg0, 1),
			(try_begin),
				#some personalities use lrep_quarrelsome (only Klethi in Native)
				(this_or_next|eq, ":reputation", lrep_debauched),
					(eq, ":reputation", lrep_quarrelsome),#<-- i.e. no change
				(assign, ":new_reputation", lrep_quarrelsome),
			(else_try),
				#other personalities use lrep_martial
					(assign, ":new_reputation", lrep_martial),
			(try_end),
		(else_try),
			#10% chance of lrep_upstanding or lrep_selfrighteous if appropriate
			#Applies to: Marnid, Alayen, Artimenner
			#(Also Firentis, but he is already lrep_upstanding)
			(is_between, ":random_chance", 16, 18),
			(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_honest),
			(assign, ":honest", reg0),
			(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_pious),
			(assign, ":pious", reg0),
			(this_or_next|ge, ":honest", 1),#one or the other must be greater than zero
				(ge, ":pious", 1),
			(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_egalitarian),
			(assign, ":egalitarian", reg0),
			(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_humanitarian),
			(assign, ":humanitarian", reg0),
			(try_begin),
				#Unpleasant personalities use "selfrighteous" instead
				#(Applies to no one in Native)
				(this_or_next|eq, ":reputation", lrep_debauched),
				(this_or_next|eq, ":reputation", lrep_quarrelsome),
				(this_or_next|eq, ":reputation", lrep_selfrighteous),#<- i.e. no change
				(this_or_next|lt, ":honest", 0),
				(this_or_next|lt, ":egalitarian", 0),
					(lt, ":humanitarian", 0),
				(assign, ":new_reputation", lrep_selfrighteous),
			(else_try),
				#Other personalities use upstanding
				(assign, ":new_reputation", lrep_upstanding),
			(try_end),
		(else_try),
			#10% chance of lrep_cunning if appropriate
			(is_between, ":random_chance", 16, 18),
			(lt, ":honest", 0),#<- In Native only Rolf satisfies this, but he is already lrep_cunning
			(assign, ":reputation", lrep_cunning),
		(else_try),
			#Ruler, if personality triggers not met: 10% cunning, 10% martial
			(is_between, ":random_chance", 16, 20),
			(eq, ":reputation", lrep_none),
			(this_or_next|is_between, ":lord", kings_begin, kings_end),
				(is_between, ":lord", pretenders_begin, pretenders_end),
			(try_begin),
				(is_between, ":random_chance", 16, 18),
				(assign, ":new_reputation", lrep_cunning),
			(else_try),
				(is_between, ":random_chance", 18, 20),
				(call_script, "script_dplmc_get_troop_morality_value", ":lord", tmt_aristocratic),
				(ge, reg0, 0),#Won't reach here if positive, so you could just check if it equals zero
				(assign, ":new_reputation", lrep_martial),
			(try_end),
		(else_try),
			#Others, if personality triggers not met: 5% chance of null
			(is_between, ":random_chance", 16, 20),#base 20%
			(store_mod, ":rand_mod", ":random_chance",4),
			(troop_get_slot, reg0, ":lord", slot_troop_temp_decision_seed),
			(val_mod, reg0, 4),
			(eq, ":rand_mod", reg0),#1/4 of the time, 5%
			#disable for things that don't have a "lrep_none" version defined
			(neq, ":default_string", "str_rebellion_dilemma_default"),
			(neq, ":default_string", "str_rebellion_dilemma_2_default"),
			(neq, ":default_string", "str_changed_my_mind_default"),
			(neq, ":default_string", "str_political_philosophy_default"),
			(neq, ":default_string", "str_rebellion_rival_default"),
			(neq, ":default_string", "str_rebellion_agree_default"),
			(neq, ":default_string", "str_rebellion_refuse_default"),
			(neq, ":default_string", "str_talk_later_default"),
			(neq, ":default_string", "str_npc_claim_throne_liege"),
			#use lrep_none
			(assign, ":new_reputation", lrep_none),
		(try_end),
		(try_begin),
			(eq, 1, 0),#Disable this feature for now.
			(ge, "$cheat_mode", 1),
			(assign, ":save_reg1", reg1),
			(assign, ":save_reg2", reg2),
			(assign, reg0, ":random_chance"),
			(assign, reg1, ":reputation"),
			(assign, reg2, ":new_reputation"),
			(try_begin),
				(neq, ":reputation", ":new_reputation"),
				(display_message, "@{!} DEBUG - random {reg0} (0 to 20), used reputation {reg2} instead of {reg1}"),
			(else_try),
				(lt, ":random_chance", 0),
				(display_message, "@{!} DEBUG - variable responses disabled, kept reputation {reg2}"),
			(else_try),
				(display_message, "@{!} DEBUG - random {reg0} (0 to 20), kept reputation {reg2}"),
			(try_end),
			(assign, reg1, ":save_reg1"),
			(assign, reg2, ":save_reg2"),
		(try_end),
		(assign, ":reputation", ":new_reputation"),
		##diplomacy end+

		(store_add, ":result", ":reputation", ":default_string"),

		(str_store_string, 43, ":result"),
		(assign, reg0, ":result"),


		]),
        
        #Troop Commentaries begin
        
        # script_add_log_entry
        # Input: arg1 = entry_type, arg2 = event_actor, arg3 = center_object, arg4 = troop_object, arg5 = faction_object
        # Output: none
        ("add_log_entry",
          [(store_script_param, ":entry_type", 1),
            (store_script_param, ":actor", 2),
            (store_script_param, ":center_object", 3),
            (store_script_param, ":troop_object", 4),
            (store_script_param, ":faction_object", 5),
            (assign, ":center_object_lord", -1),
            (assign, ":center_object_faction", -1),
            (assign, ":troop_object_faction", -1),
            
            (try_begin),
              (party_is_active, ":center_object", 0),
              (party_get_slot, ":center_object_lord", ":center_object", slot_town_lord),
              (store_faction_of_party, ":center_object_faction", ":center_object"),
            (else_try),
              (assign, ":center_object_lord", 0),
              (assign, ":center_object_faction", 0),
            (try_end),
            
            (try_begin),
              (is_between, ":troop_object", 0, "trp_local_merchant"),
              (store_troop_faction, ":troop_object_faction", ":troop_object"),
            (else_try),
              (assign, ":troop_object_faction", 0),
            (try_end),
            
            (val_add, "$num_log_entries", 1),
            
            (store_current_hours, ":entry_time"),
            (troop_set_slot, "trp_log_array_entry_type",            "$num_log_entries", ":entry_type"),
            (troop_set_slot, "trp_log_array_entry_time",            "$num_log_entries", ":entry_time"),
            (troop_set_slot, "trp_log_array_actor",                 "$num_log_entries", ":actor"),
            (troop_set_slot, "trp_log_array_center_object",         "$num_log_entries", ":center_object"),
            (troop_set_slot, "trp_log_array_center_object_lord",    "$num_log_entries", ":center_object_lord"),
            (troop_set_slot, "trp_log_array_center_object_faction", "$num_log_entries", ":center_object_faction"),
            (troop_set_slot, "trp_log_array_troop_object",          "$num_log_entries", ":troop_object"),
            (troop_set_slot, "trp_log_array_troop_object_faction",  "$num_log_entries", ":troop_object_faction"),
            (troop_set_slot, "trp_log_array_faction_object",        "$num_log_entries", ":faction_object"),
            
            (try_begin),
              (eq, "$cheat_mode", 1),
              (assign, reg3, "$num_log_entries"),
              (assign, reg4, ":entry_type"),
              (display_message, "@{!}Log entry {reg3}: type {reg4}"),
              (try_begin),
                (gt, ":center_object", 0),
                (neq, ":entry_type", logent_traveller_attacked),
                (neq, ":entry_type", logent_party_traded),
                (party_is_active, ":center_object"), #sometimes is a troop
                
                (str_store_party_name, s4, ":center_object"),
                (display_message, "@{!}Center: {s4}"),
              (try_end),
              (try_begin),
                (gt, ":troop_object", 0),
                (neq, ":entry_type", logent_traveller_attacked),
                (neq, ":entry_type", logent_party_traded),
                
                (str_store_troop_name, s4, ":troop_object"),
                (display_message, "@{!}Troop: {s4}"),
              (try_end),
              (try_begin),
                (gt, ":center_object_lord", 0),
                (neq, ":entry_type", logent_traveller_attacked),
                (neq, ":entry_type", logent_party_traded),
                
                (str_store_troop_name, s4, ":center_object_lord"),
                (display_message, "@{!}Lord: {s4}"),
              (try_end),
            (try_end),
            
            
            (try_begin),
              (this_or_next|eq, ":entry_type", logent_lord_defeated_by_player),
              (this_or_next|eq, ":entry_type", logent_player_participated_in_major_battle),
              (eq, ":entry_type", logent_player_participated_in_siege),
              
              (try_begin),
                (eq, "$cheat_mode", 1),
                (display_message, "@{!}Ally party is present"),
              (try_end),
				##diplomacy start+ support kingdom ladies as well
				#(try_for_range, ":hero", active_npcs_begin, active_npcs_end),
				(try_for_range, ":hero", heroes_begin, heroes_end),
					(this_or_next|is_between, ":hero", active_npcs_begin, active_npcs_end),
					(this_or_next|troop_slot_eq, ":hero", slot_troop_occupation, slto_kingdom_hero),
					(this_or_next|troop_slot_eq, ":hero", slot_troop_occupation, slto_player_companion),
					(troop_slot_eq, ":hero", slot_troop_occupation, slto_kingdom_seneschal),
				##diplomacy end+
					(party_count_companions_of_type, ":hero_present", "p_collective_friends", ":hero"),
					(gt, ":hero_present", 0),
					(troop_set_slot, ":hero", slot_troop_present_at_event, "$num_log_entries"),
					(call_script, "script_post_combat_relation_changes", ":hero", 1),
					#         (store_sub, ":skip_up_to_here", "$num_log_entries", 1),
					#         (troop_set_slot, ":hero", slot_troop_last_comment_slot, ":skip_up_to_here"),
					(try_begin),
						(eq, "$cheat_mode", 1),
						(str_store_troop_name, s4, ":hero"),
						(display_message, "@{!}{s4} is present at event"),
					(try_end),
				(try_end),
            (try_end),
        ]),
        
        
        # script_get_relevant_comment_for_log_entry
        # Input: arg1 = log_entry_no,
        # Output: reg0 = comment_id; reg1 = relevance
        # Notes: 50 is the default relevance.
        # A comment with relevance less than 30 will always be skipped.
        # A comment with relevance 75 or more will never be skipped.
        # A comment with relevance 50 has about 50% chance to be skipped.
        # If there is more than one comment that is not skipped, the system will randomize their relevance values, and then choose the highest one.
	  # Also note that the relevance of events decreases as time passes. After three months, relevance reduces to 50%, after 6 months, 25%, etc...
	  ##diplomacy start+
	  ##May also set reg4 or reg3 to correspond to gender
	  ##diplomac end+
        ("get_relevant_comment_for_log_entry",
          [(store_script_param, ":log_entry_no", 1),
            
            (troop_get_slot, ":entry_type",            "trp_log_array_entry_type",            ":log_entry_no"),
            (troop_get_slot, ":entry_time",            "trp_log_array_entry_time",            ":log_entry_no"),
            (troop_get_slot, ":actor",                 "trp_log_array_actor",                 ":log_entry_no"),
            (troop_get_slot, ":center_object",         "trp_log_array_center_object",         ":log_entry_no"),
            (troop_get_slot, ":center_object_lord",    "trp_log_array_center_object_lord",    ":log_entry_no"),
            (troop_get_slot, ":center_object_faction", "trp_log_array_center_object_faction", ":log_entry_no"),
            (troop_get_slot, ":troop_object",          "trp_log_array_troop_object",          ":log_entry_no"),
            (troop_get_slot, ":troop_object_faction",  "trp_log_array_troop_object_faction",  ":log_entry_no"),
            (troop_get_slot, ":faction_object",        "trp_log_array_faction_object",        ":log_entry_no"),
            
            (assign, ":relevance", 0),
            (assign, ":comment", -1),
            (assign, ":rejoinder", -1),
            (assign, ":suggested_relation_change", 0),
            
			 (troop_get_slot, ":reputation", "$g_talk_troop", slot_lord_reputation_type),
			 ##diplomacy start+
			 (assign, ":return_reg4", reg4),
			 #Set an initial value for ":return_reg4", although further down
			 #some specific log types override this.
			 (try_begin),
				(is_between, ":troop_object", heroes_begin, heroes_end),
				(neq, ":troop_object", "$g_talk_troop"),
				(assign, ":return_reg4", 0),
				(try_begin),
					(call_script, "script_cf_dplmc_troop_is_female", ":troop_object"),
					(assign, ":return_reg4", 1),
				(try_end),
			 (else_try),
				(is_between, ":actor", heroes_begin, heroes_end),
				(neq, ":actor", "$g_talk_troop"),
				(assign, ":return_reg4", 0),
				(try_begin),
					(call_script, "script_cf_dplmc_troop_is_female", ":actor"),
					(assign, ":return_reg4", 1),
				(try_end),
			 (try_end),
			 
			 
			 #add support for commoner/lady reputations
			 (troop_get_slot, ":true_reputation", "$g_talk_troop", slot_lord_reputation_type),#unmodified value
			 #(troop_get_type, ":talk_troop_gender",  "$g_talk_troop"),
			 (call_script, "script_dplmc_store_troop_is_female", "$g_talk_troop"),
			 (assign, ":talk_troop_gender", reg0),
			 (try_begin),
				(neg|is_between, ":reputation", lrep_none, lrep_upstanding + 1),#<-- no changes are required for standard lord personalities
				(try_begin),
					(eq, ":true_reputation", lrep_ambitious),
					(assign, ":reputation", lrep_cunning),
				(else_try),
					(eq, ":true_reputation", lrep_moralist),
					(assign, ":reputation", lrep_upstanding),
				(else_try),
					(this_or_next|eq, ":true_reputation", lrep_conventional),
					   (this_or_next|eq, ":true_reputation", lrep_otherworldly),
					   (eq, ":true_reputation", lrep_benefactor),
					(assign, ":reputation", lrep_goodnatured),
				(try_end),
			 (try_end),
			 ##diplomacy end+
			 (store_current_hours, ":current_time"),
            (store_sub, ":entry_hours_elapsed", ":current_time", ":entry_time"),
            
            #Post 0907 changes begin
            (assign, ":players_kingdom_relation", 0), ##the below is so that lords will not congratulate player on attacking neutrals
            (try_begin),
              (gt, "$players_kingdom", 0),
              (store_relation, ":players_kingdom_relation", "$players_kingdom", ":troop_object_faction"),
            (try_end),
            
            (try_begin),
              (eq, "$cheat_mode", -1), #temporarily disabled
              (try_begin),
                (assign, reg5, ":log_entry_no"),
                (assign, reg6, ":entry_type"),
                (assign, reg8, ":entry_time"),
                
                (gt, "$players_kingdom", 0),
                (try_begin),
                  (gt, ":troop_object_faction", 0),
                  (assign, reg7, ":players_kingdom_relation"),
                  (display_message, "@{!}Event #{reg5}, type {reg6}, time {reg8}: player's kingdom relation to troop object = {reg7}"),
                  (else_try),
                    (gt, ":center_object_faction", 0),
                    (assign, reg7, ":players_kingdom_relation"),
                    (display_message, "@{!}Event #{reg5}, type {reg6}, time {reg8}: player's kingdom relation to center object faction = {reg7}"),
                    (else_try),
                      (gt, ":faction_object", 0),
                      (assign, reg7, ":players_kingdom_relation"),
                      (display_message, "@{!}Event #{reg5}, type {reg6}, time {reg8}: player's kingdom relation to faction object = {reg7}"),
                      (else_try),
                        (display_message, "@{!}Event #{reg5}, type {reg6}, time {reg8}. No relevant kingdom relation"),
                        (try_end),
                      (else_try),
                        (display_message, "@{!}Event #{reg5}, type {reg6}, time {reg8}. Player unaffiliated"),
                        (try_end),
                      (try_end),
                      
					 ##diplomacy start+
					 #In Native, it's assumed that anyone with lrep_none is a liege, but that isn't alwasys true.
					 #(For example, it's possible in a Native game for a defeated pretender to end up as the vassal
					 #of an NPC lord (!), but still talk as if they're ruling a kingdom.)
					 #  Instead of just relying on personality for this, explicily check if they're a liege.
					 (call_script, "script_dplmc_get_troop_standing_in_faction", "$g_talk_troop", "$g_talk_troop_faction"),
					 (try_begin),		 
						 (ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
						 (assign, ":speaker_is_a_liege", 1),
					 (else_try),
						 (assign, ":speaker_is_a_liege", 0),
					 (try_end),
					 ##diplomacy end+
					 (try_begin),
					   (eq, ":entry_type", logent_game_start),
					   (eq, "$g_talk_troop_met", 0),
					   (is_between, "$g_talk_troop_faction_relation", -5, 5),
					   (is_between, "$g_talk_troop_relation", -5, 5),

					   (assign, ":relevance", 25),
					   (troop_get_slot, ":plyr_renown", "trp_player", slot_troop_renown),
						##diplomacy start+
						(try_begin),
							(lt, "$g_disable_condescending_comments", 0),#prejudice mode: high
							(call_script, "script_cf_dplmc_faction_has_bias_against_gender", "$g_talk_troop_faction", "$character_gender"),#bias against gender			
							#80% renown
							(val_mul, ":plyr_renown", 4),
							(val_add, ":plyr_renown", 3),
							(val_div, ":plyr_renown", 5),
						(try_end),
						##diplomacy end+
                        #normal_banner_begin
                        (troop_get_slot, ":banner", "trp_player", slot_troop_banner_scene_prop),
                        #custom_banner_begin
                        #       (troop_get_slot, ":banner", "trp_player", slot_troop_custom_banner_flag_type),
					   (store_random_in_range, ":renown_check", 100, 200),
					   (try_begin),
						  ##diplomacy start+
						  (gt, ":speaker_is_a_liege", 0),#Explicitly check if the speaker is a liege rather than relying solely on reputation
						  ##diplomacy end+
						  (eq, ":reputation", lrep_none),
						  (gt, "$players_kingdom", 0),
						  (assign, ":comment", "str_comment_intro_liege_affiliated"),
						  (try_begin),
							(faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
							(assign, ":comment", "str_comment_intro_liege_affiliated_to_player"),
						  (try_end),
					   (else_try),
						  ##diplomacy start+
						  ##OLD:
						  #(eq, "$character_gender",tf_female),
						  ##NEW:
						  #Instead of assuming there's anti-female bias in all settings, check on a kingdom-by-kingdom basis.
						  (call_script, "script_cf_dplmc_faction_has_bias_against_gender", "$g_talk_troop_faction", "$character_gender"),
						  ##diplomacy end+
						  
						  (call_script, "script_troop_get_romantic_chemistry_with_troop", "$g_talk_troop", "trp_player"),
						  (assign, ":attraction", reg0),
						  (store_random_in_range, ":random", 0, 2),
						  (this_or_next|eq, ":random", 0),
							  (gt, ":attraction", 10),
						  ##diplomacy start+ disable remarks about women if the speaker is a woman (or visa versa, for settings with biases against men)
						  (this_or_next|gt, ":attraction", 10),
							(neq, ":talk_troop_gender", "$character_gender"),
						  ##diplomacy end+
						  (try_begin),
							(this_or_next|gt, ":plyr_renown", ":renown_check"),
							##diplomacy start+
							#	(eq, "$g_disable_condescending_comments", 1),
								(ge, "$g_disable_condescending_comments", 1),
							##diplomacy end+
							(assign, ":comment", "str_comment_intro_female_famous_liege"),
							(val_add, ":comment", ":reputation"),
						  (else_try),
							(ge, ":attraction", 9),
							(assign, ":comment", "str_comment_intro_female_admiring_liege"),
							(val_add, ":comment", ":reputation"),
						  (else_try),
							(gt, ":banner", 0),
							(assign, ":comment", "str_comment_intro_female_noble_liege"),
							(val_add, ":comment", ":reputation"),
						  (else_try),
							(assign, ":comment", "str_comment_intro_female_common_liege"),
							(val_add, ":comment", ":reputation"),
						  (try_end),

						  #Rejoinders for comments
						  (try_begin),
							(eq, ":comment", "str_comment_intro_female_common_badtempered"),
							(assign, ":rejoinder", "str_rejoinder_intro_female_common_badtempered"),
						  (else_try),
							(eq, ":comment", "str_comment_intro_female_noble_pitiless"),
							(assign, ":rejoinder", "str_rejoinder_intro_female_noble_pitiless"),
						  (else_try),
							(eq, ":comment", "str_comment_intro_female_common_pitiless"),
							(assign, ":rejoinder", "str_rejoinder_intro_female_common_pitiless"),
						  (else_try),
							(eq, ":comment", "str_comment_intro_female_noble_sadistic"),
							(assign, ":rejoinder", "str_rejoinder_intro_female_noble_sadistic"),
						  (else_try),
							(eq, ":comment", "str_comment_intro_female_common_sadistic"),
							(assign, ":rejoinder", "str_rejoinder_intro_female_common_sadistic"),
						  (else_try),
							(eq, ":comment", "str_comment_intro_female_common_upstanding"),
							(assign, ":rejoinder", "str_rejoinder_intro_female_common_upstanding"),
						  (else_try),
							(eq, ":comment", "str_comment_intro_female_noble_upstanding"),
							(assign, ":rejoinder", "str_rejoinder_intro_female_noble_upstanding"),
						  (else_try),
							(eq, ":comment", "str_comment_intro_female_common_martial"),
							(assign, ":rejoinder", "str_rejoinder_intro_female_common_martial"),
						  (else_try),
							(eq, ":comment", "str_comment_intro_female_sadistic_admiring"),
							(assign, ":rejoinder", "str_rejoinder_intro_female_sadistic_admiring"),
						  (else_try),
							(eq, ":comment", "str_comment_intro_female_badtempered_admiring"),
							(assign, ":rejoinder", "str_rejoinder_intro_female_badtempered_admiring"),
						  (else_try),
							(eq, ":comment", "str_comment_intro_female_pitiless_admiring"),
							(assign, ":rejoinder", "str_rejoinder_intro_female_pitiless_admiring"),
						  (try_end),

					   (else_try),
						  #Male character or non-gendered comment
						  (try_begin),
							(gt, ":plyr_renown", ":renown_check"),
							(assign, ":comment", "str_comment_intro_famous_liege"),
							(val_add, ":comment", ":reputation"),
						  (else_try),
							(gt, ":banner", 0),
							(assign, ":comment", "str_comment_intro_noble_liege"),
							(val_add, ":comment", ":reputation"),

							(try_begin),
								(eq, ":comment", "str_comment_intro_noble_sadistic"),
								(assign, ":rejoinder", "str_rejoinder_intro_noble_sadistic"),
							(try_end),

						  (else_try),
							(assign, ":comment", "str_comment_intro_common_liege"),
							(val_add, ":comment", ":reputation"),
						  (try_end),
					   (try_end),
				#Post 0907 changes end
                        
                      (else_try),
                        (eq, ":entry_type", logent_village_raided),
                        (eq, ":actor", "trp_player"),
                        (try_begin),
                          (eq, ":center_object_lord", "$g_talk_troop"),
                          (assign, ":relevance", 200),
                          (assign, ":suggested_relation_change", -1),
                          (assign, ":comment", "str_comment_you_raided_my_village_default"),
                          (try_begin),
                            (lt, "$g_talk_troop_faction_relation", -5),
                            (this_or_next|eq, ":reputation", lrep_goodnatured),
                            (eq, ":reputation", lrep_upstanding),
                            (assign, ":comment", "str_comment_you_raided_my_village_enemy_benevolent"),
                          (else_try),
                            (lt, "$g_talk_troop_faction_relation", -5),
                            (this_or_next|eq, ":reputation", lrep_cunning),
                            (eq, ":reputation", lrep_selfrighteous),
                            (assign, ":comment", "str_comment_you_raided_my_village_enemy_coldblooded"),
                          (else_try),
                            (lt, "$g_talk_troop_faction_relation", -5),
                            (this_or_next|eq, ":reputation", lrep_quarrelsome),
                            (eq, ":reputation", lrep_debauched),
                            (assign, ":comment", "str_comment_you_raided_my_village_enemy_spiteful"),
                          (else_try),
                            (lt, "$g_talk_troop_faction_relation", -5),
                            (assign, ":comment", "str_comment_you_raided_my_village_enemy"),
                          (else_try),
                            (lt, "$g_talk_troop_relation", -5),
                            (this_or_next|eq, ":reputation", lrep_quarrelsome),
                            (eq, ":reputation", lrep_debauched),
                            (assign, ":comment", "str_comment_you_raided_my_village_unfriendly_spiteful"),
                          (else_try),
                            (gt, "$g_talk_troop_relation", 5),
                            (assign, ":comment", "str_comment_you_raided_my_village_friendly"),
                          (try_end),
                        (try_end),
                        
                      (else_try),
                        (eq, ":entry_type", logent_village_extorted),
                        (eq, ":actor", "trp_player"),
                        (try_begin),
                          (eq, ":center_object_lord", "$g_talk_troop"),
                          (assign, ":relevance", 30),
                          (assign, ":suggested_relation_change", -1),
                          (assign, ":comment", "str_comment_you_robbed_my_village_default"),
                          (try_begin),
                            (lt, "$g_talk_troop_faction_relation", -5),
                            (this_or_next|eq, ":reputation", lrep_cunning),
                            (eq, ":reputation", lrep_selfrighteous),
                            (assign, ":comment", "str_comment_you_robbed_my_village_enemy_coldblooded"),
                          (else_try),
                            (lt, "$g_talk_troop_faction_relation", -5),
                            (assign, ":comment", "str_comment_you_robbed_my_village_enemy"),
                          (else_try),
                            (gt, "$g_talk_troop_relation", 5),
                            (this_or_next|eq, ":reputation", lrep_quarrelsome),
                            (eq, ":reputation", lrep_debauched),
                            (assign, ":comment", "str_comment_you_robbed_my_village_friendly_spiteful"),
                          (else_try),
                            (gt, "$g_talk_troop_relation", 5),
                            (assign, ":comment", "str_comment_you_robbed_my_village_friendly"),
                          (try_end),
                        (try_end),
                        
                      (else_try),
                        (eq, ":entry_type", logent_caravan_accosted),
                        (eq, ":actor", "trp_player"),
                        (eq, ":faction_object", "$g_talk_troop_faction"),
                        (eq, ":center_object", -1),
                        (eq, ":troop_object", -1),
                        
                        
                        
                        (faction_slot_eq, "$g_talk_troop_faction", slot_faction_leader, "$g_talk_troop"),
                        (assign, ":relevance", 30),
                        (assign, ":suggested_relation_change", -1),
                        (assign, ":comment", "str_comment_you_accosted_my_caravan_default"),
                        (try_begin),
                          (lt, "$g_talk_troop_faction_relation", -5),
                          (assign, ":comment", "str_comment_you_accosted_my_caravan_enemy"),
                        (try_end),
                        
                      (else_try),
                        (eq, ":entry_type", logent_helped_peasants),
                        (eq, ":actor", "trp_player"),
                        (try_begin),
                          (eq, ":center_object_lord", "$g_talk_troop"),
                          (assign, ":relevance", 40),
                          (assign, ":suggested_relation_change", 0),
                          (try_begin),
                            (this_or_next|eq, ":reputation", lrep_goodnatured),
                            (eq, ":reputation", lrep_upstanding),
                            (assign, ":comment", "str_comment_you_helped_villagers_benevolent"),
                            (assign, ":suggested_relation_change", 1),
                          (else_try),
                            (gt, "$g_talk_troop_relation", 5),
                            (this_or_next|eq, ":reputation", lrep_quarrelsome),
                            (eq, ":reputation", lrep_debauched),
                            (assign, ":comment", "str_comment_you_helped_villagers_friendly_cruel"),
                            (assign, ":suggested_relation_change", -1),
                          (else_try),
                            (lt, "$g_talk_troop_relation", -5),
                            (this_or_next|eq, ":reputation", lrep_quarrelsome),
                            (eq, ":reputation", lrep_debauched),
                            (assign, ":comment", "str_comment_you_helped_villagers_unfriendly_spiteful"),
                            (assign, ":suggested_relation_change", -1),
                          (else_try),
                            (gt, "$g_talk_troop_relation", 5),
                            (assign, ":comment", "str_comment_you_helped_villagers_friendly"),
                          (else_try),
                            (this_or_next|eq, ":reputation", lrep_selfrighteous),
                            (eq, ":reputation", lrep_debauched),
                            (assign, ":comment", "str_comment_you_helped_villagers_cruel"),
                            (assign, ":suggested_relation_change", -1),
                          (else_try),
                            (assign, ":comment", "str_comment_you_helped_villagers_default"),
                          (try_end),
                        (try_end),
                        
                        ###Combat events
                      (else_try),
                        (eq, ":entry_type", logent_castle_captured_by_player),
                        
                        (try_begin),
                          (eq, ":center_object_lord", "$g_talk_troop"),
                          (store_faction_of_party, ":current_center_faction", ":center_object"),
                          (eq, ":current_center_faction", "$players_kingdom"),
                          (neq, "$g_talk_troop_faction", "$players_kingdom"),
                          
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          
                          (assign, ":comment", "str_comment_you_captured_my_castle_enemy_spiteful"),
                          (assign, ":relevance", 200),
                        (else_try),
                          (eq, ":center_object_lord", "$g_talk_troop"),
                          (store_faction_of_party, ":current_center_faction", ":center_object"),
                          (eq, ":current_center_faction", "$players_kingdom"),
                          (neq, "$g_talk_troop_faction", "$players_kingdom"),
                          
                          (this_or_next|eq, ":reputation", lrep_martial),
                          (eq, ":reputation", lrep_goodnatured),
                          
                          (assign, ":comment", "str_comment_you_captured_my_castle_enemy_chivalrous"),
                          (assign, ":relevance", 200),
                        (else_try),
                          (eq, ":center_object_lord", "$g_talk_troop"),
                          (store_faction_of_party, ":current_center_faction", ":center_object"),
                          (eq, ":current_center_faction", "$players_kingdom"),
                          (neq, "$g_talk_troop_faction", "$players_kingdom"),
                          
                          (assign, ":comment", "str_comment_you_captured_my_castle_enemy"),
                          (assign, ":relevance", 200),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (lt, ":players_kingdom_relation", 0),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_you_captured_a_castle_allied_spiteful"),
                          (assign, ":relevance", 75),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (lt, ":players_kingdom_relation", 0),
                          (gt, "$g_talk_troop_relation", 5),
                          (assign, ":comment", "str_comment_you_captured_a_castle_allied_friendly"),
                          (assign, ":relevance", 75),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (lt, ":players_kingdom_relation", 0),
                          (lt, "$g_talk_troop_relation", -5),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_you_captured_a_castle_allied_unfriendly_spiteful"),
                          (assign, ":relevance", 75),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (lt, ":players_kingdom_relation", 0),
                          (lt, "$g_talk_troop_relation", -5),
                          (assign, ":comment", "str_comment_you_captured_a_castle_allied_unfriendly"),
                          (assign, ":relevance", 75),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (lt, ":players_kingdom_relation", 0),
                          (assign, ":comment", "str_comment_you_captured_a_castle_allied"),
                          (assign, ":relevance", 75),
                        (try_end),
                        
                      (else_try),
                        (eq, ":entry_type", logent_player_claims_throne_1),
                        (eq, "$players_kingdom", "$g_talk_troop_faction"),
                        (faction_slot_eq, "$g_talk_troop_faction", slot_faction_leader, "$g_talk_troop"),
                        (assign, ":comment", "str_comment_you_claimed_the_throne_1_player_liege"),
                        (assign, ":relevance", 500),
                        (lt, "$g_talk_troop_relation", -10),
                        
                      (else_try),
                        (eq, ":entry_type", logent_player_claims_throne_2),
                        (eq, "$players_kingdom", "$g_talk_troop_faction"),
                        (faction_slot_eq, "$g_talk_troop_faction", slot_faction_leader, "$g_talk_troop"),
                        (assign, ":comment", "str_comment_you_claimed_the_throne_2_player_liege"),
                        (assign, ":relevance", 500),
                        (lt, "$g_talk_troop_relation", -10),
                        
                      (else_try), #player appointed a commoner
					   (eq, ":entry_type", logent_liege_grants_fief_to_vassal),
					   (eq, ":actor", "trp_player"),
						   (troop_slot_ge, ":troop_object", slot_lord_reputation_type, lrep_roguish),
						   ##diplomacy start+
						   (neq, ":troop_object", "trp_npc13"),#Nizar isn't a commoner
						   (neg|troop_slot_ge, ":troop_object", slot_lord_reputation_type, lrep_conventional),#ladies aren't commoners
						   (assign, ":return_reg4", 0),
						   (try_begin),
							  (call_script, "script_cf_dplmc_troop_is_female", ":troop_object"),
							  (assign, ":return_reg4", 1),
						   (try_end),
						   ##diplomacy end+
					   (try_begin),
					   ##diplomacy start+
						  #Companions: make a supportive remark if the person is compatible with you
						  (is_between, "$g_talk_troop", companions_begin, companions_end),
						  (troop_slot_eq, "$g_talk_troop", slot_troop_personalitymatch_object, ":troop_object"),
						  (assign, ":comment", "str_dplmc_comment_you_enfiefed_a_commoner_supportive"),
						  (assign, ":relevance", 100),
						  (assign, ":suggested_relation_change", 0),
					   (else_try),
						   #Make a supportive remark if you like the person a lot (overrides objections)
						   (call_script, "script_troop_get_relation_with_troop", ":troop_object", "$g_talk_troop"),
						   (ge, reg0, 50),
						   (assign, ":comment", "str_dplmc_comment_you_enfiefed_a_commoner_supportive"),
						   (assign, ":relevance", 100),
						   (assign, ":suggested_relation_change", 0),
					   (else_try),
						   #Make a supportive remark if you like the person and wouldn't ordinarily object
						   (ge, reg0, 20),
						   (this_or_next|is_between, ":true_reputation", lrep_roguish, lrep_conventional),
						   (this_or_next|eq, ":reputation", lrep_cunning),
						   (eq, ":reputation", lrep_goodnatured),
						   (assign, ":comment", "str_dplmc_comment_you_enfiefed_a_commoner_supportive"),
						   (assign, ":relevance", 100),
						   (assign, ":suggested_relation_change", 0),
					   (else_try),
						   #Don't complain about your own spouse.
						   (troop_slot_eq, "$g_talk_troop", ":troop_object", slot_troop_spouse),
					   (else_try),
						   #Don't complain if you aren't actually a lord.
						   (is_between, ":true_reputation", lrep_roguish, lrep_conventional),
					   (else_try),
					   ##diplomacy end+
						   (this_or_next|eq, ":reputation", lrep_quarrelsome),
							   (eq, ":reputation", lrep_debauched),
						   (assign, ":comment", "str_comment_you_enfiefed_a_commoner_nasty"),##diplomacy start+ note: this line uses reg4 from above for gender-correct pronoun ##diplomacy end+
						   (assign, ":relevance", 100),
						   (assign, ":suggested_relation_change", -3),

					   (else_try),
						   (eq, ":reputation", lrep_upstanding),
						   (assign, ":comment", "str_comment_you_enfiefed_a_commoner_hesitant"),##diplomacy start+ note: next line uses reg4 from above for gender-correct pronoun ##diplomacy end+
						   (assign, ":relevance", 100),
						   (assign, ":suggested_relation_change", -2),

					   (else_try),
						   (this_or_next|eq, ":reputation", lrep_selfrighteous),
							   (eq, ":reputation", lrep_martial),
						   (assign, ":comment", "str_comment_you_enfiefed_a_commoner_derisive"),##diplomacy start+ note: next line uses reg4 from above for gender-correct pronoun ##diplomacy end+
						   (assign, ":relevance", 100),
						   (assign, ":suggested_relation_change", -4),

					   (try_end),

				#Post 0907 changes begin
                      (else_try),
                        (this_or_next|eq, ":entry_type", logent_lord_defeated_by_player),
                        (eq, ":entry_type", logent_lord_helped_by_player),
                        (troop_slot_eq, "$g_talk_troop", slot_troop_present_at_event, ":log_entry_no"),
                        (try_begin),
                          (lt, "$g_talk_troop_relation", -5),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_we_defeated_a_lord_unfriendly_spiteful"),
                          (assign, ":relevance", 150),
                        (else_try),
                          (lt, "$g_talk_troop_relation", -5),
                          (assign, ":comment", "str_comment_we_defeated_a_lord_unfriendly"),
                          (assign, ":relevance", 150),
                        (else_try),
                          (this_or_next|eq, ":reputation", lrep_selfrighteous),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_we_defeated_a_lord_cruel"),
                          (assign, ":relevance", 150),
                        (else_try),
                          (eq, ":reputation", lrep_quarrelsome),
                          (assign, ":comment", "str_comment_we_defeated_a_lord_cruel"),
                          (assign, ":relevance", 150),
                        (else_try),
                          (eq, ":reputation", lrep_upstanding),
                          (assign, ":comment", "str_comment_we_defeated_a_lord_upstanding"),
                          (assign, ":relevance", 150),
                        (else_try),
                          (assign, ":comment", "str_comment_we_defeated_a_lord_default"),
                          (assign, ":relevance", 150),
                        (try_end),
                        
                      (else_try),
                        (this_or_next|eq, ":entry_type", logent_castle_captured_by_player),
                        (eq, ":entry_type", logent_player_participated_in_siege),
                        
                        (troop_slot_eq, "$g_talk_troop", slot_troop_present_at_event, ":log_entry_no"),
                        
                        (try_begin),
                          (lt, "$g_talk_troop_relation", -5),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_we_fought_in_siege_unfriendly_spiteful"),
                          (assign, ":relevance", 150),
                        (else_try),
                          (lt, "$g_talk_troop_relation", -5),
                          (assign, ":comment", "str_comment_we_fought_in_siege_unfriendly"),
                          (assign, ":relevance", 150),
                        (else_try),
                          (this_or_next|eq, ":reputation", lrep_selfrighteous),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_we_fought_in_siege_cruel"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", 1),
                        (else_try),
                          (eq, ":reputation", lrep_quarrelsome),
                          (assign, ":comment", "str_comment_we_fought_in_siege_quarrelsome"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", 1),
                        (else_try),
                          (eq, ":reputation", lrep_upstanding),
                          (assign, ":comment", "str_comment_we_fought_in_siege_upstanding"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", 1),
                        (else_try),
                          (eq, ":reputation", lrep_martial),
                          (assign, ":comment", "str_comment_we_fought_in_siege_default"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", 2),
                        (else_try),
                          (faction_slot_eq, "$players_kingdom", slot_faction_leader, "$g_talk_troop"),
                          (assign, ":comment", "str_comment_we_fought_in_siege_default"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", 1),
                        (else_try),
                          (assign, ":comment", "str_comment_we_fought_in_siege_default"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", 1),
                        (try_end),
                        
                      (else_try),
                        (eq, ":entry_type", logent_castle_given_to_lord_by_player),
                        
                        (try_begin),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_you_give_castle_in_my_control"),
                          (assign, ":relevance", 200),
                        (else_try),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (this_or_next|eq, ":reputation", lrep_martial),
                          (eq, ":reputation", lrep_goodnatured),
                          (assign, ":comment", "str_comment_you_give_castle_in_my_control"),
                          (assign, ":relevance", 200),
                        (else_try),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (assign, ":comment", "str_comment_you_give_castle_in_my_control"),
                          (assign, ":relevance", 200),
                        (try_end),
                        
                      (else_try),
                        (eq, ":entry_type", logent_player_participated_in_major_battle),
                        (troop_slot_eq, "$g_talk_troop", slot_troop_present_at_event, ":log_entry_no"),
                        (try_begin),
                          (lt, "$g_talk_troop_relation", -5),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_we_fought_in_major_battle_unfriendly_spiteful"),
                          (assign, ":relevance", 150),
                        (else_try),
                          (lt, "$g_talk_troop_relation", -5),
                          (assign, ":comment", "str_comment_we_fought_in_major_battle_unfriendly"),
                          (assign, ":relevance", 150),
                        (else_try),
                          (this_or_next|eq, ":reputation", lrep_selfrighteous),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_we_fought_in_major_battle_cruel"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", 1),
                        (else_try),
                          (eq, ":reputation", lrep_quarrelsome),
                          (assign, ":comment", "str_comment_we_fought_in_major_battle_cruel"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", 1),
                        (else_try),
                          (eq, ":reputation", lrep_upstanding),
                          (assign, ":comment", "str_comment_we_fought_in_major_battle_upstanding"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", 1),
                        (else_try),
                          (faction_slot_eq, "$players_kingdom", slot_faction_leader, "$g_talk_troop"),
                          (assign, ":comment", "str_comment_we_fought_in_major_battle_default"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", 1),
                        (else_try),
                          (eq, ":reputation", lrep_martial),
                          (assign, ":comment", "str_comment_we_fought_in_major_battle_default"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", 2),
                        (else_try),
                          (assign, ":comment", "str_comment_we_fought_in_major_battle_default"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", 1),
                        (try_end),
                        
                      (else_try),
                        (eq, ":entry_type", logent_player_suggestion_succeeded),
                        (try_begin),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (assign, ":comment", "str_comment_player_suggestion_succeeded"),
                          (assign, ":relevance", 200),
                          (assign, ":suggested_relation_change", 3),
                          
                        (try_end),
                      (else_try),
                        (eq, ":entry_type", logent_player_suggestion_failed),
                        (try_begin),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (assign, ":comment", "str_comment_player_suggestion_failed"),
                          (assign, ":relevance", 200),
                          (assign, ":suggested_relation_change", -5),
                          
                        (try_end),
                        
                        #Post 0907 changes end
                        
					 (else_try),
					   (eq, ":entry_type", logent_lord_defeated_by_player),
					   ##diplomacy start+  Set reg4 for calling scripts
					   (try_begin),
						  (neq, ":troop_object", "$g_talk_troop"),
						  (assign, ":return_reg4", 0),
						  (call_script, "script_cf_dplmc_troop_is_female", ":troop_object"),
						  (assign, ":return_reg4", 1),
					   (try_end),
					   ##diplomacy end+
                        (try_begin),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (this_or_next|eq, ":reputation", lrep_martial),
                          (eq, ":reputation", lrep_goodnatured),
                          (assign, ":comment", "str_comment_you_defeated_me_enemy_chivalrous"),
                          (assign, ":relevance", 200),
                        (else_try),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (this_or_next|eq, ":reputation", lrep_debauched),
                          (eq, ":reputation", lrep_quarrelsome),
                          (assign, ":comment", "str_comment_you_defeated_me_enemy_spiteful"),
                          (assign, ":relevance", 200),
                        (else_try),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (assign, ":comment", "str_comment_you_defeated_me_enemy"),
                          (assign, ":relevance", 200),
                        (else_try),
                          (eq, ":troop_object_faction", "$g_talk_troop_faction"),
                          (this_or_next|eq, ":reputation", lrep_upstanding),
                          (eq, ":reputation", lrep_cunning),
                          (assign, ":comment", "str_comment_you_defeated_my_friend_enemy_pragmatic"),
                          (assign, ":relevance", 85),
                        (else_try),
                          (eq, ":troop_object_faction", "$g_talk_troop_faction"),
                          (this_or_next|eq, ":reputation", lrep_martial),
                          (eq, ":reputation", lrep_goodnatured),
                          (assign, ":comment", "str_comment_you_defeated_my_friend_enemy_chivalrous"),
                          (assign, ":relevance", 85),
                        (else_try),
                          (eq, ":troop_object_faction", "$g_talk_troop_faction"),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_you_defeated_my_friend_enemy_spiteful"),
                          (assign, ":relevance", 85),
                        (else_try),
                          (eq, ":troop_object_faction", "$g_talk_troop_faction"),
                          (assign, ":comment", "str_comment_you_defeated_my_friend_enemy"),
                          (assign, ":relevance", 85),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (lt, ":players_kingdom_relation", 0),
                          (faction_slot_eq, "$players_kingdom", slot_faction_leader, "$g_talk_troop"),
                          (assign, ":comment", "str_comment_you_defeated_a_lord_allied_liege"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", 1),
                          
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (lt, ":players_kingdom_relation", 0),
                          (lt, "$g_talk_troop_relation", -5),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_you_defeated_a_lord_allied_unfriendly_spiteful"),
                          (assign, ":relevance", 65),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (lt, ":players_kingdom_relation", 0),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_you_defeated_a_lord_allied_spiteful"),
                          (assign, ":relevance", 65),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (lt, ":players_kingdom_relation", 0),
                          (lt, "$g_talk_troop_relation", -5),
                          (this_or_next|eq, ":reputation", lrep_upstanding),
                          (eq, ":reputation", lrep_martial),
                          (assign, ":comment", "str_comment_you_defeated_a_lord_allied_unfriendly_chivalrous"),
                          (assign, ":relevance", 65),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (lt, ":players_kingdom_relation", 0),
                          (assign, ":comment", "str_comment_you_defeated_a_lord_allied"),
                          (assign, ":relevance", 65),
                        (try_end),
                        
					 (else_try),
					   (eq, ":entry_type", logent_lord_defeated_by_player),
					   ##diplomacy start+  Set reg4 for calling scripts
					   (try_begin),
						  (neq, ":troop_object", "$g_talk_troop"),
						  (assign, ":return_reg4", 0),
						  (call_script, "script_cf_dplmc_troop_is_female", ":troop_object"),
						  (assign, ":return_reg4", 1),
					   (try_end),
					   ##diplomacy end+
                        (try_begin),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (this_or_next|eq, ":reputation", lrep_martial),
                          (eq, ":reputation", lrep_goodnatured),
                          (assign, ":comment", "str_comment_you_defeated_me_enemy_chivalrous"),
                          (assign, ":relevance", 200),
                        (else_try),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (this_or_next|eq, ":reputation", lrep_debauched),
                          (eq, ":reputation", lrep_quarrelsome),
                          (assign, ":comment", "str_comment_you_defeated_me_enemy_spiteful"),
                          (assign, ":relevance", 200),
                        (else_try),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (assign, ":comment", "str_comment_you_defeated_me_enemy"),
                          (assign, ":relevance", 200),
                        (else_try),
                          (eq, ":troop_object_faction", "$g_talk_troop_faction"),
                          (this_or_next|eq, ":reputation", lrep_upstanding),
                          (eq, ":reputation", lrep_cunning),
                          (assign, ":comment", "str_comment_you_defeated_my_friend_enemy_pragmatic"),
                          (assign, ":relevance", 85),
                        (else_try),
                          (eq, ":troop_object_faction", "$g_talk_troop_faction"),
                          (this_or_next|eq, ":reputation", lrep_martial),
                          (eq, ":reputation", lrep_goodnatured),
                          (assign, ":comment", "str_comment_you_defeated_my_friend_enemy_chivalrous"),
                          (assign, ":relevance", 85),
                        (else_try),
                          (eq, ":troop_object_faction", "$g_talk_troop_faction"),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_you_defeated_my_friend_enemy_spiteful"),
                          (assign, ":relevance", 85),
                        (else_try),
                          (eq, ":troop_object_faction", "$g_talk_troop_faction"),
                          (assign, ":comment", "str_comment_you_defeated_my_friend_enemy"),
                          (assign, ":relevance", 85),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (lt, ":players_kingdom_relation", 0),
                          (faction_slot_eq, "$players_kingdom", slot_faction_leader, "$g_talk_troop"),
                          (assign, ":comment", "str_comment_you_defeated_a_lord_allied_liege"),
                          (assign, ":relevance", 70),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (lt, ":players_kingdom_relation", 0),
                          (lt, "$g_talk_troop_relation", -5),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_you_defeated_a_lord_allied_unfriendly_spiteful"),
                          (assign, ":relevance", 65),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (lt, ":players_kingdom_relation", 0),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_you_defeated_a_lord_allied_spiteful"),
                          (assign, ":relevance", 65),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (lt, ":players_kingdom_relation", 0),
                          (lt, "$g_talk_troop_relation", -5),
                          (this_or_next|eq, ":reputation", lrep_upstanding),
                          (eq, ":reputation", lrep_martial),
                          (assign, ":comment", "str_comment_you_defeated_a_lord_allied_unfriendly_chivalrous"),
                          (assign, ":relevance", 65),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (lt, ":players_kingdom_relation", 0),
                          (assign, ":comment", "str_comment_you_defeated_a_lord_allied"),
                          (assign, ":relevance", 65),
                        (try_end),
                        
                        #Post 0907 changes begin
                      (else_try),
                        (eq, ":entry_type", logent_lord_helped_by_player),
                        (neq, ":troop_object", "$g_talk_troop"),
                        (eq, ":troop_object_faction", "$g_talk_troop_faction"),
					   ##diplomacy start+  Set reg4 for calling scripts
					   (assign, ":return_reg4", 0),
					   (try_begin),
						  (call_script, "script_cf_dplmc_troop_is_female", ":troop_object"),
						  (assign, ":return_reg4", 1),
					   (try_end),
					   ##diplomacy end+
                        (try_begin),
                          (lt, "$g_talk_troop_relation", -5),
                          (this_or_next|eq, ":reputation", lrep_upstanding),
                          (eq, ":reputation", lrep_martial),
                          (assign, ":comment", "str_comment_you_helped_my_ally_unfriendly_chivalrous"),
                          (assign, ":relevance", 65),
                          (assign, ":suggested_relation_change", 2),
                        (else_try),
                          (lt, "$g_talk_troop_relation", -5),
                          (assign, ":comment", "str_comment_you_helped_my_ally_unfriendly"),
                          (assign, ":relevance", 0),
                        (else_try),
						  ##diplomacy start+
						  (gt, ":speaker_is_a_liege", 0),#Explicitly check if the speaker is a liege rather than relying solely on reputation
						  ##diplomacy end+
                          (eq, ":reputation", lrep_none),
                          (assign, ":comment", "str_comment_you_helped_my_ally_liege"),
                          (assign, ":relevance", 65),
                          (assign, ":suggested_relation_change", 3),
                        (else_try),
                          (lt, "$g_talk_troop_relation", -5),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_you_helped_my_ally_unfriendly_spiteful"),
                          (assign, ":relevance", 65),
                        (else_try),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_you_helped_my_ally_spiteful"),
                          (assign, ":relevance", 65),
                        (else_try),
                          (this_or_next|eq, ":reputation", lrep_martial),
                          (eq, ":reputation", lrep_upstanding),
                          (assign, ":comment", "str_comment_you_helped_my_ally_chivalrous"),
                          (assign, ":relevance", 65),
                          (assign, ":suggested_relation_change", 2),
                        (else_try),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (assign, ":comment", "str_comment_you_helped_my_ally_default"),
                        (try_end),
                        
				#Post 0907 changes begin
					 (else_try),
					   (eq, ":entry_type", logent_player_defeated_by_lord),
					   ##diplomacy start+  Set reg4 for calling scripts
					   (try_begin),
						  (neq, ":troop_object", "$g_talk_troop"),
						  (assign, ":return_reg4", 0),
						  (call_script, "script_cf_dplmc_troop_is_female", ":troop_object"),
						  (assign, ":return_reg4", 1),
					   (try_end),
					   ##diplomacy end+
					   (troop_slot_eq, "$g_talk_troop", slot_troop_present_at_event, ":log_entry_no"),
					   (try_begin),
						   (lt, "$g_talk_troop_relation", -5),
						   (this_or_next|eq, ":reputation", lrep_quarrelsome),
							   (eq, ":reputation", lrep_debauched),
						   (assign, ":comment", "str_comment_we_were_defeated_unfriendly_spiteful"),
						   (assign, ":relevance", 150),
					   (else_try),
						   (lt, "$g_talk_troop_relation", -5),
						   (assign, ":comment", "str_comment_we_were_defeated_unfriendly"),
						   (assign, ":relevance", 150),
					   (else_try),
						   (this_or_next|eq, ":reputation", lrep_selfrighteous),
							   (eq, ":reputation", lrep_debauched),
						   (assign, ":comment", "str_comment_we_were_defeated_cruel"),
						   (assign, ":relevance", 150),
					   (else_try),
						   (assign, ":comment", "str_comment_we_were_defeated_default"),
						   (assign, ":relevance", 150),
					   (try_end),
                        
                      (else_try),
						   (eq, ":entry_type", logent_player_defeated_by_lord),
						   ##diplomacy start+  Set reg4 for calling scripts
						   (try_begin),
							  (neq, ":troop_object", "$g_talk_troop"),
							  (assign, ":return_reg4", 0),
							  (call_script, "script_cf_dplmc_troop_is_female", ":troop_object"),
							  (assign, ":return_reg4", 1),
						   (try_end),
						   ##diplomacy end+
                        (try_begin),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_I_defeated_you_enemy_spiteful"),
                          (assign, ":relevance", 200),
                        (else_try),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (eq, ":reputation", lrep_martial),
                          (assign, ":comment", "str_comment_I_defeated_you_enemy_chivalrous"),
                          (assign, ":relevance", 200),
                        (else_try),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (this_or_next|eq, ":reputation", lrep_goodnatured),
                          (eq, ":reputation", lrep_upstanding),
                          (assign, ":comment", "str_comment_I_defeated_you_enemy_benevolent"),
                          (assign, ":relevance", 200),
                        (else_try),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (this_or_next|eq, ":reputation", lrep_selfrighteous),
                          (eq, ":reputation", lrep_cunning),
                          (assign, ":comment", "str_comment_I_defeated_you_enemy_coldblooded"),
                          (assign, ":relevance", 200),
                        (else_try),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (assign, ":comment", "str_comment_I_defeated_you_enemy"),
                          (assign, ":relevance", 200),
                        (else_try),
                          (eq, ":troop_object", "$g_talk_troop"),
                          (assign, ":comment", "str_comment_I_defeated_you_enemy"),
                          (assign, ":relevance", 200),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (gt, "$g_talk_troop_relation", 5),
                          (assign, ":comment", "str_comment_you_were_defeated_allied_friendly_spiteful"),
                          (assign, ":relevance", 80),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (this_or_next|eq, ":reputation", lrep_selfrighteous),
                          (eq, ":reputation", lrep_debauched),
                          (lt, "$g_talk_troop_relation", -5),
                          (assign, ":comment", "str_comment_you_were_defeated_allied_unfriendly_cruel"),
                          (assign, ":relevance", 80),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (le, "$g_talk_troop_relation", 5),
                          (assign, ":comment", "str_comment_you_were_defeated_allied_spiteful"),
                          (assign, ":relevance", 80),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (eq, ":reputation", lrep_selfrighteous),
                          (assign, ":comment", "str_comment_you_were_defeated_allied_pitiless"),
                          (assign, ":relevance", 65),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (eq, ":reputation", lrep_upstanding),
                          (lt, "$g_talk_troop_relation", -15),
                          (assign, ":comment", "str_comment_you_were_defeated_allied_unfriendly_upstanding"),
                          (assign, ":relevance", 65),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (lt, "$g_talk_troop_relation", -10),
                          (assign, ":comment", "str_comment_you_were_defeated_allied_unfriendly"),
                          (assign, ":relevance", 65),
                        (else_try),
                          (eq, "$players_kingdom", "$g_talk_troop_faction"),
                          (assign, ":comment", "str_comment_you_were_defeated_allied"),
                          (assign, ":relevance", 65),
                        (try_end),
                        #Post 0907 changes end
                        
                        #Post 0907 changes begin
                      (else_try),
						   (eq, ":entry_type", logent_player_retreated_from_lord),
						   (troop_slot_eq, "$g_talk_troop", slot_troop_present_at_event, ":log_entry_no"),
						   ##diplomacy start+  Set reg4 for calling scripts
						   (try_begin),
							  (neq, ":troop_object", "$g_talk_troop"),
							  (assign, ":return_reg4", 0),
							  (call_script, "script_cf_dplmc_troop_is_female", ":troop_object"),
							  (assign, ":return_reg4", 1),
						   (try_end),
						   ##diplomacy end+
                        (try_begin),
                          (lt, "$g_talk_troop_relation", -5),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_you_abandoned_us_unfriendly_spiteful"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", -5),
                        (else_try),
                          (lt, "$g_talk_troop_relation", -5),
                          (eq, ":reputation", lrep_selfrighteous),
                          (assign, ":comment", "str_comment_you_abandoned_us_unfriendly_pitiless"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", -5),
                        (else_try),
                          (lt, "$g_talk_troop_relation", -5),
                          (this_or_next|eq, ":reputation", lrep_quarrelsome),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_you_abandoned_us_spiteful"),
                          (assign, ":suggested_relation_change", -5),
                        (else_try),
                          (eq, ":reputation", lrep_martial),
                          (assign, ":comment", "str_comment_you_abandoned_us_chivalrous"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", -2),
                        (else_try),
                          (this_or_next|eq, ":reputation", lrep_upstanding),
                          (eq, ":reputation", lrep_goodnatured),
                          (assign, ":comment", "str_comment_you_abandoned_us_benefitofdoubt"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", -1),
                        (else_try),
                          (assign, ":comment", "str_comment_you_abandoned_us_default"),
                          (assign, ":relevance", 150),
                          (assign, ":suggested_relation_change", -2),
                        (try_end),
                        
                        
                        #Post 0907 changes end
                        
                      (else_try),
                        (this_or_next|eq, ":entry_type", logent_player_retreated_from_lord),
                        (eq, ":entry_type", logent_player_retreated_from_lord_cowardly),
                        
                        (eq, ":troop_object", "$g_talk_troop"),
                        (try_begin),
                          (eq, "$cheat_mode", 1),
                          (assign, reg7, ":entry_hours_elapsed"),
                          (display_message, "@{!}Elapsed hours: {reg7}"),
                        (try_end),
                        (gt, ":entry_hours_elapsed", 2),
                        (try_begin),
                          (this_or_next|eq, ":reputation", lrep_selfrighteous),
                          (eq, ":reputation", lrep_debauched),
                          (assign, ":comment", "str_comment_you_ran_from_me_enemy_spiteful"),
                          (assign, ":relevance", 25),
                        (else_try),
                          (eq, ":reputation", lrep_martial),
                          (assign, ":comment", "str_comment_you_ran_from_me_enemy_chivalrous"),
                          (assign, ":relevance", 25),
                        (else_try),
                          (this_or_next|eq, ":reputation", lrep_goodnatured),
                          (eq, ":reputation", lrep_upstanding),
                          (assign, ":comment", "str_comment_you_ran_from_me_enemy_benevolent"),
                          (assign, ":relevance", 25),
                        (else_try),
                          (eq, ":reputation", lrep_cunning),
                          (assign, ":comment", "str_comment_you_ran_from_me_enemy_coldblooded"),
                          (assign, ":relevance", 25),
                        (else_try),
                          (assign, ":comment", "str_comment_you_ran_from_me_enemy"),
                          (assign, ":relevance", 25),
                        (try_end),
                        
					 (else_try),
					   (eq, ":entry_type", logent_player_retreated_from_lord_cowardly),
					   ##diplomacy start+  Set reg4 for calling scripts
					   (try_begin),
						  (neq, ":troop_object", "$g_talk_troop"),
						  (assign, ":return_reg4", 0),
						  (call_script, "script_cf_dplmc_troop_is_female", ":troop_object"),
						  (assign, ":return_reg4", 1),
					   (try_end),
					   ##diplomacy end+
					   (try_begin),
						 (eq, "$players_kingdom", "$g_talk_troop_faction"),
						 (neq, ":troop_object", "$g_talk_troop"),
						 (lt, "$g_talk_troop_relation", 5),
						 (eq, ":reputation", lrep_martial),
						 (assign, ":comment", "str_comment_you_ran_from_foe_allied_chivalrous"),
						 (assign, ":relevance", 80),
						 (assign, ":suggested_relation_change", -3),
					   (else_try),
						 (eq, "$players_kingdom", "$g_talk_troop_faction"),
						 (neq, ":troop_object", "$g_talk_troop"),
						 (eq, ":reputation", lrep_upstanding),
						 (assign, ":comment", "str_comment_you_ran_from_foe_allied_upstanding"),
						 (assign, ":relevance", 80),
						 (assign, ":suggested_relation_change", -1),
					   (else_try),
						 (eq, "$players_kingdom", "$g_talk_troop_faction"),
						 (neq, ":troop_object", "$g_talk_troop"),
						 (lt, "$g_talk_troop_relation", 5),
						 (this_or_next|eq, ":reputation", lrep_quarrelsome),
							 (eq, ":reputation", lrep_debauched),
						 (assign, ":comment", "str_comment_you_ran_from_foe_allied_spiteful"),
						 (assign, ":relevance", 80),
					   (try_end),

					 (else_try),
					   (eq, ":entry_type", logent_lord_defeated_but_let_go_by_player),
					   ##diplomacy start+  Set reg4 for calling scripts
					   (try_begin),
						  (neq, ":troop_object", "$g_talk_troop"),
						  (assign, ":return_reg4", 0),
						  (call_script, "script_cf_dplmc_troop_is_female", ":troop_object"),
						  (assign, ":return_reg4", 1),
					   (try_end),
					   ##diplomacy end+
					   (try_begin),
						 (eq, ":troop_object", "$g_talk_troop"),
						 (this_or_next|eq, ":reputation", lrep_quarrelsome),
							 (eq, ":reputation", lrep_debauched),
						 (assign, ":comment", "str_comment_you_let_me_go_spiteful"),
						 (assign, ":relevance", 300),
						 (assign, ":suggested_relation_change", -15),
					   (else_try),
						 (eq, ":troop_object", "$g_talk_troop"),
						 (ge, "$g_talk_troop_faction_relation", 0),
						 (assign, ":comment", "str_comment_you_let_me_go_default"),
						 (assign, ":relevance", 300),
						 (assign, ":suggested_relation_change", 2),
					   (else_try),
						 (eq, ":troop_object", "$g_talk_troop"),
						 (lt, "$g_talk_troop_faction_relation", 0),
						 (this_or_next|eq, ":reputation", lrep_martial),
							 (eq, ":reputation", lrep_upstanding),
						 (assign, ":suggested_relation_change", 5),
						 (assign, ":relevance", 300),
						 (assign, ":comment", "str_comment_you_let_me_go_enemy_chivalrous"),
					   (else_try),
						 (eq, ":troop_object", "$g_talk_troop"),
						 (lt, "$g_talk_troop_faction_relation", 0),
						 (this_or_next|eq, ":reputation", lrep_selfrighteous),
							 (eq, ":reputation", lrep_cunning),
						 (assign, ":relevance", 300),
						 (assign, ":comment", "str_comment_you_let_me_go_enemy_coldblooded"),
					   (else_try),
						 (eq, ":troop_object", "$g_talk_troop"),
						 (lt, "$g_talk_troop_faction_relation", 0),
						 (assign, ":relevance", 300),
						 (assign, ":comment", "str_comment_you_let_me_go_enemy"),
						 (assign, ":suggested_relation_change", 1),
					   (else_try),
						 (eq, "$players_kingdom", "$g_talk_troop_faction"),
						 (lt, ":players_kingdom_relation", 0),
						 (neq, ":troop_object", "$g_talk_troop"),
						 (this_or_next|eq, ":reputation", lrep_martial),
							 (eq, ":reputation", lrep_goodnatured),
						 (assign, ":comment", "str_comment_you_let_go_a_lord_allied_chivalrous"),
						 (assign, ":relevance", 80),
					   (else_try),
						 (eq, "$players_kingdom", "$g_talk_troop_faction"),
						 (lt, ":players_kingdom_relation", 0),
						 (neq, ":troop_object", "$g_talk_troop"),
						 (eq, ":reputation", lrep_upstanding),
						 (assign, ":comment", "str_comment_you_let_go_a_lord_allied_upstanding"),
						 (assign, ":relevance", 80),
					   (else_try),
						 (eq, "$players_kingdom", "$g_talk_troop_faction"),
						 (lt, ":players_kingdom_relation", 0),
						 (neq, ":troop_object", "$g_talk_troop"),
						 (this_or_next|eq, ":reputation", lrep_cunning),
							 (eq, ":reputation", lrep_selfrighteous),
						 (assign, ":comment", "str_comment_you_let_go_a_lord_allied_coldblooded"),
						 (assign, ":relevance", 80),
					   (else_try),
						 (eq, "$players_kingdom", "$g_talk_troop_faction"),
						 (lt, ":players_kingdom_relation", 0),
						 (neq, ":troop_object", "$g_talk_troop"),
						 (lt, "$g_talk_troop_relation", -5),
						 (this_or_next|eq, ":reputation", lrep_quarrelsome),
							 (eq, ":reputation", lrep_debauched),
						 (assign, ":comment", "str_comment_you_let_go_a_lord_allied_unfriendly_spiteful"),
						 (assign, ":relevance", 80),
					   (else_try),
						 (eq, "$players_kingdom", "$g_talk_troop_faction"),
						 (lt, ":players_kingdom_relation", 0),
						 (neq, ":troop_object", "$g_talk_troop"),
						 (assign, ":comment", "str_comment_you_let_go_a_lord_allied"),
						 (assign, ":relevance", 80),
					   (try_end),
                        
                        #Internal faction relations
                        
                      (else_try),
                        (eq, ":entry_type", logent_pledged_allegiance),
                        (eq, ":actor", "trp_player"),
                        (try_begin),
                          (eq, ":faction_object", "$g_talk_troop_faction"),
                          (neq, ":troop_object", "$g_talk_troop"),
                          (eq, ":faction_object", "$players_kingdom"), #Ie, no switch of kingdoms
                          (assign, ":relevance", 200),
                          (try_begin),
                            (lt, "$g_talk_troop_relation", -5),
                            (eq, ":reputation", lrep_martial),
                            (assign, ":comment", "str_comment_pledged_allegiance_allied_martial_unfriendly"),
                          (else_try),
                            (eq, ":reputation", lrep_martial),
                            (assign, ":comment", "str_comment_pledged_allegiance_allied_martial"),
                          (else_try),
                            (lt, "$g_talk_troop_relation", -5),
                            (eq, ":reputation", lrep_quarrelsome),
                            (assign, ":comment", "str_comment_pledged_allegiance_allied_quarrelsome_unfriendly"),
                          (else_try),
                            (eq, ":reputation", lrep_quarrelsome),
                            (assign, ":comment", "str_comment_pledged_allegiance_allied_quarrelsome"),
                          (else_try),
                            (lt, "$g_talk_troop_relation", -5),
                            (eq, ":reputation", lrep_selfrighteous),
                            (assign, ":comment", "str_comment_pledged_allegiance_allied_selfrighteous_unfriendly"),
                          (else_try),
                            (eq, ":reputation", lrep_selfrighteous),
                            (assign, ":comment", "str_comment_pledged_allegiance_allied_selfrighteous"),
                          (else_try),
                            (lt, "$g_talk_troop_relation", -5),
                            (eq, ":reputation", lrep_cunning),
                            (assign, ":comment", "str_comment_pledged_allegiance_allied_cunning_unfriendly"),
                          (else_try),
                            (eq, ":reputation", lrep_cunning),
                            (assign, ":comment", "str_comment_pledged_allegiance_allied_cunning"),
                          (else_try),
                            (lt, "$g_talk_troop_relation", -5),
                            (eq, ":reputation", lrep_debauched),
                            (assign, ":comment", "str_comment_pledged_allegiance_allied_debauched_unfriendly"),
                          (else_try),
                            (eq, ":reputation", lrep_debauched),
                            (assign, ":comment", "str_comment_pledged_allegiance_allied_debauched"),
                          (else_try),
                            (lt, "$g_talk_troop_relation", -5),
                            (eq, ":reputation", lrep_goodnatured),
                            (assign, ":comment", "str_comment_pledged_allegiance_allied_goodnatured_unfriendly"),
                          (else_try),
                            (eq, ":reputation", lrep_goodnatured),
                            (assign, ":comment", "str_comment_pledged_allegiance_allied_goodnatured"),
                          (else_try),
                            (lt, "$g_talk_troop_relation", -5),
                            (eq, ":reputation", lrep_upstanding),
                            (assign, ":comment", "str_comment_pledged_allegiance_allied_upstanding_unfriendly"),
                          (else_try),
                            (eq, ":reputation", lrep_upstanding),
                            (assign, ":comment", "str_comment_pledged_allegiance_allied_upstanding"),
                          (try_end),
                        (try_end),
                        
                        
                      (else_try),
                        (eq, ":entry_type", logent_liege_grants_fief_to_vassal),
                        (eq, ":troop_object", "trp_player"),
                        (try_begin),
                          (eq, ":faction_object", "$g_talk_troop_faction"),
                          (neq, ":actor", "$g_talk_troop"),
                          (eq, ":faction_object", "$players_kingdom"),
                          (assign, ":relevance", 110),
                          (try_begin),
                            (gt, "$g_talk_troop_relation", 5),
                            (this_or_next|eq, ":reputation", lrep_selfrighteous),
                            (eq, ":reputation", lrep_debauched),
                            (assign, ":comment", "str_comment_our_king_granted_you_a_fief_allied_friendly_cruel"),
                          (else_try),
                            (gt, "$g_talk_troop_relation", 5),
                            (this_or_next|eq, ":reputation", lrep_quarrelsome),
                            (eq, ":reputation", lrep_cunning),
                            (assign, ":comment", "str_comment_our_king_granted_you_a_fief_allied_friendly_cynical"),
                          (else_try),
                            (gt, "$g_talk_troop_relation", 5),
                            (assign, ":comment", "str_comment_our_king_granted_you_a_fief_allied_friendly"),
                          (else_try),
                            (is_between, "$g_talk_troop_relation", -5, 5),
                            (this_or_next|eq, ":reputation", lrep_quarrelsome),
                            (eq, ":reputation", lrep_debauched),
                            (assign, ":comment", "str_comment_our_king_granted_you_a_fief_allied_spiteful"),
                            (assign, ":suggested_relation_change", -2),
                          (else_try),
                            (lt, "$g_talk_troop_relation", -5),
                            (eq, ":reputation", lrep_upstanding),
                            (assign, ":comment", "str_comment_our_king_granted_you_a_fief_allied_unfriendly_upstanding"),
                          (else_try),
                            (lt, "$g_talk_troop_relation", -5),
                            (this_or_next|eq, ":reputation", lrep_quarrelsome),
                            (eq, ":reputation", lrep_debauched),
                            (assign, ":comment", "str_comment_our_king_granted_you_a_fief_allied_unfriendly_spiteful"),
                          (else_try),
                            (assign, ":comment", "str_comment_our_king_granted_you_a_fief_allied"),
                          (try_end),
                        (try_end),
                        
                      (else_try),
                        (eq, ":entry_type", logent_renounced_allegiance),
                        (eq, ":actor", "trp_player"),
                        (try_begin),
                          (eq, ":faction_object", "$g_talk_troop_faction"),
                          (neq, ":troop_object", "$g_talk_troop"),
                          (try_begin),
                            (ge, "$g_talk_troop_faction_relation", 0),
                            (neq, "$g_talk_troop_faction", "$players_kingdom"),
                            (assign, ":relevance", 180),
                            (try_begin),
                              (gt, "$g_talk_troop_relation", 5),
                              (assign, ":comment", "str_comment_you_renounced_your_alliegance_friendly"),
                            (else_try),
                              (ge, "$g_talk_troop_relation", 0),
                              (eq, ":reputation", lrep_goodnatured),
                              (assign, ":comment", "str_comment_you_renounced_your_alliegance_friendly"),
                            (else_try),
                              (assign, ":comment", "str_comment_you_renounced_your_alliegance_default"),
                            (try_end),
                          (else_try),
                            (lt, "$g_talk_troop_faction_relation", 0),
                            (assign, ":relevance", 300),
                            (try_begin),
                              (ge, "$g_talk_troop_relation", 0),
                              (this_or_next|eq, ":reputation", lrep_selfrighteous),
                              (eq, ":reputation", lrep_debauched),
                              (assign, ":comment", "str_comment_you_renounced_your_alliegance_unfriendly_moralizing"),
                            (else_try),
                              (gt, "$g_talk_troop_relation", 5),
                              (this_or_next|eq, ":reputation", lrep_goodnatured),
                              (eq, ":reputation", lrep_upstanding),
                              (assign, ":comment", "str_comment_you_renounced_your_alliegance_enemy_friendly"),
                            (else_try),
                              (gt, "$g_talk_troop_relation", 5),
                              (assign, ":comment", "str_comment_you_renounced_your_alliegance_enemy"),
                            (else_try),
                              (is_between, "$g_talk_troop_relation", -5, 5),
                              (this_or_next|eq, ":reputation", lrep_quarrelsome),
                              (eq, ":reputation", lrep_debauched),
                              (assign, ":comment", "str_comment_you_renounced_your_alliegance_unfriendly_spiteful"),
                              (assign, ":suggested_relation_change", -2),
                            (else_try),
                              (lt, "$g_talk_troop_relation", -5),
                              (this_or_next|eq, ":reputation", lrep_quarrelsome),
                              (this_or_next|eq, ":reputation", lrep_selfrighteous),
                              (eq, ":reputation", lrep_debauched),
                              (assign, ":comment", "str_comment_you_renounced_your_alliegance_unfriendly_spiteful"),
                            (else_try),
                              (assign, ":comment", "str_comment_you_renounced_your_alliegance_default"),
                            (try_end),
                          (try_end),
                        (try_end),
                        
					 (else_try),
					   (eq, ":entry_type", logent_lady_marries_lord),
					   (eq, ":troop_object", "trp_player"),
					   ##diplomacy start+  Set reg4 for calling scripts
					   (try_begin),
						  (neq, ":actor", "$g_talk_troop"),
						  (assign, ":return_reg4", 0),
						  (call_script, "script_cf_dplmc_troop_is_female", ":actor"),
						  (assign, ":return_reg4", 1),
					   (try_end),
					   ##diplomacy end+
					   (try_begin),
						  (this_or_next|eq, ":reputation", lrep_quarrelsome),
							(eq, ":reputation", lrep_debauched),
						  (lt, "$g_talk_troop_relation", -5),
						  (assign, ":relevance", 200),
						  (assign, ":comment", "str_comment_marriage_normal_nasty"),
					   (else_try),
						  (call_script, "script_troop_get_family_relation_to_troop", ":actor", "$g_talk_troop"),
						  (ge, reg0, 5),
						  (assign, ":comment", "str_comment_marriage_normal_family"),
						  (assign, ":relevance", 300),
						  (assign, ":suggested_relation_change", reg0),
						  (val_div, ":suggested_relation_change", 3),
					   (else_try),
						  (store_faction_of_troop, ":bride_faction", ":actor"),
						  (eq, ":bride_faction", "$g_talk_troop_faction"),
						  (assign, ":comment", "str_comment_marriage_normal"),
						  (assign, ":relevance", 100),
					   (try_end),
					 (else_try),
					   (eq, ":entry_type", logent_lady_elopes_with_lord),
					   (eq, ":troop_object", "trp_player"),
					   ##diplomacy start+  Set reg4 for calling scripts
					   (try_begin),
						  (neq, ":actor", "$g_talk_troop"),
						  (assign, ":return_reg4", 0),
						  (call_script, "script_cf_dplmc_troop_is_female", ":troop_object"),
						  (assign, ":return_reg4", 1),
					   (try_end),
					   ##diplomacy end+
					   (try_begin),
						  (call_script, "script_troop_get_family_relation_to_troop", ":actor", "$g_talk_troop"),
						  (ge, reg0, 5),
						  (assign, ":comment", "str_comment_marriage_elopement_family"),
						  (assign, ":relevance", 300),
						  (store_sub, ":suggested_relation_change", 0, reg0),
						  (val_div, ":suggested_relation_change", 3),
					   (else_try),
						  (store_faction_of_troop, ":bride_faction", ":actor"),
						  (eq, ":bride_faction", "$g_talk_troop_faction"),
						  (faction_slot_eq, ":bride_faction", slot_faction_leader, "$g_talk_troop"),
						  (assign, ":comment", "str_comment_marriage_elopement_liege"),
						  (assign, ":relevance", 300),
						  (assign, ":suggested_relation_change", -10),
					   (try_end),
					 (else_try), #this is specific to quarrels with the player
					   (eq, ":entry_type", logent_lords_quarrel_over_woman),
					   (eq, ":actor", "$g_talk_troop"),
					   (eq, ":center_object", "trp_player"),
                        
                        (neg|troop_slot_ge, ":troop_object", slot_troop_spouse, "trp_player"), ##1.132, new line
                        
					   (str_store_troop_name, s54, ":troop_object"),
					   ##diplomacy start+  Set reg4 for calling scripts
					   (assign, ":return_reg4", 0),
					   (try_begin),
						  (call_script, "script_cf_dplmc_troop_is_female", ":troop_object"),
						  (assign, ":return_reg4", 1),
					   (try_end),
					   ##diplomacy end+
					   (try_begin),
						   (this_or_next|eq, ":reputation", lrep_selfrighteous),
						   (this_or_next|eq, ":reputation", lrep_quarrelsome),
								(eq, ":reputation", lrep_debauched),
                          
                          (assign, ":comment", "str_comment_i_quarreled_with_you_over_woman_derisive"),
                          (assign, ":relevance", 200),
                          (assign, ":suggested_relation_change", -20),
                        (else_try),
                          (assign, ":comment", "str_comment_i_quarreled_with_you_over_woman_default"),
                          (assign, ":relevance", 200),
                          (assign, ":suggested_relation_change", -20),
                        (try_end),
                        
                      (else_try),
                        (eq, ":entry_type", logent_border_incident_troop_breaks_truce),
                        (eq, ":actor", "trp_player"),
                        (faction_slot_eq, ":faction_object", slot_faction_leader, "$g_talk_troop"),
                        (eq, "$players_kingdom", ":faction_object"),
                        
                        (assign, ":suggested_relation_change", -10),
                        (assign, ":comment", "str_comment_you_broke_truce_as_my_vassal"),
                        (assign, ":relevance", 300),
                        
                      (else_try),
                        (eq, ":entry_type", logent_border_incident_troop_attacks_neutral),
                        (eq, ":actor", "trp_player"),
                        (faction_slot_eq, ":faction_object", slot_faction_leader, "$g_talk_troop"),
                        (eq, "$players_kingdom", ":faction_object"),
                        
                        (assign, ":suggested_relation_change", -3),
                        (assign, ":comment", "str_comment_you_attacked_neutral_as_my_vassal"),
                        (assign, ":relevance", 200),
                        
                        #THE FOLLOWING ARE ALL COMPLAINTS SPOKEN BY LORDS WITHIN CONVERATIONS, RATHER THAN COMMENTS WHEN THE PLAYER FIRST SPEAKS TO A LORD
                      (else_try), #these need to have the actor and object strings added because they are used outside of "script_get_relevant_comment_to_s42"
                        (eq, ":entry_type", logent_ruler_intervenes_in_quarrel),
                        (eq, ":center_object", "$g_talk_troop"), #actor is liege lord, center object is loser lord, troop object is winner lord
                        (str_store_troop_name, s50, ":actor"),
                        (str_store_troop_name, s51, ":center_object"), #s50 is actor, s51 is center object, s54 is troop object
                        (str_store_troop_name, s54, ":troop_object"), #s50 is actor, s51 is center object, s54 is troop object
                        (assign, ":comment", "str_comment_lord_intervened_against_me"),
                        (assign, ":relevance", -1),
                        
                      (else_try),
                        (eq, ":entry_type", logent_lord_protests_marshall_appointment),
                        (eq, ":actor", "$g_talk_troop"),
                        
                        (str_store_troop_name, s51, ":center_object"), #s51 is center object (marshall), s54 is troop object (liege lord),
                        (str_store_troop_name, s54, ":troop_object"),
                        
                        (assign, ":comment", "str_comment_i_protested_marshall_appointment"),
                        (assign, ":relevance", -1),
                        
                      (else_try),
                        (eq, ":entry_type", logent_lord_blames_defeat),
                        (eq, ":actor", "$g_talk_troop"),
                        
                        (str_store_troop_name, s51, ":center_object"), #s51 is center object (marshall), s54 is troop object (liege lord),
                        (str_store_troop_name, s54, ":troop_object"),
                        (str_store_troop_name, s56, ":faction_object"), #faction object is unusual in this circumstance
                        
                        (assign, ":comment", "str_comment_i_blamed_defeat"),
                        (assign, ":relevance", -1),
                        
                      (else_try),
                        (eq, ":entry_type", logent_troop_feels_cheated_by_troop_over_land),
					   (eq, ":actor", "$g_talk_troop"),

					   ##diplomacy start+ fix fief quarrel comment bug (where the name of a random troop replaces the name of the center)
					   (str_store_party_name, s51, ":center_object"),#str_store_troop_name -> str_store_party_name
					   (str_store_troop_name, s54, ":troop_object"),
					   (str_store_troop_name, s56, ":faction_object"), #faction object is unusual in this circumstance 
 ##diplomacy end+  
					   (assign, ":comment", "str_comment_i_was_entitled_to_fief"),
					   (assign, ":relevance", -1),
                        
                      (else_try),
                        (eq, ":entry_type", logent_lords_quarrel_over_woman),
                        (eq, ":actor", "$g_talk_troop"),
                        
					   (str_store_troop_name, s51, ":center_object"),
					   (str_store_troop_name, s54, ":troop_object"),
					   ##diplomacy start+  Set reg4 and reg3 for calling scripts
					   #(assign, reg3, 0),# #Exclude reg3, since it is used for output anyway
					   #(try_begin),
					   #  (call_script, "script_cf_dplmc_troop_is_female", ":center_object"),
					   #  (assign, reg3, 1),
					   #(try_end),
					   (assign, ":return_reg4", 0),
					   (try_begin),
						  (call_script, "script_cf_dplmc_troop_is_female", ":troop_object"),
						  (assign, ":return_reg4", 1),
					   (try_end),
					   ##diplomacy end+
                        
                        (assign, ":comment", "str_comment_i_quarreled_with_troop_over_woman"),
                        (assign, ":relevance", -1),
                        
                      (else_try),
                        (eq, ":entry_type", logent_lords_quarrel_over_woman),
                        (eq, ":center_object", "$g_talk_troop"),
						
					   (str_store_troop_name, s51, ":actor"),
					   (str_store_troop_name, s54, ":troop_object"),
					   ##diplomacy start+  Set reg4 and reg3 for calling scripts
					   #(assign, reg3, 0),#Exclude reg3, since it is used for output anyway
					   #(try_begin),
					   #  (call_script, "script_cf_dplmc_troop_is_female", ":actor"),
					   #  (assign, reg3, 1),
					   #(try_end),
					   (assign, ":return_reg4", 0),
					   (try_begin),
						  (call_script, "script_cf_dplmc_troop_is_female", ":troop_object"),
						  (assign, ":return_reg4", 1),
					   (try_end),
					   ##diplomacy end+
                        
                        (assign, ":comment", "str_comment_i_quarreled_with_troop_over_woman"),
                        (assign, ":relevance", -1),
                        
                      (else_try),
                        (eq, ":entry_type", logent_player_stole_cattles_from_village),
                        
                        (eq, ":actor", "trp_player"),
                        (try_begin),
                          (eq, ":center_object_lord", "$g_talk_troop"),
                          (assign, ":relevance", 200),
                          (assign, ":suggested_relation_change", -1),
                          (assign, ":comment", "str_comment_you_stole_cattles_from_my_village_default"),
                          (try_begin),
                            (lt, "$g_talk_troop_faction_relation", -3),
                            (this_or_next|eq, ":reputation", lrep_goodnatured),
                            (eq, ":reputation", lrep_upstanding),
                            (assign, ":comment", "str_comment_you_stole_cattles_from_my_village_enemy_benevolent"),
                          (else_try),
                            (lt, "$g_talk_troop_faction_relation", -3),
                            (this_or_next|eq, ":reputation", lrep_cunning),
                            (eq, ":reputation", lrep_selfrighteous),
                            (assign, ":comment", "str_comment_you_stole_cattles_from_my_village_enemy_coldblooded"),
                          (else_try),
                            (lt, "$g_talk_troop_faction_relation", -3),
                            (this_or_next|eq, ":reputation", lrep_quarrelsome),
                            (eq, ":reputation", lrep_debauched),
                            (assign, ":comment", "str_comment_you_stole_cattles_from_my_village_enemy_spiteful"),
                          (else_try),
                            (lt, "$g_talk_troop_faction_relation", -3),
                            (assign, ":comment", "str_comment_you_stole_cattles_from_my_village_enemy"),
                          (else_try),
                            (lt, "$g_talk_troop_relation", -3),
                            (this_or_next|eq, ":reputation", lrep_quarrelsome),
                            (eq, ":reputation", lrep_debauched),
                            (assign, ":comment", "str_comment_you_stole_cattles_from_my_village_unfriendly_spiteful"),
                          (else_try),
                            (gt, "$g_talk_troop_relation", 6),
                            (assign, ":comment", "str_comment_you_stole_cattles_from_my_village_friendly"),
                          (try_end),
                        (try_end),
                        
                      (try_end),
                      
                      (assign, reg0, ":comment"),
                      (assign, reg1, ":relevance"),
                      (assign, reg2, ":suggested_relation_change"),
                      (assign, reg3, ":rejoinder"),
					 ##diplomacy start+
					 (assign, reg4, ":return_reg4"),
					 ##diplomacy end+
					]),
                  
                  # script_get_relevant_comment_to_s42
                  # Input: none
                  # Output: reg0 = 1 if comment found, 0 otherwise; s61 will contain comment string if found
                  ("get_relevant_comment_to_s42",
                    [
                      
                      (troop_get_slot, ":reputation", "$g_talk_troop", slot_lord_reputation_type),
                      (try_begin),
                        (eq, "$cheat_mode", 1),
                        (store_add, ":rep_string", ":reputation", "str_personality_archetypes"),
                        (str_store_string, s15, ":rep_string"),
                        (display_message, "@{!}Reputation type: {s15}"),
                      (try_end),
                      
                      
                      (assign, ":highest_score_so_far", 50),
                      (assign, ":best_comment_so_far", -1),
                      (assign, ":rejoinder_to_best_comment_so_far", -1),
                      (assign, ":comment_found", 0),
                      (assign, ":best_log_entry", -1),
                      (assign, ":comment_relation_change", 0),
					 (store_current_hours, ":current_time"),
					 ##diplomacy start+
					 (assign, ":best_comment_reg4", 0),
					 ##diplomacy end+
                      
                      #prevents multiple comments in conversations in same hour
                      
                      #     (troop_get_slot, ":talk_troop_last_comment_time", "$g_talk_troop", slot_troop_last_comment_time),
                      #"$num_log_entries should also be set to one, not zero. This is included in the initialize npcs script, although could be moved to game_start
                      (troop_get_slot, ":talk_troop_last_comment_slot", "$g_talk_troop", slot_troop_last_comment_slot),
                      (troop_set_slot, "$g_talk_troop", slot_troop_last_comment_slot, "$num_log_entries"),
                      
                      (store_add, ":log_entries_plus_one", "$num_log_entries", 1),
                      (try_for_range, ":log_entry_no", 1, ":log_entries_plus_one"),
                        #      It should be log entries plus one, so that the try_ sequence does not stop short of the last log entry
                        #      $Num_log_entries is now the number of the last log entry, which begins at "1" rather than "0"
                        #      This is so that (le, ":log_entry_no", ":talk_troop_last_comment_slot") works properly
                        
                        (troop_get_slot, ":entry_time",           "trp_log_array_entry_time",           ":log_entry_no"),
                        #      (val_max, ":entry_time", 1), #This is needed for pre-game events to be commented upon, if hours are used rather than the order of events
                        (store_sub, ":entry_hours_elapsed", ":current_time", ":entry_time"),
                        (try_begin),
                          (le, ":log_entry_no", ":talk_troop_last_comment_slot"),
                          #         (le, ":entry_time", ":talk_troop_last_comment_time"),
                          (try_begin),
                            (eq, ":log_entry_no", ":talk_troop_last_comment_slot"),
                            (eq, "$cheat_mode", 1),
                            (assign, reg5, ":log_entry_no"),
                            (display_message, "@{!}Entries up to #{reg5} skipped"),
                            (try_end),
                            #       I suggest using the log entry number as opposed to time so that events in the same hour can be commented upon
                            #       This feels more natural, for example, if there are other lords in the court when the player pledges allegiance
                          (else_try),
                            #         (le, ":entry_hours_elapsed", 3), #don't comment on really fresh events
                            #       (else_try),
                            (call_script, "script_get_relevant_comment_for_log_entry", ":log_entry_no"),
                            (gt, reg1, 10),
                            (assign, ":score", reg1),
                            (assign, ":comment", reg0),
                            #reg2 is what
                            (assign, ":rejoinder", reg3),
                            
                            (store_random_in_range, ":rand", 70, 140),
                            (val_mul, ":score", ":rand"),
                            (store_add, ":entry_time_score", ":entry_hours_elapsed", 500), #approx. one month
                            (val_mul, ":score", 1000),
                            (val_div, ":score", ":entry_time_score"), ###Relevance decreases over time - halved after one month, one-third after two, etc
                            (try_begin),
                              (gt, ":score", ":highest_score_so_far"),
                              (assign, ":highest_score_so_far", ":score"),
                              (assign, ":best_comment_so_far",  ":comment"),
                              (assign, ":rejoinder_to_best_comment_so_far",  ":rejoinder"),
                              (assign, ":best_log_entry", ":log_entry_no"),
							   (assign, ":comment_relation_change", reg2),
							   ##diplomacy start+
							   (assign, ":best_comment_reg4", reg4),
							   ##diplomacy end+
							 (try_end),
                          (try_end),
                        (try_end),
                        
                        (try_begin),
                          (gt, ":best_comment_so_far", 0),
                          (assign, ":comment_found", 1), #comment found print it to s61 now.
                          (troop_get_slot, ":actor",                 "trp_log_array_actor",                 ":best_log_entry"),
                          (troop_get_slot, ":center_object",         "trp_log_array_center_object",         ":best_log_entry"),
                          (troop_get_slot, ":center_object_lord",    "trp_log_array_center_object_lord",    ":best_log_entry"),
                          (troop_get_slot, ":center_object_faction", "trp_log_array_center_object_faction", ":best_log_entry"),
                          (troop_get_slot, ":troop_object",          "trp_log_array_troop_object",          ":best_log_entry"),
                          (troop_get_slot, ":troop_object_faction",  "trp_log_array_troop_object_faction",  ":best_log_entry"),
                          (troop_get_slot, ":faction_object",        "trp_log_array_faction_object",        ":best_log_entry"),
						   ##diplomacy start+
						   (assign, reg4, ":best_comment_reg4"),
						   ##diplomacy end+
						   (try_begin),
							 (ge, ":actor", 0),
							 (str_store_troop_name,   s50, ":actor"),
							 ##diplomacy start+
							 (eq, ":best_comment_so_far", "str_comment_i_quarreled_with_troop_over_woman"),
							 (neq, ":actor", "$g_talk_troop"),
							 (neq, ":actor", "trp_player"),
							 (assign, reg3, 0),
							 (try_begin),
								(call_script, "script_cf_dplmc_troop_is_female", ":actor"),
								(assign, reg3, 1),
							 (try_end),
							 ##diplomacy end+
						   (try_end),
						   (try_begin),
							 (ge, ":center_object", 0),
							 ##diplomacy start+
							 ##OLD:
							 #(str_store_party_name,   s51, ":center_object"),
							 ##NEW:
							 #Alternate meaning (not usually called from this script, but just in case)
							 #In this case, s51 is actually a troop.  Use reg3 for the gender.
							 (try_begin),
								(eq, ":best_comment_so_far", "str_comment_i_quarreled_with_troop_over_woman"),
								(str_store_troop_name, s51, ":center_object"),
								(neq, ":center_object", "$g_talk_troop"),
								(neq, ":center_object", "trp_player"),
								(call_script, "script_dplmc_store_troop_is_female_reg", ":center_object", 3),
							 (else_try),
							   (neq, ":best_comment_so_far", "str_comment_i_quarreled_with_troop_over_woman"),	
							   (str_store_party_name,   s51, ":center_object"),#<- old behavior
							(try_end),
							##diplomacy end+
						   (try_end),
						   (try_begin),
							 (ge, ":center_object_lord", 0),
							 (str_store_troop_name,   s52, ":center_object_lord"),
						   (try_end),
						   (try_begin),
							 (ge, ":center_object_faction", 0),
							 (str_store_faction_name, s53, ":center_object_faction"),
						   (try_end),
						   (try_begin),
							 (ge, ":troop_object", 0),
							 (str_store_troop_name,   s54, ":troop_object"),
						   (try_end),
						   (try_begin),
							 (is_between, ":troop_object_faction", kingdoms_begin, kingdoms_end),
							 (str_store_faction_name, s55, ":troop_object_faction"),
							 (str_store_string, s55, "str_the_s55"),
						   (else_try),
							 (is_between, ":troop_object", bandits_begin, bandits_end),
							 (str_store_string, s55, "str_bandits"),
						   (else_try),
							 (eq, ":troop_object_faction", "fac_deserters"),
							 (str_store_string, s55, "str_deserters"),
						   (else_try),
							 (str_store_string, s55, "str_travellers_on_the_road"),
						   (else_try),

						   (try_end),

						   (try_begin),
							 (ge, ":faction_object", 0),
							 (str_store_faction_name, s56, ":faction_object"),
						   (try_end),
						   (assign, "$g_last_comment_copied_to_s42", ":best_comment_so_far"), #maybe deprecate
						   (assign, "$g_rejoinder_to_last_comment", ":rejoinder_to_best_comment_so_far"),

						   (str_store_string, s42, ":best_comment_so_far"),
						 (try_end),

						 (assign, reg0, ":comment_found"),

						 (assign, "$log_comment_relation_change", ":comment_relation_change"),
						 ]),
	 
                    #
                    ("merchant_road_info_to_s42", #also does itemss to s32
                      [
                        (store_script_param, ":center", 1),
                        
                        (assign, ":last_bandit_party_found", -1),
                        (assign, ":last_bandit_party_origin", -1),
                        (assign, ":last_bandit_party_destination", -1),
                        (assign, ":last_bandit_party_hours_ago", -1),
                        
                        (str_clear, s32),
                        
                        (str_clear, s42),
                        (str_clear, s47), #safe roads
                        
                        (try_for_range, ":center_to_reset", centers_begin, centers_end),
                          (party_set_slot, ":center_to_reset", slot_party_temp_slot_1, 0),
                        (try_end),
                        
                        (assign, ":road_attacks", 0),
                        (assign, ":trades", 0),
                        
                        #first mention all attacks
                        (try_for_range, ":log_entry_iterator", 0, "$num_log_entries"),
                          (store_sub, ":log_entry_no", "$num_log_entries", ":log_entry_iterator"),
                          #how long ago?
                          (this_or_next|troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_traveller_attacked),
                          (troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_party_traded),
                          
                          #       reference - (call_script, "script_add_log_entry", logent_traveller_attacked, ":winner_party" (actor),  ":origin" (center object), ":destination" (troop_object), ":winner_faction"),
                          
                          (troop_get_slot, ":origin",         "trp_log_array_center_object",         ":log_entry_no"),
                          (troop_get_slot, ":destination",    "trp_log_array_troop_object",          ":log_entry_no"),
                          
                          (this_or_next|eq, ":origin", ":center"),
                          (eq, ":destination", ":center"),
                          
                          
                          (troop_get_slot, ":event_time",            "trp_log_array_entry_time",              ":log_entry_no"),
                          (store_current_hours, ":cur_hour"),
                          (store_sub, ":hours_ago", ":cur_hour", ":event_time"),
                          (assign, reg3, ":hours_ago"),
                          
                          (lt, ":hours_ago", 672), #four weeks
                          
                          (try_begin),
                            (eq, "$cheat_mode", 1),
                            (troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_traveller_attacked),
                            (display_message, "str_attack_on_travellers_found_reg3_hours_ago"),
                          (else_try),
                            (eq, "$cheat_mode", 1),
                            (troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_party_traded),
                            (display_message, "str_trade_event_found_reg3_hours_ago"),
                          (try_end),
                          
                          (try_begin), #possibly make script -- get_colloquial_for_time
                            (lt, ":hours_ago", 24),
                            (str_store_string, s46, "str_a_short_while_ago"),
                          (else_try),
                            (lt, ":hours_ago", 48),
                            (str_store_string, s46, "str_one_day_ago"),
                          (else_try),
                            (lt, ":hours_ago", 72),
                            (str_store_string, s46, "@two days ago"),
                          (else_try),
                            (lt, ":hours_ago", 154),
                            (str_store_string, s46, "str_earlier_this_week"),
                          (else_try),
                            (lt, ":hours_ago", 240),
                            (str_store_string, s46, "str_about_a_week_ago"),
                          (else_try),
                            (lt, ":hours_ago", 480),
                            (str_store_string, s46, "str_about_two_weeks_ago"),
                          (else_try),
                            (str_store_string, s46, "str_several_weeks_ago"),
                          (try_end),
                          
                          
                          
                          (troop_get_slot, ":actor", "trp_log_array_actor", ":log_entry_no"),
                          (troop_get_slot, ":faction_object", "trp_log_array_faction_object", ":log_entry_no"),
                          
                          (str_store_string, s39, "str_unknown_assailants"),
                          (assign, ":assailants_known", -1),
                          (try_begin),
                            (party_is_active, ":actor"),
                            (store_faction_of_party, ":actor_faction", ":actor"),
                            (eq, ":faction_object", ":actor_faction"),
                            (assign, ":assailants_known", ":actor"),
                            (str_store_party_name, s39, ":assailants_known"),
                            (assign, "$g_bandit_party_for_bounty", -1),
                            (try_begin), #possibly make script -- get_colloquial_for_faction
                              (eq, ":faction_object", "fac_kingdom_1"),
                              (str_store_string, s39, "str_swadians"),
                            (else_try),
                              (eq, ":faction_object", "fac_kingdom_2"),
                              (str_store_string, s39, "str_vaegirs"),
                            (else_try),
                              (eq, ":faction_object", "fac_kingdom_3"),
                              (str_store_string, s39, "str_khergits"),
                            (else_try),
                              (eq, ":faction_object", "fac_kingdom_4"),
                              (str_store_string, s39, "str_nords"),
                            (else_try),
                              (eq, ":faction_object", "fac_kingdom_5"),
                              (str_store_string, s39, "str_rhodoks"),
                            (else_try),
                              (eq, ":faction_object", "fac_kingdom_6"),
                              (str_store_string, s39, "str_sarranids"),
                            (else_try),
                              (eq, ":faction_object", "fac_player_supporters_faction"),
                              (str_store_string, s39, "str_your_followers"),
                            (else_try), #bandits
                              (assign, ":last_bandit_party_found", ":assailants_known"),
                              (assign, ":last_bandit_party_origin", ":origin"),
                              (assign, ":last_bandit_party_destination", ":destination"),
                              (assign, ":last_bandit_party_hours_ago", ":hours_ago"),
                            (try_end),
                          (try_end),
                          
                          (try_begin),
                            (eq, ":origin", ":center"),
                            (troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_traveller_attacked),
                            (party_slot_eq, ":destination", slot_party_temp_slot_1, 0),
                            
                            (party_set_slot, ":destination", slot_party_temp_slot_1, 1),
                            (str_store_party_name, s40, ":destination"),
                            (str_store_string, s44, "str_we_have_heard_that_travellers_heading_to_s40_were_attacked_on_the_road_s46_by_s39"),
                            (str_store_string, s43, "str_s42"),
                            (str_store_string, s42, "str_s43_s44"),
                            
                            (val_add, ":road_attacks", 1),
                            #travellers were attacked on the road to...
                          (else_try),
                            (eq, ":destination", ":center"),
                            (troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_traveller_attacked),
                            (party_slot_eq, ":origin", slot_party_temp_slot_1, 0),
                            
                            (party_set_slot, ":origin", slot_party_temp_slot_1, 1),
                            (str_store_party_name, s40, ":origin"),
                            (str_store_string, s44, "str_we_have_heard_that_travellers_coming_from_s40_were_attacked_on_the_road_s46_by_s39"),
                            
                            (str_store_string, s43, "str_s42"),
                            (str_store_string, s42, "str_s43_s44"),
                            
                            (val_add, ":road_attacks", 1),
                            
                            #travellers from here traded at...
                            #		(else_try),
                            #			(eq, ":origin", ":center"),
                            #			(troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_party_traded),
                            #			(party_slot_eq, ":destination", slot_party_temp_slot_1, 0),
                            
                            #			(party_set_slot, ":destination", slot_party_temp_slot_1, 1),
                            #			(str_store_party_name, s40, ":destination"),
                            #			(str_store_string, s44, "@Travellers headed to {s40} traded there {s46}"),
                            #			(str_store_string, s43, "@{s42"),
                            #			(str_store_string, s42, "str_s43_s44"),
                            
                            #caravan from traded at...
                          (else_try),
                            (eq, ":destination", ":center"),
                            (troop_slot_eq, "trp_log_array_entry_type", ":log_entry_no", logent_party_traded),
                            (party_slot_eq, ":origin", slot_party_temp_slot_1, 0),
                            
                            (party_set_slot, ":origin", slot_party_temp_slot_1, 1),
                            (str_store_party_name, s40, ":origin"),
                            (str_store_string, s44, "str_travellers_coming_from_s40_traded_here_s46"),
                            (str_store_string, s43, "str_s42"),
                            (str_store_string, s42, "str_s43_s44"),
                            
                            (val_add, ":trades", 1),
                            
                            #caravan from traded at...
                          (try_end),
                          
                        (try_end),
                        
                        
                        (try_begin),
                          (le, ":trades", 2),
                          (eq, ":road_attacks", 0),
                          (store_current_hours, ":hours"),
                          (lt, ":hours", 168),
                          (str_store_string, s42, "str_it_is_still_early_in_the_caravan_season_so_we_have_seen_little_tradings42"),
                        (else_try),
                          (eq, ":trades", 0),
                          (eq, ":road_attacks", 0),
                          (str_store_string, s42, "str_there_has_been_very_little_trading_activity_here_recentlys42"),
                        (else_try),
                          (le, ":trades", 2),
                          (eq, ":road_attacks", 0),
                          (str_store_string, s42, "str_there_has_some_trading_activity_here_recently_but_not_enoughs42"),
                        (else_try),
                          (le, ":trades", 2),
                          (le, ":road_attacks", 2),
                          (str_store_string, s42, "str_there_has_some_trading_activity_here_recently_but_the_roads_are_dangerouss42"),
                        (else_try),
                          (ge, ":road_attacks", 3),
                          (str_store_string, s42, "str_the_roads_around_here_are_very_dangerouss42"),
                        (else_try),
                          (ge, ":road_attacks", 1),
                          (str_store_string, s42, "str_we_have_received_many_traders_in_town_here_although_there_is_some_danger_on_the_roadss42"),
                        (else_try),
                          (str_store_string, s42, "str_we_have_received_many_traders_in_town_heres42"),
                        (try_end),
                        
                        #do safe roads
                        (assign, ":unused_trade_route_found", 0),
                        (try_for_range, ":trade_route_slot", slot_town_trade_routes_begin, slot_town_trade_routes_end),
                          (party_get_slot, ":trade_center", ":center", ":trade_route_slot"),
                          (is_between, ":trade_center", centers_begin, centers_end),
                          
                          (party_slot_eq, ":trade_center", slot_party_temp_slot_1, 0),
                          
                          #		(party_get_slot, ":town_lord", ":trade_center", slot_town_lord),
                          
                          (str_store_party_name, s41, ":trade_center"),
                          (try_begin),
                            (eq, ":unused_trade_route_found", 1),
                            (str_store_string, s44, "str_s44_s41"),
                          (else_try),
                            (str_store_string, s44, "str_s41"),
                          (try_end),
                          (assign, ":unused_trade_route_found", 1),
                        (try_end),
                        (try_begin),
                          (eq, ":unused_trade_route_found", 1),
                          (str_store_string, s47, "str_there_is_little_news_about_the_caravan_routes_to_the_towns_of_s44_and_nearby_parts_but_no_news_is_good_news_and_those_are_therefore_considered_safe"),
                        (try_end),
                        
                        (assign, ":safe_village_road_found", 0),
                        (try_for_range, ":village", villages_begin, villages_end),
                          (party_slot_eq, ":village", slot_village_market_town, ":center"),
                          (party_slot_eq, ":village", slot_party_temp_slot_1, 0),
                          
                          #		(party_get_slot, ":town_lord", ":village", slot_town_lord),
                          (str_store_party_name, s41, ":village"),
                          (try_begin),
                            (eq, ":safe_village_road_found", 1),
                            (str_store_string, s44, "str_s44_s41"),
                          (else_try),
                            (str_store_string, s44, "str_s41"),
                          (try_end),
                          (assign, ":safe_village_road_found", 1),
                        (try_end),
                        
                        (try_begin),
                          (eq, ":safe_village_road_found", 1),
                          (eq, ":unused_trade_route_found", 1),
                          (str_store_string, s47, "str_s47_also_the_roads_to_the_villages_of_s44_and_other_outlying_hamlets_are_considered_safe"),
                        (else_try),
                          (eq, ":safe_village_road_found", 1),
                          (str_store_string, s47, "str_however_the_roads_to_the_villages_of_s44_and_other_outlying_hamlets_are_considered_safe"),
                        (try_end),
                        
                        (str_store_string, s33, "str_we_have_shortages_of"),
                        (assign, ":some_shortages_found", 0),
                        (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
                          (store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
                          (val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
                          (party_get_slot, ":price", ":center", ":cur_good_price_slot"),
                          (gt, ":price", 1100),
                          
                          (str_store_item_name, s34, ":cur_good"),
                          (assign, reg1, ":price"),
                          (str_store_string, s33, "str_s33_s34_reg1"),
                          
                          (assign, ":some_shortages_found", 1),
                        (try_end),
                        
                        (try_begin),
                          (eq, ":some_shortages_found", 0),
                          (str_store_string, s32, "str_we_have_adequate_stores_of_all_commodities"),
                        (else_try),
                          (str_store_string, s32, "str_s33_and_some_other_commodities"),
                        (try_end),
                        
                        (assign, reg0, ":last_bandit_party_found"),
                        (assign, reg1, ":last_bandit_party_origin"),
                        (assign, reg2, ":last_bandit_party_destination"),
                        (assign, reg3, ":last_bandit_party_hours_ago"),
                        
                        
                      ]
                    ),
                    
                    ("get_manhunt_information_to_s15",
                      [
                        (store_script_param, ":quest", 1),
                        
                        (str_store_string, s15, "str_the_roads_are_full_of_brigands_friend_but_that_name_in_particular_does_not_sound_familiar_good_hunting_to_you_nonetheless"),
                        (quest_get_slot, ":quarry", ":quest", slot_quest_target_party),
                        (try_begin),
                          (is_between, "$g_talk_troop", active_npcs_begin, active_npcs_end),
                          (troop_get_slot, ":talk_party", "$g_talk_troop", slot_troop_leaded_party),
                        (else_try),
                          (gt, "$g_encountered_party", "p_spawn_points_end"),
                          (assign, ":talk_party", "$g_encountered_party"),
                        (else_try),
                          (assign, ":talk_party", -1),
                        (try_end),
                        
                        (try_for_range, ":log_entry", 0, "$num_log_entries"),
                          (gt, ":talk_party", -1),
                          (troop_get_slot, ":party", "trp_log_array_actor", ":log_entry"),
                          (eq, ":party", ":talk_party"),
                          (troop_get_slot, ":bandit_party", "trp_log_array_troop_object", ":log_entry"),
                          (eq, ":bandit_party", ":quarry"),
                          (store_current_hours, ":hours_ago"),
                          (troop_get_slot, ":sighting_time", "trp_log_array_entry_time",  ":log_entry"),
                          (val_sub, ":hours_ago", ":sighting_time"),
                          (try_begin),
                            (le, ":hours_ago", 1),
                            (str_store_string, s16, "str_less_than_an_hour_ago"),
                          (else_try),
                            (le, ":hours_ago", 48),
                            (assign, reg3, ":hours_ago"),
                            (str_store_string, s16, "str_maybe_reg3_hours_ago"),
                          (else_try),
                            (val_div, ":hours_ago", 24),
                            (assign, reg3, ":hours_ago"),
                            (str_store_string, s16, "str_reg3_days_ago"),
                          (try_end),
                          
                          (troop_get_slot, ":center", "trp_log_array_center_object", ":log_entry"),
                          (str_store_party_name, s17, ":center"),
                          (troop_get_slot, ":entry_type", "trp_log_array_entry_type", ":log_entry"),
                          (eq, ":entry_type", logent_party_spots_wanted_bandits),
                          (str_store_string, s15, "str_youre_in_luck_we_sighted_those_bastards_s16_near_s17_hurry_and_you_might_be_able_to_pick_up_their_trail_while_its_still_hot"),
                          
                          #		(try_begin),
                          #			(eq, ":entry_type", logent_party_chases_wanted_bandits),
                          #			(str_store_string, s15, "@You're in luck. We gave chase to those bastards {s16} near {s17}. They have eluded us so far -- but perhaps you will do better..."),
                          #		(else_try),
                          #			(eq, ":entry_type", logent_party_runs_from_wanted_bandits),
                          #			(str_store_string, s15, "@As it happens, they tried to run us down near {s17} {s16}. By the heavens, I hope you teach them a lesson."),
                          #		(try_end),
                        (try_end),
                    ]),
                    
                    
                    #Troop Commentaries end
                    
                    
                    
                    ("rebellion_arguments", #Right now, called only in one place. This is only used when for player overtures, and will need some changes if this script is called when NPCs try to suborn lords
                      [
                        (store_script_param, ":lord", 1),
                        (store_script_param, ":argument", 2),
                        (store_script_param, ":candidate", 3),
                        
                        (assign, ":argument_appeal", 0),
                        (assign, ":argument_strength", 0),
                        
                        (troop_get_slot, ":reputation", ":lord", slot_lord_reputation_type),
                        
                        (store_faction_of_troop, ":lord_faction", ":candidate"),
                        (store_faction_of_troop, ":candidate_faction", ":candidate"),
                        
                        (try_begin),
                          (eq, ":candidate", "trp_player"),
                          (assign, ":right_to_rule", "$player_right_to_rule"),
                        (else_try), #default right to rule of 75 for pretenders claiming throne
                          (is_between, ":candidate", pretenders_begin, pretenders_end),
                          (troop_slot_eq, ":candidate", slot_troop_original_faction, ":lord_faction"),
                          (assign, ":right_to_rule", 75),
                        (else_try), #default right to rule of 60 for all other lords
                          (assign, ":right_to_rule", 60),
                        (try_end),
                        
                        (try_begin),
                          (eq, ":argument", argument_claim),
                          (store_sub, ":argument_strength", ":right_to_rule", 30),
                        (else_try),
                          (eq, ":argument", argument_ruler),
                          (store_sub, ":argument_strength", "$player_honor", 20),
                        (else_try),
                          (eq, ":argument", argument_lords),
                          (store_sub, ":argument_strength", "$player_honor", 20),
                        (else_try),
                          #argument_strength is ((5 * number of centers player have) - 40) if argument type is argument_victory
                          (eq, ":argument", argument_victory),
                          (assign, ":argument_strength", 0),
                          (try_for_range, ":center", centers_begin, centers_end),
                            (store_faction_of_party, ":center_faction", ":center"),
                            (assign, ":argument_strength", -40),
							(try_begin),
								(eq, "$players_kingdom", ":candidate_faction"),
								##diplomacy start+
								(this_or_next|eq, ":center_faction", "$players_kingdom"),
								##diplomacy end+
								(this_or_next|eq, ":center_faction", "fac_player_faction"),
								(eq, ":center_faction", "fac_player_supporters_faction"),
								(val_add, ":argument_strength", 5),
							(else_try),
								(eq, ":center_faction", ":candidate_faction"),
								(val_add, ":argument_strength", 5),
							(try_end),
                          (try_end),
                        (else_try),
                          #argument_strength is (20 - 20 * (number of lords in player's faction which not awareded fief by player although there is a fief awarding in future promise))
                          (eq, ":argument", argument_benefit),
                          (assign, ":argument_strength", 20),
                          (try_for_range, ":lord_promised_fief", active_npcs_begin, active_npcs_end),
                            (store_faction_of_troop, ":other_faction", ":lord_promised_fief"),
                            (neq, ":lord", "$g_talk_troop"),
                            (this_or_next|eq, ":other_faction", "fac_player_supporters_faction"),
                            (eq, ":other_faction", "$players_kingdom"),
                            (troop_slot_eq, ":lord_promised_fief", slot_troop_promised_fief, 1),
                            (val_sub, ":argument_strength", 20),
                          (try_end),
                        (try_end),
                        (val_clamp, ":argument_strength", -40, 41),
                        
                        (try_begin),
                          (eq, ":reputation", lrep_martial),
                          (try_begin),
                            (eq, ":argument", argument_claim),
                            (assign, ":argument_appeal", 30),
                            (try_begin),
                              (gt, ":argument_strength", 0),
                              (str_store_string, s15, "str_you_speak_of_claims_to_the_throne_good_there_is_nothing_id_rather_do_than_fight_for_a_good_cause"),
                            (else_try),
                              (str_store_string, s15, "str_you_speak_of_claims_to_the_throne_well_there_is_nothing_id_rather_do_than_fight_for_a_good_cause_but_the_claim_you_make_seems_somewhat_weak"),
                            (try_end),
                          (else_try),
                            (eq, ":argument", argument_lords),
                            (assign, ":argument_appeal", 10),
                            (try_begin),
                              (gt, ":argument_strength", 0),
                              (str_store_string, s15, "str_i_am_pleased_that_you_speak_of_upholding_my_ancient_rights_which_are_sometimes_trod_upon_in_these_sorry_days"),
                            (else_try),
								##diplomacy start+ use culturally-approrpriate term
								(call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_KING, 14),
								##diplomacy end+
								(str_store_string, s15, "str_i_am_pleased_that_you_speak_of_upholding_my_ancient_rights_but_sometimes_men_make_pledges_before_they_are_king_which_they_cannot_keep_once_they_take_the_throne"),
							 (try_end),
						 (else_try),
							 (eq, ":argument", argument_ruler),
							 (assign, ":argument_appeal", 0),
							 (try_begin),
								##diplomacy start+: use culturally-approrpriate term
								(call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_USE_MY_WEAPON, s14),
								##diplomacy end+
								(str_store_string, s15, "str_you_speak_of_protecting_the_commons_well_i_supposed_thats_good_but_sometimes_the_commons_overstep_their_boundaries_im_more_concerned_that_your_claim_be_legal_so_i_can_swing_my_sword_with_a_good_conscience"),
							 (try_end),
						 (else_try),
							 (eq, ":argument", argument_benefit),
							 (assign, ":argument_appeal", -10),
							 (try_begin),
								(gt, ":argument_strength", 0),
								(str_store_string, s15, "str_you_speak_of_giving_me_land_good_i_ask_for_no_more_than_my_due"),
							 (else_try),
								(str_store_string, s15, "str_you_speak_of_giving_me_land_unfortunately_you_are_not_wellknown_for_rewarding_those_to_whom_you_have_made_such_offers"),
							 (try_end),
						 (else_try),
							 (eq, ":argument", argument_victory),
							 (assign, ":argument_appeal", -30),
							 (str_store_string, s15, "str_you_speak_of_unifying_calradia_well_i_believe_that_well_always_be_fighting__its_important_that_we_fight_for_a_rightful_cause"),
						 (try_end),
					 (else_try),
						(eq, ":reputation", lrep_quarrelsome),
						(try_begin),
							 (eq, ":argument", argument_claim),
							 (assign, ":argument_appeal", -20),
							 (str_store_string, s15, "str_you_talk_of_claims_to_the_throne_but_i_leave_bickering_about_legalities_to_the_lawyers_and_clerks"),
						(else_try),
							 (eq, ":argument", argument_ruler),
							 (assign, ":argument_appeal", -30),
							  ##diplomacy start+ use culturally-approrpriate term
							  (call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_KING, 14),
							  ##diplomacy end+
							 (str_store_string, s15, "str_you_speak_of_ruling_justly_hah_ill_believe_theres_such_a_thing_as_a_just_king_when_i_see_one"),
						(else_try),
							 (eq, ":argument", argument_lords),
							 (assign, ":argument_appeal", 0),
							 ##diplomacy start+ use culturally-approrpriate term
							  (call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_KING, 14),
							  ##diplomacy end+
							 (str_store_string, s15, "str_you_spoke_of_protecting_the_rights_of_the_nobles_if_you_did_youd_be_the_first_king_to_do_so_in_a_very_long_time"),
						(else_try),
							 (eq, ":argument", argument_benefit),
							 (assign, ":argument_appeal", 30),
							 (try_begin),
								(gt, ":argument_strength", 0),
								(str_store_string, s15, "str_you_speak_of_giving_me_land_ay_well_lets_see_if_you_deliver"),
							 (else_try),
								(str_store_string, s15, "str_you_speak_of_giving_me_land_bah_youre_not_known_for_delivering_on_your_pledges"),
							 (try_end),
						(else_try),
							 (eq, ":argument", argument_victory),
							 (assign, ":argument_appeal", 10),
							 (try_begin),
								(gt, ":argument_strength", 0),
								(str_store_string, s15, "str_you_speak_of_unifying_calradia_well_youve_done_a_good_job_at_making_calradia_bend_its_knee_to_you_so_maybe_thats_not_just_talk"),
							 (else_try),
								(str_store_string, s15, "str_you_speak_of_unifying_calradia_id_be_impressed_if_i_thought_you_could_do_it_but_unfortunately_you_dont"),
							 (try_end),
						(try_end),
					 (else_try),
						 (eq, ":reputation", lrep_selfrighteous),
						 (try_begin),
							 (eq, ":argument", argument_claim),
							 (assign, ":argument_appeal", -20),
							 (str_store_string, s15, "str_you_speak_of_claims_to_the_throne_well_any_peasant_can_claim_to_be_a_kings_bastard"),
						 (else_try),
							 (eq, ":argument", argument_ruler),
							 (assign, ":argument_appeal", -30),
							 (str_store_string, s15, "str_well_its_a_fine_thing_to_court_the_commons_with_promises_but_what_do_you_have_to_offer_me"),
						 (else_try),
							 (eq, ":argument", argument_lords),
							 (assign, ":argument_appeal", 0),
							 ##diplomacy start+ use culturally-approrpriate term
							 (call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_LORD_PLURAL, 15),
							 (call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_LORD, 14),
							 ##diplomacy end+
							 (try_begin),
								(gt, ":argument_strength", 0),
								(str_store_string, s15, "str_you_speak_of_protecting_the_rights_of_lords_that_would_make_a_fine_change_if_my_rights_as_lord_would_be_respected"),
							 (else_try),
								(str_store_string, s15, "str_you_speak_of_protecting_the_rights_of_lords_that_would_make_a_fine_change_if_my_rights_as_lord_would_be_respected_however_it_is_easy_for_you_to_make_promises_while_you_are_weak_that_you_have_no_intention_of_keeping_when_you_are_strong"),
							 (try_end),
						 (else_try),
							 (eq, ":argument", argument_benefit),
							 (assign, ":argument_appeal", 20),
							 (try_begin),
								(gt, ":argument_strength", 0),
								(str_store_string, s15, "str_you_speak_of_giving_me_land_well_my_family_is_of_ancient_and_noble_lineage_so_you_promise_me_no_more_than_my_due_still_your_gesture_is_appreciated"),
							 (else_try),
								(str_store_string, s15, "str_you_speak_of_giving_me_land_well_you_make_that_pledge_but_i_am_not_impressed"),
							 (try_end),
						 (else_try),
							 (eq, ":argument", argument_victory),
							 (assign, ":argument_appeal", 20),
							 (try_begin),
								(gt, ":argument_strength", 0),
								(str_store_string, s15, "str_you_speak_of_unifying_calradia_well_much_of_this_land_now_bends_its_knee_to_you_so_perhaps_that_is_not_just_talk"),
							 (else_try),
								(str_store_string, s15, "str_you_speak_of_unifying_calradia_but_right_now_yours_is_just_one_squabbling_faction_among_many"),
							 (try_end),
						 (try_end),
					 (else_try),
						 (eq, ":reputation", lrep_cunning),
						 (try_begin),
							 (eq, ":argument", argument_claim),
							 (assign, ":argument_appeal", -30),
							 (str_store_string, s15, "str_you_speak_of_claims_well_no_offense_but_a_claim_unsupported_by_might_rarely_prospers"),
						 (else_try),
							 (eq, ":argument", argument_ruler),
							 (assign, ":argument_appeal", 10),
							 (try_begin),
								(gt, ":argument_strength", 0),
								(str_store_string, s15, "str_you_speak_of_protecting_the_commons_well_i_suppose_that_will_make_for_a_more_prosperous_realm_ive_always_tried_to_treat_my_peasants_decently_saves_going_to_bed_worrying_about_whether_youll_wake_up_with_the_roof_on_fire"),
							 (else_try),
								(str_store_string, s15, "str_you_speak_of_protecting_the_commons_very_well_but_remember_that_peasants_are_more_likely_to_cause_trouble_if_you_make_promises_then_dont_deliver_than_if_you_never_made_the_promise_in_the_first_place"),
							 (try_end),
						 (else_try),
							 (eq, ":argument", argument_lords),
							 (assign, ":argument_appeal", 15),
							 ##diplomacy start+ use culturally-approrpriate term
							 (call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_KING, 15),
							 (call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_LORD_PLURAL, 14),
							 ##diplomacy end+
							 (try_begin),
								(gt, ":argument_strength", 0),
								(str_store_string, s15, "str_you_speak_of_protecting_the_rights_of_lords_good_youd_be_well_advised_to_do_that__men_fight_better_for_a_king_wholl_respect_their_rights"),
							 (else_try),
								(str_store_string, s15, "str_you_speak_of_protecting_the_rights_of_lords_very_well_but_remember__failing_to_keep_promises_which_you_made_while_scrambling_up_the_throne_is_the_quickest_way_to_topple_off_of_it_once_you_get_there"),
							 (try_end),
						 (else_try),
							 (eq, ":argument", argument_benefit),
							 (assign, ":argument_appeal", -20),
							 (str_store_string, s15, "str_you_speak_of_giving_me_land_very_good_but_often_i_find_that_when_a_man_makes_too_many_promises_trying_to_get_to_the_top_he_has_trouble_keeping_them_once_he_reaches_it"),
						 (else_try),
							 (eq, ":argument", argument_victory),
							 (assign, ":argument_appeal", 20),
							 (try_begin),
								(gt, ":argument_strength", 0),
								(str_store_string, s15, "str_you_speak_of_unifying_calradia_well_many_have_said_that_you_might_very_well_be_the_one_to_do_it"),
							 (else_try),
								(str_store_string, s15, "str_you_speak_of_unifying_calradia_well_all_the_kings_say_that_im_not_sure_that_you_will_succeed_while_they_fail"),
							 (try_end),
						 (try_end),
					 (else_try),
						 (eq, ":reputation", lrep_debauched),
						 (try_begin),
							 (eq, ":argument", argument_claim),
							 (assign, ":argument_appeal", -20),
							 (str_store_string, s15, "str_you_speak_of_claims_do_you_think_i_care_for_the_nattering_of_lawyers"),
						 (else_try),
							 (eq, ":argument", argument_ruler),
							 (assign, ":argument_appeal", -20),
							 ##diplomacy start+ replace "swineherd" with culturally-appropriate term
							 (call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_SWINEHERD, 14),
							 ##diplomacy end+
							 (str_store_string, s15, "str_you_speak_of_protecting_the_commons_how_kind_of_you_i_shall_tell_my_swineherd_all_about_your_sweet_promises_no_doubt_he_will_become_your_most_faithful_vassal"),
						 (else_try),
							 (eq, ":argument", argument_lords),
							 (assign, ":argument_appeal", -10),
							 ##diplomacy start+ replace "lords" with culturally-appropriate term
							 (call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_LORD_PLURAL, 14),
							 ##diplomacy end+
							 (str_store_string, s15, "str_you_speak_of_protecing_the_rights_of_lords_such_sweet_words_but_ill_tell_you_this__the_only_rights_that_are_respected_in_this_world_are_the_rights_to_dominate_whoever_is_weaker_and_to_submit_to_whoever_is_stronger"),
						 (else_try),
							 (eq, ":argument", argument_benefit),
							 (assign, ":argument_appeal", 20),
							 (try_begin),
								(gt, ":argument_strength", 0),
								(str_store_string, s15, "str_you_speak_of_giving_me_land_yes_very_good__but_you_had_best_deliver"),
							 (else_try),
								(str_store_string, s15, "str_you_speak_of_giving_me_land_hah_perhaps_all_those_others_to_whom_you_promised_lands_will_simply_step_aside"),
							 (try_end),
						 (else_try),
							 (eq, ":argument", argument_victory),
							 (assign, ":argument_appeal", 10),
							 (try_begin),
								(gt, ":argument_strength", 0),
								(str_store_string, s15, "str_you_speak_of_unifying_calradia_you_may_indeed_humble_the_other_kings_of_this_land_and_in_that_case_i_would_hope_that_you_would_remember_me_as_your_faithful_servant"),
							 (else_try),
								(str_store_string, s15, "str_you_speak_of_unifying_calradia_but_you_are_weak_and_i_think_that_you_will_remain_weak"),
							 (try_end),
						 (try_end),
					 (else_try),
						 (eq, ":reputation", lrep_goodnatured),
						 (try_begin),
							 (eq, ":argument", argument_claim),
							 (assign, ":argument_appeal", 10),
							 ##diplomacy start+ replace "king" with culturally-appropriate term
							 (call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_KING, 14),
							 ##diplomacy end+
							 (try_begin),
								(gt, ":argument_strength", 0),
								(str_store_string, s15, "str_you_speak_of_claims_its_good_for_a_king_to_have_a_strong_claim_although_admittedly_im_more_concerned_that_he_rules_just_ly_than_with_legalities_anyway_your_claim_seems_wellfounded_to_me"),
							 (else_try),
								(str_store_string, s15, "str_you_speak_of_claims_but_your_claim_seems_a_bit_weak_to_me"),
							 (try_end),
						 (else_try),
							 (eq, ":argument", argument_ruler),
							 (assign, ":argument_appeal", 20),
							 (try_begin),
								(gt, ":argument_strength", 0),
								(str_store_string, s15, "str_you_speak_of_protecting_the_commons_i_like_that_my_tenants_are_a_happy_lot_i_think_but_i_hear_of_others_in_other_estates_that_arent_so_fortunate"),
							 (else_try),
								(str_store_string, s15, "str_you_speak_of_protecting_the_commons_im_glad_to_hear_you_say_that_but_do_me_a_favor__dont_promise_the_commons_anything_you_cant_deliver_thats_a_sure_way_to_get_them_to_rebel_and_it_breaks_my_heart_to_have_to_put_them_down"),
							 (try_end),
						 (else_try),
							 (eq, ":argument", argument_lords),
							 (assign, ":argument_appeal", 0),
							 ##diplomacy start+ use culturally-approrpriate term
							 (call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_KING, 15),
							 (call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_LORD_PLURAL, 14),
							 ##diplomacy end+
							 (str_store_string, s15, "str_you_speak_of_protecting_the_rights_of_lords_well_very_good_i_suppose_but_you_know__we_lords_can_take_of_ourselves_its_the_common_folk_who_need_a_strong_king_to_look_out_for_them_to_my_mind"),
						 (else_try),
							 (eq, ":argument", argument_benefit),
							 (assign, ":argument_appeal", -15),
							 (str_store_string, s15, "str_you_speak_of_giving_me_land_its_kind_of_you_really_though_that_is_not_necessary"),
						 (else_try),
							 (eq, ":argument", argument_victory),
							 (assign, ":argument_appeal", -25),
							 ##diplomacy start+
							 #Save culturally-appropriate variant of "sword" (as in "by the sword") to s14
							 (call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_WEAPON, 14),
							 ##diplomacy end+
							 (str_store_string, s15, "str_you_speak_of_unifying_calradia_well_maybe_you_can_unite_this_land_by_the_sword_but_im_not_sure_that_this_will_make_you_a_good_ruler"),
						 (try_end),
					 (else_try),
						 (eq, ":reputation", lrep_upstanding),
						 (try_begin),
							 (eq, ":argument", argument_claim),
							 (assign, ":argument_appeal", 10),
							 ##diplomacy start+ use culturally-approrpriate term
							 (call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_KING, 14),
							 ##diplomacy end+
							 (try_begin),
								(gt, ":argument_strength", 0),
								(str_store_string, s15, "str_you_speak_of_claims_a_king_must_have_a_strong_legal_claim_for_there_not_to_be_chaos_in_the_realm_and_yours_is_wellestablished"),
							 (else_try),
								(str_store_string, s15, "str_you_speak_of_claims_a_king_must_have_a_strong_legal_claim_for_there_not_to_be_chaos_in_the_realm_but_your_claim_is_not_so_strong"),
							 (try_end),
						 (else_try),
							 (eq, ":argument", argument_lords),
							 (assign, ":argument_appeal", -5),
							 ##diplomacy start+ use culturally-approrpriate term
							 (call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_KING, 14),
							 (call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_LORD_PLURAL, 15),
							 ##diplomacy end+
							 (try_begin),
								(gt, ":argument_strength", 0),
								(str_store_string, s15, "str_you_speak_of_protecting_the_rights_of_lords_it_is_of_course_important_that_a_king_respect_the_rights_of_his_vassals_although_i_worry_that_a_king_who_took_a_throne_without_proper_cause_would_not_rule_with_justice"),
							 (else_try),
								(str_store_string, s15, "str_you_speak_of_protecting_the_rights_of_lords_it_is_of_course_important_that_a_king_respect_the_rights_of_his_vassals_however_i_would_like_to_know_that_you_would_indeed_deliver_on_your_promises"),
							 (try_end),
						 (else_try),
							 (eq, ":argument", argument_ruler),
							 (assign, ":argument_appeal", 5),
							 ##diplomacy start+ use culturally-approrpriate term
							 (call_script, "script_dplmc_print_cultural_word_to_sreg", ":lord", DPLMC_CULTURAL_TERM_KING, 14),
							 ##diplomacy end+
							 (try_begin),
								(gt, ":argument_strength", 0),
								(str_store_string, s15, "str_you_speak_of_protecting_the_commons_i_would_be_pleased_to_serve_a_king_who_respected_the_rights_of_his_subjects_although_i_worry_that_a_king_who_took_a_throne_without_proper_cause_would_not_rule_with_justice"),
							 (else_try),
								(str_store_string, s15, "str_you_speak_of_protecting_the_commons_i_would_be_pleased_to_serve_a_king_who_respected_the_rights_of_his_subjects_however_i_would_like_to_know_that_you_would_indeed_deliver_on_your_promises"),
							 (try_end),
						 (else_try),
							 (eq, ":argument", argument_benefit),
							 (assign, ":argument_appeal", -40),
							 (str_store_string, s15, "str_i_am_not_swayed_by_promises_of_reward"),
						 (else_try),
							 (eq, ":argument", argument_victory),
							 (assign, ":argument_appeal", 10),
							 (try_begin),
								(gt, ":argument_strength", 0),
								(str_store_string, s15, "str_you_speak_of_unifying_calradia_it_would_be_good_to_bring_peace_to_the_realm_and_i_believe_that_you_are_strong_enough_to_do_so"),
							 (else_try),
								(str_store_string, s15, "str_you_speak_of_unifying_calradia_it_would_be_good_to_bring_peace_the_realm_but_with_your_kingdom_in_its_current_state_i_worry_that_you_are_just_bringing_more_discord"),
							 (try_end),
						 (try_end),
					 (try_end),

					 (str_store_string, s14, "str_s15"),

					 (assign, reg0, ":argument_appeal"),
					 (assign, reg1, ":argument_strength"),
				]),
                    
                    
                    
                    #Rebellion changes end
                    
                    # script_get_culture_with_party_faction_for_music
                    # Input: arg1 = party_no
                    # Output: reg0 = culture
                    ("get_culture_with_party_faction_for_music",
                      [
                        (store_script_param, ":party_no", 1),
                        (store_faction_of_party, ":faction_no", ":party_no"),
                        (try_begin),
                          (this_or_next|eq, ":faction_no", "fac_player_faction"),
                          (eq, ":faction_no", "fac_player_supporters_faction"),
                          (assign, ":faction_no", "$players_kingdom"),
                        (try_end),
                        (try_begin),
                          (is_between, ":party_no", centers_begin, centers_end),
                          (this_or_next|eq, ":faction_no", "fac_player_supporters_faction"),
                          (neg|is_between, ":faction_no", kingdoms_begin, kingdoms_end),
                          (party_get_slot, ":faction_no", ":party_no", slot_center_original_faction),
                        (try_end),
                        (call_script, "script_get_culture_with_faction_for_music", ":faction_no"),
                    ]),
                    
                    # script_get_culture_with_faction_for_music
                    # Input: arg1 = party_no
                    # Output: reg0 = culture
                    ("get_culture_with_faction_for_music",
                      [
                        (store_script_param, ":faction_no", 1),
                        (try_begin),
                          (eq, ":faction_no", "fac_kingdom_1"),
                          (assign, ":result", mtf_culture_1),
                        (else_try),
                          (eq, ":faction_no", "fac_kingdom_2"),
                          (assign, ":result", mtf_culture_2),
                        (else_try),
                          (eq, ":faction_no", "fac_kingdom_3"),
                          (assign, ":result", mtf_culture_3),
                        (else_try),
                          (eq, ":faction_no", "fac_kingdom_4"),
                          (assign, ":result", mtf_culture_4),
                        (else_try),
                          (eq, ":faction_no", "fac_kingdom_5"),
                          (assign, ":result", mtf_culture_5),
                        (else_try),
                          (eq, ":faction_no", "fac_kingdom_6"),
                          (assign, ":result", mtf_culture_6),
                          ##Floris: Removed this to make it savegame compatible.
                          #      (else_try),
                          #        (eq, ":faction_no", "fac_player_supporters_faction"),
                          #        (assign, ":result", mtf_culture_1),
                          ##
                          
                          ##Floris: Check it out
                        (else_try),
                          (this_or_next|eq, ":faction_no", "fac_outlaws"),
                          (this_or_next|eq, ":faction_no", "fac_peasant_rebels"),
                          (this_or_next|eq, ":faction_no", "fac_deserters"), ##Diplomacy 3.2
                          (this_or_next|eq, ":faction_no", "fac_mountain_bandits"),
                          (eq, ":faction_no", "fac_forest_bandits"),##
                          (assign, ":result", mtf_culture_6),
                        (else_try),
                          (assign, ":result", 0), #no culture, including player with no bindings to another kingdom
                        (try_end),
                        (assign, reg0, ":result"),
                    ]),
                    
                    # script_music_set_situation_with_culture
                    # Input: arg1 = music_situation
                    # Output: none
                    ("music_set_situation_with_culture",
                      [
                        (store_script_param, ":situation", 1),
                        (assign, ":culture", 0), #no culture
                        (try_begin),
                          (this_or_next|eq, ":situation", mtf_sit_town),
                          (this_or_next|eq, ":situation", mtf_sit_day),
                          (this_or_next|eq, ":situation", mtf_sit_night),
                          (this_or_next|eq, ":situation", mtf_sit_town_infiltrate),
                          (eq, ":situation", mtf_sit_encounter_hostile),
                          (call_script, "script_get_culture_with_party_faction_for_music", "$g_encountered_party"),
                          (val_or, ":culture", reg0),
                        (else_try),
                          (this_or_next|eq, ":situation", mtf_sit_ambushed),
                          (eq, ":situation", mtf_sit_fight),
                          (call_script, "script_get_culture_with_party_faction_for_music", "$g_encountered_party"),
                          (val_or, ":culture", reg0),
                          (call_script, "script_get_culture_with_party_faction_for_music", "p_main_party"),
                          (val_or, ":culture", reg0),
                          (call_script, "script_get_closest_center", "p_main_party"),
                          (call_script, "script_get_culture_with_party_faction_for_music", reg0),
                          (val_or, ":culture", reg0),
                        (else_try),
                          (eq, ":situation", mtf_sit_multiplayer_fight),
                          (call_script, "script_get_culture_with_faction_for_music", "$g_multiplayer_team_1_faction"),
                          (val_or, ":culture", reg0),
                          (call_script, "script_get_culture_with_faction_for_music", "$g_multiplayer_team_2_faction"),
                          (val_or, ":culture", reg0),
                        (else_try),
                          (eq, ":situation", mtf_sit_travel),
                          (call_script, "script_get_culture_with_party_faction_for_music", "p_main_party"),
                          (val_or, ":culture", reg0),
                          (call_script, "script_get_closest_center", "p_main_party"),
                          (call_script, "script_get_culture_with_party_faction_for_music", reg0),
                          (val_or, ":culture", reg0),
                        (else_try),
                          (eq, ":situation", mtf_sit_victorious),
                          (call_script, "script_get_culture_with_party_faction_for_music", "p_main_party"),
                          (val_or, ":culture", reg0),
                        (else_try),
                          (eq, ":situation", mtf_sit_killed),
                          (call_script, "script_get_culture_with_party_faction_for_music", "$g_encountered_party"),
                          (val_or, ":culture", reg0),
                        (try_end),
                        (try_begin),
                          (this_or_next|eq, ":situation", mtf_sit_town),
                          (eq, ":situation", mtf_sit_day),
                          (try_begin),
                            (is_currently_night),
                            (assign, ":situation", mtf_sit_night),
                          (try_end),
                        (try_end),
                        (music_set_situation, ":situation"),
                        (music_set_culture, ":culture"),
                    ]),
                    
                    
                    # script_combat_music_set_situation_with_culture
                    # Input: none
                    # Output: none
                    ("combat_music_set_situation_with_culture",
                      [
                        (assign, ":situation", mtf_sit_fight),
                        (assign, ":num_allies", 0),
                        (assign, ":num_enemies", 0),
                        (try_for_agents, ":agent_no"),
                          (agent_is_alive, ":agent_no"),
                          (agent_is_human, ":agent_no"),
                          (agent_get_troop_id, ":agent_troop_id", ":agent_no"),
                          (store_character_level, ":troop_level", ":agent_troop_id"),
                          (val_add,  ":troop_level", 10),
                          (val_mul, ":troop_level", ":troop_level"),
                          (try_begin),
                            (agent_is_ally, ":agent_no"),
                            (val_add, ":num_allies", ":troop_level"),
                          (else_try),
                            (val_add, ":num_enemies", ":troop_level"),
                          (try_end),
                        (try_end),
                        (val_mul, ":num_allies", 4), #play ambushed music if we are 2 times outnumbered.
                        (val_div, ":num_allies", 3),
                        (try_begin),
                          (lt, ":num_allies", ":num_enemies"),
                          (assign, ":situation", mtf_sit_ambushed),
                        (try_end),
                        (call_script, "script_music_set_situation_with_culture", ":situation"),
                    ]),
                    
                    # script_play_victorious_sound
                    # Input: none
                    # Output: none
                    ("play_victorious_sound",
                      [
                        (call_script, "script_music_set_situation_with_culture", mtf_sit_victorious),
                        #      (play_cue_track, "track_victorious_neutral_1"),
                        #      (play_track, "track_victorious_neutral_1", 1),
                    ]),
                    
                    # script_set_items_for_tournament
                    # Input: arg1 = horse_chance, arg2 = lance_chance (with horse only), arg3 = sword_chance, arg4 = axe_chance, arg5 = bow_chance (without horse only), arg6 = javelin_chance (with horse only), arg7 = mounted_bow_chance (with horse only), arg8 = crossbow_sword_chance, arg9 = armor_item_begin, arg10 = helm_item_begin
                    # Output: none (sets mt_arena_melee_fight items)
                    ("set_items_for_tournament",
                      [
                        (store_script_param, ":horse_chance", 1),
                        (store_script_param, ":lance_chance", 2),
                        (store_script_param, ":sword_chance", 3),
                        (store_script_param, ":axe_chance", 4),
                        (store_script_param, ":bow_chance", 5),
                        (store_script_param, ":javelin_chance", 6),
                        (store_script_param, ":mounted_bow_chance", 7),
                        (store_script_param, ":crossbow_sword_chance", 8),
                        (store_script_param, ":armor_item_begin", 9),
                        (store_script_param, ":helm_item_begin", 10),
                        (store_add, ":total_chance", ":sword_chance", ":axe_chance"),
                        (val_add, ":total_chance", ":crossbow_sword_chance"),
                        (try_for_range, ":i_ep", 0, 32),
                          (mission_tpl_entry_clear_override_items, "mt_arena_melee_fight", ":i_ep"),
                          (assign, ":has_horse", 0),
                          (store_div, ":cur_team", ":i_ep", 8),
                          (try_begin),
                            (store_random_in_range, ":random_no", 0, 100),
                            (lt, ":random_no", ":horse_chance"),
                            (assign, ":has_horse", 1),
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_horse"),
                          (try_end),
                          (try_begin),
                            (eq, ":has_horse", 1),
                            (store_add, ":cur_total_chance", ":total_chance", ":lance_chance"),
                            (val_add, ":cur_total_chance", ":javelin_chance"),
                            (val_add, ":cur_total_chance", ":mounted_bow_chance"),
                          (else_try),
                            (store_add, ":cur_total_chance", ":total_chance", ":bow_chance"),
                          (try_end),
                          (store_random_in_range, ":random_no", 0, ":cur_total_chance"),
                          (store_add, ":cur_shield_item", "itm_arena_shield_red", ":cur_team"),
                          (try_begin),
                            (val_sub, ":random_no", ":sword_chance"),
                            (lt, ":random_no", 0),
                            (try_begin),
                              (store_random_in_range, ":sub_random_no", 0, 100),
                              (lt, ":sub_random_no", 50),
                              (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_sword"),
                              (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
                              #            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_shield"),
                            (else_try),
                              (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_sword_heavy"),
                            (try_end),
                          (else_try),
                            (val_sub, ":random_no", ":axe_chance"),
                            (lt, ":random_no", 0),
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_axe"),
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
                            #         (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_shield"),
                          (else_try),
                            (val_sub, ":random_no", ":crossbow_sword_chance"),
                            (lt, ":random_no", 0),
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_sword"),
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_crossbow"),
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_bolts"),
                          (else_try),
                            (eq, ":has_horse", 0),
                            (val_sub, ":random_no", ":bow_chance"),
                            (lt, ":random_no", 0),
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_bow"),
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_arrows"),
                            #(mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_dagger"),
                            #LAZERAS MODIFIED  {Backup Weapon}
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_sword"),
                            #LAZERAS MODIFIED  {Backup Weapon}
                          (else_try),
                            (eq, ":has_horse", 1),
                            (val_sub, ":random_no", ":lance_chance"),
                            (lt, ":random_no", 0),
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_lance"),
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
                            #          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_shield"),
                            #LAZERAS MODIFIED  {Backup Weapon}
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_sword"),
                            #LAZERAS MODIFIED  {Backup Weapon}
                          (else_try),
                            (eq, ":has_horse", 1),
                            (val_sub, ":random_no", ":javelin_chance"),
                            (lt, ":random_no", 0),
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_javelin"),
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_shield_item"),
                            #          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_shield"),
                            #LAZERAS MODIFIED  {Backup Weapon}
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_sword"),
                            #LAZERAS MODIFIED  {Backup Weapon}
                          (else_try),
                            (eq, ":has_horse", 1),
                            (val_sub, ":random_no", ":mounted_bow_chance"),
                            (lt, ":random_no", 0),
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_bow"),
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_arrows"),
                            #          (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_dagger"),
                            #LAZERAS MODIFIED  {Backup Weapon}
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", "itm_practice_sword"),
                            #LAZERAS MODIFIED  {Backup Weapon}
                          (try_end),
                          (try_begin),
                            (ge, ":armor_item_begin", 0),
                            (store_add, ":cur_armor_item", ":armor_item_begin", ":cur_team"),
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_armor_item"),
                          (try_end),
                          (try_begin),
                            (ge, ":helm_item_begin", 0),
                            (store_add, ":cur_helm_item", ":helm_item_begin", ":cur_team"),
                            (mission_tpl_entry_add_override_item, "mt_arena_melee_fight", ":i_ep", ":cur_helm_item"),
                          (try_end),
                        (try_end),
                    ]),
                    
                    
                    # script_custom_battle_end
                    # Input: none
                    # Output: none
                    ("custom_battle_end",
                      [
                        (assign, "$g_custom_battle_team1_death_count", 0),
                        (assign, "$g_custom_battle_team2_death_count", 0),
                        (get_player_agent_no, ":player_agent"),
                        (agent_get_team, ":player_team", ":player_agent"),
                        (try_for_agents, ":cur_agent"),
                          (agent_is_human, ":cur_agent"),
                          (neg|agent_is_alive, ":cur_agent"),
                          (agent_get_team, ":cur_team", ":cur_agent"),
                          (try_begin),
                            (eq, ":cur_team", ":player_team"),
                            (val_add, "$g_custom_battle_team1_death_count", 1),
                          (else_try),
                            (val_add, "$g_custom_battle_team2_death_count", 1),
                          (try_end),
                        (try_end),
                    ]),
                    
                    # script_remove_troop_from_prison
                    # Input: troop_no
                    # Output: none
                    #Other search terms: release, peace
                    
                    ("remove_troop_from_prison",
                      [
                        (store_script_param, ":troop_no", 1),
                        (troop_set_slot, ":troop_no", slot_troop_prisoner_of_party, -1),
                        (try_begin),
                          (eq, "$do_not_cancel_quest", 0),
                          (check_quest_active, "qst_rescue_lord_by_replace"),
                          (quest_slot_eq, "qst_rescue_lord_by_replace", slot_quest_target_troop, ":troop_no"),
                          (call_script, "script_cancel_quest", "qst_rescue_lord_by_replace"),
                        (try_end),
                        (try_begin),
                          (eq, "$do_not_cancel_quest", 0),
                          (check_quest_active, "qst_rescue_prisoner"),
                          (quest_slot_eq, "qst_rescue_prisoner", slot_quest_target_troop, ":troop_no"),
                          (call_script, "script_cancel_quest", "qst_rescue_prisoner"),
                        (try_end),
                        (try_begin),
                          (check_quest_active, "qst_deliver_message_to_prisoner_lord"),
                          (quest_slot_eq, "qst_deliver_message_to_prisoner_lord", slot_quest_target_troop, ":troop_no"),
                          (call_script, "script_cancel_quest", "qst_deliver_message_to_prisoner_lord"),
                        (try_end),
                    ]),
                    
                    ## Companions Overview, by Jedediah Q, modified by lazeras
                    # (lvl 2-12)  600,1360, 2296, 3426, 4768, 6345, 8179, 10297, 13010, 16161, 19806,
                    # (lvl 13-21) 24007, 28832, 34362, 40682, 47892, 56103, 65441, 77233, 90809
                    # (lvl 22-31) 106425, 124371, 144981, 168636, 195769, 226879, 262533, 303381, 350164, 412091
                    # script_jq_xp_to_next_lvl
                    # Input: xp points
                    # Output: none
                    ("jq_xp_to_next_lvl",
                      [
                        (store_script_param, ":jq_xpvalue", 1),
                        (try_begin),
                          (lt, ":jq_xpvalue",600),
                          (assign, ":jq_xpvalue2", 600),
                        (else_try),
                          (lt, ":jq_xpvalue",1360),
                          (assign, ":jq_xpvalue2", 1360),
                        (else_try),
                          (lt, ":jq_xpvalue",2296),
                          (assign, ":jq_xpvalue2", 2296),
                        (else_try),
                          (lt, ":jq_xpvalue",3426),
                          (assign, ":jq_xpvalue2", 3426),
                        (else_try),
                          (lt, ":jq_xpvalue",4768),
                          (assign, ":jq_xpvalue2", 4768),
                        (else_try),
                          (lt, ":jq_xpvalue",6345),
                          (assign, ":jq_xpvalue2", 6345),
                        (else_try),
                          (lt, ":jq_xpvalue",8179),
                          (assign, ":jq_xpvalue2", 8179),
                        (else_try),
                          (lt, ":jq_xpvalue",10297),
                          (assign, ":jq_xpvalue2", 10297),
                        (else_try),
                          (lt, ":jq_xpvalue",13010),
                          (assign, ":jq_xpvalue2", 13010),
                        (else_try),
                          (lt, ":jq_xpvalue",16161),
                          (assign, ":jq_xpvalue2", 16161),
                        (else_try),
                          (lt, ":jq_xpvalue",19806),
                          (assign, ":jq_xpvalue2", 19806),
                        (else_try),
                          (lt, ":jq_xpvalue",24007),
                          (assign, ":jq_xpvalue2", 24007),
                        (else_try),
                          (lt, ":jq_xpvalue",28832),
                          (assign, ":jq_xpvalue2", 28832),
                        (else_try),
                          (lt, ":jq_xpvalue",34362),
                          (assign, ":jq_xpvalue2", 34362),
                        (else_try),
                          (lt, ":jq_xpvalue",40682),
                          (assign, ":jq_xpvalue2", 40682),
                        (else_try),
                          (lt, ":jq_xpvalue",47892),
                          (assign, ":jq_xpvalue2", 47892),
                        (else_try),
                          (lt, ":jq_xpvalue",56103),
                          (assign, ":jq_xpvalue2", 56103),
                        (else_try),
                          (lt, ":jq_xpvalue",65441),
                          (assign, ":jq_xpvalue2", 65441),
                        (else_try),
                          (lt, ":jq_xpvalue",77233),
                          (assign, ":jq_xpvalue2", 77233),
                        (else_try),
                          (lt, ":jq_xpvalue",90809),
                          (assign, ":jq_xpvalue2", 90809),
                        (else_try),
                          (lt, ":jq_xpvalue",106425),
                          (assign, ":jq_xpvalue2", 106425),
                        (else_try),
                          (lt, ":jq_xpvalue",124371),
                          (assign, ":jq_xpvalue2", 124371),
                        (else_try),
                          (lt, ":jq_xpvalue",144981),
                          (assign, ":jq_xpvalue2", 144981),
                        (else_try),
                          (lt, ":jq_xpvalue",168636),
                          (assign, ":jq_xpvalue2", 168636),
                        (else_try),
                          (lt, ":jq_xpvalue",195769),
                          (assign, ":jq_xpvalue2", 195769),
                        (else_try),
                          (lt, ":jq_xpvalue",226879),
                          (assign, ":jq_xpvalue2", 226879),
                        (else_try),
                          (lt, ":jq_xpvalue",262533),
                          (assign, ":jq_xpvalue2", 262533),
                        (else_try),
                          (lt, ":jq_xpvalue",303381),
                          (assign, ":jq_xpvalue2", 303381),
                        (else_try),
                          (lt, ":jq_xpvalue",350164),
                          (assign, ":jq_xpvalue2", 350164),
                        (else_try),
                          (lt, ":jq_xpvalue",412091),
                          (assign, ":jq_xpvalue2", 412091),
                          
                          # Feel free to continue from here on. I'm just lazy...
                          
                        (try_end),
                        (store_sub, reg1, ":jq_xpvalue2", ":jq_xpvalue"),
                        (str_store_string, s1, "@{reg1}"),
                    ]),
                    # -----------------------------------------------------------------------------------------------------------
                    # -----------------------------------------------------------------------------------------------------------
                    # script_jq_extra_stats - get extra info about the selected hero in 'Companions Overview'
                    # Input: Selected hero, Morale slot nr in 'trp_temp_array_c'
                    # Output: none
                    ("jq_extra_stats",
                      [
                        (store_script_param, ":jq_troop_no", 1),
                        (store_script_param, ":jq_morl", 2),
                        (assign, reg5, ":jq_morl"),
                        (assign, "$jq_last_checked_hero", ":jq_troop_no"),
                        (str_store_troop_name, s9, ":jq_troop_no"),
                        (store_troop_health , reg2, ":jq_troop_no"),
                        (store_character_level, reg3, ":jq_troop_no"),
                        (troop_get_slot, reg4, "trp_temp_array_c", ":jq_morl"),
                        (str_store_string, s1, "@{s9}^^^Level: {reg3}^Health: {reg2}%^Morale: {reg4}"),
                        #(str_store_string, s1, "@{s9}^^^Level: {reg3}^Health: {reg2}%^Morale: {reg4} jq_morl: {reg5}"),
                        (overlay_set_text, "$g_jq_equipment_status", s1),
                        
                        (try_for_range, ":jq_cur_slot", 0, 8),#equipment slots
                          (troop_get_inventory_slot, reg1, ":jq_troop_no", ":jq_cur_slot"),
                          (try_begin),
                            (lt, reg1, 1), # if item slot is empty...
                            (str_store_string, s8, "@________________n/a________________"),
                          (else_try),
                            (str_store_item_name, s8, reg1),
                          (try_end),
                          (try_begin),
                            (eq, ":jq_cur_slot", 0),
                            (overlay_set_text, "$g_jq_equipment_item0", s8),
                          (else_try),
                            (eq, ":jq_cur_slot", 1),
                            (overlay_set_text, "$g_jq_equipment_item1", s8),
                          (else_try),
                            (eq, ":jq_cur_slot", 2),
                            (overlay_set_text, "$g_jq_equipment_item2", s8),
                          (else_try),
                            (eq, ":jq_cur_slot", 3),
                            (overlay_set_text, "$g_jq_equipment_item3", s8),
                          (else_try),
                            (eq, ":jq_cur_slot", 4),
                            (overlay_set_text, "$g_jq_equipment_item4", s8),#head
                          (else_try),
                            (eq, ":jq_cur_slot", 5),
                            (overlay_set_text, "$g_jq_equipment_item5", s8),#body
                          (else_try),
                            (eq, ":jq_cur_slot", 6),
                            (overlay_set_text, "$g_jq_equipment_item6", s8),#feet
                          (else_try),
                            (eq, ":jq_cur_slot", 7),
                            (overlay_set_text, "$g_jq_equipment_item7", s8),#hands
                          (try_end),
                        (try_end), # try-for-range-loop-end
                        (set_result_string, s8),
                    ]),
                    # --------------------------------------------------------------------------------------
                    # script_jq_browse - browse thru party in 'extended view'
                    # INPUT:
                    # param1: selected hero (":dude")
                    # param2: slot nr
                    # Output: All
                    ("jq_browse",
                      [
                        
                        (store_script_param, ":jq_troop_no", 1),
                        (assign, "$jq_last_checked_hero", ":jq_troop_no"),
                        
                        (str_store_troop_name, s9, "$jq_dude"),
                        (overlay_set_text, "$jq_troop_name", s9),
                        
                        (str_store_string, s9, "@{s9} feels..."),
                        (overlay_set_text, "$jq_mrlc", s9),
                        (call_script, "script_npc_morale", "$jq_dude"),
                        (overlay_set_text,  "$jq_feeling1", s6),
                        (overlay_set_text,  "$jq_feeling2", s7),
                        (overlay_set_text,  "$jq_feeling3", s8),
                        (troop_get_slot, ":home", "$jq_dude", slot_troop_home),
                        (str_store_party_name, 21, ":home"),
                        (str_store_string, s9, "@Morale: {reg0}^^Origin: {s21}"),
                        (overlay_set_text,  "$jq_comphome", s9),
                        (try_begin),
                          (troop_is_mounted,  "$jq_dude"),
                          (str_store_string, s1, "@State: Riding"),
                        (else_try),
                          (str_store_string, s1, "@State: On foot"),
                        (try_end),
                        (overlay_set_text,  "$jq_state", s1),
                        
                        #Draw the troop
                        (overlay_set_alpha, "$jq_portrait", 0xFF),
                        (set_fixed_point_multiplier, 1000),
                        (position_set_x, pos1, 1150),
                        (position_set_y, pos1, 1150),
                        (overlay_set_size, "$jq_portrait", pos1),
                        (position_set_x, pos1, 10),
                        (position_set_y, pos1, 295),
                        (position_set_z, pos1, 170),
                        (overlay_set_position, "$jq_portrait", pos1),
                        
                        (store_attribute_level, reg1, "$jq_dude", ca_strength),
                        (str_store_string, s1, "@_{reg1}_"),
                        (overlay_set_text, "$jqregstr", s1),
                        
                        (store_attribute_level, reg1, "$jq_dude", ca_agility),
                        (str_store_string, s1, "@_{reg1}_"),
                        (overlay_set_text, "$jqregagi", s1),
                        
                        (store_attribute_level, reg1, "$jq_dude", ca_intelligence),
                        (str_store_string, s1, "@_{reg1}_"),
                        (overlay_set_text, "$jqregint", s1),
                        
                        (store_attribute_level, reg1, "$jq_dude", ca_charisma),
                        (str_store_string, s1, "@_{reg1}_"),
                        (overlay_set_text, "$jqregcha", s1),
                        
                        (store_troop_health, reg1,  "$jq_dude"),
                        (str_store_string, s1, "@_{reg1}%"),
                        (overlay_set_text, "$jqhealth", s1),
                        
                        (store_character_level, reg1, "$jq_dude"),
                        (str_store_string, s1, "@_{reg1}_"),
                        (overlay_set_text, "$jqreglvl", s1),
                        
                        (troop_get_xp, ":jqreg", "$jq_dude"),
                        (call_script, "script_jq_xp_to_next_lvl", ":jqreg"),
                        (overlay_set_text, "$jqtonextlvl", s1),
                        
                        # Skills Values
                        (str_clear, s1),
                        (try_for_range_backwards, reg1, 0, 37),
                          (neg|is_between, reg1, 3, 7),
                          (neg|is_between, reg1, 18, 22),
                          (neg|is_between, reg1, 28, 33),
                          (store_skill_level, reg2, reg1, "$jq_dude"),
                          (str_store_string, s1, "@{s1}^{reg2}"),
                          (overlay_set_text, "$jq_allskills",  s1),
                        (try_end),
                        
                        #PROFICIENCIES #spelling contest
                        (str_clear, s1),
                        (store_proficiency_level,  reg1, "$jq_dude", wpt_one_handed_weapon),
                        (str_store_string, s1, "@{s1}^^{reg1}"),
                        (store_proficiency_level,  reg1, "$jq_dude", wpt_two_handed_weapon),
                        (str_store_string, s1, "@{s1}^^{reg1}"),
                        (store_proficiency_level,  reg1, "$jq_dude", wpt_polearm),
                        (str_store_string, s1, "@{s1}^^{reg1}"),
                        (store_proficiency_level,  reg1, "$jq_dude", wpt_archery),
                        (str_store_string, s1, "@{s1}^^{reg1}"),
                        (store_proficiency_level,  reg1, "$jq_dude", wpt_crossbow),
                        (str_store_string, s1, "@{s1}^^{reg1}"),
                        (store_proficiency_level,  reg1, "$jq_dude", wpt_throwing),
                        (str_store_string, s1, "@{s1}^^{reg1}"),
                        (store_proficiency_level,  reg1, "$jq_dude", wpt_firearm),
                        (str_store_string, s1, "@{s1}^^{reg1}"),
                        (overlay_set_text, "$jq_allprofs",  s1),
                        
                        (try_for_range, ":jq_cur_slot", 0, 8),#equipment slots
                          (troop_get_inventory_slot, reg1, "$jq_dude", ":jq_cur_slot"),
                          (try_begin),
                            (lt, reg1, 1), # if item slot is empty...
                            (str_store_string, s8, "@n/a________________________________"),
                          (else_try),
                            (str_store_item_name, s8, reg1),
                          (try_end),
                          (try_begin),
                            (eq, ":jq_cur_slot", 0),
                            (overlay_set_text, "$g_jq_equipment_item0", s8),
                          (else_try),
                            (eq, ":jq_cur_slot", 1),
                            (overlay_set_text, "$g_jq_equipment_item1", s8),
                          (else_try),
                            (eq, ":jq_cur_slot", 2),
                            (overlay_set_text, "$g_jq_equipment_item2", s8),
                          (else_try),
                            (eq, ":jq_cur_slot", 3),
                            (overlay_set_text, "$g_jq_equipment_item3", s8),
                          (else_try),
                            (eq, ":jq_cur_slot", 4),
                            (overlay_set_text, "$g_jq_equipment_item4", s8),# head
                          (else_try),
                            (eq, ":jq_cur_slot", 5),
                            (overlay_set_text, "$g_jq_equipment_item5", s8),# body
                          (else_try),
                            (eq, ":jq_cur_slot", 6),
                            (overlay_set_text, "$g_jq_equipment_item6", s8),# feet
                          (else_try),
                            (eq, ":jq_cur_slot", 7),
                            (overlay_set_text, "$g_jq_equipment_item7", s8),# hands
                          (try_end),
                        (try_end), # try-for-range-loop-end
                        
                    ]),
                    ##
                    
                    # script_debug_variables
                    # Input: two variables which will be examined by coder, this script is only for debugging.
                    # Output: none
                    ("debug_variables",
                      [
                        (store_script_param, ":unused", 1),
                        (store_script_param, ":unused_2", 2),
                    ]),
                    
                    #lord recruitment scripts begin
                    ("troop_describes_troop_to_s15",
                      [
                        (store_script_param, ":troop_1", 1),
                        (store_script_param, ":troop_2", 2),
                        
                        
                        (str_store_troop_name, s15, ":troop_2"),
                        
                        (try_begin),
                          (eq, ":troop_2", "trp_player"),
                          (str_store_string, s15, "str_you"),
                        (else_try),
                          (eq, ":troop_2", ":troop_1"),
                          (str_store_string, s15, "str_myself"),
                        (else_try),
                          (call_script, "script_troop_get_family_relation_to_troop", ":troop_2", ":troop_1"),
                          (gt, reg0, 0),
                          (str_store_string, s15, "str_my_s11_s15"),
                        (else_try),
                          (call_script, "script_troop_get_relation_with_troop", ":troop_2", ":troop_1"),
                          (ge, reg0, 20),
                          (str_store_string, s15, "str_my_friend_s15"),
                        (try_end),
                        
                    ]),
                    
                    ("troop_describes_quarrel_with_troop_to_s14",
                      #perhaps replace this with get_relevant_comment at a later date
                      [
                        (store_script_param, ":troop", 1),
                        (store_script_param, ":troop_2", 2),
                        
                        (str_store_troop_name, s15, ":troop"),
                        (str_store_troop_name, s16, ":troop_2"),
                        
                        (str_store_string, s14, "str_stop_gap__s15_is_the_rival_of_s16"),
                        
                        (try_begin),
                          (eq, ":troop", "$g_talk_troop"),
                          (call_script, "script_cf_test_lord_incompatibility_to_s17", ":troop", ":troop_2"),
                          (str_store_string, s14, s17), ##1.132, new line
                        (else_try),
                          (eq, ":troop_2", "$g_talk_troop"),
                          (call_script, "script_cf_test_lord_incompatibility_to_s17", ":troop_2", ":troop"),
                          (str_store_string, s14, s17), ##1.132, 3 new lines
                        (else_try),
                          (str_store_string, s14, "str_general_quarrel"),##
                        (try_end),
                        #	(str_store_string, s14, s17), ##1.131, this line is removed in 1.132
                    ]),
                    
                    ("cf_test_lord_incompatibility_to_s17", #writes rivalry chance to reg0
                      [
                        
                        (store_script_param, ":source_lord", 1),
                        (store_script_param, ":target_lord", 2),
                        
                        
                        (assign, ":chance_of_rivalry", 0),
                        
                        (troop_get_slot, ":source_reputation", ":source_lord", slot_lord_reputation_type),
                        (troop_get_slot, ":target_reputation", ":target_lord", slot_lord_reputation_type),
                        
						##diplomacy start+ Note: the next line is in native, but as far as I can discern the register value wasn't actually used.
						(troop_get_type, reg15, ":target_lord"),
						##diplomacy end+
                        
                        (str_store_troop_name, s18, ":target_lord"),
                        
                        (assign, ":divisor", 1),
                        
                        (call_script, "script_troop_get_family_relation_to_troop", ":target_lord", ":source_lord"),
                        (assign, ":family_relationship", reg0),
                        
                        (try_begin),
                          (gt, ":family_relationship", 0),
                          (store_div, ":family_divisor", reg0, 5),
                          (val_add, ":divisor", ":family_divisor"),
                          (str_store_string, s18, "str_my_s11_s18"),
                        (else_try),
                          (gt, ":target_reputation", lrep_upstanding),
                          (this_or_next|eq, ":source_reputation", lrep_debauched),
                          (eq, ":source_reputation", lrep_selfrighteous),
                          (str_store_string, s18, "str_the_socalled_s11_s18"),
                        (try_end),
                        
					   ##diplomacy start+ get gender types
						(assign, ":save_reg65", reg65),#save register values to revert at end of script
						(assign, ":save_reg3", reg3),
						(call_script, "script_dplmc_store_troop_is_female_reg", ":target_lord", 3),#reg3 used below for gender-correct pronouns
						(call_script, "script_dplmc_store_troop_is_female", ":source_lord"),
					   (assign, reg65, reg0),#used below in some situations for speaker
					   (assign, reg0, ":family_relationship"),#revert register to value before this section
						##diplomacy end+
						(try_begin), #test if reps are compatible
                          (eq, ":source_reputation", lrep_martial),
                          (is_between, ":family_relationship", 1, 5), #uncles and cousins
                          
                          (assign, ":chance_of_rivalry", 100),
                          (str_store_string, s17, "str_s18_would_cheat_me_of_my_inheritance_by_heaven_i_know_my_rights_and_im_not_going_to_back_down"),
                        (else_try),
                          (eq, ":source_reputation", lrep_martial),
                          (eq, ":target_reputation", lrep_quarrelsome),
                          (str_store_string, s17, "str_s18_once_questioned_my_honour_and_my_bravery_i_long_for_the_day_when_i_can_meet_him_in_battle_and_make_him_retract_his_statement"),
                          (assign, ":chance_of_rivalry", 50),
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_martial),
                          (eq, ":target_reputation", lrep_upstanding),
                          (str_store_string, s17, "str_s18_once_questioned_my_judgment_in_battle_by_heaven_would_he_have_us_shirk_our_duty_to_smite_our_sovereigns_foes"),
                          (assign, ":chance_of_rivalry", 50),
                          
                        (else_try),
                          (eq, ":target_reputation", lrep_martial),
                          (is_between, ":family_relationship", 1, 5),
                          
                          (assign, ":chance_of_rivalry", 100),
                          (str_store_string, s17, "str_s18_seems_to_think_he_has_the_right_to_some_of_my_property_well_he_does_not"),
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_quarrelsome),
                          (eq, ":target_reputation", lrep_martial),
                          (str_store_string, s17, "str_s18_once_took_something_i_said_amiss_stubborn_bastard_wont_give_it_up_and_keeps_trying_to_get_me_to_recant_my_words"),
                          (assign, ":chance_of_rivalry", 50),
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_quarrelsome),
                          (eq, ":target_reputation", lrep_cunning),
                          (str_store_string, s17, "str_s18_is_a_crafty_weasel_and_i_dont_trust_him_one_bit"),
                          (assign, ":chance_of_rivalry", 100),
                          
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_debauched),
                          (eq, ":target_reputation", lrep_upstanding),
                          (str_store_string, s17, "str_s18_i_despite_him_he_puts_on_such_a_nauseating_display_of_virtue_and_thinks_nothing_of_insulting_his_betters"),
                          (assign, ":chance_of_rivalry", 100),
                          
                          #debauched insults upstanding
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_debauched),
                          (eq, ":target_reputation", lrep_selfrighteous),
                          (str_store_string, s17, "str_s18_entered_into_a_little_deal_with_me_and_is_now_trying_to_wriggle_out_of_it"),
                          (assign, ":chance_of_rivalry", 100),
                          
                          #debauched insults selfrighteous
                          
                          
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_selfrighteous),
                          (eq, ":target_reputation", lrep_debauched),
                          (str_store_string, s17, "str_s18_once_ran_an_errand_for_me_and_now_thinks_i_owe_him_something_i_owe_his_ilk_nothing"),
                          (assign, ":chance_of_rivalry", 100),
                          #selfrighteous dismisses debauched
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_selfrighteous),
                          (eq, ":target_reputation", lrep_goodnatured),
                          (str_store_string, s17, "str_s18_is_soft_and_weak_and_not_fit_to_govern_a_fief_and_i_have_always_detested_him"),
                          (assign, ":chance_of_rivalry", 100),
                          
                          
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_cunning),
                          (eq, ":target_reputation", lrep_quarrelsome),
                          (str_store_string, s17, "str_s18_is_a_quarrelsome_oaf_and_a_liability_in_my_opinion_and_ive_let_him_know_as_much"),
                          (assign, ":chance_of_rivalry", 100),
                          #cunning insults quarrelsome
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_cunning),
                          (eq, ":target_reputation", lrep_goodnatured),
                          (str_store_string, s17, "str_s18_i_am_sorry_to_say_is_far_too_softhearted_a_man_to_be_given_any_kind_of_responsibility_his_chivalry_will_allow_the_enemy_to_flee_to_fight_another_day_and_will_cost_the_lives_of_my_own_faithful_men"),
                          (assign, ":chance_of_rivalry", 100),
                          
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_goodnatured),
                          (eq, ":target_reputation", lrep_cunning),
                          (str_store_string, s17, "str_s18_seems_to_have_something_against_me_for_some_reason_i_dont_like_to_talk_ill_of_people_but_i_think_hes_can_be_a_bit_of_a_cad_sometimes"),
                          (assign, ":chance_of_rivalry", 100),
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_goodnatured),
                          (eq, ":target_reputation", lrep_selfrighteous),
                          (str_store_string, s17, "str_s18_has_always_treated_me_contemptuously_although_i_have_done_him_no_wrong"),
                          (assign, ":chance_of_rivalry", 100),
                          
                          
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_upstanding),
                          (eq, ":target_reputation", lrep_debauched),
                          (str_store_string, s17, "str_s18_is_thoroughly_dishonorable_and_a_compulsive_spinner_of_intrigues_which_i_fear_will_drag_us_into_wars_or_incite_rebellions"),
                          (assign, ":chance_of_rivalry", 50),
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_upstanding),
                          (eq, ":target_reputation", lrep_martial),
                          (str_store_string, s17, "str_s18_disappoints_me_i_once_scolded_for_his_rashness_in_battle_and_he_took_offense_i_do_not_care_to_apologize_for_my_efforts_to_save_his_life_and_the_lives_of_his_men"),
                          (assign, ":chance_of_rivalry", 50),
                          
                          #for commons
                        (else_try),
                          (this_or_next|eq, ":source_reputation", lrep_upstanding),
                          (this_or_next|eq, ":source_reputation", lrep_martial),
                          (eq, ":source_reputation", lrep_selfrighteous),
                          (eq, ":target_reputation", lrep_roguish),
                          (str_store_string, s17, "str_s18_squanders_money_and_carouses_in_a_way_most_unbefitting_a_noble_by_doing_so_he_disgraces_us_all"),
                          (assign, ":chance_of_rivalry", 100),
                          
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_roguish),
                          (this_or_next|eq, ":target_reputation", lrep_upstanding),
                          (this_or_next|eq, ":target_reputation", lrep_martial),
                          (eq, ":target_reputation", lrep_selfrighteous),
                          (str_store_string, s17, "str_s18_has_been_speaking_ill_of_me_behind_my_back_or_so_they_say"),
                          (assign, ":chance_of_rivalry", 100),
                          
                          
                        (else_try),
                          (this_or_next|eq, ":source_reputation", lrep_quarrelsome),
                          (this_or_next|eq, ":source_reputation", lrep_martial),
                          (eq, ":source_reputation", lrep_selfrighteous),
                          (eq, ":target_reputation", lrep_custodian),
                          (str_store_string, s17, "str_s18_is_a_disgrace_reg3shehe_consorts_with_merchants_lends_money_at_interest_uses_coarse_language_and_shows_no_attempt_to_uphold_the_dignity_of_the_honor_bestowed_upon_reg3herhim"),
                          (assign, ":chance_of_rivalry", 100),
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_custodian),
                          (this_or_next|eq, ":target_reputation", lrep_quarrelsome),
                          (this_or_next|eq, ":target_reputation", lrep_martial),
                          (eq, ":target_reputation", lrep_selfrighteous),
                          (str_store_string, s17, "str_s18_has_condemned_me_for_engaging_in_commerce_what_could_possibly_be_wrong_with_that"),
                          (assign, ":chance_of_rivalry", 100),
                          
                          
                        (else_try),
                          (this_or_next|eq, ":source_reputation", lrep_debauched),
                          (this_or_next|eq, ":source_reputation", lrep_martial),
                          (eq, ":source_reputation", lrep_selfrighteous),
                          (eq, ":target_reputation", lrep_benefactor),
                          (str_store_string, s17, "str_s18_i_have_heard_has_been_encouraging_seditious_ideas_among_the_peasantry__a_foolish_move_which_endangers_us_all"),
                          (assign, ":chance_of_rivalry", 100),
                          
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_benefactor),
                          (this_or_next|eq, ":target_reputation", lrep_debauched),
                          (this_or_next|eq, ":target_reputation", lrep_martial),
                          (eq, ":target_reputation", lrep_selfrighteous),
                          (str_store_string, s17, "str_s18_has_called_me_out_for_the_way_i_deal_with_my_tenants_well_so_be_it_if_i_teach_them_that_they_are_the_equal_of_anyone_with_socalled_gentle_blood_what_is_it_to_reg3herhim"),
                          (assign, ":chance_of_rivalry", 100),
                          
                          
                          #lady incompatibilities
                        (else_try),
                          (eq, ":source_reputation", lrep_conventional),
                          (this_or_next|eq, ":target_reputation", lrep_martial),
                          (eq, ":target_reputation", lrep_selfrighteous),
                          (str_store_string, s17, "str_a_most_gallant_gentleman_who_knows_how_to_treat_a_lady"),
                          (assign, ":chance_of_rivalry", -50),
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_conventional),
                          (eq, ":target_reputation", lrep_quarrelsome),
                          (str_store_string, s17, "str_a_base_cad"),
                          (assign, ":chance_of_rivalry", 50),
                          
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_adventurous),
                          (eq, ":target_reputation", lrep_cunning),
                          (str_store_string, s17, "str_a_man_who_treats_me_as_his_equal_which_is_rare"),
                          (assign, ":chance_of_rivalry", -50),
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_adventurous),
                          (this_or_next|eq, ":target_reputation", lrep_martial),
                          (eq, ":target_reputation", lrep_debauched),
                          (str_store_string, s17, "str_appears_to_value_me_with_his_estate_and_his_horse_as_prizes_worth_having"),
                          (assign, ":chance_of_rivalry", 50),
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_adventurous),
                          (neq, ":target_reputation", lrep_goodnatured),
                          
                          (str_store_string, s17, "str_a_bit_dull_but_what_can_you_expect"),
                          (assign, ":chance_of_rivalry", 10),
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_otherworldly),
                          (call_script, "script_troop_get_romantic_chemistry_with_troop", ":source_lord", ":target_lord"),
                          (ge, reg0, 10),
                          (str_store_string, s17, "str_the_man_whom_destiny_intends_for_me"),
                          (assign, ":chance_of_rivalry", -50),
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_otherworldly),
                          (lt, reg0, 0),
                          
                          (str_store_string, s17, "str_is_not_right_for_me__i_cannot_say_why_but_he_makes_my_skin_crawl"),
                          (assign, ":chance_of_rivalry", 50),
                          
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_ambitious),
                          (this_or_next|eq, ":target_reputation", lrep_selfrighteous),
                          (eq, ":target_reputation", lrep_cunning),
                          (str_store_string, s17, "str_is_a_man_who_clearly_intends_to_make_his_mark_in_the_world"),
                          (assign, ":chance_of_rivalry", -20),
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_ambitious),
                          (eq, ":target_reputation", lrep_goodnatured),
                          
                          (str_store_string, s17, "str_is_a_layabout_a_naif_prey_for_others_who_are_cleverer_than_he"),
                          (assign, ":chance_of_rivalry", 30),
                          
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_moralist),
                          (eq, ":target_reputation", lrep_upstanding),
                          
                          (str_store_string, s17, "str_is_a_man_of_stalwart_character"),
                          (assign, ":chance_of_rivalry", -50),
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_moralist),
                          (this_or_next|eq, ":target_reputation", lrep_debauched),
                          (eq, ":target_reputation", lrep_cunning),
                          
                          (str_store_string, s17, "str_appears_to_be_a_man_of_low_morals"),
                          (assign, ":chance_of_rivalry", 50),
                          
                        (else_try),
                          (eq, ":source_reputation", lrep_moralist),
                          (eq, ":target_reputation", lrep_quarrelsome),
                          
                          (str_store_string, s17, "str_appears_to_be_a_man_who_lacks_selfdiscipline"),
                          (assign, ":chance_of_rivalry", 50),
					##diplomacy start+ Support for promoted ladies:
					   (else_try),
						   #Ambitious vs otherworldly
						   (eq, ":source_reputation", lrep_ambitious),
						   (troop_slot_eq, ":source_lord", slot_troop_occupation, slto_kingdom_hero),       
						   (eq, ":target_reputation", lrep_otherworldly),
						   (troop_slot_eq, ":target_lord", slot_troop_occupation, slto_kingdom_hero),
						   (str_store_string, s17, "str_s18_is_soft_and_weak_and_not_fit_to_govern_a_fief_and_i_have_always_detested_him"),
						   (str_store_string, s17, "str_s18_has_always_treated_me_contemptuously_although_i_have_done_him_no_wrong"),
							(assign, ":chance_of_rivalry", 100),
					   (else_try),
						   #Otherworldly vs ambitious
						   (eq, ":source_reputation", lrep_otherworldly),
						   (troop_slot_eq, ":source_lord", slot_troop_occupation, slto_kingdom_hero),       
						   (eq, ":target_reputation", lrep_ambitious),
						   (troop_slot_eq, ":target_lord", slot_troop_occupation, slto_kingdom_hero),
						   (str_store_string, s17, "str_s18_has_always_treated_me_contemptuously_although_i_have_done_him_no_wrong"),
							(assign, ":chance_of_rivalry", 100),
					   (else_try),
						   #Quarrelsome quarrels with conventional and moralist
						   (eq, ":source_reputation", lrep_quarrelsome),
						   (troop_slot_eq, ":target_lord", slot_troop_occupation, slto_kingdom_hero),
						   (this_or_next|eq, ":target_reputation", lrep_moralist),
							  (eq, ":target_reputation", lrep_conventional),
						   (str_store_string, s17, "str_s18_once_took_something_i_said_amiss_stubborn_bastard_wont_give_it_up_and_keeps_trying_to_get_me_to_recant_my_words"),
							(assign, ":chance_of_rivalry", 50),
					   (else_try),
							#Cunning conflicts with moralist
							(eq, ":source_reputation", lrep_cunning),
							(eq, ":target_reputation", lrep_moralist),
							(troop_slot_eq, ":target_lord", slot_troop_occupation, slto_kingdom_hero),
							(str_store_string, s17, "str_s18_i_am_sorry_to_say_is_far_too_softhearted_a_man_to_be_given_any_kind_of_responsibility_his_chivalry_will_allow_the_enemy_to_flee_to_fight_another_day_and_will_cost_the_lives_of_my_own_faithful_men"),
							(assign, ":chance_of_rivalry", 50),
						(else_try),
							#Debauched conflicts with moralist
							(eq, ":source_reputation", lrep_debauched),
							(troop_slot_eq, ":target_lord", slot_troop_occupation, slto_kingdom_hero),
							(eq, ":target_reputation", lrep_moralist),
							(str_store_string, s17, "str_s18_i_despite_him_he_puts_on_such_a_nauseating_display_of_virtue_and_thinks_nothing_of_insulting_his_betters"),
							(assign, ":chance_of_rivalry", 50),
						(else_try),
							#Martial or debauched conflicts with adventurous
						   (this_or_next|eq, ":source_reputation", lrep_martial),
						   (eq, ":source_reputation", lrep_debauched),
						  (troop_slot_eq, ":target_lord", slot_troop_occupation, slto_kingdom_hero),
						  (eq, ":target_reputation", lrep_adventurous),
						  (str_store_string, s17, "str_s18_once_took_something_i_said_amiss_stubborn_bastard_wont_give_it_up_and_keeps_trying_to_get_me_to_recant_my_words"),
							(assign, ":chance_of_rivalry", 50),
						(else_try),
							(eq, ":source_reputation", lrep_goodnatured),
							(troop_slot_eq, ":target_lord", slot_troop_occupation, slto_kingdom_hero),
							(eq, ":target_reputation", lrep_ambitious),
							(str_store_string, s17, "str_s18_seems_to_have_something_against_me_for_some_reason_i_dont_like_to_talk_ill_of_people_but_i_think_hes_can_be_a_bit_of_a_cad_sometimes"),
							  (assign, ":chance_of_rivalry", 30),
					##Add support for secondary morality types
						(else_try),
							(call_script, "script_dplmc_get_troop_morality_value", ":target_lord", tmt_honest),
							(ge, reg0, 1),#This would apply (if no previous condition was reached) to Marnid, Rolf, Firentis, Alayan, and Jeremus.
							(eq, ":source_reputation", lrep_moralist),
							(str_store_string, s17, "str_is_a_man_of_stalwart_character"),#<- (does not apply to Rolf, since he is Cunning)
							(assign, ":chance_of_rivalry", -50),
						(else_try),
							(call_script, "script_dplmc_get_troop_morality_value", ":target_lord", tmt_pious),
							(ge, reg0, 1),#This doesn't apply to anyone at the moment.
							(eq, ":source_reputation", lrep_moralist),
							(str_store_string, s17, "str_is_a_man_of_stalwart_character"),
							(assign, ":chance_of_rivalry", -50),
						(try_end),
							
					##diplomacy end+

						(val_div, ":chance_of_rivalry", ":divisor"),
					##diplomacy start+ for companions, use compatability information
						(try_begin),
						   (is_between, ":source_lord", companions_begin, companions_end),
						   (troop_slot_eq, ":source_lord", slot_troop_personalitymatch_object, ":target_lord"),
						   (val_min, ":chance_of_rivalry", -100),
						(else_try),
						   (is_between, ":source_lord", companions_begin, companions_end),
						   (this_or_next|troop_slot_eq, ":source_lord", slot_troop_personalityclash_object, ":target_lord"),
						   (troop_slot_eq, ":source_lord", slot_troop_personalityclash2_object, ":target_lord"),
						   (try_begin),
							  (le, ":chance_of_rivalry", 0),
							  (str_store_string, s17, "str_general_quarrel"),
						   (try_end),
						   (val_max, ":chance_of_rivalry", 100),
						(try_end),
						(assign, reg3, ":save_reg3"),#revert reg3
						(assign, reg65, ":save_reg65"),#revert reg65
					##diplomacy end+
						(assign, reg0, ":chance_of_rivalry"),

						(neq, ":chance_of_rivalry", 0),
					#	(eq, ":incompatibility_found", 1), #cf can be removed with this

						]),
                    
					  ("troop_get_romantic_chemistry_with_troop", #source is lady, target is man
						[
						  ##diplomacy start+ (players of either gender may marry opposite-gender lords)
						  #Note: the above is misleading even in Native, since when target_lord is the player,
						  #target_lord can be female and source_lady can be male.
						  (assign, ":save_reg1", reg1),
						  ##diplomacy end+
						  (store_script_param, ":source_lady", 1),
						  (store_script_param, ":target_lord", 2),

						  (store_add, ":chemistry_sum", ":source_lady", ":target_lord"),
						  (val_add, ":chemistry_sum", "$romantic_attraction_seed"),

						  #This calculates (modula ^ 2) * 3
						  (store_mod, ":chemistry_remainder", ":chemistry_sum", 5),
						  (val_mul, ":chemistry_remainder", ":chemistry_remainder"), #0, 1, 4, 9, 16
						  (val_mul, ":chemistry_remainder", 3), #0, 3, 12, 27, 48

						  (store_attribute_level, ":romantic_chemistry", ":target_lord", ca_charisma),
						  (val_sub, ":romantic_chemistry", ":chemistry_remainder"),

						  (val_mul, ":romantic_chemistry", 2),
						  ##diplomacy start+ ensure companion compatability
						  (try_begin),
							 (is_between, ":source_lady", companions_begin, companions_end),
							 (troop_slot_eq, ":source_lady", slot_troop_personalitymatch_object, ":target_lord"),
							 (val_max, ":romantic_chemistry", 15),
						  (else_try),
							 (is_between, ":target_lord", companions_begin, companions_end),
							 (troop_slot_eq, ":target_lord", slot_troop_personalitymatch_object, ":source_lady"),
							 (val_max, ":romantic_chemistry", 15),
						  #...and companion incompatibility.
						  (else_try),
							 (is_between, ":source_lady", companions_begin, companions_end),
							 (this_or_next|troop_slot_eq, ":source_lady", slot_troop_personalityclash_object, ":target_lord"),
								(troop_slot_eq, ":source_lady", slot_troop_personalityclash2_object, ":target_lord"),
							 (val_min, ":romantic_chemistry", -15),
						  (else_try),
							 (is_between, ":target_lord", companions_begin, companions_end),
							 (this_or_next|troop_slot_eq, ":target_lord", slot_troop_personalityclash_object, ":source_lady"),
								(troop_slot_eq, ":target_lord", slot_troop_personalityclash2_object, ":source_lady"),
							(val_min, ":romantic_chemistry", -15),
						  #Prevent glitches.  This can be enabled explicitly if intentional.
						  (else_try),
							 (call_script, "script_dplmc_store_is_female_troop_1_troop_2", ":source_lady", ":target_lord"),
							 (eq, reg0, reg1),#different genders
							 (val_min, ":romantic_chemistry", -15),
						  (try_end),
						  (assign, reg1, ":save_reg1"),
						  ##diplomacy end+
						  (assign, reg0, ":romantic_chemistry"),

						  #examples :
						  #For a charisma of 18, yields (18 - 0) * 2 = 36, (18 - 3) * 2 = 30, (18 - 12) * 2 = 12, (18 - 27) * 2 = -18, (18 - 48) * 2 = -60
						  #For a charisma of 10, yields (10 - 0) * 2 = 20, (10 - 3) * 2 = 14, (10 - 12) * 2 = -4, (10 - 27) * 2 = -34, (10 - 48) * 2 = -76
						  #For a charisma of 7, yields  (7 - 0) * 2 = 14,  (7 - 3) * 2 = 8,   (7 - 12) * 2 = -10, (7 - 27) * 2 = -40,  (7 - 48) * 2 = -82

						  #15 is high attraction, 0 is moderate attraction, -76 is lowest attraction
						]),
                    
                    
					  ("cf_troop_get_romantic_attraction_to_troop", #source is lady, target is man
						[

						(store_script_param, ":source_lady", 1),
						(store_script_param, ":target_lord", 2),

						(assign, ":weighted_romantic_assessment", 0),
						##diplomacy start+
						(assign, ":save_reg1", reg1),
						#Use gender script
						#(troop_get_type, ":source_is_female", ":source_lady"),
						#(eq, ":source_is_female", 1),
						#(troop_get_type, ":target_is_female", ":target_lord"),
						#(eq, ":target_is_female", 0),
						(call_script, "script_dplmc_store_is_female_troop_1_troop_2", ":source_lady", ":target_lord"),
						(assign, ":source_is_female", reg0),
						(assign, ":target_is_female", reg1),
						(assign, reg1, ":save_reg1"),
					   (assign, reg0, -15),
						(neq, ":source_is_female", ":target_is_female"),
						##diplomacy end+

						(call_script, "script_troop_get_romantic_chemistry_with_troop", ":source_lady", ":target_lord"),
						(assign, ":romantic_chemistry", reg0),


						#objective attraction - average renown
						(troop_get_slot, ":modified_renown", ":target_lord", slot_troop_renown),
						(assign, ":lady_status", 60),
					   ##diplomacy start+ adjust status based on who they are
						(try_begin),
						  #The renown bonus is decreased the more important the lady's relatives are.
						  (ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_HIGH),
						  (troop_get_slot, ":best_renown", ":source_lady", slot_troop_renown),
						  (try_begin),
							(troop_get_slot, ":relative", ":source_lady", slot_troop_father),
							(ge, ":relative", 0),
							(troop_get_slot, ":other_renown", ":relative", slot_troop_renown),
							(val_max, ":best_renown", ":other_renown"),
						(try_end),
						(try_begin),
							  (troop_get_slot, ":relative", ":source_lady", slot_troop_guardian),
							(ge, ":relative", 0),
							(troop_get_slot, ":other_renown", ":relative", slot_troop_renown),
							(val_max, ":best_renown", ":other_renown"),
						(try_end),
						(try_begin),
							  (troop_get_slot, ":relative", ":source_lady", slot_troop_mother),
							(ge, ":relative", 0),
							(troop_get_slot, ":other_renown", ":relative", slot_troop_renown),
							(val_max, ":best_renown", ":other_renown"),
						(try_end),
						(try_begin),
							  (ge, ":best_renown", 600),
							(store_div, ":lady_status", ":best_renown", 10),
						(else_try),
							  (lt, ":best_renown", 400),
							(store_div, ":lady_status", ":best_renown", 10),
							  (val_add, ":lady_status", 20),
						(try_end),
						(val_clamp, ":lady_status", 30, 90),
					   (try_end),
					   ##diplomacy end+
						(val_div, ":modified_renown", 5),
						(val_sub, ":modified_renown", ":lady_status"),
						(val_min, ":modified_renown", 60),



						#weight values
						(try_begin),
							(assign, ":personality_match", 0),
							(call_script, "script_cf_test_lord_incompatibility_to_s17", ":source_lady", ":target_lord"),
							(store_sub, ":personality_match", 0, reg0),
						(try_end),

						(troop_get_slot, ":lady_reputation", ":source_lady", slot_lord_reputation_type),
						(try_begin),
							(eq, ":lady_reputation", lrep_ambitious),
							(val_mul, ":modified_renown", 2),
							(val_div, ":romantic_chemistry", 2),
						(else_try),
							(eq, ":lady_reputation", lrep_otherworldly),
							(val_div, ":modified_renown", 2),
							(val_mul, ":romantic_chemistry", 2),
						(else_try),
							(eq, ":lady_reputation", lrep_adventurous),
							(val_div, ":modified_renown", 2),
						(else_try),
							(eq, ":lady_reputation", lrep_moralist),
							(val_div, ":modified_renown", 2),
							(val_div, ":romantic_chemistry", 2),
						(try_end),

						(val_add, ":weighted_romantic_assessment", ":romantic_chemistry"),
						(val_add, ":weighted_romantic_assessment", ":personality_match"),
						(val_add, ":weighted_romantic_assessment", ":modified_renown"),

						(assign, reg0, ":weighted_romantic_assessment"),

						]),
                    
                    
                    ("cf_random_political_event", #right now, just enmities
                      [
                        
                        (store_random_in_range, ":lord_1", active_npcs_begin, active_npcs_end),
                        (store_random_in_range, ":lord_2", active_npcs_begin, active_npcs_end),
                        
                        (troop_slot_eq, ":lord_1", slot_troop_occupation, slto_kingdom_hero),
                        (troop_slot_eq, ":lord_2", slot_troop_occupation, slto_kingdom_hero),
                        
                        (neq, ":lord_1", ":lord_2"),
                        
                        (val_add, "$total_political_events", 1),
                        
                        (store_troop_faction, ":lord_1_faction", ":lord_1"),
                        (store_troop_faction, ":lord_2_faction", ":lord_2"),
                        
                        (assign, reg8, "$total_political_events"),
                        
                        
                        (faction_get_slot, ":faction_1_leader", ":lord_1_faction", slot_faction_leader),
                        (faction_get_slot, ":faction_2_leader", ":lord_2_faction", slot_faction_leader),
                        
                        (this_or_next|eq, ":lord_1_faction", ":lord_2_faction"),
                        (this_or_next|eq, ":lord_1", ":faction_1_leader"),
                        (eq, ":lord_2", ":faction_2_leader"),
                        
                        
                        (call_script, "script_troop_get_relation_with_troop", ":lord_1", ":lord_2"),
                        (assign, ":relation", reg0),
                        
                        
                        (store_random_in_range, ":random", 0, 100),
                        
                        (try_begin),
                          #reconciliation
                          #The chance of a liege reconciling two quarreling vassals is equal to (relationship with lord 1 x relationship with lord 2) / 4
                          
                          (eq, ":lord_1_faction", ":lord_2_faction"),
                          (neq, ":faction_1_leader", "trp_player"),
                          
                          (le, ":relation", -10),
                          
                          #		(ge, "$total_political_events", 5000),
                          
                          (call_script, "script_troop_get_relation_with_troop", ":lord_1", ":faction_1_leader"),
                          (gt, reg0, 0),
                          (assign, ":lord_1_leader_rel", reg0),
                          
                          (call_script, "script_troop_get_relation_with_troop", ":lord_2", ":faction_1_leader"),
                          (gt, reg0, 0),
                          (store_mul, ":reconciliation_chance", ":lord_1_leader_rel", reg0),
                          (val_div, ":reconciliation_chance", 4),	#was 2 before
                          
                          (le, ":random", ":reconciliation_chance"),
                          
                          (str_store_troop_name, s4, ":faction_1_leader"),
                          (str_store_troop_name, s5, ":lord_1"),
                          (str_store_troop_name, s6, ":lord_2"),
                          (try_begin),
                            (eq, "$cheat_mode", 1),
                            (display_message, "str_check_reg8_s4_reconciles_s5_and_s6_"),
                          (try_end),
                          
                          (call_script, "script_troop_change_relation_with_troop", ":lord_1", ":lord_2", 20),
                          (val_add, "$total_random_quarrel_changes", 20),
                        (else_try),	#lord intervenes in quarrel
                          (eq, ":lord_1_faction", ":lord_2_faction"),
                          
                          (le, ":relation", -10),
                          #		(ge, ":random", 50),
                          (try_begin),
                            (eq, ":faction_1_leader", "trp_player"),
                            (try_begin),
                              (eq, "$cheat_mode", 1),
                              (display_message, "str_diagnostic__player_should_receive_consultation_quest_here_if_not_already_active"),
                            (try_end),
                            (neg|check_quest_active, "qst_consult_with_minister"),
                            (neg|check_quest_active, "qst_resolve_dispute"),
                            (eq, "$g_minister_notification_quest", 0),
                            (assign, "$g_minister_notification_quest", "qst_resolve_dispute"),
                            (quest_set_slot, "qst_resolve_dispute", slot_quest_target_troop, ":lord_1"),
                            (quest_set_slot, "qst_resolve_dispute", slot_quest_object_troop, ":lord_2"),
                            
                            (call_script, "script_add_notification_menu", "mnu_notification_player_should_consult", 0, 0),
                            
                            
                          (else_try),
                            (call_script, "script_troop_get_relation_with_troop", ":lord_1", ":faction_1_leader"),
                            (assign, ":lord_1_rel_w_leader", reg0),
                            
                            (call_script, "script_troop_get_relation_with_troop", ":lord_2", ":faction_1_leader"),
                            (assign, ":lord_2_rel_w_leader", reg0),
                            
                            (store_random_in_range, ":another_random", -5, 5),
                            
                            (val_add, ":lord_1_rel_w_leader", ":another_random"),
                            
                            (try_begin),
                              (ge, ":lord_1_rel_w_leader", ":lord_2_rel_w_leader"),
                              (assign, ":winner_lord", ":lord_1"),
                              (assign, ":loser_lord", ":lord_2"),
                            (else_try),
                              (assign, ":loser_lord", ":lord_1"),
                              (assign, ":winner_lord", ":lord_2"),
                            (try_end),
                            
                            (str_store_troop_name, s4, ":faction_1_leader"),
                            (str_store_troop_name, s5, ":winner_lord"),
                            (str_store_troop_name, s6, ":loser_lord"),
                            
                            (try_begin),
                              (eq, "$cheat_mode", 1),
                              (display_message, "str_check_reg8_s4_rules_in_s5s_favor_in_quarrel_with_s6_"),
                            (try_end),
                            
                            (call_script, "script_add_log_entry", logent_ruler_intervenes_in_quarrel, ":faction_1_leader",  ":loser_lord", ":winner_lord", ":lord_1_faction"), #faction leader is actor, loser lord is center object, winner lord is troop_object
                            
                            (call_script, "script_troop_change_relation_with_troop", ":winner_lord", ":faction_1_leader", 10),
                            (call_script, "script_troop_change_relation_with_troop", ":loser_lord", ":faction_1_leader", -20),
                            (val_add, "$total_random_quarrel_changes", -10),
                            
                          (try_end),
                          
                          
                        (else_try), #new quarrel - companions
                          (is_between, ":lord_1", companions_begin, companions_end),
                          (is_between, ":lord_2", companions_begin, companions_end),
                          
                          (ge, ":relation", -10),
                          (this_or_next|troop_slot_eq, ":lord_1", slot_troop_personalityclash_object, ":lord_2"),
                          (troop_slot_eq, ":lord_1", slot_troop_personalityclash2_object, ":lord_2"),
                          
                          (str_store_troop_name, s5, ":lord_1"),
                          (str_store_troop_name, s6, ":lord_2"),
                          
                          (try_begin),
                            (eq, "$cheat_mode", 1),
                            (display_message, "str_check_reg8_new_rivalry_generated_between_s5_and_s6"),
                          (try_end),
                          
                          (call_script, "script_troop_change_relation_with_troop", ":lord_1", ":lord_2", -30),
                          (val_add, "$total_random_quarrel_changes", -30),
                          
                          
                        (else_try), #new quarrel - others
                          (eq, ":lord_1_faction", ":lord_2_faction"),
                          
                          (ge, ":relation", -10), #can have two quarrels
                          
                          (call_script, "script_cf_test_lord_incompatibility_to_s17", ":lord_1", ":lord_2"),
                          (assign, ":chance_of_enmity", reg0),
                          (gt, ":chance_of_enmity", 0),
                          
                          (lt, ":random", ":chance_of_enmity"), #50 or 100 percent, usually ##1.134
                          
                          
                          (str_store_troop_name, s5, ":lord_1"),
                          (str_store_troop_name, s6, ":lord_2"),
                          (try_begin),
                            (eq, "$cheat_mode", 1),
                            (display_message, "str_check_reg8_new_rivalry_generated_between_s5_and_s6"),
                          (try_end),
                          
                          (call_script, "script_troop_change_relation_with_troop", ":lord_1", ":lord_2", -30),
                          (val_add, "$total_random_quarrel_changes", -30),
                          
                          #		(call_script, "script_update_troop_notes", ":lord_1"),
                          #		(call_script, "script_update_troop_notes", ":lord_2"),
                        (else_try), #a lord attempts to suborn a character
                          (store_current_hours, ":hours"),
                          (ge, ":hours", 24),
                          
                          (neq, ":lord_1_faction", ":lord_2_faction"),
                          #		(eq, ":lord_1", ":faction_1_leader"),
                          (is_between, ":lord_1_faction", kingdoms_begin, kingdoms_end),
                          
                          (call_script, "script_cf_troop_can_intrigue", ":lord_2", 0),
                          (neq, ":lord_2", ":faction_2_leader"), ##1.134
                          (neq, ":lord_2", ":faction_1_leader"), ##1.134
                          
                          (str_store_troop_name, s5, ":faction_1_leader"),
                          (str_store_troop_name, s6, ":lord_2"),
                          
                          (try_begin),
                            (ge, "$cheat_mode", 1), ##1.134
                            (display_message, "str_check_reg8_s5_attempts_to_win_over_s6"),
                          (try_end),
                          
                          (call_script, "script_calculate_troop_political_factors_for_liege", ":lord_2", ":faction_1_leader"),
                          (assign, ":lord_1_score", reg0),
                          
                          (call_script, "script_calculate_troop_political_factors_for_liege", ":lord_2", ":faction_2_leader"),
                          (assign, ":faction_2_leader_score", reg0),
                          
                          (try_begin),
                            (gt, ":lord_1_score", ":faction_2_leader_score"),
                            ## Begin 1.134
                            (try_begin),
                              (ge, "$cheat_mode", 1),
                              (str_store_troop_name, s4, ":lord_2"),
                              (display_message, "@{!}DEBUG - {s4} faction changed in subornment"),
                            (try_end),
                            ## End 1.134
                            (call_script, "script_change_troop_faction", ":lord_2", ":lord_1_faction"),
                          (try_end),
                        (try_end),
                        
                        
                        
                    ]),
                    
                    
                    #this calculates the average number of rivalries per lord, giving a rough indication of how easily a faction may be divided
                    #fairly expensive in terms of CPU
                    ("evaluate_realm_stability",
                      
                      [
                        (store_script_param, ":realm", 1),
                        
                        (assign, ":total_lords", 0),
                        (assign, ":total_restless_lords", 0),
                        (assign, ":total_disgruntled_lords", 0),
                        
                        (faction_get_slot, ":liege", ":realm", slot_faction_leader),
                        
                        (try_for_range, ":lord", active_npcs_begin, active_npcs_end),
                          (troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
                          (store_troop_faction, ":lord_faction", ":lord"),
                          (eq, ":lord_faction", ":realm"),
                          (val_add, ":total_lords", 1),
                          
                          (call_script, "script_calculate_troop_political_factors_for_liege", ":lord", ":liege"),
                          (try_begin),
                            (le, reg3, -10),
                            (val_add, ":total_disgruntled_lords", 1),
                          (else_try),
                            (le, reg3, 10),
                            (val_add, ":total_restless_lords", 1),
                          (try_end),
                        (try_end),
                        
                        (try_begin),
                          (gt, ":total_lords", 0),
                          (store_mul, ":instability_quotient", ":total_disgruntled_lords", 100),
                          (val_div, ":instability_quotient", ":total_lords"),
                          
                          (store_mul, ":restless_quotient", ":total_restless_lords", 100),
                          (val_div, ":restless_quotient", ":total_lords"),
                          
                          (store_mul, ":combined_quotient", ":instability_quotient", 2),
                          (val_add, ":combined_quotient", ":restless_quotient"),
                          (faction_set_slot, ":realm", slot_faction_instability, ":combined_quotient"),
                          
                          (assign, reg0, ":instability_quotient"),
                          (assign, reg1, ":restless_quotient"),
                          (assign, reg1, ":restless_quotient"),
                        (else_try),
                          (try_begin),
                            (eq, "$cheat_mode", 1),
                            (str_store_faction_name, s1, ":realm"),
                            (display_message, "str_s1_has_no_lords"),
                          (try_end),
                          (assign, reg0, 0),
                          (assign, reg1, 0),
                        (try_end),
                        
                    ]),
                    
                    
                    
                    #lord recruitment scripts end
                    
                    #called from game_event_simulate_battle
                    #Includes a number of consequences that follow on battles, mostly affecting relations between different NPCs
                    #This only fires from complete victories
                    ("battle_political_consequences",
                      [
                        (store_script_param, ":defeated_party", 1),
                        (store_script_param, ":winner_party", 2),
                        
                        (try_begin),
                          (eq, "$cheat_mode", 1),
                          (str_store_party_name, s4, ":winner_party"),
                          (str_store_party_name, s5, ":defeated_party"),
                          (display_message, "str_do_political_consequences_for_s4_victory_over_s5"),
                        (try_end),
                        
                        (store_faction_of_party, ":winner_faction", ":winner_party"),
                        (try_begin),
                          (eq, ":winner_party", "p_main_party"),
                          (assign, ":winner_faction", "$players_kingdom"),
                        (try_end),
                        
                        (party_get_template_id, ":defeated_party_template", ":defeated_party"),
                        
                        #did the battle involve travellers?
                        (try_begin),
						##Floris MTT begin
                          (this_or_next|eq, ":defeated_party_template", "pt_village_farmers"),
                          (this_or_next|eq, ":defeated_party_template", "pt_kingdom_caravan_party"),
                          (this_or_next|eq, ":defeated_party_template", "pt_village_farmers_r"),
                          (this_or_next|eq, ":defeated_party_template", "pt_kingdom_caravan_party_r"),
                          (this_or_next|eq, ":defeated_party_template", "pt_village_farmers_e"),
                          (eq, ":defeated_party_template", "pt_kingdom_caravan_party_e"),
						##Floris MTT end                          
                          
                          (party_get_slot, ":destination", ":defeated_party", slot_party_ai_object),
                          (party_get_slot, ":origin", ":defeated_party", slot_party_last_traded_center),
                          
                          (call_script, "script_add_log_entry", logent_traveller_attacked, ":winner_party",  ":origin", ":destination", ":winner_faction"),
                          
                          (try_begin),
                            (eq, "$cheat_mode", 2),
                            (neg|is_between, ":winner_faction", kingdoms_begin, kingdoms_end),
                            (str_store_string, s65, "str_bandits_attacked_a_party_on_the_roads_so_a_bounty_is_probably_available"),
                            (call_script, "script_add_notification_menu", "mnu_debug_alert_from_s65", 0, 0),
                            
                            (str_store_party_name, s15, ":origin"),
                            (str_store_party_name, s16, ":destination"),
                            (display_message, "str_travellers_attacked_on_road_from_s15_to_s16"),
                          (try_end),
                          
                          
                          #by logging the faction and the party, we can verify that the party number is unlikely to have been reassigned - or at any rate, that the factions have not changed
                        (try_end),
                        
                        #winner consequences:
                        #1)   leader improves relations with other leaders
                        #2)  Player given credit for victory if the victorious party is following the player's advice
                        (try_begin),
                          (party_get_template_id, ":winner_party_template", ":winner_party"),
                          (eq, ":winner_party_template", "pt_kingdom_hero_party"),
                          (neq, ":winner_party", "p_main_party"),
                          #Do not do for player party, as is included in post-battle dialogs
                          
                          (party_stack_get_troop_id, ":winner_leader", ":winner_party", 0),
                          (is_between, ":winner_leader", active_npcs_begin, active_npcs_end),
                          
                          (store_faction_of_party, ":winner_faction", ":winner_party"),
                          
                          (party_collect_attachments_to_party, ":winner_party", "p_temp_party_2"),
                          (party_get_num_companion_stacks, ":num_stacks", "p_temp_party_2"),
                          (try_for_range, ":troop_iterator", 0, ":num_stacks"),
                            (party_stack_get_troop_id, ":cur_troop_id", "p_temp_party_2", ":troop_iterator"),
                            (is_between, ":cur_troop_id", active_npcs_begin, active_npcs_end),
                            
                            (try_begin),
                              (troop_get_slot, ":winner_lord_party", ":cur_troop_id", slot_troop_leaded_party),
                              (party_is_active, ":winner_lord_party"),
                              (call_script, "script_cf_party_under_player_suggestion", ":winner_lord_party"),
                              (call_script, "script_add_log_entry", logent_player_suggestion_succeeded, "trp_player", -1, ":cur_troop_id", -1),
                            (try_end),
                            
                            
                            (store_faction_of_troop, ":troop_faction", ":cur_troop_id"),
                            (eq, ":troop_faction", ":winner_faction"),
                            (neq, ":cur_troop_id", ":winner_leader"),
                            
                            (try_begin),
                              (eq, "$cheat_mode", 4),
                              (str_store_troop_name, s15, ":cur_troop_id"),
                              (str_store_troop_name, s16, ":winner_leader"),
                              (display_message, "str_s15_shares_joy_of_victory_with_s16"),
                            (try_end),
                            
                            (call_script, "script_troop_change_relation_with_troop", ":cur_troop_id", ":winner_leader", 3),
                            (val_add, "$total_battle_ally_changes", 3),
                            
                          (try_end),
                          (party_clear, "p_temp_party_2"),
                        (try_end),
                        
                        #consequences of defeat,
                        #1) -1 relation with lord per lord, plus -15 if there is an incompatible marshal
                        #2)  losers under player suggestion blame the player
                        #3) Some losers resent the victor lord
                        #4) Possible quarrels over defeat
                        (try_begin),
                          (party_collect_attachments_to_party, ":defeated_party", "p_temp_party_2"),
                          (party_get_num_companion_stacks, ":num_stacks", "p_temp_party_2"),
                          
                          (try_begin),
                            (gt, "$marshall_defeated_in_battle", 0),
                            (str_store_troop_name, s15, "$marshall_defeated_in_battle"),
                            (store_faction_of_troop, ":defeated_marshall_faction", "$marshall_defeated_in_battle"),
                            (try_begin),
                              (eq, "$cheat_mode", 1),
                              (display_message, "str_faction_marshall_s15_involved_in_defeat"),
                            (try_end),
                          (else_try),
                            (eq, "$marshall_defeated_in_battle", "trp_player"),
                            (eq, ":defeated_party", "p_main_party"),
                            (faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
                            (try_begin),
                              (eq, "$cheat_mode", 1),
                              (display_message, "str_player_faction_marshall_involved_in_defeat"),
                            (try_end),
                          (else_try),
                            (assign, "$marshall_defeated_in_battle", -1),
                          (try_end),
                          
                          (try_for_range, ":troop_iterator", 0, ":num_stacks"),
                            (party_stack_get_troop_id, ":cur_troop_id", "p_temp_party_2", ":troop_iterator"),
                            (troop_slot_eq, ":cur_troop_id", slot_troop_occupation, slto_kingdom_hero),
                            
                            (try_begin), #is party under suggestion?
                              (troop_get_slot, ":defeated_lord_party", ":cur_troop_id", slot_troop_leaded_party),
                              (party_is_active, ":defeated_lord_party"),
                              
                              #is party under suggestion?
                              (call_script, "script_cf_party_under_player_suggestion", ":defeated_lord_party"),
                              (call_script, "script_add_log_entry", logent_player_suggestion_failed, "trp_player", -1, ":cur_troop_id", -1),
                            (try_end),
                            
                            
                            (store_faction_of_troop, ":troop_faction", ":cur_troop_id"),
                            
                            (faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),
                            (neq, ":cur_troop_id", ":faction_leader"),
                            
                            #Lose one point relation with liege
                            (try_begin),
                              (eq, "$cheat_mode", 1),
                              (str_store_troop_name, s14, ":cur_troop_id"),
                              (str_store_faction_name, s15, ":troop_faction"),
                              
                              (display_message, "str_s14_of_s15_defeated_in_battle_loses_one_point_relation_with_liege"),
                            (try_end),
                            
                            (try_begin),
                              (this_or_next|neq, ":faction_leader", "trp_player"), #if leader is zero at beginning of game. I'm not entirely sure how this could happen...
                              (eq, "$players_kingdom", ":troop_faction"),
                              
                              (call_script, "script_troop_change_relation_with_troop", ":cur_troop_id", ":faction_leader", -1),
                              (val_add, "$total_battle_ally_changes", -1),
                            (try_end),
                            
                            
                            (call_script, "script_faction_inflict_war_damage_on_faction", ":winner_faction", ":troop_faction", 10),
                            
                            
                            (try_begin),
                              (this_or_next|is_between, ":winner_leader", active_npcs_begin, active_npcs_end),
                              (eq, ":winner_leader", "trp_player"),
                              
                              (this_or_next|neq, ":winner_leader", "trp_player"), #prevents winner leader being zero, for whatever reason
                              (eq, ":winner_party", "p_main_party"),
                              
                              (this_or_next|troop_slot_eq, ":cur_troop_id", slot_lord_reputation_type, lrep_quarrelsome),
                              (this_or_next|troop_slot_eq, ":cur_troop_id", slot_lord_reputation_type, lrep_selfrighteous),
                              (troop_slot_eq, ":cur_troop_id", slot_lord_reputation_type, lrep_debauched),
                              
                              (call_script, "script_troop_change_relation_with_troop", ":cur_troop_id", ":winner_leader", -1),
                              (val_add, "$total_battle_enemy_changes", -1),
                              
                              (try_begin),
                                (eq, "$cheat_mode", 1),
                                (str_store_troop_name, s14, ":cur_troop_id"),
                                (str_store_troop_name, s15, ":winner_leader"),
                                
                                (display_message, "str_s14_defeated_in_battle_by_s15_loses_one_point_relation"),
                              (try_end),
                              
                              
                            (try_end),
                            
                            (gt, "$marshall_defeated_in_battle", -1),
                            (eq, ":troop_faction", ":defeated_marshall_faction"),
                            (str_store_troop_name, s14, ":cur_troop_id"),
                            
                            (call_script, "script_cf_test_lord_incompatibility_to_s17", ":cur_troop_id", "$marshall_defeated_in_battle"),
                            (try_begin),
                              (eq, "$cheat_mode", 1),
                              (display_message, "str_s14_blames_s15_for_defeat"),
                            (try_end),
                            
                            (call_script, "script_add_log_entry", logent_lord_blames_defeat, ":cur_troop_id", "$marshall_defeated_in_battle", ":faction_leader", ":winner_faction"),
                            
                            (call_script, "script_troop_change_relation_with_troop", ":cur_troop_id", ":faction_leader", -15),
                            (val_add, "$total_battle_ally_changes", -15),
                            
                            (neq, "$marshall_defeated_in_battle", ":faction_leader"),
                            (call_script, "script_troop_change_relation_with_troop", ":cur_troop_id", "$marshall_defeated_in_battle", -15),
                            (val_add, "$total_battle_ally_changes", -15),
                            
                          (try_end),
                          
                          (party_clear, "p_temp_party_2"),
                        (try_end),
                    ]),
                    
                    ("faction_inflict_war_damage_on_faction",
                      [
                        (store_script_param, ":actor_faction", 1),
                        (store_script_param, ":target_faction", 2),
                        (store_script_param, ":amount", 3),
                        
                        
                        (store_add, ":slot_war_damage", ":target_faction", slot_faction_war_damage_inflicted_on_factions_begin),
                        (val_sub, ":slot_war_damage", kingdoms_begin),
                        (faction_get_slot, ":cur_war_damage", ":actor_faction", ":slot_war_damage"),
                        
                        (val_add, ":cur_war_damage", ":amount"),
                        (faction_set_slot, ":actor_faction", ":slot_war_damage", ":cur_war_damage"),
                        
                        
                        (try_begin),
                          (ge, "$cheat_mode", 1),
                          (str_store_faction_name, s4, ":actor_faction"),
                          (str_store_faction_name, s5, ":target_faction"),
                          (assign, reg3, ":cur_war_damage"),
                          (assign, reg4, ":amount"),
                          (display_message, "@{!}{s4} inflicts {reg4} damage on {s5}, raising total inflicted to {reg3}"),
                        (try_end),
                        
                        
                        (faction_get_slot, ":faction_marshal", ":target_faction", slot_faction_marshall),
                        (try_begin),
                          (ge, ":faction_marshal", 0),
                          (gt, ":amount", 0),
                          
                          (troop_get_slot, ":controversy", ":faction_marshal", slot_troop_controversy),
                          (val_add, ":controversy", ":amount"),
                          (val_min, ":controversy", 100),
                          (troop_set_slot, ":faction_marshal", slot_troop_controversy, ":controversy"),
                          
                          (try_begin),
                            (ge, "$cheat_mode", 1),
                            (str_store_troop_name, s4, ":faction_marshal"),
                            (assign, reg4, ":amount"),
                            (assign, reg5, ":controversy"),
                            (display_message, "@{!}War damage raises {s4}'s controversy by {reg4} to {reg5}"),
                          (try_end),
                        (try_end),
                        
                        (faction_get_slot, ":faction_marshal", ":actor_faction", slot_faction_marshall),
                        (try_begin),
                          (ge, ":faction_marshal", 0),
                          (val_div, ":amount", 3),
                          (gt, ":amount", 0),
                          
                          
                          (troop_get_slot, ":controversy", ":faction_marshal", slot_troop_controversy),
                          (val_sub, ":controversy", ":amount"),
                          (val_max, ":controversy", 0),
                          (troop_set_slot, ":faction_marshal", slot_troop_controversy, ":controversy"),
                          
                          (try_begin),
                            (ge, "$cheat_mode", 1),
                            (str_store_troop_name, s4, ":faction_marshal"),
                            (assign, reg4, ":amount"),
                            (assign, reg5, ":controversy"),
                            (display_message, "@{!}War damage lowers {s4}'s controversy by {reg4} to {reg5}"),
                          (try_end),
                        (try_end),
                        
                        
                        
                    ]),
                    
                    ("calculate_troop_political_factors_for_liege",
                      [
                        (store_script_param, ":troop", 1),
                        (store_script_param, ":liege", 2),
                        
                        (troop_get_slot, ":lord_reputation", ":troop", slot_lord_reputation_type),
                        
                        (store_faction_of_troop, ":faction", ":liege"),
                        
                        
                        (try_begin),
                          (eq, ":faction", "fac_player_faction"),
                          (assign, ":faction", "fac_player_supporters_faction"),
                        (try_end),
                        
                        (assign, ":liege_is_undeclared_rebel", 0),
                        (try_begin),
                          (neg|faction_slot_eq, ":faction", slot_faction_leader, ":liege"),
                          #the liege is a rebel
                          (assign, ":liege_is_undeclared_rebel", 1),
                          (try_begin),
                            (eq, "$cheat_mode", 1),
                            (str_store_troop_name, s32, ":liege"),
                            (display_message, "str_s32_is_undeclared_rebel"),
                          (try_end),
                        (try_end),
                        
                        (assign, ":result_for_material", 0),
                        (assign, ":penalty_for_changing_sides", 0),
                        
                        
                        
                        #FACTOR 1 - MILITARY SECURITY
                        (assign, ":result_for_security", 0),
                        
						#find the lord's home
						(assign, ":base_center", -1),
						(try_begin),
							##diplomacy start+ add support for promoted kingdom ladies
							(is_between, ":troop", heroes_begin, heroes_end),
							(this_or_next|troop_slot_eq, ":troop", slot_troop_occupation, slto_kingdom_hero),
							##diplomacy end+
							(is_between, ":troop", active_npcs_begin, active_npcs_end),
							(try_for_range, ":center", centers_begin, centers_end),
								(eq, ":base_center", -1),
								(party_slot_eq, ":center", slot_town_lord, ":troop"),
								(assign, ":base_center", ":center"),
							(try_end),
						(try_end),
                        
                        (assign, ":faction_has_base", 0),
                        
                        #add up all other centers for the security value
                        (try_for_range, ":center", centers_begin, centers_end),
                          (neq, ":center", ":base_center"),
                          (gt, ":base_center", 0),
                          
                          (try_begin),
                            (is_between, ":center", towns_begin, towns_end),
                            (assign, ":weight", 9000),
                          (else_try),
                            (is_between, ":center", castles_begin, castles_end),
                            (assign, ":weight", 6000),
                          (else_try),
                            (assign, ":weight", 1000),
                          (try_end),
                          
                          (store_distance_to_party_from_party, ":distance", ":base_center", ":center"),
                          (val_add, ":distance", 10),
                          (val_div, ":weight", ":distance"),
                          (val_div, ":weight", ":distance"),
                          
                          (store_faction_of_party, ":center_faction", ":center"),
                          
                          (try_begin),
                            (eq, ":center_faction", ":faction"),
                            
                            (assign, ":faction_has_base", 1),
                            (val_add, ":result_for_security", ":weight"),
                          (else_try),
                            (neq, ":center_faction", ":faction"),
                            (store_relation, ":center_relation", ":center_faction", ":faction"),
                            
                            (try_begin), #potentially hostile center
                              (this_or_next|eq, ":liege_is_undeclared_rebel", 1),
                              (lt, ":center_relation", 0),
                              (val_div, ":weight", 2),
                            (else_try), #neutral center
                              (val_div, ":weight", 4),
                            (try_end),
                            
                            (val_sub, ":result_for_security", ":weight"),
                          (try_end),
                        (try_end),
                        
                        
                        #if a faction controls no other centers, then there is a small bonus
                        (try_begin),
                          (eq, ":faction_has_base", 0),
                          (val_add, ":result_for_security", 20),
                          (try_begin),
                            (eq, "$cheat_mode", 2),
                            (display_message, "str_small_bonus_for_no_base"),
                          (try_end),
                        (try_end),
                        (val_clamp, ":result_for_security", -100, 100),
                        
                        
						(assign, ":result_for_security_weighted", ":result_for_security"),
						##diplomacy start+
					   #ADDED TO THIS, SEE BELOW
						#(try_begin),
						#	(eq, ":lord_reputation", lrep_cunning),
						#	(val_mul, ":result_for_security_weighted", 2),
						#(else_try),
						#	(eq, ":lord_reputation", lrep_martial),
						#	(val_div, ":result_for_security_weighted", 2),
						#(try_end),
						#
						##Use companion morality type "tmt_aristocratic" as a synonym/antonym for bold
						(call_script, "script_dplmc_get_troop_morality_value", ":troop", tmt_aristocratic),
						(assign, ":lord_tmt_aristocratic", reg0),
						(try_begin),
							(lt, ":lord_tmt_aristocratic", 1),
							(this_or_next|lt, ":lord_tmt_aristocratic", 0),
							(eq, ":lord_reputation", lrep_cunning),
							(val_mul, ":result_for_security_weighted", 2),
						(else_try),
							(ge, ":lord_tmt_aristocratic", 0),
							(this_or_next|ge, ":lord_tmt_aristocratic", 1),
							(eq, ":lord_reputation", lrep_martial),
							(val_div, ":result_for_security_weighted", 2),
						(try_end),
						##diplomacy end+
                        
                        
                        
                        #FACTOR 2 - INTERNAL FACTION POLITICS
                        #this is a calculation of how much influence the lord believes he will have in each faction
                        (assign, ":result_for_political", 0),
                        
                        (try_for_range, ":loop_var", "trp_kingdom_heroes_including_player_begin", active_npcs_end),
                          (assign, ":kingdom_hero", ":loop_var"),
                          
                          (this_or_next|troop_slot_eq, ":kingdom_hero", slot_troop_occupation, slto_kingdom_hero),
                          (this_or_next|eq, ":kingdom_hero", "trp_kingdom_heroes_including_player_begin"),
                          (is_between, ":kingdom_hero", pretenders_begin, pretenders_end),
                          
                          (store_faction_of_troop, ":kingdom_hero_faction", ":kingdom_hero"),
                          
                          (try_begin),
                            (eq, ":loop_var", "trp_kingdom_heroes_including_player_begin"),
                            (assign, ":kingdom_hero", "trp_player"),
                            (assign, ":kingdom_hero_faction", "$players_kingdom"),
                            (try_begin), #do not count player relation if the player is trying to suborn the character. this has the slight potential for a miscalculation, if the script is called from outside dialogs and $g_talk_troop has not been reset
                              (eq, "$g_talk_troop", ":troop"),
                              (store_faction_of_troop, ":cur_faction", ":troop"),
                              (eq, ":cur_faction", ":faction"),
                              (assign, ":kingdom_hero_faction", 0),
                            (try_end),
                          (try_end),
                          
                          (eq, ":kingdom_hero_faction", ":faction"),
                          (neg|faction_slot_eq, ":kingdom_hero_faction", slot_faction_leader, ":kingdom_hero"),
                          (neq, ":liege_is_undeclared_rebel", 1),
                          (neg|is_between, ":kingdom_hero", pretenders_begin, pretenders_end),
                          
                          
                          (call_script, "script_troop_get_relation_with_troop", ":troop", ":kingdom_hero"),
                          (assign, ":troop_rel_w_hero", reg0),
                          
                          (call_script, "script_troop_get_relation_with_troop", ":kingdom_hero", ":liege"),
                          (assign, ":hero_rel_w_liege", reg0),
                          
                          (store_mul, ":lord_political_weight", ":troop_rel_w_hero", ":hero_rel_w_liege"),
                          (val_div, ":lord_political_weight", 100),
                          
                          (try_begin),
                            (eq, "$cheat_mode", 2), #disabled
                            (eq, "$g_talk_troop", ":troop"),
                            (str_store_faction_name, s20, ":kingdom_hero_faction"),
                            (str_store_troop_name, s15, ":kingdom_hero"),
                            (assign, reg15, ":lord_political_weight"),
                            (display_message, "str_s15_considered_member_of_faction_s20_weight_of_reg15"),
                          (try_end),
                          
                          (val_add, ":result_for_political", ":lord_political_weight"),
                        (try_end),
                        
                        (val_clamp, ":result_for_political", -100, 101), #lords portion represents half
                        
                        (try_begin),
                          (call_script, "script_troop_get_relation_with_troop", ":troop", ":liege"),
                          (assign, ":liege_relation", reg0),
                          (val_add, ":result_for_political", ":liege_relation"),
                        (try_end),
                        
                        (val_div, ":result_for_political", 2),
                        
                        (val_clamp, ":result_for_political", -100, 101), #liege portion represents half
                        
                        (assign, ":result_for_political_weighted", ":result_for_political"),
                        
                        (try_begin),
                          (this_or_next|eq, ":lord_reputation", lrep_goodnatured),
                          (eq, ":lord_reputation", lrep_quarrelsome),
                          (val_mul, ":result_for_political_weighted", 2),
                        (try_end),
                        
                        #FACTOR 3 - PROMISES AND OTHER ANTICIPATED GAINS
                        #lord's calculation of anticipated gains
                        (assign, ":result_for_material", 0),
                        (assign, ":result_for_material_weighted", ":result_for_material"),
                        
                        
                        #FACTOR 4 - IDEOLOGY
                        #lord's calculation of ideological comfort
                        (try_begin),
                          #Originally, the argument section was not used for a non-player liege. Actually, it can be used
                          (eq, 1, 0),
                          (neq, ":liege", "trp_player"),
                          (neq, ":liege", "$supported_pretender"), #player is advocate for pretender
                          (assign, ":argument_strength", 0),
                          (assign, ":argument_appeal", 0),
                          (assign, ":result_for_argument", 0),
                        (else_try),	#only if the recruitment candidate is either the player, or a supported pretender
                          (troop_get_slot, ":recruitment_argument", ":troop", slot_lord_recruitment_argument),
                          
                          (call_script, "script_rebellion_arguments", ":troop", ":recruitment_argument", ":liege"),
                          (assign, ":argument_appeal", reg0),
                          (assign, ":argument_strength", reg1),
                          
                          (store_add, ":result_for_argument", ":argument_appeal", ":argument_strength"),
                          
                          (store_skill_level, ":player_persuasion_skill", "skl_persuasion", "trp_player"),
                          (try_begin),
                            (gt, ":result_for_argument", 0),
                            #make sure player is the one making the overture
                            
                            #if player has 0 persuasion, ":result_for_argument" will be multiplied by 3/10.
                            (store_add, ":player_persuasion_skill_plus_5_mul_066", ":player_persuasion_skill", 5),
                            (val_mul, ":player_persuasion_skill_plus_5_mul_066", 2),
                            (val_div, ":player_persuasion_skill_plus_5_mul_066", 3),
                            
                            (val_mul, ":result_for_argument", ":player_persuasion_skill_plus_5_mul_066"),
                            (val_div, ":result_for_argument", 10),
                          (else_try),
                            (lt, ":result_for_argument", 0),
                            (store_sub, ":ten_minus_player_persuasion_skill", 10, ":player_persuasion_skill"),
                            (val_mul, ":result_for_argument", ":ten_minus_player_persuasion_skill"),
                            (val_div, ":result_for_argument", 10),
                          (try_end),
                          
                          (try_begin),
                            (neq, ":liege", "trp_player"),
                            (neq, ":liege", "$supported_pretender"), #player is advocate for pretender
                            (val_div, ":argument_strength", 2),
                            (val_div, ":argument_appeal", 2),
                            (val_div, ":result_for_argument", 2),
                          (try_end),
                          
                        (try_end),
                        
                        #	(try_begin),
                        #		(eq, ":lord_reputation", lrep_cunning),
                        #		(val_div, ":result_for_ideological_weighted", 2),
                        #	(else_try),
                        #		(eq, ":lord_reputation", lrep_upstanding),
                        #		(val_mul, ":result_for_ideological_weighted", 2),
                        #	(try_end),
                        
                        
                        #FACTOR 5 - PENALTY FOR CHANGING SIDES
                        (try_begin), #no penalty for the incumbent
                          (store_faction_of_troop, ":cur_faction", ":troop"),
                          (eq, ":cur_faction", ":faction"),
                          (assign, ":penalty_for_changing_sides", 0),
                        (else_try), #penalty for the player
                          (eq, ":liege", "trp_player"),
                          (store_sub, ":penalty_for_changing_sides", 60, "$player_right_to_rule"),
                        (else_try), #same culture, such as a pretender
                          (troop_get_slot, ":orig_faction_of_lord", ":troop", slot_troop_original_faction),
                          (troop_get_slot, ":orig_faction_of_liege", ":liege", slot_troop_original_faction),
                          (eq, ":orig_faction_of_lord", ":orig_faction_of_liege"),
                          (assign, ":penalty_for_changing_sides", 10),
                        (else_try), #a liege from a different culture
                          (assign, ":penalty_for_changing_sides", 50),
                        (try_end),
                        (val_clamp, ":penalty_for_changing_sides", 0, 101),
                        
						(assign, ":penalty_for_changing_sides_weighted", ":penalty_for_changing_sides"),
						##diplomacy start+
						#(try_begin),
						#	(eq, ":lord_reputation", lrep_debauched),
						#	(val_div, ":penalty_for_changing_sides_weighted", 2),
						#(else_try),
						#	(eq, ":lord_reputation", lrep_upstanding),
						#	(val_mul, ":penalty_for_changing_sides_weighted", 2),
						#(try_end),
						#
						##Use companion morality type "tmt_honest" as a synonym/antonym for deal-keeping
						(call_script, "script_dplmc_get_troop_morality_value", ":troop", tmt_honest),
						(assign, ":lord_tmt_honest", reg0),
						(try_begin),
							(this_or_next|lt, ":lord_tmt_honest", 0),
							(eq, ":lord_reputation", lrep_debauched),
							(val_div, ":penalty_for_changing_sides_weighted", 2),
						(else_try),
							(this_or_next|ge, ":lord_tmt_honest", 1),
							(eq, ":lord_reputation", lrep_upstanding),
							(val_mul, ":penalty_for_changing_sides_weighted", 2),
						(try_end),
						##diplomacy end+
                        
                        
                        
                        (assign, reg1, ":result_for_security"),
                        (assign, reg2, ":result_for_security_weighted"),
                        (assign, reg3, ":result_for_political"),
                        (assign, reg4, ":result_for_political_weighted"),
                        (assign, reg5, ":result_for_material"),
                        (assign, reg6, ":result_for_material_weighted"),
                        (assign, reg7, ":argument_strength"),
                        (assign, reg17, ":argument_appeal"),
                        
                        (assign, reg8, ":result_for_argument"),
                        (assign, reg9, ":penalty_for_changing_sides"),
                        (assign, reg10, ":penalty_for_changing_sides_weighted"),
                        
                        
                        (try_begin),
                          (eq, "$cheat_mode", 1),
                          (eq, "$g_talk_troop", ":troop"),
                          (str_store_troop_name, s20, ":troop"),
                          (str_store_faction_name, s21, ":faction"),
                          (str_store_troop_name, s22, ":liege"),
                          
                          (display_message, "@{!}G_talk_troop {s20} evaluates being vassal to {s22} of {s21}"),
                          
                          (display_message, "str_base_result_for_security_reg1"),
                          (display_message, "str_result_for_security_weighted_by_personality_reg2"),
                          (display_message, "str_base_result_for_political_connections_reg3"),
                          (display_message, "str_result_for_political_connections_weighted_by_personality_reg4"),
                          #		(display_message, "@{!}Result for anticipated_gains: {reg5}"),
                          #		(display_message, "@{!}Result for anticipated_gains weighted by personality: {reg6}"),
                          
                          (try_begin),
                            (this_or_next|eq, ":liege", "trp_player"),
                            (eq, ":liege", "$supported_pretender"), #player is advocate for pretender
                            (display_message, "str_result_for_argument_strength_reg7"),
                            (display_message, "str_result_for_argument_appeal_reg17"),
                            (display_message, "str_combined_result_for_argument_modified_by_persuasion_reg8"),
                          (try_end),
                          (display_message, "str_base_changing_sides_penalty_reg9"),
                          (display_message, "str_changing_sides_penalty_weighted_by_personality_reg10"),
                        (try_end),
                        
                        (store_add, ":total", ":result_for_security_weighted", ":result_for_political_weighted"),
                        (val_add, ":total", ":result_for_material_weighted"),
                        (val_add, ":total", ":result_for_argument"),
                        (val_sub, ":total", ":penalty_for_changing_sides_weighted"),
                        
                        
                        (assign, reg0, ":total"),
                        
                        (try_begin),
                          (eq, "$cheat_mode", 2),
                          (display_message, "@{!}DEBUG -- Analyzing lord allegiances, combined bonuses and penalties = {reg0}"),
                          #(display_message, "str_combined_bonuses_and_penalties_=_reg0"),
                        (try_end),
                    ]),
                    
                    
                    
                    ("cf_troop_can_intrigue",
                      #This script should be called from dialogs, and also prior to any event which might result in a lord changing sides
                      [
                        (store_script_param, ":troop", 1),
                        (store_script_param, ":skip_player_party", 2),
                        
						##diplomacy start+
						#Use this to filter out lords who are supposed to be "off the board"
						(assign, ":bad_occupation", 0),
						(try_begin),
						   (gt, ":troop", 0),
							(troop_is_hero, ":troop"),
						   (troop_slot_eq, ":troop", slot_lord_reputation_type, dplmc_slto_dead),
						   (assign, ":bad_occupation", 1),#altered 2011-06-08
						(try_end),
						(eq, ":bad_occupation", 0),
						##diplomacy end+
						
                        (troop_get_slot, ":led_party_1", ":troop", slot_troop_leaded_party),
                        (party_is_active, ":led_party_1"),
                        
                        (try_begin),
                          (eq, "$cheat_mode", 1),
                          (eq, ":troop", "$g_talk_troop"),
                          (display_message, "str_intrigue_test_troop_party_is_active"),
                        (try_end),
                        
                        (party_get_battle_opponent, ":battle_opponent", ":led_party_1"),
                        (le, ":battle_opponent", 0), #battle opponent can be 0 for an attached party?
                        
                        (try_begin),
                          (eq, "$cheat_mode", 1),
                          (eq, ":troop", "$g_talk_troop"),
                          (display_message, "str_intrigue_test_troop_party_is_not_in_battle"),
                        (try_end),
                        
                        (troop_slot_eq, ":troop", slot_troop_prisoner_of_party, -1),
                        
                        (try_begin),
                          (eq, "$cheat_mode", 1),
                          (eq, ":troop", "$g_talk_troop"),
                          (display_message, "str_intrigue_test_troop_is_not_prisoner"),
                        (try_end),
                        
                        (party_get_attached_to, ":led_party_1_attached", ":led_party_1"),
                        
                        (store_faction_of_party, ":led_party_1_faction", ":led_party_1"),
                        
                        (assign, ":other_lords_nearby", 0),
                        (try_for_range, ":troop_2", active_npcs_begin, active_npcs_end),
                          (neq, ":troop", ":troop_2"),
                          (eq, ":other_lords_nearby", 0),
                          
                          (troop_slot_eq, ":troop_2", slot_troop_occupation, slto_kingdom_hero),
                          
                          (troop_get_slot, ":led_party_2", ":troop_2", slot_troop_leaded_party),
                          (party_is_active, ":led_party_2"),
                          (neq, ":led_party_1", ":led_party_2"),
                          
                          (store_faction_of_party, ":led_party_2_faction", ":led_party_2"),
                          (eq, ":led_party_1_faction", ":led_party_2_faction"),
                          
                          (try_begin),
                            (eq, ":led_party_1_attached", -1),
                            (store_distance_to_party_from_party, ":distance", ":led_party_1", ":led_party_2"),
                            (lt, ":distance", 3),
                            (assign, ":other_lords_nearby", 1),
                          (else_try),
                            (is_between, ":led_party_1_attached", walled_centers_begin, walled_centers_end),
                            (party_get_attached_to, ":led_party_2_attached", ":led_party_2"),
                            (eq, ":led_party_1_attached", ":led_party_2_attached"),
                            (assign, ":other_lords_nearby", 1),
                          (try_end),
                        (try_end),
                        
                        (try_begin),
                          (eq, "$cheat_mode", 1),
                          (eq, ":troop", "$g_talk_troop"),
                          (display_message, "str_intrigue_test_troop_is_nearby"),
                        (try_end),
                        
                        (try_begin),
                          (eq, ":skip_player_party", 0),
                          #temporary spot
                        (try_end),
                        
                        (eq, ":other_lords_nearby", 0),
                    ]),
                    
                    
                    ("troop_change_relation_with_troop",
                      [
                        (store_script_param, ":troop1", 1),
                        (store_script_param, ":troop2", 2),
                        (store_script_param, ":amount", 3),
                        
                        (try_begin),
                          (eq, ":troop1", "trp_player"),
                          (call_script, "script_change_player_relation_with_troop", ":troop2", ":amount"),
                        (else_try),
                          (eq, ":troop2", "trp_player"),
                          (call_script, "script_change_player_relation_with_troop", ":troop1", ":amount"),
                        (else_try),
                          (eq, ":troop1", ":troop2"),
                          
                        (else_try),
                          (call_script, "script_troop_get_relation_with_troop", ":troop1", ":troop2"),
                          (store_add, ":new_relation", reg0, ":amount"),
                          
                          (val_clamp, ":new_relation", -100, 101),
                          
                          (try_begin),
                            (eq, ":new_relation", 0),
                            (assign, ":new_relation", 1), #this removes the need for a separate "met" slot - any non-zero relation will be a met
                          (try_end),
                          
                          (store_add, ":troop1_slot_for_troop2", ":troop2", slot_troop_relations_begin),
                          (troop_set_slot, ":troop1", ":troop1_slot_for_troop2", ":new_relation"),
                          
                          (store_add, ":troop2_slot_for_troop1", ":troop1", slot_troop_relations_begin),
                          (troop_set_slot, ":troop2", ":troop2_slot_for_troop1", ":new_relation"),
                        (try_end),
                        
                        
                        (try_begin), #generate controversy if troops are in the same faciton
                          (lt, ":amount", -5),
                          (try_begin),
                            (eq, ":troop1", "trp_player"),
                            (assign, ":faction1", "$players_kingdom"),
                          (else_try),
                            (store_faction_of_troop, ":faction1", ":troop1"),
                          (try_end),
                          (try_begin),
                            (eq, ":troop2", "trp_player"),
                            (assign, ":faction2", "$players_kingdom"),
                          (else_try),
                            (store_faction_of_troop, ":faction2", ":troop2"),
                          (try_end),
                          (eq, ":faction1", ":faction2"),
                          (is_between, ":faction1", kingdoms_begin, kingdoms_end),
                          
                          (store_mul, ":controversy_generated", ":amount", -1),
                          
                          (troop_get_slot, ":controversy1", ":troop1", slot_troop_controversy),
                          (val_add, ":controversy1", ":controversy_generated"),
                          (val_min, ":controversy1", 100),
                          (troop_set_slot, ":troop1", slot_troop_controversy, ":controversy1"),
                          
                          (troop_get_slot, ":controversy2", ":troop2", slot_troop_controversy),
                          (val_add, ":controversy2", ":controversy_generated"),
                          (val_min, ":controversy2", 100),
                          (troop_set_slot, ":troop2", slot_troop_controversy, ":controversy2"),
                          
                        (try_end),
                        
						(try_begin),
							##diplomacy start+ Also enable messages for promoted kingdom ladies
							#OLD:
							#(is_between, ":troop1", active_npcs_begin, active_npcs_end),
							#(is_between, ":troop2", active_npcs_begin, active_npcs_end),
							#
							#NEW:
							(is_between, ":troop1", heroes_begin, heroes_end),
							(this_or_next|troop_slot_eq, ":troop1", slot_troop_occupation, slto_kingdom_hero),
								(is_between, ":troop1", active_npcs_begin, active_npcs_end),
								
							(is_between, ":troop2", heroes_begin, heroes_end),
							(this_or_next|troop_slot_eq, ":troop2", slot_troop_occupation, slto_kingdom_hero),
								(is_between, ":troop2", active_npcs_begin, active_npcs_end),
							##diplomacy end+
							(neq, ":troop1", ":troop2"),
                          
                          (try_begin),
                            (gt, ":amount", 0),
                            (val_add, "$total_relation_adds", ":amount"),
                          (else_try),
                            (val_sub, "$total_relation_subs", ":amount"),
                          (try_end),
                        (try_end),
                        
                        #LAZERAS MODIFIED  {ENTK}
                        # Jrider + TITLES v0.3.2 update title for relation suffix
                        (try_begin),
                          (store_troop_faction, ":troop1_faction", ":troop1"),
                          (store_troop_faction, ":troop2_faction", ":troop2"),
                          (faction_get_slot, ":troop1_faction_leader", ":troop1_faction", slot_faction_leader),
                          (eq, ":troop1_faction", ":troop2_faction"),
                          (eq, ":troop2", ":troop1_faction_leader"),
                          (call_script, "script_troop_set_title_according_to_faction", ":troop1", ":troop1_faction"),
                        (try_end),
                        # Jrider -
                        #LAZERAS MODIFIED  {ENTK}
                        
						(try_begin),
							(eq, "$cheat_mode", 4), #change back to 4
							##diplomacy start+ Also enable messages for promoted kingdom ladies
							#OLD:
							# (is_between, ":troop1", active_npcs_begin, active_npcs_end),
							# (is_between, ":troop2", active_npcs_begin, active_npcs_end),
							#
							#NEW:
							(is_between, ":troop1", heroes_begin, heroes_end),
							(this_or_next|troop_slot_eq, ":troop1", slot_troop_occupation, slto_kingdom_hero),
								(is_between, ":troop1", active_npcs_begin, active_npcs_end),
								
							(is_between, ":troop2", heroes_begin, heroes_end),
							(this_or_next|troop_slot_eq, ":troop2", slot_troop_occupation, slto_kingdom_hero),
								(is_between, ":troop2", active_npcs_begin, active_npcs_end),
							##diplomacy end+
							(neq, ":troop1", ":troop2"),
                          
                          (str_store_troop_name, s20, ":troop1"),
                          (str_store_troop_name, s15, ":troop2"),
                          (assign, reg4, ":amount"),
                          (assign, reg14, ":new_relation"),
                          (display_message, "str_s20_relation_with_s15_changed_by_reg4_to_reg14"),
                          
                          (assign, reg4, "$total_relation_adds"),
                          (display_message, "str_total_additions_reg4"),
                          (assign, reg4, "$total_relation_subs"),
                          (display_message, "str_total_subtractions_reg4"),
                          
                          (assign, reg4, "$total_courtship_quarrel_changes"),
                          (display_message, "@{!}DEBUG -- Total courtship quarrel changes: {reg4}"),
                          
                          (assign, reg4, "$total_random_quarrel_changes"),
                          (display_message, "@{!}DEBUG -- Total random quarrel changes: {reg4}"),
                          
                          (assign, reg4, "$total_battle_ally_changes"),
                          (display_message, "@{!}DEBUG -- Total battle changes for allies: {reg4}"),
                          
                          (assign, reg4, "$total_battle_enemy_changes"),
                          (display_message, "@{!}DEBUG -- Total battle changes for enemies: {reg4}"),
                          
                          (assign, reg4, "$total_promotion_changes"),
                          (display_message, "@{!}DEBUG -- Total promotion changes: {reg4}"),
                          
                          (assign, reg4, "$total_feast_changes"),
                          (display_message, "@{!}DEBUG -- Total feast changes: {reg4}"),
                          
                          (assign, reg4, "$total_policy_dispute_changes"),
                          (assign, reg5, "$number_of_controversial_policy_decisions"), ##1.134
                          (display_message, "@{!}DEBUG -- Total policy dispute changes: {reg4} from {reg5} decisions"), ##1.134
                          
                          (assign, reg4, "$total_indictment_changes"),
                          (display_message, "@{!}DEBUG -- Total faction switch changes: {reg4}"),
                          
                          (assign, reg4, "$total_no_fief_changes"),
                          (display_message, "@{!}DEBUG -- Total no fief changes: {reg4}"),
                          
                          (assign, reg4, "$total_relation_changes_through_convergence"),
                          (display_message, "@{!}DEBUG -- Total changes through convergence: {reg4}"),
                          
                          (assign, reg4, "$total_vassal_days_responding_to_campaign"),
                          (display_message, "@{!}DEBUG -- Total vassal responses to campaign: {reg4}"),
                          
                          (assign, reg4, "$total_vassal_days_on_campaign"),
                          (display_message, "@{!}DEBUG -- Total vassal campaign days: {reg4}"),
                          
                          (val_max, "$total_vassal_days_on_campaign", 1),
                          (store_mul, ":response_rate", "$total_vassal_days_responding_to_campaign", 100),
                          (val_div, ":response_rate", "$total_vassal_days_on_campaign"),
                          (assign, reg4, ":response_rate"),
                          (display_message, "@{!}DEBUG -- Vassal response rate: {reg4}"),
                          
                          
                          
                          #		(assign, reg4, "$total_joy_battle_changes"),
                          #		(display_message, "@{!}DEBUG -- Total joy of battle changes"),
                          
                        (try_end),
                        
                    ]),
                    
                    
					("troop_get_relation_with_troop",
					[
					(store_script_param, ":troop1", 1),
					(store_script_param, ":troop2", 2),

					(assign, ":relation", 0),
					(try_begin),
						##diplomacy start+
						#Change "eq -1", to "lt 0"
						(this_or_next|lt, ":troop1", 0),
							(lt, ":troop2", 0),
						##diplomacy end+

						#Possibly switch to relation with liege
						(assign, ":relation", 0),
					(else_try),
						(eq, ":troop1", "trp_player"),
						(call_script, "script_troop_get_player_relation", ":troop2"),
						(assign, ":relation", reg0),
					(else_try),
						(eq, ":troop2", "trp_player"),
						(call_script, "script_troop_get_player_relation", ":troop1"),
						(assign, ":relation", reg0),
					(else_try),
						(store_add, ":troop1_slot_for_troop2", ":troop2", slot_troop_relations_begin),
						(troop_get_slot, ":relation", ":troop1", ":troop1_slot_for_troop2"),
					(try_end),


					(val_clamp, ":relation", -100, 101),
					(assign, reg0, ":relation"),

					]),
                    
                    
                    
                    ("appoint_faction_marshall",
                      [
                        (store_script_param, ":faction_no", 1),
                        (store_script_param, ":faction_marshall", 2),
                        
                        
                        (faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
                        (faction_get_slot, ":old_marshall", ":faction_no", slot_faction_marshall),
                        
                        (faction_set_slot, ":faction_no", slot_faction_marshall, ":faction_marshall"),
                              
                        (try_begin),
                          (ge, ":old_marshall", 0),
                          (troop_get_slot, ":old_marshall_party", ":old_marshall", slot_troop_leaded_party),
                          (party_is_active, ":old_marshall_party"),
                          (party_set_marshall, ":old_marshall_party", 0),
                        (try_end),
                        
                        
                        (try_begin),
                          (ge, ":faction_marshall", 0),
                          (troop_get_slot, ":new_marshall_party", ":faction_marshall", slot_troop_leaded_party),
                          (party_is_active, ":new_marshall_party"),
                          (party_set_marshall,":new_marshall_party", 1),
                        (try_end),
                        
                        
					(try_begin),
						(neq, ":faction_marshall", ":faction_leader"),
						(neq, ":faction_marshall", ":old_marshall"),
						##diplomacy start+ Support promoted kingdom ladies
						(this_or_next|eq, ":faction_marshall", "trp_player"),
							(is_between, ":faction_marshall", heroes_begin, heroes_end),
						(this_or_next|troop_slot_eq, ":faction_marshall", slot_troop_occupation, slto_kingdom_hero),
						##diplomacy end+
						(this_or_next|eq, ":faction_marshall", "trp_player"),
							(is_between, ":faction_marshall", active_npcs_begin, active_npcs_end),
                          
                          (this_or_next|neq, ":faction_no", "fac_player_supporters_faction"),
                          (neg|check_quest_active, "qst_rebel_against_kingdom"),
                          
                          (try_begin),
                            (eq, "$cheat_mode", 1),
                            (str_store_faction_name, s15, ":faction_no"),
                            (display_message, "str_checking_lord_reactions_in_s15"),
                          (try_end),
                          
                          
                          (call_script, "script_troop_change_relation_with_troop", ":faction_marshall", ":faction_leader", 5),
                          (val_add, "$total_promotion_changes", 5),
                          
						##diplomacy start+
						(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", ":faction_no"),
						(assign, ":player_standing_in_faction", reg0),
						#(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
						
						#Support promoted kingdom ladies
						##OLD:
						#(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
						##NEW:
						(try_for_range, ":lord", heroes_begin, heroes_end),
						##diplomacy end+
							(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
							(store_faction_of_troop, ":lord_faction", ":lord"),
							(eq, ":lord_faction", ":faction_no"),

							(neq, ":lord", ":faction_marshall"),
							(neq, ":lord", ":faction_leader"),

							(call_script, "script_troop_get_relation_with_troop", ":faction_marshall", ":lord"),
				#			(try_begin),
				#				(eq, "$cheat_mode", 1),
				#				(str_store_troop_name, s14, ":lord"),
				#				(str_store_troop_name, s17, ":faction_marshall"),
				#				(display_message, "@{!}{s14}'s relation with {s17} is {reg0}"),
				#			(try_end),
							(store_sub, ":adjust_relations", reg0, 10),
							(val_div, ":adjust_relations", 15),
							##diplomacy start+
							#In some situtations the player can set the marshall freely even though he isn't the faction leader.
							(try_begin),
								(eq, ":faction_marshall", "trp_player"),
								(ge, ":player_standing_in_faction", DPLMC_FACTION_STANDING_LEADER_SPOUSE),
								#Still allow a relation gain below if the lord had actively supported the player
								#(which doesn't happen now if the player is the ruler, but could).
								(val_min, ":adjust_relations", 0),
							(try_end),
							##diplomacy end+
							(neq, ":adjust_relations", 0),

							#Not negatively affected if they favored the lord
							(try_begin),
								(troop_slot_eq, ":lord", slot_troop_stance_on_faction_issue, ":faction_marshall"),
								(val_add, ":adjust_relations", 1),
								(val_max, ":adjust_relations", 0),
							(try_end),

							(call_script, "script_troop_change_relation_with_troop", ":faction_leader", ":lord", ":adjust_relations"),
							(val_add, "$total_promotion_changes", ":adjust_relations"),

							(lt, ":adjust_relations", -2),
							(store_random_in_range, ":random", 1, 10),

							(val_add, ":adjust_relations", ":random"),

							(lt, ":adjust_relations", 0),

							(str_store_troop_name, s14, ":lord"),
							(str_store_troop_name, s15, ":faction_marshall"),

							(try_begin),
							##diplomacy start+ Show protest information for your own kingdom if you have a chancellor or are the ruler
								(ge, ":player_standing_in_faction", DPLMC_FACTION_STANDING_MEMBER),
								(this_or_next|ge, ":player_standing_in_faction", DPLMC_FACTION_STANDING_LEADER_SPOUSE),#<- via the minister, or just hearing about it
									(gt, "$g_player_chancellor", 0),#<- via your chancellor
								(neg|troop_slot_eq, ":lord", slot_troop_met, 0),
								(display_message, "str_s14_protests_the_appointment_of_s15_as_marshall"),
							(else_try),
								(call_script, "script_dplmc_store_troop_is_eligible_for_affiliate_messages", ":lord"),
								(this_or_next|gt, reg0, 0),
							##diplomacy end+
								(eq, "$cheat_mode", 1),
								(display_message, "str_s14_protests_the_appointment_of_s15_as_marshall"),
							(try_end),

							(call_script, "script_troop_change_relation_with_troop", ":faction_leader", ":lord", -10),
							(call_script, "script_troop_change_relation_with_troop", ":faction_marshall", ":lord", -5),
							(val_add, "$total_promotion_changes", -15),

							(call_script, "script_add_log_entry", logent_lord_protests_marshall_appointment, ":lord",  ":faction_marshall", ":faction_leader", "$g_encountered_party_faction"),

						(try_end),
					(try_end),

						]),
                    
                    #it might be easier to monitor whether prices are following an intuitive pattern if we separate production from consumption
                    #the current system still works very well, however
						("center_get_item_consumption",
						  [
						]),
						
						("locate_player_minister", #maybe deprecate this
						[
						##diplomacy start+ Handle player is co-ruler of NPC faction
						(assign, ":alt_faction", "fac_player_supporters_faction"),
						(try_begin),
							(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
							(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
							(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
							(assign, ":alt_faction", "$players_kingdom"),
						(try_end),
						##diplomacy end+
						(assign, ":walled_center_found", 0),
						(try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
							(lt, ":walled_center_found", centers_begin),
							(store_faction_of_party, ":walled_center_faction", ":walled_center"),
							##diplomacy start+
							(this_or_next|eq, ":walled_center_faction", ":alt_faction"),
							##diplomacy end+
							(eq, ":walled_center_faction", "fac_player_supporters_faction"),
							(neg|party_slot_ge, ":walled_center", slot_town_lord, active_npcs_begin), #ie, player or a reserved slot
							(assign, ":walled_center_found", ":walled_center"),
						(try_end),

						(troop_get_slot, ":old_location", "$g_player_minister", slot_troop_cur_center),
						(troop_set_slot, "$g_player_minister", slot_troop_cur_center, ":walled_center_found"),

						(try_begin),
							(neq, ":old_location", ":walled_center"),
							(str_store_party_name, s10, ":walled_center"),
							(str_store_troop_name, s11, "$g_player_minister"),
							(display_message, "str_s11_relocates_to_s10"),
						(try_end),

						]),
                    
                    
						("lord_get_home_center",
						[
						  (store_script_param, ":troop_no", 1),
						  (assign, ":result", -1),

							##diplomacy start+
							(assign, ":best_score", -1),
							(troop_get_slot, ":troop_original_faction", ":troop_no", slot_troop_original_faction),
							#The default script prefers towns to castles, but aside from that is
							#fairly arbitrary.  Add scores that take into account original faction
							#and so forth.
						  (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
							(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
							  (assign, ":center_score", 10),#10 for castles, 20 for towns
							  (try_begin),
								 (is_between, ":center_no", towns_begin, towns_end),
								  (assign, ":center_score", 20),
							  (try_end),
							  (try_begin),
								 (troop_slot_eq, ":troop_no", slot_troop_home, ":center_no"),
								  (val_add, ":center_score", 6),
							(else_try),
								  (party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":troop_no"),
								  (val_add, ":center_score", 5),
							  (else_try),
								 (is_between, ":troop_original_faction", kingdoms_begin, kingdoms_end),
								  (party_slot_eq, ":center_no", slot_center_original_faction, ":troop_original_faction"),
								  (val_add, ":center_score", 4),
							  (try_end),
							  (gt, ":center_score", ":best_score"),
							(assign, ":result", ":center_no"),
							  (assign, ":best_score", ":center_score"),
						  (try_end),
							##diplomacy end+

						  (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
							(eq, ":result", -1),
							(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
							(assign, ":result", ":center_no"),
						  (try_end),
                        
                        #NOTE : In old code if a lord has no walled center then home city of this lord is assigning to
                        #faction leader's home city. Now I changed this to assign home cities more logical and homogeneous.
                        #In new code if a lord has no walled center then his home city becomes his village's border_city.
                        #This means his home city becomes owner city of his village. If he has no village then as last change
                        #his home city become faction leader's home city.
                        (try_begin),
                          (eq, ":result", -1),
                          (try_for_range, ":center_no", centers_begin, centers_end),
                            (eq, ":result", -1),
                            (party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
                            
                            (try_begin),
                              (neg|is_between, ":center_no", walled_centers_begin, walled_centers_end),
                              (party_get_slot, ":bound_center", ":center_no", slot_village_bound_center),
                              (assign, ":result", ":bound_center"),
                            (try_end),
                          (try_end),
                        (try_end),
                        
                        #If lord has no walled center and is player faction, then assign player court ##1.132, 11 new lines
                        (try_begin),
                          (eq, ":result", -1),
                          (store_faction_of_troop, ":faction_no", ":troop_no"),
                          (eq, ":faction_no", "fac_player_supporters_faction"),
                          (is_between, "$g_player_court", walled_centers_begin, walled_centers_end),
                          (store_faction_of_party, ":player_court_faction", "$g_player_court"),
                          (eq, ":player_court_faction", "fac_player_supporters_faction"),
                          
                          (assign, ":result", "$g_player_court"),
                        (try_end), ##
                        
                        #If lord has no walled center and any not walled village then assign faction capital
                        (try_begin),
                          (eq, ":result", -1),
                          (store_faction_of_troop, ":faction_no", ":troop_no"),
                          (faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
                          (neq, ":troop_no", ":faction_leader"),
						  (ge, ":faction_leader", 0), # Bugfix to filter invalid faction leader values.  Floris 2.6 - Windyplains
                          (call_script, "script_lord_get_home_center", ":faction_leader"),
                          (gt, reg0, -1),
                          (assign, ":result", reg0),
                        (try_end),
                        
                        #Any center of the faction
                        (try_begin),
                          (eq, ":result", -1),
                          (store_faction_of_troop, ":faction_no", ":troop_no"),
                          
                          (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
                            (eq, ":result", -1),
                            
                            (store_faction_of_party, ":center_faction", ":walled_center"),
                            (eq, ":faction_no", ":center_faction"),
                            (assign, ":result", ":walled_center"),
                          (try_end),
                        (try_end),
                        
                        
                        
                        (assign, reg0, ":result"),
                    ]),
                    
                    
                    
                    
                    ("get_kingdom_lady_social_determinants", #Calradian society is rather patriarchal, at least among the upper classes
                      [
                        (store_script_param, ":kingdom_lady", 1),
                        
                        (store_faction_of_troop, ":faction_of_lady", ":kingdom_lady"),
                        (assign, ":center", -1),
                        (assign, ":closest_male_relative", -1),
                        (assign, ":best_center_score", 0),
                        
						##diplomacy start+
						##TODO: Re-implement, disabled for now.  "Don't get stuck attached to a MIA relative"
						(try_begin),
							(troop_slot_ge, ":kingdom_lady", slot_troop_spouse, 0),
							(troop_get_slot, ":closest_male_relative", ":kingdom_lady", slot_troop_spouse),
							#(neg|troop_slot_ge, ":closest_male_relative", slot_troop_occupation, slto_retirement),#added: has not been removed from play
						(else_try),
							(troop_slot_ge, ":kingdom_lady", slot_troop_father, 0),
							(troop_get_slot, ":closest_male_relative", ":kingdom_lady", slot_troop_father),
							#(neg|troop_slot_ge, ":closest_male_relative", slot_troop_occupation, slto_retirement),#added: has not been removed from play
						(else_try),
							#added
							(troop_slot_ge, ":kingdom_lady", slot_troop_mother, 0),
							(troop_get_slot, ":closest_male_relative", ":kingdom_lady", slot_troop_mother),
							(troop_slot_eq, ":closest_male_relative", slot_troop_occupation, slto_kingdom_hero),
						(else_try),
							(troop_slot_ge, ":kingdom_lady", slot_troop_guardian, 0),
							(troop_get_slot, ":closest_male_relative", ":kingdom_lady", slot_troop_guardian),
							#(neg|troop_slot_ge, ":closest_male_relative", slot_troop_occupation, slto_retirement),#added: has not been removed from play
						(try_end),
						##diplomacy end+

						##diplomacy start+
						#Avoid strange problems if the argument is not a kingdom lady.
						(try_begin),
							(this_or_next|is_between, ":kingdom_lady", kingdom_ladies_begin, kingdom_ladies_end),
								(troop_slot_eq, ":kingdom_lady", slot_troop_occupation, slto_kingdom_lady),
							(neg|troop_slot_eq, ":kingdom_lady", slot_troop_occupation, slto_kingdom_hero),
							(assign, ":is_lady", 1),
						(else_try),
							(assign, ":is_lady", 0),
							(assign, ":closest_male_relative", ":kingdom_lady"),# is doing this useful for the way this script is used, or should we just set it to -1?
						(try_end),
						
						##OLD:
						#(try_begin), #if ongoing social event (maybe add if not besieged)
						##NEW:
						(try_begin),
							(eq, ":is_lady", 0),
							(call_script, "script_lord_get_home_center", ":kingdom_lady"),
							(assign, ":center", reg0),
							(is_between, ":center", walled_centers_begin, walled_centers_end),
						(else_try), #if ongoing social event (maybe add if not besieged)
						##diplomacy end+
							(faction_slot_eq, ":faction_of_lady", slot_faction_ai_state, sfai_feast),
							(faction_get_slot, ":feast_center", ":faction_of_lady", slot_faction_ai_object),

							(gt, ":closest_male_relative", -1),
							(troop_get_slot, ":closest_male_party", ":closest_male_relative", slot_troop_leaded_party),
							(party_is_active, ":closest_male_party"),
							(party_get_attached_to, ":closest_male_cur_location", ":closest_male_party"),

							(eq, ":closest_male_cur_location", ":feast_center"),
							(is_between, ":feast_center", walled_centers_begin, walled_centers_end),

							(assign, ":center", ":feast_center"),

						(else_try),
							(troop_slot_eq, "trp_player", slot_troop_spouse, ":kingdom_lady"),
							###diplomacy begin
							(try_begin),
							##diplomacy end
								(is_between, "$g_player_court", walled_centers_begin, walled_centers_end),
								(assign, ":center", "$g_player_court"),
								##diplomacy begin
							(else_try),
							  (troop_get_slot, ":cur_residence", ":kingdom_lady", slot_troop_cur_center),
							  (is_between, ":cur_residence", walled_centers_begin, walled_centers_end),
							  (party_slot_eq, ":cur_residence", slot_town_lord, "trp_player"),
							  (assign, ":center", ":cur_residence"),
							(try_end),
							(is_between, ":center",  walled_centers_begin, walled_centers_end),
							##diplomacy end
						(else_try),
							(try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
								(store_faction_of_party, ":walled_center_faction", ":walled_center"),
								(this_or_next|eq, ":faction_of_lady", ":walled_center_faction"),
									(neg|is_between, ":faction_of_lady", kingdoms_begin, kingdoms_end), #lady married to a player without a faction

								(party_get_slot, ":castle_lord", ":walled_center", slot_town_lord),

								(gt, ":castle_lord", -1),

								(call_script, "script_troop_get_family_relation_to_troop", ":kingdom_lady", ":castle_lord"),
								##diplomacy start+
								(try_begin),
									(eq, ":is_lady", 0),
									(eq, ":castle_lord", ":kingdom_lady"),
									(val_max, reg0, 16),
								(try_end),
								##diplomacy end+

								(try_begin),
									(this_or_next|is_between, ":faction_of_lady", kingdoms_begin, kingdoms_end),
										(troop_slot_eq, "trp_player", slot_troop_spouse, ":kingdom_lady"),

									(faction_slot_eq, ":faction_of_lady", slot_faction_leader, ":castle_lord"),
									(val_max, reg0, 1),
								(try_end),

								(try_begin),
									(eq, "$cheat_mode", 2),
									(str_store_troop_name, s3, ":kingdom_lady"),
									(str_store_troop_name, s4, ":castle_lord"),
									(str_store_party_name, s5, ":walled_center"),
									(display_message, "str_checking_s3_at_s5_with_s11_relationship_with_s4_score_reg0"),
									(str_clear, s11),
								(try_end),

								(gt, reg0, ":best_center_score"),

								(assign, ":best_center_score", reg0),
								(assign, ":center", ":walled_center"),


							(try_end),
						(try_end),

						(assign, reg0, ":closest_male_relative"),
						(assign, reg1, ":center"),


						]),
                    
                    
                    #This is probably unnecessarily complicated, but can support a multi-generational mod
                    ("age_troop_one_year",
					[
						(store_script_param, ":troop_no", 1),
						##diplomacy start+ use gender script
						#(troop_get_type, ":is_female", ":troop_no"),
						(assign, ":save_reg0", reg0),
						(call_script, "script_dplmc_store_troop_is_female", ":troop_no"),
						(assign, ":is_female", reg0),
						(assign, reg0, ":save_reg0"),
						##diplomacy end+
                        
                        (troop_get_slot, ":age", ":troop_no", slot_troop_age),
                        (troop_get_slot, ":appearance", ":troop_no", slot_troop_age_appearance),
                        
                        (val_add, ":age", 1),
                        (store_random_in_range, ":addition", 1, 5),
                        
                        (try_begin),
                          (eq, ":is_female", 1),
                          #		(val_add, ":addition", 2), #the women's age slider seems to produce less change than the male one - commented out: makes women look too old.
                        (try_end),
                        
                        (val_add, ":appearance", ":addition"),
                        (try_begin),
                          (gt, ":age", 45),
                          (store_attribute_level, ":strength", ":troop_no", ca_strength),
                          (store_attribute_level, ":agility", ":troop_no", ca_agility),
                          (store_random_in_range, ":random", 0, 50), #2% loss brings it down to about 36% by age 90, but of course can be counteracted by new level gain
                          (try_begin),
                            (lt, ":random", ":strength"),
                            (troop_raise_attribute, ":troop_no", ca_strength, -1), ##1.134
                          (try_end),
                          (try_begin),
                            (lt, ":random", ":agility"),
                            (troop_raise_attribute, ":troop_no", ca_agility, -1), ##1.134
                          (try_end),
                        (try_end),
                        
                        (val_clamp, ":appearance", 1, 100),
                        
                        (troop_set_slot, ":troop_no", slot_troop_age, ":age"),
                        (troop_set_slot, ":troop_no", slot_troop_age_appearance, ":appearance"),
                        (troop_set_age, ":troop_no", ":appearance"),
                    ]),
                    
                    
                    ("add_lady_items",
                      [
                        (store_script_param, ":lady_no", 1),
                        (troop_equip_items, ":lady_no"),
                        
                        (store_faction_of_troop, ":faction_no", ":lady_no"),
                        
                        (store_random_in_range, ":random", 0, 6),
                        
                        (try_begin), #assign clothes
                          (this_or_next|troop_slot_eq, ":lady_no", slot_lord_reputation_type, lrep_adventurous),
                          (troop_slot_eq, ":lady_no", slot_lord_reputation_type, lrep_ambitious),
                          
                          (this_or_next|troop_slot_eq, ":lady_no", slot_lord_reputation_type, lrep_adventurous),
                          (lt, ":random", 2),
                          
                          (neg|troop_slot_ge, ":lady_no", slot_troop_age, 40),
                          (try_begin),
                            (eq, ":faction_no", "fac_kingdom_1"),
                            (lt, ":random", 6),
                            (troop_add_item, ":lady_no", "itm_ar_swa_t2_gambeson_a", 0),
                          (else_try),
                            (eq, ":faction_no", "fac_kingdom_2"),
                            (lt, ":random", 5),
                            (troop_add_item, ":lady_no", "itm_ar_vae_t2_leather_a", 0),
                          (else_try),
                            (eq, ":faction_no", "fac_kingdom_3"),
                            (lt, ":random", 4),
                            (troop_add_item, ":lady_no", "itm_ar_khe_t2_armor_a", 0),
                          (else_try),
                            (eq, ":faction_no", "fac_kingdom_4"),
                            (lt, ":random", 3),
                            (troop_add_item, ":lady_no", "itm_ar_nor_t2_vikinglamellar_a", 0),
                          (else_try),
                            (eq, ":faction_no", "fac_kingdom_5"),
                            (lt, ":random", 2),
                            (troop_add_item, ":lady_no", "itm_ar_rho_t2_ragged_a", 0),
                          (else_try),
                            (eq, ":faction_no", "fac_kingdom_6"),
                            (lt, ":random", 1),
                            (troop_add_item, ":lady_no", "itm_ar_sar_t2_quilted_a", 0),
                          (else_try),
                            (troop_add_item, ":lady_no", "itm_ar_pla_t2_tabard_a", 0),
                          (try_end),
                        (else_try),
                          (eq, ":faction_no", "fac_kingdom_1"),
                          (try_begin),
                            (lt, ":random", 2),
                            (troop_add_item, ":lady_no", "itm_dress_swadia_lady_a", 0),
                          (else_try),
                            (troop_add_item, ":lady_no", "itm_dress_swadia_lady_b", 0),
                          (try_end),
                        (else_try),
                          (eq, ":faction_no", "fac_kingdom_2"),
                          (try_begin),
                            (eq, ":random", 0),
                            (troop_add_item, ":lady_no", "itm_dress_vaegir_lady_a", 0),
                          (else_try),
                            (lt, ":random", 5),
                            (neg|troop_slot_eq, ":lady_no", slot_lord_reputation_type, lrep_conventional),
                            (neg|troop_slot_eq, ":lady_no", slot_lord_reputation_type, lrep_ambitious),
                            (troop_add_item, ":lady_no", "itm_dress_vaegir_common_a", 0),
                          (else_try),
                            (troop_add_item, ":lady_no", "itm_dress_vaegir_lady_b", 0),
                          (try_end),
                        (else_try),
                          (eq, ":faction_no", "fac_kingdom_3"),
                          (try_begin),
                            (eq, ":random", 0),
                            (troop_add_item, ":lady_no", "itm_dress_khergit_lady_a", 0),
                          (else_try),
                            (troop_add_item, ":lady_no", "itm_dress_khergit_lady_b", 0),
                          (try_end),
                        (else_try),
                          (eq, ":faction_no", "fac_kingdom_4"),
                          (try_begin),
                            (eq, ":random", 0),
                            (troop_add_item, ":lady_no", "itm_dress_nord_lady_a", 0),
                          (else_try),
                            (troop_add_item, ":lady_no", "itm_dress_nord_lady_b", 0),
                          (try_end),
                        (else_try),
                          (eq, ":faction_no", "fac_kingdom_5"),
                          (try_begin),
                            (eq, ":random", 0),
                            (troop_add_item, ":lady_no", "itm_dress_rhodok_lady_a", 0),
                          (else_try),
                            (troop_add_item, ":lady_no", "itm_dress_rhodok_lady_b", 0),
                          (try_end),
                        (else_try),
                          (eq, ":faction_no", "fac_kingdom_6"),
                          (try_begin),
                            (eq, ":random", 0),
                            (troop_add_item, ":lady_no", "itm_dress_sarranid_lady_a", 0),
                          (else_try),
                            (troop_add_item, ":lady_no", "itm_dress_sarranid_lady_b", 0),
                          (try_end),
                        (try_end),
                        (troop_equip_items, ":lady_no"),
                        
                        #also available:
                        #itm_blue_dress
                        #itm_court_dress
                        
                        #to add for khergits -- salwar/shalvar?
                        #western tang costume (p105, china's golden age)
                        #kipchak woman from russia book
                        
                        (try_begin), #assign headguear matched to item
                          (this_or_next|troop_has_item_equipped, ":lady_no", "itm_ar_swa_t2_gambeson_a"),
                          (this_or_next|troop_has_item_equipped, ":lady_no", "itm_ar_vae_t2_leather_a"),
                          (this_or_next|troop_has_item_equipped, ":lady_no", "itm_ar_khe_t2_armor_a"),
                          (this_or_next|troop_has_item_equipped, ":lady_no", "itm_ar_nor_t2_vikinglamellar_a"),
                          (this_or_next|troop_has_item_equipped, ":lady_no", "itm_ar_rho_t2_ragged_a"),
                          (this_or_next|troop_has_item_equipped, ":lady_no", "itm_ar_sar_t2_quilted_a"),
                          (troop_has_item_equipped, ":lady_no", "itm_ar_pla_t2_tabard_a"),
                          
                          #assign no headgear
                        (else_try),
                          (this_or_next|troop_slot_eq, ":lady_no", slot_lord_reputation_type, lrep_moralist),
                          (this_or_next|troop_slot_eq, ":lady_no", slot_lord_reputation_type, lrep_conventional),
                          (lt, ":random", 2),
                          
                          
                          (try_begin),
                            (troop_has_item_equipped, ":lady_no", "itm_dress_swadia_lady_a"),
                            (troop_add_item, ":lady_no", "itm_he_swa_lad_lady_a", 0),

                            (str_store_troop_name, s4, ":lady_no"),
                            #			(display_message, "@Giving ruby turret hat to {s4}"),
                          (else_try),
                            (troop_has_item_equipped, ":lady_no", "itm_dress_swadia_lady_b"),
                            (troop_add_item, ":lady_no", "itm_he_swa_lad_lady_a", 0),
                            
                            (str_store_troop_name, s4, ":lady_no"),
                            #			(display_message, "@Giving ruby turret hat to {s4}"),
                          (else_try),
                            (troop_has_item_equipped, ":lady_no", "itm_dress_vaegir_lady_a"),
                            (troop_add_item, ":lady_no", "itm_he_vae_lad_lady_a", 0),
                            
                            (str_store_troop_name, s4, ":lady_no"),
                            #			(display_message, "@Giving blue turret hat to {s4}"),
                          (else_try),
                            (troop_has_item_equipped, ":lady_no", "itm_dress_vaegir_lady_b"),
                            (troop_add_item, ":lady_no", "itm_he_vae_lad_lady_a", 0),
                            
                            (str_store_troop_name, s4, ":lady_no"),
                            #			(display_message, "@Giving green turret hat to {s4}"),
                          (else_try),
                            (troop_has_item_equipped, ":lady_no", "itm_dress_khergit_lady_a"),
                            (troop_add_item, ":lady_no", "itm_he_khe_lad_lady_a", 0),
                            
                            (str_store_troop_name, s4, ":lady_no"),
                            #			(display_message, "@Giving green-lined wimple to {s4}"),
                          (else_try),
                            (troop_has_item_equipped, ":lady_no", "itm_dress_khergit_lady_b"),
                            (troop_add_item, ":lady_no", "itm_he_khe_lad_lady_a", 0),
                            
                            (str_store_troop_name, s4, ":lady_no"),
                            #			(display_message, "@Giving green-lined wimple to {s4}"),
                          (else_try),
                            (troop_has_item_equipped, ":lady_no", "itm_dress_nord_lady_a"),
                            (troop_add_item, ":lady_no", "itm_he_nor_lad_lady_a", 0),
                            
                            (str_store_troop_name, s4, ":lady_no"),
                            #			(display_message, "@Giving green-lined wimple to {s4}"),
                          (else_try),
                            (troop_has_item_equipped, ":lady_no", "itm_dress_nord_lady_b"),
                            (troop_add_item, ":lady_no", "itm_he_nor_lad_lady_a", 0),
                            
                            (str_store_troop_name, s4, ":lady_no"),
                            #			(display_message, "@Giving green-lined wimple to {s4}"),
                          (else_try),
                            (troop_has_item_equipped, ":lady_no", "itm_dress_rhodok_lady_a"),
                            (troop_add_item, ":lady_no", "itm_he_rho_lad_lady_a", 0),
                            
                            (str_store_troop_name, s4, ":lady_no"),
                            #			(display_message, "@Giving green-lined wimple to {s4}"),
                          (else_try),
                            (troop_has_item_equipped, ":lady_no", "itm_dress_rhodok_lady_b"),
                            (troop_add_item, ":lady_no", "itm_he_rho_lad_lady_a", 0),
                            
                            (str_store_troop_name, s4, ":lady_no"),
                            #			(display_message, "@Giving green-lined wimple to {s4}"),
                          (else_try),
                            (troop_has_item_equipped, ":lady_no", "itm_dress_sarranid_lady_a"),
                            (troop_add_item, ":lady_no", "itm_he_sar_lad_lady_a", 0),
                            
                            (str_store_troop_name, s4, ":lady_no"),
                            #			(display_message, "@Giving green-lined wimple to {s4}"),
                          (else_try),
                            (troop_has_item_equipped, ":lady_no", "itm_dress_sarranid_lady_b"),
                            (troop_add_item, ":lady_no", "itm_he_sar_lad_lady_a", 0),
                            
                            (str_store_troop_name, s4, ":lady_no"),
                            #			(display_message, "@Giving green-lined wimple to {s4}"),
                          (try_end),
                        (try_end),
                        (troop_equip_items, ":lady_no"),
                        
                      ]
                    ),
                    
                    ("init_troop_age",
                      [
                        (store_script_param, ":troop_no", 1),
                        (store_script_param, ":age", 2), #minimum 20
                        
                        (try_begin),
                          (gt, ":age", 20),
                          (troop_set_slot, ":troop_no", slot_troop_age, 20),
                        (else_try),
                          (troop_set_slot, ":troop_no", slot_troop_age, ":age"),
                        (try_end),
                        
                        (store_sub, ":years_to_age", ":age", 20),
                        (troop_set_age, ":troop_no", 0),
                        
                        (try_begin),
                          (gt, ":years_to_age", 0),
                          (try_for_range, ":unused", 0, ":years_to_age"),
                            (call_script, "script_age_troop_one_year", ":troop_no"),
                          (try_end),
                        (try_end),
                        
                    ]),
                    
                    
                    ("assign_troop_love_interests", #Called at the beginning, or whenever a lord is spurned
					[
						(store_script_param, ":cur_troop", 1),
						##diplomacy start+
						#wrap the entire thing in a try-statement: do nothing when called erroneously
						(assign, ":save_reg0", reg0),
						(assign, ":save_reg1", reg1),
						(try_begin),
						(this_or_next|is_between, ":cur_troop", lords_begin, lords_end),
						(this_or_next|is_between, ":cur_troop", companions_begin, companions_end),
						(troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),#kingdom heroes only
						(troop_slot_eq, ":cur_troop", slot_troop_spouse, -1),#not married, engaged
						(troop_slot_eq, ":cur_troop", slot_troop_betrothed, -1),
						
						#avoid unintentional erroneous pairings (intentional exceptions can be added)
						#(troop_get_type, ":troop_type", ":cur_troop"),
						(call_script, "script_dplmc_store_troop_is_female", ":cur_troop"),
						(assign, ":troop_type", reg0),

						(try_begin),
							#Certain personality types don't care about flouting convention.
							(this_or_next|troop_slot_eq, ":cur_troop", slot_lord_reputation_type, lrep_debauched),
							(this_or_next|troop_slot_eq, ":cur_troop", slot_lord_reputation_type, lrep_roguish),
							(troop_slot_eq, ":cur_troop", slot_lord_reputation_type, lrep_adventurous),
							(assign, ":troop_type", abs(tf_male) + abs(tf_female) + 1),#guaranteed not to equal tf_male or tf_female
						(try_end),
						(store_faction_of_troop, ":troop_faction", ":cur_troop"),
						#assign default initial courtships for companions
						(try_begin),
							(is_between, ":cur_troop", companions_begin, companions_end),
							(troop_get_slot, ":cur_lady", ":cur_troop", slot_troop_personalitymatch_object),
							(is_between, ":cur_lady", heroes_begin, heroes_end),
									
							(store_faction_of_troop, ":lady_faction", ":cur_lady"),
							(eq, ":troop_faction", ":lady_faction"),
							#(call_script, "script_troop_get_family_relation_to_troop", ":cur_troop", ":cur_lady"),	
							(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":cur_troop", ":cur_lady"),
							(lt, reg0, 2),#check not a close relative
							#(troop_get_type, reg0, ":cur_lady"),
							(call_script, "script_dplmc_store_troop_is_female", ":cur_lady"),
							(neq, ":troop_type", reg0),#check gender compatability
							(neq, ":cur_lady", ":cur_troop"),#check not yourself
							(neg|troop_slot_ge, ":cur_lady", slot_troop_occupation, slto_retirement),#check in the game and not retired, exiled, dead, etc.
							(troop_slot_ge, ":cur_lady", slot_troop_occupation, slto_kingdom_hero),
							(call_script, "script_troop_get_relation_with_troop", ":cur_troop", ":cur_lady"),
							(ge, reg0, 0), #do not develop love interest if already spurned (but DO allow re-courting)
							
							(neg|troop_slot_eq, ":cur_troop", slot_troop_love_interest_1, ":cur_lady"),
							(neg|troop_slot_eq, ":cur_troop", slot_troop_love_interest_2, ":cur_lady"),
							(neg|troop_slot_eq, ":cur_troop", slot_troop_love_interest_3, ":cur_lady"),
							(try_begin),
								(this_or_next|troop_slot_eq, ":cur_troop", slot_troop_love_interest_1, -1),
								(troop_slot_eq, ":cur_troop", slot_troop_love_interest_1, 0),
								(troop_set_slot, ":cur_troop", slot_troop_love_interest_1, ":cur_lady"),
							(else_try),
								(this_or_next|troop_slot_eq, ":cur_troop", slot_troop_love_interest_2, -1),
								(troop_slot_eq, ":cur_troop", slot_troop_love_interest_2, 0),
								(troop_set_slot, ":cur_troop", slot_troop_love_interest_2, ":cur_lady"),
							(else_try),
								(this_or_next|troop_slot_eq, ":cur_troop", slot_troop_love_interest_3, -1),
								(troop_slot_eq, ":cur_troop", slot_troop_love_interest_3, 0),
								(troop_set_slot, ":cur_troop", slot_troop_love_interest_3, ":cur_lady"),
							(try_end),
						(try_end),
						##diplomacy end+
						(try_for_range, ":unused", 0, 50),
							(store_random_in_range, ":cur_lady", kingdom_ladies_begin, kingdom_ladies_end),
							(troop_slot_eq, ":cur_lady", slot_troop_spouse, -1),
							(store_faction_of_troop, ":lady_faction", ":cur_lady"),
							(eq, ":troop_faction", ":lady_faction"),
							##diplomacy start+
							##(call_script, "script_troop_get_family_relation_to_troop", ":cur_troop", ":cur_lady"),
							(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":cur_troop", ":cur_lady"),
							#(eq, reg0, 0),
							#right now nothing gives a value of 1, but change this check in case more distant relations are reported		
							(lt, reg0, 2),#check not a close relative
							#(troop_get_type, reg0, ":cur_lady"),
							(call_script, "script_dplmc_store_troop_is_female", ":cur_lady"),
							(neq, ":troop_type", reg0),#check gender compatability
							(neq, ":cur_lady", ":cur_troop"),#check not yourself
							(neg|troop_slot_ge, ":cur_lady", slot_troop_occupation, slto_retirement),#check in the game and not retired, exiled, dead, etc.
							(troop_slot_ge, ":cur_lady", slot_troop_occupation, slto_kingdom_hero),
							##diplomacy end+
							(call_script, "script_troop_get_relation_with_troop", ":cur_troop", ":cur_lady"),
							
							(eq, reg0, 0), #do not develop love interest if already spurned or courted

							(neg|troop_slot_eq, ":cur_troop", slot_troop_love_interest_1, ":cur_lady"),
							(neg|troop_slot_eq, ":cur_troop", slot_troop_love_interest_2, ":cur_lady"),
							(neg|troop_slot_eq, ":cur_troop", slot_troop_love_interest_3, ":cur_lady"),
						##diplomacy start+ also allow -1 to signify no-one courted
							(try_begin),
								(this_or_next|troop_slot_eq, ":cur_troop", slot_troop_love_interest_1, -1),#< added
								(troop_slot_eq, ":cur_troop", slot_troop_love_interest_1, 0),
								(troop_set_slot, ":cur_troop", slot_troop_love_interest_1, ":cur_lady"),
							(else_try),
								(this_or_next|troop_slot_eq, ":cur_troop", slot_troop_love_interest_2, -1),#< added
								(troop_slot_eq, ":cur_troop", slot_troop_love_interest_2, 0),
								(troop_set_slot, ":cur_troop", slot_troop_love_interest_2, ":cur_lady"),
							(else_try),
								(this_or_next|troop_slot_eq, ":cur_troop", slot_troop_love_interest_3, -1),#< added
								(troop_slot_eq, ":cur_troop", slot_troop_love_interest_3, 0),
								(troop_set_slot, ":cur_troop", slot_troop_love_interest_3, ":cur_lady"),
							(try_end),
						(try_end),
							(try_end),
						(assign, reg1, ":save_reg1"),
						(assign, reg0, ":save_reg0"),#revert register
						##diplomacy end+
						]),
                    
                    ("faction_conclude_feast",
                      [
                        (store_script_param, ":faction_no", 1),
                        (store_script_param, ":venue", 2),
                        
                        (str_store_faction_name, s3, ":faction_no"),
                        (str_store_party_name, s4, ":venue"),
                        
                        (try_begin),
                          (eq, "$cheat_mode", 1),
                          (display_message, "str_s3_feast_concludes_at_s4"),
                        (try_end),
                        
                        (try_begin),
                          (eq, ":faction_no", "fac_player_faction"),
                          (assign, ":faction_no", "$players_kingdom"),
                        (try_end),
                        
                        (party_set_slot, ":venue", slot_town_has_tournament, 0),
                        
                        #markspot
                        
                        (assign, ":nobility_in_faction", 0),
                        (assign, ":nobility_in_attendance", 0),
                        
                        (try_for_range, ":troop_no", active_npcs_begin, kingdom_ladies_end),
                          (store_faction_of_troop, ":troop_faction", ":troop_no"),
                          (eq, ":faction_no", ":troop_faction"),
                          
                          (val_add, ":nobility_in_faction", 1),
                          
                          #CHECK -- is the troop there?
                          (troop_slot_eq, ":troop_no", slot_troop_cur_center, ":venue"),
                          (val_add, ":nobility_in_attendance", 1),
                          
						#check for marriages
						##diplomacy start+ enable marriages for non-kingdom ladies (for example, between two companions)
						(this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_robber_knight),
						(this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
						(this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_seneschal),
						(this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_player_companion),
						##diplomacy end+
						(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_lady),
						(troop_get_slot, ":groom", ":troop_no", slot_troop_betrothed),
						(gt, ":groom", 0),
                          
                          (troop_get_slot, ":groom_party", ":groom", slot_troop_leaded_party),
                          (party_is_active, ":groom_party"),
                          (party_get_attached_to, ":groom_party_attached", ":groom_party"),
                          (eq, ":groom_party_attached", ":venue"),
                          
                          (store_faction_of_troop, ":lady_faction", ":troop_no"),
                          (store_faction_of_troop, ":groom_faction", ":groom"),
                          
                          (eq, ":groom_faction", ":lady_faction"),
                          (eq, ":lady_faction", ":faction_no"),
                          (store_current_hours, ":hours_since_betrothal"),
                          (troop_get_slot, ":betrothal_time", ":troop_no", slot_troop_betrothal_time),
                          (val_sub, ":hours_since_betrothal", ":betrothal_time"),
                          (ge, ":hours_since_betrothal", 144), #6 days, should perhaps eventually be 29 days, or 696 yours
                          
						(call_script, "script_get_kingdom_lady_social_determinants", ":troop_no"),
						(assign, ":wedding_venue", reg1),
						##diplomacy start+ be less picky about where to hold the feast as time goes on
						#(eq, ":venue", ":wedding_venue"),
						(neq, ":troop_no", "trp_player"),
						(neq, ":groom", "trp_player"),
						(party_get_slot, ":town_lord", ":venue", slot_town_lord),
						(assign, ":hold_the_wedding", 0),
						(try_begin),
							#after 6 days, will be held if the venue is the ideal one
							(eq, ":venue", ":wedding_venue"),                    
							(assign, ":hold_the_wedding", 1),
						(else_try),
							#after 6 days, will be held if the bride's father/guardian holds a feast
							(ge, ":town_lord", 0),
							(this_or_next|troop_slot_eq, ":troop_no", slot_troop_father, ":town_lord"),
							(this_or_next|troop_slot_eq, ":troop_no", slot_troop_mother, ":town_lord"),
							   (troop_slot_eq, ":troop_no", slot_troop_guardian, ":town_lord"),
							(assign, ":hold_the_wedding", 1),
						(else_try),
							#after 20 days, will be held if the bride, the groom, or either of their
							#parents hold a feast
							(ge, ":hours_since_betrothal", 24 * 20),
							(ge, ":town_lord", 0),
							(this_or_next|eq, ":troop_no", ":town_lord"),
							(this_or_next|eq, ":groom", ":town_lord"),
							(this_or_next|troop_slot_eq, ":groom", slot_troop_father, ":town_lord"),
							   (troop_slot_eq, ":groom", slot_troop_mother, ":town_lord"),
							(assign, ":hold_the_wedding", 1),
						(else_try),
							#after 60 days, if against all odds the engagement hasn't been called off,
							#the faction leader qualifies, as does any relative
							(ge, ":hours_since_betrothal", 24 * 60),
							(ge, ":town_lord", 0),
							#(call_script, "script_troop_get_family_relation_to_troop", ":town_lord", ":troop_no"),
							(call_script, "script_dplmc_troop_get_family_relation_to_troop",  ":town_lord", ":troop_no"),
							(assign, ":bride_relation", reg0),
							#(call_script, "script_troop_get_family_relation_to_troop", ":town_lord", ":groom"),
							(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":town_lord", ":groom"),
							(this_or_next|faction_slot_eq, ":troop_faction", slot_faction_leader, ":town_lord"),
							(this_or_next|ge, reg0, 1),
								(ge, ":bride_relation", 1),
							(assign, ":hold_the_wedding", 1),
						(try_end),
						(eq, ":hold_the_wedding", 1),
						##diplomacy end+
						(call_script, "script_courtship_event_bride_marry_groom", ":troop_no", ":groom", 0), #parameters from dialog
					(try_end),
                        
                        
                        #ssss	(assign, ":placeholder_reminder_to_calculate_effect_for_player_feast", 1),
                        
                        
                        
                        (party_get_slot, ":feast_host", ":venue", slot_town_lord),
                        (assign, ":quality_of_feast", 0),
                        
                        (try_begin),
                          (check_quest_active, "qst_organize_feast"),
                          (quest_slot_eq, "qst_organize_feast", slot_quest_target_center, ":venue"),
                          (assign, ":feast_host", "trp_player"),
                          
                          (assign, ":total_guests", 400),
                          
                          (call_script, "script_succeed_quest", "qst_organize_feast"),
                          (call_script, "script_end_quest", "qst_organize_feast"),
                          
                          (call_script, "script_internal_politics_rate_feast_to_s9", "trp_household_possessions", ":total_guests", "$players_kingdom", 1),
                          (assign, ":quality_of_feast", reg0),
                        (else_try),
                          (assign, ":quality_of_feast", 60),
                        (try_end),
                        
                        
                        (try_begin),
                          (ge, "$cheat_mode", 1),
                          (str_store_troop_name, s4, ":feast_host"),
                          (assign, reg4, ":quality_of_feast"),
                          (display_message, "@{!}DEBUG - {s4}'s feast has rating of {reg4}"),
                        (try_end),
                        
                        
                        (try_begin),
                          (ge, ":feast_host", 0),
                          (store_div, ":renown_boost", ":quality_of_feast", 3),
                          (call_script, "script_change_troop_renown", ":feast_host", ":renown_boost"),
                          
                          (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
                            (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
                            (troop_get_slot, ":leaded_party", ":troop_no", slot_troop_leaded_party),
                            (party_is_active, ":leaded_party"),
                            (party_get_attached_to, ":leaded_party_attached", ":leaded_party"),
                            (eq, ":leaded_party_attached", ":venue"),
                            
                            (assign, ":relation_booster", ":quality_of_feast"),
                            (val_div, ":relation_booster", 20),
                            
                            (try_begin),
                              (eq, ":feast_host", "trp_player"),
                              (val_sub, ":relation_booster", 1),
                              (val_max, ":relation_booster", 0),
                            (try_end),
                            (call_script, "script_troop_change_relation_with_troop", ":feast_host", ":troop_no", ":relation_booster"),
                            (val_add, "$total_feast_changes", ":relation_booster"),
                          (try_end),
                        (try_end),
                        
                        
                        (assign, reg3, ":nobility_in_attendance"),
                        (assign, reg4, ":nobility_in_faction"),
                        
                        (try_begin),
                          (eq, "$cheat_mode", 1),
                          (display_message, "str_attendance_reg3_nobles_out_of_reg4"),
                        (try_end),
                    ]),
                    
                    ("lady_evaluate_troop_as_suitor",
                      [
                        (store_script_param, ":lady", 1),
                        (store_script_param, ":suitor", 2),
                        
                        (call_script, "script_troop_get_romantic_chemistry_with_troop", ":lady", ":suitor"),
                        (assign, ":romantic_chemistry", reg0),
                        
                        (try_begin),
                          (call_script, "script_cf_test_lord_incompatibility_to_s17", ":lady", ":suitor"),
                        (try_end),
                        
                        (store_sub, ":personality_modifier", 0, reg0),
                        (assign, reg2, ":personality_modifier"),
                        
                        (try_begin),
                          (troop_get_slot, ":renown_modifier", ":suitor", slot_troop_renown),
                          (val_div, ":renown_modifier", 20),
                          (try_begin),
                            (this_or_next|troop_slot_eq, ":lady", slot_lord_reputation_type, lrep_conventional),
                            (troop_slot_eq, ":lady", slot_lord_reputation_type, lrep_ambitious),
                            (val_mul, ":renown_modifier", 2),
                            (val_sub, ":renown_modifier", 15),
                          (try_end),
                        (try_end),
                        
                        (store_add, ":final_score", ":renown_modifier", ":personality_modifier"),
                        (val_add, ":final_score", ":romantic_chemistry"),
                        (assign, reg0, ":final_score"),
                    ]),
                    
                    ("courtship_event_troop_court_lady",
                      [
                        (store_script_param, ":suitor", 1),
                        (store_script_param, ":lady", 2),
                        
                        
                        #(try_begin),
                        #(eq, "$cheat_mode", 1),
                        #(str_store_troop_name, s4, ":suitor"),
                        #(str_store_troop_name, s5, ":lady"),
                        #(troop_get_slot, ":lady_location", ":lady", slot_troop_cur_center),
                        #(str_store_party_name, s7, ":lady_location"),
                        #(display_message, "str_s4_pursues_suit_with_s5_in_s7"),
                        #(try_end),
                        
                        (troop_get_slot, ":previous_suitor", ":lady", slot_lady_last_suitor),
                        (troop_set_slot, ":lady", slot_lady_last_suitor, ":suitor"), #can determine quarrels
                        
                        (try_begin),
                          (eq, ":previous_suitor", "trp_player"),
                          
                          (troop_slot_ge, ":lady", slot_troop_met, 2),
                          (call_script, "script_troop_get_relation_with_troop", ":suitor", "trp_player"), #add this to list of quarrels
                          (assign, ":suitor_relation_w_player", reg0),
                          
                          (try_begin),
                            (this_or_next|troop_slot_eq, ":suitor", slot_lord_reputation_type, lrep_selfrighteous),
                            (this_or_next|troop_slot_eq, ":suitor", slot_lord_reputation_type, lrep_quarrelsome),
                            (troop_slot_eq, ":suitor", slot_lord_reputation_type, lrep_debauched),
                            (gt, ":suitor_relation_w_player", -20),
                            (call_script, "script_add_log_entry", logent_lords_quarrel_over_woman, ":suitor", "trp_player", ":lady", 0),
                          (else_try),
                            (is_between, ":suitor_relation_w_player", -5, -25),
                            (call_script, "script_add_log_entry", logent_lords_quarrel_over_woman, ":suitor", "trp_player", ":lady", 0),
                          (try_end),
                        (else_try),
                          (neq, ":previous_suitor", "trp_player"), #not the player
                          
                          (neq, ":suitor", ":previous_suitor"),
                          (ge, ":previous_suitor", active_npcs_begin),
                          
                          (call_script, "script_cf_test_lord_incompatibility_to_s17", ":suitor", ":previous_suitor"),
                          (call_script, "script_add_log_entry", logent_lords_quarrel_over_woman, ":suitor", ":previous_suitor", ":lady", 0),
                          
                          (call_script, "script_troop_get_relation_with_troop", ":suitor", ":previous_suitor"), #add this to list of quarrels
                          (ge, reg0, 0),
                          (call_script, "script_troop_change_relation_with_troop", ":suitor", ":previous_suitor", -20),
                          (val_add, "$total_courtship_quarrel_changes", -20),
                        (else_try),	 #quarrelsome lords quarrel anyway
                          (troop_slot_eq, ":suitor", slot_lord_reputation_type, lrep_quarrelsome),
                          (neq, ":suitor", ":previous_suitor"),
                          (ge, ":previous_suitor", active_npcs_begin),
                          
                          #		(neq, ":previous_suitor", "trp_player"),
                          
                          (call_script, "script_troop_get_relation_with_troop", ":suitor", ":previous_suitor"), #add this to list of quarrels
                          (lt, reg0, 10),
                          (call_script, "script_add_log_entry", logent_lords_quarrel_over_woman, ":suitor", ":previous_suitor", ":lady", 0),
                          (ge, reg0, 0),
                          (call_script, "script_troop_change_relation_with_troop", ":suitor", ":previous_suitor", -20),
                          (val_add, "$total_courtship_quarrel_changes", -20),
                          
                        (try_end),
                        
                        
                        #	(call_script, "script_troop_get_relation_with_troop", ":lady", ":suitor"),
                        #	(assign, ":orig_relation", reg0),
                        
                        (call_script, "script_lady_evaluate_troop_as_suitor", ":lady", ":suitor"),
                        
                        (store_random_in_range, ":random", 5, 16),
                        (store_div, ":relationship_change", reg0, ":random"),
                        
                        (call_script, "script_troop_get_relation_with_troop", ":lady", ":suitor"),
                        (assign, ":orig_relation", reg0),
                        
                        (call_script, "script_troop_change_relation_with_troop", ":lady", ":suitor", ":relationship_change"),
                        
                        (call_script, "script_troop_get_relation_with_troop", ":lady", ":suitor"),
                        (assign, ":lady_suitor_relation", reg0),
                        
                        (try_begin),
                          (ge, ":lady_suitor_relation", 10),
                          (lt, ":orig_relation", 10),
                          (call_script, "script_add_log_entry", logent_lady_favors_suitor, ":lady", 0, ":suitor", 0),
                          
                          (try_begin),
                            (eq, "$cheat_mode", 1),
                            (display_message, "str_note__favor_event_logged"),
                          (try_end),
                          
                        (else_try),
                          (this_or_next|lt, ":lady_suitor_relation", -20),
                          (ge, ":lady_suitor_relation", 20),
                          
                          (call_script, "script_get_kingdom_lady_social_determinants", ":lady"),
                          (assign, ":guardian", reg0),
                          (call_script, "script_troop_get_relation_with_troop", ":suitor", ":guardian"),
                          (assign, ":suitor_guardian_relation", reg0),
                          #things come to a head, one way or another
                          
                          (assign, ":highest_competitor_lady_score", -1),
                          (assign, ":competitor_preferred_by_lady", -1),
                          
                          (assign, ":highest_competitor_guardian_score", ":suitor_guardian_relation"),
                          (assign, ":competitor_preferred_by_guardian", -1),
                          
                          #log potential competitors
                          (try_for_range, ":possible_competitor", lords_begin, lords_end),
                            (neq, ":possible_competitor", ":suitor"),
                            
                            (this_or_next|troop_slot_eq, ":possible_competitor", slot_troop_love_interest_1, ":lady"),
                            (this_or_next|troop_slot_eq, ":possible_competitor", slot_troop_love_interest_2, ":lady"),
                            (troop_slot_eq, ":possible_competitor", slot_troop_love_interest_3, ":lady"),
                            
                            (try_begin),
                              (call_script, "script_troop_get_relation_with_troop", ":possible_competitor", ":lady"),
                              (gt, reg0, ":highest_competitor_lady_score"),
                              (assign, ":competitor_preferred_by_lady", ":possible_competitor"),
                              (assign, ":highest_competitor_lady_score", reg0),
                            (try_end),
                            
                            (try_begin),
                              (call_script, "script_troop_get_relation_with_troop", ":possible_competitor", ":guardian"),
                              (gt, reg0, ":highest_competitor_guardian_score"),
                              (assign, ":competitor_preferred_by_guardian", ":possible_competitor"),
                              (assign, ":highest_competitor_guardian_score", reg0),
                            (try_end),
                          (try_end),
                          
                          #RESULTS
                          #Guardian forces lady to be betrothed to suitor now
                          (try_begin),
                            (lt, ":lady_suitor_relation", -20),
                            (this_or_next|troop_slot_eq, ":guardian", slot_lord_reputation_type, lrep_selfrighteous),
                            (this_or_next|troop_slot_eq, ":guardian", slot_lord_reputation_type, lrep_debauched),
                            (troop_slot_eq, ":guardian", slot_lord_reputation_type, lrep_quarrelsome),
                            (eq, ":competitor_preferred_by_guardian", -1),
                            
                            (this_or_next|troop_slot_eq, ":suitor", slot_lord_reputation_type, lrep_selfrighteous),
                            (this_or_next|troop_slot_eq, ":suitor", slot_lord_reputation_type, lrep_debauched),
                            (troop_slot_eq, ":suitor", slot_lord_reputation_type, lrep_quarrelsome),
                            
                            (troop_slot_eq, ":suitor", slot_troop_betrothed, -1),
                            (troop_slot_eq, ":lady", slot_troop_betrothed, -1),
                            
                            (call_script, "script_add_log_entry", logent_lady_betrothed_to_suitor_by_family, ":lady", 0, ":suitor", 0),
                            (troop_set_slot, ":suitor", slot_troop_betrothed, ":lady"),
                            (troop_set_slot, ":lady", slot_troop_betrothed, ":suitor"),
                            (store_current_hours, ":hours"),
                            (troop_set_slot, ":lady", slot_troop_betrothal_time, ":hours"),
                            (troop_set_slot, ":suitor", slot_troop_betrothal_time, ":hours"),
                            (try_begin),
                              (eq, "$cheat_mode", 1),
                              (display_message, "str_result_lady_forced_to_agree_to_engagement"),
                            (try_end),
                            
                            #Lady rejects the suitor
                          (else_try),
                            (lt, ":lady_suitor_relation", -20),
                            
                            (call_script, "script_add_log_entry", logent_lady_rejects_suitor, ":lady", 0, ":suitor", 0),
                            (call_script, "script_courtship_event_lady_break_relation_with_suitor", ":lady", ":suitor"),
                            (try_begin),
                              (eq, "$cheat_mode", 1),
                              (display_message, "str_result_lady_rejects_suitor"),
                            (try_end),
                            
                            #A happy engagement, with parental blessing
                          (else_try),
                            (gt, ":lady_suitor_relation", 20),
                            (gt, ":suitor_guardian_relation", 0),
                            (eq, ":competitor_preferred_by_lady", -1),
                            
                            (troop_slot_eq, ":suitor", slot_troop_betrothed, -1),
                            (troop_slot_eq, ":lady", slot_troop_betrothed, -1),
                            
                            (call_script, "script_add_log_entry", logent_lady_betrothed_to_suitor_by_choice, ":lady", 0, ":suitor", 0),
                            (troop_set_slot, ":suitor", slot_troop_betrothed, ":lady"),
                            (troop_set_slot, ":lady", slot_troop_betrothed, ":suitor"),
                            (store_current_hours, ":hours"),
                            (troop_set_slot, ":lady", slot_troop_betrothal_time, ":hours"),
                            (troop_set_slot, ":suitor", slot_troop_betrothal_time, ":hours"),
                            
                            (try_begin),
                              (eq, "$cheat_mode", 1),
                              (str_store_troop_name, s4, ":lady"),
                              (str_store_troop_name, s5, ":suitor"),
                              (display_message, "str_result_happy_engagement_between_s4_and_s5"),
                            (try_end),
                            
                            #Lady elopes
                          (else_try),
                            (gt, ":lady_suitor_relation", 20),
                            
							(eq, ":competitor_preferred_by_lady", -1),
							##diplomacy start+
							##Fix Native bug, the following line should be checking ":lady", not ":guardian"
							##OLD:
							#(this_or_next|troop_slot_eq, ":guardian", slot_lord_reputation_type, lrep_adventurous),
							#	(troop_slot_eq, ":guardian", slot_lord_reputation_type, lrep_ambitious),
							##NEW:
							(this_or_next|troop_slot_eq, ":lady", slot_lord_reputation_type, lrep_adventurous),
								(troop_slot_eq, ":lady", slot_lord_reputation_type, lrep_ambitious),
							##diplomacy end+
                            
                            (troop_slot_eq, ":suitor", slot_troop_betrothed, -1),
                            (troop_slot_eq, ":lady", slot_troop_betrothed, -1),
                            
                            #lady elopes
                            (call_script, "script_courtship_event_bride_marry_groom", ":lady", ":suitor", 1),
                            #add elopements to quarrel descriptions
                            
                            (try_begin),
                              (eq, "$cheat_mode", 1),
                              (str_store_troop_name, s4, ":lady"),
                              (str_store_troop_name, s5, ":suitor"),
                              (display_message, "str_result_s4_elopes_with_s5"),
                            (try_end),
                            
                            #Lady reluctantly agrees to marry under pressure from family
                          (else_try),
                            (troop_slot_eq, ":lady", slot_lord_reputation_type, lrep_conventional),
                            (eq, ":competitor_preferred_by_guardian", -1),
                            (gt, ":suitor_guardian_relation", 4),
                            
                            (store_random_in_range, ":random", 0, 5),
                            (eq, ":random", 0),
                            
                            (troop_slot_eq, ":suitor", slot_troop_betrothed, -1),
                            (troop_slot_eq, ":lady", slot_troop_betrothed, -1),
                            
                            (call_script, "script_add_log_entry", logent_lady_betrothed_to_suitor_by_pressure, ":lady", 0, ":suitor", 0),
                            (troop_set_slot, ":suitor", slot_troop_betrothed, ":lady"),
                            (troop_set_slot, ":lady", slot_troop_betrothed, ":suitor"),
                            (store_current_hours, ":hours"),
                            (troop_set_slot, ":lady", slot_troop_betrothal_time, ":hours"),
                            (troop_set_slot, ":suitor", slot_troop_betrothal_time, ":hours"),
                            (try_begin),
                              (eq, "$cheat_mode", 1),
                              (str_store_troop_name, s4, ":lady"),
                              (str_store_troop_name, s5, ":suitor"),
                              (display_message, "str_result_s4_reluctantly_agrees_to_engagement_with_s5"),
                            (try_end),
                            
                            #Stalemate -- make patience roll
                          (else_try),
                            (gt, ":lady_suitor_relation", 20),
                            
                            (store_random_in_range, reg3, 0, 3),
                            (try_begin),
                              (eq, "$cheat_mode", 1),
                              (display_message, "str_result_stalemate_patience_roll_=_reg3"),
                            (try_end),
                            
                            (eq, reg3, 0),
                            (call_script, "script_add_log_entry", logent_lady_rejected_by_suitor, ":lady", 0, ":suitor", 0),
                            (call_script, "script_courtship_event_lady_break_relation_with_suitor", ":lady", ":suitor"),
                          (try_end),
                          
                        (try_end),
                        
                    ]),
                    
                    
                    
                    ("courtship_event_lady_break_relation_with_suitor", #parameters from dialog
                      [
                        (store_script_param, ":lady", 1),
                        (store_script_param, ":suitor", 2),
                        
						(try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
							(troop_slot_eq, ":suitor", ":love_interest_slot", ":lady"),
							##diplomacy start+ set to -1 instead, since 0 is the player (how annoying)
							#(troop_set_slot, ":suitor", ":love_interest_slot", 0),
							(troop_set_slot, ":suitor", ":love_interest_slot", -1),
							##diplomacy end+
						(try_end),
						(call_script, "script_assign_troop_love_interests", ":suitor"),

						(try_begin),
							(troop_slot_eq, ":lady", slot_troop_betrothed, ":suitor"),


							(troop_set_slot, ":lady", slot_troop_betrothed, -1),
						##diplomacy start+ perform the same check for the suitor that was done,
						#for the lady, so this script has no unfortunate consequences even if
						#called inappropriately.
						(try_end),
						(try_begin),
							(troop_slot_eq, ":suitor", slot_troop_betrothed, ":lady"),
							(troop_set_slot, ":suitor", slot_troop_betrothed, -1),
						##diplomacy end+
						(try_end),


					]),
                    
                    
                    ("courtship_event_bride_marry_groom", #parameters from dialog or scripts
                      [
                        (store_script_param, ":bride", 1),
                        (store_script_param, ":groom", 2),
                        (store_script_param, ":elopement", 3),
                        
						(try_begin),
							(eq, ":bride", "trp_player"),
							(assign, ":venue", "$g_encountered_party"),
						(else_try),
							(troop_get_slot, ":venue", ":bride", slot_troop_cur_center),
							##diplomacy start+
							#Ensure there is a venue.
							(lt, ":venue", 1),
							(troop_get_slot, ":venue", ":groom", slot_troop_cur_center),
							##diplomacy end+
						(try_end),

						(store_faction_of_troop, ":groom_faction", ":groom"),


						(try_begin),
							(eq, ":elopement", 0),
							(call_script, "script_add_log_entry", logent_lady_marries_suitor, ":bride", ":venue", ":groom", 0),
						(else_try),
							(call_script, "script_add_log_entry", logent_lady_elopes_with_lord, ":bride", ":venue", ":groom", 0),
						(try_end),

						(str_store_troop_name, s3, ":bride"),
						(str_store_troop_name, s4, ":groom"),
						(str_store_party_name, s5, ":venue"),

						(try_begin),
						##diplomacy start+ this should be globally-visible for notable personages
						#    (this_or_next|is_between, ":groom_faction", kingdoms_begin, kingdoms_end),
						#    (this_or_next|troop_slot_ge, ":groom", slot_troop_met, 1),
						#    (troop_slot_ge, ":bride", slot_troop_met, 1),
							(display_log_message, "str_s3_marries_s4_at_s5"),
						#(else_try),
						#    (eq, "$cheat_mode", 1),
						#    (display_message, "str_s3_marries_s4_at_s5"),
						##diplomacy end+
						(try_end),

						(troop_set_slot, ":bride", slot_troop_spouse, ":groom"),
						(troop_set_slot, ":groom", slot_troop_spouse, ":bride"),

						#Break groom's romantic relations
						(try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
							(troop_set_slot, ":groom", ":love_interest_slot", 0),
						(try_end),

						#Break bride's romantic relations
						(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
							(try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
								(troop_slot_eq, ":active_npc", ":love_interest_slot", ":bride"),
								(call_script, "script_courtship_event_lady_break_relation_with_suitor", ":bride", ":active_npc"),
							(try_end),
						(try_end),



						(troop_set_slot, ":bride", slot_troop_betrothed, -1),
						(troop_set_slot, ":groom", slot_troop_betrothed, -1),



						#change relations with family
						##diplomacy start+ Include kingdom ladies
						#(try_for_range, ":family_member", lords_begin, lords_end),
						(try_for_range, ":family_member", heroes_begin, heroes_end),
							(neq, ":family_member", ":bride"),
							(neq, ":family_member", ":groom"),
						##diplomacy end+
							(call_script, "script_troop_get_family_relation_to_troop", ":bride", ":family_member"),
							(gt, reg0, 0),
							(store_div, ":family_relation_boost", reg0, 3),
							(try_begin),
								(eq, ":elopement", 1),
								(val_mul, ":family_relation_boost", -2),
							(try_end),
							##diplomacy start+ Fix error!  Change relation between groom and family member, not groom and bride.
							#(call_script, "script_troop_change_relation_with_troop", ":groom", ":bride", ":family_relation_boost"),
							(call_script, "script_troop_change_relation_with_troop", ":groom", ":family_member", ":family_relation_boost"),
							##diplomacy end+
							(val_add, "$total_courtship_quarrel_changes", ":family_relation_boost"),
						(try_end),

						(try_begin),
							(this_or_next|eq, ":groom", "trp_player"),
								(eq, ":bride", "trp_player"),
							##diplomacy start+ fix bug where player didn't get right to rule
							(call_script, "script_change_player_right_to_rule", 15),##one argument, not two
							##diplomacy end+
						(try_end),


						(try_begin),
							(eq, ":groom", "trp_player"),
							(check_quest_active, "qst_wed_betrothed"),
							(call_script, "script_succeed_quest", "qst_wed_betrothed"),
							(call_script, "script_end_quest", "qst_wed_betrothed"),
						(try_end),


						(try_begin),
							(check_quest_active, "qst_visit_lady"),
							(quest_slot_eq, "qst_visit_lady", slot_quest_giver_troop, ":bride"),
							(call_script, "script_abort_quest", "qst_visit_lady", 0),
						(try_end),


						(try_begin),
							(eq, ":groom", "trp_player"),
							(check_quest_active, "qst_visit_lady"),
							(call_script, "script_abort_quest", "qst_visit_lady", 0),
						(try_end),
						(try_begin),
							(eq, ":groom", "trp_player"),
							(check_quest_active, "qst_duel_courtship_rival"),
							(call_script, "script_abort_quest", "qst_duel_courtship_rival", 0),
						(try_end),
                        
                        
                        (try_begin),
                          (eq, ":bride", "trp_player"),
                          (call_script, "script_player_join_faction", ":groom_faction"),
                          (assign, "$player_has_homage", 1),
                        (else_try),
                          (eq, ":groom", "trp_player"),
                          ## Begin 1.134
                          (try_begin),
                            (ge, "$cheat_mode", 1),
                            (str_store_troop_name, s4, ":bride"),
                            (display_message, "@{!} DEBUG - {s4} faction change in marriage case 5"),
                          (try_end),
                          ## End 1.134
                          (troop_set_faction, ":bride", "$players_kingdom"),
                          #LAZERAS MODIFIED  {ENTK}
                          # Jrider + TITLES v0.0 change title of bride, according to player faction
                          (call_script, "script_troop_set_title_according_to_faction", ":bride", "$players_kingdom"),
                          # Jrider -
                          #LAZERAS MODIFIED  {ENTK}
                        (else_try),
                          ## Begin 1.134
                          (try_begin),
                            (ge, "$cheat_mode", 1),
                            (str_store_troop_name, s4, ":bride"),
                            (display_message, "@{!}DEBUG - {s4} faction changed by marriage, case 6"),
                          (try_end),
                          ## End 1.134
                          (troop_set_faction, ":bride", ":groom_faction"),
                          #LAZERAS MODIFIED  {ENTK}
                          # Jrider + TITLES v0.0 change title of groom and bride, according to player faction
                          (call_script, "script_troop_set_title_according_to_faction", ":groom", ":groom_faction"),
                          (call_script, "script_troop_set_title_according_to_faction", ":bride", ":groom_faction"),
                          # Jrider -
                          #LAZERAS MODIFIED  {ENTK}
                        (try_end),
                        
                        (try_begin),
                          (this_or_next|eq, ":groom", "trp_player"),
                          (eq, ":bride", "trp_player"),
                          (unlock_achievement, ACHIEVEMENT_HAPPILY_EVER_AFTER),
                          (try_begin),
                            (eq, ":elopement", 1),
                            (unlock_achievement, ACHIEVEMENT_HEART_BREAKER),
                          (try_end),
                        (try_end),
                        
                        
                        
                        (try_begin),
                          (this_or_next|eq, ":groom", "trp_player"),
                          (eq, ":bride", "trp_player"),
                          #(eq, ":elopement", 0),
                          (call_script, "script_start_wedding_cutscene", ":groom", ":bride"),
                        (try_end),
                    ]),
                    
                    
                    #script_npc_decision_checklist_party_ai
                    # DECISION CHECKLISTS (OCT 14)
                    # I was thinking of trying to convert as much AI decision-making as possible to the checklist format
                    # While outcomes are not as nuanced and varied as a random decision using weighted chances for each outcoms,
                    # the checklist has the advantage of being much more transparent, both to developers and to players
                    # The checklist can yield a string (standardized to s14) which explains the rationale for the decision
                    # When the script yields a yes/no/maybe result, than that is standardized from -3 to +3
                    # INPUT: troop_no
                    # OUTPUT: none
                    ("npc_decision_checklist_party_ai",
                      [
                        #this script can replace decide_kingdom_hero_ai and decide_kingdom_hero_ai_follow_or_not
                        #However, it does not contain script_party_set_ai_state
                        
                        (store_script_param, ":troop_no", 1),
                        
                        (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
                        #(party_get_slot, ":our_strength", ":party_no", slot_party_cached_strength),
                        #(store_div, ":min_strength_behind", ":our_strength", 2),
                        #(party_get_slot, ":our_follower_strength", ":party_no", slot_party_follower_strength),
                        
                        (try_begin),
                          (eq, "$cheat_mode", 1),
                          (assign, "$g_talk_troop", ":troop_no"),
                        (try_end),
                        
                        (store_troop_faction, ":faction_no", ":troop_no"),
                        
                        (try_begin),
                          (eq, ":troop_no", "$g_talk_troop"),
                          (str_store_string, s15, "str__i_must_attend_to_this_matter_before_i_worry_about_the_affairs_of_the_realm"),
                        (try_end),
                        
                        #find current center
                        (party_get_attached_to, ":cur_center_no", ":party_no"),
                        (try_begin),
                          (lt, ":cur_center_no", 0),
                          (party_get_cur_town, ":cur_center_no", ":party_no"),
                        (try_end),
                        (assign, ":besieger_party", -1),
                        (try_begin),
                          (neg|is_between, ":cur_center_no", centers_begin, centers_end),
                          (assign, ":cur_center_no", -1),
                        (else_try),
                          (party_get_slot, ":besieger_party", ":cur_center_no", slot_center_is_besieged_by),
                          (try_begin),
                            (neg|party_is_active, ":besieger_party"),
                            (assign, ":besieger_party", -1),
                          (try_end),
                        (try_end),
                        
                        #party_count
                        (call_script, "script_party_count_fit_for_battle", ":party_no"),
                        (assign, ":party_fit_for_battle", reg0),
                        (call_script, "script_party_get_ideal_size", ":party_no"),
                        (assign, ":ideal_size", reg0),
                        (store_mul, ":party_strength_as_percentage_of_ideal", ":party_fit_for_battle", 100),
                        (val_div, ":party_strength_as_percentage_of_ideal", ":ideal_size"),
                        (try_begin),
                          (faction_slot_eq, ":faction_no", slot_faction_num_towns, 0),
                          (faction_slot_eq, ":faction_no", slot_faction_num_castles, 0),
                          (assign, ":party_ratio_of_prisoners", 0), #do not let prisoners have an effect on ai calculation
                        (else_try),
                          (party_get_num_prisoners, ":num_prisoners", ":party_no"),
                          (val_max, ":party_fit_for_battle", 1), #avoid division by zero error
                          (store_div, ":party_ratio_of_prisoners", ":num_prisoners", ":party_fit_for_battle"),
                        (try_end),
                        
                        (assign, ":faction_is_at_war", 0),
                        (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
                          (faction_slot_eq, ":kingdom", slot_faction_state, sfs_active),
                          (store_relation, ":relation", ":faction_no", ":kingdom"),
                          (lt, ":relation", 0),
                          (assign, ":faction_is_at_war", 1),
                        (try_end),
                        
                        (assign, ":operation_in_progress", 0),
                        (try_begin),
                          (this_or_next|party_slot_eq, ":party_no", slot_party_ai_state, spai_raiding_around_center),
                          (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
                          
                          (party_get_slot, ":target_center", ":party_no", slot_party_ai_object),
                          (is_between, ":target_center", centers_begin, centers_end),
                          
                          (store_faction_of_party, ":target_center_faction", ":target_center"),
                          (store_relation, ":relation", ":faction_no", ":target_center_faction"),
                          (lt, ":relation", 0),
                          
                          (store_distance_to_party_from_party, ":distance", ":party_no", ":target_center"),
                          (lt, ":distance", 10),
                          (this_or_next|party_slot_eq, ":target_center", slot_village_state, svs_under_siege),
                          (this_or_next|party_slot_eq, ":target_center", slot_village_state, svs_normal),
                          (party_slot_eq, ":target_center", slot_village_state, svs_being_raided),
                          
                          (assign, ":operation_in_progress", 1),
                        (try_end),
                        
                        (troop_get_slot, ":troop_reputation", ":troop_no", slot_lord_reputation_type),
                        
                        (party_get_slot, ":old_ai_state", ":party_no", slot_party_ai_state),
                        (party_get_slot, ":old_ai_object", ":party_no", slot_party_ai_object),
                        
                        (party_get_slot, ":party_cached_strength", ":party_no", slot_party_cached_strength),
                        
                        (store_current_hours, ":hours_since_last_rest"),
                        (party_get_slot, ":last_rest_time", ":party_no", slot_party_last_in_any_center),
                        (val_sub, ":hours_since_last_rest", ":last_rest_time"),
                        
                        (store_current_hours, ":hours_since_last_home"),
                        (party_get_slot, ":last_home_time", ":party_no", slot_party_last_in_home_center),
                        (val_sub, ":hours_since_last_home", ":last_home_time"),
                        
                        (store_current_hours, ":hours_since_last_combat"),
                        (party_get_slot, ":last_combat_time", ":party_no", slot_party_last_in_combat),
                        (val_sub, ":hours_since_last_combat", ":last_combat_time"),
                        
                        (store_current_hours, ":hours_since_last_courtship"),
                        (party_get_slot, ":last_courtship_time", ":party_no", slot_party_leader_last_courted),
                        (val_sub, ":hours_since_last_courtship", ":last_courtship_time"),
                        
                        (troop_get_slot, ":temp_ai_seed", ":troop_no", slot_troop_temp_decision_seed),
                        (store_mod, ":aggressiveness", ":temp_ai_seed", 73), #To derive the
                        (try_begin),
                          (eq, ":troop_reputation", lrep_martial),
                          (val_add, ":aggressiveness", 27),
                        (else_try),
                          (neq, ":troop_reputation", lrep_debauched),
                          (neq, ":troop_reputation", lrep_quarrelsome),
                          (val_add, ":aggressiveness", 14),
                        (try_end),
                        
                        (try_begin),
                          (gt, ":aggressiveness", ":hours_since_last_combat"),
                          (val_add, ":aggressiveness", ":hours_since_last_combat"),
                          (val_div, ":aggressiveness", 2),
                        (try_end),
                        
                        (try_begin),
                          (eq, "$cheat_mode", 1), #100
                          (eq, ":troop_no", "$g_talk_troop"),
                          (str_store_troop_name, s4, ":troop_no"),
                          (assign, reg3, ":hours_since_last_rest"),
                          (assign, reg4, ":hours_since_last_courtship"),
                          (assign, reg5, ":hours_since_last_combat"),
                          (assign, reg6, ":hours_since_last_home"),
                          (assign, reg7, ":aggressiveness"),
                          #(display_message, "@{!}{s4}: hours since rest {reg3}, courtship {reg4}, combat {reg5}, home {reg6}, aggressiveness {reg7}"),
                        (try_end),
                        
                        ##I am inspecting an estate (use slot_center_npc_volunteer_troop_amount)
                        
                        (str_store_string, s17, "str_the_other_matter_took_precedence"),
                        
                        (assign, ":do_only_collecting_rents", 0),
                        
                        #Wait in current city (dangerous to travel with less (<=10) men)
                        (try_begin),
                          #NOTE : I added also this condition to very top of list. Because if this condition does not exists in top then a bug happens.
                          #Bug is about alone wounded lords without any troop near him travels between cities, sometimes it want to return his home city
                          #to collect reinforcements, sometimes it want to patrol ext, but his party is so weak even without anyone. So we sometimes see
                          #(0/1) parties in map with only one wounded lord inside. Because after wars completely defeated lords spawn again in a walled center
                          #in 48 hours periods (by codes in module_simple_trigers). He spawns with only wounded himself. Then he should wait in there for
                          #a time to collect new men to his (0/1) party. If a lord is the only one in his party and if he is at any walled center already then he
                          #should stay where he is. He should not travel to anywhere because of any reason. If he is the only one and he is wounded and
                          #he is not in any walled center this means this situation happens because of one another bug, because any lord cannot be out of
                          #walled centers with wounded himself only. So I am adding this condition below.
                          
                          #SUMMARY : If lord has not got enought troops (<10 || <10%) with himself and he is currently at a walled center he should not leave
                          #his current center because of any reason.
                          
                          (ge, ":cur_center_no", 0),
                          
                          (this_or_next|le, ":party_fit_for_battle", 10),
                          (le, ":party_strength_as_percentage_of_ideal", 30),
                          
                          (assign, ":action", spai_holding_center),
                          (assign, ":object", ":cur_center_no"),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_i_need_to_raise_some_men_before_attempting_anything_else"),
                            (str_store_string, s16, "str_i_need_to_raise_some_men_before_attempting_anything_else"),
                          (try_end),
                          
                          #Stand in a siege
                        (else_try),
                          (gt, ":besieger_party", -1),
                          
                          (assign, ":action", spai_holding_center),
                          (assign, ":object", ":cur_center_no"),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_i_cannot_leave_this_fortress_now_as_it_is_under_siege"),
                            (str_store_string, s16, "str_after_all_we_are_under_siege"),
                          (try_end),
                          
                          #Continue retreat to walled center
                        (else_try),
                          (eq, ":old_ai_state", spai_retreating_to_center),
                          (neg|party_is_in_any_town, ":party_no"),
                          
                          (ge, ":old_ai_object", 0),
                          (party_is_active, ":old_ai_object"),
                          
                          (store_faction_of_party, ":retreat_center_faction", ":old_ai_object"),
                          (eq, ":faction_no", ":retreat_center_faction"),
                          
                          (assign, ":action", spai_retreating_to_center),
                          (assign, ":object", ":old_ai_object"),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_we_are_not_strong_enough_to_face_the_enemy_out_in_the_open"),
                            (str_store_string, s16, "str_i_should_probably_seek_shelter_behind_some_stout_walls"),
                          (try_end),
                          
                          #Stand by in current center against enemies
                        (else_try),
                          (is_between, ":cur_center_no", walled_centers_begin, walled_centers_end),
                          
                          (party_get_slot, ":enemy_strength_in_area", ":cur_center_no", slot_center_sortie_enemy_strength), ##1.132, new line
                          (party_get_slot, ":enemy_strength_in_area", ":cur_center_no", slot_center_sortie_enemy_strength),
                          (ge, ":enemy_strength_in_area", 50),
                          
                          (assign, ":action", spai_holding_center),
                          (assign, ":object", ":cur_center_no"),
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_enemies_are_reported_to_be_nearby_and_we_should_stand_ready_to_either_man_the_walls_or_sortie_out_to_do_battle"),
                            (str_store_string, s16, "str_the_enemy_is_nearby"),
                          (try_end),
                          
                          #As the marshall, lead faction campaign
                        (else_try),
                          (faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
                          (str_clear, s15), #Does not say that overrides faction orders
                          (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_gathering_army),
                          
                          (party_set_ai_initiative, ":party_no", 10),
                          
                          #new ozan added - active gathering
                          #this code will allow marshal to travel around cities while gathering army if currently collected are less than 60%.
                          #By ratio increases travel distances become less. Travels will be only points around walled centers.
                          (party_get_slot, ":old_ai_object", ":party_no", slot_party_ai_object),
                          (assign, ":travel_target", ":old_ai_object"),
                          
                          (call_script, "script_find_center_to_defend", ":troop_no"),
                          (assign, ":most_threatened_center", reg0),
                          (assign, ":travel_target_new_assigned", 0),
                          
                          (try_begin),
                            (lt, ":old_ai_object", 0),
                            
                            (store_random_in_range, ":random_value", 0, 8), #to eanble marshal to wait sometime during active gathering
                            (this_or_next|eq, "$g_gathering_new_started", 1),
                            (eq, ":random_value", 0),
                            
                            (assign, ":vassals_already_assembled", 0),
                            (assign, ":total_vassals", 0),
                            (try_for_range, ":lord", active_npcs_begin, active_npcs_end),
                              (store_faction_of_troop, ":lord_faction", ":lord"),
                              (eq, ":lord_faction", ":faction_no"),
                              (troop_get_slot, ":led_party", ":lord", slot_troop_leaded_party),
                              (party_is_active, ":led_party"),
                              (val_add, ":total_vassals", 1),
                              
                              (party_slot_eq, ":led_party", slot_party_ai_state, spai_accompanying_army),
                              (party_slot_eq, ":led_party", slot_party_ai_object, ":party_no"),
                              
                              (party_is_active, ":party_no"),
                              (store_distance_to_party_from_party, ":distance_to_marshal", ":led_party", ":party_no"),
                              (lt, ":distance_to_marshal", 15),
                              (val_add, ":vassals_already_assembled", 1),
                            (try_end),
                            
                            (assign, ":ratio_of_vassals_assembled", -1),
                            (try_begin),
                              (gt, ":total_vassals", 0),
                              (store_mul, ":ratio_of_vassals_assembled", ":vassals_already_assembled", 100),
                              (val_div, ":ratio_of_vassals_assembled", ":total_vassals"),
                            (try_end),
                            
                            (try_begin),
                              #if more than 35% of vassals already collected do not make any more active gathering, just hold and wait last vassals to participate.
                              (le, ":ratio_of_vassals_assembled", 35),
                              
                              (assign, ":best_center_to_travel", ":most_threatened_center"),
                              
                              (try_begin),
                                (eq, "$g_gathering_new_started", 1),
                                
                                (assign, ":minimum_distance", 100000),
                                (try_for_range, ":center_no", centers_begin, centers_end),
                                  (store_faction_of_party, ":center_faction", ":center_no"),
                                  (eq, ":center_faction", ":faction_no"),
                                  (try_begin),
                                    (neq, ":center_no", ":most_threatened_center"), #200
                                    (store_distance_to_party_from_party, ":dist", ":party_no", ":center_no"),
                                    (lt, ":dist", ":minimum_distance"),
                                    (assign, ":minimum_distance", ":dist"),
                                    (assign, ":best_center_to_travel", ":center_no"),
                                  (try_end),
                                (try_end),
                              (else_try),
                                #active gathering
                                (assign, ":max_travel_distance", 150),
                                (try_begin),
                                  (ge, ":ratio_of_vassals_assembled",15),
                                  (store_sub, ":max_travel_distance", 35, ":ratio_of_vassals_assembled"),
                                  (val_add, ":max_travel_distance", 5), #5..25
                                  (val_mul, ":max_travel_distance", 6), #30..150
                                (try_end),
                                
                                (try_begin),
                                  (ge, ":most_threatened_center", 0),
                                  (store_distance_to_party_from_party, reg12, ":party_no", ":most_threatened_center"),
                                (else_try),
                                  (assign, reg12, 0),
                                (try_end),
                                
                                (assign, ":num_centers", 0),
                                (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
                                  (store_faction_of_party, ":center_faction", ":center_no"),
                                  (eq, ":center_faction", ":faction_no"),
                                  (try_begin),
                                    #(ge, ":max_travel_distance", 0),
                                    (store_distance_to_party_from_party, ":dist", ":party_no", ":center_no"),
                                    
                                    (try_begin),
                                      (ge, ":most_threatened_center", 0),
                                      (store_distance_to_party_from_party, reg13, ":center_no", ":most_threatened_center"),
                                    (else_try),
                                      (assign, reg13, 0),
                                    (try_end),
                                    
                                    (store_sub, reg11, reg13, reg12),
                                    
                                    (this_or_next|ge, reg11, 40),
                                    (this_or_next|ge, ":dist", ":max_travel_distance"),
                                    (eq, ":center_no", ":most_threatened_center"),
                                  (else_try),
                                    #this center is a candidate so increase num_centers by one.
                                    (val_add, ":num_centers", 1),
                                  (try_end),
                                (try_end),
                                
                                (try_begin),
                                  (ge, ":num_centers", 0),
                                  (store_random_in_range, ":random_center_no", 0, ":num_centers"),
                                  (val_add, ":random_center_no", 1),
                                  (assign, ":num_centers", 0),
                                  (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
                                    (store_faction_of_party, ":center_faction", ":center_no"),
                                    (eq, ":center_faction", ":faction_no"),
                                    (try_begin),
                                      (neq, ":center_no", ":most_threatened_center"),
                                      (store_distance_to_party_from_party, ":dist", ":party_no", ":center_no"),
                                      (lt, ":dist", ":max_travel_distance"),
                                      
                                      (try_begin),
                                        (ge, ":most_threatened_center", 0),
                                        (store_distance_to_party_from_party, reg13, ":center_no", ":most_threatened_center"),
                                      (else_try),
                                        (assign, reg13, 0),
                                      (try_end),
                                      
                                      (store_sub, reg11, reg13, reg12),
                                      (lt, reg11, 40),
                                      
                                      (val_sub, ":random_center_no", 1),
                                      (eq, ":random_center_no", 0),
                                      (assign, ":best_center_to_travel", ":center_no"),
                                    (try_end),
                                  (try_end),
                                (try_end),
                              (try_end),
                              
                              (assign, ":travel_target", ":best_center_to_travel"),
                              (assign, ":travel_target_new_assigned", 1),
                            (try_end),
                          (else_try),
                            #if party has an ai object and they are close to that object while gathering army,
                            #forget that ai object so they will select a new ai object next.
                            (is_between, ":old_ai_object", centers_begin, centers_end),
                            (party_get_position, pos1, ":party_no"),
                            (party_get_position, pos2, ":old_ai_object"),
                            (get_distance_between_positions, ":dist", pos1, pos2),
                            (le, ":dist", 3),
                            (assign, ":travel_target", -1),
                          (try_end),
                          #end ozan
                          
                          (try_begin),
                            (eq, ":travel_target", -1),
                            (assign, ":action", spai_undefined),
                          (else_try),
                            (assign, ":action", spai_visiting_village),
                          (try_end),
                          
                          (assign, ":object", ":travel_target"),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (try_begin),
                              (eq, ":travel_target", -1),
                              (str_store_string, s14, "str_as_the_marshall_i_am_assembling_the_army_of_the_realm"),
                            (else_try),
                              (try_begin),
                                (eq, ":faction_no", "$players_kingdom"),
                                (eq, ":travel_target_new_assigned", 1),
                                (le, "$number_of_report_to_army_quest_notes", 13),
                                (check_quest_active, "qst_report_to_army"),
                                (str_store_party_name_link, s10, ":travel_target"),
                                
                                (faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
                                
                                (str_store_troop_name_link, s11, ":faction_marshal"),
                                (store_current_hours, ":hours"),
                                (call_script, "script_game_get_date_text", 0, ":hours"),
                                
                                (str_store_string, s14, "str_as_the_marshall_i_am_assembling_the_army_of_the_realm_and_travel_to_lands_near_s10_to_inform_more_vassals"),
                                (str_store_string, s14, "@({s1}) {s11}: {s14}"),
                                (add_quest_note_from_sreg, "qst_report_to_army", "$number_of_report_to_army_quest_notes", s14, 0),
                                (val_add, "$number_of_report_to_army_quest_notes", 1),
                              (try_end),
                              
                              (assign, reg0, ":travel_target"),
                              (str_store_party_name, s10, ":travel_target"),
                              (str_store_string, s14, "str_as_the_marshall_i_am_assembling_the_army_of_the_realm_and_travel_to_lands_near_s10_to_inform_more_vassals"),
                            (try_end),
                            (str_store_string, s16, "str_i_intend_to_assemble_the_army_of_the_realm"),
                          (try_end),
                        (else_try),
                          (faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
                          (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_center),
                          (faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
                          
                          (assign, ":action", spai_besieging_center),
                          (assign, ":object", ":faction_object"),
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_as_the_marshall_i_am_leading_the_siege"),
                            (str_store_string, s16, "str_i_intend_to_begin_the_siege"),
                          (try_end),
                          
                        (else_try),
                          (faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
                          (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_raiding_village),
                          (faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
                          
                          (assign, ":action", spai_raiding_around_center),
                          (assign, ":object", ":faction_object"),
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_as_the_marshall_i_am_leading_our_raid"),
                            (str_store_string, s16, "str_i_intend_to_start_our_raid"),
                          (try_end),
                          
                        (else_try),
                          (faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
                          (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemies_around_center),
                          (faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
                          (party_is_active, ":faction_object"),
                          
                          #moved (party_set_ai_initiative, ":party_no", 10), #new to avoid losing time of marshal with attacking unimportant targets while there is a threat in our centers.
                          
                          (party_get_battle_opponent, ":besieger_party", ":faction_object"),
                          
                          (try_begin),
                            (gt, ":besieger_party", 0),
                            (party_is_active, ":besieger_party"), ##1.134
                            
                            (assign, ":action", spai_engaging_army),
                            (assign, ":object", ":besieger_party"),
                            (try_begin),
                              (eq, ":troop_no", "$g_talk_troop"),
                              (str_store_string, s14, "str_as_the_marshall_i_am_leading_our_forces_to_engage_the_enemy_in_battle"),
                              (str_store_string, s16, "str_i_intend_to_lead_our_forces_out_to_engage_the_enemy"),
                            (try_end),
                          (else_try),
                            (assign, ":action", spai_patrolling_around_center),
                            (assign, ":object", ":faction_object"),
                            (try_begin),
                              (eq, ":troop_no", "$g_talk_troop"),
                              (str_store_string, s14, "str_as_the_marshall_i_am_leading_our_forces_in_search_of_the_enemy"),
                              (str_store_string, s16, "str_i_intend_to_lead_our_forces_out_to_find_the_enemy"),
                            (try_end),
                          (try_end),
                          
                        (else_try),
                          (faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
                          (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemy_army),
                          (faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
                          (party_is_active, ":faction_object"), ##1.134
                          
                          (assign, ":action", spai_engaging_army),
                          (assign, ":object", ":faction_object"),
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_as_the_marshall_i_am_leading_our_forces_to_engage_the_enemy_in_battle"),
                            (str_store_string, s16, "str_i_intend_to_lead_our_forces_out_to_engage_the_enemy"),
                          (try_end),
                          
                          #Get reinforcements
                        (else_try),
                          (assign, ":lowest_acceptable_strength_percentage", 30),
                          
                          #if troop has enought gold then increase by 10%
                          #(troop_get_slot, ":cur_wealth", ":troop_no", slot_troop_wealth),
                          #(try_begin),
                          #  (ge, ":cur_wealth", 2000),
                          #  (assign, ":wealth_addition", 10),
                          #(else_try),
                          #  (store_div, ":wealth_addition", ":cur_wealth", 200),
                          #(try_end),
                          #(val_add, ":lowest_acceptable_strength_percentage", ":wealth_addition"),
                          
                          (call_script, "script_lord_get_home_center", ":troop_no"),
                          (assign, ":home_center", reg0),
                          (gt, ":home_center", -1),
                          (party_slot_eq, ":home_center", slot_town_lord, ":troop_no"), #newly added ##1.132, new line
                          
                          #if troop is very close to its home center increase by 20%
                          (assign, ":distance_addition", 0),
                          (party_get_position, pos0, ":home_center"),
                          (party_get_position, pos1, ":party_no"),
                          (get_distance_between_positions, ":dist", pos0, pos1),
                          
                          (try_begin),
                            (le, ":dist", 9000),
                            (store_div, ":distance_addition", ":dist", 600),
                            (store_sub, ":distance_addition", 15, ":distance_addition"),
                          (else_try),
                            (assign, ":distance_addition", 0),
                          (try_end),
                          (val_add, ":lowest_acceptable_strength_percentage", ":distance_addition"),
                          
                          #if there is no campaign for faction increase by 35%
                          (assign, ":no_campaign_addition", 35),
                          (try_begin),
                            (this_or_next|faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemy_army),
                            (this_or_next|faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemies_around_center),
                            (this_or_next|faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_raiding_village),
                            (this_or_next|faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_center),
                            (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_gathering_army),
                            (assign, ":no_campaign_addition", 0),
                            
                            #If marshal is player itself and if there is a campaign then lower lowest_acceptable_strength_percentage by 10 instead of not changing it.
                            #Because players become confused when they see very less participation from AI lords to their campaigns.
                            (try_begin),
                              (faction_slot_eq, ":faction_no", slot_faction_marshall, "trp_player"),
                              (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
                              (try_begin),
                                (eq, ":reduce_campaign_ai", 0), #hard
                                (assign, ":no_campaign_addition", 0),
                              (else_try),
                                (eq, ":reduce_campaign_ai", 1), #medium
                                (assign, ":no_campaign_addition", -10),
                              (else_try),
                                (eq, ":reduce_campaign_ai", 2), #easy
                                (assign, ":no_campaign_addition", -15),
                              (try_end),
                            (try_end),
                          (try_end),
                          (val_add, ":lowest_acceptable_strength_percentage", ":no_campaign_addition"),
                          (val_max, ":lowest_acceptable_strength_percentage", 25),
                          
                          #max : 30%+15%+35% = 80% (happens when there is no campaign and player is near to its home center.)
                          (lt, ":party_strength_as_percentage_of_ideal", ":lowest_acceptable_strength_percentage"),
                          
                          (try_begin),
                            (store_div, ":lowest_acceptable_strength_percentage_div_3", ":lowest_acceptable_strength_percentage", 3),
                            (ge, ":party_strength_as_percentage_of_ideal", ":lowest_acceptable_strength_percentage_div_3"),
                            (troop_get_slot, ":troop_wealth", ":troop_no", slot_troop_wealth),
                            (le, ":troop_wealth", 1800),
                            (assign, ":do_only_collecting_rents", 1),
                          (try_end),
                          
                          (assign, ":action", spai_holding_center),
                          (assign, ":object", ":home_center"),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_i_dont_have_enough_troops_and_i_need_to_get_some_more"),
                            
                            (str_store_string, s16, "str_i_am_running_low_on_troops"),
                          (try_end),
                          
                          (eq, ":do_only_collecting_rents", 0),
                          
                          #follow player orders
                        (else_try),
                          (eq, ":do_only_collecting_rents", 0),
                          (party_slot_ge, ":party_no", slot_party_following_orders_of_troop, "trp_kingdom_heroes_including_player_begin"),
                          
                          (party_get_slot, ":orders_type", ":party_no", slot_party_orders_type),
                          (party_get_slot, ":orders_object", ":party_no", slot_party_orders_object),
                          (party_get_slot, ":orders_time", ":party_no", slot_party_orders_time),
                          
                          (ge, ":orders_object", 0),
                          
                          (store_current_hours, ":hours_since_orders_given"),
                          (val_sub, ":hours_since_orders_given", ":orders_time"),
                          
                          (party_is_active, ":orders_object"),
                          (party_get_slot, ":object_state", ":orders_object", slot_village_state),
                          (store_faction_of_party, ":object_faction", ":orders_object"),
                          (store_relation, ":relation_with_object", ":faction_no", ":object_faction"),
                          
                          (assign, ":orders_are_appropriate", 1),
                          (try_begin),
                            (gt, ":hours_since_orders_given", 48),
                            (assign, ":orders_are_appropriate", 0),
                          (else_try),
                            (eq, ":orders_type", spai_raiding_around_center),
                            (this_or_next|ge, ":relation_with_object", 0),
                            (ge, ":object_state", 2),
                            (assign, ":orders_are_appropriate", 0),
                          (else_try),
                            (eq, ":orders_type", spai_besieging_center),
                            (ge, ":relation_with_object", 0),
                            (assign, ":orders_are_appropriate", 0),
                          (else_try),
                            (this_or_next|eq, ":orders_type", spai_holding_center),
                            (this_or_next|eq, ":orders_type", spai_retreating_to_center),
                            (this_or_next|eq, ":orders_type", spai_accompanying_army),
                            (eq, ":orders_type", spai_visiting_village),
                            (le, ":relation_with_object", 0),
                            (assign, ":orders_are_appropriate", 0),
                          (try_end),
                          
                          (eq, ":orders_are_appropriate", 1),
                          
                          (assign, ":action", ":orders_type"),
                          (assign, ":object", ":orders_object"),
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_we_are_following_your_direction"),
                          (try_end),
                          
                          #Host of player wedding
                        (else_try),
                          (eq, ":do_only_collecting_rents", 0),
                          (eq, ":operation_in_progress", 0),
                          (check_quest_active, "qst_wed_betrothed"),
                          (quest_slot_eq, "qst_wed_betrothed", slot_quest_giver_troop, ":troop_no"),
                          (quest_get_slot, ":bride", "qst_wed_betrothed", slot_quest_target_troop),
                          (call_script, "script_get_kingdom_lady_social_determinants", ":bride"),
                          (assign, ":wedding_venue", reg1),
                          
                          (assign, ":action", spai_holding_center),
                          (assign, ":object", ":wedding_venue"),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_i_need_to_make_preparations_for_your_wedding"),
                            (str_store_string, s16, "str_after_all_i_need_to_make_preparations_for_your_wedding"),
                          (try_end),
                          
                          #Bridegroom at player wedding
                        (else_try),
                          (eq, ":do_only_collecting_rents", 0),
                          (eq, ":operation_in_progress", 0),
                          (check_quest_active, "qst_wed_betrothed_female"),
                          (quest_slot_eq, "qst_wed_betrothed_female", slot_quest_giver_troop, ":troop_no"),
                          
                          (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_feast),
                          (faction_get_slot, ":feast_venue", ":faction_no", slot_faction_ai_object),
                          
                          (assign, ":action", spai_holding_center),
                          (assign, ":object", ":feast_venue"),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_i_am_heading_to_the_site_of_our_wedding"),
                            (str_store_string, s16, "str_after_all_we_are_soon_to_be_wed"),
                          (try_end),
                          
                          #Host of other feast
                        (else_try),
                          (eq, ":do_only_collecting_rents", 0),
                          (eq, ":operation_in_progress", 0),
                          (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_feast),
                          (faction_get_slot, ":feast_venue", ":faction_no", slot_faction_ai_object),
                          (party_slot_eq, ":feast_venue", slot_town_lord, ":troop_no"),
                          
                          (assign, ":action", spai_holding_center),
                          (assign, ":object", ":feast_venue"),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_i_am_hosting_a_feast_there"),
                            (str_store_string, s16, "str_i_have_a_feast_to_host"),
                          (try_end),
                          
                          #I am the bridegroom at a feast
                        (else_try),
                          (eq, ":do_only_collecting_rents", 0),
                          (eq, ":operation_in_progress", 0),
                          (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_feast),
                          (troop_get_slot, ":troop_betrothed", ":troop_no", slot_troop_betrothed),
                          (is_between, ":troop_betrothed", kingdom_ladies_begin, kingdom_ladies_end),
                          
                          (faction_get_slot, ":feast_venue", ":faction_no", slot_faction_ai_object),
                          
                          (assign, ":action", spai_holding_center),
                          (assign, ":object", ":feast_venue"),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_i_am_to_be_the_bridegroom_there"),
                            (str_store_string, s16, "str_my_wedding_day_draws_near"),
                          (try_end),
                          
                          #Drop off prisoners
                        (else_try),
                          (eq, ":do_only_collecting_rents", 0),
                          (gt,  ":party_ratio_of_prisoners", 35),
                          (eq, ":operation_in_progress", 0),
                          
                          (call_script, "script_lord_get_home_center", ":troop_no"),
                          (assign, ":home_center", reg0),
                          
                          (gt, ":home_center", -1),
                          
                          (assign, ":action", spai_holding_center),
                          (assign, ":object", ":home_center"),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_i_have_too_much_loot_and_too_many_prisoners_and_need_to_secure_them"),
                            (str_store_string, s16, "str_i_should_think_of_dropping_off_some_of_my_prisoners"),
                          (try_end),
                          
                          #Reinforce a weak center
                        (else_try),
                          (eq, ":do_only_collecting_rents", 0),
                          (assign, ":center_to_reinforce", -1),
                          (assign, ":center_reinforce_score", 100),
                          (eq, ":operation_in_progress", 0),
                          
                          (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
                            (party_slot_eq, ":walled_center", slot_town_lord, ":troop_no"),
                            (party_get_slot, ":center_strength", ":walled_center", slot_party_cached_strength),
                            (lt, ":center_strength", ":center_reinforce_score"),
                            (assign, ":center_to_reinforce", ":walled_center"),
                            (assign, ":center_reinforce_score", ":center_strength"),
                          (try_end),
                          
                          (gt, ":center_to_reinforce", -1),
                          
                          (assign, ":action", spai_holding_center),
                          (assign, ":object", ":center_to_reinforce"),
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_i_need_to_reinforce_it_as_it_is_poorly_garrisoned"),
                            (str_store_string, s16, "str_there_is_a_hole_in_our_defenses"),
                          (try_end),
                          
                          #Continue screening, if already doing so
                        (else_try),
                          (eq, ":do_only_collecting_rents", 0),
                          (eq, ":old_ai_state", spai_screening_army),
                          
                          (faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
						  (ge, ":faction_marshal", 0),
                          (troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
                          (party_is_active, ":marshal_party"),
                          
                          (call_script, "script_npc_decision_checklist_troop_follow_or_not", ":troop_no"),
                          (eq, reg0, 1),
                          
                          (assign, ":action", spai_screening_army),
                          (assign, ":object", ":marshal_party"),
                          (try_begin),
                            (eq, "$g_talk_troop", ":troop_no"),
                            (str_store_string, s14, "str_i_am_following_the_marshals_orders"),
                            (str_store_string, s16, "str_the_marshal_has_given_me_this_command"),
                          (try_end),
                          
                        (else_try), #special case for sfai_attacking_enemies_around_center for village raids
                          (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemies_around_center),
                          (is_between, ":faction_object", villages_begin, villages_end),
                          
                          (call_script, "script_npc_decision_checklist_troop_follow_or_not", ":troop_no"),
                          (eq, reg0, 1),
                          
                          (faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
                          (party_get_slot, ":raider_party", ":faction_object", slot_village_raided_by),
                          (party_is_active, ":raider_party"), ##1.134
                          
                          #think about adding one more condition here, what if raider army is so powerfull, again lords will go and engage enemy one by one?
                          (party_get_slot, ":enemy_strength_nearby", ":faction_object", slot_center_sortie_enemy_strength),
                          (lt, ":enemy_strength_nearby", 4000),
                          #end think
                          
                          (assign, ":action", spai_engaging_army),
                          (assign, ":object", ":raider_party"),
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_our_realm_needs_my_support_there_is_enemy_raiding_one_of_our_villages_which_is_not_to_far_from_here_i_am_going_there"),
                            (str_store_string, s16, "str_the_marshal_has_issued_a_summons"),
                          (try_end),
                          
                          #Follow the marshall's orders - if on the offensive, and the campaign has not lasted too long. Readiness is currently randomly set
                        (else_try),
                          (eq, ":do_only_collecting_rents", 0),
                          (call_script, "script_npc_decision_checklist_troop_follow_or_not", ":troop_no"),
                          (eq, reg0, 1),
                          
                          (faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
						  (ge, ":faction_marshal", 0),
                          (troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
                          
                          (assign, ":action", spai_accompanying_army),
                          (assign, ":object", ":marshal_party"),
                          
                          (try_begin),
                            (eq, "$g_talk_troop", ":troop_no"),
                            (str_store_string, s14, "str_i_am_answering_the_marshals_summons"),
                            (str_store_string, s16, "str_the_marshal_has_issued_a_summons"),
                          (try_end),
                          
                          #Support a nearby ally who is on the offensive
                        (else_try),
                          (eq, ":do_only_collecting_rents", 0),
                          (eq, ":faction_is_at_war", 1),
                          
                          (assign, ":party_to_support", -1),
                          (try_for_range, ":allied_hero", active_npcs_begin, active_npcs_end),
                            (troop_slot_eq, ":allied_hero", slot_troop_occupation, slto_kingdom_hero),
                            (store_faction_of_troop, ":allied_hero_faction", ":allied_hero"),
                            (eq, ":allied_hero_faction", ":faction_no"),
                            
                            (neq, ":allied_hero", ":troop_no"),
                            
                            (troop_get_slot, ":allied_hero_party", ":allied_hero", slot_troop_leaded_party),
                            (gt, ":allied_hero_party", 1),
                            (party_is_active, ":allied_hero_party"),
                            
                            
                            (this_or_next|party_slot_eq, ":allied_hero_party", slot_party_ai_state, spai_raiding_around_center),
                            (party_slot_eq, ":allied_hero_party", slot_party_ai_state, spai_besieging_center),
                            
                            (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":allied_hero"),
                            (gt, reg0, 4),
                            
                            (troop_get_slot, ":troop_renown", ":troop_no", slot_troop_renown),
                            (troop_get_slot, ":ally_renown", ":allied_hero", slot_troop_renown),
                            (le, ":troop_renown", ":ally_renown"), #Ally to support must have higher renown
                            
                            (store_distance_to_party_from_party, ":distance", ":party_no", ":allied_hero_party"),
                            
                            (lt, ":distance", 5),
                            
                            (assign, ":party_to_support", ":allied_hero_party"),
                          (try_end),
                          (gt, ":party_to_support", 0),
                          
                          (assign, ":action", spai_accompanying_army),
                          (assign, ":object", ":party_to_support"),
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (party_stack_get_troop_id, ":leader", ":object", 0),
                            (str_store_troop_name, s10, ":leader"),
                            
                            (call_script, "script_troop_get_family_relation_to_troop", ":leader", "$g_talk_troop"),
                            (try_begin),
                              (eq, reg0, 0),
                              (str_store_string, s11, "str_comradeinarms"),
                            (try_end),
                            (str_store_string, s14, "str_i_am_supporting_my_s11_s10"),
                            (str_store_string, s16, "str_i_believe_that_one_of_my_comrades_is_in_need"),
                          (try_end),
                          #I have decided to attack a vulnerable fortress
                        (else_try),
                          (eq, ":do_only_collecting_rents", 0),
                          (eq, ":faction_is_at_war", 1),
                          (eq, ":operation_in_progress", 0),
                          
                          (assign, ":walled_center_to_attack", -1),
                          (assign, ":walled_center_score", 50),
                          
                          (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
                            (store_faction_of_party, ":walled_center_faction", ":walled_center"),
                            (store_relation, ":relation", ":faction_no", ":walled_center_faction"),
                            (lt, ":relation", 0),
                            
                            (party_get_slot, ":center_cached_strength", ":walled_center", slot_party_cached_strength),
                            (val_mul, ":center_cached_strength", 3),
                            (val_mul, ":center_cached_strength", 2),
                            
                            (lt, ":center_cached_strength", ":party_cached_strength"),
                            (lt, ":center_cached_strength", 750),
                            
                            (party_slot_eq, ":walled_center", slot_village_state, svs_normal),
                            (store_distance_to_party_from_party, ":distance", ":walled_center", ":party_no"),
                            (lt, ":distance", ":walled_center_score"),
                            
                            (assign, ":walled_center_to_attack", ":walled_center"),
                            (assign, ":walled_center_score", ":distance"),
                          (try_end),
                          
                          (is_between, ":walled_center_to_attack", centers_begin, centers_end),
                          
                          (assign, ":action", spai_besieging_center),
                          (assign, ":object", ":walled_center_to_attack"),
                          (try_begin),
                            (eq, "$cheat_mode", 1),
                            (str_store_faction_name, s20, ":faction_no"),
                            (str_store_party_name, s21, ":object"),
                            (display_message, "str_s20_decided_to_attack_s21"),
                          (try_end),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_a_fortress_is_vulnerable"),
                            (str_store_string, s16, "str_i_believe_that_the_enemy_may_be_vulnerable"),
                          (try_end),
                          
                          #I am visiting an estate
                        (else_try),
                          (assign, ":center_to_visit", -1),
                          (assign, ":score_to_beat", 300), #at least 300 gold to pick up
                          (troop_get_slot, ":troop_wealth", ":troop_no", slot_troop_wealth), #average troop wealth is 2000
                          (val_div, ":troop_wealth", 10), #average troop wealth 10% is is 200
                          (val_add, ":score_to_beat", ":troop_wealth"), #average score to beat is 500
                          (eq, ":operation_in_progress", 0),
                          
                          (try_begin),
                            (faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
                            
                            (assign, reg17, 0),
                            (try_begin),
                              (party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
                              (party_slot_eq, ":party_no", slot_party_ai_object, ":faction_marshal"),
                              (assign, reg17, 1),
                            (else_try),
                              (party_slot_eq, ":party_no", slot_party_following_player, 1),
                              (assign, reg17, 1),
                            (try_end),
                            (eq, reg17, 1),
                            
                            (try_begin),
                              (neq, ":faction_marshal", "trp_player"),
                              (neg|party_slot_eq, ":party_no", slot_party_following_player, 1),
                              (val_add, ":score_to_beat", 125),
                            (else_try),
                              (val_add, ":score_to_beat", 250),
                            (try_end),
                          (try_end),
                          
                          (try_for_range, ":center_no", centers_begin, centers_end),
                            (party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
                            
                            (assign, reg17, 0),
                            (try_begin),
                              (is_between, ":center_no", villages_begin, villages_end),
                              (party_slot_eq, ":center_no", slot_village_state, svs_normal),
                              (assign, reg17, 1),
                            (else_try),
                              (party_slot_eq, ":center_no", slot_center_is_besieged_by, -1),
                              (assign, reg17, 1),
                            (try_end),
                            (eq, reg17, 1),
                            
                            (party_get_slot, ":tariffs_available", ":center_no", slot_center_accumulated_tariffs),
                            (party_get_slot, ":rents_available", ":center_no", slot_center_accumulated_rents),
                            (store_add, ":money_available", ":rents_available", ":tariffs_available"),
                            
                            (gt, ":money_available", ":score_to_beat"),
                            (assign, ":center_to_visit", ":center_no"),
                            (assign, ":score_to_beat", ":money_available"),
                          (try_end),
                          
                          (is_between, ":center_to_visit", centers_begin, centers_end),
                          
                          (try_begin),
                            (is_between, ":center_to_visit", walled_centers_begin, walled_centers_end),
                            (assign, ":action", spai_holding_center),
                            (assign, ":object", ":center_to_visit"),
                          (else_try),
                            (assign, ":action", spai_visiting_village),
                            (assign, ":object", ":center_to_visit"),
                          (try_end),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_i_need_to_inspect_my_properties_and_collect_my_dues"),
                            (str_store_string, s16, "str_it_has_been_too_long_since_i_have_inspected_my_estates"),
                          (try_end),
                          
                          #My men are weary, and I wish to return home
                        (else_try),
                          (eq, ":do_only_collecting_rents", 0),
                          (this_or_next|gt, ":hours_since_last_rest", 504), #Three weeks
                          (lt, ":aggressiveness", 25),
                          (gt, ":hours_since_last_rest", 168), #one week if aggressiveness < 25
                          (eq, ":operation_in_progress", 0),
                          
                          (call_script, "script_lord_get_home_center", ":troop_no"),
                          (assign, ":home_center", reg0),
                          
                          (gt, ":home_center", -1),
                          (assign, ":action", spai_holding_center),
                          (assign, ":object", ":home_center"),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_my_men_are_weary_so_we_are_returning_home"),
                            (str_store_string, s16, "str_my_men_are_becoming_weary"),
                          (try_end),
                          
                          #I have a score to settle with the enemy
                        (else_try),
                          (eq, ":do_only_collecting_rents", 0),
                          (this_or_next|gt, ":hours_since_last_combat", 12),
                          (lt, ":hours_since_last_rest", 96),
                          (eq, ":operation_in_progress", 0),
                          
						  (eq, ":faction_is_at_war", 1),
						  ##diplomacy start+ roguish lords can also do this, but humanitarian lords of any kind won't
						  (call_script, "script_dplmc_get_troop_morality_value", ":troop_no", tmt_humanitarian),
						  (lt, reg0, 1),
						  (this_or_next|eq, ":troop_reputation", lrep_roguish),
						  ##diplomacy end+
						  (this_or_next|eq, ":troop_reputation", lrep_debauched),
						  (eq, ":troop_reputation", lrep_quarrelsome),
                          
                          (assign, ":target_village", -1),
                          (assign, ":score_to_beat", 0), #based on relation
                          
                          (try_for_range, ":possible_target", villages_begin, villages_end),
                            (store_faction_of_party, ":village_faction", ":possible_target"),
                            (store_relation, ":relation", ":village_faction", ":faction_no"),
                            (lt, ":relation", 0),
                            
                            (neg|party_slot_ge, ":possible_target", slot_village_state, svs_looted),
                            (party_get_slot, ":town_lord", ":possible_target", slot_town_lord),
                            (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":town_lord"),
                            (assign, ":village_score", reg0),
                            
                            (lt, ":village_score", ":score_to_beat"),
                            (assign, ":score_to_beat", ":village_score"),
                            (assign, ":target_village", ":possible_target"),
                          (try_end),
                          
                          (is_between, ":target_village", centers_begin, centers_end),
                          (assign, ":action", spai_raiding_around_center),
                          (assign, ":object", ":target_village"),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_i_have_a_score_to_settle_with_the_lord_there"),
                            (str_store_string, s16, "str_i_am_thinking_of_settling_an_old_score"),
                          (try_end),
                          
                          #I need money, so I am raiding where the money is
                        (else_try),
                          (eq, ":do_only_collecting_rents", 0),
                          (eq, ":faction_is_at_war", 1),
                          (eq, ":operation_in_progress", 0),
                          
                          (this_or_next|gt, ":hours_since_last_combat", 12),
                          (lt, ":hours_since_last_rest", 96),
                          (gt, ":aggressiveness", 40),
                          
						  ##diplomacy start+
						  #Roguish lords can also do this.  Humanitarian companions will never
						  #do this, even if they otherwise have an eligible reputation.  Companions
						  #who actively enjoy raiding can also do this, regardless of whether they
						  #have an eligible reputation.
						  (call_script, "script_dplmc_get_troop_morality_value", ":troop_no", tmt_humanitarian),
						  (lt, reg0, 1),
						  (this_or_next|lt, reg0, 0),
						  (this_or_next|eq, ":troop_reputation", lrep_roguish),
						  ##diplomacy end+
						  (this_or_next|eq, ":troop_reputation", lrep_debauched),
						  (this_or_next|eq, ":troop_reputation", lrep_selfrighteous),
						  (this_or_next|eq, ":troop_reputation", lrep_cunning),
						  (eq, ":troop_reputation", lrep_quarrelsome),
                          
                          (troop_get_slot, ":wealth", ":troop_no", slot_troop_wealth),
                          (lt, ":wealth", 500),
                          
                          (assign, ":score_to_beat", 0),
                          (assign, ":target_village", -1),
                          
                          (try_for_range, ":possible_target", villages_begin, villages_end),
                            (store_faction_of_party, ":village_faction", ":possible_target"),
                            (store_relation, ":relation", ":village_faction", ":faction_no"),
                            (lt, ":relation", 0),
                            
                            (this_or_next|party_slot_eq, ":possible_target", slot_village_state, svs_normal),
                            (party_slot_eq, ":possible_target", slot_village_state, svs_being_raided),
                            
                            (party_get_slot, reg17, ":possible_target", slot_town_prosperity),
                            (store_distance_to_party_from_party, ":distance", ":party_no", ":possible_target"),
                            (val_sub, reg17, ":distance"),
                            
                            (gt, reg17, ":score_to_beat"),
                            (assign, ":score_to_beat", reg17),
                            (assign, ":target_village", ":possible_target"),
                          (try_end),
                          
                          (gt, ":target_village", -1),
                          
                          (assign, ":action", spai_raiding_around_center),
                          (assign, ":object", ":target_village"),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_i_am_short_of_money_and_i_hear_that_there_is_much_wealth_there"),
                            (str_store_string, s16, "str_i_need_to_refill_my_purse_preferably_with_the_enemys_money"),
                          (try_end),
                          
                          #Attacking wealthiest lands
                        (else_try),
                          (eq, ":do_only_collecting_rents", 0),
                          (eq, ":faction_is_at_war", 1),
                          (eq, ":operation_in_progress", 0),
                          (gt, ":aggressiveness", 65),
                          
                          (assign, ":score_to_beat", 0),
                          (assign, ":target_village", -1),
                          
                          (try_for_range, ":possible_target", villages_begin, villages_end),
                            (store_faction_of_party, ":village_faction", ":possible_target"),
                            (store_relation, ":relation", ":village_faction", ":faction_no"),
                            (lt, ":relation", 0),
                            (neg|party_slot_eq, ":possible_target", slot_village_state, svs_looted),
                            (party_get_slot, ":village_prosperity", ":possible_target", slot_town_prosperity),
                            (val_mul, ":village_prosperity", 2),
                            
                            (store_distance_to_party_from_party, ":distance", ":party_no", ":possible_target"),
                            (val_sub, ":village_prosperity", ":distance"),
                            (gt, ":village_prosperity", ":score_to_beat"),
                            
                            (assign, ":score_to_beat", ":village_prosperity"),
                            (assign, ":target_village", ":possible_target"),
                          (try_end),
                          
							##diplomacy start+ companions who hate raiding will not raid
							(call_script, "script_dplmc_get_troop_morality_value", ":troop_no", tmt_humanitarian),
							(lt, reg0, 1),
							##diplomacy end+
							(gt, ":target_village", -1),
                          
                          (assign, ":action", spai_raiding_around_center),
                          (assign, ":object", ":target_village"),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s14, "str_by_striking_at_the_enemys_richest_lands_perhaps_i_can_draw_them_out_to_battle"),
                            (str_store_string, s16, "str_i_am_thinking_of_going_on_the_attack"),
                          (try_end),
                          
                          #End the war
						(else_try),
						  (eq, ":do_only_collecting_rents", 0),
							##diplomacy start+
							(assign, reg0, 0),
							(try_begin),
								#A liege in service to another lord or allied with the player can do this.
								(this_or_next|eq, ":troop_reputation", lrep_none),
								(this_or_next|is_between, ":troop_no", kings_begin, kings_end),
								(is_between, ":troop_no", pretenders_begin, pretenders_end),
								(this_or_next|neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":troop_no"),
								(this_or_next|troop_slot_eq, ":troop_no", slot_troop_spouse, "trp_player"),
									(troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_no"),
								(assign, reg0, 0),
							(else_try),
								#Lords who are simulatenously Martial and tmt_honest (such as Alayen),
								#or Custodian and tmt_honest (such as Artimenner) can also do this.
								(this_or_next|eq, ":troop_reputation", lrep_martial),
								(eq, ":troop_reputation", lrep_custodian),
								(call_script, "script_dplmc_get_troop_morality_value", ":troop_no", tmt_honest),
							(try_end),
							(this_or_next|ge, reg0, 1),
							##diplomacy end+
							(eq, ":troop_reputation", lrep_upstanding),
							(eq, ":faction_is_at_war", 1),
							(eq, ":operation_in_progress", 0),

							(assign, ":faction_to_attack", -1),
							(try_for_range, ":possible_faction_to_attack", kingdoms_begin, kingdoms_end),
								(store_relation, ":relation", ":faction_no", ":possible_faction_to_attack"),
								(lt, ":relation", 0),
								(faction_slot_eq, ":possible_faction_to_attack", slot_faction_state, sfs_active),

								(store_add, ":war_damage_inflicted_slot", ":possible_faction_to_attack", slot_faction_war_damage_inflicted_on_factions_begin),
								(val_sub, ":war_damage_inflicted_slot", kingdoms_begin),
								(faction_get_slot, ":war_damage_inflicted", ":faction_no", ":war_damage_inflicted_slot"),

								(store_add, ":war_damage_suffered_slot", ":faction_no", slot_faction_war_damage_inflicted_on_factions_begin),
								(val_sub, ":war_damage_suffered_slot", kingdoms_begin),
								(faction_get_slot, ":war_damage_suffered", ":possible_faction_to_attack", ":war_damage_suffered_slot"),

								(gt, ":war_damage_inflicted", 80),
								(lt, ":war_damage_inflicted", ":war_damage_suffered"),
								(assign, ":faction_to_attack", ":possible_faction_to_attack"),
							(try_end),

							(gt, ":faction_to_attack", -1),

							(assign, ":target_village", -1),
							(assign, ":score_to_beat", 50),

							(try_for_range, ":possible_target_village", villages_begin, villages_end),
								(store_faction_of_party, ":village_faction", ":possible_target_village"),
								(eq, ":village_faction", ":faction_to_attack"),
								(neg|party_slot_eq, ":possible_target_village", slot_village_state, svs_looted),
								(store_distance_to_party_from_party, ":distance", ":party_no", ":possible_target_village"),
								(lt, ":distance", ":score_to_beat"),

								(assign, ":score_to_beat", ":distance"),
								(assign, ":target_village", ":possible_target_village"),
							(try_end),

							(gt, ":target_village", -1),

							(assign, ":action", spai_raiding_around_center),
							(assign, ":object", ":target_village"),

							(try_begin),
								(eq, ":troop_no", "$g_talk_troop"),
								(str_store_string, s14, "str_perhaps_if_i_strike_one_more_blow_we_may_end_this_war_on_our_terms_"),
								(str_store_string, s16, "str_we_may_be_able_to_bring_this_war_to_a_close_with_a_few_more_blows"),
							(try_end),

						#I have a feast to attend
						(else_try),
						  (eq, ":do_only_collecting_rents", 0),
							(faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_feast),
							(faction_get_slot, ":feast_venue", ":faction_no", slot_faction_ai_object),
							(party_get_slot, ":feast_host", ":feast_venue", slot_town_lord),
							(eq, ":operation_in_progress", 0),

							(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":feast_host"),
							(assign, ":relation_with_host", reg0),

							(ge, ":relation_with_host", 0),

							(assign, ":action", spai_holding_center),
							(assign, ":object", ":feast_venue"),

							(try_begin),
								(eq, ":troop_no", "$g_talk_troop"),
								(str_store_string, s14, "str_i_wish_to_attend_the_feast_there"),
								(str_store_string, s16, "str_there_is_a_feast_which_i_wish_to_attend"),
							(try_end),
						#A lady to court
						(else_try),
						  (eq, ":do_only_collecting_rents", 0),
							(neg|troop_slot_eq, "trp_player", slot_troop_betrothed, ":troop_no"),
							(troop_slot_eq, ":troop_no", slot_troop_spouse, -1),
							(neg|is_between, ":troop_no", kings_begin, kings_end),
							(neg|is_between, ":troop_no", pretenders_begin, pretenders_end),


							(gt, ":hours_since_last_courtship", 72),
							(eq, ":operation_in_progress", 0),

							(assign, ":center_to_visit", -1),
							(assign, ":score_to_beat", 150),

							(try_for_range, ":love_interest_slot", slot_troop_love_interest_1, slot_troop_love_interests_end),
								(troop_get_slot, ":love_interest", ":troop_no", ":love_interest_slot"),
								(is_between, ":love_interest", kingdom_ladies_begin, kingdom_ladies_end),
								(troop_get_slot, ":love_interest_center", ":love_interest", slot_troop_cur_center),
								(is_between, ":love_interest_center", centers_begin, centers_end),
								(store_faction_of_party, ":love_interest_faction_no", ":love_interest_center"),
								(eq, ":faction_no", ":love_interest_faction_no"),
								#(store_relation, ":relation", ":faction_no", ":love_interest_faction_no"),
								#(ge, ":relation", 0),

								(store_distance_to_party_from_party, ":distance", ":party_no", ":love_interest_center"),

								(lt, ":distance", ":score_to_beat"),
								(assign, ":center_to_visit", ":love_interest_center"),
								(assign, ":score_to_beat", ":distance"),
							(try_end),

							(gt, ":center_to_visit", -1),

							(assign, ":action", spai_holding_center),
							(assign, ":object", ":center_to_visit"),

							(try_begin),
								(eq, ":troop_no", "$g_talk_troop"),
								(str_store_string, s14, "str_there_is_a_fair_lady_there_whom_i_wish_to_court"),
								(str_store_string, s16, "str_i_have_the_inclination_to_pay_court_to_a_fair_lady"),
							(try_end),

						#Patrolling an alarmed center
						(else_try),
						  (eq, ":do_only_collecting_rents", 0),
							(assign, ":target_center", -1),
							(assign, ":score_to_beat", 60),
							(eq, ":operation_in_progress", 0),
							(gt, ":aggressiveness", 40),

							(try_for_range, ":center_to_patrol", centers_begin, centers_end), #find closest center that has spotted enemies.
								(store_faction_of_party, ":center_faction", ":center_to_patrol"),
								(eq, ":center_faction", ":faction_no"),
								(party_slot_ge, ":center_to_patrol", slot_center_last_spotted_enemy, 0),

								#new - begin
								(party_get_slot, ":sortie_strength", ":center_to_patrol", slot_center_sortie_strength),
								(party_get_slot, ":enemy_strength", ":center_to_patrol", slot_center_sortie_enemy_strength),
								(store_mul, ":enemy_strength_mul_14_div_10", ":enemy_strength", 14),
								(val_div, ":enemy_strength_mul_14_div_10", 10),
								(party_get_slot, ":party_strength", ":party_no", slot_party_cached_strength),

								(this_or_next|neg|party_is_in_town, ":party_no", ":center_to_patrol"),
								(gt, ":sortie_strength", ":enemy_strength_mul_14_div_10"),

								(ge, ":party_strength", 100),
								#new - end

								(party_get_slot, reg17, ":center_to_patrol", slot_town_lord),
								(call_script, "script_troop_get_relation_with_troop", reg17, ":troop_no"),

								(this_or_next|eq, ":troop_reputation", lrep_upstanding),
									(gt, reg0, -5),

								(store_distance_to_party_from_party, ":distance", ":party_no", ":center_to_patrol"),
								(lt, ":distance", ":score_to_beat"),

								(assign, ":target_center", ":center_to_patrol"),
								(assign, ":score_to_beat", ":distance"),
							(try_end),

							(is_between, ":target_center", centers_begin, centers_end),

							(assign, ":action", spai_patrolling_around_center),
							(assign, ":object", ":target_center"),

							(try_begin),
								(eq, ":troop_no", "$g_talk_troop"),
								(str_store_string, s14, "str_we_have_heard_reports_that_the_enemy_is_in_the_area"),
								(str_store_string, s16, "str_i_have_heard_reports_of_enemy_incursions_into_our_territory"),
							(try_end),

						#Time in household
						(else_try),
						  (eq, ":do_only_collecting_rents", 0),
							(gt, ":hours_since_last_home", 168),
							(eq, ":operation_in_progress", 0),

							(call_script, "script_lord_get_home_center", ":troop_no"),
							(assign, ":home_center", reg0),
							(gt, ":home_center", -1),

							(assign, ":action", spai_holding_center),
							(assign, ":object", ":home_center"),

							(try_begin),
								(eq, ":troop_no", "$g_talk_troop"),
								(str_store_string, s14, "str_i_need_to_spend_some_time_with_my_household"),
								(str_store_string, s16, "str_it_has_been_a_long_time_since_i_have_been_able_to_spend_time_with_my_household"),
							(try_end),

						#Patrolling the borders
						(else_try),
						  (eq, ":do_only_collecting_rents", 0),
							(eq, ":faction_is_at_war", 1),
							(gt, ":aggressiveness", 65),
							(eq, ":operation_in_progress", 0),

							(assign, ":center_to_patrol", -1),
							(assign, ":score_to_beat", 75),

							(try_for_range, ":village", villages_begin, villages_end),
								(store_faction_of_party, ":village_faction", ":village"),
								(store_relation, ":relation", ":village_faction", ":faction_no"),
								(lt, ":relation", 0),

								(store_distance_to_party_from_party, ":distance", ":village", ":party_no"),
								(lt, ":distance", ":score_to_beat"),

								(assign, ":score_to_beat", ":distance"),
								(assign, ":center_to_patrol", ":village"),
							(try_end),

							(is_between, ":center_to_patrol", villages_begin, villages_end),

							(assign, ":action", spai_patrolling_around_center),
							(assign, ":object", ":center_to_patrol"),

							(try_begin),
								(eq, ":troop_no", "$g_talk_troop"),
								(str_store_string, s14, "str_i_am_watching_the_borders"),
								(str_store_string, s16, "str_i_may_be_needed_to_watch_the_borders"),
							(try_end),

						#Visiting a friend - temporarily disabled
						(else_try),
							(eq, 1, 0),

						#Patrolling home
						(else_try),
						  (eq, ":do_only_collecting_rents", 0),
							(call_script, "script_lord_get_home_center", ":troop_no"),
							(assign, ":home_center", reg0),

							(is_between, ":home_center", centers_begin, centers_end),
							(eq, ":operation_in_progress", 0),

							(assign, ":action", spai_patrolling_around_center),
							(assign, ":object", ":home_center"),

							(try_begin),
								(eq, ":troop_no", "$g_talk_troop"),
								(str_store_string, s14, "str_i_will_guard_the_areas_near_my_home"),
								(str_store_string, s16, "str_i_am_perhaps_needed_most_at_home"),
							(try_end),

						#Default end
						(else_try),
						  (eq, ":do_only_collecting_rents", 0),
							(eq, ":operation_in_progress", 0),

							(call_script, "script_lord_get_home_center", ":troop_no"),
							(assign, ":home_center", reg0),
							(is_between, ":home_center", walled_centers_begin, walled_centers_end),

							(assign, ":action", spai_holding_center),
							(assign, ":object", ":home_center"),

							(try_begin),
								(eq, ":troop_no", "$g_talk_troop"),
								(str_store_string, s14, "str_i_cant_think_of_anything_better_to_do"),
							(try_end),
						(else_try),
						  (eq, ":do_only_collecting_rents", 0),
							(eq, ":operation_in_progress", 1),

							(party_get_slot, ":action", ":party_no", slot_party_ai_state),
							(party_get_slot, ":object", ":party_no", slot_party_ai_object),

							(try_begin),
								(eq, ":troop_no", "$g_talk_troop"),
								(str_store_string, s14, "str_i_am_completing_what_i_have_already_begun"),
							(try_end),
						(else_try),
						  (eq, ":do_only_collecting_rents", 0),
							(assign, ":action", spai_undefined),
							(assign, ":object", -1),

							(try_begin),
								(eq, ":troop_no", "$g_talk_troop"),
								(str_store_string, s14, "str_i_dont_even_have_a_home_to_which_to_return"),
							(try_end),
						(try_end),

						(try_begin),
							(eq, "$cheat_mode", 2),
							(str_store_troop_name, s10, ":troop_no"),
							(display_message, "str_debug__s10_decides_s14_faction_ai_s15"),
						(try_end),

						(assign, reg0, ":action"),
						(assign, reg1, ":object"),
						]),
                    
                    #script_npc_decision_checklist_troop_follow_or_not
                    # INPUT: troop_no
                    # OUTPUT: reg0
                    (
                      "npc_decision_checklist_troop_follow_or_not", [
                        
                        (store_script_param, ":troop_no", 1),
                        (store_faction_of_troop, ":faction_no", ":troop_no"),
                        (faction_get_slot, ":faction_ai_state", ":faction_no", slot_faction_ai_state),
                        
                        (troop_get_slot, ":troop_reputation", ":troop_no", slot_lord_reputation_type),
                        (faction_get_slot, ":faction_marshall", ":faction_no", slot_faction_marshall),
                        
						(assign, ":result", 0),
						(try_begin),
							##diplomacy start+ add another check
							(this_or_next|lt, ":faction_marshall", 0),
							##diplomacy end+
							(eq, ":faction_marshall", -1),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s15, "str__i_am_acting_independently_because_no_marshal_is_appointed"),
                          (try_end),
                        (else_try),
                          (troop_get_slot, ":faction_marshall_party", ":faction_marshall", slot_troop_leaded_party),
                          (neg|party_is_active, ":faction_marshall_party"),
                          
                          #Not doing an offensive
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s15, "str__i_am_acting_independently_because_our_marshal_is_currently_indisposed"),
                          (try_end),
                        (else_try),
                          (neq, ":faction_ai_state", sfai_attacking_center),
                          (neq, ":faction_ai_state", sfai_raiding_village),
                          (neq, ":faction_ai_state", sfai_attacking_enemies_around_center),
                          (neq, ":faction_ai_state", sfai_attacking_enemy_army),
                          (neq, ":faction_ai_state", sfai_gathering_army),
                          
                          #Not doing an offensive
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s15, "str__i_am_acting_independently_because_our_realm_is_currently_not_on_campaign"),
                          (try_end),
                        (else_try),
                          (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_marshall"),
                          (assign, ":relation_with_marshall", reg0),
                          
                          (try_begin),
                            (le, ":relation_with_marshall", -10),
                            (assign, ":acceptance_level", 10000),
                          (else_try),
                            (store_mul, ":acceptance_level", ":relation_with_marshall", -1000),
                          (try_end),
                          
                          (val_add, ":acceptance_level", 1500),
                          
                          (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
                          (try_begin),
                            (neq, ":faction_no", "$players_kingdom"),
                            (try_begin),
                              (eq, ":reduce_campaign_ai", 0), #hard
                              (val_add, ":acceptance_level", -1250),
                            (else_try),
                              (eq, ":reduce_campaign_ai", 1), #moderate
                            (else_try),
                              (eq, ":reduce_campaign_ai", 2), #easy
                              (val_add, ":acceptance_level", 1250),
                            (try_end),
                          (else_try),
                            (faction_slot_eq, ":faction_no", slot_faction_marshall, "trp_player"),
                            (try_begin),
                              (eq, ":reduce_campaign_ai", 0), #hard/player's faction
                              (val_add, ":acceptance_level", -1000),
                            (else_try),
                              (eq, ":reduce_campaign_ai", 1), #moderate/player's faction
                              (val_add, ":acceptance_level", -1500),
                            (else_try),
                              (eq, ":reduce_campaign_ai", 2), #easy/player's faction
                              (val_add, ":acceptance_level", -2000),
                            (try_end),
                          (try_end),
                          
                          (troop_get_slot, ":temp_ai_seed", ":troop_no", slot_troop_temp_decision_seed),
                          
                          (le, ":temp_ai_seed", ":acceptance_level"),
                          
                          #Very low opinion of marshall
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s15, "str__i_am_not_accompanying_the_marshal_because_i_fear_that_he_may_lead_us_into_disaster"),
                          (try_end),
                          #Make nuanced, depending on personality type
                        (else_try),
                          (troop_get_slot, ":marshal_controversy", ":faction_marshall", slot_faction_marshall),
                          
                          (lt, ":relation_with_marshall", 0),
                          (ge, ":marshal_controversy", 50),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s15, "str_i_am_not_accompanying_the_marshal_because_i_question_his_judgment"),
                          (try_end),
                        (else_try),
                          (troop_get_slot, ":marshal_controversy", ":faction_marshall", slot_faction_marshall),
                          (neg|faction_slot_eq, ":faction_no", slot_faction_leader, ":faction_marshall"),
                          
                          (lt, ":relation_with_marshall", 5),
                          (ge, ":marshal_controversy", 80),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s15, "str_i_am_not_accompanying_the_marshal_because_will_be_reappointment"),
                          (try_end),
                        (else_try),
                          #(lt, ":relation_with_marshall", 45),
                          #(eq, ":faction_marshall", "trp_player"), #moved below as only effector. Search "think about this".
                          
                          (store_sub, ":relation_with_marshal_difference", 50, ":relation_with_marshall"),
                          
                          #for 50 relation with marshal ":acceptance_level" will be 0
                          #for 20 relation with marshal ":acceptance_level" will be 2100
                          #for 10 relation with marshal ":acceptance_level" will be 2800
                          #for 0 relation with marshal ":acceptance_level" will be 3500
                          #for -10 relation with marshal ":acceptance_level" will be 4200
                          #average is about 2500
                          (store_mul, ":acceptance_level", ":relation_with_marshal_difference", 70),
                          
                          (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
                          (try_begin),
                            (neq, ":faction_no", "$players_kingdom"),
                            
                            (try_begin),
                              (eq, ":reduce_campaign_ai", 0), #hard
                              (val_add, ":acceptance_level", -1200),
                            (else_try),
                              (eq, ":reduce_campaign_ai", 1), #moderate
                            (else_try),
                              (eq, ":reduce_campaign_ai", 2), #easy
                              (val_add, ":acceptance_level", 1200),
                            (try_end),
                          (else_try),
                            (eq, ":faction_marshall", "trp_player"),
                            
                            (try_begin),
                              (eq, ":reduce_campaign_ai", 0), #hard
                              (val_add, ":acceptance_level", -1000),
                            (else_try),
                              (eq, ":reduce_campaign_ai", 1), #moderate
                              (val_add, ":acceptance_level", -1500),
                            (else_try),
                              (eq, ":reduce_campaign_ai", 2), #easy
                              (val_add, ":acceptance_level", -2000),
                            (try_end),
                          (try_end),
                          
                          (try_begin),
                            (eq, ":troop_reputation", lrep_selfrighteous),
                            (val_add, ":acceptance_level", 1500),
                          (else_try),
                            (this_or_next|eq, ":troop_reputation", lrep_martial),
                            (this_or_next|eq, ":troop_reputation", lrep_roguish),
                            (eq, ":troop_reputation", lrep_quarrelsome),
                            (val_add, ":acceptance_level", 1000),
                          (else_try),
                            (eq, ":troop_reputation", lrep_cunning),
                            (val_add, ":acceptance_level", 500),
                          (else_try),
                            (eq, ":troop_reputation", lrep_upstanding), #neutral
                          (else_try),
                            (this_or_next|eq, ":troop_reputation", lrep_benefactor), #helper
                            (eq, ":troop_reputation", lrep_goodnatured),
                            (val_add, ":acceptance_level", -500),
                          (else_try),
                            (eq, ":troop_reputation", lrep_custodian), #very helper
                            (val_add, ":acceptance_level", -1000),
                          (try_end),
                          
                          (try_begin),
                            (troop_slot_eq, ":faction_marshall", slot_lord_reputation_type, lrep_quarrelsome),
                            (val_add, ":acceptance_level", -750),
                          (else_try),
                            (this_or_next|troop_slot_eq, ":faction_marshall", slot_lord_reputation_type, lrep_martial),
                            (troop_slot_eq, ":faction_marshall", slot_lord_reputation_type, lrep_upstanding),
                            (val_add, ":acceptance_level", -250),
                          (try_end),
                          
                          (val_add, ":acceptance_level", 2000),
                          #average become 2500 + 2000 = 4500, (45% of lords will not join campaign because of this reason. (33% for hard, 57% for easy, 30% for marshal player))
                          
                          (troop_get_slot, ":temp_ai_seed", ":troop_no", slot_troop_temp_decision_seed),
                          
                          (le, ":temp_ai_seed", ":acceptance_level"),
                          
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s15, "str_i_am_not_accompanying_the_marshal_because_i_can_do_greater_deeds"),
                          (try_end),
                          
                          #(try_begin),
                          #  (ge, "$cheat_mode", 1),
                          #  (assign, reg7, ":acceptance_level"),
                          #  (assign, reg8, ":relation_with_marshall"),
                          #  (display_message, "@{!}DEBUGS : acceptance level : {reg7}, relation with marshal : {reg8}"),
                          #(try_end),
                        (else_try),
                          (store_current_hours, ":hours_since_last_faction_rest"),
                          (faction_get_slot, ":last_rest_time", ":faction_no", slot_faction_ai_last_rest_time),
                          (val_sub, ":hours_since_last_faction_rest", ":last_rest_time"),
                          
                          #nine days on average, marshal will usually end after 10 days
                          #ozan changed, 360 hours (15 days) in average, marshal cannot end it during a siege attack/defence anymore.
                          (assign, ":troop_campaign_limit", 360),
                          (store_mul, ":marshal_relation_modifier", ":relation_with_marshall", 6), #ozan changed 4 to 6.
                          (val_add, ":troop_campaign_limit", ":marshal_relation_modifier"),
                          
                          (try_begin),
                            (eq, ":troop_reputation", lrep_upstanding),
                            (val_mul, ":troop_campaign_limit", 4),
                            (val_div, ":troop_campaign_limit", 3),
                          (try_end),
                          
                          (str_store_troop_name, s16, ":faction_marshall"),
                          
                          (gt, ":hours_since_last_faction_rest", ":troop_campaign_limit"),
                          
                          #Too long a campaign
                          (try_begin),
                            (eq, ":troop_no", "$g_talk_troop"),
                            (str_store_string, s15, "str__s16_has_kept_us_on_campaign_on_far_too_long_and_there_are_other_pressing_matters_to_which_i_must_attend"),
                          (try_end),
                          #Also make nuanced, depending on personality type
                        (else_try),
                          (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
                          (neg|party_is_active, ":party_no"),
                          #This string should not occur, as it will only happen if a lord is contemplating following the player
                        (else_try),
                          (troop_get_slot, ":marshal_party", ":faction_marshall", slot_troop_leaded_party),
                          
                          (assign, ":information_radius", 40),
                          (try_begin),
                            (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_gathering_army),
                            (assign, ":information_radius", 50),
                          (try_end),
                          
						(game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
						(try_begin),
						  (neq, ":faction_no", "fac_player_supporters_faction"),
						  (neq, ":faction_no", "$players_kingdom"),
						  ##diplomacy start+ the player may be able to become leader in other situations
						  (neg|faction_slot_eq, ":faction_no", slot_faction_leader, "trp_player"),
						  ##diplomacy end+
						  (try_begin),
							(eq, ":reduce_campaign_ai", 2), #easy
							(try_begin),
							  (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_gathering_army),
							  (val_add, ":information_radius", -10),
							(else_try),
							  (val_add, ":information_radius", -8),
							(try_end),
						  (else_try),
							(eq, ":reduce_campaign_ai", 1), #moderate
							(try_begin),
							  (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_gathering_army),
							  (val_add, ":information_radius", -5),
							(else_try),
							  (val_add, ":information_radius", -4),
							(try_end),
						  (try_end),
						(else_try),
						  (try_begin),
							(eq, ":reduce_campaign_ai", 2), #easy
							(try_begin),
							  (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_gathering_army),
							  (val_add, ":information_radius", 25),
							(else_try),
							  (val_add, ":information_radius", 20),
							(try_end),
						  (else_try),
							(eq, ":reduce_campaign_ai", 1), #moderate
							(try_begin),
							  (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_gathering_army),
							  (val_add, ":information_radius", 15),
							(else_try),
							  (val_add, ":information_radius", 12),
							(try_end),
						  (else_try),
							(eq, ":reduce_campaign_ai", 0), #hard
							(try_begin),
							  (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_gathering_army),
							  (val_add, ":information_radius", 5),
							(else_try),
							  (val_add, ":information_radius", 4),
							(try_end),
						  (try_end),
						(try_end),

						(faction_get_slot, ":faction_object", ":faction_no", slot_faction_ai_object),
						(assign, reg17, 0),
						(try_begin),
						  (try_begin),
							(neg|is_between, ":faction_object", villages_begin, villages_end),
							(assign, reg17, 1),
						  (try_end),
						  (try_begin),
							(neg|faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_attacking_enemies_around_center),
							(assign, reg17, 1),
						  (try_end),
						  (eq, reg17, 1),

						  (store_distance_to_party_from_party, ":distance", ":marshal_party", ":party_no"),

						  (gt, ":distance", ":information_radius"),

						  (try_begin),
							(eq, ":troop_no", "$g_talk_troop"),
							(str_store_string, s15, "str__i_am_not_participating_in_the_marshals_campaign_because_i_do_not_know_where_to_find_our_main_army"),
						  (try_end),
						(else_try),
						  (eq, reg17, 0),

						  (assign, reg17, 1),
						  (try_begin),
							#if we are already accompanying marshal forget below.
							(party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
							(party_slot_eq, ":party_no", slot_party_ai_object, ":marshal_party"),
							(assign, reg17, 0),
						  (try_end),
						  (eq, reg17, 1),

						  #if faction ai is "attacking enemies around a center" is then do not find and compare distance to marshal, find and compare distance to "attacked village"
						  (party_get_slot, ":enemy_strength_nearby", ":faction_object", slot_center_sortie_enemy_strength),

						  (try_begin), #changes between 70..x (as ":enemy_strength_nearby" increases, ":information_radius" increases too.),
							(ge, ":enemy_strength_nearby", 4000),
							(val_sub, ":enemy_strength_nearby", 4000),
							(store_div, ":information_radius", ":enemy_strength_nearby", 200),
							(val_add, ":information_radius", 70),
						  (else_try), #changes between 30..70
							(store_div, ":information_radius", ":enemy_strength_nearby", 100),
							(val_add, ":information_radius", 30),
						  (try_end),

						  (store_distance_to_party_from_party, ":distance", ":faction_object", ":party_no"),

						  (gt, ":distance", ":information_radius"),

						  (try_begin),
							(eq, ":troop_no", "$g_talk_troop"),
							(str_store_string, s15, "str__i_am_acting_independently_although_some_enemies_have_been_spotted_within_our_borders_they_havent_come_in_force_and_the_local_troops_should_be_able_to_dispatch_them"),
						  (try_end),
						(try_end),

						(gt, ":distance", ":information_radius"),
					(else_try),
						(try_begin),
						  (eq, ":troop_no", "$g_talk_troop"),
						  (str_store_string, s15, "str__the_needs_of_the_realm_must_come_first"),
						(try_end),
						(assign, ":result", 1),
					(try_end),

					(assign, reg0, ":result"),
					]),
                    
                    #script_find_total_prosperity_score
                    # INPUT: center_no
                    # OUTPUT: reg0 = total_prosperity_score
                    (
                      "find_total_prosperity_score",
                      [
                        (store_script_param, ":center_no", 1),
                        
                        (try_begin), #":total_prosperity_score" changes between 10..100
                          (is_between, ":center_no", walled_centers_begin, walled_centers_end),
                          
                          (party_get_slot, ":center_prosperity", ":center_no", slot_town_prosperity),
                          (store_add, ":center_prosperity_add_200_div_10", ":center_prosperity", 200),
                          (val_div, ":center_prosperity_add_200_div_10", 10),
                          (try_begin),
                            (is_between, ":center_no", towns_begin, towns_end),
                            (store_mul, ":this_center_score", ":center_prosperity_add_200_div_10", 15),
                          (else_try),
                            (store_mul, ":this_center_score", ":center_prosperity_add_200_div_10", 5),
                          (try_end),
                          (assign, ":total_prosperity_score", ":this_center_score"),
                          
                          (try_for_range_backwards, ":village_no", villages_begin, villages_end),
                            (party_slot_eq, ":village_no", slot_village_bound_center, ":center_no"),
                            
                            (party_get_slot, ":village_prosperity", ":village_no", slot_town_prosperity),
                            (store_add, ":village_prosperity_add_200_div_10", ":village_prosperity", 200),
                            (val_div, ":village_prosperity_add_200_div_10", 10),
                            (store_mul, ":this_village_score", ":village_prosperity_add_200_div_10", 5),
                            
                            (val_add, ":total_prosperity_score", ":this_village_score"),
                          (try_end),
                        (else_try),
                          (party_get_slot, ":center_prosperity", ":center_no", slot_town_prosperity),
                          (store_add, ":center_prosperity_add_200_div_10", ":center_prosperity", 200),
                          (val_div, ":center_prosperity_add_200_div_10", 10),
                          (store_mul, ":this_center_score", ":center_prosperity_add_200_div_10", 5),
                          (assign, ":total_prosperity_score", ":this_center_score"),
                        (try_end),
                        (val_div, ":total_prosperity_score", 10),
                        
                        (assign, reg0, ":total_prosperity_score"),
                    ]),
                    
                    #script_calculate_center_assailability_score
                    # INPUT: faction_no
                    # param1: faction_no
                    # param2: all_vassals_included, (becomes 1 if we want to find attackable center if we collected 20% of vassals during gathering army phase)
                    # OUTPUT:
                    # reg0 = center_to_attack (-1 if none is logical)
                    # reg1 = maximum_attack_score
                    (
                      "calculate_center_assailability_score",
                      [
                        (store_script_param, ":troop_no", 1),
                        (store_script_param, ":potential_target", 2),
                        (store_script_param, ":all_vassals_included", 3),
                        
                        (assign, ":target_score", -1),
                        
                        (store_faction_of_troop, ":faction_no", ":troop_no"),
                        
                        (store_current_hours, ":hours_since_last_offensive"),
                        (faction_get_slot, ":last_offensive_time", ":faction_no", slot_faction_last_offensive_concluded),
                        (val_sub, ":hours_since_last_offensive", ":last_offensive_time"),
                        
                        (store_div, ":last_offensive_time_score", ":hours_since_last_offensive", 12), #30..50
                        (val_add, ":last_offensive_time_score", 30),
                        (val_min, ":last_offensive_time_score", 100),
                        
                        (faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
                        
                        (assign, ":marshal_party", -1),
                        (assign, ":marshal_strength", 0),
                        #(assign, ":strength_of_nearby_friend", 0),
                        
                        (try_begin),
                          (gt, ":faction_marshal", 0),
                          (troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
                          (party_is_active, ":marshal_party"),
                          (party_get_slot, ":marshal_strength", ":marshal_party", slot_party_cached_strength),
                          #(eq, ":all_vassals_included", 0),
                          (party_get_slot, ":strength_of_current_followers", ":marshal_party", slot_party_follower_strength),
                          #(party_get_slot, ":strength_of_nearby_friend", ":marshal_party", slot_party_nearby_friend_strength),
                        (try_end),
                        
                        #(try_begin),
                        #  (eq, ":all_vassals_included", 0),
                        #
                        #  (try_begin),
                        #    (gt, ":faction_marshal", 0),
                        #    (troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
                        #    (party_is_active, ":marshal_party"),
                        #    (party_get_slot, ":strength_of_potential_followers", ":marshal_party", slot_party_follower_strength),
                        #  (try_end),
                        #(else_try),
                        #  (eq, ":all_vassals_included", 1),
                        #
                        #  (assign, ":strength_of_potential_followers", 0),
                        #
                        #  (try_for_parties, ":party_no"),
                        #    (store_faction_of_party, ":party_faction", ":party_no"),
                        #    (eq, ":party_faction", ":faction_no"),
                        #    (neq, ":party_no", ":marshal_party"),
                        #    (party_slot_eq, ":party_no", slot_party_type, spt_kingdom_hero_party),
                        #    (call_script, "script_party_calculate_strength", ":party_no", 0),
                        #    (val_add, ":strength_of_potential_followers", reg0),
                        #  (try_end),
                        #
                        #  (val_div, ":strength_of_potential_followers", 2), #Ozan - Think about this, will you divide strength_of_potential_followers to 3 or 2.5 or 2
                        #(else_try),
                        #  (assign, ":strength_of_potential_followers", 0),
                        #(try_end),
                        
                        (faction_get_slot, ":last_attacked_center", ":faction_no", slot_faction_last_attacked_center),
                        (faction_get_slot, ":last_attacked_hours", ":faction_no", slot_faction_last_attacked_hours),
                        
                        (try_begin),
                          (store_current_hours, ":hours"),
                          (store_add, ":last_attacked_hours_plus_24", ":last_attacked_hours", 24),
                          (gt, ":hours", ":last_attacked_hours_plus_24"),
                          (faction_set_slot, ":faction_no", slot_faction_last_attacked_center, 0),
                          (assign, ":last_attacked_center", 0),
                        (try_end),
                        
                        (try_begin),
                          (this_or_next|eq, ":last_attacked_center", 0),
                          (this_or_next|eq, ":last_attacked_center", ":potential_target"),
                          (this_or_next|eq, "$g_do_not_skip_other_than_current_ai_object", 1),
                          (neg|faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
                          
                          (party_is_active, ":potential_target"),
                          (store_faction_of_party, ":potential_target_faction", ":potential_target"),
                          
                          (store_relation, ":relation", ":potential_target_faction", ":faction_no"),
                          (lt, ":relation", 0),
                          
                          #attack if and only if we are already besieging that center or anybody do not making besiege.
                          (assign, ":faction_of_besieger_party", -1),
                          (try_begin),
                            (is_between, ":potential_target", walled_centers_begin, walled_centers_end),
                            (neg|party_slot_eq, ":potential_target", slot_center_is_besieged_by, -1),
                            (party_get_slot, ":besieger_party", ":potential_target", slot_center_is_besieged_by),
                            (party_is_active, ":besieger_party"),
                            (store_faction_of_party, ":faction_of_besieger_party", ":besieger_party"),
                          (try_end),
                          
                          (this_or_next|eq, ":faction_of_besieger_party", -1),
                          (eq, ":faction_of_besieger_party", ":faction_no"),
                          
                          #attack if and only if this center is not a village or if it is village it should not be raided or looted
                          (assign, ":village_is_looted_or_raided_already", 0),
                          (try_begin),
                            (is_between, ":potential_target", villages_begin, villages_end),
                            (try_begin),
                              (party_slot_eq, ":potential_target", slot_village_state, svs_being_raided),
                              (party_get_slot, ":raider_party", ":potential_target", slot_village_raided_by),
                              (party_is_active, ":raider_party"),
                              
                              (store_faction_of_party, ":raider_faction", ":raider_party"),
                              (neq, ":raider_faction", ":faction_no"),
                              (assign, ":raiding_by_one_other_faction", 1),
                            (else_try),
                              (assign, ":raiding_by_one_other_faction", 0),
                            (try_end),
                            (this_or_next|party_slot_eq, ":potential_target", slot_village_state, svs_looted),
                            (eq, ":raiding_by_one_other_faction", 1),
                            (assign, ":village_is_looted_or_raided_already", 1),
                          (try_end),
                          (eq, ":village_is_looted_or_raided_already", 0),
                          
                          #if ":potential_target" is faction object of some other faction which is enemy to owner of
                          #":potential_target" then this target cannot be new target we are looking for.
                          (assign, ":this_potantial_target_is_target_of_some_other_faction", 0),
                          (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
                            (is_between, ":cur_faction", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
                            (neq, ":cur_faction", ":faction_no"),
                            (faction_get_slot, ":faction_object", ":cur_faction", slot_faction_ai_object),
                            (eq, ":faction_object", ":potential_target"),
                            (store_relation, ":rel", ":potential_target_faction", ":cur_faction"),
                            (lt, ":rel", 0),
                            (assign, ":this_potantial_target_is_target_of_some_other_faction", 1),
                          (try_end),
                          (eq, ":this_potantial_target_is_target_of_some_other_faction", 0),
                          
                          (try_begin),
                            (is_between, ":potential_target", walled_centers_begin, walled_centers_end),
                            (party_get_slot, ":potential_target_inside_strength", ":potential_target", slot_party_cached_strength),
                            (party_get_slot, ":potential_target_nearby_enemy_strength", ":potential_target", slot_party_nearby_friend_strength),
                            (val_div, ":potential_target_nearby_enemy_strength", 2),
                            (store_add, ":potential_target_strength", ":potential_target_inside_strength", ":potential_target_nearby_enemy_strength"),
                            
                            #(try_begin),
                            #(eq, ":faction_no", "fac_kingdom_4"),
                            #(assign, reg0, ":potential_target_inside_strength"),
                            #(assign, reg1, ":potential_target_nearby_enemy_strength"),
                            #(assign, reg2, ":marshal_strength"),
                            #(assign, reg3, ":strength_of_potential_followers"),
                            #(assign, reg4, ":strength_of_nearby_friend"),
                            #(assign, reg6, ":marshal_party"),
                            #(str_store_party_name, s8, ":potential_target"),
                            #(eq, ":all_vassals_included", 0),
                            #(display_message, "@DEBUG : {s8}:{reg0}, neare {reg1}, our {reg2}, follow {reg3}, nearf {reg4}"),
                            #(try_end),
                            
                            (val_mul, ":potential_target_strength", 4), #in walled centers defenders have advantage.
                            (val_div, ":potential_target_strength", 3),
                            
                            #(store_add, ":army_strength", ":marshal_strength", ":strength_of_potential_followers"),
                            (assign, ":army_strength", ":marshal_strength"),
                            (val_add, ":army_strength", ":strength_of_current_followers"),
                            (store_mul, ":power_ratio", ":army_strength", 100),
                            
                            #this ratio ":power_ratio" shows (our total army power) / (their total army power)
                            (try_begin),
                              (gt, ":potential_target_strength", 0),
                              (val_div, ":power_ratio", ":potential_target_strength"),
                            (else_try),
                              (assign, ":power_ratio", 1000),
                            (try_end),
                          (else_try),
                            (party_get_slot, ":potential_target_nearby_enemy_strength", ":potential_target", slot_party_nearby_friend_strength),
                            (assign, ":potential_target_strength", 1000),
                            
                            #(store_add, ":army_strength", ":marshal_strength", ":strength_of_potential_followers"),
                            (assign, ":army_strength", ":marshal_strength"),
                            (val_add, ":army_strength", ":strength_of_current_followers"),
                            (store_mul, ":power_ratio", ":army_strength", 100),
                            
                            (try_begin),
                              (gt, ":potential_target_strength", 0),
                              (val_div, ":power_ratio", ":potential_target_strength"),
                            (else_try),
                              (assign, ":power_ratio", 1000),
                            (try_end),
                          (try_end),
                          
                          (ge, ":power_ratio", 120), #attack if and only if our army is at least 1.2 times powerfull
                          (store_sub, ":power_ratio_sub_120", ":power_ratio", 120),
                          
                          (try_begin),
                            (lt, ":power_ratio_sub_120", 100), #changes between 20..120
                            (store_add, ":power_ratio_score", ":power_ratio_sub_120", 20),
                          (else_try),
                            (lt, ":power_ratio_sub_120", 200), #changes between 120..170
                            (store_sub, ":power_ratio_score", ":power_ratio_sub_120", 100),
                            (val_div, ":power_ratio_score", 2),
                            (val_add, ":power_ratio_score", 120),
                          (else_try),
                            (lt, ":power_ratio_sub_120", 400), #changes between 170..210
                            (store_sub, ":power_ratio_score", ":power_ratio_sub_120", 200),
                            (val_div, ":power_ratio_score", 5),
                            (val_add, ":power_ratio_score", 170),
                          (else_try),
                            (lt, ":power_ratio_sub_120", 800), #changes between 210..250
                            (store_sub, ":power_ratio_score", ":power_ratio_sub_120", 400),
                            (val_div, ":power_ratio_score", 10),
                            (val_add, ":power_ratio_score", 210),
                          (else_try),
                            (assign, ":power_ratio_score", 250),
                          (try_end),
                          
                          (assign, ":number_of_walled_centers", 0),
                          (assign, ":total_distance", 0),
                          (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
                            (store_faction_of_party, ":walled_center_faction", ":walled_center"),
                            (eq, ":walled_center_faction", ":faction_no"),
                            
                            (store_distance_to_party_from_party, ":dist", ":walled_center", ":potential_target"),
                            (val_add, ":total_distance", ":dist"),
                            
                            (val_add, ":number_of_walled_centers", 1),
                          (try_end),
                          
                          (try_begin),
                            (gt, ":number_of_walled_centers", 0),
                            (store_div, ":average_distance", ":total_distance", ":number_of_walled_centers"),
                            #(assign, reg0, ":average_distance"),
                            #(str_store_faction_name, s7, ":faction_no"),
                            #(str_store_party_name, s8, ":potential_target"),
                            #(display_message, "@average distance for {s7} for {s8} is {reg0}"),
                            
                            (try_begin),
                              (ge, ":marshal_party", 0),
                              (party_is_active, ":marshal_party"),
                              (store_distance_to_party_from_party, ":marshal_dist_to_potential_target", ":marshal_party", ":potential_target"),
                            (else_try),
                              (assign, ":marshal_dist_to_potential_target", 100),
                            (try_end),
                            
                            (try_begin),
							#if currently main aim of our faction is attacking to an enemy center and that center is already besieged/raided by one of 				#	1.143 Port // New commentary
							#our parties then divide marshal_dist_to_potential_target_div_x score for current center to "3/2" instead of "3" and this
							#result in decrease at distance_score, and also decrease some scores from power_ratio_score in order to avoid frequently 
							#changes at main aimed target city of our faction during sieges.

                              
                              (faction_get_slot, ":current_ai_state", ":faction_no", slot_faction_ai_state),
                              (eq, ":current_ai_state", sfai_attacking_center),
                              (faction_get_slot, ":current_ai_object", ":faction_no", slot_faction_ai_object),
                              
                              (ge, ":current_ai_object", 0),
                              (neq, ":current_ai_object", ":potential_target"),
                              
                              (try_begin),
                                (ge, ":power_ratio_score", 300), #200 max
                                (assign, ":power_ratio_score", 200),
                              (else_try),
                                (ge, ":power_ratio_score", 100), #100..200
                                (val_sub, ":power_ratio_score", 100),
                                (val_div, ":power_ratio_score", 2),
                                (val_add, ":power_ratio_score", 100),
                              (try_end),
                              
                              (try_begin),
                                (faction_slot_eq, ":faction_no", slot_faction_marshall, ":troop_no"),
                                (eq, "$g_do_not_skip_other_than_current_ai_object", 0),
                                (assign, ":power_ratio_score", 0), #lets completely forget all other choices if we are already besieging one center.
                              (try_end),
                              
                              (faction_set_slot, ":faction_no", slot_faction_last_attacked_center, ":current_ai_object"),
                              (store_current_hours, ":hours"),
                              (faction_set_slot, ":faction_no", slot_faction_last_attacked_hours, ":hours"),
                              
                              (eq, ":all_vassals_included", 0),
                              
								(store_mul, ":marshal_dist_to_potential_target_div_x", ":marshal_dist_to_potential_target", 2),			#	1.143 Port // see native 1.134
								(val_div, ":marshal_dist_to_potential_target_div_x", 3),												#	1.143 Port // see native 1.134
                            (else_try),
                              (store_div, ":marshal_dist_to_potential_target_div_x", ":marshal_dist_to_potential_target", 3),
                            (try_end),
                            
                            (store_add, ":total_distance", ":average_distance", ":marshal_dist_to_potential_target_div_x"), #in average ":total_distance" is about 150, min : 0, max : 1000
                          (else_try),
                            (assign, ":total_distance", 100),
                          (try_end),
                          
                          (try_begin),
							  #according to cautious troop distance is more important
							  ##diplomacy start+ Take into account lady & companion personality types
							  ##OLD:
							  #(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
							  #(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
							  #(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
							  #(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
							  #
							  ##NEW:
							  (call_script, "script_dplmc_store_troop_personality_caution_level", ":troop_no"),
							  (assign, ":troop_caution", reg0),
							  (gt, ":troop_caution", 0),
							  ##diplomacy end+
                            
                            (try_begin),
                              (lt, ":total_distance", 30), #very close (100p)
                              (assign, ":distance_score", 100),
                            (else_try),
                              (lt, ":total_distance", 80), #close (50p-100p)
                              (store_sub, ":distance_score", ":total_distance", 30),
                              (val_div, ":distance_score", 1),
                              (store_sub, ":distance_score", 100, ":distance_score"),
                            (else_try),
                              (lt, ":total_distance", 160), #far (10p-50p)
                              (store_sub, ":distance_score", ":total_distance", 80),
                              (val_div, ":distance_score", 2),
                              (store_sub, ":distance_score", 50, ":distance_score"),
                            (else_try),
                              (assign, ":distance_score", 10), #very far
                            (try_end),
                          (else_try),
                            #according to agressive troop distance is less important
                            
                            (try_begin),
                              (lt, ":total_distance", 40), #very close (100p)
                              (assign, ":distance_score", 100),
                            (else_try),
                              (lt, ":total_distance", 140), #close (50p-100p)
                              (store_sub, ":distance_score", ":total_distance", 40),
                              (val_div, ":distance_score", 2),
                              (store_sub, ":distance_score", 100, ":distance_score"),
                            (else_try),
                              (lt, ":total_distance", 300), #far (10p-50p)
                              (store_sub, ":distance_score", ":total_distance", 140),
                              (val_div, ":distance_score", 4),
                              (store_sub, ":distance_score", 50, ":distance_score"),
                            (else_try),
                              (assign, ":distance_score", 10), #very far
                            (try_end),
					   (try_end),
						##diplomacy start+ If AI changes are enabled, reduce distance penalty (increase score)
						##for recently-lost fiefs.
						(try_begin),
							(lt, ":distance_score", 100),
							(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
							(party_slot_eq, ":potential_target", slot_center_ex_faction, ":faction_no"),
							(party_get_slot, reg0, ":potential_target", dplmc_slot_center_last_transfer_time),
							(gt, reg0, 0),#0 means the slot was uninitialized.  A negative number would be before the start of the game.
							(store_current_hours, ":hours_since_transfer"),
							(val_sub, ":hours_since_transfer", reg0),
							(try_begin),
								(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_HIGH),
								(assign, reg0, 24 * 21),#within last three weeks
							(else_try),
								(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
								(assign, reg0, 24 * 14),#within last two weeks
							(else_try),
								(assign, reg0, 24 * 7),#within last week
							(try_end),
							(lt, ":hours_since_transfer", reg0),
							(val_add, ":distance_score", 100),
							(val_div, ":distance_score", 2),
						(try_end),
						##diplomacy end+
                          
                          (store_mul, ":target_score", ":distance_score", ":power_ratio_score"),
                          (val_mul, ":target_score", ":last_offensive_time_score"),
                          (val_div, ":target_score", 100), #target score is between 0..10000 generally here
                          
                          (call_script, "script_find_total_prosperity_score", ":potential_target"),
                          (assign, ":total_prosperity_score", reg0),
                          
                          #(try_begin), #new for increase attackability of villages by ai
                          #(is_between, ":potential_target", villages_begin, villages_end),
                          (val_mul, ":total_prosperity_score", 3),
                          (val_div, ":total_prosperity_score", 2),
                          #(try_end),
                          
                          (val_mul, ":target_score", ":total_prosperity_score"),
                          
                          (try_begin), #if both that center was our (original center) and (ex center) than bonus is 1.2x
                            (party_slot_eq, ":potential_target", slot_center_ex_faction, ":faction_no"),
                            (party_slot_eq, ":potential_target", slot_center_original_faction, ":faction_no"),
                            (val_mul, ":target_score", 12),
                            (val_div, ":target_score", 10),
                          (else_try), #if either that center was our (original center) or (ex center) than bonus is 1.1x
                            (this_or_next|party_slot_eq, ":potential_target", slot_center_ex_faction, ":faction_no"),
                            (party_slot_eq, ":potential_target", slot_center_original_faction, ":faction_no"),
                            (val_mul, ":target_score", 11),
                            (val_div, ":target_score", 10),
                          (try_end),
                          
                          (val_div, ":target_score", 1000), #target score is between 0..1000 generally here
                          
                          (try_begin),
                            (eq, ":potential_target_faction", "fac_player_supporters_faction"),
                            (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
                            
                            (assign, ":number_of_walled_centers_player_have", 0),
                            (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
                              (store_faction_of_party, ":center_faction", ":center_no"),
                              (eq, ":center_faction", "fac_player_supporters_faction"),
                              (val_add, ":number_of_walled_centers_player_have", 1),
                            (try_end),
                            
                            (try_begin),
                              (eq, ":reduce_campaign_ai", 2), #easy
                              
                              (try_begin),
                                (le, ":number_of_walled_centers_player_have", 2),
                                (assign, ":hardness_score", 0),
                              (else_try),
                                (eq, ":number_of_walled_centers_player_have", 3),
                                (assign, ":hardness_score", 20),
                              (else_try),
                                (eq, ":number_of_walled_centers_player_have", 4),
                                (assign, ":hardness_score", 40),
                              (else_try),
                                (eq, ":number_of_walled_centers_player_have", 5),
                                (eq, ":number_of_walled_centers_player_have", 6),
                                (assign, ":hardness_score", 55),
                              (else_try),
                                (eq, ":number_of_walled_centers_player_have", 7),
                                (eq, ":number_of_walled_centers_player_have", 8),
                                (eq, ":number_of_walled_centers_player_have", 9),
                                (assign, ":hardness_score", 70),
                              (else_try),
                                (assign, ":hardness_score", 85),
                              (try_end),
                            (else_try),
                              (eq, ":reduce_campaign_ai", 1), #medium
                              
                              (try_begin),
                                (le, ":number_of_walled_centers_player_have", 1),
                                (assign, ":hardness_score", 25),
                              (else_try),
                                (eq, ":number_of_walled_centers_player_have", 2),
                                (assign, ":hardness_score", 45),
                              (else_try),
                                (eq, ":number_of_walled_centers_player_have", 3),
                                (assign, ":hardness_score", 60),
                              (else_try),
                                (eq, ":number_of_walled_centers_player_have", 4),
                                (eq, ":number_of_walled_centers_player_have", 5),
                                (assign, ":hardness_score", 75),
                              (else_try),
                                (eq, ":number_of_walled_centers_player_have", 6),
                                (eq, ":number_of_walled_centers_player_have", 7),
                                (eq, ":number_of_walled_centers_player_have", 8),
                                (assign, ":hardness_score", 85),
                              (else_try),
                                (assign, ":hardness_score", 92),
                              (try_end),
                            (else_try), #hard
                              (assign, ":hardness_score", 100),
                            (try_end),
                            
                            (val_mul, ":target_score", ":hardness_score"),
                            (val_div, ":target_score", 100),
                          (try_end),
                          
                          (try_begin),
                            (ge, "$cheat_mode", 1),
                            (eq, ":faction_no", "fac_kingdom_4"),
                            (ge, ":target_score", -1),
                            (assign, reg0, ":target_score"),
                            (assign, reg7, ":total_prosperity_score"),
                            (assign, reg8, ":power_ratio_score"),
                            (assign, reg9, ":distance_score"),
                            (assign, reg10, ":last_offensive_time_score"),
                            (str_store_party_name, s8, ":potential_target"),
                            #(eq, ":all_vassals_included", 0),
                            (assign, reg11, ":all_vassals_included"),
                            #(display_message, "@DEBUG : attack of {s8} is {reg0}({reg11}), prs:{reg7}, pow:{reg8}, dis:{reg9}, lst:{reg10}"),
                          (try_end),
                        (try_end),
                        
                        (assign, reg0, ":target_score"),
                        (assign, reg1, ":power_ratio"),
                        (assign, reg2, ":distance_score"),
                        (assign, reg3, ":total_prosperity_score"),
                    ]),
                    
                    #script_find_center_to_defend
                    # INPUT:
                    # param1: faction_no
                    # OUTPUT:
                    # reg0 = center_to_defend (-1 if none is logical)
                    # reg1 = maximum_defend_score
                    # reg3 = enemy_strength_near_most_threatened_center
                    (
                      "find_center_to_defend",
                      [
                        (store_script_param, ":troop_no", 1),
                        
                        (store_faction_of_troop, ":faction_no", ":troop_no"),
                        
                        (faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
                        (faction_get_slot, ":current_ai_state", ":faction_no", slot_faction_ai_state),
                        (assign, ":marshal_party", -1),
                        (try_begin),
                          (gt, ":faction_marshal", 0),
                          (troop_get_slot, ":marshal_party", ":faction_marshal", slot_troop_leaded_party),
                        (try_end),
                        
                        (assign, ":most_threatened_center", -1),
                        (assign, ":maximum_threat_score", 0),
                        (try_for_range, ":cur_center", centers_begin, centers_end),
                          (store_faction_of_party, ":center_faction", ":cur_center"),
                          (eq, ":center_faction", ":faction_no"),
                          
                          (party_get_slot, ":exact_enemy_strength", ":cur_center", slot_center_sortie_enemy_strength),
                          #Distort this to account for questionable intelligence
                          #(call_script, "script_reduce_exact_number_to_estimate", ":exact_enemy_strength"),
                          #(assign, ":enemy_strength_nearby", reg0),
                          (assign, ":enemy_strength_nearby", ":exact_enemy_strength"),
                          
                          (assign, ":threat_importance", 0),
                          (try_begin),
                            (is_between, ":cur_center", walled_centers_begin, walled_centers_end),
                            (party_slot_ge, ":cur_center", slot_center_is_besieged_by, 0),
                            
                            (call_script, "script_find_total_prosperity_score", ":cur_center"),
                            (assign, ":total_prosperity_score", reg0),
                            
                            (party_get_slot, ":cur_center_strength", ":cur_center", slot_party_cached_strength),
                            (val_mul, ":cur_center_strength", 4),
                            (val_div, ":cur_center_strength", 3), #give 33% bonus to insiders because they are inside a castle
                            
                            #I removed below line and assigned ":cur_center_nearby_strength" to 0, because if not when defender army comes to help
                            #threat become less because of high defence power but not yet enemy cleared.
                            #(party_get_slot, ":cur_center_nearby_strength", ":cur_center", slot_party_nearby_friend_strength),
                            (assign, ":cur_center_nearby_strength", 0),
                            
                            (val_add, ":cur_center_strength", ":cur_center_nearby_strength"), #add nearby friends and find ":cur_center_strength"
                            
                            (store_mul, ":power_ratio", ":enemy_strength_nearby", 100),
                            (val_add, ":cur_center_strength", 1),
                            (val_max, ":cur_center_strength", 1),
                            (val_div, ":power_ratio", ":cur_center_strength"),
                            
                            (assign, ":player_is_attacking", 0),
                            (party_get_slot, ":besieger_party", ":cur_center", slot_center_is_besieged_by),
                            (try_begin),
                              (party_is_active, ":besieger_party"),
                              (try_begin),
                                (eq, ":besieger_party", "p_main_party"),
                                (assign, ":player_is_attacking", 1),
                                #(display_message, "@{!}DEBUG : player is attacking a center (1)"),
                              (else_try),
                                (store_faction_of_party, ":besieger_faction", ":besieger_party"),
                                (eq, ":besieger_faction", "fac_player_faction"),
                                (assign, ":player_is_attacking", 1),
                                #(display_message, "@{!}DEBUG : player is attacking a center (2)"),
                              (else_try),
                                (party_get_attached_to, ":player_is_attached_to", "p_main_party"),
                                (ge, ":player_is_attached_to", 0),
                                (eq, ":player_is_attached_to", ":besieger_party"),
                                (assign, ":player_is_attacking", 1),
                                #(display_message, "@{!}DEBUG : player is attacking a center (3)"),
                              (try_end),
                            (try_end),
                            
                            (try_begin),
                              (eq, ":player_is_attacking", 0),
                              
                              (try_begin),
                                (lt, ":power_ratio", 40), #changes between 1..1
                                (assign, ":threat_importance", 1),
                              (else_try),
                                (lt, ":power_ratio", 80), #changes between 1..7
                                (store_sub, ":threat_importance", ":power_ratio", 40),
                                (val_div, ":threat_importance", 5),
                                (val_add, ":threat_importance", 1), #1
                              (else_try),
                                (lt, ":power_ratio", 120), #changes between 7..17
                                (store_sub, ":threat_importance", ":power_ratio", 80),
                                (val_div, ":threat_importance", 4),
                                (val_add, ":threat_importance", 7), #1 + 6
                              (else_try),
                                (lt, ":power_ratio", 200),
                                (store_sub, ":threat_importance", ":power_ratio", 120),
                                (val_div, ":threat_importance", 10),
                                (val_add, ":threat_importance", 17), #1 + 6 + 10
                              (else_try),
                                (assign, ":threat_importance", 25),
                              (try_end),
                            (else_try),
                              (try_begin),
                                (lt, ":power_ratio", 200), #changes between 5..25
                                (store_div, ":threat_importance", ":power_ratio", 10),    #MOTO correction (thanks MOTO:) (mexxico))
                                (val_add, ":threat_importance", 6 ),
                              (else_try),
                                (assign, ":threat_importance", 26),
                              (try_end),
                            (try_end),
                          (else_try),
                            (is_between, ":cur_center", villages_begin, villages_end),
                            (party_slot_eq, ":cur_center", slot_village_state, svs_being_raided),
                            
                            (gt, ":enemy_strength_nearby", 0),
                            
                            (call_script, "script_find_total_prosperity_score", ":cur_center"),
                            (assign, ":power_ratio", 100), #useless
                            (assign, ":total_prosperity_score", reg0),
                            (assign, ":threat_importance", 10), #if faction village is looted they lose money for shorter time period. So importance is something low (6-8).
                          (try_end),
                          
                          (gt, ":threat_importance", 0),
                          
                          (try_begin),
                            (is_between, ":cur_center", walled_centers_begin, walled_centers_end),
                            (assign, ":enemy_strength_nearby_score", 120),
                            
                            (try_begin),
                              (ge, ":marshal_party", 0),
                              (party_is_active, ":marshal_party"),
                              (store_distance_to_party_from_party, ":marshal_dist_to_cur_center", ":marshal_party", ":cur_center"),
                            (else_try),
                              (assign, ":marshal_dist_to_cur_center", 100),
                            (try_end),
                            
                            (try_begin),
                              #if currently our target is ride to break a siege then
                              #divide marshal_distance for other center's to "2" instead of "4" and add some small more distance to avoid easily
                              #changing mind during siege because of small score differences.
                              
                              #(faction_get_slot, ":current_ai_state", ":faction_no", slot_faction_ai_state),
                              (eq, ":current_ai_state", sfai_attacking_enemies_around_center),
                              (faction_get_slot, ":current_ai_object", ":faction_no", slot_faction_ai_object),
                              (is_between, ":current_ai_object", walled_centers_begin, walled_centers_end),
                              (neq, ":current_ai_object", ":cur_center"),
                              (val_mul, ":marshal_dist_to_cur_center", 2),
                              (val_add, ":marshal_dist_to_cur_center", 20),
                            (try_end),
                            
                            (val_mul, ":marshal_dist_to_cur_center", 2), #standard multipication (1.5x) to adjust distance scoring same with formula at find_center_to_attack
                            #(val_div, ":marshal_dist_to_cur_center", 2),
                            
                            (try_begin),
                              (lt, ":marshal_dist_to_cur_center", 10), #very close (100p)
                              (assign, ":distance_score", 100),
                            (else_try),
                              (lt, ":marshal_dist_to_cur_center", 160), #close (50p-100p)
                              (store_sub, ":distance_score", ":marshal_dist_to_cur_center", 10),
                              (val_div, ":distance_score", 3),
                              (store_sub, ":distance_score", 100, ":distance_score"),
                            (else_try),
                              (lt, ":marshal_dist_to_cur_center", 360), #far (10p-50p)
                              (store_sub, ":distance_score", ":marshal_dist_to_cur_center", 250),
                              (val_div, ":distance_score", 5),
                              (store_sub, ":distance_score", 50, ":distance_score"),
                            (else_try),
                              (assign, ":distance_score", 10), #very far
                            (try_end),
                          (else_try),
                            (store_add, ":enemy_strength_nearby_score", ":enemy_strength_nearby", 20000),
                            (val_div, ":enemy_strength_nearby_score", 200),
                            (assign, ":distance_score", 70), #not related to marshal's position, because everybody is going same place (no gathering in most village raids)
                          (try_end),
                          
							##diplomacy start+
							(try_begin),
								#AI changes LOW: Give priority to defending centers with lords
								(eq, DPLMC_AI_CHANGES_LOW, "$g_dplmc_ai_changes"),
								(party_slot_ge, ":cur_center", slot_town_lord, 0),
								(val_mul, ":threat_importance", 120),
								(val_div, ":threat_importance", 100),
							(try_end),
							##diplomacy end+
							(store_mul, ":threat_score", ":enemy_strength_nearby_score", ":total_prosperity_score"),
							(val_mul, ":threat_score", ":threat_importance"),
							(val_mul, ":threat_score", ":distance_score"),
							(val_div, ":threat_score", 10000),
                          
                          (try_begin),
                            (ge, "$cheat_mode", 1),
                            (gt, ":threat_score", 0),
                            (eq, ":faction_no", "fac_kingdom_6"),
                            (assign, reg0, ":threat_score"),
                            (str_store_party_name, s32, ":cur_center"),
                            (assign, reg1,  ":total_prosperity_score"),
                            (assign, reg2, ":enemy_strength_nearby_score"),
                            (assign, reg3, ":threat_importance"),
                            (assign, reg4, ":distance_score"),
                            #(display_message, "@{!}DEBUG : defend of {s32} is {reg0}, prosperity:{reg1}, enemy nearby:{reg2}, threat importance:{reg3}, distance: {reg4}"),
                          (try_end),
                          
                          (gt, ":threat_score", ":maximum_threat_score"),
                          
                          (assign, ":most_threatened_center", ":cur_center"),
                          (assign, ":maximum_threat_score", ":threat_score"),
                          (assign, ":enemy_strength_near_most_threatened_center", ":enemy_strength_nearby"),
                        (try_end),
                        
                        (val_mul, ":maximum_threat_score", 3),
                        (val_div, ":maximum_threat_score", 2),
                        
                        (assign, reg0, ":most_threatened_center"),
                        (assign, reg1, ":maximum_threat_score"),
                        (assign, reg2, ":enemy_strength_near_most_threatened_center"),
                    ]),
                    
                    
					#script_npc_decision_checklist_peace_or_war
				   ##diplomacy start+
				   #Modified this to return additional information.
					##diplomacy end+
					(
					"npc_decision_checklist_peace_or_war",
					#this script is used to add a bit more color to diplomacy, particularly with regards to the player

					[
						(store_script_param, ":actor_faction", 1),
						(store_script_param, ":target_faction", 2),
						(store_script_param, ":envoy", 3),
						
						##diplomacy start+
						#Since "fac_player_supporters_faction" is used as a synonym for "the faction led by the player"
						#in many places, correct this here.
						(call_script, "script_dplmc_translate_inactive_player_supporter_faction_2", ":actor_faction", ":target_faction"),
						(assign, ":actor_faction", reg0),
						(assign, ":target_faction", reg1),
						##diplomacy end+

						(assign, ":actor_strength", 0),
						(assign, ":target_strength", 0),
						(assign, ":actor_centers_held_by_target", 0),

					#	(assign, ":two_factions_share_border", 0),
						(assign, ":third_party_war", 0),
						(assign, ":num_third_party_wars", 0),

						(assign, ":active_mutual_enemy", 0), #an active enemy with which the target is at war
						(assign, "$g_concession_demanded", 0),
						##diplomacy start+
						(assign, ":last_center_lost", 0),#  last center lost to the target faction
						(assign, ":last_center_lost_time", 0),# time the last center was lost to the target faction
						
						#"Third party" after taking into account alliances
						#(assign, ":actual_third_party_war", 0),
						(assign, ":num_actual_third_party_wars", 0),
						##diplomacy end+

						(store_relation, ":current_faction_relation", ":actor_faction", ":target_faction"),

						(try_begin),
							(eq, ":target_faction", "fac_player_supporters_faction"),
							(assign, ":modified_honor_and_relation", "$player_honor"), #this can be affected by the emissary's skill

							(val_add, ":target_strength", 2), #for player party
						(else_try),
							(assign, ":modified_honor_and_relation", 0), #this can be affected by the emissary's skill
						(try_end),

						(faction_get_slot, ":actor_leader", ":actor_faction", slot_faction_leader),
						(faction_get_slot, ":target_leader", ":target_faction", slot_faction_leader),

						(call_script, "script_troop_get_relation_with_troop", ":actor_leader", ":target_leader"),

						(assign, ":relation_bonus", reg0),
						(val_min, ":relation_bonus", 10),
						(val_add, ":modified_honor_and_relation", ":relation_bonus"),

						(str_store_troop_name, s15, ":actor_leader"),
						(str_store_troop_name, s16, ":target_leader"),


						(assign, ":war_damage_suffered", 0),
						(assign, ":war_damage_inflicted", 0),

						(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":actor_faction", ":target_faction"),
						(assign, ":war_peace_truce_status", reg0),
						(str_clear, s12),
						(try_begin),
							(eq, ":war_peace_truce_status", -2),
							(str_store_string, s12, "str_s15_is_at_war_with_s16_"),

							(store_add, ":war_damage_inflicted_slot", ":target_faction", slot_faction_war_damage_inflicted_on_factions_begin),
							(val_sub, ":war_damage_inflicted_slot", kingdoms_begin),
							(faction_get_slot, ":war_damage_inflicted", ":actor_faction", ":war_damage_inflicted_slot"),

							(store_add, ":war_damage_suffered_slot", ":actor_faction", slot_faction_war_damage_inflicted_on_factions_begin),
							(val_sub, ":war_damage_suffered_slot", kingdoms_begin),
							(faction_get_slot, ":war_damage_suffered", ":target_faction", ":war_damage_suffered_slot"),


						(else_try),
							#truce in effect
							(eq, ":war_peace_truce_status", 1),
							(str_store_string, s12, "str_in_the_short_term_s15_has_a_truce_with_s16_as_a_matter_of_general_policy_"),
						(else_try),
							#provocation noted
							(eq, ":war_peace_truce_status", -1),
							(str_store_string, s12, "str_in_the_short_term_s15_was_recently_provoked_by_s16_and_is_under_pressure_to_declare_war_as_a_matter_of_general_policy_"),
						(try_end),

						#clear for dialog with lords
						(try_begin),
							(is_between, "$g_talk_troop", active_npcs_begin, active_npcs_end),
							(str_clear, s12),
						(try_end),

						(try_begin),
							(gt, ":envoy", -1),
							(store_skill_level, ":persuasion_x_2", "skl_persuasion", ":envoy"),
							(val_mul, ":persuasion_x_2", 2),
							(val_add, ":modified_honor_and_relation", ":persuasion_x_2"),

							(try_begin),
								(eq, "$cheat_mode", 1),
								(assign, reg4, ":modified_honor_and_relation"),
								(display_message, "str_envoymodified_diplomacy_score_honor_plus_relation_plus_envoy_persuasion_=_reg4"),
							(try_end),

						(try_end),


						(try_for_range, ":kingdom_to_reset", kingdoms_begin, kingdoms_end),
							(faction_set_slot, ":kingdom_to_reset", slot_faction_temp_slot, 0),
						(try_end),

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
							(party_get_slot, ":party_original_faction", ":party_no", slot_center_original_faction),
							(party_get_slot, ":party_ex_faction", ":party_no", slot_center_ex_faction),


							#total strengths
							(try_begin),
								(is_between, ":party_current_faction", kingdoms_begin, kingdoms_end),
								(faction_get_slot, ":faction_strength", ":party_current_faction", slot_faction_temp_slot),
								(val_add, ":faction_strength", ":party_value"),
								(faction_set_slot, ":party_current_faction", slot_faction_temp_slot, ":faction_strength"),
							(try_end),


							(try_begin),
								(eq, ":party_current_faction", ":target_faction"),
								(val_add, ":target_strength", ":party_value"),

								(try_begin),
									(this_or_next|eq, ":party_original_faction", ":actor_faction"),
										(eq, ":party_ex_faction", ":actor_faction"),
									(val_add, ":actor_centers_held_by_target", 1),
									(try_begin),
										(is_between, ":party_no", walled_centers_begin, walled_centers_end),
										(assign, "$g_concession_demanded", ":party_no"),
										(str_store_party_name, s18, "$g_concession_demanded"),
										##diplomacy start+ Also track the most recently taken walled center
										(eq, ":party_ex_faction", ":actor_faction"),
										(this_or_next|lt, ":last_center_lost", 1),
											(party_slot_ge, ":party_no", dplmc_slot_center_last_transfer_time, ":last_center_lost_time"),
										(assign, ":last_center_lost", ":party_no"),
										(party_get_slot, ":last_center_lost_time", ":party_no", dplmc_slot_center_last_transfer_time),
										##diplomacy end+
									(try_end),
								(try_end),

					# Could include two factions share border, but war is unlikely to break out in the first place unless there is a common border

					#			(try_begin),
					#				(is_between, ":party_no", walled_centers_begin, walled_centers_end),
					#				(try_for_range, ":other_center", walled_centers_begin, walled_centers_end),
					#					(assign, ":two_factions_share_border", 0),
					#					(store_faction_of_party, ":other_faction", ":other_center"),
					#					(eq, ":other_faction", ":actor_faction"),
					#					(store_distance_to_party_from_party, ":distance", ":party_no", ":other_center"),
					#					(le, ":distance", 15),
					#					(assign, ":two_factions_share_border", 1),
					#				(try_end),
					#			(try_end),
							(else_try),
								(eq, ":party_current_faction", ":actor_faction"),
								(val_add, ":actor_strength", ":party_value"),
							(try_end),
						(try_end),

						#Total Calradia strength = 110 x 1 (villages,), 48? x 2 castles, 22 x 3 towns, 88 x 2 lord parties = 272 + 176 = 448
						(assign, ":strongest_kingdom", -1),
						(assign, ":score_to_beat", 60), #Maybe raise once it works
						##diplomacy start+
						#Take into account alliances
						(assign, ":strongest_kingdom_offensive", -1),
						(assign, ":strongest_kingdom_offensive_score", -1),
						
						(assign, ":strongest_kingdom_defensive", -1),
						(assign, ":strongest_kingdom_defensive_score", -1),
						
						(faction_get_slot, ":actor_offensive_score", ":actor_faction", slot_faction_temp_slot),
						(faction_get_slot, ":actor_defensive_score", ":actor_faction", slot_faction_temp_slot),
						
						#(faction_get_slot, ":target_offensive_score", ":target_faction", slot_faction_temp_slot),
						(faction_get_slot, ":target_defensive_score", ":target_faction", slot_faction_temp_slot),

						#Use these instead of just counting the number of factions
						(assign, ":strength_against_actor", 0),
						(assign, ":strength_against_target", 0),
						
						##diplomacy end+
						(try_for_range, ":strongest_kingdom_candidate", kingdoms_begin, kingdoms_end),
							(faction_get_slot, ":candidate_strength", ":strongest_kingdom_candidate", slot_faction_temp_slot),
							##diplomacy start+
							#Take into account allies
							(assign, ":candidate_offensive_score", ":candidate_strength"),
							(assign, ":candidate_defensive_score", ":candidate_strength"),
							(try_for_range, ":other_kingdom", kingdoms_begin, kingdoms_end),
							   (neq, ":other_kingdom", ":strongest_kingdom_candidate"),
								(faction_get_slot, ":other_kingdom_strength", ":other_kingdom", slot_faction_temp_slot),
								(call_script, "script_dplmc_get_faction_truce_length_with_faction", ":strongest_kingdom_candidate", ":other_kingdom"),
								#Add 90% rather than 100%, because otherwise, if several kingdoms are
								#allied all of them will have the same strength by this measurement.
								(try_begin),
										 #Full alliance
										 (gt, reg0, dplmc_treaty_alliance_days_expire),
										 (store_mul, reg0, ":other_kingdom_strength", 9),
										 (val_div, reg0, 10),
										 (val_add, ":candidate_offensive_score", reg0),
										 (val_add, ":candidate_defensive_score", reg0),
								(else_try),
										 #Defensive alliance
										 (gt, reg0, dplmc_treaty_defense_days_expire),
										 (store_mul, reg0, ":other_kingdom_strength", 9),
										 (val_div, reg0, 10),
										 (val_add, ":candidate_defensive_score", reg0),
								(try_end),
							(try_end),
							#Update actor/target strengths with alliances, and "strength against"
							(try_begin),
								(eq, ":strongest_kingdom_candidate", ":actor_faction"),
								(assign, ":actor_offensive_score", ":candidate_offensive_score"),
								(assign, ":actor_defensive_score", ":candidate_defensive_score"),
							(else_try),
								(store_relation, ":relation", ":strongest_kingdom_candidate", ":actor_faction"),
								(lt, ":relation", 0),
								(val_add, ":strength_against_actor", ":other_kingdom_strength"),
							(try_end),
							(try_begin),
								(eq, ":strongest_kingdom_candidate", ":target_faction"),
								#(assign, ":target_offensive_score", ":candidate_offensive_score"),
								(assign, ":target_defensive_score", ":candidate_defensive_score"),
							(else_try),
								(store_relation, ":relation", ":strongest_kingdom_candidate", ":target_faction"),
								(lt, ":relation", 0),
								(val_add, ":strength_against_target", ":other_kingdom_strength"),
							(try_end),
							#Update global max/min
							(try_begin),
								(gt, ":candidate_offensive_score", ":strongest_kingdom_offensive_score"),
								(assign, ":strongest_kingdom_offensive", ":strongest_kingdom_candidate"),
								(assign, ":strongest_kingdom_offensive_score", ":candidate_offensive_score"),
							(try_end),
							(try_begin),
								(gt, ":candidate_defensive_score", ":strongest_kingdom_defensive_score"),
								(assign, ":strongest_kingdom_defensive", ":strongest_kingdom_candidate"),
								(assign, ":strongest_kingdom_defensive_score", ":candidate_defensive_score"),		
							(try_end),
							##diplomacy end+
							(gt, ":candidate_strength", ":score_to_beat"),
							(assign, ":strongest_kingdom", ":strongest_kingdom_candidate"),
							(assign, ":score_to_beat", ":candidate_strength"),
						(try_end),


						(try_begin),
							(eq, "$cheat_mode", 2),
							(gt, ":strongest_kingdom", 1),
							(str_store_faction_name, s4, ":strongest_kingdom"),
							(assign, reg3, ":score_to_beat"),
							(display_message, "@{!}DEBUG - {s4} strongest kingdom with {reg3} strength"),
							##diplomacy start+ Show strongest counting alliances if it's different
							(try_begin),
								(gt, ":strongest_kingdom_offensive", 0),
								(neq, ":strongest_kingdom_offensive", ":strongest_kingdom"),
								(str_store_faction_name, s4, ":strongest_kingdom_offensive"),
								(assign, reg3, ":strongest_kingdom_offensive_score"),
								(display_message, "@{!}DEBUG - including offensive and defensive alliances {s4} strongest kingdom with {reg3} strength"),
							(try_end),
							(try_begin),
								(gt, ":strongest_kingdom_defensive", 0),
								(neq, ":strongest_kingdom_defensive", ":strongest_kingdom"),
								(neq, ":strongest_kingdom_defensive", ":strongest_kingdom_offensive"),
								(str_store_faction_name, s4, ":strongest_kingdom_defensive"),
								(assign, reg3, ":strongest_kingdom_defensive_score"),
								(display_message, "@{!}DEBUG - including only defensive alliances {s4} strongest kingdom with {reg3} strength"),
							(try_end),
							#Revert values
							(assign, reg3, ":score_to_beat"),
							(str_store_faction_name, s4, ":strongest_kingdom"),
							##diplomacy end+
						(try_end),


						(assign, ":strength_ratio", 1),
						(try_begin),
							(gt, ":actor_strength", 0),
							(store_mul, ":strength_ratio", ":target_strength", 100),
							(val_div, ":strength_ratio", ":actor_strength"),
						(try_end),
						##diplomacy start+
						#Other strength ratios using strengths counting alliances
						(assign, ":strength_ratio_new_attack", 1),
						(try_begin),
							(gt, ":actor_offensive_score", 0),
							(store_mul, ":strength_ratio_new_attack", ":target_defensive_score", 100),
							(val_div, ":strength_ratio_new_attack", ":actor_offensive_score"),
						(try_end),
						(assign, ":strength_ratio_current_war", 1),
						(try_begin),
							(gt, ":actor_defensive_score", 0),
							(store_mul, ":strength_ratio_current_war", ":target_defensive_score", 100),
							(val_div, ":strength_ratio_current_war", ":actor_defensive_score"),
						(try_end),
						#Calculate the total magnitude of the forces hostile to the faction versus its allies
						(assign, ":strength_ratio_all_enemies_actor", 1),
						(try_begin),
							(gt, ":actor_defensive_score", 0),
							(store_mul, ":strength_ratio_all_enemies_actor", ":strength_against_actor", 100),
							(val_div, ":strength_ratio_all_enemies_actor", ":actor_defensive_score"),
						(try_end),
						##diplomacy end+

						(try_for_range, ":possible_mutual_enemy", kingdoms_begin, kingdoms_end),
							(neq, ":possible_mutual_enemy", ":target_faction"),
							(neq, ":possible_mutual_enemy", ":actor_faction"),
							(faction_slot_eq, ":possible_mutual_enemy", slot_faction_state, sfs_active),

							(store_relation, ":relation", ":possible_mutual_enemy", ":actor_faction"),
							(lt, ":relation", 0),
							(assign, ":third_party_war", ":possible_mutual_enemy"),
							(val_add, ":num_third_party_wars", 1),
							
							##diplomacy start+
							##ACTUAL third-party wars (i.e. not allied to the target faction)
							(call_script, "script_dplmc_get_faction_truce_length_with_faction", ":target_faction", ":possible_mutual_enemy"),
							(try_begin),
								(neg|gt, reg0, dplmc_treaty_defense_days_expire),
								#(assign, ":actual_third_party_war", ":possible_mutual_enemy"),
								(val_add, ":num_actual_third_party_wars", 1),
							(try_end),
							##diplomacy end+

							(store_relation, ":relation", ":possible_mutual_enemy", ":target_faction"),
							(lt, ":relation", 0),
							(assign, ":active_mutual_enemy", ":possible_mutual_enemy"),
						(try_end),

						(store_current_hours, ":cur_hours"),
						(faction_get_slot, ":faction_ai_last_decisive_event", ":actor_faction", slot_faction_ai_last_decisive_event),
						(store_sub, ":hours_since_last_decisive_event", ":cur_hours", ":faction_ai_last_decisive_event"),
						
						##diplomacy start+ use gender script
						(call_script, "script_dplmc_store_troop_is_female_reg", ":actor_leader", 4),
						##diplomacy end+

						(try_begin),
							(gt, "$supported_pretender", 0),
							(this_or_next|eq, "$supported_pretender", ":actor_leader"),
								(eq, "$supported_pretender", ":target_leader"),
							(this_or_next|eq, ":actor_faction", "$supported_pretender_old_faction"),
								(eq, ":target_faction", "$supported_pretender_old_faction"),

							(assign, ":result", -3),
							##diplomacy start+
							#(troop_get_type, reg4, ":actor_leader"),#<- commented out
							##diplomacy end+
							(assign, ":explainer_string", "str_s12s15_cannot_negotiate_with_s16_as_to_do_so_would_undermine_reg4herhis_own_claim_to_the_throne_this_civil_war_must_almost_certainly_end_with_the_defeat_of_one_side_or_another"),
						(else_try),
							(lt, ":modified_honor_and_relation", -20),
							##diplomacy start+ Take into account strengths including alliances
							(this_or_next|lt, ":strength_ratio_current_war", 125),
							##diplomacy end+
							(lt, ":strength_ratio", 125),
							(lt, ":war_damage_suffered", 400),
							(this_or_next|neq, ":war_peace_truce_status", -2),
								(lt, ":hours_since_last_decisive_event", 720),
							##diplomacy start+ Examine strength of enemies versus allies
							(this_or_next|lt, ":strength_ratio_all_enemies_actor", 125),
							##diplomacy end+
							(eq, ":num_third_party_wars", 0),

							(assign, ":result", -3),
							##diplomacy start+
							#(troop_get_type, reg4, ":actor_leader"),#<- commented out
							##diplomacy end+
							(assign, ":explainer_string", "str_s12s15_considers_s16_to_be_dangerous_and_untrustworthy_and_shehe_wants_to_bring_s16_down"),
						(else_try),
							(gt, ":actor_centers_held_by_target", 0),
							(try_begin),
							  (eq, "$cheat_mode", 1),
							  (display_message, "@{!}Actor centers held by target noted"),
							(try_end),

							(lt, ":war_damage_suffered", 200),
							(try_begin),
							  (eq, "$cheat_mode", 1),
							  (display_message, "@{!}War damage under minimum"),
							(try_end),

							##diplomacy start+ Take into account strengths including alliances
							(this_or_next|lt, ":strength_ratio_current_war", 125),
							##diplomacy end+
							(lt, ":strength_ratio", 125),
							(try_begin),
							  (eq, "$cheat_mode", 1),
							  (display_message, "@{!}Strength ratio correct"),
							(try_end),
							##diplomacy start+ Examine strength of enemies versus allies
							(this_or_next|lt, ":strength_ratio_all_enemies_actor", 125),
							##diplomacy end+
							(eq, ":num_third_party_wars", 0),
							(try_begin),
							  (eq, "$cheat_mode", 1),
							  (display_message, "@{!}Third party wars"),
							(try_end),

							(assign, ":result", -2),
							(assign, ":explainer_string", "str_s12s15_is_anxious_to_reclaim_old_lands_such_as_s18_now_held_by_s16"),
						(else_try),
							(eq, ":war_peace_truce_status", -2),
							##diplomacy start+ Take into account strengths including alliances
							(this_or_next|lt, ":strength_ratio_current_war", 125),
							##diplomacy end+
							(lt, ":strength_ratio", 125),
							(le, ":num_third_party_wars", 1),
							(ge, ":war_damage_inflicted", 5),
							(this_or_next|neq, ":war_peace_truce_status", -2),
								(lt, ":hours_since_last_decisive_event", 720),

							(store_mul, ":war_damage_suffered_x_2", ":war_damage_suffered", 2),
							(gt, ":war_damage_inflicted", ":war_damage_suffered_x_2"),

							(assign, ":result", -2),
							##diplomacy start+
							#(troop_get_type, reg4, ":actor_leader"),#<- commented out
							##diplomacy end+
							(assign, ":explainer_string", "str_s12s15_feels_that_reg4shehe_is_winning_the_war_against_s16_and_sees_no_reason_not_to_continue"),
						(else_try),
							(le, ":war_peace_truce_status", -1),

							(this_or_next|eq, ":war_peace_truce_status", -1), #either a war is just beginning, or there is a provocation
								(le, ":war_damage_inflicted", 1),
							##diplomacy start+ Take into account strengths including alliances
							(this_or_next|lt, ":strength_ratio_new_attack", 150),
							##diplomacy end+
							(lt, ":strength_ratio", 150),
							##diplomacy start+ Examine strength of enemies versus allies
							(this_or_next|lt, ":strength_ratio_all_enemies_actor", 150),
							##diplomacy end+
							(eq, ":num_third_party_wars", 0),

							(faction_slot_ge, ":actor_faction", slot_faction_instability, 60),

							(assign, ":result", -1),
							(assign, ":explainer_string", "str_s12s15_faces_too_much_internal_discontent_to_feel_comfortable_ignoring_recent_provocations_by_s16s_subjects"),
						(else_try),
							(eq, ":war_peace_truce_status", -2),
							(lt, ":war_damage_inflicted", 100),
							(eq, ":num_third_party_wars", 1),

							(assign, ":result", -1),
							##diplomacy start+
							#(troop_get_type, reg4, ":actor_leader"),#<- commented out
							##diplomacy end+
							(assign, ":explainer_string", "str_s12even_though_reg4shehe_is_fighting_on_two_fronts_s15_is_inclined_to_continue_the_war_against_s16_for_a_little_while_longer_for_the_sake_of_honor"),

						(else_try),
							(eq, ":war_peace_truce_status", -2),
							(lt, ":war_damage_inflicted", 100),
							(eq, ":num_third_party_wars", 0),

							(assign, ":result", -1),
							##diplomacy start+
							#(troop_get_type, reg4, ":actor_leader"),#<- commented out
							##diplomacy end+
							(assign, ":explainer_string", "str_s12s15_feels_that_reg4shehe_must_pursue_the_war_against_s16_for_a_little_while_longer_for_the_sake_of_honor"),
						(else_try),
							(this_or_next|faction_slot_eq, ":actor_faction", slot_faction_ai_state, sfai_attacking_center),
							(this_or_next|faction_slot_eq, ":actor_faction", slot_faction_ai_state, sfai_raiding_village),
								(faction_slot_eq, ":actor_faction", slot_faction_ai_state, sfai_attacking_enemy_army),
							(faction_get_slot, ":offensive_object", ":actor_faction", slot_faction_ai_object),
							(party_is_active, ":offensive_object"),
							(store_faction_of_party, ":offensive_object_faction", ":offensive_object"),
							(eq, ":offensive_object_faction", ":target_faction"),
							(str_store_party_name, s17, ":offensive_object"),

							(assign, ":result", -1),
							(assign, ":explainer_string", "str_s12s15_is_currently_on_the_offensive_against_s17_now_held_by_s16_and_reluctant_to_negotiate"),


						(else_try),
							#Attack strongest kingdom, if it is also at war
							##diplomacy start+ Take into account strengths including alliances
							(this_or_next|eq, ":strongest_kingdom_offensive", ":target_faction"),
							##diplomacy end+
							(eq, ":strongest_kingdom", ":target_faction"),
							(eq, ":num_third_party_wars", 0),

							#Either not at war, or at war for two months
							(this_or_next|ge, ":war_peace_truce_status", -1),
								(lt, ":hours_since_last_decisive_event", 1440),

					#		(eq, ":two_factions_share_border", 0),

							(assign, ":at_least_one_other_faction_at_war_with_strongest", 0),
							(try_for_range, ":kingdom_to_check", kingdoms_begin, kingdoms_end),
								(neq, ":kingdom_to_check", ":actor_faction"),
								(neq, ":kingdom_to_check", ":target_faction"),
								(faction_slot_eq, ":kingdom_to_check", slot_faction_state, sfs_active),
								(store_relation, ":relation_of_factions", ":kingdom_to_check", ":target_faction"),
								(lt, ":relation_of_factions", 0),
								(assign, ":at_least_one_other_faction_at_war_with_strongest", 1),
							(try_end),
							(eq, ":at_least_one_other_faction_at_war_with_strongest", 1),


							(assign, ":result", -1),
							(assign, ":explainer_string", "str_s12s15_is_alarmed_by_the_growing_power_of_s16"),

						#bid to conquer all Calradia
						(else_try),
							(eq, ":num_third_party_wars", 0),
							(try_begin),
								(ge, "$cheat_mode", 1),
								(display_message, "@{!}DEBUG -- No third party wars for {s15}"),
							(try_end),
							(eq, ":actor_faction", ":strongest_kingdom"),
							#peace with no truce or provocation

							(try_begin),
								(ge, "$cheat_mode", 1),
								(display_message, "@{!}DEBUG -- {s15} is strongest kingdom"),
							(try_end),


							(faction_get_slot, ":actor_strength", ":actor_faction", slot_faction_temp_slot),
							(faction_get_slot, ":target_strength", ":target_faction", slot_faction_temp_slot),
							(store_sub, ":strength_difference", ":actor_strength", ":target_strength"),
							##diplomacy start+ Include bonus from alliance
							(store_sub, reg0, ":actor_offensive_score", ":target_defensive_score"),
							(this_or_next|ge, reg0, 30),
							##diplomacy end+
							(ge, ":strength_difference", 30),

							(try_begin),
								(ge, "$cheat_mode", 1),
								(display_message, "@{!}DEBUG -- {s15} has 30 point advantage over {s16}"),
							(try_end),


							(assign, ":nearby_center_found", 0),
							(try_for_range, ":actor_faction_walled_center", walled_centers_begin, walled_centers_end),
								(store_faction_of_party, ":walled_center_faction_1", ":actor_faction_walled_center"),
								(eq, ":walled_center_faction_1", ":actor_faction"),
								(try_for_range, ":target_faction_walled_center", walled_centers_begin, walled_centers_end),
									(store_faction_of_party, ":walled_center_faction_2", ":target_faction_walled_center"),
									(eq, ":walled_center_faction_2", ":target_faction"),
									(store_distance_to_party_from_party, ":distance", ":target_faction_walled_center", ":actor_faction_walled_center"),
									(lt, ":distance", 25),
									(assign, ":nearby_center_found", 1),
								(try_end),
							(try_end),
							(eq, ":nearby_center_found", 1),


							(try_begin),
								(ge, "$cheat_mode", 1),
								(display_message, "@{!}DEBUG -- {s15} has proximity to {s16}"),
							(try_end),

							(assign, ":result", -1),
							(assign, ":explainer_string", "str_s12s15_declared_war_to_control_calradia"),

						(else_try),
							(lt, ":modified_honor_and_relation", -20),

							(assign, ":result", 0),
							(assign, ":explainer_string", "str_s12s15_distrusts_s16_and_fears_that_any_deals_struck_between_the_two_realms_will_not_be_kept"),


						#wishes to deal
						(else_try),
							(lt, ":current_faction_relation", 0),
							(ge, ":num_third_party_wars", 2),
							(assign, ":result", 3),

							(assign, ":explainer_string", "str_s12s15_is_at_war_on_too_many_fronts_and_eager_to_make_peace_with_s16"),
						(else_try),
							(gt, ":active_mutual_enemy", 0),
							(eq, ":actor_centers_held_by_target", 0),
							(this_or_next|ge, ":current_faction_relation", 0),
					#			(eq, ":two_factions_share_border", 0),
								(eq, 1, 1),

							(assign, ":result", 3),
							(str_store_faction_name, s17, ":active_mutual_enemy"),
							##diplomacy start+
							#(troop_get_type, reg4, ":actor_leader"),#<- commented out
							##diplomacy end+
							(assign, ":explainer_string", "str_s12s15_seems_to_think_that_s16_and_reg4shehe_have_a_common_enemy_in_the_s17"),

						(else_try),
							(eq, ":war_peace_truce_status", -2),
							(ge, ":hours_since_last_decisive_event", 720),

							##diplomacy start+
							#(troop_get_type, reg4, ":actor_leader"),#<- commented out
							##diplomacy end+

							(assign, ":result", 2),
							(assign, ":explainer_string", "str_s12s15_feels_frustrated_by_reg4herhis_inability_to_strike_a_decisive_blow_against_s16"),


						(else_try),
							(lt, ":current_faction_relation", 0),
							(gt, ":war_damage_suffered", 100),

							(val_mul, ":war_damage_suffered_x_2", 2),
							(lt, ":war_damage_inflicted", ":war_damage_suffered_x_2"),

							(assign, ":result", 2),
							(assign, ":explainer_string", "str_s12s15_has_suffered_enough_in_the_war_with_s16_for_too_little_gain_and_is_ready_to_pursue_a_peace"),

						(else_try),
							(gt, ":third_party_war", 0),
							(ge, ":modified_honor_and_relation", 0),
							(lt, ":current_faction_relation", 0),

							(assign, ":result", 1),
							(str_store_faction_name, s17, ":third_party_war"),
							(assign, ":explainer_string", "str_s12s15_would_like_to_firm_up_a_truce_with_s16_to_respond_to_the_threat_from_the_s17"),
						(else_try),
							(gt, ":third_party_war", 0),
							(ge, ":modified_honor_and_relation", 0),

							(assign, ":result", 1),
							(str_store_faction_name, s17, ":third_party_war"),
							(assign, ":explainer_string", "str_s12s15_wishes_to_be_at_peace_with_s16_so_as_to_pursue_the_war_against_the_s17"),
						(else_try),
							(gt, ":strength_ratio", 175),
					#		(eq, ":two_factions_share_border", 1),

							(assign, ":result", 1),
							(assign, ":explainer_string", "str_s12s15_seems_to_be_intimidated_by_s16_and_would_like_to_avoid_hostilities"),
						(else_try),
							(lt, ":current_faction_relation", 0),

							(assign, ":result", 1),
							(assign, ":explainer_string", "str_s12s15_has_no_particular_reason_to_continue_the_war_with_s16_and_would_probably_make_peace_if_given_the_opportunity"),
						(else_try),
							(assign, ":result", 1),
							(assign, ":explainer_string", "str_s12s15_seems_to_be_willing_to_improve_relations_with_s16"),
						(try_end),
						##diplomacy start+
						#Possibly change the concession demanded
						(try_begin),
							(gt, "$g_concession_demanded", 0),
							(gt, ":last_center_lost", 0),
							(neq, "$g_concession_demanded", ":last_center_lost"),
							(try_begin),
								#This logically can't happen due to the order centers appear in
								(is_between, "$g_concession_demanded", towns_begin, towns_end),
								(neg|is_between, ":last_center_lost", towns_begin, towns_end),#Do not replace
							(else_try),
								(is_between, ":last_center_lost", towns_begin, towns_end),
								(neg|is_between, "$g_concession_demanded", towns_begin, towns_end),
								(assign, "$g_concession_demanded", ":last_center_lost"),
							(else_try),
								(party_slot_eq, ":last_center_lost", slot_center_original_faction, ":actor_faction"),
								(neg|party_slot_eq, "$g_concession_demanded", slot_center_original_faction, ":actor_faction"),
								(assign, "$g_concession_demanded", ":last_center_lost"),
							(try_end),
							(eq, "$g_concession_demanded", ":last_center_lost"),
							(str_store_party_name, s18, "$g_concession_demanded"),#change s18 to match
						(try_end),
						##diplomacy end+
						(str_store_string, s14, ":explainer_string"),
						(assign, reg0, ":result"),
						(assign, reg1, ":explainer_string"),

					]),
                    
                    ("npc_decision_checklist_male_guardian_assess_suitor", #parameters from dialog
                      [
                        (store_script_param, ":lord", 1),
                        (store_script_param, ":suitor", 2),
                        
                        (troop_get_slot, ":lord_reputation", ":lord", slot_lord_reputation_type),
                        (store_faction_of_troop, ":lord_faction", ":lord"),
                        
                        (try_begin),
                          (eq, ":suitor", "trp_player"),
                          (assign, ":suitor_faction", "$players_kingdom"),
                        (else_try),
                          (store_faction_of_troop, ":suitor_faction", ":suitor"),
                        (try_end),
                        (store_relation, ":faction_relation_with_suitor", ":lord_faction", ":suitor_faction"),
                        
                        (call_script, "script_troop_get_relation_with_troop", ":lord", ":suitor"),
                        (assign, ":lord_suitor_relation", reg0),
                        
                        (troop_get_slot, ":suitor_renown", ":suitor", slot_troop_renown),
                        
                        
                        (assign, ":competitor_found", -1),
                        
                        (try_begin),
                          (eq, ":suitor", "trp_player"),
                          (gt, "$marriage_candidate", 0),
                          
                          (try_for_range, ":competitor", lords_begin, lords_end),
                            (store_faction_of_troop, ":competitor_faction", ":competitor"),
                            (eq, ":competitor_faction", ":lord_faction"),
                            (this_or_next|troop_slot_eq, ":competitor", slot_troop_love_interest_1, "$marriage_candidate"),
                            (this_or_next|troop_slot_eq, ":competitor", slot_troop_love_interest_2, "$marriage_candidate"),
                            (troop_slot_eq, ":competitor", slot_troop_love_interest_3, "$marriage_candidate"),
                            
                            (call_script, "script_troop_get_relation_with_troop", ":competitor", ":lord"),
                            (gt, reg0, 5),
                            
                            (troop_slot_ge, ":competitor", slot_troop_renown, ":suitor_renown"),  #higher renown than player
                            
                            (assign, ":competitor_found", ":competitor"),
                            (str_store_troop_name, s14, ":competitor"),
                            (str_store_troop_name, s16, "$marriage_candidate"),
                          (try_end),
                        (try_end),
                        
                        #renown
                        (try_begin),
                          (lt, ":suitor_renown", 50),
                          (this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_quarrelsome),
                          (this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_debauched),
                          (troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_selfrighteous),
                          (assign, ":explainer_string", "str_excuse_me_how_can_you_possibly_imagine_yourself_worthy_to_marry_into_our_family"),
                          (assign, ":result", -3),
                        (else_try),
                          (lt, ":suitor_renown", 50),
                          (troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_goodnatured),
                          
                          (assign, ":explainer_string", "str_em_with_regard_to_her_ladyship_we_were_looking_specifically_for_a_groom_of_some_distinction_fight_hard_count_your_dinars_and_perhaps_some_day_in_the_future_we_may_speak_of_such_things_my_good_man"),
                          (assign, ":result", -1),
                        (else_try),
                          (lt, ":suitor_renown", 50),
                          
                          (assign, ":explainer_string", "str_em_with_regard_to_her_ladyship_we_were_looking_specifically_for_a_groom_of_some_distinction"),
                          (assign, ":result", -2),
                          
                        (else_try),
                          (lt, ":suitor_renown", 200),
                          (neg|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_goodnatured),
                          (assign, ":explainer_string", "str_it_is_too_early_for_you_to_be_speaking_of_such_things_you_are_still_making_your_mark_in_the_world"),
                          
                          (assign, ":result", -1),
                          
                        (else_try), #wrong faction
                          (eq, ":suitor", "trp_player"),
                          (neq, ":suitor_faction", "$players_kingdom"),
                          (str_store_faction_name, s4, ":lord_faction"),
                          (this_or_next|eq, ":lord_reputation", lrep_quarrelsome),
                          (eq, ":lord_reputation", lrep_debauched),
                          (assign, ":explainer_string", "str_you_dont_serve_the_s4_so_id_say_no_one_day_we_may_be_at_war_and_i_prefer_not_to_have_to_kill_my_inlaws_if_at_all_possible"),
                          
                          (assign, ":result", -1),
                          
                        (else_try),
                          (eq, ":suitor", "trp_player"),
                          (neq, ":suitor_faction", "$players_kingdom"),
                          (neq, ":lord_reputation", lrep_goodnatured),
                          (neq, ":lord_reputation", lrep_cunning),
                          
                          (assign, ":explainer_string", "str_as_you_are_not_a_vassal_of_the_s4_i_must_decline_your_request_the_twists_of_fate_may_mean_that_we_will_one_day_cross_swords_and_i_would_hope_not_to_make_a_widow_of_a_lady_whom_i_am_obligated_to_protect"),
                          
                          (assign, ":result", -1),
                        (else_try),
                          (eq, ":suitor", "trp_player"),
                          (lt, ":faction_relation_with_suitor", 0),
                          
                          (assign, ":explainer_string", "str_as_you_are_not_a_vassal_of_the_s4_i_must_decline_your_request_the_twists_of_fate_may_mean_that_we_will_one_day_cross_swords_and_i_would_hope_not_to_make_a_widow_of_a_lady_whom_i_am_obligated_to_protect"),
                          
                          (assign, ":result", -1),
                          
                        (else_try),
                          (eq, ":suitor", "trp_player"),
                          (neq, "$player_has_homage", 1),
                          (neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_state, sfs_active),
                          
                          (assign, ":explainer_string", "str_as_you_are_not_a_pledged_vassal_of_our_liege_with_the_right_to_hold_land_i_must_refuse_your_request_to_marry_into_our_family"),
                          
                          (assign, ":result", -1),
                        (else_try),
                          (gt, ":competitor_found", -1),
                          
                          (this_or_next|eq, ":lord_reputation", lrep_selfrighteous),
                          (this_or_next|eq, ":lord_reputation", lrep_debauched),
                          (this_or_next|eq, ":lord_reputation", lrep_martial),
                          (eq, ":lord_reputation", lrep_quarrelsome),
                          
                          (assign, ":explainer_string",	"str_look_here_lad__the_young_s14_has_been_paying_court_to_s16_and_youll_have_to_admit__hes_a_finer_catch_for_her_than_you_so_lets_have_no_more_of_this_talk_shall_we"),
                          (assign, ":result", -1),
                          
                        (else_try),
                          (lt, ":lord_suitor_relation", -4),
                          
                          (assign, ":explainer_string", "str_i_do_not_care_for_you_sir_and_i_consider_it_my_duty_to_protect_the_ladies_of_my_household_from_undesirable_suitors"),
                          (assign, ":result", -3),
                        (else_try),
                          (lt, ":lord_suitor_relation", 5),
                          
                          (assign, ":explainer_string",	"str_hmm_young_girls_may_easily_be_led_astray_so_out_of_a_sense_of_duty_to_the_ladies_of_my_household_i_think_i_would_like_to_get_to_know_you_a_bit_better_we_may_speak_of_this_at_a_later_date"),
                          (assign, ":result", -1),
                        (else_try),
                          
                          (assign, ":explainer_string",	"str_you_may_indeed_make_a_fine_match_for_the_young_mistress"),
                          (assign, ":result", 1),
                        (try_end),
                        
                        (assign, reg0, ":result"),
                        (assign, reg1, ":explainer_string"),
                        
                    ]),
                    
                    ("npc_decision_checklist_marry_female_pc", #
                      [
						(store_script_param, ":npc", 1),
						#diplomacy start+ (players of either gender may marry opposite-gender lords)
						#  Note that many of the strings used here have been altered to change based on the player's gender.
						#  Also, it should be mention that reason is written to s14.
						(assign, ":save_reg1", reg1),
						#Use gender script
						(call_script, "script_dplmc_store_is_female_troop_1_troop_2", "trp_player", ":npc"),
						(assign, ":is_female", reg0),
						(assign, ":npc_female", reg1),
						#diplomacy end+
                        
                        (troop_get_slot, ":npc_reputation_type", ":npc", slot_lord_reputation_type),
                        
                        (call_script, "script_troop_get_romantic_chemistry_with_troop", ":npc", "trp_player"),
                        (assign, ":romantic_chemistry", reg0),
                        
                        (call_script, "script_troop_get_relation_with_troop", ":npc", "trp_player"),
                        (assign, ":relation_with_player", reg0),
                        
                        (assign, ":competitor", -1),
                        (try_for_range, ":competitor_candidate", kingdom_ladies_begin, kingdom_ladies_end),
                          (this_or_next|troop_slot_eq, ":npc", slot_troop_love_interest_1, ":competitor_candidate"),
                          (this_or_next|troop_slot_eq, ":npc", slot_troop_love_interest_2, ":competitor_candidate"),
                          (troop_slot_eq, ":npc", slot_troop_love_interest_3, ":competitor_candidate"),
                          (call_script, "script_troop_get_relation_with_troop", ":npc", ":competitor"),
                          (assign, ":competitor_relation", reg0),
                          
                          (gt, ":competitor_relation", ":relation_with_player"),
                          (assign, ":competitor", ":competitor_candidate"),
                        (try_end),
                        
                        (assign, ":player_possessions", 0),
                        (try_for_range, ":center", centers_begin, centers_end),
                          (troop_slot_eq, ":center", slot_town_lord, "trp_player"),
                          (val_add, ":player_possessions", 1),
                        (try_end),
                        
                        (assign, ":lord_agrees", 0),
                        #reasons for refusal
                        (try_begin),
                          (troop_slot_ge, "trp_player", slot_troop_betrothed, active_npcs_begin),
                          (neg|troop_slot_eq, "trp_player", slot_troop_betrothed, ":npc"),
                          
							(str_store_string, s14, "str_my_lady_engaged_to_another"),
						(else_try),
							#bad relationship - minor
							(lt, ":relation_with_player", -3),
							(this_or_next|eq, ":npc_reputation_type", lrep_upstanding),
							(this_or_next|eq, ":npc_reputation_type", lrep_cunning),
							##diplomacy start+ also test commoner types
							(this_or_next|eq, ":npc_reputation_type", lrep_roguish),
							(this_or_next|eq, ":npc_reputation_type", lrep_custodian),
							(this_or_next|eq, ":npc_reputation_type", lrep_benefactor),
							#And certain lady types?
							(this_or_next|eq, ":npc_reputation_type", lrep_ambitious),
							(this_or_next|eq, ":npc_reputation_type", lrep_moralist),
							##diplomacy end+
								(eq, ":npc_reputation_type", lrep_goodnatured),
                          
                          (str_store_string, s14, "str_madame__given_our_relations_in_the_past_this_proposal_is_most_surprising_i_do_not_think_that_you_are_the_kind_of_woman_who_can_be_bent_to_a_hushands_will_and_i_would_prefer_not_to_have_our_married_life_be_a_source_of_constant_acrimony"),
                          
                        (else_try), #really bad relationship
                          (lt, ":relation_with_player", -10),
                          
                          (this_or_next|eq, ":npc_reputation_type", lrep_quarrelsome),
                          (this_or_next|eq, ":npc_reputation_type", lrep_debauched),
                          (eq, ":npc_reputation_type", lrep_selfrighteous),
                          
                          (str_store_string, s14, "str_i_would_prefer_to_marry_a_proper_maiden_who_will_obey_her_husband_and_is_not_likely_to_split_his_head_with_a_sword"),
                        (else_try),
                          (lt, ":romantic_chemistry", 5),
                          
                          (str_store_string, s14, "str_my_lady_not_sufficient_chemistry"),
                          
						(else_try), #would prefer someone more ladylike
								(this_or_next|eq, ":npc_reputation_type", lrep_upstanding),
									(eq, ":npc_reputation_type", lrep_martial),
								#diplomacy start+ (players of either gender may marry opposite-gender lords)
								#I tried to keep this as symmetric as possible, but this sentence is ridiculous with reversed genders
								(neq, ":npc_female", 1),
								(eq, ":is_female", 1),
								#To reduce annoyance, I've changed this away from an absolute prohibition.
								(troop_get_slot, ":veto", ":npc", slot_troop_set_decision_seed),
								(val_add, ":veto", "$romantic_attraction_seed"),
								(val_mod, ":veto", 5),#4 out of 5 will still automatically refuse
								(try_begin),#make an exception for companions
									(is_between, ":npc", companions_begin, companions_end),
									(assign, ":veto", 0),
								(else_try),
									#On diminished prejudice mode, get rid of the "80% automatically refuse" condition.
									(ge, "$g_disable_condescending_comments", 2),
									(assign, ":veto", 0),
								(try_end),
								(try_begin),
									#Skip the subsequent checks if there's no way for them to pass
									(neq, ":veto", 0),
								(else_try),
									#Requires high chemistry, high relation, and positive honor
									(this_or_next|lt, ":romantic_chemistry", 15),
									(this_or_next|lt, ":relation_with_player", 30),
										(lt, "$player_honor", 10),
									(assign, ":veto", 1),
								(else_try),
									#Relation must be above some arbitrary threshold (only if prejudice settings are not "low")
									(lt, "$g_disable_condescending_comments", 2),
									(store_sub, reg0, 100, ":romantic_chemistry"),
									(lt, ":relation_with_player", reg0),
									(assign, ":veto", 1),
								(else_try),
									#The lord's level must not be less than 75% of the player's (only if prejudice settings are not "low")
									(lt, "$g_disable_condescending_comments", 2),
									(store_character_level, reg0, "trp_player"),
									(val_mul, reg0, 3),
									(val_div, reg0, 4),
									(store_character_level, reg1, ":npc"),
									(lt, reg1, reg0),
									(assign, ":veto", 1),
								(else_try),
									#One of the lord's female relatives must like the player, if any such lords exist.
									(lt, "$g_disable_condescending_comments", 2),
									(troop_get_slot, ":npc_mother", ":npc", slot_troop_mother),
									(assign, reg1, 0),#3 = some disapproved, 2 = some approved, 1 = some existed and had no opinion, 0 = there were none
									(try_for_range, ":kingdom_lady", kingdom_ladies_begin, kingdom_ladies_end),
										(neg|troop_slot_ge, ":kingdom_lady", slot_troop_occupation, slto_retirement),
										(assign, reg0, 0),
										(try_begin),
											(troop_slot_eq, ":kingdom_lady", slot_troop_guardian, ":npc"),
											(assign, reg0, 1),
										(else_try),
											(is_between, ":npc_mother", heroes_begin, heroes_end),
											(this_or_next|eq, ":kingdom_lady", ":npc_mother"),
												(troop_slot_eq, ":kingdom_lady", slot_troop_mother, ":npc_mother"),
											(assign, reg0, 1),
										(try_end),
										(neq, reg0, 0),
										(call_script, "script_troop_get_player_relation", ":kingdom_lady"),
										(try_begin),#some were found and like the player
											(ge, reg0, 1),
											(val_max, reg1, 2),
										(else_try),#some were found and have no opinion
											(eq, reg0, 0),
											(val_max, reg1, 1),
										(else_try),#some were found and dislike the player
											(val_max, reg1, 3),	
										(try_end),
									(try_end),
									(neq, reg0, 0),
									(neq, reg0, 2),   
									(assign, ":veto", 1),
								(try_end),
								#Check if the veto holds
								(neq, ":veto", 0),
								#diplomacy end+
                          
                          (str_store_string, s14, "str_my_lady_while_i_admire_your_valor_you_will_forgive_me_if_i_tell_you_that_a_woman_like_you_does_not_uphold_to_my_ideal_of_the_feminine_of_the_delicate_and_of_the_pure"),
                        (else_try),
                          (eq, ":npc_reputation_type", lrep_quarrelsome),
                          (lt, ":romantic_chemistry", 15),
                          
                          (str_store_string, s14, "str_nah_i_want_a_woman_wholl_keep_quiet_and_do_what_shes_told_i_dont_think_thats_you"),
                        (else_try), #no properties
                          (this_or_next|eq, ":npc_reputation_type", lrep_selfrighteous),
                          (eq, ":npc_reputation_type", lrep_debauched),
                          
                          (ge, ":romantic_chemistry", 10),
                          (eq, ":player_possessions", 0),
                          
                          (str_store_string, s14, "str_my_lady_you_are_possessed_of_great_charms_but_no_properties_until_you_obtain_some_to_marry_you_would_be_an_act_of_ingratitude_towards_my_ancestors_and_my_lineage"),
                          
                        (else_try), #you're a nobody - I can do better
                          (this_or_next|eq, ":npc_reputation_type", lrep_selfrighteous),
                          (eq, ":npc_reputation_type", lrep_debauched),
                          
                          (eq, ":player_possessions", 0),
                          
                          (str_store_string, s14, "str_my_lady_you_are_a_woman_of_no_known_family_of_no_possessions__in_short_a_nobody_do_you_think_that_you_are_fit_to_marry_into_may_family"),
                        (else_try), #just not that into you
                          (lt, ":romantic_chemistry", 5),
                          (lt, ":relation_with_player", 20),
                          
                          (neq, ":npc_reputation_type", lrep_debauched),
                          (neq, ":npc_reputation_type", lrep_selfrighteous),
                          
                          (str_store_string, s14, "str_my_lady__forgive_me__the_quality_of_our_bond_is_not_of_the_sort_which_the_poets_tell_us_is_necessary_to_sustain_a_happy_marriage"),
                          
                        (else_try), #you're a liability, given your relation with the liege
                          (eq, ":npc_reputation_type", lrep_cunning),
                          (faction_get_slot, ":leader", slot_faction_leader, "$g_talk_troop_faction"),
                          (str_store_troop_name, s4, ":leader"),
                          (call_script, "script_troop_get_relation_with_troop", ":leader", "trp_player"),
                          (lt, reg0, -10),
                          
                          (str_store_string, s14, "str_um_i_think_that_if_i_want_to_stay_on_s4s_good_side_id_best_not_marry_you"),
                        (else_try),	#part of another faction
                          (gt, "$players_kingdom", 0),
                          (neq, "$players_kingdom", "$g_talk_troop_faction"),
						(faction_get_slot, ":leader", slot_faction_leader, "$g_talk_troop_faction"),
						##diplomacy start+ use gender script
						#(troop_get_type, reg4, ":leader"),
						(call_script, "script_dplmc_store_troop_is_female_reg", ":leader", 4),
						##diplomacy end+
                          
                          (str_store_string, s14, "str_you_serve_another_realm_i_dont_see_s4_granting_reg4herhis_blessing_to_our_union"),
                        (else_try), #there's a competitor
                          (gt, ":competitor", -1),
                          (str_store_troop_name, s4, ":competitor"),
                          
							(str_store_string, s14, "str_madame_my_heart_currently_belongs_to_s4"),
						##diplomacy start+
						#By default these should not be reachable, but future changes may expose them
						#unintentionally.
						(else_try),#redundant: shouldn't be called for betrothed lords
						   (troop_slot_ge, ":npc", slot_troop_betrothed, 1),
						   (troop_get_slot, ":competitor", ":npc", slot_troop_betrothed),
						   (str_store_troop_name, s4, ":competitor"),
						   (str_store_string, s14, "str_madame_my_heart_currently_belongs_to_s4"),
						(else_try),#redundant: shouldn't be called for married lords
						   (troop_slot_ge, ":npc", slot_troop_spouse, 1),
						   (troop_get_slot, ":competitor", ":npc", slot_troop_spouse),
						   (str_store_troop_name, s4, ":competitor"),
						   (str_store_string, s14, "str_madame_my_heart_currently_belongs_to_s4"),
						(else_try),#redundant: shouldn't be called for claimants or kings
						   (this_or_next|is_between, ":npc", kings_begin, kings_end),
							  (is_between, ":npc", pretenders_begin, pretenders_end),
						   #This probably wouldn't ever occur, but put a string here just in case.
						   #The male version is ridiculous.
						   (str_store_string, s14, "str_my_lady_while_i_admire_your_valor_you_will_forgive_me_if_i_tell_you_that_a_woman_like_you_does_not_uphold_to_my_ideal_of_the_feminine_of_the_delicate_and_of_the_pure"),
						##diplomacy end+
						(else_try),
							(lt, ":relation_with_player", 10),
							(assign, ":lord_agrees", 2),

							(str_store_string, s14, "str_my_lady_you_are_a_woman_of_great_spirit_and_bravery_possessed_of_beauty_grace_and_wit_i_shall_give_your_proposal_consideration"),
						(else_try),
							(assign, ":lord_agrees", 1),

							(str_store_string, s14, "str_my_lady_you_are_a_woman_of_great_spirit_and_bravery_possessed_of_beauty_grace_and_wit_i_would_be_most_honored_were_you_to_become_my_wife"),
						(try_end),

						##diplomacy start+ revert register
						(assign, reg1, ":save_reg1"),
						##diplomacy end+
						(assign, reg0, ":lord_agrees"),

					]),
                    
                    
                    #	(
                    #	"npc_decision_checklist_king_chooses_lord_for_center",
                    #	[
                    #	(store_script_param, ":center", 1),
                    
                    #	(store_faction_of_party, ":faction", ":center"),
                    #	(faction_get_slot, ":king", ":faction", slot_faction_leader),
                    
                    #	(assign, ":total_renown_in_faction"),
                    #	(try_for_range, ":lord_iterator", active_npcs_including_player_begin, active_npcs_end),
                    #		(assign, ":lord", ":lord_iterator"),
                    #		(store_faction_of_troop, ":lord_faction", ":lord"),
                    #		(try_begin),
                    #			(eq, ":lord_iterator", "trp_kingdom_heroes_including_player_begin"),
                    #			(assign, ":lord", "trp_player"),
                    #			(assign, ":lord_faction", "$players_kingdom"),
                    #		(try_end),
                    #		(troop_get_slot, ":renown", ":lord", slot_troop_renown),
                    #		(val_add, ":total_renown_in_faction", ":renown"),
                    
                    #		(troop_set_slot, ":lord", slot_troop_temp_slot, 0),
                    #	(try_end),
                    
                    #	(assign, ":total_property_points_in_faction"),
                    #	(try_for_range, ":village", villages_begin, villages_end),
                    
                    #	(try_end),
                    
                    
                    
                    #	(try_begin),
                    
                    #I needed it for myself
                    
                    #The one who captured it was suitably deserving
                    
                    #I had not sufficiently recognized Lord X for his service
                    
                    #	(try_end),
                    
                    
                    #	]),
                    
                    
                    
                    ("courtship_poem_reactions", #parameters from dialog
                      [
                        (store_script_param, ":lady", 1),
                        (store_script_param, ":poem", 2),
                        
                        (troop_get_slot, ":lady_reputation", ":lady", slot_lord_reputation_type),
                        
                        (try_begin),
                          (eq, "$cheat_mode", 1),
                          (assign, reg4, ":poem"),
                          (assign, reg5, ":lady_reputation"),
                          (display_message, "str_poem_choice_reg4_lady_rep_reg5"),
                        (try_end),
                        
                        (try_begin), #conventional ++, ambitious -, adventurous -
                          (eq, ":poem", courtship_poem_tragic),
                          (eq, ":lady_reputation", lrep_conventional),
                          (str_store_string, s11, "str_ah__kais_and_layali__such_a_sad_tale_many_a_time_has_it_been_recounted_for_my_family_by_the_wandering_poets_who_come_to_our_home_and_it_has_never_failed_to_bring_tears_to_our_eyes"),
                          (assign, ":result", 5),
                        (else_try),
                          (eq, ":poem", courtship_poem_tragic),
                          (eq, ":lady_reputation", lrep_ambitious),
                          (str_store_string, s11, "str_kais_and_layali_three_hundred_stanzas_of_pathetic_sniveling_if_you_ask_me_if_kais_wanted_to_escape_heartbreak_he_should_have_learned_to_live_within_his_station_and_not_yearn_for_what_he_cannot_have"),
                          (assign, ":result", 0),
                        (else_try),
                          (eq, ":poem", courtship_poem_tragic),
                          (eq, ":lady_reputation", lrep_otherworldly),
                          (str_store_string, s11, "str_kais_and_layali_no_one_should_ever_have_written_such_a_sad_poem_if_it_was_the_destiny_of_kais_and_layali_to_be_together_than_their_love_should_have_conquered_all_obstacles"),
                          (assign, ":result", 1),
                        (else_try),
                          (eq, ":poem", courtship_poem_tragic),
                          #		moralizing and adventurous
                          (str_store_string, s11, "str_ah_kais_and_layali_a_very_old_standby_but_moving_in_its_way"),
                          (assign, ":result", 3),
                          #Heroic
                        (else_try), #adventurous ++, conventional -1, moralizing -1
                          (eq, ":poem", courtship_poem_heroic),
                          (eq, ":lady_reputation", lrep_adventurous),
                          (str_store_string, s11, "str_the_saga_of_helgered_and_kara_such_happy_times_in_which_our_ancestors_lived_women_like_kara_could_venture_out_into_the_world_like_men_win_a_name_for_themselves_and_not_linger_in_their_husbands_shadow"),
                          (assign, ":result", 5),
                        (else_try), #adventurous ++, conventional -1, moralizing -1
                          (eq, ":poem", courtship_poem_heroic),
                          (eq, ":lady_reputation", lrep_ambitious),
                          (str_store_string, s11, "str_ah_the_saga_of_helgered_and_kara_now_there_was_a_lady_who_knew_what_she_wanted_and_was_not_afraid_to_obtain_it"),
                          (assign, ":result", 2),
                        (else_try), #adventurous ++, conventional -1, moralizing -1
                          (eq, ":poem", courtship_poem_heroic),
                          (eq, ":lady_reputation", lrep_otherworldly),
                          (str_store_string, s11, "str_the_saga_of_helgered_and_kara_a_terrible_tale__but_it_speaks_of_a_very_great_love_if_she_were_willing_to_make_war_on_her_own_family"),
                          (assign, ":result", 2),
                        (else_try), #adventurous ++, conventional -1, moralizing -1
                          (eq, ":poem", courtship_poem_heroic),
                          (eq, ":lady_reputation", lrep_moralist),
                          (str_store_string, s11, "str_the_saga_of_helgered_and_kara_as_i_recall_kara_valued_her_own_base_passions_over_duty_to_her_family_that_she_made_war_on_her_own_father_i_have_no_time_for_a_poem_which_praises_such_a_woman"),
                          (assign, ":result", 0),
                        (else_try), #adventurous ++, conventional -1, moralizing -1
                          (eq, ":poem", courtship_poem_heroic),
                          (eq, ":lady_reputation", lrep_conventional),
                          (str_store_string, s11, "str_the_saga_of_helgered_and_kara_how_could_a_woman_don_armor_and_carry_a_sword_how_could_a_man_love_so_ungentle_a_creature"),
                          (assign, ":result", 0),
                          #Comic
                        (else_try), #ambitious ++, romantic -, moralizing 0
                          (eq, ":poem", courtship_poem_comic),
                          (eq, ":lady_reputation", lrep_otherworldly),
                          (str_store_string, s11, "str_a_conversation_in_the_garden_i_cannot_understand_the_lady_in_that_poem_if_she_loves_the_man_why_does_she_tease_him_so"),
                          (assign, ":result", 0),
                        (else_try), #ambitious ++, romantic -, moralizing 0
                          (eq, ":poem", courtship_poem_comic),
                          (eq, ":lady_reputation", lrep_moralist),
                          (str_store_string, s11, "str_a_conversation_in_the_garden_let_us_see__it_is_morally_unedifying_it_exalts_deception_it_ends_with_a_maiden_surrendering_to_her_base_passions_and_yet_i_cannot_help_but_find_it_charming_perhaps_because_it_tells_us_that_love_need_not_be_tragic_to_be_memorable"),
                          (assign, ":result", 1),
                        (else_try), #ambitious ++, romantic -, moralizing 0
                          (eq, ":poem", courtship_poem_comic),
                          (eq, ":lady_reputation", lrep_ambitious),
                          (str_store_string, s11, "str_a_conversation_in_the_garden_now_that_is_a_tale_every_lady_should_know_by_heart_to_learn_the_subtleties_of_the_politics_she_must_practice"),
                          (assign, ":result", 5),
                        (else_try), #ambitious ++, romantic -, moralizing 0
                          (eq, ":poem", courtship_poem_comic),
                          #adventurous, conventional
                          (str_store_string, s11, "str_a_conversation_in_the_garden_it_is_droll_i_suppose__although_there_is_nothing_there_that_truly_stirs_my_soul"),
                          (assign, ":result", 3),
                          
                          #Allegoric
                        (else_try), #moralizing ++, adventurous -, romantic -
                          (eq, ":poem", courtship_poem_allegoric),
                          (eq, ":lady_reputation", lrep_adventurous),
                          (str_store_string, s11, "str_storming_the_fortress_of_love_ah_yes_the_lady_sits_within_doing_nothing_while_the_man_is_the_one_who_strives_and_achieves_i_have_enough_of_that_in_my_daily_life_why_listen_to_poems_about_it"),
                          (assign, ":result", 0),
                        (else_try), #moralizing ++, adventurous -, romantic -
                          (eq, ":poem", courtship_poem_allegoric),
                          (this_or_next|eq, ":lady_reputation", lrep_conventional),
                          (eq, ":lady_reputation", lrep_moralist),
                          (str_store_string, s11, "str_storming_the_fortress_of_love_ah_yes_an_uplifting_tribute_to_the_separate_virtues_of_man_and_woman"),
                          (assign, ":result", 3),
                        (else_try), #moralizing ++, adventurous -, romantic -
                          (eq, ":poem", courtship_poem_allegoric),
                          (eq, ":lady_reputation", lrep_otherworldly),
                          (str_store_string, s11, "str_storming_the_fortress_of_love_ah_yes_but_although_it_is_a_fine_tale_of_virtues_it_speaks_nothing_of_passion"),
                          (assign, ":result", 1),
                        (else_try), #moralizing ++, adventurous -, romantic -
                          (eq, ":poem", courtship_poem_allegoric),
                          (eq, ":lady_reputation", lrep_ambitious),
                          (str_store_string, s11, "str_storming_the_fortress_of_love_ah_a_sermon_dressed_up_as_a_love_poem_if_you_ask_me"),
                          (assign, ":result", 1),
                          
                        (else_try), #romantic ++, moralizing 0, ambitious -
                          (eq, ":poem", courtship_poem_mystic),
                          (eq, ":lady_reputation", lrep_otherworldly),
                          (str_store_string, s11, "str_a_hearts_desire_ah_such_a_beautiful_account_of_the_perfect_perfect_love_to_love_like_that_must_be_to_truly_know_rapture"),
                          (assign, ":result", 4),
                          
                        (else_try), #romantic ++, moralizing 0, ambitious -
                          (eq, ":poem", courtship_poem_mystic),
                          (eq, ":lady_reputation", lrep_ambitious),
                          (str_store_string, s11, "str_a_hearts_desire_silly_if_you_ask_me_if_the_poet_desires_a_lady_then_he_should_endeavor_to_win_her__and_not_dress_up_his_desire_with_a_pretense_of_piety"),
                          (assign, ":result", 0),
                          
                        (else_try), #romantic ++, moralizing 0, ambitious -
                          (eq, ":poem", courtship_poem_mystic),
                          (eq, ":lady_reputation", lrep_moralist),
                          (str_store_string, s11, "str_a_hearts_desire_hmm__it_is_an_interesting_exploration_of_earthly_and_divine_love_it_does_speak_of_the_spiritual_quest_which_brings_out_the_best_in_man_but_i_wonder_if_the_poet_has_not_confused_his_yearning_for_higher_things_with_his_baser_passions"),
                          (assign, ":result", 2),
                          
                        (else_try), #romantic ++, moralizing 0, ambitious -
                          (eq, ":poem", courtship_poem_mystic),
                          (str_store_string, s11, "str_a_hearts_desire_oh_yes__it_is_very_worthy_and_philosophical_but_if_i_am_to_listen_to_a_bard_strum_a_lute_for_three_hours_i_personally_prefer_there_to_be_a_bit_of_a_story"),
                          (assign, ":result", 1),
                        (try_end),
                        
                        
                        (try_begin),
                          (eq, "$cheat_mode", 1),
                          (assign, reg4, ":result"),
                          (display_message, "str_result_reg4_string_s11"),
                        (try_end),
                        
                        
                        (assign, reg0, ":result"),
                        
                    ]),
                    
                    (
                      "diplomacy_faction_get_diplomatic_status_with_faction",
                      #result: -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
                      [
						(store_script_param, ":actor_faction", 1),
						(store_script_param, ":target_faction", 2),
						##diplomacy start+
						#Since "fac_player_supporters_faction" is used as a shorthand for the faction
						#run by the player, intercept that here instead of the various places this is
						#called from.
						(call_script, "script_dplmc_translate_inactive_player_supporter_faction_2", ":actor_faction", ":target_faction"),
						(assign, ":actor_faction", reg0),
						(assign, ":target_faction", reg1),
						##diplomacy end+
                        
                        (store_add, ":truce_slot", ":target_faction", slot_faction_truce_days_with_factions_begin),
                        (store_add, ":provocation_slot", ":target_faction", slot_faction_provocation_days_with_factions_begin),
                        (val_sub, ":truce_slot", kingdoms_begin),
                        (val_sub, ":provocation_slot", kingdoms_begin),
                        
                        (assign, ":result", 0),
                        (assign, ":duration", 0),
                        
                        (try_begin),
                          (store_relation, ":relation", ":actor_faction", ":target_faction"),
                          (lt, ":relation", 0),
                          (assign, ":result", -2),
                        (else_try),
                          (faction_slot_ge, ":actor_faction", ":truce_slot", 1),
                          (assign, ":result", 1),
                          
                          (faction_get_slot, ":duration", ":actor_faction", ":truce_slot"),
                        (else_try),
                          (faction_slot_ge, ":actor_faction", ":provocation_slot", 1),
                          (assign, ":result", -1),
                          
                          (faction_get_slot, ":duration", ":actor_faction", ":provocation_slot"),
                        (try_end),
                        
                        (assign, reg0, ":result"),
                        (assign, reg1, ":duration"),
                    ]),
                    
                    ("faction_follows_controversial_policy",
                      [
                        (store_script_param, ":faction_no", 1),
                        (store_script_param, ":policy_type", 2),
                        
                        (faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
                        
                        (try_begin),
                          (ge, "$cheat_mode", 1), ##1.134
                          (str_store_faction_name, s3, ":faction_no"),
                          (display_message, "str_calculating_effect_for_policy_for_s3"),
                          
                          (val_add, "$number_of_controversial_policy_decisions", 1), ##1.134
                        (try_end),
                        
                        (try_begin),
                          (eq, ":policy_type", logent_policy_ruler_attacks_without_provocation),
                          (assign, ":hawk_relation_effect", 0),
                          (assign, ":honorable_relation_effect", -2),
                          (assign, ":honor_change", -1),
                          
                        (else_try),
                          (eq, ":policy_type", logent_policy_ruler_ignores_provocation),
                          (assign, ":hawk_relation_effect", -3),
                          (assign, ":honorable_relation_effect", 0),
                          (assign, ":honor_change", 0),
                          
                        (else_try),
                          (eq, ":policy_type", logent_policy_ruler_declares_war_with_justification),
                          (assign, ":hawk_relation_effect", 3),
                          (assign, ":honorable_relation_effect", 1),
                          (assign, ":honor_change", 0),
                          
                        (else_try),
                          (eq, ":policy_type", logent_policy_ruler_breaks_truce),
                          (assign, ":hawk_relation_effect", 0),
                          (assign, ":honorable_relation_effect", -3),
                          (assign, ":honor_change", -5),
                          
                        (else_try),
                          (eq, ":policy_type", logent_policy_ruler_makes_peace_too_soon),
                          (assign, ":hawk_relation_effect", -5),
                          (assign, ":honorable_relation_effect", 0),
                          (assign, ":honor_change", 0),
                          
						 ##diplomacy start+ If none of the preceeding match, don't use random memory
						(else_try),
							(assign, ":hawk_relation_effect", 0),
							(assign, ":honorable_relation_effect", 0),
							(assign, ":honor_change", 0),
						##diplomacy end+ 
                        (try_end),
                        
                        (try_begin),
                          (eq, ":faction_leader", "trp_player"),
                          (call_script, "script_change_player_honor", ":honor_change"),
                        (try_end),
                        
					   ##diplomacy start+ add support for promoted kingdom ladies
						#(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
						(try_for_range, ":lord", heroes_begin, heroes_end),
						##diplomacy end+
							(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
							(store_faction_of_troop, ":lord_faction", ":lord"),
							(eq, ":lord_faction", ":faction_no"),
							(neq, ":lord", ":faction_leader"),

							(try_begin),
							   ##diplomacy start+ Add support for lady personality type
								(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_adventurous),
								##diplomacy end+
								(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_martial),
								(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_quarrelsome),
								(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_selfrighteous),
									(troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_debauched),
								(call_script, "script_troop_change_relation_with_troop", ":faction_leader", ":lord", ":hawk_relation_effect"),
								(val_add, "$total_policy_dispute_changes", ":hawk_relation_effect"),
							(try_end),

							(try_begin),
							   ##diplomacy start+ Add support for lady personality type
								(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_moralist),
								##diplomacy end+
								(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_martial),
								(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_goodnatured),
								(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_selfrighteous),
								(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_benefactor), #new for enfiefed commoners
								(this_or_next|troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_custodian), #new for enfiefed commoners
									(troop_slot_eq, ":lord", slot_lord_reputation_type, lrep_upstanding),
								(call_script, "script_troop_change_relation_with_troop", ":faction_leader", ":lord", ":honorable_relation_effect"),
								(val_add, "$total_policy_dispute_changes", ":honorable_relation_effect"),

							(try_end),

						(try_end),

					]),
                    
                    
                    ("internal_politics_rate_feast_to_s9",
                      [
                        (store_script_param, ":householder", 1),
                        (store_script_param, ":num_servings", 2),
                        #	(store_script_param, ":faction", 3),
                        (store_script_param, ":consume_items", 4),
                        
                        (val_max, ":num_servings", 1),
                        
                        (try_for_range, ":item", trade_goods_begin, trade_goods_end),
                          (item_set_slot, ":item", slot_item_amount_available, 0), #had no "item"
                        (try_end),
                        
                        (troop_get_inventory_capacity, ":capacity", ":householder"),
                        (try_for_range, ":inventory_slot", 0, ":capacity"),
                          (troop_get_inventory_slot, ":item", ":householder", ":inventory_slot"),
                          (is_between, ":item", trade_goods_begin, trade_goods_end),
                          (troop_inventory_slot_get_item_amount, ":slot_amount", ":householder", ":inventory_slot"),
                          (item_get_slot, ":item_amount", ":item", slot_item_amount_available),
                          (val_add, ":item_amount", ":slot_amount"),
                          (item_set_slot, ":item", slot_item_amount_available, ":item_amount"),
                        (try_end),
                        #food
                        (assign, ":food_amount", 0),
                        (assign, ":food_variety", 0),
                        
                        (store_div, ":servings_div_by_12", ":num_servings", 12),
                        (try_for_range, ":food_item", food_begin, food_end),
                          (item_get_slot, ":food_in_slot", ":food_item", slot_item_amount_available),
                          (val_add, ":food_amount", ":food_in_slot"),
                          
                          
                          ##		(str_store_item_name, s4, ":food_item"),
                          ##		(assign, reg3, ":food_in_slot"),
                          ##		(assign, reg5, ":servings_div_by_12"),
                          ##		(display_message, "str_reg3_units_of_s4_for_reg5_guests_and_retinue"),
                          
                          
                          (ge, ":food_in_slot", ":servings_div_by_12"),
                          (val_add, ":food_variety", 1),
                        (try_end),
                        
                        (val_mul, ":food_amount", 100),
                        (val_div, ":food_amount", ":num_servings"), #1 to 100 for each
                        (val_min, ":food_amount", 100),
                        
                        (val_mul, ":food_variety", 85), #1 to 100 for each
                        (val_div, ":food_variety", 10),
                        (val_min, ":food_variety", 100),
                        
                        #drink
                        (assign, ":drink_amount", 0),
                        (assign, ":drink_variety", 0),
                        (store_div, ":servings_div_by_4", ":num_servings", 4),
                        (try_for_range, ":drink_iterator", "itm_trade_wine", "itm_trade_smoked_fish"),
                          (assign, ":drink_item", ":drink_iterator"),
                          (item_get_slot, ":drink_in_slot", ":drink_item", slot_item_amount_available),
                          
                          (val_add, ":drink_amount", ":drink_in_slot"),
                          
                          (ge, ":drink_in_slot", ":servings_div_by_4"),
                          (val_add, ":drink_variety", 1),
                        (try_end),
                        
                        (val_mul, ":drink_amount", 200), #amount needed is 50% of the number of guests
                        (val_max, ":num_servings", 1),
                        
                        (val_div, ":drink_amount", ":num_servings"), #1 to 100 for each
                        (val_min, ":drink_amount", 100),
                        (val_mul, ":drink_variety", 50), #1 to 100 for each
                        
                        #in the future, it might be worthwhile to add different varieties of spices
                        (item_get_slot, ":spice_amount", "itm_trade_spice", slot_item_amount_available),
                        (store_mul, ":spice_percentage", ":spice_amount", 100),
                        (val_max, ":servings_div_by_12", 1),
                        (val_div, ":spice_amount", ":servings_div_by_12"),
                        (val_min, ":spice_percentage", 100),
                        ##	(assign, reg3, ":spice_amount"),
                        ##	(assign, reg5, ":servings_div_by_12"),
                        ##	(assign, reg6, ":spice_percentage"),
                        ##	(display_message, "str_reg3_units_of_spice_of_reg5_to_be_consumed"),
                        
                        #oil availability. In the future, this may become an "atmospherics" category, including incenses
                        (item_get_slot, ":oil_amount", "itm_trade_oil", slot_item_amount_available),
                        (store_mul, ":oil_percentage", ":oil_amount", 100),
                        (val_max, ":servings_div_by_12", 1),
                        (val_div, ":oil_amount", ":servings_div_by_12"),
                        (val_min, ":oil_percentage", 100),
                        ##	(assign, reg3, ":oil_amount"),
                        ##	(assign, reg5, ":servings_div_by_12"),
                        ##	(assign, reg6, ":oil_percentage"),
                        ##	(display_message, "str_reg3_units_of_oil_of_reg5_to_be_consumed"),
                        
                        (store_div, ":food_amount_string", ":food_amount", 20),
                        (val_add, ":food_amount_string", "str_feast_description"),
                        (str_store_string, s8, ":food_amount_string"),
                        (str_store_string, s9, "str_of_food_which_must_come_before_everything_else_the_amount_is_s8"),
                        
                        (store_div, ":food_variety_string", ":food_variety", 20),
                        (val_add, ":food_variety_string", "str_feast_description"),
                        (str_store_string, s8, ":food_variety_string"),
                        (str_store_string, s9, "str_s9_and_the_variety_is_s8_"),
                        
                        (store_div, ":drink_amount_string", ":drink_amount", 20),
                        (val_add, ":drink_amount_string", "str_feast_description"),
                        (str_store_string, s8, ":drink_amount_string"),
                        (str_store_string, s9, "str_s9_of_drink_which_guests_will_expect_in_great_abundance_the_amount_is_s8"),
                        
                        (store_div, ":drink_variety_string", ":drink_variety", 20),
                        (val_add, ":drink_variety_string", "str_feast_description"),
                        (str_store_string, s8, ":drink_variety_string"),
                        (str_store_string, s9, "str_s9_and_the_variety_is_s8_"),
                        
                        (store_div, ":spice_string", ":spice_percentage", 20),
                        (val_add, ":spice_string", "str_feast_description"),
                        (str_store_string, s8, ":spice_string"),
                        (str_store_string, s9, "str_s9_of_spice_which_is_essential_to_demonstrate_that_we_spare_no_expense_as_hosts_the_amount_is_s8_"),
                        
                        (store_div, ":oil_string", ":oil_percentage", 20),
                        (val_add, ":oil_string", "str_feast_description"),
                        (str_store_string, s8, ":oil_string"),
                        (str_store_string, s9, "str_s9_of_oil_which_we_shall_require_to_light_the_lamps_the_amount_is_s8"),
                        
                        (store_mul, ":food_amount_cap", ":food_amount", 8),
                        (store_add, ":total", ":food_amount", ":food_variety"),
                        (val_mul, ":total", 2), #x4
                        (val_add, ":total", ":drink_variety"),
                        (val_add, ":total", ":drink_amount"), #x6
                        (val_add, ":total", ":spice_amount"), #x7
                        (val_add, ":total", ":oil_amount"), #x8
                        (val_min, ":total", ":food_amount_cap"),
                        (val_div, ":total", 8),
                        (val_clamp, ":total", 1, 101),
                        (store_div, ":total_string", ":total", 20),
                        (val_add, ":total_string", "str_feast_description"),
                        (str_store_string, s8, ":total_string"),
                        (str_store_string, s9, "str_s9_overall_our_table_will_be_considered_s8"),
                        
                        (assign, reg0, ":total"), #zero to 100
                        
                        
                        
                        (try_begin),
                          (eq, ":consume_items", 1),
                          
                          (assign, ":num_of_servings_to_serve", ":num_servings"),
                          (try_for_range, ":unused", 0, 1999),
                            (gt, ":num_of_servings_to_serve", 0),
                            
                            (try_for_range, ":item", trade_goods_begin, trade_goods_end),
                              (item_set_slot, ":item", slot_item_is_checked, 0),
                            (try_end),
                            
                            (troop_get_inventory_capacity, ":inv_size", ":householder"),
                            (try_for_range, ":i_slot", 0, ":inv_size"),
                              (troop_get_inventory_slot, ":item", ":householder", ":i_slot"),
                              (this_or_next|eq, ":item", "itm_trade_spice"),
                              (this_or_next|eq, ":item", "itm_trade_oil"),
                              (this_or_next|eq, ":item", "itm_trade_wine"),
                              (this_or_next|eq, ":item", "itm_trade_ale"),
                              (is_between, ":item",  food_begin, food_end),
                              (item_slot_eq, ":item", slot_item_is_checked, 0),
                              (troop_inventory_slot_get_item_amount, ":cur_amount", ":householder", ":i_slot"),
                              (gt, ":cur_amount", 0),
                              
                              (val_sub, ":cur_amount", 1),
                              (troop_inventory_slot_set_item_amount, ":householder", ":i_slot", ":cur_amount"),
                              (val_sub, ":num_of_servings_to_serve", 1),
                              (item_set_slot, ":item", slot_item_is_checked, 1),
                            (try_end),
                          (try_end),																		#	1.143 Port // fixed try_begin to try_end
                        (try_end),
                        ]),
                        
                        
                        ("faction_get_adjective_to_s10",
                          [
                            (store_script_param, ":faction_no", 1),
                            
                            #Diplomacy 3.2 begin
                            (try_begin),
                              (eq, ":faction_no", "fac_player_faction"),
                              (assign, ":faction_no", "$players_kingdom"),
                            (try_end),
                            
                            
                            (try_begin),
                              (eq, ":faction_no", "fac_player_supporters_faction"),
                              (str_store_string, s10, "str_rebel"),
                            (else_try),
                              (this_or_next|eq, ":faction_no", "fac_outlaws"),
                              (this_or_next|eq, ":faction_no", "fac_mountain_bandits"),
                              (this_or_next|eq, ":faction_no", "fac_forest_bandits"),
                              (eq, ":faction_no", "fac_deserters"),
                              (str_store_string, s10, "str_bandit"),
                            (else_try),
                              (faction_get_slot, ":adjective_string", ":faction_no", slot_faction_adjective),
                              (str_store_string, s10, ":adjective_string"),
                            (try_end),
                        ]),
                        #Diplomacy 3.2 end
                        
                        ("setup_tavern_attacker",
                          [
                            (store_script_param, ":cur_entry", 1),
                            
                            (try_begin),
                              (neg|troop_slot_eq, "trp_hired_assassin", slot_troop_cur_center, "$g_encountered_party"),
                              (troop_slot_eq, "trp_belligerent_drunk", slot_troop_cur_center, "$g_encountered_party"),
                              (set_visitor, ":cur_entry", "trp_belligerent_drunk"),
                            (try_end),
                            
                            (try_begin),
                              (troop_slot_eq, "trp_hired_assassin", slot_troop_cur_center, "$g_encountered_party"),
                              (set_visitor, ":cur_entry", "trp_hired_assassin"),
                            (try_end),
                        ]),
                        
                        ("activate_tavern_attackers",
                          [
                            (set_party_battle_mode),
                            (try_for_agents, ":cur_agent"),
                              (agent_get_troop_id, ":cur_agent_troop", ":cur_agent"),
                              (this_or_next|eq, ":cur_agent_troop", "trp_fugitive"),
                              (this_or_next|eq, ":cur_agent_troop", "trp_belligerent_drunk"),
                              (eq, ":cur_agent_troop", "trp_hired_assassin"),
                              (agent_set_team, ":cur_agent", 1),
                              (assign, "$g_main_attacker_agent", ":cur_agent"),
                              (agent_ai_set_aggressiveness, ":cur_agent", 199),
                            (try_end),
                        ]),
                        
                        ("deactivate_tavern_attackers",
                          [
                            (finish_party_battle_mode),
                            (try_for_agents, ":cur_agent"),
                              (agent_get_troop_id, ":cur_agent_troop", ":cur_agent"),
                              (this_or_next|eq, ":cur_agent_troop", "trp_fugitive"),
                              (this_or_next|eq, ":cur_agent_troop", "trp_belligerent_drunk"),
                              (eq, ":cur_agent_troop", "trp_hired_assassin"),
                              (agent_set_team, ":cur_agent", 0),
                              (agent_ai_set_aggressiveness, ":cur_agent", 0),
                            (try_end),
                        ]),
                        
                        ("activate_town_guard",
                          [
                            (set_party_battle_mode),
                            #(get_player_agent_no, ":player_agent"),
                            #(agent_get_team, ":player_team", ":player_agent"),
                            
                            (try_for_agents, ":cur_agent"),
                              (agent_get_troop_id, ":troop_type", ":cur_agent"),
                              (is_between, ":troop_type", "trp_swadian_n_peasant", "trp_bandit_n_looter"),
                              (agent_set_team, ":cur_agent", 1),
                              #(team_give_order, 1, grc_everyone, mordr_charge), - for some reason, this freezes everyone if the player is not yet spawned
                              #(try_begin),
                              #	(eq, "$g_main_attacker_agent", 0),
                              #	(assign, "$g_main_attacker_agent", ":cur_agent"),
                              #(try_end),
                            (else_try),
                              (this_or_next|is_between, ":cur_agent", walkers_begin, walkers_end),
                              (is_between, ":cur_agent", armor_merchants_begin, mayors_end),
                              
                              (agent_clear_scripted_mode, ":cur_agent"),
                              (agent_set_team, ":cur_agent", 2),
                            (try_end),
                        ]),
                        
                        
                        #this determines whether or not a lord is thrown into a dungeon by his captor, or is kept out on parole
                        #Not currently used (ie, it always fails)
                        ("cf_prisoner_offered_parole",
                          [
                            (store_script_param, ":prisoner", 1),
                            
                            (eq, 1, 0), #disabled, this will always return false
                            
                            (troop_get_slot, ":captor_party", ":prisoner", slot_troop_prisoner_of_party),
                            (party_is_active, ":captor_party"),
                            (is_between, ":captor_party", walled_centers_begin, walled_centers_end),
                            (party_get_slot, ":captor", ":captor_party", slot_town_lord),
                            
                            (troop_get_slot, ":prisoner_rep", ":prisoner", slot_lord_reputation_type),
                            (troop_get_slot, ":captor_rep", ":captor", slot_lord_reputation_type),
                            
                            (neq, ":prisoner_rep", lrep_debauched),
                            (neq, ":captor_rep", lrep_debauched),
                            (neq, ":captor_rep", lrep_quarrelsome),
                            
                            #Prisoner is a noble, or lord is goodnatured
                            (this_or_next|eq, ":captor_rep", lrep_goodnatured),
                            (this_or_next|troop_slot_eq, ":prisoner", slot_troop_occupation, slto_kingdom_hero),
                            (troop_slot_eq, ":prisoner", slot_troop_occupation, slto_kingdom_lady),
                            
                            (call_script, "script_troop_get_relation_with_troop", ":captor", ":prisoner"),
                            ##	(display_message, "str_relation_of_prisoner_with_captor_is_reg0"),
                            (ge, reg0, -10),
                        ]),
                        
                        ("neutral_behavior_in_fight",
                          [
                            (get_player_agent_no, ":player_agent"),
                            (agent_get_position, pos3, ":player_agent"),
                            (agent_get_team, ":player_team", ":player_agent"),
                            
                            (try_begin),
                              (gt, "$g_main_attacker_agent", 0),
							  (agent_is_active, "$g_main_attacker_agent"), #Floris - bugfix
                              (agent_get_team, ":attacker_team_no", "$g_main_attacker_agent"),
                              (agent_get_position, pos5, "$g_main_attacker_agent"),
                            (else_try),
                              #(eq, ":attacker_team_no", -1), #Floris - bugfix - stupid native coding
							  (assign, ":attacker_team_no", -1), #Floris - bugfix
                              (agent_get_position, pos5, ":player_agent"),
                            (try_end),
                            
                            (set_fixed_point_multiplier, 100),
                            
                            (try_for_agents, ":agent"),
                              (agent_get_team, ":other_team", ":agent"),
                              (neq, ":other_team", ":attacker_team_no"),
                              (neq, ":other_team", ":player_team"),
                              
                              (agent_get_troop_id, ":troop_type", ":agent"),
                              (neg|is_between, ":troop_type", kingdom_troops_begin, "trp_bandit_n_looter"), ##FLORIS - MTT
                              
                              (agent_get_position, pos4, ":agent"),
                              
                              (assign, ":best_position_score", 0),
                              (assign, ":best_position", -1),
                              
                              (try_begin),
                                (neg|agent_slot_eq, ":agent", slot_agent_is_running_away, 0), #if agent is running away
                                (agent_get_slot, ":target_entry_point_plus_one",  ":agent", slot_agent_is_running_away),
                                (store_sub, ":target_entry_point", ":target_entry_point_plus_one", 1),
                                (entry_point_get_position, pos6, ":target_entry_point"),
                                (get_distance_between_positions, ":agent_distance_to_target", pos6, pos4),
                                (lt, ":agent_distance_to_target", 100),
                                (agent_set_slot, ":agent", slot_agent_is_running_away, 0),
                              (try_end),
                              
                              (agent_slot_eq, ":agent", slot_agent_is_running_away, 0), #if agent is not already running away
                              
                              (try_begin), #stand in place
                                (get_distance_between_positions, ":distance", pos4, pos5),
                                (get_distance_between_positions, ":distance_to_player", pos4, pos3),
                                
                                (val_min, ":distance", ":distance_to_player"),
                                
                                (this_or_next|gt, ":distance", 700), #7 meters away from main belligerents
                                (main_hero_fallen),
                                
                                (agent_set_scripted_destination, ":agent", pos4),
                              (else_try), #get out of the way
                                (try_for_range, ":target_entry_point", 0, 64),
                                  (neg|entry_point_is_auto_generated, ":target_entry_point"),
                                  (entry_point_get_position, pos6, ":target_entry_point"),
                                  (get_distance_between_positions, ":agent_distance_to_target", pos6, pos4),
                                  (get_distance_between_positions, ":player_distance_to_target", pos6, pos3),
                                  (store_sub, ":position_score", ":player_distance_to_target", ":agent_distance_to_target"),
                                  (ge, ":position_score", 0),
                                  (try_begin),
                                    (ge, ":agent_distance_to_target", 2000),
                                    (store_sub, ":extra_distance", ":agent_distance_to_target", 2000),
                                    (val_min, ":extra_distance", 1000),
                                    (val_min, ":agent_distance_to_target", 2000), #if more than 10 meters assume it is 10 meters far while calculating best run away target
                                    (val_sub, ":agent_distance_to_target", ":extra_distance"),
                                  (try_end),
                                  (val_mul, ":position_score", ":agent_distance_to_target"),
                                  (try_begin),
                                    (ge, ":position_score", ":best_position_score"),
                                    (assign, ":best_position_score", ":position_score"),
                                    (assign, ":best_position", ":target_entry_point"),
                                  (try_end),
                                (try_end),
                                
                                (try_begin),
                                  (ge, ":best_position", 0),
                                  (entry_point_get_position, pos6, ":best_position"),
                                  (agent_set_speed_limit, ":agent", 10),
                                  (agent_set_scripted_destination, ":agent", pos6),
                                  (store_add, ":best_position_plus_one", ":best_position", 1),
                                  (agent_set_slot, ":agent", slot_agent_is_running_away, ":best_position_plus_one"),
                                (try_end),
                              (try_end),
                            (try_end),
                        ]),
                        
                        ("party_inflict_attrition", #parameters from dialog
                          [
                            (store_script_param, ":party", 1),
                            (store_script_param, ":attrition_rate", 2),
						#	(store_script_param, ":attrition_type", 3), #1 = desertion, 2 = sickness
						##diplomacy start+
							(store_script_param, ":unused", 3), #1 = desertion, 2 = sickness
						##diplomacy end+
                            
                            (party_clear, "p_temp_casualties"),
                            
                            (party_get_num_companion_stacks, ":num_stacks", ":party"),
                            
                            #add to temp casualties
                            (try_for_range, ":stack", 0, ":num_stacks"),
                              (party_stack_get_troop_id, ":troop_type", ":party", ":stack"),
                              (neg|troop_is_hero, ":troop_type"),
                              (party_stack_get_size, ":size", ":party", ":stack"),
                              (store_mul, ":casualties_x_100", ":attrition_rate", ":size"),
                              (store_div, ":casualties", ":casualties_x_100", 100),
                              (party_add_members, "p_temp_casualties", ":troop_type", ":casualties"),
                              
                              (store_mul, ":subtractor", ":casualties", 100),
                              (store_sub, ":chance_of_additional_casualty", ":casualties_x_100", ":subtractor"),
                              
                              (try_begin),
                                (gt, ":chance_of_additional_casualty", 0),
                                (store_random_in_range, ":random", 0, 100),
                                (lt, ":random", ":chance_of_additional_casualty"),
                                (party_add_members, "p_temp_casualties", ":troop_type", ":casualties"),
                              (try_end),
                              
                              #		(try_begin),
                              #			(eq, "$cheat_mode", 1),
                              #			(str_store_party_name, s7, ":party"),
                              #           		...
                              #		(try_end),
                            (try_end),
                            
                            #take temp casualties from main party
                            (party_get_num_companion_stacks, ":num_stacks", "p_temp_casualties"),
                            
                            #add to temp casualties
                            (try_for_range, ":stack", 0, ":num_stacks"),
                              (party_stack_get_troop_id, ":troop_type", "p_temp_casualties", ":stack"),
                              (party_stack_get_size, ":size", "p_temp_casualties", ":stack"),
                              (party_remove_members, ":party", ":troop_type", ":size"),
                              
                              (eq, "$cheat_mode", 1),
                              (assign, reg3, ":size"),
                              (str_store_troop_name, s4, ":troop_type"),
                              (str_store_party_name, s5, ":party"),
                              #		(display_message, "str_s5_suffers_attrition_reg3_x_s4"),
                              (str_store_string, s65, "str_s5_suffers_attrition_reg3_x_s4"),
                              (display_message, "str_s65"),
                              (try_begin),
                                (eq, "$debug_message_in_queue", 0),
                                (call_script, "script_add_notification_menu", "mnu_debug_alert_from_s65", 0, 0),
                                (assign, "$debug_message_in_queue", 1),
                              (try_end),
                            (try_end),
                            
                        ]),
                        
                        
                        
                        ##diplomacy start+ (documentation only)
						# 
						# Registers changed:
						#   reg4 - (sometimes, cheat only) current troop rumor of :object_1 or :object_2
						#
						# String registers changed:
						#    s10 - speaker name
						#    s11 - the third argument
						#     s1 - the date
						#     s5 - str_s10_said_on_s1_s11__
						#     s3 - (sometimes, cheat only) the troop name of :object_1 or :object_2
						#
						#
						# Diplomacy+ mod change:
						# - Use reg4 to contain the gender of the subject of a rumor string 
						##diplomacy end+ (documentation only)
                        ("add_rumor_string_to_troop_notes", #parameters from dialog
                          [
                            (store_script_param, ":object_1", 1),
                            (store_script_param, ":object_2", 2),
                            (store_script_param, ":string", 3),
                            
                            (str_store_troop_name, s10, "$g_talk_troop"),
                            (str_store_string_reg, s11, ":string"),
                            
                            (store_current_hours, ":hours"),
                            (call_script, "script_game_get_date_text", 0, ":hours"),
                            
                            (str_store_string, s5, "str_s10_said_on_s1_s11__"),
                            
                            (try_begin),
                              (is_between, ":object_1", active_npcs_begin, kingdom_ladies_end),
                              (troop_get_slot, ":current_rumor_note", ":object_1", slot_troop_current_rumor),
                              (val_add, ":current_rumor_note", 1),
                              (try_begin),
                                (neg|is_between, ":current_rumor_note", 3, 16),
                                (assign, ":current_rumor_note", 3),
                              (try_end),
                              (troop_set_slot, ":object_1", slot_troop_current_rumor, ":current_rumor_note"),
                              
                              (add_troop_note_from_sreg, ":object_1", ":current_rumor_note", s5, 0), #troop, note slot, string, show
                              
                              (try_begin),
                                (eq, "$cheat_mode", 1),
                                (str_store_troop_name, s3, ":object_1"),
                                (assign, reg4, ":current_rumor_note"),
                                (display_message, "str_rumor_note_to_s3s_slot_reg4_s5"),
                              (try_end),
                            (try_end),
                            
                            (try_begin),
                              (is_between, ":object_2", active_npcs_begin, kingdom_ladies_end),
                              (troop_get_slot, ":current_rumor_note", ":object_2", slot_troop_current_rumor),
                              (val_add, ":current_rumor_note", 1),
                              (try_begin),
                                (neg|is_between, ":current_rumor_note", 3, 16),
                                (assign, ":current_rumor_note", 3),
                              (try_end),
                              (troop_set_slot, ":object_2", slot_troop_current_rumor, ":current_rumor_note"),
                              
                              (add_troop_note_from_sreg, ":object_2", ":current_rumor_note", s5, 0), #troop, note slot, string, show
                              
                              (try_begin),
                                (eq, "$cheat_mode", 1),
                                (str_store_troop_name, s3, ":object_2"),
                                (assign, reg4, ":current_rumor_note"),
                                (display_message, "str_rumor_note_to_s3s_slot_reg4_s5"),
                              (try_end),
                            (try_end),
                        ]),
                        
                        ("character_can_wed_character", #empty now, but might want to add mid-game
                          [
                        ]),
                        
                        ("troop_change_career", #empty now, but might want to add mid-game
                          [
                        ]),
                        
                        ("center_get_goods_availability",
                          [
                            (store_script_param, ":center_no", 1),
                            
                            (str_store_party_name, s4, ":center_no"),
                            
                            (assign, ":hardship_index", 0),
                            (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
                              
                              #Must have consumption of at least 4 to be relevant
                              #This prevents perishables and raw materials from having a major impact
                              (try_begin),
                                (is_between, ":center_no", villages_begin, villages_end),
                                (item_get_slot, ":consumer_consumption", ":cur_good", slot_item_rural_demand),
                              (else_try),
                                (item_get_slot, ":consumer_consumption", ":cur_good", slot_item_urban_demand),
                              (try_end),
                              (gt, ":consumer_consumption", 2),

                              (store_div, ":max_impact", ":consumer_consumption", 4), #was 4, dropped 3 again 4 now
	
                              #High-demand items like grain tend to have much more dramatic price differentiation, so they yield substantially higher results than low-demand items
                              
                              (store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
                              (val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
                              (party_get_slot, ":price", ":center_no", ":cur_good_price_slot"),

							  (store_sub, ":price_differential", ":price", 1000),
							  (gt, ":price_differential", 200), #was 100
  
  							  (val_div, ":price_differential", 200),
                              (val_min, ":price_differential", ":max_impact"),
                              
                              (val_add, ":hardship_index", ":price_differential"),
                            (try_end),
                            
                            (assign, reg0, ":hardship_index"),
                            
                            (try_begin),																		#	1.143 Port // uncommented
								(eq, "$cheat_mode", 1),
								(display_message, "@{!}DEBUG -- hardship index for {s4} = {reg0}"),				
                            (try_end),																			#	End
                        ]),	
                        
						("lord_find_alternative_faction", #Also, make it so that lords will try to keep at least one center unassigned				Diplo 4 // Decided to copy over 1.143 Port
						[
						  (store_script_param, ":troop_no", 1),
						  (store_faction_of_troop, ":orig_faction", ":troop_no"),

						  (assign, ":new_faction", -1),
						  (assign, ":score_to_beat", -5),
						  ##diplomacy start+
						  (troop_get_slot, ":true_original_faction", ":troop_no", slot_troop_original_faction),#not necessarily ":orig_faction"
						  (assign, ":original_culture", -2),
						  (try_begin),
							 (gt, ":true_original_faction", 0),
							 (faction_get_slot, ":original_culture", ":true_original_faction", slot_faction_culture),
							 (lt, ":original_culture", 1),
							 (assign, ":original_culture", ":true_original_faction"),
						  (try_end),
						  ##diplomacy end+

						  #Factions with an available center
						  (try_for_range, ":center_no", centers_begin, centers_end),
							(this_or_next|party_slot_eq, ":center_no", slot_town_lord, stl_unassigned),
							(party_slot_eq, ":center_no", slot_town_lord, stl_rejected_by_player),
							(store_faction_of_party, ":center_faction", ":center_no"),
							(neq, ":center_faction", ":orig_faction"),
							(faction_get_slot, ":liege", ":center_faction", slot_faction_leader),
							(this_or_next|neq, ":liege", "trp_player"),
							(ge, "$player_right_to_rule", 25),
							(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":liege"),
							(assign, ":liege_relation", reg0),

							##diplomacy start+
							(try_begin),
								(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
								#If behavioral changes are enabled, bias heavily towards joining the
								#faction that contains your home (if you have one), or that has the
								#greatest cultural similarity.
								(ge, reg0, 0),
								(try_begin),
									(this_or_next|troop_slot_eq, ":troop_no", slot_troop_original_faction, ":center_faction"),
									(this_or_next|party_slot_eq, ":center_no", dplmc_slot_center_original_lord, ":troop_no"),
										(troop_slot_eq, ":troop_no", slot_troop_home, ":center_no"),
									(val_add, ":liege_relation", 20),
								(else_try),
									(gt, ":true_original_faction", 0),
									(party_slot_eq, ":center_no", slot_center_original_faction, ":true_original_faction"),
									(val_add, ":liege_relation", 5),
								(else_try),
									(gt, ":original_culture", 0),
									(faction_slot_eq, ":center_faction", slot_faction_culture, ":original_culture"),
									(val_add, ":liege_relation", 5),
								(try_end),
							(try_end),
							##diplomacy end+

							(gt, ":liege_relation", ":score_to_beat"),
							(assign, ":new_faction", ":center_faction"),
							(assign, ":score_to_beat", ":liege_relation"),
						  (try_end),

						  #Factions without an available center
						  (try_begin),
							(eq, ":new_faction", -1),
							(assign, ":score_to_beat", 0),
							 #diplomacy start+
							 #If AI changes are explicitly enabled, slightly ease the requirements for entry.
							 (try_begin),
								(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
								(assign, ":score_to_beat", -5),
							 (try_end),
							 (store_add, ":min_acceptable_score", ":score_to_beat", 1),#used below
							 ##diplomacy end+

							(try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
							  (faction_slot_eq, ":kingdom", slot_faction_state, sfs_active),
							  (faction_get_slot, ":liege", ":kingdom", slot_faction_leader),
							  (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":liege"),
							  (assign, ":liege_relation", reg0),

							  ##diplomacy start+
							  (try_begin),
									(neq, ":kingdom", ":orig_faction"),
									(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
									#If behavioral changes are enabled, base your decision in part
									#on how many friends you have in the faction.
									(ge, reg0, ":min_acceptable_score"),
									(try_for_range, ":lord", heroes_begin, heroes_end),
										(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
										(neq, ":lord", ":troop_no"),
										(neq, ":lord", ":liege"),
										(store_faction_of_troop, ":lord_faction", ":lord"),
										(eq, ":lord_faction", ":kingdom"),
										(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":lord"),
										(try_begin),
											(ge, reg0, 20),
											(val_add, ":liege_relation", 1),
										(else_try),
											(lt, reg0, -19),
											(val_sub, ":liege_relation", 1),
										(try_end),
									(try_end),
									#Also give a bonus towards rejoining the lord's original faction.
									#if it isn't the one the lord has just left.
									(try_begin),
										(eq, ":true_original_faction", ":kingdom"),
										(val_add, ":liege_relation", 5),
									(else_try),
										#Not the same but similar
										(gt, ":original_culture", 0),
										(faction_slot_eq, ":kingdom", slot_faction_culture, ":original_culture"),
										(val_add, ":liege_relation", 2),
									(try_end),
									#The next bit is to prevent this change from increasing the number of
									#lords who find all kingdoms unacceptable.
									(val_max, ":liege_relation", ":min_acceptable_score"),
							  (try_end),
							  ##diplomacy end+

							  (gt, ":liege_relation", ":score_to_beat"),

							  (assign, ":new_faction", ":kingdom"),
							  (assign, ":score_to_beat", ":liege_relation"),
							(try_end),
						  (try_end),

						  (assign, reg0, ":new_faction"),
						]),
                        
                        ("set_up_duel_with_troop", #now the setup is handled through the menu
                          [
                            (store_script_param, "$g_duel_troop", 1),
                            (assign, "$g_start_arena_fight_at_nearest_town", 1),
                            (try_begin),
                              (eq, "$g_start_arena_fight_at_nearest_town", 1),
                            (try_end),
                            (unlock_achievement, ACHIEVEMENT_PUGNACIOUS_D),
                            (jump_to_menu, "mnu_arena_duel_fight"),
                            (finish_mission),
                            
                        ]),
                        
                        ("test_player_for_career_and_marriage_incompatability", #empty now, but might want to add mid-game
                          [
                            #Married to a lord of one faction, while fighting for another
                            #Married to one lord while holding a stipend from the king
                        ]),
                        
                        ("deduct_casualties_from_garrison", #after a battle in a center, deducts any casualties from "$g_encountered_party"
                          [
                            ##(display_message, "str_totalling_casualties_caused_during_mission"),
                            
                            (try_for_agents, ":agent"),
                              (agent_get_troop_id, ":troop_type", ":agent"),
                              (is_between, ":troop_type", regular_troops_begin, regular_troops_end),
                              
                              (neg|agent_is_alive, ":agent"),
                              
                              (try_begin), #if troop not present, search for another type which is
                                (store_troop_count_companions, ":number", ":troop_type", "$g_encountered_party"),
                                (eq, ":number", 0),
                                (assign, ":troop_type", 0),
                                (try_for_range, ":new_tier", slot_faction_tier_1_troop, slot_faction_tier_5_troop),
                                  (faction_get_slot, ":troop_type", "$g_encountered_party_faction", ":new_tier"),
                                  (faction_get_slot, ":new_troop_type", "$g_encountered_party_faction", ":new_tier"),
                                  (store_troop_count_companions, ":number", ":new_troop_type", "$g_encountered_party"),
                                  (gt, ":number", 0),
                                  (assign, ":troop_type", ":new_troop_type"),
                                (try_end),
                              (try_end),
                              
                              (gt, ":troop_type", 0),
                              
                              (party_remove_members, "$g_encountered_party", ":troop_type", 1),
                              (str_store_troop_name, s4, ":troop_type"),
                              (str_store_party_name, s5, "$g_encountered_party"),
                            (try_end),
                        ]),
                        
                        ("npc_decision_checklist_take_stand_on_issue",
                          #Called from dialogs, and from simple_triggers
                          
                          #This a very inefficient checklist, and if I did it again, I would score for each troop. That way the troop could answer "why not" to an individual lord
                          [
                            (store_script_param, ":troop_no", 1),
                            (store_faction_of_troop, ":troop_faction", ":troop_no"),
                            
                            (assign, ":result", -1),
                            (faction_get_slot, ":faction_issue", ":troop_faction", slot_faction_political_issue),
                            
                            (assign, ":player_declines_honor", 0),
                            (try_begin),
                              (is_between, ":faction_issue", centers_begin, centers_end),
                              (gt, "$g_dont_give_fief_to_player_days", 1),
                              (assign, ":player_declines_honor", 1),
                            (else_try),
                              (gt, "$g_dont_give_marshalship_to_player_days", 1),
                              (assign, ":player_declines_honor", 1),
                            (try_end),
                            
							##diplomacy start+
							(faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),
							(call_script, "script_dplmc_is_affiliated_family_member", ":troop_no"),
							(assign, ":affiliated_with_player", reg0),

							(assign, ":subaltern_gender", -1),#The gender subject to sexism (as far as leadership is concerned).
							(try_begin),
								(lt, "$g_disable_condescending_comments", 2),#Prejudice not disabled
								(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),#Don't bother with the rest of the check
								(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),#if the lord has an unbiased outlook.
								(neg|troop_slot_ge, ":troop_no", slot_lord_reputation_type, lrep_roguish),
								(call_script, "script_dplmc_store_troop_is_female", ":troop_no"),
								(store_sub, ":subaltern_gender", 1, reg0),
								(try_begin),
									(call_script, "script_cf_dplmc_faction_has_bias_against_gender", ":troop_faction", ":subaltern_gender"),
								(else_try),
									(assign, ":subaltern_gender", -1),
								(try_end),
							(try_end),

							(assign, ":faction_lord_count", 0),#Keep track of the number of lords in the faction
							##diplomacy end+
                            
                            (assign, ":total_faction_renown", 0),
                            (troop_set_slot, "trp_player", slot_troop_temp_slot, 0),
							(try_begin),
								(eq, "$players_kingdom", ":troop_faction"),
								(eq, "$player_has_homage", 1),
								(troop_get_slot, ":total_faction_renown", "trp_player", slot_troop_renown),
								##diplomacy start+
								#Increment the faction lord count
								(val_add, ":faction_lord_count", 1),

								(try_begin),
									(lt, "$g_disable_condescending_comments", 0),#If the player has set the prejudice mode to "high"
									(eq, ":subaltern_gender", "$character_gender"),
									(val_mul, ":total_faction_renown", 4),
									(val_add, ":total_faction_renown", 3),
									(val_div, ":total_faction_renown", 5),
								(try_end),
								##diplomacy end+
							(try_end),

						##diplomacy start+
							(try_for_range, ":active_npc", heroes_begin, heroes_end),#Changed range to include kingdom ladies
								(troop_set_slot, ":active_npc", dplmc_slot_troop_temp_slot, 0), #this will hold distance to closest owned fief
						##diplomacy end+
								(troop_set_slot, ":active_npc", slot_troop_temp_slot, 0), #reset to zero

								(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
								(eq, ":active_npc_faction", ":troop_faction"),
								(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),

								(troop_get_slot, ":renown", ":active_npc", slot_troop_renown),
								##diplomacy start+
								#Increment the faction lord count
								(val_add, ":faction_lord_count", 1),

								(try_begin),#If the player has set the prejudice mode to "high".
									(lt, "$g_disable_condescending_comments", 0),#If the player has set the prejudice mode to "high"
									(call_script, "script_dplmc_store_troop_is_female", ":active_npc"),
									(eq, reg0, ":subaltern_gender"),
									(val_mul, ":renown", 4),
									(val_add, ":renown", 3),
									(val_div, ":renown", 5),
								(try_end),
								##diplomacy end+
								(val_add, ":total_faction_renown", ":renown"),
							(try_end),


							(assign, ":total_faction_center_value", 0),
							(try_for_range, ":center", centers_begin, centers_end),
								(store_faction_of_party, ":center_faction", ":center"),
								(eq, ":center_faction", ":troop_faction"),

								(assign, ":center_value", 1),
								(try_begin),
								##diplomacy start+
								#Use different scoring scheme
									(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
									(try_begin),
									   (party_slot_eq, ":center", slot_party_type, spt_town),
									   (assign, ":center_value", 3),
									(else_try),
									   (neg|party_slot_eq, ":center", slot_party_type, spt_village),
									   (this_or_next|party_slot_eq, ":center", slot_party_type, spt_castle),
										(is_between, ":center", walled_centers_begin, walled_centers_end),
									   (assign, ":center_value", 2),
									(try_end),
								#Otherwise fall through to old behavior
								(else_try),
								##diplomacy end+
									(is_between, ":center", towns_begin, towns_end),
									(assign, ":center_value", 2),
								(try_end),

								(val_add, ":total_faction_center_value", ":center_value"),

								(party_get_slot, ":town_lord", ":center", slot_town_lord),
								##diplomacy start+
								#The rest of the script assumes that non-player lords are heroes,
								#so add that condition here to get the count right.
								#(gt, ":town_lord", -1),
								(this_or_next|eq, ":town_lord", "trp_player"),
									(is_between, ":town_lord", heroes_begin, heroes_end),

								#Calculate distance for alternate scoring if the issue is a center
								(try_begin),
									(is_between, ":faction_issue", centers_begin, centers_end),
									(neq, ":center", ":faction_issue"),
									(troop_get_slot, ":dplmc_temp_slot", ":town_lord", dplmc_slot_troop_temp_slot),
									(store_distance_to_party_from_party, reg0, ":center", ":faction_issue"),
									(gt, reg0, 0),
									(try_begin),
										(eq, ":dplmc_temp_slot", 0),
										(assign, ":dplmc_temp_slot", reg0),
									(else_try),
										(val_min, ":dplmc_temp_slot", reg0),
									(try_end),
									(troop_set_slot, ":town_lord", dplmc_slot_troop_temp_slot, ":dplmc_temp_slot"),
								(try_end),
								##diplomacy end+

								(troop_get_slot, ":temp_slot", ":town_lord", slot_troop_temp_slot),
								(val_add, ":temp_slot", ":center_value"),
								(troop_set_slot, ":town_lord", slot_troop_temp_slot, ":temp_slot"),
							(try_end),
							(val_max, ":total_faction_center_value", 1),

							(store_div, ":average_renown_per_center_point", ":total_faction_renown", ":total_faction_center_value"),
							##diplomacy start+
							(val_max, ":faction_lord_count", 1),

						#	(store_mul, ":avg_renown_plus_500_per_cp", ":faction_lord_count", 500),
						#	(val_add, ":avg_renown_plus_500_per_cp", ":total_faction_renown"),
						#	(store_add, reg0, ":total_faction_center_value", ":faction_lord_count"),
						#	(val_div, ":avg_renown_plus_500_per_cp", reg0),

							#Get the standard deviation of renown per center point
							(assign, ":renown_per_center_point_variance", 0),
						#	(assign, ":renown_plus_500_per_center_point_variance", 0),

							(try_for_range, ":active_npc", active_npcs_including_player_begin, heroes_end),
								(store_sub, ":active_npc_faction", ":troop_faction", 1),#guaranteed not to equal
								(try_begin),
									#handle player
									(eq, ":active_npc", active_npcs_including_player_begin),
									(assign, ":active_npc", "trp_player"),
									(eq, "$players_kingdom", ":troop_faction"),
									(eq, "$player_has_homage", 1),
									(assign, ":active_npc_faction", ":troop_faction"),
								(else_try),
									#handle kingdom heroes
									(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
									(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
								(try_end),

								(eq, ":active_npc_faction", ":troop_faction"),

								(troop_get_slot, ":renown", ":active_npc", slot_troop_renown),
								(try_begin),
									(lt, "$g_disable_condescending_comments", 0),#If the player has set the prejudice mode to "high"
									(call_script, "script_dplmc_store_troop_is_female", ":active_npc"),
									(eq, reg0, ":subaltern_gender"),
									(val_mul, ":renown", 4),
									(val_add, ":renown", 3),
									(val_div, ":renown", 5),
								(try_end),
								(troop_get_slot, ":center_points", ":active_npc", slot_troop_temp_slot),
								#Variance for renown / center points
								(val_max, ":center_points", 1),
								(store_div, reg0, ":renown", ":center_points"),
								(val_sub, reg0, ":average_renown_per_center_point"),
								(val_mul, reg0, reg0),
								(val_add, ":renown_per_center_point_variance", reg0),

						#		#Variance for renown + 500 / center points + 1
						#		(troop_get_slot, ":center_points", ":active_npc", slot_troop_temp_slot),
						#		(val_add, ":center_points", 1),
						#		(store_add, reg0, ":renown", 500),
						#		(val_div, reg0, ":center_points"),
						#		(val_sub, reg0, ":avg_renown_plus_500_per_cp"),
						#		(val_mul, reg0, reg0),
						#		(val_add, ":renown_plus_500_per_center_point_variance", reg0),
							(try_end),

							#Get renown per center point standard deviation, or 10%, whichever is greater
							(store_div, reg0, ":faction_lord_count", 2),#for rounding
							(val_add, ":renown_per_center_point_variance", reg0),
							(val_div, ":renown_per_center_point_variance", 	":faction_lord_count"),

							(assign, reg0, ":renown_per_center_point_variance"),
							(convert_to_fixed_point, reg0),
							(store_sqrt, reg0, reg0),
							(convert_from_fixed_point, reg0),
							(assign, ":renown_per_center_point_standard_deviation", reg0),
							(val_add, reg0, 5),
							(val_div, reg0, 10),
							(val_max, ":renown_per_center_point_standard_deviation", reg0),
							(store_sub, ":renown_low_target", ":average_renown_per_center_point", ":renown_per_center_point_standard_deviation"),
							(val_max, ":renown_low_target", 0),

						#	#Get (renown + 500) per (center point plus one) standard deviation, or 10%, whichever is greater
						#	(store_div, reg0, ":faction_lord_count", 2),#for rounding
						#	(val_add, ":renown_plus_500_per_center_point_variance", reg0),
						#	(val_div, ":renown_plus_500_per_center_point_variance", ":faction_lord_count"),
						#
						#	(assign, reg0, ":renown_plus_500_per_center_point_variance"),
						#	(convert_to_fixed_point, reg0),
						#	(store_sqrt, reg0, reg0),
						#	(convert_from_fixed_point, reg0),
						#	(assign, ":renown_plus_500_per_center_point_standard_deviation", reg0),
						#	(val_add, reg0, 5),
						#	(val_div, reg0, 10),
						#	(val_max, ":renown_plus_500_per_center_point_standard_deviation", reg0),
						#	(store_sub, ":renown_500_low_target", ":avg_renown_plus_500_per_cp", ":renown_plus_500_per_center_point_standard_deviation"),
						#	(val_max, ":renown_500_low_target", 0),
							##diplomacy end+
                            
                            (try_begin),
                              (is_between, ":faction_issue", centers_begin, centers_end),
                              #NOTE -- The algorithms here might seem a bit repetitive, but are designed that way to create internal cliques among the lords in a faction.
                              
                              
                              
                              (try_begin),#If the center is a village, and a lord has no fief, choose him
                                (neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
                                (neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
                                (neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
                                
                                (is_between, ":faction_issue", villages_begin, villages_end),
                                (assign, ":favorite_lord_without_center", -1),
								(assign, ":score_to_beat", -1),
								##diplomacy start+
								(try_begin),
									#With changes enabled, widen the range of scores to check for certain personality types
									(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
									(try_begin),
										(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
										(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
										(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_benefactor),
										(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_conventional),
										(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_moralist),
										(this_or_next|is_between, ":troop_no", kings_begin, kings_end),
											(is_between, ":troop_no", pretenders_begin, pretenders_end),
										(assign, ":score_to_beat", -6),#-5 or better is indifferent
									(else_try),
										(ge, ":faction_leader", 0),
										(this_or_next|eq, ":faction_leader", ":troop_no"),
										(this_or_next|troop_slot_eq, ":faction_leader", slot_troop_spouse, ":troop_no"),
											(troop_slot_eq, ":troop_no", slot_troop_spouse, ":faction_leader"),
										(assign, ":score_to_beat", -6),#-5 or better is indifferent
									(try_end),
								(try_end),
								##diplomacy end+
                                
								(try_begin),
									(eq, "$players_kingdom", ":troop_faction"),
									(eq, "$player_has_homage", 1),
									(eq, ":player_declines_honor", 0),

									(troop_slot_eq, "trp_player", slot_troop_temp_slot, 0),
									(call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop_no"),
									(assign, ":relation", reg0),
									##diplomacy start+
									#If the player doesn't have prejudice disabled, don't automatically support for a first fief
									(try_begin),
										(this_or_next|neq, ":subaltern_gender", "$character_gender"),
										(this_or_next|is_between, ":troop_no", companions_begin, companions_end),#Former companions will support the player
										(this_or_next|troop_slot_eq, ":troop_no", slot_troop_spouse, "trp_player"),#Spouses will support the player
											(troop_slot_eq, "trp_player", slot_troop_spouse, ":troop_no"),
									(else_try),
										(val_sub, ":relation", 20),
									(try_end),
									##diplomacy end+

									(gt, ":relation", ":score_to_beat"),
									(neg|troop_slot_ge, "trp_player", slot_troop_controversy, 75),
									(assign, ":favorite_lord_without_center", "trp_player"),
									(assign, ":score_to_beat", ":relation"),
								(try_end),
								##diplomacy start+  Support promoted kingdom ladise
								#(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),  #<-- replace this
								(try_for_range, ":active_npc", heroes_begin, heroes_end),
								##diplomacy end+
									(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
									(eq, ":active_npc_faction", ":troop_faction"),
									(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),

									(troop_slot_eq, ":active_npc", slot_troop_temp_slot, 0),
									(try_begin),
										(eq, ":active_npc", ":troop_no"),
										(assign, ":relation", 50),
									(else_try),
										(call_script, "script_troop_get_relation_with_troop", ":active_npc", ":troop_no"),
										(assign, ":relation", reg0),
									(try_end),
									##diplomacy start+ Disadvantage the subaltern gender
									(call_script, "script_dplmc_store_troop_is_female", ":troop_no"),
									(try_begin),
										(eq, reg0, ":subaltern_gender"),
										(val_sub, ":relation", 20),
									(try_end),
									##diplomacy end+
									(neg|troop_slot_ge, ":active_npc", slot_troop_controversy, 75),

									(gt, ":relation", ":score_to_beat"),
									(assign, ":favorite_lord_without_center", ":active_npc"),
									(assign, ":score_to_beat", ":relation"),
								(try_end),

								(gt, ":favorite_lord_without_center", -1),
								(assign, ":result", ":favorite_lord_without_center"),
								(assign, ":result_explainer", "str_political_explanation_lord_lacks_center"),
							##diplomacy start+
							##Faction leaders are more rational about whom they support.
						   (else_try),
								(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
								(call_script, "script_dplmc_get_troop_standing_in_faction", ":troop_no", ":troop_faction"),
								(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
								(assign, ":best_candidate", -1),
								(assign, ":best_score", -1),
								(assign, ":explanation", 0),
								(try_begin),
								   (eq,"$players_kingdom", ":troop_faction"),
									(eq, "$player_has_homage", 1),
									(eq, ":player_declines_honor", 0),
									(call_script, "script_dplmc_calculate_troop_score_for_center_aux", ":troop_no", "trp_player", ":faction_issue"),#reg0 = score, reg1 = explanation
									(assign, ":best_candidate", "trp_player"),
									(assign, ":best_score", reg0),
									(assign, ":explanation", reg1),
								(try_end),
								(try_for_range, ":active_npc", heroes_begin, heroes_end),
								   (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
									(eq, ":active_npc_faction", ":troop_faction"),
									(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
									(call_script, "script_dplmc_calculate_troop_score_for_center_aux", ":troop_no", ":active_npc", ":faction_issue"),#reg0 = score, reg1 = explanation
									(this_or_next|eq, ":best_candidate", -1),
									   (gt, reg0, ":best_score"),
									(assign, ":best_candidate", ":active_npc"),
									(assign, ":best_score", reg0),
									(assign, ":explanation", reg1),
								(try_end),
								(gt, ":best_candidate", -1),
								(assign, ":result", ":best_candidate"),
								(assign, ":result_explainer", ":explanation"),
							##diplomacy end+
							(else_try),	#taken by troop
								(is_between, ":faction_issue", walled_centers_begin, walled_centers_end),
								(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
								(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
								(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),

								(party_get_slot, ":last_taken_by_troop", ":faction_issue", slot_center_last_taken_by_troop),
								(try_begin),
									(try_begin),
										(neq, ":troop_faction", "$players_kingdom"),
										(assign, ":last_taken_by_troop", -1),
									(else_try),
										(eq, "$player_has_homage", 0),
										(assign, ":last_taken_by_troop", -1),
									(else_try),
										(eq, ":faction_issue", "$g_castle_requested_by_player"),
										(assign, ":last_taken_by_troop", "trp_player"),
									(else_try),
										(eq, ":faction_issue", "$g_castle_requested_for_troop"),
										(assign, ":last_taken_by_troop", "trp_player"),
									(else_try), #ie, the fellow who took it is no longer in the faction
										(gt, ":last_taken_by_troop", -1),
										(store_faction_of_troop, ":last_take_by_troop_faction", ":last_taken_by_troop"),
										(neq, ":last_take_by_troop_faction", ":troop_faction"),
										(assign, ":last_taken_by_troop", -1),
									(try_end),
								(try_end),
								(gt, ":last_taken_by_troop", -1),

								(try_begin),
									(eq, "$cheat_mode", 1),
									(gt, ":last_taken_by_troop", -1),
									(str_store_troop_name, s3, ":last_taken_by_troop"),
									(display_message, "@{!}Castle taken by {s3}"),
								(try_end),


								(call_script, "script_troop_get_relation_with_troop", ":troop_no", ":last_taken_by_troop"),
								##diplomacy start+
								#If behavior changes are enabled, increase the accepted range for certain personality types.
								(assign, ":relation", reg0),
								(try_begin),
									(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
									(try_begin),
										(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
										(val_add, reg0, 5),#i.e. accept at -5 (indifferent) or higher
									(else_try),
										(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
										(val_add, reg0, 5),#i.e. accept at -5 (indifferent) or higher
									(try_end),
								(try_end),
								##diplomacy end+
								(ge, reg0, 0),

								(neg|troop_slot_ge, ":last_taken_by_troop", slot_troop_controversy, 25),

								(troop_get_slot, ":renown", ":last_taken_by_troop", slot_troop_renown),
								##diplomacy start+
								(try_begin),
									(lt, "$g_disable_condescending_comments", 0),#If the player has set the prejudice mode to "high"
									(call_script, "script_dplmc_store_troop_is_female", ":last_taken_by_troop"),
									(eq, reg0, ":subaltern_gender"),
									(val_mul, ":renown", 4),
									(val_add, ":renown", 3),
									(val_div, ":renown", 5),
								(try_end),
								##diplomacy end+
								(troop_get_slot, ":center_points", ":last_taken_by_troop", slot_troop_temp_slot),
								(val_max, ":center_points", 1),
								(store_div, ":renown_divided_by_center_points", ":renown", ":center_points"),
								(val_mul, ":renown_divided_by_center_points", 6), #was five
								(val_div, ":renown_divided_by_center_points", 4),

								##diplomacy start+
								(try_begin),
									(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
									#Possibly raise renown_divided_by_center_points
									(store_div, reg0, ":renown", ":center_points"),
									(val_add, reg0, ":renown_per_center_point_standard_deviation"),
									(val_max, ":renown_divided_by_center_points", reg0),
								(try_end),
								##diplomacy end+
								(ge, ":renown_divided_by_center_points", ":average_renown_per_center_point"),


								(assign, ":result", ":last_taken_by_troop"),
								(assign, ":result_explainer", "str_political_explanation_lord_took_center"),
                                
                                
                                #Check self, immediate family
                                #This is done instead of a single weighted score to create cliques -- groups of NPCs who support one another
                              (else_try),
                                (assign, ":most_deserving_close_friend", -1),
                                (assign, ":score_to_beat", ":average_renown_per_center_point"),
                                (val_div, ":score_to_beat", 3),
                                (val_mul, ":score_to_beat", 2),
                                
                                (try_begin),
                                  (eq, "$cheat_mode", 1),
                                  (assign, reg3, ":score_to_beat"),
                                  (display_message, "@{!}Two-thirds average_renown = {reg3}"),
                                (try_end),
								
								###diplomacy start+
								#(try_begin),
								#	(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
								#	(try_begin),
								#		(eq, "$cheat_mode", 1),
								#		(assign, reg3, ":renown_low_target"),
								#		(display_message, "@{!}Average renown per center minus one standard deviation = {reg3}"),
								#	(try_end),
								#(try_end),
								###diplomacy end+
                                
								(try_begin),
									(eq, "$players_kingdom", ":troop_faction"),
									(eq, "$player_has_homage", 1),
									(eq, ":player_declines_honor", 0),

									(call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop_no"),
									(assign, ":relation", reg0),
									##diplomacy start+
									#If affiliated with player
									(this_or_next|gt, ":affiliated_with_player", 0),
									##diplomacy end+
									(ge, ":relation", 20),
									(neg|troop_slot_ge, "trp_player", slot_troop_controversy, 50),

									(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
									##diplomacy start+
									(try_begin),
										(lt, "$g_disable_condescending_comments", 0),#If the player has set the prejudice mode to "high"
										(eq, ":subaltern_gender", "$character_gender"),
										(val_mul, ":renown", 4),
										(val_add, ":renown", 3),
										(val_div, ":renown", 5),
									(try_end),
									(troop_get_slot, ":center_points", "trp_player", slot_troop_temp_slot),
									(val_max, ":center_points", 1),
									(store_div, ":renown_divided_by_center_points", ":renown", ":center_points"),


									(assign, ":most_deserving_close_friend", "trp_player"),
									(assign, ":score_to_beat", ":renown_divided_by_center_points"),
								(try_end),
								##diplomacy start+  Support promoted kingdom ladies
								#(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end), #<- replace
								(try_for_range, ":active_npc", heroes_begin, heroes_end),
								##diplomacy end+
									(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
									(eq, ":active_npc_faction", ":troop_faction"),
									(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),

									(call_script, "script_troop_get_relation_with_troop", ":active_npc", ":troop_no"),
									(assign, ":relation", reg0),
									##diplomacy start+
									(assign, reg0, 0),
									#If affiliated with player
									(try_begin),
										(lt, ":relation", 20),
										(gt, ":affiliated_with_player", 0),
										(neq, ":active_npc", ":troop_no"),
										(call_script, "script_dplmc_is_affiliated_family_member", ":troop_no"),
									(try_end),
									(this_or_next|gt, reg0, 0),#<-- both affiliated
									##diplomacy end+
									(this_or_next|eq, ":active_npc", ":troop_no"),
										(ge, ":relation", 20),
									(neg|troop_slot_ge, ":active_npc", slot_troop_controversy, 50),

									(troop_get_slot, ":renown", ":active_npc", slot_troop_renown),
									##diplomacy start+
									(try_begin),
										(lt, "$g_disable_condescending_comments", 0),#If the player has set the prejudice mode to "high"
										(call_script, "script_dplmc_store_troop_is_female", ":active_npc"),
										(eq, reg0, ":subaltern_gender"),
										(val_mul, ":renown", 4),
										(val_add, ":renown", 3),
										(val_div, ":renown", 5),
									(try_end),
									##diplomacy end+
									(troop_get_slot, ":center_points", ":active_npc", slot_troop_temp_slot),
									(val_max, ":center_points", 1),
									(store_div, ":renown_divided_by_center_points", ":renown", ":center_points"),


									(try_begin),
										(eq, "$cheat_mode", 1),
										(str_store_troop_name, s10, ":active_npc"),
										(assign, reg3, ":renown_divided_by_center_points"),
										(display_message, "@{!}DEBUG -- Colleague test: score for {s10} = {reg3}"),
									(try_end),


									(gt, ":renown_divided_by_center_points", ":score_to_beat"),

									(assign, ":most_deserving_close_friend", ":active_npc"),
									(assign, ":score_to_beat", ":renown_divided_by_center_points"),
								(try_end),

								(gt, ":most_deserving_close_friend", -1),


								(assign, ":result", ":most_deserving_close_friend"),
								(assign, ":result_explainer", "str_political_explanation_most_deserving_friend"),
                                
                                
                                
                              (else_try),
                                #Most deserving in entire faction, minus those with no relation
                                (neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
                                (neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
                                (neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
                                
                                (assign, ":most_deserving_in_faction", -1),
                                (assign, ":score_to_beat", 0),
                                
                                (try_begin),
                                  (eq, "$players_kingdom", ":troop_faction"),
                                  (eq, "$player_has_homage", 1),
                                  (eq, ":player_declines_honor", 0),
                                  
									(call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop_no"),
									(assign, ":relation", reg0),
									(ge, ":relation", 0),
									(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
									##diplomacy start+
									(try_begin),
										(lt, "$g_disable_condescending_comments", 0),#If the player has set the prejudice mode to "high"
										(eq, ":subaltern_gender", "$character_gender"),
										(val_mul, ":renown", 4),
										(val_add, ":renown", 3),
										(val_div, ":renown", 5),
									(try_end),
									##diplomacy end+
									(troop_get_slot, ":center_points", "trp_player", slot_troop_temp_slot),
									(neg|troop_slot_ge, "trp_player", slot_troop_controversy, 25),

									(val_max, ":center_points", 1),
									(store_div, ":renown_divided_by_center_points", ":renown", ":center_points"),

									(assign, ":most_deserving_in_faction", "trp_player"),
									(assign, ":score_to_beat", ":renown_divided_by_center_points"),
								(try_end),
								##diplomacy start+ add support for promoted kingdom ladies
								#(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
								(try_for_range, ":active_npc", heroes_begin, heroes_end),
								   (this_or_next|is_between, ":active_npc", active_npcs_begin, active_npcs_end),
									  (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
								##diplomacy end+
									(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
									(eq, ":active_npc_faction", ":troop_faction"),
									(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),

									(call_script, "script_troop_get_relation_with_troop", ":active_npc", ":troop_no"),
									(assign, ":relation", reg0),
									(this_or_next|eq, ":active_npc", ":troop_no"),
										(ge, ":relation", 0),
									(neg|troop_slot_ge, ":active_npc", slot_troop_controversy, 25),

									(troop_get_slot, ":renown", ":active_npc", slot_troop_renown),
									##diplomacy start+
									(try_begin),
										(lt, "$g_disable_condescending_comments", 0),#If the player has set the prejudice mode to "high"
										(call_script, "script_dplmc_store_troop_is_female", ":active_npc"),
										(eq, reg0, ":subaltern_gender"),
										(val_mul, ":renown", 4),
										(val_add, ":renown", 3),
										(val_div, ":renown", 5),
									(try_end),
									##diplomacy end+
									(troop_get_slot, ":center_points", ":active_npc", slot_troop_temp_slot),
									(val_max, ":center_points", 1),

									(store_div, ":renown_divided_by_center_points", ":renown", ":center_points"),
									(gt, ":renown_divided_by_center_points", ":score_to_beat"),

									(try_begin),
										(eq, "$cheat_mode", 1),
										(str_store_string, s10, ":active_npc"),
										(assign, reg3, ":renown_divided_by_center_points"),
										(display_message, "@{!}DEBUG -- Open test: score for {s10} = {reg3}"),
									(try_end),


									(assign, ":most_deserving_in_faction", ":active_npc"),
									(assign, ":score_to_beat", ":renown_divided_by_center_points"),
								(try_end),


								(gt, ":most_deserving_in_faction", -1),
								(assign, ":result", ":most_deserving_in_faction"),
								(assign, ":result_explainer", "str_political_explanation_most_deserving_in_faction"),
							##diplomacy start+
							(else_try),
								#The lord wasn't able to find any suitable candidates,
								#so now we perform the evaluation from another perspective.
								(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
								#DPLMC_AI_CHANGES >= LOW
								#DPLMC_AI_CHANGES >= MEDIUM   XOR   status >= DPLMC_FACTION_STANDING_LEADER_SPOUSE
								(call_script, "script_dplmc_get_troop_standing_in_faction", ":troop_no", ":troop_faction"),
								(this_or_next|ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
									(ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
								(this_or_next|lt, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
									(lt, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
								(assign, ":save_reg1", reg1),

								(assign, ":score_to_beat", 0),
								(assign, ":most_deserving_in_faction", -1),
								#(assign, ":tmp_explanation", 0),

								(try_for_range, ":active_npc", active_npcs_including_player_begin, heroes_end),
									(store_sub, ":active_npc_faction", ":troop_faction", 1),
									(try_begin),
										(eq, ":active_npc", active_npcs_including_player_begin),
										(assign, ":active_npc", "trp_player"),
										(eq, "$players_kingdom", ":troop_faction"),
										(eq, "$player_has_homage", 1),
										(assign, ":active_npc_faction", ":troop_faction"),
									(else_try),
										(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
										(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
									(try_end),
									(eq, ":active_npc_faction", ":troop_faction"),

									#(call_script, "script_dplmc_aux_troop_evaluate_troop_for_center", ":troop_no", ":active_npc", ":faction_issue"),#reg0 = score, reg1 = explanation
									(call_script, "script_dplmc_calculate_troop_score_for_center_aux", ":troop_no", ":active_npc", ":faction_issue"),#reg0 = score, reg1 = explanation

									(this_or_next|eq, ":most_deserving_in_faction", -1),
										(ge, reg0, ":score_to_beat"),
									(assign, ":score_to_beat", reg0),
								(assign, ":result_explainer", reg1),
									(assign, ":most_deserving_in_faction", ":active_npc"),
								(try_end),

								(gt, ":most_deserving_in_faction", -1),
								(assign, ":result", ":most_deserving_in_faction"),
								#(assign, ":result_explainer", ":result_explainer"),#unneeded
							 (assign, reg1, ":save_reg1"),
							##diplomacy end+
							(else_try),
								(assign, ":result", ":troop_no"),
								(assign, ":result_explainer", "str_political_explanation_self"),
							(try_end),                              
                              
                            (else_try),
                              (eq, ":faction_issue", 1),
                              
                              (assign, ":relationship_threshhold", 15),
                              (try_begin),
                                (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
                                (assign, ":relationship_threshhold", 5),
                              (else_try),
                                (troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
                                (assign, ":relationship_threshhold", 25),
                              (try_end),
                              
                              #For marshals, score marshals according to renown divided by controversy - first for friends and family, then for everyone
                              (assign, ":marshal_candidate", -1),
                              (assign, ":score_to_beat", 0),
                              (try_begin),
                                (eq, "$players_kingdom", ":troop_faction"),
                                (eq, "$player_has_homage", 1),
                                (eq, "$g_player_is_captive", 0),
                                (eq, ":player_declines_honor", 0),
                                
                                
								(call_script, "script_troop_get_relation_with_troop", "trp_player", ":troop_no"),
								(ge, reg0, ":relationship_threshhold"),
								(assign, ":marshal_candidate", "trp_player"),
								(troop_get_slot, ":renown", "trp_player", slot_troop_renown),
								##diplomacy start+
								(try_begin),
									(lt, "$g_disable_condescending_comments", 0),#If the player has set the prejudice mode to "high"
									(eq, ":subaltern_gender", "$character_gender"),
									(val_mul, ":renown", 4),
									(val_add, ":renown", 3),
									(val_div, ":renown", 5),
								(try_end),
								##diplomacy end+
								(troop_get_slot, ":controversy_divisor", "trp_player", slot_troop_controversy),
								(val_add, ":controversy_divisor", 50),
								(store_div, ":score_to_beat", ":renown", ":controversy_divisor"),
							(try_end),

						  ##diplomacy start+ Support promoted ladies
							#(try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
							(try_for_range, ":active_npc", heroes_begin, heroes_end),
						  ##diplomacy end+
								(store_faction_of_troop, ":active_npc_faction", ":active_npc"),
								(eq, ":active_npc_faction", ":troop_faction"),
								(troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
								(troop_slot_eq, ":active_npc", slot_troop_prisoner_of_party, -1),

								(neg|faction_slot_eq, ":troop_faction", slot_faction_leader, ":active_npc"),

								(call_script, "script_troop_get_relation_with_troop", ":active_npc", ":troop_no"),
								(assign, ":relation", reg0),
								(this_or_next|eq, ":active_npc", ":troop_no"),
									(ge, ":relation", ":relationship_threshhold"),

								(troop_get_slot, ":renown", ":active_npc", slot_troop_renown),
								##diplomacy start+
								(try_begin),
									(lt, "$g_disable_condescending_comments", 0),#If the player has set the prejudice mode to "high"
									(call_script, "script_dplmc_store_troop_is_female", ":troop_no"),
									(eq, reg0, ":subaltern_gender"),
									(val_mul, ":renown", 4),
									(val_add, ":renown", 3),
									(val_div, ":renown", 5),
								(try_end),
								##diplomacy end+
								(troop_get_slot, ":controversy_divisor", ":active_npc", slot_troop_controversy),
								(val_add, ":controversy_divisor", 50),
								(store_div, ":score", ":renown", ":controversy_divisor"),

								(gt, ":score", ":score_to_beat"),

								(assign, ":marshal_candidate", ":active_npc"),
								(assign, ":score_to_beat", ":score"),

							(try_end),

							(assign, ":result", ":marshal_candidate"),
							(assign, ":result_explainer", "str_political_explanation_marshal"),
						(try_end),

						(try_begin),
							(eq, "$cheat_mode", 1),
							(gt, ":result", -1),
							(str_store_troop_name, s8, ":troop_no"),
							(str_store_troop_name, s9, ":result"),
							(str_store_string, s10, ":result_explainer"),
							(display_message, "@{!}DEBUG -- {s8} backs {s9}:{s10}"),
						(try_end),

						(assign, reg0, ":result"),
						(assign, reg1, ":result_explainer"),

						]),
                        
                        
                        ("npc_decision_checklist_evaluate_faction_strategy",
                          [
                            #Decides whether the strategy is good or bad -- to be added
                        ]),
                        
                        
                        ("process_player_enterprise",
						#reg0: Profit per cycle
						##diplomacy start+
						#Actual documentation of original parameters and outputs.
						# INPUTS:
						#   arg1: item_type
						#   arg2: center
						# OUTPUTS:
						#   reg0:  profit_per_cycle"),
						#   reg1:  final_price_for_total_produced_goods"),
						#   reg2:  final_price_for_total_inputs"),
						#   reg3:  price_of_labor"),
						#   reg4:  final_price_for_single_produced_good"),
						#   reg5:  final_price_for_single_input"),
						#	reg10: final_price_for_secondary_input"),
						#
						# Further, if experimental changes are enabled, modify the price.
						##diplomacy end+
                          [
                            (store_script_param, ":item_type", 1),
                            (store_script_param, ":center", 2),
                            
                            (item_get_slot, ":price_of_labor", ":item_type", slot_item_overhead_per_run),
                            
							  (item_get_slot, ":base_price", ":item_type", slot_item_base_price),
							  (store_sub, ":cur_good_price_slot", ":item_type", trade_goods_begin),
							  (val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
							  (party_get_slot, ":cur_price_modifier", ":center", ":cur_good_price_slot"),
							  ##diplomacy start+
							  (val_clamp, ":cur_price_modifier", minimum_price_factor, maximum_price_factor + 1),#Added enforcement of minimum/maximum
							  (store_mul, ":final_price_for_single_produced_good", ":base_price", ":cur_price_modifier"),#<- (Unchanged)
							  (val_div, ":final_price_for_single_produced_good", average_price_factor),#Replaced "1000" with "average_price_factor"
							  ##diplomacy end+
							  (item_get_slot, ":number_of_outputs_produced", ":item_type", slot_item_output_per_run),
							  (store_mul, ":final_price_for_total_produced_goods", ":number_of_outputs_produced", ":final_price_for_single_produced_good"),

							  (item_get_slot, ":primary_raw_material", ":item_type", slot_item_primary_raw_material),
							  (item_get_slot, ":base_price", ":primary_raw_material", slot_item_base_price),
							  (store_sub, ":cur_good_price_slot", ":primary_raw_material", trade_goods_begin),
							  (val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
							  (party_get_slot, ":cur_price_modifier", ":center", ":cur_good_price_slot"),
							  ##diplomacy start+
							  (try_begin),
								 (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),#<-- experimental changes must be enabled
								 (call_script, "script_dplmc_assess_ability_to_purchase_good_from_center", ":primary_raw_material", ":center"),
								 (val_max, ":cur_price_modifier", reg0),
							  (try_end),
							  (val_clamp, ":cur_price_modifier", minimum_price_factor, maximum_price_factor + 1),#Added enforcement of minimum/maximum
							  (store_mul, ":final_price_for_single_input", ":base_price", ":cur_price_modifier"),#<- (Unchanged)
							  (val_div, ":final_price_for_single_input", average_price_factor),#Replaced "1000" with "average_price_factor"
							  ##diplomacy end+
							  (item_get_slot, ":number_of_inputs_required", ":item_type", slot_item_input_number),
							  (try_begin),
								(lt, ":number_of_inputs_required", 0),
								(store_div, ":final_price_for_total_inputs", ":final_price_for_single_input", 2),
							  (else_try),
								(store_mul, ":final_price_for_total_inputs", ":final_price_for_single_input", ":number_of_inputs_required"),
							  (try_end),

							  (try_begin),
								(item_slot_ge, ":item_type", slot_item_secondary_raw_material, 1),
								(item_get_slot, ":secondary_raw_material", ":item_type", slot_item_secondary_raw_material),
								(item_get_slot, ":base_price", ":secondary_raw_material", slot_item_base_price),
								(store_sub, ":cur_good_price_slot", ":secondary_raw_material", trade_goods_begin),
								(val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
								(party_get_slot, ":cur_price_modifier", ":center", ":cur_good_price_slot"),
								##diplomacy start+
								(try_begin),
								  (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_MEDIUM),#<-- experimental changes must be enabled
								  (call_script, "script_dplmc_assess_ability_to_purchase_good_from_center", ":secondary_raw_material", ":center"),
								  (val_max, ":cur_price_modifier", reg0),
								(try_end),
								(val_clamp, ":cur_price_modifier", minimum_price_factor, maximum_price_factor + 1),#Added enforcement of minimum/maximum
								##diplomacy end+

								(try_begin),
								  (lt, ":number_of_inputs_required", 0),
								  (store_div, ":final_price_for_secondary_input", ":final_price_for_secondary_input", 2),
								(else_try),
								  (store_mul, ":final_price_for_secondary_input", ":final_price_for_secondary_input", ":number_of_inputs_required"),
								(try_end),

								(store_mul, ":final_price_for_secondary_input", ":base_price", ":cur_price_modifier"),
								##diplomacy start+
								(val_div, ":final_price_for_secondary_input", average_price_factor),#Replaced "1000" with "average_price_factor"
								##diplomacy end+
							  (else_try),
								(assign, ":final_price_for_secondary_input", 0),
							  (try_end),

							  (store_sub, ":profit_per_cycle", ":final_price_for_total_produced_goods", ":final_price_for_total_inputs"),
							  (val_sub, ":profit_per_cycle", ":price_of_labor"),
							  (val_sub, ":profit_per_cycle", ":final_price_for_secondary_input"),

							  (assign, reg0, ":profit_per_cycle"),
							  (assign, reg1, ":final_price_for_total_produced_goods"),
							  (assign, reg2, ":final_price_for_total_inputs"),
							  (assign, reg3, ":price_of_labor"),
							  (assign, reg4, ":final_price_for_single_produced_good"),
							  (assign, reg5, ":final_price_for_single_input"),
							  (assign, reg10, ":final_price_for_secondary_input"),
							]),
                        
                        # script_replace_scene_items_with_spawn_items_before_ms
                        # Input: none
                        # Output: none
                        ("replace_scene_items_with_spawn_items_before_ms",
                          [
                            (try_for_range, ":item_no", all_items_begin, all_items_end),
                              (scene_item_get_num_instances, ":num_instances", ":item_no"),
                              (item_set_slot, ":item_no", slot_item_num_positions, 0),
                              (assign, ":num_positions", 0),
                              (try_for_range, ":cur_instance", 0, ":num_instances"),
                                (scene_item_get_instance, ":scene_item", ":item_no", ":cur_instance"),
                                (prop_instance_get_position, "$g_position_to_use_for_replacing_scene_items", ":scene_item"),
                                (store_add, ":cur_slot", slot_item_positions_begin, ":num_positions"),
                                (item_set_slot, ":item_no", ":cur_slot", "$g_position_to_use_for_replacing_scene_items"),
                                (val_add, ":num_positions", 1),
                                (val_add, "$g_position_to_use_for_replacing_scene_items", 1),
                                (item_set_slot, ":item_no", slot_item_num_positions, ":num_positions"),
                              (try_end),
                              (replace_scene_items_with_scene_props, ":item_no", "spr_empty"),
                            (try_end),
                        ]),
                        
                        # script_replace_scene_items_with_spawn_items_after_ms
                        # Input: none
                        # Output: none
                        ("replace_scene_items_with_spawn_items_after_ms",
                          [
                            (try_for_range, ":item_no", all_items_begin, all_items_end),
                              (item_get_slot,  ":num_positions", ":item_no", slot_item_num_positions),
                              (try_for_range, ":cur_position", 0, ":num_positions"),
                                (store_add, ":cur_slot", slot_item_positions_begin, ":cur_position"),
                                (item_get_slot, ":pos_no", ":item_no", ":cur_slot"),
                                (set_spawn_position, ":pos_no"),
                                (spawn_item, ":item_no", 0),
                              (try_end),
                            (try_end),
                        ]),
                        
                        # script_cf_is_melee_weapon_for_tutorial
                        # Input: arg1 = item_no
                        # Output: none (can fail)
                        ("cf_is_melee_weapon_for_tutorial",
                          [
                            (store_script_param, ":item_no", 1),
                            (assign, ":result", 0),
                            (try_begin),
                              (this_or_next|eq, ":item_no", "itm_we_sar_spear_staff_quarter"),
                              (eq, ":item_no", "itm_practice_sword"),
                              (assign, ":result", 1),
                            (try_end),
                            (eq, ":result", 1),
                        ]),
                        
                        # script_iterate_pointer_arrow
                        # Input: none
                        # Output: none
                        ("iterate_pointer_arrow",
                          [
                            (store_mission_timer_a_msec, ":cur_time"),
                            (try_begin),
                              (assign, ":up_down", ":cur_time"),
                              (assign, ":turn_around", ":cur_time"),
                              (val_mod, ":up_down", 1080),
                              (val_div, ":up_down", 3),
                              (scene_prop_get_instance, ":prop_instance", "spr_pointer_arrow", 0),
                              (prop_instance_get_position, pos0, ":prop_instance"),
                              (position_set_z_to_ground_level, pos0),
                              (position_move_z, pos0, "$g_pointer_arrow_height_adder", 1),
                              (set_fixed_point_multiplier, 100),
                              (val_mul, ":up_down", 100),
                              (store_sin, ":up_down_sin", ":up_down"),
                              (position_move_z, pos0, ":up_down_sin", 1),
                              (position_move_z, pos0, 100, 1),
                              (val_mod, ":turn_around", 2880),
                              (val_div, ":turn_around", 8),
                              (init_position, pos1),
                              (position_rotate_z, pos1, ":turn_around"),
                              (position_copy_rotation, pos0, pos1),
                              (prop_instance_set_position, ":prop_instance", pos0),
                            (try_end),
                        ]),
                        
                        ("find_center_to_attack_alt",
                          [
                            (store_script_param, ":troop_no", 1),
                            (store_script_param, ":attack_by_faction", 2),
                            (store_script_param, ":all_vassals_included", 3),
                            
                            (assign, ":result", -1),
                            (assign, ":score_to_beat", 0),
                            
                            (try_for_range, ":center_no", centers_begin, centers_end),
                              (call_script, "script_npc_decision_checklist_evaluate_enemy_center_for_attack",	":troop_no", ":center_no", ":attack_by_faction", ":all_vassals_included"),
                              (assign, ":score", reg0),
                              
                              (gt, ":score", ":score_to_beat"),
                              
                              (assign, ":result", ":center_no"),
                              (assign, ":score_to_beat", ":score"),
                            (try_end),
                            
                            (assign, reg0, ":result"),
                            (assign, reg1, ":score_to_beat"),
                        ]),
                        
                        ("npc_decision_checklist_evaluate_enemy_center_for_attack",
                          [
                            #NOTES -- LAST OFFENSIVE TIME SCORE IS NOT USED
                            
                            (store_script_param, ":troop_no", 1),
                            (store_script_param, ":potential_target", 2),
                            (store_script_param, ":attack_by_faction", 3),
                            (store_script_param, ":all_vassals_included", 4),
                            
                            (assign, ":result", -1),
                            (assign, ":explainer_string", -1),
                            #(assign, ":reason_is_obvious", 0),
                            (assign, ":power_ratio", 0),
                            #(assign, ":hours_since_last_recce", -1),
                            
                            #(assign, ":value_of_target", 0),
                            #(assign, ":difficulty_of_capture", 0),
                            (store_faction_of_troop, ":faction_no", ":troop_no"),
                            
                            (try_begin),
                              (eq, ":attack_by_faction", 1),
                              (faction_get_slot, ":faction_marshal", ":faction_no", slot_faction_marshall),
                              (ge, ":faction_marshal", 0), #STEVE ADDITION TO AVOID MESSAGE SPAM
                              (troop_get_slot, ":party_no", ":faction_marshal", slot_troop_leaded_party),
                            (else_try),
                              (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
                            (try_end),
                            
							  (assign, "$g_use_current_ai_object_as_s8", 0),
							  ##diplomacy start+ Use this if AI changes are enabled.
							  (party_get_slot, ":hours_since_capture", ":potential_target", dplmc_slot_center_last_transfer_time),
							  (try_begin),
								 #If the slot was uninitialized, set it to negative to indicate invalid.
								 (eq, ":hours_since_capture", 0),
								 (assign, ":hours_since_capture", -1),
							  (else_try),
								 (store_current_hours, reg0),
								 (val_sub, ":hours_since_capture", reg0),
							  (try_end),
							  #How recent counts as "recent" depends on the AI settings.
							  (try_begin),
								 (ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_HIGH),
								 (assign, ":recency_maximum", 24 * 21),#The last three weeks
							  (else_try),
								 (ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_MEDIUM),
								 (assign, ":recency_maximum", 24 * 14),#The last two weeks
							  (else_try),
								 (ge, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
								 (assign, ":recency_maximum", 24 * 7),#The last week
							  (else_try),
								 (assign, ":recency_maximum", 0),
							  (try_end),
							  ##diplomacy end+
                            
                            #THE FIRST BATCH OF DISQUALIFYING CONDITIONS DO NOT REQUIRE THE ATTACKING PARTY TO HAVE CURRENT INTELLIGENCE ON THE TARGET
                            (try_begin),
                              (neg|party_is_active, ":party_no"),
                              
                              (assign, ":result", -1),
                              (assign, ":explainer_string", "str_center_party_not_active"),
                              #(assign, ":reason_is_obvious", 1),
                            (else_try),
                              (store_faction_of_party, ":potential_target_faction", ":potential_target"),
                              (store_relation, ":relation", ":potential_target_faction", ":faction_no"),
                              (ge, ":relation", 0),
                              
                              (assign, ":result", -1),
                              (assign, ":explainer_string", "str_center_is_friendly"),
                              #(assign, ":reason_is_obvious", 1),
                            (else_try),
                              (is_between, ":potential_target", walled_centers_begin, walled_centers_end),
                              (assign, ":faction_of_besieger_party", -1),
                              (try_begin),
                                (neg|party_slot_eq, ":potential_target", slot_center_is_besieged_by, -1),
                                (party_get_slot, ":besieger_party", ":potential_target", slot_center_is_besieged_by),
                                (party_is_active, ":besieger_party"),
                                (store_faction_of_party, ":faction_of_besieger_party", ":besieger_party"),
                              (try_end),
                              
                              (neq, ":faction_of_besieger_party", -1),
                              (neq, ":faction_of_besieger_party", ":faction_no"),
                              
                              (assign, ":result", -1),
                              (assign, ":explainer_string", "str_center_is_already_besieged"),
                              #(assign, ":reason_is_obvious", 1),
                            (else_try),
                              (is_between, ":potential_target", villages_begin, villages_end),
                              (assign, ":village_is_looted_or_raided_already", 0),
                              (try_begin),
                                (party_slot_eq, ":potential_target", slot_village_state, svs_being_raided),
                                (party_get_slot, ":raider_party", ":potential_target", slot_village_raided_by),
                                (party_is_active, ":raider_party"),
                                (store_faction_of_party, ":raider_faction", ":raider_party"),
                                (neq, ":raider_faction", ":faction_no"),
                                (assign, ":raiding_by_one_other_faction", 1),
                              (else_try),
                                (assign, ":raiding_by_one_other_faction", 0),
                              (try_end),
                              
                              (try_begin),
                                (this_or_next|party_slot_eq, ":potential_target", slot_village_state, svs_looted),
                                (eq, ":raiding_by_one_other_faction", 1),
                                (assign, ":village_is_looted_or_raided_already", 1),
                              (try_end),
                              
                              (eq, ":village_is_looted_or_raided_already", 1),
                              
								(assign, ":result", -1),
								(assign, ":explainer_string", "str_center_is_looted_or_raided_already"),
								#(assign, ":reason_is_obvious", 1),
							  (else_try),
								##diplomacy start+ Add support for companion / lady personality types: does not want to attack innocents
								(call_script, "script_dplmc_get_troop_morality_value", ":troop_no", tmt_humanitarian),
								(this_or_next|gt, reg0, 0),
								(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_benefactor),
								(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_moralist),
								#diplomacy end+
								(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
								(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),

								(is_between, ":potential_target", villages_begin, villages_end),
								(assign, ":result", -1),
								(assign, ":explainer_string", "str_center_marshal_does_not_want_to_attack_innocents"),
							  (else_try),
								(assign, ":distance_from_our_closest_walled_center", 1000),
								(try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
								   (store_faction_of_party, ":cur_center_faction", ":cur_center"),
								   (eq, ":cur_center_faction", ":faction_no"),
								   (store_distance_to_party_from_party, ":distance_from_cur_center", ":cur_center", ":potential_target"),
								   (lt, ":distance_from_cur_center", ":distance_from_our_closest_walled_center"),
								   (assign, ":distance_from_our_closest_walled_center", ":distance_from_cur_center"),
								(try_end),

								(gt, ":distance_from_our_closest_walled_center", 75),
								##diplomacy start+ Add support for companion / lady personality types: cautious
								##OLD:
								#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
								#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
								#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
								#(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
								##NEW:
								(call_script, "script_dplmc_store_troop_personality_caution_level", ":troop_no"),
								(gt, reg0, 0),
								##Do not apply the check to recently-lost centers if AI changes are on.
								(this_or_next|lt, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
								(this_or_next|neg|party_slot_eq,":potential_target", slot_center_ex_faction, ":faction_no"),
								(this_or_next|lt, ":hours_since_capture", 0), #i.e. invalid
								(ge, ":hours_since_capture", ":recency_maximum"),#hasn't been taken recently
								##diplomacy end+

                              
                              (assign, ":result", -1),
                              (assign, ":explainer_string", "str_center_far_away_our_cautious_marshal_does_not_wish_to_reconnoiter"),
                              #RECONNOITERING BEGINS HERE - VALUE WILL BE TEN OR LESS
                            (else_try),
								(gt, ":distance_from_our_closest_walled_center", 90),
								##diplomacy start+ Do not apply the check to recently-lost centers if AI changes are on.
								(this_or_next|lt, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
								(this_or_next|neg|party_slot_eq,":potential_target", slot_center_ex_faction, ":faction_no"),
								(this_or_next|lt, ":hours_since_capture", 0), #i.e. invalid
								(ge, ":hours_since_capture", ":recency_maximum"),#hasn't been taken recently
								##diplomacy end+

								(assign, ":result", -1),
								(assign, ":explainer_string", "str_center_far_away_even_for_our_aggressive_marshal_to_reconnoiter"),
								#(assign, ":reason_is_obvious", 1),
							  (else_try),
								(is_between, ":potential_target", walled_centers_begin, walled_centers_end),
								##diplomacy start+ Add support for companion / lady personality types: aggessive
								##OLD:
								#(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
								#(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
								#(neg|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
								##NEW:
								(call_script, "script_dplmc_store_troop_personality_caution_level", ":troop_no"),
								(lt, reg0, 0),
								##Do not apply the check to recently-lost centers if AI changes are on.
								(this_or_next|lt, "$g_dplmc_ai_changes", DPLMC_AI_CHANGES_LOW),
								(this_or_next|neg|party_slot_eq,":potential_target", slot_center_ex_faction, ":faction_no"),
								(this_or_next|lt, ":hours_since_capture", 0), #i.e. invalid
								(ge, ":hours_since_capture", ":recency_maximum"),#hasn't been taken recently
								##diplomacy end+
                              
                              (assign, ":close_center_found", 0),
                              (try_for_range, ":friendly_walled_center", walled_centers_begin, walled_centers_end),
                                (eq, ":close_center_found", 0),
                                (store_faction_of_party, ":friendly_walled_center_faction", ":friendly_walled_center"),
                                (eq, ":friendly_walled_center_faction", ":faction_no"),
                                (store_distance_to_party_from_party, ":distance_from_walled_center", ":potential_target", ":friendly_walled_center"),
                                (lt, ":distance_from_walled_center", 60),
                                (assign, ":close_center_found", 1),
                              (try_end),
                              (eq, ":close_center_found", 0),
                              
                              (assign, ":result", -1),
                              (assign, ":explainer_string", "str_center_is_indefensible"),
                              #(else_try),
                              #For now it is removed as Armagan's decision, we can add this option in later patchs. I and Armagan accept it has good potential. But this system needs also
                              #scouting quests and scouting AI added together. If we only add this then we limit AI very much, it can attack only very few of centers, this damages
                              #variability of game and surprise attacks of AI. Player can predict where AI will attack and he can full garnisons of only this center.
                              #We can add asking travellers about how good defended center X by paying 100 denars for example to equalize situations of AI and human player.
                              #But these needs much work and detailed AI tests so Armagan decided to skip this for now.
                              
                              #(store_sub, ":faction_recce_slot", ":faction_no", kingdoms_begin),
                              #(val_add, ":faction_recce_slot", slot_center_last_reconnoitered_by_faction_time),
                              #(party_get_slot, ":last_recce_time", ":potential_target", ":faction_recce_slot"),
                              #(store_current_hours, ":hours_since_last_recce"),
                              #(val_sub, ":hours_since_last_recce", ":last_recce_time"),
                              
                              #(this_or_next|eq, ":last_recce_time", 0),
                              #(gt, ":hours_since_last_recce", 96), #Information is presumed to be accurate for four days
                              
                              #(store_sub, ":150_minus_distance_div_by_10", 150, ":distance_from_party"),
                              #(val_div, ":150_minus_distance_div_by_10", 10),
                              
                              #(assign, ":result", ":150_minus_distance_div_by_10"),
                              #(assign, ":explainer_string", "str_center_has_not_been_scouted"),
                              #DECISIONS BASED ON ENEMY STRENGTH BEGIN HERE
                            (else_try),
                              (party_get_slot, ":party_strength", ":party_no", slot_party_cached_strength),
                              (party_get_slot, ":follower_strength", ":party_no", slot_party_follower_strength),
                              (party_get_slot, ":strength_of_nearby_friend", ":party_no", slot_party_nearby_friend_strength),
                              
                              (store_add, ":total_strength", ":party_strength", ":follower_strength"),
                              (val_add, ":total_strength", ":strength_of_nearby_friend"),
                              
								#(party_get_slot, ":potential_target_nearby_enemy_exact_strength", ":potential_target", slot_party_nearby_friend_strength),
								#(assign, ":potential_target_nearby_enemy_strength", ":potential_target_nearby_enemy_exact_strength"),
								(try_begin),
								  (is_between, ":potential_target", villages_begin, villages_end),
								  (assign, ":enemy_strength", 10),
								(else_try),
								  (party_get_slot, ":enemy_strength", ":potential_target", slot_party_cached_strength),
								  (party_get_slot, ":enemy_strength_nearby", ":potential_target", slot_party_nearby_friend_strength),
								  (val_add, ":enemy_strength", ":enemy_strength_nearby"),
								(try_end),
								(val_max, ":enemy_strength", 1),
								##diplomacy start+  Add support for lady/companion personalities: aggressive
								##OLD:
								#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_martial),
								#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_quarrelsome),
								#(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_selfrighteous),
								##NEW:
								(call_script, "script_dplmc_store_troop_personality_caution_level", ":troop_no"),
								(lt, reg0, 0),
								###xxx yyy zzz TODO: The logic here seems backwards!
								###Later look at this and verify that it's what we want.
								##diplomacy end+

								(store_mul, ":power_ratio", ":total_strength", 100),
								(val_div, ":power_ratio", ":enemy_strength"),
								(lt, ":power_ratio", 150),

								(assign, ":result", -1),
								(assign, ":explainer_string", "str_center_protected_by_enemy_army_aggressive"),
							  (else_try),
								(ge, ":enemy_strength", ":total_strength"), #if enemy is powerful

								(assign, ":result", -1),
								(assign, ":explainer_string", "str_center_protected_by_enemy_army_cautious"),
							  (else_try),
								(store_mul, ":power_ratio", ":total_strength", 100),
								(val_div, ":power_ratio", ":enemy_strength"),
								(lt, ":power_ratio", 185),
								##diplomacy start+ Add support for companion/lady personalities: cautious
								##OLD:
								#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
								#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
								#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
								#(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
								##NEW:
								(call_script, "script_dplmc_store_troop_personality_caution_level", ":troop_no"),
								(gt, reg0, 0),
								##diplomacy end+
                              
                              #equations here
                              (assign, ":result", -1),
                              (assign, ":explainer_string", "str_center_cautious_marshal_believes_center_too_difficult_to_capture"),
                            (else_try),
                              (lt, ":power_ratio", 140), #it was 140
                              
                              (assign, ":result", -1),
                              (assign, ":explainer_string", "str_center_even_aggressive_marshal_believes_center_too_difficult_to_capture"),
                              #To Steve - I moved below two if statement here from upper places, to enable in answering different different answers even
                              #if we are close to an unlooted enemy village. For example now it can say "center X" is too far too while our army is
                              #looting a village because of its closeness.
                            (else_try),
                              #if the party has already started the siege
                              (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_raiding_village),
                              (faction_get_slot, ":current_object", ":faction_no", slot_faction_ai_object),
                              (is_between, ":current_object", villages_begin, villages_end),
                              (neq, ":potential_target", ":current_object"),
                              (party_slot_eq, ":current_object", slot_village_state, svs_under_siege),
                              
                              (store_current_hours, ":hours_since_siege_began"),
                              (party_get_slot, ":hour_that_siege_began", ":current_object", slot_center_siege_begin_hours),
                              (val_sub, ":hours_since_siege_began", ":hour_that_siege_began"),
                              (gt, ":hours_since_siege_began", 4),
                              
                              (call_script, "script_npc_decision_checklist_evaluate_enemy_center_for_attack", ":troop_no", ":current_object", ":attack_by_faction", 0),
                              (gt, reg0, -1),
                              
                              (assign, ":result", -1),
                              (assign, ":explainer_string", "str_center_we_have_already_committed_too_much_time_to_our_present_siege_to_move_elsewhere"),
                            (else_try),
                              #If the party is close to an unlooted village
                              (faction_slot_eq, ":faction_no", slot_faction_ai_state, sfai_raiding_village),
                              (faction_get_slot, ":current_object", ":faction_no", slot_faction_ai_object),
                              (neq, ":potential_target", ":current_object"),
                              (is_between, ":current_object", villages_begin, villages_end),
                              (store_distance_to_party_from_party, ":distance_to_cur_object", ":party_no", ":current_object"),
                              (lt, ":distance_to_cur_object", 10),
                              
                              (call_script, "script_npc_decision_checklist_evaluate_enemy_center_for_attack", ":troop_no", ":current_object", ":attack_by_faction", 0),
                              (gt, reg0, -1),
                              
                              (assign, "$g_use_current_ai_object_as_s8", 1),
                              
                              (assign, ":result", -1),
                              (assign, ":explainer_string", "str_center_we_are_already_here_we_should_at_least_loot_the_village"),
                              #DECISION TO ATTACK IS HERE
                              #(else_try),
                              #To Steve - I removed below lines, as here decided. We will use pre-function to evaluate assailability scores for centers rather than below lines to make AI
                              #selecting better targets. If you want to make some marshals to select not-best options I can add that option into script_calculate_center_assailability_score,
                              #for that we can need seed values for each center and for each lord, so we can add these seed values to create variability, clever marshals have seeds with less
                              #standard deviation and less values and less-clever marshals have bigger seeds. Then probability of some lords to disagree marshal increases because their seed
                              #values will be different from marshal's. If Steve wants it from me to implement I can add this.
                              
                              #(try_begin),
                              #  (is_between, ":potential_target", villages_begin, villages_end),
                              #  (party_get_slot, ":score", ":potential_target", slot_town_prosperity),
                              #  (val_add, ":score", 50), #average 100
                              #(else_try),
                              #  (is_between, ":potential_target", castles_begin, castles_end),
                              #  (assign, ":score", ":power_ratio"), #ie, at least 140
                              #(else_try),
                              #  (party_get_slot, ":score", ":potential_target", slot_town_prosperity),
                              #  (val_add, ":score", 75),
                              #  (val_mul, ":score", ":power_ratio"),
                              #  (val_div, ":score", 100), #ie, at least about 200
                              #(try_end),
                              #
                              #(val_sub, ":score", ":distance_from_party"),
                              #(lt, ":score", -1),
                              
                              #(assign, ":result", -1),
                              #(assign, ":explainer_string", "str_center_value_outweighed_by_difficulty_of_capture"),
                            (else_try),
                              (try_begin),
                                (eq, "$cheat_mode", 1),
                                (eq, ":faction_no", "fac_kingdom_3"),
                                (store_faction_of_party, ":potential_target_faction", ":potential_target"),
                                (store_relation, ":relation", ":potential_target_faction", ":faction_no"),
                                (lt, ":relation", 0),
                              (try_end),
                              
                              (call_script, "script_calculate_center_assailability_score", ":troop_no", ":potential_target", ":all_vassals_included"),
                              (assign, ":score", reg0),
                              (assign, ":power_ratio", reg1),
                              #(assign, ":distance_score", reg2),
                              
                              (assign, ":result", ":score"),
                              
								(try_begin),
								  (le, ":power_ratio", 100),
								  (try_begin),
									##diplomacy start+ Add support for companion / lady personalities: cautious
									##OLD:
									#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
									#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
									#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
									#(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
									##NEW:
									(call_script, "script_dplmc_store_troop_personality_caution_level", ":troop_no"),
									(gt, reg0, 0),
									##diplomacy end+
									(assign, ":explainer_string", "str_center_cautious_marshal_believes_center_too_difficult_to_capture"),
								  (else_try),
									(assign, ":explainer_string", "str_center_even_aggressive_marshal_believes_center_too_difficult_to_capture"),
								  (try_end),
								(else_try),
								  (le, ":power_ratio", 150),

								  (try_begin),
									##diplomacy start+ Add support for companion / lady personalities: cautious
									##OLD
									#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_upstanding),
									#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_debauched),
									#(this_or_next|troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_goodnatured),
									#(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_cunning),
									##NEW:
									(call_script, "script_dplmc_store_troop_personality_caution_level", ":troop_no"),
									(lt, reg0, 0),
									##diplomacy end+
									(assign, ":explainer_string", "str_center_protected_by_enemy_army_cautious"),
								  (else_try),
									(assign, ":explainer_string", "str_center_protected_by_enemy_army_aggressive"),
								  (try_end),
								(else_try),
								  (try_begin),
									(le, ":score", "$g_faction_object_score"),
									(assign, ":explainer_string", "str_center_value_outweighed_by_difficulty_of_capture"),
								  (else_try),
									#To Steve, does not this sentence needs to explain why we are not attacking that city?
									#This sentence says it justifies, so why we are not attacking?
									(assign, ":explainer_string", "str_center_value_justifies_the_difficulty_of_capture"),
								  (try_end),
								(try_end),
							  (try_end),

							  (assign, reg0, ":result"),
							  (assign, reg1, ":explainer_string"),
							  (assign, reg2, ":power_ratio"),
							 ]),
]
