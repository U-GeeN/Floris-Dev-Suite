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

scripts_part1 = [

  
  #script_game_start:
  # This script is called when a new game is started
  # INPUT: none
  ("game_start",
    [
####Floris MTT (Multiple Troop Trees): Here are the slots for all the troops that have multiple tree iterations.
	(assign, "$troop_trees", troop_trees_2), #Default on Expanded
	(call_script, "script_mtt_troop_slots"),
###

      #LAZERAS MODIFIED  {Top Tier Troops Recruit}
#	   #Floris: I used the tier 6 troops that don't upgrade to tier 7.
		  		## Floris: Multiple troop trees
		  		# Native
      (troop_set_slot,"trp_swadian_n_hero1", slot_troop_occupation, "trp_swadian_n_jock"),
      (troop_set_slot,"trp_swadian_n_hero2", slot_troop_occupation, "trp_swadian_n_selfbow_archer"),
      (troop_set_slot,"trp_vaegir_n_hero1", slot_troop_occupation, "trp_vaegir_n_pansirniy_kazan"),
      (troop_set_slot,"trp_vaegir_n_hero2", slot_troop_occupation, "trp_vaegir_n_druzhinnik_veteran"),
      (troop_set_slot,"trp_khergit_n_hero1", slot_troop_occupation, "trp_khergit_n_borjigin"),
      (troop_set_slot,"trp_nord_n_hero1", slot_troop_occupation, "trp_nord_n_husbondi"),
      (troop_set_slot,"trp_rhodok_n_hero1", slot_troop_occupation, "trp_rhodok_n_fante"),
      (troop_set_slot,"trp_rhodok_n_hero2", slot_troop_occupation, "trp_rhodok_n_balestriere"),
      (troop_set_slot,"trp_sarranid_n_hero1", slot_troop_occupation, "trp_sarranid_n_kapikula"),
      (troop_set_slot,"trp_sarranid_n_hero2", slot_troop_occupation, "trp_sarranid_n_uluteci"),
		  		# Reworked
      (troop_set_slot,"trp_swadian_r_hero1", slot_troop_occupation, "trp_swadian_r_jock"),
      (troop_set_slot,"trp_swadian_r_hero2", slot_troop_occupation, "trp_swadian_r_selfbow_archer"),
      (troop_set_slot,"trp_vaegir_r_hero1", slot_troop_occupation, "trp_vaegir_r_ataman"),
      (troop_set_slot,"trp_vaegir_r_hero2", slot_troop_occupation, "trp_vaegir_r_druzhinnik_veteran"),
      (troop_set_slot,"trp_khergit_r_hero1", slot_troop_occupation, "trp_khergit_r_khevtuul"),
      (troop_set_slot,"trp_khergit_r_hero2", slot_troop_occupation, "trp_khergit_r_borjigin"),
      (troop_set_slot,"trp_nord_r_hero1", slot_troop_occupation, "trp_nord_r_heahgerefa"),
      (troop_set_slot,"trp_nord_r_hero2", slot_troop_occupation, "trp_nord_r_kappi"),
#      (troop_set_slot,"trp_rhodok_r_hero1", slot_troop_occupation, "trp_rhodok_r_balestriere_d_assedio"),
      (troop_set_slot,"trp_rhodok_r_hero2", slot_troop_occupation, "trp_rhodok_r_picchiere_veterano"),
      (troop_set_slot,"trp_sarranid_r_hero1", slot_troop_occupation, "trp_sarranid_r_kapikula"),
      (troop_set_slot,"trp_sarranid_r_hero2", slot_troop_occupation, "trp_sarranid_r_uluteci"),
		  		# Expanded
      (troop_set_slot,"trp_swadian_e_hero1", slot_troop_occupation, "trp_swadian_e_highlander"),
      (troop_set_slot,"trp_swadian_e_hero2", slot_troop_occupation, "trp_swadian_e_lancer"),
      (troop_set_slot,"trp_vaegir_e_hero1", slot_troop_occupation, "trp_vaegir_e_legkoy_vityas"),
      (troop_set_slot,"trp_vaegir_e_hero2", slot_troop_occupation, "trp_vaegir_e_voevoda"),
      (troop_set_slot,"trp_vaegir_e_hero3", slot_troop_occupation, "trp_vaegir_e_elitniy_druzhinnik"),
      (troop_set_slot,"trp_khergit_e_hero1", slot_troop_occupation, "trp_khergit_e_keshig"),
      (troop_set_slot,"trp_khergit_e_hero2", slot_troop_occupation, "trp_khergit_e_kharvaach"),
      (troop_set_slot,"trp_khergit_e_hero3", slot_troop_occupation, "trp_khergit_e_jurtchi"),
      (troop_set_slot,"trp_nord_e_hero1", slot_troop_occupation, "trp_nord_e_skutilsveinr"),
      (troop_set_slot,"trp_nord_e_hero2", slot_troop_occupation, "trp_nord_e_hetja"),
      (troop_set_slot,"trp_nord_e_hero3", slot_troop_occupation, "trp_nord_e_hetja"),
#      (troop_set_slot,"trp_rhodok_e_hero1", slot_troop_occupation, "trp_rhodok_e_balestriere_d_assedio"),
      (troop_set_slot,"trp_rhodok_e_hero2", slot_troop_occupation, "trp_rhodok_e_capitano_di_ventura"),
      (troop_set_slot,"trp_rhodok_e_hero3", slot_troop_occupation, "trp_rhodok_e_guardia_ducale"),
      (troop_set_slot,"trp_sarranid_e_hero1", slot_troop_occupation, "trp_sarranid_e_qilich_arslan"),
      (troop_set_slot,"trp_sarranid_e_hero2", slot_troop_occupation, "trp_sarranid_e_sekban"),
		  		##
      (troop_set_slot,"trp_sarranid_e_hero3", slot_troop_occupation, "trp_sarranid_e_silahtar"),
      #LAZERAS MODIFIED  {Top Tier Troops Recruit}

      ## CC
      # keys
      # (assign, "$g_camera_up", key_up),
      # (assign, "$g_camera_down", key_down),
      # (assign, "$g_camera_left", key_left),
      # (assign, "$g_camera_right", key_right),
      
      # hp bars
      # (assign, "$g_hp_bar_dis_limit", 30),
      # (assign, "$g_hp_bar_ally", 0),
      # (assign, "$g_hp_bar_enemy", 0),
      
      ##Floris: Updated from CC 1.321
      #This is the fog of war on the map. Unfortunately it doesn't work yet as intended, therefor I disabled it.
      #      # pf_always_visible to 0
      #      (try_for_range, ":center_no", centers_begin, centers_end),
      #        (party_set_flags, ":center_no", pf_always_visible, 0),
      #      (try_end),
      #The following lines are removed in CC 1.322, but I actually like them...
      #      # hide troops' name
      #      (try_for_range, ":troop_no", ransom_brokers_begin, companions_end),
      #        (neq, ":troop_no", "trp_kingdom_heroes_including_player_begin"),
      #        (troop_set_name, ":troop_no", "@???"),
      #      (try_end),
      ##
      
      # chest troop
      (try_for_range, ":town_no", walled_centers_begin, walled_centers_end),
        (store_sub, ":offset", ":town_no", towns_begin),
        (store_add, ":cur_object_no", "trp_town_1_seneschal", ":offset"),
        (party_set_slot,":town_no", slot_town_seneschal, ":cur_object_no"),
      (try_end),
      
      # food
      (try_for_range, ":cur_food", food_begin, food_end),
        (item_set_slot, ":cur_food", slot_item_food_portion, 1),
      (try_end),
      
      # bandit troops
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
	  ##Floris MTT End
      (try_for_range, ":troop_id", ":outlaws_begin", ":outlaws_end"), ##Floris MTT - was bandit_troops_begin, bandit_troops_end
        (store_troop_faction, ":faction_id", ":troop_id"),
        (troop_set_slot, ":troop_id", slot_troop_original_faction, ":faction_id"),
        (troop_set_faction, ":troop_id", "fac_outlaws"),
      (try_end),
      
      # (assign, "$g_report_extra_xp_and_wpt", 1), ##CC 1.324
      # (assign, "$g_report_shot_distance", 1), ##CC 1.324
      # (assign, "$g_speed_ai_battles", 1),
      # #(assign, "$g_game_difficulty", 1), ##CC 1.324
      # (assign, "$g_rand_rain_limit", 30),
      # (assign, "$g_encumbrance_penalty", 1),
	  # (assign, "$g_show_minimap", 0),
      # (assign, "$g_minimap_ratio", 80),
      (troop_set_auto_equip, "trp_player", 0),
      
      (call_script, "script_init_item_score"),
      
      (assign, "$g_persuasion_success_count", 0),
      (assign, "$g_persuasion_success_limit", 50),
      (assign, "$g_reinforcement_stage", 20),

      
      (assign, "$g_auto_sell_price_limit", 50),
      (item_set_slot, itp_type_book, slot_item_type_not_for_sell, 1),
      (item_set_slot, itp_type_goods, slot_item_type_not_for_sell, 1),
      (item_set_slot, itp_type_animal, slot_item_type_not_for_sell, 1),
      ## CC
      
      (faction_set_slot, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
      (assign, "$g_player_luck", 200),
      (assign, "$g_player_luck", 200), ##1.134
      (troop_set_slot, "trp_player", slot_troop_occupation, slto_kingdom_hero),
      (store_random_in_range, ":starting_training_ground", training_grounds_begin, training_grounds_end),
      (party_relocate_near_party, "p_main_party", ":starting_training_ground", 3),
      (str_store_troop_name, s5, "trp_player"),
      (party_set_name, "p_main_party", s5),
      (call_script, "script_update_party_creation_random_limits"),
      (assign, "$g_player_party_icon", -1),
      
      #Warband changes begin -- set this early
      (try_for_range, ":npc", 0, kingdom_ladies_end),
        (this_or_next|eq, ":npc", "trp_player"),
        (is_between, ":npc", active_npcs_begin, kingdom_ladies_end),
        (troop_set_slot, ":npc", slot_troop_father, -1),
        (troop_set_slot, ":npc", slot_troop_mother, -1),
        (troop_set_slot, ":npc", slot_troop_guardian, -1),
        (troop_set_slot, ":npc", slot_troop_spouse, -1),
        (troop_set_slot, ":npc", slot_troop_betrothed, -1),
        (troop_set_slot, ":npc", slot_troop_prisoner_of_party, -1),
        (troop_set_slot, ":npc", slot_lady_last_suitor, -1),
        (troop_set_slot, ":npc", slot_troop_stance_on_faction_issue, -1),
        
        (store_random_in_range, ":decision_seed", 0, 10000),
        (troop_set_slot, ":npc", slot_troop_set_decision_seed, ":decision_seed"),	#currently not used
        (troop_set_slot, ":npc", slot_troop_temp_decision_seed, ":decision_seed"),	#currently not used, holds for at least 24 hours
	  (try_end),

	  (assign, "$g_lord_long_term_count", 0),
	  ##diplomacy start+ Clear faction leader/marshall, since 0 is the player
	  (try_for_range, ":faction_no", 0, dplmc_factions_end),
	     (neq, ":faction_no", "fac_player_faction"),
	     (neq, ":faction_no", "fac_player_supporters_faction"),
	     (faction_set_slot, ":faction_no", slot_faction_leader, -1),
	     (faction_set_slot, ":faction_no", slot_faction_marshall, -1),
	  (try_end),
	  ##diplomacy end+

	  (call_script, "script_initialize_banner_info"),
	  (call_script, "script_initialize_item_info"),
	  (call_script, "script_initialize_aristocracy"),
      (call_script, "script_initialize_npcs"),
      (assign, "$disable_npc_complaints", 0),
      #NPC companion changes end
      
      # Setting random feast time
      (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (store_random_in_range, ":last_feast_time", 0, 312), #240 + 72
        (val_mul, ":last_feast_time", -1),
        (faction_set_slot, ":faction_no", slot_faction_last_feast_start_time, ":last_feast_time"),
      (try_end),
      
      # Setting the random town sequence:
      (store_sub, ":num_towns", towns_end, towns_begin),
      (assign, ":num_iterations", ":num_towns"),
      (try_for_range, ":cur_town_no", 0, ":num_towns"),
        (troop_set_slot, "trp_random_town_sequence", ":cur_town_no", -1),
      (try_end),
      (assign, ":cur_town_no", 0),
      (try_for_range, ":unused", 0, ":num_iterations"),
        (store_random_in_range, ":random_no", 0, ":num_towns"),
        (assign, ":is_unique", 1),
        (try_for_range, ":cur_town_no_2", 0, ":num_towns"),
          (troop_slot_eq, "trp_random_town_sequence", ":cur_town_no_2", ":random_no"),
          (assign, ":is_unique", 0),
        (try_end),
        (try_begin),
          (eq, ":is_unique", 1),
          (troop_set_slot, "trp_random_town_sequence", ":cur_town_no", ":random_no"),
          (val_add, ":cur_town_no", 1),
        (else_try),
          (val_add, ":num_iterations", 1),
        (try_end),
      (try_end),
      

	  
	  
      # Cultures:
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_1_troop, "trp_swadian_e_peasant"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_2_troop, "trp_swadian_e_militia"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_3_troop, "trp_swadian_e_vougier"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_4_troop, "trp_swadian_e_piquier"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_5_troop, "trp_swadian_e_chevalier"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_6_troop, "trp_swadian_e_chevalier_banneret"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_7_troop, "trp_swadian_e_baron_mineures"),
		  
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_1_troop, "trp_vaegir_e_kholop"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_2_troop, "trp_vaegir_e_otrok"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_3_troop, "trp_vaegir_e_kazak"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_4_troop, "trp_vaegir_e_yesaul"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_5_troop, "trp_vaegir_e_ataman"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_6_troop, "trp_vaegir_e_legkoy_vityas"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_7_troop, "trp_vaegir_e_bogatyr"),
		  
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_1_troop, "trp_khergit_e_tariachin"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_2_troop, "trp_khergit_e_tsereg"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_3_troop, "trp_khergit_e_morici"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_4_troop, "trp_khergit_e_yabagharu_morici"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_5_troop, "trp_khergit_e_torguu"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_6_troop, "trp_khergit_e_khorchen"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_7_troop, "trp_khergit_e_cherbi"),
		  
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_1_troop, "trp_nord_e_bondi"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_2_troop, "trp_nord_e_huskarl"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_3_troop, "trp_nord_e_gridman"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_4_troop, "trp_nord_e_ascoman"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_5_troop, "trp_nord_e_hirdman"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_6_troop, "trp_nord_e_skutilsveinr"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_7_troop, "trp_nord_e_aetheling"),
		  
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_1_troop, "trp_rhodok_e_cittadino"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_2_troop, "trp_rhodok_e_novizio"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_3_troop, "trp_rhodok_e_milizia"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_4_troop, "trp_rhodok_e_lanza_spezzata"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_5_troop, "trp_rhodok_e_provisionato"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_6_troop, "trp_rhodok_e_capitano_di_ventura"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_7_troop, "trp_rhodok_e_condottiero"),
		  
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_1_troop, "trp_sarranid_e_millet"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_2_troop, "trp_sarranid_e_ajam"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_3_troop, "trp_sarranid_e_azab"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_4_troop, "trp_sarranid_e_al_haqa"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_5_troop, "trp_sarranid_e_kapikula"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_6_troop, "trp_sarranid_e_qilich_arslan"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_7_troop, "trp_sarranid_e_hasham"),

		  #Player Faction
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_1_troop, "trp_custom_e_recruit"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_2_troop, "trp_custom_e_militia"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_3_troop, "trp_custom_e_guard"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_4_troop, "trp_custom_e_swordman"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_5_troop, "trp_custom_e_swordmaster"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_6_troop, "trp_custom_e_heavy_knight"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_7_troop, "trp_custom_e_heavy_horse_archer"),
		  #Player Faction
      
      (faction_set_slot, "fac_culture_1", slot_faction_town_walker_male_troop, "trp_swadian_town_walker_m_average"),
      (faction_set_slot, "fac_culture_1", slot_faction_town_walker_female_troop, "trp_swadian_town_walker_f_average"),
      (faction_set_slot, "fac_culture_1", slot_faction_village_walker_male_troop, "trp_swadian_village_walker_m_average"),
      (faction_set_slot, "fac_culture_1", slot_faction_village_walker_female_troop, "trp_swadian_village_walker_f_average"),
      (faction_set_slot, "fac_culture_1", slot_faction_town_spy_male_troop, "trp_swadian_spy_walker_1"),
      (faction_set_slot, "fac_culture_1", slot_faction_town_spy_female_troop, "trp_swadian_spy_walker_2"),
      
      (faction_set_slot, "fac_culture_2", slot_faction_town_walker_male_troop, "trp_vaegir_town_walker_m_average"),
      (faction_set_slot, "fac_culture_2", slot_faction_town_walker_female_troop, "trp_vaegir_town_walker_f_average"),
      (faction_set_slot, "fac_culture_2", slot_faction_village_walker_male_troop, "trp_vaegir_village_walker_m_average"),
      (faction_set_slot, "fac_culture_2", slot_faction_village_walker_female_troop, "trp_vaegir_village_walker_f_average"),
      (faction_set_slot, "fac_culture_2", slot_faction_town_spy_male_troop, "trp_vaegir_spy_walker_1"),
      (faction_set_slot, "fac_culture_2", slot_faction_town_spy_female_troop, "trp_vaegir_spy_walker_2"),
      
      (faction_set_slot, "fac_culture_3", slot_faction_town_walker_male_troop, "trp_khergit_town_walker_m_average"),
      (faction_set_slot, "fac_culture_3", slot_faction_town_walker_female_troop, "trp_khergit_town_walker_f_average"),
      (faction_set_slot, "fac_culture_3", slot_faction_village_walker_male_troop, "trp_khergit_village_walker_m_average"),
      (faction_set_slot, "fac_culture_3", slot_faction_village_walker_female_troop, "trp_khergit_village_walker_f_average"),
      (faction_set_slot, "fac_culture_3", slot_faction_town_spy_male_troop, "trp_khergit_spy_walker_1"),
      (faction_set_slot, "fac_culture_3", slot_faction_town_spy_female_troop, "trp_khergit_spy_walker_2"),
      
      (faction_set_slot, "fac_culture_4", slot_faction_town_walker_male_troop, "trp_nord_town_walker_m_average"),
      (faction_set_slot, "fac_culture_4", slot_faction_town_walker_female_troop, "trp_nord_town_walker_f_average"),
      (faction_set_slot, "fac_culture_4", slot_faction_village_walker_male_troop, "trp_nord_village_walker_m_average"),
      (faction_set_slot, "fac_culture_4", slot_faction_village_walker_female_troop, "trp_nord_village_walker_f_average"),
      (faction_set_slot, "fac_culture_4", slot_faction_town_spy_male_troop, "trp_nord_spy_walker_1"),
      (faction_set_slot, "fac_culture_4", slot_faction_town_spy_female_troop, "trp_nord_spy_walker_2"),
      
      (faction_set_slot, "fac_culture_5", slot_faction_town_walker_male_troop, "trp_rhodok_town_walker_m_average"),
      (faction_set_slot, "fac_culture_5", slot_faction_town_walker_female_troop, "trp_rhodok_town_walker_f_average"),
      (faction_set_slot, "fac_culture_5", slot_faction_village_walker_male_troop, "trp_rhodok_village_walker_m_average"),
      (faction_set_slot, "fac_culture_5", slot_faction_village_walker_female_troop, "trp_rhodok_village_walker_f_average"),
      (faction_set_slot, "fac_culture_5", slot_faction_town_spy_male_troop, "trp_rhodok_spy_walker_1"),
      (faction_set_slot, "fac_culture_5", slot_faction_town_spy_female_troop, "trp_rhodok_spy_walker_2"),
      
      (faction_set_slot, "fac_culture_6", slot_faction_town_walker_male_troop, "trp_sarranid_town_walker_m_average"),
      (faction_set_slot, "fac_culture_6", slot_faction_town_walker_female_troop, "trp_sarranid_town_walker_f_average"),
      (faction_set_slot, "fac_culture_6", slot_faction_village_walker_male_troop, "trp_sarranid_village_walker_m_average"),
      (faction_set_slot, "fac_culture_6", slot_faction_village_walker_female_troop, "trp_sarranid_village_walker_f_average"),
      (faction_set_slot, "fac_culture_6", slot_faction_town_spy_male_troop, "trp_sarranid_spy_walker_1"),
      (faction_set_slot, "fac_culture_6", slot_faction_town_spy_female_troop, "trp_sarranid_spy_walker_2"),

      #Player Faction
      (faction_set_slot, "fac_culture_7", slot_faction_town_walker_male_troop, "trp_town_walker_m_average"),
      (faction_set_slot, "fac_culture_7", slot_faction_town_walker_female_troop, "trp_town_walker_f_average"),
      (faction_set_slot, "fac_culture_7", slot_faction_village_walker_male_troop, "trp_village_walker_m_average"),
      (faction_set_slot, "fac_culture_7", slot_faction_village_walker_female_troop, "trp_village_walker_f_average"),
      (faction_set_slot, "fac_culture_7", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
      (faction_set_slot, "fac_culture_7", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),
      #Player Faction
      
      (try_begin),
        (eq, "$cheat_mode", 1),
        (assign, reg3, "$cheat_mode"),
        (display_message, "@{!}DEBUG : Completed faction troop assignments, cheat mode: {reg3}"),
      (try_end),
      
      # Factions:
      (faction_set_slot, "fac_kingdom_1",  slot_faction_culture, "fac_culture_1"),
      (faction_set_slot, "fac_kingdom_1",  slot_faction_leader, "trp_kingdom_1_lord"),
      (troop_set_slot, "trp_kingdom_1_lord", slot_troop_renown, 1200),
      
      (faction_set_slot, "fac_kingdom_2",  slot_faction_culture, "fac_culture_2"),
      (faction_set_slot, "fac_kingdom_2",  slot_faction_leader, "trp_kingdom_2_lord"),
      (troop_set_slot, "trp_kingdom_2_lord", slot_troop_renown, 1200),
      
      (faction_set_slot, "fac_kingdom_3",  slot_faction_culture, "fac_culture_3"),
      (faction_set_slot, "fac_kingdom_3",  slot_faction_leader, "trp_kingdom_3_lord"),
      (troop_set_slot, "trp_kingdom_3_lord", slot_troop_renown, 1200),
      
      (faction_set_slot, "fac_kingdom_4",  slot_faction_culture, "fac_culture_4"),
      (faction_set_slot, "fac_kingdom_4",  slot_faction_leader, "trp_kingdom_4_lord"),
      (troop_set_slot, "trp_kingdom_4_lord", slot_troop_renown, 1200),
      
      (faction_set_slot, "fac_kingdom_5",  slot_faction_culture, "fac_culture_5"),
      (faction_set_slot, "fac_kingdom_5",  slot_faction_leader, "trp_kingdom_5_lord"),
      (troop_set_slot, "trp_kingdom_5_lord", slot_troop_renown, 1200),
      
      (faction_set_slot, "fac_kingdom_6",  slot_faction_culture, "fac_culture_6"),
      (faction_set_slot, "fac_kingdom_6",  slot_faction_leader, "trp_kingdom_6_lord"),
      (troop_set_slot, "trp_kingdom_6_lord", slot_troop_renown, 1200),
      
      (assign, ":player_faction_culture", "fac_culture_1"),##Floris: Changed it from 7 to 1 to make it savegame compatible
      (faction_set_slot, "fac_player_supporters_faction",  slot_faction_culture, ":player_faction_culture"),##Floris: Stayed the same.
      (faction_set_slot, "fac_player_faction",  slot_faction_culture, ":player_faction_culture"),
      
      (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_set_slot, ":faction_no", slot_faction_marshall, -1),
      (try_end),
      (faction_set_slot, "fac_player_supporters_faction", slot_faction_marshall, "trp_player"),
      (call_script, "script_initialize_faction_troop_types"),
      ##diplomacy begin
      (call_script, "script_dplmc_init_domestic_policy"),
      ##diplomacy end
      
      
      # Towns:
      (try_for_range, ":item_no", trade_goods_begin, trade_goods_end),
        (store_sub, ":offset", ":item_no", trade_goods_begin),
        (val_add, ":offset", slot_town_trade_good_prices_begin),
        (try_for_range, ":center_no", centers_begin, centers_end),
          (party_set_slot, ":center_no", ":offset", average_price_factor), #1000
        (try_end),
        ##        (party_set_slot, "p_zendar", ":offset", average_price_factor),
        ##        (party_set_slot, "p_salt_mine", ":offset", average_price_factor),
        ##        (party_set_slot, "p_four_ways_inn", ":offset", average_price_factor),
      (try_end),
      
      (call_script, "script_initialize_trade_routes"),
      (call_script, "script_initialize_sea_trade_routes"), ###Seatrade Marker
      (call_script, "script_initialize_town_arena_info"),
      #start some tournaments
      (try_for_range, ":town_no", towns_begin, towns_end),
        (store_random_in_range, ":rand", 0, 100),
        (lt, ":rand", 20),
        (store_random_in_range, ":random_days", 12, 15),
        (party_set_slot, ":town_no", slot_town_has_tournament, ":random_days"),
      (try_end),
      
      #village products -- at some point we might make it so that the villages supply raw materials to towns, and the towns produce manufactured goods
      #village products designate the raw materials produced in the vicinity
      #right now, just doing a test for grain produced in the swadian heartland
      
      
      # fill_village_bound_centers
      #pass 1: Give one village to each castle
      (try_for_range, ":cur_center", castles_begin, castles_end),
        (assign, ":min_dist", 999999),
        (assign, ":min_dist_village", -1),
        (try_for_range, ":cur_village", villages_begin, villages_end),
          (neg|party_slot_ge, ":cur_village", slot_village_bound_center, 1), #skip villages which are already bound.
          (store_distance_to_party_from_party, ":cur_dist", ":cur_village", ":cur_center"),
          (lt, ":cur_dist", ":min_dist"),
          (assign, ":min_dist", ":cur_dist"),
          (assign, ":min_dist_village", ":cur_village"),
        (try_end),
        (party_set_slot, ":min_dist_village", slot_village_bound_center, ":cur_center"),
        (store_faction_of_party, ":town_faction", ":cur_center"),
        (call_script, "script_give_center_to_faction_aux", ":min_dist_village", ":town_faction"),
      (try_end),
      
      
      #pass 2: Give other villages to closest town.
      (try_for_range, ":cur_village", villages_begin, villages_end),
        (neg|party_slot_ge, ":cur_village", slot_village_bound_center, 1), #skip villages which are already bound.
        (assign, ":min_dist", 999999),
        (assign, ":min_dist_town", -1),
        (try_for_range, ":cur_town", towns_begin, towns_end),
          (store_distance_to_party_from_party, ":cur_dist", ":cur_village", ":cur_town"),
          (lt, ":cur_dist", ":min_dist"),
          (assign, ":min_dist", ":cur_dist"),
          (assign, ":min_dist_town", ":cur_town"),
        (try_end),
        (party_set_slot, ":cur_village", slot_village_bound_center, ":min_dist_town"),
        (store_faction_of_party, ":town_faction", ":min_dist_town"),
        (call_script, "script_give_center_to_faction_aux", ":cur_village", ":town_faction"),
      (try_end),
	  
	# Towns (loop)
    (try_for_range, ":town_no", towns_begin, towns_end),
        (store_sub, ":offset", ":town_no", towns_begin),
        (party_set_slot,":town_no", slot_party_type, spt_town),
        #(store_add, ":cur_object_no", "trp_town_1_seneschal", ":offset"),
        #(party_set_slot,":town_no", slot_town_seneschal, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_center", ":offset"),
        (party_set_slot,":town_no", slot_town_center, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_castle", ":offset"),
        (party_set_slot,":town_no", slot_town_castle, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_prison", ":offset"),
        (party_set_slot,":town_no", slot_town_prison, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_walls", ":offset"),
        (party_set_slot,":town_no", slot_town_walls, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_tavern", ":offset"),
        (party_set_slot,":town_no", slot_town_tavern, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_store", ":offset"),
        (party_set_slot,":town_no", slot_town_store, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_arena", ":offset"),
        (party_set_slot,":town_no", slot_town_arena, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_alley", ":offset"),
        (party_set_slot,":town_no", slot_town_alley, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_mayor", ":offset"),
        (party_set_slot,":town_no", slot_town_elder, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_tavernkeeper", ":offset"),
        (party_set_slot,":town_no", slot_town_tavernkeeper, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_weaponsmith", ":offset"),
        (party_set_slot,":town_no", slot_town_weaponsmith, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_armorer", ":offset"),
        (party_set_slot,":town_no", slot_town_armorer, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_merchant", ":offset"),
        (party_set_slot,":town_no", slot_town_merchant, ":cur_object_no"),
        (store_add, ":cur_object_no", "trp_town_1_horse_merchant", ":offset"),
        (party_set_slot,":town_no", slot_town_horse_merchant, ":cur_object_no"),
        (store_add, ":cur_object_no", "scn_town_1_center", ":offset"),
        (party_set_slot,":town_no", slot_town_center, ":cur_object_no"),
		
		(party_set_slot,":town_no", slot_town_reinforcement_party_template, "pt_center_reinforcements"),

    (try_end),
      
      # Castles
    (try_for_range, ":castle_no", castles_begin, castles_end),
        (store_sub, ":offset", ":castle_no", castles_begin),
        (val_mul, ":offset", 3),
        
        #        (store_add, ":senechal_troop_no", "trp_castle_1_seneschal", ":offset"),
        #        (party_set_slot,":castle_no", slot_town_seneschal, ":senechal_troop_no"),
        (store_add, ":exterior_scene_no", "scn_castle_1_exterior", ":offset"),
        (party_set_slot,":castle_no", slot_castle_exterior, ":exterior_scene_no"),
        (store_add, ":interior_scene_no", "scn_castle_1_interior", ":offset"),
        (party_set_slot,":castle_no", slot_town_castle, ":interior_scene_no"),
        (store_add, ":interior_scene_no", "scn_castle_1_prison", ":offset"),
        (party_set_slot,":castle_no", slot_town_prison, ":interior_scene_no"),
        
		(party_set_slot,":castle_no", slot_town_reinforcement_party_template, "pt_center_reinforcements"),
        (party_set_slot,":castle_no", slot_party_type, spt_castle),
        (party_set_slot,":castle_no", slot_center_is_besieged_by, -1),
		
	(try_end),
      
      
      # Set which castles need to be attacked with siege towers.
      (party_set_slot,"p_town_13", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_town_16", slot_center_siege_with_belfry, 1),
      
      (party_set_slot,"p_castle_1", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_2", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_4", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_7", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_8", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_9", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_11", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_13", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_21", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_25", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_34", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_35", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_38", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_40", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_41", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_42", slot_center_siege_with_belfry, 1),
      (party_set_slot,"p_castle_43", slot_center_siege_with_belfry, 1),
      
      # Villages characters
      (try_for_range, ":village_no", villages_begin, villages_end),
        (store_sub, ":offset", ":village_no", villages_begin),
        
        (store_add, ":exterior_scene_no", "scn_village_1", ":offset"),
        (party_set_slot,":village_no", slot_castle_exterior, ":exterior_scene_no"),
        
        (store_add, ":store_troop_no", "trp_village_1_elder", ":offset"),
        (party_set_slot,":village_no", slot_town_elder, ":store_troop_no"),
        
        (party_set_slot,":village_no", slot_party_type, spt_village),
        (party_set_slot,":village_no", slot_village_raided_by, -1),
        
        (call_script, "script_start_refresh_village_defenders", ":village_no"),
        (call_script, "script_start_refresh_village_defenders", ":village_no"),
        (call_script, "script_start_refresh_village_defenders", ":village_no"),
        (call_script, "script_start_refresh_village_defenders", ":village_no"),
      (try_end),
      
      (try_for_range, ":center_no", centers_begin, centers_end),
        (party_set_slot, ":center_no", slot_center_last_spotted_enemy, -1),
        (party_set_slot, ":center_no", slot_center_is_besieged_by, -1),
        (party_set_slot, ":center_no", slot_center_last_taken_by_troop, -1),
        ##diplomacy start+ Set the home slots for town merchants, elders, etc. for reverse-lookup
        (try_for_range, ":offset", dplmc_slot_town_merchants_begin, dplmc_slot_town_merchants_end),
           (party_get_slot, ":npc", ":center_no", ":offset"),
           (gt, ":npc", 0),
           (neg|troop_slot_ge, ":npc", slot_troop_home, 1),#If the startup script wasn't altered by another mod, we don't have to worry about this condition.
           (troop_set_slot, ":npc", slot_troop_home, ":center_no"),
        (try_end),
        ##diplomacy end+
      (try_end),

# Troops:

# Assign banners and renown.
# We assume there are enough banners for all kingdom heroes.

      #faction banners
      (faction_set_slot, "fac_kingdom_1", slot_faction_banner, "mesh_banner_kingdom_f"),
      (faction_set_slot, "fac_kingdom_2", slot_faction_banner, "mesh_banner_kingdom_b"),
      (faction_set_slot, "fac_kingdom_3", slot_faction_banner, "mesh_banner_kingdom_c"),
      (faction_set_slot, "fac_kingdom_4", slot_faction_banner, "mesh_banner_kingdom_a"),
      (faction_set_slot, "fac_kingdom_5", slot_faction_banner, "mesh_banner_kingdom_d"),
      (faction_set_slot, "fac_kingdom_6", slot_faction_banner, "mesh_banner_kingdom_e"),

      (try_for_range, ":cur_faction", npc_kingdoms_begin, npc_kingdoms_end),
        (faction_get_slot, ":cur_faction_king", ":cur_faction", slot_faction_leader),
        (faction_get_slot, ":cur_faction_banner", ":cur_faction", slot_faction_banner),
        (val_sub, ":cur_faction_banner", banner_meshes_begin),
        (val_add, ":cur_faction_banner", banner_scene_props_begin),
        (troop_set_slot, ":cur_faction_king", slot_troop_banner_scene_prop, ":cur_faction_banner"),
      (try_end),
      (assign, ":num_swadia_lords_assigned", 0),
      (assign, ":num_vaegir_lords_assigned", 0),
      (assign, ":num_khergit_lords_assigned", 0),
      (assign, ":num_nord_lords_assigned", 0),
      (assign, ":num_rhodok_lords_assigned", 0),
      (assign, ":num_sarranid_lords_assigned", 0),
      (assign, ":num_other_lords_assigned", 0),

      (try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
        (this_or_next|troop_slot_eq, ":kingdom_hero", slot_troop_occupation, slto_kingdom_hero),
        (troop_slot_eq, ":kingdom_hero", slot_troop_occupation, slto_inactive_pretender),

        (store_troop_faction, ":kingdom_hero_faction", ":kingdom_hero"),
        (neg|faction_slot_eq, ":kingdom_hero_faction", slot_faction_leader, ":kingdom_hero"),
        (try_begin),
          (eq, ":kingdom_hero_faction", "fac_kingdom_1"), #Kingdom of Swadia
          (store_add, ":kingdom_1_banners_begin", banner_scene_props_begin, swadia_banners_begin_offset),
          (store_add, ":banner_id", ":kingdom_1_banners_begin", ":num_swadia_lords_assigned"),
          (troop_set_slot, ":kingdom_hero", slot_troop_banner_scene_prop, ":banner_id"),
          (val_add, ":num_swadia_lords_assigned", 1),
        (else_try),
          (eq, ":kingdom_hero_faction", "fac_kingdom_2"), #Grand Principiality of Vaegir
          (store_add, ":kingdom_2_banners_begin", banner_scene_props_begin, vaegir_banners_begin_offset),
          (store_add, ":banner_id", ":kingdom_2_banners_begin", ":num_vaegir_lords_assigned"),
          (troop_set_slot, ":kingdom_hero", slot_troop_banner_scene_prop, ":banner_id"),
          (val_add, ":num_vaegir_lords_assigned", 1),
        (else_try),
          (eq, ":kingdom_hero_faction", "fac_kingdom_3"), #Khergit Khanate
          (store_add, ":kingdom_3_banners_begin", banner_scene_props_begin, khergit_banners_begin_offset),
          (store_add, ":banner_id", ":kingdom_3_banners_begin", ":num_khergit_lords_assigned"),
          (troop_set_slot, ":kingdom_hero", slot_troop_banner_scene_prop, ":banner_id"),
          (val_add, ":num_khergit_lords_assigned", 1),
        (else_try),
          (eq, ":kingdom_hero_faction", "fac_kingdom_4"), #Kingdom of Nord
          (store_add, ":kingdom_4_banners_begin", banner_scene_props_begin, nord_banners_begin_offset),
          (store_add, ":banner_id", ":kingdom_4_banners_begin", ":num_nord_lords_assigned"),
          (troop_set_slot, ":kingdom_hero", slot_troop_banner_scene_prop, ":banner_id"),
          (val_add, ":num_nord_lords_assigned", 1),
        (else_try),
          (eq, ":kingdom_hero_faction", "fac_kingdom_5"), #Rhodok Republic
          (store_add, ":kingdom_5_banners_begin", banner_scene_props_begin, rhodok_banners_begin_offset),
          (store_add, ":banner_id", ":kingdom_5_banners_begin", ":num_rhodok_lords_assigned"),
          (troop_set_slot, ":kingdom_hero", slot_troop_banner_scene_prop, ":banner_id"),
          (val_add, ":num_rhodok_lords_assigned", 1),
        (else_try),
          (eq, ":kingdom_hero_faction", "fac_kingdom_6"), #Sarranid Sultanate
          (store_add, ":kingdom_6_banners_begin", banner_scene_props_begin, sarranid_banners_begin_offset),
          (store_add, ":banner_id", ":kingdom_6_banners_begin", ":num_sarranid_lords_assigned"),
          (troop_set_slot, ":kingdom_hero", slot_troop_banner_scene_prop, ":banner_id"),
          (val_add, ":num_sarranid_lords_assigned", 1),
        (else_try),
          (assign, ":hero_offset", ":num_other_lords_assigned"),
          (try_begin),
            (gt, ":hero_offset", swadia_banners_begin_offset),#Do not add swadian banners to other lords
            (val_add, ":hero_offset", swadia_banners_end_offset),
            (val_sub, ":hero_offset", swadia_banners_begin_offset),
          (try_end),
          (try_begin),
            (gt, ":hero_offset", vaegir_banners_begin_offset),#Do not add vaegir banners to other lords
            (val_add, ":hero_offset", vaegir_banners_end_offset),
            (val_sub, ":hero_offset", vaegir_banners_begin_offset),
          (try_end),
          (try_begin),
            (gt, ":hero_offset", khergit_banners_begin_offset),#Do not add khergit banners to other lords
            (val_add, ":hero_offset", khergit_banners_end_offset),
            (val_sub, ":hero_offset", khergit_banners_begin_offset),
          (try_end),
          (try_begin),
            (gt, ":hero_offset", nord_banners_begin_offset),#Do not add nord banners to other lords
            (val_add, ":hero_offset", nord_banners_end_offset),
            (val_sub, ":hero_offset", nord_banners_begin_offset),
          (try_end),
          (try_begin),
            (gt, ":hero_offset", rhodok_banners_begin_offset),#Do not add rhodok banners to other lords
            (val_add, ":hero_offset", nord_banners_end_offset),
            (val_sub, ":hero_offset", nord_banners_begin_offset),
          (try_end),
          (try_begin),
            (gt, ":hero_offset", sarranid_banners_begin_offset),#Do not add sarranid banners to other lords
            (val_add, ":hero_offset", sarranid_banners_end_offset),
            (val_sub, ":hero_offset", sarranid_banners_begin_offset),
          (try_end),
          (store_add, ":banner_id", banner_scene_props_begin, ":hero_offset"),
          (troop_set_slot, ":kingdom_hero", slot_troop_banner_scene_prop, ":banner_id"),
          (val_add, ":num_other_lords_assigned", 1),
        (try_end),
        (try_begin),
          (this_or_next|lt, ":banner_id", banner_scene_props_begin),
          (gt, ":banner_id", banner_scene_props_end_minus_one),
          (display_message, "@{!}ERROR: Not enough banners for heroes!"),
        (try_end),

		##CABA - comment out: this isn't the place for these; moved to dialogs "member_fief_grant_3"
		# (troop_set_slot, "trp_npc1", slot_troop_banner_scene_prop, "spr_banner_companions01"),
		# (troop_set_slot, "trp_npc2", slot_troop_banner_scene_prop, "spr_banner_companions02"),
		# (troop_set_slot, "trp_npc3", slot_troop_banner_scene_prop, "spr_banner_companions03"),
		# (troop_set_slot, "trp_npc4", slot_troop_banner_scene_prop, "spr_banner_companions04"),
		# (troop_set_slot, "trp_npc5", slot_troop_banner_scene_prop, "spr_banner_companions05"),
		# (troop_set_slot, "trp_npc6", slot_troop_banner_scene_prop, "spr_banner_companions06"),
		# (troop_set_slot, "trp_npc7", slot_troop_banner_scene_prop, "spr_banner_companions07"),
		# (troop_set_slot, "trp_npc8", slot_troop_banner_scene_prop, "spr_banner_companions08"),
		# (troop_set_slot, "trp_npc9", slot_troop_banner_scene_prop, "spr_banner_companions09"),
		# (troop_set_slot, "trp_npc10", slot_troop_banner_scene_prop, "spr_banner_companions10"),
		# (troop_set_slot, "trp_npc11", slot_troop_banner_scene_prop, "spr_banner_companions11"),
		# (troop_set_slot, "trp_npc12", slot_troop_banner_scene_prop, "spr_banner_companions12"),
		# (troop_set_slot, "trp_npc13", slot_troop_banner_scene_prop, "spr_banner_companions13"),
		# (troop_set_slot, "trp_npc14", slot_troop_banner_scene_prop, "spr_banner_companions14"),
		# (troop_set_slot, "trp_npc15", slot_troop_banner_scene_prop, "spr_banner_companions15"),
		# (troop_set_slot, "trp_npc16", slot_troop_banner_scene_prop, "spr_banner_companions16"),
		# (troop_set_slot, "trp_npc17", slot_troop_banner_scene_prop, "spr_banner_companions17"),
		# (troop_set_slot, "trp_npc18", slot_troop_banner_scene_prop, "spr_banner_companions18"),
		# (troop_set_slot, "trp_npc19", slot_troop_banner_scene_prop, "spr_banner_companions19"),
		# (troop_set_slot, "trp_npc20", slot_troop_banner_scene_prop, "spr_banner_companions20"),
		# (troop_set_slot, "trp_npc21", slot_troop_banner_scene_prop, "spr_banner_companions21"),
		# (troop_set_slot, "trp_npc22", slot_troop_banner_scene_prop, "spr_banner_companions22"),
        
        (store_character_level, ":level", ":kingdom_hero"),
        (store_mul, ":renown", ":level", ":level"),
        (val_div, ":renown", 4), #for top lord, is about 400
        
        (troop_get_slot, ":age", ":kingdom_hero", slot_troop_age),
        (store_mul, ":age_addition", ":age", ":age"),
        (val_div, ":age_addition", 8), #for top lord, is about 400
        (val_add, ":renown", ":age_addition"),
        
        (try_begin),
          (faction_slot_eq, ":kingdom_hero_faction", slot_faction_leader, ":kingdom_hero"),
          (store_random_in_range, ":random_renown", 250, 400),
        (else_try),
          (store_random_in_range, ":random_renown", 0, 100),
        (try_end),
        (val_add, ":renown", ":random_renown"),
        
        (troop_set_slot, ":kingdom_hero", slot_troop_renown, ":renown"),
      (try_end),
      
      (try_for_range, ":troop_no", "trp_player", "trp_merchants_end"),
        (add_troop_note_tableau_mesh, ":troop_no", "tableau_troop_note_mesh"),
      (try_end),
      
      (try_for_range, ":center_no", centers_begin, centers_end),
        (add_party_note_tableau_mesh, ":center_no", "tableau_center_note_mesh"),
      (try_end),
      
      (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (is_between, ":faction_no", "fac_kingdom_1", kingdoms_end), #Excluding player kingdom
        (add_faction_note_tableau_mesh, ":faction_no", "tableau_faction_note_mesh"),
      (else_try),
        (add_faction_note_tableau_mesh, ":faction_no", "tableau_faction_note_mesh_banner"),
      (try_end),
      
      #Give centers to factions first, to ensure more equal distributions
      (call_script, "script_give_center_to_faction_aux", "p_town_1", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_town_2", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_town_3", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_town_4", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_town_5", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_town_6", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_town_7", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_town_8", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_town_9", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_town_10", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_town_11", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_town_12", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_town_13", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_town_14", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_town_15", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_town_16", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_town_17", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_town_18", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_town_19", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_town_20", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_town_21", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_town_22", "fac_kingdom_6"),
      
      (call_script, "script_give_center_to_faction_aux", "p_castle_1", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_2", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_3", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_4", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_5", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_6", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_7", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_8", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_9", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_10", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_11", "fac_kingdom_4"),
      
      (call_script, "script_give_center_to_faction_aux", "p_castle_12", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_13", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_14", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_15", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_16", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_17", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_18", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_19", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_20", "fac_kingdom_1"),
      
      (call_script, "script_give_center_to_faction_aux", "p_castle_21", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_22", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_23", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_24", "fac_kingdom_1"),
      
      (call_script, "script_give_center_to_faction_aux", "p_castle_25", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_26", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_27", "fac_kingdom_1"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_28", "fac_kingdom_5"),
      
      (call_script, "script_give_center_to_faction_aux", "p_castle_29", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_30", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_31", "fac_kingdom_1"),
      
      (call_script, "script_give_center_to_faction_aux", "p_castle_32", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_33", "fac_kingdom_5"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_34", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_35", "fac_kingdom_1"),
      
      (call_script, "script_give_center_to_faction_aux", "p_castle_36", "fac_kingdom_4"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_37", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_38", "fac_kingdom_3"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_39", "fac_kingdom_2"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_40", "fac_kingdom_3"),
      
      (call_script, "script_give_center_to_faction_aux", "p_castle_41", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_42", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_43", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_44", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_45", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_46", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_47", "fac_kingdom_6"),
      (call_script, "script_give_center_to_faction_aux", "p_castle_48", "fac_kingdom_6"),
      
      
      #Now give towns to great lords
      (call_script, "script_start_give_center_to_lord", "p_town_1",  "trp_kingdom_4_lord", 0),
      (call_script, "script_start_give_center_to_lord", "p_town_2",  "trp_knight_4_1", 0),
      (call_script, "script_start_give_center_to_lord", "p_town_3",  "trp_knight_5_1", 0),
      (call_script, "script_start_give_center_to_lord", "p_town_4",  "trp_knight_1_1", 0),
      (call_script, "script_start_give_center_to_lord", "p_town_5",  "trp_kingdom_5_lord", 0),
      (call_script, "script_start_give_center_to_lord", "p_town_6",  "trp_kingdom_1_lord", 0),
      (call_script, "script_start_give_center_to_lord", "p_town_7",  "trp_knight_1_2", 0),
      
      (call_script, "script_start_give_center_to_lord", "p_town_8",  "trp_kingdom_2_lord", 0),
      (call_script, "script_start_give_center_to_lord", "p_town_9",  "trp_knight_2_1", 0),
      (call_script, "script_start_give_center_to_lord", "p_town_10", "trp_kingdom_3_lord", 0),
      (call_script, "script_start_give_center_to_lord", "p_town_11", "trp_knight_2_2", 0),
      (call_script, "script_start_give_center_to_lord", "p_town_12", "trp_knight_4_2", 0),
      (call_script, "script_start_give_center_to_lord", "p_town_13", "trp_knight_2_3", 0),
      (call_script, "script_start_give_center_to_lord", "p_town_14", "trp_knight_3_1", 0),
      
      (call_script, "script_start_give_center_to_lord", "p_town_15", "trp_knight_5_2", 0),
      (call_script, "script_start_give_center_to_lord", "p_town_16", "trp_knight_1_4", 0), #changed from 1_3
      (call_script, "script_start_give_center_to_lord", "p_town_17", "trp_knight_3_2", 0),
      (call_script, "script_start_give_center_to_lord", "p_town_18", "trp_knight_3_3", 0),
      
      (call_script, "script_start_give_center_to_lord", "p_town_19", "trp_kingdom_6_lord", 0),
      (call_script, "script_start_give_center_to_lord", "p_town_20", "trp_knight_6_1", 0),
      (call_script, "script_start_give_center_to_lord", "p_town_21", "trp_knight_6_2", 0),
      (call_script, "script_start_give_center_to_lord", "p_town_22", "trp_knight_6_3", 0),
      
      # Give family castles to certain nobles.
      (call_script, "script_start_give_center_to_lord", "p_castle_29", "trp_knight_2_10", 0), #Nelag_Castle
      (call_script, "script_start_give_center_to_lord", "p_castle_30", "trp_knight_3_4", 0), #Asugan_Castle
      (call_script, "script_start_give_center_to_lord", "p_castle_35", "trp_knight_1_3", 0), #Haringoth_Castle
       ##diplomacy start+
      (call_script, "script_give_center_to_lord", "p_castle_33", "trp_knight_5_11", 0), #Etrosq Castle -- why wasn't this being done already?
	  #Add home centers for claimants
	  (troop_set_slot, "trp_kingdom_1_pretender", slot_troop_home, "p_town_4"),#Lady Isolle - Suno
	  (troop_set_slot, "trp_kingdom_2_pretender", slot_troop_home, "p_town_11"),#Prince Valdym - Curaw
      (troop_set_slot, "trp_kingdom_3_pretender", slot_troop_home, "p_town_18"),#Dustum Khan - Narra
      (troop_set_slot, "trp_kingdom_4_pretender", slot_troop_home, "p_town_12"),#Lethwin Far-Seeker - Wercheg
      (troop_set_slot, "trp_kingdom_5_pretender", slot_troop_home, "p_town_3"),#Lord Kastor - Veluca
	  (troop_set_slot, "trp_kingdom_6_pretender", slot_troop_home, "p_town_20"),#Arwa the Pearled One - Durquba
 	  #add ancestral fiefs to home slots (mods not using standard NPCs should remove this)
      (troop_set_slot, "trp_knight_2_10", slot_troop_home, "p_castle_29"), #Nelag_Castle
      (troop_set_slot, "trp_knight_3_4", slot_troop_home, "p_castle_30"), #Asugan_Castle
      (troop_set_slot, "trp_knight_1_3", slot_troop_home, "p_castle_35"), #Haringoth_Castle
      (troop_set_slot, "trp_knight_5_11", slot_troop_home, "p_castle_33"), #Etrosq_Castle
	  #Also the primary six towns:
	  (troop_set_slot, "trp_kingdom_1_lord", slot_troop_home, "p_town_6"),#King Harlaus to Praven
	  (troop_set_slot, "trp_kingdom_2_lord", slot_troop_home, "p_town_8"),#King Yaroglek to Reyvadin
	  (troop_set_slot, "trp_kingdom_3_lord", slot_troop_home, "p_town_10"),#Sanjar Khan to Tulga
	  (troop_set_slot, "trp_kingdom_4_lord", slot_troop_home, "p_town_1"),#King Ragnar to Sargoth
	  (troop_set_slot, "trp_kingdom_5_lord", slot_troop_home, "p_town_5"),#King Graveth to Jelkala
	  (troop_set_slot, "trp_kingdom_6_lord", slot_troop_home, "p_town_19"),#Sultan Hakim to Shariz
      ##diplomacy end+

      (call_script, "script_assign_lords_to_empty_centers"),
      
      #set original factions
      (try_for_range, ":center_no", centers_begin, centers_end),
        (store_faction_of_party, ":original_faction", ":center_no"),
        (faction_get_slot, ":culture", ":original_faction", slot_faction_culture),
        (party_set_slot, ":center_no", slot_center_culture,  ":culture"),
        (party_set_slot, ":center_no", slot_center_original_faction,  ":original_faction"),
        (party_set_slot, ":center_no", slot_center_ex_faction,  ":original_faction"),
		##diplomacy start+ set additional slots
		(party_get_slot, ":town_lord", ":center_no", slot_town_lord),
		
		(try_begin),
			(eq, ":town_lord", "trp_player"),
			#Use trp_kingdom_heroes_including_player_begin instead of trp_player as a workaround for
			#old saved games (since uninitialized memory is 0).
			(party_set_slot, ":center_no", dplmc_slot_center_ex_lord, "trp_kingdom_heroes_including_player_begin"),
			(troop_slot_eq, "trp_player", slot_troop_home, ":center_no"),
			(neg|party_slot_ge, ":center_no", dplmc_slot_center_original_lord, 1),
			(party_set_slot, ":center_no", dplmc_slot_center_original_lord, "trp_kingdom_heroes_including_player_begin"),
		(else_try),
			(party_set_slot, ":center_no", dplmc_slot_center_ex_lord, ":town_lord"),
			(ge, ":town_lord", 0),
			(troop_slot_eq, ":town_lord", slot_troop_home, ":center_no"),
			(neg|party_slot_ge, ":center_no", dplmc_slot_center_original_lord, 1),
			(party_set_slot, ":center_no", dplmc_slot_center_original_lord, ":town_lord"),
		(try_end),
		##diplomacy end+
      (try_end),
      
      #set territorial disputes/outstanding border issues
      (party_set_slot, "p_castle_10", slot_center_ex_faction, "fac_kingdom_2"), #vaegirs claim nord-held alburq
      (party_set_slot, "p_castle_13", slot_center_ex_faction, "fac_kingdom_4"), #nords claim swadian-held kelredan
      (party_set_slot, "p_castle_15", slot_center_ex_faction, "fac_kingdom_1"), #swadians claim rhodok-held ergelon
      (party_set_slot, "p_castle_46", slot_center_ex_faction, "fac_kingdom_5"), #rhodoks claim sarranid-held weyyah
      (party_set_slot, "p_castle_40", slot_center_ex_faction, "fac_kingdom_6"), #sarranids claim khergit-held uhhun
      (party_set_slot, "p_town_11",   slot_center_ex_faction, "fac_kingdom_3"), #Khergits claim vaegir-held curaw
      
      #Swadians, being in the middle, will have additional claims on two of their neighhbors
      (party_set_slot, "p_castle_6", slot_center_ex_faction, "fac_kingdom_1"), #swadians claim vaegir-held tilbault
      (party_set_slot, "p_castle_22", slot_center_ex_faction, "fac_kingdom_1"), #swadians claim khergit-held unuzdaq
      
      (call_script, "script_update_village_market_towns"),
      
	  ##diplomacy start+
	  #(1) Assign plausible ancestral homes to some of the lords (not all of them) who didn't have
      #one set before.  Among other things, this is used for a sense of possessiveness.
      #(2) Assign last-transfer-times to the contested centers.
      (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
		 (try_begin),
			#Assign last-transfer-times to the contested centers.
			(party_get_slot, ":original_faction", ":center_no", slot_center_original_faction),
			(neg|party_slot_eq, ":center_no", slot_center_ex_faction, ":original_faction"),
			(store_random_in_range, ":transfer_time", 1, 181),#some time in the last 180 days (the length of a short game)
			(val_mul, ":transfer_time", -24),
			(party_set_slot, ":center_no", dplmc_slot_center_last_transfer_time, ":transfer_time"),
		 (else_try),
			#For non-contested centers, possibly set the lord's home slot.  Note that because
			#we're iterating in order, lords will get set to towns they own before they get
			#set to cities.
			(party_get_slot, ":town_lord", ":center_no", slot_town_lord),
			(ge, ":town_lord", 1),#only NPCs
			(neg|party_slot_ge, ":center_no", dplmc_slot_center_original_lord, 1),#If there is an original owner who is dispossessed, such as a claimant
			(neg|troop_slot_ge, ":town_lord", slot_troop_home, 1),
			(troop_set_slot, ":town_lord", slot_troop_home, ":center_no"),
		 (try_end),
      (try_end),
	  
	  (try_for_range, ":troop_id", heroes_begin, heroes_end),
	  (try_end),
      #
      #etc.
      (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
		 #If the original owner of the lord is set, don't apply this
		 (neg|party_slot_ge, ":center_no", dplmc_slot_center_original_lord, 1),
		 #Don't apply this to contested centers.
		 (party_get_slot, ":original_faction", ":center_no", slot_center_original_faction),
		 (party_slot_eq, ":center_no", slot_center_ex_faction, ":original_faction"), 
		 #If the owner already has his "home" slot set, don't overwrite it
         (party_get_slot, ":town_lord", ":center_no", slot_town_lord),
		 (neg|troop_slot_ge, ":town_lord", slot_troop_home, 1),
		 #No objections, so go ahead
		 (troop_set_slot, ":town_lord", slot_troop_home, ":center_no"),
      (try_end),
      ##diplomacy end+
	  
	  
      #this should come after assignment of territorial grievances
      (try_for_range, ":unused", 0, 70),
        (try_begin),
          (eq, "$cheat_mode", 1),
          (display_message, "@{!}DEBUG -- initial war/peace check begins"),
        (try_end),
        (call_script, "script_randomly_start_war_peace_new", 0),
      (try_end),
            
      #Initialize walkers
      (try_for_range, ":center_no", centers_begin, centers_end),
        (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
        (party_slot_eq, ":center_no", slot_party_type, spt_village),
        (try_for_range, ":walker_no", 0, num_town_walkers),
          (call_script, "script_center_set_walker_to_type", ":center_no", ":walker_no", walkert_default),
        (try_end),
      (try_end),


	  #This needs to be after market towns
	  (call_script, "script_initialize_economic_information"),

	  (try_for_range, ":village_no", villages_begin, villages_end),
        (call_script, "script_refresh_village_merchant_inventory", ":village_no"),
      (try_end),

      (try_for_range, ":troop_id", original_kingdom_heroes_begin, active_npcs_end),
        (try_begin),
          (store_troop_faction, ":faction_id", ":troop_id"),
          (is_between, ":faction_id", kingdoms_begin, kingdoms_end),
          (troop_set_slot, ":troop_id", slot_troop_original_faction, ":faction_id"),
          (try_begin),
            (is_between, ":troop_id", pretenders_begin, pretenders_end),
            (faction_set_slot, ":faction_id", slot_faction_has_rebellion_chance, 1),
          (try_end),
        (try_end),
        (assign, ":initial_wealth", 6000),
        (try_begin),
          (store_troop_faction, ":faction", ":troop_id"),
          (faction_slot_eq, ":faction", slot_faction_leader, ":troop_id"),
          (assign, ":initial_wealth", 20000),
        (try_end),
        (troop_set_slot, ":troop_id", slot_troop_wealth, ":initial_wealth"),
      (try_end),

      (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),#add town garrisons
        #Add initial center wealth
        (assign, ":initial_wealth", 2000),
        (try_begin),
          (is_between, ":center_no", towns_begin, towns_end),
          (val_mul, ":initial_wealth", 2),
        (try_end),
        (party_set_slot, ":center_no", slot_town_wealth, ":initial_wealth"),

        (assign, ":garrison_strength", 15),
        (try_begin),
          (party_slot_eq, ":center_no", slot_party_type, spt_town),
          (assign, ":garrison_strength", 40),
        (try_end),
        (try_for_range, ":unused", 0, ":garrison_strength"),
          (call_script, "script_cf_reinforce_party", ":center_no"),
        (try_end),
        ## ADD some XP initially
        (store_div, ":xp_rounds", ":garrison_strength", 5),
        (val_add, ":xp_rounds", 2),
        
        (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
        
        (try_begin), #hard
          (eq, ":reduce_campaign_ai", 0),
          (assign, ":xp_addition_for_centers", 7500),
        (else_try), #moderate
          (eq, ":reduce_campaign_ai", 1),
          (assign, ":xp_addition_for_centers", 5000),
        (else_try), #easy
          (eq, ":reduce_campaign_ai", 2),
          (assign, ":xp_addition_for_centers", 2500),
        (try_end),
        
        (try_for_range, ":unused", 0, ":xp_rounds"),
          (party_upgrade_with_xp, ":center_no", ":xp_addition_for_centers", 0),
        (try_end),
        
        #Fill town food stores upto half the limit
        (call_script, "script_center_get_food_store_limit", ":center_no"),
        (assign, ":food_store_limit", reg0),
        (val_div, ":food_store_limit", 2),
        (party_set_slot, ":center_no", slot_party_food_store, ":food_store_limit"),
        
        #create lord parties
        (party_get_slot, ":center_lord", ":center_no", slot_town_lord),
        (ge, ":center_lord", 1),
        (troop_slot_eq, ":center_lord", slot_troop_leaded_party, 0),
		(assign, "$g_there_is_no_avaliable_centers", 0),
        (call_script, "script_create_kingdom_hero_party", ":center_lord", ":center_no"),
        (assign, ":lords_party", "$pout_party"),
        (party_attach_to_party, ":lords_party", ":center_no"),
        (party_set_slot, ":center_no", slot_town_player_odds, 1000),
      (try_end),
      
      #More pre-Warband family structures removed here
      
      #Warband changes begin - set companions relations
      (try_for_range, ":companion", companions_begin, companions_end),
        (try_for_range, ":other_companion", companions_begin, companions_end),
          (neq, ":other_companion", ":companion"),
          (neg|troop_slot_eq, ":companion", slot_troop_personalityclash_object, ":other_companion"),
          (neg|troop_slot_eq, ":companion", slot_troop_personalityclash2_object, ":other_companion"),
          (call_script, "script_troop_change_relation_with_troop", ":companion", ":other_companion", 7), #companions have a starting relation of 14, unless they are rivals
        (try_end),
      (try_end),
      
      #Warband changes continue -  sets relations in the same faction
      (try_for_range, ":lord", original_kingdom_heroes_begin, active_npcs_end),
        (troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
        (troop_get_slot, ":lord_faction", ":lord", slot_troop_original_faction),
        
        (try_for_range, ":other_hero", original_kingdom_heroes_begin, active_npcs_end),
          (this_or_next|troop_slot_eq, ":other_hero", slot_troop_occupation, slto_kingdom_hero),
          (troop_slot_eq, ":other_hero", slot_troop_occupation, slto_inactive_pretender),
          (troop_get_slot, ":other_hero_faction", ":other_hero", slot_troop_original_faction),
          (eq, ":other_hero_faction", ":lord_faction"),
          (call_script, "script_troop_get_family_relation_to_troop", ":lord", ":other_hero"),
          (call_script, "script_troop_change_relation_with_troop", ":lord", ":other_hero", reg0),
          
          (store_random_in_range, ":random", 0, 11), #this will be scored twice between two kingdom heroes, so starting relation will average 10. Between lords and pretenders it will average 7.5
          (call_script, "script_troop_change_relation_with_troop", ":lord", ":other_hero", ":random"),
        (try_end),
      (try_end),
	  
	 ##diplomacy start+
     ##Initialize town "last caravan arrived" times randomly
	  (try_for_range, ":cur_town", towns_begin, towns_end),
	     (try_for_range, ":cur_slot", dplmc_slot_town_trade_route_last_arrivals_begin, dplmc_slot_town_trade_route_last_arrivals_end),
		    (party_slot_eq, ":cur_town", ":cur_slot", 0),
		    (store_random_in_range, ":last_arrived", 1, (24 * 7 * 5) + 1),#some time in the last five weeks
			(val_mul, ":last_arrived", -1),			
			(party_get_slot, ":prosperity_factor", ":cur_town", slot_town_prosperity),#modify plus or minus 40% based on prosperity
			(val_clamp, ":prosperity_factor", 0, 101),
			(val_add, ":prosperity_factor", 75),
			(val_mul, ":last_arrived", 125),
			(val_div, ":last_arrived", ":prosperity_factor"),#last arrival some time in the last five weeks, plus or minus 40%
			(party_set_slot, ":cur_town", ":cur_slot", ":last_arrived"),
		 (try_end),
	  (try_end),
      (try_for_range, ":cur_village", villages_begin, villages_end),
          (party_get_slot, ":prosperity_factor", ":cur_town", slot_town_prosperity),#modify plus or minus 40% based on prosperity
          (val_clamp, ":prosperity_factor", 0, 101),
          (val_add, ":prosperity_factor", 75),#average 125, min 75, max 175          
          (store_random_in_range, ":last_arrived", 1, (24 * 7) + 1),
          (val_mul, ":last_arrived", -1),#some time in the last 7 days, plus or minus 40%
          (val_mul, ":last_arrived", 125),
          (val_div, ":last_arrived", ":prosperity_factor"),
          (party_set_slot, ":cur_village", dplmc_slot_village_trade_last_returned_from_market, ":last_arrived"),
          (store_random_in_range, ":last_arrived", 1, (24 * 7) + 1),
          (val_mul, ":last_arrived", -1),#some time in the last 7 days
          (val_mul, ":last_arrived", 125),
          (val_div, ":last_arrived", ":prosperity_factor"),
          (party_set_slot, ":cur_village", dplmc_slot_village_trade_last_arrived_to_market, ":last_arrived"),
      (try_end),
      ##diplomacy end+
      
      #do about 5 years' worth of political history (assuming 3 random checks a day)
      (try_for_range, ":unused", 0, 5000),
        (call_script, "script_cf_random_political_event"),
      (try_end),
      (assign, "$total_random_quarrel_changes", 0),
      (assign, "$total_relation_adds", 0),
      (assign, "$total_relation_subs", 0),
      
      (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
        (call_script, "script_evaluate_realm_stability", ":kingdom"),
        #(faction_set_slot, ":kingdom", slot_faction_last_feast_time, -264),
      (try_end),
      #Warband changes end
      
      (try_begin),
        (eq, "$cheat_mode", 1),
        (assign, reg3, "$cheat_mode"),
        (display_message, "@{!}DEBUG : Completed political events, cheat mode: {reg3}"),
      (try_end),
      
      #assign love interests to unmarried male lords
	  (try_for_range, ":cur_troop", lords_begin, lords_end),
	    (troop_slot_eq, ":cur_troop", slot_troop_spouse, -1),
##diplomacy start+ Also bypass this for characters that start with manually-assigned fiancees
       (troop_slot_eq, ":cur_troop", slot_troop_betrothed, -1),
##diplomacy end+
        (neg|is_between, ":cur_troop", kings_begin, kings_end),
        (neg|is_between, ":cur_troop", pretenders_begin, pretenders_end),
        
        (call_script, "script_assign_troop_love_interests", ":cur_troop"),
      (try_end),
      
      (store_random_in_range, "$romantic_attraction_seed", 0, 5),
      
      (try_begin),
        (eq, "$cheat_mode", 1),
        (assign, reg3, "$romantic_attraction_seed"),
        (display_message, "@{!}DEBUG : Assigned love interests. Attraction seed: {reg3}"),
      (try_end),
      
      #we need to spawn more bandits in warband, because map is bigger.
      #(try_for_range, ":unused", 0, 7),
      #  (call_script, "script_spawn_bandits"),
      #(try_end),
      
      #(set_spawn_radius, 50),
      #(try_for_range, ":unused", 0, 25),
      #  (spawn_around_party, "p_main_party", "pt_looters_e"),
      #(try_end),
      ##Floris MTT begin - moved to script_initialize_troop_tree_sets
      # (try_for_range, ":unused", 0, 10),
        # (call_script, "script_start_spawn_bandits"),  # CABA - this script no longer used, wasn't setting slots correctly
      # (try_end),
	  ##Floris MTT end
      
      #we are adding looter parties around each village with 1/5 probability.
      (set_spawn_radius, 5),
      (try_for_range, ":cur_village", villages_begin, villages_end),
        (store_random_in_range, ":random_value", 0, 5),
        (eq, ":random_value", 0),
        (spawn_around_party, ":cur_village", "pt_looters_e"),
      (try_end),
      
      (call_script, "script_update_town_specialists"),	#Floris STAT
      (call_script, "script_update_companion_candidates_in_taverns"),
      (call_script, "script_update_ransom_brokers"),
      (call_script, "script_update_tavern_travellers"),
      (call_script, "script_update_tavern_minstrels"),
      (call_script, "script_update_booksellers"),
      
      (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
        (call_script, "script_update_faction_notes", ":cur_kingdom"),
        (store_random_in_range, ":random_no", -60, 0),
        (faction_set_slot, ":faction_no", slot_faction_last_offensive_concluded, ":random_no"), ##1.132
        #		(faction_set_slot, ":faction_no", slot_faction_last_offensive_concluded, ":random_no"), ##1.131
      (try_end),
      
      (try_for_range, ":cur_troop", original_kingdom_heroes_begin, active_npcs_end),
        (call_script, "script_update_troop_notes", ":cur_troop"),
      (try_end),
      
      (try_for_range, ":cur_center", centers_begin, centers_end),
        ##diplomacy start+
        (party_get_slot, ":original_faction", ":center_no", slot_center_original_faction),
        (try_begin),
           #Assign plausible last-transfer-times to the contested centers based
           #on the "last offensive concluded" slot of the controlling faction.
           (is_between, ":original_faction", kingdoms_begin, kingdoms_end),
           (neg|party_slot_eq, ":center_no", slot_center_ex_faction, ":original_faction"),
           (faction_get_slot, reg0, ":original_faction", slot_faction_last_offensive_concluded),
           (party_set_slot, ":center_no", dplmc_slot_center_last_transfer_time, reg0),
        (try_end),
        (call_script, "script_update_center_notes", ":cur_center"),
      (try_end),
      
      (call_script, "script_update_troop_notes", "trp_player"),
      
      #Place kingdom ladies
      (try_for_range, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
		(call_script, "script_get_kingdom_lady_social_determinants", ":troop_id"),
		(troop_set_slot, ":troop_id", slot_troop_cur_center, reg1),
		##diplomacy start+
		#Set their original faction.
		(ge, reg0, 0),
		(troop_get_slot, ":original_faction", reg0, slot_troop_original_faction),
		(troop_set_slot, ":troop_id", slot_troop_original_faction, ":original_faction"),
		##diplomacy end+
	  (try_end),

	  ##diplomacy start+
	  ##Set initial relations between kingdom ladies and their relatives.
	  ##Do *not* initialize their relations with anyone they aren't related to:
	  ##that is used for courtship.
	  ##  The purpose of this initialization is so if a kingdom lady gets promoted,
	  ##her relations aren't a featureless slate.  Also, it would be interesting to
	  ##further develop the idea of ladies as pursuing agendas even if they aren't
	  ##leading warbands, which would benefit from giving them relations with other
	  ##people.
     (try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
		(troop_slot_eq, ":lady", slot_troop_occupation, slto_kingdom_lady),
		(troop_get_slot, ":lady_faction", ":lady", slot_troop_original_faction),

		(try_for_range, ":other_hero", heroes_begin, heroes_end),
		   (this_or_next|troop_slot_eq, ":other_hero", slot_troop_occupation, slto_kingdom_lady),
			(this_or_next|troop_slot_eq, ":other_hero", slot_troop_occupation, slto_kingdom_hero),
				(troop_slot_eq, ":other_hero", slot_troop_occupation, slto_inactive_pretender),
			(troop_slot_eq, ":other_hero", slot_troop_original_faction, ":lady_faction"),

			(neq, ":other_hero", ":lady"),
			(try_begin),
			   (this_or_next|troop_slot_eq, ":lady", slot_troop_spouse, ":other_hero"),
				   (troop_slot_eq, ":other_hero", slot_troop_spouse, ":lady"),
				(store_random_in_range, reg0, 0, 11),
			(else_try),				 
			   (call_script, "script_troop_get_family_relation_to_troop", ":lady", ":other_hero"),
			(try_end),
			(call_script, "script_troop_change_relation_with_troop", ":lady", ":other_hero", reg0),

			#This relation change only applies between kingdom ladies.
			(troop_slot_eq, ":other_hero", slot_troop_occupation, slto_kingdom_lady),
			(is_between, ":other_hero", kingdom_ladies_begin, kingdom_ladies_end),

			(store_random_in_range, ":random", 0, 11),
			(call_script, "script_troop_change_relation_with_troop", ":lady", ":other_hero", ":random"),
		(try_end),
	  (try_end),
	  ##diplomacy end+
      
      (try_begin),
        (eq, "$cheat_mode", 1),
        (assign, reg3, "$cheat_mode"),
        (display_message, "@{!}DEBUG : Located kingdom ladies, cheat mode: {reg3}"),
      (try_end),
      
      (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (call_script, "script_faction_recalculate_strength", ":faction_no"),
      (try_end),
      
      ##Floris: Removed this to make it savegame compatible.
      #	  (faction_set_slot, "fac_player_supporters_faction", slot_faction_adjective, "str_psf_adjective"),
      ##
      (faction_set_slot, "fac_kingdom_1", slot_faction_adjective, "str_kingdom_1_adjective"),
      (faction_set_slot, "fac_kingdom_2", slot_faction_adjective, "str_kingdom_2_adjective"),
      (faction_set_slot, "fac_kingdom_3", slot_faction_adjective, "str_kingdom_3_adjective"),
      (faction_set_slot, "fac_kingdom_4", slot_faction_adjective, "str_kingdom_4_adjective"),
      (faction_set_slot, "fac_kingdom_5", slot_faction_adjective, "str_kingdom_5_adjective"),
      (faction_set_slot, "fac_kingdom_6", slot_faction_adjective, "str_kingdom_6_adjective"),
      
      ##      (assign, "$players_kingdom", "fac_kingdom_1"),
      ##      (call_script, "script_give_center_to_lord", "p_town_7", "trp_player", 0),
      ##      (call_script, "script_give_center_to_lord", "p_town_16", "trp_player", 0),
      ####      (call_script, "script_give_center_to_lord", "p_castle_10", "trp_player", 0),
      ##      (assign, "$g_castle_requested_by_player", "p_castle_10"),
      (call_script, "script_get_player_party_morale_values"),
      (party_set_morale, "p_main_party", reg0),
      
      (troop_set_note_available, "trp_player", 1),
      
      (try_for_range, ":troop_no", kings_begin, kings_end),
        (troop_set_note_available, ":troop_no", 1),
      (try_end),
      
      (try_for_range, ":troop_no", lords_begin, lords_end),
        (troop_set_note_available, ":troop_no", 1),
      (try_end),
      
      (try_for_range, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
        (troop_set_note_available, ":troop_no", 1),
      (try_end),
      (troop_set_note_available, "trp_knight_1_1_wife", 0),
      
      (try_for_range, ":troop_no", pretenders_begin, pretenders_end),
        (troop_set_note_available, ":troop_no", 1),
      (try_end),
      
      #Lady and companion notes become available as you meet/recruit them
      
      (try_for_range, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
        (faction_set_note_available, ":faction_no", 1),
      (try_end),
      (faction_set_note_available, "fac_neutral", 0),
      
      (try_for_range, ":party_no", centers_begin, centers_end),
        (party_set_note_available, ":party_no", 1),
      (try_end),
	  
	  #Duh Town Population for Land required // Linked to bank system
	  
	  (try_for_range, ":town_no", towns_begin, towns_end),
		(this_or_next|eq,":town_no","p_town_1"),
		(this_or_next|eq,":town_no","p_town_5"),
		(this_or_next|eq,":town_no","p_town_6"),
		(this_or_next|eq,":town_no","p_town_8"),
		(this_or_next|eq,":town_no","p_town_10"),
		(eq,"$current_town","p_town_19"),
		(store_random_in_range, ":amount", 18000, 22000),
		(party_set_slot, ":town_no", slot_center_population, ":amount"),
		(val_div, ":amount", 200),
		(party_set_slot, ":town_no", slot_town_acres, ":amount"),
	  (else_try),
		(store_random_in_range, ":amount", 8000, 12000),
		(party_set_slot, ":town_no", slot_center_population, ":amount"),
		(val_div, ":amount", 200),
		(party_set_slot, ":town_no", slot_town_acres, ":amount"),		
	  (try_end),
	  
	  #Duh Over
    	  
      #TEMPERED    ADDED CALL TO SCRIPT TO INITIALIZE MODULE VARIABLES AND SLOTS
      (call_script, "script_init_temp_var"),
      #LAZERAS MODIFIED  {ENTK}
      # Jrider + TITLES v0.0, init new titles
      (try_for_range, ":troop_no", active_npcs_begin, kingdom_ladies_end),
        (store_troop_faction, ":faction_no", ":troop_no"),
        (call_script, "script_troop_set_title_according_to_faction", ":troop_no", ":faction_no"),
      (try_end),
      # Jrider 
      #LAZERAS MODIFIED  {ENTK}
	  # TPE+ 1.3 - Initialize TPE defaults - Windyplains
	  (call_script, "script_tpe_initialize_player_settings"),
	  # TPE- 

  ]),

  ##Floris MTT begin
  ("mtt_troop_slots",
							[
	###Mercenary
	##Native
	#Tier 1
	(troop_set_slot, troop_trees_0, slot_mercenary_townsman, "trp_mercenary_n_townsman"),
	(troop_set_slot, troop_trees_0, slot_mercenary_farmer, "trp_mercenary_n_farmer"),
	#Tier 2
	(troop_set_slot, troop_trees_0, slot_mercenary_miliz, "trp_mercenary_n_spiessknecht"),
	(troop_set_slot, troop_trees_0, slot_mercenary_spiessknecht, "trp_mercenary_n_spiessknecht"),
	(troop_set_slot, troop_trees_0, slot_mercenary_edelknecht, "trp_mercenary_n_spiessknecht"),
	(troop_set_slot, troop_trees_0, slot_mercenary_armbruster, "trp_mercenary_n_spiessknecht"),
	#Tier 3
	(troop_set_slot, troop_trees_0, slot_mercenary_brabanzon, "trp_mercenary_n_armbrust_soldner"),
	(troop_set_slot, troop_trees_0, slot_mercenary_armbrust_miliz, "trp_mercenary_n_armbrust_soldner"),
	(troop_set_slot, troop_trees_0, slot_mercenary_volksheer, "trp_mercenary_n_page"),
	(troop_set_slot, troop_trees_0, slot_mercenary_halberdier, "trp_mercenary_n_page"),
	(troop_set_slot, troop_trees_0, slot_mercenary_page, "trp_mercenary_n_page"),
	(troop_set_slot, troop_trees_0, slot_mercenary_armbrust_soldner, "trp_mercenary_n_armbrust_soldner"),
	(troop_set_slot, troop_trees_0, slot_mercenary_burger, "trp_mercenary_n_armbrust_soldner"),
	#Tier 4
	(troop_set_slot, troop_trees_0, slot_mercenary_doppelsoldner, "trp_mercenary_n_soldner"),
	(troop_set_slot, troop_trees_0, slot_mercenary_soldner, "trp_mercenary_n_soldner"),
	(troop_set_slot, troop_trees_0, slot_mercenary_reichslandser, "trp_mercenary_n_ritter"),
	(troop_set_slot, troop_trees_0, slot_mercenary_ritter, "trp_mercenary_n_ritter"),
	(troop_set_slot, troop_trees_0, slot_mercenary_armbrust_komtur, "trp_mercenary_n_soldner"),
	#Tier 5
	(troop_set_slot, troop_trees_0, slot_mercenary_kreuzritter, "trp_mercenary_n_komtur"),
	(troop_set_slot, troop_trees_0, slot_mercenary_komtur, "trp_mercenary_n_komtur"),
	(troop_set_slot, troop_trees_0, slot_mercenary_burgmann, "trp_mercenary_n_komtur_ritter"),
	(troop_set_slot, troop_trees_0, slot_mercenary_komtur_ritter, "trp_mercenary_n_komtur_ritter"),
	(troop_set_slot, troop_trees_0, slot_mercenary_ritterbroeder, "trp_mercenary_n_komtur"),
	#Tier 6
	(troop_set_slot, troop_trees_0, slot_mercenary_grosskomtur, "trp_mercenary_n_komtur"),
	(troop_set_slot, troop_trees_0, slot_mercenary_landsknecht, "trp_mercenary_n_komtur"),
	(troop_set_slot, troop_trees_0, slot_mercenary_hochmeister, "trp_mercenary_n_komtur_ritter"),
	#Extra
	(troop_set_slot, troop_trees_0, slot_mercenary_extra1, "trp_mercenary_n_extra1"),
	(troop_set_slot, troop_trees_0, slot_mercenary_extra2, "trp_mercenary_n_extra2"),
	(troop_set_slot, troop_trees_0, slot_mercenary_extra3, "trp_mercenary_n_extra3"),
	(troop_set_slot, troop_trees_0, slot_mercenary_extra4, "trp_mercenary_n_extra4"),
	(troop_set_slot, troop_trees_0, slot_mercenary_extra5, "trp_mercenary_n_extra5"),
	##Reworked
	#Tier 1
	(troop_set_slot, troop_trees_1, slot_mercenary_townsman, "trp_mercenary_r_townsman"),
	(troop_set_slot, troop_trees_1, slot_mercenary_farmer, "trp_mercenary_r_farmer"),
	#Tier 2
	(troop_set_slot, troop_trees_1, slot_mercenary_miliz, "trp_mercenary_r_spiessknecht"),
	(troop_set_slot, troop_trees_1, slot_mercenary_spiessknecht, "trp_mercenary_r_spiessknecht"),
	(troop_set_slot, troop_trees_1, slot_mercenary_edelknecht, "trp_mercenary_r_edelknecht"),
	(troop_set_slot, troop_trees_1, slot_mercenary_armbruster, "trp_mercenary_r_armbruster"),
	#Tier 3
	(troop_set_slot, troop_trees_1, slot_mercenary_brabanzon, "trp_mercenary_r_burger"),
	(troop_set_slot, troop_trees_1, slot_mercenary_armbrust_miliz, "trp_mercenary_r_armbrust_miliz"),
	(troop_set_slot, troop_trees_1, slot_mercenary_volksheer, "trp_mercenary_r_halberdier"),
	(troop_set_slot, troop_trees_1, slot_mercenary_halberdier, "trp_mercenary_r_halberdier"),
	(troop_set_slot, troop_trees_1, slot_mercenary_page, "trp_mercenary_r_page"),
	(troop_set_slot, troop_trees_1, slot_mercenary_armbrust_soldner, "trp_mercenary_r_armbrust_miliz"),
	(troop_set_slot, troop_trees_1, slot_mercenary_burger, "trp_mercenary_r_burger"),
	#Tier 4
	(troop_set_slot, troop_trees_1, slot_mercenary_doppelsoldner, "trp_mercenary_r_brabanzon"),
	(troop_set_slot, troop_trees_1, slot_mercenary_soldner, "trp_mercenary_r_brabanzon"),
	(troop_set_slot, troop_trees_1, slot_mercenary_reichslandser, "trp_mercenary_r_reichslandser"),
	(troop_set_slot, troop_trees_1, slot_mercenary_ritter, "trp_mercenary_r_ritter"),
	(troop_set_slot, troop_trees_1, slot_mercenary_armbrust_komtur, "trp_mercenary_r_armbrust_soldner"),
	#Tier 5
	(troop_set_slot, troop_trees_1, slot_mercenary_kreuzritter, "trp_mercenary_r_doppelsoldner"),
	(troop_set_slot, troop_trees_1, slot_mercenary_komtur, "trp_mercenary_r_doppelsoldner"),
	(troop_set_slot, troop_trees_1, slot_mercenary_burgmann, "trp_mercenary_r_burgmann"),
	(troop_set_slot, troop_trees_1, slot_mercenary_komtur_ritter, "trp_mercenary_r_komtur_ritter"),
	(troop_set_slot, troop_trees_1, slot_mercenary_ritterbroeder, "trp_mercenary_r_armbrust_komtur"),
	#Tier 6
	(troop_set_slot, troop_trees_1, slot_mercenary_grosskomtur, "trp_mercenary_r_doppelsoldner"),
	(troop_set_slot, troop_trees_1, slot_mercenary_landsknecht, "trp_mercenary_r_burgmann"),
	(troop_set_slot, troop_trees_1, slot_mercenary_hochmeister, "trp_mercenary_r_komtur_ritter"),
	#Extra
	(troop_set_slot, troop_trees_1, slot_mercenary_extra1, "trp_mercenary_r_extra1"),
	(troop_set_slot, troop_trees_1, slot_mercenary_extra2, "trp_mercenary_r_extra2"),
	(troop_set_slot, troop_trees_1, slot_mercenary_extra3, "trp_mercenary_r_extra3"),
	(troop_set_slot, troop_trees_1, slot_mercenary_extra4, "trp_mercenary_r_extra4"),
	(troop_set_slot, troop_trees_1, slot_mercenary_extra5, "trp_mercenary_r_extra5"),
	##Expanded
	#Tier 1
	(troop_set_slot, troop_trees_2, slot_mercenary_townsman, "trp_mercenary_e_townsman"),
	(troop_set_slot, troop_trees_2, slot_mercenary_farmer, "trp_mercenary_e_farmer"),
	#Tier 2
	(troop_set_slot, troop_trees_2, slot_mercenary_miliz, "trp_mercenary_e_miliz"),
	(troop_set_slot, troop_trees_2, slot_mercenary_spiessknecht, "trp_mercenary_e_spiessknecht"),
	(troop_set_slot, troop_trees_2, slot_mercenary_edelknecht, "trp_mercenary_e_edelknecht"),
	(troop_set_slot, troop_trees_2, slot_mercenary_armbruster, "trp_mercenary_e_armbruster"),
	#Tier 3
	(troop_set_slot, troop_trees_2, slot_mercenary_brabanzon, "trp_mercenary_e_brabanzon"),
	(troop_set_slot, troop_trees_2, slot_mercenary_armbrust_miliz, "trp_mercenary_e_armbrust_miliz"),
	(troop_set_slot, troop_trees_2, slot_mercenary_volksheer, "trp_mercenary_e_volksheer"),
	(troop_set_slot, troop_trees_2, slot_mercenary_halberdier, "trp_mercenary_e_halberdier"),
	(troop_set_slot, troop_trees_2, slot_mercenary_page, "trp_mercenary_e_page"),
	(troop_set_slot, troop_trees_2, slot_mercenary_armbrust_soldner, "trp_mercenary_e_armbrust_soldner"),
	(troop_set_slot, troop_trees_2, slot_mercenary_burger, "trp_mercenary_e_burger"),
	#Tier 4
	(troop_set_slot, troop_trees_2, slot_mercenary_ritterbroeder, "trp_mercenary_e_ritterbroeder"),
	(troop_set_slot, troop_trees_2, slot_mercenary_soldner, "trp_mercenary_e_soldner"),
	(troop_set_slot, troop_trees_2, slot_mercenary_reichslandser, "trp_mercenary_e_reichslandser"),
	(troop_set_slot, troop_trees_2, slot_mercenary_ritter, "trp_mercenary_e_ritter"),
	(troop_set_slot, troop_trees_2, slot_mercenary_armbrust_komtur, "trp_mercenary_e_armbrust_komtur"),
	#Tier 5
	(troop_set_slot, troop_trees_2, slot_mercenary_kreuzritter, "trp_mercenary_e_kreuzritter"),
	(troop_set_slot, troop_trees_2, slot_mercenary_komtur, "trp_mercenary_e_komtur"),
	(troop_set_slot, troop_trees_2, slot_mercenary_burgmann, "trp_mercenary_e_burgmann"),
	(troop_set_slot, troop_trees_2, slot_mercenary_komtur_ritter, "trp_mercenary_e_komtur_ritter"),
	(troop_set_slot, troop_trees_2, slot_mercenary_doppelsoldner, "trp_mercenary_e_doppelsoldner"),
	#Tier 6
	(troop_set_slot, troop_trees_2, slot_mercenary_grosskomtur, "trp_mercenary_e_grosskomtur"),
	(troop_set_slot, troop_trees_2, slot_mercenary_landsknecht, "trp_mercenary_e_landsknecht"),
	(troop_set_slot, troop_trees_2, slot_mercenary_hochmeister, "trp_mercenary_e_hochmeister"),
	#Extra
	(troop_set_slot, troop_trees_2, slot_mercenary_extra1, "trp_mercenary_e_extra1"),
	(troop_set_slot, troop_trees_2, slot_mercenary_extra2, "trp_mercenary_e_extra2"),
	(troop_set_slot, troop_trees_2, slot_mercenary_extra3, "trp_mercenary_e_extra3"),
	(troop_set_slot, troop_trees_2, slot_mercenary_extra4, "trp_mercenary_e_extra4"),
	(troop_set_slot, troop_trees_2, slot_mercenary_extra5, "trp_mercenary_e_extra5"),
	###Swadian
	##Native
	#Tier 1
	(troop_set_slot, troop_trees_0, slot_swadian_peasant, "trp_swadian_n_peasant"),
	#Tier 2
	(troop_set_slot, troop_trees_0, slot_swadian_militia, "trp_swadian_n_militia"),
	(troop_set_slot, troop_trees_0, slot_swadian_peasant_archer, "trp_swadian_n_militia"),
	#Tier 3
	(troop_set_slot, troop_trees_0, slot_swadian_vougier, "trp_swadian_n_page"),
	(troop_set_slot, troop_trees_0, slot_swadian_page, "trp_swadian_n_page"),
	(troop_set_slot, troop_trees_0, slot_swadian_sergeant_at_arms, "trp_swadian_n_archer_militia"),
	(troop_set_slot, troop_trees_0, slot_swadian_archer_militia, "trp_swadian_n_archer_militia"),
	#Tier 4
	(troop_set_slot, troop_trees_0, slot_swadian_piquier, "trp_swadian_n_ecuyer"),
	(troop_set_slot, troop_trees_0, slot_swadian_ecuyer, "trp_swadian_n_ecuyer"),
	(troop_set_slot, troop_trees_0, slot_swadian_jacobite, "trp_swadian_n_jacobite"),
	(troop_set_slot, troop_trees_0, slot_swadian_guard, "trp_swadian_n_jacobite"),
	(troop_set_slot, troop_trees_0, slot_swadian_longbowman, "trp_swadian_n_longbowman"),
	(troop_set_slot, troop_trees_0, slot_swadian_tracker, "trp_swadian_n_longbowman"),
	#Tier 5
	(troop_set_slot, troop_trees_0, slot_swadian_chevalier, "trp_swadian_n_chevalier"),
	(troop_set_slot, troop_trees_0, slot_swadian_hobilar, "trp_swadian_n_chevalier"),
	(troop_set_slot, troop_trees_0, slot_swadian_jock, "trp_swadian_n_jock"),
	(troop_set_slot, troop_trees_0, slot_swadian_man_at_arms, "trp_swadian_n_jock"),
	(troop_set_slot, troop_trees_0, slot_swadian_sheriff, "trp_swadian_n_jock"),
	(troop_set_slot, troop_trees_0, slot_swadian_selfbow_archer, "trp_swadian_n_selfbow_archer"),
	(troop_set_slot, troop_trees_0, slot_swadian_skirmisher, "trp_swadian_n_selfbow_archer"),
	#Tier 6
	(troop_set_slot, troop_trees_0, slot_swadian_chevalier_banneret, "trp_swadian_n_chevalier"),
	(troop_set_slot, troop_trees_0, slot_swadian_highlander, "trp_swadian_n_jock"),
	(troop_set_slot, troop_trees_0, slot_swadian_lancer, "trp_swadian_n_chevalier"),
	(troop_set_slot, troop_trees_0, slot_swadian_yeoman_archer, "trp_swadian_n_selfbow_archer"),
	#Tier 7
	(troop_set_slot, troop_trees_0, slot_swadian_baron_mineures, "trp_swadian_n_chevalier"),
	(troop_set_slot, troop_trees_0, slot_swadian_retinue_longbowman, "trp_swadian_n_selfbow_archer"),
	#Extra
	(troop_set_slot, troop_trees_0, slot_swadian_extra1, "trp_swadian_n_extra1"),
	(troop_set_slot, troop_trees_0, slot_swadian_extra2, "trp_swadian_n_extra2"),
	(troop_set_slot, troop_trees_0, slot_swadian_extra3, "trp_swadian_n_extra3"),
	(troop_set_slot, troop_trees_0, slot_swadian_extra4, "trp_swadian_n_extra4"),
	(troop_set_slot, troop_trees_0, slot_swadian_extra5, "trp_swadian_n_extra5"),
	##Reworked
	#Tier 1
	(troop_set_slot, troop_trees_1, slot_swadian_peasant, "trp_swadian_r_peasant"),
	#Tier 2
	(troop_set_slot, troop_trees_1, slot_swadian_militia, "trp_swadian_r_militia"),
	(troop_set_slot, troop_trees_1, slot_swadian_peasant_archer, "trp_swadian_r_peasant_archer"),
	#Tier 3
	(troop_set_slot, troop_trees_1, slot_swadian_vougier, "trp_swadian_r_sergeant_at_arms"),
	(troop_set_slot, troop_trees_1, slot_swadian_page, "trp_swadian_r_page"),
	(troop_set_slot, troop_trees_1, slot_swadian_sergeant_at_arms, "trp_swadian_r_sergeant_at_arms"),
	(troop_set_slot, troop_trees_1, slot_swadian_archer_militia, "trp_swadian_r_archer_militia"),
	#Tier 4
	(troop_set_slot, troop_trees_1, slot_swadian_piquier, "trp_swadian_r_piquier"),
	(troop_set_slot, troop_trees_1, slot_swadian_ecuyer, "trp_swadian_r_ecuyer"),
	(troop_set_slot, troop_trees_1, slot_swadian_jacobite, "trp_swadian_r_jacobite"),
	(troop_set_slot, troop_trees_1, slot_swadian_guard, "trp_swadian_r_hobilar"),
	(troop_set_slot, troop_trees_1, slot_swadian_longbowman, "trp_swadian_r_longbowman"),
	(troop_set_slot, troop_trees_1, slot_swadian_tracker, "trp_swadian_r_longbowman"),
	#Tier 5
	(troop_set_slot, troop_trees_1, slot_swadian_chevalier, "trp_swadian_r_chevalier"),
	(troop_set_slot, troop_trees_1, slot_swadian_hobilar, "trp_swadian_r_chevalier"),
	(troop_set_slot, troop_trees_1, slot_swadian_jock, "trp_swadian_r_jock"),
	(troop_set_slot, troop_trees_1, slot_swadian_man_at_arms, "trp_swadian_r_jock"),
	(troop_set_slot, troop_trees_1, slot_swadian_sheriff, "trp_swadian_r_jock"),
	(troop_set_slot, troop_trees_1, slot_swadian_selfbow_archer, "trp_swadian_r_selfbow_archer"),
	(troop_set_slot, troop_trees_1, slot_swadian_skirmisher, "trp_swadian_r_selfbow_archer"),
	#Tier 6
	(troop_set_slot, troop_trees_1, slot_swadian_chevalier_banneret, "trp_swadian_r_chevalier_banneret"),
	(troop_set_slot, troop_trees_1, slot_swadian_highlander, "trp_swadian_r_jock"),
	(troop_set_slot, troop_trees_1, slot_swadian_lancer, "trp_swadian_r_chevalier_banneret"),
	(troop_set_slot, troop_trees_1, slot_swadian_yeoman_archer, "trp_swadian_r_selfbow_archer"),
	#Tier 7
	(troop_set_slot, troop_trees_1, slot_swadian_baron_mineures, "trp_swadian_r_chevalier_banneret"),
	(troop_set_slot, troop_trees_1, slot_swadian_retinue_longbowman, "trp_swadian_r_selfbow_archer"),
	#Extra
	(troop_set_slot, troop_trees_1, slot_swadian_extra1, "trp_swadian_r_extra1"),
	(troop_set_slot, troop_trees_1, slot_swadian_extra2, "trp_swadian_r_extra2"),
	(troop_set_slot, troop_trees_1, slot_swadian_extra3, "trp_swadian_r_extra3"),
	(troop_set_slot, troop_trees_1, slot_swadian_extra4, "trp_swadian_r_extra4"),
	(troop_set_slot, troop_trees_1, slot_swadian_extra5, "trp_swadian_r_extra5"),
	##Expanded
	#Tier 1
	(troop_set_slot, troop_trees_2, slot_swadian_peasant, "trp_swadian_e_peasant"),
	#Tier 2
	(troop_set_slot, troop_trees_2, slot_swadian_militia, "trp_swadian_e_militia"),
	(troop_set_slot, troop_trees_2, slot_swadian_peasant_archer, "trp_swadian_e_peasant_archer"),
	#Tier 3
	(troop_set_slot, troop_trees_2, slot_swadian_vougier, "trp_swadian_e_vougier"),
	(troop_set_slot, troop_trees_2, slot_swadian_page, "trp_swadian_e_page"),
	(troop_set_slot, troop_trees_2, slot_swadian_sergeant_at_arms, "trp_swadian_e_sergeant_at_arms"),
	(troop_set_slot, troop_trees_2, slot_swadian_archer_militia, "trp_swadian_e_archer_militia"),
	#Tier 4
	(troop_set_slot, troop_trees_2, slot_swadian_piquier, "trp_swadian_e_piquier"),
	(troop_set_slot, troop_trees_2, slot_swadian_ecuyer, "trp_swadian_e_ecuyer"),
	(troop_set_slot, troop_trees_2, slot_swadian_jacobite, "trp_swadian_e_jacobite"),
	(troop_set_slot, troop_trees_2, slot_swadian_guard, "trp_swadian_e_guard"),
	(troop_set_slot, troop_trees_2, slot_swadian_longbowman, "trp_swadian_e_longbowman"),
	(troop_set_slot, troop_trees_2, slot_swadian_tracker, "trp_swadian_e_tracker"),
	#Tier 5
	(troop_set_slot, troop_trees_2, slot_swadian_chevalier, "trp_swadian_e_chevalier"),
	(troop_set_slot, troop_trees_2, slot_swadian_hobilar, "trp_swadian_e_hobilar"),
	(troop_set_slot, troop_trees_2, slot_swadian_jock, "trp_swadian_e_jock"),
	(troop_set_slot, troop_trees_2, slot_swadian_man_at_arms, "trp_swadian_e_man_at_arms"),
	(troop_set_slot, troop_trees_2, slot_swadian_sheriff, "trp_swadian_e_sheriff"),
	(troop_set_slot, troop_trees_2, slot_swadian_selfbow_archer, "trp_swadian_e_selfbow_archer"),
	(troop_set_slot, troop_trees_2, slot_swadian_skirmisher, "trp_swadian_e_skirmisher"),
	#Tier 6
	(troop_set_slot, troop_trees_2, slot_swadian_chevalier_banneret, "trp_swadian_e_chevalier_banneret"),
	(troop_set_slot, troop_trees_2, slot_swadian_highlander, "trp_swadian_e_highlander"),
	(troop_set_slot, troop_trees_2, slot_swadian_lancer, "trp_swadian_e_lancer"),
	(troop_set_slot, troop_trees_2, slot_swadian_yeoman_archer, "trp_swadian_e_yeoman_archer"),
	#Tier 7
	(troop_set_slot, troop_trees_2, slot_swadian_baron_mineures, "trp_swadian_e_baron_mineures"),
	(troop_set_slot, troop_trees_2, slot_swadian_retinue_longbowman, "trp_swadian_e_retinue_longbowman"),
	#Extra
	(troop_set_slot, troop_trees_2, slot_swadian_extra1, "trp_swadian_e_extra1"),
	(troop_set_slot, troop_trees_2, slot_swadian_extra2, "trp_swadian_e_extra2"),
	(troop_set_slot, troop_trees_2, slot_swadian_extra3, "trp_swadian_e_extra3"),
	(troop_set_slot, troop_trees_2, slot_swadian_extra4, "trp_swadian_e_extra4"),
	(troop_set_slot, troop_trees_2, slot_swadian_extra5, "trp_swadian_e_extra5"),
	###Vaegir
	##Native
	#Tier 1
	(troop_set_slot, troop_trees_0, slot_vaegir_kholop, "trp_vaegir_n_kholop"),
	#Tier 2
	(troop_set_slot, troop_trees_0, slot_vaegir_otrok, "trp_vaegir_n_otrok"),
	(troop_set_slot, troop_trees_0, slot_vaegir_pasynok, "trp_vaegir_n_otrok"),
	#Tier 3
	(troop_set_slot, troop_trees_0, slot_vaegir_kazak, "trp_vaegir_n_kazak"),
	(troop_set_slot, troop_trees_0, slot_vaegir_kmet, "trp_vaegir_n_kmet"),
	(troop_set_slot, troop_trees_0, slot_vaegir_grid, "trp_vaegir_n_kmet"),
	#Tier 4
	(troop_set_slot, troop_trees_0, slot_vaegir_yesaul, "trp_vaegir_n_yesaul"),
	(troop_set_slot, troop_trees_0, slot_vaegir_plastun, "trp_vaegir_n_plastun"),
	(troop_set_slot, troop_trees_0, slot_vaegir_ratnik, "trp_vaegir_n_yesaul"),
	(troop_set_slot, troop_trees_0, slot_vaegir_zalstrelshik, "trp_vaegir_n_zalstrelshik"),
	(troop_set_slot, troop_trees_0, slot_vaegir_mladshiy_druzhinnik, "trp_vaegir_n_plastun"),
	(troop_set_slot, troop_trees_0, slot_vaegir_poztoma_druzhinaik, "trp_vaegir_n_zalstrelshik"),
	#Tier 5
	(troop_set_slot, troop_trees_0, slot_vaegir_ataman, "trp_vaegir_n_pansirniy_kazan"),
	(troop_set_slot, troop_trees_0, slot_vaegir_pansirniy_kazan, "trp_vaegir_n_pansirniy_kazan"),
	(troop_set_slot, troop_trees_0, slot_vaegir_posadnik, "trp_vaegir_n_luchnik"),
	(troop_set_slot, troop_trees_0, slot_vaegir_golova, "trp_vaegir_n_luchnik"),
	(troop_set_slot, troop_trees_0, slot_vaegir_luchnik, "trp_vaegir_n_luchnik"),
	(troop_set_slot, troop_trees_0, slot_vaegir_druzhinnik, "trp_vaegir_n_druzhinnik_veteran"),
	(troop_set_slot, troop_trees_0, slot_vaegir_druzhinnik_veteran, "trp_vaegir_n_druzhinnik_veteran"),
	#Tier 6
	(troop_set_slot, troop_trees_0, slot_vaegir_legkoy_vityas, "trp_vaegir_n_pansirniy_kazan"),
	(troop_set_slot, troop_trees_0, slot_vaegir_vityas, "trp_vaegir_n_pansirniy_kazan"),
	(troop_set_slot, troop_trees_0, slot_vaegir_voevoda, "trp_vaegir_n_luchnik"),
	(troop_set_slot, troop_trees_0, slot_vaegir_metkiy_luchnik, "trp_vaegir_n_luchnik"),
	(troop_set_slot, troop_trees_0, slot_vaegir_elitniy_druzhinnik, "trp_vaegir_n_druzhinnik_veteran"),
	#Tier 7
	(troop_set_slot, troop_trees_0, slot_vaegir_bogatyr, "trp_vaegir_n_pansirniy_kazan"),
	(troop_set_slot, troop_trees_0, slot_vaegir_sokoliniy_glaz, "trp_vaegir_n_druzhinnik_veteran"),
	#Extra
	(troop_set_slot, troop_trees_0, slot_vaegir_extra1, "trp_vaegir_n_extra1"),
	(troop_set_slot, troop_trees_0, slot_vaegir_extra2, "trp_vaegir_n_extra2"),
	(troop_set_slot, troop_trees_0, slot_vaegir_extra3, "trp_vaegir_n_extra3"),
	(troop_set_slot, troop_trees_0, slot_vaegir_extra4, "trp_vaegir_n_extra4"),
	(troop_set_slot, troop_trees_0, slot_vaegir_extra5, "trp_vaegir_n_extra5"),
	##Reworked
	#Tier 1
	(troop_set_slot, troop_trees_1, slot_vaegir_kholop, "trp_vaegir_r_kholop"),
	#Tier 2
	(troop_set_slot, troop_trees_1, slot_vaegir_otrok, "trp_vaegir_r_otrok"),
	(troop_set_slot, troop_trees_1, slot_vaegir_pasynok, "trp_vaegir_r_pasynok"),
	#Tier 3
	(troop_set_slot, troop_trees_1, slot_vaegir_kazak, "trp_vaegir_r_kazak"),
	(troop_set_slot, troop_trees_1, slot_vaegir_kmet, "trp_vaegir_r_kmet"),
	(troop_set_slot, troop_trees_1, slot_vaegir_grid, "trp_vaegir_r_grid"),
	#Tier 4
	(troop_set_slot, troop_trees_1, slot_vaegir_yesaul, "trp_vaegir_r_yesaul"),
	(troop_set_slot, troop_trees_1, slot_vaegir_plastun, "trp_vaegir_r_plastun"),
	(troop_set_slot, troop_trees_1, slot_vaegir_ratnik, "trp_vaegir_r_ratnik"),
	(troop_set_slot, troop_trees_1, slot_vaegir_zalstrelshik, "trp_vaegir_r_zalstrelshik"),
	(troop_set_slot, troop_trees_1, slot_vaegir_mladshiy_druzhinnik, "trp_vaegir_r_mladshiy_druzhinnik"),
	(troop_set_slot, troop_trees_1, slot_vaegir_poztoma_druzhinaik, "trp_vaegir_r_mladshiy_druzhinnik"),
	#Tier 5
	(troop_set_slot, troop_trees_1, slot_vaegir_ataman, "trp_vaegir_r_ataman"),
	(troop_set_slot, troop_trees_1, slot_vaegir_pansirniy_kazan, "trp_vaegir_r_ataman"),
	(troop_set_slot, troop_trees_1, slot_vaegir_posadnik, "trp_vaegir_r_luchnik"),
	(troop_set_slot, troop_trees_1, slot_vaegir_golova, "trp_vaegir_r_luchnik"),
	(troop_set_slot, troop_trees_1, slot_vaegir_luchnik, "trp_vaegir_r_luchnik"),
	(troop_set_slot, troop_trees_1, slot_vaegir_druzhinnik, "trp_vaegir_r_druzhinnik_veteran"),
	(troop_set_slot, troop_trees_1, slot_vaegir_druzhinnik_veteran, "trp_vaegir_r_druzhinnik_veteran"),
	#Tier 6
	(troop_set_slot, troop_trees_1, slot_vaegir_legkoy_vityas, "trp_vaegir_r_ataman"),
	(troop_set_slot, troop_trees_1, slot_vaegir_vityas, "trp_vaegir_r_luchnik"),
	(troop_set_slot, troop_trees_1, slot_vaegir_voevoda, "trp_vaegir_r_luchnik"),
	(troop_set_slot, troop_trees_1, slot_vaegir_metkiy_luchnik, "trp_vaegir_r_metkiy_luchnik"),
	(troop_set_slot, troop_trees_1, slot_vaegir_elitniy_druzhinnik, "trp_vaegir_r_druzhinnik_veteran"),
	#Tier 7
	(troop_set_slot, troop_trees_1, slot_vaegir_bogatyr, "trp_vaegir_r_ataman"),
	(troop_set_slot, troop_trees_1, slot_vaegir_sokoliniy_glaz, "trp_vaegir_r_metkiy_luchnik"),
	#Extra
	(troop_set_slot, troop_trees_1, slot_vaegir_extra1, "trp_vaegir_r_extra1"),
	(troop_set_slot, troop_trees_1, slot_vaegir_extra2, "trp_vaegir_r_extra2"),
	(troop_set_slot, troop_trees_1, slot_vaegir_extra3, "trp_vaegir_r_extra3"),
	(troop_set_slot, troop_trees_1, slot_vaegir_extra4, "trp_vaegir_r_extra4"),
	(troop_set_slot, troop_trees_1, slot_vaegir_extra5, "trp_vaegir_r_extra5"),
	##Expanded
	#Tier 1
	(troop_set_slot, troop_trees_2, slot_vaegir_kholop, "trp_vaegir_e_kholop"),
	#Tier 2
	(troop_set_slot, troop_trees_2, slot_vaegir_otrok, "trp_vaegir_e_otrok"),
	(troop_set_slot, troop_trees_2, slot_vaegir_pasynok, "trp_vaegir_e_pasynok"),
	#Tier 3
	(troop_set_slot, troop_trees_2, slot_vaegir_kazak, "trp_vaegir_e_kazak"),
	(troop_set_slot, troop_trees_2, slot_vaegir_kmet, "trp_vaegir_e_kmet"),
	(troop_set_slot, troop_trees_2, slot_vaegir_grid, "trp_vaegir_e_grid"),
	#Tier 4
	(troop_set_slot, troop_trees_2, slot_vaegir_yesaul, "trp_vaegir_e_yesaul"),
	(troop_set_slot, troop_trees_2, slot_vaegir_plastun, "trp_vaegir_e_plastun"),
	(troop_set_slot, troop_trees_2, slot_vaegir_ratnik, "trp_vaegir_e_ratnik"),
	(troop_set_slot, troop_trees_2, slot_vaegir_zalstrelshik, "trp_vaegir_e_zalstrelshik"),
	(troop_set_slot, troop_trees_2, slot_vaegir_mladshiy_druzhinnik, "trp_vaegir_e_mladshiy_druzhinnik"),
	(troop_set_slot, troop_trees_2, slot_vaegir_poztoma_druzhinaik, "trp_vaegir_e_poztoma_druzhinaik"),
	#Tier 5
	(troop_set_slot, troop_trees_2, slot_vaegir_ataman, "trp_vaegir_e_ataman"),
	(troop_set_slot, troop_trees_2, slot_vaegir_pansirniy_kazan, "trp_vaegir_e_pansirniy_kazan"),
	(troop_set_slot, troop_trees_2, slot_vaegir_posadnik, "trp_vaegir_e_posadnik"),
	(troop_set_slot, troop_trees_2, slot_vaegir_golova, "trp_vaegir_e_golova"),
	(troop_set_slot, troop_trees_2, slot_vaegir_luchnik, "trp_vaegir_e_luchnik"),
	(troop_set_slot, troop_trees_2, slot_vaegir_druzhinnik, "trp_vaegir_e_druzhinnik"),
	(troop_set_slot, troop_trees_2, slot_vaegir_druzhinnik_veteran, "trp_vaegir_e_druzhinnik_veteran"),
	#Tier 6
	(troop_set_slot, troop_trees_2, slot_vaegir_legkoy_vityas, "trp_vaegir_e_legkoy_vityas"),
	(troop_set_slot, troop_trees_2, slot_vaegir_vityas, "trp_vaegir_e_vityas"),
	(troop_set_slot, troop_trees_2, slot_vaegir_voevoda, "trp_vaegir_e_voevoda"),
	(troop_set_slot, troop_trees_2, slot_vaegir_metkiy_luchnik, "trp_vaegir_e_metkiy_luchnik"),
	(troop_set_slot, troop_trees_2, slot_vaegir_elitniy_druzhinnik, "trp_vaegir_e_elitniy_druzhinnik"),
	#Tier 7
	(troop_set_slot, troop_trees_2, slot_vaegir_bogatyr, "trp_vaegir_e_bogatyr"),
	(troop_set_slot, troop_trees_2, slot_vaegir_sokoliniy_glaz, "trp_vaegir_e_sokoliniy_glaz"),
	#Extra
	(troop_set_slot, troop_trees_2, slot_vaegir_extra1, "trp_vaegir_e_extra1"),
	(troop_set_slot, troop_trees_2, slot_vaegir_extra2, "trp_vaegir_e_extra2"),
	(troop_set_slot, troop_trees_2, slot_vaegir_extra3, "trp_vaegir_e_extra3"),
	(troop_set_slot, troop_trees_2, slot_vaegir_extra4, "trp_vaegir_e_extra4"),
	(troop_set_slot, troop_trees_2, slot_vaegir_extra5, "trp_vaegir_e_extra5"),
	###Khergit
	##Native
	#Tier 1
	(troop_set_slot, troop_trees_0, slot_khergit_tariachin, "trp_khergit_n_tariachin"),
	#Tier 2
	(troop_set_slot, troop_trees_0, slot_khergit_tsereg, "trp_khergit_n_qarbughaci"),
	(troop_set_slot, troop_trees_0, slot_khergit_qarbughaci, "trp_khergit_n_qarbughaci"),
	#Tier 3
	(troop_set_slot, troop_trees_0, slot_khergit_morici, "trp_khergit_n_morici"),
	(troop_set_slot, troop_trees_0, slot_khergit_asud, "trp_khergit_n_morici"),
	(troop_set_slot, troop_trees_0, slot_khergit_surcin, "trp_khergit_n_morici"),
	(troop_set_slot, troop_trees_0, slot_khergit_abaci, "trp_khergit_n_morici"),
	#Tier 4
	(troop_set_slot, troop_trees_0, slot_khergit_yabagharu_morici, "trp_khergit_n_kipchak"),
	(troop_set_slot, troop_trees_0, slot_khergit_kipchak, "trp_khergit_n_kipchak"),
	(troop_set_slot, troop_trees_0, slot_khergit_quaqli, "trp_khergit_n_kipchak"),
	(troop_set_slot, troop_trees_0, slot_khergit_aqala_asud, "trp_khergit_n_qubuci"),
	(troop_set_slot, troop_trees_0, slot_khergit_aqala_surcin, "trp_khergit_n_qubuci"),
	(troop_set_slot, troop_trees_0, slot_khergit_teriguci, "trp_khergit_n_qubuci"),
	(troop_set_slot, troop_trees_0, slot_khergit_qubuci, "trp_khergit_n_qubuci"),
	#Tier 5
	(troop_set_slot, troop_trees_0, slot_khergit_torguu, "trp_khergit_n_borjigin"),
	(troop_set_slot, troop_trees_0, slot_khergit_khevtuul, "trp_khergit_n_borjigin"),
	(troop_set_slot, troop_trees_0, slot_khergit_numici, "trp_khergit_n_borjigin"),
	(troop_set_slot, troop_trees_0, slot_khergit_aqala_teriguci, "trp_khergit_n_borjigin"),
	(troop_set_slot, troop_trees_0, slot_khergit_borjigin, "trp_khergit_n_borjigin"),
	(troop_set_slot, troop_trees_0, slot_khergit_numyn_ad, "trp_khergit_n_borjigin"),
	#Tier 6
	(troop_set_slot, troop_trees_0, slot_khergit_khorchen, "trp_khergit_n_borjigin"),
	(troop_set_slot, troop_trees_0, slot_khergit_keshig, "trp_khergit_n_borjigin"),
	(troop_set_slot, troop_trees_0, slot_khergit_kharvaach, "trp_khergit_n_borjigin"),
	(troop_set_slot, troop_trees_0, slot_khergit_jurtchi, "trp_khergit_n_borjigin"),
	(troop_set_slot, troop_trees_0, slot_khergit_aqata_borjigin, "trp_khergit_n_borjigin"),
	#Tier 7
	(troop_set_slot, troop_trees_0, slot_khergit_cherbi, "trp_khergit_n_borjigin"),
	(troop_set_slot, troop_trees_0, slot_khergit_mandugai, "trp_khergit_n_borjigin"),
	#Extra
	(troop_set_slot, troop_trees_0, slot_khergit_extra1, "trp_khergit_n_extra1"),
	(troop_set_slot, troop_trees_0, slot_khergit_extra2, "trp_khergit_n_extra2"),
	(troop_set_slot, troop_trees_0, slot_khergit_extra3, "trp_khergit_n_extra3"),
	(troop_set_slot, troop_trees_0, slot_khergit_extra4, "trp_khergit_n_extra4"),
	(troop_set_slot, troop_trees_0, slot_khergit_extra5, "trp_khergit_n_extra5"),
	##Reworked
	#Tier 1
	(troop_set_slot, troop_trees_1, slot_khergit_tariachin, "trp_khergit_r_tariachin"),
	#Tier 2
	(troop_set_slot, troop_trees_1, slot_khergit_tsereg, "trp_khergit_r_tsereg"),
	(troop_set_slot, troop_trees_1, slot_khergit_qarbughaci, "trp_khergit_r_qarbughaci"),
	#Tier 3
	(troop_set_slot, troop_trees_1, slot_khergit_morici, "trp_khergit_r_morici"),
	(troop_set_slot, troop_trees_1, slot_khergit_asud, "trp_khergit_r_asud"),
	(troop_set_slot, troop_trees_1, slot_khergit_surcin, "trp_khergit_r_asud"),
	(troop_set_slot, troop_trees_1, slot_khergit_abaci, "trp_khergit_r_abaci"),
	#Tier 4
	(troop_set_slot, troop_trees_1, slot_khergit_yabagharu_morici, "trp_khergit_r_kipchak"),
	(troop_set_slot, troop_trees_1, slot_khergit_kipchak, "trp_khergit_r_kipchak"),
	(troop_set_slot, troop_trees_1, slot_khergit_quaqli, "trp_khergit_r_quaqli"),
	(troop_set_slot, troop_trees_1, slot_khergit_aqala_asud, "trp_khergit_r_aqala_asud"),
	(troop_set_slot, troop_trees_1, slot_khergit_aqala_surcin, "trp_khergit_r_aqala_asud"),
	(troop_set_slot, troop_trees_1, slot_khergit_teriguci, "trp_khergit_r_teriguci"),
	(troop_set_slot, troop_trees_1, slot_khergit_qubuci, "trp_khergit_r_qubuci"),
	#Tier 5
	(troop_set_slot, troop_trees_1, slot_khergit_torguu, "trp_khergit_r_khevtuul"),
	(troop_set_slot, troop_trees_1, slot_khergit_khevtuul, "trp_khergit_r_khevtuul"),
	(troop_set_slot, troop_trees_1, slot_khergit_numici, "trp_khergit_r_aqala_teriguci"),
	(troop_set_slot, troop_trees_1, slot_khergit_aqala_teriguci, "trp_khergit_r_aqala_teriguci"),
	(troop_set_slot, troop_trees_1, slot_khergit_borjigin, "trp_khergit_r_borjigin"),
	(troop_set_slot, troop_trees_1, slot_khergit_numyn_ad, "trp_khergit_r_borjigin"),
	#Tier 6
	(troop_set_slot, troop_trees_1, slot_khergit_khorchen, "trp_khergit_r_khevtuul"),
	(troop_set_slot, troop_trees_1, slot_khergit_keshig, "trp_khergit_r_keshig"),
	(troop_set_slot, troop_trees_1, slot_khergit_kharvaach, "trp_khergit_r_aqala_teriguci"),
	(troop_set_slot, troop_trees_1, slot_khergit_jurtchi, "trp_khergit_r_aqala_teriguci"),
	(troop_set_slot, troop_trees_1, slot_khergit_aqata_borjigin, "trp_khergit_r_borjigin"),
	#Tier 7
	(troop_set_slot, troop_trees_1, slot_khergit_cherbi, "trp_khergit_r_keshig"),
	(troop_set_slot, troop_trees_1, slot_khergit_mandugai, "trp_khergit_r_borjigin"),
	#Extra
	(troop_set_slot, troop_trees_1, slot_khergit_extra1, "trp_khergit_r_extra1"),
	(troop_set_slot, troop_trees_1, slot_khergit_extra2, "trp_khergit_r_extra2"),
	(troop_set_slot, troop_trees_1, slot_khergit_extra3, "trp_khergit_r_extra3"),
	(troop_set_slot, troop_trees_1, slot_khergit_extra4, "trp_khergit_r_extra4"),
	(troop_set_slot, troop_trees_1, slot_khergit_extra5, "trp_khergit_r_extra5"),
	##Expanded
	#Tier 1
	(troop_set_slot, troop_trees_2, slot_khergit_tariachin, "trp_khergit_e_tariachin"),
	#Tier 2
	(troop_set_slot, troop_trees_2, slot_khergit_tsereg, "trp_khergit_e_tsereg"),
	(troop_set_slot, troop_trees_2, slot_khergit_qarbughaci, "trp_khergit_e_qarbughaci"),
	#Tier 3
	(troop_set_slot, troop_trees_2, slot_khergit_morici, "trp_khergit_e_morici"),
	(troop_set_slot, troop_trees_2, slot_khergit_asud, "trp_khergit_e_asud"),
	(troop_set_slot, troop_trees_2, slot_khergit_surcin, "trp_khergit_e_surcin"),
	(troop_set_slot, troop_trees_2, slot_khergit_abaci, "trp_khergit_e_abaci"),
	#Tier 4
	(troop_set_slot, troop_trees_2, slot_khergit_kipchak, "trp_khergit_e_kipchak"),
	(troop_set_slot, troop_trees_2, slot_khergit_quaqli, "trp_khergit_e_quaqli"),
	(troop_set_slot, troop_trees_2, slot_khergit_aqala_asud, "trp_khergit_e_aqala_asud"),
	(troop_set_slot, troop_trees_2, slot_khergit_aqala_surcin, "trp_khergit_e_aqala_surcin"),
	(troop_set_slot, troop_trees_2, slot_khergit_teriguci, "trp_khergit_e_teriguci"),
	(troop_set_slot, troop_trees_2, slot_khergit_qubuci, "trp_khergit_e_qubuci"),
	#Tier 5
	(troop_set_slot, troop_trees_2, slot_khergit_torguu, "trp_khergit_e_torguu"),
	(troop_set_slot, troop_trees_2, slot_khergit_khevtuul, "trp_khergit_e_khevtuul"),
	(troop_set_slot, troop_trees_2, slot_khergit_yabagharu_morici, "trp_khergit_e_yabagharu_morici"),
	(troop_set_slot, troop_trees_2, slot_khergit_numici, "trp_khergit_e_numici"),
	(troop_set_slot, troop_trees_2, slot_khergit_aqala_teriguci, "trp_khergit_e_aqala_teriguci"),
	(troop_set_slot, troop_trees_2, slot_khergit_borjigin, "trp_khergit_e_borjigin"),
	(troop_set_slot, troop_trees_2, slot_khergit_numyn_ad, "trp_khergit_e_numyn_ad"),
	#Tier 6
	(troop_set_slot, troop_trees_2, slot_khergit_khorchen, "trp_khergit_e_khorchen"),
	(troop_set_slot, troop_trees_2, slot_khergit_keshig, "trp_khergit_e_keshig"),
	(troop_set_slot, troop_trees_2, slot_khergit_kharvaach, "trp_khergit_e_kharvaach"),
	(troop_set_slot, troop_trees_2, slot_khergit_jurtchi, "trp_khergit_e_jurtchi"),
	(troop_set_slot, troop_trees_2, slot_khergit_aqata_borjigin, "trp_khergit_e_aqata_borjigin"),
	#Tier 7
	(troop_set_slot, troop_trees_2, slot_khergit_cherbi, "trp_khergit_e_cherbi"),
	(troop_set_slot, troop_trees_2, slot_khergit_mandugai, "trp_khergit_e_mandugai"),
	#Extra
	(troop_set_slot, troop_trees_2, slot_khergit_extra1, "trp_khergit_e_extra1"),
	(troop_set_slot, troop_trees_2, slot_khergit_extra2, "trp_khergit_e_extra2"),
	(troop_set_slot, troop_trees_2, slot_khergit_extra3, "trp_khergit_e_extra3"),
	(troop_set_slot, troop_trees_2, slot_khergit_extra4, "trp_khergit_e_extra4"),
	(troop_set_slot, troop_trees_2, slot_khergit_extra5, "trp_khergit_e_extra5"),
	###Nord
	##Native
	#Tier 1
	(troop_set_slot, troop_trees_0, slot_nord_bondi, "trp_nord_n_bondi"),
	#Tier 2
	(troop_set_slot, troop_trees_0, slot_nord_berserkr, "trp_nord_n_gesith"),
	(troop_set_slot, troop_trees_0, slot_nord_huskarl, "trp_nord_n_huskarl"),
	#Tier 3
	(troop_set_slot, troop_trees_0, slot_nord_kertilsveinr, "trp_nord_n_bogmadur"),
	(troop_set_slot, troop_trees_0, slot_nord_bogmadur, "trp_nord_n_bogmadur"),
	(troop_set_slot, troop_trees_0, slot_nord_gesith, "trp_nord_n_gridman"),
	(troop_set_slot, troop_trees_0, slot_nord_gridman, "trp_nord_n_gridman"),
	#Tier 4
	(troop_set_slot, troop_trees_0, slot_nord_ascoman, "trp_nord_n_vigamadr"),
	(troop_set_slot, troop_trees_0, slot_nord_vikingr, "trp_nord_n_vigamadr"),
	(troop_set_slot, troop_trees_0, slot_nord_einhleyping, "trp_nord_n_bogsveigir"),
	(troop_set_slot, troop_trees_0, slot_nord_bogsveigir, "trp_nord_n_bogsveigir"),
	(troop_set_slot, troop_trees_0, slot_nord_hermadur, "trp_nord_n_bogsveigir"),
	(troop_set_slot, troop_trees_0, slot_nord_innaesmaen, "trp_nord_n_vigamadr"),
	(troop_set_slot, troop_trees_0, slot_nord_vigamadr, "trp_nord_n_vigamadr"),
	#Tier 5
	(troop_set_slot, troop_trees_0, slot_nord_hirdman, "trp_nord_n_skjadsveinn"),
	(troop_set_slot, troop_trees_0, slot_nord_lausaman, "trp_nord_n_skjadsveinn"),
	(troop_set_slot, troop_trees_0, slot_nord_heahgerefa, "trp_nord_n_skjadsveinn"),
	(troop_set_slot, troop_trees_0, slot_nord_himthige, "trp_nord_n_skjadsveinn"),
	(troop_set_slot, troop_trees_0, slot_nord_kappi, "trp_nord_n_skjadsveinn"),
	(troop_set_slot, troop_trees_0, slot_nord_skjadsveinn, "trp_nord_n_skjadsveinn"),
	(troop_set_slot, troop_trees_0, slot_nord_heimthegi, "trp_nord_n_skjadsveinn"),
	#Tier 6
	(troop_set_slot, troop_trees_0, slot_nord_skutilsveinr, "trp_nord_n_husbondi"),
	(troop_set_slot, troop_trees_0, slot_nord_ealdorman, "trp_nord_n_husbondi"),
	(troop_set_slot, troop_trees_0, slot_nord_erfane_himthige, "trp_nord_n_husbondi"),
	(troop_set_slot, troop_trees_0, slot_nord_hetja, "trp_nord_n_husbondi"),
	(troop_set_slot, troop_trees_0, slot_nord_husbondi, "trp_nord_n_husbondi"),
	#Tier 7
	(troop_set_slot, troop_trees_0, slot_nord_aetheling, "trp_nord_n_husbondi"),
	(troop_set_slot, troop_trees_0, slot_nord_vaeringi, "trp_nord_n_husbondi"),
	#Extra
	(troop_set_slot, troop_trees_0, slot_nord_extra1, "trp_nord_n_extra1"),
	(troop_set_slot, troop_trees_0, slot_nord_extra2, "trp_nord_n_extra2"),
	(troop_set_slot, troop_trees_0, slot_nord_extra3, "trp_nord_n_extra3"),
	(troop_set_slot, troop_trees_0, slot_nord_extra4, "trp_nord_n_extra4"),
	(troop_set_slot, troop_trees_0, slot_nord_extra5, "trp_nord_n_extra5"),
	##Reworked
	#Tier 1
	(troop_set_slot, troop_trees_1, slot_nord_bondi, "trp_nord_r_bondi"),
	#Tier 2
	(troop_set_slot, troop_trees_1, slot_nord_berserkr, "trp_nord_r_berserkr"),
	(troop_set_slot, troop_trees_1, slot_nord_huskarl, "trp_nord_r_huskarl"),
	#Tier 3
	(troop_set_slot, troop_trees_1, slot_nord_kertilsveinr, "trp_nord_r_kertilsveinr"),
	(troop_set_slot, troop_trees_1, slot_nord_bogmadur, "trp_nord_r_gesith"),
	(troop_set_slot, troop_trees_1, slot_nord_gesith, "trp_nord_r_gesith"),
	(troop_set_slot, troop_trees_1, slot_nord_gridman, "trp_nord_r_gridman"),
	#Tier 4
	(troop_set_slot, troop_trees_1, slot_nord_ascoman, "trp_nord_r_vikingr"),
	(troop_set_slot, troop_trees_1, slot_nord_vikingr, "trp_nord_r_vikingr"),
	(troop_set_slot, troop_trees_1, slot_nord_einhleyping, "trp_nord_r_vigamadr"),
	(troop_set_slot, troop_trees_1, slot_nord_bogsveigir, "trp_nord_r_bogsveigir"),
	(troop_set_slot, troop_trees_1, slot_nord_hermadur, "trp_nord_r_hermadur"),
	(troop_set_slot, troop_trees_1, slot_nord_innaesmaen, "trp_nord_r_innaesmaen"),
	(troop_set_slot, troop_trees_1, slot_nord_vigamadr, "trp_nord_r_vigamadr"),
	#Tier 5
	(troop_set_slot, troop_trees_1, slot_nord_hirdman, "trp_nord_r_skjadsveinn"),
	(troop_set_slot, troop_trees_1, slot_nord_lausaman, "trp_nord_r_heahgerefa"),
	(troop_set_slot, troop_trees_1, slot_nord_heahgerefa, "trp_nord_r_heahgerefa"),
	(troop_set_slot, troop_trees_1, slot_nord_himthige, "trp_nord_r_kappi"),
	(troop_set_slot, troop_trees_1, slot_nord_kappi, "trp_nord_r_kappi"),
	(troop_set_slot, troop_trees_1, slot_nord_skjadsveinn, "trp_nord_r_skjadsveinn"),
	(troop_set_slot, troop_trees_1, slot_nord_heimthegi, "trp_nord_r_skjadsveinn"),
	#Tier 6
	(troop_set_slot, troop_trees_1, slot_nord_skutilsveinr, "trp_nord_r_skjadsveinn"),
	(troop_set_slot, troop_trees_1, slot_nord_ealdorman, "trp_nord_r_heahgerefa"),
	(troop_set_slot, troop_trees_1, slot_nord_erfane_himthige, "trp_nord_r_kappi"),
	(troop_set_slot, troop_trees_1, slot_nord_hetja, "trp_nord_r_skjadsveinn"),
	(troop_set_slot, troop_trees_1, slot_nord_husbondi, "trp_nord_r_husbondi"),
	#Tier 7
	(troop_set_slot, troop_trees_1, slot_nord_aetheling, "trp_nord_r_skjadsveinn"),
	(troop_set_slot, troop_trees_1, slot_nord_vaeringi, "trp_nord_r_husbondi"),
	#Extra
	(troop_set_slot, troop_trees_1, slot_nord_extra1, "trp_nord_r_extra1"),
	(troop_set_slot, troop_trees_1, slot_nord_extra2, "trp_nord_r_extra2"),
	(troop_set_slot, troop_trees_1, slot_nord_extra3, "trp_nord_r_extra3"),
	(troop_set_slot, troop_trees_1, slot_nord_extra4, "trp_nord_r_extra4"),
	(troop_set_slot, troop_trees_1, slot_nord_extra5, "trp_nord_r_extra5"),
	##Expanded
	#Tier 1
	(troop_set_slot, troop_trees_2, slot_nord_bondi, "trp_nord_e_bondi"),
	#Tier 2
	(troop_set_slot, troop_trees_2, slot_nord_berserkr, "trp_nord_e_huskarl"),
	(troop_set_slot, troop_trees_2, slot_nord_huskarl, "trp_nord_e_huskarl"),
	#Tier 3
	(troop_set_slot, troop_trees_2, slot_nord_kertilsveinr, "trp_nord_e_gridman"),
	(troop_set_slot, troop_trees_2, slot_nord_bogmadur, "trp_nord_e_bogmadur"),
	(troop_set_slot, troop_trees_2, slot_nord_gesith, "trp_nord_e_gridman"),
	(troop_set_slot, troop_trees_2, slot_nord_gridman, "trp_nord_e_gridman"),
	#Tier 4
	(troop_set_slot, troop_trees_2, slot_nord_ascoman, "trp_nord_e_ascoman"),
	(troop_set_slot, troop_trees_2, slot_nord_vikingr, "trp_nord_e_innaesmaen"),
	(troop_set_slot, troop_trees_2, slot_nord_einhleyping, "trp_nord_e_einhleyping"),
	(troop_set_slot, troop_trees_2, slot_nord_bogsveigir, "trp_nord_e_bogsveigir"),
	(troop_set_slot, troop_trees_2, slot_nord_hermadur, "trp_nord_e_vigamadr"),
	(troop_set_slot, troop_trees_2, slot_nord_innaesmaen, "trp_nord_e_innaesmaen"),
	(troop_set_slot, troop_trees_2, slot_nord_vigamadr, "trp_nord_e_vigamadr"),
	#Tier 5
	(troop_set_slot, troop_trees_2, slot_nord_hirdman, "trp_nord_e_hirdman"),
	(troop_set_slot, troop_trees_2, slot_nord_lausaman, "trp_nord_e_lausaman"),
	(troop_set_slot, troop_trees_2, slot_nord_heahgerefa, "trp_nord_e_heimthegi"),
	(troop_set_slot, troop_trees_2, slot_nord_himthige, "trp_nord_e_kappi"),
	(troop_set_slot, troop_trees_2, slot_nord_kappi, "trp_nord_e_kappi"),
	(troop_set_slot, troop_trees_2, slot_nord_skjadsveinn, "trp_nord_e_skjadsveinn"),
	(troop_set_slot, troop_trees_2, slot_nord_heimthegi, "trp_nord_e_heimthegi"),
	#Tier 6
	(troop_set_slot, troop_trees_2, slot_nord_skutilsveinr, "trp_nord_e_skutilsveinr"),
	(troop_set_slot, troop_trees_2, slot_nord_ealdorman, "trp_nord_e_skutilsveinr"),
	(troop_set_slot, troop_trees_2, slot_nord_erfane_himthige, "trp_nord_e_hetja"),
	(troop_set_slot, troop_trees_2, slot_nord_hetja, "trp_nord_e_hetja"),
	(troop_set_slot, troop_trees_2, slot_nord_husbondi, "trp_nord_e_husbondi"),
	#Tier 7
	(troop_set_slot, troop_trees_2, slot_nord_aetheling, "trp_nord_e_aetheling"),
	(troop_set_slot, troop_trees_2, slot_nord_vaeringi, "trp_nord_e_vaeringi"),
	#Extra
	(troop_set_slot, troop_trees_2, slot_nord_extra1, "trp_nord_e_extra1"),
	(troop_set_slot, troop_trees_2, slot_nord_extra2, "trp_nord_e_extra2"),
	(troop_set_slot, troop_trees_2, slot_nord_extra3, "trp_nord_e_extra3"),
	(troop_set_slot, troop_trees_2, slot_nord_extra4, "trp_nord_e_extra4"),
	(troop_set_slot, troop_trees_2, slot_nord_extra5, "trp_nord_e_extra5"),
	###Rhodok
	##Native
	#Tier 1
	(troop_set_slot, troop_trees_0, slot_rhodok_cittadino, "trp_rhodok_n_cittadino"),
	#Tier 2
	(troop_set_slot, troop_trees_0, slot_rhodok_novizio, "trp_rhodok_n_novizio"),
	(troop_set_slot, troop_trees_0, slot_rhodok_recluta, "trp_rhodok_n_recluta_balestriere"),
	#Tier 3
	(troop_set_slot, troop_trees_0, slot_rhodok_milizia, "trp_rhodok_n_milizia"),
	(troop_set_slot, troop_trees_0, slot_rhodok_milizia_balestriere, "trp_rhodok_n_milizia_balestriere"),
	(troop_set_slot, troop_trees_0, slot_rhodok_recluta_balestriere, "trp_rhodok_n_milizia_balestriere"),
	(troop_set_slot, troop_trees_0, slot_rhodok_lanciere, "trp_rhodok_n_milizia"),
	#Tier 4
	(troop_set_slot, troop_trees_0, slot_rhodok_lanza_spezzata, "trp_rhodok_n_fante"),
	(troop_set_slot, troop_trees_0, slot_rhodok_fante, "trp_rhodok_n_fante"),
	(troop_set_slot, troop_trees_0, slot_rhodok_balestriere, "trp_rhodok_n_balestriere"),
	(troop_set_slot, troop_trees_0, slot_rhodok_balestriere_leggero, "trp_rhodok_n_balestriere"),
	(troop_set_slot, troop_trees_0, slot_rhodok_lanciere_veterano, "trp_rhodok_n_fante"),
	(troop_set_slot, troop_trees_0, slot_rhodok_lanciere_a_cavallo, "trp_rhodok_n_fante"),
	#Tier 5
	(troop_set_slot, troop_trees_0, slot_rhodok_provisionato, "trp_rhodok_n_fante"),
	(troop_set_slot, troop_trees_0, slot_rhodok_veterano, "trp_rhodok_n_fante"),
	(troop_set_slot, troop_trees_0, slot_rhodok_balestriere_veterano, "trp_rhodok_n_balestriere"),
	(troop_set_slot, troop_trees_0, slot_rhodok_balestriere_d_assedio, "trp_rhodok_n_balestriere"),
	(troop_set_slot, troop_trees_0, slot_rhodok_balestriere_a_cavallo, "trp_rhodok_n_balestriere"),
	(troop_set_slot, troop_trees_0, slot_rhodok_picchiere_veterano, "trp_rhodok_n_fante"),
	(troop_set_slot, troop_trees_0, slot_rhodok_guardia, "trp_rhodok_n_fante"),
	#Tier 6
	(troop_set_slot, troop_trees_0, slot_rhodok_capitano_di_ventura, "trp_rhodok_n_fante"),
	(troop_set_slot, troop_trees_0, slot_rhodok_balestriere_pesante, "trp_rhodok_n_balestriere"),
	(troop_set_slot, troop_trees_0, slot_rhodok_capitano_d_assedio, "trp_rhodok_n_balestriere"),
	(troop_set_slot, troop_trees_0, slot_rhodok_picchiere_fiammingo, "trp_rhodok_n_fante"),
	(troop_set_slot, troop_trees_0, slot_rhodok_guardia_ducale, "trp_rhodok_n_fante"),
	#Tier 7
	(troop_set_slot, troop_trees_0, slot_rhodok_condottiero, "trp_rhodok_n_fante"),
	(troop_set_slot, troop_trees_0, slot_rhodok_condottiero_d_assedio, "trp_rhodok_n_balestriere"),
	#Extra
	(troop_set_slot, troop_trees_0, slot_rhodok_extra1, "trp_rhodok_n_extra1"),
	(troop_set_slot, troop_trees_0, slot_rhodok_extra2, "trp_rhodok_n_extra2"),
	(troop_set_slot, troop_trees_0, slot_rhodok_extra3, "trp_rhodok_n_extra3"),
	(troop_set_slot, troop_trees_0, slot_rhodok_extra4, "trp_rhodok_n_extra4"),
	(troop_set_slot, troop_trees_0, slot_rhodok_extra5, "trp_rhodok_n_extra5"),
	##Reworked
	#Tier 1
	(troop_set_slot, troop_trees_1, slot_rhodok_cittadino, "trp_rhodok_r_cittadino"),
	#Tier 2
	(troop_set_slot, troop_trees_1, slot_rhodok_novizio, "trp_rhodok_r_novizio"),
	(troop_set_slot, troop_trees_1, slot_rhodok_recluta, "trp_rhodok_r_recluta"),
	#Tier 3
	(troop_set_slot, troop_trees_1, slot_rhodok_milizia, "trp_rhodok_r_lanciere_a_cavallo"),
	(troop_set_slot, troop_trees_1, slot_rhodok_milizia_balestriere, "trp_rhodok_r_recluta_balestriere"),
	(troop_set_slot, troop_trees_1, slot_rhodok_recluta_balestriere, "trp_rhodok_r_recluta_balestriere"),
	(troop_set_slot, troop_trees_1, slot_rhodok_lanciere, "trp_rhodok_r_lanciere"),
	#Tier 4
	(troop_set_slot, troop_trees_1, slot_rhodok_lanza_spezzata, "trp_rhodok_r_lanza_spezzata"),
	(troop_set_slot, troop_trees_1, slot_rhodok_fante, "trp_rhodok_r_fante"),
	(troop_set_slot, troop_trees_1, slot_rhodok_balestriere, "trp_rhodok_r_balestriere"),
	(troop_set_slot, troop_trees_1, slot_rhodok_balestriere_leggero, "trp_rhodok_r_balestriere_leggero"),
	(troop_set_slot, troop_trees_1, slot_rhodok_lanciere_veterano, "trp_rhodok_r_lanciere_veterano"),
	(troop_set_slot, troop_trees_1, slot_rhodok_lanciere_a_cavallo, "trp_rhodok_r_lanza_spezzata"),
	#Tier 5
	(troop_set_slot, troop_trees_1, slot_rhodok_provisionato, "trp_rhodok_r_picchiere_veterano"),
	(troop_set_slot, troop_trees_1, slot_rhodok_veterano, "trp_rhodok_r_picchiere_veterano"),
#	(troop_set_slot, troop_trees_1, slot_rhodok_balestriere_veterano, "trp_rhodok_r_balestriere_d_assedio"),
	(troop_set_slot, troop_trees_1, slot_rhodok_balestriere_d_assedio, "trp_rhodok_r_balestriere_d_assedio"),
	(troop_set_slot, troop_trees_1, slot_rhodok_balestriere_a_cavallo, "trp_rhodok_r_balestriere_d_assedio"),
	(troop_set_slot, troop_trees_1, slot_rhodok_picchiere_veterano, "trp_rhodok_r_picchiere_veterano"),
	(troop_set_slot, troop_trees_1, slot_rhodok_guardia, "trp_rhodok_r_picchiere_veterano"),
	#Tier 6
	(troop_set_slot, troop_trees_1, slot_rhodok_capitano_di_ventura, "trp_rhodok_r_picchiere_veterano"),
	(troop_set_slot, troop_trees_1, slot_rhodok_balestriere_pesante, "trp_rhodok_r_capitano_d_assedio"),
	(troop_set_slot, troop_trees_1, slot_rhodok_capitano_d_assedio, "trp_rhodok_r_capitano_d_assedio"),
	(troop_set_slot, troop_trees_1, slot_rhodok_picchiere_fiammingo, "trp_rhodok_r_picchiere_veterano"),
	(troop_set_slot, troop_trees_1, slot_rhodok_guardia_ducale, "trp_rhodok_r_picchiere_veterano"),
	#Tier 7
	(troop_set_slot, troop_trees_1, slot_rhodok_condottiero, "trp_rhodok_r_picchiere_veterano"),
	(troop_set_slot, troop_trees_1, slot_rhodok_condottiero_d_assedio, "trp_rhodok_r_capitano_d_assedio"),
	#Extra
	(troop_set_slot, troop_trees_1, slot_rhodok_extra1, "trp_rhodok_r_extra1"),
	(troop_set_slot, troop_trees_1, slot_rhodok_extra2, "trp_rhodok_r_extra2"),
	(troop_set_slot, troop_trees_1, slot_rhodok_extra3, "trp_rhodok_r_extra3"),
	(troop_set_slot, troop_trees_1, slot_rhodok_extra4, "trp_rhodok_r_extra4"),
	(troop_set_slot, troop_trees_1, slot_rhodok_extra5, "trp_rhodok_r_extra5"),
	##Expanded
	#Tier 1
	(troop_set_slot, troop_trees_2, slot_rhodok_cittadino, "trp_rhodok_e_cittadino"),
	#Tier 2
	(troop_set_slot, troop_trees_2, slot_rhodok_novizio, "trp_rhodok_e_novizio"),
	(troop_set_slot, troop_trees_2, slot_rhodok_recluta, "trp_rhodok_e_recluta"),
	#Tier 3
	(troop_set_slot, troop_trees_2, slot_rhodok_milizia, "trp_rhodok_e_milizia"),
	(troop_set_slot, troop_trees_2, slot_rhodok_milizia_balestriere, "trp_rhodok_e_milizia_balestriere"),
	(troop_set_slot, troop_trees_2, slot_rhodok_recluta_balestriere, "trp_rhodok_e_recluta_balestriere"),
	(troop_set_slot, troop_trees_2, slot_rhodok_lanciere, "trp_rhodok_e_lanciere"),
	#Tier 4
	(troop_set_slot, troop_trees_2, slot_rhodok_lanza_spezzata, "trp_rhodok_e_lanza_spezzata"),
	(troop_set_slot, troop_trees_2, slot_rhodok_fante, "trp_rhodok_e_fante"),
	(troop_set_slot, troop_trees_2, slot_rhodok_balestriere, "trp_rhodok_e_balestriere"),
	(troop_set_slot, troop_trees_2, slot_rhodok_balestriere_leggero, "trp_rhodok_e_balestriere_leggero"),
	(troop_set_slot, troop_trees_2, slot_rhodok_lanciere_veterano, "trp_rhodok_e_lanciere_veterano"),
	(troop_set_slot, troop_trees_2, slot_rhodok_lanciere_a_cavallo, "trp_rhodok_e_lanciere_a_cavallo"),
	#Tier 5
	(troop_set_slot, troop_trees_2, slot_rhodok_provisionato, "trp_rhodok_e_provisionato"),
	(troop_set_slot, troop_trees_2, slot_rhodok_veterano, "trp_rhodok_e_veterano"),
#	(troop_set_slot, troop_trees_2, slot_rhodok_balestriere_veterano, "trp_rhodok_e_balestriere_d_assedio"),
	(troop_set_slot, troop_trees_2, slot_rhodok_balestriere_d_assedio, "trp_rhodok_e_balestriere_d_assedio"),
	(troop_set_slot, troop_trees_2, slot_rhodok_balestriere_a_cavallo, "trp_rhodok_e_balestriere_a_cavallo"),
	(troop_set_slot, troop_trees_2, slot_rhodok_picchiere_veterano, "trp_rhodok_e_picchiere_veterano"),
	(troop_set_slot, troop_trees_2, slot_rhodok_guardia, "trp_rhodok_e_guardia"),
	#Tier 6
	(troop_set_slot, troop_trees_2, slot_rhodok_capitano_di_ventura, "trp_rhodok_e_capitano_di_ventura"),
#	(troop_set_slot, troop_trees_2, slot_rhodok_balestriere_pesante, "trp_rhodok_e_balestriere_d_assedio"),
	(troop_set_slot, troop_trees_2, slot_rhodok_capitano_d_assedio, "trp_rhodok_e_capitano_d_assedio"),
	(troop_set_slot, troop_trees_2, slot_rhodok_picchiere_fiammingo, "trp_rhodok_e_picchiere_fiammingo"),
	(troop_set_slot, troop_trees_2, slot_rhodok_guardia_ducale, "trp_rhodok_e_guardia_ducale"),
	#Tier 7
	(troop_set_slot, troop_trees_2, slot_rhodok_condottiero, "trp_rhodok_e_condottiero"),
	(troop_set_slot, troop_trees_2, slot_rhodok_condottiero_d_assedio, "trp_rhodok_e_condottiero_d_assedio"),
	#Extra
	(troop_set_slot, troop_trees_2, slot_rhodok_extra1, "trp_rhodok_e_extra1"),
	(troop_set_slot, troop_trees_2, slot_rhodok_extra2, "trp_rhodok_e_extra2"),
	(troop_set_slot, troop_trees_2, slot_rhodok_extra3, "trp_rhodok_e_extra3"),
	(troop_set_slot, troop_trees_2, slot_rhodok_extra4, "trp_rhodok_e_extra4"),
	(troop_set_slot, troop_trees_2, slot_rhodok_extra5, "trp_rhodok_e_extra5"),
	###Sarranid
	##Native
	#Tier 1
	(troop_set_slot, troop_trees_0, slot_sarranid_millet, "trp_sarranid_n_millet"),
	#Tier 2
	(troop_set_slot, troop_trees_0, slot_sarranid_ajam, "trp_sarranid_n_ajam"),
	(troop_set_slot, troop_trees_0, slot_sarranid_oglan, "trp_sarranid_n_ajam"),
	#Tier 3
	(troop_set_slot, troop_trees_0, slot_sarranid_azab, "trp_sarranid_n_cemaat"),
	(troop_set_slot, troop_trees_0, slot_sarranid_cemaat, "trp_sarranid_n_cemaat"),
	(troop_set_slot, troop_trees_0, slot_sarranid_jebelus, "trp_sarranid_n_jebelus"),
	(troop_set_slot, troop_trees_0, slot_sarranid_ghulam, "trp_sarranid_n_jebelus"),
	#Tier 4
	(troop_set_slot, troop_trees_0, slot_sarranid_al_haqa, "trp_sarranid_n_timariot"),
	(troop_set_slot, troop_trees_0, slot_sarranid_timariot, "trp_sarranid_n_timariot"),
	(troop_set_slot, troop_trees_0, slot_sarranid_yerliyya, "trp_sarranid_n_yerliyya"),
	(troop_set_slot, troop_trees_0, slot_sarranid_kapikulu_savari, "trp_sarranid_n_yerliyya"),
	(troop_set_slot, troop_trees_0, slot_sarranid_garip, "trp_sarranid_n_garip"),
	(troop_set_slot, troop_trees_0, slot_sarranid_badw, "trp_sarranid_n_timariot"),
	(troop_set_slot, troop_trees_0, slot_sarranid_serdengecti, "trp_sarranid_n_garip"),
	(troop_set_slot, troop_trees_0, slot_sarranid_tabardariyya, "trp_sarranid_n_garip"),
	#Tier 5
	(troop_set_slot, troop_trees_0, slot_sarranid_kapikula, "trp_sarranid_n_kapikula"),
	(troop_set_slot, troop_trees_0, slot_sarranid_yeniceri, "trp_sarranid_n_yeniceri"),
	(troop_set_slot, troop_trees_0, slot_sarranid_beylik, "trp_sarranid_n_yeniceri"),
	(troop_set_slot, troop_trees_0, slot_sarranid_uluteci, "trp_sarranid_n_uluteci"),
	(troop_set_slot, troop_trees_0, slot_sarranid_akinci, "trp_sarranid_n_uluteci"),
	(troop_set_slot, troop_trees_0, slot_sarranid_terkes_serdengecti, "trp_sarranid_n_yeniceri"),
	#Tier 6
	(troop_set_slot, troop_trees_0, slot_sarranid_qilich_arslan, "trp_sarranid_n_yeniceri"),
	(troop_set_slot, troop_trees_0, slot_sarranid_memluk, "trp_sarranid_n_kapikula"),
	(troop_set_slot, troop_trees_0, slot_sarranid_sekban, "trp_sarranid_n_kapikula"),
	(troop_set_slot, troop_trees_0, slot_sarranid_silahtar, "trp_sarranid_n_uluteci"),
	(troop_set_slot, troop_trees_0, slot_sarranid_sipahi, "trp_sarranid_n_uluteci"),
	#Tier 7
	(troop_set_slot, troop_trees_0, slot_sarranid_hasham, "trp_sarranid_n_kapikula"),
	(troop_set_slot, troop_trees_0, slot_sarranid_iqta_dar, "trp_sarranid_n_uluteci"),
	#Extra
	(troop_set_slot, troop_trees_0, slot_sarranid_extra1, "trp_sarranid_n_extra1"),
	(troop_set_slot, troop_trees_0, slot_sarranid_extra2, "trp_sarranid_n_extra2"),
	(troop_set_slot, troop_trees_0, slot_sarranid_extra3, "trp_sarranid_n_extra3"),
	(troop_set_slot, troop_trees_0, slot_sarranid_extra4, "trp_sarranid_n_extra4"),
	(troop_set_slot, troop_trees_0, slot_sarranid_extra5, "trp_sarranid_n_extra5"),
	##Reworked
	#Tier 1
	(troop_set_slot, troop_trees_1, slot_sarranid_millet, "trp_sarranid_r_millet"),
	#Tier 2
	(troop_set_slot, troop_trees_1, slot_sarranid_ajam, "trp_sarranid_r_ajam"),
	(troop_set_slot, troop_trees_1, slot_sarranid_oglan, "trp_sarranid_r_oglan"),
	#Tier 3
	(troop_set_slot, troop_trees_1, slot_sarranid_azab, "trp_sarranid_r_azab"),
	(troop_set_slot, troop_trees_1, slot_sarranid_cemaat, "trp_sarranid_r_cemaat"),
	(troop_set_slot, troop_trees_1, slot_sarranid_jebelus, "trp_sarranid_r_jebelus"),
	(troop_set_slot, troop_trees_1, slot_sarranid_ghulam, "trp_sarranid_r_jebelus"),
	#Tier 4
	(troop_set_slot, troop_trees_1, slot_sarranid_al_haqa, "trp_sarranid_r_al_haqa"),
	(troop_set_slot, troop_trees_1, slot_sarranid_timariot, "trp_sarranid_r_timariot"),
	(troop_set_slot, troop_trees_1, slot_sarranid_yerliyya, "trp_sarranid_r_kapikulu_savari"),
	(troop_set_slot, troop_trees_1, slot_sarranid_kapikulu_savari, "trp_sarranid_r_kapikulu_savari"),
	(troop_set_slot, troop_trees_1, slot_sarranid_garip, "trp_sarranid_r_garip"),
	(troop_set_slot, troop_trees_1, slot_sarranid_badw, "trp_sarranid_r_badw"),
	(troop_set_slot, troop_trees_1, slot_sarranid_serdengecti, "trp_sarranid_r_badw"),
	(troop_set_slot, troop_trees_1, slot_sarranid_tabardariyya, "trp_sarranid_r_garip"),
	#Tier 5
	(troop_set_slot, troop_trees_1, slot_sarranid_kapikula, "trp_sarranid_r_kapikula"),
	(troop_set_slot, troop_trees_1, slot_sarranid_yeniceri, "trp_sarranid_r_kapikula"),
	(troop_set_slot, troop_trees_1, slot_sarranid_beylik, "trp_sarranid_r_yerliyya"),
	(troop_set_slot, troop_trees_1, slot_sarranid_uluteci, "trp_sarranid_r_uluteci"),
	(troop_set_slot, troop_trees_1, slot_sarranid_akinci, "trp_sarranid_r_uluteci"),
	(troop_set_slot, troop_trees_1, slot_sarranid_terkes_serdengecti, "trp_sarranid_r_yerliyya"),
	#Tier 6
	(troop_set_slot, troop_trees_1, slot_sarranid_qilich_arslan, "trp_sarranid_r_kapikula"),
	(troop_set_slot, troop_trees_1, slot_sarranid_memluk, "trp_sarranid_r_yeniceri"),
	(troop_set_slot, troop_trees_1, slot_sarranid_sekban, "trp_sarranid_r_yeniceri"),
	(troop_set_slot, troop_trees_1, slot_sarranid_silahtar, "trp_sarranid_r_uluteci"),
	(troop_set_slot, troop_trees_1, slot_sarranid_sipahi, "trp_sarranid_r_uluteci"),
	#Tier 7
	(troop_set_slot, troop_trees_1, slot_sarranid_hasham, "trp_sarranid_r_yeniceri"),
	(troop_set_slot, troop_trees_1, slot_sarranid_iqta_dar, "trp_sarranid_r_uluteci"),
	#Extra
	(troop_set_slot, troop_trees_1, slot_sarranid_extra1, "trp_sarranid_r_extra1"),
	(troop_set_slot, troop_trees_1, slot_sarranid_extra2, "trp_sarranid_r_extra2"),
	(troop_set_slot, troop_trees_1, slot_sarranid_extra3, "trp_sarranid_r_extra3"),
	(troop_set_slot, troop_trees_1, slot_sarranid_extra4, "trp_sarranid_r_extra4"),
	(troop_set_slot, troop_trees_1, slot_sarranid_extra5, "trp_sarranid_r_extra5"),
	##Expanded
	#Tier 1
	(troop_set_slot, troop_trees_2, slot_sarranid_millet, "trp_sarranid_e_millet"),
	#Tier 2
	(troop_set_slot, troop_trees_2, slot_sarranid_ajam, "trp_sarranid_e_ajam"),
	(troop_set_slot, troop_trees_2, slot_sarranid_oglan, "trp_sarranid_e_oglan"),
	#Tier 3
	(troop_set_slot, troop_trees_2, slot_sarranid_azab, "trp_sarranid_e_azab"),
	(troop_set_slot, troop_trees_2, slot_sarranid_cemaat, "trp_sarranid_e_cemaat"),
	(troop_set_slot, troop_trees_2, slot_sarranid_jebelus, "trp_sarranid_e_jebelus"),
	(troop_set_slot, troop_trees_2, slot_sarranid_ghulam, "trp_sarranid_e_ghulam"),
	#Tier 4
	(troop_set_slot, troop_trees_2, slot_sarranid_al_haqa, "trp_sarranid_e_al_haqa"),
	(troop_set_slot, troop_trees_2, slot_sarranid_timariot, "trp_sarranid_e_timariot"),
	(troop_set_slot, troop_trees_2, slot_sarranid_yerliyya, "trp_sarranid_e_yerliyya"),
	(troop_set_slot, troop_trees_2, slot_sarranid_kapikulu_savari, "trp_sarranid_e_kapikulu_savari"),
	(troop_set_slot, troop_trees_2, slot_sarranid_garip, "trp_sarranid_e_garip"),
	(troop_set_slot, troop_trees_2, slot_sarranid_badw, "trp_sarranid_e_badw"),
	(troop_set_slot, troop_trees_2, slot_sarranid_serdengecti, "trp_sarranid_e_serdengecti"),
	(troop_set_slot, troop_trees_2, slot_sarranid_tabardariyya, "trp_sarranid_e_tabardariyya"),
	#Tier 5
	(troop_set_slot, troop_trees_2, slot_sarranid_kapikula, "trp_sarranid_e_kapikula"),
	(troop_set_slot, troop_trees_2, slot_sarranid_yeniceri, "trp_sarranid_e_yeniceri"),
	(troop_set_slot, troop_trees_2, slot_sarranid_beylik, "trp_sarranid_e_beylik"),
	(troop_set_slot, troop_trees_2, slot_sarranid_uluteci, "trp_sarranid_e_uluteci"),
	(troop_set_slot, troop_trees_2, slot_sarranid_akinci, "trp_sarranid_e_akinci"),
	(troop_set_slot, troop_trees_2, slot_sarranid_terkes_serdengecti, "trp_sarranid_e_terkes_serdengecti"),
	#Tier 6
	(troop_set_slot, troop_trees_2, slot_sarranid_qilich_arslan, "trp_sarranid_e_qilich_arslan"),
	(troop_set_slot, troop_trees_2, slot_sarranid_memluk, "trp_sarranid_e_memluk"),
	(troop_set_slot, troop_trees_2, slot_sarranid_sekban, "trp_sarranid_e_sekban"),
	(troop_set_slot, troop_trees_2, slot_sarranid_silahtar, "trp_sarranid_e_silahtar"),
	(troop_set_slot, troop_trees_2, slot_sarranid_sipahi, "trp_sarranid_e_sipahi"),
	#Tier 7
	(troop_set_slot, troop_trees_2, slot_sarranid_hasham, "trp_sarranid_e_hasham"),
	(troop_set_slot, troop_trees_2, slot_sarranid_iqta_dar, "trp_sarranid_e_iqta_dar"),
	#Extra
	(troop_set_slot, troop_trees_2, slot_sarranid_extra1, "trp_sarranid_e_extra1"),
	(troop_set_slot, troop_trees_2, slot_sarranid_extra2, "trp_sarranid_e_extra2"),
	(troop_set_slot, troop_trees_2, slot_sarranid_extra3, "trp_sarranid_e_extra3"),
	(troop_set_slot, troop_trees_2, slot_sarranid_extra4, "trp_sarranid_e_extra4"),
	(troop_set_slot, troop_trees_2, slot_sarranid_extra5, "trp_sarranid_e_extra5"),
	###Custom
	##Native
	#Tier 1
	(troop_set_slot, troop_trees_0, slot_custom_recruit, "trp_custom_n_recruit"),
	#Tier 2
	(troop_set_slot, troop_trees_0, slot_custom_militia, "trp_custom_n_militia"),
	(troop_set_slot, troop_trees_0, slot_custom_hunter, "trp_custom_n_militia"),
	#Tier 3
	(troop_set_slot, troop_trees_0, slot_custom_guard, "trp_custom_n_guard"),
	(troop_set_slot, troop_trees_0, slot_custom_page, "trp_custom_n_page"),
	(troop_set_slot, troop_trees_0, slot_custom_woodsman, "trp_custom_n_guard"),
	#Tier 4
	(troop_set_slot, troop_trees_0, slot_custom_swordman, "trp_custom_n_swordman"),
	(troop_set_slot, troop_trees_0, slot_custom_spearman, "trp_custom_n_swordman"),
	(troop_set_slot, troop_trees_0, slot_custom_squire, "trp_custom_n_squire"),
	(troop_set_slot, troop_trees_0, slot_custom_archer, "trp_custom_n_archer"),
	(troop_set_slot, troop_trees_0, slot_custom_skirmisher, "trp_custom_n_archer"),
	#Tier 5
	(troop_set_slot, troop_trees_0, slot_custom_swordmaster, "trp_custom_n_swordmaster"),
	(troop_set_slot, troop_trees_0, slot_custom_spearmaster, "trp_custom_n_swordmaster"),
	(troop_set_slot, troop_trees_0, slot_custom_knight, "trp_custom_n_knight"),
	(troop_set_slot, troop_trees_0, slot_custom_horse_archer, "trp_custom_n_expert_archer"),
	(troop_set_slot, troop_trees_0, slot_custom_expert_archer, "trp_custom_n_expert_archer"),
	(troop_set_slot, troop_trees_0, slot_custom_frontline_skirmisher, "trp_custom_n_expert_archer"),
	#Tier 6
	(troop_set_slot, troop_trees_0, slot_custom_heavy_knight, "trp_custom_n_knight"),
	(troop_set_slot, troop_trees_0, slot_custom_heavy_horse_archer, "trp_custom_n_expert_archer"),
	##Reworked
	#Tier 1
	(troop_set_slot, troop_trees_1, slot_custom_recruit, "trp_custom_r_recruit"),
	#Tier 2
	(troop_set_slot, troop_trees_1, slot_custom_militia, "trp_custom_r_militia"),
	(troop_set_slot, troop_trees_1, slot_custom_hunter, "trp_custom_r_hunter"),
	#Tier 3
	(troop_set_slot, troop_trees_1, slot_custom_guard, "trp_custom_r_guard"),
	(troop_set_slot, troop_trees_1, slot_custom_page, "trp_custom_r_page"),
	(troop_set_slot, troop_trees_1, slot_custom_woodsman, "trp_custom_r_woodsman"),
	#Tier 4
	(troop_set_slot, troop_trees_1, slot_custom_swordman, "trp_custom_r_swordman"),
	(troop_set_slot, troop_trees_1, slot_custom_spearman, "trp_custom_r_spearman"),
	(troop_set_slot, troop_trees_1, slot_custom_squire, "trp_custom_r_squire"),
	(troop_set_slot, troop_trees_1, slot_custom_archer, "trp_custom_r_archer"),
	(troop_set_slot, troop_trees_1, slot_custom_skirmisher, "trp_custom_r_skirmisher"),
	#Tier 5
	(troop_set_slot, troop_trees_1, slot_custom_swordmaster, "trp_custom_r_swordmaster"),
	(troop_set_slot, troop_trees_1, slot_custom_spearmaster, "trp_custom_r_swordmaster"),
	(troop_set_slot, troop_trees_1, slot_custom_knight, "trp_custom_r_knight"),
	(troop_set_slot, troop_trees_1, slot_custom_horse_archer, "trp_custom_r_expert_archer"),
	(troop_set_slot, troop_trees_1, slot_custom_expert_archer, "trp_custom_r_expert_archer"),
	(troop_set_slot, troop_trees_1, slot_custom_frontline_skirmisher, "trp_custom_r_frontline_skirmisher"),
	#Tier 6
	(troop_set_slot, troop_trees_1, slot_custom_heavy_knight, "trp_custom_r_knight"),
	(troop_set_slot, troop_trees_1, slot_custom_heavy_horse_archer, "trp_custom_r_expert_archer"),
	##Expanded
	#Tier 1
	(troop_set_slot, troop_trees_2, slot_custom_recruit, "trp_custom_e_recruit"),
	#Tier 2
	(troop_set_slot, troop_trees_2, slot_custom_militia, "trp_custom_e_militia"),
	(troop_set_slot, troop_trees_2, slot_custom_hunter, "trp_custom_e_hunter"),
	#Tier 3
	(troop_set_slot, troop_trees_2, slot_custom_guard, "trp_custom_e_guard"),
	(troop_set_slot, troop_trees_2, slot_custom_page, "trp_custom_e_page"),
	(troop_set_slot, troop_trees_2, slot_custom_woodsman, "trp_custom_e_woodsman"),
	#Tier 4
	(troop_set_slot, troop_trees_2, slot_custom_swordman, "trp_custom_e_swordman"),
	(troop_set_slot, troop_trees_2, slot_custom_spearman, "trp_custom_e_spearman"),
	(troop_set_slot, troop_trees_2, slot_custom_squire, "trp_custom_e_squire"),
	(troop_set_slot, troop_trees_2, slot_custom_archer, "trp_custom_e_archer"),
	(troop_set_slot, troop_trees_2, slot_custom_skirmisher, "trp_custom_e_skirmisher"),
	#Tier 5
	(troop_set_slot, troop_trees_2, slot_custom_swordmaster, "trp_custom_e_swordmaster"),
	(troop_set_slot, troop_trees_2, slot_custom_spearmaster, "trp_custom_e_spearmaster"),
	(troop_set_slot, troop_trees_2, slot_custom_knight, "trp_custom_e_knight"),
	(troop_set_slot, troop_trees_2, slot_custom_horse_archer, "trp_custom_e_horse_archer"),
	(troop_set_slot, troop_trees_2, slot_custom_expert_archer, "trp_custom_e_expert_archer"),
	(troop_set_slot, troop_trees_2, slot_custom_frontline_skirmisher, "trp_custom_e_frontline_skirmisher"),
	#Tier 6
	(troop_set_slot, troop_trees_2, slot_custom_heavy_knight, "trp_custom_e_heavy_knight"),
	(troop_set_slot, troop_trees_2, slot_custom_heavy_horse_archer, "trp_custom_e_heavy_horse_archer"),
	###Bandits
	##Native
	#Looters
	(troop_set_slot, troop_trees_0, slot_bandit_looter, "trp_bandit_n_looter"),
	(troop_set_slot, troop_trees_0, slot_bandit_bandit, "trp_bandit_n_bandit"),
	(troop_set_slot, troop_trees_0, slot_bandit_brigand, "trp_bandit_n_brigand"),
	#Bandits
	(troop_set_slot, troop_trees_0, slot_bandit_mountain, "trp_bandit_n_mountain"),
	(troop_set_slot, troop_trees_0, slot_bandit_forest, "trp_bandit_n_forest"),
	(troop_set_slot, troop_trees_0, slot_bandit_sea_raider, "trp_bandit_n_sea_raider"),
	(troop_set_slot, troop_trees_0, slot_bandit_steppe, "trp_bandit_n_steppe"),
	(troop_set_slot, troop_trees_0, slot_bandit_taiga, "trp_bandit_n_taiga"),
	(troop_set_slot, troop_trees_0, slot_bandit_desert, "trp_bandit_n_desert"),
	#Black Khergit
	(troop_set_slot, troop_trees_0, slot_bandit_black_khergit_horseman, "trp_bandit_n_black_khergit_horseman"),
	#Slavers
	(troop_set_slot, troop_trees_0, slot_bandit_manhunter, "trp_bandit_n_manhunter"),
	(troop_set_slot, troop_trees_0, slot_bandit_slave_driver, "trp_bandit_n_slave_driver"),
	(troop_set_slot, troop_trees_0, slot_bandit_slave_hunter, "trp_bandit_n_slave_hunter"),
	(troop_set_slot, troop_trees_0, slot_bandit_slave_crusher, "trp_bandit_n_slave_crusher"),
	(troop_set_slot, troop_trees_0, slot_bandit_slaver_chief, "trp_bandit_n_slaver_chief"),
	##Reworked
	#Looters
	(troop_set_slot, troop_trees_1, slot_bandit_looter, "trp_bandit_r_looter"),
	(troop_set_slot, troop_trees_1, slot_bandit_bandit, "trp_bandit_r_bandit"),
	(troop_set_slot, troop_trees_1, slot_bandit_brigand, "trp_bandit_r_brigand"),
	#Bandits
	(troop_set_slot, troop_trees_1, slot_bandit_mountain, "trp_bandit_r_mountain"),
	(troop_set_slot, troop_trees_1, slot_bandit_forest, "trp_bandit_r_forest"),
	(troop_set_slot, troop_trees_1, slot_bandit_sea_raider, "trp_bandit_r_sea_raider"),
	(troop_set_slot, troop_trees_1, slot_bandit_steppe, "trp_bandit_r_steppe"),
	(troop_set_slot, troop_trees_1, slot_bandit_taiga, "trp_bandit_r_taiga"),
	(troop_set_slot, troop_trees_1, slot_bandit_desert, "trp_bandit_r_desert"),
	#Black Khergit
	(troop_set_slot, troop_trees_1, slot_bandit_black_khergit_horseman, "trp_bandit_r_black_khergit_horseman"),
	#Slavers
	(troop_set_slot, troop_trees_1, slot_bandit_manhunter, "trp_bandit_r_manhunter"),
	(troop_set_slot, troop_trees_1, slot_bandit_slave_driver, "trp_bandit_r_slave_driver"),
	(troop_set_slot, troop_trees_1, slot_bandit_slave_hunter, "trp_bandit_r_slave_hunter"),
	(troop_set_slot, troop_trees_1, slot_bandit_slave_crusher, "trp_bandit_r_slave_crusher"),
	(troop_set_slot, troop_trees_1, slot_bandit_slaver_chief, "trp_bandit_r_slaver_chief"),
	##Expanded
	#Looters
	(troop_set_slot, troop_trees_2, slot_bandit_looter, "trp_bandit_e_looter"),
	(troop_set_slot, troop_trees_2, slot_bandit_bandit, "trp_bandit_e_bandit"),
	(troop_set_slot, troop_trees_2, slot_bandit_brigand, "trp_bandit_e_brigand"),
	#Bandits
	(troop_set_slot, troop_trees_2, slot_bandit_mountain, "trp_bandit_e_mountain"),
	(troop_set_slot, troop_trees_2, slot_bandit_forest, "trp_bandit_e_forest"),
	(troop_set_slot, troop_trees_2, slot_bandit_sea_raider, "trp_bandit_e_sea_raider"),
	(troop_set_slot, troop_trees_2, slot_bandit_steppe, "trp_bandit_e_steppe"),
	(troop_set_slot, troop_trees_2, slot_bandit_taiga, "trp_bandit_e_taiga"),
	(troop_set_slot, troop_trees_2, slot_bandit_desert, "trp_bandit_e_desert"),
	#Black Khergit
	(troop_set_slot, troop_trees_2, slot_bandit_black_khergit_horseman, "trp_bandit_e_black_khergit_horseman"),
	#Slavers
	(troop_set_slot, troop_trees_2, slot_bandit_manhunter, "trp_bandit_e_manhunter"),
	(troop_set_slot, troop_trees_2, slot_bandit_slave_driver, "trp_bandit_e_slave_driver"),
	(troop_set_slot, troop_trees_2, slot_bandit_slave_hunter, "trp_bandit_e_slave_hunter"),
	(troop_set_slot, troop_trees_2, slot_bandit_slave_crusher, "trp_bandit_e_slave_crusher"),
	(troop_set_slot, troop_trees_2, slot_bandit_slaver_chief, "trp_bandit_e_slaver_chief"),
	###Women
	##Native
	#Tier 1
	(troop_set_slot, troop_trees_0, slot_woman_refugee, "trp_woman_n_refugee"),
	(troop_set_slot, troop_trees_0, slot_woman_peasant, "trp_woman_n_peasant"),
	#Tier 2
	(troop_set_slot, troop_trees_0, slot_woman_militia, "trp_woman_n_camp_follower"),
	(troop_set_slot, troop_trees_0, slot_woman_camp_follower, "trp_woman_n_camp_follower"),
	(troop_set_slot, troop_trees_0, slot_woman_dressed_up, "trp_woman_n_camp_follower"),
	#Tier 3
	(troop_set_slot, troop_trees_0, slot_woman_warrior, "trp_woman_n_huntress"),
	(troop_set_slot, troop_trees_0, slot_woman_nurse, "trp_woman_n_huntress"),
	(troop_set_slot, troop_trees_0, slot_woman_huntress, "trp_woman_n_huntress"),
	(troop_set_slot, troop_trees_0, slot_woman_stedinger, "trp_woman_n_huntress"),
	(troop_set_slot, troop_trees_0, slot_woman_hospitaller, "trp_woman_n_huntress"),
	#Tier 4
	(troop_set_slot, troop_trees_0, slot_woman_sword_sister, "trp_woman_n_maiden"),
	(troop_set_slot, troop_trees_0, slot_woman_truus_te_paard, "trp_woman_n_maiden"),
	(troop_set_slot, troop_trees_0, slot_woman_maiden, "trp_woman_n_maiden"),
	(troop_set_slot, troop_trees_0, slot_woman_markswoman, "trp_woman_n_maiden"),
	(troop_set_slot, troop_trees_0, slot_woman_mounted_markswoman, "trp_woman_n_maiden"),
	(troop_set_slot, troop_trees_0, slot_woman_kriegerin, "trp_woman_n_maiden"),
	(troop_set_slot, troop_trees_0, slot_woman_beritten_jungfrau, "trp_woman_n_maiden"),
	(troop_set_slot, troop_trees_0, slot_woman_jungfrau, "trp_woman_n_maiden"),
	#Tier 5
	(troop_set_slot, troop_trees_0, slot_woman_swob_ridder, "trp_woman_n_swob_ridder"),
	(troop_set_slot, troop_trees_0, slot_woman_femme_fatale, "trp_woman_n_swob_ridder"),
	(troop_set_slot, troop_trees_0, slot_woman_virago, "trp_woman_n_swob_ridder"),
	(troop_set_slot, troop_trees_0, slot_woman_amazon, "trp_woman_n_swob_ridder"),
	(troop_set_slot, troop_trees_0, slot_woman_schildmaid, "trp_woman_n_swob_ridder"),
	(troop_set_slot, troop_trees_0, slot_woman_schildjungfer, "trp_woman_n_swob_ridder"),
	#Tier 6
	(troop_set_slot, troop_trees_0, slot_woman_kenau, "trp_woman_n_swob_ridder"),
	(troop_set_slot, troop_trees_0, slot_woman_black_widow, "trp_woman_n_swob_ridder"),
	(troop_set_slot, troop_trees_0, slot_woman_walkure, "trp_woman_n_swob_ridder"),
	#Extra
	(troop_set_slot, troop_trees_0, slot_woman_extra1, "trp_woman_n_extra1"),
	(troop_set_slot, troop_trees_0, slot_woman_extra2, "trp_woman_n_extra2"),
	(troop_set_slot, troop_trees_0, slot_woman_extra3, "trp_woman_n_extra3"),
	(troop_set_slot, troop_trees_0, slot_woman_extra4, "trp_woman_n_extra4"),
	(troop_set_slot, troop_trees_0, slot_woman_extra5, "trp_woman_n_extra5"),
	##Reworked
	#Tier 1
	(troop_set_slot, troop_trees_1, slot_woman_refugee, "trp_woman_r_refugee"),
	(troop_set_slot, troop_trees_1, slot_woman_peasant, "trp_woman_r_peasant"),
	#Tier 2
	(troop_set_slot, troop_trees_1, slot_woman_militia, "trp_woman_r_militia"),
	(troop_set_slot, troop_trees_1, slot_woman_camp_follower, "trp_woman_r_camp_follower"),
	(troop_set_slot, troop_trees_1, slot_woman_dressed_up, "trp_woman_r_dressed_up"),
	#Tier 3
	(troop_set_slot, troop_trees_1, slot_woman_warrior, "trp_woman_r_warrior"),
	(troop_set_slot, troop_trees_1, slot_woman_nurse, "trp_woman_r_warrior"),
	(troop_set_slot, troop_trees_1, slot_woman_huntress, "trp_woman_r_huntress"),
	(troop_set_slot, troop_trees_1, slot_woman_stedinger, "trp_woman_r_stedinger"),
	(troop_set_slot, troop_trees_1, slot_woman_hospitaller, "trp_woman_r_stedinger"),
	#Tier 4
	(troop_set_slot, troop_trees_1, slot_woman_sword_sister, "trp_woman_r_truus_te_paard"),
	(troop_set_slot, troop_trees_1, slot_woman_truus_te_paard, "trp_woman_r_truus_te_paard"),
	(troop_set_slot, troop_trees_1, slot_woman_maiden, "trp_woman_r_markswoman"),
	(troop_set_slot, troop_trees_1, slot_woman_markswoman, "trp_woman_r_markswoman"),
	(troop_set_slot, troop_trees_1, slot_woman_mounted_markswoman, "trp_woman_r_mounted_markswoman"),
	(troop_set_slot, troop_trees_1, slot_woman_kriegerin, "trp_woman_r_kriegerin"),
	(troop_set_slot, troop_trees_1, slot_woman_beritten_jungfrau, "trp_woman_r_mounted_markswoman"),
	(troop_set_slot, troop_trees_1, slot_woman_jungfrau, "trp_woman_r_kriegerin"),
	#Tier 5
	(troop_set_slot, troop_trees_1, slot_woman_swob_ridder, "trp_woman_r_swob_ridder"),
	(troop_set_slot, troop_trees_1, slot_woman_femme_fatale, "trp_woman_r_swob_ridder"),
	(troop_set_slot, troop_trees_1, slot_woman_virago, "trp_woman_r_virago"),
	(troop_set_slot, troop_trees_1, slot_woman_amazon, "trp_woman_r_amazon"),
	(troop_set_slot, troop_trees_1, slot_woman_schildmaid, "trp_woman_r_schildmaid"),
	(troop_set_slot, troop_trees_1, slot_woman_schildjungfer, "trp_woman_r_schildmaid"),
	#Tier 6
	(troop_set_slot, troop_trees_1, slot_woman_kenau, "trp_woman_r_swob_ridder"),
	(troop_set_slot, troop_trees_1, slot_woman_black_widow, "trp_woman_r_virago"),
	(troop_set_slot, troop_trees_1, slot_woman_walkure, "trp_woman_r_amazon"),
	#Extra
	(troop_set_slot, troop_trees_1, slot_woman_extra1, "trp_woman_r_extra1"),
	(troop_set_slot, troop_trees_1, slot_woman_extra2, "trp_woman_r_extra2"),
	(troop_set_slot, troop_trees_1, slot_woman_extra3, "trp_woman_r_extra3"),
	(troop_set_slot, troop_trees_1, slot_woman_extra4, "trp_woman_r_extra4"),
	(troop_set_slot, troop_trees_1, slot_woman_extra5, "trp_woman_r_extra5"),
	##Expanded
	#Tier 1
	(troop_set_slot, troop_trees_2, slot_woman_refugee, "trp_woman_e_refugee"),
	(troop_set_slot, troop_trees_2, slot_woman_peasant, "trp_woman_e_peasant"),
	#Tier 2
	(troop_set_slot, troop_trees_2, slot_woman_militia, "trp_woman_e_militia"),
	(troop_set_slot, troop_trees_2, slot_woman_camp_follower, "trp_woman_e_camp_follower"),
	(troop_set_slot, troop_trees_2, slot_woman_dressed_up, "trp_woman_e_dressed_up"),
	#Tier 3
	(troop_set_slot, troop_trees_2, slot_woman_warrior, "trp_woman_e_warrior"),
	(troop_set_slot, troop_trees_2, slot_woman_nurse, "trp_woman_e_nurse"),
	(troop_set_slot, troop_trees_2, slot_woman_huntress, "trp_woman_e_huntress"),
	(troop_set_slot, troop_trees_2, slot_woman_stedinger, "trp_woman_e_stedinger"),
	(troop_set_slot, troop_trees_2, slot_woman_hospitaller, "trp_woman_e_hospitaller"),
	#Tier 4
	(troop_set_slot, troop_trees_2, slot_woman_sword_sister, "trp_woman_e_sword_sister"),
	(troop_set_slot, troop_trees_2, slot_woman_truus_te_paard, "trp_woman_e_truus_te_paard"),
	(troop_set_slot, troop_trees_2, slot_woman_maiden, "trp_woman_e_maiden"),
	(troop_set_slot, troop_trees_2, slot_woman_markswoman, "trp_woman_e_markswoman"),
	(troop_set_slot, troop_trees_2, slot_woman_mounted_markswoman, "trp_woman_e_mounted_markswoman"),
	(troop_set_slot, troop_trees_2, slot_woman_kriegerin, "trp_woman_e_kriegerin"),
	(troop_set_slot, troop_trees_2, slot_woman_beritten_jungfrau, "trp_woman_e_beritten_jungfrau"),
	(troop_set_slot, troop_trees_2, slot_woman_jungfrau, "trp_woman_e_jungfrau"),
	#Tier 5
	(troop_set_slot, troop_trees_2, slot_woman_swob_ridder, "trp_woman_e_swob_ridder"),
	(troop_set_slot, troop_trees_2, slot_woman_femme_fatale, "trp_woman_e_femme_fatale"),
	(troop_set_slot, troop_trees_2, slot_woman_virago, "trp_woman_e_virago"),
	(troop_set_slot, troop_trees_2, slot_woman_amazon, "trp_woman_e_amazon"),
	(troop_set_slot, troop_trees_2, slot_woman_schildmaid, "trp_woman_e_schildmaid"),
	(troop_set_slot, troop_trees_2, slot_woman_schildjungfer, "trp_woman_e_schildjungfer"),
	#Tier 6
	(troop_set_slot, troop_trees_2, slot_woman_kenau, "trp_woman_e_kenau"),
	(troop_set_slot, troop_trees_2, slot_woman_black_widow, "trp_woman_e_black_widow"),
	(troop_set_slot, troop_trees_2, slot_woman_walkure, "trp_woman_e_walkure"),
	#Extra
	(troop_set_slot, troop_trees_2, slot_woman_extra1, "trp_woman_e_extra1"),
	(troop_set_slot, troop_trees_2, slot_woman_extra2, "trp_woman_e_extra2"),
	(troop_set_slot, troop_trees_2, slot_woman_extra3, "trp_woman_e_extra3"),
	(troop_set_slot, troop_trees_2, slot_woman_extra4, "trp_woman_e_extra4"),
	(troop_set_slot, troop_trees_2, slot_woman_extra5, "trp_woman_e_extra5"),
	
    ]),
	##Floris MTT end

##Floris MTT: Multiple Troop Trees Fix Begin
  ("initialize_troop_tree_sets",
	[
	(try_for_range, ":unused", 0, 10),
        (call_script, "script_spawn_bandits"),
    (try_end),
	
	(call_script, "script_start_update_mercenary_units_of_towns"),
	(call_script, "script_update_ranger_master"),
	(set_relation, "fac_outlaws", "fac_player_faction", -10),
	(set_relation, "fac_outlaws", "fac_player_supporters_faction", -10),
	
	(try_for_parties, ":party_no"),
		(party_get_template_id, ":template", ":party_no"),
	##Correct the party templates
		(try_begin),
			(eq, "$troop_trees", troop_trees_0),
			(try_begin),
				(eq, ":template", "pt_village_defenders_e"),
				(spawn_around_party, ":party_no", "pt_village_defenders"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_looters_e"),
				(spawn_around_party, ":party_no", "pt_looters"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_forest_bandits_e"),
				(spawn_around_party, ":party_no", "pt_forest_bandits"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_steppe_bandits_e"),
				(spawn_around_party, ":party_no", "pt_steppe_bandits"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_sea_raiders_e"),
				(spawn_around_party, ":party_no", "pt_sea_raiders"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_mountain_bandits_e"),
				(spawn_around_party, ":party_no", "pt_mountain_bandits"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_desert_bandits_e"),
				(spawn_around_party, ":party_no", "pt_desert_bandits"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_steppe_bandit_lair_e"),
				(spawn_around_party, ":party_no", "pt_steppe_bandit_lair"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_taiga_bandit_lair_e"),
				(spawn_around_party, ":party_no", "pt_taiga_bandit_lair"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_desert_bandit_lair_e"),
				(spawn_around_party, ":party_no", "pt_desert_bandit_lair"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_forest_bandit_lair_e"),
				(spawn_around_party, ":party_no", "pt_forest_bandit_lair"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_mountain_bandit_lair_e"),
				(spawn_around_party, ":party_no", "pt_mountain_bandit_lair"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_sea_raider_lair_e"),
				(spawn_around_party, ":party_no", "pt_sea_raider_lair"),
				(remove_party, ":party_no"),
			(try_end),
		(else_try),
			(eq, "$troop_trees", troop_trees_1),
			(try_begin),
				(eq, ":template", "pt_village_defenders_e"),
				(spawn_around_party, ":party_no", "pt_village_defenders_r"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_looters_e"),
				(spawn_around_party, ":party_no", "pt_looters_r"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_forest_bandits_e"),
				(spawn_around_party, ":party_no", "pt_forest_bandits_r"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_steppe_bandits_e"),
				(spawn_around_party, ":party_no", "pt_steppe_bandits_r"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_sea_raiders_e"),
				(spawn_around_party, ":party_no", "pt_sea_raiders_r"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_mountain_bandits_e"),
				(spawn_around_party, ":party_no", "pt_mountain_bandits_r"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_desert_bandits_e"),
				(spawn_around_party, ":party_no", "pt_desert_bandits_r"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_steppe_bandit_lair_e"),
				(spawn_around_party, ":party_no", "pt_steppe_bandit_lair_r"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_taiga_bandit_lair_e"),
				(spawn_around_party, ":party_no", "pt_taiga_bandit_lair_r"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_desert_bandit_lair_e"),
				(spawn_around_party, ":party_no", "pt_desert_bandit_lair_r"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_forest_bandit_lair_e"),
				(spawn_around_party, ":party_no", "pt_forest_bandit_lair_r"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_mountain_bandit_lair_e"),
				(spawn_around_party, ":party_no", "pt_mountain_bandit_lair_r"),
				(remove_party, ":party_no"),
			(else_try),
				(eq, ":template", "pt_sea_raider_lair_e"),
				(spawn_around_party, ":party_no", "pt_sea_raider_lair_r"),
				(remove_party, ":party_no"),
			(try_end),
		(else_try),
			(eq, "$troop_trees", troop_trees_2),
		(try_end),		
	(try_end),	
	
	## Correct the culture and faction slots
	(try_begin),
		(eq, "$troop_trees", troop_trees_0),	  
        # Cultures:
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_1_troop, "trp_swadian_n_peasant"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_2_troop, "trp_swadian_n_militia"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_3_troop, "trp_swadian_n_page"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_4_troop, "trp_swadian_n_ecuyer"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_5_troop, "trp_swadian_n_chevalier"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_6_troop, "trp_swadian_n_chevalier"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_7_troop, "trp_swadian_n_chevalier"),
		  
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_1_troop, "trp_vaegir_n_kholop"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_2_troop, "trp_vaegir_n_otrok"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_3_troop, "trp_vaegir_n_kazak"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_4_troop, "trp_vaegir_n_yesaul"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_5_troop, "trp_vaegir_n_pansirniy_kazan"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_6_troop, "trp_vaegir_n_pansirniy_kazan"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_7_troop, "trp_vaegir_n_pansirniy_kazan"),
		  
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_1_troop, "trp_khergit_n_tariachin"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_2_troop, "trp_khergit_n_qarbughaci"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_3_troop, "trp_khergit_n_morici"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_4_troop, "trp_khergit_n_kipchak"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_5_troop, "trp_khergit_n_borjigin"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_6_troop, "trp_khergit_n_borjigin"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_7_troop, "trp_khergit_n_borjigin"),
		  
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_1_troop, "trp_nord_n_bondi"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_2_troop, "trp_nord_n_gesith"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_3_troop, "trp_nord_n_bogmadur"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_4_troop, "trp_nord_n_vigamadr"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_5_troop, "trp_nord_n_skjadsveinn"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_6_troop, "trp_nord_n_husbondi"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_7_troop, "trp_nord_n_husbondi"),
		  
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_1_troop, "trp_rhodok_n_cittadino"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_2_troop, "trp_rhodok_n_novizio"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_3_troop, "trp_rhodok_n_milizia"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_4_troop, "trp_rhodok_n_fante"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_5_troop, "trp_rhodok_n_fante"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_6_troop, "trp_rhodok_n_fante"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_7_troop, "trp_rhodok_n_fante"),
		  
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_1_troop, "trp_sarranid_n_millet"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_2_troop, "trp_sarranid_n_ajam"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_3_troop, "trp_sarranid_n_cemaat"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_4_troop, "trp_sarranid_n_timariot"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_5_troop, "trp_sarranid_n_kapikula"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_6_troop, "trp_sarranid_n_yeniceri"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_7_troop, "trp_sarranid_n_kapikula"),

		  #Player Faction
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_1_troop, "trp_custom_n_recruit"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_2_troop, "trp_custom_n_militia"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_3_troop, "trp_custom_n_guard"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_4_troop, "trp_custom_n_swordman"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_5_troop, "trp_custom_n_swordmaster"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_6_troop, "trp_custom_n_knight"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_7_troop, "trp_custom_n_knight"),
		  #Player Faction
		  
      (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_get_slot, ":culture", ":faction_no", slot_faction_culture),
        
        (faction_get_slot, ":troop", ":culture",  slot_faction_tier_1_troop),
        (faction_set_slot, ":faction_no",  slot_faction_tier_1_troop, ":troop"),
        (faction_get_slot, ":troop", ":culture",  slot_faction_tier_2_troop),
        (faction_set_slot, ":faction_no",  slot_faction_tier_2_troop, ":troop"),
        (faction_get_slot, ":troop", ":culture",  slot_faction_tier_3_troop),
        (faction_set_slot, ":faction_no",  slot_faction_tier_3_troop, ":troop"),
        (faction_get_slot, ":troop", ":culture",  slot_faction_tier_4_troop),
        (faction_set_slot, ":faction_no",  slot_faction_tier_4_troop, ":troop"),
        (faction_get_slot, ":troop", ":culture",  slot_faction_tier_5_troop),
        (faction_set_slot, ":faction_no",  slot_faction_tier_5_troop, ":troop"),
        
        (try_begin),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_1"),
          
          (faction_set_slot, ":faction_no",  slot_faction_deserter_troop, "trp_swadian_deserter"),
          (faction_set_slot, ":faction_no",  slot_faction_guard_troop, "trp_swadian_n_jacobite"),
          (faction_set_slot, ":faction_no",  slot_faction_messenger_troop, "trp_swadian_messenger"),
          (faction_set_slot, ":faction_no",  slot_faction_prison_guard_troop, "trp_swadian_prison_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_castle_guard_troop, "trp_swadian_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_1_reinforcements_a"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_1_reinforcements_b"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_1_reinforcements_c"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_1_reinforcements_d"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_1_reinforcements_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_1_reinforcements_f"),
        (else_try),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_2"),
          
          (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_vaegir_deserter"),
          (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_vaegir_n_plastun"),
          (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_vaegir_messenger"),
          (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_vaegir_prison_guard"),
          (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_vaegir_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_2_reinforcements_a"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_2_reinforcements_b"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_2_reinforcements_c"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_2_reinforcements_d"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_2_reinforcements_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_2_reinforcements_f"),
        (else_try),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_3"),
          
          (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_khergit_deserter"),
          (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_khergit_n_qubuci"),
          (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_khergit_messenger"),
          (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_khergit_prison_guard"),
          (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_khergit_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_3_reinforcements_a"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_3_reinforcements_b"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_3_reinforcements_c"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_3_reinforcements_d"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_3_reinforcements_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_3_reinforcements_f"),
        (else_try),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_4"),
          
          (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_nord_deserter"),
          (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_nord_n_bogsveigir"),
          (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_nord_messenger"),
          (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_nord_prison_guard"),
          (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_nord_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_4_reinforcements_a"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_4_reinforcements_b"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_4_reinforcements_c"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_4_reinforcements_d"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_4_reinforcements_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_4_reinforcements_f"),
        (else_try),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_5"),
          
          (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_rhodok_deserter"),
          (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_rhodok_n_fante"),
          (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_rhodok_messenger"),
          (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_rhodok_prison_guard"),
          (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_rhodok_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_5_reinforcements_a"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_5_reinforcements_b"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_5_reinforcements_c"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_5_reinforcements_d"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_5_reinforcements_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_5_reinforcements_f"),
        (else_try),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_6"),
          
          (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_sarranid_deserter"),
          (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_sarranid_n_timariot"),
          (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_sarranid_messenger"),
          (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_sarranid_prison_guard"),
          (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_sarranid_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_6_reinforcements_a"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_6_reinforcements_b"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_6_reinforcements_c"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_6_reinforcements_d"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_6_reinforcements_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_6_reinforcements_f"),

          #Player Faction
		(else_try),
			(faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_7"),

			(faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_custom_deserter"),
			(faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_custom_n_swordman"),
			(faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_custom_messenger"),
			(faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_custom_prison_guard"),
			(faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_custom_castle_guard"),
			(faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_7_reinforcements_a"),
			(faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_7_reinforcements_b"),
			(faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_7_reinforcements_c"),
			(faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_7_reinforcements_d"),
			(faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_7_reinforcements_e"),
			(faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_7_reinforcements_f"),
          #Player Faction
        (try_end),
      (try_end),		  
	(else_try),
		(eq, "$troop_trees", troop_trees_1),
# Cultures:
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_1_troop, "trp_swadian_r_peasant"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_2_troop, "trp_swadian_r_militia"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_3_troop, "trp_swadian_r_sergeant_at_arms"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_4_troop, "trp_swadian_r_piquier"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_5_troop, "trp_swadian_r_chevalier"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_6_troop, "trp_swadian_r_chevalier_banneret"),
		  (faction_set_slot, "fac_culture_1",  slot_faction_tier_7_troop, "trp_swadian_r_chevalier_banneret"),
		  
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_1_troop, "trp_vaegir_r_kholop"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_2_troop, "trp_vaegir_r_otrok"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_3_troop, "trp_vaegir_r_kazak"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_4_troop, "trp_vaegir_r_yesaul"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_5_troop, "trp_vaegir_r_ataman"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_6_troop, "trp_vaegir_r_ataman"),
		  (faction_set_slot, "fac_culture_2", slot_faction_tier_7_troop, "trp_vaegir_r_ataman"),
		  
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_1_troop, "trp_khergit_r_tariachin"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_2_troop, "trp_khergit_r_tsereg"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_3_troop, "trp_khergit_r_morici"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_4_troop, "trp_khergit_r_kipchak"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_5_troop, "trp_khergit_r_khevtuul"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_6_troop, "trp_khergit_r_khevtuul"),
		  (faction_set_slot, "fac_culture_3", slot_faction_tier_7_troop, "trp_khergit_r_keshig"),
		  
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_1_troop, "trp_nord_r_bondi"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_2_troop, "trp_nord_r_berserkr"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_3_troop, "trp_nord_r_kertilsveinr"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_4_troop, "trp_nord_r_vikingr"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_5_troop, "trp_nord_r_skjadsveinn"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_6_troop, "trp_nord_r_skjadsveinn"),
		  (faction_set_slot, "fac_culture_4", slot_faction_tier_7_troop, "trp_nord_r_skjadsveinn"),
		  
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_1_troop, "trp_rhodok_r_cittadino"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_2_troop, "trp_rhodok_r_novizio"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_3_troop, "trp_rhodok_r_lanciere_a_cavallo"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_4_troop, "trp_rhodok_r_lanza_spezzata"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_5_troop, "trp_rhodok_r_picchiere_veterano"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_6_troop, "trp_rhodok_r_picchiere_veterano"),
		  (faction_set_slot, "fac_culture_5", slot_faction_tier_7_troop, "trp_rhodok_r_picchiere_veterano"),
		  
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_1_troop, "trp_sarranid_r_millet"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_2_troop, "trp_sarranid_r_ajam"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_3_troop, "trp_sarranid_r_azab"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_4_troop, "trp_sarranid_r_al_haqa"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_5_troop, "trp_sarranid_r_kapikula"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_6_troop, "trp_sarranid_r_kapikula"),
		  (faction_set_slot, "fac_culture_6", slot_faction_tier_7_troop, "trp_sarranid_r_yeniceri"),

		  #Player Faction
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_1_troop, "trp_custom_r_recruit"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_2_troop, "trp_custom_r_militia"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_3_troop, "trp_custom_r_guard"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_4_troop, "trp_custom_r_swordman"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_5_troop, "trp_custom_r_swordmaster"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_6_troop, "trp_custom_r_knight"),
		  (faction_set_slot, "fac_culture_7",  slot_faction_tier_7_troop, "trp_custom_r_knight"),
		  #Player Faction
      
      (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_get_slot, ":culture", ":faction_no", slot_faction_culture),
        
        (faction_get_slot, ":troop", ":culture",  slot_faction_tier_1_troop),
        (faction_set_slot, ":faction_no",  slot_faction_tier_1_troop, ":troop"),
        (faction_get_slot, ":troop", ":culture",  slot_faction_tier_2_troop),
        (faction_set_slot, ":faction_no",  slot_faction_tier_2_troop, ":troop"),
        (faction_get_slot, ":troop", ":culture",  slot_faction_tier_3_troop),
        (faction_set_slot, ":faction_no",  slot_faction_tier_3_troop, ":troop"),
        (faction_get_slot, ":troop", ":culture",  slot_faction_tier_4_troop),
        (faction_set_slot, ":faction_no",  slot_faction_tier_4_troop, ":troop"),
        (faction_get_slot, ":troop", ":culture",  slot_faction_tier_5_troop),
        (faction_set_slot, ":faction_no",  slot_faction_tier_5_troop, ":troop"),
        
        (try_begin),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_1"),
          
          (faction_set_slot, ":faction_no",  slot_faction_deserter_troop, "trp_swadian_deserter"),
          (faction_set_slot, ":faction_no",  slot_faction_guard_troop, "trp_swadian_r_hobilar"),
          (faction_set_slot, ":faction_no",  slot_faction_messenger_troop, "trp_swadian_messenger"),
          (faction_set_slot, ":faction_no",  slot_faction_prison_guard_troop, "trp_swadian_prison_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_castle_guard_troop, "trp_swadian_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_1_reinforcements_a_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_1_reinforcements_b_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_1_reinforcements_c_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_1_reinforcements_d_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_1_reinforcements_e_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_1_reinforcements_f_r"),
        (else_try),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_2"),
          
          (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_vaegir_deserter"),
          (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_vaegir_r_plastun"),
          (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_vaegir_messenger"),
          (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_vaegir_prison_guard"),
          (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_vaegir_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_2_reinforcements_a_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_2_reinforcements_b_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_2_reinforcements_c_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_2_reinforcements_d_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_2_reinforcements_e_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_2_reinforcements_f_r"),
        (else_try),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_3"),
          
          (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_khergit_deserter"),
          (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_khergit_r_aqala_asud"),
          (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_khergit_messenger"),
          (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_khergit_prison_guard"),
          (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_khergit_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_3_reinforcements_a_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_3_reinforcements_b_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_3_reinforcements_c_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_3_reinforcements_d_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_3_reinforcements_e_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_3_reinforcements_f_r"),
        (else_try),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_4"),
          
          (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_nord_deserter"),
          (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_nord_r_vigamadr"),
          (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_nord_messenger"),
          (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_nord_prison_guard"),
          (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_nord_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_4_reinforcements_a_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_4_reinforcements_b_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_4_reinforcements_c_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_4_reinforcements_d_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_4_reinforcements_e_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_4_reinforcements_f_r"),
        (else_try),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_5"),
          
          (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_rhodok_deserter"),
          (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_rhodok_r_lanciere_veterano"),
          (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_rhodok_messenger"),
          (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_rhodok_prison_guard"),
          (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_rhodok_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_5_reinforcements_a_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_5_reinforcements_b_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_5_reinforcements_c_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_5_reinforcements_d_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_5_reinforcements_e_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_5_reinforcements_f_r"),
        (else_try),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_6"),
          
          (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_sarranid_deserter"),
          (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_sarranid_r_al_haqa"),
          (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_sarranid_messenger"),
          (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_sarranid_prison_guard"),
          (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_sarranid_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_6_reinforcements_a_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_6_reinforcements_b_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_6_reinforcements_c_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_6_reinforcements_d_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_6_reinforcements_e_r"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_6_reinforcements_f_r"),

          #Player Faction
		(else_try),
			(faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_7"),

			(faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_custom_deserter"),
			(faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_custom_r_swordman"),
			(faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_custom_messenger"),
			(faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_custom_prison_guard"),
			(faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_custom_castle_guard"),
			(faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_7_reinforcements_a_r"),
			(faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_7_reinforcements_b_r"),
			(faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_7_reinforcements_c_r"),
			(faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_7_reinforcements_d_r"),
			(faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_7_reinforcements_e_r"),
			(faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_7_reinforcements_f_r"),
          #Player Faction
        (try_end),
      (try_end),				
	(else_try),
		(eq, "$troop_trees", troop_trees_2),
		#nothing necessary, default
	(try_end),
	
	(try_for_range, ":village_no", villages_begin, villages_end),
		(call_script, "script_update_volunteer_troops_in_village", ":village_no"),
    (try_end),
	
	
    # Towns (loop)
    (try_for_range, ":town_no", towns_begin, towns_end),
		(try_begin),
			(eq, "$troop_trees", troop_trees_0),
			(party_set_slot,":town_no", slot_town_reinforcement_party_template, "pt_center_reinforcements"),
		(else_try),
			(eq, "$troop_trees", troop_trees_1),
			(party_set_slot,":town_no", slot_town_reinforcement_party_template, "pt_center_reinforcements_r"),
		(else_try),
			(eq, "$troop_trees", troop_trees_2),
			(party_set_slot,":town_no", slot_town_reinforcement_party_template, "pt_center_reinforcements_e"),
		(try_end),
    (try_end),
      
      # Castles
    (try_for_range, ":castle_no", castles_begin, castles_end),
		(try_begin),
			(eq, "$troop_trees", troop_trees_0),
			(party_set_slot,":castle_no", slot_town_reinforcement_party_template, "pt_center_reinforcements"),
		(else_try),
			(eq, "$troop_trees", troop_trees_1),
			(party_set_slot,":castle_no", slot_town_reinforcement_party_template, "pt_center_reinforcements_r"),
		(else_try),
			(eq, "$troop_trees", troop_trees_2),
			(party_set_slot,":castle_no", slot_town_reinforcement_party_template, "pt_center_reinforcements_e"),
		(try_end),
    (try_end),

	## Correct the troops
	(try_for_parties, ":party_no"),
		(party_is_active, ":party_no"),										#added to avoid invalid parties // do inactive parties have to be reset? if so an else_try to seperate them from active parties should suffice, set them active, exchange things, then set them inactive again
		(party_get_num_companion_stacks, ":range", ":party_no"),
		(try_for_range_backwards, ":stack_no", 0, ":range"),
			(party_stack_get_troop_id, ":troop_no", ":party_no", ":stack_no"),
			(neg|troop_is_hero, ":troop_no"),
			(party_stack_get_size, ":size", ":party_no", ":stack_no"),
			(try_for_range, ":troop_slot", mtt_troop_slots_begin, mtt_troop_slots_end),
				(troop_slot_eq, troop_trees_2, ":troop_slot", ":troop_no"), #this troop, since default is troop_trees_2
				(troop_get_slot, ":new_troop", "$troop_trees", ":troop_slot"),
				(neg|troop_slot_eq, troop_trees_2, ":troop_slot", ":new_troop"),				
				(party_remove_members, ":party_no", ":troop_no", ":size"),
				(party_add_members, ":party_no", ":new_troop", ":size"),
			(try_end), #Troop loop
		(try_end), #Stack loop	
 	(try_end), #Party Loop	
	
	]),
## Floris: Multiple Troop Trees Fix End

  #script_game_get_use_string
  # This script is called from the game engine for getting using information text
  # INPUT: used_scene_prop_id
  # OUTPUT: s0
  ("game_get_use_string",
    [
      (store_script_param, ":instance_id", 1),
      
      (prop_instance_get_scene_prop_kind, ":scene_prop_id", ":instance_id"),
      
      (try_begin),
        (this_or_next|eq, ":scene_prop_id", "spr_winch_b"),
        (eq, ":scene_prop_id", "spr_winch"),
        (assign, ":effected_object", "spr_portcullis"),
      (else_try),
        (this_or_next|eq, ":scene_prop_id", "spr_door_destructible"),
        (this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_b"),
        (this_or_next|eq, ":scene_prop_id", "spr_castle_e_sally_door_a"),
        (this_or_next|eq, ":scene_prop_id", "spr_castle_f_sally_door_a"),
        (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_left"),
        (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_right"),
        (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),
        (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_right"),
        (this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_a"),
        (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_6m"),
        (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_8m"),
        (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_10m"),
        (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_12m"),
        (eq, ":scene_prop_id", "spr_siege_ladder_move_14m"),
        (assign, ":effected_object", ":scene_prop_id"),
      (try_end),
      
      (scene_prop_get_slot, ":item_situation", ":instance_id", scene_prop_open_or_close_slot),
      
      (try_begin), #opening/closing portcullis
        (eq, ":effected_object", "spr_portcullis"),
        
        (try_begin),
          (eq, ":item_situation", 0),
          (str_store_string, s0, "str_open_gate"),
        (else_try),
          (str_store_string, s0, "str_close_gate"),
        (try_end),
      (else_try), #opening/closing door
        (this_or_next|eq, ":effected_object", "spr_door_destructible"),
        (this_or_next|eq, ":effected_object", "spr_castle_f_door_b"),
        (this_or_next|eq, ":effected_object", "spr_castle_e_sally_door_a"),
        (this_or_next|eq, ":effected_object", "spr_castle_f_sally_door_a"),
        (this_or_next|eq, ":effected_object", "spr_earth_sally_gate_left"),
        (this_or_next|eq, ":effected_object", "spr_earth_sally_gate_right"),
        (this_or_next|eq, ":effected_object", "spr_viking_keep_destroy_sally_door_left"),
        (this_or_next|eq, ":effected_object", "spr_viking_keep_destroy_sally_door_right"),
        (eq, ":effected_object", "spr_castle_f_door_a"),
        
        (try_begin),
          (eq, ":item_situation", 0),
          (str_store_string, s0, "str_open_door"),
        (else_try),
          (str_store_string, s0, "str_close_door"),
        (try_end),
      (else_try), #raising/dropping ladder
        (try_begin),
          (eq, ":item_situation", 0),
          (str_store_string, s0, "str_raise_ladder"),
        (else_try),
          (str_store_string, s0, "str_drop_ladder"),
        (try_end),
      (try_end),
  ]),
  
  #script_game_quick_start
  # This script is called from the game engine for initializing the global variables for tutorial, multiplayer and custom battle modes.
  # INPUT:
  # none
  # OUTPUT:
  # none
  ("game_quick_start",
    [
      #for quick battle mode
      (assign, "$g_is_quick_battle", 0),
      (assign, "$g_quick_battle_game_type", 0),
      (assign, "$g_quick_battle_troop", quick_battle_troops_begin),
      (assign, "$g_quick_battle_map", quick_battle_scenes_begin),
      (assign, "$g_quick_battle_team_1_faction", "fac_kingdom_1"),
      (assign, "$g_quick_battle_team_2_faction", "fac_kingdom_2"),
      (assign, "$g_quick_battle_army_1_size", 25),
      (assign, "$g_quick_battle_army_2_size", 25),
      
		  (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_1_infantry, "trp_bandit_e_mountain"),
		  (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_2_infantry, "trp_bandit_e_sea_raider"),
		  (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_1_archer, "trp_bandit_e_forest"),
		  (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_2_archer, "trp_bandit_e_taiga"),
		  (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_1_cavalry, "trp_bandit_e_steppe"),
		  (faction_set_slot, "fac_outlaws", slot_faction_quick_battle_tier_2_cavalry, "trp_bandit_e_desert"),
		  (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_1_infantry, "trp_swadian_e_vougier"),
		  (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_2_infantry, "trp_swadian_e_jock"),
		  (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_1_archer, "trp_swadian_e_archer_militia"),
		  (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_2_archer, "trp_swadian_e_sheriff"),
		  (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_1_cavalry, "trp_swadian_e_man_at_arms"),
		  (faction_set_slot, "fac_kingdom_1", slot_faction_quick_battle_tier_2_cavalry, "trp_swadian_e_chevalier_banneret"),
		  (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_1_infantry, "trp_vaegir_e_kazak"),
		  (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_2_infantry, "trp_vaegir_e_druzhinnik_veteran"),
		  (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_1_archer, "trp_vaegir_e_kmet"),
		  (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_2_archer, "trp_vaegir_e_luchnik"),
		  (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_1_cavalry, "trp_vaegir_e_ratnik"),
		  (faction_set_slot, "fac_kingdom_2", slot_faction_quick_battle_tier_2_cavalry, "trp_vaegir_e_vityas"),
		  (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_1_infantry, "trp_khergit_e_asud"),
		  (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_2_infantry, "trp_khergit_e_yabagharu_morici"),
		  (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_1_archer, "trp_khergit_e_surcin"),
		  (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_2_archer, "trp_khergit_e_aqala_teriguci"),
		  (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_1_cavalry, "trp_khergit_e_kipchak"),
		  (faction_set_slot, "fac_kingdom_3", slot_faction_quick_battle_tier_2_cavalry, "trp_khergit_e_aqata_borjigin"),
		  (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_1_infantry, "trp_nord_e_gridman"),
		  (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_2_infantry, "trp_nord_e_kappi"),
		  (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_1_archer, "trp_nord_e_bogmadur"),
		  (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_2_archer, "trp_nord_e_heimthegi"),
		  (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_1_cavalry, "trp_nord_e_innaesmaen"),
		  (faction_set_slot, "fac_kingdom_4", slot_faction_quick_battle_tier_2_cavalry, "trp_nord_e_skutilsveinr"),
		  (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_1_infantry, "trp_rhodok_e_lanciere"),
		  (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_2_infantry, "trp_rhodok_e_veterano"),
		  (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_1_archer, "trp_rhodok_e_milizia_balestriere"),
		  (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_2_archer, "trp_rhodok_e_balestriere"),
		  (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_1_cavalry, "trp_rhodok_e_lanciere_a_cavallo"),
		  (faction_set_slot, "fac_kingdom_5", slot_faction_quick_battle_tier_2_cavalry, "trp_rhodok_e_picchiere_fiammingo"),
		  (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_1_infantry, "trp_sarranid_e_azab"),
		  (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_2_infantry, "trp_sarranid_e_yeniceri"),
		  (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_1_archer, "trp_sarranid_e_jebelus"),
		  (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_2_archer, "trp_sarranid_e_uluteci"),
		  (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_1_cavalry, "trp_sarranid_e_badw"),
		  (faction_set_slot, "fac_kingdom_6", slot_faction_quick_battle_tier_2_cavalry, "trp_sarranid_e_memluk"),
		
      #Player Faction
          (faction_set_slot, "fac_player_supporters_faction", slot_faction_quick_battle_tier_1_infantry, "trp_custom_e_swordman"),
          (faction_set_slot, "fac_player_supporters_faction", slot_faction_quick_battle_tier_2_infantry, "trp_custom_e_swordmaster"),
          (faction_set_slot, "fac_player_supporters_faction", slot_faction_quick_battle_tier_1_archer, "trp_custom_e_archer"),
          (faction_set_slot, "fac_player_supporters_faction", slot_faction_quick_battle_tier_2_archer, "trp_custom_e_expert_archer"),
          (faction_set_slot, "fac_player_supporters_faction", slot_faction_quick_battle_tier_1_cavalry, "trp_custom_e_squire"),
          (faction_set_slot, "fac_player_supporters_faction", slot_faction_quick_battle_tier_2_cavalry, "trp_custom_e_knight"),
      #Player Faction
      
      #for multiplayer mode
      (assign, "$g_multiplayer_selected_map", multiplayer_scenes_begin),
      (assign, "$g_multiplayer_respawn_period", 5),
      (assign, "$g_multiplayer_round_max_seconds", 300),
      (assign, "$g_multiplayer_game_max_minutes", 30),
      (assign, "$g_multiplayer_game_max_points", 300),
      
      (server_get_renaming_server_allowed, "$g_multiplayer_renaming_server_allowed"),
      (server_get_changing_game_type_allowed, "$g_multiplayer_changing_game_type_allowed"),
      (assign, "$g_multiplayer_point_gained_from_flags", 100),
      (assign, "$g_multiplayer_point_gained_from_capturing_flag", 5),
      (assign, "$g_multiplayer_game_type", 0),
      (assign, "$g_multiplayer_team_1_faction", "fac_kingdom_1"),
      (assign, "$g_multiplayer_team_2_faction", "fac_kingdom_2"),
      (assign, "$g_multiplayer_next_team_1_faction", "$g_multiplayer_team_1_faction"),
      (assign, "$g_multiplayer_next_team_2_faction", "$g_multiplayer_team_2_faction"),
      (assign, "$g_multiplayer_num_bots_team_1", 0),
      (assign, "$g_multiplayer_num_bots_team_2", 0),
      (assign, "$g_multiplayer_number_of_respawn_count", 0),
      (assign, "$g_multiplayer_num_bots_voteable", 50),
      (assign, "$g_multiplayer_max_num_bots", 101),
      (assign, "$g_multiplayer_factions_voteable", 1),
      (assign, "$g_multiplayer_maps_voteable", 1),
      (assign, "$g_multiplayer_kick_voteable", 1),
      (assign, "$g_multiplayer_ban_voteable", 1),
      (assign, "$g_multiplayer_valid_vote_ratio", 51), #more than 50 percent
      (assign, "$g_multiplayer_auto_team_balance_limit", 3), #auto balance when difference is more than 2
      (assign, "$g_multiplayer_player_respawn_as_bot", 1),
      (assign, "$g_multiplayer_stats_chart_opened_manually", 0),
      (assign, "$g_multiplayer_mission_end_screen", 0),
      (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
      (assign, "$g_multiplayer_welcome_message_shown", 0),
      (assign, "$g_multiplayer_allow_player_banners", 1),
      (assign, "$g_multiplayer_force_default_armor", 1),
      (assign, "$g_multiplayer_disallow_ranged_weapons", 0),
      
      (assign, "$g_multiplayer_initial_gold_multiplier", 100),
      (assign, "$g_multiplayer_battle_earnings_multiplier", 100),
      (assign, "$g_multiplayer_round_earnings_multiplier", 100),
      
      #faction banners
      (faction_set_slot, "fac_kingdom_1", slot_faction_banner, "mesh_banner_kingdom_f"),
      (faction_set_slot, "fac_kingdom_2", slot_faction_banner, "mesh_banner_kingdom_b"),
      (faction_set_slot, "fac_kingdom_3", slot_faction_banner, "mesh_banner_kingdom_c"),
      (faction_set_slot, "fac_kingdom_4", slot_faction_banner, "mesh_banner_kingdom_a"),
      (faction_set_slot, "fac_kingdom_5", slot_faction_banner, "mesh_banner_kingdom_d"),
      (faction_set_slot, "fac_kingdom_6", slot_faction_banner, "mesh_banner_kingdom_e"),
      
      (try_for_range, ":cur_item", all_items_begin, all_items_end),
        (try_for_range, ":cur_faction", npc_kingdoms_begin, npc_kingdoms_end),
          (store_sub, ":faction_index", ":cur_faction", npc_kingdoms_begin),
          (val_add, ":faction_index", slot_item_multiplayer_faction_price_multipliers_begin),
          (item_set_slot, ":cur_item", ":faction_index", 100), #100 is the default price multiplier
        (try_end),
      (try_end),
      (store_sub, ":swadian_price_slot", "fac_kingdom_1", npc_kingdoms_begin),
      (val_add, ":swadian_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),
      (store_sub, ":vaegir_price_slot", "fac_kingdom_2", npc_kingdoms_begin),
      (val_add, ":vaegir_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),
      (store_sub, ":khergit_price_slot", "fac_kingdom_3", npc_kingdoms_begin),
      (val_add, ":khergit_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),
      (store_sub, ":nord_price_slot", "fac_kingdom_4", npc_kingdoms_begin),
      (val_add, ":nord_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),
      (store_sub, ":rhodok_price_slot", "fac_kingdom_5", npc_kingdoms_begin),
      (val_add, ":rhodok_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),
      (store_sub, ":sarranid_price_slot", "fac_kingdom_6", npc_kingdoms_begin),
      (val_add, ":sarranid_price_slot", slot_item_multiplayer_faction_price_multipliers_begin),
      
      #      (item_set_slot, "itm_steppe_horse", ":khergit_price_slot", 50),


      ###Horses
      (item_set_slot, "itm_ho_swa_saddle_black", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_swa_destrier_black", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_vae_saddle_feather", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_vae_rus_brown", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_khe_saddle_coloured", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_khe_steppe_brownpainted", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_nor_mule", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_nor_courser_greysteel", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_rho_donkey_brown", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_rho_rouncy_brown", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_sar_camel_bactrian", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_sar_arab_dun", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_pla_sumpter_white", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_swa_war_royal", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_swa_charger_long", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_vae_war_leathered", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_vae_charger_leathered", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_khe_war_brass", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_khe_charger_steppe", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_nor_war_blue", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_nor_charger_lamellar", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_rho_war_chain", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_rho_charger_chain", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_sar_war_golden", slot_item_multiplayer_item_class, multi_item_class_type_horse),
      (item_set_slot, "itm_ho_sar_charger_sarranid", slot_item_multiplayer_item_class, multi_item_class_type_horse),
	  ###Weapons
      #Axes
      (item_set_slot, "itm_we_vae_axe_bardiche", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_we_vae_axe_bardichelong", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_we_vae_axe_bardichegreat", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_we_vae_axe_bardichegreatlong", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_we_nor_axe_jomsviking", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_we_nor_axe_danox", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_we_nor_axe_haloygox", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_we_nor_axe_breithofudox", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_we_nor_axe_hedmarkox_tveirhendr", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_we_nor_axe_danox_tveirhendr", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_we_rho_axe_pick", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      (item_set_slot, "itm_we_rho_axe_pick_military", slot_item_multiplayer_item_class, multi_item_class_type_axe),
      #Blunt
      (item_set_slot, "itm_we_swa_blunt_club", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_we_swa_blunt_morningstar", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_we_vae_blunt_hammer", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_we_vae_blunt_hammerthick", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_we_vae_blunt_hammersleek", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_we_vae_blunt_hammerempirewar", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_we_vae_blunt_maul", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_we_vae_blunt_sledgehammer", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_we_sar_blunt_maceiron", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_we_sar_blunt_macespiked", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_we_sar_blunt_macespikedlong", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_we_sar_blunt_mace_ironlong", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
	  ##Polearms
      #Spears
      (item_set_slot, "itm_we_swa_spear_boar", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_swa_spear_glaive_small", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_swa_spear_glaive", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_swa_spear_bill_english", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_vae_spear_scythe", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_vae_spear_scythe_military", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_vae_spear_scythe_shortened", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_khe_spear_staff", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_khe_spear_nagita", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_khe_spear_viper", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_khe_spear_haftedblade", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_nor_spear_sviar", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_nor_spear_hoggkesja", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_nor_spear_krokaspjott_kastad", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_nor_spear_hoggspjott_langr", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_rho_spear_fork_pitch", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_rho_spear_fork_military", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_rho_spear_fork_battle", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_rho_spear_mountain", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_rho_spear_large", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_rho_spear_phalanx", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      #Lance
      (item_set_slot, "itm_we_swa_spear_lance_jousting", slot_item_multiplayer_item_class, multi_item_class_type_lance),
      (item_set_slot, "itm_we_swa_spear_lance_light", slot_item_multiplayer_item_class, multi_item_class_type_lance),
      (item_set_slot, "itm_we_swa_spear_lance_heavy", slot_item_multiplayer_item_class, multi_item_class_type_lance),
      (item_set_slot, "itm_we_swa_spear_lance_great", slot_item_multiplayer_item_class, multi_item_class_type_lance),
      (item_set_slot, "itm_we_vae_spear_lance", slot_item_multiplayer_item_class, multi_item_class_type_lance),
      (item_set_slot, "itm_we_khe_spear_lance", slot_item_multiplayer_item_class, multi_item_class_type_lance),
      (item_set_slot, "itm_we_khe_spear_lanceflag_a", slot_item_multiplayer_item_class, multi_item_class_type_lance),
      (item_set_slot, "itm_we_khe_spear_lancehook", slot_item_multiplayer_item_class, multi_item_class_type_lance),
      (item_set_slot, "itm_we_nor_spear_svia_langr", slot_item_multiplayer_item_class, multi_item_class_type_lance),
      (item_set_slot, "itm_we_rho_spear_lance", slot_item_multiplayer_item_class, multi_item_class_type_lance),
      (item_set_slot, "itm_we_sar_spear_desert", slot_item_multiplayer_item_class, multi_item_class_type_lance),
      (item_set_slot, "itm_we_sar_spear_lance", slot_item_multiplayer_item_class, multi_item_class_type_lance),
      ##Swords
	  #One-Handed
      (item_set_slot, "itm_we_swa_sword_clamshelldagger", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_swa_sword_senlac", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_swa_sword_clamshell", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_swa_sword_knight", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_swa_sword_lord", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_vae_sword_sickle", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_we_vae_sword_knife", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_we_vae_sword_sickle_military", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_we_vae_sword_jarl", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_we_vae_sword_cleaver_military", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_we_khe_sword_dagger", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_we_khe_sword_executionerone", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
      (item_set_slot, "itm_we_khe_sword_nomad", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
      (item_set_slot, "itm_we_khe_sword_khergit", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
      (item_set_slot, "itm_we_khe_sword_steppe", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
      (item_set_slot, "itm_we_khe_sword_broad", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
      (item_set_slot, "itm_we_nor_sword_seax", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
      (item_set_slot, "itm_we_nor_sword_pict", slot_item_multiplayer_item_class, multi_item_class_type_cleavers),
      (item_set_slot, "itm_we_nor_sword_angle", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_we_nor_sword_nordic", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_we_nor_sword_saxon", slot_item_multiplayer_item_class, multi_item_class_type_blunt),
      (item_set_slot, "itm_we_nor_sword_eurodino", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_we_rho_sword_rondeldagger", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_we_rho_sword_short", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_axe),
      (item_set_slot, "itm_we_rho_sword_squire", slot_item_multiplayer_item_class, multi_item_class_type_spear),
      (item_set_slot, "itm_we_rho_sword_castellan", slot_item_multiplayer_item_class, multi_item_class_type_war_picks),
      (item_set_slot, "itm_we_rho_sword_estoc_small", slot_item_multiplayer_item_class, multi_item_class_type_war_picks),
      (item_set_slot, "itm_we_rho_sword_general", slot_item_multiplayer_item_class, multi_item_class_type_war_picks),
      (item_set_slot, "itm_we_sar_sword_khyber", slot_item_multiplayer_item_class, multi_item_class_type_war_picks),
      (item_set_slot, "itm_we_sar_sword_sarranid", slot_item_multiplayer_item_class, multi_item_class_type_war_picks),
      (item_set_slot, "itm_we_sar_sword_arming", slot_item_multiplayer_item_class, multi_item_class_type_war_picks),
      (item_set_slot, "itm_we_sar_sword_cavalry", slot_item_multiplayer_item_class, multi_item_class_type_war_picks),
      (item_set_slot, "itm_we_sar_sword_scimitar", slot_item_multiplayer_item_class, multi_item_class_type_war_picks),
      (item_set_slot, "itm_we_sar_sword_guard", slot_item_multiplayer_item_class, multi_item_class_type_war_picks),
	  #Two-Handed
      (item_set_slot, "itm_we_swa_sword_crusader", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_swa_sword_longenglish", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_swa_sword_clamshell_claymore", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_swa_sword_twohanded_claymore", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_vae_sword_cleaverwar", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_khe_sword_sabre", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_khe_sword_sabredark", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_nor_sword_danish_great", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_rho_sword_estoc", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_rho_sword_estoc_empire", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_rho_sword_great", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_rho_sword_great_long", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_sar_sword_scimitarbastard", slot_item_multiplayer_item_class, multi_item_class_type_sword),
      (item_set_slot, "itm_we_sar_sword_scimitartwolarge", slot_item_multiplayer_item_class, multi_item_class_type_two_handed_sword),
	  ##Ranged Weapons
      #Ammunition
      (item_set_slot, "itm_we_swa_arrow_gromite", slot_item_multiplayer_item_class, multi_item_class_type_arrow),
      (item_set_slot, "itm_we_swa_arrow_steel", slot_item_multiplayer_item_class, multi_item_class_type_arrow),
      (item_set_slot, "itm_we_vae_arrow_sharp", slot_item_multiplayer_item_class, multi_item_class_type_arrow),
      (item_set_slot, "itm_we_vae_arrow_imperial", slot_item_multiplayer_item_class, multi_item_class_type_arrow),
      (item_set_slot, "itm_we_khe_arrow_khergit", slot_item_multiplayer_item_class, multi_item_class_type_arrow),
      (item_set_slot, "itm_we_khe_arrow_mongol", slot_item_multiplayer_item_class, multi_item_class_type_arrow),
      (item_set_slot, "itm_we_khe_arrow_mongol_piercing", slot_item_multiplayer_item_class, multi_item_class_type_arrow),
      (item_set_slot, "itm_we_nor_arrow_bodkin", slot_item_multiplayer_item_class, multi_item_class_type_arrow),
      (item_set_slot, "itm_we_nor_arrow_barbed", slot_item_multiplayer_item_class, multi_item_class_type_arrow),
      (item_set_slot, "itm_we_rho_bolt", slot_item_multiplayer_item_class, multi_item_class_type_bolt),
      (item_set_slot, "itm_we_rho_bolt_steel", slot_item_multiplayer_item_class, multi_item_class_type_bolt),
      (item_set_slot, "itm_we_sar_arrow_sarranid", slot_item_multiplayer_item_class, multi_item_class_type_arrow),
      (item_set_slot, "itm_we_sar_arrow_desert", slot_item_multiplayer_item_class, multi_item_class_type_arrow),
      #Bows
      (item_set_slot, "itm_we_swa_bow_practice", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_we_swa_bow_straight", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_we_swa_bow_long", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_we_vae_bow_hunting", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_we_vae_bow_war", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_we_vae_bow_imperial", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_we_khe_bow_practice", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_we_khe_bow_red", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_we_khe_bow_strong", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_we_nor_bow_hunting", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_we_nor_bow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_we_rho_crossbow_hunting", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_we_rho_crossbow", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_we_rho_crossbow_siege", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_we_sar_bow_practice", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_we_sar_bow_leopard", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      (item_set_slot, "itm_we_sar_bow_recurved", slot_item_multiplayer_item_class, multi_item_class_type_bow),
      #Throwing
      (item_set_slot, "itm_we_swa_throw_darts", slot_item_multiplayer_item_class, multi_item_class_type_throwing),
      (item_set_slot, "itm_we_swa_throw_darts_war", slot_item_multiplayer_item_class, multi_item_class_type_throwing),
      (item_set_slot, "itm_we_vae_sword_throw_knives", slot_item_multiplayer_item_class, multi_item_class_type_throwing),
      (item_set_slot, "itm_we_vae_sword_throw_daggers", slot_item_multiplayer_item_class, multi_item_class_type_throwing),
      (item_set_slot, "itm_we_nor_axe_throw_light", slot_item_multiplayer_item_class, multi_item_class_type_throwing),
      (item_set_slot, "itm_we_nor_axe_throw_vendelox", slot_item_multiplayer_item_class, multi_item_class_type_throwing_axe),
      (item_set_slot, "itm_we_nor_axe_throw_mammen", slot_item_multiplayer_item_class, multi_item_class_type_throwing_axe),
      (item_set_slot, "itm_we_nor_spear_kastspjottmidtaggir", slot_item_multiplayer_item_class, multi_item_class_type_throwing_axe),
      (item_set_slot, "itm_we_nor_spear_atgeirr", slot_item_multiplayer_item_class, multi_item_class_type_throwing_axe),
      (item_set_slot, "itm_we_sar_spear_javelin", slot_item_multiplayer_item_class, multi_item_class_type_throwing_axe),
      (item_set_slot, "itm_we_sar_spear_throwing_spears", slot_item_multiplayer_item_class, multi_item_class_type_throwing_axe),
      (item_set_slot, "itm_we_sar_spear_jarid", slot_item_multiplayer_item_class, multi_item_class_type_throwing_axe),
      ###Armors
      (item_set_slot, "itm_ar_swa_tun_tabard", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_swa_t2_gambeson_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_swa_t3_hauberk_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_swa_t4_tabardmail_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_swa_t5_mailsurcoat_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_swa_t6_coatplate_b", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_swa_t7_fullplate_c", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_vae_tun_red", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_vae_t2_leather_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_vae_t3_padded_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_vae_t4_jerkin_b", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_vae_t5_studded_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_vae_t6_cuirbouilli_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_vae_t7_elite_b", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_khe_tun_furcoat", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_khe_t2_armor_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_khe_t3_steppe_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_khe_t4_lamellar_b", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_khe_t5_guard_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_khe_t6_tunic_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_khe_t7_mongol_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_nor_tun_blue", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_nor_t2_vikinglamellar_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_nor_t3_furcoat_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_nor_t4_lightarmor_b", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_nor_t5_byrnie_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_nor_t6_mailshirt_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_nor_t7_vikingbyrnie_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_rho_tun_vest", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_rho_t2_ragged_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_rho_t3_aketon_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_rho_t4_highlander_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_rho_t5_brigandine_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_rho_t6_corrazina_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_rho_t7_milan_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_sar_tun_robeblack", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_sar_t2_quilted_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_sar_t3_leather_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_sar_t4_chihal_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_sar_t5_mailshirt_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_sar_t6_chaintab_a", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      (item_set_slot, "itm_ar_sar_t7_fullplate_b", slot_item_multiplayer_item_class, multi_item_class_type_light_armor),
      ###Boots
      (item_set_slot, "itm_bo_swa_t1_sandal", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_swa_t2_hose", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_swa_t3_wrapping", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_swa_t4_sandal", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_swa_t5_hose", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_swa_t6_mail", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_swa_t7_greaves", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_vae_t1_sandal", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_vae_t2_shoes", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_vae_t3_leather", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_vae_t4_shoes", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_vae_t5_chausses", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_vae_t6_leather", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_vae_t7_greaves", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_khe_t1_sandal", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_khe_t2_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_khe_t3_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_khe_t4_sandal", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_khe_t5_mail", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_khe_t6_mail", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_khe_t7_greaves", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_nor_t1_sandal", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_nor_t2_shoes", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_nor_t3_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_nor_t4_sandal", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_nor_t5_mail", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_nor_t6_mail", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_nor_t7_greaves", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_rho_t1_bear", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_rho_t2_highlander", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_rho_t3_highlander", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_rho_t4_greaves", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_rho_t5_greaves", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_rho_t6_shynbaulds", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_rho_t7_greaves", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_sar_t1_sandal", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_sar_t2_shoes", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_sar_t3_boots", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_sar_t4_camel", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_sar_t5_mail", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_sar_t6_mail", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      (item_set_slot, "itm_bo_sar_t7_greaves", slot_item_multiplayer_item_class, multi_item_class_type_light_foot),
      ###Gauntlets
      (item_set_slot, "itm_ga_swa_a2_leather", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_swa_a4_plate", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_swa_a5_churburg", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_swa_a6_plate", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_vae_a2_leather", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_vae_a4_leather", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_vae_a5_mail", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_vae_a6_black", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_khe_a2_leather", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_khe_a4_lamellar", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_khe_a5_armor", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_khe_a6_lamellar", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_nor_a2_leather", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_nor_a4_scale", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_nor_a5_scale", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_nor_a6_mail", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_rho_a2_leather", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_rho_a4_brigandine", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_rho_a5_bnw", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_rho_a6_hourglass", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_sar_a2_leather", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_sar_a4_brass", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_sar_a5_scale", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      (item_set_slot, "itm_ga_sar_a6_lamellar", slot_item_multiplayer_item_class, multi_item_class_type_glove),
      ###Helmets
      (item_set_slot, "itm_he_swa_t1_common_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_swa_t2_coif_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_swa_t3_helmet_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_swa_t4_bascinet_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_swa_t5_flat_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_swa_t6_full_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_swa_t7_great_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_vae_t1_common_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_vae_t2_furcap_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_vae_t3_furcap_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_vae_t4_helmet_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_vae_t5_helmet_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_vae_t6_warhelmet_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_vae_t7_warmask_b", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_khe_t1_common_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_khe_t2_steppe_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_khe_t3_steppe_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_khe_t4_war_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_khe_t5_neck_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_khe_t6_helmet_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_khe_t7_mask_b", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_nor_t1_common_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_nor_t2_spangen_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_nor_t3_valsgarde_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_nor_t4_valsgarde_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_nor_t5_valsgarde_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_nor_t6_valsgarde_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_nor_t7_valsgarde_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_rho_t1_common_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_rho_t2_beret_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_rho_t3_bascinet_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_rho_t4_kettle_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_rho_t5_kettle_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_rho_t6_kettle_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_rho_t7_clap_b", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_sar_t1_common_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_sar_t2_tuareg_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_sar_t3_rabati_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_sar_t4_tuareg_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_sar_t5_horseman_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_sar_t6_spire_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      (item_set_slot, "itm_he_sar_t7_veiled_a", slot_item_multiplayer_item_class, multi_item_class_type_light_helm),
      ###Shields
      (item_set_slot, "itm_sh_swa_hea_english_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_swa_hea_plain", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_swa_kit_swadian_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_swa_hea_horseman", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_vae_kit_fur", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_vae_kit_leather", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_vae_hae_striped_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_vae_kit_vaegir_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_khe_rou_old", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_khe_rou_plain", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_khe_rou_heavy", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_khe_rou_steel_c", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_nor_rou_small_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_nor_rou_medium_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_nor_rou_roundshield_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_nor_rou_large_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_rho_buc_steel_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_rho_hea_golden", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_rho_pav_deploy_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_rho_pav_deploy_b", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_sar_rou_plain", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_sar_rou_round", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_sar_rou_steel_a", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),
      (item_set_slot, "itm_sh_sar_rou_elite", slot_item_multiplayer_item_class, multi_item_class_type_small_shield),


      #1-Swadian Warriors
      #1a-Swadian Longbowman
		#Blunt
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_blunt_club", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_blunt_morningstar", "trp_swadian_crossbowman_multiplayer"),
		#Swords
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_clamshelldagger", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_senlac", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_clamshell", "trp_swadian_crossbowman_multiplayer"),
		#Ranged Weapons
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_arrow_gromite", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_arrow_steel", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_bow_practice", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_bow_straight", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_bow_long", "trp_swadian_crossbowman_multiplayer"),
		#Armors
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_swa_tun_tabard", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_swa_t2_gambeson_a", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_swa_t3_hauberk_a", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_swa_t4_tabardmail_a", "trp_swadian_crossbowman_multiplayer"),
		#Boots
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_swa_t1_sandal", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_swa_t2_hose", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_swa_t3_wrapping", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_swa_t4_sandal", "trp_swadian_crossbowman_multiplayer"),
		#Gauntlets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_swa_a2_leather", "trp_swadian_crossbowman_multiplayer"),
		#Helmets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_swa_t1_common_a", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_swa_t2_coif_a", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_swa_t3_helmet_a", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_swa_t4_bascinet_a", "trp_swadian_crossbowman_multiplayer"),
		#Shields
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_swa_hea_english_a", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_swa_hea_plain", "trp_swadian_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_swa_kit_swadian_a", "trp_swadian_crossbowman_multiplayer"),
      
      #1b-Swadian Infantry
		#Spears
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_spear_boar", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_spear_glaive_small", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_spear_glaive", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_spear_bill_english", "trp_swadian_infantry_multiplayer"),
		#Swords
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_clamshelldagger", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_senlac", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_clamshell", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_knight", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_lord", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_crusader", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_longenglish", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_clamshell_claymore", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_twohanded_claymore", "trp_swadian_infantry_multiplayer"),
		#Ranged Weapons
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_throw_darts", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_throw_darts_war", "trp_swadian_infantry_multiplayer"),
		#Armor
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_swa_tun_tabard", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_swa_t2_gambeson_a", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_swa_t3_hauberk_a", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_swa_t4_tabardmail_a", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_swa_t5_mailsurcoat_a", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_swa_t6_coatplate_b", "trp_swadian_infantry_multiplayer"),
		#Boots
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_swa_t1_sandal", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_swa_t2_hose", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_swa_t3_wrapping", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_swa_t4_sandal", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_swa_t5_hose", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_swa_t6_mail", "trp_swadian_infantry_multiplayer"),
		#Gauntlets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_swa_a2_leather", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_swa_a4_plate", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_swa_a5_churburg", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_swa_a6_plate", "trp_swadian_infantry_multiplayer"),
		#Helmets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_swa_t1_common_a", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_swa_t2_coif_a", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_swa_t3_helmet_a", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_swa_t4_bascinet_a", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_swa_t5_flat_a", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_swa_t6_full_a", "trp_swadian_infantry_multiplayer"),
		#Shields
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_swa_hea_english_a", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_swa_hea_plain", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_swa_kit_swadian_a", "trp_swadian_infantry_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_swa_hea_horseman", "trp_swadian_infantry_multiplayer"),

      #1c-Swadian Man At Arms
		#Horses
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_pla_sumpter_white", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_swa_saddle_black", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_swa_destrier_black", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_swa_war_royal", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_swa_charger_long", "trp_swadian_man_at_arms_multiplayer"),
		#Lances
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_spear_lance_jousting", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_spear_lance_light", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_spear_lance_heavy", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_spear_lance_great", "trp_swadian_man_at_arms_multiplayer"),
		#Swords
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_clamshelldagger", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_senlac", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_clamshell", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_knight", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_crusader", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_sword_longenglish", "trp_swadian_man_at_arms_multiplayer"),
		#Ranged Weapons
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_throw_darts", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_swa_throw_darts_war", "trp_swadian_man_at_arms_multiplayer"),
		#Armor
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_swa_tun_tabard", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_swa_t2_gambeson_a", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_swa_t3_hauberk_a", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_swa_t4_tabardmail_a", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_swa_t5_mailsurcoat_a", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_swa_t6_coatplate_b", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_swa_t7_fullplate_c", "trp_swadian_man_at_arms_multiplayer"),
		#Boots
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_swa_t1_sandal", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_swa_t2_hose", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_swa_t3_wrapping", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_swa_t4_sandal", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_swa_t5_hose", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_swa_t6_mail", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_swa_t7_greaves", "trp_swadian_man_at_arms_multiplayer"),
		#Gauntlets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_swa_a2_leather", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_swa_a4_plate", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_swa_a5_churburg", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_swa_a6_plate", "trp_swadian_man_at_arms_multiplayer"),
		#Helmets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_swa_t1_common_a", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_swa_t2_coif_a", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_swa_t3_helmet_a", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_swa_t4_bascinet_a", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_swa_t5_flat_a", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_swa_t6_full_a", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_swa_t7_great_a", "trp_swadian_man_at_arms_multiplayer"),
		#Shields
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_swa_hea_english_a", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_swa_hea_plain", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_swa_kit_swadian_a", "trp_swadian_man_at_arms_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_swa_hea_horseman", "trp_swadian_man_at_arms_multiplayer"),


      #2-Vaegir Warriors
      #2a-Vaegir Archer
		#Blunt
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_blunt_hammer", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_blunt_hammerthick", "trp_vaegir_archer_multiplayer"),
		#Swords
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_sword_sickle", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_sword_knife", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_sword_sickle_military", "trp_vaegir_archer_multiplayer"),
		#Ranged Weapons
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_arrow_sharp", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_arrow_imperial", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_bow_hunting", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_bow_war", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_bow_imperial", "trp_vaegir_archer_multiplayer"),
		#Armor
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_vae_tun_red", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_vae_t2_leather_a", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_vae_t3_padded_a", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_vae_t4_jerkin_b", "trp_vaegir_archer_multiplayer"),
		#Boots
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_vae_t1_sandal", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_vae_t2_shoes", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_vae_t3_leather", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_vae_t4_shoes", "trp_vaegir_archer_multiplayer"),
		#Gauntlets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_vae_a2_leather", "trp_vaegir_archer_multiplayer"),
		#Helmets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_vae_t1_common_a", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_vae_t2_furcap_a", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_vae_t3_furcap_a", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_vae_t4_helmet_a", "trp_vaegir_archer_multiplayer"),
		#Shields
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_vae_kit_fur", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_vae_kit_leather", "trp_vaegir_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_vae_hae_striped_a", "trp_vaegir_archer_multiplayer"),

      #2b-Vaegir Spearman
		#Axes
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_axe_bardiche", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_axe_bardichelong", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_axe_bardichegreat", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_axe_bardichegreatlong", "trp_vaegir_spearman_multiplayer"),
		#Spears
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_spear_scythe", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_spear_scythe_military", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_spear_scythe_shortened", "trp_vaegir_spearman_multiplayer"),
		#Swords
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_sword_sickle", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_sword_knife", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_sword_sickle_military", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_sword_jarl", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_sword_cleaver_military", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_sword_cleaverwar", "trp_vaegir_spearman_multiplayer"),
		#Range Weapons
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_sword_throw_knives", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_sword_throw_daggers", "trp_vaegir_spearman_multiplayer"),
		#Armor
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_vae_tun_red", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_vae_t2_leather_a", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_vae_t3_padded_a", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_vae_t4_jerkin_b", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_vae_t5_studded_a", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_vae_t6_cuirbouilli_a", "trp_vaegir_spearman_multiplayer"),
		#Boots
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_vae_t1_sandal", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_vae_t2_shoes", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_vae_t3_leather", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_vae_t4_shoes", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_vae_t5_chausses", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_vae_t6_leather", "trp_vaegir_spearman_multiplayer"),
		#Gauntlets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_vae_a2_leather", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_vae_a4_leather", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_vae_a5_mail", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_vae_a6_black", "trp_vaegir_spearman_multiplayer"),
		#Helmets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_vae_t1_common_a", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_vae_t2_furcap_a", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_vae_t3_furcap_a", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_vae_t4_helmet_a", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_vae_t5_helmet_a", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_vae_t6_warhelmet_a", "trp_vaegir_spearman_multiplayer"),
		#Shields
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_vae_kit_fur", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_vae_kit_leather", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_vae_hae_striped_a", "trp_vaegir_spearman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_vae_kit_vaegir_a", "trp_vaegir_spearman_multiplayer"),

      #2c-Vaegir Horseman
		#Horses
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_pla_sumpter_white", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_vae_saddle_feather", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_vae_rus_brown", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_vae_war_leathered", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_vae_charger_leathered", "trp_vaegir_horseman_multiplayer"),
		#Blunt
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_blunt_hammer", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_blunt_hammerthick", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_blunt_hammersleek", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_blunt_hammerempirewar", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_blunt_sledgehammer", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_blunt_greathammer", "trp_vaegir_horseman_multiplayer"),
		#Lances
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_spear_lance", "trp_vaegir_horseman_multiplayer"),
		#Swords
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_sword_sickle", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_sword_knife", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_sword_sickle_military", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_sword_jarl", "trp_vaegir_horseman_multiplayer"),
		#Ranged Weapons
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_sword_throw_knives", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_vae_sword_throw_daggers", "trp_vaegir_horseman_multiplayer"),
		#Armor
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_vae_tun_red", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_vae_t2_leather_a", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_vae_t3_padded_a", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_vae_t4_jerkin_b", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_vae_t5_studded_a", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_vae_t6_cuirbouilli_a", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_vae_t7_elite_b", "trp_vaegir_horseman_multiplayer"),
		#Boots
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_vae_t1_sandal", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_vae_t2_shoes", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_vae_t3_leather", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_vae_t4_shoes", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_vae_t5_chausses", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_vae_t6_leather", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_vae_t7_greaves", "trp_vaegir_horseman_multiplayer"),
		#Gauntlets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_vae_a2_leather", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_vae_a4_leather", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_vae_a5_mail", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_vae_a6_black", "trp_vaegir_horseman_multiplayer"),
		#Helmets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_vae_t1_common_a", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_vae_t2_furcap_a", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_vae_t3_furcap_a", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_vae_t4_helmet_a", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_vae_t5_helmet_a", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_vae_t6_warhelmet_a", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_vae_t7_warmask_b", "trp_vaegir_horseman_multiplayer"),
		#Shields
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_vae_kit_fur", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_vae_kit_leather", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_vae_hae_striped_a", "trp_vaegir_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_vae_kit_vaegir_a", "trp_vaegir_horseman_multiplayer"),


      #3-Khergit Warriors
      #3a-Khergit Veteran Horse Archer
		#Horses
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_pla_sumpter_white", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_khe_saddle_coloured", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_khe_steppe_brownpainted", "trp_khergit_veteran_horse_archer_multiplayer"),
		#Spears
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_spear_staff", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_spear_nagita", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_spear_viper", "trp_khergit_veteran_horse_archer_multiplayer"),
		#Swords
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_sword_dagger", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_sword_executionerone", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_sword_nomad", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_sword_khergit", "trp_khergit_veteran_horse_archer_multiplayer"),
		#Ranged Weapons
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_arrow_khergit", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_arrow_mongol", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_arrow_mongol_piercing", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_bow_practice", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_bow_red", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_bow_strong", "trp_khergit_veteran_horse_archer_multiplayer"),
		#Armor
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_khe_tun_furcoat", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_khe_t2_armor_a", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_khe_t3_steppe_a", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_khe_t4_lamellar_b", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_khe_t5_guard_a", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_khe_t6_tunic_a", "trp_khergit_veteran_horse_archer_multiplayer"),
		#Boots
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_khe_t1_sandal", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_khe_t2_boots", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_khe_t3_boots", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_khe_t4_sandal", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_khe_t5_mail", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_khe_t6_mail", "trp_khergit_veteran_horse_archer_multiplayer"),
		#Gauntlets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_khe_a2_leather", "trp_khergit_veteran_horse_archer_multiplayer"),
		#Helmets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_khe_t1_common_a", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_khe_t2_steppe_a", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_khe_t3_steppe_a", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_khe_t4_war_a", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_khe_t5_neck_a", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_khe_t6_helmet_a", "trp_khergit_veteran_horse_archer_multiplayer"),
		#Shields
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_khe_rou_old", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_khe_rou_plain", "trp_khergit_veteran_horse_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_khe_rou_heavy", "trp_khergit_veteran_horse_archer_multiplayer"),

      #3a-Khergit Lancer
		#Horses
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_pla_sumpter_white", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_khe_saddle_coloured", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_khe_steppe_brownpainted", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_khe_war_brass", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_khe_charger_steppe", "trp_khergit_lancer_multiplayer"),
		#Spears
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_spear_staff", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_spear_nagita", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_spear_viper", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_spear_haftedblade", "trp_khergit_lancer_multiplayer"),
		#Lances
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_spear_lance", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_spear_lanceflag_a", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_spear_lancehook", "trp_khergit_lancer_multiplayer"),
		#Swords
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_sword_dagger", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_sword_executionerone", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_sword_nomad", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_sword_khergit", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_sword_steppe", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_sword_broad", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_sword_sabre", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_khe_sword_sabredark", "trp_khergit_lancer_multiplayer"),
		#Armor
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_khe_tun_furcoat", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_khe_t2_armor_a", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_khe_t3_steppe_a", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_khe_t4_lamellar_b", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_khe_t5_guard_a", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_khe_t6_tunic_a", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_khe_t7_mongol_a", "trp_khergit_lancer_multiplayer"),
		#Boots
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_khe_t1_sandal", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_khe_t2_boots", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_khe_t3_boots", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_khe_t4_sandal", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_khe_t5_mail", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_khe_t6_mail", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_khe_t7_greaves", "trp_khergit_lancer_multiplayer"),
		#Gauntlets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_khe_a2_leather", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_khe_a4_lamellar", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_khe_a5_armor", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_khe_a6_lamellar", "trp_khergit_lancer_multiplayer"),
		#Helmets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_khe_t1_common_a", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_khe_t2_steppe_a", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_khe_t3_steppe_a", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_khe_t4_war_a", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_khe_t5_neck_a", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_khe_t6_helmet_a", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_khe_t7_mask_b", "trp_khergit_lancer_multiplayer"),
		#Shields
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_khe_rou_old", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_khe_rou_plain", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_khe_rou_heavy", "trp_khergit_lancer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_khe_rou_steel_c", "trp_khergit_lancer_multiplayer"),


      #Nord Warriors
      #4c-Nord Archer
		#Swords
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_sword_seax", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_sword_pict", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_sword_angle", "trp_nord_archer_multiplayer"),
		#Ranged Weapons
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_arrow_bodkin", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_arrow_barbed", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_bow_hunting", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_bow", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_axe_throw_light", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_axe_throw_vendelox", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_spear_kastspjottmidtaggir", "trp_nord_archer_multiplayer"),
		#Armor
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_nor_tun_blue", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_nor_t2_vikinglamellar_a", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_nor_t3_furcoat_a", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_nor_t4_lightarmor_b", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_nor_t5_byrnie_a", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_nor_t6_mailshirt_a", "trp_nord_archer_multiplayer"),
		#Boots
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_nor_t1_sandal", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_nor_t2_shoes", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_nor_t3_boots", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_nor_t4_sandal", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_nor_t5_mail", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_nor_t6_mail", "trp_nord_archer_multiplayer"),
		#Gauntlets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_nor_a2_leather", "trp_nord_archer_multiplayer"),
		#Helmets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_nor_t1_common_a", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_nor_t2_spangen_a", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_nor_t3_valsgarde_a", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_nor_t4_valsgarde_a", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_nor_t5_valsgarde_a", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_nor_t6_valsgarde_a", "trp_nord_archer_multiplayer"),
		#Shields
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_nor_rou_small_a", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_nor_rou_medium_a", "trp_nord_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_nor_rou_roundshield_a", "trp_nord_archer_multiplayer"),

      #4a-Nord Veteran
		#Axes
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_axe_jomsviking", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_axe_danox", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_axe_haloygox", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_axe_breithofudox", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_axe_hedmarkox_tveirhendr", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_axe_danox_tveirhendr", "trp_nord_veteran_multiplayer"),
		#Spears
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_spear_sviar", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_spear_hoggkesja", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_spear_krokaspjott_kastad", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_spear_hoggspjott_langr", "trp_nord_veteran_multiplayer"),
		#Swords
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_sword_seax", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_sword_pict", "trp_nord_veteran_multiplayer"),
		#Ranged Weapons
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_axe_throw_light", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_axe_throw_vendelox", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_spear_kastspjottmidtaggir", "trp_nord_veteran_multiplayer"),
		#Armor
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_nor_tun_blue", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_nor_t2_vikinglamellar_a", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_nor_t3_furcoat_a", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_nor_t4_lightarmor_b", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_nor_t5_byrnie_a", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_nor_t6_mailshirt_a", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_nor_t7_vikingbyrnie_a", "trp_nord_veteran_multiplayer"),
		#Boots
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_nor_t1_sandal", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_nor_t2_shoes", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_nor_t3_boots", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_nor_t4_sandal", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_nor_t5_mail", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_nor_t6_mail", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_nor_t7_greaves", "trp_nord_veteran_multiplayer"),
		#Gauntlets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_nor_a2_leather", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_nor_a4_scale", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_nor_a5_scale", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_nor_a6_mail", "trp_nord_veteran_multiplayer"),
		#Helmets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_nor_t1_common_a", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_nor_t2_spangen_a", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_nor_t3_valsgarde_a", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_nor_t4_valsgarde_a", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_nor_t5_valsgarde_a", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_nor_t6_valsgarde_a", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_nor_t7_valsgarde_a", "trp_nord_veteran_multiplayer"),
		#Shields
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_nor_rou_small_a", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_nor_rou_medium_a", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_nor_rou_roundshield_a", "trp_nord_veteran_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_nor_rou_large_a", "trp_nord_veteran_multiplayer"),

      #4b-Nord Scout
		#Horses
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_pla_sumpter_white", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_nor_mule", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_nor_courser_greysteel", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_nor_war_blue", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_nor_charger_lamellar", "trp_nord_scout_multiplayer"),
		#Lances
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_spear_svia_langr", "trp_nord_scout_multiplayer"),
		#Swords
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_sword_seax", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_sword_pict", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_sword_angle", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_sword_nordic", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_sword_saxon", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_sword_eurodino", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_sword_danish_great", "trp_nord_scout_multiplayer"),
		#Ranged Weapons
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_axe_throw_light", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_axe_throw_vendelox", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_axe_throw_mammen", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_spear_kastspjottmidtaggir", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_nor_spear_atgeirr", "trp_nord_scout_multiplayer"),
		#Armor
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_nor_tun_blue", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_nor_t2_vikinglamellar_a", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_nor_t3_furcoat_a", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_nor_t4_lightarmor_b", "trp_nord_scout_multiplayer"),
		#Boots
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_nor_t1_sandal", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_nor_t2_shoes", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_nor_t3_boots", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_nor_t4_sandal", "trp_nord_scout_multiplayer"),
		#Gauntlets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_nor_a2_leather", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_nor_a4_scale", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_nor_a5_scale", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_nor_a6_mail", "trp_nord_scout_multiplayer"),
		#Helmets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_nor_t1_common_a", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_nor_t2_spangen_a", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_nor_t3_valsgarde_a", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_nor_t4_valsgarde_a", "trp_nord_scout_multiplayer"),
		#Shields
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_nor_rou_small_a", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_nor_rou_medium_a", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_nor_rou_roundshield_a", "trp_nord_scout_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_nor_rou_large_a", "trp_nord_scout_multiplayer"),


      #5-Rhodok Warriors
      #5a-Rhodok Veteran Crossbowman
		#Axes
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_axe_pick", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_axe_pick_military", "trp_rhodok_veteran_crossbowman_multiplayer"),
		#Swords
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_rondeldagger", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_short", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_squire", "trp_rhodok_veteran_crossbowman_multiplayer"),
		#Ranged Weapons
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_bolt", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_bolt_steel", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_crossbow_hunting", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_crossbow", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_crossbow_siege", "trp_rhodok_veteran_crossbowman_multiplayer"),
		#Armor
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_rho_tun_vest", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_rho_t2_ragged_a", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_rho_t3_aketon_a", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_rho_t4_highlander_a", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_rho_t5_brigandine_a", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_rho_t6_corrazina_a", "trp_rhodok_veteran_crossbowman_multiplayer"),
		#Boots
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_rho_t1_bear", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_rho_t2_highlander", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_rho_t3_highlander", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_rho_t4_greaves", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_rho_t5_greaves", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_rho_t6_shynbaulds", "trp_rhodok_veteran_crossbowman_multiplayer"),
		#Gauntlets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_rho_a2_leather", "trp_rhodok_veteran_crossbowman_multiplayer"),
		#Helmets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_rho_t1_common_a", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_rho_t2_beret_a", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_rho_t3_bascinet_a", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_rho_t4_kettle_a", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_rho_t5_kettle_a", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_rho_t6_kettle_a", "trp_rhodok_veteran_crossbowman_multiplayer"),
		#Shields
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_rho_buc_steel_a", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_rho_hea_golden", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_rho_pav_deploy_a", "trp_rhodok_veteran_crossbowman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_rho_pav_deploy_b", "trp_rhodok_veteran_crossbowman_multiplayer"),

      #5b-Rhodok Sergeant
		#Axes
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_axe_pick", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_axe_pick_military", "trp_rhodok_sergeant_multiplayer"),
		#Spears
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_spear_fork_pitch", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_spear_fork_military", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_spear_fork_battle", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_spear_mountain", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_spear_large", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_spear_phalanx", "trp_rhodok_sergeant_multiplayer"),
		#Swords
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_rondeldagger", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_short", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_squire", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_castellan", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_estoc_small", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_estoc", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_estoc_empire", "trp_rhodok_sergeant_multiplayer"),
		#Armor
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_rho_tun_vest", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_rho_t2_ragged_a", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_rho_t3_aketon_a", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_rho_t4_highlander_a", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_rho_t5_brigandine_a", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_rho_t6_corrazina_a", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_rho_t7_milan_a", "trp_rhodok_sergeant_multiplayer"),
		#Boots
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_rho_t1_bear", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_rho_t2_highlander", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_rho_t3_highlander", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_rho_t4_greaves", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_rho_t5_greaves", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_rho_t6_shynbaulds", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_rho_t7_greaves", "trp_rhodok_sergeant_multiplayer"),
		#Gauntlets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_rho_a2_leather", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_rho_a4_brigandine", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_rho_a5_bnw", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_rho_a6_hourglass", "trp_rhodok_sergeant_multiplayer"),
		#Helmets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_rho_t1_common_a", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_rho_t2_beret_a", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_rho_t3_bascinet_a", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_rho_t4_kettle_a", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_rho_t5_kettle_a", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_rho_t6_kettle_a", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_rho_t7_clap_b", "trp_rhodok_sergeant_multiplayer"),
		#Shields
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_rho_buc_steel_a", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_rho_hea_golden", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_rho_pav_deploy_a", "trp_rhodok_sergeant_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_rho_pav_deploy_b", "trp_rhodok_sergeant_multiplayer"),

      #5c-Rhodok Horseman
		#Horses
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_pla_sumpter_white", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_rho_donkey_brown", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_rho_rouncy_brown", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_rho_war_chain", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_rho_charger_chain", "trp_rhodok_horseman_multiplayer"),
		#Spears
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_spear_fork_pitch", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_spear_fork_military", "trp_rhodok_horseman_multiplayer"),
		#Lances
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_spear_lance", "trp_rhodok_horseman_multiplayer"),
		#Swords
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_rondeldagger", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_short", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_squire", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_castellan", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_estoc_small", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_general", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_estoc", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_estoc_empire", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_great", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_rho_sword_great_long", "trp_rhodok_horseman_multiplayer"),
		#Armor
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_rho_tun_vest", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_rho_t2_ragged_a", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_rho_t3_aketon_a", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_rho_t4_highlander_a", "trp_rhodok_horseman_multiplayer"),
		#Boots
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_rho_t1_bear", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_rho_t2_highlander", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_rho_t3_highlander", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_rho_t4_greaves", "trp_rhodok_horseman_multiplayer"),
		#Gauntlets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_rho_a2_leather", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_rho_a4_brigandine", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_rho_a5_bnw", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_rho_a6_hourglass", "trp_rhodok_horseman_multiplayer"),
		#Helmets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_rho_t1_common_a", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_rho_t2_beret_a", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_rho_t3_bascinet_a", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_rho_t4_kettle_a", "trp_rhodok_horseman_multiplayer"),
		#Shields
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_rho_buc_steel_a", "trp_rhodok_horseman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_rho_hea_golden", "trp_rhodok_horseman_multiplayer"),


      #6-Sarranid Warriors
      #6a-Sarranid archer
		#Blunt
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_blunt_maceiron", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_blunt_macespiked", "trp_sarranid_archer_multiplayer"),
		#Swords
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_sword_khyber", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_sword_sarranid", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_sword_arming", "trp_sarranid_archer_multiplayer"),
		#Ranged Weapons
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_arrow_sarranid", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_arrow_desert", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_bow_practice", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_bow_leopard", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_bow_recurved", "trp_sarranid_archer_multiplayer"),
		#Armor
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_sar_tun_robeblack", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_sar_t2_quilted_a", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_sar_t3_leather_a", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_sar_t4_chihal_a", "trp_sarranid_archer_multiplayer"),
		#Boots
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_sar_t1_sandal", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_sar_t2_shoes", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_sar_t3_boots", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_sar_t4_camel", "trp_sarranid_archer_multiplayer"),
		#Gauntlets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_sar_a2_leather", "trp_sarranid_archer_multiplayer"),
		#Helmets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_sar_t1_common_a", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_sar_t2_tuareg_a", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_sar_t3_rabati_a", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_sar_t4_tuareg_a", "trp_sarranid_archer_multiplayer"),
		#Shields
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_sar_rou_plain", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_sar_rou_round", "trp_sarranid_archer_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_sar_rou_steel_a", "trp_sarranid_archer_multiplayer"),

      #6b-Sarranid footman
		#Blunt
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_blunt_maceiron", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_blunt_macespiked", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_blunt_macespikedlong", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_blunt_mace_ironlong", "trp_sarranid_footman_multiplayer"),
		#Swords
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_sword_khyber", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_sword_sarranid", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_sword_arming", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_sword_cavalry", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_sword_scimitar", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_sword_guard", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_sword_scimitarbastard", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_sword_scimitartwolarge", "trp_sarranid_footman_multiplayer"),
		#Ranged Weapons
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_spear_javelin", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_spear_throwing_spears", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_spear_jarid", "trp_sarranid_footman_multiplayer"),
		#Armor
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_sar_tun_robeblack", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_sar_t2_quilted_a", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_sar_t3_leather_a", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_sar_t4_chihal_a", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_sar_t5_mailshirt_a", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_sar_t6_chaintab_a", "trp_sarranid_footman_multiplayer"),
		#Boots
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_sar_t1_sandal", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_sar_t2_shoes", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_sar_t3_boots", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_sar_t4_camel", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_sar_t5_mail", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_sar_t6_mail", "trp_sarranid_footman_multiplayer"),
		#Gauntlets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_sar_a2_leather", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_sar_a4_brass", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_sar_a5_scale", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_sar_a6_lamellar", "trp_sarranid_footman_multiplayer"),
		#Helmets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_sar_t1_common_a", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_sar_t2_tuareg_a", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_sar_t3_rabati_a", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_sar_t4_tuareg_a", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_sar_t5_horseman_a", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_sar_t6_spire_a", "trp_sarranid_footman_multiplayer"),
		#Shields
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_sar_rou_plain", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_sar_rou_round", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_sar_rou_steel_a", "trp_sarranid_footman_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_sar_rou_elite", "trp_sarranid_footman_multiplayer"),

      #6c-Sarranid mamluke
		#Horses
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_pla_sumpter_white", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_sar_camel_bactrian", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_sar_arab_dun", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_sar_war_golden", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ho_sar_charger_sarranid", "trp_sarranid_mamluke_multiplayer"),
		#Blunt
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_blunt_maceiron", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_blunt_macespiked", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_blunt_macespikedlong", "trp_sarranid_mamluke_multiplayer"),
		#Lances
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_spear_desert", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_spear_lance", "trp_sarranid_mamluke_multiplayer"),
		#Swords
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_sword_khyber", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_sword_sarranid", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_sword_arming", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_sword_cavalry", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_sword_scimitar", "trp_sarranid_mamluke_multiplayer"),
		#Ranged Weapons
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_spear_javelin", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_spear_throwing_spears", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_we_sar_spear_jarid", "trp_sarranid_mamluke_multiplayer"),
		#Armor
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_sar_tun_robeblack", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_sar_t2_quilted_a", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_sar_t3_leather_a", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_sar_t4_chihal_a", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_sar_t5_mailshirt_a", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_sar_t6_chaintab_a", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ar_sar_t7_fullplate_b", "trp_sarranid_mamluke_multiplayer"),
		#Boots
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_sar_t1_sandal", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_sar_t2_shoes", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_sar_t3_boots", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_sar_t4_camel", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_sar_t5_mail", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_sar_t6_mail", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_bo_sar_t7_greaves", "trp_sarranid_mamluke_multiplayer"),
		#Shields
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_sar_rou_plain", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_sar_rou_round", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_sar_rou_steel_a", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_sh_sar_rou_elite", "trp_sarranid_mamluke_multiplayer"),
		#Gauntlets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_sar_a2_leather", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_sar_a4_brass", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_sar_a5_scale", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_ga_sar_a6_lamellar", "trp_sarranid_mamluke_multiplayer"),
		#Helmets
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_sar_t1_common_a", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_sar_t2_tuareg_a", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_sar_t3_rabati_a", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_sar_t4_tuareg_a", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_sar_t5_horseman_a", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_sar_t6_spire_a", "trp_sarranid_mamluke_multiplayer"),
      (call_script, "script_multiplayer_set_item_available_for_troop", "itm_he_sar_t7_veiled_a", "trp_sarranid_mamluke_multiplayer"),

	  ##FLORIS
		##Floris MTT begin
		(assign, "$troop_trees", troop_trees_2), #Default on Expanded
		(call_script, "script_mtt_troop_slots"),
		##Floris MTT end
		(call_script, "script_floris_set_default_prefs", 1),
  ]),
  
  #script_get_army_size_from_slider_value
  # INPUT: arg1 = slider_value
  # OUTPUT: reg0 = army_size
  ("get_army_size_from_slider_value",
    [
      (store_script_param, ":slider_value", 1),
      (assign, ":army_size", ":slider_value"),
      (try_begin),
        (gt, ":slider_value", 25),
        (store_sub, ":adder_value", ":slider_value", 25),
        (val_add, ":army_size", ":adder_value"),
        (try_begin),
          (gt, ":slider_value", 50),
          (store_sub, ":adder_value", ":slider_value", 50),
          (val_mul, ":adder_value", 3),
          (val_add, ":army_size", ":adder_value"),
        (try_end),
      (try_end),
      (assign, reg0, ":army_size"),
  ]),
  
  #script_spawn_quick_battle_army
  # INPUT: arg1 = initial_entry_point, arg2 = faction_no, arg3 = infantry_ratio, arg4 = archers_ratio, arg5 = cavalry_ratio, arg6 = divide_archer_entry_points, arg7 = player_team
  # OUTPUT: none
  ("spawn_quick_battle_army",
    [
      (store_script_param, ":cur_entry_point", 1),
      (store_script_param, ":faction_no", 2),
      (store_script_param, ":infantry_ratio", 3),
      (store_script_param, ":archers_ratio", 4),
      (store_script_param, ":cavalry_ratio", 5),
      (store_script_param, ":divide_archer_entry_points", 6),
      (store_script_param, ":player_team", 7),
      
      (try_begin),
        (eq, ":player_team", 1),
        (call_script, "script_get_army_size_from_slider_value", "$g_quick_battle_army_1_size"),
        (assign, ":army_size", reg0),
        (set_player_troop, "$g_quick_battle_troop"),
        (set_visitor, ":cur_entry_point", "$g_quick_battle_troop"),
        (try_begin),
          (eq, ":cur_entry_point", 0),
          (try_begin),
            (is_between, ":faction_no", kingdoms_begin, kingdoms_end), #Player Faction
            (faction_get_slot, "$g_quick_battle_team_0_banner", ":faction_no", slot_faction_banner),
          (else_try),
            (assign, "$g_quick_battle_team_0_banner", "mesh_banners_default_b"),
          (try_end),
        (else_try),
          (try_begin),
            (is_between, ":faction_no", kingdoms_begin, kingdoms_end), #Player Faction
            (faction_get_slot, "$g_quick_battle_team_1_banner", ":faction_no", slot_faction_banner),
          (else_try),
            (assign, "$g_quick_battle_team_1_banner", "mesh_banners_default_b"),
          (try_end),
        (try_end),
        (val_add, ":cur_entry_point", 1),
        
      (else_try),
        (call_script, "script_get_army_size_from_slider_value", "$g_quick_battle_army_2_size"),
        (assign, ":army_size", reg0),
        (try_begin),
          (eq, ":cur_entry_point", 0),
          (assign, "$g_quick_battle_team_0_banner", "mesh_banners_default_a"),
        (else_try),
          (assign, "$g_quick_battle_team_1_banner", "mesh_banners_default_a"),
        (try_end),
        (val_add, ":cur_entry_point", 1),
      (try_end),
      
      (store_mul, ":num_infantry", ":infantry_ratio", ":army_size"),
      (val_div, ":num_infantry", 100),
      (store_mul, ":num_archers", ":archers_ratio", ":army_size"),
      (val_div, ":num_archers", 100),
      (store_mul, ":num_cavalry", ":cavalry_ratio", ":army_size"),
      (val_div, ":num_cavalry", 100),
      
      (try_begin),
        (store_add, ":num_total", ":num_infantry", ":num_archers"),
        (val_add, ":num_total", ":num_cavalry"),
        (neq, ":num_total", ":army_size"),
        (store_sub, ":leftover", ":army_size", ":num_total"),
        (try_begin),
          (gt, ":infantry_ratio", ":archers_ratio"),
          (gt, ":infantry_ratio", ":cavalry_ratio"),
          (val_add, ":num_infantry", ":leftover"),
        (else_try),
          (gt, ":archers_ratio", ":cavalry_ratio"),
          (val_add, ":num_archers", ":leftover"),
        (else_try),
          (val_add, ":num_cavalry", ":leftover"),
        (try_end),
      (try_end),
      
      (store_mul, ":rand_min", ":num_infantry", 15),
      (val_div, ":rand_min", 100),
      (store_mul, ":rand_max", ":num_infantry", 45),
      (val_div, ":rand_max", 100),
      (store_random_in_range, ":num_tier_2_infantry", ":rand_min", ":rand_max"),
      (store_sub, ":num_tier_1_infantry", ":num_infantry", ":num_tier_2_infantry"),
      (store_mul, ":rand_min", ":num_archers", 15),
      (val_div, ":rand_min", 100),
      (store_mul, ":rand_max", ":num_archers", 45),
      (val_div, ":rand_max", 100),
      (store_random_in_range, ":num_tier_2_archers", ":rand_min", ":rand_max"),
      (store_sub, ":num_tier_1_archers", ":num_archers", ":num_tier_2_archers"),
      (store_mul, ":rand_min", ":num_cavalry", 15),
      (val_div, ":rand_min", 100),
      (store_mul, ":rand_max", ":num_cavalry", 45),
      (val_div, ":rand_max", 100),
      (store_random_in_range, ":num_tier_2_cavalry", ":rand_min", ":rand_max"),
      (store_sub, ":num_tier_1_cavalry", ":num_cavalry", ":num_tier_2_cavalry"),
      
      (faction_get_slot, ":cur_troop", ":faction_no", slot_faction_quick_battle_tier_2_infantry),
      (set_visitors, ":cur_entry_point", ":cur_troop", ":num_tier_2_infantry"),
      (val_add, ":cur_entry_point", 1),
      (faction_get_slot, ":cur_troop", ":faction_no", slot_faction_quick_battle_tier_1_infantry),
      (set_visitors, ":cur_entry_point", ":cur_troop", ":num_tier_1_infantry"),
      (val_add, ":cur_entry_point", 1),
      (faction_get_slot, ":cur_troop", ":faction_no", slot_faction_quick_battle_tier_2_cavalry),
      (set_visitors, ":cur_entry_point", ":cur_troop", ":num_tier_2_cavalry"),
      (val_add, ":cur_entry_point", 1),
      (faction_get_slot, ":cur_troop", ":faction_no", slot_faction_quick_battle_tier_1_cavalry),
      (set_visitors, ":cur_entry_point", ":cur_troop", ":num_tier_1_cavalry"),
      (val_add, ":cur_entry_point", 1),
      
      (try_begin),
        (eq, ":divide_archer_entry_points", 0),
        (faction_get_slot, ":cur_troop", ":faction_no", slot_faction_quick_battle_tier_2_archer),
        (set_visitors, ":cur_entry_point", ":cur_troop", ":num_tier_2_archers"),
        (val_add, ":cur_entry_point", 1),
        (faction_get_slot, ":cur_troop", ":faction_no", slot_faction_quick_battle_tier_1_archer),
        (set_visitors, ":cur_entry_point", ":cur_troop", ":num_tier_1_archers"),
        (val_add, ":cur_entry_point", 1),
      (else_try),
        (assign, ":cur_entry_point", 40), #archer positions begin point
        (store_div, ":num_tier_1_archers_ceil_8", ":num_tier_1_archers", 8),
        (val_mul, ":num_tier_1_archers_ceil_8", 8),
        (try_begin),
          (neq, ":num_tier_1_archers_ceil_8", ":num_tier_1_archers"),
          (val_div, ":num_tier_1_archers_ceil_8", 8),
          (val_add, ":num_tier_1_archers_ceil_8", 1),
          (val_mul, ":num_tier_1_archers_ceil_8", 8),
        (try_end),
        (store_div, ":num_tier_2_archers_ceil_8", ":num_tier_2_archers", 8),
        (val_mul, ":num_tier_2_archers_ceil_8", 8),
        (try_begin),
          (neq, ":num_tier_2_archers_ceil_8", ":num_tier_2_archers"),
          (val_div, ":num_tier_2_archers_ceil_8", 8),
          (val_add, ":num_tier_2_archers_ceil_8", 1),
          (val_mul, ":num_tier_2_archers_ceil_8", 8),
        (try_end),
        (store_add, ":num_archers_ceil_8", ":num_tier_1_archers_ceil_8", ":num_tier_2_archers_ceil_8"),
        (store_div, ":num_archers_per_entry_point", ":num_archers_ceil_8", 8),
        (assign, ":left_tier_1_archers", ":num_tier_1_archers"),
        (assign, ":left_tier_2_archers", ":num_tier_2_archers"),
        (assign, ":end_cond", 1000),
        (try_for_range, ":unused", 0, ":end_cond"),
          (try_begin),
            (gt, ":left_tier_2_archers", 0),
            (assign, ":used_tier_2_archers", ":num_archers_per_entry_point"),
            (val_min, ":used_tier_2_archers", ":left_tier_2_archers"),
            (faction_get_slot, ":cur_troop", ":faction_no", slot_faction_quick_battle_tier_2_archer),
            (set_visitors, ":cur_entry_point", ":cur_troop", ":used_tier_2_archers"),
            (val_add, ":cur_entry_point", 1),
            (val_sub, ":left_tier_2_archers", ":used_tier_2_archers"),
          (else_try),
            (gt, ":left_tier_1_archers", 0),
            (assign, ":used_tier_1_archers", ":num_archers_per_entry_point"),
            (val_min, ":used_tier_1_archers", ":left_tier_1_archers"),
            (faction_get_slot, ":cur_troop", ":faction_no", slot_faction_quick_battle_tier_1_archer),
            (set_visitors, ":cur_entry_point", ":cur_troop", ":used_tier_1_archers"),
            (val_add, ":cur_entry_point", 1),
            (val_sub, ":left_tier_1_archers", ":used_tier_1_archers"),
          (else_try),
            (assign, ":end_cond", 0),
          (try_end),
        (try_end),
      (try_end),
  ]),
  
  ("player_arrived",
    [
      (assign, ":player_faction_culture", "fac_culture_1"),##Floris: Changed the 7 back into 1 to make it savegame compatible.
      (faction_set_slot, "fac_player_supporters_faction",  slot_faction_culture, ":player_faction_culture"),##Floris: Stayed the same.
      (faction_set_slot, "fac_player_faction",  slot_faction_culture, ":player_faction_culture"),
  ]),
  
  
  #script_game_set_multiplayer_mission_end
  # This script is called from the game engine when a multiplayer map is ended in clients (not in server).
  # INPUT:
  # none
  # OUTPUT:
  # none
  ("game_set_multiplayer_mission_end",
    [
      (assign, "$g_multiplayer_mission_end_screen", 1),
  ]),
  #script_game_enable_cheat_menu
  # This script is called from the game engine when user enters "cheatmenu from command console (ctrl+~).
  # INPUT:
  # none
  # OUTPUT:
  # none
  ("game_enable_cheat_menu",
    [
      (store_script_param, ":input", 1),
      (try_begin),
        (eq, ":input", 0),
        (assign, "$cheat_mode", 0),
      (else_try),
        (eq, ":input", 1),
        (assign, "$cheat_mode", 1),
      (try_end),
  ]),
  
  #script_game_get_console_command
  # This script is called from the game engine when a console command is entered from the dedicated server.
  # INPUT: anything
  # OUTPUT: s0 = result text
  ("game_get_console_command",
    [
      (store_script_param, ":input", 1),
      (store_script_param, ":val1", 2),
      (try_begin),
        #getting val2 for some commands
        (eq, ":input", 2),
        (store_script_param, ":val2", 3),
      (end_try),
      (try_begin),
        (eq, ":input", 1),
        (assign, reg0, ":val1"),
        (try_begin),
          (eq, ":val1", 1),
          (assign, reg1, "$g_multiplayer_num_bots_team_1"),
          (str_store_string, s0, "str_team_reg0_bot_count_is_reg1"),
        (else_try),
          (eq, ":val1", 2),
          (assign, reg1, "$g_multiplayer_num_bots_team_2"),
          (str_store_string, s0, "str_team_reg0_bot_count_is_reg1"),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 2),
        (assign, reg0, ":val1"),
        (assign, reg1, ":val2"),
        (try_begin),
          (eq, ":val1", 1),
          (ge, ":val2", 0),
          (assign, "$g_multiplayer_num_bots_team_1", ":val2"),
          (str_store_string, s0, "str_team_reg0_bot_count_is_reg1"),
        (else_try),
          (eq, ":val1", 2),
          (ge, ":val2", 0),
          (assign, "$g_multiplayer_num_bots_team_2", ":val2"),
          (str_store_string, s0, "str_team_reg0_bot_count_is_reg1"),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 3),
        (assign, reg0, "$g_multiplayer_round_max_seconds"),
        (str_store_string, s0, "str_maximum_seconds_for_round_is_reg0"),
      (else_try),
        (eq, ":input", 4),
        (assign, reg0, ":val1"),
        (try_begin),
          (is_between, ":val1", multiplayer_round_max_seconds_min, multiplayer_round_max_seconds_max),
          (assign, "$g_multiplayer_round_max_seconds", ":val1"),
          (str_store_string, s0, "str_maximum_seconds_for_round_is_reg0"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_round_max_seconds, ":val1"),
          (try_end),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 5),
        (assign, reg0, "$g_multiplayer_respawn_period"),
        (str_store_string, s0, "str_respawn_period_is_reg0_seconds"),
      (else_try),
        (eq, ":input", 6),
        (assign, reg0, ":val1"),
        (try_begin),
          (is_between, ":val1", multiplayer_respawn_period_min, multiplayer_respawn_period_max),
          (assign, "$g_multiplayer_respawn_period", ":val1"),
          (str_store_string, s0, "str_respawn_period_is_reg0_seconds"),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 7),
        (assign, reg0, "$g_multiplayer_num_bots_voteable"),
        (str_store_string, s0, "str_bots_upper_limit_for_votes_is_reg0"),
      (else_try),
        (eq, ":input", 8),
        (try_begin),
          (is_between, ":val1", 0, 51),
          (assign, "$g_multiplayer_num_bots_voteable", ":val1"),
          (store_add, "$g_multiplayer_max_num_bots", ":val1", 1),
          (assign, reg0, "$g_multiplayer_num_bots_voteable"),
          (str_store_string, s0, "str_bots_upper_limit_for_votes_is_reg0"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_num_bots_voteable, ":val1"),
          (try_end),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 9),
        (try_begin),
          (eq, "$g_multiplayer_maps_voteable", 1),
          (str_store_string, s0, "str_map_is_voteable"),
        (else_try),
          (str_store_string, s0, "str_map_is_not_voteable"),
        (try_end),
      (else_try),
        (eq, ":input", 10),
        (try_begin),
          (is_between, ":val1", 0, 2),
          (assign, "$g_multiplayer_maps_voteable", ":val1"),
          (try_begin),
            (eq, ":val1", 1),
            (str_store_string, s0, "str_map_is_voteable"),
          (else_try),
            (str_store_string, s0, "str_map_is_not_voteable"),
          (try_end),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_maps_voteable, ":val1"),
          (try_end),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 11),
        (try_begin),
          (eq, "$g_multiplayer_factions_voteable", 1),
          (str_store_string, s0, "str_factions_are_voteable"),
        (else_try),
          (str_store_string, s0, "str_factions_are_not_voteable"),
        (try_end),
      (else_try),
        (eq, ":input", 12),
        (try_begin),
          (is_between, ":val1", 0, 2),
          (assign, "$g_multiplayer_factions_voteable", ":val1"),
          (try_begin),
            (eq, ":val1", 1),
            (str_store_string, s0, "str_factions_are_voteable"),
          (else_try),
            (str_store_string, s0, "str_factions_are_not_voteable"),
          (try_end),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_factions_voteable, ":val1"),
          (try_end),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 13),
        (try_begin),
          (eq, "$g_multiplayer_player_respawn_as_bot", 1),
          (str_store_string, s0, "str_players_respawn_as_bot"),
        (else_try),
          (str_store_string, s0, "str_players_do_not_respawn_as_bot"),
        (try_end),
      (else_try),
        (eq, ":input", 14),
        (try_begin),
          (is_between, ":val1", 0, 2),
          (assign, "$g_multiplayer_player_respawn_as_bot", ":val1"),
          (try_begin),
            (eq, ":val1", 1),
            (str_store_string, s0, "str_players_respawn_as_bot"),
          (else_try),
            (str_store_string, s0, "str_players_do_not_respawn_as_bot"),
          (try_end),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_player_respawn_as_bot, ":val1"),
          (try_end),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 15),
        (try_begin),
          (eq, "$g_multiplayer_kick_voteable", 1),
          (str_store_string, s0, "str_kicking_a_player_is_voteable"),
        (else_try),
          (str_store_string, s0, "str_kicking_a_player_is_not_voteable"),
        (try_end),
      (else_try),
        (eq, ":input", 16),
        (try_begin),
          (is_between, ":val1", 0, 2),
          (assign, "$g_multiplayer_kick_voteable", ":val1"),
          (try_begin),
            (eq, ":val1", 1),
            (str_store_string, s0, "str_kicking_a_player_is_voteable"),
          (else_try),
            (str_store_string, s0, "str_kicking_a_player_is_not_voteable"),
          (try_end),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_kick_voteable, ":val1"),
          (try_end),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 17),
        (try_begin),
          (eq, "$g_multiplayer_ban_voteable", 1),
          (str_store_string, s0, "str_banning_a_player_is_voteable"),
        (else_try),
          (str_store_string, s0, "str_banning_a_player_is_not_voteable"),
        (try_end),
      (else_try),
        (eq, ":input", 18),
        (try_begin),
          (is_between, ":val1", 0, 2),
          (assign, "$g_multiplayer_ban_voteable", ":val1"),
          (try_begin),
            (eq, ":val1", 1),
            (str_store_string, s0, "str_banning_a_player_is_voteable"),
          (else_try),
            (str_store_string, s0, "str_banning_a_player_is_not_voteable"),
          (try_end),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_ban_voteable, ":val1"),
          (try_end),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 19),
        (assign, reg0, "$g_multiplayer_valid_vote_ratio"),
        (str_store_string, s0, "str_percentage_of_yes_votes_required_for_a_poll_to_get_accepted_is_reg0"),
      (else_try),
        (eq, ":input", 20),
        (try_begin),
          (is_between, ":val1", 50, 101),
          (assign, "$g_multiplayer_valid_vote_ratio", ":val1"),
          (assign, reg0, ":val1"),
          (str_store_string, s0, "str_percentage_of_yes_votes_required_for_a_poll_to_get_accepted_is_reg0"),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 21),
        (assign, reg0, "$g_multiplayer_auto_team_balance_limit"),
        (str_store_string, s0, "str_auto_team_balance_threshold_is_reg0"),
      (else_try),
        (eq, ":input", 22),
        (try_begin),
          (is_between, ":val1", 2, 7),
          (assign, "$g_multiplayer_auto_team_balance_limit", ":val1"),
          (assign, reg0, "$g_multiplayer_auto_team_balance_limit"),
          (str_store_string, s0, "str_auto_team_balance_threshold_is_reg0"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_auto_team_balance_limit, ":val1"),
          (try_end),
        (else_try),
          (ge, ":val1", 7),
          (assign, "$g_multiplayer_auto_team_balance_limit", 1000),
          (assign, reg0, "$g_multiplayer_auto_team_balance_limit"),
          (str_store_string, s0, "str_auto_team_balance_threshold_is_reg0"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_auto_team_balance_limit, ":val1"),
          (try_end),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 23),
        (assign, reg0, "$g_multiplayer_initial_gold_multiplier"),
        (str_store_string, s0, "str_starting_gold_ratio_is_reg0"),
      (else_try),
        (eq, ":input", 24),
        (try_begin),
          (is_between, ":val1", 0, 1001),
          (assign, "$g_multiplayer_initial_gold_multiplier", ":val1"),
          (assign, reg0, "$g_multiplayer_initial_gold_multiplier"),
          (str_store_string, s0, "str_starting_gold_ratio_is_reg0"),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 25),
        (assign, reg0, "$g_multiplayer_battle_earnings_multiplier"),
        (str_store_string, s0, "str_combat_gold_bonus_ratio_is_reg0"),
      (else_try),
        (eq, ":input", 26),
        (try_begin),
          (is_between, ":val1", 0, 1001),
          (assign, "$g_multiplayer_battle_earnings_multiplier", ":val1"),
          (assign, reg0, "$g_multiplayer_battle_earnings_multiplier"),
          (str_store_string, s0, "str_combat_gold_bonus_ratio_is_reg0"),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 27),
        (assign, reg0, "$g_multiplayer_round_earnings_multiplier"),
        (str_store_string, s0, "str_round_gold_bonus_ratio_is_reg0"),
      (else_try),
        (eq, ":input", 28),
        (try_begin),
          (is_between, ":val1", 0, 1001),
          (assign, "$g_multiplayer_round_earnings_multiplier", ":val1"),
          (assign, reg0, "$g_multiplayer_round_earnings_multiplier"),
          (str_store_string, s0, "str_round_gold_bonus_ratio_is_reg0"),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 29),
        (try_begin),
          (eq, "$g_multiplayer_allow_player_banners", 1),
          (str_store_string, s0, "str_player_banners_are_allowed"),
        (else_try),
          (str_store_string, s0, "str_player_banners_are_not_allowed"),
        (try_end),
      (else_try),
        (eq, ":input", 30),
        (try_begin),
          (is_between, ":val1", 0, 2),
          (assign, "$g_multiplayer_allow_player_banners", ":val1"),
          (try_begin),
            (eq, ":val1", 1),
            (str_store_string, s0, "str_player_banners_are_allowed"),
          (else_try),
            (str_store_string, s0, "str_player_banners_are_not_allowed"),
          (try_end),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 31),
        (try_begin),
          (eq, "$g_multiplayer_force_default_armor", 1),
          (str_store_string, s0, "str_default_armor_is_forced"),
        (else_try),
          (str_store_string, s0, "str_default_armor_is_not_forced"),
        (try_end),
      (else_try),
        (eq, ":input", 32),
        (try_begin),
          (is_between, ":val1", 0, 2),
          (assign, "$g_multiplayer_force_default_armor", ":val1"),
          (try_begin),
            (eq, ":val1", 1),
            (str_store_string, s0, "str_default_armor_is_forced"),
          (else_try),
            (str_store_string, s0, "str_default_armor_is_not_forced"),
          (try_end),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 33),
        (assign, reg0, "$g_multiplayer_point_gained_from_flags"),
        (str_store_string, s0, "str_point_gained_from_flags_is_reg0"),
      (else_try),
        (eq, ":input", 34),
        (try_begin),
          (is_between, ":val1", 25, 401),
          (assign, "$g_multiplayer_point_gained_from_flags", ":val1"),
          (assign, reg0, "$g_multiplayer_point_gained_from_flags"),
          (str_store_string, s0, "str_point_gained_from_flags_is_reg0"),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 35),
        (assign, reg0, "$g_multiplayer_point_gained_from_capturing_flag"),
        (str_store_string, s0, "str_point_gained_from_capturing_flag_is_reg0"),
      (else_try),
        (eq, ":input", 36),
        (try_begin),
          (is_between, ":val1", 0, 11),
          (assign, "$g_multiplayer_point_gained_from_capturing_flag", ":val1"),
          (assign, reg0, "$g_multiplayer_point_gained_from_capturing_flag"),
          (str_store_string, s0, "str_point_gained_from_capturing_flag_is_reg0"),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 37),
        (assign, reg0, "$g_multiplayer_game_max_minutes"),
        (str_store_string, s0, "str_map_time_limit_is_reg0"),
      (else_try),
        (eq, ":input", 38),
        (try_begin),
          (is_between, ":val1", 5, 121),
          (assign, "$g_multiplayer_game_max_minutes", ":val1"),
          (assign, reg0, "$g_multiplayer_game_max_minutes"),
          (str_store_string, s0, "str_map_time_limit_is_reg0"),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 39),
        (assign, reg0, "$g_multiplayer_game_max_points"),
        (str_store_string, s0, "str_team_points_limit_is_reg0"),
      (else_try),
        (eq, ":input", 40),
        (try_begin),
          (is_between, ":val1", 3, 1001),
          (assign, "$g_multiplayer_game_max_points", ":val1"),
          (assign, reg0, "$g_multiplayer_game_max_points"),
          (str_store_string, s0, "str_team_points_limit_is_reg0"),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 41),
        (assign, reg0, "$g_multiplayer_number_of_respawn_count"),
        (try_begin),
          (eq, reg0, 0),
          (str_store_string, s1, "str_unlimited"),
        (else_try),
          (str_store_string, s1, "str_reg0"),
        (try_end),
        (str_store_string, s0, "str_defender_spawn_count_limit_is_s1"),
      (else_try),
        (eq, ":input", 42),
        (try_begin),
          (is_between, ":val1", 0, 6),
          (assign, "$g_multiplayer_number_of_respawn_count", ":val1"),
          (assign, reg0, "$g_multiplayer_number_of_respawn_count"),
          (try_begin),
            (eq, reg0, 0),
            (str_store_string, s1, "str_unlimited"),
          (else_try),
            (str_store_string, s1, "str_reg0"),
          (try_end),
          (str_store_string, s0, "str_defender_spawn_count_limit_is_s1"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_respawn_count, ":val1"),
          (try_end),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (eq, ":input", 43),
        (try_begin),
          (eq, "$g_multiplayer_disallow_ranged_weapons", 1),
          (str_store_string, s0, "str_ranged_weapons_are_disallowed"),
        (else_try),
          (str_store_string, s0, "str_ranged_weapons_are_allowed"),
        (try_end),
      (else_try),
        (eq, ":input", 44),
        (try_begin),
          (is_between, ":val1", 0, 2),
          (assign, "$g_multiplayer_disallow_ranged_weapons", ":val1"),
          (try_begin),
            (eq, ":val1", 1),
            (str_store_string, s0, "str_ranged_weapons_are_disallowed"),
          (else_try),
            (str_store_string, s0, "str_ranged_weapons_are_allowed"),
          (try_end),
        (else_try),
          (str_store_string, s0, "str_input_is_not_correct_for_the_command_type_help_for_more_information"),
        (try_end),
      (else_try),
        (str_store_string, s0, "@{!}DEBUG : SYSTEM ERROR!"),
      (try_end),
  ]),
  
  
  # script_game_event_party_encounter:
  # This script is called from the game engine whenever player party encounters another party or a battle on the world map
  # INPUT:
  # param1: encountered_party
  # param2: second encountered_party (if this was a battle
  ("game_event_party_encounter",
    [
      (store_script_param_1, "$g_encountered_party"),
      (store_script_param_2, "$g_encountered_party_2"),# encountered_party2 is set when we come across a battle or siege, otherwise it's a negative value
      #       (store_encountered_party, "$g_encountered_party"),
      #       (store_encountered_party2,"$g_encountered_party_2"), # encountered_party2 is set when we come across a battle or siege, otherwise it's a minus value
      (store_faction_of_party, "$g_encountered_party_faction","$g_encountered_party"),
      (store_relation, "$g_encountered_party_relation", "$g_encountered_party_faction", "fac_player_faction"),
      
      (party_get_slot, "$g_encountered_party_type", "$g_encountered_party", slot_party_type),
      (party_get_template_id,"$g_encountered_party_template","$g_encountered_party"),
      #       (try_begin),
      #         (gt, "$g_encountered_party_2", 0),
      #         (store_faction_of_party, "$g_encountered_party_2_faction","$g_encountered_party_2"),
      #         (store_relation, "$g_encountered_party_2_relation", "$g_encountered_party_2_faction", "fac_player_faction"),
      #         (party_get_template_id,"$g_encountered_party_2_template","$g_encountered_party_2"),
      #       (else_try),
      #         (assign, "$g_encountered_party_2_faction",-1),
      #         (assign, "$g_encountered_party_2_relation", 0),
      #         (assign,"$g_encountered_party_2_template", -1),
      #       (try_end),
      
      #NPC companion changes begin
      (call_script, "script_party_count_fit_regulars", "p_main_party"),
      (assign, "$playerparty_prebattle_regulars", reg0),
      
      #        (try_begin),
      #            (assign, "$player_party__regulars", 0),
      #            (call_script, "script_party_count_fit_regulars", "p_main_party"),
      #            (gt, reg0, 0),
      #            (assign, "$player_party_contains_regulars", 1),
      #        (try_end),
      #NPC companion changes end
      
      
      (assign, "$g_last_rest_center", -1),
      (assign, "$talk_context", 0),
      (assign,"$g_player_surrenders",0),
      (assign,"$g_enemy_surrenders",0),
      (assign, "$g_leave_encounter",0),
      (assign, "$g_engaged_enemy", 0),
      #       (assign,"$waiting_for_arena_fight_result", 0),
      #       (assign,"$arena_bet_amount",0),
      #       (assign,"$g_player_raiding_village",0),
      (try_begin),
        (neg|is_between, "$g_encountered_party", centers_begin, centers_end),
        (rest_for_hours, 0), #stop waiting
        (assign, "$g_infinite_camping", 0),
      (try_end),
      #       (assign, "$g_permitted_to_center",0),
      (assign, "$new_encounter", 1), #check this in the menu.
      (try_begin),
        (lt, "$g_encountered_party_2",0), #Normal encounter. Not battle or siege.
        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
          (jump_to_menu, "mnu_castle_outside"),
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
          (jump_to_menu, "mnu_castle_outside"),
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_ship),
          (jump_to_menu, "mnu_ship_reembark"),
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_village),
          (jump_to_menu, "mnu_village"),
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_cattle_herd),
          (jump_to_menu, "mnu_cattle_herd"),
        (else_try),
          (is_between, "$g_encountered_party", training_grounds_begin, training_grounds_end),
          (jump_to_menu, "mnu_training_ground"),
        (else_try),
		  (party_slot_eq, "$g_encountered_party", slot_party_type, spt_bandit_lair), ##Floris MTT - needed due to nested try block
		  (party_get_template_id, ":template", "$g_encountered_party"),
				##Floris MTT begin
				(try_begin),
		 			(eq, "$troop_trees", troop_trees_0),
					(ge, ":template", "pt_steppe_bandit_lair"), ## CC fix
					(lt, ":template", "pt_bandit_lair_templates_end"),
					(assign, "$loot_screen_shown", 0),
					#(call_script, "script_encounter_init_variables"),
					(jump_to_menu, "mnu_bandit_lair"),
				(else_try),
		 			(eq, "$troop_trees", troop_trees_1),
					(ge, ":template", "pt_steppe_bandit_lair_r"), ## CC fix
					(lt, ":template", "pt_bandit_lair_templates_end_r"),
					(assign, "$loot_screen_shown", 0),
					#(call_script, "script_encounter_init_variables"),
					(jump_to_menu, "mnu_bandit_lair"),
				(else_try),
					(eq, "$troop_trees", troop_trees_2),
					(ge, ":template", "pt_steppe_bandit_lair_e"), ## CC fix
					(lt, ":template", "pt_bandit_lair_templates_end_e"),
					(assign, "$loot_screen_shown", 0),
					#(call_script, "script_encounter_init_variables"),
					(jump_to_menu, "mnu_bandit_lair"),
				(try_end),
				##Floris MTT end
        (else_try),
          (eq, "$g_encountered_party", "p_zendar"),
          (jump_to_menu, "mnu_zendar"),
        (else_try),
          (eq, "$g_encountered_party", "p_salt_mine"),
          (jump_to_menu, "mnu_salt_mine"),
        (else_try),
          (eq, "$g_encountered_party", "p_four_ways_inn"),
          (jump_to_menu, "mnu_four_ways_inn"),
        (else_try),
          (eq, "$g_encountered_party", "p_test_scene"),
          (jump_to_menu, "mnu_test_scene"),
		(else_try),
          (eq, "$g_encountered_party", "p_battlefields"),
          (jump_to_menu, "mnu_battlefields"),
        (else_try),
          (eq, "$g_encountered_party", "p_training_ground"),
          (jump_to_menu, "mnu_tutorial"),
        (else_try),
          (eq, "$g_encountered_party", "p_camp_bandits"),
          (jump_to_menu, "mnu_camp"),
        (else_try),
          (jump_to_menu, "mnu_simple_encounter"),
        (try_end),
      (else_try), #Battle or siege
        (try_begin),
          (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
          (try_begin),
            (eq, "$auto_enter_town", "$g_encountered_party"),
            (jump_to_menu, "mnu_town"),
          (else_try),
            (eq, "$auto_besiege_town", "$g_encountered_party"),
            (jump_to_menu, "mnu_besiegers_camp_with_allies"),
          (else_try),
            (jump_to_menu, "mnu_join_siege_outside"),
          (try_end),
        (else_try),
          (jump_to_menu, "mnu_pre_join"),
        (try_end),
      (try_end),
      (assign,"$auto_enter_town",0),
      (assign,"$auto_besiege_town",0),
  ]),
  
  #script_game_event_simulate_battle:
  # This script is called whenever the game simulates the battle between two parties on the map.
  # INPUT:
  # param1: Defender Party
  # param2: Attacker Party
  ("game_event_simulate_battle",
    [
      (store_script_param_1, ":root_defender_party"),
      (store_script_param_2, ":root_attacker_party"),
      
      (assign, "$marshall_defeated_in_battle", -1),
      
      (store_current_hours, ":hours"),
	  
	  ##diplomacy start+ Get campaign AI, used below
      (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
      ##diplomacy end+
      
      (try_for_parties, ":party"),
        (party_get_battle_opponent, ":opponent", ":party"),
        (gt, ":opponent", 0),
        (party_set_slot, ":party", slot_party_last_in_combat, ":hours"),
      (try_end),
      
      (assign, ":trigger_result", 1), ##1.134
      (try_begin),
        (ge, ":root_defender_party", 0),
        (ge, ":root_attacker_party", 0),
        (party_is_active, ":root_defender_party"),
        (party_is_active, ":root_attacker_party"),
        (store_faction_of_party, ":defender_faction", ":root_defender_party"),
        (store_faction_of_party, ":attacker_faction", ":root_attacker_party"),
        #(neq, ":defender_faction", "fac_player_faction"),					1.143 Port
        #(neq, ":attacker_faction", "fac_player_faction"),
        (store_relation, ":reln", ":defender_faction", ":attacker_faction"),
        ## Removed in 1.134
        #        (ge, ":reln", 0),
        #        (set_trigger_result, 1),
        #      (else_try),
        ##
        (lt, ":reln", 0), ##1.134
        (assign, ":trigger_result", 0),
        
        (try_begin),
          (this_or_next|eq, "$g_battle_simulation_cancel_for_party", ":root_defender_party"),
          (eq, "$g_battle_simulation_cancel_for_party", ":root_attacker_party"),
          (assign, "$g_battle_simulation_cancel_for_party", -1),
          (assign, "$auto_enter_town", "$g_battle_simulation_auto_enter_town_after_battle"),
          (assign, ":trigger_result", 1),
        (else_try),
          (try_begin),
            (this_or_next|party_slot_eq, ":root_defender_party", slot_party_retreat_flag, 1),
            (party_slot_eq, ":root_attacker_party", slot_party_retreat_flag, 1),
            (assign, ":trigger_result", 1), #End battle!
          (try_end),
          (party_set_slot, ":root_attacker_party", slot_party_retreat_flag, 0),
          
          #(assign, ":cancel_attack", 0),
          
          (party_collect_attachments_to_party, ":root_defender_party", "p_collective_ally"),
          (party_collect_attachments_to_party, ":root_attacker_party", "p_collective_enemy"),
          
	      ##diplomacy start+
 		  (assign, ":terrain_code", dplmc_terrain_code_none),#defined in header_terrain.py
          (try_begin),
              (eq, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
			  (call_script, "script_dplmc_get_terrain_code_for_battle", ":root_attacker_party", ":root_defender_party"),
			  (assign, ":terrain_code", reg0),
			  #
              (call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_collective_ally", ":terrain_code", 0, 1),
              (assign, ":defender_strength", reg0),
              (call_script, "script_dplmc_party_calculate_strength_in_terrain", "p_collective_enemy", ":terrain_code", 0, 1),
              (assign, ":attacker_strength", reg0),
          (else_try),
              (call_script, "script_party_calculate_strength", "p_collective_ally", 0),
              (assign, ":defender_strength", reg0),
              (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
              (assign, ":attacker_strength", reg0),
          (try_end),
          ##diplomacy end+
          
          (store_div, ":defender_strength", ":defender_strength", 20),
          (val_min, ":defender_strength", 50),
          (val_max, ":defender_strength", 1),
          (store_div, ":attacker_strength", ":attacker_strength", 20),
          (val_min, ":attacker_strength", 50),
          (val_add, ":attacker_strength", 1),
          (try_begin),
            #For sieges increase attacker casualties and reduce defender casualties.
            (this_or_next|party_slot_eq, ":root_defender_party", slot_party_type, spt_castle),
            (party_slot_eq, ":root_defender_party", slot_party_type, spt_town),
            (val_mul, ":defender_strength", 123), #it was 1.5 in old version, now it is only 1.23
            (val_div, ":defender_strength", 100),
            
            (val_mul, ":attacker_strength", 100), #it was 0.5 in old version, now it is only 1 / 1.23
            (val_div, ":attacker_strength", 123),
          (try_end),
          
          ##diplomacy begin
          (assign, ":defender_percent", 100),
          (try_begin),
            (faction_get_slot, ":serfdom", ":defender_faction", dplmc_slot_faction_serfdom),
            (neq, ":serfdom", 0),
            (val_mul, ":serfdom", -2),
            (val_add, ":defender_percent", ":serfdom"),
          (try_end),
          (try_begin),
            (faction_get_slot, ":quality", ":defender_faction", dplmc_slot_faction_quality),
            (neq, ":quality", 0),
            (val_mul, ":quality", 4),
            (val_add, ":defender_percent", ":quality"),
          (try_end),
          (val_mul, ":defender_strength", ":defender_percent"),
          (val_div, ":defender_strength", 100),
          
          (assign, ":attacker_percent", 100),
          (try_begin),
            (faction_get_slot, ":serfdom", ":attacker_faction", dplmc_slot_faction_serfdom),
            (neq, ":serfdom", 0),
            (val_mul, ":serfdom", -2),
            (val_add, ":attacker_percent", ":serfdom"),
          (try_end),
          (try_begin),
            (faction_get_slot, ":quality", ":attacker_faction", dplmc_slot_faction_quality),
            (neq, ":quality", 0),
            (val_mul, ":quality", 4),
            (val_add, ":attacker_percent", ":quality"),
          (try_end),
          (val_mul, ":attacker_strength", ":attacker_percent"),
          (val_div, ":attacker_strength", 100),
          ##diplomacy end
          
          (call_script, "script_party_count_fit_for_battle", "p_collective_ally", 0),
          (assign, ":old_defender_strength", reg0),
          
          ## CC
          (val_max, "$g_speed_ai_battles", 1),
          (try_for_range, ":unused", 0, "$g_speed_ai_battles"), # speed
            (try_begin),
              (neg|is_currently_night), #Don't fight at night
              (inflict_casualties_to_party_group, ":root_attacker_party", ":defender_strength", "p_temp_casualties"),
              (party_collect_attachments_to_party, ":root_attacker_party", "p_collective_enemy"),
            (try_end),
            (call_script, "script_party_count_fit_for_battle", "p_collective_enemy", 0),
            (assign, ":new_attacker_strength", reg0),
            (try_begin),
              (gt, ":new_attacker_strength", 0),
              (neg|is_currently_night), #Don't fight at night
              (inflict_casualties_to_party_group, ":root_defender_party", ":attacker_strength", "p_temp_casualties"),
              (party_collect_attachments_to_party, ":root_defender_party", "p_collective_ally"),
            (try_end),
            (call_script, "script_party_count_fit_for_battle", "p_collective_ally", 0),
            (assign, ":new_defender_strength", reg0),
          (try_end),
          ## CC
          
          (try_begin),
            (neg|is_currently_night), #Don't fight at night
            (inflict_casualties_to_party_group, ":root_attacker_party", ":defender_strength", "p_temp_casualties"),
            (party_collect_attachments_to_party, ":root_attacker_party", "p_collective_enemy"),
          (try_end),
          (call_script, "script_party_count_fit_for_battle", "p_collective_enemy", 0),
          (assign, ":new_attacker_strength", reg0),
          
          (try_begin),
            (gt, ":new_attacker_strength", 0),
            (neg|is_currently_night), #Don't fight at night
            (inflict_casualties_to_party_group, ":root_defender_party", ":attacker_strength", "p_temp_casualties"),
            (party_collect_attachments_to_party, ":root_defender_party", "p_collective_ally"),
          (try_end),
          (call_script, "script_party_count_fit_for_battle", "p_collective_ally", 0),
          (assign, ":new_defender_strength", reg0),
          
          (try_begin),
            (this_or_next|eq, ":new_attacker_strength", 0),
            (eq, ":new_defender_strength", 0),
            # Battle concluded! determine winner
            
            (assign, ":do_not_end_battle", 0),
            (try_begin),
              (neg|troop_is_wounded, "trp_player"),
              (eq, ":new_defender_strength", 0),
              (eq, "$auto_enter_town", "$g_encountered_party"),
              (eq, ":old_defender_strength", ":new_defender_strength"),
              (assign, ":do_not_end_battle", 1),
            (try_end),
            (eq, ":do_not_end_battle", 0),
            
            (try_begin),
              (eq, ":new_attacker_strength", 0),
              (eq, ":new_defender_strength", 0),
              (assign, ":root_winner_party", -1),
              (assign, ":root_defeated_party", -1),
              (assign, ":collective_casualties", -1),
            (else_try),
              (eq, ":new_attacker_strength", 0),
              (assign, ":root_winner_party", ":root_defender_party"),
              (assign, ":root_defeated_party", ":root_attacker_party"),
              (assign, ":collective_casualties", "p_collective_enemy"),
            (else_try),
              (assign, ":root_winner_party", ":root_attacker_party"),
              (assign, ":root_defeated_party", ":root_defender_party"),
              (assign, ":collective_casualties", "p_collective_ally"),
            (try_end),
		    ## Floris - Trade with Merchant Caravans 
			(try_begin),
				(gt, ":root_defeated_party", -1),
				(party_slot_eq, ":root_defeated_party", slot_party_type, spt_kingdom_caravan),
				(party_get_slot, ":num_goods", ":root_defeated_party", slot_town_trade_good_productions_begin),
				(party_set_slot, ":root_defeated_party", slot_town_wealth, 0),
				(party_set_slot, ":root_defeated_party", slot_town_prosperity, 0),
				(gt, ":num_goods", 0),
				(val_add, ":num_goods", 1),
				(try_for_range, ":i", 1, ":num_goods"),
					(store_add, ":slot", slot_town_trade_good_productions_begin, ":i"), 
					(party_set_slot, ":root_defeated_party", ":slot", 0),	
				(try_end),
			(try_end),	
			## Floris - Trade with Merchant Caravans 
            ##diplomacy begin
            (try_begin),
              (gt, ":root_defeated_party", -1),
              # Recruiter kit begin
              # This little fella just shows a message when a recruiter is defeated.
              
              (assign, ":minimum_distance", 1000000),
              (try_for_range, ":center", centers_begin, centers_end),
                (store_distance_to_party_from_party, ":dist", ":root_defeated_party", ":center"),
                (try_begin),
                  (lt, ":dist", ":minimum_distance"),
                  (assign, ":minimum_distance", ":dist"),
                  (assign, ":nearest_center", ":center"),
                (try_end),
              (try_end),
              
              (str_clear, s10),
              (try_begin),
                (gt, ":nearest_center", 0),
                (str_store_party_name, s10, ":nearest_center"),
                (str_store_string, s10, "@ near {s10}"),
              (try_end),
              
              (try_begin),
                (party_slot_eq, ":root_defeated_party", slot_party_type, dplmc_spt_recruiter),
                (party_get_slot, reg10, ":root_defeated_party", dplmc_slot_party_recruiter_needed_recruits),
                (party_get_slot, ":party_origin", ":root_defeated_party", dplmc_slot_party_recruiter_origin),
                (str_store_party_name_link, s13, ":party_origin"),
                (display_log_message, "@Your recruiter who was commissioned to recruit {reg10} recruits to {s13} has been defeated{s10}!", 0xFF0000),
              (try_end),
              # Recruiter kit end
              
              (try_begin),
                (party_slot_eq,":root_defeated_party", slot_party_type, dplmc_spt_gift_caravan),
                
                (party_get_slot, ":target_troop", ":root_defeated_party", slot_party_orders_object),
                (party_get_slot, ":target_party", ":root_defeated_party", slot_party_ai_object),
                (try_begin),
                  (gt, ":target_troop", 0),
                  (str_store_troop_name, s13, ":target_troop"),
                (else_try),
                  (str_store_party_name, s13, ":target_party"),
                (end_try),
                (party_get_slot, ":gift", ":root_defeated_party", dplmc_slot_party_mission_diplomacy),
                (str_store_item_name, s12, ":gift"),
                (display_log_message, "@Your caravan sending {s12} to {s13} has been defeated{s10}!", 0xFF0000),
              (try_end),
              
              (try_begin),
                (party_slot_eq,":root_defeated_party", slot_party_type, spt_messenger),
                (party_get_slot, ":target_party", ":root_defeated_party", slot_party_orders_object),
                (party_stack_get_troop_id, ":party_leader", ":target_party", 0),
                (str_store_troop_name, s13, ":party_leader"),
                (display_log_message, "@Your messenger on the way to {s13} has been defeated{s10}!", 0xFF0000),
              (try_end),
              
              (try_begin),
                (party_slot_eq,":root_defeated_party", slot_party_type, spt_patrol),
                #          (party_slot_eq, ":root_defeated_party", dplmc_slot_party_mission_diplomacy, "trp_player"), #Diplomacy 3.3.2, disabled because of a bug.
                (store_faction_of_party, ":party_faction", ":root_defeated_party"),
                (eq, ":party_faction", "fac_player_faction"),
                (party_get_slot, ":target_party", ":root_defeated_party", slot_party_ai_object),
                (str_store_party_name, s13, ":target_party"),
                (display_log_message, "@Your soldiers patrolling {s13} have been defeated{s10}!", 0xFF0000),
              (try_end),
              
              (try_begin),
                (party_slot_eq,":root_defeated_party", slot_party_type, spt_scout),
                (store_faction_of_party, ":party_faction", ":root_defeated_party"),
                (eq, ":party_faction", "$players_kingdom"),
                (party_get_slot, ":target_party", ":root_defeated_party", slot_party_orders_object),
                (str_store_party_name, s13, ":target_party"),
                (display_log_message, "@A scout trying to gather information about {s13} has been slain{s10}!", 0xFF0000),
              (try_end),
            (try_end),
            ##diplomacy end
            
            (try_begin),
              (ge, ":root_winner_party", 0),
              (call_script, "script_get_nonempty_party_in_group", ":root_winner_party"),
              (assign, ":nonempty_winner_party", reg0),
              (store_faction_of_party, ":faction_receiving_prisoners", ":nonempty_winner_party"),
              (store_faction_of_party, ":defeated_faction", ":root_defeated_party"),
            (else_try),
              (assign, ":nonempty_winner_party", -1),
            (try_end),
            
            (try_begin),
              (ge, ":collective_casualties", 0),
              (party_get_num_companion_stacks, ":num_stacks", ":collective_casualties"),
            (else_try),
              (assign, ":num_stacks", 0),
            (try_end),
            
            (try_for_range, ":troop_iterator", 0, ":num_stacks"),
              (party_stack_get_troop_id, ":cur_troop_id", ":collective_casualties", ":troop_iterator"),
              (troop_is_hero, ":cur_troop_id"),
			  
              ## Start 1.134
              (try_begin),
                #abort quest if troop loses a battle during rest time
                (check_quest_active, "qst_lend_surgeon"),
                (quest_slot_eq, "qst_lend_surgeon", slot_quest_giver_troop, ":cur_troop_id"),
                (call_script, "script_abort_quest", "qst_lend_surgeon", 0),
              (try_end),
              ## End 1.134
              
              (call_script, "script_remove_troop_from_prison", ":cur_troop_id"),
              
              (troop_set_slot, ":cur_troop_id", slot_troop_leaded_party, -1),
              
              (store_random_in_range, ":rand", 0, 100),
              (str_store_troop_name_link, s1, ":cur_troop_id"),
              (str_store_faction_name_link, s2, ":faction_receiving_prisoners"),
              (store_troop_faction, ":defeated_troop_faction", ":cur_troop_id"),
              (str_store_faction_name_link, s3, ":defeated_troop_faction"),
              (try_begin),
                (ge, ":rand", hero_escape_after_defeat_chance),
                (neq, ":defeated_troop_faction", "fac_outlaws"), ## CC
				(party_stack_get_troop_id, ":leader_troop_id", ":nonempty_winner_party", 0),
                ##diplomacy start+ kingdom ladies might lead kingdom parties
                (this_or_next|is_between,":leader_troop_id", kingdom_ladies_begin, kingdom_ladies_end),
                (is_between, ":leader_troop_id", active_npcs_begin, active_npcs_end),
                (this_or_next|troop_slot_eq, ":leader_troop_id", slot_troop_occupation, slto_kingdom_hero),
                ##diplomacy end+
                (is_between, ":leader_troop_id", active_npcs_begin, active_npcs_end), #disable non-kingdom parties capturing enemy lords
                (party_add_prisoners, ":nonempty_winner_party", ":cur_troop_id", 1),
                (gt, reg0, 0),
                #(troop_set_slot, ":cur_troop_id", slot_troop_is_prisoner, 1),
                (troop_set_slot, ":cur_troop_id", slot_troop_prisoner_of_party, ":nonempty_winner_party"),
                (display_log_message, "str_hero_taken_prisoner"),
                
                (try_begin),
                  (call_script, "script_cf_prisoner_offered_parole", ":cur_troop_id"),
                  
                  (try_begin),
                    (eq, "$cheat_mode", 1),
                    (display_message, "@{!}DEBUG : Prisoner granted parole"),
                  (try_end),
                  
                  (call_script, "script_troop_change_relation_with_troop", ":leader_troop_id", ":cur_troop_id", 3),
                  (val_add, "$total_battle_enemy_changes", 3),
                (else_try),
                  (try_begin),
                    (eq, "$cheat_mode", 1),
                    (display_message, "@{!}DEBUG : Prisoner not offered parole"),
                  (try_end),
                  
                  (call_script, "script_troop_change_relation_with_troop", ":leader_troop_id", ":cur_troop_id", -5),
                  (val_add, "$total_battle_enemy_changes", -5),
                (try_end),
                
                (store_faction_of_party, ":capturer_faction", ":nonempty_winner_party"),
                (call_script, "script_update_troop_location_notes_prisoned", ":cur_troop_id", ":capturer_faction"),
              (else_try),
                (display_message,"@{s1} of the {s3} was defeated in battle but managed to escape."),
                                 ## CC
                                (try_begin),
                                  (is_between, ":cur_troop_id", bandit_heroes_begin, bandit_heroes_end),
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
                                    (party_template_slot_eq, ":pt_no", slot_party_template_hero_id, ":cur_troop_id"),
                                    (party_template_set_slot, ":pt_no", slot_party_template_has_hero, 0),
                                    (party_template_set_slot, ":pt_no", slot_party_template_hero_party_id, -1),
                                  (try_end),
                                (try_end),
                                ## CC
              (try_end),
              
              (try_begin),
                (store_troop_faction, ":cur_troop_faction", ":cur_troop_id"),
                (is_between, ":cur_troop_faction", kingdoms_begin, kingdoms_end),
                (faction_slot_eq, ":cur_troop_faction", slot_faction_marshall, ":cur_troop_id"),
                (is_between, ":cur_troop_faction", kingdoms_begin, kingdoms_end),
                (assign, "$marshall_defeated_in_battle", ":cur_troop_id"),
                #Marshall is defeated, refresh ai.
                (assign, "$g_recalculate_ais", 1),
              (try_end),
              
              ##diplomacy begin
              (try_begin),
                (call_script, "script_dplmc_is_affiliated_family_member", ":cur_troop_id"),
                 (eq, reg0, 1),
                ##diplomacy start+ skip relationship decay for defeat when the player himself is imprisoned or wounded
					 (eq, "$g_player_is_captive", 0),
                (neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 1),
                (neg|troop_is_wounded, "trp_player"),
                ##diplomacy end+
					 (assign, ":mitigating_factors", 0),
					 (try_begin),
					    #Being at war with the troop's faction is a mitigating factor, unless the player leads his faction.
						 (store_relation, reg0, "$players_kingdom", ":cur_troop_faction"),
						 (lt, reg0, 0),
						 (neq, "$players_kingdom", "fac_player_supporters_faction"),
						 (neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
						 (assign, ":mitigating_factors", 1),
					 (try_end),

                (try_for_range, ":family_member", lords_begin, kingdom_ladies_end),
					   ##diplomacy start+
						#The dead, exiled, and retired don't participate in this
						(neg|troop_slot_ge, ":family_member", slot_troop_occupation, slto_retirement),
						#Members of factions at war with the defeated affiliate's faction don't have
						#any relation loss either: it would be nonsensical for them to be willing to
						#battle him themselves, but become enraged at his defeat.
						(store_troop_faction, ":family_member_faction", ":family_member"),
						(store_relation, reg0, ":family_member_faction", ":cur_troop_faction"),
						(this_or_next|eq, ":family_member_faction", ":cur_troop_faction"),
							(ge, reg0, 0),
                  ##(call_script, "script_troop_get_family_relation_to_troop", ":family_member", "$g_player_affiliated_troop"),
                  (call_script, "script_dplmc_is_affiliated_family_member", ":family_member"),
                  (gt, reg0, 0),
						(assign, reg0, -2),
                        (try_begin),
                        	(eq, ":reduce_campaign_ai", 0),#hard: -1
                        	(assign, reg0, -1),
                        (else_try),
                        	(eq, ":reduce_campaign_ai", 1),#medium: -1 or 0
                        	(store_random_in_range, reg0, -1, 1),
                        (else_try),
                        	(eq, ":reduce_campaign_ai", 2),#easy: 0
                        	(assign, reg0, 0),
                        (try_end),
						(val_add, reg0, ":mitigating_factors"),
						(lt, reg0, 0),
                  (call_script, "script_change_player_relation_with_troop", ":family_member", reg0),
                  ##diplomacy end+
                (try_end),
              (try_end),
              ##diplomacy end
            (try_end),
            
            (try_begin),
              (ge, ":collective_casualties", 0),
              (party_get_num_prisoner_stacks, ":num_stacks", ":collective_casualties"),
            (else_try),
              (assign, ":num_stacks", 0),
            (try_end),
            (try_for_range, ":troop_iterator", 0, ":num_stacks"),
              (party_prisoner_stack_get_troop_id, ":cur_troop_id", ":collective_casualties", ":troop_iterator"),
              (troop_is_hero, ":cur_troop_id"),
              (call_script, "script_remove_troop_from_prison", ":cur_troop_id"),
              (store_troop_faction, ":cur_troop_faction", ":cur_troop_id"),
              (str_store_troop_name_link, s1, ":cur_troop_id"),
              (str_store_faction_name_link, s2, ":faction_receiving_prisoners"),
              (str_store_faction_name_link, s3, ":cur_troop_faction"),
              (display_log_message,"str_hero_freed"),
            (try_end),
            
            (try_begin),
              (ge, ":collective_casualties", 0),
              (party_clear, "p_temp_party"),
              (assign, "$g_move_heroes", 0), #heroes are already processed above. Skip them here.
              (call_script, "script_party_add_party_prisoners", "p_temp_party", ":collective_casualties"),
              (call_script, "script_party_prisoners_add_party_companions", "p_temp_party", ":collective_casualties"),
              (distribute_party_among_party_group, "p_temp_party", ":root_winner_party"),
              
              (call_script, "script_battle_political_consequences", ":root_defeated_party", ":root_winner_party"),
              
              (call_script, "script_clear_party_group", ":root_defeated_party"),
            (try_end),
            (assign, ":trigger_result", 1), #End battle!
            
            #Center captured
            (try_begin),
              (ge, ":collective_casualties", 0),
              (party_get_slot, ":cur_party_type", ":root_defeated_party", slot_party_type),
              (this_or_next|eq, ":cur_party_type", spt_town),
              (eq, ":cur_party_type", spt_castle),
              
              (assign, "$g_recalculate_ais", 1),
              
              (store_faction_of_party, ":winner_faction", ":root_winner_party"),
              (store_faction_of_party, ":defeated_faction", ":root_defeated_party"),
              
              (str_store_party_name, s1, ":root_defeated_party"),
              (str_store_faction_name, s2, ":winner_faction"),
              (str_store_faction_name, s3, ":defeated_faction"),
              (display_log_message, "str_center_captured"),
              
              (store_current_hours, ":hours"),
              (faction_set_slot, ":winner_faction", slot_faction_ai_last_decisive_event, ":hours"),
              
              (try_begin),
                (eq, "$g_encountered_party", ":root_defeated_party"),
                (call_script, "script_add_log_entry", logent_player_participated_in_siege, "trp_player",  "$g_encountered_party", 0, "$g_encountered_party_faction"),
              (try_end),
              
               (try_begin),
                 (party_get_num_companion_stacks, ":num_stacks", ":root_winner_party"),
                 (gt, ":num_stacks", 0),
                 (party_stack_get_troop_id, ":leader_troop_no", ":root_winner_party", 0),
		##diplomacy start+ support for promoted kingdom ladies
                 (is_between, ":leader_troop_no", heroes_begin, heroes_end),#<- dplmc+ added
                 (this_or_next|troop_slot_eq, ":leader_troop_no", slot_troop_occupation, slto_kingdom_hero),#<- dplmc+ addded
                     (is_between, ":leader_troop_no", active_npcs_begin, active_npcs_end),
		##diplomacy end+
                 (party_set_slot, ":root_defeated_party", slot_center_last_taken_by_troop, ":leader_troop_no"),
               (else_try),
                 (party_set_slot, ":root_defeated_party", slot_center_last_taken_by_troop, -1),
               (try_end),
              
              (call_script, "script_lift_siege", ":root_defeated_party", 0),
              (store_faction_of_party, ":fortress_faction", ":root_defeated_party"),
              (try_begin),
                (is_between, ":root_defeated_party", towns_begin, towns_end),
                (assign, ":damage", 40),
              (else_try),
                (assign, ":damage", 20),
              (try_end),
              (call_script, "script_faction_inflict_war_damage_on_faction", ":winner_faction", ":fortress_faction", ":damage"),
              
               (call_script, "script_give_center_to_faction", ":root_defeated_party", ":winner_faction"),
               (try_begin),
			     ##diplomacy start+ Handle player is co-ruler of faction
			     (assign, ":is_defeated_faction_coruler", 0),
				 (try_begin),
            		##zerilius changes begin
            		(eq, ":defeated_faction", "$players_kingdom"),
            		# (eq, ":is_defeated_faction_coruler", "$players_kingdom"),
            		##zerilius changes end
					(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
					(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
					(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
					(assign, ":is_defeated_faction_coruler", 1),
				 (try_end),
				 (this_or_next|eq, ":is_defeated_faction_coruler", 1),
	  		     ##diplomacy end+
                 (eq, ":defeated_faction", "fac_player_supporters_faction"),
                 (call_script, "script_add_notification_menu", "mnu_notification_center_lost", ":root_defeated_party", ":winner_faction"),
               (try_end),
              
              (party_get_num_attached_parties, ":num_attached_parties",  ":root_attacker_party"),
              (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
                (party_get_attached_party_with_rank, ":attached_party", ":root_attacker_party", ":attached_party_rank"),
                
                (party_get_num_companion_stacks, ":num_stacks", ":attached_party"),
                (assign, ":total_size", 0),
                (try_for_range, ":i_stack", 0, ":num_stacks"),
                  (party_stack_get_size, ":stack_size", ":attached_party", ":i_stack"),
                  (val_add, ":total_size", ":stack_size"),
                (try_end),
                
                (try_begin),
                  (ge, ":total_size", 10),
                  
                  (assign, ":stacks_added", 0),
                  (assign, ":last_random_stack", -1),
                  
                  (assign, ":end_condition", 10),
                  (try_for_range, ":unused", 0, ":end_condition"),
                    (store_random_in_range, ":random_stack", 1, ":num_stacks"),
                    (party_stack_get_troop_id, ":random_stack_troop", ":attached_party", ":random_stack"),
                    (party_stack_get_size, ":stack_size", ":attached_party", ":random_stack"),
                    (ge, ":stack_size", 4),
                    (neq, ":random_stack", ":last_random_stack"),
                    
                    (store_mul, ":total_size_mul_2", ":total_size", 2),
                    (assign, ":percentage", ":total_size_mul_2"),
                    (val_min, ":percentage", 100),
                    
                    (val_mul, ":stack_size", ":percentage"),
                    (val_div, ":stack_size", 100),
                    
                    (party_stack_get_troop_id, ":party_leader", ":attached_party", 0),
                    
                    (try_begin),
                       ##diplomacy start+ add lady personality
                       (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_conventional),
                       (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_otherworldly),
                       (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_adventurous),
                       ##diplomacy end+					
                      (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_goodnatured),
                      (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_upstanding),
                      (troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_martial),
                      (assign, reg2, 0),
                      (store_random_in_range, ":random_percentage", 40, 50), #average 45%
                    (else_try),
                       ##diplomacy start+ add lady personality
                       (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_ambitious),
                       ##diplmoacy end+					
                      (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_quarrelsome),
                      (troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_cunning),
                      (assign, reg2, 1),
                      (store_random_in_range, ":random_percentage", 30, 40), #average 35%
                    (else_try),
                      (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_selfrighteous),
                      (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_roguish),
                      (troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_debauched),
                      (assign, reg2, 2),
                      (store_random_in_range, ":random_percentage", 20, 30), #average 25%
                    (else_try),
                       ##diplomacy start+ add lady personality
                       (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_moralist),
                       ##diplomacy end+					
                      (this_or_next|troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_benefactor),
                      (troop_slot_eq, ":party_leader", slot_lord_reputation_type, lrep_custodian),
                      (assign, reg2, 3),
                      (store_random_in_range, ":random_percentage", 50, 60), #average 55%
                    (try_end),
                    
                    (val_min, ":random_percentage", 100),
                    (val_mul, ":stack_size", ":random_percentage"),
                    (val_div, ":stack_size", 100),
                    
                    (party_add_members, ":root_defender_party", ":random_stack_troop", ":stack_size"),
                    (party_remove_members, ":attached_party", ":random_stack_troop", ":stack_size"),
                    
                    (val_add, ":stacks_added", 1),
                    (assign, ":last_random_stack", ":random_stack"),
                    
                    (try_begin),
                      #if troops from three different stack is already added then break
                      (eq, ":stacks_added", 3),
                      (assign, ":end_condition", 0),
                    (try_end),
                  (try_end),
                (try_end),
              (try_end),
              
              #Reduce prosperity of the center by 5
              (try_begin),
                (neg|is_between, ":root_defeated_party", castles_begin, castles_end),
                (call_script, "script_change_center_prosperity", ":root_defeated_party", -5),
                (val_add, "$newglob_total_prosperity_from_townloot", -5),
              (try_end),
              (call_script, "script_order_best_besieger_party_to_guard_center", ":root_defeated_party", ":winner_faction"),
              (call_script, "script_move_prisoners_to_defeated_center", ":root_defeated_party", ":winner_faction"), ## CC
              (call_script, "script_cf_reinforce_party", ":root_defeated_party"),
              (call_script, "script_cf_reinforce_party", ":root_defeated_party"),
            (try_end),
          (try_end),
          
          #ADD XP
          (try_begin),
            (party_slot_eq, ":root_attacker_party", slot_party_type, spt_kingdom_hero_party),
            
            (assign, ":xp_gained_attacker", 200),
            (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
            (store_faction_of_party, ":root_attacker_party_faction", ":root_attacker_party"),
            (try_begin),
              (this_or_next|eq, ":root_attacker_party", "p_main_party"),
              (this_or_next|eq, ":root_attacker_party_faction", "fac_player_supporters_faction"),
              (eq, ":root_attacker_party_faction", "$players_kingdom"),
              #same
            (else_try),
              (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
              (val_mul, ":xp_gained_attacker", 3),
              (val_div, ":xp_gained_attacker", 2),
            (else_try),
              (eq, ":reduce_campaign_ai", 1), #moderate (1.0x)
              #same
            (else_try),
              (eq, ":reduce_campaign_ai", 2), #easy (0.5x)
              (val_div, ":xp_gained_attacker", 2),
            (try_end),
            
            (gt, ":new_attacker_strength", 0),
            (call_script, "script_upgrade_hero_party", ":root_attacker_party", ":xp_gained_attacker"),
          (try_end),
          (try_begin),
            (party_slot_eq, ":root_defender_party", slot_party_type, spt_kingdom_hero_party),
            
            (assign, ":xp_gained_defender", 200),
            (store_faction_of_party, ":root_defender_party_faction", ":root_defender_party"),
            (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
            (try_begin),
              (this_or_next|eq, ":root_defender_party", "p_main_party"),
              (this_or_next|eq, ":root_defender_party_faction", "fac_player_supporters_faction"),
              (eq, ":root_defender_party_faction", "$players_kingdom"),
              #same
            (else_try),
              (eq, ":reduce_campaign_ai", 0), #hard (1.5x)
              (val_mul, ":xp_gained_defender", 3),
              (val_div, ":xp_gained_defender", 2),
            (else_try),
              (eq, ":reduce_campaign_ai", 1), #moderate (1.0x)
              #same
            (else_try),
              (eq, ":reduce_campaign_ai", 2), #easy (0.5x)
              (val_div, ":xp_gained_defender", 2),
            (try_end),
            
            (gt, ":new_defender_strength", 0),
            (call_script, "script_upgrade_hero_party", ":root_defender_party", ":xp_gained_defender"),
          (try_end),
          
          (try_begin),
            #ozan - do not randomly end battles aganist towns or castles.
            (neg|party_slot_eq, ":root_defender_party", slot_party_type, spt_castle), #added by ozan
            (neg|party_slot_eq, ":root_defender_party", slot_party_type, spt_town),   #added by ozan
            #end ozan
            
            (party_get_slot, ":attacker_root_strength", ":root_attacker_party", slot_party_cached_strength),
            (party_get_slot, ":attacker_nearby_friend_strength", ":root_attacker_party", slot_party_nearby_friend_strength),
            (party_get_slot, ":strength_of_attacker_followers", ":root_attacker_party", slot_party_follower_strength),
            (store_add, ":total_attacker_strength", ":attacker_root_strength", ":attacker_nearby_friend_strength"),
            (val_add, ":total_attacker_strength", ":strength_of_attacker_followers"),
            
            (party_get_slot, ":defender_root_strength", ":root_defender_party", slot_party_cached_strength),
            (party_get_slot, ":defender_nearby_friend_strength", ":root_defender_party", slot_party_nearby_friend_strength),
            (party_get_slot, ":strength_of_defender_followers", ":root_defender_party", slot_party_follower_strength),
            (store_add, ":total_defender_strength", ":defender_root_strength", ":defender_nearby_friend_strength"),
            (val_add, ":total_attacker_strength", ":strength_of_defender_followers"),
            
            #Players can make save loads and change history because these random values are not determined from random_slots of troops
            (store_random_in_range, ":random_num", 0, 100),
            
            (try_begin),
              (lt, ":random_num", 10),
              (assign, ":trigger_result", 1), #End battle!
            (try_end),
          (else_try),
            (party_get_slot, ":attacker_root_strength", ":root_attacker_party", slot_party_cached_strength),
            (party_get_slot, ":attacker_nearby_friend_strength", ":root_attacker_party", slot_party_nearby_friend_strength),
            (party_get_slot, ":strength_of_followers", ":root_attacker_party", slot_party_follower_strength),
            (store_add, ":total_attacker_strength", ":attacker_root_strength", ":attacker_nearby_friend_strength"),
            (val_add, ":total_attacker_strength", ":strength_of_followers"),
            
            (party_get_slot, ":defender_root_strength", ":root_defender_party", slot_party_cached_strength),
            (party_get_slot, ":defender_nearby_friend_strength", ":root_defender_party", slot_party_nearby_friend_strength),
            (store_add, ":total_defender_strength", ":defender_root_strength", ":defender_nearby_friend_strength"),
            
            (val_mul, ":total_defender_strength", 13), #multiply defender strength with 1.3
            (val_div, ":total_defender_strength", 10),
            
            (gt, ":total_defender_strength", ":total_attacker_strength"),
            (gt, ":total_defender_strength", 3),
            
            #Players can make save loads and change history because these random values are not determined from random_slots of troops
            (store_random_in_range, ":random_num", 0, 100),
            
            (try_begin),
              (lt, ":random_num", 15), #15% is a bit higher than 10% (which is open area escape probability)
              (assign, ":trigger_result", 1), #End battle!
              
              (assign, "$g_recalculate_ais", 1), #added new
              
              (try_begin),
                (eq, "$cheat_mode", 1),
                (display_message, "@{!}DEBUG : Siege attackers are running away"),
              (try_end),
            (try_end),
          (try_end),
        (try_end),
      (try_end),
      (set_trigger_result, ":trigger_result"), ##1.134: This line was moved one line down
  ]),
  
  #script_game_event_battle_end:
  # This script is called whenever the game ends the battle between two parties on the map.
  # INPUT:
  # param1: Defender Party
  # param2: Attacker Party
  ("game_event_battle_end",
    [
      ##       (store_script_param_1, ":root_defender_party"),
      ##       (store_script_param_2, ":root_attacker_party"),
      
      #Fixing deleted heroes
      ##diplomacy start+ kingdom ladies may also potentially lead parties
      (try_for_range, ":cur_troop", heroes_begin, heroes_end),#<- achanged active_npcs to heroes
      #diplomacy end+
        (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
        (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
        (troop_get_slot, ":cur_prisoner_of_party", ":cur_troop", slot_troop_prisoner_of_party),
        (try_begin),
          (ge, ":cur_party", 0),
          (assign, ":continue", 0),
          (try_begin),
            (neg|party_is_active, ":cur_party"),
            (assign, ":continue", 1),
          (else_try),
            (party_count_companions_of_type, ":amount", ":cur_party", ":cur_troop"),
            (le, ":amount", 0),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_troop_name, s1, ":cur_troop"),
            (display_message, "@{!}DEBUG: {s1} no longer leads a party."),
          (try_end),
          
          (troop_set_slot, ":cur_troop", slot_troop_leaded_party, -1),
          #(str_store_troop_name, s5, ":cur_troop"),
          #(display_message, "@{!}DEBUG : {s5}'s troop_leaded_party set to -1"),
        (try_end),
        (try_begin),
          (ge, ":cur_prisoner_of_party", 0),
          (assign, ":continue", 0),
          (try_begin),
            (neg|party_is_active, ":cur_prisoner_of_party"),
            (assign, ":continue", 1),
          (else_try),
            (party_count_prisoners_of_type, ":amount", ":cur_prisoner_of_party", ":cur_troop"),
            (le, ":amount", 0),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_troop_name, s1, ":cur_troop"),
            (display_message, "@{!}DEBUG: {s1} is no longer a prisoner."),
          (try_end),
          (call_script, "script_remove_troop_from_prison", ":cur_troop"),
          #searching player
          (try_begin),
            (party_count_prisoners_of_type, ":amount", "p_main_party", ":cur_troop"),
            (gt, ":amount", 0),
            (troop_set_slot, ":cur_troop", slot_troop_prisoner_of_party, "p_main_party"),
            (assign, ":continue", 0),
            (try_begin),
              (eq, "$cheat_mode", 1),
              (str_store_troop_name, s1, ":cur_troop"),
              (display_message, "@{!}DEBUG: {s1} is now a prisoner of player."),
            (try_end),
          (try_end),
          (eq, ":continue", 1),
		  ##diplomacy start+
		  #Add increased information for affiliates.
		  (call_script, "script_dplmc_store_troop_is_eligible_for_affiliate_messages", ":cur_troop"),
		  (assign, ":is_affiliated", reg0),
		  ##diplomacy end+
          #searching kingdom heroes
	  ##diplomacy start+ support for promoted kingdom ladies
          (try_for_range, ":cur_troop_2", heroes_begin, heroes_end),#<-- changed active_npcs to heroes
          ##diplomacy end+
			(troop_slot_eq, ":cur_troop_2", slot_troop_occupation, slto_kingdom_hero),
			(eq, ":continue", 1),
            (troop_get_slot, ":cur_prisoner_of_party_2", ":cur_troop_2", slot_troop_leaded_party),
            (party_is_active, ":cur_prisoner_of_party_2"),
            (party_count_prisoners_of_type, ":amount", ":cur_prisoner_of_party_2", ":cur_troop"),
            (gt, ":amount", 0),
            (troop_set_slot, ":cur_troop", slot_troop_prisoner_of_party, ":cur_prisoner_of_party_2"),
            (assign, ":continue", 0),
            (try_begin),
			##diplomacy start+ Show for affiliates
			  (ge, ":is_affiliated", 1),
			  (str_store_troop_name, s1, ":cur_troop"),
			  (str_store_party_name, s2, ":cur_prisoner_of_party_2"),
			  (display_message, "@{s1} is now a prisoner of {s2}."),
			(else_try),
			##diplomacy end+
              (eq, "$cheat_mode", 1),
              (str_store_troop_name, s1, ":cur_troop"),
              (str_store_party_name, s2, ":cur_prisoner_of_party_2"),
              (display_message, "@{!}DEBUG: {s1} is now a prisoner of {s2}."),
            (try_end),
          (try_end),
          #searching walled centers
          (try_for_range, ":cur_prisoner_of_party_2", walled_centers_begin, walled_centers_end),
            (eq, ":continue", 1),
            (party_count_prisoners_of_type, ":amount", ":cur_prisoner_of_party_2", ":cur_troop"),
            (gt, ":amount", 0),
            (troop_set_slot, ":cur_troop", slot_troop_prisoner_of_party, ":cur_prisoner_of_party_2"),
            (assign, ":continue", 0),
            (try_begin),
			##diplomacy start+ Show for affiliates
			  (ge, ":is_affiliated", 1),
			  (str_store_troop_name, s1, ":cur_troop"),
			  (str_store_party_name, s2, ":cur_prisoner_of_party_2"),
			  (display_message, "@{s1} is now a prisoner of {s2}."),
			(else_try),
			##diplomacy end+
              (eq, "$cheat_mode", 1),
              (str_store_troop_name, s1, ":cur_troop"),
              (str_store_party_name, s2, ":cur_prisoner_of_party_2"),
              (display_message, "@{!}DEBUG: {s1} is now a prisoner of {s2}."),
            (try_end),
          (try_end),
        (try_end),
      (try_end),
  ]),
  
  #script_order_best_besieger_party_to_guard_center:
  # INPUT:
  # param1: defeated_center, param2: winner_faction
  # OUTPUT:
  # none
  ("order_best_besieger_party_to_guard_center",
	[
      (store_script_param, ":defeated_center", 1),
      (store_script_param, ":winner_faction", 2),
      (assign, ":best_party", -1),
      (assign, ":best_party_strength", 0),
      ##diplomacy start+ support for promoted kingdom ladies
      (try_for_range, ":kingdom_hero", heroes_begin, heroes_end),#<- changed to heroes
        (this_or_next|troop_slot_eq, ":kingdom_hero", slot_troop_occupation, slto_kingdom_hero),
           (is_between, ":kingdom_hero", active_npcs_begin, active_npcs_end),
      ##diplomacy end+
        (troop_get_slot, ":kingdom_hero_party", ":kingdom_hero", slot_troop_leaded_party),
        (gt, ":kingdom_hero_party", 0),
        (party_is_active, ":kingdom_hero_party"),
        (store_faction_of_party, ":kingdom_hero_party_faction", ":kingdom_hero_party"),
        (eq, ":winner_faction", ":kingdom_hero_party_faction"),
        (store_distance_to_party_from_party, ":dist", ":kingdom_hero_party", ":defeated_center"),
        (lt, ":dist", 5),
        #If marshall has captured the castle, then do not leave him behind.
        (neg|faction_slot_eq, ":winner_faction", slot_faction_marshall, ":kingdom_hero"),
        (assign, ":has_besiege_ai", 0),
        (try_begin),
          (party_slot_eq, ":kingdom_hero_party", slot_party_ai_state, spai_besieging_center),
          (party_slot_eq, ":kingdom_hero_party", slot_party_ai_object, ":defeated_center"),
          (assign, ":has_besiege_ai", 1),
        (else_try),
          (party_slot_eq, ":kingdom_hero_party", slot_party_ai_state, spai_accompanying_army),
          (party_get_slot, ":kingdom_hero_party_commander_party", ":kingdom_hero_party", slot_party_ai_object),
          (party_slot_eq, ":kingdom_hero_party_commander_party", slot_party_ai_state, spai_besieging_center),
          (party_slot_eq, ":kingdom_hero_party_commander_party", slot_party_ai_object, ":defeated_center"),
          (assign, ":has_besiege_ai", 1),
        (try_end),
        (eq, ":has_besiege_ai", 1),
        (party_get_slot, ":kingdom_hero_party_strength", ":kingdom_hero_party", slot_party_cached_strength),#recently calculated
        (gt, ":kingdom_hero_party_strength", ":best_party_strength"),
        (assign, ":best_party_strength", ":kingdom_hero_party_strength"),
        (assign, ":best_party", ":kingdom_hero_party"),
      (try_end),
      (try_begin),
        (gt, ":best_party", 0),
        (call_script, "script_party_set_ai_state", ":best_party", spai_holding_center, ":defeated_center"),
        #(party_set_slot, ":best_party", slot_party_commander_party, -1),
        (party_set_flags, ":best_party", pf_default_behavior, 1),
      (try_end),
  ]),
  
  #script_game_get_item_buy_price_factor:
  # This script is called from the game engine for calculating the buying price of any item.
  # INPUT:
  # param1: item_kind_id
  # OUTPUT:
  # trigger_result and reg0 = price_factor
  ("game_get_item_buy_price_factor",
    [
      (store_script_param_1, ":item_kind_id"),
      (assign, ":price_factor", 100),
      
      (call_script, "script_get_trade_penalty", ":item_kind_id"),
      (assign, ":trade_penalty", reg0),
      
      (try_begin),
        (is_between, "$g_encountered_party", centers_begin, centers_end),
        (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
        (store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
        (val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
        (party_get_slot, ":price_factor", "$g_encountered_party", ":item_slot_no"),
        
        #(try_begin),																					1.143 Port
        #  (is_between, "$g_encountered_party", villages_begin, villages_end),
        #  (party_get_slot, ":market_town", "$g_encountered_party", slot_village_market_town),
        #  (party_get_slot, ":price_in_market_town", ":market_town", ":item_slot_no"),
        #  (val_max, ":price_factor", ":price_in_market_town"),
        #(try_end),
        
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
  
  #script_game_get_item_sell_price_factor:
  # This script is called from the game engine for calculating the selling price of any item.
  # INPUT:
  # param1: item_kind_id
  # OUTPUT:
  # trigger_result and reg0 = price_factor
  ("game_get_item_sell_price_factor",
    [
      (store_script_param_1, ":item_kind_id"),
      (assign, ":price_factor", 100),
      
      (call_script, "script_get_trade_penalty", ":item_kind_id"),
      (assign, ":trade_penalty", reg0),
      
      (try_begin),
        (is_between, "$g_encountered_party", centers_begin, centers_end),
        (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
        (store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
        (val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
        (party_get_slot, ":price_factor", "$g_encountered_party", ":item_slot_no"),
        (val_mul, ":price_factor", 100),#normalize price factor to range 0..100
        (val_div, ":price_factor", average_price_factor),
      (else_try),
        #increase trade penalty while selling weapons, armor, and horses
        (val_mul, ":trade_penalty", 4),
      (try_end),
      
	  	  ##diplomacy start+
	  #If economic changes are enabled, use a lesser trade penalty when selling
 	  #to the correct merchant in town.
	  (try_begin),
		(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
		(is_between, "$g_encountered_party", towns_begin, towns_end),
		(gt, "$g_talk_troop", "trp_player"),
		(try_begin),
			#Selling weapons to the weaponsmith
			(party_slot_eq, "$g_encountered_party", slot_town_weaponsmith, "$g_talk_troop"),		
			(this_or_next|is_between, ":item_kind_id", weapons_begin, weapons_end),
			(this_or_next|is_between, ":item_kind_id", shields_begin, shields_end),
				(is_between, ":item_kind_id", weapons_ranged_begin, weapons_ranged_end),
			(val_mul, ":trade_penalty", 9),
			(val_div, ":trade_penalty", 10),
		(else_try),
			#Selling armor to the armorer
			(party_slot_eq, "$g_encountered_party", slot_town_armorer, "$g_talk_troop"),
			(is_between, ":item_kind_id", armors_begin, armors_end),	
			(val_mul, ":trade_penalty", 9),
			(val_div, ":trade_penalty", 10),
		(else_try),
			#Selling horses to the horse merchant
			(party_slot_eq, "$g_encountered_party", slot_town_horse_merchant, "$g_talk_troop"),
			(is_between, ":item_kind_id", horses_begin, horses_end),
			(val_mul, ":trade_penalty", 9),
			(val_div, ":trade_penalty", 10),
		(try_end),
	  (try_end),
		
	  #If economic changes are enabled, increase food prices in a town under siege.
	  (try_begin),
		(ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
		(is_between, "$g_encountered_party", centers_begin, centers_end),
		#Check selling food
		(is_between, ":item_kind_id", food_begin, food_end),
		#Check at a town or castle under siege for at least 48 hours
		(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
			(party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle), 
		(party_slot_eq, "$g_encountered_party", slot_village_state, svs_under_siege),
		
		(party_slot_ge, "$g_encountered_party", slot_center_is_besieged_by, 1),
		(party_get_slot, ":siege_start", "$g_encountered_party", slot_center_siege_begin_hours),
		(store_current_hours, ":cur_hours"),
		(store_sub, reg0, ":cur_hours", ":siege_start"),
		(ge, reg0, 48),
		#Check last caravan or village trading party arrival (default to eight weeks ago)
		(store_sub, ":last_arrival", ":cur_hours", 8 * 7 * 24),
		(val_min, ":last_arrival", ":siege_start"),
		(try_for_range, ":village_no", villages_begin, villages_end),
			(party_slot_eq, ":village_no", slot_village_market_town, "$g_encountered_party"),
			(party_get_slot, reg0, ":village_no", dplmc_slot_village_trade_last_arrived_to_market),
			(val_min, reg0, ":cur_hours"),
			(val_max, ":last_arrival", reg0),
		(try_end),
		(try_for_range, ":slot_no", dplmc_slot_town_trade_route_last_arrivals_begin, dplmc_slot_town_trade_route_last_arrivals_end),
			#Not all of these slots correspond to towns, but that doesn't
			#matter since their arrival times won't update after the start
			#of the game.
			(party_get_slot, reg0, "$g_encountered_party", ":slot_no"),
			(val_min, reg0, ":cur_hours"),
			(val_max, ":last_arrival", reg0),
		(try_end),
		##Increase food prices by 10% for every 3 days the siege has been going on,
		#or a minimum of 5%.
		#TODO: Make use of the last caravan arrival time.
		(store_sub, ":hours_since", ":cur_hours", ":siege_start"),
		(store_mul, ":siege_percent", ":hours_since", 10),
		(val_add, ":siege_percent", (3 * 24) // 2),
		(val_div, ":siege_percent", 3 * 24),
		(val_max, ":siege_percent", 5),
		(val_add, ":siege_percent", 100),
		(val_mul, ":price_factor", ":siege_percent"),
		(val_add, ":price_factor", 50),
		(val_div, ":price_factor", 100),
	  (try_end),
	  ##diplomacy end+
      
      (store_add, ":penalty_divisor", 100, ":trade_penalty"),
      
      (val_mul, ":price_factor", 100),
	  ##diplomacy start+
	  (try_begin),
		(gt, ":penalty_divisor", 0),
		(store_div, reg0, ":penalty_divisor", 2),
		(val_add, ":price_factor", reg0),#round correctly
	  (try_end),
	  ##diplomacy end+
      (val_div, ":price_factor", ":penalty_divisor"),
      
      (assign, reg0, ":price_factor"),
      (set_trigger_result, reg0),
  ]),
  
  # script_get_trade_penalty
  #
  # Input:
  # param1: troop_id,
  # Output: reg0
  
  ("get_trade_penalty",
    [
	##diplomacy start+
	##Changed to fall back to parameterized version
	##NEW:
      (store_script_param_1, ":item_kind_id"),
	  (call_script, "script_dplmc_get_trade_penalty", ":item_kind_id", "$g_encountered_party", "trp_player", "$g_talk_troop"),
	  
	##OLD:
#	  (store_script_param_1, ":item_kind_id"),
#	  
#      (assign, ":penalty",0),
#
#      (party_get_skill_level, ":trade_skill", "p_main_party", skl_trade),
#      (try_begin),
#        (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
#        (assign, ":penalty",15), #reduced slightly
#        (store_mul, ":skill_bonus", ":trade_skill", 1),
#        (val_sub, ":penalty", ":skill_bonus"),
#      (else_try),
#        (assign, ":penalty",100),
#        (store_mul, ":skill_bonus", ":trade_skill", 5),
#        (val_sub, ":penalty", ":skill_bonus"),
#      (try_end),
#
#	  ##diplomacy start+
#      (assign, ":penalty_multiplier", average_price_factor),#<-- replaced 1000 with average_price_factor
#	  ##diplomacy end+
###       # Apply penalty if player is hostile to merchants faction
###      (store_relation, ":merchants_reln", "fac_merchants", "fac_player_supporters_faction"),
###      (try_begin),
###        (lt, ":merchants_reln", 0),
###        (store_sub, ":merchants_reln_dif", 10, ":merchants_reln"),
###        (store_mul, ":merchants_relation_penalty", ":merchants_reln_dif", 20),
###        (val_add, ":penalty_multiplier", ":merchants_relation_penalty"),
###      (try_end),
#
#       # Apply penalty if player is on bad terms with the town
#      (try_begin),
#        (is_between, "$g_encountered_party", centers_begin, centers_end),
#        (party_get_slot, ":center_relation", "$g_encountered_party", slot_center_player_relation),
#        (store_mul, ":center_relation_penalty", ":center_relation", -3),
#        (val_add, ":penalty_multiplier", ":center_relation_penalty"),
#        (try_begin),
#          (lt, ":center_relation", 0),
#          (store_sub, ":center_penalty_multiplier", 100, ":center_relation"),
#          (val_mul, ":penalty_multiplier", ":center_penalty_multiplier"),
#          (val_div, ":penalty_multiplier", 100),
#        (try_end),
#      (try_end),
#
#       # Apply penalty if player is on bad terms with the merchant (not currently used)
#      (call_script, "script_troop_get_player_relation", "$g_talk_troop"),
#      (assign, ":troop_reln", reg0),
#      #(troop_get_slot, ":troop_reln", "$g_talk_troop", slot_troop_player_relation),
#      (try_begin),
#        (lt, ":troop_reln", 0),
#        (store_sub, ":troop_reln_dif", 0, ":troop_reln"),
#        (store_mul, ":troop_relation_penalty", ":troop_reln_dif", 20),
#        (val_add, ":penalty_multiplier", ":troop_relation_penalty"),
#      (try_end),
#
#
#	  (try_begin),
#		(is_between, "$g_encountered_party", villages_begin, villages_end),
#	    (val_mul, ":penalty", 2),
#	  (try_end),
#
#	  (try_begin),
#            (is_between, "$g_encountered_party", centers_begin, centers_end),
#	    #Double trade penalty if no local production or consumption
#	    (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
#		##diplomacy start+ 
#		#OPTIONAL CHANGE: Do not apply this to food
#       (this_or_next|lt, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
#		   (neg|is_between, ":item_kind_id", food_begin, food_end),
#		##diplomacy end+
#	    (call_script, "script_center_get_production", "$g_encountered_party", ":item_kind_id"),
#	    (eq, reg0, 0),
#	    (call_script, "script_center_get_consumption", "$g_encountered_party", ":item_kind_id"),
#	    (eq, reg0, 0),
#	    (val_mul, ":penalty", 2),
#	  (try_end),
#
#      (val_mul, ":penalty",  ":penalty_multiplier"),
#	  ##diplomacy start+ 
#	  (val_add, ":penalty", average_price_factor // 2),#round in the correct direction (we don't need to worry about penalty < 0)
#      (val_div, ":penalty", average_price_factor),#replace the hardcoded constant 1000 with average_price_factor
#	  ##diplomacy end+
#      (val_max, ":penalty", 1),
#      (assign, reg0, ":penalty"),
  ]),
  
  #script_game_event_buy_item:
  # This script is called from the game engine when player buys an item.
  # INPUT:
  # param1: item_kind_id
  ("game_event_buy_item",
    [
      (store_script_param_1, ":item_kind_id"),
      (store_script_param_2, ":reclaim_mode"),
      (try_begin),
        (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
        (store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
        (val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
        (party_get_slot, ":multiplier", "$g_encountered_party", ":item_slot_no"),
        (try_begin),
          (eq, ":reclaim_mode", 0),
          (val_add, ":multiplier", 10),		# 20	1.143 Port // increased from 10
        (else_try),
          (val_add, ":multiplier", 15),		# 30	1.143 Port // increased from 15
        (try_end),
 
		(store_item_value, ":item_value", ":item_kind_id"),		#	1.143 Port // newly added
		(try_begin),
		  (ge, ":item_value", 100),
		  (store_sub, ":item_value_sub_100", ":item_value", 100),
		  (store_div, ":item_value_sub_100_div_8", ":item_value_sub_100", 8),
		  (val_add, ":multiplier", ":item_value_sub_100_div_8"),
		(try_end),												#
		
       (val_min, ":multiplier", maximum_price_factor),
	   
        (party_set_slot, "$g_encountered_party", ":item_slot_no", ":multiplier"),
      (try_end),
  ]),
  
  #script_game_event_sell_item:
  # This script is called from the game engine when player sells an item.
  # INPUT:
  # param1: item_kind_id
  ("game_event_sell_item",
    [
      (store_script_param_1, ":item_kind_id"),
      (store_script_param_2, ":return_mode"),
      (try_begin),
        (is_between, ":item_kind_id", trade_goods_begin, trade_goods_end),
        (store_sub, ":item_slot_no", ":item_kind_id", trade_goods_begin),
        (val_add, ":item_slot_no", slot_town_trade_good_prices_begin),
        (party_get_slot, ":multiplier", "$g_encountered_party", ":item_slot_no"),
        (try_begin),
          (eq, ":return_mode", 0),
		  ## WINDYPLAINS+ ## - 2.55 - Prevent buy/sell price bumping glitch.
          (val_sub, ":multiplier", 10), # 30),		#	1.143 Port	//	changed from 15
        (else_try),
          (val_sub, ":multiplier", 15), # 20),		#	1.143 Port	//	changed from 10
		  ## WINDYPLAINS- ##
        (try_end),

		(store_item_value, ":item_value", ":item_kind_id"),			#	1.143 Port	//	Newly added
		(try_begin),
		  (ge, ":item_value", 100),
		  (store_sub, ":item_value_sub_100", ":item_value", 100),
		  (store_div, ":item_value_sub_100_div_8", ":item_value_sub_100", 8),
		  (val_sub, ":multiplier", ":item_value_sub_100_div_8"),
        (try_end),													#	End
        (val_max, ":multiplier", minimum_price_factor),

        (party_set_slot, "$g_encountered_party", ":item_slot_no", ":multiplier"),
      (try_end),
  ]),
  
  #script_start_wedding_cutscene
  # INPUT: arg1 = groom_troop, arg2 = bride_troop
  # OUTPUT: none
  ("start_wedding_cutscene",
    [
      (store_script_param, "$g_wedding_groom_troop", 1),
      (store_script_param, "$g_wedding_bride_troop", 2),
     ##diplomacy start+
	 (assign, ":save_reg0", reg0),
	 (assign, ":save_reg1", reg1),
	 
	 
     #To prevent a ridiculous cutscene, reverse genders if the bride is male.
	 (call_script, "script_dplmc_store_is_female_troop_1_troop_2", "$g_wedding_groom_troop", "$g_wedding_bride_troop"),
	 (assign, ":groom_is_woman", reg0),
	 (assign, ":bride_is_woman", reg1),
     
     (try_begin),
       (eq, ":bride_is_woman", 0),
       (neq, ":groom_is_woman", 0),#Don't bother reversing if both are male
       (assign, reg0, "$g_wedding_bride_troop"),
       (assign, "$g_wedding_bride_troop", "$g_wedding_groom_troop"),
       (assign, "$g_wedding_groom_troop", reg0),
	 (else_try),
	   #If it's a same-sex wedding, put the player in the role of the groom.
	   (eq, ":bride_is_woman", ":groom_is_woman"),
	   (eq, "$g_wedding_bride_troop", "trp_player"),
	   (assign, "$g_wedding_bride_troop", "$g_wedding_groom_troop"),
	   (assign, "$g_wedding_groom_troop", "trp_player"),
     (try_end),
     #diplomacy end+
     (assign, "$g_wedding_bishop_troop", "trp_temporary_minister"),
     (try_begin),
       (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
       (neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "$g_wedding_groom_troop"),
       (neg|faction_slot_eq, "$players_kingdom", slot_faction_leader, "$g_wedding_bride_troop"),
       (faction_get_slot, ":players_king", "$players_kingdom", slot_faction_leader),
	   ##diplomacy start+
	   (neq, ":players_king", "$g_wedding_bride_troop"),#necessary now that marrying monarchs can occur
	   (neq, ":players_king", "$g_wedding_groom_troop"),
	   #Changed the gender requirement (used to be required male)
       #(troop_get_type, ":troop_type", ":players_king"),       
       #(eq, ":troop_type", 0), #male
	   (call_script, "script_dplmc_store_troop_is_female", ":players_king"),
	   (this_or_next|eq, reg0, 0),
	   (this_or_next|eq, ":groom_is_woman", ":bride_is_woman"),
	      (ge, "$g_disable_condescending_comments", 2),
       (neq, ":players_king", "$g_wedding_bride_troop"),
       (neg|troop_slot_eq, "$g_wedding_bride_troop", slot_troop_father, ":players_king"),
	   (neg|troop_slot_eq, "$g_wedding_bride_troop", slot_troop_mother, ":players_king"),
       ##diplomacy end+
       (neq, ":players_king", "$g_wedding_groom_troop"),
       (assign, "$g_wedding_bishop_troop", ":players_king"),
     (else_try),
       (eq, "$players_kingdom", "fac_player_supporters_faction"),
       (faction_slot_eq, "$players_kingdom", slot_faction_leader, "trp_player"),
       (gt, "$g_player_minister", 0),
	   ##diplomacy start+ 
       #(troop_get_type, ":troop_type", "$g_player_minister"),
	   #(eq, ":troop_type", 0), #male
	   (call_script, "script_dplmc_store_troop_is_female", "$g_player_minister"),
	   (this_or_next|eq, reg0, 0),
	   (this_or_next|eq, ":groom_is_woman", ":bride_is_woman"),
	      (ge, "$g_disable_condescending_comments", 2),
	   ##diplomacy end+
       (neq, "$g_player_minister", "$g_wedding_groom_troop"),
       (assign, "$g_wedding_bishop_troop", "$g_player_minister"),
     (try_end),

     (assign, "$g_wedding_brides_dad_troop", "trp_temporary_minister"),
     (try_begin),
       (neq, "$g_wedding_bride_troop", "trp_player"),
       (try_begin),
         (troop_get_slot, ":father", "$g_wedding_bride_troop", slot_troop_father),
         (gt, ":father", 0),
         ##diplomacy start+
         (neg|troop_slot_ge, ":father", slot_troop_occupation, slto_retirement),
         #(troop_get_type, ":troop_type", ":father"), #just to make sure #<- dplmc+ replaced
		 (call_script, "script_dplmc_store_troop_is_female", ":father"),
		 (this_or_next|eq, ":bride_is_woman", 0),
			(eq, reg0, 0), #male
		 ##diplomacy end+
         (neq, ":father", "$g_wedding_groom_troop"), #this might be 0 due to an error
         (neq, ":father", "$g_wedding_bishop_troop"),
         (assign, "$g_wedding_brides_dad_troop", ":father"),
       (else_try),
         (troop_get_slot, ":guardian", "$g_wedding_bride_troop", slot_troop_guardian),
         (gt, ":guardian", 0),
         ##diplomacy start+
         (neg|troop_slot_ge, ":guardian", slot_troop_occupation, slto_retirement),
         #(troop_get_type, ":troop_type", ":guardian"), #just to make sure #<- dplmc+ replaced
		 (call_script, "script_dplmc_store_troop_is_female", ":guardian"),
		 (this_or_next|eq, ":bride_is_woman", 0),
			(eq, reg0, 0), #male
		 (call_script, "script_dplmc_store_troop_is_female", ":guardian"),
		 ##diplomacy end+
         (neq, ":guardian", "$g_wedding_groom_troop"), #this might be 0 due to an error
         (neq, ":guardian", "$g_wedding_bishop_troop"),
         (assign, "$g_wedding_brides_dad_troop", ":guardian"),
       ##diplomacy start+
	   #mother might be appropriate
	   (else_try),
		  (troop_get_slot, ":mother", "$g_wedding_bride_troop", slot_troop_mother),
	      (gt, ":mother", 0),
	      (neg|troop_slot_ge, ":mother", slot_troop_occupation, slto_retirement),
		  
		  (neq, ":mother", "$g_wedding_groom_troop"),
		  (neq, ":mother", "$g_wedding_bride_troop"),
		  (neq, ":mother", "$g_wedding_bishop_troop"),
			 
	      (assign, "$g_wedding_brides_dad_troop", ":mother"),
	   #we can get here, since male players can marry female lords
       (else_try),
          (is_between, "$g_wedding_bride_troop", companions_begin, companions_end),
          (troop_get_slot, ":cur_npc", "$g_wedding_bride_troop", slot_troop_personalitymatch_object),
          (ge, ":cur_npc", heroes_begin),
          (troop_slot_ge, ":cur_npc", slot_troop_met, 1),
		  (neg|troop_slot_ge, ":cur_npc", slot_troop_occupation, slto_retirement),
		  (this_or_next|troop_slot_eq, ":cur_npc", slot_troop_occupation, slto_kingdom_hero),
		  (this_or_next|troop_slot_eq, ":cur_npc", slot_troop_occupation, slto_player_companion),
		  (this_or_next|troop_slot_eq, ":cur_npc", slot_troop_occupation, slto_kingdom_seneschal),
		     (troop_slot_eq, ":cur_npc", slot_troop_occupation, slto_kingdom_lady),
		  
		  (neg|troop_slot_ge, ":cur_npc", slot_troop_occupation, slto_retirement),
		  (neq, ":cur_npc", "$g_wedding_groom_troop"),
	      (neq, ":cur_npc", "$g_wedding_bride_troop"),
	      (neq, ":cur_npc", "$g_wedding_bishop_troop"),
		  
		  (this_or_next|neg|troop_slot_ge, ":cur_npc", slot_lord_reputation_type, lrep_roguish),
		  (this_or_next|troop_slot_ge, ":cur_npc", slot_lord_reputation_type, lrep_conventional),
		  
          (assign, "$g_wedding_brides_dad_troop", ":cur_npc"),
	   (else_try),
	      #any other companion or lord that is favorable
		  (assign, ":best_score", 0),#must be at least positive
		  (try_for_range, ":cur_npc", heroes_begin, heroes_end),
			(neq, ":cur_npc", "$g_wedding_groom_troop"),
	        (neq, ":cur_npc", "$g_wedding_bride_troop"),
	        (neq, ":cur_npc", "$g_wedding_bishop_troop"),
			(neq, ":cur_npc", "trp_knight_1_1_wife"),
			(neq, ":cur_npc", "trp_kingdom_heroes_including_player_begin"),
			
			(neg|troop_slot_ge, ":cur_npc", slot_troop_occupation, slto_retirement),
				
			(call_script, "script_troop_get_relation_with_troop", ":cur_npc", "$g_wedding_bride_troop"),
			(assign, ":relation", reg0),
			#(call_script, "script_troop_get_family_relation_to_troop", ":cur_npc", "$g_wedding_bride_troop"),
			(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":cur_npc",  "$g_wedding_bride_troop"),
			(assign, ":family_relation", reg0),
			
			(store_add, ":score", ":relation", ":family_relation"),
			
			(gt, ":score", ":best_score"),#score better than current best
			(assign, ":best_score", ":score"),
			(assign, "$g_wedding_brides_dad_troop", ":cur_npc"),
		  (try_end),
       ##diplomacy end+
       (try_end),
     (else_try),
       (try_for_range, ":cur_companion", companions_begin, companions_end),
         (this_or_next|troop_slot_eq, ":cur_companion", slot_troop_occupation, slto_player_companion),
         (troop_slot_eq, ":cur_companion", slot_troop_occupation, slto_kingdom_hero),
		 ##diplomacy start+
         #(troop_get_type, ":troop_type", ":cur_companion"), #just to make sure
         #(eq, ":troop_type", 0), #male
		 (call_script, "script_dplmc_store_troop_is_female", ":cur_companion"),
		 (this_or_next|eq, reg0, 0),
			(eq, ":bride_is_woman", 0),
		 ##diplomacy end+
         (neq, ":cur_companion", "$g_wedding_groom_troop"),
         (neq, ":cur_companion", "$g_wedding_bishop_troop"),
         (assign, "$g_wedding_brides_dad_troop", ":cur_companion"),
       (try_end),
       ##diplomacy start+ try again with female companions if no male companions available
       (eq, "$g_wedding_brides_dad_troop", "trp_temporary_minister"),
       (try_for_range, ":cur_companion", companions_begin, companions_end),
         (this_or_next|troop_slot_eq, ":cur_companion", slot_troop_occupation, slto_player_companion),
			(troop_slot_eq, ":cur_companion", slot_troop_occupation, slto_kingdom_hero),
         (neq, ":cur_companion", "$g_wedding_groom_troop"),
         (neq, ":cur_companion", "$g_wedding_bishop_troop"),
         (assign, "$g_wedding_brides_dad_troop", ":cur_companion"),
       (try_end),
	   #try again with all lords if no female companions available
	   (eq, "$g_wedding_brides_dad_troop", "trp_temporary_minister"),
	   (assign, ":best_score", -100),#best score
       (try_for_range, ":cur_npc", heroes_begin, heroes_end),
	     (neg|troop_slot_eq, ":cur_npc", slot_troop_met, 0),
	   
 	     (this_or_next|troop_slot_eq, ":cur_npc", slot_troop_occupation, slto_kingdom_seneschal),
         (this_or_next|troop_slot_eq, ":cur_npc", slot_troop_occupation, slto_player_companion),
		 (this_or_next|troop_slot_eq, ":cur_npc", slot_troop_occupation, slto_kingdom_lady),
			(troop_slot_eq, ":cur_npc", slot_troop_occupation, slto_kingdom_hero),
		 
         (neq, ":cur_npc", "$g_wedding_groom_troop"),
         (neq, ":cur_npc", "$g_wedding_bishop_troop"),
		 (neq, ":cur_npc", "trp_knight_1_1_wife"),
	 	 (neq, ":cur_npc", "trp_kingdom_heroes_including_player_begin"),
		 
		 (call_script, "script_troop_get_player_relation", ":cur_npc"),
		 (assign, ":score", reg0),
		 (ge, ":score", 0),
		 (call_script, "script_dplmc_is_affiliated_family_member", ":cur_npc"),
		 (this_or_next|ge, ":score", 20),
			(ge, reg0, 1),
		 (gt, ":score", ":best_score"),
		 (assign, ":best_score", ":score"),
         (assign, "$g_wedding_brides_dad_troop", ":cur_npc"),
       (try_end),
       ##diplomacy end+
     (try_end),

     (modify_visitors_at_site,"scn_wedding"),
     (reset_visitors,0),
     (set_visitor, 0, "$g_wedding_groom_troop"),
     (set_visitor, 1, "$g_wedding_bride_troop"),
     (set_visitor, 2, "$g_wedding_brides_dad_troop"),
     (set_visitor, 3, "$g_wedding_bishop_troop"),
     (assign, ":num_visitors", 4),
     (assign, ":num_male_visitors", 0),
	 ##diplomacy start+
	 (store_troop_faction, ":groom_faction", "$g_wedding_groom_troop"),
	 (store_troop_faction, ":bride_faction", "$g_wedding_bride_troop"),
	 ##diplomacy end+
     (try_for_range, ":cur_npc", active_npcs_begin, kingdom_ladies_end),
       (lt, ":num_visitors", 32),
       (neq, ":cur_npc", "$g_wedding_groom_troop"),
       (neq, ":cur_npc", "$g_wedding_bride_troop"),
       (neq, ":cur_npc", "$g_wedding_brides_dad_troop"),
       (neq, ":cur_npc", "$g_wedding_bishop_troop"),
       (store_troop_faction, ":npc_faction", ":cur_npc"),
	   ##diplomacy start+
       #(is_between, ":npc_faction", kingdoms_begin, kingdoms_end),
       #(eq, ":npc_faction", "$players_kingdom"),
	   (this_or_next|eq, ":groom_faction", ":npc_faction"),
	      (eq, ":bride_faction", ":npc_faction"),
       ##diplomacy end+		  
       (this_or_next|troop_slot_eq, ":cur_npc", slot_troop_occupation, slto_player_companion),
       (this_or_next|troop_slot_eq, ":cur_npc", slot_troop_occupation, slto_kingdom_hero),
       (troop_slot_eq, ":cur_npc", slot_troop_occupation, slto_kingdom_lady),
	   ##diplomacy start+
       #(troop_get_type, ":troop_type", ":cur_npc"),
	   (call_script, "script_dplmc_store_troop_is_female", ":cur_npc"),
	   (assign, ":troop_type", reg0),
	   ##diplomacy end+
       (assign, ":continue_adding", 1),
       (try_begin),
         (eq, ":troop_type", 0),
         (assign, ":continue_adding", 0),
         (lt, ":num_male_visitors", 16), #limit number of male visitors
         (assign, ":continue_adding", 1),
         (val_add, ":num_male_visitors", 1),
       (try_end),
       (eq, ":continue_adding", 1),
       (set_visitor, ":num_visitors", ":cur_npc"),
       (val_add, ":num_visitors", 1),
     (try_end),
	 ##diplomacy start+
	 (assign, reg0, ":save_reg0"),
	 (assign, reg1, ":save_reg1"),
	 ##diplomacy end+
     (set_jump_mission,"mt_wedding"),
     (jump_to_scene,"scn_wedding"),
     (change_screen_mission),
    ]),
  
  
  # script_game_get_troop_wage
  # This script is called from the game engine for calculating troop wages.
  # Input:
  # param1: troop_id, param2: party-id
  # Output: reg0: weekly wage
  
  ("game_get_troop_wage",
    [
      (store_script_param_1, ":troop_id"),
      (store_script_param_2, ":unused"), #party id
      
      (assign,":wage", 0),
      (try_begin),
        (this_or_next|eq, ":troop_id", "trp_player"),
        (eq, ":troop_id", "trp_kidnapped_girl"),
      (else_try),
        (is_between, ":troop_id", pretenders_begin, pretenders_end),
      ##diplomacy start+
      (else_try),
      #Temporarily joined lords and ladies don't require wages.
        (is_between, ":troop_id", heroes_begin, heroes_end),
        (this_or_next|troop_slot_eq, ":troop_id", slot_troop_playerparty_history,dplmc_pp_history_lord_rejoined),      
        (this_or_next|troop_slot_eq, ":troop_id", slot_troop_occupation, slto_kingdom_hero),
           (troop_slot_eq, ":troop_id",slot_troop_occupation, slto_kingdom_lady),
      ##diplomacy end+
      (else_try),
        (store_character_level, ":troop_level", ":troop_id"),
        (assign, ":wage", ":troop_level"),
        (val_add, ":wage", 3),
        (val_mul, ":wage", ":wage"),
        (val_div, ":wage", 25),
      (try_end),
      
      (try_begin), #mounted troops cost 65% more than the normal cost
        (neg|is_between, ":troop_id", companions_begin, companions_end), ##1.132, new line
        (troop_is_mounted, ":troop_id"),
        (val_mul, ":wage", 5),
        (val_div, ":wage", 3),
      (try_end),
      
      (try_begin), #mercenaries cost %50 more than the normal cost
        (is_between, ":troop_id", mercenary_troops_begin, mercenary_troops_end),
        (val_mul, ":wage", 3),
        (val_div, ":wage", 2),
      (try_end),
      
      (try_begin),
        (is_between, ":troop_id", companions_begin, companions_end),
        (val_mul, ":wage", 2),
      (try_end),
      
      (store_skill_level, ":leadership_level", "skl_leadership", "trp_player"),
      (store_mul, ":leadership_bonus", 5, ":leadership_level"),
      (store_sub, ":leadership_factor", 100, ":leadership_bonus"),
      (val_mul, ":wage", ":leadership_factor"),  #wage = wage * (100 - 5*leadership)/100
      (val_div, ":wage", 100),
      
      (try_begin),
        (neq, ":troop_id", "trp_player"),
        (neq, ":troop_id", "trp_kidnapped_girl"),
        (neg|is_between, ":troop_id", pretenders_begin, pretenders_end),
		  ##diplomacy start+ For temporarily rejoined lords, and temporarily joined ladies
        (neg|troop_slot_eq, ":troop_id", slot_troop_playerparty_history,dplmc_pp_history_lord_rejoined),      
        (neg|troop_slot_eq, ":troop_id", slot_troop_occupation, slto_kingdom_hero),
        (neg|is_between, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
		  ##diplomacy end+
        (val_max, ":wage", 1),
      (try_end),
      
      (assign, reg0, ":wage"),
      (set_trigger_result, reg0),
  ]),
  
  # script_game_get_total_wage
  # This script is called from the game engine for calculating total wage of the player party which is shown at the party window.
  # Input: none
  # Output: reg0: weekly wage
  
  ("game_get_total_wage",
    [
      (assign, ":total_wage", 0),
      (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
      (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
        (party_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),
        (call_script, "script_game_get_troop_wage", ":stack_troop", 0),
        (val_mul, reg0, ":stack_size"),
        (val_add, ":total_wage", reg0),
      (try_end),
	  ##diplomacy start+
	  #If the player leads a kingdom, take into account centralization.
	  (faction_get_slot, ":centralization", "$players_kingdom", dplmc_slot_faction_centralization),
	  (try_begin),
		  (neq, ":centralization", 0),

		  (assign, reg0, 0),
	     (try_begin),
		     (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
		     (faction_get_slot, ":faction_leader", "$players_kingdom", slot_faction_leader),
		     (ge, ":faction_leader", 0),
		     (this_or_next|eq, ":faction_leader", "trp_player"),
		     (this_or_next|troop_slot_eq, ":faction_leader", slot_troop_spouse, "trp_player"),
              (troop_slot_eq, "trp_player", slot_troop_spouse, reg0),
           (assign, reg0, 1),
        (try_end),

		  (this_or_next|eq, reg0, 1),
		     (eq, "$players_kingdom", "fac_player_supporters_faction"),
		  (faction_slot_eq, "$players_kingdom", slot_faction_state, sfs_active),

		  #Apply centralization, but limit it for nascent kingdoms
        (val_clamp, ":centralization", -3, 4),
	     (faction_get_slot, ":policy_limit", "$players_kingdom", slot_faction_num_towns),
	     (faction_get_slot, reg0, "$players_kingdom", slot_faction_num_castles),
	     (val_add, ":policy_limit", reg0),

	     (val_max, ":policy_limit", 0),
	     (val_min, ":centralization", ":policy_limit"),
	     (val_mul, ":policy_limit", -1),
	     (val_max, ":centralization", ":policy_limit"),

		  #Now reg0 is going to be the result again
		  (store_mul, reg0, ":centralization", -5),
		  (val_add, reg0, 100),
		  (val_mul, reg0, ":total_wage"),
		  (val_add, reg0, 50),#rounding
		  (val_div, reg0, 100),
	  (try_end),
    ##diplomacy end+
      (assign, reg0, ":total_wage"),
      (set_trigger_result, reg0),
  ]),
  
  # script_game_get_join_cost
  # This script is called from the game engine for calculating troop join cost.
  # Input:
  # param1: troop_id,
  # Output: reg0: weekly wage
  
  ("game_get_join_cost",
    [
      (store_script_param_1, ":troop_id"),
      
      (assign,":join_cost", 0),
      (try_begin),
        (troop_is_hero, ":troop_id"),
      (else_try),
        (store_character_level, ":troop_level", ":troop_id"),
        (assign, ":join_cost", ":troop_level"),
        (val_add, ":join_cost", 5),
        (val_mul, ":join_cost", ":join_cost"),
        (val_add, ":join_cost", 40),
        (val_div, ":join_cost", 5),
        (try_begin), #mounted troops cost %100 more than the normal cost
          (troop_is_mounted, ":troop_id"),
          (val_mul, ":join_cost", 2),
        (try_end),
      (try_end),
      (assign, reg0, ":join_cost"),
      (set_trigger_result, reg0),
  ]),
  
  # script_game_get_upgrade_xp
  # This script is called from game engine for calculating needed troop upgrade exp
  # Input:
  # param1: troop_id,
  # Output: reg0 = needed exp for upgrade
  ("game_get_upgrade_xp",
    [
      (store_script_param_1, ":troop_id"),
      
      ##Floris: Updated from CC 1.321
      (assign, ":needed_upgrade_xp", 0),
      #formula : int needed_upgrade_xp = 2 * (30 + 0.006f * level_boundaries[troops[troop_id].level * 1.5); # CC
      (store_character_level, ":troop_level", ":troop_id"),
      ## CC
      (store_mul, ":needed_upgrade_xp", ":troop_level", 3),
      (val_div, ":needed_upgrade_xp", 2),
      ## CC
      (get_level_boundary, reg0, ":needed_upgrade_xp"),
      (val_mul, reg0, 6),
      (val_div, reg0, 1000),
      (val_add, reg0, 30),
      
      (try_begin),
        (ge, ":troop_id", bandits_begin),
        (lt, ":troop_id", bandits_end),
        (val_mul, reg0, 2),
      (try_end),
      
      (set_trigger_result, reg0),
  ]),
  ##
  
  # script_game_get_upgrade_cost
  # This script is called from game engine for calculating needed troop upgrade exp
  # Input:
  # param1: troop_id,
  # Output: reg0 = needed cost for upgrade
  ("game_get_upgrade_cost",
    [
      (store_script_param_1, ":troop_id"),
      
      (store_character_level, ":troop_level", ":troop_id"),
      #(try_begin),
      #(is_between, ":troop_level", 0, 6),
      #(assign, reg0, 10),
      #(else_try),
      #(is_between, ":troop_level", 6, 11),
      #(assign, reg0, 20),
      #(else_try),
      #(is_between, ":troop_level", 11, 16),
      #(assign, reg0, 40),
      #(else_try),
      #(is_between, ":troop_level", 16, 21),
      #(assign, reg0, 80),
      #(else_try),
      #(is_between, ":troop_level", 21, 26),
      #(assign, reg0, 120),
      #(else_try),
      #(is_between, ":troop_level", 26, 31),
      #(assign, reg0, 160),
      #(else_try),
      #(assign, reg0, 200),
      #(try_end),
      
      ## CC
      (assign, ":cost", ":troop_level"),
      (val_add, ":cost", 3),
      (val_mul, ":cost", ":cost"),
      (val_div, ":cost", 5),
      (try_begin), #mounted troops cost 50% more than the normal cost
        (this_or_next|troop_is_guarantee_horse, ":troop_id"),
        (is_between, ":troop_id", customizable_troops_begin, customizable_troops_end), #custom troops cost 50% more than the normal cost
        (val_mul, ":cost", 3),
        (val_div, ":cost", 2),
      (try_end),
      (assign, reg0, ":cost"),
      ## CC
      (set_trigger_result, reg0),
  ]),
  
  # script_game_get_prisoner_price
  # This script is called from the game engine for calculating prisoner price
  # Input:
  # param1: troop_id,
  # Output: reg0
  ("game_get_prisoner_price",
    [
      (store_script_param_1, ":troop_id"),
      
      (try_begin),
        (is_between, "$g_talk_troop", ransom_brokers_begin, ransom_brokers_end),
        (store_character_level, ":troop_level", ":troop_id"),
        (assign, ":ransom_amount", ":troop_level"),
        (val_add, ":ransom_amount", 10),
        (val_mul, ":ransom_amount", ":ransom_amount"),
        (val_div, ":ransom_amount", 6),
      (else_try),
        (assign, ":ransom_amount", 50),
      (try_end),
      (assign, reg0, ":ransom_amount"),
      (set_trigger_result, reg0),
  ]),
  
  
  # script_game_check_prisoner_can_be_sold
  # This script is called from the game engine for checking if a given troop can be sold.
  # Input:
  # param1: troop_id,
  # Output: reg0: 1= can be sold; 0= cannot be sold.
  
  ("game_check_prisoner_can_be_sold",
    [
      (store_script_param_1, ":troop_id"),
      (assign, reg0, 0),
      (try_begin),
        (neg|troop_is_hero, ":troop_id"),
        (assign, reg0, 1),
      (try_end),
      (set_trigger_result, reg0),
  ]),
  
  # script_game_get_morale_of_troops_from_faction
  # This script is called from the game engine
  # Input:
  # param1: faction_no,
  # Output: reg0: extra morale x 100
  
  ("game_get_morale_of_troops_from_faction",
    [
      (store_script_param_1, ":troop_no"),

      (store_troop_faction, ":faction_no", ":troop_no"),

      (try_begin),
        (ge, ":faction_no", npc_kingdoms_begin),
        (lt, ":faction_no", npc_kingdoms_end),

        (faction_get_slot, reg0, ":faction_no",  slot_faction_morale_of_player_troops),

        #(assign, reg1, ":faction_no"),
        #(assign, reg2, ":troop_no"),
        #(assign, reg3, reg0),
        #(display_message, "@extra morale for troop {reg2} of faction {reg1} is {reg3}"),
      (else_try),
        (assign, reg0, 0),
      (try_end),
      ##diplomacy start+
      #If there is no current morale penalty, then there will be a minor morale bonus
		#if the player has his own faction and his culture matches the source kingdom.
		(try_begin),
		   (eq, reg0, 0),
			(is_between,"$g_player_culture", npc_kingdoms_begin, npc_kingdoms_end),
			(eq, "$g_player_culture", ":faction_no"),
			#xxx TODO: pick a number less arbitrarily
			(assign, reg0, 100),
		(try_end),
      ##diplomacy end+
      (val_div, reg0, 100),

      (party_get_morale, reg1, "p_main_party"),

      (val_add, reg0, reg1),

      (set_trigger_result, reg0),
  ]),

  ## WINDYPLAINS+ ## - Replaced script_game_event_detect_party with Silverstag's for better forced pausing.
  # #script_game_event_detect_party:
  # # This script is called from the game engine when player party inspects another party.
  # # INPUT:
  # # param1: Party-id
  # ("game_event_detect_party",
    # [
        # (store_script_param_1, ":party_id"),
        # (try_begin),
          # (party_slot_eq, ":party_id", slot_party_type, spt_kingdom_hero_party),
		  # #Floris - pause on detection
		  # (try_begin),
		    # (eq, "$g_ft_force_pause", 1),
			# (key_is_down, key_space),
			# (this_or_next|key_is_down, key_left_control),
			# (key_is_down, key_right_control),
			# (store_faction_of_party, ":faction", ":party_id"),
			# (store_relation, reg0, "fac_player_supporters_faction", ":faction"),
			# (lt, reg0, 0),
			# (dialog_box, "@Enemies on the horizon!", "@Warning!"),
			# #(rest_for_hours_interactive), #pause/stop movement
		  # (try_end),
		  # #Floris - end
          # (party_stack_get_troop_id, ":leader", ":party_id", 0),
          # ##diplomacy start+ support for promoted kingdom ladies
          # (is_between, ":leader", heroes_begin, heroes_end),
          # (this_or_next|troop_slot_eq, ":leader", slot_troop_occupation, slto_kingdom_hero),
          # ##diplomacy end+
          # (is_between, ":leader", active_npcs_begin, active_npcs_end),
          # (call_script, "script_update_troop_location_notes", ":leader", 0),
        # (else_try),
          # (is_between, ":party_id", walled_centers_begin, walled_centers_end),
          # (party_get_num_attached_parties, ":num_attached_parties",  ":party_id"),
          # (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
            # (party_get_attached_party_with_rank, ":attached_party", ":party_id", ":attached_party_rank"),
            # (party_stack_get_troop_id, ":leader", ":attached_party", 0),
			# ##diplomacy start+ support for promoted kingdom ladies
			# (is_between, ":leader", heroes_begin, heroes_end),
			# (this_or_next|troop_slot_eq, ":leader", slot_troop_occupation, slto_kingdom_hero),
			# ##diplomacy end+
            # (is_between, ":leader", active_npcs_begin, active_npcs_end),
            # (call_script, "script_update_troop_location_notes", ":leader", 0),
          # (try_end),
		# #Floris - pause on detection
		# (else_try),
		  # (eq, "$g_ft_force_pause", 1),
		  # (key_is_down, key_space),
		  # (this_or_next|key_is_down, key_left_control),
		  # (key_is_down, key_right_control),
		  # (gt, ":party_id", "p_spawn_points_end"), #other spawned party (merchant, bandit, etc)
		  # (party_is_active, ":party_id"),
		  # (store_faction_of_party, ":faction", ":party_id"),
		  # (store_relation, reg0, "fac_player_supporters_faction", ":faction"),
		  # (lt, reg0, 0),
		  # (dialog_box, "@Enemies on the horizon!", "@Warning!"),
		  # #(rest_for_hours_interactive), #pause/stop movement
		# #Floris - end
        # (try_end),
  # ]),
  
  #script_game_event_detect_party:
  # This script is called from the game engine when player party inspects another party.
  # INPUT:
  # param1: Party-id
  ("game_event_detect_party",
    [
        (store_script_param_1, ":party_id"),

        (try_begin),
          (party_slot_eq, ":party_id", slot_party_type, spt_kingdom_hero_party),
		  ## WINDYPLAINS+ ## - Fast travel pause.  Initial code by Caba'drin with (level 2) revision by Windyplains.
		  (try_begin),
		    (ge, "$g_ft_force_pause", 1),
			(key_is_down, key_space),
			(this_or_next|key_is_down, key_left_control),
			(key_is_down, key_right_control),
			(store_faction_of_party, ":faction_no", ":party_id"),
			(store_relation, reg0, "fac_player_supporters_faction", ":faction_no"),
			(lt, reg0, 0),
			## WINDYPLAINS+ ## - Revision to make this less sensitive towards enemies who pose no threat.
			(party_stack_get_troop_id, ":troop_no", ":party_id", 0),
			(str_store_troop_name, s22, ":troop_no"),
			(str_store_faction_name, s23, ":faction_no"),
			(str_store_string, s21, "@An force under the banner of {s22} from the {s23} has been spotted."),
			(dialog_box, "@{s21}", "@Scout Report!"),
			## WINDYPLAINS- ##
		  (try_end),
		  ## WINDYPLAINS- ##
          (party_stack_get_troop_id, ":leader", ":party_id", 0),
          ##diplomacy start+ support for promoted kingdom ladies
		  (is_between, ":leader", heroes_begin, heroes_end),
		  (this_or_next|troop_slot_eq, ":leader", slot_troop_occupation, slto_kingdom_hero),
		  ##diplomacy end+
          (is_between, ":leader", active_npcs_begin, active_npcs_end),
          (call_script, "script_update_troop_location_notes", ":leader", 0),
        (else_try),
          (is_between, ":party_id", walled_centers_begin, walled_centers_end),
          (party_get_num_attached_parties, ":num_attached_parties",  ":party_id"),
          (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
            (party_get_attached_party_with_rank, ":attached_party", ":party_id", ":attached_party_rank"),
            (party_stack_get_troop_id, ":leader", ":attached_party", 0),
			##diplomacy start+ support for promoted kingdom ladies
			(is_between, ":leader", heroes_begin, heroes_end),
			(this_or_next|troop_slot_eq, ":leader", slot_troop_occupation, slto_kingdom_hero),
			##diplomacy end+
            (is_between, ":leader", active_npcs_begin, active_npcs_end),
            (call_script, "script_update_troop_location_notes", ":leader", 0),
          (try_end),
		## WINDYPLAINS+ ## - Fast travel pause.  Stop the player party if a quest party is nearby.
        (else_try),
			(ge, "$g_ft_force_pause", 1),
			(key_is_down, key_space),
			(this_or_next|key_is_down, key_left_control),
			(key_is_down, key_right_control),
			(gt, ":party_id", "p_spawn_points_end"), #other spawned party (merchant, bandit, etc)
			(party_is_active, ":party_id"),
			(this_or_next|neg|party_slot_eq, ":party_id", slot_party_type, spt_kingdom_caravan), # These are never hostile so ignore them.
			(check_quest_active, "qst_cause_provocation"),
			(assign, ":block", 1),
			(try_begin),
				### QUEST - TROUBLESOME BANDITS ###
				(check_quest_active, "qst_troublesome_bandits"),
				(quest_slot_eq, "qst_troublesome_bandits", slot_quest_target_party, ":party_id"),
				(quest_get_slot, ":center_no", "qst_troublesome_bandits", slot_quest_giver_center),
				(str_store_party_name, s22, ":center_no"),
				(str_store_string, s21, "@A warband matching the description the guildmaster back in {s22} gave us was spotted nearby."),
				(assign, ":block", 0),
			(else_try),
				### QUEST - DESTROY THE LAIR ###
				(check_quest_active, "qst_destroy_bandit_lair"),
				(quest_slot_eq, "qst_destroy_bandit_lair", slot_quest_target_party, ":party_id"),
				(quest_get_slot, ":troop_no", "qst_destroy_bandit_lair", slot_quest_giver_troop),
				(str_store_troop_name, s22, ":troop_no"),
				(str_store_string, s21, "@There are signs that the bandit lair {s22} asked us to hunt down is nearby."),
				(assign, ":block", 0),
			(else_try),
				### QUEST - CAUSE PROVOCATION ###
				(check_quest_active, "qst_cause_provocation"),
				(store_faction_of_party, ":faction_no", ":party_id"),
				(quest_slot_eq, "qst_cause_provocation", slot_quest_target_faction, ":faction_no"),
				(party_slot_eq, ":party_id", slot_party_type, spt_kingdom_caravan),
				(quest_get_slot, ":troop_no", "qst_cause_provocation", slot_quest_giver_troop),
				(str_store_troop_name, s22, ":troop_no"),
				(str_store_faction_name, s23, ":faction_no"),
				(str_store_string, s21, "@Scouts report that a caravan from the {s23} is nearby and would make just the kind of target {s22} wanted us to find."),
				(assign, ":block", 0),
			(try_end),
			(eq, ":block", 0),
			(dialog_box, "@{s21}", "@Scout Report!"),
		## WINDYPLAINS- ##
		## WINDYPLAINS+ ## - Fast travel pause.  Initial code by Caba'drin with (level 2) revision by Windyplains.
        (else_try),
			(ge, "$g_ft_force_pause", 1),
			(key_is_down, key_space),
			(this_or_next|key_is_down, key_left_control),
			(key_is_down, key_right_control),
			(gt, ":party_id", "p_spawn_points_end"), #other spawned party (merchant, bandit, etc)
			(party_is_active, ":party_id"),
			(neg|party_slot_eq, ":party_id", slot_party_type, spt_kingdom_caravan), # These are never hostile so ignore them.
			(store_faction_of_party, ":faction_no", ":party_id"),
			(store_relation, reg0, "fac_player_supporters_faction", ":faction_no"),
			(lt, reg0, 0),
			(try_begin),
				(ge, "$g_ft_force_pause", 2),
				(assign, ":block", 0),
				(try_begin),
					# They're hostile AND are larger than we are. (to catch serious bandit threats)
					(party_get_num_companions, ":enemy_size", ":party_id"),
					(party_get_num_companions, ":player_size", "p_main_party"),
					# Toss a buffer in by removing 20% of the player party size as a bandit group with 1 less person will definitely attack.
					(store_mul, ":buffer", ":player_size", 20),
					(val_div, ":buffer", 100),
					(val_sub, ":player_size", ":buffer"),
					(lt, ":player_size", ":enemy_size"),
					(str_store_string, s21, "@A potentially hostile force comparable to our own has been spotted in the distance."),
				(else_try),
					# They're hostile AND mean us harm.
					(get_party_ai_behavior, ":behavior", ":party_id"),
					(get_party_ai_object, ":focus", ":party_id"),
					(eq, ":behavior", ai_bhvr_attack_party),
					(eq, ":focus", "p_main_party"),
					(str_store_string, s21, "@An enemy party has been spotted by your scouts moving to intercept you."),
				(else_try),
					(assign, ":block", 1),
				(try_end),
				(eq, ":block", 0),
				(dialog_box, "@{s21}", "@Scout Report!"),
			(else_try),
				(eq, "$g_ft_force_pause", 1),
				(dialog_box, "@Enemies on the horizon!", "@Warning!"),
			(try_end),
		## WINDYPLAINS- ##
		(try_end),
  ]),
  ## WINDYPLAINS- ##
  
  #script_game_event_undetect_party:
  # This script is called from the game engine when player party inspects another party.
  # INPUT:
  # param1: Party-id
  ("game_event_undetect_party",
    [
        (store_script_param_1, ":party_id"),
        (try_begin),
          (party_slot_eq, ":party_id", slot_party_type, spt_kingdom_hero_party),
          (party_stack_get_troop_id, ":leader", ":party_id", 0),
          ##diplomacy start+ support for promoted kingdom ladies
          (is_between, ":leader", heroes_begin, heroes_end),
          (this_or_next|troop_slot_eq, ":leader", slot_troop_occupation, slto_kingdom_hero),
          ##diplomacy end+
          (is_between, ":leader", active_npcs_begin, active_npcs_end),
          (call_script, "script_update_troop_location_notes", ":leader", 0),
        (try_end),
  ]),
  
  #script_game_get_statistics_line:
  # This script is called from the game engine when statistics page is opened.
  # INPUT:
  # param1: line_no
  ("game_get_statistics_line",
    [
      (store_script_param_1, ":line_no"),
      (try_begin),
        (eq, ":line_no", 0),
        (get_player_agent_kill_count, reg1),
        (str_store_string, s1, "str_number_of_troops_killed_reg1"),
        (set_result_string, s1),
      (else_try),
        (eq, ":line_no", 1),
        (get_player_agent_kill_count, reg1, 1),
        (str_store_string, s1, "str_number_of_troops_wounded_reg1"),
        (set_result_string, s1),
      (else_try),
        (eq, ":line_no", 2),
        (get_player_agent_own_troop_kill_count, reg1),
        (str_store_string, s1, "str_number_of_own_troops_killed_reg1"),
        (set_result_string, s1),
      (else_try),
        (eq, ":line_no", 3),
        (get_player_agent_own_troop_kill_count, reg1, 1),
        (str_store_string, s1, "str_number_of_own_troops_wounded_reg1"),
        (set_result_string, s1),
      (try_end),
  ]),
  
  #script_game_get_date_text:
  # This script is called from the game engine when the date needs to be displayed.
  # INPUT: arg1 = number of days passed since the beginning of the game
  # OUTPUT: result string = date
  ("game_get_date_text",
    [
		(store_script_param_1, ":version"),
      (store_script_param_2, ":num_hours"),
      (store_div, ":num_days", ":num_hours", 24),
      (store_add, ":cur_day", ":num_days", 23),
      (assign, ":cur_month", 3),
      (assign, ":cur_year", 1257),
      (assign, ":try_range", 99999),
      (try_for_range, ":unused", 0, ":try_range"),
        (try_begin),
          (this_or_next|eq, ":cur_month", 1),
          (this_or_next|eq, ":cur_month", 3),
          (this_or_next|eq, ":cur_month", 5),
          (this_or_next|eq, ":cur_month", 7),
          (this_or_next|eq, ":cur_month", 8),
          (this_or_next|eq, ":cur_month", 10),
          (eq, ":cur_month", 12),
          (assign, ":month_day_limit", 31),
        (else_try),
          (this_or_next|eq, ":cur_month", 4),
          (this_or_next|eq, ":cur_month", 6),
          (this_or_next|eq, ":cur_month", 9),
          (eq, ":cur_month", 11),
          (assign, ":month_day_limit", 30),
        (else_try),
          (try_begin),
            (store_div, ":cur_year_div_4", ":cur_year", 4),
            (val_mul, ":cur_year_div_4", 4),
            (eq, ":cur_year_div_4", ":cur_year"),
            (assign, ":month_day_limit", 29),
          (else_try),
            (assign, ":month_day_limit", 28),
          (try_end),
        (try_end),
        (try_begin),
          (gt, ":cur_day", ":month_day_limit"),
          (val_sub, ":cur_day", ":month_day_limit"),
          (val_add, ":cur_month", 1),
          (try_begin),
            (gt, ":cur_month", 12),
            (val_sub, ":cur_month", 12),
            (val_add, ":cur_year", 1),
          (try_end),
        (else_try),
          (assign, ":try_range", 0),
        (try_end),
      (try_end),
      (assign, reg1, ":cur_day"),
      (assign, reg2, ":cur_year"),
      (store_time_of_day, reg3), ## CC
	  (try_begin),
		(this_or_next|eq, ":version", 1),
		(eq, "$g_date", 1),
		(try_begin),
			(eq, ":cur_month", 1),
			(str_store_string, s1, "str_january_reg1_reg2_v2"),
		  (else_try),
			(eq, ":cur_month", 2),
			(str_store_string, s1, "str_february_reg1_reg2_v2"),
		  (else_try),
			(eq, ":cur_month", 3),
			(str_store_string, s1, "str_march_reg1_reg2_v2"),
		  (else_try),
			(eq, ":cur_month", 4),
			(str_store_string, s1, "str_april_reg1_reg2_v2"),
		  (else_try),
			(eq, ":cur_month", 5),
			(str_store_string, s1, "str_may_reg1_reg2_v2"),
		  (else_try),
			(eq, ":cur_month", 6),
			(str_store_string, s1, "str_june_reg1_reg2_v2"),
		  (else_try),
			(eq, ":cur_month", 7),
			(str_store_string, s1, "str_july_reg1_reg2_v2"),
		  (else_try),
			(eq, ":cur_month", 8),
			(str_store_string, s1, "str_august_reg1_reg2_v2"),
		  (else_try),
			(eq, ":cur_month", 9),
			(str_store_string, s1, "str_september_reg1_reg2_v2"),
		  (else_try),
			(eq, ":cur_month", 10),
			(str_store_string, s1, "str_october_reg1_reg2_v2"),
		  (else_try),
			(eq, ":cur_month", 11),
			(str_store_string, s1, "str_november_reg1_reg2_v2"),
		  (else_try),
			(eq, ":cur_month", 12),
			(str_store_string, s1, "str_december_reg1_reg2_v2"),
		  (try_end),
		(else_try),	  
		  (try_begin),
			(eq, ":cur_month", 1),
			(str_store_string, s1, "str_january_reg1_reg2"),
		  (else_try),
			(eq, ":cur_month", 2),
			(str_store_string, s1, "str_february_reg1_reg2"),
		  (else_try),
			(eq, ":cur_month", 3),
			(str_store_string, s1, "str_march_reg1_reg2"),
		  (else_try),
			(eq, ":cur_month", 4),
			(str_store_string, s1, "str_april_reg1_reg2"),
		  (else_try),
			(eq, ":cur_month", 5),
			(str_store_string, s1, "str_may_reg1_reg2"),
		  (else_try),
			(eq, ":cur_month", 6),
			(str_store_string, s1, "str_june_reg1_reg2"),
		  (else_try),
			(eq, ":cur_month", 7),
			(str_store_string, s1, "str_july_reg1_reg2"),
		  (else_try),
			(eq, ":cur_month", 8),
			(str_store_string, s1, "str_august_reg1_reg2"),
		  (else_try),
			(eq, ":cur_month", 9),
			(str_store_string, s1, "str_september_reg1_reg2"),
		  (else_try),
			(eq, ":cur_month", 10),
			(str_store_string, s1, "str_october_reg1_reg2"),
		  (else_try),
			(eq, ":cur_month", 11),
			(str_store_string, s1, "str_november_reg1_reg2"),
		  (else_try),
			(eq, ":cur_month", 12),
			(str_store_string, s1, "str_december_reg1_reg2"),
		  (try_end),
		(try_end),
      (set_result_string, s1),
  ]),
  
  #script_game_get_money_text:
  # This script is called from the game engine when an amount of money needs to be displayed.
  # INPUT: arg1 = amount in units
  # OUTPUT: result string = money in text
  ("game_get_money_text",
    [
      (store_script_param_1, ":amount"),
      (try_begin),
        (eq, ":amount", 1),
        (str_store_string, s1, "str_1_denar"),
      (else_try),
        (assign, reg1, ":amount"),
        (str_store_string, s1, "str_reg1_denars"),
      (try_end),
      (set_result_string, s1),
  ]),
  
  #script_game_get_party_companion_limit:
  # This script is called from the game engine when the companion limit is needed for a party.
  # INPUT: arg1 = none
  # OUTPUT: reg0 = companion_limit
  #Floris: Changed by Caba'drin to add a bonus for the player troop size in case you are King, Marshall and/or hold fiefs.
  ("game_get_party_companion_limit",
    [
      (assign, ":troop_no", "trp_player"),
      
      (assign, ":limit", 30),
      (store_skill_level, ":skill", "skl_leadership", ":troop_no"),
      (store_attribute_level, ":charisma", ":troop_no", ca_charisma),
      (val_mul, ":skill", 5),
      (val_add, ":limit", ":skill"),
      (val_add, ":limit", ":charisma"),
      
      (troop_get_slot, ":troop_renown", ":troop_no", slot_troop_renown),
      (store_div, ":renown_bonus", ":troop_renown", 20),
      (val_add, ":limit", ":renown_bonus"),
      
      (try_begin),
        (gt, "$players_kingdom", 0),
        (faction_slot_eq, "$players_kingdom", slot_faction_leader, ":troop_no"), #bonus for king
        (val_add, ":limit", 100),
        (assign, reg6, 100), #For size report
      (else_try),
        (assign, reg6, 0), #For size report
      (try_end),
      (try_begin),
        (gt, "$players_kingdom", 0), ##Floris 2.4: fix by Caba
        (faction_slot_eq, "$players_kingdom", slot_faction_marshall, ":troop_no"), #bonus for marshall
        (val_add, ":limit", 20),
        (assign, reg7, 20), #For size report
      (else_try),
        (assign, reg7, 0), #For size report
      (try_end),
      
      (assign, ":fief_count", 0),
      (assign, ":pre_limit", ":limit"),
      (try_for_range, ":cur_center", centers_begin, centers_end),
        (party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
        (val_add, ":fief_count", 1),
        (party_slot_eq, ":cur_center", slot_party_type, spt_castle), #This will do what this loop did previously, giving a 20 troop boost for each castle owned
        (val_add, ":limit", 20),
      (try_end),
      (store_sub, ":pre_limit", ":limit", ":pre_limit"),
      (assign, reg8, ":pre_limit"), #For size report, castles
      (try_begin),
        (gt, ":fief_count", 0),
        (val_add, ":limit", 10), #bonus for holding at least one fief and therefore being nobility
        (assign, reg9, 10), #For size report
      (else_try),
        (assign, reg9, 0), #For size report
      (try_end),
      
      (assign, reg0, ":limit"),
      (set_trigger_result, reg0),
  ]),
  
  
  #script_game_reset_player_party_name:
  # This script is called from the game engine when the player name is changed.
  # INPUT: none
  # OUTPUT: none
  ("game_reset_player_party_name",
     [(try_begin),                             ##Custom Player Party Name by Caba`Drin
      (party_slot_eq, 0, 1, 0),                ##Custom Player Party Name by Caba`Drin
      (str_store_troop_name, s5, "trp_player"),
	  (party_set_name, "p_main_party", s5), ##BUGFIX - Caba
	  (try_end),                               ##Custom Player Party Name by Caba`Drin
      #LAZERAS MODIFIED  {ENTK}  #BUGFIX - CABA - Commented out since this doesn't apply to players anyhow????
      # Jrider + TITLES v0.0, init new titles
      # (try_for_range, ":troop_no", active_npcs_begin, kingdom_ladies_end),
      #   (store_troop_faction, ":faction_no", ":troop_no"),
        #(call_script, "script_troop_set_title_according_to_faction_gender_and_lands", ":troop_no", ":faction_no"),
	  # 	(call_script, "script_troop_set_title_according_to_faction", ":troop_no", ":faction_no"), ##BUGFIX - Caba
      # (try_end),
      # Jrider 
      #LAZERAS MODIFIED  {ENTK}
  ]),
  
  #script_game_get_troop_note
  # This script is called from the game engine when the notes of a troop is needed.
  # INPUT: arg1 = troop_no, arg2 = note_index
  # OUTPUT: s0 = note
  ("game_get_troop_note",
    [
      (store_script_param_1, ":troop_no"),
      (store_script_param_2, ":note_index"),
      (set_trigger_result, 0),
      
      (str_store_troop_name, s54, ":troop_no"),
      (try_begin),
        (eq, ":troop_no", "trp_player"),
        (this_or_next|eq, "$player_has_homage", 1),
        (eq, "$players_kingdom", "fac_player_supporters_faction"),
        (assign, ":troop_faction", "$players_kingdom"),
      (else_try),
        (store_troop_faction, ":troop_faction", ":troop_no"),
      (try_end),
      (str_clear, s49),
      
      #Family notes
      (try_begin),
	    ##diplomacy start+ add support for displaying relations with kings and claimants
		#(this_or_next|is_between, ":troop_no", lords_begin, kingdom_ladies_end),
        #(eq, ":troop_no", "trp_player"),
        #(neg|is_between, ":troop_no", pretenders_begin, pretenders_end),
		
		(this_or_next|eq, ":troop_no", "trp_player"),
		(this_or_next|is_between, ":troop_no", lords_begin, kingdom_ladies_end),#includes pretenders
			(is_between, ":troop_no", kings_begin, kings_end),
		
		##The following would only show relations for kings and claimants if they are married.
        #(this_or_next|troop_slot_ge, ":troop_no", slot_troop_spouse, 0),
		#	(neg|is_between, ":troop_no", pretenders_begin, pretenders_end),
		#(this_or_next|troop_slot_ge, ":troop_no", slot_troop_spouse, 0),
		#	(neg|is_between, ":troop_no", kings_begin, kings_end),
		
		##diplomacy end+
        (assign, ":num_relations", 0),

        (try_begin),
          (call_script, "script_troop_get_family_relation_to_troop", "trp_player", ":troop_no"),
          (gt, reg0, 0),
          (val_add, ":num_relations", 1),
        (try_end),
		##diplomacy start+
        #(try_for_range, ":aristocrat", lords_begin, kingdom_ladies_end),
		#Display relations with kings and claimants
		(try_for_range, ":aristocrat", heroes_begin, heroes_end),
		  (this_or_next|is_between, ":aristocrat", lords_begin, kingdom_ladies_end),#includes pretenders
			  (is_between, ":aristocrat", kings_begin, kings_end),
		##diplomacy end+
          (call_script, "script_troop_get_family_relation_to_troop", ":aristocrat", ":troop_no"),
          (gt, reg0, 0),
          (val_add, ":num_relations", 1),
        (try_end),
        (try_begin),
          (gt, ":num_relations", 0),
          (try_begin),
            (eq, ":troop_no", "trp_player"),
            (str_store_string, s49, "str__family_"),
          (else_try),
            (troop_get_slot, reg1, ":troop_no", slot_troop_age),
            (str_store_string, s49, "str__age_reg1_family_"),
          (try_end),
          (try_begin),
            (call_script, "script_troop_get_family_relation_to_troop", "trp_player", ":troop_no"),
            (gt, reg0, 0),
            (str_store_troop_name_link, s12, "trp_player"),
            (val_sub, ":num_relations", 1),
            (try_begin),
              (eq, ":num_relations", 0),
              (str_store_string, s49, "str_s49_s12_s11_end"),
            (else_try),
              (str_store_string, s49, "str_s49_s12_s11"),
            (try_end),
          (try_end),
		  ##diplomacy start+
          #(try_for_range, ":aristocrat", lords_begin, kingdom_ladies_end),
		  #Display relations with kings and claimants
		  (try_for_range, ":aristocrat", heroes_begin, heroes_end),
		    (this_or_next|is_between, ":aristocrat", lords_begin, kingdom_ladies_end),#includes pretenders
			   (is_between, ":aristocrat", kings_begin, kings_end),
		  ##diplomacy end+
            (call_script, "script_troop_get_family_relation_to_troop", ":aristocrat", ":troop_no"),
            (gt, reg0, 0),
            (try_begin),
              (neg|is_between, ":aristocrat", kingdom_ladies_begin, kingdom_ladies_end),
              (eq, "$cheat_mode", 1),
              (str_store_troop_name_link, s12, ":aristocrat"),
              (call_script, "script_troop_get_relation_with_troop", ":aristocrat", ":troop_no"),
              (str_store_string, s49, "str_s49_s12_s11_rel_reg0"),
            (else_try),
              (str_store_troop_name_link, s12, ":aristocrat"),
              (val_sub, ":num_relations", 1),
              (try_begin),
                (eq, ":num_relations", 0),
                (str_store_string, s49, "str_s49_s12_s11_end"),
              (else_try),
                (str_store_string, s49, "str_s49_s12_s11"),
              (try_end),
            (try_end),
          (try_end),
        (try_end),
      (try_end),
      
      (try_begin),
        (neq, ":troop_no", "trp_player"),
        (neg|is_between, ":troop_faction", kingdoms_begin, kingdoms_end),
        (neg|is_between, ":troop_no", companions_begin, companions_end),
        (neg|is_between, ":troop_no", pretenders_begin, pretenders_end),
        
        (try_begin),
          (eq, ":note_index", 0),
          (str_store_string, s0, "str_s54_has_left_the_realm"),
          ##diplomacy start+
          #Check for "deceased" instead
          (try_begin),
             (troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_dead),
             (str_store_string, s0, "str_s54_is_deceased"),
          (try_end),
          ##diplomacy end+
          (set_trigger_result, 1),
        (else_try),
          (str_clear, s0),
          (this_or_next|eq, ":note_index", 1),
          (eq, ":note_index", 2),
          (set_trigger_result, 1),
        (try_end),

        
      (else_try),
        (is_between, ":troop_no", companions_begin, companions_end),
        (neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (eq, ":note_index", 0),
        (set_trigger_result, 1),
        (str_clear, s0),
        (assign, ":companion", ":troop_no"),
        (str_store_troop_name, s4, ":companion"),
        (try_begin),
          (troop_get_slot, ":days_left", ":companion", slot_troop_days_on_mission),
          (this_or_next|main_party_has_troop, ":companion"),
          (this_or_next|troop_slot_ge, ":companion", slot_troop_current_mission, 1),
          (eq, "$g_player_minister", ":companion"),
          
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
          (else_try),
            
            (troop_slot_ge, ":companion", slot_troop_current_mission, npc_mission_peace_request),
            (neg|troop_slot_ge, ":companion", slot_troop_current_mission, 8),
            
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
            (str_store_party_name, s9, "$g_player_court"),
            (is_between, "$g_player_court", centers_begin, centers_end),
            (str_store_string, s5, "str_in_your_court_at_s9"),
          (else_try),
            (eq, ":companion", "$g_player_minister"),
            (str_store_string, s8, "str_serving_as_minister"),
            (str_store_string, s5, "str_awaiting_the_capture_of_a_fortress_which_can_serve_as_your_court"),
          (else_try),
            (main_party_has_troop, ":companion"),
            (str_store_string, s8, "str_under_arms"),
            (str_store_string, s5, "str_in_your_party"),
          (try_end),
          
			(str_store_string, s0, "str_s4_s8_s5"),
		##diplomacy start+
		#Check for explicit "exiled" and "dead" settings
		(else_try),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_dead),
			(str_store_string, s0, "str_s54_is_deceased"),
		(else_try),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_exile),
			(str_store_string, s0, "str_s54_has_left_the_realm"),
		##diplomacy end+
		(else_try),
			(str_store_string, s0, "str_whereabouts_unknown"),
		(try_end),
        
        
      (else_try),
        (is_between, ":troop_no", pretenders_begin, pretenders_end),
        (neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (neq, ":troop_no", "$supported_pretender"),
        
        
        (troop_get_slot, ":orig_faction", ":troop_no", slot_troop_original_faction),
        (try_begin),
          (faction_slot_eq, ":orig_faction", slot_faction_state, sfs_active),
          (faction_slot_eq, ":orig_faction", slot_faction_has_rebellion_chance, 1),
          (try_begin),
            (eq, ":note_index", 0),
            (str_store_faction_name_link, s56, ":orig_faction"),
            ##diplomacy start+ xxx Removed third argument (was it doing anything?)
            #(str_store_string, s0, "@{s54} is a claimant to the throne of {s56}.", 0),
            (str_store_string, s0, "@{s54} is a claimant to the throne of {s56}."),
            ##diplomacy end+
            (set_trigger_result, 1),
          (try_end),
        (else_try),
          (try_begin),
            (str_clear, s0),
            (this_or_next|eq, ":note_index", 0),
            (this_or_next|eq, ":note_index", 1),
            (eq, ":note_index", 2),
            (set_trigger_result, 1),
          (try_end),
        (try_end),
        
      (else_try),
        (try_begin),
          (eq, ":note_index", 0),
          (faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),
          (str_store_troop_name_link, s55, ":faction_leader"),
          (str_store_faction_name_link, s56, ":troop_faction"),
          (assign, ":troop_is_player_faction", 0),
          (assign, ":troop_is_faction_leader", 0),
          (try_begin),
            (eq, ":troop_faction", "fac_player_faction"),
            (assign, ":troop_is_player_faction", 1),
          (else_try),
            (eq, ":faction_leader", ":troop_no"),
            (assign, ":troop_is_faction_leader", 1),
          (try_end),
          (assign, ":num_centers", 0),
          (str_store_string, s58, "@nowhere"),
          (try_for_range_backwards, ":cur_center", centers_begin, centers_end),
            (party_slot_eq, ":cur_center", slot_town_lord, ":troop_no"),
            (try_begin),
              (eq, ":num_centers", 0),
              (str_store_party_name_link, s58, ":cur_center"),
            (else_try),
              (eq, ":num_centers", 1),
              (str_store_party_name_link, s57, ":cur_center"),
              (str_store_string, s58, "@{s57} and {s58}"),
            (else_try),
              (str_store_party_name_link, s57, ":cur_center"),
              (str_store_string, s58, "@{!}{s57}, {s58}"),
            (try_end),
            (val_add, ":num_centers", 1),
          (try_end),
		  ##diplomacy start+ use script for gender
          #(troop_get_type, reg3, ":troop_no"),
        (call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 3),
		  #(assign, reg3, reg0),
		  ##diplomacy end+
          (troop_get_slot, reg5, ":troop_no", slot_troop_renown),
          (troop_get_slot, reg15, ":troop_no", slot_troop_controversy),
          
          (str_clear, s59),
          (try_begin),
            (call_script, "script_troop_get_player_relation", ":troop_no"),
            (assign, ":relation", reg0),
            (store_add, ":normalized_relation", ":relation", 100),
            (val_add, ":normalized_relation", 5),
            (store_div, ":str_offset", ":normalized_relation", 10),
            (val_clamp, ":str_offset", 0, 20),
            (store_add, ":str_id", "str_relation_mnus_100_ns",  ":str_offset"),
            (neq, ":str_id", "str_relation_plus_0_ns"),
            (str_store_string, s60, "@{reg3?She:He}"),
            (str_store_string, s59, ":str_id"),
            (str_store_string, s59, "@{!}^{s59}"),
          (try_end),
          #lord recruitment changes begin
          #This sends a bunch of political information to s47.
          
          #refresh registers
          (assign, reg9, ":num_centers"),
		  ##diplomacy start+ use script for gender
          #(troop_get_type, reg3, ":troop_no"),
		  (call_script, "script_dplmc_store_troop_is_female_reg", ":troop_no", 3),
		  ##diplomacy end+
          (troop_get_slot, reg5, ":troop_no", slot_troop_renown),
          (assign, reg4, ":troop_is_faction_leader"),
          (assign, reg6, ":troop_is_player_faction"),

          (troop_get_slot, reg17, ":troop_no", slot_troop_wealth), #DEBUGS
          ##diplomacy start+ xxx remove third argument (was it doing anything?)
          #(str_store_string, s0, "str_lord_info_string", 0),
          (str_store_string, s0, "str_lord_info_string"),
          ##diplomacy end+
          #lord recruitment changes end
          (add_troop_note_tableau_mesh, ":troop_no", "tableau_troop_note_mesh"),
          (set_trigger_result, 1),
        (try_end),
      (try_end),
     ]),
  
  #script_game_get_center_note
  # This script is called from the game engine when the notes of a center is needed.
  # INPUT: arg1 = center_no, arg2 = note_index
  # OUTPUT: s0 = note
  ("game_get_center_note",
    [
      (store_script_param_1, ":center_no"),
      (store_script_param_2, ":note_index"),

      (set_trigger_result, 0),
      (try_begin),
        (eq, ":note_index", 0),
        (party_get_slot, ":lord_troop", ":center_no", slot_town_lord),
        (try_begin),
          (ge, ":lord_troop", 0),
          (store_troop_faction, ":lord_faction", ":lord_troop"),
          (str_store_troop_name_link, s1, ":lord_troop"),
          (try_begin),
            (eq, ":lord_troop", "trp_player"),
            (gt, "$players_kingdom", 0),
            (str_store_faction_name_link, s2, "$players_kingdom"),
          (else_try),
            (str_store_faction_name_link, s2, ":lord_faction"),
          (try_end),
          (str_store_party_name, s50, ":center_no"),
          (try_begin),
            (party_slot_eq, ":center_no", slot_party_type, spt_town),
            (str_store_string, s51, "@The town of {s50}"),
          (else_try),
            (party_slot_eq, ":center_no", slot_party_type, spt_village),
            (party_get_slot, ":bound_center", ":center_no", slot_village_bound_center),
            (str_store_party_name_link, s52, ":bound_center"),
            (str_store_string, s51, "@The village of {s50} near {s52}"),
          (else_try),
            (str_store_string, s51, "@{!}{s50}"),
          (try_end),
          ##diplomacy start+ Show when the city is the home of a lord or is a court
          (assign, ":bound_center", reg0),#Save reg0 to avoid having it randomly change
          (try_begin),
             (eq, "$g_player_court", ":center_no"),
             (str_store_string, s2, "@{s51} belongs to {s1} of {s2}, and is where you make your court.^"),
          (else_try),
             (neq, ":lord_troop", "trp_player"),
             (neg|is_between, ":center_no", villages_begin, villages_end),
             (call_script, "script_lord_get_home_center", ":lord_troop"),
             (eq, reg0, ":center_no"),
             (call_script, "script_dplmc_get_troop_standing_in_faction", ":lord_troop", ":lord_faction"),
             (try_begin),
                (ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
                (call_script, "script_dplmc_store_troop_is_female", ":lord_troop"),
                (str_store_string, s2, "@{s51} belongs to {s1} of {s2}, and is where {reg0?she:he} makes {reg0?her:his} court.^"),
             (else_try),
                (call_script, "script_dplmc_store_troop_is_female", ":lord_troop"),
                (str_store_string, s2, "@{s51} belongs to {s1} of {s2}, and is where {reg0?she:he} makes {reg0?her:his} home.^"),
             (try_end),
          (else_try),#Fall through to normal behavior
          ##diplomacy end+
          (str_store_string, s2, "@{s51} belongs to {s1} of {s2}.^"),
          ##diplomacy start+
          (try_end),
          (assign, reg0, ":bound_center"),#Revert reg0 to avoid having it randomly change
          ##diplomacy end+
        (else_try),
          (str_clear, s2),
          ##diplomacy start+ Don't hide notes for centers with no lords.
          (store_faction_of_party, ":lord_faction", ":center_no"),
          (str_store_string, s1, "str_noone"),
          (try_begin),
             (ge, ":lord_faction", 1),
             (str_store_faction_name_link, s2, ":lord_faction"),
          (else_try),
             (str_store_string, s2, "str_noone"),
          (try_end),
          (str_store_party_name, s50, ":center_no"),
          (try_begin),
            (party_slot_eq, ":center_no", slot_party_type, spt_town),
            (str_store_string, s51, "@The town of {s50}"),
          (else_try),
            (party_slot_eq, ":center_no", slot_party_type, spt_village),
            (party_get_slot, ":bound_center", ":center_no", slot_village_bound_center),
            (str_store_party_name_link, s52, ":bound_center"),
            (str_store_string, s51, "@The village of {s50} near {s52}"),
          (else_try),
            (str_store_string, s51, "@{!}{s50}"),
          (try_end),
          (try_begin),
             (is_between, ":lord_faction", kingdoms_begin, kingdoms_end),
             (faction_slot_eq, ":lord_faction", slot_faction_state, sfs_active),
             (str_store_string, s2, "@{s51} belongs to {s2} but has not yet been granted to a lord.^"),
          (else_try),
             (str_store_string, s2, "@{s51} belongs to {s2}.^"),
          (try_end),
          ##diplomacy end+
        (try_end),
        (try_begin),
          (is_between, ":center_no", villages_begin, villages_end),
          ##diplomacy start+ Show market town if it differs from the bound center
          (party_get_slot, ":market_center", ":center_no", slot_village_market_town),
          (try_begin),
             (is_between, ":market_center", centers_begin, centers_end),
             (neq, ":market_center", ":center_no"),
             (neg|party_slot_eq, ":center_no", slot_village_bound_center, ":market_center"),
             (str_store_party_name_link, s8, ":market_center"),
             (str_store_string, s2, "@{s2}Its market town is {s8}.^"),
          (try_end),
          ##diplomacy end+
        (else_try),
          (assign, ":num_villages", 0),
          (try_for_range_backwards, ":village_no", villages_begin, villages_end),
            (party_slot_eq, ":village_no", slot_village_bound_center, ":center_no"),
            (try_begin),
              (eq, ":num_villages", 0),
              (str_store_party_name_link, s8, ":village_no"),
            (else_try),
              (eq, ":num_villages", 1),
              (str_store_party_name_link, s7, ":village_no"),
              (str_store_string, s8, "@{s7} and {s8}"),
            (else_try),
              (str_store_party_name_link, s7, ":village_no"),
              (str_store_string, s8, "@{!}{s7}, {s8}"),
            (try_end),
            (val_add, ":num_villages", 1),
          (try_end),
          (try_begin),
            (eq, ":num_villages", 0),
            (str_store_string, s2, "@{s2}It has no villages.^"),
          (else_try),
            (store_sub, reg0, ":num_villages", 1),
            (str_store_string, s2, "@{s2}{reg0?Its villages are:Its village is} {s8}.^"),
          (try_end),
        (try_end),
        (call_script, "script_get_prosperity_text_to_s50", ":center_no"),
        (str_store_string, s0, "@{s2}Its prosperity is: {s50}", 0),
        (set_trigger_result, 1),
      (try_end),
     ]),
  
  #script_game_get_faction_note
  # This script is called from the game engine when the notes of a faction is needed.
  # INPUT: arg1 = faction_no, arg2 = note_index
  # OUTPUT: s0 = note
  ("game_get_faction_note",
    [
      (store_script_param_1, ":faction_no"),
      (store_script_param_2, ":note_index"),
      (set_trigger_result, 0),
      
      ##      (try_begin),
      ##        (eq, 2, 1),
      ##        (str_store_faction_name, s14, ":faction_no"),
      ##        (assign, reg4, "$temp"),
      ##        (display_message, "str_updating_faction_notes_for_s14_temp_=_reg4"),
      ##      (try_end),
      
      (try_begin),
        (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
        #conditions end
        (try_begin),
          (eq, ":note_index", 0),
          (faction_get_slot, ":faction_leader", ":faction_no", slot_faction_leader),
          (str_store_faction_name, s5, ":faction_no"),
          ##diplomacy start+
          ##OLD:
          #(str_store_troop_name_link, s6, ":faction_leader"),
          ##NEW:
          (try_begin),
             (lt, ":faction_leader", 0),
             #(le, ":faction_leader", 0),
             #(this_or_next|lt, ":faction_leader", 0),
             #   (neg|is_between, ":faction_no", kingdoms_begin, kingdoms_end),
             (str_store_string, s6, "str_noone"),
          (else_try),
             (eq, ":faction_leader", "trp_kingdom_heroes_including_player_begin"),
             (assign, ":faction_leader", "trp_player"),
          (str_store_troop_name_link, s6, ":faction_leader"),
          (else_try),
             (str_store_troop_name_link, s6, ":faction_leader"),
          (try_end),
		 ##diplomacy end+
          (assign, ":num_centers", 0),
          (str_store_string, s8, "@nowhere"),
          (try_for_range_backwards, ":cur_center", centers_begin, centers_end),
            (store_faction_of_party, ":center_faction", ":cur_center"),
            (eq, ":center_faction", ":faction_no"),
            (try_begin),
              (eq, ":num_centers", 0),
              (str_store_party_name_link, s8, ":cur_center"),
            (else_try),
              (eq, ":num_centers", 1),
              (str_store_party_name_link, s7, ":cur_center"),
              (str_store_string, s8, "@{s7} and {s8}"),
            (else_try),
              (str_store_party_name_link, s7, ":cur_center"),
              (str_store_string, s8, "@{s7}, {s8}"), ## CC
            (try_end),
            (val_add, ":num_centers", 1),
          (try_end),
          (assign, ":num_members", 0),
          (str_store_string, s10, "@noone"),
          ##diplomacy start+ support for promoted kingdom ladies
          (try_for_range_backwards, ":loop_var", "trp_kingdom_heroes_including_player_begin", heroes_end),#<- changed active_npcs_end to heroes_end
          ##diplomacy end+
            (assign, ":cur_troop", ":loop_var"),
            (try_begin),
              (eq, ":loop_var", "trp_kingdom_heroes_including_player_begin"),
              (assign, ":cur_troop", "trp_player"),
              (assign, ":troop_faction", "$players_kingdom"),
            (else_try),
              (store_troop_faction, ":troop_faction", ":cur_troop"),
            (try_end),
            (eq, ":troop_faction", ":faction_no"),
            (neq, ":cur_troop", ":faction_leader"),
            (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
            (try_begin),
              (eq, ":num_members", 0),
              (str_store_troop_name_link, s10, ":cur_troop"),
            (else_try),
              (eq, ":num_members", 1),
              (str_store_troop_name_link, s9, ":cur_troop"),
              (str_store_string, s10, "@{s9} and {s10}"),
            (else_try),
              (str_store_troop_name_link, s9, ":cur_troop"),
              (str_store_string, s10, "@{s9}, {s10}"), ## CC
            (try_end),
            (val_add, ":num_members", 1),
          (try_end),
          
          #wars
          (str_store_string, s12, "@noone"),
          #       (assign, ":num_enemies", 0),
          #       (try_for_range_backwards, ":cur_faction", kingdoms_begin, kingdoms_end),
          #         (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
          #         (store_relation, ":cur_relation", ":cur_faction", ":faction_no"),
          #         (lt, ":cur_relation", 0),
          #         (try_begin),
          #           (eq, ":num_enemies", 0),
          #           (str_store_faction_name_link, s12, ":cur_faction"),
          #         (else_try),
          #           (eq, ":num_enemies", 1),
          #           (str_store_faction_name_link, s11, ":cur_faction"),
          #           (str_store_string, s12, "@the {s11} and the {s12}"),
          #         (else_try),
          #           (str_store_faction_name_link, s11, ":cur_faction"),
          #           (str_store_string, s12, "@the {s11}, the {s12}"),
          #         (try_end),
          #         (val_add, ":num_enemies", 1),
          #       (try_end),
          
          (str_store_string, s21, "str_foreign_relations__"),
          
          #other foreign relations
          (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
            (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
            (neq, ":faction_no", ":cur_faction"),
            (str_store_faction_name_link, s14, ":cur_faction"),
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":faction_no", ":cur_faction"),
            (assign, ":diplomatic_status", reg0),
            (assign, ":duration_of_status", reg1),
            
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":cur_faction", ":faction_no"),
            (assign, ":reverse_diplomatic_status", reg0),
            #			(assign, ":reverse_diplomatic_duration", reg1),
            
            (try_begin),
              (eq, ":diplomatic_status", -2),
              (str_store_string, s21, "str_s21__the_s5_is_at_war_with_the_s14"),
              (store_add, ":slot_war_damage_inflicted", ":cur_faction", slot_faction_war_damage_inflicted_on_factions_begin),
              (val_sub, ":slot_war_damage_inflicted", kingdoms_begin),
              (faction_get_slot, ":war_damage_inflicted", ":faction_no", ":slot_war_damage_inflicted"),
              (store_mul, ":war_damage_inflicted_x_2", ":war_damage_inflicted", 2),
              
              (store_add, ":slot_war_damage_suffered", ":faction_no", slot_faction_war_damage_inflicted_on_factions_begin),
              (val_sub, ":slot_war_damage_suffered", kingdoms_begin),
              (faction_get_slot, ":war_damage_suffered", ":cur_faction", ":slot_war_damage_suffered"),
              (store_mul, ":war_damage_suffered_x_2", ":war_damage_suffered", 2),
              
              
              (assign, ":war_cause", 0),
              (assign, ":attacker", 0),
              (try_for_range, ":log_entry", 0, "$num_log_entries"),
                (troop_get_slot, ":type", "trp_log_array_entry_type", ":log_entry"),
                (is_between, ":type", logent_faction_declares_war_out_of_personal_enmity, logent_war_declaration_types_end),
                (troop_get_slot, ":actor", "trp_log_array_actor", ":log_entry"),
                (troop_get_slot, ":object", "trp_log_array_faction_object", ":log_entry"),
                
                (try_begin),
                  (eq, ":actor", ":cur_faction"),
                  (eq, ":object", ":faction_no"),
                  (assign, ":war_cause", ":type"),
                  (assign, ":attacker", ":actor"),
                (else_try),
                  (eq, ":actor", ":faction_no"),
                  (eq, ":object", ":cur_faction"),
                  (assign, ":war_cause", ":type"),
                  (assign, ":attacker", ":actor"),
                (try_end),
              (try_end),
              
              #bug fix! backing up s8 to somewhere else
              (str_store_string, s25, s8),
              (try_begin),
                (gt, ":war_cause", 0),
                (str_store_faction_name, s8, ":attacker"),
                (try_begin),
                  (eq, ":war_cause", logent_faction_declares_war_out_of_personal_enmity),
                  (str_store_string, s21, "str_s21_the_s8_declared_war_out_of_personal_enmity"),
                (else_try),
                  (eq, ":war_cause", logent_faction_declares_war_to_respond_to_provocation),
                  (str_store_string, s21, "str_s21_the_s8_declared_war_in_response_to_border_provocations"),
                (else_try),
                  (eq, ":war_cause", logent_faction_declares_war_to_curb_power),
                  (str_store_string, s21, "str_s21_the_s8_declared_war_to_curb_the_other_realms_power"),
                (else_try),
                  (eq, ":war_cause", logent_faction_declares_war_to_regain_territory),
                  (str_store_string, s21, "str_s21_the_s8_declared_war_to_regain_lost_territory"),
                  ##diplomacy begin
                (else_try),
                  (eq, ":war_cause", logent_faction_declares_war_to_fulfil_pact),
                  (str_store_string, s21, "str_dplmc_s21_the_s8_declared_war_to_fulfil_pact"),
                  ##diplomacy end
                (else_try),
                  (eq, ":war_cause", logent_player_faction_declares_war),
                  (neq, ":attacker", "fac_player_supporters_faction"),
                  (str_store_string, s21, "str_s21_the_s8_declared_war_as_part_of_a_bid_to_conquer_all_calradia"),
                (try_end),
              (try_end),
              #bug fix! restoring the back up to s8
              (str_store_string, s8, s25),
              
              (try_begin),
                (gt, ":war_damage_inflicted", ":war_damage_suffered_x_2"),
                (str_store_string, s21, "str_s21_the_s5_has_had_the_upper_hand_in_the_fighting"),
              (else_try),
                (gt, ":war_damage_suffered", ":war_damage_inflicted_x_2"),
                (str_store_string, s21, "str_s21_the_s5_has_gotten_the_worst_of_the_fighting"),
              (else_try),
                (gt, ":war_damage_inflicted", 100),
                (gt, ":war_damage_inflicted", 100),
                (str_store_string, s21, "str_s21_the_fighting_has_gone_on_for_some_time_and_the_war_may_end_soon_with_a_truce"),
              (else_try),
                (str_store_string, s21, "str_s21_the_fighting_has_begun_relatively_recently_and_the_war_may_continue_for_some_time"),
              (try_end),
              (try_begin),
                (eq, "$cheat_mode", 1),
                (assign, reg4, ":war_damage_inflicted"),
                (assign, reg5, ":war_damage_suffered"),
                (str_store_string, s21, "str_s21_reg4reg5"),
              (try_end),
            (else_try),
              (eq, ":diplomatic_status", 1),
              (str_clear, s18),
              (try_begin),
                (neq, ":reverse_diplomatic_status", 1),
                (str_store_string, s18, "str__however_the_truce_is_no_longer_binding_on_the_s14"),
              (try_end),
              (assign, reg1, ":duration_of_status"),
              ##diplomacy begin
			(try_begin),
			    ##nested diplomacy start+ Use named variables for truce lengths
                #(is_between, ":duration_of_status", 1, 21),
				(is_between, ":duration_of_status", dplmc_treaty_truce_days_expire + 1, dplmc_treaty_truce_days_initial + 1),
				##nested diplomacy end+
                ##diplomacy end
                (str_store_string, s21, "str_s21__the_s5_is_bound_by_truce_not_to_attack_the_s14s18_the_truce_will_expire_in_reg1_days"),
                ##diplomacy begin
			  ##nested diplomacy start+ Use named variables for truce lengths
              (else_try),
                #(is_between, ":duration_of_status", 21, 41),
                #(val_sub, reg1, 20),
                (is_between, ":duration_of_status", dplmc_treaty_trade_days_expire + 1, dplmc_treaty_trade_days_initial + 1),
                (val_sub, reg1, dplmc_treaty_trade_days_expire),
                (str_store_string, s21, "str_dplmc_s21__the_s5_is_bound_by_trade_not_to_attack_the_s14s18_it_will_expire_in_reg1_days"),
              (else_try),
                #(is_between, ":duration_of_status", 41, 61),
                #(val_sub, reg1, 40),
                (is_between, ":duration_of_status", dplmc_treaty_defense_days_expire + 1, dplmc_treaty_defense_days_initial + 1),
                (val_sub, reg1, dplmc_treaty_defense_days_expire),
                (str_store_string, s21, "str_dplmc_s21__the_s5_is_bound_by_defensive_not_to_attack_the_s14s18_it_will_expire_in_reg1_days"),
              (else_try),
                #(is_between, ":duration_of_status", 61, 81),
                #(val_sub, reg1, 60),
                (is_between, ":duration_of_status", dplmc_treaty_alliance_days_expire + 1, dplmc_treaty_alliance_days_initial + 1),
                (val_sub, reg1, dplmc_treaty_alliance_days_expire),
                (str_store_string, s21, "str_dplmc_s21__the_s5_is_bound_by_alliance_not_to_attack_the_s14s18_it_will_expire_in_reg1_days"),
              (try_end),
			  ##nested diplomacy end+ (Use named variables for truce lengths)
              ##diplomacy end
            (else_try),
              (eq, ":diplomatic_status", -1),
              (str_store_string, s21, "str_s21__the_s5_has_recently_suffered_provocation_by_subjects_of_the_s14_and_there_is_a_risk_of_war"),
            (else_try),
              (eq, ":diplomatic_status", 0),
              (str_store_string, s21, "str_s21__the_s5_has_no_outstanding_issues_with_the_s14"),
            (try_end),
            (try_begin),
              (eq, ":reverse_diplomatic_status", -1),
              (str_store_string, s21, "str_s21_the_s14_was_recently_provoked_by_subjects_of_the_s5_and_there_is_a_risk_of_war_"),
            (try_end),
            (try_begin),
              (eq, "$cheat_mode", 1),
              (call_script, "script_npc_decision_checklist_peace_or_war", ":faction_no", ":cur_faction", -1),
              (str_store_string, s21, "@{!}DEBUG : {s21}.^CHEAT MODE ASSESSMENT: {s14}^"),
            (try_end),
          (try_end),
          (str_store_string, s0, "str_the_s5_is_ruled_by_s6_it_occupies_s8_its_vassals_are_s10__s21", 0),
          (set_trigger_result, 1),
        (try_end),
      (else_try),
        (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_slot_eq, ":faction_no", slot_faction_state, sfs_defeated),
        (try_begin),
          (eq, ":note_index", 0),
          (str_store_faction_name, s5, ":faction_no"),
          (str_store_string, s0, "@{s5} has been defeated!", 0),
          (set_trigger_result, 1),
        (else_try),
          (eq, ":note_index", 1),
          (str_clear, s0),
          (set_trigger_result, 1),
        (try_end),
      (else_try),
        (try_begin),
          (this_or_next|eq, ":note_index", 0),
          (eq, ":note_index", 1),
          (str_clear, s0),
          (set_trigger_result, 1),
        (try_end),
      (try_end),
  ]),
  
  #script_game_get_quest_note
  # This script is called from the game engine when the notes of a quest is needed.
  # INPUT: arg1 = quest_no, arg2 = note_index
  # OUTPUT: s0 = note
  ("game_get_quest_note",
    [
      ##      (store_script_param_1, ":quest_no"),
      ##      (store_script_param_2, ":note_index"),
      (set_trigger_result, 0), # set it to 1 if this script is wanted to be used rather than static notes
  ]),
  
  #script_game_get_info_page_note
  # This script is called from the game engine when the notes of a info_page is needed.
  # INPUT: arg1 = info_page_no, arg2 = note_index
  # OUTPUT: s0 = note
  ("game_get_info_page_note",
    [
      ##      (store_script_param_1, ":info_page_no"),
      ##      (store_script_param_2, ":note_index"),
      (set_trigger_result, 0), # set it to 1 if this script is wanted to be used rather than static notes
  ]),
  
  #script_game_get_scene_name
  # This script is called from the game engine when a name for the scene is needed.
  # INPUT: arg1 = scene_no
  # OUTPUT: s0 = name
  ("game_get_scene_name",
    [
      (store_script_param, ":scene_no", 1),
      (try_begin),
        (is_between, ":scene_no", multiplayer_scenes_begin, multiplayer_scenes_end),
        (store_sub, ":string_id", ":scene_no", multiplayer_scenes_begin),
        (val_add, ":string_id", multiplayer_scene_names_begin),
        (str_store_string, s0, ":string_id"),
      (try_end),
  ]),
  
  #script_game_get_mission_template_name
  # This script is called from the game engine when a name for the mission template is needed.
  # INPUT: arg1 = mission_template_no
  # OUTPUT: s0 = name
  ("game_get_mission_template_name",
    [
      (store_script_param, ":mission_template_no", 1),
      (call_script, "script_multiplayer_get_mission_template_game_type", ":mission_template_no"),
      (assign, ":game_type", reg0),
      (try_begin),
        (is_between, ":game_type", 0, multiplayer_num_game_types),
        (store_add, ":string_id", ":game_type", multiplayer_game_type_names_begin),
        (str_store_string, s0, ":string_id"),
      (try_end),
  ]),
  
  #script_add_kill_death_counts
  # INPUT: arg1 = killer_agent_no, arg2 = dead_agent_no
  # OUTPUT: none
  ("add_kill_death_counts",
    [
      (store_script_param, ":killer_agent_no", 1),
      (store_script_param, ":dead_agent_no", 2),
      
      (try_begin),
        (ge, ":killer_agent_no", 0),
        (agent_get_team, ":killer_agent_team", ":killer_agent_no"),
      (else_try),
        (assign, ":killer_agent_team", -1),
      (try_end),
      
      (try_begin),
        (ge, ":dead_agent_no", 0),
        (agent_get_team, ":dead_agent_team", ":dead_agent_no"),
      (else_try),
        (assign, ":dead_agent_team", -1),
      (try_end),
      
      #adjusting kill counts of players/bots
      (try_begin),
        (try_begin),
          (ge, ":killer_agent_no", 0),
          (ge, ":dead_agent_no", 0),
          (agent_is_human, ":killer_agent_no"),
          (agent_is_human, ":dead_agent_no"),
          (neq, ":killer_agent_no", ":dead_agent_no"),
          
          (this_or_next|neq, ":killer_agent_team", ":dead_agent_team"),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
          
          (agent_get_player_id, ":killer_agent_player", ":killer_agent_no"),
          (try_begin),
            (agent_is_non_player, ":killer_agent_no"), #if killer agent is bot then increase bot kill counts of killer agent's team by one.
            (agent_get_team, ":killer_agent_team", ":killer_agent_no"),
            (team_get_bot_kill_count, ":killer_agent_team_bot_kill_count", ":killer_agent_team"),
            (val_add, ":killer_agent_team_bot_kill_count", 1),
            (team_set_bot_kill_count, ":killer_agent_team", ":killer_agent_team_bot_kill_count"),
          (else_try), #if killer agent is not bot then increase kill counts of killer agent's player by one.
            (player_is_active, ":killer_agent_player"),
            (player_get_kill_count, ":killer_agent_player_kill_count", ":killer_agent_player"),
            (val_add, ":killer_agent_player_kill_count", 1),
            (player_set_kill_count, ":killer_agent_player", ":killer_agent_player_kill_count"),
          (try_end),
        (try_end),
        
        (try_begin),
          (ge, ":dead_agent_no", 0),
          (agent_is_human, ":dead_agent_no"),
          (try_begin),
            (agent_is_non_player, ":dead_agent_no"), #if dead agent is bot then increase bot kill counts of dead agent's team by one.
            (agent_get_team, ":dead_agent_team", ":dead_agent_no"),
            (team_get_bot_death_count, ":dead_agent_team_bot_death_count", ":dead_agent_team"),
            (val_add, ":dead_agent_team_bot_death_count", 1),
            (team_set_bot_death_count, ":dead_agent_team", ":dead_agent_team_bot_death_count"),
          (else_try), #if dead agent is not bot then increase death counts of dead agent's player by one.
            (agent_get_player_id, ":dead_agent_player", ":dead_agent_no"),
            (player_is_active, ":dead_agent_player"),
            (player_get_death_count, ":dead_agent_player_death_count", ":dead_agent_player"),
            (val_add, ":dead_agent_player_death_count", 1),
            (player_set_death_count, ":dead_agent_player", ":dead_agent_player_death_count"),
          (try_end),
          
          (try_begin),
            (assign, ":continue", 0),
            
            (try_begin),
              (this_or_next|lt, ":killer_agent_no", 0), #if he killed himself (1a(team change) or 1b(self kill)) then decrease kill counts of killer player by one.
              (eq, ":killer_agent_no", ":dead_agent_no"),
              (assign, ":continue", 1),
            (try_end),
            
            (try_begin),
              (eq, ":killer_agent_team", ":dead_agent_team"), #if he killed a teammate and game mod is not deathmatch then decrease kill counts of killer player by one.
              (neq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
              (neq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
              (assign, ":continue", 1),
            (try_end),
            
            (eq, ":continue", 1),
            
            (try_begin),
              (ge, ":killer_agent_no", 0),
              (assign, ":responsible_agent", ":killer_agent_no"),
            (else_try),
              (assign, ":responsible_agent", ":dead_agent_no"),
            (try_end),
            
            (try_begin),
              (ge, ":responsible_agent", 0),
              (neg|agent_is_non_player, ":responsible_agent"),
              (agent_get_player_id, ":responsible_player", ":responsible_agent"),
              (ge, ":responsible_player", 0),
              (player_get_kill_count, ":dead_agent_player_kill_count", ":responsible_player"),
              (val_add, ":dead_agent_player_kill_count", -1),
              (player_set_kill_count, ":responsible_player", ":dead_agent_player_kill_count"),
            (try_end),
          (try_end),
        (try_end),
      (try_end),
  ]),
  
  #script_warn_player_about_auto_team_balance
  # INPUT: none
  # OUTPUT: none
  ("warn_player_about_auto_team_balance",
    [
      (assign, "$g_multiplayer_message_type", multiplayer_message_type_auto_team_balance_next),
      (start_presentation, "prsnt_multiplayer_message_2"),
  ]),
  
  #script_check_team_balance
  # INPUT: none
  # OUTPUT: none
  ("check_team_balance",
    [
      (try_begin),
        (multiplayer_is_server),
        
        (assign, ":number_of_players_at_team_1", 0),
        (assign, ":number_of_players_at_team_2", 0),
        (get_max_players, ":num_players"),
        (try_for_range, ":cur_player", 0, ":num_players"),
          (player_is_active, ":cur_player"),
          (player_get_team_no, ":player_team", ":cur_player"),
          (try_begin),
            (eq, ":player_team", 0),
            (val_add, ":number_of_players_at_team_1", 1),
          (else_try),
            (eq, ":player_team", 1),
            (val_add, ":number_of_players_at_team_2", 1),
          (try_end),
        (try_end),
        
        (store_sub, ":difference_of_number_of_players", ":number_of_players_at_team_1", ":number_of_players_at_team_2"),
        (assign, ":number_of_players_will_be_moved", 0),
        (try_begin),
          (try_begin),
            (store_mul, ":checked_value", "$g_multiplayer_auto_team_balance_limit", -1),
            (le, ":difference_of_number_of_players", ":checked_value"),
            (store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", -2),
            (assign, ":team_with_more_players", 1),
            (assign, ":team_with_less_players", 0),
          (else_try),
            (ge, ":difference_of_number_of_players", "$g_multiplayer_auto_team_balance_limit"),
            (store_div, ":number_of_players_will_be_moved", ":difference_of_number_of_players", 2),
            (assign, ":team_with_more_players", 0),
            (assign, ":team_with_less_players", 1),
          (try_end),
        (try_end),
        #team balance checks are done
        (try_begin),
          (gt, ":number_of_players_will_be_moved", 0),
          (try_begin),
            (eq, "$g_team_balance_next_round", 1), #if warning is given
            
            #auto team balance starts
            (try_for_range, ":unused", 0, ":number_of_players_will_be_moved"),
              (assign, ":max_player_join_time", 0),
              (assign, ":latest_joined_player_no", -1),
              (get_max_players, ":num_players"),
              (try_for_range, ":player_no", 0, ":num_players"),
                (player_is_active, ":player_no"),
                (player_get_team_no, ":player_team", ":player_no"),
                (eq, ":player_team", ":team_with_more_players"),
                (player_get_slot, ":player_join_time", ":player_no", slot_player_join_time),
                (try_begin),
                  (gt, ":player_join_time", ":max_player_join_time"),
                  (assign, ":max_player_join_time", ":player_join_time"),
                  (assign, ":latest_joined_player_no", ":player_no"),
                (try_end),
              (try_end),
              (try_begin),
                (ge, ":latest_joined_player_no", 0),
                (try_begin),
                  #if player is living add +1 to his kill count because he will get -1 because of team change while living.
                  (player_get_agent_id, ":latest_joined_agent_id", ":latest_joined_player_no"),
                  (ge, ":latest_joined_agent_id", 0),
                  (agent_is_alive, ":latest_joined_agent_id"),
                  
                  (player_get_kill_count, ":player_kill_count", ":latest_joined_player_no"), #adding 1 to his kill count, because he will lose 1 undeserved kill count for dying during team change
                  (val_add, ":player_kill_count", 1),
                  (player_set_kill_count, ":latest_joined_player_no", ":player_kill_count"),
                  
                  (player_get_death_count, ":player_death_count", ":latest_joined_player_no"), #subtracting 1 to his death count, because he will gain 1 undeserved death count for dying during team change
                  (val_sub, ":player_death_count", 1),
                  (player_set_death_count, ":latest_joined_player_no", ":player_death_count"),
                  
                  (player_get_score, ":player_score", ":latest_joined_player_no"), #adding 1 to his score count, because he will lose 1 undeserved score for dying during team change
                  (val_add, ":player_score", 1),
                  (player_set_score, ":latest_joined_player_no", ":player_score"),
                  
                  (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
                    (player_is_active, ":player_no"),
                    (multiplayer_send_4_int_to_player, ":player_no", multiplayer_event_set_player_score_kill_death, ":latest_joined_player_no", ":player_score", ":player_kill_count", ":player_death_count"),
                  (try_end),
                  
                  (player_get_value_of_original_items, ":old_items_value", ":latest_joined_player_no"),
                  (player_get_gold, ":player_gold", ":latest_joined_player_no"),
                  (val_add, ":player_gold", ":old_items_value"),
                  (player_set_gold, ":latest_joined_player_no", ":player_gold", multi_max_gold_that_can_be_stored),
                (end_try),
                
                (player_set_troop_id, ":latest_joined_player_no", -1),
                (player_set_team_no, ":latest_joined_player_no", ":team_with_less_players"),
                (multiplayer_send_message_to_player, ":latest_joined_player_no", multiplayer_event_force_start_team_selection),
              (try_end),
            (try_end),
            
            #for only server itself-----------------------------------------------------------------------------------------------
            (call_script, "script_show_multiplayer_message", multiplayer_message_type_auto_team_balance_done, 0), #0 is useless here
            #for only server itself-----------------------------------------------------------------------------------------------
            (get_max_players, ":num_players"),
            (try_for_range, ":player_no", 1, ":num_players"),
              (player_is_active, ":player_no"),
              (multiplayer_send_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_auto_team_balance_done),
            (try_end),
            (assign, "$g_team_balance_next_round", 0),
            #auto team balance done
          (else_try),
            #tutorial message (next round there will be auto team balance)
            (assign, "$g_team_balance_next_round", 1),
            
            #for only server itself-----------------------------------------------------------------------------------------------
            (call_script, "script_show_multiplayer_message", multiplayer_message_type_auto_team_balance_next, 0), #0 is useless here
            #for only server itself-----------------------------------------------------------------------------------------------
            (get_max_players, ":num_players"),
            (try_for_range, ":player_no", 1, ":num_players"),
              (player_is_active, ":player_no"),
              (multiplayer_send_int_to_player, ":player_no", multiplayer_event_show_multiplayer_message, multiplayer_message_type_auto_team_balance_next),
            (try_end),
          (try_end),
        (else_try),
          (assign, "$g_team_balance_next_round", 0),
        (try_end),
      (try_end),
  ]),
  
  #script_check_creating_ladder_dust_effect
  # INPUT: arg1 = instance_id, arg2 = remaining_time
  # OUTPUT: none
  ("check_creating_ladder_dust_effect",
    [
      (store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":remaining_time"),
      
      (try_begin),
        (lt, ":remaining_time", 15), #less then 0.15 seconds
        (gt, ":remaining_time", 3), #more than 0.03 seconds
        
        (scene_prop_get_slot, ":smoke_effect_done", ":instance_id", scene_prop_smoke_effect_done),
        (scene_prop_get_slot, ":opened_or_closed", ":instance_id", scene_prop_open_or_close_slot),
        
        (try_begin),
          (eq, ":smoke_effect_done", 0),
          (eq, ":opened_or_closed", 0),
          
          (prop_instance_get_position, pos0, ":instance_id"),
          
          (assign, ":smallest_dist", -1),
          (try_for_range, ":entry_point_no", multi_entry_points_for_usable_items_start, multi_entry_points_for_usable_items_end),
            (entry_point_get_position, pos1, ":entry_point_no"),
            (get_sq_distance_between_positions, ":dist", pos0, pos1),
            (this_or_next|eq, ":smallest_dist", -1),
            (lt, ":dist", ":smallest_dist"),
            (assign, ":smallest_dist", ":dist"),
            (assign, ":nearest_entry_point", ":entry_point_no"),
          (try_end),
          
          (try_begin),
            (set_fixed_point_multiplier, 100),
            
            (ge, ":smallest_dist", 0),
            (lt, ":smallest_dist", 22500), #max 15m distance
            
            (entry_point_get_position, pos1, ":nearest_entry_point"),
            (position_rotate_x, pos1, -90),
            
            (prop_instance_get_scene_prop_kind, ":scene_prop_kind", ":instance_id"),
            (try_begin),
              (eq, ":scene_prop_kind", "spr_siege_ladder_move_6m"),
              (init_position, pos2),
              (position_set_z, pos2, 300),
              (position_transform_position_to_parent, pos3, pos1, pos2),
              (particle_system_burst, "psys_ladder_dust_6m", pos3, 100),
              (particle_system_burst, "psys_ladder_straw_6m", pos3, 100),
            (else_try),
              (eq, ":scene_prop_kind", "spr_siege_ladder_move_8m"),
              (init_position, pos2),
              (position_set_z, pos2, 400),
              (position_transform_position_to_parent, pos3, pos1, pos2),
              (particle_system_burst, "psys_ladder_dust_8m", pos3, 100),
              (particle_system_burst, "psys_ladder_straw_8m", pos3, 100),
            (else_try),
              (eq, ":scene_prop_kind", "spr_siege_ladder_move_10m"),
              (init_position, pos2),
              (position_set_z, pos2, 500),
              (position_transform_position_to_parent, pos3, pos1, pos2),
              (particle_system_burst, "psys_ladder_dust_10m", pos3, 100),
              (particle_system_burst, "psys_ladder_straw_10m", pos3, 100),
            (else_try),
              (eq, ":scene_prop_kind", "spr_siege_ladder_move_12m"),
              (init_position, pos2),
              (position_set_z, pos2, 600),
              (position_transform_position_to_parent, pos3, pos1, pos2),
              (particle_system_burst, "psys_ladder_dust_12m", pos3, 100),
              (particle_system_burst, "psys_ladder_straw_12m", pos3, 100),
            (else_try),
              (eq, ":scene_prop_kind", "spr_siege_ladder_move_14m"),
              (init_position, pos2),
              (position_set_z, pos2, 700),
              (position_transform_position_to_parent, pos3, pos1, pos2),
              (particle_system_burst, "psys_ladder_dust_14m", pos3, 100),
              (particle_system_burst, "psys_ladder_straw_14m", pos3, 100),
            (try_end),
            
            (scene_prop_set_slot, ":instance_id", scene_prop_smoke_effect_done, 1),
          (try_end),
        (try_end),
      (try_end),
  ]),
  
  #script_money_management_after_agent_death
  # INPUT: arg1 = killer_agent_no, arg2 = dead_agent_no
  # OUTPUT: none
  ("money_management_after_agent_death",
    [
      (store_script_param, ":killer_agent_no", 1),
      (store_script_param, ":dead_agent_no", 2),
      
      (assign, ":dead_agent_player_id", -1),
      
      (try_begin),
        (multiplayer_is_server),
        (ge, ":killer_agent_no", 0),
        (ge, ":dead_agent_no", 0),
        (agent_is_human, ":dead_agent_no"), #if dead agent is not horse
        (agent_is_human, ":killer_agent_no"), #if killer agent is not horse
        (agent_get_team, ":killer_agent_team", ":killer_agent_no"),
        (agent_get_team, ":dead_agent_team", ":dead_agent_no"),
        
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
        (neq, ":killer_agent_team", ":dead_agent_team"), #if these agents are enemies
        
        (neq, ":dead_agent_no", ":killer_agent_no"), #if agents are different, do not remove it is needed because in deathmatch mod, self killing passes here because of this or next.
        
        (try_begin),
          (neg|agent_is_non_player, ":dead_agent_no"),
          (agent_get_player_id, ":dead_player_no", ":dead_agent_no"),
          (player_get_slot, ":dead_agent_equipment_value", ":dead_player_no", slot_player_total_equipment_value),
        (else_try),
          (assign, ":dead_agent_equipment_value", 0),
        (try_end),
        
        (assign, ":dead_agent_team_human_players_count", 0),
        (get_max_players, ":num_players"),
        (try_for_range, ":player_no", 0, ":num_players"),
          (player_is_active, ":player_no"),
          (player_get_team_no, ":player_team", ":player_no"),
          (eq, ":player_team", ":dead_agent_team"),
          (val_add, ":dead_agent_team_human_players_count", 1),
        (try_end),
        
        (try_for_range, ":player_no", 0, ":num_players"),
          (player_is_active, ":player_no"),
          
          (try_begin),
            (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
            (eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
            (assign, ":one_spawn_per_round_game_type", 1),
          (else_try),
            (assign, ":one_spawn_per_round_game_type", 0),
          (try_end),
          
          (this_or_next|eq, ":one_spawn_per_round_game_type", 0),
          (this_or_next|player_slot_eq, ":player_no", slot_player_spawned_this_round, 0),
          (player_slot_eq, ":player_no", slot_player_spawned_this_round, 1),
          
          (player_get_agent_id, ":agent_no", ":player_no"),
          (try_begin),
            (eq, ":agent_no", ":dead_agent_no"), #if this agent is dead agent then get share from total loot. (20% of total equipment value)
            (player_get_gold, ":player_gold", ":player_no"),
            
            (assign, ":dead_agent_player_id", ":player_no"),
            
            #dead agent loot share (32%-48%-64%, norm : 48%)
            (store_mul, ":share_of_dead_agent", ":dead_agent_equipment_value", multi_dead_agent_loot_percentage_share),
            (val_div, ":share_of_dead_agent", 100),
            (val_mul, ":share_of_dead_agent", "$g_multiplayer_battle_earnings_multiplier"),
            (val_div, ":share_of_dead_agent", 100),
            (try_begin),
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch), #(4/3x) share if current mod is deathmatch
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_duel), #(4/3x) share if current mod is duel
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_team_deathmatch), #(4/3x) share if current mod is team_deathmatch
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag), #(4/3x) share if current mod is capture the flag
              (eq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters), #(4/3x) share if current mod is headquarters
              (val_mul, ":share_of_dead_agent", 4),
              (val_div, ":share_of_dead_agent", 3),
              (val_add, ":player_gold", ":share_of_dead_agent"),
            (else_try),
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle), #(2/3x) share if current mod is battle
              (eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy), #(2/3x) share if current mod is fight and destroy
              (val_mul, ":share_of_dead_agent", 2),
              (val_div, ":share_of_dead_agent", 3),
              (val_add, ":player_gold", ":share_of_dead_agent"),
            (else_try),
              (val_add, ":player_gold", ":share_of_dead_agent"), #(3/3x) share if current mod is siege
            (try_end),
            (player_set_gold, ":player_no", ":player_gold", multi_max_gold_that_can_be_stored),
          (else_try),
            (eq, ":agent_no", ":killer_agent_no"), #if this agent is killer agent then get share from total loot. (10% of total equipment value)
            (player_get_gold, ":player_gold", ":player_no"),
            
            #killer agent standart money (100-150-200, norm : 150)
            (assign, ":killer_agent_standard_money_addition", multi_killer_agent_standard_money_add),
            (val_mul, ":killer_agent_standard_money_addition", "$g_multiplayer_battle_earnings_multiplier"),
            (val_div, ":killer_agent_standard_money_addition", 100),
            (try_begin),
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch), #(4/3x) share if current mod is deathmatch
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_duel), #(4/3x) share if current mod is duel
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_team_deathmatch), #(4/3x) share if current mod is team_deathmatch
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag), #(4/3x) share if current mod is capture the flag
              (eq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters), #(4/3x) share if current mod is headquarters
              (val_mul, ":killer_agent_standard_money_addition", 4),
              (val_div, ":killer_agent_standard_money_addition", 3),
              (val_add, ":player_gold", ":killer_agent_standard_money_addition"),
            (else_try),
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle), #(2/3x) share if current mod is battle
              (eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy), #(2/3x) share if current mod is fight and destroy
              (val_mul, ":killer_agent_standard_money_addition", 2),
              (val_div, ":killer_agent_standard_money_addition", 3),
              (val_add, ":player_gold", ":killer_agent_standard_money_addition"),
            (else_try),
              (val_add, ":player_gold", ":killer_agent_standard_money_addition"), #(3/3x) share if current mod is siege
            (try_end),
            
            #killer agent loot share (8%-12%-16%, norm : 12%)
            (store_mul, ":share_of_killer_agent", ":dead_agent_equipment_value", multi_killer_agent_loot_percentage_share),
            (val_div, ":share_of_killer_agent", 100),
            (val_mul, ":share_of_killer_agent", "$g_multiplayer_battle_earnings_multiplier"),
            (val_div, ":share_of_killer_agent", 100),
            (try_begin),
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch), #(4/3x) share if current mod is deathmatch
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_duel), #(4/3x) share if current mod is duel
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_team_deathmatch), #(4/3x) share if current mod is team_deathmatch
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag), #(4/3x) share if current mod is capture the flag
              (eq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters), #(4/3x) share if current mod is headquarters
              (val_mul, ":share_of_killer_agent", 4),
              (val_div, ":share_of_killer_agent", 3),
              (val_add, ":player_gold", ":share_of_killer_agent"),
            (else_try),
              (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle), #(2/3x) share if current mod is battle
              (eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy), #(2/3x) share if current mod is fight and destroy
              (val_mul, ":share_of_killer_agent", 2),
              (val_div, ":share_of_killer_agent", 3),
              (val_add, ":player_gold", ":share_of_killer_agent"),
            (else_try),
              (val_add, ":player_gold", ":share_of_killer_agent"), #(3/3x) share if current mod is siege
            (try_end),
            (player_set_gold, ":player_no", ":player_gold", multi_max_gold_that_can_be_stored),
          (try_end),
        (try_end),
      (try_end),
      
      #(below lines added new at 25.11.09 after Armagan decided new money system)
      (try_begin),
        (multiplayer_is_server),
        (neq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
        (neq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
        
        (ge, ":dead_agent_no", 0),
        (agent_is_human, ":dead_agent_no"), #if dead agent is not horse
        (agent_get_player_id, ":dead_agent_player_id", ":dead_agent_no"),
        (ge, ":dead_agent_player_id", 0),
        
        (player_get_gold, ":player_gold", ":dead_agent_player_id"),
        (try_begin),
          (store_mul, ":minimum_gold", "$g_multiplayer_initial_gold_multiplier", 10),
          (lt, ":player_gold", ":minimum_gold"),
          (assign, ":player_gold", ":minimum_gold"),
        (try_end),
        (player_set_gold, ":dead_agent_player_id", ":player_gold"),
      (try_end),
      #new money system addition end
  ]),
  
  ("initialize_aristocracy",
    [
      #LORD OCCUPATIONS, BLOOD RELATIONSHIPS, RENOWN AND REPUTATIONS
      
	  #King ages
	  (try_for_range, ":cur_troop", kings_begin, kings_end),
		(troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
		(store_random_in_range, ":age", 50, 60),
		(troop_set_slot, ":cur_troop", slot_troop_age, ":age"),
		##diplomacy start+
		#(eq, ":cur_troop", "trp_kingdom_5_lord"),#<-- There was no reason for this to be in the loop, so moved it out.
		#(troop_set_slot, ":cur_troop", slot_troop_age, 47),
	  (try_end),
	  (troop_set_slot, "trp_kingdom_5_lord", slot_troop_age, 47),#<-- Moved from above
	  ##diplomacy end+
      
      #The first thing - family structure
      #lords 1 to 8 are patriarchs with one live-at-home son and one daughter. They come from one of six possible ancestors, thus making it likely that there will be two sets of siblings
      #lords 9 to 12 are unmarried landowners with sisters
      #lords 13 to 20 are sons who still live in their fathers' houses
      #For the sake of simplicity, we can assume that all male aristocrats in prior generations either married commoners or procured their brides from the Old Country, thus discounting intermarriage
      
      (try_for_range, ":cur_troop", kingdom_ladies_begin, kingdom_ladies_end),
        (troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_lady),
      (try_end),
      
      (assign, ":cur_lady", "trp_kingdom_1_lady_1"),
      
      (try_for_range, ":cur_troop", lords_begin, lords_end),
        (troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
        
        (store_random_in_range, ":father_age_at_birth", 23, 26),
        #		(store_random_in_range, ":mother_age_at_birth", 19, 22),
        
        (try_begin),
          (is_between, ":cur_troop", "trp_knight_1_1", "trp_knight_2_1"),
          (store_sub, ":npc_seed", ":cur_troop", "trp_knight_1_1"),
          (assign, ":ancestor_seed", 1),
          
        (else_try),
          (is_between, ":cur_troop", "trp_knight_2_1", "trp_knight_3_1"),
          (store_sub, ":npc_seed", ":cur_troop", "trp_knight_2_1"),
          (assign, ":ancestor_seed", 7),
          
        (else_try),
          (is_between, ":cur_troop", "trp_knight_3_1", "trp_knight_4_1"),
          (store_sub, ":npc_seed", ":cur_troop", "trp_knight_3_1"),
          (assign, ":ancestor_seed", 13),
          
        (else_try),
          (is_between, ":cur_troop", "trp_knight_4_1", "trp_knight_5_1"),
          (store_sub, ":npc_seed", ":cur_troop", "trp_knight_4_1"),
          (assign, ":ancestor_seed", 19),
          
        (else_try),
          (is_between, ":cur_troop", "trp_knight_5_1", "trp_knight_6_1"),
          (store_sub, ":npc_seed", ":cur_troop", "trp_knight_5_1"),
          (assign, ":ancestor_seed", 25),
          
        (else_try),
          (is_between, ":cur_troop", "trp_knight_6_1", "trp_kingdom_1_pretender"),
          (store_sub, ":npc_seed", ":cur_troop", "trp_knight_6_1"),
          (assign, ":ancestor_seed", 31),
          
        (try_end),
        
        
		(try_begin),
			(lt, ":npc_seed", 8), #NPC seed is the order in the faction
			##diplomacy start+ do not overwrite reputation if it was already set explicitly
			(troop_get_slot, ":reputation", ":cur_troop", slot_lord_reputation_type),
			(try_begin),
				(lt, ":reputation", 1),
				#Original behavior:
				(assign, ":reputation", ":npc_seed"),
			(try_end),
			##diplomacy end+
			(store_random_in_range, ":age", 45, 64),

			##diplomacy start+ only set father if not already set
			(try_begin),#<- dplmc+ added
				(troop_slot_eq, ":cur_troop", slot_troop_father, -1),#<- dplmc+ added
				(store_random_in_range, ":father", 0, 6), #six possible fathers
				(val_add, ":father", ":ancestor_seed"),
				(troop_set_slot, ":cur_troop", slot_troop_father, ":father"),
			(try_end),#<- dplmc+ added
			##diplomacy end+

			#wife
			##diplomacy start+ do not rebind an already-set wife
			(try_begin),
				(troop_slot_eq, ":cur_troop", slot_troop_spouse, -1),
				#There may be a better solution, but to avoid oddities disable automatic spouses if there is a gender mismatch.
				#Mods that add additional races may want to tweak this (for example if some races shouldn't intermarry).
				(call_script, "script_dplmc_store_is_female_troop_1_troop_2", ":cur_troop", ":cur_lady"),
				#Types are stored to reg0 and reg1.
				(neq, reg0, reg1),#lord and lady aren't both female or both non-female
				(val_mul, reg0, reg1),
				(eq, reg0, 0),#at least one of lord or lady is non-female
			##diplomacy end+
				(troop_set_slot, ":cur_troop", slot_troop_spouse, ":cur_lady"),
				(troop_set_slot, ":cur_lady", slot_troop_spouse, ":cur_troop"),
				(store_random_in_range, ":wife_reputation", 20, 26),
				(try_begin),
					(eq, ":wife_reputation", 20),
					(assign, ":wife_reputation", lrep_conventional),
				(try_end),
				(troop_set_slot, ":cur_lady", slot_lord_reputation_type, ":wife_reputation"),


				(call_script, "script_init_troop_age", ":cur_lady", 49),
				(call_script, "script_add_lady_items", ":cur_lady"),

				(val_add, ":cur_lady", 1),
			##diplomacy start+
			(try_end),
			##diplomacy end+

			#daughter
			##diplomacy start+
			(try_begin),
			##diplomacy end+
				(troop_set_slot, ":cur_lady", slot_troop_father, ":cur_troop"),
				(store_sub, ":mother", ":cur_lady", 1),
				(call_script, "script_init_troop_age", ":cur_lady", 19),
			##diplomacy start+
				#fix native bug (daughters are their own mothers)
				#(troop_set_slot, ":cur_lady", slot_troop_mother, ":cur_lady"),
				(troop_set_slot, ":cur_lady", slot_troop_mother, ":mother"),
				(try_begin),
					#swap father and mother slots if the lord was female (do nothing if both were female)
					(call_script, "script_dplmc_store_is_female_troop_1_troop_2", ":cur_troop", ":mother"),
					(neq, reg0, 0),#:cur_troop is female
					(eq, reg1, 0),#:mother is not female
					(troop_set_slot, ":cur_lady", slot_troop_mother, ":cur_troop"),
					(troop_set_slot, ":cur_lady", slot_troop_father, ":mother"),
				(try_end),
			##diplomacy end+
				(store_random_in_range, ":lady_reputation", lrep_conventional, 34), #33% chance of father-derived
				(try_begin),
					(le, ":lady_reputation", 25),
					(troop_set_slot, ":cur_lady", slot_lord_reputation_type, ":lady_reputation"),
				(else_try),
					(eq, ":lady_reputation", 26),
					(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_conventional),
				(else_try),
					(eq, ":lady_reputation", 27),
					(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_moralist),
				(else_try),
					(assign, ":guardian_reputation", ":reputation"),
					(try_begin),
						(this_or_next|eq, ":guardian_reputation", lrep_martial),
							(eq, ":guardian_reputation", 0),
						(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_conventional),
					(else_try),
						(eq, ":guardian_reputation", lrep_quarrelsome),
						(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_otherworldly),
					(else_try),
						(eq, ":guardian_reputation", lrep_selfrighteous),
						(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_ambitious),
					(else_try),
						(eq, ":guardian_reputation", lrep_cunning),
						(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_adventurous),
					(else_try),
						(eq, ":guardian_reputation", lrep_goodnatured),
						(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_adventurous),
					(else_try),
						(eq, ":guardian_reputation", lrep_debauched),
						(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_ambitious),
					(else_try),
						(eq, ":guardian_reputation", lrep_upstanding),
						(troop_set_slot, ":cur_lady", slot_lord_reputation_type, lrep_moralist),
					(try_end),
				(try_end),

				(call_script, "script_add_lady_items", ":cur_lady"),
				(val_add, ":cur_lady", 1),
			##diplomacy start+
			(try_end),
			##diplomacy end+
			#high renown

		(else_try),	#Older unmarried lords
			(is_between, ":npc_seed", 8, 12),

			(store_random_in_range, ":age", 25, 36),
			##diplomacy start+ do not overwrite reputation if it was already set explicitly
			(troop_get_slot, ":reputation", ":cur_troop", slot_lord_reputation_type),
			(try_begin),
				(lt, ":reputation", 1),
				#Original behavior:
				(store_random_in_range, ":reputation", 0, 8),
			(try_end),
			##diplomacy end+

			(store_random_in_range, ":sister_reputation", 20, 26),
			(try_begin),
				(eq, ":sister_reputation", 20),
				(assign, ":sister_reputation", lrep_conventional),
			(try_end),
			(troop_set_slot, ":cur_lady", slot_lord_reputation_type, ":sister_reputation"),

			(troop_set_slot, ":cur_lady", slot_troop_guardian, ":cur_troop"),
			##diplomacy start+
			#Initialize parents
			(try_begin),
				(troop_slot_eq, ":cur_troop", slot_troop_father, -1),
				(store_mul, ":new_index", ":cur_troop", DPLMC_VIRTUAL_RELATIVE_MULTIPLIER),#defined in module_constants.py
				(val_add, ":new_index", DPLMC_VIRTUAL_RELATIVE_FATHER_OFFSET),#defined in module_constants.py
				(troop_set_slot, ":cur_troop", slot_troop_father, ":new_index"),
				(troop_slot_eq, ":cur_lady", slot_troop_father, -1),
				(troop_set_slot, ":cur_lady", slot_troop_father, ":new_index"),
			(try_end),
			(try_begin),
				(troop_slot_eq, ":cur_troop", slot_troop_mother, -1),
				(store_mul, ":new_index", ":cur_troop", DPLMC_VIRTUAL_RELATIVE_MULTIPLIER),#defined in module_constants.py
				(val_add, ":new_index", DPLMC_VIRTUAL_RELATIVE_MOTHER_OFFSET),#defined in module_constants.py
				(troop_set_slot, ":cur_troop", slot_troop_mother, ":new_index"),
				(troop_slot_eq, ":cur_lady", slot_troop_mother, -1),
				(troop_set_slot, ":cur_lady", slot_troop_mother, ":new_index"),
			(try_end),
			##diplomacy end+

			(call_script, "script_init_troop_age", ":cur_lady", 21),
			(call_script, "script_add_lady_items", ":cur_lady"),

			(val_add, ":cur_lady", 1),

		(else_try),	#Younger unmarried lords
			#age is father's minus 20 to 25
			(store_sub, ":father", ":cur_troop", 12),
			##diplomacy start+
			#Some submods don't pay attention to this aspect of the troop list, and
			#so initialization produces absurd or impossible results.  Prevent such
			#things from appearing in the game.
			(try_begin),
				#"father" can be father or mother
				#(troop_get_type, ":parent_type", ":father"),
				(try_begin),
					#(eq, ":parent_type", tf_female),
					(call_script, "script_cf_dplmc_troop_is_female", ":father"),
					(assign, ":parent_slot", slot_troop_mother),
					(assign, ":other_parent_slot", slot_troop_father),
				(else_try),
					(assign, ":parent_slot", slot_troop_father),
					(assign, ":other_parent_slot", slot_troop_mother),
				(try_end),
			
				(troop_slot_eq, ":cur_troop", ":parent_slot", -1),
				(store_add, ":logical_minimum_age", ":father_age_at_birth", 16),
				(troop_slot_ge, ":father", slot_troop_age, ":logical_minimum_age"),
				#Passed test
				(troop_set_slot, ":cur_troop", ":parent_slot", ":father"),
				#Set mother if not already specified
				(try_begin),
					(troop_slot_eq, ":cur_troop", ":other_parent_slot", -1),
					(troop_get_slot, ":mother", ":father", slot_troop_spouse),
					(troop_set_slot, ":cur_troop", ":other_parent_slot", ":mother"),
				(try_end),

				(troop_get_slot, ":father_age", ":father", slot_troop_age),
				(store_sub, ":age", ":father_age", ":father_age_at_birth"),
					
				(troop_get_slot, ":reputation", ":cur_troop", slot_lord_reputation_type),
				(try_begin),
					#Don't change reputation if it already has been set
					(lt, ":reputation", 1),
					#50% chance of having father's rep
					(store_random_in_range, ":reputation", 0, 16),

					(gt, ":reputation", 7),
					(troop_get_slot, ":reputation", ":father", slot_lord_reputation_type),
				(try_end),
			(else_try),
				#Average age is [45,63] minus [23,25], so [22, 38]
				(store_random_in_range, ":age", 22, 39),
				(troop_get_slot, ":reputation", ":cur_troop", slot_lord_reputation_type),
				#Don't change reputation if it already has been set
				(lt, ":reputation", 1),
				(store_random_in_range, ":reputation", 0, 8),
			(try_end),
			#diplomacy end+
		(try_end),
        
        (try_begin),
          (eq, ":reputation", 0),
          (assign, ":reputation", 1),
        (try_end),
        
        (troop_set_slot, ":cur_troop", slot_lord_reputation_type, ":reputation"),
        
        (call_script, "script_init_troop_age", ":cur_troop", ":age"),
      (try_end),
      
      (try_begin),
        (eq, "$cheat_mode", 1),
        (assign, reg3, "$cheat_mode"),
        (display_message, "@{!}DEBUG -- Assigned lord reputation and relations"),
        
        #	    (display_message, "str_assigned_lord_reputation_and_relations_cheat_mode_reg3"), #This string can be removed
      (try_end),
      
      (try_for_range, ":cur_troop", pretenders_begin, pretenders_end),
        (troop_set_slot, ":cur_troop", slot_troop_occupation, slto_inactive_pretender),
        (store_random_in_range, ":age", 25, 30),
        (troop_set_slot, ":cur_troop", slot_troop_age, ":age"),
        (eq, ":cur_troop", "trp_kingdom_5_pretender"),
        (troop_set_slot, ":cur_troop", slot_troop_age, 45),
      (try_end),
  ]),
  
  
  
  
  
  ("initialize_trade_routes",
    [
      #SARGOTH - 10 routes
      (call_script, "script_set_trade_route_between_centers", "p_town_1", "p_town_2"), #Sargoth - Tihr
      (call_script, "script_set_trade_route_between_centers", "p_town_1", "p_town_4"), #Sargoth - Suno
      (call_script, "script_set_trade_route_between_centers", "p_town_1", "p_town_12"), #Sargoth - Wercheg
      (call_script, "script_set_trade_route_between_centers", "p_town_1", "p_town_11"), #Sargoth - Curaw
      (call_script, "script_set_trade_route_between_centers", "p_town_1", "p_town_8"), #Sargoth - Reyvadin
      (call_script, "script_set_trade_route_between_centers", "p_town_1", "p_town_13"), #Sargoth - Rivacheg
      (call_script, "script_set_trade_route_between_centers", "p_town_1", "p_town_7"), #Sargoth - Uxkhal
      (call_script, "script_set_trade_route_between_centers", "p_town_1", "p_town_9"), #Sargoth - Khudan
      (call_script, "script_set_trade_route_between_centers", "p_town_1", "p_town_6"), #Sargoth - Praven
      (call_script, "script_set_trade_route_between_centers", "p_town_1", "p_town_15"), #Sargoth - Yalen
      (call_script, "script_set_trade_route_between_centers", "p_town_1", "p_town_16"), #Sargoth - Dhirim
      
      #TIHR- 8 Routes
      (call_script, "script_set_trade_route_between_centers", "p_town_2", "p_town_4"), #Tihr- Suno
      (call_script, "script_set_trade_route_between_centers", "p_town_2", "p_town_6"), #Tihr - Praven
      (call_script, "script_set_trade_route_between_centers", "p_town_2", "p_town_7"), #Tihr - Uxkhal
      (call_script, "script_set_trade_route_between_centers", "p_town_2", "p_town_15"), #Tihr - Yalen
      (call_script, "script_set_trade_route_between_centers", "p_town_2", "p_town_12"), #Tihr - Wercheg
      (call_script, "script_set_trade_route_between_centers", "p_town_2", "p_town_8"), #Tihr - Reyvadin
      (call_script, "script_set_trade_route_between_centers", "p_town_2", "p_town_11"), #Tihr - Curaw
      (call_script, "script_set_trade_route_between_centers", "p_town_2", "p_town_16"), #Thir - Dhirim
      
      #VELUCA - 8 Routes
      (call_script, "script_set_trade_route_between_centers", "p_town_3", "p_town_7"), #Veluca- Uxkhal
      (call_script, "script_set_trade_route_between_centers", "p_town_3", "p_town_5"), #Veluca - Jelkala
      (call_script, "script_set_trade_route_between_centers", "p_town_3", "p_town_15"), #Veluca - Yalen
      (call_script, "script_set_trade_route_between_centers", "p_town_3", "p_town_16"), #Veluca - Dhirim
      (call_script, "script_set_trade_route_between_centers", "p_town_3", "p_town_14"), #Veluca - Halmar
      (call_script, "script_set_trade_route_between_centers", "p_town_3", "p_town_4"), #Veluca - Suno
      (call_script, "script_set_trade_route_between_centers", "p_town_3", "p_town_19"), #Veluca - Shariz
      (call_script, "script_set_trade_route_between_centers", "p_town_3", "p_town_6"), #Veluca - Praven
      
      #SUNO - 11 routes
      #Sargoth, Tihr, Veluca
      (call_script, "script_set_trade_route_between_centers", "p_town_4", "p_town_12"), #Suno - Wercheg
      (call_script, "script_set_trade_route_between_centers", "p_town_4", "p_town_8"), #Suno - Reyvadin
      (call_script, "script_set_trade_route_between_centers", "p_town_4", "p_town_11"), #Suno - Curaw
      (call_script, "script_set_trade_route_between_centers", "p_town_4", "p_town_6"), #Suno - Praven
      (call_script, "script_set_trade_route_between_centers", "p_town_4", "p_town_7"), #Suno - Uxkhal
      (call_script, "script_set_trade_route_between_centers", "p_town_4", "p_town_16"), #Suno - Dhirim
      (call_script, "script_set_trade_route_between_centers", "p_town_4", "p_town_5"), #Suno - Jelkala
      (call_script, "script_set_trade_route_between_centers", "p_town_4", "p_town_15"), #Suno - Yalen
      
      #JELKALA - 6 ROUTES
      #Veluca, Suno
      (call_script, "script_set_trade_route_between_centers", "p_town_5", "p_town_15"), #Jelkala - Yalen
      (call_script, "script_set_trade_route_between_centers", "p_town_5", "p_town_6"), #Jelkala - Praven
      (call_script, "script_set_trade_route_between_centers", "p_town_5", "p_town_7"), #Jelkala - Uxkhal
      (call_script, "script_set_trade_route_between_centers", "p_town_5", "p_town_19"), #Jelkala - Shariz
      
      #PRAVEN - 7 ROUTES
      #Tihr, Veluca, Suno, Jelkala
      (call_script, "script_set_trade_route_between_centers", "p_town_6", "p_town_7"), #Praven - Uxkhal
      (call_script, "script_set_trade_route_between_centers", "p_town_6", "p_town_15"), #Praven - Yalen
      (call_script, "script_set_trade_route_between_centers", "p_town_6", "p_town_16"), #Praven - Dhirim
      
      #UXKHAL - 9 Routes
      #Sargoth, Tihr, Suno, Jelkala, Praven
      (call_script, "script_set_trade_route_between_centers", "p_town_7", "p_town_15"), #Yalen
      (call_script, "script_set_trade_route_between_centers", "p_town_7", "p_town_16"), #Dhirim
      (call_script, "script_set_trade_route_between_centers", "p_town_7", "p_town_19"), #Shariz
      (call_script, "script_set_trade_route_between_centers", "p_town_7", "p_town_14"), #Halmar
      
      #REYVADIN - 9 Routes
      #Suno, Sargoth
      (call_script, "script_set_trade_route_between_centers", "p_town_8", "p_town_9"), #Khudan
      (call_script, "script_set_trade_route_between_centers", "p_town_8", "p_town_11"), #Curaw
      (call_script, "script_set_trade_route_between_centers", "p_town_8", "p_town_12"), #Wercheg
      (call_script, "script_set_trade_route_between_centers", "p_town_8", "p_town_13"), #Rivacheg
      (call_script, "script_set_trade_route_between_centers", "p_town_8", "p_town_16"), #Dhirim
      (call_script, "script_set_trade_route_between_centers", "p_town_8", "p_town_18"), #Narra
      (call_script, "script_set_trade_route_between_centers", "p_town_8", "p_town_17"), #Ichamur
      
      #KHUDAN - 9 Routes
      #Sargoth, Reyvadin
      (call_script, "script_set_trade_route_between_centers", "p_town_9", "p_town_11"), #Curaw
      (call_script, "script_set_trade_route_between_centers", "p_town_9", "p_town_13"), #Rivacheg
      (call_script, "script_set_trade_route_between_centers", "p_town_9", "p_town_12"), #Wercheg
      (call_script, "script_set_trade_route_between_centers", "p_town_9", "p_town_17"), #Ichamur
      (call_script, "script_set_trade_route_between_centers", "p_town_9", "p_town_10"), #Tulga
      (call_script, "script_set_trade_route_between_centers", "p_town_9", "p_town_16"), #Dhirim
      (call_script, "script_set_trade_route_between_centers", "p_town_9", "p_town_18"), #Narra
      
      #TULGA - 7 Routes
      #Khudan
      (call_script, "script_set_trade_route_between_centers", "p_town_10", "p_town_17"), #Ichamur
      (call_script, "script_set_trade_route_between_centers", "p_town_10", "p_town_18"), #Narra
      (call_script, "script_set_trade_route_between_centers", "p_town_10", "p_town_22"), #Bariyye
      (call_script, "script_set_trade_route_between_centers", "p_town_10", "p_town_21"), #Ahmerrad
      (call_script, "script_set_trade_route_between_centers", "p_town_10", "p_town_14"), #Halmar
      (call_script, "script_set_trade_route_between_centers", "p_town_10", "p_town_20"), #Durquba
      
      #CURAW - 9 Routes
      #Khudan, Reyvadin, Sargoth, Suno
      (call_script, "script_set_trade_route_between_centers", "p_town_11", "p_town_12"), #Wercheg
      (call_script, "script_set_trade_route_between_centers", "p_town_11", "p_town_13"), #Rivacheg
      (call_script, "script_set_trade_route_between_centers", "p_town_11", "p_town_14"), #Halmar
      (call_script, "script_set_trade_route_between_centers", "p_town_11", "p_town_16"), #Dhirim
      (call_script, "script_set_trade_route_between_centers", "p_town_11", "p_town_17"), #Ichamur
      
      #WERCHEG - 7 Routes
      #Sargoth, Suno, Reyvadin, Khudan, Curaw, Tihr
      (call_script, "script_set_trade_route_between_centers", "p_town_12", "p_town_13"), #Rivacheg
      
      #RIVACHEG - 6 Routes
      #Sargoth, Reyvadin, Khudan, Curaw, Wercheg
      (call_script, "script_set_trade_route_between_centers", "p_town_13", "p_town_17"), #Ichamur
      
      #HALMAR- 11 Routes
      #Veluca, Uxkhal, Tulga, Curaw
      (call_script, "script_set_trade_route_between_centers", "p_town_14", "p_town_17"), #Ichamur
      (call_script, "script_set_trade_route_between_centers", "p_town_14", "p_town_18"), #Narra
      (call_script, "script_set_trade_route_between_centers", "p_town_14", "p_town_21"), #Ahmerrad
      (call_script, "script_set_trade_route_between_centers", "p_town_14", "p_town_22"), #Bariyye
      (call_script, "script_set_trade_route_between_centers", "p_town_14", "p_town_20"), #Durquba
      (call_script, "script_set_trade_route_between_centers", "p_town_14", "p_town_19"), #Shariz
      (call_script, "script_set_trade_route_between_centers", "p_town_14", "p_town_16"), #Dhirim
      
      #YALEN - 7 Routes
      #Sargoth, Tihr, Veluca, Suno, Jelkala, Praven, Uxkhal
      
      #DHIRIM - 13 Routes
      #Sargoth, Thir, Veluca, Suno, Praven, Uxkhal, Reyvadin, Khudan, Curaw, Halmar
      (call_script, "script_set_trade_route_between_centers", "p_town_16", "p_town_18"), #Narra
      (call_script, "script_set_trade_route_between_centers", "p_town_16", "p_town_20"), #Durquba
      (call_script, "script_set_trade_route_between_centers", "p_town_16", "p_town_19"), #Shariz
      
      #ICHAMUR - 7 Routes
      #Reyvadin, Khudan, Tulga, Curaw, Rivacheg, Halmar
      (call_script, "script_set_trade_route_between_centers", "p_town_17", "p_town_18"), #Narra
      
      #NARRA - 9 Routes
      #Reyvadin, Khudan, Tulga, Halmar, Dhirim, Ichamur
      (call_script, "script_set_trade_route_between_centers", "p_town_18", "p_town_20"), #Durquba
      (call_script, "script_set_trade_route_between_centers", "p_town_18", "p_town_21"), #Ahmerrad
      (call_script, "script_set_trade_route_between_centers", "p_town_18", "p_town_22"), #Bariyye
      
      #SHARIZ - 8 Routes
      #Veluca, Jelkala, Uxkhal, Halmar, Dhirim
      (call_script, "script_set_trade_route_between_centers", "p_town_19", "p_town_20"), #Durquba
      (call_script, "script_set_trade_route_between_centers", "p_town_19", "p_town_21"), #Ahmerrad
      (call_script, "script_set_trade_route_between_centers", "p_town_19", "p_town_22"), #Bariyye
      
      #DURQUBA - 7 Routes
      #Tulga, Halmar, Dhirim, Narra, Shariz
      (call_script, "script_set_trade_route_between_centers", "p_town_20", "p_town_21"), #Ahmerrad
      (call_script, "script_set_trade_route_between_centers", "p_town_20", "p_town_22"), #Bariyye
      
      #AHMERRAD - 6 Routes
      #Tulga, Halmar, Narra, Shariz, Durquba
      (call_script, "script_set_trade_route_between_centers", "p_town_21", "p_town_22"), #Bariyye
      
      #BARIYYE - 6 Routes
      #Tulga, Halmar, Narra, Shariz, Durquba, Ahmerrad
  ]),
  
  ("initialize_sea_trade_routes",
    [
     (party_set_slot, "p_town_1", slot_town_is_coastal, 4), #Sargoth
     (party_set_slot, "p_town_2", slot_town_is_coastal, 2), #Thir
     (party_set_slot, "p_town_6", slot_town_is_coastal, 3), #Praven
     (party_set_slot, "p_town_12", slot_town_is_coastal, 3), #Wercheg
     (party_set_slot, "p_town_13", slot_town_is_coastal, 5), #Rivacheg
     (party_set_slot, "p_town_15", slot_town_is_coastal, 4), #Yalen
     (party_set_slot, "p_town_19", slot_town_is_coastal, 8), #Shariz
	 
	   #Coastal town slots begin with no ships
	 (party_set_slot,"P_town_1", slot_town_has_ship, 0),
	 (party_set_slot,"P_town_2", slot_town_has_ship, 0),
	 (party_set_slot,"P_town_6", slot_town_has_ship, 0),
	 (party_set_slot,"P_town_12", slot_town_has_ship, 0),
	 (party_set_slot,"P_town_13", slot_town_has_ship, 0),
	 (party_set_slot,"P_town_15", slot_town_has_ship, 0),
	 (party_set_slot,"P_town_19", slot_town_has_ship, 0),	 
	 
      #RIVACHEG - 2 Routes
      (call_script, "script_set_trade_route_between_centers", "p_town_13", "p_town_2"), #Rivacheg - Thir
      (call_script, "script_set_trade_route_between_centers", "p_town_13", "p_town_6"), #Rivacheg - Praven
      
      #WERCHEG - 2 Routes
      (call_script, "script_set_trade_route_between_centers", "p_town_12", "p_town_2"), #Wercheg - Thir
      (call_script, "script_set_trade_route_between_centers", "p_town_12", "p_town_1"), #Wercheg - Sargoth
      
      #SARGOTH - 2 routes
      #Wercheg
      (call_script, "script_set_trade_route_between_centers", "p_town_1", "p_town_2"), #Sargoth - Tihr
      
      #TIHR - 4 Routes
      #Rivacheg, Wercheg, Sargoth
      (call_script, "script_set_trade_route_between_centers", "p_town_2", "p_town_6"), #Tihr - Praven
      
      #Praven - 3 Routes
      #Rivacheg, Thir
      (call_script, "script_set_trade_route_between_centers", "p_town_6", "p_town_15"), #Praven - Yalen
      
      #Yalen - 2 Routes
      #Praven
      (call_script, "script_set_trade_route_between_centers", "p_town_15", "p_town_19"), #Yalen - Shariz
      
      #Shariz - 1 Route
      #Yalen
  ]),
  
  
				##Floris MTT begin - all default to 'e' troop_trees_2
  ("initialize_faction_troop_types",
    [
      
      (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
        (faction_get_slot, ":culture", ":faction_no", slot_faction_culture),
        
        (faction_get_slot, ":troop", ":culture",  slot_faction_tier_1_troop),
        (faction_set_slot, ":faction_no",  slot_faction_tier_1_troop, ":troop"),
        (faction_get_slot, ":troop", ":culture",  slot_faction_tier_2_troop),
        (faction_set_slot, ":faction_no",  slot_faction_tier_2_troop, ":troop"),
        (faction_get_slot, ":troop", ":culture",  slot_faction_tier_3_troop),
        (faction_set_slot, ":faction_no",  slot_faction_tier_3_troop, ":troop"),
        (faction_get_slot, ":troop", ":culture",  slot_faction_tier_4_troop),
        (faction_set_slot, ":faction_no",  slot_faction_tier_4_troop, ":troop"),
        (faction_get_slot, ":troop", ":culture",  slot_faction_tier_5_troop),
        (faction_set_slot, ":faction_no",  slot_faction_tier_5_troop, ":troop"),
        
        (try_begin),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_1"),
          
          (faction_set_slot, ":faction_no",  slot_faction_deserter_troop, "trp_swadian_deserter"),
          (faction_set_slot, ":faction_no",  slot_faction_guard_troop, "trp_swadian_e_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_messenger_troop, "trp_swadian_messenger"),
          (faction_set_slot, ":faction_no",  slot_faction_prison_guard_troop, "trp_swadian_prison_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_castle_guard_troop, "trp_swadian_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_1_reinforcements_a_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_1_reinforcements_b_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_1_reinforcements_c_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_1_reinforcements_d_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_1_reinforcements_e_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_1_reinforcements_f_e"),
        (else_try),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_2"),
          
          (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_vaegir_deserter"),
          (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_vaegir_e_plastun"),
          (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_vaegir_messenger"),
          (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_vaegir_prison_guard"),
          (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_vaegir_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_2_reinforcements_a_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_2_reinforcements_b_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_2_reinforcements_c_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_2_reinforcements_d_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_2_reinforcements_e_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_2_reinforcements_f_e"),
        (else_try),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_3"),
          
          (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_khergit_deserter"),
          (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_khergit_e_aqala_asud"),
          (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_khergit_messenger"),
          (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_khergit_prison_guard"),
          (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_khergit_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_3_reinforcements_a_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_3_reinforcements_b_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_3_reinforcements_c_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_3_reinforcements_d_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_3_reinforcements_e_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_3_reinforcements_f_e"),
        (else_try),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_4"),
          
          (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_nord_deserter"),
          (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_nord_e_einhleyping"),
          (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_nord_messenger"),
          (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_nord_prison_guard"),
          (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_nord_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_4_reinforcements_a_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_4_reinforcements_b_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_4_reinforcements_c_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_4_reinforcements_d_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_4_reinforcements_e_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_4_reinforcements_f_e"),
        (else_try),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_5"),
          
          (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_rhodok_deserter"),
          (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_rhodok_e_lanciere_veterano"),
          (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_rhodok_messenger"),
          (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_rhodok_prison_guard"),
          (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_rhodok_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_5_reinforcements_a_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_5_reinforcements_b_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_5_reinforcements_c_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_5_reinforcements_d_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_5_reinforcements_e_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_5_reinforcements_f_e"),
        (else_try),
          (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_6"),
          
          (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_sarranid_deserter"),
          (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_sarranid_e_al_haqa"),
          (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_sarranid_messenger"),
          (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_sarranid_prison_guard"),
          (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_sarranid_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_6_reinforcements_a_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_6_reinforcements_b_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_6_reinforcements_c_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_6_reinforcements_d_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_6_reinforcements_e_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_6_reinforcements_f_e"),

          #Player Faction
                  (else_try),
                    (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_7"),
          
                    (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_custom_deserter"),
                    (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_custom_e_swordman"),
                    (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_custom_messenger"),
                    (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_custom_prison_guard"),
                    (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_custom_castle_guard"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_a, "pt_kingdom_7_reinforcements_a_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_b, "pt_kingdom_7_reinforcements_b_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_c, "pt_kingdom_7_reinforcements_c_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_d, "pt_kingdom_7_reinforcements_d_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_e, "pt_kingdom_7_reinforcements_e_e"),
          (faction_set_slot, ":faction_no",  slot_faction_reinforcements_f, "pt_kingdom_7_reinforcements_f_e"),
          #Player Faction
        (try_end),
      (try_end),
  ]),
				##Floris MTT end
  
  ("initialize_item_info",
    [
      # Setting food bonuses - these have been changed to incentivize using historical rations. Bread is the most cost-efficient
      #Staples
      (item_set_slot, "itm_trade_bread", slot_item_food_bonus, 8), #brought up from 4
      (item_set_slot, "itm_trade_grain", slot_item_food_bonus, 2), #new - can be boiled as porridge
      
      #Fat sources - preserved
      (item_set_slot, "itm_trade_smoked_fish", slot_item_food_bonus, 4),
      (item_set_slot, "itm_trade_dried_meat", slot_item_food_bonus, 5),
      (item_set_slot, "itm_trade_cheese", slot_item_food_bonus, 5),
      (item_set_slot, "itm_trade_sausages", slot_item_food_bonus, 5),
      (item_set_slot, "itm_trade_butter", slot_item_food_bonus, 4), #brought down from 8
      
      #Fat sources - perishable
      (item_set_slot, "itm_trade_chicken", slot_item_food_bonus, 8), #brought up from 7
      (item_set_slot, "itm_trade_cattle_meat", slot_item_food_bonus, 7), #brought down from 7
      (item_set_slot, "itm_trade_pork", slot_item_food_bonus, 6), #brought down from 6
      
      #Produce
      (item_set_slot, "itm_trade_raw_olives", slot_item_food_bonus, 1),
      (item_set_slot, "itm_trade_cabbages", slot_item_food_bonus, 2),
      (item_set_slot, "itm_trade_raw_grapes", slot_item_food_bonus, 3),
      (item_set_slot, "itm_trade_apples", slot_item_food_bonus, 4), #brought down from 5
      
      #Sweet items
      (item_set_slot, "itm_trade_raw_date_fruit", slot_item_food_bonus, 4), #brought down from 8
      (item_set_slot, "itm_trade_honey", slot_item_food_bonus, 6), #brought down from 12
      
      (item_set_slot, "itm_trade_wine", slot_item_food_bonus, 5),
      (item_set_slot, "itm_trade_ale", slot_item_food_bonus, 4),
      
      #Item economic settings
      (item_set_slot, "itm_trade_grain", slot_item_urban_demand, 20),
      (item_set_slot, "itm_trade_grain", slot_item_rural_demand, 20),
      (item_set_slot, "itm_trade_grain", slot_item_desert_demand, 20),
      (item_set_slot, "itm_trade_grain", slot_item_production_slot, slot_center_acres_grain),
      (item_set_slot, "itm_trade_grain", slot_item_production_string, "str_acres_grain"),
      (item_set_slot, "itm_trade_grain", slot_item_base_price, 30),
      
      (item_set_slot, "itm_trade_bread", slot_item_urban_demand, 30),
      (item_set_slot, "itm_trade_bread", slot_item_rural_demand, 30),
      (item_set_slot, "itm_trade_bread", slot_item_desert_demand, 30),
      (item_set_slot, "itm_trade_bread", slot_item_production_slot, slot_center_mills),
      (item_set_slot, "itm_trade_bread", slot_item_production_string, "str_mills"),
      (item_set_slot, "itm_trade_bread", slot_item_primary_raw_material, "itm_trade_grain"),
      (item_set_slot, "itm_trade_bread", slot_item_input_number, 6),
      (item_set_slot, "itm_trade_bread", slot_item_output_per_run, 6),
      (item_set_slot, "itm_trade_bread", slot_item_overhead_per_run, 30),
      (item_set_slot, "itm_trade_bread", slot_item_base_price, 50),
      (item_set_slot, "itm_trade_bread", slot_item_enterprise_building_cost, 1500),
      
      (item_set_slot, "itm_trade_ale", slot_item_urban_demand, 10),
      (item_set_slot, "itm_trade_ale", slot_item_rural_demand, 15),
      (item_set_slot, "itm_trade_ale", slot_item_desert_demand, 0),
      (item_set_slot, "itm_trade_ale", slot_item_production_slot, slot_center_breweries),
      (item_set_slot, "itm_trade_ale", slot_item_production_string, "str_breweries"),
      (item_set_slot, "itm_trade_ale", slot_item_base_price, 120),
      (item_set_slot, "itm_trade_ale", slot_item_primary_raw_material, "itm_trade_grain"),
      (item_set_slot, "itm_trade_ale", slot_item_input_number, 1),
      (item_set_slot, "itm_trade_ale", slot_item_output_per_run, 2),
      (item_set_slot, "itm_trade_ale", slot_item_overhead_per_run, 50),
      (item_set_slot, "itm_trade_ale", slot_item_base_price, 120),
      (item_set_slot, "itm_trade_ale", slot_item_enterprise_building_cost, 2500),
      
      (item_set_slot, "itm_trade_wine", slot_item_urban_demand, 15),
      (item_set_slot, "itm_trade_wine", slot_item_rural_demand, 10),
      (item_set_slot, "itm_trade_wine", slot_item_desert_demand, 25),
      (item_set_slot, "itm_trade_wine", slot_item_production_slot, slot_center_wine_presses),
      (item_set_slot, "itm_trade_wine", slot_item_production_string, "str_presses"),
      (item_set_slot, "itm_trade_wine", slot_item_primary_raw_material, "itm_trade_raw_grapes"),
      (item_set_slot, "itm_trade_wine", slot_item_input_number, 4),
      (item_set_slot, "itm_trade_wine", slot_item_output_per_run, 2),
      (item_set_slot, "itm_trade_wine", slot_item_overhead_per_run, 60),
      (item_set_slot, "itm_trade_wine", slot_item_base_price, 220),
      (item_set_slot, "itm_trade_wine", slot_item_enterprise_building_cost, 5000),
      
      (item_set_slot, "itm_trade_raw_grapes", slot_item_urban_demand, 0),
      (item_set_slot, "itm_trade_raw_grapes", slot_item_rural_demand, 0),
      (item_set_slot, "itm_trade_raw_grapes", slot_item_desert_demand, 0),
      (item_set_slot, "itm_trade_raw_grapes", slot_item_production_slot, slot_center_acres_vineyard),
      (item_set_slot, "itm_trade_raw_grapes", slot_item_production_string, "str_acres_orchard"),
      (item_set_slot, "itm_trade_raw_grapes", slot_item_is_raw_material_only_for, "itm_trade_wine"),
      (item_set_slot, "itm_trade_raw_grapes", slot_item_base_price, 75),
      
      (item_set_slot, "itm_trade_apples", slot_item_urban_demand, 4),
      (item_set_slot, "itm_trade_apples", slot_item_rural_demand, 4),
      (item_set_slot, "itm_trade_apples", slot_item_desert_demand, 0),
      (item_set_slot, "itm_trade_apples", slot_item_production_slot, slot_center_acres_vineyard),
      (item_set_slot, "itm_trade_apples", slot_item_production_string, "str_acres_orchard"),
      (item_set_slot, "itm_trade_apples", slot_item_base_price, 44),
      
      (item_set_slot, "itm_trade_smoked_fish", slot_item_urban_demand, 16),
      (item_set_slot, "itm_trade_smoked_fish", slot_item_rural_demand, 16),
      (item_set_slot, "itm_trade_smoked_fish", slot_item_desert_demand, 16),
      (item_set_slot, "itm_trade_smoked_fish", slot_item_production_slot, slot_center_fishing_fleet),
      (item_set_slot, "itm_trade_smoked_fish", slot_item_production_string, "str_boats"),
      
      (item_set_slot, "itm_trade_salt", slot_item_urban_demand, 5),
      (item_set_slot, "itm_trade_salt", slot_item_rural_demand, 3),
      (item_set_slot, "itm_trade_salt", slot_item_desert_demand, -1),
      (item_set_slot, "itm_trade_salt", slot_item_production_slot, slot_center_salt_pans),
      (item_set_slot, "itm_trade_salt", slot_item_production_string, "str_pans"),
      
      (item_set_slot, "itm_trade_dried_meat", slot_item_urban_demand, 20),							#	1.143 Port // increased from 15
      (item_set_slot, "itm_trade_dried_meat", slot_item_rural_demand, 5),								#	1.143 Port // decreased from 15
      (item_set_slot, "itm_trade_dried_meat", slot_item_desert_demand, -1),							#	1.143 Port // decreased from 15
      (item_set_slot, "itm_trade_dried_meat", slot_item_production_slot, slot_center_head_cattle),
      (item_set_slot, "itm_trade_dried_meat", slot_item_production_string, "str_head_cattle"),
	  
      (item_set_slot, "itm_trade_cattle_meat", slot_item_urban_demand, 12),							#	1.143 Port // newly added
      (item_set_slot, "itm_trade_cattle_meat", slot_item_rural_demand, 3),
      (item_set_slot, "itm_trade_cattle_meat", slot_item_desert_demand, -1),
      (item_set_slot, "itm_trade_cattle_meat", slot_item_production_slot, slot_center_head_cattle),
      (item_set_slot, "itm_trade_cattle_meat", slot_item_production_string, "str_head_cattle"),		#

      
      (item_set_slot, "itm_trade_cheese", slot_item_urban_demand, 10),
      (item_set_slot, "itm_trade_cheese", slot_item_rural_demand, 10),
      (item_set_slot, "itm_trade_cheese", slot_item_desert_demand, 10),
      (item_set_slot, "itm_trade_cheese", slot_item_production_slot, slot_center_head_cattle),
      (item_set_slot, "itm_trade_cheese", slot_item_production_string, "str_head_cattle"),
      
      (item_set_slot, "itm_trade_butter", slot_item_urban_demand, 2),
      (item_set_slot, "itm_trade_butter", slot_item_rural_demand, 2),
      (item_set_slot, "itm_trade_butter", slot_item_desert_demand, 2),
      (item_set_slot, "itm_trade_butter", slot_item_production_slot, slot_center_head_cattle),
      (item_set_slot, "itm_trade_butter", slot_item_production_string, "str_head_cattle"),
      
      (item_set_slot, "itm_trade_leatherwork", slot_item_urban_demand, 10),
      (item_set_slot, "itm_trade_leatherwork", slot_item_rural_demand, 10),
      (item_set_slot, "itm_trade_leatherwork", slot_item_desert_demand, 10),
      (item_set_slot, "itm_trade_leatherwork", slot_item_production_slot, slot_center_tanneries),
      (item_set_slot, "itm_trade_leatherwork", slot_item_production_string, "str_tanneries"),
      (item_set_slot, "itm_trade_leatherwork", slot_item_primary_raw_material, "itm_trade_raw_leather"),
      (item_set_slot, "itm_trade_leatherwork", slot_item_input_number, 3),
      (item_set_slot, "itm_trade_leatherwork", slot_item_output_per_run, 3),
      (item_set_slot, "itm_trade_leatherwork", slot_item_overhead_per_run, 50),
      (item_set_slot, "itm_trade_leatherwork", slot_item_base_price, 220),
      (item_set_slot, "itm_trade_leatherwork", slot_item_enterprise_building_cost, 8000),
      
      (item_set_slot, "itm_trade_raw_leather", slot_item_urban_demand, 0),
      (item_set_slot, "itm_trade_raw_leather", slot_item_rural_demand, 0),
      (item_set_slot, "itm_trade_raw_leather", slot_item_desert_demand, 0),
      (item_set_slot, "itm_trade_raw_leather", slot_item_production_slot, slot_center_head_cattle),
      (item_set_slot, "itm_trade_raw_leather", slot_item_production_string, "str_head_cattle"),
      (item_set_slot, "itm_trade_raw_leather", slot_item_is_raw_material_only_for, "itm_trade_leatherwork"),
      (item_set_slot, "itm_trade_raw_leather", slot_item_base_price, 120),
      
      (item_set_slot, "itm_trade_sausages", slot_item_urban_demand, 12),									#	1.143 Port //	increased from 5
      (item_set_slot, "itm_trade_sausages", slot_item_rural_demand, 3),									#	1.143 Port //	decreased from 5
      (item_set_slot, "itm_trade_sausages", slot_item_desert_demand, -1),									#	1.143 Port //	decreased from 5
      (item_set_slot, "itm_trade_sausages", slot_item_production_slot, slot_center_head_sheep),
      (item_set_slot, "itm_trade_sausages", slot_item_production_string, "str_head_sheep"),
      
      (item_set_slot, "itm_trade_wool", slot_item_urban_demand, 0),
      (item_set_slot, "itm_trade_wool", slot_item_rural_demand, 0),
      (item_set_slot, "itm_trade_wool", slot_item_desert_demand, 0),
      (item_set_slot, "itm_trade_wool", slot_item_production_slot, slot_center_head_sheep),
      (item_set_slot, "itm_trade_wool", slot_item_production_string, "str_head_sheep"),
      (item_set_slot, "itm_trade_wool", slot_item_is_raw_material_only_for, "itm_trade_wool_cloth"),
      (item_set_slot, "itm_trade_wool", slot_item_base_price,130),
      
      (item_set_slot, "itm_trade_wool_cloth", slot_item_urban_demand, 15),
      (item_set_slot, "itm_trade_wool_cloth", slot_item_rural_demand, 20),
      (item_set_slot, "itm_trade_wool_cloth", slot_item_desert_demand, 5),
      (item_set_slot, "itm_trade_wool_cloth", slot_item_production_slot, slot_center_wool_looms),
      (item_set_slot, "itm_trade_wool_cloth", slot_item_production_string, "str_looms"),
      (item_set_slot, "itm_trade_wool_cloth", slot_item_primary_raw_material, "itm_trade_wool"),
      (item_set_slot, "itm_trade_wool_cloth", slot_item_input_number, 2),
      (item_set_slot, "itm_trade_wool_cloth", slot_item_output_per_run, 2),
      (item_set_slot, "itm_trade_wool_cloth", slot_item_overhead_per_run, 120),
      (item_set_slot, "itm_trade_wool_cloth", slot_item_base_price, 250),
      (item_set_slot, "itm_trade_wool_cloth", slot_item_enterprise_building_cost, 6000),
      
      (item_set_slot, "itm_trade_raw_flax", slot_item_urban_demand, 0),
      (item_set_slot, "itm_trade_raw_flax", slot_item_rural_demand, 0),
      (item_set_slot, "itm_trade_raw_flax", slot_item_desert_demand, 0),
      (item_set_slot, "itm_trade_raw_flax", slot_item_production_slot, slot_center_acres_flax),
      (item_set_slot, "itm_trade_raw_flax", slot_item_production_string, "str_acres_flax"),
      (item_set_slot, "itm_trade_raw_flax", slot_item_is_raw_material_only_for, "itm_trade_linen"),
      (item_set_slot, "itm_trade_raw_flax", slot_item_base_price, 150),
      
      (item_set_slot, "itm_trade_linen", slot_item_urban_demand, 7),
      (item_set_slot, "itm_trade_linen", slot_item_rural_demand, 3),
      (item_set_slot, "itm_trade_linen", slot_item_desert_demand, 15),
      (item_set_slot, "itm_trade_linen", slot_item_production_slot, slot_center_linen_looms),
      (item_set_slot, "itm_trade_linen", slot_item_production_string, "str_looms"),
      (item_set_slot, "itm_trade_linen", slot_item_primary_raw_material, "itm_trade_raw_flax"),
      (item_set_slot, "itm_trade_linen", slot_item_input_number, 2),
      (item_set_slot, "itm_trade_linen", slot_item_output_per_run, 2),
      (item_set_slot, "itm_trade_linen", slot_item_overhead_per_run, 120),
      (item_set_slot, "itm_trade_linen", slot_item_base_price, 250),
      (item_set_slot, "itm_trade_linen", slot_item_enterprise_building_cost, 6000),
      
      (item_set_slot, "itm_trade_iron", slot_item_urban_demand, 0),
      (item_set_slot, "itm_trade_iron", slot_item_rural_demand, 0),
      (item_set_slot, "itm_trade_iron", slot_item_desert_demand, 0),
      (item_set_slot, "itm_trade_iron", slot_item_production_slot, slot_center_iron_deposits),
      (item_set_slot, "itm_trade_iron", slot_item_production_string, "str_deposits"),
      (item_set_slot, "itm_trade_iron", slot_item_is_raw_material_only_for, "itm_trade_tools"),
      (item_set_slot, "itm_trade_iron", slot_item_base_price, 264),
      
      (item_set_slot, "itm_trade_tools", slot_item_urban_demand, 7),
      (item_set_slot, "itm_trade_tools", slot_item_rural_demand, 7),
      (item_set_slot, "itm_trade_tools", slot_item_desert_demand, 7),
      (item_set_slot, "itm_trade_tools", slot_item_production_slot, slot_center_smithies),
      (item_set_slot, "itm_trade_tools", slot_item_production_string, "str_smithies"),
      (item_set_slot, "itm_trade_tools", slot_item_primary_raw_material, "itm_trade_iron"),
      (item_set_slot, "itm_trade_tools", slot_item_input_number, 2),
      (item_set_slot, "itm_trade_tools", slot_item_output_per_run, 2),
      (item_set_slot, "itm_trade_tools", slot_item_overhead_per_run, 60),
      (item_set_slot, "itm_trade_tools", slot_item_base_price, 410),
      (item_set_slot, "itm_trade_tools", slot_item_enterprise_building_cost, 3500),
      
      (item_set_slot, "itm_trade_pottery", slot_item_urban_demand, 5),							#	1.143 Port // Increased from 5
      (item_set_slot, "itm_trade_pottery", slot_item_rural_demand, 5),							
      (item_set_slot, "itm_trade_pottery", slot_item_desert_demand, -1),							#	1.143 Port // Decreased from 5
      (item_set_slot, "itm_trade_pottery", slot_item_production_slot, slot_center_pottery_kilns),
      (item_set_slot, "itm_trade_pottery", slot_item_production_string, "str_kilns"),
      
      (item_set_slot, "itm_trade_oil", slot_item_urban_demand, 10),
      (item_set_slot, "itm_trade_oil", slot_item_rural_demand, 5),
      (item_set_slot, "itm_trade_oil", slot_item_desert_demand, -1),
      (item_set_slot, "itm_trade_oil", slot_item_production_slot, slot_center_olive_presses),
      (item_set_slot, "itm_trade_oil", slot_item_production_string, "str_presses"),
      (item_set_slot, "itm_trade_oil", slot_item_primary_raw_material, "itm_trade_raw_olives"),
      (item_set_slot, "itm_trade_oil", slot_item_input_number, 6),
      (item_set_slot, "itm_trade_oil", slot_item_output_per_run, 2),
      (item_set_slot, "itm_trade_oil", slot_item_overhead_per_run, 80),
      (item_set_slot, "itm_trade_oil", slot_item_base_price, 450),
      (item_set_slot, "itm_trade_oil", slot_item_enterprise_building_cost, 4500),
      
      (item_set_slot, "itm_trade_raw_olives", slot_item_urban_demand, 0),
      (item_set_slot, "itm_trade_raw_olives", slot_item_rural_demand, 0),
      (item_set_slot, "itm_trade_raw_olives", slot_item_desert_demand, 0),
      (item_set_slot, "itm_trade_raw_olives", slot_item_production_slot, slot_center_acres_olives),
      (item_set_slot, "itm_trade_raw_olives", slot_item_production_string, "str_olive_groves"),
      (item_set_slot, "itm_trade_raw_olives", slot_item_is_raw_material_only_for, "itm_trade_oil"),
      (item_set_slot, "itm_trade_raw_olives", slot_item_base_price, 100),
      
      (item_set_slot, "itm_trade_velvet", slot_item_urban_demand, 5),
      (item_set_slot, "itm_trade_velvet", slot_item_rural_demand, 0),
      (item_set_slot, "itm_trade_velvet", slot_item_desert_demand, -1),
      (item_set_slot, "itm_trade_velvet", slot_item_production_slot, slot_center_silk_looms),
      (item_set_slot, "itm_trade_velvet", slot_item_production_string, "str_looms"),
      (item_set_slot, "itm_trade_velvet", slot_item_primary_raw_material, "itm_trade_raw_silk"),
      (item_set_slot, "itm_trade_velvet", slot_item_input_number, 2),
      (item_set_slot, "itm_trade_velvet", slot_item_output_per_run, 2),
      (item_set_slot, "itm_trade_velvet", slot_item_overhead_per_run, 160),
      (item_set_slot, "itm_trade_velvet", slot_item_base_price, 1025),
      (item_set_slot, "itm_trade_velvet", slot_item_secondary_raw_material, "itm_trade_raw_dyes"),
      (item_set_slot, "itm_trade_velvet", slot_item_enterprise_building_cost, 10000),
      
      (item_set_slot, "itm_trade_raw_silk", slot_item_urban_demand, 0),
      (item_set_slot, "itm_trade_raw_silk", slot_item_rural_demand, 0),
      (item_set_slot, "itm_trade_raw_silk", slot_item_production_slot, slot_center_silk_farms),
      (item_set_slot, "itm_trade_raw_silk", slot_item_production_string, "str_mulberry_groves"),
      (item_set_slot, "itm_trade_raw_silk", slot_item_is_raw_material_only_for, "itm_trade_velvet"),
      (item_set_slot, "itm_trade_raw_silk", slot_item_base_price, 600),
      
      (item_set_slot, "itm_trade_raw_dyes", slot_item_urban_demand, 3),
      (item_set_slot, "itm_trade_raw_dyes", slot_item_rural_demand, 0),
      (item_set_slot, "itm_trade_raw_dyes", slot_item_desert_demand, -1),
      (item_set_slot, "itm_trade_raw_dyes", slot_item_production_string, "str_caravans"),
      (item_set_slot, "itm_trade_raw_dyes", slot_item_base_price, 200),
      
      (item_set_slot, "itm_trade_spice", slot_item_urban_demand, 5),
      (item_set_slot, "itm_trade_spice", slot_item_rural_demand, 0),
      (item_set_slot, "itm_trade_spice", slot_item_desert_demand, 5),
      (item_set_slot, "itm_trade_spice", slot_item_production_string, "str_caravans"),
      
      (item_set_slot, "itm_trade_furs", slot_item_urban_demand, 5),
      (item_set_slot, "itm_trade_furs", slot_item_rural_demand, 0),
      (item_set_slot, "itm_trade_furs", slot_item_desert_demand, -1),
      (item_set_slot, "itm_trade_furs", slot_item_production_slot, slot_center_fur_traps),
      (item_set_slot, "itm_trade_furs", slot_item_production_string, "str_traps"),
      
      (item_set_slot, "itm_trade_honey", slot_item_urban_demand, 12),							#	1.143 Port // Increased from 5
      (item_set_slot, "itm_trade_honey", slot_item_rural_demand, 3),							#	1.143 Port // Decreased from 5
      (item_set_slot, "itm_trade_honey", slot_item_desert_demand, -1),							#	1.143 Port // Decreased from 5	
      (item_set_slot, "itm_trade_honey", slot_item_production_slot, slot_center_apiaries),
      (item_set_slot, "itm_trade_honey", slot_item_production_string, "str_hives"),
      
      (item_set_slot, "itm_trade_cabbages", slot_item_urban_demand, 7),
      (item_set_slot, "itm_trade_cabbages", slot_item_rural_demand, 7),
      (item_set_slot, "itm_trade_cabbages", slot_item_desert_demand, 7),
      (item_set_slot, "itm_trade_cabbages", slot_item_production_slot, slot_center_household_gardens),
      (item_set_slot, "itm_trade_cabbages", slot_item_production_string, "str_gardens"),
      
      (item_set_slot, "itm_trade_raw_date_fruit", slot_item_urban_demand, 7),
      (item_set_slot, "itm_trade_raw_date_fruit", slot_item_rural_demand, 7),
      (item_set_slot, "itm_trade_raw_date_fruit", slot_item_desert_demand, 7),
      (item_set_slot, "itm_trade_raw_date_fruit", slot_item_production_slot, slot_center_household_gardens),
      (item_set_slot, "itm_trade_raw_date_fruit", slot_item_production_string, "str_acres_oasis"),
      
      (item_set_slot, "itm_trade_chicken", slot_item_urban_demand, 40),						#	1.143 Port // Newly Added
      (item_set_slot, "itm_trade_chicken", slot_item_rural_demand, 10),
      (item_set_slot, "itm_trade_chicken", slot_item_desert_demand, -1),

      (item_set_slot, "itm_trade_pork", slot_item_urban_demand, 40),
      (item_set_slot, "itm_trade_pork", slot_item_rural_demand, 10),
      (item_set_slot, "itm_trade_pork", slot_item_desert_demand, -1),							#

      # Setting book intelligence requirements
      (item_set_slot, "itm_book_tactics", slot_item_intelligence_requirement, 9),
      (item_set_slot, "itm_book_persuasion", slot_item_intelligence_requirement, 8),
      (item_set_slot, "itm_book_leadership", slot_item_intelligence_requirement, 7),
      (item_set_slot, "itm_book_intelligence", slot_item_intelligence_requirement, 10),
      (item_set_slot, "itm_book_trade", slot_item_intelligence_requirement, 11),
      (item_set_slot, "itm_book_weapon_mastery", slot_item_intelligence_requirement, 9),
      (item_set_slot, "itm_book_engineering", slot_item_intelligence_requirement, 12),
      ## CC
      (item_set_slot, "itm_book_prisoner_management", slot_item_intelligence_requirement, 8),
      (item_set_slot, "itm_book_spotting_reference", slot_item_intelligence_requirement, 10),
      (item_set_slot, "itm_book_first_aid_reference", slot_item_intelligence_requirement, 10),
      (item_set_slot, "itm_book_pathfinding_reference", slot_item_intelligence_requirement, 10),
      ## CC
      (item_set_slot, "itm_book_wound_treatment_reference", slot_item_intelligence_requirement, 10),
      (item_set_slot, "itm_book_training_reference", slot_item_intelligence_requirement, 10),
      (item_set_slot, "itm_book_surgery_reference", slot_item_intelligence_requirement, 10),
      ## Floris: OSP Spak Items
      (item_set_slot, "itm_book_bible", slot_item_intelligence_requirement, 12),
      (item_set_slot, "itm_book_necronomicon", slot_item_intelligence_requirement, 13),
      ##
  ]),
  
  
  ("initialize_town_arena_info",
    [
      (try_for_range, ":town_no", towns_begin, towns_end),
        (party_set_slot, ":town_no", slot_town_tournament_max_teams, 4),
        (party_set_slot, ":town_no", slot_town_tournament_max_team_size, 8),
      (try_end),
      (party_set_slot, "p_town_6", slot_town_tournament_max_team_size, 2),
      
      (party_set_slot,"p_town_1", slot_town_arena_melee_1_num_teams,   2),
      (party_set_slot,"p_town_1", slot_town_arena_melee_1_team_size,   1),
      (party_set_slot,"p_town_1", slot_town_arena_melee_2_num_teams,   4),
      (party_set_slot,"p_town_1", slot_town_arena_melee_2_team_size,   1),
      (party_set_slot,"p_town_1", slot_town_arena_melee_3_num_teams,   4),
      (party_set_slot,"p_town_1", slot_town_arena_melee_3_team_size,   1),
      
      (party_set_slot,"p_town_2", slot_town_arena_melee_1_num_teams,   4),
      (party_set_slot,"p_town_2", slot_town_arena_melee_1_team_size,   4),
      (party_set_slot,"p_town_2", slot_town_arena_melee_2_num_teams,   4),
      (party_set_slot,"p_town_2", slot_town_arena_melee_2_team_size,   6),
      (party_set_slot,"p_town_2", slot_town_arena_melee_3_num_teams,   4),
      (party_set_slot,"p_town_2", slot_town_arena_melee_3_team_size,   8),
      
      (party_set_slot,"p_town_3", slot_town_arena_melee_1_num_teams,   2),
      (party_set_slot,"p_town_3", slot_town_arena_melee_1_team_size,   8),
      (party_set_slot,"p_town_3", slot_town_arena_melee_2_num_teams,   2),
      (party_set_slot,"p_town_3", slot_town_arena_melee_2_team_size,   8),
      (party_set_slot,"p_town_3", slot_town_arena_melee_3_num_teams,   2),
      (party_set_slot,"p_town_3", slot_town_arena_melee_3_team_size,   8),
      
      (party_set_slot,"p_town_4", slot_town_arena_melee_1_num_teams,   2),
      (party_set_slot,"p_town_4", slot_town_arena_melee_1_team_size,   8),
      (party_set_slot,"p_town_4", slot_town_arena_melee_2_num_teams,   3),
      (party_set_slot,"p_town_4", slot_town_arena_melee_2_team_size,   8),
      (party_set_slot,"p_town_4", slot_town_arena_melee_3_num_teams,   2),
      (party_set_slot,"p_town_4", slot_town_arena_melee_3_team_size,   5),
      
      (party_set_slot,"p_town_5", slot_town_arena_melee_1_num_teams,   2),
      (party_set_slot,"p_town_5", slot_town_arena_melee_1_team_size,   3),
      (party_set_slot,"p_town_5", slot_town_arena_melee_2_num_teams,   2),
      (party_set_slot,"p_town_5", slot_town_arena_melee_2_team_size,   5),
      (party_set_slot,"p_town_5", slot_town_arena_melee_3_num_teams,   2),
      (party_set_slot,"p_town_5", slot_town_arena_melee_3_team_size,   8),
      
      (party_set_slot,"p_town_6", slot_town_arena_melee_1_num_teams,   2),
      (party_set_slot,"p_town_6", slot_town_arena_melee_1_team_size,   4),
      (party_set_slot,"p_town_6", slot_town_arena_melee_2_num_teams,   3),
      (party_set_slot,"p_town_6", slot_town_arena_melee_2_team_size,   4),
      (party_set_slot,"p_town_6", slot_town_arena_melee_3_num_teams,   3),
      (party_set_slot,"p_town_6", slot_town_arena_melee_3_team_size,   6),
      
      (party_set_slot,"p_town_7", slot_town_arena_melee_1_num_teams,   4),
      (party_set_slot,"p_town_7", slot_town_arena_melee_1_team_size,   4),
      (party_set_slot,"p_town_7", slot_town_arena_melee_2_num_teams,   4),
      (party_set_slot,"p_town_7", slot_town_arena_melee_2_team_size,   6),
      (party_set_slot,"p_town_7", slot_town_arena_melee_3_num_teams,   4),
      (party_set_slot,"p_town_7", slot_town_arena_melee_3_team_size,   8),
      
      (party_set_slot,"p_town_8", slot_town_arena_melee_1_num_teams,   3),
      (party_set_slot,"p_town_8", slot_town_arena_melee_1_team_size,   1),
      (party_set_slot,"p_town_8", slot_town_arena_melee_2_num_teams,   3),
      (party_set_slot,"p_town_8", slot_town_arena_melee_2_team_size,   3),
      (party_set_slot,"p_town_8", slot_town_arena_melee_3_num_teams,   3),
      (party_set_slot,"p_town_8", slot_town_arena_melee_3_team_size,   7),
      
      (party_set_slot,"p_town_9", slot_town_arena_melee_1_num_teams,   2),
      (party_set_slot,"p_town_9", slot_town_arena_melee_1_team_size,   2),
      (party_set_slot,"p_town_9", slot_town_arena_melee_2_num_teams,   2),
      (party_set_slot,"p_town_9", slot_town_arena_melee_2_team_size,   5),
      (party_set_slot,"p_town_9", slot_town_arena_melee_3_num_teams,   2),
      (party_set_slot,"p_town_9", slot_town_arena_melee_3_team_size,   8),
      
      (party_set_slot,"p_town_10", slot_town_arena_melee_1_num_teams,   2),
      (party_set_slot,"p_town_10", slot_town_arena_melee_1_team_size,   3),
      (party_set_slot,"p_town_10", slot_town_arena_melee_2_num_teams,   2),
      (party_set_slot,"p_town_10", slot_town_arena_melee_2_team_size,   5),
      (party_set_slot,"p_town_10", slot_town_arena_melee_3_num_teams,   2),
      (party_set_slot,"p_town_10", slot_town_arena_melee_3_team_size,   8),
      
      (party_set_slot,"p_town_11", slot_town_arena_melee_1_num_teams,   2),
      (party_set_slot,"p_town_11", slot_town_arena_melee_1_team_size,   8),
      (party_set_slot,"p_town_11", slot_town_arena_melee_2_num_teams,   3),
      (party_set_slot,"p_town_11", slot_town_arena_melee_2_team_size,   4),
      (party_set_slot,"p_town_11", slot_town_arena_melee_3_num_teams,   3),
      (party_set_slot,"p_town_11", slot_town_arena_melee_3_team_size,   6),
      
      (party_set_slot,"p_town_12", slot_town_arena_melee_1_num_teams,   3),
      (party_set_slot,"p_town_12", slot_town_arena_melee_1_team_size,   8),
      (party_set_slot,"p_town_12", slot_town_arena_melee_2_num_teams,   4),
      (party_set_slot,"p_town_12", slot_town_arena_melee_2_team_size,   6),
      (party_set_slot,"p_town_12", slot_town_arena_melee_3_num_teams,   4),
      (party_set_slot,"p_town_12", slot_town_arena_melee_3_team_size,   5),
      
      (party_set_slot,"p_town_13", slot_town_arena_melee_1_num_teams,   2),
      (party_set_slot,"p_town_13", slot_town_arena_melee_1_team_size,   8),
      (party_set_slot,"p_town_13", slot_town_arena_melee_2_num_teams,   4),
      (party_set_slot,"p_town_13", slot_town_arena_melee_2_team_size,   5),
      (party_set_slot,"p_town_13", slot_town_arena_melee_3_num_teams,   4),
      (party_set_slot,"p_town_13", slot_town_arena_melee_3_team_size,   7),
      
      (party_set_slot,"p_town_14", slot_town_arena_melee_1_num_teams,   2),
      (party_set_slot,"p_town_14", slot_town_arena_melee_1_team_size,   4),
      (party_set_slot,"p_town_14", slot_town_arena_melee_2_num_teams,   2),
      (party_set_slot,"p_town_14", slot_town_arena_melee_2_team_size,   5),
      (party_set_slot,"p_town_14", slot_town_arena_melee_3_num_teams,   2),
      (party_set_slot,"p_town_14", slot_town_arena_melee_3_team_size,   6),
      
      (party_set_slot,"p_town_15", slot_town_arena_melee_1_num_teams,   2),
      (party_set_slot,"p_town_15", slot_town_arena_melee_1_team_size,   8),
      (party_set_slot,"p_town_15", slot_town_arena_melee_2_num_teams,   3),
      (party_set_slot,"p_town_15", slot_town_arena_melee_2_team_size,   4),
      (party_set_slot,"p_town_15", slot_town_arena_melee_3_num_teams,   3),
      (party_set_slot,"p_town_15", slot_town_arena_melee_3_team_size,   6),
      
      (party_set_slot,"p_town_16", slot_town_arena_melee_1_num_teams,   3),
      (party_set_slot,"p_town_16", slot_town_arena_melee_1_team_size,   8),
      (party_set_slot,"p_town_16", slot_town_arena_melee_2_num_teams,   4),
      (party_set_slot,"p_town_16", slot_town_arena_melee_2_team_size,   6),
      (party_set_slot,"p_town_16", slot_town_arena_melee_3_num_teams,   4),
      (party_set_slot,"p_town_16", slot_town_arena_melee_3_team_size,   5),
      
      (party_set_slot,"p_town_17", slot_town_arena_melee_1_num_teams,   2),
      (party_set_slot,"p_town_17", slot_town_arena_melee_1_team_size,   8),
      (party_set_slot,"p_town_17", slot_town_arena_melee_2_num_teams,   4),
      (party_set_slot,"p_town_17", slot_town_arena_melee_2_team_size,   5),
      (party_set_slot,"p_town_17", slot_town_arena_melee_3_num_teams,   4),
      (party_set_slot,"p_town_17", slot_town_arena_melee_3_team_size,   7),
      
      (party_set_slot,"p_town_18", slot_town_arena_melee_1_num_teams,   2),
      (party_set_slot,"p_town_18", slot_town_arena_melee_1_team_size,   4),
      (party_set_slot,"p_town_18", slot_town_arena_melee_2_num_teams,   2),
      (party_set_slot,"p_town_18", slot_town_arena_melee_2_team_size,   5),
      (party_set_slot,"p_town_18", slot_town_arena_melee_3_num_teams,   2),
      (party_set_slot,"p_town_18", slot_town_arena_melee_3_team_size,   6),
      
      (party_set_slot,"p_town_19", slot_town_arena_melee_1_num_teams,   2),
      (party_set_slot,"p_town_19", slot_town_arena_melee_1_team_size,   8),
      (party_set_slot,"p_town_19", slot_town_arena_melee_2_num_teams,   4),
      (party_set_slot,"p_town_19", slot_town_arena_melee_2_team_size,   4),
      (party_set_slot,"p_town_19", slot_town_arena_melee_3_num_teams,   4),
      (party_set_slot,"p_town_19", slot_town_arena_melee_3_team_size,   6),
      
      (party_set_slot,"p_town_20", slot_town_arena_melee_1_num_teams,   4),
      (party_set_slot,"p_town_20", slot_town_arena_melee_1_team_size,   2),
      (party_set_slot,"p_town_20", slot_town_arena_melee_2_num_teams,   4),
      (party_set_slot,"p_town_20", slot_town_arena_melee_2_team_size,   4),
      (party_set_slot,"p_town_20", slot_town_arena_melee_3_num_teams,   4),
      (party_set_slot,"p_town_20", slot_town_arena_melee_3_team_size,   6),
      
      (party_set_slot,"p_town_21", slot_town_arena_melee_1_num_teams,   3),
      (party_set_slot,"p_town_21", slot_town_arena_melee_1_team_size,   3),
      (party_set_slot,"p_town_21", slot_town_arena_melee_2_num_teams,   2),
      (party_set_slot,"p_town_21", slot_town_arena_melee_2_team_size,   6),
      (party_set_slot,"p_town_21", slot_town_arena_melee_3_num_teams,   2),
      (party_set_slot,"p_town_21", slot_town_arena_melee_3_team_size,   8),
      
      (party_set_slot,"p_town_22", slot_town_arena_melee_1_num_teams,   4),
      (party_set_slot,"p_town_22", slot_town_arena_melee_1_team_size,   3),
      (party_set_slot,"p_town_22", slot_town_arena_melee_2_num_teams,   3),
      (party_set_slot,"p_town_22", slot_town_arena_melee_2_team_size,   4),
      (party_set_slot,"p_town_22", slot_town_arena_melee_3_num_teams,   2),
      (party_set_slot,"p_town_22", slot_town_arena_melee_3_team_size,   6),
  ]),
  
  ("initialize_banner_info",
    [
      #Banners
      (try_for_range, ":cur_troop", active_npcs_begin, kingdom_ladies_end),
        (troop_set_slot, ":cur_troop", slot_troop_custom_banner_flag_type, -1),
        (troop_set_slot, ":cur_troop", slot_troop_custom_banner_map_flag_type, -1),
      (try_end),
      (troop_set_slot, "trp_player", slot_troop_custom_banner_flag_type, -1),
      (troop_set_slot, "trp_player", slot_troop_custom_banner_map_flag_type, -1),
      (store_random_in_range, "$g_election_date", 0, 45), #setting a random election date
      #Assigning global constant
      #(call_script, "script_store_average_center_value_per_faction"),
      
      (troop_set_slot, "trp_player", slot_troop_custom_banner_bg_color_1, 0xFFFFFFFF),
      (troop_set_slot, "trp_player", slot_troop_custom_banner_bg_color_2, 0xFFFFFFFF),
      (troop_set_slot, "trp_player", slot_troop_custom_banner_charge_color_1, 0xFFFFFFFF),
      (troop_set_slot, "trp_player", slot_troop_custom_banner_charge_color_2, 0xFFFFFFFF),
      (troop_set_slot, "trp_player", slot_troop_custom_banner_charge_color_3, 0xFFFFFFFF),
      (troop_set_slot, "trp_player", slot_troop_custom_banner_charge_color_4, 0xFFFFFFFF),
      
      #Setting background colors for banners
      (troop_set_slot, "trp_banner_background_color_array", 0, 0xFF8f4531),
      (troop_set_slot, "trp_banner_background_color_array", 1, 0xFFd9d7d1),
      (troop_set_slot, "trp_banner_background_color_array", 2, 0xFF373736),
      (troop_set_slot, "trp_banner_background_color_array", 3, 0xFFa48b28),
      (troop_set_slot, "trp_banner_background_color_array", 4, 0xFF497735),
      (troop_set_slot, "trp_banner_background_color_array", 5, 0xFF82362d),
      (troop_set_slot, "trp_banner_background_color_array", 6, 0xFF793329),
      (troop_set_slot, "trp_banner_background_color_array", 7, 0xFF262521),
      (troop_set_slot, "trp_banner_background_color_array", 8, 0xFFd9dad1),
      (troop_set_slot, "trp_banner_background_color_array", 9, 0xFF524563),
      (troop_set_slot, "trp_banner_background_color_array", 10, 0xFF91312c),
      (troop_set_slot, "trp_banner_background_color_array", 11, 0xFFafa231),
      (troop_set_slot, "trp_banner_background_color_array", 12, 0xFF706d3c),
      (troop_set_slot, "trp_banner_background_color_array", 13, 0xFFd6d3ce),
      (troop_set_slot, "trp_banner_background_color_array", 14, 0xFF521c08),
      (troop_set_slot, "trp_banner_background_color_array", 15, 0xFF394584),
      (troop_set_slot, "trp_banner_background_color_array", 16, 0xFF42662e),
      (troop_set_slot, "trp_banner_background_color_array", 17, 0xFFdfded6),
      (troop_set_slot, "trp_banner_background_color_array", 18, 0xFF292724),
      (troop_set_slot, "trp_banner_background_color_array", 19, 0xFF58611b),
      (troop_set_slot, "trp_banner_background_color_array", 20, 0xFF313a67),
      (troop_set_slot, "trp_banner_background_color_array", 21, 0xFF9c924a),
      (troop_set_slot, "trp_banner_background_color_array", 22, 0xFF998b39),
      (troop_set_slot, "trp_banner_background_color_array", 23, 0xFF365168),
      (troop_set_slot, "trp_banner_background_color_array", 24, 0xFFd6d3ce),
      (troop_set_slot, "trp_banner_background_color_array", 25, 0xFF94a642),
      (troop_set_slot, "trp_banner_background_color_array", 26, 0xFF944131),
      (troop_set_slot, "trp_banner_background_color_array", 27, 0xFF893b34),
      (troop_set_slot, "trp_banner_background_color_array", 28, 0xFF425510),
      (troop_set_slot, "trp_banner_background_color_array", 29, 0xFF94452e),
      (troop_set_slot, "trp_banner_background_color_array", 30, 0xFF475a94),
      (troop_set_slot, "trp_banner_background_color_array", 31, 0xFFd1b231),
      (troop_set_slot, "trp_banner_background_color_array", 32, 0xFFe1e2df),
      (troop_set_slot, "trp_banner_background_color_array", 33, 0xFF997c1e),
      (troop_set_slot, "trp_banner_background_color_array", 34, 0xFFc6b74d),
      (troop_set_slot, "trp_banner_background_color_array", 35, 0xFFad9a18),
      (troop_set_slot, "trp_banner_background_color_array", 36, 0xFF212421),
      (troop_set_slot, "trp_banner_background_color_array", 37, 0xFF8c2021),
      (troop_set_slot, "trp_banner_background_color_array", 38, 0xFF4d7136),
      (troop_set_slot, "trp_banner_background_color_array", 39, 0xFF395d84),
      (troop_set_slot, "trp_banner_background_color_array", 40, 0xFF527539),
      (troop_set_slot, "trp_banner_background_color_array", 41, 0xFF9c3c39),
      (troop_set_slot, "trp_banner_background_color_array", 42, 0xFF42518c),
      (troop_set_slot, "trp_banner_background_color_array", 43, 0xFFa46a2c),
      (troop_set_slot, "trp_banner_background_color_array", 44, 0xFF9f5141),
      (troop_set_slot, "trp_banner_background_color_array", 45, 0xFF2c6189),
      (troop_set_slot, "trp_banner_background_color_array", 46, 0xFF556421),
      (troop_set_slot, "trp_banner_background_color_array", 47, 0xFF9d621e),
      (troop_set_slot, "trp_banner_background_color_array", 48, 0xFFdeded6),
      (troop_set_slot, "trp_banner_background_color_array", 49, 0xFF6e4891),
      (troop_set_slot, "trp_banner_background_color_array", 50, 0xFF865a29),
      (troop_set_slot, "trp_banner_background_color_array", 51, 0xFFdedfd9),
      (troop_set_slot, "trp_banner_background_color_array", 52, 0xFF524273),
      (troop_set_slot, "trp_banner_background_color_array", 53, 0xFF8c3821),
      (troop_set_slot, "trp_banner_background_color_array", 54, 0xFFd1cec6),
      (troop_set_slot, "trp_banner_background_color_array", 55, 0xFF313031),
      (troop_set_slot, "trp_banner_background_color_array", 56, 0xFF47620d),
      (troop_set_slot, "trp_banner_background_color_array", 57, 0xFF6b4139),
      (troop_set_slot, "trp_banner_background_color_array", 58, 0xFFd6d7d6),
      (troop_set_slot, "trp_banner_background_color_array", 59, 0xFF2e2f2c),
      (troop_set_slot, "trp_banner_background_color_array", 60, 0xFF604283),
      (troop_set_slot, "trp_banner_background_color_array", 61, 0xFF395584),
      (troop_set_slot, "trp_banner_background_color_array", 62, 0xFF313031),
      (troop_set_slot, "trp_banner_background_color_array", 63, 0xFF7e3f2e),
      (troop_set_slot, "trp_banner_background_color_array", 64, 0xFF343434),
      (troop_set_slot, "trp_banner_background_color_array", 65, 0xFF3c496b),
      (troop_set_slot, "trp_banner_background_color_array", 66, 0xFFd9d8d1),
      (troop_set_slot, "trp_banner_background_color_array", 67, 0xFF99823c),
      (troop_set_slot, "trp_banner_background_color_array", 68, 0xFF9f822e),
      (troop_set_slot, "trp_banner_background_color_array", 69, 0xFF393839),
      (troop_set_slot, "trp_banner_background_color_array", 70, 0xFFa54931),
      (troop_set_slot, "trp_banner_background_color_array", 71, 0xFFdfdcd6),
      (troop_set_slot, "trp_banner_background_color_array", 72, 0xFF9f4a36),
      (troop_set_slot, "trp_banner_background_color_array", 73, 0xFF8c7521),
      (troop_set_slot, "trp_banner_background_color_array", 74, 0xFF9f4631),
      (troop_set_slot, "trp_banner_background_color_array", 75, 0xFF793324),
      (troop_set_slot, "trp_banner_background_color_array", 76, 0xFF395076),
      (troop_set_slot, "trp_banner_background_color_array", 77, 0xFF2c2b2c),
      (troop_set_slot, "trp_banner_background_color_array", 78, 0xFF657121),
      (troop_set_slot, "trp_banner_background_color_array", 79, 0xFF7e3121),
      (troop_set_slot, "trp_banner_background_color_array", 80, 0xFF76512e),
      (troop_set_slot, "trp_banner_background_color_array", 81, 0xFFe7e3de),
      (troop_set_slot, "trp_banner_background_color_array", 82, 0xFF947921),
      (troop_set_slot, "trp_banner_background_color_array", 83, 0xFF4d7b7c),
      (troop_set_slot, "trp_banner_background_color_array", 84, 0xFF343331),
      (troop_set_slot, "trp_banner_background_color_array", 85, 0xFFa74d36),
      (troop_set_slot, "trp_banner_background_color_array", 86, 0xFFe7e3de),
      (troop_set_slot, "trp_banner_background_color_array", 87, 0xFFd6d8ce),
      (troop_set_slot, "trp_banner_background_color_array", 88, 0xFF3e4d67),
      (troop_set_slot, "trp_banner_background_color_array", 89, 0xFF9f842e),
      (troop_set_slot, "trp_banner_background_color_array", 90, 0xFF4d6994),
      (troop_set_slot, "trp_banner_background_color_array", 91, 0xFF4a6118),
      (troop_set_slot, "trp_banner_background_color_array", 92, 0xFF943c29),
      (troop_set_slot, "trp_banner_background_color_array", 93, 0xFF394479),
      (troop_set_slot, "trp_banner_background_color_array", 94, 0xFF343331),
      (troop_set_slot, "trp_banner_background_color_array", 95, 0xFF3f4d5d),
      (troop_set_slot, "trp_banner_background_color_array", 96, 0xFF4a6489),
      (troop_set_slot, "trp_banner_background_color_array", 97, 0xFF313031),
      (troop_set_slot, "trp_banner_background_color_array", 98, 0xFFd6d7ce),
      (troop_set_slot, "trp_banner_background_color_array", 99, 0xFFc69e00),
      (troop_set_slot, "trp_banner_background_color_array", 100, 0xFF638e52),
      (troop_set_slot, "trp_banner_background_color_array", 101, 0xFFdcdbd3),
      (troop_set_slot, "trp_banner_background_color_array", 102, 0xFFdbdcd3),
      (troop_set_slot, "trp_banner_background_color_array", 103, 0xFF843831),
      (troop_set_slot, "trp_banner_background_color_array", 104, 0xFFcecfc6),
      (troop_set_slot, "trp_banner_background_color_array", 105, 0xFFc39d31),
      (troop_set_slot, "trp_banner_background_color_array", 106, 0xFFcbb670),
      (troop_set_slot, "trp_banner_background_color_array", 107, 0xFF394a18),
      (troop_set_slot, "trp_banner_background_color_array", 108, 0xFF372708),
      (troop_set_slot, "trp_banner_background_color_array", 109, 0xFF9a6810),
      (troop_set_slot, "trp_banner_background_color_array", 110, 0xFFb27910),
      (troop_set_slot, "trp_banner_background_color_array", 111, 0xFF8c8621),
      (troop_set_slot, "trp_banner_background_color_array", 112, 0xFF975a03),
      (troop_set_slot, "trp_banner_background_color_array", 113, 0xFF2c2924),
      (troop_set_slot, "trp_banner_background_color_array", 114, 0xFFaa962c),
      (troop_set_slot, "trp_banner_background_color_array", 115, 0xFFa2822e),
      (troop_set_slot, "trp_banner_background_color_array", 116, 0xFF7b8a8c),
      (troop_set_slot, "trp_banner_background_color_array", 117, 0xFF3c0908),
      (troop_set_slot, "trp_banner_background_color_array", 118, 0xFFFF00FF),
      (troop_set_slot, "trp_banner_background_color_array", 119, 0xFF671e14),
      (troop_set_slot, "trp_banner_background_color_array", 120, 0xFF103042),
      (troop_set_slot, "trp_banner_background_color_array", 121, 0xFF4a4500),
      (troop_set_slot, "trp_banner_background_color_array", 122, 0xFF703324),
      (troop_set_slot, "trp_banner_background_color_array", 123, 0xFF24293c),
      (troop_set_slot, "trp_banner_background_color_array", 124, 0xFF5d6966),
      (troop_set_slot, "trp_banner_background_color_array", 125, 0xFFbd9631),
      (troop_set_slot, "trp_banner_background_color_array", 126, 0xFFc6b26b),
      (troop_set_slot, "trp_banner_background_color_array", 127, 0xFF394918),
      
      #Default banners
      (troop_set_slot, "trp_banner_background_color_array", 128, 0xFF212221),
      (troop_set_slot, "trp_banner_background_color_array", 129, 0xFF212221),
      (troop_set_slot, "trp_banner_background_color_array", 130, 0xFF2E3B10),
      (troop_set_slot, "trp_banner_background_color_array", 131, 0xFF425D7B),
      (troop_set_slot, "trp_banner_background_color_array", 132, 0xFF394608),
  ]),
  
  
  ("initialize_economic_information",																#	1.143 Port // Completely Overhauled - See Native 1.34 for initial values
    [
      #All towns produce tools, pottery, and wool cloth for sale in countryside
      (try_for_range, ":town_no", towns_begin, towns_end),
		(store_random_in_range, ":random_average_20_variation_10", 10, 31), #10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29 or 30
		(party_set_slot, ":town_no", slot_center_wool_looms, ":random_average_20_variation_10"),

		(store_random_in_range, ":random_average_2_variation_1", 1, 4), #1,2 or 3
		(party_set_slot, ":town_no", slot_center_breweries, ":random_average_2_variation_1"),

		(store_random_in_range, ":random_average_5_variation_3", 3, 9), #2,3,4,5,6,7 or 8
		(party_set_slot, ":town_no", slot_center_pottery_kilns, ":random_average_5_variation_3"),

		(store_random_in_range, ":random_average_15_variation_9", 6, 25), #6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23 or 24
		(party_set_slot, ":town_no", slot_center_smithies, ":random_average_15_variation_9"),

		(store_random_in_range, ":random_average_5_variation_3", 3, 9), #2,3,4,5,6,7 or 8
		(party_set_slot, ":town_no", slot_center_mills, ":random_average_5_variation_3"),

		(store_random_in_range, ":random_average_2_variation_1", 1, 4), #1,2 or 3
		(party_set_slot, ":town_no", slot_center_tanneries, ":random_average_2_variation_1"),

		(store_random_in_range, ":random_average_1_variation_1", 0, 3), #0,1 or 2
		(party_set_slot, ":town_no", slot_center_wine_presses, ":random_average_1_variation_1"),

		(store_random_in_range, ":random_average_2_variation_1", 1, 4), #1,2 or 3
		(party_set_slot, ":town_no", slot_center_olive_presses, ":random_average_2_variation_1"),
		
		(store_random_in_range, ":random_average_1000_variation_1000", 0, 2001), #0..2000
		(party_set_slot, ":town_no", slot_center_acres_grain, ":random_average_1000_variation_1000"), #0..2000

		(store_random_in_range, ":random_average_1000_variation_1000", 0, 2001), #0..2000
		(party_set_slot, ":town_no", slot_center_acres_vineyard, ":random_average_1000_variation_1000"), #0..2000
    (try_end),
	  
	#Sargoth (linen, wine)
	(party_set_slot, "p_town_1", slot_center_linen_looms, 15), 		
	(party_set_slot, "p_town_1", slot_center_wine_presses, 4), 	    
	
	#Tihr (salt, smoked fish, linen)
	(party_set_slot, "p_town_2", slot_center_salt_pans, 3),
	(party_set_slot, "p_town_2", slot_center_fishing_fleet, 25), 	
	(party_set_slot, "p_town_2", slot_center_linen_looms, 15), 		
	
	#Veluca	(wine, velvet)	
	(party_set_slot, "p_town_3", slot_center_wine_presses, 10), 	
	(party_set_slot, "p_town_3", slot_center_silk_looms, 12), 		
	
	#Suno (velvet, oil)
	(party_set_slot, "p_town_4", slot_center_silk_looms, 12), 		
	(party_set_slot, "p_town_4", slot_center_olive_presses, 15), 	
	
	#Jelkala (velvet, smoked fish)
	(party_set_slot, "p_town_5", slot_center_silk_looms, 24), 		
	(party_set_slot, "p_town_5", slot_center_fishing_fleet, 30), 	

	#Praven (ale, leatherwork, smoked fish)
	(party_set_slot, "p_town_6", slot_center_breweries, 10), 		
	(party_set_slot, "p_town_6", slot_center_tanneries, 4), 	    
	(party_set_slot, "p_town_6", slot_center_fishing_fleet, 10), 	
	
	#Uxkhal (bread, leatherwork, oil)
	(party_set_slot, "p_town_7", slot_center_mills, 15), 			
	(party_set_slot, "p_town_7", slot_center_tanneries, 4), 	    
	(party_set_slot, "p_town_7", slot_center_olive_presses, 5), 	

	#Reyvadin (tools, wool cloth, wine)
	(party_set_slot, "p_town_8", slot_center_smithies, 25), 	    
	(party_set_slot, "p_town_8", slot_center_wool_looms, 35), 	    	
	(party_set_slot, "p_town_8", slot_center_wine_presses, 4), 	    

	#Khudan (tools, leatherwork, smoked fish)
	(party_set_slot, "p_town_9", slot_center_smithies, 18), 	    
	(party_set_slot, "p_town_9", slot_center_tanneries, 3), 	    
	(party_set_slot, "p_town_9", slot_center_fishing_fleet, 5), 	
	
	#Tulga (salt, spice)
	(party_set_slot, "p_town_10", slot_center_salt_pans, 2), 	    
	#also produces 100 spice
	
	#Curaw (tools, iron, smoked fish)
	(party_set_slot, "p_town_11", slot_center_smithies, 19),		
	(party_set_slot, "p_town_11", slot_center_iron_deposits, 10),   
	(party_set_slot, "p_town_11", slot_center_fishing_fleet, 10), 	
	
	#Wercheg (salt, smoked fish)
    (party_set_slot, "p_town_12", slot_center_salt_pans, 3), 		
	(party_set_slot, "p_town_12", slot_center_fishing_fleet, 25), 		

	#Rivacheg (wool cloth, leatherwork, smoked fish)
	(party_set_slot, "p_town_13", slot_center_wool_looms, 30), 	    
	(party_set_slot, "p_town_13", slot_center_tanneries, 5), 	    
	(party_set_slot, "p_town_13", slot_center_fishing_fleet, 20), 	

	#Halmar (leatherwork, pottery)    
	(party_set_slot, "p_town_14", slot_center_tanneries, 3),
	(party_set_slot, "p_town_14", slot_center_pottery_kilns, 18),		 	    
	
	#Yalen (tools, wine, oil, smoked fish)
	(party_set_slot, "p_town_15", slot_center_smithies, 20), 		
	(party_set_slot, "p_town_15", slot_center_wine_presses, 6), 	
	(party_set_slot, "p_town_15", slot_center_olive_presses, 5), 	
	(party_set_slot, "p_town_15", slot_center_fishing_fleet, 25), 	
	
	#Dhirim (tools, leatherwork)
	(party_set_slot, "p_town_16", slot_center_smithies, 30), 		
	(party_set_slot, "p_town_16", slot_center_tanneries, 4), 	    

	#Ichamur (wool cloth, spice)
	(party_set_slot, "p_town_17", slot_center_wool_looms, 40), 	    
	#also produces 50 spice

	#Narra (wool cloth, oil)
	(party_set_slot, "p_town_18", slot_center_wool_looms, 35), 	    
	(party_set_slot, "p_town_18", slot_center_olive_presses, 10), 	
	  
	#Shariz (leatherwork, smoked fish, oil)
	(party_set_slot, "p_town_19", slot_center_tanneries, 5), 	    
	(party_set_slot, "p_town_19", slot_center_breweries, 0), 	    #no alcohol (ale) in arabic region
	(party_set_slot, "p_town_19", slot_center_wine_presses, 0), 	#no alcohol (wine) in arabic region
	(party_set_slot, "p_town_19", slot_center_fishing_fleet, 5), 	
	(party_set_slot, "p_town_19", slot_center_olive_presses, 5), 	
	#also produces 50 spice

	#Darquba (linen, pottery, oil)
	(party_set_slot, "p_town_20", slot_center_breweries, 0), 	    #no alcohol (ale) in arabic region
	(party_set_slot, "p_town_20", slot_center_wine_presses, 0), 	#no alcohol (wine) in arabic region
	(party_set_slot, "p_town_20", slot_center_linen_looms, 15), 
	(party_set_slot, "p_town_20", slot_center_pottery_kilns, 12),	
	(party_set_slot, "p_town_19", slot_center_olive_presses, 3), 		

	#Ahmerrad (pottery, salt)
	(party_set_slot, "p_town_21", slot_center_breweries, 0), 	    #no alcohol (ale) in arabic region
	(party_set_slot, "p_town_21", slot_center_wine_presses, 0), 	#no alcohol (wine) in arabic region
	(party_set_slot, "p_town_21", slot_center_pottery_kilns, 24),	
	(party_set_slot, "p_town_21", slot_center_salt_pans, 1),
	  
	#Bariyye (salt, pottery, spice)	
	(party_set_slot, "p_town_22", slot_center_breweries, 0), 	    #no alcohol (ale) in arabic region
	(party_set_slot, "p_town_22", slot_center_wine_presses, 0), 	#no alcohol (wine) in arabic region	
	(party_set_slot, "p_town_22", slot_center_pottery_kilns, 12),		
	(party_set_slot, "p_town_22", slot_center_salt_pans, 2), 		
	#also produces 50 spice
	
    (try_for_range, ":village_no", villages_begin, villages_end),
      (try_begin),
	    (this_or_next|eq, ":village_no", "p_village_93"), #mazigh
		(this_or_next|eq, ":village_no", "p_village_94"), #sekhtem
		(this_or_next|eq, ":village_no", "p_village_95"), #qalyut
		(this_or_next|eq, ":village_no", "p_village_96"), #tilimsal
		(this_or_next|eq, ":village_no", "p_village_97"), #shibal zumr
		(this_or_next|eq, ":village_no", "p_village_102"), #tamnuh
		(this_or_next|eq, ":village_no", "p_village_109"), #habba
		(this_or_next|eq, ":village_no", "p_village_98"), #mawiti
		(this_or_next|eq, ":village_no", "p_village_103"), #mijayet
		(this_or_next|eq, ":village_no", "p_village_105"), #aab
		(this_or_next|eq, ":village_no", "p_village_99"), #fishara
		(this_or_next|eq, ":village_no", "p_village_100"), #iqbayl
		(this_or_next|eq, ":village_no", "p_village_107"), #unriya
		(this_or_next|eq, ":village_no", "p_village_101"), #uzgha
		(this_or_next|eq, ":village_no", "p_village_104"), #tazjunat
        (this_or_next|eq, ":village_no", "p_village_110"), #rushdigh
		(this_or_next|eq, ":village_no", "p_village_108"), #mit nun
		(eq, ":village_no", "p_village_92"), #dhibbain

		(assign, ":village_is_at_desert", 1),
	  (else_try),
		(assign, ":village_is_at_desert", 0),
	  (try_end),

      (store_random_in_range, ":random_cattle", 20, 100),
	  (try_begin),
	    (eq, ":village_is_at_desert", 1),
		(val_div, ":random_cattle", 5),
	  (try_end),
      (party_set_slot, ":village_no", slot_center_head_cattle, ":random_cattle"), #average : 50, min : 25, max : 75

      (store_random_in_range, ":random_sheep", 40, 200),
	  (try_begin),
	    (eq, ":village_is_at_desert", 1),
		(val_div, ":random_sheep", 5),
	  (try_end),
      (party_set_slot, ":village_no", slot_center_head_sheep, ":random_sheep"), #average : 100, min : 50, max : 150

	  #grain production
      (store_random_in_range, ":random_value_between_0_and_40000", 0, 40000),
	  (store_random_in_range, ":random_value_between_0_and_average_20000", 0, ":random_value_between_0_and_40000"),
	  (try_begin),
	    (eq, ":village_is_at_desert", 1),
		(val_div, ":random_value_between_0_and_average_20000", 5),
	  (try_end),
	  (party_set_slot, ":village_no", slot_center_acres_grain, ":random_value_between_0_and_average_20000"), #average : 10000, min : 0, max : 40000

      #grape production
	  (store_random_in_range, ":random_value_between_0_and_2000", 0, 2000),
	  (store_random_in_range, ":random_value_between_0_and_average_1000", 0, ":random_value_between_0_and_2000"),
	  (try_begin),
	    (eq, ":village_is_at_desert", 1),
		(val_div, ":random_value_between_0_and_average_1000", 5),
	  (try_end),
	  (party_set_slot, ":village_no", slot_center_acres_vineyard, ":random_value_between_0_and_average_1000"), #average : 500, min : 0, max : 2000
	  
	  #olive production
      (store_random_in_range, ":random_value_between_0_and_2000", 0, 2000),
	  (store_random_in_range, ":random_value_between_0_and_average_1000", 0, ":random_value_between_0_and_2000"),
	  (try_begin),
	    (eq, ":village_is_at_desert", 1),
		(val_div, ":random_value_between_0_and_average_1000", 5),
	  (try_end),
	  (party_set_slot, ":village_no", slot_center_acres_olives, ":random_value_between_0_and_average_1000"), #average : 500, min : 0, max : 2000
	  
	  #honey production
	  (store_random_in_range, ":random_value_between_0_and_3", 0, 3),
	  (try_begin),
	    (eq, ":village_is_at_desert", 1),
		(assign, ":random_value_between_0_and_3", 0), #at desert regions no honey production
	  (try_end),
	  (party_set_slot, ":village_no", slot_center_apiaries, ":random_value_between_0_and_3"), 
	  
	  #cabbage and fruit production
	  (store_random_in_range, ":random_value_between_0_and_5", 0, 5),
	  (try_begin),
	    (eq, ":village_is_at_desert", 1),
		(assign, ":random_value_between_0_and_5", 0), #at desert regions no cabbage and fruit production
	  (try_end),
	  (party_set_slot, ":village_no", slot_center_household_gardens, ":random_value_between_0_and_5"), 

	  #bread production
      (store_random_in_range, ":random_value_between_0_and_3", 0, 3),
	  (party_set_slot, ":village_no", slot_center_mills, ":random_value_between_0_and_3"),
	  
	  #pottery production
	  (store_random_in_range, ":random_value_between_0_and_5", 0, 5),
	  (try_begin),
	    (eq, ":village_is_at_desert", 1),
		(val_mul, ":random_value_between_0_and_5", 5), #at desert regions pottery production 4x more than normal (totally 5x)
	  (try_end),
	  (party_set_slot, ":village_no", slot_center_pottery_kilns, ":random_value_between_0_and_5"),
	  
	  #Sargoth (village productions : Ambean, Fearichen and Fenada)
	  (try_begin),
	    (party_slot_eq, ":village_no", slot_village_market_town, "p_town_1"), 
		(party_set_slot, ":village_no", slot_center_acres_flax, 4000),
		(party_set_slot, ":village_no", slot_center_acres_vineyard, 8000),
		
	  #Tihr (village productions : Kulum, Haen and Aldelen)
	  (else_try),
	    (party_slot_eq, ":village_no", slot_village_market_town, "p_town_2"), 
		(party_set_slot, ":village_no", slot_center_acres_vineyard, 8000),
		(party_set_slot, ":village_no", slot_center_household_gardens, 10),
		
	  #Veluca (village productions : Emer, Fedner, Chaeza and Sarimish)
	  (else_try),	
	    (party_slot_eq, ":village_no", slot_village_market_town, "p_town_3"), 
		(party_set_slot, ":village_no", slot_center_acres_vineyard, 6000),
		(party_set_slot, ":village_no", slot_center_acres_olives, 6000),		
		
	  #Suno (village productions : Ruluns and Lyindah)
	  (else_try),
	    (party_slot_eq, ":village_no", slot_village_market_town, "p_town_4"), 			
		(party_set_slot, ":village_no", slot_center_fur_traps, 2),
		(party_set_slot, ":village_no", slot_center_acres_olives, 8000),
	  
	  #Jelkala (village productions : Buvran, Ruldi and Chelez)
	  (else_try),
	    (party_slot_eq, ":village_no", slot_village_market_town, "p_town_5"), 
		(party_set_slot, ":village_no", slot_center_silk_farms, 1500),
		(party_set_slot, ":village_no", slot_center_kirmiz_farms, 1500),
		
	  #Praven (village productions : Azgad, Veidar, Elberl and Gisim)
	  (else_try),
	    (party_slot_eq, ":village_no", slot_village_market_town, "p_town_6"), 			
		(party_set_slot, ":village_no", slot_center_acres_flax, 4000),
		(party_set_slot, ":village_no", slot_center_breweries, 4),
		
	  #Uxkhal (village productions : Nomar, Ibiran and Tahlberl)
	  (else_try),
	    (party_slot_eq, ":village_no", slot_village_market_town, "p_town_7"), 			
		(party_set_slot, ":village_no", slot_center_fur_traps, 1),
		(party_set_slot, ":village_no", slot_center_acres_olives, 8000),			
		(party_set_slot, ":village_no", slot_center_apiaries, 8),			
		
      #Reyvadin (village productions : Ulburban and Ayyike)
	  (else_try),
	    (party_slot_eq, ":village_no", slot_village_market_town, "p_town_8"), 
		(party_set_slot, ":village_no", slot_center_fur_traps, 2),
		(party_set_slot, ":village_no", slot_center_head_cattle, 100),			
		(party_set_slot, ":village_no", slot_center_iron_deposits, 6),
		
      #Khudan (village productions : Uslum, Shulus and Tismirr)
	  (else_try),
	    (party_slot_eq, ":village_no", slot_village_market_town, "p_town_9"), 
		(party_set_slot, ":village_no", slot_center_fur_traps, 2),			
		(party_set_slot, ":village_no", slot_center_acres_olives, 4000),
	
      #Tulga (village productions : Dusturil and Dashbigha)
	  (else_try),
	    (party_slot_eq, ":village_no", slot_village_market_town, "p_town_10"), 
		(party_set_slot, ":village_no", slot_center_head_sheep, 150),			
		(party_set_slot, ":village_no", slot_center_salt_pans, 1),
		(party_set_slot, ":village_no", slot_center_fur_traps, 1),
		(party_set_slot, ":village_no", slot_center_apiaries, 8),
		
      #Curaw (village productions : Bazeck and Rebache)
	  (else_try),
	    (party_slot_eq, ":village_no", slot_village_market_town, "p_town_11"), 
		(party_set_slot, ":village_no", slot_center_iron_deposits, 6),
		(party_set_slot, ":village_no", slot_center_fur_traps, 2),			
		
      #Wercheg (village productions : Ruvar and Odasan)
	  (else_try),
	    (party_slot_eq, ":village_no", slot_village_market_town, "p_town_12"), 
		(party_set_slot, ":village_no", slot_center_acres_vineyard, 8000),
		(party_set_slot, ":village_no", slot_center_household_gardens, 10),
		(party_set_slot, ":village_no", slot_center_salt_pans, 1),

      #Rivacheg (village productions : Shapeshte, Vezin and Fisdnar)
	  (else_try),
	    (party_slot_eq, ":village_no", slot_village_market_town, "p_town_13"), 
		(party_set_slot, ":village_no", slot_center_fur_traps, 2),
		(party_set_slot, ":village_no", slot_center_head_cattle, 100),			
		(party_set_slot, ":village_no", slot_center_silk_farms, 1500),
		
      #Halmar (village productions : Peshmi)
	  (else_try),
	    (party_slot_eq, ":village_no", slot_village_market_town, "p_town_14"), 
		(party_set_slot, ":village_no", slot_center_acres_grain, 40000),		
		(party_set_slot, ":village_no", slot_center_mills, 5),
		
      #Yalen (village productions : Ilvia, Glunmar, Epeshe and Istiniar)
	  (else_try),
	    (party_slot_eq, ":village_no", slot_village_market_town, "p_town_15"), 
		(party_set_slot, ":village_no", slot_center_acres_vineyard, 8000),
		(party_set_slot, ":village_no", slot_center_acres_olives, 8000),
		(party_set_slot, ":village_no", slot_center_household_gardens, 10),
			
      #Dhirim (village productions : Burglen, Amere, Ushkuru, Tshibtin and Yalibe)
      (else_try),
        (party_slot_eq, ":village_no", slot_village_market_town, "p_town_16"), 
        (party_set_slot, ":village_no", slot_center_acres_grain, 40000),
        (party_set_slot, ":village_no", slot_center_iron_deposits, 3),
		(party_set_slot, ":village_no", slot_center_mills, 5),

      #Ichamur (village productions : Ada Kulun and Drigh Aban)
      (else_try),
        (party_slot_eq, ":village_no", slot_village_market_town, "p_town_17"), 			
        (party_set_slot, ":village_no", slot_center_acres_grain, 20000),
        (party_set_slot, ":village_no", slot_center_fur_traps, 1),		

      #Narra (village productions : Zagush and Kedelke)
      (else_try),
        (party_slot_eq, ":village_no", slot_village_market_town, "p_town_18"), 
        (party_set_slot, ":village_no", slot_center_acres_grain, 20000),
        (party_set_slot, ":village_no", slot_center_iron_deposits, 3),
		(party_set_slot, ":village_no", slot_center_apiaries, 8),
		(party_set_slot, ":village_no", slot_center_acres_flax, 4000),
			
      #Shariz (village productions : Ayn Assuadi, Dhibbain, Qalyut, Tilimsal and Rushdigh)
      (else_try),
        (party_slot_eq, ":village_no", slot_village_market_town, "p_town_19"), 
        (party_set_slot, ":village_no", slot_center_acres_grain, 6000), #low grain (partially desert)
        (party_set_slot, ":village_no", slot_center_acres_flax, 2000),
        (party_set_slot, ":village_no", slot_center_acres_olives, 3000),
        (party_set_slot, ":village_no", slot_center_acres_dates, 5000),									

      #Durquba (village productions : Tamnuh and Sekhtem)
      (else_try),
        (party_slot_eq, ":village_no", slot_village_market_town, "p_town_20"), 
        (party_set_slot, ":village_no", slot_center_acres_grain, 3000), #low grain (heavy desert)
        (party_set_slot, ":village_no", slot_center_acres_dates, 10000),
        (party_set_slot, ":village_no", slot_center_salt_pans, 1),									
			
      #Ahmerrad (village productions : Mawiti, Uzgha and Mijayet)
      (else_try),
        (party_slot_eq, ":village_no", slot_village_market_town, "p_town_21"), 
        (party_set_slot, ":village_no", slot_center_acres_grain, 3000), #low grain (heavy desert)
        (party_set_slot, ":village_no", slot_center_acres_dates, 5000),
		(party_set_slot, ":village_no", slot_center_kirmiz_farms, 1500),

      #Bariyye (village productions : Fishara and Iqbayl)
      (else_try),
        (party_slot_eq, ":village_no", slot_village_market_town, "p_town_22"), 
        (party_set_slot, ":village_no", slot_center_acres_grain, 2000), #low grain (heavy desert)
        (party_set_slot, ":village_no", slot_center_acres_flax, 2000),
        (party_set_slot, ":village_no", slot_center_acres_dates, 10000),
        (party_set_slot, ":village_no", slot_center_salt_pans, 1),
        (party_set_slot, ":village_no", slot_center_kirmiz_farms, 1500),
						
      (try_end),
	(try_end),																								#	1.143 Port //	Economic Overhaul ends here
     
	#determining village productions which are bounded by castle by nearby village productions which are bounded by a town.
	(try_for_range, ":village_no", villages_begin, villages_end),
	  (party_get_slot, ":bound_center", ":village_no", slot_village_bound_center),
	  (is_between, ":bound_center", castles_begin, castles_end),

	  (try_for_range, ":cur_production_source", slot_production_sources_begin, slot_production_sources_end),

		(assign, ":total_averaged_production", 0),
		(try_for_range, ":effected_village_no", villages_begin, villages_end),
		  (party_get_slot, ":bound_center", ":effected_village_no", slot_village_bound_center),
	      (is_between, ":bound_center", towns_begin, towns_end),

		  (store_distance_to_party_from_party, ":dist", ":village_no", ":effected_village_no"),
		  (le, ":dist", 72),
		  
		  (party_get_slot, ":production", ":village_no", ":cur_production_source"),
		  
		  (store_add, ":dist_plus_24", ":dist", 24),
		  (store_mul, ":production_mul_12", ":production", 12),
		  (store_div, ":averaged_production", ":production_mul_12", ":dist_plus_24"), #if close (12/24=1/2) else (12/96=1/8)		  
		  (val_div, ":averaged_production", 2), #if close (1/4) else (1/16)
		  (val_add, ":total_averaged_production", ":averaged_production"),
		(try_end),
		
		(party_set_slot, ":village_no", ":cur_production_source", ":total_averaged_production"),
      (try_end),
	(try_end),
	 
	#Ocean and river villages, new map  	 
      
      (party_set_slot, "p_village_1", slot_center_fishing_fleet, 15), #Yaragar
      (party_set_slot, "p_village_3", slot_center_fishing_fleet, 15), #Azgad
      (party_set_slot, "p_village_5", slot_center_fishing_fleet, 15), #Kulum
      
      (party_set_slot, "p_village_8", slot_center_fishing_fleet, 15), #Haen
      (party_set_slot, "p_village_9", slot_center_fishing_fleet, 15), #Buvran
      
      (party_set_slot, "p_village_20", slot_center_fishing_fleet, 15), #Uslum
      (party_set_slot, "p_village_21", slot_center_fishing_fleet, 15), #Bazeck
      (party_set_slot, "p_village_23", slot_center_fishing_fleet, 15), #Ilvia
      (party_set_slot, "p_village_27", slot_center_fishing_fleet, 15), #Glunmar
      
      (party_set_slot, "p_village_30", slot_center_fishing_fleet, 20), #Ruvar
      (party_set_slot, "p_village_31", slot_center_fishing_fleet, 15), #Ambean
      (party_set_slot, "p_village_35", slot_center_fishing_fleet, 15), #Feacharin
      
      (party_set_slot, "p_village_47", slot_center_fishing_fleet, 15), #Epeshe
      (party_set_slot, "p_village_49", slot_center_fishing_fleet, 15), #Tismirr
      
      (party_set_slot, "p_village_51", slot_center_fishing_fleet, 15), #Jelbegi
      (party_set_slot, "p_village_56", slot_center_fishing_fleet, 15), #Fenada
      
      (party_set_slot, "p_village_66", slot_center_fishing_fleet, 15), #Fisdnar
      #    (party_set_slot, "p_village_67", slot_center_fishing_fleet, 15), #Tebandra
      (party_set_slot, "p_village_68", slot_center_fishing_fleet, 15), #Ibdeles
      (party_set_slot, "p_village_69", slot_center_fishing_fleet, 15), #Kwynn
      
      (party_set_slot, "p_village_77", slot_center_fishing_fleet, 25), #Rizi - Estuary
      (party_set_slot, "p_village_79", slot_center_fishing_fleet, 15), #Istiniar
      
      (party_set_slot, "p_village_81", slot_center_fishing_fleet, 15), #Odasan
      (party_set_slot, "p_village_85", slot_center_fishing_fleet, 15), #Ismirala
      (party_set_slot, "p_village_87", slot_center_fishing_fleet, 15), #Udiniad
      
      (party_set_slot, "p_village_90", slot_center_fishing_fleet, 15), #Jamiche
      
      #   (party_set_slot, "p_village_18", slot_center_fishing_fleet, 20), #Ulburban
      #    (party_set_slot, "p_village_26", slot_center_fishing_fleet, 20), #Pagundur
      #    (party_set_slot, "p_village_36", slot_center_fishing_fleet, 25), #Jayek
      
      #Initialize pastureland
      (try_for_range, ":center", centers_begin, centers_end),
        (party_get_slot, ":head_cattle", ":center", slot_center_head_cattle),
        (party_get_slot, ":head_sheep", ":center", slot_center_head_sheep),
        (store_mul, ":num_acres", ":head_cattle", 4),
        (val_add, ":num_acres", ":head_sheep"),
        (val_add, ":num_acres", ":head_sheep"),
        (val_mul, ":num_acres", 6),
        (val_div, ":num_acres", 5),

		(store_random_in_range, ":random", 60, 150),
		(val_mul, ":num_acres", ":random"),
		(val_div, ":num_acres", 100),

		(party_set_slot, ":center", slot_center_acres_pasture, ":num_acres"),
        
      (try_end),
      
      #Initialize prices based on production, etc
		(try_for_range, ":unused", 0, 3), #15 cycles = 45 days. For a village with -20 production, this should lead to approximate +1000, modified				1.143 Port // Changed 15 to 3, also removed several dupliacte call_scripts
			(call_script, "script_update_trade_good_prices"), #changes prices based on production																				as well as a (call_script, "script_average_trade_good_prices"),
		(try_end),
      
      #Initialize prosperity based on final prices
      (try_for_range, ":center_no", centers_begin, centers_end),
        (neg|is_between, ":center_no", castles_begin, castles_end),
        (store_random_in_range, ":random_prosperity_adder", -10, 10),
        (call_script, "script_get_center_ideal_prosperity", ":center_no"),
        (assign, ":prosperity", reg0),
        (val_add, ":prosperity", ":random_prosperity_adder"),
        (val_clamp, ":prosperity", 0, 100),
        (party_set_slot, ":center_no", slot_town_prosperity, ":prosperity"),
      (try_end),
      
      (call_script, "script_calculate_castle_prosperities_by_using_its_villages"),
  ]),
  
  #script_initialize_all_scene_prop_slots
  # INPUT: arg1 = scene_prop_no
  # OUTPUT: none
  ("initialize_all_scene_prop_slots",
    [
      (call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_6m"),
      (call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_8m"),
      (call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_10m"),
      (call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_12m"),
      (call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_14m"),
      (call_script, "script_initialize_scene_prop_slots", "spr_castle_e_sally_door_a"),
      (call_script, "script_initialize_scene_prop_slots", "spr_castle_f_sally_door_a"),
      (call_script, "script_initialize_scene_prop_slots", "spr_earth_sally_gate_left"),
      (call_script, "script_initialize_scene_prop_slots", "spr_earth_sally_gate_right"),
      (call_script, "script_initialize_scene_prop_slots", "spr_viking_keep_destroy_sally_door_left"),
      (call_script, "script_initialize_scene_prop_slots", "spr_viking_keep_destroy_sally_door_right"),
      (call_script, "script_initialize_scene_prop_slots", "spr_castle_f_door_a"),
      (call_script, "script_initialize_scene_prop_slots", "spr_belfry_a"),
      (call_script, "script_initialize_scene_prop_slots", "spr_belfry_b"),
      (call_script, "script_initialize_scene_prop_slots", "spr_winch_b"),
  ]),
  
  #script_initialize_scene_prop_slots
  # INPUT: arg1 = scene_prop_no
  # OUTPUT: none
  ("initialize_scene_prop_slots",
    [
      (store_script_param, ":scene_prop_no", 1),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", ":scene_prop_no"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", ":scene_prop_no", ":cur_instance"),
        (try_for_range, ":cur_slot", 0, scene_prop_slots_end),
          (scene_prop_set_slot, ":cur_instance_id", ":cur_slot", 0),
        (try_end),
      (try_end),
  ]),
  
  #script_use_item
  # INPUT: arg1 = agent_id, arg2 = instance_id
  # OUTPUT: none
  ("use_item",
    [
      (store_script_param, ":instance_id", 1),
      (store_script_param, ":user_id", 2),
      
      (try_begin),
        (game_in_multiplayer_mode),
        (prop_instance_get_scene_prop_kind, ":scene_prop_id", ":instance_id"),
        (eq, ":scene_prop_id", "spr_winch_b"),
        
        (multiplayer_get_my_player, ":my_player_no"),
        
        (this_or_next|gt, ":my_player_no", 0),
        (neg|multiplayer_is_dedicated_server),
        
        (ge, ":my_player_no", 0),
        (player_get_agent_id, ":my_agent_id", ":my_player_no"),
        (ge, ":my_agent_id", 0),
        (agent_is_active, ":my_agent_id"),
        (agent_get_team, ":my_team_no", ":my_agent_id"),
        (eq, ":my_team_no", 0),
        
        (scene_prop_get_slot, ":opened_or_closed", ":instance_id", scene_prop_open_or_close_slot),
        (ge, ":user_id", 0),
        (agent_is_active, ":user_id"),
        (agent_get_player_id, ":user_player", ":user_id"),
        (str_store_player_username, s7, ":user_player"),
        
        (try_begin),
          (eq, ":opened_or_closed", 0),
          (display_message, "@{s7} opened the gate"),
        (else_try),
          (display_message, "@{s7} closed the gate"),
        (try_end),
      (try_end),
      
      (prop_instance_get_scene_prop_kind, ":scene_prop_id", ":instance_id"),
      
      (try_begin),
        (this_or_next|eq, ":scene_prop_id", "spr_winch_b"),
        (eq, ":scene_prop_id", "spr_winch"),
        (assign, ":effected_object", "spr_portcullis"),
      (else_try),
        (this_or_next|eq, ":scene_prop_id", "spr_door_destructible"),
        (this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_b"),
        (this_or_next|eq, ":scene_prop_id", "spr_castle_e_sally_door_a"),
        (this_or_next|eq, ":scene_prop_id", "spr_castle_f_sally_door_a"),
        (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_left"),
        (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_right"),
        (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),
        (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_right"),
        (this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_a"),
        (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_6m"),
        (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_8m"),
        (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_10m"),
        (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_12m"),
        (eq, ":scene_prop_id", "spr_siege_ladder_move_14m"),
        (assign, ":effected_object", ":scene_prop_id"),
      (try_end),
      
      (assign, ":smallest_dist", -1),
      (prop_instance_get_position, pos0, ":instance_id"),
      (scene_prop_get_num_instances, ":num_instances_of_effected_object", ":effected_object"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_effected_object"),
        (scene_prop_get_instance, ":cur_instance_id", ":effected_object", ":cur_instance"),
        (prop_instance_get_position, pos1, ":cur_instance_id"),
        (get_sq_distance_between_positions, ":dist", pos0, pos1),
        (this_or_next|eq, ":smallest_dist", -1),
        (lt, ":dist", ":smallest_dist"),
        (assign, ":smallest_dist", ":dist"),
        (assign, ":effected_object_instance_id", ":cur_instance_id"),
      (try_end),
      
      (try_begin),
        (ge, ":instance_id", 0),
        (ge, ":smallest_dist", 0),
        
        (try_begin),
          (eq, ":effected_object", "spr_portcullis"),
          (scene_prop_get_slot, ":opened_or_closed", ":instance_id", scene_prop_open_or_close_slot),
          
          (try_begin),
            (eq, ":opened_or_closed", 0), #open gate
            
            (scene_prop_enable_after_time, ":instance_id", 400), #4 seconds
            (try_begin),
              (this_or_next|multiplayer_is_server),
              (neg|game_in_multiplayer_mode),
              (prop_instance_get_position, pos0, ":effected_object_instance_id"),
              (position_move_z, pos0, 375),
              (prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 400),
            (try_end),
            (scene_prop_set_slot, ":instance_id", scene_prop_open_or_close_slot, 1),
            
            (try_begin),
              (eq, ":scene_prop_id", "spr_winch_b"),
              (this_or_next|multiplayer_is_server),
              (neg|game_in_multiplayer_mode),
              (prop_instance_get_position, pos1, ":instance_id"),
              (prop_instance_rotate_to_position, ":instance_id", pos1, 400, 72000),
            (try_end),
          (else_try), #close gate
            (scene_prop_enable_after_time, ":instance_id", 400), #4 seconds
            (try_begin),
              (this_or_next|multiplayer_is_server),
              (neg|game_in_multiplayer_mode),
              (prop_instance_get_position, pos0, ":effected_object_instance_id"),
              (position_move_z, pos0, -375),
              (prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 400),
            (try_end),
            (scene_prop_set_slot, ":instance_id", scene_prop_open_or_close_slot, 0),
            
            (try_begin),
              (eq, ":scene_prop_id", "spr_winch_b"),
              (this_or_next|multiplayer_is_server),
              (neg|game_in_multiplayer_mode),
              (prop_instance_get_position, pos1, ":instance_id"),
              (prop_instance_rotate_to_position, ":instance_id", pos1, 400, -72000),
            (try_end),
          (try_end),
        (else_try),
          (this_or_next|eq, ":effected_object", "spr_siege_ladder_move_6m"),
          (this_or_next|eq, ":effected_object", "spr_siege_ladder_move_8m"),
          (this_or_next|eq, ":effected_object", "spr_siege_ladder_move_10m"),
          (this_or_next|eq, ":effected_object", "spr_siege_ladder_move_12m"),
          (eq, ":effected_object", "spr_siege_ladder_move_14m"),
          
          (try_begin),
            (eq, ":effected_object", "spr_siege_ladder_move_6m"),
            (assign, ":animation_time_drop", 120),
            (assign, ":animation_time_elevate", 240),
          (else_try),
            (eq, ":effected_object", "spr_siege_ladder_move_8m"),
            (assign, ":animation_time_drop", 140),
            (assign, ":animation_time_elevate", 280),
          (else_try),
            (eq, ":effected_object", "spr_siege_ladder_move_10m"),
            (assign, ":animation_time_drop", 160),
            (assign, ":animation_time_elevate", 320),
          (else_try),
            (eq, ":effected_object", "spr_siege_ladder_move_12m"),
            (assign, ":animation_time_drop", 190),
            (assign, ":animation_time_elevate", 360),
          (else_try),
            (eq, ":effected_object", "spr_siege_ladder_move_14m"),
            (assign, ":animation_time_drop", 230),
            (assign, ":animation_time_elevate", 400),
          (try_end),
          
          (scene_prop_get_slot, ":opened_or_closed", ":instance_id", scene_prop_open_or_close_slot),
          
          (try_begin),
            (scene_prop_enable_after_time, ":effected_object_instance_id", ":animation_time_elevate"), #3 seconds in average
            (eq, ":opened_or_closed", 0), #ladder at ground
            (prop_instance_get_starting_position, pos0, ":effected_object_instance_id"),
            (prop_instance_enable_physics, ":effected_object_instance_id", 0),
            (prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 300),
            (scene_prop_set_slot, ":effected_object_instance_id", scene_prop_open_or_close_slot, 1),
          (else_try), #ladder at wall
            (scene_prop_enable_after_time, ":effected_object_instance_id", ":animation_time_drop"), #1.5 seconds in average
            (prop_instance_get_position, pos0, ":instance_id"),
            
            (assign, ":smallest_dist", -1),
            (try_for_range, ":entry_point_no", multi_entry_points_for_usable_items_start, multi_entry_points_for_usable_items_end),
              (entry_point_get_position, pos1, ":entry_point_no"),
              (get_sq_distance_between_positions, ":dist", pos0, pos1),
              (this_or_next|eq, ":smallest_dist", -1),
              (lt, ":dist", ":smallest_dist"),
              (assign, ":smallest_dist", ":dist"),
              (assign, ":nearest_entry_point", ":entry_point_no"),
            (try_end),
            
            (try_begin),
              (ge, ":smallest_dist", 0),
              (lt, ":smallest_dist", 22500), #max 15m distance
              (entry_point_get_position, pos1, ":nearest_entry_point"),
              (position_rotate_x, pos1, -90),
              (scene_prop_set_slot, ":effected_object_instance_id", scene_prop_smoke_effect_done, 0),
              (prop_instance_enable_physics, ":effected_object_instance_id", 0),
              (prop_instance_animate_to_position, ":effected_object_instance_id", pos1, 130),
            (try_end),
            
            (scene_prop_set_slot, ":effected_object_instance_id", scene_prop_open_or_close_slot, 0),
          (try_end),
        (else_try),
          (this_or_next|eq, ":effected_object", "spr_door_destructible"),
          (this_or_next|eq, ":effected_object", "spr_castle_f_door_b"),
          (this_or_next|eq, ":scene_prop_id", "spr_castle_e_sally_door_a"),
          (this_or_next|eq, ":scene_prop_id", "spr_castle_f_sally_door_a"),
          (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_left"),
          (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_right"),
          (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),
          (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_right"),
          (eq, ":scene_prop_id", "spr_castle_f_door_a"),
          
          (assign, ":effected_object_instance_id", ":instance_id"),
          (scene_prop_get_slot, ":opened_or_closed", ":effected_object_instance_id", scene_prop_open_or_close_slot),
          
          (try_begin),
            (eq, ":opened_or_closed", 0),
            
            (prop_instance_get_starting_position, pos0, ":effected_object_instance_id"),
            
            (scene_prop_enable_after_time, ":effected_object_instance_id", 100),
            
            (try_begin),
              (neg|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),
              (neg|eq, ":scene_prop_id", "spr_earth_sally_gate_left"),
              
              (position_rotate_z, pos0, -85),
            (else_try),
              (position_rotate_z, pos0, 85),
            (try_end),
            
            (prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 100),
            
            (scene_prop_set_slot, ":effected_object_instance_id", scene_prop_open_or_close_slot, 1),
          (else_try),
            (prop_instance_get_starting_position, pos0, ":effected_object_instance_id"),
            
            (scene_prop_enable_after_time, ":effected_object_instance_id", 100),
            
            (prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 100),
            
            (scene_prop_set_slot, ":effected_object_instance_id", scene_prop_open_or_close_slot, 0),
          (try_end),
        (try_end),
      (try_end),
  ]),
  
  #script_determine_team_flags
  # INPUT: none
  # OUTPUT: none
  ("determine_team_flags",
    [
      (store_script_param, ":team_no", 1),
      
      (try_begin),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
        
        (try_begin),
          (eq, ":team_no", 0),
          
          (team_get_faction, ":team_faction_no", 0),
          (try_begin),
            (eq, ":team_faction_no", "fac_kingdom_1"),
            (assign, "$team_1_flag_scene_prop", "spr_ctf_flag_kingdom_1"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_2"),
            (assign, "$team_1_flag_scene_prop", "spr_ctf_flag_kingdom_2"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_3"),
            (assign, "$team_1_flag_scene_prop", "spr_ctf_flag_kingdom_3"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_4"),
            (assign, "$team_1_flag_scene_prop", "spr_ctf_flag_kingdom_4"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_5"),
            (assign, "$team_1_flag_scene_prop", "spr_ctf_flag_kingdom_5"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_6"),
            (assign, "$team_1_flag_scene_prop", "spr_ctf_flag_kingdom_6"),
          (try_end),
        (else_try),
          (team_get_faction, ":team_faction_no", 1),
          (try_begin),
            (eq, ":team_faction_no", "fac_kingdom_1"),
            (assign, "$team_2_flag_scene_prop", "spr_ctf_flag_kingdom_1"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_2"),
            (assign, "$team_2_flag_scene_prop", "spr_ctf_flag_kingdom_2"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_3"),
            (assign, "$team_2_flag_scene_prop", "spr_ctf_flag_kingdom_3"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_4"),
            (assign, "$team_2_flag_scene_prop", "spr_ctf_flag_kingdom_4"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_5"),
            (assign, "$team_2_flag_scene_prop", "spr_ctf_flag_kingdom_5"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_6"),
            (assign, "$team_2_flag_scene_prop", "spr_ctf_flag_kingdom_6"),
          (try_end),
          
          (try_begin),
            (eq, "$team_1_flag_scene_prop", "$team_2_flag_scene_prop"),
            (assign, "$team_2_flag_scene_prop", "spr_ctf_flag_kingdom_7"),
          (try_end),
        (try_end),
      (else_try),
        (try_begin),
          (eq, ":team_no", 0),
          
          (team_get_faction, ":team_faction_no", 0),
          (try_begin),
            (eq, ":team_faction_no", "fac_kingdom_1"),
            (assign, "$team_1_flag_scene_prop", "spr_headquarters_flag_swadian"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_2"),
            (assign, "$team_1_flag_scene_prop", "spr_headquarters_flag_vaegir"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_3"),
            (assign, "$team_1_flag_scene_prop", "spr_headquarters_flag_khergit"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_4"),
            (assign, "$team_1_flag_scene_prop", "spr_headquarters_flag_nord"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_5"),
            (assign, "$team_1_flag_scene_prop", "spr_headquarters_flag_rhodok"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_6"),
            (assign, "$team_1_flag_scene_prop", "spr_headquarters_flag_sarranid"),
          (try_end),
        (else_try),
          (team_get_faction, ":team_faction_no", 1),
          (try_begin),
            (eq, ":team_faction_no", "fac_kingdom_1"),
            (assign, "$team_2_flag_scene_prop", "spr_headquarters_flag_swadian"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_2"),
            (assign, "$team_2_flag_scene_prop", "spr_headquarters_flag_vaegir"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_3"),
            (assign, "$team_2_flag_scene_prop", "spr_headquarters_flag_khergit"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_4"),
            (assign, "$team_2_flag_scene_prop", "spr_headquarters_flag_nord"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_5"),
            (assign, "$team_2_flag_scene_prop", "spr_headquarters_flag_rhodok"),
          (else_try),
            (eq, ":team_faction_no", "fac_kingdom_6"),
            (assign, "$team_2_flag_scene_prop", "spr_headquarters_flag_sarranid"),
          (try_end),
          
          (try_begin),
            (eq, "$team_1_flag_scene_prop", "$team_2_flag_scene_prop"),
            (assign, "$team_2_flag_scene_prop", "spr_headquarters_flag_rebel"),
          (try_end),
        (try_end),
      (try_end),
  ]),
  
  
  #script_calculate_flag_move_time
  # INPUT: arg1 = number_of_total_agents_around_flag, arg2 = dist_between_flag_and_its_pole
  # OUTPUT: reg0 = flag move time
  ("calculate_flag_move_time",
    [
      (store_script_param, ":number_of_total_agents_around_flag", 1),
      (store_script_param, ":dist_between_flag_and_its_target", 2),
      
      (try_begin), #(if no one is around flag it again moves to its current owner situation but 5 times slower than normal)
        (eq, ":number_of_total_agents_around_flag", 0),
        (store_mul, reg0, ":dist_between_flag_and_its_target", 2500),#5.00 * 1.00 * (500 stable) = 2000
      (else_try),
        (eq, ":number_of_total_agents_around_flag", 1),
        (store_mul, reg0, ":dist_between_flag_and_its_target", 500), #1.00 * (500 stable) = 500
      (else_try),
        (eq, ":number_of_total_agents_around_flag", 2),
        (store_mul, reg0, ":dist_between_flag_and_its_target", 300), #0.60(0.60) * (500 stable) = 300
      (else_try),
        (eq, ":number_of_total_agents_around_flag", 3),
        (store_mul, reg0, ":dist_between_flag_and_its_target", 195), #0.39(0.60 * 0.65) * (500 stable) = 195
      (else_try),
        (eq, ":number_of_total_agents_around_flag", 4),
        (store_mul, reg0, ":dist_between_flag_and_its_target", 137), #0.273(0.60 * 0.65 * 0.70) * (500 stable) = 136.5 >rounding> 137
      (else_try),
        (eq, ":number_of_total_agents_around_flag", 5),
        (store_mul, reg0, ":dist_between_flag_and_its_target", 102), #0.20475(0.60 * 0.65 * 0.70 * 0.75) * (500 stable) = 102.375 >rounding> 102
      (else_try),
        (eq, ":number_of_total_agents_around_flag", 6),
        (store_mul, reg0, ":dist_between_flag_and_its_target", 82),  #0.1638(0.60 * 0.65 * 0.70 * 0.75 * 0.80) * (500 stable) = 81.9 >rounding> 82
      (else_try),
        (eq, ":number_of_total_agents_around_flag", 7),
        (store_mul, reg0, ":dist_between_flag_and_its_target", 66),  #0.13104(0.60 * 0.65 * 0.70 * 0.75 * 0.80 * 0.85) * (500 stable) = 65.52 >rounding> 66
      (else_try),
        (eq, ":number_of_total_agents_around_flag", 8),
        (store_mul, reg0, ":dist_between_flag_and_its_target", 59),  #0.117936(0.60 * 0.65 * 0.70 * 0.75 * 0.80 * 0.85 * 0.90) * (500 stable) = 58.968 >rounding> 59
      (else_try),
        (store_mul, reg0, ":dist_between_flag_and_its_target", 56),  #0.1120392(0.60 * 0.65 * 0.70 * 0.75 * 0.80 * 0.85 * 0.90 * 0.95) * (500 stable) = 56.0196 >rounding> 56
      (try_end),
      
      (assign, ":number_of_players", 0),
      (get_max_players, ":num_players"),
      (try_for_range, ":cur_player", 0, ":num_players"),
        (player_is_active, ":cur_player"),
        (val_add, ":number_of_players", 1),
      (try_end),
      
      (try_begin),
        (lt, ":number_of_players", 10),
        (val_mul, reg0, 50),
      (else_try),
        (lt, ":number_of_players", 35),
        (store_sub, ":number_of_players_multipication", 35, ":number_of_players"),
        (val_mul, ":number_of_players_multipication", 2),
        (store_sub, ":number_of_players_multipication", 100, ":number_of_players_multipication"),
        (val_mul, reg0, ":number_of_players_multipication"),
      (else_try),
        (val_mul, reg0, 100),
      (try_end),
      
      (try_begin),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
        (val_mul, reg0, 2),
      (try_end),
      
      (val_div, reg0, 10000), #100x for number of players around flag, 100x for number of players in game
  ]),
  
  #script_move_death_mode_flags_down
  # INPUT: none
  # OUTPUT: none
  ("move_death_mode_flags_down",
    [
      (try_begin),
        (scene_prop_get_instance, ":pole_1_id", "spr_headquarters_pole_code_only", 0),
        (prop_instance_get_position, pos0, ":pole_1_id"),
        (position_move_z, pos0, -2000),
        (prop_instance_set_position, ":pole_1_id", pos0),
      (try_end),
      
      (try_begin),
        (scene_prop_get_instance, ":pole_2_id", "spr_headquarters_pole_code_only", 1),
        (prop_instance_get_position, pos1, ":pole_2_id"),
        (position_move_z, pos1, -2000),
        (prop_instance_set_position, ":pole_2_id", pos1),
      (try_end),
      
      (try_begin),
        (scene_prop_get_instance, ":pole_1_id", "spr_headquarters_pole_code_only", 0),
        (prop_instance_get_position, pos0, ":pole_1_id"),
        (scene_prop_get_instance, ":flag_1_id", "$team_1_flag_scene_prop", 0),
        (prop_instance_stop_animating, ":flag_1_id"),
        (position_move_z, pos0, multi_headquarters_flag_initial_height),
        (prop_instance_set_position, ":flag_1_id", pos0),
      (try_end),
      
      (try_begin),
        (scene_prop_get_instance, ":pole_2_id", "spr_headquarters_pole_code_only", 1),
        (prop_instance_get_position, pos1, ":pole_2_id"),
        (scene_prop_get_instance, ":flag_2_id", "$team_2_flag_scene_prop", 0),
        (prop_instance_stop_animating, ":flag_2_id"),
        (position_move_z, pos1, multi_headquarters_flag_initial_height),
        (prop_instance_set_position, ":flag_2_id", pos1),
      (try_end),
  ]),
  
  #script_move_flag
  # INPUT: arg1 = shown_flag_id, arg2 = move time in seconds, pos0 = target position
  # OUTPUT: none
  ("move_flag",
    [
      (store_script_param, ":shown_flag_id", 1),
      (store_script_param, ":shown_flag_move_time", 2),
      
      (try_begin),
        (multiplayer_is_server), #added after auto-animating
        
        (try_begin),
          (eq, ":shown_flag_move_time", 0), #stop
          (prop_instance_stop_animating, ":shown_flag_id"),
        (else_try),
          (prop_instance_animate_to_position, ":shown_flag_id", pos0, ":shown_flag_move_time"),
        (try_end),
      (try_end),
  ]),
  
  #script_move_headquarters_flags
  # INPUT: arg1 = current_owner, arg2 = number_of_agents_around_flag_team_1, arg3 = number_of_agents_around_flag_team_2
  # OUTPUT: none
  ("move_headquarters_flags",
    [
      (store_script_param, ":flag_no", 1),
      (store_script_param, ":number_of_agents_around_flag_team_1", 2),
      (store_script_param, ":number_of_agents_around_flag_team_2", 3),
      
      (store_add, ":cur_flag_slot", multi_data_flag_owner_begin, ":flag_no"),
      (troop_get_slot, ":current_owner", "trp_multiplayer_data", ":cur_flag_slot"),
      
      (scene_prop_get_num_instances, ":num_instances", "spr_headquarters_flag_gray_code_only"),
      (try_begin),
        (assign, ":visibility", 0),
        (lt, ":flag_no", ":num_instances"),
        (scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_gray_code_only", ":flag_no"),
        (scene_prop_get_visibility, ":visibility", ":flag_id"),
      (try_end),
      
      (try_begin),
        (eq, ":visibility", 1),
        (assign, ":shown_flag", 0),
        (assign, ":shown_flag_id", ":flag_id"),
      (else_try),
        (scene_prop_get_num_instances, ":num_instances", "$team_1_flag_scene_prop"),
        (try_begin),
          (assign, ":visibility", 0),
          (lt, ":flag_no", ":num_instances"),
          (scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":flag_no"),
          (scene_prop_get_visibility, ":visibility", ":flag_id"),
        (try_end),
        
        #(scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":flag_no"),
        #(scene_prop_get_visibility, ":visibility", ":flag_id"),
        (try_begin),
          (eq, ":visibility", 1),
          (assign, ":shown_flag", 1),
          (assign, ":shown_flag_id", ":flag_id"),
        (else_try),
          (scene_prop_get_num_instances, ":num_instances", "$team_2_flag_scene_prop"),
          (try_begin),
            (assign, ":visibility", 0),
            (lt, ":flag_no", ":num_instances"),
            (scene_prop_get_instance, ":flag_id", "$team_2_flag_scene_prop", ":flag_no"),
            (scene_prop_get_visibility, ":visibility", ":flag_id"),
          (try_end),
          
          #(scene_prop_get_instance, ":flag_id", "$team_2_flag_scene_prop", ":flag_no"),
          #(scene_prop_get_visibility, ":visibility", ":flag_id"),
          (try_begin),
            (eq, ":visibility", 1),
            (assign, ":shown_flag", 2),
            (assign, ":shown_flag_id", ":flag_id"),
          (try_end),
        (try_end),
      (try_end),
      
      (try_begin),
        (scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":flag_no"),
      (try_end),
      
      (try_begin),
        (eq, ":shown_flag", ":current_owner"), #situation 1 : (current owner is equal shown flag)
        (try_begin),
          (ge, ":number_of_agents_around_flag_team_1", 1),
          (ge, ":number_of_agents_around_flag_team_2", 1),
          (assign, ":flag_movement", 0), #0:stop
        (else_try),
          (eq, ":number_of_agents_around_flag_team_1", 0),
          (eq, ":number_of_agents_around_flag_team_2", 0),
          (assign, ":flag_movement", 1), #1:rise (slow)
        (else_try),
          (try_begin),
            (ge, ":number_of_agents_around_flag_team_1", 1),
            (eq, ":number_of_agents_around_flag_team_2", 0),
            (eq, ":current_owner", 1),
            (assign, ":flag_movement", 1), #1:rise (fast)
          (else_try),
            (eq, ":number_of_agents_around_flag_team_1", 0),
            (ge, ":number_of_agents_around_flag_team_2", 1),
            (eq, ":current_owner", 2),
            (assign, ":flag_movement", 1), #1:rise (fast)
          (else_try),
            (assign, ":flag_movement", -1), #-1:drop (fast)
          (try_end),
        (try_end),
      (else_try), #situation 2 : (current owner is different than shown flag)
        (try_begin),
          (ge, ":number_of_agents_around_flag_team_1", 1),
          (ge, ":number_of_agents_around_flag_team_2", 1),
          (assign, ":flag_movement", 0), #0:stop
        (else_try),
          (eq, ":number_of_agents_around_flag_team_1", 0),
          (eq, ":number_of_agents_around_flag_team_2", 0),
          (assign, ":flag_movement", -1), #-1:drop (slow)
        (else_try),
          (try_begin),
            (ge, ":number_of_agents_around_flag_team_1", 1),
            (eq, ":number_of_agents_around_flag_team_2", 0),
            (try_begin),
              (eq, ":shown_flag", 1),
              (assign, ":flag_movement", 1), #1:rise (fast)
            (else_try),
              (neq, ":current_owner", 1),
              (assign, ":flag_movement", -1), #-1:drop (fast)
            (try_end),
          (else_try),
            (eq, ":number_of_agents_around_flag_team_1", 0),
            (ge, ":number_of_agents_around_flag_team_2", 1),
            (try_begin),
              (eq, ":shown_flag", 2),
              (assign, ":flag_movement", 1), #1:rise (fast)
            (else_try),
              (neq, ":current_owner", 2),
              (assign, ":flag_movement", -1), #-1:drop (fast)
            (try_end),
          (try_end),
        (try_end),
      (try_end),
      
      (store_add, ":number_of_total_agents_around_flag", ":number_of_agents_around_flag_team_1", ":number_of_agents_around_flag_team_2"),
      
      (try_begin),
        (eq, ":flag_movement", 0),
        (assign, reg0, 0),
      (else_try),
        (eq, ":flag_movement", 1),
        (prop_instance_get_position, pos1, ":shown_flag_id"),
        (prop_instance_get_position, pos0, ":pole_id"),
        (position_move_z, pos0, multi_headquarters_pole_height),
        (get_distance_between_positions, ":dist_between_flag_and_its_target", pos0, pos1),
        (call_script, "script_calculate_flag_move_time", ":number_of_total_agents_around_flag", ":dist_between_flag_and_its_target"),
      (else_try),
        (eq, ":flag_movement", -1),
        (prop_instance_get_position, pos1, ":shown_flag_id"),
        (prop_instance_get_position, pos0, ":pole_id"),
        (get_distance_between_positions, ":dist_between_flag_and_its_target", pos0, pos1),
        (call_script, "script_calculate_flag_move_time", ":number_of_total_agents_around_flag", ":dist_between_flag_and_its_target"),
      (try_end),
      
      (call_script, "script_move_flag", ":shown_flag_id", reg0), #pos0 : target position
  ]),
  
  #script_set_num_agents_around_flag
  # INPUT: arg1 = flag_no, arg2 = owner_code
  # OUTPUT: none
  ("set_num_agents_around_flag",
    [
      (store_script_param, ":flag_no", 1),
      (store_script_param, ":current_owner_code", 2),
      
      (store_div, ":number_of_agents_around_flag_team_1", ":current_owner_code", 100),
      (store_mod, ":number_of_agents_around_flag_team_2", ":current_owner_code", 100),
      
      (store_add, ":cur_flag_owner_counts_slot", multi_data_flag_players_around_begin, ":flag_no"),
      (troop_set_slot, "trp_multiplayer_data", ":cur_flag_owner_counts_slot", ":current_owner_code"),
      
      (call_script, "script_move_headquarters_flags", ":flag_no", ":number_of_agents_around_flag_team_1", ":number_of_agents_around_flag_team_2"),
  ]),
  
  #script_change_flag_owner
  # INPUT: arg1 = flag_no, arg2 = owner_code
  # OUTPUT: none
  ("change_flag_owner",
    [
      (store_script_param, ":flag_no", 1),
      (store_script_param, ":owner_code", 2),
      
      (try_begin),
        (lt, ":owner_code", 0),
        (val_add, ":owner_code", 1),
        (val_mul, ":owner_code", -1),
      (try_end),
      
      (store_div, ":owner_team_no", ":owner_code", 100),
      (store_mod, ":shown_flag_no", ":owner_code", 100),
      
      (store_add, ":cur_flag_slot", multi_data_flag_owner_begin, ":flag_no"),
      (troop_get_slot, ":older_owner_team_no", "trp_multiplayer_data", ":cur_flag_slot"),
      
      (store_add, ":cur_flag_slot", multi_data_flag_owner_begin, ":flag_no"),
      (troop_set_slot, "trp_multiplayer_data", ":cur_flag_slot", ":owner_team_no"),
      
      #senchronizing flag positions
      (try_begin),
        #(this_or_next|eq, ":initial_flags", 0), #moved after auto-animating
        (multiplayer_is_server),
        
        (scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":flag_no"),
        (try_begin),
          (eq, ":owner_team_no", 0), #if new owner team is 0 then flags are at bottom
          (neq, ":older_owner_team_no", -1), #clients
          (assign, ":continue", 1),
          (try_begin),
            (multiplayer_is_server),
            (eq, "$g_placing_initial_flags", 1),
            (assign, ":continue", 0),
          (try_end),
          (eq, ":continue", 1),
          (prop_instance_get_position, pos0, ":pole_id"),
          (position_move_z, pos0, multi_headquarters_distance_to_change_flag),
        (else_try),
          (prop_instance_get_position, pos0, ":pole_id"), #if new owner team is not 0 then flags are at top
          (position_move_z, pos0, multi_headquarters_pole_height),
        (try_end),
        
        (scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":flag_no"),
        (prop_instance_stop_animating, ":flag_id"),
        (prop_instance_set_position, ":flag_id", pos0),
        
        (scene_prop_get_instance, ":flag_id", "$team_2_flag_scene_prop", ":flag_no"),
        (prop_instance_stop_animating, ":flag_id"),
        (prop_instance_set_position, ":flag_id", pos0),
        
        (scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_gray_code_only", ":flag_no"),
        (prop_instance_stop_animating, ":flag_id"),
        (prop_instance_set_position, ":flag_id", pos0),
      (try_end),
      
      #setting visibilities of flags
      (try_begin),
        (eq, ":shown_flag_no", 0),
        (scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":flag_no"),
        (scene_prop_set_visibility, ":flag_id", 0),
        (scene_prop_get_instance, ":flag_id", "$team_2_flag_scene_prop", ":flag_no"),
        (scene_prop_set_visibility, ":flag_id", 0),
        (scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_gray_code_only", ":flag_no"),
        (scene_prop_set_visibility, ":flag_id", 1),
      (else_try),
        (eq, ":shown_flag_no", 1),
        (scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":flag_no"),
        (scene_prop_set_visibility, ":flag_id", 1),
        (scene_prop_get_instance, ":flag_id", "$team_2_flag_scene_prop", ":flag_no"),
        (scene_prop_set_visibility, ":flag_id", 0),
        (scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_gray_code_only", ":flag_no"),
        (scene_prop_set_visibility, ":flag_id", 0),
      (else_try),
        (eq, ":shown_flag_no", 2),
        (scene_prop_get_instance, ":flag_id", "$team_1_flag_scene_prop", ":flag_no"),
        (scene_prop_set_visibility, ":flag_id", 0),
        (scene_prop_get_instance, ":flag_id", "$team_2_flag_scene_prop", ":flag_no"),
        (scene_prop_set_visibility, ":flag_id", 1),
        (scene_prop_get_instance, ":flag_id", "spr_headquarters_flag_gray_code_only", ":flag_no"),
        (scene_prop_set_visibility, ":flag_id", 0),
      (try_end),
      
      #other
      (store_add, ":cur_flag_players_around_slot", multi_data_flag_players_around_begin, ":flag_no"),
      (troop_get_slot, ":players_around_code", "trp_multiplayer_data", ":cur_flag_players_around_slot"),
      
      (store_div, ":number_of_agents_around_flag_team_1", ":players_around_code", 100),
      (store_mod, ":number_of_agents_around_flag_team_2", ":players_around_code", 100),
      
      (call_script, "script_move_headquarters_flags", ":flag_no", ":number_of_agents_around_flag_team_1", ":number_of_agents_around_flag_team_2"),
  ]),
  
  #script_move_object_to_nearest_entry_point
  # INPUT: none
  # OUTPUT: none
  ("move_object_to_nearest_entry_point",
    [
      (store_script_param, ":scene_prop_no", 1),
      
      (scene_prop_get_num_instances, ":num_instances", ":scene_prop_no"),
      
      (try_for_range, ":instance_no", 0, ":num_instances"),
        (scene_prop_get_instance, ":instance_id", ":scene_prop_no", ":instance_no"),
        (prop_instance_get_position, pos0, ":instance_id"),
        
        (assign, ":smallest_dist", -1),
        (try_for_range, ":entry_point_no", multi_entry_points_for_usable_items_start, multi_entry_points_for_usable_items_end),
          (entry_point_get_position, pos1, ":entry_point_no"),
          (get_sq_distance_between_positions, ":dist", pos0, pos1),
          (this_or_next|eq, ":smallest_dist", -1),
          (lt, ":dist", ":smallest_dist"),
          (assign, ":smallest_dist", ":dist"),
          (assign, ":nearest_entry_point", ":entry_point_no"),
        (try_end),
        
        (try_begin),
          (ge, ":smallest_dist", 0),
          (lt, ":smallest_dist", 22500), #max 15m distance
          (entry_point_get_position, pos1, ":nearest_entry_point"),
          (position_rotate_x, pos1, -90),
          (prop_instance_animate_to_position, ":instance_id", pos1, 1),
        (try_end),
      (try_end),
  ]),
  
  
  #script_multiplayer_server_on_agent_spawn_common
  # INPUT: arg1 = agent_no
  # OUTPUT: none
  ("multiplayer_server_on_agent_spawn_common",
    [
      (store_script_param, ":agent_no", 1),
      (agent_set_slot, ":agent_no", slot_agent_in_duel_with, -1),
      (try_begin),
        (agent_is_non_player, ":agent_no"),
        (assign, "$g_multiplayer_ready_for_spawning_agent", 1),
      (try_end),
  ]),
  
  #script_multiplayer_server_player_joined_common
  # INPUT: arg1 = player_no
  # OUTPUT: none
  ("multiplayer_server_player_joined_common",
    [
      (store_script_param, ":player_no", 1),
      (try_begin),
        (this_or_next|player_is_active, ":player_no"),
        (eq, ":player_no", 0),
        (call_script, "script_multiplayer_init_player_slots", ":player_no"),
        (store_mission_timer_a, ":player_join_time"),
        (player_set_slot, ":player_no", slot_player_join_time, ":player_join_time"),
        (player_set_slot, ":player_no", slot_player_first_spawn, 1),
        #fight and destroy only
        (player_set_slot, ":player_no", slot_player_damage_given_to_target_1, 0),
        (player_set_slot, ":player_no", slot_player_damage_given_to_target_2, 0),
        #fight and destroy only end
        (try_begin),
          (multiplayer_is_server),
          (assign, ":initial_gold", multi_initial_gold_value),
          (val_mul, ":initial_gold", "$g_multiplayer_initial_gold_multiplier"),
          (val_div, ":initial_gold", 100),
          (player_set_gold, ":player_no", ":initial_gold"),
          (call_script, "script_multiplayer_send_initial_information", ":player_no"),
        (try_end),
      (try_end),
  ]),
  
  #script_multiplayer_server_before_mission_start_common
  # INPUT: none
  # OUTPUT: none
  ("multiplayer_server_before_mission_start_common",
    [
      (try_begin),
        (scene_allows_mounted_units),
        (assign, "$g_horses_are_avaliable", 1),
      (else_try),
        (assign, "$g_horses_are_avaliable", 0),
      (try_end),
      (scene_set_day_time, 15),
      (assign, "$g_multiplayer_mission_end_screen", 0),
      
      (get_max_players, ":num_players"),
      (try_for_range, ":player_no", 0, ":num_players"),
        (player_is_active, ":player_no"),
        (call_script, "script_multiplayer_init_player_slots", ":player_no"),
        (assign, ":initial_gold", multi_initial_gold_value),
        (val_mul, ":initial_gold", "$g_multiplayer_initial_gold_multiplier"),
        (val_div, ":initial_gold", 100),
        (player_set_gold, ":player_no", ":initial_gold"),
        (player_set_slot, ":player_no", slot_player_first_spawn, 1), #not required in siege, bt, fd
      (try_end),
  ]),
  
  #script_multiplayer_server_on_agent_killed_or_wounded_common
  # INPUT: arg1 = dead_agent_no, arg2 = killer_agent_no
  # OUTPUT: none
  ("multiplayer_server_on_agent_killed_or_wounded_common",
    [
      (store_script_param, ":dead_agent_no", 1),
      (store_script_param, ":killer_agent_no", 2),
      
      (call_script, "script_multiplayer_event_agent_killed_or_wounded", ":dead_agent_no", ":killer_agent_no"),
      #adding 1 score points to agent which kills enemy agent at server
      (try_begin),
        (multiplayer_is_server),
        (try_begin), #killing myself because of some reason (friend hit, fall, team change)
          (lt, ":killer_agent_no", 0),
          (ge, ":dead_agent_no", 0),
          (neg|agent_is_non_player, ":dead_agent_no"),
          (agent_get_player_id, ":dead_agent_player_id", ":dead_agent_no"),
          (player_is_active, ":dead_agent_player_id"),
          (player_get_score, ":dead_agent_player_score", ":dead_agent_player_id"),
          (val_add, ":dead_agent_player_score", -1),
          (player_set_score, ":dead_agent_player_id", ":dead_agent_player_score"),
        (else_try), #killing teammate
          (ge, ":killer_agent_no", 0),
          (ge, ":dead_agent_no", 0),
          (agent_get_team, ":killer_team_no", ":killer_agent_no"),
          (agent_get_team, ":dead_team_no", ":dead_agent_no"),
          (eq, ":killer_team_no", ":dead_team_no"),
          (neg|agent_is_non_player, ":killer_agent_no"),
          (agent_get_player_id, ":killer_agent_player_id", ":killer_agent_no"),
          (player_is_active, ":killer_agent_player_id"),
          (player_get_score, ":killer_agent_player_score", ":killer_agent_player_id"),
          (val_add, ":killer_agent_player_score", -1),
          (player_set_score, ":killer_agent_player_id", ":killer_agent_player_score"),
          #(player_get_kill_count, ":killer_agent_player_kill_count", ":killer_agent_player_id"),
          #(val_add, ":killer_agent_player_kill_count", -2),
          #(player_set_kill_count, ":killer_agent_player_id", ":killer_agent_player_kill_count"),
        (else_try), #killing enemy
          (ge, ":killer_agent_no", 0),
          (ge, ":dead_agent_no", 0),
          (agent_is_human, ":dead_agent_no"),
          (agent_is_human, ":killer_agent_no"),
          (try_begin),
            (eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
            (try_begin),
              (eq, "$g_battle_death_mode_started", 1),
              (neq, ":dead_agent_no", ":killer_agent_no"),
              (call_script, "script_calculate_new_death_waiting_time_at_death_mod"),
            (try_end),
          (try_end),
          (try_begin),
            (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
            (eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
            (agent_get_player_id, ":dead_player_no", ":dead_agent_no"),
            (try_begin),
              (ge, ":dead_player_no", 0),
              (player_is_active, ":dead_player_no"),
              (neg|agent_is_non_player, ":dead_agent_no"),
              (try_for_agents, ":cur_agent"),
                (agent_is_non_player, ":cur_agent"),
                (agent_is_human, ":cur_agent"),
                (agent_is_alive, ":cur_agent"),
                (agent_get_group, ":agent_group", ":cur_agent"),
                (try_begin),
                  (eq, ":dead_player_no", ":agent_group"),
                  (agent_set_group, ":cur_agent", -1),
                (try_end),
              (try_end),
            (try_end),
          (try_end),
          (neg|agent_is_non_player, ":killer_agent_no"),
          (agent_get_player_id, ":killer_agent_player_id", ":killer_agent_no"),
          (player_is_active, ":killer_agent_player_id"),
          (player_get_score, ":killer_agent_player_score", ":killer_agent_player_id"),
          (agent_get_team, ":killer_agent_team", ":killer_agent_no"),
          (agent_get_team, ":dead_agent_team", ":dead_agent_no"),
          (try_begin),
            (neq, ":killer_agent_team", ":dead_agent_team"),
            (val_add, ":killer_agent_player_score", 1),
          (else_try),
            (val_add, ":killer_agent_player_score", -1),
          (try_end),
          (player_set_score, ":killer_agent_player_id", ":killer_agent_player_score"),
        (try_end),
      (try_end),
      
      (call_script, "script_add_kill_death_counts", ":killer_agent_no", ":dead_agent_no"),
      #money management
      (call_script, "script_money_management_after_agent_death", ":killer_agent_no", ":dead_agent_no"),
  ]),
  
  #script_multiplayer_close_gate_if_it_is_open
  # INPUT: none
  # OUTPUT: none
  ("multiplayer_close_gate_if_it_is_open",
    [
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_winch_b"),
      (try_for_range, ":cur_prop_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":prop_instance_id", "spr_winch_b", ":cur_prop_instance"),
        (scene_prop_slot_eq, ":prop_instance_id", scene_prop_open_or_close_slot, 1),
        (scene_prop_get_instance, ":effected_object_instance_id", "spr_portcullis", ":cur_prop_instance"),
        (prop_instance_get_starting_position, pos0, ":effected_object_instance_id"),
        (prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 1),
      (try_end),
  ]),
  
  #script_multiplayer_move_moveable_objects_initial_positions
  # INPUT: none
  # OUTPUT: none
  ("multiplayer_move_moveable_objects_initial_positions",
    [
      (call_script, "script_move_object_to_nearest_entry_point", "spr_siege_ladder_move_6m"),
      (call_script, "script_move_object_to_nearest_entry_point", "spr_siege_ladder_move_8m"),
      (call_script, "script_move_object_to_nearest_entry_point", "spr_siege_ladder_move_10m"),
      (call_script, "script_move_object_to_nearest_entry_point", "spr_siege_ladder_move_12m"),
      (call_script, "script_move_object_to_nearest_entry_point", "spr_siege_ladder_move_14m"),
  ]),
  
  #script_move_belfries_to_their_first_entry_point
  # INPUT: none
  # OUTPUT: none
  ("move_belfries_to_their_first_entry_point",
    [
      (store_script_param, ":belfry_body_scene_prop", 1),
      
      (set_fixed_point_multiplier, 100),
      (scene_prop_get_num_instances, ":num_belfries", ":belfry_body_scene_prop"),
      
      (try_for_range, ":belfry_no", 0, ":num_belfries"),
        #belfry
        (scene_prop_get_instance, ":belfry_scene_prop_id", ":belfry_body_scene_prop", ":belfry_no"),
        (prop_instance_get_position, pos0, ":belfry_scene_prop_id"),
        
        (try_begin),
          (eq, ":belfry_body_scene_prop", "spr_belfry_a"),
          #belfry platform_a
          (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_platform_a", ":belfry_no"),
          #belfry platform_b
          (scene_prop_get_instance, ":belfry_platform_b_scene_prop_id", "spr_belfry_platform_b", ":belfry_no"),
        (else_try),
          #belfry platform_a
          (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_b_platform_a", ":belfry_no"),
        (try_end),
        
        #belfry wheel_1
        (store_mul, ":wheel_no", ":belfry_no", 3),
        (try_begin),
          (eq, ":belfry_body_scene_prop", "spr_belfry_b"),
          (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),
          (store_mul, ":number_of_belfry_a_wheels", ":number_of_belfry_a", 3),
          (val_add, ":wheel_no", ":number_of_belfry_a_wheels"),
        (try_end),
        (scene_prop_get_instance, ":belfry_wheel_1_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
        #belfry wheel_2
        (val_add, ":wheel_no", 1),
        (scene_prop_get_instance, ":belfry_wheel_2_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
        #belfry wheel_3
        (val_add, ":wheel_no", 1),
        (scene_prop_get_instance, ":belfry_wheel_3_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
        
        (store_add, ":belfry_first_entry_point_id", 11, ":belfry_no"), #belfry entry points are 110..119 and 120..129 and 130..139
        (try_begin),
          (eq, ":belfry_body_scene_prop", "spr_belfry_b"),
          (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),
          (val_add, ":belfry_first_entry_point_id", ":number_of_belfry_a"),
        (try_end),
        (val_mul, ":belfry_first_entry_point_id", 10),
        (entry_point_get_position, pos1, ":belfry_first_entry_point_id"),
        
        #this code block is taken from module_mission_templates.py (multiplayer_server_check_belfry_movement)
        #up down rotation of belfry's next entry point
        (init_position, pos9),
        (position_set_y, pos9, -500), #go 5.0 meters back
        (position_set_x, pos9, -300), #go 3.0 meters left
        (position_transform_position_to_parent, pos10, pos1, pos9),
        (position_get_distance_to_terrain, ":height_to_terrain_1", pos10), #learn distance between 5 meters back of entry point(pos10) and ground level at left part of belfry
        
        (init_position, pos9),
        (position_set_y, pos9, -500), #go 5.0 meters back
        (position_set_x, pos9, 300), #go 3.0 meters right
        (position_transform_position_to_parent, pos10, pos1, pos9),
        (position_get_distance_to_terrain, ":height_to_terrain_2", pos10), #learn distance between 5 meters back of entry point(pos10) and ground level at right part of belfry
        
        (store_add, ":height_to_terrain", ":height_to_terrain_1", ":height_to_terrain_2"),
        (val_mul, ":height_to_terrain", 100), #because of fixed point multiplier
        
        (store_div, ":rotate_angle_of_next_entry_point", ":height_to_terrain", 24), #if there is 1 meters of distance (100cm) then next target position will rotate by 2 degrees. #ac sonra
        (init_position, pos20),
        (position_rotate_x_floating, pos20, ":rotate_angle_of_next_entry_point"),
        (position_transform_position_to_parent, pos23, pos1, pos20),
        
        #right left rotation of belfry's next entry point
        (init_position, pos9),
        (position_set_x, pos9, -300), #go 3.0 meters left
        (position_transform_position_to_parent, pos10, pos1, pos9), #applying 3.0 meters in -x to position of next entry point target, final result is in pos10
        (position_get_distance_to_terrain, ":height_to_terrain_at_left", pos10), #learn distance between 3.0 meters left of entry point(pos10) and ground level
        (init_position, pos9),
        (position_set_x, pos9, 300), #go 3.0 meters left
        (position_transform_position_to_parent, pos10, pos1, pos9), #applying 3.0 meters in x to position of next entry point target, final result is in pos10
        (position_get_distance_to_terrain, ":height_to_terrain_at_right", pos10), #learn distance between 3.0 meters right of entry point(pos10) and ground level
        (store_sub, ":height_to_terrain_1", ":height_to_terrain_at_left", ":height_to_terrain_at_right"),
        
        (init_position, pos9),
        (position_set_x, pos9, -300), #go 3.0 meters left
        (position_set_y, pos9, -500), #go 5.0 meters forward
        (position_transform_position_to_parent, pos10, pos1, pos9), #applying 3.0 meters in -x to position of next entry point target, final result is in pos10
        (position_get_distance_to_terrain, ":height_to_terrain_at_left", pos10), #learn distance between 3.0 meters left of entry point(pos10) and ground level
        (init_position, pos9),
        (position_set_x, pos9, 300), #go 3.0 meters left
        (position_set_y, pos9, -500), #go 5.0 meters forward
        (position_transform_position_to_parent, pos10, pos1, pos9), #applying 3.0 meters in x to position of next entry point target, final result is in pos10
        (position_get_distance_to_terrain, ":height_to_terrain_at_right", pos10), #learn distance between 3.0 meters right of entry point(pos10) and ground level
        (store_sub, ":height_to_terrain_2", ":height_to_terrain_at_left", ":height_to_terrain_at_right"),
        
        (store_add, ":height_to_terrain", ":height_to_terrain_1", ":height_to_terrain_2"),
        (val_mul, ":height_to_terrain", 100), #100 is because of fixed_point_multiplier
        (store_div, ":rotate_angle_of_next_entry_point", ":height_to_terrain", 24), #if there is 1 meters of distance (100cm) then next target position will rotate by 25 degrees.
        (val_mul, ":rotate_angle_of_next_entry_point", -1),
        
        (init_position, pos20),
        (position_rotate_y_floating, pos20, ":rotate_angle_of_next_entry_point"),
        (position_transform_position_to_parent, pos22, pos23, pos20),
        
        (copy_position, pos1, pos22),
        #end of code block
        
        #belfry
        (prop_instance_stop_animating, ":belfry_scene_prop_id"),
        (prop_instance_set_position, ":belfry_scene_prop_id", pos1),
        
        #belfry platforms
        (try_begin),
          (eq, ":belfry_body_scene_prop", "spr_belfry_a"),
          
          #belfry platform_a
          (prop_instance_get_position, pos6, ":belfry_platform_a_scene_prop_id"),
          (position_transform_position_to_local, pos7, pos0, pos6),
          (position_transform_position_to_parent, pos8, pos1, pos7),
          (try_begin),
            (neg|scene_prop_slot_eq, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 0),
            
            (init_position, pos20),
            (position_rotate_x, pos20, 90),
            (position_transform_position_to_parent, pos8, pos8, pos20),
          (try_end),
          (prop_instance_stop_animating, ":belfry_platform_a_scene_prop_id"),
          (prop_instance_set_position, ":belfry_platform_a_scene_prop_id", pos8),
          #belfry platform_b
          (prop_instance_get_position, pos6, ":belfry_platform_b_scene_prop_id"),
          (position_transform_position_to_local, pos7, pos0, pos6),
          (position_transform_position_to_parent, pos8, pos1, pos7),
          (prop_instance_stop_animating, ":belfry_platform_b_scene_prop_id"),
          (prop_instance_set_position, ":belfry_platform_b_scene_prop_id", pos8),
        (else_try),
          #belfry platform_a
          (prop_instance_get_position, pos6, ":belfry_platform_a_scene_prop_id"),
          (position_transform_position_to_local, pos7, pos0, pos6),
          (position_transform_position_to_parent, pos8, pos1, pos7),
          (try_begin),
            (neg|scene_prop_slot_eq, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 0),
            
            (init_position, pos20),
            (position_rotate_x, pos20, 50),
            (position_transform_position_to_parent, pos8, pos8, pos20),
          (try_end),
          (prop_instance_stop_animating, ":belfry_platform_a_scene_prop_id"),
          (prop_instance_set_position, ":belfry_platform_a_scene_prop_id", pos8),
        (try_end),
        
        #belfry wheel_1
        (store_mul, ":wheel_no", ":belfry_no", 3),
        (try_begin),
          (eq, ":belfry_body_scene_prop", "spr_belfry_b"),
          (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),
          (store_mul, ":number_of_belfry_a_wheels", ":number_of_belfry_a", 3),
          (val_add, ":wheel_no", ":number_of_belfry_a_wheels"),
        (try_end),
        (prop_instance_get_position, pos6, ":belfry_wheel_1_scene_prop_id"),
        (position_transform_position_to_local, pos7, pos0, pos6),
        (position_transform_position_to_parent, pos8, pos1, pos7),
        (prop_instance_stop_animating, ":belfry_wheel_1_scene_prop_id"),
        (prop_instance_set_position, ":belfry_wheel_1_scene_prop_id", pos8),
        #belfry wheel_2
        (prop_instance_get_position, pos6, ":belfry_wheel_2_scene_prop_id"),
        (position_transform_position_to_local, pos7, pos0, pos6),
        (position_transform_position_to_parent, pos8, pos1, pos7),
        (prop_instance_stop_animating, ":belfry_wheel_2_scene_prop_id"),
        (prop_instance_set_position, ":belfry_wheel_2_scene_prop_id", pos8),
        #belfry wheel_3
        (prop_instance_get_position, pos6, ":belfry_wheel_3_scene_prop_id"),
        (position_transform_position_to_local, pos7, pos0, pos6),
        (position_transform_position_to_parent, pos8, pos1, pos7),
        (prop_instance_stop_animating, ":belfry_wheel_3_scene_prop_id"),
        (prop_instance_set_position, ":belfry_wheel_3_scene_prop_id", pos8),
      (try_end),
  ]),
  
  #script_team_set_score
  # INPUT: arg1 = team_no, arg2 = score
  # OUTPUT: none
  ("team_set_score",
    [
      (store_script_param, ":team_no", 1),
      (store_script_param, ":score", 2),
      
      (team_set_score, ":team_no", ":score"),
  ]),
  
  #script_player_set_score
  # INPUT: arg1 = player_no, arg2 = score
  # OUTPUT: none
  ("player_set_score",
    [
      (store_script_param, ":player_no", 1),
      (store_script_param, ":score", 2),
      
      (player_set_score, ":player_no", ":score"),
  ]),
  
  #script_player_set_kill_count
  # INPUT: arg1 = player_no, arg2 = score
  # OUTPUT: none
  ("player_set_kill_count",
    [
      (store_script_param, ":player_no", 1),
      (store_script_param, ":score", 2),
      
      (player_set_kill_count, ":player_no", ":score"),
  ]),
  
  #script_player_set_death_count
  # INPUT: arg1 = player_no, arg2 = score
  # OUTPUT: none
  ("player_set_death_count",
    [
      (store_script_param, ":player_no", 1),
      (store_script_param, ":score", 2),
      
      (player_set_death_count, ":player_no", ":score"),
  ]),
  
  #script_set_attached_scene_prop
  # INPUT: arg1 = agent_id, arg2 = flag_id
  # OUTPUT: none
  ("set_attached_scene_prop",
    [
      (store_script_param, ":agent_id", 1),
      (store_script_param, ":flag_id", 2),
      
      (try_begin), #if current mod is capture the flag and attached scene prop is flag then change flag situation of flag owner team.
        (scene_prop_get_instance, ":red_flag_id", "spr_tutorial_flag_red", 0),
        (scene_prop_get_instance, ":blue_flag_id", "spr_tutorial_flag_blue", 0),
        (assign, ":flag_owner_team", -1),
        (try_begin),
          (ge, ":red_flag_id", 0),
          (eq, ":flag_id", ":red_flag_id"),
          (assign, ":flag_owner_team", 0),
        (else_try),
          (ge, ":blue_flag_id", 0),
          (eq, ":flag_id", ":blue_flag_id"),
          (assign, ":flag_owner_team", 1),
        (try_end),
        (ge, ":flag_owner_team", 0),
        (team_set_slot, ":flag_owner_team", slot_team_flag_situation, 1), #1-stolen flag
      (try_end),
      
      (agent_set_attached_scene_prop, ":agent_id", ":flag_id"),
      (agent_set_attached_scene_prop_x, ":agent_id", 20),
      (agent_set_attached_scene_prop_z, ":agent_id", 50),
  ]),
  
  #script_set_team_flag_situation
  # INPUT: arg1 = team_no, arg2 = score
  # OUTPUT: none
  ("set_team_flag_situation",
    [
      (store_script_param, ":team_no", 1),
      (store_script_param, ":flag_situation", 2),
      
      (team_set_slot, ":team_no", slot_team_flag_situation, ":flag_situation"),
  ]),
  
  #script_start_death_mode
  # INPUT: none
  # OUTPUT: none
  ("start_death_mode",
    [
      (assign, "$g_multiplayer_message_type", multiplayer_message_type_start_death_mode),
      (start_presentation, "prsnt_multiplayer_message_1"),
  ]),
  
  #script_calculate_new_death_waiting_time_at_death_mod
  # INPUT: none
  # OUTPUT: none
  ("calculate_new_death_waiting_time_at_death_mod",
    [
      (assign, ":num_living_players", 0), #count number of living players to find out death wait time
      (try_begin),
        (try_for_agents, ":agent_no"),
          (agent_is_human, ":agent_no"),
          (agent_is_alive, ":agent_no"),
          (val_add, ":num_living_players", 1),
        (try_end),
      (try_end),
      
      (val_add, ":num_living_players", multiplayer_battle_formula_value_a),
      (set_fixed_point_multiplier, 100),
      (store_mul, ":num_living_players", ":num_living_players", 100),
      (store_sqrt, ":sqrt_num_living_players", ":num_living_players"),
      (store_div, "$g_battle_waiting_seconds", multiplayer_battle_formula_value_b, ":sqrt_num_living_players"),
      (store_mission_timer_a, "$g_death_mode_part_1_start_time"),
  ]),
  
  #script_calculate_number_of_targets_destroyed
  # INPUT: none
  # OUTPUT: none
  
  ("calculate_number_of_targets_destroyed",
    [
      (assign, "$g_number_of_targets_destroyed", 0),
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_catapult_destructible"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_catapult_destructible", ":cur_instance"),
        (prop_instance_get_starting_position, pos0, ":cur_instance_id"),
        (prop_instance_get_position, pos1, ":cur_instance_id"),
        (get_sq_distance_between_positions_in_meters, ":dist", pos0, pos1),
        (gt, ":dist", 2), #this can be 0 or 1 too.
        (val_add, "$g_number_of_targets_destroyed", 1),
      (try_end),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_trebuchet_destructible"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_trebuchet_destructible", ":cur_instance"),
        (prop_instance_get_starting_position, pos0, ":cur_instance_id"),
        (prop_instance_get_position, pos1, ":cur_instance_id"),
        (get_sq_distance_between_positions_in_meters, ":dist", pos0, pos1),
        (gt, ":dist", 2), #this can be 0 or 1 too.
        (val_add, "$g_number_of_targets_destroyed", 1),
      (try_end),
  ]),
  
  #script_initialize_objects
  # INPUT: none
  # OUTPUT: none
  ("initialize_objects",
    [
      (assign, ":number_of_players", 0),
      (get_max_players, ":num_players"),
      (try_for_range, ":player_no", 0, ":num_players"),
        (player_is_active, ":player_no"),
        (val_add, ":number_of_players", 1),
      (try_end),
      
      #1 player = (Sqrt(1) - 1) * 200 + 1200 = 1200, 1800 (minimum)
      #4 player = (Sqrt(4) - 1) * 200 + 1200 = 1400, 2100
      #9 player = (Sqrt(9) - 1) * 200 + 1200 = 1600, 2400
      #16 player = (Sqrt(16) - 1) * 200 + 1200 = 1800, 2700 (general used)
      #25 player = (Sqrt(25) - 1) * 200 + 1200 = 2000, 3000 (average)
      #36 player = (Sqrt(36) - 1) * 200 + 1200 = 2200, 3300
      #49 player = (Sqrt(49) - 1) * 200 + 1200 = 2400, 3600
      #64 player = (Sqrt(49) - 1) * 200 + 1200 = 2600, 3900
      
      (set_fixed_point_multiplier, 100),
      (val_mul, ":number_of_players", 100),
      (store_sqrt, ":number_of_players", ":number_of_players"),
      (val_sub, ":number_of_players", 100),
      (val_max, ":number_of_players", 0),
      (store_mul, ":effect_of_number_of_players", ":number_of_players", 2),
      (store_add, ":health_catapult", multi_minimum_target_health, ":effect_of_number_of_players"),
      (store_mul, ":health_trebuchet", ":health_catapult", 15), #trebuchet's health is 1.5x of catapult's
      (val_div, ":health_trebuchet", 10),
      (store_mul, ":health_sally_door", ":health_catapult", 18), #sally door's health is 1.8x of catapult's
      (val_div, ":health_sally_door", 10),
      (store_mul, ":health_sally_door_double", ":health_sally_door", 2),
      
      (assign, "$g_number_of_targets_destroyed", 0),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_catapult_destructible"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_catapult_destructible", ":cur_instance"),
        (prop_instance_get_starting_position, pos0, ":cur_instance_id"),
        (prop_instance_stop_animating, ":cur_instance_id"),
        (prop_instance_set_position, ":cur_instance_id", pos0),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_catapult"),
      (try_end),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_trebuchet_destructible"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_trebuchet_destructible", ":cur_instance"),
        (prop_instance_get_starting_position, pos0, ":cur_instance_id"),
        (prop_instance_stop_animating, ":cur_instance_id"),
        (prop_instance_set_position, ":cur_instance_id", pos0),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_trebuchet"),
      (try_end),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_castle_e_sally_door_a"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_castle_e_sally_door_a", ":cur_instance"),
        (prop_instance_get_starting_position, pos0, ":cur_instance_id"),
        (prop_instance_stop_animating, ":cur_instance_id"),
        (prop_instance_set_position, ":cur_instance_id", pos0),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door"),
      (try_end),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_castle_f_sally_door_a"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_castle_f_sally_door_a", ":cur_instance"),
        (prop_instance_get_starting_position, pos0, ":cur_instance_id"),
        (prop_instance_stop_animating, ":cur_instance_id"),
        (prop_instance_set_position, ":cur_instance_id", pos0),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door"),
      (try_end),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_earth_sally_gate_left"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_earth_sally_gate_left", ":cur_instance"),
        (prop_instance_get_starting_position, pos0, ":cur_instance_id"),
        (prop_instance_stop_animating, ":cur_instance_id"),
        (prop_instance_set_position, ":cur_instance_id", pos0),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door_double"),
      (try_end),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_earth_sally_gate_right"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_earth_sally_gate_right", ":cur_instance"),
        (prop_instance_get_starting_position, pos0, ":cur_instance_id"),
        (prop_instance_stop_animating, ":cur_instance_id"),
        (prop_instance_set_position, ":cur_instance_id", pos0),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door_double"),
      (try_end),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_viking_keep_destroy_sally_door_left"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_viking_keep_destroy_sally_door_left", ":cur_instance"),
        (prop_instance_get_starting_position, pos0, ":cur_instance_id"),
        (prop_instance_stop_animating, ":cur_instance_id"),
        (prop_instance_set_position, ":cur_instance_id", pos0),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door"),
      (try_end),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_viking_keep_destroy_sally_door_right"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_viking_keep_destroy_sally_door_right", ":cur_instance"),
        (prop_instance_get_starting_position, pos0, ":cur_instance_id"),
        (prop_instance_stop_animating, ":cur_instance_id"),
        (prop_instance_set_position, ":cur_instance_id", pos0),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door"),
      (try_end),
      
      (store_div, ":health_sally_door_div_3", ":health_sally_door", 3),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_castle_f_door_a"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_castle_f_door_a", ":cur_instance"),
        (prop_instance_get_starting_position, pos0, ":cur_instance_id"),
        (prop_instance_stop_animating, ":cur_instance_id"),
        (prop_instance_set_position, ":cur_instance_id", pos0),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door_div_3"),
      (try_end),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_castle_f_door_b"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_castle_f_door_b", ":cur_instance"),
        (prop_instance_get_starting_position, pos0, ":cur_instance_id"),
        (prop_instance_stop_animating, ":cur_instance_id"),
        (prop_instance_set_position, ":cur_instance_id", pos0),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door_div_3"),
      (try_end),
  ]),
  
  #script_initialize_objects_clients
  # INPUT: none
  # OUTPUT: none
  ("initialize_objects_clients",
    [
      (assign, ":number_of_players", 0),
      (get_max_players, ":num_players"),
      (try_for_range, ":player_no", 0, ":num_players"),
        (player_is_active, ":player_no"),
        (val_add, ":number_of_players", 1),
      (try_end),
      
      #1 player = (Sqrt(1) - 1) * 200 + 1200 = 1200, 1800 (minimum)
      #4 player = (Sqrt(4) - 1) * 200 + 1200 = 1400, 2100
      #9 player = (Sqrt(9) - 1) * 200 + 1200 = 1600, 2400
      #16 player = (Sqrt(16) - 1) * 200 + 1200 = 1800, 2700 (general used)
      #25 player = (Sqrt(25) - 1) * 200 + 1200 = 2000, 3000 (average)
      #36 player = (Sqrt(36) - 1) * 200 + 1200 = 2200, 3300
      #49 player = (Sqrt(49) - 1) * 200 + 1200 = 2400, 3600
      #64 player = (Sqrt(49) - 1) * 200 + 1200 = 2600, 3900
      
      (set_fixed_point_multiplier, 100),
      (val_mul, ":number_of_players", 100),
      (store_sqrt, ":number_of_players", ":number_of_players"),
      (val_sub, ":number_of_players", 100),
      (val_max, ":number_of_players", 0),
      (store_mul, ":effect_of_number_of_players", ":number_of_players", 2),
      (store_add, ":health_catapult", multi_minimum_target_health, ":effect_of_number_of_players"),
      (store_mul, ":health_trebuchet", ":health_catapult", 15), #trebuchet's health is 1.5x of catapult's
      (val_div, ":health_trebuchet", 10),
      (store_mul, ":health_sally_door", ":health_catapult", 18), #trebuchet's health is 1.8x of trebuchet's
      (val_div, ":health_sally_door", 10),
      (store_mul, ":health_sally_door_double", ":health_sally_door", 2),
      
      (assign, "$g_number_of_targets_destroyed", 0),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_catapult_destructible"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_catapult_destructible", ":cur_instance"),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_catapult"),
      (try_end),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_trebuchet_destructible"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_trebuchet_destructible", ":cur_instance"),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_trebuchet"),
      (try_end),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_castle_e_sally_door_a"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_castle_e_sally_door_a", ":cur_instance"),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door"),
      (try_end),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_castle_f_sally_door_a"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_castle_f_sally_door_a", ":cur_instance"),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door"),
      (try_end),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_earth_sally_gate_left"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_earth_sally_gate_left", ":cur_instance"),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door_double"),
      (try_end),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_earth_sally_gate_right"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_earth_sally_gate_right", ":cur_instance"),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door_double"),
      (try_end),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_viking_keep_destroy_sally_door_left"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_viking_keep_destroy_sally_door_left", ":cur_instance"),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door"),
      (try_end),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_viking_keep_destroy_sally_door_right"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_viking_keep_destroy_sally_door_right", ":cur_instance"),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door"),
      (try_end),
      
      (store_div, ":health_sally_door_div_3", ":health_sally_door", 3),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_castle_f_door_a"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_castle_f_door_a", ":cur_instance"),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door_div_3"),
      (try_end),
      
      (scene_prop_get_num_instances, ":num_instances_of_scene_prop", "spr_castle_f_door_b"),
      (try_for_range, ":cur_instance", 0, ":num_instances_of_scene_prop"),
        (scene_prop_get_instance, ":cur_instance_id", "spr_castle_f_door_b", ":cur_instance"),
        (prop_instance_enable_physics, ":cur_instance_id", 1),
        (scene_prop_set_hit_points, ":cur_instance_id", ":health_sally_door_div_3"),
      (try_end),
  ]),
  
  #script_show_multiplayer_message
  # INPUT: arg1 = multiplayer_message_type
  # OUTPUT: none
  ("show_multiplayer_message",
    [
      (store_script_param, ":multiplayer_message_type", 1),
      (store_script_param, ":value", 2),
      
      (assign, "$g_multiplayer_message_type", ":multiplayer_message_type"),
      
      (try_begin),
        (eq, ":multiplayer_message_type", multiplayer_message_type_round_result_in_battle_mode),
        (assign, "$g_multiplayer_message_value_1", ":value"),
        (start_presentation, "prsnt_multiplayer_message_1"),
        
        (try_begin), #end of round in clients
          (neg|multiplayer_is_server),
          (assign, "$g_battle_death_mode_started", 0),
        (try_end),
      (else_try),
        (eq, ":multiplayer_message_type", multiplayer_message_type_auto_team_balance_done),
        (assign, "$g_multiplayer_message_value_1", ":value"),
        (start_presentation, "prsnt_multiplayer_message_2"),
        (assign, "$g_team_balance_next_round", 0),
      (else_try),
        (eq, ":multiplayer_message_type", multiplayer_message_type_auto_team_balance_next),
        (assign, "$g_team_balance_next_round", 1),
        (call_script, "script_warn_player_about_auto_team_balance"),
      (else_try),
        (eq, ":multiplayer_message_type", multiplayer_message_type_auto_team_balance_no_need),
        (assign, "$g_team_balance_next_round", 0),
      (else_try),
        (eq, ":multiplayer_message_type", multiplayer_message_type_capture_the_flag_score),
        (assign, "$g_multiplayer_message_value_1", ":value"),
        (start_presentation, "prsnt_multiplayer_message_1"),
      (else_try),
        (eq, ":multiplayer_message_type", multiplayer_message_type_flag_returned_home),
        (assign, "$g_multiplayer_message_value_1", ":value"),
        (start_presentation, "prsnt_multiplayer_message_1"),
      (else_try),
        (eq, ":multiplayer_message_type", multiplayer_message_type_capture_the_flag_stole),
        (assign, "$g_multiplayer_message_value_1", ":value"),
        (start_presentation, "prsnt_multiplayer_message_1"),
      (else_try),
        (eq, ":multiplayer_message_type", multiplayer_message_type_poll_result),
        (assign, "$g_multiplayer_message_value_3", ":value"),
        (start_presentation, "prsnt_multiplayer_message_3"),
      (else_try),
        (eq, ":multiplayer_message_type", multiplayer_message_type_flag_neutralized),
        (assign, "$g_multiplayer_message_value_1", ":value"),
        (start_presentation, "prsnt_multiplayer_message_1"),
      (else_try),
        (eq, ":multiplayer_message_type", multiplayer_message_type_flag_captured),
        (assign, "$g_multiplayer_message_value_1", ":value"),
        (start_presentation, "prsnt_multiplayer_message_1"),
      (else_try),
        (eq, ":multiplayer_message_type", multiplayer_message_type_flag_is_pulling),
        (assign, "$g_multiplayer_message_value_1", ":value"),
        (start_presentation, "prsnt_multiplayer_message_1"),
      (else_try),
        (eq, ":multiplayer_message_type", multiplayer_message_type_round_draw),
        (start_presentation, "prsnt_multiplayer_message_1"),
      (else_try),
        (eq, ":multiplayer_message_type", multiplayer_message_type_target_destroyed),
        
        (try_begin), #destroy score (condition : a target destroyed)
          (eq, "$g_defender_team", 0),
          (assign, ":attacker_team_no", 1),
        (else_try),
          (assign, ":attacker_team_no", 0),
        (try_end),
        
        (team_get_score, ":team_score", ":attacker_team_no"),
        (val_add, ":team_score", 1),
        (call_script, "script_team_set_score", ":attacker_team_no", ":team_score"), #destroy score end
        
        (assign, "$g_multiplayer_message_value_1", ":value"),
        (start_presentation, "prsnt_multiplayer_message_1"),
      (else_try),
        (eq, ":multiplayer_message_type", multiplayer_message_type_defenders_saved_n_targets),
        (assign, "$g_multiplayer_message_value_1", ":value"),
        (start_presentation, "prsnt_multiplayer_message_1"),
      (else_try),
        (eq, ":multiplayer_message_type", multiplayer_message_type_attackers_won_the_round),
        (try_begin),
          (eq, "$g_defender_team", 0),
          (assign, "$g_multiplayer_message_value_1", 1),
        (else_try),
          (assign, "$g_multiplayer_message_value_1", 0),
        (try_end),
        (start_presentation, "prsnt_multiplayer_message_1"),
      (try_end),
  ]),
  
  #script_get_headquarters_scores
  # INPUT: none
  # OUTPUT: reg0 = team_1_num_flags, reg1 = team_2_num_flags
  ("get_headquarters_scores",
    [
      (assign, ":team_1_num_flags", 0),
      (assign, ":team_2_num_flags", 0),
      (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
        (store_add, ":cur_flag_owner_slot", multi_data_flag_owner_begin, ":flag_no"),
        (troop_get_slot, ":cur_flag_owner", "trp_multiplayer_data", ":cur_flag_owner_slot"),
        (neq, ":cur_flag_owner", 0),
        (try_begin),
          (eq, ":cur_flag_owner", 1),
          (val_add, ":team_1_num_flags", 1),
        (else_try),
          (val_add, ":team_2_num_flags", 1),
        (try_end),
      (try_end),
      (assign, reg0, ":team_1_num_flags"),
      (assign, reg1, ":team_2_num_flags"),
  ]),
  
  
  #script_draw_this_round
  # INPUT: arg1 = value
  ("draw_this_round",
    [
      (store_script_param, ":value", 1),
      
      (try_begin),
        (eq, ":value", -9), #destroy mod round end
        (assign, "$g_round_ended", 1),
        (store_mission_timer_a, "$g_round_finish_time"),
        #(assign, "$g_multiplayer_message_value_1", -1),
        #(assign, "$g_multiplayer_message_type", multiplayer_message_type_round_draw),
        #(start_presentation, "prsnt_multiplayer_message_1"),
      (else_try),
        (eq, ":value", -1), #draw
        (assign, "$g_round_ended", 1),
        (store_mission_timer_a, "$g_round_finish_time"),
        (assign, "$g_multiplayer_message_value_1", -1),
        (assign, "$g_multiplayer_message_type", multiplayer_message_type_round_draw),
        (start_presentation, "prsnt_multiplayer_message_1"),
      (else_try),
        (eq, ":value", 0), #defender wins
        #THIS_IS_OUR_LAND achievement
        (try_begin),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
          (multiplayer_get_my_player, ":my_player_no"),
          (is_between, ":my_player_no", 0, multiplayer_max_possible_player_id),
          (player_get_agent_id, ":my_player_agent", ":my_player_no"),
          (ge, ":my_player_agent", 0),
          (agent_is_alive, ":my_player_agent"),
          (agent_get_team, ":my_player_agent_team_no", ":my_player_agent"),
          (eq, ":my_player_agent_team_no", 0), #defender
          (unlock_achievement, ACHIEVEMENT_THIS_IS_OUR_LAND),
        (try_end),
        #THIS_IS_OUR_LAND achievement end
        (assign, "$g_round_ended", 1),
        (store_mission_timer_a, "$g_round_finish_time"),
        
        (team_get_faction, ":faction_of_winner_team", 0),
        (team_get_score, ":team_1_score", 0),
        (val_add, ":team_1_score", 1),
        (team_set_score, 0, ":team_1_score"),
        (assign, "$g_winner_team", 0),
        (str_store_faction_name, s1, ":faction_of_winner_team"),
        
        (assign, "$g_multiplayer_message_value_1", ":value"),
        (try_begin),
          (neq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
          (neq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
          (assign, "$g_multiplayer_message_type", multiplayer_message_type_round_result_in_siege_mode),
        (else_try),
          (assign, "$g_multiplayer_message_type", multiplayer_message_type_round_result_in_battle_mode),
        (try_end),
        (start_presentation, "prsnt_multiplayer_message_1"),
      (else_try),
        (eq, ":value", 1), #attacker wins
        (assign, "$g_round_ended", 1),
        (store_mission_timer_a, "$g_round_finish_time"),
        
        (team_get_faction, ":faction_of_winner_team", 1),
        (team_get_score, ":team_2_score", 1),
        (val_add, ":team_2_score", 1),
        (team_set_score, 1, ":team_2_score"),
        (assign, "$g_winner_team", 1),
        (str_store_faction_name, s1, ":faction_of_winner_team"),
        
        (assign, "$g_multiplayer_message_value_1", ":value"),
        (try_begin),
          (neq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
          (neq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
          (assign, "$g_multiplayer_message_type", multiplayer_message_type_round_result_in_siege_mode),
        (else_try),
          (assign, "$g_multiplayer_message_type", multiplayer_message_type_round_result_in_battle_mode),
        (try_end),
        (start_presentation, "prsnt_multiplayer_message_1"),
      (try_end),
      #LAST_MAN_STANDING achievement
      (try_begin),
        (is_between, ":value", 0, 2), #defender or attacker wins
        (try_begin),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
          (multiplayer_get_my_player, ":my_player_no"),
          (is_between, ":my_player_no", 0, multiplayer_max_possible_player_id),
          (player_get_agent_id, ":my_player_agent", ":my_player_no"),
          (ge, ":my_player_agent", 0),
          (agent_is_alive, ":my_player_agent"),
          (agent_get_team, ":my_player_agent_team_no", ":my_player_agent"),
          (eq, ":my_player_agent_team_no", ":value"), #winner team
          (unlock_achievement, ACHIEVEMENT_LAST_MAN_STANDING),
        (try_end),
      (try_end),
      #LAST_MAN_STANDING achievement end
  ]),
  
  #script_check_achievement_last_man_standing ##1.132, 22 new lines
  #INPUT: arg1 = value
  ("check_achievement_last_man_standing",
    [
      #LAST_MAN_STANDING achievement
      (try_begin),
        (store_script_param, ":value", 1),
        (is_between, ":value", 0, 2), #defender or attacker wins
        (try_begin),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
          (multiplayer_get_my_player, ":my_player_no"),
          (is_between, ":my_player_no", 0, multiplayer_max_possible_player_id),
          (player_get_agent_id, ":my_player_agent", ":my_player_no"),
          (ge, ":my_player_agent", 0),
          (agent_is_alive, ":my_player_agent"),
          (agent_get_team, ":my_player_agent_team_no", ":my_player_agent"),
          (eq, ":my_player_agent_team_no", ":value"), #winner team
          (unlock_achievement, ACHIEVEMENT_LAST_MAN_STANDING),
        (try_end),
      (try_end),
      #LAST_MAN_STANDING achievement end
  ]), ##
  
  #script_find_most_suitable_bot_to_control
  # INPUT: arg1 = value
  ("find_most_suitable_bot_to_control",
    [
      (set_fixed_point_multiplier, 100),
      (store_script_param, ":player_no", 1),
      (player_get_team_no, ":player_team", ":player_no"),
      
      (player_get_slot, ":x_coor", ":player_no", slot_player_death_pos_x),
      (player_get_slot, ":y_coor", ":player_no", slot_player_death_pos_y),
      (player_get_slot, ":z_coor", ":player_no", slot_player_death_pos_z),
      
      (init_position, pos0),
      (position_set_x, pos0, ":x_coor"),
      (position_set_y, pos0, ":y_coor"),
      (position_set_z, pos0, ":z_coor"),
      
      (assign, ":most_suitable_bot", -1),
      (assign, ":max_bot_score", -1),
      
      (try_for_agents, ":cur_agent"),
        (agent_is_alive, ":cur_agent"),
        (agent_is_human, ":cur_agent"),
        (agent_is_non_player, ":cur_agent"),
        (agent_get_team ,":cur_team", ":cur_agent"),
        (eq, ":cur_team", ":player_team"),
        (agent_get_position, pos1, ":cur_agent"),
        
        #getting score for distance of agent to death point (0..3000)
        (get_distance_between_positions_in_meters, ":dist", pos0, pos1),
        
        (try_begin),
          (lt, ":dist", 500),
          (store_sub, ":bot_score", 500, ":dist"),
        (else_try),
          (assign, ":bot_score", 0),
        (try_end),
        (val_mul, ":bot_score", 6),
        
        #getting score for distance of agent to enemy & friend agents (0..300 x agents)
        (try_for_agents, ":cur_agent_2"),
          (agent_is_alive, ":cur_agent_2"),
          (agent_is_human, ":cur_agent_2"),
          (neq, ":cur_agent", ":cur_agent_2"),
          (agent_get_team ,":cur_team_2", ":cur_agent_2"),
          (try_begin),
            (neq, ":cur_team_2", ":player_team"),
            (agent_get_position, pos1, ":cur_agent_2"),
            (get_distance_between_positions, ":dist_2", pos0, pos1),
            (try_begin),
              (lt, ":dist_2", 300),
              (assign, ":enemy_near_score", ":dist_2"),
            (else_try),
              (assign, ":enemy_near_score", 300),
            (try_end),
            (val_add, ":bot_score", ":enemy_near_score"),
          (else_try),
            (agent_get_position, pos1, ":cur_agent_2"),
            (get_distance_between_positions, ":dist_2", pos0, pos1),
            (try_begin),
              (lt, ":dist_2", 300),
              (assign, ":friend_near_score", 300, ":dist_2"),
            (else_try),
              (assign, ":friend_near_score", 0),
            (try_end),
            (val_add, ":bot_score", ":friend_near_score"),
          (try_end),
        (try_end),
        
        #getting score for health (0..200)
        (store_agent_hit_points, ":agent_hit_points", ":cur_agent"),
        (val_mul, ":agent_hit_points", 2),
        (val_add, ":bot_score", ":agent_hit_points"),
        
        (ge, ":bot_score", ":max_bot_score"),
        (assign, ":max_bot_score", ":bot_score"),
        (assign, ":most_suitable_bot", ":cur_agent"),
      (try_end),
      
      (assign, reg0, ":most_suitable_bot"),
  ]),
  
  #script_game_receive_url_response
  #response format should be like this:
  #  [a number or a string]|[another number or a string]|[yet another number or a string] ...
  # here is an example response:
  # 12|Player|100|another string|142|323542|34454|yet another string
  # INPUT: arg1 = num_integers, arg2 = num_strings
  # reg0, reg1, reg2, ... up to 128 registers contain the integer values
  # s0, s1, s2, ... up to 128 strings contain the string values
  ("game_receive_url_response",
    [
      #here is an example usage
      ##      (store_script_param, ":num_integers", 1),
      ##      (store_script_param, ":num_strings", 2),
      ##      (try_begin),
      ##        (gt, ":num_integers", 4),
      ##        (display_message, "@{reg0}, {reg1}, {reg2}, {reg3}, {reg4}"),
      ##      (try_end),
      ##      (try_begin),
      ##        (gt, ":num_strings", 4),
      ##        (display_message, "@{s0}, {s1}, {s2}, {s3}, {s4}"),
      ##      (try_end),
  ]),
  
  ("game_get_cheat_mode",
    [
      (assign, reg0, "$cheat_mode"),
  ]),
  
  #script_game_receive_network_message
  # This script is called from the game engine when a new network message is received.
  # INPUT: arg1 = player_no, arg2 = event_type, arg3 = value, arg4 = value_2, arg5 = value_3, arg6 = value_4
  ("game_receive_network_message",
    [
      (store_script_param, ":player_no", 1),
      (store_script_param, ":event_type", 2),
      (try_begin),
        ###############
        #SERVER EVENTS#
        ###############
        (eq, ":event_type", multiplayer_event_set_item_selection),
        (store_script_param, ":slot_no", 3),
        (store_script_param, ":value", 4),
        (try_begin),
          #valid slot check
          (is_between, ":slot_no", slot_player_selected_item_indices_begin, slot_player_selected_item_indices_end),
          #valid item check
          (assign, ":valid_item", 0),
          (try_begin),
            (eq, ":value", -1),
            (assign, ":valid_item", 1),
          (else_try),
            (ge, ":value", 0),
            (player_get_troop_id, ":player_troop_no", ":player_no"),
            (is_between, ":player_troop_no", multiplayer_troops_begin, multiplayer_troops_end),
            (store_sub, ":troop_index", ":player_troop_no", multiplayer_troops_begin),
            (val_add, ":troop_index", slot_item_multiplayer_availability_linked_list_begin),
            (item_get_slot, ":prev_next_item_ids", ":value", ":troop_index"),
            (gt, ":prev_next_item_ids", 0), #0 if the item is not valid for the multiplayer mode
            (assign, ":valid_item", 1),
            (try_begin),
              (neq, "$g_horses_are_avaliable", 1),
              (item_get_slot, ":item_class", ":value", slot_item_multiplayer_item_class),
              (is_between, ":item_class", multi_item_class_type_horses_begin, multi_item_class_type_horses_end),
              (assign, ":valid_item", 0),
            (try_end),
            (try_begin),
              (eq, "$g_multiplayer_disallow_ranged_weapons", 1),
              (item_get_slot, ":item_class", ":value", slot_item_multiplayer_item_class),
              (is_between, ":item_class", multi_item_class_type_ranged_weapons_begin, multi_item_class_type_ranged_weapons_end),
              (assign, ":valid_item", 0),
            (try_end),
          (try_end),
          (eq, ":valid_item", 1),
          #condition checks are done
          (player_set_slot, ":player_no", ":slot_no", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_set_bot_selection),
        (store_script_param, ":slot_no", 3),
        (store_script_param, ":value", 4),
        (try_begin),
          #condition check
          (is_between, ":slot_no", slot_player_bot_type_1_wanted, slot_player_bot_type_4_wanted + 1),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (player_set_slot, ":player_no", ":slot_no", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_change_team_no),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_get_team_no, ":player_team", ":player_no"),
          (neq, ":player_team", ":value"),
          
          #condition checks are done
          (try_begin),
            #check if available
            (call_script, "script_cf_multiplayer_team_is_available", ":player_no", ":value"),
            #reset troop_id to -1
            (player_set_troop_id, ":player_no", -1),
            (player_set_team_no, ":player_no", ":value"),
            (try_begin),
              (neq, ":value", multi_team_spectator),
              (neq, ":value", multi_team_unassigned),
              
              (store_mission_timer_a, ":player_last_team_select_time"),
              (player_set_slot, ":player_no", slot_player_last_team_select_time, ":player_last_team_select_time"),
              
              (multiplayer_send_message_to_player, ":player_no", multiplayer_event_return_confirmation),
            (try_end),
          (else_try),
            #reject request
            (multiplayer_send_message_to_player, ":player_no", multiplayer_event_return_rejection),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_change_troop_id),
        (store_script_param, ":value", 3),
        #troop-faction validity check
        (try_begin),
          (eq, ":value", -1),
          (player_set_troop_id, ":player_no", -1),
        (else_try),
          (is_between, ":value", multiplayer_troops_begin, multiplayer_troops_end),
          (player_get_team_no, ":player_team", ":player_no"),
          (is_between, ":player_team", 0, multi_team_spectator),
          (team_get_faction, ":team_faction", ":player_team"),
          (store_troop_faction, ":new_troop_faction", ":value"),
          (eq, ":new_troop_faction", ":team_faction"),
          (player_set_troop_id, ":player_no", ":value"),
          (call_script, "script_multiplayer_clear_player_selected_items", ":player_no"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_start_map),
        (store_script_param, ":value", 3),
        (store_script_param, ":value_2", 4),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", multiplayer_scenes_begin, multiplayer_scenes_end),
          (is_between, ":value_2", 0, multiplayer_num_game_types),
          (server_get_changing_game_type_allowed, "$g_multiplayer_changing_game_type_allowed"),
          (this_or_next|eq, "$g_multiplayer_changing_game_type_allowed", 1),
          (eq, "$g_multiplayer_game_type", ":value_2"),
          (call_script, "script_multiplayer_fill_map_game_types", ":value_2"),
          (assign, ":num_maps", reg0),
          (assign, ":is_valid", 0),
          (store_add, ":end_cond", multi_data_maps_for_game_type_begin, ":num_maps"),
          (try_for_range, ":i_map", multi_data_maps_for_game_type_begin, ":end_cond"),
            (troop_slot_eq, "trp_multiplayer_data", ":i_map", ":value"),
            (assign, ":is_valid", 1),
            (assign, ":end_cond", 0),
          (try_end),
          (eq, ":is_valid", 1),
          #condition checks are done
          (assign, "$g_multiplayer_game_type", ":value_2"),
          (assign, "$g_multiplayer_selected_map", ":value"),
          (team_set_faction, 0, "$g_multiplayer_next_team_1_faction"),
          (team_set_faction, 1, "$g_multiplayer_next_team_2_faction"),
          (call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
          (start_multiplayer_mission, reg0, "$g_multiplayer_selected_map", 1),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_max_num_players),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 2, 201),
          #condition checks are done
          (server_set_max_num_players, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_num_bots_in_team),
        (store_script_param, ":value", 3),
        (store_script_param, ":value_2", 4),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 1, 3),
          (is_between, ":value_2", 0, "$g_multiplayer_max_num_bots"),
          #condition checks are done
          (try_begin),
            (eq, ":value", 1),
            (assign, "$g_multiplayer_num_bots_team_1", ":value_2"),
          (else_try),
            (assign, "$g_multiplayer_num_bots_team_2", ":value_2"),
          (try_end),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_2_int_to_player, ":cur_player", multiplayer_event_return_num_bots_in_team, ":value", ":value_2"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_anti_cheat),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (server_set_anti_cheat, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_friendly_fire),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (server_set_friendly_fire, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_melee_friendly_fire),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (server_set_melee_friendly_fire, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_friendly_fire_damage_self_ratio),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 101),
          #condition checks are done
          (server_set_friendly_fire_damage_self_ratio, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_friendly_fire_damage_friend_ratio),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 101),
          #condition checks are done
          (server_set_friendly_fire_damage_friend_ratio, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_ghost_mode),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 4),
          #condition checks are done
          (server_set_ghost_mode, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_control_block_dir),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (server_set_control_block_dir, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_combat_speed),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 5),
          #condition checks are done
          (server_set_combat_speed, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_respawn_count),
        (store_script_param, ":value", 3),
        #validity check
        (player_is_admin, ":player_no"),
        (is_between, ":value", 0, 6),
        #condition checks are done
        (assign, "$g_multiplayer_number_of_respawn_count", ":value"),
        (get_max_players, ":num_players"),
        (try_for_range, ":cur_player", 1, ":num_players"),
          (player_is_active, ":cur_player"),
          (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_respawn_count, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_add_to_servers_list),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          #condition checks are done
          (server_set_add_to_game_servers_list, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_respawn_period),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 3, 31),
          #condition checks are done
          (assign, "$g_multiplayer_respawn_period", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_respawn_period, ":value"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_game_max_minutes),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 5, 121),
          #condition checks are done
          (assign, "$g_multiplayer_game_max_minutes", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_round_max_seconds),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 60, 901),
          #condition checks are done
          (assign, "$g_multiplayer_round_max_seconds", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_round_max_seconds, ":value"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_player_respawn_as_bot),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (assign, "$g_multiplayer_player_respawn_as_bot", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_player_respawn_as_bot, ":value"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_game_max_points),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 3, 1001),
          #condition checks are done
          (assign, "$g_multiplayer_game_max_points", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_point_gained_from_flags),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 25, 401),
          #condition checks are done
          (assign, "$g_multiplayer_point_gained_from_flags", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_point_gained_from_capturing_flag),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 11),
          #condition checks are done
          (assign, "$g_multiplayer_point_gained_from_capturing_flag", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_initial_gold_multiplier),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 1001),
          #condition checks are done
          (assign, "$g_multiplayer_initial_gold_multiplier", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_battle_earnings_multiplier),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 1001),
          #condition checks are done
          (assign, "$g_multiplayer_battle_earnings_multiplier", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_round_earnings_multiplier),
        (store_script_param, ":value", 3),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 1001),
          #condition checks are done
          (assign, "$g_multiplayer_round_earnings_multiplier", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_server_name),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (server_get_renaming_server_allowed, "$g_multiplayer_renaming_server_allowed"),
          (eq, "$g_multiplayer_renaming_server_allowed", 1),
          #condition checks are done
          (server_set_name, s0), #validity is checked inside this function
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_game_password),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          #condition checks are done
          (server_set_password, s0), #validity is checked inside this function
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_welcome_message),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          #condition checks are done
          (server_set_welcome_message, s0), #validity is checked inside this function
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_team_faction),
        (store_script_param, ":value", 3),
        (store_script_param, ":value_2", 4),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 1, 3),
          (is_between, ":value_2", npc_kingdoms_begin, npc_kingdoms_end),
          ##          (assign, ":is_valid", 0),
          ##          (try_begin),
          ##            (eq, ":value", 1),
          ##            (neq, ":value_2", "$g_multiplayer_next_team_2_faction"),
          ##            (assign, ":is_valid", 1),
          ##          (else_try),
          ##            (neq, ":value_2", "$g_multiplayer_next_team_1_faction"),
          ##            (assign, ":is_valid", 1),
          ##          (try_end),
          ##          (eq, ":is_valid", 1),
          #condition checks are done
          (try_begin),
            (eq, ":value", 1),
            (assign, "$g_multiplayer_next_team_1_faction", ":value_2"),
          (else_try),
            (assign, "$g_multiplayer_next_team_2_faction", ":value_2"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_open_game_rules),
        (try_begin),
          #no validity check
          (server_get_max_num_players, ":max_num_players"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_max_num_players, ":max_num_players"),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_next_team_faction, 1, "$g_multiplayer_next_team_1_faction"),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_next_team_faction, 2, "$g_multiplayer_next_team_2_faction"),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_num_bots_in_team, 1, "$g_multiplayer_num_bots_team_1"),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_num_bots_in_team, 2, "$g_multiplayer_num_bots_team_2"),
          (server_get_anti_cheat, ":server_anti_cheat"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_anti_cheat, ":server_anti_cheat"),
          (server_get_friendly_fire, ":server_friendly_fire"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire, ":server_friendly_fire"),
          (server_get_melee_friendly_fire, ":server_melee_friendly_fire"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_melee_friendly_fire, ":server_melee_friendly_fire"),
          (server_get_friendly_fire_damage_self_ratio, ":friendly_fire_damage_self_ratio"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire_damage_self_ratio, ":friendly_fire_damage_self_ratio"),
          (server_get_friendly_fire_damage_friend_ratio, ":friendly_fire_damage_friend_ratio"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire_damage_friend_ratio, ":friendly_fire_damage_friend_ratio"),
          (server_get_ghost_mode, ":server_ghost_mode"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_ghost_mode, ":server_ghost_mode"),
          (server_get_control_block_dir, ":server_control_block_dir"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_control_block_dir, ":server_control_block_dir"),
          (server_get_combat_speed, ":server_combat_speed"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_combat_speed, ":server_combat_speed"),
          (server_get_add_to_game_servers_list, ":server_add_to_servers_list"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_add_to_servers_list, ":server_add_to_servers_list"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_respawn_period, "$g_multiplayer_respawn_period"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_game_max_minutes, "$g_multiplayer_game_max_minutes"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_round_max_seconds, "$g_multiplayer_round_max_seconds"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_player_respawn_as_bot, "$g_multiplayer_player_respawn_as_bot"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_game_max_points, "$g_multiplayer_game_max_points"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_point_gained_from_flags, "$g_multiplayer_point_gained_from_flags"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_point_gained_from_capturing_flag, "$g_multiplayer_point_gained_from_capturing_flag"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_initial_gold_multiplier, "$g_multiplayer_initial_gold_multiplier"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_battle_earnings_multiplier, "$g_multiplayer_battle_earnings_multiplier"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_round_earnings_multiplier, "$g_multiplayer_round_earnings_multiplier"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_valid_vote_ratio, "$g_multiplayer_valid_vote_ratio"),
          (str_store_server_name, s0),
          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_return_server_name, s0),
          (multiplayer_send_message_to_player, ":player_no", multiplayer_event_return_open_game_rules),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_open_admin_panel),
        (try_begin),
          #validity check
          (player_is_admin, ":player_no"),
          #condition checks are done
          (server_get_renaming_server_allowed, "$g_multiplayer_renaming_server_allowed"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_renaming_server_allowed, "$g_multiplayer_renaming_server_allowed"),
          (server_get_changing_game_type_allowed, "$g_multiplayer_changing_game_type_allowed"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_changing_game_type_allowed, "$g_multiplayer_changing_game_type_allowed"),
          (server_get_max_num_players, ":max_num_players"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_max_num_players, ":max_num_players"),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_next_team_faction, 1, "$g_multiplayer_next_team_1_faction"),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_next_team_faction, 2, "$g_multiplayer_next_team_2_faction"),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_num_bots_in_team, 1, "$g_multiplayer_num_bots_team_1"),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_num_bots_in_team, 2, "$g_multiplayer_num_bots_team_2"),
          (server_get_anti_cheat, ":server_anti_cheat"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_anti_cheat, ":server_anti_cheat"),
          (server_get_friendly_fire, ":server_friendly_fire"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire, ":server_friendly_fire"),
          (server_get_melee_friendly_fire, ":server_melee_friendly_fire"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_melee_friendly_fire, ":server_melee_friendly_fire"),
          (server_get_friendly_fire_damage_self_ratio, ":friendly_fire_damage_self_ratio"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire_damage_self_ratio, ":friendly_fire_damage_self_ratio"),
          (server_get_friendly_fire_damage_friend_ratio, ":friendly_fire_damage_friend_ratio"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_friendly_fire_damage_friend_ratio, ":friendly_fire_damage_friend_ratio"),
          (server_get_ghost_mode, ":server_ghost_mode"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_ghost_mode, ":server_ghost_mode"),
          (server_get_control_block_dir, ":server_control_block_dir"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_control_block_dir, ":server_control_block_dir"),
          (server_get_combat_speed, ":server_combat_speed"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_combat_speed, ":server_combat_speed"),
          (server_get_add_to_game_servers_list, ":server_add_to_servers_list"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_add_to_servers_list, ":server_add_to_servers_list"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_respawn_period, "$g_multiplayer_respawn_period"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_game_max_minutes, "$g_multiplayer_game_max_minutes"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_round_max_seconds, "$g_multiplayer_round_max_seconds"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_player_respawn_as_bot, "$g_multiplayer_player_respawn_as_bot"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_game_max_points, "$g_multiplayer_game_max_points"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_point_gained_from_flags, "$g_multiplayer_point_gained_from_flags"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_point_gained_from_capturing_flag, "$g_multiplayer_point_gained_from_capturing_flag"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_initial_gold_multiplier, "$g_multiplayer_initial_gold_multiplier"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_battle_earnings_multiplier, "$g_multiplayer_battle_earnings_multiplier"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_round_earnings_multiplier, "$g_multiplayer_round_earnings_multiplier"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_valid_vote_ratio, "$g_multiplayer_valid_vote_ratio"),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_max_num_bots, "$g_multiplayer_max_num_bots"),
          (str_store_server_name, s0),
          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_return_server_name, s0),
          (str_store_server_password, s0),
          (multiplayer_send_string_to_player, ":player_no", multiplayer_event_return_game_password, s0),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_start_new_poll),
        (try_begin),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          #validity check
          (eq, "$g_multiplayer_poll_running", 0),
          (store_mission_timer_a, ":mission_timer"),
          (player_get_slot, ":poll_disable_time", ":player_no", slot_player_poll_disabled_until_time),
          (ge, ":mission_timer", ":poll_disable_time"),
          (assign, ":continue", 0),
          (try_begin),
            (eq, ":value", 1), # kicking a player
            (try_begin),
              (eq, "$g_multiplayer_kick_voteable", 1),
              (player_is_active, ":value_2"),
              (assign, ":continue", 1),
            (try_end),
          (else_try),
            (eq, ":value", 2), # banning a player
            (try_begin),
              (eq, "$g_multiplayer_ban_voteable", 1),
              (player_is_active, ":value_2"),
              (save_ban_info_of_player, ":value_2"),
              (assign, ":continue", 1),
            (try_end),
          (else_try), # vote for map
            (eq, ":value", 0),
            (try_begin),
              (eq, "$g_multiplayer_maps_voteable", 1),
              (call_script, "script_multiplayer_fill_map_game_types", "$g_multiplayer_game_type"),
              (assign, ":num_maps", reg0),
              (try_for_range, ":i_map", 0, ":num_maps"),
                (store_add, ":map_slot", ":i_map", multi_data_maps_for_game_type_begin),
                (troop_slot_eq, "trp_multiplayer_data", ":map_slot", ":value_2"),
                (assign, ":continue", 1),
                (assign, ":num_maps", 0), #break
              (try_end),
            (try_end),
          (else_try),
            (eq, ":value", 3), #vote for map and factions
            (try_begin),
              (eq, "$g_multiplayer_factions_voteable", 1),
              (store_script_param, ":value_3", 5),
              (store_script_param, ":value_4", 6),
              (call_script, "script_multiplayer_fill_map_game_types", "$g_multiplayer_game_type"),
              (assign, ":num_maps", reg0),
              (try_for_range, ":i_map", 0, ":num_maps"),
                (store_add, ":map_slot", ":i_map", multi_data_maps_for_game_type_begin),
                (troop_slot_eq, "trp_multiplayer_data", ":map_slot", ":value_2"),
                (assign, ":continue", 1),
                (assign, ":num_maps", 0), #break
              (try_end),
              (try_begin),
                (eq, ":continue", 1),
                (this_or_next|neg|is_between, ":value_3", npc_kingdoms_begin, npc_kingdoms_end),
                (this_or_next|neg|is_between, ":value_4", npc_kingdoms_begin, npc_kingdoms_end),
                (eq, ":value_3", ":value_4"),
                (assign, ":continue", 0),
              (try_end),
            (try_end),
          (else_try),
            (eq, ":value", 4), #vote for number of bots
            (store_script_param, ":value_3", 5),
            (store_add, ":upper_limit", "$g_multiplayer_num_bots_voteable", 1),
            (is_between, ":value_2", 0, ":upper_limit"),
            (is_between, ":value_3", 0, ":upper_limit"),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
          #condition checks are done
          (str_store_player_username, s0, ":player_no"),
          (try_begin),
            (eq, ":value", 1), #kicking a player
            (str_store_player_username, s1, ":value_2"),
            (server_add_message_to_log, "str_poll_kick_player_s1_by_s0"),
          (else_try),
            (eq, ":value", 2), #banning a player
            (str_store_player_username, s1, ":value_2"),
            (server_add_message_to_log, "str_poll_ban_player_s1_by_s0"),
          (else_try),
            (eq, ":value", 0), #vote for map
            (store_sub, ":string_index", ":value_2", multiplayer_scenes_begin),
            (val_add, ":string_index", multiplayer_scene_names_begin),
            (str_store_string, s1, ":string_index"),
            (server_add_message_to_log, "str_poll_change_map_to_s1_by_s0"),
          (else_try),
            (eq, ":value", 3), #vote for map and factions
            (store_sub, ":string_index", ":value_2", multiplayer_scenes_begin),
            (val_add, ":string_index", multiplayer_scene_names_begin),
            (str_store_string, s1, ":string_index"),
            (str_store_faction_name, s2, ":value_3"),
            (str_store_faction_name, s3, ":value_4"),
            (server_add_message_to_log, "str_poll_change_map_to_s1_and_factions_to_s2_and_s3_by_s0"),
          (else_try),
            (eq, ":value", 4), #vote for number of bots
            (assign, reg0, ":value_2"),
            (assign, reg1, ":value_3"),
            (server_add_message_to_log, "str_poll_change_number_of_bots_to_reg0_and_reg1_by_s0"),
          (try_end),
          (assign, "$g_multiplayer_poll_running", 1),
          (assign, "$g_multiplayer_poll_ended", 0),
          (assign, "$g_multiplayer_poll_num_sent", 0),
          (assign, "$g_multiplayer_poll_yes_count", 0),
          (assign, "$g_multiplayer_poll_no_count", 0),
          (assign, "$g_multiplayer_poll_to_show", ":value"),
          (assign, "$g_multiplayer_poll_value_to_show", ":value_2"),
          (try_begin),
            (eq, ":value", 3),
            (assign, "$g_multiplayer_poll_value_2_to_show", ":value_3"),
            (assign, "$g_multiplayer_poll_value_3_to_show", ":value_4"),
          (else_try),
            (eq, ":value", 4),
            (assign, "$g_multiplayer_poll_value_2_to_show", ":value_3"),
            (assign, "$g_multiplayer_poll_value_3_to_show", -1),
          (else_try),
            (assign, "$g_multiplayer_poll_value_2_to_show", -1),
            (assign, "$g_multiplayer_poll_value_3_to_show", -1),
          (try_end),
          (store_add, ":poll_disable_until", ":mission_timer", multiplayer_poll_disable_period),
          (player_set_slot, ":player_no", slot_player_poll_disabled_until_time, ":poll_disable_until"),
          (store_add, "$g_multiplayer_poll_end_time", ":mission_timer", 60),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 0, ":num_players"),
            (player_is_active, ":cur_player"),
            (player_set_slot, ":cur_player", slot_player_can_answer_poll, 1),
            (val_add, "$g_multiplayer_poll_num_sent", 1),
            (multiplayer_send_4_int_to_player, ":cur_player", multiplayer_event_ask_for_poll, "$g_multiplayer_poll_to_show", "$g_multiplayer_poll_value_to_show", "$g_multiplayer_poll_value_2_to_show", "$g_multiplayer_poll_value_3_to_show"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_answer_to_poll),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (eq, "$g_multiplayer_poll_running", 1),
          (is_between, ":value", 0, 2),
          (player_slot_eq, ":player_no", slot_player_can_answer_poll, 1),
          #condition checks are done
          (player_set_slot, ":player_no", slot_player_can_answer_poll, 0),
          (try_begin),
            (eq, ":value", 0),
            (val_add, "$g_multiplayer_poll_no_count", 1),
          (else_try),
            (eq, ":value", 1),
            (val_add, "$g_multiplayer_poll_yes_count", 1),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_kick_player),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (player_is_active, ":value"),
          #condition checks are done
          (kick_player, ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_ban_player),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (player_is_active, ":value"),
          #condition checks are done
          (ban_player, ":value", 0, ":player_no"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_valid_vote_ratio),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 50, 101),
          #condition checks are done
          (assign, "$g_multiplayer_valid_vote_ratio", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_auto_team_balance_limit),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (this_or_next|is_between, ":value", 2, 7),
          (eq, ":value", 1000),
          #condition checks are done
          (assign, "$g_multiplayer_auto_team_balance_limit", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_auto_team_balance_limit, ":value"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_num_bots_voteable),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 51),
		  (is_between, ":value", 0, "$g_multiplayer_max_num_bots"),						#	1.143 Port // added the , 0
          #condition checks are done
          (assign, "$g_multiplayer_num_bots_voteable", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_num_bots_voteable, ":value"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_factions_voteable),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (assign, "$g_multiplayer_factions_voteable", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_factions_voteable, ":value"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_maps_voteable),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (assign, "$g_multiplayer_maps_voteable", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_maps_voteable, ":value"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_kick_voteable),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (assign, "$g_multiplayer_kick_voteable", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_kick_voteable, ":value"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_ban_voteable),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (assign, "$g_multiplayer_ban_voteable", ":value"),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 1, ":num_players"),
            (player_is_active, ":cur_player"),
            (multiplayer_send_int_to_player, ":cur_player", multiplayer_event_return_ban_voteable, ":value"),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_allow_player_banners),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (assign, "$g_multiplayer_allow_player_banners", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_force_default_armor),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (assign, "$g_multiplayer_force_default_armor", ":value"),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_offer_duel),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
          (agent_is_active, ":value"),
          (agent_is_alive, ":value"),
          (agent_is_human, ":value"),
          (player_get_agent_id, ":player_agent_no", ":player_no"),
          (agent_is_active, ":player_agent_no"),
          (agent_is_alive, ":player_agent_no"),
          (agent_get_position, pos0, ":player_agent_no"),
          (agent_get_position, pos1, ":value"),
          (get_sq_distance_between_positions_in_meters, ":agent_dist_sq", pos0, pos1),
          (le, ":agent_dist_sq", 49),
          #allow duelists to receive new offers
          (this_or_next|agent_check_offer_from_agent, ":player_agent_no", ":value"),
          (agent_slot_eq, ":player_agent_no", slot_agent_in_duel_with, -1),
          (neg|agent_slot_eq, ":player_agent_no", slot_agent_in_duel_with, ":value"), #don't allow spamming duel offers during countdown
          #condition checks are done
          (try_begin),
            #accepting a duel
            (agent_check_offer_from_agent, ":player_agent_no", ":value"),
            (call_script, "script_multiplayer_accept_duel", ":player_agent_no", ":value"),
          (else_try),
            #sending a duel request
            (assign, ":display_notification", 1),
            (try_begin),
              (agent_check_offer_from_agent, ":value", ":player_agent_no"),
              (assign, ":display_notification", 0),
            (try_end),
            (agent_add_offer_with_timeout, ":value", ":player_agent_no", 10000), #10 second timeout
            (agent_get_player_id, ":value_player", ":value"),
            (try_begin),
              (player_is_active, ":value_player"), #might be AI
              (try_begin),
                (eq, ":display_notification", 1),
                (multiplayer_send_int_to_player, ":value_player", multiplayer_event_show_duel_request, ":player_agent_no"),
              (try_end),
            (else_try),
              (call_script, "script_multiplayer_accept_duel", ":value", ":player_agent_no"),
            (try_end),
          (try_end),
        (try_end),
      (else_try),
        (eq, ":event_type", multiplayer_event_admin_set_disallow_ranged_weapons),
        (try_begin),
          (store_script_param, ":value", 3),
          #validity check
          (player_is_admin, ":player_no"),
          (is_between, ":value", 0, 2),
          #condition checks are done
          (assign, "$g_multiplayer_disallow_ranged_weapons", ":value"),
        (try_end),
      (else_try),
        ###############
        #CLIENT EVENTS#
        ###############
        (neg|multiplayer_is_dedicated_server), ##1.134
        (try_begin),
          (eq, ":event_type", multiplayer_event_return_renaming_server_allowed),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_renaming_server_allowed", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_changing_game_type_allowed),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_changing_game_type_allowed", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_max_num_players),
          (store_script_param, ":value", 3),
          (server_set_max_num_players, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_next_team_faction),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (try_begin),
            (eq, ":value", 1),
            (assign, "$g_multiplayer_next_team_1_faction", ":value_2"),
          (else_try),
            (assign, "$g_multiplayer_next_team_2_faction", ":value_2"),
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_num_bots_in_team),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (try_begin),
            (eq, ":value", 1),
            (assign, "$g_multiplayer_num_bots_team_1", ":value_2"),
          (else_try),
            (assign, "$g_multiplayer_num_bots_team_2", ":value_2"),
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_anti_cheat),
          (store_script_param, ":value", 3),
          (server_set_anti_cheat, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_friendly_fire),
          (store_script_param, ":value", 3),
          (server_set_friendly_fire, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_melee_friendly_fire),
          (store_script_param, ":value", 3),
          (server_set_melee_friendly_fire, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_friendly_fire_damage_self_ratio),
          (store_script_param, ":value", 3),
          (server_set_friendly_fire_damage_self_ratio, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_friendly_fire_damage_friend_ratio),
          (store_script_param, ":value", 3),
          (server_set_friendly_fire_damage_friend_ratio, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_ghost_mode),
          (store_script_param, ":value", 3),
          (server_set_ghost_mode, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_control_block_dir),
          (store_script_param, ":value", 3),
          (server_set_control_block_dir, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_add_to_servers_list),
          (store_script_param, ":value", 3),
          (server_set_add_to_game_servers_list, ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_respawn_period),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_respawn_period", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_game_max_minutes),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_game_max_minutes", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_round_max_seconds),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_round_max_seconds", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_player_respawn_as_bot),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_player_respawn_as_bot", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_game_max_points),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_game_max_points", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_point_gained_from_flags),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_point_gained_from_flags", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_point_gained_from_capturing_flag),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_point_gained_from_capturing_flag", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_initial_gold_multiplier),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_initial_gold_multiplier", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_battle_earnings_multiplier),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_battle_earnings_multiplier", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_round_earnings_multiplier),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_round_earnings_multiplier", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_respawn_count),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_number_of_respawn_count", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_server_name),
          (server_set_name, s0),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_game_password),
          (server_set_password, s0),
          #this is the last option in admin panel, so start the presentation
          (start_presentation, "prsnt_game_multiplayer_admin_panel"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_open_game_rules),
          #this is the last message for game rules, so start the presentation
          (assign, "$g_multiplayer_show_server_rules", 1),
          (start_presentation, "prsnt_multiplayer_welcome_message"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_game_type),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_game_type", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_valid_vote_ratio),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_valid_vote_ratio", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_max_num_bots),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_max_num_bots", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_server_mission_timer_while_player_joined),
          (store_script_param, ":value", 3),
          (assign, "$server_mission_timer_while_player_joined", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_auto_team_balance_limit),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_auto_team_balance_limit", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_num_bots_voteable),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_num_bots_voteable", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_factions_voteable),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_factions_voteable", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_maps_voteable),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_maps_voteable", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_kick_voteable),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_kick_voteable", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_ban_voteable),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_ban_voteable", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_allow_player_banners),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_allow_player_banners", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_force_default_armor),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_force_default_armor", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_disallow_ranged_weapons),
          (store_script_param, ":value", 3),
          (assign, "$g_multiplayer_disallow_ranged_weapons", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_confirmation),
          (assign, "$g_confirmation_result", 1),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_rejection),
          (assign, "$g_confirmation_result", -1),
        (else_try),
          (eq, ":event_type", multiplayer_event_show_multiplayer_message),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (call_script, "script_show_multiplayer_message", ":value", ":value_2"),
        (else_try),
          (eq, ":event_type", multiplayer_event_draw_this_round),
          (store_script_param, ":value", 3),
          (call_script, "script_draw_this_round", ":value"),
        (else_try),
          (eq, ":event_type", multiplayer_event_set_attached_scene_prop),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (call_script, "script_set_attached_scene_prop", ":value", ":value_2"),
          (try_begin),
            (eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
            (try_begin),
              (neq, ":value_2", -1),
              (agent_set_horse_speed_factor, ":value", 75),
            (else_try),
              (agent_set_horse_speed_factor, ":value", 100),
            (try_end),
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_set_team_flag_situation),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (call_script, "script_set_team_flag_situation", ":value", ":value_2"),
        (else_try),
          (eq, ":event_type", multiplayer_event_set_team_score),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (call_script, "script_team_set_score", ":value", ":value_2"),
        (else_try),
          (eq, ":event_type", multiplayer_event_set_player_score_kill_death),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (store_script_param, ":value_3", 5),
          (store_script_param, ":value_4", 6),
          (call_script, "script_player_set_score", ":value", ":value_2"),
          (call_script, "script_player_set_kill_count", ":value", ":value_3"),
          (call_script, "script_player_set_death_count", ":value", ":value_4"),
        (else_try),
          (eq, ":event_type", multiplayer_event_set_num_agents_around_flag),
          (store_script_param, ":flag_no", 3),
          (store_script_param, ":current_owner_code", 4),
          (call_script, "script_set_num_agents_around_flag", ":flag_no", ":current_owner_code"),
        (else_try),
          (eq, ":event_type", multiplayer_event_ask_for_poll),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (store_script_param, ":value_3", 5),
          (store_script_param, ":value_4", 6),
          (assign, ":continue_to_poll", 0),
          (try_begin),
            (this_or_next|eq, ":value", 1),
            (eq, ":value", 2),
            (player_is_active, ":value_2"), #might go offline before here
            (assign, ":continue_to_poll", 1),
          (else_try),
            (assign, ":continue_to_poll", 1),
          (try_end),
          (try_begin),
            (eq, ":continue_to_poll", 1),
            (assign, "$g_multiplayer_poll_to_show", ":value"),
            (assign, "$g_multiplayer_poll_value_to_show", ":value_2"),
            (assign, "$g_multiplayer_poll_value_2_to_show", ":value_3"),
            (assign, "$g_multiplayer_poll_value_3_to_show", ":value_4"),
            (store_mission_timer_a, ":mission_timer"),
            (store_add, "$g_multiplayer_poll_client_end_time", ":mission_timer", 60),
            (start_presentation, "prsnt_multiplayer_poll"),
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_change_flag_owner),
          (store_script_param, ":flag_no", 3),
          (store_script_param, ":owner_code", 4),
          (call_script, "script_change_flag_owner", ":flag_no", ":owner_code"),
        (else_try),
          (eq, ":event_type", multiplayer_event_use_item),
          (store_script_param, ":value", 3),
          (store_script_param, ":value_2", 4),
          (call_script, "script_use_item", ":value", ":value_2"),
        (else_try),
          (eq, ":event_type", multiplayer_event_set_scene_prop_open_or_close),
          (store_script_param, ":instance_id", 3),
          
          (scene_prop_set_slot, ":instance_id", scene_prop_open_or_close_slot, 1),
          
          (prop_instance_get_scene_prop_kind, ":scene_prop_id", ":instance_id"),
          
          (try_begin),
            (eq, ":scene_prop_id", "spr_winch_b"),
            (assign, ":effected_object", "spr_portcullis"),
          (else_try),
            (this_or_next|eq, ":scene_prop_id", "spr_castle_e_sally_door_a"),
            (this_or_next|eq, ":scene_prop_id", "spr_castle_f_sally_door_a"),
            (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_left"),
            (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_right"),
            (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),
            (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_right"),
            (this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_a"),
            (this_or_next|eq, ":scene_prop_id", "spr_door_destructible"),
            (this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_b"),
            (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_6m"),
            (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_8m"),
            (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_10m"),
            (this_or_next|eq, ":scene_prop_id", "spr_siege_ladder_move_12m"),
            (eq, ":scene_prop_id", "spr_siege_ladder_move_14m"),
            (assign, ":effected_object", ":scene_prop_id"),
          (try_end),
          
          (try_begin),
            (eq, ":effected_object", "spr_portcullis"),
            
            (assign, ":smallest_dist", -1),
            (prop_instance_get_position, pos0, ":instance_id"),
            (scene_prop_get_num_instances, ":num_instances_of_effected_object", ":effected_object"),
            (try_for_range, ":cur_instance", 0, ":num_instances_of_effected_object"),
              (scene_prop_get_instance, ":cur_instance_id", ":effected_object", ":cur_instance"),
              (prop_instance_get_position, pos1, ":cur_instance_id"),
              (get_sq_distance_between_positions, ":dist", pos0, pos1),
              (this_or_next|eq, ":smallest_dist", -1),
              (lt, ":dist", ":smallest_dist"),
              (assign, ":smallest_dist", ":dist"),
              (assign, ":effected_object_instance_id", ":cur_instance_id"),
            (try_end),
            
            (ge, ":smallest_dist", 0),
            (prop_instance_is_animating, ":is_animating", ":effected_object_instance_id"),
            (eq, ":is_animating", 0),
            
            (prop_instance_get_starting_position, pos0, ":effected_object_instance_id"),
            (position_move_z, pos0, 375),
            (prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 1),
          (else_try),
            (this_or_next|eq, ":scene_prop_id", "spr_castle_e_sally_door_a"),
            (this_or_next|eq, ":scene_prop_id", "spr_castle_f_sally_door_a"),
            (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_left"),
            (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_right"),
            (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),
            (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_right"),
            (this_or_next|eq, ":scene_prop_id", "spr_castle_f_door_a"),
            (this_or_next|eq, ":scene_prop_id", "spr_door_destructible"),
            (eq, ":scene_prop_id", "spr_castle_f_door_b"),
            (assign, ":effected_object_instance_id", ":instance_id"),
            (prop_instance_get_starting_position, pos0, ":effected_object_instance_id"),
            (position_rotate_z, pos0, -80),
            (prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 1),
          (else_try),
            (assign, ":effected_object_instance_id", ":instance_id"),
            (prop_instance_is_animating, ":is_animating", ":effected_object_instance_id"),
            (eq, ":is_animating", 0),
            (prop_instance_get_starting_position, pos0, ":effected_object_instance_id"),
            (prop_instance_animate_to_position, ":effected_object_instance_id", pos0, 1),
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_set_round_start_time),
          (store_script_param, ":value", 3),
          
          (try_begin),
            (neq, ":value", -9999),
            (assign, "$g_round_start_time", ":value"),
          (else_try),
            (store_mission_timer_a, "$g_round_start_time"),
            
            #if round start time is assigning to current time (so new round is starting) then also initialize moveable object slots too.
            (call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_6m"),
            (call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_8m"),
            (call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_10m"),
            (call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_12m"),
            (call_script, "script_initialize_scene_prop_slots", "spr_siege_ladder_move_14m"),
            (call_script, "script_initialize_scene_prop_slots", "spr_winch_b"),
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_force_start_team_selection),
          (try_begin),
            (is_presentation_active, "prsnt_multiplayer_item_select"),
            (assign, "$g_close_equipment_selection", 1),
          (try_end),
          (start_presentation, "prsnt_multiplayer_troop_select"),
        (else_try),
          (eq, ":event_type", multiplayer_event_start_death_mode),
          (assign, "$g_battle_death_mode_started", 2),
          (start_presentation, "prsnt_multiplayer_flag_projection_display_bt"),
          (call_script, "script_start_death_mode"),
        (else_try),
          (eq, ":event_type", multiplayer_event_return_player_respawn_spent),
          (store_script_param, ":value", 3),
          (try_begin),
            (gt, "$g_my_spawn_count", 0),
            (store_add, "$g_my_spawn_count", "$g_my_spawn_count", ":value"),
          (else_try),
            (assign, "$g_my_spawn_count", ":value"),
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_show_duel_request),
          (store_script_param, ":value", 3),
          (try_begin),
            (agent_is_active, ":value"),
            (agent_get_player_id, ":value_player_no", ":value"),
            (try_begin),
              (player_is_active, ":value_player_no"),
              (str_store_player_username, s0, ":value_player_no"),
            (else_try),
              (str_store_agent_name, s0, ":value"),
            (try_end),
            (display_message, "str_s0_offers_a_duel_with_you"),
            (try_begin),
              (get_player_agent_no, ":player_agent"),
              (agent_is_active, ":player_agent"),
              (agent_add_offer_with_timeout, ":player_agent", ":value", 10000), #10 second timeout
            (try_end),
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_start_duel),
          (store_script_param, ":value", 3),
          (store_mission_timer_a, ":mission_timer"),
          (try_begin),
            (agent_is_active, ":value"),
            (get_player_agent_no, ":player_agent"),
            (agent_is_active, ":player_agent"),
            (agent_get_player_id, ":value_player_no", ":value"),
            (try_begin),
              (player_is_active, ":value_player_no"),
              (str_store_player_username, s0, ":value_player_no"),
            (else_try),
              (str_store_agent_name, s0, ":value"),
            (try_end),
            (display_message, "str_a_duel_between_you_and_s0_will_start_in_3_seconds"),
            (assign, "$g_multiplayer_duel_start_time", ":mission_timer"),
            (start_presentation, "prsnt_multiplayer_duel_start_counter"),
            (agent_set_slot, ":player_agent", slot_agent_in_duel_with, ":value"),
            (agent_set_slot, ":value", slot_agent_in_duel_with, ":player_agent"),
            (agent_set_slot, ":player_agent", slot_agent_duel_start_time, ":mission_timer"),
            (agent_set_slot, ":value", slot_agent_duel_start_time, ":mission_timer"),
            (agent_clear_relations_with_agents, ":player_agent"),
            (agent_clear_relations_with_agents, ":value"),
            ##            (agent_add_relation_with_agent, ":player_agent", ":value", -1),
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_cancel_duel),
          (store_script_param, ":value", 3),
          (try_begin),
            (agent_is_active, ":value"),
            (agent_get_player_id, ":value_player_no", ":value"),
            (try_begin),
              (player_is_active, ":value_player_no"),
              (str_store_player_username, s0, ":value_player_no"),
            (else_try),
              (str_store_agent_name, s0, ":value"),
            (try_end),
            (display_message, "str_your_duel_with_s0_is_cancelled"),
          (try_end),
          (try_begin),
            (get_player_agent_no, ":player_agent"),
            (agent_is_active, ":player_agent"),
            (agent_set_slot, ":player_agent", slot_agent_in_duel_with, -1),
            (agent_clear_relations_with_agents, ":player_agent"),
          (try_end),
        (else_try),
          (eq, ":event_type", multiplayer_event_show_server_message),
          (display_message, "str_server_s0", 0xFFFF6666),
        (try_end),
    ]),
    
    # script_cf_multiplayer_evaluate_poll
    # Input: none
    # Output: none (can fail)
    ("cf_multiplayer_evaluate_poll",
      [
        (assign, ":result", 0),
        (assign, "$g_multiplayer_poll_ended", 1),
        (store_add, ":total_votes", "$g_multiplayer_poll_yes_count", "$g_multiplayer_poll_no_count"),
        (store_sub, ":abstain_votes", "$g_multiplayer_poll_num_sent", ":total_votes"),
        (store_mul, ":nos_from_abstains", 3, ":abstain_votes"),
        (val_div, ":nos_from_abstains", 10), #30% of abstains are counted as no
        (val_add, ":total_votes", ":nos_from_abstains"),
        (val_max, ":total_votes", 1), #if someone votes and only 1-3 abstain occurs?
        (store_mul, ":vote_ratio", 100, "$g_multiplayer_poll_yes_count"),
        (val_div, ":vote_ratio", ":total_votes"),
        (try_begin),
          (ge, ":vote_ratio", "$g_multiplayer_valid_vote_ratio"),
          (assign, ":result", 1),
          (try_begin),
            (eq, "$g_multiplayer_poll_to_show", 1), #kick player
            (try_begin),
              (player_is_active, "$g_multiplayer_poll_value_to_show"),
              (kick_player, "$g_multiplayer_poll_value_to_show"),
            (try_end),
          (else_try),
            (eq, "$g_multiplayer_poll_to_show", 2), #ban player
            (ban_player_using_saved_ban_info), #already loaded at the beginning of the poll
          (else_try),
            (eq, "$g_multiplayer_poll_to_show", 3), #change map with factions
            (team_set_faction, 0, "$g_multiplayer_poll_value_2_to_show"),
            (team_set_faction, 1, "$g_multiplayer_poll_value_3_to_show"),
          (else_try),
            (eq, "$g_multiplayer_poll_to_show", 4), #change number of bots
            (assign, "$g_multiplayer_num_bots_team_1", "$g_multiplayer_poll_value_to_show"),
            (assign, "$g_multiplayer_num_bots_team_2", "$g_multiplayer_poll_value_2_to_show"),
            (get_max_players, ":num_players"),
            (try_for_range, ":cur_player", 1, ":num_players"),
              (player_is_active, ":cur_player"),
              (multiplayer_send_2_int_to_player, ":cur_player", multiplayer_event_return_num_bots_in_team, 1, "$g_multiplayer_num_bots_team_1"),
              (multiplayer_send_2_int_to_player, ":cur_player", multiplayer_event_return_num_bots_in_team, 2, "$g_multiplayer_num_bots_team_2"),
            (try_end),
          (try_end),
        (else_try),
          (assign, "$g_multiplayer_poll_running", 0), #end immediately if poll fails. but end after some time if poll succeeds (apply the results first)
        (try_end),
        (get_max_players, ":num_players"),
        #for only server itself-----------------------------------------------------------------------------------------------
        (call_script, "script_show_multiplayer_message", multiplayer_message_type_poll_result, ":result"), #0 is useless here
        #for only server itself-----------------------------------------------------------------------------------------------
        (try_for_range, ":cur_player", 1, ":num_players"),
          (player_is_active, ":cur_player"),
          (multiplayer_send_2_int_to_player, ":cur_player", multiplayer_event_show_multiplayer_message, multiplayer_message_type_poll_result, ":result"),
        (try_end),
        (eq, ":result", 1),
    ]),
    
    # script_multiplayer_accept_duel
    # Input: arg1 = agent_no, arg2 = agent_no_offerer
    # Output: none
    ("multiplayer_accept_duel",
      [
        (store_script_param, ":agent_no", 1),
        (store_script_param, ":agent_no_offerer", 2),
        (try_begin),
          (agent_slot_ge, ":agent_no", slot_agent_in_duel_with, 0),
          (agent_get_slot, ":ex_duelist", ":agent_no", slot_agent_in_duel_with),
          (agent_is_active, ":ex_duelist"),
          (agent_clear_relations_with_agents, ":ex_duelist"),
          (agent_set_slot, ":ex_duelist", slot_agent_in_duel_with, -1),
          (agent_get_player_id, ":player_no", ":ex_duelist"),
          (try_begin),
            (player_is_active, ":player_no"), #might be AI
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_cancel_duel, ":agent_no"),
          (else_try),
            (agent_force_rethink, ":ex_duelist"),
          (try_end),
        (try_end),
        (try_begin),
          (agent_slot_ge, ":agent_no_offerer", slot_agent_in_duel_with, 0),
          (agent_get_slot, ":ex_duelist", ":agent_no_offerer", slot_agent_in_duel_with),
          (agent_is_active, ":ex_duelist"),
          (agent_clear_relations_with_agents, ":ex_duelist"),
          (agent_set_slot, ":ex_duelist", slot_agent_in_duel_with, -1),
          (try_begin),
            (player_is_active, ":player_no"), #might be AI
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_cancel_duel, ":agent_no_offerer"),
          (else_try),
            (agent_force_rethink, ":ex_duelist"),
          (try_end),
        (try_end),
        (agent_set_slot, ":agent_no", slot_agent_in_duel_with, ":agent_no_offerer"),
        (agent_set_slot, ":agent_no_offerer", slot_agent_in_duel_with, ":agent_no"),
        (agent_clear_relations_with_agents, ":agent_no"),
        (agent_clear_relations_with_agents, ":agent_no_offerer"),
        ##     (agent_add_relation_with_agent, ":agent_no", ":agent_no_offerer", -1),
        ##     (agent_add_relation_with_agent, ":agent_no_offerer", ":agent_no", -1),
        (agent_get_player_id, ":player_no", ":agent_no"),
        (store_mission_timer_a, ":mission_timer"),
        (try_begin),
          (player_is_active, ":player_no"), #might be AI
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_start_duel, ":agent_no_offerer"),
        (else_try),
          (agent_force_rethink, ":agent_no"),
        (try_end),
        (agent_set_slot, ":agent_no", slot_agent_duel_start_time, ":mission_timer"),
        (agent_get_player_id, ":agent_no_offerer_player", ":agent_no_offerer"),
        (try_begin),
          (player_is_active, ":agent_no_offerer_player"), #might be AI
          (multiplayer_send_int_to_player, ":agent_no_offerer_player", multiplayer_event_start_duel, ":agent_no"),
        (else_try),
          (agent_force_rethink, ":agent_no_offerer"),
        (try_end),
        (agent_set_slot, ":agent_no_offerer", slot_agent_duel_start_time, ":mission_timer"),
    ]),
    
    # script_game_get_multiplayer_server_option_for_mission_template
    # Input: arg1 = mission_template_id, arg2 = option_index
    # Output: trigger_result = 1 for option available, 0 for not available
    # reg0 = option_value
    ("game_get_multiplayer_server_option_for_mission_template",
      [
        (store_script_param, ":mission_template_id", 1),
        (store_script_param, ":option_index", 2),
        (try_begin),
          (eq, ":option_index", 0),
          (assign, reg0, "$g_multiplayer_team_1_faction"),
          (set_trigger_result, 1),
        (else_try),
          (eq, ":option_index", 1),
          (assign, reg0, "$g_multiplayer_team_2_faction"),
          (set_trigger_result, 1),
        (else_try),
          (eq, ":option_index", 2),
          (assign, reg0, "$g_multiplayer_num_bots_team_1"),
          (set_trigger_result, 1),
        (else_try),
          (eq, ":option_index", 3),
          (assign, reg0, "$g_multiplayer_num_bots_team_2"),
          (set_trigger_result, 1),
        (else_try),
          (eq, ":option_index", 4),
          (server_get_friendly_fire, reg0),
          (set_trigger_result, 1),
        (else_try),
          (eq, ":option_index", 5),
          (server_get_melee_friendly_fire, reg0),
          (set_trigger_result, 1),
        (else_try),
          (eq, ":option_index", 6),
          (server_get_friendly_fire_damage_self_ratio, reg0),
          (set_trigger_result, 1),
        (else_try),
          (eq, ":option_index", 7),
          (server_get_friendly_fire_damage_friend_ratio, reg0),
          (set_trigger_result, 1),
        (else_try),
          (eq, ":option_index", 8),
          (server_get_ghost_mode, reg0),
          (set_trigger_result, 1),
        (else_try),
          (eq, ":option_index", 9),
          (server_get_control_block_dir, reg0),
          (set_trigger_result, 1),
        (else_try),
          (eq, ":option_index", 10),
          (server_get_combat_speed, reg0),
          (set_trigger_result, 1),
        (else_try),
          (try_begin),
            (eq, ":mission_template_id", "mt_multiplayer_hq"),
            (val_add, ":option_index", 1), #max game time
          (try_end),
          (eq, ":option_index", 11),
          (assign, reg0, "$g_multiplayer_game_max_minutes"),
          (set_trigger_result, 1),
        (else_try),
          (try_begin),
            (neq, ":mission_template_id", "mt_multiplayer_bt"),
            (neq, ":mission_template_id", "mt_multiplayer_fd"),
            (neq, ":mission_template_id", "mt_multiplayer_sg"),
            (val_add, ":option_index", 1), #max round time
          (try_end),
          (eq, ":option_index", 12),
          (assign, reg0, "$g_multiplayer_round_max_seconds"),
          (set_trigger_result, 1),
        (else_try),
          (try_begin),
            (neq, ":mission_template_id", "mt_multiplayer_bt"),
            (neq, ":mission_template_id", "mt_multiplayer_fd"),
            (val_add, ":option_index", 1), #respawn as bot
          (try_end),
          (eq, ":option_index", 13),
          (assign, reg0, "$g_multiplayer_player_respawn_as_bot"),
          (set_trigger_result, 1),
        (else_try),
          (try_begin),
            (neq, ":mission_template_id", "mt_multiplayer_sg"),
            (val_add, ":option_index", 1), #respawn limit
          (try_end),
          (eq, ":option_index", 14),
          (assign, reg0, "$g_multiplayer_number_of_respawn_count"),
          (set_trigger_result, 1),
        (else_try),
          (eq, ":option_index", 15),
          (assign, reg0, "$g_multiplayer_game_max_points"),
          (set_trigger_result, 1),
        (else_try),
          (try_begin),
            (neq, ":mission_template_id", "mt_multiplayer_hq"),
            (val_add, ":option_index", 1), #point gained from flags
          (try_end),
          (eq, ":option_index", 16),
          (assign, reg0, "$g_multiplayer_point_gained_from_flags"),
          (set_trigger_result, 1),
        (else_try),
          (try_begin),
            (neq, ":mission_template_id", "mt_multiplayer_cf"),
            (val_add, ":option_index", 1), #point gained from capturing flag
          (try_end),
          (eq, ":option_index", 17),
          (assign, reg0, "$g_multiplayer_point_gained_from_capturing_flag"),
          (set_trigger_result, 1),
        (else_try),
          (eq, ":option_index", 18),
          (assign, reg0, "$g_multiplayer_respawn_period"),
          (set_trigger_result, 1),
        (else_try),
          (eq, ":option_index", 19),
          (assign, reg0, "$g_multiplayer_initial_gold_multiplier"),
          (set_trigger_result, 1),
        (else_try),
          (eq, ":option_index", 20),
          (assign, reg0, "$g_multiplayer_battle_earnings_multiplier"),
          (set_trigger_result, 1),
        (else_try),
          (try_begin),
            (neq, ":mission_template_id", "mt_multiplayer_bt"),
            (neq, ":mission_template_id", "mt_multiplayer_fd"),
            (neq, ":mission_template_id", "mt_multiplayer_sg"),
            (val_add, ":option_index", 1),
          (try_end),
          (eq, ":option_index", 21),
          (assign, reg0, "$g_multiplayer_round_earnings_multiplier"),
          (set_trigger_result, 1),
        (try_end),
    ]),
    
    # script_game_multiplayer_server_option_for_mission_template_to_string
    # Input: arg1 = mission_template_id, arg2 = option_index, arg3 = option_value
    # Output: s0 = option_text
    ("game_multiplayer_server_option_for_mission_template_to_string",
      [
        (store_script_param, ":mission_template_id", 1),
        (store_script_param, ":option_index", 2),
        (store_script_param, ":option_value", 3),
        (str_clear, s0),
        (try_begin),
          (eq, ":option_index", 0),
          (assign, reg1, 1),
          (str_store_string, s0, "str_team_reg1_faction"),
          (str_store_faction_name, s1, ":option_value"),
          (str_store_string, s0, "str_s0_s1"),
        (else_try),
          (eq, ":option_index", 1),
          (assign, reg1, 2),
          (str_store_string, s0, "str_team_reg1_faction"),
          (str_store_faction_name, s1, ":option_value"),
          (str_store_string, s0, "str_s0_s1"),
        (else_try),
          (eq, ":option_index", 2),
          (assign, reg1, 1),
          (str_store_string, s0, "str_number_of_bots_in_team_reg1"),
          (assign, reg0, ":option_value"),
          (str_store_string, s0, "str_s0_reg0"),
        (else_try),
          (eq, ":option_index", 3),
          (assign, reg1, 2),
          (str_store_string, s0, "str_number_of_bots_in_team_reg1"),
          (assign, reg0, ":option_value"),
          (str_store_string, s0, "str_s0_reg0"),
        (else_try),
          (eq, ":option_index", 4),
          (str_store_string, s0, "str_allow_friendly_fire"),
          (try_begin),
            (eq, ":option_value", 0),
            (str_store_string, s1, "str_no_wo_dot"),
          (else_try),
            (str_store_string, s1, "str_yes_wo_dot"),
          (try_end),
          (str_store_string, s0, "str_s0_s1"),
        (else_try),
          (eq, ":option_index", 5),
          (str_store_string, s0, "str_allow_melee_friendly_fire"),
          (try_begin),
            (eq, ":option_value", 0),
            (str_store_string, s1, "str_no_wo_dot"),
          (else_try),
            (str_store_string, s1, "str_yes_wo_dot"),
          (try_end),
          (str_store_string, s0, "str_s0_s1"),
        (else_try),
          (eq, ":option_index", 6),
          (str_store_string, s0, "str_friendly_fire_damage_self_ratio"),
          (assign, reg0, ":option_value"),
          (str_store_string, s0, "str_s0_reg0"),
        (else_try),
          (eq, ":option_index", 7),
          (str_store_string, s0, "str_friendly_fire_damage_friend_ratio"),
          (assign, reg0, ":option_value"),
          (str_store_string, s0, "str_s0_reg0"),
        (else_try),
          (eq, ":option_index", 8),
          (str_store_string, s0, "str_spectator_camera"),
          (try_begin),
            (eq, ":option_value", 0),
            (str_store_string, s1, "str_free"),
          (else_try),
            (eq, ":option_value", 1),
            (str_store_string, s1, "str_stick_to_any_player"),
          (else_try),
            (eq, ":option_value", 2),
            (str_store_string, s1, "str_stick_to_team_members"),
          (else_try),
            (str_store_string, s1, "str_stick_to_team_members_view"),
          (try_end),
          (str_store_string, s0, "str_s0_s1"),
        (else_try),
          (eq, ":option_index", 9),
          (str_store_string, s0, "str_control_block_direction"),
          (try_begin),
            (eq, ":option_value", 0),
            (str_store_string, s1, "str_automatic"),
          (else_try),
            (str_store_string, s1, "str_by_mouse_movement"),
          (try_end),
          (str_store_string, s0, "str_s0_s1"),
        (else_try),
          (eq, ":option_index", 10),
          (str_store_string, s0, "str_combat_speed"),
          (try_begin),
            (eq, ":option_value", 0),
            (str_store_string, s1, "str_combat_speed_0"),
          (else_try),
            (eq, ":option_value", 1),
            (str_store_string, s1, "str_combat_speed_1"),
          (else_try),
            (eq, ":option_value", 2),
            (str_store_string, s1, "str_combat_speed_2"),
          (else_try),
            (eq, ":option_value", 3),
            (str_store_string, s1, "str_combat_speed_3"),
          (else_try),
            (str_store_string, s1, "str_combat_speed_4"),
          (try_end),
          (str_store_string, s0, "str_s0_s1"),
        (else_try),
          (try_begin),
            (eq, ":mission_template_id", "mt_multiplayer_hq"),
            (val_add, ":option_index", 1), #max game time
          (try_end),
          (eq, ":option_index", 11),
          (str_store_string, s0, "str_map_time_limit"),
          (assign, reg0, ":option_value"),
          (str_store_string, s0, "str_s0_reg0"),
        (else_try),
          (try_begin),
            (neq, ":mission_template_id", "mt_multiplayer_bt"),
            (neq, ":mission_template_id", "mt_multiplayer_fd"),
            (neq, ":mission_template_id", "mt_multiplayer_sg"),
            (val_add, ":option_index", 1), #max round time
          (try_end),
          (eq, ":option_index", 12),
          (str_store_string, s0, "str_round_time_limit"),
          (assign, reg0, ":option_value"),
          (str_store_string, s0, "str_s0_reg0"),
        (else_try),
          (try_begin),
            (neq, ":mission_template_id", "mt_multiplayer_bt"),
            (neq, ":mission_template_id", "mt_multiplayer_fd"),
            (val_add, ":option_index", 1), #respawn as bot
          (try_end),
          (eq, ":option_index", 13),
          (str_store_string, s0, "str_players_take_control_of_a_bot_after_death"),
          (try_begin),
            (eq, ":option_value", 0),
            (str_store_string, s1, "str_no_wo_dot"),
          (else_try),
            (str_store_string, s1, "str_yes_wo_dot"),
          (try_end),
          (str_store_string, s0, "str_s0_s1"),
        (else_try),
          (try_begin),
            (neq, ":mission_template_id", "mt_multiplayer_sg"),
            (val_add, ":option_index", 1), #respawn limit
          (try_end),
          (eq, ":option_index", 14),
          (str_store_string, s0, "str_defender_spawn_count_limit"),
          (try_begin),
            (eq, ":option_value", 0),
            (str_store_string, s1, "str_unlimited"),
          (else_try),
            (assign, reg1, ":option_value"),
            (str_store_string, s1, "str_reg1"),
          (try_end),
          (str_store_string, s0, "str_s0_s1"),
        (else_try),
          (eq, ":option_index", 15),
          (str_store_string, s0, "str_team_points_limit"),
          (assign, reg0, ":option_value"),
          (str_store_string, s0, "str_s0_reg0"),
        (else_try),
          (try_begin),
            (neq, ":mission_template_id", "mt_multiplayer_hq"),
            (val_add, ":option_index", 1), #point gained from flags
          (try_end),
          (eq, ":option_index", 16),
          (str_store_string, s0, "str_point_gained_from_flags"),
          (assign, reg0, ":option_value"),
          (str_store_string, s0, "str_s0_reg0"),
        (else_try),
          (try_begin),
            (neq, ":mission_template_id", "mt_multiplayer_cf"),
            (val_add, ":option_index", 1), #point gained from capturing flag
          (try_end),
          (eq, ":option_index", 17),
          (str_store_string, s0, "str_point_gained_from_capturing_flag"),
          (assign, reg0, ":option_value"),
          (str_store_string, s0, "str_s0_reg0"),
        (else_try),
          (eq, ":option_index", 18),
          (str_store_string, s0, "str_respawn_period"),
          (assign, reg0, ":option_value"),
          (str_store_string, s0, "str_s0_reg0"),
        (else_try),
          (eq, ":option_index", 19),
          (str_store_string, s0, "str_initial_gold_multiplier"),
          (assign, reg0, ":option_value"),
          (str_store_string, s0, "str_s0_reg0"),
        (else_try),
          (eq, ":option_index", 20),
          (str_store_string, s0, "str_battle_earnings_multiplier"),
          (assign, reg0, ":option_value"),
          (str_store_string, s0, "str_s0_reg0"),
        (else_try),
          (try_begin),
            (neq, ":mission_template_id", "mt_multiplayer_bt"),
            (neq, ":mission_template_id", "mt_multiplayer_fd"),
            (neq, ":mission_template_id", "mt_multiplayer_sg"),
            (val_add, ":option_index", 1),
          (try_end),
          (eq, ":option_index", 21),
          (str_store_string, s0, "str_round_earnings_multiplier"),
          (assign, reg0, ":option_value"),
          (str_store_string, s0, "str_s0_reg0"),
        (try_end),
    ]),
    
    # script_cf_multiplayer_team_is_available
    # Input: arg1 = player_no, arg2 = team_no
    # Output: none, true or false
    ("cf_multiplayer_team_is_available",
      [
        (store_script_param, ":player_no", 1),
        (store_script_param, ":team_no", 2),
        (assign, ":continue_change_team", 1),
        (try_begin),
          (neq, "$g_multiplayer_game_type", multiplayer_game_type_deathmatch),
          (neq, "$g_multiplayer_game_type", multiplayer_game_type_duel),
          (is_between, ":team_no", 0, multi_team_spectator),
          (neg|teams_are_enemies, ":team_no", ":team_no"), #checking if it is a deathmatch or not
          (assign, ":continue_change_team", 0),
          #counting number of players for team balance checks
          (assign, ":number_of_players_at_team_1", 0),
          (assign, ":number_of_players_at_team_2", 0),
          (get_max_players, ":num_players"),
          (try_for_range, ":cur_player", 0, ":num_players"),
            (player_is_active, ":cur_player"),
            (neq, ":cur_player", ":player_no"),
            (player_get_team_no, ":player_team", ":cur_player"),
            (try_begin),
              (eq, ":player_team", 0),
              (val_add, ":number_of_players_at_team_1", 1),
            (else_try),
              (eq, ":player_team", 1),
              (val_add, ":number_of_players_at_team_2", 1),
            (try_end),
          (try_end),
          (store_sub, ":difference_of_number_of_players", ":number_of_players_at_team_1", ":number_of_players_at_team_2"),
          
          (try_begin),
            (ge, ":difference_of_number_of_players", 0),
            (val_add, ":difference_of_number_of_players", 1),
          (else_try),
            (val_add, ":difference_of_number_of_players", -1),
          (try_end),
          
          (try_begin),
            (eq, ":team_no", 0),
            (lt, ":difference_of_number_of_players", "$g_multiplayer_auto_team_balance_limit"),
            (assign, ":continue_change_team", 1),
          (else_try),
            (eq, ":team_no", 1),
            (store_mul, ":checked_value", "$g_multiplayer_auto_team_balance_limit", -1),
            (gt, ":difference_of_number_of_players", ":checked_value"),
            (assign, ":continue_change_team", 1),
          (try_end),
        (try_end),
        (eq, ":continue_change_team", 1),
    ]),
    
    # script_find_number_of_agents_constant
    # Input: none
    # Output: reg0 = 100xconstant (100..500)
    ("find_number_of_agents_constant",
      [
        (assign, ":num_dead_or_alive_agents", 0),
        
        (try_for_agents, ":cur_agent"),
          (agent_is_human, ":cur_agent"),
          (val_add, ":num_dead_or_alive_agents", 1),
        (try_end),
        
        (try_begin),
          (le, ":num_dead_or_alive_agents", 2), #2
          (assign, reg0, 100),
        (else_try),
          (le, ":num_dead_or_alive_agents", 4), #2+2
          (assign, reg0, 140),
        (else_try),
          (le, ":num_dead_or_alive_agents", 7), #2+2+3
          (assign, reg0, 180),
        (else_try),
          (le, ":num_dead_or_alive_agents", 11), #2+2+3+4
          (assign, reg0, 220),
        (else_try),
          (le, ":num_dead_or_alive_agents", 17), #2+2+3+4+6
          (assign, reg0, 260),
        (else_try),
          (le, ":num_dead_or_alive_agents", 25), #2+2+3+4+6+8
          (assign, reg0, 300),
        (else_try),
          (le, ":num_dead_or_alive_agents", 36), #2+2+3+4+6+8+11
          (assign, reg0, 340),
        (else_try),
          (le, ":num_dead_or_alive_agents", 50), #2+2+3+4+6+8+11+14
          (assign, reg0, 380),
        (else_try),
          (le, ":num_dead_or_alive_agents", 68), #2+2+3+4+6+8+11+14+18
          (assign, reg0, 420),
        (else_try),
          (le, ":num_dead_or_alive_agents", 91), #2+2+3+4+6+8+11+14+18+23
          (assign, reg0, 460),
        (else_try),
          (assign, reg0, 500),
        (try_end),
    ]),
    
    # script_game_multiplayer_event_duel_offered
    # Input: arg1 = agent_no
    # Output: none
    ("game_multiplayer_event_duel_offered",
      [
        (store_script_param, ":agent_no", 1),
        (get_player_agent_no, ":player_agent_no"),
        (try_begin),
          (agent_is_active, ":player_agent_no"),
          (this_or_next|agent_slot_eq, ":player_agent_no", slot_agent_in_duel_with, -1),
          (agent_check_offer_from_agent, ":player_agent_no", ":agent_no"),
          (neg|agent_slot_eq, ":player_agent_no", slot_agent_in_duel_with, ":agent_no"), #don't allow spamming duel offers during countdown
          (multiplayer_send_int_to_server, multiplayer_event_offer_duel, ":agent_no"),
          (agent_get_player_id, ":player_no", ":agent_no"),
          (try_begin),
            (player_is_active, ":player_no"),
            (str_store_player_username, s0, ":player_no"),
          (else_try),
            (str_store_agent_name, s0, ":agent_no"),
          (try_end),
          (display_message, "str_a_duel_request_is_sent_to_s0"),
        (try_end),
    ]),
    
    # script_game_get_multiplayer_game_type_enum
    # Input: none
    # Output: reg0:first type, reg1:type count
    ("game_get_multiplayer_game_type_enum",
      [
        (assign, reg0, multiplayer_game_type_deathmatch),
        (assign, reg1, multiplayer_num_game_types),
    ]),
    
    # script_game_multiplayer_get_game_type_mission_template
    # Input: arg1 = game_type
    # Output: mission_template
    ("game_multiplayer_get_game_type_mission_template",
      [
        (assign, ":selected_mt", -1),
        (store_script_param, ":game_type", 1),
        (try_begin),
          (eq, ":game_type", multiplayer_game_type_deathmatch),
          (assign, ":selected_mt", "mt_multiplayer_dm"),
        (else_try),
          (eq, ":game_type", multiplayer_game_type_team_deathmatch),
          (assign, ":selected_mt", "mt_multiplayer_tdm"),
        (else_try),
          (eq, ":game_type", multiplayer_game_type_battle),
          (assign, ":selected_mt", "mt_multiplayer_bt"),
        (else_try),
          (eq, ":game_type", multiplayer_game_type_destroy),
          (assign, ":selected_mt", "mt_multiplayer_fd"),
        (else_try),
          (eq, ":game_type", multiplayer_game_type_capture_the_flag),
          (assign, ":selected_mt", "mt_multiplayer_cf"),
        (else_try),
          (eq, ":game_type", multiplayer_game_type_headquarters),
          (assign, ":selected_mt", "mt_multiplayer_hq"),
        (else_try),
          (eq, ":game_type", multiplayer_game_type_siege),
          (assign, ":selected_mt", "mt_multiplayer_sg"),
        (else_try),
          (eq, ":game_type", multiplayer_game_type_duel),
          (assign, ":selected_mt", "mt_multiplayer_duel"),
        (try_end),
        (assign, reg0, ":selected_mt"),
    ]),
    
    # script_multiplayer_get_mission_template_game_type
    # Input: arg1 = mission_template_no
    # Output: game_type
    ("multiplayer_get_mission_template_game_type",
      [
        (store_script_param, ":mission_template_no", 1),
        (assign, ":game_type", -1),
        (try_begin),
          (eq, ":mission_template_no", "mt_multiplayer_dm"),
          (assign, ":game_type", multiplayer_game_type_deathmatch),
        (else_try),
          (eq, ":mission_template_no", "mt_multiplayer_tdm"),
          (assign, ":game_type", multiplayer_game_type_team_deathmatch),
        (else_try),
          (eq, ":mission_template_no", "mt_multiplayer_bt"),
          (assign, ":game_type", multiplayer_game_type_battle),
        (else_try),
          (eq, ":mission_template_no", "mt_multiplayer_fd"),
          (assign, ":game_type", multiplayer_game_type_destroy),
        (else_try),
          (eq, ":mission_template_no", "mt_multiplayer_cf"),
          (assign, ":game_type", multiplayer_game_type_capture_the_flag),
        (else_try),
          (eq, ":mission_template_no", "mt_multiplayer_hq"),
          (assign, ":game_type", multiplayer_game_type_headquarters),
        (else_try),
          (eq, ":mission_template_no", "mt_multiplayer_sg"),
          (assign, ":game_type", multiplayer_game_type_siege),
        (else_try),
          (eq, ":mission_template_no", "mt_multiplayer_duel"),
          (assign, ":game_type", multiplayer_game_type_duel),
        (try_end),
        (assign, reg0, ":game_type"),
    ]),
    
    
    # script_multiplayer_fill_available_factions_combo_button
    # Input: arg1 = overlay_id, arg2 = selected_faction_no, arg3 = opposite_team_selected_faction_no
    # Output: none
    ("multiplayer_fill_available_factions_combo_button",
      [
        (store_script_param, ":overlay_id", 1),
        (store_script_param, ":selected_faction_no", 2),
        ##     (store_script_param, ":opposite_team_selected_faction_no", 3),
        ##     (try_for_range, ":cur_faction", "fac_kingdom_1", "fac_kingdoms_end"),
        ##       (try_begin),
        ##         (eq, ":opposite_team_selected_faction_no", ":cur_faction"),
        ##         (try_begin),
        ##           (gt, ":selected_faction_no", ":opposite_team_selected_faction_no"),
        ##           (val_sub, ":selected_faction_no", 1),
        ##         (try_end),
        ##       (else_try),
        ##         (str_store_faction_name, s0, ":cur_faction"),
        ##         (overlay_add_item, ":overlay_id", s0),
        ##       (try_end),
        ##     (try_end),
        ##     (val_sub, ":selected_faction_no", "fac_kingdom_1"),
        ##     (overlay_set_val, ":overlay_id", ":selected_faction_no"),
        (try_for_range, ":cur_faction", npc_kingdoms_begin, npc_kingdoms_end),
          (str_store_faction_name, s0, ":cur_faction"),
          (overlay_add_item, ":overlay_id", s0),
        (try_end),
        (val_sub, ":selected_faction_no", "fac_kingdom_1"),
        (overlay_set_val, ":overlay_id", ":selected_faction_no"),
    ]),
    
    
    # script_multiplayer_get_troop_class
    # Input: arg1 = troop_no
    # Output: reg0: troop_class
    ("multiplayer_get_troop_class",
      [
        (store_script_param_1, ":troop_no"),
        (assign, ":troop_class", multi_troop_class_other),
        (try_begin),
          (this_or_next|eq, ":troop_no", "trp_vaegir_archer_multiplayer"),
          (this_or_next|eq, ":troop_no", "trp_nord_archer_multiplayer"),
          (eq, ":troop_no", "trp_sarranid_archer_multiplayer"),
          (assign, ":troop_class", multi_troop_class_archer),
        (else_try),
          (this_or_next|eq, ":troop_no", "trp_swadian_man_at_arms_multiplayer"),
          (this_or_next|eq, ":troop_no", "trp_nord_scout_multiplayer"),
          (this_or_next|eq, ":troop_no", "trp_rhodok_horseman_multiplayer"),
          (this_or_next|eq, ":troop_no", "trp_sarranid_mamluke_multiplayer"),
          (eq, ":troop_no", "trp_vaegir_horseman_multiplayer"),
          (assign, ":troop_class", multi_troop_class_cavalry),
        (else_try),
          (eq, ":troop_no", "trp_khergit_veteran_horse_archer_multiplayer"),
          (assign, ":troop_class", multi_troop_class_mounted_archer),
          #     (else_try),
          #       (eq, ":troop_no", "trp_swadian_mounted_crossbowman_multiplayer"),
          #       (assign, ":troop_class", multi_troop_class_mounted_crossbowman),
        (else_try),
          (this_or_next|eq, ":troop_no", "trp_swadian_crossbowman_multiplayer"),
          (eq, ":troop_no", "trp_rhodok_veteran_crossbowman_multiplayer"),
          (assign, ":troop_class", multi_troop_class_crossbowman),
        (else_try),
          (this_or_next|eq, ":troop_no", "trp_swadian_infantry_multiplayer"),
          (this_or_next|eq, ":troop_no", "trp_sarranid_footman_multiplayer"),
          (eq, ":troop_no", "trp_nord_veteran_multiplayer"),
          (assign, ":troop_class", multi_troop_class_infantry),
        (else_try),
          (eq, ":troop_no", "trp_vaegir_spearman_multiplayer"),
          (assign, ":troop_class", multi_troop_class_spearman),
        (try_end),
        (assign, reg0, ":troop_class"),
    ]),
    
    #script_multiplayer_clear_player_selected_items
    # Input: arg1 = player_no
    # Output: none
    ("multiplayer_clear_player_selected_items",
      [
        (store_script_param, ":player_no", 1),
        (try_for_range, ":slot_no", slot_player_selected_item_indices_begin, slot_player_selected_item_indices_end),
          (player_set_slot, ":player_no", ":slot_no", -1),
        (try_end),
    ]),
    
    
    #script_multiplayer_init_player_slots
    # Input: arg1 = player_no
    # Output: none
    ("multiplayer_init_player_slots",
      [
        (store_script_param, ":player_no", 1),
        (call_script, "script_multiplayer_clear_player_selected_items", ":player_no"),
        (player_set_slot, ":player_no", slot_player_spawned_this_round, 0),
        (player_set_slot, ":player_no", slot_player_last_rounds_used_item_earnings, 0),
        (player_set_slot, ":player_no", slot_player_poll_disabled_until_time, 0),
        
        (player_set_slot, ":player_no", slot_player_bot_type_1_wanted, 0),
        (player_set_slot, ":player_no", slot_player_bot_type_2_wanted, 0),
        (player_set_slot, ":player_no", slot_player_bot_type_3_wanted, 0),
        (player_set_slot, ":player_no", slot_player_bot_type_4_wanted, 0),
    ]),
    
    #script_multiplayer_initialize_belfry_wheel_rotations
    # Input: none
    # Output: none
    ("multiplayer_initialize_belfry_wheel_rotations",
      [
        ##    (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_a"),
        ##    (try_for_range, ":belfry_no", 0, ":num_belfries"),
        ##      (store_mul, ":wheel_no", ":belfry_no", 3),
        ##      (scene_prop_get_instance, ":belfry_wheel_1_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
        ##      (prop_instance_initialize_rotation_angles, ":belfry_wheel_1_scene_prop_id"),
        ##      #belfry wheel_2
        ##      (val_add, ":wheel_no", 1),
        ##      (scene_prop_get_instance, ":belfry_wheel_2_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
        ##      (prop_instance_initialize_rotation_angles, ":belfry_wheel_2_scene_prop_id"),
        ##      #belfry wheel_3
        ##      (val_add, ":wheel_no", 1),
        ##      (scene_prop_get_instance, ":belfry_wheel_3_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
        ##      (prop_instance_initialize_rotation_angles, ":belfry_wheel_3_scene_prop_id"),
        ##    (try_end),
        ##
        ##    (scene_prop_get_num_instances, ":num_belfries_a", "spr_belfry_a"),
        ##
        ##    (scene_prop_get_num_instances, ":num_belfries", "spr_belfry_b"),
        ##    (try_for_range, ":belfry_no", 0, ":num_belfries"),
        ##      (store_add, ":wheel_no_plus_num_belfries_a", ":wheel_no", ":num_belfries_a"),
        ##      (store_mul, ":wheel_no_plus_num_belfries_a", ":belfry_no", 3),
        ##      (scene_prop_get_instance, ":belfry_wheel_1_scene_prop_id", "spr_belfry_wheel", ":wheel_no_plus_num_belfries_a"),
        ##      (prop_instance_initialize_rotation_angles, ":belfry_wheel_1_scene_prop_id"),
        ##      #belfry wheel_2
        ##      (val_add, ":wheel_no_plus_num_belfries_a", 1),
        ##      (scene_prop_get_instance, ":belfry_wheel_2_scene_prop_id", "spr_belfry_wheel", ":wheel_no_plus_num_belfries_a"),
        ##      (prop_instance_initialize_rotation_angles, ":belfry_wheel_2_scene_prop_id"),
        ##      #belfry wheel_3
        ##      (val_add, ":wheel_no_plus_num_belfries_a", 1),
        ##      (scene_prop_get_instance, ":belfry_wheel_3_scene_prop_id", "spr_belfry_wheel", ":wheel_no_plus_num_belfries_a"),
        ##      (prop_instance_initialize_rotation_angles, ":belfry_wheel_3_scene_prop_id"),
        ##    (try_end),
        
        (scene_prop_get_num_instances, ":num_wheel", "spr_belfry_wheel"),
        (try_for_range, ":wheel_no", 0, ":num_wheel"),
          (scene_prop_get_instance, ":wheel_id", "spr_belfry_wheel", ":wheel_no"),
          (prop_instance_initialize_rotation_angles, ":wheel_id"),
        (try_end),
        
        (scene_prop_get_num_instances, ":num_winch", "spr_winch"),
        (try_for_range, ":winch_no", 0, ":num_winch"),
          (scene_prop_get_instance, ":winch_id", "spr_winch", ":winch_no"),
          (prop_instance_initialize_rotation_angles, ":winch_id"),
        (try_end),
        
        (scene_prop_get_num_instances, ":num_winch_b", "spr_winch_b"),
        (try_for_range, ":winch_b_no", 0, ":num_winch_b"),
          (scene_prop_get_instance, ":winch_b_id", "spr_winch_b", ":winch_b_no"),
          (prop_instance_initialize_rotation_angles, ":winch_b_id"),
        (try_end),
    ]),
    
    #script_send_open_close_information_of_object
    # Input: arg1 = mission_object_id
    # Output: none
    ("send_open_close_information_of_object",
      [
        (store_script_param, ":player_no", 1),
        (store_script_param, ":scene_prop_no", 2),
        
        (scene_prop_get_num_instances, ":num_instances", ":scene_prop_no"),
        
        (try_for_range, ":instance_no", 0, ":num_instances"),
          (scene_prop_get_instance, ":instance_id", ":scene_prop_no", ":instance_no"),
          (scene_prop_get_slot, ":opened_or_closed", ":instance_id", scene_prop_open_or_close_slot),
          (try_begin),
            (eq, ":opened_or_closed", 1),
            (multiplayer_send_int_to_player, ":player_no", multiplayer_event_set_scene_prop_open_or_close, ":instance_id"),
          (try_end),
        (try_end),
    ]),
    
    #script_multiplayer_send_initial_information
    # Input: arg1 = player_no
    # Output: none
    ("multiplayer_send_initial_information",
      [
        (store_script_param, ":player_no", 1),
        
        (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_num_bots_in_team, 1, "$g_multiplayer_num_bots_team_1"),
        (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_return_num_bots_in_team, 2, "$g_multiplayer_num_bots_team_2"),
        (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_auto_team_balance_limit, "$g_multiplayer_auto_team_balance_limit"),
        (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_num_bots_voteable, "$g_multiplayer_num_bots_voteable"),
        (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_factions_voteable, "$g_multiplayer_factions_voteable"),
        (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_maps_voteable, "$g_multiplayer_maps_voteable"),
        (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_kick_voteable, "$g_multiplayer_kick_voteable"),
        (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_ban_voteable, "$g_multiplayer_ban_voteable"),
        (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_allow_player_banners, "$g_multiplayer_allow_player_banners"),
        (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_force_default_armor, "$g_multiplayer_force_default_armor"),
        (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_disallow_ranged_weapons, "$g_multiplayer_disallow_ranged_weapons"),
        (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_respawn_period, "$g_multiplayer_respawn_period"),
        (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_round_max_seconds, "$g_multiplayer_round_max_seconds"),
        (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_game_type, "$g_multiplayer_game_type"),
        (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_player_respawn_as_bot, "$g_multiplayer_player_respawn_as_bot"),
        
        (store_mission_timer_a, ":mission_timer"),
        (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_server_mission_timer_while_player_joined, ":mission_timer"),
        
        (try_begin),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_return_respawn_count, "$g_multiplayer_number_of_respawn_count"),
        (try_end),
        
        (try_for_agents, ":cur_agent"), #send if any agent is carrying any scene object
          (agent_is_human, ":cur_agent"),
          (agent_get_attached_scene_prop, ":attached_scene_prop", ":cur_agent"),
          (ge, ":attached_scene_prop", 0),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_attached_scene_prop, ":cur_agent", ":attached_scene_prop"),
        (try_end),
        
        (call_script, "script_send_open_close_information_of_object", ":player_no", "spr_siege_ladder_move_6m"),
        (call_script, "script_send_open_close_information_of_object", ":player_no", "spr_siege_ladder_move_8m"),
        (call_script, "script_send_open_close_information_of_object", ":player_no", "spr_siege_ladder_move_10m"),
        (call_script, "script_send_open_close_information_of_object", ":player_no", "spr_siege_ladder_move_12m"),
        (call_script, "script_send_open_close_information_of_object", ":player_no", "spr_siege_ladder_move_14m"),
        (call_script, "script_send_open_close_information_of_object", ":player_no", "spr_winch_b"),
        (call_script, "script_send_open_close_information_of_object", ":player_no", "spr_castle_e_sally_door_a"),
        (call_script, "script_send_open_close_information_of_object", ":player_no", "spr_castle_f_sally_door_a"),
        (call_script, "script_send_open_close_information_of_object", ":player_no", "spr_earth_sally_gate_left"),
        (call_script, "script_send_open_close_information_of_object", ":player_no", "spr_earth_sally_gate_right"),
        (call_script, "script_send_open_close_information_of_object", ":player_no", "spr_viking_keep_destroy_sally_door_left"),
        (call_script, "script_send_open_close_information_of_object", ":player_no", "spr_viking_keep_destroy_sally_door_right"),
        (call_script, "script_send_open_close_information_of_object", ":player_no", "spr_castle_f_door_a"),
        (call_script, "script_send_open_close_information_of_object", ":player_no", "spr_door_destructible"),
        (call_script, "script_send_open_close_information_of_object", ":player_no", "spr_castle_f_door_b"),
        
        (try_begin),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
          
          (store_mission_timer_a, ":current_time"),
          (val_sub, ":current_time", "$g_round_start_time"),
          (val_mul, ":current_time", -1),
          
          (multiplayer_send_int_to_player, ":player_no", multiplayer_event_set_round_start_time, ":current_time"),
        (else_try),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_capture_the_flag),
          #if game type is capture the flag send current flag situations to each player.
          (team_get_slot, ":flag_situation_team_1", 0, slot_team_flag_situation),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_flag_situation, 0, ":flag_situation_team_1"),
          (team_get_slot, ":flag_situation_team_2", 1, slot_team_flag_situation),
          (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_team_flag_situation, 1, ":flag_situation_team_2"),
        (else_try),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
          #if game type is headquarters send number of agents placed around each pole's around to player.
          (try_for_range, ":flag_no", 0, "$g_number_of_flags"),
            (assign, ":number_of_agents_around_flag_team_1", 0),
            (assign, ":number_of_agents_around_flag_team_2", 0),
            
            (scene_prop_get_instance, ":pole_id", "spr_headquarters_pole_code_only", ":flag_no"),
            (prop_instance_get_position, pos0, ":pole_id"), #pos0 holds pole position.
            
            (try_for_agents, ":cur_agent"),
              (agent_is_human, ":cur_agent"),
              (agent_is_alive, ":cur_agent"),
              (neg|agent_is_non_player, ":cur_agent"),
              (agent_get_team, ":cur_agent_team", ":cur_agent"),
              (agent_get_position, pos1, ":cur_agent"), #pos1 holds agent's position.
              (get_sq_distance_between_positions, ":squared_dist", pos0, pos1),
              (get_sq_distance_between_position_heights, ":squared_height_dist", pos0, pos1),
              (val_add, ":squared_dist", ":squared_height_dist"),
              (lt, ":squared_dist", multi_headquarters_max_distance_sq_to_raise_flags),
              (try_begin),
                (eq, ":cur_agent_team", 0),
                (val_add, ":number_of_agents_around_flag_team_1", 1),
              (else_try),
                (eq, ":cur_agent_team", 1),
                (val_add, ":number_of_agents_around_flag_team_2", 1),
              (try_end),
            (try_end),
            
            (store_mul, ":current_owner_code", ":number_of_agents_around_flag_team_1", 100),
            (val_add, ":current_owner_code", ":number_of_agents_around_flag_team_2"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_num_agents_around_flag, ":flag_no", ":current_owner_code"),
          (try_end),
          
          #if game type is headquarters send owners of each pole to player.
          (assign, "$g_placing_initial_flags", 1),
          (try_for_range, ":cur_flag", 0, "$g_number_of_flags"),
            (store_add, ":cur_flag_slot", multi_data_flag_owner_begin, ":cur_flag"),
            (troop_get_slot, ":cur_flag_owner", "trp_multiplayer_data", ":cur_flag_slot"),
            (store_mul, ":cur_flag_owner_code", ":cur_flag_owner", 100),
            (val_add, ":cur_flag_owner_code", ":cur_flag_owner"),
            (val_add, ":cur_flag_owner_code", 1),
            (val_mul, ":cur_flag_owner_code", -1),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_change_flag_owner, ":cur_flag", ":cur_flag_owner_code"),
          (try_end),
          (assign, "$g_placing_initial_flags", 0),
        (try_end),
        
        #(multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_set_day_time, "$g_round_day_time"),
    ]),
    
    #script_multiplayer_remove_headquarters_flags
    # Input: none
    # Output: none
    ("multiplayer_remove_headquarters_flags",
      [
        (store_add, ":end_cond", "spr_headquarters_flag_gray", 1),
        (try_for_range, ":headquarters_flag_no", "spr_headquarters_flag_red", ":end_cond"),
          (replace_scene_props, ":headquarters_flag_no", "spr_empty"),
        (try_end),
    ]),
    
    #script_multiplayer_remove_destroy_mod_targets
    # Input: none
    # Output: none
    ("multiplayer_remove_destroy_mod_targets",
      [
        (replace_scene_props, "spr_catapult_destructible", "spr_empty"),
        (replace_scene_props, "spr_trebuchet_destructible", "spr_empty"),
    ]),
    
    #script_multiplayer_init_mission_variables
    ("multiplayer_init_mission_variables",
      [
        (assign, "$g_multiplayer_team_1_first_spawn", 1),
        (assign, "$g_multiplayer_team_2_first_spawn", 1),
        (assign, "$g_multiplayer_poll_running", 0),
        ##     (assign, "$g_multiplayer_show_poll_when_suitable", 0),
        (assign, "$g_waiting_for_confirmation_to_terminate", 0),
        (assign, "$g_confirmation_result", 0),
        (assign, "$g_team_balance_next_round", 0),
        (team_get_faction, "$g_multiplayer_team_1_faction", 0),
        (team_get_faction, "$g_multiplayer_team_2_faction", 1),
        (assign, "$g_multiplayer_next_team_1_faction", "$g_multiplayer_team_1_faction"),
        (assign, "$g_multiplayer_next_team_2_faction", "$g_multiplayer_team_2_faction"),
        
        (assign, "$g_multiplayer_bot_type_1_wanted", 0),
        (assign, "$g_multiplayer_bot_type_2_wanted", 0),
        (assign, "$g_multiplayer_bot_type_3_wanted", 0),
        (assign, "$g_multiplayer_bot_type_4_wanted", 0),
        
        (call_script, "script_music_set_situation_with_culture", mtf_sit_multiplayer_fight),
    ]),
]
