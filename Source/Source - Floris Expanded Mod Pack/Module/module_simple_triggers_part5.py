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



simple_triggers_part5 = [

  
  # affilated family ai
   (24 * 7,
   [
	##nested diplomacy start+ (piggyback on this trigger) allow lords to return from exile
	(assign, ":save_reg0", reg0),
	(assign, ":save_reg1", reg1),
	(assign, ":save_reg4", reg4),
	(try_begin),
		#only proceed if setting is enabled
		(ge, "$g_dplmc_lord_recycling", DPLMC_LORD_RECYCLING_ENABLE),
		#Kings/pretenders do not return in this manner (it should be different if it does happen).
		#Companions have a separate mechanism for return.
		(assign, ":chosen_lord", -1),
		(assign, ":best_score", -101),
		(assign, ":num_exiles", 0),
		#iterate over lords from a random start point, wrapping back to zero
		#(store_random_in_range, ":rand_no", lords_begin, lords_end),
		(try_for_range, ":troop_no", lords_begin, lords_end),				# formerly :index_no changed to get rid of invalid troops
		  # (store_add, ":troop_no", ":rand_no", ":index"),
		  # (try_begin),
			# #wrap back around when you go off the end
			# (ge, ":troop_no", lords_end),
			# (val_sub, ":troop_no", lords_end),
			# (val_add, ":troop_no", lords_begin),
		  # (try_end),
		  #Elsewhere we do the bookkeeping of ensuring that when a lord gets exiled
		  #his occupation changes to dplmc_slto_exile, and when loading a Native
		  #saved gamed with diplomacy we make this change for any lords required.
		  (troop_slot_eq, ":troop_no", slot_troop_occupation, dplmc_slto_exile), ## BUG - invalid troop ID 1868-1890
		  
		  (store_troop_faction, ":faction_no", ":troop_no"),
		  (this_or_next|eq, ":faction_no", -1),
		  (this_or_next|eq, ":faction_no", "fac_commoners"),
			 (eq, ":faction_no", "fac_outlaws"),
		  (val_add, ":num_exiles", 1),
		  (try_begin),
		     #Pick the lord with the best relation with his original liege.
			  #In most cases this will be the lord that has been in exile
			  #the longest.
			  (troop_get_slot, ":new_faction", ":troop_no", slot_troop_original_faction),
			  (is_between, ":new_faction", kingdoms_begin, kingdoms_end),
			  (faction_get_slot, ":faction_leader", ":new_faction", slot_faction_leader),
			  (gt, ":faction_leader", 0),
			  (call_script, "script_troop_get_relation_with_troop", ":troop_no", ":faction_leader"),
			  (this_or_next|eq, ":chosen_lord", -1),
			     (gt, reg0, ":best_score"),
			  (assign, ":chosen_lord", ":troop_no"),
			  (assign, ":best_score", reg0),
		  (else_try),
		     (eq, ":chosen_lord", -1),
			 (assign, ":chosen_lord", ":troop_no"),
		  (try_end),
      (try_end),
		#search is done
		(try_begin),
		 #no lord found
		 (eq, ":chosen_lord", -1),
		 (try_begin),
			(ge, "$cheat_mode", 1),
			(display_message, "@{!}DEBUG - no eligible lords in exile"),
		 (try_end),
	    (else_try),
			#If there were fewer than 3 lords in exile, random chance that none will return.
			(lt, ":num_exiles", 3),
			(store_random_in_range, ":random", 0, 256),
			(ge, ":random", 128),
			(try_begin),
				(ge, "$cheat_mode", 1),
				(assign, reg0, ":num_exiles"),
				(display_message, "@{!}DEBUG - {reg0} lords found in exile; randomly decided not to try to return anyone."),
			(try_end),
		(else_try),
		 #found a lord
		 (neq, ":chosen_lord", -1),
		 (try_begin),
			(ge, "$cheat_mode", 1),
			(str_store_troop_name, s4, ":chosen_lord"),
			(assign, reg0, ":best_score"),
			(assign, reg1, ":num_exiles"),
			(display_message, "@{!}DEBUG - {reg1} lords found in exile; {s4} chosen to return, score was {reg0}"),
		 (try_end),
		 #To decrease the displeasing fragmentation of lord cultures, bias towards assigning
		 #the lord back to his original faction if possible.
		 (troop_get_slot, ":new_faction", ":chosen_lord", slot_troop_original_faction),
		 (try_begin),
			 #If the original faction is not active, or the lord's relation is too low, use a different faction
			 (this_or_next|lt, ":best_score", -50),
			 (this_or_next|neg|is_between, ":new_faction", kingdoms_begin, kingdoms_end),
			    (neg|faction_slot_eq, ":new_faction", slot_faction_state, sfs_active),
		    (call_script, "script_lord_find_alternative_faction", ":chosen_lord"),
			(assign, ":new_faction", reg0),
		 (try_end),
		 (try_begin),
		   (neg|is_between, ":new_faction", kingdoms_begin, kingdoms_end),
			(ge, "$cheat_mode", 1),
			(str_store_troop_name, s4, ":chosen_lord"),
			(display_message, "@{!}DEBUG - {s4} found no faction to return to!"),
		 (try_end),
		 (is_between, ":new_faction", kingdoms_begin, kingdoms_end),
		 (assign, ":num_inactive", 0),
		 (try_begin),
			(eq, ":new_faction", "$players_kingdom"),
			(call_script, "script_dplmc_get_troop_standing_in_faction", "trp_player", "$players_kingdom"),
			(ge, reg0, DPLMC_FACTION_STANDING_LEADER_SPOUSE),
			(assign, ":num_inactive", 0),
			(try_for_range, ":other_lord", lords_begin, lords_end),
			   (store_troop_faction, ":other_lord_faction", ":other_lord"),
			   (this_or_next|eq, ":other_lord_faction", "fac_player_supporters_faction"),
				(eq, ":other_lord_faction", "$players_kingdom"),
			   (troop_slot_eq, ":other_lord", slot_troop_occupation, slto_inactive),
			   (val_add, ":num_inactive", 1),
			(try_end),
			(gt, ":num_inactive", 1),
			(try_begin),
				(ge, "$cheat_mode", 1),
				(assign, reg0, ":num_inactive"),
				(display_message, "@{!}DEBUG - Not returning a lord to the player's kingdom, since there are already {reg0} lords waiting for their petitions to be heard."),
			(try_end),
		 (else_try),
			(call_script, "script_dplmc_lord_return_from_exile", ":chosen_lord", ":new_faction"),
		 (try_end),
		(try_end),
	(try_end),
	##More piggybacking
	##
	(assign, reg0, ":save_reg0"),
	(assign, reg1, ":save_reg1"),
	(assign, reg4, ":save_reg4"),
	##nested diplomacy end+
    (is_between, "$g_player_affiliated_troop", lords_begin, kingdom_ladies_end),
	##nested diplomacy start+
	(assign, ":best_relation", -101),
	(assign, ":worst_relation", 101),
	
	(assign, ":num_at_least_20", 0),
	(assign, ":num_below_0", 0),
	
	(assign, ":good_relation", 0),
	##nested diplomacy end+

    (assign, ":bad_relation", 0),
    (try_for_range, ":family_member", lords_begin, kingdom_ladies_end),
      (call_script, "script_dplmc_is_affiliated_family_member", ":family_member"),
      (gt, reg0, 0),
      (call_script, "script_troop_get_player_relation", ":family_member"),
	  ##nested diplomacy start+
	  #(le, reg0, -20),
	  #(assign, ":bad_relation", ":family_member"),
  	  (try_begin),
		(lt, reg0, 0),
		(val_add, ":num_below_0", 1),
		(le, reg0, ":worst_relation"),
		(assign, ":bad_relation", ":family_member"),
	  (else_try),
		(ge, reg0, 20),
		(val_add, ":num_at_least_20", 1),
		(gt, reg0, ":best_relation"),
		(assign, ":good_relation", ":family_member"),
	  (try_end),

	  (val_max, ":best_relation", reg0),
	  (val_min, ":worst_relation", reg0),
	  ##nested diplomacy end+      
    (try_end),
	##nested diplomacy start+
	(try_begin),
		(gt, ":worst_relation", -15),
		(assign, ":bad_relation", 0),#suppress with no message
	(else_try),
		(gt, ":worst_relation", -20),
		(str_store_troop_name, s0, ":bad_relation"),
		(display_message, "@{s0} is grumbling against you.  Your affiliation could be jeopardized if this continues."),
		(str_clear, s0),
	(else_try),
		(neq, ":bad_relation", 0),
		(ge, ":num_at_least_20", ":num_below_0"),
		(store_add, reg0, ":worst_relation", ":best_relation"),
		(ge, reg0, 0),
		(str_store_troop_name, s0, ":bad_relation"),
		(str_store_troop_name, s1, ":good_relation"),
		(display_message, "@{s0} is grumbling against you, but with {s1}'s support you remain affiliated for now."),
		(str_clear, s0),
		(str_clear, s1),
		(assign, ":bad_relation", 0),
	(try_end),
	##nested diplomacy end+
    (try_begin),
      (eq, ":bad_relation", 0),

      (try_for_range, ":family_member", lords_begin, kingdom_ladies_end),
        (call_script, "script_dplmc_is_affiliated_family_member", ":family_member"),
        (gt, reg0, 0),
        (try_begin),
           (troop_slot_ge, ":family_member", slot_troop_prisoner_of_party, 0),
           ##diplomacy start+ skip relationship decay for imprisonment when the player himself is imprisoned or wounded
           (neg|troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 1),
           (neg|troop_is_wounded, "trp_player"),
           ##diplomacy end+
           (call_script, "script_change_player_relation_with_troop", ":family_member", -1),
        (else_try),
          (call_script, "script_change_player_relation_with_troop", ":family_member", 1),
        (try_end),
      (try_end),
    (else_try),
      (call_script, "script_add_notification_menu", "mnu_dplmc_affiliate_end", ":bad_relation", 0),
      (call_script, "script_dplmc_affiliate_end", 1),
    (try_end),
    ##nested diplomacy start+
 	 (assign, reg0, ":save_reg0"),
	 (assign, reg1, ":save_reg1"),
	 (assign, reg4, ":save_reg4"),
    ##nested diplomacy end+
    ]),

   (2,
   [
    (assign, ":has_walled_center", 0),
    (assign, ":has_fief", 0),
    (try_for_range, ":center_no", centers_begin, centers_end),
      (party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
      (eq, ":lord_troop_id", "trp_player"),
      (try_begin),
        (is_between, ":center_no", walled_centers_begin, walled_centers_end),
        (assign, ":has_walled_center", 1),
      (try_end),
      (assign, ":has_fief", 1),
    (try_end),

    (try_begin),
      (eq, ":has_walled_center", 0),
      (this_or_next|neq, "$g_player_constable", 0),
      (neq, "$g_player_chancellor", 0),
      (assign, "$g_player_constable", 0),
      (assign, "$g_player_chancellor", 0),
    (try_end),

    (try_begin),
      (eq, ":has_fief", 0),
      (neq, "$g_player_chamberlain", 0),
      (assign, "$g_player_chamberlain", 0),

      ##nested diplomacy start+
      #Adjust gold loss by difficulty
      (assign, ":save_reg0", reg0),
      (assign, ":save_reg1", reg1),

      (assign, ":loss_numerator", 2),
      (assign, ":loss_denominator", 3),

      (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
      (try_begin),
         (eq, ":reduce_campaign_ai", 0), #hard, lose 5/6
	 (assign, ":loss_numerator", 5),
	 (assign, ":loss_denominator", 6),
      (else_try),
         (eq, ":reduce_campaign_ai", 1), #medium, lose 2/3
	 (assign, ":loss_numerator", 2),
	 (assign, ":loss_denominator", 3),
      (else_try),
         (eq, ":reduce_campaign_ai", 2), #easy, lose 1/2
	 (assign, ":loss_numerator", 1),
	 (assign, ":loss_denominator", 2),
      (try_end),

      (store_troop_gold, ":cur_gold", "trp_household_possessions"),
      (try_begin),
        (gt, ":cur_gold", 0),
        #(call_script, "script_dplmc_withdraw_from_treasury", ":cur_gold"),
        #(val_div, ":cur_gold", 3),
        #(call_script, "script_troop_add_gold", "trp_player", ":cur_gold"),
        #(display_message, "@Your last fief was captured and you lost 2/3 of your treasury"),
	(store_mul, ":lost_gold", ":cur_gold", ":loss_numerator"),
	(val_div, ":lost_gold", ":loss_denominator"),
	(val_mul, ":lost_gold", -1),
	(call_script, "script_dplmc_withdraw_from_treasury", ":lost_gold"),
	(assign, reg0, ":loss_numerator"),
	(assign, reg1, ":loss_denominator"),
	(display_message, "@Your last fief was captured and you lost {reg0}/{reg1} of your treasury"),
      (try_end),

      (assign, reg0, ":save_reg0"),
      (assign, reg1, ":save_reg1"),
      ##nested diplomacy end+
    (try_end),
    ]),

   (24,
   [
      (try_for_range, ":faction1", npc_kingdoms_begin, npc_kingdoms_end),
        (assign, ":attitude_change", 2), #positive means good attitude
        (try_for_range, ":faction2", kingdoms_begin, kingdoms_end),
          (neq, ":faction1", ":faction2"),
		  ##diplomacy start+
		  #FIX: Stop the attitude change from carrying over from the previous kingdom!
		  (assign, ":attitude_change", 2),
		  #Handling for fac_player_supporters_faction & players_kingdom
		  (assign, ":alt_faction", ":faction2"),
		  (try_begin),
		     (eq, ":faction2", "fac_player_supporters_faction"),
			 (neq, ":faction1", "$players_kingdom"),
			 (assign, ":alt_faction", "$players_kingdom"),
		  (else_try),
		     (eq, ":faction2", "$players_kingdom"),
			 (assign, ":alt_faction", "fac_player_supporters_faction"),
		  (try_end),
		  ##Make loop less wasteful.
		  ##OLD:
          #(try_for_parties, ":party"),
          #  (is_between, ":party", centers_begin, centers_end),
		  ##NEW:
		  (try_for_range, ":party", centers_begin, centers_end),
		  ##diplomacy end+
            (store_faction_of_party, ":party_faction", ":party"),
			##diplomacy start+
			##FIX broken slot check!
			##ADD support for player's faction
			##OLD:
            #(eq, ":party_faction", ":faction2"),
            #(party_slot_eq, ":faction1", ":party", slot_center_original_faction),
			##NEW:
			(this_or_next|eq, ":party_faction", ":faction2"),
				(eq, ":party_faction", ":alt_faction"),
			(party_slot_eq, ":party", slot_center_original_faction, ":faction1"),
			#Don't subtract relation when it would be nonsensical
			(this_or_next|neq, ":faction1", "$players_kingdom"),
			(this_or_next|neq, ":faction2", "fac_player_supporters_faction"),
				(party_slot_ge, ":party", dplmc_slot_center_original_lord, 1),
			##diplomacy end+
            (val_sub, ":attitude_change", 1), #less attitude
          (try_end),

          (try_for_range, ":faction3", kingdoms_begin, kingdoms_end),
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":faction2", ":faction3"),
            (eq, reg0, -2), #war between 2 and 3
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":faction1", ":faction3"),
            (eq, reg0, -2), #war between 1 and 3
            (val_add, ":attitude_change", 1), #higher attitude
          (try_end),
        (try_end),

        (store_add, ":faction1_to_faction2_slot", ":faction2", dplmc_slot_faction_attitude_begin),
        (party_set_slot, ":faction1", ":faction1_to_faction2_slot", ":attitude_change"),
      (try_end),
    ]),

  ##diplomacy end

#TEMPERED                  #########################  CHECK FOR ENTRENCHMENT FINISHED  ##############################

  (0, [	(party_get_slot,":entrenched","p_main_party",slot_party_entrenched),
		(eq,"$g_camp_mode", 1),
		(eq,":entrenched",-1),
		(store_current_hours,":cur_hour"),
		(try_begin),
			(ge,":cur_hour","$entrench_time"),
			(set_spawn_radius,0),
			(spawn_around_party,"p_main_party","pt_entrench"),
			(assign,"$current_camp_party",reg0),
			(party_set_slot,"$current_camp_party",slot_village_state,1),
			(party_set_slot,"$current_camp_party",slot_party_type,spt_entrenchment),
			(party_set_slot,"p_main_party",slot_party_entrenched,1),
			(display_message,"@_Camp defenses have been completed."),
			(assign,"$entrench_time",0),
			(jump_to_menu,"mnu_camp"),
		(try_end),
       ]),
#TEMPERED                    ##########################           CHECK FOR NO LONGER ENTRENCHED    ##########################

  (0, [ (eq,"$g_player_icon_state",pis_normal),
		(eq, "$g_camp_mode", 0),#not camping
		(try_begin),
			(party_slot_eq,"p_main_party",slot_party_entrenched,1), #entrenched			
			(party_set_slot,"p_main_party",slot_party_entrenched,0), #not entrenched
			#(try_begin),
				#(party_slot_eq,"$current_camp_party",slot_village_state,1),#Tempered check to see if player just left entrenchment
				(party_set_slot,"$current_camp_party",slot_village_state,2),
				(store_current_hours,":cur_hour"),
				(val_add,":cur_hour",72),
				(party_set_slot,"$current_camp_party",slot_village_smoke_added,":cur_hour"),
				(party_add_particle_system, "$current_camp_party", "psys_map_village_fire_smoke"),
			#(try_end),
		(else_try),
			(party_slot_eq,"p_main_party",slot_party_entrenched,-1), #working on entrenchment
			(party_set_slot,"p_main_party",slot_party_entrenched,0), #not entrenched
		(try_end),	
		(assign,"$current_camp_party",-1),
       ]),
#TEMPERED                    ##########################         Deteriorate abandoned entrenchments    ##########################

  (3, [ (try_for_parties,":current_party"),
			(party_slot_eq,":current_party",slot_party_type,spt_entrenchment),
			(party_slot_eq,":current_party",slot_village_state,2),
			(party_get_slot,":end_hour",":current_party",slot_village_smoke_added),
			(store_current_hours,":cur_hour"),
			(gt,":cur_hour",":end_hour"),
			(party_clear_particle_systems, ":current_party"),
			(remove_party,":current_party"),
		(try_end),
		#(party_set_flags, ":new_camp", pf_icon_mask, 1),
       ]),   

##Floris: A simple trigger that checks the current version of the Floris Expanded Mod Pack. The version number is defined in module_constants.py.
##Also does a few other mod tasks
(0, [
    (try_begin),
        (party_slot_eq, "p_main_party", slot_party_pref_wp_prof_decrease, 2),
        (call_script, "script_weather_restore_proficiencies"),
        (party_set_slot, "p_main_party", slot_party_pref_wp_prof_decrease, 1),
    (try_end),
	(try_begin),
		(game_key_clicked, gk_view_orders),
		(start_presentation, "prsnt_mod_option"),
	(try_end),	
    (try_begin), #To allow player to cancel/move around during village raid
      (ge,"$g_player_raiding_village",1),
      (store_distance_to_party_from_party, ":distance", "$g_player_raiding_village", "p_main_party"),
      (try_begin),
        (gt, ":distance", raid_distance),
        (str_store_party_name_link, s1, "$g_player_raiding_village"),
        (display_message, "@You have broken off your raid of {s1}."),
        (call_script, "script_village_set_state", "$current_town", 0),
        (party_set_slot, "$current_town", slot_village_raided_by, -1),
        (assign, "$g_player_raiding_village", 0),
        (rest_for_hours, 0, 0, 0), #stop resting - abort
      (else_try),
        (ge, ":distance", raid_distance / 2),
        (map_free),
        (jump_to_menu, "mnu_village_loot_continue"),
      (try_end),
	(try_end),
	(try_begin),
	  (gt,"$auto_besiege_town",0),
      (gt,"$g_player_besiege_town", 0),
      (ge, "$g_siege_method", 1),
   
      (store_distance_to_party_from_party, ":distance", "$g_player_besiege_town", "p_main_party"),
      (try_begin),
        (gt, ":distance", raid_distance / 2),
        (str_store_party_name_link, s1, "$g_player_besiege_town"),
        (display_message, "@You have broken off your siege of {s1}."),
        (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
        (assign, "$g_player_besiege_town", -1),
        (rest_for_hours, 0, 0, 0), #stop resting - abort
      (else_try),
        (ge, ":distance", raid_distance / 3),
        (map_free),
        (str_store_party_name_link, s1, "$g_player_besiege_town"),
        (display_message, "@You cannot maintain your siege of {s1} from this distance. You risk your lines breaking."),
      (else_try),
        (store_current_hours, ":cur_hours"),
        (ge, ":cur_hours", "$g_siege_method_finish_hours"),
		(eq, "$g_siege_force_wait", 0), #bugfix?
        (neg|is_currently_night),
        (rest_for_hours, 0, 0, 0), #stop resting, if resting
        (start_encounter, "$auto_besiege_town"),
      (try_end),
	(try_end),	

    (neq, "$g_mod_version", floris_version),
	#(try_begin), #Version 2.41 Fixes (25)
	
    #(try_begin), #Version 2.4 Fixes (24)
    #    (lt, "$g_mod_version", 24),
	(call_script, "script_init_item_score"), ##just in case
	(call_script, "script_init_all_keys"),
	(call_script, "script_floris_set_default_prefs", 1),
	(try_begin),
		(neg|party_slot_eq, "p_town_1", slot_town_is_coastal, 4),
		(call_script, "script_initialize_sea_trade_routes"),
	(try_end),
		
	(try_begin),
		(neq, "$g_mod_version", 0),
		(display_message, "@Floris Bugfixed^Mod Options and Key Configuration Reset."),

		##attempted bug fix for old saves - player getting duplicated when taken prisoner/losing denars
		(try_begin),
			(troop_slot_ge, "trp_player", slot_troop_prisoner_of_party, 1),
			(troop_get_slot, ":party_no", "trp_player", slot_troop_prisoner_of_party),
			(assign, "$do_not_cancel_quest", 1),
			(call_script, "script_remove_troop_from_prison", "trp_player"),
			(assign, "$do_not_cancel_quest", 0),
			(party_is_active, ":party_no"),
			(party_count_prisoners_of_type, reg0, ":party_no", "trp_player"),
			(gt, reg0, 0),
			(party_remove_prisoners, ":party_no", "trp_player", reg0),
			(gt, reg0, 0), #number removed
		(try_end),
		(try_for_parties, ":party_no"),
			(party_count_prisoners_of_type, reg0, ":party_no", "trp_player"),
			(gt, reg0, 0),
			(party_remove_prisoners, ":party_no", "trp_player", reg0),
		(try_end),
		(troop_set_slot, "trp_player", slot_troop_leaded_party, "p_main_party"),
		(str_clear, s5),
		(add_troop_note_from_sreg, "trp_player", 2, s5, 0), #clear if the it reported the player was prisoner
		
		(party_get_slot, ":custom_state", "p_main_party", slot_custom_army),
		(try_begin),
			(eq, ":custom_state", 100),
			(troop_set_slot, "trp_custom_master", slot_troop_state, 1),
		(else_try),
			(is_between, ":custom_state", towns_begin, towns_end),
			(troop_set_slot, "trp_custom_master", slot_troop_state, 2),
			(troop_set_slot, "trp_custom_master", slot_troop_cur_center, ":custom_state"),
		(try_end),
		
		(neq, "$freelancer_state", 0),
		(neg|check_quest_active, "qst_freelancer_enlisted"),
		(store_troop_faction, ":commander_faction", "$enlisted_lord"),
		(str_store_troop_name_link, s13, "$enlisted_lord"),
		(str_store_faction_name_link, s14, ":commander_faction"),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_target_party, "$enlisted_party"),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_importance, 5),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_xp_reward, 1000),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_gold_reward, 100),
		(setup_quest_text, "qst_freelancer_enlisted"),
		(str_clear, s2), #description. necessary?
        (call_script, "script_start_quest", "qst_freelancer_enlisted", "$enlisted_lord"),
		(str_store_troop_name, s5, "$player_cur_troop"),
		(str_store_string, s1, "@Enlisted as a {s5} in the party of {s13} of {s14}."),
		(add_troop_note_from_sreg, "trp_player", 3, s1, 0),
		(str_store_string, s5, "@Current rank: {s5}"),
        (add_quest_note_from_sreg, "qst_freelancer_enlisted", 3, s5, 1),	
		
		(troop_get_slot, reg0, "trp_player", slot_troop_freelancer_start_xp),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_freelancer_start_xp, reg0),
		(troop_get_slot, reg0, "trp_player", slot_troop_freelancer_start_date),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_freelancer_start_date, reg0),
		(party_get_slot, reg0, "p_main_party", slot_party_orig_morale),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_freelancer_orig_morale, reg0),
		(call_script, "script_freelancer_get_upgrade_xp", "$player_cur_troop"),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_freelancer_upgrade_xp, reg0),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_freelancer_banner_backup, 0),
		(quest_set_slot, "qst_freelancer_enlisted", slot_quest_freelancer_next_payday, "$g_next_pay_time"),
		
		(eq, "$freelancer_state", 2), #vacation
		(str_store_troop_name_link, s13, "$enlisted_lord"),
		(str_store_faction_name_link, s14, ":commander_faction"),
		(quest_set_slot, "qst_freelancer_vacation", slot_quest_target_party, "$enlisted_party"),
		(quest_set_slot, "qst_freelancer_vacation", slot_quest_importance, 0),
		(quest_set_slot, "qst_freelancer_vacation", slot_quest_xp_reward, 50),
		(quest_set_slot, "qst_freelancer_vacation",	slot_quest_expiration_days, 10),
		(setup_quest_text, "qst_freelancer_vacation"),
		(str_clear, s2), #description. necessary?
        (call_script, "script_start_quest", "qst_freelancer_vacation", "$enlisted_lord"),		
	(try_end),
	
	# --- Lieutenant recruitment notification purge ---
	# The old code called script_add_notification_menu for mnu_lieutenant_recruitment,
	# leaving stale entries in trp_notification_menu_types that caused the menu to fire
	# every time the player resumed travel. This block compacts them out of the queue.
	(assign, ":write_slot", 0),
	(try_for_range, ":read_slot", 0, 80), # Fixed range is necessary, try_for_range evaluates limit once.
	  (troop_get_slot, ":queued_menu", "trp_notification_menu_types", ":read_slot"),
	  (try_begin),
	    (gt, ":queued_menu", 0),
	    (try_begin),
	      # Skip (discard) any lieutenant_recruitment entries
	      (eq, ":queued_menu", "mnu_lieutenant_recruitment"),
	    (else_try),
	      # Keep all other entries - copy them to the write position
	      (troop_set_slot, "trp_notification_menu_types", ":write_slot", ":queued_menu"),
	      (troop_get_slot, ":var1", "trp_notification_menu_var1", ":read_slot"),
	      (troop_set_slot, "trp_notification_menu_var1", ":write_slot", ":var1"),
	      (troop_get_slot, ":var2", "trp_notification_menu_var2", ":read_slot"),
	      (troop_set_slot, "trp_notification_menu_var2", ":write_slot", ":var2"),
	      (val_add, ":write_slot", 1),
	    (try_end),
	  (try_end),
	(try_end),
	# Zero out any trailing slots left after compaction
	(try_for_range, ":clear_slot", ":write_slot", 80),
	  (troop_set_slot, "trp_notification_menu_types", ":clear_slot", 0),
	  (troop_set_slot, "trp_notification_menu_var1", ":clear_slot", 0),
	  (troop_set_slot, "trp_notification_menu_var2", ":clear_slot", 0),
	(try_end),
	# --- End lieutenant recruitment notification purge ---

    (assign, "$g_mod_version", floris_version),
  ]),

#LAZERAS MODIFIED  {BANK OF CALRADIA}		#	Floris Overhaul

  (24 * 7,
   [
	(neq, "$g_infinite_camping", 1),
	(assign, ":end", towns_end),
	(try_for_range, ":center_no", towns_begin, ":end"),
		(this_or_next|party_slot_ge, ":center_no", slot_town_player_acres, 1),
		(this_or_next|party_slot_ge, ":center_no", slot_town_bank_assets, 1),
		(party_slot_ge, ":center_no",slot_town_bank_debt, 1),
		(assign, ":end", towns_begin), #break
	(try_end),
	(eq, ":end", towns_begin), #ONLY DISPLAY BANK PRESENTATION IF THE PLAYER IS USING BANK
	(start_presentation, "prsnt_bank_quickview"),
    ]),
#LAZERAS MODIFIED  {BANK OF CALRADIA}

#LAZERAS MODIFIED  {Top Tier Troops Recruit}
  (24,
   [
	#	Floris Entirely Rewritten // Based on troop experience instead of time passed, also checks whether the troop is actually in the player party
	(party_get_num_companion_stacks, ":range", "p_main_party"),
	(try_for_range, ":stack_no", 0, ":range"),
		(party_stack_get_troop_id, ":troop_no", "p_main_party", ":stack_no"),
		(neg|troop_is_hero, ":troop_no"),
		(assign, ":end", "trp_town_1_seneschal"),
		(try_for_range, ":hero_troop", "trp_swadian_n_hero1", ":end"),
			(troop_slot_eq, ":hero_troop" , slot_troop_occupation, ":troop_no"),
			(assign, ":end", ":hero_troop"),
		(try_end),
		(neq, ":end", "trp_town_1_seneschal"),
		(troop_get_xp, ":experience", ":troop_no"),
		(ge, ":experience", 2000000), 
		(jump_to_menu, "mnu_upgrade_to_hero"),
	(try_end),
    ]),   
##LAZERAS MODIFIED  {Top Tier Troops Recruit} 


#TEMPERED                     ########################      CHECK FOR SIEGE CAMP COMPLETE  OR OUT OF RANGE   ##################################
	(0,	[	(party_slot_eq,"p_main_party",slot_party_siege_camp,-1),
			(store_current_hours,":cur_hour"),
			(try_begin),
				(lt, "$g_player_besiege_town", 1),
				(party_set_slot,"p_main_party",slot_party_siege_camp,0),
				(assign,"$entrench_time",0),
			(else_try),				
				(gt, "$g_player_besiege_town", 0),
				(store_distance_to_party_from_party, ":distance", "$g_player_besiege_town", "p_main_party"),
				(try_begin),
					(le,":distance",3),
					(ge,":cur_hour","$entrench_time"),
					(party_set_slot,"p_main_party",slot_party_siege_camp,1),
					(assign,"$entrench_time",0),
				(else_try),
					(gt,":distance",3),
					(party_set_slot,"p_main_party",slot_party_siege_camp,0),
					(display_message,"@ Your siege camp was destroyed while you were away!"),
					(assign,"$entrench_time",0),
				(try_end),
			(try_end),
		]),
#TEMPERED CHECK FOR SIEGE CAMP OUT OF RANGE OR ABANDONED		
	(1,	[	
			(party_slot_eq,"p_main_party",slot_party_siege_camp,1),
			(try_begin),
				(lt, "$g_player_besiege_town", 1),
				(party_set_slot,"p_main_party",slot_party_siege_camp,0),
			(else_try),				
				(gt, "$g_player_besiege_town", 0),
				(store_distance_to_party_from_party, ":distance", "$g_player_besiege_town", "p_main_party"),
				(gt,":distance",3),
				(party_set_slot,"p_main_party",slot_party_siege_camp,0),
				(display_message,"@ Your siege camp was destroyed while you were away!"),
			(try_end),
		]),
		
####################################################################################################################################
# LAV MODIFICATIONS START (COMPANIONS OVERSEER MOD)
####################################################################################################################################
	(0,
		[
			(map_free),
			(this_or_next|key_clicked, key_o),
			(neq, "$g_lco_operation", 0),
			(try_begin),
				(this_or_next|key_clicked, key_o),
				(eq, "$g_lco_operation", lco_run_presentation),
				(assign, "$g_lco_operation", 0),
				(jump_to_menu, "mnu_lco_presentation"),
			(else_try),
				(eq, "$g_lco_operation", lco_view_character),
				(jump_to_menu, "mnu_lco_view_character"),
			(try_end),
		]

	),

  # Infinite prisoners escape trigger - MOBILE PARTIES (Player & NPC)
  # Processed every 12 hours
  (12,
   [
      (try_for_parties, ":party_no"),
          (party_is_active, ":party_no"),
          (party_get_num_prisoners, ":num_prisoners", ":party_no"),
          (gt, ":num_prisoners", 0),
          
          # Only mobile parties (not centers)
          (party_get_slot, ":spt", ":party_no", 0), # slot_party_type = 0
          (try_begin),
              (neg|is_between, ":spt", 2, 5), # Exclude Castle (2), Town (3), Village (4)
              
              (party_stack_get_troop_id, ":leader", ":party_no", 0),
              (assign, ":pm_skill", 0),
              (try_begin),
                  (gt, ":leader", 0),
                  (store_skill_level, ":pm_skill", "skl_prisoner_management", ":leader"),
              (try_end),

              # Reduced safely managed amount to 3 per skill level
              (store_mul, ":pm_bonus", ":pm_skill", 3),
              (store_sub, ":unmanaged", ":num_prisoners", ":pm_bonus"),
              (val_max, ":unmanaged", 0),
              
              # Formula: (unmanaged * unmanaged) / 1000
              (store_mul, ":unmanaged_sq", ":unmanaged", ":unmanaged"),
              (store_div, ":escape_chance", ":unmanaged_sq", 1000),
              
              # Guard factor: -1% per 2 troops in the party
              (party_get_num_companions, ":num_troops", ":party_no"),
              (store_div, ":guard_factor", ":num_troops", 2),
              (val_sub, ":escape_chance", ":guard_factor"),
              
              (val_max, ":escape_chance", 0),
              
              (store_random_in_range, ":rand", 0, 100),
              (lt, ":rand", ":escape_chance"),
              
              # Escape quantity logic: 5% to 15% missing per stack
              (store_random_in_range, ":escape_percent", 5, 16),
              
              (party_get_num_prisoner_stacks, ":num_stacks", ":party_no"),
              (try_for_range_backwards, ":stack_no", 0, ":num_stacks"),
                  (party_prisoner_stack_get_troop_id, ":troop_id", ":party_no", ":stack_no"),
                  (neg|troop_is_hero, ":troop_id"), 
                  (party_prisoner_stack_get_size, ":stack_size", ":party_no", ":stack_no"),
                  
                  (store_mul, ":to_remove", ":stack_size", ":escape_percent"),
                  (val_div, ":to_remove", 100),
                  
                  # Remainder chance
                  (store_random_in_range, ":rand2", 0, 100),
                  (try_begin),
                      (lt, ":rand2", ":escape_percent"),
                      (val_add, ":to_remove", 1),
                  (try_end),
                  
                  (val_min, ":to_remove", ":stack_size"),
                  (try_begin),
                      (gt, ":to_remove", 0),
                      (party_remove_prisoners, ":party_no", ":troop_id", ":to_remove"),
                      
                      (try_begin),
                          (eq, ":party_no", "p_main_party"),
                          (str_store_troop_name, s1, ":troop_id"),
                          (assign, reg1, ":to_remove"),
                          (try_begin),
                              (eq, ":to_remove", 1),
                              (display_message, "@{reg1} {s1} has escaped from your party!", 0xFFFF5533),
                          (else_try),
                              (str_store_troop_name_plural, s1, ":troop_id"),
                              (display_message, "@{reg1} {s1} have escaped from your party!", 0xFFFF5533),
                          (try_end),
                      (try_end),
                  (try_end),
              (try_end),
          (try_end),
      (try_end),
   ]),



####################################################################################################################################
# LAV MODIFICATIONS END (COMPANIONS OVERSEER MOD)
####################################################################################################################################

]
