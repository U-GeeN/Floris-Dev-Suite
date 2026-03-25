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



simple_triggers_part3 = [


  (3, #check to see if player's court has been captured
   [
     ##diplomacy start+ The player might be the ruler of another kingdom
     (assign, ":save_reg0", reg0),
	 (assign, ":alt_led_faction", "fac_player_supporters_faction"),
	 (try_begin),
		(is_between, "$players_kingdom", npc_kingdoms_begin, npc_kingdoms_end),
		(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
	    (ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
		(assign, ":alt_led_faction", "$players_kingdom"),
	 (try_end),
	 ##diplomacy end+
     (try_begin), #The old court has been lost
     ##diplomacy begin
       (is_between, "$g_player_court", centers_begin, centers_end),
				##Floris MTT begin
				(troop_get_slot,":woman_peasant","$troop_trees",slot_woman_peasant),
				(party_slot_eq, "$g_player_court", slot_village_infested_by_bandits, ":woman_peasant"),
				##Floris MTT end
       (call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
     (else_try),
     ##diplomacy end
       (is_between, "$g_player_court", centers_begin, centers_end),
       (store_faction_of_party, ":court_faction", "$g_player_court"),
       (neq, ":court_faction", "fac_player_supporters_faction"),
	   ##diplomacy start+ The player might be ruler of a faction other than fac_player_supporters_faction
	   (neq, ":court_faction", ":alt_led_faction"),
	   ##diplomacy end+
       (call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
     (else_try),	#At least one new court has been found
       (lt, "$g_player_court", centers_begin),
       #Will by definition not active until a center is taken by the player faction
       #Player minister must have been appointed at some point
       (this_or_next|faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
		(gt, "$g_player_minister", 0),

       (assign, ":center_found", 0),
       (try_for_range, ":walled_center", walled_centers_begin, walled_centers_end),
         (eq, ":center_found", 0),
         (store_faction_of_party, ":court_faction", ":walled_center"),
		   ##diplomacy start+ The player might be ruler of a faction other than fac_player_supporters_faction
		   (this_or_next|eq, ":court_faction", ":alt_led_faction"),
		   ##diplomacy end+
         (eq, ":court_faction", "fac_player_supporters_faction"),
         (assign, ":center_found", ":walled_center"),
       (try_end),
       (ge, ":center_found", 1),
       (call_script, "script_add_notification_menu", "mnu_notification_court_lost", 0, 0),
     (try_end),
     #Also, piggy-backing on this -- having bandits go to lairs and back
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
     (try_for_parties, ":bandit_party"),
       (gt, ":bandit_party", "p_spawn_points_end"),
       (party_get_template_id, ":bandit_party_template", ":bandit_party"),
       (is_between, ":bandit_party_template", ":templates_begin", ":templates_end"), ##Floris MTT begin and end; changed from bandit_party_template_begin to bandit_party_template_end ## CC
	   (party_template_get_slot, ":bandit_lair", ":bandit_party_template", slot_party_template_lair_party),
       (try_begin),#If party is active and bandit is far away, then move to location
         (gt, ":bandit_lair", "p_spawn_points_end"),
         (store_distance_to_party_from_party, ":distance", ":bandit_party", ":bandit_lair"), #this is the cause of the error
         (gt, ":distance", 30),
         #All this needs checking
         (party_set_ai_behavior, ":bandit_party", ai_bhvr_travel_to_point),
         (party_get_position, pos5, ":bandit_lair"),
         (party_set_ai_target_position, ":bandit_party", pos5),
       (else_try), #Otherwise, act freely
         (get_party_ai_behavior, ":behavior", ":bandit_party"),
         (eq, ":behavior", ai_bhvr_travel_to_point),
         (try_begin),
           (gt, ":bandit_lair", "p_spawn_points_end"),
           (store_distance_to_party_from_party, ":distance", ":bandit_party", ":bandit_lair"),
           (lt, ":distance", 3),
           (party_set_ai_behavior, ":bandit_party", ai_bhvr_patrol_party),
           (party_template_get_slot, ":spawnpoint", ":bandit_party_template", slot_party_template_lair_spawnpoint),
           (party_set_ai_object, ":bandit_party", ":spawnpoint"),
           (party_set_ai_patrol_radius, ":bandit_party", 45),
         (else_try),
           (lt, ":bandit_lair", "p_spawn_points_end"),
           (party_set_ai_behavior, ":bandit_party", ai_bhvr_patrol_party),
           (party_template_get_slot, ":spawnpoint", ":bandit_party_template", slot_party_template_lair_spawnpoint),
           (party_set_ai_object, ":bandit_party", ":spawnpoint"),
           (party_set_ai_patrol_radius, ":bandit_party", 45),
         (try_end),
       (try_end),
     (try_end),
     #Piggybacking on trigger:
     (try_begin),
       (troop_get_slot, ":betrothed", "trp_player", slot_troop_betrothed),
       (gt, ":betrothed", 0),
       (neg|check_quest_active, "qst_wed_betrothed"),
       (neg|check_quest_active, "qst_wed_betrothed_female"),
       (str_store_troop_name, s5, ":betrothed"),
       (display_message, "@Betrothal to {s5} expires"),
       (troop_set_slot, "trp_player", slot_troop_betrothed, -1),
       (troop_set_slot, ":betrothed", slot_troop_betrothed, -1),
     (try_end),
	 ##diplomacy start+
	 (assign, reg0, ":save_reg0"),#revert register
	 ##diplomacy end+
     ]),

  # Reduce renown slightly by 0.5% every week
  (7 * 24,
   [
       (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
       (store_div, ":renown_decrease", ":player_renown", 200),
       (val_sub, ":player_renown", ":renown_decrease"),
       (troop_set_slot, "trp_player", slot_troop_renown, ":player_renown"),
    ]),

  # Read books if player is resting.
  (1, [(neg|map_free),
       (gt, "$g_player_reading_book", 0),
       (player_has_item, "$g_player_reading_book"),
       (store_attribute_level, ":int", "trp_player", ca_intelligence),
       (item_get_slot, ":int_req", "$g_player_reading_book", slot_item_intelligence_requirement),
       (le, ":int_req", ":int"),
       (item_get_slot, ":book_reading_progress", "$g_player_reading_book", slot_item_book_reading_progress),
       (item_get_slot, ":book_read", "$g_player_reading_book", slot_item_book_read),
       (eq, ":book_read", 0),
      ## CC
       (assign, ":read_speed", 0),
       (try_for_range, ":other_troop", companions_begin, companions_end),
         (main_party_has_troop, ":other_troop"),
         (call_script, "script_get_book_read_slot", ":other_troop", "$g_player_reading_book"),
         (assign, ":other_slot_no", reg0),
         (troop_slot_eq, "trp_book_read", ":other_slot_no", 1),
         (val_add, ":read_speed", 1),
       (try_end),
       (val_div, ":read_speed", 4),
       (val_add, ":read_speed", 3),
       (val_add, ":book_reading_progress", ":read_speed"),
      ## CC
       (item_set_slot, "$g_player_reading_book", slot_item_book_reading_progress, ":book_reading_progress"),
       (ge, ":book_reading_progress", 1000),
       (item_set_slot, "$g_player_reading_book", slot_item_book_read, 1),
       (item_set_slot, "$g_player_reading_book", slot_item_book_reading_progress, 1000), ## CC
       (str_store_item_name, s1, "$g_player_reading_book"),
       (str_clear, s2),
       (try_begin),
         (eq, "$g_player_reading_book", "itm_book_tactics"),
         (troop_raise_skill, "trp_player", "skl_tactics", 1),
         (str_store_string, s2, "@ Your tactics skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_persuasion"),
         (troop_raise_skill, "trp_player", "skl_persuasion", 1),
         (str_store_string, s2, "@ Your persuasion skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_leadership"),
         (troop_raise_skill, "trp_player", "skl_leadership", 1),
         (str_store_string, s2, "@ Your leadership skill has increased by 1."),
      ## CC
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_prisoner_management"),
         (troop_raise_skill, "trp_player", "skl_prisoner_management", 1),
         (str_store_string, s2, "@ Your prisoner management skill has increased by 1."),
      ## CC
      ## Floris
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_bible"),
         (troop_raise_attribute, "trp_player", ca_charisma, 1),
         (str_store_string, s2, "@ Your charisma has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_necronomicon"),
         (troop_raise_skill, "trp_player", "skl_looting", 1),
         (str_store_string, s2, "@ Your looting skill has increased by 1."),
      ##
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_intelligence"),
         (troop_raise_attribute, "trp_player", ca_intelligence, 1),
         (str_store_string, s2, "@ Your intelligence has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_trade"),
         (troop_raise_skill, "trp_player", "skl_trade", 1),
         (str_store_string, s2, "@ Your trade skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_weapon_mastery"),
         (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
         (str_store_string, s2, "@ Your weapon master skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_engineering"),
         (troop_raise_skill, "trp_player", "skl_engineer", 1),
         (str_store_string, s2, "@ Your engineer skill has increased by 1."),
       (try_end),

       (unlock_achievement, ACHIEVEMENT_BOOK_WORM),

       (try_begin),
         (eq, "$g_infinite_camping", 0),
         (dialog_box, "@You have finished reading {s1}.{s2}", "@Book Read"),
       (try_end),

       (assign, "$g_player_reading_book", 0),
       ]),

# Removing cattle herds if they are way out of range
  (12, [(try_for_parties, ":cur_party"),
          (party_slot_eq, ":cur_party", slot_party_type, spt_cattle_herd),
          (store_distance_to_party_from_party, ":dist",":cur_party", "p_main_party"),
          (try_begin),
            (gt, ":dist", 30),
            (remove_party, ":cur_party"),
            (try_begin),
              #Fail quest if the party is the quest party
              (check_quest_active, "qst_move_cattle_herd"),
              (neg|check_quest_concluded, "qst_move_cattle_herd"),
              (quest_slot_eq, "qst_move_cattle_herd", slot_quest_target_party, ":cur_party"),
              (call_script, "script_fail_quest", "qst_move_cattle_herd"),
            (end_try),
          (else_try),
            (gt, ":dist", 10),
            (party_set_slot, ":cur_party", slot_cattle_driven_by_player, 0),
            (party_set_ai_behavior, ":cur_party", ai_bhvr_hold),
          (try_end),
        (try_end),
    ]),


#####!!!!!

# Village upgrade triggers

# School
  (30 * 24,
   [(try_for_range, ":cur_village", villages_begin, villages_end),
      (party_slot_eq, ":cur_village", slot_town_lord, "trp_player"),
      (party_slot_eq, ":cur_village", slot_center_has_school, 1),
      (party_get_slot, ":cur_relation", ":cur_village", slot_center_player_relation),
      (val_add, ":cur_relation", 1),
      (val_min, ":cur_relation", 100),
      (party_set_slot, ":cur_village", slot_center_player_relation, ":cur_relation"),
    (try_end),
    ]),

# Quest triggers:

# Remaining days text update
  (24, [(try_for_range, ":cur_quest", all_quests_begin, all_quests_end),
          (try_begin),
            (check_quest_active, ":cur_quest"),
            (try_begin),
              (neg|check_quest_concluded, ":cur_quest"),
              (quest_slot_ge, ":cur_quest", slot_quest_expiration_days, 1),
              (quest_get_slot, ":exp_days", ":cur_quest", slot_quest_expiration_days),
              (val_sub, ":exp_days", 1),
              (try_begin),
                (eq, ":exp_days", 0),
                (call_script, "script_abort_quest", ":cur_quest", 1),
              (else_try),
                (quest_set_slot, ":cur_quest", slot_quest_expiration_days, ":exp_days"),
                (assign, reg0, ":exp_days"),
                (add_quest_note_from_sreg, ":cur_quest", 7, "@You have {reg0} days to finish this quest.", 0),
              (try_end),
            (try_end),
          (else_try),
            (quest_slot_ge, ":cur_quest", slot_quest_dont_give_again_remaining_days, 1),
            (quest_get_slot, ":value", ":cur_quest", slot_quest_dont_give_again_remaining_days),
            (val_sub, ":value", 1),
            (quest_set_slot, ":cur_quest", slot_quest_dont_give_again_remaining_days, ":value"),
          (try_end),
        (try_end),
    ]),

# Report to army quest
  (2,
   [
     (eq, "$g_infinite_camping", 0),
     (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
     (eq, "$g_player_is_captive", 0),

	 (try_begin),
		(check_quest_active, "qst_report_to_army"),
		(faction_slot_eq, "$players_kingdom", slot_faction_marshall, -1),
		(call_script, "script_abort_quest", "qst_report_to_army", 0),
	 (try_end),

	 (faction_get_slot, ":faction_object", "$players_kingdom", slot_faction_ai_object),

     (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_default),
     (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_feast),

     (assign, ":continue", 1),
     (try_begin),
       (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_enemies_around_center),
       (this_or_next|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_center),
       (faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_raiding_village),
       (neg|is_between, ":faction_object", walled_centers_begin, walled_centers_end),
       (assign, ":continue", 0),
     (try_end),
     (eq, ":continue", 1),

	 (assign, ":kingdom_is_at_war", 0),
	 (try_for_range, ":faction", kingdoms_begin, kingdoms_end),
		(neq, ":faction", "$players_kingdom"),
		(store_relation, ":relation", ":faction", "$players_kingdom"),
		(lt, ":relation", 0),
		(assign, ":kingdom_is_at_war", 1),
	 (try_end),
	 (eq, ":kingdom_is_at_war", 1),

     (neg|check_quest_active, "qst_report_to_army"),
     (neg|check_quest_active, "qst_follow_army"),

     (neg|quest_slot_ge, "qst_report_to_army", slot_quest_dont_give_again_remaining_days, 1),
     (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
     (gt, ":faction_marshall", 0),
     (troop_get_slot, ":faction_marshall_party", ":faction_marshall", slot_troop_leaded_party),
     (gt, ":faction_marshall_party", 0),
     (party_is_active, ":faction_marshall_party"),

     (store_distance_to_party_from_party, ":distance_to_marshal", ":faction_marshall_party", "p_main_party"),
     (le, ":distance_to_marshal", 96),

     (assign, ":has_no_quests", 1),
     (try_for_range, ":cur_quest", lord_quests_begin, lord_quests_end),
       (check_quest_active, ":cur_quest"),
       (quest_slot_eq, ":cur_quest", slot_quest_giver_troop, ":faction_marshall"),
       (assign, ":has_no_quests", 0),
     (try_end),
     (eq, ":has_no_quests", 1),

     (try_for_range, ":cur_quest", lord_quests_begin_2, lord_quests_end_2),
       (check_quest_active, ":cur_quest"),
       (quest_slot_eq, ":cur_quest", slot_quest_giver_troop, ":faction_marshall"),
       (assign, ":has_no_quests", 0),
     (try_end),
     (eq, ":has_no_quests", 1),

     (try_for_range, ":cur_quest", army_quests_begin, army_quests_end),
       (check_quest_active, ":cur_quest"),
       (assign, ":has_no_quests", 0),
     (try_end),
     (eq, ":has_no_quests", 1),

     (store_character_level, ":level", "trp_player"),
     (ge, ":level", 8),
     (assign, ":cur_target_amount", 2),
     (try_for_range, ":cur_center", centers_begin, centers_end),
       (party_slot_eq, ":cur_center", slot_town_lord, "trp_player"),
       (try_begin),
         (party_slot_eq, ":cur_center", slot_party_type, spt_town),
         (val_add, ":cur_target_amount", 3),
       (else_try),
         (party_slot_eq, ":cur_center", slot_party_type, spt_castle),
         (val_add, ":cur_target_amount", 1),
       (else_try),
         (val_add, ":cur_target_amount", 1),
       (try_end),
     (try_end),

     (val_mul, ":cur_target_amount", 4),
     (val_min, ":cur_target_amount", 60),
     (quest_set_slot, "qst_report_to_army", slot_quest_giver_troop, ":faction_marshall"),
     (quest_set_slot, "qst_report_to_army", slot_quest_target_troop, ":faction_marshall"),
     (quest_set_slot, "qst_report_to_army", slot_quest_target_amount, ":cur_target_amount"),
     (quest_set_slot, "qst_report_to_army", slot_quest_expiration_days, 4),
     (quest_set_slot, "qst_report_to_army", slot_quest_dont_give_again_period, 22),
     (jump_to_menu, "mnu_kingdom_army_quest_report_to_army"),
   ]),


# Army quest initializer
  (3,
   [
     (assign, "$g_random_army_quest", -1),
     (check_quest_active, "qst_follow_army", 1),
     (is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
#Rebellion changes begin
#     (neg|is_between, "$players_kingdom", rebel_factions_begin, rebel_factions_end),
#Rebellion changes end
     (neg|faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_default),
     (faction_get_slot, ":faction_marshall", "$players_kingdom", slot_faction_marshall),
     (neq, ":faction_marshall", "trp_player"),
     (gt, ":faction_marshall", 0),
     (troop_get_slot, ":faction_marshall_party", ":faction_marshall", slot_troop_leaded_party),
     (gt, ":faction_marshall_party", 0),
     (party_is_active, ":faction_marshall_party"),
     (store_distance_to_party_from_party, ":dist", ":faction_marshall_party", "p_main_party"),
     (try_begin),
       (lt, ":dist", 15),
       (assign, "$g_player_follow_army_warnings", 0),
       (store_current_hours, ":cur_hours"),
       (faction_get_slot, ":last_offensive_time", "$players_kingdom", slot_faction_last_offensive_concluded), ##1.132
#       (faction_get_slot, ":last_offensive_time", "$players_kingdom", slot_faction_ai_last_offensive_time), ##1.131
       (store_sub, ":passed_time", ":cur_hours", ":last_offensive_time"),

       (assign, ":result", -1),
       (try_begin),
         (store_random_in_range, ":random_no", 0, 100),
         (lt, ":random_no", 30),
         (troop_slot_eq, ":faction_marshall", slot_troop_does_not_give_quest, 0),
         (try_for_range, ":unused", 0, 20), #Repeat trial twenty times
           (eq, ":result", -1),
           (store_random_in_range, ":quest_no", army_quests_begin, army_quests_end),
           (neg|quest_slot_ge, ":quest_no", slot_quest_dont_give_again_remaining_days, 1),
           (try_begin),
             (eq, ":quest_no", "qst_deliver_cattle_to_army"),
			# (eq, 1, 0), #disables temporarily
             (try_begin),
               (faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_center),
               (gt, ":passed_time", 120),#5 days
               (store_random_in_range, ":quest_target_amount", 5, 10),
               (assign, ":result","qst_deliver_cattle_to_army"),
               (quest_set_slot, ":result", slot_quest_target_amount, ":quest_target_amount"),
               (quest_set_slot, ":result", slot_quest_expiration_days, 10),
               (quest_set_slot, ":result", slot_quest_dont_give_again_period, 30),
             (try_end),
           (else_try),
             (eq, ":quest_no", "qst_join_siege_with_army"),
			 (eq, 1, 0),
             (try_begin),
               (faction_slot_eq, "$players_kingdom", slot_faction_ai_state, sfai_attacking_center),
               (faction_get_slot, ":ai_object", "$players_kingdom", slot_faction_ai_object),
               (is_between, ":ai_object", walled_centers_begin, walled_centers_end),
               (party_get_battle_opponent, ":besieged_center", ":faction_marshall_party"),
               (eq, ":besieged_center", ":ai_object"),
               #army is assaulting the center
               (assign, ":result", ":quest_no"),
               (quest_set_slot, ":result", slot_quest_target_center, ":ai_object"),
               (quest_set_slot, ":result", slot_quest_expiration_days, 2),
               (quest_set_slot, ":result", slot_quest_dont_give_again_period, 15),
             (try_end),
           (else_try),
             (eq, ":quest_no", "qst_scout_waypoints"),
             (try_begin),
               (assign, ":end_cond", 100),
               (assign, "$qst_scout_waypoints_wp_1", -1),
               (assign, "$qst_scout_waypoints_wp_2", -1),
               (assign, "$qst_scout_waypoints_wp_3", -1),
               (assign, ":continue", 0),
               (try_for_range, ":unused", 0, ":end_cond"),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_1", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (assign, "$qst_scout_waypoints_wp_1", reg0),
                 (try_end),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_2", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (neq, "$qst_scout_waypoints_wp_1", reg0),
                   (assign, "$qst_scout_waypoints_wp_2", reg0),
                 (try_end),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_3", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (neq, "$qst_scout_waypoints_wp_1", reg0),
                   (neq, "$qst_scout_waypoints_wp_2", reg0),
                   (assign, "$qst_scout_waypoints_wp_3", reg0),
                 (try_end),
                 (neq, "$qst_scout_waypoints_wp_1", "$qst_scout_waypoints_wp_2"),
                 (neq, "$qst_scout_waypoints_wp_1", "$qst_scout_waypoints_wp_2"),
                 (neq, "$qst_scout_waypoints_wp_2", "$qst_scout_waypoints_wp_3"),
                 (ge, "$qst_scout_waypoints_wp_1", 0),
                 (ge, "$qst_scout_waypoints_wp_2", 0),
                 (ge, "$qst_scout_waypoints_wp_3", 0),
                 (assign, ":end_cond", 0),
                 (assign, ":continue", 1),
               (try_end),
               (eq, ":continue", 1),
               (assign, "$qst_scout_waypoints_wp_1_visited", 0),
               (assign, "$qst_scout_waypoints_wp_2_visited", 0),
               (assign, "$qst_scout_waypoints_wp_3_visited", 0),
               (assign, ":result", "qst_scout_waypoints"),
               (quest_set_slot, ":result", slot_quest_expiration_days, 7),
               (quest_set_slot, ":result", slot_quest_dont_give_again_period, 25),
             (try_end),
           (try_end),
         (try_end),

         (try_begin),
           (neq, ":result", -1),
           (quest_set_slot, ":result", slot_quest_current_state, 0),
           (quest_set_slot, ":result", slot_quest_giver_troop, ":faction_marshall"),
           (try_begin),
             (eq, ":result", "qst_join_siege_with_army"),
             (jump_to_menu, "mnu_kingdom_army_quest_join_siege_order"),
           (else_try),
             (assign, "$g_random_army_quest", ":result"),
             (quest_set_slot, "$g_random_army_quest", slot_quest_giver_troop, ":faction_marshall"),
             (jump_to_menu, "mnu_kingdom_army_quest_messenger"),
           (try_end),
         (try_end),
       (try_end),
     (else_try),
       (val_add, "$g_player_follow_army_warnings", 1),
       (try_begin),
         (lt, "$g_player_follow_army_warnings", 15),
         (try_begin),
           (store_mod, ":follow_mod", "$g_player_follow_army_warnings", 3),
           (eq, ":follow_mod", 0),
           (str_store_troop_name_link, s1, ":faction_marshall"),
           (try_begin),
             (lt, "$g_player_follow_army_warnings", 8),
#             (display_message, "str_marshal_warning"),
           (else_try),
             (display_message, "str_marshal_warning"),
           (try_end),
         (try_end),
       (else_try),
         (jump_to_menu, "mnu_kingdom_army_follow_failed"),
       (try_end),
     (try_end),
    ]),

# Move cattle herd
  (0.5, [(check_quest_active,"qst_move_cattle_herd"),
         (neg|check_quest_concluded,"qst_move_cattle_herd"),
         (quest_get_slot, ":target_party", "qst_move_cattle_herd", slot_quest_target_party),
         (quest_get_slot, ":target_center", "qst_move_cattle_herd", slot_quest_target_center),
         (store_distance_to_party_from_party, ":dist",":target_party", ":target_center"),
         (lt, ":dist", 3),
         (remove_party, ":target_party"),
         (call_script, "script_succeed_quest", "qst_move_cattle_herd"),
    ]),

  (2, [
       (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
		 (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
		 (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
         (ge, ":party_no", 1),
		 (party_is_active, ":party_no"),
         (party_slot_eq, ":party_no", slot_party_following_player, 1),
         (store_current_hours, ":cur_time"),
         (neg|party_slot_ge, ":party_no", slot_party_follow_player_until_time, ":cur_time"),
         (party_set_slot, ":party_no", slot_party_commander_party, -1),
         (party_set_slot, ":party_no", slot_party_following_player, 0),
         (assign,  ":dont_follow_period", 200),
         (store_add, ":dont_follow_time", ":cur_time", ":dont_follow_period"),
         (party_set_slot, ":party_no", slot_party_dont_follow_player_until_time,  ":dont_follow_time"),
       (try_end),
    ]),

# Deliver cattle and deliver cattle to army
  (0.5,
   [
     (try_begin),
       (check_quest_active,"qst_deliver_cattle"),
       (neg|check_quest_succeeded, "qst_deliver_cattle"),
       (quest_get_slot, ":target_center", "qst_deliver_cattle", slot_quest_target_center),
       (quest_get_slot, ":target_amount", "qst_deliver_cattle", slot_quest_target_amount),
       (quest_get_slot, ":cur_amount", "qst_deliver_cattle", slot_quest_current_state),
       (store_sub, ":left_amount", ":target_amount", ":cur_amount"),
       (call_script, "script_remove_cattles_if_herd_is_close_to_party", ":target_center", ":left_amount"),
       (val_add, ":cur_amount", reg0),
       (quest_set_slot, "qst_deliver_cattle", slot_quest_current_state, ":cur_amount"),
       (le, ":target_amount", ":cur_amount"),
       (call_script, "script_succeed_quest", "qst_deliver_cattle"),
     (try_end),
     (try_begin),
       (check_quest_active, "qst_deliver_cattle_to_army"),
       (neg|check_quest_succeeded, "qst_deliver_cattle_to_army"),
       (quest_get_slot, ":giver_troop", "qst_deliver_cattle_to_army", slot_quest_giver_troop),
       (troop_get_slot, ":target_party", ":giver_troop", slot_troop_leaded_party),
       (try_begin),
         (gt, ":target_party", 0),
         (quest_get_slot, ":target_amount", "qst_deliver_cattle_to_army", slot_quest_target_amount),
         (quest_get_slot, ":cur_amount", "qst_deliver_cattle_to_army", slot_quest_current_state),
         (store_sub, ":left_amount", ":target_amount", ":cur_amount"),
         (call_script, "script_remove_cattles_if_herd_is_close_to_party", ":target_party", ":left_amount"),
         (val_add, ":cur_amount", reg0),
         (quest_set_slot, "qst_deliver_cattle_to_army", slot_quest_current_state, ":cur_amount"),
         (try_begin),
           (le, ":target_amount", ":cur_amount"),
           (call_script, "script_succeed_quest", "qst_deliver_cattle_to_army"),
         (try_end),
       (else_try),
         (call_script, "script_abort_quest", "qst_deliver_cattle_to_army", 0),
       (try_end),
     (try_end),
     ]),

# Train peasants against bandits
  (1,
   [
     (neg|map_free),
     (check_quest_active, "qst_train_peasants_against_bandits"),
     (neg|check_quest_concluded, "qst_train_peasants_against_bandits"),
     (eq, "$qst_train_peasants_against_bandits_currently_training", 1),
     (val_add, "$qst_train_peasants_against_bandits_num_hours_trained", 1),
     (call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
     (assign, ":trainer_skill", reg0),
     (store_sub, ":needed_hours", 20, ":trainer_skill"),
     (val_mul, ":needed_hours", 3),
     (val_div, ":needed_hours", 5),
     (ge, "$qst_train_peasants_against_bandits_num_hours_trained", ":needed_hours"),
     (assign, "$qst_train_peasants_against_bandits_num_hours_trained", 0),
     (rest_for_hours, 0, 0, 0), #stop resting
     (jump_to_menu, "mnu_train_peasants_against_bandits_ready"),
     ]),

# Scout waypoints
  (1,
   [
     (check_quest_active,"qst_scout_waypoints"),
     (neg|check_quest_succeeded, "qst_scout_waypoints"),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_1_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_1", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_1_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_1"),
       (display_message, "@{s1} is scouted."),
     (try_end),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_2_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_2", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_2_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_2"),
       (display_message, "@{s1} is scouted."),
     (try_end),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_3_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_3", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_3_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_3"),
       (display_message, "@{s1} is scouted."),
     (try_end),
     (eq, "$qst_scout_waypoints_wp_1_visited", 1),
     (eq, "$qst_scout_waypoints_wp_2_visited", 1),
     (eq, "$qst_scout_waypoints_wp_3_visited", 1),
     (call_script, "script_succeed_quest", "qst_scout_waypoints"),
     ]),

# Kill local merchant

  (3, [(neg|map_free),
       (check_quest_active, "qst_kill_local_merchant"),
       (quest_slot_eq, "qst_kill_local_merchant", slot_quest_current_state, 0),
       (quest_set_slot, "qst_kill_local_merchant", slot_quest_current_state, 1),
       (rest_for_hours, 0, 0, 0), #stop resting
       (assign, "$auto_enter_town", "$qst_kill_local_merchant_center"),
       (assign, "$quest_auto_menu", "mnu_kill_local_merchant_begin"),
       ]),

# Collect taxes
  (1, [(neg|map_free),
       (check_quest_active, "qst_collect_taxes"),
       (eq, "$g_player_is_captive", 0),
       (eq, "$qst_collect_taxes_currently_collecting", 1),
       (quest_get_slot, ":quest_current_state", "qst_collect_taxes", slot_quest_current_state),
       (this_or_next|eq, ":quest_current_state", 1),
       (this_or_next|eq, ":quest_current_state", 2),
       (eq, ":quest_current_state", 3),
       (quest_get_slot, ":left_hours", "qst_collect_taxes", slot_quest_target_amount),
       (val_sub, ":left_hours", 1),
       (quest_set_slot, "qst_collect_taxes", slot_quest_target_amount, ":left_hours"),
       (call_script, "script_get_max_skill_of_player_party", "skl_trade"),

       (try_begin),
         (lt, ":left_hours", 0),
         (assign, ":quest_current_state", 4),
         (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 4),
         (rest_for_hours, 0, 0, 0), #stop resting
         (jump_to_menu, "mnu_collect_taxes_complete"),
       (else_try),
         #Continue collecting taxes
         (assign, ":max_collected_tax", "$qst_collect_taxes_hourly_income"),
         (party_get_slot, ":prosperity", "$g_encountered_party", slot_town_prosperity),
         (store_add, ":multiplier", 30, ":prosperity"),
         (val_mul, ":max_collected_tax", ":multiplier"),
         (val_div, ":max_collected_tax", 80),#Prosperity of 50 gives the default values

         (try_begin),
           (eq, "$qst_collect_taxes_halve_taxes", 1),
           (val_div, ":max_collected_tax", 2),
         (try_end),
         (val_max, ":max_collected_tax", 2),
         (store_random_in_range, ":collected_tax", 1, ":max_collected_tax"),
         (quest_get_slot, ":cur_collected", "qst_collect_taxes", slot_quest_gold_reward),
         (val_add, ":cur_collected", ":collected_tax"),
         (quest_set_slot, "qst_collect_taxes", slot_quest_gold_reward, ":cur_collected"),
         (call_script, "script_troop_add_gold", "trp_player", ":collected_tax"),
       (try_end),
       (try_begin),
         (eq, ":quest_current_state", 1),
         (val_sub, "$qst_collect_taxes_menu_counter", 1),
         (le, "$qst_collect_taxes_menu_counter", 0),
         (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 2),
         (jump_to_menu, "mnu_collect_taxes_revolt_warning"),
       (else_try), #Chance of revolt against player
         (eq, ":quest_current_state", 2),
         (val_sub, "$qst_collect_taxes_unrest_counter", 1),
         (le, "$qst_collect_taxes_unrest_counter", 0),
         (eq, "$qst_collect_taxes_halve_taxes", 0),
         (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 3),

         (store_div, ":unrest_chance", 10000, "$qst_collect_taxes_total_hours"),
         (val_add, ":unrest_chance",30),

         (store_random_in_range, ":unrest_roll", 0, 1000),
         (try_begin),
           (lt, ":unrest_roll", ":unrest_chance"),
           (jump_to_menu, "mnu_collect_taxes_revolt"),
         (try_end),
       (try_end),
       ]),

#persuade_lords_to_make_peace begin
  (72, [(gt, "$g_force_peace_faction_1", 0),
        (gt, "$g_force_peace_faction_2", 0),
        (try_begin),
          (store_relation, ":relation", "$g_force_peace_faction_1", "$g_force_peace_faction_2"),
          (lt, ":relation", 0),
          (call_script, "script_diplomacy_start_peace_between_kingdoms", "$g_force_peace_faction_1", "$g_force_peace_faction_2", 1),
        (try_end),
        (assign, "$g_force_peace_faction_1", 0),
        (assign, "$g_force_peace_faction_2", 0),
       ]),

#NPC changes begin
#Resolve one issue each hour
(1,
   [
		(str_store_string, s51, "str_no_trigger_noted"),

		# Rejoining party
        (try_begin),
            (gt, "$npc_to_rejoin_party", 0),
            (eq, "$g_infinite_camping", 0),
			##(is_between, "$npc_to_rejoin_party", heroes_begin, heroes_end), #FLORIS - bugfix  ##NOT NEEDED - fixed elsewhere
            (try_begin),
                (neg|main_party_has_troop, "$npc_to_rejoin_party"),
                (neq, "$g_player_is_captive", 1),

				(str_store_string, s51, "str_triggered_by_npc_to_rejoin_party"),

                (assign, "$npc_map_talk_context", slot_troop_days_on_mission),
                (start_map_conversation, "$npc_to_rejoin_party", -1),
			(else_try),
				(troop_set_slot, "$npc_to_rejoin_party", slot_troop_current_mission, npc_mission_rejoin_when_possible),
				(assign, "$npc_to_rejoin_party", 0),
            (try_end),
		# Here do NPC that is quitting
		(else_try),
            (gt, "$npc_is_quitting", 0),
            (eq, "$g_infinite_camping", 0),
			## WINDYPLAINS+ ## - Disabling companion complaints also prevents quitting.
			(eq, "$disable_npc_complaints", 0),
			## WINDYPLAINS- ##
            (try_begin),
                (main_party_has_troop, "$npc_is_quitting"),
                (neq, "$g_player_is_captive", 1),
				##diplomacy start+ disable spouse quitting to avoid problems
				(neg|troop_slot_eq, "trp_player", slot_troop_spouse, "$npc_is_quitting"),
				(neg|troop_slot_eq, "$npc_is_quitting", slot_troop_spouse, "trp_player"),
				##diplomacy end+
				(str_store_string, s51, "str_triggered_by_npc_is_quitting"),
                (start_map_conversation, "$npc_is_quitting", -1),
            (else_try),
                (assign, "$npc_is_quitting", 0),
            (try_end),
		#NPC with grievance
        (else_try), #### Grievance
            (gt, "$npc_with_grievance", 0),
            (eq, "$g_infinite_camping", 0),
            (eq, "$disable_npc_complaints", 0),
            (try_begin),
                (main_party_has_troop, "$npc_with_grievance"),
                (neq, "$g_player_is_captive", 1),

				(str_store_string, s51, "str_triggered_by_npc_has_grievance"),

                (assign, "$npc_map_talk_context", slot_troop_morality_state),
                (start_map_conversation, "$npc_with_grievance", -1),
            (else_try),
                (assign, "$npc_with_grievance", 0),
            (try_end),
        (else_try),
            (gt, "$npc_with_personality_clash", 0),
            (eq, "$g_infinite_camping", 0),
            (eq, "$disable_npc_complaints", 0),
            (troop_get_slot, ":object", "$npc_with_personality_clash", slot_troop_personalityclash_object),
            (try_begin),
                (main_party_has_troop, "$npc_with_personality_clash"),
                (main_party_has_troop, ":object"),
                (neq, "$g_player_is_captive", 1),

                (assign, "$npc_map_talk_context", slot_troop_personalityclash_state),
				(str_store_string, s51, "str_triggered_by_npc_has_personality_clash"),
                (start_map_conversation, "$npc_with_personality_clash", -1),
            (else_try),
                (assign, "$npc_with_personality_clash", 0),
            (try_end),
        (else_try), #### Political issue
            (gt, "$npc_with_political_grievance", 0),
            (eq, "$g_infinite_camping", 0),
            (eq, "$disable_npc_complaints", 0),
            (try_begin),
                (main_party_has_troop, "$npc_with_political_grievance"),
                (neq, "$g_player_is_captive", 1),

				(str_store_string, s51, "str_triggered_by_npc_has_political_grievance"),
                (assign, "$npc_map_talk_context", slot_troop_kingsupport_objection_state),
                (start_map_conversation, "$npc_with_political_grievance", -1),
			(else_try),
				(assign, "$npc_with_political_grievance", 0),
            (try_end),
		(else_try),
            (eq, "$disable_sisterly_advice", 0),
            (eq, "$g_infinite_camping", 0),
            (gt, "$npc_with_sisterly_advice", 0),
            (try_begin),
				(main_party_has_troop, "$npc_with_sisterly_advice"),
                (neq, "$g_player_is_captive", 1),
				
				##diplomacy start+
				(troop_slot_ge, "$npc_with_sisterly_advice", slot_troop_woman_to_woman_string, 1),
				##diplomacy end+
				(assign, "$npc_map_talk_context", slot_troop_woman_to_woman_string), #was npc_with_sisterly advice
	            (start_map_conversation, "$npc_with_sisterly_advice", -1),
			(else_try),
				(assign, "$npc_with_sisterly_advice", 0),
            (try_end),
		(else_try), #check for regional background
            (eq, "$disable_local_histories", 0),
            (eq, "$g_infinite_camping", 0),
            (try_for_range, ":npc", companions_begin, companions_end),
                (main_party_has_troop, ":npc"),
                (troop_slot_eq, ":npc", slot_troop_home_speech_delivered, 0),
                (troop_get_slot, ":home", ":npc", slot_troop_home),
                (gt, ":home", 0),
                (store_distance_to_party_from_party, ":distance", ":home", "p_main_party"),
                (lt, ":distance", 7),
                (assign, "$npc_map_talk_context", slot_troop_home),

				(str_store_string, s51, "str_triggered_by_local_histories"),

                (start_map_conversation, ":npc", -1),
            (try_end),
        (try_end),

		#add pretender to party if not active
		(try_begin),
			(check_quest_active, "qst_rebel_against_kingdom"),
			(is_between, "$supported_pretender", pretenders_begin, pretenders_end),
			(neg|main_party_has_troop, "$supported_pretender"),
			(neg|troop_slot_eq, "$supported_pretender", slot_troop_occupation, slto_kingdom_hero),
			(party_add_members, "p_main_party", "$supported_pretender", 1),
		(try_end),

		#make player marshal of rebel faction
		(try_begin),
			(check_quest_active, "qst_rebel_against_kingdom"),
			(is_between, "$supported_pretender", pretenders_begin, pretenders_end),
			(main_party_has_troop, "$supported_pretender"),
			(neg|faction_slot_eq, "fac_player_supporters_faction", slot_faction_marshall, "trp_player"),
			(call_script, "script_appoint_faction_marshall", "fac_player_supporters_faction", "trp_player"),
		(try_end),


]),
#NPC changes end

(4,
   ##diplomacy start+ Add support for promoted kingdom ladies
   ##OLD:
   #[(try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
   ##NEW:
   [(try_for_range, ":troop_no", heroes_begin, heroes_end),
      (this_or_next|is_between, ":troop_no", active_npcs_begin, active_npcs_end),
	  (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
   ##diplomacy end+
      (troop_slot_ge, ":troop_no", slot_troop_change_to_faction, 1),
      (store_troop_faction, ":faction_no", ":troop_no"),
      (troop_get_slot, ":new_faction_no", ":troop_no", slot_troop_change_to_faction),
      (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
      (assign, ":continue", 0),
      (try_begin),
        (le, ":party_no", 0),
        #(troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
        (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
        (assign, ":continue", 1),
      (else_try),
        (gt, ":party_no", 0),

        #checking if the party is outside the centers
        (party_get_attached_to, ":cur_center_no", ":party_no"),
        (try_begin),
          (lt, ":cur_center_no", 0),
          (party_get_cur_town, ":cur_center_no", ":party_no"),
        (try_end),
        (this_or_next|neg|is_between, ":cur_center_no", centers_begin, centers_end),
        (party_slot_eq, ":cur_center_no", slot_town_lord, ":troop_no"),

        #checking if the party is away from his original faction parties
		##diplomacy start+
		##Add support for promoted kingdom lades.
		##OLD:
        #(assign, ":end_cond", active_npcs_end),
		##NEW:
        (assign, ":end_cond", heroes_end),
		##diplomacy end+
        (try_for_range, ":enemy_troop_no", active_npcs_begin, ":end_cond"),
          (neq, ":enemy_troop_no", ":troop_no"), ## CC
		  (troop_slot_eq, ":enemy_troop_no", slot_troop_occupation, slto_kingdom_hero),
          (troop_get_slot, ":enemy_party_no", ":enemy_troop_no", slot_troop_leaded_party),
          (party_is_active, ":enemy_party_no"),
          (store_faction_of_party, ":enemy_faction_no", ":enemy_party_no"),
          (eq, ":enemy_faction_no", ":faction_no"),
          (store_distance_to_party_from_party, ":dist", ":party_no", ":enemy_party_no"),
          (lt, ":dist", 4),
          (assign, ":end_cond", 0),
        (try_end),
        (neq, ":end_cond", 0),
        (assign, ":continue", 1),
      (try_end),
      (eq, ":continue", 1),
## Begin 1.134
		(try_begin),
			(ge, "$cheat_mode", 1),
			(str_store_troop_name, s4, ":troop_no"),
			(display_message, "@{!}DEBUG - {s4} faction changed from slot_troop_change_to_faction"), 
		(try_end),	  
## End 1.134
      (call_script, "script_change_troop_faction", ":troop_no", ":new_faction_no"),
      (troop_set_slot, ":troop_no", slot_troop_change_to_faction, 0),
      (try_begin),
        (is_between, ":new_faction_no", kingdoms_begin, kingdoms_end),
        (str_store_troop_name_link, s1, ":troop_no"),
        (str_store_faction_name_link, s2, ":faction_no"),
        (str_store_faction_name_link, s3, ":new_faction_no"),
        (display_message, "@{s1} has switched from {s2} to {s3}."),
        (try_begin),
          (eq, ":faction_no", "$players_kingdom"),
          (call_script, "script_add_notification_menu", "mnu_notification_troop_left_players_faction", ":troop_no", ":new_faction_no"),
        (else_try),
          (eq, ":new_faction_no", "$players_kingdom"),
          (call_script, "script_add_notification_menu", "mnu_notification_troop_joined_players_faction", ":troop_no", ":faction_no"),
        (try_end),
      (try_end),
    (try_end),
    ]),


(1,
   [
     (eq, "$cheat_mode", 1),
     (try_for_range, ":center_no", centers_begin, centers_end),
       (party_get_battle_opponent, ":besieger_party", ":center_no"),
       (try_begin),
         (gt, ":besieger_party", 0),
         (str_store_party_name, s2, ":center_no"),
         (str_store_party_name, s3, ":besieger_party"),
         (display_message, "@{!}DEBUG : {s2} is besieging by {s3}"),
       (try_end),
     (try_end),
     ]),

(1,
   [
     (store_current_day, ":cur_day"),
     (gt, ":cur_day", "$g_last_report_control_day"),
     (store_time_of_day, ":cur_hour"),
     (ge, ":cur_hour", 18),

     (store_random_in_range, ":rand_no", 0, 4),
     (this_or_next|ge, ":cur_hour", 22),
     (eq, ":rand_no", 0),

     (assign, "$g_last_report_control_day", ":cur_day"),

     (store_troop_gold, ":gold", "trp_player"),

     (try_begin),
       (lt, ":gold", 0),
       (store_sub, ":gold_difference", 0, ":gold"),
       (troop_add_gold, "trp_player", ":gold_difference"),
     (try_end),

     (party_get_morale, ":main_party_morale", "p_main_party"),

     #(assign, ":swadian_soldiers_are_upset_message_showed", 0),
     #(assign, ":vaegir_soldiers_are_upset_message_showed", 0),
     #(assign, ":khergit_soldiers_are_upset_message_showed", 0),
     #(assign, ":nord_soldiers_are_upset_message_showed", 0),
     #(assign, ":rhodok_soldiers_are_upset_message_showed", 0),

     (try_begin),
       (str_store_string, s1, "str_party_morale_is_low"),
       (str_clear, s2),

       (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
       (assign, ":num_deserters_total", 0),
       (try_for_range_backwards, ":i_stack", 0, ":num_stacks"), ##1.132
#       (try_for_range, ":i_stack", 0, ":num_stacks"), ##1.131
         (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
         (neg|troop_is_hero, ":stack_troop"),
         (party_stack_get_size, ":stack_size", "p_main_party", ":i_stack"),

         (store_troop_faction, ":faction_no", ":stack_troop"),

         (assign, ":troop_morale", ":main_party_morale"),
         (try_begin),
           (ge, ":faction_no", kingdoms_begin), #Player Faction
           (lt, ":faction_no", kingdoms_end), #Player Faction
        
           (faction_get_slot, ":troop_morale_addition", ":faction_no",  slot_faction_morale_of_player_troops),
           (val_div, ":troop_morale_addition", 100),
           (val_add, ":troop_morale", ":troop_morale_addition"),
         (try_end),

         (lt, ":troop_morale", 32),
         (store_sub, ":desert_prob", 36, ":troop_morale"),
         (val_div, ":desert_prob", 4),

         (assign, ":num_deserters_from_that_troop", 0),
         (try_for_range, ":unused", 0, ":stack_size"),
           (store_random_in_range, ":rand_no", 0, 100),
           (lt, ":rand_no", ":desert_prob"),
           (val_add, ":num_deserters_from_that_troop", 1),
           #p.remove_members_from_stack(i_stack,cur_deserters, &main_party_instances);
           (remove_member_from_party, ":stack_troop", "p_main_party"),
         (try_end),
         (try_begin),
           (ge, ":num_deserters_from_that_troop", 1),
           (str_store_troop_name, s2, ":stack_troop"),
           (assign, reg0, ":num_deserters_from_that_troop"),

#           (try_begin),
#             (lt, ":troop_morale_addition", -2),
#             (ge, ":main_party_morale", 28),
#             (try_begin),
#               (eq, ":faction_no", "fac_kingdom_1"),
#               (eq, ":swadian_soldiers_are_upset_message_showed", 0),
#               (str_store_string, s3, "str_swadian_soldiers_are_upset"),
#               (assign, ":swadian_soldiers_are_upset_message_showed", 1),
#             (else_try),
#               (eq, ":faction_no", "fac_kingdom_2"),
#               (eq, ":vaegir_soldiers_are_upset_message_showed", 0),
#               (str_store_string, s3, "str_vaegir_soldiers_are_upset"),
#               (assign, ":vaegir_soldiers_are_upset_message_showed", 1),
#             (else_try),
#               (eq, ":faction_no", "fac_kingdom_3"),
#               (eq, ":khergit_soldiers_are_upset_message_showed", 0),
#               (str_store_string, s3, "str_khergit_soldiers_are_upset"),
#               (assign, ":khergit_soldiers_are_upset_message_showed", 1),
#             (else_try),
#               (eq, ":faction_no", "fac_kingdom_4"),
#               (eq, ":nord_soldiers_are_upset_message_showed", 0),
#               (str_store_string, s3, "str_nord_soldiers_are_upset"),
#               (assign, ":nord_soldiers_are_upset_message_showed", 1),
#             (else_try),
#               (eq, ":faction_no", "fac_kingdom_5"),
#               (eq, ":rhodok_soldiers_are_upset_message_showed", 0),
#               (str_store_string, s3, "str_rhodok_soldiers_are_upset"),
#               (assign, ":rhodok_soldiers_are_upset_message_showed", 1),
#             (try_end),
#             (str_store_string, s1, "@{!}{s1} {s3}"),
#           (try_end),

           (try_begin),
             (ge, ":num_deserters_total", 1),
             (str_store_string, s1, "str_s1_reg0_s2"),
           (else_try),
             (str_store_string, s3, s1),
             (str_store_string, s1, "str_s3_reg0_s2"),
           (try_end),
           (val_add, ":num_deserters_total", ":num_deserters_from_that_troop"),
         (try_end),
       (try_end),

       (try_begin),
         (ge, ":num_deserters_total", 1),

         (try_begin),
           (ge, ":num_deserters_total", 2),
           (str_store_string, s2, "str_have_deserted_the_party"),
         (else_try),
           (str_store_string, s2, "str_has_deserted_the_party"),
         (try_end),

         (str_store_string, s1, "str_s1_s2"),

         (eq, "$g_infinite_camping", 0),

         (tutorial_box, s1, "str_weekly_report"),
       (try_end),
     (try_end),
 ]),
 # reserved for future use. For backward compatibility, we need to use these triggers instead of creating new ones.

  (1,
   [
     (call_script, "script_calculate_castle_prosperities_by_using_its_villages"),

     (store_add, ":fac_kingdom_6_plus_one", "fac_kingdom_6", 1),

     (try_for_range, ":faction_1", "fac_kingdom_1", ":fac_kingdom_6_plus_one"),
       (try_for_range, ":faction_2", "fac_kingdom_1", ":fac_kingdom_6_plus_one"),
         (store_relation, ":faction_relation", ":faction_1", ":faction_2"),
         (str_store_faction_name, s7, ":faction_1"),
         (str_store_faction_name, s8, ":faction_2"),
         (neq, ":faction_1", ":faction_2"),
         (assign, reg1, ":faction_relation"),
         #(display_message, "@{s7}-{s8}, relation is {reg1}"),
       (try_end),
     (try_end),
   ]),

  (1,
   [
     (try_begin),
       (eq, "$g_player_is_captive", 1),
       (neg|party_is_active, "$capturer_party"),
       (rest_for_hours, 0, 0, 0),
     (try_end),

     ##diplomacy begin
      #seems to be a native bug
     (is_between, "$next_center_will_be_fired", villages_begin, villages_end),
     ##diplomacy end
     (assign, ":village_no", "$next_center_will_be_fired"),
     (party_get_slot, ":is_there_already_fire", ":village_no", slot_village_smoke_added),
     (eq, ":is_there_already_fire", 0),


     (try_begin),
       (party_get_slot, ":bound_center", ":village_no", slot_village_bound_center),
       (party_get_slot, ":last_nearby_fire_time", ":bound_center", slot_town_last_nearby_fire_time),
       (store_current_hours, ":cur_hours"),
## Begin 1.134
	   (try_begin),
		(eq, "$cheat_mode", 1),
		(is_between, ":village_no", centers_begin, centers_end),
		(is_between, ":bound_center", centers_begin, centers_end),
		(str_store_party_name, s4, ":village_no"),
		(str_store_party_name, s5, ":bound_center"),
		(store_current_hours, reg3),
        (party_get_slot, reg4, ":bound_center", slot_town_last_nearby_fire_time),
		(display_message, "@{!}DEBUG - Checking fire at {s4} for {s5} - current time {reg3}, last nearby fire {reg4}"),
	   (try_end),
## End 1.134
       (eq, ":cur_hours", ":last_nearby_fire_time"),
       (party_add_particle_system, ":village_no", "psys_map_village_fire"),
       (party_add_particle_system, ":village_no", "psys_map_village_fire_smoke"),
     (else_try),
       (store_add, ":last_nearby_fire_finish_time", ":last_nearby_fire_time", fire_duration),
       (eq, ":last_nearby_fire_finish_time", ":cur_hours"),
       (party_clear_particle_systems, ":village_no"),
     (try_end),  
     
## Removed in 1.134
#     (assign, ":village_no", "$next_center_will_be_fired"),
#       (party_get_slot, ":is_there_already_fire", ":village_no", slot_village_smoke_added),
#       (eq, ":is_there_already_fire", 0),
#       (try_begin),
#         (party_get_slot, ":bound_center", ":village_no", slot_village_bound_center),  
#         (party_get_slot, ":last_nearby_fire_time", ":bound_center", slot_town_last_nearby_fire_time),
#         (store_current_hours, ":cur_hours"),
#         (eq, ":cur_hours", ":last_nearby_fire_time"),
#         (party_add_particle_system, ":village_no", "psys_map_village_fire"),
#         (party_add_particle_system, ":village_no", "psys_map_village_fire_smoke"),       
#       (else_try),  
#         (store_add, ":last_nearby_fire_finish_time", ":last_nearby_fire_time", fire_duration),
#         (eq, ":last_nearby_fire_finish_time", ":cur_hours"),
#         (party_clear_particle_systems, ":village_no"),
#       (try_end),
##
   ]),

  (24,
   [
   (val_sub, "$g_dont_give_fief_to_player_days", 1),
   (val_max, "$g_dont_give_fief_to_player_days", -1),
   (val_sub, "$g_dont_give_marshalship_to_player_days", 1),
   (val_max, "$g_dont_give_marshalship_to_player_days", -1),
   
   ##diplomacy start+
   ##Add version checking, so the corrections are only applied once.
   ##This allows for more complicated things to be added here in the future
   (troop_get_slot, ":diplomacy_version_code", "trp_dplmc_chamberlain", dplmc_slot_troop_affiliated),#I've arbitrarily picked "when I started tracking this" as 0
   (store_mod, ":verification", ":diplomacy_version_code", 128),
   (assign, ":save_reg0", reg0),
   (assign, ":save_reg1", reg1),
   (try_begin),
		#Detect bad values
		(neq, ":diplomacy_version_code", 0),
		(neq, ":verification", 68),
		(assign, reg0, ":diplomacy_version_code"),
		(display_message, "@{!} A slot had an unexpected value: {reg0}.  This might be because you are using an incompatible troop list, or are using a non-native strange game.  This message will repeat daily."),
		(assign, ":diplomacy_version_code", -1),
	(else_try),
		(val_div, ":diplomacy_version_code", 128),
		#Update if necessary.
		(lt, ":diplomacy_version_code", DPLMC_current_version_CODE),
		(ge, "$cheat_mode", 1),
		(assign, reg0, ":diplomacy_version_code"),
		
		(assign, reg1, DPLMC_current_version_CODE),
		(display_message, "@{!} DEBUG - Detected a new version of diplomacy: previous version was {reg0}, and current version is {reg1}.  Performing updates."),
		(val_mul, reg1, 128),
		(val_add, reg1, DPLMC_VERSION_LOW_7_BITS),
		(troop_set_slot, "trp_dplmc_chamberlain", dplmc_slot_troop_affiliated, reg1),
	(try_end),

	(try_begin),
	(is_between, ":diplomacy_version_code", -1, 1),#-1 or 0
	#Native behavior follows
	##diplomacy end+

   #this to correct string errors in games started in 1.104 or before
   (party_set_name, "p_steppe_bandit_spawn_point", "str_the_steppes"),
   (party_set_name, "p_taiga_bandit_spawn_point", "str_the_tundra"),
   (party_set_name, "p_forest_bandit_spawn_point", "str_the_forests"),
   (party_set_name, "p_mountain_bandit_spawn_point", "str_the_highlands"),
   (party_set_name, "p_sea_raider_spawn_point_1", "str_the_coast"),
   (party_set_name, "p_sea_raider_spawn_point_2", "str_the_coast"),
   (party_set_name, "p_desert_bandit_spawn_point", "str_the_deserts"),


   #This to correct inappropriate home strings - Katrin to Uxkhal, Matheld to Fearichen
   (troop_set_slot, "trp_npc11", slot_troop_home, "p_town_7"),
   (troop_set_slot, "trp_npc8", slot_troop_home, "p_village_35"),

   (troop_set_slot, "trp_npc15", slot_troop_town_with_contacts, "p_town_20"), #durquba
   
   #this to correct linen production at villages of durquba 					#	1.143 Port // Changed commentary
   (party_set_slot, "p_village_93", slot_center_linen_looms, 0), #mazigh
   (party_set_slot, "p_village_94", slot_center_linen_looms, 0), #sekhtem
   (party_set_slot, "p_village_95", slot_center_linen_looms, 0), #qalyut
   (party_set_slot, "p_village_96", slot_center_linen_looms, 0), #tilimsal
   (party_set_slot, "p_village_97", slot_center_linen_looms, 0), #shibal zumr
   (party_set_slot, "p_village_102", slot_center_linen_looms, 0), #tamnuh
   (party_set_slot, "p_village_109", slot_center_linen_looms, 0), #habba

   (party_set_slot, "p_village_67", slot_center_fishing_fleet, 0), #Tebandra
   (party_set_slot, "p_village_5", slot_center_fishing_fleet, 15), #Kulum
   
   ##diplomacy start+
   #End the changes in Native
	(try_end),
	
   #Behavior specific to a fresh Diplomacy version
	(try_begin),
   (ge, ":diplomacy_version_code", 0),#do not run this if the code is bad
   (lt, ":diplomacy_version_code", 1),
   #Add home centers for claimants (mods not using standard NPCs or map may wish to remove this)
   (troop_set_slot, "trp_kingdom_1_pretender", slot_troop_home, "p_town_4"),#Lady Isolle - Suno
   (troop_set_slot, "trp_kingdom_2_pretender", slot_troop_home, "p_town_11"),#Prince Valdym - Curaw
   (troop_set_slot, "trp_kingdom_3_pretender", slot_troop_home, "p_town_18"),#Dustum Khan - Narra
   (troop_set_slot, "trp_kingdom_4_pretender", slot_troop_home, "p_town_12"),#Lethwin Far-Seeker - Wercheg
   (troop_set_slot, "trp_kingdom_5_pretender", slot_troop_home, "p_town_3"),#Lord Kastor - Veluca
   (troop_set_slot, "trp_kingdom_6_pretender", slot_troop_home, "p_town_20"),#Arwa the Pearled One - Durquba
   #add ancestral fiefs to home slots (mods not using standard NPCs or map should remove this)
   (troop_set_slot, "trp_knight_2_10", slot_troop_home, "p_castle_29"), #Nelag_Castle
   (troop_set_slot, "trp_knight_3_4", slot_troop_home, "p_castle_30"), #Asugan_Castle
   (troop_set_slot, "trp_knight_1_3", slot_troop_home, "p_castle_35"), #Haringoth_Castle
   (troop_set_slot, "trp_knight_5_11", slot_troop_home, "p_castle_33"), #Etrosq_Castle
   #Also the primary six towns (mods not using standard NPCs or map may wish to remove this)
   (troop_set_slot, "trp_kingdom_1_lord", slot_troop_home, "p_town_6"),#King Harlaus to Praven
   (troop_set_slot, "trp_kingdom_2_lord", slot_troop_home, "p_town_8"),#King Yaroglek to Reyvadin
   (troop_set_slot, "trp_kingdom_3_lord", slot_troop_home, "p_town_10"),#Sanjar Khan to Tulga
   (troop_set_slot, "trp_kingdom_4_lord", slot_troop_home, "p_town_1"),#King Ragnar to Sargoth
   (troop_set_slot, "trp_kingdom_5_lord", slot_troop_home, "p_town_5"),#King Graveth to Jelkala
   (troop_set_slot, "trp_kingdom_6_lord", slot_troop_home, "p_town_19"),#Sultan Hakim to Shariz
   
   #Set the "original lord" values corresponding to the above.
   (try_for_range, ":troop_no", active_npcs_begin, active_npcs_end),
		(this_or_next|eq, ":troop_no", "trp_knight_2_10"),#Nelag
		(this_or_next|eq, ":troop_no", "trp_knight_3_4"),#Asugan
		(this_or_next|eq, ":troop_no", "trp_knight_1_3"),#Haringoth
		(this_or_next|eq, ":troop_no", "trp_knight_5_11"),#Etrosq
		(this_or_next|is_between, ":troop_no", kings_begin, kings_end),
			(is_between, ":troop_no", pretenders_begin, pretenders_end),
		
		(troop_get_slot, ":center_no", ":troop_no", slot_troop_home),
		(is_between, ":center_no", centers_begin, centers_end),
		(neg|party_slot_ge, ":center_no", dplmc_slot_center_original_lord, 1),
		(party_set_slot, ":center_no",  dplmc_slot_center_original_lord, ":troop_no"),
		
		#Also set "ex-lord"
		(neg|is_between, ":troop_no", pretenders_begin, pretenders_end),
		(troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
		(neg|party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
		(neg|party_slot_ge, ":center_no", dplmc_slot_center_ex_lord, 1),
		(party_set_slot, ":center_no", dplmc_slot_center_ex_lord, ":troop_no"),
   (try_end),
      
   #Make sure the affiliation slot is set correctly.
   (try_begin),
	 (is_between, "$g_player_affiliated_troop", lords_begin, kingdom_ladies_end),
	 (troop_get_slot, ":slot_val", "$g_player_affiliated_troop", dplmc_slot_troop_affiliated),
	 (is_between, ":slot_val", 0, 3),#0 is default, 1 is asked, in previous versions there was no use of 2
	 (troop_set_slot, "$g_player_affiliated_troop", dplmc_slot_troop_affiliated, 3),#3 is affiliated
   (try_end),
   
   #Set father/mother slots for the unmarried medium-age lords, so checking for
   #being related will work as expected.
   (try_for_range, ":troop_no", lords_begin, lords_end),
		(troop_slot_eq, ":troop_no", slot_troop_father, -1),
		(troop_slot_eq, ":troop_no", slot_troop_mother, -1),
		(store_mul, ":father", ":troop_no", DPLMC_VIRTUAL_RELATIVE_MULTIPLIER),#defined in module_constants.py
		(val_add, ":father", DPLMC_VIRTUAL_RELATIVE_FATHER_OFFSET),
		(troop_set_slot, ":troop_no", slot_troop_father, ":father"),
		(store_add, ":mother", ":father", DPLMC_VIRTUAL_RELATIVE_MOTHER_OFFSET - DPLMC_VIRTUAL_RELATIVE_FATHER_OFFSET),
		(troop_set_slot, ":troop_no", slot_troop_mother, ":mother"),
   (try_end),
   
   #Fix kingdom lady daughters having "slot_troop_mother" set to themselves.
   #The old fix was in troop_get_family_relation_to_troop, but now we can
   #just do it once here.
   (try_for_range, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
		(try_begin),
			(troop_slot_eq, ":troop_no", slot_troop_mother, ":troop_no"),
			(troop_get_slot, ":father", ":troop_no", slot_troop_father),
			(try_begin),
				(is_between, ":father", active_npcs_begin, active_npcs_end),
				(troop_get_slot, ":mother", ":father", slot_troop_spouse),
				(troop_set_slot, ":troop_no", slot_troop_mother, ":mother"),
				(try_begin),
					#Print a message if desired
					(ge, "$cheat_mode", 1),
					(str_store_troop_name, s0, ":troop_no"),
					(display_message, "@{!}DEBUG - Fixed slot_troop_mother for {s0}."),
				(try_end),
			(else_try),
				(troop_set_slot, ":troop_no", slot_troop_mother, -1),#better than being set to herself 
				#Print a message if desired
				(ge, "$cheat_mode", 1),
				(str_store_troop_name, s0, ":troop_no"),
				(display_message, "@{!}DEBUG - When fixing slot_troop_mother for {s0}, could not find a valid mother."),
			(try_end),
	#While we're at it, also give parents to the sisters of the middle-aged lords.
		(else_try),
			(troop_slot_eq, ":troop_no", slot_troop_father, -1),
			(troop_slot_eq, ":troop_no", slot_troop_mother, -1),
			#"Guardian" here means brother
			(troop_get_slot, ":guardian", ":troop_no", slot_troop_guardian),
			(ge, ":guardian", 1),
			#Has brother's father
			(troop_get_slot, ":father", ":guardian", slot_troop_father),
			(troop_set_slot, ":troop_no", slot_troop_father, ":father"),
			#Has brother's mother
			(troop_get_slot, ":mother", ":guardian", slot_troop_mother),
			(troop_set_slot, ":troop_no", slot_troop_mother, ":mother"),
		(try_end),
   #Also set original factions for ladies.
	   (neg|troop_slot_ge, ":troop_no", slot_troop_original_faction, 1),
		(assign, ":guardian", -1),
		(try_begin),
		   (troop_slot_ge, ":troop_no", slot_troop_father, 1),
			(troop_get_slot, ":guardian", ":troop_no", slot_troop_father),
 	   (else_try),
		   (troop_slot_ge, ":troop_no", slot_troop_guardian, 1),
			(troop_get_slot, ":guardian", ":troop_no", slot_troop_guardian),
		(else_try),
		   (troop_slot_ge, ":troop_no", slot_troop_spouse, 1),
			(troop_get_slot, ":guardian", ":troop_no", slot_troop_spouse),
	   (try_end),
		(ge, ":guardian", 1),
		(troop_get_slot, ":original_faction", ":guardian", slot_troop_original_faction),
		(troop_set_slot, ":troop_no", slot_troop_original_faction, ":original_faction"),
   (try_end),

	  ##Set relations between kingdom ladies and their relatives.
	  ##Do *not* initialize their relations with anyone they aren't related to:
	  ##that is used for courtship.
	  ##  The purpose of this initialization is so if a kingdom lady gets promoted,
	  ##her relations aren't a featureless slate.  Also, it would be interesting to
	  ##further develop the idea of ladies as pursuing agendas even if they aren't
	  ##leading warbands, which would benefit from giving them relations with other
	  ##people.
	  #
	  #Because relations may already exist, only call this in instances where
	  #they are 0 or 1 (the latter just means "met" between NPCs).
     (try_for_range, ":lady", kingdom_ladies_begin, kingdom_ladies_end),
		(troop_slot_eq, ":lady", slot_troop_occupation, slto_kingdom_lady),
		(troop_get_slot, ":lady_faction", ":lady", slot_troop_original_faction),
		(ge, ":lady_faction", 1),

		(try_for_range, ":other_hero", heroes_begin, heroes_end),
		   (this_or_next|troop_slot_eq, ":other_hero", slot_troop_occupation, slto_kingdom_lady),
			(this_or_next|troop_slot_eq, ":other_hero", slot_troop_occupation, slto_kingdom_hero),
				(troop_slot_eq, ":other_hero", slot_troop_occupation, slto_inactive_pretender),
			(troop_slot_eq, ":other_hero", slot_troop_original_faction, ":lady_faction"),

			#Because this is not a new game: first check if relations have developed
			(call_script, "script_troop_get_relation_with_troop", ":lady", ":other_hero"),
			(is_between, reg0, 0, 2),#0 or 1

			(try_begin),
				(this_or_next|troop_slot_eq, ":lady", slot_troop_spouse, ":other_hero"),
				(troop_slot_eq, ":other_hero", slot_troop_spouse, ":lady"),
				(store_random_in_range, reg0, 0, 11),
			(else_try),
				#(call_script, "script_troop_get_family_relation_to_troop", ":lady", ":other_hero"),
				(call_script, "script_dplmc_troop_get_family_relation_to_troop", ":lady", ":other_hero"),
			(try_end),
			
			(call_script, "script_troop_change_relation_with_troop", ":lady", ":other_hero", reg0),

			#This relation change only applies between kingdom ladies.
			(troop_slot_eq, ":other_hero", slot_troop_occupation, slto_kingdom_lady),
			(is_between, ":other_hero", kingdom_ladies_begin, kingdom_ladies_end),

			(store_random_in_range, ":random", 0, 11),
			(call_script, "script_troop_change_relation_with_troop", ":lady", ":other_hero", ":random"),
		(try_end),
	  (try_end),
   
   #Change the occupation of exiled lords (not including pretenders or kings)
   (try_for_range, ":troop_no", lords_begin, lords_end),
		(store_troop_faction, ":faction_no", ":troop_no"),
		#A lord in the outlaw faction
		(eq, ":faction_no", "fac_outlaws"),
		#Possible values for his occupation if he's an exile (but there's some overlap between these and "bandit hero")
		(this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),#<- The default
		(this_or_next|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive),#<- This can happen joining the player faction
			(troop_slot_eq, ":troop_no", slot_troop_occupation, 0),#<- This gets set for prisoners
		#(Quick Check) Not leading a party or the prisoner of a party or at a center
		(neg|troop_slot_ge, ":troop_no", slot_troop_leaded_party, 0),
		(neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
		(neg|troop_slot_ge, ":troop_no", slot_troop_cur_center, 1),#deliberately 1 instead of 0
		#(Slow check) Does not own any fiefs
		(assign, ":end", centers_end),
		(try_for_range, ":center_no", centers_begin, ":end"),
			(party_slot_eq, ":center_no", slot_town_lord, ":troop_no"),
			(assign, ":end", ":center_no"),#stop loop, and also signal failure
		(try_end),
		#(Slow check) Explicitly verify he is not a prisoner anywhere.
		(call_script, "script_search_troop_prisoner_of_party", ":troop_no"),
		(eq, reg0, -1),
		#(Slow check) Explicitly verify he's not a member of any party
		(assign, ":member_of_party", -1),
		(try_for_parties, ":party_no"),
			(eq, ":member_of_party", -1),
			(this_or_next|eq, ":party_no", "p_main_party"),
				(ge, ":party_no", centers_begin),
			(party_count_members_of_type, ":count", ":party_no", ":troop_no"),
			(gt, ":count", 0),
			(assign, ":member_of_party", ":party_no"),
		(try_end),
		(eq, ":member_of_party", -1),
		#Finally verified that he is in exile.  Set the slot value to make
		#this easier in the future.
		(troop_set_slot, ":troop_no", slot_troop_occupation, dplmc_slto_exile),
		(try_begin),
			(ge, "$cheat_mode", 1),
			(str_store_troop_name, s0, ":troop_no"),
			(display_message, "@{!}DEBUG - Changed occupation of {s0} to dplmc_slto_exile"),
		(try_end),
   (try_end),
   
   #Initialize histories for supported pretenders.
   (try_for_range, ":troop_no", pretenders_begin, pretenders_end),
      (neg|troop_slot_eq, ":troop_no", slot_troop_met, 0),
      (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
	  (troop_slot_eq, ":troop_no", slot_troop_playerparty_history, 0),
	  (troop_set_slot, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
   (try_end),
   
   #Initialize histories for promoted companions
   (try_for_range, ":troop_no", companions_begin, companions_end),
	  (neg|troop_slot_eq, ":troop_no", slot_troop_met, 0),
      (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
	  (neg|troop_slot_eq, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_nonplayer_entry),
	  (troop_set_slot, ":troop_no", slot_troop_playerparty_history, dplmc_pp_history_granted_fief),
   (try_end),
   
   #For all centers, update new slots
   (try_for_range, ":center_no", centers_begin, centers_end),
	  #Last attacker
	  (try_begin),
	     (party_slot_eq, ":center_no", dplmc_slot_center_last_attacker, 0),
		 (party_slot_eq, ":center_no", dplmc_slot_center_last_attacked_time, 0),
		 (party_set_slot, ":center_no", dplmc_slot_center_last_attacker, -1),
	  (try_end),
	  
      (party_slot_eq, ":center_no", dplmc_slot_center_last_transfer_time, 0),
	  #Ex-lord
	  (try_begin),
  	     (party_slot_eq, ":center_no", dplmc_slot_center_ex_lord, 0),
	     (party_set_slot, ":center_no", dplmc_slot_center_ex_lord, -1),
	  (try_end),
	  #Original lord
	  (try_begin),
		(party_slot_eq, ":center_no", dplmc_slot_center_original_lord, 0),
		(neg|troop_slot_eq, "trp_player", slot_troop_home, ":center_no"),
		(party_set_slot, ":center_no", dplmc_slot_center_original_lord, -1),
	  (try_end),
   (try_end),
   
   #Don't bother filling in "last caravan arrival" slots with fake values.
   #Right now the scripts check and do that automatically if they aren't
   #set.
   
   
   #Fix a mistake I had introduced before, where you could get the wrong
   #"marry betrothed" quest when courting a lady.
   (try_begin),
      (check_quest_active, "qst_wed_betrothed_female"),
	  (quest_get_slot, ":betrothed_troop", "qst_wed_betrothed_female", slot_quest_giver_troop),
	  (is_between, ":betrothed_troop", kingdom_ladies_begin, kingdom_ladies_end),
	  (display_message, "@{!}FIXED PROBLEM - Cancelled erroneous version of qst_wed_betrothed_female.  You should be able to marry normally if you try again."),
	  (call_script, "script_abort_quest", "qst_wed_betrothed_female", 0),#abort with type 0 "event" should give no penalties to the player
   (try_end),   
   #End version-checked block.   
   (try_end),
   
   (try_begin),
    (ge, ":diplomacy_version_code", 1),
    (lt, ":diplomacy_version_code", 110615),
    #Fix a bug that was introduced in some version before 2011-06-15 that made
	#all "young unmarried lords" only have half-siblings, with either their own
	#father or mother slot uninitialized.
	(try_begin),
		(lt, 31, heroes_begin),
		(neg|troop_slot_eq, 31, 31, 0),#"slot_troop_father" was 31 in those saved games
		(troop_set_slot, 31, 31, -1),#(it still is 31 as far as I know, but this code should remain the same even if the slot value changes)
	(try_end),
	(try_begin),
		(lt, 32, heroes_begin),
		(neg|troop_slot_eq, 32,32,0),#"slot_troop_mother" was 32 in those saved games
		(troop_set_slot, 32, 32, -1),
	(try_end),
	(try_for_range, ":troop_no", lords_begin, lords_end),
		(troop_get_slot, reg0, ":troop_no", slot_troop_father),
		(troop_get_slot, reg1, ":troop_no", slot_troop_mother),
		(try_begin),
			(is_between, reg0, lords_begin, lords_end),
			(neg|is_between, reg1, kingdom_ladies_begin, kingdom_ladies_end),
			(troop_get_slot, reg1, reg0, slot_troop_spouse),
			(is_between, reg1, kingdom_ladies_begin, kingdom_ladies_end),
			(troop_set_slot, ":troop_no", slot_troop_mother, reg1),
			(call_script, "script_update_troop_notes", ":troop_no"),#Doesn't actually do anything
		(else_try),
			(is_between, reg1, kingdom_ladies_begin, kingdom_ladies_end),
			(neg|is_between, reg0, lords_begin, lords_end),
			(troop_get_slot, reg0, reg1, slot_troop_spouse),
			(is_between, reg0, lords_begin, lords_end),
			(troop_set_slot, ":troop_no", slot_troop_father, reg0),
			(call_script, "script_update_troop_notes", ":troop_no"),#Doesn't actually do anything
		(try_end),
	(try_end),

	#For old saved games, a reputation bug that was introduced in the release 2011-06-06 and was fixed on 2011-06-07.
	(eq, ":diplomacy_version_code", 1),
	(assign, reg0, 0),
	(try_for_range, ":troop_no", lords_begin, lords_end),
		(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_none),
		(store_random_in_range, reg1, lrep_none, lrep_roguish),
		(val_max, reg1, lrep_none + 1),#So there's an extra chance of getting reputation 1, which is lrep_martial
		(troop_set_slot, ":troop_no", slot_lord_reputation_type, reg1),
		(val_add, reg0, 1),
	(try_end),
	
	(try_begin),
		(ge, "$cheat_mode", 1),
		(store_sub, reg1, reg0, 1),
		(display_message, "@{!} Bug fix: set personality types for {reg0} {reg1?lords:lord}"),
	(try_end),
	
	(assign, reg0, 0),
	(try_for_range, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
		(neq, ":troop_no", "trp_knight_1_1_wife"),#That lady should not appear in the game
		(troop_slot_eq, ":troop_no", slot_lord_reputation_type, lrep_none),
		(store_random_in_range, reg1, lrep_conventional - 1, lrep_moralist + 1),
		(val_max, reg1, lrep_conventional),#So there's an extra chance of getting lrep_conventional
		(troop_set_slot, ":troop_no", slot_lord_reputation_type, reg1),
		(val_add, reg0, 1),
	(try_end),
	
	(try_begin),
		(ge, "$cheat_mode", 1),
		(store_sub, reg1, reg0, 1),
		(display_message, "@{!} Bug fix: set personality types for {reg0} {reg1?ladies:lady}"),
	(try_end),
   (try_end),
   
   #Behavior for an upgrade from Native or pre-Diplomacy 4.0 to Diplomacy 4.0
   (try_begin),
      (is_between, ":diplomacy_version_code", 0, 111001),
      #Fix: slot_faction_leader and slot_faction_marshall should not equal trp_player
      #if the player is not a member of the faction.  (This is initially true because
      #trp_player is 0, and uninitialized slots default to 0.)
      (try_for_range, ":faction_no", 0, dplmc_factions_end),
         (neq, ":faction_no", "fac_player_faction"),
         (neq, ":faction_no", "fac_player_supporters_faction"),
         (this_or_next|neq, ":faction_no", "$players_kingdom"),
         (eq, ":faction_no", 0),
         #The player is not a member of the faction:
         (try_begin),
            (faction_slot_eq, ":faction_no", slot_faction_leader, 0),
            (faction_set_slot, ":faction_no", slot_faction_leader, -1),
         (try_end),
         (try_begin),
            (faction_slot_eq, ":faction_no", slot_faction_marshall, 0),
            (faction_set_slot, ":faction_no", slot_faction_marshall, -1),
         (try_end),
      (try_end),
      #Initialize home slots for town merchants, elders, etc.
      (try_for_range, ":center_no", centers_begin, centers_end),
         (try_for_range, ":troop_no", dplmc_slot_town_merchants_begin, dplmc_slot_town_merchants_end),
            (party_get_slot, ":troop_no", ":center_no", ":troop_no"),
            (gt, ":troop_no", walkers_end),
            (troop_is_hero, ":troop_no"),
            (troop_slot_eq, ":troop_no", slot_troop_home, 0),
            (troop_set_slot, ":troop_no", slot_troop_home, ":center_no"),
         (try_end),
      (try_end),
      #Initialize home slots for startup merchants.  (Merchant of Praven, etc.)
      #This should be done after kings have their home slots initialized.
      (try_for_range, ":troop_no", kings_begin, kings_end),
         (troop_get_slot, ":center_no", ":troop_no", slot_troop_home),
         (val_sub, ":troop_no", kings_begin),
         (val_add, ":troop_no", startup_merchants_begin),
         (is_between, ":troop_no", startup_merchants_begin, startup_merchants_end),#Right now there's a startup merchant for each faction.  Verify this hasn't unexpectedly changed.
         (neg|troop_slot_ge, ":troop_no", slot_troop_home, 1),#Verify that the home slot is not already set
         (troop_set_slot, ":troop_no", slot_troop_home, ":center_no"),
      (try_end),
      #Reset potentially bad value in "slot_troop_stance_on_faction_issue" (i.e. 153) from auto-loot
      (eq, 153, slot_troop_stance_on_faction_issue),
      (try_for_range, ":troop_no", companions_begin, companions_end),
         (try_begin),
            (neg|troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
            (troop_set_slot, ":troop_no", slot_troop_stance_on_faction_issue, -1),
         (else_try),
            (troop_get_slot, ":slot_val", ":troop_no", slot_troop_stance_on_faction_issue),
            (neg|is_between, ":slot_val", -1, 1),#0 or -1
            (neg|is_between, ":slot_val", heroes_begin, heroes_end),
            (troop_set_slot, ":troop_no", slot_troop_stance_on_faction_issue, -1),
         (try_end),
      (try_end),
   (try_end),

   (assign, reg1, ":save_reg1"),#Revert register
   (assign, reg0, ":save_reg0"),#Revert register
   
   #Ensure $character_gender is set correctly
   (try_begin),
      (call_script, "script_cf_dplmc_troop_is_female", "trp_player"),
	  (assign, "$character_gender", 1),
   (else_try),
	  (assign, "$character_gender", 0),
   (try_end),
   ##diplomacy end+


   #The following scripts are to end quests which should have cancelled, but did not because of a bug
   (try_begin),
	(check_quest_active, "qst_formal_marriage_proposal"),
	(check_quest_failed, "qst_formal_marriage_proposal"),
    (call_script, "script_end_quest", "qst_formal_marriage_proposal"),
   (try_end),

   (try_begin),
	(check_quest_active, "qst_lend_companion"),
	(quest_get_slot, ":giver_troop", "qst_lend_companion", slot_quest_giver_troop),
	(store_faction_of_troop, ":giver_troop_faction", ":giver_troop"),
    (store_relation, ":faction_relation", ":giver_troop_faction", "$players_kingdom"), ## 1.134
    (this_or_next|lt, ":faction_relation", 0), ## 1.134
    (neg|is_between, ":giver_troop_faction", kingdoms_begin, kingdoms_end), ## 1.134
    (call_script, "script_abort_quest", "qst_lend_companion", 0),
   (try_end),



   (try_begin),
	(is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
	(neq, "$players_kingdom", "fac_player_supporters_faction"),
    (faction_slot_eq, "$players_kingdom", slot_faction_marshall, "trp_player"),
    (val_add, "$g_player_days_as_marshal", 1),
   (else_try),
    (assign, "$g_player_days_as_marshal", 0),
   (try_end),

   (try_for_range, ":town", towns_begin, towns_end),
	(party_get_slot, ":days_to_completion", ":town", slot_center_player_enterprise_days_until_complete),
    (ge, ":days_to_completion", 1),
	(val_sub, ":days_to_completion", 1),
	(party_set_slot, ":town", slot_center_player_enterprise_days_until_complete, ":days_to_completion"),
   (try_end),
    ]),
  (24,
   [
	  # Setting food bonuses in every 6 hours again and again because of a bug (we could not find its reason) which decreases especially slot_item_food_bonus slots of items to 0.
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
   ]),
  (24,
   []),
  (24,
   []),
  (24,
   []),
  (24,
   []),
  (24,
   []),
  (24,
   []),
  (24,
   []),
  (24,
   []),
  (24,
   []),


## CC - npc read book
  (1, [
     (try_for_range, ":troop_no", companions_begin, companions_end),
       (neg|map_free),
       (troop_get_slot, ":item_no", ":troop_no", slot_troop_current_reading_book),
       (gt, ":item_no", 0),
       (call_script, "script_get_troop_item_amount", ":troop_no", ":item_no"),
       (assign, ":continue", 1),
       (try_begin),
         (eq, reg0, 0),
         (troop_set_slot, "$g_talk_troop", slot_troop_current_reading_book, 0),
         (assign, ":continue", 0),
       (try_end),
       (eq, ":continue", 1),
       (store_attribute_level, ":int", ":troop_no", ca_intelligence),
       (item_get_slot, ":int_req", ":item_no", slot_item_intelligence_requirement),
       (le, ":int_req", ":int"),

       (call_script, "script_get_book_read_slot", ":troop_no", ":item_no"),
       (assign, ":slot_no", reg0),
       (troop_get_slot, ":book_read", "trp_book_read", ":slot_no"),
       (troop_get_slot, ":book_reading_progress", "trp_book_reading_progress", ":slot_no"),
       
       (eq, ":book_read", 0),
       (assign, ":read_speed", 0),
       (try_for_range, ":other_troop", companions_begin, companions_end),
         (neq, ":other_troop", ":troop_no"),
         (main_party_has_troop, ":other_troop"),
         (call_script, "script_get_book_read_slot", ":other_troop", ":item_no"),
         (assign, ":other_slot_no", reg0),
         (troop_slot_eq, "trp_book_read", ":other_slot_no", 1),
         (val_add, ":read_speed", 1),
       (try_end),
       (try_begin),
         (item_slot_eq, ":item_no", slot_item_book_read, 1),
         (val_add, ":read_speed", 1),
       (try_end),
       (val_div, ":read_speed", 4),
       (val_add, ":read_speed", 3),
       
       (val_add, ":book_reading_progress", ":read_speed"),
       (troop_set_slot, "trp_book_reading_progress", ":slot_no", ":book_reading_progress"),
       
       (ge, ":book_reading_progress", 1000),
       (troop_set_slot, "trp_book_read", ":slot_no", 1),
       (troop_set_slot, "trp_book_reading_progress", ":slot_no", 1000),
       (troop_set_slot, ":troop_no", slot_troop_current_reading_book, 0),
       
       (str_store_troop_name, s1, ":troop_no"),
       (str_store_item_name, s2, ":item_no"),
       (str_clear, s3),
       (try_begin),
         (eq, ":item_no", "itm_book_tactics"),
         (troop_raise_skill, ":troop_no", "skl_tactics", 1),
         (str_store_string, s3, "@ {s1}'s tactics skill has increased by 1."),
       (else_try),
         (eq, ":item_no", "itm_book_persuasion"),
         (troop_raise_skill, ":troop_no", "skl_persuasion", 1),
         (str_store_string, s3, "@ {s1}'s persuasion skill has increased by 1."),
       (else_try),
         (eq, ":item_no", "itm_book_leadership"),
         (troop_raise_skill, ":troop_no", "skl_leadership", 1),
         (str_store_string, s3, "@ {s1}'s leadership skill has increased by 1."),
## CC
       (else_try),
         (eq, ":item_no", "itm_book_prisoner_management"),
         (troop_raise_skill, ":troop_no", "skl_prisoner_management", 1),
         (str_store_string, s3, "@ {s1}'s prisoner management skill has increased by 1."),
## CC
## Floris
       (else_try),
         (eq, ":item_no", "itm_book_bible"),
         (troop_raise_attribute, ":troop_no", ca_charisma, 1),
         (str_store_string, s3, "@ {s1}'s charisma has increased by 1."),
       (else_try),
         (eq, ":item_no", "itm_book_necronomicon"),
         (troop_raise_skill, ":troop_no", "skl_looting", 1),
         (str_store_string, s3, "@ {s1}'s looting skill has increased by 1."),
##
       (else_try),
         (eq, ":item_no", "itm_book_intelligence"),
         (troop_raise_attribute, ":troop_no", ca_intelligence, 1),
         (str_store_string, s3, "@ {s1}'s intelligence has increased by 1."),
       (else_try),
         (eq, ":item_no", "itm_book_trade"),
         (troop_raise_skill, ":troop_no", "skl_trade", 1),
         (str_store_string, s3, "@ {s1}'s trade skill has increased by 1."),
       (else_try),
         (eq, ":item_no", "itm_book_weapon_mastery"),
         (troop_raise_skill, ":troop_no", "skl_weapon_master", 1),
         (str_store_string, s3, "@ {s1}'s weapon master skill has increased by 1."),
       (else_try),
         (eq, ":item_no", "itm_book_engineering"),
         (troop_raise_skill, ":troop_no", "skl_engineer", 1),
         (str_store_string, s3, "@ {s1}'s engineer skill has increased by 1."),
       (try_end),
       (display_message, "@{s1} have finished reading {s2}.{s3}", 0x88ff88),
       (assign, ":item_no", 0),
     (try_end),
   ]),
   
  (3, ##CABA - while testing 2.52 in WSE, was getting itermittent script errors for invalid party IDs in this trigger...though try_for_parties should include a party_is_active check. So I dunno what's up
    [
      (try_for_parties, ":party_no"),
        (party_get_template_id, ":template_id", ":party_no"),
		##Floris MTT begin
		(this_or_next|is_between, ":template_id", "pt_looters", "pt_looters_r"),
		(this_or_next|is_between, ":template_id", "pt_looters_r", "pt_looters_e"),
		(this_or_next|is_between, ":template_id", "pt_looters_e", "pt_deserters"),
		(eq, ":template_id", "pt_deserters"),
		##Floris MTT end
        (try_for_parties, ":party_no_2"),
          (neq, ":party_no_2", ":party_no"),
          (party_get_template_id, ":template_id_2", ":party_no_2"),
          (eq, ":template_id_2", ":template_id"),
          (party_get_battle_opponent, ":opponent", ":party_no_2"),
          (lt, ":opponent", 0),
          (party_get_attached_to, ":attached_to",":party_no_2"),
          (lt, ":attached_to", 0),
          (party_stack_get_troop_id, ":leader_2", ":party_no_2", 0),
          (neg|troop_is_hero, ":leader_2"),
          (party_get_num_companions, ":party_size", ":party_no"),
          (party_get_num_companions, ":party_size_2", ":party_no_2"),
          (store_add, ":party_total_size", ":party_size", ":party_size_2"),
          (store_character_level, ":player_level", "trp_player"),
          (val_mul, ":player_level", 3),
          (val_div, ":player_level", 2),
          (store_add, ":party_size_limit", ":player_level", 20),
          (try_begin),
            (party_stack_get_troop_id, ":leader", ":party_no", 0),
            (troop_is_hero, ":leader"),
            (val_mul, ":party_size_limit", 2),
          (try_end),
          (le, ":party_total_size", ":party_size_limit"),
          (store_distance_to_party_from_party, ":dist", ":party_no", ":party_no_2"),
          (le, ":dist", 4),
          (call_script, "script_party_add_party", ":party_no", ":party_no_2"),
          (party_detach, ":party_no_2"),
          (remove_party, ":party_no_2"),
        (try_end),
      (try_end),
    ]),
   
  (24,
    [
      #(try_for_range, ":loop_var", "trp_kingdom_heroes_including_player_begin", companions_end),
        #(assign, ":cur_troop", ":loop_var"),
        #(try_begin),
          #(eq, ":loop_var", "trp_kingdom_heroes_including_player_begin"),
          #(assign, ":cur_troop", "trp_player"),
        #(try_end),
        #(main_party_has_troop, ":cur_troop"),
        #(assign, ":continue", 0),
        #(try_for_range, ":slot_proficiency_type", slot_one_handed_proficiency_limit, slot_throwing_proficiency_limit+1),
          #(store_sub, ":proficiency_type", ":slot_proficiency_type", slot_one_handed_proficiency_limit),
          #(val_add, ":proficiency_type", wpt_one_handed_weapon),
          #(troop_get_slot, ":slot_proficiency_limit", ":cur_troop", ":slot_proficiency_type"),
          #(troop_get_slot, ":slot_all_proficiency_limit", ":cur_troop", slot_all_proficiency_limit),
          
          #(try_begin),
            #(eq, ":slot_proficiency_limit", 0),
            #(val_add, ":slot_proficiency_limit", proficiency_limit_increase),
          #(else_try),
            #(eq, ":slot_all_proficiency_limit", 0),
            #(val_add, ":slot_all_proficiency_limit", proficiency_limit_increase),
          #(try_end),
          
          #(str_store_troop_name, s1, ":cur_troop"),
          #(str_clear, s2),
          #(store_sub, ":out_string", ":proficiency_type", wpt_one_handed_weapon),
          #(val_add, ":out_string", "str_one_handed_weapon"),
          #(str_store_string, s2, ":out_string"),
          
          #(str_clear, s3),
          #(store_div, ":out_string", ":slot_proficiency_limit", proficiency_limit_increase),
          #(val_sub, ":out_string", 1),
          #(val_add, ":out_string", "str_level_d"),
          #(str_store_string, s3, ":out_string"),
          
          #(store_proficiency_level, ":weapon_proficiency", ":cur_troop", ":proficiency_type"),
          #(try_begin),
            #(ge, ":weapon_proficiency", ":slot_proficiency_limit"),
            #(display_message, "@{s1}'s proficiency in {s2}has reach level {s3}."),
            #(try_begin),
              #(eq, ":slot_proficiency_type", slot_one_handed_proficiency_limit),
              #(troop_raise_attribute, ":cur_troop", ca_agility, 1),
              #(display_message, "@+1 agility."),
            #(else_try),
              #(eq, ":slot_proficiency_type", slot_two_handed_proficiency_limit),
              #(call_script, "script_troop_raise_skill_limit", ":cur_troop", skl_power_strike, 1),
              #(display_message, "@+1 power strike."),
            #(else_try),
              #(eq, ":slot_proficiency_type", slot_polearm_proficiency_limit),
              #(troop_raise_attribute, ":cur_troop", ca_strength, 1),
              #(display_message, "@+1 strength."),
            #(else_try),
              #(eq, ":slot_proficiency_type", slot_archery_proficiency_limit),
              #(call_script, "script_troop_raise_skill_limit", ":cur_troop", skl_power_draw, 1),
              #(display_message, "@+1 power draw."),
            #(else_try),
              #(eq, ":slot_proficiency_type", slot_crossbow_proficiency_limit),
              #(troop_raise_attribute, ":cur_troop", ca_strength, 1),
              #(display_message, "@+1 strength."),
            #(else_try),
              #(eq, ":slot_proficiency_type", slot_throwing_proficiency_limit),
              #(call_script, "script_troop_raise_skill_limit", ":cur_troop", skl_power_throw, 1),
              #(display_message, "@+1 power throw."),
            #(try_end),
            #(val_add, ":slot_proficiency_limit", proficiency_limit_increase),
            #(troop_set_slot, ":cur_troop", ":slot_proficiency_type", ":slot_proficiency_limit"),
          #(else_try),
            #(ge, ":weapon_proficiency", ":slot_all_proficiency_limit"),
            #(val_add, ":continue", 1),
          #(try_end),
          #(try_begin),
            #(eq, ":continue", 6),
            #(call_script, "script_troop_raise_skill_limit", ":cur_troop", skl_weapon_master, 1),
            
            #(str_clear, s3),
            #(store_div, ":out_string", ":slot_all_proficiency_limit", proficiency_limit_increase),
            #(val_sub, ":out_string", 1),
            #(val_add, ":out_string", "str_level_d"),
            #(str_store_string, s3, ":out_string"),
            #(display_message, "@{s1}'s proficiency in all weapons have reach level {s3}."),
            #(display_message, "@+1 weapon_master"),
            #(val_add, ":slot_all_proficiency_limit", proficiency_limit_increase),
            #(troop_set_slot, ":cur_troop", slot_all_proficiency_limit, ":slot_all_proficiency_limit"),
          #(try_end),
        #(try_end),
      #(try_end),
    ]),

   (1,
    [
        (try_for_range, ":troop_no", heroes_begin, heroes_end),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
          (troop_get_slot, ":troop_party_no", ":troop_no", slot_troop_leaded_party),
          (ge, ":troop_party_no", 1),
          (party_get_attached_to, ":cur_attached_town", ":troop_party_no"),
          (ge, ":cur_attached_town", 1),
          (call_script, "script_get_relation_between_parties", ":cur_attached_town", ":troop_party_no"),
          (try_begin),
            (lt, reg0, 0),
            (party_detach, ":troop_party_no"),
          (try_end),
        (try_end),
     ]),
]
